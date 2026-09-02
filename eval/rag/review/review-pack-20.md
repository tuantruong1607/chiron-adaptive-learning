# Chiron golden-set review pack

Cases: **20** — direct 8, prerequisite 6, multi-hop 6.

Review mỗi case: câu hỏi tự nhiên, class đúng, required evidence thực sự bắt buộc, và alternate evidence không bị thiếu.

## ret-001 · direct

**Query:** Vì sao RRF gộp thứ hạng thay vì cộng trực tiếp raw score của BM25 và dense retrieval?

**Rationale:** Kiểm tra truy xuất định nghĩa và lý do dùng rank-only fusion.

### Required evidence

- `51baf090-11e9-5a34-83ed-0b6674095dba` — **RAG Pipeline**, 66 · Thuật Toán Giải Quyết: RRF (Reciprocal Rank Fusion)
  - Thuật Toán Giải Quyết: RRF (Reciprocal Rank Fusion) • Đừng gộp điểm số (Scores), hãy gộp Thứ hạng (Ranks). RRF = 1/(k + Rank_Dense) + 1/(k + Rank_Sparse) (Giá trị hằng số k thường được chọn mặc định là 60) • Tài liệu nào nằm trong Top cao ở cả 2 bảng xếp hạng sẽ vươn lên vị trí số 1 tuyệt đối. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

### Acceptable/alternate evidence

- `c54b8f84-4b7c-5e47-b9c3-cab7162b9bf4` — **Vector Store & Feature Store**, 18 · Hybrid Search: BM25 + Vector + RRF
  - Hybrid Search: BM25 + Vector + RRF Query BM25 / SPLADE Vector ANN (HNSW) RRF Merge k= 60 Top-K Hybrid sparse, exact-term match dense, semantic match Reciprocal Rank Fusion — score(d) = ∑ r 1 k + rankr(d) (k = 60) Rank-only: không cần normalize raw scores giữa BM25 (TF-IDF) và cosine. Production 2026 (Hybrid wins) ■ Recall@10: hybrid > dense-only ∼10–15 pp (đo trên golden set của bạn — Lab 19) ■ Latency +6 ms (song song) · storage 1.4× ■ Native: Qdrant, Weaviate, OpenSearch, Milvus ■ SPLADE: reca
- `711e564d-14fa-51fe-b56d-66ab8b8632c1` — **Production RAG**, 24 · Hybrid Search — BM25 + Dense Vector Fusion
  - Hybrid Search — BM25 + Dense Vector Fusion User Query BM25 exact keywords Rank A Dense Vector semantic match Rank BRRF Fusion Top-K Results Không cần GPU Cần embedding model Merge rankings đơn giản: score (d) = ∑ 1 k+ranki(d) . Không cần training, production standard. M.Sc Trần Minh Tú (VinUni) AICB · Ngày 18 Tuần 4 17 / 42

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-002 · direct

**Query:** Dense retrieval và sparse retrieval khác nhau ở loại tín hiệu tìm kiếm nào?

**Rationale:** Kiểm tra semantic meaning so với exact keyword matching.

### Required evidence

- `156dd3dc-7d49-5fd5-a265-5866c21c6131` — **RAG Pipeline**, 54 · 2.2 Dense vs. Sparse Retrieval
  - 2.2 Dense vs. Sparse Retrieval Meaning vs. Keywords: Comparing the semantic understanding of dense vector embeddings against the exact-match precision of sparse retrieval algorithms like BM25.

### Acceptable/alternate evidence

- `1b45856b-93d4-5da3-9509-b6f5a79aae4c` — **RAG Pipeline**, 55 · Hai Trường Phái Tìm Kiếm Cốt Lõi
  - Hai Trường Phái Tìm Kiếm Cốt Lõi Dense Retrieval (Tân binh AI) Tìm theo "Ý Nghĩa" (Semantic). Mã hóa văn bản thành mảng vector dày đặc (ví dụ 1536 chiều). Sparse Retrieval (Lão làng) Tìm theo "Từ Khóa". Dựa trên tần suất xuất hiện của từ (BM25, TF-IDF, Inverted Index). Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-003 · direct

**Query:** Vì sao embedding model tốt không thể cứu một chiến lược chunking tồi?

**Rationale:** Kiểm tra failure mode ở offline ingestion.

### Required evidence

- `f22da771-c78c-5b18-b296-aa9b0424afd3` — **Data Foundations**, 41 · Chunking & Chuẩn Bị Tài Liệu
  - 06 Chunking & Chuẩn Bị Tài Liệu Chunk sai thì mọi retrieval xây trên top- k đều sai theo — không mô hình embedding nào cứu được một chunk tồi

### Acceptable/alternate evidence

- `c7bff788-d0be-5fb0-9978-ecbf66dae8a4` — **Production RAG**, 10 · Fix OFFLINE — Ingestion
  - 02 Fix OFFLINE — Ingestion Pipeline Data Processing: Chunking, Embedding & Enrichment

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-004 · direct

**Query:** Tại sao cross-encoder reranker chỉ nên chạy trên một danh sách candidates nhỏ?

**Rationale:** Kiểm tra trade-off accuracy, latency và compute của reranking.

### Required evidence

- `e19857c8-3111-5197-a94f-57b1006722b5` — **RAG Pipeline**, 77 · Hiệu Năng vs. Độ Chính Xác
  - Hiệu Năng vs. Độ Chính Xác Đặc điểm mô hình ● Cross-Encoder chấm điểm cực kỳ chính xác (như một người đọc kiểm tra chéo). ● Nhưng nó quá chậm và tốn compute. Không bao giờ được dùng Reranker để quét toàn bộ database. ● Chỉ dùng cho list nhỏ đã lọt qua vòng 1. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

### Acceptable/alternate evidence

- `52275ecd-b8ac-5a27-8974-d53e43d8ec4f` — **Production RAG**, 23 · Fix ONLINE — Retrieval & Aug
  - 05 Fix ONLINE — Retrieval & Aug- ment Hybrid Search, Metadata Filtering & Reranking — fix R và A

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-005 · direct

**Query:** False-hit trong semantic cache xảy ra như thế nào và cần theo dõi metric gì?

**Rationale:** Kiểm tra cache poisoning do cosine gần nhưng intent khác.

### Required evidence

- `dc56e77c-fe6b-5f19-b51b-5a6fd62eb717` — **Circuit Breakers, Caching & Re**, 18 · Semantic cache flow
  - Semantic cache flow User query Embed Vector search HIT return cache MISS call LLM Store result sim > threshold sim < threshold Lưu ý: Cache poisoning: hai query cosine gần nhau nhưng intent khác nhau. Metric quan trọng: hit rate và false-hit rate. Instructor (VinUni) AICB · Day 10 Week 5 12 / 23

### Acceptable/alternate evidence

- `4090f69a-a543-5d78-861f-d1ac9cd0ed11` — **Circuit Breakers, Caching & Reliability — phân tích & breakdown từng slide**, A–Z Từ điển thuật ngữ
  - A–Z Từ điển thuật ngữ Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện. Circuit breaker Cơ chế ngừng gọi một dịch vụ đang hỏng, thay vì cứ thử mãi. Không sửa được nguyên nhân — chỉ ngăn nó lan rộng. CLOSED / OPEN / HALF-OPEN Ba trạng thái breaker. CLOSED = gọi bình thường. OPEN = không gọi, trả lỗi ngay ở 0 ms. HALF-OPEN = thả một request thăm dò. Chú ý: "closed" nghĩa là mạch thông, giống cầu dao điện — dễ nhớ ngược. failure_threshold Bao nhiêu lần lỗi liên tiếp thì breaker mở. Thấp = mở nhanh nh

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-006 · direct

**Query:** Circuit breaker và fallback chain đảm nhiệm hai vai trò khác nhau nào khi provider hỏng?

**Rationale:** Kiểm tra containment so với duy trì trải nghiệm người dùng.

### Required evidence

- `fee28308-52a9-5daa-9f5d-1c82e17133bf` — **Circuit Breakers, Caching & Re**, 11 · Circuit Breaker & Fallback
  - 03 Circuit Breaker & Fallback Circuit breaker ngắt gọi provider đang hỏng; fallback chain giữ trải nghiệm user ở mức chấp nhận được.

### Acceptable/alternate evidence

- `bbd9c2c5-a12f-5ee9-90f9-c687956a9d6c` — **Circuit Breakers, Caching & Re**, 4 · Mục tiêu & timeline 2 giờ
  - 01 Mục tiêu & timeline 2 giờ Tập trung vào reliability primitives: circuit breaker, fall- back, cache, metrics, chaos test.

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-007 · direct

**Query:** Context Recall thấp cho biết retriever đang gặp vấn đề gì?

**Rationale:** Kiểm tra phân biệt retrieve thiếu evidence với hallucination.

### Required evidence

- `80cd6dde-bdf8-5afb-a313-bcd30b9c5403` — **RAG Pipeline**, 116 · Context Recall (Độ Phủ Ngữ Cảnh)
  - Context Recall (Độ Phủ Ngữ Cảnh) Định nghĩa Retriever có mang về đủ thông tin cần thiết để trả lời trọn vẹn câu hỏi không? Bài toán Nếu câu hỏi cần 3 chứng cứ (A, B, C), nhưng hệ thống chỉ tìm được A và B → Recall thấp. Cách khắc phục ● Tối ưu hóa Vector DB ● Dùng Hybrid Search ● Tăng Top-K Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

### Acceptable/alternate evidence

- `a715fda9-515d-5cae-a3bd-1b03a70403ed` — **AI Evaluation & Benchmarking**, 45 · 4 RAGAS Metrics
  - 4 RAGAS Metrics Faithfulness Answer có dựa trên retrieved context không? Thấp = hallucination, bịa thông tin Context Recall Retriever có lấy đủ evidence không? Thấp = retrieve thiếu tài liệu quan trọng Answer Relevancy Answer có trả lời đúng câu hỏi không? Thấp = lạc đề, trả lời chung chung Context Precision Context retrieved có relevant không? Thấp = retrieve nhiều nhưng thừa, noise cao Giảng viên (VinUni) AICB · Evaluation 2026 38 / 76
- `e616b892-38db-5ea9-9b29-0ac6ca1f3cec` — **AI Evaluation & Benchmarking**, 18 · RAG Metrics — Bức Tranh T oàn Cảnh
  - RAG Metrics — Bức Tranh T oàn Cảnh Question Retriever Context Generator Answer Context Recall Context Precision Faithfulness Answer Relevancy Đọc kết quả Context Recall thấp = retrieve thiếu. Context Precision thấp = retrieve thừa. Faithfulness thấp = hallucinate. Answer Relevancy thấp = trả lời lạc đề. Giảng viên (VinUni) AICB · Evaluation 2026 14 / 76

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-008 · direct

**Query:** Tại sao similarity search đơn thuần chưa đủ và metadata filter đặt sai có thể làm recall giảm âm thầm?

**Rationale:** Kiểm tra metadata filtering và silent recall failure.

### Required evidence

- `d67640e0-122a-5532-a861-4a93c701d87c` — **Data Foundations**, 64 · Metadata Filtering & Hybrid
  - 09 Metadata Filtering & Hybrid Search Similarity thôi chưa đủ: filter đặt sai chỗ làm sập recall trong im lặng, và một số truy vấn chỉ BM25 mới giải được

### Acceptable/alternate evidence

- `995e871b-ce71-5b47-abc7-54b1be7e9c03` — **Vector Store & Feature Store**, 21 · RAG Pipeline: End-to-End Flow
  - RAG Pipeline: End-to-End Flow Documents Chunking Embedding Vector DB 512 tokens 50 overlap text-embed-3 bge-m3 User Query Query Embed Retrieve Top-K LLM Generate Metadata filter: source, date≥2024 Giảng viên (VinUni) AICB · Ngày 19 Tuần 4 19 / 56
- `52275ecd-b8ac-5a27-8974-d53e43d8ec4f` — **Production RAG**, 23 · Fix ONLINE — Retrieval & Aug
  - 05 Fix ONLINE — Retrieval & Aug- ment Hybrid Search, Metadata Filtering & Reranking — fix R và A

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-009 · prerequisite

**Query:** Cần hiểu những thành phần retrieval nào trước khi học công thức RRF?

**Rationale:** Yêu cầu nối dense/sparse ranked lists với rank fusion.

### Required evidence

- `156dd3dc-7d49-5fd5-a265-5866c21c6131` — **RAG Pipeline**, 54 · 2.2 Dense vs. Sparse Retrieval
  - 2.2 Dense vs. Sparse Retrieval Meaning vs. Keywords: Comparing the semantic understanding of dense vector embeddings against the exact-match precision of sparse retrieval algorithms like BM25.
- `51baf090-11e9-5a34-83ed-0b6674095dba` — **RAG Pipeline**, 66 · Thuật Toán Giải Quyết: RRF (Reciprocal Rank Fusion)
  - Thuật Toán Giải Quyết: RRF (Reciprocal Rank Fusion) • Đừng gộp điểm số (Scores), hãy gộp Thứ hạng (Ranks). RRF = 1/(k + Rank_Dense) + 1/(k + Rank_Sparse) (Giá trị hằng số k thường được chọn mặc định là 60) • Tài liệu nào nằm trong Top cao ở cả 2 bảng xếp hạng sẽ vươn lên vị trí số 1 tuyệt đối. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

### Acceptable/alternate evidence

- `7c038496-2887-5717-ace4-b305697ee246` — **RAG Pipeline**, 63 · 2.3 Hybrid Search Deep Dive
  - 2.3 Hybrid Search Deep Dive The best of both worlds: A deep dive into Hybrid Search, combining dense semantic vectors with sparse exact-match keywords using Reciprocal Rank Fusion (RRF) and Alpha-tuning.

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-010 · prerequisite

**Query:** Để xây agent có loop, retry, human approval và resume sau crash, cần hai khái niệm orchestration nền tảng nào?

**Rationale:** Kiểm tra state transitions và durable checkpoint trước workflow nâng cao.

### Required evidence

- `55a18c4e-4f7f-52a0-8d15-0c141fda1bd9` — **LangGraph & Agentic Orchestration**, 13 · State Machine: khái niệm cốt lõi
  - State Machine: khái niệm cốt lõi START plan execute done? END yes no: retry State: {messages, plan, tool_results, attempt, status, pending_approval} Python function đọc state và trả về partial update. Đường chuyển bước; có thể cố định hoặc conditional. Instructor (VinUni) AICB · Day 08 Week 5 8 / 25
- `cb113eb2-9c5a-5af3-936a-5affd816e40f` — **LangGraph & Agentic Orchestration**, 19 · Persistence & Time T ravel
  - 04 Persistence & Time T ravel Checkpointing biến graph thành workflow có thể pause, resume, replay và debug.

### Acceptable/alternate evidence

- `4fac6c46-aa89-5b40-ab1d-cc3d64358ec0` — **LangGraph & Agentic Orchestration**, 2 · HÃ Y SUY NGHĨ...
  - ? HÃ Y SUY NGHĨ... “Khi agent cần loop, retry, human approval và resume sau crash, chain một chiều còn đủ không?” Giữ câu hỏi này trong đầu khi học bài hôm nay

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-011 · prerequisite

**Query:** Trước khi chọn mô hình HITL, cần đánh giá cost of error và khả năng hoàn tác như thế nào?

**Rationale:** Kiểm tra risk model đứng trước approval routing.

### Required evidence

- `eede4ef2-9f19-55dd-b3aa-0c59516a68d5` — **Human-in-the**, 12 · Nguyên tắc: Cost of Interrupt vs Cost of Error
  - Nguyên tắc: Cost of Interrupt vs Cost of Error $10 Cost of error thấp → đừng hỏi 0.70 Confidence threshold mặc định $10K Cost of error cao → luôn hỏi Đo accuracy vs confidencetrên historical data. Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng lên. Đây là empirical tuning, không có magic number. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 7 / 17
- `3a5a32a3-adbe-5d40-866b-1b85fc1ef08e` — **Guardrails, HITL & Responsible AI**, 58 · 3 Mô Hình HITL
  - 3 Mô Hình HITL Human-on-the-loop Agent hành động Human review sau Low-risk, reversible Human-in-the-loop Agent đề xuất Human approve trước Medium-risk Human-as-tiebreaker Human quyết định Agent chỉ hỗ trợ High-stakes Mức độ rủi ro tăng dần → Nguyên tắc Chọn mô hình HITL dựa trên mức độ rủi ro và khả năng hoàn tác của hành động. Giảng viên (VinUni) AICB · Guardrails & HITL 2026 45 / 92

### Acceptable/alternate evidence

- `70a83b3d-ad09-5cad-8f4c-f3ec19ac278f` — **Guardrails, HITL & Responsible AI**, 59 · Khi Nào Cần Human?
  - Khi Nào Cần Human? Trigger Ví dụ HITL Model Irreversible action Gửi email, xoá data, publish Human-in-the-loop High-stakes decision Chuyển tiền, thay đổi policy Human-as-tiebreaker Tín hiệu bất thường Grounding check fail, tool trả lỗi Human-in-the-loop Edge case Input chưa gặp bao giờ Human-as-tiebreaker Sensitive topic Y tế, pháp lý, tài chính Human-in-the-loop Ghi nhớ HITL không phải thừa nhận AI yếu. HITL là feature — nó tăng độ tin cậy của sản phẩm. Giảng viên (VinUni) AICB · Guardrails & H
- `940bed7d-ac5e-5d89-93f9-746b291503c1` — **Human-in-the**, 5 · Agent tự ý hành động — chuyện gì xảy ra?
  - Agent tự ý hành động — chuyện gì xảy ra? User request Agent suy luận Xoá database Mất dữ liệu confidence 62% không ai kiểm tra! Không có approval gate Sự cố thực tế: ■ Agent CS auto-refund $50K không cần duyệt ■ Code agent xoá branch production ■ Email agent gửi nội bộ ra ngoài Lưu ý: Full autonomy chỉ an toàn khi mọi action đều reversible và low-cost. Trong thực tế, rất ít action thoả mãn cả hai. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 2 / 17

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-012 · prerequisite

**Query:** Muốn chẩn đoán một RAG pipeline trả lời kém, cần phân biệt bốn metric nền tảng nào trước?

**Rationale:** Kiểm tra mental model tách retriever, context và generator failures.

### Required evidence

- `e616b892-38db-5ea9-9b29-0ac6ca1f3cec` — **AI Evaluation & Benchmarking**, 18 · RAG Metrics — Bức Tranh T oàn Cảnh
  - RAG Metrics — Bức Tranh T oàn Cảnh Question Retriever Context Generator Answer Context Recall Context Precision Faithfulness Answer Relevancy Đọc kết quả Context Recall thấp = retrieve thiếu. Context Precision thấp = retrieve thừa. Faithfulness thấp = hallucinate. Answer Relevancy thấp = trả lời lạc đề. Giảng viên (VinUni) AICB · Evaluation 2026 14 / 76
- `a715fda9-515d-5cae-a3bd-1b03a70403ed` — **AI Evaluation & Benchmarking**, 45 · 4 RAGAS Metrics
  - 4 RAGAS Metrics Faithfulness Answer có dựa trên retrieved context không? Thấp = hallucination, bịa thông tin Context Recall Retriever có lấy đủ evidence không? Thấp = retrieve thiếu tài liệu quan trọng Answer Relevancy Answer có trả lời đúng câu hỏi không? Thấp = lạc đề, trả lời chung chung Context Precision Context retrieved có relevant không? Thấp = retrieve nhiều nhưng thừa, noise cao Giảng viên (VinUni) AICB · Evaluation 2026 38 / 76

### Acceptable/alternate evidence

- `34f77842-b9c2-5783-81c4-923a6ac5f897` — **RAG Pipeline**, 113 · 4.1 The RAG Evaluation Triad
  - 4.1 The RAG Evaluation Triad Discover the RAG Evaluation Triad—Context Recall, Faithfulness, and Answer Relevance—to quantitatively measure and debug your system's true performance.

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-013 · prerequisite

**Query:** Trước khi dùng GraphRAG cho câu hỏi multi-hop, cần nắm primitives nào của knowledge graph và entity-relation retrieval?

**Rationale:** Kiểm tra nodes/edges/triples trước graph traversal.

### Required evidence

- `ffd44b9e-f468-5502-8678-762eb52dff2d` — **GraphRAG & Knowledge Graphs**, 12 · Knowledge Graph
  - 2 Knowledge Graph Fundamentals Nodes, Edges, Triples — nền tảng của graph-based retrieval
- `af0f1602-fa18-5e3c-affd-ab0f12ac3ce8` — **Vector Store & Feature Store**, 26 · GraphRAG: Khi Quan Hệ Quan Trọng Hơn Đoạn Văn
  - GraphRAG: Khi Quan Hệ Quan Trọng Hơn Đoạn Văn Vector RAG (chunks) q T op-K nearest chunks(cosine similarity) GraphRAG (entity-relation) Alice Project X Bob PayPal Mahle worked_on by at hired_by q Multi-hop: PayPal→Alice→Project X→Bob→Mahle Câu hỏi mà vector RAG kém “Ai ở PayPal từng cộng tác với người được Mahle thuê?” — Vector trả về chunks về PayPal HOẶC Mahle riêng lẻ; không thể cross-document multi- hop. KG traverse 3-hop trong µs. Use Cases 2026 ■ P3C diabetes copilot (Memgraph): patient journey + drug interactions ■ Alzheimer research: 1.6M edges nối genes-drugs-trials ■ M&A intel (GlassDollar/Siemens, Mahle): entity search across millions of companies F Vector RAG = “đoạn văn liên qua

### Acceptable/alternate evidence

- `7c24ed09-58db-50e0-8c8f-dcd9b4d8eeff` — **GraphRAG — Truy xuất theo Quan hệ**, ☰ Từ điển thuật ngữ
  - ☰ Từ điển thuật ngữ Khi vector search thiếu quan hệ slide 1 · 4 GraphRAG & Knowledge Graphs AICB-P2T3 · Ngày 19 · Chương 4 — Agent Nâng Cao Knowledge graph primitives slide 8 · 11 Cấu trúc Vector RAG (Flat RAG) Tìm kiếm sự tương đồng về mặt ngữ nghĩa (Semantic similarity). Entity & relationship extraction slide 15 · 18 Đây là nguyên tử cơ bản để cấu trúc hóa kiến thức nhân loại. Graph construction & provenance slide 22 · 25 Entity Disambiguation  Ngôn ngữ có tính mơ hồ “Apple báo cáo doanh số i

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-014 · prerequisite

**Query:** Vì sao phải sửa chunking và candidate retrieval trước khi thêm reranker?

**Rationale:** Reranker không thể quét toàn DB hoặc phục hồi evidence chưa vào candidate set.

### Required evidence

- `f22da771-c78c-5b18-b296-aa9b0424afd3` — **Data Foundations**, 41 · Chunking & Chuẩn Bị Tài Liệu
  - 06 Chunking & Chuẩn Bị Tài Liệu Chunk sai thì mọi retrieval xây trên top- k đều sai theo — không mô hình embedding nào cứu được một chunk tồi
- `e19857c8-3111-5197-a94f-57b1006722b5` — **RAG Pipeline**, 77 · Hiệu Năng vs. Độ Chính Xác
  - Hiệu Năng vs. Độ Chính Xác Đặc điểm mô hình ● Cross-Encoder chấm điểm cực kỳ chính xác (như một người đọc kiểm tra chéo). ● Nhưng nó quá chậm và tốn compute. Không bao giờ được dùng Reranker để quét toàn bộ database. ● Chỉ dùng cho list nhỏ đã lọt qua vòng 1. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

### Acceptable/alternate evidence

- `c7bff788-d0be-5fb0-9978-ecbf66dae8a4` — **Production RAG**, 10 · Fix OFFLINE — Ingestion
  - 02 Fix OFFLINE — Ingestion Pipeline Data Processing: Chunking, Embedding & Enrichment
- `52275ecd-b8ac-5a27-8974-d53e43d8ec4f` — **Production RAG**, 23 · Fix ONLINE — Retrieval & Aug
  - 05 Fix ONLINE — Retrieval & Aug- ment Hybrid Search, Metadata Filtering & Reranking — fix R và A

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-015 · multi_hop

**Query:** Hãy nối chuỗi provider timeout → retry storm → circuit breaker → fallback và nêu evidence cần thấy trong chaos test.

**Rationale:** Kiểm tra causal chain và operational evidence qua nhiều spans.

### Required evidence

- `a4493d36-af27-5de7-9d9c-3a62d10307a9` — **Circuit Breakers, Caching & Re**, 9 · Case: cascading failure từ retry vô tội vạ
  - Case: cascading failure từ retry vô tội vạ Provider timeout Client retry 3 lần Quota/rate limit cạn Workflow outage Think-pair-share: 5 phút Hãy chọn một sản phẩm agent bạn biết. Nếu provider chính bị timeout 30 giây, người dùng sẽ thấy gì? Nhóm đề xuất một cách contain, isolate, recover. Retry chỉ là bước đầu. Nếu không có circuit breaker + fallback + budget, retry có thể biến lỗi nhỏ thành outage lớn. Instructor (VinUni) AICB · Day 10 Week 5 5 / 23
- `fee28308-52a9-5daa-9f5d-1c82e17133bf` — **Circuit Breakers, Caching & Re**, 11 · Circuit Breaker & Fallback
  - 03 Circuit Breaker & Fallback Circuit breaker ngắt gọi provider đang hỏng; fallback chain giữ trải nghiệm user ở mức chấp nhận được.
- `2aa5d5de-c0bd-58e5-93ca-011c2951c6d4` — **Circuit Breakers, Caching & Re**, 24 · Chaos testing: cố tình làm hỏng
  - Chaos testing: cố tình làm hỏng Chaos scenarios trong lab 1. Primary provider timeout 100%. 2. Primary provider intermittent 50%. 3. Cache returns stale candidate. 4. Cost cap gần cạn. Expected evidence ■ Circuit chuyển CLOSED → OPEN. ■ Gateway route sang fallback. ■ Không retry storm. ■ Metrics/report ghi rõ recovery time. Mini design review - 7 phút Mỗi nhóm viết 1 chaos scenario mới và metric chứng minh system recover. Nhóm khác phản biện: scenario đó có side effect không? Instructor (VinUni) AICB · Day 10 Week 5 17 / 23

### Acceptable/alternate evidence

- `4090f69a-a543-5d78-861f-d1ac9cd0ed11` — **Circuit Breakers, Caching & Reliability — phân tích & breakdown từng slide**, A–Z Từ điển thuật ngữ
  - A–Z Từ điển thuật ngữ Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện. Circuit breaker Cơ chế ngừng gọi một dịch vụ đang hỏng, thay vì cứ thử mãi. Không sửa được nguyên nhân — chỉ ngăn nó lan rộng. CLOSED / OPEN / HALF-OPEN Ba trạng thái breaker. CLOSED = gọi bình thường. OPEN = không gọi, trả lỗi ngay ở 0 ms. HALF-OPEN = thả một request thăm dò. Chú ý: "closed" nghĩa là mạch thông, giống cầu dao điện — dễ nhớ ngược. failure_threshold Bao nhiêu lần lỗi liên tiếp thì breaker mở. Thấp = mở nhanh nh

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-016 · multi_hop

**Query:** Citation UX, strict grounding và RAG evaluation phối hợp thế nào để người học kiểm chứng câu trả lời?

**Rationale:** Kiểm tra grounding policy, source inspection và quality metrics.

### Required evidence

- `f5461031-4984-5dd2-a497-c2d28a93be42` — **RAG Pipeline**, 92 · 3.2 Prompt Engineering for Strict Grounding
  - 3.2 Prompt Engineering for Strict Grounding Taming the LLM: Discover how to construct robust system prompts that enforce strict citations, prevent hallucinations, and gracefully handle knowledge gaps.
- `88d9b904-3ebf-564e-86cf-84f01ee72fcd` — **RAG Pipeline**, 102 · Inline Citations (Trích Dẫn Trong Dòng)
  - Inline Citations (Trích Dẫn Trong Dòng) • Giống Wikipedia: Đặt các reference ID ngay sát bên cạnh thông tin kiện. • Góc độ UI/UX: Các ID này (ví dụ [1], [2]) nên là hyperlink. Khi hover/click vào, nó sẽ popup ra đoạn text gốc để user đối chiếu nhanh. AI ASSISTANT MOCKUP Hoàn tiền diễn ra trong 7 ngày [1] Source: Refund_Policy.pdf Section 3: All verified claims are processed within 7 business days. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2
- `e616b892-38db-5ea9-9b29-0ac6ca1f3cec` — **AI Evaluation & Benchmarking**, 18 · RAG Metrics — Bức Tranh T oàn Cảnh
  - RAG Metrics — Bức Tranh T oàn Cảnh Question Retriever Context Generator Answer Context Recall Context Precision Faithfulness Answer Relevancy Đọc kết quả Context Recall thấp = retrieve thiếu. Context Precision thấp = retrieve thừa. Faithfulness thấp = hallucinate. Answer Relevancy thấp = trả lời lạc đề. Giảng viên (VinUni) AICB · Evaluation 2026 14 / 76

### Acceptable/alternate evidence

- `a8f844b0-7b57-5c24-9329-10165fcf267b` — **Guardrails, HITL & Responsible AI**, 104 · Trust UX Trong Thực Tế
  - Trust UX Trong Thực Tế Feature Cách implement Tại sao quan trọng Show sources Citation từ RAG pipeline User verify được thông tin Confidence badge High / Medium / Low Set đúng expectation Action preview “Tôi sẽ gửi email này...” User kiểm soát trước khi thực hiện Undo có thời hạn “Đã gửi. [Hoàn tác trong 30s]” Biến hành động không hoàn tác được thành hoàn tác được Liên kết Đây là mặt người dùng nhìn thấy của những thứ đã dựng ở §11–13: audit trail thành “lịch sử hành động”, escalation thành “act
- `34f77842-b9c2-5783-81c4-923a6ac5f897` — **RAG Pipeline**, 113 · 4.1 The RAG Evaluation Triad
  - 4.1 The RAG Evaluation Triad Discover the RAG Evaluation Triad—Context Recall, Faithfulness, and Answer Relevance—to quantitatively measure and debug your system's true performance.

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-017 · multi_hop

**Query:** Vì sao error rate bằng 0 vẫn có thể che giấu silent degradation, và SLI/SLO nào phải bổ sung cho LLM agent?

**Rationale:** Nối content quality failure với SLI/SLO và observability.

### Required evidence

- `3cb697bf-be80-5961-be4e-9537b58c42eb` — **Circuit Breakers, Caching & Re**, 10 · Silent degradation: không lỗi nhưng chất lượng giảm
  - Silent degradation: không lỗi nhưng chất lượng giảm time quality error rate = 0% faithfulness giảm dần Nguyên nhân thường gặp ■ Provider cập nhật model silently . ■ Prompt/schema thay đổi nhưng eval không đổi. ■ Knowledge base stale hoặc retrieval yếu. ■ Cache trả câu đúng cũ nhưng sai hiện tại. Lưu ý: Quality SLO phải đi cùng uptime SLO. Error rate = 0% không đủ. Instructor (VinUni) AICB · Day 10 Week 5 6 / 23
- `73c69027-0cba-560e-ab0f-1f94d9e23f7b` — **Circuit Breakers, Caching & Re**, 22 · SLI, SLO, SLA cho LLM agent
  - SLI, SLO, SLA cho LLM agent Khái niệm Ý nghĩa Ví dụ trong lab SLI metric đo được availability, P95 latency, cache hit rate, false-hit rate SLO target nội bộ availability ≥ 99%, P95 < 2.5s, fallback success ≥ 95% SLA cam kết bên ngoài 99.5% uptime/tháng cho customer-facing API Error budget mức lỗi được phép nếu burn rate cao → freeze fea- ture, ưu tiên reliability Lưu ý: LLM agent cần thêm quality SLO: faithfulness, safety pass rate, escalation correctness. Instructor (VinUni) AICB · Day 10 Week 5 15 / 23
- `448e2003-d150-5c77-975e-c0c6da0f74a5` — **Circuit Breakers, Caching & Re**, 21 · Observability & SLO
  - 05 Observability & SLO Không đo thì không biết system đang tốt, chậm, đắt, hay đang trả lời sai.

### Acceptable/alternate evidence

- Không có trong candidate hiện tại.

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-018 · multi_hop

**Query:** Từ tài liệu thô đến top-k chính xác, chunking, hybrid retrieval và reranking tác động nối tiếp nhau ra sao?

**Rationale:** Kiểm tra dependency chain offline ingestion → retrieval → re-score.

### Required evidence

- `f22da771-c78c-5b18-b296-aa9b0424afd3` — **Data Foundations**, 41 · Chunking & Chuẩn Bị Tài Liệu
  - 06 Chunking & Chuẩn Bị Tài Liệu Chunk sai thì mọi retrieval xây trên top- k đều sai theo — không mô hình embedding nào cứu được một chunk tồi
- `711e564d-14fa-51fe-b56d-66ab8b8632c1` — **Production RAG**, 24 · Hybrid Search — BM25 + Dense Vector Fusion
  - Hybrid Search — BM25 + Dense Vector Fusion User Query BM25 exact keywords Rank A Dense Vector semantic match Rank BRRF Fusion Top-K Results Không cần GPU Cần embedding model Merge rankings đơn giản: score (d) = ∑ 1 k+ranki(d) . Không cần training, production standard. M.Sc Trần Minh Tú (VinUni) AICB · Ngày 18 Tuần 4 17 / 42
- `e19857c8-3111-5197-a94f-57b1006722b5` — **RAG Pipeline**, 77 · Hiệu Năng vs. Độ Chính Xác
  - Hiệu Năng vs. Độ Chính Xác Đặc điểm mô hình ● Cross-Encoder chấm điểm cực kỳ chính xác (như một người đọc kiểm tra chéo). ● Nhưng nó quá chậm và tốn compute. Không bao giờ được dùng Reranker để quét toàn bộ database. ● Chỉ dùng cho list nhỏ đã lọt qua vòng 1. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

### Acceptable/alternate evidence

- `c7bff788-d0be-5fb0-9978-ecbf66dae8a4` — **Production RAG**, 10 · Fix OFFLINE — Ingestion
  - 02 Fix OFFLINE — Ingestion Pipeline Data Processing: Chunking, Embedding & Enrichment
- `52275ecd-b8ac-5a27-8974-d53e43d8ec4f` — **Production RAG**, 23 · Fix ONLINE — Retrieval & Aug
  - 05 Fix ONLINE — Retrieval & Aug- ment Hybrid Search, Metadata Filtering & Reranking — fix R và A

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-019 · multi_hop

**Query:** Context Recall và Context Precision thấp biểu hiện hai lỗi khác nhau nào, và thứ tự sửa pipeline nên ra sao?

**Rationale:** Kiểm tra phân biệt retrieve thiếu/thừa và mapping sang fix.

### Required evidence

- `a715fda9-515d-5cae-a3bd-1b03a70403ed` — **AI Evaluation & Benchmarking**, 45 · 4 RAGAS Metrics
  - 4 RAGAS Metrics Faithfulness Answer có dựa trên retrieved context không? Thấp = hallucination, bịa thông tin Context Recall Retriever có lấy đủ evidence không? Thấp = retrieve thiếu tài liệu quan trọng Answer Relevancy Answer có trả lời đúng câu hỏi không? Thấp = lạc đề, trả lời chung chung Context Precision Context retrieved có relevant không? Thấp = retrieve nhiều nhưng thừa, noise cao Giảng viên (VinUni) AICB · Evaluation 2026 38 / 76
- `18438e91-32b6-5ee6-a19d-c90c9c845b7f` — **AI Evaluation & Benchmarking**, 49 · Diagnostic Flowchart — Score Thấp, Fix Ở Đâu?
  - Diagnostic Flowchart — Score Thấp, Fix Ở Đâu? Faithfulness thấp? Context Recall thấp? Context Precision thấp? Answer Relevancy thấp? ⇒ Prompt: “only answer from context” ⇒ Tăng top-k, re-chunk nhỏ hơn ⇒ Re-ranking, semantic filter ⇒ Prompt clearer, answer template Thứ tự fix Context Recall → Context Precision → Faithfulness → Answer Relevancy. Fix retriever trước, generator sau. Giảng viên (VinUni) AICB · Evaluation 2026 42 / 76

### Acceptable/alternate evidence

- `e616b892-38db-5ea9-9b29-0ac6ca1f3cec` — **AI Evaluation & Benchmarking**, 18 · RAG Metrics — Bức Tranh T oàn Cảnh
  - RAG Metrics — Bức Tranh T oàn Cảnh Question Retriever Context Generator Answer Context Recall Context Precision Faithfulness Answer Relevancy Đọc kết quả Context Recall thấp = retrieve thiếu. Context Precision thấp = retrieve thừa. Faithfulness thấp = hallucinate. Answer Relevancy thấp = trả lời lạc đề. Giảng viên (VinUni) AICB · Evaluation 2026 14 / 76

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:

## ret-020 · multi_hop

**Query:** Vì sao vector RAG gặp khó với câu hỏi quan hệ nhiều bước, còn GraphRAG cần nodes, edges và triples để giải quyết?

**Rationale:** Kiểm tra sự khác biệt semantic similarity và relationship traversal.

### Required evidence

- `af0f1602-fa18-5e3c-affd-ab0f12ac3ce8` — **Vector Store & Feature Store**, 26 · GraphRAG: Khi Quan Hệ Quan Trọng Hơn Đoạn Văn
  - GraphRAG: Khi Quan Hệ Quan Trọng Hơn Đoạn Văn Vector RAG (chunks) q T op-K nearest chunks(cosine similarity) GraphRAG (entity-relation) Alice Project X Bob PayPal Mahle worked_on by at hired_by q Multi-hop: PayPal→Alice→Project X→Bob→Mahle Câu hỏi mà vector RAG kém “Ai ở PayPal từng cộng tác với người được Mahle thuê?” — Vector trả về chunks về PayPal HOẶC Mahle riêng lẻ; không thể cross-document multi- hop. KG traverse 3-hop trong µs. Use Cases 2026 ■ P3C diabetes copilot (Memgraph): patient journey + drug interactions ■ Alzheimer research: 1.6M edges nối genes-drugs-trials ■ M&A intel (GlassDollar/Siemens, Mahle): entity search across millions of companies F Vector RAG = “đoạn văn liên qua
- `f62efc80-1b8e-5b99-98e4-fcd6b3ce95bd` — **GraphRAG & Knowledge Graphs**, 26 · Pipeline GraphRAG Tiêu
  - 3 Pipeline GraphRAG Tiêu chuẩn Hành trình từ Câu hỏi của User đến Câu trả lời của LLM
- `ffd44b9e-f468-5502-8678-762eb52dff2d` — **GraphRAG & Knowledge Graphs**, 12 · Knowledge Graph
  - 2 Knowledge Graph Fundamentals Nodes, Edges, Triples — nền tảng của graph-based retrieval

### Acceptable/alternate evidence

- `7c24ed09-58db-50e0-8c8f-dcd9b4d8eeff` — **GraphRAG — Truy xuất theo Quan hệ**, ☰ Từ điển thuật ngữ
  - ☰ Từ điển thuật ngữ Khi vector search thiếu quan hệ slide 1 · 4 GraphRAG & Knowledge Graphs AICB-P2T3 · Ngày 19 · Chương 4 — Agent Nâng Cao Knowledge graph primitives slide 8 · 11 Cấu trúc Vector RAG (Flat RAG) Tìm kiếm sự tương đồng về mặt ngữ nghĩa (Semantic similarity). Entity & relationship extraction slide 15 · 18 Đây là nguyên tử cơ bản để cấu trúc hóa kiến thức nhân loại. Graph construction & provenance slide 22 · 25 Entity Disambiguation  Ngôn ngữ có tính mơ hồ “Apple báo cáo doanh số i

- [ ] Approve
- [ ] Sửa query/class
- [ ] Sửa required/acceptable sources
- Ghi chú:
