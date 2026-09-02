from chiron_worker.qdrant import DenseEmbeddingUnavailable, SparseVector
from chiron_worker.retrieval import (
    AdaptiveRetriever,
    HybridRetriever,
    deduplicate_hits_by_source_span,
    expand_subqueries,
)


class FakeEncoder:
    def encode_query(self, query):
        assert query == "RRF khác weighted sum thế nào?"
        return [0.4, 0.6], SparseVector([3, 8], [1.0, 0.5])


class FakeIndex:
    def __init__(self):
        self.scope = None

    def hybrid_query(self, dense, sparse, **scope):
        assert dense == [0.4, 0.6]
        assert sparse.indices == [3, 8]
        self.scope = scope
        return [
            {"id": "a", "score": 0.7, "payload": {"content": "weighted sum"}},
            {"id": "b", "score": 0.6, "payload": {"content": "reciprocal rank fusion"}},
        ]


class FakeReranker:
    def scores(self, query, documents):
        assert query == "RRF khác weighted sum thế nào?"
        assert documents == ["weighted sum", "reciprocal rank fusion"]
        return [0.1, 0.9]


def test_hybrid_retrieval_enforces_tenant_course_scope_and_reranks() -> None:
    index = FakeIndex()
    result = HybridRetriever(FakeEncoder(), index, FakeReranker()).retrieve(
        "RRF khác weighted sum thế nào?",
        tenant_id="tenant-1",
        course_id="course-1",
        candidate_limit=24,
        limit=1,
    )

    assert index.scope == {
        "tenant_id": "tenant-1",
        "course_id": "course-1",
        "candidate_limit": 24,
    }
    assert result["reranked"] is True
    assert result["candidate_count"] == 2
    assert result["hits"] == [
        {"id": "b", "score": 0.9, "payload": {"content": "reciprocal rank fusion"}}
    ]


def test_hybrid_retrieval_can_use_rrf_without_cross_encoder() -> None:
    result = HybridRetriever(FakeEncoder(), FakeIndex()).retrieve(
        "RRF khác weighted sum thế nào?",
        tenant_id="tenant-1",
        course_id="course-1",
        candidate_limit=12,
        limit=2,
    )

    assert result["reranked"] is False
    assert [hit["id"] for hit in result["hits"]] == ["a", "b"]
    assert result["retrieval_mode"] == "hybrid"
    assert result["degraded"] is False


def test_source_span_dedup_happens_before_top_k() -> None:
    hits = [
        {"id": "a1", "payload": {"source_span_id": "span-a"}},
        {"id": "a2", "payload": {"source_span_id": "span-a"}},
        {"id": "b1", "payload": {"source_span_id": "span-b"}},
    ]

    assert [item["id"] for item in deduplicate_hits_by_source_span(hits)[:2]] == ["a1", "b1"]


def test_subquery_expansion_is_bounded_and_direct_is_never_expanded() -> None:
    assert expand_subqueries("Vì sao RRF dùng thứ hạng?", "direct", 3) == [
        "Vì sao RRF dùng thứ hạng?"
    ]
    expanded = expand_subqueries("So sánh dense và sparse", "multi_hop", 3)
    assert len(expanded) == 2
    assert len(set(expanded)) == 2


class UnavailableDenseEncoder:
    def encode_query(self, query):
        raise DenseEmbeddingUnavailable(SparseVector([7], [1.0]))


class SparseFallbackIndex:
    def sparse_query(self, sparse, **scope):
        assert sparse == SparseVector([7], [1.0])
        assert scope == {
            "tenant_id": "tenant-1",
            "course_id": "course-1",
            "candidate_limit": 12,
        }
        return [{"id": "bm25", "score": 0.5, "payload": {"content": "fallback"}}]


def test_openai_failure_degrades_to_tenant_scoped_bm25() -> None:
    result = HybridRetriever(UnavailableDenseEncoder(), SparseFallbackIndex()).retrieve(
        "RRF khác weighted sum thế nào?",
        tenant_id="tenant-1",
        course_id="course-1",
        candidate_limit=12,
        limit=2,
    )

    assert result["retrieval_mode"] == "bm25_only"
    assert result["degraded"] is True
    assert result["reranked"] is False
    assert [hit["id"] for hit in result["hits"]] == ["bm25"]


class RecordingHybrid:
    def __init__(self):
        self.queries = []

    def retrieve(self, query, **scope):
        self.queries.append((query, scope))
        shared = {
            "id": f"shared-{len(self.queries)}",
            "score": 0.8,
            "payload": {"source_span_id": "span-shared", "content": "shared"},
        }
        unique = {
            "id": f"unique-{len(self.queries)}",
            "score": 0.7,
            "payload": {
                "source_span_id": f"span-{len(self.queries)}",
                "content": query,
            },
        }
        return {
            "hits": [shared, unique],
            "candidate_count": 2,
            "reranked": False,
            "degraded": False,
            "retrieval_mode": "hybrid",
        }


def test_adaptive_retrieval_keeps_direct_question_to_one_search() -> None:
    hybrid = RecordingHybrid()
    result = AdaptiveRetriever(hybrid).retrieve(
        "RRF là gì?",
        tenant_id="tenant-1",
        course_id="course-1",
        route="direct",
        direct_candidate_limit=16,
        direct_limit=5,
        multi_hop_candidate_limit=12,
        multi_hop_limit=8,
        max_subqueries=3,
    )
    assert len(hybrid.queries) == 1
    assert result["strategy"] == "single_hybrid"


def test_adaptive_retrieval_can_disable_expansion_for_non_direct_routes() -> None:
    hybrid = RecordingHybrid()
    result = AdaptiveRetriever(hybrid).retrieve(
        "Cần học gì trước RRF?",
        tenant_id="tenant-1",
        course_id="course-1",
        route="prerequisite",
        direct_candidate_limit=16,
        direct_limit=5,
        multi_hop_candidate_limit=12,
        multi_hop_limit=8,
        max_subqueries=1,
    )
    assert len(hybrid.queries) == 1
    assert result["strategy"] == "single_hybrid"
    assert result["route"] == "prerequisite"


def test_adaptive_retrieval_fuses_multi_hop_results_by_source_span() -> None:
    hybrid = RecordingHybrid()
    result = AdaptiveRetriever(hybrid).retrieve(
        "So sánh dense và sparse",
        tenant_id="tenant-1",
        course_id="course-1",
        route="multi_hop",
        direct_candidate_limit=16,
        direct_limit=5,
        multi_hop_candidate_limit=12,
        multi_hop_limit=8,
        max_subqueries=3,
    )
    assert len(hybrid.queries) == 2
    assert result["strategy"] == "multi_query_hybrid_rrf"
    assert result["hits"][0]["payload"]["source_span_id"] == "span-shared"
    assert result["hits"][0]["score"] == 1.0
    assert len(result["hits"]) == 3
