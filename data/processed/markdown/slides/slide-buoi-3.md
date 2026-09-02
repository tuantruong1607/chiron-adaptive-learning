---
schema_version: 1
course_id: rag-intensive
document_id: "35a87322-6adc-5af4-9ba9-48fad57683f0"
document_version_id: "7179acc4-81a5-5ce1-a390-1b4597051613"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Từ Chatbot Đến Agentic Agent"
source_file: "slide buổi 3.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\slide buổi 3.pdf"
source_sha256: "f5cd8a14c019075ed2f6e1ba35dae7a2d1e39bd206b26cb9cdf1b1636db3f26f"
parser_version: chiron-structured-markdown-v1
page_count: 46
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":46}"
language: vi
---

# Từ Chatbot Đến Agentic Agent

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"19e8f019-9cf5-5b38-a4dd-f0fc3a88fd23","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Từ Chatbot Đến Agentic Agent","extraction_method":"pdf-text-layer"},"checksum":"9945d631f1e9b0226b355224444fd1fa1afaa676b3182f216ded5950cfb683fb"} -->

## Slide 1 - Từ Chatbot Đến Agentic Agent

AICB-P1 · Ngày 3 · Design Pattern ReAct T ên Giảng Viên VinUniversity · Phase 1 · T uần 1 · 17/03/2026

---

<!-- chiron-source-span: {"source_span_id":"57dbf940-560f-5f1e-a9ae-53fa891fd0c1","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"4fc41fa3b434877593530eccca8821eb0b8ab57e71ea6a798dc37a367a904496"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “ChatGPT là chatbot hay agent? Siri thì sao? Cursor IDE thì sao?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"804ed4f0-08ed-5bc6-9cce-553468efd6a8","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"1f9fec51526efb35af0009e7e8646620130063aca35bda41c1614b383a091d56"} -->

## Slide 3 - Nội Dung Bài Học

1. 3 Kiểu Hệ Thống AI

2. Agentic Fit Framework

3. Kiến Trúc Agent

4. ReAct Pattern

5. Agent Loop: Code Anatomy

6. Live Demo & Debug

7. Chatbot vs Agent

8. Lab 3 Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 1 / 34

---

<!-- chiron-source-span: {"source_span_id":"1f77e48f-7a8e-5e45-b4b4-132d561ccf0d","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu Ngày 3","extraction_method":"pdf-text-layer"},"checksum":"cc114263b4bcfcc3d6cddfb3013576db3ed00821f6b21e1d862479665a30f692"} -->

## Slide 4 - Mục Tiêu Ngày 3

- Phân biệt được rule-based bot, LLM chatbot, và agent

- Dùng Agentic Fit để biết khi nào nên nâng từ chatbot lên agent

- Hiểu và giải thích được vòng lặp ReAct: Thought → Action → Observation

- Build được ReAct agent đầu tiên với tools, system prompt, và safeguard cơ bản
Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 2 / 34

---

<!-- chiron-source-span: {"source_span_id":"397af108-cde1-511e-96be-151ffab658a9","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"55b695bcf3bea4e62369a7728a683691d5f40fe4fc7beea31cd410dbce3fbfd8"} -->

## Slide 5 - Deliverable Cuối Ngày

Chatbot baseline + ReAct agent cho cùng một bài toán, kèm trace và flowchart luồng xử lý

- 5 test cases để so sánh chatbot và agent

- 1 trace Thought / Action / Observation của agent

- 1 nhận định rõ: khi nào chatbot đủ, khi nào agent vượt trội
Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 3 / 34

---

<!-- chiron-source-span: {"source_span_id":"f5ce323e-54a3-5bc1-99f1-9c288bf2ea5a","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"3 Kiểu Hệ Thống AI","extraction_method":"pdf-text-layer"},"checksum":"3532da5b006c7ac1455bf7ec8c948f797a0f52fe1db877f504b280a34b508430"} -->

## Slide 6 - 3 Kiểu Hệ Thống AI

01 T ừ bot có rule đến agent có khả năng lập kế hoạch và dùng công cụ

---

<!-- chiron-source-span: {"source_span_id":"88b9c348-dd30-54e8-947a-c414a5fd2bc3","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Spectrum: Bot → Chatbot → Agent","extraction_method":"pdf-text-layer"},"checksum":"4dd1607d516e517d9f9c11bd570316a8e56b1935ab659d5dfd28a1d8bce12fb1"} -->

## Slide 7 - Spectrum: Bot → Chatbot → Agent

Rule-based Bot If/else cứng predictable LLM Chatbot Trả lời thông minh nhưng chủ yếu 1 lượt Reactive Agent Dùng tools + loop quan sát theo từng bước Autonomous Agent Long-horizon goal nhiều quyết định liên tiếp Khả năng thích nghi, tool use, memory, risk tăng dần Không phải mọi thứ dùng LLM đều là agent. Agent chỉ xuất hiện khi hệ thống phải quyết định, hành động, quan sát kết quả, rồi lặp lại. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 4 / 34

---

<!-- chiron-source-span: {"source_span_id":"ccf6fa54-4e81-59d6-9c09-383b164eb897","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"So Sánh 3 Kiểu Hệ Thống AI","extraction_method":"pdf-text-layer"},"checksum":"cdfed85f27da2124d13d18264564b6ec4b50e4e85ebb9939984f0a7e65605d77"} -->

## Slide 8 - So Sánh 3 Kiểu Hệ Thống AI

Tiêu chí Rule-based Bot LLM Chatbot Agent Cách xử lý If/else cố định Sinh câu trả lời tốt theo context Plan → act → ob- serve → adapt Flexibility Thấp Trung bình Cao Memory Gần như không có Ngắn hạn trong con- text Ngắn hạn + có thể thêm long-term memory Tool use Hard-coded Có thể gọi tool theo chỉ định Chủ động chọn tool theo bước tiếp theo Cost Thấp nhất Trung bình Cao hơn do loop và nhiều calls Risk Logic dễ kiểm soát Hallucination / for- mat drift Hallucination + tool misuse + loop Ví dụ phù hợp Menu IVR, form vali- dation FAQ, support cơ bản Booking, research, coding assistant So sánh trực quan để chọn đúng mức độ phức tạp Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 5 / 34

---

<!-- chiron-source-span: {"source_span_id":"f8329bc1-9a6d-51ea-9aef-0121121d9a6d","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Ví Dụ Nhanh: Cùng Một Câu Hỏi, 3 Mức Độ Hệ Thống","extraction_method":"pdf-text-layer"},"checksum":"e50ddd2e5057af2213078c5841c8eb9c619aa62afdf17ee60909a05d74cfe62b"} -->

## Slide 9 - Ví Dụ Nhanh: Cùng Một Câu Hỏi, 3 Mức Độ Hệ Thống

Bài toán: “Tìm vé HAN → HCM dưới 2 triệu, rồi gợi ý mang gì nếu trời mưa.” Bot có rule

- Trả menu lựa chọn cố định

- Không search được dữ liệu mới

- Không tổng hợp nhiều điều kiện
LLM chatbot

- Viết câu trả lời mượt

- Nhưng không tự truy vấn giá vé
thật Reactive agent

- Tách goal thành 2 việc: tìm vé +
check thời tiết

- Gọi từng tool theo bước

- So sánh kết quả rồi trả lời gộp
Lưu ý: Nếu bài toán không cần dữ liệu mới, nhiều bước, hay quyết định động, agent thường là overkill. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 6 / 34

---

<!-- chiron-source-span: {"source_span_id":"179a4c2d-abab-5c80-bc87-3c3b3009dfc3","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Agentic Fit Framework","extraction_method":"pdf-text-layer"},"checksum":"17eab981f1f0f72be4d791bb5e8753aa1c09424565f50baded49fa425c3840f6"} -->

## Slide 10 - Agentic Fit Framework

02 4 tiêu chí để biết bài toán có thật sự cần agent hay không

---

<!-- chiron-source-span: {"source_span_id":"ed121970-3cef-5330-b5b2-c095c8bd8bc6","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"4 Tiêu Chí Agentic Fit","extraction_method":"pdf-text-layer"},"checksum":"33a73203d0aeb8704c517c9d924eae78c783f090f919e1b5b67aefa77a67f55b"} -->

## Slide 11 - 4 Tiêu Chí Agentic Fit

1. Multi-step Reasoning Bài toán có cần chia thành nhiều bước phụ thuộc nhau không?

2. T ool Interaction Hệ thống có cần gọi search, API, database, calculator, browser, file system...?

3. Dynamic Decision Mỗi bước tiếp theo có phụ thuộc vào kết quả vừa quan sát không?

4. Long Horizon Hệ thống có phải giữ mục tiêu xuyên suốt qua nhiều vòng lặp hoặc nhiều state không? Nếu đa số tiêu chí chỉ ở mức 1–2/5, hãy bắt đầu bằng chatbot hoặc workflow đơn giản. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 7 / 34

---

<!-- chiron-source-span: {"source_span_id":"3736c41a-00d1-58ae-a610-d655b8b2b79b","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Scoring Matrix: Có Cần Agent Không?","extraction_method":"pdf-text-layer"},"checksum":"73e95261134084b6f6ed9ab8af5c1d5c71f0204b345708db7ae0b74028da262a"} -->

## Slide 12 - Scoring Matrix: Có Cần Agent Không?

Use case Reasoning T ool use Dynamic deci- sion T ổng FAQ nội bộ HR 1 1 1 3 Tóm tắt hợp đồng và highlight risk 3 2 2 7 Booking assistant du lịch 4 5 4 13 Research agent tìm đối thủ cạnh tranh 4 4 4 12 Code assistant có test & fix loop 5 5 4 14 Gợi ý đọc điểm: 0–5 = chatbot/rule đủ 6–10 = augmented chatbot 11+ = agent đáng thử Chấm nhanh theo thang 1–5 cho từng tiêu chí Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 8 / 34

---

<!-- chiron-source-span: {"source_span_id":"b44734e1-09a5-567e-8878-958d41baaaaf","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Anti-Patterns: Khi Dùng Agent Là Sai Bài","extraction_method":"pdf-text-layer"},"checksum":"ba347395df90ffef40667312e6dbaea380477dd00e5acd7736ba2061a0f1993a"} -->

## Slide 13 - Anti-Patterns: Khi Dùng Agent Là Sai Bài

- Bài toán 1 bước: hỏi đáp, tra FAQ, phân loại cơ bản

- Không có tool nào để gọi: agent chỉ “suy nghĩ” nhưng không hành động
được

- Mọi thứ phải 100% deterministic: mỗi sai sót đều rất đắt

- Chi phí latency không chấp nhận được: loop 3–5 bước là đã quá chậm

- ✓ Nguyên tắc: luôn benchmark rule / workflow / chatbot trước khi mở agent
loop Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 9 / 34

---

<!-- chiron-source-span: {"source_span_id":"6dba2e9c-06ed-5235-ad28-8c16c607c499","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Case Study: Chatbot Đủ Hay Cần Agent?","extraction_method":"pdf-text-layer"},"checksum":"a639494cbd4387a3cbd5d29524fd7b86e84a795a9a57904e94b7dccb7e3b060f"} -->

## Slide 14 - Case Study: Chatbot Đủ Hay Cần Agent?

Customer FAQ

- Câu hỏi lặp lại, intent khá ổn định

- Chủ yếu retrieve policy rồi trả lời

- Có thể thêm RAG nhưng chưa
cần autonomy

- Best fit: chatbot có retrieval
Booking Assistant

- Nhiều ràng buộc: thời gian, ngân
sách, preference

- Phải search, so sánh, hỏi lại, rồi
chốt phương án

- Bước sau phụ thuộc kết quả bước
trước

- Best fit: reactive agent có tool
use Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 10 / 34

---

<!-- chiron-source-span: {"source_span_id":"694dd6f0-9901-5bbf-9750-0bc017924295","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Từ Anthropic: Agent Patterns Nên T ăng Dần Theo Nhu Cầu","extraction_method":"pdf-text-layer"},"checksum":"5b3d2e746c5308c246d73cd0100891b76bb9db25331eef8d0c4a8a08fe631c29"} -->

## Slide 15 - Từ Anthropic: Agent Patterns Nên T ăng Dần Theo Nhu Cầu

Augmented LLM Prompt + docs + tools Prompt Chaining Bước nối tiếp rõ ràng Routing Chọn path / specialist Orchestrator Worker Phân việc rồi tổng hợp Agent T ự quyết nhiều bước Bắt đầu từ cấu trúc đơn giản nhất đủ dùng. Agent là pattern mạnh nhưng cũng đắt nhất về cost, eval, guardrails, và vận hành. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 11 / 34

---

<!-- chiron-source-span: {"source_span_id":"ca203055-a74e-57b2-a8f2-01cfd9320311","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Kiến Trúc Agent","extraction_method":"pdf-text-layer"},"checksum":"ce05e0ed0375b7f900dbeefc5ba4490d9c4aec5b74b817636be38418ec4f5376"} -->

## Slide 16 - Kiến Trúc Agent

03 Perception, reasoning, action, memory và luồng thông tin giữa các khối

---

<!-- chiron-source-span: {"source_span_id":"92236cd1-76bf-55aa-b146-4236ea6c29d7","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Kiến Trúc Agent: Từ Trong Ra Ngoài","extraction_method":"pdf-text-layer"},"checksum":"94578cb3676302b7731ef9b37118411b4fed703cdadf9356050ae193096bd6e7"} -->

## Slide 17 - Kiến Trúc Agent: Từ Trong Ra Ngoài

Reasoning LLM Core Perception User input T ool results Action API / Search Final answer Short-term Memory Context window Long-term Memory Store / DB Input từ môi trường State và memory giúp agent không “mất mạch”

- Perception: agent nhận text,
tool output, feedback

- Reasoning: phân tích trạng thái
và chọn bước tiếp theo

- Action: gọi tool hoặc trả lời
user

- Memory: giữ goal, facts, và
intermediate results 4 khối kiến trúc thường kéo theo 4 nhóm cost chính: token, storage, API, và latency. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 12 / 34

---

<!-- chiron-source-span: {"source_span_id":"0f53dc45-7218-52e4-b05d-697721a1793b","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Memory: Short-term vs Long-term","extraction_method":"pdf-text-layer"},"checksum":"7fec4550f29e2e2d5651d0482e9afd07895852933f42e53071fec0e9089e6abe"} -->

## Slide 18 - Memory: Short-term vs Long-term

Short-term memory

- Nằm trong context window

- Dùng cho task hiện tại

- Rẻ để implement, nhưng dễ đầy
Phù hợp khi

- Cuộc hội thoại ngắn

- Goal chỉ kéo dài vài bước
Long-term memory

- Lưu facts, preferences, hay state
ngoài context

- Có thể là DB, vector store,
key-value store

- Cần retrieval strategy và
permission model Lưu ý: Không phải thêm memory là agent giỏi hơn. Memory chỉ có ích khi chiến lược đọc/ghi và quyền truy cập được thiết kế rõ. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 13 / 34

---

<!-- chiron-source-span: {"source_span_id":"1a9a2f9f-805b-57ba-8117-13d6fd1b9251","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"T ool Calling = T ay Chân Của Agent","extraction_method":"pdf-text-layer"},"checksum":"1dab1f46d9230cf5745183321de17f02ec84a27428c1345635d86fdded320812"} -->

## Slide 19 - T ool Calling = T ay Chân Của Agent

User Goal LLM T ool Call API / DB / Search JSON / args observation final answer

- Tool definitions phải rõ input / output / error mode

- Agent mạnh lên nhờ tool, nhưng cũng dễ fail hơn vì external dependency

- Tool calling là cầu nối giữa reasoning trong model và hành động ngoài thế
giới thực Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 14 / 34

---

<!-- chiron-source-span: {"source_span_id":"df2f9e75-6b22-58fd-a3a7-dddbddac8da8","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"ReAct Pattern","extraction_method":"pdf-text-layer"},"checksum":"812aabc560fd474d0f8d4937d67fc2248d74bd2593003670c26a9b1512a97afd"} -->

## Slide 20 - ReAct Pattern

04 Reasoning + Acting: cách đơn giản nhất để biến LLM thành agent có thể debug được

---

<!-- chiron-source-span: {"source_span_id":"494fd50d-5ef4-570a-bb47-3a79fe769f60","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Định Nghĩa","extraction_method":"pdf-text-layer"},"checksum":"ae33b00aa544e528c28cd831344b267e0f6765c4a20f74414f0cc9c9c9993e9c"} -->

## Slide 21 - Định Nghĩa

ReAct = Reasoning + Acting ReAct là pattern kết hợp suy luận theo từng bước với gọi công cụ và quan

### sát kết quả. Thay vì trả lời ngay, agent sẽ lặp qua các bước

- Thought: mình đang thiếu gì, nên làm gì tiếp?

- Action: gọi tool nào, với tham số nào?

- Observation: kết quả trả về là gì?

- Lặp lại đến khi đủ thông tin để trả lời hoặc gặp điều kiện dừng
Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 15 / 34

---

<!-- chiron-source-span: {"source_span_id":"26736e03-f728-54e3-acb1-b141f7f58b6c","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"ReAct Loop: Thought → Action → Observation","extraction_method":"pdf-text-layer"},"checksum":"c59202292160c20b4dfaecdc1f203076bf4fc6392021064fe1829442134b7216"} -->

## Slide 22 - ReAct Loop: Thought → Action → Observation

User Input Thought phân tích bước tiếp Action tool_name(args) Observation kết quả tool Final Answer chưa đủ đủ ReAct mạnh vì trace lý do hành động được bộc lộ ra ngoài, giúp con người debug và can thiệp dễ hơn so với chỉ nhìn final answer. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 16 / 34

---

<!-- chiron-source-span: {"source_span_id":"6af849d9-a652-5e85-8f7f-50a7f5fdc512","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Trace Ví Dụ: Tìm Chuyến Bay HAN → HCM (1/2)","extraction_method":"pdf-text-layer"},"checksum":"52da7f42aaf7b9b2638ded8c80588d031d6c7eca0235200c33d2776888258f4a"} -->

## Slide 23 - Trace Ví Dụ: Tìm Chuyến Bay HAN → HCM (1/2)

Thought 1: Tôi cần tìm chuyến bay sáng mai từ HAN tới HCM dưới 2 triệu. Action 1: search_flights(origin=”HAN”, destination=”SGN”, date=”2026-03-18”, max_price=2000000) Observation 1: Có 2 lựa chọn phù hợp: VietJet 06:10 giá 1.75M, Vietnam Airlines 08:20 giá 1.95M. Thought 2: User cũng hỏi về trang phục nếu trời mưa. Tôi cần check thời tiết tại HCM. Action 2: get_weather(city=”Ho Chi Minh City”, date=”2026-03-18”) Mỗi Thought nên làm rõ agent còn thiếu gì; mỗi Action phải chỉ ra tool và args đủ cụ thể để kiểm tra. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 17 / 34

---

<!-- chiron-source-span: {"source_span_id":"aa792503-dd0e-525a-a335-1173947a23df","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Trace Ví Dụ: Tìm Chuyến Bay HAN → HCM (2/2)","extraction_method":"pdf-text-layer"},"checksum":"287871fbf4dda47f0be68dc1a63c29eb99041d2f66824f2eeea1d948f8daf277"} -->

## Slide 24 - Trace Ví Dụ: Tìm Chuyến Bay HAN → HCM (2/2)

Observation 2: Nhiệt độ 27–32C, xác suất mưa 70%. Thought 3: Tôi đã có cả lựa chọn chuyến bay và dữ liệu thời tiết. Có thể kết luận. Final Answer: Gợi ý chuyến 06:10 giá 1.75M; mang áo mỏng, giày dễ khô, ô gập hoặc áo mưa nhẹ. Điểm mạnh không chỉ là answer tốt hơn, mà là con người nhìn được agent đã hành động dựa trên quan sát nào. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 18 / 34

---

<!-- chiron-source-span: {"source_span_id":"d4f5133f-5201-539f-9c6b-edc7dc2fff37","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"ReAct T ốt Ở Điểm Nào?","extraction_method":"pdf-text-layer"},"checksum":"f115d8b9912b994425ae5eebf4dc1103ee5b031c623c518c0181640e6a272f66"} -->

## Slide 25 - ReAct T ốt Ở Điểm Nào?

Ưu điểm

- Dễ đọc trace và debug

- T ự quyết được bước tiếp theo từ
observation

- Phù hợp các bài toán search /
booking / investigation / coding

- Có thể cài safeguard ở từng vòng
lặp Giới hạn

- Tốn nhiều token và latency hơn
chatbot

- Dễ loop hoặc gọi sai tool

- Cần eval theo trace, không chỉ
final answer

- Không phù hợp bài toán đơn giản
hoặc cần deterministic tuyệt đối Lưu ý: ReAct dễ bắt đầu nhất, nhưng khi hệ thống nhiều nhánh hơn, nên chuyển sang graph/state machine rõ ràng. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 19 / 34

---

<!-- chiron-source-span: {"source_span_id":"39c9dfe6-6f89-5ece-a0e3-0392dd099991","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Agent Loop: Code Anatomy","extraction_method":"pdf-text-layer"},"checksum":"bc27d4ae98dbbfb957c60a66f2a753c8c055552fb1f8c4430f894c6df9dcabf4"} -->

## Slide 26 - Agent Loop: Code Anatomy

05 T ừ prompt, tool registry, đến loop control và framework hóa

---

<!-- chiron-source-span: {"source_span_id":"67655c35-1499-5034-974b-4dc5987728a3","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Pseudocode: Agent Loop T ối Thiểu","extraction_method":"pdf-text-layer"},"checksum":"3180e49809e4f0d86c509603e63c8077e7bb5ded97ab12f781e89106bd41d488"} -->

## Slide 27 - Pseudocode: Agent Loop T ối Thiểu

messages = []

### for step in range(MAX_ITERATIONS)
output = call_model( system=SYSTEM_PROMPT, messages=messages, tools=TOOLS, )

### if output.type == "final_answer"

```text
return output.content
result = run_tool(output.name, output.args)
messages += [
output.as_message(),
tool_message(output.name, result),
```
]

```text
return "Stopped: max iterations reached"
Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 20 / 34
```

---

<!-- chiron-source-span: {"source_span_id":"431c0a8f-6c53-503a-84bc-08554c307440","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"System Prompt Cho ReAct Agent","extraction_method":"pdf-text-layer"},"checksum":"323e59fd0e79d51efc0ed708e8c5218d4e76c0430ae5f5871f2f2df750ecf887"} -->

## Slide 28 - System Prompt Cho ReAct Agent

SYSTEM_PROMPT = """ You are a travel planning agent.

### Your job
- Break the user goal into smaller steps
- Use tools when fresh information is required
- Think briefly, then choose the best next action
- Stop when you have enough evidence to answer

### Rules
- Never invent tool results
- If a tool fails, explain the failure and try a fallback
- Keep internal thoughts short and actionable
- Output either a tool call or a final answer
""" Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 21 / 34

---

<!-- chiron-source-span: {"source_span_id":"38ac5fc7-1a7f-502c-956f-a1801ae9f585","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"T ool Registry: Khai Báo “T ay Chân” Cho Agent","extraction_method":"pdf-text-layer"},"checksum":"ab998b2f93f4e4d378386818d36e32334b7d90c112d6f39d34142b7632056e5d"} -->

## Slide 29 - T ool Registry: Khai Báo “T ay Chân” Cho Agent

```text
TOOLS = {
"get_weather": {
```
"description": "Weather by city/date", "args": [ "city", "date"], },

```text
"search_flights": {
```
"description": "Flights by route/date/budget", "args": [ "origin", "destination", "date", "max_price"], }, } Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 22 / 34

---

<!-- chiron-source-span: {"source_span_id":"f72f8779-89e0-5bf7-9ec6-a62176f5776e","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Max Iterations Safeguard: Tránh Agent Đi Vòng","extraction_method":"pdf-text-layer"},"checksum":"65198ba586679ff625d4e2e53873e663ca39649b81166023e59b82b1afcb8d37"} -->

## Slide 30 - Max Iterations Safeguard: Tránh Agent Đi Vòng

Cần guardrails gì?

- Giới hạn số vòng lặp

- Timeout cho từng tool

- Budget token / cost trần

- Retry có kiểm soát

- Fallback sang human hoặc
chatbot Dấu hiệu loop

- lặp lại cùng một tool call

- hỏi lại thông tin đã có

- reasoning không tiến thêm

- observation không thay đổi nhưng
vẫn tiếp tục Khi output không tiến triển, cùng một tool bị gọi lặp lại, hoặc observation không đổi mà agent vẫn tiếp tục, cần dừng loop và fallback. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 23 / 34

---

<!-- chiron-source-span: {"source_span_id":"b7b97c04-63d4-5600-a50e-77ed5d52bb9e","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Từ ReAct Đến LangGraph","extraction_method":"pdf-text-layer"},"checksum":"3211d34f231517ad833154e944db96ba9001c37132bff375095207fffb7b4712"} -->

## Slide 31 - Từ ReAct Đến LangGraph

State Input LLM Node T ool Node Conditional Edge Final Answer tool call observation continue done

- ReAct loop bằng tay phù hợp để học bản chất

- LangGraph giúp biểu diễn state, nodes, edges, conditional routing rõ hơn

- Khi workflow nhiều nhánh hoặc cần persist state, graph approach dễ
maintain hơn loop ad-hoc Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 24 / 34

---

<!-- chiron-source-span: {"source_span_id":"b93f8019-ddb6-5c60-907b-329ad2547781","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Live Demo & Debug","extraction_method":"pdf-text-layer"},"checksum":"85933be40d9c594a839e9a8a628378fc00b926c26b22488db8bc7d3b132314e0"} -->

## Slide 32 - Live Demo & Debug

06 Build agent tra cứu thời tiết và gợi ý trang phục ngay trên lớp

---

<!-- chiron-source-span: {"source_span_id":"1da838ea-06f1-53e8-bec5-cd08f1f167eb","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Kịch Bản Live Demo","extraction_method":"pdf-text-layer"},"checksum":"866ae27dca788bea4768096ea79d955602f43f3843e4c2357b7cf9db1dfc06a6"} -->

## Slide 33 - Kịch Bản Live Demo

1. Định nghĩa 2 tools: get_weather và recommend_outfit

2. Viết system prompt: agent chỉ được kết luận khi đã có dữ liệu thời tiết

3. Chạy loop và đọc trace Thought / Action / Observation

4. Cố tình tạo lỗi: tool timeout hoặc agent chọn sai outfit

5. Debug: sửa prompt, sửa tool description, hoặc thêm safeguard Cho học viên thấy agent fail ở đâu và vì sao trace lại quan trọng hơn một final answer “trông có vẻ đúng”. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 25 / 34

---

<!-- chiron-source-span: {"source_span_id":"c07a1dbd-552c-51a4-8c0e-c22a327fe3fd","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Code Demo: 2 T ool T ối Thiểu","extraction_method":"pdf-text-layer"},"checksum":"5cc40959a5cf90353197740f1bb41066d0da6a717340b122fa8a3e1139a1abad"} -->

## Slide 34 - Code Demo: 2 T ool T ối Thiểu

```text
def get_weather(city: str, date: str) -> dict:
return {
```
"city": city, "date": date, "temperature_c": [27, 32], "rain_probability": 0.7, }

```text
def recommend_outfit(temp_high: int, rain_probability: float) -> str:
```

### if rain_probability > 0.5

```text
return "Ao mong, giay de kho, mang theo o gap."
```

### if temp_high > 30

```text
return "Ao nhe, thoang, uu tien vai cotton."
return "Trang phuc thoai mai, co the mang ao khoac nhe."
Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 26 / 34
```

---

<!-- chiron-source-span: {"source_span_id":"1d0621a3-3d70-5d1e-8a8f-2585215ea637","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Debug Checklist Khi Agent Lỗi","extraction_method":"pdf-text-layer"},"checksum":"507341687d158c3dad4f8501c1d13050da1c45732209a5120a9baf1f94c4ca76"} -->

## Slide 35 - Debug Checklist Khi Agent Lỗi

Nhìn vào trace trước

- Thought có đúng mục tiêu không?

- Agent chọn đúng tool chưa?

- Args truyền vào có hợp lệ không?

- Observation có bị thiếu field quan
trọng không? 4 nơi thường phải sửa

- Tool description quá mơ hồ

- System prompt thiếu rule dừng

- Không có safeguard cho retry /
loop

- Evaluation chỉ chấm final answer,
không chấm trace Lưu ý: Agent debugging gần với debugging distributed system hơn là chỉ prompt tuning. Ta phải nhìn cả model, tool, state, và orchestration. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 27 / 34

---

<!-- chiron-source-span: {"source_span_id":"81f00cc9-3ce0-5d7c-9840-1ef30c58838d","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Chatbot vs Agent","extraction_method":"pdf-text-layer"},"checksum":"f1007583e57470307f31cd8f9b5faa91628342b332d195363f5af8cee74c85d3"} -->

## Slide 36 - Chatbot vs Agent

07 Khi nào mỗi loại thắng và tại sao hybrid pattern thường thực dụng nhất

---

<!-- chiron-source-span: {"source_span_id":"68645e4d-46a8-53f1-ad75-c4e0e09edded","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Khi Nào Chatbot Thắng, Khi Nào Agent Thắng?","extraction_method":"pdf-text-layer"},"checksum":"8e1cee314b795f316dc3cfff67fdcb0693b1ada36be94777455028acf24047ce"} -->

## Slide 37 - Khi Nào Chatbot Thắng, Khi Nào Agent Thắng?

Khía cạnh Chatbot thắng Agent thắng Tác vụ FAQ, support đơn giản, nội dung 1 lượt Booking, research, coding, data analysis nhiều bước Tốc độ Nhanh, ít round-trip Chậm hơn do loop và tool calls Cost Thấp hơn, predictable hơn Cao hơn nhưng đổi lại xử lý được bài toán khó hơn Kiểm soát Dễ hơn, ít state Khó hơn vì cần orchestration và eval theo trace UX Phản hồi nhanh, đơn giản Tạo cảm giác “làm việc giúp bạn” nếu làm tốt Bắt đầu bằng chatbot là lựa chọn mặc định tốt Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 28 / 34

---

<!-- chiron-source-span: {"source_span_id":"047acc09-2248-542d-b9c0-5d7e38ac70e6","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Hybrid Pattern: Thực Dụng Hơn Cực Đoan","extraction_method":"pdf-text-layer"},"checksum":"42aea9f4c84f7d33e9bbb40d0b8d620e893b1f84ad96aaed95381fc34710ff02"} -->

## Slide 38 - Hybrid Pattern: Thực Dụng Hơn Cực Đoan

User Query Intent / Triage Simple Chatbot path Agent path Human / Escalation simple multi-step fallback Không cần chọn một phe. Thiết kế tốt thường là: triage nhanh, câu đơn giản đi chatbot path, câu phức tạp mới mở agent loop. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 29 / 34

---

<!-- chiron-source-span: {"source_span_id":"4b00f7de-c01f-560e-ade0-71b8f2edbb1d","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Thực Hành","extraction_method":"pdf-text-layer"},"checksum":"a544e208f8bcd4de04626726584630505203c631d17a585953674458e6b9d476"} -->

## Slide 39 - Thực Hành

08 Lab 3: Chatbot vs Agent — Hands-on Comparison

---

<!-- chiron-source-span: {"source_span_id":"e20abf46-9e55-5893-acf0-e565937efb67","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Cách Chạy Lab 3","extraction_method":"pdf-text-layer"},"checksum":"39400183aafb6ae52d59a08d8bfc9d8686172eb674fd206b245d625abcd23401"} -->

## Slide 40 - Cách Chạy Lab 3

1. Chọn lại use case từ Ngày 2 hoặc một use case tương đương

2. Build chatbot baseline cho bài toán đó

3. Nâng cấp thành ReAct agent có ít nhất 1–2 tools

4. Chạy 5 test cases giống nhau trên cả hai hệ thống

5. Vẽ flowchart và ghi nhận nơi agent thực sự tạo thêm giá trị Nhờ AI generate scaffolding code, nhưng nhóm phải tự sửa system prompt, tool description, và điều kiện dừng. Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 30 / 34

---

<!-- chiron-source-span: {"source_span_id":"ffed3d43-61cc-51ab-8629-e6717057a96c","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Lab #3","extraction_method":"pdf-text-layer"},"checksum":"77196e91f6b385f455c4a2ecc6696446a896f96d80ee6805796cf8e980a3a926"} -->

## Slide 41 - Lab #3

Mục tiêu: Build chatbot baseline rồi nâng cấp thành ReAct agent cho cùng một use case để so sánh trực tiếp Deliverable: Nộp cuối buổi: chatbot + agent + 5 test cases + 1 trace + 1 flowchart Bonus: thêm fallback path hoặc human escalation Thời gian: 150 phút Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 31 / 34

---

<!-- chiron-source-span: {"source_span_id":"24d2d6e0-a07f-5e8d-ad50-f907c517b3eb","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"T ổng Kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"3a0c61da739b4b7cac59a778cf6ddc4984d5d0ebc95e073821dbfaa0cd201d73"} -->

## Slide 42 - T ổng Kết — Key T akeaways

1 Agent không phải “chatbot thông minh hơn”; agent = LLM + reasoning + tools + memory/state 2 ReAct là pattern dễ học nhất để biến LLM thành hệ thống biết hành động và dễ debug 3 Chỉ dùng agent khi bài toán có multi-step reasoning, tool use, dynamic decisions, long horizon 4 Trong production, guardrails, trace, và evaluation quan trọng không kém model quality Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 32 / 34

---

<!-- chiron-source-span: {"source_span_id":"60bc85ac-aa0c-5c57-9e9e-990511c1b452","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"b5b1f0c214db6073622a9cc189a01f87cfc1c8d4c9b0c6cfae41ec952d1a85b9"} -->

## Slide 43 - Tiếp theo & Bài tập

Prompt Engineering & T ool Call- ing “Ngày mai ta đi sâu hơn vào cách viết system prompt production- grade và mô tả tools để agent dùng đúng ý.”

- Đọc lại trace lab hôm nay và
tìm 1 chỗ agent ra quyết định chưa tối ưu

- Thử viết lại tool description
theo hướng rõ input, output, và failure mode hơn Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 33 / 34

---

<!-- chiron-source-span: {"source_span_id":"66d58f36-2757-58cf-81d7-88e81091b2a6","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"T ài Liệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"211ad6b5df7b5b82e7d233352ecc863b12f2c420130a208285d9892617e375c2"} -->

## Slide 44 - T ài Liệu Tham Khảo

1 Y ao et al.ReAct: Synergizing Reasoning and Acting in Language Models. arXiv:2210.03629, 2023. 2 Anthropic. Building effective agents. anthropic.com/research/building-effective-agents 3 LangChain / LangGraph docs. Quickstart and Introduction. langchain-ai.github.io/langgraph Giảng viên (VinUni) AICB · Ngày 3 17/03/2026 34 / 34

---

<!-- chiron-source-span: {"source_span_id":"b5e5da49-6d48-5ca0-9646-4c9c22b2be42","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"38a6a4f95b7ec66a302a8970e216edcf29853cbed692822f5bd7027a2003aa7e"} -->

## Slide 45 - Hỏi & Đáp

Use case nào trong công việc của bạn chỉ cần chatbot, và use case nào thực sự cần agent loop?

---

<!-- chiron-source-span: {"source_span_id":"c93ca7eb-7971-5365-847d-d0129f29346b","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"c512986259d37dc95ee0a6ccd21df287e13377916631c86c59b91332bd0f6251"} -->

## Slide 46 - Cảm ơn!

Email: lecturer@vinuni.edu.vn Slides & tài liệu: github.com/aicb-vinuni Lab template: bit.ly/aicb-day03-lab
