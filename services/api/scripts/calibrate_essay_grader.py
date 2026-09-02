from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from app.adaptive.essay_calibration import CalibrationCase, summarize_calibration
from app.adaptive.essay_judge import EssayJudge
from app.adaptive.rubrics import get_rubric
from app.config import get_settings
from app.llm import build_llm_router


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare the configured essay grader with human-scored calibration cases"
    )
    parser.add_argument("input", type=Path, help="JSONL with prompt, answer, rubric_id and human_scores")
    parser.add_argument("--output", type=Path, required=True, help="Versioned calibration artifact")
    parser.add_argument("--review-threshold", type=float, default=0.65)
    return parser.parse_args()


async def run(input_path: Path, output_path: Path, review_threshold: float) -> None:
    router = build_llm_router(get_settings())
    if router is None:
        raise RuntimeError("Configure a real approved LLM provider before running calibration")
    judge = EssayJudge(router)
    raw_cases = [json.loads(line) for line in input_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    results: list[dict] = []
    metrics_cases: list[CalibrationCase] = []

    for index, item in enumerate(raw_cases, start=1):
        rubric = get_rubric(str(item["rubric_id"]))
        judgement = await judge.grade(
            prompt=str(item["prompt"]),
            answer=str(item["answer"]),
            rubric=rubric.criteria,
        )
        human_scores = {key: float(value) for key, value in item["human_scores"].items()}
        predicted_scores = {
            key: float(value) for key, value in judgement.criterion_scores.items()
        }
        metrics_cases.append(
            CalibrationCase(
                human_scores=human_scores,
                predicted_scores=predicted_scores,
                confidence=judgement.confidence,
            )
        )
        results.append(
            {
                "case_id": item.get("id", f"case-{index:03d}"),
                "rubric_id": rubric.id,
                "human_scores": human_scores,
                "predicted_scores": predicted_scores,
                "confidence": judgement.confidence,
                "provider": judgement.provider,
                "model": judgement.model,
                "feedback": judgement.feedback,
            }
        )

    artifact = {
        "summary": summarize_calibration(metrics_cases, review_threshold),
        "cases": results,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    arguments = parse_args()
    asyncio.run(run(arguments.input, arguments.output, arguments.review_threshold))
