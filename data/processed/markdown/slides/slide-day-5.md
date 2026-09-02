---
schema_version: 1
course_id: rag-intensive
document_id: "bcfc37c8-e644-533a-b1d5-1be1c8293a31"
document_version_id: "8db0641a-f58c-5456-8ca9-87d4249a9f0a"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "AI IN ACTION · NGÀY 5"
source_file: "slide day 5.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\slide day 5.pdf"
source_sha256: "514d943952129d6daa1456056d89377ae18b175bbfd06f17f72a6d64744cdb60"
parser_version: chiron-structured-markdown-v1
page_count: 62
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":60,\"ocr-tesseract-vie+eng\":2}"
language: vi
---

# AI IN ACTION · NGÀY 5

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"c6e9cf09-d970-5c16-9983-27724a24f511","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"AI IN ACTION · NGÀY 5","extraction_method":"pdf-text-layer"},"checksum":"fb060a29ef7a5d97d245800feb825872a1a62b510e40b93066247b5dafc4f381"} -->

## Slide 1 - AI IN ACTION · NGÀY 5

Thiết kế sản phẩm AI cho sự không chắc chắn Từ khả năng của model đến trải nghiệm đáng tin cậy của người dùng Instructor: Mai Anh Nguyen Blue · VinUniversity · Day 5 · 2026

---

<!-- chiron-source-span: {"source_span_id":"4c3ed6ca-04b5-53f1-8ece-cfdbe73ae670","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"Instructor","extraction_method":"pdf-text-layer"},"checksum":"f1a416212f41fc2e4b4537df539be43899a160d135a8ee9136e0b8327f6d23e0"} -->

## Slide 2 - Instructor

Mai Anh Nguyen (Blue) Generalist Product Builder 2026 FPT Long Châu (PM · Healthcare Product) 2025 Thongtincuuho.org (Co-founder) 2025 FPT Software AI Center (PM · AI Agent) 2021 - 2025 Xantus (PM · On-chain Analytics, AI Agent) 2016 - 2021 DYNO, Kalapa (PM · OCR, eKYC, Credit Scoring) Linkedin | Facebook

---

<!-- chiron-source-span: {"source_span_id":"cb68d478-52a5-52d9-9f6c-eb8237376500","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"AI IN ACTION · NGÀY 5","extraction_method":"pdf-text-layer"},"checksum":"c13cb52e86b7de63e8d0034c38fe56526f0a10c9314e06931be34ad2c58ed207"} -->

## Slide 3 - AI IN ACTION · NGÀY 5

Agenda

- AI Prototyping & MVP

- Scope & PRD cho AI feature

- Human-centered AI design

- Evals flow
Thiết kế sản phẩm AI cho sự không chắc chắn Từ prototype rẻ nhất → spec đúng → đo chất lượng bằng chu trình

---

<!-- chiron-source-span: {"source_span_id":"bb413bbd-1257-581d-9acc-c2cb540419bb","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"S E C T I O N 0 1","extraction_method":"pdf-text-layer"},"checksum":"06689694c7f3a9030a2629800c2334eec060849c7909d0f9770f93d883b0c669"} -->

## Slide 4 - S E C T I O N 0 1

AI Prototyping & MVP Test giả thuyết rẻ nhất trước khi build

---

<!-- chiron-source-span: {"source_span_id":"7d8bb03a-867e-59c1-919d-751e57ca9c42","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"High business importance","extraction_method":"pdf-text-layer"},"checksum":"b56c647795b2eae442124d531dcdf3fac33b82df871c7891e6aae4a15f305f4c"} -->

## Slide 5 - High business importance

Low business importance Strong evidence Low evidence We will gain new customers by building X Leap of faith assumptions Leap of Faith Assumptions (The Lean Startup)

- Will the customer buy this, or
choose to use it? Value risk) Khách có mua — hoặc chọn dùng — không?

- Can the user figure out how to
use it? Usability risk) User có tự biết cách dùng không?

- Can we build it? Feasibility
risk) Ta có build được không?

- Does this solution work for our
business? Business viability risk) Giải pháp này có hợp với business của ta không?

---

<!-- chiron-source-span: {"source_span_id":"fc4c1bb3-20b9-5519-8057-c3b2d8657590","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Build software: từ rất đắt → rẻ hơn nhiều","extraction_method":"pdf-text-layer"},"checksum":"5f49323863ceace1af665a46fb398936fa202dbccb5f8e085563da4f18ba77c0"} -->

## Slide 6 - Build software: từ rất đắt → rẻ hơn nhiều

Toàn bộ product lifecycle được thiết kế quanh việc "build là đắt" — khi build rẻ đi, lifecycle đó phải đổi theo.

- 
Cùng một thang "signal vs effort" — MVP và prototype giờ nằm ở chỗ trước đây chỉ có wireframe. Nguồn: Day 17 lecture — "Until recently, building software was expensive" / "Now, building software is much cheaper".

---

<!-- chiron-source-span: {"source_span_id":"eae2c4b2-f52b-50c8-a55f-ab5f1400a8eb","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Với AI, cả 3 khâu đều nhanh hơn","extraction_method":"pdf-text-layer"},"checksum":"b6c4086923f890af7aa51f20cd96b670d75c7f6963e0dfa2337b0236b1b17f53"} -->

## Slide 7 - Với AI, cả 3 khâu đều nhanh hơn

Double diamond không đổi — tốc độ đi qua nó thay đổi hoàn toàn. Nhiều ý tưởng giải pháp hơn Đồng thuận stakeholder nhanh hơn Deliver nhanh hơn, lấy feedback nhanh hơn Prototype as decision-making tools — for exploration, alignment, and validation. "If you aren't prototyping with AI, you're doing it wrong" — Microsoft CPO.

---

<!-- chiron-source-span: {"source_span_id":"84a46ebd-63da-521a-ac29-51e4c7feb371","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Thang fidelity: Sketch → Wireframe → Mockup → Prototype","extraction_method":"pdf-text-layer"},"checksum":"300621f9e17852c109b009c2696e9a29b206bf2214b18fe103f86f907c5c21fa"} -->

## Slide 8 - Thang fidelity: Sketch → Wireframe → Mockup → Prototype

Low-fidelity kiểm tra luồng & tính năng — high-fidelity kiểm tra trải nghiệm “như thậtˮ. LOW-FIDELITY HIGH-FIDELITY Đúng luồng / workflow chưa? Người dùng có thấy rõ tính năng không? Mô phỏng trông như thật Test với người dùng cuối 01 Sketch 02 Wireframe functional · structure 03 Mockup style · color 04 Prototype interactive · clickable ĐỘ TRUNG THỰC (FIDELITY) TĂNG DẦN Low-fi chốt luồng & tính năng — high-fi kiểm chứng “trông như thậtˮ với người dùng cuối. Sketch → Wireframe → Mockup → Prototype: fidelity và effort tăng dần theo từng bậc.

---

<!-- chiron-source-span: {"source_span_id":"5e65647b-46b6-5e78-89d4-cbd1151a8b08","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Prototype · Pilot · MVP · Proof-of-concept — định nghĩa cho rõ","extraction_method":"pdf-text-layer"},"checksum":"493fee6921f74f4d7849c7f6df99cda97746b2b646212cb5c3c3aa8c274a19df"} -->

## Slide 9 - Prototype · Pilot · MVP · Proof-of-concept — định nghĩa cho rõ

Trục ngang: mức độ hoàn thiện (fidelity & completion) · Trục dọc: phạm vi test (parts → whole).

---

<!-- chiron-source-span: {"source_span_id":"f1cc7bf9-6d02-5aa8-9618-b736c995fd67","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Sketch Wireframe functional, structure","extraction_method":"ocr-tesseract-vie+eng"},"checksum":"18114ac4848e3ce37b8b6ce2d07253ab148061456c51b8a5de0811d2e1253ba1"} -->

## Slide 10 - Sketch Wireframe functional, structure

— - 7 Bat C—ml s= = Lo oa G3 — iWnstszzn h Em oe c= © Watch on phone "° -—— ee 0 Zoolander ae = = sa i al = | Eee A fi l Miee I ¿ n Prototype Interactive, clickable Mockup style, color 1941 alo. uuireol ch =: =: ~ = REEL 2% Jessy J. Œœ @ peas © soit payment nao f sane luca NÓ ` > ¢ năng = 9 ' 2: SPARROW.

---

<!-- chiron-source-span: {"source_span_id":"008f7c72-954f-5bf5-9e8c-8a55d596b661","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"MVP: cách nào rẻ nhất để test được giả thuyết?","extraction_method":"pdf-text-layer"},"checksum":"189a341c5100e4f93ede6d71cbf723188ea718a852485209f6596b24e60d757b"} -->

## Slide 11 - MVP: cách nào rẻ nhất để test được giả thuyết?

Using variations for brainstorming — nhiều biến thể, rẻ, trước khi chọn một. ① 1 màn hình → 3 biến thể trong vài giờ

- 
Trước: 1 màn hình desktop duy nhất → Sau: Insight First · Momentum Mode · Sheet Reveal — cùng một bài toán, 3 hướng giải, so sánh trước khi cược vào một. ② Lát cắt mỏng xuyên suốt, không phải một tầng hoàn chỉnh Không build "bánh xe trước, xe hơi sau". Build chiếc xe đạp chạy được ngay — nhỏ nhưng đủ cả 4 tầng.

---

<!-- chiron-source-span: {"source_span_id":"cf2c54f8-c130-56bf-ae95-2fa20a33081d","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"The old way The new model","extraction_method":"ocr-tesseract-vie+eng"},"checksum":"da2cc57da189e98bcf3414c9ffc4d452a30e3f9b03c5a9891fdde89b1e815649"} -->

## Slide 12 - The old way The new model

PM > Design > Engineering PM + Design + Engineering Weeks of lag Build in hours Rigid handoffs Collaborative riffing Limited customer engagement More customer conversations

---

<!-- chiron-source-span: {"source_span_id":"72f018d5-ad7e-5e25-b5ba-c58bbf5b286a","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"MVP: build cái dùng được, không build từng mảnh","extraction_method":"pdf-text-layer"},"checksum":"eee4c08b30f7322c2ce1dd2113ed43770e6a5430b69bd49aab7a7be46ac141a6"} -->

## Slide 13 - MVP: build cái dùng được, không build từng mảnh

Not like this: từng bộ phận rời — user chưa dùng được gì. Like this: ván trượt → xe đạp → xe máy → ô tô, mỗi bước đều đi được.

---

<!-- chiron-source-span: {"source_span_id":"4b086202-1b73-5e73-8756-0e5186d3e3d7","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Wizard of Oz MVP","extraction_method":"pdf-text-layer"},"checksum":"8af77e6f587433bf03e70725fba44d4012753474717d203b9869059e6c095e25"} -->

## Slide 14 - Wizard of Oz MVP

DoorDash - "Palo Alto Delivery" 2013 Giả định: "Có ai cần giao đồ ăn từ quán địa phương không?" MVP: một trang web tĩnh + PDF menu 8 quán (không xin phép), để một số Google Voice chung (đổ chuông máy cả 4 founder). Có cuộc gọi → tự gọi đặt món, tự lái đi giao, lấy $6. Dán tờ rơi quanh Stanford — đơn đầu tiên từ khách lạ qua Google sau 45 phút. Landing page + ads — bán trước khi có sản phẩm Dựng landing page, chạy ads dù chưa có sản phẩm Khách hàng đăng ký mua → gọi điện xin lỗi rồi refund Nguồn: Tony Xu CEO DoorDash) kể lại trên Founders Podcast — davidsenra.com/episode/tony-xu.

---

<!-- chiron-source-span: {"source_span_id":"f052d8aa-4859-5ec0-8be9-849bc675ea33","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"AI Wizard of Oz MVP","extraction_method":"pdf-text-layer"},"checksum":"42113904f6b337746fcf5ea50c9faecb8f2b2c3c11b2e78ce7061faa3dedcd6c"} -->

## Slide 15 - AI Wizard of Oz MVP

This $1 billion AI startup founded by an MIT alum claimed to use AI, but its "AI" was just two founders taking notes by hand

### Giả định rủi ro nhất
"Người ta có trả tiền cho 'AI ghi chú họp' không? MVP 2 founder tham gia vào cuộc họp dưới danh nghĩa một bot AI tên "Fred" (giả kiểu Siri), ngồi gõ note bằng tay. Làm tay hơn 100 cuộc họp, thu $100/tháng cho AI Kết quả: seed $5M 10/2019 → kỳ lân $1 tỷ 6/2025 Nguồn: TechStartups, 12/11/2025 (headline trích nguyên văn) · Fireflies Blog — seed $5M 10/2019.

---

<!-- chiron-source-span: {"source_span_id":"d204c6ac-86b9-5f4a-ad09-15bcf3b23d68","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"AI development tools","extraction_method":"pdf-text-layer"},"checksum":"9f4c2c2e96f19ae4d148107b25a042b31de0a9a64e8e56cfa94c240062a53d1e"} -->

## Slide 16 - AI development tools

Phù hợp với: Prototype 1-vài trang, không có yêu cầu thiết kế quá phức tạp. Phù hợp với: Prototype có nhiều hơn 1 tính năng, có yêu cầu thiết kế cụ thể, hoặc có nhiều trang / màn hình. Phù hợp với: Người đã biết code và đang xây ứng dụng nghiêm túc, có mục tiêu đưa lên production. Microsoft CPO If you aren't prototyping with AI, you're doing it wrong

---

<!-- chiron-source-span: {"source_span_id":"b16a16b1-3209-5709-aa7d-6b36d8a1a814","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"S E C T I O N 0 2","extraction_method":"pdf-text-layer"},"checksum":"1e54a6870ddfa09c278e55b64181a1eaeaa7f2ef864b260805898f132f45ad97"} -->

## Slide 17 - S E C T I O N 0 2

Scope & PRD cho AI feature Khung 6 bước của Ailian Gan Lead PM AI, Zoom) — ví dụ Zoom meeting summary xuyên suốt

---

<!-- chiron-source-span: {"source_span_id":"84a84e14-c07f-5539-8e44-6dcc5f87cbaf","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"① Identify good use cases: AI là cây búa đi tìm cái đinh","extraction_method":"pdf-text-layer"},"checksum":"2105c250179050adaf14dd006ece2e437b6f9216ad413cbb6bd75fae629c8b7b"} -->

## Slide 18 - ① Identify good use cases: AI là cây búa đi tìm cái đinh

Team thường được giao sẵn "cây búa" AI rồi mới đi tìm bài toán. Hãy tìm đinh tốt — đừng đóng lỗ lung tung. A · HIỂU SÂU USER NEED User làm những hoạt động chính nào trong product? Pain point lớn nhất là gì — chỗ nào complex hay tedious trong flow hiện tại? Điều gì sẽ delight user tới mức họ chưa từng nghĩ tới? B · BRAINSTORM THEO LLM SKILLS User need nào cải thiện được bằng các skill của LLM summarization · question- answering · content generation · personalization · data processing · predictive insights. Nghĩ rộng: tóm tắt không chỉ PDF — còn chat, transcript, video. C · CHỌN THEO GIÁ TRỊ + MOAT Use case nào giải pain lớn nhất, tạo delight nhiều nhất? Cái nào tạo competitive moat — data nào (để train, để generate output) mà đối thủ có model tốt cũng không copy được? Ví dụ: PM tại Zoom cân các use case Scheduling — khả thi, nhưng cần biết availability & preferences của mọi người. Draft agendas — khả thi, nhưng cần input data đủ tốt mới đề xuất được agenda hay. Brainstorm ideas — khả thi, nhưng Zoom đã có sẵn sản phẩm whiteboard. Extract takeaways — THẮNG. Zoom đã có sẵn transcript · LLM rất giỏi tóm tắt · app bên thứ ba đang bán note-taking → market demand rõ ràng. PAIR Guidebook, ch. "User Needs + Defining Success" gọi đây là bước identify AI opportunities: bắt đầu từ user need, không bắt đầu từ công nghệ — câu hỏi đầu tiên luôn là "vấn đề này có thật sự cần AI không?" Nguồn: Ailian Gan — "Write a PRD for a generative AI feature" Reforge) · PAIR Guidebook, ch. "User Needs + Defining Success".

---

<!-- chiron-source-span: {"source_span_id":"73addfb3-7298-5b68-8346-310e7c37e8d4","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"② Articulate the problem: đừng nhắc chữ AI","extraction_method":"pdf-text-layer"},"checksum":"51264ef78936a9bc5b9ac4c41ffac34440933335b53d4d6ee89650b8f4df9cc0"} -->

## Slide 19 - ② Articulate the problem: đừng nhắc chữ AI

Problem statement KHÔNG được nhắc chữ AI — vấn đề của user không phải là "đời tôi thiếu AI". Hỏi: vấn đề là gì, vì sao là vấn đề, bạn biết từ đâu?

- BAD
"Users don't have an automated AI notetaker for all their meetings." Phát biểu thiếu solution = vấn đề. Giả định user cần một AI notetaker — nhưng tại sao? Không mô tả vấn đề nền hay mục tiêu của user. Hỏi "why" vài lần để đào sâu hơn. ◐ GOOD "Users want a record of the key points

```text
from their meetings, but it is tedious and
```
distracting to take thorough manual notes for every meeting." Tưởng tượng được nhiều giải pháp: thuê intern ghi note cho mọi cuộc họp? Bắt cả team ghi note chung?  AI chỉ là phương án scalable và rẻ hơn.

- EVEN BETTER
"…a record of discussion topics, key decisions, and action items… In addition, users sometimes cannot attend a meeting, and they want a quick way to catch up." Gợi ý nội dung cần focus (decisions, action items), use case phụ (người vắng mặt cần xin note), và cách consume — phải nhanh, dễ đọc. Nguồn: Ailian Gan — "Write a PRD for a generative AI feature" Reforge) · ví dụ Zoom meeting summary.

---

<!-- chiron-source-span: {"source_span_id":"39007584-a74f-5f20-9498-0737c658e56a","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"③ Define goals: goals · non-goals · success metrics","extraction_method":"pdf-text-layer"},"checksum":"8d29d0dc9989a99a24e7b4aaa2720d30c345cb8702e3d930d3a34f60ba0b7d3f"} -->

## Slide 20 - ③ Define goals: goals · non-goals · success metrics

Goals là outcome định tính gắn với problem statement — không phải solution, và cũng không nhắc AI. Ví dụ: Zoom meeting summary. GOALS · Đọc được recap đầy đủ & chính xác của cuộc họp — không cần đọc full transcript hay xem lại recording · Nhận được list action items + owners · Vắng mặt vẫn nắm được thông tin chính · Truy cập summary theo cách hợp workflow · Edit summary để sửa lỗi của LLM hoặc thêm context · Quản lý được ai xem summary Bài toán có thể giải tốt nhất mà không cần AI — goal không gắn với công nghệ. NON-GOALS · Không có customizable templates cho từng loại meeting · Không bao gồm nội dung từ screen shares, chats, calendar invite hay tài liệu liên quan Ghi rõ out-of-scope: ý tưởng cho version sau, vấn đề lâu đời feature này không giải, vấn đề kề cận cần xử lý riêng. SUCCESS METRICS — 3 TẦNG Usage ·% accounts enable base setting (setting default off) · MAU của meeting summaries ·% meetings chạy summary Quality ·% thumbs up vs thumbs down Impact (khó đo → dùng proxy) · Thời gian tiết kiệm khi không cần người ghi note ·% meetings user vắng mặt nhưng đọc summary PAIR Guidebook, ch. "User Needs + Defining Success": define success từ sớm, trước khi scope giải pháp — success của AI feature không chỉ là accuracy mà là outcome cho user. Nguồn: Ailian Gan — Reforge · ví dụ Zoom meeting summary · PAIR Guidebook, ch. "User Needs + Defining Success".

---

<!-- chiron-source-span: {"source_span_id":"8a547be7-61b9-52a8-9a5e-ddc79afbe4eb","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"④a Scope the solution: mô tả user flow end-to-end","extraction_method":"pdf-text-layer"},"checksum":"ed71bd92f8524505fd6c7e593d92ed405cdcbf60ab4641b7a717865bcfd03c82"} -->

## Slide 21 - ④a Scope the solution: mô tả user flow end-to-end

Bao gồm cả các bước KHÔNG có AI — đừng chỉ định nghĩa đoạn AI. Ví dụ: detect scheduling intent trong email xong → tự suggest giờ luôn, hay đưa user sang calendar app để hoàn tất? Click a button User bấm nút để invoke — ví dụ: summarize một chat thread. One-shot prompt Gõ prompt một lần vào text field — Notion brainstorm ý tưởng, Canva tạo graphic cho post. Pre-set prompts Prompt có sẵn để bấm — LinkedIn gợi ý takeaway questions trên mỗi post. Automated report Tự chạy theo lịch/sự kiện — Zoom meeting summary auto-start, Slack daily recap các chat bỏ lỡ. Automated suggestions Gợi ý hiện sẵn trong flow — Superhuman tóm tắt email 1 dòng, Vanta gợi ý trả lời questionnaire. Chatbot Hội thoại tự do — Intercom "Fin" trả lời support, Duolingo Roleplay luyện nói. ⚠ Đừng bắt đầu bằng chatbot User gõ gì cũng được → quality khó kiểm soát; lại dính cold start — user không biết hỏi gì, hỏi thế nào, probe tiếp ra sao. Cân nhắc các interaction non-chatbot trước. Figjam: pre-set prompt gợi ý ở mỗi bước + vẫn cho gõ free text → khỏi viết prompt từ đầu, template chất lượng hơn. Human-in-the-loop Output có thể hallucinate → quyết định sai hoặc gây hại? Thêm bước review / edit / delete trước khi share. LLM soạn draft email — user sửa rồi mới gửi, không gửi ngay. Nguồn: Ailian Gan — "Write a PRD for a generative AI feature" Reforge).

---

<!-- chiron-source-span: {"source_span_id":"f96942c8-7bec-5971-8873-d0f26a327a40","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"④b AI-specific requirements — phần PRD không có ở feature thường","extraction_method":"pdf-text-layer"},"checksum":"a89804bff1395eb0d84ee6eab505be6cfeb7e36753522d25d9bf3dd0d41ce2d6"} -->

## Slide 22 - ④b AI-specific requirements — phần PRD không có ở feature thường

① USER INPUT  CONTEXTUAL DATA Ai invoke LLM — bấm nút, gõ prompt, hay auto khi có sự kiện? LLM được đọc dữ

### liệu nào làm context — phải định ranh giới data rõ ràng
· Notion: QA đọc cả document · Loom: tạo title & chapters từ transcript · Intercom: chatbot đọc knowledge base articles · M365 Copilot: calendar + emails + docs + contacts ② LLM OUTPUT SPEC Output non-deterministic → mô tả length · tone · format · exclusion độc lập ví dụ. "What good looks like": case common · critical phải đúng · obscure vẽ ranh giới. Tip: prototype câu trả lời bằng ChatGPT/Claude (upload transcript → generate). Ví dụ Zoom — mục "Next Steps": chỉ action sau cuộc họp (không gồm việc trong meeting) · 1 action/bullet · có tên assignee · tối đa 8 · tone professional. ③ FEEDBACK MECHANISM QA tốt đến đâu cũng không lường hết cách user dùng thật → cần kênh

### feedback
Thumbs up/down — nhẹ, response rate cao, nhưng ít chi tiết vì sao tốt/xấu. Form scoring + open text — nặng, response rate thấp, nhưng giàu chi tiết; ghi rõ data nào (input + output) được gửi kèm feedback. PAIR Guidebook, ch. "Feedback + Control": feedback phải được thiết kế ngay trong spec, không gắn thêm sau khi ship — mỗi tương tác là cơ hội để hệ thống học. ④ QUALITY EVALUATION  BAR PHỤ THUỘC RISK Có HITL check trước khi publish + output tiết kiệm nhiều thời gian → chấp nhận bar thấp hơn. Sai gây quyết định tồi / hại, long-tail offensive → bar cao hơn. Auto eval: dataset mẫu → chạy task → auto score. Manual eval: PM/QA đọc mẫu bắt nuance. Tìm CONVERGENCE giữa hai cái. Nguồn: Ailian Gan — "Write a PRD for a generative AI feature" Reforge) · ví dụ Zoom meeting summary · PAIR Guidebook, ch. "Feedback + Control".

---

<!-- chiron-source-span: {"source_span_id":"894e7ed1-438c-5a73-bc2c-237f0eba9572","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Nondeterminism là mặc định — không phải edge case","extraction_method":"pdf-text-layer"},"checksum":"d8d38bb1808838f32670bd297a7ed5cb52770b6a1a81c389435c0e3776840ef4"} -->

## Slide 23 - Nondeterminism là mặc định — không phải edge case

Ba loại failure của hệ xác suất — và ba sai lầm thiết kế khiến chúng gây thiệt hại. ① Output variance Cùng một input, hai lần chạy ra hai output khác nhau. Đây là hành vi mặc định của mọi hệ probabilistic — không phải trường hợp ngoại lệ. ② Behavioral drift Release thì đúng, vài tuần sau lệch — model update, input của user đổi, prompt gặp case chưa test. Team biết qua complaint của user, không qua monitoring của mình. ③ Reasoning-level failure Retrieval đúng, tool call đúng, model trả lời trôi chảy — nhưng tổ hợp các bước ra kết quả sai. "Monitoring shows all green. But the product fails." Sai lầm ① — Giấu variance Không nút regenerate, không confidence framing → user báo "bug" cho hành vi đúng kỹ thuật. Hãy lộ ra: "Here is one way to think about this" + nút thử lại. Sai lầm ② — Acceptance criteria nhị phân "AI trả lời đúng" + 3 test case xanh → ship. Nhưng vài test case là demo, không phải distribution — nó giấu messy input và drift. Sai lầm ③ — Fallback là ý sau cùng Spec chỉ có 1 dòng "display error message". Nhưng failure trong hệ nondeterministic hiếm khi nhị phân — AI vẫn trả lời, chỉ là trả lời tệ, âm thầm bào mòn trust. Nondeterminism không phải bug để sửa — là constraint để thiết kế vòng tránh, như latency hay kích thước màn hình. Nguồn: Adaline Labs — "Designing AI Features for Nondeterminism" Nilesh Barla, 28/3/2026.

---

<!-- chiron-source-span: {"source_span_id":"459dccd7-7ecb-5b89-b19e-aa189a7b93f4","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"FALLBACK 3 TẦNG (chọn là quyết định product, ghi vào PRD):","extraction_method":"pdf-text-layer"},"checksum":"bdc897f6f96847b63245835b01ccb2bc656d06c7aecfb5b55a5843446416cc84"} -->

## Slide 24 - FALLBACK 3 TẦNG (chọn là quyết định product, ghi vào PRD):

Spec cho feature xác suất: 3 ca chuyển đổi Mỗi ca chuyển đổi thay đổi thứ bạn ship — và thứ bạn đo được sau launch. ① Từ expected output → acceptance criteria dạng tỉ lệ

- "The AI returns a correct summary." → ✓ "The AI produces a summary that passes this rubric on 90% of a representative input set." — Tỉ lệ đo được, và
biết ngay khi nó xuống dốc. ② Từ test cases → test distributions Một test case là demo. Một distribution mới là product. Bắt đầu bằng 20 case phản ánh input thật (messy, edge, ambiguous — không chỉ happy path), lớn dần từ production traces, không phải từ trực giác. ③ Từ "works" → "fails by design" Spec phải có Failure Modes section: confidence thấp thì sao? tool timeout thì sao? output ngoài ngưỡng chấp nhận thì user thấy gì? Đây là quyết định product — viết vào spec, không phải thread Slack 3 tuần sau launch. Soft fallback — output đơn giản/hẹp hơn khi confidence thấp Human handoff — case rủi ro cao/mơ hồ → chuyển người thật Silent skip — không làm gì, nhưng cũng không làm sai AI PRD thiếu acceptance threshold section = chưa phải AI PRD. Nguồn: Adaline Labs — "Designing AI Features for Nondeterminism" Nilesh Barla, 28/3/2026.

---

<!-- chiron-source-span: {"source_span_id":"9e77d7bc-1a9b-5a1c-b9c5-58b18e3410a0","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"1. Mô tả tính năng AI","extraction_method":"pdf-text-layer"},"checksum":"b8979953f57b8acd3b8fcd384d50bb083e62f8129501e374d160b9849a1663a9"} -->

## Slide 25 - 1. Mô tả tính năng AI

- Loại hệ thống

- Phương thức input:
Text/Voice

- Có trigger rõ ràng?

- Có phân định rõ input?

- Input có nhiều nghĩa

- Dạng output:

- Cách tạo response:
Generated/Selected

- Playbook tự suy ra các
kiểu lỗi, kịch bản cần test Microsoft HAX Playbook Github Playbook giúp các nhóm phát triển sản phẩm AI xác định những kịch bản kiểm thử quan trọng cần thực hiện trước khi ra mắt tính năng AI, dựa trên đặc điểm cụ thể của hệ thống đó.github.com/microsoft/HAXPlaybook

---

<!-- chiron-source-span: {"source_span_id":"6d7f450f-c5e3-501f-be5f-22bda30fb534","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Case BatchBuddy: bản đồ 9 kịch bản theo lớp lỗi","extraction_method":"pdf-text-layer"},"checksum":"03e29e0fc7350ea536492eb7af96e765199450bd3649894873196813747cc8e9"} -->

## Slide 26 - Case BatchBuddy: bản đồ 9 kịch bản theo lớp lỗi

Chatbot kênh #batch02-general · source of truth: deadline 2000 22/06/2026 config · trigger: bot tự đoán khi nào nói Correct operation 1 đường chạy đúng User hỏi deadline → bot trả đúng 2000 22/06 Không nói khi không cần Input errors 1 typo trong câu hỏi truncation substitution insertion swapping Trigger errors 3 bot tự đoán khi nào nói missed — đáng nói thì im spurious — không ai hỏi vẫn nói delayed — nói quá trễ Delimiter errors 0 “0ˮ cũng là một câu trả lời có ý nghĩa — lớp này được xét và loại trừ, không phải bị quên. Response generation 4 sinh câu trả lời sai ambiguities implausible plausible-but-incorrect inappropriate ⚠ Ví dụ SCN08 — plausible-but-incorrect User hỏi deadline, bot trả “1800 22/06ˮ — nghe hợp lý nhưng sai (đúng: 2000. Kiểu sai nguy hiểm nhất: hợp lý nên khó bị phát hiện. Nếu có nút bấm để hỏi thay vì tự đoán → 3 lỗi trigger biến mất. Cấu hình quyết định bề mặt rủi ro. BatchBuddy · failure-mode map theo config hiện tại (trigger tự đoán) — đổi config = đổi bản đồ lỗi.

---

<!-- chiron-source-span: {"source_span_id":"2fd511d5-8ee3-5b23-8207-ae0eb20630db","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"④c Privacy · ⑤ Align engineering · ⑥ GTM","extraction_method":"pdf-text-layer"},"checksum":"e5ef38ab410ae5b28d2e5f57a04b9932a46cc3f445539ce0c8777c88db4bfe16"} -->

## Slide 27 - ④c Privacy · ⑤ Align engineering · ⑥ GTM

Ba phần cuối của PRD cho AI feature — vẫn lấy ví dụ Zoom AI Companion / meeting summary. ④c PRIVACY & CONTROLS · Disclosure: banner pop-up cho mọi participant khi AI bắt đầu chạy + sparkle indicator hiển thị suốt lúc summary đang chạy · Base setting default off tới khi account admin enable · Kill switch: host dừng summary bất cứ lúc nào, xóa luôn transcript tương ứng · Transcript retention tối đa 30 ngày · Data của khách KHÔNG dùng để train model ⑤ ALIGN ENGINEERING Đừng over-spec. Thảo luận với engineering ngay khi draft spec — đừng chờ spec hoàn chỉnh; sẽ có nhiều unknown về việc LLM làm được/không làm được.

### PM cần hiểu đủ để cân quyết định product
· Prompting — prompt user gửi thẳng hay lồng trong prompt lớn hơn · Model selection — 1st vs 3rd party, privacy · LLM techniques — fine-tuning, RAG · Scaling — GPU đắt, capacity, data residency ⑥ GTM

### Rollout theo tier (beta trước để monitor quality)
nội bộ → premium tier → GA Pricing: add-on SKU hay bundled? Zoom: free kèm meetings license — muốn AI phổ biến rộng, không để IT admin phải chọn ai được dùng AI. Enablement: training deck về behavior + rollout + privacy · FAQ · channel chat "Ask AI Companion" cho field team hỏi đáp. Nguồn: Ailian Gan — "Write a PRD for a generative AI feature" Reforge) · ví dụ Zoom AI Companion.

---

<!-- chiron-source-span: {"source_span_id":"a66d2fca-31a8-55f2-a650-d6b82ae5211e","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"S E C T I O N 0 3","extraction_method":"pdf-text-layer"},"checksum":"ece2e52d8543b5b8a5b3d8c453c8ebbf93c9d5103882403d8f2f71f185a6fd53"} -->

## Slide 28 - S E C T I O N 0 3

Human-centered AI design Thiết kế AI lấy con người làm trung tâm

---

<!-- chiron-source-span: {"source_span_id":"c9411d0c-db56-5fb3-99d2-8fc4a4ceecbd","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"PHẦN MỀM TRUYỀN THỐNG AI PRODUCT","extraction_method":"pdf-text-layer"},"checksum":"cdd0011e5d2930ed0f99f58a2a8a644431f80e0ccf4e90b6b55547ed3cf5d0bc"} -->

## Slide 29 - PHẦN MỀM TRUYỀN THỐNG AI PRODUCT

Kết quả Ví dụ Kiểm thử Lỗi Phần mềm truyền thống vs AI product Phần mềm chạy theo luật. AI chạy theo xác suất — và xác suất nghĩa là sẽ có lúc sai. Luôn giống nhau Mỗi lần một khác "Số dư của tôi?" → trả đúng số, mọi lúc "Tóm tắt email này" → mỗi lần một bản Đạt / không đạt Chạy 100 lần → bao nhiêu lần "đủ tốt"? Bug — tìm và sửa được Sai xác suất — không sửa được, chỉ giảm được "Bạn không biết user sẽ tương tác thế nào, và cũng không biết LLM sẽ phản hồi ra sao — input, output, process, cả ba đều không chắc chắn." — Aishwarya Ashi Naresh Reganti, Lenny's Newsletter 1/2026 Nếu sản phẩm dùng AI, bạn đang thiết kế cho uncertainty. Nguồn: Aishwarya Naresh Reganti (ex-AWS · LevelUp Labs) & Kiriti Badam OpenAI — Lenny's Newsletter, 11/1/2026 (diễn giải ý).

---

<!-- chiron-source-span: {"source_span_id":"6cc7f0a8-0846-511d-9e9c-148af0beaf94","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Những câu hỏi thiết kế dành cho sản phẩm AI","extraction_method":"pdf-text-layer"},"checksum":"fe9a2f97f41440fb47806bdbcfd06d07e9c4254d1365991bd36f12c421960bf7"} -->

## Slide 30 - Những câu hỏi thiết kế dành cho sản phẩm AI

Mình đã đặt đúng kỳ vọng cho người dùng chưa? Làm thế nào chúng ta biết được AI có thể làm gì, không thể làm gì và cách nó sẽ mắc lỗi? Thiết kế phản hồi thế nào khi AI sai? Xây dựng vòng lặp feedback

---

<!-- chiron-source-span: {"source_span_id":"b55f8a46-bda3-57a7-b5b4-7641454db428","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"PAIR Guidebook Google","extraction_method":"pdf-text-layer"},"checksum":"afacedb0d5e7d53253327317e3874e70ca81c6adf65ce24b9be145a436327ebd"} -->

## Slide 31 - PAIR Guidebook Google

PAIR thiên về AI product framing: chọn đúng bài toán AI, định nghĩa success, trust, feedback, graceful failure. HAX Toolkit Microsoft) HAX thiên về AI interaction design: guideline, pattern, planning, và test scenario cho những failure của AI Tài liệu buổi học PAIR: pair.withgoogle.com · HAX Playbook: github.com/microsoft/HAXPlaybook

---

<!-- chiron-source-span: {"source_span_id":"61e600dd-a8b1-59b1-8e42-9e2721f3660d","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Krug thiên về how: làm sao để interface bớt","extraction_method":"pdf-text-layer"},"checksum":"9e51c3129fde67c3a23c58289f42347ae54f02a050dfad5fb680fa6d197682ad"} -->

## Slide 32 - Krug thiên về how: làm sao để interface bớt

rối, bớt bắt người dùng dừng lại để suy nghĩ. Norman thiên về why: vì sao user không hiểu hệ thống, vì sao feedback, mapping và conceptual model lại quan trọng Link sách Sách nên đọc

---

<!-- chiron-source-span: {"source_span_id":"7b097291-3b2d-571a-8ded-67ed93a76529","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Why Johnny Can't Prompt CHI 2023","extraction_method":"pdf-text-layer"},"checksum":"dc91bd96c160a43a267f43ac25d8b4d35ac318a125fd1ab9ed874e1b21438677"} -->

## Slide 33 - Why Johnny Can't Prompt CHI 2023

Người dùng viết prompt thường không biết AI làm được gì / không làm được gì. Vì vậy họ cần ví dụ hoặc chỉ dẫn cụ thể để biết nên tiếp cận thế nào. Người dùng viết prompt thường khái quát hóa quá mức từ chỉ một vài ví dụ hoặc một vài lỗi nhỏ (và dễ bỏ cuộc sớm). Một số người kỳ vọng AI sẽ hiểu chỉ dẫn giống như con người hiểu Zamfirescu-Pereira, J.D., et al. “Why Johnny Canʼt Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts.ˮ CHI 2023 — people.eecs.berkeley.edu/~bjoern/papers/zamfirescu-johnny-chi2023.pdf

---

<!-- chiron-source-span: {"source_span_id":"36ee0957-ff8a-53d2-9deb-c0a642eda7ca","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Đừng hứa hẹn quá khả năng của AI","extraction_method":"pdf-text-layer"},"checksum":"1b1d5a3f5cd8d0d8fcdf23e333969474d4aa105b9f7b9e233942de73684c102a"} -->

## Slide 34 - Đừng hứa hẹn quá khả năng của AI

Đây là vấn đề về kỳ vọng, không chỉ là vấn đề về độ chính xác

```text
“Don't let your UI write a check that your
```
AI can't cash.ˮ - Eytan Adar 2018

- Auto-resolve customer issue vs ✓ Draft reply for human review
1 INITIALLY Make clear what the system can do ⓘ Help the user understand what the AI system is capable of doing. Guidelines for Human-AI Interaction Microsoft) PAIR Guidebook, ch. "Mental Models" — cùng một ý: UI là nơi đặt kỳ vọng.

---

<!-- chiron-source-span: {"source_span_id":"bb18975c-e728-53a1-8a85-8861d54159b7","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Guidelines for Human-AI Interaction Microsoft)","extraction_method":"pdf-text-layer"},"checksum":"871ebd215d0a258622b627ce36345c4b1aa5c49108da8c1a91b7451e01626b18"} -->

## Slide 35 - Guidelines for Human-AI Interaction Microsoft)

Bộ 18 nguyên tắc thiết kế AI UX theo 4 chặng của trải nghiệm người dùng Amershi et al., “Guidelines for Human-AI Interactionˮ, CHI 2019 — microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction · HAX Playbook: github.com/microsoft/HAXPlaybook

---

<!-- chiron-source-span: {"source_span_id":"8478fadd-4076-5e69-9110-aad2e84a9b55","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"không còn ở","extraction_method":"pdf-text-layer"},"checksum":"e9ecb6423fe951e8fe2b6a4ca0a35e04564e5c488e125becc2d8eae5a00b0e37"} -->

## Slide 36 - không còn ở

case 2 nữa Email Assistant AI gợi ý reply khi nhận email mới

- Đổi cách AI tạo câu trả lời = đổi luôn nghĩa vụ thiết
kế và kiểm soát của team.

---

<!-- chiron-source-span: {"source_span_id":"677af76f-058c-559d-87eb-214181336aa2","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"High","extraction_method":"pdf-text-layer"},"checksum":"b49f6bd9b908ccfc0a531b1b7cb66b342e28c952df04f92450173d2258535a17"} -->

## Slide 37 - High

Low Low High Trust in AI system AI capability Calibr ated trust Overtrust = user tin cao hơn năng lực thật của AI Ví dụ AI chỉ nên gợi ý, nhưng UI làm user tưởng nó có thể tự quyết Nguy hiểm vì user dễ giao việc quá mức, bỏ qua kiểm tra Distrust = user tin thấp hơn năng lực thật của AI Ví dụ AI thực ra giúp tốt, nhưng user không dám dùng hoặc bỏ qua hoàn toàn Hậu quả là underuse: có giá trị nhưng không được tận dụng Thiết kế AI nhằm hiệu chỉnh trust đúng mức Figure 4-1. Trust calibration. Users can overtrust the AI when their trust exceeds the system's capabilities. They can distrust the system if they are not confident of the AI's performance Source: Designing Human-Centric AI Experiences Applied UX Design for Artificial Intelligence Akshay Kore) Trust calibration

---

<!-- chiron-source-span: {"source_span_id":"900797b2-b08e-5d48-967a-ccd341e92bff","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Trust calibration = expectation + explainability + control","extraction_method":"pdf-text-layer"},"checksum":"e1378a2a468f217ab87ba0b4c2a6bb42910fde44026159d71badaf96bb709230"} -->

## Slide 38 - Trust calibration = expectation + explainability + control

Expectation Nói rõ AI làm được gì, làm tốt tới đâu, khi nào dễ sai. Explainability Giúp user hiểu vì sao AI ra output này và khi nào nên nghi ngờ. Control Cho user sửa, bỏ qua, undo, preview, hoặc duyệt trước khi commit. Ba phần còn lại của deck thực ra chính là unpack ba trụ này.

---

<!-- chiron-source-span: {"source_span_id":"0ea0d117-1917-5ee2-88f3-92f5bff60f8b","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Augmentation vs Automation","extraction_method":"pdf-text-layer"},"checksum":"a0cfa92c3634a4ee665b307a6c7d6ec17497a7828763bdaf1d1799f5a10cde3a"} -->

## Slide 39 - Augmentation vs Automation

Chọn mức độ tự chủ (agency) theo độ chắc chắn và chi phí khi sai. Augmentation Automation

- Cần phán đoán, sáng tạo hoặc sở thích cá nhân.

- Ý định và yêu cầu của user còn mơ hồ

- User phải chịu trách nhiệm cho quyết định cuối cùng.

- Sai sót có hậu quả lớn, khó phục hồi

- Workflow kéo dài, nhiều bước, thường xuyên thay đổi.

- Lặp lại, tốn thời gian hoặc ít giá trị sáng tạo.

- Quy trình rõ ràng; input và output dễ xác định.

- Hệ thống có thể thực hiện ổn định với ít giám sát.

- Nếu AI sai, hậu quả thấp, dễ phát hiện hoặc dễ hoàn
tác.

- User muốn giao việc vì không đủ thời gian hoặc nguồn
lực. Copilot: 30% acceptance rate mà 4.7M paid users 1/2026 — augmentation đúng chuẩn GitHub · Microsoft earnings).

---

<!-- chiron-source-span: {"source_span_id":"97143d6c-2eab-5c9e-a7d1-3200dbb9b3f3","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Augmentation Automation","extraction_method":"pdf-text-layer"},"checksum":"3a9b4782374306e0420dbbf35a45e1d655bca1d05eebfbdaad4cfa1b085960f8"} -->

## Slide 40 - Augmentation Automation

Inaction Chưa đủ chắc user muốn gì Sai một lần là rất đắt Giữ quyền quyết định cho người dùng Ask Có tín hiệu đúng, nhưng còn mơ hồ Một câu hỏi ngắn giảm rủi ro lớn Hợp với việc quan trọng nhưng chưa rõ ý Act Đủ chắc user muốn gì Làm sai vẫn dễ sửa hoặc undo Tự động hóa để tiết kiệm thời gian Mixed initiative như một bài toán quyết định giữa act, ask, hay not act dựa trên expected value, chứ không chỉ là sở thích thiết kế. Ask thường là trạng thái thông minh nhất nhưng lại hay bị bỏ quên nhất. Eric Horvitz, Principles of Mixed-Initiative User Interfaces CHI 1999 Augmentation vs Automation Chọn mức độ tự chủ (agency) theo độ chắc chắn và chi phí khi sai.

---

<!-- chiron-source-span: {"source_span_id":"60822687-ad1c-568c-bb0c-d62f94c8d51b","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Thiết kế độ tự chủ (agency) theo chi phí khi sai (cost-of-error)","extraction_method":"pdf-text-layer"},"checksum":"5591d2096c68c490a37840fca075cbf91534c5a715964a920dfcfe5f62782934"} -->

## Slide 41 - Thiết kế độ tự chủ (agency) theo chi phí khi sai (cost-of-error)

_[Trang không có text layer và OCR không cung cấp thêm văn bản.]_

---

<!-- chiron-source-span: {"source_span_id":"32a814a2-4f16-5b00-b3b7-9f2ce41436cb","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Thiết kế độ tự chủ (agency) theo chi phí khi sai (cost-of-error)","extraction_method":"pdf-text-layer"},"checksum":"5591d2096c68c490a37840fca075cbf91534c5a715964a920dfcfe5f62782934"} -->

## Slide 42 - Thiết kế độ tự chủ (agency) theo chi phí khi sai (cost-of-error)

_[Trang không có text layer và OCR không cung cấp thêm văn bản.]_

---

<!-- chiron-source-span: {"source_span_id":"3b7a3f8e-6920-5127-8f93-3fc5a717977c","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Thiết kế độ tự chủ (agency) theo chi phí khi sai (cost-of-error)","extraction_method":"pdf-text-layer"},"checksum":"5591d2096c68c490a37840fca075cbf91534c5a715964a920dfcfe5f62782934"} -->

## Slide 43 - Thiết kế độ tự chủ (agency) theo chi phí khi sai (cost-of-error)

_[Trang không có text layer và OCR không cung cấp thêm văn bản.]_

---

<!-- chiron-source-span: {"source_span_id":"5c993d9e-c690-5375-b8d2-384da3b5cf60","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Làm rõ AI làm được gì Source: Make clear what the system can do","extraction_method":"pdf-text-layer"},"checksum":"edf178922434737c1b96975a7b4ec60b1a0d5b913fecaed7a1f13e70cadce509"} -->

## Slide 44 - Làm rõ AI làm được gì Source: Make clear what the system can do

### Nên dùng khi

- Người dùng chưa quen với loại AI này.

- Tính năng mới hoặc khó tự khám phá.

- Hệ thống có nhiều khả năng nhưng không dễ nhìn ra ngay.

- Muốn hướng người dùng vào những kiểu đầu vào mà AI xử lý tốt hơn.

### Design patterns
Use explanations: Dùng phần giải thích để người dùng hiểu hệ thống có thể làm gì Expose system controls: Làm lộ các nút, menu, tùy chọn, hoặc cài đặt để người dùng nhìn vào là hiểu hệ thống có những khả năng nào…. Demonstrate possible inputs: Cho ví dụ prompt, ví dụ câu hỏi, hoặc gợi ý đầu vào để người dùng thấy được những dạng tương tác… Capability cue là một phần của interaction design — không chỉ là onboarding copy.

---

<!-- chiron-source-span: {"source_span_id":"77239f23-0da6-5d69-bfc7-24490e95064d","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Làm rõ hệ thống làm tốt đến đâu Source: Make clear how well the system can do what it can do","extraction_method":"pdf-text-layer"},"checksum":"8a78822837392e3fa1368d7fa501e52b62ac61c7bd276c93051d97a455baa4be"} -->

## Slide 45 - Làm rõ hệ thống làm tốt đến đâu Source: Make clear how well the system can do what it can do

Hệ thống cần giúp user hình dung đúng về mức độ chính xác, độ ổn định, và những tình huống AI có thể sai. ✈ Trip Planner AI Gợi ý lịch trình & giá khách sạn theo ngân sách.

- Do Giá tham khảo tại thời điểm gợi ý —
"giá thực tế có thể thay đổi khi đặt".

- Don't "Đây là lựa chọn phù hợp nhất" +
tổng chi phí 4.200.000đ nói như chắc chắn. 🍱 Food Scanner Chụp món ăn, AI ước tính calo và ghi nhật ký.

- Do Khoảng "350430 kcal" + nói rõ là
ước tính vì ảnh hơi mờ.

- Don't Một con số exact "387 kcal" —
precision giả. 📄 Resume Screener AI xếp hạng CV, hỗ trợ HR ra quyết định sàng lọc.

- Do "Danh sách phù hợp để bạn xem
trước" + nêu giới hạn dữ liệu đầu vào.

- Don't Auto loại ứng viên ("Đã loại")
trước khi con người xem. 🧠 Mental Health Journaling AI Đọc nhật ký, nhận diện cảm xúc, gợi ý reflection.

- Do "Đây là quan sát từ nhật ký, không
phải chẩn đoán".

- Don't Gắn nhãn "Burnout giai đoạn 2"
như chẩn đoán chắc chắn. Mỗi domain cần một cách nói khác nhau — precision giả là một lỗi thiết kế.

---

<!-- chiron-source-span: {"source_span_id":"46f947ea-0e8d-51c2-93eb-a8d2c8431a27","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"Khi AI sai / không chắc chắn Source: Scope services when in doubt","extraction_method":"pdf-text-layer"},"checksum":"68092ebec43572c83c3c017d7c70247571ca602766f3d45d91b7e63b027c1c51"} -->

## Slide 46 - Khi AI sai / không chắc chắn Source: Scope services when in doubt

Hỏi lại trước khi làm Cho phép user tuỳ chỉnh Khi AI không chắc để hiểu người dùng, nó nên hỏi lại — thay vì cố giải quyết một câu hỏi mơ hồ. Khi AI không chắc, bớt làm đi thường là UX tốt hơn. HAX G10 "Scope services when in doubt" Amershi et al., CHI 2019 · D18 HCAI (batch02 day18.

---

<!-- chiron-source-span: {"source_span_id":"56bb38e1-870a-5f47-aff6-1d97be988cf7","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Giải thích vì sao","extraction_method":"pdf-text-layer"},"checksum":"019645885c5d766f941a94f6f3d56528679736396507a764352f7c23904b7c21"} -->

## Slide 47 - Giải thích vì sao

hệ thống làm như vậy Người dùng cần hiểu tại sao khi kết quả ảnh hưởng quyết định, hoặc có vẻ "khó hiểu" Source: Make clear why the system did what it did Giải thích lý do đưa ra quyết định Map user behaviors to

### system outputs
hành vi trước đây ảnh hưởng đầu ra thế nào Map system input attributes

### to system outputs
yếu tố đầu vào nào ảnh hưởng mạnh What-if

### explanations
cho user thử đổi đầu vào để xem kết quả đổi ra sao PAIR Guidebook, ch. "Explainability + Trust" — explanation là cách duy trì trust đúng mức.

---

<!-- chiron-source-span: {"source_span_id":"96732567-2b78-5f8a-b995-9727b40612f1","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"AI có thể chuẩn bị. Người dùng mới là người phê duyệt. Friction thêm đó là friction tốt.","extraction_method":"pdf-text-layer"},"checksum":"33a598232c569b3b83565dda369fbcb673d0e76f62c0cbad958ad1e1a5960607"} -->

## Slide 48 - AI có thể chuẩn bị. Người dùng mới là người phê duyệt. Friction thêm đó là friction tốt.

Cho phép user duyệt trước khi đi tiếp

---

<!-- chiron-source-span: {"source_span_id":"ebeafefc-f69b-5bc8-bd60-2c13d79e4359","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Chọn cách nào phụ thuộc vào việc báo sai hay bỏ sót gây hại hơn.","extraction_method":"pdf-text-layer"},"checksum":"8a54590342b78b7707b30c93c06d3225fdaa9098b0a0a940d3b4bab748a88e23"} -->

## Slide 49 - Chọn cách nào phụ thuộc vào việc báo sai hay bỏ sót gây hại hơn.

FN TN TP FPRecall Precision Precision / Recall tradeoff

---

<!-- chiron-source-span: {"source_span_id":"5c112c08-9635-5b9b-9b3a-464665362b36","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"Hiển thị kết quả theo mức độ tự tin","extraction_method":"pdf-text-layer"},"checksum":"112ba28005b71fb0dba22a5d5a1e6c8c285e3fa99366dbf92ae9c62c552d8ca8"} -->

## Slide 50 - Hiển thị kết quả theo mức độ tự tin

User không cần biết 0.71 hay 0.84 — user cần thấy hệ thống cư xử khác nhau khi độ chắc khác nhau. Kayak từng hiển thị "Confidence 79%" 20132019 — nay đã bỏ số%: confidence không nhất thiết là một con số Kayak Help).

---

<!-- chiron-source-span: {"source_span_id":"a6a293c4-80bc-5446-b095-dbe874ff9163","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"R E C OV E RY","extraction_method":"pdf-text-layer"},"checksum":"86522dbbf8fd956fff42cb3779df1d652d89efe8c44a875eaec1228aac2defef"} -->

## Slide 51 - R E C OV E RY

Thiết kế khi AI sai Nửa đầu giảm khả năng sai. Nửa này: khi sai rồi, user không bị kẹt.

---

<!-- chiron-source-span: {"source_span_id":"da86dde9-2622-5ff6-a2ee-7078eec7e99a","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"Cho phép user chỉnh sửa kết quả Undo / Rollback","extraction_method":"pdf-text-layer"},"checksum":"fe6d2abf45a3287e744178312bc943c94546d94c15060ea55226656316d6547c"} -->

## Slide 52 - Cho phép user chỉnh sửa kết quả Undo / Rollback

Nếu AI không hoàn hảo, đừng bắt user làm lại từ đầu.

---

<!-- chiron-source-span: {"source_span_id":"51ea7cb0-90d9-59eb-bbb2-2c2c317b1ce8","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"Màn hình lỗi là cơ hội để hướng dẫn cách dùng đúng Lỗi là cơ hội để xin feedback","extraction_method":"pdf-text-layer"},"checksum":"98b0e5ebc90036d55ce5f4f206162fe1d50a515ee96789b849af574fb029c1c4"} -->

## Slide 53 - Màn hình lỗi là cơ hội để hướng dẫn cách dùng đúng Lỗi là cơ hội để xin feedback

Error state là lúc user sẵn sàng học nhất — và cũng sẵn sàng phản hồi nhất.

---

<!-- chiron-source-span: {"source_span_id":"199e219c-34d9-5f41-bc93-2cb356e82167","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"Trả quyền kiểm soát cho người dùng","extraction_method":"pdf-text-layer"},"checksum":"1200b9eec5a53ddd950aecef77df4868eea5b0fc6b09002494af21b7a9cb76ae"} -->

## Slide 54 - Trả quyền kiểm soát cho người dùng

Cung cấp lối thoát rõ ràng khi AI không đủ khả năng Chuyển sang người thật Gợi ý bước tiếp theo Có chế độ cho user tự chỉnh AI tốt không phải AI luôn có câu trả lời — AI tốt biết đưa user sang con đường khác khi mình không đủ khả năng.

---

<!-- chiron-source-span: {"source_span_id":"6787960e-6909-5484-a7fe-6b7bcb871de7","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"AI IN ACTION · NGÀY 5","extraction_method":"pdf-text-layer"},"checksum":"20247c9482b07d1fc149dd233c311df16445b61e341d6dbc7a6eb04411361a94"} -->

## Slide 55 - AI IN ACTION · NGÀY 5

S E C T I O N 0 4 Evals cơ bản Sai kiểu nào tệ hơn · Precision hay Recall · Ba giai đoạn của eval flow — phần chuyên sâu gặp lại ở Ngày 6

---

<!-- chiron-source-span: {"source_span_id":"315edd22-3056-54d4-8c49-536224e63508","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"Eval: sai kiểu nào tệ hơn?","extraction_method":"pdf-text-layer"},"checksum":"4b398f9b49b651118f867950e8680a8f64a596ccb748fa5b064d0e7af1fd5efe"} -->

## Slide 56 - Eval: sai kiểu nào tệ hơn?

Ví dụ: AI lọc video cho app trẻ em — 100 video, 10 video xấu thật XẤU THẬT 10 LÀNH THẬT 90 AI đánh dấu XẤU13 AI cho qua87 8 ✓ Chặn đúng 5 ✗ Báo nhầm — video tốt bị gỡ oan 2 ✗ BỎ SÓT — trẻ thấy nội dung xấu 85 ✓ Cho qua đúng P R E C I S I O N 8 / 13  62% Khi AI nói CÓ, đúng bao nhiêu? R E CA L L 8 / 10  80% Trong số cần tìm, AI tìm được bao nhiêu? Cái nào tệ hơn? Lọt 2 video xấu (trẻ thấy) tệ hơn gỡ oan 5 video tốt → cần RECALL cao. Precision = chặn đúng / tổng bị đánh dấu = 8/13 · Recall = chặn đúng / tổng xấu thật = 8/10.

---

<!-- chiron-source-span: {"source_span_id":"97a4ccc3-2cc8-5538-891d-86e75f567241","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"Precision hay Recall — phụ thuộc context","extraction_method":"pdf-text-layer"},"checksum":"8493b38f5d270f957e08760e645a1e79e671cb94fd4f1802a77cbab466dc1231"} -->

## Slide 57 - Precision hay Recall — phụ thuộc context

User act theo kết quả sai — FP tệ hơn

- PRECISION
Bỏ lọt = mất giá trị — FN tệ hơn

- RECALL
User THẤY & sửa được User KHÔNG thấy Legal RAG chatbot User thấy câu trả lời, nhưng sai mà act theo

- hậu quả pháp lý nặng
Copilot, FAQ chatbot Gợi ý nhiều, user tự lọc — bỏ lọt gợi ý hay = mất giá trị Spam filter, auto-send email Sai mà không ai biết = nguy hiểm (email quan trọng vào spam) Content mod trẻ em, fraud Bỏ lọt = thảm họa — Recall bất kể user thấy hay không Sai mà user KHÔNG BIẾT → thường cần Precision. Nhưng bỏ lọt = thảm họa → Recall bất kể user thấy hay không.

---

<!-- chiron-source-span: {"source_span_id":"24acffa0-d46f-5eb9-9e51-85fc9688f97a","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"Không có đáp án tuyệt đối — chấm theo lý do thuyết phục.","extraction_method":"pdf-text-layer"},"checksum":"7f5f9d462e561c5d8e45d8ad0b0b00f792d2f78b03c2d4ed3335d8e556857fd8"} -->

## Slide 58 - Không có đáp án tuyệt đối — chấm theo lý do thuyết phục.

Precision hay Recall? DISCORD — 5 PHÚT Với mỗi sản phẩm: sai kiểu nào tệ hơn — báo nhầm (ưu Precision) hay bỏ lọt (ưu Recall)? 01 Lọc nội dung trẻ em Bỏ lọt = trẻ xem được video xấu. Báo nhầm = video tốt bị gỡ oan. 02 Code autocomplete Gợi ý sai user thấy ngay và gõ đè. Thiếu gợi ý = mất giá trị. 03 AI đọc X-quang Bỏ sót khối u vs báo động giả cho bác sĩ kiểm tra thêm. 04 Duyệt khoản vay Cho vay người không trả được vs từ chối nhầm khách tốt. 05 Gợi ý nhạc Gợi ý dở thì user skip. Bỏ sót bài hay thì user không biết. Gõ Discord 5 dòng: [số]-P hoặc [số]-R + lý do 1 câu · VD 3R — bỏ sót khối u nguy hiểm hơn báo nhầm

---

<!-- chiron-source-span: {"source_span_id":"29c26e83-c5ad-5092-a7c6-058dd88aabb2","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"EVAL FLOW · CƠ BẢNDemo chạy tốt không có nghĩa sản phẩm chạy tốt","extraction_method":"pdf-text-layer"},"checksum":"81bc7596108a89e7b0d211d362e9d62c0fd3cc851a4692b51831ee3c3b0cf09d"} -->

## Slide 59 - EVAL FLOW · CƠ BẢNDemo chạy tốt không có nghĩa sản phẩm chạy tốt

Vì sao phải đánh giá chất lượng AI (eval) thành một chu trình — không phải chấm điểm một lần. Lúc demo mọi thứ trong tầm kiểm soát 1020 case do team tự chọn.· Input "sạch", đúng kịch bản đã chuẩn bị.· Chạy vài lần thấy ổn → kết luận "xong".· Lúc user thật dùng không còn kiểm soát được input Hàng nghìn câu hỏi mỗi ngày — không giống lúc demo.· User hỏi theo cách team chưa từng nghĩ tới.· AI chắc chắn sẽ có lúc sai — vấn đề là sai bao nhiêu, sai ở đâu.· Chất lượng AI là một phân bố — đúng bao nhiêu%, trên loại case nào. Muốn biết con số đó thì phải đo, và phải đo liên tục.

---

<!-- chiron-source-span: {"source_span_id":"d81232c3-eed7-55de-8f41-7853d08ca45f","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"EVAL FLOW · CƠ BẢNEval khác test phần mềm thường ở chỗ nào","extraction_method":"pdf-text-layer"},"checksum":"d129a6b0ed4199ed8f73b72b73031e8144cbb073c722c4fe5781b470379e160d"} -->

## Slide 60 - EVAL FLOW · CƠ BẢNEval khác test phần mềm thường ở chỗ nào

Eval (đánh giá chất lượng AI = chấm AI trên một bộ case đại diện, lặp đi lặp lại — trước và sau khi ra mắt. Test phần mềm thường Eval cho AI Kết quả Cùng input → cùng output. Pass hoặc fail, rõ ràng. Cùng input → mỗi lần một khác. "Đúng" là chuyện mức độ: đúng bao nhiêu%? Bộ câu hỏi Viết một lần, chạy mãi. Phải lớn dần theo case thật từ user — không bao giờ "đủ". Khi nào đo Trước khi release (ra mắt). Trước release và liên tục sau release — user tạo case mới mỗi ngày. Precision / Recall hồi nãy chính là một kiểu thước đo của eval — chọn thước đo nào là một quyết định sản phẩm.

---

<!-- chiron-source-span: {"source_span_id":"d41e1dad-c4cb-567a-a81c-9924aebafb05","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"EVAL FLOW · CƠ BẢNBa giai đoạn của eval flow — nói trước bằng lời","extraction_method":"pdf-text-layer"},"checksum":"28b04ab563e1b84cdd712c4434d35d4a52b9d2d99c8b7904874000ff07efb25a"} -->

## Slide 61 - EVAL FLOW · CƠ BẢNBa giai đoạn của eval flow — nói trước bằng lời

Slide tiếp theo là hình tổng kết — nắm 3 khái niệm này trước đã. 01 · Vibe Check chấm tay, cảm tính Chạy thử 1030 case rồi tự chấm tay.· Mục đích: hiểu AI hay sai kiểu gì — chưa cần con số chính thức. · Khi nào: lúc còn prototype — trước cả khi viết PRD. · 02 · Offline Eval chấm tự động, trước ra mắt Có bộ câu hỏi chuẩn (reference dataset). Mỗi lần đổi prompt / model → chạy lại toàn bộ, so với phiên bản hiện tại. · Qua "cổng chất lượng" (quality gate) mới được release. · Cái từng chạy tốt nay tệ đi = regression (lỗi quay đầu). · 03 · Online Monitoring theo dõi sau ra mắt User thật tạo case mới không lường trước. · Gom tín hiệu: thumbs up/down, user gõ lại prompt, bỏ giữa chừng. · Case lạ → đưa ngược về bộ câu hỏi chuẩn. · Case thật từ online chảy ngược về bộ câu hỏi offline — bộ câu hỏi ngày càng chuẩn. Vì vậy gọi là chu trình, không phải chấm một lần.

---

<!-- chiron-source-span: {"source_span_id":"6caa2931-1ddf-50b7-8c51-529795aea30b","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Ba giai đoạn","extraction_method":"pdf-text-layer"},"checksum":"bbbe2e631eac1bdcb070457c3dd40418089465a730972db9116bce63a5fb1dcd"} -->

## Slide 62 - Ba giai đoạn

STAGE 01 Vibe Check Manual review để hình thành intuition trước khi đóng cứng spec Prototype phase STAGE 02 Offline Eval So sánh, phát hiện regression, đặt quality gate trước rollout Build phase STAGE 03 Online Monitoring Theo dõi sau launch, bắt drift và failure mode mới Production phase
