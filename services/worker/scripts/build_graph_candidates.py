from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from uuid import NAMESPACE_URL, uuid5

import psycopg

from chiron_worker.config import get_settings
from chiron_worker.graph import GraphStore


@dataclass(frozen=True, slots=True)
class Evidence:
    source_span_id: str
    chunk_id: str
    title: str
    locator: dict[str, Any]
    text: str
    score: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build reviewable Graph-lite candidates")
    parser.add_argument(
        "--spec", type=Path, default=Path("services/api/app/course_taxonomy.json")
    )
    parser.add_argument(
        "--review-output", type=Path, default=Path("eval/graph/review-pack-course-v2.md")
    )
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    return parser.parse_args()


def stable_id(kind: str, course_id: str, version: str, identity: str) -> str:
    return str(
        uuid5(NAMESPACE_URL, f"https://chiron.local/{kind}/{course_id}/{version}/{identity}")
    )


def find_evidence(
    connection: psycopg.Connection, tenant_id: str, course_id: str, terms: list[str]
) -> list[Evidence]:
    patterns = [f"%{term}%" for term in terms]
    rows = connection.execute(
        """
        SELECT DISTINCT ON (s.id)
          s.id::text, c.id::text, d.title, s.locator, s.text
        FROM source_spans s
        JOIN document_versions d ON d.id=s.document_version_id
        JOIN chunks c ON c.source_span_id=s.id AND c.is_active=true AND c.chunk_type='child'
        WHERE s.tenant_id=%s AND d.course_id=%s AND s.text ILIKE ANY(%s)
        ORDER BY s.id, c.ordinal
        LIMIT 240
        """,
        (tenant_id, course_id, patterns),
    ).fetchall()
    evidence = []
    for source_span_id, chunk_id, title, locator, text in rows:
        normalized = str(text).casefold()
        matches = sum(term.casefold() in normalized for term in terms)
        length_penalty = min(abs(len(str(text)) - 900) / 9000, 0.25)
        evidence.append(
            Evidence(
                source_span_id=str(source_span_id),
                chunk_id=str(chunk_id),
                title=str(title or "Nguồn học"),
                locator=dict(locator or {}),
                text=str(text),
                score=matches / max(len(terms), 1) - length_penalty,
            )
        )
    return sorted(evidence, key=lambda item: (-item.score, item.source_span_id))


def edge_evidence(
    connection: psycopg.Connection,
    tenant_id: str,
    course_id: str,
    source_terms: list[str],
    target_terms: list[str],
) -> tuple[Evidence | None, float]:
    candidates = find_evidence(connection, tenant_id, course_id, source_terms + target_terms)
    for item in candidates:
        normalized = item.text.casefold()
        if any(term.casefold() in normalized for term in source_terms) and any(
            term.casefold() in normalized for term in target_terms
        ):
            return item, 0.86
    return (candidates[0], 0.58) if candidates else (None, 0.0)


def render_review(
    spec: dict[str, Any], nodes: dict[str, dict[str, Any]], edges: dict[str, dict[str, Any]]
) -> str:
    lines = [
        "# Chiron Graph-lite review pack — 10 candidates",
        "",
        "Phạm vi: 5 node + 5 edge từ graph version draft. Check `Approve`, `Edit` hoặc `Reject`; production không dùng candidate trước khi duyệt.",
        "",
    ]
    for node_id in spec["review_sample"]["nodes"]:
        node = nodes[node_id]
        evidence: Evidence = node["evidence"]
        lines.extend(
            [
                f"## Node `{node_id}` — {node['name']}",
                "",
                "- [ ] Approve  - [ ] Edit  - [ ] Reject",
                f"- Confidence: `{node['confidence']:.2f}`",
                f"- Summary: {node['summary']}",
                f"- Source: **{evidence.title}** — `{json.dumps(evidence.locator, ensure_ascii=False)}`",
                f"- Source span: `{evidence.source_span_id}`",
                "",
                f"> {evidence.text[:700].replace(chr(10), ' ')}",
                "",
                "Reviewer note:",
                "",
            ]
        )
    for edge_id in spec["review_sample"]["edges"]:
        edge = edges[edge_id]
        evidence = edge["evidence"]
        lines.extend(
            [
                f"## Edge `{edge_id}`",
                "",
                "- [ ] Approve  - [ ] Edit  - [ ] Reject",
                f"- Triple: `{edge['source']}` — **{edge['relation']}** → `{edge['target']}`",
                f"- Confidence: `{edge['confidence']:.2f}`",
                f"- Source: **{evidence.title}** — `{json.dumps(evidence.locator, ensure_ascii=False)}`",
                f"- Source span: `{evidence.source_span_id}`",
                "",
                f"> {evidence.text[:700].replace(chr(10), ' ')}",
                "",
                "Reviewer note:",
                "",
            ]
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    settings = get_settings()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    database_url = settings.database_url.replace("postgresql+psycopg://", "postgresql://", 1)
    nodes_by_spec = {node["id"]: node for node in spec["nodes"]}
    node_records: dict[str, dict[str, Any]] = {}
    edge_records: dict[str, dict[str, Any]] = {}
    chunk_link_count = 0
    expected_chunk_link_ids: list[str] = []
    with psycopg.connect(database_url) as connection:
        tenant_row = connection.execute(
            "SELECT id::text FROM tenants WHERE slug=%s", (args.tenant,)
        ).fetchone()
        if tenant_row is None:
            raise LookupError(f"Unknown tenant: {args.tenant}")
        tenant_id = str(tenant_row[0])
        connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
        course_row = connection.execute(
            "SELECT id::text FROM courses WHERE tenant_id=%s AND slug=%s",
            (tenant_id, args.course),
        ).fetchone()
        if course_row is None:
            raise LookupError(f"Unknown course: {args.course}")
        course_id = str(course_row[0])
        graph_id = stable_id("graph", course_id, spec["version"], spec["version"])
        connection.execute(
            """
            INSERT INTO graph_versions (id, tenant_id, course_id, version, status)
            VALUES (%s, %s, %s, %s, 'draft')
            ON CONFLICT ON CONSTRAINT uq_graph_version
            DO UPDATE SET updated_at=now()
            """,
            (graph_id, tenant_id, course_id, spec["version"]),
        )
        for node in spec["nodes"]:
            evidence = find_evidence(
                connection, tenant_id, course_id, [str(term) for term in node["terms"]]
            )
            if not evidence:
                raise ValueError(f"No source evidence for concept {node['id']}")
            confidence = min(0.95, 0.72 + max(evidence[0].score, 0) * 0.2)
            node_id = stable_id("concept", course_id, spec["version"], node["id"])
            connection.execute(
                """
                INSERT INTO concept_nodes (
                  id, tenant_id, course_id, graph_version_id, canonical_name,
                  normalized_name, node_type, summary, exam_weight, confidence,
                  extraction_method, review_status, evidence_source_span_id
                ) VALUES (%s,%s,%s,%s,%s,%s,'concept',%s,0.5,%s,'deterministic_terms_v1','candidate',%s)
                ON CONFLICT ON CONSTRAINT uq_concept_identity DO UPDATE SET
                  canonical_name=excluded.canonical_name, summary=excluded.summary,
                  confidence=excluded.confidence, extraction_method=excluded.extraction_method,
                  evidence_source_span_id=excluded.evidence_source_span_id,
                  updated_at=now()
                """,
                (
                    node_id,
                    tenant_id,
                    course_id,
                    graph_id,
                    node["name"],
                    node["id"],
                    node["summary"],
                    confidence,
                    evidence[0].source_span_id,
                ),
            )
            for item in evidence[:3]:
                link_id = stable_id(
                    "chunk-concept", course_id, spec["version"], f"{item.chunk_id}:{node_id}"
                )
                expected_chunk_link_ids.append(link_id)
                connection.execute(
                    """
                    INSERT INTO chunk_concepts (
                      id, tenant_id, graph_version_id, chunk_id, concept_id,
                      evidence_source_span_id, confidence, extraction_method, review_status
                    ) VALUES (%s,%s,%s,%s,%s,%s,%s,'deterministic_terms_v1','candidate')
                    ON CONFLICT ON CONSTRAINT uq_chunk_concept_link DO UPDATE SET
                      confidence=excluded.confidence, evidence_source_span_id=excluded.evidence_source_span_id,
                      extraction_method=excluded.extraction_method, updated_at=now()
                    """,
                    (
                        link_id,
                        tenant_id,
                        graph_id,
                        item.chunk_id,
                        node_id,
                        item.source_span_id,
                        confidence,
                    ),
                )
                chunk_link_count += 1
            node_records[node["id"]] = {
                **node,
                "database_id": node_id,
                "confidence": confidence,
                "evidence": evidence[0],
            }
        connection.execute(
            """
            DELETE FROM chunk_concepts
            WHERE graph_version_id=%s
              AND extraction_method='deterministic_terms_v1'
              AND review_status='candidate'
              AND NOT (id=ANY(%s::uuid[]))
            """,
            (graph_id, expected_chunk_link_ids),
        )
        skipped_edges: list[str] = []
        expected_edge_ids = [
            stable_id("edge", course_id, spec["version"], edge["id"]) for edge in spec["edges"]
        ]
        connection.execute(
            """
            DELETE FROM concept_edges
            WHERE graph_version_id=%s
              AND extraction_method='deterministic_terms_v1'
              AND review_status='candidate'
              AND NOT (id=ANY(%s::uuid[]))
            """,
            (graph_id, expected_edge_ids),
        )
        for edge in spec["edges"]:
            source = nodes_by_spec[edge["source"]]
            target = nodes_by_spec[edge["target"]]
            evidence, confidence = edge_evidence(
                connection,
                tenant_id,
                course_id,
                source["terms"],
                target["terms"],
            )
            if evidence is None:
                skipped_edges.append(edge["id"])
                continue
            edge_id = stable_id("edge", course_id, spec["version"], edge["id"])
            connection.execute(
                """
                INSERT INTO concept_edges (
                  id, tenant_id, graph_version_id, source_concept_id, target_concept_id,
                  relation_type, weight, confidence, evidence_source_span_id,
                  review_status, extraction_method
                ) VALUES (%s,%s,%s,%s,%s,%s,1.0,%s,%s,'candidate','deterministic_terms_v1')
                ON CONFLICT (id) DO UPDATE SET
                  source_concept_id=excluded.source_concept_id,
                  target_concept_id=excluded.target_concept_id,
                  relation_type=excluded.relation_type,
                  weight=excluded.weight, confidence=excluded.confidence,
                  evidence_source_span_id=excluded.evidence_source_span_id,
                  extraction_method=excluded.extraction_method,
                  updated_at=now()
                """,
                (
                    edge_id,
                    tenant_id,
                    graph_id,
                    node_records[edge["source"]]["database_id"],
                    node_records[edge["target"]]["database_id"],
                    edge["relation"],
                    confidence,
                    evidence.source_span_id,
                ),
            )
            edge_records[edge["id"]] = {**edge, "confidence": confidence, "evidence": evidence}
        connection.commit()
    cycles = GraphStore(settings.database_url).prerequisite_cycles(
        tenant_id=tenant_id,
        course_id=course_id,
        graph_version_status="draft",
    )
    if cycles:
        raise ValueError(f"Prerequisite cycles found: {cycles}")
    missing_review_edges = set(spec["review_sample"]["edges"]) - set(edge_records)
    if missing_review_edges:
        raise ValueError(f"Review sample edges were not extracted: {sorted(missing_review_edges)}")
    args.review_output.parent.mkdir(parents=True, exist_ok=True)
    args.review_output.write_text(render_review(spec, node_records, edge_records), encoding="utf-8")
    print(
        json.dumps(
            {
                "graph_version": spec["version"],
                "nodes": len(node_records),
                "edges": len(edge_records),
                "chunk_links": chunk_link_count,
                "skipped_edges": skipped_edges,
                "prerequisite_cycles": cycles,
                "review_items": 10,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
