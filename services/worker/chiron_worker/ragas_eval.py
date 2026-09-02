from __future__ import annotations

import warnings
from typing import Any

from ragas import EvaluationDataset

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    # Ragas 0.4.3 advertises collections imports, but the ID metrics are still
    # exported only from ragas.metrics. Keep this compatibility boundary local.
    from ragas.metrics import IDBasedContextPrecision, IDBasedContextRecall


def _unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


async def add_ragas_id_metrics(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Score retrieval rows with Ragas while preserving Chiron's source policy.

    Precision counts required and acceptable spans as relevant. Recall uses only
    required spans because acceptable spans are alternatives, not mandatory
    evidence that every query must retrieve.
    """

    precision_samples: list[dict[str, Any]] = []
    recall_samples: list[dict[str, Any]] = []
    for row in rows:
        retrieved = _unique([str(value) for value in row["retrieved_source_span_ids"]])
        required = _unique([str(value) for value in row["required_source_span_ids"]])
        acceptable = _unique([str(value) for value in row["acceptable_source_span_ids"]])
        base = {"user_input": str(row["query"]), "retrieved_context_ids": retrieved}
        precision_samples.append(
            {**base, "reference_context_ids": _unique(required + acceptable)}
        )
        recall_samples.append({**base, "reference_context_ids": required})

    precision_dataset = EvaluationDataset.from_list(
        precision_samples, name="chiron_retrieval_precision"
    )
    recall_dataset = EvaluationDataset.from_list(
        recall_samples, name="chiron_retrieval_recall"
    )
    precision_metric = IDBasedContextPrecision()
    recall_metric = IDBasedContextRecall()
    scored: list[dict[str, Any]] = []
    for row, precision_sample, recall_sample in zip(
        rows, precision_dataset.samples, recall_dataset.samples, strict=True
    ):
        precision = await precision_metric.single_turn_ascore(precision_sample)
        recall = await recall_metric.single_turn_ascore(recall_sample)
        scored.append(
            {
                **row,
                "ragas_id_context_precision": float(precision),
                "ragas_id_context_recall": float(recall),
            }
        )
    return scored
