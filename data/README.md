# Chiron data corpus

This directory contains the auditable Markdown staging corpus for course `rag-intensive`.

## Layout

- `processed/markdown/slides/`: authoritative PDF decks, one Markdown file per binary source.
- `processed/markdown/lessons/`: authoritative interactive lesson HTML converted to semantic Markdown.
- `processed/assets/page-images/`: visual fallback for pages whose text layer and OCR remain sparse.
- `manifests/corpus.json`: document-level IDs, checksums, extraction metrics, and duplicate mapping.
- `manifests/source_spans.jsonl`: page/section records matching Chiron's `source_spans` persistence boundary.

## Ingestion invariants

- `document_version_id` and `source_span_id` are deterministic UUIDv5 values.
- Every source span has a locator and SHA-256 checksum.
- PDF page boundaries and HTML section boundaries are explicit in Markdown comments.
- Text-layer extraction is preferred. OCR mode for this run: `auto`.
- OCR never overwrites a richer text layer; it is selected only when it yields more text.
- Sparse visual pages retain a PNG reference in both Markdown and the source-span locator.
- OCR language data is stored under `ocr/tessdata/` for reproducible Vietnamese-English extraction.
- No LLM rewrites source text during parsing. Concept/relationship extraction is downstream and must retain source-span provenance.

## Current corpus

- Documents: 70
- Source spans: 2817
- Pages improved by OCR: 3
- Pages still sparse after text/OCR inspection: 7 (typically visual dividers or image-only pages; locators are retained)
