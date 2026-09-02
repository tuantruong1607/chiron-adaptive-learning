from __future__ import annotations

from math import log2
from statistics import fmean
from typing import Any


def ranking_metrics(
    hits: list[dict[str, Any]],
    required_source_span_ids: list[str],
    acceptable_source_span_ids: list[str] | None = None,
    *,
    top_k: int,
) -> dict[str, float | int | bool | list[str]]:
    required = set(required_source_span_ids)
    relevant = required | set(acceptable_source_span_ids or [])
    retrieved: list[str] = []
    seen: set[str] = set()
    for hit in hits:
        source_id = str(hit.get("payload", {}).get("source_span_id") or "")
        if not source_id or source_id in seen:
            continue
        seen.add(source_id)
        retrieved.append(source_id)
        if len(retrieved) == top_k:
            break
    relevant_ranks = [rank for rank, source_id in enumerate(retrieved, start=1) if source_id in relevant]
    retrieved_required = required.intersection(retrieved)
    dcg = sum(1.0 / log2(rank + 1) for rank in relevant_ranks)
    ideal_count = min(len(relevant), top_k)
    ideal_dcg = sum(1.0 / log2(rank + 1) for rank in range(1, ideal_count + 1))
    return {
        "hit_at_k": bool(relevant_ranks),
        "required_recall_at_k": len(retrieved_required) / len(required) if required else 1.0,
        "mrr_at_k": 1.0 / relevant_ranks[0] if relevant_ranks else 0.0,
        "ndcg_at_k": dcg / ideal_dcg if ideal_dcg else 0.0,
        "source_precision_at_k": (
            sum(source_id in relevant for source_id in retrieved) / len(retrieved)
            if retrieved
            else 0.0
        ),
        "first_relevant_rank": relevant_ranks[0] if relevant_ranks else 0,
        "retrieved_source_span_ids": retrieved,
    }


def percentile(values: list[float], quantile: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = round((len(ordered) - 1) * quantile)
    return ordered[index]


def summarize(results: list[dict[str, Any]]) -> dict[str, float | int]:
    if not results:
        return {"cases": 0}
    metric_names = (
        "hit_at_k",
        "required_recall_at_k",
        "mrr_at_k",
        "ndcg_at_k",
        "source_precision_at_k",
        "ragas_id_context_precision",
        "ragas_id_context_recall",
    )
    summary: dict[str, float | int] = {"cases": len(results)}
    for name in metric_names:
        values = [float(result[name]) for result in results if name in result]
        if values:
            summary[name] = fmean(values)
    latencies = [float(result["retrieval_latency_ms"]) for result in results]
    summary["retrieval_latency_p50_ms"] = percentile(latencies, 0.50)
    summary["retrieval_latency_p95_ms"] = percentile(latencies, 0.95)
    end_to_end = [
        float(result["end_to_end_latency_ms"])
        for result in results
        if "end_to_end_latency_ms" in result
    ]
    if end_to_end:
        summary["end_to_end_latency_p50_ms"] = percentile(end_to_end, 0.50)
        summary["end_to_end_latency_p95_ms"] = percentile(end_to_end, 0.95)
    return summary


def quality_gates(report: dict[str, Any]) -> dict[str, Any]:
    modes = report.get("modes", {})
    coverage = report.get("dataset_coverage", {})
    checks: list[dict[str, Any]] = []

    def add(name: str, passed: bool, actual: Any, expected: str) -> None:
        checks.append(
            {"name": name, "passed": passed, "actual": actual, "expected": expected}
        )

    expected_coverage = report.get(
        "expected_coverage",
        {"total": 50, "by_class": {"direct": 20, "prerequisite": 15, "multi_hop": 15}},
    )
    expected_total = int(expected_coverage.get("total", 50))
    add(
        "dataset_has_expected_cases",
        int(coverage.get("total", 0)) == expected_total,
        coverage.get("total"),
        f"= {expected_total}",
    )
    total = int(coverage.get("total", 0))
    resolved = int(report.get("label_status", {}).get("resolved", total))
    add("all_cases_have_resolved_source_labels", resolved == total, resolved, f"= {total}")
    user_questions = int(coverage.get("by_interaction_type", {}).get("user_question", 0))
    add(
        "retrieval_suite_contains_only_user_questions",
        user_questions == total,
        user_questions,
        f"= {total}",
    )
    for query_class in ("direct", "prerequisite", "multi_hop"):
        minimum = int(expected_coverage.get("by_class", {}).get(query_class, 0))
        actual = int(coverage.get("by_class", {}).get(query_class, 0))
        add(f"coverage_{query_class}", actual == minimum, actual, f"= {minimum}")

    hybrid = modes.get("hybrid", {}).get("by_class", {})
    adaptive = modes.get("adaptive", {}).get("by_class", {})
    if hybrid and adaptive:
        adaptive_p95 = float(
            modes.get("adaptive", {}).get("overall", {}).get("end_to_end_latency_p95_ms", 0)
        )
        add(
            "adaptive_p95_within_budget",
            0 < adaptive_p95 <= 500,
            round(adaptive_p95, 1),
            "<= 500 ms",
        )
        direct_hybrid = float(hybrid.get("direct", {}).get("required_recall_at_k", 0))
        direct_adaptive = float(adaptive.get("direct", {}).get("required_recall_at_k", 0))
        add(
            "adaptive_direct_no_material_regression",
            direct_adaptive >= direct_hybrid - 0.02,
            round(direct_adaptive - direct_hybrid, 4),
            ">= -0.02 recall delta",
        )
        for query_class in ("prerequisite", "multi_hop"):
            baseline = float(hybrid.get(query_class, {}).get("required_recall_at_k", 0))
            candidate = float(adaptive.get(query_class, {}).get("required_recall_at_k", 0))
            add(
                f"adaptive_{query_class}_no_regression",
                candidate >= baseline,
                round(candidate - baseline, 4),
                ">= 0 recall delta",
            )

    graph_lite = modes.get("graph_lite", {}).get("by_class", {})
    if hybrid and graph_lite:
        graph_p95 = float(
            modes.get("graph_lite", {}).get("overall", {}).get("end_to_end_latency_p95_ms", 0)
        )
        add(
            "graph_lite_p95_within_budget",
            0 < graph_p95 <= 500,
            round(graph_p95, 1),
            "<= 500 ms",
        )
        for query_class, budget in (("direct", -0.02), ("prerequisite", 0.0), ("multi_hop", 0.0)):
            baseline = float(hybrid.get(query_class, {}).get("required_recall_at_k", 0))
            candidate = float(graph_lite.get(query_class, {}).get("required_recall_at_k", 0))
            add(
                f"graph_lite_{query_class}_recall_gate",
                candidate >= baseline + budget,
                round(candidate - baseline, 4),
                f">= {budget:g} recall delta",
            )

    return {"passed": all(check["passed"] for check in checks), "checks": checks}
