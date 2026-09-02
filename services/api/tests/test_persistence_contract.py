from __future__ import annotations

import os
from concurrent.futures import ThreadPoolExecutor
from uuid import UUID, uuid4

import pytest
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker

from app.adaptive.essay_judge import deterministic_grade
from app.adaptive.rubrics import get_rubric
from app.adaptive.service import MemoryAdaptiveService
from app.auth import Principal
from app.db import normalize_database_url, set_tenant_context
from app.essay import PostgresEssayStore
from app.labs import score_lab
from app.persistence.service import EnrollmentRequiredError, PostgresAdaptiveService
from app.persistence.tables import (
    attempts,
    courses,
    evidence_ledger,
    learning_events,
    mastery_states,
)
from app.schemas import (
    DiagnosticSubmission,
    EssayHumanReviewRequest,
    EssaySubmissionRequest,
    LabSubmission,
)
from app.seed import LABS
from tests.adaptive_contract import assert_adaptive_contract

DEMO_PRINCIPAL = Principal(
    user_id=UUID("a0635031-8db9-5229-bd8f-173e680cea8b"),
    tenant_id=UUID("c2e1e494-3fa4-596f-8714-6877bac903dd"),
    role="learner",
)


def _postgres_factory():
    database_url = os.getenv("CHIRON_INTEGRATION_DATABASE_URL")
    if not database_url:
        pytest.skip("Set CHIRON_INTEGRATION_DATABASE_URL to run PostgreSQL contracts")
    engine = create_engine(normalize_database_url(database_url), pool_pre_ping=True)
    return sessionmaker(bind=engine, expire_on_commit=False)


@pytest.mark.parametrize("adapter", ["memory", "postgres"])
def test_adaptive_service_contract(adapter: str) -> None:
    if adapter == "memory":
        service = MemoryAdaptiveService()
        principal = Principal(user_id=uuid4(), tenant_id=uuid4(), role="learner")
    else:
        service = PostgresAdaptiveService(_postgres_factory())
        principal = DEMO_PRINCIPAL
    assert_adaptive_contract(service, principal, f"contract-{adapter}-{uuid4()}")


def test_postgres_transaction_rolls_back_every_state_change() -> None:
    factory = _postgres_factory()
    key = f"rollback-{uuid4()}"
    before: dict[str, int] = {}
    with factory() as session, session.begin():
        set_tenant_context(session, DEMO_PRINCIPAL.tenant_id)
        before["attempts"] = session.scalar(select(func.count()).select_from(attempts)) or 0
        before["evidence"] = session.scalar(select(func.count()).select_from(evidence_ledger)) or 0
        before["mastery"] = session.scalar(select(func.count()).select_from(mastery_states)) or 0

    def fail_after_evidence(stage: str) -> None:
        if stage == "after_evidence":
            raise RuntimeError("injected transaction failure")

    service = PostgresAdaptiveService(factory, fault_hook=fail_after_evidence)
    payload = DiagnosticSubmission.model_validate(
        {"answers": [{"question_id": "diag-foundation-01", "option_id": "b"}]}
    )
    with pytest.raises(RuntimeError, match="injected transaction failure"):
        service.submit_diagnostic("rag-intensive", payload, key, DEMO_PRINCIPAL)

    with factory() as session, session.begin():
        set_tenant_context(session, DEMO_PRINCIPAL.tenant_id)
        assert session.scalar(select(func.count()).select_from(attempts)) == before["attempts"]
        assert (
            session.scalar(select(func.count()).select_from(evidence_ledger)) == before["evidence"]
        )
        assert session.scalar(select(func.count()).select_from(mastery_states)) == before["mastery"]


def test_postgres_concurrent_idempotency_and_restart_replay() -> None:
    factory = _postgres_factory()
    key = f"concurrent-{uuid4()}"
    payload = DiagnosticSubmission.model_validate(
        {"answers": [{"question_id": "diag-foundation-01", "option_id": "b"}]}
    )

    def submit_once():
        return PostgresAdaptiveService(factory).submit_diagnostic(
            "rag-intensive", payload, key, DEMO_PRINCIPAL
        )

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(lambda _: submit_once(), range(2)))

    assert results[0].attempt_id == results[1].attempt_id
    assert results[0].model_dump(mode="json") == results[1].model_dump(mode="json")

    # A fresh service instance proves replay state lives in PostgreSQL, not process memory.
    replay = PostgresAdaptiveService(factory).submit_diagnostic(
        "rag-intensive", payload, key, DEMO_PRINCIPAL
    )
    assert replay.attempt_id == results[0].attempt_id

    with factory() as session, session.begin():
        set_tenant_context(session, DEMO_PRINCIPAL.tenant_id)
        evidence_count = session.scalar(
            select(func.count())
            .select_from(evidence_ledger)
            .where(evidence_ledger.c.attempt_id == replay.attempt_id)
        )
        assert evidence_count == 1


def test_postgres_tenant_filter_rejects_cross_tenant_access() -> None:
    service = PostgresAdaptiveService(_postgres_factory())
    enrolled_map = service.knowledge_map("rag-intensive", DEMO_PRINCIPAL)
    source_span_id = enrolled_map.nodes[0].citations[0].source_span_id
    locator = service.source_locator("rag-intensive", source_span_id, DEMO_PRINCIPAL)
    assert locator.source_span_id == source_span_id
    assert locator.locator
    foreign_principal = Principal(
        user_id=DEMO_PRINCIPAL.user_id,
        tenant_id=uuid4(),
        role="learner",
    )
    with pytest.raises(EnrollmentRequiredError):
        service.learning_states("rag-intensive", foreign_principal)
    with pytest.raises(EnrollmentRequiredError):
        service.knowledge_map("rag-intensive", foreign_principal)
    with pytest.raises(EnrollmentRequiredError):
        service.source_locator("rag-intensive", source_span_id, foreign_principal)


def test_postgres_distinct_attempts_serialize_mastery_updates() -> None:
    factory = _postgres_factory()
    service = PostgresAdaptiveService(factory)
    before_state = next(
        item
        for item in service.learning_states("rag-intensive", DEMO_PRINCIPAL)
        if item.concept_id == "ai_llm_foundations"
    )
    payload = DiagnosticSubmission.model_validate(
        {"answers": [{"question_id": "diag-foundation-01", "option_id": "b"}]}
    )

    def submit_distinct(_):
        return PostgresAdaptiveService(factory).submit_diagnostic(
            "rag-intensive", payload, f"distinct-{uuid4()}", DEMO_PRINCIPAL
        )

    with ThreadPoolExecutor(max_workers=2) as executor:
        list(executor.map(submit_distinct, range(2)))

    after_state = next(
        item
        for item in service.learning_states("rag-intensive", DEMO_PRINCIPAL)
        if item.concept_id == "ai_llm_foundations"
    )
    assert len(after_state.evidence_ids) == len(before_state.evidence_ids) + 2


def test_postgres_lab_persists_evidence_event_mastery_and_plan_idempotently() -> None:
    factory = _postgres_factory()
    service = PostgresAdaptiveService(factory)
    lab = next(item for item in LABS if item.id == "metadata-filtering")
    payload = LabSubmission.model_validate(
        {
            "configuration": {
                "tenant_filter": True,
                "course_filter": True,
                "filter_stage": "pre",
            },
            "transfer_answers": {
                "isolation": "Tenant authorization ngăn leak và rò rỉ chéo tenant.",
                "recall": "Pre-filter payload thu hẹp candidate trước top-k và giữ recall đúng scope.",
            },
        }
    )
    deterministic_score = score_lab(lab, payload)
    idempotency_key = f"lab-contract-{uuid4()}"

    result = service.submit_lab(
        "rag-intensive",
        lab.id,
        lab.concept_id,
        payload,
        deterministic_score,
        idempotency_key,
        DEMO_PRINCIPAL,
    )
    replay = service.submit_lab(
        "rag-intensive",
        lab.id,
        lab.concept_id,
        payload,
        deterministic_score,
        idempotency_key,
        DEMO_PRINCIPAL,
    )

    assert result.score == 100
    assert result.passed is True
    assert result.mastery_update is not None
    assert result.mastery_update.concept_id == "metadata_filtered_search"
    assert result.study_plan is not None
    assert replay.model_dump(mode="json") == result.model_dump(mode="json")

    with factory() as session, session.begin():
        set_tenant_context(session, DEMO_PRINCIPAL.tenant_id)
        evidence_count = session.scalar(
            select(func.count())
            .select_from(evidence_ledger)
            .where(evidence_ledger.c.id == result.evidence_event_id)
        )
        event_count = session.scalar(
            select(func.count())
            .select_from(learning_events)
            .where(learning_events.c.id == result.evidence_event_id)
        )
    assert evidence_count == 1
    assert event_count == 1


def test_postgres_essay_jsonb_updates_support_ai_and_human_review() -> None:
    factory = _postgres_factory()
    with factory() as session, session.begin():
        set_tenant_context(session, DEMO_PRINCIPAL.tenant_id)
        course_id = session.scalar(
            select(courses.c.id).where(
                courses.c.tenant_id == DEMO_PRINCIPAL.tenant_id,
                courses.c.slug == "rag-intensive",
            )
        )
    assert course_id is not None

    store = PostgresEssayStore(factory)
    submission = EssaySubmissionRequest(
        prompt="Thiết kế một pipeline RAG an toàn và có kiểm chứng nguồn.",
        answer=(
            "Áp dụng tenant filter trước retrieval, hợp nhất dense và BM25 bằng RRF, "
            "rồi kiểm tra citation với source span trước khi trả lời."
        ),
        rubric_id="system-design-v1",
    )
    submitted = store.submit(
        principal=DEMO_PRINCIPAL,
        course_id=course_id,
        payload=submission,
        idempotency_key=f"essay-jsonb-{uuid4()}",
    )
    rubric = get_rubric(submission.rubric_id)
    judgement = deterministic_grade(
        prompt=submission.prompt,
        answer=submission.answer,
        rubric=rubric.criteria,
    )
    graded = store.apply_judgement(
        tenant_id=DEMO_PRINCIPAL.tenant_id,
        essay_id=submitted.id,
        judgement=judgement,
        rubric=rubric,
    )
    assert graded.provider == "mock"
    assert graded.rubric_version == rubric.id

    reviewed = store.release_human_review(
        tenant_id=DEMO_PRINCIPAL.tenant_id,
        essay_id=submitted.id,
        reviewer_id=uuid4(),
        review=EssayHumanReviewRequest(
            score=8,
            max_score=10,
            feedback="Đã đối chiếu rubric và source evidence.",
            criterion_scores={"grounding": 3, "reasoning": 3, "transfer": 2},
        ),
    )
    assert reviewed.status == "graded"
    assert reviewed.provider == "human"
