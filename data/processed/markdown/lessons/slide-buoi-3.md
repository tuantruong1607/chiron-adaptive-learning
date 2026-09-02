---
schema_version: 1
course_id: rag-intensive
document_id: "089ec265-1dbf-5aa7-a441-9c3247f4cc22"
document_version_id: "cf93f06e-46d8-5281-bc5e-28fd4935a1af"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Từ Chatbot đến Agentic Agent — phân tích & breakdown từng slide"
source_file: "slide-buoi-3.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-buoi-3.html"
source_sha256: "4e7181a01332595059e4b350f63fed0485e938313ae8125af0117aa72ba807aa"
parser_version: chiron-structured-markdown-v1
html_section_count: 17
interactive_module_count: 1
interactive_control_count: 4
language: vi
---

# Từ Chatbot đến Agentic Agent — phân tích & breakdown từng slide

> 46 slide, trả lời đúng một câu hỏi: khi nào một bài toán thật sự cần agent, và khi 
 nào agent chỉ là chi phí thừa. Bài này là chỗ đầu tiên trong khoá bạn nhìn thấy vòng lặp 
 Thought → Action → Observation — nền của toàn bộ Track 3.

<!-- chiron-source-span: {"source_span_id":"05ff6cab-92c1-52f3-a1b9-c0a6653a3fa9","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-buoi-3.html"},"checksum":"cdba8965bcdf1e7cdf8403965c1923a871689cee119434d93f4bb14a520751dc"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Bài này **nối thẳng từ Ngày 2** và trả lời chi tiết hơn cho đúng một ô trong Problem 
 Statement: *Mức chọn — Rule / Workflow / Agent*. Ngày 2 cho bạn cây quyết định năm câu; Ngày 3 cho 
 bạn một **thang điểm** và một **pattern cụ thể để cài đặt**.

Mạch của bài rất gọn:

```text
phân biệt 3 kiểu hệ thống  →  chấm điểm xem có cần agent  →  kiến trúc agent  →  ReAct  →  code  →  debug  →  hybrid
        ch.1                        ch.2                       ch.3          ch.4     ch.5    ch.6     ch.7
```

Lượt 1 · ~12 phút

Nắm mạch chính

- Đọc slide 7 (spectrum), 11 (4 tiêu chí), 
 22 (vòng lặp ReAct), 38 (hybrid)
- Nhìn Hình 2 — vòng lặp ReAct, hình cốt lõi của cả bài
- Mục tiêu: nói được agent khác chatbot ở vòng lặp, không ở model

Lượt 2 · ~45 phút

Chương 2, 4, 5

- Chấm bài toán của bạn bằng mô-đun Agentic Fit trước khi đọc đáp án
- Đọc kỹ trace ví dụ — mỗi Thought nói rõ agent còn thiếu gì
- Chương 5 đọc code chậm: pseudocode 15 dòng chứa toàn bộ ý tưởng

Lượt 3 · ~15 phút

Trước quiz

- 6 hiểu lầm — nhất là hai cái đầu về định nghĩa agent
- Cheat sheet — bốn tiêu chí, ba vòng ReAct, danh sách guardrail
- Từ điển — ReAct, tool calling, trace, agentic fit, hybrid

"ChatGPT là chatbot hay agent? Siri thì sao? Cursor IDE thì sao?"

"tuỳ lúc"

Agent là một chế độ hoạt động, không phải một loại 
 sản phẩm.

---

<!-- chiron-source-span: {"source_span_id":"9333f345-c8f2-5384-95a1-d9c32d436674","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"slide-buoi-3.html"},"checksum":"2a90cd3aedd1054956fbbc24cd4c0e33f817801490f83b31b9d48fc295e711f4"} -->

## 00 Mở đầu

Slide 1–5: câu hỏi dẫn dắt, bốn mục tiêu, và deliverable so sánh trực tiếp.

### Slide 1–5 Mục tiêu và deliverable — chú ý cấu trúc "so sánh"

> Trích slide 
>  " ChatGPT là chatbot hay agent? Siri thì sao? Cursor IDE thì sao? " 
>  " Mục tiêu: ■ Phân biệt được rule-based bot, LLM chatbot, và agent ■ Dùng Agentic 
>  Fit để biết khi nào nên nâng từ chatbot lên agent ■ Hiểu và giải thích được vòng lặp ReAct: 
>  Thought → Action → Observation ■ Build được ReAct agent đầu tiên với tools, system prompt, và 
>  safeguard cơ bản" 
>  " Deliverable: Chatbot baseline + ReAct agent cho cùng một bài toán, kèm 
>  trace và flowchart. ■ 5 test cases để so sánh ■ 1 trace Thought/Action/Observation ■ 
>  1 nhận định rõ: khi nào chatbot đủ, khi nào agent vượt trội "

Deliverable này có một thiết kế đáng chú ý: nó bắt bạn xây **cả hai** cho *cùng một bài toán*. Đó không phải để tốn thời gian — đó là cách duy nhất để trả lời câu hỏi 
 cuối cùng một cách có căn cứ.

Nếu chỉ xây agent, bạn không bao giờ biết chatbot có đủ hay không — và bạn sẽ luôn cảm thấy agent 
 là lựa chọn đúng, vì nó là thứ duy nhất bạn có.

Xây cả hai rồi chạy *cùng 5 test case* cho ra một dữ liệu mà không lập luận nào thay thế 
 được: **trên test case nào agent thắng, và thắng nhờ điều gì.** Nếu agent chỉ thắng ở 
 1 trong 5 ca, đó là thông tin rất giá trị — có thể tách riêng ca đó ra thay vì đẩy toàn bộ traffic 
 qua agent loop.

Đây chính là [hybrid pattern ở slide 38](#s38), và nó là kết 
 luận thực dụng nhất của cả bài — nhưng nó chỉ *thuyết phục* khi bạn đã tự đo.

---

<!-- chiron-source-span: {"source_span_id":"4bcdeb41-d4e3-5561-ba77-484a6b3e66c9","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Ba kiểu hệ thống AI","source_file":"slide-buoi-3.html"},"checksum":"6c134c3e31e273251e2a1dfef1965e8afd85d2792fb95fe6a0f345df4f101732"} -->

## 01 Ba kiểu hệ thống AI

Slide 6–9: spectrum bốn mức, bảng so sánh sáu tiêu chí, và một bài toán chạy qua cả ba mức.

### Slide 6–8 Spectrum: Bot → Chatbot → Reactive Agent → Autonomous Agent

> Trích slide 
>  " Rule-based Bot — If/else cứng, predictable. LLM Chatbot — 
>  Trả lời thông minh nhưng chủ yếu 1 lượt. Reactive Agent — Dùng tools + loop, quan sát 
>  theo từng bước. Autonomous Agent — Long-horizon goal, nhiều quyết định liên tiếp." 
>  " Khả năng thích nghi, tool use, memory, risk tăng dần " 
>  " Không phải mọi thứ dùng LLM đều là agent. Agent chỉ xuất hiện khi hệ thống phải quyết 
>  định, hành động, quan sát kết quả, rồi lặp lại. "

Câu in đậm là **định nghĩa hoạt động** của agent, và nó gọn hơn mọi định nghĩa dài dòng 
 khác. Bốn động từ: *quyết định → hành động → quan sát → lặp lại*. Thiếu bất kỳ động từ nào thì 
 chưa phải agent.

_Sơ đồ: Bốn mức hệ thống AI từ bot có luật tới agent tự chủ - Bốn ô xếp từ trái sang phải. Rule-based Bot dùng if else cứng, kết quả đoán trước được. LLM Chatbot trả lời thông minh nhưng chủ yếu một lượt. Reactive Agent dùng công cụ và vòng lặp, quan sát theo từng bước. Autonomous Agent giữ mục tiêu dài hạn qua nhiều quyết định liên tiếp. Bên dưới có bốn thanh cho thấy khả năng thích nghi, dùng công cụ, bộ nhớ và rủi ro đều tăng dần từ trái sang phải. Ranh giới thành agent nằm giữa ô thứ hai và ô thứ ba, nơi hệ thống bắt đầu có vòng lặp quan sát._

Hình 1 — Spectrum bốn mức (slide 7).

không

có vòng lặp quan sát hay không

Bốn dòng đầu (cách xử lý, flexibility, memory, tool use) mô tả *năng lực* — và chúng đều 
 nghiêng về phía agent. Nếu chỉ đọc bốn dòng đó, kết luận sẽ là "agent tốt hơn".

| Tiêu chí | Rule-based Bot | LLM Chatbot | Agent |
| --- | --- | --- | --- |
| Cost | Thấp nhất | Trung bình | Cao hơn do loop và nhiều calls |
| Risk | Logic dễ kiểm soát | Hallucination / format drift | Hallucination + tool misuse + loop |

Hai dòng cuối lật ngược lại. Đặc biệt dòng *Risk*: agent kế thừa **toàn bộ** rủi ro của chatbot rồi cộng thêm hai loại mới — *dùng sai tool* và *kẹt vòng lặp*. Đây là phép cộng, không phải phép thay thế. Ai đã học [Ngày 25](track-3-day-25.html) sẽ nhận ra hai loại đó chính là nhóm lỗi ④ và ⑥ trong bản 
 đồ sáu nhóm lỗi.

Bài toán: *"Tìm vé HAN → HCM dưới 2 triệu, rồi gợi ý mang gì nếu trời mưa."*

• **Bot có rule:** trả menu cố định — không search được dữ liệu mới. 
 • **LLM chatbot:** viết câu trả lời mượt — *nhưng không tự truy vấn giá vé thật*. 
 • **Reactive agent:** tách goal thành hai việc, gọi từng tool, so sánh rồi trả lời gộp.

**Điều làm ví dụ này hay:** chatbot ở đây *không phải không 
 đủ thông minh* — nó thừa thông minh để viết câu trả lời hay. Nó thiếu **quyền truy cập dữ 
 liệu thật**. Đó chính xác là "bong bóng thời gian" ở [Ngày 
 1](day-1-ai-llm-foundation.html), và là lý do agent tồn tại: không phải để nghĩ giỏi hơn, mà để *đi lấy được thứ nó cần*.

---

<!-- chiron-source-span: {"source_span_id":"60248e5f-17f6-5f15-903c-b07a2fe980fb","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Agentic Fit Framework","source_file":"slide-buoi-3.html"},"checksum":"ea478c83414a39f8f9792e193017e2c09c21a1ea02b455d9ce747b303889a62f"} -->

## 02 Agentic Fit Framework

Slide 10–15: bốn tiêu chí, ma trận chấm điểm, bốn anti-pattern, và thang pattern của Anthropic.

### Slide 10–12 Bốn tiêu chí và ma trận chấm điểm

> Trích slide 
>  " 1. Multi-step Reasoning — Bài toán có cần chia thành nhiều bước phụ thuộc nhau 
>  không? 2. Tool Interaction — Hệ thống có cần gọi search, API, database, calculator, 
>  browser, file system? 3. Dynamic Decision — Mỗi bước tiếp theo có phụ thuộc vào kết 
>  quả vừa quan sát không? 4. Long Horizon — Hệ thống có phải giữ mục tiêu xuyên suốt 
>  qua nhiều vòng lặp hoặc nhiều state không?" 
>  " Nếu đa số tiêu chí chỉ ở mức 1–2/5, hãy bắt đầu bằng chatbot hoặc workflow đơn giản. " 
>  " Ma trận: FAQ nội bộ HR (1+1+1 = 3) · Tóm tắt hợp đồng và highlight risk 
>  (3+2+2 = 7) · Booking assistant du lịch (4+5+4 = 13) · Research agent tìm đối thủ (4+4+4 = 12) · 
>  Code assistant có test & fix loop (5+5+4 = 14)" 
>  " Gợi ý đọc điểm: 0–5 = chatbot/rule đủ · 6–10 = augmented chatbot · 11+ = agent đáng 
>  thử "

Bốn tiêu chí này **không độc lập nhau**, và nhận ra quan hệ giữa chúng giúp chấm nhanh 
 và nhất quán hơn:

| Tiêu chí | Câu hỏi kiểm tra nhanh | Quan hệ với các tiêu chí khác |
| --- | --- | --- |
| 1 · Multi-step reasoning | Vẽ ra được mấy bước? Bước sau có cần kết quả bước trước không? | Điều kiện cần cho ③ — không nhiều bước thì không có gì để quyết động |
| 2 · Tool interaction | Có dữ liệu nào model không thể tự biết không? | Độc lập nhất. Có thể cao trong khi ba cái kia thấp |
| 3 · Dynamic decision | Lộ trình có viết trước được không? (câu của Ngày 2 ) | Tiêu chí quyết định nhất — nó là ranh giới workflow ↔ agent |
| 4 · Long horizon | Mục tiêu có kéo dài qua nhiều phiên / nhiều state không? | Thường đi kèm ①. Là tiêu chí phân biệt reactive với autonomous agent |

Slide 11 định nghĩa **bốn** tiêu chí. Nhưng ma trận ở slide 12 chỉ có **ba cột**: Reasoning, Tool use, Dynamic decision — *Long Horizon bị bỏ ra*.

Kiểm lại các tổng thì đúng là cộng ba: FAQ 1+1+1 = 3 ✓ · Hợp đồng 3+2+2 = 7 ✓ · 
 Booking 4+5+4 = 13 ✓ · Research 4+4+4 = 12 ✓ · Code assistant 5+5+4 = 14 ✓.

**Hệ quả cho việc dùng thang điểm:** ngưỡng *0–5 / 6–10 / 11+* được thiết kế cho thang tối đa **15** (3 tiêu chí × 5), không 
 phải 20. Nếu bạn cộng cả bốn tiêu chí rồi so với ngưỡng đó, bạn sẽ đẩy mọi bài toán lên cao hơn thực 
 tế. [Mô-đun bên dưới](#m-fit) tính cả hai cách để bạn thấy khác biệt.

Nhìn cột **Tool use**: FAQ 1 · Hợp đồng 2 · Booking 5 · Research 4 · Code 5. 
 Nhìn cột **Dynamic decision**: 1 · 2 · 4 · 4 · 4.

Hai ca ở giữa (FAQ và Tóm tắt hợp đồng) đều thấp ở *cả hai* cột — đó là lý do chúng rơi vào 
 vùng chatbot. Nhưng chú ý **Tóm tắt hợp đồng có Reasoning = 3**, cao hơn hẳn tool use và 
 dynamic decision của nó.

**Đó là mẫu hình đáng nhớ:** "suy luận nhiều bước" một mình *không* đòi agent — vì các bước đó có thể viết cố định thành một chuỗi prompt. 
 Cái đòi agent là khi **bước tiếp theo phụ thuộc kết quả vừa quan sát**. Tiêu chí ③ mới 
 là tiêu chí phân định.

#### Tương tác Chấm Agentic Fit cho bài toán của bạn

Cho điểm 1–5 từng tiêu chí. Mô-đun tính tổng theo *cả hai* cách — ba tiêu chí 
 (khớp ma trận slide 12) và bốn tiêu chí (khớp định nghĩa slide 11) — rồi đối chiếu với ngưỡng.

Mặc định là ca **Tóm tắt hợp đồng và highlight risk** ở slide 12: 
 Reasoning **3**, Tool use **2**, Dynamic decision **2**, 
 Long horizon **2**.

Đoán trước: tổng ba tiêu chí là 7 ⇒ rơi vào vùng nào? Và nếu cộng cả bốn thì kết luận có đổi không?

#### Xem thẻ số rồi mở

**Ba tiêu chí: 7/15 ⇒ "augmented chatbot" — không cần agent.** Bốn tiêu chí: 9/20, cũng vẫn trong vùng 6–10 nếu dùng chung ngưỡng.

**Nhưng đây là chỗ ngưỡng bắt đầu lệch.** Với thang 20, vùng "6–10" chỉ chiếm 25% 
 dải điểm thay vì 33% như ở thang 15 — nên một bài toán ở giữa dễ bị đẩy lên vùng "agent đáng thử" 
 một cách máy móc. Mô-đun tính thêm *ngưỡng đã chuẩn hoá* (nhân 20/15) để so cho công bằng: 
 vùng agent bắt đầu từ **14,7** chứ không phải 11.

**Thử ca Booking assistant** (4, 5, 4, 4): ba tiêu chí = **13/15** ⇒ 
 agent đáng thử. Bốn tiêu chí = 17/20, vượt cả ngưỡng chuẩn hoá 14,7 ⇒ kết luận nhất quán.

**Và thử một ca dễ nhầm:** đặt Reasoning = 5, Tool use = 1, Dynamic = 1, 
 Long horizon = 1. Tổng ba tiêu chí chỉ **7** — vẫn là chatbot. Suy luận nhiều bước 
 một mình *không* đòi agent, vì chuỗi bước cố định viết được bằng prompt chaining. **Chỉ tiêu chí ③ mới mở cửa cho agent.**

*Thử ngược lại:* Reasoning 2, Tool use 2, Dynamic 5 — tổng 9, vẫn dưới ngưỡng. Nghĩa là 
 thang điểm này *không* để một tiêu chí đơn lẻ quyết định; nó đòi ít nhất hai tiêu chí cùng 
 cao. Đó là thiết kế có chủ ý, và nó chống lại việc "tìm cớ để dùng agent".

- **Control - ① Multi-step reasoning 3 /5**: min `1`, max `5`, step `1`, default `3`

- **Control - ② Tool interaction 2 /5**: min `1`, max `5`, step `1`, default `2`

- **Control - ③ Dynamic decision 2 /5**: min `1`, max `5`, step `1`, default `2`

- **Control - ④ Long horizon 2 /5**: min `1`, max `5`, step `1`, default `2`

Tổng 3 tiêu chí (như slide 12)

—

thang tối đa 15

Kết luận

—

—

Tổng 4 tiêu chí

—

—

Tiêu chí quyết định

—

—

điểm của bạn năm ca mẫu ở slide 12 ngưỡng 11 — agent đáng thử

#### Xem bảng năm ca mẫu và bảng ngưỡng



#### Công thức & giới hạn của mô hình

- Tổng 3 = reasoning + tool + dynamic — đúng cách ma trận slide 12 cộng (đã kiểm lại 
 cả năm dòng ví dụ đều khớp).
- Tổng 4 cộng thêm long horizon theo định nghĩa slide 11. 
 Ngưỡng chuẩn hoá = ngưỡng gốc × 20/15, tức 8,0 và 14,7 — đây là 
 phép quy đổi của tài liệu này, không có trên slide.
- Ngưỡng gốc 0–5 / 6–10 / 11+ lấy nguyên từ slide 12. Slide không giải thích 
 chúng đến từ đâu — hãy coi là quy ước dạy học, không phải kết quả nghiên cứu.
- "Tiêu chí quyết định" là nhận định của tài liệu này: khi ③ (dynamic decision) 
 ≥ 4 thì nó là yếu tố mở cửa cho agent, vì đó chính là ranh giới workflow ↔ agent mà 
 Ngày 2 và Anthropic đều dùng.
- Thang điểm này là công cụ đối thoại, không phải phép đo. Hai người chấm cùng 
 một bài toán có thể lệch 1–2 điểm mỗi tiêu chí. Giá trị của nó nằm ở việc bắt bạn nói ra lý do 
 cho từng điểm, không nằm ở con số tổng.

### Slide 13–15 Bốn anti-pattern, và thang pattern của Anthropic

> Trích slide 
>  " Anti-Patterns — khi dùng agent là sai bài: □ Bài toán 1 bước: hỏi đáp, tra FAQ, 
>  phân loại cơ bản □ Không có tool nào để gọi: agent chỉ 'suy nghĩ' nhưng không hành động được 
>  □ Mọi thứ phải 100% deterministic: mỗi sai sót đều rất đắt □ Chi phí latency không chấp nhận được: 
>  loop 3–5 bước là đã quá chậm" 
>  " Nguyên tắc: luôn benchmark rule / workflow / chatbot trước khi mở agent loop " 
>  " Anthropic — agent patterns nên tăng dần theo nhu cầu: Augmented LLM (prompt + 
>  docs + tools) → Prompt Chaining → Routing → Orchestrator-Worker → Agent" 
>  " Bắt đầu từ cấu trúc đơn giản nhất đủ dùng. Agent là pattern mạnh nhưng cũng đắt nhất về cost, 
>  eval, guardrails, và vận hành. "

Anti-pattern thứ hai đáng dừng lại, vì nó là lỗi **hay gặp nhất ở người mới học agent**:

Đây là một agent *rỗng*: nó chạy vòng lặp Thought → Action → Observation, nhưng mọi Action 
 đều là "suy nghĩ thêm" chứ không chạm được vào thế giới bên ngoài.

Kết quả: bạn trả tiền cho nhiều lượt gọi model, chịu độ trễ của vòng lặp, **và nhận về đúng thứ mà một prompt duy nhất có "hãy nghĩ từng bước" đã cho** — 
 chính là Chain-of-Thought ở [Ngày 1](day-1-ai-llm-foundation.html), nhưng đắt hơn nhiều lần.

**Cách tự kiểm rất nhanh:** liệt kê các tool agent của bạn có. 
 Nếu danh sách trống, hoặc mọi tool đều là biến thể của "gọi lại chính model", bạn không cần agent — 
 bạn cần một prompt tốt hơn.

| Anthropic (slide 15) | Ngày 2 gọi là | Đặc trưng |
| --- | --- | --- |
| Augmented LLM — prompt + docs + tools | Workflow (đơn giản nhất) | Một lượt gọi, có ngữ cảnh và tool |
| Prompt Chaining | Workflow | Chuỗi bước cố định, có gate giữa các bước |
| Routing | Workflow | Phân loại rồi rẽ nhánh — mỗi nhánh viết trước |
| Orchestrator-Worker | Ranh giới | Phân việc động, nhưng khung điều phối vẫn do code |
| Agent | Agent | Model tự quyết lộ trình nhiều bước |

**Điều đáng chú ý:** bốn trong năm pattern nằm ở phía *workflow*. Nghĩa là khoảng cách từ "một prompt" tới "agent thật" có rất nhiều nấc trung gian 
 — và phần lớn bài toán dừng lại ở một trong các nấc đó. Đây là cùng thông điệp với [cây quyết định Ngày 2](slide-buoi-2.html), chỉ khác là Anthropic chia mịn hơn.

deliverable slide 5

chatbot baseline + ReAct agent cho cùng một bài toán, chạy cùng 5 test case

đó là một kết quả hợp lệ và 
 đáng nộp

#### Ô kiểm tra — Chương 1 & 2

Trả lời thành tiếng trước khi mở đáp án.

**1.** Hệ thống của bạn gọi LLM sáu lần cho mỗi yêu cầu, theo một trình tự cố định. 
 Đó là agent chưa? Hiểu

#### Đáp án

**Chưa. Đó là *prompt chaining* — một workflow.**

Định nghĩa hoạt động ở slide 7: *"Agent chỉ xuất hiện khi hệ thống phải quyết định, hành động, 
 quan sát kết quả, rồi lặp lại."* Bốn động từ, và cái thiếu ở đây là **quyết định**: 
 trình tự sáu bước đã được viết sẵn, model không chọn bước tiếp theo.

**Ranh giới không nằm ở "có dùng LLM" hay "gọi bao nhiêu lần"** mà ở *lộ trình có viết trước được không* — cùng câu hỏi mà [Ngày 2](slide-buoi-2.html) dùng để phân biệt workflow với agent.

**Ngược lại:** một hệ thống chỉ gọi LLM *hai* lần, nhưng lần thứ hai gọi tool 
 nào là do kết quả lần đầu quyết định — *đã là agent*.

**2.** Chấm Agentic Fit cho "tóm tắt hợp đồng và highlight rủi ro" ra 7 điểm. 
 Nhưng bài toán này rõ ràng cần suy luận nhiều bước. Vì sao vẫn không nên dùng 
 agent? Phân tích

#### Đáp án

**Vì suy luận nhiều bước một mình không đòi agent — các bước đó viết cố định được.**

Nhìn điểm từng tiêu chí: Reasoning **3**, Tool use **2**, 
 Dynamic decision **2**. Chỉ tiêu chí ① cao.

Quy trình "đọc hợp đồng → trích điều khoản → đối chiếu danh mục rủi ro → viết tóm tắt" là một *chuỗi cố định*. Bước 3 luôn theo sau bước 2, bất kể bước 2 trả về gì. Đó là **prompt chaining** — pattern thứ hai trong thang Anthropic, thuộc phía workflow.

**Cái mở cửa cho agent là tiêu chí ③** — "bước tiếp theo phụ thuộc kết quả vừa quan 
 sát". Ở đây nó chỉ 2/5.

**Kiểm chứng bằng mô-đun:** đặt Reasoning = 5 mà Tool = 1, Dynamic = 1 thì tổng vẫn 
 chỉ 7 — dưới ngưỡng. Thang điểm được thiết kế để *một tiêu chí đơn lẻ không quyết định được*.

**3.** Đồng nghiệp xây một agent cho bài toán viết email marketing. Agent chạy 4 
 vòng lặp, mỗi vòng đều "suy nghĩ" rồi tự đánh giá bản nháp. Nhận xét. Đánh giá

#### Đáp án

**Đây là anti-pattern thứ hai ở slide 13: "không có tool nào để gọi — agent chỉ suy nghĩ 
 nhưng không hành động được".**

Mọi Action đều là biến thể của "gọi lại chính model". Agent không chạm được vào thế giới bên 
 ngoài, nên vòng lặp không mang về *thông tin mới* nào — chỉ mang về ý kiến của chính model 
 về chính nó.

**Cái giá:** trả tiền cho 4 lượt gọi thay vì 1, cộng độ trễ của vòng lặp, để nhận 
 về thứ mà một prompt có "hãy nghĩ từng bước rồi tự rà lại" đã cho — chính là Chain-of-Thought ở 
 Ngày 1, rẻ hơn nhiều lần.

**Đề xuất thay thế:** nếu muốn vòng lặp tự cải thiện thật, hãy cho nó một *tín hiệu bên ngoài* — dữ liệu hiệu quả email cũ, checklist thương hiệu dưới dạng tool tra 
 cứu, hoặc một model khác làm evaluator (pattern *evaluator-optimizer* ). Khi đó vòng lặp mới 
 có cái để quan sát.

**Cách tự kiểm nhanh:** liệt kê tool của agent. Danh sách trống hoặc toàn "gọi lại 
 model" ⇒ bạn cần prompt tốt hơn, không cần agent.

---

<!-- chiron-source-span: {"source_span_id":"af4cd035-fcab-5c0b-923f-102290ace957","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Kiến trúc agent","source_file":"slide-buoi-3.html"},"checksum":"8d3d0e82905203c9fbcc6e253b16c6bac76c6f6da7272c76f6ba688466773904"} -->

## 03 Kiến trúc agent

Slide 16–19: bốn khối, hai loại memory, và tool calling như "tay chân" của agent.

### Slide 16–18 Bốn khối kiến trúc, và hai loại memory

> Trích slide 
>  "■ Perception: agent nhận text, tool output, feedback ■ Reasoning: 
>  phân tích trạng thái và chọn bước tiếp theo ■ Action: gọi tool hoặc trả lời user 
>  ■ Memory: giữ goal, facts, và intermediate results" 
>  " 4 khối kiến trúc thường kéo theo 4 nhóm cost chính: token, storage, API, và latency. " 
>  " Short-term memory — nằm trong context window, dùng cho task hiện tại, rẻ để 
>  implement nhưng dễ đầy. Long-term memory — lưu facts, preferences, state ngoài 
>  context; có thể là DB, vector store, key-value store; cần retrieval strategy và permission 
>  model." 
>  " Không phải thêm memory là agent giỏi hơn. Memory chỉ có ích khi chiến lược đọc/ghi và 
>  quyền truy cập được thiết kế rõ. "

Câu về **bốn nhóm chi phí** là câu đáng nhớ nhất slide 17, vì nó biến một sơ đồ kiến 
 trúc thành một bảng ngân sách:

| Khối | Nhóm chi phí | Tăng lên khi | Kiểm soát bằng |
| --- | --- | --- | --- |
| Perception | Token | Tool output dài, lịch sử tích luỹ | Cắt gọn observation trước khi nhét vào context |
| Reasoning | Token + latency | Mỗi vòng lặp là một lượt gọi model | MAX_ITERATIONS ( slide 30 ) |
| Action | API + latency | Nhiều tool call, tool chậm | Timeout mỗi tool, gọi song song khi độc lập |
| Memory | Storage + token | Long-term memory phình ra | Retrieval strategy — chỉ lấy phần liên quan |

Một chatbot: **1 lượt gọi model**. Một agent 4 vòng lặp: **4 lượt gọi**, 
 và mỗi lượt sau đọc lại toàn bộ lịch sử của các lượt trước — *cộng thêm observation từ tool*.

Đây đúng là cơ chế "càng chat càng đắt" ở [Ngày 1](day-1-ai-llm-foundation.html), nhưng 
 xảy ra **trong một request duy nhất**. Người dùng chỉ hỏi một câu; agent tự sinh ra một 
 cuộc hội thoại nội bộ dài.

**Hệ quả thực hành:** tool trả về output dài (một trang JSON, 
 một kết quả tìm kiếm 20 mục) sẽ bị đọc lại ở *mọi* vòng lặp sau. Cắt gọn observation là việc 
 rẻ nhất và hiệu quả nhất để giảm chi phí agent — rẻ hơn cả việc hạ tầng model.

*"Không phải thêm memory là agent giỏi hơn."* Long-term memory nghe như một nâng cấp hiển 
 nhiên, nhưng slide gắn hai điều kiện: **retrieval strategy** và **permission model**.

Thiếu điều kiện thứ nhất, memory phình ra và agent lôi vào context những 
 thứ không liên quan — đúng "context rác = attention rác" của Ngày 1. Thiếu điều kiện thứ hai, agent 
 có thể nhớ và tiết lộ thông tin của người dùng này cho người dùng khác — cùng loại rủi ro với [false-hit của semantic cache ở Ngày 25](track-3-day-25.html). Memory là chủ đề riêng của 
 Ngày 17.

### Slide 19 Tool calling — cầu nối giữa suy luận và thế giới thật

> Trích slide 
>  "User Goal → LLM → Tool Call (JSON/args) → API / DB / Search → observation → LLM → final answer" 
>  "■ Tool definitions phải rõ input / output / error mode ■ Agent mạnh lên nhờ tool, 
>  nhưng cũng dễ fail hơn vì external dependency ■ Tool calling là cầu nối giữa reasoning trong 
>  model và hành động ngoài thế giới thực"

```text
Mục tiêu người dùng
        │
        ▼
  ┌───────────┐   quyết định gọi tool nào, với tham số gì
  │    LLM    │───────────────────┐
  └───────────┘                   ▼
        ▲              ┌──────────────────────┐
        │              │  {"tool": "get_...",  │   ← JSON có schema
        │              │   "args": {...}}      │
        │              └──────────┬───────────┘
        │                         ▼
        │              ┌──────────────────────┐
        │              │  API / DB / Search   │   ← thế giới thật
        │              └──────────┬───────────┘
        │   observation           │
        └─────────────────────────┘
        │
        ▼  đủ thông tin
   Câu trả lời cuối
```

Người ta thường mô tả tool bằng *nó làm gì* và *cần tham số nào*. Rất ít mô tả **nó hỏng như thế nào**.

Nhưng agent phải biết phân biệt ba tình huống khác nhau: *"không tìm thấy kết quả"* (nên 
 thử truy vấn khác), *"tham số sai định dạng"* (nên sửa args rồi gọi lại), và *"dịch vụ đang lỗi"* (nên chuyển sang phương án khác hoặc dừng). Nếu cả ba đều trả về cùng một 
 thông báo lỗi mơ hồ, agent sẽ xử lý sai — thường là gọi lại y hệt, và đó là một trong bốn dấu hiệu 
 kẹt vòng lặp ở [slide 30](#s30).

**Việc rẻ nhất bạn làm được:** trong mô tả mỗi tool, thêm một 
 dòng *"Trả về X khi không có kết quả; trả về lỗi Y khi tham số không hợp lệ."* Ngày 4 sẽ đi 
 sâu vào cách viết tool description.

bốn

tool/cache failure

Ngày 25

---

<!-- chiron-source-span: {"source_span_id":"de2a3522-2460-5f85-ada0-c3d29f130132","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 ReAct Pattern","source_file":"slide-buoi-3.html"},"checksum":"9bc7fdb8d2a8d5412a9e15c27216e97e8401dee637f20502502c05cc6e405128"} -->

## 04 ReAct Pattern

Slide 20–25: định nghĩa, vòng lặp ba bước, trace mẫu, và giới hạn của pattern.

### Slide 20–22 ReAct = Reasoning + Acting

> Trích slide 
>  "ReAct là pattern kết hợp suy luận theo từng bước với gọi công cụ và quan sát kết quả. Thay vì trả 
>  lời ngay, agent sẽ lặp qua các bước: ■ Thought: mình đang thiếu gì, nên làm gì tiếp? 
>  ■ Action: gọi tool nào, với tham số nào? ■ Observation: kết quả trả 
>  về là gì? ■ Lặp lại đến khi đủ thông tin để trả lời hoặc gặp điều kiện dừng" 
>  " ReAct mạnh vì trace lý do hành động được bộc lộ ra ngoài, giúp con người debug và can 
>  thiệp dễ hơn so với chỉ nhìn final answer. "

Câu in đậm nêu **lý do thật** khiến ReAct trở thành pattern được dạy đầu tiên — và nó 
 không phải "vì ReAct cho câu trả lời tốt hơn".

_Sơ đồ: Vòng lặp ReAct gồm Thought, Action, Observation và điều kiện dừng - Đầu vào của người dùng đi vào bước Thought, nơi agent phân tích còn thiếu gì và nên làm gì tiếp. Từ Thought sang Action, agent gọi một công cụ với tham số cụ thể. Kết quả trả về là Observation. Nếu chưa đủ thông tin, vòng lặp quay lại Thought. Nếu đủ, agent đưa ra câu trả lời cuối. Bên phải liệt kê ba chốt an toàn gắn vào vòng lặp: giới hạn số vòng, timeout cho mỗi công cụ, và trần chi phí. Bên dưới là ví dụ trace ba vòng cho bài toán tìm chuyến bay và kiểm tra thời tiết._

Hình 2 — Vòng lặp ReAct (slide 22–24).

Observation

Với một chatbot, khi câu trả lời sai bạn chỉ có *một* thứ để nhìn: câu trả lời. Bạn đoán 
 xem prompt sai chỗ nào, sửa, chạy lại, đoán tiếp.

Với ReAct, bạn thấy **chuỗi quyết định**: agent nghĩ gì ở bước 1, chọn tool nào, 
 nhận về gì, rồi từ đó nghĩ tiếp ra sao. Khi kết quả sai, bạn khoanh vùng được ngay — *Thought sai mục tiêu? Chọn nhầm tool? Args sai? Hay Observation thiếu field?* Đó chính là 
 bốn câu trong [checklist debug ở slide 35](#s35).

**Hệ quả sâu hơn:** vì trace nhìn được, bạn *đánh giá* được nó — và đó là lý do [Ngày 24](track-3-day-24.html) nói *"agent quality = trajectory quality, không phải final answer"*. Một agent trả lời đúng nhờ 
 gọi sai tool năm lần vẫn là một agent hỏng, và chỉ trace mới cho bạn thấy điều đó.

### Slide 23–25 Trace mẫu, và giới hạn của ReAct

> Trích slide 
>  " Thought 1: Tôi cần tìm chuyến bay sáng mai từ HAN tới HCM dưới 2 triệu. 
>  Action 1: search_flights(origin="HAN", destination="SGN", date="2026-03-18", 
>  max_price=2000000) Observation 1: Có 2 lựa chọn phù hợp […] 
>  Thought 2: User cũng hỏi về trang phục nếu trời mưa. Tôi cần check thời tiết […]" 
>  " Mỗi Thought nên làm rõ agent còn thiếu gì; mỗi Action phải chỉ ra tool và args đủ cụ thể để 
>  kiểm tra. " 
>  " Giới hạn: ■ Tốn nhiều token và latency hơn chatbot ■ Dễ loop hoặc gọi sai tool 
>  ■ Cần eval theo trace, không chỉ final answer ■ Không phù hợp bài toán đơn giản hoặc 
>  cần deterministic tuyệt đối" 
>  " ReAct dễ bắt đầu nhất, nhưng khi hệ thống nhiều nhánh hơn, nên chuyển sang graph/state machine 
>  rõ ràng. "

Lời khuyên về cách viết Thought và Action đáng đọc kỹ, vì nó là **tiêu chí chấm một trace tốt 
 hay tệ**:

|  | Trace tốt | Trace tệ |
| --- | --- | --- |
| Thought | Nói rõ còn thiếu gì: "Tôi cần tìm chuyến bay… dưới 2 triệu" | Kể lại việc đã làm: "Tôi sẽ giúp bạn tìm chuyến bay" |
| Action | Tool và args cụ thể tới mức kiểm tra được: search_flights(origin="HAN", …, max_price=2000000) | Mơ hồ: search("chuyến bay rẻ") |
| Observation | Dữ liệu thật, có thể đối chiếu | Model tự bịa kết quả — vi phạm rule "never invent tool results" |

**① Tốn token và latency.** Trace ba vòng ở trên = ba lượt gọi model, mỗi lượt đọc lại 
 toàn bộ trace trước đó. Chi phí không tăng tuyến tính mà nhanh hơn.

**② Dễ loop hoặc gọi sai tool.** Bốn dấu hiệu ở [slide 30](#s30): lặp cùng 
 một tool call, hỏi lại thông tin đã có, reasoning không tiến thêm, observation không đổi mà vẫn tiếp 
 tục.

**③ Cần eval theo trace, không chỉ final answer.** Đây là giới hạn *khó chịu 
 nhất* về mặt vận hành: bạn không thể chấm agent bằng một hàm so sánh chuỗi. Muốn biết agent tốt 
 hay không, phải đọc đường đi — và đó là bài toán mà cả [Ngày 24](track-3-day-24.html) dành 
 ra để giải.

Ba giới hạn này cộng lại chính là ba dòng "mất gì" của pattern *Agent* trong bảng tradeoff ở [Ngày 2](slide-buoi-2.html): chi phí cao, lỗi cộng 
 dồn, khó kiểm thử.

"ReAct dễ bắt đầu nhất, nhưng khi hệ thống nhiều nhánh hơn, nên chuyển sang graph/state machine 
 rõ ràng."

toàn bộ logic điều hướng nằm trong prompt

code

#### Ô kiểm tra — Chương 3 & 4

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao chi phí một agent 4 vòng lặp cao hơn *nhiều* so với 4 lần gọi 
 chatbot riêng lẻ? Phân tích

#### Đáp án

**Vì mỗi vòng lặp đọc lại toàn bộ lịch sử của các vòng trước — cộng cả observation từ 
 tool.**

Bốn lần gọi chatbot riêng lẻ: mỗi lần chỉ có prompt của riêng nó. Một agent 4 vòng: vòng 2 đọc 
 (prompt + thought 1 + action 1 + observation 1), vòng 3 đọc thêm vòng 2, v.v. Đây là tăng trưởng 
 bậc hai — cùng cơ chế "càng chat càng đắt" của Ngày 1, nhưng xảy ra *trong một request duy 
 nhất*.

**Điểm nặng nhất là observation:** nếu tool trả về một trang JSON hoặc 20 kết quả 
 tìm kiếm, khối đó bị đọc lại ở *mọi* vòng sau.

**Cách giảm rẻ nhất:** cắt gọn observation trước khi nhét vào context — chỉ giữ 
 trường agent thật sự cần. Rẻ hơn và hiệu quả hơn việc hạ tầng model.

**Cộng thêm:** latency cũng nhân lên vì các vòng *phải* tuần tự — vòng sau 
 cần observation của vòng trước.

**2.** Agent của bạn trả lời đúng, nhưng trace cho thấy nó gọi `search_flights` ba lần với cùng tham số. Đánh giá. Đánh giá

#### Đáp án

**Đây là một agent hỏng, dù câu trả lời đúng.**

"Lặp lại cùng một tool call" là dấu hiệu kẹt vòng lặp số một ở slide 30. Nó tốn tiền gấp ba, 
 chậm gấp ba, và lần này may mà kết thúc đúng — lần sau có thể chạm `MAX_ITERATIONS` rồi 
 trả về lỗi.

**Nguyên tắc:** *agent quality = trajectory quality, không phải final answer* (Ngày 24, slide 13). Chấm agent bằng câu trả lời cuối sẽ bỏ sót đúng loại lỗi này.

**Chẩn đoán theo checklist slide 35:** ① Thought có tiến triển không, hay lặp lại 
 cùng một nội dung? ② Observation có thay đổi giữa ba lần gọi không? Nếu không đổi mà agent vẫn gọi 
 lại ⇒ nó không "nhìn thấy" observation — thường do **tool description mơ hồ** hoặc **system prompt thiếu rule dừng**.

**Sửa:** làm rõ tool description (nêu cả error mode), thêm rule "không gọi lại cùng 
 tool với cùng tham số", và thêm safeguard phát hiện lặp.

**3.** Khi nào nên chuyển từ ReAct thuần sang graph/state machine, và bạn *mất* gì khi chuyển? Hiểu

#### Đáp án

**Khi hệ thống có nhiều nhánh, hoặc cần lưu state qua nhiều phiên.**

**Lý do:** trong ReAct thuần, toàn bộ logic điều hướng nằm *trong prompt* — 
 bạn dặn model khi nào dừng, khi nào gọi tool nào. Prompt là chỗ tệ nhất để đặt logic phân nhánh: 
 không kiểm thử được từng nhánh riêng, không nhìn thấy state, và không có gì đảm bảo model tuân thủ 
 chỉ dẫn.

Graph đưa logic đó ra **code**: node, conditional edge, state tường minh — kiểm thử 
 được, đọc được, persist được.

**Mất gì:** tính linh hoạt. Trong ReAct, model tự nghĩ ra lộ trình cho tình huống 
 bạn chưa lường; trong graph, model chỉ đi được những cạnh bạn đã vẽ. Với bài toán mở thì đó là mất 
 mát thật; với bài toán có phạm vi rõ thì đó lại là *ưu điểm* — bạn biết chắc nó không đi 
 đâu ngoài dự tính.

**Và bạn mất cả sự đơn giản:** ReAct là 15 dòng pseudocode; graph cần định nghĩa 
 state schema, reducer, node, edge. Đó là lý do slide gọi ReAct là "dễ bắt đầu nhất" — nó phù hợp để *học bản chất*, còn graph phù hợp để *vận hành*.

---

<!-- chiron-source-span: {"source_span_id":"551fd677-08cb-5d23-a522-a38de95d362b","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Agent loop — code anatomy","source_file":"slide-buoi-3.html"},"checksum":"9333ed8abbae9bafede631885ef79310728df413e0cb4e2578a7583c2e84c942"} -->

## 05 Agent loop — code anatomy

Slide 26–31: pseudocode 15 dòng, system prompt, tool registry, guardrail, và đường sang LangGraph.

### Slide 26–27 Pseudocode: toàn bộ agent trong 15 dòng

> Trích slide 
>  messages = [] 
>  for step in range(MAX_ITERATIONS): 
>  output = call_model(system=SYSTEM_PROMPT, messages=messages, tools=TOOLS) 
>  if output.type == "final_answer": 
>  return output.content 
>  result = run_tool(output.name, output.args) 
>  messages += [output.as_message(), tool_message(output.name, result)] 
>  return "Stopped: max iterations reached"

Mười lăm dòng này chứa **toàn bộ ý tưởng agent**. Đáng đọc chậm, vì mỗi dòng ứng với một 
 khái niệm đã học:

| Dòng | Làm gì | Ứng với khái niệm |
| --- | --- | --- |
| for step in range(MAX_ITERATIONS) | Vòng lặp có trần | Guardrail — chống lặp vô hạn ( slide 30 ) |
| call_model(system, messages, tools) | Reasoning — model chọn bước tiếp | Khối Reasoning ( slide 17 ) |
| if output.type == "final_answer": return | Điều kiện dừng | Nhánh "đủ" trong Hình 2 |
| run_tool(output.name, output.args) | Action — chạm thế giới thật | Khối Action · tool calling |
| messages += [...] | Nối kết quả vào ngữ cảnh | Short-term memory — và là nguồn chi phí |
| return "Stopped: max iterations" | Lối thoát khi hết lượt | Dead-letter — nối sang Ngày 23 |

`return "Stopped: max iterations reached"` — nó nằm *ngoài* vòng lặp, và nó là 
 thứ đảm bảo hàm luôn trả về một cái gì đó.

Người mới viết agent hay bỏ nhánh này, hoặc để nó ném exception. Cả hai đều tệ: 
 không có nhánh thì hàm trả `None` và lỗi nổ ở chỗ khác; ném exception thì người dùng nhận 
 một trang lỗi thay vì một câu trả lời.

**Cách làm đúng:** nhánh này phải trả về một câu *hữu ích cho người dùng* — "tôi chưa hoàn tất được yêu cầu này, đây là những gì tôi đã tìm 
 được, bạn có muốn chuyển sang nhân viên hỗ trợ không?" Đây chính là *dead-letter* và *fallback* mà Ngày 23 và [Ngày 25](track-3-day-25.html) dạy có hệ thống.

run_tool

chủ ý

ý tưởng cốt lõi

Ngày 25

### Slide 28–29 System prompt và tool registry

> Trích slide 
>  " SYSTEM_PROMPT: You are a travel planning agent. Your job: Break the user goal 
>  into smaller steps · Use tools when fresh information is required · Think briefly, then choose the 
>  best next action · Stop when you have enough evidence to answer. " 
>  " Rules: Never invent tool results · If a tool fails, explain the failure and 
>  try a fallback · Keep internal thoughts short and actionable · Output either a tool call or a final 
>  answer " 
>  " TOOLS = {"get_weather": {"description": "Weather by city/date", "args": ["city","date"]}, 
>  "search_flights": {"description": "Flights by route/date/budget", "args": [...]}} "

Bốn *rule* ở nửa dưới system prompt đáng phân tích, vì mỗi rule chặn một chế độ hỏng cụ thể:

| Rule | Chặn chế độ hỏng nào | Nếu thiếu thì sao |
| --- | --- | --- |
| Never invent tool results | Bịa observation | Agent "tưởng tượng" ra kết quả tool và trả lời tự tin — lỗi tệ nhất, vì trace trông hợp lệ |
| If a tool fails, explain and try a fallback | Kẹt khi tool lỗi | Agent gọi lại y hệt cho tới khi hết lượt |
| Keep internal thoughts short and actionable | Token phình | Mỗi Thought dài một đoạn văn ⇒ chi phí tăng, và trace khó đọc |
| Output either a tool call or a final answer | Đầu ra không parse được | Model trả về văn xuôi lẫn lộn ⇒ vòng lặp không biết làm gì tiếp |

*"Never invent tool results"* chặn đúng loại lỗi nguy hiểm nhất của agent: model tự viết ra 
 một Observation mà tool chưa hề trả về. Khi đó trace **trông hoàn toàn hợp lệ** — 
 có Thought, có Action, có Observation — nhưng dữ liệu là bịa.

**Nhưng đây chỉ là một câu trong prompt, tức là một thoả thuận, không phải cưỡng chế.** Cách chặn thật nằm ở kiến trúc: vòng lặp phải *tự chèn* observation từ kết quả `run_tool` vào messages, chứ không để model tự viết. Nhìn lại pseudocode ở slide 27 sẽ thấy 
 nó làm đúng vậy — `tool_message(output.name, result)` được thêm bởi *code*.

Đây là cùng bài học với [Ngày 24](track-3-day-24.html): *"system prompt alone không đủ"*. Prompt giảm xác suất; kiến trúc mới là thứ đảm bảo.

"description": "Weather by city/date"

slide 19

"tool definitions phải rõ input / 
 output / error mode"

input

"thử viết lại tool description theo hướng rõ input, output, và failure mode hơn"

### Slide 30–31 Guardrail chống lặp, và đường sang LangGraph

> Trích slide 
>  " Cần guardrails gì? ■ Giới hạn số vòng lặp ■ Timeout cho từng tool ■ Budget token 
>  / cost trần ■ Retry có kiểm soát ■ Fallback sang human hoặc chatbot" 
>  " Dấu hiệu loop: ■ lặp lại cùng một tool call ■ hỏi lại thông tin đã có ■ reasoning 
>  không tiến thêm ■ observation không thay đổi nhưng vẫn tiếp tục" 
>  " Từ ReAct đến LangGraph: State Input → LLM Node → Tool Node → Conditional Edge → 
>  Final Answer. ■ ReAct loop bằng tay phù hợp để học bản chất ■ LangGraph giúp biểu diễn state, nodes, 
>  edges, conditional routing rõ hơn ■ Khi workflow nhiều nhánh hoặc cần persist state, graph approach dễ 
>  maintain hơn loop ad-hoc"

Bốn dấu hiệu loop đáng học thuộc, vì chúng là thứ bạn *lập trình được* — không phải chỉ để 
 con người nhìn:

| Dấu hiệu | Phát hiện tự động bằng cách nào | Xử lý |
| --- | --- | --- |
| Lặp lại cùng một tool call | So (tool_name, args) với các bước trước — dễ nhất | Dừng, hoặc buộc agent thử tool khác |
| Hỏi lại thông tin đã có | Khó hơn — cần so ngữ nghĩa | Nhắc lại trong prompt những gì đã biết |
| Reasoning không tiến thêm | So độ tương đồng giữa các Thought liên tiếp | Dừng — đây là dấu hiệu model kẹt |
| Observation không đổi mà vẫn tiếp tục | So hash của observation | Dừng — gọi thêm cũng không có gì mới |

Lưu một `set` các `(tool_name, args)` đã gọi. Trước mỗi lần `run_tool`, kiểm tra. Nếu trùng, không gọi lại mà trả về cho model một thông báo: *"Bạn đã gọi tool này với đúng tham số đó ở bước trước, kết quả là […]. Hãy thử cách khác."*

**Vì sao cách này tốt hơn là dừng hẳn:** nó cho agent một cơ 
 hội tự sửa, đồng thời nhét lại thông tin nó đã có vào context. Nếu agent vẫn lặp lần nữa thì mới dừng. 
 Khoảng chục dòng code, và nó xử lý được dấu hiệu loop phổ biến nhất.

Giới hạn vòng lặp · timeout tool · trần token · retry có kiểm soát — bốn cái này là code.

**"Fallback sang human hoặc chatbot"** thì khác: nó là một 
 quyết định thiết kế sản phẩm, và nó đòi bạn *có sẵn* một đường thoát. Với **SmartCheck AI**, đường thoát đó là nút gọi lễ tân — và như [Ngày 25](track-3-day-25.html) chỉ ra, nó nên được xây *trước* các guardrail kỹ 
 thuật, vì nó có tác dụng ngay cả khi mọi thứ khác hỏng.

---

<!-- chiron-source-span: {"source_span_id":"6b2599a3-653d-5848-b542-1c10fe0e3496","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Live demo & debug","source_file":"slide-buoi-3.html"},"checksum":"fc6c344681cf9702c932b03b2096acc02bf9c4baffbc9e64dae4593a9b2265cc"} -->

## 06 Live demo & debug

Slide 32–35: kịch bản demo có chủ đích gây lỗi, hai tool tối thiểu, và checklist debug.

### Slide 32–34 Kịch bản demo — chú ý bước 4

> Trích slide 
>  "1. Định nghĩa 2 tools: get_weather và recommend_outfit 
>  2. Viết system prompt: agent chỉ được kết luận khi đã có dữ liệu thời tiết 
>  3. Chạy loop và đọc trace Thought / Action / Observation 
>  4. Cố tình tạo lỗi: tool timeout hoặc agent chọn sai outfit 
>  5. Debug: sửa prompt, sửa tool description, hoặc thêm safeguard" 
>  " Cho học viên thấy agent fail ở đâu và vì sao trace lại quan trọng hơn một final answer 
>  'trông có vẻ đúng'. "

Bước 4 — **cố tình tạo lỗi** — là bước dạy nhiều nhất, và nó là thói quen đáng mang đi 
 ngoài lớp học.

Đường xử lý lỗi là đường **ít được chạy nhất** trong mọi hệ thống. Nếu bạn chỉ chạy 
 các ca thành công, code xử lý lỗi có thể sai suốt nhiều tháng mà không ai biết — cho tới đúng ngày 
 cần nó.

Đây chính là *chaos testing* mà [Ngày 
 25](track-3-day-25.html) dạy có hệ thống, và câu chốt ở đó áp thẳng vào đây: **"biến giả định thành bằng chứng"**. Bạn *nghĩ* agent sẽ fallback khi tool 
 timeout; chỉ khi ép nó timeout bạn mới *biết*.

**Hai tool ở slide 34 rất tối giản** — `get_weather` trả dữ liệu cứng, `recommend_outfit` là ba nhánh if/else. Điều đáng chú ý: *tool thứ hai hoàn toàn không 
 cần LLM*. Nó là một hàm thuần tuý, và đó là lời nhắc rằng **tool của agent không nhất thiết phải thông minh** — chúng chỉ cần đáng tin và mô tả rõ.

recommend_outfit(temp_high, rain_probability)

hai số

get_weather

một dict

temperature_c: [27, 32]

rain_probability: 0.7

tự bóc

27

32

vì sao phải đọc args trong 
 trace

### Slide 35 Checklist debug — bốn chỗ nhìn, bốn chỗ sửa

> Trích slide 
>  " Nhìn vào trace trước: ■ Thought có đúng mục tiêu không? ■ Agent chọn đúng tool 
>  chưa? ■ Args truyền vào có hợp lệ không? ■ Observation có bị thiếu field quan trọng không?" 
>  " 4 nơi thường phải sửa: ■ Tool description quá mơ hồ ■ System prompt thiếu rule 
>  dừng ■ Không có safeguard cho retry / loop ■ Evaluation chỉ chấm final answer, không chấm trace" 
>  " Agent debugging gần với debugging distributed system hơn là chỉ prompt tuning. Ta phải 
>  nhìn cả model, tool, state, và orchestration. "

Bốn câu "nhìn trace" và bốn "nơi phải sửa" **ghép được thành một bảng chẩn đoán** — 
 và đó là thứ đáng in ra để cạnh máy khi làm lab:

| Triệu chứng trong trace | Nguyên nhân thường gặp | Sửa ở đâu |
| --- | --- | --- |
| Thought đi lạc mục tiêu ban đầu | System prompt không nhắc lại goal, hoặc context quá dài nên goal bị loãng | System prompt · cắt gọn observation |
| Chọn sai tool | Tool description mơ hồ — hai tool nghe giống nhau | Tool description (Ngày 4) |
| Args sai định dạng hoặc sai giá trị | Description không nêu rõ định dạng input | Tool description · thêm validate trong run_tool |
| Observation thiếu field agent cần | Tool trả về không đủ, hoặc bị cắt gọn quá tay | Sửa tool · xem lại chiến lược cắt observation |
| Chạy hết MAX_ITERATIONS | Thiếu rule dừng, hoặc kẹt loop | System prompt · safeguard phát hiện lặp |

*"Evaluation chỉ chấm final answer, không chấm trace"* — ba mục kia là chỗ bạn sửa code hoặc 
 prompt. Mục này là **chỗ sai trong cách bạn đánh giá**.

Nó được xếp ngang hàng với ba mục kia vì hậu quả tương đương: nếu bạn chỉ chấm câu trả lời cuối, 
 bạn sẽ *không phát hiện* ba loại lỗi đầu. Agent gọi sai tool ba lần rồi may mà ra đúng đáp án 
 vẫn được chấm "đạt".

Đây là mầm của một trong những ý chính của [Ngày 
 24](track-3-day-24.html): *trajectory correctness, tool selection accuracy, step efficiency* — ba metric đo đường 
 đi, không đo kết quả.

*"Agent debugging gần với debugging distributed system hơn là chỉ prompt tuning."*

Câu này nói rằng kỹ năng bạn cần **không phải kỹ năng viết prompt hay hơn**, mà là kỹ 
 năng của kỹ sư hệ thống: đọc log, khoanh vùng lỗi giữa nhiều thành phần, phân biệt lỗi của model với 
 lỗi của tool với lỗi của điều phối.

Và nó giải thích vì sao Track 3 dành nhiều ngày cho observability, circuit 
 breaker, eval — *những thứ nghe không giống AI chút nào*. Chúng không giống AI vì chúng không 
 phải vấn đề của AI; chúng là vấn đề của hệ phân tán, mà agent tình cờ cũng là một hệ phân tán.

---

<!-- chiron-source-span: {"source_span_id":"560ae9c6-42f4-59c1-8273-37f529fd430c","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Chatbot vs Agent & Lab","source_file":"slide-buoi-3.html"},"checksum":"0343d619a8d214999a1e058f534025605b11e04d9e62df8a12fb510416e91baa"} -->

## 07 Chatbot vs Agent & Lab

Slide 36–41: bảng năm khía cạnh, hybrid pattern, và cách chạy Lab 3.

### Slide 36–37 Khi nào chatbot thắng, khi nào agent thắng

> Trích slide 
>  " Tác vụ — Chatbot: FAQ, support đơn giản, nội dung 1 lượt. Agent: Booking, 
>  research, coding, data analysis nhiều bước. 
>  Tốc độ — Chatbot: nhanh, ít round-trip. Agent: chậm hơn do loop và tool calls. 
>  Cost — Chatbot: thấp hơn, predictable hơn. Agent: cao hơn nhưng đổi lại xử 
>  lý được bài toán khó hơn. 
>  Kiểm soát — Chatbot: dễ hơn, ít state. Agent: khó hơn vì cần orchestration và eval 
>  theo trace. 
>  UX — Chatbot: phản hồi nhanh, đơn giản. Agent: tạo cảm giác 'làm việc giúp bạn' 
>  nếu làm tốt." 
>  " Bắt đầu bằng chatbot là lựa chọn mặc định tốt "

Hai chữ trong bảng đáng để ý hơn phần còn lại, vì chúng là hai cảnh báo được cài kín đáo:

**① Cost: chatbot "thấp hơn, *predictable hơn* ".** Chữ thứ hai quan trọng hơn 
 chữ thứ nhất. Chi phí chatbot tính được trước: một lượt gọi, biết trước độ dài. Chi phí agent *phụ thuộc dữ liệu* — một câu hỏi khó có thể chạy 8 vòng lặp, câu dễ chạy 2 vòng.

Nghĩa là bạn không lập ngân sách được bằng phép nhân đơn giản, và một thay đổi nhỏ trong prompt có 
 thể làm chi phí trung bình nhảy vọt. Đây là lý do [trần token](#s30) nằm trong danh sách 
 guardrail bắt buộc.

**② UX: agent tạo cảm giác "làm việc giúp bạn" — *nếu làm 
 tốt*.** Vế điều kiện này thừa nhận một điều: agent làm *không* tốt thì UX **tệ hơn hẳn** chatbot. Người dùng chờ 15 giây để nhận một câu trả lời sai, sau khi nhìn 
 màn hình "đang xử lý" — trải nghiệm đó tệ hơn nhiều so với nhận câu trả lời sai trong 2 giây. Agent 
 đặt cược trải nghiệm vào chất lượng, và nó là canh bạc hai chiều.

slide 13

slide 15

về

Rules of ML

Ngày 2

### Slide 38 Hybrid pattern — kết luận thực dụng nhất của bài

> Trích slide 
>  "User Query → Intent / Triage → simple → Simple Chatbot path · multi-step → 
>  Agent path · fallback → Human / Escalation" 
>  " Không cần chọn một phe. Thiết kế tốt thường là: triage nhanh, câu đơn giản đi chatbot 
>  path, câu phức tạp mới mở agent loop. "

_Sơ đồ: Mẫu hybrid phân loại yêu cầu rồi rẽ sang chatbot, agent hoặc người thật - Yêu cầu của người dùng đi vào bước phân loại nhanh. Từ đó rẽ ba nhánh: câu đơn giản đi sang nhánh chatbot, nhanh và rẻ; câu nhiều bước đi sang nhánh agent, chậm và đắt hơn nhưng xử lý được bài khó; và nhánh dự phòng chuyển sang người thật khi hai nhánh kia không xử lý được. Bên dưới ghi chú rằng phần lớn lưu lượng thường đi nhánh chatbot, nên chi phí trung bình gần với chatbot chứ không phải với agent._

Hình 3 — Hybrid pattern (slide 38).

routing

slide 15

slide 30

Phân bố độ khó của yêu cầu người dùng hầu như luôn lệch: **rất nhiều câu dễ, ít câu khó**. 
 Với một kiosk khách sạn, "wifi mật khẩu gì" nhiều gấp bội "tôi cần đổi phòng vì điều hoà hỏng và có 
 con nhỏ".

Nếu đẩy tất cả qua agent loop, bạn trả giá agent cho *toàn bộ* lưu lượng để phục vụ một 
 thiểu số cần nó. Nếu đẩy tất cả qua chatbot, thiểu số đó không được phục vụ.

**Cái giá của hybrid** nằm ở bước triage: phân loại sai thì 
 câu khó rơi vào chatbot path (trả lời hời hợt) hoặc câu dễ rơi vào agent loop (đắt và chậm vô ích). 
 Đây đúng là dòng "mất gì" của pattern *Routing* ở [Ngày 2](slide-buoi-2.html): *"cần phân loại đúng ngay từ đầu"*. Và nó cũng là lý do nhánh thứ ba — người thật — phải tồn 
 tại: nó bắt cả những ca mà triage đoán sai.

triage

khung để đo

bao nhiêu phần trăm lưu lượng đi mỗi nhánh? Triage phân loại đúng bao nhiêu phần 
 trăm? Và chi phí trung bình mỗi lượt là bao nhiêu?

### Slide 39–41 Lab 3 — so sánh trực tiếp

> Trích slide 
>  "1. Chọn lại use case từ Ngày 2 hoặc một use case tương đương 2. Build chatbot baseline 
>  3. Nâng cấp thành ReAct agent có ít nhất 1–2 tools 4. Chạy 5 test cases giống nhau trên cả 
>  hai hệ thống 5. Vẽ flowchart và ghi nhận nơi agent thực sự tạo thêm giá trị " 
>  " Nhờ AI generate scaffolding code, nhưng nhóm phải tự sửa system prompt, tool description, và 
>  điều kiện dừng. " 
>  " Deliverable: chatbot + agent + 5 test cases + 1 trace + 1 flowchart. 
>  Bonus: thêm fallback path hoặc human escalation. Thời gian: 150 phút"

Bước 1 — *"chọn lại use case từ Ngày 2"* — làm cho hai bài học nối liền: bạn đã có Problem 
 Statement, giờ bạn kiểm chứng ô *Mức chọn* bằng thực nghiệm thay vì bằng lập luận.

| Thứ phải tự sửa | Vì sao AI không làm hộ được |
| --- | --- |
| System prompt | Nó mã hoá quy tắc nghiệp vụ của bạn — AI không biết bài toán của bạn cấm điều gì |
| Tool description | Nó mô tả tool thật của bạn, kể cả các chế độ hỏng mà chỉ bạn biết |
| Điều kiện dừng | Nó là quyết định đánh đổi: dừng sớm thì trả lời thiếu, dừng muộn thì tốn tiền |

Ba thứ này cũng đúng là ba trong [bốn nơi phải sửa khi 
 debug](#s35). Không phải trùng hợp: chúng là chỗ chứa *tri thức về bài toán*, còn scaffolding code 
 chỉ chứa tri thức về framework.

"Ghi nhận nơi agent thực sự tạo thêm giá trị"

chỉ ra test case nào và nhờ điều gì

"Agent thắng ở test case 3 và 5 — hai ca cần dữ liệu thật mà 
 chatbot không truy cập được. Ở ba ca còn lại, agent cho cùng kết quả nhưng chậm hơn 4 lần và tốn gấp 
 3 lần token. Kết luận: nên dùng hybrid, tách hai loại ca đó ra agent path."

Mức chọn

---

<!-- chiron-source-span: {"source_span_id":"c5e94fca-93b0-5049-a208-db02a23375c0","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Tổng kết","source_file":"slide-buoi-3.html"},"checksum":"2d914bfcfd4157490817dcd27f48317d9b3c0135dcfa5b84f38961bfdca07f6b"} -->

## 08 Tổng kết

Slide 42–46: bốn ý chốt, bài tập về nhà, và ba nguồn tham khảo.

### Slide 42–44 Bốn ý chốt và tài liệu

> Trích slide 
>  "1 Agent không phải 'chatbot thông minh hơn'; agent = LLM + reasoning + tools + 
>  memory/state. 2 ReAct là pattern dễ học nhất để biến LLM thành hệ thống biết hành 
>  động và dễ debug. 3 Chỉ dùng agent khi bài toán có multi-step reasoning, tool use, 
>  dynamic decisions, long horizon. 4 Trong production, guardrails, trace, và evaluation quan 
>  trọng không kém model quality " 
>  " Bài tập: Đọc lại trace lab hôm nay và tìm 1 chỗ agent ra quyết định chưa tối ưu · 
>  Thử viết lại tool description theo hướng rõ input, output, và failure mode hơn" 
>  " Tham khảo: Yao et al. ReAct: Synergizing Reasoning and Acting in Language 
>  Models (arXiv:2210.03629) · Anthropic Building effective agents · LangGraph docs"

Ý số 1 là ý chống hiểu lầm quan trọng nhất, và công thức của nó đáng đọc kỹ: **agent = LLM + reasoning + tools + memory/state**. Chú ý *LLM chỉ là số hạng đầu 
 tiên*.

| Thiếu | Bạn còn lại cái gì |
| --- | --- |
| Thiếu tools | Agent rỗng — chỉ suy nghĩ, không hành động được (anti-pattern slide 13) |
| Thiếu reasoning (lộ trình cố định) | Workflow / prompt chaining — không phải agent |
| Thiếu memory/state | Mỗi vòng lặp quên vòng trước ⇒ không tích luỹ được, dễ lặp lại tool call |
| Thiếu LLM | Một chương trình có luật — hoàn toàn hợp lệ, và thường là lựa chọn đúng |

Dòng cuối không phải đùa. Rất nhiều "agent" trong thực tế nên là một 
 script — đó là toàn bộ nội dung [anti-pattern ở slide 13](#s13) và [cây quyết định Ngày 2](slide-buoi-2.html).

"Trong production, guardrails, trace, và evaluation quan trọng không kém model quality."

guardrails

Ngày 24

trace

Ngày 25

evaluation

xây

chạy được trong thực tế

#### Ô kiểm tra — Chương 5, 6 & 7

Trả lời thành tiếng trước khi mở đáp án.

**1.** Trong pseudocode 15 dòng, dòng nào đảm bảo agent không chạy mãi, và dòng nào 
 quyết định câu trả lời cuối cùng người dùng nhận được khi mọi thứ hỏng? Nhớ + Hiểu

#### Đáp án

**Chặn chạy mãi:** `for step in range(MAX_ITERATIONS)` — trần cứng số 
 vòng lặp.

**Câu trả lời khi mọi thứ hỏng:** `return "Stopped: max iterations 
 reached"` — dòng cuối, nằm *ngoài* vòng lặp.

**Vì sao dòng cuối quan trọng hơn vẻ ngoài của nó:** nó là thứ đảm bảo hàm luôn trả 
 về một cái gì đó. Bỏ nó thì hàm trả `None` và lỗi nổ ở chỗ khác; ném exception thì người 
 dùng nhận trang lỗi.

**Làm cho đúng:** trả về câu *hữu ích cho người dùng* — "tôi chưa hoàn tất 
 được, đây là những gì đã tìm được, bạn có muốn chuyển sang nhân viên hỗ trợ không?" Đây chính là *dead-letter* và *fallback* mà Ngày 23 và Ngày 25 dạy có hệ thống.

**2.** Rule *"Never invent tool results"* trong system prompt đủ để chặn 
 agent bịa observation chưa? Đánh giá

#### Đáp án

**Chưa — đó là một thoả thuận trong prompt, không phải cưỡng chế.** Model có thể vi 
 phạm, và khi vi phạm thì trace *trông hoàn toàn hợp lệ*: có Thought, có Action, có 
 Observation — chỉ là dữ liệu bịa.

**Cách chặn thật nằm ở kiến trúc:** vòng lặp phải *tự chèn* observation từ 
 kết quả `run_tool` vào messages, chứ không để model tự viết. Pseudocode slide 27 làm đúng 
 vậy — `tool_message(output.name, result)` được thêm bởi **code**, không phải 
 bởi model.

**Nguyên tắc chung:** prompt giảm xác suất, kiến trúc mới đảm bảo. Đây là cùng bài 
 học với Ngày 24 — *"system prompt alone không đủ"* (vụ Bing Sydney).

**Thêm một lớp nữa nếu cần:** kiểm tra định dạng output — nếu model trả về text 
 trông giống Observation mà không đi kèm một tool call hợp lệ, từ chối và yêu cầu lại.

**3.** Sau lab, bạn thấy agent thắng ở 2/5 test case, còn 3 ca kia cho cùng kết quả 
 nhưng chậm hơn 4 lần. Kết luận và đề xuất? Áp dụng

#### Đáp án

**Kết luận: hybrid pattern — không chọn một phe.**

Đẩy toàn bộ lưu lượng qua agent nghĩa là trả giá agent (chậm 4×, đắt hơn) cho *cả 3 ca mà 
 chatbot đã đủ*. Đẩy toàn bộ qua chatbot thì 2 ca kia không được phục vụ.

**Đề xuất cụ thể:** thêm bước *triage* ở đầu — phân loại yêu cầu, câu đơn 
 giản đi chatbot path, câu cần dữ liệu thật hoặc nhiều bước mới mở agent loop. Cộng nhánh thứ ba: 
 chuyển người thật khi cả hai không xử lý được.

**Phải nói rõ agent thắng NHỜ ĐIỀU GÌ**, không chỉ nói "thắng". Ví dụ: "hai ca đó 
 cần dữ liệu thật mà chatbot không truy cập được" — đó là *tool use*, tiêu chí ② của Agentic 
 Fit. Biết lý do thì mới thiết kế được luật triage.

**Cái giá của hybrid phải nêu:** bước triage có thể phân loại sai — câu khó rơi vào 
 chatbot path, câu dễ rơi vào agent loop. Nên cần đo *độ chính xác của triage* như một metric 
 riêng, và giữ nhánh escalation để bắt các ca đoán sai.

---

<!-- chiron-source-span: {"source_span_id":"0489f5ed-6588-5281-a665-9e05736f5909","locator":{"kind":"html_section","section_id":"ladder","order":11,"heading":"▤ Luyện kỹ năng cốt lõi: quyết định cấp độ và đọc trace","source_file":"slide-buoi-3.html"},"checksum":"19062ede57b2646db0b56107f120141171c23cff18e8033408f7732757594ebd"} -->

## ▤ Luyện kỹ năng cốt lõi: quyết định cấp độ và đọc trace

Ba bài giảm dần giàn giáo. Làm đúng thứ tự.

① Lộ trình xử lý có viết trước được không?

② Có tool nào để gọi không?

③ Chấm Agentic Fit

④ Nếu là agent: guardrail nào, và trace sẽ nhìn gì?

#### "Làm một agent tra cứu chính sách nội bộ cho nhân viên"

Đọc cách *lập luận*, không chỉ đáp án.

1. Lộ trình có viết trước được không? Có. Nhận câu hỏi → tìm đoạn chính sách liên 
 quan → trả lời kèm trích dẫn. Ba bước cố định, bước sau không phụ thuộc nội dung kết quả bước 
 trước — chỉ phụ thuộc việc có tìm thấy hay không. 
 Cách nhận ra: nếu bạn vẽ được sơ đồ luồng mà không có ô hình thoi "tuỳ kết quả thì rẽ đâu", 
 lộ trình là cố định.
2. Có tool không? Có — tìm kiếm tài liệu. Nên không rơi vào anti-pattern "agent 
 rỗng". Nhưng chú ý: có tool không có nghĩa là cần agent. Một chatbot có retrieval 
 (RAG) cũng gọi tool, mà vẫn là chatbot vì không có vòng lặp quyết định.
3. Chấm Agentic Fit: Reasoning 2 (tìm rồi trả lời, không nhiều 
 bước phụ thuộc) · Tool use 3 (một tool, dùng mọi lần) · Dynamic decision 
 1 (không rẽ nhánh theo quan sát) · Long horizon 1. 
 Tổng ba tiêu chí = 6/15 ⇒ vùng "augmented chatbot", không phải agent. 
 Đối chiếu slide 12: rất gần ca "FAQ nội bộ HR" (3 điểm).
4. Kết luận và cách nói: đây là chatbot có retrieval — 
 pattern Augmented LLM, nấc đầu tiên trong thang Anthropic. Rẻ hơn, nhanh hơn, dễ đánh 
 giá hơn (chấm được bằng câu trả lời và trích dẫn, không cần eval theo trace). 
 Điều kiện đổi ý: nếu về sau cần "so sánh chính sách qua các phiên bản" hay "kiểm tra trường 
 hợp của nhân viên này có thoả điều kiện không" — tiêu chí ③ tăng lên, và lúc đó mới xét lại.

Câu chốt kiểu vấn đáp "Lộ trình ba bước viết trước được và không rẽ nhánh theo quan sát, nên đây là chatbot có retrieval chứ 
 không phải agent — chấm Agentic Fit ra 6/15. Em chọn Augmented LLM: rẻ hơn, nhanh hơn, và đánh giá 
 được bằng câu trả lời kèm trích dẫn thay vì phải eval theo trace. Em sẽ xét lại nếu xuất hiện yêu cầu 
 so sánh nhiều phiên bản chính sách, vì lúc đó bước sau mới phụ thuộc kết quả bước trước."

#### Agent đặt lịch họp của bạn chạy hết MAX_ITERATIONS ở 30% số yêu cầu

Hai bước đầu cho sẵn. Hai bước sau tự viết rồi mới mở.

1. 30% là tỷ lệ rất cao — đây không phải ca biên. Chạm trần vòng lặp nghĩa là agent 
 không đạt điều kiện dừng, chứ không phải nó thất bại ở một tool. Hai khả năng: kẹt loop, hoặc điều 
 kiện dừng không bao giờ thoả.
2. Việc đầu tiên là đọc trace, không phải nâng MAX_ITERATIONS. Nâng trần chỉ làm 
 agent chạy lâu hơn rồi vẫn hỏng, và tốn gấp đôi. Đây là phản xạ sai phổ biến nhất.
3. ③ Bốn dấu hiệu loop ở slide 30 — bạn kiểm từng cái thế nào trong trace, và 
 mỗi dấu hiệu chỉ về nguyên nhân gì?
4. ④ Giả sử xác định được agent gọi check_calendar lặp lại với 
 cùng tham số. Sửa ở đâu, và thêm safeguard gì?

#### Đáp án hai bước còn lại

**③ Bốn dấu hiệu và cách kiểm:**

| Dấu hiệu | Kiểm bằng cách | Chỉ về nguyên nhân |
| --- | --- | --- |
| Lặp cùng tool call | So (tool, args) giữa các bước — dễ nhất | Tool description mơ hồ, hoặc agent không "thấy" observation |
| Hỏi lại thông tin đã có | Đọc Thought xem có nhắc lại câu hỏi đã trả lời | Context quá dài, thông tin bị loãng |
| Reasoning không tiến thêm | So các Thought liên tiếp — có gần trùng nhau không | System prompt thiếu rule dừng |
| Observation không đổi mà vẫn tiếp tục | So hash observation | Agent không hiểu observation đã đủ để kết luận |

**④ Sửa ở ba chỗ, theo thứ tự rẻ dần:**

**① Tool description** — nêu rõ *output* và *error mode*. Nếu `check_calendar` trả về mảng rỗng khi không có lịch trống, mà description không nói, agent 
 sẽ tưởng mình gọi sai và gọi lại. Thêm một dòng: *"Trả về mảng rỗng nếu không có khung giờ trống 
 trong khoảng đã cho — đây là kết quả hợp lệ, không phải lỗi."*

**② System prompt** — thêm rule dừng tường minh: *"Nếu đã kiểm tra lịch và không có 
 khung trống, hãy báo lại cho người dùng và đề xuất khoảng thời gian khác. Không gọi lại cùng một tool 
 với cùng tham số."*

**③ Safeguard trong code** — lưu `set` các `(tool_name, args)` đã gọi; nếu trùng thì *không* gọi lại mà trả về cho model một thông báo: *"Bạn đã gọi tool 
 này với đúng tham số đó ở bước trước, kết quả là […]. Hãy thử cách khác."*

**Vì sao cách ③ tốt hơn là dừng hẳn:** nó cho agent một cơ hội tự sửa và nhét lại 
 thông tin đã có vào context. Lặp lần nữa thì mới dừng. Khoảng chục dòng code, xử lý được dấu hiệu loop 
 phổ biến nhất.

**Và đừng quên nhánh cuối:** khi thật sự chạm trần, câu trả về phải hữu ích cho người 
 dùng — không phải `"Stopped: max iterations reached"`.

#### Chấm Agentic Fit cho SmartCheck AI và quyết định kiến trúc

Không có gợi ý. Chấm rồi so với [mục áp dụng](#apply).

1. Bối cảnh: kiosk check-in khách sạn. Luồng hiện tại: nhận yêu cầu → phân loại ý 
 định → định tuyến (tra đặt phòng / trả lời thông tin chung / cần lễ tân) → gọi tool nếu cần → 
 cổng phê duyệt cho hành động rủi ro → trả lời.
2. Chấm bốn tiêu chí, mỗi tiêu chí kèm một câu lý do. Đừng chấm theo cảm 
 giác "hệ này phức tạp nên chắc điểm cao".
3. Đối chiếu với kết luận của Ngày 2 (cây quyết định 
 cho ra Workflow). Hai khung có nhất quán không? Nếu lệch, khung nào đúng hơn và vì sao?
4. Nếu giữ kiến trúc hiện tại, ba guardrail nào bạn cần có, và trace của bạn nên ghi 
 gì để debug được?

"có nhiều bước"

"bước sau phụ thuộc kết quả quan sát của 
 bước trước"

một

routing

---

<!-- chiron-source-span: {"source_span_id":"6555c192-c1b7-570b-b465-32099d70a418","locator":{"kind":"html_section","section_id":"misc","order":12,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"slide-buoi-3.html"},"checksum":"3d3ee8071c6adb9a9f20f5f21e4a7df50887b4ab575f8b250d7f7cc615c6574b"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Mỗi thẻ: niềm tin phổ biến, lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng.

*Vì sao nghe hợp lý:* tool calling là thứ dễ thấy nhất của agent, và tài liệu marketing hay 
 dùng "AI agent" cho bất cứ thứ gì gọi được API.

Định nghĩa hoạt động ở slide 7 có **bốn động từ**: *quyết định → hành động → 
 quan sát → lặp lại*. Gọi tool mới chỉ là "hành động".

Ranh giới thật: **lộ trình xử lý có viết trước được không?** Một hệ gọi LLM sáu lần 
 theo trình tự cố định vẫn là *prompt chaining*. Một hệ gọi hai lần nhưng lần hai phụ thuộc kết 
 quả lần một — đã là agent.

[Slide 7](#s7) · [Hình 1](#f1) — đường đứt đánh dấu ranh giới.

*Vì sao nghe hợp lý:* spectrum ở slide 7 vẽ từ trái sang phải, trông như một lộ trình nâng 
 cấp. Và agent làm được nhiều hơn thật.

Bảng ở slide 8 có **sáu tiêu chí**, và hai tiêu chí cuối lật ngược: *Cost* — 
 agent cao hơn và *kém dự đoán hơn*; *Risk* — agent kế thừa toàn bộ rủi ro của chatbot **rồi cộng thêm** tool misuse và loop.

Bốn thanh trong Hình 1 đều tăng cùng chiều — kể cả thanh rủi ro và chi phí. **Không có mức nào "tốt hơn", chỉ có mức phù hợp hơn.**

[Slide 8](#s7) — hai dòng Cost và Risk · [Slide 37](#s37).

*Vì sao nghe hợp lý:* "multi-step reasoning" là tiêu chí đầu tiên trong Agentic Fit, nên 
 trông như tiêu chí quan trọng nhất.

Nhiều bước *cố định* = prompt chaining, vẫn là workflow. Ca "tóm tắt hợp đồng" ở slide 12 
 có Reasoning 3 nhưng tổng chỉ 7 ⇒ không cần agent.

**Tiêu chí quyết định là ③ — dynamic decision:** bước tiếp theo có phụ thuộc kết quả *vừa quan sát* không. Đặt Reasoning = 5 mà Dynamic = 1 thì tổng vẫn dưới ngưỡng — 
 thang điểm được thiết kế để một tiêu chí đơn lẻ không quyết định được.

[Mô-đun Agentic Fit](#m-fit) — thử Reasoning 5 / Tool 1 / Dynamic 1.

*Vì sao nghe hợp lý:* với mọi phần mềm khác, đầu ra đúng là tiêu chí đủ. Và câu trả lời cuối 
 là thứ người dùng thấy.

Một agent gọi cùng tool ba lần với cùng tham số rồi *may mà* ra đúng đáp án là một agent 
 hỏng: tốn gấp ba, chậm gấp ba, và lần sau có thể chạm `MAX_ITERATIONS`.

Slide 25 xếp *"cần eval theo trace, không chỉ final answer"* vào phần **giới hạn** — vì đó là chi phí vận hành thật. Và slide 35 xếp *"evaluation chỉ chấm final answer"* vào **bốn nơi phải sửa khi debug**, ngang hàng với lỗi code.

[Slide 25](#s23) · [Slide 35](#s35) · nối tới [Ngày 24](track-3-day-24.html) — "agent quality = trajectory quality".

*Vì sao nghe hợp lý:* nó nằm ngay trong system prompt mẫu của slide 28, viết rõ ràng, và 
 model thường tuân thủ.

Prompt là **thoả thuận**, không phải **cưỡng chế**. Khi model vi phạm, 
 trace *trông hoàn toàn hợp lệ* — có đủ Thought, Action, Observation — chỉ là dữ liệu bịa. 
 Đây là loại lỗi khó phát hiện nhất.

**Chặn thật bằng kiến trúc:** vòng lặp phải tự chèn observation từ kết quả `run_tool` vào messages. Pseudocode slide 27 làm đúng vậy — *code* thêm `tool_message`, không phải model.

[Slide 27](#s27) so với [slide 28](#s28) · nối tới [Ngày 24](track-3-day-24.html) — "system prompt alone không đủ".

*Vì sao nghe hợp lý:* cả bài học được đóng khung như một so sánh, và deliverable bắt xây cả 
 hai để "chọn".

Slide 38 nói thẳng: **"Không cần chọn một phe."** Thiết kế tốt là *triage nhanh* → câu đơn giản đi chatbot path, câu phức tạp mới mở agent loop, cộng nhánh thứ 
 ba sang người thật.

Vì phân bố độ khó luôn lệch — rất nhiều câu dễ, ít câu khó — nên **chi phí trung bình của hybrid gần với chatbot** chứ không gần agent.

Cái giá: bước triage phải đúng, và phải đo độ chính xác của nó như một metric riêng.

[Hình 3](#f3) · [Slide 38](#s38) · đối chiếu pattern *Routing* ở [Ngày 2](slide-buoi-2.html).

---

<!-- chiron-source-span: {"source_span_id":"bcf0b791-bd19-521d-b24b-31b6a89fd6a8","locator":{"kind":"html_section","section_id":"apply","order":13,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-buoi-3.html"},"checksum":"14e48b4eaf7798a1c7dff7ff0ca7653b56765378a41b842cd8f4c5115d1176d0"} -->

## ◆ Áp dụng vào SmartCheck AI

Chấm Agentic Fit, đối chiếu với kết luận Ngày 2, và ba việc làm được ngay.

### Chấm Agentic Fit — kèm lý do từng điểm

| Tiêu chí | Điểm | Lý do |
| --- | --- | --- |
| ① Multi-step reasoning | 3 /5 | Luồng check-in có nhiều bước (phân loại → tra cứu → xác nhận → trả lời), nhưng phần lớn là chuỗi cố định. Bước sau cần kết quả có/không của bước trước, chứ không cần nội dung để quyết đi đâu. |
| ② Tool interaction | 4 /5 | Có tool thật và cần thiết: tra đặt phòng, kiểm phòng trống, cập nhật trạng thái. Đây là tiêu chí cao nhất — model không thể tự biết dữ liệu này. |
| ③ Dynamic decision | 2 /5 | Tiêu chí quyết định, và nó thấp. Chỉ có một chỗ rẽ thật sự theo quan sát: kết quả phân loại ý định. Đó là routing — nhánh viết trước được, không phải model tự nghĩ ra lộ trình. |
| ④ Long horizon | 1 /5 | Mỗi lượt check-in là một phiên độc lập, kết thúc trong vài phút. Không có mục tiêu kéo dài qua nhiều phiên. |

Cộng ba tiêu chí như ma trận slide 12: 3 + 4 + 2 = **9**. Cộng cả bốn: 10/20, cũng dưới 
 ngưỡng chuẩn hoá 14,7.

**Và điều này khớp với [Ngày 2](slide-buoi-2.html):** cây quyết định năm câu ở đó cũng cho ra *Workflow* (câu ③ "quy trình có cố định" = có, 
 câu ④ "cần tự thích ứng" = không). Hai khung độc lập, cùng một kết luận — đó là tín hiệu tốt cho thấy 
 kết luận đáng tin, không phải do cách chấm.

### Vậy hệ hiện tại là gì, theo từ vựng của bài này?

| Thành phần trong SmartCheck AI | Tên gọi ở Ngày 3 |
| --- | --- |
| Node phân loại ý định ở đầu luồng | Triage — bước đầu của hybrid pattern ( Hình 3 ) |
| Định tuyến theo loại yêu cầu | Routing — pattern thứ ba trong thang Anthropic |
| Gọi tool tra đặt phòng | Augmented LLM — pattern thứ nhất |
| Cổng phê duyệt trước hành động rủi ro | Human-in-the-loop — guardrail thứ năm ở slide 30 |
| Retry hữu hạn + dead-letter | Guardrail chống loop — đúng thứ slide 30 đòi |
| Nút gọi lễ tân | Nhánh escalation — nhánh thứ ba của hybrid |

Sáu thành phần trên ghép lại chính là [Hình 3](#f3): triage → ba nhánh (chatbot path, 
 tool path, người thật). Không có chỗ nào model *tự quyết lộ trình nhiều bước*, nên theo định 
 nghĩa slide 51 của Ngày 2 và slide 7 của bài này, nó không phải agent.

**Giá trị của việc gọi đúng tên:** nó cho bạn biết *nên đánh giá nó bằng gì*. Workflow đánh giá được bằng độ chính xác từng bước (phân loại đúng 
 bao nhiêu%, tool trả đúng không) — *không* cần eval theo trace phức tạp như agent. Đó là tin 
 tốt: rẻ hơn và làm được ngay.

### Ba việc làm được ngay tuần này

| # | Việc | Công sức | Đổi lại |
| --- | --- | --- | --- |
| 1 | Ghi trace từng bước vào log: bước nào, tool nào, args gì, observation ra sao | ~1–2 giờ | Đây là điều kiện để debug được. Slide 35 nói "nhìn vào trace trước" — không có trace thì mọi việc sau đều là đoán |
| 2 | Đo tỷ lệ ba nhánh: bao nhiêu% lưu lượng đi thông tin chung, bao nhiêu% cần tra cứu, bao nhiêu% chuyển lễ tân | ~nửa buổi (nếu đã có việc 1) | Ba con số này nói cho bạn biết thiết kế hybrid có đúng không — và nhánh nào đáng tối ưu trước |
| 3 | Đo độ chính xác của bước triage trên 100 yêu cầu thật | ~1 buổi xem tay | Đây là metric quan trọng nhất của hybrid. Triage sai đẩy câu khó vào nhánh sai — và không có gì bắt được nếu không đo |

điểm hỏng đơn

Routing

Ngày 2

"cần phân loại đúng ngay từ đầu"

---

<!-- chiron-source-span: {"source_span_id":"b7fa8d11-16da-51b5-be30-01e5e3ce6331","locator":{"kind":"html_section","section_id":"numbers","order":14,"heading":"! Con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"slide-buoi-3.html"},"checksum":"e58dd8274f7b395c67b80d4eb65fa9b7f519ef322efe296e3faae9ea8d84b4a8"} -->

## ! Con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài này ít số. Điểm đáng chú ý nhất không phải một con số sai mà là một *khung điểm không nhất quán giữa hai slide*.

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| Ma trận Agentic Fit — 4 tiêu chí nhưng chỉ cộng 3 | 11 vs 12 | Không nhất quán — xem ô cảnh báo bên dưới | Cộng ba tiêu chí (reasoning + tool + dynamic) khi dùng ngưỡng gốc |
| Ngưỡng 0–5 / 6–10 / 11+ | 12 | Quy ước dạy học, không có nguồn | Dùng làm điểm khởi đầu cho thảo luận. Nó không phải kết quả nghiên cứu, và slide không giải thích ngưỡng đến từ đâu |
| Điểm năm ca mẫu (FAQ 3 · Hợp đồng 7 · Booking 13 · Research 12 · Code 14) | 12 | Cộng đúng — đã kiểm cả năm dòng | Dùng làm mốc so sánh khi chấm bài toán của bạn. Đây là giá trị lớn nhất của bảng |
| "MAX_ITERATIONS", "loop 3–5 bước là đã quá chậm" | 13, 27 | Không có giá trị cụ thể | Slide không nói nên đặt trần bao nhiêu — đúng, vì nó phụ thuộc bài toán. Tự đo: chạy 50 ca thật, xem phân bố số vòng lặp, đặt trần ở phân vị 95 rồi cộng biên |
| Trace mẫu: VietJet 1.75M, Vietnam Airlines 1.95M, mưa 70% | 23–24 | Dữ liệu minh hoạ | Không phải giá vé thật. Dùng để đọc cấu trúc trace |
| Code demo: temperature_c: [27, 32], rain_probability: 0.7 | 34 | Hàm trả dữ liệu cứng | Cố ý — để demo chạy được offline. Chú ý nó tạo ra một bước suy luận thật: agent phải tự bóc 32 từ mảng |
| Điểm SmartCheck AI ở mục áp dụng (3, 4, 2, 1) | — | Nhận định của tài liệu này | Có kèm lý do từng điểm. Bạn nên tự chấm rồi so — nếu lệch, chỗ lệch là chỗ đáng bàn |
| Ngưỡng chuẩn hoá 8,0 và 14,7 trong mô-đun | — | Phép quy đổi của tài liệu này (× 20/15) | Không có trên slide. Dùng để so công bằng khi cộng cả bốn tiêu chí |

Slide 11 nêu bốn tiêu chí: Multi-step Reasoning · Tool Interaction · Dynamic Decision · **Long Horizon**. Nhưng ma trận ở slide 12 chỉ có ba cột — *Long Horizon không xuất 
 hiện*.

Kiểm lại từng tổng đều khớp với phép cộng ba: FAQ 1+1+1 = 3 · Hợp đồng 3+2+2 = 7 · 
 Booking 4+5+4 = 13 · Research 4+4+4 = 12 · Code assistant 5+5+4 = 14. Cả năm dòng đều đúng.

**Hệ quả thực hành:** ngưỡng *0–5 / 6–10 / 11+* được thiết 
 kế cho thang tối đa **15**, không phải 20. Nếu bạn cộng cả bốn tiêu chí rồi so với ngưỡng 
 đó, bạn sẽ đẩy mọi bài toán lên cao hơn thực tế — và kết luận "cần agent" nhiều hơn mức đáng. [Mô-đun](#m-fit) tính cả hai cách để bạn thấy khác biệt.

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực 
 tế đã chạy."

đừng ghi "hệ thống của tôi là agent" nếu chưa 
 chấm Agentic Fit

---

<!-- chiron-source-span: {"source_span_id":"8f62dbf7-bb48-5d34-bf2a-100bbdbe4524","locator":{"kind":"html_section","section_id":"cheat","order":15,"heading":"✓ Cheat sheet ôn thi","source_file":"slide-buoi-3.html"},"checksum":"3a48bc188043e094065bddfeefbf8a6af22e1a0ebfbd0aa07e57638cd6965418"} -->

## ✓ Cheat sheet ôn thi

Nén 46 slide xuống một trang.

### Định nghĩa và ranh giới

**Agent = LLM + reasoning + tools + memory/state.** Định nghĩa hoạt động (slide 7): 
 agent xuất hiện khi hệ thống phải *quyết định → hành động → quan sát → lặp lại*. Thiếu động từ 
 nào cũng chưa phải agent.

**Ranh giới workflow ↔ agent:** *"lộ trình xử lý có viết trước được không?"* Viết trước được = workflow (code điều phối). Không = agent (model điều phối).

**Spectrum 4 mức:** Rule-based Bot → LLM Chatbot → *[ranh giới]* → Reactive Agent → Autonomous Agent. Bốn thứ tăng cùng chiều: thích nghi, tool use, 
 memory, **và rủi ro + chi phí**.

### Agentic Fit — bốn tiêu chí, ba cột chấm

| Tiêu chí | Câu hỏi kiểm tra |
| --- | --- |
| ① Multi-step reasoning | Mấy bước? Bước sau cần kết quả bước trước không? |
| ② Tool interaction | Có dữ liệu nào model không thể tự biết không? |
| ③ Dynamic decision | Lộ trình viết trước được không? — tiêu chí quyết định |
| ④ Long horizon | Mục tiêu kéo dài qua nhiều phiên / state không? |

**Ngưỡng (cộng ba tiêu chí ①②③, tối đa 15):** *0–5* chatbot/rule đủ · *6–10* augmented chatbot · *11+* agent đáng thử. 
 **Mốc so sánh:** FAQ nội bộ 3 · Tóm tắt hợp đồng 7 · Research agent 12 · 
 Booking assistant 13 · Code assistant có test loop 14.

### ReAct và guardrail

**Vòng lặp:** Thought (còn thiếu gì?) → Action (tool + args) → Observation (kết quả) 
 → lặp lại cho tới khi đủ hoặc chạm điều kiện dừng.

**Vì sao ReAct được dạy đầu tiên:** không phải vì câu trả lời tốt hơn, mà vì *lý do hành động lộ ra ngoài* nên debug được và đánh giá được.

**Năm guardrail (slide 30):** giới hạn vòng lặp · timeout mỗi tool · trần token/chi phí · 
 retry có kiểm soát · fallback sang người hoặc chatbot.

**Bốn dấu hiệu loop:** lặp cùng tool call · hỏi lại thông tin đã 
 có · reasoning không tiến thêm · observation không đổi mà vẫn tiếp tục. *Dấu hiệu thứ nhất phát hiện tự động được bằng ~10 dòng code.*

### Debug và kết luận thực dụng

**Nhìn trace trước — bốn câu:** Thought có đúng mục tiêu? · Chọn đúng tool chưa? · 
 Args hợp lệ không? · Observation thiếu field nào không?

**Bốn nơi phải sửa:** tool description mơ hồ · system prompt thiếu rule dừng · không có 
 safeguard retry/loop · **evaluation chỉ chấm final answer**.

**Thang pattern Anthropic:** Augmented LLM → Prompt Chaining → Routing → 
 Orchestrator-Worker → Agent. *Bốn trong năm nằm ở phía workflow.*

**Hybrid là kết luận thực dụng nhất:** triage → chatbot path 
 (phần lớn lưu lượng) / agent path (thiểu số giá trị cao) / người thật (lưới an toàn). Chi phí trung bình 
 gần chatbot, không gần agent. Cái giá: triage phải đúng.

---

<!-- chiron-source-span: {"source_span_id":"9c2e6175-d362-527a-98c9-06e135344338","locator":{"kind":"html_section","section_id":"gloss","order":16,"heading":"A–Z Từ điển thuật ngữ","source_file":"slide-buoi-3.html"},"checksum":"667f3c64c7af31c3999ebe736aa6b791be677cb1878d82508b234821f8d72ca4"} -->

## A–Z Từ điển thuật ngữ

Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện.

---

<!-- chiron-source-span: {"source_span_id":"7d4ea511-4717-501e-b25b-ae823e4df48f","locator":{"kind":"html_section","section_id":"bloom","order":17,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-buoi-3.html"},"checksum":"f73a5e8eb6eea9ec52c2aea3601dea61bb96c243e3f2b099515804a71ce35a9f"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab 3 kiểm tra mức 3–4; câu hỏi cuối bài 
 (slide 45) kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được bốn mức spectrum, bốn tiêu chí Agentic Fit, ba bước ReAct, và năm guardrail. | Hình 1 · Hình 2 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao "gọi LLM sáu lần theo trình tự cố định" vẫn chưa phải 
 agent. | Slide 7 · ô kiểm tra chương 1–2 |
| 3 · Áp dụng | Chấm Agentic Fit cho một bài toán mới, kèm lý do từng điểm, và chọn được cấp độ. | mô-đun Agentic Fit · Bài 1 → 3 |
| 4 · Phân tích | Đọc một trace và chỉ ra agent sai ở Thought, ở chọn tool, ở args, hay ở observation. | Slide 35 — bảng chẩn đoán · Bài 2 |
| 5 · Đánh giá | Trả lời "use case nào của bạn chỉ cần chatbot, use case nào cần agent loop?" bằng 
 điều kiện — và nói được điều gì sẽ làm bạn đổi ý. | mục áp dụng · Hình 3 |

không phải

"Nó gọi được tool gì? Và lộ trình xử lý có viết trước 
 được không?"
