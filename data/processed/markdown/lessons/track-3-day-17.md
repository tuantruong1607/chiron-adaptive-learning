---
schema_version: 1
course_id: rag-intensive
document_id: "57c8dc81-9a0d-517c-82cc-988bdb64a8b6"
document_version_id: "2e28eafc-b896-5fd1-af29-f4b2c6f6d1ea"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Agent Memory & Context Engineering"
source_file: "track-3-day-17.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-17.html"
source_sha256: "362b0947a4d3557eaa9bcfb412304fd65db3e8baef3bec06039d700de357c091"
parser_version: chiron-structured-markdown-v1
html_section_count: 18
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# Agent Memory & Context Engineering

> Thiết kế bộ nhớ theo vòng đời, relevance và privacy thay vì nhét toàn bộ lịch sử vào context.

<!-- chiron-source-span: {"source_span_id":"b76006bc-0bcc-5250-9deb-0f880e122b84","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"track-3-day-17.html"},"checksum":"c375a5eeeed59b8a6a8e936d2970f3389a37036880fd4f1d41557f1f318b5ad8"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: context window không phải memory architecture. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"113a31f3-b846-5de8-9bfa-3b949bb59826","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"track-3-day-17.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

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

<!-- chiron-source-span: {"source_span_id":"7f6c98d5-f897-5c5a-8afc-ce7a884dfa28","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Memory taxonomy","source_file":"track-3-day-17.html"},"checksum":"c7504e33e475e5d71d8d4242f7219f6780a47acb421301abe0e032644e075864"} -->

## 01 Memory taxonomy

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Memory taxonomy · Mental model & quyết định

> Trích slide Slide 1: Memory Systems for Agents AICB-P2T3 · Ngày 17 · Chương 4 — Agent Nâng Cao Giảng viên VinUniversity · Phase 2 · Track 3 · T uần 4

Memory Systems for Agents AICB-P2T3 · Ngày 17 · Chương 4 — Agent Nâng Cao. Điểm nối sang production là: context window không phải memory architecture. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- “Tại sao agent của bạn quên mọi thứ sau mỗi conversation — và làm sao fix nó đúng cách?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

#### Tự kiểm tra · Với memory taxonomy, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là context window không phải memory architecture.

### Slide 2 Memory taxonomy · Evidence & failure lens

> Trích slide Slide 2:? HÃ Y SUY NGHĨ... “Tại sao agent của bạn quên mọi thứ sau mỗi conversation — và làm sao fix nó đúng cách?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

**Đọc như kỹ sư:** “Tại sao agent của bạn quên mọi thứ sau mỗi conversation — và làm sao fix nó đúng cách?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 2 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 3 Memory taxonomy · Evidence & failure lens

> Trích slide Slide 3: Nội dung vận hành 1. Tại sao Agent “quên”? 2. Context Engineering Framework 3. Cognitive Memory Model — 4 loại Memory 4. Implementation Deep-Dive 5. Frameworks chuyên dụng & Privacy 6. Demo & Thực hành Giảng viên (VinUni) AICB · Ngày 17 T uần 4 1 / 19

**Đọc như kỹ sư:** Nội dung vận hành 1. Tại sao Agent “quên”? 2. Context Engineering Framework 3. Cognitive Memory Model — 4 loại Memory 4. Implementation Deep-Dive 5. Frameworks chuyên dụng & Privacy 6. Demo & Thực hành

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 3 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"618da8bb-263d-594d-90af-b9125b4dc946","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Context engineering","source_file":"track-3-day-17.html"},"checksum":"aa176ae3638920303ba63cceb7b5016010e334100b1b17c7d285827e01c5b450"} -->

## 02 Context engineering

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 4 Context engineering · Mental model & quyết định

> Trích slide Slide 4: 01 T ại sao Agent “quên”? Context window có giới hạn — và hầu hết agent không có bộ nhớ ngoài

Context window có giới hạn — và hầu hết agent không có bộ nhớ ngoài. Điểm nối sang production là: ghi mọi thứ làm giảm relevance và tăng privacy risk. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Agent hiện tại — Stateless by default Session 1 LLMcontext Session 2 LLMcontext mới không truyền Mỗi session bắt đầu từ zero
- LLM không có persistent state — mỗi API call là một request độc lập
- User nói “tôi thích Python” ở session 1 → session 2 agent không nhớ

#### Tự kiểm tra · Với context engineering, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là ghi mọi thứ làm giảm relevance và tăng privacy risk.

### Slide 6 Context engineering · Evidence & failure lens

> Trích slide Slide 6: Analogy: Bộ nhớ Agent giống não người Não người Working Memory Long-term Memory consolidation Agent Context Window External Store persist facts tương đương tương đương Context Window = RAM — Nhanh, tạm thời, giới hạn dung lượng ( ∼128K tokens) External Store = Ổ cứng — Chậm hơn, bền vững, gần như vô hạn (Redis, Vector DB)…

**Đọc như kỹ sư:** Analogy: Bộ nhớ Agent giống não người Não người Working Memory Long-term Memory consolidation Agent Context Window External Store persist facts tương đương tương đương Context Window = RAM — Nhanh, tạm thời, giới hạn dung lượng ( ∼128K tokens) External Store =

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 6 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 7 Context engineering · Evidence & failure lens

> Trích slide Slide 7: 02 Context Engineering Frame- work 7 layers of context — quản lý những gì agent “thấy”

**Đọc như kỹ sư:** 02 Context Engineering Frame- work 7 layers of context — quản lý những gì agent “thấy”

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 7 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"a5914f6d-557f-549d-9cd2-f9fd00f03798","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Short-term memory","source_file":"track-3-day-17.html"},"checksum":"b34856b0378ca3f740ad6bc970c7a371fa1193a3f45bb33bdbc75fec9eb34026"} -->

## 03 Short-term memory

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 8 Short-term memory · Mental model & quyết định

> Trích slide Slide 8: 7 Context Layers — Kiến trúc thông tin cho Agent Policy Context — Guardrails, safety rules T ool Context — Function outputs, API responses Retrieval Context — RAG results, documents Memory Context — Recalled facts, episodes User Context — Preferences, history T ask Context — Objective, instructions System Context — Persona,…

Policy context trim cuối cùng (safety không bao giờ bỏ).. Điểm nối sang production là: working memory nên nhỏ và gắn với task hiện tại. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Lưu ý: Conflict resolution: user preference mâu thuẫn policy con- straint → policy luôn thắng.
- T oken Budget — Phân bổ context window 10% Short-term memory 4% Long-term facts 3% Episodic memory 3% Semantic knowledge Phần còn lại dành cho system prompt, task instructions, tool outputs, và out- put generation.
- 03 Cognitive Memory Model — 4 loại Memory Short-term, Long-term, Episodic, Semantic

#### Tự kiểm tra · Với short-term memory, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là working memory nên nhỏ và gắn với task hiện tại.

### Slide 10 Short-term memory · Evidence & failure lens

> Trích slide Slide 10: 03 Cognitive Memory Model — 4 loại Memory Short-term, Long-term, Episodic, Semantic

**Đọc như kỹ sư:** 03 Cognitive Memory Model — 4 loại Memory Short-term, Long-term, Episodic, Semantic

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 10 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 11 Short-term memory · Evidence & failure lens

> Trích slide Slide 11: 4 loại Memory — Cognitive Model cho AI Agents Short-term (Working) Context window buffer Nhanh, tạm thời,∼128K tokens Long-term (Declarative) Redis, PostgreSQL User prefs, facts qua sessions Episodic Log trải nghiệm có thứ tự “Lần trước tôi đã làm gì?” Semantic Embeddings + Vector DB Domain knowledge retrieval Tạm thời Bền…

**Đọc như kỹ sư:** 4 loại Memory — Cognitive Model cho AI Agents Short-term (Working) Context window buffer Nhanh, tạm thời,∼128K tokens Long-term (Declarative) Redis, PostgreSQL User prefs, facts qua sessions Episodic Log trải nghiệm có thứ tự “Lần trước tôi đã làm gì?” Semanti

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 11 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"1d1e410d-bc76-56b8-acaf-d37401898bdd","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Episodic memory","source_file":"track-3-day-17.html"},"checksum":"0ff0a9bc9678aeb6cfe5c72120b7b0801c98fb0f5022079a87c2b343766e47cf"} -->

## 04 Episodic memory

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 12 Episodic memory · Mental model & quyết định

> Trích slide Slide 12: Short-term Memory — Context Window Management Buffer M1 M2 M3 M4 M5 limit! SummarySummary M4 M5 Sliding System Sum. M4 M5 Best! 3 strategies chính: 1. Buffer: giữ tất cả — đơn giản nhưng hit limit sau ∼50 turns 2. Summary: LLM tóm tắt history cũ — ổn định nhưng tốn thêm LLM calls 3. Sliding window: system + summary + last K…

Short-term Memory — Context Window Management Buffer M1 M2 M3 M4 M5 limit!. Điểm nối sang production là: episodic memory lưu trải nghiệm có ích chứ không chép transcript. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Buffer: giữ tất cả — đơn giản nhưng hit limit sau ∼50 turns 2.
- Summary: LLM tóm tắt history cũ — ổn định nhưng tốn thêm LLM calls 3.
- Sliding window: system + summary + last K turns — best tradeoff cho production Short-term memory nên chiếm tối đa 10% context window.

#### Tự kiểm tra · Với episodic memory, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là episodic memory lưu trải nghiệm có ích chứ không chép transcript.

### Slide 14 Episodic memory · Evidence & failure lens

> Trích slide Slide 14: Memory Management Flow — Buffer → Summarize → Store 1. Buffer (Context Window) 2. Summarize (LLM call) 3. Extract (Key facts) 4. Persist (External store) Redis long-term facts Chroma semantic embeddings Trigger: token count>threshold Chỉ persist sau task completion — không write giữa chừng để tránh inconsistent state Lưu ý:…

**Đọc như kỹ sư:** Memory Management Flow — Buffer → Summarize → Store 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 14 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 15 Episodic memory · Evidence & failure lens

> Trích slide Slide 15: 04 Implementation Deep-Dive Code-level: LangGraph nodes cho mỗi memory type

**Đọc như kỹ sư:** 04 Implementation Deep-Dive Code-level: LangGraph nodes cho mỗi memory type

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 15 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"f147331c-53e1-5084-8cc1-fc50fc4a4cf5","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 Semantic memory","source_file":"track-3-day-17.html"},"checksum":"8224fe5eadc47dda11f8625c0a5a7732b3e0a3a569b910d97d97e7672e69b132"} -->

## 05 Semantic memory

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 16 Semantic memory · Mental model & quyết định

> Trích slide Slide 16: LangGraph Memory State — Code-Level class MemoryState(TypedDict): messages: list[BaseMessage] user_profile: dict # long-term episodes: list[dict] # episodic semantic_hits: list[str] # semantic memory_budget: int # tokens left # Memory router: ọchn ạloi phù ợhp def retrieve_memory(state): query = state[ "messages"][-1].content…

Node load_memory: đọc 3 loại memory khi bắt đầu 2.. Điểm nối sang production là: semantic memory cần provenance và cơ chế sửa. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Episodic Memory — Learning từ Past Trajectories Task: debug API Trajectory: tried X, Y Outcome: Y worked Reflection: X fails vì...
- New similar task similarity search Lưu tuple mỗi episode
- Agent biết: “approach X đã fail vì Y trong task tương tự” LRU: xóa episode ít dùng nhất Importance decay: score giảm theo thời gian Consolidation: merge episodes tương tự Voyager-style: extract reusable strategy → skill li- brary

#### Tự kiểm tra · Với semantic memory, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là semantic memory cần provenance và cơ chế sửa.

### Slide 17 Semantic memory · Evidence & failure lens

> Trích slide Slide 17: Episodic Memory — Learning từ Past Trajectories Task: debug API Trajectory: tried X, Y Outcome: Y worked Reflection: X fails vì... New similar task similarity search Lưu tuple mỗi episode: ■ (task, trajectory, outcome, reflection) ■ Agent biết: “approach X đã fail vì Y trong task tương tự” LRU: xóa episode ít dùng nhất…

**Đọc như kỹ sư:** Episodic Memory — Learning từ Past Trajectories Task: debug API Trajectory: tried X, Y Outcome: Y worked Reflection: X fails vì...

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- New similar task similarity search Lưu tuple mỗi episode
- Agent biết: “approach X đã fail vì Y trong task tương tự” LRU: xóa episode ít dùng nhất Importance decay: score giảm theo thời gian Consolidation: merge episodes tương tự Voyager-style: extract reusable strategy → skill li- brary

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 17 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 18 Semantic memory · Evidence & failure lens

> Trích slide Slide 18: Semantic Memory — Vector DB cho Knowledge Retrieval Domain Docs Embed Chroma DB Agent Query T op-K vectors cosine sim ■ Encode domain knowledge → embeddings → Chroma/Pinecone ■ Query = task description → cosine similarity → top-k chunks ■ Agent discover facts mới → add vào DB với metadata (source, confidence, timestamp) Agent…

**Đọc như kỹ sư:** Semantic Memory — Vector DB cho Knowledge Retrieval Domain Docs Embed Chroma DB Agent Query T op-K vectors cosine sim

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Encode domain knowledge → embeddings → Chroma/Pinecone
- Query = task description → cosine similarity → top-k chunks
- Agent discover facts mới → add vào DB với metadata (source, confidence, timestamp) Agent tự mở rộng knowledge base qua interactions — incremental knowledge growth

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 18 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"49d3d4f9-c25e-5e9a-b734-311ec20371f6","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Retrieval, decay & consolidation","source_file":"track-3-day-17.html"},"checksum":"3170c8a4e09c05c206ec4ba4f0bdfab439cd704cd34f4204f5860c37b82b4053"} -->

## 06 Retrieval, decay & consolidation

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 19 Retrieval, decay & consolidation · Mental model & quyết định

> Trích slide Slide 19: Memory Architecture — Combining All 4 Types Agent retrieve(query) Short-term Long-term Episodic Semantic priority 1 priority 2 priority 3 priority 4 Merged context→LLM Lưu ý: Unified interface: retrieve(query, types=["all"]) trả về merged con- text từ cả 4 loại memory, đã trim theo token budget. Giảng viên (VinUni) AICB · Ngày…

05 Frameworks chuyên dụng & Privacy Mem0, Zep — và khi nào dùng framework có sẵn. Điểm nối sang production là: retrieval nên kết hợp relevance, recency và importance. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Claim: 90% token reduction, 91% faster retrieval
- Entity extraction + progressive summarization
- Multi-level summaries: turn → session → cross-session

#### Tự kiểm tra · Với retrieval, decay & consolidation, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là retrieval nên kết hợp relevance, recency và importance.

### Slide 21 Retrieval, decay & consolidation · Evidence & failure lens

> Trích slide Slide 21: Mem0 & Zep — Managed Memory Layers ■ Auto-classify memory types ■ Smart retrieval: relevance + recency ranking ■ Claim: 90% token reduction, 91% faster retrieval ■ API-first, nhanh go-to-market ■ Entity extraction + progressive summarization ■ T ự build user knowledge graph qua sessions ■ Multi-level summaries: turn → session…

**Đọc như kỹ sư:** Claim: 90% token reduction, 91% faster retrieval

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Entity extraction + progressive summarization
- Multi-level summaries: turn → session → cross-session
- Giảm context size tối ưu Tiêu chí Mem0 / Zep Custom (Redis + Chroma) Setup time Nhanh (API) Chậm (build from scratch) Control Hạn chế Full control Khi nào dùng MVP, go-to-market Production, đặc thù domain

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 21 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 22 Retrieval, decay & consolidation · Evidence & failure lens

> Trích slide Slide 22: Quyền riêng tư, Bảo mật & GDPR Privacy-by-Design — Mặc định không lưu PII. User phải explicit opt-in trước khi agent ghi nhớ thông tin cá nhân. Right to be Forgotten — User yêu cầu xóa → xóa tất cả memory en- tries liên quan → confirm deletion. Lưu ý: Federated Forgetting: trong multi-agent system, dele- tion request phải…

**Đọc như kỹ sư:** Quyền riêng tư, Bảo mật & GDPR Privacy-by-Design — Mặc định không lưu PII.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- User phải explicit opt-in trước khi agent ghi nhớ thông tin cá nhân.
- Right to be Forgotten — User yêu cầu xóa → xóa tất cả memory en- tries liên quan → confirm deletion.
- Lưu ý: Federated Forgetting: trong multi-agent system, dele- tion request phải propagate đến tất cả agents có copy.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 22 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"3be74152-a17b-5631-ad6c-fb1567225e9a","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Redis và persistence","source_file":"track-3-day-17.html"},"checksum":"b31f03be8628a20f86d41e32a4aae7f31bab7df5b07768569a8bdd703b117204"} -->

## 07 Redis và persistence

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 23 Redis và persistence · Mental model & quyết định

> Trích slide Slide 23: 06 Demo & Thực hành Xem agent nhớ user preferences qua 3 sessions

06 Demo & Thực hành Xem agent nhớ user preferences qua 3 sessions. Điểm nối sang production là: memory phải có vòng đời create–retrieve–update–delete. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Session 1: User nói “tôi thích Python, không thích Java” → agent ghi vào Redis 2.
- Session 2 (new process): Agent load memory → proactively suggest Python solution mà không cần hỏi lại 3.
- Session 3: Agent recall episode “user bị confused async/await” → tự thêm explanation 4.

#### Tự kiểm tra · Với redis và persistence, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là memory phải có vòng đời create–retrieve–update–delete.

### Slide 25 Redis và persistence · Evidence & failure lens

> Trích slide Slide 25: Lab #17 Mục tiêu: Build Multi-Memory Agent với LangGraph Deliverable: Agent với full memory stack + benchmark report: so sánh agent có/không memory trên 10 multi-turn conversations Thời gian: 2 giờ Giảng viên (VinUni) AICB · Ngày 17 T uần 4 17 / 19

**Đọc như kỹ sư:** Lab #17 Mục tiêu: Build Multi-Memory Agent với LangGraph Deliverable: Agent với full memory stack + benchmark report: so sánh agent có/không memory trên 10 multi-turn conversations Thời gian: 2 giờ

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 25 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 26 Redis và persistence · Evidence & failure lens

> Trích slide Slide 26: Lab 17 — Các bước thực hành 1. Implement 4 memory backends: ConversationBufferMemory (short-term), Redis (long-term), JSON episodic log, Chroma (semantic) 2. Build memory router: chọn memory type phù hợp dựa trên query intent — user preference vs factual recall vs experience recall 3. Context window management: auto-trim khi…

**Đọc như kỹ sư:** Implement 4 memory backends: ConversationBufferMemory (short-term), Redis (long-term), JSON episodic log, Chroma (semantic) 2.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Build memory router: chọn memory type phù hợp dựa trên query intent — user preference vs factual recall vs experience recall 3.
- Context window management: auto-trim khi gần limit, priority-based eviction theo 4-level hierarchy 4.
- Benchmark: so sánh agent có/không memory trên 10 multi-turn conversations — đo response relevance, context utilization, token efficiency GitHub repo + benchmark report: bảng so sánh metrics, memory hit rate anal- ysis, token budget breakdown

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 26 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"c720524f-feb7-5780-b72a-7965dd633a70","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Privacy, deletion & Lab","source_file":"track-3-day-17.html"},"checksum":"c5c846bebb2903608e9d6b140a14eae288a5d2f835d043b54549135d9876db53"} -->

## 08 Privacy, deletion & Lab

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 27 Privacy, deletion & Lab · Mental model & quyết định

> Trích slide Slide 27: T ổng kết — Key T akeaways Những ý chính cần nhớ sau buổi học hôm nay 1 Không có “one size fits all” — production agent cần ít nhất short-term + long-term, thêm episodic/semantic tùy use case 2 Memory retrieval quality quyết định agent quality — bad retrieval = irrelevant context = wrong answer 3 Memory write-back cần careful…

Tiếp theo & Bài tập Ngày 18: Production RAG “Agent đã có memory, tiếp theo cần knowledge retrieval tốt hơn — tại sao RAG pipeline demo chạy tốt nhưng production chỉ đạt 60%?”. Điểm nối sang production là: xóa dữ liệu phải lan tới index và cache.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Hoàn thành Lab 17: Multi-Memory Agent + benchmark
- Đọc: Anthropic “Building Effective Agents” (mục Context Engineering)
- Hỏi & Đáp Memory nào là “must-have” cho production agent?

#### Tự kiểm tra · Với privacy, deletion & lab, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là xóa dữ liệu phải lan tới index và cache.

### Slide 29 Privacy, deletion & Lab · Evidence & failure lens

> Trích slide Slide 29: Hỏi & Đáp Memory nào là “must-have” cho production agent? Khi nào thì dùng framework (Mem0, Zep) vs tự build?

**Đọc như kỹ sư:** Hỏi & Đáp Memory nào là “must-have” cho production agent?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Khi nào thì dùng framework (Mem0, Zep) vs tự build?

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 29 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 30 Privacy, deletion & Lab · Evidence & failure lens

> Trích slide Slide 30: Cảm ơn! AICB-P2T3 · Ngày 17 · Memory Systems for Agents github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn

**Đọc như kỹ sư:** AICB-P2T3 · Ngày 17 · Memory Systems for Agents github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 30 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"3c59ecdd-f63d-50a3-b264-472f39a8c413","locator":{"kind":"html_section","section_id":"ladder","order":11,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"track-3-day-17.html"},"checksum":"9233ec132eb0392a18d533d68b60aa3ae8c1c326e9e0ad8dd3d405f13ce6d29a"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của Memory architecture bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"40118128-07af-50be-a110-f9575c7da508","locator":{"kind":"html_section","section_id":"section-012","order":12,"heading":"∑ Phòng mô phỏng quyết định","source_file":"track-3-day-17.html"},"checksum":"cfd442d2c9cd97ad0c9847903a1f6d936c460ee3516ccbeac2c48452e79f6fe9"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Context budget — ký ức nào được quyền vào prompt?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Context window:**: min `8`, max `256`, step `8`, default `64`

- **Control - Recent turns:**: min `0`, max `100`, step `5`, default `35`

- **Control - Semantic facts:**: min `0`, max `100`, step `5`, default `30`

- **Control - Episodes:**: min `0`, max `100`, step `5`, default `20`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Memory retrieval — relevance, tuổi và importance

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Relevance:**: min `0`, max `100`, step `1`, default `82`

- **Control - Tuổi ký ức:**: min `0`, max `180`, step `1`, default `14`

- **Control - Importance:**: min `0`, max `100`, step `1`, default `70`

- **Control - Half-life:**: min `1`, max `180`, step `1`, default `30`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Retention — tiện ích đổi lấy privacy exposure

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Người dùng:**: min `100`, max `100000`, step `100`, default `10000`

- **Control - Memory/user/ngày:**: min `1`, max `50`, step `1`, default `8`

- **Control - Retention:**: min `1`, max `365`, step `1`, default `90`

- **Control - Có PII:**: min `0`, max `100`, step `1`, default `12`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"3ddd5aea-c9b3-5328-9161-8d15aff5184c","locator":{"kind":"html_section","section_id":"misc","order":13,"heading":"✕ Hiểu lầm phổ biến","source_file":"track-3-day-17.html"},"checksum":"05ea7250df2b6f935f213cce89d2320074ffc2918df2cbe34ed9498d5c24a514"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai memory taxonomy là phần còn lại tự động an toàn và ổn định.

Sửa lại Context window không phải memory architecture.

Vì sao quan trọng · slide 1 · 2 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai context engineering là phần còn lại tự động an toàn và ổn định.

Sửa lại Ghi mọi thứ làm giảm relevance và tăng privacy risk.

Vì sao quan trọng · slide 4 · 6 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai short-term memory là phần còn lại tự động an toàn và ổn định.

Sửa lại Working memory nên nhỏ và gắn với task hiện tại.

Vì sao quan trọng · slide 8 · 10 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai episodic memory là phần còn lại tự động an toàn và ổn định.

Sửa lại Episodic memory lưu trải nghiệm có ích chứ không chép transcript.

Vì sao quan trọng · slide 12 · 14 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai semantic memory là phần còn lại tự động an toàn và ổn định.

Sửa lại Semantic memory cần provenance và cơ chế sửa.

Vì sao quan trọng · slide 16 · 17 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai retrieval, decay & consolidation là phần còn lại tự động an toàn và ổn định.

Sửa lại Retrieval nên kết hợp relevance, recency và importance.

Vì sao quan trọng · slide 19 · 21 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"0e21511e-b60f-5d57-b81c-939e94234a36","locator":{"kind":"html_section","section_id":"apply","order":14,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"track-3-day-17.html"},"checksum":"23ce75e0c9a5f3a219f87c3be29391579ab08e080b4219f8a1facb2b3c049b29"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI phải nhớ preference hữu ích nhưng quên PII đúng hạn và không để ký ức cũ lấn át yêu cầu mới.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Memory taxonomy | Context window không phải memory architecture. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 2 |
| Context engineering | Ghi mọi thứ làm giảm relevance và tăng privacy risk. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 4 · 6 |
| Short-term memory | Working memory nên nhỏ và gắn với task hiện tại. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 8 · 10 |
| Episodic memory | Episodic memory lưu trải nghiệm có ích chứ không chép transcript. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 12 · 14 |
| Semantic memory | Semantic memory cần provenance và cơ chế sửa. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 16 · 17 |
| Retrieval, decay & consolidation | Retrieval nên kết hợp relevance, recency và importance. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 19 · 21 |
| Redis và persistence | Memory phải có vòng đời create–retrieve–update–delete. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 23 · 25 |
| Privacy, deletion & Lab | Xóa dữ liệu phải lan tới index và cache. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 27 · 29 |

---

<!-- chiron-source-span: {"source_span_id":"f23c5134-b52e-5514-8df7-5b5a0847bb0e","locator":{"kind":"html_section","section_id":"numbers","order":15,"heading":"# Con số cần kiểm chứng","source_file":"track-3-day-17.html"},"checksum":"43e7ee4771a3d7e8d3a549c50a2af843b0eacf8075c0365aed2be29dd11fd95c"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 1 k | ent không nhớ ■ Conversation dài >50 turns → hit context limit Lưu ý: Đây là vấn đề #1 khi de- ploy agent thực tế: user kỳ vọng agent “nhớ” — nhưng nó không. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 5 |
| 128K | ơng đương tương đương Context Window = RAM — Nhanh, tạm thời, giới hạn dung lượng ( ∼128K tokens) External Store = Ổ cứng — Chậm hơn, bền vững, gần như vô hạn (Redis, Vector DB) Agent cần cả hai: fast access cho conversa- tion hiện tại + p | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 6 |
| 10% | T oken Budget — Phân bổ context window 10% Short-term memory 4% Long-term facts 3% Episodic memory 3% Semantic knowledge Phần còn lại dành cho system prompt, task instructions, tool outputs, v | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 4% | T oken Budget — Phân bổ context window 10% Short-term memory 4% Long-term facts 3% Episodic memory 3% Semantic knowledge Phần còn lại dành cho system prompt, task instructions, tool outputs, và out- put generation | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 3% | T oken Budget — Phân bổ context window 10% Short-term memory 4% Long-term facts 3% Episodic memory 3% Semantic knowledge Phần còn lại dành cho system prompt, task instructions, tool outputs, và out- put generation. Vượt 20% → contex | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 20% | ành cho system prompt, task instructions, tool outputs, và out- put generation. Vượt 20% → context bị nhiễu, accuracy giảm. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 4 M | ry) Short-term Long-term Episodic Semantic priority 1 priority 2 priority 3 priority 4 Merged context→LLM Lưu ý: Unified interface: retrieve(query, types=["all"]) trả về merged con- text từ cả 4 loại memory, đã trim theo token budget. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 19 |
| 90% | ■ Auto-classify memory types ■ Smart retrieval: relevance + recency ranking ■ Claim: 90% token reduction, 91% faster retrieval ■ API-first, nhanh go-to-market ■ Entity extraction + progressive summarization ■ T ự build user knowledge grap | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 21 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"5c7f0ea0-89f2-5417-8ca8-9e84af0a77b6","locator":{"kind":"html_section","section_id":"cheat","order":16,"heading":"▣ Cheat sheet ôn thi","source_file":"track-3-day-17.html"},"checksum":"299b719a068217b0cef5188623fc4c375dbd8590b3d730fb3168c8c43d073215"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp memory taxonomy | context window không phải memory architecture | 1 · 2 |
| Khi gặp context engineering | ghi mọi thứ làm giảm relevance và tăng privacy risk | 4 · 6 |
| Khi gặp short-term memory | working memory nên nhỏ và gắn với task hiện tại | 8 · 10 |
| Khi gặp episodic memory | episodic memory lưu trải nghiệm có ích chứ không chép transcript | 12 · 14 |
| Khi gặp semantic memory | semantic memory cần provenance và cơ chế sửa | 16 · 17 |
| Khi gặp retrieval, decay & consolidation | retrieval nên kết hợp relevance, recency và importance | 19 · 21 |
| Khi gặp redis và persistence | memory phải có vòng đời create–retrieve–update–delete | 23 · 25 |
| Khi gặp privacy, deletion & lab | xóa dữ liệu phải lan tới index và cache | 27 · 29 |
| Khi gặp memory taxonomy | PII không được vào long-term memory theo mặc định | 1 · 2 |

---

<!-- chiron-source-span: {"source_span_id":"3da4d675-82ac-5903-8d6d-77b0cd4f598b","locator":{"kind":"html_section","section_id":"gloss","order":17,"heading":"☰ Từ điển thuật ngữ","source_file":"track-3-day-17.html"},"checksum":"9f53ef4ae0175c17470e20a42af348f694ecf4135f05b0daec0dcaa43374e6b4"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"9759b183-33cc-542c-86e5-28d48da260e1","locator":{"kind":"html_section","section_id":"bloom","order":18,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-17.html"},"checksum":"812717fee80f20fd20612dabd98f85de158911fed860aba3a2c11930b408bbbc"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 2 · 3 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 4 · 6 · 7 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 8 · 10 · 11 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 12 · 14 · 15 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 16 · 17 · 18 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 19 · 21 · 22 |
