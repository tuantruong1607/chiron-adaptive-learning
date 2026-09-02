from __future__ import annotations

from collections.abc import Iterator
from functools import lru_cache
from uuid import UUID

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from .config import get_settings


def normalize_database_url(url: str) -> str:
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+psycopg://", 1)
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql+psycopg://", 1)
    return url


@lru_cache
def get_engine() -> Engine:
    settings = get_settings()
    if not settings.database_url:
        raise RuntimeError("DATABASE_URL is required for PostgreSQL persistence")
    normalized_url = normalize_database_url(settings.database_url)
    connect_args: dict = {}
    if "postgresql+psycopg" in normalized_url:
        connect_args["prepare_threshold"] = None
    return create_engine(
        normalized_url,
        connect_args=connect_args,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
    )


@lru_cache
def get_session_factory() -> sessionmaker[Session]:
    return sessionmaker(bind=get_engine(), expire_on_commit=False, autoflush=False)


def get_db_session() -> Iterator[Session]:
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()


def set_tenant_context(session: Session, tenant_id: UUID) -> None:
    """Set the transaction-local tenant used by PostgreSQL RLS policies."""
    session.execute(
        text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
        {"tenant_id": str(tenant_id)},
    )
