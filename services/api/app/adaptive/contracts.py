from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class DiagnosticStatus(StrEnum):
    NOT_ASSESSED = "not_assessed"
    UNVERIFIED = "unverified"
    PARTIAL = "partial"
    VERIFIED = "verified"


@dataclass(frozen=True, slots=True)
class EvidenceSignal:
    evidence_id: str
    concept_id: str
    value: float
    confidence: float
    evidence_type: str
    misconception: bool = False

    def __post_init__(self) -> None:
        if not 0 <= self.value <= 1:
            raise ValueError("evidence value must be within [0, 1]")
        if not 0 <= self.confidence <= 1:
            raise ValueError("evidence confidence must be within [0, 1]")


@dataclass(frozen=True, slots=True)
class KnowledgeState:
    concept_id: str
    self_confidence: float
    diagnostic_status: DiagnosticStatus = DiagnosticStatus.NOT_ASSESSED
    mastery: float | None = None
    evidence_confidence: float | None = None
    confidence_gap: float | None = None
    misconception: bool = False
    evidence_ids: tuple[str, ...] = ()
    version: str = "adaptive-v1"

    def __post_init__(self) -> None:
        if not 0 <= self.self_confidence <= 1:
            raise ValueError("self confidence must be within [0, 1]")
        for name, value in (
            ("mastery", self.mastery),
            ("evidence_confidence", self.evidence_confidence),
        ):
            if value is not None and not 0 <= value <= 1:
                raise ValueError(f"{name} must be within [0, 1]")
        has_diagnostic = self.diagnostic_status in {
            DiagnosticStatus.PARTIAL,
            DiagnosticStatus.VERIFIED,
        }
        if has_diagnostic and (self.mastery is None or self.evidence_confidence is None):
            raise ValueError("partial/verified state requires mastery and evidence confidence")
        if not has_diagnostic and (
            self.mastery is not None
            or self.evidence_confidence is not None
            or self.confidence_gap is not None
        ):
            raise ValueError("unassessed/unverified state cannot fabricate diagnostic values")


@dataclass(frozen=True, slots=True)
class LearningUnit:
    concept_id: str
    title: str
    exam_weight: float
    state: KnowledgeState
    estimated_minutes: int = 30


@dataclass(frozen=True, slots=True)
class PriorityDecision:
    concept_id: str
    title: str
    need: float
    importance: float
    urgency: float
    score: float
    reliability: float
    estimated_minutes: int
    reasons: tuple[str, ...] = ()
    rank: int | None = None
    missing_signals: tuple[str, ...] = ()
    version: str = "niu-v1"


@dataclass(frozen=True, slots=True)
class ScheduledLearningItem:
    concept_id: str
    title: str
    activity: str
    duration_minutes: int
    day_offset: int
    priority_rank: int
    priority_score: float
    expected_gain: float
    reason: str


@dataclass(frozen=True, slots=True)
class DeferredLearningItem:
    concept_id: str
    title: str
    duration_minutes: int
    reason: str


@dataclass(frozen=True, slots=True)
class PlanDecision:
    horizon_days: int
    daily_minutes: int
    scheduled: tuple[ScheduledLearningItem, ...] = ()
    deferred: tuple[DeferredLearningItem, ...] = ()
    component_scores: dict[str, dict[str, float]] = field(default_factory=dict)
    version: str = "cram-planner-v1"
