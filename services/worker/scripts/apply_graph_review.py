from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any
from uuid import NAMESPACE_URL, uuid5

import psycopg

from chiron_worker.config import get_settings
from chiron_worker.graph import GraphStore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply an audited Graph-lite review sample")
    parser.add_argument("--spec", type=Path, default=Path("eval/graph/candidates_v1.json"))
    parser.add_argument(
        "--decisions",
        type=Path,
        default=Path("eval/graph/review-decisions-10.json"),
    )
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    return parser.parse_args()


def stable_id(kind: str, course_id: str, version: str, identity: str) -> str:
    value = f"https://chiron.local/{kind}/{course_id}/{version}/{identity}"
    return str(uuid5(NAMESPACE_URL, value))


def decision_map(payload: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    result: dict[tuple[str, str], dict[str, Any]] = {}
    for item in payload.get("decisions", []):
        key = (str(item.get("kind")), str(item.get("id")))
        if key in result:
            raise ValueError(f"Duplicate review decision: {key}")
        if item.get("decision") not in {"approve", "reject"}:
            raise ValueError(f"Invalid review decision: {key}")
        if not str(item.get("note") or "").strip():
            raise ValueError(f"Review note is required: {key}")
        result[key] = item
    return result


def main() -> int:
    args = parse_args()
    settings = get_settings()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    payload = json.loads(args.decisions.read_text(encoding="utf-8"))
    if payload.get("graph_version") != spec.get("version"):
        raise ValueError("Decision artifact and candidate spec target different graph versions")

    expected = {
        *(("node", item_id) for item_id in spec["review_sample"]["nodes"]),
        *(("edge", item_id) for item_id in spec["review_sample"]["edges"]),
    }
    decisions = decision_map(payload)
    if set(decisions) != expected:
        missing = sorted(expected - set(decisions))
        extra = sorted(set(decisions) - expected)
        raise ValueError(f"Review sample mismatch; missing={missing}, extra={extra}")

    database_url = settings.database_url.replace("postgresql+psycopg://", "postgresql://", 1)
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
        version = str(spec["version"])
        graph_id = stable_id("graph", course_id, version, version)
        graph_row = connection.execute(
            "SELECT status FROM graph_versions WHERE id=%s AND tenant_id=%s AND course_id=%s",
            (graph_id, tenant_id, course_id),
        ).fetchone()
        if graph_row is None or graph_row[0] != "draft":
            raise ValueError("Reviews may only be applied to the expected draft graph")

        node_count = 0
        edge_count = 0
        for (kind, item_id), item in sorted(decisions.items()):
            status = "approved" if item["decision"] == "approve" else "rejected"
            identity_kind = "concept" if kind == "node" else "edge"
            object_id = stable_id(identity_kind, course_id, version, item_id)
            table = "concept_nodes" if kind == "node" else "concept_edges"
            row = connection.execute(
                f"""
                UPDATE {table}
                SET review_status=%s, updated_at=now()
                WHERE id=%s AND tenant_id=%s AND graph_version_id=%s
                  AND evidence_source_span_id IS NOT NULL
                RETURNING id
                """,
                (status, object_id, tenant_id, graph_id),
            ).fetchone()
            if row is None:
                raise LookupError(f"Review object missing or lacks provenance: {kind}/{item_id}")
            if kind == "node":
                connection.execute(
                    """
                    UPDATE chunk_concepts
                    SET review_status=%s, updated_at=now()
                    WHERE tenant_id=%s AND graph_version_id=%s AND concept_id=%s
                    """,
                    (status, tenant_id, graph_id, object_id),
                )
                node_count += 1
            else:
                edge_count += 1
        connection.commit()

    cycles = GraphStore(settings.database_url).prerequisite_cycles(
        tenant_id=tenant_id,
        course_id=course_id,
        graph_version_status="draft",
    )
    if cycles:
        raise ValueError(f"Review introduced prerequisite cycles: {cycles}")
    print(
        json.dumps(
            {
                "graph_version": version,
                "graph_status": "draft",
                "nodes_reviewed": node_count,
                "edges_reviewed": edge_count,
                "prerequisite_cycles": cycles,
                "activation_changed": False,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
