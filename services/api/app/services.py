from __future__ import annotations

from datetime import UTC, datetime, timedelta
from functools import lru_cache
from typing import Annotated, Protocol
from uuid import uuid4

from fastapi import Depends
from sqlalchemy.orm import Session

from .adaptive.service import MemoryAdaptiveService
from .auth import (
    Principal,
    create_access_token,
    create_refresh_token,
    hash_password,
    parse_refresh_token,
    refresh_token_hash,
    verify_password,
)
from .config import get_settings
from .db import get_session_factory, set_tenant_context
from .persistence.repositories import (
    CourseRepository,
    IdentityRepository,
    RefreshSessionRepository,
    UserAlreadyExistsError,
)
from .persistence.service import EnrollmentRequiredError, PostgresAdaptiveService
from .schemas import (
    AccessTokenResponse,
    DiagnosticResult,
    DiagnosticSubmission,
    KnowledgeMap,
    LabResult,
    LabSubmission,
    LearningStateOut,
    LoginRequest,
    RegisterRequest,
    SourceLocator,
    StudyPlan,
)


class InvalidRefreshTokenError(PermissionError):
    pass


class AdaptiveService(Protocol):
    def knowledge_map(self, course_slug: str, principal: Principal) -> KnowledgeMap: ...

    def source_locator(
        self, course_slug: str, source_span_id: str, principal: Principal
    ) -> SourceLocator: ...

    def submit_diagnostic(
        self,
        course_slug: str,
        payload: DiagnosticSubmission,
        idempotency_key: str,
        principal: Principal,
    ) -> DiagnosticResult: ...

    def diagnostic_completed(self, course_slug: str, principal: Principal) -> bool: ...

    def learning_states(self, course_slug: str, principal: Principal) -> list[LearningStateOut]: ...

    def plan(
        self,
        course_slug: str,
        principal: Principal,
        *,
        horizon_days: int,
        daily_minutes: int,
    ) -> StudyPlan: ...

    def submit_lab(
        self,
        course_slug: str,
        lab_id: str,
        concept_id: str,
        payload: LabSubmission,
        score: LabResult,
        idempotency_key: str,
        principal: Principal,
    ) -> LabResult: ...


@lru_cache
def get_memory_adaptive_service() -> MemoryAdaptiveService:
    return MemoryAdaptiveService()


@lru_cache
def get_postgres_adaptive_service() -> PostgresAdaptiveService:
    return PostgresAdaptiveService()


def get_adaptive_service() -> AdaptiveService:
    return (
        get_postgres_adaptive_service()
        if get_settings().use_postgres
        else get_memory_adaptive_service()
    )


AdaptiveServiceDep = Annotated[AdaptiveService, Depends(get_adaptive_service)]


def resolve_enrolled_course_id(course_slug: str, principal: Principal):
    repository = CourseRepository()
    with get_session_factory()() as session, session.begin():
        set_tenant_context(session, principal.tenant_id)
        course = repository.require_enrollment(
            session,
            tenant_id=principal.tenant_id,
            learner_id=principal.user_id,
            course_slug=course_slug,
        )
        if course is None:
            raise EnrollmentRequiredError("Active course enrollment required")
        return course.id


def authenticate(payload: LoginRequest) -> Principal | None:
    settings = get_settings()
    if not settings.database_url:
        return None
    identity = IdentityRepository()
    session_factory = get_session_factory()
    with session_factory() as session, session.begin():
        session: Session
        tenant_id = identity.find_tenant(session, payload.tenant_slug)
        if tenant_id is None:
            return None
        set_tenant_context(session, tenant_id)
        record = identity.find_login(session, tenant_id, payload.email)
        if record is None or not verify_password(payload.password, record.password_hash):
            return None
        return Principal(
            user_id=record.user_id,
            tenant_id=record.tenant_id,
            role=record.role,
        )


def register_learner_service(payload: RegisterRequest) -> Principal:
    settings = get_settings()
    if not settings.database_url:
        raise RuntimeError("DATABASE_URL is required for registration")
    identity = IdentityRepository()
    session_factory = get_session_factory()
    hashed = hash_password(payload.password)
    with session_factory() as session:
        record = identity.register_learner(
            session,
            tenant_slug=payload.tenant_slug,
            email=payload.email,
            password_hash=hashed,
            display_name=payload.display_name,
        )
        return Principal(
            user_id=record.user_id,
            tenant_id=record.tenant_id,
            role=record.role,
        )


def issue_token_pair(principal: Principal, user_agent: str | None = None) -> AccessTokenResponse:
    settings = get_settings()
    session_id = uuid4()
    refresh_token = create_refresh_token(principal.tenant_id, session_id)
    refresh_expires = datetime.now(UTC) + timedelta(days=settings.auth_refresh_token_days)
    repository = RefreshSessionRepository()
    with get_session_factory()() as session, session.begin():
        set_tenant_context(session, principal.tenant_id)
        repository.create(
            session,
            session_id=session_id,
            tenant_id=principal.tenant_id,
            user_id=principal.user_id,
            token_hash=refresh_token_hash(refresh_token),
            expires_at=refresh_expires,
            user_agent=user_agent,
        )
    return AccessTokenResponse(
        access_token=create_access_token(principal),
        refresh_token=refresh_token,
        expires_in=settings.auth_access_token_minutes * 60,
        refresh_expires_in=settings.auth_refresh_token_days * 86400,
    )


def rotate_refresh_token(token: str, user_agent: str | None = None) -> AccessTokenResponse:
    try:
        tenant_id, old_session_id = parse_refresh_token(token)
    except ValueError as exc:
        raise InvalidRefreshTokenError("Invalid or expired refresh token") from exc

    settings = get_settings()
    identity = IdentityRepository()
    repository = RefreshSessionRepository()
    with get_session_factory()() as session, session.begin():
        set_tenant_context(session, tenant_id)
        current = repository.acquire_active(
            session,
            tenant_id=tenant_id,
            session_id=old_session_id,
            token_hash=refresh_token_hash(token),
        )
        if current is None:
            raise InvalidRefreshTokenError("Invalid or expired refresh token")
        membership = identity.active_membership(session, tenant_id, current["user_id"])
        if membership is None:
            repository.revoke(session, session_id=old_session_id)
            raise InvalidRefreshTokenError("Membership is no longer active")

        principal = Principal(
            user_id=membership.user_id,
            tenant_id=membership.tenant_id,
            role=membership.role,
        )
        new_session_id = uuid4()
        new_refresh_token = create_refresh_token(tenant_id, new_session_id)
        repository.create(
            session,
            session_id=new_session_id,
            tenant_id=tenant_id,
            user_id=principal.user_id,
            token_hash=refresh_token_hash(new_refresh_token),
            expires_at=datetime.now(UTC) + timedelta(days=settings.auth_refresh_token_days),
            user_agent=user_agent,
        )
        repository.revoke(
            session,
            session_id=old_session_id,
            replacement_id=new_session_id,
        )

    return AccessTokenResponse(
        access_token=create_access_token(principal),
        refresh_token=new_refresh_token,
        expires_in=settings.auth_access_token_minutes * 60,
        refresh_expires_in=settings.auth_refresh_token_days * 86400,
    )


def revoke_refresh_token(token: str) -> None:
    try:
        tenant_id, session_id = parse_refresh_token(token)
    except ValueError:
        return
    repository = RefreshSessionRepository()
    with get_session_factory()() as session, session.begin():
        set_tenant_context(session, tenant_id)
        current = repository.acquire_active(
            session,
            tenant_id=tenant_id,
            session_id=session_id,
            token_hash=refresh_token_hash(token),
        )
        if current is not None:
            repository.revoke(session, session_id=session_id)
