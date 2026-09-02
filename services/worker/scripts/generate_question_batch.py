"""Fan-out generation of question-bank candidates from the course blueprint.

Pipeline per wave:

    BlueprintCompiler -> question_specs
      -> evidence pack from curated concept spans -> evidence_packs
      -> Groq fan-out (generation_count variants) -> question_candidates
      -> validate_candidate -> item_validations

Every write is idempotent against the table's unique constraint, so a rerun after
a crash resumes instead of duplicating. Candidates are never auto-approved: they
land in state 'validator_passed' or 'rejected' for QUESTION_REVIEW_PROTOCOL.md.

    python scripts/generate_question_batch.py --forms 1 --limit 20 --dry-run
    python scripts/generate_question_batch.py --forms 3 --variants 3
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from hashlib import sha256
from pathlib import Path
from uuid import uuid4

import httpx
import psycopg
from psycopg.types.json import Jsonb

from chiron_worker.blueprint import Concept, compile_specs, load_course_spec, quota_report
from chiron_worker.question_bank import (
    ClaimEvidence,
    EvidencePack,
    Option,
    QuestionCandidate,
    QuestionSpec,
    build_evidence_pack,
    validate_candidate,
)

ROOT = Path(__file__).resolve().parents[3]
COURSE_SPEC = ROOT / "data" / "courses" / "rag-intensive" / "course-spec-v1.yaml"
CONTRACT = ROOT / "docs" / "QUESTION_AUTHORING_CONTRACT.md"
TENANT_SLUG = "chiron-demo"
COURSE_SLUG = "rag-intensive"
CORPUS_VERSION = "corpus-2026-08-30"
VALIDATOR_NAME = "question_bank.validate_candidate"
VALIDATOR_VERSION = "question-bank-contract-v2"

# Rút từ docs/QUESTION_AUTHORING_CONTRACT.md. Sửa contract thì sửa cả đây.
SYSTEM_PROMPT = """You are a Vietnamese assessment author for an AI engineering course.

HARD RULES — an item breaking any of these is rejected:
1. Use ONLY the supplied evidence. Never add facts from your own knowledge. Every
   technical claim must be traceable to a supplied source span.
2. Objective items have EXACTLY four options (A, B, C, D) and EXACTLY one correct option.
3. Every distractor must be something a half-learned student would really pick.
   BANNED: absurd options ("disable monitoring", "log secrets", "retry forever",
   "infinite context"), and options that are off-topic for the stem.
4. At least one distractor must be a REAL technique taught in the course that is
   correct in a different situation but does not solve the stem's problem.
5. If the evidence names a misconception ("many people think X, actually Y"),
   make X a distractor. This is the highest-value distractor available.
6. No formal cues. The correct option must not be the longest, the most detailed,
   nor the only one written in a polished multi-clause style. Keep all four options
   within a similar length. Vary which letter is correct.
7. The stem must not contain citations, and must not leak the answer by wording.
8. The rationale explains WHY EACH DISTRACTOR IS WRONG. It must not restate the answer.
9. Every option carries a `misconception` field naming the specific wrong belief it
   encodes; for the correct option state why it is right.

Write natural Vietnamese, keeping established English technical terms.
Return valid JSON only, no markdown."""

OBJECTIVE_SCHEMA = {
    "name": "question_candidates",
    "schema": {
        "type": "object",
        "properties": {
            "questions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "variant": {"type": "integer"},
                        "stem": {"type": "string", "description": "Question stem in Vietnamese, no citations."},
                        "options": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string", "description": "Exactly one of A, B, C, D."},
                                    "text": {"type": "string", "description": "Option text in Vietnamese."},
                                    "authoring_note": {
                                        "type": "string",
                                        "description": (
                                            "REQUIRED for EVERY option including the correct one; never empty, "
                                            "at least 8 characters. Distractor: name the wrong belief that makes "
                                            "a student pick it. Correct option: say why it is right."
                                        ),
                                    },
                                },
                                "required": ["id", "text", "authoring_note"],
                                "additionalProperties": False,
                            },
                        },
                        "correct_option_ids": {
                            "type": "array", "items": {"type": "string"},
                            "description": "Exactly one element: the id of the single correct option.",
                        },
                        "rationale": {"type": "string"},
                        "difficulty_rationale": {"type": "string"},
                        "claim_to_evidence": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "claim": {"type": "string"},
                                    "source_span_ids": {"type": "array", "items": {"type": "string"}},
                                },
                                "required": ["claim", "source_span_ids"],
                                "additionalProperties": False,
                            },
                        },
                    },
                    "required": [
                        "variant", "stem", "options", "correct_option_ids",
                        "rationale", "difficulty_rationale", "claim_to_evidence",
                    ],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["questions"],
        "additionalProperties": False,
    },
}

CONSTRUCTED_SCHEMA = {
    "name": "constructed_candidates",
    "schema": {
        "type": "object",
        "properties": {
            "questions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "variant": {"type": "integer"},
                        "stem": {"type": "string"},
                        "rationale": {"type": "string"},
                        "difficulty_rationale": {"type": "string"},
                        "rubric": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string"},
                                    "label": {"type": "string"},
                                    "max_score": {"type": "integer"},
                                    "observable_evidence": {"type": "array", "items": {"type": "string"}},
                                    "common_failure_modes": {"type": "array", "items": {"type": "string"}},
                                },
                                "required": [
                                    "id", "label", "max_score",
                                    "observable_evidence", "common_failure_modes",
                                ],
                                "additionalProperties": False,
                            },
                        },
                        "acceptable_alternatives": {"type": "array", "items": {"type": "string"}},
                        "claim_to_evidence": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "claim": {"type": "string"},
                                    "source_span_ids": {"type": "array", "items": {"type": "string"}},
                                },
                                "required": ["claim", "source_span_ids"],
                                "additionalProperties": False,
                            },
                        },
                    },
                    "required": [
                        "variant", "stem", "rationale", "difficulty_rationale",
                        "rubric", "acceptable_alternatives", "claim_to_evidence",
                    ],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["questions"],
        "additionalProperties": False,
    },
}


def load_env() -> None:
    env = ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


class ConceptSpanRetriever:
    """Retriever backed by the curated concept -> source-span mapping.

    ponytail: curated mapping instead of Qdrant hybrid search. It is deterministic
    and needs no dense encoder; swap in HybridRetriever when evidence packs must
    follow the live index.
    """

    def __init__(self, spans_by_concept: dict[str, list[dict]]) -> None:
        self._spans = spans_by_concept
        self.concept: str = ""

    def retrieve(self, query: str, **scope: object) -> dict:
        limit = int(scope.get("limit", 3) or 3)
        hits = [
            {"payload": payload}
            for payload in self._spans.get(self.concept, [])[:limit]
        ]
        return {"hits": hits, "retrieval_mode": "curated_concept_spans"}


def fetch_concepts(cursor) -> tuple[list[Concept], dict[str, list[dict]]]:
    cursor.execute(
        """
        SELECT cn.normalized_name, cn.summary, s.id::text, s.text, dv.title, s.locator
        FROM chunk_concepts cc
        JOIN concept_nodes cn ON cn.id = cc.concept_id
        JOIN source_spans s
          ON s.id = COALESCE(cc.evidence_source_span_id,
                             (SELECT source_span_id FROM chunks WHERE id = cc.chunk_id))
        JOIN document_versions dv ON dv.id = s.document_version_id
        WHERE cn.review_status = 'approved' AND cn.summary IS NOT NULL
        ORDER BY cn.normalized_name, length(s.text) DESC
        """
    )
    concepts: dict[str, Concept] = {}
    spans: dict[str, list[dict]] = {}
    for name, summary, span_id, text, title, locator in cursor.fetchall():
        concepts.setdefault(name, Concept(name, summary))
        spans.setdefault(name, []).append(
            {
                "source_span_id": span_id,
                "content": text.strip(),
                "document_title": title or "Untitled source",
                "locator": json.dumps(locator, ensure_ascii=False) if locator else "corpus",
            }
        )
    ordered = [concepts[name] for name in sorted(concepts)]
    return ordered, spans


PROVIDERS = {
    "groq": {
        "base_url_env": "GROQ_BASE_URL",
        "base_url_default": "https://api.groq.com/openai/v1",
        "key_env": "GROQ_API_KEY",
        "model_default": "openai/gpt-oss-20b",
        "strict_schema": False,
    },
    "openai": {
        "base_url_env": "OPENAI_BASE_URL",
        "base_url_default": "https://api.openai.com/v1",
        "key_env": "OPENAI_API_KEY",
        "model_default": "gpt-4o-mini",
        "strict_schema": True,
    },
}

_DURATION = re.compile(r"(\d+(?:\.\d+)?)(ms|s|m|h)")
_UNIT_SECONDS = {"ms": 0.001, "s": 1.0, "m": 60.0, "h": 3600.0}


def _reset_seconds(value: str | None) -> float:
    """Parse rate-limit reset windows: '21.067s', '12m57.599s', '6ms', '1h2m'."""
    if not value:
        return 0.0
    total = 0.0
    for amount, unit in _DURATION.findall(value.strip()):
        total += float(amount) * _UNIT_SECONDS[unit]
    return total


class TokenBudget:
    """Pace requests against Groq's tokens-per-minute window.

    Groq counts `max_tokens` against TPM at admission, so a request whose
    input + max_tokens exceeds the window is rejected outright (413/429) no
    matter how short the real completion turns out to be.
    """

    def __init__(self, max_tokens: int) -> None:
        self.max_tokens = max_tokens
        self.remaining: int | None = None
        self.reset_in = 0.0

    def wait_if_needed(self, estimated_input: int) -> None:
        need = estimated_input + self.max_tokens
        if self.remaining is not None and self.remaining < need and self.reset_in > 0:
            print(f"  [tpm] còn {self.remaining} token, cần {need} — chờ {self.reset_in:.0f}s", flush=True)
            time.sleep(self.reset_in + 1)
            self.remaining = None

    def observe(self, headers) -> None:
        try:
            self.remaining = int(headers.get("x-ratelimit-remaining-tokens", ""))
        except ValueError:
            self.remaining = None
        self.reset_in = _reset_seconds(headers.get("x-ratelimit-reset-tokens"))


def call_llm(system: str, user: str, schema: dict, model: str, provider: str,
             budget: TokenBudget, retries: int = 4) -> list[dict]:
    config = PROVIDERS[provider]
    # OpenAI structured outputs only guarantee the shape when strict is set.
    json_schema = {**schema, "strict": True} if config["strict_schema"] else schema
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.4,
        "max_tokens": budget.max_tokens,
        "response_format": {"type": "json_schema", "json_schema": json_schema},
    }
    # ~3 chars per token for Vietnamese + JSON; deliberately pessimistic.
    estimated_input = (len(system) + len(user)) // 3
    last: Exception | None = None
    for attempt in range(retries):
        budget.wait_if_needed(estimated_input)
        try:
            response = httpx.post(
                f"{os.environ.get(config['base_url_env'], config['base_url_default'])}/chat/completions",
                headers={"Authorization": f"Bearer {os.environ[config['key_env']]}"},
                json=payload,
                timeout=180,
            )
            budget.observe(response.headers)
            if response.status_code in (413, 429):
                wait = _reset_seconds(response.headers.get("x-ratelimit-reset-tokens")) or 20.0
                last = RuntimeError(f"HTTP {response.status_code} (token window)")
                time.sleep(wait + 1)
                continue
            if response.status_code >= 400:
                raise RuntimeError(f"HTTP {response.status_code}: {response.text[:300]}")
            content = response.json()["choices"][0]["message"]["content"]
            return json.loads(content)["questions"]
        except Exception as exc:  # noqa: BLE001 - bounded retry, then give up on this spec
            last = exc
            time.sleep(2 ** attempt)
    raise RuntimeError(f"{provider} call failed after {retries} attempts: {last}")


def build_prompt(spec: QuestionSpec, pack: EvidencePack) -> str:
    evidence = [
        {
            "source_span_id": span.source_span_id,
            "document_title": span.document_title,
            "locator": span.locator,
            "text": span.excerpt[:1600],
        }
        for span in pack.spans
    ]
    task = "constructed response" if spec.is_constructed_response else "objective"
    shape = (
        "For each question return: variant, stem, rationale, difficulty_rationale, "
        "rubric (3-5 criteria; every criterion needs observable_evidence and "
        "common_failure_modes), acceptable_alternatives (solutions that reach the same "
        "properties by another route and must still score full marks), claim_to_evidence."
        if spec.is_constructed_response
        else "For each question return: variant, stem, options (exactly A/B/C/D, each with "
        "id, text and misconception), correct_option_ids (exactly one), rationale, "
        "difficulty_rationale, claim_to_evidence."
    )
    return f"""Write {spec.generation_count} DIFFERENT {task} questions in Vietnamese for this specification.

The variants must differ in scenario or in the misconception they probe. Do NOT paraphrase one stem {spec.generation_count} times.

Specification:
{json.dumps({
    "concept": spec.concept_ids,
    "learning_objective": spec.learning_objective,
    "format": spec.format,
    "cognitive_level": spec.cognitive_level,
    "difficulty_target": spec.difficulty_target,
    "misconception_target": spec.misconception_target,
    "scope": spec.scope,
}, ensure_ascii=False, indent=2)}

Evidence (the ONLY facts you may use; cite source_span_id verbatim):
{json.dumps(evidence, ensure_ascii=False, indent=2)}

{shape}
Return an object {{"questions": [...]}} with exactly {spec.generation_count} entries."""


def to_candidate(spec: QuestionSpec, raw: dict, variant: int, provider: str) -> QuestionCandidate:
    # provider is part of the key so the same spec can be regenerated on another
    # model without the old rows blocking the insert.
    return QuestionCandidate(
        candidate_id=f"qc-{spec.spec_id.removeprefix('qs-')}-{provider}-v{variant}",
        spec_id=spec.spec_id,
        format=spec.format,
        stem=raw["stem"].strip(),
        options=[
            Option(id=option["id"], text=option["text"],
                   misconception=option.get("authoring_note") or option.get("misconception") or "")
            for option in raw.get("options", [])
        ],
        correct_option_ids=raw.get("correct_option_ids", []),
        rationale=raw["rationale"].strip(),
        claim_to_evidence=[ClaimEvidence(**claim) for claim in raw["claim_to_evidence"]],
        difficulty_rationale=raw["difficulty_rationale"].strip(),
        rubric=raw.get("rubric", []),
        acceptable_alternatives=raw.get("acceptable_alternatives", []),
    )


def persist_spec(cursor, spec: QuestionSpec, tenant_id: str, course_id: str) -> str:
    checksum = sha256(spec.model_dump_json().encode("utf-8")).hexdigest()
    cursor.execute(
        """
        INSERT INTO question_specs (
            id, tenant_id, course_id, external_id, blueprint_cell, concept_slugs,
            learning_objective, format, cognitive_level, difficulty_target,
            misconception_target, required_evidence, generation_count, exposure_group,
            state, input_checksum
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (tenant_id, course_id, external_id) DO NOTHING
        RETURNING id
        """,
        (
            str(uuid4()), tenant_id, course_id, spec.spec_id,
            Jsonb({"scope": spec.scope, "format": spec.format,
                   "cognitive_level": spec.cognitive_level, "difficulty": spec.difficulty_target}),
            Jsonb(spec.concept_ids), spec.learning_objective, spec.format,
            spec.cognitive_level, spec.difficulty_target, spec.misconception_target,
            spec.required_evidence, spec.generation_count, spec.exposure_group,
            "ready", checksum,
        ),
    )
    row = cursor.fetchone()
    if row:
        return str(row[0])
    cursor.execute(
        "SELECT id FROM question_specs WHERE tenant_id=%s AND course_id=%s AND external_id=%s",
        (tenant_id, course_id, spec.spec_id),
    )
    return str(cursor.fetchone()[0])


def persist_pack(cursor, pack: EvidencePack, spec_row_id: str, tenant_id: str, course_id: str) -> str:
    cursor.execute(
        """
        INSERT INTO evidence_packs (
            id, tenant_id, course_id, question_spec_id, corpus_version,
            retrieval_mode, retrieval_trace, checksum, state
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (question_spec_id, checksum) DO NOTHING
        RETURNING id
        """,
        (
            str(uuid4()), tenant_id, course_id, spec_row_id, pack.corpus_version,
            pack.retrieval_mode,
            Jsonb({"spans": [s.source_span_id for s in pack.spans], "mode": pack.retrieval_mode}),
            pack.checksum, "frozen",
        ),
    )
    row = cursor.fetchone()
    if row is None:
        cursor.execute(
            "SELECT id FROM evidence_packs WHERE question_spec_id=%s AND checksum=%s",
            (spec_row_id, pack.checksum),
        )
        return str(cursor.fetchone()[0])
    pack_id = str(row[0])
    for span in pack.spans:
        cursor.execute(
            """
            INSERT INTO evidence_pack_spans (id, tenant_id, evidence_pack_id, source_span_id, rank, excerpt)
            VALUES (%s,%s,%s,%s,%s,%s)
            ON CONFLICT (evidence_pack_id, source_span_id) DO NOTHING
            """,
            (str(uuid4()), tenant_id, pack_id, span.source_span_id, span.rank, span.excerpt),
        )
    return pack_id


def persist_candidate(cursor, candidate: QuestionCandidate, result, *, tenant_id: str,
                      course_id: str, spec_row_id: str, pack_id: str, model: str) -> bool:
    content = candidate.model_dump(mode="json")
    checksum = sha256(json.dumps(content, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    cursor.execute(
        """
        INSERT INTO question_candidates (
            id, tenant_id, course_id, question_spec_id, evidence_pack_id, candidate_key,
            format, content, generator_metadata, state, content_checksum
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (question_spec_id, candidate_key) DO NOTHING
        RETURNING id
        """,
        (
            str(uuid4()), tenant_id, course_id, spec_row_id, pack_id, candidate.candidate_id,
            candidate.format, Jsonb(content),
            Jsonb({"provider": model.split(":", 1)[0], "model": model.split(":", 1)[-1],
                   "prompt_version": "authoring-contract-v1"}),
            "validator_passed" if result.passed else "rejected", checksum,
        ),
    )
    row = cursor.fetchone()
    if row is None:
        return False
    cursor.execute(
        """
        INSERT INTO item_validations (
            id, tenant_id, question_candidate_id, validator_name, validator_version,
            status, score, findings, input_checksum
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (question_candidate_id, validator_name, validator_version, input_checksum)
        DO NOTHING
        """,
        (
            str(uuid4()), tenant_id, str(row[0]), VALIDATOR_NAME, VALIDATOR_VERSION,
            "passed" if result.passed else "failed",
            1.0 if result.passed else 0.0,
            Jsonb([{"rule": f.rule, "message": f.message, "severity": f.severity}
                   for f in result.findings]),
            checksum,
        ),
    )
    return True


def main() -> int:
    load_env()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--forms", type=int, default=1, help="số form đề để nhân blueprint")
    parser.add_argument("--variants", type=int, default=3, help="số candidate mỗi spec")
    parser.add_argument("--limit", type=int, default=0, help="chỉ xử lý N spec đầu (0 = tất cả)")
    parser.add_argument("--wave-size", type=int, default=20)
    parser.add_argument("--max-tokens", type=int, default=5000,
                        help="ngân sách completion mỗi request; input + giá trị này phải lọt TPM")
    parser.add_argument("--dry-run", action="store_true", help="compile + evidence pack, không gọi LLM")
    parser.add_argument("--database-url", default=os.getenv("DATABASE_ADMIN_URL") or os.getenv("DATABASE_URL"))
    parser.add_argument("--provider", choices=sorted(PROVIDERS), default="openai")
    parser.add_argument("--model", default=None, help="mặc định theo provider")
    args = parser.parse_args()

    if not args.database_url:
        raise SystemExit("DATABASE_ADMIN_URL or DATABASE_URL is required")
    config = PROVIDERS[args.provider]
    model = args.model or config["model_default"]
    if not args.dry_run and not os.environ.get(config["key_env"]):
        raise SystemExit(f"{config['key_env']} is required (or use --dry-run)")

    course_spec = load_course_spec(COURSE_SPEC)
    url = args.database_url.replace("postgresql+psycopg://", "postgresql://", 1)
    stats = {"specs": 0, "packs": 0, "candidates": 0, "passed": 0, "failed": 0, "errors": 0}
    findings: dict[str, int] = {}

    with psycopg.connect(url) as connection, connection.cursor() as cursor:
        cursor.execute("SELECT id FROM tenants WHERE slug=%s", (TENANT_SLUG,))
        tenant = cursor.fetchone()
        cursor.execute("SELECT id FROM courses WHERE slug=%s", (COURSE_SLUG,))
        course = cursor.fetchone()
        if tenant is None or course is None:
            raise SystemExit("Seeded tenant/course missing — run the seed step first")
        tenant_id, course_id = str(tenant[0]), str(course[0])
        cursor.execute("SELECT set_config('app.tenant_id', %s, true)", (tenant_id,))

        concepts, spans_by_concept = fetch_concepts(cursor)
        if not concepts:
            raise SystemExit("No approved concepts with summaries — cannot compile a blueprint")
        specs = compile_specs(course_spec, concepts, forms=args.forms, generation_count=args.variants)
        if args.limit:
            specs = specs[: args.limit]
        print(json.dumps({"provider": args.provider, "model": model,
                          "concepts": len(concepts), "specs": len(specs),
                          "quota": quota_report(specs)}, ensure_ascii=False))

        budget = TokenBudget(args.max_tokens)
        retriever = ConceptSpanRetriever(spans_by_concept)
        for index, spec in enumerate(specs, 1):
            retriever.concept = spec.concept_ids[0]
            try:
                pack = build_evidence_pack(
                    spec, tenant_id=tenant_id, course_id=course_id,
                    corpus_version=CORPUS_VERSION, retriever=retriever,
                )
            except ValueError as exc:
                stats["errors"] += 1
                print(f"  skip {spec.spec_id}: {exc}", file=sys.stderr)
                continue

            spec_row_id = persist_spec(cursor, spec, tenant_id, course_id)
            pack_id = persist_pack(cursor, pack, spec_row_id, tenant_id, course_id)
            stats["specs"] += 1
            stats["packs"] += 1
            if args.dry_run:
                connection.commit()
                continue

            schema = CONSTRUCTED_SCHEMA if spec.is_constructed_response else OBJECTIVE_SCHEMA
            try:
                raw_items = call_llm(SYSTEM_PROMPT, build_prompt(spec, pack), schema,
                                     model, args.provider, budget)
            except RuntimeError as exc:
                stats["errors"] += 1
                print(f"  fail {spec.spec_id}: {exc}", file=sys.stderr)
                connection.commit()
                continue

            for variant, raw in enumerate(raw_items[: args.variants], 1):
                try:
                    candidate = to_candidate(spec, raw, variant, args.provider)
                except Exception as exc:  # noqa: BLE001 - malformed model output is data, not a crash
                    stats["errors"] += 1
                    findings["schema_parse"] = findings.get("schema_parse", 0) + 1
                    print(f"  bad shape {spec.spec_id} v{variant}: {exc}", file=sys.stderr)
                    continue
                result = validate_candidate(spec, pack, candidate)
                if persist_candidate(cursor, candidate, result, tenant_id=tenant_id,
                                     course_id=course_id, spec_row_id=spec_row_id,
                                     pack_id=pack_id, model=f"{args.provider}:{model}"):
                    stats["candidates"] += 1
                    stats["passed" if result.passed else "failed"] += 1
                    for finding in result.errors:
                        findings[finding.rule] = findings.get(finding.rule, 0) + 1

            connection.commit()
            if index % args.wave_size == 0:
                print(json.dumps({"progress": index, **stats}, ensure_ascii=False), flush=True)

        connection.commit()

    print(json.dumps({"done": True, **stats, "top_findings": dict(
        sorted(findings.items(), key=lambda kv: -kv[1])[:8])}, ensure_ascii=False))
    return 0 if stats["errors"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
