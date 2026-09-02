import logging

from ..config import Settings
from .provider import LLMProvider, OpenAICompatibleProvider
from .registry import ModelRegistry, build_model_registry
from .state import LLMStateStore, build_state_store
from .types import (
    DataSensitivity,
    FailureKind,
    LLMProviderFailure,
    LLMRequest,
    LLMResult,
)

logger = logging.getLogger("chiron.llm.router")


class LLMRouter:
    def __init__(
        self,
        *,
        providers: dict[str, LLMProvider],
        registry: ModelRegistry,
        state: LLMStateStore,
        fallback_enabled: bool = True,
        fallback_on_quota: bool = True,
        fallback_on_unavailable: bool = True,
        fallback_allowed_sensitivities: set[str] | None = None,
    ) -> None:
        self.providers = providers
        self.registry = registry
        self.state = state
        self.fallback_enabled = fallback_enabled
        self.fallback_on_quota = fallback_on_quota
        self.fallback_on_unavailable = fallback_on_unavailable
        self.fallback_allowed_sensitivities = fallback_allowed_sensitivities or set()

    def _provider_allowed(self, provider: str, sensitivity: DataSensitivity) -> bool:
        if sensitivity is DataSensitivity.RESTRICTED:
            return False
        if provider != "gemini":
            return True
        return sensitivity.value in self.fallback_allowed_sensitivities

    def _failure_allows_next_route(self, failure: LLMProviderFailure) -> bool:
        if failure.kind in {
            FailureKind.AUTHENTICATION,
            FailureKind.REQUEST,
            FailureKind.SAFETY,
        }:
            return False
        if failure.is_quota_error:
            return self.fallback_on_quota
        if failure.is_unavailable_error:
            return self.fallback_on_unavailable
        return False

    async def complete(self, request: LLMRequest) -> LLMResult:
        if request.sensitivity is DataSensitivity.RESTRICTED:
            raise LLMProviderFailure(
                "policy",
                "Restricted data cannot use configured external providers",
                kind=FailureKind.SAFETY,
            )

        candidates = self.registry.candidates(request.workload)
        if not self.fallback_enabled:
            candidates = candidates[:1]
        attempted: list[str] = []
        first_failure: LLMProviderFailure | None = None
        last_failure: LLMProviderFailure | None = None

        for route_index, route in enumerate(candidates):
            if len(attempted) >= request.max_fallbacks + 1:
                break
            if not self._provider_allowed(route.provider, request.sensitivity):
                continue
            provider = self.providers.get(route.provider)
            if provider is None:
                continue
            if not await self.state.allow_request(
                route.provider,
                route.model,
                request.priority,
            ):
                continue

            attempted.append(route.key)
            try:
                result = await provider.complete(request, route.model)
            except LLMProviderFailure as exc:
                failure = exc
                if exc.model is None:
                    failure = LLMProviderFailure(
                        exc.provider,
                        str(exc),
                        exc.status_code,
                        model=route.model,
                        kind=exc.kind,
                        rate_limit=exc.rate_limit,
                    )
                await self.state.record_failure(failure)
                first_failure = first_failure or failure
                last_failure = failure
                logger.warning(
                    "llm_route_failed provider=%s model=%s kind=%s trace_id=%s",
                    route.provider,
                    route.model,
                    failure.kind.value,
                    request.trace_id,
                )
                if not self._failure_allows_next_route(failure):
                    raise failure from exc
                continue

            await self.state.record_success(
                route.provider,
                route.model,
                result.rate_limit,
            )
            return LLMResult(
                content=result.content,
                provider=result.provider,
                model=result.model,
                used_fallback=route_index > 0,
                fallback_reason=first_failure.kind.value if first_failure else None,
                attempted_routes=tuple(attempted),
                usage=result.usage,
                rate_limit=result.rate_limit,
            )

        if last_failure:
            raise last_failure
        raise LLMProviderFailure(
            "router",
            "No policy-allowed LLM route is currently available",
            503,
            kind=FailureKind.UNAVAILABLE,
        )

    async def status(self) -> list[dict]:
        recorded = await self.state.snapshot()
        by_route = {(str(item.get("provider")), str(item.get("model"))): item for item in recorded}
        routes: list[dict] = []
        for route in self.registry.all_routes():
            if route.provider not in self.providers:
                continue
            routes.append(
                by_route.get(
                    (route.provider, route.model),
                    {
                        "provider": route.provider,
                        "model": route.model,
                        "availability": "unknown",
                        "checked_at": None,
                        "open_until": 0,
                        "unavailable_until": 0,
                    },
                )
            )
        return routes


def build_llm_router(settings: Settings) -> LLMRouter | None:
    if settings.llm_provider == "mock":
        return None

    providers: dict[str, LLMProvider] = {}
    if settings.groq_api_key:
        providers["groq"] = OpenAICompatibleProvider(
            name="groq",
            base_url=settings.groq_base_url,
            api_key=settings.groq_api_key,
            timeout_seconds=settings.llm_request_timeout_seconds,
        )
    if settings.openai_api_key:
        providers["openai"] = OpenAICompatibleProvider(
            name="openai",
            base_url=settings.openai_base_url,
            api_key=settings.openai_api_key,
            timeout_seconds=settings.llm_request_timeout_seconds,
        )
    if settings.openrouter_api_key:
        providers["openrouter"] = OpenAICompatibleProvider(
            name="openrouter",
            base_url=settings.openrouter_base_url,
            api_key=settings.openrouter_api_key,
            timeout_seconds=settings.llm_request_timeout_seconds,
        )
    if settings.deepseek_api_key:
        providers["deepseek"] = OpenAICompatibleProvider(
            name="deepseek",
            base_url=settings.deepseek_base_url,
            api_key=settings.deepseek_api_key,
            timeout_seconds=settings.llm_request_timeout_seconds,
        )
    if settings.gemini_api_key:
        providers["gemini"] = OpenAICompatibleProvider(
            name="gemini",
            base_url=settings.gemini_base_url,
            api_key=settings.gemini_api_key,
            timeout_seconds=settings.llm_request_timeout_seconds,
        )
    if settings.llm_api_key:
        provider_name = settings.llm_provider if settings.llm_provider not in providers else "generic"
        providers[provider_name] = OpenAICompatibleProvider(
            name=provider_name,
            base_url=settings.llm_base_url or "https://api.openai.com/v1",
            api_key=settings.llm_api_key,
            timeout_seconds=settings.llm_request_timeout_seconds,
        )
    if settings.llm_provider not in providers:
        return None

    return LLMRouter(
        providers=providers,
        registry=build_model_registry(settings),
        state=build_state_store(settings),
        fallback_enabled=settings.llm_fallback_enabled,
        fallback_on_quota=settings.llm_fallback_on_quota,
        fallback_on_unavailable=settings.llm_fallback_on_unavailable,
        fallback_allowed_sensitivities=settings.fallback_allowed_sensitivities,
    )
