from __future__ import annotations

from app.ingestion.chunking import child_chunks, estimate_tokens, hierarchical_chunks


def test_hierarchical_chunking_keeps_parent_and_bounded_children() -> None:
    paragraphs = [
        f"Phần {index}. Đây là nội dung giải thích có quan hệ nhân quả và citation nguồn. " * 18
        for index in range(1, 9)
    ]
    source = "\n\n".join(paragraphs)
    drafts = hierarchical_chunks(source, target_tokens=120, max_tokens=170, overlap_tokens=25)

    assert drafts[0].chunk_type == "parent"
    assert drafts[0].content == source.strip()
    children = drafts[1:]
    assert len(children) > 2
    assert [chunk.ordinal for chunk in children] == list(range(1, len(children) + 1))
    assert all(chunk.chunk_type == "child" for chunk in children)
    assert all(chunk.token_count <= 170 for chunk in children)
    assert all(chunk.content.strip() for chunk in children)


def test_child_overlap_repeats_boundary_evidence_without_empty_chunks() -> None:
    source = "\n\n".join(
        f"Evidence {index}: " + ("retrieval grounding production " * 24)
        for index in range(1, 7)
    )
    children = child_chunks(source, target_tokens=100, max_tokens=140, overlap_tokens=20)

    assert len(children) >= 3
    assert all(estimate_tokens(chunk) <= 140 for chunk in children)
    boundaries = [set(children[index].split()) & set(children[index + 1].split()) for index in range(len(children) - 1)]
    assert all(boundary for boundary in boundaries)


def test_empty_span_creates_no_chunks() -> None:
    assert hierarchical_chunks("  \n\n ") == []


def test_invalid_chunk_budget_is_rejected() -> None:
    try:
        child_chunks("content", target_tokens=100, max_tokens=80, overlap_tokens=20)
    except ValueError as exc:
        assert "overlap < target <= max" in str(exc)
    else:
        raise AssertionError("Invalid chunk budget must raise ValueError")
