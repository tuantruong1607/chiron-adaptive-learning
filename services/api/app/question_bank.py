from __future__ import annotations

import json
import re
from collections import defaultdict, deque
from hashlib import sha256
from pathlib import Path

from .adaptive.essay_judge import Criterion
from .schemas import DiagnosticQuestion, QuestionOption

_BANK_PATH = Path(__file__).with_name("generated_question_bank.json")
_TAXONOMY_PATH = Path(__file__).with_name("course_taxonomy.json")
_BANK: list[dict] = json.loads(_BANK_PATH.read_text(encoding="utf-8"))
_TAXONOMY: dict = json.loads(_TAXONOMY_PATH.read_text(encoding="utf-8"))
_NODES_BY_ID = {node["id"]: node for node in _TAXONOMY["nodes"]}
_TOPIC_TO_CONCEPT = {
    topic: node["id"]
    for node in _TAXONOMY["nodes"]
    for topic in node.get("question_topics", [])
}
_DOMAIN_ORDER = tuple(domain["id"] for domain in _TAXONOMY["domains"])
_DOMAIN_TARGETS = {
    "data_retrieval": 5,
    "agents_orchestration": 4,
    "memory_graph": 2,
    "safety_governance": 2,
    "deployment_operations": 2,
    "evaluation": 3,
    "fine_tuning_alignment": 1,
    "production_architecture": 1,
}


def _concept_for_topic(topic: str) -> str | None:
    return _TOPIC_TO_CONCEPT.get(topic)


def build_diagnostic_questions(limit: int = 20) -> tuple[list[tuple[DiagnosticQuestion, str]], dict[str, str]]:
    concept_buckets: dict[str, deque[dict]] = defaultdict(deque)
    for item in _BANK:
        if item["kind"] != "objective" or item["reviewDecision"] == "reject":
            continue
        concept_id = _concept_for_topic(item["topic"])
        if concept_id:
            concept_buckets[concept_id].append(item)

    selected: list[dict] = []
    domain_concepts: dict[str, list[str]] = defaultdict(list)
    for node in _TAXONOMY["nodes"]:
        if concept_buckets[node["id"]]:
            domain_concepts[node["domain"]].append(node["id"])

    # Blueprint-stratified sampling: cover distinct concepts in every domain
    # before drawing a second question from the same concept.
    for domain_id in _DOMAIN_ORDER:
        target = min(_DOMAIN_TARGETS.get(domain_id, 0), limit - len(selected))
        concepts = domain_concepts[domain_id]
        while target > 0 and any(concept_buckets[item] for item in concepts):
            for concept_id in concepts:
                if target == 0:
                    break
                if concept_buckets[concept_id]:
                    item = concept_buckets[concept_id].popleft()
                    selected.append({**item, "conceptId": concept_id})
                    target -= 1

    # Keep the requested length stable if a future bank temporarily has fewer
    # items than one of the configured domain targets.
    while len(selected) < limit and any(concept_buckets.values()):
        for node in _TAXONOMY["nodes"]:
            concept_id = node["id"]
            if concept_buckets[concept_id] and len(selected) < limit:
                item = concept_buckets[concept_id].popleft()
                selected.append({**item, "conceptId": concept_id})

    questions: list[tuple[DiagnosticQuestion, str]] = []
    explanations: dict[str, str] = {}
    for item in selected:
        question = DiagnosticQuestion(
            id=item["id"],
            concept_id=item["conceptId"],
            prompt=item["prompt"],
            options=[QuestionOption(id=option["id"], text=option["text"]) for option in item["options"]],
        )
        questions.append((question, item["answerKey"]))
        explanations[question.id] = item["explanation"]
    return questions, explanations


def mock_exam_questions(form_id: str) -> list[dict]:
    if form_id not in {"de-01", "de-02", "de-03", "de-04"}:
        raise LookupError("Mock exam form not found")
    ordered = sorted(
        _BANK,
        key=lambda item: sha256(f"{form_id}:{item['id']}".encode()).hexdigest(),
    )
    return [
        {
            key: value
            for key, value in item.items()
            if key not in {"answerKey", "explanation", "referenceAnswer", "reviewDecision"}
        }
        for item in ordered
    ]


def mock_exam_item(question_id: str) -> dict | None:
    return next((item for item in _BANK if item["id"] == question_id), None)


def rubric_criteria(item: dict) -> tuple[Criterion, ...]:
    criteria: list[Criterion] = []
    for index, match in enumerate(
        re.finditer(r"\s*(.+?)\s+(\d+)đ(?:;|\.|$)", item.get("rubric", "")),
        start=1,
    ):
        label = match.group(1).strip()
        keywords = tuple(
            word
            for word in re.findall(r"[A-Za-zÀ-ỹ_/-]{5,}", label)
            if word.casefold() not in {"trong", "được", "hoặc", "không"}
        )[:5]
        criteria.append(
            Criterion(
                id=f"criterion-{index}",
                label=label,
                max_score=int(match.group(2)),
                observable_evidence=keywords or (label,),
            )
        )
    if not criteria:
        criteria.append(
            Criterion(
                id="criterion-1",
                label="Lập luận đúng, cụ thể và có cách kiểm chứng",
                max_score=10,
                observable_evidence=("kiểm chứng", "điều kiện", "trade-off"),
            )
        )
    return tuple(criteria)
