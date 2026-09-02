from app.retrieval import response_from_task, route_query


def test_route_query_uses_single_search_for_narrow_question() -> None:
    assert route_query("RRF là gì?") == "direct"


def test_route_query_escalates_relationship_and_prerequisite_questions() -> None:
    assert route_query("So sánh dense retrieval và sparse retrieval") == "multi_hop"
    assert route_query("Vì sao chunking ảnh hưởng đến citation?") == "multi_hop"
    assert route_query("Kiến thức nền tảng trước khi học reranking") == "prerequisite"


def test_retrieval_task_response_preserves_source_provenance() -> None:
    response = response_from_task(
        "Giải thích RRF",
        {
            "hits": [
                {
                    "id": "chunk-1",
                    "score": 0.82,
                    "payload": {
                        "content": "RRF hợp nhất các danh sách theo thứ hạng.",
                        "source_span_id": "span-1",
                        "document_title": "Day 04 — Hybrid Search",
                        "source_path": "slides/day04.pdf",
                        "locator": {"pdf_page": 12, "section": "Reciprocal Rank Fusion"},
                    },
                }
            ]
        },
    )

    hit = response.hits[0]
    assert hit.concept_id is None
    assert hit.citation.source_span_id == "span-1"
    assert hit.citation.title == "Day 04 — Hybrid Search"
    assert hit.citation.locator == "trang 12 · Reciprocal Rank Fusion"
    assert hit.citation.excerpt == hit.text
    assert response.retrieval_mode == "hybrid"
    assert response.degraded is False
    assert response.strategy == "single_hybrid"
    assert response.subqueries == ["Giải thích RRF"]


def test_retrieval_task_response_exposes_bm25_degraded_mode() -> None:
    response = response_from_task(
        "OpenAI đang rate limit",
        {"hits": [], "retrieval_mode": "bm25_only", "degraded": True},
    )

    assert response.retrieval_mode == "bm25_only"
    assert response.degraded is True


def test_retrieval_task_response_preserves_adaptive_route_metadata() -> None:
    response = response_from_task(
        "So sánh dense và sparse",
        {
            "hits": [],
            "route": "multi_hop",
            "strategy": "multi_query_hybrid_rrf",
            "subqueries": ["q1", "q2", "q3"],
        },
    )
    assert response.route == "multi_hop"
    assert response.strategy == "multi_query_hybrid_rrf"
    assert response.subqueries == ["q1", "q2", "q3"]


def test_retrieval_task_response_accepts_graph_lite_strategy() -> None:
    response = response_from_task(
        "multi-hop retrieval",
        {
            "hits": [],
            "route": "multi_hop",
            "strategy": "graph_lite_2hop",
            "subqueries": ["multi-hop retrieval"],
        },
    )

    assert response.strategy == "graph_lite_2hop"
