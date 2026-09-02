"""Deterministic adaptive-learning core distilled from the Fidea prototype."""

from .contracts import (
    DiagnosticStatus,
    EvidenceSignal,
    KnowledgeState,
    PlanDecision,
    PriorityDecision,
)
from .mastery import update_knowledge_state
from .planner import build_cram_plan
from .priority import rank_learning_units

__all__ = [
    "DiagnosticStatus",
    "EvidenceSignal",
    "KnowledgeState",
    "PlanDecision",
    "PriorityDecision",
    "build_cram_plan",
    "rank_learning_units",
    "update_knowledge_state",
]
