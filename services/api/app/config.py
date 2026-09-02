from functools import lru_cache
from typing import Literal

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../../.env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: Literal["development", "test", "production"] = "development"
    app_name: str = "Chiron API"
    app_base_url: str = "http://localhost:3000"
    database_url: str | None = None
    database_admin_url: str | None = Field(default=None, repr=False)
    database_runtime_user: str = "chiron_runtime"
    database_runtime_password: str | None = Field(default=None, repr=False)
    worker_internal_token: str | None = Field(default=None, repr=False)
    ops_metrics_token: str | None = Field(default=None, repr=False)
    qdrant_url: str | None = None
    qdrant_api_key: str | None = Field(default=None, repr=False)
    redis_url: str | None = None
    persistence_backend: Literal["auto", "memory", "postgres"] = "auto"
    auth_mode: Literal["local", "oidc", "hybrid"] = "local"
    auth_jwt_secret: str = Field(
        default="chiron-dev-secret-change-me-before-production", min_length=32, repr=False
    )
    auth_jwt_algorithm: Literal["HS256"] = "HS256"
    auth_access_token_minutes: int = Field(default=60, ge=5, le=1440)
    auth_refresh_token_days: int = Field(default=14, ge=1, le=90)
    oidc_issuer_url: str | None = None
    oidc_audience: str | None = None
    oidc_jwks_url: str | None = None
    oidc_algorithms: str = "RS256"
    oidc_user_id_claim: str = "chiron_user_id"
    oidc_tenant_id_claim: str = "chiron_tenant_id"
    oidc_role_claim: str = "chiron_role"
    readiness_timeout_seconds: float = Field(default=2.0, ge=0.2, le=10)
    retrieval_task_timeout_seconds: float = Field(default=3.0, ge=0.5, le=120)
    retrieval_candidate_limit: int = Field(default=24, ge=5, le=100)
    retrieval_limit: int = Field(default=5, ge=1, le=20)
    retrieval_direct_candidate_limit: int = Field(default=16, ge=5, le=100)
    retrieval_multi_hop_candidate_limit: int = Field(default=12, ge=5, le=100)
    retrieval_multi_hop_limit: int = Field(default=8, ge=2, le=20)
    retrieval_max_subqueries: int = Field(default=1, ge=1, le=3)
    graph_lite_enabled: bool = False
    llm_provider: Literal["mock", "groq", "gemini", "openai", "openrouter", "deepseek", "generic"] = "mock"
    llm_api_key: str | None = Field(default=None, repr=False)
    llm_base_url: str | None = None
    openai_api_key: str | None = Field(default=None, repr=False)
    openai_base_url: str = "https://api.openai.com/v1"
    openai_tutor_model: str = "gpt-4o-mini"
    openrouter_api_key: str | None = Field(default=None, repr=False)
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_tutor_model: str = "meta-llama/llama-3.3-70b-instruct"
    deepseek_api_key: str | None = Field(default=None, repr=False)
    deepseek_base_url: str = "https://api.deepseek.com/v1"
    deepseek_tutor_model: str = "deepseek-chat"
    groq_api_key: str | None = Field(default=None, repr=False)
    groq_base_url: str = "https://api.groq.com/openai/v1"
    gemini_api_key: str | None = Field(default=None, repr=False)
    gemini_base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai"
    llm_tutor_model: str = "llama-3.3-70b-versatile"
    llm_extraction_model: str = "llama-3.1-8b-instant"
    llm_grader_model: str = "llama-3.3-70b-versatile"
    llm_research_model: str = "llama-3.3-70b-versatile"
    llm_groq_fallback_model: str = "llama-3.1-8b-instant"
    gemini_tutor_model: str = "gemini-3.5-flash-lite"
    gemini_extraction_model: str = "gemini-3.5-flash-lite"
    gemini_grader_model: str = "gemini-3.5-flash-lite"
    gemini_research_model: str = "gemini-3.5-flash-lite"
    llm_fallback_enabled: bool = True
    llm_fallback_on_quota: bool = True
    llm_fallback_on_unavailable: bool = True
    llm_fallback_allowed_sensitivities: str = "public,synthetic"
    llm_request_timeout_seconds: float = 60
    llm_state_backend: Literal["auto", "memory", "redis"] = "auto"
    llm_circuit_failure_threshold: int = 3
    llm_circuit_failure_window_seconds: int = 30
    llm_circuit_open_seconds: int = 60
    llm_model_not_found_ttl_seconds: int = 3600
    llm_quota_reserve_ratio: float = 0.1
    llm_probe_on_startup: bool = False
    llm_probe_active: bool = False
    essay_grading_sla_minutes: int = Field(default=15, ge=1, le=1440)

    @property
    def fallback_allowed_sensitivities(self) -> set[str]:
        return {
            item.strip().casefold()
            for item in self.llm_fallback_allowed_sensitivities.split(",")
            if item.strip()
        }

    @property
    def use_postgres(self) -> bool:
        if self.persistence_backend == "postgres":
            return True
        if self.persistence_backend == "memory":
            return False
        return bool(self.database_url) and self.app_env != "test"

    @model_validator(mode="after")
    def validate_production(self) -> "Settings":
        if self.app_env == "production":
            required = {
                "DATABASE_URL": self.database_url,
                "QDRANT_URL": self.qdrant_url,
                "REDIS_URL": self.redis_url,
                "WORKER_INTERNAL_TOKEN": self.worker_internal_token,
                "OPS_METRICS_TOKEN": self.ops_metrics_token,
            }
            missing = [key for key, value in required.items() if not value]
            if missing:
                raise ValueError(f"Missing production settings: {', '.join(missing)}")
            if self.auth_mode in {"local", "hybrid"} and self.auth_jwt_secret in {
                "chiron-dev-secret-change-me-before-production",
                "chiron-local-only-jwt-secret-change-before-production",
                "replace-with-at-least-32-random-characters",
            }:
                raise ValueError("AUTH_JWT_SECRET must be changed in production")
            if self.auth_mode in {"oidc", "hybrid"}:
                oidc_required = {
                    "OIDC_ISSUER_URL": self.oidc_issuer_url,
                    "OIDC_AUDIENCE": self.oidc_audience,
                }
                oidc_missing = [key for key, value in oidc_required.items() if not value]
                if oidc_missing:
                    raise ValueError(
                        f"Missing production OIDC settings: {', '.join(oidc_missing)}"
                    )
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
