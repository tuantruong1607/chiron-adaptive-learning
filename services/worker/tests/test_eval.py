from chiron_worker.eval import quality_gates, ranking_metrics, summarize


def _hit(source_span_id: str) -> dict:
    return {"payload": {"source_span_id": source_span_id}}


def test_ranking_metrics_support_required_and_acceptable_sources() -> None:
    result = ranking_metrics(
        [_hit("noise"), _hit("alternate"), _hit("required-a")],
        ["required-a", "required-b"],
        ["alternate"],
        top_k=3,
    )

    assert result["hit_at_k"] is True
    assert result["required_recall_at_k"] == 0.5
    assert result["mrr_at_k"] == 0.5
    assert result["first_relevant_rank"] == 2
    assert result["source_precision_at_k"] == 2 / 3


def test_summarize_reports_quality_and_latency() -> None:
    rows = [
        {
            "hit_at_k": True,
            "required_recall_at_k": 1.0,
            "mrr_at_k": 1.0,
            "ndcg_at_k": 1.0,
            "source_precision_at_k": 0.5,
            "retrieval_latency_ms": 10.0,
        },
        {
            "hit_at_k": False,
            "required_recall_at_k": 0.0,
            "mrr_at_k": 0.0,
            "ndcg_at_k": 0.0,
            "source_precision_at_k": 0.0,
            "retrieval_latency_ms": 30.0,
        },
    ]

    result = summarize(rows)

    assert result["cases"] == 2
    assert result["hit_at_k"] == 0.5
    assert result["retrieval_latency_p50_ms"] == 10.0
    assert result["retrieval_latency_p95_ms"] == 30.0


def test_ranking_metrics_collapses_duplicate_child_chunks_by_source_span() -> None:
    result = ranking_metrics(
        [_hit("duplicate"), _hit("duplicate"), _hit("required")],
        ["required"],
        top_k=2,
    )

    assert result["retrieved_source_span_ids"] == ["duplicate", "required"]
    assert result["hit_at_k"] is True
    assert result["first_relevant_rank"] == 2


def test_quality_gates_compare_adaptive_by_query_class() -> None:
    report = {
        "dataset_coverage": {
            "total": 50,
            "by_class": {"direct": 20, "prerequisite": 15, "multi_hop": 15},
            "by_interaction_type": {"user_question": 50},
        },
        "review_status": {"approved": 50},
        "expected_coverage": {
            "total": 50,
            "by_class": {"direct": 20, "prerequisite": 15, "multi_hop": 15},
        },
        "modes": {
            "hybrid": {
                "overall": {"end_to_end_latency_p95_ms": 250},
                "by_class": {
                    "direct": {"required_recall_at_k": 0.8},
                    "prerequisite": {"required_recall_at_k": 0.4},
                    "multi_hop": {"required_recall_at_k": 0.5},
                }
            },
            "adaptive": {
                "overall": {"end_to_end_latency_p95_ms": 420},
                "by_class": {
                    "direct": {"required_recall_at_k": 0.79},
                    "prerequisite": {"required_recall_at_k": 0.5},
                    "multi_hop": {"required_recall_at_k": 0.6},
                }
            },
        },
    }

    result = quality_gates(report)

    assert result["passed"] is True


def test_quality_gates_reject_assessment_items_in_retrieval_suite() -> None:
    report = {
        "dataset_coverage": {
            "total": 50,
            "by_class": {"direct": 20, "prerequisite": 15, "multi_hop": 15},
            "by_interaction_type": {"user_question": 49, "assessment_item": 1},
        },
        "review_status": {"approved": 50},
        "expected_coverage": {
            "total": 50,
            "by_class": {"direct": 20, "prerequisite": 15, "multi_hop": 15},
        },
        "modes": {},
    }

    result = quality_gates(report)

    scope_gate = next(
        check
        for check in result["checks"]
        if check["name"] == "retrieval_suite_contains_only_user_questions"
    )
    assert scope_gate["passed"] is False
    assert result["passed"] is False


def test_quality_gates_compare_graph_lite_without_direct_regression() -> None:
    report = {
        "dataset_coverage": {
            "total": 15,
            "by_class": {"direct": 5, "prerequisite": 5, "multi_hop": 5},
            "by_interaction_type": {"user_question": 15},
        },
        "expected_coverage": {
            "total": 15,
            "by_class": {"direct": 5, "prerequisite": 5, "multi_hop": 5},
        },
        "review_status": {"approved": 15},
        "modes": {
            "hybrid": {
                "overall": {"end_to_end_latency_p95_ms": 200},
                "by_class": {
                    "direct": {"required_recall_at_k": 0.8},
                    "prerequisite": {"required_recall_at_k": 0.4},
                    "multi_hop": {"required_recall_at_k": 0.4},
                },
            },
            "graph_lite": {
                "overall": {"end_to_end_latency_p95_ms": 260},
                "by_class": {
                    "direct": {"required_recall_at_k": 0.8},
                    "prerequisite": {"required_recall_at_k": 0.5},
                    "multi_hop": {"required_recall_at_k": 0.5},
                },
            },
        },
    }

    result = quality_gates(report)

    assert result["passed"] is True
