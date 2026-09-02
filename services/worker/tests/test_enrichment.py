from hashlib import sha256

import pytest

from chiron_worker.enrichment import (
    ENRICHMENT_VERSION,
    blend_dense_vectors,
    enrich_chunk,
    validate_enriched_payload,
)


def sample_chunk() -> dict:
    content = "RAG là Retrieval Augmented Generation. So với fine-tuning, RAG truy xuất nguồn ngoài."
    return {
        "content": content,
        "checksum": sha256(content.encode()).hexdigest(),
        "course_title": "AI In Action",
        "document_title": "RAG Pipeline",
        "source_type": "course_pdf",
        "locator": {"label": "Slide 12", "section_title": "RAG và Fine-tuning"},
    }


def test_context_enrichment_preserves_raw_content_and_citation_checksum() -> None:
    chunk = sample_chunk()
    result = enrich_chunk(chunk, variant="context")

    assert result.raw_content == chunk["content"]
    assert result.raw_checksum == chunk["checksum"]
    assert result.retrieval_text.endswith(f"[CONTENT]\n{chunk['content']}")
    assert "[SECTION] RAG và Fine-tuning > Slide 12" in result.retrieval_text
    assert result.contextualized is True
    assert result.estimated_retrieval_tokens <= 500
    assert result.aliases == ()


def test_term_and_pedagogy_enrichment_is_deterministic_and_provenanced() -> None:
    first = enrich_chunk(sample_chunk(), variant="context_terms_pedagogy")
    second = enrich_chunk(sample_chunk(), variant="context_terms_pedagogy")

    assert first == second
    assert first.enrichment_version == ENRICHMENT_VERSION
    assert "retrieval augmented generation = RAG" in first.aliases
    assert "RAG" in first.entities
    assert "comparison" in first.pedagogy_labels
    assert "curated_alias_glossary_v1" in first.provenance
    assert first.retrieval_text_checksum == sha256(first.retrieval_text.encode()).hexdigest()


def test_long_chunk_keeps_raw_embedding_text_instead_of_losing_tail_to_context() -> None:
    chunk = sample_chunk()
    chunk["content"] = "nội dung " * 900
    chunk["token_count"] = 700
    result = enrich_chunk(chunk, variant="context_terms_pedagogy")

    assert result.contextualized is False
    assert result.estimated_header_tokens == 0
    assert result.retrieval_text == chunk["content"]
    assert result.context_text == ""


def test_untrusted_control_characters_are_removed_from_context_only() -> None:
    chunk = sample_chunk()
    chunk["document_title"] = "RAG\x00 Pipeline"
    result = enrich_chunk(chunk, variant="context")

    assert "\x00" not in result.retrieval_text
    assert result.raw_content == chunk["content"]


def test_unknown_variant_fails_closed() -> None:
    with pytest.raises(ValueError, match="Unsupported enrichment variant"):
        enrich_chunk(sample_chunk(), variant="synthetic")  # type: ignore[arg-type]


def test_payload_integrity_detects_citation_and_retrieval_tampering() -> None:
    chunk = sample_chunk()
    result = enrich_chunk(chunk, variant="context_terms_pedagogy")
    expected = {
        "tenant_id": "tenant-1",
        "course_id": "course-1",
        "source_span_id": "span-1",
        "content": chunk["content"],
        "checksum": chunk["checksum"],
    }
    payload = {
        **expected,
        "raw_checksum": chunk["checksum"],
        "retrieval_text": result.retrieval_text,
        "retrieval_text_checksum": result.retrieval_text_checksum,
        "enrichment_version": result.enrichment_version,
        "enrichment_provenance": list(result.provenance),
    }
    assert validate_enriched_payload(payload, expected) == []

    payload["content"] = "tampered"
    payload["retrieval_text_checksum"] = "bad"
    expected["retrieval_text_checksum"] = result.retrieval_text_checksum
    assert validate_enriched_payload(payload, expected) == [
        "raw_content_mismatch",
        "retrieval_text_checksum_mismatch",
    ]


def test_dense_blend_is_normalized_and_validates_dimensions() -> None:
    blended = blend_dense_vectors([1.0, 0.0], [0.0, 1.0], 0.25)
    assert sum(value * value for value in blended) == pytest.approx(1.0)
    assert blended[0] > blended[1]

    with pytest.raises(ValueError, match="same non-zero dimensions"):
        blend_dense_vectors([1.0], [1.0, 2.0], 0.2)
