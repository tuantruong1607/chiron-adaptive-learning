from __future__ import annotations

import re
from threading import Lock

from app.auth import Principal
from app.repository import AdaptiveLearningRepository
from app.schemas import (
    DiagnosticResult,
    DiagnosticSubmission,
    LabResult,
    LabSubmission,
    LearningStateOut,
    SourceLocator,
    StudyPlan,
)


class MemoryAdaptiveService:
    """Per-learner memory adapter used by unit tests and offline development."""

    def __init__(self) -> None:
        self._lock = Lock()
        self._repositories: dict[tuple[str, str], AdaptiveLearningRepository] = {}

    def _repository(self, principal: Principal) -> AdaptiveLearningRepository:
        key = (str(principal.tenant_id), str(principal.user_id))
        with self._lock:
            return self._repositories.setdefault(key, AdaptiveLearningRepository())

    def submit_diagnostic(
        self,
        course_slug: str,
        payload: DiagnosticSubmission,
        idempotency_key: str,
        principal: Principal,
    ) -> DiagnosticResult:
        repository = self._repository(principal)
        if course_slug != repository.course().id:
            raise LookupError("course not found")
        return repository.submit_diagnostic(payload, idempotency_key)

    def diagnostic_completed(self, course_slug: str, principal: Principal) -> bool:
        repository = self._repository(principal)
        if course_slug != repository.course().id:
            raise LookupError("course not found")
        return repository.diagnostic_completed()

    def knowledge_map(self, course_slug: str, principal: Principal):
        repository = self._repository(principal)
        if course_slug != repository.course().id:
            raise LookupError("course not found")
        return repository.knowledge_map()

    def source_locator(
        self, course_slug: str, source_span_id: str, principal: Principal
    ) -> SourceLocator:
        knowledge_map = self.knowledge_map(course_slug, principal)
        citation = next(
            (
                citation
                for node in knowledge_map.nodes
                for citation in node.citations
                if citation.source_span_id == source_span_id
            ),
            None,
        )
        if citation is None:
            raise LookupError("Source span not found in active knowledge graph")
        page_match = re.search(r"\d+", citation.locator)
        return SourceLocator(
            **citation.model_dump(),
            source_type="course_source",
            locator_kind="page" if page_match else "source_span",
            label=citation.locator,
            page=int(page_match.group()) if page_match else None,
        )

    def learning_states(self, course_slug: str, principal: Principal) -> list[LearningStateOut]:
        repository = self._repository(principal)
        if course_slug != repository.course().id:
            raise LookupError("course not found")
        return repository.learning_states()

    def plan(
        self,
        course_slug: str,
        principal: Principal,
        *,
        horizon_days: int,
        daily_minutes: int,
    ) -> StudyPlan:
        repository = self._repository(principal)
        if course_slug != repository.course().id:
            raise LookupError("course not found")
        return repository.plan(horizon_days=horizon_days, daily_minutes=daily_minutes)

    def submit_lab(
        self,
        course_slug: str,
        lab_id: str,
        concept_id: str,
        payload: LabSubmission,
        score: LabResult,
        idempotency_key: str,
        principal: Principal,
    ) -> LabResult:
        repository = self._repository(principal)
        if course_slug != repository.course().id:
            raise LookupError("course not found")
        del concept_id, score
        return repository.submit_lab(lab_id, payload, idempotency_key)
