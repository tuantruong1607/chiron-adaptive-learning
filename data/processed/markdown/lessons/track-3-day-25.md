---
schema_version: 1
course_id: rag-intensive
document_id: "01f21759-462e-5b60-bc95-8d72023ac9a7"
document_version_id: "36fa91fc-caf3-5fef-a040-339916ecd7c3"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Circuit Breakers, Caching & Reliability — phân tích & breakdown từng slide"
source_file: "track-3-day-25.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-25.html"
source_sha256: "4188d8b2b12335f3d8b822c465539d87cb18795aa9ff86d7d42e416bd2e39e9b"
parser_version: chiron-structured-markdown-v1
html_section_count: 15
interactive_module_count: 3
interactive_control_count: 13
language: vi
---

# Circuit Breakers, Caching & Reliability — phân tích & breakdown từng slide

> 34 slide, bài ngắn nhất Track 3 nhưng là bài áp dụng được ngay nhiều 
 nhất. Ngày 24 dạy cách phát hiện vấn đề; bài này dạy cách hệ thống sống sót khi vấn 
 đề xảy ra — và cách chứng minh nó sống sót bằng số.

<!-- chiron-source-span: {"source_span_id":"f3c55b36-a9f8-526f-b3d9-005d0dfa73f5","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"track-3-day-25.html"},"checksum":"7724c0ce3c207193e214880f7fa081765c963cd6b02a38cc2104993b991daa6f"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Bài này **ít slide nhất Track 3** (34 trang, so với 74 của Ngày 24) nhưng đừng nhầm 
 ngắn với dễ. Mật độ khái niệm rất cao: mỗi slide gần như đưa đúng một danh sách phải nhớ — 6 loại lỗi, 
 3 trạng thái, 4 bậc fallback, 3 tầng cache, 3 lớp kiểm soát chi phí, 4 khái niệm SLI/SLO/SLA/error 
 budget.

Điểm khác biệt so với các bài trước: **hầu hết nội dung ở đây tính ra được bằng số**. 
 Circuit breaker cứu được bao nhiêu lời gọi, cache tiết kiệm bao nhiêu tiền và đổi lại bao nhiêu câu 
 trả lời sai, SLO 99% nghĩa là được phép sập bao nhiêu phút mỗi tháng — cả ba đều là số học thuần tuý. 
 Ba mô-đun tương tác trong tài liệu tồn tại để bạn tự tính, chứ không phải để minh hoạ.

Lượt 1 · ~10 phút

Nắm mạch chính

- Đọc slide 8 (6 loại lỗi), 12 (3 trạng thái), 
 14 (fallback ladder), 22 (SLI/SLO/SLA)
- Nhìn Hình 2 — máy trạng thái circuit breaker, hình phải vẽ được từ trí nhớ
- Mục tiêu: nói được vì sao retry một mình làm lỗi nhỏ thành sự cố lớn

Lượt 2 · ~50 phút

Ba mô-đun và chương 2–4

- Làm hết phần "Dự đoán trước khi kéo" ở 3 mô-đun — đây là phần đắt giá nhất
- Chương 5 (lab) đọc lướt, trừ slide 28 — danh sách metric bắt buộc
- 3 bài tập bậc thang theo thứ tự

Lượt 3 · ~15 phút

Trước quiz

- 6 hiểu lầm — bài này có hai bẫy rất dễ mắc về cache và về retry
- Cheat sheet — sáu danh sách và một bảng số
- Từ điển — SLI, SLO, SLA, error budget, half-open, false-hit

Ngày 24

"Khi LLM provider timeout trong production, agent của bạn sẽ tự phục hồi hay làm sập cả 
 workflow?"

hệ thống của chính bạn

mục áp dụng

"AICB · Day 10 · Week 5"

Lab #10

track 3 — day 25.pdf

10 là số thứ tự trong Track 3

---

<!-- chiron-source-span: {"source_span_id":"30cf47d9-8745-5a63-b1ef-a8e9e9598f5b","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"track-3-day-25.html"},"checksum":"dd396ffef6609a48d786669eb3d55ffbc61a21314799540f2019c4427bf728cb"} -->

## 00 Mở đầu

Slide 1–6: câu hỏi dẫn dắt, mục tiêu chia hai nhóm, và timeline 2 giờ.

### Slide 1–3 Trang bìa, câu hỏi dẫn dắt và nội dung

> Trích slide 
>  "Circuit Breakers, Caching & Reliability for Production Agents — AICB-P2T3 · Day 10 · 
>  Agent Production-Ready" 
>  "Khi LLM provider timeout trong production, agent của bạn sẽ tự phục hồi hay làm sập cả 
>  workflow?" 
>  "1. Mục tiêu & timeline 2 giờ 2. Failure Modes 3. Circuit Breaker & Fallback 
>  4. Caching & Cost Budgeting 5. Observability & SLO 6. Lab: Reliability Engineering 
>  7. Tổng kết"

Câu hỏi dẫn dắt được viết rất chính xác, và cách nó chọn từ đáng để ý. 
 Nó **không** hỏi "làm sao để provider không timeout" — đó là câu hỏi sai, vì bạn không 
 kiểm soát được provider. Nó hỏi *khi* timeout xảy ra thì chuyện gì diễn ra tiếp theo.

Phần lớn kỹ năng học từ Ngày 16 đến Ngày 24 là làm cho agent *tốt hơn*: kiến trúc tốt hơn, 
 truy xuất tốt hơn, alignment tốt hơn, đo lường tốt hơn. Bài này giả định **mọi thứ vẫn sẽ hỏng** và hỏi: hỏng thì hỏng như thế nào?

Trong kỹ thuật hệ thống có một cách nói gọn: bạn không thiết kế để *không* hỏng, bạn thiết 
 kế để **hỏng một cách có kiểm soát**. Toàn bộ từ vựng của bài — circuit breaker, 
 fallback ladder, graceful degradation, error budget — đều là biến thể của ý đó.

Nó cũng giải thích vì sao [danh mục tài liệu](#s33) dẫn *Release It!* của Michael Nygard, một cuốn sách viết năm 2007 — trước LLM cả thập kỷ. 
 Các mẫu ổn định không mới; cái mới chỉ là chúng chưa được áp cho lời gọi model.

### Slide 4–5 Mục tiêu — hai nhóm kết quả

> Trích slide 
>  " Conceptual outcomes ■ Nhận diện 6 nhóm lỗi production của LLM agent. 
>  ■ Giải thích 3 trạng thái circuit breaker. ■ Phân biệt exact cache, semantic cache, tool-result 
>  cache. ■ Thiết kế SLI/SLO/SLA cho agent." 
>  " Practical outcomes ■ Xây gateway có fallback chain. ■ Log latency/cost/cache 
>  hit/circuit state. ■ Chạy chaos test và load test nhỏ. ■ Viết report có metric để chấm điểm." 
>  "Trong lớp: hoàn thành baseline reliability harness. Bài lab mở rộng 4 giờ giúp phân loại nhóm 
>  hoàn thành sớm và nhóm đào sâu."

Bốn mục *conceptual* chính là bốn danh sách phải thuộc, và chúng ánh xạ một-một vào bốn 
 chương nội dung. Đây là bản đồ đề thi rõ ràng nhất trong cả Track 3:

| Mục tiêu | Con số phải nhớ | Học ở chương |
| --- | --- | --- |
| Nhận diện nhóm lỗi | 6 loại | 01 — slide 8 |
| Giải thích circuit breaker | 3 trạng thái | 02 — slide 12 |
| Phân biệt cache | 3 tầng | 03 — slide 17 |
| Thiết kế SLI/SLO/SLA | 4 khái niệm (kèm error budget) | 04 — slide 22 |

Xây

Log

Chạy

Viết

slide 28

"Report không có metric định lượng = không đạt phần 
 grading."

### Slide 6 Timeline 2 giờ trên lớp

> Trích slide 
>  "Lý thuyết có tương tác: ■ 20' reliability failure map ■ 25' circuit breaker + fallback 
>  ■ 25' caching + cost budget ■ 25' metrics + chaos thinking" 
>  "Lab kickoff trong lớp: ■ 10' repo walkthrough ■ 15' team planning + first run ■ Sau lớp: hoàn 
>  thiện 4h lab/report"

Phân bổ thời gian cho biết trọng số thật: ba khối chính (circuit breaker, cache, metrics) mỗi khối 
 25 phút, đều nhau. Nếu bạn đang phân bổ thời gian ôn, hãy chia đều cho ba chương đó và dành ít hơn cho 
 chương failure modes — nó là phần dẫn nhập, không phải phần bị hỏi sâu.

Slide 27

"Core pass khoảng 2 giờ cho nhóm mạnh. Stretch 2 giờ còn 
 lại"

hai giờ đầu là phần bắt buộc để qua, hai giờ sau là phần lấy điểm cao

slide 29

---

<!-- chiron-source-span: {"source_span_id":"d4eec43d-f144-503a-992f-9595e4b57366","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Failure modes","source_file":"track-3-day-25.html"},"checksum":"37b6775819957942494ae0e0f86d9f817294da67f53abf26bfcf44fc5220f78e"} -->

## 01 Failure modes

Slide 7–10: sáu loại lỗi, cơ chế lan truyền của retry, và loại lỗi không tạo ra lỗi nào.

### Slide 7–8 Sáu nhóm lỗi và nơi chúng xuất hiện

> Trích slide 
>  "Reliability bắt đầu từ việc gọi đúng tên lỗi: transient, outage, degraded, stale, costly, unsafe." 
>  "Lỗi có thể xuất hiện ở provider, gateway, cache, tool, hoặc business action. 
>  Reliability là system property, không phải chỉ là thêm retry. " 
>  "6 loại lỗi cần monitor: 1. Provider transient: 429/500/timeout. 
>  2. Degraded latency: P95 tăng mạnh. 3. Full outage: provider không 
>  phản hồi. 4. Orchestration loop: state/retry sai. 5. Tool/cache failure: 
>  stale/schema/auth. 6. Business action sai: side effect không rollback."

Câu *"Reliability là system property"* là luận điểm trung tâm. Ý nghĩa cụ thể của nó: **không có bộ phận nào trong hệ thống chịu trách nhiệm về độ tin cậy**. Bạn không thể 
 thêm một thư viện, một decorator, hay một lớp bọc rồi tuyên bố đã xong — vì sáu loại lỗi nằm ở sáu 
 chỗ khác nhau và cần sáu cơ chế khác nhau.

_Sơ đồ: Đường đi của một request và sáu nhóm lỗi xuất hiện ở đâu - Phần trên vẽ đường đi: request của người dùng tới LLM Gateway; gateway gọi Provider A hoặc Provider B, và gọi các Cache hoặc Tool API, từ đó dẫn tới hành động nghiệp vụ. Phần dưới liệt kê sáu nhóm lỗi và vị trí của chúng: ba nhóm đầu là provider transient, degraded latency và full outage đều nằm ở provider; nhóm bốn là orchestration loop nằm ở gateway; nhóm năm là tool hoặc cache failure; nhóm sáu là business action sai không rollback được._

Hình 1 — Bản đồ lỗi (slide 8).

không

**Nhóm 1–3 ở phía provider.** Bạn không sửa được nguyên nhân; bạn chỉ *chứa* hậu quả. Vũ khí: timeout, circuit breaker, fallback chain. Cả chương 2 của bài dành 
 cho ba nhóm này.

**Nhóm 4–6 ở phía bạn.** Đây là bug trong code của chính bạn, và chúng sửa được — 
 nhưng thường bị bỏ qua vì chúng ít ồn ào hơn.

**Nhóm 4 là nhóm bạn đã học cách chữa rồi.** "Orchestration 
 loop: state/retry sai" chính là thứ mà Ngày 23 gọi là *retry hữu hạn* và *dead-letter* — bounded retry với bộ đếm trong state, và một nhánh thoát an toàn khi hết 
 lượt. Nếu bài lab LangGraph của bạn đã có `retry_count` và nhánh dead-letter, bạn đã 
 xử lý xong nhóm 4.

transient, outage, degraded, stale, costly, unsafe

costly

unsafe

costly

slide 19

unsafe

Ngày 24

### Slide 9 Cascading failure — khi retry biến lỗi nhỏ thành sự cố lớn

> Trích slide 
>  "Provider timeout → Client retry 3 lần → Quota/rate limit cạn → Workflow outage" 
>  "Think-pair-share: 5 phút — Hãy chọn một sản phẩm agent bạn biết. Nếu provider chính bị 
>  timeout 30 giây, người dùng sẽ thấy gì? Nhóm đề xuất một cách contain, isolate, recover." 
>  " Retry chỉ là bước đầu. Nếu không có circuit breaker + fallback + budget, 
>  retry có thể biến lỗi nhỏ thành outage lớn."

Chuỗi bốn bước này là **lập luận quan trọng nhất của cả bài**, vì nó cho thấy một cơ 
 chế phòng thủ hợp lý lại trở thành nguyên nhân gây sự cố. Cần đọc chậm để thấy chỗ nghịch lý:

```text
Provider chậm đi một chút          (lỗi nhỏ, tự khỏi được)
        │
        ▼
Mỗi request retry 3 lần            tải gửi tới provider ×3
        │
        ▼
Provider đang yếu, nay nhận ×3     chậm thêm  →  nhiều timeout hơn
        │                                              │
        │         ┌────────────────────────────────────┘
        │         ▼
        │   nhiều timeout hơn  →  nhiều retry hơn  →  vòng lặp khuếch đại
        ▼
Quota / rate limit cạn             giờ thì CẢ request lành cũng bị chặn
        │
        ▼
Workflow outage                    (sự cố lớn, không tự khỏi)
```

Provider chậm ⇒ nhiều timeout ⇒ nhiều retry ⇒ tải cao hơn ⇒ provider chậm hơn nữa. Vòng lặp tự 
 nuôi mình, và nó **mạnh nhất đúng lúc hệ thống yếu nhất**.

Đây là lý do tại sao "cứ retry đi" là lời khuyên nguy hiểm. Retry giả định lỗi là *độc lập và ngẫu nhiên* — retry lần hai có cơ hội tốt hơn vì lần một chỉ xui. Giả định đó 
 đúng với lỗi mạng thoáng qua, và **sai hoàn toàn** khi nguyên nhân là provider quá tải: 
 lúc đó retry không phải "thử lại" mà là "đổ thêm dầu".

**Circuit breaker chính là thứ cắt vòng lặp này.** Nó phát 
 hiện "lỗi đang có hệ thống, không phải ngẫu nhiên" và ngừng gửi — biến vòng phản hồi dương thành 
 một cái công tắc.

**Ba động từ trong bài tập nhóm — *contain, isolate, recover* — chính là dàn ý của ba 
 chương tiếp theo**, và đáng dùng làm khung trả lời cho mọi câu hỏi vấn đáp về reliability:

| Động từ | Nghĩa là gì | Cơ chế trong bài |
| --- | --- | --- |
| Contain | Không để lỗi lan rộng hơn phạm vi của nó | Circuit breaker, timeout, rate limit, cost cap |
| Isolate | Giữ các phần khoẻ mạnh không bị kéo theo | Breaker riêng cho từng provider ( slide 12 ) |
| Recover | Tự trở lại bình thường khi nguyên nhân hết | Trạng thái HALF-OPEN, reset timeout |

"hệ thống sẽ làm gì"

"người dùng sẽ thấy gì"

90 giây

fail nhanh thường là trải nghiệm tốt hơn fail chậm

### Slide 10 Silent degradation — lỗi không tạo ra lỗi nào — slide nối thẳng với Ngày 24

> Trích slide 
>  "error rate = 0% · faithfulness giảm dần" 
>  "Nguyên nhân thường gặp: ■ Provider cập nhật model silently. ■ Prompt/schema thay đổi nhưng eval 
>  không đổi. ■ Knowledge base stale hoặc retrieval yếu. ■ Cache trả câu đúng cũ nhưng sai hiện tại." 
>  " Quality SLO phải đi cùng uptime SLO. Error rate = 0% không đủ. "

Slide này là chỗ Ngày 25 và Ngày 24 gặp nhau, và nó nói một điều mà mọi bảng điều khiển vận hành 
 truyền thống đều bỏ sót: **với hệ thống LLM, "không có lỗi" không đồng nghĩa với "đang chạy 
 tốt"**.

Một API thông thường hoặc trả đúng dữ liệu, hoặc trả lỗi. Không có trạng thái thứ ba.

Một LLM **luôn** trả về một câu trả lời trông hợp lệ. Mọi tín hiệu vận hành — 
 mã trạng thái 200, độ trễ bình thường, không có ngoại lệ — đều xanh, trong khi nội dung câu trả lời 
 đã tệ đi. Đây là trạng thái thứ ba: *thành công về mặt kỹ thuật, thất bại về mặt nội dung*.

Nên câu *"Quality SLO phải đi cùng uptime SLO"* không phải lời 
 khuyên thêm cho đủ — nó là điều kiện cần. Uptime SLO đo *máy có chạy không*; quality SLO đo *câu trả lời có còn đúng không*. Với LLM, hai thứ đó rời nhau hoàn toàn.

Bốn nguyên nhân được liệt kê không cùng loại, và phân biệt chúng quyết định cách bạn phát hiện:

| Nguyên nhân | Ai gây ra | Phát hiện bằng cách nào | Đã học ở đâu |
| --- | --- | --- | --- |
| Provider cập nhật model âm thầm | Bên ngoài — bạn không được báo | Ghim phiên bản model có ngày tháng; chạy golden set định kỳ | Ngày 24 — model drift |
| Prompt/schema đổi mà eval không đổi | Bên trong — đội bạn | Đưa prompt vào quản lý phiên bản; eval chạy trong CI | Ngày 24 — prompt drift |
| Knowledge base cũ hoặc retrieval yếu | Bên trong — dữ liệu | Context Recall trên golden set; theo dõi thời điểm index | Ngày 24 — data drift |
| Cache trả câu đúng cũ nhưng sai hiện tại | Bên trong — do chính bạn thêm vào | TTL, invalidation theo sự kiện, theo dõi false-hit | Slide 18 của bài này |

chỉ xuất hiện sau khi bạn thêm 
 cache vào để tối ưu

slide 16

"cache sai chỗ tạo stale answer và hallucination ổn định"

"ổn định"

lặp lại y hệt

#### Ô kiểm tra — Chương 1

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao "cứ thêm retry là xong" lại là lời khuyên nguy hiểm? Mô tả cơ chế 
 biến một lỗi nhỏ thành sự cố lớn. Hiểu

#### Đáp án

**Vì retry là một vòng phản hồi dương, và nó mạnh nhất đúng lúc hệ thống yếu nhất.**

Chuỗi bốn bước ở slide 9: provider timeout → client retry 3 lần → quota/rate limit cạn → 
 workflow outage. Cơ chế: provider chậm ⇒ nhiều timeout ⇒ nhiều retry ⇒ tải gửi tới provider tăng 
 gấp ba ⇒ provider chậm hơn nữa ⇒ càng nhiều timeout. Vòng lặp tự nuôi mình.

**Giả định sai nằm ở đâu:** retry giả định lỗi là *độc lập và ngẫu nhiên* — 
 lần hai có cơ hội tốt hơn vì lần một chỉ xui. Đúng với lỗi mạng thoáng qua; sai hoàn toàn khi 
 nguyên nhân là provider quá tải, vì khi đó retry không phải "thử lại" mà là "đổ thêm tải".

**Cái cắt vòng lặp:** circuit breaker — nó phát hiện lỗi đang có hệ thống chứ 
 không ngẫu nhiên, rồi ngừng gửi. Slide chốt: "retry chỉ là bước đầu; nếu không có circuit breaker 
 + fallback + budget, retry có thể biến lỗi nhỏ thành outage lớn".

**2.** Dashboard của bạn báo error rate 0%, P95 latency bình thường, không có 
 exception nào trong 30 ngày. Có thể kết luận hệ thống đang chạy tốt 
 không? Phân tích

#### Đáp án

**Không.** Đây đúng là mô tả của *silent degradation* ở slide 10: 
 "error rate = 0%" trong khi faithfulness giảm dần.

**Vì sao hệ LLM có kiểu hỏng này còn hệ thường thì không:** một API bình thường 
 hoặc trả đúng dữ liệu, hoặc trả lỗi. Một LLM *luôn* trả về câu trả lời trông hợp lệ — nên 
 mã 200, độ trễ ổn và không có exception đều là tín hiệu xanh trong khi nội dung đã tệ đi. Đó là 
 trạng thái thứ ba: thành công kỹ thuật, thất bại nội dung.

**Thiếu gì:** quality SLO. Slide chốt "Quality SLO phải đi cùng uptime SLO. 
 Error rate = 0% không đủ". Cụ thể (slide 22): faithfulness, safety pass rate, escalation 
 correctness — đo trên mẫu traffic, đúng cách [Ngày 24](track-3-day-24.html) mô tả.

**Bốn nguyên nhân cần loại trừ:** provider đổi model âm thầm, prompt/schema đổi mà 
 eval không đổi, knowledge base cũ, và cache trả câu đúng-cũ-sai-hiện-tại.

**3.** Trong sáu nhóm lỗi ở slide 8, nhóm nào bạn đã có sẵn cơ chế chữa từ bài 
 lab LangGraph Ngày 23, và cơ chế đó là gì? Áp dụng

#### Đáp án

**Nhóm ④ — Orchestration loop: state/retry sai.** Đây là nhóm nằm trong code của 
 bạn, ở tầng gateway/orchestrator, chứ không ở phía provider.

**Cơ chế đã có từ Ngày 23:** *bounded retry* — một bộ đếm `retry_count` trong state, và một điều kiện định tuyến ngừng thử lại khi vượt ngưỡng; 
 cộng với nhánh *dead-letter* làm lối thoát an toàn khi hết lượt, thay vì lặp vô hạn cho tới 
 khi đụng recursion limit.

**Cũng chấp nhận được nếu nêu ⑥ (business action sai):** Ngày 23 có cổng *approval* đặt **trước** mọi hành động rủi ro, tức là ngăn side effect xảy ra 
 thay vì phải rollback sau. Đây là HITL đúng nghĩa.

**Điều cần nói thêm để đạt điểm cao:** ba nhóm ①②③ nằm ở phía provider — 
 Ngày 23 *không* chạm tới, và đó chính là khoảng trống mà bài hôm nay lấp: timeout, circuit 
 breaker, fallback chain.

---

<!-- chiron-source-span: {"source_span_id":"958170b7-dcbf-502d-98b4-6f558c728f29","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Circuit breaker & fallback","source_file":"track-3-day-25.html"},"checksum":"556b965fcadfa37b33b8e6e876208ba35c09810457cd8677919edbdd3fb579b9"} -->

## 02 Circuit breaker & fallback

Slide 11–15: ba trạng thái, bốn tham số, thang tụt bậc năm nấc và bẫy tương thích tính năng.

### Slide 11–12 Ba trạng thái của circuit breaker

> Trích slide 
>  "Circuit breaker ngắt gọi provider đang hỏng; fallback chain giữ trải nghiệm user ở mức chấp 
>  nhận được." 
>  " CLOSED normal calls — failure threshold → OPEN fail 
>  fast — reset timeout → HALF-OPEN probe call — success → CLOSED / 
>  fail → OPEN" 
>  "Nên có breaker theo từng provider/model/task. Provider A open không nên kéo provider B 
>  hoặc cache layer sập theo. "

Cái tên mượn từ cầu dao điện, và phép ẩn dụ chính xác hơn nhiều người nghĩ: cầu dao không sửa được 
 chỗ chập điện, nó chỉ **ngắt mạch để chỗ chập không đốt cháy cả nhà**. Circuit breaker 
 phần mềm cũng vậy — nó không làm provider khoẻ lại, nó chỉ ngừng gửi request vào một nơi đang hỏng.

_Sơ đồ: Ba trạng thái của circuit breaker và các điều kiện chuyển trạng thái - Ba trạng thái. CLOSED gọi provider bình thường và đếm số lần lỗi; khi số lỗi vượt failure threshold thì chuyển sang OPEN. OPEN không gọi provider nữa mà trả lỗi hoặc fallback ngay lập tức; sau khi hết reset timeout thì chuyển sang HALF-OPEN. HALF-OPEN thả một request thăm dò: nếu thành công đủ số lần thì quay lại CLOSED, nếu thất bại thì quay lại OPEN._

Hình 2 — Máy trạng thái circuit breaker (slide 12).

bốn

Giả sử bỏ HALF-OPEN: hết reset timeout thì về CLOSED luôn. Chuyện gì xảy ra?

Trong lúc breaker OPEN, request vẫn tiếp tục đến. Khi đột ngột về CLOSED, **toàn bộ lưu lượng đổ vào provider cùng một lúc** — và nếu provider chưa thật sự khoẻ, 
 bạn vừa tái tạo đúng cascading failure ở [slide 9](#s9), chỉ khác là lần này do chính 
 breaker gây ra.

HALF-OPEN giải quyết bằng cách **thả một request duy nhất để thăm 
 dò**. Thành công thì mở dần; thất bại thì đóng lại ngay và tiếp tục đợi. Chi phí của phép thử 
 là *một* lời gọi, không phải cả hàng đợi. Đây là ý tưởng cốt lõi và cũng là câu trả lời cho 
 câu hỏi vấn đáp phổ biến nhất về chủ đề này.

Một breaker chung cho cả hệ thống thì *chính nó* trở thành điểm hỏng đơn: Provider A gặp 
 sự cố sẽ làm breaker mở, và mọi lời gọi tới Provider B cũng bị chặn theo — dù B hoàn toàn khoẻ.

Đây chính là chữ **isolate** trong bộ ba *contain–isolate–recover* ở [slide 9](#s9). Về mặt code, nó nghĩa là breaker phải 
 được đánh khoá theo `(provider, model, task)` chứ không phải một biến toàn cục — một chi 
 tiết nhỏ trong cấu trúc dữ liệu nhưng quyết định việc hệ thống có thật sự chịu lỗi được hay không.

### Slide 13 Circuit breaker ở mức code — và bốn tham số

> Trích slide 
>  " class CircuitBreaker: · def call(self, fn, *args, **kwargs): · 
>  if self.state == "OPEN": · if not self.ready_to_probe(): raise CircuitOpenError() · 
>  self.state = "HALF_OPEN" · try: result = fn(...); self.record_success(); return result · 
>  except Exception: self.record_failure(); raise " 
>  "Các tham số chính: ■ failure_threshold ■ reset_timeout_seconds 
>  ■ success_threshold ■ exception nào được tính là failure" 
>  " Production multi-instance: state nên có backend chung như Redis, không chỉ 
>  in-memory. "

Đoạn code chỉ mười mấy dòng, nhưng tham số thứ tư — *"exception nào được tính là failure"* — 
 là tham số **không xuất hiện trong code** và lại là tham số dễ làm hỏng cả cơ chế nhất.

except Exception

Đoạn code như trên tính **mọi** ngoại lệ là failure. Nhưng không phải lỗi nào cũng 
 là lỗi của provider:

| Ngoại lệ | Có phải lỗi provider? | Nên tính là failure? |
| --- | --- | --- |
| Timeout, 500, 503 | ✓ có | Có — đúng thứ breaker sinh ra để bắt |
| 429 rate limit | ✓ có, nhưng khác loại | Có — và nên có breaker riêng, vì cách chữa là giảm tải chứ không phải đổi provider |
| 400 bad request, schema sai | ✕ không — lỗi của bạn | Không. Provider hoàn toàn khoẻ; mở breaker chỉ che mất bug của bạn |
| 401 sai API key | ✕ không — lỗi cấu hình | Không. Đổi provider không cứu được, và breaker sẽ mở vĩnh viễn |
| Guardrail chặn nội dung | ✕ không — hệ thống chạy đúng | Không. Đây là thành công của lớp an toàn |

Nếu tính lỗi 400 là failure, một đợt request sai định dạng sẽ mở breaker 
 và **chặn luôn cả traffic hợp lệ** — bạn tự gây ra outage bằng chính cơ chế chống 
 outage. Đây là dạng lỗi rất khó truy ra vì mọi thứ trông đúng thiết kế.

**Ba tham số còn lại có ý nghĩa vận hành rõ ràng, và chúng đánh đổi với nhau:**

| Tham số | Đặt thấp thì | Đặt cao thì |
| --- | --- | --- |
| failure_threshold bao nhiêu lỗi thì mở | Mở nhanh, chặn thiệt hại sớm — nhưng dễ mở nhầm vì một chùm lỗi ngẫu nhiên | Ít mở nhầm — nhưng để lọt nhiều lời gọi vào provider đã hỏng |
| reset_timeout_seconds bao lâu thì thử lại | Phục hồi nhanh sau khi provider khoẻ — nhưng tốn nhiều lần thăm dò vô ích khi outage kéo dài | Ít thăm dò vô ích — nhưng có thể để hệ thống ở chế độ suy giảm lâu hơn cần thiết |
| success_threshold bao nhiêu lần thành công thì đóng lại | Trở lại bình thường nhanh — nhưng dễ đóng khi provider mới hồi một nửa | Chắc chắn hơn — nhưng kéo dài thời gian chạy ở bậc fallback |

Mô-đun bên dưới cho bạn tự đặt ba con số này và xem chúng đổi kết quả bao nhiêu.

trong bộ nhớ mỗi instance

4 × failure_threshold

#### Tương tác Circuit breaker cứu được bao nhiêu lời gọi

Đặt kịch bản outage và ba tham số breaker. Mô-đun đếm số lời gọi thật sự chạm tới 
 provider đã hỏng, thời gian chờ bị lãng phí, và độ trễ phục hồi.

Mặc định: provider chết **5 phút**, hệ thống nhận **2 request/giây**, 
 timeout **10 giây**, `failure_threshold = 5`, `reset_timeout = 30 giây`.

Không có breaker, cả **600** request đều đâm vào provider chết và mỗi request chờ đủ 
 10 giây. Đoán trước: *có* breaker thì bao nhiêu request còn chạm tới provider?

#### Nhìn thẻ số đầu tiên rồi mở

**15 — tức 2,5% của 600. Breaker chặn được 97,5%.**

**Con số 15 đến từ đâu:** 5 lời gọi đầu tiên phải thất bại thật thì breaker mới 
 biết mà mở (đó là `failure_threshold` ). Sau đó, cứ mỗi 30 giây breaker thả *một* request thăm dò — 300 giây outage chia cho 30 giây được 10 lần thăm dò. **5 + 10 = 15.**

**Điều đáng chú ý hơn con số:** 585 request còn lại được trả lời *ngay lập tức* ở trạng thái OPEN — 0 ms, không có lời gọi mạng nào. Không có breaker, 
 585 request đó mỗi cái chờ 10 giây rồi vẫn thất bại. Tổng thời gian chờ bị đốt vô ích rơi từ **6.000 giây (100 phút) xuống 150 giây (3 phút)**.

**Vì sao đây là lập luận thuyết phục nhất cho circuit breaker:** nó không chỉ tiết 
 kiệm tiền và tải. Nó đổi trải nghiệm người dùng từ *"chờ 10 giây rồi báo lỗi"* sang *"báo ngay và chuyển sang phương án dự phòng"*. Fail nhanh là một tính năng.

*Thử thêm:* kéo `reset_timeout` xuống 10 giây — số lời gọi chạm provider tăng 
 lên **35**, nhưng khi provider khoẻ lại bạn phát hiện trong vòng 10 giây thay vì 30. 
 Kéo lên 60 giây thì chỉ còn **10** lời gọi, đổi lại có thể chạy ở bậc fallback lâu hơn 
 cần thiết tới một phút. Đó là toàn bộ đánh đổi của tham số này, và không có giá trị nào đúng cho 
 mọi hệ thống.

- **Control - Provider chết trong 5 phút**: min `30`, max `900`, step `30`, default `300`

- **Control - Lưu lượng 2 req/giây**: min `1`, max `40`, step `1`, default `2`

- **Control - Timeout mỗi lời gọi 10 s**: min `1`, max `30`, step `1`, default `10`

- **Control - failure_threshold 5**: min `1`, max `20`, step `1`, default `5`

- **Control - reset_timeout 30 s**: min `5`, max `120`, step `5`, default `30`

Lời gọi chạm provider hỏng

—

—

Chặn được

—

so với không có breaker

Thời gian chờ bị đốt

—

—

Chậm nhất bao lâu mới nhận ra provider đã khoẻ

—

bằng đúng reset_timeout

chạm provider hỏng (chờ hết timeout) trả lời ngay ở trạng thái OPEN · 0 ms

#### Xem bảng quét reset_timeout



#### Công thức & giới hạn của mô hình

- Không có breaker: mọi request trong thời gian outage đều chạm provider và chờ hết timeout ⇒ 
 số lời gọi = R × D, thời gian đốt = R × D × T.
- Có breaker: số lời gọi = failure_threshold + floor(D / reset_timeout) — nhóm đầu 
 là các lần lỗi cần thiết để breaker học được, nhóm sau là các lần thăm dò ở HALF-OPEN.
- Độ trễ phục hồi tệ nhất bằng đúng reset_timeout: nếu provider khoẻ lại ngay sau 
 một lần thăm dò thất bại, bạn phải đợi trọn chu kỳ tiếp theo mới biết.
- Đây là mô hình đếm, không phải mô phỏng. Nó giả định outage là 
 toàn phần và liên tục — đúng với chaos scenario 1 ở slide 24 
 ("primary provider timeout 100%"), nhưng không áp cho scenario 2 (lỗi ngắt quãng 50%), 
 nơi breaker sẽ đóng-mở lặp lại và cần mô phỏng ngẫu nhiên mới ước lượng được.
- Giả định success_threshold = 1. Nếu đặt cao hơn, mỗi chu kỳ phục hồi cần nhiều 
 lời gọi thăm dò hơn, nên con số thực tế cao hơn một chút.
- Giả định một instance gateway. Với N instance dùng state trong bộ nhớ riêng, 
 nhân số lời gọi lên khoảng N lần — đúng lý do slide 13 khuyên dùng backend chung.
- Không mô hình hoá chi phí tiền: request bị timeout thường vẫn bị tính phí một phần hoặc toàn 
 phần tuỳ provider.

### Slide 14 Fallback ladder — tụt bậc có kiểm soát

> Trích slide 
>  " Best model highest quality → Backup provider same feature set 
>  → Cheaper/smaller model limited quality → Cached response → 
>  Static fallback message " 
>  "Fallback không chỉ là đổi model. Cần kiểm tra feature compatibility: 
>  JSON mode, tool calling, context length, latency/cost, policy behavior."

Thang này có một tính chất dễ bỏ qua: **hai bậc cuối không phải là model**. Bậc 4 là 
 một câu trả lời đã lưu từ trước, bậc 5 là một câu xin lỗi viết sẵn. Nghĩa là thang không kết thúc 
 bằng "model tệ nhất" mà bằng *"không dùng model nữa"* — và đó là lựa chọn thiết kế có chủ ý.

_Sơ đồ: Thang tụt bậc năm nấc và danh sách kiểm tra tương thích tính năng - Năm bậc xuống dần. Bậc một là model tốt nhất, chất lượng cao nhất. Bậc hai là provider dự phòng cùng bộ tính năng. Bậc ba là model rẻ hơn hoặc nhỏ hơn, chất lượng giới hạn. Bậc bốn là câu trả lời lấy từ cache, có thể đã cũ. Bậc năm là thông báo tĩnh, không trả lời được nhưng trung thực. Bên phải là năm thứ cần kiểm tra trước mỗi lần tụt bậc: JSON mode, tool calling, độ dài context, độ trễ và chi phí, và hành vi chính sách._

Hình 3 — Thang tụt bậc (slide 14).

danh sách các mức chất lượng bạn chấp nhận được

Câu *"Fallback không chỉ là đổi model"* nghe hiển nhiên, nhưng hậu quả thì không. Giả sử 
 agent của bạn dựa vào **structured output** để lấy về một JSON có schema cố định — 
 đúng như node phân loại trong bài lab Ngày 23.

Provider chính hỏng, breaker mở, hệ thống tụt xuống một model nhỏ hơn *không hỗ trợ JSON 
 mode*. Model trả về văn xuôi. Code parse ném lỗi. **Fallback vừa tạo ra một sự cố 
 mới** — và tệ hơn, sự cố này chỉ xuất hiện *trong lúc đang có sự cố*, tức đúng lúc 
 khó chẩn đoán nhất.

**Hệ quả cho kiểm thử:** đường fallback phải được test *thường xuyên*, không chỉ test một lần lúc viết. Cách rẻ nhất là ép hệ thống chạy fallback 
 trên một phần nhỏ lưu lượng theo lịch — nếu đường dự phòng chỉ được dùng lúc khẩn cấp, nó sẽ hỏng 
 lúc khẩn cấp.

① JSON mode và ② tool calling

vỡ code

③ context length

④ latency/cost

⑤ policy behavior

bẫy over-filtering của Ngày 24

### Slide 15 Bài tập nhóm — thiết kế chính sách fallback

> Trích slide 
>  "Nhóm 3 người - 8 phút — Mỗi nhóm chọn 1 task: customer support, code review, medical triage, 
>  hoặc internal HR chatbot. Thiết kế fallback ladder 4 bậc và nêu task nào không được phép 
>  fallback sang model yếu hơn." 
>  "Gợi ý trade-off: ■ Quality vs latency ■ Cost vs safety ■ Cached answer vs freshness 
>  ■ Static response vs user trust" 
>  "Output cần nộp: ■ Ladder 4 bậc ■ Điều kiện chuyển bậc ■ Metric để kiểm chứng ■ Rủi ro lớn nhất"

Câu hỏi cài trong đề bài — *"task nào không được phép fallback sang model yếu hơn"* — là câu 
 quan trọng nhất, và đáp án nằm ngay trong danh sách bốn task được đưa ra:

| Task | Được tụt bậc? | Vì sao |
| --- | --- | --- |
| Customer support | ✓ được, đủ 5 bậc | Câu trả lời kém vẫn hữu ích hơn không có câu trả lời; sai thì sửa được ở lượt sau |
| Internal HR chatbot | ✓ được | Rủi ro thấp, người dùng nội bộ, dễ kiểm chứng lại |
| Code review | ⚠ hạn chế | Model yếu bỏ sót lỗi mà vẫn báo "đã review" — tệ hơn không review, vì tạo cảm giác an toàn giả |
| Medical triage | ✕ không | Phân loại sai mức độ khẩn cấp gây hại trực tiếp. Không có "chất lượng chấp nhận được thấp hơn" |

Tụt bậc chấp nhận được khi **câu trả lời kém vẫn tốt hơn không có câu trả lời**. 
 Nó không chấp nhận được khi **câu trả lời kém tệ hơn việc thừa nhận không trả lời được**.

Cách kiểm nhanh: hỏi *"nếu người dùng biết câu này do model dự phòng sinh ra, họ có còn muốn 
 dùng không?"* Với hỗ trợ khách hàng: có. Với phân loại cấp cứu: không.

**Với task không được tụt bậc, thang vẫn tồn tại — chỉ là nó ngắn:** bậc 1 (model tốt nhất), bậc 2 (provider dự phòng *cùng năng lực* ), rồi nhảy thẳng xuống bậc 5 
 (thông báo tĩnh, chuyển sang người thật). Không có bậc 3 và 4. Đây là câu trả lời được điểm cao, 
 vì nó cho thấy bạn hiểu thang là công cụ chứ không phải nghi thức.

fallback success 
 rate

Slide 22

≥ 95%

route reason

slide 29

#### Ô kiểm tra — Chương 2

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao circuit breaker cần trạng thái HALF-OPEN? Nếu bỏ nó và cho OPEN 
 chuyển thẳng về CLOSED sau reset timeout thì sao? Hiểu

#### Đáp án

**Vì phục hồi đột ngột tái tạo đúng cascading failure mà breaker sinh ra để chặn.**

Trong lúc OPEN, request vẫn tiếp tục đến. Nếu về CLOSED ngay, *toàn bộ* lưu lượng đổ vào 
 provider cùng lúc. Provider chưa chắc đã khoẻ hẳn ⇒ lại lỗi hàng loạt ⇒ breaker lại mở ⇒ hệ thống 
 dao động liên tục (đóng-mở lặp lại), và mỗi vòng lại đấm một nhát vào provider đang hồi phục.

**HALF-OPEN giải quyết bằng cách thả đúng MỘT request thăm dò.** Chi phí của phép 
 thử là một lời gọi thay vì cả hàng đợi. Thành công đủ `success_threshold` lần thì về 
 CLOSED; thất bại thì quay lại OPEN ngay và đợi tiếp.

**Chi tiết hay bị quên:** máy trạng thái có *bốn* chuyển, không phải ba — 
 chuyển HALF-OPEN → OPEN (probe lỗi) chính là chuyển giữ cho hệ không dao động.

**2.** Đội bạn cấu hình breaker với `except Exception` — mọi ngoại lệ 
 đều tính là failure. Nêu một kịch bản trong đó cấu hình này *tự gây ra* outage. Phân tích

#### Đáp án

**Kịch bản:** một client mới deploy gửi request sai schema, provider trả **400 Bad Request** hàng loạt. Breaker đếm chúng là failure, vượt ngưỡng, và **mở**. Từ lúc đó mọi traffic hợp lệ cũng bị chặn — kể cả khi provider hoàn toàn khoẻ.

Bạn vừa tự tạo outage *bằng chính cơ chế chống outage*, và rất khó truy vì mọi thành 
 phần đều đang chạy đúng như được viết.

**Kịch bản tương đương cũng được chấp nhận:** sai API key (401) làm breaker mở 
 vĩnh viễn — đổi provider không cứu được vì nguyên nhân là cấu hình; hoặc guardrail chặn nội dung 
 bị tính là failure, trong khi đó là *thành công* của lớp an toàn.

**Cách sửa:** phân loại tường minh — chỉ tính là failure các lỗi *của 
 provider* (timeout, 500, 503, và 429 với breaker riêng). Lỗi 4xx do client, lỗi cấu hình và 
 quyết định của guardrail đều không được tính.

**3.** Agent của bạn dùng structured output để phân loại yêu cầu. Nêu rủi ro cụ 
 thể khi fallback sang một model nhỏ hơn, và cách phát hiện rủi ro đó *trước* khi sự cố xảy 
 ra. Đánh giá

#### Đáp án

**Rủi ro: model dự phòng không hỗ trợ JSON mode.** Nó trả về văn xuôi, code parse 
 ném lỗi, và fallback vừa tạo ra một sự cố mới — *đúng lúc đang có sự cố*, tức lúc khó chẩn 
 đoán nhất.

Đây chính là điều slide 14 cảnh báo: "Fallback không chỉ là đổi model. Cần kiểm tra feature 
 compatibility: JSON mode, tool calling, context length, latency/cost, policy behavior."

**Phát hiện trước bằng cách nào:**

① **Test đường fallback trong CI** — có test ép router đi xuống từng bậc và kiểm 
 kết quả parse được, chứ không chỉ test đường chính. 
 ② **Chạy fallback trên một phần nhỏ lưu lượng theo lịch** — nếu đường dự phòng chỉ 
 được dùng lúc khẩn cấp thì nó sẽ hỏng lúc khẩn cấp. 
 ③ **Đưa vào chaos test** (slide 24, scenario 1): ép primary timeout 100% và kiểm 
 bằng chứng gateway route sang fallback *thành công*, không chỉ route đi.

**Metric:** fallback success rate, mục tiêu ≥ 95% (slide 22). Chỉ tính được nếu 
 có ghi route reason cho từng request.

---

<!-- chiron-source-span: {"source_span_id":"a8524c82-41be-5128-bccb-116bf7234f87","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Caching & cost budgeting","source_file":"track-3-day-25.html"},"checksum":"3eb3141964412d6381c7ffb6275ebddb138b038c0082949c6cf49ad287e4d4ed"} -->

## 03 Caching & cost budgeting

Slide 16–20: ba tầng cache, luồng semantic cache và cái bẫy false-hit, ba lớp kiểm soát chi phí.

### Slide 16–17 Ba tầng cache cho ứng dụng LLM

> Trích slide 
>  "Cache đúng chỗ có thể giảm latency/cost; cache sai chỗ tạo stale answer và hallucination 
>  ổn định. " 
>  "1. Provider prompt/prefix cache: giảm cost khi prefix dài được reuse 
>  2. App semantic response cache: query tương tự → reuse response 
>  3. Tool/result cache: API/DB/result expensive nhưng deterministic" 
>  " Cache deterministic và low-risk trước. Với semantic response cache, cần 
>  threshold, TTL, invalidation, và allowlist theo task."

Ba tầng này khác nhau ở một điểm quyết định: **mức độ chắc chắn rằng thứ lấy ra từ cache 
 đúng bằng thứ bạn sẽ tính lại**. Đó là trục để xếp hạng rủi ro, và nó giải thích luôn câu 
 "cache deterministic và low-risk trước".

| Tầng | Khoá cache là gì | Trúng cache có chắc đúng không? | Rủi ro |
| --- | --- | --- | --- |
| 1 · Prefix cache (phía provider) | Tiền tố prompt khớp chính xác | Chắc chắn — provider vẫn sinh phần đuôi bình thường | Gần như không có. Chỉ giảm tiền, không đổi kết quả |
| 3 · Tool/result cache | Tham số lời gọi khớp chính xác | Chắc, nếu dữ liệu chưa đổi | Chỉ có stale — chữa bằng TTL và invalidation theo sự kiện |
| 2 · Semantic response cache | Câu hỏi gần giống theo vector | Không chắc — "gần giống" không phải "cùng ý" | Vừa stale vừa trả nhầm câu của người khác |

Thứ tự đánh số theo *vị trí trong kiến trúc* (provider → app → tool). Thứ tự triển khai 
 thì theo *rủi ro*, và câu "cache deterministic và low-risk trước" đảo tầng 2 xuống cuối.

**Tầng 1 gần như miễn phí về rủi ro:** bạn bật nó lên, hoá đơn giảm, không có gì 
 khác đổi. Nếu prompt hệ thống của bạn dài (mà prompt agent thì luôn dài — chỉ dẫn, định nghĩa tool, 
 few-shot), đây là khoản tiết kiệm lớn nhất mà không phải đánh đổi gì.

**Tầng 3 rủi ro có kiểm soát:** nó chỉ hỏng theo một chiều — dữ liệu cũ. Bạn biết 
 chính xác cần chữa gì: TTL đủ ngắn, và xoá cache khi có sự kiện thay đổi dữ liệu.

**Tầng 2 mới là chỗ cần dè chừng**, vì nó hỏng theo một 
 chiều mà bạn không lường trước được: hai câu hỏi nghe giống nhau nhưng hỏi hai việc khác nhau. 
 Slide dành hẳn slide sau để nói về nó.

Một câu bịa thông thường là ngẫu nhiên — chạy lại có thể không lặp lại, nên lấy mẫu vài lần là 
 bắt được, và đó chính là nguyên lý của SelfCheckGPT ở [Ngày 24](track-3-day-24.html).

Một câu bịa *đã được cache* thì **lặp lại y hệt cho mọi 
 người dùng cho tới khi hết TTL**. Nó vượt qua mọi phép kiểm dựa trên tính nhất quán, vì nó 
 hoàn toàn nhất quán. Cache vừa biến một lỗi ngẫu nhiên thành một lỗi có hệ thống — và đó là lý do 
 slide 16 chọn đúng từ "ổn định" thay vì "nhiều hơn".

### Slide 18 Luồng semantic cache — và hai metric phải đo cùng nhau

> Trích slide 
>  "User query → Embed → Vector search → sim > threshold → HIT return 
>  cache / sim < threshold → MISS call LLM → Store result" 
>  " Cache poisoning: hai query cosine gần nhau nhưng intent khác nhau. 
>  Metric quan trọng: hit rate và false-hit rate."

Luồng thì đơn giản. Cái slide vẽ ra *không đầy đủ*, và chỗ thiếu chính là chỗ nguy hiểm: 
 nhánh HIT có **hai kết cục**, không phải một.

_Sơ đồ: Luồng semantic cache với nhánh trúng đúng và trúng nhầm - Câu hỏi người dùng được nhúng thành vector rồi tìm kiếm trong kho vector. Nếu độ tương đồng dưới ngưỡng thì trượt cache, gọi LLM, lưu kết quả lại. Nếu trên ngưỡng thì trúng cache, nhưng trúng cache tách làm hai kết cục: trúng đúng khi ý định thật sự giống nhau, trả lời nhanh và rẻ; và trúng nhầm khi hai câu hỏi gần nhau về vector nhưng khác ý định, lúc đó người dùng nhận câu trả lời của người khác. Nhánh trúng nhầm không xuất hiện trên slide gốc và cũng không tạo ra lỗi nào trong log._

Hình 4 — Luồng semantic cache (slide 18, có bổ sung).

trúng nhầm

"false-hit rate"

Hạ ngưỡng tương đồng ⇒ nhiều câu hỏi được coi là "đủ giống" ⇒ **hit rate tăng**. 
 Báo cáo trông tuyệt: tiết kiệm nhiều hơn, nhanh hơn.

Nhưng đúng thao tác đó cũng làm **false-hit rate tăng** — và false-hit không tạo ra 
 lỗi nào. Không có exception, không có mã 500, độ trễ còn *tốt hơn* bình thường. Người dùng 
 chỉ nhận một câu trả lời mạch lạc, tự tin, và không liên quan đến câu họ hỏi.

**Đây chính là silent degradation ở [slide 10](#s10), 
 nhưng do chính bạn tạo ra.** Và nó là lý do slide 18 không viết "metric quan trọng: hit rate" 
 mà viết *"hit rate **và** false-hit rate"*. Báo cáo chỉ có hit rate là báo cáo 
 chưa hoàn chỉnh — rubric ở [slide 29](#s29) đòi *"false-hit examples"*, tức là ví 
 dụ cụ thể, không phải chỉ con số.

Trong bảo mật, *cache poisoning* thường nghĩa là kẻ tấn công cố tình nhét dữ liệu độc vào 
 cache. Slide dùng từ này theo nghĩa nhẹ hơn và cụ thể hơn: **hai query cosine gần nhau nhưng intent khác nhau** — tức là tai nạn, không phải tấn công.

Ví dụ dễ thấy trong bối cảnh khách sạn: *"Phòng 302 còn trống không?"* và *"Phòng 320 còn trống không?"* gần như trùng khớp về vector — khác đúng một chữ số, và mô 
 hình nhúng không được huấn luyện để coi con số là quan trọng. Nhưng hai câu hỏi hai phòng khác nhau, 
 và câu trả lời sai ở đây dẫn tới một sự cố thật với khách. Đây chính là lý do [slide 20](#s20) xếp truy vấn liên quan tới tài khoản vào nhóm **không cache**.

Slide 17

threshold

TTL

invalidation

allowlist theo task

được phép

quyết định phạm vi

#### Tương tác Cache — tiền tiết kiệm được và cái giá phải trả

Nhập tỷ lệ trúng cache và tỷ lệ trúng nhầm mà bạn *đo được*. Mô-đun quy đổi 
 chúng ra tiền tiết kiệm mỗi tháng, độ trễ trung bình, và số câu trả lời sai phục vụ mỗi ngày.

Mặc định: **3.000 lượt/ngày**, trúng cache **40%**, trong số lần trúng 
 thì **2%** là trúng nhầm, giá mỗi lời gọi LLM **$0,002**.

Đoán trước: mỗi tháng tiết kiệm được bao nhiêu, và mỗi ngày có bao nhiêu người nhận câu trả lời 
 của người khác?

#### Xem thẻ số rồi mở

**Tiết kiệm $72/tháng. Và 24 câu trả lời sai mỗi ngày** — tức khoảng 720 lượt 
 mỗi tháng.

**Thẻ số thứ tư là thẻ đáng nhìn nhất:** chia hai con số đó cho nhau ra **giá của mỗi câu trả lời sai ≈ $0,10**. Đó là cách phát biểu lại toàn bộ đánh đổi 
 thành một câu trả lời được: *"Bạn có sẵn sàng trả 10 xu để đổi lấy một lần trả lời sai 
 không?"*

**Và câu trả lời phụ thuộc hoàn toàn vào việc câu hỏi đó là gì** — đúng như bảng 
 ở [slide 20](#s20):

• *"Bữa sáng mấy giờ?"* — trả lời sai thì khách hỏi lại. 10 xu quá rẻ. **Cache.** 
 • *"Phòng tôi đã thanh toán chưa?"* — trả lời sai là một sự cố với khách và có thể là vấn 
 đề riêng tư. 10 xu không mua nổi. **Không cache.**

Nên câu hỏi đúng không bao giờ là *"có nên dùng cache không"* mà là **"loại truy vấn nào được vào allowlist"**. Một con số hit rate cho toàn hệ thống 
 che mất đúng câu hỏi đó.

*Thử thêm:* kéo tỷ lệ trúng nhầm xuống **0,2%** — giá mỗi câu sai vọt lên 
 $1,00, tức cache trở nên đáng giá gấp mười lần. Đó là lý do việc siết ngưỡng và giới hạn allowlist 
 có giá trị lớn hơn nhiều so với việc cố nâng hit rate.

- **Control - Lưu lượng 3.000 lượt/ngày**: min `100`, max `20000`, step `100`, default `3000`

- **Control - Tỷ lệ trúng cache 40%**: min `0`, max `90`, step `1`, default `40`

- **Control - Trúng nhầm (trong số lần trúng) 2,0%**: min `0`, max `100`, step `1`, default `20`

- **Control - Giá mỗi lời gọi LLM $0,0020**: min `1`, max `100`, step `1`, default `20`

- **Control - Độ trễ khi gọi LLM 1.200 ms**: min `200`, max `5000`, step `100`, default `1200`

Tiết kiệm mỗi tháng

—

—

Câu trả lời sai mỗi ngày

—

—

Độ trễ trung bình

—

—

Giá của mỗi câu trả lời sai

—

tiền tiết kiệm ÷ số câu sai

chi phí gọi LLM phần cache trả lời (≈ 0đ)

#### Xem bảng quét tỷ lệ trúng cache



#### Công thức & giới hạn của mô hình

- tiết kiệm/ngày = lưu lượng × hit_rate × giá mỗi lời gọi; 
 câu sai/ngày = lưu lượng × hit_rate × false_hit_rate. Tháng = ngày × 30.
- độ trễ trung bình = hit_rate × 40ms + (1 − hit_rate) × độ trễ LLM. Con số 40 ms 
 cho một lần trúng cache là giả định của tài liệu này (nhúng câu hỏi cộng tìm 
 vector), không có trên slide.
- Mọi con số đầu vào ở đây là do bạn nhập, không phải từ slide. Slide 18 chỉ 
 nói phải đo hit rate và false-hit rate; nó không đưa giá trị mẫu. Hãy thay bằng số đo thật của hệ 
 thống bạn trước khi trích dẫn bất kỳ kết quả nào.
- Mô hình không giả định mối quan hệ nào giữa ngưỡng tương đồng và hai tỷ lệ 
 kia — vì quan hệ đó phụ thuộc dữ liệu và mô hình nhúng của bạn. Chỉ có một điều chắc chắn về mặt 
 định tính: hạ ngưỡng làm cả hai tỷ lệ cùng tăng.
- Bỏ qua chi phí vận hành cache (kho vector, bộ nhớ, chi phí nhúng mỗi truy vấn). Với lưu lượng 
 nhỏ, chi phí nhúng có thể ăn hết phần tiết kiệm.
- Giả định mọi lời gọi LLM có giá như nhau. Thực tế giá thay đổi theo độ dài prompt và câu trả 
 lời, nên nếu cache trúng nhiều ở các truy vấn ngắn thì tiền tiết kiệm thật thấp hơn.
- Không mô hình hoá stale — một lần trúng đúng ý định nhưng dữ liệu đã cũ vẫn tính là 
 trúng đúng ở đây. TTL và invalidation nằm ngoài phạm vi mô hình.

### Slide 19 Cost budgeting — độ tin cậy của ví tiền

> Trích slide 
>  " 3 lớp control: 1. Per-request cap: max tokens, max tools, 
>  timeout. 2. Per-user/app rate limit: token bucket. 3. Monthly budget: 
>  warn 80%, hard stop/route cheap at 100%." 
>  " Metric cần log: ■ provider, model, route reason ■ input/output tokens, estimated 
>  cost ■ cache hit/miss, similarity score ■ latency, status, circuit state" 
>  "Đừng chỉ tổng cost theo ngày. Cần cost theo feature/user/model để tìm đường call 
>  đắt và tối ưu đúng nơi."

Tiêu đề slide — *"reliability của ví tiền"* — là cách đóng khung rất chính xác. Hết ngân 
 sách **là một dạng outage**, chỉ khác là nó xảy ra chậm và ở nơi không ai theo dõi. Ba 
 lớp kiểm soát tương ứng với ba khoảng thời gian:

| Lớp | Chặn cái gì | Thang thời gian | Hỏng thì hậu quả là |
| --- | --- | --- | --- |
| 1 · Per-request cap max tokens, max tools, timeout | Một request chạy mất kiểm soát | Giây | Một agent lặp vô hạn đốt hết ngân sách trong vài phút |
| 2 · Rate limit theo user/app token bucket | Một người dùng chiếm hết tài nguyên | Phút — giờ | Một script hoặc một người dùng lạm dụng làm chậm mọi người |
| 3 · Ngân sách tháng cảnh báo 80%, dừng ở 100% | Tổng chi vượt kế hoạch | Ngày — tháng | Hoá đơn bất ngờ, hoặc dịch vụ bị cắt giữa tháng |

*"max tools"* và *"timeout"* ở mức mỗi request chính là **bounded retry** và **recursion limit** trong LangGraph. Một agent bị kẹt trong vòng lặp `tool → error → retry → tool` sẽ đốt tiền đúng như nó đốt thời gian.

Điều này khép lại một vòng: **nhóm lỗi ④ (orchestration loop)** ở [slide 8](#s8) không chỉ gây treo workflow — nó còn là con đường nhanh nhất để đốt ngân 
 sách. Cùng một cơ chế phòng vệ, hai loại thiệt hại.

**Về hành vi ở mốc 100% — slide đưa hai lựa chọn và chúng rất khác nhau:**

**Hard stop** — dừng phục vụ. Chi phí không bao giờ vượt trần, nhưng đây là một 
 outage tự gây ra, và nó xảy ra đúng lúc bạn đang được dùng nhiều nhất.

**Route cheap** — tụt xuống model rẻ hơn. Đây chính là [bậc 3 của 
 thang fallback](#s14), chỉ khác là kích hoạt bởi *tiền* thay vì bởi *lỗi*. Dịch vụ vẫn 
 chạy ở chất lượng thấp hơn, chi phí giảm nhưng không về không.

**Nhận xét đáng nhớ:** thang fallback không chỉ dành cho sự 
 cố kỹ thuật. Nó là cơ chế chung để *tụt bậc chất lượng có kiểm soát*, và ngân sách cạn là một 
 lý do tụt bậc hợp lệ y như provider chết. Nếu bạn đã xây thang cho lý do thứ nhất, bạn dùng lại được 
 nó cho lý do thứ hai gần như miễn phí — chỉ cần thêm một điều kiện chuyển bậc.

Bốn dòng metric ở slide này gần như trùng khớp với danh sách metric bắt buộc ở [slide 28](#s28) để chấm điểm. Chú ý ba trường hay bị quên:

• **`route reason`** — vì sao request này đi đường đó. Không có nó thì 
 không tính được fallback success rate. 
 • **`similarity score`** — không chỉ hit/miss mà là *trúng ở mức nào*. 
 Đây là thứ duy nhất cho phép bạn điều chỉnh ngưỡng về sau bằng dữ liệu thật thay vì đoán. 
 • **`circuit state`** — trạng thái breaker lúc request đi qua. Không có nó 
 thì không chứng minh được breaker đã hoạt động trong chaos test.

Cả ba đều rẻ để ghi *ngay từ đầu* và gần như không thể khôi phục 
 về sau. Nếu bắt đầu lab, hãy thêm ba trường này vào bản ghi log trong giờ đầu tiên.

### Slide 20 Bài tập — cache hay không cache

> Trích slide 
>  "FAQ admissions — nên cache semantic — rủi ro: thông tin deadline stale · 
>  Account balance — không cache response — privacy + freshness · 
>  Code explanation — cache có điều kiện — context khác nhau · 
>  Weather today — tool cache TTL ngắn — stale theo thời gian · 
>  Policy summary — cache + event invalidation — policy update"

Bảng năm dòng này là **bản mẫu của một allowlist**, và nó dạy bốn chế độ cache khác 
 nhau chứ không phải hai. Đọc theo cột "quyết định" sẽ thấy phổ:

| Chế độ | Dòng ví dụ | Điều kiện áp dụng được |
| --- | --- | --- |
| Cache semantic thoải mái | FAQ tuyển sinh | Câu hỏi lặp lại nhiều, câu trả lời chung cho mọi người, thay đổi chậm |
| Cache + xoá theo sự kiện | Tóm tắt chính sách | Thay đổi hiếm nhưng đột ngột — TTL không đủ, cần hook lúc cập nhật |
| Cache tool với TTL ngắn | Thời tiết hôm nay | Thay đổi đều đặn theo thời gian — TTL là công cụ đúng |
| Cache có điều kiện | Giải thích code | Câu hỏi giống nhau nhưng ngữ cảnh khác nhau — phải đưa ngữ cảnh vào khoá cache |
| Không cache | Số dư tài khoản | Dữ liệu riêng cho từng người hoặc phải tươi tuyệt đối |

Slide ghi *"privacy + freshness"*. Hai lý do này không cùng mức độ:

**Freshness** — trả về số dư cũ là sai, nhưng sai theo cách *tự sửa được*: 
 người dùng tải lại, thấy số đúng, hết chuyện.

**Privacy** — nếu semantic cache trúng nhầm giữa hai người dùng khác nhau, người này 
 nhận **dữ liệu của người kia**. Đây không còn là lỗi chất lượng mà là *sự cố lộ dữ liệu*, và nó rơi thẳng vào trục Compliance mà [Ngày 24](track-3-day-24.html) mô tả.

**Quy tắc rút ra được, mạnh hơn những gì slide nói:** khoá 
 cache *phải* chứa định danh người dùng cho mọi truy vấn chạm dữ liệu cá nhân — hoặc đơn giản 
 là loại chúng khỏi allowlist hoàn toàn. Cách thứ hai an toàn hơn và rẻ hơn, vì nó không phụ thuộc 
 vào việc ai đó nhớ đặt khoá đúng.

| Loại truy vấn ở kiosk | Quyết định | Vì sao |
| --- | --- | --- |
| "Bữa sáng mấy giờ?" · "Mật khẩu wifi?" · "Trả phòng lúc mấy giờ?" | Cache semantic | Lặp lại rất nhiều, chung cho mọi khách, gần như không đổi. Đây là chỗ ROI cao nhất |
| "Chính sách huỷ phòng thế nào?" | Cache + xoá theo sự kiện | Đổi hiếm nhưng đột ngột. Hook vào lúc cập nhật chính sách |
| "Còn phòng trống không?" | Tool cache TTL rất ngắn (giây) | Đổi liên tục; nhưng nhiều khách hỏi cùng lúc nên TTL 10–30 giây vẫn có tác dụng |
| "Phòng tôi đã thanh toán chưa?" · "Đặt phòng của tôi tên gì?" | ✕ Không cache | Dữ liệu riêng từng khách. Trúng nhầm ở đây là lộ thông tin khách khác — cùng loại rủi ro với dòng "Account balance" |

Chú ý nhóm đầu tiên: ba câu hỏi đó có lẽ chiếm phần lớn lưu lượng của một 
 kiosk. **Chính vì allowlist hẹp mà cache vẫn có giá trị lớn** — bạn không cần cache mọi 
 thứ để tiết kiệm được nhiều, bạn chỉ cần cache đúng nhóm phổ biến nhất và an toàn nhất.

#### Ô kiểm tra — Chương 3

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao slide đánh số ba tầng cache là 1-2-3 nhưng lại khuyên triển khai 
 theo thứ tự khác? Hiểu

#### Đáp án

**Đánh số theo vị trí kiến trúc; triển khai theo rủi ro.** Câu 
 "cache deterministic và low-risk trước" đảo tầng 2 (semantic response cache) xuống cuối.

**Thứ tự đúng là 1 → 3 → 2:**

• **Tầng 1 (prefix cache)** — khoá là tiền tố khớp chính xác, provider vẫn sinh 
 phần đuôi bình thường ⇒ kết quả không đổi, chỉ rẻ hơn. Gần như không có rủi ro. 
 • **Tầng 3 (tool/result cache)** — khoá là tham số khớp chính xác ⇒ chỉ hỏng theo một 
 chiều duy nhất là *stale*, chữa bằng TTL và invalidation. 
 • **Tầng 2 (semantic)** — khoá là "gần giống theo vector", mà gần giống không phải 
 cùng ý ⇒ vừa stale vừa có thể trả nhầm câu của người khác.

**Trục phân biệt:** mức độ chắc chắn rằng thứ lấy từ cache đúng bằng thứ bạn sẽ 
 tính lại.

**2.** Đội bạn hạ ngưỡng tương đồng và báo cáo hit rate tăng từ 30% lên 55%. 
 Vì sao đây chưa phải tin tốt? Phân tích

#### Đáp án

**Vì hạ ngưỡng làm hit rate và false-hit rate cùng tăng — chúng luôn đi cùng chiều.** Báo cáo chỉ có một trong hai là báo cáo chưa hoàn chỉnh; slide 18 viết rõ 
 "metric quan trọng: hit rate *và* false-hit rate".

**Vì sao false-hit nguy hiểm hơn hầu hết các lỗi khác:** nó không tạo ra lỗi nào. 
 Không exception, không mã 500, độ trễ còn *tốt hơn* bình thường vì không phải gọi LLM. 
 Người dùng chỉ nhận một câu trả lời mạch lạc và không liên quan đến câu họ hỏi. Đây đúng là 
 silent degradation ở slide 10, nhưng do chính đội bạn tạo ra.

**Cần bổ sung gì vào báo cáo:** false-hit rate đo được, kèm *ví dụ cụ thể* (rubric slide 29 đòi "false-hit examples", không chỉ con số), và độ trễ/chi phí tiết kiệm đặt cạnh 
 số câu trả lời sai mỗi ngày để thấy giá phải trả.

Kiểm chứng bằng [mô-đun cache](#m-cache): ở 3.000 lượt/ngày, hit 40% và false-hit 2% 
 cho ra $72 tiết kiệm mỗi tháng đổi lấy 24 câu trả lời sai mỗi ngày — khoảng $0,10 cho mỗi câu sai.

**3.** Kiosk SmartCheck AI nhận bốn loại câu hỏi: giờ ăn sáng, chính sách huỷ 
 phòng, còn phòng trống không, và "phòng tôi đã thanh toán chưa". Quyết định cache cho từng loại và 
 nêu lý do. Áp dụng

#### Đáp án

**① Giờ ăn sáng — cache semantic thoải mái.** Lặp lại rất nhiều, câu trả lời chung 
 cho mọi khách, gần như không đổi. Đây là chỗ ROI cao nhất.

**② Chính sách huỷ phòng — cache + xoá theo sự kiện.** Thay đổi *hiếm nhưng đột 
 ngột*, nên TTL không đủ: hoặc quá dài (phục vụ chính sách cũ) hoặc quá ngắn (mất hết lợi ích). 
 Cần hook xoá cache lúc cập nhật chính sách — đúng dòng "Policy summary" ở slide 20.

**③ Còn phòng trống không — tool cache TTL rất ngắn.** Đổi liên tục, nhưng nhiều 
 khách hỏi cùng lúc nên TTL 10–30 giây vẫn có tác dụng. Đây là tầng 3, không phải tầng 2.

**④ "Phòng tôi đã thanh toán chưa" — KHÔNG cache.** Cùng loại với dòng 
 "Account balance" ở slide 20, và có *hai* lý do khác mức độ: *freshness* (số cũ thì 
 sai nhưng tự sửa được) và *privacy* — nếu semantic cache trúng nhầm giữa hai khách, người 
 này nhận dữ liệu đặt phòng của người kia. Đó là sự cố lộ dữ liệu, không phải lỗi chất lượng.

**Quy tắc chung:** mọi truy vấn chạm dữ liệu cá nhân phải có định danh người dùng 
 trong khoá cache — hoặc đơn giản là loại khỏi allowlist. Cách thứ hai an toàn hơn vì không phụ 
 thuộc vào việc ai đó nhớ đặt khoá đúng.

---

<!-- chiron-source-span: {"source_span_id":"cd48b5af-a0fe-5361-8ce1-f14f76a70bf3","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Observability & SLO","source_file":"track-3-day-25.html"},"checksum":"208523e4ce5be5a000ce5eba09d7b59e1d9dd2e03385d88cf39419c4e624168c"} -->

## 04 Observability & SLO

Slide 21–24: bốn khái niệm SLI/SLO/SLA/error budget, bốn metric tối thiểu, và chaos testing.

### Slide 21–22 SLI, SLO, SLA và error budget

> Trích slide 
>  "Không đo thì không biết system đang tốt, chậm, đắt, hay đang trả lời sai." 
>  " SLI — metric đo được — availability, P95 latency, cache hit rate, 
>  false-hit rate. SLO — target nội bộ — availability ≥ 99%, P95 < 2.5s, 
>  fallback success ≥ 95%. SLA — cam kết bên ngoài — 99.5% uptime/tháng cho 
>  customer-facing API. Error budget — mức lỗi được phép — nếu burn rate cao 
>  → freeze feature, ưu tiên reliability." 
>  "LLM agent cần thêm quality SLO: faithfulness, safety pass rate, escalation 
>  correctness."

Bốn khái niệm này hay bị dùng lẫn lộn. Cách phân biệt gọn nhất là hỏi **"ai đọc con số này, và hậu quả khi vi phạm là gì"**:

| Khái niệm | Là gì | Ai đọc | Vi phạm thì sao |
| --- | --- | --- | --- |
| SLI | Một phép đo. Không có ngưỡng, không có phán xét | Kỹ sư | Không có khái niệm "vi phạm" — nó chỉ là số |
| SLO | Ngưỡng nội bộ đặt trên SLI | Đội kỹ thuật | Dừng làm tính năng mới, dồn người vào độ tin cậy |
| SLA | Cam kết trong hợp đồng | Khách hàng, pháp lý | Tiền — hoàn phí, phạt, mất hợp đồng |
| Error budget | Phần còn được phép hỏng của SLO | Cả đội, kể cả quản lý sản phẩm | Cạn budget = đóng băng tính năng |

Nhìn qua thì ngược đời: mục tiêu nội bộ *dễ hơn* cam kết với khách hàng?

Đọc kỹ slide thì hai con số này gắn với **hai đối tượng khác nhau**: SLO 99% là cho 
 hệ thống trong lab, còn SLA 99,5% là cho *customer-facing API*. Nhưng nguyên tắc chung trong 
 ngành thì ngược lại và đáng biết:

**SLO nội bộ phải chặt hơn SLA**, để bạn phát hiện vấn đề và 
 xử lý *trước* khi chạm ngưỡng phải đền tiền. Nếu SLA là 99,5% thì SLO nội bộ nên là 99,9%: 
 khoảng đệm giữa hai con số chính là thời gian phản ứng của bạn. Đặt SLO bằng đúng SLA nghĩa là lần 
 đầu tiên bạn biết mình có vấn đề cũng là lần đầu tiên bạn đã vi phạm hợp đồng.

**Error budget là khái niệm hữu ích nhất trong bốn cái, và cũng khó chấp nhận nhất về mặt tâm 
 lý**, vì nó phát biểu một điều nghe như thất bại: *bạn được phép hỏng một lượng nhất định*.

Mục tiêu 100% uptime nghe có vẻ nghiêm túc, nhưng nó vô nghĩa về mặt kỹ thuật: chi phí tăng theo 
 hàm mũ khi tiến gần 100%, và bạn không kiểm soát được provider, mạng, hay điện.

Error budget biến câu hỏi mơ hồ *"có nên đánh đổi độ tin cậy lấy tốc độ phát triển không"* thành một câu hỏi có số: **tháng này còn bao nhiêu phút được phép hỏng?** Còn nhiều thì cứ deploy tính năng mới. Cạn rồi thì đóng băng và sửa độ tin cậy.

Điều tinh tế: nó **hết chỗ cho tranh cãi**. Không còn cảnh 
 đội sản phẩm và đội hạ tầng cãi nhau bằng cảm tính — cả hai nhìn cùng một con số, và con số đó quyết 
 định. *"Burn rate cao → freeze feature"* là một luật, không phải một đề nghị.

Ba SLO trong ví dụ — availability, P95 latency, fallback success — đều là SLO **vận hành**. Chúng đo máy móc. Câu cuối thêm ba thứ hoàn toàn khác: *faithfulness, safety pass rate, escalation correctness*.

Đây là chỗ bài này nối thẳng vào [Ngày 24](track-3-day-24.html), 
 và là hệ quả trực tiếp của [silent degradation ở slide 10](#s10): một hệ LLM có thể đạt 
 100% các SLO vận hành trong khi chất lượng câu trả lời đã tệ đi. Nếu bảng SLO của bạn chỉ có ba dòng 
 đầu, bạn đang đo *máy có chạy không* chứ không đo *nó có còn làm đúng việc không*.

#### Tương tác SLO, error budget và sức mạnh thật của fallback

Đặt mục tiêu SLO và độ tin cậy của từng provider. Mô-đun quy đổi ra số phút được phép 
 hỏng mỗi tháng, rồi so bốn kiến trúc: một provider, hai provider phụ thuộc nhau, và fallback chain.

Mặc định: mục tiêu SLO **99%**, mỗi provider tự nó đạt **99,5%**, 
 fallback thành công **95%** số lần được gọi (đúng ngưỡng slide 22 đặt ra).

Đoán trước hai điều: ① SLO 99% cho phép hỏng bao nhiêu phút mỗi tháng? ② Thêm một provider dự 
 phòng 99,5% nữa thì tổng downtime giảm còn bao nhiêu?

#### Xem biểu đồ rồi mở

**① SLO 99% = 432 phút/tháng = 7,2 giờ.** Con số này lớn hơn nhiều so với cảm giác 
 của hầu hết mọi người khi nghe "99%". Còn 99,9% chỉ cho phép **43 phút** — gấp mười 
 lần chặt hơn.

**② Một provider 99,5% hỏng 216 phút/tháng. Thêm fallback thì còn khoảng 12 phút.** Giảm khoảng **18 lần** — chỉ bằng cách thêm một đường dự phòng, không cần cải thiện 
 provider nào cả.

**Vì sao lại mạnh đến vậy:** hai đường độc lập chỉ cùng hỏng khi *cả hai* cùng hỏng, mà xác suất đó là tích của hai xác suất nhỏ. Đây là toàn bộ lý do tồn tại của fallback 
 chain, và nó là con số mạnh nhất trong cả bài học.

**Nhưng chú ý cột "hai provider phụ thuộc":** nếu request phải đi qua *cả hai* mới thành công (chuỗi phụ thuộc, không phải dự phòng), độ tin cậy tổng **giảm** xuống 99,0025% — tức 431 phút/tháng, tệ hơn một provider đơn lẻ. Cùng hai 
 thành phần, cùng độ tin cậy, mà kết quả chênh nhau **36 lần** — khác biệt duy nhất 
 là chúng được nối theo kiểu *dự phòng* hay *phụ thuộc*.

*Thử thêm:* kéo "fallback thành công" từ 95% xuống 60% — thấy ngay vì sao slide 22 đặt 
 SLO riêng cho chỉ số này. Một đường dự phòng không đáng tin thì lợi ích của nó bốc hơi rất nhanh, 
 và đó là lý do đường fallback phải được kiểm thử thường xuyên chứ không chỉ tồn tại trên sơ đồ.

- **Control - Mục tiêu SLO 99,0%**: min `900`, max `9995`, step `5`, default `9900`

- **Control - Độ tin cậy mỗi provider 99,50%**: min `9000`, max `9995`, step `5`, default `9950`

- **Control - Fallback thành công 95%**: min `0`, max `100`, step `1`, default `95`

Error budget mỗi tháng

—

—

Downtime với fallback chain

—

—

Đạt SLO chưa?

—

—

Fallback giúp giảm downtime

—

so với một provider đơn lẻ

phút hỏng mỗi tháng vượt error budget error budget theo SLO

#### Xem bảng quy đổi SLO sang thời gian



#### Công thức & giới hạn của mô hình

- Tháng quy ước 30 ngày = 43.200 phút. Error budget = 
 (1 − SLO) × 43.200.
- Một provider: downtime = (1 − A) × 43.200.
- Hai provider phụ thuộc (phải cả hai cùng chạy): A_tổng = A × A.
- Fallback chain hai bậc: A_tổng = A + (1 − A) × s × A, trong đó s là tỷ lệ 
 fallback thành công. Ba bậc thì cộng thêm một tầng tương tự. Với s = 1 công thức rút 
 về dạng lý tưởng 1 − (1 − A)ⁿ.
- Giả định lớn nhất và cũng là giả định đáng ngờ nhất: các provider hỏng độc lập 
 nhau. Thực tế chúng tương quan — cùng sự cố mạng khu vực, cùng nhà cung cấp hạ tầng, cùng 
 một đợt tấn công, hoặc đơn giản là một prompt sai thì cả hai cùng từ chối. Khi có tương quan, lợi 
 ích thật thấp hơn đáng kể so với con số ở đây. Hãy đọc kết quả như một trần trên, 
 không phải một dự báo.
- Không mô hình hoá độ trễ khi chuyển bậc: mỗi lần fallback tốn thêm thời gian phát hiện lỗi 
 cộng thời gian gọi lại, nên trải nghiệm trong khoảng đó vẫn xấu dù không tính là downtime.
- Không mô hình hoá suy giảm chất lượng: fallback chain giữ được availability nhưng bậc 
 dưới có thể trả lời tệ hơn. Đây đúng là lý do slide 22 đòi thêm quality SLO bên cạnh uptime SLO.

### Slide 23 Bốn metric tối thiểu — và bốn kiểu Prometheus

> Trích slide 
>  " REQUESTS = Counter("agent_requests_total", ["provider", "status", "route"]) 
>  LATENCY = Histogram("agent_latency_seconds", ["provider", "route"]) 
>  CACHE_HITS = Counter("cache_hits_total", ["cache_type"]) 
>  CIRCUIT_STATE = Gauge("circuit_state", ["provider"]) # 0 closed, 1 open, 2 half-open 
>  " Report cần có: ■ Latency P50/P95/P99. ■ Availability/error rate. 
>  ■ Fallback success rate. ■ Cache hit rate và false-hit examples. ■ Recovery time trong chaos test."

Bốn dòng code này dạy một thứ vượt ra ngoài bài học: **chọn đúng kiểu metric**. Ba kiểu 
 Prometheus không thay thế nhau, và chọn sai làm mất thông tin không lấy lại được.

| Kiểu | Dùng khi | Ví dụ trong slide | Vì sao không dùng kiểu khác |
| --- | --- | --- | --- |
| Counter | Đại lượng chỉ tăng, đếm sự kiện | agent_requests_total, cache_hits_total | Dùng Gauge sẽ mất khả năng tính tốc độ giữa hai lần lấy mẫu |
| Histogram | Phân bố giá trị — cần phân vị | agent_latency_seconds | Dùng Gauge hay trung bình sẽ không tính được P95/P99, mà đó mới là thứ cần |
| Gauge | Đại lượng lên xuống, đọc "ngay lúc này" | circuit_state | Trạng thái breaker là ảnh chụp tức thời, không phải thứ để cộng dồn |

Trung bình che đúng thứ bạn cần thấy. Ví dụ 100 request: 95 request 200 ms, 5 request 10.000 ms. **Trung bình = 690 ms** — trông chấp nhận được. Nhưng **P95 = 10.000 ms**, và 5 người dùng đó vừa có trải nghiệm tệ.

Với hệ thống có timeout và fallback, phân phối độ trễ *luôn* có đuôi dài — đó là bản chất 
 của nó. Nên trung bình không chỉ kém thông tin mà **gây hiểu lầm có hệ thống**.

Đây cũng là lý do slide đòi **cả ba** P50/P95/P99 chứ không 
 chỉ một: P50 nói trải nghiệm điển hình, P95 nói trải nghiệm tệ, P99 nói trường hợp xấu nhất còn đáng 
 quan tâm. Chênh lệch giữa chúng chính là thông tin — P50 200 ms với P99 400 ms là một hệ ổn định; 
 P50 200 ms với P99 10.000 ms là một hệ có vấn đề ẩn.

Chú ý các nhãn: `provider`, `status`, `route`, `cache_type`. Chúng cho phép **tách nhỏ** — và tách nhỏ là toàn bộ giá trị 
 của việc đo.

Không có nhãn `provider`, bạn thấy "error rate 3%" mà không biết là Provider A hỏng 
 hay cả hai. Không có nhãn `route`, bạn không tính được fallback success rate. Không có `cache_type`, bạn không phân biệt được ba tầng cache đang hoạt động ra sao.

**Cùng bài học đã gặp ở [Ngày 24](track-3-day-24.html):** không bao giờ hành động dựa trên một con số tổng khi có thể tách nhỏ nó ra. Ở đó là tách theo nhóm 
 người dùng và loại truy vấn; ở đây là tách theo provider và route. Cùng một nguyên tắc, hai bối cảnh.

### Slide 24 Chaos testing — cố tình làm hỏng để có bằng chứng

> Trích slide 
>  " Chaos scenarios trong lab: 1. Primary provider timeout 100%. 
>  2. Primary provider intermittent 50%. 3. Cache returns stale candidate. 4. Cost cap gần cạn." 
>  " Expected evidence: ■ Circuit chuyển CLOSED → OPEN. ■ Gateway route sang 
>  fallback. ■ Không retry storm. ■ Metrics/report ghi rõ recovery time." 
>  "Mini design review - 7 phút — Mỗi nhóm viết 1 chaos scenario mới và metric chứng minh system 
>  recover. Nhóm khác phản biện: scenario đó có side effect không?"

Cột *"expected evidence"* quan trọng hơn cột scenario, và nó là lý do chaos test khác với 
 "thử nghịch xem sao": **bạn phải nói trước điều gì chứng minh hệ thống đã phục hồi**. 
 Không có tiêu chí đặt trước thì mọi kết quả đều giải thích được theo hướng có lợi.

| Scenario | Kiểm tra cái gì | Vì sao khó |
| --- | --- | --- |
| 1 · Primary timeout 100% | Breaker mở, fallback hoạt động | Dễ nhất — trạng thái rõ ràng, kết quả tiền định |
| 2 · Lỗi ngắt quãng 50% | Breaker có dao động không | Khó nhất. Breaker liên tục đóng-mở; hệ thống có thể tệ hơn cả khi provider hỏng hẳn |
| 3 · Cache trả bản cũ | TTL, invalidation, phát hiện false-hit | Không có lỗi nào xuất hiện — phải chủ động đi tìm |
| 4 · Ngân sách gần cạn | Cảnh báo 80%, hành vi ở 100% | Cần mô phỏng được đồng hồ chi tiêu, không chỉ mô phỏng lỗi |

**Vì sao scenario 2 đáng làm nhất:** lỗi 50% là tình huống *phổ biến hơn* outage toàn phần trong thực tế, và nó là tình huống duy nhất bộc lộ được việc 
 bạn chọn `failure_threshold` và `success_threshold` có hợp lý không. Ngưỡng 
 đặt quá nhạy thì breaker mở-đóng liên tục, mỗi lần đóng lại đấm một nhát vào provider đang yếu. 
 Mô hình đếm trong [mô-đun circuit breaker](#m-cb) **không** áp được cho 
 scenario này — nó cần mô phỏng ngẫu nhiên thật.

*"Nhóm khác phản biện: scenario đó có side effect không?"*

Đây là câu hỏi phân biệt chaos test an toàn với một sự cố tự gây ra. Nếu bạn ép agent thất bại ở 
 giữa một luồng **đã gọi tool có tác dụng thật** — đã trừ phòng, đã gửi email, đã ghi 
 vào cơ sở dữ liệu — thì bạn không đang test, bạn đang tạo dữ liệu rác.

Nối thẳng với **nhóm lỗi ⑥** ở [slide 8](#s8): 
 "business action sai — side effect không rollback". Chaos test phải chạy ở môi trường mà tool là 
 giả lập, hoặc phải dừng trước điểm có tác dụng thật. Đây cũng là lý do cổng approval của Ngày 23 
 hữu ích ngoài mục đích an toàn: nó cho bạn một điểm dừng tự nhiên để chèn hỗn loạn vào.

có/không

không thể quan sát từ production bình thường

reset_timeout

mô-đun

#### Ô kiểm tra — Chương 4

Trả lời thành tiếng trước khi mở đáp án.

**1.** Phân biệt SLI, SLO, SLA và error budget. Vì sao SLO nội bộ nên chặt hơn 
 SLA? Hiểu

#### Đáp án

**SLI** = một phép đo, không có ngưỡng (availability, P95 latency, cache hit rate). **SLO** = ngưỡng nội bộ đặt trên SLI (availability ≥ 99%, P95 < 2,5 s, fallback 
 success ≥ 95%). **SLA** = cam kết trong hợp đồng với khách hàng (99,5% uptime/tháng). **Error budget** = phần còn được phép hỏng của SLO.

**Cách nhớ:** hỏi ai đọc con số và hậu quả khi vi phạm. SLI — kỹ sư, không có khái 
 niệm vi phạm. SLO — đội kỹ thuật, vi phạm thì đóng băng tính năng. SLA — khách hàng và pháp lý, 
 vi phạm thì *mất tiền*.

**Vì sao SLO phải chặt hơn SLA:** khoảng đệm giữa hai con số chính là thời gian 
 bạn có để phản ứng. Nếu SLA là 99,5% mà SLO cũng đặt 99,5%, thì lần đầu tiên bạn biết mình có vấn 
 đề cũng là lần đầu tiên bạn đã vi phạm hợp đồng. Đặt SLO 99,9% cho SLA 99,5% nghĩa là bạn được 
 cảnh báo khi còn hơn 170 phút dự phòng.

**Điểm cộng:** nêu được rằng LLM agent cần thêm *quality SLO* — faithfulness, 
 safety pass rate, escalation correctness — vì ba SLO vận hành có thể xanh hết trong khi chất lượng 
 đã tệ đi (silent degradation, slide 10).

**2.** Hai hệ thống đều dùng hai provider, mỗi provider đạt 99,5%. Hệ A gọi cả 
 hai cho mỗi request (cần cả hai thành công). Hệ B dùng provider thứ hai làm fallback. So sánh 
 downtime mỗi tháng. Phân tích

#### Đáp án

**Hệ A (phụ thuộc): 0,995 × 0,995 = 99,0025% ⇒ khoảng 431 phút/tháng.** *Tệ hơn* một provider đơn lẻ (216 phút) — vì mỗi thành phần thêm vào là một điểm hỏng thêm.

**Hệ B (fallback lý tưởng): 1 − 0,005² = 99,9975% ⇒ khoảng 1 phút/tháng.** Với tỷ lệ fallback thành công thực tế 95% thì khoảng 12 phút/tháng.

**Chênh lệch khoảng 36 lần** giữa hai kiến trúc dùng *cùng hai thành phần, cùng 
 độ tin cậy*. Khác biệt duy nhất là chúng được nối theo kiểu phụ thuộc hay dự phòng.

**Vì sao:** phụ thuộc thì nhân xác suất *thành công* (cả hai phải chạy); 
 dự phòng thì nhân xác suất *thất bại* (cả hai phải hỏng), mà tích của hai số nhỏ thì rất nhỏ.

**Cảnh báo bắt buộc nêu:** phép tính giả định hai provider hỏng *độc lập*. 
 Thực tế chúng tương quan — cùng sự cố mạng khu vực, cùng hạ tầng, hoặc một prompt sai làm cả hai 
 cùng từ chối. Con số thật thấp hơn, nên hãy đọc kết quả như trần trên.

**3.** Trong bốn chaos scenario ở slide 24, scenario nào khó nhất và vì sao? 
 Nêu một điều kiện an toàn bắt buộc khi chạy chaos test. Đánh giá

#### Đáp án

**Scenario 2 — lỗi ngắt quãng 50% — khó nhất.**

Với outage toàn phần (scenario 1), breaker mở một lần và ở yên đó: trạng thái rõ ràng, kết quả 
 tiền định. Với lỗi 50%, breaker **liên tục đóng rồi mở**, và mỗi lần đóng lại là một 
 nhát đấm vào provider đang yếu. Hệ thống có thể tệ hơn cả khi provider hỏng hẳn.

Đây cũng là tình huống *phổ biến hơn* trong thực tế, và là tình huống duy nhất bộc lộ 
 được việc chọn `failure_threshold` và `success_threshold` có hợp lý không. 
 Mô hình đếm đơn giản không áp được — cần mô phỏng ngẫu nhiên thật.

**Điều kiện an toàn bắt buộc:** chaos test *không được* chạy trên đường có 
 side effect thật. Nếu ép agent thất bại giữa một luồng đã gọi tool có tác dụng — đã trừ phòng, đã 
 gửi email, đã ghi database — thì bạn không đang test mà đang tạo dữ liệu rác và có thể gây sự cố 
 thật. Đây chính là nhóm lỗi ⑥ ở slide 8: "business action sai — side effect không rollback".

**Cách làm đúng:** chạy với tool giả lập, hoặc dừng trước điểm có tác dụng thật — 
 cổng approval của Ngày 23 cho bạn sẵn một điểm dừng như vậy. Đó chính là câu phản biện mà slide 
 yêu cầu nhóm khác đặt ra: "scenario đó có side effect không?"

---

<!-- chiron-source-span: {"source_span_id":"4e5ebf41-b66e-5d67-89a4-1f1960bf7cf9","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Lab 10 — Reliability Engineering","source_file":"track-3-day-25.html"},"checksum":"b9ff6fc32e601922fdd50fceb7d0574136c143f1441277b98970809d470f753a"} -->

## 05 Lab 10 — Reliability Engineering

Slide 25–30: mục tiêu, năm mốc thời gian, metric bắt buộc, rubric và kịch bản demo.

### Slide 25–26 Lab 10 — đề bài

> Trích slide 
>  " Mục tiêu: Build reliability gateway: circuit breaker + semantic/tool cache + 
>  metrics + chaos report" 
>  " Deliverable: Repo hoàn chỉnh, metrics JSON/CSV, report Markdown/PDF, demo 
>  command chạy được" 
>  " Thời gian: 2 giờ trên lớp + 2 giờ mở rộng"

Đề bài gói gọn bốn chương lý thuyết thành một hệ thống, và bốn deliverable ánh xạ đúng bốn thứ 
 người chấm cần:

| Deliverable | Chứng minh điều gì | Chương tương ứng |
| --- | --- | --- |
| Repo hoàn chỉnh | Bạn xây được, không chỉ mô tả | 02 · 03 |
| metrics JSON/CSV | Bạn đo được — đây là phần khó làm giả | 04 |
| Report Markdown/PDF | Bạn diễn giải được số liệu | 04 |
| Demo command chạy được | Kết quả tái lập được, không phải ảnh chụp một lần may mắn | tất cả |

*"Demo command chạy được"* nghĩa là người chấm gõ **một lệnh** và nhận được 
 metric mới. Không phải mở notebook chạy từng ô, không phải làm theo tám bước trong README.

[Slide 30](#s30) gọi tên luôn: `make run-chaos` hoặc tương đương. Nếu bài 
 lab LangGraph Ngày 23 của bạn đã có `Makefile`, hãy dùng lại đúng cấu trúc đó — 
 người chấm sẽ nhận ra ngay và bạn không mất thời gian nghĩ lại quy ước.

**Vì sao nó quan trọng:** tái lập được là điều kiện để con 
 số của bạn *có nghĩa*. Một bảng metric không kèm cách tạo lại nó thì không khác gì một tuyên 
 bố — mà rubric ở [slide 28](#s28) nói thẳng: report không có metric định lượng thì không 
 đạt phần grading.

### Slide 27 Năm mốc thời gian — và cái bẫy trong bảng

> Trích slide 
>  "0–30' Setup repo, chạy tests baseline, đọc TODO → screenshot/test log 
>  30–75' Implement circuit breaker + fallback router → state transition log 
>  75–120' Implement metrics + run mini chaos test → metrics.json lần 1 
>  120–180' Implement cache + TTL/threshold tuning → cache comparison table 
>  180–240' Load test + report + rubric self-check → final report + plots/CSV " 
>  "Core pass khoảng 2 giờ cho nhóm mạnh. Stretch 2 giờ còn lại: false-hit analysis, cost simulation, 
>  report chất lượng cao, và test coverage."

Bảng này có một thông tin ẩn rất giá trị: **cache nằm ở mốc 120–180 phút, tức là *sau* vạch 2 giờ**. Nghĩa là theo chính thiết kế của giảng viên, cache thuộc phần 
 "stretch", không thuộc phần bắt buộc để qua.

Ghép mốc thời gian với trọng số rubric ở [slide 29](#s29):

| Việc | Nằm ở mốc | Điểm rubric | Kết luận |
| --- | --- | --- | --- |
| Circuit breaker + fallback | 30–75' — trong 2 giờ | 25 | Làm trước, nặng điểm nhất |
| Metrics + chaos lần 1 | 75–120' — trong 2 giờ | 20 + 20 = 40 | Làm ngay sau — hai hạng mục cộng lại nặng nhất |
| Cache + TTL | 120–180' — ngoài 2 giờ | 20 | Làm sau, nếu còn thời gian |
| Report + tests | 180–240' | 15 | Không bỏ được — xem ghi chú dưới |

**Nhận xét đáng chú ý:** metrics và chaos test cộng lại **40/100 điểm** — nhiều hơn cả circuit breaker. Nhưng chúng lại là phần dễ bị bỏ dở 
 nhất vì làm sau. Nếu bạn chỉ có 2 giờ, hãy dừng việc code sớm hơn dự định để chắc chắn có `metrics.json` — một breaker hoàn hảo không có số đo vẫn mất 40 điểm.

Mỗi mốc đều đòi một **tạo tác cụ thể**: test log, state transition log, `metrics.json`, bảng so sánh cache, report kèm biểu đồ. Đây không phải trang trí — đó là 
 cách người chấm xác minh bạn thật sự chạy chứ không phải viết ra.

**Sai lầm thường gặp:** code hết bốn giờ rồi mới ngồi viết 
 report, và lúc đó không còn state transition log của lần chạy nào cả — vì bạn đã sửa code mười lần 
 từ đó. **Lưu tạo tác ngay tại mỗi mốc**, kể cả khi nó chưa đẹp. Một `metrics.json` xấu ở phút thứ 120 có giá trị hơn một cái đẹp không tồn tại ở phút 240.

### Slide 28 Metric và report bắt buộc — slide có câu gay gắt nhất bài

> Trích slide 
>  " Metrics bắt buộc: ■ availability, error rate ■ latency P50/P95/P99 
>  ■ fallback success rate ■ circuit open count + recovery time ■ cache hit rate + estimated cost saved 
>  ■ chaos scenario pass/fail" 
>  " Report bắt buộc: ■ architecture diagram ngắn ■ config table ■ experiment setup 
>  ■ metrics table trước/sau cache ■ failure analysis ■ next steps" 
>  " Report không có metric định lượng = không đạt phần grading. "

Sáu metric bắt buộc ánh xạ một-một vào bốn chương lý thuyết. Đây là danh sách kiểm tra đáng in ra 
 và gạch từng dòng:

| Metric | Đo bằng gì | Chỉ tính được nếu có |
| --- | --- | --- |
| availability, error rate | Counter theo status | nhãn status trên mọi request |
| latency P50/P95/P99 | Histogram, không phải Gauge | chọn đúng kiểu metric từ đầu ( slide 23 ) |
| fallback success rate | Counter theo route | route reason ghi cho từng request |
| circuit open count + recovery time | Gauge circuit_state + dấu thời gian | chaos test — production không đo được recovery time |
| cache hit rate + cost saved | Counter theo cache_type + ước lượng giá | ghi estimated cost mỗi lời gọi |
| chaos scenario pass/fail | Tiêu chí đặt trước cho từng kịch bản | viết expected evidence trước khi chạy |

**`route reason`** — không có thì fallback success rate không tính được. 
 **`circuit_state`** tại thời điểm mỗi request — không có thì không chứng minh 
 được breaker đã hoạt động. 
 **`similarity score`** cho mỗi lần tra cache — không có thì không điều chỉnh 
 được ngưỡng bằng dữ liệu thật.

Cả ba đều tốn vài dòng code nếu thêm ngay từ đầu, và đều **không thể dựng lại** từ log cũ. Đây là lời khuyên có giá trị cao nhất trong cả chương 
 lab: *quyết định ghi gì vào log là quyết định bạn sẽ trả lời được câu hỏi nào ba giờ sau*.

**Về mục "metrics table trước/sau cache":** chú ý chữ *trước*. Nghĩa là bạn phải 
 chạy và lưu kết quả **khi chưa có cache** — tức là ở mốc 75–120 phút, trước khi bắt tay 
 vào cache ở mốc sau. Nếu bỏ qua bước này, đến lúc viết report bạn không còn baseline để so, và phải 
 gỡ cache ra chạy lại. Đây đúng là thứ mà thứ tự các mốc ở [slide 27](#s27) đã cài sẵn để 
 bạn không mắc phải.

nhìn ra giới hạn của chính mình

Slide 30

"giải thích 1 failure mode còn tồn tại"

"Breaker dùng state trong bộ nhớ, 
 nên với nhiều instance thì số lời gọi lọt qua nhân lên theo số instance"

"chưa xử lý được scenario lỗi ngắt quãng 50% — breaker dao động, cần điều chỉnh 
 success_threshold"

### Slide 29 Rubric tổng quan

> Trích slide 
>  " Circuit breaker/fallback — 25 — state machine đúng, không retry storm, fallback 
>  có route reason 
>  Cache/cost — 20 — hit rate/cost saved rõ, TTL/threshold có giải thích, false-hit examples 
>  Observability/metrics — 20 — P50/P95/P99, availability, circuit state, cache metrics 
>  reproducible 
>  Chaos/load test — 20 — ít nhất 3 scenarios, có recovery evidence 
>  Report/code quality — 15 — README rõ, tests, type hints, config, report dễ chấm"

Đọc rubric theo *động từ* thay vì theo hạng mục sẽ thấy tiêu chí thật:

**① "không retry storm"** (25 điểm) — người chấm sẽ tìm bằng chứng rằng số lời gọi 
 tới provider hỏng *không* tăng vọt. Đây là lý do bạn cần log số lời gọi theo thời gian, không 
 chỉ log trạng thái breaker.

**② "fallback có route reason"** — nhắc lại lần thứ ba trong bài. Nếu chỉ nhớ một 
 chi tiết triển khai từ cả bài học, nhớ cái này.

**③ "TTL/threshold có giải thích"** (20 điểm) — không phải "có TTL" mà là *giải thích vì sao chọn giá trị đó*. Một câu như *"TTL 300 giây vì chính sách khách sạn 
 cập nhật theo ca, và một ca là 8 giờ nên 5 phút là đủ tươi"* ăn điểm hơn hẳn một con số trần trụi.

**④ "cache metrics reproducible"** (20 điểm) — chạy lại phải ra kết quả tương đương. 
 Nghĩa là bộ truy vấn test phải cố định và lưu trong repo, không phải gõ tay lúc demo.

"README rõ, tests, type hints, config, report dễ chấm"

ruff

### Slide 30 Kịch bản demo cuối buổi

> Trích slide 
>  "1. Chạy một command tạo metrics: make run-chaos hoặc tương đương. 
>  2. Chỉ ra breaker chuyển state khi primary fail. 
>  3. So sánh latency/cost có cache và không cache. 
>  4. Mở report và giải thích 1 failure mode còn tồn tại. 
>  5. Nêu 1 config bạn sẽ đổi nếu deploy production."

Năm bước này là một bài kiểm tra vấn đáp trá hình, và **hai bước cuối mới là phần chấm 
 thật** — ba bước đầu chỉ xác nhận hệ thống chạy.

**Bước 4 — "một failure mode còn tồn tại".** Đây là câu hỏi về sự trung thực kỹ 
 thuật. Ba câu trả lời tốt, chọn cái đúng với bài của bạn:

• *"Breaker giữ state trong bộ nhớ. Với N instance thì mỗi instance phải tự học riêng, nên số 
 lời gọi lọt qua nhân lên khoảng N lần. Sửa bằng backend Redis chung."* 
 • *"Chưa xử lý được scenario lỗi ngắt quãng 50% — breaker đóng-mở liên tục. Cần nâng `success_threshold` và thêm cơ chế giãn thời gian chờ."* 
 • *"Semantic cache chưa có định danh người dùng trong khoá, nên chưa an toàn cho truy vấn chạm 
 dữ liệu cá nhân. Hiện tôi giới hạn bằng allowlist."*

**Bước 5 — "một config sẽ đổi khi lên production".** Câu này 
 kiểm tra bạn có phân biệt được môi trường lab với môi trường thật không. Câu trả lời tốt phải có *lý do định lượng*:

• *"Trong lab tôi đặt `reset_timeout` = 5 giây để thấy 
 chuyển trạng thái nhanh khi demo. Lên production tôi đổi thành 30–60 giây, vì ở 5 giây thì với 
 outage 5 phút sẽ có 60 lần thăm dò vô ích thay vì 10."* 
 • *"Ngưỡng tương đồng cache trong lab là 0,80 để hit rate trông đẹp. Production tôi nâng lên và 
 thu hẹp allowlist, vì false-hit tốn đắt hơn nhiều so với một lần miss."*

"So sánh latency/cost có cache và không cache"

trước khi

slide 28

metrics_before_cache.json

---

<!-- chiron-source-span: {"source_span_id":"751d730b-340d-5bfa-a52a-c17c56649701","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Tổng kết","source_file":"track-3-day-25.html"},"checksum":"d6b40d0f69b7815db2abc6675117a667a86db02aec52dd96f0815ad0400a5ebd"} -->

## 06 Tổng kết

Slide 31–34: bốn ý chốt và danh mục tài liệu.

### Slide 31–32 Bốn ý chốt

> Trích slide 
>  "Reliability engineering giúp agent fail gracefully, đo được, và có thể cải thiện bằng dữ liệu." 
>  "1 Circuit breaker + fallback là minimum viable reliability cho agent production. 
>  2 Cache có ROI cao nhưng cần guardrail: TTL, threshold, invalidation, false-hit tracking. 
>  3 Metrics phải bao phủ latency, availability, cost, cache, circuit state và quality. 
>  4 Chaos/load test biến giả định thành bằng chứng; report định lượng giúp chấm điểm 
>  công bằng."

Bốn ý này đọc như một danh sách, nhưng chúng có quan hệ thứ bậc rõ ràng — và nhận ra thứ bậc đó là 
 cách hiểu bài sâu nhất:

```text
①  Circuit breaker + fallback     ← nền móng. Không có thì các thứ khác vô nghĩa
        │
        ▼
②  Cache                          ← tối ưu. Chỉ làm SAU khi hệ thống đã đứng vững
        │                              (và bản thân nó tạo ra kiểu hỏng mới)
        ▼
③  Metrics                        ← lớp nhìn. Không đo thì không biết ① và ② có chạy không
        │
        ▼
④  Chaos test                     ← lớp chứng minh. Biến "tôi nghĩ nó chạy" thành "tôi đã thấy nó chạy"
```

Đây là câu đáng mang ra khỏi bài học nhất, và nó đúng vượt ra ngoài phạm vi reliability.

Bạn *viết* circuit breaker. Bạn *tin* nó hoạt động — code trông đúng, test đơn vị 
 xanh. Nhưng cho tới khi bạn cố tình làm provider chết và *quan sát* breaker chuyển trạng 
 thái, đó vẫn chỉ là một giả định.

Khoảng cách giữa hai trạng thái đó lớn hơn nhiều người tưởng, vì **đường xử lý lỗi là đường ít được chạy nhất**. Code chạy hàng triệu lần mỗi ngày thì 
 lỗi lộ ra ngay. Code chỉ chạy khi provider chết có thể sai suốt sáu tháng mà không ai biết — cho tới 
 đúng ngày bạn cần nó.

nhưng

liên tục

### Slide 33–34 Danh mục tài liệu

> Trích slide 
>  "1. Microsoft Azure Architecture Center: Circuit Breaker pattern. 
>  2. Release It! Design and Deploy Production-Ready Software, Michael Nygard. 
>  3. Prometheus client Python: Counter, Gauge, Histogram docs. 
>  4. LiteLLM documentation: routing, retries, fallbacks. 
>  5. Langfuse documentation: LLM observability, traces, cost and latency metrics."

Danh mục này chia làm hai nhóm rõ rệt, và tỷ lệ giữa chúng là một thông điệp:

| Nhóm | Tài liệu | Nói lên điều gì |
| --- | --- | --- |
| Mẫu hình chung, có trước LLM | Azure Circuit Breaker pattern · Release It! (2007) · Prometheus | Ba trong năm nguồn không liên quan gì tới LLM. Reliability engineering là ngành đã trưởng thành; bạn đang mượn, không phát minh |
| Công cụ riêng cho LLM | LiteLLM (định tuyến, fallback) · Langfuse (quan sát, chi phí, độ trễ) | Phần đặc thù chỉ là lớp áp dụng — routing đa nhà cung cấp và theo dõi chi phí theo token |

*Release It!* xuất bản **2007** — trước GPT-3 mười ba năm. Circuit breaker, 
 bulkhead, timeout, fail fast đều được mô tả trong đó, cho hệ thống Java doanh nghiệp gọi web service.

Điều đó nghĩa là: **bài học hôm nay gần như không có gì mới về mặt khái niệm**. Cái 
 mới chỉ là *chúng chưa được áp cho lời gọi model* — và lý do rất đơn giản: hầu hết người xây 
 ứng dụng LLM đến từ nền tảng khoa học dữ liệu, không phải kỹ thuật hệ thống phân tán.

Nên nếu bạn thấy chương này dễ hơn các chương trước, đó không phải ảo 
 giác. Và nếu bạn muốn đào sâu hơn giáo trình, hai nguồn đầu tiên trong danh mục cho bạn nhiều hơn 
 bất kỳ tài liệu LLM nào.

#### Ô kiểm tra — Chương 5 & 6

Trả lời thành tiếng trước khi mở đáp án.

**1.** Bạn chỉ có 2 giờ cho lab 4 giờ. Ưu tiên làm gì và bỏ gì? 
 Lập luận bằng rubric. Đánh giá

#### Đáp án

**Làm: circuit breaker + fallback (25đ), rồi metrics (20đ) + chaos test (20đ). 
 Bỏ hoặc làm tối giản: cache (20đ).**

**Lập luận:** chính bảng mốc thời gian ở slide 27 đã sắp sẵn — cache nằm ở mốc 
 120–180 phút, tức *sau* vạch 2 giờ, nên nó thuộc phần stretch theo thiết kế của giảng viên.

**Điểm quan trọng hơn:** metrics + chaos cộng lại là **40/100 điểm**, 
 nhiều hơn cả circuit breaker. Nhưng chúng làm sau nên hay bị bỏ dở. Một breaker hoàn hảo không có `metrics.json` vẫn mất 40 điểm — nên phải dừng code sớm hơn dự định để chắc chắn có số 
 đo.

**Đừng bỏ hạng mục 15 điểm cuối** (README, tests, type hints, config): nó không 
 cần hiểu biết sâu, chỉ cần kỷ luật, và tốn khoảng 20 phút. Đây là 15 điểm rẻ nhất trong rubric.

**Và lưu tạo tác tại mỗi mốc** — một `metrics.json` xấu ở phút 120 có 
 giá trị hơn một cái đẹp không tồn tại ở phút 240.

**2.** Ở bước 5 của demo, bạn phải nêu một config sẽ đổi khi lên production. 
 Cho một câu trả lời có lý do định lượng. Áp dụng

#### Đáp án

**Ví dụ tốt:** *"Trong lab tôi đặt `reset_timeout` = 5 giây để demo 
 thấy chuyển trạng thái nhanh. Lên production tôi đổi thành 30–60 giây, vì với outage 5 phút thì ở 
 5 giây sẽ có 60 lần thăm dò vô ích, còn ở 30 giây chỉ có 10 — mỗi lần thăm dò là một request thật 
 đâm vào provider đang hỏng."*

Kiểm chứng bằng [mô-đun circuit breaker](#m-cb): giữ nguyên outage 300 giây và kéo `reset_timeout` để thấy đúng hai con số đó.

**Ví dụ tốt khác:** *"Ngưỡng tương đồng cache trong lab là 0,80 để hit rate 
 trông đẹp. Production tôi nâng ngưỡng và thu hẹp allowlist, vì ở 3.000 lượt/ngày với false-hit 2% 
 thì mỗi ngày có 24 người nhận câu trả lời của người khác, trong khi tiền tiết kiệm chỉ khoảng 
 $2,40/ngày — tức 10 xu cho mỗi câu sai."*

**Điều làm câu trả lời đạt điểm:** có con số, có đánh đổi hai chiều, và phân biệt 
 được *mục tiêu của lab* (thấy rõ hành vi khi demo) với *mục tiêu của production* (giảm thiệt hại thật).

**3.** Ba trong năm tài liệu tham khảo không liên quan gì tới LLM. Điều đó nói 
 lên gì về bài học này? Đánh giá

#### Đáp án

**Rằng reliability engineering là một ngành đã trưởng thành, và bài này chủ yếu là *mượn* chứ không phát minh.**

*Release It!* xuất bản 2007 — trước GPT-3 mười ba năm — và đã mô tả đầy đủ circuit 
 breaker, bulkhead, timeout, fail fast cho hệ thống doanh nghiệp gọi web service. Azure Circuit 
 Breaker pattern và Prometheus cũng không dính gì tới LLM.

**Phần đặc thù LLM chỉ là lớp áp dụng:** LiteLLM (định tuyến và fallback giữa các 
 nhà cung cấp model) và Langfuse (theo dõi chi phí theo token, độ trễ, trace).

**Vì sao các mẫu này chưa phổ biến trong ứng dụng LLM:** phần lớn người xây ứng 
 dụng LLM đến từ nền khoa học dữ liệu chứ không phải kỹ thuật hệ thống phân tán — nên khoảng trống 
 không nằm ở kỹ thuật mà ở việc *biết những mẫu này tồn tại*.

**Hệ quả thực hành:** muốn đào sâu hơn giáo trình thì hai nguồn đầu cho nhiều hơn 
 bất kỳ tài liệu LLM nào. Và khi thiết kế hệ thống, hãy hỏi "vấn đề này đã được giải trong kỹ thuật 
 hệ thống chưa" trước khi nghĩ đây là vấn đề mới của AI.

---

<!-- chiron-source-span: {"source_span_id":"0d8a5ee7-03ae-543c-80b6-ee5678809873","locator":{"kind":"html_section","section_id":"ladder","order":9,"heading":"▤ Luyện kỹ năng cốt lõi: chẩn đoán và thiết kế phòng thủ","source_file":"track-3-day-25.html"},"checksum":"33c83005ee2ae846687a4d6d0185efbea9e9707201d9afb43f9b431078717991"} -->

## ▤ Luyện kỹ năng cốt lõi: chẩn đoán và thiết kế phòng thủ

Ba bài giảm dần giàn giáo. Làm đúng thứ tự.

① Lỗi này thuộc nhóm nào trong sáu nhóm?

② Contain bằng gì?

③ Isolate và recover thế nào?

④ Metric nào chứng minh nó hoạt động?

slide 29

#### Chatbot hỗ trợ khách hàng: provider chính timeout ngẫu nhiên, người dùng phàn nàn "quay mãi rồi báo lỗi"

Đọc cách *lập luận*, không chỉ đáp án.

1. Nhóm ① provider transient, đang trên đường thành nhóm ③. Timeout ngẫu nhiên là 
 lỗi thoáng qua ở phía provider. Nhưng triệu chứng người dùng mô tả — "quay mãi rồi báo lỗi" — cho 
 biết hệ thống đang retry và mỗi lần retry đều chờ hết timeout. 
 Cách nhận ra: nếu thời gian chờ của người dùng là bội số của timeout (30 s, 60 s, 90 s), 
 gần như chắc chắn đó là retry nối tiếp.
2. Contain: circuit breaker + timeout ngắn hơn. Đặt breaker cho riêng provider này 
 với failure_threshold khoảng 5. Khi mở, người dùng nhận phản hồi ở 
 0 ms thay vì chờ ba lần timeout. Quan trọng: chỉ tính timeout và 5xx là failure — 
 không tính lỗi 4xx ( slide 13 ), nếu không một đợt request sai định dạng sẽ tự mở 
 breaker và gây outage.
3. Isolate: breaker riêng theo (provider, model). Provider A mở không 
 được kéo provider B theo. Recover: HALF-OPEN với reset_timeout 30 giây 
 — thả một request thăm dò, không thả cả hàng đợi. 
 Fallback: đây là hỗ trợ khách hàng nên tụt bậc được đủ 5 nấc 
 ( slide 15 ) — provider B, rồi model rẻ hơn, rồi cache, cuối cùng là thông báo tĩnh 
 kèm nút gọi người thật.
4. Chỉ số theo dõi: ① circuit_state theo provider — phải thấy 
 CLOSED → OPEN khi sự cố; ② số lời gọi tới provider hỏng theo thời gian — nếu không 
 giảm mạnh thì breaker chưa hoạt động; ③ fallback success rate, mục tiêu ≥ 95%; 
 ④ P95 latency — kỳ vọng giảm trong lúc sự cố, vì fail nhanh nhanh hơn fail chậm.

giảm

#### Sau khi bật semantic cache, hoá đơn giảm 35% và P95 latency giảm một nửa. Ba tuần sau, đội hỗ trợ báo có khách phàn nàn "bot trả lời về phòng của người khác"

Hai bước đầu cho sẵn. Hai bước sau tự viết rồi mới mở.

1. Nhóm ⑤ tool/cache failure, biến thể nguy hiểm nhất. Không phải stale — stale là 
 trả dữ liệu cũ của đúng người. Đây là trả dữ liệu của người khác, tức false-hit ở 
 semantic cache ( slide 18 ).
2. Vì sao không ai phát hiện trong ba tuần: false-hit không tạo ra lỗi nào. Mã 
 trạng thái 200, không exception, và độ trễ còn tốt hơn bình thường vì không phải gọi LLM. 
 Mọi chỉ số vận hành đều xanh — đây đúng là silent degradation ở slide 10, do chính 
 đội tạo ra khi thêm cache.
3. ③ Hai việc phải làm ngay hôm nay, và một việc làm trong tuần? 
 (gợi ý: cái nào chặn được thiệt hại ngay, cái nào cần đo mới quyết được)
4. ④ Metric nào lẽ ra đã bắt được chuyện này từ tuần đầu? 
 (gợi ý: slide 18 nêu hai metric, đội này chỉ theo dõi một)

#### Đáp án hai bước còn lại

**③ Ngay hôm nay — hai việc:**

• **Thu hẹp allowlist:** loại toàn bộ truy vấn chạm dữ liệu riêng của khách (đặt 
 phòng, thanh toán, số phòng) khỏi semantic cache. Đây là *chặn thiệt hại*, làm được trong vài 
 phút, và không cần đo gì trước. Đúng dòng "Account balance — không cache response" ở [slide 20](#s20). 
 • **Thêm định danh người dùng vào khoá cache** cho mọi truy vấn còn lại có yếu tố cá 
 nhân. Hai việc này chồng lên nhau có chủ ý — allowlist là hàng rào chính, khoá cache là lưới an toàn.

**Trong tuần:** đo false-hit rate thật bằng cách lấy mẫu các lần trúng cache và đối 
 chiếu với câu trả lời sinh mới. Chỉ sau khi có con số mới nên chỉnh ngưỡng tương đồng — chỉnh trước 
 khi đo là đoán mò.

**④ Metric bị thiếu: false-hit rate.** Slide 18 viết rõ *"Metric quan trọng: hit rate **và** false-hit rate"*. Đội này chỉ theo dõi hit 
 rate — và hit rate là metric *luôn trông đẹp lên* khi bạn nới lỏng cache, nên nó một mình 
 không bao giờ báo động.

**Kèm theo, hai thứ nên có:** ghi `similarity score` cho mỗi lần trúng 
 (không có nó thì không hiệu chỉnh được ngưỡng bằng dữ liệu thật), và lưu *ví dụ* false-hit 
 chứ không chỉ con số — rubric [slide 29](#s29) đòi đúng chữ "false-hit examples".

**Điểm đáng nói thêm:** đây không chỉ là lỗi chất lượng. Trả dữ liệu đặt phòng của 
 khách này cho khách khác là *sự cố lộ dữ liệu cá nhân*, thuộc trục Compliance mà [Ngày 24](track-3-day-24.html) mô tả — nên nó cần được xử lý theo quy trình sự cố, không 
 chỉ là một ticket kỹ thuật.

#### Thiết kế lớp reliability cho kiosk check-in SmartCheck AI

Không có gợi ý. Viết ra bốn câu trả lời rồi so với [mục áp dụng](#apply).

1. Bối cảnh: kiosk đặt ở sảnh khách sạn, khách đứng trước màn hình chờ. 
 Khoảng 300 lượt check-in mỗi ngày, mỗi lượt vài lượt hội thoại. Agent LangGraph có các node phân 
 loại, định tuyến, gọi tool, cổng phê duyệt, và finalize. Hiện dùng một nhà cung cấp 
 model duy nhất, không có breaker, không có cache, không có trần chi phí.
2. Câu hỏi ①: liệt kê các nhóm lỗi trong sáu nhóm mà hệ này đã có phòng 
 thủ, và các nhóm còn trống.
3. Câu hỏi ②–③: thiết kế thang fallback. Chú ý một ràng buộc đặc thù — khách 
 đang đứng đợi, nên định nghĩa "chấp nhận được" ở đây khác với một chatbot web.
4. Câu hỏi ④: chọn ba metric bạn sẽ log đầu tiên, và nói rõ mỗi metric trả lời 
 được câu hỏi nào mà bạn hiện không trả lời được.

bậc 5 của thang fallback không phải là thất bại

hoàn toàn chấp nhận được

có người thật đứng cách đó mười 
 mét

---

<!-- chiron-source-span: {"source_span_id":"fc51fed9-1afa-5234-b1ab-07a829a50de5","locator":{"kind":"html_section","section_id":"misc","order":10,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"track-3-day-25.html"},"checksum":"2b1a274a45dcb81ac9198ad9fa380851919a2d271d7218632c7d7108c9166b5c"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Mỗi thẻ: niềm tin phổ biến, lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng.

*Vì sao nghe hợp lý:* retry đúng là cơ chế phòng thủ đầu tiên ai cũng nghĩ tới, và nó *có* hiệu quả với lỗi mạng thoáng qua. Thư viện nào cũng có sẵn một decorator retry.

Retry giả định lỗi **độc lập và ngẫu nhiên**. Khi nguyên nhân là provider quá tải, 
 giả định đó sai hoàn toàn — retry không phải "thử lại" mà là *đổ thêm tải*.

Chuỗi ở [slide 9](#s9): provider timeout → retry 3 lần → quota cạn → workflow outage. 
 Đây là vòng phản hồi dương, và nó mạnh nhất đúng lúc hệ thống yếu nhất.

[Slide 9](#s9) nguyên văn: *"Retry chỉ là bước đầu"* · [Mô-đun circuit breaker](#m-cb) — so 600 lời gọi với 15.

*Vì sao nghe hợp lý:* với mọi hệ thống phần mềm khác thì đúng. API hoặc trả đúng dữ liệu, 
 hoặc trả lỗi — không có trạng thái thứ ba.

LLM **luôn** trả về câu trả lời trông hợp lệ. Có một trạng thái thứ ba: *thành công về kỹ thuật, thất bại về nội dung*. Mã 200, độ trễ bình thường, không exception — 
 trong khi faithfulness đã giảm dần.

Đây là lý do [slide 22](#s22) đòi **quality SLO** bên cạnh uptime SLO: 
 faithfulness, safety pass rate, escalation correctness.

[Slide 10](#s10) — biểu đồ "error rate = 0%" đi cùng "faithfulness giảm dần" · [Ngày 24](track-3-day-24.html) — bốn nguồn trôi dạt.

*Vì sao nghe hợp lý:* hit rate cao nghĩa là tiết kiệm nhiều, nhanh hơn, ít gọi API hơn. 
 Mọi hệ thống cache truyền thống đều tối ưu đúng chỉ số này.

Với *semantic* cache, hit rate là metric **luôn trông đẹp lên khi bạn làm hỏng hệ 
 thống**. Hạ ngưỡng tương đồng ⇒ hit rate tăng **và** false-hit rate tăng, cùng 
 chiều.

Cache truyền thống khoá bằng *khớp chính xác* nên không có khái niệm trúng nhầm. Semantic 
 cache khoá bằng "gần giống", mà gần giống không phải cùng ý.

[Slide 18](#s18) — *"Metric quan trọng: hit rate và false-hit rate"* · [mô-đun cache](#m-cache) — giá của mỗi câu trả lời sai.

*Vì sao nghe hợp lý:* nhiều đường đi hơn thì ít có khả năng tắc hết. Và với fallback thì 
 đúng là như vậy — rất mạnh.

Chỉ đúng khi hai provider được nối theo kiểu **dự phòng**. Nếu request phải đi qua *cả hai* mới thành công (phụ thuộc), độ tin cậy **giảm**: 
 0,995 × 0,995 = 99,0025%, tức *tệ hơn* một provider đơn lẻ.

Cùng hai thành phần, cùng độ tin cậy, chênh nhau khoảng **36 lần** về downtime. 
 Và cả hai con số đều giả định các provider hỏng *độc lập* — thực tế chúng tương quan.

[Mô-đun SLO](#m-slo) — cột "hai provider phụ thuộc" so với "fallback chain" · 
 mục giả định của mô-đun về tính độc lập.

*Vì sao nghe hợp lý:* bắt rộng nghe như phòng thủ kỹ hơn. Và đoạn code mẫu ở [slide 13](#s13) viết đúng `except Exception`.

Bắt quá rộng làm breaker **tự gây ra outage**. Một đợt request sai schema (400) hoặc 
 sai API key (401) sẽ đẩy breaker sang OPEN, và từ đó *traffic hợp lệ cũng bị chặn* — dù 
 provider hoàn toàn khoẻ.

Chỉ lỗi *của provider* mới được tính: timeout, 5xx, và 429 (nên có breaker riêng). Lỗi 
 4xx do client, lỗi cấu hình, và quyết định của guardrail đều không phải failure. Slide liệt kê 
 "exception nào được tính là failure" là tham số thứ tư — tham số duy nhất không có trong code.

[Slide 13](#s13) — bốn tham số chính · bảng phân loại ngoại lệ ở cùng mục.

*Vì sao nghe hợp lý:* về mặt code thì đúng là đổi một tham số `model=`. Các 
 thư viện định tuyến như LiteLLM làm cho nó trông như một dòng cấu hình.

[Slide 14](#s14) nói thẳng: cần kiểm **tương thích tính năng** — JSON 
 mode, tool calling, context length, latency/cost, policy behavior.

Nếu agent dựa vào structured output mà model dự phòng không hỗ trợ JSON mode, fallback sẽ *tạo ra một sự cố mới ngay giữa lúc đang có sự cố* — đúng lúc khó chẩn đoán nhất. Và vì đường 
 fallback ít khi chạy, nó có thể sai suốt sáu tháng mà không ai biết.

[Hình 3](#f3) — hộp "kiểm 5 thứ trước mỗi lần tụt bậc" · [Slide 24](#s24) chaos scenario 1 — bằng chứng phải là fallback *thành công*, 
 không chỉ được gọi.

---

<!-- chiron-source-span: {"source_span_id":"7e1b4b8e-735a-5219-a5c5-964b7f06b0e8","locator":{"kind":"html_section","section_id":"apply","order":11,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"track-3-day-25.html"},"checksum":"b6c1df1b1538c7848c4e7f81f6fd884d1e1fdc7a5a20668e9713c9b877a857d5"} -->

## ◆ Áp dụng vào SmartCheck AI

Đây là bài học áp dụng được trực tiếp nhất trong cả Track 3 — và có một việc nên làm ngay tuần này.

Kiosk check-in có một đặc điểm khiến bài học hôm nay khẩn thiết hơn hẳn so với một chatbot web: **khách đang đứng trước màn hình**. Không có tab khác để chuyển sang, không có thông báo 
 đẩy để nhận sau. Mọi giây chờ là một giây có người thật đứng nhìn một vòng xoay.

### Bước 1 — Sáu nhóm lỗi, hệ hiện tại đứng ở đâu

| Nhóm lỗi | Đã có phòng thủ? | Từ đâu |
| --- | --- | --- |
| ① Provider transient | ✕ trống | Không có breaker, không rõ có timeout tường minh không |
| ② Degraded latency | ✕ trống | Không đo P95, nên không phát hiện được |
| ③ Full outage | ✕ trống | Một nhà cung cấp duy nhất — provider chết là kiosk chết |
| ④ Orchestration loop | ✓ đã có | Bounded retry với bộ đếm trong state + nhánh dead-letter (Ngày 23) |
| ⑤ Tool/cache failure | — chưa áp dụng | Chưa có cache; tool failure chưa rõ được xử lý thế nào |
| ⑥ Business action sai | ✓ đã có | Cổng approval đặt trước mọi hành động rủi ro (Ngày 23) |

**Đọc bảng này theo hướng tích cực:** hai nhóm khó nhất về mặt 
 thiết kế — vòng lặp điều phối và side effect không rollback — *đã xong* từ bài lab trước. Ba 
 nhóm còn trống đều ở phía provider, và cả ba dùng chung một bộ công cụ: timeout, circuit breaker, 
 fallback chain. Nghĩa là khoảng trống lớn nhưng **tập trung ở một chỗ**.

### Bước 2 — Điểm hỏng đơn, và vì sao nó nghiêm trọng hơn với kiosk

Slide 72 của [Ngày 24](track-3-day-24.html) đặt sẵn câu hỏi chuẩn bị cho bài này: *"agent của bạn có 1 single point of failure nào không? Provider down = system down?"*

Với SmartCheck AI hiện tại, câu trả lời là **có**. Một khoá API, một nhà cung cấp. 
 Nếu nhà cung cấp gặp sự cố khu vực, mọi kiosk ngừng hoạt động cùng lúc.

Giả sử nhà cung cấp đạt **99,5%** — con số hợp lý cho một API thương mại. Đó là **216 phút mỗi tháng**, khoảng 3,6 giờ.

Với 300 lượt check-in mỗi ngày phân bố không đều (dồn vào giờ nhận phòng buổi chiều), 
 3,6 giờ mất dịch vụ *rơi vào giờ cao điểm* có thể ảnh hưởng vài chục khách. Và mỗi khách bị 
 ảnh hưởng đều quay sang quầy lễ tân — tức là kiosk không chỉ ngừng giúp, nó **chuyển tải sang đúng chỗ nó sinh ra để giảm tải**.

**Thêm một nhà cung cấp dự phòng**, với tỷ lệ fallback thành 
 công 95%, đưa con số đó xuống khoảng **12 phút mỗi tháng** — giảm khoảng 18 lần. Đây là 
 thay đổi kiến trúc lớn nhất về giá trị trên mỗi giờ công trong toàn bộ danh sách việc. *(Nhắc lại cảnh báo ở mô-đun: phép tính giả định hai nhà cung cấp hỏng độc lập; thực tế có tương 
 quan nên hãy đọc đây là trần trên.)*

### Bước 3 — Thang fallback cho kiosk, và vì sao nó chỉ có bốn bậc

| Bậc | Làm gì | Điều kiện chuyển | Khách thấy gì |
| --- | --- | --- | --- |
| 1 | Model chính | mặc định | Trả lời bình thường |
| 2 | Nhà cung cấp thứ hai, cùng năng lực | breaker của provider 1 ở OPEN | Không nhận ra khác biệt |
| 3 | Cache — chỉ cho nhóm câu hỏi chung | cả hai provider OPEN, và câu hỏi nằm trong allowlist | Trả lời tức thì; nếu là thông tin có thể cũ thì kèm dòng ghi chú |
| 4 | Màn hình tĩnh + nút gọi lễ tân | mọi thứ khác thất bại | "Hệ thống đang bận — bấm để gọi lễ tân" |

Node phân loại của SmartCheck AI dùng **structured output** — nó phải trả về JSON 
 đúng schema để định tuyến hoạt động. Đây chính là bẫy tương thích tính năng ở [slide 14](#s14): một model nhỏ hơn không đảm bảo JSON mode sẽ làm vỡ luồng định tuyến, 
 và vỡ *đúng lúc đang có sự cố*.

Có thể thêm bậc này về sau, nhưng chỉ khi đã *test được* rằng model nhỏ giữ đúng schema. 
 Cho tới lúc đó, bỏ nó đi là lựa chọn đúng — một bậc fallback chưa được kiểm chứng còn tệ hơn không có 
 bậc đó.

**Và bậc 4 ở đây không phải đường cùng.** Với kiosk khách 
 sạn, "gọi lễ tân" là một lối thoát *tử tế* vì có người thật đứng cách đó mười mét. Ở nhiều sản 
 phẩm khác, thông báo tĩnh là thất bại hoàn toàn; ở đây nó là một trải nghiệm chấp nhận được — và tốt 
 hơn nhiều so với vòng xoay 90 giây.

### Bước 4 — Cache: allowlist hẹp, giá trị vẫn lớn

Áp [bảng slide 20](#s20) cho các loại câu hỏi thật ở kiosk:

| Loại câu hỏi | Quyết định | Cấu hình |
| --- | --- | --- |
| Giờ ăn sáng · mật khẩu wifi · giờ trả phòng · hồ bơi mở lúc nào | Cache semantic | TTL dài (giờ); đây là nhóm chiếm phần lớn lưu lượng |
| Chính sách huỷ phòng · quy định thú cưng | Cache + xoá theo sự kiện | Hook vào lúc cập nhật chính sách; TTL một mình không đủ |
| Còn phòng trống không | Tool cache TTL rất ngắn | 10–30 giây; nhiều khách hỏi cùng lúc nên vẫn có tác dụng |
| Đặt phòng của tôi · đã thanh toán chưa · số phòng tôi | ✕ Không cache | Dữ liệu riêng từng khách — trúng nhầm là lộ thông tin khách khác |

**Nhận xét quan trọng:** allowlist chỉ có ba nhóm, nhưng nhóm 
 đầu tiên có lẽ chiếm phần lớn lưu lượng của một kiosk khách sạn. *Bạn không cần cache mọi thứ để 
 tiết kiệm được nhiều* — chỉ cần cache đúng nhóm phổ biến nhất và an toàn nhất. Đây là lập luận 
 ngược lại với bản năng tối ưu hoá thông thường, và nó đúng.

### Bước 5 — Việc nên làm ngay, xếp theo giá trị trên mỗi giờ công

| # | Việc | Công sức | Đổi lại |
| --- | --- | --- | --- |
| 1 | Log ba trường: route reason, circuit_state, độ trễ mỗi lời gọi | ~1 giờ | Không có ba trường này thì mọi việc sau đều không đo được. Và chúng không khôi phục được từ log cũ |
| 2 | Đặt timeout tường minh cho mọi lời gọi model | ~30 phút | Chặn kịch bản tệ nhất: khách đứng chờ vô hạn |
| 3 | Bậc 4 của thang: màn hình tĩnh + nút gọi lễ tân | ~2 giờ | Biến "kiosk treo" thành "kiosk chỉ đường". Làm được trước khi có provider thứ hai |
| 4 | Circuit breaker cho provider hiện tại | ~3 giờ | Fail nhanh thay vì fail chậm; chuẩn bị sẵn chỗ cắm cho bậc 2 |
| 5 | Nhà cung cấp thứ hai + router fallback | ~1 ngày | Giảm downtime khoảng 18 lần — thay đổi lớn nhất về giá trị |
| 6 | Semantic cache cho nhóm câu hỏi chung | ~1 ngày | Giảm chi phí và độ trễ; nhưng chỉ sau khi 1–5 xong |

Ghi log không sửa được lỗi nào. Nhưng nó là điều kiện để bạn *biết* mình có lỗi gì, và để 
 chứng minh các việc 2–6 có tác dụng.

Cụ thể hơn: nếu không có `circuit_state` ghi theo từng 
 request, bạn **không thể chứng minh** breaker đã hoạt động khi sự cố xảy ra — và đó 
 chính là bằng chứng mà [chaos test](#s24) đòi, cũng là thứ rubric [slide 29](#s29) chấm. Một giờ bỏ ra hôm nay giữ lại khả năng trả lời mọi câu hỏi về sau.

bậc 4 rẻ hơn năm lần và có tác dụng ngay cả khi mọi thứ khác thất bại

đáy

làm cho trường hợp xấu nhất trở nên tử 
 tế, trước khi làm cho nó trở nên hiếm.

---

<!-- chiron-source-span: {"source_span_id":"187f1c4b-4dba-5ced-8aea-6c600d70c18f","locator":{"kind":"html_section","section_id":"numbers","order":12,"heading":"! Con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"track-3-day-25.html"},"checksum":"1f6b714e21d6cf8f5b9f687ae135a6e1e9ea519ff9672260ce78875eb0aa57bb"} -->

## ! Con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài này ít con số hơn các bài khác, và phần lớn là *ví dụ cấu hình* chứ không 
 phải kết quả đo. Phân biệt hai loại đó là việc quan trọng.

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| SLO ví dụ: availability ≥ 99%, P95 < 2,5 s, fallback success ≥ 95% | 22 | Ví dụ cho lab, không có nguồn | Dùng làm điểm khởi đầu. SLO thật phải suy ra từ hậu quả kinh doanh của việc vi phạm, không chép từ slide |
| SLA ví dụ: 99,5% uptime/tháng | 22 | Ví dụ minh hoạ | Chú ý slide đặt SLO (99%) thấp hơn SLA (99,5%) vì hai đối tượng khác nhau. Thực hành chuẩn thì SLO nội bộ phải chặt hơn SLA |
| Ngân sách: cảnh báo 80%, dừng ở 100% | 19 | Quy ước phổ biến, không có nguồn | Dùng được. Nhưng phải quyết định trước: ở 100% là hard stop hay route cheap — hai lựa chọn rất khác nhau |
| Chaos scenario 2: lỗi ngắt quãng 50% | 24 | Tham số kịch bản test | Là mức để thử, không phải mức quan sát được ở đâu. Chọn tỷ lệ theo lỗi thật bạn từng gặp |
| "Core pass khoảng 2 giờ cho nhóm mạnh" | 27 | Ước lượng của giảng viên | Dùng để lập kế hoạch, không phải cam kết. Bảng mốc thời gian đáng tin hơn con số tổng |
| Anyscale 80/5, Standard 50/30/20 | — | Không có trong bài này | Đây là số của Ngày 24. Đừng lẫn hai bài khi ôn |
| "600 lời gọi → 15" trong mô-đun breaker | — | Tính toán của tài liệu này | Suy ra từ threshold + floor(D/reset). Đúng cho outage toàn phần liên tục; không áp cho lỗi ngắt quãng. Đọc kỹ mục giả định |
| "432 phút/tháng cho SLO 99%" trong mô-đun SLO | — | Tính toán của tài liệu này | Số học thuần tuý: (1 − 0,99) × 30 × 24 × 60. Kiểm lại được bằng máy tính bỏ túi |
| "Fallback giảm downtime ~18 lần" | — | Ước lượng của tài liệu này | Giả định hai provider hỏng độc lập — giả định mạnh và thường sai trong thực tế. Đọc là trần trên, không phải dự báo |
| Độ trễ 40 ms cho một lần trúng cache | — | Giả định của tài liệu này | Không có trên slide. Thay bằng số đo thật của bạn trước khi trích |
| Mọi con số trong mô-đun cache (3.000 lượt/ngày, hit 40%, false-hit 2%, $0,002) | — | Giá trị mặc định để minh hoạ | Slide 18 chỉ nói phải đo hit rate và false-hit rate; nó không đưa giá trị mẫu nào. Đây là số của bạn nhập, không phải số của giáo trình |

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực 
 tế đã chạy."

gần như mọi con số trong bài là ví dụ 
 cấu hình chứ không phải kết quả đo

bạn đo được

bạn quan sát được

bạn thống kê được

mô hình số học

bậc độ lớn

chiều của đánh đổi

không

---

<!-- chiron-source-span: {"source_span_id":"f880368c-a828-5af8-b89a-92db161e36cb","locator":{"kind":"html_section","section_id":"cheat","order":13,"heading":"✓ Cheat sheet ôn thi","source_file":"track-3-day-25.html"},"checksum":"9ca05f9ca9d6620feab7580e6d5c6c4423e5ac89a516963a53de28219435ba26"} -->

## ✓ Cheat sheet ôn thi

Nén 34 slide xuống một trang.

### Sáu danh sách phải thuộc

| Danh sách | Nội dung | Slide |
| --- | --- | --- |
| 6 nhóm lỗi | ① provider transient · ② degraded latency · ③ full outage · ④ orchestration loop · ⑤ tool/cache failure · ⑥ business action sai ①②③ ở provider (chứa được, không sửa được) · ④⑤⑥ ở phía bạn (sửa được) | 8 |
| 3 trạng thái breaker | CLOSED → (vượt failure_threshold) → OPEN → (hết reset_timeout) → HALF-OPEN → (thành công) CLOSED / (lỗi) OPEN Bốn mũi tên, không phải ba | 12 |
| 4 tham số breaker | failure_threshold · reset_timeout_seconds · success_threshold · exception nào tính là failure | 13 |
| 5 bậc fallback | model tốt nhất → provider dự phòng → model rẻ hơn → cache → thông báo tĩnh Kiểm 5 thứ khi tụt bậc: JSON mode, tool calling, context length, latency/cost, policy behavior | 14 |
| 3 tầng cache | ① prefix cache (provider) · ② semantic response cache (app) · ③ tool/result cache Triển khai theo thứ tự 1 → 3 → 2, vì tầng 2 rủi ro nhất | 17 |
| 3 lớp kiểm soát chi phí | per-request cap (giây) · rate limit theo user (phút–giờ) · ngân sách tháng (ngày–tháng) | 19 |

### Bảng số phải nhớ — quy đổi SLO sang thời gian

| SLO | Downtime mỗi tháng | Mỗi tuần | Ghi chú |
| --- | --- | --- | --- |
| 99% | 432 phút ≈ 7,2 giờ | 101 phút | Nghe cao nhưng cho phép hỏng rất nhiều |
| 99,5% | 216 phút ≈ 3,6 giờ | 50 phút | Mức điển hình của một API thương mại |
| 99,9% | 43 phút | 10 phút | "Ba số chín" — cần fallback mới đạt được |
| 99,99% | 4,3 phút | 1 phút | Cần dự phòng nhiều tầng và tự động hoá |

**Ghép provider:** phụ thuộc (cần cả hai) ⇒ `A × A`, độ tin cậy *giảm*. Dự phòng (fallback) ⇒ `1 − (1 − A)²`, độ tin cậy *tăng mạnh*. 
 Hai provider 99,5%: phụ thuộc ra 99,0025% (431 phút/tháng); fallback ra 99,9975% (~1 phút). **Chênh khoảng 36 lần với cùng hai thành phần.**

**Circuit breaker:** số lời gọi lọt vào provider hỏng = `failure_threshold + floor(thời gian outage / reset_timeout)`.

### Ba câu hay ra đề nhất — và câu trả lời một dòng

| Câu hỏi | Trả lời gọn |
| --- | --- |
| Vì sao retry một mình nguy hiểm? | Là vòng phản hồi dương: provider chậm ⇒ nhiều timeout ⇒ nhiều retry ⇒ tải ×3 ⇒ chậm hơn. Mạnh nhất đúng lúc hệ yếu nhất |
| Vì sao cần HALF-OPEN? | Để phục hồi không tạo đợt tấn công thứ hai — thử một request thay vì thả cả hàng đợi |
| Vì sao hit rate một mình gây hiểu lầm? | Hạ ngưỡng làm hit rate và false-hit rate cùng tăng. False-hit không tạo ra lỗi nào nên không ai thấy |
| Error rate 0% có đủ không? | Không. LLM luôn trả câu trông hợp lệ ⇒ cần quality SLO (faithfulness, safety, escalation) bên cạnh uptime SLO |
| Chi tiết triển khai được nhắc nhiều nhất? | route reason — nhắc ở slide 19, 28, 29. Không có nó thì fallback success rate không tính được |

### Metric bắt buộc cho report — danh sách gạch đầu dòng

**Đo:** availability · error rate · latency **P50/P95/P99** (Histogram, 
 không phải Gauge) · fallback success rate · circuit open count + **recovery time** · 
 cache hit rate + estimated cost saved · chaos scenario pass/fail

**Ghi từ giờ đầu tiên** (không khôi phục được về sau): `route reason` · `circuit_state` tại mỗi request · `similarity score` mỗi lần tra cache

**Report:** sơ đồ kiến trúc ngắn · bảng config · thiết lập thí 
 nghiệm · **bảng metric trước/sau cache** (nhớ lưu baseline *trước* khi viết cache) 
 · phân tích lỗi (nêu *một failure mode còn tồn tại* ) · next steps

---

<!-- chiron-source-span: {"source_span_id":"f2c553b9-d619-5393-9505-32483767b1c9","locator":{"kind":"html_section","section_id":"gloss","order":14,"heading":"A–Z Từ điển thuật ngữ","source_file":"track-3-day-25.html"},"checksum":"00060d4f950175962e07df46ee1a1a6d09610146f61110c75d37fcc8d99766bf"} -->

## A–Z Từ điển thuật ngữ

Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện.

---

<!-- chiron-source-span: {"source_span_id":"82e4cee9-0cb7-59c3-ad10-d7046f39835d","locator":{"kind":"html_section","section_id":"bloom","order":15,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-25.html"},"checksum":"bf80ad593ce1d571a0a43e36844cd98bf12f5fb59e5fe49970c5094b75beb3ab"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Quiz kiểm tra mức 1–3; demo cuối lab 
 (slide 30) kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 6 nhóm lỗi, 3 trạng thái breaker (kèm bốn mũi tên), 3 tầng cache, và 
 SLI/SLO/SLA/error budget. | Hình 1 · Hình 2 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao retry một mình nguy hiểm, và vì sao cần HALF-OPEN. | Ô kiểm tra chương 1 và 2 · slide 9 |
| 3 · Áp dụng | Cho một hệ thống mới, chạy khung 4 câu hỏi và thiết kế được thang fallback kèm điều kiện chuyển 
 bậc và metric kiểm chứng. | Bài 1 → 2 → 3 · slide 15 |
| 4 · Phân tích | Nhìn một báo cáo metric của người khác và chỉ ra chỗ nó đang che giấu vấn đề — trung bình thay 
 vì P95, hit rate không kèm false-hit, error rate 0% không kèm quality SLO. | Slide 23 · hiểu lầm 2 và 3 |
| 5 · Đánh giá | Trả lời "config nào bạn sẽ đổi khi lên production?" bằng con số và đánh đổi hai chiều, 
 và nêu được một failure mode còn tồn tại trong chính hệ của bạn. | Slide 30 bước 4–5 · mục áp dụng |

reset_timeout

không đi tìm giá trị đúng

cái gì hỏng nếu đặt quá thấp, cái gì hỏng 
 nếu đặt quá cao
