import asyncio

from chiron_worker.ragas_eval import add_ragas_id_metrics


def test_ragas_id_metrics_respect_required_and_acceptable_policy() -> None:
    rows = [
        {
            "query": "RRF là gì?",
            "retrieved_source_span_ids": ["alternate", "required", "noise", "noise"],
            "required_source_span_ids": ["required", "missing-required"],
            "acceptable_source_span_ids": ["alternate"],
        }
    ]

    result = asyncio.run(add_ragas_id_metrics(rows))[0]

    assert result["ragas_id_context_precision"] == 2 / 3
    assert result["ragas_id_context_recall"] == 0.5
