"""Generate a review-only 30 objective + 6 constructed-response pilot pack.

Run from services/worker with DATABASE_URL and GROQ_API_KEY available. The
result is deliberately Markdown, not a published assessment record.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

import httpx
import psycopg

ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "data" / "questions" / "review" / "pilot-v1.md"

OBJECTIVE = [
    ("chunking", "scenario_diagnosis", "apply", "medium"),
    ("embedding", "single_choice", "understand", "easy"),
    ("dense_retrieval", "scenario_diagnosis", "apply", "medium"),
    ("sparse_retrieval", "single_choice", "understand", "easy"),
    ("hybrid_search", "scenario_diagnosis", "analyze", "hard"),
    ("reciprocal_rank_fusion", "single_choice", "apply", "medium"),
    ("reranking", "scenario_diagnosis", "apply", "medium"),
    ("metadata_filtering", "scenario_diagnosis", "apply", "hard"),
    ("hnsw", "single_choice", "understand", "medium"),
    ("vector_database", "scenario_diagnosis", "apply", "medium"),
    ("rag_pipeline", "ordering_or_matching", "understand", "medium"),
    ("context_precision", "single_choice", "apply", "medium"),
    ("context_recall", "single_choice", "apply", "medium"),
    ("faithfulness", "scenario_diagnosis", "analyze", "hard"),
    ("answer_relevancy", "single_choice", "understand", "easy"),
    ("rag_evaluation", "scenario_diagnosis", "apply", "medium"),
    ("multi_hop_retrieval", "scenario_diagnosis", "analyze", "hard"),
    ("llm_agent_orchestration", "scenario_diagnosis", "apply", "medium"),
    ("state_machine", "single_choice", "apply", "medium"),
    ("checkpointing", "scenario_diagnosis", "apply", "medium"),
    ("human_in_the_loop", "scenario_diagnosis", "analyze", "hard"),
    ("circuit_breaker", "scenario_diagnosis", "apply", "medium"),
    ("fallback_chain", "single_choice", "apply", "medium"),
    ("observability", "scenario_diagnosis", "analyze", "hard"),
    ("sli_slo", "single_choice", "apply", "medium"),
    ("short_term_memory", "single_choice", "understand", "easy"),
    ("episodic_memory", "single_choice", "understand", "medium"),
    ("semantic_memory", "scenario_diagnosis", "apply", "medium"),
    ("graphrag", "scenario_diagnosis", "analyze", "hard"),
    ("prompt_injection", "scenario_diagnosis", "apply", "medium"),
]
CONSTRUCTED = [
    ("observability", "tracing_and_monitoring_diagnosis"),
    ("prompt_injection", "security_and_data_governance"),
    ("llm_agent_orchestration", "system_design"),
    ("rag_pipeline", "code_or_pseudocode"),
    ("fallback_chain", "guardrail_or_incident_reasoning"),
    ("checkpointing", "system_design"),
]


def load_env() -> None:
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        if "=" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"'))


def evidence_for(slug: str) -> dict:
    sql = """
      SELECT n.canonical_name, s.id::text, d.title, s.locator::text, c.content
      FROM concept_nodes n
      JOIN chunk_concepts cc ON cc.concept_id=n.id AND cc.review_status IN ('approved','active')
      JOIN chunks c ON c.id=cc.chunk_id
      JOIN source_spans s ON s.id=c.source_span_id
      JOIN document_versions d ON d.id=s.document_version_id
      WHERE n.normalized_name=%s AND n.review_status IN ('approved','active')
      ORDER BY cc.confidence DESC, c.ordinal ASC LIMIT 2
    """
    database_url = os.environ["DATABASE_URL"].replace("postgresql+psycopg://", "postgresql://", 1)
    with psycopg.connect(database_url) as conn:
        tenant = conn.execute("SELECT id::text FROM tenants WHERE slug='chiron-demo'").fetchone()
        if tenant is None:
            raise RuntimeError("Demo tenant chiron-demo is required")
        conn.execute("SELECT set_config('app.tenant_id', %s, true)", (tenant[0],))
        rows = conn.execute(sql, (slug,)).fetchall()
    if not rows:
        raise RuntimeError(f"No approved evidence for {slug}")
    name = rows[0][0]
    spans = [
        {"source_span_id": row[1], "title": row[2], "locator": row[3], "excerpt": row[4][:1600]}
        for row in rows
    ]
    return {"concept": slug, "canonical_name": name, "spans": spans}


def generate(batch: list[dict], constructed: bool) -> list[dict]:
    model = os.environ.get("LLM_EXTRACTION_MODEL", "openai/gpt-oss-20b")
    system = """You are a Vietnamese assessment author. Use ONLY the supplied evidence. Return valid JSON only. Each question must be original, answerable from its evidence, technically precise, and must not mention citations in the learner-facing stem. Do not invent facts. For objective questions provide exactly four options and exactly one correct option; distractors are plausible but unambiguously wrong. Write Vietnamese naturally, retaining essential English technical terms."""
    task = "constructed response" if constructed else "objective"
    user = f"""Create {task} questions for the following specifications and evidence. Return an object {{\"questions\": [...]}}. For every question include: id, concept, format, stem, options (objective only, each id/text), correct_option_ids (objective only), rationale, claim_to_evidence (array of claim and source_span_ids). For constructed response also include rubric (3-5 criteria, each label/max_score/observable_evidence/common_failure_modes), acceptable_alternatives, and model_solution_outline. Do not add markdown.\n\n{json.dumps(batch, ensure_ascii=False)}"""
    schema = {
        "name": "pilot_questions",
        "schema": {"type": "object", "properties": {"questions": {"type": "array"}}, "required": ["questions"], "additionalProperties": False},
    }
    response = httpx.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['GROQ_API_KEY']}", "Content-Type": "application/json"},
        json={"model": model, "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}], "temperature": 0.25, "max_tokens": 5000, "response_format": {"type": "json_schema", "json_schema": schema}},
        timeout=90,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"] and json.loads(response.json()["choices"][0]["message"]["content"])["questions"]


def render(question: dict, number: int, evidence: dict) -> str:
    lines = [f"## {number}. {question['stem']}", f"- **Concept:** {evidence['canonical_name']} (`{question['concept']}`)", f"- **Format:** `{question['format']}`", ""]
    if question.get("options"):
        lines += [f"- {option['id']}. {option['text']}" for option in question["options"]]
        lines += ["", f"**Đáp án:** {', '.join(question.get('correct_option_ids', []))}"]
    else:
        lines += ["**Rubric:**"]
        for criterion in question.get("rubric", []):
            lines.append(f"- {criterion['label']} ({criterion['max_score']} điểm): {', '.join(criterion['observable_evidence'])}")
        lines.append(f"\n**Hướng giải tham chiếu:** {question.get('model_solution_outline', '')}")
        lines.append(f"**Phương án hợp lệ khác:** {', '.join(question.get('acceptable_alternatives', []))}")
    lines += [f"\n**Rationale:** {question['rationale']}", "**Evidence:**"]
    cited = {sid for item in question.get("claim_to_evidence", []) for sid in item.get("source_span_ids", [])}
    for span in evidence["spans"]:
        marker = "✓" if span["source_span_id"] in cited else "•"
        lines.append(f"- {marker} `{span['source_span_id']}` — {span['title']} — {span['locator']}")
    return "\n".join(lines)


def main() -> None:
    load_env()
    if not os.environ.get("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY is required")
    selected = [{"id": f"obj-{i:02d}", "concept": c, "format": f, "cognitive_level": level, "difficulty": difficulty, "evidence": evidence_for(c)} for i, (c, f, level, difficulty) in enumerate(OBJECTIVE, 1)]
    selected_cr = [{"id": f"cr-{i:02d}", "concept": c, "format": f, "cognitive_level": "analyze", "difficulty": "hard", "evidence": evidence_for(c)} for i, (c, f) in enumerate(CONSTRUCTED, 1)]
    objective_questions = [question for start in range(0, len(selected), 5) for question in generate(selected[start:start + 5], False)]
    cr_questions = [question for start in range(0, len(selected_cr), 3) for question in generate(selected_cr[start:start + 3], True)]
    by_concept = {item["concept"]: item["evidence"] for item in selected + selected_cr}
    body = ["# Chiron AI — Pilot question-bank review v1", "", "**Status:** candidate for expert review — not published, not delivered to learners.", "", "## Objective questions (30)", ""]
    body += [render(question, i, by_concept[question["concept"]]) + "\n" for i, question in enumerate(objective_questions, 1)]
    body += ["## Constructed response (6)", ""]
    body += [render(question, 30 + i, by_concept[question["concept"]]) + "\n" for i, question in enumerate(cr_questions, 1)]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(body), encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT), "objective": len(objective_questions), "constructed": len(cr_questions)}))


if __name__ == "__main__":
    main()
