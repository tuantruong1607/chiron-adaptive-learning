---
schema_version: 1
course_id: rag-intensive
document_id: "3284b135-b842-59e5-aa8b-f576f9d649c7"
document_version_id: "8fd59348-f98a-53a5-9421-6574c720b163"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Multi-Agent & Kết nối hệ thống — MCP, A2A & LangGraph — phân tích & breakdown từng slide"
source_file: "slide-day09.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-day09.html"
source_sha256: "21f19d1f226af372006f0a1fd768fae9702996e4bf1d162d697220cf598381c1"
parser_version: chiron-structured-markdown-v1
html_section_count: 21
interactive_module_count: 3
interactive_control_count: 14
language: vi
---

# Multi-Agent & Kết nối hệ thống — MCP, A2A & LangGraph — phân tích & breakdown từng slide

> 85 slide, và deck này khác ba bài trước ở một điểm: nó không bán multi-agent. 
 Slide 12 viết thẳng "đừng dùng multi-agent chỉ vì thấy ngầu", slide 73 liệt kê "nhiều agent = 
 hệ thống tốt hơn" là hiểu lầm số một. Tài liệu này đi xa hơn một bước và tính ra điều 
 deck chỉ cảnh báo: có cấu hình multi-agent kém tin cậy hơn single-agent, và nó không hiếm.

<!-- chiron-source-span: {"source_span_id":"95487e29-c2cb-597f-a9cc-22bcaa16088f","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-day09.html"},"checksum":"708a4418dd2814ce1db01ee8de8e4a83ad15fe2f8a7b0218aa822f1f7df5a6f4"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Ngày 9 nhận tiếp từ [Ngày 8](slide-day08.html) đúng ở chỗ Ngày 8 kết thúc. Slide 131 của 
 Ngày 8 nói toàn bộ pipeline RAG sẽ được *"đóng gói thành một hàm Python đơn giản"* để agent gọi. 
 Ngày 9 là bài về **cái gì gọi hàm đó, và tại sao lại cần nhiều hơn một thứ để gọi**.

làm thêm

Slide 12

"Đừng dùng multi-agent chỉ vì thấy 'ngầu'. Nếu 1 workflow 
 đơn giản đã đủ, giữ đơn giản sẽ rẻ và ổn định hơn."

Slide 73

"nhiều agent = hệ thống tốt hơn"

Slide 67

Tài liệu này đi thêm một bước:

tính ra

mô-đun độ tin cậy

85,7%

95,0%

Multi-agent làm đúng thì hơn; làm ẩu thì kém hơn hẳn.

| Deck nói | Slide | Mô-đun tính ra |
| --- | --- | --- |
| "Context window có giới hạn cứng" — một agent phải giữ quá nhiều thứ | 10, 11 | Ngân sách context — tái hiện đúng ví dụ slide 11, rồi tính 
 chia vai mua được bao nhiêu chỗ |
| "Mỗi agent = ít nhất 1 LLM call" · "supervisor không cần model lớn nhất" | 66, 67 | Chi phí & độ trễ — và kết quả về việc hạ cấp supervisor 
 khiêm tốn hơn nhiều so với ấn tượng slide tạo ra |
| "No Fallback" là anti-pattern · "thất bại cục bộ không nên crash toàn hệ" | 28, 68 | Nghịch lý No Fallback — nơi có phát hiện đáng ngạc nhiên nhất của cả bài |

Lượt 1 · ~15 phút

Nắm khung

- Đọc slide 10 — bốn giới hạn của single-agent. Đây là toàn bộ lý do bài này 
 tồn tại
- Nhìn Hình 1 — ngân sách token cụ thể, và chia vai mua được gì
- Đọc slide 12 — sáu dấu hiệu nên nghĩ tới multi-agent, và một dòng cảnh báo
- Mục tiêu: nói được vì sao câu hỏi đúng không phải "agent có đủ thông 
 minh không"

Lượt 2 · ~60 phút

Chương 05, 07, 08, 11

- Chương 05: supervisor-worker và bốn anti-pattern — phần bị hỏi nhiều nhất
- Chương 07–08: MCP so với A2A — hai thứ rất dễ nhầm, xem Hình 2
- Chương 11: chạy cả hai mô-đun — chúng cho hai kết 
 luận ngược chiều nhau và đó là điểm chính
- Làm thật ba Mini-Quest trước khi đọc debrief

Lượt 3 · ~25 phút

Ôn thi

- 6 hiểu lầm — năm cái đầu chính là năm cái deck liệt kê ở slide 73
- 3 bài bậc thang — kỹ năng: đọc trace tìm lỗi im lặng
- Cheat sheet — bảng MCP/A2A và bốn anti-pattern nên thuộc

Slide 16

Claude Code, Codex, Cursor

đã dùng mà chưa nhận ra

bảng debrief slide 17

description:

tools:

max_depth

---

<!-- chiron-source-span: {"source_span_id":"2638cffe-62a4-5e51-8ef6-570a83228256","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu — khi nào một agent là không đủ","source_file":"slide-day09.html"},"checksum":"1b2ab44270627836e7fbf9185db9b4a43e1f18e49965e0872249918a647a69aa"} -->

## 00 Mở đầu — khi nào một agent là không đủ

Câu hỏi mở bài giả định bạn đã có một agent chạy được. Nó hỏi tiếp: *bài toán lớn 
 hơn agent thì tổ chức thế nào?*

### Slide 2–3 Câu hỏi mở đầu, và vị trí của Ngày 9 trên lộ trình

> Trích slide 
>  "HÃY SUY NGHĨ… 'Bạn có 1 agent rất giỏi. Nhưng bài toán đã quá lớn cho 1 agent. Làm thế 
>  nào để hệ thống vẫn rõ vai trò, dễ kiểm soát, và dễ mở rộng?' " 
>  "Day 08 đã dạy cách lấy đúng thông tin. Day 09 hỏi câu tiếp theo: khi bài 
>  toán lớn hơn một agent, ta tổ chức hệ thống như thế nào? "

Đọc kỹ ba tiêu chí trong câu hỏi — chúng không phải ba cách nói cùng một điều, và chúng xung đột với 
 nhau:

| Tiêu chí | Nghĩa là gì | Nó đánh đổi với cái gì |
| --- | --- | --- |
| Rõ vai trò | Mỗi phần hệ thống có một trách nhiệm gọi tên được | Nhiều vai = nhiều LLM call = đắt hơn |
| Dễ kiểm soát | Biết được lỗi nằm ở đâu, và khoanh vùng được | Cần trace, cần contract, cần schema — công sức thiết kế trả trước |
| Dễ mở rộng | Thêm một worker mà không phải viết lại prompt gốc | Mỗi điểm mở rộng là một điểm fail mới |

mô-đun context

không

mô-đun chi phí

mô-đun độ tin cậy

mà không thiết kế fallback

chia khi context là điểm nghẽn, và chỉ khi bạn chịu trả tiền cho 
 retry

### Slide 5–6 Sáu mục tiêu, và deliverable đòi một thứ Ngày 8 không đòi

> Trích slide 
>  "Giải thích được vì sao single-agent bắt đầu quá tải · Phân biệt được các pattern 
>  supervisor-worker, pipeline, debate, hierarchical — và biết chọn đúng pattern · 
>  Hiểu MCP là chuẩn nối agent với tool, và A2A là cách agents giao việc cho 
>  nhau với message contract rõ · Dùng LangGraph để hình dung graph, state, và 
>  conditional routing · Thiết kế được trace & observability · Nâng cấp 
>  artifact Day 08 thành hệ Supervisor + Workers có trace rõ ràng" 
>  Deliverable: "1 supervisor nhận task, route đúng worker, và tổng hợp kết quả · 2–3 
>  worker chuyên vai trò · 1 kết nối external capability qua MCP · 
>  1 trace dễ đọc để giải thích agent nào đã làm gì và khi nào "

scorecard

kết quả

trace

agent nào đã làm gì và khi 
 nào

quá trình

là

slide 30

trace

state 
 schema

Slide 23

"bắt đầu từ 2–3 worker là 
 đủ"

mô-đun độ tin cậy

không có 
 retry

85,7%

77,4%

Mỗi worker thêm vào là một điểm fail nhân vào tích.

---

<!-- chiron-source-span: {"source_span_id":"c3d4eb06-4169-5b3e-82ee-835792c0766a","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Bốn giới hạn của single-agent","source_file":"slide-day09.html"},"checksum":"734dd48639599dbd517dce5c932ed16ec488343b98cc77362dcc657dfbd93a1e"} -->

## 01 Bốn giới hạn của single-agent

Chương này là toàn bộ lý do bài tồn tại. Bốn giới hạn không ngang hàng — một trong 
 bốn là giới hạn *cứng*, ba cái còn lại là giới hạn *mềm*.

### Slide 8–9 Một agent gánh năm việc, và câu hỏi được đặt lại

> Trích slide 
>  Day 08 đã làm được: "retrieve đúng tài liệu hơn · rerank hoặc lọc context tốt hơn · generate câu 
>  trả lời grounded hơn". Nhưng khi hệ thống lớn lên: " phải phân tích task trước khi 
>  retrieve · phải gọi thêm tool ngoài · phải chia việc và tổng hợp nhiều kết 
>  quả · phải theo dõi trace để debug". 
>  Một agent phải làm: Plan task · Retrieve · Call tools · Synthesize · Monitor + retry. 
>  "Một nơi phải làm quá nhiều việc sẽ khó tối ưu, khó debug, và khó scale." 
>  " Câu hỏi đúng không còn là 'agent có đủ thông minh không?' mà là 'ta có đang ép một agent 
>  gánh quá nhiều vai trò không?' "

Việc đặt lại câu hỏi ở cuối slide là chỗ đáng dừng. Nó chuyển vấn đề từ *năng lực* sang *kiến trúc*, và hai loại vấn đề đó có hai cách chữa hoàn toàn khác nhau:

|  | Nếu là vấn đề năng lực | Nếu là vấn đề kiến trúc |
| --- | --- | --- |
| Cách chữa | Model mạnh hơn, prompt tốt hơn, fine-tune | Chia vai trò — và model giữ nguyên |
| Dấu hiệu nhận ra | Agent sai ở những câu hỏi khó, đúng ở câu dễ | Agent sai ở những câu dài hoặc nhiều bước, bất kể độ khó |
| Đổi model có giúp không | Có | Không — model to hơn vẫn hết cửa sổ, vẫn chạy tuần tự |

Ngày 7

"agent trả lời sai vì model yếu, hay vì nó không có 
 đúng dữ liệu?"

Ngày 8

"bạn đang thiếu model mạnh hơn, hay thiếu 
 một pipeline retrieval và evaluation đủ kỷ luật?"

"agent có đủ thông minh không, hay ta đang ép nó gánh quá nhiều vai?"

không phải model, mà là thứ xung quanh model.

### Slide 10 Bốn giới hạn — và chỉ một trong bốn là giới hạn cứng

> Trích slide 
>  1. Context bottleneck — "một agent phải giữ quá nhiều mục tiêu, tool outputs, 
>  evidence, và state trong cùng một lần suy luận. Context window có giới hạn cứng. " 
>  2. Specialization trade-off — "agent càng ôm nhiều vai, prompt càng dài và khó 
>  ổn định. Giỏi đều mọi thứ thường đồng nghĩa với không thật sự giỏi vai nào. " 
>  3. Parallelism hạn chế — "một agent thường chạy tuần tự. Khi có nhiều việc độc 
>  lập, hệ thống vẫn phải chờ từng bước nối nhau — tăng latency không cần thiết." 
>  4. Reliability yếu — "nếu agent chọn sai tool hoặc hiểu sai task ở đầu luồng, 
>  toàn bộ hệ thống dễ đi lệch theo. Không có isolation để khoanh vùng lỗi. "

Bốn giới hạn này khác nhau về *bản chất*, và điều đó quyết định cái nào thật sự buộc bạn phải 
 chia vai:

| # | Giới hạn | Loại | Chia vai có chắc chữa được không? |
| --- | --- | --- | --- |
| 1 | Context bottleneck | Cứng — là ràng buộc vật lý của model | Có, và đo được. Mỗi worker có cửa sổ riêng — 
 mô-đun 1 tính ra bao nhiêu |
| 2 | Specialization | Mềm — về chất lượng prompt | Thường có, nhưng không đo được trực tiếp. Phụ thuộc bạn viết prompt worker tốt tới đâu |
| 3 | Parallelism | Mềm — về kiến trúc thực thi | Chỉ khi công việc thật sự độc lập. Chạy serial thì multi 
 chậm hơn single — mô-đun 2 |
| 4 | Reliability | Mềm — và dễ đi ngược | Không tự động. Không có retry thì multi kém tin cậy hơn — 
 mô-đun 3 |

có

thiết kế isolation

ba điểm fail nối tiếp

Mô-đun 3

85,7%

95,0%

Kém hơn 9,3 điểm.

một

99,3%

toàn bộ lợi ích về độ tin cậy của multi-agent nằm ở retry và fallback, không nằm ở 
 việc chia vai.

chỗ

slide 28

không

không có cách đo nào trung thực.

đo được

mô-đun 1

### Slide 11–12 Context bottleneck bằng số, và sáu dấu hiệu nên chia vai

> Trích slide 
>  Kịch bản thực tế: "agent nhận task phân tích hợp đồng 80 trang + tra cứu luật + tóm tắt rủi ro · 
>  Tool call trả về 12.000 tokens · Chat history đã chiếm 6.000 tokens 
>  · Prompt gốc: 3.000 tokens · Còn lại cho reasoning: ≈ 3.000 tokens " 
>  Dấu hiệu nhận biết: "câu trả lời thiếu thông tin ở giữa document · agent lặp lại bước đã 
>  làm · reasoning ngắn bất thường ở bước cuối · tool call với empty context" 
>  "Agent bắt đầu 'quên' phần đầu tài liệu khi xử lý phần cuối — lost-in-the-middle 
>  problem." 
>  Sáu dấu hiệu nên nghĩ tới multi-agent: "task có nhiều bước vai trò khác nhau · có thể chia việc 
>  độc lập · cần debug rõ ai làm sai · cần mở rộng dần · context window một agent không đủ · 
>  Đừng dùng multi-agent chỉ vì thấy 'ngầu'. Nếu 1 workflow đơn giản đã đủ, giữ đơn giản sẽ rẻ 
>  và ổn định hơn. "

Đây là **chỗ duy nhất trong cả deck có một phép tính cụ thể**, và nó đáng làm rõ: 
 3.000 + 6.000 + 12.000 = 21.000, còn lại 3.000 ⇒ **cửa sổ ngụ ý là 24.000 token**.

| Thành phần | Token | % cửa sổ 24.000 |
| --- | --- | --- |
| System prompt | 3.000 | 12,5% |
| Lịch sử hội thoại | 6.000 | 25,0% |
| Tool output | 12.000 | 50,0% |
| Còn cho reasoning | 3.000 | 12,5% |

Một nửa cửa sổ bị chiếm bởi output của một tool call.

suy nghĩ

chỉ tăng

Mô-đun 1

đúng 1 lượt hội thoại nữa

Đó là ý nghĩa thật của chữ "giới hạn cứng":

hết chỗ ở lượt thứ hai

Ngày 8 · slide 90

mô-đun k của Ngày 8

càng nặng khi prompt càng dài

giảm k

[1,3,5,4,2]

chia thành nhiều context ngắn thay vì một context dài

tốn thêm LLM call

_Sơ đồ: Ngân sách context của một agent so với ba worker, và bốn giới hạn nào được chia vai chữa được - Phần trên vẽ ví dụ ngân sách token của slide mười một trên một cửa sổ hai mươi bốn nghìn token. Với một agent gánh hết: system prompt ba nghìn, lịch sử hội thoại sáu nghìn, tool output mười hai nghìn chiếm một nửa cửa sổ, chỉ còn ba nghìn tức mười hai phẩy năm phần trăm cho suy luận. Phần dưới vẽ cùng ngân sách đó khi chia thành ba worker, mỗi worker có cửa sổ riêng: mỗi worker vẫn giữ nguyên system prompt ba nghìn nhưng chỉ nhận phần lịch sử hai nghìn và phần tool output bốn nghìn của riêng mình, nên còn mười lăm nghìn token trống, tức sáu mươi hai phần trăm cửa sổ. Dung lượng hiệu dụng của cả hệ là bảy mươi hai nghìn token thay vì hai mươi bốn nghìn. Dải cuối liệt kê bốn giới hạn của single agent và cho biết chia vai chữa được cái nào: giới hạn context là giới hạn cứng và chia vai chữa được, đo được; giới hạn chuyên biệt hoá thì thường có nhưng không đo trực tiếp được; giới hạn song song chỉ chữa được khi công việc thật sự độc lập, chạy nối tiếp thì multi còn chậm hơn; giới hạn độ tin cậy thì không tự động chữa được, không có retry thì multi kém tin cậy hơn single._

Hình 1 — Ngân sách context, và bốn giới hạn nào chia vai thật sự chữa được.

slide 11

suy ra

#### Tương tác Ngân sách context — chia vai mua được bao nhiêu chỗ?

[Slide 11](#s11) là chỗ duy nhất trong cả deck có một phép tính cụ thể. 
 Mô-đun này tái hiện đúng nó, rồi trả lời câu deck không hỏi: *chia thành N worker thì mỗi worker 
 còn bao nhiêu chỗ, và cả hệ có bao nhiêu dung lượng?*

Mặc định là đúng ví dụ slide 11: cửa sổ **24.000** · system prompt **3.000** · lịch sử **6.000** · tool output **12.000**. Chia **3 worker**.

Đoán trước: *(a)* một agent còn bao nhiêu chỗ để suy luận? *(b)* nó chịu được thêm 
 mấy lượt hội thoại? *(c)* chia 3 worker thì mỗi worker còn bao nhiêu phần trăm cửa sổ?

#### Kéo rồi mở

**(a) 3.000 token — đúng con số slide 11 đưa ra**, và đó là **12,5%** cửa sổ. Bằng đúng phần dành cho system prompt. Nói cách khác: agent có *ngần ấy chỗ để nghĩ* như chỗ dành cho việc mô tả nó là ai.

**(b) Đúng 1 lượt.** Mỗi lượt hội thoại thêm khoảng 2.000 token lịch sử; cần giữ 
 tối thiểu 2.000 để còn suy luận được. Sau một lượt nữa là hết. 
 Đây là ý nghĩa thật của "giới hạn cứng" — không phải "một ngày nào đó", mà là *lượt tiếp theo*.

**(c) Mỗi worker còn 15.000 token — 62,5% cửa sổ.** Vì mỗi worker vẫn mang đủ 
 system prompt 3.000, nhưng chỉ nhận phần lịch sử (2.000) và phần tool output (4.000) của riêng nó. 
 Và dung lượng hiệu dụng của cả hệ là **72.000 token** thay vì 24.000 — *gấp ba, mà không đổi model.*

**Thử điều đáng thử nhất — kéo cửa sổ lên 128.000:** một agent giờ chịu được **53 lượt** hội thoại. Giới hạn ① gần như biến mất. 
 Đó là lập luận mạnh nhất *chống lại* multi-agent: với model cửa sổ lớn, context không 
 còn là điểm nghẽn. Nếu bạn chia vai *chỉ* vì context, hãy kiểm xem cửa sổ của bạn có thật 
 sự chật không trước đã.

*Bài học vận hành:* nhìn dòng **tool output** — nó chiếm 50% cửa sổ ở cấu 
 hình mặc định. Trước khi chia vai, thử cách rẻ hơn nhiều: **cắt bớt tool output**. 
 Trả về 20 kết quả thay vì 100, hoặc tóm tắt trước khi đưa vào context. Điều đó không tốn một LLM 
 call nào và có thể giải quyết trọn vẹn giới hạn ①.

- **Control - Cửa sổ context: 24.000 token**: min `8`, max `200`, step `4`, default `24`

- **Control - System prompt: 3.000 token**: min `1`, max `20`, step `1`, default `3`

- **Control - Lịch sử hội thoại: 6.000 token**: min `0`, max `40`, step `1`, default `6`

- **Control - Tool output: 12.000 token**: min `0`, max `60`, step `1`, default `12`

- **Control - Chia thành mấy worker: 3 worker**: min `1`, max `8`, step `1`, default `3`

Một agent còn lại

—

—

Còn chịu được mấy lượt

—

—

Mỗi worker còn trống

—

—

Dung lượng hiệu dụng cả hệ

—

—

system prompt lịch sử hội thoại tool output còn trống cho reasoning

#### Xem bảng: chia bao nhiêu vai thì mỗi worker còn bao nhiêu



#### Công thức & giới hạn của mô hình

- còn lại = cửa sổ − system prompt − lịch sử − tool output — đúng phép cộng của 
 slide 11.
- Chia N worker: mỗi worker dùng = system prompt + lịch sử/N + tool output/N. Mỗi 
 worker có cửa sổ riêng, nên dung lượng hiệu dụng của hệ là cửa sổ × N.
- Số lượt còn chịu được: mỗi lượt hội thoại cộng thêm 2.000 token lịch sử, dừng khi phần còn lại 
 dưới 2.000.
- Giới hạn ① — chia đều là giả định lạc quan. Thực tế công việc không chia đều: 
 Retrieval Worker có thể nhận toàn bộ 12.000 token tool output, còn Synthesis Worker chỉ nhận vài 
 trăm token tóm tắt. Mô hình chia đều để thấy hình dạng, không để dự toán chính xác.
- Giới hạn ② — mỗi worker vẫn cần system prompt riêng, và tổng system prompt 
 của N worker lớn hơn của một agent. Ở N lớn, phần đó ăn dần vào lợi ích. Kéo thanh 
 "system prompt" lên 15.000 và N lên 8 để thấy.
- Giới hạn ③ — không tính chi phí. N worker = N LLM call. Mô-đun này chỉ đo 
 chỗ, không đo tiền. Mô-đun 2 đo tiền.
- Giới hạn ④ — không mô hình hoá lost-in-the-middle. "Còn trống" không có nghĩa 
 là "model dùng tốt phần đã có". Ngày 8 cho thấy chất lượng giảm 
 theo độ dài prompt kể cả khi chưa hết cửa sổ.

---

<!-- chiron-source-span: {"source_span_id":"9c8d8204-f45d-5ca3-91cf-fd66f38ea5fb","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Mental model — tư duy hệ thống trước khi thiết kế","source_file":"slide-day09.html"},"checksum":"f3fadbea75254450b6cc13b37c60e0854744e446ed88df75b08527fdaaba626a"} -->

## 02 Mental model — tư duy hệ thống trước khi thiết kế

Hai slide ngắn nhưng chúng chứa ba câu hỏi thiết kế mà nếu trả lời được thì phần lớn 
 quyết định kiến trúc tự hiện ra.

### Slide 14–15 "God agent", và ba câu hỏi trước khi viết code

> Trích slide 
>  Tư duy cũ: "làm thế nào để agent thông minh hơn? · prompt nào khiến agent làm 
>  được nhiều hơn? · thêm nhiều tool cho một agent để đủ sức" — "Tư duy này dẫn đến 'god 
>  agent' — một agent làm hết nhưng không ai hiểu nó đang làm gì." 
>  Tư duy hệ thống: "task này gồm bao nhiêu loại trách nhiệm khác nhau? · 
>  ai cần biết gì, khi nào? · lỗi cần được khoanh vùng ở đâu? · 
>  điểm nào cần human oversight?" 
>  Ba câu hỏi thiết kế: " 1 — Chia trách nhiệm ở đâu? task nào cần reasoning? task 
>  nào cần data fetching? task nào chỉ cần format? · 2 — Thông tin đi theo con đường nào? 
>  agent nào cần biết gì? ai cần đầu ra của ai trước tiên? · 3 — Lỗi ở đâu là ít tổn hại 
>  nhất? " 
>  " Thiết kế tốt giúp lỗi có địa chỉ rõ ràng thay vì lan ra cả hệ thống. "

Ba câu hỏi này ánh xạ khá gọn sang ba thứ cụ thể bạn sẽ viết ra trong Lab 9:

| Câu hỏi thiết kế | Nó quyết định | Bạn viết nó ra thành |
| --- | --- | --- |
| 1 — Chia trách nhiệm ở đâu? | Có mấy worker, mỗi worker làm gì | Danh sách worker + một câu mô tả vai trò mỗi cái |
| 2 — Thông tin đi đường nào? | Ai đọc gì, ai ghi gì | State schema + message contract |
| 3 — Lỗi ở đâu ít tổn hại nhất? | Retry ở đâu, fallback là gì | Conditional edge + status + đường thoát human review |

thiết kế bình thường

thất bại

Mô-đun độ tin cậy

85,7%

99,3%

Chênh lệch 13,6 điểm nằm trọn trong câu hỏi thứ ba.

"lỗi ở đâu là ít tổn hại nhất"

sẽ

---

<!-- chiron-source-span: {"source_span_id":"61d4b7a0-649f-5b2b-b5e8-ba0a5a2b5ac1","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Mini-Quest 1 — mổ xẻ chính công cụ bạn đang dùng","source_file":"slide-day09.html"},"checksum":"74fa65ad275afd325242dbf2d97738918d282feba73935c22fc4805f93e050c7"} -->

## 03 Mini-Quest 1 — mổ xẻ chính công cụ bạn đang dùng

Bài tập hay nhất của Ngày 9, vì nó biến một chủ đề trừu tượng thành thứ bạn đã dùng 
 hằng ngày mà chưa nhận ra.

### Slide 16 Đề bài: tìm bằng chứng trong máy, không đoán

> Trích slide 
>  Phần A — Điều tra (8'): "chọn công cụ bạn dùng hằng ngày: Claude Code, Codex, 
>  Antigravity, OpenCode, Cursor… Tìm bằng chứng ngay trong máy, không đoán: có cơ chế 
>  gọi agent con không? agent con có context riêng hay dùng chung? chạy song 
>  song được mấy cái? có giới hạn tool cho từng agent được không? tool ngoài 
>  nối vào bằng đường nào?" 
>  Phần B — Tự tạo 1 agent (10'): "ba ràng buộc: một vai trò hẹp — 
>  không phải trợ lý đa năng · mô tả rõ khi nào được gọi — đây chính là tín hiệu route cho 
>  supervisor · cắt bớt tool nó được phép dùng." 
>  "Mồi sẵn: repo môn học đã có.claude/agents/*.md và.codex/agents/*.toml 
>  — cùng 5 agent, hai schema khác nhau."

Năm câu hỏi ở phần A không phải năm câu ngẫu nhiên — chúng ánh xạ đúng vào năm khái niệm cốt lõi 
 của cả bài:

| Câu hỏi điều tra | Khái niệm Ngày 9 | Chương |
| --- | --- | --- |
| Có cơ chế gọi agent con không? | Supervisor–worker | 05 |
| Agent con có context riêng không? | Chống context bottleneck — 
 lý do thật sự để tách | 01, mô-đun 1 |
| Chạy song song được mấy cái? | Parallelism — giới hạn ③ | mô-đun 2 |
| Có giới hạn tool cho từng agent không? | Trust boundary / least privilege | 08 |
| Tool ngoài nối vào bằng đường nào? | MCP | 07 |

đây chính là tín hiệu route cho supervisor

description:

người đọc

đầu vào cho quyết 
 định routing của supervisor

description: "reviews content"

description: "use when the user asks 
 to check Vietnamese slide text for tone, terminology, or typos — read-only"

chất lượng routing của bạn bị chặn trên bởi chất lượng mô tả 
 worker.

slide 44

### Slide 17 Debrief — đọc một harness bằng từ vựng Ngày 9

> Trích slide 
>  "Vòng lặp chính nhận yêu cầu rồi quyết định gọi ai" → Supervisor — phiên chat gốc 
>  của Claude Code / Codex · ".claude/agents/*.md,.codex/agents/*.toml " → 
>  Định nghĩa Worker — 5 agent: slide-reviewer, 
>  lab-smoke-tester, vn-content-reviewer … 
>  "Dòng description: 'use when…' " → Tín hiệu routing — "supervisor 
>  đọc đúng dòng này để chọn worker" · "Dòng tools: " → Trust boundary / least 
>  privilege — " vn-content-reviewer chỉ có Read, Grep, Glob — không có 
>  Write, nên không thể sửa deck " 
>  "Agent con có context window riêng" → Chống context bottleneck — " lý do thật 
>  sự để tách worker — không phải vì 'ngầu' " · " max_threads = 6 " → 
>  Parallelism · " max_depth = 1 " → Chặn hierarchical — 
>  "worker không được đẻ worker → tránh đệ quy vô hạn " 
>  " Công cụ bạn dùng hằng ngày chính là ví dụ Ngày 9 gần nhất. "

①

tools: [Read, Grep, Glob]

không có Write

least privilege

về mặt kỹ thuật không thể

"đừng sửa file"

Slide 48

"đừng giả định mọi agent đều đáng tin 
 như nhau"

②

max_depth = 1

đệ quy vô hạn

slide 20

③

"agent con có context riêng — lý do thật sự để tách worker"

mô-đun 1

"cùng 5 agent, hai schema khác nhau"

khái niệm giống nhau, cú pháp khác nhau

tên

mô tả khi nào gọi

danh sách tool được phép

MCP

---

<!-- chiron-source-span: {"source_span_id":"a46dbd1c-cb57-528c-9841-a6143e3d467c","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Bốn pattern — và vì sao deck chỉ dạy một","source_file":"slide-day09.html"},"checksum":"b4cdb7785d381451737250ecfec08cca2c8fe9fb320e202ea9550d507d7e1b0d"} -->

## 04 Bốn pattern — và vì sao deck chỉ dạy một

Deck liệt kê bốn pattern rồi *chủ động* chọn một để đi sâu, và giải thích lý 
 do. Cách làm đó đáng học riêng.

### Slide 19–22 Bốn pattern, bảng chọn, và hai minh hoạ

> Trích slide 
>  Supervisor-Worker — "1 supervisor điều phối nhiều worker chuyên biệt. Mạnh ở: 
>  routing rõ, dễ kiểm soát, dễ trace" · Pipeline — "A xong rồi mới chuyển output cho 
>  B. Mạnh ở: flow ổn định, tuyến tính, dễ test" · Debate — "nhiều agent cùng giải một 
>  bài toán rồi vote hoặc synthesize. Mạnh ở: phản biện và giảm blind spot" · 
>  Hierarchical — "supervisor lồng supervisor. Mạnh ở: mở rộng tốt ở enterprise scale" 
>  Cảnh báo từng pattern: supervisor-worker — " supervisor có thể thành bottleneck nếu làm 
>  quá nhiều " · pipeline — " kém linh hoạt khi flow đổi động " · debate — 
>  " tốn cost và khó tổng hợp " · hierarchical — " thiết kế và debugging phức 
>  tạp " 
>  Pipeline: "latency cộng dồn ở mỗi bước · khó xử lý khi flow cần rẽ nhánh · retry một bước 
>  ảnh hưởng toàn chuỗi "

Bốn pattern này khác nhau ở **ai quyết định bước tiếp theo** — và đó là cách phân biệt 
 gọn nhất:

| Pattern | Ai quyết định bước tiếp | Số LLM call cho một task | Hỏng kiểu gì |
| --- | --- | --- | --- |
| Pipeline | Không ai — thứ tự cố định lúc thiết kế | N (mỗi bước một lần) | Latency cộng dồn; retry một bước ảnh hưởng cả chuỗi |
| Supervisor-worker | Supervisor, lúc chạy | 1 + số worker được gọi + 1 | Supervisor thành bottleneck nếu ôm việc |
| Debate | Không ai — tất cả cùng chạy, rồi aggregator gộp | N + 1, luôn luôn — không tiết kiệm được | Đắt; và tổng hợp ý kiến trái 
 nhau là bài toán khó |
| Hierarchical | Nhiều supervisor lồng nhau | Nhân theo tầng | Đệ quy nếu không có max_depth; debug rất khó |

chỉ gọi worker cần thiết

luôn

chi phí mà mô-đun 2 tính

"khi bài toán có nhiều góc nhìn hợp lệ, khi rủi ro sai cao, hoặc khi cần kiểm 
 tra chéo trước một quyết định quan trọng"

quyết định đắt

Ngày 5

chi phí khi sai

rẻ hơn

tất định

không có lỗi routing

Quy tắc rút ra:

bạn thật sự không biết trước bước nào cần chạy

### Slide 23 Vì sao chọn supervisor-worker — và câu cảnh báo về cách dạy

> Trích slide 
>  Lý do sư phạm: "học viên dễ nhìn ra vai trò · dễ nối với use case thật · dễ giải 
>  thích logic route · dễ nâng cấp từ artifact Day 08" 
>  Lý do triển khai: "bắt đầu từ 2–3 worker là đủ · dễ cắm thêm MCP tool worker · 
>  trace và testing rõ hơn · supervisor thường chỉ cần một LLM call nhỏ " 
>  " Nếu Day 09 ôm nhiều pattern ngang nhau, người học sẽ nhớ tên pattern nhưng không biết 
>  ngày mai nên build theo pattern nào. "

"Nhớ tên pattern nhưng không biết ngày mai nên build theo pattern nào."

chọn hộ một cái và nói rõ vì sao

đừng liệt kê bốn lựa chọn rồi cân nhắc

nguyên tắc leo thang

slide 66

"supervisor không cần 
 là model lớn nhất"

Mô-đun 2

khiêm tốn hơn

8,6%

không có lý do gì dùng model đắt cho việc chọn giữa ba nhánh

số worker được gọi

lượng context mỗi worker nhận

---

<!-- chiron-source-span: {"source_span_id":"8d46b70a-e37d-50a2-bb96-3dd85675f9b3","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Supervisor-worker deep dive","source_file":"slide-day09.html"},"checksum":"9081e054380d900ba3d2f86c88bd048eb27d5528e131c856adcd2dfcf02756c4"} -->

## 05 Supervisor-worker deep dive

Chương dài nhất, và nó chứa bốn anti-pattern mà mọi hệ multi-agent đầu tay đều mắc 
 ít nhất hai.

### Slide 25–27 Ai làm gì, và ba đặc điểm của worker tốt

> Trích slide 
>  " Supervisor không cần 'thông minh hơn tất cả'. Vai trò chính là chia việc 
>  đúng, gọi đúng worker, và gom đầu ra thành kết quả mạch lạc." 
>  Supervisor: "phân tích yêu cầu ban đầu · quyết định worker nào nên tham gia · 
>  theo dõi trạng thái và retry nếu cần · tổng hợp đầu ra cuối cùng · biết khi nào cần human 
>  review " · Worker: "xử lý một năng lực hẹp · nhận input rõ ràng, trả output 
>  rõ ràng · càng stateless càng dễ test · thất bại cục bộ không làm hỏng cả kiến trúc 
>  · có thể được thay thế mà không ảnh hưởng supervisor " 
>  " Supervisor giữ decision flow; worker giữ domain skill. Đừng để một worker vừa 
>  làm việc hẹp vừa bí mật điều phối cả hệ thống." 
>  Ba đặc điểm worker tốt: Specialized — "một năng lực chính" · 
>  Stateless ưu tiên — "chỉ cần input hiện tại thay vì ôm cả lịch sử hệ thống" · 
>  Testable — "có input/output rõ để test độc lập trước khi cắm vào supervisor"

Câu *"supervisor giữ decision flow; worker giữ domain skill"* là một dòng đáng thuộc, vì nó 
 cho một phép kiểm nhanh khi review kiến trúc:

Không phải viết lại

"có thể được thay thế mà không ảnh hưởng supervisor"

Phải viết lại

decision flow

"Research Worker"

hai chỗ

slide 60

Mini-Quest 2

"càng stateless càng dễ test"

Test độc lập

Retry an toàn

tiền đề

toàn bộ mô-đun độ tin cậy

Song song được

multi song song

### Slide 28 Bốn anti-pattern — bảng nên in ra dán tường

> Trích slide 
>  God Supervisor — "supervisor làm quá nhiều: plan, retrieve, synthesize, monitor. 
>  Nó trở thành single-agent được đổi tên. " 
>  Chatty Workers — "workers liên tục gọi ngược lại supervisor để hỏi thêm thông 
>  tin. Message overhead tăng rất nhanh. " 
>  Implicit State — "state bị truyền qua biến toàn cục hoặc side 
>  effect. Không ai biết hệ đang ở bước nào." 
>  No Fallback — "worker gặp lỗi và không trả về gì. Supervisor chờ mãi 
>  không thấy đầu ra để tổng hợp. "

Bốn anti-pattern này không ngang hàng về mức nguy hiểm, và chúng có bốn triệu chứng rất khác nhau:

| Anti-pattern | Triệu chứng bạn quan sát được | Nó phá cái gì | Phát hiện bằng |
| --- | --- | --- | --- |
| God Supervisor | Hệ chạy đúng nhưng không nhanh hơn, không rẻ hơn, không dễ debug hơn single-agent | Toàn bộ lý do chia vai | Đếm số dòng code trong supervisor node |
| Chatty Workers | Latency và chi phí tăng phi tuyến khi thêm worker | Lợi ích chi phí — mô-đun 2 giả định mỗi worker gọi một lần | Đếm số LLM call thật trong trace so với dự kiến |
| Implicit State | Chạy lại cùng input ra kết quả khác; không replay được | Khả năng debug, và khả năng retry | Thử chạy hai lần cùng input |
| No Fallback | Hệ treo, hoặc trả về câu trả lời dựa trên dữ liệu rỗng | Độ tin cậy — và nó đẩy multi xuống dưới single | Mô-đun 3; hoặc đọc trace như Mini-Quest 3 |

lãng phí

vector_store

Nếu supervisor tự chạy được, bạn chưa chia vai — bạn chỉ 
 thêm một lớp.

hai

một

1 + N + 1

1 + 3N + 1

5 lên 11 call

message contract không đủ

Slide 46

"thiếu context → 
 phải gọi lại nhiều lần"

viết contract đủ

### Slide 29–31 Shared state hay message passing, và state schema tối thiểu

> Trích slide 
>  Shared state: "dễ xem toàn cảnh · tiện cho graph orchestration (LangGraph) · 
>  nhưng dễ bị 'đụng tay' lẫn nhau nếu không có kỷ luật · cần schema rõ: ai được đọc 
>  gì, ai được ghi gì" · Message passing: "contract rõ hơn · ít coupling hơn · 
>  nhưng phải thiết kế message format cẩn thận · cần validation ở mỗi điểm nhận" 
>  " Shared state giúp điều phối, còn message contract giúp giao tiếp không nhập nhằng. " 
>  class Day09State(TypedDict): 
>  task: str # task goc tu user 
>  plan: list[str] # worker can goi 
>  worker_results: dict # output tung worker 
>  status: str # pending | running | done 
>  final_answer: str # tong hop cuoi 
>  trace: list[dict] # log co timestamp 
>  error: Optional[str] 
>  " Tại sao trace là trường bắt buộc? Không có trace trong state, sau khi hệ chạy 
>  xong không ai biết agent đã đi theo con đường nào để ra kết quả đó. 
>  Quy tắc: trace là list, luôn append, không bao giờ overwrite. "

"Shared state giúp điều phối, message contract giúp giao tiếp không nhập nhằng."

không phải hai lựa chọn thay thế nhau

|  | Shared state | Message contract |
| --- | --- | --- |
| Tồn tại ở đâu | Tầng orchestration — LangGraph truyền nó qua mọi node | Tầng giao tiếp — định nghĩa cái gì đi vào và đi ra mỗi worker |
| Trả lời câu hỏi | "Hệ đang biết gì?" | "Worker này cần gì và trả về gì?" |
| Bỏ nó thì | Không replay được, không biết hệ ở bước nào | Worker đoán mò, hỏi lại nhiều lần ( Chatty Workers ) |

cả hai

TypedDict

```text
SAI  — mat toan bo lich su truoc do
  state["trace"] = [f"[supervisor] {decision}"]

DUNG — noi tiep
  return {**state, "trace": state["trace"] + [entry]}
```

hệ vẫn chạy đúng

đúng lúc bạn cần nó nhất

Ngày 7

Cách chống:

append_trace(state, entry)

state["trace"]

open_kb()

bọc thao tác dễ sai vào một chỗ duy nhất

| Trường | Trả lời câu hỏi | Ai ghi |
| --- | --- | --- |
| task | Người dùng muốn gì? | Điểm vào, ghi một lần |
| plan | Định gọi những worker nào? | Chỉ supervisor |
| worker_results | Mỗi worker trả về gì? | Mỗi worker ghi phần của mình |
| status | Hệ đang ở đâu? | Supervisor, và worker khi fail |
| final_answer | Kết quả là gì? | Synthesis worker hoặc supervisor |
| trace | Đã đi đường nào để tới đây? | Mọi node — chỉ append |
| error | Có gì hỏng không? | Node nào gặp lỗi |

slide 78

"worker chỉ ghi vào field của mình · không 
 để field 'không ai biết ai sở hữu'"

---

<!-- chiron-source-span: {"source_span_id":"eadfc66a-6edf-5757-a7ee-1e120452d324","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Mini-Quest 2 — bốn lỗi trong một node chạy được","source_file":"slide-day09.html"},"checksum":"aa5d1fb91a05c6e89672b6439df5e31f1edaecb63fce3e6cb9ce7165cf955009"} -->

## 06 Mini-Quest 2 — bốn lỗi trong một node chạy được

Đoạn code chạy được, không crash, và vi phạm bốn nguyên tắc. Đây là bài tập tốt nhất 
 để kiểm xem bạn có thật sự hiểu chương 05 không.

### Slide 32–33 Đề bài và đáp án — bốn lỗi, bốn anti-pattern

> Trích slide 
>  def supervisor_node(state: AgentState) -> AgentState: 
>  decision = llm.invoke(SUPERVISOR_PROMPT.format(task=state["task"])) 
>  docs = vector_store.search(state["task"], k=20) 
>  state["retrieval_result"] = docs 
>  state["trace"] = [f"[supervisor] {decision}"] 
>  result = tool_worker(state) 
>  state["final_answer"] = result["text"] 
>  return state 
>  "Đoạn code chạy được, không crash, nhưng vi phạm ít nhất 4 nguyên 
>  tắc đã học sáng nay. Lỗi nào sẽ khiến việc debug khó nhất? Vì sao?" 
>  Đáp án: "Supervisor tự gọi vector_store.search " → God Supervisor → 
>  "để Retrieval Worker làm; supervisor chỉ set need_retrieval rồi route" · 
>  " state['trace'] = [...] ghi đè" → Mất observability → "append" · 
>  "Gọi thẳng tool_worker(state) trong node" → Routing bị chôn trong code 
>  → "dùng conditional edge; node chỉ ra quyết định, không tự gọi worker" · "Không kiểm tra kết quả 
>  worker, không try/except, không set status" → No Fallback 
>  " Bonus: node mutate state tại chỗ rồi return chính nó → nên trả về dict mới để 
>  state có thể replay / persist."

Bốn lỗi này ánh xạ đúng bốn anti-pattern của [slide 28](#s28) — nhưng câu hỏi hay nhất 
 của đề bài là câu thứ tư: *lỗi nào khiến debug khó nhất?*

để lại dấu vết

vector_store.search

tool_worker(state)

phá chính công cụ bạn dùng để tìm ba lỗi kia

đây là lỗi meta.

mù

slide 58

"không có trace tốt, debugging multi-agent gần như là mò mẫm."

"Node mutate state tại chỗ rồi return chính nó → nên trả về dict mới để state có thể replay / 
 persist."

Replay

không còn tồn tại

Persist

Slide 51

human-in-the-loop

{**state,...}

```text
SAI   state["x"] = v ;  return state          # mat trang thai cu
DUNG  return {**state, "x": v}                # trang thai cu van con
```

---

<!-- chiron-source-span: {"source_span_id":"ca06b17e-3a9d-53bf-8f21-da171e2506d0","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 MCP — chuẩn nối agent với tool","source_file":"slide-day09.html"},"checksum":"402bf392090c4e8a4a71581c1ae05277ffe1d97e5d3af139501779f369dfa4f4"} -->

## 07 MCP — chuẩn nối agent với tool

Deck nói rất rõ mục tiêu học: *"hiểu vì sao MCP giúp mở rộng hệ thống, không phải 
 học thuộc protocol spec"*. Chương này giữ đúng mức đó.

### Slide 35–38 Vấn đề MCP giải, ổ cắm chuẩn, và ba thứ server công bố

> Trích slide 
>  Trước MCP: " mỗi tool cần một adapter riêng · thay đổi API của tool = viết lại 
>  code tích hợp · mỗi framework gọi tool theo cách khác nhau · không có chuẩn chung để agent 
>  biết tool làm gì " 
>  "MCP là một chuẩn để agent kết nối với external capabilities… MCP server công bố các thứ như 
>  tools, resources, và prompts. Agent có thể list, describe, và invoke 
>  các capability đó theo chuẩn chung." 
>  " Supervisor-worker nói về vai trò. MCP nói về ổ cắm chuẩn để agent dùng tài nguyên bên 
>  ngoài. Giống USB: mọi thiết bị cùng dùng một chuẩn kết nối." 
>  Tools — "hành động: search, query API, tạo ticket, gọi webhook" · 
>  Resources — "tài nguyên để đọc: file, schema, catalog, config, DB" · 
>  Prompts — "prompt dùng lại, giúp chuẩn hoá cách gọi năng lực và giảm lỗi 
>  prompt "

Phép so sánh USB đúng và đáng nhớ, nhưng nó giấu điều làm MCP thú vị hơn một chuẩn cắm thông thường: **USB không tự mô tả nó là gì, còn MCP thì có.**

|  | Là gì | Agent làm gì với nó | Tương đương ở Ngày 8 |
| --- | --- | --- | --- |
| Tools | Hành động có side effect | Gọi để làm gì đó | search_internal_docs() |
| Resources | Dữ liệu để đọc | Đọc để biết gì đó | Chunk trong vector store |
| Prompts | Mẫu prompt dùng lại, do server cung cấp | Dùng để gọi năng lực đúng cách | Không có tương đương |

Prompts là thứ đáng chú ý nhất

client

server

"giảm lỗi prompt"

người tích hợp

người xây tool

chi phí kỹ thuật

biết tool làm 
 gì

giới hạn năng lực

không thể tự khám phá

tool discovery ở slide 39

"tiết kiệm công tích hợp"

"agent làm được thứ mà lúc viết code chưa ai nghĩ tới"

### Slide 39–41 Tool discovery — và vì sao đây là phần đáng nhớ nhất

> Trích slide 
>  Luồng discovery: "1. Agent kết nối tới MCP server · 2. Gọi tools/list · 3. Mỗi tool 
>  trả về: name, description, inputSchema · 4. Agent đọc schema, quyết định 
>  tool nào phù hợp · 5. Gọi tools/call với đúng parameters · 6. Server thực thi 
>  và trả kết quả" 
>  " Agent không cần được lập trình sẵn biết tool 'X' tồn tại. Nó có thể khám phá khi chạy và 
>  tự điều chỉnh theo tool nào có sẵn. " 
>  Ví dụ: "Tool Worker cần tra policy mới nhất → gọi MCP server knowledge-base → server 
>  expose search_policy, get_faq → worker gọi 
>  search_policy(query, date_after) → kết quả JSON chuẩn kèm source" 
>  Lợi ích: "team cập nhật policy → chỉ cần update MCP server · supervisor và 
>  workers không cần sửa khi tool thay đổi · thêm tool mới = thêm endpoint · dễ audit 
>  ai đã gọi tool gì và khi nào" 
>  " MCP tạo ecosystem effect: agent dùng được nhiều năng lực hơn mà không phải mỗi lần đều 
>  tích hợp lại từ đầu. "

name

description

inputSchema

inputSchema

đúng cú pháp

name

description

chính xác

Mini-Quest 1

description:

"đây chính là tín hiệu route cho 
 supervisor"

chọn worker nào

chọn tool nào

Hệ quả thực dụng:

description: "search policies"

"search internal HR policies by keyword; 
 supports date_after to filter out superseded versions; returns chunks with source citation"

"dễ audit ai đã gọi tool gì và khi nào"

kiến trúc

một chỗ duy nhất

slide 48

"biết rõ ai được gọi ai — không phải 
 agent nào cũng được chạm mọi capability"

chỗ

tools:

slide 17

trust boundary

"Agent không cần được lập trình sẵn biết tool 'X' tồn tại."

description

description

indirect prompt injection

Ngày 8 · slide 83

Đối sách ở mức Ngày 9:

danh sách MCP server được 
 phép

_Sơ đồ: MCP và A2A là hai trục khác nhau trên cùng một kiến trúc - Trên cùng là supervisor. Ba mũi tên đi xuống từ supervisor tới ba worker là retrieval worker, tool worker và synthesis worker; đây là trục A2A, agent giao việc cho agent, và mỗi mũi tên mang theo một message contract gồm task, context và expected output. Từ mỗi worker có một mũi tên đi xuống tới một MCP server tương ứng là vector database, external API và formatter; đây là trục MCP, agent kết nối với năng lực bên ngoài qua một surface chuẩn gồm tools, resources và prompts. Bảng dưới cùng phân biệt hai trục: MCP là agent nói chuyện với tool, mục tiêu là kết nối năng lực, trọng tâm là surface chuẩn, và tool không có quyền quyết định, chỉ thực thi. A2A là agent nói chuyện với agent, mục tiêu là chia việc và đồng bộ, trọng tâm là message contract, và phía bên kia có thể ra quyết định. Câu chốt: MCP trả lời câu hỏi agent lấy năng lực ở đâu, A2A trả lời câu hỏi agent giao việc cho ai._

Hình 2 — MCP và A2A là hai trục khác nhau trên cùng một kiến trúc.

slide 41

slide 43

vẽ hai trục trên cùng một hình

---

<!-- chiron-source-span: {"source_span_id":"8c1db704-5e18-5ea0-8412-fdf023d90018","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 A2A — message contract giữa các agent","source_file":"slide-day09.html"},"checksum":"8afe924f83ad318955db9c08464d9155d06574053a19b52bc58385bdc76cafe7"} -->

## 08 A2A — message contract giữa các agent

Chương này chứa nguyên tắc *"need to know"* — một nguyên tắc bảo mật cổ điển 
 được áp cho một bài toán mới, và nó giải quyết cả chi phí lẫn chất lượng cùng lúc.

### Slide 43–44 MCP so với A2A, và cái giá của contract mơ hồ

> Trích slide 
>  MCP: "agent nói chuyện với tool/capability · mục tiêu là kết nối năng lực bên 
>  ngoài · trọng tâm là surface chuẩn · tool không có agency — chỉ thực thi " · 
>  A2A: "agent nói chuyện với agent khác · mục tiêu là chia việc và đồng bộ · trọng 
>  tâm là message contract rõ ràng · agent phía kia có thể ra quyết định " 
>  " MCP trả lời câu hỏi agent lấy năng lực ở đâu, còn A2A trả lời câu hỏi agent giao việc 
>  cho ai. " 
>  Không có contract rõ: "supervisor gọi worker với: 'Hãy tìm policy liên quan' · worker 
>  không biết context là gì · worker trả về 10 kết quả không được lọc · supervisor 
>  không biết kết quả nào dùng được · lỗi lộ ra ở phần tổng hợp, nhưng gốc là ở phần gọi "

Dòng cuối là dòng đáng nhớ, vì nó mô tả một **lỗi lệch địa chỉ** — và đó là loại lỗi 
 tốn nhiều thời gian debug nhất trong hệ multi-agent:

"Hãy tìm policy liên quan"

Không có gì sai ở đây.

Bước ④ là chỗ mất thời gian.

chính xác

Mini-Quest 3

print(formatted_context)

Ngày 8

chỗ bạn thấy lỗi gần như không bao giờ là chỗ lỗi sinh ra

|  | Gọi tool qua MCP | Giao việc cho agent qua A2A |
| --- | --- | --- |
| Đầu ra | Xác định bởi input và schema | Có thể khác nhau mỗi lần |
| Retry | An toàn — cùng input cho cùng output | Có thể ra kết quả khác; phải xử lý |
| Validate đầu ra | Theo schema — máy làm được | Phải kiểm cả nội dung, không chỉ hình thức |
| Nó có thể "hiểu sai" không | Không | Có |

có thể

slide 48

"validate đầu ra trước khi dùng — worker 
 hoàn toàn có thể trả về schema sai"

expected output

### Slide 45–47 Contract ba phần, nguyên tắc "need to know", và sync/async

> Trích slide 
>  Contract tối thiểu: Task — "agent kia cần làm gì?" · Context — 
>  "những gì worker cần biết để làm đúng: query, constraints, user role, state" · 
>  Expected output — "trả về theo format nào?" 
>  task = "retrieve evidence" 
> context = "user hoi ve refund policy, uu tien tai lieu sau 2025" 
> expected_output = "top 3 chunks + source + confidence" 
>  Thiếu context: "worker lấy kết quả không phù hợp · phải gọi lại nhiều 
>  lần · debugging rất khó" · Quá nhiều context: "tốn token không cần thiết · 
>  worker xử lý chậm · khó maintain khi schema thay đổi" 
>  " Nguyên tắc 'need to know': worker chỉ nhận context mà nó thực sự cần. Không thêm, không 
>  bớt. Khi không chắc → bắt đầu với ít hơn và thêm khi cần. " 
>  Sync: "đơn giản để hiểu và debug · nhưng dễ tăng latency toàn luồng · 
>  bắt đầu ở đây cho Day 09 " · Async: "hợp khi nhiều worker chạy song 
>  song · nhưng cần quản lý trạng thái và timeout tốt hơn"

| Phần contract | Bỏ nó thì gặp anti-pattern nào |
| --- | --- |
| Task — làm gì | Worker đoán mò → kết quả không dùng được |
| Context — cần biết gì | Chatty Workers — hỏi ngược lại supervisor để lấy thông tin thiếu |
| Expected output — trả về hình dạng nào | No Fallback — supervisor không biết kết quả có dùng được không, 
 nên không có tiêu chí để retry |

output hợp lệ trông như thế nào

không có cách nào biết worker đã thất bại

Mini-Quest 3

không

expected output không phải để worker biết trả về gì — nó để supervisor 
 biết khi nào phải retry.

hướng

Thiếu context tạo ra lỗi ồn ào

Thừa context tạo ra lỗi im lặng

Ngày 8

Khi một chiều sai thì ồn và chiều kia sai thì 
 im, hãy bắt đầu ở chiều ồn.

Mô-đun 2

là bao nhiêu

11,8 giây

6,2 giây

1,9 lần

chi phí không đổi.

thời gian chờ

độ phức tạp quản lý 
 trạng thái

Đổi sang async khi latency thật sự thành 
 vấn đề của người dùng

### Slide 48 Trust boundary — bốn câu hỏi bảo mật trong hệ nhiều agent

> Trích slide 
>  " Biết rõ ai được gọi ai: không phải agent nào cũng được chạm mọi capability · 
>  Biết dữ liệu nào được truyền đi: tránh đẩy thừa PII hoặc state nhạy cảm · 
>  Biết output nào cần xác thực lại: đặc biệt khi worker chạm tool ngoài · 
>  Validate đầu ra trước khi dùng: worker hoàn toàn có thể trả về schema sai" 
>  " Đừng giả định mọi agent đều đáng tin như nhau. Hệ nhiều agent vẫn cần trust boundary. "

| Câu hỏi của slide 48 | Cài đặt cụ thể | Thấy ở đâu |
| --- | --- | --- |
| Ai được gọi ai | max_depth = 1 — worker không đẻ worker | Slide 17,.codex/config.toml |
| Ai được chạm capability nào | tools: [Read, Grep, Glob] — không có Write | Slide 17, vn-content-reviewer |
| Dữ liệu nào được truyền đi | Nguyên tắc "need to know" | Slide 46 |
| Output nào cần xác thực lại | expected_output trong contract + validate | Slide 45 |

Hàng thứ hai là hàng đáng học nhất

ràng buộc

đề nghị

Write

không thể

mọi ràng buộc quan trọng phải nằm ngoài prompt.

"Đừng giả định mọi agent đều đáng tin như nhau."

Ngày 8 · slide 83

indirect prompt injection

Ngày 7 · slide 83

làm dài thêm

Đối sách ở mức Ngày 9:

trước khi

---

<!-- chiron-source-span: {"source_span_id":"134cc463-fc6d-5f12-82cd-1316f790457d","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 LangGraph — node, edge, state","source_file":"slide-day09.html"},"checksum":"e9d5e8673ce151cca48601573bf4738af1c36468b0a1fa84fd071f6ee913b5c4"} -->

## 09 LangGraph — node, edge, state

Deck rút gọn LangGraph xuống ba khái niệm và nói thẳng rằng ba cái đó là đủ cho Ngày 
 9. Đó là một quyết định sư phạm tốt và cũng chính xác về kỹ thuật.

### Slide 50–52 Vì sao cần framework, và ba khái niệm là đủ

> Trích slide 
>  Không có framework: " routing logic nằm trong prompt điều phối dài · khó biết hệ 
>  đang ở bước nào · thêm một nhánh mới = sửa toàn bộ prompt · debug bằng 
>  print() và hy vọng" 
>  Với LangGraph: " routing trở thành code tường minh. Graph có thể visualize. State 
>  có schema. Human-in-the-loop có điểm rõ ràng." 
>  " node = ai làm · edge = đi đâu tiếp · state = hệ đang biết gì. Ba khái niệm này 
>  là toàn bộ LangGraph bạn cần cho Day 09." 
>  Node: "một hàm Python nhận state và trả state mới" · Edge: 
>  " unconditional — luôn đi từ A sang B; conditional — hàm trả về tên node 
>  tiếp theo dựa trên state " · State: "TypedDict hoặc Pydantic được truyền 
>  qua mỗi node… State là 'bộ nhớ' của cả graph."

|  | Routing trong prompt | Routing trong code |
| --- | --- | --- |
| Đọc được không | Phải đọc một prompt dài để đoán | Đọc hàm route_to_worker là xong |
| Test được không | Phải gọi LLM mới biết | Unit test thuần — không cần LLM |
| Tất định không | Không — cùng input có thể route khác | Có |
| Thêm nhánh mới | Sửa prompt, và mọi nhánh cũ có thể lệch theo | Thêm một if và một entry trong map |

ví dụ code slide 54

route_to_worker

không gọi LLM

state["need_tool"]

state["need_retrieval"]

supervisor node

đặt

quyết định

định tuyến

| Khái niệm LangGraph | Câu hỏi thiết kế ( slide 15 ) |
| --- | --- |
| node = ai làm | ① Chia trách nhiệm ở đâu? |
| state = hệ đang biết gì | ② Thông tin đi theo con đường nào? |
| edge = đi đâu tiếp | ③ Lỗi ở đâu là ít tổn hại nhất? |

là

conditional edge chính là chỗ bạn cài đặt câu trả lời cho "lỗi ở đâu 
 ít tổn hại nhất"

### Slide 53–56 Routing code, supervisor node tối giản, và human-in-the-loop

> Trích slide 
>  def route_to_worker(state: AgentState) -> str: 
>  if state["need_tool"]: return "tool_worker" 
>  if state["need_retrieval"]: return "retrieval_worker" 
>  return "synthesis_worker" 
>  
> graph.add_conditional_edges("supervisor", route_to_worker, {... }) 
>  "Ý chính không nằm ở syntax mà ở chỗ: routing trở thành logic tường minh, thay vì ẩn 
>  trong một prompt điều phối rất dài. " 
>  def supervisor_node(state: AgentState) -> AgentState: 
>  decision = llm.invoke(SUPERVISOR_PROMPT.format(task=state["task"])) 
>  return { 
>  **state, 
>  "need_retrieval": decision.need_retrieval, 
>  "need_tool": decision.need_tool, 
>  "trace": state["trace"] + [f"[supervisor] retrieval={...} tool={...}"], 
>  } 
>  " supervisor node không làm việc của worker — nó chỉ ra quyết định route · trả về 
>  dict mới ( **state ) thay vì sửa state tại chỗ · trace được append, không 
>  overwrite " 
>  Human-in-the-loop nên chèn khi: "task có rủi ro cao (tài chính, y tế, pháp lý) · 
>  confidence score dưới ngưỡng · tool action có side effect không đảo 
>  ngược · output sẽ đi ra user hoặc stakeholder · hệ thống không chắc về intent ban đầu" 
>  " Multi-agent không đồng nghĩa với full autonomy. Nhiều hệ tốt nhất là hệ biết khi nào nên 
>  dừng để con người quyết định. "

|  | Bản sai ( slide 32 ) | Bản đúng (slide 55) |
| --- | --- | --- |
| Có tự làm việc worker không | Có — gọi vector_store.search và 
 tool_worker() | Không — chỉ đặt cờ |
| Trace | state["trace"] = [...] — ghi đè | state["trace"] + [...] — append |
| State | Sửa tại chỗ rồi return state | return {**state,...} — dict mới |
| Số dòng thực sự làm việc | 6 | 1 (một lần gọi LLM) |

God Supervisor

thật sự làm gì đó

một

Nếu supervisor node của bạn dài hơn mười dòng, gần như chắc chắn nó đang làm việc 
 của worker.

ngưỡng

side effect không đảo ngược

một khi đã làm thì không lùi lại được

Ngày 5

p* = 1 − I/(V+C)

C — chi phí khi sai

gần như luôn phải hỏi

Quy tắc thực dụng:

đảo ngược được

không đảo ngược được

interrupt

state được giữ nguyên qua interrupt

persist được

không

debrief Mini-Quest 2

return {**state,...}

state["x"] = v

---

<!-- chiron-source-span: {"source_span_id":"38dc8791-ae58-55c3-82d2-796888930863","locator":{"kind":"html_section","section_id":"c10","order":12,"heading":"10 Observability & Mini-Quest 3","source_file":"slide-day09.html"},"checksum":"486a748739b4607f0185b7cef4c13bb0a504d5461427106478f2a49f11b1b837"} -->

## 10 Observability & Mini-Quest 3

Chương này chứa câu đáng nhớ nhất của cả bài, và nó nằm ở debrief Mini-Quest 3: *"status: ok chỉ có nghĩa là bước này không văng exception."*

### Slide 58–60 Vì sao multi-agent khó debug, và trace entry nên có gì

> Trích slide 
>  "Lỗi có thể xuất phát từ: routing sai, context sai, tool fail, synthesis sai · 
>  lỗi ở bước A có thể chỉ lộ ra ở bước C · nhiều agent = nhiều LLM call = nhiều điểm 
>  fail tiềm năng" 
>  Ba câu hỏi observability: " 1. Agent nào đã chạy, theo thứ tự nào? 2. Input/output tại mỗi 
>  bước là gì? 3. Lỗi hay warning nào đã xảy ra? " 
>  Mỗi entry trace nên có: " timestamp — khi nào · agent_id — ai làm 
>  · action — làm gì · input_summary — nhận gì 
>  ( tóm tắt, không full context ) · output_summary · status — 
>  ok | warn | error · latency_ms " 
>  "Nếu log chỉ có 'agent chạy xong', học viên sẽ không học được gì về orchestration. 
>  Trace tốt phải giúp nhìn thấy đường đi của quyết định. "

Bảy trường của trace entry có một trường đặc biệt hơn sáu trường kia, và cách deck viết nó rất 
 chuẩn:

Kích thước

Đọc được

slide 61

Riêng tư

slide 48

"tránh đẩy thừa PII"

Nhưng tóm tắt cái gì thì mới là câu hỏi khó

Mini-Quest 3

"output": "0 chunks"

tại sao

điểm số cao nhất là bao nhiêu

Ngày 8

Ngày 9 · slide 44

Ngày 9 · Mini-Quest 3

Đây là đặc trưng của mọi pipeline nhiều bước, không riêng gì AI.

đo ở từng bước, đừng chỉ đo kết quả cuối

bộ ba RAGAS

### Slide 61–62 Ba công cụ, và vòng lặp từ trace tới cải thiện

> Trích slide 
>  LangSmith — "tích hợp sẵn với LangChain/LangGraph. Trace tự động, visual flow, 
>  so sánh runs" · JSON log tự viết — "structured output ghi thẳng vào state. 
>  Đơn giản nhất cho Day 09 — dễ đọc, dễ inspect " · OpenTelemetry — 
>  "chuẩn mở cho distributed tracing. Phù hợp khi hệ thống lớn hơn" 
>  "Gợi ý cho lab: bắt đầu với JSON log tự viết vào state. Đây là cách học được nhiều nhất 
>  về cách hệ hoạt động. " 
>  Vòng lặp: " Chạy hệ thống → Đọc trace → Tìm pattern lỗi → Fix: prompt/route/schema → Eval 
>  lại " 
>  " Trace không chỉ để debug lỗi hôm nay. Nó là dữ liệu để cải thiện routing, worker quality, 
>  và message contract theo thời gian. "

"học được nhiều nhất về cách hệ hoạt động"

Ngày 7 · slide 63

để thấy index internals mà Chroma giấu 
 đi

công cụ tốt giấu chi tiết, và giấu chi tiết là điều bạn muốn ở 
 production nhưng không muốn khi đang học.

ghi gì

result_count

"trace này thiếu gì?"

Tìm pattern lỗi

nhiều

dữ liệu

Cùng một worker hay fail

Supervisor hay route sai với một loại câu hỏi

Một bước hay có latency bất thường

nhiều

### Slide 63–64 Mini-Quest 3 — mọi dòng đều "ok", và câu trả lời hoàn toàn sai

> Trích slide 
>  {"t":"09:14:02","agent":"supervisor","action":"route", 
>  "decision":"retrieval_worker","status":"ok","latency_ms":240} 
> {"t":"09:14:03","agent":"retrieval_worker","action":"search", 
>  "input":"chinh sach hoan tien","output":"0 chunks","status":"ok","latency_ms":890} 
> {"t":"09:14:04","agent":"supervisor","action":"route", 
>  "decision":"synthesis_worker","reason":"retrieval done","status":"ok","latency_ms":180} 
> {"t":"09:14:09","agent":"synthesis_worker","action":"synthesize", 
>  "input":"0 chunks","output":"Chinh sach hoan tien la 30 ngay...","status":"ok","latency_ms":5100} 
> {"t":"09:14:09","agent":"supervisor","action":"finalize","status":"ok"} 
>  "Khách hàng báo câu trả lời sai hoàn toàn — công ty không hề có chính sách 30 
>  ngày. Nhưng mọi dòng trace đều status: ok. " 
>  Đáp án: " Dòng 2: retrieval trả 0 chunks nhưng vẫn ghi status: ok — 
>  'không tìm thấy' bị coi là thành công · Dòng 3: supervisor route tiếp mà 
>  không kiểm tra chất lượng evidence · Dòng 4: synthesis worker 
>  nhận 0 chunk vẫn tạo ra câu trả lời → hallucination · Lỗi lộ ra ở cuối 
>  luồng nhưng gốc nằm ở dòng 2 " 
>  Sửa ở ba chỗ: " Contract: expected_output phải cho phép 
>  insufficient_evidence; synthesis từ chối khi không đủ evidence · 
>  Routing: conditional edge — nếu result_count == 0 thì retry với query 
>  khác hoặc chuyển human review · Trace: thêm result_count, 
>  top_score; kết quả rỗng phải là status: warn, không phải 
>  ok " 
>  " status: ok chỉ có nghĩa là 'bước này không văng exception'. Nó không có 
>  nghĩa là kết quả dùng được. "

status: ok

chính xác

Ngày 7

"'không lỗi' không có nghĩa là 'đúng' — 6/14 failure mode không 
 raise exception nào."

đừng suy luận từ việc hệ thống không crash

Sửa cụ thể:

ok

```text
ok    — buoc chay xong VA ket qua dung duoc
warn  — buoc chay xong nhung ket qua DANG NGO (0 ket qua, diem thap, thieu truong)
error — buoc nem exception hoac timeout
```

ok

warn

chính việc phải định nghĩa nó

contract

| Chỗ sửa | Tầng | Nó chặn gì | Nếu chỉ làm được một |
| --- | --- | --- | --- |
| Trace: thêm result_count, top_score; 
 0 kết quả → warn | Quan sát | Không chặn gì — nhưng làm lỗi nhìn thấy được | Làm cái này trước — không thấy thì không sửa được |
| Routing: result_count == 0 → retry hoặc human review | Điều phối | Chặn việc đi tiếp với evidence rỗng | Hiệu quả nhất về mặt chặn lỗi |
| Contract: cho phép insufficient_evidence; synthesis từ chối | Giao tiếp | Chặn hallucination ngay cả khi hai tầng trên hỏng | Là lưới an toàn cuối |

Thứ tự làm nên là: trace → routing → contract.

kiến trúc

vận hành

Ngày 8

print(formatted_context)

làm cho thứ vô hình hiện ra trước, rồi mới sửa

latency_ms

5100

5,1 giây

0 chunk

nhanh hơn

viết dài

Bài học:

latency_ms

đã có sẵn

vòng lặp slide 62

_Sơ đồ: Trace của Mini-Quest 3: mọi dòng đều ok mà câu trả lời hoàn toàn sai - Năm dòng trace theo thứ tự thời gian. Dòng một: supervisor định tuyến sang retrieval worker, trạng thái ok, hai trăm bốn mươi mili giây. Dòng hai được tô đỏ: retrieval worker tìm kiếm và trả về không chunk nào, nhưng trạng thái vẫn ghi là ok; đây là gốc của lỗi. Dòng ba: supervisor định tuyến tiếp sang synthesis worker với lý do retrieval đã xong, mà không kiểm tra chất lượng bằng chứng. Dòng bốn cũng được tô đỏ: synthesis worker nhận không chunk nào mà vẫn sinh ra một câu trả lời đầy đủ về chính sách ba mươi ngày, mất năm nghìn một trăm mili giây, tức chậm bất thường vì nó đang bịa ra nội dung dài. Dòng năm: supervisor kết thúc, trạng thái ok. Bên dưới là ba chỗ phải sửa: thêm trường result_count và top_score vào trace và cho kết quả rỗng trạng thái warn thay vì ok; thêm conditional edge kiểm tra result_count bằng không để retry hoặc chuyển human review; và sửa contract để cho phép giá trị insufficient_evidence và để synthesis từ chối khi không đủ bằng chứng. Câu chốt: status ok chỉ có nghĩa là bước này không văng exception, không có nghĩa là kết quả dùng được._

Hình 3 — Trace của Mini-Quest 3, và ba chỗ sửa.

slide 63–64

latency 5.100 ms

---

<!-- chiron-source-span: {"source_span_id":"26af1bbc-b4a3-56f6-b65f-feccf13723a9","locator":{"kind":"html_section","section_id":"c11","order":13,"heading":"11 Chi phí, độ trễ, độ tin cậy — ba con số deck nêu mà không tính","source_file":"slide-day09.html"},"checksum":"29918a8dc6bf9b65519f2b03d27b11b6f0fbce73de13ffe9bbf44e699d297077"} -->

## 11 Chi phí, độ trễ, độ tin cậy — ba con số deck nêu mà không tính

Slide 66–68 là ba slide ngắn nhất và quan trọng nhất của deck: chúng nói rằng 
 multi-agent tốn hơn, chậm hơn và có nhiều điểm fail hơn — nhưng không nói *bao nhiêu*. Hai mô-đun 
 dưới đây trả lời, và câu trả lời của mô-đun thứ hai là kết quả mạnh nhất của cả bài.

### Slide 66–67 Chi phí và độ trễ

> Trích slide 
>  " Mỗi agent = ít nhất 1 LLM call · supervisor thường là một LLM call riêng · 
>  context bị truyền qua nhiều bước · supervisor không cần là model lớn 
>  nhất — routing là bài toán đơn giản hơn" 
>  " Latency: worker có thể chạy song song, nhưng tăng nếu chạy 
>  serial · Token: mỗi bước lặp lại context → tối ưu bằng 
>  context nhỏ nhất đủ dùng " 
>  " Multi-agent không miễn phí. Nó đổi token và latency lấy khả năng chia bài toán và kiểm 
>  soát context. "

Câu chốt là câu đúng, nhưng nó đặt tỷ giá của phép đổi ở dạng ẩn. Mô-đun 2 làm nó hiện ra.

#### Tương tác Mô-đun 2 — Chi phí và độ trễ: single so với multi

Single-agent = 1 LLM call ôm toàn bộ context. Multi-agent = 1 supervisor + 
 N worker + 1 synthesis, trong đó **mỗi worker chỉ nhận phần context của nó** — đó là cả 
 điểm của việc chia. Giá output lấy bằng 3× giá input (tỷ lệ thông dụng). Supervisor mặc định dùng 
 model nhỏ theo đúng gợi ý slide 66.

Mặc định: context 20.000 token · output 800 token · 3 worker · model lớn $3,00/1M input · 
 model nhỏ $0,30/1M · 2,8 giây mỗi LLM call · supervisor dùng model nhỏ theo gợi ý slide 66.

Đoán trước: *(a)* multi-agent tốn gấp mấy lần single? *(b)* supervisor chiếm bao 
 nhiêu phần trăm tổng chi phí? *(c)* hạ cấp supervisor xuống model nhỏ tiết kiệm được bao 
 nhiêu phần trăm?

#### Kéo rồi mở

**(a) Chỉ ×1,24** — $0,0834 so với $0,0672. Gần như ai cũng đoán cao hơn nhiều, 
 vì trực giác đếm *số call* (5 so với 1). Nhưng bạn trả tiền cho *token*, và mỗi 
 worker chỉ nhận 20.000 ÷ 3 + 500 token. Chia chứ không nhân.

**(b) Supervisor chiếm 1,0%** — $0,0009 trên $0,0834. Worker chiếm 86,0%, 
 synthesis 13,0%. Đây là lý do khoản tiết kiệm ở (c) nhỏ hơn bạn tưởng.

**(c) 8,6%.** Không nhỏ, nhưng cũng không phải lý do đủ để đánh đổi chất lượng 
 routing. Khoản tiết kiệm *thật* khi hạ cấp supervisor nằm ở độ trễ: 2,2 giây, tức 
 khoảng 26% tổng latency — lớn hơn ba lần khoản tiền.

- **Control - Context đầu vào**: min `4`, max `120`, step `2`, default `20`

- **Control - Output**: min `2`, max `40`, step `1`, default `8`

- **Control - Số worker**: min `2`, max `8`, step `1`, default `3`

- **Control - Giá model lớn**: min `25`, max `1500`, step `25`, default `300`

- **Control - Giá model nhỏ**: min `5`, max `300`, step `5`, default `30`

- **Control - Độ trễ mỗi LLM call**: min `8`, max `120`, step `2`, default `28`

Chi phí so với single

Độ trễ so với single

Số LLM call

Hạ cấp supervisor tiết kiệm

Ba điều đọc được ở mặc định.

Chi phí tăng ×1,24

một phần

Độ trễ tăng ×2,2 dù đã chạy song song

Hạ cấp supervisor chỉ tiết kiệm 8,6%.

| Khoản | Ở mặc định | Phần trăm | Nó đến từ đâu |
| --- | --- | --- | --- |
| Worker (3 cái) | $0,0717 | 86,0% | Mỗi worker nhận 20.000 ÷ 3 + 500 token — chia chứ không nhân |
| Synthesis | $0,0108 | 13,0% | Tóm tắt của 3 worker + toàn bộ output cuối |
| Supervisor | $0,0009 | 1,0% | 2.000 token vào, model nhỏ |

Toàn bộ phần "thêm" so với single agent nằm ở +500 token overhead mỗi worker và ở bước 
 synthesis.

Lý do thật để dè dặt 
 với multi-agent là latency và độ tin cậy, không phải tiền.

8,6%

tốt

độ trễ

tiết kiệm 2,2 giây trên đường đi nghiêm 
 ngặt

tốt hơn nữa

route_to_worker

không

Phép thử:

God Supervisor

### Slide 68 Failure mode — và nghịch lý mà deck không nêu thành số

> Trích slide 
>  " Timeout — worker treo · Retry — thử lại có kiểm soát · 
>  Fallback — đường đi thay thế · Partial failure — trả lời với những 
>  gì có" 
>  " Hệ nhiều agent có nhiều điểm fail hơn. Thiết kế cho lỗi từ đầu, đừng chờ lỗi xảy ra rồi 
>  mới thêm. "

"Nhiều điểm fail hơn" nghe như một cảnh báo mềm. Nó không mềm — nó là một phép nhân, và phép nhân 
 đó có thể ăn hết lợi ích của việc chia việc. Mô-đun 3 tính:

#### Tương tác Mô-đun 3 — Nghịch lý "No Fallback": khi chia việc làm hệ kém tin cậy đi

Mỗi worker thất bại độc lập với xác suất p. Sau r lần thử lại, 
 xác suất thất bại còn `p r+1`. Nếu hệ cần **đủ cả N worker** thành 
 công thì xác suất thành công là `(1 − p r+1 ) N`; nếu hệ **chịu được 1 worker hỏng** (partial failure — chính là mục thứ tư của slide 68) thì 
 dùng xác suất có ít nhất N−1 worker thành công. So sánh với single-agent, vốn chỉ có **một** điểm fail: 1 − p.

Mặc định: 3 worker · mỗi worker thất bại 5,0% · không retry · hệ cần **đủ cả ba** worker thành công. Single-agent tương đương có đúng một điểm fail 5,0%.

Đoán trước: *(a)* hệ multi-agent thành công bao nhiêu phần trăm — hơn hay kém single? *(b)* cần mấy lần retry để multi bằng single? *(c)* nâng lên 5 worker thì con số đi 
 về đâu?

#### Kéo rồi mở

**(a) 85,74% — kém hơn single (95,00%) tới 9,26 điểm.** Đây là kết quả phản trực 
 giác nhất của cả bài. Chia việc *không* tự làm hệ tin cậy hơn; nó nhân số điểm fail lên.

**(b) Đúng một lần.** Một retry đưa multi lên 99,25% — vượt single. Toàn bộ lợi 
 ích độ tin cậy của multi-agent nằm ở đây, không nằm ở việc chia vai.

**(c) Tụt xuống 77,38%.** Càng chia nhỏ càng tệ, nếu không có gì đỡ. Bấm sang 
 "chịu được 1 worker hỏng" để thấy nhánh kia của slide 68: partial failure một mình cũng đưa 
 3 worker lên 99,28% mà *không cần* retry.

- **Control - Số worker**: min `1`, max `10`, step `1`, default `3`

- **Control - Xác suất fail mỗi worker**: min `2`, max `200`, step `2`, default `50`

- **Control - Số lần retry**: min `0`, max `4`, step `1`, default `0`

Cần ĐỦ N worker thành công

Chịu được 1 worker hỏng (partial failure)

Multi-agent thành công

Single-agent thành công

Chênh lệch

Retry tối thiểu để hoà

Kết quả mạnh nhất của cả bài, ở đúng cấu hình mặc định.

85,74%

95,00%

Multi-agent kém hơn 9,26 điểm.

không cần retry

| Cấu hình (p = 5% mỗi điểm fail) | Thành công | So với single 95,00% |
| --- | --- | --- |
| Single agent | 95,00% | — |
| 3 worker, cần đủ cả ba, không retry | 85,74% | kém 9,26 điểm |
| 3 worker, cần đủ cả ba, 1 retry | 99,25% | hơn 4,25 điểm |
| 3 worker, chịu được 1 hỏng, không retry | 99,28% | hơn 4,28 điểm |

là

"No Fallback"

chỗ

99,998%

① Các worker fail độc lập.

giảm

② Retry độc lập với lần trước.

hay sai

Mini-Quest 3

p²

p

với query khác

③ p giống nhau ở mọi worker.

Điều nào cũng không lật kết luận

trần trên

ba trong bốn cơ chế đều cần thứ mà bạn phải quyết định lúc thiết kế.

| Cơ chế | Nó cần cái gì đã có sẵn | Thêm sau thì phải sửa gì |
| --- | --- | --- |
| Timeout | Không cần gì | Thêm bất cứ lúc nào — dễ nhất |
| Retry | Node không sửa state tại chỗ 
 ( Mini-Quest 2 ) | Viết lại mọi node |
| Fallback | Conditional edge + biết khi nào là fail 
 ( expected_output ) | Viết lại contract và routing |
| Partial failure | Synthesis chấp nhận kết quả thiếu | Viết lại synthesis worker và prompt của nó |

Chúng không phải 
 phong cách — chúng là điều kiện tiên quyết của khả năng chịu lỗi

---

<!-- chiron-source-span: {"source_span_id":"979ee263-57ce-5146-bfc0-62f2f3cd6a25","locator":{"kind":"html_section","section_id":"c12","order":14,"heading":"12 Lab 9 & tổng kết","source_file":"slide-day09.html"},"checksum":"79e401c5aa9acccdff2c584d492abb9dcb634599b7204705dbc2e32d9b81d6df"} -->

## 12 Lab 9 & tổng kết

Lab 9 không xây hệ mới — nó *tách* artifact Ngày 8. Đó là một lựa chọn đề bài 
 tốt, vì nó buộc bạn đối diện với chính câu hỏi của slide 15: chia trách nhiệm ở đâu.

### Slide 70–72 Phân bổ thời gian, prerequisite, ba cấp độ

> Trích slide 
>  "50' lý thuyết · 20' Mini-Quest 1 · 40' supervisor-worker deep dive · 20' Mini-Quest 2 · 
>  45' MCP + A2A · 30' LangGraph · 25' observability + cost/reliability · 20' Mini-Quest 3 · 
>  90' Lab 9 " 
>  Prerequisite: " Artifact Day 08 đang hoạt động · TypedDict và type hints · 
>  dictionary operations · async/await nếu đi vào async A2A" 
>  " Lưu ý: Học viên chưa có artifact Day 08 hoạt động nên dành 30 phút đầu để fix artifact 
>  trước khi bắt đầu lab Day 09. " 
>  Cấp 1 Foundation: "giải thích 4 giới hạn · vẽ sơ đồ supervisor-worker · phân biệt MCP và A2A" · 
>  Cấp 2 Implementation: "build supervisor + 2 worker với shared state · viết message contract · 
>  dùng MCP cho 1 tool worker" · Cấp 3 Mastery: " LangGraph có conditional routing · trace log 
>  đọc được và actionable · giải thích trade-off cost/reliability "

Tổng thời lượng là **340 phút — 5 giờ 40 phút**, trong đó Lab chiếm **26,5%** và ba Mini-Quest cộng lại 60 phút (17,6%).

30 phút

một phần ba thời lượng lab

tách

Đối sách:

trước buổi học

bước 1

| Cấp | Deck yêu cầu | Học ở đâu trong tài liệu này |
| --- | --- | --- |
| 1 — Foundation | 4 giới hạn, sơ đồ, phân biệt MCP/A2A | Chương 01 + Hình 1 · Hình 2 |
| 2 — Implementation | Build supervisor + 2 worker, contract, MCP | Chương 05 · Chương 08 · thang 3 bước |
| 3 — Mastery | Conditional routing, trace actionable, 
 giải thích trade-off cost/reliability | Chương 09 · Hình 3 · 
 Mô-đun 2 và Mô-đun 3 |

"giải thích được trade-off cost/reliability"

giải thích một sự đánh đổi định lượng

### Slide 76–80 Lab 9 — sáu bước, shared state, MCP, blueprint nộp

> Trích slide 
>  Mục tiêu: "biến một agent RAG đơn thành một hệ multi-agent nhỏ có route rõ, capability 
>  rõ, và trace rõ ". Sáu bước: "① tách artifact Day 08 thành supervisor + 2–3 worker · 
>  ② thiết kế shared state schema với trường trace · ③ chọn 1 worker dùng external 
>  capability qua MCP · ④ viết message contract tối thiểu · ⑤ trace lại toàn bộ luồng · ⑥ demo kèm 
>  reasoning flow" 
>  Kiểm tra trước khi tách: " Mỗi phần có thể test độc lập không? Nếu không, chưa tách đủ 
>  rõ. Supervisor có thực sự cần ra quyết định về phần đó không? Nếu không, tách ra là 
>  dư thừa. " 
>  class Day09State(TypedDict): 
>  task: str 
>  user_context: dict 
>  plan: list[str] 
>  retrieval_result: list[dict] 
>  tool_result: dict 
>  synthesis_draft: str 
>  final_answer: str 
>  status: str 
>  trace: list[dict] 
>  error: Optional[str] 
>  Nguyên tắc state: " trace là list — luôn append, không overwrite · error là 
>  Optional để graceful fail · worker chỉ ghi vào field của mình · supervisor đọc tất 
>  cả, ghi plan · không để field 'không ai biết ai sở hữu' " 
>  Blueprint nộp: "1 supervisor routing rõ · 2–3 worker rõ vai trò · 1 MCP-connected capability · 
>  shared state có trace" — Evidence: "trace đọc được · output kèm source · ghi chú route hợp lý chưa 
>  và tại sao · ít nhất 1 ví dụ về worker fail gracefully "

| Câu hỏi | Nó lọc ra cái gì | Anti-pattern tương ứng |
| --- | --- | --- |
| "Mỗi phần test độc lập được không?" | Tách chưa đủ — hai worker còn dính nhau | Chatty Workers — phải hỏi nhau mới làm được |
| "Supervisor có thực sự cần quyết định không?" | Tách quá nhiều — worker không cần tồn tại riêng | Multi-agent khi single là đủ ( slide 14 ) |

slide 14

"nếu single-agent làm 
 được thì đừng chia"

viết được unit test cho worker mà không phải mock worker kia không?

"Không để field 'không ai biết ai sở hữu'."

Day09State

retrieval_result

tool_result

synthesis_draft

final_answer

plan

trace

mọi

chỉ 
 vì

status

không

status="warn"

status="ok"

Mini-Quest 3

Sửa:

status

list[str]

field nhiều node ghi thì phải append-only, hoặc phải có đúng một chủ.

Mô-đun 3

nếu không có nó, hệ 3 worker của bạn tin cậy 85,7% — kém hơn agent đơn ở Ngày 8 mà bạn vừa 
 tách ra.

bảng ở chương 11

quyết định kiến trúc

Đề nghị thực dụng:

bước 2

luôn ném lỗi

### Slide 81–85 Rubric, năm takeaway, và câu hỏi khép lại

> Trích slide 
>  Rubric 5 tiêu chí × 3 mức. Phân vai trò: đạt "supervisor + 2 workers" → xuất sắc 
>  " tránh anti-pattern có ý thức " · MCP: đạt "1 MCP call hoạt động" → 
>  xuất sắc " discovery đúng, có error handling " · Shared state: → 
>  xuất sắc " ownership rõ từng field " · Trace quality: đạt "log cơ 
>  bản" → tốt " đủ 5 trường cần thiết " → xuất sắc " actionable, dẫn tới 
>  insight " · Routing logic: → xuất sắc " giải thích được quyết định 
>  route " 
>  Takeaway: "① multi-agent là chia vai trò — chỉ dùng khi bài toán thực sự cần · 
>  ② supervisor-worker là pattern practical nhất để bắt đầu · ③ MCP nối agent với tool; A2A cho agent 
>  giao việc bằng message contract rõ · ④ LangGraph biến orchestration thành graph có state và 
>  conditional routing · ⑤ observability là điều kiện tiên quyết: trace tốt là dữ liệu để cải 
>  thiện hệ thống lâu dài " 
>  Slide 85: " Một agent rất giỏi có thể làm nhiều việc. Nhưng hệ thống tốt hơn thường bắt 
>  đầu từ câu hỏi: nên chia vai trò ở đâu để dễ kiểm soát và dễ cải thiện nhất? "

| Tiêu chí | Mức xuất sắc | Chuẩn bị được không |
| --- | --- | --- |
| Phân vai trò | "tránh anti-pattern có ý thức " | Được — viết ra bốn anti-pattern và bạn đã tránh chúng thế nào |
| Shared state | "ownership rõ từng field" | Được — một comment cạnh mỗi field ghi node nào ghi nó |
| Routing logic | "giải thích được quyết định route" | Được — nếu routing nằm trong code chứ không trong prompt |
| MCP | "discovery đúng, có error handling" | Được — gọi list_tools() thay vì hard-code tên tool |
| Trace quality | " actionable, dẫn tới insight " | Không hoàn toàn — insight phụ thuộc vào bạn tìm được gì |

dẫn tới

Nhưng bạn tăng xác suất được.

Mini-Quest 3

result_count

top_score

warn

warn

không 
 có

cách xây

cách hệ tốt lên theo thời gian

"trace tốt là dữ liệu để cải thiện hệ 
 thống lâu dài."

Mini-Quest 3

result_count

Slide 62

nhiều

Mô-đun 3

trace không phải công cụ debug, nó là bộ đo của hệ.

Ngày 8 nói về RAGAS

Ngày 7 nói về 
 recall@k

"Nếu supervisor và workers làm đúng nhưng user không hiểu 
 chuyện gì vừa xảy ra, trải nghiệm có đủ tốt không?"

làm vấn đề đó nặng thêm

Mô-đun 2

×2,2

Mini-Quest 3

hiển thị tiến trình

confidence indicator

---

<!-- chiron-source-span: {"source_span_id":"b5896558-db7b-5ae5-adbf-c5428a57b08a","locator":{"kind":"html_section","section_id":"ladder","order":15,"heading":"▤ Luyện kỹ năng cốt lõi: quyết định chia vai ở đâu — và chứng minh được quyết định đó","source_file":"slide-day09.html"},"checksum":"8b55920f5dadd7214f49482a786cc7153ec4c70f3f67ffc8f663379fc025d5ce"} -->

## ▤ Luyện kỹ năng cốt lõi: quyết định chia vai ở đâu — và chứng minh được quyết định đó

Ba bài giảm dần giàn giáo. Kỹ năng được luyện là kỹ năng bị chấm trong Lab 9: *vai trò rõ, không overlap · tránh anti-pattern có ý thức · giải thích được quyết định route*.

Bài toán hiện tại quá tải ở [giới hạn nào trong bốn]. Tôi tách thành [N] worker vì 
 [mỗi worker test độc lập được / supervisor thật sự phải quyết định giữa chúng]. Thông tin đi qua 
 [những field nào của state], mỗi field có chủ là [ai ghi]. Khi [worker nào] hỏng thì hệ 
 [retry / fallback / trả lời thiếu], và điều đó đưa độ tin cậy từ [X] lên [Y].

giới hạn nào

ai ghi field nào

shared state không chủ

khi hỏng thì sao

Mô-đun 3

kém tin cậy hơn

#### Một đồng nghiệp nói: 
 "Con agent RAG của mình chạy chậm và hay trả lời lung tung. Chia thành 4 agent chắc là ổn hơn." 
 Trả lời câu đó bằng một quyết định có căn cứ

Đọc cách *lập luận*, không chỉ đáp án.

1. Đừng vẽ graph ngay — trước hết hỏi nó đang chạm giới hạn nào. 
 Slide 10–13 cho bốn giới hạn: context, độ chính xác của một prompt ôm hết, khả 
 năng chuyên biệt, và khả năng quan sát. Câu của đồng nghiệp nêu hai triệu chứng — chậm và 
 trả lời lung tung — nhưng chưa nêu giới hạn nào. 
 Và đây là chỗ quan trọng: chia vai trò không sửa được "chậm". 
 Mô-đun 2 cho thấy multi-agent chậm hơn ×2,2 ngay cả khi chạy 
 song song. Nếu vấn đề là latency thì chia vai làm nó tệ đi, không tốt lên. 
 Còn "trả lời lung tung" thì có thể chia vai giúp được — nhưng chỉ khi nguyên nhân là 
 một prompt ôm quá nhiều nhiệm vụ. Nếu nguyên nhân là retrieval kém (Ngày 8) thì chia vai không đụng 
 tới nó.
2. Đo trước khi chia — và cái cần đo là "prompt hiện tại đang làm bao nhiêu việc". 
 Ba số, lấy được trong một buổi: 
 ① System prompt dài bao nhiêu token, và nó mô tả bao nhiêu nhiệm vụ khác nhau — đếm số 
 câu bắt đầu bằng một động từ nhiệm vụ ("tìm", "tóm tắt", "định dạng", "kiểm tra"). 
 ② Context thực tế dùng bao nhiêu phần trăm cửa sổ — chạy 20 truy vấn thật và in ra. 
 Mô-đun 1 cho thấy nếu con số này dưới 60% thì giới hạn context không 
 phải vấn đề của bạn. 
 ③ Trong 20 câu trả lời sai, bao nhiêu sai vì thiếu chứng cứ và bao nhiêu sai vì có chứng cứ 
 mà dùng sai — phân loại tay. Loại thứ nhất là bài toán Ngày 8; chỉ loại thứ hai mới có thể 
 hưởng lợi từ việc chia vai. 
 Vì sao ba số này trước: vì nếu ② dưới 60% và ③ nghiêng về "thiếu chứng cứ" thì 
 câu trả lời đúng là đừng chia — và bạn vừa tiết kiệm 90 phút lab cùng một hệ phức tạp hơn 
 mà không tốt hơn.
3. Nếu quyết định chia, hãy chia theo năng lực chứ không theo bước. 
 Slide 24 nói worker phải "chuyên một năng lực hẹp". Bốn agent là con số 
 đồng nghiệp đưa ra tuỳ tiện; con số đúng đến từ việc trả lời: mỗi phần test độc lập được 
 không ( bước 1 của Lab ). 
 Với một agent RAG, câu trả lời thường là ba: retrieval (vector search + rerank), 
 tool (gọi API ngoài), synthesis (sinh câu trả lời). Đó cũng chính là gợi ý của 
 slide 77, và không phải tình cờ — ba phần đó có ba loại đầu vào khác nhau, ba 
 loại lỗi khác nhau, và ba cách test khác nhau. 
 Bốn thì thừa ở đâu? Thường là ở chỗ tách "rerank" thành worker riêng. Nhưng 
 rerank luôn chạy ngay sau retrieval, supervisor không bao giờ phải quyết định có rerank hay 
 không — nên theo phép thử thứ hai của slide 77, tách nó ra là dư thừa.
4. Viết message contract trước khi viết code worker. Ba phần theo 
 slide 45, và phần thứ ba là phần hay bị bỏ: 
 task = "retrieve evidence" 
context = "user hoi ve chinh sach hoan tien; uu tien tai lieu sau 2025-01" 
expected_output = "top 3 chunk + source + score; NEU KHONG DU thi tra 
 insufficient_evidence" 
 Vế thứ hai của expected_output là vế cứu bạn khỏi 
 Mini-Quest 3. Không có nó, supervisor không có cách nào biết retrieval đã thất 
 bại, vì "0 kết quả" cũng là một kết quả hợp lệ về mặt schema.
5. Quyết định chỗ đặt retry ngay lúc này, không để sau. 
 Mô-đun 3 ở ba worker, p = 5%: không retry → 85,7%, kém hơn 
 agent đơn (95,0%) 9,3 điểm. Một retry → 99,3%. 
 Nghĩa là câu trả lời cho đồng nghiệp không phải "chia hay không chia", mà: 
 "chia thành ba, và nếu không có retry thì đừng chia." 
 Và retry phải là retry với query khác, không phải thử lại y hệt — vì nếu worker fail do 
 query không khớp thì lặp lại sẽ fail y hệt.
6. Câu trả lời hoàn chỉnh, gói trong bốn câu: 
 "Chậm thì chia vai không sửa được — nó chậm thêm gấp đôi. Trước hết đo xem context đang dùng 
 bao nhiêu phần trăm cửa sổ và trong các câu sai thì bao nhiêu là do retrieval; nếu là retrieval thì 
 đây là bài toán Ngày 8, không phải Ngày 9. Nếu vẫn chia thì chia ba theo năng lực — retrieval, tool, 
 synthesis — vì mỗi cái test độc lập được và supervisor thật sự phải quyết định giữa chúng. Và phải 
 có retry ngay từ đầu, nếu không hệ ba worker sẽ tin cậy 85,7% so với 95% hiện tại."

#### Cho đoạn supervisor node dưới đây, 
 hãy chỉ ra ba vấn đề và viết lại. Gợi ý được cho sẵn, đáp án thì không

```text
def supervisor(state):
    docs = vector_store.search(state["task"], k=10)
    state["retrieval_result"] = docs
    if len(docs) > 0:
        state["status"] = "ok"
    weather = call_weather_api(state["user_context"]["city"])
    state["tool_result"] = weather
    state["trace"] = [f"supervisor xu ly xong {len(docs)} docs"]
    return state
```

Ba gợi ý, mỗi gợi ý chỉ về một dòng cụ thể.

1. Gợi ý 1 — đếm số việc. Đếm xem hàm này làm bao nhiêu việc khác nhau. 
 So với supervisor node đúng ở slide 55, con số nên là bao nhiêu? Anti-pattern nào 
 ở slide 28 có tên cho đúng tình trạng này?
2. Gợi ý 2 — nhìn dòng state["trace"] = [...]. 
 Slide 78 nói trace phải luôn append. Nếu supervisor chạy hai lần trong một luồng 
 (mà nó sẽ chạy, vì nó route nhiều lần), điều gì xảy ra với entry của lượt đầu? Và điều đó ảnh hưởng 
 thế nào tới khả năng bạn debug ca Mini-Quest 3?
3. Gợi ý 3 — nhìn state["status"] = "ok" và điều kiện của nó. 
 Điều kiện là len(docs) > 0. Có đủ không? Nếu 10 chunk trả về đều có điểm dưới 0,2 thì 
 sao? Và nếu len(docs) == 0 thì status nhận giá trị gì — hãy tra trong đoạn 
 code, đừng đoán.
4. Gợi ý 4 — thứ không nằm trong ba gợi ý trên. 
 state["user_context"]["city"] giả định trường city luôn tồn tại. Theo 
 slide 48, một agent không nên tin dữ liệu vào mà không kiểm. Đây là một 
 KeyError đang chờ, và nó sẽ làm sập toàn bộ graph chứ không chỉ một worker — vì nó nằm 
 trong supervisor.
5. Khi viết lại, tự chấm bằng ba câu hỏi: ① supervisor của tôi có gọi tool hay 
 search nào không (phải là không )? ② mọi lần ghi state có tạo dict mới không? ③ trace của 
 tôi có phân biệt được "tìm thấy nhưng điểm thấp" với "không tìm thấy" không?

#### Lấy artifact Ngày 8 của chính bạn. Tách thành 
 supervisor + 2–3 worker, viết state schema có ownership rõ, một MCP capability, và 
 một ca worker fail gracefully

Không có đáp án — nhưng có bảng tự chấm, ánh xạ thẳng vào rubric slide 81.

giới hạn nào trong bốn

test độc lập được

supervisor có thật sự phải 
 quyết định về phần này không?

không gọi tool và không search

{**state,...}

không sửa state 
 tại chỗ

đúng một chủ

status

7 trường

result_count

top_score

status: warn

ok

expected_output

cho phép giá trị "không đủ evidence"

ít nhất một

so sánh với 
 agent đơn Ngày 8

bằng số

slide 72

---

<!-- chiron-source-span: {"source_span_id":"2f213513-ec1f-5660-a0a4-6af35b1e91d2","locator":{"kind":"html_section","section_id":"misc","order":16,"heading":"✕ 6 hiểu lầm phổ biến","source_file":"slide-day09.html"},"checksum":"9ef4fe2c93d2099d8164019e6fe5aea28378f4bcdfe76d756489e1001ff358a3"} -->

## ✕ 6 hiểu lầm phổ biến

Mỗi ô: điều nhiều người tin → điều slide (hoặc phép tính) thật sự nói → vì sao khác 
 biệt quan trọng. Năm trong sáu lấy từ [bảng slide 73](#s70); hai trong số đó được tài liệu này 
 bổ sung con số, và hai ô cuối là hiểu lầm mà chỉ phép tính mới lộ ra.

"Nhiều agent = hệ thống tốt hơn. Nếu một agent giỏi thì ba agent giỏi hơn."

"nhiều agent = nhiều phức tạp, chỉ nên dùng khi cần."

×1,24

×2,2

5 điểm fail thay vì 1

85,7%

Slide 14

"nếu single-agent làm được thì đừng chia."

bước 1 của Lab

"Supervisor phải là model lớn nhất — nó ra quyết định quan trọng nhất trong hệ."

"supervisor chỉ cần đủ để route đúng."

Mô-đun 2

8,6% chi phí

2,2 giây độ trễ

code slide 54

route_to_worker

thậm chí không gọi LLM

cần

God Supervisor

độ trễ

"MCP và A2A là cùng một thứ — đều là chuẩn để agent nói chuyện với thứ bên ngoài."

"MCP: tool integration; A2A: agent delegation."

slide 43

"tool không có agency — chỉ thực thi"

hiểu sai

phải kiểm cả nội dung

slide 48

"validate đầu ra trước khi dùng"

"Multi-agent tự động giải quyết vấn đề context — chia ra thì mỗi agent nhẹ gánh, khỏi lo cửa sổ 
 nữa."

"context vẫn phải được quản lý cẩn thận ở từng worker."

Mô-đun 1

72.000 token

62,5%

system prompt không chia được

rút gọn system prompt

"Chia việc ra nhiều agent làm hệ tin cậy hơn — nếu một cái hỏng thì còn những cái kia."

Ngược lại, trừ khi bạn cài đặt đúng cái "còn những cái kia" đó.

Mô-đun 3

85,74%

95,00%

kém hơn 9,26 điểm

"No Fallback"

chỗ

blueprint nộp

"Multi-agent tốn gấp mấy lần tiền — 5 LLM call thay vì 1 thì hoá đơn gấp 5."

Mô-đun 2

×1,24

token

call

một phần

bi quan

Lý do thật để dè dặt là độ trễ (×2,2) và độ tin cậy (−9,3 điểm nếu không retry), không 
 phải tiền.

---

<!-- chiron-source-span: {"source_span_id":"2924eae9-5ebb-5c63-9d8b-3bec46ab6230","locator":{"kind":"html_section","section_id":"apply","order":17,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-day09.html"},"checksum":"5592250aa46480d3215c7aaf11e34eb1d048a04f9060fa46a3c42765d2431791"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI là agent check-in tại kiosk khách sạn, dựng trên LangGraph. Ngày 8 đã 
 cho nó một luồng RAG. Ngày 9 hỏi: *có nên tách nó thành multi-agent không?* Chạy đủ quy trình của 
 bài, và câu trả lời là **"chỉ tách một chỗ, không tách ba"** — vì phép tính nói vậy.

từ lãi mỏng chuyển sang lỗ

chia vai khi nào và vì sao

### ① Bốn giới hạn — đo chứ không đoán

Trước khi chia, [chương 01](#s10) yêu cầu chỉ ra *giới hạn nào* đang bị chạm. Với 
 SmartCheck, bốn giới hạn cho bốn câu trả lời rất khác nhau:

| Giới hạn | SmartCheck có chạm không | Bằng chứng |
| --- | --- | --- |
| Cửa sổ context | Không | System prompt 2.400 token + policy chunk ~2.800 + lịch sử hội thoại ~800 = 6.000 
 token, trên cửa sổ 128.000. Dùng 4,7%. Theo 
 Mô-đun 1, chia vai vì context ở đây là vô nghĩa |
| Một prompt ôm quá nhiều nhiệm vụ | Có — một phần | System prompt hiện tại chứa 6 nhiệm vụ: xác minh giấy tờ, tra PMS, giải thích chính sách, xử lý 
 phòng nâng cấp, tính phụ phí, và quyết định khi nào gọi lễ tân |
| Chuyên biệt hoá | Có — ở đúng một chỗ | Nhiệm vụ "xác minh giấy tờ" cần gọi API bên ngoài và có luật rất khác phần còn lại |
| Khả năng quan sát | Có | Hiện chỉ log câu hỏi và câu trả lời. Khi khách phàn nàn, không biết agent đã tra PMS hay bịa |

**Đọc bảng này:** hai giới hạn thật sự bị chạm là *prompt ôm quá nhiều* và *không quan sát được*. Giới hạn thứ hai **không cần multi-agent để sửa** — nó cần 
 trace, và trace thêm được vào agent đơn. Nghĩa là chỉ có **một** lý do thật để chia vai.

### ② Quyết định: hai worker, không phải ba

Áp hai phép thử của [slide 77](#s76) lên ba cách tách khả dĩ:

| Ứng viên worker | Test độc lập được? | Supervisor có phải quyết định? | Kết luận |
| --- | --- | --- | --- |
| Verification worker — xác minh CCCD/hộ chiếu qua API | Có — đầu vào là ảnh giấy tờ, đầu ra là struct, test bằng 50 ảnh mẫu | Có — khách có thể đã check-in online, khi đó bỏ qua bước này | Tách |
| Policy worker — RAG trên chính sách khách sạn | Có — đây chính là artifact Ngày 8 | Có — phần lớn lượt check-in không hỏi chính sách nào cả | Tách |
| Synthesis worker — sinh câu trả lời cuối | Có | Không — nó luôn chạy, và luôn chạy cuối cùng | Đừng tách — để nó là node cuối của graph, không phải worker được route |

Đây là điểm dễ bị làm sai nhất trong Lab: [slide 77](#s76) gợi ý ba worker gồm cả 
 synthesis. Nhưng gợi ý đó dành cho một agent RAG tổng quát. Với SmartCheck, synthesis luôn chạy và 
 supervisor không bao giờ phải *quyết định* có gọi nó hay không — nên theo chính phép thử thứ hai 
 của slide 77, **tách nó ra là dư thừa**. Nó vẫn là một node trong graph, chỉ không phải một 
 nhánh của conditional edge.

### ③ State schema — và trường nào không có chủ

```text
class SmartCheckState(TypedDict):
    guest_input:     str            # supervisor ghi (tu input kiosk)
    booking_ref:     Optional[str]  # supervisor ghi
    id_result:       Optional[dict] # verification_worker ghi  ← chu duy nhat
    policy_result:   list[dict]     # policy_worker ghi        ← chu duy nhat
    room_assigned:   Optional[str]  # synthesis ghi
    needs_human:     bool           # supervisor ghi
    final_answer:    str            # synthesis ghi
    trace:           list[dict]     # MOI node append          ← an toan vi append-only
    status_log:      list[str]      # MOI node append          ← doi tu "status: str"
```

status

status_log

slide 78

status: str

nhiều node ghi và không append-only

status="warn"

status="ok"

chính xác

Mini-Quest 3

Sửa:

list[str]

### ④ Human-in-the-loop — hai hành động không đảo ngược

[Slide 56](#s54) liệt kê năm điều kiện chèn human review, và điều kiện thứ ba là điều kiện 
 tuyệt đối: *"tool action có side effect không đảo ngược"*. SmartCheck có đúng hai:

| Hành động | Đảo ngược được? | Xử lý |
| --- | --- | --- |
| Trả lời câu hỏi về chính sách | Có — khách hỏi lại | Tự động |
| Tra PMS lấy thông tin đặt phòng | Có — chỉ đọc | Tự động |
| Gợi ý phòng nâng cấp | Có — khách từ chối được | Tự động |
| Kích hoạt thẻ phòng | Không — thẻ đã mở được cửa | Human review, hoặc chỉ khi 
 id_result.confidence ≥ ngưỡng |
| Trừ tiền cọc trên thẻ tín dụng | Không — hoàn tiền là 
 một quy trình khác | Human review không điều kiện |

Và đây là chỗ [slide 56](#s54) nối với [Mini-Quest 2](#s32): LangGraph giữ được 
 state qua `interrupt()` **chỉ vì** node trả về dict mới thay vì sửa state tại 
 chỗ. Nếu SmartCheck viết node theo kiểu sửa tại chỗ, tính năng human-in-the-loop *không cài đặt được* mà không viết lại mọi node. Một chi tiết phong cách ở chương 06 quyết định 
 một tính năng an toàn ở chương 09.

### ⑤ Cái giá — và đây là chỗ khuyến nghị đảo chiều

Chạy [Mô-đun 2](#m-cost) với tham số SmartCheck (context 6.000 token, output 400 token, 
 giá $3,00/1M input):

| Cấu hình | Chi phí mỗi lượt | Mỗi tháng (2.475 lượt) | Độ trễ |
| --- | --- | --- | --- |
| Agent đơn (hiện tại) | $0,0216 | $53,46 ≈ 1,34 triệu đ | 2,8 s |
| 3 worker (theo gợi ý Lab) | $0,0342 | $84,57 ≈ 2,11 triệu đ | 6,2 s |
| Chênh lệch | +$0,0126 (+314 đ) | +778 nghìn đ/tháng | +3,4 s |

Ngày 6

3.750 đ/lượt

2.400 lượt/tháng

2.475 lượt

3%

281 nghìn đ/tháng

3.436 đ/lượt

2.619 lượt/tháng

Sản lượng thực tế là 2.475. Dự án chuyển từ lãi 281 nghìn đ/tháng sang lỗ khoảng 
 496 nghìn đ/tháng.

Mô-đun 3

85,74%

95,00%

9,26 điểm

229 lượt check-in hỏng thêm mỗi tháng

7,6 lượt mỗi ngày

Ngày 6

không

năng lực giờ cao điểm

### ⑥ Khuyến nghị

① Thêm trace vào agent đơn hiện tại — tuần này.

slide 60

result_count

top_score

status_log

một trong hai giới hạn thật

một

một nửa

③ Cùng lúc với ②, cài retry cho verification worker.

với

đúng

chương 11

Không làm:

trước 
 khi

một

---

<!-- chiron-source-span: {"source_span_id":"72471d87-4e55-5f99-baba-1deeb6bb24bf","locator":{"kind":"html_section","section_id":"numbers","order":18,"heading":"# Con số cần kiểm chứng","source_file":"slide-day09.html"},"checksum":"ec9e294312c779c0762dcfd07f1d8628d06b561a2840f4068003bf87fefc5612"} -->

## # Con số cần kiểm chứng

Ranh giới giữa *số của slide* và *số của tài liệu này* — và ở bài 
 Ngày 9, ranh giới đó cực kỳ rõ.

"2–3 workers"

"5 trường cần 
 thiết"

50'/20'/40'/20'/45'/30'/25'/20'/90'

"30 phút đầu để fix artifact"

"10 kết quả không được lọc"

Mini-Quest 3

latency_ms

slide 66–68

tốn hơn

chậm hơn

nhiều điểm fail hơn

slide 72

"giải thích được trade-off 
 cost/reliability"

Nghĩa là: mọi con số về chi phí, độ trễ và độ tin cậy trong tài liệu này đều đến từ 
 tài liệu này, không đến từ slide.

cấu trúc

con số

| Con số | Nguồn | Cần kiểm gì trước khi dùng |
| --- | --- | --- |
| Cửa sổ 24.000 token · system 3.000 · lịch sử 6.000 · tool 12.000 · còn ≈3.000 | Slide 11 — deck cho bốn số đầu và nói "còn khoảng 3.000" | Cửa sổ 24.000 là suy ra: 3.000+6.000+12.000+3.000. Deck không nói cửa sổ bao nhiêu. 
 Mô-đun 1 tái lập đúng cấu hình này làm mặc định |
| Chia 3 worker → mỗi worker còn 62,5% cửa sổ trống · dung lượng hiệu dụng 
 72.000 token · agent đơn còn 1 lượt hội thoại | Tính ra từ số slide 11 | Giả định: system prompt không chia được (lặp ở mọi worker), lịch sử và tool result chia 
 đều cho N. "1 lượt" giả định mỗi lượt thêm 2.000 token. Trong hệ thật, chia không bao giờ đều |
| 20.000 token vào · 800 ra · $3,00/1M · 3 worker · 2,8 s mỗi call | Giả định của tài liệu này cho ví dụ tổng quát. Không có trong slide | Tham số minh hoạ. Dùng số của hệ bạn. Giá output lấy bằng 3× giá input — đúng với nhiều 
 model nhưng không phải mọi model |
| Chi phí ×1,24 · độ trễ ×2,2 (song song) và 
 ×4,2 (nối tiếp) · hạ cấp supervisor tiết kiệm 8,6% · 
 cơ cấu 86,0% worker / 13,0% synthesis / 1,0% supervisor | Tính ra từ các giả định trên | Rất nhạy với mức chia context. Mô hình giả định mỗi worker nhận in/N + 500 
 token. Nếu worker của bạn thật ra nhận gần trọn context (điều rất hay xảy ra), tỷ số tiến về ×N — 
 hãy đo bằng cách in ra độ dài prompt thật của từng worker |
| 3 worker · p = 5% · không retry → 85,74% so với single 
 95,00% · 1 retry → 99,25% · chịu 1 hỏng → 99,28% | Tính ra — nhị thức, các worker độc lập | Ba giả định, và giả định thứ hai là giả định lạc quan: ① fail độc lập (thực tế có tương quan — 
 chung model, chung endpoint); ② retry độc lập với lần trước — sai nếu nguyên nhân 
 fail là tất định, khi đó p² thật ra là p; ③ p giống nhau ở mọi worker. Con số 99,25% là 
 trần trên, không phải kỳ vọng |
| p = 5% mỗi worker | Giả định | Đây là con số bạn phải tự đo, và đo được chỉ khi đã có trace với 
 result_count / status đúng. Worker gọi tool ngoài thường có p cao hơn hẳn 
 worker chỉ đọc state — đừng dùng một con số chung |
| SmartCheck: 6.000 token context · 400 token output · 2.475 lượt/tháng · biên gộp 3.750 đ/lượt · 
 hoà vốn 2.400 lượt | Bốn số cuối từ mô hình Ngày 6; hai số đầu là giả 
 định của mục này | Số Ngày 6 vốn đã là mô hình có giả định (trần adoption 55% là đoán ). Mọi kết luận ở mục 
 ⑤ thừa hưởng độ bất định đó |
| Tách 3 worker → +314 đ/lượt · +778 nghìn đ/tháng · hoà vốn dời lên 2.619 
 lượt · lỗ ≈496 nghìn đ/tháng · thêm 229 lượt hỏng/tháng | Tính ra, quy đổi 25.000 đ/USD | Kết luận "chuyển sang lỗ" đúng với biên an toàn 3% của Ngày 6. Nếu sản lượng thật cao 
 hơn 2.619 lượt/tháng thì kết luận đảo chiều — nên hãy kiểm sản lượng thật trước khi trích câu này |
| Trace Mini-Quest 3: latency 240 · 890 · 180 · 5.100 ms | Slide 63 — số gốc của deck | Nhận xét "5.100 ms là dấu vân tay của hallucination" là diễn giải của tài liệu này, 
 deck không nói. Nó hợp lý nhưng không phải kết luận đã được deck xác nhận |

① Prompt thật của mỗi worker dài bao nhiêu token.

print(formatted_context)

Ngày 8

không

② p thật của từng bước.

không dùng được

slide 64

③ Độ trễ thật của mỗi LLM call trong hệ bạn

---

<!-- chiron-source-span: {"source_span_id":"0123df0b-529c-5b80-9451-bc2a5ba6beb6","locator":{"kind":"html_section","section_id":"cheat","order":19,"heading":"▣ Cheat sheet ôn thi","source_file":"slide-day09.html"},"checksum":"5fa5d23c813fa9135532ba2f2f2488abe072ebffeffdf56cde5641f7218bec33"} -->

## ▣ Cheat sheet ôn thi

Những thứ nên nhớ được mà không cần mở lại tài liệu.

| Danh sách | Các mục | Slide |
| --- | --- | --- |
| Bốn giới hạn của single-agent | Cửa sổ context · một prompt ôm quá nhiều nhiệm vụ · thiếu chuyên biệt hoá · 
 không quan sát được | 10–13 (+ Hình 1 ) |
| Ba câu hỏi thiết kế | Chia trách nhiệm ở đâu · thông tin đi theo con đường nào · 
 lỗi ở đâu là ít tổn hại nhất | 15 |
| Bốn pattern | Supervisor-worker · Pipeline · Debate/Critic · Blackboard | 20–23 |
| Bốn anti-pattern | God Supervisor · Chatty Workers · Shared State không chủ · No Fallback | 28 (+ Mô-đun 3 ) |
| Ba khái niệm LangGraph | node = ai làm · edge = đi đâu tiếp · state = hệ đang biết gì | 52 |
| Message contract 3 phần | Task · Context · Expected output | 45 |
| Trace entry 7 trường | timestamp · agent_id · action · input_summary · output_summary · status · latency_ms | 60 (+ Hình 3 ) |
| Bốn cơ chế chịu lỗi | Timeout · Retry · Fallback · Partial failure | 68 |
| Trust boundary 4 câu hỏi | Ai gọi ai · dữ liệu nào truyền đi · output nào cần xác thực · validate trước khi dùng | 48 |

"MCP trả lời câu hỏi agent lấy năng lực ở đâu, còn A2A trả lời câu hỏi agent giao việc cho ai."

"Nguyên tắc 'need to know': worker chỉ nhận context mà nó thực sự cần. Không thêm, không bớt."

"Đừng giả định mọi agent đều đáng tin như nhau. Hệ nhiều agent vẫn cần trust boundary."

"node = ai làm · edge = đi đâu tiếp · state = hệ đang biết gì."

"status: ok chỉ có nghĩa là 'bước này không văng exception'. Nó không có nghĩa là 
 kết quả dùng được."

"Multi-agent không miễn phí. Nó đổi token và latency lấy khả năng chia bài toán và kiểm soát 
 context."

| Câu hỏi | Con số | Nguồn |
| --- | --- | --- |
| Multi-agent tốn hơn bao nhiêu? | ×1,24 — không phải ×N | Mô-đun 2 |
| Chậm hơn bao nhiêu? | ×2,2 song song · ×4,2 nối tiếp | Mô-đun 2 |
| Hạ cấp supervisor tiết kiệm bao nhiêu? | 8,6% tiền, nhưng 26% độ trễ | Mô-đun 2 |
| 3 worker, p = 5%, không retry — hệ tin cậy bao nhiêu? | 85,74% — kém hơn agent đơn 95,00% | Mô-đun 3 |
| Thêm 1 retry thì sao? | 99,25% | Mô-đun 3 |
| Chia 3 worker được thêm bao nhiêu context? | Dung lượng hiệu dụng ×3, nhưng system prompt không chia được | Mô-đun 1 |
| Cơ cấu chi phí multi-agent? | Worker 86,0% · synthesis 13,0% · supervisor 1,0% | Mô-đun 2 |

① "LangGraph chỉ dùng được với LangChain."

slide 73

② "Supervisor node gọi LLM để route."

ra quyết định

need_tool

need_retrieval

route_to_worker

Python thuần, không LLM

slide 54

③ "Trace là để debug."

slide 82

dữ liệu để cải thiện hệ thống lâu dài

---

<!-- chiron-source-span: {"source_span_id":"f6516866-2007-514a-bef8-46dcb2a81520","locator":{"kind":"html_section","section_id":"gloss","order":20,"heading":"☰ Từ điển thuật ngữ","source_file":"slide-day09.html"},"checksum":"9a248f276c9dae82e6ad4231dd25dd03559e48033823325340e0e8cee7e224d9"} -->

## ☰ Từ điển thuật ngữ

Định nghĩa theo cách dùng được trong bài thi và trong công việc, không phải theo cách 
 tra từ điển.

---

<!-- chiron-source-span: {"source_span_id":"c97f38fc-6f73-5a0e-82dd-0801c7c258b0","locator":{"kind":"html_section","section_id":"bloom","order":21,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-day09.html"},"checksum":"58ce56a818c551be28dcd3a67d1dc1b1a36dea78cc7fc0e239e50f7e095fe356"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Ba cấp độ của [slide 72](#s70) phủ 
 mức 1–4; rubric Lab 9 chấm mức 3–5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 4 giới hạn single-agent, 3 câu hỏi thiết kế, 4 pattern, 4 anti-pattern, 3 khái niệm 
 LangGraph, 3 phần contract, 7 trường trace, 4 cơ chế chịu lỗi. | Cheat sheet · Hình 1 · Hình 2 |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao MCP và A2A khác nhau ở chỗ bên kia có agency hay 
 không chứ không ở giao thức; và vì sao status: ok không có nghĩa là kết quả 
 dùng được. | Slide 43 · Mini-Quest 3 · 
 hiểu lầm 3 |
| 3 · Áp dụng | Tách được artifact Ngày 8 thành supervisor + 2–3 worker có state schema với ownership rõ, viết 
 được message contract đủ ba phần, và cài được một MCP capability. | Slide 76–79 · Bài 1 · chương 05 |
| 4 · Phân tích | Cho một trace, chỉ ra được dòng nào là gốc chứ không phải dòng nào lộ triệu chứng — và 
 nói được cần thêm trường gì để lần sau nó tự hiện lên. | Mini-Quest 3 · Hình 3 · Bài 2 |
| 5 · Đánh giá | Nhìn một đề xuất chia vai và nói được nó có đáng làm không — bằng số: 
 chi phí gấp mấy lần, độ trễ gấp mấy lần, độ tin cậy tăng hay giảm mấy điểm. Kể cả khi câu 
 trả lời là "đừng chia". | Mô-đun 2 · Mô-đun 3 · 
 hiểu lầm 5 |
| 6 · Sáng tạo | Nhận ra rằng lợi ích độ tin cậy của multi-agent không nằm ở việc chia vai mà ở chỗ chia 
 vai tạo ra vị trí để đặt retry và fallback — rồi thiết kế hệ dựa trên nhận định đó thay vì 
 dựa trên sơ đồ đẹp. | Chương 11 · mục SmartCheck ⑤–⑥ |

①

số đo

②

test độc lập

③

chạy thử

Mô-đun 3

kém hơn
