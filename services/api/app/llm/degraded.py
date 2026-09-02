from uuid import uuid4

from ..schemas import RetrievalResponse, TutorAnswer


def build_degraded_tutor_answer(
    retrieval: RetrievalResponse,
    *,
    reason: str,
) -> TutorAnswer:
    hits = retrieval.hits[:3]
    source_lines = [f"- {hit.citation.title}, {hit.citation.locator}: {hit.text}" for hit in hits]
    answer = (
        "AI giải thích đang tạm thời không khả dụng. Bạn vẫn có thể học từ các nguồn "
        "đã truy xuất và kiểm chứng dưới đây:\n" + "\n".join(source_lines)
    )
    return TutorAnswer(
        answer=answer,
        confidence=hits[0].score if hits else 0,
        citations=[hit.citation for hit in hits],
        trace_id=uuid4(),
        provider="retrieval-only",
        model=None,
        used_fallback=True,
        fallback_reason=reason,
        degraded=True,
    )
