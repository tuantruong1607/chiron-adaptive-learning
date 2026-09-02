"""Export the reviewed Markdown bank to runtime-safe assessment JSON files.

The Markdown remains the authoring source of truth. This exporter only performs
a deterministic format conversion; it never calls an LLM.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from validate_question_bank import parse


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "questions" / "review" / "question-bank-v1.md"
REVIEW = ROOT / "data" / "questions" / "review" / "question-bank-v1-review.json"
TARGETS = (
    ROOT / "apps" / "web" / "lib" / "generated-question-bank.json",
    ROOT / "services" / "api" / "app" / "generated_question_bank.json",
)

ANSWER = re.compile(r"^\*\*Đáp án:\*\* ([A-D])\. (.*?)(?=\n\*\*Evidence:)", re.M | re.S)
RUBRIC = re.compile(r"^\*\*Rubric:\*\* (.+?)[ \t]*$", re.M)
REFERENCE = re.compile(
    r"^\*\*Đáp án tham chiếu ngắn gọn:\*\* (.+?)(?=\n\n\*\*|\n\n---|\Z)",
    re.M | re.S,
)


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def prompt_between_metadata_and(body: str, marker: str) -> str:
    metadata_end = body.find("\n", body.find("**Metadata:**"))
    marker_start = body.find(marker, metadata_end)
    return clean(body[metadata_end:marker_start])


def main() -> None:
    items = parse(SOURCE.read_text(encoding="utf-8"))
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    default = review["default_decision"]
    exported: list[dict] = []

    for item in items:
        lines = item.body.strip().splitlines()
        title = lines[0].strip(" —-")
        decision = review.get("exceptions", {}).get(str(item.number), default)
        base = {
            "id": f"qb-{item.number:03d}",
            "number": item.number,
            "title": title,
            "topic": item.meta.get("topic", "general"),
            "difficulty": item.meta.get("difficulty", "medium"),
            "cognitiveLevel": item.meta.get("cognitive_level", "understand"),
            "reviewDecision": decision["decision"],
            "evidenceIds": item.span_ids,
        }
        if item.number <= 90:
            answer = ANSWER.search(item.body)
            if answer is None:
                raise RuntimeError(f"Q{item.number} is missing a parseable answer")
            exported.append(
                {
                    **base,
                    "kind": "objective",
                    "prompt": prompt_between_metadata_and(item.body, "\n- A."),
                    "options": [
                        {"id": label.lower(), "text": clean(text)}
                        for label, text in item.options
                    ],
                    "answerKey": answer.group(1).lower(),
                    "explanation": clean(answer.group(2)),
                }
            )
            continue

        rubric = RUBRIC.search(item.body)
        if rubric is None:
            raise RuntimeError(f"Q{item.number} is missing a parseable rubric")
        reference = REFERENCE.search(item.body)
        exported.append(
            {
                **base,
                "kind": "constructed",
                "prompt": prompt_between_metadata_and(item.body, "\n**Rubric:**"),
                "rubric": clean(rubric.group(1)),
                "referenceAnswer": clean(reference.group(1)) if reference else "",
            }
        )

    if [item["number"] for item in exported] != list(range(1, 101)):
        raise RuntimeError("Assessment export must contain Q1 through Q100")

    payload = json.dumps(exported, ensure_ascii=False, indent=2) + "\n"
    for target in TARGETS:
        target.write_text(payload, encoding="utf-8")
        print(f"wrote {len(exported)} questions to {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
