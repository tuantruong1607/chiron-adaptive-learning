from typing import Protocol

import httpx

from .types import (
    FailureKind,
    LLMProviderFailure,
    LLMRequest,
    LLMResult,
    RateLimitSnapshot,
    TokenUsage,
)


class LLMProvider(Protocol):
    name: str

    async def complete(self, request: LLMRequest, model: str) -> LLMResult: ...

    async def list_models(self) -> set[str]: ...


def _integer_header(headers: httpx.Headers, name: str) -> int | None:
    value = headers.get(name)
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _float_header(headers: httpx.Headers, name: str) -> float | None:
    value = headers.get(name)
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def rate_limit_from_headers(headers: httpx.Headers) -> RateLimitSnapshot:
    return RateLimitSnapshot(
        request_limit=_integer_header(headers, "x-ratelimit-limit-requests"),
        request_remaining=_integer_header(headers, "x-ratelimit-remaining-requests"),
        token_limit=_integer_header(headers, "x-ratelimit-limit-tokens"),
        token_remaining=_integer_header(headers, "x-ratelimit-remaining-tokens"),
        request_reset=headers.get("x-ratelimit-reset-requests"),
        token_reset=headers.get("x-ratelimit-reset-tokens"),
        retry_after_seconds=_float_header(headers, "retry-after"),
    )


class OpenAICompatibleProvider:
    def __init__(
        self,
        *,
        name: str,
        base_url: str,
        api_key: str,
        timeout_seconds: float,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.name = name
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._timeout = timeout_seconds
        self._transport = transport

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

    async def list_models(self) -> set[str]:
        try:
            async with httpx.AsyncClient(
                timeout=self._timeout,
                transport=self._transport,
            ) as client:
                response = await client.get(
                    f"{self._base_url}/models",
                    headers=self._headers(),
                )
        except httpx.TimeoutException as exc:
            raise LLMProviderFailure(self.name, f"{self.name} model list timed out", 408) from exc
        except httpx.RequestError as exc:
            raise LLMProviderFailure(self.name, f"{self.name} model list network error") from exc
        if response.status_code >= 400:
            raise LLMProviderFailure(
                self.name,
                f"{self.name} model list returned HTTP {response.status_code}",
                response.status_code,
                rate_limit=rate_limit_from_headers(response.headers),
            )
        try:
            models = response.json().get("data", [])
            return {
                str(item["id"]).removeprefix("models/")
                for item in models
                if isinstance(item, dict) and item.get("id")
            }
        except (AttributeError, TypeError, ValueError) as exc:
            raise LLMProviderFailure(
                self.name,
                f"{self.name} returned an invalid model list",
                response.status_code,
                kind=FailureKind.INVALID_RESPONSE,
            ) from exc

    async def complete(self, request: LLMRequest, model: str) -> LLMResult:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": request.system_prompt},
                {"role": "user", "content": request.user_prompt},
            ],
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
        }
        try:
            async with httpx.AsyncClient(
                timeout=self._timeout,
                transport=self._transport,
            ) as client:
                response = await client.post(
                    f"{self._base_url}/chat/completions",
                    headers=self._headers(),
                    json=payload,
                )
        except httpx.TimeoutException as exc:
            raise LLMProviderFailure(
                self.name,
                f"{self.name} timed out",
                408,
                model=model,
            ) from exc
        except httpx.RequestError as exc:
            raise LLMProviderFailure(
                self.name,
                f"{self.name} network error",
                model=model,
            ) from exc

        rate_limit = rate_limit_from_headers(response.headers)
        if response.status_code >= 400:
            raise LLMProviderFailure(
                self.name,
                f"{self.name} returned HTTP {response.status_code}",
                response.status_code,
                model=model,
                rate_limit=rate_limit,
            )

        try:
            data = response.json()
            content = data["choices"][0]["message"]["content"]
            raw_usage = data.get("usage", {})
        except (AttributeError, KeyError, IndexError, TypeError, ValueError) as exc:
            raise LLMProviderFailure(
                self.name,
                f"{self.name} returned an invalid response",
                response.status_code,
                model=model,
                kind=FailureKind.INVALID_RESPONSE,
                rate_limit=rate_limit,
            ) from exc
        if not isinstance(content, str) or not content.strip():
            raise LLMProviderFailure(
                self.name,
                f"{self.name} returned empty content",
                response.status_code,
                model=model,
                kind=FailureKind.INVALID_RESPONSE,
                rate_limit=rate_limit,
            )
        usage = TokenUsage(
            prompt_tokens=raw_usage.get("prompt_tokens"),
            completion_tokens=raw_usage.get("completion_tokens"),
            total_tokens=raw_usage.get("total_tokens"),
        )
        return LLMResult(
            content=content.strip(),
            provider=self.name,
            model=model,
            usage=usage,
            rate_limit=rate_limit,
        )
