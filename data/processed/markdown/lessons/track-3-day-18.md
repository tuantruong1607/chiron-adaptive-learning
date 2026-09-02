---
schema_version: 1
course_id: rag-intensive
document_id: "cef2a66a-bf91-5c07-80fd-4163716c07b9"
document_version_id: "b8d0b1bc-4184-52df-803c-9fb29560e9b3"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Production RAG — Từ Ingestion đến Eval"
source_file: "track-3-day-18.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-18.html"
source_sha256: "0b9bd4f4630996dfec2b5ba23c1345b0ff87133d4f79d151e861187092a628a4"
parser_version: chiron-structured-markdown-v1
html_section_count: 20
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# Production RAG — Từ Ingestion đến Eval

> Thiết kế hai pipeline offline/online, đo retrieval riêng với generation và giữ context trong ngân sách.

<!-- chiron-source-span: {"source_span_id":"de9ef1c5-821a-55bd-9eda-76ae334fda61","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"track-3-day-18.html"},"checksum":"4d3da086204b2640acc28fb70acd2e069a8000f50692754fd6204186cb31e32c"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: offline và online pipeline có failure mode khác nhau. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"8b24cc1b-c670-5f5c-9795-d8905d363b9c","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"track-3-day-18.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

## ◎ Bản đồ tư duy trước khi học

Ba hình dưới đây là khung nối kiến thức với quyết định vận hành; chúng không thay thế nội dung slide.

| Tín hiệu đầu vào | Cơ chế quyết định | Đầu ra cần kiểm |
| --- | --- | --- |
| Yêu cầu, state, ràng buộc | Chuẩn hóa → đánh giá → route | Kết quả + evidence + telemetry |
| Failure hoặc uncertainty | Retry có giới hạn / escalation | Trạng thái bền vững, không nhân đôi tác dụng phụ |

Hình 1 — Mental model production: dữ liệu đi qua quyết định có kiểm soát, không đi thẳng vào model.

| Lớp | Câu hỏi phải trả lời | Failure mode nếu bỏ qua |
| --- | --- | --- |
| Quality | Đầu ra có đúng và grounded? | Demo đẹp nhưng sai ngầm |
| Reliability | Restart, timeout, retry có an toàn? | Mất state hoặc tác dụng phụ trùng |
| Economics | Latency và chi phí ở p95 là bao nhiêu? | Pilot được nhưng không scale |
| Governance | Ai có quyền làm gì, audit ở đâu? | Không thể vận hành có trách nhiệm |

Hình 2 — Bốn lăng kính dùng để đọc mọi quyết định trong bài.

| Mức bằng chứng | Dùng để làm gì | Không được suy diễn |
| --- | --- | --- |
| Trích slide | Nhắc lại định nghĩa và con số | Không biến ví dụ thành benchmark chung |
| Phép tính mô-đun | Phân tích độ nhạy của giả định | Không gọi là số đo production |
| Telemetry thực | Ra quyết định deploy/rollback | Không thay thế đánh giá nhân quả |

Hình 3 — Tách nguồn slide, mô hình tính và dữ liệu vận hành để không tạo “độ chính xác giả”.

---

<!-- chiron-source-span: {"source_span_id":"3a0e58a2-9b61-56d7-9da7-28a71db8bf66","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Production RAG mental model","source_file":"track-3-day-18.html"},"checksum":"eacc145b94a5b9fd8916e9a8a8728c843be86bf8bba05a0f0e8d1289d1f3d23f"} -->

## 01 Production RAG mental model

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Production RAG mental model · Mental model & quyết định

> Trích slide Slide 1: Production RAG AICB-P2T3 · Ngày 18 · Chương 4 — Agent Nâng Cao M.Sc Trần Minh Tú VinUniversity · Phase 2 · Track3 ·Tuần4

Production RAG AICB-P2T3 · Ngày 18 · Chương 4 — Agent Nâng Cao M.Sc Trần Minh Tú VinUniversity · Phase 2 · Track3 ·Tuần4. Điểm nối sang production là: offline và online pipeline có failure mode khác nhau. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- “Tại sao RAG pipeline demo chạy tốt nhưng production accuracy chỉ đạt 60% — ingestion hay retrieval đang giết bạn?” Giữcâu hỏi này trong đầu khihọc bài hôm nay
- Ingestion & Retrieval — failure nằm ở đâu trong pipeline?
- RAGPipeline — Tổng quan ONLINE &OFFLINE Output Query/ Question RAG StorageLayer ONLINE OFFLINE Data Data Processing Data → Data Processing → Storage Layer.

#### Tự kiểm tra · Với production rag mental model, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là offline và online pipeline có failure mode khác nhau.

### Slide 3 Production RAG mental model · Evidence & failure lens

> Trích slide Slide 3: Nộidung bài học 1. Tạisao Basic RAG thất bại? 2. FixOFFLINE — Ingestion Pipeline 3. EnrichmentPipeline 4. FixONLINE — PreRAG 5. FixONLINE — Retrieval & Augment 6. FixONLINE — Generate & PostRAG 7. Evaluation— Đo lường RAG Pipeline 8. AgenticRAG 9. RAGvẫn chưa giải quyết đượcmọi thứ 10. Demo& Thực hành M.ScTrầnMinh Tú (VinUni)…

**Đọc như kỹ sư:** Nộidung bài học 1. Tạisao Basic RAG thất bại? 2. FixOFFLINE — Ingestion Pipeline 3. EnrichmentPipeline 4. FixONLINE — PreRAG 5. FixONLINE — Retrieval & Augment 6. FixONLINE — Generate & PostRAG 7. Evaluation— Đo lường RAG Pipeline 8. AgenticRAG 9. RAGvẫn chưa

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 3 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 5 Production RAG mental model · Evidence & failure lens

> Trích slide Slide 5: RAGPipeline — Tổng quan ONLINE &OFFLINE Output Query/ Question RAG StorageLayer ONLINE OFFLINE Data Data Processing Data → Data Processing → Storage Layer. Chạy 1 lần (hoặc khi data thay đổi). “Garbage in, garbageout.” Query → RAG → Output. Chạy mỗi query. Production accuracy chỉ 55– 65%—tại sao? M.ScTrầnMinh Tú (VinUni) AICB·…

**Đọc như kỹ sư:** RAGPipeline — Tổng quan ONLINE &OFFLINE Output Query/ Question RAG StorageLayer ONLINE OFFLINE Data Data Processing Data → Data Processing → Storage Layer.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- “Garbage in, garbageout.” Query → RAG → Output.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 5 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"d4af9c53-521f-55ee-859f-9068ff0a98dc","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Offline ingestion pipeline","source_file":"track-3-day-18.html"},"checksum":"5af0fe9311a7a87cfb7f71bfb480131c424e5e6cf63e130555a0cc4c0ae47ced"} -->

## 02 Offline ingestion pipeline

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 6 Offline ingestion pipeline · Mental model & quyết định

> Trích slide Slide 6: OFFLINEPipeline — Failure ở đâu? Data Data Processing StorageLayer • Datasai • Datacó chất lượngthấp • Chunking Mismatch • Embedding Mismatch • Metadatathiếu • Parsingchưa tốt • Frameworkquản trịchưa tốt Lưuý: Trongthựctế: chỉcóingestionpipelinelàchưađủ. EnrichmentPipeline sẽ…

Data Data Processing StorageLayer • Datasai • Datacó chất lượngthấp • Chunking Mismatch • Embedding Mismatch • Metadatathiếu • Parsingchưa tốt • Frameworkquản trịchưa tốt Lưuý: Trongthựctế: chỉcóingestionpipelinelàchưađủ.. Điểm nối sang production là: chunk theo đơn vị nghĩa trước khi theo số token.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- EnrichmentPipeline sẽ giúpchúngtalàmgiàuthêmthôngtin(contextualembeddings,metadataextraction, datacleaning).
- Production RAGcần fixtoànbộ chuỗi,không chỉ 1 bước.
- ErrorTreeAnalysis — Log từngbước, tìm đúng chỗ sai Query PreRAG R·A·G PostRAG Output Log: raw query Log: rewrittenquery+ intent Log: chunks+scores Log: answer+eval scores Log: output+feedback Outputđúng?

#### Tự kiểm tra · Với offline ingestion pipeline, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là chunk theo đơn vị nghĩa trước khi theo số token.

### Slide 9 Offline ingestion pipeline · Evidence & failure lens

> Trích slide Slide 9: Bằngchứng: Gap giữaNaive và Production RAG 60% Naive RAG Accuracy 85%+ Production RAG Accuracy +25% Improvement khi optimize Metric NaiveRAG Production RAG Nguyên nhâncải thiện Faithfulness ∼0.70 ≥0.85 Betterprompt + reranking ContextRecall ∼0.55 ≥0.75 Hybridsearch + enrichment ContextPrecision ∼0.50 ≥0.75 Reranking+ metadata…

**Đọc như kỹ sư:** Bằngchứng: Gap giữaNaive và Production RAG 60% Naive RAG Accuracy 85%+ Production RAG Accuracy +25% Improvement khi optimize Metric NaiveRAG Production RAG Nguyên nhâncải thiện Faithfulness ∼0.70 ≥0.85 Betterprompt + reranking ContextRecall ∼0.55 ≥0.75 Hybrids

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 9 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 11 Offline ingestion pipeline · Evidence & failure lens

> Trích slide Slide 11: IngestionPipeline — Mỗi bước fix 1failure từ Section 1 Document PDF/HTML/MD Parse extracttext Clean noiseremoval Chunk hierarchical Metadata date,source Enrich LLMcontext Fix: Parsing chưa tốt Fix: Data chất lượng thấp Fix: Chunking Mismatch Fix: Metadata thiếu Fix: Embedding Mismatch Embed text→vector Index VectorDB Slide1.2…

**Đọc như kỹ sư:** Pipelinenày fixtừngfailure một: Parse →Clean →Chunk →Metadata →Enrich.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Bỏ bước nào = để lọt failure đó vào VectorDB.
- Lưu ý: “Garbage in, garbage out” — mỗi bước bỏ qua sẽtích lũy lỗi.
- Parse sai → chunk sai → embed sai →retrievesai →outputsai.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 11 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"fabdf6d2-32c8-59e5-84f0-1f27642eff93","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Parsing & enrichment","source_file":"track-3-day-18.html"},"checksum":"b9a0607b23fe44b73bf635c646e4f78e1ba0e1291ad65e342d939b22b13a37c6"} -->

## 03 Parsing & enrichment

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 12 Parsing & enrichment · Mental model & quyết định

> Trích slide Slide 12: 3Chunking Strategies — So sánh Fixed-size Chunk1 Chunk2 Chunk3 cắt giữa câu! Semantic Chủđề A Chủđề B Chủđề C nhóm theo similarity Hierarchical Parentchunk (full context) Child1 Child2 Child3 retrieve child, return parent Hierarchical (parent-child) nên làde- fault: chunks nhỏ cho retrieval preci- sion+ chunks lớn cho LLM…

3Chunking Strategies — So sánh Fixed-size Chunk1 Chunk2 Chunk3 cắt giữa câu!. Điểm nối sang production là: metadata là tín hiệu retrieval, không phải trang trí. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Semantic Chủđề A Chủđề B Chủđề C nhóm theo similarity Hierarchical Parentchunk (full context) Child1 Child2 Child3 retrieve child, return parent Hierarchical (parent-child) nên làde- fault: chunks nhỏ cho retrieval preci- sion+ chunks lớn cho LLM context.
- Fixed: 512 tokens, overlap64 Semantic: cosine threshold 0.85 Hierarchical: parent 2048, child256 M.ScTrầnMinh Tú (VinUni)
- AdvancedChunking — Structure-Aware& LateChunking Parse markdown headers, HTML tags, PDF sections rồi chunk theo logicalstructure.

#### Tự kiểm tra · Với parsing & enrichment, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là metadata là tín hiệu retrieval, không phải trang trí.

### Slide 15 Parsing & enrichment · Evidence & failure lens

> Trích slide Slide 15: ContextualEmbeddings — Anthropic’sContextual Retrieval Chunkgốc “Nhânviên được nghỉ 12 ngày/năm.” LLMprepend context ClaudeHaiku / GPT-4o-mini Contextualchunk “TríchChương 3 — Chính sáchnghỉ phép Sổtay VinUni2024. NV được nghỉ 12 ngày/năm.” Embed→Index Ýtưởng(Anthropic,Sep2024) — Trước khi embed mỗi chunk, dùng LLM prepend 1…

**Đọc như kỹ sư:** ContextualEmbeddings — Anthropic’sContextual Retrieval Chunkgốc “Nhânviên được nghỉ 12 ngày/năm.” LLMprepend context ClaudeHaiku / GPT-4o-mini Contextualchunk “TríchChương 3 — Chính sáchnghỉ phép Sổtay VinUni2024.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- NV được nghỉ 12 ngày/năm.” Embed→Index Ýtưởng(Anthropic,Sep2024) — Trước khi embed mỗi chunk, dùng LLM prepend 1 đoạn context ngắn giải thích chunk nằm ở đâu trong document.
- Retrievalfailure giảm49%(alone) Giảm 67% khi kết hợp Contextual BM25+ Reranking Lưuý: Trade-off: +1LLMcall/chunkkhiindexing (one-time).

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 15 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 17 Parsing & enrichment · Evidence & failure lens

> Trích slide Slide 17: 03 Enrichment Pipeline Làm giàu chunks trước khi embed — Summarize, HyQA, Meta- data

**Đọc như kỹ sư:** 03 Enrichment Pipeline Làm giàu chunks trước khi embed — Summarize, HyQA, Meta- data

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 17 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"e584842f-95fd-52a4-80ba-6cb7728e0c86","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Chunking strategy","source_file":"track-3-day-18.html"},"checksum":"d952aa2799c4359e9ed7411b6a78d991f8d61fe37ab10debac32bef1549ed627"} -->

## 04 Chunking strategy

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 18 Chunking strategy · Mental model & quyết định

> Trích slide Slide 18: EnrichmentPipeline — Tại sao cần “làmgiàu” chunks? Raw Chunk Summarize HypothesisQ&A Contextual Prepend AutoMetadata Enriched Chunk Song song — LLM-powered, one-time, offline Raw chunks thiếu context→ embed- dingchỉ capture surface meaning. Enrichment = thêm thông tintrước khi embedđể vector representations phongphú hơn. 4…

EnrichmentPipeline — Tại sao cần “làmgiàu” chunks?. Điểm nối sang production là: hybrid search giảm blind spot giữa semantic và exact term. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Raw Chunk Summarize HypothesisQ&A Contextual Prepend AutoMetadata Enriched Chunk Song song — LLM-powered, one-time, offline Raw chunks thiếu context→ embed- dingchỉ capture surface meaning.
- Enrichment = thêm thông tintrước khi embedđể vector representations phongphú hơn.
- 4 techniquesđộc lập→chạy parallel trênmỗi chunk.

#### Tự kiểm tra · Với chunking strategy, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là hybrid search giảm blind spot giữa semantic và exact term.

### Slide 20 Chunking strategy · Evidence & failure lens

> Trích slide Slide 20: 04 Fix ONLINE — PreRAG Query Transform, Corrective RAG — fix trước khi search

**Đọc như kỹ sư:** 04 Fix ONLINE — PreRAG Query Transform, Corrective RAG — fix trước khi search

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 20 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 22 Chunking strategy · Evidence & failure lens

> Trích slide Slide 22: CorrectiveRAG & Adaptive Retrieval Query Retrieve EvaluateQuality Generate WebSearch orRewrite good low Nếuretrieval quality thấp: 1. Triggerwebsearch (fallback) 2. Hoặcqueryrewrite rồiretry 3. Rồi mới generate Tránhgenerate trên bad context Routequeries theo complexity: Simple →directLLM (no RAG) Medium →standardRAG Complex…

**Đọc như kỹ sư:** CorrectiveRAG & Adaptive Retrieval Query Retrieve EvaluateQuality Generate WebSearch orRewrite good low Nếuretrieval quality thấp: 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Rồi mới generate Tránhgenerate trên bad context Routequeries theo complexity: Simple →directLLM (no RAG) Medium →standardRAG Complex →fullpipeline + rerank Giảmlatency 40%trungbình M.ScTrầnMinh Tú (VinUni)

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 22 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"3a5b8cd5-0d78-5661-a1a7-738aa8fa42fb","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 Embedding & indexing","source_file":"track-3-day-18.html"},"checksum":"b050b6a6fe15fc13badd5ddc641cc17a4d640cca7a729ab3e46e7f04b3b0ab5f"} -->

## 05 Embedding & indexing

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 23 Embedding & indexing · Mental model & quyết định

> Trích slide Slide 23: 05 Fix ONLINE — Retrieval & Aug- ment Hybrid Search, Metadata Filtering & Reranking — fix R và A

05 Fix ONLINE — Retrieval & Aug- ment Hybrid Search, Metadata Filtering & Reranking — fix R và A. Điểm nối sang production là: reranker dùng sau candidate retrieval, không thay retriever. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- HybridSearch — BM25 + Dense VectorFusion UserQuery BM25 exactkeywords RankA DenseVector semanticmatch RankBRRFFusion Top-KResults Không cần GPU Cần embedding model Merge rankings đơn giản: score(d) = ∑ 1 k+ranki(d).
- Tiêuchí BM25 DenseVector Hybrid Exactkeywords Tốt Yếu Tốt Synonyms/ paraphrase Yếu Tốt Tốt Multilingual Yếu Tốt Tốt GPUrequired Không Có Có Latency <5ms ∼20ms ∼25ms Lưu ý:BM25 cho tiếng Việt: cầnword segmentation(underthesea, VnCoreNLP) trướckhi index.
- BeyondRRF — TensorFusion,Late Interaction & Learned Sparse Tensor Fusion là gì?

#### Tự kiểm tra · Với embedding & indexing, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là reranker dùng sau candidate retrieval, không thay retriever.

### Slide 26 Embedding & indexing · Evidence & failure lens

> Trích slide Slide 26: BeyondRRF — TensorFusion,Late Interaction & Learned Sparse Tensor Fusion là gì? — Thay vì concatenate vectors (ghép nối), tensor fusion tính outer product giữa feature vectors từ các modali- ties/signalskhác nhau. Tạo ra tensor đa chiều mapmọi tương tácgiữa features của BM25 signal và Dense signal→ cap- turecross-signal…

**Đọc như kỹ sư:** BeyondRRF — TensorFusion,Late Interaction & Learned Sparse Tensor Fusion là gì?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- — Thay vì concatenate vectors (ghép nối), tensor fusion tính outer product giữa feature vectors từ các modali- ties/signalskhác nhau.
- Tạo ra tensor đa chiều mapmọi tương tácgiữa features của BM25 signal và Dense signal→ cap- turecross-signal interactions mà RRF bỏ lỡ.
- Query tokens↔ doc tokens→ MaxSim per query token.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 26 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 28 Embedding & indexing · Evidence & failure lens

> Trích slide Slide 28: VectorDB cho Production RAG DB HybridSearch Metadata Filter Khi nào? Qdrant Built-in Rich Defaultpick Weaviate Built-in Rich GraphQLfans Pinecone Sparse+ Good Managed/SaaS Milvus Built-in Rich Large-scale,GPU Neo4j Vector+Graph Cypher GraphRAG pgvector Manual SQL AlreadyPostgres Chroma — Basic Prototype FAISS — — Researchonly…

**Đọc như kỹ sư:** VectorDB cho Production RAG DB HybridSearch Metadata Filter Khi nào?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- GraphRAG: Neo4j (vector + graph traversal).Lab: Qdrant local (Docker).

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 28 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"f11d366f-0f2f-54ed-b8f1-020ecca084d5","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Pre-retrieval routing","source_file":"track-3-day-18.html"},"checksum":"e64c537e2d4cb3f79ac1d23c94289701517d57fb55a02b2cb9c595cd0dfe7f4b"} -->

## 06 Pre-retrieval routing

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 29 Pre-retrieval routing · Mental model & quyết định

> Trích slide Slide 29: Reranking— Highest ROI Optimization Retrievetop-20 Cross-Encoder rerank Passtop-3→LLM ∼1ms ∼50ms +15–25% precision Bi: encoderiêng,fast( ∼1ms),nointeraction Cross: encode cùng, chậm (∼50ms), accu- ratehơn nhiều RerankingModels — So sánh: Model Cost Note CohereRerank v3.5 API Productiondefault bge-reranker-v2-m3 Free…

Augmentation— Nâng cao context trước khiđưa vào LLM NLImodelkiểmtra entailmentgiữaqueryvàchunk.. Điểm nối sang production là: top-k lớn hơn có thể làm giảm answer quality. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Prompt: “Cite sources using[1], [2]...” Output: answer + citations+ source links.
- Resolveconflicts: newest winshoặc LLM arbitrate.
- Lưuý: Augmentation=bướcgiữaRetrievalvàGeneration.

#### Tự kiểm tra · Với pre-retrieval routing, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là top-k lớn hơn có thể làm giảm answer quality.

### Slide 32 Pre-retrieval routing · Evidence & failure lens

> Trích slide Slide 32: Self-RAG,RAG-Fusion & Semantic Caching Self-RAG — LLMtựquyết khinàoretrieve. Fine- tune model output special tokens ( [Retrieve], [IsRel], [IsSup]). Không hoạt động out-of-the- box. 1. Generatemultiplequery variants 2. Retrieve cho mỗivariant→3. RRF merge Semantic Cache— Cache theo semantic similar- ity. Query mới…

**Đọc như kỹ sư:** Self-RAG,RAG-Fusion & Semantic Caching Self-RAG — LLMtựquyết khinàoretrieve.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Fine- tune model output special tokens ( [Retrieve], [IsRel], [IsSup]).
- RRF merge Semantic Cache— Cache theo semantic similar- ity.
- HyDE $$ Vocabmismatch Multi-query $$ Multi-hopQ CRAG $$ Unreliableretrieval Self-RAG $$$ Fine-tunedmodel RAG-Fusion $$$ Maxrecall Sem.Cache $ Repeatedqueries Lưu ý: Đừng dùng tất cả cùng lúc!

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 32 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 34 Pre-retrieval routing · Evidence & failure lens

> Trích slide Slide 34: RAGAS— 4 metrics đánh giá RAGquality Faithfulness Answerclaims được contextsupport không? Target:≥0.85 AnswerRelevancy Q&Acosine similarity Target:≥0.80 ContextPrecision Chunksretrieved có relevantkhông? Target:≥0.75 ContextRecall Đãretrieve đủ infocần thiết chưa? Target:≥0.75 Generation quality Generation quality Retrieval…

**Đọc như kỹ sư:** RAGAS— 4 metrics đánh giá RAGquality Faithfulness Answerclaims được contextsupport không?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Target:≥0.85 AnswerRelevancy Q&Acosine similarity Target:≥0.80 ContextPrecision Chunksretrieved có relevantkhông?
- Target:≥0.75 ContextRecall Đãretrieve đủ infocần thiết chưa?
- Target:≥0.75 Generation quality Generation quality Retrieval quality Retrieval quality Lưu ý:RAGAS phụ thuộc judge model — scoresbrittle khi đổi judge.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 34 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"34273eba-9e9e-58f3-bfe7-469eb7c61dd7","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Dense, sparse & hybrid retrieval","source_file":"track-3-day-18.html"},"checksum":"c9fb5442d9a8fdbda04602ce1dc5205be8bd89bebddfabca5ee949de302ddc83"} -->

## 07 Dense, sparse & hybrid retrieval

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 35 Dense, sparse & hybrid retrieval · Mental model & quyết định

> Trích slide Slide 35: RAGASDiagnostic — Score thấp thì fixở đâu? Contextchứa info đúng nhưng LLM bịathêm →Tightenprompt (“Only use provided context”) →Giảmtemperature, model ít hallucinate hơn Contextkhông chứa info cần thiết →Thựcra là Context Recall problem↓ Chunksđúng tồn tại nhưng không đượcretrieve →Đổichunking (hierarchical) →ThêmBM25 (hybrid…

Re-runRAGAS, so sánh Faithfulness ≥0.85,AnswerRele- vancy ≥0.80 ContextRecall ≥0.75 Luônfailure analysis trước aggregate M.ScTrầnMinh Tú (VinUni). Điểm nối sang production là: citation phải trỏ tới evidence thực sự được dùng. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Các frameworkkhông loại trừ nhau— nhiềuteam dùng kết hợp.
- CostEstimation — 1M documents, bao nhiêutiền?
- Lưu ý: Semantic caching giảm 30– 50%LLMcalls →tiếtkiệmđángkểkhi nhiềuuser hỏi tương tự.

#### Tự kiểm tra · Với dense, sparse & hybrid retrieval, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là citation phải trỏ tới evidence thực sự được dùng.

### Slide 37 Dense, sparse & hybrid retrieval · Evidence & failure lens

> Trích slide Slide 37: EvaluationFrameworks — RAGAS vs TruLensvs DeepEval Dimension RAGAS TruLens DeepEval Focus RAGpipeline eval Eval+ Tracing(OTel) RAG+ Agents + Chatbot Metrics 4core metrics RAGTriad 50+metrics Custom Hạnchế Feedbackfunctions G-Eval,DAG, BaseMetric Tracing Minimal OpenTelemetryspans @observedecorator CI/CD Manualsetup Moderate…

**Đọc như kỹ sư:** EvaluationFrameworks — RAGAS vs TruLensvs DeepEval Dimension RAGAS TruLens DeepEval Focus RAGpipeline eval Eval+ Tracing(OTel) RAG+ Agents + Chatbot Metrics 4core metrics RAGTriad 50+metrics Custom Hạnchế Feedbackfunctions G-Eval,DAG, BaseMetric Tracing Minima

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 37 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 39 Dense, sparse & hybrid retrieval · Evidence & failure lens

> Trích slide Slide 39: CostEstimation — 1M documents, bao nhiêutiền? Embedding 1M chunks × $0.02/1M tokens ≈$10–50 Contextual embeddings: +$50–200 (GPT-4o-mini) Vector DB storage: ∼$20–50/month (QdrantCloud) Embedding: ∼$0.00002 · Reranking: ∼$0.001 LLMgeneration: ∼$0.01–0.05 Total: ∼$0.01–0.06/query NaiveRAG: ∼$1,500/month Production RAG:…

**Đọc như kỹ sư:** CostEstimation — 1M documents, bao nhiêutiền?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Lưu ý: Semantic caching giảm 30– 50%LLMcalls →tiếtkiệmđángkểkhi nhiềuuser hỏi tương tự.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 39 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"264aa4df-0ef9-567e-aec7-e0ad03ecdfd5","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Reranking & context packing","source_file":"track-3-day-18.html"},"checksum":"159df79e1e689b94860c9ad4267fc9688503f4a53a232870189fbe514a41fa1e"} -->

## 08 Reranking & context packing

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 40 Reranking & context packing · Mental model & quyết định

> Trích slide Slide 40: 08 Agentic RAG Khi agent điều khiển RAG pipeline — từ static sang autonomous

08 Agentic RAG Khi agent điều khiển RAG pipeline — từ static sang autonomous. Điểm nối sang production là: đo recall trước khi trách generator. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- RAGEvolution — Từ Naive đến Agentic NaiveRAG staticpipeline AdvancedRAG hybrid+ rerank ModularRAG composable AgenticRAG autonomous Hôm nay: đây Next level Agentic RAG là gì?
- — Agent tự quyết định khi nào retrieve, query nào,bao nhiêu lần, dùng tool nào.
- 4 agentic patterns:Reflection, Plan- ning,Tool Use,Multi-Agent Collab- oration.

#### Tự kiểm tra · Với reranking & context packing, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là đo recall trước khi trách generator.

### Slide 43 Reranking & context packing · Evidence & failure lens

> Trích slide Slide 43: AgenticRAG — Corrective & Adaptive (đãhọc) + mới ✓CRAG=Corrective RAG (slide PreRAG) ✓AdaptiveRetrieval =route by complexity ✓Self-RAG=LLM tự quyết retrieve ✓RAG-Fusion=multi-query + RRF Đâychính làbuildingblocks củaAgentic RAG! Production RAG + Agent orchestration = Agentic RAG. 1. Reflection: Agent tự đánh giá output, retry…

**Đọc như kỹ sư:** AgenticRAG — Corrective & Adaptive (đãhọc) + mới ✓CRAG=Corrective RAG (slide PreRAG) ✓AdaptiveRetrieval =route by complexity ✓Self-RAG=LLM tự quyết retrieve ✓RAG-Fusion=multi-query + RRF Đâychính làbuildingblocks củaAgentic RAG!

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Production RAG + Agent orchestration = Agentic RAG.
- Reflection: Agent tự đánh giá output, retry nếu kém 2.
- Planning: Decomposecomplexquerythànhsub- tasks 3.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 43 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 45 Reranking & context packing · Evidence & failure lens

> Trích slide Slide 45: Tạisao RAG không thể đạt 100%accuracy? Nhiềuretrievalfailures khôngphải vìthiếuevidence trongcorpus. Nguyên nhân thực:alignment gapgiữa query và evidencespace. Queryformulationkhôngmatchcáchevidenceđược biểudiễntrongvectorspace →cosinesimilaritycao nhưngsemanticmismatch. “Query-evidence misalignment is a typed rather than…

**Đọc như kỹ sư:** Nhiềuretrievalfailures khôngphải vìthiếuevidence trongcorpus.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nguyên nhân thực:alignment gapgiữa query và evidencespace.
- Queryformulationkhôngmatchcáchevidenceđược biểudiễntrongvectorspace →cosinesimilaritycao nhưngsemanticmismatch.
- “Query-evidence misalignment is a typed rather than monolithic phenomenon” — có nhiều loại mis- alignmentkhác nhau.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 45 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"05830315-cec4-5d98-afc4-66c82def7f56","locator":{"kind":"html_section","section_id":"c8","order":11,"heading":"09 Grounded generation & citation","source_file":"track-3-day-18.html"},"checksum":"6765f0723138434d61a23a30ce015a1369d774e1036a38313f75b5695bb8f913"} -->

## 09 Grounded generation & citation

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 46 Grounded generation & citation · Mental model & quyết định

> Trích slide Slide 46: FundamentalLimitations — Embedding không capture hết 1. Temporalblindness: Vectorkhôngcóchiềuthời gian →doc2022 và 2024 cùng score. 2. Entity-swap: “capital of France” vs “capital of Germany” →embeddingsgần nhau! 3. Negation insensitivity: “Approved” vs “Not ap- proved” →cosinesimilarity cao. 4. Stale embeddings: Model version…

FundamentalLimitations — Embedding không capture hết 1.. Điểm nối sang production là: index update cần version và khả năng rollback. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Temporalblindness: Vectorkhôngcóchiềuthời gian →doc2022 và 2024 cùng score.
- Entity-swap: “capital of France” vs “capital of Germany” →embeddingsgần nhau!
- Negation insensitivity: “Approved” vs “Not ap- proved” →cosinesimilarity cao.

#### Tự kiểm tra · Với grounded generation & citation, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là index update cần version và khả năng rollback.

### Slide 49 Grounded generation & citation · Evidence & failure lens

> Trích slide Slide 49: LiveDemo — Naive vs Production RAG 1. PipelineA (basic): paragraph chunking +dense-only→chạyRAGAS 2. PipelineB (production): hierarchical chunks +hybrid search + Cohere Rerank →chạyRAGAS 3. PipelineC (bonus): thêm contextual embeddings→sosánh thêm 4. Failureanalysis: zoom bottom-5 questions— dùng Diagnostic Treemap failure…

**Đọc như kỹ sư:** PipelineA (basic): paragraph chunking +dense-only→chạyRAGAS 2.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- PipelineB (production): hierarchical chunks +hybrid search + Cohere Rerank →chạyRAGAS 3.
- PipelineC (bonus): thêm contextual embeddings→sosánh thêm 4.
- Failureanalysis: zoom bottom-5 questions— dùng Diagnostic Treemap failure →fix M.ScTrầnMinh Tú (VinUni)

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 49 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 51 Grounded generation & citation · Evidence & failure lens

> Trích slide Slide 51: Bàitập nhóm — Ghép thành ProductionRAG System (30 phút) Cácbước ghép: 1. Integrate: ghép M1→M5 →M2 →M3 thànhpipeline 2. RunM4: RAGAS eval end-to-end 3. Compare: basic baseline vsproduction pipeline 4. Failureanalysis: bottom-5, map vào ErrorTree 5. Present: 5 phút/nhóm —scores + 1 failurecase study Lưuý: Nếu1modulechưaxong…

**Đọc như kỹ sư:** Bàitập nhóm — Ghép thành ProductionRAG System (30 phút) Cácbước ghép: 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Integrate: ghép M1→M5 →M2 →M3 thànhpipeline 2.
- Compare: basic baseline vsproduction pipeline 4.
- Failureanalysis: bottom-5, map vào ErrorTree 5.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 51 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"532d6eea-24dd-5f12-bc3a-ccb1d886c16e","locator":{"kind":"html_section","section_id":"c9","order":12,"heading":"10 RAG evaluation & operations","source_file":"track-3-day-18.html"},"checksum":"f37712d76ccdc1e12e79c8ba664b4846bc3774de3c32c107d0cb5b3bbc8fe800"} -->

## 10 RAG evaluation & operations

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 52 RAG evaluation & operations · Mental model & quyết định

> Trích slide Slide 52: Hệthống chấm điểm — Cá nhân+ Nhóm Điểmcá nhân (60%): Tiêuchí Điểm Moduleimplementation đúng 15 Testpass criteria đạt 15 Vietnamese-specifichandling 10 Codequality + comments 10 TODOmarkers hoàn thành 10 Subtotalcá nhân 60 Mỗimodule có test_m*.py. Chạy pytest test_m1.py →pass/fail. CIcheck: rufflint+ type hints. Điểmnhóm (40%):…

Hệthống chấm điểm — Cá nhân+ Nhóm Điểmcá nhân (60%): Tiêuchí Điểm Moduleimplementation đúng 15 Testpass criteria đạt 15 Vietnamese-specifichandling 10 Codequality + comments 10 TODOmarkers hoàn thành 10 Subtotalcá nhân 60 Mỗimodule có test_m*.py..

Điểm nối sang production là: context packing là bài toán ngân sách, thứ tự và redundancy. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Implement → pytest tests/ Lưuý: Chạy naive_baseline.pyTRƯỚCđểcóba- sic scores.
- Tiếptheo & Bài tập Ngày 19: GraphRAG & Knowledge Graphs “Khi user hỏi về mối quan hệ giữa 5 entities — flat RAG trả lời sai, GraphRAG trả lời đúng — tại sao?”
- Hoànthành Lab 18: Production RAGpipeline + RAGAS report

#### Tự kiểm tra · Với rag evaluation & operations, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là context packing là bài toán ngân sách, thứ tự và redundancy.

### Slide 55 RAG evaluation & operations · Evidence & failure lens

> Trích slide Slide 55: Tiếptheo & Bài tập Ngày 19: GraphRAG & Knowledge Graphs “Khi user hỏi về mối quan hệ giữa 5 entities — flat RAG trả lời sai, GraphRAG trả lời đúng — tại sao?” ■ Hoànthành Lab 18: Production RAGpipeline + RAGAS report ■ Đọc: Microsoft GraphRAG paper (2024) ■ Optional: Skill-RAG (arxiv 2604.15771),SKILL-RAG (arxiv…

**Đọc như kỹ sư:** Tiếptheo & Bài tập Ngày 19: GraphRAG & Knowledge Graphs “Khi user hỏi về mối quan hệ giữa 5 entities — flat RAG trả lời sai, GraphRAG trả lời đúng — tại sao?”

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Hoànthành Lab 18: Production RAGpipeline + RAGAS report
- Optional: Skill-RAG (arxiv 2604.15771),SKILL-RAG (arxiv 2509.20377),MASS-RAG (arxiv 2604.18509) M.ScTrầnMinh Tú (VinUni)

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 55 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 57 RAG evaluation & operations · Evidence & failure lens

> Trích slide Slide 57: Cảmơn! AICB-P2T3 · Ngày 18 · Production RAG

**Đọc như kỹ sư:** Cảmơn! AICB-P2T3 · Ngày 18 · Production RAG

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 57 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"98c79d11-440c-542f-a5f8-021220123b54","locator":{"kind":"html_section","section_id":"ladder","order":13,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"track-3-day-18.html"},"checksum":"13c8dac00e90efa2b2952ffc8626642541d8d8ec23be60d5f427e4b6a6959534"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của Production RAG bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"5183d894-6456-53cd-987a-004d79c66257","locator":{"kind":"html_section","section_id":"section-014","order":14,"heading":"∑ Phòng mô phỏng quyết định","source_file":"track-3-day-18.html"},"checksum":"6f1ad0cee22eba3e2d6c26270a3dedba80606bbad23fe305d9a37a9204617119"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Chunking economics — overlap giúp recall nhưng phình index

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Số tài liệu:**: min `100`, max `100000`, step `100`, default `10000`

- **Control - Token/tài liệu:**: min `500`, max `20000`, step `100`, default `5000`

- **Control - Chunk size:**: min `100`, max `2000`, step `50`, default `600`

- **Control - Overlap:**: min `0`, max `50`, step `5`, default `15`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Hybrid retrieval — RRF dung hòa hai bảng xếp hạng

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Dense rank:**: min `1`, max `100`, step `1`, default `3`

- **Control - Sparse rank:**: min `1`, max `100`, step `1`, default `18`

- **Control - RRF k:**: min `10`, max `100`, step `5`, default `60`

- **Control - Trọng số dense:**: min `0`, max `100`, step `5`, default `55`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Context budget — top-k tối đa trước khi prompt vỡ

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Top-k:**: min `1`, max `40`, step `1`, default `12`

- **Control - Token/chunk:**: min `100`, max `2000`, step `50`, default `600`

- **Control - Prompt + output:**: min `500`, max `16000`, step `500`, default `5000`

- **Control - Context window:**: min `8`, max `256`, step `8`, default `32`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"27f9cf53-dc8f-5749-94c8-3d12518f6b97","locator":{"kind":"html_section","section_id":"misc","order":15,"heading":"✕ Hiểu lầm phổ biến","source_file":"track-3-day-18.html"},"checksum":"a4c6c37ea1b1028a87aa913dfd0eb1b6f1729dd682c0be8d2ea45a5812f53729"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai production rag mental model là phần còn lại tự động an toàn và ổn định.

Sửa lại Offline và online pipeline có failure mode khác nhau.

Vì sao quan trọng · slide 1 · 3 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai offline ingestion pipeline là phần còn lại tự động an toàn và ổn định.

Sửa lại Chunk theo đơn vị nghĩa trước khi theo số token.

Vì sao quan trọng · slide 6 · 9 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai parsing & enrichment là phần còn lại tự động an toàn và ổn định.

Sửa lại Metadata là tín hiệu retrieval, không phải trang trí.

Vì sao quan trọng · slide 12 · 15 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai chunking strategy là phần còn lại tự động an toàn và ổn định.

Sửa lại Hybrid search giảm blind spot giữa semantic và exact term.

Vì sao quan trọng · slide 18 · 20 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai embedding & indexing là phần còn lại tự động an toàn và ổn định.

Sửa lại Reranker dùng sau candidate retrieval, không thay retriever.

Vì sao quan trọng · slide 23 · 26 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai pre-retrieval routing là phần còn lại tự động an toàn và ổn định.

Sửa lại Top-k lớn hơn có thể làm giảm answer quality.

Vì sao quan trọng · slide 29 · 32 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"0c369790-db3c-5eda-9926-74f93dc40b41","locator":{"kind":"html_section","section_id":"apply","order":16,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"track-3-day-18.html"},"checksum":"2733c62d34c2b2f6dce8200589d6e53fb97d8a0494bac12b45a56a9b2686261e"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI tra chính sách khách sạn đa ngôn ngữ; câu trả lời đúng phụ thuộc cả chunking, hybrid search và citation.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Production RAG mental model | Offline và online pipeline có failure mode khác nhau. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 3 |
| Offline ingestion pipeline | Chunk theo đơn vị nghĩa trước khi theo số token. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 6 · 9 |
| Parsing & enrichment | Metadata là tín hiệu retrieval, không phải trang trí. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 12 · 15 |
| Chunking strategy | Hybrid search giảm blind spot giữa semantic và exact term. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 18 · 20 |
| Embedding & indexing | Reranker dùng sau candidate retrieval, không thay retriever. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 23 · 26 |
| Pre-retrieval routing | Top-k lớn hơn có thể làm giảm answer quality. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 29 · 32 |
| Dense, sparse & hybrid retrieval | Citation phải trỏ tới evidence thực sự được dùng. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 35 · 37 |
| Reranking & context packing | Đo recall trước khi trách generator. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 40 · 43 |

---

<!-- chiron-source-span: {"source_span_id":"676105da-2baa-526c-a8a4-bb4fd39ab610","locator":{"kind":"html_section","section_id":"numbers","order":17,"heading":"# Con số cần kiểm chứng","source_file":"track-3-day-18.html"},"checksum":"ab87957939c7835dd0e52e50012d25043d5fdc60d0dd673db73ea37b3cd9f088"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 60% | HÃYSUY NGHĨ... “Tại sao RAG pipeline demo chạy tốt nhưng production accuracy chỉ đạt 60% — ingestion hay retrieval đang giết bạn?” Giữcâu hỏi này trong đầu khihọc bài hôm nay | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 2 |
| 65% | e in, garbageout.” Query → RAG → Output. Chạy mỗi query. Production accuracy chỉ 55– 65%—tại sao? M.ScTrầnMinh Tú (VinUni) | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 5 |
| 85% | Bằngchứng: Gap giữaNaive và Production RAG 60% Naive RAG Accuracy 85%+ Production RAG Accuracy +25% Improvement khi optimize Metric NaiveRAG Production RAG Nguyên nhâncải thiện Faithfulness ∼0.70 ≥0.85 Betterprompt + re | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 25% | Gap giữaNaive và Production RAG 60% Naive RAG Accuracy 85%+ Production RAG Accuracy +25% Improvement khi optimize Metric NaiveRAG Production RAG Nguyên nhâncải thiện Faithfulness ∼0.70 ≥0.85 Betterprompt + reranking ContextRecall ∼0.55 ≥0 | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 1M | case Model Dims TiếngViệt Max Tokens Cost text-embedding-3-small 1536 OK 8191 $0.02/1M text-embedding-3-large 3072 Tốt 8191 $0.13/1M Cohereembed-v3 1024 Tốt 512 $0.10/1M bge-m3(open-source) 1024 Rấttốt 8192 Free multilingual-e5-large 10 | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 14 |
| 128K | ừ đầu! Benchmark trên MTEB multilingual leaderboard. Note: Cohere Embed v4 đã hỗ trợ 128K tokens — cânnhắc nếu cần long-context. M.ScTrầnMinh Tú (VinUni) | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 14 |
| 12 ngày | ContextualEmbeddings — Anthropic’sContextual Retrieval Chunkgốc “Nhânviên được nghỉ 12 ngày/năm.” LLMprepend context ClaudeHaiku / GPT-4o-mini Contextualchunk “TríchChương 3 — Chính sáchnghỉ phép Sổtay VinUni2024. NV được nghỉ 12 ngày/năm.” | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 15 |
| 67% | ngắn giải thích chunk nằm ở đâu trong document. Retrievalfailure giảm49%(alone) Giảm 67% khi kết hợp Contextual BM25+ Reranking Lưuý: Trade-off: +1LLMcall/chunkkhiindexing (one-time). Dùng model rẻ(Haiku, GPT-4o-mini). M.ScTrầnMinh Tú (Vi | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 15 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"f3532f3f-d7f4-52ba-9ee6-bfd4404858c2","locator":{"kind":"html_section","section_id":"cheat","order":18,"heading":"▣ Cheat sheet ôn thi","source_file":"track-3-day-18.html"},"checksum":"1e793c8b93de5fcb802e49f968c4c00741318c206d6d99d2d64ff4bd35fa9b47"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp production rag mental model | offline và online pipeline có failure mode khác nhau | 1 · 3 |
| Khi gặp offline ingestion pipeline | chunk theo đơn vị nghĩa trước khi theo số token | 6 · 9 |
| Khi gặp parsing & enrichment | metadata là tín hiệu retrieval, không phải trang trí | 12 · 15 |
| Khi gặp chunking strategy | hybrid search giảm blind spot giữa semantic và exact term | 18 · 20 |
| Khi gặp embedding & indexing | reranker dùng sau candidate retrieval, không thay retriever | 23 · 26 |
| Khi gặp pre-retrieval routing | top-k lớn hơn có thể làm giảm answer quality | 29 · 32 |
| Khi gặp dense, sparse & hybrid retrieval | citation phải trỏ tới evidence thực sự được dùng | 35 · 37 |
| Khi gặp reranking & context packing | đo recall trước khi trách generator | 40 · 43 |
| Khi gặp grounded generation & citation | index update cần version và khả năng rollback | 46 · 49 |
| Khi gặp rag evaluation & operations | context packing là bài toán ngân sách, thứ tự và redundancy | 52 · 55 |

---

<!-- chiron-source-span: {"source_span_id":"124692c9-922f-5b06-8e9b-b6f4bbcc64ee","locator":{"kind":"html_section","section_id":"gloss","order":19,"heading":"☰ Từ điển thuật ngữ","source_file":"track-3-day-18.html"},"checksum":"f1888926c8c6fd649a87ae79fa4f8a06099ec3b8165c234acc35fb7b988dbc88"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"8b5e1c20-81a4-5d14-a705-e5a0cc71ead7","locator":{"kind":"html_section","section_id":"bloom","order":20,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-18.html"},"checksum":"6cb66d582f5a3578b48b76548e8c53e2a61a48463ba9970721231137ea658eaf"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 3 · 5 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 6 · 9 · 11 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 12 · 15 · 17 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 18 · 20 · 22 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 23 · 26 · 28 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 29 · 32 · 34 |
