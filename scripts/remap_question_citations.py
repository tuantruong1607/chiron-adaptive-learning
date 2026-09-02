"""Fail-closed remapper for Markdown question-bank citations.

Evidence lines must use ``title — slide N``. Existing UUIDs are replaced only
when the exact document title and page resolve to one manifest source span.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "data" / "manifests" / "corpus.json"
DEFAULT_SPANS = ROOT / "data" / "manifests" / "source_spans.jsonl"
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
EVIDENCE = re.compile(
    rf"(?m)^(\*\*Evidence:\*\*\s*)`{UUID}`\s+—\s+\*([^*]+)\*,\s+slide\s+(\d+)\.$"
)


def build_index(corpus_path: Path, spans_path: Path) -> dict[tuple[str, int], str]:
    corpus = json.loads(corpus_path.read_text(encoding="utf-8"))
    titles = {item["document_version_id"]: item["title"] for item in corpus["documents"]}
    index: dict[tuple[str, int], str] = {}
    for line in spans_path.read_text(encoding="utf-8").splitlines():
        span = json.loads(line)
        page = span.get("locator", {}).get("page")
        title = titles.get(span["document_version_id"])
        if isinstance(page, int) and title:
            key = (title, page)
            if key in index:
                raise RuntimeError(f"Ambiguous span mapping: {title!r} slide {page}")
            index[key] = span["source_span_id"]
    return index


def remap(markdown: str, index: dict[tuple[str, int], str]) -> tuple[str, int]:
    misses: list[str] = []

    def replace(match: re.Match[str]) -> str:
        prefix, title, page = match.groups()
        source_span_id = index.get((title, int(page)))
        if source_span_id is None:
            misses.append(f"{title} — slide {page}")
            return match.group(0)
        return f"{prefix}`{source_span_id}` — *{title}*, slide {page}."

    updated, count = EVIDENCE.subn(replace, markdown)
    if misses:
        raise RuntimeError("Unresolved citations:\n- " + "\n- ".join(sorted(set(misses))))
    return updated, count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--spans", type=Path, default=DEFAULT_SPANS)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    original = args.markdown.read_text(encoding="utf-8")
    updated, count = remap(original, build_index(args.corpus, args.spans))
    if not count:
        raise RuntimeError("No page-based evidence lines found")
    if not args.check:
        args.markdown.write_text(updated, encoding="utf-8")
    print(json.dumps({"remapped": count, "check_only": args.check, "path": str(args.markdown)}))


if __name__ == "__main__":
    main()
