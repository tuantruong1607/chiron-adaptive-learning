---
schema_version: 1
course_id: rag-intensive
document_id: "6a3afe4e-3720-55d5-8888-6487c388efe3"
document_version_id: "560e4356-16f3-5418-b7a6-a7b700271b20"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Prompt Engineering & T ool Calling"
source_file: "slide day 4.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\slide day 4.pdf"
source_sha256: "5ba9e3a2df83be5fc6c027fc47da9ef9c657f6cdc06db479353c4df5531b3bda"
parser_version: chiron-structured-markdown-v1
page_count: 43
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":43}"
language: vi
---

# Prompt Engineering & T ool Calling

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"7eb635c9-9e95-5286-9914-2ee19fe1a3a8","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Prompt Engineering & T ool Calling","extraction_method":"pdf-text-layer"},"checksum":"5ee297c9c8e735ce87f7e1e29b9be0d52c7779d8421733f6efef1715ec38a188"} -->

## Slide 1 - Prompt Engineering & T ool Calling

AICB-P1 · Ngày 4 · Làm sao nói để AI hiểu đúng ý? T ên Giảng Viên VinUniversity · Phase 1 · T uần 1 · 2026

---

<!-- chiron-source-span: {"source_span_id":"4ddfc939-0455-5f58-a635-256147424f87","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"4bd0e3976f1389bfaef5c422017561ff4e5e7f0c715fce68294089e0d93be6cf"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Hai người hỏi AI cùng một việc, một người nhận kết quả xuất sắc, người kia nhận rác. Tại sao?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"662acde2-0cf5-5369-84ed-ff966c170477","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"1c64d250e87d34d8fce4f3ac96048ba279157e9d73ae60830f6cd839d9d2b5d9"} -->

## Slide 3 - Nội Dung Bài Học

1. Prompt fundamentals

2. Advanced prompting techniques

3. System prompt engineering

4. Context engineering

5. Tool calling

6. Design principles cho tools

7. Parallel tool calls & patterns

8. Lab 4 + deliverable cuối buổi Giảng viên (VinUni) AICB · Ngày 4 T uần 1 1 / 30

---

<!-- chiron-source-span: {"source_span_id":"e559b1d7-661f-5c4e-bff1-2f2f419f5dc7","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu Ngày 4","extraction_method":"pdf-text-layer"},"checksum":"f54cf9bf4465e03e214521413e3087d9e9d401a353911ae3bcbf6fa49ed79174"} -->

## Slide 4 - Mục Tiêu Ngày 4

- Viết được prompt rõ ràng theo các thành phần Role / T ask / Context / Format

- Hiểu khi nào nên dùng zero-shot, few-shot, CoT, và khi nào không cần

- Viết được system prompt production-grade cho agent

- Khai báo được tool schema và hiểu vòng lặp tool calling từ model đến tool rồi quay
lại model Mục tiêu của buổi này là hiểu cơ chế: prompt là interface giữa human intent và model behavior; tool calling là interface giữa model và thế giới bên ngoài. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 2 / 30

---

<!-- chiron-source-span: {"source_span_id":"c377c69a-a3f2-5da0-baa3-e7a9321d3c66","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"4167742f8b2a372b1bd5898f03f6903ec4c526fbc6f1580be55f4c3f39234649"} -->

## Slide 5 - Deliverable Cuối Ngày

1 agent script chạy được + 1 system prompt + 2 tool schemas + 5 test questions + ghi chú lỗi prompt/tool/control flow

- 2 tools tự viết: 1 API wrapper đơn giản, 1 data query đơn giản

- 1 system prompt có rules, constraints, output contract

- 5 câu test để chứng minh agent biết khi nào trả lời trực tiếp, khi nào gọi tool
Giảng viên (VinUni) AICB · Ngày 4 T uần 1 3 / 30

---

<!-- chiron-source-span: {"source_span_id":"222d96bd-1e58-5b9c-8b50-2697b795492f","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Prompt Engineering Funda","extraction_method":"pdf-text-layer"},"checksum":"32b80815ef096994828e84cc625198930a481868cc0fdf1a7c90dbbe733c1dd5"} -->

## Slide 6 - Prompt Engineering Funda

01 Prompt Engineering Funda- mentals Prompt tốt không phải prompt “hay”, mà là prompt tạo ra hành vi mong muốn ổn định

---

<!-- chiron-source-span: {"source_span_id":"ff339ff1-cb33-53a4-8f0a-bdd94fd3ff00","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Prompt = Interface Giữa Ý Định và Khả Năng Model","extraction_method":"pdf-text-layer"},"checksum":"0cf67078ada6deb5c002d1c657f076bd92a1085766d4e9c9aace2a488278b652"} -->

## Slide 7 - Prompt = Interface Giữa Ý Định và Khả Năng Model

Prompt kém “Viết email cho tôi” Không rõ gửi ai, về gì, tone nào, dài bao nhiêu. Kết quả: chung chung, khó dùng ngay. Prompt tốt Viết email xin lỗi khách hàng về giao hàng trễ 2 ngày, tone lịch sự, dưới 120 từ, có CTA rõ ràng. Rõ task, context, constraint, format. Kết quả: actionable hơn hẳn. Lưu ý: Nguyên tắc vàng: Specificity beats cleverness. Prompt ngắn nhưng rõ nghĩa thường tốt hơn prompt dài mà lan man. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 4 / 30

---

<!-- chiron-source-span: {"source_span_id":"7018c761-2fa9-513f-999a-922d70e0d83e","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"4 Thành Phần Của Prompt T ốt","extraction_method":"pdf-text-layer"},"checksum":"f04220c277e9427d8bf69181698e208077c26f4248fe124edf11e97f8d1d327a"} -->

## Slide 8 - 4 Thành Phần Của Prompt T ốt

ROLE Vai trò T ASK Nhiệm vụ CONTEXT Bối cảnh FORMA T Định dạng “Act as a senior support analyst” “Summarize the ticket and propose next step” “For an internal operations dashboard” “Output as JSON with 3 fields” Bắt đầu với T ask + Format. Chỉ thêm Role hoặc Context khi chúng thực sự cải thiện chất lượng hoặc tính nhất quán. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 5 / 30

---

<!-- chiron-source-span: {"source_span_id":"716dd007-5339-5040-a7ad-00564e0597ce","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Instruction vs Conversation vs System Prompt","extraction_method":"pdf-text-layer"},"checksum":"fb91f48d0873e0a9db02aa5e48e4227d6c95cb813004b67b89e6255f1ff8ce26"} -->

## Slide 9 - Instruction vs Conversation vs System Prompt

Loại prompt Mục đích chính Khi dùng Instruction prompt Ra lệnh trực tiếp cho một tác vụ Hỏi đáp 1 lượt, transform, summarize, classify Conversation prompt Giữ ngữ cảnh nhiều lượt với user Chatbot, support, tutor, de- bugging nhiều bước System prompt Đặt policy, boundary, output contract Agent, assistant production, use case cần hành vi ổn định Anthropic prompting guidance + teaching heuristics Giảng viên (VinUni) AICB · Ngày 4 T uần 1 6 / 30

---

<!-- chiron-source-span: {"source_span_id":"990a5d11-ed68-5bce-b4bf-aa606c244cb4","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"T oken Budget Awareness","extraction_method":"pdf-text-layer"},"checksum":"f9c48248f4a80b1872f6511eee7e294cc3e8513d62888a849498991dbe73a843"} -->

## Slide 10 - T oken Budget Awareness

- Prompt dài hơn không đồng nghĩa prompt tốt hơn.

- Mỗi token thừa làm tăng chi phí, latency, và đôi khi cả nhiễu.

- Hãy ưu tiên: instruction rõ, examples đúng chỗ, output contract rõ.

- Rule thực dụng: nếu prompt dài thêm nhưng không làm thay đổi hành vi mong
muốn, hãy cắt bớt. Lưu ý: Prompt engineering tốt là tối ưu độ rõ và khả năng kiểm soát, không phải thi xem ai viết prompt dài hơn. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 7 / 30

---

<!-- chiron-source-span: {"source_span_id":"21e54abf-7a49-5ede-bbf1-a0a6c19474b6","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Advanced Prompting T ech","extraction_method":"pdf-text-layer"},"checksum":"15392847969d316cce04934f607851186a8edb25c2a8e749ef8dca5efd2cc29d"} -->

## Slide 11 - Advanced Prompting T ech

02 Advanced Prompting T ech- niques Dùng kỹ thuật nâng cao khi chúng cải thiện chất lượng thật sự, không dùng như thần chú

---

<!-- chiron-source-span: {"source_span_id":"4a535d49-8407-55ee-aa95-2e8c76129a99","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Zero-shot, One-shot, Few-shot, CoT","extraction_method":"pdf-text-layer"},"checksum":"022d1893b0f927d7f16f0877e2e242de8f6d89a943172f4d91f7b902649e40e1"} -->

## Slide 12 - Zero-shot, One-shot, Few-shot, CoT

Zero-shot Không có ví dụ mẫu. Nhanh, rẻ, nên thử trước. One-shot 1 ví dụ mẫu. Tốt khi cần giữ format rõ hơn. Few-shot 2–5 ví dụ. Tăng consistency, nhưng tốn token hơn. CoT Cho model reasoning từng bước. Hữu ích cho task suy luận. Thứ tự thử thực dụng: zero-shot -> few-shot -> decomposition / CoT. Đừng nhảy vào prompt phức tạp ngay từ đầu. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 8 / 30

---

<!-- chiron-source-span: {"source_span_id":"e1be08b2-3da5-5d21-a778-aeae72fc32d0","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Khi Nào Dùng Few-shot?","extraction_method":"pdf-text-layer"},"checksum":"60563c3dfd1bc5ef813f6d240c1b48593182a864fbd18ad76325bfd6e25227dc"} -->

## Slide 13 - Khi Nào Dùng Few-shot?

- Khi model hiểu task nhưng ra sai
format hoặc không ổn định giữa các input tương tự.

- Khi cần giữ tiêu chuẩn đánh giá, tone,
hoặc cách lập luận nhất quán.

- Ví dụ mẫu nên relevant, đa dạng vừa
đủ, và đúng format mong muốn. Few-shot không phải để “dạy lại” model mọi thứ; nó là cách chỉ ra pattern mà bạn muốn model bám theo. Nguồn minh họa: zero/few-shot teaching graphic trong repo Giảng viên (VinUni) AICB · Ngày 4 T uần 1 9 / 30

---

<!-- chiron-source-span: {"source_span_id":"95316c0c-a16b-5d3e-bb00-d9e23bd7952c","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Few-shot Prompting — Python Example","extraction_method":"pdf-text-layer"},"checksum":"ae4cb4a1d511cac4e40f3c3e5b1b93d6185d0e642f9aa43394df284f51681215"} -->

## Slide 14 - Few-shot Prompting — Python Example

examples = """ Input: "Great product, fast delivery! " Output: Positive Input: "Terrible quality, waste of money " Output: Negative """ prompt = f """Classify feedback as Positive, Negative, or Neutral. {examples} Input: "Love the design but shipping was slow " Output:""" print(prompt) Giảng viên (VinUni) AICB · Ngày 4 T uần 1 10 / 30

---

<!-- chiron-source-span: {"source_span_id":"e51e4699-203d-55e0-8b67-b80951aa1017","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Chain-of-Thought (CoT) và Tree-of-Thought","extraction_method":"pdf-text-layer"},"checksum":"0ec0dc11800953ba6e0356c247fe27052a9d6c2f3e70af1b0464cba9bdefc885"} -->

## Slide 15 - Chain-of-Thought (CoT) và Tree-of-Thought

### CoT phù hợp khi

- Bài toán cần reasoning nhiều bước

- Bạn muốn model giải thích logic
trung gian

- Bạn cần debug xem model sai ở
bước nào

### Tree-of-Thought

- Hữu ích cho bài toán cần explore
nhiều hướng

- Phức tạp hơn, tốn token và latency
hơn

- Chỉ nên giới thiệu như extension,
không phải mặc định cho mọi task CoT là công cụ cải thiện reasoning, không phải phép màu. Nếu task vốn dĩ chỉ là formatting hoặc extraction đơn giản, CoT thường là overkill. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 11 / 30

---

<!-- chiron-source-span: {"source_span_id":"179b1cd4-167a-56a6-99ab-dcd78d5f90f0","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"System Prompt Engineering","extraction_method":"pdf-text-layer"},"checksum":"6cef27e107c12dc2a72a7ecd1c866405621e795a5489e1dde9e6770f60a9f52f"} -->

## Slide 16 - System Prompt Engineering

03 System prompt tốt làm agent nhất quán hơn, dễ kiểm soát hơn, và dễ test hơn

---

<!-- chiron-source-span: {"source_span_id":"80ff9133-6b33-51ad-a5d7-0b1fa379725d","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Anatomy của System Prompt Production-grade","extraction_method":"pdf-text-layer"},"checksum":"96fe487df324c286a0800748700f813a8720fffbffc8f77e796d02cfebd0425b"} -->

## Slide 17 - Anatomy của System Prompt Production-grade

Persona: role, expertise level, communication style Rules: việc nên làm, việc luôn phải làm Capabilities: model được phép dùng tools nào, dữ liệu nào Constraints: không làm gì, khi nào từ chối, khi nào escalate Output format: JSON, markdown, bullet list, schema, language priority Giảng viên (VinUni) AICB · Ngày 4 T uần 1 12 / 30

---

<!-- chiron-source-span: {"source_span_id":"ebd3957c-4eb4-553c-86b2-513f0af7b731","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"System Prompt — Python Example","extraction_method":"pdf-text-layer"},"checksum":"5d407640eb1b3557706203a17f6edf155885846397962b64d2893a26e822db30"} -->

## Slide 18 - System Prompt — Python Example

system_prompt = """ You are a support triage agent for an e-commerce team.

### Rules
- Answer in Vietnamese.
- Be concise and operational.
- If billing or refund policy is unclear, ask for more details.

### Constraints
- Never invent order status.
- Never promise refunds without tool confirmation.

### Output format
Return JSON with: intent, action, reply """ Giảng viên (VinUni) AICB · Ngày 4 T uần 1 13 / 30

---

<!-- chiron-source-span: {"source_span_id":"fc285d38-42a1-55ae-90be-890fa0fc7319","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"System Prompt Anti-Patterns","extraction_method":"pdf-text-layer"},"checksum":"0cdc8181a06e8214a115282deba96bbdb9ccf5376df915f283fe4768c2a7f53f"} -->

## Slide 19 - System Prompt Anti-Patterns

- Quá dài: nhồi mọi thứ vào 1 prompt 2000+ tokens rồi hy vọng model luôn
làm đúng

- Mâu thuẫn: vừa bảo “ngắn gọn”, vừa bắt “giải thích chi tiết từng bước”

- Mơ hồ: “hãy thông minh”, “hãy chuyên nghiệp”, nhưng không định nghĩa
chuẩn output

- Không test edge cases: quên kiểm tra câu hỏi ngoài phạm vi, refusal, tool
failure

- ✓ Nguyên tắc: system prompt là policy layer. Càng rõ boundary, càng dễ
predict hành vi Giảng viên (VinUni) AICB · Ngày 4 T uần 1 14 / 30

---

<!-- chiron-source-span: {"source_span_id":"734a80ee-a8a0-5fee-8a9e-cc15cccdc6de","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Context Engineering","extraction_method":"pdf-text-layer"},"checksum":"e05b93e46c6b3070853aacff71a71e65adacfce5c1c2463254a985b37ae29f39"} -->

## Slide 20 - Context Engineering

04 Điều quan trọng không phải nhét bao nhiêu context, mà là chọn đúng context cần thiết

---

<!-- chiron-source-span: {"source_span_id":"0ee9e7c5-78cd-5b6c-92ed-43e70db7ef96","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Context Window Management","extraction_method":"pdf-text-layer"},"checksum":"e4b2dba39646aa1992562f6774328e900d3cbcec639648c3b9cfd6e1be08c7f2"} -->

## Slide 21 - Context Window Management

System History Current input T ools Output policy recent / relevant current task schemas buffer Lưu ý: Token budget allocation cần chủ động: đừng để history, tools, và ex- amples ăn hết chỗ dành cho output. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 15 / 30

---

<!-- chiron-source-span: {"source_span_id":"4afd9e73-34bb-5ce6-85cd-065ab4c9cdf3","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Memory Injection và Context Compression","extraction_method":"pdf-text-layer"},"checksum":"b1c610449b4770f2a24e8b35e9bf2bf78c378c5f9293946a8cca1edb4387f7c2"} -->

## Slide 22 - Memory Injection và Context Compression

Memory injection

- Chỉ đưa vào facts thật sự cần cho
task hiện tại

- Ưu tiên recent history hoặc
relevant history, không dump toàn bộ transcript

- Tốt cho support agent, coding
assistant, tutor nhiều lượt Compression

- Summarize: tóm tắt phần cũ

- Drop: bỏ hẳn phần không còn liên
quan

- Archive: đẩy ra ngoài context, chỉ
fetch lại khi cần Context engineering là bài toán chọn lọc và ưu tiên. Nếu mọi thứ đều quan trọng, thực ra không có gì thực sự nổi bật với model. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 16 / 30

---

<!-- chiron-source-span: {"source_span_id":"b6f5c3e9-beae-531e-9981-b085d88bf262","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"T oken Budget Allocation: Nên Nghĩ Theo Rổ Nào?","extraction_method":"pdf-text-layer"},"checksum":"e9d7df6df599352754f4d3e6ba9b35835af65e8f158c1e955e219bb6aa6baf29"} -->

## Slide 23 - T oken Budget Allocation: Nên Nghĩ Theo Rổ Nào?

Rổ token Chứa gì Rủi ro nếu quá nhiều System prompt policy, rules, output format chậm hơn, khó maintain History recent turns, facts liên quan dễ nhiễu, dễ lost in the mid- dle Tool schemas tên tool, mô tả, tham số model chọn tool tệ nếu schema dài hoặc mơ hồ Output buffer phần model dùng để trả lời bị cắt cụt output nếu cấp thiếu Teaching heuristic for token budgeting Giảng viên (VinUni) AICB · Ngày 4 T uần 1 17 / 30

---

<!-- chiron-source-span: {"source_span_id":"d2a79968-c675-54b5-821c-3e3a8edcf3f8","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"T ool Calling","extraction_method":"pdf-text-layer"},"checksum":"79608f6752b83c1faa2d2c6ba416cbb16631a813152df170d950dd31e6add50a"} -->

## Slide 24 - T ool Calling

05 Tool calling là cách agent chuyển từ “nói” sang “tương tác với thế giới thực”

---

<!-- chiron-source-span: {"source_span_id":"fdc11719-c2d3-59a4-9474-2db780e9dd3c","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"T ool Calling Flow","extraction_method":"pdf-text-layer"},"checksum":"9e760cfc35c0a677e2b238de0d982b6ef964835718e3990858ac262d5b419296"} -->

## Slide 25 - T ool Calling Flow

LLM decides tool_call JSON App executes tool tool result LLM final response Model không tự chạy code hay tự gọi API ngoài. Ứng dụng của bạn nhận tool request, chạy tool, rồi gửi kết quả trở lại model. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 18 / 30

---

<!-- chiron-source-span: {"source_span_id":"eaef4fd2-0c57-5924-8042-4ac8863791b7","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"T ool Schema Anatomy","extraction_method":"pdf-text-layer"},"checksum":"c5304b60d0424b64a397b95f54f50bfd44b615d189dbe6a31b3639c87b40318d"} -->

## Slide 26 - T ool Schema Anatomy

- Name: nên ngắn, rõ, động từ đúng
việc

- Description: nói khi nào nên dùng
tool này

- Parameters: mô tả input bằng
JSON Schema

- Required fields: giúp model biết
thiếu gì thì chưa gọi được Lưu ý: LLM đọc description như tài liệu hướng dẫn. Nếu description mơ hồ, model sẽ chọn sai tool hoặc truyền sai arguments. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 19 / 30

---

<!-- chiron-source-span: {"source_span_id":"246d3044-26ff-54bc-a70a-4903290f69d1","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"T ool Schema — Python Example","extraction_method":"pdf-text-layer"},"checksum":"fd59f21d5c23af67a14c4cd0724bf595b948c18f73dfa9a80f7ff09b38c1ce63"} -->

## Slide 27 - T ool Schema — Python Example

```text
weather_tool = {
```
"type": "function",

```text
"function": {
```
"name": "get_weather", "description": "Get current weather for a city when the user asks about weather conditions.",

```text
"parameters": {
```
"type": "object",

```text
"properties": {
"city": { "type": "string", "description": "City name, e.g. Hanoi"}
},
```
"required": [ "city"] } } } Giảng viên (VinUni) AICB · Ngày 4 T uần 1 20 / 30

---

<!-- chiron-source-span: {"source_span_id":"43fbb5a0-df03-599e-a8f6-b9901b6fb5e0","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Design Principles Cho T ools","extraction_method":"pdf-text-layer"},"checksum":"08b0e8e7e409fca80f43800770ef561591b7b76c4b441f4fc09103cc33f1f1e2"} -->

## Slide 28 - Design Principles Cho T ools

06 Tool tốt là software interface tốt, không phải prompt trang trí

---

<!-- chiron-source-span: {"source_span_id":"e5dae4b0-45ff-57ba-9526-34a62cdadf85","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"4 Nguyên T ắc Thiết Kế T ool","extraction_method":"pdf-text-layer"},"checksum":"95c82c874012a2dc73a110221890b01cb78a30bde24d9b4586e25e02cc252efd"} -->

## Slide 29 - 4 Nguyên T ắc Thiết Kế T ool

Nguyên tắc Ý nghĩa Nếu vi phạm Single Responsi- bility Mỗi tool làm 1 việc rõ ràng model khó quyết định nên gọi tool nào Idempotency Cùng input cho cùng kết quả; side effect được kiểm soát retry dễ sinh lỗi phụ Granularity hợp lý Không quá nhỏ, cũng không ôm quá nhiều việc hoặc overhead lớn, hoặc tool quá cứng Test độc lập Unit test từng tool trước khi gắn vào agent khó tách lỗi tool khỏi lỗi prompt Principles for reliable tool interfaces Giảng viên (VinUni) AICB · Ngày 4 T uần 1 21 / 30

---

<!-- chiron-source-span: {"source_span_id":"2ff38833-da95-50ff-bcb7-0cd159e13ffa","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"T ool Granularity: Quá Nhỏ Hay Quá T o Đều Có Giá","extraction_method":"pdf-text-layer"},"checksum":"39745c8590a6463ef478f452026057e3d9ec9298d38dc17d55edbbb977b24f48"} -->

## Slide 30 - T ool Granularity: Quá Nhỏ Hay Quá T o Đều Có Giá

Quá nhỏ

- get_customer_name

- get_customer_email

- get_customer_phone
Hệ quả: quá nhiều calls, overhead lớn, flow rối. Quá to

- handle_all_customer_operations
Hệ quả: model không hiểu boundary, khó debug, khó reuse. Thiết kế tool quanh một hành động nghiệp vụ rõ ràng: ví dụ lookup_order, get_weather, query_sales_data, send_email_draft. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 22 / 30

---

<!-- chiron-source-span: {"source_span_id":"1be90849-4d0b-575c-ad9a-445d3b03846c","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Parallel T ool Calling & Pat","extraction_method":"pdf-text-layer"},"checksum":"fe07bf58b42d534dc7aa6410ede967a2aa7ac1553f7862935a9a8d7c2ebb483b"} -->

## Slide 31 - Parallel T ool Calling & Pat

07 Parallel T ool Calling & Pat- terns Nhanh hơn không có nghĩa là tốt hơn nếu flow control và merge logic không rõ

---

<!-- chiron-source-span: {"source_span_id":"b9dfd20f-4026-5589-b012-6a277580493d","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Sequential vs Parallel T ool Calls","extraction_method":"pdf-text-layer"},"checksum":"e122919b73066779c5c6d6c77cde2ca184a925fbcda44a5ea43b2284a0a8cc74"} -->

## Slide 32 - Sequential vs Parallel T ool Calls

Sequential Tool B cần output của Tool A. Ví dụ: tìm order ID -> rồi mới tra shipping sta- tus. Parallel Các tool độc lập có thể chạy cùng lúc. Ví dụ: gọi thời tiết, tỷ giá, và lịch họp song song. Lưu ý: Chỉ song song hóa khi không có phụ thuộc dữ liệu. Nếu vẫn cần bước merge / verify rõ ràng ở cuối. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 23 / 30

---

<!-- chiron-source-span: {"source_span_id":"3990cda7-503a-56f3-b1e0-dd005e18a7f9","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"3 T ool Use Patterns Thường Gặp","extraction_method":"pdf-text-layer"},"checksum":"57367332de040eb0a49091e00264889896cecaf1203a37c61cb821fe1373e52f"} -->

## Slide 33 - 3 T ool Use Patterns Thường Gặp

1. Conditional tool use: agent tự quyết định có cần tool hay trả lời trực tiếp.

2. T ool chaining:output của tool A là input của tool B.

3. Parallel fetch + merge: lấy nhiều nguồn độc lập rồi tổng hợp kết quả. Tool calling không chỉ là “gọi API”. Nó là bài toán control flow: khi nào gọi, gọi cái gì, gọi theo thứ tự nào, và làm gì khi tool fail. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 24 / 30

---

<!-- chiron-source-span: {"source_span_id":"626d9f61-d80e-54f8-8a79-2090e05716eb","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Minimal T ool Loop — Python Example","extraction_method":"pdf-text-layer"},"checksum":"31366b4629665e0e5e37b23f61f2a2796533a9db311072b8e34c2bf099326327"} -->

## Slide 34 - Minimal T ool Loop — Python Example

messages = [{ "role": "user", "content": "ờThi ếtit Hà ộNi và ỷt giá USD hôm nay?"}] response = client.responses.create(model= "gpt-4.1", input=messages, tools=tools)

### for item in response.output

### if item.type == "function_call"
result = run_tool(item.name, json.loads(item.arguments)) messages.append(item) messages.append({"type": "function_call_output", "call_id": item.call_id, "output": result}) final = client.responses.create(model= "gpt-4.1", input=messages, tools=tools) print(final.output_text) Giảng viên (VinUni) AICB · Ngày 4 T uần 1 25 / 30

---

<!-- chiron-source-span: {"source_span_id":"50533d3b-9cc2-5e8e-829b-69429daf951c","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Thực Hành","extraction_method":"pdf-text-layer"},"checksum":"e5b340b060434e03004049f73035b2ecc9168109c2f8937feb8eacba6825bcad"} -->

## Slide 35 - Thực Hành

08 Lab 4: Build first agent với system prompt + 2 tools + 5 test cases

---

<!-- chiron-source-span: {"source_span_id":"3404fb9a-814e-55e9-996e-d09b1de5ee66","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Hands-on 4: Cách Chạy Lab","extraction_method":"pdf-text-layer"},"checksum":"6586543290b3c73f21ed695fccd242fc6688d994af915f60e66f5312092ceff7"} -->

## Slide 36 - Hands-on 4: Cách Chạy Lab

1. Viết 1 system prompt với rules, constraints, output format

2. Tạo 2 custom tools: 1 API wrapper đơn giản, 1 data query đơn giản

3. Nối tools vào agent loop

4. Chạy 5 câu test để xem khi nào agent trả lời trực tiếp, khi nào gọi tool

5. Ghi lại lỗi thuộc loại prompt, tool schema, hay control flow Giảng viên (VinUni) AICB · Ngày 4 T uần 1 26 / 30

---

<!-- chiron-source-span: {"source_span_id":"4038412e-cc14-5260-8f2a-78e8e3a032bc","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Lab Skeleton — Python Example","extraction_method":"pdf-text-layer"},"checksum":"fdb625ef9ea2aab63ed492bf1824e30c8a12f069e89f98edf837ef5d8170f05c"} -->

## Slide 37 - Lab Skeleton — Python Example

SYSTEM_PROMPT = open("system_prompt.txt").read() TOOLS = [get_weather_tool(), query_sales_tool()]

### while True
user_input = input("You: ") messages.append({"role": "user", "content": user_input}) response = call_model(messages, SYSTEM_PROMPT, TOOLS) messages = handle_tool_calls(response, messages) print(render_final_answer(messages, SYSTEM_PROMPT, TOOLS)) Giảng viên (VinUni) AICB · Ngày 4 T uần 1 27 / 30

---

<!-- chiron-source-span: {"source_span_id":"b7b67736-3179-59c2-b2fa-ad5b1d05ffa2","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Lab #4","extraction_method":"pdf-text-layer"},"checksum":"a33ea74e1676c0c627fa29eb2f71b0f153c9d9f37717534e9cd74a1770d63d6d"} -->

## Slide 38 - Lab #4

Mục tiêu: Build ReAct agent với 2 custom tools, viết system prompt chuẩn, và test end-to-end trên 5 câu hỏi Deliverable: Deliverable: Agent script chạy được + system prompt + 2 tool schemas + 5 test outputs + note lỗi prompt/tool/control flow Thời gian: 150 phút Giảng viên (VinUni) AICB · Ngày 4 T uần 1 28 / 30

---

<!-- chiron-source-span: {"source_span_id":"35513d4e-6eb4-5e16-86f0-4452adff1229","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"f38662b43fa50da87114ce464d2e175587ea0631ccee25b2f4b95da21b38bb01"} -->

## Slide 39 - T ổng kết — Key T akeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Prompt = interface giữa human intent và model capability. Prompt tốt giúp model làm đúng việc, đúng format, đúng boundary. 2 System prompt tốt = agent nhất quán và predictable hơn, đặc biệt khi có tools và constraints. 3 Tool schema description quyết định rất mạnh việc model biết khi nào dùng tool nào và gọi với arguments gì. 4 Parallel tool calls nhanh hơn đáng kể khi các tool độc lập; nếu có phụ thuộc dữ liệu, hãy giữ flow tuần tự. Giảng viên (VinUni) AICB · Ngày 4 T uần 1 28 / 30

---

<!-- chiron-source-span: {"source_span_id":"627103de-82bc-574e-aeb7-82f4baaab0b2","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"b2cdd452ba1628246956ce4f1261bded87f9f9639f52aac37927c51607d03128"} -->

## Slide 40 - Tiếp theo & Bài tập

AI Product Thinking & Require- ments “Bạn đã build được agent đầu tiên. Nhưng build xong chưa đủ. Ngày mai: sản phẩm này dành cho ai, yêu cầu ra sao, và rủi ro nào phải nghĩ từ đầu?”

- Hoàn thiện Lab 4 với 5 test
questions rõ pass/fail

- Đọc lại system prompt của
mình và chỉ ra 2 chỗ còn mơ hồ hoặc mâu thuẫn Giảng viên (VinUni) AICB · Ngày 4 T uần 1 29 / 30

---

<!-- chiron-source-span: {"source_span_id":"ed445068-d84e-5f5c-9db2-92b5b71e125d","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"T ài Liệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"d18f2e4aef75ef4dd5de239c97699787f306f8ae5e7b5bc608181b5f1654f285"} -->

## Slide 41 - T ài Liệu Tham Khảo

1 Anthropic. Prompt Engineering Overview. platform.claude.com/docs 2 Anthropic. Claude Prompting Best Practices và Multishot Prompting. platform.claude.com/docs 3 Anthropic. Tool Use Overview. platform.claude.com/docs 4 OpenAI. Function Calling Guide. developers.openai.com/api/docs/guides/function-calling 5 Wei et al. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. 2022. 6 LangGraph Docs. Quickstart. langchain-ai.github.io/langgraph Giảng viên (VinUni) AICB · Ngày 4 T uần 1 30 / 30

---

<!-- chiron-source-span: {"source_span_id":"2417a6d7-580e-5c11-8422-6bfb02885a88","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"88747dbe4ccf68a19b3cd1950886948e7a58fd189dba2fdd945eb70a2b95c530"} -->

## Slide 42 - Hỏi & Đáp

Bạn đang gặp lỗi vì model chưa hiểu ý bạn, hay vì tool contract của bạn chưa đủ rõ?

---

<!-- chiron-source-span: {"source_span_id":"92c4a868-b254-52fe-a7e4-7c160ad2472e","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"79981d038d2c1d1edcc4429d58a0600f5787c736caf2d354a1e14de091f5e741"} -->

## Slide 43 - Cảm ơn!

Email: lecturer@vinuni.edu.vn Slides & tài liệu: github.com/aicb-vinuni Lab template: bit.ly/aicb-day04-lab
