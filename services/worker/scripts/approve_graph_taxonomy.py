from __future__ import annotations

import argparse
import json
from pathlib import Path

import psycopg

from chiron_worker.config import get_settings
from chiron_worker.graph import GraphStore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Approve a draft Graph-lite taxonomy after deterministic quality checks"
    )
    parser.add_argument("--version", default="course-knowledge-v2")
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    parser.add_argument(
        "--policy", type=Path, default=Path("eval/graph/auto-approval-course-v2.json")
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    policy = json.loads(args.policy.read_text(encoding="utf-8"))
    if policy.get("graph_version") != args.version:
        raise ValueError("Approval policy targets a different graph version")
    gate = policy["quality_gate"]
    settings = get_settings()
    database_url = settings.database_url.replace("postgresql+psycopg://", "postgresql://", 1)

    with psycopg.connect(database_url) as connection:
        tenant_row = connection.execute(
            "SELECT id::text FROM tenants WHERE slug=%s", (args.tenant,)
        ).fetchone()
        if tenant_row is None:
            raise LookupError(f"Unknown tenant: {args.tenant}")
        tenant_id = str(tenant_row[0])
        connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
        graph_row = connection.execute(
            """
            SELECT g.id::text, g.status, c.id::text
            FROM graph_versions g
            JOIN courses c ON c.id=g.course_id
            WHERE g.tenant_id=%s AND g.version=%s AND c.slug=%s
            """,
            (tenant_id, args.version, args.course),
        ).fetchone()
        if graph_row is None:
            raise LookupError(f"Unknown graph version: {args.version}")
        graph_id, graph_status, course_id = map(str, graph_row)
        if graph_status != "draft":
            raise ValueError("Only draft graph versions may be taxonomy-approved")

        node_count, missing_nodes, min_node_confidence = connection.execute(
            """
            SELECT count(*), count(*) FILTER (WHERE evidence_source_span_id IS NULL), min(confidence)
            FROM concept_nodes
            WHERE tenant_id=%s AND graph_version_id=%s
            """,
            (tenant_id, graph_id),
        ).fetchone()
        edge_count, missing_edges, min_edge_confidence = connection.execute(
            """
            SELECT count(*), count(*) FILTER (WHERE evidence_source_span_id IS NULL), min(confidence)
            FROM concept_edges
            WHERE tenant_id=%s AND graph_version_id=%s
            """,
            (tenant_id, graph_id),
        ).fetchone()
        lower, upper = gate["required_node_count_range"]
        if not lower <= node_count <= upper or edge_count < gate["required_edge_count_minimum"]:
            raise ValueError(f"Unexpected graph size: nodes={node_count}, edges={edge_count}")
        if missing_nodes or missing_edges:
            raise ValueError("All taxonomy nodes and edges require source provenance")
        if min_node_confidence < gate["minimum_node_confidence"]:
            raise ValueError(f"Node confidence below gate: {min_node_confidence}")
        if min_edge_confidence < gate["minimum_edge_confidence"]:
            raise ValueError(f"Edge confidence below gate: {min_edge_confidence}")

        invalid_relations = connection.execute(
            """
            SELECT count(*)
            FROM concept_edges
            WHERE tenant_id=%s AND graph_version_id=%s
              AND NOT (relation_type=ANY(%s))
            """,
            (tenant_id, graph_id, gate["allowed_relation_types"]),
        ).fetchone()[0]
        invalid_scope = connection.execute(
            """
            SELECT count(*)
            FROM concept_edges e
            JOIN graph_versions g ON g.id=e.graph_version_id
            LEFT JOIN source_spans s ON s.id=e.evidence_source_span_id AND s.tenant_id=e.tenant_id
            LEFT JOIN document_versions d ON d.id=s.document_version_id AND d.course_id=g.course_id
            WHERE e.tenant_id=%s AND e.graph_version_id=%s AND (s.id IS NULL OR d.id IS NULL)
            """,
            (tenant_id, graph_id),
        ).fetchone()[0]
        if invalid_relations or invalid_scope:
            raise ValueError(
                f"Invalid relation/provenance scope: relations={invalid_relations}, scope={invalid_scope}"
            )

        cycles = GraphStore(settings.database_url).prerequisite_cycles(
            tenant_id=tenant_id,
            course_id=course_id,
            review_statuses=("candidate", "approved"),
            graph_version_status="draft",
        )
        if cycles:
            raise ValueError(f"Prerequisite graph contains cycles: {cycles}")

        node_approved = connection.execute(
            """
            UPDATE concept_nodes SET review_status='approved', updated_at=now()
            WHERE tenant_id=%s AND graph_version_id=%s AND review_status='candidate'
            """,
            (tenant_id, graph_id),
        ).rowcount
        edge_approved = connection.execute(
            """
            UPDATE concept_edges SET review_status='approved', updated_at=now()
            WHERE tenant_id=%s AND graph_version_id=%s AND review_status='candidate'
            """,
            (tenant_id, graph_id),
        ).rowcount
        link_approved = connection.execute(
            """
            UPDATE chunk_concepts SET review_status='approved', updated_at=now()
            WHERE tenant_id=%s AND graph_version_id=%s AND review_status='candidate'
            """,
            (tenant_id, graph_id),
        ).rowcount
        connection.commit()

    print(
        json.dumps(
            {
                "graph_version": args.version,
                "graph_status": "draft",
                "nodes_approved": node_approved,
                "edges_approved": edge_approved,
                "chunk_concept_links_approved": link_approved,
                "prerequisite_cycles": cycles,
                "activation_changed": False,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
