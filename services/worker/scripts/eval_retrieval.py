from __future__ import annotations

import argparse
import asyncio
import json
import platform
from collections import Counter
from datetime import UTC, datetime
from hashlib import sha256
from importlib.metadata import version
from pathlib import Path
from statistics import median
from time import perf_counter
from typing import Any

import psycopg

from chiron_worker.config import get_settings
from chiron_worker.eval import quality_gates, ranking_metrics, summarize
from chiron_worker.graph import GraphLiteRetriever, GraphStore
from chiron_worker.qdrant import FastEmbedEncoder, QdrantChunkIndex
from chiron_worker.ragas_eval import add_ragas_id_metrics
from chiron_worker.retrieval import (
    AdaptiveRetriever,
    HybridRetriever,
    deduplicate_hits_by_source_span,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate Chiron retrieval against a golden set")
    parser.add_argument("--dataset", type=Path, default=Path("eval/rag/golden.jsonl"))
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    parser.add_argument("--tenant-id")
    parser.add_argument("--course-id")
    parser.add_argument("--collection", help="Override Qdrant collection for A/B evaluation")
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--candidate-limit", type=int, default=24)
    parser.add_argument("--require-approved", action="store_true")
    parser.add_argument("--split-manifest", type=Path)
    parser.add_argument("--split", choices=("all", "development", "holdout"), default="all")
    parser.add_argument("--max-subqueries", type=int, default=1, choices=(1, 2, 3))
    parser.add_argument("--quiet", action="store_true", help="Print summaries instead of cases")
    parser.add_argument(
        "--modes",
        nargs="+",
        choices=("dense", "bm25", "hybrid", "adaptive", "graph_lite"),
        default=("dense", "bm25", "hybrid", "adaptive"),
    )
    parser.add_argument("--graph-version-status", default="active", choices=("draft", "active"))
    parser.add_argument(
        "--graph-review-statuses",
        nargs="+",
        choices=("candidate", "approved", "active"),
        default=("active",),
    )
    parser.add_argument("--graph-max-hops", type=int, default=2, choices=(1, 2))
    parser.add_argument("--graph-expansion-limit", type=int, default=8)
    parser.add_argument(
        "--latency-repetitions",
        type=int,
        choices=(1, 3),
        default=1,
        help="Repeat retrieval and report the per-case median latency",
    )
    return parser.parse_args()


def load_cases(path: Path) -> list[dict[str, Any]]:
    cases = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [str(case["id"]) for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("Golden dataset contains duplicate IDs")
    for case in cases:
        required = case.get("required_source_span_ids") or []
        if not required:
            raise ValueError(f"Golden case {case['id']} has no required source spans")
        if case.get("query_class") not in {"direct", "prerequisite", "multi_hop"}:
            raise ValueError(f"Golden case {case['id']} has an invalid query class")
        if case.get("interaction_type") != "user_question":
            raise ValueError(
                f"Golden case {case['id']} is not a user_question; "
                "assessment items must use the separate reasoning/rubric evaluation suite"
            )
        if not case.get("review_status"):
            raise ValueError(f"Golden case {case['id']} has no review status")
    return cases


def apply_split(
    cases: list[dict[str, Any]], dataset_path: Path, manifest_path: Path | None, split: str
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    by_class = Counter(str(case["query_class"]) for case in cases)
    if split == "all":
        return cases, {"total": len(cases), "by_class": dict(by_class)}
    if manifest_path is None:
        raise ValueError("--split-manifest is required when --split is not all")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checksum = sha256(dataset_path.read_bytes()).hexdigest()
    if manifest.get("dataset_sha256") != checksum:
        raise ValueError("Split manifest dataset checksum does not match the golden dataset")
    development = set(manifest.get("development_ids") or [])
    holdout = set(manifest.get("holdout_ids") or [])
    all_ids = {str(case["id"]) for case in cases}
    if development & holdout or development | holdout != all_ids:
        raise ValueError("Split manifest must be disjoint and cover every golden case exactly once")
    selected_ids = development if split == "development" else holdout
    selected = [case for case in cases if str(case["id"]) in selected_ids]
    selected_coverage = Counter(str(case["query_class"]) for case in selected)
    return selected, {"total": len(selected), "by_class": dict(selected_coverage)}


def resolve_scope(database_url: str, tenant_slug: str, course_slug: str) -> tuple[str, str]:
    psycopg_url = database_url.replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(psycopg_url) as connection:
        tenant_row = connection.execute(
            "SELECT id::text FROM tenants WHERE slug=%s", (tenant_slug,)
        ).fetchone()
        if tenant_row is None:
            raise LookupError(f"Unknown tenant: {tenant_slug}")
        tenant_id = str(tenant_row[0])
        connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
        course_row = connection.execute(
            "SELECT id::text FROM courses WHERE tenant_id=%s AND slug=%s",
            (tenant_id, course_slug),
        ).fetchone()
    if course_row is None:
        raise LookupError(f"Unknown course in tenant {tenant_slug}: {course_slug}")
    return tenant_id, str(course_row[0])


def validate_source_ids(
    database_url: str, tenant_id: str, course_id: str, cases: list[dict[str, Any]]
) -> None:
    expected = {
        str(source_id)
        for case in cases
        for field in ("required_source_span_ids", "acceptable_source_span_ids")
        for source_id in case.get(field, [])
    }
    psycopg_url = database_url.replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(psycopg_url) as connection:
        connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
        rows = connection.execute(
            """
            SELECT s.id::text
            FROM source_spans s
            JOIN document_versions d ON d.id = s.document_version_id
            WHERE d.tenant_id = %s AND d.course_id = %s AND s.id = ANY(%s::uuid[])
            """,
            (tenant_id, course_id, list(expected)),
        ).fetchall()
    found = {str(row[0]) for row in rows}
    missing = sorted(expected - found)
    if missing:
        raise ValueError(f"Golden dataset references {len(missing)} missing source spans: {missing}")


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Chiron RAGAS retrieval baseline",
        "",
        f"- Dataset: `{report['dataset']}`",
        f"- Cases: **{report['dataset_coverage']['total']}**",
        f"- Collection: `{report['collection']}`",
        f"- Embedding: `{report['embedding_model']}` / `{report['embedding_version']}`",
        f"- RAGAS: `{report['ragas_version']}`",
        f"- Quality gate: **{'PASS' if report['quality_gate']['passed'] else 'FAIL'}**",
        "",
        "## Overall",
        "",
        "| Mode | Hit@K | Required recall | MRR | nDCG | RAGAS precision | RAGAS recall | P95 E2E ms |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for mode, data in report["modes"].items():
        item = data["overall"]
        lines.append(
            "| {mode} | {hit:.3f} | {recall:.3f} | {mrr:.3f} | {ndcg:.3f} | "
            "{precision:.3f} | {ragas_recall:.3f} | {latency:.1f} |".format(
                mode=mode,
                hit=float(item.get("hit_at_k", 0)),
                recall=float(item.get("required_recall_at_k", 0)),
                mrr=float(item.get("mrr_at_k", 0)),
                ndcg=float(item.get("ndcg_at_k", 0)),
                precision=float(item.get("ragas_id_context_precision", 0)),
                ragas_recall=float(item.get("ragas_id_context_recall", 0)),
                latency=float(item.get("end_to_end_latency_p95_ms", 0)),
            )
        )
    lines.extend(["", "## By query class", ""])
    for mode, data in report["modes"].items():
        lines.extend([f"### {mode}", "", "| Class | Cases | Hit@K | Required recall | MRR | nDCG |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
        for query_class, item in data["by_class"].items():
            lines.append(
                f"| {query_class} | {item.get('cases', 0)} | {float(item.get('hit_at_k', 0)):.3f} "
                f"| {float(item.get('required_recall_at_k', 0)):.3f} | {float(item.get('mrr_at_k', 0)):.3f} "
                f"| {float(item.get('ndcg_at_k', 0)):.3f} |"
            )
        lines.append("")
    if "hybrid" in report["modes"] and "adaptive" in report["modes"]:
        hybrid_cases = {
            str(item["id"]): item for item in report["modes"]["hybrid"]["cases"]
        }
        adaptive_cases = {
            str(item["id"]): item for item in report["modes"]["adaptive"]["cases"]
        }
        regressions = sorted(
            (
                (
                    case_id,
                    str(hybrid_cases[case_id]["query_class"]),
                    float(hybrid_cases[case_id]["required_recall_at_k"]),
                    float(adaptive_cases[case_id]["required_recall_at_k"]),
                )
                for case_id in hybrid_cases.keys() & adaptive_cases.keys()
            ),
            key=lambda item: item[3] - item[2],
        )[:10]
        lines.extend(
            [
                "## Largest adaptive recall regressions",
                "",
                "| Case | Class | Hybrid recall | Adaptive recall | Delta |",
                "| --- | --- | ---: | ---: | ---: |",
            ]
        )
        for case_id, query_class, hybrid_recall, adaptive_recall in regressions:
            lines.append(
                f"| {case_id} | {query_class} | {hybrid_recall:.3f} | {adaptive_recall:.3f} | {adaptive_recall - hybrid_recall:+.3f} |"
            )
        lines.append("")
    lines.extend(["## Quality gates", ""])
    for check in report["quality_gate"]["checks"]:
        marker = "PASS" if check["passed"] else "FAIL"
        lines.append(
            f"- **{marker}** `{check['name']}` — actual `{check['actual']}`, expected `{check['expected']}`"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    settings = get_settings()
    if settings.embedding_provider != "local":
        raise RuntimeError("Golden corpus evaluation requires EMBEDDING_PROVIDER=local")
    if bool(args.tenant_id) != bool(args.course_id):
        raise ValueError("--tenant-id and --course-id must be provided together")
    if args.tenant_id and args.course_id:
        tenant_id, course_id = args.tenant_id, args.course_id
    else:
        tenant_id, course_id = resolve_scope(settings.database_url, args.tenant, args.course)
    cases = load_cases(args.dataset)
    cases, expected_coverage = apply_split(
        cases, args.dataset, args.split_manifest, args.split
    )
    if args.require_approved:
        unapproved = [case["id"] for case in cases if case["review_status"] != "approved"]
        if unapproved:
            raise ValueError(f"Golden cases require human approval: {unapproved}")
    validate_source_ids(settings.database_url, tenant_id, course_id, cases)
    encoder = FastEmbedEncoder(
        settings.embedding_model,
        settings.sparse_embedding_model,
        settings.embedding_cache_path,
    )
    evaluation_settings = (
        settings.model_copy(update={"qdrant_collection": args.collection})
        if args.collection
        else settings
    )
    index = QdrantChunkIndex(evaluation_settings)
    adaptive_retriever = AdaptiveRetriever(HybridRetriever(encoder, index))
    graph_lite_retriever = GraphLiteRetriever(
        adaptive_retriever, GraphStore(settings.database_url), index
    )
    # Production workers are long-lived. Warm the encoder, Qdrant query path and
    # small graph read model once per route so startup I/O is not reported as P95.
    # The measured cases remain the immutable development/holdout cases below.
    warmup_cases: list[str] = []
    if "graph_lite" in args.modes:
        for route in ("direct", "prerequisite", "multi_hop"):
            case = next((item for item in cases if item["query_class"] == route), None)
            if case is None:
                continue
            graph_lite_retriever.retrieve(
                str(case["query"]),
                tenant_id=tenant_id,
                course_id=course_id,
                route=route,
                direct_candidate_limit=args.candidate_limit,
                direct_limit=args.top_k,
                multi_hop_candidate_limit=args.candidate_limit,
                multi_hop_limit=args.top_k,
                max_subqueries=args.max_subqueries,
                graph_max_hops=args.graph_max_hops,
                graph_expansion_limit=args.graph_expansion_limit,
                graph_review_statuses=tuple(args.graph_review_statuses),
                graph_version_status=args.graph_version_status,
            )
            warmup_cases.append(str(case["id"]))
    by_mode: dict[str, list[dict[str, Any]]] = {mode: [] for mode in args.modes}
    embedding_latencies: list[float] = []

    for case in cases:
        query = str(case["query"])
        standard_modes = [
            mode for mode in args.modes if mode not in {"adaptive", "graph_lite"}
        ]
        dense = sparse = None
        embedding_latency_ms = 0.0
        if standard_modes:
            started = perf_counter()
            dense, sparse = encoder.encode_query(query)
            embedding_latency_ms = (perf_counter() - started) * 1000
            embedding_latencies.append(embedding_latency_ms)
        for mode in standard_modes:
            started = perf_counter()
            if mode == "dense":
                hits = index.dense_query(
                    dense,
                    tenant_id=tenant_id,
                    course_id=course_id,
                    candidate_limit=args.candidate_limit,
                )
            elif mode == "bm25":
                hits = index.sparse_query(
                    sparse,
                    tenant_id=tenant_id,
                    course_id=course_id,
                    candidate_limit=args.candidate_limit,
                )
            else:
                hits = index.hybrid_query(
                    dense,
                    sparse,
                    tenant_id=tenant_id,
                    course_id=course_id,
                    candidate_limit=args.candidate_limit,
                )
                # Compare Graph-lite with the exact semantic baseline it wraps.
                # Qdrant RRF ties are otherwise returned in a non-deterministic order,
                # which can manufacture a recall regression before graph expansion runs.
                hits.sort(
                    key=lambda item: (-float(item.get("score", 0)), str(item.get("id", "")))
                )
                hits = deduplicate_hits_by_source_span(hits)
            retrieval_latency_ms = (perf_counter() - started) * 1000
            metrics = ranking_metrics(
                hits,
                list(case["required_source_span_ids"]),
                list(case.get("acceptable_source_span_ids") or []),
                top_k=args.top_k,
            )
            by_mode[mode].append(
                {
                    "id": case["id"],
                    "query": query,
                    "query_class": case["query_class"],
                    "required_source_span_ids": list(case["required_source_span_ids"]),
                    "acceptable_source_span_ids": list(
                        case.get("acceptable_source_span_ids") or []
                    ),
                    **metrics,
                    "embedding_latency_ms": embedding_latency_ms,
                    "retrieval_latency_ms": retrieval_latency_ms,
                    "end_to_end_latency_ms": embedding_latency_ms + retrieval_latency_ms,
                }
            )

        if "adaptive" in args.modes:
            started = perf_counter()
            adaptive_result = adaptive_retriever.retrieve(
                query,
                tenant_id=tenant_id,
                course_id=course_id,
                route=str(case["query_class"]),
                direct_candidate_limit=args.candidate_limit,
                direct_limit=args.top_k,
                multi_hop_candidate_limit=args.candidate_limit,
                multi_hop_limit=args.top_k,
                max_subqueries=args.max_subqueries,
            )
            retrieval_latency_ms = (perf_counter() - started) * 1000
            metrics = ranking_metrics(
                list(adaptive_result["hits"]),
                list(case["required_source_span_ids"]),
                list(case.get("acceptable_source_span_ids") or []),
                top_k=args.top_k,
            )
            by_mode["adaptive"].append(
                {
                    "id": case["id"],
                    "query": query,
                    "query_class": case["query_class"],
                    "required_source_span_ids": list(case["required_source_span_ids"]),
                    "acceptable_source_span_ids": list(
                        case.get("acceptable_source_span_ids") or []
                    ),
                    **metrics,
                    "retrieval_latency_ms": retrieval_latency_ms,
                    "end_to_end_latency_ms": retrieval_latency_ms,
                    "strategy": adaptive_result["strategy"],
                    "subqueries": adaptive_result["subqueries"],
                    "degraded": adaptive_result["degraded"],
                }
            )

        if "graph_lite" in args.modes:
            graph_latencies: list[float] = []
            graph_result: dict[str, Any] = {}
            for _ in range(args.latency_repetitions):
                started = perf_counter()
                graph_result = graph_lite_retriever.retrieve(
                    query,
                    tenant_id=tenant_id,
                    course_id=course_id,
                    route=str(case["query_class"]),
                    direct_candidate_limit=args.candidate_limit,
                    direct_limit=args.top_k,
                    multi_hop_candidate_limit=args.candidate_limit,
                    multi_hop_limit=args.top_k,
                    max_subqueries=args.max_subqueries,
                    graph_max_hops=args.graph_max_hops,
                    graph_expansion_limit=args.graph_expansion_limit,
                    graph_review_statuses=tuple(args.graph_review_statuses),
                    graph_version_status=args.graph_version_status,
                )
                graph_latencies.append((perf_counter() - started) * 1000)
            retrieval_latency_ms = median(graph_latencies)
            metrics = ranking_metrics(
                list(graph_result["hits"]),
                list(case["required_source_span_ids"]),
                list(case.get("acceptable_source_span_ids") or []),
                top_k=args.top_k,
            )
            by_mode["graph_lite"].append(
                {
                    "id": case["id"],
                    "query": query,
                    "query_class": case["query_class"],
                    "required_source_span_ids": list(case["required_source_span_ids"]),
                    "acceptable_source_span_ids": list(
                        case.get("acceptable_source_span_ids") or []
                    ),
                    **metrics,
                    "retrieval_latency_ms": retrieval_latency_ms,
                    "end_to_end_latency_ms": retrieval_latency_ms,
                    "strategy": graph_result["strategy"],
                    "subqueries": graph_result["subqueries"],
                    "graph_expanded": graph_result["graph_expanded"],
                    "graph_sources": graph_result["graph_sources"],
                    "degraded": graph_result.get("degraded", False),
                }
            )

    for mode in args.modes:
        by_mode[mode] = asyncio.run(add_ragas_id_metrics(by_mode[mode]))

    coverage = Counter(str(case["query_class"]) for case in cases)
    interaction_coverage = Counter(str(case["interaction_type"]) for case in cases)

    report = {
        "generated_at": datetime.now(UTC).isoformat(),
        "dataset": str(args.dataset),
        "split": args.split,
        "split_manifest": str(args.split_manifest) if args.split_manifest else None,
        "expected_coverage": expected_coverage,
        "dataset_coverage": {
            "total": len(cases),
            "by_class": dict(coverage),
            "by_interaction_type": dict(interaction_coverage),
        },
        "review_status": dict(Counter(str(case["review_status"]) for case in cases)),
        "embedding_model": settings.embedding_model,
        "embedding_version": settings.embedding_version,
        "collection": evaluation_settings.qdrant_collection,
        "ragas_version": version("ragas"),
        "python_version": platform.python_version(),
        "ragas_reference_policy": {
            "precision": "required + acceptable source spans",
            "recall": "required source spans only",
        },
        "top_k": args.top_k,
        "candidate_limit": args.candidate_limit,
        "latency_repetitions": args.latency_repetitions,
        "graph_policy": {
            "version_status": args.graph_version_status,
            "review_statuses": list(args.graph_review_statuses),
            "max_hops": args.graph_max_hops,
            "expansion_limit": args.graph_expansion_limit,
        },
        "warmup_policy": {
            "excluded_from_metrics": True,
            "case_ids": warmup_cases,
            "reason": "warm long-lived encoder, Qdrant and graph read paths",
        },
        "embedding_latency_p50_ms": (
            sorted(embedding_latencies)[len(embedding_latencies) // 2]
            if embedding_latencies
            else 0.0
        ),
        "modes": {
            mode: {
                "overall": summarize(results),
                "by_class": {
                    query_class: summarize(
                        [result for result in results if result["query_class"] == query_class]
                    )
                    for query_class in ("direct", "prerequisite", "multi_hop")
                },
                "cases": results,
            }
            for mode, results in by_mode.items()
        },
    }
    report["quality_gate"] = quality_gates(report)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
        args.output.with_suffix(".md").write_text(render_markdown(report), encoding="utf-8")
    if args.quiet:
        print(
            json.dumps(
                {
                    "embedding_latency_p50_ms": report["embedding_latency_p50_ms"],
                    "modes": {
                        mode: data["overall"] for mode, data in report["modes"].items()
                    },
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
