---
schema_version: 1
course_id: rag-intensive
document_id: "d67dd538-7a89-5ad6-83b2-9ceb0280af83"
document_version_id: "9b549345-7808-553c-876d-ed5b34316bb7"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "LangGraph & Agentic Orchestration — phân tích & breakdown từng slide"
source_file: "track-3-day-23.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-23.html"
source_sha256: "d3b6b5634c313136382b8f719cba650759a6dba7242410eeacd615fac2b46d00"
parser_version: chiron-structured-markdown-v1
html_section_count: 17
interactive_module_count: 6
interactive_control_count: 10
language: vi
---

# LangGraph & Agentic Orchestration — phân tích & breakdown từng slide

> Đọc lại toàn bộ 36 slide, giải thích cặn kẽ từ state/reducer đến checkpointing, 
 human-in-the-loop và error recovery, kèm 4 mô-đun tương tác. Đây là bài học 
 áp dụng trực tiếp nhất vào SmartCheck AI — vì nó nói về chính stack bạn đang dùng.

<!-- chiron-source-span: {"source_span_id":"8f528428-02fd-5770-b166-250e26bd0159","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"track-3-day-23.html"},"checksum":"c6ae01feaf6826f6c8be4a16442aab44617602a1072208e8735638f9abd14e48"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Bài này khác hai bài trước ở một điểm quyết định: **bạn đã đang dùng chính công nghệ này**. 
 SmartCheck AI là một LangGraph workflow. Nên đây không phải bài học "để biết" — nó là bản 
 kiểm tra sức khoẻ cho code bạn sắp viết.

Lượt 1 · ~15 phút

Trước khi vào lab

- Đọc slide 9, 14, 20, 34
- Chạy mô phỏng reducer — 2 phút, và nó sẽ làm bạn giật mình
- Mục tiêu: biết reducer sai làm mất dữ liệu im lặng như thế nào

Lượt 2 · ~60 phút

Để làm được, không chỉ hiểu

- Chương 2–5, làm hết phần "Dự đoán trước khi kéo"
- Làm 3 bài tập bậc thang theo thứ tự
- Dừng ở mỗi Ô kiểm tra cuối chương

Lượt 3 · ~30 phút

Trong và sau lab

- Dùng bộ tự chấm rubric khi còn 30 phút cuối lab
- Áp dụng vào SmartCheck AI — có diff code cụ thể
- Cheat sheet + Từ điển thuật ngữ

track 3 — day 23

"Day 08 · State Machines cho Agents"

LangGraph & Agentic Orchestration

---

<!-- chiron-source-span: {"source_span_id":"bd30a62b-efe5-5e53-9a3f-18e5fac9d342","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"track-3-day-23.html"},"checksum":"46591b54c90af41d3b6dfb4645e2e2ebb9087fbdc8070e11774cdb4a6ba5c2b5"} -->

## 00 Mở đầu

Slide 1–3: định vị bài học và câu hỏi dẫn dắt.

### Slide 1 Trang bìa

> Trích slide 
>  "LangGraph & Agentic Orchestration — Day 08 · State Machines cho Agents · 
>  2h theory + 2h guided lab. Instructor. VinUniversity · Phase 2 · Track 3 · Week 5"

**Tên phụ mới là tên thật của bài học:** *State Machines cho Agents*. 
 "LangGraph" chỉ là tên thư viện; thứ bạn thật sự học là **cách nghĩ về agent như một máy trạng thái** — và cách nghĩ đó sống lâu hơn bất kỳ thư viện nào.

Vì sao phân biệt này quan trọng Nếu bạn học "cú pháp LangGraph", kiến thức hết hạn khi API đổi phiên bản. 
 Nếu bạn học "state, node, edge, reducer, checkpoint", bạn đọc được cả Temporal, Airflow, 
 AWS Step Functions và bất kỳ orchestrator nào khác — vì tất cả đều là cùng một mô hình. 
 Toàn bộ tài liệu này ưu tiên tầng thứ hai.

### Slide 2 Câu hỏi dẫn dắt

> Trích slide 
>  "HÃY SUY NGHĨ… — Khi agent cần loop, retry, human approval và resume sau crash, 
>  chain một chiều còn đủ không? "

Câu hỏi liệt kê **bốn nhu cầu**, và mỗi nhu cầu phá vỡ mô hình chain theo một cách khác nhau. 
 Đây là bảng đáng nắm trước khi đọc tiếp:

| Nhu cầu | Chain gãy ở đâu | Cần khái niệm gì |
| --- | --- | --- |
| Loop | Chain là đồ thị không chu trình — không có đường quay lại | Conditional edge trỏ ngược |
| Retry | Không có chỗ nào lưu "đã thử mấy lần" | State có trường attempt |
| Human approval | Chain chạy một mạch, không có khái niệm "tạm dừng" | interrupt() + resume |
| Resume sau crash | Toàn bộ tiến trình nằm trong RAM; tiến trình chết là mất sạch | Checkpointer + thread id |

loop

retry

human approval

resume

context.md

### Slide 3 Nội dung bài học

> Trích slide 
>  "1. Mục tiêu & lịch học 2. Khi nào chain không đủ? 3. Core API 4. Persistence & Time Travel 
>  5. Human-in-the-Loop & Error Recovery 6. Lab 4 giờ 7. Takeaways"

Bảy chương đi theo trình tự **động cơ → công cụ → độ bền → an toàn → thực hành**. 
 Chương 3 (Core API) là chương dài nhất và cũng là chương duy nhất bạn *bắt buộc* phải nắm chắc: 
 ba chương sau đều xây trên nó.

Chương 3, cụ thể là phần reducer (slide 14–15), mới là nơi lab chết

---

<!-- chiron-source-span: {"source_span_id":"8f9612f4-b850-5c91-85ef-8a6f50e812f2","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Mục tiêu & lịch học","source_file":"track-3-day-23.html"},"checksum":"0b0143f8dee88d61ca0b87ad450f50c1b3bf199fea7b40a2c48d53bbd00f0ab8"} -->

## 01 Mục tiêu & lịch học

Slide 4–6: đầu ra mong đợi và cách 4 giờ được chia.

### Slide 4 Section divider

> Trích slide 
>  "01 — Mục tiêu & lịch học. 2 giờ lý thuyết cô đọng, 2 giờ lab có hướng dẫn; 
>  bài lab thiết kế đủ 4 giờ để phân loại năng lực."

Chú ý câu cuối: lab **cố tình** dài hơn thời gian trên lớp. 
 Đây là thiết kế "phân loại năng lực" — nghĩa là phần mở rộng (crash-resume, time travel, parallel) 
 không phải bonus vui vẻ mà là *thang đo*. Ai chỉ làm xong phần core sẽ nằm ở mức trung bình theo thiết kế.

### Slide 5 Sau buổi học, học viên làm được gì?

> Trích slide 
>  Conceptual outcomes: ■ Phân biệt LCEL chain, agent loop và stateful graph. 
>  ■ Thiết kế state, node, edge, reducer trong LangGraph. ■ Hiểu checkpointing, time travel, HITL và error recovery. 
>  Practical outcomes: ■ Xây dựng workflow có conditional routing, retry và interrupt. 
>  ■ Ghi trace/metric phục vụ chấm điểm. ■ Viết report kỹ thuật ngắn theo rubric production. 
>  Checkpoint: Cuối buổi: mỗi nhóm demo một graph chạy được trên test case cơ bản; 
>  học viên giỏi hoàn thiện thêm crash recovery và report.

Sáu outcome này ánh xạ gần như 1-1 vào [rubric chấm điểm ở slide 31](#s31). 
 Đọc chúng như một danh sách kiểm tra chứ không phải văn mô tả khoá học:

| Outcome | Bằng chứng phải nộp | Mục rubric |
| --- | --- | --- |
| Phân biệt chain / loop / graph | Phần mở đầu report giải thích vì sao chọn graph | Report & demo (15đ) |
| Thiết kế state, node, edge, reducer | State schema có typing và reducer khai báo rõ | Architecture & state (20đ) |
| Checkpointing, time travel, HITL, recovery | State history dump + demo resume | Persistence & recovery (15đ) |
| Routing + retry + interrupt chạy được | 6 scenario chạy qua | Graph behavior (25đ) |
| Trace/metric | metrics.json hợp lệ | Metrics & tests (20đ) |
| Report theo rubric | report.md có failure analysis | Report (15đ) + hygiene (5đ) |

trước khi

rubric

### Slide 6 Timeline 4 giờ

> Trích slide 
>  2h lý thuyết: ■ 20' LCEL gap + state machine ■ 30' StateGraph API 
>  ■ 25' persistence + checkpointing ■ 25' HITL + error recovery ■ 20' metric/report briefing 
>  2h trên lớp + 2h mở rộng: ■ 0-2h: build runnable core graph 
>  ■ 2-3h: persistence + crash-resume ■ 3-4h: metrics, report, polish

Phần lý thuyết dành **30 phút cho StateGraph API** — nhiều nhất trong năm mục. 
 Đó là tín hiệu rõ về nơi trọng lượng kiến thức nằm.

35 điểm

Chiến thuật an toàn:

stub trả về giá trị cứng

luôn có một graph chạy được

---

<!-- chiron-source-span: {"source_span_id":"d35430d6-3914-522a-b7fc-feebc0c2db08","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Khi nào chain không đủ?","source_file":"track-3-day-23.html"},"checksum":"de52e993b18f6eac912feea7cab24f0106668c16fa0f8d2c9ccadf8d4934ad29"} -->

## 02 Khi nào chain không đủ?

Slide 7–11: giới hạn của LCEL, năm khoảng trống production, và ví dụ support ticket.

### Slide 7 Section divider

> Trích slide 
>  "02 — Khi nào chain không đủ? LCEL phù hợp pipeline một chiều; agent production thường cần 
>  trạng thái, nhánh, vòng lặp và kiểm soát lỗi."

Chú ý cách slide phát biểu: **không phải "LCEL dở"** mà là "LCEL phù hợp pipeline một chiều". 
 Đây lại đúng khuôn mẫu "start simplest" của Ngày 20 — chain là bậc thấp, graph là bậc cao, 
 và bạn chỉ leo lên khi có nhu cầu cụ thể.

### Slide 8 LCEL Chain — con đường một chiều

> Trích slide 
>  "Retrieve → LLM → Output — khó loop lại · khó pause cho human · khó resume sau crash 
>  Chain đủ khi: ■ task đơn giản, single-shot; ■ không cần retry thông minh; 
>  ■ không cần human approval; ■ không cần lưu state dài hạn. 
>  Workflow của bạn có cần quyết định bước tiếp theo dựa trên kết quả bước trước không? 
>  Nếu có, hãy nghĩ tới graph. "

_Sơ đồ: So sánh LCEL chain một chiều với StateGraph có chu trình - Chain chạy thẳng từ retrieve qua LLM tới output, không có đường quay lại và không có điểm dừng. StateGraph có nhánh điều kiện, đường lặp lại từ bước kiểm tra về bước thực thi, và một nút interrupt cho phép tạm dừng chờ người rồi tiếp tục._

Hình 1 — Chain vs StateGraph (slide 8).

hình dạng đồ thị

#### Bốn điều kiện "chain đủ" — đọc như một cổng, không phải một gợi ý

Slide liệt kê bốn điều kiện **phải đúng đồng thời** thì chain mới đủ. 
 Chỉ cần một điều sai là bạn cần graph:

1. Task đơn giản, single-shot — một lượt vào, một lượt ra.
2. Không cần retry thông minh — "thông minh" ở đây nghĩa là retry có điều kiện 
 (chỉ retry lỗi tạm thời, có backoff, có giới hạn). Retry ngu ngốc bằng try/except thì chain làm được.
3. Không cần human approval — không có bước nào cần dừng lại chờ người.
4. Không cần lưu state dài hạn — chạy xong là quên.

"Workflow của bạn có cần quyết định bước tiếp theo dựa trên kết quả bước trước không?"

có

state

conditional edge

classify_intent

### Slide 9 Production gap — 5 vấn đề thường gặp

> Trích slide 
>  " LCEL gap → LangGraph pattern 
>  Retry logic → Loop + conditional edge · Human approval → interrupt + resume · 
>  Dynamic routing → conditional edges · Crash recovery → checkpointing · 
>  Parallel work → fan-out + reducer 
>  Mini poll - 4 phút: Trong sản phẩm bạn từng làm, vấn đề nào xuất hiện nhiều nhất: 
>  retry, routing, human approval, crash recovery hay parallel work? "

Bảng ánh xạ này là **bản đồ của cả bài học** — mỗi dòng là một chương sau. 
 Đáng mở rộng thêm hai cột: triệu chứng bạn thấy trong production, và cái giá nếu bỏ qua:

| Khoảng trống | Pattern | Triệu chứng trong production | Cái giá nếu bỏ qua |
| --- | --- | --- | --- |
| Retry logic | Loop + conditional edge | Tool lỗi 503 một lần là cả request hỏng | Tỷ lệ thành công tụt theo độ tin cậy của dịch vụ yếu nhất |
| Human approval | interrupt + resume | Không có cách nào chèn người vào giữa luồng | Hoặc chặn hết mọi hành động rủi ro, hoặc để agent tự làm — không có đường giữa |
| Dynamic routing | Conditional edges | Mọi request đi cùng một đường, tốn như nhau | Cost và latency không tối ưu được theo độ khó |
| Crash recovery | Checkpointing | Deploy giữa giờ là mất hết phiên đang chạy | Không deploy được giờ cao điểm; user mất việc đang làm dở |
| Parallel work | Fan-out + reducer | Các bước độc lập vẫn chạy tuần tự | Latency cộng dồn không cần thiết |

reducer

hai

không báo lỗi

mô-đun mô phỏng reducer

cơ chế

### Slide 10 LangGraph trong một câu

> Trích slide 
>  "LangGraph — Framework orchestration theo graph: typed state + node functions + 
>  edges/conditional edges + checkpointing để xây workflow agent có loop, interrupt, 
>  persistence và fault tolerance. 
>  Khi dùng: ■ agent cần nhiều bước và quyết định động; ■ cần human-in-the-loop; 
>  ■ cần khôi phục sau lỗi; ■ cần trace/debug. 
>  Khi chưa cần: ■ prompt đơn lẻ; ■ ETL tuyến tính; ■ không có state; 
>  ■ không cần approval hoặc audit."

Định nghĩa một câu này có **bốn thành phần**, và chúng chính là bốn khái niệm bạn 
 phải nắm ở chương 3. Đáng học thuộc theo đúng thứ tự này vì nó cũng là thứ tự bạn viết code:

```text
typed state          →  cái gì được truyền đi và ghi nhớ
       ↓
node functions       →  ai làm gì với state đó
       ↓
edges / conditional  →  đi đâu tiếp theo
       ↓
checkpointing        →  lưu lại sau mỗi bước để pause / resume / replay
```

công cụ mạnh hơn không phải công cụ mặc định

### Slide 11 Ví dụ thực tế — support ticket triage

> Trích slide 
>  " Flow: 1. Nhận ticket. 2. Classify: billing, bug, policy, urgent. 
>  3. Nếu thiếu thông tin: hỏi lại khách. 4. Nếu rủi ro cao: dừng để human approve. 
>  5. Nếu tool lỗi: retry hoặc dead-letter. 
>  Routing, loop hỏi lại, HITL và retry đều phụ thuộc state hiện tại. Một chain tuyến tính 
>  sẽ nhanh trở nên khó maintain. 
>  Think-pair-share - 5 phút: Viết 1 state field cần có cho ticket workflow và lý do. "

Năm bước của flow này ánh xạ chính xác vào năm dòng của [slide 9](#s9) — 
 không phải trùng hợp, đây là ví dụ được thiết kế để minh hoạ đủ cả bảng.

#### Bài tập "1 state field" — vài đáp án tốt và vì sao

| Field | Kiểu & reducer | Vì sao cần |
| --- | --- | --- |
| attempt | int, overwrite | Không có nó thì không thể giới hạn retry — vòng lặp sẽ chạy mãi |
| missing_fields | list[str], overwrite | Là trạng thái hiện tại chứ không phải lịch sử — append sẽ khiến field đã điền vẫn nằm trong danh sách thiếu |
| errors | list[str], append | Là lịch sử — cần đủ để phân tích failure trong report |
| pending_approval | bool, overwrite | Cổng chặn hành động phá huỷ khi chưa có người duyệt |
| risk_level | str, overwrite | Đầu vào cho quyết định "có cần approval không" |

missing_fields

errors

list[str]

reducer ngược nhau

trạng thái hiện tại

lịch sử đã xảy ra

slide 15

phần áp dụng SmartCheck AI

#### Ô kiểm tra — Chương 2

Trả lời thành tiếng trước khi mở đáp án.

**1.** Đồng nghiệp nói: "LangGraph mạnh hơn LCEL nên mình cứ dùng LangGraph cho mọi thứ." 
 Phản biện thế nào? Hiểu

#### Đáp án

Slide 10 có sẵn danh sách "khi chưa cần": prompt đơn lẻ, ETL tuyến tính, không có state, 
 không cần approval/audit. Với những bài toán đó, LangGraph thêm một tầng trừu tượng 
 (state schema, node, edge, checkpointer) mà *không đổi lấy gì*.

Phép thử một câu của slide 8: *"có cần quyết định bước tiếp theo dựa trên kết quả bước trước không?"* Không → chain. Có → graph.

*Điểm cộng nếu bạn nhận ra:* đây đúng là khuôn mẫu của Ngày 20 (đừng thêm agent) 
 và Ngày 21 (đừng fine-tune). Ba bài khác nhau, cùng một nguyên tắc: công cụ mạnh hơn 
 không phải công cụ mặc định.

**2.** Trong năm khoảng trống của slide 9, cái nào có pattern gồm *hai* phần — 
 và vì sao phần thứ hai nguy hiểm? Phân tích

#### Đáp án

**Parallel work → fan-out *+ reducer*.**

Phần thứ hai nguy hiểm vì bỏ quên nó **không gây lỗi**. Reducer mặc định là *overwrite*, nên khi nhiều nhánh song song cùng ghi vào một field, nhánh sau ghi đè nhánh trước. 
 Không exception, không warning — chỉ là kết quả bị mất.

Bốn khoảng trống còn lại đều "kêu" khi sai: thiếu retry thì thấy lỗi, thiếu interrupt thì 
 không dừng được, thiếu checkpoint thì crash mất phiên. Chỉ reducer là hỏng trong im lặng.

**3.** Cùng là `list[str]`, vì sao `errors` nên append còn `missing_fields` nên overwrite? Áp dụng

#### Đáp án

Vì chúng trả lời hai câu hỏi khác nhau. `errors` là **nhật ký**: 
 "những gì đã hỏng trong phiên này" — mất một mục là mất bằng chứng cho failure analysis. `missing_fields` là **ảnh chụp**: "hiện tại còn thiếu gì".

Nếu append `missing_fields`: khách cung cấp số điện thoại, node cập nhật danh sách 
 thiếu thành `[]`, nhưng append giữ nguyên `["phone"]` từ lượt trước → **graph hỏi lại số điện thoại vô hạn**. Một reducer sai tạo ra một vòng lặp vô hạn.

**Quy tắc mang đi:** hỏi "ảnh chụp hay nhật ký?" chứ đừng hỏi "kiểu list hay không?".

---

<!-- chiron-source-span: {"source_span_id":"9bed4da4-fb6f-5ce3-82ed-a1f57064c4eb","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Core API","source_file":"track-3-day-23.html"},"checksum":"f87d9ff67fec5d5046e32daadaf01839560dfbae90625e00b12b2f7666d3fc35"} -->

## 03 Core API

Slide 12–18: state, node, edge, reducer — bốn khái niệm nền tảng, và chương quyết định thành bại của lab.

### Slide 12 Section divider

> Trích slide 
>  "03 — Core API. State, node, edge, reducer là bốn khái niệm nền tảng của StateGraph."

Bốn khái niệm, và chúng có **độ khó rất không đều nhau**. 
 Node và edge là trực giác — ai cũng hiểu ngay. State cần chút kỷ luật thiết kế. **Reducer là khái niệm duy nhất mà hiểu sai sẽ hỏng trong im lặng**, nên nó chiếm 
 phần lớn chương này.

### Slide 13 State Machine — khái niệm cốt lõi

> Trích slide 
>  "START → plan → execute → done? → END (yes) / no: retry (quay lại) 
>  State: {messages, plan, tool_results, attempt, status, pending_approval} 
>  Node: Python function đọc state và trả về partial update. 
>  Edge: đường chuyển bước; có thể cố định hoặc conditional."

Ba định nghĩa này ngắn nhưng có một chữ mang toàn bộ sức nặng: **"partial update"**. 
 Node *không* trả về state mới — nó trả về *một mẩu* state, và LangGraph tự ghép mẩu đó vào. 
 Cách ghép chính là reducer.

_Sơ đồ: Cách reducer ghép partial update từ nhiều node vào state - State ban đầu chứa một phần tử. Hai node chạy song song, mỗi node trả về một partial update. Reducer add nối cả hai vào thành ba phần tử; reducer overwrite mặc định chỉ giữ lại phần tử của node ghi sau cùng và làm mất phần tử của node kia._

Hình 2 — Reducer quyết định điều gì sống sót (slide 13–15).

### Slide 14 State design — code-level

> Trích slide 
>  class AgentState(TypedDict): messages: Annotated[list[str], add]; query: str; route: str; 
>  attempt: int; tool_results: Annotated[list[str], add]; final_answer: str | None; 
>  errors: Annotated[list[str], add] 
>  5 quy tắc thiết kế state: 1. Flat, ít nested dict. 2. Reducer rõ cho list. 
>  3. Typed và validate được. 4. Lean: không lưu blob lớn. 5. Versioned khi schema thay đổi. 
>  Lưu ý: Default reducer là overwrite. Nếu 2 node cùng ghi một field list mà không khai báo reducer, 
>  rất dễ mất dữ liệu.

#### Năm quy tắc, và cái giá cụ thể khi vi phạm

| Quy tắc | Vi phạm thì sao | Dấu hiệu nhận ra sớm |
| --- | --- | --- |
| 1 · Flat | Reducer không chạm được vào field lồng sâu — merge lồng nhau phải tự viết và rất dễ sai | Bạn thấy mình viết hàm merge dict đệ quy |
| 2 · Reducer rõ cho list | Mất dữ liệu im lặng khi fan-out | Không có dấu hiệu — đó chính là vấn đề |
| 3 · Typed & validate | Node nhận state sai kiểu, lỗi nổ ở nơi cách xa nguyên nhân | KeyError / NoneType ở node không liên quan |
| 4 · Lean | Mỗi checkpoint copy nguyên blob → chậm và phình storage | Latency tăng dần theo số bước; xem máy tính checkpoint |
| 5 · Versioned | Checkpoint cũ không load được sau khi đổi schema → mất phiên đang chạy khi deploy | Deploy xong là các phiên dở dang chết hàng loạt |

đã được serialize

không resume được

schema_version: int

migrate

bỏ qua một cách có kiểm soát

#### Đọc kỹ đoạn code trên slide: bốn field có reducer, ba field không

| Field | Reducer | Vì sao |
| --- | --- | --- |
| messages, tool_results, errors | add (append) | Đều là nhật ký — thứ tự và tính đầy đủ mới có giá trị |
| query, route, final_answer | mặc định (overwrite) | Đều là ảnh chụp — chỉ giá trị mới nhất có nghĩa |
| attempt | mặc định (overwrite) | Đúng miễn là chỉ một node ghi. Nếu hai node cùng tăng attempt song song, bạn cần reducer cộng dồn — nếu không, một lần tăng sẽ biến mất |

### Slide 15 Reducer — luật merge state

> Trích slide 
>  Overwrite phù hợp cho: ■ status hiện tại; ■ route hiện tại; ■ final answer; 
>  ■ counter nếu chỉ một node ghi. 
>  Append phù hợp cho: ■ messages; ■ tool results; ■ errors; ■ audit events; ■ metric records. 
>  Quick check - 3 phút: Field audit_log nên overwrite hay append? Vì sao?

**Đáp án cho quick check: append** — và lý do sâu hơn "vì nó là list". 
 Audit log tồn tại để trả lời câu hỏi *"chuyện gì đã xảy ra, theo thứ tự nào"*. 
 Một audit log bị ghi đè không chỉ mất dữ liệu — nó **mất chính lý do tồn tại của mình**, 
 vì một bản ghi kiểm toán không đầy đủ thì tệ hơn không có: nó tạo cảm giác an toàn giả.

chỉ

duy nhất một node

attempt

không tái hiện được

#### Tương tác Mô phỏng reducer — dữ liệu biến mất như thế nào

Nhiều node chạy song song, mỗi node trả về một partial update cho cùng một field list. 
 Đổi reducer và xem có bao nhiêu thứ sống sót.

**3 node song song, mỗi node ghi 3 item** vào cùng một field `list[str]` — tổng cộng 9 item được tạo ra. Bạn *quên* khai báo reducer. 
 Đoán trước:

1. Bao nhiêu item còn lại trong state?
2. Chương trình có báo lỗi gì không?

#### Kéo xong rồi mở

**① Còn lại 3 trên 9 — mất 67%.** Reducer mặc định là overwrite, nên nhánh ghi sau cùng đè lên tất cả các nhánh trước.

**② Không có lỗi nào cả.** Không exception, không warning, không log đỏ. 
 Test "graph chạy được" vẫn pass. Metrics "task success rate" vẫn 100%. 
 Bạn chỉ phát hiện khi ai đó hỏi *"sao báo cáo thiếu kết quả của hai tool kia?"*

**Vì sao đây là lỗi nguy hiểm nhất trong bài:** bốn khoảng trống còn lại ở [slide 9](#s9) đều "kêu" khi sai — thiếu retry thì thấy lỗi, thiếu interrupt thì 
 không dừng được, thiếu checkpoint thì crash mất phiên. Chỉ reducer là hỏng *trong im lặng*.

**Bài học mang đi:** mỗi khi bạn thêm một field `list` vào state, 
 hãy hỏi ngay *"ảnh chụp hay nhật ký?"* — và nếu là nhật ký thì gõ luôn `Annotated[list[str], add]` ở chính dòng đó. Đừng để lại "làm sau", 
 vì lỗi này không có triệu chứng để nhắc bạn.

*Thử thêm:* kéo số node lên 5. Tỷ lệ mất tăng lên 80% — **càng song song hoá nhiều, bạn càng mất nhiều**. Nghĩa là tối ưu latency 
 bằng fan-out (bài học Ngày 20) sẽ *khuếch đại* chính lỗi này.

Reducer mặc định (overwrite)

Annotated[list, add]

- **Control - Số node ghi song song 3**: min `2`, max `6`, step `1`, default `3`

- **Control - Số item mỗi node ghi 3**: min `1`, max `6`, step `1`, default `3`

Item được tạo ra

—

tổng của mọi node

Còn trong state

—

—

Bị mất

—

không có exception nào

Tỷ lệ mất

—

tăng theo số nhánh song song

Giữ lại trong state ⚠ Bị ghi đè, mất im lặng

#### Xem dạng bảng



#### Mô hình này giả định gì

- Các node chạy trong cùng một super-step và cùng ghi vào một field. 
 Đây đúng là tình huống fan-out mà slide 9 mô tả.
- Với reducer mặc định, LangGraph lấy giá trị của nhánh ghi sau cùng — thứ tự không đảm bảo, 
 nên bạn thậm chí không dự đoán được nhánh nào sống sót. Mô hình này giữ lại đúng một nhánh.
- Nếu các node ghi vào các field khác nhau thì không có xung đột — vấn đề chỉ xuất hiện 
 khi nhiều nhánh cùng chạm một field.
- Thực tế LangGraph sẽ báo lỗi InvalidUpdateError ở một số cấu hình fan-out; 
 đừng dựa vào đó — nhiều trường hợp vẫn merge im lặng.

### Slide 16 Node function — nguyên tắc production

> Trích slide 
>  def classify_node(state: AgentState) -> dict: route = classify_query(state["query"]); 
>  return {"route": route, "messages": [f"classified:{route}"]} 
>  def tool_node(state: AgentState) -> dict: result = run_tool(state["query"]); 
>  return {"tool_results": [result]} — # Nodes should be small and testable 
>  Checklist: ■ Pure-ish: không side effect nếu tránh được. ■ Idempotent cho retry. 
>  ■ Return partial update, không mutate toàn state. ■ Log đủ cho audit. ■ Timeout và error typed.

Năm mục checklist này không ngang nhau về mức độ quan trọng. Xếp lại theo "sai thì đau đến đâu":

| Mức | Nguyên tắc | Sai thì sao |
| --- | --- | --- |
| Cao nhất | Idempotent cho retry | Retry một node gửi email = gửi email hai lần. Retry một node charge tiền = charge hai lần. Đây là loại lỗi không rollback được |
| Cao | Return partial update, không mutate | Mutate state trực tiếp phá vỡ checkpoint và time travel — snapshot không còn phản ánh đúng lịch sử |
| Trung bình | Timeout và error typed | Node treo làm cả graph treo; error không phân loại được thì không biết nên retry hay dead-letter |
| Trung bình | Pure-ish | Side effect ẩn làm node không test được độc lập |
| Nền tảng | Log đủ cho audit | Không có bằng chứng khi cần điều tra — và mất điểm rubric |

Một node idempotent là node mà **chạy 1 lần hay 5 lần đều cho cùng một kết quả bên ngoài**.

*An toàn tự nhiên:* đọc DB, gọi API tra cứu, tính toán, gọi LLM (tốn tiền nhưng không hỏng gì).

*KHÔNG an toàn:* gửi email/SMS, tạo bản ghi, trừ tiền, cập nhật trạng thái. 
 Ba việc cuối trong luồng SmartCheck AI đều thuộc nhóm này: `register_visitor`, `generate_visitor_pass`, `notify_host`.

**Cách sửa chuẩn — idempotency key:**

```text
def notify_host_node(state):
    key = f"notify:{state['session_id']}:{state['host_id']}"
    if cache.get(key):                 # đã gửi rồi trong phiên này
        return {"messages": ["notify: skipped (đã gửi)"]}
    send_notification(state["host_id"], state["visitor_id"])
    cache.set(key, 1, ex=3600)
    return {"messages": ["notify: sent"]}
```

Khoá phải suy ra được *từ state*, không phải sinh ngẫu nhiên — vì sau khi retry, 
 node phải tính ra **đúng cái khoá cũ** thì mới biết là đã làm rồi.

### Slide 17 Conditional edges — dynamic routing

> Trích slide 
>  "classify → route → simple_qa (easy) / rag_search (medium) / full_agent (hard) → output 
>  Nhận state, trả về tên nhánh tiếp theo. Dùng để tối ưu cost, latency và risk. 
>  ■ Easy query: cheap path. ■ Missing info: ask user. ■ Risky action: approval. 
>  ■ Repeated error: fallback/dead-letter."

_Sơ đồ: Conditional edge phân nhánh theo độ khó của câu hỏi - Node classify đưa state vào một hàm route, hàm này trả về tên nhánh: câu dễ đi đường rẻ simple_qa, câu trung bình đi rag_search, câu khó đi full_agent; cả ba nhánh hội tụ về output._

Hình 3 — Conditional edge (slide 17).

partial update

tên nhánh

- Hàm route không ghi vào state — muốn lưu quyết định route thì node phía trước 
 phải ghi nó (như classify_node trả về {"route": route} ở slide 16).
- Hàm route nên là code thuần, không gọi LLM. Nếu bạn cần LLM để quyết định, 
 hãy để LLM chạy trong node và ghi kết quả vào state, rồi route chỉ việc đọc field đó. 
 Cách này giúp quyết định routing được ghi vào checkpoint và xem lại được khi debug.

context.md

intent

CheckInState

### Slide 18 Graph wiring — từ node sang runnable graph

> Trích slide 
>  graph = StateGraph(AgentState); graph.add_node("classify", classify_node); … 
>  graph.add_edge(START, "classify"); graph.add_conditional_edges("classify", route_next, 
>  {"simple": "answer", "tool": "tool"}); graph.add_edge("answer", END); 
>  compiled = graph.compile(checkpointer=saver) 
>  Build order: 1. Define state schema. 2. Implement nodes. 3. Implement route functions. 
>  4. Add edges. 5. Compile with checkpointer. 6. Invoke with thread id.

Sáu bước này là **thứ tự bạn nên gõ code trong lab**, và nó có lý do: 
 mỗi bước chỉ phụ thuộc vào các bước trước nó. Nhưng có một mẹo thực chiến làm nó tốt hơn nữa:

```text
# Giờ đầu: mọi node là stub trả giá trị cứng
def classify_node(state): return {"route": "simple", "messages": ["stub:classify"]}
def answer_node(state):   return {"final_answer": "stub answer"}

# Nối graph, chạy end-to-end, xác nhận wiring đúng — 10 phút
# RỒI mới điền logic thật vào từng node
```

lỗi wiring

lỗi logic

rubric

luôn

compile(checkpointer=saver)

thread_id

không có tác dụng

thread_id

checkpointer

slide 22

#### Ô kiểm tra — Chương 3

Chương nặng nhất. Ba câu này bao trọn phần dễ mất điểm nhất của lab.

**1.** Vì sao node phải trả về *partial update* thay vì state đầy đủ đã sửa? Hiểu

#### Đáp án

Ba lý do, xếp theo độ quan trọng:

**① Để reducer có việc để làm.** Nếu node trả về state đầy đủ, LangGraph không biết 
 field nào *thật sự* thay đổi, nên không áp dụng được luật merge. Fan-out sẽ vô nghĩa.

**② Để checkpoint đúng.** Snapshot phải phản ánh chính xác node nào đã đổi gì. 
 Mutate toàn state làm mất khả năng truy vết — time travel không còn nói cho bạn biết ai gây ra thay đổi.

**③ Để node test được độc lập.** Một node nhận state và trả về dict nhỏ là một 
 hàm thuần, test bằng `assert` thường. Node mutate state là hàm có side effect.

**2.** Node `notify_host` gửi thông báo cho chủ nhà. Bạn thêm retry. 
 Cần làm gì trước? Áp dụng

#### Đáp án

**Làm cho nó idempotent** — nếu không, retry 3 lần = host nhận 3 thông báo.

Cách chuẩn: một **idempotency key** suy ra *từ state* (ví dụ `f"notify:{session_id}:{host_id}"` ), kiểm tra trước khi gửi, ghi lại sau khi gửi.

**Chi tiết quan trọng:** khoá phải *suy ra được từ state*, không phải sinh ngẫu nhiên 
 hay lấy timestamp. Sau khi retry, node phải tính ra **đúng cái khoá cũ** thì mới nhận ra 
 "việc này làm rồi". Khoá ngẫu nhiên biến idempotency thành vô nghĩa.

*Nguyên tắc chung:* "retry" và "idempotent" là một cặp. Thêm retry vào một node không 
 idempotent là biến một lỗi tạm thời thành một lỗi vĩnh viễn.

**3.** Bạn cần LLM để quyết định đi nhánh nào. Đặt lời gọi LLM ở đâu — trong 
 hàm `route()` hay trong node? Phân tích

#### Đáp án

**Trong node**, rồi ghi kết quả vào state; hàm `route()` chỉ đọc field đó và 
 trả về tên nhánh.

**Vì sao:** hàm route *không ghi vào state*, nên nếu quyết định được tạo ra 
 bên trong nó thì quyết định đó **không nằm trong checkpoint**. Hậu quả:

• Time travel không cho bạn biết vì sao graph rẽ nhánh đó. 
 • Replay có thể đi đường khác (LLM không tất định) → debug không tái hiện được. 
 • Metrics không đếm được phân bố route.

Đặt LLM trong node biến quyết định thành *dữ liệu* — và dữ liệu thì lưu được, xem lại được, 
 đếm được. Đây chính là lý do `CheckInState` của SmartCheck AI có field `intent`.

---

<!-- chiron-source-span: {"source_span_id":"81d95842-db4e-5757-943a-ad873624d54f","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Persistence & Time Travel","source_file":"track-3-day-23.html"},"checksum":"82147bf558d5a9b75a66a913f24cb45c6f983c9dc250b84ebc598c3000ef0477"} -->

## 04 Persistence & Time Travel

Slide 19–22: checkpointing biến graph thành workflow có thể pause, resume, replay và debug.

### Slide 19 Section divider

> Trích slide 
>  "04 — Persistence & Time Travel. Checkpointing biến graph thành workflow có thể pause, resume, 
>  replay và debug."

Bốn năng lực trong một câu, và chúng đều là **hệ quả của cùng một thứ**: 
 state được lưu lại sau mỗi bước. Không có checkpoint thì không có cái nào trong bốn cái đó — 
 kể cả human-in-the-loop ở chương 5.

### Slide 20 Checkpointing — state snapshot mỗi bước

> Trích slide 
>  "plan → C1 → execute → C2 → CRASH → resume (load checkpoint) → output 
>  Memory saver: nhanh, không bền sau restart. SQLite saver: persistent, dễ demo. 
>  Postgres saver: phù hợp service nhiều thread. 
>  Lưu ý: Large state = checkpoint lớn = chậm. Lưu references thay vì full document/blob. "

_Sơ đồ: Checkpoint và khôi phục sau crash - Sau mỗi bước graph ghi một checkpoint. Khi tiến trình crash ở giữa, phiên được khôi phục bằng cách nạp lại checkpoint gần nhất thay vì chạy lại từ đầu. Ba loại saver khác nhau về độ bền và tốc độ._

Hình 4 — Checkpoint và crash resume (slide 20).

#### Chọn saver nào — và vì sao lab nên dùng SQLite

| Saver | Bền sau restart | Nhiều tiến trình | Dùng khi |
| --- | --- | --- | --- |
| MemorySaver | ✕ | ✕ | Unit test, thử nghiệm nhanh. Không chứng minh được crash-resume |
| SqliteSaver | ✓ | Hạn chế (khoá file) | Lab — bền, một file, dễ đính kèm làm bằng chứng |
| PostgresSaver | ✓ | ✓ | Service thật có nhiều worker/thread |

MemorySaver

chưa chứng minh gì cả

SqliteSaver

kill tiến trình

thread_id

#### Tương tác Chi phí checkpointing — vì sao "lưu reference thay vì blob"

Mỗi super-step ghi một snapshot của *toàn bộ* state. Nhân với số bước, 
 nhân với số run, nhân với 30 ngày — con số lớn nhanh hơn trực giác.

Mặc định: state **50 KB**, 12 super-step mỗi run, 5.000 run/ngày, SQLite saver → 
 khoảng **92 GB/tháng**. Giờ bạn quyết định nhét kết quả RAG (cả nội dung tài liệu) 
 vào state, làm state phình lên **2.000 KB**. Đoán trước:

1. Storage mỗi tháng thành bao nhiêu?
2. Độ trễ ghi checkpoint mỗi run tăng bao nhiêu?

#### Kéo "Kích thước state" lên 2000 rồi mở

**① Từ 92 GB lên 3,7 TB mỗi tháng** — 
 gấp 40 lần, đúng bằng tỷ lệ phình của state. Quan hệ là tuyến tính, nhưng hệ số nhân 
 (12 bước × 5.000 run × 30 ngày = **1,8 triệu** ) làm mọi thứ nở ra rất nhanh.

**② Độ trễ ghi từ ~ 32 ms lên ~ 90 ms mỗi run** — 
 và đây là độ trễ *thêm vào* mọi request, không phải chỉ khi có sự cố.

**Vì sao đây là bẫy tự nhiên:** nhét kết quả RAG vào state là việc *hợp lý nhất trên đời* — node sau cần dùng nó mà. Không ai cố tình "lưu blob"; 
 người ta chỉ lưu thứ mình cần, và thứ đó tình cờ rất to.

**Cách sửa (đúng lời slide 20):** lưu `doc_ids` và một đoạn tóm tắt ngắn 
 vào state; nội dung đầy đủ để trong cache/DB và node nào cần thì tra lại. 
 Kéo về **5 KB** để thấy con số: khoảng 9,2 GB/tháng — 
 rẻ hơn **400 lần** so với phương án blob.

*Thử thêm:* đổi saver sang **Memory**. Độ trễ gần như biến mất — 
 đó là lý do MemorySaver hấp dẫn trong lúc dev, và cũng là lý do nó che mất chi phí thật 
 cho tới khi bạn lên production.

- **Control - Kích thước state 50 KB**: min `1`, max `4000`, step `1`, default `50`

- **Control - Super-step mỗi run 12**: min `3`, max `40`, step `1`, default `12`

- **Control - Run mỗi ngày 5.000**: min `100`, max `100000`, step `100`, default `5000`

Checkpointer

Memory saver

SQLite saver

Postgres saver

Ghi mỗi run

—

—

Storage mỗi tháng

—

chưa tính index và overhead của DB

Độ trễ thêm mỗi run

—

cộng vào MỌI request, không chỉ khi lỗi

So với lưu reference

—

nếu state chỉ 5 KB

Cấu hình hiện tại Chỉ lưu reference (5 KB)

#### Xem dạng bảng



#### Giả định của mô hình

- Mỗi super-step ghi một snapshot đầy đủ của state. Cài đặt thật có thể nén 
 hoặc ghi delta — khi đó con số thấp hơn, nhưng hình dạng của bài toán không đổi.
- Độ trễ ghi mỗi checkpoint: Memory ~0,05 ms · SQLite ~2,5 ms · Postgres ~5 ms. 
 Đây là số minh hoạ — hãy đo trên hạ tầng của bạn.
- Chi phí serialize ước tính theo thông lượng ~400 MB/s.
- Bỏ qua: index, WAL, replication, và chi phí đọc lại khi resume. 
 Con số thật sẽ cao hơn, không thấp hơn.

### Slide 21 Thread, checkpoint, time travel

> Trích slide 
>  "■ Thread: một phiên workflow, ví dụ một user request hoặc một ticket. 
>  ■ Checkpoint: snapshot state sau mỗi super-step khi graph có checkpointer. 
>  ■ Replay: chạy lại từ một checkpoint để debug hoặc A/B test route khác. 
>  ■ Update state: chỉnh state tại checkpoint trước khi resume, hữu ích cho HITL. 
>  Khi khách báo "agent gửi sai email", bạn cần state history để biết node nào quyết định sai, 
>  input lúc đó là gì, human đã approve hay chưa. "

Câu ví dụ ở cuối là câu hay nhất của slide, vì nó cho thấy time travel **không phải tính năng 
 debug cho lập trình viên** — nó là *hạ tầng chịu trách nhiệm*. Ba câu hỏi trong đó 
 là ba câu hỏi pháp lý/vận hành thật:

| Câu hỏi khi có sự cố | Trả lời được nhờ | Không có thì sao |
| --- | --- | --- |
| "Node nào quyết định sai?" | State history — thấy route tại từng checkpoint | Chỉ có thể đoán từ log rời rạc |
| "Input lúc đó là gì?" | Snapshot state trước node đó | Không tái hiện được — dữ liệu đã đổi |
| "Human đã approve chưa?" | Field approval trong checkpoint | Không chứng minh được — đây là rủi ro thật, không phải bất tiện |

node

super-step

song song

state sau super-step trông thế nào

lưu chính cái đó

### Slide 22 Invoke với thread id

> Trích slide 
>  config = {"configurable": {"thread_id": "ticket-123"}} 
>  result = compiled.invoke({"query": "Refund request for order 42"}, config=config) 
>  snapshot = compiled.get_state(config) 
>  history = list(compiled.get_state_history(config)) 
>  Lab metric liên quan: ■ Có thread id riêng cho mỗi run. ■ Có state history sau run. 
>  ■ Có trace events đủ để tính node count, retry count, approval count.

Bốn dòng code này là **toàn bộ API persistence** bạn cần cho lab. 
 Đáng chú ý là dòng cuối: `get_state_history()` trả về *toàn bộ* lịch sử checkpoint — 
 và đó chính là nguồn dữ liệu cho `metrics.json` mà rubric yêu cầu.

```text
hist = list(compiled.get_state_history(config))
metrics = {
    "thread_id":      config["configurable"]["thread_id"],
    "checkpoints":    len(hist),
    "nodes_visited":  sum(len(h.metadata.get("writes") or {}) for h in hist),
    "retry_count":    hist[0].values.get("attempt", 0),
    "interrupt_count": sum(1 for h in hist if h.next and "approval" in str(h.next)),
    "errors":         len(hist[0].values.get("errors", [])),
    "final_status":   hist[0].values.get("status"),
}
```

**Lưu ý về thứ tự:** `get_state_history()` trả về *mới nhất trước*, nên `hist[0]` là state **cuối cùng**, không phải đầu tiên. 
 Nhầm chỗ này làm mọi metric của bạn sai — và nó là lỗi rất hay gặp vì trực giác nói ngược lại.

Ba metric mà slide 22 yêu cầu (node count, retry count, approval count) đều suy ra được từ đây. 
 Viết hàm này ngay sau khi persistence chạy, đừng để tới mốc 180 phút.

ổn định theo phiên

duy nhất giữa các phiên

- ✓ f"ticket-{ticket_id}", f"session-{session_id}" — suy ra từ nghiệp vụ, 
 nên resume được từ tiến trình khác.
- ✕ str(uuid4()) sinh mới mỗi lần invoke — mỗi lần chạy là một thread mới, 
 không bao giờ resume được.
- ✕ Dùng chung một id cố định cho mọi run — các phiên ghi đè lên nhau.

session_id

context.md

config

#### Ô kiểm tra — Chương 4

**1.** Bạn dùng `MemorySaver` và demo "resume" bằng cách gọi `invoke` hai lần trong cùng script. Vì sao điều này không chứng minh crash recovery? Phân tích

#### Đáp án

Vì state **chưa bao giờ rời khỏi RAM của tiến trình đó**. Bạn đang chứng minh rằng 
 một biến Python vẫn còn giá trị — điều luôn đúng và không liên quan gì tới crash.

Crash recovery nghĩa là: *tiến trình chết, state vẫn sống*. Muốn chứng minh thì phải có 
 ranh giới tiến trình thật: dùng `SqliteSaver`, chạy lần 1 rồi kill, 
 chạy lần 2 với **cùng thread_id** từ một tiến trình mới, và cho thấy nó tiếp tục 
 chứ không làm lại từ đầu.

*Bằng chứng nộp kèm:* log của cả hai lần chạy + file `.sqlite` + 
 dump `get_state_history()` cho thấy các checkpoint trước khi kill vẫn còn.

**2.** Vì sao checkpoint được ghi sau mỗi *super-step* chứ không phải sau mỗi node — 
 và điều đó liên quan gì tới reducer? Hiểu

#### Đáp án

Một super-step là một nhịp: mọi node đủ điều kiện chạy sẽ chạy *song song*, 
 rồi kết quả của chúng được **merge qua reducer** và mới thành một state nhất quán.

Ghi checkpoint sau từng node riêng lẻ sẽ lưu những state *chưa merge xong* — 
 tức là state không hợp lệ. Checkpoint phải là một ảnh chụp **nhất quán**.

**Hệ quả quan trọng:** reducer sai ⇒ state sau merge đã mất dữ liệu ⇒ 
 checkpoint lưu lại đúng cái state thiếu đó ⇒ resume từ nó cũng thiếu. 
 Reducer và checkpoint là hai mặt của một đồng xu; sửa checkpoint không cứu được reducer sai.

**3.** Node RAG của bạn trả về 8 tài liệu, mỗi tài liệu 40 KB. Bạn định lưu cả 
 vào state cho node sau dùng. Nên làm gì? Áp dụng

#### Đáp án

**Đừng.** 320 KB × mỗi super-step × mỗi run — xem [máy tính checkpoint](#m-ckpt) để thấy con số nở ra thế nào.

**Làm thay:** lưu `doc_ids` + đoạn trích ngắn (vài trăm byte mỗi tài liệu) 
 vào state; nội dung đầy đủ để trong cache hoặc DB, node nào cần thì tra lại bằng id.

Đây đúng lời dặn của slide 20 — *"lưu references thay vì full document/blob"* — 
 và cũng là quy tắc 4 trong 5 quy tắc thiết kế state ở slide 14 ( *lean* ).

*Lợi ích phụ ít ai nghĩ tới:* state gọn thì `get_state_history()` đọc nhanh, 
 nên chính việc debug và tính metrics của bạn cũng nhanh hơn.

---

<!-- chiron-source-span: {"source_span_id":"5d0d4b1a-0164-5db6-b10e-a408fd566d9e","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Human-in-the-Loop & Error Recovery","source_file":"track-3-day-23.html"},"checksum":"3cbb8c4b87802d1d6af669d6145eb72b74c59b4d09395c7d5868747d98aab223"} -->

## 05 Human-in-the-Loop & Error Recovery

Slide 23–27: khi nào agent tự làm, khi nào hỏi người, khi nào dừng an toàn — và cách đo tất cả.

### Slide 23 Section divider

> Trích slide 
>  "05 — Human-in-the-Loop & Error Recovery. Agent production phải biết khi nào tự làm, 
>  khi nào hỏi người, khi nào dừng an toàn."

Ba chế độ, và **chế độ thứ ba mới là chế độ khó nhất**. "Tự làm" thì mặc định. 
 "Hỏi người" cần một API. "Dừng an toàn" cần bạn đã nghĩ trước về việc *dừng ở đâu thì không để lại 
 hậu quả nửa vời* — đó là thiết kế, không phải thư viện.

### Slide 24 Human-in-the-loop — interrupt và resume

> Trích slide 
>  "draft → INTERRUPT → send/action → END (approve) / edit-reject (quay lại) 
>  Approval trước destructive action; clarification khi thiếu thông tin; escalation khi vượt quyền; 
>  review trước publish. 
>  Graph pause, lưu state; human trả lời; graph resume từ đúng vị trí với state mới. 
>  Role-play - 6 phút: Một bạn đóng agent, một bạn đóng reviewer. Reviewer chỉ được approve 
>  khi state có đủ evidence. "

_Sơ đồ: Vòng human-in-the-loop với interrupt và resume - Graph soạn đề xuất rồi dừng lại tại nút interrupt để chờ người duyệt. Nếu duyệt thì hành động được thực thi và kết thúc; nếu sửa hoặc từ chối thì quay lại bước soạn. Nút interrupt mang theo hành động đề xuất, mức rủi ro và bằng chứng._

Hình 5 — Interrupt và resume (slide 24).

ý nghĩa

#### Bốn tình huống cần HITL — và chúng khác nhau về bản chất

| Tình huống | Người làm gì | Nếu không có người thì hệ nên làm gì |
| --- | --- | --- |
| Approval trước destructive action | Duyệt / từ chối | Dừng — không được tự làm |
| Clarification khi thiếu thông tin | Cung cấp dữ liệu còn thiếu | Hỏi lại, và sau N lần thì escalate |
| Escalation khi vượt quyền | Tiếp quản hoàn toàn | Bàn giao, không cố tự xử |
| Review trước publish | Sửa nội dung | Giữ ở trạng thái nháp |

escalation

- Approval: graph dừng và chờ, rồi tiếp tục với quyết định của người. 
 Cần interrupt() + Command(resume=...).
- Escalation: graph bàn giao và kết thúc. Người tiếp quản ngoài hệ thống. 
 Chỉ cần một node cuối và một field requires_human.

requires_human: bool

đúng

Khi nào bạn sẽ cần interrupt thật:

duyệt

sau khi

### Slide 25 HITL code skeleton

> Trích slide 
>  from langgraph.types import interrupt, Command 
>  def approval_node(state: AgentState) -> dict: 
>  decision = interrupt({"action": state["proposed_action"], "risk": state["risk_level"], 
>  "evidence": state["tool_results"]}) 
>  return {"approval": decision} 
>  # Resume later: compiled.invoke(Command(resume={"approved": True}), config) 
>  Chấm điểm lab: ■ Có interrupt object rõ ràng. ■ Có route approve/reject/edit. 
>  ■ Report ghi số lần approval và kết quả. ■ Không execute destructive action khi chưa approve.

Đoạn code này ngắn nhưng có một điều rất phản trực giác: **`interrupt()` không 
 "trả về" theo nghĩa thông thường**. Khi graph chạy tới đó lần đầu, nó *ném ra* để 
 dừng graph lại. Khi bạn resume, node **chạy lại từ đầu** và lần này `interrupt()` mới trả về giá trị bạn truyền vào.

interrupt()

```text
# ✕ SAI — gửi email sẽ chạy 2 lần (một lần trước interrupt, một lần khi resume)
def approval_node(state):
    send_notification_to_reviewer(...)        # side effect trước interrupt
    decision = interrupt({...})
    return {"approval": decision}

# ✓ ĐÚNG — node approval chỉ dừng và nhận quyết định, không làm gì khác
def approval_node(state):
    decision = interrupt({
        "action":   state["proposed_action"],
        "risk":     state["risk_level"],
        "evidence": state["tool_results"],
    })
    return {"approval": decision}
```

slide 16

idempotent

"Không execute destructive action khi chưa approve."

nhị phân

Cách chứng minh trong 3 phút:

rồi dừng luôn

assert spy.call_count == 0

### Slide 26 Error recovery — retry, fallback, dead-letter

> Trích slide 
>  "llm/tool call → error? → no: next / retry → max retry → fallback → dead-letter (fail) 
>  3 tầng: 1. Retry với backoff và max attempts. 2. Fallback model/tool. 3. Dead-letter để manual review. 
>  Lưu ý: Node retry phải idempotent. Gửi email, charge payment, update database cần idempotency key. "

_Sơ đồ: Ba tầng xử lý lỗi: retry, fallback, dead-letter - Lỗi từ LLM hoặc tool đi qua ba tầng nối tiếp. Tầng một retry có backoff và giới hạn số lần. Nếu vẫn lỗi, tầng hai đổi sang model hoặc tool dự phòng. Nếu vẫn lỗi, tầng ba đưa task vào hàng đợi dead-letter để người xem lại. Hai tầng đầu thành công thì workflow chạy tiếp._

Hình 6 — Ba tầng error recovery (slide 26).

thoát khỏi luồng tự động

timeout + retry

circuit breaker

dead letter queue

fallback

ngay trong phiên đó

#### Tương tác Ngân sách retry — thêm lần thử có đáng không?

Retry cải thiện tỷ lệ thành công theo hàm mũ giảm dần, nhưng làm độ trễ xấu nhất 
 tăng theo hàm mũ tăng. Hai đường cong ngược chiều nhau — và điểm hợp lý thường sớm hơn bạn nghĩ.

Tool lỗi tạm thời **20%** mỗi lần gọi, mỗi lần gọi mất **2 giây**, 
 backoff bắt đầu từ **1 giây**. Bạn đang để `max_attempts = 3`. 
 Sếp bảo "tăng lên 6 cho chắc". Đoán trước:

1. Tỷ lệ thành công tăng thêm bao nhiêu điểm phần trăm?
2. Độ trễ xấu nhất tăng từ bao nhiêu lên bao nhiêu?

#### Kéo max_attempts 3 → 6 rồi mở

**① Từ 99,20% lên 99,99%** — 
 thêm đúng **0,79 điểm phần trăm**.

**② Độ trễ xấu nhất từ 9 giây lên 43 giây** — 
 gấp gần **5 lần**.

**Vì sao hai con số lệch nhau đến vậy:** tỷ lệ thất bại giảm theo *luỹ thừa của p* (0,2³ = 0,8% → 0,2⁶ = 0,006%) nên phần cải thiện cạn rất nhanh. 
 Còn backoff *gấp đôi mỗi lần*, nên tổng thời gian chờ tăng theo 2ⁿ. 
 Một bên hội tụ, một bên bùng nổ.

**Bài học mang đi:** câu hỏi đúng không phải "retry mấy lần cho chắc?" mà là **"người dùng chờ được bao lâu?"** Chọn ngân sách thời gian trước 
 (ví dụ 10 giây), rồi suy ngược ra số lần retry vừa vào ngân sách đó. 
 Thêm lần thứ 6 không phải là cẩn thận — nó là bắt người dùng chờ 43 giây để cứu 6 request trên 100.000.

*Thử thêm:* kéo tỷ lệ lỗi lên 50%. Bây giờ retry *thật sự* đáng — 
 từ 1 lần lên 3 lần đưa thành công từ 50% lên 87,5%. **Giá trị của retry phụ thuộc 
 vào độ tin cậy của thứ bạn đang gọi**: dịch vụ càng ổn định thì retry càng ít đáng, 
 và ngược lại. Đo tỷ lệ lỗi thật trước khi chọn con số.

- **Control - Tỷ lệ lỗi mỗi lần gọi 20%**: min `1`, max `60`, step `1`, default `20`

- **Control - max_attempts 3**: min `1`, max `8`, step `1`, default `3`

- **Control - Độ trễ mỗi lần gọi 2,0s**: min `5`, max `100`, step `5`, default `20`

- **Control - Backoff khởi điểm 1,0s**: min `0`, max `80`, step `5`, default `10`

Tỷ lệ thành công

—

—

Rơi vào dead-letter

—

cần người xem lại

Số lần gọi trung bình

—

= hệ số nhân chi phí

Độ trễ xấu nhất

—

gọi + chờ backoff, khi dùng hết lượt

Tỷ lệ thành công Rơi vào dead-letter max_attempts hiện tại

#### Xem dạng bảng



#### Công thức & giả định

- Mỗi lần thử thất bại độc lập với xác suất p ⇒ thành công sau N lần = 1 − p N.
- Giả định "độc lập" là giả định mạnh nhất ở đây. Nếu dịch vụ đang sập hẳn, 
 các lần thử tương quan hoàn toàn — retry không cứu được gì và bạn cần circuit breaker. 
 Retry chỉ hợp lý cho lỗi thoáng qua.
- Backoff nhân đôi: chờ b, 2b, 4b… ⇒ tổng chờ khi dùng hết N lượt = b·(2 N−1 − 1).
- Số lần gọi trung bình = Σ k·p k−1 (1−p) cộng N·p N — cũng là hệ số nhân chi phí token.
- Bỏ qua jitter (thực tế nên có, để tránh nhiều client retry đồng loạt).

### Slide 27 Observability — trace, metric, report

> Trích slide 
>  Metrics bắt buộc: ■ task success rate; ■ nodes visited; ■ retry count; 
>  ■ interrupt count; ■ state validation errors; ■ latency per run; ■ resume success. 
>  Report bắt buộc: ■ architecture diagram; ■ state schema; ■ test cases; 
>  ■ metrics table; ■ failure analysis; ■ improvement plan. 
>  Checkpoint: Lab sẽ chấm bằng cả code chạy được, metrics JSON và report markdown.

Bảy metric này không phải danh sách tuỳ chọn — chúng là **đầu ra bắt buộc** của lab. 
 Điều tốt là *tất cả* đều suy ra được từ `get_state_history()`, nên bạn viết một hàm 
 là xong cả bảy:

| Metric | Lấy từ đâu | Nói lên điều gì |
| --- | --- | --- |
| task_success_rate | Đếm run có status == "done" | Chỉ số tổng quát — nhưng che giấu nhiều thứ, đừng chỉ nhìn nó |
| nodes_visited | Đếm writes trong history | Bất thường cao ⇒ đang có vòng lặp không cần thiết |
| retry_count | Field attempt ở checkpoint cuối | Độ tin cậy của tool/model bên dưới |
| interrupt_count | Số checkpoint có next trỏ tới node approval | Bao nhiêu việc thật sự cần người — cơ sở để tính chi phí vận hành |
| state_validation_errors | Đếm lỗi schema khi ghi state | Dấu hiệu node trả về sai kiểu — thường là bug thật |
| latency_per_run | Thời gian giữa checkpoint đầu và cuối | Nhớ tách phần chờ người ra khỏi phần máy chạy |
| resume_success | Tỷ lệ resume thành công sau khi kill | Bằng chứng duy nhất cho 15 điểm persistence |

latency_per_run

vô nghĩa

Tách làm hai:

machine_latency

wall_clock_latency

đã làm

failure analysis

đã hỏng

triệu chứng quan sát được

nguyên nhân gốc

đã sửa thế nào hoặc vì sao chưa sửa

#### Ô kiểm tra — Chương 5

**1.** Vì sao mọi code đứng *trước* `interrupt()` trong một node 
 sẽ chạy hai lần? Hiểu

#### Đáp án

Vì `interrupt()` không "tạm dừng ở giữa hàm" như trực giác gợi ý. 
 Lần đầu chạy tới đó, nó **ném ra để dừng graph**. Khi bạn resume, 
 LangGraph **chạy lại node từ đầu**, và lần này `interrupt()` trả về 
 giá trị bạn truyền qua `Command(resume=...)`.

**Hệ quả thực dụng:** node có interrupt phải *chỉ* làm việc dừng và nhận 
 quyết định. Mọi side effect (gửi thông báo cho reviewer, ghi log nghiệp vụ, tạo bản ghi) 
 phải nằm ở node khác — nếu không chúng chạy đúng hai lần.

**2.** Tool của bạn lỗi 5% mỗi lần gọi. Đồng nghiệp đề xuất tăng `max_attempts` từ 3 lên 6. Phản hồi thế nào? Đánh giá

#### Đáp án

Với p = 5%: thành công sau 3 lần đã là **99,9875%**. Sau 6 lần là **99,999998%** — cải thiện khoảng *0,0125 điểm phần trăm*.

Đổi lại, độ trễ xấu nhất tăng từ ~9 giây lên ~43 giây (với backoff khởi điểm 1 giây).

**Câu trả lời:** "Ở tỷ lệ lỗi 5%, retry lần 4–6 gần như không cứu thêm gì, 
 nhưng làm đuôi latency xấu gấp 5 lần. Nếu lo về 0,01% còn lại, tầng đúng để giải quyết là *fallback* hoặc *dead-letter*, chứ không phải thêm retry."

*Điểm cộng nếu bạn nói thêm:* nếu tool đang **sập hẳn** chứ không lỗi thoáng qua, 
 giả định "các lần thử độc lập" sai hoàn toàn — retry không giúp gì và cần circuit breaker.

**3.** Graph của bạn dừng ở interrupt chờ người 4 phút. `latency_per_run` báo 4 phút. Vấn đề ở đâu? Phân tích

#### Đáp án

Metric đang trộn **thời gian máy chạy** với **thời gian người phản hồi** — 
 hai đại lượng có bản chất khác nhau và dùng cho hai mục đích khác nhau.

Hậu quả: bạn không thể dùng con số này để tối ưu kỹ thuật (nó bị nhiễu bởi tốc độ của con người), 
 và cũng không thể dùng để thiết kế SLA (nó lẫn phần máy).

**Sửa:** tách `machine_latency` (tổng thời gian node thật sự chạy) và `wall_clock_latency` (tính cả chờ người). Đồng thời thêm `time_waiting_for_human` như một metric riêng — nó chính là chỉ số vận hành 
 cho biết đội ngũ duyệt có đang là nút thắt không.

---

<!-- chiron-source-span: {"source_span_id":"9d5ba736-eab6-5791-b347-0b825b235e91","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Lab 4 giờ","source_file":"track-3-day-23.html"},"checksum":"96dd180cb6c79ca99273920ffa38234738fa2bfdacb51da9fea2aa60b4f13258"} -->

## 06 Lab 4 giờ

Slide 28–32: mục tiêu, mốc thời gian, rubric 100 điểm và format demo.

### Slide 28 Section divider

> Trích slide 
>  "06 — Lab 4 giờ. Xây LangGraph workflow cho agent xử lý yêu cầu support có routing, HITL, 
>  retry và metric report."

### Slide 29 Lab objective

> Trích slide 
>  "■ Hoàn thiện production skeleton repo: state schema, nodes, graph wiring, persistence adapter. 
>  ■ Chạy 6 test scenarios: simple, tool, missing-info, risky-action, transient-error, max-error. 
>  ■ Xuất file metrics JSON và report markdown theo template. 
>  ■ Học viên giỏi hoàn thành extension: crash-resume, time-travel debug hoặc parallel fan-out. 
>  Skeleton đã có vùng TODO(student). Không cần viết lại kiến trúc repo; tập trung hoàn thiện 
>  logic và bằng chứng chấm điểm. "

Sáu scenario này được thiết kế để **phủ đúng năm khoảng trống của [slide 9](#s9)**. 
 Đọc chúng như một ma trận kiểm thử, và bạn sẽ biết mỗi test đang chứng minh điều gì:

| Scenario | Chứng minh năng lực gì | Assert quan trọng nhất |
| --- | --- | --- |
| simple | Đường đi cơ bản chạy thông | Kết thúc ở END, final_answer khác None |
| tool | Node gọi tool và ghi kết quả đúng reducer | len(tool_results) đúng như kỳ vọng |
| missing-info | Loop hỏi lại có giới hạn | Số vòng lặp ≤ ngưỡng, không treo |
| risky-action | HITL chặn hành động phá huỷ | spy.call_count == 0 khi chưa approve |
| transient-error | Retry cứu được lỗi thoáng qua | attempt > 1 và cuối cùng thành công |
| max-error | Dead-letter khi hết lượt | status == "dead_letter", không lặp vô hạn |

transient-error

hoạt động

max-error

biết dừng

fail_times

logic trong vùng TODO

bằng chứng

### Slide 30 Lab milestones 4 giờ

> Trích slide 
>  "0-30' Setup repo, chạy tests baseline, đọc state schema → screenshot/tests log · 
>  30-75' Implement core nodes + graph wiring → core tests pass · 
>  75-120' Conditional routing + retry + HITL mock → 6 scenarios run · 
>  120-180' Persistence/checkpoint + crash-resume extension → trace JSON/history · 
>  180-225' Metrics runner + report template → metrics.json + report.md · 
>  225-240' Demo, cleanup, self-assessment → final zip/repo"

Đối chiếu mốc thời gian với [rubric](#s31) cho ra một kết luận quan trọng về **mật độ điểm theo phút**:

| Mốc | Phút | Điểm rubric liên quan | Điểm / phút |
| --- | --- | --- | --- |
| Setup | 30 | ~0 | 0 |
| Core nodes + wiring | 45 | 20 (architecture) | 0,44 |
| Routing + retry + HITL | 45 | 25 (graph behavior) | 0,56 |
| Persistence + crash-resume | 60 | 15 (persistence) | 0,25 |
| Metrics + report | 45 | 35 (metrics 20 + report 15) | 0,78 |
| Demo, cleanup | 15 | 5 (hygiene) | 0,33 |

35 điểm trong 45 phút

cuối

Chiến thuật ngược dòng:

metrics.json

report.md

75–120'

bổ sung

### Slide 31 Scoring rubric

> Trích slide 
>  "Architecture & state — 20 — Typed state, reducer đúng, node nhỏ và testable · 
>  Graph behavior — 25 — Routing đúng, retry có giới hạn, HITL hoạt động · 
>  Persistence & recovery — 15 — Checkpoint, thread id, resume hoặc mock tương đương · 
>  Metrics & tests — 20 — Metrics JSON hợp lệ, 6 scenarios, tests pass · 
>  Report & demo — 15 — Report rõ, failure analysis, diagram/screenshot · 
>  Production hygiene — 5 — README, config, typing, lint, env handling"

Điều đáng chú ý nhất: **55 trên 100 điểm là "bằng chứng", không phải "code chạy được"**. 
 Metrics (20) + Report (15) + Persistence phải chứng minh được (15) + hygiene (5) — tất cả đều là 
 thứ bạn *trình bày*, không phải thứ bạn *viết logic*.

chứng minh cùng một điều

cái bẫy MemorySaver ở slide 20

ghi state ra file JSON sau mỗi bước

#### Tương tác Tự chấm theo rubric codelab — dùng khi còn 30 phút cuối lab

Đây là rubric **của codelab** (7 hạng mục) — bảng thực tế chấm bài nộp, 
 khác với bảng ở slide 31; xem [so sánh ở Bước 1](#lb1). 
 Tick những gì bạn *thật sự đã có bằng chứng*, không phải những gì bạn định làm.

0

##### Architecture & state schema

Typed state đầy đủ, serializable 4

Reducer đúng

4 field bổ sung hợp lý và có consumer rõ ràng 3

Node boundary rõ, không node nào chứa cả workflow 2

##### Graph construction & wiring

Đủ 11 node đúng tên, 8 fixed edge 5

4 conditional edge nối đúng decision table 5

Graph compile với checkpointer truyền vào và chạy được 5

##### LLM integration

Structured-output classifier

Grounded answer sinh từ LLM thật và context thật 7

##### Graph behavior

Route đúng trên cả 7 sample scenario 7

Retry hữu hạn — không cần nâng recursion limit 5

Approval gate chặn tool

finalize

##### Persistence & recovery

thread_id

Dump được state history gắn đúng thread 3

Crash-resume evidence (SQLite, log hai process) 3

##### Metrics & tests

metrics.json

và có nghĩa

Scenario coverage ≥ 6, chạy thật 5

Toàn bộ test pass ở gate cuối 4

##### Report & demo

Kiến trúc + state schema + bảng kết quả 4

Failure analysis ≥ 2 mode

Improvement plan có ưu tiên và lý do 2

Đã có bằng chứng Còn thiếu

#### Bộ tiêu chí phụ này ở đâu ra

- Sáu nhóm và tổng điểm mỗi nhóm lấy nguyên văn từ slide 31.
- Các tiêu chí con là diễn giải của tài liệu này, dựa trên yêu cầu rải rác ở 
 slide 22 (thread id, state history), 25 (không execute khi chưa approve), 27 (7 metric, failure analysis) 
 và 29 (6 scenario). Giảng viên có thể chấm chi tiết khác — dùng bộ này để tự kiểm, 
 không phải để tranh luận điểm.
- Nguyên tắc khi tick: chỉ tick khi bạn chỉ được vào một file, một dòng log 
 hoặc một test làm bằng chứng. "Tôi có làm" không tính.

### Slide 32 Demo format cuối lab

> Trích slide 
>  "1. Graph của bạn có những node nào và state field quan trọng nhất là gì? 
>  2. Một test case đi qua route nào? Có retry/interrupt không? 
>  3. Metrics JSON cho thấy success rate, retry count, interrupt count là bao nhiêu? 
>  4. Bạn đã chứng minh resume/crash recovery thế nào? 
>  5. Nếu thêm 1 ngày, bạn sẽ productionize phần nào trước?"

Năm câu này là **kịch bản demo, hãy tập trả lời trước** — mỗi câu 60–90 giây. 
 Bốn câu đầu kiểm tra bạn có làm không; câu thứ năm kiểm tra bạn có *hiểu* không.

Câu hỏi thật là: *bạn có nhận ra được điểm yếu nhất trong hệ của chính mình không?* Vài hướng trả lời mạnh:

• *"Idempotency cho các node có side effect."* Retry hiện đang an toàn vì tool của em là mock; 
 với tool thật thì `notify` cần idempotency key trước tiên. 
 • *"Đổi từ SQLite sang Postgres saver."* SQLite khoá file nên không chạy được nhiều worker — 
 đây là thứ chặn scale đầu tiên. 
 • *"Thêm `schema_version` và migration."* Hiện checkpoint cũ sẽ vỡ nếu em đổi state schema, 
 nghĩa là chưa deploy được khi có phiên đang chạy. 
 • *"Tách `machine_latency` khỏi thời gian chờ người"* để metric latency có ý nghĩa kỹ thuật.

Điểm chung của bốn câu trên: đều nêu **một rủi ro cụ thể** và **lý do nó là 
 rủi ro lớn nhất**. Câu trả lời yếu thường là "em sẽ thêm nhiều test hơn" — 
 đúng nhưng không cho thấy bạn đã đánh giá gì.

---

<!-- chiron-source-span: {"source_span_id":"ce3fe876-ac61-5568-81cb-df6f885a5205","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Takeaways & tài liệu","source_file":"track-3-day-23.html"},"checksum":"0c6a27f5f80adb9c53534d56b1a2f67317053436271183179d55f284cdb153f7"} -->

## 07 Takeaways & tài liệu

Slide 33–36.

### Slide 33 Section divider

> Trích slide 
>  "07 — Takeaways. LangGraph không chỉ là thư viện orchestration; nó là cách thiết kế agent 
>  như một system có state, audit và recovery."

Câu này đáng đọc lại lần hai. Nó nói rằng giá trị thật của bài học **không nằm ở API** — 
 mà ở việc chuyển cách nghĩ từ *"agent là một chuỗi lời gọi LLM"* sang *"agent là một hệ thống có trạng thái, có nhật ký kiểm toán và có khả năng phục hồi"*. 
 Cách nghĩ đó áp dụng được cho Temporal, Step Functions, Airflow — và sống lâu hơn bất kỳ phiên bản thư viện nào.

### Slide 34 Key Takeaways

> Trích slide 
>  "■ Dùng LCEL cho pipeline tuyến tính; dùng LangGraph khi có loop, conditional route, 
>  persistence hoặc HITL. 
>  ■ State schema và reducer quyết định độ ổn định của graph. 
>  ■ Checkpointing là nền tảng cho HITL, memory, time travel và fault tolerance. 
>  ■ Production agent cần metric, trace và report, không chỉ demo chạy được."

Bốn takeaway, đọc như một chuỗi nhân quả chứ không phải bốn ý rời:

```text
① Chọn đúng công cụ      →  chỉ dùng graph khi thật sự có loop / route / HITL / persistence
        ↓
② State schema + reducer →  nền móng. Sai ở đây thì mọi tầng trên đều lung lay
        ↓
③ Checkpointing          →  mở khoá HITL, time travel, crash recovery — cả ba cùng một cơ chế
        ↓
④ Metric + trace + report→  thứ biến "demo chạy được" thành "hệ thống vận hành được"
```

không có triệu chứng

"field này là ảnh chụp hay nhật ký?"

### Slide 35 References

> Trích slide 
>  "1. LangGraph documentation: Persistence, Human-in-the-loop, Functional API — 
>  docs.langchain.com/oss/python/langgraph 
>  2. LangGraph reference: StateGraph, interrupt, Command, checkpointers — reference.langchain.com 
>  3. LangChain blog/docs examples for agent workflows and deployment — langchain.com"

Thứ tự đọc theo mức độ hoàn vốn cho lab:

1. Persistence (mục 1) — đọc trước tiên. Đây là phần bạn cần cho 15 điểm rubric 
 và là phần dễ làm sai nhất (MemorySaver, thread_id).
2. Human-in-the-loop (mục 1) — đặc biệt phần nói về việc node chạy lại từ đầu 
 khi resume. Đây là hành vi phản trực giác nhất của cả API.
3. Reference: StateGraph, interrupt, Command (mục 2) — 
 tra khi cần chữ ký hàm chính xác, không đọc tuần tự.
4. Mục 3 để sau lab, khi bạn nghĩ tới deploy.

interrupt

Command

requirements.txt

### Slide 36 Hỏi & Đáp

> Trích slide "Hỏi & Đáp"

Ba câu hỏi đáng tự đặt sau buổi học, kèm câu trả lời gọn:

| Câu hỏi | Trả lời gọn |
| --- | --- |
| Khi nào không nên dùng LangGraph? | Prompt đơn lẻ, ETL tuyến tính, không có state, không cần approval/audit (slide 10). Đây là phần lớn công việc thực tế. |
| Khái niệm nào dễ làm hỏng lab nhất? | Reducer — vì nó là khái niệm duy nhất hỏng mà không báo lỗi. |
| Nếu chỉ làm được một extension thì chọn cái nào? | Crash-resume. Nó chứng minh trực tiếp 15 điểm persistence và là thứ khó nói suông nhất — có hoặc không có, log nói hết. |

---

<!-- chiron-source-span: {"source_span_id":"0bb5db35-f099-500d-972c-68f591330e27","locator":{"kind":"html_section","section_id":"lab","order":10,"heading":"🛠 Hướng dẫn Lab từng bước","source_file":"track-3-day-23.html"},"checksum":"6c027d12743fefa1a55fbf25206cd7c1a4b9cae6138aaff527ad7229778e6449"} -->

## 🛠 Hướng dẫn Lab từng bước

Toàn bộ codelab *Day 23 — LangGraph Agentic Orchestration* (240 phút, trung cấp), 
 phân tích và trực quan hoá. Mục tiêu: xây support-ticket agent với typed state, conditional routing, 
 bounded retry, human approval, persistence và metrics kiểm toán được.

Codelab nêu rải rác một loạt **khoảng trống có chủ ý** trong repo. Chúng không phải bug 
 của bạn, nhưng nếu không biết trước thì mỗi cái ăn 15–40 phút. Đây là danh sách đầy đủ:

1. cp.env.example.env KHÔNG nạp biến vào process. 
 pyproject.toml chưa khai báo python-dotenv và không entrypoint nào gọi 
 load_dotenv(). → Bước 4
2. Thứ tự ưu tiên provider là cố định: Gemini → OpenAI → Anthropic. 
 Cài OpenAI không có nghĩa OpenAI được dùng, nếu process còn thấy GEMINI_API_KEY. 
 → Bước 3
3. CHECKPOINTER trong.env.example không được CLI đọc. 
 CLI đọc checkpointer từ configs/lab.yaml. → Bước 12
4. render_report() còn NotImplementedError. 
 run-scenarios gọi nó ở cuối — nên lệnh sẽ fail sau khi đã đốt hết API call. 
 → Bước 13
5. metric_from_state() không đo latency → latency_ms luôn bằng 0. 
 → Bước 14
6. summarize_metrics() luôn đặt resume_success=False, 
 kể cả khi bạn đã dùng checkpointer. → Bước 14
7. interrupt_count đếm event có node == "approval" — 
 nên mock approval bị tính là "interrupt" dù workflow chưa hề pause. → Bước 14
8. nodes_visited là số event, không phải số node. 
 Node không log event thì biến mất; node log hai event bị đếm hai lần. → Bước 14

Bẫy số 4 là bẫy đắt nhất về tiền: bạn chạy đủ 7 scenario qua LLM thật, rồi lệnh crash ở dòng cuối. **Implement `render_report()` trước lần chạy full đầu tiên.**

_Sơ đồ: Timeline 240 phút của lab - Năm giai đoạn nối tiếp trong 240 phút: setup và baseline 20 phút, state và node contract 70 phút, routing và graph wiring 60 phút, persistence và recovery 30 phút, scenarios metrics và report 60 phút._

Hình 7 — Timeline 240 phút.

bằng chứng chấm điểm

code

#### Clone repo và định vị vùng phải sửa

Mục tiêu: biết chính xác phần nào là *contract* (không sửa) và phần nào là *implementation* (phải viết).

```text
git clone https://github.com/VinUni-AI20k/phase2-k3-4-track3-day8-langgraph-agent
cd phase2-k3-4-track3-day8-langgraph-agent
git status
rg -n "TODO\(student\)|NotImplementedError" src tests docs README.md
```

Lệnh `rg` cuối cùng là lệnh quan trọng nhất — nó liệt kê **toàn bộ bề mặt công việc** của bạn trong một lần. Chạy nó trước khi mở bất kỳ file nào.

| File | Vai trò | Bạn làm gì |
| --- | --- | --- |
| state.py | Route enum, AgentState, Scenario, initial state, audit event | Bổ sung 4 field; kiểm reducer và tính serializable |
| nodes.py | 1 node mẫu + 10 node TODO | Implement theo partial-update contract, không mutate input |
| routing.py | 4 conditional routing function | Implement đúng decision table và tên node |
| graph.py | StateGraph builder | Đăng ký 11 node, nối edge, compile với checkpointer |
| llm.py | Factory chọn Gemini / OpenAI / Anthropic | Dùng lại — chỉ cần bảo đảm env thật sự được nạp |
| persistence.py | Memory checkpointer + extension durable | Memory cho core; SQLite/Postgres cho extension |
| metrics.py | Schema và tổng hợp metrics | Hiểu metric nào đo thật, metric nào là default |
| report.py | Renderer Markdown | Implement TRƯỚC khi chạy full scenario |
| tests/ | Public contract | Đọc và chạy — không sửa test để che lỗi |
| data/sample/scenarios.jsonl | 7 scenario công khai | Dùng để kiểm coverage, không biến thành lookup table |

Ranh giới không được vượt

`configs/grading.yaml` trỏ tới **hidden grading data không được phân phối**. 
 Không chạy config này, không tìm, không tạo lại, không thêm bất kỳ `data/grading/` nào 
 vào bài nộp.

Hidden scenarios kiểm tra khả năng **tổng quát hoá**. Nghĩa là mọi thủ thuật 
 "khớp đúng 7 câu mẫu" — hard-code scenario ID, so khớp exact query, bảng tra cứu — 
 sẽ pass sample và *fail hidden*. Đây là thiết kế, không phải rủi ro.

Kết quả mong đợi

#### Hiểu target graph và rubric trước khi gõ code

Mục tiêu: có một sơ đồ duy nhất để đối chiếu khi wiring, và biết mỗi quyết định 
 kỹ thuật sẽ được chấm ở hạng mục nào.

route_after_classify

route_after_evaluate

route_after_retry

route_after_approval

KHÔNG phải bốn node

hàm quyết định cạnh

11 node

add_conditional_edges("classify", route_after_classify, {...})

tham số

add_node

#### Quy tắc ưu tiên phân loại — phần dễ mất điểm nhất của classifier

```text
risky  >  tool  >  missing_info  >  error  >  simple
```

Khi một query có nhiều tín hiệu, **tín hiệu ưu tiên cao hơn thắng**. 
 Ví dụ của codelab: yêu cầu *vừa tra cứu vừa hoàn tiền* vẫn là `risky` — 
 vì side effect cần approval quan trọng hơn lookup.

mức độ không thể hoàn tác của hậu quả

thực hiện side effect mà bỏ qua approval gate

simple

tường minh

#### Hai rubric khác nhau — dùng cái nào?

Slide 31 và codelab đưa ra **hai bảng rubric khác nhau**. Codelab là bảng 
 thực tế chấm bài nộp:

| Hạng mục | Codelab | Slide 31 | Khác biệt đáng chú ý |
| --- | --- | --- | --- |
| Architecture & state | 15 | 20 | Codelab tách "wiring" ra riêng |
| Graph construction & wiring | 15 | — | Chỉ có ở codelab |
| LLM integration | 15 | — | Chỉ có ở codelab — structured output + grounded answer |
| Graph behavior | 20 | 25 | Vẫn là hạng mục nặng nhất |
| Persistence & recovery | 10 | 15 | Codelab hạ trọng số |
| Metrics & tests | 15 | 20 | — |
| Report & demo | 10 | 15 | — |
| Production hygiene | — | 5 | Chỉ có ở slide |
| Tổng | 100 | 100 |  |

structured-output classifier và grounded answer bằng LLM thật

mất trọn 15 điểm

tự chấm tương tác

Kết quả mong đợi

#### Tạo môi trường đa nền tảng

Mục tiêu: Python 3.11+, editable install trong `.venv`, và **một interpreter duy nhất** cho cả cài đặt lẫn chạy test.

macOS / Linux / WSL

Windows PowerShell

```text
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev,openai]"
cp .env.example .env
```

```text
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,openai]"
Copy-Item .env.example .env
```

Hai block trên dùng OpenAI làm ví dụ. Nếu chọn Gemini hoặc Anthropic, thay extra tương ứng ở [Bước 3](#lb3) — **không cần cài cả ba provider**.

#### Kiểm tra bắt buộc sau khi activate

```text
python -c "import sys; print(sys.executable)"
python -c "import langgraph, pydantic; print('core imports: ok')"
```

Lỗi môi trường phổ biến nhất

Nếu lệnh đầu **không** in ra đường dẫn nằm trong `.venv`, 
 dừng lại và activate lại *trước khi* cài package.

Triệu chứng khi sai: `pip install` báo thành công, nhưng `pytest` vẫn `ModuleNotFoundError`. Nguyên nhân: bạn cài bằng interpreter A và chạy bằng interpreter B. 
 Đây là 20 phút bị mất phổ biến nhất trong mọi lab Python.

Kết quả mong đợi

sys.executable

.venv

#### Chọn đúng MỘT provider

Mục tiêu: một provider package, biết model nào sẽ chạy, và không vô tình gửi request 
 sang provider khác.

| Provider | Extra cài đặt | Biến bắt buộc | Model mặc định | Ưu tiên |
| --- | --- | --- | --- | --- |
| Gemini | ".[dev,google]" | GEMINI_API_KEY | gemini-2.5-flash | 1 |
| OpenAI | ".[dev,openai]" | OPENAI_API_KEY | gpt-4o-mini | 2 |
| Anthropic | ".[dev,anthropic]" | ANTHROPIC_API_KEY | claude-sonnet-4-20250514 | 3 |

Bẫy 2 — "đã cài OpenAI" ≠ "đang dùng OpenAI"

`get_llm()` chọn provider theo **thứ tự cố định**: 
 Gemini → OpenAI → Anthropic. Nó chọn cái *đầu tiên có key*, không quan tâm bạn cài gì.

Nghĩa là: nếu shell của bạn còn `GEMINI_API_KEY` từ một lab trước, 
 mọi request sẽ đi Gemini — kể cả khi bạn vừa cài `openai` và đặt `OPENAI_API_KEY`. Bạn sẽ debug sai chỗ, hoặc tốn quota nhầm tài khoản.

**Cách an toàn nhất:** chỉ expose key của provider đã chọn. 
 Xoá các key khác khỏi process trước khi chạy live.

`LLM_MODEL` có thể override model mặc định. Hãy chọn model **hỗ trợ structured output** theo pattern mà implementation của bạn dùng. Classifier và answer nên dùng *cùng một factory* để việc đổi provider không làm thay đổi graph contract.

Kết quả mong đợi

#### Nạp secret vào process — khoảng trống lớn nhất của starter

Mục tiêu: hiểu vì sao `cp.env.example.env` **chưa đủ**, 
 và chọn một trong hai cách hợp lệ.

Bẫy 1 — bẫy tốn thời gian nhất của cả lab

`llm.py` gọi `os.getenv()`. Nhưng:

• `pyproject.toml` **chưa khai báo** `python-dotenv`; 
 • **không entrypoint nào** gọi `load_dotenv()`.

Nên `cp.env.example.env` chỉ *tạo ra một file*. Nó không làm các biến 
 trong file đó xuất hiện trong Python process. Triệu chứng: bạn thấy file `.env` có key, 
 nhưng code vẫn báo thiếu API key — và bạn đi kiểm tra key có đúng không, thay vì kiểm tra 
 nó có được *nạp* không.

#### Cách A — nạp file bằng python-dotenv

Thêm `python-dotenv` vào dependency của project, rồi gọi **đúng một lần** trước khi factory đọc biến môi trường (ở CLI entrypoint hoặc graph/LLM factory):

```text
from dotenv import load_dotenv

load_dotenv()   # gọi MỘT lần, KHÔNG gọi lại trong từng node
```

#### Cách B — inject secret vào process

Đặt biến bằng shell profile, cấu hình Run/Debug của IDE, CI secret hoặc secret manager. 
 Không cần `python-dotenv`; điều kiện là process chạy pytest/CLI *thật sự* nhận được biến.

#### Kiểm tra an toàn — không in secret, không gọi API

```text
python -c "import os; keys=('GEMINI_API_KEY','OPENAI_API_KEY','ANTHROPIC_API_KEY'); print(next((k for k in keys if os.getenv(k)), 'NONE'))"
```

| Kết quả | Nghĩa là | Làm gì |
| --- | --- | --- |
| NONE | .env chưa được load hoặc secret chưa inject | Quay lại cách A hoặc B |
| Khác provider dự kiến | Có key thừa với ưu tiên cao hơn | Bỏ key không dùng khỏi process |
| Đúng provider đã chọn | ✓ Sẵn sàng | Đi tiếp |

Git history

không

Kết quả mong đợi

.env

#### Chạy baseline và phân loại expected failure

Mục tiêu: phân biệt *lỗi scaffold có chủ ý* với *lỗi môi trường* — 
 và không sửa test để tạo màu xanh giả.

```text
python -m pytest tests/test_state.py tests/test_metrics.py -q
python -m pytest tests/test_routing.py -q
python -m pytest tests/test_graph_smoke.py -q
```

Chạy **từng nhóm riêng**, không chạy gộp — để không nhầm nguyên nhân.

| Nhóm | Trạng thái hợp lý ở baseline | Diễn giải |
| --- | --- | --- |
| State + metrics | PASS | Starter đã có initial state, schema metrics và tổng hợp cơ bản |
| Routing | FAIL | NotImplementedError tại 4 routing function — expected failure, không phải lý do sửa test |
| Graph smoke | SKIP hoặc FAIL | Skip nếu thiếu API key; nếu đủ dependency/key thì fail tại TODO |

pass

fail

skip

nguyên nhân

sau khi

request và chi phí thật

#### Ba dấu hiệu là lỗi môi trường, phải sửa trước khi viết logic

1. ModuleNotFoundError cho package core hoặc provider đã chọn
2. Python executable không nằm trong.venv
3. Key check trả NONE dù bạn đang chuẩn bị chạy live smoke test

Kết quả mong đợi

#### Thiết kế AgentState và reducers

Mục tiêu: state lean, serializable, đủ cho routing + audit + metrics + recovery cùng đọc — 
 và **không node nào mutate input**.

`AgentState` là `TypedDict(total=False)`: node chỉ cần trả các field nó thay đổi. 
 Bảng dưới đây gộp 12 field có sẵn và 4 field bạn phải bổ sung, tô theo reducer:

| Field | Reducer | Ý nghĩa | Ai đọc |
| --- | --- | --- | --- |
| messages | append | Dấu vết hội thoại / tóm tắt xử lý | Report, debug |
| tool_results | append | Kết quả tool theo thứ tự thời gian | evaluate, answer |
| errors | append | Lỗi / failure note theo thứ tự | Failure analysis, metrics |
| events | append | Audit event chuẩn hoá của từng node | Toàn bộ metrics |
| thread_id | overwrite | Khoá execution thread cho checkpointer | Checkpointer |
| scenario_id | overwrite | ID cho metrics — không dùng để ra quyết định | Metrics |
| query | overwrite | Ticket text đã normalize | classify, tool, answer |
| route | overwrite | Route phân loại ban đầu | route_after_classify, metrics |
| risk_level | overwrite | Mức rủi ro phục vụ audit/prompt | risky_action, report |
| attempt | overwrite | Số lần đã đi qua retry node | route_after_retry, tool |
| max_attempts | overwrite | Retry bound — không tăng trong loop | route_after_retry |
| final_answer | overwrite | Output cuối | finalize, metrics |
| evaluation_result (thêm) | overwrite | success hoặc needs_retry | route_after_evaluate |
| pending_question (thêm) | overwrite | Câu hỏi clarification hiện tại | Output, success metric |
| proposed_action (thêm) | overwrite | Action đang chờ duyệt | approval, report/audit |
| approval (thêm) | overwrite | Mapping serializable theo ApprovalDecision | route_after_approval, answer, metrics |

add

"ảnh chụp hay nhật ký?"

slide 15

#### Contract đúng — và cái sai trông giống hệt cái đúng

```text
đọc state hiện tại
   → tính giá trị mới trong local variables
   → trả partial update dict
   → để LangGraph reducer merge update vào state
```

Anti-pattern: mutate rồi trả lại cả list

```text
# ✕ SAI — vừa mutate input, vừa có nguy cơ nhân đôi dữ liệu
def bad_node(state):
    state["events"].append(make_event(...))   # mutate input state
    return {"events": state["events"]}        # reducer add sẽ NỐI cả list vào lần nữa

# ✓ ĐÚNG — trả đúng phần mới, để reducer làm việc của nó
def good_node(state):
    return {"events": [make_event("classify", "completed", "...")]}
```

Cái sai không ném exception. Nó chỉ làm `events` phình lên theo cấp số nhân, 
 và `nodes_visited` (vốn đếm event) trở nên vô nghĩa.

route

Route

dead_letter

done

metric_from_state()

state["route"]

actual input route

finalize

route = "done"

dead_letter

route = "dead_letter"

route mismatch

Cách đúng:

finalize event

route

classify

`make_event()` tạo cùng một shape gồm `node`, event type, message, latency và 
 metadata. Mỗi node nên trả `events: [make_event(...)]` — nhờ vậy metrics và report 
 không phải đoán schema riêng của từng node.

Kết quả mong đợi

route

#### Implement 11 node theo dependency order

Mục tiêu: mỗi checkpoint chỉ phụ thuộc phần đã có. `intake` đã là 
 implementation mẫu; 10 node còn lại là `TODO(student)`.

state + reducer

classify

clarify · risky_action · approval

tool · evaluate · retry · dead_letter

answer

finalize + audit trail

Hai node tô cam là hai node **bắt buộc dùng LLM thật** — chúng gánh trọn 
 15 điểm "LLM integration" của rubric.

#### intake — node mẫu, đã có sẵn 1 / 11

**Đọc**

: raw query

**Ghi**

: query đã strip, một message append, một event append

**Event**

: make_event("intake", "completed",...)

**Failure**

: Input rỗng khi graph bị gọi ngoài Scenario validator; hoặc vô tình trả lại toàn bộ list cũ

**Checkpoint**

: Giữ node mẫu chạy qua tests/test_state.py; dùng nó làm chuẩn partial update cho 10 node còn lại

#### classify — LLM bắt buộc 2 / 11

**Đọc**

: query — không đọc scenario_id để quyết định route

**Ghi**

: route, risk_level, event. Khi LLM lỗi: ghi error/event hoặc fallback có chủ đích và audit được

**Event**

: Route được chọn, risk level, trạng thái structured validation. Không log secret hay toàn bộ sensitive prompt

**Failure**

: Keyword-only classifier · raw text parsing không validate · route ngoài enum · không áp dụng priority

**Checkpoint**

: 5 route hợp lệ · risky > tool > missing_info > error > simple · unseen wording vẫn phân loại được

```text
định nghĩa schema với route thuộc năm giá trị cho phép
prompt := mô tả intent + priority + query, KHÔNG có scenario ID
decision := get_llm().with_structured_output(schema).invoke(prompt)
validate decision
return partial update route + risk_level + event
```

`.with_structured_output()` hoặc contract tương đương là **bắt buộc** cho submission chính. Fallback heuristic chỉ được là failure-handling 
 có log rõ — nó không thay thế đường LLM chính.

#### clarify 3 / 11

**Đọc**

: query; trên nhánh rejected có thể đọc approval.comment và proposed_action

**Ghi**

: overwrite pending_question và final_answer bằng một câu hỏi cụ thể, append event

**Event**

: Clarification requested, kèm nguyên nhân: missing info hay rejection

**Failure**

: Hỏi lại quá chung chung · để cả hai output rỗng · vô tình tiếp tục gọi tool

**Checkpoint**

: Cả missing-info route lẫn rejected approval đều kết thúc bằng câu hỏi hành động được, rồi đi finalize

#### risky_action 4 / 11

**Đọc**

: query, risk_level và context cần để mô tả side effect

**Ghi**

: overwrite proposed_action, append event

**Event**

: Action proposed và lý do cần review

**Failure**

: Thực thi tool/side effect ngay trong node · tạo action không liên hệ query

**Checkpoint**

: Sau node này chưa có tool result mới. Output chỉ là đề xuất chờ duyệt

#### approval 5 / 11

**Đọc**

: proposed_action

**Ghi**

: overwrite approval bằng mapping có approved, reviewer, comment; append event

**Event**

: Approval observed, kèm status approved/rejected

**Failure**

: Sai shape · thiếu decision · gọi tool trong approval node · khiến CI chờ input vô hạn

**Checkpoint**

: Mặc định mock approved=True để test/CI không bị block. Real interrupt() chỉ làm ở extension

Xem [slide 25](#s25): nếu dùng `interrupt()` thật ở core, 
 test có thể treo hoặc cần resume command mà CI không cung cấp.

#### tool 6 / 11

**Đọc**

: route, attempt, query; với risky route còn phải dựa trên action đã được approval

**Ghi**

: Append đúng một latest result vào tool_results, append event; có thể append error khi tool thật sự fail

**Event**

: Tool completed/failed, attempt hiện tại, metadata đủ audit nhưng không chứa secret

**Failure**

: Thực thi risky side effect trước approval · hard-code scenario ID · replace toàn bộ result history

**Checkpoint**

: Theo starter: route == "error" và attempt < 2 → sinh result chứa ERROR. Các trường hợp khác → mock success tổng quát

**Quy tắc `attempt < 2` là mấu chốt để hiểu trace của S05:** lần thử đầu (attempt=1) trả ERROR, lần sau (attempt=2) mới thành công. Xem [trình mô phỏng trace](#m-trace).

#### evaluate 7 / 11

**Đọc**

: Phần tử mới nhất của tool_results

**Ghi**

: overwrite evaluation_result thành needs_retry hoặc success, append event

**Event**

: Verdict và lý do ngắn gọn

**Failure**

: Đọc nhầm result đầu tiên · retry khi không có bằng chứng lỗi · để field không tồn tại

**Checkpoint**

: Heuristic nhận diện ERROR là đủ cho base score. LLM-as-judge là extension, không phải blocker

Lỗi "đọc nhầm result đầu tiên" rất dễ mắc: `tool_results[0]` là kết quả 
 của lần thử *đầu tiên* (thường là ERROR), nên retry sẽ chạy mãi. Phải là `tool_results[-1]`.

#### retry 8 / 11

**Đọc**

: attempt, max_attempts, latest failure / tool result

**Ghi**

: overwrite attempt bằng giá trị cũ cộng đúng một, append một error và một event

**Event**

: Retry recorded, attempt mới, retry bound

**Failure**

: Tăng attempt ở cả tool lẫn retry · không tăng attempt · reset về 0 · mutate errors

**Checkpoint**

: Routing dùng giá trị sau increment để quyết định tool hay dead_letter

**Ownership của counter phải rõ:** chỉ *một* node được tăng `attempt`, và tăng đúng một. Hai node cùng tăng → bound sai → hoặc lặp thừa, hoặc dừng sớm.

#### dead_letter 9 / 11

**Đọc**

: attempt, max_attempts, errors, tool results cuối

**Ghi**

: overwrite final_answer bằng thông báo không thể hoàn tất / escalate, append event

**Event**

: Exhausted / dead-letter, kèm retry evidence

**Failure**

: Trả output rỗng · quay lại retry · overwrite route làm metrics sai

**Checkpoint**

: Node chỉ có cạnh cố định tới finalize — không có cạnh trở lại tool

#### answer — LLM bắt buộc 10 / 11

**Đọc**

: query, các tool_results liên quan, approval / proposed_action nếu có

**Ghi**

: overwrite final_answer, append event; ghi error/event nếu model call thất bại

**Event**

: Grounded generation completed/failed; provider/model metadata không nhạy cảm nếu cần

**Failure**

: Hard-code câu trả lời · bỏ qua tool result · tuyên bố action bị từ chối là đã thực hiện · nuốt LLM exception

**Checkpoint**

: Answer được model sinh từ context thực tế, không từ scenario ID hay mapping 7 câu mẫu

```text
context := query + relevant tool results + approval/action context
prompt  := chỉ trả lời dựa trên context; nói rõ giới hạn khi context thiếu
response := get_llm().invoke(prompt)
return final_answer + event
```

#### finalize 11 / 11

**Đọc**

: final_answer hoặc pending_question, và audit state cần để xác nhận completion

**Ghi**

: Append duy nhất một finalize event. Không cần thay classified route

**Event**

: make_event("finalize", "completed", "workflow finished")

**Failure**

: Một branch bypass node · event bị lặp · workflow kết thúc mà không có answer/question

**Checkpoint**

: Graph smoke tìm thấy ít nhất một event có node == "finalize" trên mọi route

một

errors

events

không

Kết quả mong đợi

#### Implement 4 routing function

Mục tiêu: routing chỉ *đọc state và trả tên node đã đăng ký*. 
 Không gọi LLM, không mutate state, không side effect.

| Function | Điều kiện | Node tiếp theo |
| --- | --- | --- |
| route_after_classify | simple | answer |
| tool | tool |  |
| missing_info | clarify |  |
| risky | risky_action |  |
| error | retry — không phải tool |  |
| unknown / missing | answer (default an toàn) |  |
| route_after_evaluate | evaluation_result == "needs_retry" | retry |
| mọi giá trị khác | answer |  |
| route_after_retry | attempt < max_attempts | tool |
| attempt >= max_attempts | dead_letter |  |
| route_after_approval | approval.approved is True | tool |
| false hoặc không được duyệt | clarify |  |

**① Route `error` đi vào `retry`, KHÔNG vào `tool`.** Điều này khiến `attempt` được tăng *trước* lần gọi tool đầu tiên — và đó chính là 
 cơ chế làm S07 ( `max_attempts=1` ) dead-letter ngay lập tức.

**② Unknown route mặc định về `answer`,** không phải raise. 
 Đây là fail-open có chủ đích: một route lạ vẫn cho ra câu trả lời, thay vì làm sập graph.

**③ `route_after_approval` nhận `approval` dạng *mapping*** trong public tests — không phải object. Truy cập bằng `approval.get("approved")`.

```text
route_after_classify := lookup route trong decision table, default answer
route_after_evaluate := retry CHỈ khi verdict là needs_retry
route_after_retry    := tool CHỈ khi attempt còn nhỏ hơn max_attempts
route_after_approval := tool CHỈ khi approved là true
```

Checkpoint ngay sau khi xong:

```text
python -m pytest tests/test_routing.py -q
```

Nếu test báo tên node khác nhau

Sửa **một phía** theo contract public. Đừng thêm alias tuỳ ý trong graph 
 (kiểu `add_node("tool_node",...)` rồi map cả hai tên) — alias làm graph có node thừa 
 và phá tiêu chí "đủ 11 node" của rubric.

Kết quả mong đợi

answer

<

==

>

#### Build và compile StateGraph

Mục tiêu: 11 node đúng tên, 8 fixed edge, 4 conditional edge, 
 compile với **chính** checkpointer mà `build_graph()` nhận.

_Sơ đồ: Khung chính của graph: fan-out từ classify và hội tụ về finalize - START vào intake rồi classify. Classify phân nhánh thành năm hướng: risky đi risky_action rồi approval, error đi retry rồi có thể dead_letter, tool đi tool rồi evaluate, missing_info đi clarify, simple đi thẳng answer. Ba nhánh dead_letter, clarify và answer hội tụ về finalize rồi END._

Hình 8 — Khung chính (fan-out + hội tụ).

classify

dead_letter

clarify

answer

finalize

_Sơ đồ: Hai vòng điều khiển: retry loop và approval gate - Bên trái là vòng retry: từ classify error vào retry, nếu attempt còn nhỏ hơn max thì sang tool rồi evaluate, evaluate cho verdict needs_retry thì quay lại retry, cho success thì sang answer; khi attempt chạm max thì đi dead_letter. Bên phải là cổng approval: risky_action đề xuất, approval quyết định, approved thì sang tool, rejected thì sang clarify._

Hình 9 — Hai vòng điều khiển.

#### 11 tên node đăng ký — tên là contract mà routing function trả về

| Tên đăng ký | Python function | Tên đăng ký | Python function |
| --- | --- | --- | --- |
| intake | intake_node | risky_action | risky_action_node |
| classify | classify_node | approval | approval_node |
| tool | tool_node | retry | retry_or_fallback_node |
| evaluate | evaluate_node | dead_letter | dead_letter_node |
| answer | answer_node | finalize | finalize_node |
| clarify | ask_clarification_node |  |  |

Hai dòng in đậm là hai chỗ **tên node ≠ tên function** — nguồn lỗi `KeyError` phổ biến nhất khi wiring.

#### 8 fixed edge

| Từ | Đến | Từ | Đến |
| --- | --- | --- | --- |
| START | intake | answer | finalize |
| intake | classify | clarify | finalize |
| tool | evaluate | dead_letter | finalize |
| risky_action | approval | finalize | END |

```text
builder := StateGraph(AgentState)
đăng ký 11 node
nối 8 fixed edge
nối 4 conditional edge sau classify, evaluate, retry, approval
compiled := builder.compile(checkpointer=checkpointer)   # checkpointer TRUYỀN VÀO
return compiled
```

Đừng tạo checkpointer bên trong builder

Compile với **chính argument** `checkpointer` mà `build_graph()` nhận. 
 Nếu builder tự tạo một checkpointer mới bên trong, CLI mất quyền quản lý lifecycle và backend từ config — 
 và bạn sẽ thấy state history rỗng dù "đã có checkpointer".

```text
python -m pytest tests/test_graph_smoke.py -q
```

trước

một lần có chủ đích

Kết quả mong đợi

finalize → END

#### Kiểm tra bounded retry và dead-letter

Mục tiêu: retry loop hữu hạn nhờ *ownership của counter rõ ràng* — 
 và **không dựa vào recursion limit** để chữa một graph nối sai.

| State SAU khi retry node chạy | Quyết định | Ý nghĩa |
| --- | --- | --- |
| attempt < max_attempts | tool | Còn quyền thử lại |
| attempt == max_attempts | dead_letter | Đã chạm giới hạn, không gọi tool thêm |
| attempt > max_attempts | dead_letter | Fail closed nếu state bất thường |

**Error route bắt đầu tại `retry`, không đi thẳng vào `tool`.** Đây là chi tiết quyết định hành vi của S07 — dùng trình mô phỏng dưới đây để thấy tại sao.

```text
python -m pytest tests/test_routing.py -k retry -q
```

#### Tương tác Trình mô phỏng trace — 7 scenario mẫu đi qua route nào

Chọn scenario và kéo `max_attempts`. Trace được tính từ chính decision table 
 của repo, nên bạn có thể đối chiếu trực tiếp với event trail thật khi chạy lab.

Scenario **S07_dead_letter** có `max_attempts = 1`, và `attempt` khởi tạo bằng 0. Đoán trước:

1. Node tool có được gọi lần nào không?
2. Trace dài bao nhiêu bước?

#### Chọn S07 rồi mở

**① `tool` KHÔNG bao giờ chạy.** Từ `attempt=0`, lần vào `retry` đầu tiên tạo `attempt=1`. Điều kiện `1 >= 1` đúng ngay, 
 nên `route_after_retry` đưa thẳng tới `dead_letter`.

**② Trace chỉ có 7 bước:** START → intake → classify → retry → dead_letter → finalize → END.

**Vì sao đây là bài kiểm tra tốt:** nó bắt đúng lỗi phổ biến nhất — 
 cho error route đi thẳng vào `tool` thay vì `retry`. Nếu bạn nối sai, 
 S07 sẽ gọi tool ít nhất một lần (hoặc tệ hơn, chạy vô hạn), và bạn thấy ngay trong event trail.

**Bài học mang đi:** *ownership của counter* quyết định tính hữu hạn của loop. 
 Chỉ `retry` được tăng `attempt`, tăng đúng một, và routing đọc giá trị **sau** increment. Nếu `tool` cũng tăng, bound của bạn sai gấp đôi.

*Thử thêm:* chọn **S05_error** rồi kéo `max_attempts` từ 3 xuống 2. 
 Ở max=3 scenario kết thúc bằng `answer`; ở max=2 nó rơi vào `dead_letter`. 
 Cùng một graph, cùng một query — chỉ khác một con số cấu hình. Đó là lý do `max_attempts` phải nằm trong state chứ không hard-code trong node.

S01_simple

S02_tool

S03_missing

S04_risky

S04 — bị từ chối

S05_error

S06_delete

S07_dead_letter

- **Control - max_attempts 3 (S07 luôn = 1)**: min `1`, max `5`, step `1`, default `3`

Expected route

—

—

Số bước

—

tính cả START và END

tool được gọi

—

—

Kết cục

—

—

#### Xem dạng bảng — dùng để đối chiếu với event trail thật



#### Trace được tính từ đâu

- Decision table của Bước 8 — nguyên văn từ codelab.
- Tool contract của Bước 7: route == "error" và 
 attempt < 2 → sinh result chứa ERROR; các trường hợp khác → mock success.
- Evaluate heuristic: thấy ERROR trong result mới nhất → needs_retry.
- max_attempts mặc định trong repo chưa được codelab nêu rõ — 
 đây là lý do nó là thanh trượt. Kiểm giá trị thật trong initial_state() hoặc 
 data/sample/scenarios.jsonl, trừ S07 mà codelab ghi rõ là 1.
- Mock approval mặc định approved=True; nhánh "bị từ chối" là biến thể để bạn kiểm approval gate.

#### Kiểm tra risky action và approval gate

Mục tiêu: approval là **cổng chặn trước side effect**, 
 không phải event ghi nhận sau khi tool đã chạy.

| Quyết định | Trace bắt buộc | Điều KHÔNG được xảy ra |
| --- | --- | --- |
| Approved | risky_action → approval → tool → evaluate → … → finalize | Tool chạy trước approval |
| Rejected | risky_action → approval → clarify → finalize | Tool xuất hiện ở bất kỳ vị trí nào sau rejection |

```text
python -m pytest tests/test_routing.py -k approval -q
```

#### Kiểm tra thứ tự event — bằng chứng mạnh nhất cho hạng mục Graph behavior

```text
approved:  index(approval) < index(tool)
rejected:  approval và clarify tồn tại, tool KHÔNG tồn tại
mọi case:  finalize là event terminal
```

Viết probe bằng **state tổng quát**, không dùng scenario ID. Một test kiểu này 
 chứng minh được điều mà không đoạn văn nào trong report chứng minh nổi.

interrupt()

interrupt()

treo

approved

reviewer

comment

Kết quả mong đợi

chuẩn bị

#### Gắn checkpointer và thread_id

Mục tiêu: checkpointer thật sự được truyền vào compiled graph, mỗi run có thread đúng, 
 và có *evidence* chứ không chỉ mô tả ý định.

```text
configs/lab.yaml
   → CLI đọc checkpointer
   → build_checkpointer(...)
   → build_graph(checkpointer=...)
   → graph.invoke(..., configurable.thread_id)
```

`initial_state()` đã tạo `thread_id`, và `cli.py` đã truyền nó 
 theo đúng shape LangGraph cần:

```text
{"configurable": {"thread_id": state["thread_id"]}}
```

CHECKPOINTER

.env.example

CLI hiện đọc `checkpointer` từ `configs/lab.yaml`, **không** từ 
 biến môi trường. Đặt `CHECKPOINTER=sqlite` trong `.env` sẽ không có tác dụng gì 
 và cũng không báo lỗi.

**Quy tắc chung rút ra:** chỉ tuyên bố một biến cấu hình "hoạt động" sau khi bạn đã 
 nối code đọc nó, hoặc đặt giá trị ở *đúng nguồn mà CLI đang dùng*.

| Mức | Trạng thái trong repo | Evidence phù hợp | Sức nặng |
| --- | --- | --- | --- |
| Memory | Có sẵn, default trong configs/lab.yaml | Graph compile với MemorySaver, mỗi run có thread ID, đọc được state history trong cùng process | Yếu |
| SQLite | Extension thực tế | State/history còn tồn tại sau khi process kết thúc; chứng minh được crash-resume | Mạnh |
| Postgres | Optional qua Docker Compose | Durable multi-process backend | Mạnh |

tối thiểu

mạnh hơn hẳn

thread_id

sqlite

SqliteSaver

checkpoints.db

chỉ khởi động database

database_url

Kết quả mong đợi

thread_id

#### Chạy 7 sample scenario mà không hard-code

Mục tiêu: 7 sample chạy qua một implementation *tổng quát*, 
 có event trail đúng, và không có điều kiện theo exact query hay scenario ID.

| Scenario | Expected route | Approval | Retry signal | Điểm cần quan sát |
| --- | --- | --- | --- | --- |
| S01_simple | simple | — | — | Đường ngắn nhất, 6 bước |
| S02_tool | tool | — | — | Tool → evaluate → answer, không retry |
| S03_missing | missing_info | — | — | pending_question phải có nội dung |
| S04_risky | risky | Có | — | approval xuất hiện trước tool |
| S05_error | error | — | Có | attempt tăng, tool ERROR rồi thành công |
| S06_delete | risky | Có | — | Cùng route với S04 nhưng wording khác — kiểm tổng quát hoá |
| S07_dead_letter | error | — | Có, max_attempts=1 | tool không được gọi lần nào |

render_report()

`run-scenarios` ghi metrics rồi **gọi `write_report()` ở cuối**. 
 Nếu renderer còn `NotImplementedError`, lệnh sẽ chạy hết 7 scenario qua LLM thật — 
 tốn đủ tiền và thời gian — rồi **crash ở dòng cuối** mà không lưu report.

Đây là bẫy đắt nhất về chi phí trong cả lab. Implement renderer trước, kể cả một phiên bản 
 thô chỉ in bảng metrics.

Có Make (macOS / Linux / WSL)

Windows — không có Make

```text
make run-scenarios
```

```text
python -m langgraph_agent_lab.cli run-scenarios --config configs/lab.yaml --output outputs/metrics.json
```

answer

run-scenarios

nhiều request

run-scenarios

#### Đánh giá theo behavior, không theo exact wording

1. Actual route khớp intent và priority ladder
2. Output có final_answer hoặc pending_question
3. Risky scenario quan sát được approval trước tool
4. Error scenario có bounded retry / dead-letter phù hợp
5. Event trail kết thúc ở finalize

configs/grading.yaml

coverage fixture

Kết quả mong đợi

#### Sinh và diễn giải đúng outputs/metrics.json

Mục tiêu: metrics parse đúng schema **và** phản ánh runtime thật — 
 không phải một file toàn giá trị mặc định.

| Field cấp report | Ý nghĩa |
| --- | --- |
| total_scenarios | Số scenario đã chạy — local validator yêu cầu ít nhất 6 |
| success_rate | Tỷ lệ route/output/approval contract đạt |
| avg_nodes_visited | Trung bình số audit event được đếm như node visit |
| total_retries | Tổng event có node == "retry" |
| total_interrupts | Tổng event có node == "approval" |
| resume_success | Bằng chứng resume/replay — helper hiện mặc định False |
| scenario_metrics | Danh sách metric từng scenario |

Mỗi scenario metric gồm: `scenario_id` · `expected_route` · `actual_route` · `success` · `nodes_visited` · `retry_count` · `interrupt_count` · `approval_required` · `approval_observed` · `latency_ms` · `errors`.

| Metric | Scaffold thực tế làm gì | Hệ quả |
| --- | --- | --- |
| latency_ms | metric_from_state() không đo wall-clock | Luôn bằng 0 |
| resume_success | summarize_metrics() luôn đặt False | False kể cả khi bạn đã dùng checkpointer |
| interrupt_count | Đếm event có node == "approval" | Mock approval bị gọi là "interrupt" dù chưa hề pause |
| nodes_visited | Là số event, không phải số node | Node không log event → biến mất. Node log 2 event → đếm 2 lần |
| approval_observed | Chỉ kiểm approval object có tồn tại | Không tự chứng minh tool chạy sau approval |

#### Instrument có chủ đích — đây là chỗ lấy điểm "metrics có nghĩa"

1. Đo time.perf_counter() quanh từng graph.invoke và đưa duration 
 thật vào ScenarioMetric
2. Giữ quy ước một completion event chính cho mỗi node, hoặc tách rõ 
 event count khỏi node count
3. Chỉ đặt resume_success=True khi có evidence replay/resume kiểm chứng được
4. Phân biệt approval-node visit · real interrupt · successful resume, nếu bạn làm HITL extension

```text
make grade-local
# hoặc:
python -m langgraph_agent_lab.cli validate-metrics --metrics outputs/metrics.json
```

latency_ms = 0

retry_count = 0

total_interrupts = 0

mọi

không phải evidence tốt

giải thích trong report

perf_counter

Kết quả mong đợi

outputs/metrics.json

#### Hoàn thiện reports/lab_report.md

Mục tiêu: report là một *lập luận có evidence* nối từ architecture → state/events → 
 metrics → failure/recovery, không phải bản chép lại schema.

| Phần | Phải chứng minh điều gì |
| --- | --- |
| Student | Tên, repo/commit, ngày — không có secret |
| Architecture | 11 node, fixed/conditional edges, termination |
| State schema | Field nào append, field nào overwrite, và lý do |
| Scenario results | Số liệu lấy từ outputs/metrics.json — không chép tay từ nguồn khác |
| Failure analysis | Ít nhất hai failure mode: tín hiệu phát hiện, containment, residual risk |
| Persistence/recovery | Thread ID, state history hoặc crash-resume evidence |
| Extension work | Chỉ ghi phần đã chạy và có proof |
| Improvement plan | Một ưu tiên productionize tiếp theo, và lý do |

**① Tool failure → bounded retry → dead-letter.** Lỗi bắt đầu ở tool (result chứa `ERROR` ) → `evaluate` phát hiện qua 
 verdict `needs_retry` → graph đi `retry`, tăng `attempt` → 
 khi chạm `max_attempts` thì `dead_letter` bảo đảm termination → 
 residual risk: nếu lỗi là *kéo dài* chứ không thoáng qua, retry chỉ làm chậm thêm; 
 cần circuit breaker.

**② Risky action bị chặn/từ chối trước tool.** Lỗi tiềm tàng: side effect không hoàn tác được → phát hiện bằng `route == risky` và `proposed_action` tồn tại mà `tool_results` chưa có → 
 graph dừng ở `approval` → rejected thì đi `clarify` → 
 residual risk: mock approval luôn `approved=True`, nên gate chưa được kiểm thật.

Cấu trúc bắt buộc cho mỗi failure mode: *lỗi bắt đầu ở đâu* → *state/event nào giúp phát hiện* → *graph đi đâu tiếp* → *termination được bảo đảm thế nào* → *còn giới hạn gì*.

run-scenarios

`make run-scenarios` gọi `write_report()` với path từ `configs/lab.yaml` — nên nó **overwrite `reports/lab_report.md`**.

**Thứ tự an toàn:** implement `render_report()` để sinh các bảng metric 
 ổn định *trước*, rồi hoàn thiện phần phân tích/evidence *sau lần scenario run cuối cùng*. 
 Nếu còn chạy lại, bảo đảm renderer giữ được nội dung cần nộp (hoặc viết phân tích vào file riêng 
 rồi merge).

**Không dùng screenshot chứa** API key, environment dump, database credential hay raw secret. 
 Khi trích event/history, chỉ giữ phần cần chứng minh route, retry, approval và recovery.

Kết quả mong đợi

#### Gate cuối và submission checklist

Mục tiêu: mọi gate core pass, output và report khớp nhau, không có secret hay hidden data.

macOS / Linux / WSL

Windows PowerShell

```text
make lint
make typecheck
make test
make run-scenarios
make grade-local
git status
git diff --check
```

```text
python -m ruff check src tests
python -m mypy src
python -m pytest -q
python -m langgraph_agent_lab.cli run-scenarios --config configs/lab.yaml --output outputs/metrics.json
python -m langgraph_agent_lab.cli validate-metrics --metrics outputs/metrics.json
git status
git diff --check
```

run-scenarios

không

run-scenarios

#### Tương tác Submission checklist — 19 mục

Tick những gì bạn *có bằng chứng chỉ ra được* (một file, một dòng log, một test). 
 "Em có làm" không tính.

0

State fields và reducers đúng — 4 list append, còn lại overwrite

TODO(student)

tests/test_routing.py

mười một

structured output

Answer dùng LLM và grounded context thật

Không hard-code sample scenario (không dùng scenario ID hay exact query)

Retry hữu hạn và dead-letter hoạt động — không cần nâng recursion limit

trước

Rejected approval đi clarification, tool không xuất hiện

finalize

thread_id

Có persistence/recovery evidence (state history hoặc crash-resume)

outputs/metrics.json

có nghĩa

reports/lab_report.md

ít nhất hai

Không có secret trong Git (kể cả trong history)

Không có hidden grading data trong bài nộp

Lint, typecheck và tests pass theo gate cuối

git status

giải thích được mọi file đã thay đổi

git diff --check

#### Extensions — chỉ bắt đầu khi core checklist đã đạt

Mục tiêu: hướng tới band điểm cao hơn. Mỗi extension **chỉ có giá trị khi kèm 
 test hoặc evidence trong report**.

| Extension | Làm gì | Evidence tối thiểu | Độ khó |
| --- | --- | --- | --- |
| LLM-as-judge | Thay heuristic evaluator bằng structured verdict có reason, timeout/fallback, cost guard | So sánh verdict judge vs heuristic trên ≥5 case | Trung bình |
| Real HITL interrupt/resume | interrupt() cho approval, nhận decision, resume đúng thread_id | Log hai lần invoke với cùng thread; giữ mock làm default cho CI | Cao |
| SQLite/Postgres recovery | Chứng minh checkpoint durable qua process restart | Log hai process + file DB | Thấp — hiệu quả nhất |
| Time travel | Đọc state history, chọn checkpoint cũ, replay/fork có kiểm soát | Dump history + kết quả replay | Trung bình |
| Parallel fan-out bằng Send() | Nhiều tool độc lập, reducer merge deterministic | Test assert đủ N kết quả — xem mô phỏng reducer | Cao |
| Streamlit UI | Hiển thị ticket, proposed action, approval và event trail | Screenshot không lộ secret | Trung bình |
| Mermaid graph export | Xuất graph thực tế từ compiled graph, đối chiếu target diagram | File mermaid + so sánh | Thấp |

không thể nói suông

Mermaid export

tự kiểm tra

baseline → thay đổi → cách kiểm tra → evidence → giới hạn

âm điểm

Kết quả mong đợi

---

<!-- chiron-source-span: {"source_span_id":"b5985699-4e29-5aa6-8984-a53c6b37cad8","locator":{"kind":"html_section","section_id":"ladder","order":11,"heading":"▤ Luyện kỹ năng cốt lõi: chẩn đoán một graph","source_file":"track-3-day-23.html"},"checksum":"12d4efaa644ff015e269bec486008b67b24d3c69651ef1064c9d224d29c09e37"} -->

## ▤ Luyện kỹ năng cốt lõi: chẩn đoán một graph

Kỹ năng mà rubric, demo và phỏng vấn đều hỏi không phải "LangGraph có API gì" — 
 mà là **"nhìn một graph và chỉ ra chỗ nó sẽ hỏng"**. Ba bài dưới đây giảm dần sự trợ giúp.

① Field này là ảnh chụp hay nhật ký?

② Node này có side effect không?

③ Quyết định này có cần nằm trong checkpoint không?

④ Lỗi ở đây thuộc tầng nào?

⑤ Bằng chứng nào chứng minh nó hoạt động?

không có triệu chứng

#### Node tổng hợp gọi 3 tool song song, nhưng báo cáo cuối chỉ có kết quả của 1 tool

Đọc kỹ cách *lập luận*. Bài 2 và 3 sẽ yêu cầu bạn lặp lại đúng mạch này.

1. Ảnh chụp hay nhật ký? — Nhật ký. tool_results là danh sách những gì 
 đã chạy, cần đủ và đúng thứ tự. Đây chính là nguyên nhân: nó đang dùng reducer mặc định 
 (overwrite), nên ba nhánh song song ghi đè nhau và chỉ một sống sót. 
 Sửa: tool_results: Annotated[list[str], add]. 
 Cách nhận ra sớm: triệu chứng "mất dữ liệu mà không có exception" gần như luôn là reducer.
2. Side effect? — Tuỳ tool. Nếu là tool tra cứu thì không. Nếu có tool ghi dữ liệu 
 thì fan-out + retry sẽ nhân đôi tác động, cần idempotency key. Ở bài này giả định là tool đọc.
3. Cần trong checkpoint? — Có. tool_results là bằng chứng cho 
 failure analysis và cho người duyệt ở bước HITL. Nó phải nằm trong state, không phải biến cục bộ.
4. Tầng lỗi? — Chưa tới tầng nào. Đây không phải lỗi runtime; đây là lỗi 
 thiết kế state. Ba tầng retry/fallback/dead-letter không cứu được, vì không có gì "thất bại" cả.
5. Bằng chứng? — Một test cho fan-out. Chạy graph với 3 tool giả, 
 assert len(state["tool_results"]) == 3. Test này sẽ fail trước khi sửa và 
 pass sau khi sửa — đó là bằng chứng mạnh nhất, và nó vào thẳng mục 
 "Metrics & tests" của rubric.

tool_results

Annotated[list[str], add]

#### Sau khi thêm retry, khách hàng nhận được 3 email giống hệt nhau

Hai bước đầu đã làm sẵn. Ba bước sau bạn tự viết ra giấy rồi mới mở đáp án.

1. Ảnh chụp hay nhật ký? — Không phải câu hỏi đúng ở đây. Vấn đề không nằm ở state 
 mà ở tác động ra thế giới bên ngoài. Đây là dấu hiệu bạn phải nhảy sang câu ②.
2. Side effect? — Có, loại nguy hiểm nhất. Gửi email là hành động 
 không rollback được. Node gửi email đang không idempotent, và retry 
 biến một lỗi tạm thời thành ba email thật.
3. ③ Quyết định "đã gửi hay chưa" nên lưu ở đâu? 
 (gợi ý: sau khi crash và resume từ checkpoint, node có biết là mình đã gửi rồi không?)
4. ④ Lỗi gốc thuộc tầng nào — retry, fallback hay dead-letter? 
 (gợi ý: câu hỏi thật là "có nên retry node này không", chứ không phải "retry mấy lần")
5. ⑤ Bằng chứng nào chứng minh đã sửa? 
 (gợi ý: bạn cần đếm cái gì, và đếm ở đâu?)

#### Đáp án ba bước còn lại

**③ Lưu ở nơi sống sót qua cả retry lẫn crash — tức là ngoài bộ nhớ tiến trình.** Hai lựa chọn, và chúng khác nhau về sức mạnh:

• *Trong state* ( `notified: bool` ): sống sót qua retry *và* qua crash, 
 vì state nằm trong checkpoint. Đủ cho hầu hết trường hợp. 
 • *Idempotency key ở phía dịch vụ* (Redis hoặc bảng DB, khoá suy ra từ state như `f"notify:{session_id}:{host_id}"` ): mạnh hơn, vì nó còn chống được cả trường hợp *hai tiến trình cùng chạy một thread*.

**Điểm mấu chốt:** khoá phải *suy ra được từ state*. Nếu bạn sinh khoá bằng `uuid4()` hay timestamp, sau khi retry node sẽ tính ra khoá *mới* và không nhận ra 
 việc đã làm — idempotency trở thành vô nghĩa.

**④ Không tầng nào cả — câu hỏi sai.** Ba tầng của [slide 26](#s26) nói về *xử lý lỗi thế nào*. Ở đây lỗi nằm ở chỗ khác: bạn đã bọc retry quanh một node **không được phép retry**.

Nguyên tắc của [slide 16](#s16): *"node retry phải idempotent"*. 
 Đây là điều kiện **tiên quyết**, không phải lời khuyên. Thứ tự đúng là: 
 làm node idempotent *trước*, thêm retry *sau*. Ngược lại là biến lỗi tạm thời 
 thành lỗi vĩnh viễn.

**⑤ Một test đếm số lần gọi thật.** Thay hàm gửi email bằng spy, ép nó lỗi 2 lần đầu, 
 chạy graph với retry, rồi `assert send_spy.call_count == 1` — *một*, không phải ba. 
 Bổ sung một test crash-resume: kill sau khi gửi, resume, assert vẫn là 1.

*Đối chiếu với bài 1:* cùng khung câu hỏi, nhưng bài 1 dừng ở câu ① (lỗi state) 
 còn bài này nhảy tới câu ② (lỗi side effect). **Biết câu hỏi nào áp dụng được 
 chính là kỹ năng chẩn đoán.**

#### SmartCheck AI — soát CheckInState theo 5 quy tắc của slide 14

Không có bước nào làm sẵn. Đây là state schema thật trong `context.md` của bạn.

```text
class CheckInState(TypedDict):
    messages: list
    visitor_info: dict | None
    intent: str | None
    appointment: dict | None
    destination: dict | None
    missing_fields: list[str]
    confidence: float
    checkin_status: str
    requires_human: bool
    error: str | None
```

ảnh chụp hay nhật ký?

ít nhất hai lỗi

Viết ra rồi mới mở. Nếu bạn tìm được cả hai lỗi và giải thích được hậu quả, 
 bạn đã đạt mức "Phân tích" của bài học này.

#### Đáp án tham khảo — so với bài của bạn, không thay thế nó

**Lỗi 1 (nghiêm trọng nhất) — `messages: list` không có reducer.** Đây là nhật ký hội thoại, phải là `Annotated[list[AnyMessage], add]`. 
 Hiện tại nó dùng reducer mặc định là *overwrite*.

*Vì sao đây không phải lỗi lý thuyết:* ở bài Ngày 20 bạn đã lên kế hoạch chạy song song `search_appointment` và `retrieve_policy` để cắt P95 latency. 
 Ngay khi hai node đó cùng ghi vào `messages` trong một super-step, **một trong hai biến mất — im lặng**. Tối ưu latency sẽ *tạo ra* lỗi mất dữ liệu.

**Lỗi 2 — `error: str | None` nên là `errors: Annotated[list[str], add]`.** Một chuỗi đơn chỉ giữ được lỗi *cuối cùng*. Với retry, lỗi lần 1 và lần 2 bị mất, 
 nên failure analysis mất sạch dữ liệu — và đó là mục ăn điểm trong report.

**Lỗi 3 — thiếu bộ đếm.** Không có `attempt` hay `clarify_attempts`, nên vòng "hỏi lại thông tin thiếu" không có giới hạn. 
 (Đây đúng là phát hiện của tài liệu Ngày 20 — giờ bạn thấy nó lại từ một góc khác.)

**Lỗi 4 — thiếu `schema_version`.** Quy tắc 5. Khi bạn thêm `errors` và `attempt` như trên, mọi checkpoint cũ sẽ không load được — 
 đúng vấn đề mà quy tắc này tồn tại để chặn.

**Điểm đúng đáng ghi nhận:** `missing_fields: list[str]` để reducer mặc định 
 là **chính xác** — nó là *ảnh chụp*, không phải nhật ký. 
 Nếu append, field đã điền vẫn nằm trong danh sách thiếu và kiosk sẽ hỏi lại vô hạn. 
 Đây là ví dụ đẹp cho việc "list" không tự động nghĩa là "append".

**Schema sau khi sửa:**

```text
from typing import Annotated, TypedDict
from operator import add

class CheckInState(TypedDict):
    schema_version: int                                  # quy tắc 5
    messages:       Annotated[list[AnyMessage], add]     # nhật ký  ← LỖI 1
    errors:         Annotated[list[str], add]            # nhật ký  ← LỖI 2
    tool_calls:     Annotated[list[dict], add]           # nhật ký (audit trail)
    visitor_info:   dict | None                          # ảnh chụp
    intent:         str | None                           # ảnh chụp
    appointment:    dict | None                          # ảnh chụp
    destination:    dict | None                          # ảnh chụp
    missing_fields: list[str]                            # ảnh chụp — ĐÚNG như cũ
    confidence:     float
    checkin_status: str
    requires_human: bool
    clarify_attempts: int                                # ← LỖI 3
    tool_attempts:    int
```

**Về quy tắc 4 (lean) — một cảnh báo cho tương lai:** danh sách log trong `context.md` có `retrieved_documents`. Nếu bạn đưa *nội dung* tài liệu 
 vào state thay vì chỉ `doc_ids`, mỗi checkpoint sẽ nặng lên hàng trăm KB. 
 Chạy thử ở [máy tính checkpoint](#m-ckpt) để thấy con số.

**Bẫy trong đề:** nếu bạn kết luận "mọi field list nên append" thì bạn đã sai ở `missing_fields` — và cái sai đó tạo ra một vòng lặp vô hạn, tệ hơn cả lỗi ban đầu. 
 Quy tắc không phải "list thì append"; quy tắc là **"ảnh chụp hay nhật ký"**.

---

<!-- chiron-source-span: {"source_span_id":"e92819c5-e003-5335-b601-5c0c33a9de2e","locator":{"kind":"html_section","section_id":"misc","order":12,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"track-3-day-23.html"},"checksum":"813ea69136c7b67cd6bf88a81d3099fd723d8a2ef5d2b16f44a17e67ca587dec"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Mỗi thẻ: niềm tin phổ biến, lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng 
 ngay trong trang này.

*Vì sao nghe hợp lý:* nó *thật sự* mạnh hơn, và ai cũng muốn dùng công cụ tốt nhất. 
 Thêm nữa, dùng graph cho mọi thứ nghe như "nhất quán về kiến trúc".

Slide 10 có sẵn danh sách "khi chưa cần": prompt đơn lẻ, ETL tuyến tính, không có state, 
 không cần approval/audit. Với những bài đó, graph thêm state schema, node, edge và checkpointer — 
 bốn tầng trừu tượng — mà **không đổi lấy gì**. Nó còn thêm cả một họ lỗi mới: reducer.

Phép thử một câu ở [slide 8](#s8): *"có cần quyết định bước tiếp theo dựa trên 
 kết quả bước trước không?"* · Cùng khuôn mẫu với "đừng thêm agent" (Ngày 20) và 
 "đừng fine-tune" (Ngày 21).

*Vì sao nghe hợp lý:* ví dụ trong slide toàn là `messages`, `tool_results`, `errors` — đều là list và đều append. 
 Quy tắc "list → append" trông như một mẫu hình rõ ràng.

Quy tắc thật là **"ảnh chụp hay nhật ký"**, không phải "kiểu dữ liệu là gì". `missing_fields: list[str]` là *ảnh chụp* và phải overwrite. 
 Nếu append, field đã được điền vẫn nằm trong danh sách thiếu → graph hỏi lại vô hạn. **Một reducer sai tạo ra một vòng lặp vô hạn.**

[Slide 11](#s11): `errors` append nhưng `missing_fields` overwrite, 
 cùng kiểu dữ liệu · [Bài 3](#ladder) chỉ ra `CheckInState` của bạn 
 đang làm đúng ở chính field này.

*Vì sao nghe hợp lý:* `compile(checkpointer=MemorySaver())` chạy trơn tru, `get_state_history()` trả về dữ liệu thật, và "resume" trong cùng script hoạt động. 
 Mọi thứ trông đúng.

`MemorySaver` giữ state **trong RAM của tiến trình**. Tiến trình chết là 
 state chết. Bạn đang chứng minh rằng một biến Python vẫn còn giá trị — điều luôn đúng và 
 không liên quan gì tới crash. Ngoài ra, quên truyền `thread_id` khi invoke thì 
 checkpointer *không có tác dụng*, cũng không báo lỗi.

[Slide 20](#s20) — bảng ba loại saver · Phép thử thật: chạy, **kill tiến trình**, 
 chạy lại từ tiến trình mới với cùng `thread_id`. Không kill thì chưa chứng minh gì.

interrupt()

*Vì sao nghe hợp lý:* tên hàm gợi đúng như vậy, và nó trông y hệt `await` hay `yield` — những thứ thật sự tạm dừng rồi tiếp tục tại chỗ.

Lần đầu chạy tới, `interrupt()` **ném ra để dừng graph**. 
 Khi resume, node **chạy lại từ dòng đầu tiên**, và lần này interrupt mới trả về giá trị. 
 Nghĩa là *mọi code đứng trước nó chạy đúng hai lần* — kể cả lời gọi API, kể cả gửi thông báo.

[Slide 25](#s25) — ví dụ sai/đúng đặt cạnh nhau · Đây là lý do checklist [slide 16](#s16) yêu cầu node idempotent, và interrupt biến yêu cầu đó thành bắt buộc.

*Vì sao nghe hợp lý:* nhiều cơ hội hơn thì tỷ lệ thành công cao hơn — và điều đó *đúng*. Vấn đề nằm ở chỗ nó đúng ít hơn bạn nghĩ, và tốn nhiều hơn bạn nghĩ.

Tỷ lệ thất bại giảm theo **luỹ thừa** (cạn rất nhanh), còn backoff tăng theo **2ⁿ** (bùng nổ). Với lỗi 20%: từ 3 lên 6 lần thử chỉ thêm 0,79 điểm phần trăm 
 thành công, đổi lấy độ trễ xấu nhất từ 9 giây lên 43 giây.

Và nếu dịch vụ *sập hẳn* thay vì lỗi thoáng qua, giả định "các lần thử độc lập" sai hoàn toàn — 
 retry không cứu gì mà chỉ làm tình hình tệ hơn.

[Ngân sách retry](#m-retry) — kéo max_attempts 3 → 6 và nhìn hai con số đi ngược chiều nhau.

*Vì sao nghe hợp lý:* code chạy là cảm giác hoàn thành mạnh nhất trong lập trình. 
 Và "Graph behavior" đúng là mục điểm cao nhất của rubric (25).

**55 trên 100 điểm là bằng chứng, không phải logic:** Metrics & tests (20) + 
 Report & demo (15) + Persistence phải *chứng minh* được (15) + hygiene (5). 
 Một graph chạy hoàn hảo mà không có `metrics.json`, không có failure analysis và 
 không kill được tiến trình để chứng minh resume thì trần điểm là 45.

[Bộ tự chấm rubric](#m-rubric) — tick những gì bạn *có bằng chứng* và xem tổng · [Bảng mật độ điểm/phút ở slide 30](#s30): mốc metrics+report có mật độ cao nhất 
 và nằm cuối cùng.

---

<!-- chiron-source-span: {"source_span_id":"81a8e3b3-0045-5a1b-adfa-d01aa6d6f61e","locator":{"kind":"html_section","section_id":"apply","order":13,"heading":"→ Áp dụng vào SmartCheck AI","source_file":"track-3-day-23.html"},"checksum":"e854ff60c1b98ebd4d02e9acdc46ffe260fea0a74d89a0255c128fa0f564ac37"} -->

## → Áp dụng vào SmartCheck AI

Đây là bài học duy nhất trong ba bài nói về **chính công nghệ bạn đang dùng** — 
 nên phần này là một bản soát code, không phải một phép loại suy.

### Soát CheckInState theo 5 quy tắc slide 14

| Quy tắc | Hiện trạng | Mức | Việc cần làm |
| --- | --- | --- | --- |
| 1 · Flat | visitor_info, appointment, destination là dict lồng | Chấp nhận được | Giữ nguyên — chúng là object lá từ DB, không cần merge sâu |
| 2 · Reducer rõ cho list | messages: list không có reducer | Nghiêm trọng | Annotated[list[AnyMessage], add] |
| 3 · Typed | messages: list và visitor_info: dict chưa có kiểu phần tử | Trung bình | Thêm kiểu cụ thể để validate được |
| 4 · Lean | Chưa vi phạm — nhưng retrieved_documents trong danh sách log là rủi ro | Rủi ro tương lai | Lưu doc_ids, không lưu nội dung tài liệu |
| 5 · Versioned | Không có | Trung bình | Thêm schema_version: int ngay bây giờ, khi chưa có checkpoint nào |

search_appointment

retrieve_policy

messages

một trong hai kết quả biến mất — không exception, không log đỏ

tối ưu latency của Ngày 20 sẽ kích hoạt lỗi mất dữ liệu của Ngày 23

### 5 thay đổi cụ thể, xếp theo tỷ lệ lợi ích trên công sức

| # | Thay đổi | Từ slide | Công sức | Vì sao đáng |
| --- | --- | --- | --- | --- |
| 1 | messages và errors dùng Annotated[..., add] | 14, 15 | 2 dòng | Chặn mất dữ liệu im lặng khi fan-out — bắt buộc trước khi song song hoá |
| 2 | Thêm schema_version, clarify_attempts, tool_attempts | 14, 26 | 3 dòng | Chặn vòng lặp vô hạn và chặn vỡ checkpoint khi deploy |
| 3 | Dùng PostgresSaver với thread_id = session_id | 20, 22 | ~10 dòng | Bạn đã chạy PostgreSQL rồi — hạ tầng có sẵn, không tốn thêm gì |
| 4 | Idempotency key cho register_visitor, generate_pass, notify_host | 16, 26 | ~15 dòng | Ba node này đều không rollback được; retry mà thiếu key là nhân đôi tác động thật |
| 5 | Xuất metrics.json từ get_state_history() | 22, 27 | ~20 dòng | Đáp ứng luôn yêu cầu observability của context.md — một hàm, hai mục đích |

context.md

PostgresSaver

backend restart lúc khách đang nhập thông tin 
 không còn làm khách phải bắt đầu lại từ đầu.

### Escalation hay interrupt — và câu trả lời phỏng vấn

Thiết kế hiện tại dùng `requires_human: bool` + route sang node escalate. [Slide 24](#s24) giới thiệu `interrupt()`. **Cái nào đúng?**

|  | Escalation (hiện tại) | Interrupt (slide 24) |
| --- | --- | --- |
| Graph làm gì | Bàn giao rồi kết thúc | Dừng và chờ, rồi chạy tiếp |
| Người làm gì | Tiếp quản ngoài hệ thống | Ra một quyết định, hệ thống dùng nó |
| Phù hợp khi | Lễ tân bước tới xử lý trực tiếp cho khách | Lễ tân duyệt một việc rồi hệ thống tự làm nốt |
| SmartCheck AI hôm nay | ✓ Đúng — khách đang đứng đó, không có gì để resume | Chưa cần |

> Câu trả lời phỏng vấn dựng sẵn 
>  "Em dùng escalation chứ không dùng interrupt, vì hai cơ chế giải hai bài khác nhau. 
>  Interrupt là để graph dừng, người ra quyết định, rồi graph chạy tiếp — 
>  phù hợp với approval trước hành động phá huỷ. Ở kiosk thì khách đang đứng trước máy và lễ tân 
>  bước tới xử lý trực tiếp, nên đúng ngữ nghĩa là bàn giao và kết thúc phiên tự động, 
>  không có gì để resume. 
>  
>  Em sẽ chuyển sang interrupt nếu có luồng mà lễ tân duyệt một việc rồi hệ thống làm nốt — 
>  ví dụ duyệt cấp thẻ cho khách VIP rồi tự sinh pass và gửi thông báo. 
>  Lúc đó em cần interrupt() với payload gồm action, risk và evidence, 
>  và phải đảm bảo node approval không có side effect nào — vì khi resume, node chạy lại từ đầu."

### Metric của slide 27 so với danh sách log trong context.md

| Metric slide 27 | Đã có trong context.md? | Ghi chú |
| --- | --- | --- |
| task_success_rate | ✓ qua final_status | Đã có |
| nodes_visited | ~ một phần qua tools_called | Node ≠ tool — bổ sung đếm node từ state history |
| retry_count | ✗ | Cần trường tool_attempts (thay đổi #2) |
| interrupt_count | ~ qua human_escalation | Ngữ nghĩa khác nhau — đặt tên rõ là escalation_count |
| state_validation_errors | ✗ | Bổ sung — bắt được node trả về sai kiểu |
| latency_per_run | ✓ qua latency | Tách machine_latency khỏi thời gian chờ người |
| resume_success | ✗ | Chỉ có nghĩa sau khi thêm checkpointer (thay đổi #3) |

retry_count

state_validation_errors

resume_success

get_state_history()

thay đổi #3 mở khoá luôn ba dòng cuối của bảng này

context.md

---

<!-- chiron-source-span: {"source_span_id":"3cb0a65e-d1be-5d98-b20a-c48932d605cd","locator":{"kind":"html_section","section_id":"numbers","order":14,"heading":"! Điểm cần kiểm chứng trước khi trích dẫn","source_file":"track-3-day-23.html"},"checksum":"e68b74a2cec56032f22d4f5304a2e1504b7d856d1373a8e34880b6df32635db9"} -->

## ! Điểm cần kiểm chứng trước khi trích dẫn

Bài này ít số hơn hai bài trước, nhưng có vài chỗ đáng cẩn thận.

| Nội dung | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| Tên bài / số ngày | 1 | File tên "day 23", slide ghi "Day 08"; tác giả để trống | Trích theo tên bài, đừng trích theo số ngày |
| "Memory / SQLite / Postgres saver" | 20 | Đúng, nhưng API và tên lớp đổi theo phiên bản LangGraph | Ghim phiên bản trong requirements.txt và đọc doc đúng phiên bản |
| Độ trễ ghi checkpoint (0,05 / 2,5 / 5 ms) | — | Số minh hoạ của tài liệu này, không có trên slide | Tự đo trên hạ tầng của bạn trước khi dùng để ra quyết định |
| Thông lượng serialize ~400 MB/s | — | Ước lượng của tài liệu này | Chỉ để cảm nhận bậc độ lớn |
| Mô hình retry "các lần thử độc lập" | 26 | Chỉ đúng cho lỗi thoáng qua | Dịch vụ sập hẳn ⇒ giả định sai hoàn toàn ⇒ cần circuit breaker, không phải retry |
| Bộ tiêu chí con trong bảng tự chấm | 31 | Tổng điểm 6 nhóm lấy từ slide; tiêu chí con là diễn giải của tài liệu này | Dùng để tự kiểm, không dùng để tranh luận điểm với giảng viên |
| Bảng "điểm / phút" ở slide 30 | — | Tài liệu này tự tính từ mốc thời gian và rubric | Là công cụ ưu tiên thời gian, không phải cam kết chấm điểm |

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực tế đã chạy."

---

<!-- chiron-source-span: {"source_span_id":"bc2c9d82-ed3f-598b-831c-2a970249752d","locator":{"kind":"html_section","section_id":"cheat","order":15,"heading":"✓ Cheat sheet ôn thi","source_file":"track-3-day-23.html"},"checksum":"a6f2c434e97377f4945c393e7b54f4c689a7c2f5e089a4d5d11c9a771bb204f3"} -->

## ✓ Cheat sheet ôn thi

Nén toàn bộ 36 slide xuống một trang.

### Năm khoảng trống → năm pattern (slide 9)

| Cần gì | Pattern | Khái niệm phải nắm | Sai thì có kêu không? |
| --- | --- | --- | --- |
| Retry logic | Loop + conditional edge | attempt trong state, max_attempts | Có — treo hoặc lỗi |
| Human approval | interrupt + resume | Node chạy lại từ đầu khi resume | Có — không dừng được |
| Dynamic routing | Conditional edges | route() đọc state, trả về tên nhánh | Có — đi sai đường |
| Crash recovery | Checkpointing | Saver bền + thread_id ổn định | Có — mất phiên |
| Parallel work | Fan-out + reducer | Ảnh chụp → overwrite · Nhật ký → append | KHÔNG |

### Bốn khái niệm nền tảng, ba nhầm lẫn hay gặp

| Khái niệm | Một câu | Nhầm lẫn hay gặp |
| --- | --- | --- |
| State | TypedDict phẳng, có kiểu, gọn, có version | Nhét cả tài liệu RAG vào — mỗi checkpoint copy nguyên khối |
| Node | Hàm đọc state, trả về partial update | Mutate state trực tiếp → phá checkpoint và time travel |
| Edge | route() trả về tên nhánh, không phải state | Gọi LLM trong route() → quyết định không vào checkpoint, replay không tái hiện |
| Reducer | Luật merge khi nhiều node cùng ghi một field | "list thì append" — sai với missing_fields |

interrupt()

chạy lại từ đầu

get_state_history()

mới nhất trước

hist[0]

super-step

### Checklist trước khi nộp lab

1. Mọi field list trong state đã trả lời câu "ảnh chụp hay nhật ký?" chưa?
2. Có schema_version chưa?
3. Mọi node có side effect đã có idempotency key suy ra từ state chưa?
4. Checkpointer có phải loại bền không (không phải MemorySaver)?
5. thread_id có suy ra từ nghiệp vụ và ổn định giữa các lần chạy không?
6. Đã kill tiến trình và resume thành công chưa — có log cả hai lần chạy chưa?
7. Đủ 6 scenario chưa, đặc biệt cặp transient-error và max-error?
8. Có test dùng spy chứng minh không execute khi chưa approve chưa?
9. metrics.json đủ 7 metric của slide 27 chưa?
10. Report có failure analysis theo mẫu triệu chứng → nguyên nhân gốc → xử lý chưa?

Reducer là khái niệm duy nhất hỏng mà không báo lỗi.

---

<!-- chiron-source-span: {"source_span_id":"65b0a2c4-d211-5a98-b5dc-92bb5bd649f7","locator":{"kind":"html_section","section_id":"gloss","order":16,"heading":"A–Z Từ điển thuật ngữ","source_file":"track-3-day-23.html"},"checksum":"dc2f084cd975b660d5f7812e37681acf645103326d2ac326075a520f6bfd4640"} -->

## A–Z Từ điển thuật ngữ

Mỗi mục: một câu tiếng Việt dễ hiểu, rồi chỗ nó xuất hiện trong bài.

---

<!-- chiron-source-span: {"source_span_id":"7ef28211-ec30-5719-af0d-adb5c52978bb","locator":{"kind":"html_section","section_id":"bloom","order":17,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-23.html"},"checksum":"9ca29bd273aef65f26bc638d2113ffb200e95087e9fec86bdffbfc48f225ada1"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Rubric chấm mức 3–4; câu hỏi số 5 của 
 demo chấm mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được bốn khái niệm nền tảng (state, node, edge, reducer), ba loại saver, và ba tầng error recovery. | Slide 10 · 20 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao node trả về partial update, và vì sao 
 interrupt() làm node chạy lại từ đầu. | Ô kiểm tra chương 3 và 5 |
| 3 · Áp dụng | Cho một field mới, chọn đúng reducer và giải thích được. Thêm retry vào một node và biết 
 phải làm gì trước đó. | Mô phỏng reducer · Bài 1 → 2 |
| 4 · Phân tích | Nhìn state schema của người khác và chỉ ra field nào sẽ mất dữ liệu khi fan-out — 
 trước khi nó xảy ra. | Bài 3 · Soát CheckInState |
| 5 · Đánh giá | Trả lời câu 5 của demo: chỉ ra điểm yếu nhất trong hệ của chính mình và 
 lý do nó là điểm yếu nhất — bằng bằng chứng, không phải cảm giác. | Slide 32 · Bộ tự chấm |

đang chạy tốt

không có triệu chứng
