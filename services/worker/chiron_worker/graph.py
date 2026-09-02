from __future__ import annotations

from dataclasses import dataclass, field
from time import monotonic
from typing import Any

import psycopg

from .retrieval import AdaptiveRetriever, deduplicate_hits_by_source_span

ALLOWED_REVIEW_STATUSES = frozenset({"candidate", "approved", "active"})
MULTI_HOP_RELATIONS = (
    "prerequisite_of",
    "part_of",
    "contrasts_with",
    "causes",
    "applies_to",
    "related_to",
)


@dataclass(frozen=True, slots=True)
class GraphSource:
    source_span_id: str
    concept_id: str
    depth: int
    confidence: float


@dataclass(slots=True)
class _GraphReadModel:
    loaded_at: float
    source_to_concepts: dict[str, set[str]] = field(default_factory=dict)
    concept_to_sources: dict[str, list[tuple[str, float]]] = field(default_factory=dict)
    prerequisites: dict[str, list[tuple[str, float]]] = field(default_factory=dict)
    neighbors: dict[str, list[tuple[str, float]]] = field(default_factory=dict)


class GraphStore:
    def __init__(self, database_url: str) -> None:
        self.database_url = database_url.replace("postgresql+psycopg://", "postgresql://", 1)
        self._read_models: dict[tuple[str, str, str, tuple[str, ...]], _GraphReadModel] = {}

    def _read_model(
        self,
        *,
        tenant_id: str,
        course_id: str,
        review_statuses: tuple[str, ...],
        graph_version_status: str,
    ) -> _GraphReadModel | None:
        key = (tenant_id, course_id, graph_version_status, review_statuses)
        cached = self._read_models.get(key)
        # An approved draft is immutable for the duration of an evaluation run,
        # while the active pointer may change during a release. Keep draft reads
        # warm long enough for a full gate without delaying active-version pickup.
        cache_ttl_seconds = 300 if graph_version_status == "draft" else 30
        if cached is not None and monotonic() - cached.loaded_at < cache_ttl_seconds:
            return cached
        with psycopg.connect(self.database_url) as connection:
            connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
            version_row = connection.execute(
                """
                SELECT id::text
                FROM graph_versions
                WHERE tenant_id=%s AND course_id=%s AND status=%s
                ORDER BY updated_at DESC, created_at DESC
                LIMIT 1
                """,
                (tenant_id, course_id, graph_version_status),
            ).fetchone()
            if version_row is None:
                return None
            graph_version_id = str(version_row[0])
            links = connection.execute(
                """
                SELECT DISTINCT c.source_span_id::text, cc.concept_id::text, cc.confidence
                FROM chunk_concepts cc
                JOIN chunks c ON c.id=cc.chunk_id
                JOIN concept_nodes n ON n.id=cc.concept_id
                WHERE cc.tenant_id=%s AND cc.graph_version_id=%s
                  AND cc.review_status=ANY(%s) AND n.review_status=ANY(%s)
                  AND c.is_active=true
                """,
                (
                    tenant_id,
                    graph_version_id,
                    list(review_statuses),
                    list(review_statuses),
                ),
            ).fetchall()
            edges = connection.execute(
                """
                SELECT e.source_concept_id::text, e.target_concept_id::text,
                       e.relation_type, e.confidence
                FROM concept_edges e
                JOIN concept_nodes source_node ON source_node.id=e.source_concept_id
                JOIN concept_nodes target_node ON target_node.id=e.target_concept_id
                WHERE e.tenant_id=%s AND e.graph_version_id=%s
                  AND e.review_status=ANY(%s)
                  AND source_node.review_status=ANY(%s)
                  AND target_node.review_status=ANY(%s)
                """,
                (
                    tenant_id,
                    graph_version_id,
                    list(review_statuses),
                    list(review_statuses),
                    list(review_statuses),
                ),
            ).fetchall()
        model = _GraphReadModel(loaded_at=monotonic())
        for source_span_id, concept_id, confidence in links:
            span_id = str(source_span_id)
            concept = str(concept_id)
            model.source_to_concepts.setdefault(span_id, set()).add(concept)
            model.concept_to_sources.setdefault(concept, []).append(
                (span_id, float(confidence))
            )
        for source_id, target_id, relation, confidence in edges:
            source = str(source_id)
            target = str(target_id)
            edge_confidence = float(confidence)
            if relation == "prerequisite_of":
                model.prerequisites.setdefault(target, []).append(
                    (source, edge_confidence)
                )
            if relation in MULTI_HOP_RELATIONS:
                model.neighbors.setdefault(source, []).append((target, edge_confidence))
                model.neighbors.setdefault(target, []).append((source, edge_confidence))
        self._read_models[key] = model
        return model

    @staticmethod
    def _validate_statuses(review_statuses: tuple[str, ...]) -> tuple[str, ...]:
        statuses = tuple(dict.fromkeys(review_statuses))
        if not statuses or not set(statuses) <= ALLOWED_REVIEW_STATUSES:
            raise ValueError(f"Invalid graph review statuses: {review_statuses}")
        return statuses

    def expand_source_spans(
        self,
        seed_source_span_ids: list[str],
        *,
        tenant_id: str,
        course_id: str,
        route: str,
        max_hops: int,
        review_statuses: tuple[str, ...] = ("active",),
        graph_version_status: str = "active",
    ) -> list[GraphSource]:
        if route == "direct" or not seed_source_span_ids or max_hops < 1:
            return []
        statuses = self._validate_statuses(review_statuses)
        max_hops = min(max_hops, 2)
        model = self._read_model(
            tenant_id=tenant_id,
            course_id=course_id,
            review_statuses=statuses,
            graph_version_status=graph_version_status,
        )
        if model is None:
            return []
        seed_concepts = {
            concept_id
            for span_id in seed_source_span_ids
            for concept_id in model.source_to_concepts.get(span_id, set())
        }
        if not seed_concepts:
            return []
        visited = set(seed_concepts)
        frontier = {concept_id: 1.0 for concept_id in seed_concepts}
        reached: dict[str, tuple[int, float]] = {}
        for depth in range(1, max_hops + 1):
            next_frontier: dict[str, float] = {}
            for concept_id, path_confidence in frontier.items():
                neighbors = (
                    model.prerequisites.get(concept_id, [])
                    if route == "prerequisite"
                    else model.neighbors.get(concept_id, [])
                )
                for neighbor_id, edge_confidence in neighbors:
                    if neighbor_id in visited:
                        continue
                    confidence = min(path_confidence, edge_confidence)
                    next_frontier[neighbor_id] = max(
                        next_frontier.get(neighbor_id, 0.0), confidence
                    )
                    current = reached.get(neighbor_id)
                    if current is None or confidence > current[1]:
                        reached[neighbor_id] = (depth, confidence)
            if not next_frontier:
                break
            visited.update(next_frontier)
            frontier = next_frontier
        if not reached:
            return []
        seed_spans = set(seed_source_span_ids)
        sources: list[GraphSource] = []
        for concept_id, (depth, edge_confidence) in reached.items():
            for span_id, link_confidence in model.concept_to_sources.get(concept_id, []):
                if span_id in seed_spans:
                    continue
                sources.append(
                    GraphSource(
                        source_span_id=span_id,
                        concept_id=concept_id,
                        depth=depth,
                        confidence=min(link_confidence, edge_confidence),
                    )
                )
        sources.sort(key=lambda item: (item.depth, -item.confidence, item.source_span_id))
        return sources

    def prerequisite_cycles(
        self,
        *,
        tenant_id: str,
        course_id: str,
        review_statuses: tuple[str, ...] = ("candidate", "approved", "active"),
        graph_version_status: str = "draft",
    ) -> list[list[str]]:
        statuses = self._validate_statuses(review_statuses)
        with psycopg.connect(self.database_url) as connection:
            connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
            rows = connection.execute(
                """
                SELECT s.normalized_name, t.normalized_name
                FROM concept_edges e
                JOIN concept_nodes s ON s.id=e.source_concept_id
                JOIN concept_nodes t ON t.id=e.target_concept_id
                JOIN graph_versions g ON g.id=e.graph_version_id
                WHERE e.tenant_id=%s AND g.course_id=%s AND g.status=%s
                  AND e.relation_type='prerequisite_of'
                  AND e.review_status=ANY(%s)
                """,
                (tenant_id, course_id, graph_version_status, list(statuses)),
            ).fetchall()
        adjacency: dict[str, set[str]] = {}
        for source, target in rows:
            adjacency.setdefault(str(source), set()).add(str(target))
            adjacency.setdefault(str(target), set())
        cycles: list[list[str]] = []
        visiting: list[str] = []
        visited: set[str] = set()

        def visit(node: str) -> None:
            if node in visiting:
                start = visiting.index(node)
                cycles.append([*visiting[start:], node])
                return
            if node in visited:
                return
            visiting.append(node)
            for neighbor in adjacency.get(node, set()):
                visit(neighbor)
            visiting.pop()
            visited.add(node)

        for node in adjacency:
            visit(node)
        return cycles


@dataclass(slots=True)
class GraphLiteRetriever:
    adaptive: AdaptiveRetriever
    graph_store: GraphStore
    index: Any

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
        graph_max_hops: int = 2,
        graph_expansion_limit: int = 8,
        graph_review_statuses: tuple[str, ...] = ("active",),
        graph_version_status: str = "active",
    ) -> dict[str, Any]:
        base = self.adaptive.retrieve(
            query,
            tenant_id=tenant_id,
            course_id=course_id,
            route=route,
            direct_candidate_limit=direct_candidate_limit,
            direct_limit=direct_limit,
            multi_hop_candidate_limit=multi_hop_candidate_limit,
            multi_hop_limit=multi_hop_limit,
            max_subqueries=max_subqueries,
        )
        if route == "direct":
            return {**base, "graph_expanded": False, "graph_sources": []}
        final_limit = multi_hop_limit
        seed_spans = [
            str((hit.get("payload") or {}).get("source_span_id") or "")
            for hit in base.get("hits", [])[:5]
        ]
        sources = self.graph_store.expand_source_spans(
            [span_id for span_id in seed_spans if span_id],
            tenant_id=tenant_id,
            course_id=course_id,
            route=route,
            max_hops=1 if route == "prerequisite" else graph_max_hops,
            review_statuses=graph_review_statuses,
            graph_version_status=graph_version_status,
        )[:graph_expansion_limit]
        if not sources:
            return {
                **base,
                "strategy": "graph_lite_no_expansion",
                "graph_expanded": False,
                "graph_sources": [],
            }
        source_scores = {
            item.source_span_id: 0.82 * item.confidence * (0.85 ** (item.depth - 1))
            for item in sources
        }
        graph_hits = self.index.fetch_by_source_span_ids(
            [item.source_span_id for item in sources],
            tenant_id=tenant_id,
            course_id=course_id,
            limit=graph_expansion_limit,
        )
        semantic_hits = [{**hit, "retrieval_origin": "semantic"} for hit in base.get("hits", [])]
        expanded_hits = []
        for hit in graph_hits:
            payload = hit.get("payload") or {}
            source_span_id = str(payload.get("source_span_id") or "")
            expanded_hits.append(
                {
                    **hit,
                    "score": source_scores.get(source_span_id, 0.0),
                    "retrieval_origin": "graph",
                }
            )
        baseline = deduplicate_hits_by_source_span(semantic_hits)[:final_limit]
        baseline_source_ids = {
            str((hit.get("payload") or {}).get("source_span_id") or "") for hit in baseline
        }
        graph_fill = [
            hit
            for hit in sorted(expanded_hits, key=lambda hit: float(hit.get("score", 0)), reverse=True)
            if str((hit.get("payload") or {}).get("source_span_id") or "") not in baseline_source_ids
        ]
        # Graph expansion is additive: it may fill missing baseline slots but must not evict
        # semantic evidence. This makes the activation gate enforceable at runtime, not only
        # in offline evaluation.
        merged = [*baseline, *graph_fill[: max(0, final_limit - len(baseline))]]
        return {
            **base,
            "hits": merged,
            "strategy": f"graph_lite_{1 if route == 'prerequisite' else graph_max_hops}hop",
            "graph_expanded": bool(expanded_hits),
            "graph_sources": [
                {
                    "source_span_id": item.source_span_id,
                    "concept_id": item.concept_id,
                    "depth": item.depth,
                    "confidence": item.confidence,
                }
                for item in sources
            ],
        }
