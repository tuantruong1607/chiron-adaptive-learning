from __future__ import annotations

import asyncio
import time
from collections.abc import Awaitable, Callable
from typing import Any

import httpx
import redis.asyncio as redis_async
from sqlalchemy import text

from .config import Settings
from .db import get_engine


async def _probe(
    name: str,
    operation: Callable[[], Awaitable[Any]],
    timeout_seconds: float,
) -> dict[str, Any]:
    started = time.perf_counter()
    try:
        await asyncio.wait_for(operation(), timeout=timeout_seconds)
        return {
            "status": "ok",
            "latency_ms": round((time.perf_counter() - started) * 1000, 1),
        }
    except TimeoutError:
        return {"status": "timeout", "error": f"{name} probe exceeded timeout"}
    except Exception as exc:
        return {"status": "error", "error": type(exc).__name__}


async def probe_database(settings: Settings) -> dict[str, Any]:
    if not settings.database_url:
        return {"status": "skipped"}

    async def operation() -> None:
        def query() -> None:
            with get_engine().connect() as connection:
                connection.execute(text("SELECT 1"))

        await asyncio.to_thread(query)

    return await _probe("database", operation, settings.readiness_timeout_seconds)


async def probe_redis(settings: Settings) -> dict[str, Any]:
    if not settings.redis_url:
        return {"status": "skipped"}

    async def operation() -> None:
        client = redis_async.from_url(
            settings.redis_url, socket_timeout=settings.readiness_timeout_seconds
        )
        try:
            await client.ping()
        finally:
            await client.aclose()

    return await _probe("redis", operation, settings.readiness_timeout_seconds)


async def probe_qdrant(settings: Settings) -> dict[str, Any]:
    if not settings.qdrant_url:
        return {"status": "skipped"}

    async def operation() -> None:
        headers = {"api-key": settings.qdrant_api_key} if settings.qdrant_api_key else {}
        async with httpx.AsyncClient(timeout=settings.readiness_timeout_seconds) as client:
            response = await client.get(
                f"{settings.qdrant_url.rstrip('/')}/collections", headers=headers
            )
            response.raise_for_status()

    return await _probe("qdrant", operation, settings.readiness_timeout_seconds)


async def dependency_readiness(settings: Settings, llm_router: Any) -> dict[str, Any]:
    database, redis, qdrant = await asyncio.gather(
        probe_database(settings),
        probe_redis(settings),
        probe_qdrant(settings),
    )
    llm_routes = await llm_router.status() if llm_router else []
    llm_status = "mock-or-missing-key"
    if llm_routes:
        statuses = {route["availability"] for route in llm_routes}
        if statuses == {"unknown"}:
            llm_status = "configured-unprobed"
        elif statuses == {"unavailable"}:
            llm_status = "unavailable"
        elif "degraded" in statuses or "unavailable" in statuses:
            llm_status = "degraded"
        else:
            llm_status = "available"
    dependencies = {
        "database": database,
        "redis": redis,
        "qdrant": qdrant,
        "llm": {"status": llm_status, "routes": llm_routes},
    }
    required_ok = all(
        dependencies[name]["status"] in {"ok", "skipped"}
        for name in ("database", "redis", "qdrant")
    )
    return {"ready": required_ok, "dependencies": dependencies}
