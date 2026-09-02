from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

import httpx

from .config import WorkerSettings
from .outbox import OutboxEvent, OutboxStore


@dataclass(slots=True)
class EssayGradingConsumer:
    store: OutboxStore
    settings: WorkerSettings

    def _grade(self, event: OutboxEvent) -> None:
        if not self.settings.worker_internal_token:
            raise RuntimeError("WORKER_INTERNAL_TOKEN is required for essay grading")
        response = httpx.post(
            f"{self.settings.api_base_url.rstrip('/')}/api/v1/internal/essays/"
            f"{event.payload['attempt_id']}/grade",
            headers={"X-Worker-Token": self.settings.worker_internal_token},
            json={"tenant_id": str(event.tenant_id)},
            timeout=90,
        )
        if response.status_code >= 400:
            raise RuntimeError(f"essay grading callback failed ({response.status_code}): {response.text[:500]}")

    def _escalate_overdue(self, tenant_id: UUID) -> int:
        response = httpx.post(
            f"{self.settings.api_base_url.rstrip('/')}/api/v1/internal/essays/escalate-overdue",
            headers={"X-Worker-Token": self.settings.worker_internal_token},
            json={"tenant_id": str(tenant_id)},
            timeout=30,
        )
        if response.status_code >= 400:
            raise RuntimeError(
                f"essay SLA escalation failed ({response.status_code}): {response.text[:500]}"
            )
        return int(response.json().get("escalated", 0))

    def drain_once(self) -> dict[str, int]:
        if not self.settings.worker_internal_token:
            return {"claimed": 0, "processed": 0, "failed": 0, "escalated": 0}
        claimed = processed = failed = escalated = 0
        for tenant_id in self.store.tenant_ids():
            for event in self.store.claim_event_type(tenant_id, "essay.grading.requested"):
                claimed += 1
                try:
                    self._grade(event)
                    self.store.success(event)
                    processed += 1
                except Exception as exc:
                    self.store.failure(event, exc)
                    failed += 1
            try:
                escalated += self._escalate_overdue(tenant_id)
            except Exception:
                failed += 1
        return {
            "claimed": claimed,
            "processed": processed,
            "failed": failed,
            "escalated": escalated,
        }
