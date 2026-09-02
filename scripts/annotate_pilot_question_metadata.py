"""Inject review metadata and mutually-exclusive construct groups into pilot Markdown."""
from __future__ import annotations

import re
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "data/questions/review/pilot-v1.md"
TOPICS = [
    ("chunking", "apply", "medium"), ("embedding", "understand", "easy"),
    ("dense-vs-sparse-retrieval", "analyze", "hard"), ("sparse-retrieval", "apply", "medium"),
    ("hybrid-fusion", "apply", "medium"), ("reranking", "apply", "medium"),
    ("tenant-isolation", "apply", "hard"), ("ann-indexing", "understand", "medium"),
    ("rag-offline-pipeline", "understand", "medium"), ("context-precision", "apply", "medium"),
    ("context-recall", "apply", "medium"), ("faithfulness", "apply", "medium"),
    ("answer-relevancy", "apply", "medium"), ("rag-diagnosis", "analyze", "hard"),
    ("multi-hop-retrieval", "analyze", "hard"), ("agent-idempotency", "apply", "hard"),
    ("agent-state-machine", "understand", "medium"), ("durable-checkpointing", "analyze", "hard"),
    ("human-in-the-loop", "analyze", "hard"), ("circuit-breaker", "apply", "hard"),
    ("fallback-policy", "apply", "medium"), ("agent-observability", "analyze", "hard"),
    ("sli-slo", "understand", "medium"), ("short-term-memory", "understand", "easy"),
    ("episodic-memory", "understand", "medium"), ("semantic-memory", "apply", "medium"),
    ("graphrag-traversal", "analyze", "hard"), ("retrieval-prompt-injection", "apply", "hard"),
    ("semantic-cache", "understand", "medium"), ("memory-consolidation", "analyze", "hard"),
]
MUTEX = {3: (4,), 4: (3,), 15: (27,), 27: (15,), 24: (30,), 30: (24,)}
GROUPS = {
    10: "ragas-metrics", 11: "ragas-metrics", 12: "ragas-metrics", 13: "ragas-metrics",
    24: "memory-taxonomy", 25: "memory-taxonomy", 26: "memory-taxonomy",
}
CR_METADATA = {
    31: ("agent-observability", "analyze", "hard"),
    32: ("rag-security", "analyze", "hard"),
    33: ("agent-reliability", "analyze", "hard"),
    34: ("retrieval-router", "apply", "hard"),
    35: ("fallback-governance", "analyze", "hard"),
    36: ("memory-architecture", "analyze", "hard"),
}


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    text = re.sub(r"\n> \*\*Metadata:\*\*.*?\n", "\n", text)
    def inject(match: re.Match[str]) -> str:
        number = int(match.group(1)); topic, cognitive, difficulty = TOPICS[number - 1]
        exclude = ", ".join(f"Q{item}" for item in MUTEX.get(number, ())) or "none"
        group = GROUPS.get(number, "none")
        metadata = f"\n> **Metadata:** `topic={topic}` · `cognitive_level={cognitive}` · `difficulty={difficulty}` · `group={group}` · `mutually_exclusive_with={exclude}`\n"
        return match.group(0) + metadata
    text, count = re.subn(r"^### ([1-9]|[12][0-9]|30)\..*$", inject, text, flags=re.M)
    if count != 30:
        raise RuntimeError(f"Expected 30 objective headings, got {count}")

    def inject_constructed_response(match: re.Match[str]) -> str:
        number = int(match.group(1))
        topic, cognitive, difficulty = CR_METADATA[number]
        metadata = f"\n> **Metadata:** `topic={topic}` · `cognitive_level={cognitive}` · `difficulty={difficulty}` · `assessment_type=constructed_response`\n"
        return match.group(0) + metadata

    text, constructed_count = re.subn(
        r"^### (3[1-6])\..*$", inject_constructed_response, text, flags=re.M
    )
    if constructed_count != 6:
        raise RuntimeError(f"Expected 6 constructed-response headings, got {constructed_count}")
    PATH.write_text(text, encoding="utf-8")
    print({"objective_annotated": count, "constructed_annotated": constructed_count, "groups": 2})


if __name__ == "__main__":
    main()
