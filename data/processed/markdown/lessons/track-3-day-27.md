---
schema_version: 1
course_id: rag-intensive
document_id: "c39cb356-ea18-56d9-8b80-5e79af7a0c00"
document_version_id: "fb4c5180-55ee-5ef6-a696-fe5f1f11e5df"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Human-in-the-Loop — Thiết kế Quyền Phê duyệt"
source_file: "track-3-day-27.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-27.html"
source_sha256: "784bf99fb5d01c9d7631195abcfb1ee81bfe63014f42753b21c64d92561f2905"
parser_version: chiron-structured-markdown-v1
html_section_count: 19
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# Human-in-the-Loop — Thiết kế Quyền Phê duyệt

> Route theo expected loss, xây approval bền vững qua restart và thiết kế UX giúp con người quyết định thật.

<!-- chiron-source-span: {"source_span_id":"280300ad-2e3b-5e1a-9ef3-5f86c7f77546","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"track-3-day-27.html"},"checksum":"0d6b33fb2028ceb0e268f9c5b6e626b12d6846bebb5e6f2d17516a53c3724aae"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: HITL không phải một câu if quanh confidence. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"2d29e684-73ec-5b67-8f7d-49db696a27d8","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"track-3-day-27.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

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

<!-- chiron-source-span: {"source_span_id":"c690e1de-308a-5665-bf4a-518b8caa0bc4","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 HITL là system design","source_file":"track-3-day-27.html"},"checksum":"36fa2bdb9abc88d10b5ca7a5230ae0d8f01f6e45a14731ce4fb323105bf828f9"} -->

## 01 HITL là system design

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 HITL là system design · Mental model & quyết định

> Trích slide Slide 1: Human-in-the- Loop UX — Khi Nào Agent Cần Xin Phép? AICB-P2T3 · Ngày 27 · Chương 6 — Agent trong Production Giảng viên VinUniversity · Phase 2 · Track 3 · T uần 6

Human-in-the- Loop UX — Khi Nào Agent Cần Xin Phép?. Điểm nối sang production là: HITL không phải một câu if quanh confidence. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- AICB-P2T3 · Ngày 27 · Chương 6 — Agent trong Production
- “Agent tự quyết hay hỏi người dùng — ranh giới nào là an toàn và không làm phiền?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

#### Tự kiểm tra · Với hitl là system design, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là HITL không phải một câu if quanh confidence.

### Slide 2 HITL là system design · Evidence & failure lens

> Trích slide Slide 2:? HÃ Y SUY NGHĨ... “Agent tự quyết hay hỏi người dùng — ranh giới nào là an toàn và không làm phiền?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

**Đọc như kỹ sư:** “Agent tự quyết hay hỏi người dùng — ranh giới nào là an toàn và không làm phiền?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 2 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 3 HITL là system design · Evidence & failure lens

> Trích slide Slide 3: Nội dung vận hành 1. Tại sao Full Autonomy nguy hiểm? 2. HITL Taxonomy — 5 Interaction Patterns 3. Confidence Routing — Khi nào interrupt? 4. Approval Workflows & Implementation 5. Feedback Loops & Audit Trails 6. HITL UX Best Practices 7. Demo & Thực hành Giảng viên (VinUni) AICB · Ngày 27 T uần 6 1 / 17

**Đọc như kỹ sư:** Nội dung vận hành 1. Tại sao Full Autonomy nguy hiểm? 2. HITL Taxonomy — 5 Interaction Patterns 3. Confidence Routing — Khi nào interrupt? 4. Approval Workflows & Implementation 5. Feedback Loops & Audit Trails 6. HITL UX Best Practices 7. Demo & Thực hành

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 3 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"8b2c65f5-288f-5552-a213-ef8a58d12435","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Mức độ can thiệp của người","source_file":"track-3-day-27.html"},"checksum":"006dfca45e4f0a08f6a3cdd8629d3949f3465a45f369dc26c36d0a4e6e429d68"} -->

## 02 Mức độ can thiệp của người

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 4 Mức độ can thiệp của người · Mental model & quyết định

> Trích slide Slide 4: 01 T ại sao Full Autonomy nguy hiểm? T ừ sự cố thực tế đến nhu cầu Human-in-the-Loop

T ừ sự cố thực tế đến nhu cầu Human-in-the-Loop. Điểm nối sang production là: route phải tính impact và reversibility của action. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- User request Agent suy luận Xoá database Mất dữ liệu confidence 62% không ai kiểm tra!
- Email agent gửi nội bộ ra ngoài Lưu ý: Full autonomy chỉ an toàn khi mọi action đều reversible và low-cost.
- Trong thực tế, rất ít action thoả mãn cả hai.

#### Tự kiểm tra · Với mức độ can thiệp của người, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là route phải tính impact và reversibility của action.

### Slide 5 Mức độ can thiệp của người · Evidence & failure lens

> Trích slide Slide 5: Agent tự ý hành động — chuyện gì xảy ra? User request Agent suy luận Xoá database Mất dữ liệu confidence 62% không ai kiểm tra! Không có approval gate Sự cố thực tế: ■ Agent CS auto-refund $50K không cần duyệt ■ Code agent xoá branch production ■ Email agent gửi nội bộ ra ngoài Lưu ý: Full autonomy chỉ an toàn khi mọi action…

**Đọc như kỹ sư:** User request Agent suy luận Xoá database Mất dữ liệu confidence 62% không ai kiểm tra!

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Email agent gửi nội bộ ra ngoài Lưu ý: Full autonomy chỉ an toàn khi mọi action đều reversible và low-cost.
- Trong thực tế, rất ít action thoả mãn cả hai.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 5 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 6 Mức độ can thiệp của người · Evidence & failure lens

> Trích slide Slide 6: Analogy: Quy trình duyệt chi công ty <5 triệu T ự duyệt 5–50 triệu Trưởng phòng ký >50 triệu Giám đốc duyệt Auto-approve 1 approval Multi-level Dưới threshold → agent tự xử lý Vùng trung gian → cần 1 lần duyệt Rủi ro cao → phải escalate lên người có thẩm quyền Cùng nguyên tắc: chi phí sai lầm quyết định mức kiểm soát Giảng…

**Đọc như kỹ sư:** Analogy: Quy trình duyệt chi công ty <5 triệu T ự duyệt 5–50 triệu Trưởng phòng ký >50 triệu Giám đốc duyệt Auto-approve 1 approval Multi-level Dưới threshold → agent tự xử lý Vùng trung gian → cần 1 lần duyệt Rủi ro cao → phải escalate lên người có thẩm quyền

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 6 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"3e6379d7-43f8-5ccf-b344-63236ce691f0","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Confidence và expected loss","source_file":"track-3-day-27.html"},"checksum":"cdb9ca562ff8b3c7d20daed752dd9f3f53cc168c0a909c7ab9214ee8b30d7a4a"} -->

## 03 Confidence và expected loss

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 7 Confidence và expected loss · Mental model & quyết định

> Trích slide Slide 7: 02 HITL T axonomy — 5 Interac- tion Patterns Phân loại cách con người tham gia vào quyết định của agent

02 HITL T axonomy — 5 Interac- tion Patterns Phân loại cách con người tham gia vào quyết định của agent. Điểm nối sang production là: confidence cao không cho phép tự động hóa hành động không thể hoàn tác. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Bắt đầu strict, nới dần khi trust được xây dựng.
- 5 HITL Interaction Patterns # Pattern Khi nào?

#### Tự kiểm tra · Với confidence và expected loss, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là confidence cao không cho phép tự động hóa hành động không thể hoàn tác.

### Slide 8 Confidence và expected loss · Evidence & failure lens

> Trích slide Slide 8: Autonomy Spectrum — Từ tự động đến kiểm soát hoàn toàn Full Manual Người làm hết HITL Strict Duyệt mọi action HITL Bal- anced Duyệt theo risk HITL Light Chỉ audit log Full Auto Agent tự quyết An toàn cao Tốc độ caoSweet spot Không có vị trí “đúng” cố định — sweet spot phụ thuộc vàodomain risk, agent maturity, và user…

**Đọc như kỹ sư:** Bắt đầu strict, nới dần khi trust được xây dựng.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 8 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 9 Confidence và expected loss · Evidence & failure lens

> Trích slide Slide 9: 5 HITL Interaction Patterns # Pattern Khi nào? Ví dụ 1 Approval Action cao rủi ro Deploy, xoá data, gửi email 2 Clarification Input mơ hồ “Bạn muốn report Q1 hay Q2?” 3 Escalation Vượt khả năng Câu hỏi pháp lý, tài chính 4 Review Checkpoint Kết quả cần kiểm Draft email, code PR 5 Edit / Correction User muốn chỉnh Sửa nội dung…

**Đọc như kỹ sư:** 5 HITL Interaction Patterns # Pattern Khi nào?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 9 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"4263df4e-8d27-50cb-b3d3-8901c1305333","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Routing theo loại hành động","source_file":"track-3-day-27.html"},"checksum":"c94c6bfec3faef4fd229117927dd7bcaf2051b24a0e05fa97ae13581bf63637b"} -->

## 04 Routing theo loại hành động

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 10 Routing theo loại hành động · Mental model & quyết định

> Trích slide Slide 10: 03 Confidence Routing — Khi nào interrupt? Agent tự đánh giá confidence để quyết định hỏi hay tự làm

Agent tự đánh giá confidence để quyết định hỏi hay tự làm. Điểm nối sang production là: interrupt phải persist state trước khi chờ. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Confidence Routing — Luồng quyết định Agent Action Confidence?
- Nguyên tắc: Cost of Interrupt vs Cost of Error $10 Cost of error thấp → đừng hỏi 0.70 Confidence threshold mặc định $10K Cost of error cao → luôn hỏi Đo accuracy vs confidencetrên historical data.
- Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng lên.

#### Tự kiểm tra · Với routing theo loại hành động, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là interrupt phải persist state trước khi chờ.

### Slide 11 Routing theo loại hành động · Evidence & failure lens

> Trích slide Slide 11: Confidence Routing — Luồng quyết định Agent Action Confidence? Auto-execute (log only) Suggest + Wait (user confirms) Ask Human (full context) ≥0.85 0.70–0.85 <0.70 Policy Override delete/deploy/PII → always ask Lưu ý: Dù confidence = 0.99, agent vẫn PHẢI dừng nếu action vi phạm policy cố định (dữ liệu nhạy cảm, email…

**Đọc như kỹ sư:** Confidence Routing — Luồng quyết định Agent Action Confidence?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 11 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 12 Routing theo loại hành động · Evidence & failure lens

> Trích slide Slide 12: Nguyên tắc: Cost of Interrupt vs Cost of Error $10 Cost of error thấp → đừng hỏi 0.70 Confidence threshold mặc định $10K Cost of error cao → luôn hỏi Đo accuracy vs confidencetrên historical data. Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng lên. Đây là empirical tuning, không có magic number. Giảng…

**Đọc như kỹ sư:** Nguyên tắc: Cost of Interrupt vs Cost of Error $10 Cost of error thấp → đừng hỏi 0.70 Confidence threshold mặc định $10K Cost of error cao → luôn hỏi Đo accuracy vs confidencetrên historical data.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng lên.
- Đây là empirical tuning, không có magic number.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 12 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"caf5cba8-a974-5b67-be54-2c5b05bb5656","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 LangGraph interrupt","source_file":"track-3-day-27.html"},"checksum":"aa63e837b5f654df9e075a0b3dcb96a6e4bc65bd42a98e2724962654a2e460f4"} -->

## 05 LangGraph interrupt

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 13 LangGraph interrupt · Mental model & quyết định

> Trích slide Slide 13: 04 Approval Workflows & Imple- mentation LangGraph interrupt/resume và Streamlit approval UI

04 Approval Workflows & Imple- mentation LangGraph interrupt/resume và Streamlit approval UI. Điểm nối sang production là: resume cần idempotency để không lặp side effect. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- LangGraph HITL — Interrupt & Resume plan act INTERRUPT human review resume END destructive approve reject→abort Hai loại interrupt
- interrupt_before: pause trước destructive action
- interrupt_after: pause sau draft generation (review trước send) 1.

#### Tự kiểm tra · Với langgraph interrupt, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là resume cần idempotency để không lặp side effect.

### Slide 15 LangGraph interrupt · Evidence & failure lens

> Trích slide Slide 15: LangGraph HITL — Code-Level # Compile with interrupt graph = builder. compile( interrupt_before=["delete_action"], checkpointer=MemorySaver(), ) # Run until interrupt state = graph.invoke( input, config) print(state["pending_action"]) # => {"action": "delete_user", # "confidence": 0.62} # Human approves -> resume…

**Đọc như kỹ sư:** LangGraph HITL — Code-Level # Compile with interrupt graph = builder.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Define interrupt nodes: liệt kê tất cả destructive actions 2.
- State inspection: pending action + confidence + reasoning 3.
- Resume logic: update approved/rejected rồi continue Lưu ý: Luôn dùng checkpointer — không có persistence, graph “quên” state khi interrupt.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 15 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 16 LangGraph interrupt · Evidence & failure lens

> Trích slide Slide 16: Streamlit HITL UI — Approval Interface Agent Approval Request Action:delete_user(id=42) Confidence:62%(below threshold) Reason: “User inactive 2 years” - user: {id: 42, name: “Nguyên”, status: active} Approve Reject Edit UI components: 1. Action card: hiển thị pending action + confidence 2. Reasoning: giải thích tại sao agent…

**Đọc như kỹ sư:** Streamlit HITL UI — Approval Interface Agent Approval Request Action:delete_user(id=42) Confidence:62%(below threshold) Reason: “User inactive 2 years” - user: {id: 42, name: “Nguyên”, status: active} Approve Reject Edit UI components: 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Action card: hiển thị pending action + confidence 2.
- Reasoning: giải thích tại sao agent muốn làm 3.
- 3 buttons: Approve / Reject / Edit Mobile: Telegram bot approve/re- ject Batch: group low-risk actions → approve in bulk để giảm fatigue

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 16 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"15747034-7443-5c22-90a2-7208445cf76d","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Durable state & resume","source_file":"track-3-day-27.html"},"checksum":"f25f53fb63d64e1526f9f0f459945b84675c59886c47b1d390a2fd574631e84a"} -->

## 06 Durable state & resume

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 17 Durable state & resume · Mental model & quyết định

> Trích slide Slide 17: 05 Feedback Loops & Audit Trails Thu thập phản hồi, ghi log, và tăng autonomy dần

05 Feedback Loops & Audit Trails Thu thập phản hồi, ghi log, và tăng autonomy dần. Điểm nối sang production là: approval phải cho reviewer đủ context để quyết định. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Why: reasoning của agent + decision Lưu ý: Audit trail là compliance requirement (GDPR, SOC2).
- Build from day one — cannot retrofit sau khi đã production.
- Decision Analytics — Đo lường để cải thiện Approval rate 87% approved Response time median 45s Override rate 3% auto-rejected Agent đáng tin cậy →nới threshold 3 metrics quan trọng: 1.

#### Tự kiểm tra · Với durable state & resume, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là approval phải cho reviewer đủ context để quyết định.

### Slide 18 Durable state & resume · Evidence & failure lens

> Trích slide Slide 18: Audit Trail — Mỗi quyết định đều được ghi lại class AuditEntry(BaseModel): timestamp: datetime agent_id: str action: str confidence: float risk_level: str # low/med/high reviewer_id: str | None decision: str # auto/approve/reject reason: str | None execution_time_ms: int # Immutable: append-only PostgreSQL # Backup: S3 daily…

**Đọc như kỹ sư:** Why: reasoning của agent + decision Lưu ý: Audit trail là compliance requirement (GDPR, SOC2).

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Build from day one — cannot retrofit sau khi đã production.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 18 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 19 Durable state & resume · Evidence & failure lens

> Trích slide Slide 19: Decision Analytics — Đo lường để cải thiện Approval rate 87% approved Response time median 45s Override rate 3% auto-rejected Agent đáng tin cậy →nới threshold 3 metrics quan trọng: 1. Approval rate: cao → agent đáng tin, nới dần autonomy 2. Response time: lâu → UI gây phiền, cần batch approval 3. Override rate: cao →…

**Đọc như kỹ sư:** Decision Analytics — Đo lường để cải thiện Approval rate 87% approved Response time median 45s Override rate 3% auto-rejected Agent đáng tin cậy →nới threshold 3 metrics quan trọng: 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Approval rate: cao → agent đáng tin, nới dần autonomy 2.
- Response time: lâu → UI gây phiền, cần batch approval 3.
- Override rate: cao → confidence calibration sai Track metrics theo thời gian.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 19 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"1b31e45c-f2ce-55b0-bf85-11659fc69904","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Approval UX","source_file":"track-3-day-27.html"},"checksum":"3c2b6b521328f9ada163edfcdd46425fba31d0e8768726dccaffc10e960f5cc9"} -->

## 07 Approval UX

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 20 Approval UX · Mental model & quyết định

> Trích slide Slide 20: 06 HITL UX Best Practices Thiết kế trải nghiệm không làm phiền user

06 HITL UX Best Practices Thiết kế trải nghiệm không làm phiền user. Điểm nối sang production là: timeout và escalation là trạng thái nghiệp vụ. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- 07 Demo & Thực hành HITL Code Review Agent + Lab hands-on

#### Tự kiểm tra · Với approval ux, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là timeout và escalation là trạng thái nghiệp vụ.

### Slide 21 Approval UX · Evidence & failure lens

> Trích slide Slide 21: HITL UX — 5 Nguyên tắc vàng 1 Start strict, loosen gradually— bắt đầu duyệt mọi thứ, nới dần khi agent chứng minh tin cậy 2 Preemptive clarification— detect ambiguityở đầu vào, không phải giữa chừng execution 3 Explainable proposals— “Confidence 65% because [X]” giúp human quyết nhanh hơn 4 Batch approvals— group low-risk…

**Đọc như kỹ sư:** HITL UX — 5 Nguyên tắc vàng 1 Start strict, loosen gradually— bắt đầu duyệt mọi thứ, nới dần khi agent chứng minh tin cậy 2 Preemptive clarification— detect ambiguityở đầu vào, không phải giữa chừng execution 3 Explainable proposals— “Confidence 65% because [X

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 21 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 22 Approval UX · Evidence & failure lens

> Trích slide Slide 22: 07 Demo & Thực hành HITL Code Review Agent + Lab hands-on

**Đọc như kỹ sư:** 07 Demo & Thực hành HITL Code Review Agent + Lab hands-on

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 22 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"2ebceb3f-134b-5876-8d7a-fbc021dce542","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Audit, idempotency & timeout","source_file":"track-3-day-27.html"},"checksum":"9d6a984a3f7526a539e99f5935824bf84cbe71256ffee12236bdf056acd90035"} -->

## 08 Audit, idempotency & timeout

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 23 Audit, idempotency & timeout · Mental model & quyết định

> Trích slide Slide 23: HITL Code Review Agent — Side-by-side 1. Agent đọc PR, phân tích code changes, đề xuất review comments 2. Confidence 72%: hiển thị diff + reasoning → user Approve → agent commit 3. Confidence 58%: escalate — hiển thị context + câu hỏi cụ thể cho reviewer 4. Mỗi interaction ghi vào PostgreSQL audit trail — replay full session…

Agent đọc PR, phân tích code changes, đề xuất review comments 2.. Điểm nối sang production là: audit log phải ghi ai duyệt gì trên evidence nào. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Confidence 72%: hiển thị diff + reasoning → user Approve → agent commit 3.
- Confidence 58%: escalate — hiển thị context + câu hỏi cụ thể cho reviewer 4.
- Mỗi interaction ghi vào PostgreSQL audit trail — replay full session

#### Tự kiểm tra · Với audit, idempotency & timeout, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là audit log phải ghi ai duyệt gì trên evidence nào.

### Slide 24 Audit, idempotency & timeout · Evidence & failure lens

> Trích slide Slide 24: Lab #27 Mục tiêu: Build HITL agent với LangGraph interrupt + Streamlit approval UI Deliverable: HITL agent + approval UI + confidence-based routing + Post- greSQL audit trail Thời gian: 2 giờ Giảng viên (VinUni) AICB · Ngày 27 T uần 6 15 / 17

**Đọc như kỹ sư:** Lab #27 Mục tiêu: Build HITL agent với LangGraph interrupt + Streamlit approval UI Deliverable: HITL agent + approval UI + confidence-based routing + Post- greSQL audit trail Thời gian: 2 giờ

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 24 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 25 Audit, idempotency & timeout · Evidence & failure lens

> Trích slide Slide 25: Lab 27 — Các bước thực hành 1. Approval workflow: LangGraph interrupt_before cho delete/deploy actions 2. Confidence routing: auto khi ≥ 0.85, suggest khi 0.70–0.85, ask khi < 0.70 3. Streamlit UI: action card + diff view + Approve/Reject/Edit buttons 4. Audit trail: PostgreSQL append-only log, replay session, export report…

**Đọc như kỹ sư:** Approval workflow: LangGraph interrupt_before cho delete/deploy actions 2.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Confidence routing: auto khi ≥ 0.85, suggest khi 0.70–0.85, ask khi < 0.70 3.
- Streamlit UI: action card + diff view + Approve/Reject/Edit buttons 4.
- Audit trail: PostgreSQL append-only log, replay session, export report A/B test: full-auto vs HITL — đo user trust score và task success rate trên 20 test cases

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 25 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"a49c368f-9214-56cc-9974-f0496b0bea82","locator":{"kind":"html_section","section_id":"c8","order":11,"heading":"09 Autonomy ladder & Lab","source_file":"track-3-day-27.html"},"checksum":"83b3c17d2e5bdee72109fc1726ce41d8424954cda262dc39f6182e9544d2d3ca"} -->

## 09 Autonomy ladder & Lab

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 26 Autonomy ladder & Lab · Mental model & quyết định

> Trích slide Slide 26: T ổng kết — Key T akeaways Những ý chính cần nhớ sau buổi học hôm nay 1 HITL là responsible deployment — xây dựng trust incrementally, không phải dấu hiệu yếu kém 2 Confidence routing: 3 vùng (auto / suggest / ask) + policy override cho high-risk ac- tions 3 Audit trail là compliance requirement — build from day one, cannot…

Tiếp theo & Bài tập Ngày 28: Workshop T ổng Hợp — Full Production Agent System “Tất cả components đã build xong — N28 là ngày ghép lại thành hệ thống production hoàn chỉnh”. Điểm nối sang production là: autonomy chỉ tăng sau khi evidence đủ và rollback sẵn sàng.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Review lại tất cả labs N16–N27 — chuẩn bị integration
- AICB-P2T3 · Ngày 27 · Human-in-the-Loop UX github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn

#### Tự kiểm tra · Với autonomy ladder & lab, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là autonomy chỉ tăng sau khi evidence đủ và rollback sẵn sàng.

### Slide 28 Autonomy ladder & Lab · Evidence & failure lens

> Trích slide Slide 28: Hỏi & Đáp HITL có làm chậm agent không? Khi nào nên bỏ approval gate?

**Đọc như kỹ sư:** Hỏi & Đáp HITL có làm chậm agent không? Khi nào nên bỏ approval gate?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 28 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 29 Autonomy ladder & Lab · Evidence & failure lens

> Trích slide Slide 29: Cảm ơn! AICB-P2T3 · Ngày 27 · Human-in-the-Loop UX github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn

**Đọc như kỹ sư:** AICB-P2T3 · Ngày 27 · Human-in-the-Loop UX github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 29 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"8c144017-9ce1-50ce-85d4-43a7875bd02d","locator":{"kind":"html_section","section_id":"ladder","order":12,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"track-3-day-27.html"},"checksum":"7dc9eaa713cc5a3dffd995028976cc407988247a4d2d586fcba38615fd89a37d"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của HITL & durable approval bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"a997ebf5-ae96-59ce-aa0a-8e82c8531205","locator":{"kind":"html_section","section_id":"section-013","order":13,"heading":"∑ Phòng mô phỏng quyết định","source_file":"track-3-day-27.html"},"checksum":"7f8770a0080fe29bb3c945b835ced5b5bf30ca73e2b1a85182c0026508adce4b"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Expected loss — tự động hay hỏi người?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Confidence:**: min `0`, max `100`, step `1`, default `78`

- **Control - Thiệt hại khi sai:**: min `1`, max `1000`, step `1`, default `200`

- **Control - Chi phí interrupt:**: min `1`, max `100`, step `1`, default `8`

- **Control - Hệ số rủi ro:**: min `1`, max `10`, step `1`, default `3`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Approval queue — reviewer có thành bottleneck?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Action/giờ:**: min `1`, max `1000`, step `1`, default `120`

- **Control - Cần duyệt:**: min `0`, max `100`, step `1`, default `35`

- **Control - Phút/lần duyệt:**: min `1`, max `30`, step `1`, default `4`

- **Control - Reviewer:**: min `1`, max `50`, step `1`, default `4`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Autonomy ladder — bằng chứng nào cho phép nâng cấp?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Độ chính xác:**: min `50`, max `100`, step `1`, default `93`

- **Control - Override:**: min `0`, max `50`, step `1`, default `8`

- **Control - Severity sự cố:**: min `0`, max `10`, step `1`, default `2`

- **Control - Mẫu đã review:**: min `10`, max `5000`, step `10`, default `500`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"f173109b-94c7-5960-9c4d-a46efffc1bee","locator":{"kind":"html_section","section_id":"misc","order":14,"heading":"✕ Hiểu lầm phổ biến","source_file":"track-3-day-27.html"},"checksum":"ce58bc4a71cd43e8c4ba374170013c9b9002b0d86b18bb146926dcf4ed2e287c"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai hitl là system design là phần còn lại tự động an toàn và ổn định.

Sửa lại HITL không phải một câu if quanh confidence.

Vì sao quan trọng · slide 1 · 2 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai mức độ can thiệp của người là phần còn lại tự động an toàn và ổn định.

Sửa lại Route phải tính impact và reversibility của action.

Vì sao quan trọng · slide 4 · 5 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai confidence và expected loss là phần còn lại tự động an toàn và ổn định.

Sửa lại Confidence cao không cho phép tự động hóa hành động không thể hoàn tác.

Vì sao quan trọng · slide 7 · 8 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai routing theo loại hành động là phần còn lại tự động an toàn và ổn định.

Sửa lại Interrupt phải persist state trước khi chờ.

Vì sao quan trọng · slide 10 · 11 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai langgraph interrupt là phần còn lại tự động an toàn và ổn định.

Sửa lại Resume cần idempotency để không lặp side effect.

Vì sao quan trọng · slide 13 · 15 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai durable state & resume là phần còn lại tự động an toàn và ổn định.

Sửa lại Approval phải cho reviewer đủ context để quyết định.

Vì sao quan trọng · slide 17 · 18 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"be22c66c-5cbb-57ff-987a-1aa337a453ef","locator":{"kind":"html_section","section_id":"apply","order":15,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"track-3-day-27.html"},"checksum":"2a6c94dfeff5dc2b5e4e20da98dd4ed23ee77ee051a7ace1a0fb74c8db09ec7e"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI có thể đề xuất hoàn tiền nhưng phải dừng đúng chỗ, lưu state, audit và tiếp tục idempotently sau duyệt.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| HITL là system design | HITL không phải một câu if quanh confidence. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 2 |
| Mức độ can thiệp của người | Route phải tính impact và reversibility của action. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 4 · 5 |
| Confidence và expected loss | Confidence cao không cho phép tự động hóa hành động không thể hoàn tác. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 7 · 8 |
| Routing theo loại hành động | Interrupt phải persist state trước khi chờ. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 10 · 11 |
| LangGraph interrupt | Resume cần idempotency để không lặp side effect. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 13 · 15 |
| Durable state & resume | Approval phải cho reviewer đủ context để quyết định. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 17 · 18 |
| Approval UX | Timeout và escalation là trạng thái nghiệp vụ. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 20 · 21 |
| Audit, idempotency & timeout | Audit log phải ghi ai duyệt gì trên evidence nào. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 23 · 24 |

---

<!-- chiron-source-span: {"source_span_id":"2c39ff30-8af8-542a-913a-e34e30c900fa","locator":{"kind":"html_section","section_id":"numbers","order":16,"heading":"# Con số cần kiểm chứng","source_file":"track-3-day-27.html"},"checksum":"d3a56228392935de44f5ca9d650425ff349b1aabd55fc7fbff32d00ccc5a093e"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 62% | — chuyện gì xảy ra? User request Agent suy luận Xoá database Mất dữ liệu confidence 62% không ai kiểm tra! Không có approval gate Sự cố thực tế: ■ Agent CS auto-refund $50K không cần duyệt ■ Code agent xoá branch production ■ Email agent | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 5 |
| $50K | 62% không ai kiểm tra! Không có approval gate Sự cố thực tế: ■ Agent CS auto-refund $50K không cần duyệt ■ Code agent xoá branch production ■ Email agent gửi nội bộ ra ngoài Lưu ý: Full autonomy chỉ an toàn khi mọi action đều reversible v | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 5 |
| $10K | s Cost of Error $10 Cost of error thấp → đừng hỏi 0.70 Confidence threshold mặc định $10K Cost of error cao → luôn hỏi Đo accuracy vs confidencetrên historical data. Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 12 |
| 0.80 m | f error cao → luôn hỏi Đo accuracy vs confidencetrên historical data. Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng lên. Đây là empirical tuning, không có magic number. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 12 |
| 60% | Đo accuracy vs confidencetrên historical data. Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng lên. Đây là empirical tuning, không có magic number. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 12 |
| 87% | Decision Analytics — Đo lường để cải thiện Approval rate 87% approved Response time median 45s Override rate 3% auto-rejected Agent đáng tin cậy →nới threshold 3 metrics quan trọng: 1. Approval rate: cao → agen | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 19 |
| 45s | on Analytics — Đo lường để cải thiện Approval rate 87% approved Response time median 45s Override rate 3% auto-rejected Agent đáng tin cậy →nới threshold 3 metrics quan trọng: 1. Approval rate: cao → agent đáng tin, nới dần autonomy 2. Re | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 19 |
| 3% | lường để cải thiện Approval rate 87% approved Response time median 45s Override rate 3% auto-rejected Agent đáng tin cậy →nới threshold 3 metrics quan trọng: 1. Approval rate: cao → agent đáng tin, nới dần autonomy 2. Response time: lâu | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 19 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"2a9ebe54-8931-5a0f-ab3a-6769064160c0","locator":{"kind":"html_section","section_id":"cheat","order":17,"heading":"▣ Cheat sheet ôn thi","source_file":"track-3-day-27.html"},"checksum":"386fb3536365a8992f381e58c98b2a755e92e1b7fdbae005725b2cc02604b264"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp hitl là system design | HITL không phải một câu if quanh confidence | 1 · 2 |
| Khi gặp mức độ can thiệp của người | route phải tính impact và reversibility của action | 4 · 5 |
| Khi gặp confidence và expected loss | confidence cao không cho phép tự động hóa hành động không thể hoàn tác | 7 · 8 |
| Khi gặp routing theo loại hành động | interrupt phải persist state trước khi chờ | 10 · 11 |
| Khi gặp langgraph interrupt | resume cần idempotency để không lặp side effect | 13 · 15 |
| Khi gặp durable state & resume | approval phải cho reviewer đủ context để quyết định | 17 · 18 |
| Khi gặp approval ux | timeout và escalation là trạng thái nghiệp vụ | 20 · 21 |
| Khi gặp audit, idempotency & timeout | audit log phải ghi ai duyệt gì trên evidence nào | 23 · 24 |
| Khi gặp autonomy ladder & lab | autonomy chỉ tăng sau khi evidence đủ và rollback sẵn sàng | 26 · 28 |

---

<!-- chiron-source-span: {"source_span_id":"28891d30-7484-5f24-b771-a437e59c5df3","locator":{"kind":"html_section","section_id":"gloss","order":18,"heading":"☰ Từ điển thuật ngữ","source_file":"track-3-day-27.html"},"checksum":"65a460a326ef95b5425ff6b539fd7125c95f99282f8a9bbb1cd0e9970143fac6"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"b27f269f-3b96-5cbd-8d47-1bc095d69c0b","locator":{"kind":"html_section","section_id":"bloom","order":19,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-27.html"},"checksum":"da97efa6a714071f7a4fc741a88f364d9166dac81bbe9b016eabe818b95135d5"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 2 · 3 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 4 · 5 · 6 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 7 · 8 · 9 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 10 · 11 · 12 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 13 · 15 · 16 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 17 · 18 · 19 |
