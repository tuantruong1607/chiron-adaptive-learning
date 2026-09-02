from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import UTC, datetime
from functools import lru_cache
from threading import RLock
from uuid import UUID, uuid4

from psycopg.types.json import Jsonb
from sqlalchemy import text

from .adaptive.essay_judge import EssayJudgement
from .adaptive.rubrics import VersionedRubric, get_rubric
from .auth import Principal
from .config import get_settings
from .db import get_session_factory, set_tenant_context
from .persistence.repositories import AttemptRepository, OutboxRepository
from .schemas import EssayHumanReviewRequest, EssayResponse, EssaySubmissionRequest


class EssayConflictError(RuntimeError):
    pass


class EssayNotFoundError(LookupError):
    pass


@dataclass(frozen=True, slots=True)
class EssayRecord:
    id: UUID
    course: str
    prompt: str
    answer: str
    rubric_id: str
    status: str
    created_at: datetime
    tenant_id: UUID | None = None
    learner_id: UUID | None = None
    score: float | None = None
    max_score: float | None = None
    confidence: float | None = None
    provider: str | None = None
    model: str | None = None
    feedback: str | None = None
    rubric_version: str | None = None
    criterion_scores: dict[str, float] | None = None
    human_review_required: bool = False
    graded_at: datetime | None = None
    reviewer_id: UUID | None = None

    def as_response(self) -> EssayResponse:
        return EssayResponse(
            id=self.id,
            course=self.course,
            prompt=self.prompt,
            answer=self.answer,
            rubric_id=self.rubric_id,
            status=self.status,
            score=self.score,
            max_score=self.max_score,
            confidence=self.confidence,
            provider=self.provider,
            model=self.model,
            feedback=self.feedback,
            rubric_version=self.rubric_version,
            criterion_scores=self.criterion_scores or {},
            human_review_required=self.human_review_required,
            graded_at=self.graded_at,
            reviewer_id=self.reviewer_id,
            created_at=self.created_at,
        )


def _record_payload(record: EssayRecord) -> dict:
    return record.as_response().model_dump(mode="json")


class InMemoryEssayStore:
    def __init__(self) -> None:
        self._lock = RLock()
        self._records: dict[UUID, EssayRecord] = {}
        self._idempotency: dict[tuple[UUID, UUID, str, str], UUID] = {}

    def submit(
        self, *, principal: Principal, payload: EssaySubmissionRequest, idempotency_key: str
    ) -> EssayResponse:
        key = (principal.tenant_id, principal.user_id, payload.course, idempotency_key)
        with self._lock:
            existing_id = self._idempotency.get(key)
            if existing_id is not None:
                existing = self._records[existing_id]
                if (existing.prompt, existing.answer, existing.rubric_id) != (
                    payload.prompt,
                    payload.answer,
                    payload.rubric_id,
                ):
                    raise EssayConflictError("Idempotency-Key was already used with a different essay")
                return existing.as_response()
            record = EssayRecord(
                id=uuid4(),
                course=payload.course,
                prompt=payload.prompt,
                answer=payload.answer,
                rubric_id=payload.rubric_id,
                status="pending_ai_grading",
                created_at=datetime.now(UTC),
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                rubric_version=payload.rubric_id,
            )
            self._records[record.id] = record
            self._idempotency[key] = record.id
            return record.as_response()

    def get(self, *, principal: Principal, essay_id: UUID) -> EssayResponse:
        with self._lock:
            record = self._records.get(essay_id)
            if (
                record is None
                or record.tenant_id != principal.tenant_id
                or record.learner_id != principal.user_id
            ):
                raise EssayNotFoundError("Essay not found")
            return record.as_response()

    def get_for_grading(self, *, tenant_id: UUID, essay_id: UUID) -> EssayRecord:
        with self._lock:
            record = self._records.get(essay_id)
            if record is None or record.tenant_id != tenant_id:
                raise EssayNotFoundError("Essay not found")
            return record

    def apply_judgement(
        self, *, tenant_id: UUID, essay_id: UUID, judgement: EssayJudgement, rubric: VersionedRubric
    ) -> EssayResponse:
        with self._lock:
            record = self._records.get(essay_id)
            if record is None or record.tenant_id != tenant_id:
                raise EssayNotFoundError("Essay not found")
            reviewed = judgement.confidence < 0.65
            self._records[essay_id] = EssayRecord(
                id=record.id,
                course=record.course,
                prompt=record.prompt,
                answer=record.answer,
                rubric_id=record.rubric_id,
                status="needs_human_review" if reviewed else "graded",
                created_at=record.created_at,
                tenant_id=record.tenant_id,
                learner_id=record.learner_id,
                score=float(judgement.total_score),
                max_score=float(judgement.max_score),
                confidence=judgement.confidence,
                provider=judgement.provider,
                model=judgement.model,
                feedback=judgement.feedback,
                rubric_version=rubric.id,
                criterion_scores={
                    key: float(value) for key, value in judgement.criterion_scores.items()
                },
                human_review_required=reviewed,
                graded_at=datetime.now(UTC),
            )
            return self._records[essay_id].as_response()

    def release_human_review(
        self,
        *,
        tenant_id: UUID,
        essay_id: UUID,
        reviewer_id: UUID,
        review: EssayHumanReviewRequest,
    ) -> EssayResponse:
        with self._lock:
            record = self._records.get(essay_id)
            if record is None or record.tenant_id != tenant_id:
                raise EssayNotFoundError("Essay not found")
            if review.score > review.max_score:
                raise ValueError("Score cannot exceed max_score")
            self._records[essay_id] = EssayRecord(
                id=record.id,
                course=record.course,
                prompt=record.prompt,
                answer=record.answer,
                rubric_id=record.rubric_id,
                status="graded",
                created_at=record.created_at,
                tenant_id=record.tenant_id,
                learner_id=record.learner_id,
                score=review.score,
                max_score=review.max_score,
                confidence=record.confidence,
                provider="human",
                model="human-review",
                feedback=review.feedback,
                rubric_version=record.rubric_version or record.rubric_id,
                criterion_scores=review.criterion_scores,
                human_review_required=False,
                graded_at=datetime.now(UTC),
                reviewer_id=reviewer_id,
            )
            return self._records[essay_id].as_response()

    def escalate_overdue(self, *, tenant_id: UUID, cutoff: datetime) -> int:
        escalated = 0
        with self._lock:
            for essay_id, record in tuple(self._records.items()):
                if (
                    record.tenant_id != tenant_id
                    or record.status != "pending_ai_grading"
                    or record.created_at > cutoff
                ):
                    continue
                self._records[essay_id] = replace(
                    record,
                    status="needs_human_review",
                    feedback="AI grading SLA expired. The response was routed to instructor review.",
                    human_review_required=True,
                )
                escalated += 1
        return escalated

    def list_review_queue(self, *, tenant_id: UUID) -> list[EssayResponse]:
        with self._lock:
            records = [
                record.as_response()
                for record in self._records.values()
                if record.tenant_id == tenant_id and record.status == "needs_human_review"
            ]
        return sorted(records, key=lambda item: item.created_at)


class PostgresEssayStore:
    def __init__(self, session_factory=None) -> None:
        self.attempts = AttemptRepository()
        self.outbox = OutboxRepository()
        self.session_factory = session_factory or get_session_factory()

    def submit(
        self,
        *,
        principal: Principal,
        course_id: UUID,
        payload: EssaySubmissionRequest,
        idempotency_key: str,
    ) -> EssayResponse:
        request = payload.model_dump(mode="json")
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            attempt = self.attempts.acquire(
                session,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                course_id=course_id,
                idempotency_key=idempotency_key,
                request_payload=request,
                attempt_type="essay",
            )
            stored = attempt.payload.get("essay")
            if stored is not None:
                if attempt.payload.get("request") != request:
                    raise EssayConflictError("Idempotency-Key was already used with a different essay")
                return EssayResponse.model_validate(stored)
            record = EssayRecord(
                id=attempt.id,
                course=payload.course,
                prompt=payload.prompt,
                answer=payload.answer,
                rubric_id=payload.rubric_id,
                status="pending_ai_grading",
                created_at=datetime.now(UTC),
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                rubric_version=payload.rubric_id,
            )
            self.attempts.complete(
                session,
                attempt.id,
                {"request": request, "essay": _record_payload(record)},
            )
            self.outbox.add(
                session,
                tenant_id=principal.tenant_id,
                event_type="essay.grading.requested",
                aggregate_id=record.id,
                payload={
                    "attempt_id": str(record.id),
                    "rubric_id": record.rubric_id,
                    "rubric": get_rubric(record.rubric_id).as_payload(),
                },
                dedupe_key=f"essay-grading:{record.id}",
            )
            return record.as_response()

    def get(self, *, principal: Principal, essay_id: UUID) -> EssayResponse:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            record = self.attempts.get_owned(
                session,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                attempt_id=essay_id,
                attempt_type="essay",
            )
            if record is None or "essay" not in record.payload:
                raise EssayNotFoundError("Essay not found")
            return EssayResponse.model_validate(record.payload["essay"])

    def get_for_grading(self, *, tenant_id: UUID, essay_id: UUID) -> EssayRecord:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, tenant_id)
            row = session.execute(
                text(
                    "SELECT payload FROM attempts WHERE id=:id AND tenant_id=:tenant_id "
                    "AND attempt_type='essay' FOR UPDATE"
                ),
                {"id": essay_id, "tenant_id": tenant_id},
            ).mappings().first()
            if row is None or "essay" not in (row["payload"] or {}):
                raise EssayNotFoundError("Essay not found")
            response = EssayResponse.model_validate(row["payload"]["essay"])
            return EssayRecord(
                **response.model_dump(), tenant_id=tenant_id, learner_id=None
            )

    def apply_judgement(
        self, *, tenant_id: UUID, essay_id: UUID, judgement: EssayJudgement, rubric: VersionedRubric
    ) -> EssayResponse:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, tenant_id)
            row = session.execute(
                text(
                    "SELECT payload FROM attempts WHERE id=:id AND tenant_id=:tenant_id "
                    "AND attempt_type='essay' FOR UPDATE"
                ),
                {"id": essay_id, "tenant_id": tenant_id},
            ).mappings().first()
            if row is None or "essay" not in (row["payload"] or {}):
                raise EssayNotFoundError("Essay not found")
            payload = dict(row["payload"])
            essay = dict(payload["essay"])
            reviewed = judgement.confidence < 0.65
            essay.update(
                {
                    "status": "needs_human_review" if reviewed else "graded",
                    "score": float(judgement.total_score),
                    "max_score": float(judgement.max_score),
                    "confidence": judgement.confidence,
                    "provider": judgement.provider,
                    "model": judgement.model,
                    "feedback": judgement.feedback,
                    "rubric_version": rubric.id,
                    "criterion_scores": {
                        key: float(value) for key, value in judgement.criterion_scores.items()
                    },
                    "human_review_required": reviewed,
                    "graded_at": datetime.now(UTC).isoformat(),
                }
            )
            payload["essay"] = essay
            session.execute(
                text(
                    "UPDATE attempts SET status='completed', payload=:payload WHERE id=:id"
                ),
                {"id": essay_id, "payload": Jsonb(payload)},
            )
            return EssayResponse.model_validate(essay)

    def escalate_overdue(self, *, tenant_id: UUID, cutoff: datetime) -> int:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, tenant_id)
            rows = session.execute(
                text(
                    "SELECT id, payload FROM attempts WHERE tenant_id=:tenant_id "
                    "AND attempt_type='essay' AND created_at <= :cutoff "
                    "AND payload->'essay'->>'status'='pending_ai_grading' FOR UPDATE"
                ),
                {"tenant_id": tenant_id, "cutoff": cutoff},
            ).mappings().all()
            for row in rows:
                payload = dict(row["payload"])
                essay = dict(payload["essay"])
                essay.update(
                    {
                        "status": "needs_human_review",
                        "feedback": (
                            "AI grading SLA expired. The response was routed to instructor review."
                        ),
                        "human_review_required": True,
                    }
                )
                payload["essay"] = essay
                session.execute(
                    text("UPDATE attempts SET payload=:payload WHERE id=:id"),
                    {"id": row["id"], "payload": Jsonb(payload)},
                )
            return len(rows)

    def list_review_queue(self, *, tenant_id: UUID) -> list[EssayResponse]:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, tenant_id)
            rows = session.execute(
                text(
                    "SELECT payload FROM attempts WHERE tenant_id=:tenant_id "
                    "AND attempt_type='essay' "
                    "AND payload->'essay'->>'status'='needs_human_review' "
                    "ORDER BY created_at ASC"
                ),
                {"tenant_id": tenant_id},
            ).mappings().all()
            return [EssayResponse.model_validate(row["payload"]["essay"]) for row in rows]

    def release_human_review(
        self,
        *,
        tenant_id: UUID,
        essay_id: UUID,
        reviewer_id: UUID,
        review: EssayHumanReviewRequest,
    ) -> EssayResponse:
        if review.score > review.max_score:
            raise ValueError("Score cannot exceed max_score")
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, tenant_id)
            row = session.execute(
                text(
                    "SELECT payload FROM attempts WHERE id=:id AND tenant_id=:tenant_id "
                    "AND attempt_type='essay' FOR UPDATE"
                ),
                {"id": essay_id, "tenant_id": tenant_id},
            ).mappings().first()
            if row is None or "essay" not in (row["payload"] or {}):
                raise EssayNotFoundError("Essay not found")
            payload = dict(row["payload"])
            essay = dict(payload["essay"])
            essay.update(
                {
                    "status": "graded",
                    "score": review.score,
                    "max_score": review.max_score,
                    "provider": "human",
                    "model": "human-review",
                    "feedback": review.feedback,
                    "criterion_scores": review.criterion_scores,
                    "human_review_required": False,
                    "graded_at": datetime.now(UTC).isoformat(),
                    "reviewer_id": str(reviewer_id),
                }
            )
            payload["essay"] = essay
            session.execute(
                text("UPDATE attempts SET status='completed', payload=:payload WHERE id=:id"),
                {"id": essay_id, "payload": Jsonb(payload)},
            )
            return EssayResponse.model_validate(essay)


@lru_cache
def get_essay_store():
    return PostgresEssayStore() if get_settings().use_postgres else InMemoryEssayStore()
