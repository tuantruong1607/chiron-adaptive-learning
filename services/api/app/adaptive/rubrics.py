from __future__ import annotations

from dataclasses import dataclass

from .essay_judge import Criterion


@dataclass(frozen=True, slots=True)
class VersionedRubric:
    id: str
    title: str
    criteria: tuple[Criterion, ...]

    def as_payload(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "criteria": [
                {
                    "id": criterion.id,
                    "label": criterion.label,
                    "max_score": criterion.max_score,
                    "observable_evidence": list(criterion.observable_evidence),
                }
                for criterion in self.criteria
            ],
        }


RUBRICS: dict[str, VersionedRubric] = {
    "system-design-v1": VersionedRubric(
        id="system-design-v1",
        title="Grounded RAG system design",
        criteria=(
            Criterion(
                "grounding",
                "Grounding and provenance",
                4,
                ("source span", "citation", "evidence", "locator"),
            ),
            Criterion(
                "reasoning",
                "Technical reasoning",
                4,
                ("trade-off", "latency", "precision", "recall", "isolation"),
            ),
            Criterion(
                "transfer",
                "Transfer to the scenario",
                2,
                ("recommend", "scenario", "failure", "monitor"),
            ),
        ),
    ),
}


def get_rubric(rubric_id: str) -> VersionedRubric:
    try:
        return RUBRICS[rubric_id]
    except KeyError as exc:
        raise ValueError(f"Unknown rubric version: {rubric_id}") from exc
