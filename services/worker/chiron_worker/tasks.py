from functools import lru_cache
from hashlib import sha256
from threading import Lock
from time import perf_counter
from typing import Any

from .app import celery_app
from .config import get_settings
from .essay_grading import EssayGradingConsumer
from .graph import GraphLiteRetriever, GraphStore
from .metrics import (
    GRADING_SLA_ESCALATIONS,
    RETENTION_ROWS,
    RETENTION_RUNS,
    RETRIEVAL_DURATION,
    record_outbox,
    update_queue_depths,
)
from .outbox import OutboxConsumer, OutboxStore
from .qdrant import (
    Encoder,
    FastEmbedEncoder,
    FastEmbedReranker,
    OpenAIEncoder,
    QdrantChunkIndex,
    QdrantCloudInferenceEncoder,
)
from .retention import RetentionEnforcer, policy_from_settings
from .retrieval import AdaptiveRetriever, HybridRetriever

_DRAIN_LOCK = Lock()
_ENCODER_LOCK = Lock()
_encoder: Encoder | None = None


@celery_app.task(
    bind=True,
    autoretry_for=(ConnectionError,),
    retry_backoff=True,
    retry_jitter=True,
    max_retries=5,
)
def ingest_document(
    self, document_version_id: str, content: str, parser_version: str = "text-v1"
) -> dict[str, Any]:
    """Idempotent parser boundary. Production persists spans and emits an outbox event."""
    checksum = sha256(f"{parser_version}:{content}".encode()).hexdigest()
    paragraphs = [paragraph.strip() for paragraph in content.split("\n\n") if paragraph.strip()]
    return {
        "document_version_id": document_version_id,
        "checksum": checksum,
        "span_count": len(paragraphs),
        "status": "parsed",
    }


@celery_app.task(
    bind=True,
    autoretry_for=(ConnectionError,),
    retry_backoff=True,
    retry_jitter=True,
    max_retries=5,
)
def sync_vectors(self, chunk_ids: list[str], embedding_version: str) -> dict[str, Any]:
    """Qdrant sync contract. Point upserts use stable chunk IDs and are safe to retry."""
    return {
        "chunk_ids": chunk_ids,
        "embedding_version": embedding_version,
        "upserted": len(set(chunk_ids)),
        "status": "synced",
    }


@celery_app.task
def update_mastery(evidence_event_id: str) -> dict[str, str]:
    return {"evidence_event_id": evidence_event_id, "status": "mastery_updated"}


def get_encoder() -> Encoder:
    global _encoder
    if _encoder is None:
        with _ENCODER_LOCK:
            if _encoder is None:
                settings = get_settings()
                if settings.embedding_provider == "openai":
                    _encoder = OpenAIEncoder(
                        api_key=settings.openai_api_key or "",
                        model=settings.embedding_model,
                        sparse_model=settings.sparse_embedding_model,
                        dimensions=settings.openai_embedding_dimensions,
                        base_url=settings.openai_base_url,
                        allow_document_embedding=settings.openai_document_embedding_allowed,
                    )
                elif settings.embedding_provider == "qdrant_cloud":
                    _encoder = QdrantCloudInferenceEncoder(
                        dense_model=settings.embedding_model,
                        sparse_model=settings.sparse_embedding_model,
                        dense_size=settings.qdrant_inference_dense_size,
                        allow_document_embedding=settings.qdrant_cloud_document_inference_allowed,
                    )
                else:
                    _encoder = FastEmbedEncoder(
                        settings.embedding_model,
                        settings.sparse_embedding_model,
                        settings.embedding_cache_path,
                    )
    return _encoder


@lru_cache
def get_outbox_consumer() -> OutboxConsumer:
    settings = get_settings()
    return OutboxConsumer(
        OutboxStore(settings),
        get_encoder(),
        QdrantChunkIndex(settings),
    )


@lru_cache
def get_essay_grading_consumer() -> EssayGradingConsumer:
    settings = get_settings()
    return EssayGradingConsumer(OutboxStore(settings), settings)


@lru_cache
def get_hybrid_retriever() -> HybridRetriever:
    settings = get_settings()
    reranker = FastEmbedReranker(settings.rerank_model) if settings.rerank_enabled else None
    return HybridRetriever(get_encoder(), QdrantChunkIndex(settings), reranker)


@lru_cache
def get_adaptive_retriever() -> AdaptiveRetriever:
    return AdaptiveRetriever(get_hybrid_retriever())


@lru_cache
def get_graph_lite_retriever() -> GraphLiteRetriever:
    settings = get_settings()
    return GraphLiteRetriever(
        get_adaptive_retriever(), GraphStore(settings.database_url), QdrantChunkIndex(settings)
    )


@celery_app.task(name="chiron.drain_outbox", ignore_result=True)
def drain_outbox() -> dict[str, int]:
    if not _DRAIN_LOCK.acquire(blocking=False):
        return {"claimed": 0, "processed": 0, "failed": 0}
    try:
        vector = get_outbox_consumer().drain_once()
        essay = get_essay_grading_consumer().drain_once()
        record_outbox("vector", vector)
        record_outbox("essay_grading", essay)
        GRADING_SLA_ESCALATIONS.inc(essay.get("escalated", 0))
        update_queue_depths(get_outbox_consumer().store.queue_depths())
        return {key: vector[key] + essay[key] for key in vector}
    finally:
        _DRAIN_LOCK.release()


@celery_app.task(name="chiron.hybrid_retrieve")
def hybrid_retrieve(
    query: str,
    tenant_id: str,
    course_id: str,
    candidate_limit: int | None = None,
    limit: int | None = None,
) -> dict:
    settings = get_settings()
    started = perf_counter()
    try:
        result = get_hybrid_retriever().retrieve(
            query,
            tenant_id=tenant_id,
            course_id=course_id,
            candidate_limit=candidate_limit or settings.retrieval_candidate_limit,
            limit=limit or settings.retrieval_limit,
        )
        RETRIEVAL_DURATION.labels(mode="hybrid", route="direct", outcome="success").observe(
            perf_counter() - started
        )
        return result
    except Exception:
        RETRIEVAL_DURATION.labels(mode="hybrid", route="direct", outcome="failed").observe(
            perf_counter() - started
        )
        raise


@celery_app.task(name="chiron.adaptive_retrieve")
def adaptive_retrieve(
    query: str,
    tenant_id: str,
    course_id: str,
    route: str = "direct",
    direct_candidate_limit: int | None = None,
    direct_limit: int | None = None,
    multi_hop_candidate_limit: int | None = None,
    multi_hop_limit: int | None = None,
    max_subqueries: int | None = None,
) -> dict:
    settings = get_settings()
    retriever = get_graph_lite_retriever() if settings.graph_lite_enabled else get_adaptive_retriever()
    kwargs = {
        "query": query,
        "tenant_id": tenant_id,
        "course_id": course_id,
        "route": route,
        "direct_candidate_limit": (
            direct_candidate_limit or settings.retrieval_direct_candidate_limit
        ),
        "direct_limit": direct_limit or settings.retrieval_limit,
        "multi_hop_candidate_limit": (
            multi_hop_candidate_limit or settings.retrieval_multi_hop_candidate_limit
        ),
        "multi_hop_limit": multi_hop_limit or settings.retrieval_multi_hop_limit,
        "max_subqueries": max_subqueries or settings.retrieval_max_subqueries,
    }
    if settings.graph_lite_enabled:
        kwargs.update(
            graph_max_hops=settings.graph_max_hops,
            graph_expansion_limit=settings.graph_expansion_limit,
            graph_review_statuses=(settings.graph_review_status,),
            graph_version_status=settings.graph_version_status,
        )
    started = perf_counter()
    mode = "graph_lite" if settings.graph_lite_enabled else "adaptive"
    try:
        result = retriever.retrieve(**kwargs)
        RETRIEVAL_DURATION.labels(mode=mode, route=route, outcome="success").observe(
            perf_counter() - started
        )
        return result
    except Exception:
        RETRIEVAL_DURATION.labels(mode=mode, route=route, outcome="failed").observe(
            perf_counter() - started
        )
        raise


@celery_app.task(name="chiron.enforce_retention")
def enforce_retention() -> dict:
    settings = get_settings()
    if not settings.retention_enabled:
        return {"status": "disabled"}
    database_url = settings.operations_database_url or settings.database_url
    try:
        report = RetentionEnforcer(database_url, policy_from_settings(settings)).run(
            dry_run=settings.retention_dry_run
        )
        RETENTION_RUNS.labels(outcome=report["status"]).inc()
        if report["status"] == "completed":
            for table, count in report["affected_rows"].items():
                RETENTION_ROWS.labels(table=table).inc(count)
        return report
    except Exception:
        RETENTION_RUNS.labels(outcome="failed").inc()
        raise
