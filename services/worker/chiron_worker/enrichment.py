from __future__ import annotations

import re
from dataclasses import dataclass
from hashlib import sha256
from math import sqrt
from typing import Any, Literal

EnrichmentVariant = Literal["context", "context_terms", "context_terms_pedagogy"]

ENRICHMENT_VERSION = "deterministic-context-terms-v2"
MAX_RETRIEVAL_TOKENS = 500
MAX_HEADER_TOKENS = 64

_SPACE = re.compile(r"\s+")
_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_ACRONYM = re.compile(r"(?<![\w])(?:[A-Z][A-Z0-9+#.-]{1,11})(?![\w])")

# Curated, deterministic aliases. A pair is added only when one side occurs in
# the raw chunk or its trusted document/section context.
_ALIASES: tuple[tuple[str, str], ...] = (
    ("retrieval augmented generation", "RAG"),
    ("large language model", "LLM"),
    ("reciprocal rank fusion", "RRF"),
    ("reinforcement learning from human feedback", "RLHF"),
    ("mixture of experts", "MoE"),
    ("model context protocol", "MCP"),
    ("application programming interface", "API"),
    ("continuous integration", "CI"),
    ("continuous delivery", "CD"),
    ("continuous deployment", "CD"),
    ("retrieval", "truy xuất"),
    ("embedding", "vector biểu diễn"),
    ("reranking", "xếp hạng lại"),
    ("chunking", "chia đoạn"),
    ("hallucination", "ảo giác"),
    ("fine-tuning", "tinh chỉnh mô hình"),
    ("prompt injection", "chèn chỉ dẫn độc hại"),
    ("circuit breaker", "bộ ngắt mạch"),
    ("rate limit", "giới hạn tốc độ"),
    ("feature store", "kho đặc trưng"),
    ("vector store", "cơ sở dữ liệu vector"),
)

_PEDAGOGY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("definition", ("là gì", "định nghĩa", "được gọi là", " là ")),
    ("comparison", ("so với", "khác nhau", "khác với", " vs ", "versus")),
    ("prerequisite", ("điều kiện tiên quyết", "prerequisite", "trước khi", "cần có")),
    ("mechanism", ("cơ chế", "hoạt động", "bên trong", "quy trình", "pipeline")),
    ("application", ("ứng dụng", "áp dụng", "use case", "khi nào dùng", "dùng cho")),
    ("limitation", ("hạn chế", "không phù hợp", "trade-off", "đánh đổi", "nhược điểm")),
    ("misconception", ("hiểu lầm", "misconception", "sai lầm", "không phải")),
    ("example", ("ví dụ", "example", "chẳng hạn")),
    ("evaluation", ("đánh giá", "metric", "đo lường", "benchmark")),
)


@dataclass(frozen=True, slots=True)
class EnrichmentResult:
    raw_content: str
    retrieval_text: str
    raw_checksum: str
    retrieval_text_checksum: str
    enrichment_version: str
    variant: EnrichmentVariant
    aliases: tuple[str, ...]
    entities: tuple[str, ...]
    pedagogy_labels: tuple[str, ...]
    provenance: tuple[str, ...]
    contextualized: bool
    estimated_header_tokens: int
    estimated_retrieval_tokens: int
    context_text: str


def validate_enriched_payload(payload: dict[str, Any], expected: dict[str, Any]) -> list[str]:
    """Return integrity violations without trusting enriched retrieval text as citation data."""
    errors: list[str] = []
    for key in ("tenant_id", "course_id", "source_span_id"):
        if str(payload.get(key)) != str(expected.get(key)):
            errors.append(f"{key}_mismatch")
    if payload.get("content") != expected.get("content"):
        errors.append("raw_content_mismatch")
    if payload.get("raw_checksum") != expected.get("checksum"):
        errors.append("raw_checksum_mismatch")
    retrieval_text_checksum = payload.get("retrieval_text_checksum")
    if not retrieval_text_checksum:
        errors.append("missing_retrieval_text_checksum")
    elif expected.get("retrieval_text_checksum"):
        if retrieval_text_checksum != expected["retrieval_text_checksum"]:
            errors.append("retrieval_text_checksum_mismatch")
    else:
        retrieval_text = payload.get("retrieval_text")
        if (
            not isinstance(retrieval_text, str)
            or retrieval_text_checksum != sha256(retrieval_text.encode()).hexdigest()
        ):
            errors.append("retrieval_text_checksum_mismatch")
    if not payload.get("enrichment_version"):
        errors.append("missing_enrichment_version")
    if not payload.get("enrichment_provenance"):
        errors.append("missing_enrichment_provenance")
    return errors


def blend_dense_vectors(raw: list[float], context: list[float], context_weight: float) -> list[float]:
    if not 0.0 <= context_weight <= 1.0:
        raise ValueError("context_weight must be between 0 and 1")
    if not raw or len(raw) != len(context):
        raise ValueError("raw and context vectors must have the same non-zero dimensions")
    mixed = [
        (1.0 - context_weight) * raw_value + context_weight * context_value
        for raw_value, context_value in zip(raw, context, strict=True)
    ]
    norm = sqrt(sum(value * value for value in mixed))
    if norm == 0:
        raise ValueError("blended vector has zero norm")
    return [value / norm for value in mixed]


def _clean(value: Any, max_chars: int) -> str:
    text = _CONTROL.sub(" ", str(value or ""))
    text = _SPACE.sub(" ", text).strip()
    return text[:max_chars].rstrip()


def _estimate_tokens(value: str) -> int:
    return max(1, round(len(value) / 3.5)) if value.strip() else 0


def _budgeted_header(lines: list[str], token_budget: int) -> list[str]:
    selected: list[str] = []
    used = 0
    for line in lines:
        cost = _estimate_tokens(line)
        if used + cost <= token_budget:
            selected.append(line)
            used += cost
    return selected


def _locator_context(locator: dict[str, Any]) -> tuple[str, str]:
    section = _clean(locator.get("section_title") or locator.get("heading"), 240)
    label = _clean(locator.get("label"), 80)
    if not label and locator.get("page") is not None:
        label = f"Page {locator['page']}"
    return section, label


def _contains(haystack: str, needle: str) -> bool:
    return re.search(rf"(?<!\w){re.escape(needle)}(?!\w)", haystack, re.IGNORECASE) is not None


def _aliases_and_entities(context: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    aliases: list[str] = []
    for left, right in _ALIASES:
        if _contains(context, left) or _contains(context, right):
            aliases.append(f"{left} = {right}")
    entities = sorted(set(_ACRONYM.findall(context)), key=lambda value: (len(value), value))
    return tuple(aliases[:12]), tuple(entities[:16])


def _pedagogy_labels(content: str) -> tuple[str, ...]:
    normalized = f" {_clean(content, 20_000).lower()} "
    labels = [label for label, markers in _PEDAGOGY_RULES if any(m in normalized for m in markers)]
    return tuple(labels[:6])


def enrich_chunk(
    chunk: dict[str, Any],
    *,
    variant: EnrichmentVariant = "context_terms_pedagogy",
) -> EnrichmentResult:
    """Build deterministic retrieval text while preserving the citation source verbatim."""
    if variant not in {"context", "context_terms", "context_terms_pedagogy"}:
        raise ValueError(f"Unsupported enrichment variant: {variant}")

    raw_content = str(chunk.get("content") or "")
    locator = chunk.get("locator") if isinstance(chunk.get("locator"), dict) else {}
    course_title = _clean(chunk.get("course_title"), 160)
    document_title = _clean(chunk.get("document_title"), 240)
    source_type = _clean(chunk.get("source_type"), 40)
    section, label = _locator_context(locator)

    context_parts = [part for part in (document_title, section, raw_content) if part]
    searchable_context = "\n".join(context_parts)
    aliases: tuple[str, ...] = ()
    entities: tuple[str, ...] = ()
    labels: tuple[str, ...] = ()
    provenance = ["document_versions.title", "source_spans.locator"]
    if variant in {"context_terms", "context_terms_pedagogy"}:
        aliases, entities = _aliases_and_entities(searchable_context)
        provenance.extend(("curated_alias_glossary_v1", "deterministic_acronym_regex_v1"))
    if variant == "context_terms_pedagogy":
        labels = _pedagogy_labels(raw_content)
        provenance.append("deterministic_pedagogy_rules_v1")

    header_candidates: list[str] = []
    document_context = " | ".join(part for part in (document_title, source_type) if part)
    section_context = " > ".join(part for part in (section, label) if part)
    if section_context:
        header_candidates.append(f"[SECTION] {section_context}")
    if document_context:
        header_candidates.append(f"[DOCUMENT] {document_context}")
    if aliases:
        header_candidates.append(f"[ALIASES] {'; '.join(aliases)}")
    if entities:
        header_candidates.append(f"[ENTITIES] {', '.join(entities)}")
    if labels:
        header_candidates.append(f"[PEDAGOGY] {', '.join(labels)}")
    if course_title:
        header_candidates.append(f"[COURSE] {course_title}")

    raw_token_estimate = max(
        int(chunk.get("token_count") or 0),
        _estimate_tokens(raw_content),
    )
    header_budget = min(MAX_HEADER_TOKENS, max(0, MAX_RETRIEVAL_TOKENS - raw_token_estimate))
    header = _budgeted_header(header_candidates, header_budget)
    estimated_header_tokens = sum(_estimate_tokens(line) for line in header)
    retrieval_text = (
        "\n".join([*header, "[CONTENT]", raw_content]).strip() if header else raw_content
    )

    raw_checksum = str(chunk.get("checksum") or sha256(raw_content.encode()).hexdigest())
    return EnrichmentResult(
        raw_content=raw_content,
        retrieval_text=retrieval_text,
        raw_checksum=raw_checksum,
        retrieval_text_checksum=sha256(retrieval_text.encode()).hexdigest(),
        enrichment_version=ENRICHMENT_VERSION,
        variant=variant,
        aliases=aliases,
        entities=entities,
        pedagogy_labels=labels,
        provenance=tuple(provenance),
        contextualized=bool(header),
        estimated_header_tokens=estimated_header_tokens,
        estimated_retrieval_tokens=raw_token_estimate + estimated_header_tokens,
        context_text="\n".join(header),
    )
