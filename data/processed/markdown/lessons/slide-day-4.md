---
schema_version: 1
course_id: rag-intensive
document_id: "28d5f803-38ad-5eb5-b849-d24b622c1460"
document_version_id: "b73f21df-9116-5c05-b3e5-8009ac315558"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Prompt Engineering & Tool Calling — phân tích & breakdown từng slide"
source_file: "slide-day-4.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-day-4.html"
source_sha256: "dfa78e7becde0747084ff44184fedb3912ac28a393ab61a9b6ca05ec13eeeb7c"
parser_version: chiron-structured-markdown-v1
html_section_count: 17
interactive_module_count: 1
interactive_control_count: 5
language: vi
---

# Prompt Engineering & Tool Calling — phân tích & breakdown từng slide

> 43 slide, lấp đúng hai chỗ mà Ngày 3 để ngỏ: system prompt và 
 tool description. Bài định vị cả hai bằng một câu: 
 prompt là interface giữa ý định con người và hành vi model; tool calling là interface giữa model và 
 thế giới bên ngoài.

<!-- chiron-source-span: {"source_span_id":"8c6467c9-b817-5fc9-a68d-ab84e69a7503","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-day-4.html"},"checksum":"cc274771f9b037c40aba67b0c8a6e0762ec72928df0562c47d82f483234a9898"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Bài này là **bài kỹ thuật đầu tiên có thể áp dụng ngay trong ngày**. Khác với Ngày 2 và 3 
 (khung quyết định), Ngày 4 cho bạn những thứ gõ được vào code: cấu trúc prompt, anatomy của system prompt, 
 schema của tool.

Nó cũng **trả nợ hai chỗ Ngày 3 bỏ dở**:

| Ngày 3 nói gì | Ngày 4 giải quyết ở đâu |
| --- | --- |
| "Tool description quá mơ hồ" — một trong bốn nơi phải sửa khi debug | Slide 26–27 — tool schema anatomy · chương 6 — bốn nguyên tắc thiết kế |
| System prompt mẫu chỉ có bốn rule | Slide 17–19 — năm khối, và bốn anti-pattern |

Lượt 1 · ~12 phút

Nắm mạch chính

- Đọc slide 8 (4 thành phần prompt), 17 (anatomy system 
 prompt), 26 (tool schema), 29 (4 nguyên tắc tool)
- Nhìn Hình 2 — luồng tool calling, và chỗ nhiều người hiểu sai nhất
- Mục tiêu: nói được vì sao model không tự chạy tool

Lượt 2 · ~45 phút

Chương 3, 4, 5, 6

- Bốn chương này là phần gõ được vào code ngay
- Chạy mô-đun bốn rổ token — phần định lượng duy nhất của bài
- Đối chiếu system prompt hiện tại của bạn với bốn anti-pattern

Lượt 3 · ~15 phút

Trước quiz

- 6 hiểu lầm — hai cái đầu về tool calling rất hay bị hỏi
- Cheat sheet — bốn danh sách và một bảng rổ token
- Từ điển — few-shot, CoT, tool schema, idempotency, granularity

"Bạn đang gặp lỗi vì model chưa hiểu ý bạn, hay vì tool contract của bạn chưa 
 đủ rõ?"

slide 35 của Ngày 3

---

<!-- chiron-source-span: {"source_span_id":"16a0f1ba-faf1-56d3-80ba-916cf0b9edba","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"slide-day-4.html"},"checksum":"4020509cd5155287511de5bce258f0cdca833216a47fbac202d37c83270c121a"} -->

## 00 Mở đầu

Slide 1–5: câu hỏi dẫn dắt, bốn mục tiêu, và deliverable.

### Slide 1–5 Hai interface, và deliverable đòi chứng minh điều gì

> Trích slide 
>  " Hai người hỏi AI cùng một việc, một người nhận kết quả xuất sắc, người kia nhận rác. Tại sao? " 
>  " Mục tiêu của buổi này là hiểu cơ chế: prompt là interface giữa human intent và model 
>  behavior; tool calling là interface giữa model và thế giới bên ngoài. " 
>  " Deliverable: 1 agent script chạy được + 1 system prompt + 2 tool schemas + 
>  5 test questions + ghi chú lỗi prompt/tool/control flow. […] 5 câu test để chứng minh 
>  agent biết khi nào trả lời trực tiếp, khi nào gọi tool "

Chữ **interface** xuất hiện hai lần và nó là cách đóng khung chính xác. Interface có một 
 tính chất quan trọng: *hai bên phải hiểu cùng một hợp đồng*, và khi có lỗi thì lỗi nằm ở một 
 trong hai phía — hoặc ở chính hợp đồng.

| Interface | Nối cái gì với cái gì | "Hợp đồng" là | Hỏng thì triệu chứng |
| --- | --- | --- | --- |
| Prompt | Ý định con người ↔ hành vi model | System prompt: persona, rules, constraints, output format | Model làm sai việc, sai format, hoặc không nhất quán giữa các lần |
| Tool calling | Model ↔ thế giới bên ngoài | Tool schema: name, description, parameters, required | Model chọn sai tool, truyền sai args, hoặc gọi tool khi không cần |

"5 câu test để chứng minh agent biết **khi nào trả lời trực tiếp, khi nào gọi tool** " 
 — chú ý nó không đòi chứng minh agent gọi tool *đúng*, mà đòi chứng minh agent *biết khi nào KHÔNG cần gọi*.

Đây là chế độ hỏng ít được nhắc: agent gọi tool cho mọi câu hỏi, kể cả câu nó tự trả lời được. 
 Tốn tiền, chậm, và thêm một điểm hỏng — mà trace vẫn trông hợp lệ.

**Nên bộ 5 test phải có ít nhất một câu *không* cần 
 tool.** Nếu cả 5 câu đều cần tool, bạn không kiểm được điều mà deliverable yêu cầu. Đây là *conditional tool use* — pattern thứ nhất ở [slide 33](#s33).

---

<!-- chiron-source-span: {"source_span_id":"b6dd4468-159c-5688-822d-b0ee2b160064","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Prompt fundamentals","source_file":"slide-day-4.html"},"checksum":"5411083f58a4c01949cc8dcf2d51245f4aa3099c235df1c60ae6159a73faacbd"} -->

## 01 Prompt fundamentals

Slide 6–10: bốn thành phần, ba loại prompt, và ngân sách token.

### Slide 6–8 Bốn thành phần, và thứ tự thêm chúng vào

> Trích slide 
>  " Prompt kém: 'Viết email cho tôi' — không rõ gửi ai, về gì, tone nào, dài bao 
>  nhiêu. Prompt tốt: 'Viết email xin lỗi khách hàng về giao hàng trễ 2 ngày, tone lịch 
>  sự, dưới 120 từ, có CTA rõ ràng.'" 
>  " Nguyên tắc vàng: Specificity beats cleverness. Prompt ngắn nhưng rõ nghĩa thường 
>  tốt hơn prompt dài mà lan man." 
>  " ROLE (Act as a senior support analyst) · TASK (Summarize the 
>  ticket and propose next step) · CONTEXT (For an internal operations dashboard) · 
>  FORMAT (Output as JSON with 3 fields)" 
>  " Bắt đầu với Task + Format. Chỉ thêm Role hoặc Context khi chúng thực sự cải thiện chất 
>  lượng hoặc tính nhất quán. "

Câu chốt là câu đáng chú ý nhất, vì nó **xếp hạng bốn thành phần** thay vì liệt kê 
 ngang nhau — và thứ hạng đó ngược với thói quen của nhiều người:

| Thành phần | Ưu tiên | Vì sao |
| --- | --- | --- |
| Task | Bắt buộc | Không có nó thì không có prompt |
| Format | Bắt buộc | Quyết định output có dùng được bằng code hay không — và là núm vặn chi phí lớn nhất ( Ngày 1 ) |
| Role | Thêm khi cần | Hữu ích cho tone và mức độ chuyên môn, nhưng không đổi được kiến thức model có |
| Context | Thêm khi cần | Cần khi model không thể tự biết — nhưng mỗi token context là tiền và là chỗ trong ngân sách |

"Act as a senior support analyst" **không** làm model biết thêm về hỗ trợ khách hàng. 
 Kiến thức nằm trong tham số và đã cố định ( [Ngày 1, slide 37](day-1-ai-llm-foundation.html) ).

Cái Role thật sự đổi là *phong cách và mức độ chi tiết* — model chọn từ ngữ, độ dài, và giả 
 định về người đọc khác đi. Đó là tác dụng thật nhưng hẹp hơn nhiều so với kỳ vọng phổ biến.

**Khi nào Role đáng thêm:** khi output cần một tone nhất 
 quán qua nhiều lần gọi, hoặc khi bạn muốn model giả định người đọc có trình độ nào. Khi nào không: 
 khi bạn hy vọng nó làm model chính xác hơn về mặt sự kiện — nó không làm được điều đó.

"Viết email xin lỗi khách hàng về giao hàng trễ 2 ngày, tone lịch sự, dưới 120 từ, có CTA rõ 
 ràng."

không dài

mỗi cụm từ loại bỏ một sự mơ hồ

### Slide 9–10 Ba loại prompt, và ngân sách token

> Trích slide 
>  " Instruction prompt — ra lệnh trực tiếp cho một tác vụ. Dùng khi: hỏi đáp 1 lượt, 
>  transform, summarize, classify. Conversation prompt — giữ ngữ cảnh nhiều lượt với 
>  user. Dùng khi: chatbot, support, tutor, debugging nhiều bước. System prompt — 
>  đặt policy, boundary, output contract. Dùng khi: agent, assistant production, use case cần hành vi 
>  ổn định." 
>  " Token Budget Awareness: ■ Prompt dài hơn không đồng nghĩa prompt tốt hơn. 
>  ■ Mỗi token thừa làm tăng chi phí, latency, và đôi khi cả nhiễu. ■ Rule thực dụng: nếu prompt 
>  dài thêm nhưng không làm thay đổi hành vi mong muốn, hãy cắt bớt. " 
>  " Prompt engineering tốt là tối ưu độ rõ và khả năng kiểm soát, không phải thi xem ai viết 
>  prompt dài hơn. "

Ba loại prompt khác nhau ở **vòng đời**, và đó là cách phân biệt hữu ích nhất:

| Loại | Sống bao lâu | Ai viết | Trả tiền bao nhiêu lần |
| --- | --- | --- | --- |
| Instruction | Một lượt | Người dùng cuối, hoặc code sinh ra | Một lần |
| Conversation | Một phiên | Người dùng, tích luỹ dần | Mỗi lượt — vì lịch sử gửi lại |
| System | Vĩnh viễn — cho tới khi bạn sửa | Bạn, một lần, dùng cho mọi người dùng | MỌI lượt gọi |

System prompt được gửi lại ở *mọi* lượt gọi, cho *mọi* người dùng, trong suốt vòng 
 đời sản phẩm. Cắt 200 token thừa ở đó, với 1.500 lượt gọi mỗi ngày, là tiết kiệm 9 triệu token mỗi 
 tháng — đúng phép tính ở [Ngày 1](day-1-ai-llm-foundation.html).

Nhưng chú ý **đánh đổi ngược**: system prompt cũng là chỗ đặt 
 guardrail và output contract. Cắt quá tay thì hành vi kém ổn định hơn. Rule thực dụng của slide xử lý 
 đúng chỗ này: *"nếu prompt dài thêm nhưng không làm thay đổi hành vi mong muốn, hãy cắt bớt"* — 
 tức là **đo trước rồi cắt**, không cắt theo cảm giác.

có bộ test

5 câu test rõ pass/fail

---

<!-- chiron-source-span: {"source_span_id":"444137e5-7e20-5cf0-8886-c2cf664f540f","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Kỹ thuật prompting nâng cao","source_file":"slide-day-4.html"},"checksum":"f7090c441f6f9071b21d1a7da60ca5efc486068c24d4229f3e367408a7900b57"} -->

## 02 Kỹ thuật prompting nâng cao

Slide 11–15: zero/one/few-shot, khi nào dùng few-shot, và CoT không phải phép màu.

### Slide 11–14 Bốn mức, và thứ tự thử thực dụng

> Trích slide 
>  " Zero-shot — không có ví dụ mẫu. Nhanh, rẻ, nên thử trước. 
>  One-shot — 1 ví dụ mẫu. Tốt khi cần giữ format rõ hơn. 
>  Few-shot — 2–5 ví dụ. Tăng consistency, nhưng tốn token hơn. 
>  CoT — cho model reasoning từng bước. Hữu ích cho task suy luận." 
>  " Thứ tự thử thực dụng: zero-shot → few-shot → decomposition / CoT. Đừng nhảy vào prompt 
>  phức tạp ngay từ đầu. " 
>  " Khi nào dùng few-shot? ■ Khi model hiểu task nhưng ra sai format hoặc không ổn 
>  định giữa các input tương tự ■ Khi cần giữ tiêu chuẩn đánh giá, tone, hoặc cách lập luận nhất quán 
>  ■ Ví dụ mẫu nên relevant, đa dạng vừa đủ, và đúng format mong muốn" 
>  " Few-shot không phải để 'dạy lại' model mọi thứ; nó là cách chỉ ra pattern mà bạn muốn model 
>  bám theo. "

Câu *"model hiểu task nhưng ra sai format hoặc không ổn định"* là **tiêu chí chẩn đoán 
 chính xác** cho việc có nên dùng few-shot hay không — và nó loại trừ một trường hợp rất phổ biến:

Nếu model trả lời *sai sự thật* vì thiếu thông tin, thêm ví dụ mẫu không giúp gì — bạn chỉ 
 dạy nó cách trình bày câu sai cho đẹp hơn.

Đối chiếu với [Ngày 1](day-1-ai-llm-foundation.html): đó là vấn đề **context** (thiếu dữ kiện), không phải vấn đề **hành vi** (sai cách nói). 
 Cách chữa là đưa thông tin vào — RAG, tool — chứ không phải thêm ví dụ.

**Cách phân biệt nhanh:** nếu bạn tự viết được câu trả lời 
 đúng mà không cần tra cứu gì thêm ⇒ vấn đề là hành vi ⇒ few-shot có thể giúp. Nếu bạn cũng phải đi tra 
 ⇒ vấn đề là kiến thức ⇒ few-shot vô ích.

**Thứ tự "zero-shot → few-shot → CoT" có lý do về chi phí**, và đáng nhìn bằng số:

| Kỹ thuật | Token thêm vào input | Token thêm vào output | Khi nào đáng |
| --- | --- | --- | --- |
| Zero-shot | 0 | 0 | Luôn thử trước |
| One-shot | ~1 ví dụ | 0 | Cần format rõ hơn |
| Few-shot (2–5) | 2–5 ví dụ, ở MỌI lượt gọi | 0 | Không ổn định giữa các input tương tự |
| CoT | ~1 câu | Nhiều — nháp là token output, loại đắt nhất | Task cần suy luận nhiều bước |

**Few-shot tốn ở đầu vào:** ví dụ mẫu nằm trong prompt, gửi lại ở mọi lượt. Năm ví dụ 
 × 120 token = 600 token, ở *mọi* lần gọi, mãi mãi. Nhưng input là loại token rẻ.

**CoT tốn ở đầu ra:** phần nháp là token model sinh ra — đắt gấp 3–5 lần input 
 ( [Ngày 1, slide 68](day-1-ai-llm-foundation.html) ), và nó cũng làm chậm vì sinh tuần tự.

**Hệ quả thực hành:** với task khối lượng lớn mà cần format 
 ổn định, few-shot là lựa chọn kinh tế. Với task khó nhưng ít lượt, CoT đáng tiền. Trộn cả hai cho một 
 task đơn giản là cách nhanh nhất để đốt ngân sách mà không được gì — 
 đúng cảnh báo *"CoT là công cụ cải thiện reasoning, không phải phép màu"* ở [slide 15](#s15).

### Slide 15 CoT và Tree-of-Thought — và một cảnh báo

> Trích slide 
>  " CoT phù hợp khi: ■ Bài toán cần reasoning nhiều bước ■ Bạn muốn model giải thích 
>  logic trung gian ■ Bạn cần debug xem model sai ở bước nào " 
>  " Tree-of-Thought: ■ Hữu ích cho bài toán cần explore nhiều hướng ■ Phức tạp hơn, 
>  tốn token và latency hơn ■ Chỉ nên giới thiệu như extension, không phải mặc định cho mọi task " 
>  " CoT là công cụ cải thiện reasoning, không phải phép màu. Nếu task vốn dĩ chỉ là formatting 
>  hoặc extraction đơn giản, CoT thường là overkill. "

Lý do thứ ba của CoT — *"debug xem model sai ở bước nào"* — ít được nhắc nhưng là lý do **thực dụng nhất**, và nó cùng logic với ReAct ở [Ngày 3](slide-buoi-3.html).

|  | Chain-of-Thought | ReAct |
| --- | --- | --- |
| Model viết ra gì | Các bước suy luận | Thought + Action + Observation |
| Có chạm thế giới ngoài không | Không — chỉ suy luận nội bộ | Có — Action gọi tool thật |
| Lợi ích chung | Lý do lộ ra ngoài ⇒ debug được, và mỗi bước viết ra trở thành dữ kiện cho bước sau |  |

Nhìn theo cách này, **ReAct = CoT + tool calling**. Đó cũng 
 giải thích vì sao [anti-pattern "agent rỗng"](slide-buoi-3.html) tồn tại: một agent không có 
 tool thật thì Action của nó chẳng chạm được gì, nên nó *chính là* CoT — chỉ đắt hơn nhiều lần vì 
 chạy thành nhiều lượt gọi.

"Chỉ nên giới thiệu như extension, không phải mặc định cho mọi task."

bạn gần như chắc chắn không cần ToT

Ngày 1, 
 slide 38

---

<!-- chiron-source-span: {"source_span_id":"0127a67f-750c-5760-9e04-f229995f927c","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 System prompt engineering","source_file":"slide-day-4.html"},"checksum":"919443f9fa6d5aa4f9a34e7424d3bcfe1f544668badc508610ee697767c0191c"} -->

## 03 System prompt engineering

Slide 16–19: năm khối của một system prompt production-grade, ví dụ, và bốn anti-pattern.

### Slide 16–18 Năm khối, và ví dụ đã viết

> Trích slide 
>  " Persona: role, expertise level, communication style. Rules: việc 
>  nên làm, việc luôn phải làm. Capabilities: model được phép dùng tools nào, dữ liệu 
>  nào. Constraints: không làm gì, khi nào từ chối, khi nào escalate. 
>  Output format: JSON, markdown, bullet list, schema, language priority." 
>  " Ví dụ: You are a support triage agent for an e-commerce team. Rules: Answer in 
>  Vietnamese. Be concise and operational. If billing or refund policy is unclear, ask for more details. 
>  Constraints: Never invent order status. Never promise refunds without tool confirmation. 
>  Output format: Return JSON with: intent, action, reply "

Năm khối này chia thành **hai nhóm rất khác nhau về mục đích**, và phân biệt được chúng 
 giúp bạn biết khối nào cần chặt chẽ nhất:

| Nhóm | Khối | Trả lời câu hỏi | Hỏng thì hậu quả |
| --- | --- | --- | --- |
| Định hình làm cho tốt hơn | Persona | Nói năng thế nào | Giọng điệu không nhất quán — khó chịu, không nguy hiểm |
| Rules | Nên làm gì | Chất lượng kém hơn |  |
| Ràng buộc ngăn điều tệ | Capabilities | Được dùng gì | Model dùng tool không nên dùng |
| Constraints | KHÔNG được làm gì | Sự cố thật — hứa hoàn tiền, bịa trạng thái đơn |  |
| Output format | Trả về hình dạng nào | Code phía sau vỡ |  |

*"Never invent order status"* và *"Never promise refunds without tool confirmation"* — cả hai đều viết dưới dạng **phủ định + hành động cụ thể**, và đó là cách viết đúng.

So với một constraint viết tệ: *"Hãy cẩn thận với thông tin đơn hàng"* — không kiểm được, 
 không biết vi phạm là gì, model không biết phải làm gì khác đi.

**Chú ý câu thứ hai còn nêu cả điều kiện thoát:** *"without tool confirmation"* — nó không cấm hứa hoàn tiền, nó nói *khi nào* được hứa. 
 Đây là cách viết constraint tốt nhất: **cấm một đường, mở một đường**. Cấm mà không mở 
 đường thì model bị kẹt và sẽ tự tìm cách lách.

Capabilities

tools

tồn tại

khi nào được phép dùng

issue_refund

lookup_order

Ngày 3

### Slide 19 Bốn anti-pattern của system prompt

> Trích slide 
>  "□ Quá dài: nhồi mọi thứ vào 1 prompt 2000+ tokens rồi hy vọng model luôn làm đúng 
>  □ Mâu thuẫn: vừa bảo 'ngắn gọn', vừa bắt 'giải thích chi tiết từng bước' 
>  □ Mơ hồ: 'hãy thông minh', 'hãy chuyên nghiệp', nhưng không định nghĩa chuẩn output 
>  □ Không test edge cases: quên kiểm tra câu hỏi ngoài phạm vi, refusal, tool failure" 
>  " Nguyên tắc: system prompt là policy layer. Càng rõ boundary, càng dễ predict hành vi. "

Bốn anti-pattern này **ánh xạ một-một vào bốn cách sửa**, và bảng dưới là cách dùng 
 chúng như một checklist khi rà lại prompt của mình:

| Anti-pattern | Cách tự phát hiện | Cách sửa |
| --- | --- | --- |
| Quá dài | Đếm token. Trên 2.000 là cờ đỏ | Xoá từng đoạn, chạy lại bộ test — đoạn nào xoá mà test không đổi là đoạn thừa |
| Mâu thuẫn | Đọc to lên. Tìm cặp chỉ dẫn kéo về hai hướng | Chọn một, hoặc nêu điều kiện phân biệt: "ngắn gọn, trừ khi người dùng hỏi 'vì sao'" |
| Mơ hồ | Với mỗi chỉ dẫn, hỏi: "tôi kiểm được điều này không?" | Thay tính từ bằng hành vi đo được: "chuyên nghiệp" → "không dùng emoji, xưng hô 'quý khách'" |
| Không test edge case | Bộ test của bạn có câu ngoài phạm vi không? Có ca tool lỗi không? | Thêm ít nhất ba ca: ngoài phạm vi · thiếu thông tin · tool trả lỗi |

Prompt quá dài thì bạn thấy hoá đơn. Prompt mơ hồ thì bạn thấy output kém. Nhưng prompt **mâu thuẫn** tạo ra một hành vi *không ổn định*: model chọn một trong hai chỉ dẫn 
 tuỳ lượt, và bạn thấy kết quả lúc đúng lúc sai mà không hiểu vì sao.

Đây là loại lỗi tệ nhất để debug, vì nó *không tái hiện được* — chạy lại cùng input có thể 
 ra kết quả khác.

**Cách phát hiện rẻ nhất:** nhờ chính LLM đọc system prompt của 
 bạn và hỏi *"có cặp chỉ dẫn nào mâu thuẫn nhau không?"* Nó bắt được phần lớn ca hiển nhiên, 
 tốn một lượt gọi. Bài tập về nhà ở [slide 40](#s39) đúng là việc này: *"đọc lại system prompt của mình và chỉ ra 2 chỗ còn mơ hồ hoặc mâu thuẫn"*.

không phải chỗ đặt kiến thức

luật

context

tool

#### Ô kiểm tra — Chương 1, 2 & 3

Trả lời thành tiếng trước khi mở đáp án.

**1.** Model của bạn trả lời sai thông tin về chính sách đổi trả của công ty. 
 Đồng nghiệp đề xuất thêm few-shot với 5 ví dụ trả lời đúng. Nhận 
 xét. Áp dụng

#### Đáp án

**Few-shot không chữa được — đây là vấn đề context, không phải hành vi.**

Slide 13 nêu tiêu chí dùng few-shot rất rõ: *"khi model **hiểu task** nhưng ra 
 sai format hoặc không ổn định"*. Ở đây model không hề biết chính sách của công ty bạn — thông 
 tin đó chưa bao giờ có trong tham số.

**Thêm 5 ví dụ sẽ dạy nó cách trình bày câu sai cho đẹp hơn**, và tệ hơn: nó có thể 
 học "giọng điệu tự tin" từ các ví dụ, làm câu sai nghe thuyết phục hơn.

**Cách phân biệt nhanh:** bạn tự viết được câu trả lời đúng mà không cần tra cứu 
 không? Nếu phải tra ⇒ vấn đề kiến thức ⇒ few-shot vô ích.

**Cách chữa đúng:** đưa văn bản chính sách vào context (RAG), hoặc cho model một 
 tool tra cứu chính sách. Và thêm constraint: *"Never invent policy details — nếu không tìm thấy 
 trong tài liệu, nói không chắc và đề nghị kiểm tra lại."*

**2.** Trong bốn anti-pattern của system prompt, cái nào khó debug nhất và vì 
 sao? Phân tích

#### Đáp án

**"Mâu thuẫn" — vì nó không báo lỗi và không tái hiện được.**

• *Quá dài* ⇒ thấy ở hoá đơn và độ trễ. 
 • *Mơ hồ* ⇒ thấy ở output kém, nhất quán kém nhưng đoán được nguyên nhân. 
 • *Không test edge case* ⇒ thấy khi gặp ca biên. 
 • **Mâu thuẫn** ⇒ model chọn một trong hai chỉ dẫn *tuỳ lượt*. Kết quả lúc đúng 
 lúc sai, chạy lại cùng input có thể ra khác. Không có gì để bám vào khi debug.

**Ví dụ điển hình:** vừa bảo "ngắn gọn" vừa bắt "giải thích chi tiết từng bước".

**Cách phát hiện rẻ nhất:** nhờ chính LLM đọc system prompt và hỏi "có cặp chỉ dẫn 
 nào mâu thuẫn không?" — tốn một lượt gọi, bắt được phần lớn ca hiển nhiên.

**Cách sửa:** chọn một, hoặc nêu *điều kiện* phân biệt — "ngắn gọn, trừ khi 
 người dùng hỏi 'vì sao'".

**3.** Vì sao few-shot và CoT tốn tiền ở hai chỗ khác nhau, và điều đó đổi cách 
 chọn giữa chúng thế nào? Hiểu

#### Đáp án

**Few-shot tốn ở INPUT, CoT tốn ở OUTPUT — mà output đắt gấp 3–5 lần.**

• *Few-shot:* ví dụ mẫu nằm trong prompt, gửi lại ở *mọi* lượt gọi. 5 ví dụ × 120 
 token = 600 token input mỗi lần. Nhưng input là loại token rẻ. 
 • *CoT:* phần nháp là token model *sinh ra* — đắt gấp 3–5 lần input (Ngày 1, slide 68), 
 và chậm hơn vì sinh tuần tự từng token.

**Hệ quả cho việc chọn:**

• Task **khối lượng lớn** cần format ổn định ⇒ few-shot kinh tế hơn: trả một lần 
 chi phí input cố định, không kéo dài output. 
 • Task **khó nhưng ít lượt** ⇒ CoT đáng tiền: chất lượng suy luận tăng thật. 
 • Task **đơn giản** (formatting, extraction) ⇒ không dùng cái nào — zero-shot trước, 
 đúng thứ tự thử của slide 12.

**Và đừng trộn cả hai cho task đơn giản** — đó là cách nhanh nhất đốt ngân sách mà 
 không được gì.

---

<!-- chiron-source-span: {"source_span_id":"40d05c6e-a359-5ae9-b151-5301180ecbf5","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Context engineering","source_file":"slide-day-4.html"},"checksum":"839be3b2e3896fc493b5747b3c5196530df20d41a944e8b232cc615112888ddf"} -->

## 04 Context engineering

Slide 20–23: quản lý context window, memory injection, nén, và bốn rổ token.

### Slide 20–23 Bốn rổ token cạnh tranh nhau trong một context window

> Trích slide 
>  " System (policy) · History (recent / relevant) · 
>  Current input (current task) · Tools (schemas) · 
>  Output (buffer)" 
>  " Token budget allocation cần chủ động: đừng để history, tools, và examples ăn hết chỗ dành 
>  cho output. " 
>  " Rổ token — rủi ro nếu quá nhiều: System prompt (policy, rules, format) → 
>  chậm hơn, khó maintain · History (recent turns, facts) → dễ nhiễu, dễ lost in the middle · 
>  Tool schemas (tên tool, mô tả, tham số) → model chọn tool tệ nếu schema dài hoặc mơ 
>  hồ · Output buffer (phần model dùng để trả lời) → bị cắt cụt output nếu cấp 
>  thiếu " 
>  " Context engineering là bài toán chọn lọc và ưu tiên. Nếu mọi thứ đều quan trọng, thực ra không 
>  có gì thực sự nổi bật với model. "

Đây là **slide có giá trị thực hành cao nhất chương**, vì nó biến một khái niệm mơ hồ 
 ("quản lý context") thành một bài toán phân bổ có bốn khoản mục cạnh tranh nhau.

_Sơ đồ: Bốn rổ token cạnh tranh nhau trong một context window - Một thanh ngang biểu diễn context window, chia thành các phần: system prompt, ví dụ few-shot, lịch sử hội thoại, schema của các tool, câu hỏi hiện tại, và phần còn lại dành cho output. Bên dưới liệt kê rủi ro khi mỗi rổ quá lớn: system prompt quá dài thì chậm và khó bảo trì; lịch sử quá dài thì nhiễu và mất thông tin ở giữa; schema tool quá dài hoặc mơ hồ thì model chọn sai tool; và nếu ba rổ trên ăn hết chỗ thì output bị cắt cụt._

Hình 1 — Bốn rổ token (slide 21, 23).

phần còn lại

không tiêu hết

chọn lọc và ưu tiên

Ba rổ System, History, Output khi quá lớn thì hậu quả là *chậm, đắt, hoặc cụt* — khó chịu 
 nhưng dễ nhận ra.

Rổ **tool schemas** thì khác: slide ghi rủi ro là *"model chọn tool tệ nếu schema dài hoặc mơ hồ"*. Đây là lỗi **chất lượng**, không 
 phải lỗi dung lượng — và nó không báo gì cả.

**Hệ quả:** thêm tool *không* miễn phí, kể cả khi 
 context còn dư. Mỗi tool thêm vào làm model có nhiều lựa chọn hơn để chọn nhầm. Đây chính là nguyên 
 tắc *granularity hợp lý* ở [slide 29](#s29), nhìn từ phía context.

#### Tương tác Bốn rổ token — cái gì đang ăn hết context của bạn

Đặt kích thước từng rổ và xem output buffer còn lại bao nhiêu. Mô-đun cũng tính điểm 
 tràn: hội thoại dài tới lượt thứ mấy thì vượt context window.

Mặc định: context **8.000** token · system prompt **800** · **12 lượt** hội thoại × 250 token · **2 tool** × 150 token · 
 câu hỏi hiện tại 200 · không có few-shot.

Đoán trước: output buffer còn bao nhiêu? Và nếu bạn thêm tool từ 2 lên **16**, nó còn 
 bao nhiêu?

#### Kéo rồi mở

**Mặc định: dùng 4.300, còn 3.700 token cho output — thoải mái.**

**Tăng lên 16 tool: schema chiếm 2.400 token, output buffer rơi xuống 1.600.** Vẫn chưa tràn, nhưng đã mất hơn một nửa chỗ trả lời — và *không có thông báo nào* cho bạn 
 biết điều đó đang xảy ra.

**Điều đáng chú ý hơn:** ở 16 tool, rủi ro thật không phải hết chỗ mà là *model chọn sai tool*. Slide 23 ghi rõ rủi ro của rổ này là chất lượng, không phải dung 
 lượng. Bạn có thể còn thừa context mà chất lượng đã tệ đi.

**Thử điều đáng thử nhất — kéo số lượt hội thoại lên 30:** tổng dùng **8.800 > 8.000**, tràn 800 token. Mô-đun báo *số lượt tối đa là 26* với cấu hình 
 mặc định — tức tràn từ lượt thứ 27. Một cuộc hội thoại bình thường sẽ tự vỡ sau khoảng hai chục 
 lượt nếu không có chiến lược nén.

**Và thử thêm 5 ví dụ few-shot × 120 token:** output buffer từ 3.700 xuống **3.100**. Few-shot không miễn phí — nó lấy chỗ của chính câu trả lời, ở mọi lượt gọi.

*Bài học vận hành:* ba rổ đầu phình ra **âm thầm** — system prompt được thêm 
 rule qua thời gian, history tích luỹ theo lượt, tool schema tăng theo số tool. Không rổ nào báo động. 
 Chỉ output buffer bị bóp, và triệu chứng là *câu trả lời cụt giữa chừng* — mà nếu bạn đang 
 dùng JSON thì đó là JSON hỏng.

- **Control - Context window 8.000 token**: min `2000`, max `32000`, step `1000`, default `8000`

- **Control - System prompt 800 token**: min `100`, max `4000`, step `50`, default `800`

- **Control - Lịch sử: 12 lượt × 250 token**: min `0`, max `40`, step `1`, default `12`

- **Control - Tool: 2 tool × 150 token**: min `0`, max `24`, step `1`, default `2`

- **Control - Few-shot: 0 ví dụ × 120 token**: min `0`, max `10`, step `1`, default `0`

Output buffer còn lại

—

—

Rổ chiếm nhiều nhất

—

—

Số lượt tối đa

—

trước khi tràn context

Đã dùng

—

—

system few-shot history tool schemas output buffer còn lại

#### Xem bảng quét số lượt hội thoại



#### Công thức & giới hạn của mô hình

- đã dùng = system + few-shot + history + tool_schemas + input hiện tại; 
 output buffer = context window − đã dùng. Input hiện tại cố định 200 token.
- Các hệ số đều là giả định minh hoạ của tài liệu này, không có trên slide: 
 250 token/lượt hội thoại · 150 token/tool schema · 120 token/ví dụ few-shot. Slide 23 chỉ liệt kê 
 bốn rổ và rủi ro, không đưa con số nào.
- Con số thật của bạn phải đo bằng tokenizer — và với tiếng Việt sẽ cao hơn ước 
 lượng theo số từ ( Ngày 1, slide 30 ).
- Mô hình không tính observation từ tool. Trong agent thật, mỗi tool call thêm 
 cả args lẫn kết quả vào history — nên history phình nhanh hơn nhiều so với hội thoại thuần 
 ( Ngày 3, chương 3 ).
- Giả định mọi lượt hội thoại dài như nhau. Thực tế phân bố lệch — một lượt dán log dài có thể 
 bằng mười lượt bình thường.
- Không mô hình hoá prompt caching, thứ làm phần prefix lặp lại (system prompt) rẻ đi 
 đáng kể ở một số nhà cung cấp. Nó giảm chi phí nhưng không giảm chỗ chiếm 
 trong context.

### Slide 22 Memory injection và ba cách nén context

> Trích slide 
>  " Memory injection: ■ Chỉ đưa vào facts thật sự cần cho task hiện tại ■ Ưu tiên 
>  recent history hoặc relevant history, không dump toàn bộ transcript ■ Tốt cho support agent, 
>  coding assistant, tutor nhiều lượt" 
>  " Compression: ■ Summarize — tóm tắt phần cũ ■ Drop 
>  — bỏ hẳn phần không còn liên quan ■ Archive — đẩy ra ngoài context, chỉ fetch lại khi 
>  cần" 
>  " Context engineering là bài toán chọn lọc và ưu tiên. Nếu mọi thứ đều quan trọng, thực ra không 
>  có gì thực sự nổi bật với model. "

Ba cách nén xếp theo **mức độ mất thông tin**, và chọn đúng cách phụ thuộc vào việc bạn 
 có thể lấy lại thông tin đó hay không:

| Cách | Mất gì | Lấy lại được không | Dùng khi |
| --- | --- | --- | --- |
| Summarize | Chi tiết, giữ ý chính | ✕ Không — bản gốc đã bỏ | Lịch sử hội thoại dài, chi tiết cũ ít có giá trị |
| Drop | Toàn bộ | ✕ Không | Phần chắc chắn không còn liên quan — chào hỏi, thử nghiệm ban đầu |
| Archive | Không mất — chỉ dời ra ngoài | ✓ Có — fetch lại khi cần | Thông tin có thể cần lại nhưng không phải lúc nào cũng cần |

"Đẩy ra ngoài context, chỉ fetch lại khi cần" là mô tả chính xác của **retrieval**. 
 Bạn không mất thông tin, chỉ trả tiền cho nó *khi dùng* thay vì ở mọi lượt.

Đó là lý do Ngày 7–8 (embedding, chunking, RAG) đứng ngay sau bài này: chúng là cách cài đặt *archive* cho tử tế — cần một chiến lược lưu và một chiến lược tìm lại.

**Và đây là cùng câu chuyện với [long-term 
 memory ở Ngày 3](slide-buoi-3.html):** slide đó cảnh báo *"memory chỉ có ích khi chiến lược đọc/ghi và quyền 
 truy cập được thiết kế rõ"*. Archive không có chiến lược fetch tốt thì bằng Drop — thông tin có 
 đó mà không bao giờ lấy đúng lúc.

"Nếu mọi thứ đều quan trọng, thực ra không có gì thực sự nổi bật với model."

"context rác = attention rác"

Ngày 1

nhiễu

mất tương phản

thật sự

---

<!-- chiron-source-span: {"source_span_id":"2c5ff31f-657d-5ea5-b421-bed620ae4223","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Tool calling","source_file":"slide-day-4.html"},"checksum":"981701df12111218b041efeb4c44a3a2ff8d550e6656399c2602477754179286"} -->

## 05 Tool calling

Slide 24–27: luồng tool calling, và bốn phần của một tool schema.

### Slide 24–25 Luồng tool calling — và chỗ nhiều người hiểu sai nhất

> Trích slide 
>  "LLM decides → tool_call JSON → App executes tool → tool result → LLM 
>  final response " 
>  " Model không tự chạy code hay tự gọi API ngoài. Ứng dụng của bạn nhận tool request, chạy 
>  tool, rồi gửi kết quả trở lại model. "

Câu in đậm sửa **hiểu lầm phổ biến nhất về tool calling**, và nó có nhiều hệ quả thực 
 hành hơn vẻ ngoài.

_Sơ đồ: Luồng tool calling bốn bước, trong đó ứng dụng chạy tool chứ không phải model - Model nhận yêu cầu và quyết định gọi tool, trả về một khối JSON mô tả tên tool và tham số. Ứng dụng của bạn nhận khối JSON đó, tự chạy tool thật, rồi gửi kết quả trở lại model. Model đọc kết quả và sinh câu trả lời cuối. Đường viền đứt bao quanh model cho thấy model không bao giờ chạm trực tiếp vào API hay cơ sở dữ liệu; mọi thao tác thật đều do ứng dụng thực hiện, và đó là nơi bạn đặt kiểm tra quyền, timeout và ghi log._

Hình 2 — Luồng tool calling (slide 25).

đề nghị

thực thi

**① Bạn luôn có một chỗ để chặn.** Trước khi `run_tool` chạy, code của bạn 
 thấy đầy đủ tên tool và tham số. Đó là chỗ tự nhiên để kiểm quyền, validate args, hoặc yêu cầu người 
 duyệt — chính là *cổng approval* trong SmartCheck AI và HITL ở [Ngày 2](slide-buoi-2.html).

**② Model không thể "vô tình" xoá dữ liệu.** Nếu nó đề nghị gọi `delete_all_orders` mà bạn không đăng ký tool đó, không có gì xảy ra. Quyền hạn thật nằm ở 
 danh sách tool bạn cung cấp — đây là phòng thủ mạnh nhất chống OWASP LLM06 
 ( *excessive agency*, [Ngày 24](track-3-day-24.html) ).

**③ Mọi observation trong trace đều do code bạn chèn vào.** Đây chính là cách chặn thật cho rule *"never invent tool results"* mà [Ngày 3](slide-buoi-3.html) nói prompt một mình không đảm bảo được.

đề nghị

bạn phải chủ động gửi cả lỗi

Ngày 3, slide 30

### Slide 26–27 Tool schema anatomy — bốn phần

> Trích slide 
>  "■ Name: nên ngắn, rõ, động từ đúng việc ■ Description: nói 
>  khi nào nên dùng tool này ■ Parameters: mô tả input bằng JSON Schema 
>  ■ Required fields: giúp model biết thiếu gì thì chưa gọi được" 
>  " LLM đọc description như tài liệu hướng dẫn. Nếu description mơ hồ, model sẽ chọn sai tool 
>  hoặc truyền sai arguments. " 
>  "name": "get_weather", "description": "Get current weather for a city when the user asks about 
>  weather conditions.", "parameters": {"city": {"type": "string", "description": "City name, e.g. 
>  Hanoi"}}, "required": ["city"]

Chú ý cách slide định nghĩa **Description**: không phải "tool này làm gì" mà là *"nói **khi nào nên dùng** tool này"*. Khác biệt nhỏ về câu chữ, lớn về hiệu quả:

|  | Description kém | Description tốt |
| --- | --- | --- |
| Cách viết | Mô tả chức năng: "Lấy thời tiết" | Mô tả tình huống dùng: "Get current weather for a city when the user asks about weather conditions " |
| Model dùng nó để | Đoán xem tool làm gì | Quyết định có nên gọi hay không |
| Hỏng khi | Hai tool nghe giống nhau ⇒ chọn nhầm | — |

Schema mẫu có Name ✓, Description ✓ (có cả "when"), Parameters ✓ (có cả ví dụ "e.g. Hanoi"), 
 Required ✓. **Nhưng không có error mode**: điều gì xảy ra nếu không tìm thấy thành phố? 
 Nếu dịch vụ thời tiết lỗi?

[Ngày 3, slide 19](slide-buoi-3.html) đã nêu yêu cầu *"rõ input / output / error 
 mode"*, và [bài tập về nhà slide 40](#s39) của chính Ngày 4 cũng đòi: *"thử viết lại tool description theo hướng rõ input, output, và failure mode hơn"*.

**Bản đầy đủ hơn:** *"Get current weather for a city when the user asks about weather conditions. 
 Returns temperature range and rain probability. 
 Returns `{error: 'city_not_found'}` if the city name is unrecognized — in that case, ask 
 the user to clarify instead of retrying."* 
 Câu cuối là câu đáng giá nhất: nó **nói cho model biết phải làm gì khi lỗi**, thay vì 
 để nó tự đoán và gọi lại y hệt.

thiếu gì thì chưa gọi được

hỏi lại người dùng

city

required

city="Hanoi"

"làm rõ ý định"

Ngày 2

---

<!-- chiron-source-span: {"source_span_id":"4e4b019f-88e0-5950-957b-ee9bd05d844c","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Nguyên tắc thiết kế tool","source_file":"slide-day-4.html"},"checksum":"519690602503749e442e7cef209418a93edfcf6a9c9c0dc428343d79512c9b45"} -->

## 06 Nguyên tắc thiết kế tool

Slide 28–30: bốn nguyên tắc, và bài toán granularity.

### Slide 28–30 Bốn nguyên tắc, và tool quá nhỏ hay quá to đều có giá

> Trích slide 
>  " Single Responsibility — mỗi tool làm 1 việc rõ ràng. Vi phạm: model khó quyết 
>  định nên gọi tool nào. Idempotency — cùng input cho cùng kết quả; side effect 
>  được kiểm soát. Vi phạm: retry dễ sinh lỗi phụ. Granularity hợp lý — không 
>  quá nhỏ, cũng không ôm quá nhiều việc. Test độc lập — unit test từng tool trước khi 
>  gắn vào agent. Vi phạm: khó tách lỗi tool khỏi lỗi prompt. " 
>  " Quá nhỏ: get_customer_name, get_customer_email, 
>  get_customer_phone → quá nhiều calls, overhead lớn, flow rối. 
>  Quá to: handle_all_customer_operations → model không hiểu boundary, 
>  khó debug, khó reuse." 
>  " Thiết kế tool quanh một hành động nghiệp vụ rõ ràng: lookup_order, get_weather, 
>  query_sales_data, send_email_draft. "

**Idempotency** là nguyên tắc ít được nhắc nhất và có hệ quả nghiêm trọng nhất — 
 vì nó là điều kiện để *retry an toàn*:

Agent **retry theo thiết kế**: khi tool lỗi, khi model thấy kết quả chưa đủ, khi 
 guardrail phát hiện vấn đề. [Ngày 3, slide 30](slide-buoi-3.html) liệt kê "retry có kiểm 
 soát" là một trong năm guardrail bắt buộc.

Nếu `send_email` không idempotent, một lần retry là một email thứ hai gửi cho khách hàng. 
 Nếu `charge_card` không idempotent, đó là một lần trừ tiền thứ hai.

**Cách làm cho idempotent trong thực tế:** thêm một *khoá thao tác* (idempotency key) vào tham số — cùng khoá thì lần gọi thứ hai trả về kết quả 
 lần đầu thay vì thực hiện lại. Đây là kỹ thuật chuẩn của API thanh toán, và nó áp thẳng cho tool của 
 agent. Với tool *chỉ đọc* ( `lookup_order`, `get_weather` ) thì idempotency 
 là miễn phí — đó là lý do nên tách rõ tool đọc và tool ghi.

**Bài toán granularity** có một tiêu chí đơn giản mà slide đưa ra ở câu cuối — *"quanh một hành động nghiệp vụ rõ ràng"*. Bảng dưới cụ thể hoá:

|  | Quá nhỏ | Vừa | Quá to |
| --- | --- | --- | --- |
| Ví dụ | get_customer_name get_customer_email | lookup_customer | handle_all_customer_operations |
| Số lượt gọi | Nhiều — mỗi trường một lượt | Một | Một |
| Vấn đề | Overhead lớn, flow rối, tốn token vì mỗi lượt đọc lại history | — | Model không hiểu boundary, khó debug, khó reuse |
| Chi phí ẩn | Chiếm nhiều chỗ trong rổ tool schema | — | Description phải mô tả quá nhiều tình huống ⇒ dài và mơ hồ |

**Quá nhỏ:** mười tool na ná nhau ⇒ model phải phân biệt giữa mười lựa chọn gần giống 
 — vi phạm *Single Responsibility* ở chiều ngược lại (mỗi tool quá hẹp nên ranh giới giữa chúng 
 mờ).

**Quá to:** một tool ôm mọi việc ⇒ description phải liệt kê mọi tình huống ⇒ dài và 
 mơ hồ ⇒ đúng cảnh báo [rổ tool schema ở slide 23](#s21): *"model chọn tool tệ nếu schema dài hoặc mơ hồ"*.

**Tiêu chí thực dụng:** một tool nên tương ứng với *một câu bạn nói với đồng nghiệp* — "tra giúp đơn hàng này", "kiểm phòng còn trống không". 
 Nếu bạn phải nói hai câu để mô tả tool, nó quá to. Nếu bạn phải nói ba tool để làm một việc, chúng 
 quá nhỏ.

"Unit test từng tool trước khi gắn vào agent. Vi phạm: khó tách lỗi tool khỏi lỗi prompt."

slide 42

"Bạn đang gặp lỗi vì model chưa hiểu ý bạn, hay vì tool contract chưa đủ rõ?"

loại trừ được một nửa không gian tìm kiếm

---

<!-- chiron-source-span: {"source_span_id":"e5d7b022-c886-5cf3-8df6-64741a944e0e","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Parallel tool calls & patterns","source_file":"slide-day-4.html"},"checksum":"46785bb9f84cdf637b63806293e12238615d1cdfbf5840509c7299a79178a0ba"} -->

## 07 Parallel tool calls & patterns

Slide 31–34: tuần tự và song song, ba pattern dùng tool, và vòng lặp tool tối thiểu.

### Slide 31–32 Sequential vs Parallel — điều kiện duy nhất để song song hoá

> Trích slide 
>  " Sequential: Tool B cần output của Tool A. Ví dụ: tìm order ID → rồi mới tra 
>  shipping status. Parallel: Các tool độc lập có thể chạy cùng lúc. 
>  Ví dụ: gọi thời tiết, tỷ giá, và lịch họp song song. " 
>  " Chỉ song song hóa khi không có phụ thuộc dữ liệu. Nếu vẫn cần bước merge / verify rõ ràng 
>  ở cuối. " 
>  " Nhanh hơn không có nghĩa là tốt hơn nếu flow control và merge logic không rõ. "

_Sơ đồ: So sánh gọi tool tuần tự và song song về thời gian - Nửa trên là gọi tuần tự: ba tool chạy nối tiếp nhau vì tool sau cần kết quả tool trước, tổng thời gian là tổng ba khoảng. Nửa dưới là gọi song song: ba tool độc lập chạy cùng lúc, tổng thời gian bằng tool chậm nhất, sau đó có một bước gộp kết quả. Ghi chú nhấn mạnh chỉ song song hoá được khi không có phụ thuộc dữ liệu giữa các tool, và tiền vẫn cộng dồn như nhau ở cả hai cách._

Hình 3 — Tuần tự và song song (slide 32).

Ngày 25

tiền cộng theo tổng, thời gian cộng theo cái 
 chậm nhất

**① Tiền không giảm.** Ba tool song song vẫn là ba lời gọi API. Bạn mua tốc độ, không 
 mua chi phí.

**② Bước merge phải xử lý lỗi từng phần.** Nếu `get_fx` lỗi mà hai tool kia 
 thành công thì sao? Trả lời với dữ liệu thiếu? Báo lỗi toàn bộ? Đây là quyết định thật, và nó không tồn 
 tại ở luồng tuần tự (nơi bạn dừng ngay khi tool đầu lỗi).

**③ Trace khó đọc hơn.** Tuần tự thì thứ tự trong trace phản 
 ánh thứ tự nhân quả. Song song thì ba observation về gần như cùng lúc, và bạn mất thông tin về việc 
 cái nào ảnh hưởng cái nào. Với một pattern mà giá trị chính là *debug được* ( [Ngày 3](slide-buoi-3.html) ), đó là mất mát có thật.

"tham số của tool B có chứa thứ gì lấy từ kết quả tool A không?"

lookup_order

get_shipping

### Slide 33–34 Ba pattern dùng tool, và vòng lặp tối thiểu

> Trích slide 
>  "1. Conditional tool use: agent tự quyết định có cần tool hay trả lời trực tiếp. 
>  2. Tool chaining: output của tool A là input của tool B. 
>  3. Parallel fetch + merge: lấy nhiều nguồn độc lập rồi tổng hợp kết quả." 
>  " Tool calling không chỉ là 'gọi API'. Nó là bài toán control flow: khi nào gọi, gọi cái gì, 
>  gọi theo thứ tự nào, và làm gì khi tool fail. " 
>  " Vòng lặp tối thiểu: for item in response.output: if item.type == "function_call": 
>  result = run_tool(item.name, json.loads(item.arguments)); messages.append(item); 
>  messages.append({"type": "function_call_output", "call_id": item.call_id, "output": result}) "

Pattern thứ nhất — **conditional tool use** — là pattern quan trọng nhất và cũng là thứ 
 mà deliverable của bài đòi chứng minh:

| Pattern | Câu hỏi control flow nó trả lời | Hỏng thì triệu chứng |
| --- | --- | --- |
| 1 · Conditional | Khi nào gọi tool — hay trả lời thẳng? | Gọi tool cho mọi câu, kể cả câu tự trả lời được ⇒ chậm và tốn vô ích |
| 2 · Chaining | Gọi theo thứ tự nào? | Gọi tool B trước khi có dữ liệu từ A ⇒ args sai ⇒ lỗi hoặc kết quả rác |
| 3 · Parallel + merge | Gọi cái gì cùng lúc, gộp thế nào? | Không xử lý được lỗi từng phần ⇒ một nhánh lỗi làm hỏng cả câu trả lời |
| — | Làm gì khi tool fail? | Câu hỏi thứ tư — và không pattern nào ở đây trả lời nó |

Slide 33 liệt kê bốn câu hỏi control flow: *khi nào gọi, gọi cái gì, gọi theo thứ tự nào, **và làm gì khi tool fail***. Ba pattern giải ba câu đầu.

Câu thứ tư — xử lý lỗi tool — là chủ đề của [Ngày 25](track-3-day-25.html): timeout, 
 circuit breaker, fallback chain, retry có kiểm soát. Ở Ngày 4 bạn chỉ cần biết **nó là một câu hỏi riêng và chưa được trả lời**.

**Việc tối thiểu làm được ngay:** khi `run_tool` ném exception, *đừng nuốt lỗi* — gửi thông báo lỗi về cho model như một observation, kèm gợi ý 
 nên làm gì. Nếu không, model tưởng chưa gọi và sẽ gọi lại — đúng dấu hiệu kẹt vòng lặp ở [Ngày 3](slide-buoi-3.html).

Ba dòng quan trọng:

① `if item.type == "function_call"` — model *đề nghị*, code kiểm tra. 
 ② `result = run_tool(...)` — **code chạy tool**, không phải model. 
 ③ `messages.append({"type": "function_call_output",...})` — **code chèn 
 observation** vào lịch sử.

Ba dòng này chính là ba mũi tên trong [Hình 2](#f2), và dòng ③ 
 là cơ chế thật đảm bảo rule *"never invent tool results"*. Chú ý cả `call_id` — nó ghép kết quả với đúng lời gọi, cần thiết khi có nhiều tool call song song.

---

<!-- chiron-source-span: {"source_span_id":"b01515e2-02c3-5d3c-8c3b-735d3e543be4","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Lab 4 & tổng kết","source_file":"slide-day-4.html"},"checksum":"ec6a86ce4c3ac23d87369f1b083bec1d7cd4876c5799e598ef4df95592a66b31"} -->

## 08 Lab 4 & tổng kết

Slide 35–43: cách chạy lab, bốn ý chốt, và bài tập về nhà.

### Slide 35–38 Lab 4 — chú ý bước 5

> Trích slide 
>  "1. Viết 1 system prompt với rules, constraints, output format 2. Tạo 2 custom tools: 1 API wrapper 
>  đơn giản, 1 data query đơn giản 3. Nối tools vào agent loop 4. Chạy 5 câu test để xem khi nào agent trả 
>  lời trực tiếp, khi nào gọi tool 5. Ghi lại lỗi thuộc loại prompt, tool schema, hay control 
>  flow " 
>  " Deliverable: Agent script chạy được + system prompt + 2 tool schemas + 5 test 
>  outputs + note lỗi prompt/tool/control flow. Thời gian: 150 phút"

Bước 5 — **phân loại lỗi thành ba nhóm** — là bước dạy nhiều nhất, vì nó buộc bạn 
 chẩn đoán thay vì chỉ sửa cho chạy:

| Loại lỗi | Triệu chứng | Sửa ở đâu | Cách xác nhận |
| --- | --- | --- | --- |
| Prompt | Sai tone, sai format, không tuân rule, không nhất quán giữa các lần | System prompt — rules, constraints, output format | Sửa prompt, chạy lại 5 test, xem có hết không |
| Tool schema | Chọn nhầm tool · args sai · gọi tool khi không cần | Description (nhất là phần "khi nào dùng") · required fields | Unit test tool riêng — nếu tool chạy đúng khi gọi tay thì lỗi ở schema |
| Control flow | Kẹt vòng lặp · không dừng đúng lúc · không xử lý tool lỗi | Code vòng lặp — điều kiện dừng, safeguard, xử lý exception | Đọc trace: thứ tự các bước có hợp lý không |

*"Bạn đang gặp lỗi vì model chưa hiểu ý bạn, hay vì tool contract của bạn chưa đủ rõ?"* — 
 và Ngày 4 thêm nhóm thứ ba: control flow, tức lỗi trong code của bạn.

**Cách khoanh vùng nhanh nhất** là nguyên tắc *test độc lập* ở [slide 29](#s29): nếu tool đã có unit test xanh, bạn loại được nhóm 
 hai ngay, còn lại hai nhóm. Rồi đọc trace: nếu Thought hợp lý mà thứ tự bước sai ⇒ control flow; 
 nếu Thought đã đi lạc ⇒ prompt. Ba nhóm, hai bước loại trừ.

### Slide 39–43 Bốn ý chốt và bài tập về nhà

> Trích slide 
>  "1 Prompt = interface giữa human intent và model capability. Prompt tốt giúp model 
>  làm đúng việc, đúng format, đúng boundary. 
>  2 System prompt tốt = agent nhất quán và predictable hơn, đặc biệt khi có tools và 
>  constraints. 
>  3 Tool schema description quyết định rất mạnh việc model biết khi nào dùng tool nào và 
>  gọi với arguments gì. 
>  4 Parallel tool calls nhanh hơn đáng kể khi các tool độc lập; nếu có phụ thuộc dữ 
>  liệu, hãy giữ flow tuần tự." 
>  " Bài tập: Hoàn thiện Lab 4 với 5 test questions rõ pass/fail · 
>  Đọc lại system prompt của mình và chỉ ra 2 chỗ còn mơ hồ hoặc mâu thuẫn " 
>  " Tiếp theo — AI Product Thinking & Requirements: 'Bạn đã build được agent đầu tiên. Nhưng 
>  build xong chưa đủ. Ngày mai: sản phẩm này dành cho ai, yêu cầu ra sao, và rủi ro nào phải nghĩ từ 
>  đầu?' "

Ý số 3 đáng nhấn lại vì nó là **phát hiện thực dụng nhất của cả bài**: *tool schema description quyết định rất mạnh*. Đây là một đòn bẩy lớn nằm ở chỗ ít ai nghĩ tới.

Model không đọc code tool của bạn. Nó chỉ thấy **tên, mô tả, và schema tham số** — 
 đúng ba thứ đó, không hơn. Với model, description *là* tool.

Nghĩa là một tool được viết hoàn hảo với description mơ hồ sẽ hoạt động tệ hơn một tool đơn giản 
 với description rõ. Slide 26 nói đúng bản chất: *"LLM đọc description như tài liệu hướng dẫn."*

**Và đây là tin tốt:** sửa description rẻ hơn nhiều so với sửa 
 code. Khi agent chọn sai tool, chỗ đầu tiên nên nhìn không phải logic mà là *hai description có 
 phân biệt được với nhau không*.

"Đọc lại system prompt của mình và chỉ ra 2 chỗ còn mơ hồ hoặc mâu thuẫn."

"Trong prompt này, có cặp chỉ dẫn nào mâu thuẫn nhau không? Có chỉ dẫn nào không kiểm chứng được 
 không?"

slide 19

"tôi kiểm được điều này không?"

#### Ô kiểm tra — Chương 4, 5, 6 & 7

Trả lời thành tiếng trước khi mở đáp án.

**1.** Agent của bạn thỉnh thoảng trả về JSON bị cắt cụt ở giữa. Không có lỗi nào 
 trong log. Chẩn đoán. Phân tích

#### Đáp án

**Output buffer bị bóp — ba rổ token phía trước đã ăn hết chỗ.**

Slide 23 ghi rõ rủi ro của rổ output buffer: *"bị cắt cụt output nếu cấp thiếu"*. Và nó là 
 rổ **còn lại**, không phải rổ được cấp — nên không có gì báo động khi nó teo dần.

**Ba nguyên nhân phình âm thầm:** system prompt được thêm rule qua thời gian · 
 lịch sử tích luỹ theo lượt (và với agent, mỗi tool call thêm cả args lẫn observation) · 
 tool schema tăng theo số tool.

**Kiểm chứng:** in ra số token của từng rổ ở lượt gọi bị lỗi. Hoặc dùng [mô-đun bốn rổ](#m-tok) để ước lượng — với cấu hình mặc định, hội thoại tràn ở *lượt thứ 24*.

**Sửa theo thứ tự:** ① tóm tắt/cắt history (rổ lớn nhất và phình nhanh nhất) → 
 ② rà lại system prompt, xoá phần không đổi hành vi → ③ giảm số tool hoặc rút gọn schema → 
 ④ nếu vẫn thiếu, đặt `max_tokens` tường minh và kiểm `finish_reason == "length"` trước khi parse.

**2.** Vì sao "model không tự chạy tool" lại là tin tốt về mặt an 
 toàn? Hiểu

#### Đáp án

**Vì mọi thao tác thật đều đi qua code của bạn — nên bạn luôn có một chỗ để chặn.**

Model chỉ *đề nghị* gọi tool bằng một khối JSON. Ứng dụng của bạn nhận khối đó, và *trước khi* chạy bất cứ gì, bạn thấy đầy đủ tên tool và tham số.

**Ba hệ quả cụ thể:**

① **Chỗ đặt guardrail tự nhiên** — kiểm quyền, validate args, hoặc yêu cầu người 
 duyệt (cổng approval, HITL). 
 ② **Quyền hạn nằm ở danh sách tool bạn cung cấp** — model đề nghị gọi `delete_all_orders` mà bạn không đăng ký thì không có gì xảy ra. Đây là phòng thủ mạnh 
 nhất chống *excessive agency* (OWASP LLM06). 
 ③ **Mọi observation trong trace do code bạn chèn** — đây là cơ chế thật đảm bảo rule 
 "never invent tool results", thứ mà prompt một mình không đảm bảo được.

**Mặt trái cần biết:** vì model không tự biết tool chạy thế nào, bạn *phải chủ 
 động gửi cả lỗi về*. Nuốt exception thì model tưởng chưa gọi và sẽ gọi lại — kẹt vòng lặp.

**3.** Bạn có hai tool: `lookup_order(order_id)` và `get_shipping_status(order_id)`. Khách hỏi "đơn của tôi tới đâu rồi, mã ABC123?". 
 Song song hay tuần tự? Còn nếu khách hỏi "thời tiết Hà Nội và tỷ giá USD hôm nay?" Áp dụng

#### Đáp án

**Câu 1: có thể song song — vì khách đã cho mã đơn.** Cả hai tool đều nhận `order_id = "ABC123"`, không tool nào cần kết quả của tool kia.

*Nhưng chú ý ví dụ của slide 32 là tuần tự* — vì ở đó phải *tìm* order ID trước rồi 
 mới tra shipping. Khác biệt nằm ở chỗ khách có cung cấp mã hay không. Đây là bài học tinh tế: **cùng bộ tool, phụ thuộc dữ liệu đổi theo input**.

**Câu 2: song song rõ ràng** — thời tiết và tỷ giá hoàn toàn độc lập, đúng ví dụ 
 slide 32.

**Cách kiểm chung:** với mỗi cặp tool, hỏi *"tham số của tool B có chứa thứ gì 
 lấy từ kết quả tool A không?"* Có ⇒ tuần tự bắt buộc.

**Và phải nói cái giá của song song:** tiền không giảm (vẫn hai lời gọi API); 
 bước merge phải xử lý được trường hợp một nhánh lỗi mà nhánh kia thành công; và trace khó đọc hơn vì 
 mất thông tin về thứ tự nhân quả.

---

<!-- chiron-source-span: {"source_span_id":"9b564e16-ade6-576c-b905-554841643e16","locator":{"kind":"html_section","section_id":"ladder","order":11,"heading":"▤ Luyện kỹ năng cốt lõi: khoanh vùng lỗi và viết contract","source_file":"slide-day-4.html"},"checksum":"d6e339f53386078a95de07d04e50e46f0a3eb9947c05406a81942793394f17b5"} -->

## ▤ Luyện kỹ năng cốt lõi: khoanh vùng lỗi và viết contract

Ba bài giảm dần giàn giáo. Làm đúng thứ tự.

① Tool có unit test xanh không?

tool schema

② Đọc trace: Thought có đi đúng mục tiêu không?

prompt

control flow

③ Sửa ở chỗ rẻ nhất trước

④ Chạy lại 5 test, xác nhận hết lỗi mà không sinh lỗi mới

#### Agent hỗ trợ có hai tool: lookup_order và check_refund_eligibility. Nó liên tục gọi nhầm tool thứ hai khi khách chỉ hỏi tình trạng đơn

Đọc cách *lập luận*, không chỉ đáp án.

1. Khoanh vùng trước: đây là nhóm nào? Chạy unit test hai tool — cả hai xanh, gọi 
 tay đều trả đúng. Nhưng đó chưa loại được nhóm tool schema, vì test kiểm code còn 
 lỗi có thể ở description. Đọc trace: Thought nói đúng mục tiêu ("khách hỏi tình trạng đơn"), 
 nhưng Action chọn sai tool ⇒ nhóm tool schema, cụ thể là description. 
 Cách nhận ra: Thought đúng + Action sai = model hiểu việc nhưng không phân biệt được tool.
2. Đọc hai description cạnh nhau. Giả sử chúng là: 
 "Look up an order" và "Check refund for an order". Cả hai đều chỉ mô tả 
 chức năng, không mô tả khi nào dùng — đúng lỗi mà 
 slide 26 cảnh báo. Model phải tự đoán ranh giới, và "check refund for an order" 
 nghe cũng liên quan tới đơn hàng.
3. Sửa ở chỗ rẻ nhất: viết lại description theo hướng "khi nào dùng". 
 lookup_order: "Get status, items, and delivery date of an order. Use when the user 
 asks where their order is, what they ordered, or when it arrives. Returns 
 {error:'not_found'} if the ID is invalid — ask the user to check the code instead of 
 retrying." 
 check_refund_eligibility: "Check whether an order qualifies for a refund under return policy. 
 Use ONLY when the user explicitly asks about refund, return, or cancellation. 
 Do not call this to answer status questions."
4. Xác nhận: chạy lại 5 test. Kỳ vọng: ca hỏi tình trạng gọi đúng 
 lookup_order; ca hỏi hoàn tiền gọi đúng tool thứ hai. Và thêm một ca mới: câu 
 không cần tool nào ("mấy giờ các bạn đóng cửa?") — để kiểm conditional tool use, đúng điều 
 deliverable đòi.

Câu chốt kiểu vấn đáp "Thought đúng mục tiêu mà Action chọn sai tool, nên lỗi nằm ở tool schema chứ không phải prompt. Hai 
 description chỉ mô tả chức năng, không mô tả khi nào dùng — nên ranh giới giữa chúng mờ. Em viết lại 
 theo hướng 'use when…', thêm cả một câu 'do not call this to…' cho tool dễ bị gọi nhầm, và thêm error 
 mode để model biết làm gì khi không tìm thấy. Em kiểm bằng 5 test cũ cộng một ca không cần tool nào."

#### System prompt của bạn dài 2.400 token. Agent chạy đúng nhưng chậm và tốn. Bạn muốn cắt.

Hai bước đầu cho sẵn. Hai bước sau tự viết rồi mới mở.

1. 2.400 token là cờ đỏ theo anti-pattern thứ nhất ( slide 19: 
 "nhồi mọi thứ vào 1 prompt 2000+ tokens"). Và vì system prompt gửi lại ở mọi lượt gọi, nó là 
 rổ token đáng tối ưu nhất trong hội thoại nhiều lượt.
2. Nhưng không được cắt theo cảm giác. System prompt là policy layer — 
 nó chứa constraints và output contract. Cắt nhầm một constraint là mở lại một chế độ hỏng mà bạn đã 
 đóng.
3. ③ Quy trình cắt an toàn gồm những bước nào, và điều kiện tiên quyết là 
 gì? (gợi ý: rule thực dụng ở slide 10 có một chữ ẩn — "không làm thay đổi hành vi mong 
 muốn" — làm sao biết được điều đó?)
4. ④ Nếu đọc kỹ thấy prompt có cả danh sách 30 sản phẩm và bảng giá — xử lý 
 thế nào?

#### Đáp án hai bước còn lại

**③ Điều kiện tiên quyết: phải có bộ test.** Rule ở slide 10 — *"nếu prompt dài thêm nhưng không làm thay đổi hành vi mong muốn, hãy cắt bớt"* — chỉ áp dụng 
 được nếu bạn *đo được* hành vi. Không có bộ test thì mọi lời khuyên về cắt prompt đều là đoán.

**Quy trình:**

① Dựng bộ test có ít nhất 5 ca, gồm **ba ca biên** mà anti-pattern thứ tư nhắc: 
 câu ngoài phạm vi · thiếu thông tin · tool trả lỗi. 
 ② Chạy để lấy baseline. 
 ③ **Xoá từng đoạn một** (không xoá nhiều đoạn cùng lúc), chạy lại. Đoạn nào xoá mà mọi 
 test vẫn pass ⇒ token thừa. Đoạn nào xoá mà có test hỏng ⇒ đoạn đó đang gánh việc, giữ lại. 
 ④ Ưu tiên soi khối *Persona* và *Rules* trước — hai khối "định hình". Khối *Constraints* và *Output format* soi sau và cẩn thận hơn, vì chúng là khối "ràng buộc": 
 hỏng thì hậu quả là sự cố thật, không chỉ chất lượng kém.

**④ Danh sách 30 sản phẩm và bảng giá KHÔNG thuộc system prompt.**

Slide 19 nói: *"system prompt là policy layer"* — chỗ đặt **luật**, không phải 
 chỗ đặt **dữ liệu**. Để dữ liệu ở đó nghĩa là trả tiền cho toàn bộ 30 sản phẩm ở mọi lượt 
 gọi, kể cả khi khách chỉ hỏi về một sản phẩm.

**Hai phương án, theo mức độ:**

• **Archive** ( [slide 22](#s22) ): đẩy ra ngoài context, cho model một tool `lookup_product(name)` để tra khi cần. Đây là phương án đúng — bạn chỉ trả tiền khi dùng. 
 • **Retrieval**: nếu danh sách lớn hơn nữa, dùng RAG (Ngày 7–8) để lấy đúng vài mục liên 
 quan vào context.

**Ước lượng lợi ích:** nếu bảng giá chiếm khoảng 1.200 token, cắt nó ra là giảm một 
 nửa system prompt — và với 1.500 lượt gọi mỗi ngày là gần 54 triệu token mỗi tháng.

#### Viết lại tool schema và rà system prompt cho SmartCheck AI

Không có gợi ý. Làm rồi so với [mục áp dụng](#apply).

1. Chọn hai tool mà kiosk đang dùng (ví dụ: tra đặt phòng theo tên/mã, kiểm phòng 
 còn trống). Viết lại schema đầy đủ bốn phần — và thêm phần thứ năm mà slide bỏ sót: 
 error mode.
2. Rà system prompt hiện tại theo bốn anti-pattern ở 
 slide 19. Với mỗi chỉ dẫn, hỏi câu kiểm: "tôi kiểm được điều này không?"
3. Đếm token bốn rổ bằng mô-đun hoặc bằng tokenizer thật. 
 Rổ nào đang chiếm nhiều nhất? Output buffer còn bao nhiêu ở lượt thứ 15?
4. Thiết kế 5 test case — nhớ có ít nhất một ca không cần tool nào, và ba 
 ca biên (ngoài phạm vi, thiếu thông tin, tool lỗi).

tra đặt phòng

khi nào model KHÔNG được gọi

"Do not call this tool to answer general questions about hotel services. Only call 
 when the guest is checking in and has provided a booking code or full name."

Boundary

Ngày 2

---

<!-- chiron-source-span: {"source_span_id":"d1ef52c2-758a-5227-b794-24980c8af179","locator":{"kind":"html_section","section_id":"misc","order":12,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"slide-day-4.html"},"checksum":"02cd9e1ed758292d61f491a1bf831c1a42c65f5b0f886e398aeb55358c1fefb6"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Mỗi thẻ: niềm tin phổ biến, lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng.

*Vì sao nghe hợp lý:* trải nghiệm người dùng đúng là như vậy — hỏi thời tiết thì nhận thời 
 tiết thật. Và tài liệu hay dùng cụm "model gọi tool".

Model chỉ **đề nghị** bằng một khối JSON. *Ứng dụng của bạn* nhận khối đó, chạy 
 tool, rồi gửi kết quả về. Slide 25 nói thẳng: *"Model không tự chạy code hay tự gọi API ngoài."*

**Ba hệ quả:** ① bạn luôn có một chỗ để chặn (guardrail, approval) ② quyền hạn nằm ở 
 danh sách tool bạn đăng ký — phòng thủ mạnh nhất chống *excessive agency* ③ mọi observation do 
 code bạn chèn, nên rule "never invent tool results" mới thật sự được đảm bảo.

[Hình 2](#f2) — đường đứt bao quanh model · [slide 34](#s33) — vòng lặp tối 
 thiểu, dòng `result = run_tool(...)`.

*Vì sao nghe hợp lý:* trong lập trình thường, docstring đúng là để người đọc. Code mới là 
 thứ quyết định hành vi.

**Model không đọc code tool của bạn.** Nó chỉ thấy tên, description, và schema tham số 
 — đúng ba thứ đó. Với model, *description LÀ tool*.

Slide 26: *"LLM đọc description như tài liệu hướng dẫn. Nếu description mơ hồ, model sẽ chọn sai 
 tool hoặc truyền sai arguments."* Một tool viết hoàn hảo với description mơ hồ hoạt động tệ hơn 
 một tool đơn giản với description rõ.

**Tin tốt:** sửa description rẻ hơn nhiều so với sửa code.

[Slide 26](#s26) · [Bài 1](#ladder) — Thought đúng + Action sai = lỗi ở 
 description.

*Vì sao nghe hợp lý:* nói rõ hơn thì hiểu đúng hơn — đúng với người. Và ai cũng từng thấy 
 một prompt dài cho kết quả tốt hơn prompt cụt.

*"Specificity beats cleverness"* — cái làm nên khác biệt là **độ rõ**, không 
 phải độ dài. Ví dụ "prompt tốt" ở slide 7 chỉ dài *một câu*.

Và prompt dài có ba chi phí: token (ở mọi lượt gọi), latency, và **nhiễu** — *"nếu mọi thứ đều quan trọng, thực ra không có gì thực sự nổi bật với model"* (slide 22).

**Rule kiểm:** xoá một đoạn, chạy lại bộ test. Test không đổi ⇒ đoạn đó là token thừa.

[Slide 10](#s9) — rule thực dụng · [Slide 19](#s19) — anti-pattern "quá dài".

*Vì sao nghe hợp lý:* cho ví dụ đúng thì model bắt chước — nghe rất hợp lý, và với lỗi 
 format thì đúng thật.

Slide 13 nêu tiêu chí rất rõ: dùng few-shot *"khi model **hiểu task** nhưng ra sai 
 format hoặc không ổn định"*. Nếu model sai vì **không biết**, few-shot chỉ dạy nó 
 trình bày câu sai cho đẹp hơn — và có thể làm câu sai nghe thuyết phục hơn.

**Cách phân biệt:** bạn tự viết được câu trả lời đúng mà không cần tra cứu không? 
 Phải tra ⇒ vấn đề kiến thức ⇒ cần context/tool, không phải few-shot.

[Slide 13](#s12) · đối chiếu ranh giới *context vs hành vi* ở [Ngày 1, slide 37](day-1-ai-llm-foundation.html).

*Vì sao nghe hợp lý:* có tham số `max_tokens` nên trông như bạn đang "cấp" chỗ 
 cho output.

Output buffer là **phần còn lại** của context window sau khi system, few-shot, history, 
 tool schemas và input đã lấy chỗ. `max_tokens` chỉ đặt *trần*, không tạo ra chỗ.

Nghĩa là ba rổ đầu phình ra *âm thầm* (thêm rule, tích luỹ lượt, thêm tool) và bóp output mà 
 không báo động gì. Triệu chứng: **câu trả lời cụt giữa chừng** — và JSON thì hỏng.

[Hình 1](#f1) · [mô-đun bốn rổ](#m-tok) — kéo số lượt lên 30 để thấy tràn.

*Vì sao nghe hợp lý:* nhanh hơn thường đi kèm rẻ hơn trong nhiều bối cảnh khác, và song song 
 nghe như tối ưu.

**Tiền không đổi.** Ba tool song song vẫn là ba lời gọi API. Bạn mua *tốc độ*, 
 không mua chi phí — cùng nguyên lý "tiền cộng theo tổng, thời gian cộng theo cái chậm nhất" ở [Ngày 25](track-3-day-25.html).

Và nó thêm hai chi phí mới: **bước merge phải xử lý lỗi từng phần** (một nhánh lỗi, 
 hai nhánh thành công thì sao?), và **trace khó đọc hơn** vì mất thông tin về thứ tự nhân 
 quả.

Điều kiện duy nhất để song song: *không có phụ thuộc dữ liệu*.

[Hình 3](#f3) · [Slide 32](#s32) — "nhanh hơn không có nghĩa là tốt hơn".

---

<!-- chiron-source-span: {"source_span_id":"91bf4c21-f2f3-5cf4-aeaf-f7e0cce0fffb","locator":{"kind":"html_section","section_id":"apply","order":13,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-day-4.html"},"checksum":"0eccb7241ee19a22134ed2294ab3f739c5967dc88836927ab24d00c631b3ce1d"} -->

## ◆ Áp dụng vào SmartCheck AI

Ngày 4 trả nợ đúng hai chỗ Ngày 3 để ngỏ — và cả hai đều làm được trong một buổi.

### Bước 1 — Viết lại hai tool schema cho tử tế

Bản mẫu để đối chiếu với bản tự làm ở [Bài 3](#ladder). Chú ý phần **error mode** — thứ mà cả slide 27 lẫn tool registry của [Ngày 3](slide-buoi-3.html) đều thiếu.

| Phần | lookup_booking |
| --- | --- |
| Name | lookup_booking — động từ + danh từ, một hành động nghiệp vụ rõ |
| Description | "Tra thông tin đặt phòng của khách: tên, loại phòng, ngày nhận/trả, trạng thái thanh toán. Dùng khi khách đang check-in và đã cung cấp mã đặt phòng hoặc họ tên đầy đủ. Không dùng để trả lời câu hỏi chung về dịch vụ khách sạn." |
| Parameters | booking_code (string, "Mã đặt phòng, ví dụ BK2026031") · full_name (string, "Họ tên đầy đủ như trên giấy tờ") |
| Required | Không bắt buộc cả hai — một trong hai là đủ. Nếu thiếu cả hai, model phải hỏi lại chứ không đoán. |
| Error mode (phần slide thiếu) | "Trả {error:'not_found'} nếu không khớp — hãy đề nghị khách kiểm tra lại mã, đừng gọi lại với cùng tham số. Trả {error:'ambiguous'} nếu nhiều đặt phòng trùng tên — hãy hỏi thêm mã đặt phòng." |

**① Câu "Không dùng để…"** — phủ định tường minh. Nó vừa cải thiện độ chính xác chọn 
 tool, vừa là guardrail, và nối thẳng với ô *Boundary* ở [Ngày 2](slide-buoi-2.html).

**② Required để trống có chủ ý.** Vì có hai cách nhận diện, không nên bắt buộc cái nào. 
 Nhưng phải nói rõ trong description rằng cần *ít nhất một*, để model biết hỏi lại thay vì đoán 
 một mã — đúng pattern HITL *"làm rõ ý định"*.

**③ Error mode nói cả "phải làm gì".** Không chỉ *"trả về gì khi lỗi"* mà *"đừng gọi lại với cùng tham số"* — câu này chặn trực tiếp dấu 
 hiệu kẹt vòng lặp số một ở [Ngày 3, slide 30](slide-buoi-3.html).

### Bước 2 — Rà system prompt theo bốn anti-pattern

| Anti-pattern | Kiểm gì trong prompt kiosk | Nếu có thì sửa |
| --- | --- | --- |
| Quá dài | Đếm token. Có danh sách dịch vụ, bảng giờ, chính sách nằm trong prompt không? | Chuyển sang tool tra cứu ( archive ) — chỉ trả tiền khi dùng |
| Mâu thuẫn | Có vừa bảo "trả lời ngắn gọn" vừa bảo "giải thích rõ ràng, đầy đủ" không? | Nêu điều kiện: "tối đa 2–3 câu; chỉ dài hơn khi khách hỏi lại" |
| Mơ hồ | Có từ nào như "thân thiện", "chuyên nghiệp" mà không định nghĩa? | Thay bằng hành vi đo được: "xưng 'quý khách', không dùng emoji, không dùng từ lóng" |
| Không test edge case | Bộ test có ca ngoài phạm vi, ca thiếu thông tin, ca tool lỗi không? | Thêm ba ca đó — chúng là ba chế độ hỏng phổ biến nhất của kiosk |

"Luôn hữu ích và cố gắng trả lời mọi câu hỏi của khách"

"Chỉ trả lời trong phạm vi dịch vụ khách sạn"

Sửa bằng cách nêu thứ tự ưu tiên:

"Chỉ trả lời trong phạm vi dịch vụ 
 khách sạn. Với câu ngoài phạm vi, từ chối ngắn gọn và chỉ đường tới lễ tân — đây là hành vi đúng, 
 không phải thất bại."

là

### Bước 3 — Ba việc làm được trong một buổi

| # | Việc | Công sức | Đổi lại |
| --- | --- | --- | --- |
| 1 | Viết lại description cho mọi tool theo mẫu "dùng khi / không dùng để / error mode" | ~1 giờ | Rẻ nhất và tác động lớn nhất — với model, description là tool. Sửa nó không cần đụng code |
| 2 | Đếm token bốn rổ ở một lượt gọi thật, xem output buffer còn bao nhiêu ở lượt 15 | ~30 phút | Trả lời được câu "vì sao thỉnh thoảng câu trả lời bị cụt" trước khi nó thành sự cố |
| 3 | Viết unit test cho từng tool, kể cả ca lỗi | ~30 phút | Loại được một trong ba nhóm lỗi ngay lập tức mỗi khi debug — tiết kiệm nhiều hơn thời gian bỏ ra |

hai trong ba nhóm lỗi

---

<!-- chiron-source-span: {"source_span_id":"02696338-5c76-5266-a28b-1f6d5c0c3555","locator":{"kind":"html_section","section_id":"numbers","order":14,"heading":"! Con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"slide-day-4.html"},"checksum":"f540ecc77ddbadbcbb054be590bed4f68e85db7b8e1488cb88be9cd6c23637c5"} -->

## ! Con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài này gần như không có số liệu nghiên cứu — nó dạy khung và cú pháp. Con số duy nhất 
 đáng chú ý là một ngưỡng kinh nghiệm.

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| "Few-shot: 2–5 ví dụ " | 12 | Quy ước kinh nghiệm, không có nguồn | Điểm khởi đầu hợp lý. Tự đo: thêm ví dụ tới khi bộ test không cải thiện nữa thì dừng |
| "System prompt 2000+ tokens là anti-pattern" | 19 | Ngưỡng cảnh báo, không có nguồn | Dùng làm cờ để đi kiểm, không phải giới hạn cứng. Prompt 2.500 token mà mọi đoạn đều gánh việc thì vẫn ổn; prompt 800 token toàn chỉ dẫn mơ hồ thì vẫn tệ |
| Ví dụ prompt tốt: "dưới 120 từ" | 7 | Ví dụ minh hoạ | Điều đáng học là có ràng buộc độ dài cụ thể, không phải con số 120 |
| Tool schema mẫu get_weather | 27 | Đúng cú pháp, nhưng thiếu error mode | Dùng làm khung. Thêm phần "trả về gì khi lỗi và model nên làm gì" — chính bài tập slide 40 đòi điều này |
| Ví dụ granularity: get_customer_name / handle_all_customer_operations | 30 | Hai đầu cực đoan có chủ ý | Tiêu chí thực dụng: một tool = một câu bạn nói với đồng nghiệp |
| Mọi hệ số trong mô-đun bốn rổ (250 token/lượt · 150/tool · 120/ví dụ) | — | Giả định minh hoạ của tài liệu này | Slide 23 chỉ liệt kê bốn rổ và rủi ro, không đưa con số nào. Thay bằng số đo bằng tokenizer thật của bạn |
| "Tràn ở lượt thứ 24" · "output còn 1.600 với 16 tool" | — | Tính toán của tài liệu này | Đúng theo mô hình đã nêu. Nhưng mô hình không tính observation từ tool — trong agent thật, history phình nhanh hơn nhiều |
| Ước lượng "cắt 1.200 token × 1.500 lượt/ngày ≈ 54 triệu token/tháng" | — | Phép nhân của tài liệu này | Số học đúng, nhưng lưu lượng 1.500 lượt/ngày là giả định về SmartCheck AI chưa đo |

Đây là con số duy nhất trong bài dễ bị dùng máy móc. Nó **không** nói prompt dưới 2.000 
 token là tốt và trên 2.000 là xấu.

Ý của slide nằm ở vế sau của câu: *"nhồi mọi thứ vào 1 prompt 2000+ tokens **rồi hy vọng model luôn làm đúng** "* — vấn đề là *nhồi và hy vọng*, không phải 
 con số.

**Cách dùng đúng:** khi prompt vượt ngưỡng đó, coi là tín hiệu 
 đi kiểm — chạy quy trình "xoá từng đoạn, chạy lại bộ test" ở [Bài 2](#ladder). Nếu mọi đoạn 
 đều gánh việc, prompt dài là hợp lý.

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực 
 tế đã chạy."

tokenizer thật của model bạn dùng

Ngày 1, slide 30

---

<!-- chiron-source-span: {"source_span_id":"52408057-8322-50cb-8053-37b0b7f6ff36","locator":{"kind":"html_section","section_id":"cheat","order":15,"heading":"✓ Cheat sheet ôn thi","source_file":"slide-day-4.html"},"checksum":"963a3d2b27d549fde0519b154acaffdea38eb11b05ea6ab8c0a367d791c3d720"} -->

## ✓ Cheat sheet ôn thi

Nén 43 slide xuống một trang.

### Prompt — bốn thành phần và ba loại

**4 thành phần:** Role · Task · Context · Format. *Bắt đầu với **Task + Format**; chỉ thêm Role/Context khi chúng thật sự cải thiện.* Nguyên tắc vàng: **Specificity beats cleverness**.

**3 loại prompt — phân biệt theo vòng đời:** *Instruction* (một lượt) · *Conversation* (một phiên, trả tiền mỗi lượt vì lịch sử gửi lại) · *System* ( **vĩnh viễn, gửi ở MỌI lượt gọi** — chỗ đáng tối ưu nhất).

**Thứ tự thử kỹ thuật:** zero-shot → few-shot → CoT. *Few-shot tốn ở INPUT (rẻ); CoT tốn ở OUTPUT (đắt gấp 3–5 lần).* Few-shot chỉ chữa *format/nhất quán*, không chữa *thiếu kiến thức*.

### System prompt — năm khối và bốn anti-pattern

**5 khối:** Persona · Rules · Capabilities · **Constraints** · 
 Output format. *Hai nhóm: "định hình" (Persona, Rules — hỏng thì chất lượng kém) và "ràng buộc" 
 (Capabilities, Constraints, Format — hỏng thì sự cố thật).*

**4 anti-pattern:** quá dài (2000+ token) · **mâu thuẫn** (khó debug nhất — 
 không tái hiện được) · mơ hồ ("hãy chuyên nghiệp") · không test edge case.

**Câu kiểm mỗi chỉ dẫn:** *"tôi kiểm được điều này không?"* Không kiểm được ⇒ mơ hồ ⇒ thay tính từ bằng hành vi đo được. **System prompt là policy layer** — chỗ đặt *luật*, không phải chỗ đặt *dữ liệu*.

### Bốn rổ token và rủi ro riêng của từng rổ

| Rổ | Rủi ro khi quá lớn |
| --- | --- |
| System prompt | Chậm hơn, khó maintain — và trả tiền ở mọi lượt |
| History | Dễ nhiễu, dễ mất thông tin ở giữa |
| Tool schemas | Model CHỌN SAI TOOL — rủi ro chất lượng, không phải dung lượng |
| Output buffer | Bị cắt cụt — và nó là phần CÒN LẠI, không phải phần được cấp |

**Ba cách nén:** *Summarize* (mất chi tiết) · *Drop* (mất hết) · ***Archive*** (không mất — đẩy ra ngoài, fetch khi cần 
 = RAG).

### Tool calling — luồng, schema, nguyên tắc

**Luồng:** LLM *đề nghị* (JSON) → **ứng dụng của BẠN chạy tool** → 
 kết quả về → LLM trả lời. *Model không tự chạy code — đó là chỗ bạn đặt guardrail, timeout, log.*

**Schema 4 phần (+1 nên có):** Name (động từ đúng việc) · **Description** (nói *khi nào dùng*, không phải làm gì) · Parameters (JSON Schema) · 
 Required (để model biết *hỏi lại* thay vì đoán) · *Error mode* (slide thiếu — nên thêm).

**4 nguyên tắc thiết kế:** Single Responsibility · **Idempotency** (điều kiện để retry an toàn) · Granularity hợp lý · Test độc lập (loại được một nhóm lỗi khi debug).

**3 pattern:** conditional (khi nào gọi) · chaining (thứ tự) · 
 parallel + merge (cùng lúc). *Song song chỉ khi không có phụ thuộc dữ liệu — và tiền KHÔNG giảm, chỉ thời gian giảm.* **3 nhóm lỗi khi debug:** prompt · tool schema · control flow.

---

<!-- chiron-source-span: {"source_span_id":"4bb78a54-8ef6-5497-bfc9-7babb7dfd2af","locator":{"kind":"html_section","section_id":"gloss","order":16,"heading":"A–Z Từ điển thuật ngữ","source_file":"slide-day-4.html"},"checksum":"6255f357e0a50be5b1ae33e565d6c36ecc91c392a762ee09b7e557c6c35392ed"} -->

## A–Z Từ điển thuật ngữ

Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện.

---

<!-- chiron-source-span: {"source_span_id":"49de2902-a134-5b8b-9cc9-cc59f4e3980f","locator":{"kind":"html_section","section_id":"bloom","order":17,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-day-4.html"},"checksum":"3c60f838a1e70f574ce4a0026fe5dd781c0686831aa0653742009c56f633f9b7"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab 4 kiểm tra mức 3–4; câu hỏi slide 42 kiểm 
 tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 4 thành phần prompt, 5 khối system prompt, 4 phần tool schema, 4 nguyên tắc thiết kế tool, 
 và 4 rổ token. | Hình 1 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao model không tự chạy tool, và vì sao điều đó là tin tốt 
 về an toàn. | Hình 2 · ô kiểm tra chương 4–7 |
| 3 · Áp dụng | Viết được tool schema đầy đủ (kể cả error mode) và system prompt có đủ năm khối cho một bài toán 
 mới. | mục áp dụng · Bài 1 → 3 |
| 4 · Phân tích | Cho một lỗi bất kỳ, khoanh vùng được nó thuộc nhóm prompt, tool schema, hay 
 control flow — và nói được vì sao. | Slide 35–38 — bảng ba nhóm lỗi · Bài 1 |
| 5 · Đánh giá | Nhìn một prompt hoặc tool schema của người khác và chỉ ra chỗ sẽ hỏng trước khi nó hỏng. | Slide 19 — bốn anti-pattern · 6 hiểu lầm |

không phải

"Tool có unit test xanh không? Thought trong trace có đi đúng mục tiêu 
 không? Thứ tự các bước có hợp lý không?"
