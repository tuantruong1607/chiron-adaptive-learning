from datetime import date

from app.adaptive.contracts import (
    DiagnosticStatus,
    EvidenceSignal,
    KnowledgeState,
    LearningUnit,
    PriorityDecision,
)
from app.adaptive.mastery import update_knowledge_state
from app.adaptive.planner import build_cram_plan
from app.adaptive.priority import rank_learning_units


def unverified_state(concept_id: str, self_confidence: float = 0.8) -> KnowledgeState:
    return KnowledgeState(concept_id=concept_id, self_confidence=self_confidence)


def measured_state(concept_id: str, mastery: float) -> KnowledgeState:
    return KnowledgeState(
        concept_id=concept_id,
        self_confidence=0.8,
        diagnostic_status=DiagnosticStatus.PARTIAL,
        mastery=mastery,
        evidence_confidence=0.7,
        confidence_gap=0.8 - mastery,
        evidence_ids=(f"seed-{concept_id}",),
    )


def test_mastery_is_not_fabricated_without_evidence() -> None:
    state = unverified_state("rrf")

    updated = update_knowledge_state(state, [])

    assert updated is state
    assert updated.mastery is None
    assert updated.diagnostic_status is DiagnosticStatus.NOT_ASSESSED


def test_evidence_updates_mastery_confidence_and_status() -> None:
    state = unverified_state("rrf")
    first = EvidenceSignal("e1", "rrf", 1, 0.9, "diagnostic_mcq")
    second = EvidenceSignal("e2", "rrf", 0.5, 0.95, "explain_back")

    partial = update_knowledge_state(state, [first])
    verified = update_knowledge_state(partial, [second])

    assert partial.diagnostic_status is DiagnosticStatus.PARTIAL
    assert verified.diagnostic_status is DiagnosticStatus.VERIFIED
    assert verified.mastery is not None
    assert 0.5 < verified.mastery < 1
    assert verified.evidence_confidence is not None
    assert verified.evidence_confidence >= 0.8
    assert verified.evidence_ids == ("e1", "e2")


def test_need_importance_urgency_ranking_is_deterministic_and_auditable() -> None:
    units = [
        LearningUnit("weak", "Weak", 0.9, measured_state("weak", 0.2), 30),
        LearningUnit("strong", "Strong", 0.7, measured_state("strong", 0.85), 20),
    ]

    ranked = rank_learning_units(
        units,
        exam_date=date(2026, 9, 3),
        evaluated_on=date(2026, 8, 30),
    )

    assert [item.concept_id for item in ranked] == ["weak", "strong"]
    assert [item.rank for item in ranked] == [1, 2]
    assert ranked[0].score > ranked[1].score
    assert ranked[0].need > ranked[1].need
    assert len(ranked[0].reasons) >= 3


def priority(concept_id: str, rank: int, score: float = 0.8) -> PriorityDecision:
    return PriorityDecision(
        concept_id=concept_id,
        title=concept_id.title(),
        need=score,
        importance=0.8,
        urgency=0.7,
        score=score,
        reliability=0.7,
        estimated_minutes=30,
        rank=rank,
    )


def test_planner_honors_prerequisites_and_reports_capacity_deferral() -> None:
    priorities = [
        priority("target", 1, 0.9),
        priority("foundation", 2, 0.7),
        priority("extra-a", 3, 0.6),
        priority("extra-b", 4, 0.5),
    ]
    states = {item.concept_id: measured_state(item.concept_id, 0.4) for item in priorities}

    plan = build_cram_plan(
        priorities,
        states,
        [("foundation", "target")],
        horizon_days=3,
        daily_minutes=30,
    )

    assert [item.concept_id for item in plan.scheduled[:2]] == ["foundation", "target"]
    assert [item.day_offset for item in plan.scheduled] == [0, 1, 2]
    assert [item.concept_id for item in plan.deferred] == ["extra-b"]
    assert plan.component_scores["target"]["priority"] == 0.9
