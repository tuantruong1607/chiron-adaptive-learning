from __future__ import annotations

import math
import re
from dataclasses import dataclass

CHUNKER_VERSION = "hierarchical-boundary-v1"


@dataclass(frozen=True, slots=True)
class ChunkDraft:
    chunk_type: str
    ordinal: int
    content: str
    token_count: int


def estimate_tokens(text: str) -> int:
    """Conservative multilingual estimate used for deterministic local chunking."""
    return max(1, math.ceil(len(text) / 3.5)) if text.strip() else 0


def _sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?。！？])\s+|\n(?=[A-ZÀ-Ỹ0-9■●•▪□✓✔-])", text.strip())
    return [re.sub(r"[ \t]+", " ", part).strip() for part in parts if part.strip()]


def _split_oversize(text: str, max_tokens: int) -> list[str]:
    max_chars = max_tokens * 3
    if estimate_tokens(text) <= max_tokens:
        return [text]
    words = text.split()
    if len(words) <= 1:
        return [text[index : index + max_chars] for index in range(0, len(text), max_chars)]
    pieces, current = [], []
    for word in words:
        candidate = " ".join([*current, word])
        if current and estimate_tokens(candidate) > max_tokens:
            pieces.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        pieces.append(" ".join(current))
    return pieces


def semantic_units(text: str, max_tokens: int) -> list[str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", normalized) if part.strip()]
    if not paragraphs:
        paragraphs = [line.strip() for line in normalized.splitlines() if line.strip()]
    units = []
    for paragraph in paragraphs:
        candidates = [paragraph]
        if estimate_tokens(paragraph) > max_tokens:
            candidates = _sentences(paragraph)
        for candidate in candidates:
            units.extend(_split_oversize(candidate, max_tokens))
    return units


def child_chunks(
    text: str,
    target_tokens: int = 500,
    max_tokens: int = 700,
    overlap_tokens: int = 80,
) -> list[str]:
    if not text.strip():
        return []
    if not 0 <= overlap_tokens < target_tokens <= max_tokens:
        raise ValueError("Require 0 <= overlap < target <= max tokens")
    units = semantic_units(text, max_tokens)
    packed, current = [], []
    for unit in units:
        candidate = "\n\n".join([*current, unit])
        if current and estimate_tokens(candidate) > target_tokens:
            packed.append("\n\n".join(current).strip())
            overlap, count = [], 0
            for previous in reversed(current):
                overlap.insert(0, previous)
                count += estimate_tokens(previous)
                if count >= overlap_tokens:
                    break
            current = overlap
            while current and estimate_tokens("\n\n".join([*current, unit])) > max_tokens:
                current.pop(0)
        current.append(unit)
    if current:
        final = "\n\n".join(current).strip()
        if not packed or final != packed[-1]:
            packed.append(final)
    return packed


def hierarchical_chunks(
    text: str,
    target_tokens: int = 500,
    max_tokens: int = 700,
    overlap_tokens: int = 80,
) -> list[ChunkDraft]:
    normalized = text.strip()
    if not normalized:
        return []
    drafts = [ChunkDraft("parent", 0, normalized, estimate_tokens(normalized))]
    drafts.extend(
        ChunkDraft("child", ordinal, content, estimate_tokens(content))
        for ordinal, content in enumerate(
            child_chunks(normalized, target_tokens, max_tokens, overlap_tokens), start=1
        )
    )
    return drafts
