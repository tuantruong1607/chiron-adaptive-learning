from __future__ import annotations

import argparse
import json
import os
from uuid import UUID

import psycopg
from psycopg.rows import dict_row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect dead outbox events; replay only explicitly reviewed event IDs"
    )
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--event-id", action="append", type=UUID, dest="event_ids")
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--reason", help="Required audit reason when replaying")
    return parser.parse_args()


def database_url() -> str:
    value = os.getenv("OPS_DATABASE_URL") or os.getenv("DATABASE_ADMIN_URL")
    if not value:
        raise RuntimeError("OPS_DATABASE_URL or DATABASE_ADMIN_URL is required")
    return value.replace("postgresql+psycopg://", "postgresql://", 1)


def inspect_dead_letters(
    connection: psycopg.Connection,
    *,
    limit: int,
    event_ids: list[UUID] | None,
) -> list[dict]:
    conditions = ["status = 'dead'"]
    params: list[object] = []
    if event_ids:
        conditions.append("id = ANY(%s)")
        params.append(event_ids)
    params.append(limit)
    query = f"""
        SELECT id::text, tenant_id::text, event_type, status, attempts,
               next_attempt_at, last_error, created_at, processed_at
        FROM outbox_events
        WHERE {' AND '.join(conditions)}
        ORDER BY created_at DESC
        LIMIT %s
    """
    with connection.cursor(row_factory=dict_row) as cursor:
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]


def replay(
    connection: psycopg.Connection,
    *,
    event_ids: list[UUID],
    reason: str,
) -> list[str]:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE outbox_events
            SET status='pending', attempts=0, next_attempt_at=NULL,
                locked_at=NULL, locked_by=NULL,
                last_error=%s
            WHERE status='dead' AND id = ANY(%s)
            RETURNING id::text
            """,
            (f"manual replay: {reason}"[:2000], event_ids),
        )
        return [str(row[0]) for row in cursor.fetchall()]


def main() -> int:
    args = parse_args()
    if args.limit < 1 or args.limit > 1000:
        raise SystemExit("--limit must be between 1 and 1000")
    if args.replay and not args.event_ids:
        raise SystemExit("--replay requires one or more --event-id values")
    if args.replay and (not args.reason or len(args.reason.strip()) < 10):
        raise SystemExit("--replay requires --reason with at least 10 characters")

    with psycopg.connect(database_url()) as connection:
        rows = inspect_dead_letters(
            connection,
            limit=args.limit,
            event_ids=args.event_ids,
        )
        inspected_count = len(rows)
        replayed: list[str] = []
        if args.replay:
            replayed = replay(connection, event_ids=args.event_ids, reason=args.reason.strip())
            rows = inspect_dead_letters(connection, limit=args.limit, event_ids=args.event_ids)

    print(
        json.dumps(
            {
                "status": "replayed" if args.replay else "inspected",
                "inspected_count": inspected_count,
                "remaining_dead_count": len(rows),
                "replayed_ids": replayed,
                "events": rows,
            },
            ensure_ascii=False,
            indent=2,
            default=str,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
