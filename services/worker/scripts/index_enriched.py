from __future__ import annotations

import argparse
import json
from collections.abc import Iterator
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from typing import Any

import psycopg
from psycopg.rows import dict_row

from chiron_worker.config import get_settings
from chiron_worker.enrichment import ENRICHMENT_VERSION, blend_dense_vectors, enrich_chunk
from chiron_worker.qdrant import FastEmbedEncoder, QdrantChunkIndex


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a versioned enriched retrieval collection")
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    parser.add_argument(
        "--variant",
        choices=("context", "context_terms", "context_terms_pedagogy"),
        default="context_terms_pedagogy",
    )
    parser.add_argument("--collection")
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--reuse-dense-from",
        help="Reuse raw dense vectors from this collection and embed context only",
    )
    parser.add_argument("--context-weight", type=float, default=0.20)
    parser.add_argument(
        "--no-resume",
        action="store_false",
        dest="resume",
        help="Re-embed points already present in the experiment collection",
    )
    parser.set_defaults(resume=True)
    return parser.parse_args()


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


def chunk_batches(
    connection: psycopg.Connection,
    *,
    tenant_id: str,
    course_id: str,
    batch_size: int,
    limit: int | None,
) -> Iterator[list[dict[str, Any]]]:
    connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
    query = """
        SELECT c.id, c.tenant_id, c.source_span_id, c.parent_chunk_id,
               c.content, c.checksum, c.is_active, c.chunk_type, c.ordinal,
               c.token_count, c.metadata AS chunk_metadata, s.locator,
               d.id AS document_version_id, d.course_id, d.title AS document_title,
               d.source_path, d.source_type, co.title AS course_title
        FROM chunks c
        JOIN source_spans s ON s.id=c.source_span_id
        JOIN document_versions d ON d.id=s.document_version_id
        JOIN courses co ON co.id=d.course_id
        WHERE c.tenant_id=%s AND d.course_id=%s
          AND c.chunk_type='child' AND c.is_active
        ORDER BY c.id
    """
    params: list[Any] = [tenant_id, course_id]
    if limit is not None:
        query += " LIMIT %s"
        params.append(limit)
    with connection.cursor(name="enriched-chunks", row_factory=dict_row) as cursor:
        cursor.execute(query, params)
        while rows := cursor.fetchmany(batch_size):
            yield [dict(row) for row in rows]


def main() -> int:
    args = parse_args()
    if args.batch_size < 1:
        raise ValueError("--batch-size must be positive")
    if args.limit is not None and args.limit < 1:
        raise ValueError("--limit must be positive")
    if not 0.0 <= args.context_weight <= 1.0:
        raise ValueError("--context-weight must be between 0 and 1")

    settings = get_settings()
    if settings.embedding_provider != "local":
        raise RuntimeError("Corpus enrichment requires EMBEDDING_PROVIDER=local")
    suffix = str(args.variant).replace("_", "-")
    collection = args.collection or f"{settings.qdrant_collection}-enriched-{suffix}-v1"
    experiment_settings = settings.model_copy(update={"qdrant_collection": collection})
    encoder = FastEmbedEncoder(
        settings.embedding_model,
        settings.sparse_embedding_model,
        settings.embedding_cache_path,
    )
    index = QdrantChunkIndex(experiment_settings)
    raw_index = (
        QdrantChunkIndex(settings.model_copy(update={"qdrant_collection": args.reuse_dense_from}))
        if args.reuse_dense_from
        else None
    )

    started = perf_counter()
    indexed = 0
    skipped_existing = 0
    contextualized = 0
    reused_dense = 0
    embedded_contexts = 0
    fallback_dense_reembedded = 0
    total_chunks_seen = 0
    raw_checksums: list[str] = []
    retrieval_checksums: list[str] = []
    with psycopg.connect(_database_url(settings.database_url)) as connection:
        tenant_id, course_id = resolve_scope(connection, args.tenant, args.course)
        existing_ids = (
            index.point_ids(tenant_id=tenant_id, course_id=course_id) if args.resume else set()
        )
        for batch in chunk_batches(
            connection,
            tenant_id=tenant_id,
            course_id=course_id,
            batch_size=args.batch_size,
            limit=args.limit,
        ):
            pending_batch = [chunk for chunk in batch if str(chunk["id"]) not in existing_ids]
            skipped_existing += len(batch) - len(pending_batch)
            total_chunks_seen += len(batch)
            if not pending_batch:
                continue
            enriched = [
                enrich_chunk(chunk, variant=args.variant)  # type: ignore[arg-type]
                for chunk in pending_batch
            ]
            retrieval_texts = [result.retrieval_text for result in enriched]
            if raw_index is None:
                dense, sparse = encoder.encode(retrieval_texts)
            else:
                raw_points = raw_index.dense_points(
                    [str(chunk["id"]) for chunk in pending_batch]
                )
                context_positions = [
                    index
                    for index, result in enumerate(enriched)
                    if result.context_text and args.context_weight > 0
                ]
                context_vectors = encoder.encode_dense(
                    [enriched[index].context_text for index in context_positions]
                )
                context_by_position = dict(zip(context_positions, context_vectors, strict=True))
                fallback_positions: list[int] = []
                for position, chunk in enumerate(pending_batch):
                    raw_point = raw_points.get(str(chunk["id"]))
                    payload = raw_point.get("payload", {}) if raw_point else {}
                    vector = raw_point.get("dense") if raw_point else None
                    if (
                        payload.get("checksum") != chunk["checksum"]
                        or payload.get("embedding_version") != settings.embedding_version
                        or not isinstance(vector, list)
                        or not vector
                    ):
                        fallback_positions.append(position)
                fallback_vectors = encoder.encode_dense(
                    [enriched[position].raw_content for position in fallback_positions]
                )
                fallback_by_position = dict(
                    zip(fallback_positions, fallback_vectors, strict=True)
                )
                dense = []
                for position, (chunk, _result) in enumerate(
                    zip(pending_batch, enriched, strict=True)
                ):
                    raw_point = raw_points.get(str(chunk["id"]))
                    raw_vector = fallback_by_position.get(position)
                    if raw_vector is None and raw_point is not None:
                        raw_vector = raw_point.get("dense")
                    if not isinstance(raw_vector, list) or not raw_vector:
                        raise RuntimeError(f"Dense fallback failed for chunk {chunk['id']}")
                    context_vector = context_by_position.get(position)
                    dense.append(
                        blend_dense_vectors(raw_vector, context_vector, args.context_weight)
                        if context_vector is not None
                        else raw_vector
                    )
                    reused_dense += int(position not in fallback_by_position)
                    fallback_dense_reembedded += int(position in fallback_by_position)
                    embedded_contexts += int(context_vector is not None)
                sparse = encoder.encode_sparse(retrieval_texts)
            indexed_chunks = []
            for chunk, result in zip(pending_batch, enriched, strict=True):
                indexed_chunks.append(
                    {
                        **chunk,
                        "retrieval_text": result.retrieval_text,
                        "raw_checksum": result.raw_checksum,
                        "retrieval_text_checksum": result.retrieval_text_checksum,
                        "enrichment_version": result.enrichment_version,
                        "enrichment_variant": result.variant,
                        "enrichment_provenance": list(result.provenance),
                        "enrichment_aliases": list(result.aliases),
                        "enrichment_entities": list(result.entities),
                        "enrichment_pedagogy_labels": list(result.pedagogy_labels),
                        "enrichment_contextualized": result.contextualized,
                        "estimated_header_tokens": result.estimated_header_tokens,
                        "estimated_retrieval_tokens": result.estimated_retrieval_tokens,
                    }
                )
                contextualized += int(result.contextualized)
                raw_checksums.append(result.raw_checksum)
                retrieval_checksums.append(result.retrieval_text_checksum)
            index.upsert(
                indexed_chunks,
                dense,
                sparse,
                embedding_version=f"{settings.embedding_version}+{ENRICHMENT_VERSION}:{args.variant}",
            )
            indexed += len(pending_batch)
            print(
                json.dumps(
                    {
                        "indexed": indexed,
                        "skipped_existing": skipped_existing,
                        "collection": collection,
                    }
                ),
                flush=True,
            )

    report = {
        "status": "indexed",
        "created_at": datetime.now(UTC).isoformat(),
        "tenant_id": tenant_id,
        "course_id": course_id,
        "collection": collection,
        "variant": args.variant,
        "enrichment_version": ENRICHMENT_VERSION,
        "embedding_model": settings.embedding_model,
        "embedding_version": settings.embedding_version,
        "indexed_chunks": indexed,
        "skipped_existing_chunks": skipped_existing,
        "total_chunks_seen": total_chunks_seen,
        "collection_points_after_run": indexed + skipped_existing,
        "contextualized_chunks": contextualized,
        "dense_strategy": (
            "reuse_raw"
            if raw_index and args.context_weight == 0
            else "reuse_and_blend_context"
            if raw_index
            else "full_reembed"
        ),
        "raw_dense_collection": args.reuse_dense_from,
        "context_weight": args.context_weight if raw_index else None,
        "reused_dense_chunks": reused_dense,
        "fallback_dense_reembedded_chunks": fallback_dense_reembedded,
        "embedded_contexts": embedded_contexts,
        "unique_raw_checksums": len(set(raw_checksums)),
        "unique_retrieval_checksums": len(set(retrieval_checksums)),
        "elapsed_seconds": round(perf_counter() - started, 3),
        "local_only": True,
    }
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
