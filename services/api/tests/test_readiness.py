from __future__ import annotations

import asyncio
from types import SimpleNamespace

from app import readiness


class FakeRouter:
    async def status(self):
        return [
            {
                "provider": "groq",
                "model": "tutor-model",
                "availability": "degraded",
            }
        ]


def test_readiness_requires_infrastructure_but_not_an_llm_prompt(monkeypatch) -> None:
    async def ok(_settings):
        return {"status": "ok", "latency_ms": 1.0}

    monkeypatch.setattr(readiness, "probe_database", ok)
    monkeypatch.setattr(readiness, "probe_redis", ok)
    monkeypatch.setattr(readiness, "probe_qdrant", ok)
    result = asyncio.run(readiness.dependency_readiness(SimpleNamespace(), FakeRouter()))

    assert result["ready"] is True
    assert result["dependencies"]["llm"]["status"] == "degraded"


def test_readiness_fails_when_a_required_dependency_probe_fails(monkeypatch) -> None:
    async def ok(_settings):
        return {"status": "ok", "latency_ms": 1.0}

    async def failed(_settings):
        return {"status": "error", "error": "OperationalError"}

    monkeypatch.setattr(readiness, "probe_database", failed)
    monkeypatch.setattr(readiness, "probe_redis", ok)
    monkeypatch.setattr(readiness, "probe_qdrant", ok)
    result = asyncio.run(readiness.dependency_readiness(SimpleNamespace(), FakeRouter()))

    assert result["ready"] is False
    assert result["dependencies"]["database"]["status"] == "error"
