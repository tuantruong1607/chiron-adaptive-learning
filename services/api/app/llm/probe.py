from dataclasses import asdict, dataclass

from .provider import LLMProvider
from .registry import ModelRegistry
from .state import LLMStateStore
from .types import (
    AvailabilityStatus,
    DataSensitivity,
    LLMProviderFailure,
    LLMRequest,
    Workload,
)


@dataclass(frozen=True)
class ProbeResult:
    provider: str
    model: str
    status: AvailabilityStatus
    active: bool
    detail: str | None = None

    def as_dict(self) -> dict:
        value = asdict(self)
        value["status"] = self.status.value
        return value


class AvailabilityProbe:
    def __init__(
        self,
        providers: dict[str, LLMProvider],
        registry: ModelRegistry,
        state: LLMStateStore,
    ) -> None:
        self._providers = providers
        self._registry = registry
        self._state = state

    async def refresh(self, *, active: bool = False) -> list[ProbeResult]:
        results: list[ProbeResult] = []
        routes_by_provider: dict[str, list] = {}
        for route in self._registry.all_routes():
            routes_by_provider.setdefault(route.provider, []).append(route)

        for provider_name, routes in routes_by_provider.items():
            provider = self._providers.get(provider_name)
            if provider is None:
                continue
            try:
                available_models = await provider.list_models()
            except LLMProviderFailure as exc:
                for route in routes:
                    await self._state.mark_availability(
                        provider_name,
                        route.model,
                        AvailabilityStatus.DEGRADED,
                    )
                    results.append(
                        ProbeResult(
                            provider_name,
                            route.model,
                            AvailabilityStatus.DEGRADED,
                            active,
                            exc.kind.value,
                        )
                    )
                continue

            for route in routes:
                status = (
                    AvailabilityStatus.AVAILABLE
                    if route.model in available_models
                    else AvailabilityStatus.UNAVAILABLE
                )
                detail: str | None = None
                if active and status is AvailabilityStatus.AVAILABLE:
                    try:
                        result = await provider.complete(
                            LLMRequest(
                                workload=Workload.TUTOR,
                                sensitivity=DataSensitivity.SYNTHETIC,
                                system_prompt="Synthetic availability probe.",
                                user_prompt="Reply exactly OK.",
                                max_tokens=256,
                                max_fallbacks=0,
                            ),
                            route.model,
                        )
                        await self._state.record_success(
                            provider_name,
                            route.model,
                            result.rate_limit,
                        )
                    except LLMProviderFailure as exc:
                        status = AvailabilityStatus.UNAVAILABLE
                        detail = exc.kind.value
                await self._state.mark_availability(provider_name, route.model, status)
                results.append(ProbeResult(provider_name, route.model, status, active, detail))
        return results
