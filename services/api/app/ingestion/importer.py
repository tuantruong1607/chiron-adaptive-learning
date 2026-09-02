from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from uuid import NAMESPACE_URL, UUID, uuid5

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session, sessionmaker

from ..db import set_tenant_context
from ..persistence.tables import (
    chunks,
    courses,
    document_versions,
    outbox_events,
    source_spans,
    tenants,
)
from .chunking import CHUNKER_VERSION, hierarchical_chunks

DEFAULT_EMBEDDING_VERSION = "multilingual-e5-large-mean-batch32-v2"
DEFAULT_OUTBOX_CHUNK_BATCH_SIZE = 32


@dataclass(slots=True)
class CorpusImportReport:
    documents: int = 0
    source_spans: int = 0
    parent_chunks: int = 0
    child_chunks: int = 0
    outbox_events: int = 0
    obsolete_chunks: int = 0

    def as_dict(self) -> dict[str, int]:
        return {
            "documents": self.documents,
            "source_spans": self.source_spans,
            "parent_chunks": self.parent_chunks,
            "child_chunks": self.child_chunks,
            "outbox_events": self.outbox_events,
            "obsolete_chunks": self.obsolete_chunks,
        }


def scoped_id(tenant_id: UUID, course_id: UUID, kind: str, identity: str) -> UUID:
    return uuid5(NAMESPACE_URL, f"chiron:{tenant_id}:{course_id}:{kind}:{identity}")


def _load(data_root: Path) -> tuple[dict, list[dict]]:
    manifest_path = data_root / "manifests" / "corpus.json"
    spans_path = data_root / "manifests" / "source_spans.jsonl"
    if not manifest_path.exists() or not spans_path.exists():
        raise FileNotFoundError("Expected data/manifests/corpus.json and source_spans.jsonl")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    spans = [json.loads(line) for line in spans_path.read_text(encoding="utf-8").splitlines() if line]
    if manifest.get("course_id") != "rag-intensive":
        raise ValueError("Corpus course_id must be rag-intensive")
    if manifest["summary"]["source_spans"] != len(spans):
        raise ValueError("Manifest/source span count mismatch")
    return manifest, spans


def _outbox(
    session: Session,
    tenant_id: UUID,
    document_id: UUID,
    chunk_ids: list[UUID],
    operation: str,
    embedding_version: str,
    chunk_batch_size: int,
) -> int:
    if not chunk_ids:
        return 0
    if chunk_batch_size < 1:
        raise ValueError("chunk_batch_size must be positive")
    inserted = 0
    for offset in range(0, len(chunk_ids), chunk_batch_size):
        batch = chunk_ids[offset : offset + chunk_batch_size]
        identity = sha256("|".join(str(value) for value in batch).encode()).hexdigest()
        dedupe_key = f"chunks.{operation}:{document_id}:{embedding_version}:{identity}"
        event_id = scoped_id(tenant_id, document_id, "outbox", dedupe_key)
        inserted_id = session.scalar(
            pg_insert(outbox_events)
            .values(
                id=event_id,
                tenant_id=tenant_id,
                event_type="chunks.sync_requested",
                aggregate_id=document_id,
                payload={
                    "chunk_ids": [str(value) for value in batch],
                    "operation": operation,
                    "embedding_version": embedding_version,
                },
                dedupe_key=dedupe_key,
                status="pending",
                attempts=0,
            )
            .on_conflict_do_nothing(constraint="uq_outbox_event_dedupe")
            .returning(outbox_events.c.id)
        )
        inserted += int(inserted_id is not None)
    return inserted


def _import_document(
    session: Session,
    tenant_id: UUID,
    course_id: UUID,
    document: dict,
    duplicate_sources: list[str],
    staging_spans: list[dict],
    report: CorpusImportReport,
    target_tokens: int,
    max_tokens: int,
    overlap_tokens: int,
    embedding_version: str,
    outbox_chunk_batch_size: int,
) -> None:
    checksum = document["source_sha256"]
    proposed_document_id = scoped_id(tenant_id, course_id, "document", checksum)
    values = {
        "id": proposed_document_id,
        "tenant_id": tenant_id,
        "course_id": course_id,
        "checksum": checksum,
        "source_type": document["source_type"],
        "status": "active",
        "title": document["title"],
        "source_path": document["source"],
        "parser_version": document.get("parser_version", "chiron-structured-markdown-v1"),
        "metadata": {
            "authority": document.get("authority", "primary"),
            "document_kind": document["kind"],
            "staging_document_id": document.get("document_id"),
            "staging_document_version_id": document["document_version_id"],
            "markdown_path": document["output"],
            "duplicate_sources": duplicate_sources,
        },
    }
    document_id = session.scalar(
        pg_insert(document_versions)
        .values(**values)
        .on_conflict_do_update(
            constraint="uq_document_versions_checksum",
            set_={key: values[key] for key in ("status", "title", "source_path", "parser_version", "metadata")},
        )
        .returning(document_versions.c.id)
    )
    if document_id is None:
        raise RuntimeError("Document upsert did not return an ID")
    report.documents += 1
    new_child_ids: list[UUID] = []
    obsolete_child_ids: list[UUID] = []
    for staging_span in staging_spans:
        staging_span_id = staging_span["source_span_id"]
        span_id = scoped_id(tenant_id, course_id, "source-span", staging_span_id)
        span_values = {
            "id": span_id,
            "tenant_id": tenant_id,
            "document_version_id": document_id,
            "locator": staging_span["locator"],
            "text": staging_span.get("text", ""),
            "checksum": staging_span["checksum"],
        }
        session.execute(
            pg_insert(source_spans)
            .values(**span_values)
            .on_conflict_do_update(
                index_elements=[source_spans.c.id],
                set_={key: span_values[key] for key in ("locator", "text", "checksum", "document_version_id")},
            )
        )
        report.source_spans += 1
        previous_children = set(
            session.scalars(
                select(chunks.c.id).where(
                    chunks.c.source_span_id == span_id,
                    chunks.c.chunk_type == "child",
                    chunks.c.is_active.is_(True),
                )
            )
        )
        drafts = hierarchical_chunks(
            staging_span.get("text", ""), target_tokens, max_tokens, overlap_tokens
        )
        if not drafts:
            obsolete_child_ids.extend(previous_children)
            session.execute(
                update(chunks).where(chunks.c.source_span_id == span_id).values(is_active=False)
            )
            continue
        checksums = [sha256(draft.content.encode()).hexdigest() for draft in drafts]
        ids = [
            scoped_id(
                tenant_id,
                course_id,
                "chunk",
                f"{CHUNKER_VERSION}:{staging_span_id}:{draft.chunk_type}:{draft.ordinal}:{digest}",
            )
            for draft, digest in zip(drafts, checksums, strict=True)
        ]
        parent_id = ids[0]
        active_ids = set(ids)
        obsolete_child_ids.extend(previous_children - active_ids)
        session.execute(
            update(chunks)
            .where(chunks.c.source_span_id == span_id, chunks.c.id.not_in(active_ids))
            .values(is_active=False)
        )
        for draft, digest, chunk_id in zip(drafts, checksums, ids, strict=True):
            chunk_values = {
                "id": chunk_id,
                "tenant_id": tenant_id,
                "source_span_id": span_id,
                "parent_chunk_id": None if draft.chunk_type == "parent" else parent_id,
                "content": draft.content,
                "checksum": digest,
                "is_active": True,
                "chunk_type": draft.chunk_type,
                "ordinal": draft.ordinal,
                "token_count": draft.token_count,
                "metadata": {
                    "chunker_version": CHUNKER_VERSION,
                    "locator": staging_span["locator"],
                    "staging_source_span_id": staging_span_id,
                },
            }
            session.execute(
                pg_insert(chunks)
                .values(**chunk_values)
                .on_conflict_do_update(
                    index_elements=[chunks.c.id],
                    set_={key: chunk_values[key] for key in (
                        "parent_chunk_id", "content", "checksum", "is_active", "chunk_type",
                        "ordinal", "token_count", "metadata",
                    )},
                )
            )
            if draft.chunk_type == "parent":
                report.parent_chunks += 1
            else:
                report.child_chunks += 1
                new_child_ids.append(chunk_id)
    report.obsolete_chunks += len(set(obsolete_child_ids))
    report.outbox_events += _outbox(
        session,
        tenant_id,
        document_id,
        sorted(set(obsolete_child_ids), key=str),
        "delete",
        embedding_version,
        outbox_chunk_batch_size,
    )
    report.outbox_events += _outbox(
        session,
        tenant_id,
        document_id,
        sorted(set(new_child_ids), key=str),
        "upsert",
        embedding_version,
        outbox_chunk_batch_size,
    )


def import_corpus(
    session_factory: sessionmaker[Session],
    data_root: Path,
    tenant_slug: str = "demo",
    course_slug: str = "rag-intensive",
    target_tokens: int = 500,
    max_tokens: int = 700,
    overlap_tokens: int = 80,
    embedding_version: str = DEFAULT_EMBEDDING_VERSION,
    outbox_chunk_batch_size: int = DEFAULT_OUTBOX_CHUNK_BATCH_SIZE,
) -> CorpusImportReport:
    manifest, staging_spans = _load(data_root)
    with session_factory() as session, session.begin():
        tenant_id = session.scalar(select(tenants.c.id).where(tenants.c.slug == tenant_slug))
        if tenant_id is None:
            raise LookupError(f"Tenant not found: {tenant_slug}")
        set_tenant_context(session, tenant_id)
        course_id = session.scalar(
            select(courses.c.id).where(courses.c.tenant_id == tenant_id, courses.c.slug == course_slug)
        )
        if course_id is None:
            raise LookupError(f"Course not found: {course_slug}")
    spans_by_document: dict[str, list[dict]] = defaultdict(list)
    for span in staging_spans:
        spans_by_document[span["document_version_id"]].append(span)
    documents = [d for d in manifest["documents"] if d.get("status") == "ok" and not d.get("duplicate_of")]
    duplicates_by_checksum: dict[str, list[str]] = defaultdict(list)
    for document in manifest["documents"]:
        if document.get("duplicate_of"):
            duplicates_by_checksum[document["source_sha256"]].append(document["source"])
    report = CorpusImportReport()
    for document in documents:
        with session_factory() as session, session.begin():
            set_tenant_context(session, tenant_id)
            _import_document(
                session, tenant_id, course_id, document,
                duplicates_by_checksum.get(document["source_sha256"], []),
                spans_by_document.get(document["document_version_id"], []), report,
                target_tokens, max_tokens, overlap_tokens, embedding_version,
                outbox_chunk_batch_size,
            )
    return report
