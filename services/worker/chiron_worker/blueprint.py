"""Deterministic BlueprintCompiler: course blueprint -> immutable question specs.

The compiler is pure. Given the same course spec, concept list and seed it emits
byte-identical specs, so re-running a batch never creates a second spec row for
work that already exists.

Quota is exact by construction: format, cognitive level, difficulty and scope are
each expanded into a multiset of the required size, permuted independently, then
zipped. Every marginal distribution in the course spec is therefore hit exactly,
while the joint distribution stays uncorrelated (analyze does not always land on
the same format).
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass
from typing import Any

import yaml

from .question_bank import QuestionSpec

OBJECTIVE_FORMATS = {"single_choice", "ordering_or_matching", "scenario_diagnosis"}


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _expand(mix: dict[str, int], forms: int) -> list[str]:
    return [key for key, count in sorted(mix.items()) for _ in range(count * forms)]


def _permute(values: list[str], seed: int, salt: int) -> list[str]:
    shuffled = list(values)
    random.Random(seed * 1000 + salt).shuffle(shuffled)
    return shuffled


@dataclass(frozen=True)
class Concept:
    name: str
    summary: str

    @property
    def slug(self) -> str:
        return _slug(self.name)


def load_course_spec(path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _scope_mix(spec: dict[str, Any], key: str, forms: int) -> list[str]:
    mix = {
        entry["scope"]: int(entry[key])
        for entry in spec["content_distribution"]
        if int(entry[key]) > 0
    }
    return _expand(mix, forms)


def compile_specs(
    course_spec: dict[str, Any],
    concepts: list[Concept],
    *,
    forms: int = 1,
    generation_count: int = 3,
    seed: int = 20260831,
    batch: str = "b02",
) -> list[QuestionSpec]:
    """Expand the blueprint into `forms` complete exam forms' worth of specs."""
    if not concepts:
        raise ValueError("BlueprintCompiler needs at least one approved concept")
    course_slug = course_spec["course"]["slug"]
    specs: list[QuestionSpec] = []
    ordinals: dict[tuple[str, ...], int] = {}

    plans = (
        ("objective", course_spec["objective_blueprint"], "objective_count"),
        ("constructed", course_spec["constructed_response_blueprint"], "constructed_response_count"),
    )
    for index, (kind, blueprint, scope_key) in enumerate(plans):
        formats = _expand(blueprint["type_mix"], forms)
        scopes = _permute(_scope_mix(course_spec, scope_key, forms), seed, 10 + index)
        if kind == "objective":
            levels = _permute(_expand(blueprint["cognitive_mix"], forms), seed, 20)
            difficulties = _permute(_expand(blueprint["difficulty_mix"], forms), seed, 30)
        else:
            # The course spec sets no cognitive/difficulty mix for constructed response.
            levels = ["analyze"] * len(formats)
            difficulties = ["hard"] * len(formats)
        formats = _permute(formats, seed, 40 + index)

        sizes = {len(formats), len(scopes), len(levels), len(difficulties)}
        if len(sizes) != 1:
            raise ValueError(
                f"{kind}: blueprint quotas disagree — formats={len(formats)}, "
                f"scopes={len(scopes)}, levels={len(levels)}, difficulty={len(difficulties)}. "
                "Fix course-spec-v1.yaml so every mix sums to the same total."
            )

        for position, (fmt, scope, level, difficulty) in enumerate(
            zip(formats, scopes, levels, difficulties, strict=True)
        ):
            concept = concepts[position % len(concepts)]
            key = (concept.slug, fmt, level, difficulty)
            ordinals[key] = ordinals.get(key, 0) + 1
            specs.append(
                QuestionSpec(
                    spec_id=f"qs-{batch}-{concept.slug}-{_slug(fmt)}-{level}-{difficulty}-{ordinals[key]:02d}",
                    course_id=course_slug,
                    concept_ids=[concept.name],
                    learning_objective=(
                        f"{concept.summary.rstrip('.')} — vận dụng ở mức {level} trong tình huống {scope}."
                    ),
                    scope=scope,
                    format=fmt,
                    cognitive_level=level,
                    difficulty_target=difficulty,
                    misconception_target=(
                        f"Nhầm {concept.name.replace('_', ' ')} với một kỹ thuật lân cận "
                        "giải cùng triệu chứng nhưng khác nguyên nhân."
                    ),
                    required_evidence=1,
                    generation_count=generation_count,
                    exposure_group=f"{batch}-{scope}",
                )
            )

    seen = [spec.spec_id for spec in specs]
    if len(seen) != len(set(seen)):
        raise ValueError("BlueprintCompiler produced duplicate spec ids")
    return specs


def quota_report(specs: list[QuestionSpec]) -> dict[str, dict[str, int]]:
    """Marginal counts, for asserting the compiled batch matches the blueprint."""
    report: dict[str, dict[str, int]] = {"format": {}, "cognitive_level": {}, "difficulty": {}, "scope": {}}
    for spec in specs:
        for field, value in (
            ("format", spec.format),
            ("cognitive_level", spec.cognitive_level),
            ("difficulty", spec.difficulty_target),
            ("scope", spec.scope),
        ):
            report[field][value] = report[field].get(value, 0) + 1
    return report


def demo() -> None:
    """Self-check: quotas must come out exactly as the course spec declares."""
    course_spec = {
        "course": {"slug": "demo"},
        "content_distribution": [
            {"scope": "a", "objective_count": 6, "constructed_response_count": 1},
            {"scope": "b", "objective_count": 2, "constructed_response_count": 1},
        ],
        "objective_blueprint": {
            "type_mix": {"single_choice": 5, "scenario_diagnosis": 3},
            "cognitive_mix": {"understand": 4, "apply": 3, "analyze": 1},
            "difficulty_mix": {"easy": 2, "medium": 5, "hard": 1},
        },
        "constructed_response_blueprint": {"type_mix": {"system_design": 2}},
    }
    concepts = [Concept("chunking", "Phân đoạn tài liệu."), Concept("reranking", "Xếp lại candidate.")]
    specs = compile_specs(course_spec, concepts, forms=2, generation_count=3)

    assert len(specs) == (8 + 2) * 2, len(specs)
    report = quota_report(specs)
    assert report["format"] == {"single_choice": 10, "scenario_diagnosis": 6, "system_design": 4}, report["format"]
    assert report["cognitive_level"]["analyze"] == 2 + 4, report["cognitive_level"]
    assert report["difficulty"]["medium"] == 10, report["difficulty"]
    assert report["scope"] == {"a": 14, "b": 6}, report["scope"]
    assert len({spec.spec_id for spec in specs}) == len(specs)

    again = compile_specs(course_spec, concepts, forms=2, generation_count=3)
    assert [s.spec_id for s in again] == [s.spec_id for s in specs], "compiler is not deterministic"

    objective = [s for s in specs if s.format in OBJECTIVE_FORMATS]
    assert all(not s.is_constructed_response for s in objective)
    print("blueprint demo ok:", {k: v for k, v in report.items() if k != "scope"})


if __name__ == "__main__":
    demo()
