from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta
from typing import Any
from uuid import UUID, uuid4

import psycopg
from psycopg.types.json import Jsonb

from .config import WorkerSettings

SENSITIVE_KEYS = {
    "answer",
    "answers",
    "code",
    "content",
    "essay",
    "prompt",
    "query",
    "response",
    "submission",
    "text",
}
REDACTED = "[redacted:retention]"


@dataclass(frozen=True, slots=True)
class RetentionPolicy:
    learner_content_days: int
    processed_outbox_days: int
    auth_session_grace_days: int
    batch_size: int


def policy_from_settings(settings: WorkerSettings) -> RetentionPolicy:
    return RetentionPolicy(
        learner_content_days=settings.retention_learner_content_days,
        processed_outbox_days=settings.retention_processed_outbox_days,
        auth_session_grace_days=settings.retention_auth_session_grace_days,
        batch_size=settings.retention_batch_size,
    )


def redact_payload(value: Any) -> Any:
    if isinstance(value, dict):
        redacted: dict[str, Any] = {}
        for key, item in value.items():
            redacted[key] = REDACTED if key.casefold() in SENSITIVE_KEYS else redact_payload(item)
        redacted["retention_redacted"] = True
        return redacted
    if isinstance(value, list):
        return [redact_payload(item) for item in value]
    return value


class RetentionEnforcer:
    def __init__(self, database_url: str, policy: RetentionPolicy) -> None:
        self.database_url = database_url.replace("postgresql+psycopg://", "postgresql://", 1)
        self.policy = policy

    def run(self, *, dry_run: bool) -> dict[str, Any]:
        started_at = datetime.now(UTC)
        totals: dict[str, int] = {}
        with psycopg.connect(self.database_url) as connection:
            tenant_ids = [
                UUID(str(row[0]))
                for row in connection.execute(
                    "SELECT id FROM tenants WHERE status='active' ORDER BY id"
                ).fetchall()
            ]
            for tenant_id in tenant_ids:
                counts = self._tenant(connection, tenant_id, started_at, dry_run=dry_run)
                for table, count in counts.items():
                    totals[table] = totals.get(table, 0) + count
            if dry_run:
                connection.rollback()
            else:
                connection.commit()
        return {
            "status": "dry_run" if dry_run else "completed",
            "started_at": started_at.isoformat(),
            "completed_at": datetime.now(UTC).isoformat(),
            "policy": asdict(self.policy),
            "affected_rows": totals,
        }

    def _tenant(
        self,
        connection: psycopg.Connection,
        tenant_id: UUID,
        now: datetime,
        *,
        dry_run: bool,
    ) -> dict[str, int]:
        connection.execute("SELECT set_config('app.tenant_id', %s, false)", (str(tenant_id),))
        learner_cutoff = now - timedelta(days=self.policy.learner_content_days)
        outbox_cutoff = now - timedelta(days=self.policy.processed_outbox_days)
        auth_cutoff = now - timedelta(days=self.policy.auth_session_grace_days)
        counts = {
            "chat_messages": self._redact_chat(connection, tenant_id, learner_cutoff, dry_run),
            "attempts": self._redact_json(
                connection, "attempts", "payload", tenant_id, learner_cutoff, dry_run
            ),
            "learning_events": self._redact_json(
                connection, "learning_events", "payload", tenant_id, learner_cutoff, dry_run
            ),
            "outbox_events": self._redact_outbox(
                connection, tenant_id, outbox_cutoff, dry_run
            ),
            "auth_refresh_sessions": self._expire_sessions(
                connection, tenant_id, auth_cutoff, dry_run
            ),
        }
        if not dry_run:
            completed_at = datetime.now(UTC)
            connection.execute(
                "INSERT INTO data_retention_runs "
                "(id, tenant_id, status, policy, affected_rows, started_at, completed_at) "
                "VALUES (%s, %s, 'completed', %s, %s, %s, %s)",
                (
                    uuid4(),
                    tenant_id,
                    Jsonb(asdict(self.policy)),
                    Jsonb(counts),
                    now,
                    completed_at,
                ),
            )
        return counts

    def _ids(
        self,
        connection: psycopg.Connection,
        query: str,
        params: tuple[Any, ...],
    ) -> list[UUID]:
        return [UUID(str(row[0])) for row in connection.execute(query, params).fetchall()]

    def _redact_chat(
        self, connection: psycopg.Connection, tenant_id: UUID, cutoff: datetime, dry_run: bool
    ) -> int:
        ids = self._ids(
            connection,
            "SELECT id FROM chat_messages WHERE tenant_id=%s AND created_at < %s "
            "AND COALESCE(metadata->>'retention_redacted', 'false') <> 'true' "
            "ORDER BY created_at LIMIT %s FOR UPDATE SKIP LOCKED",
            (tenant_id, cutoff, self.policy.batch_size),
        )
        if ids and not dry_run:
            connection.execute(
                "UPDATE chat_messages SET content=%s, citations='[]'::jsonb, "
                "metadata=COALESCE(metadata, '{}'::jsonb) || %s WHERE id=ANY(%s)",
                (REDACTED, Jsonb({"retention_redacted": True}), ids),
            )
        return len(ids)

    def _redact_json(
        self,
        connection: psycopg.Connection,
        table: str,
        column: str,
        tenant_id: UUID,
        cutoff: datetime,
        dry_run: bool,
    ) -> int:
        rows = connection.execute(
            f"SELECT id, {column} FROM {table} WHERE tenant_id=%s AND created_at < %s "
            f"AND COALESCE({column}->>'retention_redacted', 'false') <> 'true' "
            "ORDER BY created_at LIMIT %s FOR UPDATE SKIP LOCKED",
            (tenant_id, cutoff, self.policy.batch_size),
        ).fetchall()
        if not dry_run:
            for row_id, payload in rows:
                connection.execute(
                    f"UPDATE {table} SET {column}=%s WHERE id=%s",
                    (Jsonb(redact_payload(payload or {})), row_id),
                )
        return len(rows)

    def _redact_outbox(
        self, connection: psycopg.Connection, tenant_id: UUID, cutoff: datetime, dry_run: bool
    ) -> int:
        ids = self._ids(
            connection,
            "SELECT id FROM outbox_events WHERE tenant_id=%s AND status='processed' "
            "AND processed_at < %s AND COALESCE(payload->>'retention_redacted', 'false') <> 'true' "
            "ORDER BY processed_at LIMIT %s FOR UPDATE SKIP LOCKED",
            (tenant_id, cutoff, self.policy.batch_size),
        )
        if ids and not dry_run:
            connection.execute(
                "UPDATE outbox_events SET payload=%s, last_error=NULL WHERE id=ANY(%s)",
                (Jsonb({"retention_redacted": True}), ids),
            )
        return len(ids)

    def _expire_sessions(
        self, connection: psycopg.Connection, tenant_id: UUID, cutoff: datetime, dry_run: bool
    ) -> int:
        ids = self._ids(
            connection,
            "SELECT id FROM auth_refresh_sessions WHERE tenant_id=%s "
            "AND ((expires_at < %s) OR (revoked_at IS NOT NULL AND revoked_at < %s)) "
            "ORDER BY expires_at LIMIT %s FOR UPDATE SKIP LOCKED",
            (tenant_id, cutoff, cutoff, self.policy.batch_size),
        )
        if ids and not dry_run:
            connection.execute("DELETE FROM auth_refresh_sessions WHERE id=ANY(%s)", (ids,))
        return len(ids)
