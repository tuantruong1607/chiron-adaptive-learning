from __future__ import annotations

from dataclasses import replace
from datetime import date

from .contracts import DiagnosticStatus, LearningUnit, PriorityDecision

WEIGHT_NEED = 0.5
WEIGHT_IMPORTANCE = 0.3
WEIGHT_URGENCY = 0.2


def diagnostic_reliability(unit: LearningUnit) -> float:
    state = unit.state
    if state.mastery is None:
        return 0.0
    if state.diagnostic_status is DiagnosticStatus.VERIFIED:
        return 1.0
    if state.diagnostic_status is DiagnosticStatus.PARTIAL:
        return state.evidence_confidence or 0.0
    return 0.0


def urgency_score(exam_date: date, evaluated_on: date) -> float:
    days = max((exam_date - evaluated_on).days, 0)
    return round(1 / (1 + days / 7), 4)


def evaluate_learning_unit(
    unit: LearningUnit,
    *,
    exam_date: date,
    evaluated_on: date,
) -> PriorityDecision:
    reliability = diagnostic_reliability(unit)
    self_need = 1 - unit.state.self_confidence
    diagnostic_need = 1 - unit.state.mastery if unit.state.mastery is not None else None
    need = (
        reliability * diagnostic_need + (1 - reliability) * self_need
        if diagnostic_need is not None
        else self_need
    )
    importance = min(max(unit.exam_weight, 0.0), 1.0)
    urgency = urgency_score(exam_date, evaluated_on)
    score = WEIGHT_NEED * need + WEIGHT_IMPORTANCE * importance + WEIGHT_URGENCY * urgency

    reasons = [
        f"Need {need:.0%} từ self-report và diagnostic reliability {reliability:.0%}",
        f"Trọng số đề {importance:.0%}",
        f"Urgency {urgency:.0%} theo ngày thi",
    ]
    if unit.state.misconception:
        reasons.append("Có misconception cần sửa trước khi luyện chuyển giao")

    return PriorityDecision(
        concept_id=unit.concept_id,
        title=unit.title,
        need=round(need, 4),
        importance=round(importance, 4),
        urgency=urgency,
        score=round(min(max(score, 0.0), 1.0), 4),
        reliability=round(reliability, 4),
        estimated_minutes=unit.estimated_minutes,
        reasons=tuple(reasons),
    )


def rank_learning_units(
    units: list[LearningUnit],
    *,
    exam_date: date,
    evaluated_on: date,
) -> list[PriorityDecision]:
    evaluated = [
        evaluate_learning_unit(unit, exam_date=exam_date, evaluated_on=evaluated_on)
        for unit in units
    ]
    evaluated.sort(
        key=lambda item: (-item.score, -item.urgency, -item.need, -item.importance, item.concept_id)
    )
    return [replace(item, rank=rank) for rank, item in enumerate(evaluated, start=1)]
