from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import psycopg
from psycopg.rows import dict_row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remap immutable eval labels after a deterministic corpus re-ingest"
    )
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-database-url", required=True)
    parser.add_argument("--target-database-url", required=True)
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    return parser.parse_args()


def database_url(value: str) -> str:
    return value.replace("postgresql+psycopg://", "postgresql://", 1)


def source_rows(
    database: str,
    source_ids: set[str],
    tenant_slug: str,
    course_slug: str,
) -> dict[str, dict[str, Any]]:
    with psycopg.connect(database_url(database), row_factory=dict_row) as connection:
        rows = connection.execute(
            """
            SELECT s.id::text, s.checksum, s.locator, s.text,
                   d.title, d.source_path, d.source_type
            FROM source_spans s
            JOIN document_versions d ON d.id=s.document_version_id
            JOIN courses c ON c.id=d.course_id
            JOIN tenants t ON t.id=d.tenant_id
            WHERE t.slug=%s AND c.slug=%s AND s.id=ANY(%s::uuid[])
            """,
            (tenant_slug, course_slug, list(source_ids)),
        ).fetchall()
    return {str(row["id"]): dict(row) for row in rows}


def target_rows(
    database: str, tenant_slug: str, course_slug: str
) -> list[dict[str, Any]]:
    with psycopg.connect(database_url(database), row_factory=dict_row) as connection:
        rows = connection.execute(
            """
            SELECT s.id::text, s.checksum, s.locator, s.text,
                   d.title, d.source_path, d.source_type
            FROM source_spans s
            JOIN document_versions d ON d.id=s.document_version_id
            JOIN courses c ON c.id=d.course_id
            JOIN tenants t ON t.id=d.tenant_id
            WHERE t.slug=%s AND c.slug=%s
            """,
            (tenant_slug, course_slug),
        ).fetchall()
    return [dict(row) for row in rows]


def compact_text(value: Any) -> str:
    return " ".join(str(value or "").casefold().split())


def match_score(source: dict[str, Any], target: dict[str, Any]) -> int:
    if source["checksum"] == target["checksum"]:
        return 1000
    score = 0
    if source["source_path"] and source["source_path"] == target["source_path"]:
        score += 500
    source_locator = dict(source["locator"] or {})
    target_locator = dict(target["locator"] or {})
    if source_locator == target_locator:
        score += 350
    elif source_locator.get("kind") == target_locator.get("kind"):
        if source_locator.get("page") is not None and source_locator.get(
            "page"
        ) == target_locator.get("page"):
            score += 320
        elif source_locator.get("section_id") and source_locator.get(
            "section_id"
        ) == target_locator.get("section_id"):
            score += 300
        elif source_locator.get("order") is not None and source_locator.get(
            "order"
        ) == target_locator.get("order"):
            score += 260
    source_title = compact_text(source["title"])
    target_title = compact_text(target["title"])
    if source_title and target_title and (
        source_title.startswith(target_title) or target_title.startswith(source_title)
    ):
        score += 120
    if compact_text(source["text"]) == compact_text(target["text"]):
        score += 300
    if source["source_type"] == target["source_type"]:
        score += 10
    return score


def main() -> int:
    args = parse_args()
    cases = [
        json.loads(line)
        for line in args.dataset.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    fields = ("required_source_span_ids", "acceptable_source_span_ids")
    source_ids = {
        str(source_id)
        for case in cases
        for field in fields
        for source_id in case.get(field, [])
    }
    sources = source_rows(
        args.source_database_url, source_ids, args.tenant, args.course
    )
    missing_source = sorted(source_ids - set(sources))
    if missing_source:
        raise ValueError(f"Source database is missing eval labels: {missing_source}")
    targets = target_rows(args.target_database_url, args.tenant, args.course)

    remap: dict[str, str] = {}
    diagnostics: list[dict[str, Any]] = []
    for source_id, source in sources.items():
        ranked = sorted(
            ((match_score(source, target), target) for target in targets),
            key=lambda item: (-item[0], str(item[1]["id"])),
        )
        best_score, best = ranked[0]
        second_score = ranked[1][0] if len(ranked) > 1 else -1
        if best_score < 500 or best_score == second_score:
            raise ValueError(
                f"Ambiguous target for {source_id}: best={best_score}, second={second_score}"
            )
        remap[source_id] = str(best["id"])
        diagnostics.append(
            {
                "source_id": source_id,
                "target_id": str(best["id"]),
                "score": best_score,
                "source_path": source["source_path"],
                "locator": source["locator"],
            }
        )

    remapped_cases = []
    for case in cases:
        remapped = dict(case)
        for field in fields:
            remapped[field] = [remap[str(value)] for value in case.get(field, [])]
        remapped_cases.append(remapped)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "\n".join(json.dumps(case, ensure_ascii=False) for case in remapped_cases) + "\n",
        encoding="utf-8",
    )
    report_path = args.output.with_suffix(".remap.json")
    report_path.write_text(
        json.dumps(
            {
                "source_dataset": str(args.dataset),
                "output_dataset": str(args.output),
                "labels": len(source_ids),
                "cases": len(cases),
                "mappings": diagnostics,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {"status": "remapped", "cases": len(cases), "labels": len(source_ids)},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
