from app.adaptive.essay_calibration import CalibrationCase, summarize_calibration


def test_calibration_summary_measures_score_error_and_review_gate() -> None:
    summary = summarize_calibration(
        [
            CalibrationCase(
                human_scores={"grounding": 4, "reasoning": 3, "transfer": 2},
                predicted_scores={"grounding": 4, "reasoning": 2, "transfer": 2},
                confidence=0.8,
            ),
            CalibrationCase(
                human_scores={"grounding": 4, "reasoning": 4, "transfer": 2},
                predicted_scores={"grounding": 1, "reasoning": 2, "transfer": 1},
                confidence=0.4,
            ),
        ]
    )

    assert summary["case_count"] == 2
    assert summary["criterion_mae"] == 1.1667
    assert summary["total_score_mae"] == 3.5
    assert summary["within_one_total_rate"] == 0.5
    assert summary["review_precision"] == 1
    assert summary["review_recall"] == 1
