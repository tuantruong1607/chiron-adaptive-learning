from __future__ import annotations

from types import SimpleNamespace
from uuid import UUID

from chiron_worker.essay_grading import EssayGradingConsumer
from chiron_worker.outbox import OutboxEvent

TENANT_ID = UUID("c2e1e494-3fa4-596f-8714-6877bac903dd")
EVENT_ID = UUID("11111111-1111-4111-8111-111111111111")


class FakeStore:
    def __init__(self) -> None:
        self.event = OutboxEvent(
            EVENT_ID,
            TENANT_ID,
            {"attempt_id": "22222222-2222-4222-8222-222222222222"},
            0,
        )
        self.failed = False

    def tenant_ids(self):
        return [TENANT_ID]

    def claim_event_type(self, _tenant_id, _event_type):
        return [self.event]

    def success(self, _event):
        raise AssertionError("provider failure must not acknowledge the event")

    def failure(self, _event, _error):
        self.failed = True


class FakeResponse:
    def __init__(self, status_code: int, payload: dict) -> None:
        self.status_code = status_code
        self._payload = payload
        self.text = "provider unavailable"

    def json(self) -> dict:
        return self._payload


def test_failed_grading_remains_retryable_and_overdue_attempt_is_escalated(monkeypatch) -> None:
    responses = iter([FakeResponse(503, {}), FakeResponse(200, {"escalated": 1})])
    monkeypatch.setattr(
        "chiron_worker.essay_grading.httpx.post",
        lambda *args, **kwargs: next(responses),
    )
    store = FakeStore()
    settings = SimpleNamespace(
        worker_internal_token="worker-token",
        api_base_url="http://api:8000",
    )

    result = EssayGradingConsumer(store, settings).drain_once()

    assert result == {"claimed": 1, "processed": 0, "failed": 1, "escalated": 1}
    assert store.failed is True
