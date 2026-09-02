import asyncio
import json
import time
from dataclasses import asdict, dataclass, field
from typing import Protocol

from redis.asyncio import Redis
from redis.exceptions import RedisError

from ..config import Settings
from .types import (
    AvailabilityStatus,
    FailureKind,
    LLMProviderFailure,
    RateLimitSnapshot,
    RequestPriority,
)


@dataclass
class RouteState:
    provider: str
    model: str
    availability: AvailabilityStatus = AvailabilityStatus.UNKNOWN
    checked_at: float | None = None
    open_until: float = 0
    unavailable_until: float = 0
    consecutive_failures: int = 0
    failure_window_started: float = 0
    half_open_in_flight: bool = False
    rate_limit: RateLimitSnapshot = field(default_factory=RateLimitSnapshot)

    def public_dict(self) -> dict:
        value = asdict(self)
        value["availability"] = self.availability.value
        value.pop("rate_limit", None)
        return value


class LLMStateStore(Protocol):
    async def allow_request(
        self,
        provider: str,
        model: str,
        priority: RequestPriority,
    ) -> bool: ...

    async def record_success(
        self,
        provider: str,
        model: str,
        rate_limit: RateLimitSnapshot,
    ) -> None: ...

    async def record_failure(self, failure: LLMProviderFailure) -> None: ...

    async def mark_availability(
        self,
        provider: str,
        model: str,
        status: AvailabilityStatus,
    ) -> None: ...

    async def snapshot(self) -> list[dict]: ...


class InMemoryLLMStateStore:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._states: dict[str, RouteState] = {}
        self._lock = asyncio.Lock()

    def _state(self, provider: str, model: str) -> RouteState:
        key = f"{provider}:{model}"
        if key not in self._states:
            self._states[key] = RouteState(provider=provider, model=model)
        return self._states[key]

    def _has_background_reserve(self, state: RouteState) -> bool:
        rate = state.rate_limit
        reserve = self._settings.llm_quota_reserve_ratio
        if (
            rate.request_limit
            and rate.request_remaining is not None
            and rate.request_remaining / rate.request_limit <= reserve
        ):
            return False
        return not (
            rate.token_limit
            and rate.token_remaining is not None
            and rate.token_remaining / rate.token_limit <= reserve
        )

    async def allow_request(
        self,
        provider: str,
        model: str,
        priority: RequestPriority,
    ) -> bool:
        async with self._lock:
            state = self._state(provider, model)
            now = time.time()
            if state.unavailable_until > now or state.open_until > now:
                return False
            if priority is RequestPriority.BACKGROUND and not self._has_background_reserve(state):
                return False
            if state.open_until:
                if state.half_open_in_flight:
                    return False
                state.half_open_in_flight = True
            return True

    async def record_success(
        self,
        provider: str,
        model: str,
        rate_limit: RateLimitSnapshot,
    ) -> None:
        async with self._lock:
            state = self._state(provider, model)
            state.availability = AvailabilityStatus.AVAILABLE
            state.checked_at = time.time()
            state.open_until = 0
            state.unavailable_until = 0
            state.consecutive_failures = 0
            state.failure_window_started = 0
            state.half_open_in_flight = False
            state.rate_limit = rate_limit

    async def record_failure(self, failure: LLMProviderFailure) -> None:
        if failure.model is None:
            return
        async with self._lock:
            state = self._state(failure.provider, failure.model)
            now = time.time()
            state.checked_at = now
            state.half_open_in_flight = False
            state.rate_limit = failure.rate_limit
            if failure.kind is FailureKind.QUOTA:
                state.availability = AvailabilityStatus.DEGRADED
                state.open_until = now + (
                    failure.rate_limit.retry_after_seconds
                    or self._settings.llm_circuit_open_seconds
                )
                return
            if failure.kind is FailureKind.MODEL_NOT_FOUND:
                state.availability = AvailabilityStatus.UNAVAILABLE
                state.unavailable_until = now + self._settings.llm_model_not_found_ttl_seconds
                state.open_until = state.unavailable_until
                return
            if failure.kind not in {FailureKind.UNAVAILABLE, FailureKind.INVALID_RESPONSE}:
                return
            if (
                now - state.failure_window_started
                > self._settings.llm_circuit_failure_window_seconds
            ):
                state.failure_window_started = now
                state.consecutive_failures = 0
            state.consecutive_failures += 1
            state.availability = AvailabilityStatus.DEGRADED
            if state.consecutive_failures >= self._settings.llm_circuit_failure_threshold:
                state.open_until = now + self._settings.llm_circuit_open_seconds

    async def mark_availability(
        self,
        provider: str,
        model: str,
        status: AvailabilityStatus,
    ) -> None:
        async with self._lock:
            state = self._state(provider, model)
            state.availability = status
            state.checked_at = time.time()
            if status is AvailabilityStatus.AVAILABLE:
                state.unavailable_until = 0
            elif status is AvailabilityStatus.UNAVAILABLE:
                state.unavailable_until = (
                    time.time() + self._settings.llm_model_not_found_ttl_seconds
                )

    async def snapshot(self) -> list[dict]:
        async with self._lock:
            return [state.public_dict() for state in self._states.values()]


class RedisLLMStateStore:
    def __init__(self, settings: Settings, redis: Redis) -> None:
        self._settings = settings
        self._redis = redis
        self._prefix = "chiron:llm:route"

    def _key(self, provider: str, model: str) -> str:
        return f"{self._prefix}:{provider}:{model}"

    async def allow_request(
        self,
        provider: str,
        model: str,
        priority: RequestPriority,
    ) -> bool:
        key = self._key(provider, model)
        now = time.time()
        raw_rate = await self._redis.hget(key, "rate_limit")
        if priority is RequestPriority.BACKGROUND and raw_rate:
            parsed = json.loads(raw_rate)
            reserve = self._settings.llm_quota_reserve_ratio
            if (
                parsed.get("request_limit")
                and parsed.get("request_remaining") is not None
                and parsed["request_remaining"] / parsed["request_limit"] <= reserve
            ):
                return False
            if (
                parsed.get("token_limit")
                and parsed.get("token_remaining") is not None
                and parsed["token_remaining"] / parsed["token_limit"] <= reserve
            ):
                return False
        script = """
        local unavailable = tonumber(redis.call('HGET', KEYS[1], 'unavailable_until') or '0')
        local open_until = tonumber(redis.call('HGET', KEYS[1], 'open_until') or '0')
        if unavailable > tonumber(ARGV[1]) or open_until > tonumber(ARGV[1]) then return 0 end
        if open_until > 0 then
          local lock_until = tonumber(redis.call('HGET', KEYS[1], 'half_open_until') or '0')
          if lock_until > tonumber(ARGV[1]) then return 0 end
          redis.call('HSET', KEYS[1], 'half_open_until', tonumber(ARGV[1]) + tonumber(ARGV[2]))
        end
        return 1
        """
        allowed = await self._redis.eval(
            script,
            1,
            key,
            now,
            self._settings.llm_circuit_open_seconds,
        )
        return bool(allowed)

    async def record_success(
        self,
        provider: str,
        model: str,
        rate_limit: RateLimitSnapshot,
    ) -> None:
        key = self._key(provider, model)
        await self._redis.hset(
            key,
            mapping={
                "provider": provider,
                "model": model,
                "availability": AvailabilityStatus.AVAILABLE.value,
                "checked_at": time.time(),
                "open_until": 0,
                "unavailable_until": 0,
                "failures": 0,
                "window_started": 0,
                "half_open_until": 0,
                "rate_limit": json.dumps(rate_limit.as_dict()),
            },
        )
        await self._redis.expire(key, 86400)

    async def record_failure(self, failure: LLMProviderFailure) -> None:
        if failure.model is None:
            return
        key = self._key(failure.provider, failure.model)
        now = time.time()
        mapping: dict[str, str | int | float] = {
            "provider": failure.provider,
            "model": failure.model,
            "checked_at": now,
            "half_open_until": 0,
            "rate_limit": json.dumps(failure.rate_limit.as_dict()),
        }
        if failure.kind is FailureKind.QUOTA:
            mapping["availability"] = AvailabilityStatus.DEGRADED.value
            mapping["open_until"] = now + (
                failure.rate_limit.retry_after_seconds or self._settings.llm_circuit_open_seconds
            )
            await self._redis.hset(key, mapping=mapping)
        elif failure.kind is FailureKind.MODEL_NOT_FOUND:
            unavailable_until = now + self._settings.llm_model_not_found_ttl_seconds
            mapping.update(
                {
                    "availability": AvailabilityStatus.UNAVAILABLE.value,
                    "unavailable_until": unavailable_until,
                    "open_until": unavailable_until,
                }
            )
            await self._redis.hset(key, mapping=mapping)
        elif failure.kind in {FailureKind.UNAVAILABLE, FailureKind.INVALID_RESPONSE}:
            window_started = float(await self._redis.hget(key, "window_started") or 0)
            if now - window_started > self._settings.llm_circuit_failure_window_seconds:
                await self._redis.hset(key, mapping={"window_started": now, "failures": 0})
            failures = await self._redis.hincrby(key, "failures", 1)
            mapping["availability"] = AvailabilityStatus.DEGRADED.value
            if failures >= self._settings.llm_circuit_failure_threshold:
                mapping["open_until"] = now + self._settings.llm_circuit_open_seconds
            await self._redis.hset(key, mapping=mapping)
        await self._redis.expire(key, 86400)

    async def mark_availability(
        self,
        provider: str,
        model: str,
        status: AvailabilityStatus,
    ) -> None:
        mapping: dict[str, str | float] = {
            "provider": provider,
            "model": model,
            "availability": status.value,
            "checked_at": time.time(),
        }
        if status is AvailabilityStatus.AVAILABLE:
            mapping["unavailable_until"] = 0
        elif status is AvailabilityStatus.UNAVAILABLE:
            mapping["unavailable_until"] = (
                time.time() + self._settings.llm_model_not_found_ttl_seconds
            )
        key = self._key(provider, model)
        await self._redis.hset(key, mapping=mapping)
        await self._redis.expire(key, 86400)

    async def snapshot(self) -> list[dict]:
        rows: list[dict] = []
        async for key in self._redis.scan_iter(match=f"{self._prefix}:*"):
            values = await self._redis.hgetall(key)
            decoded = {
                (name.decode() if isinstance(name, bytes) else name): (
                    value.decode() if isinstance(value, bytes) else value
                )
                for name, value in values.items()
            }
            decoded.pop("rate_limit", None)
            rows.append(decoded)
        return rows


class ResilientLLMStateStore:
    def __init__(self, primary: LLMStateStore, fallback: LLMStateStore) -> None:
        self._primary = primary
        self._fallback = fallback

    async def _call(self, method: str, *args):
        try:
            return await getattr(self._primary, method)(*args)
        except RedisError:
            return await getattr(self._fallback, method)(*args)

    async def allow_request(self, provider, model, priority):
        return await self._call("allow_request", provider, model, priority)

    async def record_success(self, provider, model, rate_limit):
        await self._call("record_success", provider, model, rate_limit)

    async def record_failure(self, failure):
        await self._call("record_failure", failure)

    async def mark_availability(self, provider, model, status):
        await self._call("mark_availability", provider, model, status)

    async def snapshot(self):
        return await self._call("snapshot")


def build_state_store(settings: Settings) -> LLMStateStore:
    memory = InMemoryLLMStateStore(settings)
    use_redis = settings.llm_state_backend == "redis" or (
        settings.llm_state_backend == "auto" and settings.redis_url
    )
    if not use_redis or not settings.redis_url:
        return memory
    redis = Redis.from_url(settings.redis_url)
    return ResilientLLMStateStore(RedisLLMStateStore(settings, redis), memory)
