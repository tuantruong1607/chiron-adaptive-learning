from dataclasses import dataclass

from ..config import Settings
from .types import Workload


@dataclass(frozen=True)
class ModelRoute:
    provider: str
    model: str

    @property
    def key(self) -> str:
        return f"{self.provider}:{self.model}"


class ModelRegistry:
    def __init__(self, routes: dict[Workload, tuple[ModelRoute, ...]]) -> None:
        self._routes = routes

    def candidates(self, workload: Workload) -> tuple[ModelRoute, ...]:
        return self._routes.get(workload, ())

    def all_routes(self) -> tuple[ModelRoute, ...]:
        unique: dict[str, ModelRoute] = {}
        for routes in self._routes.values():
            for route in routes:
                unique[route.key] = route
        return tuple(unique.values())


def build_model_registry(settings: Settings) -> ModelRegistry:
    gemini_routes = {
        Workload.TUTOR: ModelRoute("gemini", settings.gemini_tutor_model),
        Workload.EXTRACTION: ModelRoute("gemini", settings.gemini_extraction_model),
        Workload.GRADER: ModelRoute("gemini", settings.gemini_grader_model),
        Workload.RESEARCH: ModelRoute("gemini", settings.gemini_research_model),
    }
    if settings.llm_provider == "gemini":
        return ModelRegistry({workload: (route,) for workload, route in gemini_routes.items()})

    if settings.llm_provider == "openai":
        openai_tutor = ModelRoute("openai", settings.openai_tutor_model)
        return ModelRegistry({
            Workload.TUTOR: (openai_tutor,),
            Workload.EXTRACTION: (openai_tutor,),
            Workload.GRADER: (openai_tutor,),
            Workload.RESEARCH: (openai_tutor,),
        })

    if settings.llm_provider == "openrouter":
        openrouter_tutor = ModelRoute("openrouter", settings.openrouter_tutor_model)
        return ModelRegistry({
            Workload.TUTOR: (openrouter_tutor,),
            Workload.EXTRACTION: (openrouter_tutor,),
            Workload.GRADER: (openrouter_tutor,),
            Workload.RESEARCH: (openrouter_tutor,),
        })

    if settings.llm_provider == "deepseek":
        deepseek_tutor = ModelRoute("deepseek", settings.deepseek_tutor_model)
        return ModelRegistry({
            Workload.TUTOR: (deepseek_tutor,),
            Workload.EXTRACTION: (deepseek_tutor,),
            Workload.GRADER: (deepseek_tutor,),
            Workload.RESEARCH: (deepseek_tutor,),
        })

    if settings.llm_provider in {"generic", "llm"}:
        generic_tutor = ModelRoute(settings.llm_provider, settings.llm_tutor_model)
        return ModelRegistry({
            Workload.TUTOR: (generic_tutor,),
            Workload.EXTRACTION: (generic_tutor,),
            Workload.GRADER: (generic_tutor,),
            Workload.RESEARCH: (generic_tutor,),
        })

    groq_fallback = ModelRoute("groq", settings.llm_groq_fallback_model)
    routes: dict[Workload, tuple[ModelRoute, ...]] = {
        Workload.TUTOR: (
            ModelRoute("groq", settings.llm_tutor_model),
            groq_fallback,
            gemini_routes[Workload.TUTOR],
        ),
        Workload.EXTRACTION: (
            ModelRoute("groq", settings.llm_extraction_model),
            groq_fallback,
            gemini_routes[Workload.EXTRACTION],
        ),
        Workload.GRADER: (
            ModelRoute("groq", settings.llm_grader_model),
            gemini_routes[Workload.GRADER],
        ),
        Workload.RESEARCH: (
            ModelRoute("groq", settings.llm_research_model),
            groq_fallback,
            gemini_routes[Workload.RESEARCH],
        ),
    }
    return ModelRegistry(routes)
