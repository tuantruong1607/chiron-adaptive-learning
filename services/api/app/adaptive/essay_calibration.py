from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CalibrationCase:
    human_scores: dict[str, float]
    predicted_scores: dict[str, float]
    confidence: float


def summarize_calibration(cases: list[CalibrationCase], review_threshold: float = 0.65) -> dict:
    if not cases:
        raise ValueError("At least one calibration case is required")

    criterion_errors: list[float] = []
    total_errors: list[float] = []
    within_one = 0
    true_review = predicted_review = matched_review = 0

    for case in cases:
        if set(case.human_scores) != set(case.predicted_scores):
            raise ValueError("Human and predicted criteria must match")
        errors = [
            abs(case.predicted_scores[key] - case.human_scores[key])
            for key in case.human_scores
        ]
        criterion_errors.extend(errors)
        total_error = abs(sum(case.predicted_scores.values()) - sum(case.human_scores.values()))
        total_errors.append(total_error)
        within_one += total_error <= 1

        needs_review = total_error > 1 or any(error > 1 for error in errors)
        flagged = case.confidence < review_threshold
        true_review += needs_review
        predicted_review += flagged
        matched_review += needs_review and flagged

    return {
        "case_count": len(cases),
        "criterion_mae": round(sum(criterion_errors) / len(criterion_errors), 4),
        "total_score_mae": round(sum(total_errors) / len(total_errors), 4),
        "within_one_total_rate": round(within_one / len(cases), 4),
        "review_precision": round(matched_review / predicted_review, 4) if predicted_review else None,
        "review_recall": round(matched_review / true_review, 4) if true_review else None,
        "review_threshold": review_threshold,
    }
