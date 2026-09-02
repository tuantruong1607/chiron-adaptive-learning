from __future__ import annotations

from dataclasses import asdict, dataclass
from urllib.parse import urlparse


@dataclass(frozen=True, slots=True)
class PreflightFinding:
    key: str
    severity: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return asdict(self)


PLACEHOLDERS = {
    "",
    "change-me",
    "change-me-now",
    "replace-me",
    "replace-with-at-least-32-random-characters",
    "chiron-local-only-jwt-secret-change-before-production",
    "chiron-dev-secret-change-me-before-production",
}


def _is_placeholder(value: str | None) -> bool:
    if value is None:
        return True
    normalized = value.strip().casefold()
    return normalized in PLACEHOLDERS or "example.com" in normalized or "runtime-password" in normalized


def _secure_url(value: str | None) -> bool:
    if not value or _is_placeholder(value):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def audit_production_environment(environment: dict[str, str]) -> list[PreflightFinding]:
    findings: list[PreflightFinding] = []

    def error(key: str, message: str) -> None:
        findings.append(PreflightFinding(key, "error", message))

    def warning(key: str, message: str) -> None:
        findings.append(PreflightFinding(key, "warning", message))

    if environment.get("APP_ENV") != "production":
        error("APP_ENV", "Production deployment must set APP_ENV=production.")
    if environment.get("PERSISTENCE_BACKEND") != "postgres":
        error("PERSISTENCE_BACKEND", "Pilot data must use PostgreSQL persistence.")

    for key in ("DATABASE_URL", "REDIS_URL", "QDRANT_URL", "QDRANT_COLLECTION"):
        if _is_placeholder(environment.get(key)):
            error(key, f"{key} must be configured with a non-placeholder production value.")

    for key in ("AUTH_JWT_SECRET", "WORKER_INTERNAL_TOKEN", "OPS_METRICS_TOKEN"):
        value = environment.get(key)
        if _is_placeholder(value) or len(value or "") < 32:
            error(key, f"{key} must be a unique secret with at least 32 characters.")

    auth_mode = environment.get("AUTH_MODE", "").casefold()
    if auth_mode not in {"oidc", "hybrid"}:
        error("AUTH_MODE", "Pilot deployment requires OIDC or hybrid authentication.")
    for key in ("OIDC_ISSUER_URL", "OIDC_AUTHORIZATION_URL", "OIDC_TOKEN_URL", "OIDC_REDIRECT_URI"):
        if not _secure_url(environment.get(key)):
            error(key, f"{key} must be a real HTTPS endpoint.")
    for key in ("OIDC_AUDIENCE", "OIDC_CLIENT_ID", "OIDC_CLIENT_SECRET"):
        if _is_placeholder(environment.get(key)):
            error(key, f"{key} must be provisioned in the live identity provider.")

    for key in ("WEB_BASE_URL", "APP_BASE_URL"):
        if not _secure_url(environment.get(key)):
            error(key, f"{key} must use the deployed HTTPS web origin.")
    if _is_placeholder(environment.get("WEB_TRUSTED_ORIGINS")):
        error("WEB_TRUSTED_ORIGINS", "Set the explicit production origin allowlist.")

    provider = environment.get("LLM_PROVIDER", "mock").casefold()
    if provider == "mock":
        error("LLM_PROVIDER", "A calibrated approved provider is required for pilot grading.")
    elif provider == "groq" and _is_placeholder(environment.get("GROQ_API_KEY")):
        error("GROQ_API_KEY", "The selected Groq provider requires its production API key.")
    elif provider == "gemini" and _is_placeholder(environment.get("GEMINI_API_KEY")):
        error("GEMINI_API_KEY", "The selected Gemini provider requires its production API key.")

    free_profile = environment.get("DEPLOYMENT_PROFILE", "").casefold() == "aws-free"
    invariants = {
        "EMBEDDING_PROVIDER": "qdrant_cloud" if free_profile else "local",
        "QDRANT_CLOUD_DOCUMENT_INFERENCE_ALLOWED": "true" if free_profile else "",
        "OPENAI_DOCUMENT_EMBEDDING_ALLOWED": "false",
        "RETENTION_ENABLED": "true",
        "RETENTION_DRY_RUN": "false",
        # The free profile uses a new Cloud Inference model/collection. Keep
        # Graph-lite gated until that collection has passed its own evaluation.
        "GRAPH_LITE_ENABLED": "false" if free_profile else "true",
    }
    for key, expected in invariants.items():
        if expected and environment.get(key, "").casefold() != expected:
            error(key, f"{key} must be {expected} for the approved pilot configuration.")

    try:
        sla = int(environment.get("ESSAY_GRADING_SLA_MINUTES", "0"))
    except ValueError:
        sla = 0
    if not 1 <= sla <= 1440:
        error("ESSAY_GRADING_SLA_MINUTES", "Set an essay grading SLA between 1 and 1440 minutes.")

    if environment.get("RERANK_ENABLED", "false").casefold() == "true":
        warning("RERANK_ENABLED", "Keep reranking disabled unless a fresh quality and latency gate passes.")
    if environment.get("LLM_FALLBACK_ALLOWED_SENSITIVITIES", "public,synthetic").casefold() != "public,synthetic":
        warning(
            "LLM_FALLBACK_ALLOWED_SENSITIVITIES",
            "Review any expansion beyond public,synthetic before private learner data can fall back.",
        )
    return findings
