from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import psycopg

from chiron_worker.config import get_settings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a human-review pack for retrieval goldens")
    parser.add_argument("--dataset", type=Path, default=Path("eval/rag/golden.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("eval/rag/review/review-pack-20.md"))
    parser.add_argument("--sample-size", type=int, default=20)
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    return parser.parse_args()


def load_cases(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def stratified_sample(cases: list[dict[str, Any]], sample_size: int) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for case in cases:
        groups[str(case["query_class"])].append(case)
    if sample_size >= len(cases):
        return cases
    weights = {"direct": 0.4, "prerequisite": 0.3, "multi_hop": 0.3}
    selected: list[dict[str, Any]] = []
    for query_class, weight in weights.items():
        count = round(sample_size * weight)
        selected.extend(groups[query_class][:count])
    return selected[:sample_size]


def source_records(
    database_url: str, tenant_slug: str, course_slug: str, source_ids: list[str]
) -> dict[str, dict[str, Any]]:
    psycopg_url = database_url.replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(psycopg_url) as connection:
        tenant_row = connection.execute(
            "SELECT id::text FROM tenants WHERE slug=%s", (tenant_slug,)
        ).fetchone()
        if tenant_row is None:
            raise LookupError(f"Unknown tenant: {tenant_slug}")
        tenant_id = str(tenant_row[0])
        connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
        rows = connection.execute(
            """
            SELECT s.id::text, d.title, s.locator, s.text
            FROM source_spans s
            JOIN document_versions d ON d.id = s.document_version_id
            JOIN courses c ON c.id = d.course_id
            WHERE d.tenant_id = %s AND c.slug = %s AND s.id = ANY(%s::uuid[])
            """,
            (tenant_id, course_slug, source_ids),
        ).fetchall()
    return {
        str(row[0]): {"title": row[1], "locator": row[2], "text": row[3]} for row in rows
    }


def locator_label(locator: dict[str, Any]) -> str:
    page = locator.get("page") or locator.get("pdf_page") or locator.get("label")
    section = locator.get("section_title") or locator.get("heading") or locator.get("section_id")
    return " · ".join(str(item) for item in (page, section) if item) or json.dumps(
        locator, ensure_ascii=False
    )


def render(cases: list[dict[str, Any]], sources: dict[str, dict[str, Any]]) -> str:
    counts = defaultdict(int)
    for case in cases:
        counts[str(case["query_class"])] += 1
    lines = [
        "# Chiron golden-set review pack",
        "",
        f"Cases: **{len(cases)}** — direct {counts['direct']}, prerequisite {counts['prerequisite']}, multi-hop {counts['multi_hop']}.",
        "",
        "Review mỗi case: câu hỏi tự nhiên, class đúng, required evidence thực sự bắt buộc, và alternate evidence không bị thiếu.",
        "",
    ]
    for case in cases:
        lines.extend(
            [
                f"## {case['id']} · {case['query_class']}",
                "",
                f"**Query:** {case['query']}",
                "",
                f"**Rationale:** {case['rationale']}",
                "",
                "### Required evidence",
                "",
            ]
        )
        for source_id in case["required_source_span_ids"]:
            source = sources[str(source_id)]
            excerpt = " ".join(str(source["text"]).split())[:700]
            lines.extend(
                [
                    f"- `{source_id}` — **{source['title']}**, {locator_label(source['locator'])}",
                    f"  - {excerpt}",
                ]
            )
        lines.extend(["", "### Acceptable/alternate evidence", ""])
        alternates = case.get("acceptable_source_span_ids") or []
        if not alternates:
            lines.append("- Không có trong candidate hiện tại.")
        for source_id in alternates:
            source = sources[str(source_id)]
            excerpt = " ".join(str(source["text"]).split())[:500]
            lines.extend(
                [
                    f"- `{source_id}` — **{source['title']}**, {locator_label(source['locator'])}",
                    f"  - {excerpt}",
                ]
            )
        lines.extend(
            [
                "",
                "- [ ] Approve",
                "- [ ] Sửa query/class",
                "- [ ] Sửa required/acceptable sources",
                "- Ghi chú:",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    cases = stratified_sample(load_cases(args.dataset), args.sample_size)
    source_ids = list(
        dict.fromkeys(
            str(source_id)
            for case in cases
            for field in ("required_source_span_ids", "acceptable_source_span_ids")
            for source_id in case.get(field, [])
        )
    )
    settings = get_settings()
    sources = source_records(
        settings.database_url, args.tenant, args.course, source_ids
    )
    missing = sorted(set(source_ids) - set(sources))
    if missing:
        raise ValueError(f"Missing sources for review pack: {missing}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(cases, sources), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "cases": len(cases)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
