from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class WorkerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../../.env"), env_file_encoding="utf-8", extra="ignore"
    )

    database_url: str
    operations_database_url: str | None = Field(default=None, repr=False)
    api_base_url: str = "http://localhost:8000"
    worker_internal_token: str = ""
    redis_url: str = "redis://localhost:6379/0"
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str | None = Field(default=None, repr=False)
    qdrant_collection: str = "chiron_chunks_v1"
    embedding_provider: Literal["local", "openai", "qdrant_cloud"] = "local"
    embedding_model: str = "intfloat/multilingual-e5-large"
    embedding_version: str = "multilingual-e5-large-mean-batch32-v2"
    embedding_cache_path: str | None = None
    openai_api_key: str | None = Field(default=None, repr=False)
    openai_base_url: str = "https://api.openai.com/v1"
    openai_embedding_dimensions: int | None = Field(default=None, ge=1, le=4096)
    openai_document_embedding_allowed: bool = False
    sparse_embedding_model: str = "Qdrant/bm25"
    qdrant_inference_dense_size: int = Field(default=384, ge=1, le=4096)
    qdrant_cloud_document_inference_allowed: bool = False
    rerank_model: str = "BAAI/bge-reranker-v2-m3"
    rerank_enabled: bool = False
    retrieval_candidate_limit: int = Field(default=24, ge=5, le=100)
    retrieval_limit: int = Field(default=5, ge=1, le=20)
    retrieval_direct_candidate_limit: int = Field(default=16, ge=5, le=100)
    retrieval_multi_hop_candidate_limit: int = Field(default=12, ge=5, le=100)
    retrieval_multi_hop_limit: int = Field(default=8, ge=2, le=20)
    retrieval_max_subqueries: int = Field(default=1, ge=1, le=3)
    graph_lite_enabled: bool = False
    graph_version_status: str = "active"
    graph_review_status: str = "active"
    graph_max_hops: int = Field(default=2, ge=1, le=2)
    graph_expansion_limit: int = Field(default=8, ge=1, le=20)
    outbox_batch_size: int = Field(default=20, ge=1, le=200)
    outbox_max_attempts: int = Field(default=8, ge=1, le=50)
    outbox_lease_seconds: int = Field(default=120, ge=10, le=3600)
    outbox_poll_seconds: int = Field(default=5, ge=1, le=300)
    worker_id: str = "chiron-worker"
    worker_metrics_port: int = Field(default=9108, ge=0, le=65535)
    retention_enabled: bool = False
    retention_dry_run: bool = True
    retention_learner_content_days: int = Field(default=90, ge=1, le=3650)
    retention_processed_outbox_days: int = Field(default=30, ge=1, le=3650)
    retention_auth_session_grace_days: int = Field(default=30, ge=1, le=365)
    retention_batch_size: int = Field(default=500, ge=1, le=10000)


@lru_cache
def get_settings() -> WorkerSettings:
    return WorkerSettings()
