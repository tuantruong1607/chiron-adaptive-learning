from __future__ import annotations

import argparse
import json
from typing import Any
from uuid import UUID

import httpx
import psycopg
from psycopg.rows import dict_row

from chiron_worker.config import get_settings
from chiron_worker.enrichment import enrich_chunk, validate_enriched_payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify PostgreSQL/Qdrant payload integrity")
    parser.add_argument("--collection", required=True)
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    parser.add_argument("--expected-count", type=int)
    return parser.parse_args()


def validate_raw_payload(payload: dict[str, Any], expected: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("tenant_id", "course_id", "source_span_id"):
        if str(payload.get(key)) != str(expected.get(key)):
            errors.append(f"{key}_mismatch")
    if payload.get("content") != expected.get("content"):
        errors.append("raw_content_mismatch")
    if payload.get("checksum") != expected.get("checksum"):
        errors.append("raw_checksum_mismatch")
    if payload.get("chunk_type") != "child":
        errors.append("chunk_type_mismatch")
    if payload.get("is_active") is not True:
        errors.append("inactive_point")
    if not payload.get("embedding_version"):
        errors.append("missing_embedding_version")
    return errors


def _database_url(value: str) -> str:
    return value.replace("postgresql+psycopg://", "postgresql://", 1)


def resolve_scope(connection: psycopg.Connection, tenant_slug: str, course_slug: str) -> tuple[str, str]:
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


def scroll_points(
    client: httpx.Client,
    *,
    base_url: str,
    collection: str,
    tenant_id: str,
    course_id: str,
) -> list[dict[str, Any]]:
    points: list[dict[str, Any]] = []
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
            "with_payload": True,
            "with_vector": False,
        }
        if offset is not None:
            body["offset"] = offset
        response = client.post(
            f"{base_url}/collections/{collection}/points/scroll", json=body
        )
        response.raise_for_status()
        result = response.json()["result"]
        points.extend(result.get("points", []))
        offset = result.get("next_page_offset")
        if offset is None:
            return points


def main() -> int:
    args = parse_args()
    settings = get_settings()
    headers = {"api-key": settings.qdrant_api_key} if settings.qdrant_api_key else {}
    with psycopg.connect(_database_url(settings.database_url)) as connection:
        tenant_id, course_id = resolve_scope(connection, args.tenant, args.course)
        with httpx.Client(headers=headers, timeout=30) as client:
            points = scroll_points(
                client,
                base_url=settings.qdrant_url.rstrip("/"),
                collection=args.collection,
                tenant_id=tenant_id,
                course_id=course_id,
            )
        point_ids = [UUID(str(point["id"])) for point in points]
        expected_rows: dict[str, dict[str, Any]] = {}
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT c.id::text
                FROM chunks c
                JOIN source_spans s ON s.id=c.source_span_id
                JOIN document_versions d ON d.id=s.document_version_id
                WHERE c.tenant_id=%s AND d.course_id=%s
                  AND c.is_active=true AND c.chunk_type='child'
                """,
                (tenant_id, course_id),
            )
            expected_active_ids = {str(row[0]) for row in cursor.fetchall()}
        if point_ids:
            with connection.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    """
                    SELECT c.id::text, c.tenant_id::text, d.course_id::text,
                           c.source_span_id::text, c.content, c.checksum,
                           c.token_count, s.locator, d.title AS document_title,
                           d.source_type, co.title AS course_title
                    FROM chunks c
                    JOIN source_spans s ON s.id=c.source_span_id
                    JOIN document_versions d ON d.id=s.document_version_id
                    JOIN courses co ON co.id=d.course_id
                    WHERE c.tenant_id=%s AND d.course_id=%s AND c.id=ANY(%s)
                    """,
                    (tenant_id, course_id, point_ids),
                )
                rows = cursor.fetchall()
            expected_rows = {str(row["id"]): dict(row) for row in rows}

    violations: list[dict[str, Any]] = []
    point_id_set = {str(point_id) for point_id in point_ids}
    for chunk_id in sorted(expected_active_ids - point_id_set):
        violations.append({"point_id": chunk_id, "errors": ["chunk_missing_from_qdrant"]})
    for point in points:
        point_id = str(point["id"])
        expected = expected_rows.get(point_id)
        payload = point.get("payload") or {}
        if expected is None:
            errors = ["point_missing_from_postgresql"]
        else:
            variant = payload.get("enrichment_variant")
            if variant is None:
                errors = validate_raw_payload(payload, expected)
            else:
                try:
                    rebuilt = enrich_chunk(expected, variant=variant)
                    expected["retrieval_text_checksum"] = rebuilt.retrieval_text_checksum
                    errors = validate_enriched_payload(payload, expected)
                except (TypeError, ValueError) as exc:
                    errors = [f"enrichment_rebuild_failed:{exc}"]
        if errors:
            violations.append({"point_id": point_id, "errors": errors})
    if len(point_ids) != len(set(point_ids)):
        violations.append({"point_id": None, "errors": ["duplicate_point_ids"]})
    if args.expected_count is not None and len(points) != args.expected_count:
        violations.append(
            {
                "point_id": None,
                "errors": [f"expected_{args.expected_count}_points_got_{len(points)}"],
            }
        )
    report = {
        "status": "passed" if not violations else "failed",
        "collection": args.collection,
        "tenant_id": tenant_id,
        "course_id": course_id,
        "points": len(points),
        "expected_active_child_chunks": len(expected_active_ids),
        "postgresql_matches": len(expected_rows),
        "payload_modes": sorted(
            {"enriched" if (point.get("payload") or {}).get("enrichment_variant") else "raw" for point in points}
        ),
        "violations": violations[:50],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not violations else 1


if __name__ == "__main__":
    raise SystemExit(main())
