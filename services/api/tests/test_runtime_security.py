from __future__ import annotations

import os
from uuid import UUID, uuid4

import pytest
from sqlalchemy import create_engine, func, select, text
from sqlalchemy.orm import sessionmaker

from app import services
from app.auth import Principal, decode_access_token
from app.db import normalize_database_url, set_tenant_context
from app.persistence.tables import courses

DEMO_PRINCIPAL = Principal(
    user_id=UUID("a0635031-8db9-5229-bd8f-173e680cea8b"),
    tenant_id=UUID("c2e1e494-3fa4-596f-8714-6877bac903dd"),
    role="learner",
)


def runtime_factory():
    url = os.getenv("CHIRON_INTEGRATION_DATABASE_URL")
    if not url:
        pytest.skip("Set CHIRON_INTEGRATION_DATABASE_URL to run runtime-role tests")
    engine = create_engine(normalize_database_url(url), pool_pre_ping=True)
    return sessionmaker(bind=engine, expire_on_commit=False)


def test_runtime_role_cannot_bypass_rls() -> None:
    factory = runtime_factory()
    with factory() as session:
        flags = (
            session.execute(
                text(
                    "SELECT current_user AS role, rolsuper, rolbypassrls "
                    "FROM pg_roles WHERE rolname=current_user"
                )
            )
            .mappings()
            .one()
        )
        assert flags["role"] == "chiron_runtime"
        assert flags["rolsuper"] is False
        assert flags["rolbypassrls"] is False
        assert session.scalar(select(func.count()).select_from(courses)) == 0

    with factory() as session, session.begin():
        set_tenant_context(session, DEMO_PRINCIPAL.tenant_id)
        assert session.scalar(select(func.count()).select_from(courses)) == 1

    with factory() as session, session.begin():
        set_tenant_context(session, uuid4())
        assert session.scalar(select(func.count()).select_from(courses)) == 0


def test_refresh_token_is_rotated_and_revocable(monkeypatch) -> None:
    factory = runtime_factory()
    monkeypatch.setattr(services, "get_session_factory", lambda: factory)

    issued = services.issue_token_pair(DEMO_PRINCIPAL, "pytest")
    assert decode_access_token(issued.access_token) == DEMO_PRINCIPAL

    rotated = services.rotate_refresh_token(issued.refresh_token, "pytest-rotated")
    assert rotated.refresh_token != issued.refresh_token
    with pytest.raises(services.InvalidRefreshTokenError):
        services.rotate_refresh_token(issued.refresh_token)

    services.revoke_refresh_token(rotated.refresh_token)
    with pytest.raises(services.InvalidRefreshTokenError):
        services.rotate_refresh_token(rotated.refresh_token)
