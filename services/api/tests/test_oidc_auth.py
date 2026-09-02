from datetime import UTC, datetime, timedelta
from uuid import uuid4

import jwt
import pytest
from pydantic import ValidationError

from app import auth
from app.auth import Principal, decode_access_token
from app.config import Settings


class _SigningKey:
    key = "synthetic-oidc-signing-secret-at-least-32-bytes"


class _JwkClient:
    def get_signing_key_from_jwt(self, _: str) -> _SigningKey:
        return _SigningKey()


def test_oidc_token_validates_issuer_audience_and_identity_claims(monkeypatch) -> None:
    principal = Principal(user_id=uuid4(), tenant_id=uuid4(), role="learner")
    settings = Settings(
        _env_file=None,
        auth_mode="oidc",
        oidc_issuer_url="https://identity.example.test",
        oidc_audience="chiron-api",
        oidc_jwks_url="https://identity.example.test/jwks",
        oidc_algorithms="HS256",
    )
    now = datetime.now(UTC)
    token = jwt.encode(
        {
            "sub": "external-subject",
            "iss": settings.oidc_issuer_url,
            "aud": settings.oidc_audience,
            "iat": now,
            "exp": now + timedelta(minutes=5),
            settings.oidc_user_id_claim: str(principal.user_id),
            settings.oidc_tenant_id_claim: str(principal.tenant_id),
            settings.oidc_role_claim: principal.role,
        },
        _SigningKey.key,
        algorithm="HS256",
    )
    monkeypatch.setattr(auth, "_jwk_client", lambda _: _JwkClient())
    assert decode_access_token(token, settings) == principal


def test_production_oidc_requires_issuer_and_audience() -> None:
    with pytest.raises(ValidationError, match="Missing production OIDC settings"):
        Settings(
            _env_file=None,
            app_env="production",
            auth_mode="oidc",
            database_url="postgresql://runtime@db/chiron",
            qdrant_url="https://qdrant.example.test",
            redis_url="rediss://redis.example.test",
            worker_internal_token="synthetic-worker-token",
            ops_metrics_token="synthetic-metrics-token",
        )
