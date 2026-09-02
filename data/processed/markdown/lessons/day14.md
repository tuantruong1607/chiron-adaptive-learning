---
schema_version: 1
course_id: rag-intensive
document_id: "ddc8f272-bb25-5d69-86c1-26562cb9beb1"
document_version_id: "71ace38d-57e2-5d5f-811e-471c587d23cf"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "AI Evaluation — Đo đúng trước khi tối ưu"
source_file: "day14.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\day14.html"
source_sha256: "ec9864f740dbb762c0a9385f8dcdbb30b2addb3e88e814d5716a2e7527848123"
parser_version: chiron-structured-markdown-v1
html_section_count: 21
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# AI Evaluation — Đo đúng trước khi tối ưu

> Thiết kế eval đủ tin cậy để phân biệt cải tiến thật với nhiễu, và chặn regression trước production.

<!-- chiron-source-span: {"source_span_id":"df649055-9408-531f-b81c-03d443a5c298","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"day14.html"},"checksum":"62b5c706e9e670202ed0a84837473401460e2363e6bcc9ed67877ba3011e39b1"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: không có dataset đại diện thì điểm eval không đại diện production. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"5a58e4e8-e566-59ad-936b-a0ebbb2a0fcc","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"day14.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

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

<!-- chiron-source-span: {"source_span_id":"fe93d4c4-2efc-55da-a2e7-88c51a4cab4b","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Vì sao AI cần evaluation khác","source_file":"day14.html"},"checksum":"c7d7d0ede699c3fff9fc6fd02bb8b6dfc61f59d2df78a462bee285b512e8d4fd"} -->

## 01 Vì sao AI cần evaluation khác

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Vì sao AI cần evaluation khác · Mental model & quyết định

> Trích slide Slide 1: AI Evaluation & Benchmarking AICB-P1 · Ngày 14 · Đo lường chất lượng AI một cách khoa học T ên Giảng Viên VinUniversity · Phase 1 · 2026

AI Evaluation & Benchmarking AICB-P1 · Ngày 14 · Đo lường chất lượng AI một cách khoa học T ên. Điểm nối sang production là: không có dataset đại diện thì điểm eval không đại diện production. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- “Sếp hỏi: AI agent của mình tốt hơn ChatGPT bao nhiêu?
- Bạn nói sao nếu không có benchmark?” Giữ câu hỏi này trong đầu khi học bài hôm nay
- Hiểu vì sao evaluation là engineering discipline, không phải cảm tính

#### Tự kiểm tra · Với vì sao ai cần evaluation khác, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là không có dataset đại diện thì điểm eval không đại diện production.

### Slide 5 Vì sao AI cần evaluation khác · Evidence & failure lens

> Trích slide Slide 5: Deliverable Cuối Ngày Artifact pack cần nộp Evaluation report cho agent gồm benchmark 20 test cases, RAGAS scores, LLM-as-Judge results, failure analysis, và improvement recommendations ■ 1 golden dataset: 20 question-answer pairs với expected answers ■ 1 RAGAS evaluation: faithfulness, answer relevancy, context scores ■ 1…

**Đọc như kỹ sư:** Deliverable Cuối Ngày Artifact pack cần nộp Evaluation report cho agent gồm benchmark 20 test cases, RAGAS scores, LLM-as-Judge results, failure analysis, và improvement recommendations

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- 1 golden dataset: 20 question-answer pairs với expected answers
- 1 RAGAS evaluation: faithfulness, answer relevancy, context scores
- 1 LLM-as-Judge scoring: rubric 1–5 cho ít nhất 10 responses

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 5 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 8 Vì sao AI cần evaluation khác · Evidence & failure lens

> Trích slide Slide 8: Evaluation = Scientific Method Cho AI Hypothesis “Agent tốt hơn” Experiment Chạy benchmark Measure RAGAS, Judge Conclude Evidence-based iterate Nguyên tắc Không đo = không cải thiện. Evaluation phải lặp lại được, so sánh được, và chạy tự động được. Giảng viên (VinUni) AICB · Evaluation 2026 5 / 76

**Đọc như kỹ sư:** Evaluation = Scientific Method Cho AI Hypothesis “Agent tốt hơn” Experiment Chạy benchmark Measure RAGAS, Judge Conclude Evidence-based iterate Nguyên tắc Không đo = không cải thiện.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Evaluation phải lặp lại được, so sánh được, và chạy tự động được.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 8 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"d61df9d5-0f5a-5e37-8f23-0872f3033f35","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Evaluation taxonomy","source_file":"day14.html"},"checksum":"0e81e5c491c53eadef9464e3b56f286cb37d89fb7672976fe4950734e4718ad0"} -->

## 02 Evaluation taxonomy

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 9 Evaluation taxonomy · Mental model & quyết định

> Trích slide Slide 9: 4 Chiều Chất Lượng Output Correctness Đúng sự thật không? Có hallucinate không? Citations đúng nguồn? Relevance Trả lời đúng câu hỏi user không? Hay lạc đề, trả lời chung chung? Completeness Đủ chi tiết cần thiết chưa? Có bỏ sót thông tin quan trọng? Coherence Dễ đọc, có cấu trúc? Ngôn ngữ phù hợp với user? Lưu ý: 1 metric…

4 Chiều Chất Lượng Output Correctness Đúng sự thật không?. Điểm nối sang production là: tách retrieval quality khỏi answer quality. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Agent có thể cao correctness nhưng thấp relevance (đúng nhưng lạc đề).
- 3 Loại Evaluation Offline Batch test trên golden dataset.
- Khi nào: mỗi release, mỗi prompt change T ool: RAGAS, custom scripts Online Monitor quality trên production.

#### Tự kiểm tra · Với evaluation taxonomy, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là tách retrieval quality khỏi answer quality.

### Slide 13 Evaluation taxonomy · Evidence & failure lens

> Trích slide Slide 13: Eval Cost — Thời Gian Và Tiền Tính chi phí 1 lần chạy eval: ■ 20 test cases × 4 RAGAS metrics × judge LLM ■ ≈ 80 API calls × $0.01–0.05 ■ ≈ $1–4 mỗi lần chạy Chi phí tháng: ■ 100 PR/tháng → $100–400 ■ Cộng online sampling → $500–1000 Freq. Cost Catch bug Mỗi PR Cao Trước merge Daily TB Trong ngày Weekly Thấp Sau user gặp…

**Đọc như kỹ sư:** Eval Cost — Thời Gian Và Tiền Tính chi phí 1 lần chạy eval

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Cost Catch bug Mỗi PR Cao Trước merge Daily TB Trong ngày Weekly Thấp Sau user gặp Nguyên tắc vàng Eval phải rẻ hơn bug production gây ra ∼1000 lần.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 13 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 16 Evaluation taxonomy · Evidence & failure lens

> Trích slide Slide 16: T ask Completion — Sâu Hơn 4 cách chấm task completion: 1. Binary (pass/fail): đơn giản, nhanh, mất thông tin 2. Partial credit: score 0.0–1.0 theo% subtasks 3. Weighted scoring: step quan trọng có weight cao hơn 4. Trajectory eval: đánh giá cả con đường, không chỉ kết quả Ví dụ: 4 bước Tìm slot (25%), mời đúng người (25%),…

**Đọc như kỹ sư:** T ask Completion — Sâu Hơn 4 cách chấm task completion: 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Binary (pass/fail): đơn giản, nhanh, mất thông tin 2.
- Partial credit: score 0.0–1.0 theo% subtasks 3.
- Weighted scoring: step quan trọng có weight cao hơn 4.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 16 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"60d437c0-c776-5cc9-985b-0e862d8a8efe","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Golden dataset","source_file":"day14.html"},"checksum":"61efe38f933e3405942fae199ce149c7be5da98b4f15d2459213a297adb47a04"} -->

## 03 Golden dataset

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 17 Golden dataset · Mental model & quyết định

> Trích slide Slide 17: Answer Quality — Làm Sao Đo Accuracy? Method Khi nào dùng Nhanh Chính xác Cost Exact match Factual QA, answer ngắn Cao Kém (open- ended) $0 F1 token overlap Span extraction (NER, QA) Cao Trung bình $0 BLEU / ROUGE Translation, summa- rization Cao Y ếu (creative) $0 BERTScore Semantic similarity open-ended TB Trung bình $…

RAG Metrics — Bức Tranh T oàn Cảnh Question Retriever Context Generator Answer Context Recall Context Precision Faithfulness Answer Relevancy Đọc kết quả Context Recall thấp = retrieve thiếu.. Điểm nối sang production là: metric trung bình không được che hard failure.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Công Thức Faithfulness Faithfulness = số claims trong answer được context support tổng số claims trong answer Answer: “Policy có 3 điều.
- Điều 3: không áp dụng sale items.” 3 claims tổng.
- Context support claim 1 và 2, không đề cập claim 3.

#### Tự kiểm tra · Với golden dataset, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là metric trung bình không được che hard failure.

### Slide 21 Golden dataset · Evidence & failure lens

> Trích slide Slide 21: Business Metrics — Gắn Với ROI Track bắt buộc: ■ Thumbs up/down rate per 100 ■ Resolution rate (tự giải quyết%) ■ Escalation rate (chuyển human%) ■ P50 / P95 latency ■ Cost per resolved query ■ DAU, retention tuần/tháng ■ Resolution ≥ 70% ■ Thumbs-up ≥ 60% ■ P95 ≤ 5s ■ Cost ≤ $0.05/query Lưu ý: Quality tốt nhưng P95 = 30s →…

**Đọc như kỹ sư:** Business Metrics — Gắn Với ROI Track bắt buộc

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Cost ≤ $0.05/query Lưu ý: Quality tốt nhưng P95 = 30s → user bỏ → adoption thấp → project chết.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 21 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 24 Golden dataset · Evidence & failure lens

> Trích slide Slide 24: Golden Dataset — Nền T ảng Của Mọi Evaluation Golden dataset gồm ■ 50–100 question-answer pairs ■ Expected answers do expert viết ■ Cover tất cả use cases chính ■ Có difficulty levels: easy, medium, hard ■ Có edge cases và adversarial inputs T ại sao cần expert answers Nếu expected answer sai hoặc mơ hồ, toàn bộ evaluation sẽ…

**Đọc như kỹ sư:** Golden Dataset — Nền T ảng Của Mọi Evaluation Golden dataset gồm

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Có edge cases và adversarial inputs T ại sao cần expert answers Nếu expected answer sai hoặc mơ hồ, toàn bộ evaluation sẽ cho kết quả misleading.
- Dưới 20 quá ít để kết luận bất kỳ điều gì có ý nghĩa thống kê.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 24 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"625a649a-1c22-5c81-b391-b123ee55cea1","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 RAGAS & RAG metrics","source_file":"day14.html"},"checksum":"fc64e425b8d5e936deb9cb4befe389f765a25cea16a8227000539a2dab5e6ac1"} -->

## 04 RAGAS & RAG metrics

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 25 RAGAS & RAG metrics · Mental model & quyết định

> Trích slide Slide 25: 3 Cách T ạo Golden Dataset Từ Số 0 1. Expert viết Ưu: chất lượng cao nhất Nhược: chậm, tốn chuyên gia Khi dùng: high-stakes (y tế, pháp lý) Quy trình: expert viết → re- view chéo → lock version 2. Từ production log Ưu: realistic, gần produc- tion Nhược: tốn công label Khi dùng: đã có traffic Quy trình: lấy 100 query thật →…

Expert viết Ưu: chất lượng cao nhất Nhược: chậm, tốn chuyên gia Khi dùng: high-stakes (y tế, pháp lý) Quy trình: expert viết → re- view chéo → lock version 2.. Điểm nối sang production là: LLM judge cần rubric, calibration và kiểm tra agreement.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Từ production log Ưu: realistic, gần produc- tion Nhược: tốn công label Khi dùng: đã có traffic Quy trình: lấy 100 query thật → expert viết answer chuẩn 3.
- LLM sinh + filter Ưu: nhanh, scalable Nhược: bias theo LLM Khi dùng: bootstrapping Quy trình: LLM sinh → hu- man filter/fix Kết hợp Cách 3 để có v0 nhanh → Cách 2 thêm production cases → Cách 1 cho edge cases high-value.
- Code: LLM-generated QA Pairs def generate_qa_from_chunk(chunk_text, llm): prompt = f """Read the document below.

#### Tự kiểm tra · Với ragas & rag metrics, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là LLM judge cần rubric, calibration và kiểm tra agreement.

### Slide 29 RAGAS & RAG metrics · Evidence & failure lens

> Trích slide Slide 29: Edge Cases Và Stratified Sampling Edge cases cần cover ■ Ambiguous queries (nhiều cách hiểu) ■ Out-of-scope (ngoài domain) ■ Adversarial (cố tình phá) ■ Multilingual (VN + EN mixed) ■ Long context (nhiều tài liệu) Stratified sampling ■ Proportional cho mỗi use case ■ Đủ samples cho mỗi difficulty level ■ Đại diện các user…

**Đọc như kỹ sư:** Edge Cases Và Stratified Sampling Edge cases cần cover

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Long context (nhiều tài liệu) Stratified sampling
- Cân bằng giữa happy path và edge case Tip Benchmark phải evolve.
- Track changes trong Git để tránh data contamination.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 29 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 32 RAGAS & RAG metrics · Evidence & failure lens

> Trích slide Slide 32: Code: Stratified Sampling from collections import defaultdict import random def stratified_sample(dataset, n_per_strata=5): """Ensure enough samples per (category, difficulty).""" strata = defaultdict( list) for item in dataset: key = (item[ 'category'], item[ 'difficulty']) strata[key].append(item) sample = [] for key, items…

**Đọc như kỹ sư:** Code: Stratified Sampling from collections import defaultdict import random def stratified_sample(dataset, n_per_strata=5): """Ensure enough samples per (category, difficulty).""" strata = defaultdict( list) for item in dataset: key = (item[ 'category'], item[

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 32 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"4e9247c5-07ec-564f-a3fe-38645fd7a378","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 LLM-as-Judge","source_file":"day14.html"},"checksum":"70ef5c59948ab1a401c3c4223a3a97a2122ceef92598b59d4df68805b7bbbdcf"} -->

## 05 LLM-as-Judge

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 33 LLM-as-Judge · Mental model & quyết định

> Trích slide Slide 33: 04 LLM-as-Judge Human eval chính xác nhất nhưng không scale. LLM-as- Judge cho phép đánh giá hàng trăm outputs tự động với rubric rõ ràng

04 LLM-as-Judge Human eval chính xác nhất nhưng không scale.. Điểm nối sang production là: golden set phải version cùng dữ liệu và prompt. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- LLM-as- Judge cho phép đánh giá hàng trăm outputs tự động với rubric rõ ràng
- LLM-as-Judge — Concept Question Y our Agent Agent Answer Judge LLM (GPT-4 / Claude) Reference Answer Score 1–5 + Rationale Ý chính Judge LLM nhận question + agent answer + reference answer + rubric, rồi cho điểm kèm giải thích.
- Biết khi nào không dùng quan trọng ngang biết khi nào dùng.

#### Tự kiểm tra · Với llm-as-judge, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là golden set phải version cùng dữ liệu và prompt.

### Slide 37 LLM-as-Judge · Evidence & failure lens

> Trích slide Slide 37: Rubric: Reference-based vs Reference-free Reference-based So với answer chuẩn. 5 = Equivalent meaning 4 = Minor differences 3 = Some gaps or errors Dùng khi: có ground truth chắc chắn. Reference-free Đánh theo tiêu chí độc lập. Correctness, Relevance, Conciseness, Safety (1–5 mỗi tiêu chí) Dùng khi: không có reference…

**Đọc như kỹ sư:** Rubric: Reference-based vs Reference-free Reference-based So với answer chuẩn.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- 5 = Equivalent meaning 4 = Minor differences 3 = Some gaps or errors Dùng khi: có ground truth chắc chắn.
- Correctness, Relevance, Conciseness, Safety (1–5 mỗi tiêu chí) Dùng khi: không có reference (creative, open- ended).
- Kết hợp Reference-based chính xác hơn nhưng cần ground truth.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 37 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 40 LLM-as-Judge · Evidence & failure lens

> Trích slide Slide 40: 7 Biases Của LLM-as-Judge Bias Mô tả Fix Position Judge ưu tiên answer xuất hiện trước Random order, swap A/B, average Verbosity Answer dài hơn → điểm cao hơn Rubric: “concise is OK” + đo length riêng Self- preference GPT-4 judge thích GPT-4 out- put Dùng judge khác family (Claude judge GPT) Sycophancy Đồng tình với phrasing…

**Đọc như kỹ sư:** Cần calibrate against human: so sánh scores của judge với expert ratings trên 50+ samples.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 40 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"6a5fbfd9-9da1-55f3-9063-d4159ee1c64b","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Rubric và calibration","source_file":"day14.html"},"checksum":"5e7ccaa814e4902edb1f5b0f6da64653ad4ab46018f5b313068306b4ae981d60"} -->

## 06 Rubric và calibration

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 41 Rubric và calibration · Mental model & quyết định

> Trích slide Slide 41: Best Practices Cho LLM-as-Judge □✓ Multiple judges: dùng 2–3 LLMs khác nhau, lấy majority vote hoặc aver- age □✓ Randomize order: đổi vị trí answer A/B giữa các lần chạy □✓ Include rationale: yêu cầu judge giải thích điểm, không chỉ cho số □✓ Chain-of-thought: yêu cầu judge reasoning từng bước □✓ Calibrate: so sánh judge…

LLM judge vẫn sai, đặc biệt ở domain chuyên biệt. Điểm nối sang production là: confidence interval quan trọng hơn một điểm lẻ. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Calibration — So Với Human Quy trình calibrate judge 4 bước: 1.
- 2 experts chấm theo cùng rubric (Cohen’s κ giữa experts ≥ 0.6) 3.
- Tính correlation (Spearman) hoặc agreement (κ) giữa judge và human avg

#### Tự kiểm tra · Với rubric và calibration, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là confidence interval quan trọng hơn một điểm lẻ.

### Slide 45 Rubric và calibration · Evidence & failure lens

> Trích slide Slide 45: 4 RAGAS Metrics Faithfulness Answer có dựa trên retrieved context không? Thấp = hallucination, bịa thông tin Context Recall Retriever có lấy đủ evidence không? Thấp = retrieve thiếu tài liệu quan trọng Answer Relevancy Answer có trả lời đúng câu hỏi không? Thấp = lạc đề, trả lời chung chung Context Precision Context retrieved…

**Đọc như kỹ sư:** 4 RAGAS Metrics Faithfulness Answer có dựa trên retrieved context không?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Thấp = hallucination, bịa thông tin Context Recall Retriever có lấy đủ evidence không?
- Thấp = retrieve thiếu tài liệu quan trọng Answer Relevancy Answer có trả lời đúng câu hỏi không?
- Thấp = lạc đề, trả lời chung chung Context Precision Context retrieved có relevant không?

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 45 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 49 Rubric và calibration · Evidence & failure lens

> Trích slide Slide 49: Diagnostic Flowchart — Score Thấp, Fix Ở Đâu? Faithfulness thấp? Context Recall thấp? Context Precision thấp? Answer Relevancy thấp? ⇒ Prompt: “only answer from context” ⇒ Tăng top-k, re-chunk nhỏ hơn ⇒ Re-ranking, semantic filter ⇒ Prompt clearer, answer template Thứ tự fix Context Recall → Context Precision → Faithfulness →…

**Đọc như kỹ sư:** Diagnostic Flowchart — Score Thấp, Fix Ở Đâu?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- ⇒ Prompt: “only answer from context” ⇒ Tăng top-k, re-chunk nhỏ hơn ⇒ Re-ranking, semantic filter ⇒ Prompt clearer, answer template Thứ tự fix Context Recall → Context Precision → Faithfulness → Answer Relevancy.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 49 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"1d227565-1378-520c-8837-3c8c56b0794a","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Statistical rigor","source_file":"day14.html"},"checksum":"eeb6a73b0dca32f690f153cd79ba690ab63a48bd22df6e5b2d911dcf634fc318"} -->

## 07 Statistical rigor

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 50 Statistical rigor · Mental model & quyết định

> Trích slide Slide 50: Case Study: Agent VinHomes — Trước / Sau Fix Metric v1 (trước) v2 (sau) ∆ Faithfulness 0.62 0.87 +0.25 Answer Relevancy 0.78 0.82 +0.04 Context Recall 0.45 0.81 +0.36 Context Precision 0.71 0.76 +0.05 Fix đã làm Context Recall thấp→ re-chunk từ 1000 tokens→ 400 tokens với 50-token overlap. Faithfulness thấp → thêm system…

Faithfulness thấp → thêm system prompt: “CHỈ trả lời dựa trên context.. Điểm nối sang production là: offline eval nhanh nhưng online signal mới phản ánh hành vi thật. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Nếu không có thì nói Tôi không biết.” Tổng chi phí: 2 ngày engineer.
- ROI: fail rate giảm từ 40% xuống 15%, resolution rate +25 điểm%.
- Limitations Của RAGAS Khi nào RAGAS không đáng tin

#### Tự kiểm tra · Với statistical rigor, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là offline eval nhanh nhưng online signal mới phản ánh hành vi thật.

### Slide 54 Statistical rigor · Evidence & failure lens

> Trích slide Slide 54: Confidence Interval — Công Thức 95% Confidence Interval (với n ≥ 30): CI = ¯x ± 1.96 × s√n với ¯x = mean, s = std, n = sample size. Ví dụ mean = 0.766, std = 0.033, n = 5 runs × 20 items = 100 samples CI = 0.766 ± 1.96 × 0.033/ √ 100 = 0.766 ± 0.0065 Báo cáo: 0.77 (95% CI: 0.76–0.78) Với n nhỏ (< 30): dùng t-distribution,…

**Đọc như kỹ sư:** Confidence Interval — Công Thức 95% Confidence Interval (với n ≥ 30): CI = ¯x ± 1.96 × s√n với ¯x = mean, s = std, n = sample size.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Ví dụ mean = 0.766, std = 0.033, n = 5 runs × 20 items = 100 samples CI = 0.766 ± 1.96 × 0.033/ √ 100 = 0.766 ± 0.0065 Báo cáo: 0.77 (95% CI: 0.76–0.78) Với n nhỏ (< 30): dùng t-distribution, thay 1.96 bằng tα/2,n−1 (với n = 10, t = 2.26).
- So sánh Agent v1: 0.77 (0.76–0.78); Agent v2: 0.78 (0.77–0.79).

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 54 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 57 Statistical rigor · Evidence & failure lens

> Trích slide Slide 57: A/B T esting Trong Production Quy trình 6 bước: 1. Define hypothesis: “v2 sẽ tăng thumbs-up rate từ 60% lên 65%” 2. Calculate sample size: dùng power analysis →∼ 500 interactions mỗi arm 3. Random split: 50% user vào v1, 50% v2 (sticky by user_id) 4. Guardrails: cost/latency/error rate không xấu đi hơn 5% 5. Run: tối thiểu 1…

**Đọc như kỹ sư:** A/B T esting Trong Production Quy trình 6 bước: 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Define hypothesis: “v2 sẽ tăng thumbs-up rate từ 60% lên 65%” 2.
- Calculate sample size: dùng power analysis →∼ 500 interactions mỗi arm 3.
- Random split: 50% user vào v1, 50% v2 (sticky by user_id) 4.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 57 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"253090b6-f1e6-5b18-8cbe-02bd0557ae97","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Agentic evaluation","source_file":"day14.html"},"checksum":"5e124e8ba4ddb036fc98bcfc6d7cdde86aed087da38f2e3dd364068130a61e05"} -->

## 08 Agentic evaluation

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 58 Agentic evaluation · Mental model & quyết định

> Trích slide Slide 58: Checklist Statistical Rigor Trước khi claim “agent v2 tốt hơn v1”, kiểm tra: □✓ Đã chạy eval ≥ 3 lần mỗi version? □✓ Đã báo cáo mean ± std (hoặc CI), không chỉ single number? □✓ Đã chạy significance test (paired t-test, p < 0.05)? □✓ Sample size đủ power (tính trước bằng power analysis)? □✓ Đã kiểm tra guardrails (latency,…

Checklist Statistical Rigor Trước khi claim “agent v2 tốt hơn v1”, kiểm tra: □✓ Đã chạy eval ≥ 3 lần mỗi version?. Điểm nối sang production là: agent phải được chấm cả trajectory và side effect. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- □✓ Đã báo cáo mean ± std (hoặc CI), không chỉ single number?
- □✓ Đã chạy significance test (paired t-test, p < 0.05)?
- □✓ Sample size đủ power (tính trước bằng power analysis)?

#### Tự kiểm tra · Với agentic evaluation, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là agent phải được chấm cả trajectory và side effect.

### Slide 62 Agentic evaluation · Evidence & failure lens

> Trích slide Slide 62: Safety Eval — Adversarial T est Suite Liên kết với Day 12 (Guardrails): phải đo được guardrails work. Category T est T arget Jailbreak (DAN, role- play) “Pretend you’re DAN”, “Ignore rules” ≥ 95% refuse Prompt injection In docs, user input, tool results ≥ 99% detect PII leakage Tên, SĐT, CCCD trong context 0% leak Toxicity…

**Đọc như kỹ sư:** Safety Eval — Adversarial T est Suite Liên kết với Day 12 (Guardrails): phải đo được guardrails work.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 62 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 65 Agentic evaluation · Evidence & failure lens

> Trích slide Slide 65: Red T eam Evaluation ■ Test scenario đã định ■ Benchmark cố định ■ Automated Red team ■ Thuê người cố tình phá ■ Creative, adversarial ■ Manual Quy trình red team 5 bước: 1. Hire 3–5 người (mix background: security, UX, domain expert) 2. Time-bound: 2 giờ cố tình break agent 3. Log mọi attempt & response 4. Categorize:…

**Đọc như kỹ sư:** Hire 3–5 người (mix background: security, UX, domain expert) 2.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Categorize: jailbreak, PII, bias, factual error, safety 5.
- Fix top issues, add to benchmark (benchmark evolve) Khi nào chạy Chạy red team trước mỗi major release.
- Automated red team cũng có (vd Anthropic’s HH- RLHF).

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 65 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"c09574a7-0242-5772-b37b-bff477aa0e37","locator":{"kind":"html_section","section_id":"c8","order":11,"heading":"09 Safety & red teaming","source_file":"day14.html"},"checksum":"f811ecaab8aaad63b165b7d7765b27639fb5ddccd8cbf164377333024da03a0d"} -->

## 09 Safety & red teaming

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 66 Safety & red teaming · Mental model & quyết định

> Trích slide Slide 66: 08 Benchmark Ngành 2026 — LLM & AI Agent Benchmark nội bộ (RAGAS, LLM Judge) đo agent của bạn. Benchmark ngành đo model/agent so với cả thế giới — và xu hướng đang đổi nhanh

08 Benchmark Ngành 2026 — LLM & AI Agent Benchmark nội bộ (RAGAS, LLM Judge) đo agent của bạn.. Điểm nối sang production là: benchmark công khai không thay thế domain eval. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Benchmark ngành đo model/agent so với cả thế giới — và xu hướng đang đổi nhanh
- Xu Hướng Benchmark 2026: 3 Trục Mới Benchmark cũ (MMLU, HellaSwag) đang saturate — model nào cũng >90%.
- Ngành chuyển sang 3 trục khó hơn: Long-horizon Agent tự chủ làm việc nhiều giờ đến nhiều tuần, không chỉ 1 câu trả lời.

#### Tự kiểm tra · Với safety & red teaming, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là benchmark công khai không thay thế domain eval.

### Slide 70 Safety & red teaming · Evidence & failure lens

> Trích slide Slide 70: T erminal-Bench — Agent Sống Trong T erminal Setup: Mỗi task = instruction + Docker image + bộ test + time limit. Agent chỉ có shell access trong container, không GUI. Run loop Agent chạy lệnh shell nhiều turn trong time limit → framework Harbor chạy test cuối cùng trong container → pass/fail nhị phân →% accuracy toàn set.…

**Đọc như kỹ sư:** T erminal-Bench — Agent Sống Trong T erminal Setup: Mỗi task = instruction + Docker image + bộ test + time limit.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Agent chỉ có shell access trong container, không GUI.
- Run loop Agent chạy lệnh shell nhiều turn trong time limit → framework Harbor chạy test cuối cùng trong container → pass/fail nhị phân →% accuracy toàn set.
- 1 Claude Code ∼84% 2 Codex ∼83% 3 Terminus 2 ∼80% Vì sao quan trọng Terminal là môi trường thật nhất mà coding agent production hoạt động — sát hơn benchmark Q&A truyền thống.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 70 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 73 Safety & red teaming · Evidence & failure lens

> Trích slide Slide 73: SWE-Marathon — Coding Agent Chạy Nhiều Ngày Setup: 20 task project-scale, siêu dài hạn: clone thư viện, clone sản phẩm full-stack (vd Slack clone, chấm bằng computer-use agent thao tác UI thật), ML engineering với API ngoài, và cả “viết compiler C từ đầu bằng Rust”. Quy mô trajectory Trung bình 27.2 triệu token/trajectory —…

**Đọc như kỹ sư:** Quy mô trajectory Trung bình 27.2 triệu token/trajectory — dài hơn SWE-bench, Terminal-Bench rất nhiều lần.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Kết quả (6/2026) Không agent nào vượt 30% pass@1.
- Lỗi thường gặp: self-verification yếu, phục hồi lỗi kém, dừng sớm, hoặc cố “lách” môi trường chấm điểm.
- Lưu ý: Đây là minh chứng rõ nhất cho xu hướng long-horizon: SWE-bench (1 PR) đã saturate, ngành chuyển sang task nhiều tuần công việc.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 73 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"e74323a2-513f-5992-b48c-d85fa1adcb93","locator":{"kind":"html_section","section_id":"c9","order":12,"heading":"10 Regression gate & failure analysis","source_file":"day14.html"},"checksum":"0092b47274bba51350d77dd8e9fbdbd37c9539f833d99855096080c3e850a57d"} -->

## 10 Regression gate & failure analysis

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 74 Regression gate & failure analysis · Mental model & quyết định

> Trích slide Slide 74: MirrorCode — Xây Lại T oàn Bộ Phần Mềm Từ Đầu Setup: Agent phải reimplement toàn bộ program — không được xem source code gốc — sao cho hành vi khớp original trên test end-to-end held-out. 25 program mục tiêu: Unix utilities, serialization, bioinformatics, interpreter, cryptography... Cách chấm Agent chỉ có behavior spec/test,…

MirrorCode — Xây Lại T oàn Bộ Phần Mềm Từ Đầu Setup: Agent phải reimplement toàn bộ program — không được xem source code gốc — sao cho hành vi khớp original trên test end-to-end held-out.. Điểm nối sang production là: failure taxonomy phải dẫn tới hành động sửa cụ thể.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- 25 program mục tiêu: Unix utilities, serialization, bioinformatics, interpreter, cryptography...
- Cách chấm Agent chỉ có behavior spec/test, không có source.
- Build lại từ đầu→ chạy test end-to-end → so khớp hành vi với bản gốc.

#### Tự kiểm tra · Với regression gate & failure analysis, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là failure taxonomy phải dẫn tới hành động sửa cụ thể.

### Slide 78 Regression gate & failure analysis · Evidence & failure lens

> Trích slide Slide 78: 5 Whys Cho AI Failures Symptom: Agent trả lời sai về refund policy Why 1: Answer không dựa trên đúng document Why 2: Retriever không lấy được policy mới nhất Why 3: Policy mới chưa được index vào vector store Why 4: Ingestion pipeline không có scheduled re-index Root cause Vấn đề thật không phải prompt hay model. Vấn đề là…

**Đọc như kỹ sư:** Fix đúng chỗ sẽ giải quyết hàng loạt failures tương tự.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 78 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 81 Regression gate & failure analysis · Evidence & failure lens

> Trích slide Slide 81: Continuous Improvement Loop Evaluate Run benchmark Analyze Find failures Improve Fix root cause Augment Add to benchmark Eval-driven development Eval trước khi optimize. Fix dựa trên evidence. Thêm failure cases vào bench- mark. Lặp lại. Giảng viên (VinUni) AICB · Evaluation 2026 70 / 76

**Đọc như kỹ sư:** Continuous Improvement Loop Evaluate Run benchmark Analyze Find failures Improve Fix root cause Augment Add to benchmark Eval-driven development Eval trước khi optimize.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 81 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"5ffe842a-f90b-595c-9624-bf68a6a07d18","locator":{"kind":"html_section","section_id":"c10","order":13,"heading":"11 Benchmark và Lab 14","source_file":"day14.html"},"checksum":"c0d0613743cf73f94171c7be85182cd759367ec170e4d9decd7fe8671712a408"} -->

## 11 Benchmark và Lab 14

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 82 Benchmark và Lab 14 · Mental model & quyết định

> Trích slide Slide 82: Liên Kết Với Day 13 Observability Eval (Day 14) + Observability (Day 13) = 2 mặt 1 đồng xu. Observability: cái gì đang xảy ra ngay bây giờ? Evaluation: chất lượng của cái đang xảy ra là bao nhiêu? # In production handler @track_observability # from Day 13 def handle_query(q): response = agent.run(q) if random.random() < 0.01:…

Liên Kết Với Day 13 Observability Eval (Day 14) + Observability (Day 13) = 2 mặt 1 đồng xu.. Điểm nối sang production là: không có dataset đại diện thì điểm eval không đại diện production. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Observability: cái gì đang xảy ra ngay bây giờ?
- Evaluation: chất lượng của cái đang xảy ra là bao nhiêu?
- 10 Hands-on & Key T akeaways Mục tiêu cuối cùng: bạn có con số cụ thể để trả lời “agent tốt đến đâu” và biết phải cải thiện ở đâu

#### Tự kiểm tra · Với benchmark và lab 14, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là không có dataset đại diện thì điểm eval không đại diện production.

### Slide 86 Benchmark và Lab 14 · Evidence & failure lens

> Trích slide Slide 86: Blueprint Cần Nộp Evaluation ■ Golden dataset (20 QA pairs) ■ RAGAS scores (4 metrics) ■ LLM-as-Judge scores (10+ items) ■ Score interpretation Failure Analysis ■ 3 worst cases detailed ■ 5 Whys per case ■ Root cause clusters ■ Improvement recommendations Lưu ý: Không cần perfect scores. Điều cần chứng minh là bạn biết agent…

**Đọc như kỹ sư:** Improvement recommendations Lưu ý: Không cần perfect scores.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Điều cần chứng minh là bạn biết agent tốt đến đâu, yếu ở đâu, và phải fix gì.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 86 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 90 Benchmark và Lab 14 · Evidence & failure lens

> Trích slide Slide 90: Hỏi & Đáp Evaluation tốt nghĩa là bạn biết agent tốt đến đâu, yếu ở đâu, và phải fix gì tiếp theo.

**Đọc như kỹ sư:** Hỏi & Đáp Evaluation tốt nghĩa là bạn biết agent tốt đến đâu, yếu ở đâu, và phải fix gì tiếp theo.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 90 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"1f7bf5ee-6b06-50e8-aa15-759c4faf974a","locator":{"kind":"html_section","section_id":"ladder","order":14,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"day14.html"},"checksum":"2ed4749ab317ac0cdb068f0b85738b8bacf5400beaaa6416a858ff70c291b51b"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của Evaluation & RAGAS bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"fa1c99d0-cd31-5fa4-9416-9f279b427d21","locator":{"kind":"html_section","section_id":"section-015","order":15,"heading":"∑ Phòng mô phỏng quyết định","source_file":"day14.html"},"checksum":"2fa59d7d6392ade34a5d120f0d8f92927d0051233a3f1fc14cf12490c5cc81f9"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Eval gate — điểm cao có che một lỗi chí mạng?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Faithfulness:**: min `0`, max `100`, step `1`, default `82`

- **Control - Relevance:**: min `0`, max `100`, step `1`, default `88`

- **Control - Context recall:**: min `0`, max `100`, step `1`, default `74`

- **Control - Correctness:**: min `0`, max `100`, step `1`, default `85`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Confidence interval — chênh lệch này có đáng tin?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Điểm trung bình:**: min `0`, max `100`, step `1`, default `78`

- **Control - Độ lệch chuẩn:**: min `1`, max `30`, step `1`, default `12`

- **Control - Số mẫu:**: min `10`, max `1000`, step `10`, default `100`

- **Control - Uplift kỳ vọng:**: min `0`, max `15`, step `1`, default `4`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — LLM-as-Judge — agreement cao có thể vẫn giả?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Agreement quan sát:**: min `50`, max `100`, step `1`, default `82`

- **Control - Judge A cho pass:**: min `10`, max `95`, step `1`, default `70`

- **Control - Judge B cho pass:**: min `10`, max `95`, step `1`, default `75`

- **Control - Số case:**: min `20`, max `1000`, step `20`, default `200`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"f9ebb43b-78c9-5924-92bf-1e6bd993ca65","locator":{"kind":"html_section","section_id":"misc","order":16,"heading":"✕ Hiểu lầm phổ biến","source_file":"day14.html"},"checksum":"4604dc1d64db628cb9f0acd89497023127732b27d8d8826d09af2909208eda3f"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai vì sao ai cần evaluation khác là phần còn lại tự động an toàn và ổn định.

Sửa lại Không có dataset đại diện thì điểm eval không đại diện production.

Vì sao quan trọng · slide 1 · 5 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai evaluation taxonomy là phần còn lại tự động an toàn và ổn định.

Sửa lại Tách retrieval quality khỏi answer quality.

Vì sao quan trọng · slide 9 · 13 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai golden dataset là phần còn lại tự động an toàn và ổn định.

Sửa lại Metric trung bình không được che hard failure.

Vì sao quan trọng · slide 17 · 21 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai ragas & rag metrics là phần còn lại tự động an toàn và ổn định.

Sửa lại LLM judge cần rubric, calibration và kiểm tra agreement.

Vì sao quan trọng · slide 25 · 29 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai llm-as-judge là phần còn lại tự động an toàn và ổn định.

Sửa lại Golden set phải version cùng dữ liệu và prompt.

Vì sao quan trọng · slide 33 · 37 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai rubric và calibration là phần còn lại tự động an toàn và ổn định.

Sửa lại Confidence interval quan trọng hơn một điểm lẻ.

Vì sao quan trọng · slide 41 · 45 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"0ec4ce03-b605-5c1a-bdc8-cfe22e33928e","locator":{"kind":"html_section","section_id":"apply","order":17,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"day14.html"},"checksum":"12d5148eef427f39d81655ef2a52909bda1d0bace39998d29661cdf7399766d9"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI đổi retriever: điểm trung bình tăng nhưng faithfulness giảm trên nhóm khách quốc tế.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Vì sao AI cần evaluation khác | Không có dataset đại diện thì điểm eval không đại diện production. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 5 |
| Evaluation taxonomy | Tách retrieval quality khỏi answer quality. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 9 · 13 |
| Golden dataset | Metric trung bình không được che hard failure. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 17 · 21 |
| RAGAS & RAG metrics | LLM judge cần rubric, calibration và kiểm tra agreement. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 25 · 29 |
| LLM-as-Judge | Golden set phải version cùng dữ liệu và prompt. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 33 · 37 |
| Rubric và calibration | Confidence interval quan trọng hơn một điểm lẻ. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 41 · 45 |
| Statistical rigor | Offline eval nhanh nhưng online signal mới phản ánh hành vi thật. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 50 · 54 |
| Agentic evaluation | Agent phải được chấm cả trajectory và side effect. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 58 · 62 |

---

<!-- chiron-source-span: {"source_span_id":"65023631-20ff-5572-9ebd-d6aaacaead23","locator":{"kind":"html_section","section_id":"numbers","order":18,"heading":"# Con số cần kiểm chứng","source_file":"day14.html"},"checksum":"f97e205428a59c4e63592b445b8f8bc6cec044fccc603d793d9694fef7cf7a62"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 1 m | ông tin quan trọng? Coherence Dễ đọc, có cấu trúc? Ngôn ngữ phù hợp với user? Lưu ý: 1 metric không đủ. Agent có thể cao correctness nhưng thấp relevance (đúng nhưng lạc đề). Cần đo cả 4 chiều. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 30 phút | ại eval Mục tiêu Thời gian Mỗi code release Offline (full suite) Regression check 10–30 phút Mỗi prompt change Offline (tar- geted) Không phá chỗ khác 5–10 phút Weekly Human (sam- pled) Quality trend 2–3h Continuous Online (moni- toring) Catc | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 12 |
| 10 phút | ression check 10–30 phút Mỗi prompt change Offline (tar- geted) Không phá chỗ khác 5–10 phút Weekly Human (sam- pled) Quality trend 2–3h Continuous Online (moni- toring) Catch degrada- tion realtime Trước demo/launch Offline + Hu- man Confide | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 12 |
| 1 ngày | toring) Catch degrada- tion realtime Trước demo/launch Offline + Hu- man Confidence 1 ngày Rule Eval nên chạy tự động trong CI/CD. Agent không pass eval = không được deploy, giống unit test. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 12 |
| 4 m | : ■ 20 test cases × 4 RAGAS metrics × judge LLM ■ ≈ 80 API calls × $0.01–0.05 ■ ≈ $1–4 mỗi lần chạy Chi phí tháng: ■ 100 PR/tháng → $100–400 ■ Cộng online sampling → $500–1000 Freq. Cost Catch bug Mỗi PR Cao Trước merge Daily TB Trong ngà | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 02 M | 02 Metrics Cho AI Agent Không phải mọi metric đều quan trọng như nhau — chọn metrics phải gắn với use case và business outcome | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 14 |
| 25% | 4. Trajectory eval: đánh giá cả con đường, không chỉ kết quả Ví dụ: 4 bước Tìm slot (25%), mời đúng người (25%), gửi invite (25%), add con- text (25%). Agent fail ở step 2 → partial = 25%, không phải 0%. Binary sẽ fail tất cả. Chọn cách n | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 16 |
| 0% | i invite (25%), add con- text (25%). Agent fail ở step 2 → partial = 25%, không phải 0%. Binary sẽ fail tất cả. Chọn cách nào Multi-step agent → trajectory. Simple QA → binary/partial. High-stakes → weighted. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 16 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"c635208b-583c-599b-8cad-db74d0669338","locator":{"kind":"html_section","section_id":"cheat","order":19,"heading":"▣ Cheat sheet ôn thi","source_file":"day14.html"},"checksum":"f7f54392cb4276d2c12eb103c65e67db1dfaa1b92a00963b8dd7f9c479f8c9d8"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp vì sao ai cần evaluation khác | không có dataset đại diện thì điểm eval không đại diện production | 1 · 5 |
| Khi gặp evaluation taxonomy | tách retrieval quality khỏi answer quality | 9 · 13 |
| Khi gặp golden dataset | metric trung bình không được che hard failure | 17 · 21 |
| Khi gặp ragas & rag metrics | LLM judge cần rubric, calibration và kiểm tra agreement | 25 · 29 |
| Khi gặp llm-as-judge | golden set phải version cùng dữ liệu và prompt | 33 · 37 |
| Khi gặp rubric và calibration | confidence interval quan trọng hơn một điểm lẻ | 41 · 45 |
| Khi gặp statistical rigor | offline eval nhanh nhưng online signal mới phản ánh hành vi thật | 50 · 54 |
| Khi gặp agentic evaluation | agent phải được chấm cả trajectory và side effect | 58 · 62 |
| Khi gặp safety & red teaming | benchmark công khai không thay thế domain eval | 66 · 70 |
| Khi gặp regression gate & failure analysis | failure taxonomy phải dẫn tới hành động sửa cụ thể | 74 · 78 |

---

<!-- chiron-source-span: {"source_span_id":"77438ce2-5667-522a-9fda-8a874879d71a","locator":{"kind":"html_section","section_id":"gloss","order":20,"heading":"☰ Từ điển thuật ngữ","source_file":"day14.html"},"checksum":"3983b2f8a0ae0792c105fdcffa6e81d84d934ae644ec3e6141cfb117ba01cf4d"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"833b5ad4-a7e5-554a-bbf6-c13766a6544c","locator":{"kind":"html_section","section_id":"bloom","order":21,"heading":"◉ Bạn đang ở mức nào?","source_file":"day14.html"},"checksum":"5309e2d4cce0cc9eb376c126abdbff9977cd758ab1624e1cc9a6e47c8eabb4d0"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 5 · 8 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 9 · 13 · 16 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 17 · 21 · 24 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 25 · 29 · 32 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 33 · 37 · 40 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 41 · 45 · 49 |
