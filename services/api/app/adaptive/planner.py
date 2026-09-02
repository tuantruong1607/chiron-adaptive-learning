from __future__ import annotations

from .contracts import (
    DeferredLearningItem,
    KnowledgeState,
    PlanDecision,
    PriorityDecision,
    ScheduledLearningItem,
)


def _activity_for(state: KnowledgeState) -> str:
    if state.misconception:
        return "lesson"
    if state.mastery is None or state.mastery < 0.4:
        return "lesson"
    if state.mastery < 0.7:
        return "retrieval"
    return "recheck"


def _ordered_with_prerequisites(
    priorities: list[PriorityDecision], prerequisite_edges: list[tuple[str, str]]
) -> list[PriorityDecision]:
    by_id = {item.concept_id: item for item in priorities}
    prerequisites: dict[str, list[str]] = {}
    for source, target in prerequisite_edges:
        if source in by_id and target in by_id and source != target:
            prerequisites.setdefault(target, []).append(source)

    ordered: list[PriorityDecision] = []
    visiting: set[str] = set()
    placed: set[str] = set()

    def place(concept_id: str) -> None:
        if concept_id in placed or concept_id in visiting:
            return
        visiting.add(concept_id)
        for prerequisite_id in prerequisites.get(concept_id, []):
            place(prerequisite_id)
        visiting.remove(concept_id)
        placed.add(concept_id)
        ordered.append(by_id[concept_id])

    for priority in priorities:
        place(priority.concept_id)
    return ordered


def build_cram_plan(
    priorities: list[PriorityDecision],
    states: dict[str, KnowledgeState],
    prerequisite_edges: list[tuple[str, str]],
    *,
    horizon_days: int = 4,
    daily_minutes: int = 120,
) -> PlanDecision:
    if horizon_days not in {3, 4}:
        raise ValueError("cram plan horizon must be 3 or 4 days")
    if not 30 <= daily_minutes <= 480:
        raise ValueError("daily minutes must be within [30, 480]")

    ordered = _ordered_with_prerequisites(priorities, prerequisite_edges)
    scheduled: list[ScheduledLearningItem] = []
    deferred: list[DeferredLearningItem] = []
    day_offset = 0
    used_minutes = 0

    for priority in ordered:
        duration = priority.estimated_minutes
        if used_minutes + duration > daily_minutes:
            day_offset += 1
            used_minutes = 0
        if day_offset >= horizon_days:
            deferred.append(
                DeferredLearningItem(
                    concept_id=priority.concept_id,
                    title=priority.title,
                    duration_minutes=duration,
                    reason="Không đủ capacity trong cửa sổ ôn thi",
                )
            )
            continue

        state = states[priority.concept_id]
        mastery = state.mastery if state.mastery is not None else state.self_confidence
        expected_gain = min((1 - mastery) * priority.importance * 0.25, 0.25)
        scheduled.append(
            ScheduledLearningItem(
                concept_id=priority.concept_id,
                title=priority.title,
                activity=_activity_for(state),
                duration_minutes=duration,
                day_offset=day_offset,
                priority_rank=priority.rank or 0,
                priority_score=priority.score,
                expected_gain=round(expected_gain, 3),
                reason="; ".join(priority.reasons),
            )
        )
        used_minutes += duration

    return PlanDecision(
        horizon_days=horizon_days,
        daily_minutes=daily_minutes,
        scheduled=tuple(scheduled),
        deferred=tuple(deferred),
        component_scores={
            item.concept_id: {
                "need": item.need,
                "importance": item.importance,
                "urgency": item.urgency,
                "priority": item.score,
                "reliability": item.reliability,
            }
            for item in priorities
        },
    )
