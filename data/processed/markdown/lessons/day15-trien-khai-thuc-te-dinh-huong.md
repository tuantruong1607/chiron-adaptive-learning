---
schema_version: 1
course_id: rag-intensive
document_id: "9b9a62c1-47bd-5850-9797-4952f6419a8e"
document_version_id: "0a1514a9-75e5-57cd-acdb-ae9344bdbd7e"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Triển khai thực tế & Định hướng"
source_file: "day15-trien-khai-thuc-te-dinh-huong.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\day15-trien-khai-thuc-te-dinh-huong.html"
source_sha256: "e5b4bd775dfc6d6664b187da01c043040f0e8d28282fd96a757b8c403c5da939"
parser_version: chiron-structured-markdown-v1
html_section_count: 19
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# Triển khai thực tế & Định hướng

> Nối kiến trúc, tài chính và năng lực đội ngũ thành quyết định triển khai có thể bảo vệ trước stakeholder.

<!-- chiron-source-span: {"source_span_id":"0d182b3e-2302-55a6-8af8-57d0a2b126a9","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"0ca47c1c1d2cca0a195f88c1d1774271ccc29d5178458c19f6323f7c01b1f1f5"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: TCO gồm model, hạ tầng, con người và chi phí lỗi. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"0951dbe8-fc69-5088-8c09-64a010ad3ca8","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

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

<!-- chiron-source-span: {"source_span_id":"d4867c9c-d3cf-5ab6-9a5c-9fac5bdeb72a","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Từ prototype tới sản phẩm","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"69b72c6a9d289c0912662f0ba16c1ca44a5170de5ffccf1540aa6b05dcb03617"} -->

## 01 Từ prototype tới sản phẩm

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Từ prototype tới sản phẩm · Mental model & quyết định

> Trích slide Slide 1: Triển Khai Thực T ế, Chi Phí Vận Hành & Định Hướng Chuyên Sâu AICB-P1 · Ngày 15 · Ngày cuối Phase 1 T ên Giảng Viên VinUniversity · Phase 1 · 2026

Triển Khai Thực T ế, Chi Phí Vận Hành & Định Hướng Chuyên Sâu AICB-P1 · Ngày 15 · Ngày cuối Phase 1 T ên. Điểm nối sang production là: TCO gồm model, hạ tầng, con người và chi phí lỗi. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- “15 ngày trước bạn chưa biết LLM hoạt động thế nào.
- Hôm nay bạn đã có agent deployed, monitored, và evaluated.
- Câu hỏi bây giờ: đi sâu hướng nào?” Giữ câu hỏi này trong đầu khi học bài hôm nay

#### Tự kiểm tra · Với từ prototype tới sản phẩm, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là TCO gồm model, hạ tầng, con người và chi phí lỗi.

### Slide 4 Từ prototype tới sản phẩm · Evidence & failure lens

> Trích slide Slide 4: Mục Tiêu Ngày 15 ■ Hiểu thách thức triển khai enterprise: security, compliance, legacy systems ■ Phân tích cost anatomy của AI system và biết cách tối ưu chi phí ■ Nắm cost optimization strategies: model routing, semantic caching, prompt compression ■ Nhìn lại skills map đã tích luỹ qua 15 ngày ■ Chọn track Phase 2 phù hợp…

**Đọc như kỹ sư:** Hiểu thách thức triển khai enterprise: security, compliance, legacy systems

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Phân tích cost anatomy của AI system và biết cách tối ưu chi phí
- Nắm cost optimization strategies: model routing, semantic caching, prompt compression
- Chọn track Phase 2 phù hợp với mục tiêu nghề nghiệp

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 4 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 6 Từ prototype tới sản phẩm · Evidence & failure lens

> Trích slide Slide 6: Timeline: Hành Trình 15 Ngày N1 LLM N2 Bài toán N3 Agent N4 T ool Call N5 Product N6 PM N7 Data N8 RAG N9 Multi N10 UX N11 Safety N12 Deploy N13 Monitor N14 Eval N15 Wrap-up Nền tảng Xây dựng Production 3 giai đoạn: Hiểu nền tảng (N1–5) → Xây dựng hệ thống (N6–10) → Đưa lên production (N11–15) Giảng viên (VinUni) AICB · Ngày…

**Đọc như kỹ sư:** Timeline: Hành Trình 15 Ngày N1 LLM N2 Bài toán N3 Agent N4 T ool Call N5 Product N6 PM N7 Data N8 RAG N9 Multi N10 UX N11 Safety N12 Deploy N13 Monitor N14 Eval N15 Wrap-up Nền tảng Xây dựng Production 3 giai đoạn: Hiểu nền tảng (N1–5) → Xây dựng hệ thống (N6

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 6 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"8903a61d-c146-5635-9695-9d07b42221ec","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Enterprise architecture","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"c8d9c09d3bb530b5b82d913a8da18439db7001af6e6cb1835f6ce4592c97dd5c"} -->

## 02 Enterprise architecture

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 7 Enterprise architecture · Mental model & quyết định

> Trích slide Slide 7: Milestones Đã Đạt Được Kỹ thuật ■ Gọi LLM API, so sánh models ■ Build ReAct agent + tool calling ■ RAG pipeline grounded ■ Multi-agent + MCP ■ Guardrails + safety testing Sản phẩm ■ Problem statement + PRD ■ UX với trust layer ■ Deployed trên cloud ■ Monitoring + alerting ■ Evaluation + benchmark Thông điệp Bạn không chỉ học…

Evaluation + benchmark Thông điệp Bạn không chỉ học lý thuyết.. Điểm nối sang production là: pilot phải có success metric và kill criteria. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Bạn đã build, deploy, monitor, và evaluate một AI product thật.
- 02 Triển Khai Enterprise Lab deploy lên Railway là bước đầu.
- Enterprise có thêm security policies, compliance, legacy systems, và network restrictions

#### Tự kiểm tra · Với enterprise architecture, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là pilot phải có success metric và kill criteria.

### Slide 10 Enterprise architecture · Evidence & failure lens

> Trích slide Slide 10: On-Premise vs Cloud vs Hybrid Cloud API On-Premise Hybrid Data control Thấp Cao nhất T uỳ chọn Setup time Phút T uần–tháng T uần Cost model Per-token Capex + GPU Mixed Performance Nhanh T uỳ hardware T uỳ routing Best for MVP, startup Bank, gov Enterprise Trend 2025–2026 Hybrid đang trở thành default cho enterprise VN:…

**Đọc như kỹ sư:** On-Premise vs Cloud vs Hybrid Cloud API On-Premise Hybrid Data control Thấp Cao nhất T uỳ chọn Setup time Phút T uần–tháng T uần Cost model Per-token Capex + GPU Mixed Performance Nhanh T uỳ hardware T uỳ routing Best for MVP, startup Bank, gov Enterprise Tren

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 10 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 12 Enterprise architecture · Evidence & failure lens

> Trích slide Slide 12: 03 Cost Anatomy Của AI System AI agent production không chỉ tốn tiền token. Hiểu đầy đủ cost structure mới optimize đúng chỗ

**Đọc như kỹ sư:** 03 Cost Anatomy Của AI System AI agent production không chỉ tốn tiền token.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Hiểu đầy đủ cost structure mới optimize đúng chỗ

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 12 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"f7e95b95-6562-5531-9fa1-243c1dcee216","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 TCO của hệ AI","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"8eb8f72f44d4b763238377836d92351f26827e7c178100f9c4e83f8168c9cba9"} -->

## 03 TCO của hệ AI

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 13 TCO của hệ AI · Mental model & quyết định

> Trích slide Slide 13: Cost Breakdown API T okens Input + Output Compute CPU/GPU Storage Vector DB Human Review Ops Monitor 40–60% 15–25% 5–10% 10–15% 5–10% Insight API tokens chiếm 40–60% cost. Optimize token usage là ROI cao nhất cho hầu hết AI systems. Giảng viên (VinUni) AICB · Ngày 15 2026 8 / 41

Cost Breakdown API T okens Input + Output Compute CPU/GPU Storage Vector DB Human Review Ops Monitor 40–60% 15–25% 5–10% 10–15% 5–10% Insight API tokens chiếm 40–60% cost.. Điểm nối sang production là: model mạnh nhất không mặc định là model kinh tế nhất.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Optimize token usage là ROI cao nhất cho hầu hết AI systems.
- Premature optimization is the root of all evil.
- 04 Cost Optimization Strategies Khi cost bắt đầu đáng kể, 4 strategies sau giúp giảm 30– 70% chi phí mà không ảnh hưởng chất lượng

#### Tự kiểm tra · Với tco của hệ ai, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là model mạnh nhất không mặc định là model kinh tế nhất.

### Slide 16 TCO của hệ AI · Evidence & failure lens

> Trích slide Slide 16: 04 Cost Optimization Strategies Khi cost bắt đầu đáng kể, 4 strategies sau giúp giảm 30– 70% chi phí mà không ảnh hưởng chất lượng

**Đọc như kỹ sư:** 04 Cost Optimization Strategies Khi cost bắt đầu đáng kể, 4 strategies sau giúp giảm 30– 70% chi phí mà không ảnh hưởng chất lượng

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 16 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 18 TCO của hệ AI · Evidence & failure lens

> Trích slide Slide 18: Model Routing — Chi Tiết User Request Complexity Classifier Haiku / GPT-4o-mini Fast + Cheap Opus / GPT-4o Strong + Expensive simple complex 70% traffic 30% traffic Kết quả Nếu 70% requests dùng cheap model (10x rẻ hơn), tổng cost giảm khoảng50% mà quality gần như không đổi trên simple tasks. Giảng viên (VinUni) AICB · Ngày 15…

**Đọc như kỹ sư:** Model Routing — Chi Tiết User Request Complexity Classifier Haiku / GPT-4o-mini Fast + Cheap Opus / GPT-4o Strong + Expensive simple complex 70% traffic 30% traffic Kết quả Nếu 70% requests dùng cheap model (10x rẻ hơn), tổng cost giảm khoảng50% mà quality gần

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 18 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"4bf39a73-52e8-5ac7-8b68-d643e45db1e6","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Cost optimization","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"81d580a21c69fd2aed2b0b0bc529cdf9b0513fc28a6c814e088e582bece3e53f"} -->

## 04 Cost optimization

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 19 Cost optimization · Mental model & quyết định

> Trích slide Slide 19: 05 Scaling & Reliability Produc- tion Khi agent phục vụ enterprise, cần thêm queue, circuit breaker, và SLA commitment

05 Scaling & Reliability Produc- tion Khi agent phục vụ enterprise, cần thêm queue, circuit breaker, và SLA commitment. Điểm nối sang production là: routing cần quality floor trước khi tối ưu giá. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Production Patterns Queue-Based Processing High load → request queue → smooth out spikes.
- T ool:Redis Queue, Celery, Bull Circuit Breaker Khi LLM API down, degrade grace- fully.
- Pattern: closed → open → half-open Horizontal Scaling Stateless agent → N instances.

#### Tự kiểm tra · Với cost optimization, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là routing cần quality floor trước khi tối ưu giá.

### Slide 22 Cost optimization · Evidence & failure lens

> Trích slide Slide 22: Skills Map — 3 Pillars CP3: AI Engineering ■ LLM API ■ ReAct Agent ■ Prompt Engineering ■ Tool Calling ■ Embedding ■ RAG Pipeline ■ Multi-Agent ■ Guardrails ■ Evaluation CP2: Infrastructure ■ Vector Store ■ Data Pipeline ■ Docker ■ Cloud Deploy ■ Monitoring ■ Structured Logging ■ Tracing CP1: Business ■ Problem Statement ■ AI…

**Đọc như kỹ sư:** Cost Analysis Sau 15 ngày: bạn đã có deployed, monitored, evaluated AI product + skills across 3 pillars.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 22 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 24 Cost optimization · Evidence & failure lens

> Trích slide Slide 24: Thị Trường Việc Làm AI T oàn Cầu Đến 2030 170M Việc làm mới được tạo ra 92M Việc làm bị mất đi +78M Tăng trưởng ròng (+7%) Bức tranh lớn 86% nhà tuyển dụng kỳ vọng AI sẽ biến đổi doanh nghiệp của họ đến 2030. Nhưng 63% coi khoảng cách kỹ năng là rào cản lớn nhất — cơ hội không tự động biến thành việc làm nếu thiếu kỹ năng…

**Đọc như kỹ sư:** Thị Trường Việc Làm AI T oàn Cầu Đến 2030 170M Việc làm mới được tạo ra 92M Việc làm bị mất đi +78M Tăng trưởng ròng (+7%) Bức tranh lớn 86% nhà tuyển dụng kỳ vọng AI sẽ biến đổi doanh nghiệp của họ đến 2030.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nhưng 63% coi khoảng cách kỹ năng là rào cản lớn nhất — cơ hội không tự động biến thành việc làm nếu thiếu kỹ năng đúng.
- Nguồn: World Economic Forum, Future of Jobs Report 2025

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 24 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"d25b616e-4dfc-58b3-baa7-1032d391b24f","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 Model routing","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"2c2add2b944c4837e9ffa931c57a4130f9fb4a4308aef8650f3e78a562a14f3a"} -->

## 05 Model routing

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 25 Model routing · Mental model & quyết định

> Trích slide Slide 25: Việt Nam Trong Bức Tranh T oàn Cầu Chỉ số Việt Nam T oàn cầu Tổ chức có chương trình AI đang chạy 96% 88% Skills gap là rào cản chuyển đổi 78% 63% Kế hoạch cắt giảm nhân sự vì AI 58% 41% Kế hoạch reskilling để làm cùng AI 52% 77% Cải thiện phát triển nhân tài nội bộ ≈0% 84% Đọc vị: nhu cầu AI ở Việt Nam cao hơn thế giới, nhưng…

Nguồn: World Economic Forum, Future of Jobs Report 2025 — Vietnam Country Profile. Điểm nối sang production là: buy giảm time-to-market nhưng tăng dependency. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Nghịch Lý 2025–2026: Đầu Tư T ối Đa, Cắt Giảm T ối Đa Đầu tư kỷ lục
- Đầu tư AI doanh nghiệp toàn cầu: $252.3 tỷ (2024) → $581.7 tỷ (2025, +130%) Nguồn: Stanford HAI AI Index 2025/2026; CNBC Cắt giảm song song
- Amazon: cắt 14.000 + 16.000 vị trí (2025–2026)

#### Tự kiểm tra · Với model routing, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là buy giảm time-to-market nhưng tăng dependency.

### Slide 28 Model routing · Evidence & failure lens

> Trích slide Slide 28: Ba Nhóm Nghề AI: Từ Nghiên Cứu Đến Sản Phẩm Sau khi thấy bức tranh vĩ mô, hãy đi sâu vào 3 nhóm nghề cụ thể mà 3 track Phase 2 dẫn tới — mỗi nhóm có tốc độ tăng trưởng, mức lương, và rào cản gia nhập khác nhau. AI Engineer #1 fastest-growing job title (LinkedIn, 2 năm liên tiếp) AI Infrastructure Kỹ năng khó tuyển #1 toàn cầu…

**Đọc như kỹ sư:** Ba Nhóm Nghề AI: Từ Nghiên Cứu Đến Sản Phẩm Sau khi thấy bức tranh vĩ mô, hãy đi sâu vào 3 nhóm nghề cụ thể mà 3 track Phase 2 dẫn tới — mỗi nhóm có tốc độ tăng trưởng, mức lương, và rào cản gia nhập khác nhau.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- AI Engineer #1 fastest-growing job title (LinkedIn, 2 năm liên tiếp) AI Infrastructure Kỹ năng khó tuyển #1 toàn cầu (ManpowerGroup 2026) AI Product Tăng trưởng +300%/3 năm, nhưng thiếu cửa junior

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 28 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 30 Model routing · Evidence & failure lens

> Trích slide Slide 30: AI Infrastructure: Nhóm Khó Tuyển Nhất Thế Giới Demand & Lương MLOps: tăng trưởng 9.8x trong 5 năm (LinkedIn Emerging Jobs) Senior/staff MLOps: $257K–$312K Chi tiêu hạ tầng AI toàn cầu: $334 tỷ (2025) → $497 tỷ (2026) → vượt $1.000 tỷ vào 2029 (IDC) Khan Hiếm Nhân Sự “AI Model & Application Develop- ment” là kỹ năng khó tìm #1…

**Đọc như kỹ sư:** AI Infrastructure: Nhóm Khó Tuyển Nhất Thế Giới Demand & Lương MLOps: tăng trưởng 9.8x trong 5 năm (LinkedIn Emerging Jobs) Senior/staff MLOps: $257K–$312K Chi tiêu hạ tầng AI toàn cầu: $334 tỷ (2025) → $497 tỷ (2026) → vượt $1.000 tỷ vào 2029 (IDC) Khan Hiếm

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 30 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"5166fc30-ee6e-54c1-9275-da2f85dcf6d0","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Scaling team và platform","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"7fd852dfce78a5ea891e5850ef6b2a1bc3732b225dcf2d8b7a61353bcf9df64f"} -->

## 06 Scaling team và platform

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 31 Scaling team và platform · Mental model & quyết định

> Trích slide Slide 31: AI Product: T ăng Trưởng Nhanh Nhưng Thiếu Cửa Junior Demand & Lương AI PM postings: +300% trong 3 năm, nhân đôi năm 2025 Lương trung vị AI PM: $194–197K (hội tụ Glassdoor & axialsearch) AI Strategist: $208K trung vị, $279K ở cấp Director OpenAI PM trung vị: ~$860K Lưu ý: Chỉ 2% postings AI PM là cấp junior — 47% là cấp…

AI Strategist còn nghiêng hơn: 69– 80% là Director/VP/C-suite.. Điểm nối sang production là: platform chỉ đáng xây khi nhiều use case dùng lại. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Thị trường “nóng nhưng chưa có lộ trình sự nghiệp rõ ràng cho người mới bắt đầu”.
- Nguồn: axialsearch Labor Market Analysis 2026; Glassdoor; levels.fyi
- Các báo cáo lớn dùng nhiều khái niệm dễ nhầm lẫn.

#### Tự kiểm tra · Với scaling team và platform, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là platform chỉ đáng xây khi nhiều use case dùng lại.

### Slide 34 Scaling team và platform · Evidence & failure lens

> Trích slide Slide 34: Nghề T ăng Trưởng: Được AI Khuếch Đại T op nghề tăng trưởng (WEF) 1. Big Data Specialists 2. FinTech Engineers 3. AI/ML Specialists 4. Software Developers 5. DevOps Engineers Vì sao tăng trưởng Wage premium kỹ năng AI: 56% trung bình (PwC), có ngành tới 118% Việc làm cần kỹ năng AI tăng nhanh gấp 8 lần thị trường chung Năng…

**Đọc như kỹ sư:** Nghề T ăng Trưởng: Được AI Khuếch Đại T op nghề tăng trưởng (WEF) 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nguồn: World Economic Forum 2025; PwC Global AI Jobs Barometer 2025

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 34 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 36 Scaling team và platform · Evidence & failure lens

> Trích slide Slide 36: Case Study Cân Bằng: Tự Động Hoá Không Phải Lúc Nào Cũng Thắng Klarna: Cắt Rồi Phải Tuyển Lại Cắt từ 5.500 xuống 3.400 nhân sự, thay bằng chatbot AI (2024) Sau đó: chất lượng dịch vụ giảm, khách hàng phàn nàn → tuyển lại người “Luôn phải rõ ràng với khách hàng rằng sẽ luôn có một con người nếu bạn muốn.” — Sebastian…

**Đọc như kỹ sư:** Case Study Cân Bằng: Tự Động Hoá Không Phải Lúc Nào Cũng Thắng Klarna: Cắt Rồi Phải Tuyển Lại Cắt từ 5.500 xuống 3.400 nhân sự, thay bằng chatbot AI (2024) Sau đó: chất lượng dịch vụ giảm, khách hàng phàn nàn → tuyển lại người “Luôn phải rõ ràng với khách hàng

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 36 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"79f3c789-13e3-581f-a858-d8b09eae83c7","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Build–buy–partner","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"f5de13f1184308e9aa9ef1a8b12ac238eb42c2220e7267a73323fd4907761015"} -->

## 07 Build–buy–partner

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 37 Build–buy–partner · Mental model & quyết định

> Trích slide Slide 37: Việt Nam: Ngành Nào Phơi Nhiễm AI Cao Nhất? Ngành Mức độ phơi nhiễm AI Tài chính & Bảo hiểm 82.6% Bán buôn & Bán lẻ 76.3% Thông tin & Truyền thông 74.3% Đọc vị: phơi nhiễm cao không đồng nghĩa mất việc — đây là ngành có nhiều nhiệm vụ có thể được AI hỗ trợ, cơ hội để tăng năng suất nếu biết dùng AI đúng cách, thay vì lo sợ bị…

Nguồn: IMF SDN/2024/001, phân tích theo ngành cho Việt Nam. Điểm nối sang production là: năng lực production là giao điểm AI, software và domain. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Tương Lai & Chọn Track Cho Chính Bạn Ngay cả những người tạo ra AI cũng đang tranh luận về tương lai việc làm.
- Đừng hoảng loạn theo một tuyên bố đơn lẻ — hãy nhìn toàn cảnh và tự quyết định.
- Chuyên gia AI nói gì — và họ có thực sự đồng thuận không?

#### Tự kiểm tra · Với build–buy–partner, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là năng lực production là giao điểm AI, software và domain.

### Slide 40 Build–buy–partner · Evidence & failure lens

> Trích slide Slide 40: Cuộc Tranh Luận: Có Nên Lo Về Việc Làm Junior? Phe Cắt Giảm “Chúng tôi sẽ không tuyển thêm kỹ sư phần mềm năm sau vì năng suất đã tăng hơn 30% nhờ AI.” — Marc Benioff, CEO Salesforce 22% CHRO xác nhận có lãnh đạo đã ngừng tuyển entry-level vì AI (Gart- ner) Nguồn: Salesforce Ben; Gartner 2025–2026 Phe Phản Bác “Ý tưởng AI thay…

**Đọc như kỹ sư:** Cuộc Tranh Luận: Có Nên Lo Về Việc Làm Junior?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 40 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 42 Build–buy–partner · Evidence & failure lens

> Trích slide Slide 42: Chọn Track: Framework Cá Nhân Hoá Trục Track 1 — Product Track 2 — Infra Track 3 — Application Cơ hội thị trường Tăng nhanh (+300%/3 năm), ít cửa junior Khó tuyển nhất thế giới (ManpowerGroup) #1 fastest-growing title 2 năm liên tiếp Độ khó gia nhập Thấp–trung bình: portfo- lio hơn bằng cấp Trung bình–cao: cần nền tảng hệ…

**Đọc như kỹ sư:** Không có track “đúng tuyệt đối”; chọn theo giao điểm sở thích, năng lực, và mức độ sẵn sàng của chính bạn.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nguồn: Vietnam National Strategy on AI to 2030; Digital Policy Alert

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 42 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"01678d42-14b5-5ea3-96ca-6f2a92cda962","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Năng lực và lộ trình nghề nghiệp","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"57ac4b9784849c2fdd98f0c9d4506587f9cc97f52cccb1efb03776e2952b8600"} -->

## 08 Năng lực và lộ trình nghề nghiệp

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 43 Năng lực và lộ trình nghề nghiệp · Mental model & quyết định

> Trích slide Slide 43: 08 3 Track Giai Đoạn 2 Phase 1 cho nền tảng chung. Phase 2 đi sâu theo hướng bạn chọn — mỗi track 3 tuần chuyên sâu

08 3 Track Giai Đoạn 2 Phase 1 cho nền tảng chung.. Điểm nối sang production là: roadmap phải ưu tiên rủi ro lớn nhất trước feature đẹp. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Phase 2 đi sâu theo hướng bạn chọn — mỗi track 3 tuần chuyên sâu
- Track 1 — AI Business & Product Nội dung chính
- Go-to-market cho AI products Phù hợp với ai Người muốn làm: AI Product Manager AI Business Analyst AI Strategist Output Business plan cho AI product + financial model + compliance checklist + go- to-market strategy.

#### Tự kiểm tra · Với năng lực và lộ trình nghề nghiệp, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là roadmap phải ưu tiên rủi ro lớn nhất trước feature đẹp.

### Slide 46 Năng lực và lộ trình nghề nghiệp · Evidence & failure lens

> Trích slide Slide 46: Track 3 — AI Application Nội dung chính ■ Advanced Agent patterns ■ Memory & long-term context ■ GraphRAG & knowledge graphs ■ Fine-tuning & model customization ■ Production evaluation systems Phù hợp với ai Người muốn làm: AI Engineer LLM Engineer AI Agent Developer Output Advanced agent system + custom fine-tuned model +…

**Đọc như kỹ sư:** Production evaluation systems Phù hợp với ai Người muốn làm: AI Engineer LLM Engineer AI Agent Developer Output Advanced agent system + custom fine-tuned model + production eval pipeline + technical portfolio.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 46 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 48 Năng lực và lộ trình nghề nghiệp · Evidence & failure lens

> Trích slide Slide 48: 09 Career Paths & Kết Thúc Phase 1 15 ngày, 15 labs, 1 deployed product. Bạn không còn là beginner — bạn là builder

**Đọc như kỹ sư:** 09 Career Paths & Kết Thúc Phase 1 15 ngày, 15 labs, 1 deployed product.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 48 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"d7570dbb-4d89-57b8-95a9-74ee69cd2a2b","locator":{"kind":"html_section","section_id":"c8","order":11,"heading":"09 Chọn track & kế hoạch 90 ngày","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"2484d8081fe9e067aae3008ddccac2f92f3bdcbf9290d061ee4b2500b864c9c9"} -->

## 09 Chọn track & kế hoạch 90 ngày

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 49 Chọn track & kế hoạch 90 ngày · Mental model & quyết định

> Trích slide Slide 49: Career Paths Sau Khoá Học Pillar Roles Track Demand CP1 AI PM, AI BA, AI Strategist Track 1 Cao, khan hiếm CP2 AI Data Engi- neer, Platform Eng, MLOps Track 2 Rất cao CP3 AI Engineer, LLM En- gineer, Agent Dev Track 3 Cao nhất VSF Internship T ừ portfolio khóa học→ dự án thực tế tại Vingroup. Portfolio mạnh = cánh cửa mở.…

AMA — Ask Me Anything Open Q&A Session Mọi câu hỏi về kỹ thuật, career, track selection, hoặc bất kỳ điều gì bạn muốn hỏi.. Điểm nối sang production là: quyết định nghề nghiệp nên dựa trên artifact đã làm, không theo FOMO. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- “Track nào dễ xin việc hơn?” — Cả 3 đều thiếu người.
- “Fine-tuning có cần không?” — 80% use cases không cần.
- “AI sẽ thay lập trình viên không?” — AI thay code, không thay builder.

#### Tự kiểm tra · Với chọn track & kế hoạch 90 ngày, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là quyết định nghề nghiệp nên dựa trên artifact đã làm, không theo FOMO.

### Slide 52 Chọn track & kế hoạch 90 ngày · Evidence & failure lens

> Trích slide Slide 52: T ổng kết — Key T akeaways Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Enterprise deploykhác startup: security, compliance, on-premise, hybrid. Hiểu con- text trước khi chọn architecture. 2 Cost optimization: model routing, semantic caching, prompt compression. API to- kens chiếm 40–60% cost — optimize đúng chỗ. 3 3…

**Đọc như kỹ sư:** T ổng kết — Key T akeaways Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Enterprise deploykhác startup: security, compliance, on-premise, hybrid.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- 2 Cost optimization: model routing, semantic caching, prompt compression.
- API to- kens chiếm 40–60% cost — optimize đúng chỗ.
- 3 3 pillars, 3 tracks: CP1 (Business) → Track 1, CP2 (Infra)→ Track 2, CP3 (Application) → Track 3.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 52 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 55 Chọn track & kế hoạch 90 ngày · Evidence & failure lens

> Trích slide Slide 55: Cảm ơn! Tên Giảng Viên Email: a.nguyen@vinuni.edu.vn Tài liệu: github.com/vinuni/aicb-materials Chúc mừng hoàn thành Phase 1!

**Đọc như kỹ sư:** Tên.nguyen@vinuni.edu.vn Tài liệu: github.com/vinuni/aicb-materials Chúc mừng hoàn thành Phase 1!

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 55 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"ad238ee5-7e63-5551-82cb-b4f475002f35","locator":{"kind":"html_section","section_id":"ladder","order":12,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"f8a55bf9d603eae0d482facd991dc6d8d7498101e0349e45165bd658fc16d134"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của TCO, scaling & career bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"ab7dff31-eca3-5bce-aea5-25f892df5be5","locator":{"kind":"html_section","section_id":"section-013","order":13,"heading":"∑ Phòng mô phỏng quyết định","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"61183f6fa33986d1428ff6aa407dbe773c220cd0ad5bf99598a92546449a5172"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — TCO — hóa đơn model chỉ là một phần

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Request/ngày:**: min `100`, max `100000`, step `100`, default `8000`

- **Control - Token/request:**: min `500`, max `20000`, step `100`, default `4500`

- **Control - Giá/triệu token:**: min `1`, max `40`, step `1`, default `6`

- **Control - Hạ tầng + review:**: min `0`, max `10000`, step `100`, default `1800`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Model routing — tiết kiệm mà không phá quality

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Query đơn giản:**: min `0`, max `100`, step `5`, default `65`

- **Control - Model nhỏ:**: min `1`, max `20`, step `1`, default `2`

- **Control - Model mạnh:**: min `2`, max `60`, step `1`, default `12`

- **Control - Token/tháng:**: min `1`, max `500`, step `1`, default `120`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Track fit — chọn theo bằng chứng, không theo FOMO

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Hứng thú product:**: min `0`, max `100`, step `5`, default `65`

- **Control - Hứng thú infra:**: min `0`, max `100`, step `5`, default `45`

- **Control - Hứng thú ứng dụng:**: min `0`, max `100`, step `5`, default `80`

- **Control - Độ sâu kỹ thuật:**: min `0`, max `100`, step `5`, default `60`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"007623ba-c8e6-5598-a1b2-8ac934f7a1cc","locator":{"kind":"html_section","section_id":"misc","order":14,"heading":"✕ Hiểu lầm phổ biến","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"ffc815be4a0efbc6d5578c4880d80283bca5663e322575513bd750ffd672d0ea"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai từ prototype tới sản phẩm là phần còn lại tự động an toàn và ổn định.

Sửa lại TCO gồm model, hạ tầng, con người và chi phí lỗi.

Vì sao quan trọng · slide 1 · 4 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai enterprise architecture là phần còn lại tự động an toàn và ổn định.

Sửa lại Pilot phải có success metric và kill criteria.

Vì sao quan trọng · slide 7 · 10 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai tco của hệ ai là phần còn lại tự động an toàn và ổn định.

Sửa lại Model mạnh nhất không mặc định là model kinh tế nhất.

Vì sao quan trọng · slide 13 · 16 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai cost optimization là phần còn lại tự động an toàn và ổn định.

Sửa lại Routing cần quality floor trước khi tối ưu giá.

Vì sao quan trọng · slide 19 · 22 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai model routing là phần còn lại tự động an toàn và ổn định.

Sửa lại Buy giảm time-to-market nhưng tăng dependency.

Vì sao quan trọng · slide 25 · 28 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai scaling team và platform là phần còn lại tự động an toàn và ổn định.

Sửa lại Platform chỉ đáng xây khi nhiều use case dùng lại.

Vì sao quan trọng · slide 31 · 34 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"f278b991-7c8b-56a7-90e3-972a2c601a25","locator":{"kind":"html_section","section_id":"apply","order":15,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"c46f167ed20ca490a5af9ff59e57018a9102ed77c9d67428e684511801db7ce6"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI chuẩn bị pilot chuỗi khách sạn và phải chọn build/buy, model routing, cùng lộ trình nhân sự.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Từ prototype tới sản phẩm | TCO gồm model, hạ tầng, con người và chi phí lỗi. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 4 |
| Enterprise architecture | Pilot phải có success metric và kill criteria. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 7 · 10 |
| TCO của hệ AI | Model mạnh nhất không mặc định là model kinh tế nhất. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 13 · 16 |
| Cost optimization | Routing cần quality floor trước khi tối ưu giá. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 19 · 22 |
| Model routing | Buy giảm time-to-market nhưng tăng dependency. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 25 · 28 |
| Scaling team và platform | Platform chỉ đáng xây khi nhiều use case dùng lại. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 31 · 34 |
| Build–buy–partner | Năng lực production là giao điểm AI, software và domain. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 37 · 40 |
| Năng lực và lộ trình nghề nghiệp | Roadmap phải ưu tiên rủi ro lớn nhất trước feature đẹp. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 43 · 46 |

---

<!-- chiron-source-span: {"source_span_id":"d69723b7-29ca-5ebd-aa48-00b0230516cd","locator":{"kind":"html_section","section_id":"numbers","order":16,"heading":"# Con số cần kiểm chứng","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"588f840b209491a3cd7bd796ac2f54cb0560fc282d554d2511ce77f6eae787f6"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 15 ngày | ? HÃ Y SUY NGHĨ... “15 ngày trước bạn chưa biết LLM hoạt động thế nào. Hôm nay bạn đã có agent deployed, monitored, và evaluated. Câu hỏi bây giờ: đi sâu hướng nào?” Giữ câu hỏi | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 2 |
| 1M | ùng khi: dev, demo, edge deploy- ment Lưu ý: Self-hosted tiết kiệm khi volume cao (> 1M tokens/ngày). Dưới mức đó, cloud API rẻ hơn khi tính cả chi phí GPU, ops, và maintenance. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 11 |
| 60% | T okens Input + Output Compute CPU/GPU Storage Vector DB Human Review Ops Monitor 40–60% 15–25% 5–10% 10–15% 5–10% Insight API tokens chiếm 40–60% cost. Optimize token usage là ROI cao nhất cho hầu hết AI systems. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 25% | Input + Output Compute CPU/GPU Storage Vector DB Human Review Ops Monitor 40–60% 15–25% 5–10% 10–15% 5–10% Insight API tokens chiếm 40–60% cost. Optimize token usage là ROI cao nhất cho hầu hết AI systems. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 10% | + Output Compute CPU/GPU Storage Vector DB Human Review Ops Monitor 40–60% 15–25% 5–10% 10–15% 5–10% Insight API tokens chiếm 40–60% cost. Optimize token usage là ROI cao nhất cho hầu hết AI systems. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 15% | ut Compute CPU/GPU Storage Vector DB Human Review Ops Monitor 40–60% 15–25% 5–10% 10–15% 5–10% Insight API tokens chiếm 40–60% cost. Optimize token usage là ROI cao nhất cho hầu hết AI systems. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 30 ngày | st = (avg input tokens + avg output to- kens) × price per token × requests per day × 30 ngày Ví dụ thực tế 1000 tokens/request $3/1M input tokens (Sonnet) 500 requests/ngày = 1000 × $0.000003 × 500 × 30 = $45/tháng chỉ LLM API Lưu ý: Hidden c | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 14 |
| 1000 × | ày Ví dụ thực tế 1000 tokens/request $3/1M input tokens (Sonnet) 500 requests/ngày = 1000 × $0.000003 × 500 × 30 = $45/tháng chỉ LLM API Lưu ý: Hidden costs thường gấp 1.5–2x API cost: retry overhead, guardrails LLM calls, monitoring, eval p | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 14 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"e44da80a-0564-56fb-ba59-40a464191c74","locator":{"kind":"html_section","section_id":"cheat","order":17,"heading":"▣ Cheat sheet ôn thi","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"1d42fd02368df335a485d537bbcc65300e0dab61137e1e0f62d14c9cc6ef7cd7"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp từ prototype tới sản phẩm | TCO gồm model, hạ tầng, con người và chi phí lỗi | 1 · 4 |
| Khi gặp enterprise architecture | pilot phải có success metric và kill criteria | 7 · 10 |
| Khi gặp tco của hệ ai | model mạnh nhất không mặc định là model kinh tế nhất | 13 · 16 |
| Khi gặp cost optimization | routing cần quality floor trước khi tối ưu giá | 19 · 22 |
| Khi gặp model routing | buy giảm time-to-market nhưng tăng dependency | 25 · 28 |
| Khi gặp scaling team và platform | platform chỉ đáng xây khi nhiều use case dùng lại | 31 · 34 |
| Khi gặp build–buy–partner | năng lực production là giao điểm AI, software và domain | 37 · 40 |
| Khi gặp năng lực và lộ trình nghề nghiệp | roadmap phải ưu tiên rủi ro lớn nhất trước feature đẹp | 43 · 46 |
| Khi gặp chọn track & kế hoạch 90 ngày | quyết định nghề nghiệp nên dựa trên artifact đã làm, không theo FOMO | 49 · 52 |

---

<!-- chiron-source-span: {"source_span_id":"ba974177-510c-561e-bdbf-5874ce3acbf0","locator":{"kind":"html_section","section_id":"gloss","order":18,"heading":"☰ Từ điển thuật ngữ","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"6d13d14f5d7c4667f9837ee54031d2dcc945c7835fc3dc5cac44fcb5cbd63b0a"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"29ab4087-cab5-59af-a40b-e3a84d13edf9","locator":{"kind":"html_section","section_id":"bloom","order":19,"heading":"◉ Bạn đang ở mức nào?","source_file":"day15-trien-khai-thuc-te-dinh-huong.html"},"checksum":"c79b29cb58ab289bcf718fd3cf0cb0b37fe76f8b065a8c45bf1983cb440ddb40"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 4 · 6 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 7 · 10 · 12 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 13 · 16 · 18 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 19 · 22 · 24 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 25 · 28 · 30 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 31 · 34 · 36 |
