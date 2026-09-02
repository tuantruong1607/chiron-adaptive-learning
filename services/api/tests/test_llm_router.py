import asyncio

import httpx
import pytest

from app.config import Settings
from app.llm.degraded import build_degraded_tutor_answer
from app.llm.provider import OpenAICompatibleProvider
from app.llm.registry import build_model_registry
from app.llm.router import LLMRouter, build_llm_router
from app.llm.state import InMemoryLLMStateStore
from app.llm.types import (
    DataSensitivity,
    LLMProviderFailure,
    LLMRequest,
    LLMResult,
    Workload,
)
from app.repository import repository


class FakeProvider:
    def __init__(
        self,
        name: str,
        failures: dict[str, LLMProviderFailure] | None = None,
    ) -> None:
        self.name = name
        self.failures = failures or {}
        self.calls: dict[str, int] = {}

    async def list_models(self) -> set[str]:
        return set(self.calls) | set(self.failures)

    async def complete(self, request: LLMRequest, model: str) -> LLMResult:
        self.calls[model] = self.calls.get(model, 0) + 1
        if model in self.failures:
            raise self.failures[model]
        return LLMResult(content=f"answer from {self.name}", provider=self.name, model=model)


def settings(**overrides) -> Settings:
    values = {
        "_env_file": None,
        "llm_provider": "groq",
        "groq_api_key": "synthetic-groq-key",
        "gemini_api_key": "synthetic-gemini-key",
        "redis_url": None,
        "llm_tutor_model": "qwen-tutor",
        "llm_extraction_model": "oss-extract",
        "llm_grader_model": "oss-grade",
        "llm_research_model": "compound-research",
        "llm_groq_fallback_model": "oss-fallback",
        "gemini_tutor_model": "gemini-tutor",
        "gemini_extraction_model": "gemini-extract",
        "gemini_grader_model": "gemini-grade",
        "gemini_research_model": "gemini-research",
    }
    values.update(overrides)
    return Settings(**values)


def request(sensitivity: DataSensitivity) -> LLMRequest:
    return LLMRequest(
        workload=Workload.TUTOR,
        system_prompt="system",
        user_prompt="synthetic test",
        sensitivity=sensitivity,
    )


def router(
    config: Settings,
    groq: FakeProvider,
    gemini: FakeProvider,
) -> LLMRouter:
    return LLMRouter(
        providers={"groq": groq, "gemini": gemini},
        registry=build_model_registry(config),
        state=InMemoryLLMStateStore(config),
        fallback_allowed_sensitivities={"public", "synthetic"},
    )


def failure(provider: str, status: int) -> LLMProviderFailure:
    return LLMProviderFailure(provider, f"HTTP {status}", status)


def test_qwen_quota_falls_back_to_gpt_oss_inside_groq() -> None:
    config = settings()
    groq = FakeProvider("groq", {"qwen-tutor": failure("groq", 429)})
    gemini = FakeProvider("gemini")
    result = asyncio.run(router(config, groq, gemini).complete(request(DataSensitivity.PRIVATE)))
    assert result.provider == "groq"
    assert result.model == "oss-fallback"
    assert result.used_fallback is True
    assert result.fallback_reason == "quota"
    assert gemini.calls == {}


def test_public_data_uses_gemini_after_both_groq_routes_fail() -> None:
    config = settings()
    groq = FakeProvider(
        "groq",
        {
            "qwen-tutor": failure("groq", 429),
            "oss-fallback": failure("groq", 429),
        },
    )
    gemini = FakeProvider("gemini")
    result = asyncio.run(router(config, groq, gemini).complete(request(DataSensitivity.PUBLIC)))
    assert result.provider == "gemini"
    assert result.model == "gemini-tutor"
    assert result.attempted_routes == (
        "groq:qwen-tutor",
        "groq:oss-fallback",
        "gemini:gemini-tutor",
    )


def test_private_data_never_falls_back_to_gemini_free() -> None:
    config = settings()
    groq = FakeProvider(
        "groq",
        {
            "qwen-tutor": failure("groq", 429),
            "oss-fallback": failure("groq", 429),
        },
    )
    gemini = FakeProvider("gemini")
    with pytest.raises(LLMProviderFailure):
        asyncio.run(router(config, groq, gemini).complete(request(DataSensitivity.PRIVATE)))
    assert gemini.calls == {}


def test_auth_error_stops_without_masking_configuration_incident() -> None:
    config = settings()
    groq = FakeProvider("groq", {"qwen-tutor": failure("groq", 401)})
    gemini = FakeProvider("gemini")
    with pytest.raises(LLMProviderFailure) as captured:
        asyncio.run(router(config, groq, gemini).complete(request(DataSensitivity.PUBLIC)))
    assert captured.value.kind.value == "authentication"
    assert groq.calls == {"qwen-tutor": 1}
    assert gemini.calls == {}


def test_circuit_opens_and_skips_repeated_unavailable_model_calls() -> None:
    config = settings(llm_circuit_failure_threshold=2)
    groq = FakeProvider("groq", {"qwen-tutor": failure("groq", 503)})
    gemini = FakeProvider("gemini")
    hardened = router(config, groq, gemini)
    for _ in range(3):
        result = asyncio.run(hardened.complete(request(DataSensitivity.PRIVATE)))
        assert result.model == "oss-fallback"
    assert groq.calls["qwen-tutor"] == 2
    assert groq.calls["oss-fallback"] == 3


def test_provider_normalizes_rate_limit_headers_and_usage() -> None:
    def handler(_: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            headers={
                "x-ratelimit-limit-requests": "1000",
                "x-ratelimit-remaining-requests": "998",
                "x-ratelimit-limit-tokens": "8000",
                "x-ratelimit-remaining-tokens": "7600",
            },
            json={
                "choices": [{"message": {"content": "ok"}}],
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": 2,
                    "total_tokens": 12,
                },
            },
        )

    provider = OpenAICompatibleProvider(
        name="test",
        base_url="https://provider.invalid/v1",
        api_key="synthetic",
        timeout_seconds=1,
        transport=httpx.MockTransport(handler),
    )
    result = asyncio.run(provider.complete(request(DataSensitivity.SYNTHETIC), "model"))
    assert result.rate_limit.request_remaining == 998
    assert result.rate_limit.token_remaining == 7600
    assert result.usage.total_tokens == 12


def test_degraded_tutor_returns_only_retrieved_sources() -> None:
    retrieval = repository.retrieve("RRF raw score")
    result = build_degraded_tutor_answer(retrieval, reason="quota")
    assert result.degraded is True
    assert result.provider == "retrieval-only"
    assert result.citations
    assert "tạm thời không khả dụng" in result.answer


def test_default_registry_uses_current_callable_models() -> None:
    config = Settings(
        _env_file=None,
        llm_provider="groq",
        groq_api_key="synthetic-groq-key",
        gemini_api_key="synthetic-gemini-key",
        redis_url=None,
    )
    built = build_llm_router(config)
    assert built is not None
    tutor_routes = built.registry.candidates(Workload.TUTOR)
    assert [(route.provider, route.model) for route in tutor_routes] == [
        ("groq", "llama-3.3-70b-versatile"),
        ("groq", "llama-3.1-8b-instant"),
        ("gemini", "gemini-3.5-flash-lite"),
    ]

    openai_config = Settings(
        _env_file=None,
        llm_provider="openai",
        openai_api_key="synthetic-openai-key",
        redis_url=None,
    )
    openai_built = build_llm_router(openai_config)
    assert openai_built is not None
    openai_tutor_routes = openai_built.registry.candidates(Workload.TUTOR)
    assert [(route.provider, route.model) for route in openai_tutor_routes] == [
        ("openai", "gpt-4o-mini"),
    ]
