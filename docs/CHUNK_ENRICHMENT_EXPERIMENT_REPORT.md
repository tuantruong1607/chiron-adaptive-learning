# Chiron AI — Chunk Enrichment Experiment Report

> **Ngày chạy:** 2026-08-30  
> **Trạng thái:** COMPLETED — QUALITY GATE NOT PASSED  
> **Quyết định:** Không cutover. `chiron_chunks_v1` tiếp tục là retrieval collection active.

## 1. Kết quả ngắn gọn

Chunk enrichment đã được implement, index local và kiểm thử trên toàn bộ `5,070` active child chunks. Tất cả experiment collection cuối đều qua kiểm tra tenant/citation/checksum với `5,070/5,070` PostgreSQL matches và `0` violation.

Tuy nhiên không biến thể nào cải thiện đồng thời recall, ranking quality và latency:

- Dense context blending `weight=0.20` gây regression lớn, bị loại.
- Dense raw + aliases/entities/pedagogy BM25 tăng Hit@10 nhưng giảm MRR/nDCG và tăng latency.
- Context-only là biến thể tốt nhất: tăng Hybrid Hit@10 và MRR rất nhẹ, cải thiện multi-hop, nhưng giảm Required Recall tổng thể và chưa đạt improvement gate.

Do đó source code hỗ trợ experiment được giữ lại, nhưng không thay đổi `QDRANT_COLLECTION` của runtime/API.

## 2. Những gì đã implement

- Deterministic enrichment contract/version `deterministic-context-terms-v2`.
- Các variant:
  - `context`.
  - `context_terms`.
  - `context_terms_pedagogy`.
- Dynamic header token budget theo giới hạn 512 input tokens của E5.
- Chunk dài giữ raw embedding text, không bị prefix đẩy mất phần cuối.
- Local-only embedding và BM25; không gửi corpus đến provider ngoài.
- Persistent FastEmbed cache tại `/home/chiron/.cache/fastembed`.
- Versioned Qdrant collections, stable point IDs và resumable indexing.
- Raw dense-vector reuse; checksum/version mismatch sẽ fallback re-embed local.
- Qdrant payload compact: không lưu bản `retrieval_text` trùng với raw content.
- Verifier tái tạo deterministic retrieval checksum từ PostgreSQL.
- Evaluator hỗ trợ `--collection` để chạy A/B trên cùng golden set.
- Unit tests cho determinism, token budget, citation integrity và dense-vector blending.

Các file chính:

- `services/worker/chiron_worker/enrichment.py`.
- `services/worker/scripts/index_enriched.py`.
- `services/worker/scripts/verify_enriched_index.py`.
- `services/worker/scripts/eval_retrieval.py`.
- `services/worker/chiron_worker/qdrant.py`.
- `services/worker/tests/test_enrichment.py`.

Validation code:

- Worker tests: `19 passed`.
- Ruff: all checks passed.
- Worker image build: passed.

## 3. Các vấn đề phát hiện trong quá trình validation

### 3.1 RLS scope resolution

Runtime role không thể join tenant/course trước khi có tenant context. Script được sửa theo đúng thứ tự:

```text
resolve tenant
  -> set app.tenant_id
  -> resolve course
  -> query chunks
```

### 3.2 FastEmbed cache không persistent

Model 2.1 GB trước đó nằm ở `/tmp/fastembed_cache`, khiến container mới kiểm tra/tải lại artifact. Cache đã được chuyển vào Docker volume và truyền qua `EMBEDDING_CACHE_PATH`.

### 3.3 E5 truncation

`intfloat/multilingual-e5-large` trong FastEmbed cắt input tại 512 tokens. Corpus hiện có:

- `1,918` chunks trên 400 estimated tokens.
- `1,334` chunks trên 450 tokens.
- `408` chunks trên 500 tokens.
- Max `697` estimated tokens.

Enrichment v2 giới hạn header tối đa 64 estimated tokens và tổng retrieval budget mục tiêu 500. Khi không còn budget, retrieval text giữ nguyên raw content.

### 3.4 Mixed legacy embedding version

Raw Qdrant collection có một point gặp trong full experiment mang embedding version legacy. Indexer không trộn vector khác version:

- `5,069` points reuse raw dense vector hợp lệ.
- `1` point fallback re-embed raw content local bằng E5 v2.

Các outbox event legacy `multilingual-e5-large-mean-v1` vẫn được giữ nguyên để xử lý trong một maintenance task riêng; worker v2 không claim chúng.

## 4. Experiment collections

| Collection | Variant | Dense strategy | Trạng thái |
| --- | --- | --- | --- |
| `chiron_chunks_v1` | Raw | Full local E5 | Active control |
| `chiron_chunks_enriched_v2_w020` | Context + terms + pedagogy | Raw/context blend 0.20 | Rejected |
| `chiron_chunks_enriched_v2_w000` | Context + terms + pedagogy | Reuse raw dense, enriched BM25 | Rejected |
| `chiron_chunks_context_v2_w000` | Context-only | Reuse raw dense, contextual BM25 | Best experiment, not approved |

Các pilot/benchmark/partial collections cũ không được dùng trong runtime. Chúng chưa bị xóa để giữ bằng chứng thí nghiệm và tránh destructive cleanup ngoài phạm vi.

## 5. Overall retrieval metrics

Golden set: 20 queries, source-span dedup, `top_k=10`, `candidate_limit=24`, reranker disabled.

### Hybrid

| Variant | Hit@10 | Required Recall@10 | MRR@10 | nDCG@10 | Precision@10 | P95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Raw control | 0.800 | 0.575 | 0.524 | 0.370 | 0.125 | 111.9 ms |
| Blend 0.20 | 0.600 | 0.375 | 0.254 | 0.204 | 0.086 | 239.8 ms |
| Terms/pedagogy, weight 0 | 0.850 | 0.567 | 0.493 | 0.347 | 0.125 | 147.1 ms |
| Context-only, weight 0 | 0.850 | 0.517 | 0.528 | 0.354 | 0.120 | 133.2 ms |

### BM25

| Variant | Hit@10 | Required Recall@10 | MRR@10 | nDCG@10 | Precision@10 | P95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Raw control | 0.700 | 0.367 | 0.335 | 0.237 | 0.090 | 57.0 ms |
| Terms/pedagogy | 0.750 | 0.408 | 0.296 | 0.225 | 0.095 | 109.1 ms |
| Context-only | 0.750 | 0.408 | 0.328 | 0.239 | 0.095 | 75.8 ms |

Dense metrics ở các variant weight 0 giữ nguyên raw control về chất lượng (`Hit=0.800`, `Recall=0.550`, `MRR=0.516`, `nDCG=0.374`).

## 6. Phân tích theo query class

Context-only cho tín hiệu tốt nhất ở multi-hop:

| Query class / Hybrid | Raw Hit | Context Hit | Raw Recall | Context Recall | Raw MRR | Context MRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Direct | 1.000 | 1.000 | 0.875 | 0.750 | 0.738 | 0.678 |
| Prerequisite | 0.667 | 0.667 | 0.333 | 0.250 | 0.214 | 0.294 |
| Multi-hop | 0.667 | 0.833 | 0.417 | 0.472 | 0.556 | 0.569 |

Điều này cho thấy contextual retrieval có ích cho câu hỏi quan hệ/đa bước, nhưng không nên áp dụng blanket cho mọi query. Direct query bị giảm recall/ranking do section/document tokens cạnh tranh với keyword chính.

## 7. Quality-gate decision

Gate ban đầu yêu cầu một trong hai:

- Hybrid Required Recall@10 tăng ít nhất `+0.10` absolute; hoặc
- Hybrid MRR@10 tăng ít nhất `+0.05`.

Đồng thời direct Hit@10 không regression quá `0.02` và P95 không tăng quá `20%`.

Context-only đạt direct Hit gate và P95 xấp xỉ giới hạn, nhưng:

- Required Recall thay đổi `-0.058`.
- MRR chỉ thay đổi khoảng `+0.004`.
- nDCG thay đổi `-0.016`.

**Kết luận:** không đạt quality gate, không cutover.

## 8. Runtime state sau experiment

- `QDRANT_COLLECTION` vẫn là `chiron_chunks_v1`.
- Reranker vẫn tắt.
- Worker đã được bật lại sau offline indexing.
- PostgreSQL/Qdrant/Redis vẫn chạy.
- Không có database migration enrichment.
- Không có learner/citation data bị thay đổi.

## 9. Bước tiếp theo được khuyến nghị

1. Human-review 20 golden cases và mở rộng lên ít nhất 50–100 queries.
2. Thêm query classifier/routing deterministic:
   - Direct query dùng raw hybrid.
   - Prerequisite/multi-hop dùng thêm contextual sparse candidates.
3. Tách `raw_bm25` và `context_bm25` thành hai named sparse vectors để fusion có trọng số, thay vì nối metadata vào một sparse document.
4. Dùng knowledge graph expansion ở query time cho `prerequisite_of`, `part_of`, `causes`, `contrasts_with`; không nhồi toàn graph vào chunk.
5. Chỉ sau khi routing/fusion pass golden set mới cân nhắc reranker.
6. Xử lý 61 outbox events embedding version legacy trong maintenance task riêng; không đổi trạng thái trong experiment này.

## 10. Artifacts

- Raw control: `eval/rag/runs/e5-large-v2-review20-source-dedup.json`.
- Blend 0.20: `eval/rag/runs/enriched-v2-w020-review20.json`.
- Terms/pedagogy weight 0: `eval/rag/runs/enriched-v2-w000-compact-review20.json`.
- Context-only weight 0: `eval/rag/runs/context-v2-w000-review20.json`.
- Index manifest weight 0: `eval/rag/runs/enriched-index-deterministic-v2-w000.json`.
- Context-only index manifest: `eval/rag/runs/context-index-v2-w000.json`.
