from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from uuid import UUID

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from .config import WorkerSettings
from .qdrant import Encoder, QdrantChunkIndex


@dataclass(frozen=True, slots=True)
class OutboxEvent:
    id: UUID
    tenant_id: UUID
    payload: dict
    attempts: int


class OutboxStore:
    def __init__(self, settings: WorkerSettings) -> None:
        url = settings.database_url.replace("postgresql://", "postgresql+psycopg://", 1)
        connect_args: dict = {}
        if "postgresql+psycopg" in url:
            connect_args["prepare_threshold"] = None
        self.sessions = sessionmaker(
            bind=create_engine(url, connect_args=connect_args, pool_pre_ping=True), expire_on_commit=False
        )
        self.settings = settings

    @staticmethod
    def set_tenant(session: Session, tenant_id: UUID) -> None:
        session.execute(
            text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
            {"tenant_id": str(tenant_id)},
        )

    def tenant_ids(self) -> list[UUID]:
        with self.sessions() as session:
            return list(
                session.scalars(text("SELECT id FROM tenants WHERE status = 'active' ORDER BY id"))
            )

    def queue_depths(self) -> dict[tuple[str, str], int]:
        depths: dict[tuple[str, str], int] = {}
        for tenant_id in self.tenant_ids():
            with self.sessions() as session, session.begin():
                self.set_tenant(session, tenant_id)
                rows = session.execute(
                    text(
                        "SELECT event_type, status, count(*) AS total FROM outbox_events "
                        "WHERE tenant_id=:tenant_id AND event_type IN "
                        "('chunks.sync_requested', 'essay.grading.requested') "
                        "AND status IN ('pending', 'processing', 'dead') "
                        "GROUP BY event_type, status"
                    ),
                    {"tenant_id": tenant_id},
                ).mappings()
                for row in rows:
                    key = (str(row["event_type"]), str(row["status"]))
                    depths[key] = depths.get(key, 0) + int(row["total"])
        return depths

    def claim(self, tenant_id: UUID) -> list[OutboxEvent]:
        now = datetime.now(UTC)
        stale_before = now - timedelta(seconds=self.settings.outbox_lease_seconds)
        with self.sessions() as session, session.begin():
            self.set_tenant(session, tenant_id)
            session.execute(
                text(
                    "UPDATE outbox_events SET status='pending', locked_at=NULL, locked_by=NULL "
                    "WHERE tenant_id=:tenant_id AND event_type='chunks.sync_requested' "
                    "AND payload->>'embedding_version'=:embedding_version "
                    "AND status='processing' AND locked_at < :stale_before"
                ),
                {
                    "tenant_id": tenant_id,
                    "embedding_version": self.settings.embedding_version,
                    "stale_before": stale_before,
                },
            )
            rows = (
                session.execute(
                    text(
                        "SELECT id, tenant_id, payload, attempts FROM outbox_events "
                        "WHERE tenant_id=:tenant_id AND event_type='chunks.sync_requested' "
                        "AND payload->>'embedding_version'=:embedding_version "
                        "AND status='pending' AND attempts < :max_attempts "
                        "AND (next_attempt_at IS NULL OR next_attempt_at <= :now) "
                        "ORDER BY created_at FOR UPDATE SKIP LOCKED LIMIT :batch_size"
                    ),
                    {
                        "tenant_id": tenant_id,
                        "embedding_version": self.settings.embedding_version,
                        "max_attempts": self.settings.outbox_max_attempts,
                        "now": now,
                        "batch_size": self.settings.outbox_batch_size,
                    },
                )
                .mappings()
                .all()
            )
            if rows:
                session.execute(
                    text(
                        "UPDATE outbox_events SET status='processing', locked_at=:now, "
                        "locked_by=:worker WHERE id = ANY(:ids)"
                    ),
                    {
                        "now": now,
                        "worker": self.settings.worker_id,
                        "ids": [row["id"] for row in rows],
                    },
                )
            return [OutboxEvent(**dict(row)) for row in rows]

    def claim_event_type(self, tenant_id: UUID, event_type: str) -> list[OutboxEvent]:
        """Claim non-vector events without changing the vector sync contract."""
        now = datetime.now(UTC)
        stale_before = now - timedelta(seconds=self.settings.outbox_lease_seconds)
        with self.sessions() as session, session.begin():
            self.set_tenant(session, tenant_id)
            session.execute(
                text(
                    "UPDATE outbox_events SET status='pending', locked_at=NULL, locked_by=NULL "
                    "WHERE tenant_id=:tenant_id AND event_type=:event_type "
                    "AND status='processing' AND locked_at < :stale_before"
                ),
                {
                    "tenant_id": tenant_id,
                    "event_type": event_type,
                    "stale_before": stale_before,
                },
            )
            rows = (
                session.execute(
                    text(
                        "SELECT id, tenant_id, payload, attempts FROM outbox_events "
                        "WHERE tenant_id=:tenant_id AND event_type=:event_type "
                        "AND status='pending' AND attempts < :max_attempts "
                        "AND (next_attempt_at IS NULL OR next_attempt_at <= :now) "
                        "ORDER BY created_at FOR UPDATE SKIP LOCKED LIMIT :batch_size"
                    ),
                    {
                        "tenant_id": tenant_id,
                        "event_type": event_type,
                        "max_attempts": self.settings.outbox_max_attempts,
                        "now": now,
                        "batch_size": self.settings.outbox_batch_size,
                    },
                )
                .mappings()
                .all()
            )
            if rows:
                session.execute(
                    text(
                        "UPDATE outbox_events SET status='processing', locked_at=:now, "
                        "locked_by=:worker WHERE id = ANY(:ids)"
                    ),
                    {"now": now, "worker": self.settings.worker_id, "ids": [row["id"] for row in rows]},
                )
            return [OutboxEvent(**dict(row)) for row in rows]

    def chunks(self, event: OutboxEvent) -> list[dict]:
        chunk_ids = [UUID(value) for value in event.payload.get("chunk_ids", [])]
        if not chunk_ids:
            return []
        with self.sessions() as session, session.begin():
            self.set_tenant(session, event.tenant_id)
            return [
                dict(row)
                for row in session.execute(
                    text(
                        "SELECT c.id, c.tenant_id, c.source_span_id, c.parent_chunk_id, "
                        "c.content, c.checksum, c.is_active, c.chunk_type, c.ordinal, "
                        "c.token_count, c.metadata AS chunk_metadata, s.locator, "
                        "d.id AS document_version_id, d.course_id, d.title AS document_title, "
                        "d.source_path, d.source_type "
                        "FROM chunks c JOIN source_spans s ON s.id=c.source_span_id "
                        "JOIN document_versions d ON d.id=s.document_version_id "
                        "WHERE c.tenant_id=:tenant_id AND c.is_active=true "
                        "AND c.id = ANY(:chunk_ids)"
                    ),
                    {"tenant_id": event.tenant_id, "chunk_ids": chunk_ids},
                ).mappings()
            ]

    def success(self, event: OutboxEvent) -> None:
        with self.sessions() as session, session.begin():
            self.set_tenant(session, event.tenant_id)
            session.execute(
                text(
                    "UPDATE outbox_events SET status='processed', processed_at=now(), "
                    "locked_at=NULL, locked_by=NULL, last_error=NULL WHERE id=:id"
                ),
                {"id": event.id},
            )

    def failure(self, event: OutboxEvent, error: Exception) -> None:
        attempts = event.attempts + 1
        status = "dead" if attempts >= self.settings.outbox_max_attempts else "pending"
        delay = min(300, 2 ** min(attempts, 8))
        with self.sessions() as session, session.begin():
            self.set_tenant(session, event.tenant_id)
            session.execute(
                text(
                    "UPDATE outbox_events SET status=:status, attempts=:attempts, "
                    "next_attempt_at=:next_attempt_at, locked_at=NULL, locked_by=NULL, "
                    "last_error=:last_error WHERE id=:id"
                ),
                {
                    "id": event.id,
                    "status": status,
                    "attempts": attempts,
                    "next_attempt_at": datetime.now(UTC) + timedelta(seconds=delay),
                    "last_error": f"{type(error).__name__}: {error}"[:2000],
                },
            )


class OutboxConsumer:
    def __init__(
        self,
        store: OutboxStore,
        encoder: Encoder,
        index: QdrantChunkIndex,
    ) -> None:
        self.store = store
        self.encoder = encoder
        self.index = index
        self._known_point_ids: dict[tuple[str, str], set[str]] = {}

    def drain_once(self) -> dict[str, int]:
        claimed = processed = failed = 0
        for tenant_id in self.store.tenant_ids():
            events = self.store.claim(tenant_id)
            claimed += len(events)
            upserts: dict[str, list[OutboxEvent]] = defaultdict(list)
            for event in events:
                if event.payload.get("operation", "upsert") != "delete":
                    upserts[str(event.payload.get("embedding_version", "unknown"))].append(
                        event
                    )
                    continue
                try:
                    self.index.delete(event.payload.get("chunk_ids", []))
                    self.store.success(event)
                    processed += 1
                except Exception as exc:
                    self.store.failure(event, exc)
                    failed += 1
            for embedding_version, grouped_events in upserts.items():
                try:
                    chunks = [
                        chunk
                        for event in grouped_events
                        for chunk in self.store.chunks(event)
                    ]
                    pending_chunks: list[dict] = []
                    for chunk in chunks:
                        key = (str(chunk["tenant_id"]), str(chunk["course_id"]))
                        known = self._known_point_ids.get(key)
                        if known is None:
                            known = self.index.point_ids(
                                tenant_id=key[0], course_id=key[1]
                            )
                            self._known_point_ids[key] = known
                        if str(chunk["id"]) not in known:
                            pending_chunks.append(chunk)
                    # FastEmbed batches internally, but bounding each explicit call keeps
                    # peak memory predictable on small deployment workers.
                    for start in range(0, len(pending_chunks), 32):
                        batch = pending_chunks[start : start + 32]
                        dense, sparse = self.encoder.encode(
                            [chunk["content"] for chunk in batch]
                        )
                        self.index.upsert(
                            batch,
                            dense,
                            sparse,
                            embedding_version=embedding_version,
                        )
                        for chunk in batch:
                            key = (str(chunk["tenant_id"]), str(chunk["course_id"]))
                            self._known_point_ids[key].add(str(chunk["id"]))
                    for event in grouped_events:
                        self.store.success(event)
                        processed += 1
                except Exception as exc:
                    for event in grouped_events:
                        self.store.failure(event, exc)
                        failed += 1
        return {"claimed": claimed, "processed": processed, "failed": failed}
