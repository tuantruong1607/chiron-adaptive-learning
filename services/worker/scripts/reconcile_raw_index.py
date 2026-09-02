from __future__ import annotations

import argparse
import json
from typing import Any

import httpx
import psycopg

from chiron_worker.config import get_settings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Reconcile active PostgreSQL child chunks with a Qdrant collection"
    )
    parser.add_argument("--collection", required=True)
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    parser.add_argument(
        "--enforce",
        action="store_true",
        help="Delete stale Qdrant points. Refuses to run while PostgreSQL chunks are missing.",
    )
    parser.add_argument("--batch-size", type=int, default=256)
    return parser.parse_args()


def _database_url(value: str) -> str:
    return value.replace("postgresql+psycopg://", "postgresql://", 1)


def resolve_scope(
    connection: psycopg.Connection[Any], tenant_slug: str, course_slug: str
) -> tuple[str, str]:
    tenant = connection.execute(
        "SELECT id::text FROM tenants WHERE slug=%s", (tenant_slug,)
    ).fetchone()
    if tenant is None:
        raise LookupError(f"Unknown tenant: {tenant_slug}")
    tenant_id = str(tenant[0])
    connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
    course = connection.execute(
        "SELECT id::text FROM courses WHERE tenant_id=%s AND slug=%s",
        (tenant_id, course_slug),
    ).fetchone()
    if course is None:
        raise LookupError(f"Unknown course in tenant {tenant_slug}: {course_slug}")
    return tenant_id, str(course[0])


def active_chunk_ids(
    connection: psycopg.Connection[Any], tenant_id: str, course_id: str
) -> set[str]:
    rows = connection.execute(
        """
        SELECT c.id::text
        FROM chunks c
        JOIN source_spans s ON s.id=c.source_span_id
        JOIN document_versions d ON d.id=s.document_version_id
        WHERE c.tenant_id=%s AND d.course_id=%s
          AND c.is_active=true AND c.chunk_type='child'
        """,
        (tenant_id, course_id),
    ).fetchall()
    return {str(row[0]) for row in rows}


def qdrant_point_ids(
    client: httpx.Client,
    *,
    base_url: str,
    collection: str,
    tenant_id: str,
    course_id: str,
) -> set[str]:
    ids: set[str] = set()
    offset: str | int | None = None
    while True:
        body: dict[str, Any] = {
            "filter": {
                "must": [
                    {"key": "tenant_id", "match": {"value": tenant_id}},
                    {"key": "course_id", "match": {"value": course_id}},
                ]
            },
            "limit": 256,
            "with_payload": False,
            "with_vector": False,
        }
        if offset is not None:
            body["offset"] = offset
        response = client.post(
            f"{base_url}/collections/{collection}/points/scroll", json=body
        )
        response.raise_for_status()
        result = response.json()["result"]
        ids.update(str(point["id"]) for point in result.get("points", []))
        offset = result.get("next_page_offset")
        if offset is None:
            return ids


def delete_points(
    client: httpx.Client,
    *,
    base_url: str,
    collection: str,
    point_ids: list[str],
    batch_size: int,
) -> int:
    deleted = 0
    for start in range(0, len(point_ids), batch_size):
        batch = point_ids[start : start + batch_size]
        response = client.post(
            f"{base_url}/collections/{collection}/points/delete?wait=true",
            json={"points": batch},
        )
        response.raise_for_status()
        deleted += len(batch)
    return deleted


def main() -> int:
    args = parse_args()
    if args.batch_size < 1 or args.batch_size > 1000:
        raise ValueError("--batch-size must be between 1 and 1000")
    settings = get_settings()
    base_url = settings.qdrant_url.rstrip("/")
    headers = {"api-key": settings.qdrant_api_key} if settings.qdrant_api_key else {}

    with psycopg.connect(_database_url(settings.database_url)) as connection:
        tenant_id, course_id = resolve_scope(connection, args.tenant, args.course)
        expected_ids = active_chunk_ids(connection, tenant_id, course_id)

    with httpx.Client(headers=headers, timeout=30) as client:
        indexed_ids = qdrant_point_ids(
            client,
            base_url=base_url,
            collection=args.collection,
            tenant_id=tenant_id,
            course_id=course_id,
        )
        missing = sorted(expected_ids - indexed_ids)
        stale = sorted(indexed_ids - expected_ids)
        deleted = 0
        if args.enforce:
            if missing:
                report = {
                    "status": "refused",
                    "reason": "postgresql_chunks_missing_from_qdrant",
                    "collection": args.collection,
                    "postgresql_active_child_chunks": len(expected_ids),
                    "qdrant_scoped_points": len(indexed_ids),
                    "missing_count": len(missing),
                    "stale_count": len(stale),
                    "missing_sample": missing[:20],
                    "stale_sample": stale[:20],
                }
                print(json.dumps(report, ensure_ascii=False, indent=2))
                return 2
            deleted = delete_points(
                client,
                base_url=base_url,
                collection=args.collection,
                point_ids=stale,
                batch_size=args.batch_size,
            )

    report = {
        "status": "reconciled" if args.enforce else "dry_run",
        "collection": args.collection,
        "tenant_id": tenant_id,
        "course_id": course_id,
        "postgresql_active_child_chunks": len(expected_ids),
        "qdrant_scoped_points_before": len(indexed_ids),
        "missing_count": len(missing),
        "stale_count": len(stale),
        "deleted_count": deleted,
        "expected_points_after": len(indexed_ids) - deleted,
        "missing_sample": missing[:20],
        "stale_sample": stale[:20],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
