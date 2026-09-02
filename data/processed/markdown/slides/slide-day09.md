---
schema_version: 1
course_id: rag-intensive
document_id: "c693fc4d-eb6a-56ba-9984-c848cd33a11d"
document_version_id: "02b50fbe-cd01-5731-a653-784ba06f4d37"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Multi-Agent & Kết Nối Hệ Thống"
source_file: "slide day09.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\slide day09.pdf"
source_sha256: "17863682e739e7b2e2cdbdb8f5f0b0353a3434fe2ecad929385c82324f8026d4"
parser_version: chiron-structured-markdown-v1
page_count: 85
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":85}"
language: vi
---

# Multi-Agent & Kết Nối Hệ Thống

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"ac41299d-4a02-52df-a2b0-e9f15a76c602","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Multi-Agent & Kết Nối Hệ Thống","extraction_method":"pdf-text-layer"},"checksum":"da94a0e9460699cf9387f1b08bcfaa7b8024713b24e4154cb49a890189f8afb6"} -->

## Slide 1 - Multi-Agent & Kết Nối Hệ Thống

AICB-P1 · Ngày 9 · MCP, A2A & LangGraph T ên Giảng Viên VinUniversity · Phase 1 · T uần 2 · 2026

---

<!-- chiron-source-span: {"source_span_id":"59c0251b-1dc0-558f-a0b2-ee0ab2bfc822","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"a8cbb717d1fc79506a0fb33078c733c0c8c1509a000df7497aec478bc0244258"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Bạn có 1 agent rất giỏi. Nhưng bài toán đã quá lớn cho 1 agent. Làm thế nào để hệ thống vẫn rõ vai trò, dễ kiểm soát, và dễ mở rộng?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"46b32a5e-37ce-5a6e-ba2d-81253b988838","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Lộ Trình 9 Ngày Đã Đi Đến Đây","extraction_method":"pdf-text-layer"},"checksum":"f326ce096bdc59f1934b38710606171b1d298e5408c7e0b91b4782ea6326b649"} -->

## Slide 3 - Lộ Trình 9 Ngày Đã Đi Đến Đây

D1 D2 D3 D4 D5 D6 D7 D8 D9 LLM foundation Bài toán kinh doanh Agentic ReAct Prompt & tool calling Product thinking Project management Embedding vector store RAG pipeline Multi-Agent MCP · A2A Vị trí hôm nay Day 08 đã dạy cáchlấy đúng thông tin. Day 09 hỏi câu tiếp theo: khi bài toán lớn hơn một agent, ta tổ chức hệ thống như thế nào? Giảng viên (VinUni) AICB · Ngày 9 T uần 2 1 / 70

---

<!-- chiron-source-span: {"source_span_id":"14a6b147-bc30-512c-afed-6a23687d1456","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"88a8bcc4676d463b27cf11f5c7eba519118bc6e12e059253a0fd4e6058c553b3"} -->

## Slide 4 - Nội Dung Bài Học

1. Giới hạn của single-agent

2. Mental model: tư duy hệ thống

3. Multi-agent patterns

4. Supervisor-worker deep dive

5. MCP — chuẩn kết nối tool

6. A2A — giao tiếp giữa agents

7. Orchestration với LangGraph

8. Observability & debugging

9. Cost, latency & reliability

10. Kế hoạch học tập Ngày 9

11. Lab 9 + deliverable Giảng viên (VinUni) AICB · Ngày 9 T uần 2 2 / 70

---

<!-- chiron-source-span: {"source_span_id":"2c5b6770-4f64-5794-9e6a-835775f73f4b","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Mục Tiêu Ngày 9","extraction_method":"pdf-text-layer"},"checksum":"ff97674f0bef682589214f2f465f8c3af2c34667ccf0eb005bd1fcef259b2df7"} -->

## Slide 5 - Mục Tiêu Ngày 9

- Giải thích được vì sao single-agent bắt đầu quá tải khi bài toán cần nhiều vai trò và
nhiều nguồn lực

- Phân biệt được các pattern supervisor-worker, pipeline, debate, và hierarchical —
và biết chọn đúng pattern

- Hiểu MCP là chuẩn nối agent với tool / service bên ngoài, và A2A là cách agents
giao việc cho nhau với message contract rõ

- Dùng LangGraph để hình dung graph, state, và conditional routing trong hệ
multi-agent

- Thiết kế được trace & observability để debug và cải thiện hệ thống

- Nâng cấp artifact Day 08 thành hệ thống Supervisor + Workers có trace rõ ràng
Giảng viên (VinUni) AICB · Ngày 9 T uần 2 3 / 70

---

<!-- chiron-source-span: {"source_span_id":"cbacf161-249c-5ce9-979b-6c01fea25a03","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"8e6912aa7c171a958eb9913ec1e90be5b10e3f4fb9897370f8036d2752c08ad1"} -->

## Slide 6 - Deliverable Cuối Ngày

Artifact pack cần nộp Bản nâng cấp từ Day 08 gồm supervisor, 2–3 workers, 1 kết nối tool qua MCP, và trace log cho toàn bộ luồng phối hợp

- 1 supervisor nhận task, route đúng worker, và tổng hợp kết quả

- 2–3 worker chuyên vai trò như retrieval, tool use, synthesis

- 1 kết nối external capability qua MCP

- 1 trace dễ đọc để giải thích agent nào đã làm gì và khi nào
Giảng viên (VinUni) AICB · Ngày 9 T uần 2 4 / 70

---

<!-- chiron-source-span: {"source_span_id":"d9cabb04-3794-57ad-ac55-ef7431d0a3f3","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Từ Single-Agent Sang Multi","extraction_method":"pdf-text-layer"},"checksum":"11d28f5ea64e65eed2484f6522e66698e62437776b29ae37aaf3a0b78c297cf0"} -->

## Slide 7 - Từ Single-Agent Sang Multi

01 Từ Single-Agent Sang Multi- Agent Day 08 giúp agent biết retrieve và trả lời grounded; Day 09 trả lời câu hỏi khi nào một agent không còn đủ để gánh toàn bộ bài toán

---

<!-- chiron-source-span: {"source_span_id":"a20dea9c-163a-5e74-ba4a-f26538e3d616","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Từ Artifact Day 08 Sang Bài T oán Lớn Hơn","extraction_method":"pdf-text-layer"},"checksum":"d908adce4b83baee8d10a07c0c672c820de164e1555c0c7f4b5232223504123a"} -->

## Slide 8 - Từ Artifact Day 08 Sang Bài T oán Lớn Hơn

Day 08 đã làm được

- retrieve đúng tài liệu hơn

- rerank hoặc lọc context tốt hơn

- generate câu trả lời grounded hơn
Nhưng khi hệ thống lớn lên

- phải phân tích task trước khi
retrieve

- phải gọi thêm tool ngoài

- phải chia việc và tổng hợp nhiều
kết quả

- phải theo dõi trace để debug
Thông điệp mở bài Day 09 không phủ định Day 08. Nó là bước tiếp theo: biến một agent có RAG thành một hệ thống có vai trò, có phối hợp, và có điểm mở rộng rõ ràng. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 5 / 70

---

<!-- chiron-source-span: {"source_span_id":"113262f8-dd02-5e92-811f-0d04a1e9a11d","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Khi Một Agent Bắt Đầu Quá T ải","extraction_method":"pdf-text-layer"},"checksum":"267d21f72dc9265d1c6773429e7a0cc92e6e7586b6fcf405c8ea7d5d7aba43d6"} -->

## Slide 9 - Khi Một Agent Bắt Đầu Quá T ải

Một Agent Plan task Retrieve Call tools Synthesize Monitor + retry Một nơi phải làm quá nhiều việc sẽ khó tối ưu, khó debug, và khó scale. Lưu ý: Câu hỏi đúng không còn là “agent có đủ thông minh không?” mà là “ta có đang ép một agent gánh quá nhiều vai trò không?” Giảng viên (VinUni) AICB · Ngày 9 T uần 2 6 / 70

---

<!-- chiron-source-span: {"source_span_id":"3c437620-ad5a-54a2-9627-2225c8c75482","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"4 Giới Hạn Cốt Lõi Của Single-Agent","extraction_method":"pdf-text-layer"},"checksum":"278b5aa2f5f91ebf245dccf742e7fb3d59a4f4cf0e3351d523c5e06c2e9016ff"} -->

## Slide 10 - 4 Giới Hạn Cốt Lõi Của Single-Agent

1. Context bottleneck Một agent phải giữ quá nhiều mục tiêu, tool outputs, evidence, và state trong cùng một lần suy luận. Context window có giới hạn cứng.

2. Specialization trade-off Agent càng ôm nhiều vai, prompt càng dài và khó ổn định. Giỏi đều mọi thứ thường đồng nghĩa với không thật sự giỏi vai nào.

3. Parallelism hạn chế Một agent thường chạy tuần tự. Khi có nhiều việc độc lập, hệ thống vẫn phải chờ từng bước nối nhau — tăng latency không cần thiết.

4. Reliability yếu Nếu agent chọn sai tool hoặc hiểu sai task ở đầu luồng, toàn bộ hệ thống dễ đi lệch theo. Không có isolation để khoanh vùng lỗi. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 7 / 70

---

<!-- chiron-source-span: {"source_span_id":"2a357b6a-8151-53c8-a94f-bb76c15818db","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Thực T ế: Context Window Bottleneck Trông Như Thế Nào?","extraction_method":"pdf-text-layer"},"checksum":"3c9997f931d2a6371d0b6a38ccec8317572740d9bf0d32d1e0e223a4005266e5"} -->

## Slide 11 - Thực T ế: Context Window Bottleneck Trông Như Thế Nào?

Kịch bản thực tế

- Agent nhận task: phân tích hợp đồng 80
trang + tra cứu luật + tóm tắt rủi ro

- Tool call trả về 12.000 tokens

- Chat history đã chiếm 6.000 tokens

- Prompt gốc: 3.000 tokens

- Còn lại cho reasoning: ≈ 3.000 tokens
Dấu hiệu nhận biết

- câu trả lời thiếu thông tin ở giữa
document

- agent lặp lại bước đã làm

- reasoning ngắn bất thường ở
bước cuối

- tool call với empty context
Lưu ý: Agent bắt đầu “quên” phần đầu tài liệu khi xử lý phần cuối — lost-in- the-middle problem. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 8 / 70

---

<!-- chiron-source-span: {"source_span_id":"8fa40c51-3244-51f4-a047-0f604a40c869","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Dấu Hiệu Nên Nghĩ T ới Multi-Agent","extraction_method":"pdf-text-layer"},"checksum":"f90f4796b4dd93d4f2f2db1240b7079a23ec5087e7fb2a79881c1e334aecaead"} -->

## Slide 12 - Dấu Hiệu Nên Nghĩ T ới Multi-Agent

- ✓ T ask có nhiều bước vai trò khác nhau: plan, retrieve, tool use, tổng hợp

- ✓ Có thể chia việc độc lập: 2 worker làm song song vẫn hợp lý

- ✓ Cần debug rõ ai làm sai: route sai, retrieve sai, hay synthesis sai

- ✓ Cần mở rộng dần: thêm 1 worker mới mà không viết lại cả prompt gốc

- ✓ Context window một agent không đủ: tài liệu lớn, nhiều tool output

- Đừng dùng multi-agent chỉ vì thấy “ngầu”. Nếu 1 workflow đơn giản đã
đủ, giữ đơn giản sẽ rẻ và ổn định hơn Giảng viên (VinUni) AICB · Ngày 9 T uần 2 9 / 70

---

<!-- chiron-source-span: {"source_span_id":"043ae0c6-5475-5b96-a15e-d05a40169bbc","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Mental Model: Tư Duy Hệ","extraction_method":"pdf-text-layer"},"checksum":"c9a90b969da2980c00ee7327fb548d5cd258096b990f5335601c1f7179c11d16"} -->

## Slide 13 - Mental Model: Tư Duy Hệ

02 Thống Trước Khi Thiết Kế Trước khi chọn pattern hay tool, cần hình thành tư duy đúng về cách chia trách nhiệm trong một hệ thống phức tạp

---

<!-- chiron-source-span: {"source_span_id":"d7133059-cf53-504d-9bfd-879b5777a446","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Từ “Agent Thông Minh” Sang “Hệ Thống Rõ Ràng”","extraction_method":"pdf-text-layer"},"checksum":"30db93801766540cf175f2104fba50aa891a59565a61b3f2d4b9116cd6a8ecc8"} -->

## Slide 14 - Từ “Agent Thông Minh” Sang “Hệ Thống Rõ Ràng”

Tư duy cũ

- Làm thế nào để agent thông minh hơn?

- Prompt nào khiến agent làm được nhiều
hơn?

- Thêm nhiều tool cho một agent để đủ
sức Lưu ý: T ư duy này dẫn đến “god agent” — một agent làm hết nhưng không ai hiểu nó đang làm gì. Tư duy hệ thống

- Task này gồm bao nhiêu loại trách
nhiệm khác nhau?

- Ai cần biết gì, khi nào?

- Lỗi cần được khoanh vùng ở đâu?

- Điểm nào cần human oversight?
Kết quả Hệ thống clear về vai trò, dễ test từng phần, và dễ cải thiện dần. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 10 / 70

---

<!-- chiron-source-span: {"source_span_id":"cf169a0a-a238-5169-9c9e-7bd23040e4f6","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Ba Câu Hỏi Thiết Kế Trước Khi Viết Code","extraction_method":"pdf-text-layer"},"checksum":"2fce6e93be15e9a237f27abf95c8bb0b9695104461df341a932ec6b39a55eda3"} -->

## Slide 15 - Ba Câu Hỏi Thiết Kế Trước Khi Viết Code

Câu hỏi 1 — Chia trách nhiệm ở đâu? Task nào cần reason- ing? Task nào cần data fetching? Task nào chỉ cần format? Câu hỏi 2 — Thông tin đi theo con đường nào? Agent nào cần biết gì? Ai cần đầu ra của ai trước tiên? Câu hỏi 3 — Lỗi ở đâu là ít tổn hại nhất? Thiết kế để lỗi tại worker không làm hỏng toàn bộ hệ thống. Nguyên tắc Thiết kế tốt giúp lỗi có địa chỉ rõ ràng thay vì lan ra cả hệ thống. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 11 / 70

---

<!-- chiron-source-span: {"source_span_id":"06476cc4-3107-57d1-86b7-196d6c5b654f","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Mini-Quest 1: Single Hay Multi-Agent?","extraction_method":"pdf-text-layer"},"checksum":"2566ebf1053bcab1f0d95c128748981df0d1ed56b65013f113db8f2a57eb9e95"} -->

## Slide 16 - Mini-Quest 1: Single Hay Multi-Agent?

MINI-QUEST 1 20 phút · cá nhân hoặc cặp · làm trực tiếp trên máy Phần A — Điều tra (8’) Chọn công cụ bạn dùng hằng ngày: Claude Code, Codex, Antigravity, OpenCode, Cursor...

### Tìm bằng chứng ngay trong máy, không đoán

- có cơ chế gọi agent con không? gọi là gì?

- agent con có context riêng hay dùng
chung?

- chạy song song được mấy cái?

- có giới hạn tool cho từng agent được
không?

- tool ngoài nối vào bằng đường nào?
Phần B — Tự tạo 1 agent (10’) Viết một agent con cho chính công cụ bạn đang dùng, rồi chạy thử một lần thật.

### Ba ràng buộc

- một vai trò hẹp — không phải trợ lý đa
năng

- mô tả rõ khi nào được gọi — đây chính
là tín hiệu route cho supervisor

- cắt bớt tool nó được phép dùng
Mồi sẵn: repo môn học đã có.claude/agents/*.md và.codex/agents/*.toml — cùng 5 agent, hai schema khác nhau. Mở đọc trước khi tự viết. · 2’ cuối: 2 bạn chia sẻ kết luận + bằng chứng. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 12 / 70

---

<!-- chiron-source-span: {"source_span_id":"20900a56-0d09-57c5-a826-0a1dac6eebcd","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Debrief Quest 1: Đọc Một Harness Bằng Từ Vựng Day 09","extraction_method":"pdf-text-layer"},"checksum":"51bf0b7ae60eb2f70c128d1f28241c9e71f8bd1a4348494d25e9680628f1bdb2"} -->

## Slide 17 - Debrief Quest 1: Đọc Một Harness Bằng Từ Vựng Day 09

Thứ bạn thấy trong công cụ Khái niệm Day 09 Bằng chứng trong repo môn học Vòng lặp chính nhận yêu cầu rồi quyết định gọi ai Supervisor phiên chat gốc của Claude Code / Codex .claude/agents/*.md, .codex/agents/*.toml Định nghĩa Worker 5 agent: slide-reviewer, lab-smoke-tester, vn-content-reviewer... Dòng description: "use when^^." Tín hiệu routing supervisor đọc đúng dòng này để chọn worker Dòng tools: Trust boundary / least privilege vn-content-reviewer chỉ có Read, Grep, Glob — không có Write, nên không thể sửa deck Agent con có context window riêng Chống context bottleneck lý do thật sự để tách worker — không phải vì “ngầu” max_threads = 6 Parallelism.codex/config.toml max_depth = 1 Chặn hierarchical worker không được đẻ worker → tránh đệ quy vô hạn Công cụ bạn dùng hằng ngày chính là ví dụ Day 09 gần nhất Giảng viên (VinUni) AICB · Ngày 9 T uần 2 13 / 70

---

<!-- chiron-source-span: {"source_span_id":"34368055-117a-5a6a-bf42-fc8bcada36d3","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Multi-Agent Patterns","extraction_method":"pdf-text-layer"},"checksum":"0780c36fa17498a8a0d80162e2e36e1cbcc2c30852a5da58b91ebb61cfc7aa17"} -->

## Slide 18 - Multi-Agent Patterns

03 Có nhiều cách chia hệ thống thành nhiều agent; điều quan trọng là chọn pattern giúp giải quyết đúng loại phức tạp, không tạo thêm phức tạp giả

---

<!-- chiron-source-span: {"source_span_id":"599f901d-7bfe-5d4d-b266-1418b40a2f80","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"4 Pattern Phổ Biến","extraction_method":"pdf-text-layer"},"checksum":"254ed75a508f0b3d95cb1eeaf01bdea26ebd052a27022d33f7b8ed3c4af5ddc2"} -->

## Slide 19 - 4 Pattern Phổ Biến

Supervisor-Worker 1 supervisor điều phối nhiều worker chuyên biệt. Mạnh ở: routing rõ, dễ kiểm soát, dễ trace Debate Nhiều agent cùng giải một bài toán rồi vote hoặc synthesize. Mạnh ở: phản biện và giảm blind spot Pipeline Agent A xong rồi mới chuyển output cho B. Mạnh ở: flow ổn định, tuyến tính, dễ test Hierarchical Supervisor lồng supervisor cho nhiều tầng hệ thống. Mạnh ở: mở rộng tốt ở enterprise scale Lựa chọn cho Day 09: đi sâu vào supervisor-worker — dễ dạy, dễ build lab, dễ nối từ artifact Day 08. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 14 / 70

---

<!-- chiron-source-span: {"source_span_id":"bd2f4e66-cf09-59f7-a8c7-3987dffc73f4","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Chọn Pattern Theo Loại Bài T oán","extraction_method":"pdf-text-layer"},"checksum":"e1257b8a4d32b19b7858f61bdf0bec2eedb941c8ae1d07db9bbb77af2f8e0ca3"} -->

## Slide 20 - Chọn Pattern Theo Loại Bài T oán

Pattern Dùng khi nào Điểm mạnh Cảnh báo Supervisor- worker Task cần route tới đúng vai trò dễ kiểm soát, dễ trace supervisor có thể thành bot- tleneck nếu làm quá nhiều Pipeline Các bước gần như cố định dễ hiểu, dễ test theo bước kém linh hoạt khi flow đổi động Debate Cần nhiều góc nhìn cho cùng một bài toán giảm blind spot, tăng phản biện tốn cost và khó tổng hợp Hierarchical Nhiều nhóm task và nhiều tầng quản trị mở rộng tốt ở quy mô lớn thiết kế và de- bugging phức tạp Đừng để 4 pattern ngang nhau trong đầu người học Giảng viên (VinUni) AICB · Ngày 9 T uần 2 15 / 70

---

<!-- chiron-source-span: {"source_span_id":"1517b09e-3352-5ecb-b945-2079d8e1d0ae","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Minh Họa: Pipeline Pattern Trông Như Thế Nào?","extraction_method":"pdf-text-layer"},"checksum":"39d92b483b6cd249824bf50c1d530a95b7ddd6b892cac0b77d89cf94a4166134"} -->

## Slide 21 - Minh Họa: Pipeline Pattern Trông Như Thế Nào?

Input Parser Agent Research Agent Writer Agent Review Agent Phù hợp nhất khi

- flow gần như cố định

- mỗi bước cần output của bước trước

- dễ test từng agent riêng biệt
Hạn chế

- latency cộng dồn ở mỗi bước

- khó xử lý khi flow cần rẽ nhánh

- retry một bước ảnh hưởng toàn chuỗi
Giảng viên (VinUni) AICB · Ngày 9 T uần 2 16 / 70

---

<!-- chiron-source-span: {"source_span_id":"c2a8bc0d-48b4-5af2-a2d5-b44c94cbe703","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Minh Họa: Debate Pattern","extraction_method":"pdf-text-layer"},"checksum":"93b9726209cb11f8ec41cb8d3a07cede4ea59730e0f74c3553aa5d3aff0b0750"} -->

## Slide 22 - Minh Họa: Debate Pattern

T ask Agent A Agent B Agent C Aggregator Dùng khi nào Khi bài toán có nhiều góc nhìn hợp lệ, khi rủi ro sai cao, hoặc khi cần kiểm tra chéo trước một quyết định quan trọng. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 17 / 70

---

<!-- chiron-source-span: {"source_span_id":"901e0f05-cb11-576a-93fc-24c3d3575e82","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Vì Sao Day 09 Chọn Supervisor-Worker?","extraction_method":"pdf-text-layer"},"checksum":"50c0674efeee8d2d66f349b85b36f3c0bb6d75a0d751ca8adbd8588b48b22cae"} -->

## Slide 23 - Vì Sao Day 09 Chọn Supervisor-Worker?

Lý do sư phạm

- học viên dễ nhìn ra vai trò

- dễ nối với use case thật

- dễ giải thích logic route

- dễ nâng cấp từ artifact Day 08
Lý do triển khai

- bắt đầu từ 2–3 worker là đủ

- dễ cắm thêm MCP tool worker

- trace và testing rõ hơn

- supervisor thường chỉ cần một
LLM call nhỏ Lưu ý: Nếu Day 09 ôm nhiều pattern ngang nhau, người học sẽ nhớ tên pattern nhưng không biết ngày mai nên build theo pattern nào. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 18 / 70

---

<!-- chiron-source-span: {"source_span_id":"f12450f4-a6f1-596b-b57b-5efd06b5982e","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Supervisor-Worker: Deep Dive","extraction_method":"pdf-text-layer"},"checksum":"09303074004e9c0d42c4d257b2f75a1eefd34e52acec1ca704c4004651f0560a"} -->

## Slide 24 - Supervisor-Worker: Deep Dive

04 Thay vì ép một agent làm hết, ta cho một supervisor phân việc và nhiều worker làm phần việc hẹp, dễ kiểm soát hơn

---

<!-- chiron-source-span: {"source_span_id":"bd19a428-aa67-5564-a9fe-3bd4d0bba543","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Supervisor-Worker Architecture","extraction_method":"pdf-text-layer"},"checksum":"998fa1e5260f490611157d3f0ab7f30d5dcb87b7e4261a58a36ea567a9995b73"} -->

## Slide 25 - Supervisor-Worker Architecture

User Request Supervisor Retrieval Worker T ool Worker Synthesis Worker Final Answer + Trace Khung nghĩ đúng Supervisor không cần “thông minh hơn tất cả”. Vai trò chính là chia việc đúng, gọi đúng worker, và gom đầu ra thành kết quả mạch lạc. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 19 / 70

---

<!-- chiron-source-span: {"source_span_id":"8fd1567b-c752-5946-b04f-ba9cc47d280d","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Supervisor Làm Gì, Worker Làm Gì?","extraction_method":"pdf-text-layer"},"checksum":"5b18fa0865c9d71f0a8485455c1d6b6ec9d1a7f5a25a475c12c9060316608a11"} -->

## Slide 26 - Supervisor Làm Gì, Worker Làm Gì?

Supervisor

- phân tích yêu cầu ban đầu

- quyết định worker nào nên tham gia

- theo dõi trạng thái và retry nếu cần

- tổng hợp đầu ra cuối cùng

- biết khi nào cần human review
Worker

- xử lý một năng lực hẹp

- nhận input rõ ràng, trả output rõ ràng

- càng stateless càng dễ test

- thất bại cục bộ không làm hỏng cả kiến
trúc

- có thể được thay thế mà không ảnh
hưởng supervisor Rule of thumb Supervisor giữ decision flow; worker giữ domain skill. Đừng để một worker vừa làm việc hẹp vừa bí mật điều phối cả hệ thống. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 20 / 70

---

<!-- chiron-source-span: {"source_span_id":"af28abe7-788e-5171-a159-41d8b1d83b88","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Thiết Kế Worker T ốt Có 3 Đặc Điểm","extraction_method":"pdf-text-layer"},"checksum":"213b43619029768af7fcb5ded8e84402283214f32b52ad479e5c617fa5f95d5a"} -->

## Slide 27 - Thiết Kế Worker T ốt Có 3 Đặc Điểm

Specialized Một worker nên có

### một năng lực chính
retrieve, gọi tool, tóm tắt, kiểm tra policy... Stateless ưu tiên Nếu có thể, worker chỉ cần input hiện tại thay vì ôm cả lịch sử hệ thống. T estable Có input / output rõ để test độc lập trước khi cắm vào supervisor. Lưu ý: Worker mơ hồ thường làm debugging cực khó: không biết lỗi do route sai, prompt sai, hay contract đầu vào chưa đủ rõ. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 21 / 70

---

<!-- chiron-source-span: {"source_span_id":"131dfeb2-1b96-5d3e-9656-0b0c70a44f48","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Anti-Pattern: Những Lỗi Thiết Kế Hay Gặp","extraction_method":"pdf-text-layer"},"checksum":"23276cdae89138c711611bbadb263ea15a90e37d49a0db3aaec1800ab2865ea0"} -->

## Slide 28 - Anti-Pattern: Những Lỗi Thiết Kế Hay Gặp

God Supervisor Supervisor làm quá nhiều: plan, re- trieve, synthesize, monitor. Nó trở thành single-agent được đổi tên. Chatty Workers Workers liên tục gọi ngược lại super- visor để hỏi thêm thông tin. Message overhead tăng rất nhanh. Implicit State State bị truyền qua biến toàn cục hoặc side effect. Không ai biết hệ đang ở bước nào. No Fallback Worker gặp lỗi và không trả về gì. Supervisor chờ mãi không thấy đầu ra để tổng hợp. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 22 / 70

---

<!-- chiron-source-span: {"source_span_id":"63ab3cef-3da4-598c-bf0c-5a54e39a34b9","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Shared State Hay Message Passing?","extraction_method":"pdf-text-layer"},"checksum":"249dd6588621a69a85bd0bf05afcefa47aa8209aa1828dd5bdbf725163b7fc8d"} -->

## Slide 29 - Shared State Hay Message Passing?

Shared state

- dễ xem toàn cảnh

- tiện cho graph orchestration
(LangGraph)

- nhưng dễ bị “đụng tay” lẫn nhau nếu
không có kỷ luật

- cần schema rõ: ai được đọc gì, ai được
ghi gì Message passing

- contract rõ hơn giữa các agents

- ít coupling hơn

- nhưng phải thiết kế message format cẩn
thận

- cần validation ở mỗi điểm nhận
Cách dạy thực dụng Trong Day 09, học viên chỉ cần nhớ: shared state giúp điều phối, còn message con- tract giúp giao tiếp không nhập nhằng. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 23 / 70

---

<!-- chiron-source-span: {"source_span_id":"af166e14-1529-549d-a352-737abf9f0806","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"State Schema T ối Thiểu Cho Day 09","extraction_method":"pdf-text-layer"},"checksum":"09c0ac04ff8182d79a3d6aff9e74ad1d8c7150dd9ec840e54111b13341a725fa"} -->

## Slide 30 - State Schema T ối Thiểu Cho Day 09

```text
class Day09State(TypedDict):
```
task: str # task ốgc ừt user plan: list[str] # worker ầcn ọgi worker_results: dict # output ừtng worker status: str # pending|running|done final_answer: str # ổtng ợhp ốcui trace: list[dict] # log có timestamp error: Optional[ str] T ại sao trace là trường bắt buộc? Không có trace trong state, sau khi hệ chạy xong không ai biết agent đã đi theo con đường nào để ra kết quả đó. Quy tắc: trace là list, luôn append, không bao giờ overwrite. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 24 / 70

---

<!-- chiron-source-span: {"source_span_id":"6e58f035-b831-5102-a2e2-26f83832ace5","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Nâng Cấp Artifact Day 08 Thành Day 09","extraction_method":"pdf-text-layer"},"checksum":"ce902df09a3981b637ebef759cb5760d388ed0265f725467431eaeb9dd79e6bf"} -->

## Slide 31 - Nâng Cấp Artifact Day 08 Thành Day 09

Day 08 RAG Agent Day 09 Supervisor Retrieval Worker T ool Worker Synthesis Worker tách vai trò Thông điệp lab Day 09 không bắt đầu từ số 0. Ta lấy năng lực retrieve và answer của Day 08 rồi chia vai trò thành các worker để hệ thống rõ ràng hơn. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 25 / 70

---

<!-- chiron-source-span: {"source_span_id":"77c60588-3ad1-5514-a246-c26ec0896680","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Mini-Quest 2: Tìm Lỗi Trong Supervisor Node","extraction_method":"pdf-text-layer"},"checksum":"0e35017a0d5dc59077c3ecf009a4310a63905c2124122d73a888e7bd4784a596"} -->

## Slide 32 - Mini-Quest 2: Tìm Lỗi Trong Supervisor Node

MINI-QUEST 2 20 phút · 5’ cá nhân + 8’ nhóm + 7’ chữa chung

```text
def supervisor_node(state: AgentState) -> AgentState:
decision = llm.invoke(
SUPERVISOR_PROMPT.format(task=state["task"])
)
docs = vector_store.search(state[ "task"], k=20)
state["retrieval_result"] = docs
state["trace"] = [f "[supervisor] {decision}"]
result = tool_worker(state)
state["final_answer"] = result[ "text"]
return state
```
Câu hỏi cho nhóm Đoạn code chạy được, không crash, nhưng vi phạm ít nhất 4 nguyên tắc đã học sáng nay.

1. Tìm đủ 4 lỗi

2. Gọi tên anti-pattern tương ứng cho từng lỗi

3. Với mỗi lỗi, viết 1 dòng mô tả cách sửa

4. Lỗi nào sẽ khiến việc debug khó nhất? Vì sao? Giảng viên (VinUni) AICB · Ngày 9 T uần 2 26 / 70

---

<!-- chiron-source-span: {"source_span_id":"d650f2b7-94bc-5269-9e9a-80a483b0324b","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Debrief Quest 2: 4 Lỗi Và Cách Sửa","extraction_method":"pdf-text-layer"},"checksum":"8331f235ba4a3a81b681c6470fee355bf266f6bca4bb911cb0ee66af35328c05"} -->

## Slide 33 - Debrief Quest 2: 4 Lỗi Và Cách Sửa

Lỗi trong code Anti-pattern Cách sửa Supervisor tự gọi vector_store.search God Supervisor để Retrieval Worker làm; supervisor chỉ set need_retrieval rồi route state["trace"] = [^^.] ghi đè Mất observability append: "trace": state["trace"] + [entry] Gọi thẳng tool_worker(state) trong node Routing bị chôn trong code dùng conditional edge của graph; node chỉ ra quyết định, không tự gọi worker Không kiểm tra kết quả worker, không try/except, không set status No Fallback validate output, set status=error, có retry và đường thoát khi worker fail

```text
Bonus: node mutate state tại chỗ rồi return chính nó → nên trả về dict mới để state có thể replay / persist.
```
Đáp án Mini-Quest 2 Giảng viên (VinUni) AICB · Ngày 9 T uần 2 27 / 70

---

<!-- chiron-source-span: {"source_span_id":"6851b615-1b44-533d-bfda-7e49e9c31c0c","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"MCP — Model Context Proto","extraction_method":"pdf-text-layer"},"checksum":"ba209b8c4bd5201a914865092d393364eb9fe74e04b2fbb5238208c131cf175d"} -->

## Slide 34 - MCP — Model Context Proto

05 MCP — Model Context Proto- col Nếu supervisor-worker là cách chia người làm việc, thì MCP là cách agent cắm được vào năng lực bên ngoài mà không phải custom từng tích hợp từ đầu

---

<!-- chiron-source-span: {"source_span_id":"0a2f253d-0b23-5143-a419-0ac5f2cf5806","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"MCP Xuất Hiện Để Giải Quyết Vấn Đề Gì?","extraction_method":"pdf-text-layer"},"checksum":"773a439a49aa1b3449072efeb833e4c2c4893ab08afdddb0b87c0305dbf3967d"} -->

## Slide 35 - MCP Xuất Hiện Để Giải Quyết Vấn Đề Gì?

Trước MCP — vấn đề thực tế

- mỗi tool cần một adapter riêng

- thay đổi API của tool = viết lại code tích
hợp

- mỗi framework gọi tool theo cách khác
nhau

- không có chuẩn chung để agent biết tool
làm gì MCP giải quyết Một chuẩn giao tiếp duy nhất giữa agent và tool. Agent biết cách khám phá các capability mà không cần hard-code từng tích hợp. Lưu ý: Điều quan trọng với người học là hiểu vì sao MCP giúp mở rộng hệ thống, không phải học thuộc protocol spec trong buổi đầu tiên. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 28 / 70

---

<!-- chiron-source-span: {"source_span_id":"98132b66-c4a5-5e4c-891a-a295217b7337","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"MCP Là Gì Theo Cách Hiểu Thực Dụng?","extraction_method":"pdf-text-layer"},"checksum":"75505c0ded07167e15bfe92734d60dda31d5db9554a180d60542d49b4a864ad6"} -->

## Slide 36 - MCP Là Gì Theo Cách Hiểu Thực Dụng?

- MCP là một chuẩn để agent kết nối với
external capabilities.

- Thay vì mỗi tool có một kiểu tích hợp riêng,
agent có thể nói chuyện với một MCP server.

- MCP server công bố các thứ như tools,
resources, và prompts.

- Agent có thể list, describe, và invoke các
capability đó theo chuẩn chung. Analogy dễ nhớ Supervisor-worker nói về vai trò. MCP nói về ổ cắm chuẩn để agent dùng tài nguyên bên ngoài. Giống USB: mọi thiết bị cùng dùng một chuẩn kết nối. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 29 / 70

---

<!-- chiron-source-span: {"source_span_id":"0978c87f-8290-5cbd-9f67-46b9ccc28762","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"MCP Architecture","extraction_method":"pdf-text-layer"},"checksum":"f4497af1eea7d16a78704dff0a4ecb4b54b6ae0e6619843b886448778deecbe6"} -->

## Slide 37 - MCP Architecture

Agent / MCP Client MCP Server Tools Resources Prompts JSON-RPC / HTTP Điểm cốt lõi Agent không cần biết chi tiết từng hệ thống phía sau. Nó chỉ cần hiểu MCP surface mà server công bố. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 30 / 70

---

<!-- chiron-source-span: {"source_span_id":"1be03496-626e-518f-81aa-ef76a3feeb13","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"MCP Server Có Thể Mở Ra Những Gì?","extraction_method":"pdf-text-layer"},"checksum":"15ec0846cc501d7aba2a3ff5ca77f4e06f77dd8f531c3569c8a9043d31d251cd"} -->

## Slide 38 - MCP Server Có Thể Mở Ra Những Gì?

T ools Hành động hoặc thao tác Ví dụ: search, query API, tạo ticket, gọi webhook Resources Tài nguyên để đọc Ví dụ: file, schema, catalog, config, DB Prompts Prompt dùng lại Giúp chuẩn hóa cách gọi năng lực và giảm lỗi prompt Lưu ý: Không phải MCP server nào cũng phải có đủ cả ba. Điều quan trọng là agent có một cách nhìn nhất quán về các capability được công bố. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 31 / 70

---

<!-- chiron-source-span: {"source_span_id":"c54ba981-4227-581a-ac75-d3f2b31b84a6","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"MCP T ool Discovery: Agent Tìm Hiểu T ool Như Thế Nào?","extraction_method":"pdf-text-layer"},"checksum":"c7e8e3017d9f2f989a6def82f9e7298bd65b394e16b3664de2980a7b5ceae428"} -->

## Slide 39 - MCP T ool Discovery: Agent Tìm Hiểu T ool Như Thế Nào?

Luồng discovery

1. Agent kết nối tới MCP server

2. Gọi tools/list để lấy danh sách tool

3. Mỗi tool trả về: name, description, inputSchema

4. Agent đọc schema, quyết định tool nào phù hợp

5. Gọi tools/call với đúng parameters

6. MCP server thực thi và trả kết quả T ại sao quan trọng? Agent không cần được lập trình sẵn biết tool “X” tồn tại. Nó có thể khám phá khi chạy và tự điều chỉnh theo tool nào có sẵn. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 32 / 70

---

<!-- chiron-source-span: {"source_span_id":"0c20e6d4-b085-5698-8e42-88923a5c5c32","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Ví Dụ Thực T ế: MCP Server Cho Hệ Thống Day 09","extraction_method":"pdf-text-layer"},"checksum":"e0b9d2afe688599854a8eb5ad03c817b65a89b24c82f8590c15574dca3d52e70"} -->

## Slide 40 - Ví Dụ Thực T ế: MCP Server Cho Hệ Thống Day 09

Kịch bản: Customer Support Agent

- Tool Worker cần tra policy mới nhất

- Gọi MCP server “knowledge-base”

- Server expose tool: search_policy,
get_faq

- Worker gọi search_policy(query,
date_after)

- Kết quả trả về JSON chuẩn kèm source
Lợi ích trực tiếp

- Team cập nhật policy → chỉ cần update
MCP server

- Supervisor và workers không cần sửa
khi tool thay đổi

- Thêm tool mới = thêm endpoint vào
MCP server

- Dễ audit ai đã gọi tool gì và khi nào
Thông điệp chốt section MCP quan trọng vì nó tạo ecosystem effect: agent dùng được nhiều năng lực hơn mà không phải mỗi lần đều tích hợp lại từ đầu. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 33 / 70

---

<!-- chiron-source-span: {"source_span_id":"a2622daa-72d6-51eb-8915-d2cdce613f3d","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"MCP Trong Bức Tranh T oàn Hệ Thống","extraction_method":"pdf-text-layer"},"checksum":"dc3f9507e7c01e8d011d2d0f13add7cb7cb5f2dabe345ba1a2e75e620ba5e9ac"} -->

## Slide 41 - MCP Trong Bức Tranh T oàn Hệ Thống

Supervisor Retrieval W. T ool W. Synthesis W. MCP: VectorDB MCP: API MCP: Formatter Điểm cần nhớ MCP là lớp giữa worker và capability thực. Worker chỉ cần biết MCP surface, không cần biết hệ thống phía sau là gì. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 34 / 70

---

<!-- chiron-source-span: {"source_span_id":"f512188b-8ec8-5b24-8fa5-c5056b25b25e","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"A2A — Agent to Agent Com","extraction_method":"pdf-text-layer"},"checksum":"e0ff8eed0301d1c7c404d525bb131a0882a3792ea1c6e5695edea1579e1eea49"} -->

## Slide 42 - A2A — Agent to Agent Com

06 A2A — Agent to Agent Com- munication MCP giúp agent nói chuyện với tool; A2A giúp agent nói chuyện với agent khác theo cách rõ nhiệm vụ, rõ bối cảnh, và rõ đầu ra mong đợi

---

<!-- chiron-source-span: {"source_span_id":"a10a0f77-7957-5e63-a9cf-1115a7207f6b","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Đừng Nhầm MCP Với A2A","extraction_method":"pdf-text-layer"},"checksum":"df32ad74406609610546ab520fff767c0cc0fb4fca87ab5254039d4acee75691"} -->

## Slide 43 - Đừng Nhầm MCP Với A2A

MCP

- agent nói chuyện với tool / capability

- mục tiêu là kết nối năng lực bên ngoài

- trọng tâm là surface chuẩn

- tool không có agency — chỉ thực thi
A2A

- agent nói chuyện với agent khác

- mục tiêu là chia việc và đồng bộ

- trọng tâm là message contract rõ ràng

- agent phía kia có thể ra quyết định
Lưu ý: Cùng là “gọi ra ngoài”, nhưng MCP trả lời câu hỏi agent lấy năng lực ở đâu, còn A2A trả lời câu hỏi agent giao việc cho ai. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 35 / 70

---

<!-- chiron-source-span: {"source_span_id":"d77849e9-281b-548f-929d-112b65a995d2","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"T ại Sao A2A Cần Message Contract?","extraction_method":"pdf-text-layer"},"checksum":"89e1d5afb6a1ac49a4f716634e256527a465540d3d241e109a930133119b0527"} -->

## Slide 44 - T ại Sao A2A Cần Message Contract?

Không có contract rõ

- supervisor gọi worker với: “Hãy tìm policy liên
quan”

- worker không biết context là gì

- worker trả về 10 kết quả không được lọc

- supervisor không biết kết quả nào dùng được

- lỗi lộ ra ở phần tổng hợp, nhưng gốc là ở phần
gọi Với contract rõ Supervisor gọi worker với đầy đủ task + context + expected format. Worker biết chính xác cần làm gì và trả về theo schema đã thống nhất. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 36 / 70

---

<!-- chiron-source-span: {"source_span_id":"06d2d2c0-b6d4-5e93-bddb-b198bfcfc155","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Một Message Contract T ối Thiểu Cho A2A","extraction_method":"pdf-text-layer"},"checksum":"53653c70c6507f250828d3d3b19f86ab7c691f68f2b6b608dd874fbde66aeff9"} -->

## Slide 45 - Một Message Contract T ối Thiểu Cho A2A

T ask Agent kia cần làm gì? Ví dụ: tìm 3 chunk pol- icy phù hợp nhất Context Những gì worker cần biết để làm đúng? query, constraints, user role, state Expected output Trả về theo format nào? list chunks, score, rationale, error

### Ví dụ
task = ”retrieve evidence” context = ”user hỏi về refund policy, ưu tiên tài liệu sau 2025” expected_output = ”top 3 chunks + source + confidence” Giảng viên (VinUni) AICB · Ngày 9 T uần 2 37 / 70

---

<!-- chiron-source-span: {"source_span_id":"1af7dbc7-9cb8-5813-9abb-96c954318964","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"A2A Contract: Bao Nhiêu Là Đủ?","extraction_method":"pdf-text-layer"},"checksum":"fef52e99f8f44f77b2e3eade8b27f64d5f19fdef4f77e49346e88bf5490742ce"} -->

## Slide 46 - A2A Contract: Bao Nhiêu Là Đủ?

Thiếu context

- worker lấy kết quả không phù hợp

- phải gọi lại nhiều lần

- debugging rất khó
Quá nhiều context

- tốn token không cần thiết

- worker xử lý chậm

- khó maintain khi schema thay đổi
Nguyên tắc “need to know” Worker chỉ nhận context mà nó thực sự cần để hoàn thành task của mình. Không thêm, không bớt. Khi không chắc → bắt đầu với ít hơn và thêm khi cần. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 38 / 70

---

<!-- chiron-source-span: {"source_span_id":"cb7e9cd4-ac78-5f1e-910b-96c96212c74e","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Sync Hay Async?","extraction_method":"pdf-text-layer"},"checksum":"d387ccabf8f0fb662393430ed1c4bbc4cbdb9dc055a8a7b4d16221e41fd13d24"} -->

## Slide 47 - Sync Hay Async?

Sync

- đơn giản để hiểu và debug

- phù hợp khi supervisor cần kết quả ngay
để đi bước tiếp

- nhưng dễ tăng latency toàn luồng

- bắt đầu ở đây cho Day 09
Async

- hợp khi nhiều worker chạy song song

- tận dụng được concurrency

- nhưng cần quản lý trạng thái và timeout
tốt hơn

- mở rộng khi đã nắm sync tốt
Cách giảng đơn giản Sync dễ dạy cho vòng đầu. Async chỉ cần giới thiệu như một hướng mở rộng khi nhiều worker có thể chạy độc lập. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 39 / 70

---

<!-- chiron-source-span: {"source_span_id":"54dc67c4-9468-53f0-8768-075fc797e474","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"Security Và Boundary Trong Giao Tiếp Agent","extraction_method":"pdf-text-layer"},"checksum":"2ea8d77ec3b33b1037b78e671c67baf2e07db9754c0d948549d42224209fabc2"} -->

## Slide 48 - Security Và Boundary Trong Giao Tiếp Agent

- ✓ Biết rõ ai được gọi ai: không phải agent nào cũng được chạm mọi capa-
bility

- ✓ Biết dữ liệu nào được truyền đi: tránh đẩy thừa PII hoặc state nhạy cảm

- ✓ Biết output nào cần xác thực lại: đặc biệt khi worker chạm tool ngoài

- ✓ Validate đầu ra trước khi dùng: worker hoàn toàn có thể trả về schema
sai

- Đừng giả định mọi agent đều đáng tin như nhau. Hệ nhiều agent vẫn cần
trust boundary Giảng viên (VinUni) AICB · Ngày 9 T uần 2 40 / 70

---

<!-- chiron-source-span: {"source_span_id":"06de4fe0-e05f-5dfb-a1b6-ef59db1787da","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Orchestration Với LangGraph","extraction_method":"pdf-text-layer"},"checksum":"05f023772144824aaf62e5607ba31facaafa45a472102ce5144421b53d47a841"} -->

## Slide 49 - Orchestration Với LangGraph

07 Sau khi hiểu vai trò và giao tiếp, ta cần một cách biểu diễn luồng chạy rõ ràng; LangGraph là cách rất trực quan để làm điều đó

---

<!-- chiron-source-span: {"source_span_id":"30c888ac-ecca-5971-b786-7b8ef52d62b0","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"T ại Sao Cần Orchestration Framework?","extraction_method":"pdf-text-layer"},"checksum":"e7d37e20f69106db1f45d88cb15c2bb3b3d4241da12c0d501e524245d94f1824"} -->

## Slide 50 - T ại Sao Cần Orchestration Framework?

Không có framework

- routing logic nằm trong prompt điều phối
dài

- khó biết hệ đang ở bước nào

- thêm một nhánh mới = sửa toàn bộ prompt

- debug bằng print() và hy vọng
Với LangGraph Routing trở thành code tường minh. Graph có thể visualize. State có schema. Human-in- the-loop có điểm rõ ràng. Lưu ý: Nếu không có orchestration rõ ràng, routing logic thường bị chôn trong prompt và trở nên rất khó debug. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 41 / 70

---

<!-- chiron-source-span: {"source_span_id":"bbf305fd-5997-5fc2-a5ee-53b53b54c696","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"LangGraph Đóng Vai Trò Gì?","extraction_method":"pdf-text-layer"},"checksum":"9f8c82ce372a2c10be53997820f162ee8d90f73ba426b00af4ca44001594e6a0"} -->

## Slide 51 - LangGraph Đóng Vai Trò Gì?

- Biến hệ multi-agent thành graph gồm nodes,
edges, và state.

- Tách rõ node nào làm việc gì và khi nào
route sang node nào.

- Giúp hệ thống bớt phụ thuộc vào một prompt
điều phối khổng lồ.

- Hỗ trợ persistence: state có thể được lưu và
chạy tiếp.

- Hỗ trợ human-in-the-loop tại bất kỳ điểm
nào. Khung nhớ nhanh node = ai làm edge = đi đâu tiếp state = hệ đang biết gì Ba khái niệm này là toàn bộ LangGraph bạn cần cho Day 09. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 42 / 70

---

<!-- chiron-source-span: {"source_span_id":"6680e89e-0a5e-5d0f-82c4-8b1d4df5ae9b","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"LangGraph: Nodes Và Edges","extraction_method":"pdf-text-layer"},"checksum":"ce2468de9649db1417b860bf83a5b3b39142e0b20bf04dc45480b849ffe0994d"} -->

## Slide 52 - LangGraph: Nodes Và Edges

Node

- là một hàm Python nhận state và trả state
mới

- tương ứng với một agent hoặc một bước
xử lý

- có thể là supervisor, worker, hoặc human
review Edge

- Unconditional edge: luôn đi từ A sang B

- Conditional edge: hàm trả về tên node
tiếp theo dựa trên state State Là TypedDict hoặc Pydantic model được truyền qua mỗi node. Mỗi node có thể đọc toàn bộ state và ghi vào các trường được phép. State là “bộ nhớ” của cả graph. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 43 / 70

---

<!-- chiron-source-span: {"source_span_id":"816b5b80-6182-5f21-8cf4-6d44141b8386","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"LangGraph Routing Diagram","extraction_method":"pdf-text-layer"},"checksum":"e591149d603250292d038beeb363bb2e22a20812990accb17b992efd3fcad157"} -->

## Slide 53 - LangGraph Routing Diagram

Input State Supervisor Retrieval Worker T ool Worker Synthesis Worker Human Review Output State conditional edges Điểm cần nhớ LangGraph làm lộ rõroute quyết định ở đâu, state đi qua đâu, và human can thiệp ở điểm nào. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 44 / 70

---

<!-- chiron-source-span: {"source_span_id":"bd4744c5-69a6-549a-b81e-944121d7e84c","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"Ví Dụ Routing Logic Ngắn","extraction_method":"pdf-text-layer"},"checksum":"635256616fc33b69fcdf56d57382be21f59af22e27e845cce6b2bd06f008f9d7"} -->

## Slide 54 - Ví Dụ Routing Logic Ngắn

```text
class AgentState(TypedDict):
```
task: str need_retrieval: bool need_tool: bool worker_results: dict final_answer: str

```text
def route_to_worker(state: AgentState) -> str:
```

### if state["need_tool"]

```text
return "tool_worker"
```

### if state["need_retrieval"]

```text
return "retrieval_worker"
return "synthesis_worker"
graph.add_conditional_edges(
```
"supervisor", route_to_worker,

```text
{
```
"tool_worker": "tool_worker", "retrieval_worker": "retrieval_worker", "synthesis_worker": "synthesis_worker", }, ) Ý chính không nằm ở syntax mà ở chỗ: routing trở thành logic tường minh, thay vì ẩn trong một prompt điều phối rất dài. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 45 / 70

---

<!-- chiron-source-span: {"source_span_id":"028e806a-7439-5f63-8353-976f8a054355","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"Một Node Supervisor T ối Giản","extraction_method":"pdf-text-layer"},"checksum":"20cfa21ec0706c0ba8c7e077d6db7ea825d56f40510fe58abafbc367f59bf628"} -->

## Slide 55 - Một Node Supervisor T ối Giản

```text
def supervisor_node(state: AgentState) -> AgentState:
decision = llm.invoke(
SUPERVISOR_PROMPT.format(task=state["task"])
)
return {
```
**state, "need_retrieval": decision.need_retrieval, "need_tool": decision.need_tool, "trace": state[ "trace"] + [ f"[supervisor] retrieval=" f"{decision.need_retrieval} " f"tool={decision.need_tool}" ], } Đọc gì từ đoạn này?

- supervisor node không làm
việc của worker — nó chỉ ra quyết định route

- trả về dict mới (**state)
thay vì sửa state tại chỗ

- trace được append, không
overwrite Giảng viên (VinUni) AICB · Ngày 9 T uần 2 46 / 70

---

<!-- chiron-source-span: {"source_span_id":"71c30e24-7e89-51c4-8afb-bb759d386ba8","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"Human-in-the-Loop Đặt Ở Đâu?","extraction_method":"pdf-text-layer"},"checksum":"7b3c3dc786fb4f69bc6fefe6de30525c8c5235725676eec5de85396d35f94b86"} -->

## Slide 56 - Human-in-the-Loop Đặt Ở Đâu?

Nên chèn khi

- task có rủi ro cao (tài chính, y tế,
pháp lý)

- confidence score dưới ngưỡng

- tool action có side effect không đảo
ngược

- output sẽ đi ra user hoặc stakeholder

- hệ thống không chắc về intent ban
đầu Cách implement trong LangGraph

- thêm node human_review vào graph

- node này interrupt graph và chờ input

- sau khi human approve → chạy tiếp

- state được giữ nguyên qua interrupt

- log lại quyết định của human trong
trace Khung nghĩ đúng Multi-agent không đồng nghĩa với full autonomy. Nhiều hệ tốt nhất là hệ biết khi nào nên dừng để con người quyết định. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 47 / 70

---

<!-- chiron-source-span: {"source_span_id":"9b0b4e30-7376-594b-8c30-8a3dc499da99","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"Observability & Debugging Hệ","extraction_method":"pdf-text-layer"},"checksum":"eb68385ea25978c5f7332cf11b299c5e6ab597af617940a23adab6a9fe669cf9"} -->

## Slide 57 - Observability & Debugging Hệ

08 Multi-Agent Hệ thống nhiều agent khó debug hơn nhiều so với single agent; observability tốt là điều kiện tiên quyết để cải thiện được hệ thống

---

<!-- chiron-source-span: {"source_span_id":"55e78e3c-6102-5797-8304-e75199272bd4","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"Vì Sao Multi-Agent Khó Debug Hơn?","extraction_method":"pdf-text-layer"},"checksum":"04499e9dcdba4a5ff7566d710838661d98e5675adc3cb4f3ff2dc5a920fa1206"} -->

## Slide 58 - Vì Sao Multi-Agent Khó Debug Hơn?

Nguồn gốc lỗi khó xác định

- Lỗi có thể xuất phát từ: routing sai, context
sai, tool fail, synthesis sai

- Lỗi ở bước A có thể chỉ lộ ra ở bước C

- Nhiều agent = nhiều LLM call = nhiều điểm
fail tiềm năng 3 câu hỏi observability

1. Agent nào đã chạy, theo thứ tự nào?

2. Input / output tại mỗi bước là gì?

3. Lỗi hay warning nào đã xảy ra? Lưu ý: Không có trace tốt, debugging multi-agent gần như là mò mẫm. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 48 / 70

---

<!-- chiron-source-span: {"source_span_id":"1d15cee3-317f-540e-8fbf-211418089696","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"Thiết Kế Trace Log T ốt","extraction_method":"pdf-text-layer"},"checksum":"9bfef61d15d48496927b0d212f06f2e8740eb753ad91742799d55373c2fc1c4c"} -->

## Slide 59 - Thiết Kế Trace Log T ốt

Mỗi entry trong trace nên có

- timestamp — khi nào

- agent_id — ai làm

- action — làm gì (route / call / synthesize / error)

- input_summary — nhận gì (tóm tắt, không full
context)

- output_summary — trả về gì

- status — ok | warn | error

- latency_ms — mất bao lâu

```text
{
```
"t": "14:03:21", "agent": "supervisor", "action": "route", "decision": "retrieval_worker", "reason": "need_retrieval=true", "status": "ok", "latency_ms": 312 } Giảng viên (VinUni) AICB · Ngày 9 T uần 2 49 / 70

---

<!-- chiron-source-span: {"source_span_id":"37530104-3ec8-5d72-981d-e9bdff961bff","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"Trace Nên Ghi Những Gì?","extraction_method":"pdf-text-layer"},"checksum":"fb82a45011dab3fecf26e8374ee118d2cbd1f2535fa28e06ea70009f925bbbd0"} -->

## Slide 60 - Trace Nên Ghi Những Gì?

- supervisor nhận task gì và route theo tiêu chí nào

- worker nào được gọi và input nó nhận là gì

- worker trả về output gì, confidence hoặc status gì

- supervisor đã tổng hợp ra answer cuối cùng như thế nào

- điểm nào bị retry, timeout, hoặc fallback

- nếu có human review, human đã quyết định gì
Lưu ý: Nếu log chỉ có “agent chạy xong”, học viên sẽ không học được gì về orchestration. Trace tốt phải giúp nhìn thấy đường đi của quyết định. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 50 / 70

---

<!-- chiron-source-span: {"source_span_id":"bb74e408-faa3-54f2-aac3-a50633b7c4e5","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"Công Cụ Observability Phổ Biến","extraction_method":"pdf-text-layer"},"checksum":"c603a9e80bdee8ca74ae5079102ef04cd178c80410693f05bd0ce490601bbf08"} -->

## Slide 61 - Công Cụ Observability Phổ Biến

LangSmith Tích hợp sẵn với LangChain / Lang- Graph. Trace tự động, visual flow, so sánh runs. JSON log tự viết Structured output ghi thẳng vào state. Đơn giản nhất cho Day 09 — dễ đọc, dễ inspect. OpenT elemetry Chuẩn mở cho dis- tributed tracing. Phù hợp khi hệ thống lớn hơn và cần dashboard. Gợi ý cho lab Bắt đầu với JSON log tự viết vào state. Đây là cách học được nhiều nhất về cách hệ hoạt động. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 51 / 70

---

<!-- chiron-source-span: {"source_span_id":"a17a8c34-b6c4-5d61-85bd-d8b877d8291b","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Từ Trace Đến Cải Thiện Hệ Thống","extraction_method":"pdf-text-layer"},"checksum":"e194d111ca016b502b56fd96456bff4bfd11cb3a7322def4e57a91baf285ca8e"} -->

## Slide 62 - Từ Trace Đến Cải Thiện Hệ Thống

Chạy hệ thống Đọc trace Tìm pattern lỗi Fix: prompt / route / schema Eval lại vòng tiếp theo Điểm cần nhớ Trace không chỉ để debug lỗi hôm nay. Nó là dữ liệu để cải thiện routing, worker quality, và message contract theo thời gian. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 52 / 70

---

<!-- chiron-source-span: {"source_span_id":"fdf3745f-d648-55e9-b886-539385661836","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"Mini-Quest 3: Đọc Trace, Tìm Root Cause","extraction_method":"pdf-text-layer"},"checksum":"3e7e61dda1d2d16ad6a4f39f9c3a6af79061d32a243d40da335a49e3c256bced"} -->

## Slide 63 - Mini-Quest 3: Đọc Trace, Tìm Root Cause

MINI-QUEST 3 20 phút · 7’ đọc trace + 8’ nhóm + 5’ chữa {"t":"09:14:02","agent":"supervisor","action":"route", "decision":"retrieval_worker","status":"ok","latency_ms":240} {"t":"09:14:03","agent":"retrieval_worker","action":"search", "input":"chính sách hoàn ềtin","output":"0 chunks", "status":"ok","latency_ms":890} {"t":"09:14:04","agent":"supervisor","action":"route", "decision":"synthesis_worker","reason":"retrieval done", "status":"ok","latency_ms":180} {"t":"09:14:09","agent":"synthesis_worker","action":"synthesize", "input":"0 chunks","output":"Chính sách hoàn ềtin là 30 ngày...", "status":"ok","latency_ms":5100} {"t":"09:14:09","agent":"supervisor","action":"finalize","status":" ok"} Tình huống Khách hàng báo câu trả lời sai hoàn toàn — công ty không hề có chính sách 30 ngày. Nhưng mọi dòng trace đều status: ok.

1. Lỗi thật sự xảy ra ở dòng nào?

2. Vì sao trace vẫn báo “ok” ở mọi bước?

3. Trace đang thiếu trường nào để phát hiện sớm?

4. Sửa ở đâu: routing, worker, contract, hay state? Giảng viên (VinUni) AICB · Ngày 9 T uần 2 53 / 70

---

<!-- chiron-source-span: {"source_span_id":"b40d6119-ae30-5dd1-8337-e4b7973bc5dc","locator":{"kind":"page","page":64,"label":"Slide 64","section_title":"Debrief Quest 3: Lỗi Im Lặng Nguy Hiểm Nhất","extraction_method":"pdf-text-layer"},"checksum":"c2e1e800b70c02c48e0f1abca1be7a8e9ba3f7cae6c2c2260bec61ec0a860d8f"} -->

## Slide 64 - Debrief Quest 3: Lỗi Im Lặng Nguy Hiểm Nhất

Root cause

- Dòng 2: retrieval trả 0 chunks nhưng vẫn
ghi status: ok — “không tìm thấy” bị coi là thành công

- Dòng 3: supervisor route tiếp mà không
kiểm tra chất lượng evidence

- Dòng 4: synthesis worker nhận 0 chunk
vẫn tạo ra câu trả lời → hallucination

- Lỗi lộ ra ở cuối luồng nhưng gốc nằm ở
dòng 2 Sửa ở 3 chỗ

- Contract: expected_output phải cho
phép insufficient_evidence; synthesis từ chối khi không đủ evidence

- Routing: conditional edge — nếu
result_count ^= 0 thì retry với query khác hoặc chuyển human review

- Trace: thêm result_count, top_score;
kết quả rỗng phải là status: warn, không phải ok Lưu ý: status: ok chỉ có nghĩa là “bước này không văng exception”. Nó không có nghĩa là kết quả dùng được. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 54 / 70

---

<!-- chiron-source-span: {"source_span_id":"a55463ee-bfc6-5d8e-958d-e463499aa1a0","locator":{"kind":"page","page":65,"label":"Slide 65","section_title":"Cost, Latency & Reliability","extraction_method":"pdf-text-layer"},"checksum":"9ee2f30f0fb54262f7cd272d2b634cbd98e746ac5f51a59068a5690902bc1236"} -->

## Slide 65 - Cost, Latency & Reliability

09 Multi-agent không miễn phí: nhiều agent = nhiều LLM call = nhiều tiền và nhiều điểm fail; cần tư duy trade-off từ sớm

---

<!-- chiron-source-span: {"source_span_id":"61d399f1-bf0a-55df-be52-51924745e2c4","locator":{"kind":"page","page":66,"label":"Slide 66","section_title":"Multi-Agent Cost: Nhân T ố Cần Biết","extraction_method":"pdf-text-layer"},"checksum":"deb8b49cecbe582639cdee41cb87450c19826da3fdaef5484dbbdf8b3c32eaa0"} -->

## Slide 66 - Multi-Agent Cost: Nhân T ố Cần Biết

Chi phí tăng từ đâu?

- Mỗi agent = ít nhất 1 LLM call

- Supervisor thường là một LLM call riêng

- Context truyền qua state có thể rất lớn

- Retry = gấp đôi cost tại điểm đó

- Human review = tăng latency, không tăng
cost LLM Nguyên tắc tối ưu Supervisor không cần là model lớn nhất. Nếu routing logic đơn giản, dùng model nhỏ hơn cho supervisor và giữ model mạnh cho worker cần reasoning sâu. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 55 / 70

---

<!-- chiron-source-span: {"source_span_id":"8bb1da69-1a50-57c5-b9b2-a9c1bd2f1680","locator":{"kind":"page","page":67,"label":"Slide 67","section_title":"So Sánh: Single vs Multi-Agent","extraction_method":"pdf-text-layer"},"checksum":"51885e6fe8289322d9254aad5f2a12ab5f24343766554a48787b2c3add8562d6"} -->

## Slide 67 - So Sánh: Single vs Multi-Agent

Tiêu chí Single Agent Multi-Agent Chi phí LLM thấp hơn (1 call) cao hơn (nhiều call) Latency thấp nếu prompt ngắn có thể song song; tăng nếu chạy se- rial Debuggability khó hơn (logic ẩn) tốt hơn (có trace rõ) Specialization hạn chế tốt hơn (mỗi worker chuyên biệt) Scalability khó scale vai trò dễ thêm worker mới Complexity đơn giản hơn phức tạp hơn khi setup Trade-off quan trọng cần hiểu khi thiết kế Giảng viên (VinUni) AICB · Ngày 9 T uần 2 56 / 70

---

<!-- chiron-source-span: {"source_span_id":"89ca5e4b-3795-5500-9591-ba35bf716fe6","locator":{"kind":"page","page":68,"label":"Slide 68","section_title":"Reliability: Khi Worker Thất Bại","extraction_method":"pdf-text-layer"},"checksum":"a8703c93cef66c03902c030845f1423d69edb34bee8f5116171147696a6f8941"} -->

## Slide 68 - Reliability: Khi Worker Thất Bại

Cần thiết kế trước

- Worker có timeout rõ ràng

- Supervisor có retry logic: thử lại bao nhiêu
lần?

- Nếu retry cũng fail: fallback là gì?

- Thất bại cục bộ không nên crash toàn bộ
hệ thống

- Partial failure: tổng hợp kết quả với những
worker đã thành công Graceful degradation Hệ thống không cần làm tốt mọi trường hợp. Nó cần thất bại theo cách kiểm soát được và báo cáo rõ ràng khi không đủ tự tin. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 57 / 70

---

<!-- chiron-source-span: {"source_span_id":"4e4879a9-272d-5dca-b3aa-d99a2e91ec94","locator":{"kind":"page","page":69,"label":"Slide 69","section_title":"Kế Hoạch Học T ập Ngày 9","extraction_method":"pdf-text-layer"},"checksum":"34853247cf857d47ffdddaf301c93e53dc54724f4c832b6a148edbff747f16ce"} -->

## Slide 69 - Kế Hoạch Học T ập Ngày 9

10 Roadmap rõ ràng giúp học viên biết nên đầu tư thời gian vào đâu và cần nắm vững điều gì trước khi chuyển sang bước tiếp

---

<!-- chiron-source-span: {"source_span_id":"61caf89d-3948-5496-accf-998ff82d38f8","locator":{"kind":"page","page":70,"label":"Slide 70","section_title":"Phân Bổ Thời Gian Trong Ngày","extraction_method":"pdf-text-layer"},"checksum":"54daad6961bcced367af7c23c7d7e2a074c0ac5b19168be7b5b81147380a9122"} -->

## Slide 70 - Phân Bổ Thời Gian Trong Ngày

50’ — Lý thuyết: single-agent limits, mental model, 4 patterns 20’ — Mini-Quest 1: mổ xẻ harness bạn đang dùng 40’ — Supervisor-worker deep dive, shared state, anti-patterns 20’ — Mini-Quest 2: tìm lỗi trong supervisor node 45’ — MCP architecture + A2A message contract 30’ — LangGraph: nodes, edges, state, routing code 25’ — Observability + cost / reliability trade-offs 20’ — Mini-Quest 3: đọc trace, tìm root cause 90’ — Lab 9: nâng cấp artifact Day 08 Giảng viên (VinUni) AICB · Ngày 9 T uần 2 58 / 70

---

<!-- chiron-source-span: {"source_span_id":"4a8e5a19-2d55-52c8-a32f-680115f2cebc","locator":{"kind":"page","page":71,"label":"Slide 71","section_title":"Kiến Thức Prerequisite Cần Vững","extraction_method":"pdf-text-layer"},"checksum":"4017d13024f237191cc2ed07d74740ae0a02b9663416191889767746f377cd8f"} -->

## Slide 71 - Kiến Thức Prerequisite Cần Vững

Từ Day 08 (bắt buộc)

- RAG pipeline: query → retrieve →
generate

- Tool calling cơ bản

- Cách viết system prompt có cấu trúc

- Artifact Day 08 đang hoạt động
Python foundations (cần có)

- TypedDict và type hints

- Dictionary operations

- Function decorators cơ bản

- async/await nếu đi vào async A2A
Lưu ý: Học viên chưa có artifact Day 08 hoạt động nên dành 30 phút đầu để fix artifact trước khi bắt đầu lab Day 09. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 59 / 70

---

<!-- chiron-source-span: {"source_span_id":"4fd0645e-7299-58b3-8637-2a054030a154","locator":{"kind":"page","page":72,"label":"Slide 72","section_title":"Lộ Trình Nắm Vững Day 09: 3 Cấp Độ","extraction_method":"pdf-text-layer"},"checksum":"8b7b157571f5333288e9ea7a1c396a0222a688d5f2d018f9c1b81ac95829b52e"} -->

## Slide 72 - Lộ Trình Nắm Vững Day 09: 3 Cấp Độ

Cấp 1: Foundation

- Giải thích được 4 giới
hạn single-agent

- Vẽ được sơ đồ
supervisor-worker

- Phân biệt được MCP và
A2A Cấp 2: Implementa- tion

- Build supervisor + 2
workers với shared state

- Viết message contract
cho A2A

- Dùng MCP cho 1 tool
worker Cấp 3: Mastery

- Thiết kế LangGraph có
conditional routing

- Trace log đọc được và
actionable

- Giải thích trade-off
cost / reliability Giảng viên (VinUni) AICB · Ngày 9 T uần 2 60 / 70

---

<!-- chiron-source-span: {"source_span_id":"92f6a307-eb7d-5e02-add8-2bc5302e2461","locator":{"kind":"page","page":73,"label":"Slide 73","section_title":"Common Misconceptions Cần Xóa Bỏ","extraction_method":"pdf-text-layer"},"checksum":"3fd778cd1ccdc4e940ad6244c26f201f6c8b9b635e3a32f72d79befbfd078e3a"} -->

## Slide 73 - Common Misconceptions Cần Xóa Bỏ

Misconception Reality “Nhiều agent = hệ thống tốt hơn” Nhiều agent = nhiều phức tạp, chỉ nên dùng khi cần “Supervisor phải là model lớn nhất” Supervisor chỉ cần đủ để route đúng “MCP và A2A là cùng một thứ” MCP: tool integration; A2A: agent delegation “Multi-agent tự động giải quyết context problem” Context vẫn phải được quản lý cẩn thận ở từng worker “LangGraph chỉ dùng được với LangChain” LangGraph dùng được với nhiều LLM frame- work khác Những nhầm lẫn này hay lộ ra ngay trong Mini-Quest 1 Giảng viên (VinUni) AICB · Ngày 9 T uần 2 61 / 70

---

<!-- chiron-source-span: {"source_span_id":"ecf3630a-a596-5bb4-bac1-6d8d07c3fda3","locator":{"kind":"page","page":74,"label":"Slide 74","section_title":"Bài Đọc Trước Và Sau Ngày 9","extraction_method":"pdf-text-layer"},"checksum":"67bdebdab5290ef35e878fd3493ef6edfe354613333ec2e469108ae9bb28ec7b"} -->

## Slide 74 - Bài Đọc Trước Và Sau Ngày 9

Đọc trước (chuẩn bị)

- LangGraph Quickstart
(docs.langchain.com)

- MCP Introduction —
modelcontextprotocol.io

- Sumers et al. (2023), CoALA — Section
2–3

- Review lại artifact Day 08 của bản thân
Đọc sau (củng cố)

- LangGraph Multi-Agent T utorial

- Anthropic — Building Effective Agents
(blog)

- MCP Server Examples trên GitHub

- LangSmith Tracing Guide
Cách đọc hiệu quả Hands-on trước, docs sau. Đọc code example thực tế trước khi đọc archi- tecture spec đầy đủ. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 62 / 70

---

<!-- chiron-source-span: {"source_span_id":"61e28c81-f954-5c38-98cd-66e93ef8a83f","locator":{"kind":"page","page":75,"label":"Slide 75","section_title":"Hands-on 9","extraction_method":"pdf-text-layer"},"checksum":"ff0ba818e61bb56e10b4ba8ccde6e1216cc1cf4648bfaf4d943081a36cc7eb6e"} -->

## Slide 75 - Hands-on 9

11 Lấy artifact Day 08 rồi chia lại thành supervisor, workers, và 1 điểm kết nối MCP để học viên thấy rõ giá trị của phân vai trong thực tế

---

<!-- chiron-source-span: {"source_span_id":"de6f04eb-8872-5277-85c8-dce2ee03e3c3","locator":{"kind":"page","page":76,"label":"Slide 76","section_title":"Lab 9: Multi-Agent System + MCP","extraction_method":"pdf-text-layer"},"checksum":"51607e470739e7df00458731c367a276ff07688c6573539798d9991271b67c31"} -->

## Slide 76 - Lab 9: Multi-Agent System + MCP

Mục tiêu lab Biến một agent RAG đơn thành một hệ multi-agent nhỏ có route rõ, capability rõ, và trace rõ để dễ giải thích và debug hơn.

1. tách artifact Day 08 thành supervisor + 2–3 workers

2. thiết kế shared state schema với trường trace

3. chọn 1 worker dùng external capability qua MCP

4. viết message contract tối thiểu giữa supervisor và workers

5. trace lại toàn bộ luồng để biết agent nào đã làm gì

6. demo kết quả cuối cùng kèm reasoning flow ở mức quan sát được Giảng viên (VinUni) AICB · Ngày 9 T uần 2 63 / 70

---

<!-- chiron-source-span: {"source_span_id":"b8625e2e-f973-539f-bf53-526d3bdb96bb","locator":{"kind":"page","page":77,"label":"Slide 77","section_title":"Bước 1: T ách Vai Trò Từ Artifact Day 08","extraction_method":"pdf-text-layer"},"checksum":"cc0fc01dd201a02b1d2ba84dbb801b08f816fe225e0b2d4c386b18d7bbefb35b"} -->

## Slide 77 - Bước 1: T ách Vai Trò Từ Artifact Day 08

Câu hỏi cần trả lời

- RAG agent Day 08 hiện đang làm bao nhiêu việc
khác nhau?

- Phần nào có thể tách thành worker riêng?

- Phần nào nên để supervisor quyết định?
Gợi ý tách vai trò

- Retrieval Worker: vector search + rerank

- T ool Worker: gọi API qua MCP

- Synthesis Worker: generate final answer
Kiểm tra trước khi tách Mỗi phần có thể test độc lập không? Nếu không, chưa tách đủ rõ. Supervisor có thực sự cần ra quyết định về phần đó không? Nếu không, tách ra là dư thừa. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 64 / 70

---

<!-- chiron-source-span: {"source_span_id":"e35d95eb-6e7c-5559-a027-b1fb4d57b7c7","locator":{"kind":"page","page":78,"label":"Slide 78","section_title":"Bước 2: Thiết Kế Shared State","extraction_method":"pdf-text-layer"},"checksum":"ef5d0e198825b0e2800acecaa80b4688002bbd4197f6726cb6266b3da636be2b"} -->

## Slide 78 - Bước 2: Thiết Kế Shared State

```text
class Day09State(TypedDict):
```
task: str user_context: dict plan: list[str] retrieval_result: list[dict] tool_result: dict synthesis_draft: str final_answer: str status: str trace: list[dict] error: Optional[ str] Nguyên tắc thiết kế

- trace là list — luôn append, không
overwrite

- error là Optional để graceful fail

- Worker chỉ ghi vào field của mình

- Supervisor đọc tất cả, ghi plan

- Không để field “không ai biết ai sở
hữu” Giảng viên (VinUni) AICB · Ngày 9 T uần 2 65 / 70

---

<!-- chiron-source-span: {"source_span_id":"076d7be2-90fd-5f00-b51d-5f30db57fca3","locator":{"kind":"page","page":79,"label":"Slide 79","section_title":"Bước 3: Kết Nối MCP","extraction_method":"pdf-text-layer"},"checksum":"ea1bb2166242d34e51dbfe75eb566848be74c77c0a7f25bd5718a8749a408d21"} -->

## Slide 79 - Bước 3: Kết Nối MCP

Chọn một trong các lựa chọn lab

- Tùy chọn A: dùng MCP server demo có sẵn (search
hoặc weather)

- Tùy chọn B: tự viết một MCP server đơn giản với 1 tool

- Tùy chọn C: mock MCP interface với real HTTP call
Điều cần chứng minh

- Tool Worker gọi MCP để lấy dữ liệu

- Kết quả từ MCP được ghi vào shared state

- Trace ghi lại lần gọi MCP
Điều quan trọng nhất Không quan trọng tool làm gì. Quan trọng là học viên thấy đượccách agent kết nối với capability bên ngoài theo chuẩn, không phải hard-code. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 66 / 70

---

<!-- chiron-source-span: {"source_span_id":"a1498ea0-b47a-51ac-a803-e0f23ca25e5f","locator":{"kind":"page","page":80,"label":"Slide 80","section_title":"Blueprint Cần Nộp","extraction_method":"pdf-text-layer"},"checksum":"26740a8292c54927fa2d1d6757c42d92cb18bb9d18284cc0ded33ba9456b624a"} -->

## Slide 80 - Blueprint Cần Nộp

System pieces

- 1 supervisor với routing logic rõ

- 2–3 workers rõ vai trò

- 1 MCP-connected capability

- Shared state schema có trường trace
Evidence

- trace / logs đọc được

- output cuối cùng kèm source

- ghi chú: route hợp lý chưa? tại sao?

- ít nhất 1 ví dụ về worker fail gracefully
Lưu ý: Không cần build hệ enterprise. Điều cần chứng minh là việc chia vai trò giúp hệ thống rõ hơn, dễ kiểm soát hơn, và mở rộng tốt hơn. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 67 / 70

---

<!-- chiron-source-span: {"source_span_id":"dbe05786-1b83-58f8-9c92-e69d27b48b1e","locator":{"kind":"page","page":81,"label":"Slide 81","section_title":"Rubric Đánh Giá Lab 9","extraction_method":"pdf-text-layer"},"checksum":"ade9806e0a1738394ae06561c43cba7c5eed2619ac2b83ab99f4aed1fbcb07fb"} -->

## Slide 81 - Rubric Đánh Giá Lab 9

Tiêu chí Đạt (70%) T ốt (85%) Xuất sắc (100%) Phân vai trò có supervisor + 2 work- ers vai trò rõ, không over- lap tránh anti-pattern có ý thức MCP kết nối có 1 MCP call hoạt động schema rõ, trace ghi được discovery đúng, có er- ror handling Shared state state hoạt động schema đầy đủ, có trace field ownership rõ từng field Trace quality log cơ bản đủ 5 trường cần thiết actionable, dẫn tới in- sight Routing logic routing hoạt động conditional edge rõ giải thích được quyết định route Rubric dùng chung cho chấm chéo giữa các nhóm Giảng viên (VinUni) AICB · Ngày 9 T uần 2 68 / 70

---

<!-- chiron-source-span: {"source_span_id":"25d313de-30e1-5a86-86a4-319ace4df750","locator":{"kind":"page","page":82,"label":"Slide 82","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"6af5d9e24667df1c922531dbd7c8d2760b63533acb85058af72603b385335852"} -->

## Slide 82 - T ổng kết — Key T akeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Multi-agent là chia vai trò để hệ đỡ quá tải và dễ kiểm soát — chỉ dùng khi bài toán thực sự cần. 2 Supervisor-worker là pattern practical nhất để bắt đầu: supervisor route, worker chuyên một năng lực hẹp. 3 MCP nối agent với tool qua chuẩn chung;A2A cho agents giao việc cho nhau bằng message con- tract rõ. 4 LangGraph biến orchestration thành graph có state và conditional routing — dễ debug, dễ visu- alize. 5 Observability là điều kiện tiên quyết: trace tốt là dữ liệu để cải thiện hệ thống lâu dài. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 68 / 70

---

<!-- chiron-source-span: {"source_span_id":"705df2a3-4b0f-5493-9e3f-0864a0096fd5","locator":{"kind":"page","page":83,"label":"Slide 83","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"d13aac611c45e890396be19003ba7c0a82495a7b39bcec591653f09686c5a979"} -->

## Slide 83 - Tiếp theo & Bài tập

Agent UX & Thiết Kế Trải Nghiệm AI “Hệ thống đã thông minh hơn và phối hợp tốt hơn. Nhưng nếu trải nghiệm kém, user vẫn sẽ không muốn dùng. ”

- Nếu supervisor và workers
làm đúng nhưng user không hiểu chuyện gì vừa xảy ra, trải nghiệm có đủ tốt không?

- Quan sát lab hôm nay để nhận
ra chỗ nào cần transparency, confidence indicator, và human handoff rõ ràng

- Chuẩn bị 1 use case để mô tả
AI flow từ góc nhìn người dùng thay vì chỉ từ kiến trúc Giảng viên (VinUni) AICB · Ngày 9 T uần 2 69 / 70

---

<!-- chiron-source-span: {"source_span_id":"dcdfd6b1-906f-5428-9ba5-fc4dae5a0742","locator":{"kind":"page","page":84,"label":"Slide 84","section_title":"T ài Liệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"454ac971d747602f4de964397a98549aa82fe6d350359e211540f060cfe864fb"} -->

## Slide 84 - T ài Liệu Tham Khảo

1. Model Context Protocol, Official Documentation — modelcontextprotocol.io — client / server model, tools, resources, prompts.

2. LangGraph Docs, Multi-Agent T utorials— supervisor-worker orchestration, graph routing, state handling, human-in-the-loop.

3. Sumers et al. (2023), Cognitive Architectures for Language Agents (CoALA) — phân loại memory, action, và decision trong language agents.

4. Anthropic (2024), Building Effective Agents — blog post về practical patterns cho agentic systems.

5. LangSmith Documentation, Tracing & Observability — công cụ trace cho LangChain / LangGraph pipelines. Giảng viên (VinUni) AICB · Ngày 9 T uần 2 70 / 70

---

<!-- chiron-source-span: {"source_span_id":"f0f26245-7ca8-512b-87f9-becace398bd6","locator":{"kind":"page","page":85,"label":"Slide 85","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"0daafa3136aa237566c27074db3b1ef3ecf15ff45ed1ebb273cc7e76639f8fa2"} -->

## Slide 85 - Hỏi & Đáp

Một agent rất giỏi có thể làm nhiều việc. Nhưng hệ thống tốt hơn thường bắt đầu từ câu hỏi: nên chia vai trò ở đâu để dễ kiểm soát và dễ cải thiện nhất?
