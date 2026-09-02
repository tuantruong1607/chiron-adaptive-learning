"""Import the reviewed 100-item question-bank snapshot into PostgreSQL.

The source Markdown remains immutable. Review outcomes come from the adjacent
JSON artifact. The import is fail-closed and idempotent: a rerun accepts the
same snapshot, but refuses to overwrite a row if its checksum has changed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from difflib import SequenceMatcher
from hashlib import sha256
from pathlib import Path
from typing import Any
from uuid import NAMESPACE_URL, uuid5

import psycopg
from psycopg.types.json import Jsonb

ROOT = Path(__file__).resolve().parents[3]
WORKER_ROOT = Path(__file__).resolve().parents[1]
for path in (ROOT, WORKER_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from scripts.validate_question_bank import load_spans, parse  # noqa: E402

from chiron_worker.question_bank import (  # noqa: E402
    ClaimEvidence,
    EvidencePack,
    EvidenceSpan,
    Option,
    QuestionCandidate,
    QuestionSpec,
    RubricCriterion,
    validate_candidate,
)

BATCH_ID = "question-bank-v1"
TENANT_SLUG = "chiron-demo"
COURSE_SLUG = "rag-intensive"
VALIDATOR_NAME = "question-bank-markdown-contract"
VALIDATOR_VERSION = "question-bank-contract-v2"
REVIEW_PROTOCOL_VERSION = "question-review-protocol-v1"
DEFAULT_SOURCE = ROOT / "data" / "questions" / "review" / "question-bank-v1.md"
DEFAULT_REVIEW = ROOT / "data" / "questions" / "review" / "question-bank-v1-review.json"
DEFAULT_CORPUS = ROOT / "data" / "manifests" / "corpus.json"
DEFAULT_SPANS = ROOT / "data" / "manifests" / "source_spans.jsonl"

META_PATTERN = re.compile(r"^> \*\*Metadata:\*\* .+$", re.MULTILINE)
ANSWER_PATTERN = re.compile(r"^\*\*Đáp án:\*\* ([A-D])\. (.*?)  $", re.MULTILINE | re.DOTALL)
RUBRIC_PATTERN = re.compile(r"^\*\*Rubric:\*\* (.+?)[ \t]*$", re.MULTILINE)
RUBRIC_CRITERION_PATTERN = re.compile(r"\s*(.+?)\s+(\d+)đ(?:;|\.|$)")
REFERENCE_PATTERN = re.compile(
    r"^\*\*Đáp án tham chiếu ngắn gọn:\*\* (.+?)(?=\n\n\*\*|\n\n---|\Z)",
    re.MULTILINE | re.DOTALL,
)
ALTERNATIVE_PATTERN = re.compile(
    r"^\*\*Đáp án chấp nhận khác:\*\* (.+?)(?=\n\n\*\*|\n\n---|\Z)",
    re.MULTILINE | re.DOTALL,
)

# Only map topics to an existing active graph concept when the relationship is
# unambiguous. The original topic remains in question_specs.concept_slugs even
# when no active graph node exists yet (notably the alignment questions).
TOPIC_TO_CONCEPTS: dict[str, tuple[str, ...]] = {
    "chunking": ("chunking",),
    "embedding": ("embedding",),
    "dense-vs-sparse-retrieval": ("dense_retrieval", "sparse_retrieval"),
    "sparse-retrieval": ("sparse_retrieval",),
    "hybrid-fusion": ("hybrid_search", "reciprocal_rank_fusion"),
    "reranking": ("reranking",),
    "tenant-isolation": ("metadata_filtering",),
    "ann-indexing": ("hnsw",),
    "rag-offline-pipeline": ("rag_pipeline",),
    "context-precision": ("context_precision",),
    "context-recall": ("context_recall",),
    "faithfulness": ("faithfulness",),
    "answer-relevancy": ("answer_relevancy",),
    "rag-diagnosis": ("rag_evaluation",),
    "multi-hop-retrieval": ("multi_hop_retrieval",),
    "agent-idempotency": ("llm_agent_orchestration",),
    "agent-state-machine": ("state_machine",),
    "durable-checkpointing": ("checkpointing",),
    "human-in-the-loop": ("human_in_the_loop",),
    "circuit-breaker": ("circuit_breaker",),
    "fallback-policy": ("fallback_chain",),
    "agent-observability": ("observability",),
    "sli-slo": ("sli_slo",),
    "short-term-memory": ("short_term_memory",),
    "episodic-memory": ("episodic_memory",),
    "semantic-memory": ("semantic_memory",),
    "graphrag-traversal": ("graphrag",),
    "retrieval-prompt-injection": ("prompt_injection",),
    "semantic-cache": ("semantic_cache",),
    "memory-consolidation": ("memory_consolidation",),
    "hitl-gating": ("human_in_the_loop",),
    "confidence-calibration": ("human_in_the_loop",),
    "tool-permission": ("llm_agent_orchestration",),
    "mcp-oauth": ("llm_agent_orchestration",),
    "health-probes": ("observability",),
    "durable-execution": ("checkpointing",),
    "session-lifetime": ("checkpointing",),
    "framework-vs-runtime": ("llm_agent_orchestration",),
    "memory-lifecycle": ("agent_memory",),
    "memory-vs-retrieval": ("agent_memory",),
    "multi-agent-design": ("llm_agent_orchestration",),
    "mcp-vs-a2a": ("llm_agent_orchestration",),
    "supervisor-routing": ("llm_agent_orchestration",),
    "error-types": ("rag_evaluation",),
    "precision-recall": ("rag_evaluation",),
    "nondeterminism": ("rag_evaluation",),
    "evaluation-types": ("rag_evaluation",),
    "faithfulness-formula": ("faithfulness",),
    "answer-relevancy-formula": ("answer_relevancy",),
    "golden-dataset": ("rag_evaluation",),
    "llm-judge-bias": ("rag_evaluation",),
    "chunking-rationale": ("chunking",),
    "chunk-overlap": ("chunking",),
    "top-k-limitation": ("dense_retrieval",),
    "mmr-diversity": ("reranking",),
    "ann-index-choice": ("vector_database",),
    "vector-quantization": ("vector_database",),
    "filtered-search": ("metadata_filtering",),
    "cosine-similarity-myth": ("embedding",),
    "asymmetric-search": ("embedding",),
    "table-chunking": ("chunking",),
    "chunk-size-tradeoff": ("chunking",),
    "chunk-size-512": ("chunking",),
    "filter-recall-collapse": ("metadata_filtering",),
    "rrf-formula": ("reciprocal_rank_fusion",),
    "pii-masking": ("embedding",),
    "etl-vs-elt": ("rag_pipeline",),
    "change-data-capture": ("rag_pipeline",),
    "dlq-triage": ("rag_pipeline",),
    "pipeline-idempotency": ("rag_pipeline",),
    "temperature-zero-myth": ("llm_agent_orchestration",),
    "prompt-cache-invalidation": ("llm_agent_orchestration",),
    "online-offline-eval": ("rag_evaluation",),
    "judge-position-bias": ("rag_evaluation",),
    "prompt-injection-types": ("prompt_injection",),
    "owasp-llm-top10": ("prompt_injection",),
    "over-filtering-trap": ("prompt_injection",),
    "single-agent-limits": ("llm_agent_orchestration",),
    "mcp-vs-a2a-boundary": ("llm_agent_orchestration",),
    "routing-pattern-cost": ("llm_agent_orchestration",),
    "supervisor-hub-spoke": ("llm_agent_orchestration",),
    "agent-reliability": ("llm_agent_orchestration", "state_machine"),
    "retrieval-router": ("hybrid_search", "multi_hop_retrieval"),
    "fallback-governance": ("fallback_chain",),
    "memory-architecture": ("agent_memory",),
    "agent-safe-retry": ("llm_agent_orchestration", "checkpointing"),
    "agent-deployment-pipeline": ("llm_agent_orchestration", "observability"),
    "incident-latency-diagnosis": ("observability",),
    "observability-pii-governance": ("observability",),
    "rag-security": ("prompt_injection", "metadata_filtering"),
}

# The learner graph remains compact until the expanded taxonomy passes the
# retrieval gates. Fold detailed authoring concepts into the closest active
# node so every reviewed item keeps a useful learning-map link.
ACTIVE_CONCEPT_ALIASES: dict[str, str] = {
    "agent_memory": "evaluation",
    "answer_relevancy": "evaluation",
    "checkpointing": "evaluation",
    "circuit_breaker": "evaluation",
    "context_precision": "evaluation",
    "context_recall": "evaluation",
    "dense_retrieval": "dense",
    "embedding": "dense",
    "episodic_memory": "evaluation",
    "faithfulness": "citation",
    "fallback_chain": "evaluation",
    "graphrag": "graph-routing",
    "hnsw": "dense",
    "human_in_the_loop": "evaluation",
    "hybrid_search": "rrf",
    "llm_agent_orchestration": "evaluation",
    "memory_consolidation": "evaluation",
    "metadata_filtering": "metadata-filtering",
    "multi_hop_retrieval": "graph-routing",
    "observability": "evaluation",
    "prompt_injection": "metadata-filtering",
    "rag_evaluation": "evaluation",
    "rag_pipeline": "chunking",
    "reciprocal_rank_fusion": "rrf",
    "semantic_cache": "evaluation",
    "semantic_memory": "evaluation",
    "short_term_memory": "evaluation",
    "sli_slo": "evaluation",
    "sparse_retrieval": "sparse",
    "state_machine": "evaluation",
    "vector_database": "dense",
}


@dataclass(frozen=True)
class ReviewOutcome:
    decision: str
    reason_code: str
    notes: str


@dataclass(frozen=True)
class ResolvedSpan:
    manifest_id: str
    database_id: str
    title: str
    locator: dict[str, Any]
    text: str
    checksum: str
    match_method: str
    similarity: float


def stable_id(name: str):
    return uuid5(NAMESPACE_URL, f"https://chiron.local/{BATCH_ID}/{name}")


def checksum(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256(encoded.encode("utf-8")).hexdigest()


def normalized_text(value: str) -> str:
    # The manifest OCR occasionally fuses words ("failfast") while the
    # database parser preserves spaces ("fail fast"). Whitespace-insensitive
    # comparison keeps the title/page remap deterministic across those parser
    # versions without weakening it to a title-only match.
    return re.sub(r"\s+", "", value).casefold()


def clean_markdown(value: str) -> str:
    return " ".join(value.strip().split())


def load_review(path: Path, item_numbers: set[int]) -> dict[int, ReviewOutcome]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    default = payload["default_decision"]
    outcomes = {
        number: ReviewOutcome(default["decision"], default["reason_code"], default["notes"])
        for number in item_numbers
    }
    for raw_number, value in payload["exceptions"].items():
        number = int(raw_number)
        if number not in outcomes:
            raise RuntimeError(f"Review artifact references unknown Q{number}")
        outcomes[number] = ReviewOutcome(value["decision"], value["reason_code"], value["notes"])
    counts = Counter(outcome.decision for outcome in outcomes.values())
    actual_counts = {name: counts[name] for name in ("accept", "revise", "reject", "escalate")}
    if actual_counts != payload["expected_counts"]:
        raise RuntimeError(
            f"Review count mismatch: actual={actual_counts} expected={payload['expected_counts']}"
        )
    return outcomes


def infer_format(number: int, title: str, metadata: dict[str, str]) -> str:
    if number <= 90:
        lowered = title.casefold()
        if "ordering" in lowered or "matching" in lowered:
            return "ordering_or_matching"
        if "scenario diagnosis" in lowered:
            return "scenario_diagnosis"
        return "single_choice"
    explicit = metadata.get("format")
    if explicit:
        return explicit
    lowered = title.casefold()
    if "pseudocode" in lowered:
        return "code_or_pseudocode"
    if "incident" in lowered or "reasoning" in lowered:
        return "guardrail_or_incident_reasoning"
    return "system_design"


def extract_title(body: str) -> str:
    return body.splitlines()[0].strip().strip("— ")


def extract_stem(body: str, *, objective: bool) -> str:
    metadata = META_PATTERN.search(body)
    if metadata is None:
        raise RuntimeError("Item is missing metadata")
    tail = body[metadata.end() :]
    marker = "\n- A." if objective else "\n**Rubric:**"
    if marker not in tail:
        raise RuntimeError(f"Cannot find stem boundary {marker!r}")
    return tail.split(marker, 1)[0].strip()


def extract_rationale(body: str, *, objective: bool) -> str:
    if objective:
        match = ANSWER_PATTERN.search(body)
        if match is None:
            raise RuntimeError("Objective item is missing answer rationale")
        return clean_markdown(match.group(2).split("\n**Evidence:**", 1)[0])
    reference = REFERENCE_PATTERN.search(body)
    if reference:
        return clean_markdown(reference.group(1))
    return "Chấm câu trả lời theo rubric 10 điểm và chỉ công nhận các claim có thể kiểm chứng từ evidence pack."


def extract_rubric(body: str) -> list[RubricCriterion]:
    match = RUBRIC_PATTERN.search(body)
    if match is None:
        raise RuntimeError("Constructed response is missing rubric")
    criteria = []
    for index, (label, raw_score) in enumerate(RUBRIC_CRITERION_PATTERN.findall(match.group(1)), 1):
        cleaned = clean_markdown(label)
        criteria.append(
            RubricCriterion(
                id=f"criterion-{index}",
                label=cleaned,
                max_score=int(raw_score),
                observable_evidence=[f"Câu trả lời thể hiện cụ thể: {cleaned}"],
                common_failure_modes=[
                    "Vắng mặt, sai cơ chế, hoặc không đáp ứng ràng buộc và cách kiểm chứng của tình huống."
                ],
            )
        )
    if not criteria or sum(item.max_score for item in criteria) != 10:
        raise RuntimeError("Constructed rubric must parse into exactly 10 points")
    return criteria


def extract_alternatives(body: str) -> list[str]:
    match = ALTERNATIVE_PATTERN.search(body)
    if match:
        return [clean_markdown(match.group(1))]
    return [
        "Giải pháp thay thế đạt cùng thuộc tính, đúng ràng buộc và có verification/trade-off được chấm đủ điểm."
    ]


def build_records(item, spans: list[ResolvedSpan]) -> tuple[QuestionSpec, EvidencePack, QuestionCandidate]:
    title = extract_title(item.body)
    objective = item.number <= 90
    item_format = infer_format(item.number, title, item.meta)
    external_id = f"qs-{BATCH_ID}-{item.number:03d}"
    candidate_id = f"qc-{BATCH_ID}-{item.number:03d}-human-v1"
    stem = extract_stem(item.body, objective=objective)
    rationale = extract_rationale(item.body, objective=objective)
    topic = item.meta["topic"]
    exposure_group = item.meta.get("group", "none")
    if exposure_group == "none":
        exposure_group = f"{BATCH_ID}-ungrouped-{item.number:03d}"
    spec = QuestionSpec(
        spec_id=external_id,
        course_id=COURSE_SLUG,
        concept_ids=[topic],
        learning_objective=stem,
        scope="question-bank-v1-reviewed-snapshot",
        format=item_format,
        cognitive_level=item.meta["cognitive_level"],
        difficulty_target=item.meta["difficulty"],
        misconception_target=(
            "Phân biệt kỹ thuật đúng với distractor đúng kỹ thuật nhưng sai ràng buộc của câu hỏi."
        ),
        required_evidence=len(spans),
        generation_count=1,
        exposure_group=exposure_group,
    )
    evidence_pack = EvidencePack(
        spec_id=external_id,
        tenant_id=TENANT_SLUG,
        course_id=COURSE_SLUG,
        corpus_version=f"corpus-{BATCH_ID}-2026-08-30",
        retrieval_mode="human_manifest_remap",
        spans=[
            EvidenceSpan(
                source_span_id=span.database_id,
                document_title=span.title,
                locator=json.dumps(span.locator, ensure_ascii=False, sort_keys=True),
                excerpt=span.text,
                rank=index,
            )
            for index, span in enumerate(spans, 1)
        ],
    )
    options = [
        Option(
            id=label,
            text=text,
            misconception="correct_answer" if label in item.answer else "reviewed_distractor",
        )
        for label, text in item.options
    ]
    candidate = QuestionCandidate(
        candidate_id=candidate_id,
        spec_id=external_id,
        format=item_format,
        stem=stem,
        options=options,
        correct_option_ids=item.answer,
        rationale=rationale,
        claim_to_evidence=[
            ClaimEvidence(
                claim=rationale,
                source_span_ids=[span.database_id for span in spans],
            )
        ],
        difficulty_rationale=(
            f"Nhãn tác vụ trong snapshot: {item.meta['cognitive_level']}/{item.meta['difficulty']}."
        ),
        rubric=[] if objective else extract_rubric(item.body),
        acceptable_alternatives=[] if objective else extract_alternatives(item.body),
    )
    result = validate_candidate(spec, evidence_pack, candidate)
    if not result.passed:
        raise RuntimeError(f"Q{item.number} fails persisted candidate contract: {result.errors}")
    return spec, evidence_pack, candidate


def resolve_database_spans(cursor, manifest_spans: dict[str, dict], corpus: dict) -> dict[str, ResolvedSpan]:
    titles = {row["document_version_id"]: row["title"] for row in corpus["documents"]}
    cursor.execute(
        """
        SELECT s.id::text, s.checksum, s.locator, s.text, dv.title
        FROM source_spans s
        JOIN document_versions dv ON dv.id = s.document_version_id
        """
    )
    database_rows = [
        {
            "id": row[0],
            "checksum": row[1],
            "locator": row[2],
            "text": row[3],
            "title": row[4] or "Untitled source",
        }
        for row in cursor.fetchall()
    ]
    by_id = {row["id"]: row for row in database_rows}
    by_checksum: dict[str, list[dict]] = {}
    for row in database_rows:
        by_checksum.setdefault(row["checksum"], []).append(row)

    resolved: dict[str, ResolvedSpan] = {}
    for manifest_id, source in manifest_spans.items():
        candidates: list[tuple[str, dict]] = []
        if manifest_id in by_id:
            candidates = [("exact_id", by_id[manifest_id])]
        elif len(by_checksum.get(source["checksum"], [])) == 1:
            candidates = [("checksum", by_checksum[source["checksum"]][0])]
        else:
            source_title = titles[source["document_version_id"]]
            source_page = source["locator"].get("page")
            for row in database_rows:
                row_page = row["locator"].get("page")
                title_matches = (
                    row["title"] == source_title
                    or row["title"].startswith(source_title)
                    or source_title.startswith(row["title"])
                )
                if row_page == source_page and title_matches:
                    candidates.append(("title_page_text", row))
        if not candidates:
            raise RuntimeError(f"Cannot resolve manifest source span {manifest_id} into PostgreSQL")
        scored = sorted(
            (
                SequenceMatcher(None, normalized_text(source["text"]), normalized_text(row["text"])).ratio(),
                method,
                row,
            )
            for method, row in candidates
        )
        similarity, method, row = scored[-1]
        if method == "title_page_text" and similarity < 0.75:
            raise RuntimeError(
                f"Unsafe source remap for {manifest_id}: title/page candidate similarity={similarity:.3f}"
            )
        if len(scored) > 1 and similarity - scored[-2][0] < 0.05:
            raise RuntimeError(f"Ambiguous source remap for {manifest_id}")
        resolved[manifest_id] = ResolvedSpan(
            manifest_id=manifest_id,
            database_id=row["id"],
            title=row["title"],
            locator=row["locator"],
            text=row["text"],
            checksum=row["checksum"],
            match_method=method,
            similarity=similarity,
        )
    return resolved


def ensure_same(cursor, table: str, row_id, fields: dict[str, Any]) -> bool:
    columns = list(fields)
    cursor.execute(
        f"SELECT {', '.join(columns)} FROM {table} WHERE id=%s",  # noqa: S608 - static table names
        (row_id,),
    )
    existing = cursor.fetchone()
    if existing is None:
        return False
    for column, actual, expected in zip(columns, existing, fields.values(), strict=True):
        if actual != expected:
            raise RuntimeError(f"Idempotency conflict in {table}.{column} for id={row_id}")
    return True


def insert_snapshot(
    cursor,
    *,
    tenant_id,
    course_id,
    reviewer_id,
    item,
    outcome: ReviewOutcome,
    spans: list[ResolvedSpan],
    active_concepts: dict[str, Any],
) -> bool:
    spec, pack, candidate = build_records(item, spans)
    spec_id = stable_id(f"spec:{item.number}")
    pack_id = stable_id(f"evidence-pack:{item.number}")
    candidate_row_id = stable_id(f"candidate:{item.number}")
    spec_payload = spec.model_dump(mode="json")
    spec_checksum = checksum(spec_payload)
    candidate_payload = candidate.model_dump(mode="json")
    candidate_checksum = checksum(candidate_payload)
    candidate_state = {
        "accept": "approved",
        "revise": "expert_reviewed",
        "reject": "rejected",
    }[outcome.decision]
    database_decision = {
        "accept": "approved",
        "revise": "needs_revision",
        "reject": "rejected",
    }[outcome.decision]

    existed = ensure_same(
        cursor,
        "question_specs",
        spec_id,
        {"external_id": spec.spec_id, "input_checksum": spec_checksum},
    )
    if not existed:
        cursor.execute(
            """
            INSERT INTO question_specs (
                id, tenant_id, course_id, external_id, blueprint_cell, concept_slugs,
                learning_objective, format, cognitive_level, difficulty_target,
                misconception_target, required_evidence, generation_count, exposure_group,
                state, input_checksum
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'ready',%s)
            """,
            (
                spec_id,
                tenant_id,
                course_id,
                spec.spec_id,
                Jsonb(
                    {
                        "batch": BATCH_ID,
                        "item_number": item.number,
                        "title": extract_title(item.body),
                        "review_decision": outcome.decision,
                    }
                ),
                Jsonb(spec.concept_ids),
                spec.learning_objective,
                spec.format,
                spec.cognitive_level,
                spec.difficulty_target,
                spec.misconception_target,
                spec.required_evidence,
                spec.generation_count,
                spec.exposure_group,
                spec_checksum,
            ),
        )

    pack_trace = {
        "batch": BATCH_ID,
        "source_file": str(DEFAULT_SOURCE.relative_to(ROOT)).replace("\\", "/"),
        "spans": [
            {
                "manifest_source_span_id": span.manifest_id,
                "database_source_span_id": span.database_id,
                "match_method": span.match_method,
                "similarity": round(span.similarity, 6),
            }
            for span in spans
        ],
    }
    if not ensure_same(cursor, "evidence_packs", pack_id, {"checksum": pack.checksum}):
        cursor.execute(
            """
            INSERT INTO evidence_packs (
                id, tenant_id, course_id, question_spec_id, corpus_version,
                retrieval_mode, retrieval_trace, checksum, state
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'frozen')
            """,
            (
                pack_id,
                tenant_id,
                course_id,
                spec_id,
                pack.corpus_version,
                pack.retrieval_mode,
                Jsonb(pack_trace),
                pack.checksum,
            ),
        )
    for rank, span in enumerate(spans, 1):
        link_id = stable_id(f"evidence-pack:{item.number}:span:{span.database_id}")
        cursor.execute(
            """
            INSERT INTO evidence_pack_spans (
                id, tenant_id, evidence_pack_id, source_span_id, rank, excerpt
            ) VALUES (%s,%s,%s,%s,%s,%s)
            ON CONFLICT (id) DO NOTHING
            """,
            (link_id, tenant_id, pack_id, span.database_id, rank, span.text),
        )

    if not ensure_same(
        cursor,
        "question_candidates",
        candidate_row_id,
        {"content_checksum": candidate_checksum, "state": candidate_state},
    ):
        cursor.execute(
            """
            INSERT INTO question_candidates (
                id, tenant_id, course_id, question_spec_id, evidence_pack_id,
                candidate_key, format, content, generator_metadata, state, content_checksum
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                candidate_row_id,
                tenant_id,
                course_id,
                spec_id,
                pack_id,
                f"{BATCH_ID}-human-reviewed-v1",
                candidate.format,
                Jsonb(candidate_payload),
                Jsonb(
                    {
                        "authoring_method": "human-authored",
                        "provider": None,
                        "review_protocol_version": REVIEW_PROTOCOL_VERSION,
                        "source_manifest_ids": [span.manifest_id for span in spans],
                    }
                ),
                candidate_state,
                candidate_checksum,
            ),
        )

    warning = item.number == 22
    validation_findings = (
        [
            {
                "rule": "R3.2",
                "severity": "warning",
                "message": "Span 153 ký tự cần semantic review; review decision đã reject theo §2.2.",
            }
        ]
        if warning
        else []
    )
    validation_id = stable_id(f"validation:{item.number}:{VALIDATOR_VERSION}")
    cursor.execute(
        """
        INSERT INTO item_validations (
            id, tenant_id, question_candidate_id, validator_name, validator_version,
            status, score, findings, input_checksum
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (id) DO NOTHING
        """,
        (
            validation_id,
            tenant_id,
            candidate_row_id,
            VALIDATOR_NAME,
            VALIDATOR_VERSION,
            "warning" if warning else "passed",
            1.0,
            Jsonb(validation_findings),
            candidate_checksum,
        ),
    )

    decision_id = stable_id(f"review:{item.number}:{REVIEW_PROTOCOL_VERSION}")
    cursor.execute(
        """
        INSERT INTO review_decisions (
            id, tenant_id, question_candidate_id, reviewer_id, decision, reason_code, notes
        ) VALUES (%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (id) DO NOTHING
        """,
        (
            decision_id,
            tenant_id,
            candidate_row_id,
            reviewer_id,
            database_decision,
            outcome.reason_code,
            outcome.notes,
        ),
    )

    concept_names = TOPIC_TO_CONCEPTS.get(item.meta["topic"], ())
    for index, concept_name in enumerate(concept_names):
        active_name = ACTIVE_CONCEPT_ALIASES.get(concept_name, concept_name)
        concept_id = active_concepts.get(active_name)
        if concept_id is None:
            raise RuntimeError(f"Active concept {active_name!r} is missing for Q{item.number}")
        role = "primary" if index == 0 else "application"
        link_id = stable_id(f"question-concept:{item.number}:{active_name}:{role}")
        cursor.execute(
            """
            INSERT INTO question_concepts (
                id, tenant_id, question_candidate_id, concept_id, role
            ) VALUES (%s,%s,%s,%s,%s)
            ON CONFLICT (id) DO NOTHING
            """,
            (link_id, tenant_id, candidate_row_id, concept_id, role),
        )
    return not existed


def database_url_from_args(value: str | None) -> str:
    candidate = value or os.getenv("OPERATIONS_DATABASE_URL") or os.getenv("OPS_DATABASE_URL")
    if not candidate:
        raise RuntimeError(
            "An operations database URL is required via --database-url, "
            "OPERATIONS_DATABASE_URL, or OPS_DATABASE_URL"
        )
    return candidate.replace("postgresql+psycopg://", "postgresql://")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--review", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--spans", type=Path, default=DEFAULT_SPANS)
    parser.add_argument("--database-url")
    parser.add_argument("--tenant-slug", default=TENANT_SLUG)
    parser.add_argument("--course-slug", default=COURSE_SLUG)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source_text = args.source.read_text(encoding="utf-8")
    items = parse(source_text)
    if [item.number for item in items] != list(range(1, 101)):
        raise RuntimeError("Source snapshot must contain exactly Q1 through Q100")
    outcomes = load_review(args.review, {item.number for item in items})
    all_manifest_spans = load_spans(args.spans)
    wanted_manifest_ids = {span_id for item in items for span_id in item.span_ids}
    manifest_spans = {span_id: all_manifest_spans[span_id] for span_id in wanted_manifest_ids}
    corpus = json.loads(args.corpus.read_text(encoding="utf-8"))

    inserted = 0
    with psycopg.connect(database_url_from_args(args.database_url)) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM tenants WHERE slug=%s", (args.tenant_slug,))
            tenant_row = cursor.fetchone()
            if tenant_row is None:
                raise RuntimeError(f"Unknown tenant {args.tenant_slug!r}")
            tenant_id = tenant_row[0]
            cursor.execute("SELECT set_config('app.tenant_id', %s, true)", (str(tenant_id),))
            cursor.execute(
                "SELECT id FROM courses WHERE tenant_id=%s AND slug=%s",
                (tenant_id, args.course_slug),
            )
            course_row = cursor.fetchone()
            if course_row is None:
                raise RuntimeError(f"Unknown course {args.course_slug!r}")
            course_id = course_row[0]

            reviewer_id = stable_id("reviewer:question-reviewer@chiron.local")
            cursor.execute(
                """
                INSERT INTO users (id, email, password_hash, display_name, status)
                VALUES (%s,%s,%s,%s,'disabled')
                ON CONFLICT (id) DO NOTHING
                """,
                (
                    reviewer_id,
                    "question-reviewer@chiron.local",
                    "!disabled-system-identity",
                    "Question Bank Review Bot",
                ),
            )
            resolved = resolve_database_spans(cursor, manifest_spans, corpus)
            cursor.execute(
                """
                SELECT normalized_name, id
                FROM concept_nodes
                WHERE course_id=%s AND review_status='active'
                """,
                (course_id,),
            )
            active_concepts = dict(cursor.fetchall())

            for item in items:
                inserted += insert_snapshot(
                    cursor,
                    tenant_id=tenant_id,
                    course_id=course_id,
                    reviewer_id=reviewer_id,
                    item=item,
                    outcome=outcomes[item.number],
                    spans=[resolved[span_id] for span_id in item.span_ids],
                    active_concepts=active_concepts,
                )

            cursor.execute(
                """
                SELECT qc.state, rd.decision, count(*)
                FROM question_candidates qc
                JOIN review_decisions rd ON rd.question_candidate_id=qc.id
                JOIN question_specs qs ON qs.id=qc.question_spec_id
                WHERE qs.tenant_id=%s AND qs.course_id=%s
                  AND qs.external_id LIKE 'qs-question-bank-v1-%%'
                GROUP BY qc.state, rd.decision
                ORDER BY qc.state, rd.decision
                """,
                (tenant_id, course_id),
            )
            reconciliation = [
                {"candidate_state": state, "decision": decision, "count": count}
                for state, decision, count in cursor.fetchall()
            ]
            if sum(row["count"] for row in reconciliation) != 100:
                raise RuntimeError(f"Post-import reconciliation is not 100 rows: {reconciliation}")
            cursor.execute(
                """
                SELECT count(DISTINCT eps.source_span_id)
                FROM evidence_pack_spans eps
                JOIN evidence_packs ep ON ep.id=eps.evidence_pack_id
                JOIN question_specs qs ON qs.id=ep.question_spec_id
                WHERE qs.tenant_id=%s AND qs.course_id=%s
                  AND qs.external_id LIKE 'qs-question-bank-v1-%%'
                """,
                (tenant_id, course_id),
            )
            database_span_count = cursor.fetchone()[0]
        if args.dry_run:
            connection.rollback()
        else:
            connection.commit()

    print(
        json.dumps(
            {
                "batch": BATCH_ID,
                "inserted_specs": inserted,
                "already_present_specs": 100 - inserted,
                "manifest_spans": len(manifest_spans),
                "database_spans": database_span_count,
                "reconciliation": reconciliation,
                "dry_run": args.dry_run,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
