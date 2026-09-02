from __future__ import annotations

from collections.abc import Callable
from uuid import uuid4

from .schemas import LabDefinition, LabResult, LabSubmission

LAB_CONCEPT_ALIASES = {
    "reciprocal_rank_fusion": "hybrid_search_rrf",
    "metadata_filtering": "metadata_filtered_search",
    "rag_evaluation": "rag_evaluation",
    "multi_hop_retrieval": "graphrag_multi_hop",
}


def canonical_lab_concept_id(concept_id: str) -> str:
    """Map legacy lab IDs to the stable Knowledge Map concept IDs."""
    return LAB_CONCEPT_ALIASES.get(concept_id, concept_id)


def normalized_submission(payload: LabSubmission) -> tuple[dict, dict[str, str]]:
    configuration = dict(payload.configuration)
    legacy = {
        "dense_weight": payload.dense_weight,
        "sparse_weight": payload.sparse_weight,
        "rerank_depth": payload.rerank_depth,
        "tenant_filter": payload.tenant_filter,
    }
    for key, value in legacy.items():
        if value is not None:
            configuration.setdefault(key, value)
    answers = {key: value.strip() for key, value in payload.transfer_answers.items()}
    if payload.transfer_answer:
        answers.setdefault("reasoning", payload.transfer_answer.strip())
    return configuration, answers


def _number(configuration: dict, key: str, default: float = 0) -> float:
    value = configuration.get(key, default)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return default
    return float(value)


def _enabled(configuration: dict, key: str) -> bool:
    return configuration.get(key) is True


def _choice(configuration: dict, key: str) -> str:
    value = configuration.get(key, "")
    return str(value).casefold()


def _covers(answer: str, groups: tuple[tuple[str, ...], ...]) -> bool:
    normalized = answer.casefold()
    return all(any(term.casefold() in normalized for term in group) for group in groups)


def _add(
    passed: bool,
    points: int,
    message: str,
    score_and_feedback: tuple[int, list[str]],
) -> tuple[int, list[str]]:
    score, feedback = score_and_feedback
    if passed:
        return score + points, feedback
    feedback.append(message)
    return score, feedback


def _hybrid(configuration: dict, answers: dict[str, str]) -> tuple[int, list[str]]:
    result: tuple[int, list[str]] = (0, [])
    result = _add(
        _enabled(configuration, "tenant_filter"),
        30,
        "Bật tenant filter trước retrieval để tránh rò rỉ dữ liệu chéo.",
        result,
    )
    weights = _number(configuration, "dense_weight") + _number(configuration, "sparse_weight")
    result = _add(
        abs(weights - 1) <= 0.05,
        25,
        "Hai trọng số fusion nên có tổng xấp xỉ 1.",
        result,
    )
    depth = _number(configuration, "rerank_depth")
    result = _add(
        10 <= depth <= 40,
        25,
        "Rerank depth 10 đến 40 cân bằng tốt hơn cho scenario này.",
        result,
    )
    result = _add(
        _covers(answers.get("reasoning", ""), (("rank", "thứ hạng"), ("raw score", "thang đo", "score"))),
        20,
        "Giải thích transfer cần phân biệt rank với raw score khác thang đo.",
        result,
    )
    return result


def _chunking(configuration: dict, answers: dict[str, str]) -> tuple[int, list[str]]:
    result: tuple[int, list[str]] = (0, [])
    result = _add(
        _choice(configuration, "strategy") in {"hierarchical", "parent-child"},
        25,
        "Chọn hierarchical hoặc parent-child để giữ ngữ cảnh cấu trúc.",
        result,
    )
    size = _number(configuration, "chunk_size")
    overlap = _number(configuration, "overlap")
    result = _add(400 <= size <= 800, 20, "Chunk size nên nằm trong khoảng 400 đến 800 token.", result)
    result = _add(
        40 <= overlap <= 120 and overlap <= size * 0.25,
        15,
        "Overlap cần đủ nối ngữ cảnh nhưng không vượt 25% chunk size.",
        result,
    )
    result = _add(
        _enabled(configuration, "preserve_locators"),
        20,
        "Phải giữ locator của source span qua mọi cấp chunk.",
        result,
    )
    result = _add(
        _covers(answers.get("boundary", ""), (("heading", "section", "ranh giới"), ("citation", "locator", "source"))),
        20,
        "Transfer check cần nối boundary theo section với citation hoặc locator ổn định.",
        result,
    )
    return result


def _rrf(configuration: dict, answers: dict[str, str]) -> tuple[int, list[str]]:
    result: tuple[int, list[str]] = (0, [])
    result = _add(_choice(configuration, "fusion") == "rrf", 25, "Dùng RRF để hợp nhất theo thứ hạng.", result)
    k = _number(configuration, "rrf_k")
    result = _add(40 <= k <= 80, 20, "RRF k nên nằm trong khoảng ổn định 40 đến 80.", result)
    depth = _number(configuration, "candidate_depth")
    result = _add(10 <= depth <= 30, 20, "Candidate depth nên nằm trong khoảng 10 đến 30.", result)
    result = _add(
        _covers(answers.get("reasoning", ""), (("rank", "thứ hạng"), ("incompatible", "khác thang", "raw score"))),
        20,
        "Hãy giải thích vì sao raw score giữa retriever không thể so trực tiếp.",
        result,
    )
    result = _add(
        _covers(answers.get("failure", ""), (("rare", "hiếm", "exact"), ("sparse", "bm25", "lexical"))),
        15,
        "Failure transfer cần nêu vai trò sparse/BM25 với exact term hiếm.",
        result,
    )
    return result


def _metadata(configuration: dict, answers: dict[str, str]) -> tuple[int, list[str]]:
    result: tuple[int, list[str]] = (0, [])
    result = _add(_enabled(configuration, "tenant_filter"), 30, "Thiếu tenant filter bắt buộc.", result)
    result = _add(_enabled(configuration, "course_filter"), 20, "Thiếu course filter cho enrollment hiện tại.", result)
    result = _add(_choice(configuration, "filter_stage") == "pre", 20, "Authorization filter phải chạy trước retrieval.", result)
    result = _add(
        _covers(answers.get("isolation", ""), (("tenant", "authorization", "phân quyền"), ("leak", "rò", "chéo"))),
        20,
        "Giải thích cần chỉ ra tenant authorization ngăn rò rỉ chéo.",
        result,
    )
    result = _add(
        _covers(answers.get("recall", ""), (("pre-filter", "payload", "filter"), ("candidate", "recall", "top-k"))),
        10,
        "Transfer check cần mô tả ảnh hưởng của pre-filter lên candidate recall.",
        result,
    )
    return result


def _evaluation(configuration: dict, answers: dict[str, str]) -> tuple[int, list[str]]:
    result: tuple[int, list[str]] = (0, [])
    result = _add(_number(configuration, "faithfulness_gate") >= 0.8, 20, "Faithfulness gate phải ít nhất 0.80.", result)
    result = _add(_number(configuration, "context_recall_gate") >= 0.75, 20, "Context recall gate phải ít nhất 0.75.", result)
    result = _add(_enabled(configuration, "verify_citations"), 20, "Bật citation verification độc lập.", result)
    result = _add(_enabled(configuration, "persist_regression"), 15, "Failure cần được lưu thành regression case có version.", result)
    result = _add(
        _covers(answers.get("diagnosis", ""), (("retrieval", "context recall"), ("generation", "faithfulness", "citation"))),
        15,
        "Diagnosis phải tách lỗi retrieval khỏi lỗi generation hoặc faithfulness.",
        result,
    )
    result = _add(
        _covers(answers.get("gate", ""), (("holdout", "golden", "regression"), ("release", "gate", "baseline"))),
        10,
        "Release gate cần so với golden/holdout baseline.",
        result,
    )
    return result


def _graph(configuration: dict, answers: dict[str, str]) -> tuple[int, list[str]]:
    result: tuple[int, list[str]] = (0, [])
    result = _add(_choice(configuration, "routing") == "adaptive", 20, "Chỉ mở graph theo intent bằng adaptive routing.", result)
    hops = _number(configuration, "max_hops")
    result = _add(hops in {1, 2}, 20, "Traversal phải bounded ở 1 hoặc 2 hop.", result)
    expansion = _number(configuration, "expansion_limit")
    result = _add(4 <= expansion <= 10, 15, "Expansion limit nên nằm trong khoảng 4 đến 10.", result)
    result = _add(_enabled(configuration, "direct_fallback"), 20, "Direct facts cần giữ hybrid-only fallback.", result)
    result = _add(
        _covers(answers.get("routing", ""), (("multi-hop", "prerequisite", "quan hệ"), ("intent", "route", "định tuyến"))),
        15,
        "Transfer check cần nối query intent với prerequisite hoặc multi-hop routing.",
        result,
    )
    result = _add(
        _covers(answers.get("regression", ""), (("direct", "fact"), ("regression", "baseline", "không giảm"))),
        10,
        "Hãy nêu gate bảo vệ direct-fact retrieval khỏi regression.",
        result,
    )
    return result


SCORERS: dict[str, Callable[[dict, dict[str, str]], tuple[int, list[str]]]] = {
    "hybrid-search": _hybrid,
    "chunking-strategy": _chunking,
    "rrf-ranking": _rrf,
    "metadata-filtering": _metadata,
    "rag-evaluation": _evaluation,
    "graph-lite-routing": _graph,
}


def score_lab(lab: LabDefinition, payload: LabSubmission) -> LabResult:
    try:
        scorer = SCORERS[lab.id]
    except KeyError as exc:
        raise LookupError("Lab scorer not found") from exc
    configuration, answers = normalized_submission(payload)
    score, feedback = scorer(configuration, answers)
    if score == 100:
        feedback.append("Bạn đã vượt toàn bộ guardrail và transfer checks của scenario.")
    return LabResult(
        score=score,
        passed=score >= lab.success_threshold,
        feedback=feedback,
        evidence_event_id=uuid4(),
    )
