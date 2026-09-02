import pytest

from chiron_worker.question_bank import (
    EvidencePack,
    EvidenceSpan,
    Option,
    QuestionCandidate,
    QuestionSpec,
    build_evidence_pack,
    validate_candidate,
)


def _spec(**overrides):
    values = {
        "spec_id": "qs-rag-apply-medium-001",
        "course_id": "rag-intensive",
        "concept_ids": ["retrieval"],
        "learning_objective": "Chọn retrieval strategy có citation phù hợp.",
        "scope": "track-3.ai-application",
        "format": "single_choice",
        "cognitive_level": "apply",
        "difficulty_target": "medium",
        "misconception_target": "Nhầm nhiều chunks với groundedness.",
        "required_evidence": 1,
        "exposure_group": "form-a",
    }
    values.update(overrides)
    return QuestionSpec(**values)


def _pack():
    return EvidencePack(
        spec_id="qs-rag-apply-medium-001",
        tenant_id="tenant",
        course_id="course",
        corpus_version="corpus-v1",
        retrieval_mode="hybrid",
        spans=[
            EvidenceSpan(
                source_span_id="span-1",
                document_title="RAG",
                locator="slide 4",
                excerpt="Citation links an answer to evidence and makes verification possible.",
                rank=1,
            )
        ],
    )


def _candidate(**overrides):
    values = {
        "candidate_id": "qc-rag-001",
        "spec_id": "qs-rag-apply-medium-001",
        "format": "single_choice",
        "stem": "Một trợ lý cần giúp người dùng kiểm chứng câu trả lời. Cách nào phù hợp nhất?",
        "options": [
            Option(id="A", text="Tăng top-k vô hạn", misconception="quantity"),
            Option(id="B", text="Trả lời kèm citation đến evidence", misconception="correct"),
            Option(id="C", text="Bỏ nguồn để câu trả lời ngắn", misconception="brevity"),
            Option(id="D", text="Dùng temperature cao", misconception="creativity"),
        ],
        "correct_option_ids": ["B"],
        "rationale": "Citation giúp đối chiếu câu trả lời với evidence.",
        "claim_to_evidence": [
            {"claim": "Citation enables verification", "source_span_ids": ["span-1"]}
        ],
        "difficulty_rationale": "Đòi hỏi áp dụng mục tiêu groundedness vào tình huống.",
    }
    values.update(overrides)
    return QuestionCandidate(**values)


def test_objective_candidate_requires_valid_key_and_evidence() -> None:
    assert validate_candidate(_spec(), _pack(), _candidate()).passed
    invalid = _candidate(correct_option_ids=["A", "B"])
    result = validate_candidate(_spec(), _pack(), invalid)
    assert not result.passed
    assert {item.rule for item in result.errors} == {"objective_exactly_one"}


def test_ordering_objective_uses_four_a_to_d_options_and_one_key() -> None:
    spec = _spec(format="ordering_or_matching")
    candidate = _candidate(
        format="ordering_or_matching",
        correct_option_ids=["A", "B"],
        options=_candidate().options + [Option(id="E", text="Option thừa", misconception="extra")],
    )
    rules = {item.rule for item in validate_candidate(spec, _pack(), candidate).errors}
    assert {"objective_option_count", "objective_option_labels", "objective_exactly_one"}.issubset(rules)


def test_candidate_cannot_cite_source_outside_snapshot() -> None:
    invalid = _candidate(
        claim_to_evidence=[{"claim": "Unsupported claim", "source_span_ids": ["other"]}]
    )
    assert not validate_candidate(_spec(), _pack(), invalid).passed


def test_constructed_response_requires_versioned_rubric() -> None:
    spec = _spec(format="system_design")
    candidate = _candidate(
        format="system_design",
        options=[],
        correct_option_ids=[],
        rubric=[],
        acceptable_alternatives=[],
    )
    rules = {item.rule for item in validate_candidate(spec, _pack(), candidate).errors}
    assert {"cr_rubric", "cr_alternatives"}.issubset(rules)


class FakeRetriever:
    def retrieve(self, _query, **_scope):
        return {
            "retrieval_mode": "hybrid",
            "hits": [
                {"payload": {"source_span_id": "span-1", "content": "x" * 30, "document_title": "A", "locator": "p1"}},
                {"payload": {"source_span_id": "span-1", "content": "duplicate" * 8}},
                {"payload": {"source_span_id": "span-2", "content": "y" * 30, "document_title": "B", "locator": "p2"}},
            ],
        }


class InsufficientRetriever:
    def retrieve(self, _query, **_scope):
        return {"hits": []}


def test_evidence_pack_snapshots_deduplicated_retrieval() -> None:
    pack = build_evidence_pack(
        _spec(required_evidence=2),
        tenant_id="tenant",
        course_id="course",
        corpus_version="corpus-v1",
        retriever=FakeRetriever(),
    )
    assert [span.source_span_id for span in pack.spans] == ["span-1", "span-2"]
    assert len(pack.checksum) == 64


def test_evidence_pack_fails_closed_when_retrieval_is_insufficient() -> None:
    with pytest.raises(ValueError, match="requires 2"):
        build_evidence_pack(
            _spec(required_evidence=2),
            tenant_id="tenant",
            course_id="course",
            corpus_version="corpus-v1",
            retriever=InsufficientRetriever(),
        )
