from __future__ import annotations

from contextlib import suppress
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from functools import lru_cache
from hashlib import sha256
from secrets import token_urlsafe
from typing import Annotated
from uuid import UUID

import httpx
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pwdlib import PasswordHash

from .config import Settings, get_settings

password_hash = PasswordHash.recommended()
bearer_scheme = HTTPBearer(auto_error=False)


@dataclass(frozen=True, slots=True)
class Principal:
    user_id: UUID
    tenant_id: UUID
    role: str


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, encoded: str) -> bool:
    return password_hash.verify(password, encoded)


def create_access_token(principal: Principal, settings: Settings | None = None) -> str:
    active_settings = settings or get_settings()
    now = datetime.now(UTC)
    expires = now + timedelta(minutes=active_settings.auth_access_token_minutes)
    return jwt.encode(
        {
            "sub": str(principal.user_id),
            "tid": str(principal.tenant_id),
            "role": principal.role,
            "iat": now,
            "exp": expires,
            "iss": "chiron-api",
            "aud": "chiron-web",
            "typ": "access",
        },
        active_settings.auth_jwt_secret,
        algorithm=active_settings.auth_jwt_algorithm,
    )


def decode_access_token(token: str, settings: Settings | None = None) -> Principal:
    active_settings = settings or get_settings()
    unverified_issuer = None
    with suppress(jwt.PyJWTError):
        unverified_issuer = jwt.decode(token, options={"verify_signature": False}).get("iss")
    if active_settings.auth_mode in {"local", "hybrid"} and unverified_issuer == "chiron-api":
        return _decode_local_access_token(token, active_settings)
    if active_settings.auth_mode in {"oidc", "hybrid"}:
        return _decode_oidc_access_token(token, active_settings)
    return _decode_local_access_token(token, active_settings)


def _decode_local_access_token(token: str, settings: Settings) -> Principal:
    try:
        payload = jwt.decode(
            token,
            settings.auth_jwt_secret,
            algorithms=[settings.auth_jwt_algorithm],
            audience="chiron-web",
            issuer="chiron-api",
        )
        role = str(payload["role"])
        if payload.get("typ") != "access":
            raise ValueError("unsupported token type")
        if role not in {"learner", "instructor", "admin"}:
            raise ValueError("unsupported role")
        return Principal(
            user_id=UUID(str(payload["sub"])),
            tenant_id=UUID(str(payload["tid"])),
            role=role,
        )
    except (jwt.PyJWTError, KeyError, TypeError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired access token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


@lru_cache(maxsize=8)
def _discovered_jwks_url(issuer_url: str) -> str:
    discovery_url = f"{issuer_url.rstrip('/')}/.well-known/openid-configuration"
    response = httpx.get(discovery_url, timeout=5)
    response.raise_for_status()
    jwks_uri = response.json().get("jwks_uri")
    if not isinstance(jwks_uri, str) or not jwks_uri.startswith("https://"):
        raise ValueError("OIDC discovery did not return a secure jwks_uri")
    return jwks_uri


@lru_cache(maxsize=8)
def _jwk_client(jwks_url: str) -> jwt.PyJWKClient:
    return jwt.PyJWKClient(jwks_url, cache_jwk_set=True, lifespan=300)


def _decode_oidc_access_token(token: str, settings: Settings) -> Principal:
    try:
        if not settings.oidc_issuer_url or not settings.oidc_audience:
            raise ValueError("OIDC issuer and audience are required")
        jwks_url = settings.oidc_jwks_url or _discovered_jwks_url(settings.oidc_issuer_url)
        key = _jwk_client(jwks_url).get_signing_key_from_jwt(token).key
        algorithms = [item.strip() for item in settings.oidc_algorithms.split(",") if item.strip()]
        if not algorithms:
            raise ValueError("OIDC algorithms are empty")
        payload = jwt.decode(
            token,
            key,
            algorithms=algorithms,
            audience=settings.oidc_audience,
            issuer=settings.oidc_issuer_url,
            options={"require": ["exp", "iat", "iss", "aud", "sub"]},
        )
        role = str(payload[settings.oidc_role_claim])
        if role not in {"learner", "instructor", "admin"}:
            raise ValueError("unsupported OIDC role")
        return Principal(
            user_id=UUID(str(payload[settings.oidc_user_id_claim])),
            tenant_id=UUID(str(payload[settings.oidc_tenant_id_claim])),
            role=role,
        )
    except (httpx.HTTPError, jwt.PyJWTError, KeyError, TypeError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired OIDC access token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def get_current_principal(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
) -> Principal:
    if credentials is None or credentials.scheme.casefold() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer access token required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return decode_access_token(credentials.credentials)


CurrentPrincipal = Annotated[Principal, Depends(get_current_principal)]


def create_refresh_token(tenant_id: UUID, session_id: UUID) -> str:
    return f"{tenant_id}.{session_id}.{token_urlsafe(48)}"


def parse_refresh_token(token: str) -> tuple[UUID, UUID]:
    try:
        tenant_raw, session_raw, secret = token.split(".", 2)
        if len(secret) < 32:
            raise ValueError("refresh secret too short")
        return UUID(tenant_raw), UUID(session_raw)
    except (TypeError, ValueError) as exc:
        raise ValueError("invalid refresh token") from exc


def refresh_token_hash(token: str) -> str:
    return sha256(token.encode()).hexdigest()
