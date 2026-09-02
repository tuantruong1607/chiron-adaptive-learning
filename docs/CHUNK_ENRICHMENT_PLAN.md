# Chiron AI — Chunk Enrichment Plan

> **Trạng thái:** EXECUTED AS AN EXPERIMENT — AUTO-CUTOVER KHI QUALITY GATE PASS  
> **Quyết định:** Giữ `chiron_chunks_v1` làm collection active; các biến thể enriched không đạt quality gate tổng thể.  
> **Báo cáo:** [`CHUNK_ENRICHMENT_EXPERIMENT_REPORT.md`](CHUNK_ENRICHMENT_EXPERIMENT_REPORT.md).  
> **Phạm vi đã thực hiện:** Pipeline/versioning, local indexing, integrity verification và A/B evaluation. Chưa migration database và chưa nối enriched collection vào learner API.

## 1. Mục tiêu

Làm giàu biểu diễn truy xuất của mỗi chunk để tăng khả năng tìm đúng nguồn, đặc biệt với:

- Câu hỏi dùng từ khác với slide nhưng cùng khái niệm.
- Câu hỏi về prerequisite, quan hệ nguyên nhân–kết quả và ứng dụng.
- Câu hỏi đa bước cần ghép nhiều source span.
- Câu hỏi tiếng Việt có thuật ngữ, viết tắt hoặc tên tiếng Anh xen kẽ.

Enrichment **không thay thế nội dung gốc**. Mọi câu trả lời và citation vẫn phải quay về `source_span_id`, locator và nguyên văn đã ingest. Nội dung làm giàu chỉ được dùng để tìm kiếm/ranking.

Enrichment cũng không mặc nhiên làm truy xuất nhanh hơn: text dài hơn có thể làm tăng chi phí embedding, dung lượng index và latency. Mục tiêu tốc độ chỉ được coi là đạt nếu chất lượng tốt hơn cho phép giảm số candidate mà vẫn giữ recall.

## 2. Baseline bắt buộc giữ nguyên

Baseline control hiện tại:

- Corpus: `5,070` active child chunks.
- PostgreSQL ↔ Qdrant: khớp ID, `missing=0`, `extra=0`.
- Golden review set: `20` query, gồm `8 direct`, `6 prerequisite`, `6 multi_hop`.
- Embedding: local `intfloat/multilingual-e5-large`.
- Reranker: tắt.
- Báo cáo control: `eval/rag/runs/e5-large-v2-review20-source-dedup.json`.

| Retriever | Hit@10 | Required Recall@10 | MRR@10 | nDCG@10 | Precision@10 | P50 | P95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Dense | 0.800 | 0.550 | 0.516 | 0.374 | 0.125 | 55.6 ms | 86.9 ms |
| BM25 | 0.700 | 0.367 | 0.335 | 0.237 | 0.090 | 44.9 ms | 57.0 ms |
| Hybrid | 0.800 | 0.575 | 0.524 | 0.370 | 0.125 | 80.2 ms | 111.9 ms |

Các thí nghiệm enrichment phải chạy trên cùng query set, cùng metric, cùng embedding model và cùng quy tắc collapse theo `source_span_id`. Không ghi đè collection/control report này.

## 3. Nguyên tắc thiết kế

1. **Raw text bất biến:** không chỉnh sửa, tóm tắt hoặc chèn nội dung vào source span gốc.
2. **Citation có thể kiểm chứng:** kết quả cuối luôn trả về source locator và raw text, không cite synthetic text.
3. **Local-only:** toàn bộ corpus enrichment và embedding chạy trên laptop hiện tại; không gửi slide/HTML riêng tư lên OpenAI, Groq hoặc Gemini.
4. **Có provenance:** mọi alias, concept, entity và quan hệ phải ghi nguồn/phương pháp tạo.
5. **Versioned và idempotent:** cùng raw checksum + enrichment config phải tạo cùng kết quả và không sinh point trùng.
6. **Tenant-safe:** mọi đọc/ghi enrichment phải giữ `tenant_id`, `course_id` và tenant filter hiện có.
7. **Tách retrieval khỏi teaching:** metadata hỗ trợ tìm kiếm; AI tutor chỉ được diễn giải sau khi đã lấy evidence có citation.
8. **Tài liệu không phải chỉ dẫn hệ thống:** câu lệnh/prompt nằm trong PDF hoặc HTML được coi là nội dung học, không được thực thi hay nâng quyền.

## 4. Retrieval document đề xuất

Mỗi chunk có hai biểu diễn:

- `content_raw`: nguyên văn để hiển thị, grounding và citation.
- `retrieval_text_enriched`: text có cấu trúc chỉ dùng cho embedding/BM25/ranking.

Mẫu retrieval text:

```text
[COURSE] <course title>
[DOCUMENT] <document title> | <source type>
[SECTION PATH] <chapter> > <section> > <subsection>
[CONCEPTS] <canonical concept IDs/names>
[ALIASES] <Vietnamese/English aliases and acronyms>
[ENTITIES] <technologies, formulas, metrics, named methods>
[PEDAGOGY] <definition | prerequisite | mechanism | example | failure mode | application>
[QUERY INTENTS] <optional, experiment-only retrieval questions>
[CONTENT]
<content_raw>
```

Giới hạn đề xuất ban đầu:

- Context header: tối đa 80 tokens.
- Aliases + entities: tối đa 40 tokens, khử trùng lặp.
- Pedagogy labels: danh mục hữu hạn, không viết prose dài.
- Synthetic query intents: tối đa 3 câu/chunk, chỉ mở ở biến thể thí nghiệm riêng.
- Không serialize toàn bộ knowledge graph vào từng chunk; chỉ lưu các concept ID/edge hint trực tiếp liên quan.

## 5. Các lớp enrichment

### E1 — Deterministic contextual prefix

Không dùng LLM. Lấy từ metadata ingest đã có:

- Course, document title, source type.
- Chapter/heading/section path.
- Page/slide hoặc HTML anchor.
- Parent heading gần nhất.

Đây là biến thể rủi ro thấp nhất và cần thử trước.

### E2 — Canonical concepts, aliases và entities

- Chuẩn hóa thuật ngữ tiếng Việt/Anh, acronym và biến thể chính tả.
- Liên kết alias về canonical concept ID trong knowledge map.
- Trích technology, formula, metric, method và named entity.
- Mỗi alias phải có provenance: xuất hiện trong corpus, glossary được duyệt hoặc rule chuẩn hóa.
- Không tự bịa synonym chỉ vì gần nghĩa.

### E3 — Pedagogical metadata và relationship hints

- Loại tri thức: definition, mechanism, prerequisite, comparison, example, application, limitation, misconception/failure mode.
- Bloom level dự kiến: remember, understand, apply, analyze, evaluate.
- Quan hệ trực tiếp: `prerequisite_of`, `part_of`, `causes`, `contrasts_with`, `applies_to`, `evidence_for`.
- Chỉ ghi ID/edge type đã được validator chấp nhận; không nhúng narrative graph dài vào retrieval text.

### E4 — Synthetic query intents (tùy chọn, rủi ro cao)

- Tạo tối đa 3 cách người học có thể hỏi về chunk: direct, misconception/application, prerequisite/relationship.
- Chạy local, batch offline.
- Không tạo câu trả lời hoặc đáp án giả trong retrieval document.
- Phải được benchmark riêng vì synthetic question có thể keyword-stuffing, làm loãng meaning hoặc đẩy nhầm chunk lên cao.

## 6. Schema/versioning dự kiến

Chưa triển khai migration. Contract dự kiến cần các trường:

```text
source_span_id
chunk_id
tenant_id
course_id
content_raw
raw_checksum
retrieval_text_enriched
retrieval_text_checksum
enrichment_version
enrichment_method
enrichment_status
enrichment_provenance
enriched_at
```

ID enrichment được suy ra từ:

```text
sha256(raw_checksum + enrichment_version + normalized_config)
```

Source thay đổi checksum thì enrichment cũ trở thành stale và phải rebuild. Retry cùng version/config không tạo bản ghi hay Qdrant point trùng.

Quyết định schema cuối cùng sẽ chọn một trong hai phương án sau khi prototype:

- Bảng `chunk_enrichments` riêng: audit/rollback tốt, phù hợp nhiều phiên bản A/B.
- JSON metadata trên chunk: đơn giản hơn nhưng khó so sánh và rollback nhiều biến thể.

Khuyến nghị hiện tại: dùng bảng riêng cho enrichment versioned.

## 7. Thiết kế Qdrant và cutover

- Giữ nguyên collection raw hiện tại làm control.
- Mỗi biến thể enrichment dùng collection hoặc named-vector version riêng, ví dụ `chiron_chunks_enriched_v1`.
- Point payload vẫn chứa `tenant_id`, `course_id`, `source_span_id`, locator và checksums.
- Không đưa answer key, learner state hoặc dữ liệu cá nhân vào vector payload.
- Cutover bằng config/collection alias sau khi pass evaluation; rollback chỉ cần trỏ lại raw collection.
- Worker/outbox phải dùng idempotency key gồm source ID + enrichment version.

## 8. Ma trận thí nghiệm

| Variant | Nội dung | Mục đích |
| --- | --- | --- |
| A | Raw chunk hiện tại | Control |
| B | A + contextual prefix | Đo tác động của section/document context |
| C | B + canonical concepts + aliases + entities | Đo semantic/lexical recall |
| D | C + pedagogical labels + relationship hints | Đo prerequisite và multi-hop retrieval |
| E | D + synthetic query intents | Thử nghiệm rủi ro cao, không mặc định production |

Quy tắc A/B:

- Cùng E5 local model, chunk corpus snapshot, tenant/course filter và query set.
- Dense, BM25 và hybrid đều được đo.
- Chưa bật reranker trong vòng này để tách riêng tác động của enrichment.
- Lưu run manifest: git commit, corpus checksum, collection, model, config, timestamp.
- Báo cáo theo toàn bộ tập và từng lớp `direct`, `prerequisite`, `multi_hop`.

## 9. Metrics và quality gates đề xuất

Metrics bắt buộc:

- Hit@10.
- Required source Recall@10.
- MRR@10 và nDCG@10.
- Source Precision@10.
- Query embedding P50/P95 và retrieval P50/P95.
- Thời gian/bộ nhớ enrichment, thời gian embedding toàn corpus, Qdrant storage size.
- Citation integrity: source IDs tồn tại và raw checksum không đổi.

Gate để cân nhắc production (cần review trước khi chạy):

- Không có citation mismatch, tenant leakage hoặc mất source span.
- Hybrid Required Recall@10 tăng ít nhất `+0.10` absolute **hoặc** MRR@10 tăng ít nhất `+0.05` so với control.
- Không làm Hit@10 của nhóm direct giảm quá `0.02` absolute.
- Retrieval P95 không tăng quá `20%` ở cùng candidate limit.
- Kích thước vector/index không tăng quá `35%` nếu chưa có lợi ích chất lượng tương xứng.

Sau khi chất lượng pass, chạy thêm experiment giảm `candidate_limit` từ 24 xuống 16. Chỉ khi chất lượng được giữ và P95 giảm mới kết luận enrichment giúp retrieval nhanh hơn.

Golden set 20 query hiện tại đủ cho vòng engineering đầu tiên nhưng chưa đủ để kết luận production. Trước cutover cần:

1. Freeze expected source labels của golden set trong versioned dataset; không chờ human-review riêng trước cutover.
2. Mở rộng tối thiểu 50 query; mục tiêu tốt hơn là 100 query.
3. Bổ sung query thực tế từ đề thi/câu hỏi học viên khi có.

## 10. Pipeline dự kiến

```text
raw source span
  -> validate checksum + tenant/course scope
  -> deterministic context builder
  -> local alias/entity/concept linker
  -> local pedagogy/relationship classifier
  -> optional local synthetic-query generator
  -> schema + provenance validator
  -> build retrieval_text_enriched
  -> local embedding
  -> idempotent outbox event
  -> versioned Qdrant collection
  -> A/B evaluation
  -> review gate
  -> optional cutover
```

Nếu một enrichment stage lỗi, raw chunk vẫn usable. Record được đánh dấu `failed`/`partial`, không được âm thầm index text thiếu provenance.

## 11. Failure modes cần kiểm soát

- Hallucinated alias, concept hoặc relationship.
- Keyword stuffing khiến precision giảm dù recall tăng.
- Synthetic query chứa đáp án hoặc chi tiết không có trong source.
- Nhiều child chunk cùng source span chiếm hết top-k.
- Section path sai do PDF/HTML parsing.
- Enrichment stale sau khi source đổi.
- Dữ liệu của tenant/course khác lọt vào prefix hoặc relation.
- Prompt injection trong slide/HTML bị hiểu thành instruction.
- Chuẩn hóa tiếng Việt làm mất dấu hoặc biến đổi công thức/code.
- Graph hints tạo cycle hoặc quan hệ mâu thuẫn.

Validator phải fail closed đối với tenant mismatch, missing source ID, checksum mismatch và provenance không hợp lệ.

## 12. Kế hoạch thực hiện sau khi được Proceed

### Phase 0 — Review control

- Freeze 20 golden cases cùng expected-source labels và chạy integrity check tự động.
- Chốt quality gates và resource budget.
- Không đổi baseline report.

**Deliverable:** golden set trạng thái approved và decision record.

### Phase 1 — Enrichment contract

- Chốt schema, config version, token budget và provenance contract.
- Thiết kế migration, repository và outbox event nhưng chưa full index.
- Viết unit/contract tests cho determinism, checksum, tenant isolation và citation preservation.

**Deliverable:** contract + tests + migration review.

### Phase 2 — Deterministic prototype

- Chọn một PDF và một HTML đại diện.
- Build E1 contextual prefix.
- Index vào collection thử nghiệm nhỏ.
- So sánh A/B và kiểm tra thủ công top-k.

**Stop gate:** không tiếp tục nếu section path/citation không chính xác.

### Phase 3 — Local semantic enrichment pilot

- Thêm E2/E3 trên khoảng 10% corpus có stratified sampling.
- Validate alias/concept/relationship và review sample thủ công.
- Benchmark CPU/RAM, throughput và index growth trên laptop hiện tại.

**Stop gate:** không full-index nếu hallucination/provenance hoặc tài nguyên vượt budget.

### Phase 4 — Full A/B local index

- Chạy B/C/D trên corpus snapshot đầy đủ.
- E chỉ chạy nếu D chưa đủ và người dùng duyệt synthetic-query experiment.
- Lưu manifests và reports riêng, không overwrite control.

### Phase 5 — Evaluation và quyết định

- Chạy dense/BM25/hybrid trên cùng golden set.
- Phân tích regression theo query class và inspect false positives.
- Chọn một variant hoặc giữ raw nếu không pass.

**Deliverable:** recommendation có số liệu, cost/latency/storage và rollback plan.

### Phase 6 — Production cutover (phê duyệt riêng)

- Cutover collection alias/config.
- Canary theo tenant/course.
- Theo dõi latency, no-result rate, citation integrity và rollback signal.
- Chỉ sau phase này mới cân nhắc reranker như một thí nghiệm độc lập.

## 13. Review gates cần người dùng quyết định

1. Approve/revise 20 golden retrieval cases.
2. Approve schema và token budget sau Phase 1.
3. Approve full-corpus local embedding sau kết quả pilot 10%.
4. Approve hoặc bỏ E4 synthetic query intents.
5. Cutover collection alias/config tự động khi A/B quality gates pass; rollback về raw collection nếu runtime SLO hoặc retrieval gate fail.

Format đề thi chưa cần để thiết kế chunk enrichment. Mô tả ngắn về cấu trúc đề sẽ cần sau này khi mở rộng golden set, tạo question bank và xác định tỷ trọng query theo Bloom level/chủ đề.

## 14. Những việc không thực hiện ở thời điểm viết plan

- Không thay đổi PostgreSQL schema/data.
- Không thay đổi importer/chunker/worker.
- Không tạo enrichment record.
- Không chạy lại embedding.
- Không tạo hoặc ghi collection Qdrant mới.
- Không bật reranker.
- Không gửi corpus tới provider bên ngoài.
