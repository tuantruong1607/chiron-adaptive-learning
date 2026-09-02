from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from .qdrant import DenseEmbeddingUnavailable, Encoder, FastEmbedReranker, QdrantChunkIndex


@dataclass(slots=True)
class HybridRetriever:
    encoder: Encoder
    index: QdrantChunkIndex
    reranker: FastEmbedReranker | None = None

    def retrieve(
        self,
        query: str,
        *,
        tenant_id: str,
        course_id: str,
        candidate_limit: int,
        limit: int,
    ) -> dict:
        degraded = False
        try:
            dense, sparse = self.encoder.encode_query(query)
            candidates = self.index.hybrid_query(
                dense,
                sparse,
                tenant_id=tenant_id,
                course_id=course_id,
                candidate_limit=candidate_limit,
            )
        except DenseEmbeddingUnavailable as exc:
            degraded = True
            candidates = self.index.sparse_query(
                exc.sparse,
                tenant_id=tenant_id,
                course_id=course_id,
                candidate_limit=candidate_limit,
            )
        raw_candidate_count = len(candidates)
        reranked = self.reranker is not None and bool(candidates)
        if reranked:
            scores = self.reranker.scores(
                query, [str(item.get("payload", {}).get("content", "")) for item in candidates]
            )
            candidates = [
                {**item, "score": score}
                for item, score in zip(candidates, scores, strict=True)
            ]
            candidates.sort(key=lambda item: float(item.get("score", 0)), reverse=True)
        # Qdrant RRF can return equal-score points in a different order across identical
        # requests. Stabilize ties before source-span deduplication so the graph gate compares
        # the same semantic baseline and production citations do not flicker between calls.
        candidates.sort(
            key=lambda item: (-float(item.get("score", 0)), str(item.get("id", "")))
        )
        candidates = deduplicate_hits_by_source_span(candidates)
        return {
            "hits": candidates[:limit],
            "reranked": reranked,
            "candidate_count": len(candidates),
            "raw_candidate_count": raw_candidate_count,
            "degraded": degraded,
            "retrieval_mode": "bm25_only" if degraded else "hybrid",
        }


def _normalized_terms(text: str) -> set[str]:
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return set(re.findall(r"[\w]+", normalized, flags=re.UNICODE))


def _near_duplicate(left: str, right: str, threshold: float = 0.88) -> bool:
    left_terms = _normalized_terms(left)
    right_terms = _normalized_terms(right)
    if not left_terms or not right_terms:
        return left.strip().casefold() == right.strip().casefold()
    return len(left_terms & right_terms) / len(left_terms | right_terms) >= threshold


def _unique_subqueries(candidates: list[str], limit: int) -> list[str]:
    unique: list[str] = []
    for candidate in candidates:
        compact = " ".join(candidate.split())
        if not compact or any(_near_duplicate(compact, item) for item in unique):
            continue
        unique.append(compact)
        if len(unique) == limit:
            break
    return unique


def deduplicate_hits_by_source_span(hits: list[dict]) -> list[dict]:
    """Keep the highest-ranked child chunk for each immutable source span."""
    unique: list[dict] = []
    seen: set[str] = set()
    for hit in hits:
        payload = hit.get("payload") or {}
        identity = str(payload.get("source_span_id") or hit.get("id") or "")
        if not identity or identity in seen:
            continue
        seen.add(identity)
        unique.append(hit)
    return unique


def expand_subqueries(query: str, route: str, max_subqueries: int = 2) -> list[str]:
    if route == "direct":
        return [query]
    if route == "prerequisite":
        candidates = [
            query,
            f"{query} định nghĩa khái niệm nền tảng cần học trước",
        ]
    else:
        normalized = query.casefold()
        if any(term in normalized for term in ("so sánh", "khác nhau", "giống nhau")):
            expansion = f"{query} tiêu chí so sánh cơ chế ứng dụng"
        elif any(term in normalized for term in ("nguyên nhân", "kết quả", "dẫn đến", "ảnh hưởng")):
            expansion = f"{query} cơ chế điều kiện hệ quả"
        else:
            expansion = f"{query} mối quan hệ giữa các khái niệm và ứng dụng"
        candidates = [query, expansion]
    return _unique_subqueries(candidates, max_subqueries)


@dataclass(slots=True)
class AdaptiveRetriever:
    hybrid: HybridRetriever
    rrf_k: int = 60

    def retrieve(
        self,
        query: str,
        *,
        tenant_id: str,
        course_id: str,
        route: str,
        direct_candidate_limit: int,
        direct_limit: int,
        multi_hop_candidate_limit: int,
        multi_hop_limit: int,
        max_subqueries: int,
    ) -> dict:
        subqueries = expand_subqueries(query, route, max_subqueries)
        if len(subqueries) == 1:
            candidate_limit = (
                direct_candidate_limit if route == "direct" else multi_hop_candidate_limit
            )
            limit = direct_limit if route == "direct" else multi_hop_limit
            result = self.hybrid.retrieve(
                query,
                tenant_id=tenant_id,
                course_id=course_id,
                candidate_limit=candidate_limit,
                limit=limit,
            )
            return {
                **result,
                "route": route,
                "strategy": "single_hybrid",
                "subqueries": subqueries,
            }

        fused: dict[str, dict] = {}
        degraded = False
        reranked = False
        modes: set[str] = set()
        total_candidates = 0
        for subquery in subqueries:
            result = self.hybrid.retrieve(
                subquery,
                tenant_id=tenant_id,
                course_id=course_id,
                candidate_limit=multi_hop_candidate_limit,
                limit=multi_hop_candidate_limit,
            )
            degraded = degraded or bool(result.get("degraded"))
            reranked = reranked or bool(result.get("reranked"))
            modes.add(str(result.get("retrieval_mode", "hybrid")))
            total_candidates += int(result.get("candidate_count", len(result.get("hits", []))))
            for rank, hit in enumerate(result.get("hits", []), start=1):
                payload = hit.get("payload") or {}
                identity = str(payload.get("source_span_id") or hit.get("id"))
                score = 1.0 / (self.rrf_k + rank)
                if identity not in fused:
                    fused[identity] = {**hit, "score": score}
                else:
                    fused[identity]["score"] = float(fused[identity]["score"]) + score

        hits = sorted(fused.values(), key=lambda item: float(item["score"]), reverse=True)
        max_rrf_score = len(subqueries) / (self.rrf_k + 1)
        for hit in hits:
            hit["score"] = min(float(hit["score"]) / max_rrf_score, 1.0)
        return {
            "hits": hits[:multi_hop_limit],
            "reranked": reranked,
            "candidate_count": total_candidates,
            "degraded": degraded,
            "retrieval_mode": "bm25_only" if modes == {"bm25_only"} else "hybrid",
            "route": route,
            "strategy": "multi_query_hybrid_rrf",
            "subqueries": subqueries,
        }
