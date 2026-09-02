from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID, uuid4


class Workload(StrEnum):
    TUTOR = "tutor"
    EXTRACTION = "extraction"
    GRADER = "grader"
    RESEARCH = "research"


class DataSensitivity(StrEnum):
    PUBLIC = "public"
    SYNTHETIC = "synthetic"
    PRIVATE = "private"
    RESTRICTED = "restricted"


class RequestPriority(StrEnum):
    INTERACTIVE = "interactive"
    ASYNC_HIGH = "async_high"
    BACKGROUND = "background"


class FailureKind(StrEnum):
    QUOTA = "quota"
    UNAVAILABLE = "unavailable"
    MODEL_NOT_FOUND = "model_not_found"
    AUTHENTICATION = "authentication"
    REQUEST = "request"
    SAFETY = "safety"
    INVALID_RESPONSE = "invalid_response"


class AvailabilityStatus(StrEnum):
    UNKNOWN = "unknown"
    AVAILABLE = "available"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"


@dataclass(frozen=True)
class RateLimitSnapshot:
    request_limit: int | None = None
    request_remaining: int | None = None
    token_limit: int | None = None
    token_remaining: int | None = None
    request_reset: str | None = None
    token_reset: str | None = None
    retry_after_seconds: float | None = None

    def as_dict(self) -> dict[str, int | float | str | None]:
        return {
            "request_limit": self.request_limit,
            "request_remaining": self.request_remaining,
            "token_limit": self.token_limit,
            "token_remaining": self.token_remaining,
            "request_reset": self.request_reset,
            "token_reset": self.token_reset,
            "retry_after_seconds": self.retry_after_seconds,
        }


@dataclass(frozen=True)
class TokenUsage:
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    total_tokens: int | None = None


@dataclass(frozen=True)
class LLMRequest:
    workload: Workload
    system_prompt: str
    user_prompt: str
    sensitivity: DataSensitivity = DataSensitivity.PRIVATE
    priority: RequestPriority = RequestPriority.INTERACTIVE
    temperature: float = 0.2
    max_tokens: int = 1200
    max_fallbacks: int = 2
    trace_id: UUID = field(default_factory=uuid4)


@dataclass(frozen=True)
class LLMResult:
    content: str
    provider: str
    model: str
    used_fallback: bool = False
    fallback_reason: str | None = None
    attempted_routes: tuple[str, ...] = ()
    usage: TokenUsage = field(default_factory=TokenUsage)
    rate_limit: RateLimitSnapshot = field(default_factory=RateLimitSnapshot)


def failure_kind_for_status(status_code: int | None) -> FailureKind:
    if status_code == 429:
        return FailureKind.QUOTA
    if status_code == 404:
        return FailureKind.MODEL_NOT_FOUND
    if status_code in {401, 403}:
        return FailureKind.AUTHENTICATION
    if status_code in {408, 500, 502, 503, 504} or status_code is None:
        return FailureKind.UNAVAILABLE
    return FailureKind.REQUEST


class LLMProviderFailure(RuntimeError):
    def __init__(
        self,
        provider: str,
        message: str,
        status_code: int | None = None,
        *,
        model: str | None = None,
        kind: FailureKind | None = None,
        rate_limit: RateLimitSnapshot | None = None,
    ) -> None:
        super().__init__(message)
        self.provider = provider
        self.model = model
        self.status_code = status_code
        self.kind = kind or failure_kind_for_status(status_code)
        self.rate_limit = rate_limit or RateLimitSnapshot()

    @property
    def is_quota_error(self) -> bool:
        return self.kind is FailureKind.QUOTA

    @property
    def is_unavailable_error(self) -> bool:
        return self.kind in {
            FailureKind.UNAVAILABLE,
            FailureKind.MODEL_NOT_FOUND,
            FailureKind.INVALID_RESPONSE,
        }

    @property
    def fallback_eligible(self) -> bool:
        return self.is_quota_error or self.is_unavailable_error
