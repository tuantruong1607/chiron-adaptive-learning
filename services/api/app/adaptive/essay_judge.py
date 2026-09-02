"""Rubric-bound LLM-as-Judge for constructed responses.

The judge cannot invent a rubric or silently pass malformed output.  Its result
is an auditable scoring artifact; callers persist it beside the attempt.
"""
from __future__ import annotations

import json
from dataclasses import dataclass

from ..llm.router import LLMRouter
from ..llm.types import DataSensitivity, LLMRequest, RequestPriority, Workload


@dataclass(frozen=True)
class Criterion:
    id: str
    label: str
    max_score: int
    observable_evidence: tuple[str, ...]


@dataclass(frozen=True)
class EssayJudgement:
    criterion_scores: dict[str, int]
    total_score: int
    max_score: int
    feedback: str
    confidence: float
    provider: str
    model: str


class EssayJudge:
    def __init__(self, router: LLMRouter) -> None:
        self.router = router

    async def grade(self, *, prompt: str, answer: str, rubric: tuple[Criterion, ...]) -> EssayJudgement:
        if not answer.strip() or not rubric:
            raise ValueError("Answer and versioned rubric are required")
        rubric_json = [
            {"id": item.id, "label": item.label, "max_score": item.max_score,
             "observable_evidence": item.observable_evidence}
            for item in rubric
        ]
        result = await self.router.complete(LLMRequest(
            workload=Workload.GRADER, sensitivity=DataSensitivity.PRIVATE,
            priority=RequestPriority.ASYNC_HIGH, temperature=0.0, max_tokens=900,
            system_prompt=("You grade Vietnamese constructed responses only against the supplied versioned rubric. "
                           "Do not reward unsupported claims. Return JSON only: criterion_scores object, "
                           "feedback string, confidence number from 0 to 1."),
            user_prompt=json.dumps({"prompt": prompt, "answer": answer, "rubric": rubric_json}, ensure_ascii=False),
        ))
        try:
            content = result.content.strip()
            if content.startswith("```json"):
                content = content[7:]
            elif content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            content = content.strip()
            payload = json.loads(content)
            raw_scores = payload["criterion_scores"]
            scores = {item.id: int(raw_scores[item.id]) for item in rubric}
            confidence = float(payload["confidence"])
            feedback = str(payload["feedback"]).strip()
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            raise ValueError("LLM judge returned invalid rubric JSON") from exc
        if any(score < 0 or score > item.max_score for item, score in ((item, scores[item.id]) for item in rubric)):
            raise ValueError("LLM judge produced a score outside the rubric range")
        if not 0 <= confidence <= 1 or not feedback:
            raise ValueError("LLM judge produced invalid confidence or feedback")
        return EssayJudgement(scores, sum(scores.values()), sum(item.max_score for item in rubric), feedback, confidence, result.provider, result.model)


def deterministic_grade(
    *, prompt: str, answer: str, rubric: tuple[Criterion, ...]
) -> EssayJudgement:
    """Deterministic development grader used when no external provider is configured."""
    del prompt
    normalized = answer.casefold()
    words = len(answer.split())
    coverage = min(1.0, words / 120)
    scores: dict[str, int] = {}
    for criterion in rubric:
        evidence = sum(term.casefold() in normalized for term in criterion.observable_evidence)
        evidence_ratio = min(1.0, evidence / max(1, min(3, len(criterion.observable_evidence))))
        score = round(criterion.max_score * max(coverage * 0.55, evidence_ratio))
        scores[criterion.id] = min(criterion.max_score, score)
    total = sum(scores.values())
    confidence = round(min(0.75, 0.35 + coverage * 0.25 + (0.15 if total else 0)), 3)
    return EssayJudgement(
        criterion_scores=scores,
        total_score=total,
        max_score=sum(item.max_score for item in rubric),
        feedback="Development-mode deterministic grading; review the evidence before release.",
        confidence=confidence,
        provider="mock",
        model="deterministic-rubric-v1",
    )
