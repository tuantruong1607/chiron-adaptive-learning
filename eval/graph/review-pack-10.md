# Chiron Graph-lite review pack — 10 candidates

Phạm vi: 5 node + 5 edge từ graph version draft. Check `Approve`, `Edit` hoặc `Reject`; production không dùng candidate trước khi duyệt.

## Node `hybrid_search` — Hybrid Search

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.87`
- Summary: Kết hợp dense và sparse retrieval để cân bằng semantic recall và exact matching.
- Source: **Vector Store & Feature Store** — `{"kind": "page", "page": 18, "label": "Slide 18", "section_title": "Hybrid Search: BM25 + Vector + RRF", "extraction_method": "pdf-text-layer"}`
- Source span: `c54b8f84-4b7c-5e47-b9c3-cab7162b9bf4`

> Hybrid Search: BM25 + Vector + RRF Query BM25 / SPLADE Vector ANN (HNSW) RRF Merge k= 60 Top-K Hybrid sparse, exact-term match dense, semantic match Reciprocal Rank Fusion — score(d) = ∑ r 1 k + rankr(d) (k = 60) Rank-only: không cần normalize raw scores giữa BM25 (TF-IDF) và cosine. Production 2026 (Hybrid wins) ■ Recall@10: hybrid > dense-only ∼10–15 pp (đo trên golden set của bạn — Lab 19) ■ Latency +6 ms (song song) · storage 1.4× ■ Native: Qdrant, Weaviate, OpenSearch, Milvus ■ SPLADE: recall > BM25 nhưng cần GPU Giảng viên (VinUni) AICB · Ngày 19 Tuần 4 16 / 56

Reviewer note:

## Node `rag_evaluation` — RAG Evaluation

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.86`
- Summary: Đánh giá độc lập retrieval, grounding và answer quality của pipeline RAG.
- Source: **RAGAS, LLM-as-Judge & Guardrails** — `{"kind": "page", "page": 24, "label": "Slide 24", "section_title": "RAGAS Benchmark Targets", "extraction_method": "pdf-text-layer"}`
- Source span: `6bc653d6-19b4-5f79-ba52-646751098ca7`

> RAGAS Benchmark Targets Metric Target Min OK Action nếu thấp Faithfulness ≥ 0.85 0.75 Hallucination → tighten prompt, add NLI guardrail Answer Relevancy ≥ 0.80 0.70 Off-topic → improve prompt instruction Context Precision ≥ 0.70 0.60 Bad ranking → add re-ranker (Cohere Rerank) Context Recall ≥ 0.75 0.65 Missing info → improve in- dexing, expand top-k T argets chogeneral RAG. Medical/legal: tăng F lên ≥ 0.95 (hallucination = liability). Creative writing: relax F xuống 0.7 (creative liberty OK). Phụ thuộc risk profile. Giảng viên (VinUni) AICB · RAGAS & Guardrails 2026 20 / 62

Reviewer note:

## Node `knowledge_graph` — Knowledge Graph

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.91`
- Summary: Mô hình hóa concept/entity thành nodes và quan hệ có kiểu thành edges.
- Source: **GraphRAG & Knowledge Graphs** — `{"kind": "page", "page": 62, "label": "Slide 62", "section_title": "Tổng kết — Key Takeaways", "extraction_method": "pdf-text-layer"}`
- Source span: `9190082d-1ec2-5eb3-9ef2-6ba66ad6d948`

> Tổng kết — Key Takeaways Những ý chính cần nhớ sau buổi học hôm nay 1 Knowledge graphs enable multi-hop reasoning mà flat RAG không làm được —  dùng cho relational queries 2 Entity extraction quality là bottleneck — invest NER + coreference resolution trước  khi build graph 3 “Graph quality beats Graph size” — 1000 high-quality triples beats 100K noisy  ones 4 GraphRAG pipeline là production-ready starting point — customize entity  extraction cho domain của bạn Giảng viên  (VinUni) AICB · Ngày  19 Tuần 4  17 /  18

Reviewer note:

## Node `agent_memory` — Agent Memory

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.82`
- Summary: Hệ thống lưu trạng thái ngắn hạn, trải nghiệm và tri thức bền vững của agent.
- Source: **Agent Memory & Context Engineering** — `{"kind": "html_section", "order": 17, "heading": "☰ Từ điển thuật ngữ", "section_id": "gloss", "source_file": "track-3-day-17.html"}`
- Source span: `62f11aca-0046-595f-945c-cdb1f2f8da9d`

> ☰ Từ điển thuật ngữ Memory taxonomy slide 1 · 2 Memory Systems for Agents AICB-P2T3 · Ngày 17 · Chương 4 — Agent Nâng Cao Context engineering slide 4 · 6 Context window có giới hạn — và hầu hết agent không có bộ nhớ ngoài Short-term memory slide 8 · 10 Policy context trim cuối cùng (safety không bao giờ bỏ). Episodic memory slide 12 · 14 Short-term Memory — Context Window Management Buffer M1 M2 M3 M4 M5 limit! Semantic memory slide 16 · 17 Node load_memory: đọc 3 loại memory khi bắt đầu 2. Retrieval, decay & consolidation slide 19 · 21 05 Frameworks chuyên dụng & Privacy Mem0, Zep — và khi nào dùng framework có sẵn Redis và persistence slide 23 · 25 06 Demo & Thực hành Xem agent nhớ user pr

Reviewer note:

## Node `circuit_breaker` — Circuit Breaker

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.87`
- Summary: Ngắt gọi dependency đang lỗi để chặn retry storm và cho hệ thống hồi phục.
- Source: **Circuit Breakers, Caching & Reliability — phân tích & breakdown từng slide** — `{"kind": "html_section", "order": 13, "heading": "✓ Cheat sheet ôn thi", "section_id": "cheat", "source_file": "track-3-day-25.html"}`
- Source span: `0897d557-4bbd-5679-8651-803d5e1b1491`

> ✓ Cheat sheet ôn thi   Nén 34 slide xuống một trang.       Sáu danh sách phải thuộc     Danh sách Nội dung Slide   6 nhóm lỗi ① provider transient · ② degraded latency · ③ full outage · ④ orchestration loop · ⑤ tool/cache failure · ⑥ business action sai ①②③ ở provider (chứa được, không sửa được) · ④⑤⑥ ở phía bạn (sửa được) 8   3 trạng thái breaker CLOSED → (vượt failure_threshold) → OPEN → (hết reset_timeout) → HALF-OPEN → (thành công) CLOSED / (lỗi) OPEN Bốn mũi tên, không phải ba 12   4 tham số breaker failure_threshold · reset_timeout_seconds · success_threshold · exception nào tính là failure 13   5 bậc fallback model tốt nhất → provider dự phòng → model rẻ hơn → cache → thông báo tĩnh K

Reviewer note:

## Edge `dense_pre_hybrid`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `dense_retrieval` — **prerequisite_of** → `hybrid_search`
- Confidence: `0.86`
- Source: **Vector Store & Feature Store** — `{"kind": "page", "page": 18, "label": "Slide 18", "section_title": "Hybrid Search: BM25 + Vector + RRF", "extraction_method": "pdf-text-layer"}`
- Source span: `c54b8f84-4b7c-5e47-b9c3-cab7162b9bf4`

> Hybrid Search: BM25 + Vector + RRF Query BM25 / SPLADE Vector ANN (HNSW) RRF Merge k= 60 Top-K Hybrid sparse, exact-term match dense, semantic match Reciprocal Rank Fusion — score(d) = ∑ r 1 k + rankr(d) (k = 60) Rank-only: không cần normalize raw scores giữa BM25 (TF-IDF) và cosine. Production 2026 (Hybrid wins) ■ Recall@10: hybrid > dense-only ∼10–15 pp (đo trên golden set của bạn — Lab 19) ■ Latency +6 ms (song song) · storage 1.4× ■ Native: Qdrant, Weaviate, OpenSearch, Milvus ■ SPLADE: recall > BM25 nhưng cần GPU Giảng viên (VinUni) AICB · Ngày 19 Tuần 4 16 / 56

Reviewer note:

## Edge `sparse_pre_hybrid`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `sparse_retrieval` — **prerequisite_of** → `hybrid_search`
- Confidence: `0.86`
- Source: **Vector Store & Feature Store** — `{"kind": "page", "page": 18, "label": "Slide 18", "section_title": "Hybrid Search: BM25 + Vector + RRF", "extraction_method": "pdf-text-layer"}`
- Source span: `c54b8f84-4b7c-5e47-b9c3-cab7162b9bf4`

> Hybrid Search: BM25 + Vector + RRF Query BM25 / SPLADE Vector ANN (HNSW) RRF Merge k= 60 Top-K Hybrid sparse, exact-term match dense, semantic match Reciprocal Rank Fusion — score(d) = ∑ r 1 k + rankr(d) (k = 60) Rank-only: không cần normalize raw scores giữa BM25 (TF-IDF) và cosine. Production 2026 (Hybrid wins) ■ Recall@10: hybrid > dense-only ∼10–15 pp (đo trên golden set của bạn — Lab 19) ■ Latency +6 ms (song song) · storage 1.4× ■ Native: Qdrant, Weaviate, OpenSearch, Milvus ■ SPLADE: recall > BM25 nhưng cần GPU Giảng viên (VinUni) AICB · Ngày 19 Tuần 4 16 / 56

Reviewer note:

## Edge `kg_pre_graphrag`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `knowledge_graph` — **prerequisite_of** → `graphrag`
- Confidence: `0.86`
- Source: **GraphRAG & Knowledge Graphs** — `{"kind": "page", "page": 62, "label": "Slide 62", "section_title": "Tổng kết — Key Takeaways", "extraction_method": "pdf-text-layer"}`
- Source span: `9190082d-1ec2-5eb3-9ef2-6ba66ad6d948`

> Tổng kết — Key Takeaways Những ý chính cần nhớ sau buổi học hôm nay 1 Knowledge graphs enable multi-hop reasoning mà flat RAG không làm được —  dùng cho relational queries 2 Entity extraction quality là bottleneck — invest NER + coreference resolution trước  khi build graph 3 “Graph quality beats Graph size” — 1000 high-quality triples beats 100K noisy  ones 4 GraphRAG pipeline là production-ready starting point — customize entity  extraction cho domain của bạn Giảng viên  (VinUni) AICB · Ngày  19 Tuần 4  17 /  18

Reviewer note:

## Edge `episodic_pre_consolidation`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `episodic_memory` — **prerequisite_of** → `memory_consolidation`
- Confidence: `0.86`
- Source: **Agent Memory & Context Engineering** — `{"kind": "html_section", "order": 17, "heading": "☰ Từ điển thuật ngữ", "section_id": "gloss", "source_file": "track-3-day-17.html"}`
- Source span: `62f11aca-0046-595f-945c-cdb1f2f8da9d`

> ☰ Từ điển thuật ngữ Memory taxonomy slide 1 · 2 Memory Systems for Agents AICB-P2T3 · Ngày 17 · Chương 4 — Agent Nâng Cao Context engineering slide 4 · 6 Context window có giới hạn — và hầu hết agent không có bộ nhớ ngoài Short-term memory slide 8 · 10 Policy context trim cuối cùng (safety không bao giờ bỏ). Episodic memory slide 12 · 14 Short-term Memory — Context Window Management Buffer M1 M2 M3 M4 M5 limit! Semantic memory slide 16 · 17 Node load_memory: đọc 3 loại memory khi bắt đầu 2. Retrieval, decay & consolidation slide 19 · 21 05 Frameworks chuyên dụng & Privacy Mem0, Zep — và khi nào dùng framework có sẵn Redis và persistence slide 23 · 25 06 Demo & Thực hành Xem agent nhớ user pr

Reviewer note:

## Edge `slo_part_observability`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `sli_slo` — **part_of** → `observability`
- Confidence: `0.86`
- Source: **Observability — Nhìn thấy Agent trong Production** — `{"kind": "html_section", "order": 20, "heading": "☰ Từ điển thuật ngữ", "section_id": "gloss", "source_file": "day-13.html"}`
- Source span: `42cf8474-4326-594c-811b-0b3708d3db77`

> ☰ Từ điển thuật ngữ Observability khác monitoring slide 1 · 6 Monitoring, Logging & Observability AICB-P1· Ngày 13 · Biếtagent đang chạy thế nào trướckhi user phàn nàn Tên Ba trụ log–metric–trace slide 11 · 16 Observability: Vài Cột Mốc 1 Logs (text) 2 Metrics & Prometheus 2012 3 Grafana 2014 4 Tracing & OTel 2019 5 LLM-native 2023+ Structured logging cho agent slide 21 · 26 REDvs USE — Hai PhươngPháp Observability RED(request-centric) Distributed tracing & OpenTelemetry slide 32 · 37 04 Structured Logging Log không cấu trúc giống ghi chú tay — khó search, khó aggre- gate. Metric riêng của AI slide 42 · 47 AuditLog — Tách Biệt VớiApp Log Audit log— Recordwho did what whencho compliance, lega

Reviewer note:
