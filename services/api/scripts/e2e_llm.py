import asyncio

from app.config import get_settings
from app.llm.degraded import build_degraded_tutor_answer
from app.llm.router import build_llm_router
from app.llm.types import (
    DataSensitivity,
    LLMProviderFailure,
    LLMRequest,
    LLMResult,
    Workload,
)
from app.repository import repository


class SelectiveQuotaProvider:
    name = "groq"

    def __init__(self, delegate, failed_models: set[str] | None = None) -> None:
        self._delegate = delegate
        self._failed_models = failed_models

    async def list_models(self) -> set[str]:
        return await self._delegate.list_models()

    async def complete(self, request: LLMRequest, model: str) -> LLMResult:
        if self._failed_models is None or model in self._failed_models:
            raise LLMProviderFailure(
                "groq",
                "forced quota for deterministic E2E",
                429,
                model=model,
            )
        return await self._delegate.complete(request, model)


def synthetic_request(sensitivity: DataSensitivity) -> LLMRequest:
    return LLMRequest(
        workload=Workload.TUTOR,
        sensitivity=sensitivity,
        system_prompt=(
            "This is a provider connectivity test. Answer in Vietnamese using only the "
            "explicitly synthetic context. Do not use external facts."
        ),
        user_prompt=(
            "SYNTHETIC CONTEXT: Reciprocal Rank Fusion combines ranked lists using rank "
            "positions rather than adding incomparable raw scores.\n"
            "QUESTION: Vì sao dữ liệu giả lập này nói RRF dùng rank?"
        ),
        max_tokens=256,
    )


def new_router():
    router = build_llm_router(get_settings())
    if router is None:
        raise RuntimeError("LLM router is not configured. Check LLM_PROVIDER and API keys.")
    return router


async def run() -> None:
    primary_router = new_router()
    groq = await primary_router.complete(synthetic_request(DataSensitivity.SYNTHETIC))
    assert groq.provider == "groq"

    intra_router = new_router()
    original_groq = intra_router.providers["groq"]
    intra_router.providers["groq"] = SelectiveQuotaProvider(
        original_groq,
        {get_settings().llm_tutor_model},
    )
    intra = await intra_router.complete(synthetic_request(DataSensitivity.PRIVATE))
    assert intra.provider == "groq"
    assert intra.model == get_settings().llm_groq_fallback_model
    assert intra.used_fallback is True

    gemini_router = new_router()
    gemini_router.providers["groq"] = SelectiveQuotaProvider(gemini_router.providers["groq"])
    try:
        gemini = await gemini_router.complete(synthetic_request(DataSensitivity.SYNTHETIC))
        assert gemini.provider == "gemini"
        assert gemini.used_fallback is True
        gemini_status = {"status": "passed", "model": gemini.model}
    except LLMProviderFailure as exc:
        if not exc.is_unavailable_error:
            raise
        degraded = build_degraded_tutor_answer(
            repository.retrieve("RRF raw score"),
            reason=exc.kind.value,
        )
        assert degraded.degraded is True
        assert degraded.citations
        gemini_status = {
            "status": "provider-unavailable-degraded-mode-passed",
            "reason": exc.kind.value,
        }

    private_router = new_router()
    private_router.providers["groq"] = SelectiveQuotaProvider(private_router.providers["groq"])
    try:
        await private_router.complete(synthetic_request(DataSensitivity.PRIVATE))
    except LLMProviderFailure:
        private_guard = "passed"
    else:
        raise AssertionError("Private data unexpectedly reached Gemini")

    print("Groq primary:", {"status": "passed", "model": groq.model})
    print("Intra-Groq fallback:", {"status": "passed", "model": intra.model})
    print("Gemini public fallback:", gemini_status)
    print("Private-data Gemini guard:", private_guard)


if __name__ == "__main__":
    asyncio.run(run())
