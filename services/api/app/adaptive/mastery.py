from __future__ import annotations

from math import prod

from .contracts import DiagnosticStatus, EvidenceSignal, KnowledgeState

EVIDENCE_TYPE_RELIABILITY: dict[str, float] = {
    "diagnostic_mcq": 0.72,
    "short_answer": 0.82,
    "explain_back": 0.9,
    "essay": 0.88,
    "lab": 0.78,
    "transfer_check": 0.92,
    "delayed_recheck": 1.0,
}


def _effective_weight(evidence: EvidenceSignal) -> float:
    type_weight = EVIDENCE_TYPE_RELIABILITY.get(evidence.evidence_type, 0.65)
    return evidence.confidence * type_weight


def update_knowledge_state(
    previous: KnowledgeState,
    evidence: list[EvidenceSignal],
) -> KnowledgeState:
    """Update mastery from auditable evidence without inventing missing measurements.

    The existing mastery is treated as a prior only when the previous state was already
    measured. An unverified self-report never becomes a numeric mastery by itself.
    """
    relevant = [item for item in evidence if item.concept_id == previous.concept_id]
    if not relevant:
        return previous

    weights = [_effective_weight(item) for item in relevant]
    evidence_weight = sum(weights)
    if evidence_weight <= 0:
        return previous

    numerator = sum(item.value * weight for item, weight in zip(relevant, weights, strict=True))
    denominator = evidence_weight

    if previous.mastery is not None and previous.evidence_confidence is not None:
        prior_weight = max(0.25, previous.evidence_confidence)
        numerator += previous.mastery * prior_weight
        denominator += prior_weight

    mastery = min(max(numerator / denominator, 0.0), 1.0)
    combined_confidence = 1 - prod(1 - min(weight, 0.95) for weight in weights)
    if previous.evidence_confidence is not None:
        combined_confidence = 1 - ((1 - combined_confidence) * (1 - previous.evidence_confidence))
    combined_confidence = min(max(combined_confidence, 0.0), 1.0)

    unique_ids = tuple(
        dict.fromkeys((*previous.evidence_ids, *(item.evidence_id for item in relevant)))
    )
    status = (
        DiagnosticStatus.VERIFIED
        if combined_confidence >= 0.8 and len(unique_ids) >= 2
        else DiagnosticStatus.PARTIAL
    )
    return KnowledgeState(
        concept_id=previous.concept_id,
        self_confidence=previous.self_confidence,
        diagnostic_status=status,
        mastery=round(mastery, 4),
        evidence_confidence=round(combined_confidence, 4),
        confidence_gap=round(previous.self_confidence - mastery, 4),
        misconception=previous.misconception or any(item.misconception for item in relevant),
        evidence_ids=unique_ids,
        version=previous.version,
    )
