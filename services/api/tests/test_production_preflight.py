from app.operations import audit_production_environment


def valid_environment() -> dict[str, str]:
    return {
        "APP_ENV": "production",
        "PERSISTENCE_BACKEND": "postgres",
        "DATABASE_URL": "postgresql://runtime:secret@postgres.internal/chiron",
        "REDIS_URL": "redis://redis.internal:6379/0",
        "QDRANT_URL": "http://qdrant.internal:6333",
        "QDRANT_COLLECTION": "chiron_chunks_v1",
        "AUTH_JWT_SECRET": "a" * 48,
        "WORKER_INTERNAL_TOKEN": "b" * 48,
        "OPS_METRICS_TOKEN": "c" * 48,
        "AUTH_MODE": "oidc",
        "OIDC_ISSUER_URL": "https://identity.company.test",
        "OIDC_AUTHORIZATION_URL": "https://identity.company.test/authorize",
        "OIDC_TOKEN_URL": "https://identity.company.test/token",
        "OIDC_REDIRECT_URI": "https://learn.company.test/api/auth/oidc/callback",
        "OIDC_AUDIENCE": "chiron-api",
        "OIDC_CLIENT_ID": "chiron-web-client",
        "OIDC_CLIENT_SECRET": "d" * 48,
        "WEB_BASE_URL": "https://learn.company.test",
        "APP_BASE_URL": "https://learn.company.test",
        "WEB_TRUSTED_ORIGINS": "https://learn.company.test",
        "LLM_PROVIDER": "groq",
        "GROQ_API_KEY": "gsk_live_configured",
        "EMBEDDING_PROVIDER": "local",
        "OPENAI_DOCUMENT_EMBEDDING_ALLOWED": "false",
        "RETENTION_ENABLED": "true",
        "RETENTION_DRY_RUN": "false",
        "GRAPH_LITE_ENABLED": "true",
        "ESSAY_GRADING_SLA_MINUTES": "15",
        "RERANK_ENABLED": "false",
        "LLM_FALLBACK_ALLOWED_SENSITIVITIES": "public,synthetic",
    }


def test_valid_pilot_environment_has_no_findings() -> None:
    assert audit_production_environment(valid_environment()) == []


def test_preflight_blocks_placeholders_and_private_fallback_expansion() -> None:
    environment = valid_environment()
    environment["OIDC_CLIENT_SECRET"] = "replace-me"
    environment["LLM_FALLBACK_ALLOWED_SENSITIVITIES"] = "public,synthetic,private"

    findings = audit_production_environment(environment)

    assert any(item.key == "OIDC_CLIENT_SECRET" and item.severity == "error" for item in findings)
    assert any(item.key == "LLM_FALLBACK_ALLOWED_SENSITIVITIES" and item.severity == "warning" for item in findings)


def test_aws_free_profile_requires_cloud_inference_and_keeps_graph_gated() -> None:
    environment = valid_environment()
    environment.update(
        {
            "DEPLOYMENT_PROFILE": "aws-free",
            "EMBEDDING_PROVIDER": "qdrant_cloud",
            "QDRANT_CLOUD_DOCUMENT_INFERENCE_ALLOWED": "true",
            "OPENAI_DOCUMENT_EMBEDDING_ALLOWED": "false",
            "GRAPH_LITE_ENABLED": "false",
        }
    )

    assert audit_production_environment(environment) == []
