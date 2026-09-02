from __future__ import annotations

from typing import Protocol

from app.auth import Principal
from app.schemas import DiagnosticSubmission


class AdaptiveContract(Protocol):
    def submit_diagnostic(
        self,
        course_slug: str,
        payload: DiagnosticSubmission,
        idempotency_key: str,
        principal: Principal,
    ): ...

    def learning_states(self, course_slug: str, principal: Principal): ...

    def plan(
        self,
        course_slug: str,
        principal: Principal,
        *,
        horizon_days: int,
        daily_minutes: int,
    ): ...


def assert_adaptive_contract(
    service: AdaptiveContract, principal: Principal, idempotency_key: str
) -> None:
    payload = DiagnosticSubmission.model_validate(
        {"answers": [{"question_id": "diag-foundation-01", "option_id": "b"}]}
    )
    first = service.submit_diagnostic("rag-intensive", payload, idempotency_key, principal)
    replay = service.submit_diagnostic("rag-intensive", payload, idempotency_key, principal)

    assert first.attempt_id == replay.attempt_id
    assert first.model_dump(mode="json") == replay.model_dump(mode="json")
    assert first.mastery_updates
    assert service.learning_states("rag-intensive", principal)
    plan = service.plan("rag-intensive", principal, horizon_days=3, daily_minutes=60)
    assert plan.horizon_days == 3
    assert plan.daily_minutes == 60
    assert plan.component_scores
