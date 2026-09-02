from __future__ import annotations

import json
from functools import lru_cache
from pathlib import PurePath
from typing import Any

from celery import Celery
from celery.exceptions import CeleryError
from celery.exceptions import TimeoutError as CeleryTimeoutError

from .auth import Principal
from .config import Settings, get_settings
from .schemas import Citation, RetrievalHit, RetrievalResponse


class RetrievalUnavailableError(RuntimeError):
    pass


def route_query(query: str) -> str:
    normalized = query.casefold()
    if any(
        term in normalized
        for term in (
            "liên hệ",
            "mối quan hệ",
            "chuỗi",
            "multi-hop",
            "multi hop",
            "nguyên nhân",
            "kết quả",
            "ảnh hưởng",
            "dẫn đến",
            "so sánh",
            "khác nhau",
        )
    ):
        return "multi_hop"
    if any(
        term in normalized
        for term in ("tiên quyết", "kiến thức nền", "nền tảng", "trước khi", "phụ thuộc")
    ):
        return "prerequisite"
    return "direct"


def _locator(payload: dict[str, Any]) -> str:
    locator = payload.get("locator") or {}
    if isinstance(locator, str):
        return locator
    page = locator.get("pdf_page") or locator.get("page") or locator.get("page_label")
    section = locator.get("section") or locator.get("heading") or locator.get("source_anchor")
    parts = []
    if page is not None:
        parts.append(f"trang {page}")
    if section:
        parts.append(str(section))
    return " · ".join(parts) or json.dumps(locator, ensure_ascii=False, sort_keys=True)


def response_from_task(query: str, result: dict[str, Any]) -> RetrievalResponse:
    hits: list[RetrievalHit] = []
    for item in result.get("hits", []):
        payload = item.get("payload") or {}
        content = str(payload.get("content") or "")
        source_path = str(payload.get("source_path") or "")
        title = str(payload.get("document_title") or PurePath(source_path).name or "Nguồn học")
        hits.append(
            RetrievalHit(
                score=float(item.get("score", 0)),
                text=content,
                citation=Citation(
                    source_span_id=str(payload.get("source_span_id") or ""),
                    title=title,
                    locator=_locator(payload),
                    excerpt=content[:500],
                ),
            )
        )
    return RetrievalResponse(
        query=query,
        route=result.get("route", route_query(query)),
        hits=hits,
        retrieval_mode=result.get("retrieval_mode", "hybrid"),
        degraded=bool(result.get("degraded", False)),
        strategy=result.get("strategy", "single_hybrid"),
        subqueries=[str(item) for item in result.get("subqueries", [query])],
    )


@lru_cache
def _celery_client() -> Celery:
    settings = get_settings()
    if not settings.redis_url:
        raise RetrievalUnavailableError("REDIS_URL is required for retrieval tasks")
    return Celery("chiron-api-retrieval", broker=settings.redis_url, backend=settings.redis_url)


def retrieve(
    query: str,
    principal: Principal,
    course_id: str,
    settings: Settings | None = None,
) -> RetrievalResponse:
    active = settings or get_settings()
    task = _celery_client().send_task(
        "chiron.adaptive_retrieve",
        kwargs={
            "query": query,
            "tenant_id": str(principal.tenant_id),
            "course_id": course_id,
            "route": route_query(query),
            "direct_candidate_limit": active.retrieval_direct_candidate_limit,
            "direct_limit": active.retrieval_limit,
            "multi_hop_candidate_limit": active.retrieval_multi_hop_candidate_limit,
            "multi_hop_limit": active.retrieval_multi_hop_limit,
            "max_subqueries": active.retrieval_max_subqueries,
        },
    )
    try:
        result = task.get(timeout=active.retrieval_task_timeout_seconds)
    except (CeleryTimeoutError, CeleryError, OSError) as exc:
        raise RetrievalUnavailableError("Hybrid retrieval worker is unavailable") from exc
    finally:
        task.forget()
    if not isinstance(result, dict):
        raise RetrievalUnavailableError("Hybrid retrieval returned an invalid response")
    return response_from_task(query, result)
