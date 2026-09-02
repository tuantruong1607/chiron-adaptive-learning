---
schema_version: 1
course_id: rag-intensive
document_id: "634b2777-95f6-58d1-8b79-eec691530eae"
document_version_id: "1041f329-086f-5d2b-aae9-258a77310e30"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Xác định bài toán cho AI — phân tích & breakdown từng slide"
source_file: "slide-buoi-2.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-buoi-2.html"
source_sha256: "c4fe1b7820f5f53a7c924ab35fbea7c66d4c3c05c8d682b86dbfb5af57010ee0"
parser_version: chiron-structured-markdown-v1
html_section_count: 16
interactive_module_count: 1
interactive_control_count: 5
language: vi
---

# Xác định bài toán cho AI — phân tích & breakdown từng slide

> 76 slide, từ yêu cầu mơ hồ đến Problem Statement đủ chặt để ra 
 quyết định. Đây là bài duy nhất trong khoá dạy cách từ chối một dự án AI — và đó là kỹ năng 
 đắt hơn nhiều so với kỹ năng xây nó.

<!-- chiron-source-span: {"source_span_id":"acffc832-faa1-5a44-8e3f-f7e601ed02f4","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-buoi-2.html"},"checksum":"3ca495345daf76dea8b7c75fdfd769c6b7fc0a0fbb0b7114879aabcd5087ad36"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Đây là bài **ít kỹ thuật nhất và khó áp dụng nhất** của cả khoá — một nghịch lý đáng 
 chú ý. Không có công thức nào để học thuộc, nhưng có *bốn bộ thẻ câu hỏi* (22 câu) và *một khung 9 trường* mà bạn sẽ dùng lại ở mọi dự án về sau.

Bài có một mạch rất rõ, và nắm được mạch thì không cần nhớ thứ tự slide:

```text
điểm đau  →  lượng hoá  →  AI có thêm giá trị không?  →  cấp độ nào?  →  đo bằng gì?  →  Go / Not Yet / No-Go
   ch.1        ch.2              ch.3                      ch.4           ch.5              ch.6
```

Lượt 1 · ~15 phút

Nắm mạch chính

- Đọc slide 26 (PAIR reframe), 45 (ba cấp độ), 
 67 (9 trường PS), 70 (Go/Not Yet/No-Go)
- Nhìn Hình 2 — cây quyết định Rule/Workflow/Agent
- Mục tiêu: nói được vì sao "làm chatbot AI" chưa phải một bài toán

Lượt 2 · ~60 phút

Chương 2, 4, 5 kỹ

- Ba chương này chứa thứ ra đề được: khung PS, ba cấp độ, precision↔recall
- Làm mô-đun precision↔recall — phần duy nhất tính ra số của bài
- Tự điền 9 trường PS cho SmartCheck AI trước khi đọc đáp án

Lượt 3 · ~20 phút

Trước quiz

- 6 hiểu lầm — bài này toàn bẫy "nghe rất hợp lý"
- Cheat sheet — 22 câu hỏi và bốn danh sách
- Từ điển — PS, PAIR, HCD, automate/augment, precision, HITL

"Do not solve the problem I am asked to solve."

một giải pháp mà ai đó tự nghĩ ra

kỹ thuật này giúp tôi lùi lại một bước như thế nào?

---

<!-- chiron-source-span: {"source_span_id":"79f5ad38-f244-593f-ba4e-7addbb6dfa6a","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"slide-buoi-2.html"},"checksum":"06fdba20942ca59368166f9266846ae34fe47c526cd69fcc4cf2c4efdefe1de1"} -->

## 00 Mở đầu

Slide 1–14: bốn câu hỏi trọng tâm, ba trụ cột, và hai tình huống mở màn.

### Slide 1–4 Bốn câu hỏi trọng tâm và agenda

> Trích slide 
>  " 01 Bài toán có thực sự cần AI giải quyết? 02 Nếu có, giải pháp 
>  ở cấp độ nào: Rule, Workflow, hay Agent? 03 Problem Statement đã đủ rõ ràng để 
>  triển khai? 04 Khi nào quyết định: Go, Not Yet, hay No-Go?" 
>  "Mục tiêu: Biến yêu cầu mơ hồ thành Problem Statement rõ ràng để ra quyết định"

Bốn câu hỏi này không phải bốn chủ đề rời — chúng là **một chuỗi có thứ tự bắt buộc**, 
 và mỗi câu chỉ trả lời được sau khi câu trước đã xong:

| Câu | Trả lời ở | Nếu bỏ qua câu này thì hỏng thế nào |
| --- | --- | --- |
| ① Có cần AI không? | PAIR bước ① — slide 36–37 | Xây AI cho việc mà một cái rule 20 dòng làm tốt hơn, rẻ hơn, giải thích được |
| ② Cấp độ nào? | PAIR bước ② + slide 45 | Nhảy thẳng lên agent — đắt hơn, chậm hơn, khó kiểm thử, lỗi khó đoán |
| ③ Đủ rõ để đo chưa? | PAIR bước ③ — slide 57–59 | Không có baseline nên không chứng minh được cải tiến; dự án bị cắt vì "không thấy giá trị" |
| ④ Go / Not Yet / No-Go | Slide 70 | Quyết định theo cảm tính hoặc theo thiên kiến công nghệ |

Bài này dành **4 giờ lý thuyết + 4 giờ lab** mà *không viết một dòng code nào*. 
 Ba bài nộp đều là văn bản: nhật ký tìm bài toán, Problem Statement, nhật ký phản tư.

Đó là một tuyên bố về thứ tự ưu tiên. Ngày 1 dạy bạn *gọi* được 
 AI; Ngày 2 dạy bạn *quyết định có nên gọi hay không*. Và như slide 16 sẽ nói: **"Giải pháp xuất sắc cho sai vấn đề có thể còn tệ hơn không có giải pháp"** — vì nó 
 tiêu tiền, tiêu thời gian, và tạo cảm giác vấn đề đã được xử lý.

### Slide 6–8 Ba trụ cột và "sách giáo khoa" Google PAIR

> Trích slide 
>  "Sản phẩm tích hợp AI bản chất vẫn là một sản phẩm hoàn chỉnh, kế thừa chứ không thay 
>  thế nguyên lý sản phẩm truyền thống." 
>  " AI Engineering — Triển khai RAG, Agent, Guardrails, Evaluation. 
>  Product Thinking — Xác định đúng bài toán, thấu hiểu người dùng, tránh xây dựng 
>  những tính năng không mang lại giá trị. Design Thinking — Thiết kế dựa trên mô hình 
>  tư duy, cơ chế phản hồi và tối ưu trải nghiệm khi AI sai sót." 
>  "Google PAIR — People + AI Guidebook, 6 chương. Chương 1 (User Needs + Defining Success) là 
>  xương sống buổi sáng nay. "

Ba trụ cột này ánh xạ khá gọn vào ba nhóm câu hỏi mà một dự án AI phải trả lời, và biết trụ cột nào 
 trả lời câu nào giúp bạn biết *hỏi ai* khi bị kẹt:

| Trụ cột | Trả lời câu hỏi | Học ở ngày nào |
| --- | --- | --- |
| Product Thinking | Có nên làm không? Ai đau, đau bao nhiêu, giá trị ở đâu | Ngày 2, 5, 6, 15 |
| AI Engineering | Làm thế nào? Kiến trúc, RAG, agent, guardrail, eval | Ngày 3–4, 7–14, cả Track 3 |
| Design Thinking | Khi AI sai thì sao? Mô hình tâm trí, phản hồi, thất bại êm | Ngày 2 (ch.5), 11, và Ngày 18 |

PAIR Guidebook (Google) là tài liệu *thiết kế sản phẩm AI lấy con người làm trung tâm*, viết 
 trước làn sóng LLM. Điểm mạnh: nó bàn về **quyết định** chứ không về công nghệ, nên 
 không lỗi thời — các câu hỏi "AI có thêm giá trị không", "automate hay augment", "định nghĩa 
 đúng/sai thế nào" đúng cho mọi thế hệ model.

**Giới hạn cần biết:** vì viết trước LLM, PAIR không nói gì 
 về prompt, context, token, hay chi phí theo lượt gọi. Hai tài liệu phụ lấp chỗ đó — Anthropic *Building effective agents* cho phần cấp độ giải pháp, và Google *Rules of ML* cho 
 nguyên tắc "đơn giản trước". Cả ba đều nói chung một điều: **bắt đầu từ giải pháp đơn giản 
 nhất**.

### Slide 9–13 "AI chatbot" chưa phải là một bài toán

> Trích slide 
>  Thảo luận: "Tôi muốn xây dựng chatbot AI cho khách hàng." — Theo bạn chatbot đó đang làm gì? 
>  " PHỤC VỤ KHÁCH HÀNG — Giải đáp FAQ · Tư vấn và hỗ trợ mua hàng · Chăm sóc sau mua 
>  hàng · Bán thêm & bán chéo. HỖ TRỢ NỘI BỘ — Phân loại yêu cầu hỗ trợ · Tra cứu 
>  thông tin nghiệp vụ · Đề xuất nháp phản hồi để con người phê duyệt · Chuyển tiếp câu hỏi phức tạp" 
>  " Đối tượng khác nhau dẫn đến quy trình, chỉ số và rủi ro khác nhau. 
>  đối tượng khác → metric khác! " 
>  "Khoan đã, bạn có hỏi không? — Học viên gặp khó khăn ở công đoạn nào? Trợ giảng quá tải ở bước nào? 
>  Quy trình hiện tại đang xử lý ra sao? Giải pháp này xây dựng phục vụ ai? 
>  Chưa thấu hiểu điểm đau thì chưa đề xuất giải pháp. "

Đây là **bài tập tư duy quan trọng nhất của chương mở đầu**. Một câu nghe rất cụ thể — 
 "chatbot AI cho khách hàng" — thực ra chứa *ít nhất tám bài toán khác nhau*, và chúng khác nhau 
 ở mọi chiều quan trọng:

| Nếu chatbot làm việc này | Đối tượng | Chỉ số thành công | Rủi ro lớn nhất khi sai |
| --- | --- | --- | --- |
| Giải đáp FAQ | Khách hàng | Tỷ lệ tự giải quyết, thời gian phản hồi | Trả lời sai chính sách → khiếu nại |
| Bán thêm / bán chéo | Khách hàng | Doanh thu, tỷ lệ chuyển đổi | Gợi ý phiền hà → mất thiện cảm, khách rời đi |
| Phân loại yêu cầu hỗ trợ | Nhân viên nội bộ | Độ chính xác phân loại, thời gian định tuyến | Định tuyến sai → chậm trễ, không ai chịu trách nhiệm |
| Soạn nháp cho người duyệt | Nhân viên nội bộ | Thời gian nhân viên phải sửa nháp | Thấp — vì đã có người duyệt |

Cùng một công nghệ, cùng một model, nhưng **"soạn nháp cho người duyệt" có rủi ro thấp hơn 
 hẳn "trả lời thẳng khách hàng"** — chỉ vì có một con người đứng giữa.

Đó chính là phân biệt *automate* và *augment* mà [slide 43](#s43) sẽ đặt 
 tên, và là lý do [slide 44](#s43) khuyên tăng mức tự động hoá *theo pha* thay vì 
 bật full-auto ngay.

**Rút ra được ngay hôm nay:** khi ai đó nói "làm chatbot AI", 
 câu hỏi đầu tiên không phải "dùng model nào" mà là **"cho ai, thay thế bước nào trong quy trình 
 hiện tại, và ai chịu trách nhiệm khi nó sai?"** Ba câu đó đã là ba trường trong Problem 
 Statement ở [slide 67](#s67).

### Slide 14 "Do not solve the problem I am asked to solve" — câu phản trực giác nhất bài

> Trích slide 
>  " COUNTER-INTUITIVE RULE — 'Do not solve the problem I am asked to solve.' 
>  — Don Norman · jnd.org"

Câu này dễ bị hiểu thành "đừng nghe khách hàng", và đó là cách hiểu sai. Ý đúng nằm ở một quan sát 
 rất cụ thể: **yêu cầu bạn nhận được hầu như luôn đã là một giải pháp**, chứ không phải 
 một vấn đề.

| Người ta nói | Đó thực ra là | Vấn đề gốc có thể là |
| --- | --- | --- |
| "Làm cho tôi một chatbot AI" | Một giải pháp | Nhân viên hỗ trợ quá tải · khách hàng chờ lâu · câu hỏi lặp lại nhiều |
| "Tôi cần báo cáo tự động" | Một giải pháp | Mỗi thứ Hai mất 90 phút gom số từ ba nơi ( slide 29 ) |
| "Cho AI chấm bài giúp" | Một giải pháp | Trợ giảng không đủ thời gian cho câu hỏi khó vì bận câu dễ |

**Vì sao phân biệt này quan trọng:** nếu bạn nhận "làm 
 chatbot" rồi làm đúng chatbot, bạn có thể giao đúng thứ được yêu cầu mà *vấn đề gốc vẫn còn* — nhân viên vẫn quá tải, chỉ là giờ họ quá tải với việc sửa câu trả lời của bot. Đây chính là 
 anti-pattern *"Solution-first"* ở [slide 24](#s23).

không

hỏi

slide 25

"Nếu stakeholder không mô tả được quy trình 
 hiện tại và chi phí thiệt hại khi xảy ra lỗi, mọi đề xuất giải pháp AI đều chỉ là phỏng đoán thiếu 
 căn cứ."

phát hiện đầu tiên của bạn

Not Yet

---

<!-- chiron-source-span: {"source_span_id":"26b71d64-2686-5d7a-b385-a94a2d6ab27b","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Problem Discovery","source_file":"slide-buoi-2.html"},"checksum":"2b24e48242a47b202dce0b4ac585ee66d8298082553174de32f1c8e0157f6615"} -->

## 01 Problem Discovery

Slide 15–26: Double Diamond, vòng lặp HCD, bốn ống kính tìm bài toán, và bốn anti-pattern.

### Slide 15–18 Double Diamond và vòng lặp HCD

> Trích slide 
>  " DIAMOND 1 — TÌM ĐÚNG VẤN ĐỀ. Discover: Mở rộng — khảo sát vấn đề căn bản. 
>  Define: Thu hẹp — xác định đúng bài toán gốc. 
>  DIAMOND 2 — TÌM ĐÚNG GIẢI PHÁP. Develop: Mở rộng — nhiều giải pháp tiềm năng. 
>  Deliver: Thu hẹp — chọn và triển khai." 
>  "Kỹ sư và doanh nhân được đào tạo để giải vấn đề. Nhà thiết kế được đào tạo để khám phá vấn đề 
>  thật." 
>  " Giải pháp xuất sắc cho sai vấn đề có thể còn tệ hơn không có giải pháp. " 
>  "Quy trình HCD: Observation → Ideation → Prototype → Test → Iteration"

Hình dạng kim cương không phải trang trí — nó mã hoá một quy tắc kỷ luật: **phải phình ra trước khi thu lại, và không được trộn hai động tác**.

_Sơ đồ: Mô hình Double Diamond với hai kim cương tìm đúng vấn đề và tìm đúng giải pháp - Hai hình kim cương nối tiếp nhau. Kim cương thứ nhất là tìm đúng vấn đề, gồm giai đoạn Discover phân kỳ mở rộng góc nhìn và giai đoạn Define hội tụ chọn lọc, kết thúc bằng một Problem Statement. Kim cương thứ hai là tìm đúng giải pháp, gồm giai đoạn Develop phân kỳ tạo nhiều phương án và giai đoạn Deliver hội tụ chọn và triển khai. Điểm hẹp ở giữa hai kim cương là nơi bài toán được chốt. Bên dưới liệt kê các kỹ thuật của từng giai đoạn._

Hình 1 — Double Diamond (slide 16–18).

Problem Statement

Đây là lỗi phổ biến nhất trong mọi buổi họp brainstorm: ai đó nêu ý tưởng, người khác lập tức 
 phản biện "cái đó không khả thi đâu". Kết quả là nhóm chỉ còn lại những ý tưởng *an toàn* — 
 tức là những ý tưởng ai cũng nghĩ ra được.

Slide 18 nói thẳng ở bước Ideation: *"Tránh phê bình ý tưởng của bản thân hay người khác. 
 Đặt câu hỏi về tất cả mọi thứ."* Việc phê bình vẫn cần — nhưng nó thuộc pha **Define**, 
 với công cụ riêng (ma trận Tác động–Nỗ lực, dot voting), và diễn ra *sau*.

**Áp dụng cho một người tự làm:** viết ra 10 cách giải trước 
 khi đánh giá cái nào tốt. Nếu bạn đánh giá ngay từ ý tưởng thứ nhất, bạn sẽ dừng ở ý tưởng thứ nhất.

"Kỹ sư và doanh nhân được đào tạo để giải vấn đề. Nhà thiết kế được đào tạo để khám phá vấn đề 
 thật."

thiên lệch nghề nghiệp

### Slide 19–22 Câu hỏi nguyên bản và ba case study

> Trích slide 
>  "Isaac Newton: Quả táo rơi xuống đất — vậy Mặt Trăng có đang 'rơi' tự do không? · Polaroid: Tại sao 
>  không thể xem ảnh ngay lập tức sau khi chụp? · Airbnb: Liệu không gian sống bỏ trống có thể dùng làm 
>  dịch vụ lưu trú? — Tò mò trước. Đánh giá sau. " 
>  " CURSOR — 'Lệch năng lực cốt lõi': Từ bỏ mảng AI thiết kế cơ khí (CAD) để tập trung 
>  vào AI code editor — nơi đội ngũ am hiểu sâu sắc quy trình nghiệp vụ." 
>  " ARTIFACT — 'Sản phẩm tốt ≠ Thị trường lớn': Ứng dụng đọc tin tích hợp AI xuất sắc, 
>  nhưng quy mô thị trường quá hẹp để thương mại hóa thành công (đóng cửa 1/2024)." 
>  " NOTEBOOKLM — 'Định vị đúng điểm đau': Tập trung giải quyết nhu cầu hỏi đáp, tóm 
>  tắt trên tài liệu cá nhân và đối chiếu nguồn gốc bằng trích dẫn." 
>  "Lộ trình: Bài toán → Quy trình vận hành → Chỉ số đo lường → Giải pháp AI "

Ba case study này minh hoạ ba kiểu thất bại/thành công **khác nhau về bản chất**, và 
 đó là lý do chúng được đặt cạnh nhau:

| Case | Bài toán có thật không? | Giải pháp có tốt không? | Thứ quyết định |
| --- | --- | --- | --- |
| Cursor | Có, ở cả hai mảng | Có | Đội ngũ am hiểu lĩnh vực nào — chọn mảng mình hiểu sâu |
| Artifact | Có | Rất tốt | Quy mô thị trường — bài toán thật nhưng quá ít người trả tiền |
| NotebookLM | Có | Có | Định vị hẹp và rõ — hỏi đáp trên tài liệu của chính bạn, có trích dẫn |

Sản phẩm tốt, công nghệ tốt, bài toán có thật. Vẫn đóng cửa. Điều đó nói rằng **"có bài toán thật" là điều kiện cần, không phải điều kiện đủ**.

Với dự án học tập hay dự án nội bộ, chiều "quy mô thị trường" dịch thành: *bao nhiêu người gặp vấn đề này, bao nhiêu lần mỗi tuần?* Đó chính là ô **Impact** trong Problem Statement ( [slide 67](#s67) ) và là lý do [slide 31](#s31) đòi lượng hoá baseline.

Một bài toán có thật nhưng chỉ xảy ra 2 lần/tháng cho 1 người thì *không đáng xây AI* — dù nó khó chịu thật. Câu hỏi đầu tiên của thang quyết định ở [slide 54](#s54) đúng là câu này: *"Tần suất & tác động có đủ lớn?"*

Bài toán → Quy trình vận hành → Chỉ số đo lường → Giải pháp AI.

cuối cùng

Quick Problem Card

### Slide 23–24 Bốn ống kính tìm bài toán, và bốn anti-pattern

> Trích slide 
>  " REPETITIVE — Việc diễn ra thường xuyên; công đoạn nào cần chuẩn hóa? 
>  TIME-CONSUMING — Khối lượng xử lý lớn; thời gian hao phí ở bước nào? 
>  AI ADVANTAGE — Tác vụ đòi hỏi phân tích ngữ cảnh, xử lý ngôn ngữ tự nhiên, tổng hợp 
>  đa nguồn. USER PAIN POINTS — Ai đang gặp khó khăn, phàn nàn hoặc bị tắc nghẽn?" 
>  " Anti-patterns: ① Solution-first — Xây chatbot/agent trước khi 
>  làm rõ quy trình và điểm nghẽn. ② No baseline — Không lượng hóa tổn thất hiện tại. 
>  ③ No evaluation — Không thiết lập kịch bản kiểm thử, chỉ số hoặc phương án đối chứng. 
>  ④ No boundary — Không rõ phạm vi tự chủ của AI và thời điểm cần con người phê duyệt."

Bốn anti-pattern này đáng học thuộc, vì chúng là **danh sách kiểm tra ngược**: khi thấy 
 một đề xuất AI, bạn đối chiếu và tìm ra ngay chỗ hổng.

| Anti-pattern | Nghe như thế nào trong thực tế | Câu hỏi phá vỡ nó | Ô nào trong PS bị thiếu |
| --- | --- | --- | --- |
| ① Solution-first | "Chúng ta cần một agent để…" | "Quy trình hiện tại có mấy bước, ai bàn giao cho ai?" | Workflow · Bottleneck |
| ② No baseline | "Việc này tốn nhiều thời gian lắm" | "Bao nhiêu phút, bao nhiêu lần một tuần, bao nhiêu người?" | Impact |
| ③ No evaluation | "Demo chạy ngon rồi" | "Đo bằng gì, so với cái gì, ngưỡng đạt là bao nhiêu?" | Success Metric |
| ④ No boundary | "AI sẽ tự xử lý hết" | "AI không được làm gì? Ai duyệt trước khi gửi?" | Boundary · Rủi ro & HITL |

Cột cuối cùng cho thấy một điều gọn gàng: **khung 9 trường ở [slide 67](#s67) chính là thuốc giải cho bốn anti-pattern này**. Điền đủ 9 trường thì tự động không mắc cả bốn.

Nên nếu phải nhớ một thứ duy nhất từ Ngày 2, hãy nhớ khung 9 trường — 
 mọi thứ khác trong bài đều là cách *điền* hoặc *kiểm tra* khung đó.

vấn đề

AI ADVANTAGE

giải pháp

đi tìm

lọc

"Tập trung nhận diện vấn đề; chưa vội đề xuất giải pháp."

### Slide 25–26 Năm câu phỏng vấn, và cách PAIR đặt lại câu hỏi

> Trích slide 
>  " Discovery interview — 5 câu nên hỏi stakeholder: 1 · Pain Point là gì? Tần suất 
>  lặp lại? 2 · Workflow hiện tại như thế nào? Công cụ nào ở từng bước, ai bàn giao cho ai? 
>  3 · Thiệt hại do vấn đề gây ra là gì? (thời gian, chi phí, SLA, conversion) 4 · Hậu quả nếu AI sai sót 
>  là gì? Khâu nào cần HITL? 5 · Ai có quyền phê duyệt (nói YES)? Metric và mức rủi ro nào quyết định 
>  việc đầu tư?" 
>  " PAIR · Chương 1 — REFRAME CÂU HỎI: 'Can we use AI to ______?' ↓ thay 
>  bằng hai câu hỏi ↓ 'How might we solve ______?' và 'Can AI solve this problem in a unique 
>  way?' " 
>  " Hỏi về bài toán trước, về AI sau — AI chỉ là một phương án trong nhiều phương án khả dĩ. "

Kỹ thuật reframe của PAIR đơn giản tới mức dễ bị coi thường, nhưng nó có tác dụng thật vì **nó tách một câu hỏi đã gộp sẵn kết luận thành hai câu hỏi trung lập**:

```text
"Can we use AI to ___?"          ← đã giả định AI là câu trả lời; chỉ còn hỏi CÁCH dùng
        │
        ├──▶ "How might we solve ___?"              ← mở lại toàn bộ không gian giải pháp
        │                                              (rule? quy trình? tài liệu? tuyển thêm người?)
        │
        └──▶ "Can AI solve this in a UNIQUE way?"    ← nếu AI thắng, nó phải thắng vì lý do RIÊNG
                                                       chứ không phải vì "cũng làm được"
```

Nó không hỏi "AI có làm được không" — gần như việc gì AI cũng làm được ở mức nào đó. Nó hỏi **AI có làm được theo cách mà phương án khác không làm được không**.

Đây chính là bộ lọc mà [slide 36–37](#s36) cụ thể hoá thành hai danh sách: tám trường 
 hợp AI có lợi thế, và sáu trường hợp AI *không* tốt hơn. Nếu bài toán của bạn không nằm trong 
 danh sách thứ nhất, câu trả lời cho "unique way" gần như chắc chắn là không.

**Ví dụ tự kiểm:** "Dùng AI để gửi email nhắc nộp bài đúng 
 hạn?" — AI làm được. Nhưng một cron job làm được y hệt, rẻ hơn, chính xác 100%, và không bao giờ bịa. 
 Câu trả lời cho "unique way" là *không* ⇒ dừng ở Rule.

"Ai có quyền phê duyệt (nói YES)? Metric và mức độ rủi ro nào sẽ trực tiếp quyết định việc đầu 
 tư?"

vấn đề

quyết định

Success Metric

người ra quyết định quan tâm

#### Ô kiểm tra — Chương mở đầu & 1

Trả lời thành tiếng trước khi mở đáp án.

**1.** Sếp bạn nói: "Quý này làm cho tôi một chatbot AI cho khách hàng." Bạn làm 
 gì tiếp theo, và *không* làm gì? Áp dụng

#### Đáp án

**Không làm: bắt tay chọn model, vẽ kiến trúc, hay hỏi "dùng RAG hay fine-tune".** Đó là anti-pattern *Solution-first* (slide 24).

**Nhận ra trước hết:** "chatbot AI cho khách hàng" là *một giải pháp*, không 
 phải một vấn đề — đúng câu Don Norman ở slide 14. Và nó chứa ít nhất tám bài toán khác nhau 
 (slide 10): FAQ, tư vấn mua hàng, upsell, phân loại ticket, soạn nháp… mỗi cái khác nhau về đối 
 tượng, chỉ số và rủi ro.

**Làm: chạy 5 câu phỏng vấn stakeholder (slide 25)** — ① pain point và tần suất 
 ② workflow hiện tại, công cụ, ai bàn giao cho ai ③ thiệt hại lượng hoá được ④ hậu quả nếu AI sai, 
 khâu nào cần HITL ⑤ ai duyệt và họ nhìn chỉ số nào.

**Và reframe theo PAIR (slide 26):** đổi "Can we use AI to…" thành *"How might we solve…"* + *"Can AI solve this in a unique way?"*

**Nếu stakeholder không mô tả được quy trình và chi phí lỗi** — slide 25 nói thẳng 
 mọi đề xuất đều là phỏng đoán. Đó không phải lý do từ chối, mà là phát hiện đầu tiên, và thường dẫn 
 tới *Not Yet*.

**2.** Artifact có sản phẩm tốt, công nghệ tốt, bài toán có thật — vẫn đóng cửa. 
 Bài học là gì, và nó tương ứng với ô nào trong Problem Statement? Phân tích

#### Đáp án

**"Có bài toán thật" là điều kiện cần, không phải điều kiện đủ.** Artifact thất bại 
 vì *quy mô thị trường quá hẹp* — không đủ người trả tiền, dù sản phẩm xuất sắc.

**Ô tương ứng: Impact** — tổn thất lượng hoá bằng thời gian, chi phí, SLA hoặc chất 
 lượng. Với dự án nội bộ, chiều này dịch thành: *bao nhiêu người gặp vấn đề, bao nhiêu lần mỗi 
 tuần, mỗi lần tốn bao nhiêu?*

**Hệ quả thực hành:** một bài toán có thật nhưng chỉ xảy ra 2 lần/tháng cho 1 người 
 thì không đáng xây AI — dù nó khó chịu thật. Câu hỏi đầu tiên của thang quyết định ở slide 54 chính 
 là *"Tần suất & tác động có đủ lớn?"*, và nếu thấp thì slide khuyên xử lý thủ công hoặc 
 sửa quy trình trước.

**Đối chiếu hai case kia:** Cursor thắng nhờ chọn mảng *đội ngũ am hiểu sâu*; 
 NotebookLM thắng nhờ *định vị hẹp và rõ*. Ba case, ba yếu tố quyết định khác nhau — đó là lý 
 do chúng được đặt cạnh nhau.

**3.** Vì sao Double Diamond cấm trộn phân kỳ với hội tụ, và điều đó nghĩa là gì 
 khi bạn làm việc một mình? Hiểu

#### Đáp án

**Vì phê bình sớm giết ý tưởng trước khi nó kịp được xem xét — và thứ sống sót chỉ là 
 những ý tưởng an toàn, tức những ý tưởng ai cũng nghĩ ra được.**

Slide 18 nói thẳng ở bước Ideation: *"Tránh phê bình ý tưởng của bản thân hay người khác."* Việc phê bình vẫn cần — nhưng nó thuộc pha **Define**, với công cụ riêng (gom nhóm, 
 ma trận Tác động–Nỗ lực, dot voting), và diễn ra *sau*.

**Khi làm một mình:** viết ra 10 cách giải *trước khi* đánh giá cái nào tốt. 
 Nếu đánh giá ngay từ ý tưởng thứ nhất, bạn sẽ dừng ở ý tưởng thứ nhất — và ý tưởng thứ nhất thường 
 chính là cái giải pháp mà người ta đã đưa cho bạn.

**Điểm cộng nếu nêu được:** Ngày 2 chỉ làm *kim cương thứ nhất* (tìm đúng vấn 
 đề). Kim cương thứ hai — tìm đúng giải pháp — là toàn bộ phần còn lại của khoá học.

---

<!-- chiron-source-span: {"source_span_id":"a8170e64-3bdf-50ce-9542-7793537124df","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Problem Statement","source_file":"slide-buoi-2.html"},"checksum":"4b1e977f044ac60d21eb71b7a345fa062bc24a3a30ce2d0b90de9b02789b96a1"} -->

## 02 Problem Statement

Slide 27–33: Quick Problem Card, lượng hoá bài toán, và cặp chỉ số output/input.

### Slide 28–29 Quick Problem Card và ví dụ đã điền

> Trích slide 
>  " Bài toán 1 câu — Vấn đề cụ thể cần giải quyết ( không bao gồm giải pháp ). 
>  Đối tượng — Cá nhân/bộ phận chịu tác động trực tiếp. Quy trình hiện tại 
>  — Các bước vận hành hiện tại (3–7 bước). Nút thắt & Tác động — Khâu gây chậm trễ, 
>  sai sót hoặc lặp lại; hệ quả cụ thể. Chỉ số đo thành công — Chỉ số định lượng cụ thể. 
>  Định hướng giải pháp — No AI / Rule / Workflow / Agent / Chưa xác định." 
>  " Ví dụ — Weekly Report: Mỗi thứ Hai, PM mất khoảng 90 phút tổng hợp Weekly Report 
>  từ Jira, Google Sheets và Slack; bước viết narrative tốn thời gian nhất. […] Nút thắt: bước viết 
>  narrative mất khoảng 25 phút. Tổng flow khoảng 90 phút/tuần/PM; team 3 PM tương đương 270 phút/tuần. 
>  Chỉ số: Giảm từ 90 phút xuống dưới 30 phút, nhưng không làm tăng số câu CEO/EM phải hỏi lại. 
>  Định hướng: Workflow."

Ví dụ đã điền này đáng đọc kỹ vì nó làm đúng **bốn điều mà bản nháp của người mới thường 
 thiếu**:

| Điều làm đúng | Trong ví dụ | Bản nháp thường viết gì |
| --- | --- | --- |
| Con số ở khắp nơi | 90 phút · 25 phút · 270 phút/tuần cho 3 PM | "tốn nhiều thời gian" |
| Chỉ ra bước cụ thể | Nút thắt là bước viết narrative, không phải cả quy trình | "quy trình làm báo cáo chậm" |
| Metric có mặt sau | " nhưng không làm tăng số câu CEO/EM phải hỏi lại" | Chỉ có mục tiêu chính, không có ràng buộc |
| Định hướng nêu rõ vai trò người | "AI hỗ trợ draft narrative, PM vẫn review/edit trước khi gửi " | "dùng AI để tự động hoá" |

*"Giảm thời gian làm report từ 90 phút xuống dưới 30 phút, **nhưng không làm tăng số câu 
 CEO/EM phải hỏi lại**."*

Vế thứ hai là một **guard metric** — chỉ số canh chừng. Không có nó, bạn có thể "thành 
 công" bằng cách viết báo cáo cẩu thả trong 10 phút, và toàn bộ thời gian tiết kiệm được chuyển sang 
 cho CEO đi hỏi lại.

**Quy tắc rút ra:** mỗi khi metric của bạn là "làm nhanh hơn" 
 hoặc "làm rẻ hơn", hãy hỏi *"nhanh/rẻ hơn có thể đạt được bằng cách làm tệ đi không?"* Nếu có, 
 bạn cần một guard metric. Đây là phiên bản sớm của điều mà Ngày 24 gọi là *quality SLO đi cùng 
 uptime SLO*.

chatbot, AI, tự động, model, agent

"PM mất khoảng 90 phút tổng hợp Weekly Report… bước 
 viết narrative tốn thời gian nhất và dễ làm trễ deadline"

### Slide 30–32 Lượng hoá bài toán và cặp chỉ số output/input

> Trích slide 
>  " 01 · BASELINE — Hiện trạng / where we are. Mức hao phí hiện tại là bao nhiêu? 
>  Bằng con số cụ thể. 02 · TARGET — Mục tiêu / where to go. Ngưỡng cụ thể là gì? 
>  03 · MEASUREMENT — Đo lường / how we know. Chỉ số nào chứng minh? Cách thu thập?" 
>  " Điểm đau chưa được định lượng thì không thể xác định giá trị thực tế của AI " 
>  " OUTPUT METRIC — Kết quả cuối cùng / what we optimize. INPUT METRICS 
>  — Các đòn bẩy / what we can move: tỷ lệ câu hỏi được phân loại chính xác · tỷ lệ yêu cầu được chuyển 
>  tiếp kịp thời · thời gian TA hiệu chỉnh bản nháp. tăng cái này → đo cái kia " 
>  " 'Nâng cao hiệu suất' không phải chỉ số — cần gắn với hiện trạng, mục tiêu và 
>  phương pháp đo."

Bộ ba **baseline → target → measurement** là thứ đơn giản đến mức dễ bỏ qua, nhưng 
 thiếu một trong ba thì cả metric vô dụng:

| Thiếu cái gì | Hậu quả | Nghe như thế nào |
| --- | --- | --- |
| Thiếu baseline | Không chứng minh được có cải thiện | "Sau khi triển khai, thời gian xử lý là 30 phút" — trước đó bao nhiêu? |
| Thiếu target | Không biết khi nào thì xong | "Chúng ta muốn giảm thời gian xử lý" — giảm bao nhiêu thì đạt? |
| Thiếu measurement | Số liệu không lấy được, hoặc mỗi người đo một kiểu | "Giảm từ 90 xuống 30 phút" — ai bấm giờ, tính từ lúc nào tới lúc nào? |

**Output metric** là thứ bạn *muốn* — nhưng thường bạn không tác động trực 
 tiếp lên nó được. "Giảm thời gian phản hồi cho học viên" là kết quả của nhiều thứ cộng lại.

**Input metrics** là những cái *bạn vặn được*: tỷ lệ phân loại đúng, tỷ lệ 
 chuyển tiếp kịp thời, thời gian TA sửa nháp. Mũi tên trên slide — *"tăng cái này → đo cái kia"* — mô tả đúng quan hệ nhân quả bạn đang đặt cược.

**Và đây là chỗ để kiểm tra giả thiết của mình:** nếu bạn cải 
 thiện input metric mà output metric không nhúc nhích, giả thiết nhân quả của bạn sai — có thể nút thắt 
 thật nằm chỗ khác. Đó là thông tin rất quý, và bạn chỉ có được nó nếu đo *cả hai*.

Thời gian:

Chất lượng:

Tải trọng:

[đại lượng] từ [baseline] xuống/lên [target]

---

<!-- chiron-source-span: {"source_span_id":"87c24b70-f88a-5bed-9dd2-9af6f703cb5e","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Có nên ứng dụng AI?","source_file":"slide-buoi-2.html"},"checksum":"27d29007d592faf091f1bcb577736f3de59094ed45848fe31085564b45877c5f"} -->

## 03 Có nên ứng dụng AI?

Slide 34–40: ba bước PAIR, tám trường hợp AI có lợi thế, sáu trường hợp không, và Build/Boost/Buy.

### Slide 34–35 Ba bước quyết định theo PAIR

> Trích slide 
>  " BƯỚC ① Giao điểm: nhu cầu × thế mạnh AI — Bài toán của bạn có nằm trong nhóm việc 
>  AI làm tốt hơn hẳn rule/heuristic không? → trả lời câu hỏi 1: có thực sự cần AI? " 
>  " BƯỚC ② Automate hay Augment? — AI thay thế hay hỗ trợ con người? Mức tự động hóa 
>  tăng dần theo độ tin cậy và rủi ro. → trả lời câu hỏi 2: giải pháp ở cấp độ nào? " 
>  " BƯỚC ③ Reward function & tiêu chí thành công — Định nghĩa 'đúng/sai' của hệ 
>  thống (precision ↔ recall) và ngưỡng thành công đo được. → trả lời câu hỏi 3: PS đã đủ rõ để đo? " 
>  "Đi hết 3 bước này, bạn trả lời được cả 4 câu hỏi của ngày hôm nay."

Ba bước này có **thứ tự bắt buộc**, và lý do của thứ tự đó rất thực dụng: mỗi bước *thu hẹp* câu hỏi cho bước sau.

```text
① Có cần AI không?                   nếu KHÔNG → dừng ở Rule, xong. Không cần bước ② ③
        │ có
        ▼
② AI thay người hay hỗ trợ người?    quyết định này định luôn mức rủi ro chấp nhận được
        │
        ▼
③ Định nghĩa đúng/sai + ngưỡng       chỉ định nghĩa được KHI đã biết ai chịu trách nhiệm
        │                              (augment thì ngưỡng lỏng hơn — vì có người duyệt)
        ▼
④ Go / Not Yet / No-Go
```

Ngưỡng "đúng bao nhiêu phần trăm thì chấp nhận được" **không có đáp án tuyệt đối** — 
 nó phụ thuộc vào việc có ai duyệt hay không.

• Nếu AI *gửi thẳng cho học viên* (automate): một câu sai đi thẳng tới người dùng ⇒ ngưỡng 
 phải rất cao. 
 • Nếu AI *soạn nháp cho TA duyệt* (augment): TA bắt được lỗi ⇒ ngưỡng thấp hơn nhiều vẫn dùng 
 được, và metric đúng lại là *"TA phải sửa bao nhiêu phần trăm"* chứ không phải "AI đúng bao 
 nhiêu phần trăm".

Nên nếu ai đó hỏi "AI phải chính xác bao nhiêu phần trăm mới dùng được?" 
 mà chưa trả lời bước ②, câu hỏi đó chưa có nghĩa.

### Slide 36–37 Tám trường hợp AI có lợi thế · sáu trường hợp AI không tốt hơn

> Trích slide 
>  " AI probably better (8): Gợi ý theo từng người · Dự đoán tương lai · Cá nhân hóa · 
>  Hiểu ngôn ngữ tự nhiên · Nhận diện cả một lớp thực thể · Phát hiện cái hiếm & biến đổi · 
>  Agent/bot cho một lĩnh vực cụ thể · Nội dung động thay giao diện tĩnh" 
>  " AI probably NOT better (6): Cần duy trì tính dự đoán được · Thông tin tĩnh, ít 
>  thay đổi · Lỗi quá tốn kém · Yêu cầu minh bạch tuyệt đối · Tối ưu tốc độ & chi phí 
>  thấp · Việc giá trị cao người dùng muốn tự làm " 
>  " Rule/heuristic dễ build, dễ giải thích, dễ debug và bảo trì hơn — nếu nó giải quyết được, 
>  đó là lựa chọn tối ưu. "

Hai danh sách này là bộ lọc cụ thể nhất của cả bài. Nhưng đọc chúng như hai danh sách rời sẽ khó nhớ 
 — **chúng đối xứng nhau theo bốn trục**:

| Trục | AI có lợi thế khi… | AI KHÔNG tốt hơn khi… |
| --- | --- | --- |
| Tính biến thiên | Đầu vào đa dạng, không viết hết rule được (ngôn ngữ tự nhiên, nhận diện lớp thực thể) | Thông tin tĩnh, ít thay đổi — cứ hiển thị trực tiếp |
| Tính cá nhân hoá | Mỗi người một nội dung khác (gợi ý, cá nhân hoá, nội dung động) | Cần duy trì tính dự đoán được — nút Home phải luôn ở một chỗ |
| Chi phí của một lần sai | Sai được, sửa được (gợi ý phim, tóm tắt nháp) | Lỗi quá tốn kém · yêu cầu minh bạch tuyệt đối |
| Ai muốn làm việc đó | Việc nhàm chán, lặp lại, không ai muốn làm | Việc giá trị cao người dùng muốn tự làm |

*"Việc giá trị cao người dùng KHÔNG muốn bị tự động hóa."* Đây không phải vấn đề kỹ thuật — 
 AI hoàn toàn làm được. Vấn đề là **làm hộ thì mất ý nghĩa**.

Ví dụ: viết lời chúc mừng sinh nhật cho đồng nghiệp, chọn quà cho người thân, viết nhận xét cho 
 nhân viên mình quản lý. Nếu người nhận biết đó do AI viết, giá trị về không — hoặc thành âm.

**Slide 43 sẽ đặt tên cho điều này** khi liệt kê lý do chọn *augment*: *"Kết quả cần trách nhiệm cá nhân / social capital"*. Nếu bài toán của bạn 
 rơi vào nhóm này, câu trả lời không phải "AI làm thay" mà là "AI giúp người làm nhanh hơn" — và ranh 
 giới đó phải viết vào ô **Boundary**.

"Rule/heuristic dễ build, dễ giải thích, dễ debug và bảo trì hơn — nếu nó giải quyết được, đó là 
 lựa chọn tối ưu."

dễ build, dễ giải thích, dễ debug, dễ bảo trì

kém hơn

Rules of ML

Building effective agents

### Slide 38–40 Khi nào AI đáng làm, và Build / Boost / Buy

> Trích slide 
>  " AI hợp khi nào: Tác vụ lặp lại nhưng có độ biến thiên vừa phải · Yêu cầu tổng hợp 
>  hoặc tìm kiếm tri thức từ nhiều nguồn · Quy trình nhiều bước phức tạp, cần tương tác nhiều công cụ. 
>  Nếu quy trình hoàn toàn có tính xác định (deterministic), rule tĩnh sẽ tối ưu hơn. " 
>  " Vì sao doanh nghiệp đầu tư: 01 Sống còn — duy trì lợi thế cạnh tranh · 02 Hiệu quả 
>  — giảm chi phí, tăng tốc độ · 03 Khám phá — tích lũy năng lực, tránh tụt hậu" 
>  " MIT CISR: Buy — giải pháp may sẵn, triển khai nhanh, ít khác biệt cạnh 
>  tranh, phụ thuộc roadmap vendor. Boost — mua model sẵn, cải tiến bằng dữ liệu nội bộ 
>  (fine-tune hoặc RAG); đòi hỏi data governance tốt. Build — tự xây model tùy biến; kiểm soát 
>  cao nhất, chi phí đắt nhất." 
>  " Thực tế: đa số đội ngũ đang ở giữa — Boost (RAG / fine-tune) "

Ba lý do đầu tư ở giữa slide đáng để ý, vì **chúng dẫn tới ba cách đánh giá thành công hoàn 
 toàn khác nhau** — và nhầm lẫn giữa chúng là nguồn của rất nhiều tranh cãi trong tổ chức:

| Động lực | Thành công đo bằng | Thất bại trông như thế nào |
| --- | --- | --- |
| Sống còn | Giữ được thị phần, không mất khách vào tay đối thủ | Làm đúng kỹ thuật nhưng quá chậm so với đối thủ |
| Hiệu quả | Chi phí giảm, thời gian xử lý giảm — đo được bằng số | Tốn nhiều hơn tiết kiệm được |
| Khám phá | Năng lực đội ngũ tăng, học được gì không làm được | Coi nó như dự án hiệu quả rồi trách nó không sinh lời |

Một dự án *khám phá* mà bị chấm bằng thước đo *hiệu quả* thì gần như chắc chắn 
 "thất bại" — vì nó không sinh ra để tiết kiệm tiền, nó sinh ra để đội ngũ học được.

Điều này liên quan trực tiếp tới câu hỏi số 5 ở [bộ phỏng vấn](#s26) ( *ai duyệt và họ nhìn chỉ số nào?* ). Nếu người duyệt nghĩ đây 
 là dự án hiệu quả còn bạn nghĩ đây là dự án khám phá, hai bên sẽ dùng hai bộ chỉ số khác nhau — 
 và bạn sẽ không bao giờ chứng minh được thành công.

Cả khoá học này thực chất dạy **Boost**: dùng model có sẵn, tăng cường bằng dữ liệu và 
 hệ thống của mình (RAG ở Ngày 7–8, fine-tune ở Ngày 21, agent ở Track 3). Không ngày nào dạy train 
 model từ đầu — đúng như slide nói, *"đa số đội ngũ đang ở giữa"*.

**Điều kiện mà slide gắn với Boost đáng chú ý:** *"đòi hỏi data governance tốt"*. Vì Boost nghĩa là đưa dữ liệu nội bộ vào model — nên câu hỏi 
 dữ liệu đi đâu, ai được xem, lưu bao lâu trở thành câu hỏi bắt buộc. Với dự án xử lý dữ liệu cá nhân 
 như **SmartCheck AI**, đây là điều kiện có tầng pháp lý chứ không chỉ kỹ thuật — 
 xem [mục áp dụng](#apply).

#### Ô kiểm tra — Chương 2 & 3

Trả lời thành tiếng trước khi mở đáp án.

**1.** Metric của bạn là "giảm thời gian xử lý ticket từ 20 phút xuống 8 phút". 
 Có vấn đề gì không? Phân tích

#### Đáp án

**Có baseline (20), có target (8), nhưng thiếu hai thứ.**

**① Thiếu measurement:** đo từ lúc nào tới lúc nào? Từ khi ticket được tạo, hay từ 
 khi nhân viên mở nó ra? Ai bấm giờ? Nếu mỗi người đo một kiểu thì con số không so sánh được.

**② Thiếu guard metric — và đây là vấn đề nghiêm trọng hơn.** "Nhanh hơn" là loại 
 metric có thể đạt được bằng cách *làm tệ đi*: xử lý ẩu, đóng ticket sớm, trả lời qua loa. 
 Toàn bộ thời gian tiết kiệm được có thể chuyển sang việc khách hàng mở lại ticket.

**Sửa theo mẫu của slide 29:** "…từ 20 phút xuống dưới 8 phút, *nhưng không làm 
 tăng tỷ lệ ticket bị mở lại trong 7 ngày*."

**Quy tắc chung:** mỗi khi metric là "nhanh hơn" hoặc "rẻ hơn", hỏi *"có thể đạt được bằng cách làm tệ đi không?"* Nếu có, cần guard metric.

**2.** Vì sao PAIR bắt buộc trả lời "automate hay augment" TRƯỚC khi định nghĩa 
 ngưỡng thành công? Hiểu

#### Đáp án

**Vì ngưỡng "đúng bao nhiêu phần trăm thì chấp nhận được" không có đáp án tuyệt đối — nó 
 phụ thuộc vào việc có người duyệt hay không.**

• **Automate** (AI gửi thẳng cho người dùng): một câu sai đi thẳng tới người dùng 
 ⇒ ngưỡng phải rất cao. 
 • **Augment** (AI soạn nháp, người duyệt): người bắt được lỗi ⇒ ngưỡng thấp hơn nhiều 
 vẫn dùng được. Và metric đúng lại đổi luôn: không phải "AI đúng bao nhiêu%" mà là *"người phải sửa bao nhiêu%"*.

**Hệ quả:** câu hỏi "AI phải chính xác bao nhiêu phần trăm mới dùng được?" là *chưa có nghĩa* nếu chưa trả lời bước ②.

**Điểm cộng:** nêu được rằng bước ② cũng định luôn mức rủi ro chấp nhận được, và đó 
 là lý do slide 44 khuyên tăng tự động hoá *theo pha* — bắt đầu ở augment, chỉ chuyển sang 
 automate cho nhóm ca đã chứng minh an toàn bằng dữ liệu.

**3.** Đội bạn muốn dùng AI viết nhận xét đánh giá nhân viên cuối năm cho quản lý. 
 Kỹ thuật hoàn toàn khả thi. Bạn nói gì? Đánh giá

#### Đáp án

**Đây rơi vào trường hợp "AI probably NOT better" thứ sáu của PAIR: việc giá trị cao mà 
 người dùng KHÔNG muốn bị tự động hoá.**

Vấn đề không phải kỹ thuật — AI viết được, thậm chí viết hay. Vấn đề là *làm hộ thì mất ý 
 nghĩa*: nhận xét đánh giá mang **trách nhiệm cá nhân và social capital** (slide 43). 
 Nếu nhân viên biết nhận xét về mình do AI viết, giá trị của nó về không hoặc thành âm — và niềm tin 
 vào quản lý bị tổn hại.

**Có thể thêm:** nó cũng chạm trường hợp *"lỗi quá tốn kém"* — một nhận xét 
 sai lệch ảnh hưởng tới lương thưởng và sự nghiệp của người thật.

**Phương án thay thế đúng — augment thay vì automate:** AI *gom* dữ liệu 
 (thành tích trong năm, feedback đã có, mục tiêu đầu năm) và trình bày có cấu trúc, để quản lý *tự viết* nhanh hơn. Việc lượng hoá vẫn do AI, việc phán xét vẫn do người.

**Và ranh giới đó phải viết vào ô Boundary:** "AI không sinh nội dung đánh giá; chỉ 
 tổng hợp dữ liệu đầu vào cho người quản lý."

---

<!-- chiron-source-span: {"source_span_id":"d32810e8-cd72-531a-98de-2ecb4e67d118","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Rule / Workflow / Agent","source_file":"slide-buoi-2.html"},"checksum":"d77bec26b073f141dd9f0bb19ab3b1f35e6736f22a810d8ba5a248fc02c5c87b"} -->

## 04 Rule / Workflow / Agent

Slide 41–56: automate vs augment, ba cấp độ giải pháp, sáu workflow pattern, và cây quyết định.

### Slide 41–44 Automate vs Augment, và tăng tự động hoá theo pha

> Trích slide 
>  " Hệ thống AI = Model + Context + Planning + Tools. Giải pháp AI là một HỆ THỐNG — 
>  model chỉ là một thành phần." 
>  " AUTOMATE — AI làm thay. Chọn khi: việc khó/nhàm chán/nguy hiểm hoặc cần scale · 
>  người dùng thiếu kiến thức hoặc khả năng tự làm · có 'đáp án đúng' mà mọi người cùng đồng thuận. 
>  Đo bằng: hiệu quả tăng · an toàn hơn · giảm việc tẻ nhạt. " 
>  " AUGMENT — AI hỗ trợ con người. Chọn khi: người dùng thích tự làm · stakes cao 
>  (tiền bạc, pháp lý, sức khỏe) · kết quả cần trách nhiệm cá nhân / social capital · sở thích khó diễn 
>  đạt thành lời. Đo bằng: mức độ thích thú · cảm giác kiểm soát · sáng tạo tăng. " 
>  " Việc đã automate vẫn gần như luôn cần human oversight — preview, edit, undo. " 
>  " Pattern #14 'Automate more when risk is low' · Pattern #17 
>  'Automate in phases'. Pha 1: AI chỉ gợi ý → Pha 2: AI soạn nháp, TA duyệt → Pha 3: AI tự động có giám 
>  sát. risk ↓ khi dữ liệu đánh giá ↑ "

Điểm quan trọng nhất và dễ bỏ qua nhất: **automate/augment là quyết định theo từng tác vụ, 
 không phải theo cả sản phẩm**. Slide ghi rõ "quyết định theo từng tác vụ" ở giữa hai cột.

|  | Automate | Augment |
| --- | --- | --- |
| Đo bằng | Hiệu quả tăng · an toàn hơn · giảm việc tẻ nhạt | Mức độ thích thú · cảm giác kiểm soát · sáng tạo tăng |
| Loại chỉ số | Khách quan, đếm được | Chủ quan, phải hỏi người dùng |
| Hệ quả cho eval | Đo được tự động từ log | Cần khảo sát, phỏng vấn — không suy ra từ log được |

Đây là chi tiết có hệ quả thật cho kế hoạch đánh giá: nếu bạn chọn *augment* mà lại chỉ đo bằng chỉ số tự động (thời gian, tỷ lệ chính xác), bạn đang đo sai thứ. 
 Người dùng có thể làm nhanh hơn mà vẫn ghét công cụ — và bạn sẽ không biết cho tới khi họ ngừng dùng.

không

preview

edit

undo

SmartCheck AI

preview

undo

Mũi tên giữa các pha ghi *"risk ↓ khi dữ liệu đánh giá ↑"*. Đây là điều kiện chuyển pha, và 
 nó là một câu rất chặt: **bạn không được lên pha vì thấy nó "chạy ổn" — bạn lên pha vì có 
 dữ liệu chứng minh**.

| Pha | AI làm gì | Dữ liệu cần có để lên pha tiếp |
| --- | --- | --- |
| 1 | Chỉ gợi ý — TA viết lại toàn bộ | Tỷ lệ gợi ý được TA dùng lại; loại câu hỏi nào gợi ý tốt |
| 2 | Soạn nháp — TA hiệu chỉnh trước khi gửi | Tỷ lệ nháp bị sửa nhiều; nhóm câu hỏi nào gần như không phải sửa |
| 3 | Tự động có giám sát — chỉ cho nhóm đã chứng minh an toàn | — |

**Chú ý pha 3 không phải "tự động cho mọi thứ"** mà là *"chỉ áp dụng cho nhóm câu hỏi đã chứng minh an toàn qua dữ liệu"*. Nghĩa là ở trạng thái 
 trưởng thành, hệ thống chạy *đồng thời cả ba pha* cho ba nhóm câu hỏi khác nhau — chứ không 
 phải cả hệ thống nhảy sang pha 3.

### Slide 45–50 Ba cấp độ giải pháp, áp cho một tình huống

> Trích slide 
>  " CẤP ĐỘ 1 — Rule / Script: Đầu vào ổn định · Logic viết được thành if/else · 
>  Cần kết quả luôn đúng 100% · Quy định pháp lý chặt. VD: tính thuế, chặn spam theo từ khóa, 
>  auto-reply theo template. " 
>  " CẤP ĐỘ 2 — LLM Feature / Workflow: Đầu vào đa dạng, không viết hết rule được · 
>  Đầu ra cần linh hoạt · Có cách đo chất lượng · Người có thể kiểm tra trước khi gửi. 
>  VD: tóm tắt email, chatbot FAQ, phân loại ticket. " 
>  " CẤP ĐỘ 3 — Agent: Nhiều bước, dùng nhiều công cụ · Tình huống thay đổi liên tục · 
>  Cần tự ra quyết định giữa các bước · Có kiểm soát rủi ro rõ ràng." 
>  " Rule/Workflow/Agent là cấp độ KỸ THUẬT — còn Automate/Augment (PAIR) là cấp độ VAI TRÒ 
>  của con người. " 
>  " Không bắt buộc nâng cấp tuần tự từ Rule lên Agent → dừng ở cấp tối giản nhất nếu đã đáp 
>  ứng mục tiêu. "

Câu in đậm thứ nhất là một phân biệt **rất dễ nhầm và hay bị hỏi**. Hai trục này *vuông góc nhau*, không phải hai tên gọi của một thứ:

|  | Augment (người quyết định cuối) | Automate (AI quyết định cuối) |
| --- | --- | --- |
| Rule | Checklist gợi ý cho nhân viên tự đối chiếu | Auto-reply theo template · chặn spam theo từ khoá |
| Workflow | AI soạn nháp, TA duyệt rồi gửi ← ô phổ biến nhất | Chatbot FAQ trả lời thẳng khách |
| Agent | Agent tổng hợp và đề xuất, TA nhấn gửi | Agent tự chạy nhiều bước, tự hành động |

Trả lời "em dùng workflow" mới nói được nửa. Trả lời **"workflow, ở chế độ augment — AI soạn 
 nháp, trợ giảng duyệt trước khi gửi"** mới đủ, vì nó nói luôn ai chịu trách nhiệm khi sai.

Và đó chính là hai trường riêng biệt trong [khung 9 
 trường](#s67): *Mức chọn* (Rule/Workflow/Agent) và *Rủi ro & HITL*. Slide tách chúng ra 
 có chủ ý.

Đây không phải mô tả năng lực của rule — đó là **tiêu chí chọn**. Nếu bài toán của 
 bạn *đòi hỏi* đúng tuyệt đối (tính thuế, tính lương, kiểm tra tuân thủ), thì AI **không phải lựa chọn**, bất kể nó chính xác 99,9%.

Nối với [slide 37](#s36): đây là trường hợp "lỗi quá tốn kém" 
 và "yêu cầu minh bạch tuyệt đối" cộng lại. Câu chốt của slide 47 nói thẳng: *"Giải pháp dựa trên Luật không thua kém AI — nếu giải quyết triệt để bài toán, đó luôn là lựa chọn 
 tối ưu."*

Rule

Workflow

Agent

Điều đáng nhận ra:

không loại trừ nhau

### Slide 51–53 Sáu workflow pattern — đọc như người làm sản phẩm

> Trích slide 
>  " CÂU HỎI QUYẾT ĐỊNH: 'Lộ trình xử lý có viết trước được không?' 
>  WORKFLOW — lộ trình do CODE ĐIỀU PHỐI. AGENT — MODEL TỰ ĐIỀU PHỐI lộ trình & cách dùng tools." 
>  " Mỗi pattern = một tradeoff: Prompt chaining — chính xác hơn (có gate) / 
>  chậm hơn (độ trễ cộng dồn). Routing — tối ưu chi phí / cần phân loại đúng ngay từ đầu. 
>  Parallelization — tin cậy hơn (vote, guardrail song song) / chi phí nhân theo số nhánh. 
>  Orchestrator-workers — xử lý được bài toán không biết trước subtasks / khó kiểm thử. 
>  Evaluator-optimizer — chất lượng tăng qua vòng lặp / cần tiêu chí chấm rõ ràng. 
>  Agent — giải được bài toán mở / chi phí cao, lỗi cộng dồn." 
>  " PM không cần code pattern — nhưng phải đọc được sơ đồ và nói được tradeoff, vì nó 
>  quyết định chi phí, độ trễ, khả năng kiểm thử và dạng lỗi — đầu vào của ô Boundary, Metric, HITL 
>  trong Problem Statement."

Câu hỏi quyết định ở đầu slide — *"lộ trình xử lý có viết trước được không?"* — là **ranh giới duy nhất giữa workflow và agent**, và nó gọn hơn nhiều so với các định nghĩa 
 dài dòng thường gặp.

| Pattern | Dùng khi | Được gì | Mất gì | Ví dụ quen thuộc |
| --- | --- | --- | --- | --- |
| Prompt chaining | Việc chia được thành bước tuần tự có thể kiểm giữa chừng | Chính xác hơn nhờ gate | Chậm hơn — độ trễ cộng dồn | Viết outline → kiểm → viết bài |
| Routing | Input có vài loại rõ rệt, mỗi loại xử lý khác | Rẻ hơn — câu dễ đi model rẻ | Phải phân loại đúng ngay từ đầu | Node phân loại của SmartCheck AI |
| Parallelization | Cần nhiều góc nhìn, hoặc chạy guardrail song song | Tin cậy hơn — vote giảm rủi ro một đầu ra sai | Chi phí nhân theo số nhánh | Guardrail + trả lời cùng lúc (Ngày 24) |
| Orchestrator-workers | Không liệt kê trước được các bước con | Xử lý được bài toán mở hơn | Khó kiểm thử, hành vi khó dự đoán | Coding agent sửa nhiều file |
| Evaluator-optimizer | Có tiêu chí chấm rõ ràng | Chất lượng tăng qua vòng lặp | Cần tiêu chí chấm — chính là reward function | Dịch → review → sửa |
| Agent | Bài toán mở, môi trường thay đổi | Giải được thứ năm cái trên không giải được | Chi phí cao, lỗi cộng dồn | SWE-bench, computer use |

Câu hỏi kiểu *"Vì sao không dùng agent cho mọi việc?"* được trả lời trọn vẹn bằng đúng cột 
 đó: chi phí cao, độ trễ lớn, khó kiểm thử, và **lỗi cộng dồn**.

**"Lỗi cộng dồn" đáng giải thích thêm:** nếu mỗi bước đúng 
 95% và agent chạy 10 bước phụ thuộc nhau, xác suất cả chuỗi đúng là 0,95¹⁰ ≈ **60%**. 
 Không bước nào "hỏng", nhưng kết quả cuối vẫn sai 4 lần trong 10. Đây là lý do agent cần *gate*, *retry hữu hạn* và *điều kiện dừng* — những thứ Ngày 23 và Ngày 25 dạy.

"PM không cần code pattern — nhưng phải đọc được sơ đồ và nói được tradeoff, vì nó quyết định 
 chi phí, độ trễ, khả năng kiểm thử và dạng lỗi."

lựa chọn pattern là một quyết định sản phẩm, không phải quyết định kỹ 
 thuật thuần tuý

Boundary

Metric

HITL

### Slide 54–56 Thang câu hỏi và cây quyết định chọn cấp độ

> Trích slide 
>  " 01 TẦN SUẤT & TÁC ĐỘNG — Nếu thấp → Xử lý thủ công hoặc hiệu chỉnh quy trình 
>  trước. 02 LOGIC — Logic xử lý có rành mạch? Nếu tường minh → Ưu tiên Rule. 
>  03 QUY TRÌNH — Quy trình có cố định? Nếu có → Workflow tích hợp AI hỗ trợ từng công 
>  đoạn. 04 TỰ THÍCH ỨNG — Chỉ khi có nhiều biến số phức tạp → Mới cân nhắc Agent. 
>  05 GIÁ TRỊ vs RỦI RO — Nếu không vượt trội → Đặt chốt HITL hoặc chọn Not Yet / No-Go." 
>  " Đi từ trên xuống — mỗi nhánh 'KHÔNG' là một lần tránh được độ phức tạp không cần thiết. "

_Sơ đồ: Cây quyết định năm bước chọn giữa xử lý thủ công, Rule, Workflow và Agent - Năm câu hỏi nối tiếp từ trên xuống. Câu một hỏi tần suất và tác động có đủ lớn không; nếu không thì xử lý thủ công hoặc sửa quy trình. Câu hai hỏi logic có rành mạch không; nếu có thì dùng Rule. Câu ba hỏi quy trình có cố định không; nếu có thì dùng Workflow. Câu bốn hỏi có cần tự thích ứng linh hoạt không; chỉ khi có mới cân nhắc Agent. Câu năm là cổng cuối, hỏi giá trị có vượt chi phí và rủi ro không; nếu không thì đặt chốt kiểm duyệt của con người hoặc chọn Not Yet hay No-Go._

Hình 2 — Cây quyết định chọn cấp độ (slide 54–55).

sửa quy trình

chấp nhận làm tay

Bốn câu đầu *chọn cấp độ*. Câu thứ năm — *"Giá trị mang lại có vượt trội chi phí & 
 rủi ro?"* — áp cho **mọi** lựa chọn ở trên, kể cả khi bạn đã chọn Rule.

Và nó có hai lối ra chứ không phải một: *thêm chốt HITL* (giữ dự án 
 nhưng giảm rủi ro), hoặc *Not Yet / No-Go* (dừng). Cách phân biệt: nếu rủi ro đến từ **việc AI sai** thì thêm người vào duyệt; nếu rủi ro đến từ **việc bài toán chưa 
 rõ hoặc dữ liệu chưa có** thì đó là Not Yet — quay lại làm rõ Problem Statement trước.

---

<!-- chiron-source-span: {"source_span_id":"6141a1ee-864b-5ad6-b3e4-56a569b7270f","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Reward function & lỗi AI","source_file":"slide-buoi-2.html"},"checksum":"16674df69762e46f950819b89c33e9c9e2ad88d7ebcdb9242e47547e61b24878"} -->

## 05 Reward function & lỗi AI

Slide 57–65: bốn ô TP/FP/FN/TN, đánh đổi precision↔recall, tiêu chí thành công hành động được, và ba loại lỗi AI.

### Slide 57 Reward function — hệ thống hiểu "đúng / sai" thế nào

> Trích slide 
>  "Reward function là công thức quyết định đâu là dự đoán 'đúng', đâu là 'sai' — và chính nó 
>  định hình trải nghiệm người dùng cuối. Vì vậy nó phải được thiết kế liên chức năng: 
>  tối thiểu UX × Product × Engineering cùng ngồi lại." 
>  " TP — Câu hỏi nghẽn thật → AI gợi ý đúng. TN — Câu hỏi đã có tài 
>  liệu sẵn → AI không can thiệp. FP — AI gợi ý câu trả lời SAI (hallucination) và gửi 
>  thẳng cho học viên → học viên đi sai hướng thực hành. FN — Học viên đang kẹt thật 
>  nhưng AI bỏ sót → học viên vẫn chờ lâu như cũ." 
>  " Chi phí của FP và FN KHÔNG đối xứng — báo cháy giả ≠ bỏ sót đám cháy. "

Bảng bốn ô này quen thuộc với ai đã học machine learning, nhưng slide dùng nó cho một mục đích khác 
 và quan trọng hơn: **bắt bạn viết ra bằng lời điều gì xảy ra với người dùng thật trong từng 
 ô**.

| Ô | Cách mô tả kỹ thuật | Cách slide mô tả |
| --- | --- | --- |
| FP | "Dương tính giả" | "AI gợi ý câu trả lời SAI và gửi thẳng cho học viên → học viên đi sai hướng thực hành " |
| FN | "Âm tính giả" | "Học viên đang kẹt thật nhưng AI bỏ sót → học viên vẫn chờ lâu như cũ " |

Đọc cột phải rồi so hai dòng, bạn *thấy ngay* chúng không tương 
 đương: FN đưa người dùng về đúng trạng thái cũ (chờ lâu — vốn đã là tình trạng hiện tại), còn FP đẩy 
 họ sang trạng thái *tệ hơn cả khi không có AI* (đi sai hướng). Không có cách mô tả kỹ thuật 
 nào cho bạn thấy điều đó.

ngưỡng nào khả thi

chi phí kinh doanh của mỗi loại lỗi

người dùng cảm nhận lỗi đó thế nào

Ngày 2

### Slide 58 Precision ↔ Recall: đánh đổi không tránh khỏi

> Trích slide 
>  " PRECISION CAO = TP / (TP + FP). Ít gợi ý — nhưng gợi ý nào cũng chắc đúng. Người 
>  dùng tin vào từng gợi ý nhận được. Hệ quả: nhiều False Negative — bỏ sót học viên đang thực sự 
>  cần giúp. " 
>  " RECALL CAO = TP / (TP + FN). Bao trọn mọi trường hợp cần giúp — không học viên 
>  nào bị bỏ lại phía sau. Hệ quả: nhiều False Positive — gợi ý sai nhiều, TA phải lọc lại thủ công. " 
>  " Không có cấu hình đúng tuyệt đối — phải test điểm cân bằng với chính người dùng. "

Hai công thức này khác nhau đúng ở **mẫu số**, và đó là toàn bộ câu chuyện:

|  | Công thức | Trả lời câu hỏi | Nhìn từ góc nào |
| --- | --- | --- | --- |
| Precision | TP / (TP + FP ) | "Trong những lần AI có gợi ý, bao nhiêu phần trăm là đúng?" | Từ phía đầu ra — người nhận gợi ý |
| Recall | TP / (TP + FN ) | "Trong những ca thực sự cần, AI bắt được bao nhiêu phần trăm?" | Từ phía nhu cầu — người cần giúp |

Mô-đun dưới đây cho bạn vặn hai núm đó và nhìn hệ quả — kèm một hiện tượng mà slide không nhắc tới 
 nhưng làm hỏng rất nhiều dự án AI thật.

#### Tương tác Precision ↔ Recall, base rate, và chi phí bất đối xứng

Đặt tỷ lệ ca thật sự cần gợi ý, chất lượng bộ phát hiện, và chi phí tương đối của hai 
 loại lỗi. Mô-đun dựng bảng bốn ô và tính tổng thiệt hại.

Mặc định: **1.000 câu hỏi**, trong đó **10%** là ca thật sự cần gợi ý. 
 Bộ phát hiện *nghe rất tốt*: bắt được **90%** ca cần giúp, và chỉ báo nhầm **10%** số ca không cần.

Đoán trước: trong tất cả các gợi ý mà AI đưa ra, bao nhiêu phần trăm là **đúng**?

#### Xem thẻ số rồi mở

**Chỉ 50%. Một nửa số gợi ý AI đưa ra là sai** — dù bộ phát hiện bắt được 90% và 
 chỉ báo nhầm 10%.

**Vì sao:** có 100 ca cần giúp và 900 ca không cần. Bắt 90% của 100 được **90 gợi ý đúng**. Báo nhầm 10% của 900 được **90 gợi ý sai**. Tổng 180 
 gợi ý, một nửa sai.

**Đây là hiện tượng base rate — và nó là cái bẫy lớn nhất của cả chương.** Vì lớp 
 "cần giúp" hiếm hơn lớp "không cần" 9 lần, nên ngay cả tỷ lệ báo nhầm *nhỏ* trên lớp đa số 
 cũng sinh ra số lỗi *lớn* về tuyệt đối.

**Thử điều đáng thử nhất:** giữ nguyên bộ phát hiện, chỉ kéo "ca thật sự cần gợi ý" 
 từ 10% lên **50%**. Precision nhảy từ 50% lên **90%** — cùng một hệ thống, 
 không sửa một dòng code nào. Kéo xuống **2%** thì precision rơi còn **15,5%**.

**Hệ quả thực hành, rất cụ thể:** khi ai đó khoe "model của tôi chính xác 90%", 
 câu hỏi đúng là *"90% theo nghĩa nào, và base rate của bạn là bao nhiêu?"* Cùng một model 
 có thể dùng được hoặc vô dụng tuỳ vào việc lớp cần bắt hiếm đến đâu.

*Thử tiếp:* đặt chi phí FP = 5, FN = 1 (gợi ý sai gây hại gấp 5 lần bỏ sót — đúng phân 
 tích ở slide 57). Rồi **siết bộ phát hiện** xuống recall 60%, báo nhầm 2%. Bắt được ít 
 ca hơn hẳn, nhưng tổng thiệt hại rơi từ **460 xuống 130** — và precision lên **76,9%**. Khi FP đắt hơn FN, *chặt chẽ hơn thắng bao phủ rộng hơn*.

- **Control - Số câu hỏi 1.000**: min `100`, max `5000`, step `100`, default `1000`

- **Control - Ca thật sự cần gợi ý 10%**: min `1`, max `60`, step `1`, default `10`

- **Control - Recall — bắt được 90% ca cần giúp**: min `10`, max `99`, step `1`, default `90`

- **Control - Báo nhầm 10% số ca không cần**: min `0`, max `50`, step `1`, default `10`

- **Control - Thiệt hại: 1 lần gợi ý SAI = 5 lần bỏ sót**: min `1`, max `20`, step `1`, default `5`

Precision

—

—

Recall

—

—

Tổng thiệt hại

—

—

Loại lỗi chi phối

—

—

precision theo tỷ lệ ca cần giúp recall (không đổi theo base rate) vị trí hiện tại

#### Xem bảng bốn ô và bảng quét base rate



#### Công thức & giới hạn của mô hình

- Với N câu hỏi và tỷ lệ ca cần giúp p: TP = recall × N·p, 
 FN = (1−recall) × N·p, FP = tỷ_lệ_báo_nhầm × N·(1−p), 
 TN = phần còn lại.
- Precision = TP/(TP+FP) · Recall = TP/(TP+FN) · 
 Tổng thiệt hại = FP × chi_phí_FP + FN × 1.
- Recall và tỷ lệ báo nhầm là hai thanh trượt độc lập ở đây, nhưng trong hệ thống 
 thật chúng gắn với nhau qua một ngưỡng: siết ngưỡng thì cả hai cùng giảm, nới thì cả hai cùng tăng. 
 Mô-đun không giả định hình dạng đường cong đó vì nó phụ thuộc model và dữ liệu của bạn — 
 hãy đọc kết quả như "nếu tôi đo được hai con số này thì hệ quả là gì".
- Chi phí là đơn vị tương đối (bỏ sót = 1), không phải tiền. Slide 57 chỉ nói 
 chi phí hai loại lỗi không đối xứng, không đưa con số.
- Giả định mọi ca cùng loại có cùng chi phí. Thực tế một số ca sai nghiêm trọng hơn hẳn các ca 
 khác — nên thiệt hại thật có đuôi dài hơn mô hình này.
- Mọi con số mặc định là giá trị minh hoạ của tài liệu này, không có trên slide. 
 Thay bằng số đo thật của bạn trước khi trích dẫn.

### Slide 59–60 Viết tiêu chí thành công mà hành động được

> Trích slide 
>  " TEMPLATE CỦA PAIR: If {chỉ số cụ thể} for {tính năng AI} {drops below / goes 
>  above} {ngưỡng có nghĩa}, we will {hành động cụ thể}. " 
>  " Ví dụ điền sẵn: Nếu tỷ lệ câu trả lời AI gợi ý bị TA sửa > 30% trong 2 tuần, 
>  ta sẽ hạ mức tự động về pha 1 (chỉ gợi ý, không gửi thẳng cho học viên)." 
>  " Checklist trước khi chốt metric: 01 Metric có ý nghĩa với MỌI người dùng không? 
>  02 Có nhóm nào bị ảnh hưởng tiêu cực không? 03 Đây là thành công của ngày 1 — còn ngày 1000 thì sao?" 
>  " Thiết lập kỳ vọng: 01 Tác động kinh doanh · 02 Sự hài lòng khách hàng · 
>  03 Ngưỡng hữu dụng (chất lượng, độ trễ, chi phí mỗi lượt)"

Template này có **bốn ô, và ô thứ tư là ô làm nên khác biệt**. Hầu hết metric mà người 
 ta viết dừng ở ô thứ ba — có chỉ số, có ngưỡng, nhưng không nói làm gì khi chạm ngưỡng.

| Ô | Trong ví dụ | Bỏ qua thì sao |
| --- | --- | --- |
| Chỉ số cụ thể | tỷ lệ câu trả lời AI bị TA sửa | Không đo được |
| Tính năng | gợi ý câu trả lời | Không biết đo phần nào của hệ thống |
| Ngưỡng có nghĩa | > 30% trong 2 tuần | Tranh cãi mỗi lần nhìn số |
| Hành động cụ thể | hạ mức tự động về pha 1 | Chạm ngưỡng rồi vẫn không ai làm gì — chỉ ghi nhận rồi thôi |

Không có nó, một ngày xấu bất thường cũng kích hoạt hành động. Đây là cùng một vấn đề mà [Ngày 25](track-3-day-25.html) gặp với cảnh báo trôi dạt: ngưỡng đặt trên nhiễu tự nhiên 
 thì báo động giả, mà báo động giả nhiều lần thì người ta tắt cảnh báo.

**Và hành động ở đây rất cụ thể:** *hạ mức tự động về 
 pha 1* — tức là quay lại một bậc trong [thang ba pha ở slide 44](#s43). Điều này chỉ 
 viết ra được nếu bạn *đã* thiết kế theo pha. Một hệ thống chỉ có hai trạng thái bật/tắt thì 
 hành động duy nhất khi có vấn đề là tắt hẳn — đắt hơn nhiều.

"Đây là thành công của ngày 1 — còn ngày 1000 thì sao?"

xấu

"lên lịch review metric định kỳ — tiêu chí thành công cũng cần được bảo trì."

### Slide 61–65 Khoảng cách demo→production, ba loại lỗi AI, và bốn pattern HITL

> Trích slide 
>  " Khoảng cách giữa Demo và Production: 01 BASELINE — đối chiếu với rule tĩnh, nhân 
>  sự hay quy trình hiện tại · 02 EVALUATION — bộ dữ liệu kiểm thử, kịch bản biên, tiêu chí nghiệm thu · 
>  03 CONTROLS — logging, fallback, rollback, nhân sự chịu trách nhiệm · 04 OPERATIONS — ai giám sát lỗi, 
>  cập nhật tri thức nền. Phản hồi chính xác trong vài lần thử chưa đủ cơ sở để triển khai. " 
>  " LOẠI 1 · CONTEXT ERRORS — Hệ thống chạy 'đúng' nhưng giả định sai về người dùng, 
>  thời điểm hoặc bối cảnh. VD: gợi ý ôn bài giữa kỳ nghỉ. 
>  LOẠI 2 · FAILSTATES — Không trả lời được. 
>  LOẠI 3 · BACKGROUND ERRORS — Cả người dùng lẫn hệ thống đều không nhận ra — 
>  'unknown unknowns'. Cần QA chủ động, không chờ người dùng báo lỗi. " 
>  " Cùng một hệ gợi ý đúng 60% — là thành công hay thất bại? Tùy vào kỳ vọng bạn đã hứa với 
>  người dùng. " 
>  " 4 pattern Human-in-the-loop: Làm rõ ý định · Minh bạch thông tin (trích dẫn 
>  nguồn) · Phê duyệt thủ công · Thiết lập ranh giới."

Ba loại lỗi này xếp theo **độ khó phát hiện tăng dần**, và loại thứ ba là loại quyết 
 định bạn có cần một quy trình QA chủ động hay không:

| Loại | Ai nhận ra | Phát hiện bằng cách nào | Ví dụ |
| --- | --- | --- | --- |
| 1 · Context error | Người dùng nhận ra ngay — họ thấy nó vô lý | Kênh phản hồi trong sản phẩm | Gợi ý ôn bài giữa kỳ nghỉ |
| 2 · Failstate | Cả hai đều biết — hệ thống báo không trả lời được | Log lỗi, đếm tỷ lệ từ chối | Không tìm thấy tài liệu liên quan |
| 3 · Background error | Không ai nhận ra | QA chủ động — phải đi tìm, không chờ báo | Câu trả lời hợp lý nhưng sai; thiên lệch với một nhóm người dùng |

"Cả người dùng lẫn hệ thống đều không nhận ra" — đây chính xác là thứ mà [Ngày 24](track-3-day-24.html) gọi là *silent degradation* và [Ngày 25](track-3-day-25.html) mô tả bằng biểu đồ "error rate = 0% nhưng faithfulness giảm 
 dần".

Nó cũng giải thích vì sao *"chờ người dùng báo lỗi"* là chiến lược 
 không đủ: người dùng chỉ báo được loại 1 và 2. Loại 3 chỉ lộ ra khi bạn **chủ động lấy mẫu và 
 chấm lại** — tức là eval, và đó là toàn bộ Ngày 14 và Ngày 24.

Slide trả lời: *"Tùy vào kỳ vọng bạn đã hứa với người dùng."* Cụ thể hoá ra:

• Nếu bạn hứa "AI sẽ trả lời thay bạn" ⇒ đúng 60% là **thất bại thảm hại** — 4 trong 
 10 lần người dùng nhận thông tin sai mà không biết. 
 • Nếu bạn hứa "AI gợi ý vài phương án để bạn chọn" ⇒ đúng 60% có thể là **rất tốt** — 
 người dùng vẫn tiết kiệm được thời gian, và họ *biết* mình đang chọn.

**Nghĩa là: bạn thiết kế được thành công bằng cách thiết kế kỳ 
 vọng.** Đó không phải mẹo vặt — nó là lý do ô *Boundary* trong Problem Statement quan 
 trọng. Viết Boundary chính là khai báo trước với người dùng: *hệ thống này làm gì, không làm gì, 
 và lỗi nào được phép xảy ra*.

① Làm rõ ý định

② Minh bạch thông tin

③ Phê duyệt thủ công

④ Thiết lập ranh giới

Chú ý ④ khác ba cái trên:

khi

AI có được phép làm việc đó không

#### Ô kiểm tra — Chương 4 & 5

Trả lời thành tiếng trước khi mở đáp án.

**1.** Model của bạn bắt được 90% ca cần hỗ trợ và chỉ báo nhầm 10% số ca không 
 cần. Đồng nghiệp nói "quá tốt, triển khai thôi". Bạn cần biết thêm gì? Phân tích

#### Đáp án

**Cần biết base rate — tỷ lệ ca thật sự cần hỗ trợ trong tổng số.** Không có nó, 
 hai con số kia không nói lên precision.

**Tính thử với 1.000 câu hỏi, base rate 10%:** có 100 ca cần giúp và 900 ca không. 
 Bắt 90% của 100 → **90 gợi ý đúng**. Báo nhầm 10% của 900 → **90 gợi ý sai**. 
 Precision = 90/180 = **50%** — một nửa số gợi ý AI đưa ra là sai.

**Cùng model, base rate 50% thì precision = 90%. Base rate 2% thì precision = 15,5%.** Không sửa một dòng code nào.

**Vì sao:** khi lớp cần bắt hiếm hơn lớp còn lại nhiều lần, ngay cả tỷ lệ báo nhầm *nhỏ* trên lớp đa số cũng sinh ra số lỗi *lớn* về tuyệt đối.

**Còn cần biết:** chi phí tương đối của FP và FN (slide 57 — "báo cháy giả ≠ bỏ sót 
 đám cháy"), và AI này chạy ở chế độ automate hay augment — vì có người duyệt thì ngưỡng chấp nhận 
 được khác hẳn.

**2.** Với case TA, gợi ý SAI gây hại gấp 5 lần bỏ sót. Nên vặn hệ thống về phía 
 precision hay recall, và cái giá là gì? Đánh giá

#### Đáp án

**Về phía precision — siết chặt, gợi ý ít nhưng chắc.**

**Kiểm chứng bằng số** (1.000 câu, base rate 10%, chi phí FP = 5, FN = 1): 
 • Cấu hình rộng (recall 90%, báo nhầm 10%): FP = 90, FN = 10 → thiệt hại **460**, 
 precision 50%. 
 • Cấu hình chặt (recall 60%, báo nhầm 2%): FP = 18, FN = 40 → thiệt hại **130**, 
 precision 76,9%.

Bắt được ít ca hơn hẳn (60% thay vì 90%) nhưng **tổng thiệt hại giảm hơn 3 lần**. 
 Khi FP đắt hơn FN, chặt chẽ thắng bao phủ.

**Cái giá phải nói rõ:** 40 học viên thực sự cần giúp bị bỏ sót thay vì 10 — 
 họ chờ lâu như cũ. Đó là *quay về hiện trạng*, không tệ hơn hiện trạng.

**Nhưng có lựa chọn thứ ba tốt hơn cả hai:** đổi từ automate sang **augment**. Nếu TA duyệt trước khi gửi, chi phí của FP tụt mạnh (TA bắt được lỗi), 
 nên bạn giữ được recall cao *mà không trả giá*. Đây đúng là lý do PAIR bắt trả lời bước ② 
 trước bước ③.

**3.** Trong ba loại lỗi AI, loại nào nguy hiểm nhất và vì sao "chờ người dùng 
 báo lỗi" không đủ? Hiểu

#### Đáp án

**Loại 3 — background errors: "cả người dùng lẫn hệ thống đều không nhận ra" 
 (unknown unknowns).**

• *Loại 1 (context error)* — người dùng nhận ra ngay vì thấy nó vô lý (gợi ý ôn bài giữa 
 kỳ nghỉ) ⇒ kênh phản hồi bắt được. 
 • *Loại 2 (failstate)* — hệ thống tự biết mình không trả lời được ⇒ log bắt được. 
 • *Loại 3* — câu trả lời trông hợp lý, không ai nghi ngờ. **Không có tín hiệu nào để 
 chờ.**

**Nên "chờ người dùng báo lỗi" chỉ bắt được loại 1 và 2.** Loại 3 chỉ lộ ra khi bạn *chủ động lấy mẫu và chấm lại* — tức là eval, và đó là lý do slide đòi "QA chủ động".

**Nối tới Track 3:** đây chính là *silent degradation* của Ngày 25 
 ("error rate = 0% nhưng faithfulness giảm dần") và là lý do Ngày 24 dành cả ngày cho việc dựng bộ 
 đo riêng. Loại 3 là loại lỗi mà cả Track 3 tồn tại để xử lý.

---

<!-- chiron-source-span: {"source_span_id":"f8230555-ad48-5ad2-921e-d3e355ee59b0","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Problem Statement hoàn chỉnh & quyết định","source_file":"slide-buoi-2.html"},"checksum":"83b4e0c9755f6f9da4c8ebccfbdd1489d44ac652c58a3f0a9556726a27b88687"} -->

## 06 Problem Statement hoàn chỉnh & quyết định

Slide 66–71: khung 9 trường, ví dụ mẫu, năm câu gate, và Go / Not Yet / No-Go.

### Slide 66–68 Chín trường: sáu yếu tố bài toán + ba yếu tố quyết định AI

> Trích slide 
>  " 6 YẾU TỐ BÀI TOÁN CỐT LÕI: Actor — đối tượng trực tiếp chịu ảnh hưởng · 
>  Workflow — quy trình vận hành hiện tại gồm các bước nào · Bottleneck — khâu nào chậm 
>  trễ, sai sót, lặp lại · Impact — tổn thất lượng hóa bằng thời gian, chi phí, SLA hoặc chất 
>  lượng · Success Metric — chỉ số đo lường cụ thể · Boundary — AI không được làm gì; 
>  khâu nào bắt buộc có con người." 
>  " 3 YẾU TỐ QUYẾT ĐỊNH AI: Điểm AI can thiệp — AI hỗ trợ hoặc tự động hóa ở 
>  bước cụ thể nào · Mức chọn — Rule / Workflow / Agent · Rủi ro & HITL — phương án 
>  xử lý khi AI sai sót và quy trình phê duyệt." 
>  " Một Problem Statement đủ 9 trường là căn cứ để ra quyết định Go, Not Yet hay No-Go. "

Chín trường này không phải một danh sách để điền cho đủ — chúng có **quan hệ phụ thuộc**, 
 và điền sai thứ tự là nguồn của phần lớn Problem Statement kém.

_Sơ đồ: Chín trường của Problem Statement và thứ tự phụ thuộc giữa chúng - Sáu trường bài toán cốt lõi xếp thành một chuỗi từ trái sang phải: Actor, Workflow, Bottleneck, Impact, Success Metric, Boundary. Ba trường quyết định AI nằm ở hàng dưới: Điểm AI can thiệp suy ra từ Bottleneck, Mức chọn Rule Workflow Agent suy ra từ Workflow và Impact, và Rủi ro cùng HITL suy ra từ Boundary. Mũi tên cho thấy ba trường quyết định AI đều phụ thuộc vào các trường bài toán, nên phải điền sáu trường trên trước. Toàn bộ chín trường dẫn tới quyết định Go, Not Yet hoặc No-Go, và tiếp đó là Eval Plan._

Hình 3 — Chín trường và thứ tự phụ thuộc (slide 67).

xuống

Điểm AI can thiệp

Mức chọn

Rủi ro & HITL

Năm ô đầu mô tả *cái đang có*. Ô Boundary mô tả **cái AI không được làm**, và 
 đó là ô duy nhất trong chín ô được viết theo hướng phủ định.

Ví dụ mẫu ở slide 68: *"AI không tự đánh giá/chấm điểm bài; chỉ hỗ trợ gợi ý làm rõ và điều 
 phối quy trình."* Câu này làm được ba việc cùng lúc:

• **Đóng khung kỳ vọng người dùng** — họ biết trước không nên tin AI về việc chấm điểm 
 (nối với [slide 64](#s64): "lỗi được định nghĩa bởi kỳ vọng"). 
 • **Giới hạn phạm vi kỹ thuật** — đội không cần xây tính năng chấm điểm. 
 • **Định trước điều gì là lỗi nghiêm trọng** — nếu AI lỡ chấm điểm, đó là vi phạm ranh 
 giới chứ không phải "câu trả lời chưa tốt".

**Cách viết Boundary tốt:** nêu *hành động cụ thể* AI 
 không được làm, không phải phẩm chất trừu tượng. "AI không được thiên vị" là vô dụng — không kiểm 
 được. "AI không gửi phản hồi trực tiếp cho học viên khi độ tin cậy dưới ngưỡng; chuyển TA duyệt" thì 
 kiểm được.

6 ô

9 ô

quyết định AI

Quick Card ở pha khám phá

PS đầy đủ ở pha quyết định

### Slide 69–71 Năm câu gate, khung Go/Not Yet/No-Go, và sáu nguyên tắc

> Trích slide 
>  " Đánh giá mức độ phù hợp của AI — 5 câu gate: 01 Nghiệp vụ có đòi hỏi xử lý ngôn 
>  ngữ, tri thức chuyên môn hoặc suy luận? 02 Dữ liệu đầu vào có đủ ngữ cảnh để AI phản hồi chính xác? 
>  03 Đã thiết lập chỉ số định lượng? 04 Hậu quả khi AI sai sót có nằm trong phạm vi kiểm soát? 
>  05 Có giải pháp thay thế đơn giản và tối ưu chi phí hơn AI không? 
>  Nếu phần lớn câu trả lời chưa rõ ràng → Quyết định: Not Yet. " 
>  " ✓ Go — Bài toán rõ ràng · Chỉ số đo lường khả thi · Điểm can thiệp AI phù hợp · 
>  Kiểm soát được rủi ro. ⏸ Not Yet — Cần bổ sung dữ liệu thực tế · Chuẩn hóa quy trình · 
>  Thiết lập chỉ số · Xác định ranh giới. ✕ No-Go — AI không mang giá trị vượt trội · 
>  Rủi ro vận hành quá cao · Giải pháp không dùng AI tối ưu hơn." 
>  " Quyết định 'Not Yet' thể hiện sự chín chắn trong tư duy thiết kế sản phẩm, không phải sự 
>  thất bại. "

Khung ba lựa chọn này mạnh hơn khung hai lựa chọn (làm / không làm) ở đúng một điểm: **nó tách "chưa đủ thông tin" ra khỏi "không nên làm"** — hai kết luận rất khác nhau nhưng 
 hay bị gộp.

| Quyết định | Nghĩa là | Việc tiếp theo | Thời hạn xem lại |
| --- | --- | --- | --- |
| ✓ Go | Đủ căn cứ để đầu tư | Chuyển sang Eval Plan, rồi triển khai | Theo mốc dự án |
| ⏸ Not Yet | Bài toán có thể đúng, nhưng ta chưa biết đủ | Việc cụ thể để lấp chỗ thiếu: đo baseline, chuẩn hoá quy trình, thu dữ liệu | Phải có — nếu không nó thành No-Go ngầm |
| ✕ No-Go | Đã đủ thông tin để kết luận không nên làm | Ghi lại lý do để lần sau không bàn lại từ đầu | Chỉ mở lại khi điều kiện đổi |

Slide gọi Not Yet là dấu hiệu chín chắn, và đúng — nhưng chỉ khi nó đi kèm **① việc cụ thể phải làm** và **② thời hạn xem lại**.

Thiếu hai thứ đó, "Not Yet" chỉ là cách nói lịch sự của "không" — dự án nằm im vô thời hạn, và 
 sáu tháng sau ai đó lại đề xuất lại từ đầu vì không ai nhớ vì sao đã hoãn.

**Viết Not Yet cho tốt:** *"Not Yet — cần đo baseline thời 
 gian xử lý trong 2 tuần và chuẩn hoá quy trình tiếp nhận. Xem lại ngày [X]."* Nhìn vào bốn gạch 
 đầu dòng của ô Not Yet trên slide sẽ thấy cả bốn đều là *việc làm được*, không phải điều kiện 
 mơ hồ — đó là chủ ý.

*"Có giải pháp thay thế đơn giản và tối ưu chi phí hơn AI không?"* — Bốn câu đầu hỏi *AI có làm được không*. Câu thứ năm hỏi *có nên không*, và nó có thể phủ quyết cả bốn 
 câu trên.

Nếu bốn câu đầu đều "có" mà câu năm cũng "có" (tồn tại phương án đơn giản 
 hơn), câu trả lời vẫn là **No-Go cho AI** — và Go cho phương án kia. Điều này nhất quán 
 với [slide 37](#s36) ("rule dễ build, dễ giải thích, dễ debug — nếu nó giải quyết được, đó 
 luôn là lựa chọn tối ưu") và với câu ② trong [cây quyết định](#f2).

① Brief mơ hồ không thay thế Problem Statement · ② Mô hình hóa workflow trước khi tích hợp AI · 
 ③ Pain point phải được lượng hóa · ④ Phức tạp không đồng nghĩa với hiệu quả · 
 ⑤ Quyết định dựa trên lập luận thực tế · ⑥ Đo reward function bằng trải nghiệm người dùng, không chỉ 
 accuracy.

**Nguyên tắc ⑥ được đánh dấu "MỚI · PAIR"** trên slide, và nó 
 là nguyên tắc dễ vi phạm nhất với người có nền kỹ thuật: accuracy là con số duy nhất dễ lấy, nên rất 
 dễ trở thành con số duy nhất được nhìn. [Mô-đun precision↔recall](#m-pr) tồn tại để cho 
 thấy vì sao một con số không đủ.

---

<!-- chiron-source-span: {"source_span_id":"674e1ef8-9e69-58c9-8048-c9834d1280fa","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Phụ lục","source_file":"slide-buoi-2.html"},"checksum":"697336af88e919180b65966e3dbb5fdc711d3dd171ece774f377d06d22ea22a0"} -->

## 07 Phụ lục

Slide 72–76: bốn nguồn gốc lỗi AI, ba lối thoát khi thất bại, và bộ 22 câu hỏi.

### Slide 72–73 Bốn nguồn gốc lỗi và ba lối thoát

> Trích slide 
>  " NGUỒN LỖI 1 Lỗi dữ liệu & dự đoán — Dữ liệu gán nhãn sai, suy luận kém, thiếu 
>  dữ liệu huấn luyện. NGUỒN LỖI 2 Lỗi đầu vào — Input bất ngờ ngoài thiết kế. 
>  NGUỒN LỖI 3 Lỗi liên quan — Độ tin cậy thấp, kết quả không liên quan. 
>  VD: gợi ý 'hoạt động vui chơi' cho chuyến đi đám tang. 
>  NGUỒN LỖI 4 Lỗi phân cấp hệ thống — Nhiều hệ thống AI cùng hoạt động và xung đột." 
>  " PATH 1 Mở kênh feedback — kể cả trên những output 'đúng'. 
>  PATH 2 Trả quyền kiểm soát khi automation thất bại — kèm đủ thông tin để họ tiếp 
>  quản. PATH 3 Giả định người dùng sẽ dùng sai — thiết kế để thất bại trở nên 
>  'an toàn, nhàm chán' thay vì thảm họa." 
>  "Nguyên tắc thông báo lỗi: 'be human, not machine'."

Ví dụ ở nguồn lỗi 3 — *gợi ý "hoạt động vui chơi" cho chuyến đi đám tang* — là ví dụ hay nhất 
 trong cả phụ lục, vì **hệ thống không sai chút nào về mặt kỹ thuật**. Nó gợi ý hoạt động 
 ở đúng thành phố, đúng khoảng thời gian, đúng sở thích đã ghi nhận. Thứ nó không biết là *vì sao* người ta đi.

| Path | Giả định về lỗi | Việc phải làm |
| --- | --- | --- |
| 1 · Mở kênh feedback | Lỗi sẽ xảy ra, và người dùng biết | Nút phản hồi — kể cả trên output đúng, vì bạn cần biết cả cái gì đang tốt |
| 2 · Trả quyền kiểm soát | Automation sẽ hỏng ở một số ca | Đường thoát sang làm tay, kèm đủ thông tin để tiếp quản |
| 3 · Giả định người dùng dùng sai | Chính bạn đã lường sai cách người ta dùng | Thiết kế sao cho thất bại "an toàn, nhàm chán" |

**Path 2 có một chi tiết dễ bỏ:** "kèm đủ thông tin để họ 
 tiếp quản". Trả quyền mà không trả ngữ cảnh thì người dùng phải làm lại từ đầu — tệ hơn cả việc 
 không có AI. Với **SmartCheck AI**, điều này rất cụ thể: khi kiosk chuyển khách sang lễ 
 tân, lễ tân có thấy được khách đã nhập gì và kẹt ở đâu không? Nếu không, khách phải kể lại từ đầu.

khi hệ thống hỏng, chuyện gì là tệ nhất có thể xảy 
 ra?

Ngày 25

"không thiết kế để 
 không hỏng, thiết kế để hỏng có kiểm soát"

### Slide 74–76 Bộ 22 câu hỏi theo hành trình

> Trích slide 
>  " #1 · PHÂN KỲ (6 câu gợi mở, slide 21) · #2 · PHỎNG VẤN 
>  (5 câu stakeholder, slide 25) · #3 · CẤU TRÚC PS (6 câu khai thác, slide 30) · 
>  #4 · GATE QUYẾT ĐỊNH (5 câu readiness, slide 69)" 
>  "22 câu hỏi theo hành trình: Phân kỳ → Phỏng vấn → Cấu trúc PS → Gate quyết định"

Bốn bộ thẻ này là **sản phẩm mang đi được nhất của cả ngày** — thứ bạn thật sự mở ra 
 dùng ở dự án tiếp theo. Chúng ánh xạ đúng vào bốn giai đoạn:

| Bộ thẻ | Dùng khi | Với ai | Đầu ra |
| --- | --- | --- | --- |
| #1 Phân kỳ (6 câu) | Đang mở rộng góc nhìn, chưa chốt bài toán | Tự hỏi mình, hoặc brainstorm nhóm | Danh sách nhiều bài toán ứng viên |
| #2 Phỏng vấn (5 câu) | Đã có ứng viên, cần hiểu bối cảnh thật | Stakeholder — người có vấn đề | Workflow, Impact, ai duyệt |
| #3 Cấu trúc PS (6 câu) | Đang viết Problem Statement | Tự hỏi, hoặc hỏi lại stakeholder | 9 trường được điền |
| #4 Gate (5 câu) | Trước khi ra quyết định cuối | Cả nhóm, có mặt người duyệt | Go / Not Yet / No-Go |

*"Có giải pháp phi AI đơn giản hơn không?"* nằm ở cả slide 30 (câu 06) và slide 69 (câu 05).

Lặp lại có chủ ý, vì câu trả lời **có thể đổi** giữa hai thời 
 điểm. Lúc mới khai thác bài toán, bạn chưa biết đủ để nói chắc. Sau khi đã điền hết 9 trường — 
 đã hiểu workflow, đã lượng hoá impact, đã biết bottleneck nằm ở bước nào — bạn thường *thấy ra* một phương án đơn giản mà lúc đầu không thấy. Đó là lý do nó phải được hỏi lại ở 
 cổng cuối.

#### Ô kiểm tra — Chương 6 & 7

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao không thể điền ô "Mức chọn (Rule/Workflow/Agent)" trước ô 
 "Workflow" và "Impact"? Hiểu

#### Đáp án

**Vì ba trường quyết định AI đều là *hệ quả* của sáu trường bài toán — mũi tên chỉ 
 đi một chiều.**

• *Mức chọn* suy ra từ **Workflow** (lộ trình có viết trước được không? — 
 câu hỏi quyết định ở slide 51) và **Impact** (tần suất/tác động có đủ lớn không? — 
 câu ① của cây quyết định). 
 • *Điểm AI can thiệp* suy ra từ **Bottleneck** — bạn phải biết bước nào nghẽn 
 mới biết cắm AI vào đâu. 
 • *Rủi ro & HITL* suy ra từ **Boundary**.

**Điền ngược lại là chẩn đoán trước khi khám** — chính là anti-pattern *Solution-first* ở slide 24. Bạn sẽ chọn cấp độ theo cảm tính hoặc theo thứ đang thời thượng, 
 rồi mô tả workflow sao cho khớp với lựa chọn đó.

**2.** Bạn kết luận "Not Yet" cho một đề xuất. Cần viết thêm gì để kết luận đó có 
 giá trị? Áp dụng

#### Đáp án

**Hai thứ: ① việc cụ thể phải làm để lấp chỗ thiếu, và ② thời hạn xem lại.**

Thiếu chúng, "Not Yet" chỉ là cách nói lịch sự của "không" — dự án nằm im vô thời hạn, và vài 
 tháng sau có người đề xuất lại từ đầu vì không ai nhớ vì sao đã hoãn.

**Viết tốt:** *"Not Yet — cần ① đo baseline thời gian xử lý trong 2 tuần, 
 ② chuẩn hoá quy trình tiếp nhận yêu cầu. Xem lại ngày [X]."*

**Chú ý bốn gạch đầu dòng của ô Not Yet trên slide 70 đều là việc làm được** — 
 bổ sung dữ liệu thực tế, chuẩn hoá quy trình, thiết lập chỉ số, xác định ranh giới. Không cái nào 
 là điều kiện mơ hồ. Đó là chủ ý: Not Yet phải chuyển được thành danh sách công việc.

**Và với No-Go, việc tương ứng là ghi lại *lý do*** — để lần sau không bàn 
 lại từ đầu, và để biết khi nào điều kiện đã đổi đủ để mở lại.

**3.** Hệ thống gợi ý "hoạt động vui chơi" cho một người đang đặt vé đi dự đám 
 tang. Không có bug nào. Đây là loại lỗi gì, và thiết kế thế nào để nó "an toàn, nhàm 
 chán"? Đánh giá

#### Đáp án

**Nguồn lỗi 3 — "lỗi liên quan" (relevance error), và cũng là context error ở slide 64: 
 hệ thống chạy đúng nhưng giả định sai về bối cảnh.**

Nó gợi ý đúng thành phố, đúng thời gian, đúng sở thích đã ghi nhận. Thứ nó không biết là *vì sao* người ta đi — và đó là thông tin hệ thống không có, không phải thông tin nó xử lý sai.

**Thiết kế để thất bại "an toàn, nhàm chán" (Path 3):**

• **Hạ mức tự tin trong cách trình bày** — "Gợi ý cho bạn" thay vì "Bạn sẽ thích". 
 Ngôn ngữ đề xuất khiêm tốn làm một gợi ý lệch trở nên vô hại thay vì vô duyên. 
 • **Không tự động hoá phần cảm xúc** — Boundary: AI gợi ý địa điểm, không viết lời chúc 
 hay đoán tâm trạng. 
 • **Cho đường thoát rõ ràng** — nút "không liên quan" (Path 1: kênh feedback), và 
 không nhồi lại gợi ý tương tự.

**Điều KHÔNG nên làm:** cố đoán mục đích chuyến đi. Đó là đi sâu hơn vào chỗ hệ 
 thống vốn không có dữ liệu — làm tăng cả rủi ro lẫn cảm giác bị theo dõi. Giảm mức tự tin rẻ hơn và 
 an toàn hơn nhiều so với tăng độ thông minh.

---

<!-- chiron-source-span: {"source_span_id":"1225bd37-a94d-5e94-9507-6e45e5479a74","locator":{"kind":"html_section","section_id":"ladder","order":10,"heading":"▤ Luyện kỹ năng cốt lõi: từ yêu cầu mơ hồ tới quyết định","source_file":"slide-buoi-2.html"},"checksum":"fc77a9ee9c8be7cedf1702fffe7dacc94464723bc9525560fb90ea4727b88da7"} -->

## ▤ Luyện kỹ năng cốt lõi: từ yêu cầu mơ hồ tới quyết định

Ba bài giảm dần giàn giáo. Làm đúng thứ tự.

① Ai đau, quy trình hiện tại mấy bước, nghẽn ở bước nào?

② Thiệt hại bao nhiêu, bằng con số?

③ Đo thành công bằng gì, baseline → target?

④ AI không được làm gì?

⑤ Cắm AI vào bước nào, cấp độ nào, ai duyệt?

chưa được phép

#### "Bên vận hành muốn một con AI đọc hoá đơn nhà cung cấp rồi tự nhập vào hệ thống kế toán"

Đọc cách *lập luận*, không chỉ đáp án.

1. Nhận ra đây là một giải pháp, không phải bài toán. "AI đọc hoá đơn rồi tự nhập" 
 đã chứa cả công nghệ (AI), cả cấp độ (tự động), cả điểm can thiệp. Áp Don Norman: vấn đề gốc có thể là 
 "kế toán mất 3 phút mỗi hoá đơn để gõ tay, mỗi tháng 400 hoá đơn" — hoặc có thể là 
 "nhập sai số tiền gây lệch sổ, mỗi tháng 5 lần". Hai vấn đề này dẫn tới hai giải pháp khác nhau. 
 Cách phân biệt: hỏi "điều gì tệ đang xảy ra?" chứ không hỏi "bạn muốn gì?"
2. Chạy bộ thẻ #2 (phỏng vấn) để lấy ①②: quy trình hiện tại mấy bước, ai bàn giao 
 cho ai, mỗi bước tốn bao lâu. Giả sử kết quả: nhận email → tải file → gõ 8 trường vào phần mềm → 
 đối chiếu với đơn đặt hàng → duyệt. Nghẽn ở bước gõ 8 trường (3 phút) và bước đối chiếu (2 phút). 
 Impact: 400 hoá đơn/tháng × 5 phút = 33 giờ/tháng.
3. Trước khi nghĩ tới AI, chạy câu ② của cây quyết định: logic có rành 
 mạch không? Nếu nhà cung cấp gửi hoá đơn theo một mẫu cố định, một parser thường 
 đọc được — Rule, chính xác 100%, không bao giờ bịa. Chỉ khi mẫu đa dạng và không viết hết 
 rule được thì mới sang Workflow. Đây là chỗ tiết kiệm lớn nhất mà người ta hay bỏ qua.
4. Boundary và HITL — quyết định trước khi chọn công nghệ. Số tiền là dữ liệu tài 
 chính: "lỗi quá tốn kém" ở slide 37 và "stakes cao: tiền bạc" ở 
 slide 43 đều chỉ về augment. Boundary: "AI điền sẵn 8 trường 
 và đánh dấu ô có độ tin cậy thấp; AI không tự lưu — kế toán bấm duyệt." 
 Success metric: "giảm thời gian mỗi hoá đơn từ 5 phút xuống dưới 2 phút, nhưng không làm tăng số 
 lần lệch sổ" — có guard metric.

Câu chốt kiểu vấn đáp "Yêu cầu đưa xuống đã là một giải pháp nên em lùi lại hỏi quy trình: 5 bước, nghẽn ở gõ tay và đối 
 chiếu, tốn 33 giờ mỗi tháng. Em kiểm câu 'logic có rành mạch không' trước — nếu mẫu hoá đơn cố định 
 thì parser thường rẻ hơn và chính xác 100%. Vì đây là dữ liệu tài chính, lỗi tốn kém, em chọn augment: 
 AI điền sẵn và đánh dấu ô không chắc, kế toán duyệt. Metric là giảm từ 5 xuống dưới 2 phút mỗi hoá 
 đơn, kèm ràng buộc không tăng số lần lệch sổ."

#### Đội bạn đã chạy pilot 6 tuần. AI phân loại ticket đúng 88%. Sếp hỏi: "triển khai toàn bộ được chưa?"

Hai bước đầu cho sẵn. Hai bước sau tự viết rồi mới mở.

1. "Đúng 88%" chưa phải một câu trả lời được. Đúng theo nghĩa nào — precision hay 
 recall? Trên phân bố ticket nào? Và slide 64 nói thẳng: cùng một hệ đúng 60% có thể 
 là thành công hoặc thất bại tuỳ kỳ vọng đã hứa.
2. Thiếu baseline. Con người phân loại đúng bao nhiêu phần trăm? Nếu người đúng 82% 
 thì 88% là cải thiện thật. Nếu người đúng 97% thì đây là bước lùi. Không có baseline thì con số 88% 
 không so được với gì — đúng anti-pattern No baseline ở slide 24.
3. ③ Ba câu hỏi bạn phải trả lời trước khi nói Go — lấy từ bộ thẻ #4? 
 (gợi ý: chú ý câu hỏi về chi phí của lỗi, và câu hỏi về phương án đơn giản hơn)
4. ④ Nếu quyết định là "Go", bạn triển khai ở chế độ nào và viết tiêu chí rút 
 lui ra sao? (gợi ý: slide 44 và template slide 59)

#### Đáp án hai bước còn lại

**③ Ba câu quan trọng nhất từ bộ thẻ #4 (slide 69):**

• **"Hậu quả khi AI sai sót có nằm trong phạm vi kiểm soát?"** — 12% ticket bị phân 
 loại sai đi đâu? Nếu ticket khẩn cấp bị xếp vào hàng chờ thường, hậu quả rất khác so với ticket 
 thường bị xếp nhầm nhóm. *Phải tách 12% đó ra xem sai kiểu gì*, không chỉ đếm. 
 • **"Đã thiết lập chỉ số định lượng?"** — 88% là chỉ số của model, không phải chỉ số của *bài toán*. Chỉ số bài toán phải là thời gian phản hồi, hoặc tỷ lệ ticket được xử lý đúng hạn. 
 • **"Có giải pháp thay thế đơn giản hơn?"** — có thể một bộ rule theo từ khoá đã đạt 80%, 
 và 8 điểm phần trăm còn lại không đáng chi phí vận hành một model.

**Và một câu ngoài bộ thẻ, từ [mô-đun](#m-pr):** base rate của từng nhóm 
 ticket là bao nhiêu? Nếu nhóm "khẩn cấp" chỉ chiếm 3% thì precision trên nhóm đó có thể rất thấp dù 
 accuracy tổng là 88%.

**④ Triển khai theo pha, không bật toàn bộ (slide 44):**

*Pha 2 — AI phân loại sẵn, người xác nhận bằng một cú bấm.* Không nhảy thẳng pha 3, vì 
 6 tuần pilot chưa đủ dữ liệu cho từng nhóm ticket. Và có thể chạy **pha 3 cho riêng nhóm ticket 
 đã chứng minh an toàn** (ví dụ nhóm "đặt lại mật khẩu" nếu nhóm đó đúng ~99%) trong khi các 
 nhóm khác vẫn ở pha 2.

**Tiêu chí rút lui theo template slide 59:** *"Nếu tỷ lệ ticket bị người phân loại 
 lại > 15% trong 2 tuần liên tiếp, ta sẽ đưa nhóm ticket đó về pha 1 (AI chỉ gợi ý)."* — có chỉ 
 số, có ngưỡng, có cửa sổ thời gian, và **có hành động cụ thể**.

#### Viết Problem Statement 9 trường cho SmartCheck AI

Không có gợi ý. Viết đủ 9 trường rồi so với [mục áp dụng](#apply).

1. Bối cảnh: kiosk check-in đặt ở sảnh khách sạn, khoảng 300 lượt check-in mỗi ngày, 
 dồn vào giờ cao điểm buổi chiều. Hiện lễ tân làm toàn bộ: hỏi thông tin, tra đặt phòng, xác minh giấy 
 tờ, giao thẻ phòng, trả lời câu hỏi lặt vặt. Giờ cao điểm khách xếp hàng.
2. Điền sáu trường bài toán trước — Actor, Workflow, Bottleneck, Impact, 
 Success Metric, Boundary. Chú ý ô Impact phải có con số, kể cả con số bạn giả định (ghi rõ 
 là giả định).
3. Rồi mới ba trường quyết định AI. Trước khi điền "Mức chọn", chạy 
 cây quyết định từ câu ① xuống — và trung thực với từng nhánh.
4. Cuối cùng: Go, Not Yet hay No-Go? Dùng bộ thẻ #4, và nếu là Not Yet thì viết kèm 
 việc cụ thể và thời hạn.

đã

"quy trình có cố định không?"

hữu ích

mục áp dụng

---

<!-- chiron-source-span: {"source_span_id":"0e838036-31d4-584a-b70e-f4f3ddca8ceb","locator":{"kind":"html_section","section_id":"misc","order":11,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"slide-buoi-2.html"},"checksum":"a8b3445f2e84aa504b055c0259ff84f34f9059a27f49cde85756b6707d95dd7d"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Mỗi thẻ: niềm tin phổ biến, lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng.

*Vì sao nghe hợp lý:* lắng nghe khách hàng là nguyên tắc cơ bản, và cãi lại yêu cầu nghe như 
 thái độ ngạo mạn.

Yêu cầu bạn nhận được **hầu như luôn đã là một giải pháp** mà ai đó tự nghĩ ra, không 
 phải một vấn đề. "Làm cho tôi chatbot AI" chứa sẵn công nghệ, cấp độ và điểm can thiệp.

Don Norman: *"Do not solve the problem I am asked to solve."* Lùi lại tìm vấn đề gốc **không** phải bác bỏ — cách làm đúng là *hỏi*, bằng bộ 5 câu ở slide 25.

[Slide 14](#s14) · [Slide 10](#s10) — "AI chatbot" chứa ít nhất tám bài toán 
 khác nhau.

*Vì sao nghe hợp lý:* AI làm được hầu như mọi việc ở mức nào đó, và dùng công nghệ mới nghe 
 như tiến bộ.

PAIR reframe hỏi *"Can AI solve this in a **unique** way?"* — không phải 
 "AI có làm được không". Nếu rule làm được, rule thắng: **dễ build, dễ giải thích, dễ debug, 
 dễ bảo trì** — bốn thứ AI kém hơn.

Sáu trường hợp AI *không* tốt hơn (slide 37) đáng nhớ, đặc biệt: *lỗi quá tốn kém*, *yêu cầu minh bạch tuyệt đối*, và *việc giá trị cao người dùng muốn tự làm*.

[Slide 26](#s26) — chữ "unique" · [Slide 37](#s36) · [cây quyết 
 định](#f2), câu ②.

*Vì sao nghe hợp lý:* Agent nghe hiện đại hơn Workflow, Workflow nghe hiện đại hơn Rule. 
 Và thang ba cấp trông như một lộ trình nâng cấp.

Slide nói thẳng: **"Không bắt buộc nâng cấp tuần tự → dừng ở cấp tối giản nhất nếu đã đáp ứng 
 mục tiêu."** Agent trả giá bằng chi phí cao, độ trễ lớn, khó kiểm thử, và **lỗi cộng dồn**.

Lỗi cộng dồn cụ thể: mỗi bước đúng 95%, chạy 10 bước phụ thuộc nhau ⇒ cả chuỗi đúng 
 0,95¹⁰ ≈ **60%**. Không bước nào "hỏng" mà kết quả vẫn sai 4/10 lần.

Một hệ trưởng thành thường chạy *cả ba cấp cùng lúc* cho ba nhóm việc khác nhau.

[Slide 50](#s45) · [Slide 51](#s51) — cột "mất gì" của mỗi pattern.

*Vì sao nghe hợp lý:* 90% nghe cao, và accuracy là con số duy nhất dễ lấy nên dễ trở thành 
 con số duy nhất được nhìn.

**Precision phụ thuộc nặng vào base rate.** Bắt được 90% ca cần giúp và chỉ báo nhầm 
 10% ca không cần — nghe rất tốt. Nhưng nếu chỉ 10% ca thật sự cần giúp, thì trong 180 gợi ý AI đưa ra, **90 cái sai**: precision chỉ 50%.

Cùng model đó ở base rate 50% cho precision 90%; ở base rate 2% cho **15,5%**. 
 Không sửa một dòng code nào.

Và **chi phí FP ≠ chi phí FN** — "báo cháy giả ≠ bỏ sót đám cháy".

[Mô-đun precision↔recall](#m-pr) — kéo thanh base rate · [Slide 57–58](#s57).

*Vì sao nghe hợp lý:* tự động hoàn toàn nghe như đích đến, còn "có người duyệt" nghe như 
 chưa xong việc.

Đây là **hai lựa chọn khác nhau về bản chất, quyết định theo từng tác vụ** — không 
 phải hai chặng của một hành trình. Có những tác vụ *phải* ở augment vĩnh viễn: stakes cao 
 (tiền bạc, pháp lý, sức khoẻ), kết quả cần trách nhiệm cá nhân, hoặc người dùng *muốn tự làm*.

Và ngay cả việc đã automate *vẫn cần* human oversight: preview, edit, undo.

Hai chế độ còn **đo bằng hai loại chỉ số khác nhau**: automate đo hiệu quả (khách 
 quan, lấy từ log); augment đo *cảm giác kiểm soát* và sự hài lòng (chủ quan, phải đi hỏi).

[Slide 43](#s43) — "quyết định theo từng tác vụ" ở giữa hai cột.

*Vì sao nghe hợp lý:* người dùng thật là nguồn phản hồi đáng tin nhất, và họ sẽ phàn nàn khi 
 có gì đó sai.

Người dùng chỉ báo được **hai trong ba loại lỗi**. Loại thứ ba — *background errors* — là loại mà **cả người dùng lẫn hệ thống đều không nhận ra**: 
 câu trả lời trông hợp lý nhưng sai, hoặc thiên lệch với một nhóm người dùng.

Không có tín hiệu nào để chờ. Loại này chỉ lộ ra khi bạn *chủ động lấy mẫu và chấm lại* — 
 tức là eval. Slide gọi đúng tên: **"cần QA chủ động, không chờ người dùng báo lỗi."**

[Slide 64](#s64) — ba loại lỗi · nối tới [Ngày 25](track-3-day-25.html) (silent degradation) và [Ngày 24](track-3-day-24.html).

---

<!-- chiron-source-span: {"source_span_id":"e3339831-cd53-5024-bd22-2ea6c9179346","locator":{"kind":"html_section","section_id":"apply","order":12,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-buoi-2.html"},"checksum":"800c520d66dd694e32a801d0855f2054f82eb657aa32bd7dd8b5dd24125ead84"} -->

## ◆ Áp dụng vào SmartCheck AI

Ngày 2 là bài áp dụng thẳng nhất cho dự án của bạn — vì nó là bài duy nhất kiểm tra *quyết định* chứ không kiểm tra cách xây.

### Problem Statement 9 trường cho SmartCheck AI

Đây là bản mẫu để bạn đối chiếu với bản tự làm ở [Bài 3](#ladder). Con số là **giả định** — đánh dấu rõ, và cần đo lại.

| Trường | Nội dung |
| --- | --- |
| Actor | Khách check-in vào giờ cao điểm (14–18h) và lễ tân phải xử lý hàng chờ. Hai nhóm này chịu tác động khác nhau — khách chờ lâu, lễ tân quá tải. |
| Workflow | Khách đến quầy → lễ tân hỏi thông tin đặt phòng → tra hệ thống → xác minh giấy tờ → thu tiền/đặt cọc nếu cần → giao thẻ phòng → trả lời câu hỏi lặt vặt (wifi, ăn sáng, giờ trả phòng). |
| Bottleneck | Hai nút thắt khác loại: ① bước tra cứu + xác minh chiếm phần lớn thời gian mỗi lượt; ② câu hỏi lặt vặt chen ngang giữa các lượt check-in, làm hàng chờ dài thêm mà không liên quan tới check-in. |
| Impact | [giả định — cần đo] 300 lượt/ngày, khoảng 60% dồn vào 4 giờ cao điểm ⇒ ~45 lượt/giờ. Nếu mỗi lượt 4 phút và có 3 quầy, năng lực là 45 lượt/giờ — đúng ngưỡng bão hoà, nên chỉ cần một lượt chậm là hàng chờ tích luỹ. |
| Success Metric | Giảm thời gian chờ trung bình giờ cao điểm từ [baseline cần đo] xuống dưới X phút, nhưng không làm tăng tỷ lệ khách phải quay lại quầy vì chưa xong việc. |
| Boundary | AI không xác minh giấy tờ tuỳ thân và không xử lý thanh toán. AI không trả lời câu hỏi ngoài phạm vi dịch vụ khách sạn (y tế, pháp lý, chỉ đường ngoài khu vực). Khi độ tin cậy thấp hoặc khách yêu cầu, chuyển lễ tân kèm ngữ cảnh đã nhập. |
| Điểm AI can thiệp | Ở nút thắt ② trước — tách luồng câu hỏi lặt vặt ra khỏi hàng chờ check-in. Và ở phần thu thập thông tin của nút thắt ①, không ở phần xác minh. |
| Mức chọn | Workflow — xem phân tích bên dưới. |
| Rủi ro & HITL | Câu hỏi thông tin chung: AI trả lời thẳng (rủi ro thấp, sai thì khách hỏi lại). Mọi thao tác chạm dữ liệu đặt phòng: AI điền sẵn, lễ tân xác nhận. Nút gọi lễ tân luôn hiện trên màn hình. |

### Chạy cây quyết định — trung thực từng nhánh

| Câu | Trả lời | Vì sao |
| --- | --- | --- |
| ① Tần suất & tác động đủ lớn? | Có | 300 lượt/ngày, dồn giờ cao điểm, năng lực đúng ngưỡng bão hoà |
| ② Logic có rành mạch? | Một phần | Câu hỏi lặt vặt (wifi, giờ ăn sáng, giờ trả phòng) hoàn toàn rành mạch ⇒ nhóm này nên là Rule, không cần AI. Phần hiểu ý định khách nói tự do thì không viết hết rule được |
| ③ Quy trình có cố định? | Có | Check-in là quy trình tuyến tính, các bước biết trước, thứ tự cố định. Lộ trình xử lý viết trước được |
| ④ Cần tự thích ứng linh hoạt? | Không | Không có tình huống nào đòi agent tự lập kế hoạch nhiều bước không lường trước |
| ⑤ Giá trị vượt chi phí & rủi ro? | Có, với Boundary ở trên | Nhưng chỉ khi AI không chạm xác minh giấy tờ và thanh toán |

Câu ③ trả lời "có" ⇒ theo cây quyết định, dừng ở **Workflow**. Câu ④ "không" ⇒ *không cần Agent*.

**Đây không phải lời chê.** Nhìn lại kiến trúc LangGraph mà bạn đã xây: node phân loại, 
 định tuyến có điều kiện, retry hữu hạn, cổng phê duyệt, finalize. **Đó chính là một 
 Workflow** — lộ trình do *code* điều phối, LLM được gọi ở từng bước để hiểu ngôn ngữ và 
 phân loại. Theo đúng định nghĩa ở [slide 51](#s51), nó không phải Agent, vì model *không* tự điều phối lộ trình.

**Vậy giá trị của việc chạy bài tập này là gì:** nó xác nhận 
 bạn đã ở đúng cấp độ, và cho bạn một câu trả lời gọn khi bị hỏi *"sao không dùng agent?"* — *"Vì lộ trình check-in viết trước được, nên workflow đủ; agent chỉ thêm chi phí, độ trễ và lỗi cộng 
 dồn mà không giải quyết thêm gì."* Đó là câu trả lời của người hiểu đánh đổi.

### Hai phát hiện đáng giá nhất từ việc điền PS

Nút thắt ① (tra cứu, xác minh) là phần *khó* và có rủi ro pháp lý. Nút thắt ② (câu hỏi lặt 
 vặt chen ngang) là phần **dễ, rủi ro thấp, và có thể giải bằng Rule thuần** — một bảng 
 FAQ với vài chục câu, không cần LLM.

**Nếu nút ② chiếm phần đáng kể lượng tương tác**, giải nó 
 trước cho ROI cao hơn hẳn: rẻ hơn, nhanh hơn, không có rủi ro bịa, và giảm hàng chờ ngay. Đây đúng là 
 câu ② của cây quyết định — *logic rành mạch thì dùng Rule*. Nhưng nó chỉ lộ ra khi bạn **vẽ workflow và tách bottleneck**, chứ không lộ ra khi bắt đầu từ "xây agent check-in".

Mọi con số trong bảng trên đều đánh dấu *[giả định]*. Bạn chưa có baseline: thời gian chờ 
 trung bình giờ cao điểm hiện là bao nhiêu? Tỷ lệ tương tác là câu hỏi lặt vặt so với check-in thật là 
 bao nhiêu?

Theo [bộ thẻ #4](#s70), câu 03 ( *"Đã thiết lập chỉ số định 
 lượng?"* ) chưa trả lời được ⇒ nghiêm khắc mà nói, trạng thái đúng là **Not Yet** cho phần mở rộng — kèm việc cụ thể: *đo baseline thời gian chờ và phân 
 loại 200 tương tác thật trong 2 tuần*. Điều đó không chặn việc tiếp tục hoàn thiện phần đã xây; 
 nó chặn việc *tuyên bố giá trị* khi chưa có gì để so.

①

②

③

---

<!-- chiron-source-span: {"source_span_id":"035013ad-4df9-5df2-aef6-98be5549dfce","locator":{"kind":"html_section","section_id":"numbers","order":13,"heading":"! Con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"slide-buoi-2.html"},"checksum":"98b40170bbca15226b7f7dc40ec094c223d77c3dbc5124227446c1cd3f173664"} -->

## ! Con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài này rất ít số — và đó là đặc điểm đáng chú ý: hầu hết con số ở đây là *ví dụ minh hoạ* cho khung, không phải kết quả nghiên cứu.

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| Weekly Report: 90 phút → dưới 30 phút; narrative 25 phút; 3 PM = 270 phút/tuần | 29 | Ví dụ minh hoạ cho cách điền Quick Card | Dùng làm khuôn mẫu cấu trúc, không phải benchmark. Điều đáng học là cách viết, không phải con số |
| Ba ví dụ metric: 90→30 phút · lỗi 20%→dưới 5% · cắt 40% câu hỏi trùng lặp | 31 | Ví dụ minh hoạ | Dùng làm khuôn: [đại lượng] từ [baseline] xuống [target]. Nếu metric của bạn điền được vào khuôn này thì nó dùng được |
| "Tỷ lệ AI gợi ý bị TA sửa > 30% trong 2 tuần → hạ về pha 1" | 59 | Ví dụ điền sẵn cho template PAIR | Ngưỡng 30% và cửa sổ 2 tuần là minh hoạ. Ngưỡng thật phải suy từ chi phí của lỗi trong bối cảnh của bạn |
| "Lớp 1000 học viên (K3 & K4)" | xuyên suốt | Case giả định của lớp học | Case xuyên suốt để minh hoạ, không phải số liệu thật |
| Rule / Workflow / Agent — "3–7 bước" cho ô Workflow | 28 | Hướng dẫn thực hành, không có nguồn | Dùng như gợi ý về độ chi tiết. Ít hơn 3 bước thì thường chưa đủ chi tiết để tìm bottleneck; nhiều hơn 7 thì nên gộp |
| Cursor / Artifact / NotebookLM | 22 | Case có thật, có dẫn nguồn | Trích được. Nhưng chú ý đây là kể lại — mỗi case còn nhiều yếu tố khác mà slide không nêu |
| Mọi con số trong mô-đun precision↔recall | — | Giá trị minh hoạ của tài liệu này | Slide 57–58 chỉ nêu công thức và đánh đổi, không đưa số. Mọi con số trong mô-đun là do bạn nhập — thay bằng số đo thật |
| "0,95¹⁰ ≈ 60%" (lỗi cộng dồn) | — | Phép tính của tài liệu này | Đúng về số học, và minh hoạ đúng ý "lỗi cộng dồn" ở slide 51. Nhưng giả định các bước độc lập — thực tế lỗi có tương quan |
| Ước lượng SmartCheck AI ở mục áp dụng (300 lượt, 60% giờ cao điểm, 4 phút/lượt) | — | Giả định chưa đo — đã đánh dấu trong bảng | Chính đây là lý do trạng thái đúng là Not Yet: ô Impact chưa có baseline thật |

Khác hẳn Ngày 1 (giá token, benchmark) hay Ngày 24–25 (ngưỡng, độ trễ), Ngày 2 đưa rất ít số liệu 
 ngoài. Lý do rất hợp lý: **bài này dạy khung, và khung thì phải điền bằng số của chính bạn**.

Nên "con số cần kiểm chứng" ở đây chủ yếu là lời nhắc: *đừng chép con số ví dụ vào Problem Statement của mình*. Một PS chép 90 phút từ ví dụ Weekly 
 Report là một PS chưa làm việc — và người chấm nhận ra ngay.

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực 
 tế đã chạy."

ô Impact và ô Success 
 Metric phải ghi rõ con số nào là đo được, con số nào là giả định

mục áp dụng

---

<!-- chiron-source-span: {"source_span_id":"08965f8c-df9f-5eac-813c-2f1c500b43ab","locator":{"kind":"html_section","section_id":"cheat","order":14,"heading":"✓ Cheat sheet ôn thi","source_file":"slide-buoi-2.html"},"checksum":"7db31b99d191aecbee14444b689f0c972995fbdd2e4b2a9e5292d4e087beb125"} -->

## ✓ Cheat sheet ôn thi

Nén 76 slide xuống một trang.

### Khung 9 trường — thứ tự điền bắt buộc

**6 yếu tố bài toán** (điền trước): Actor → Workflow → Bottleneck → Impact → 
 Success Metric → Boundary

**3 yếu tố quyết định AI** (suy ra từ trên): Điểm AI can thiệp (từ Bottleneck) · 
 Mức chọn (từ Workflow + Impact) · Rủi ro & HITL (từ Boundary)

**Bốn anti-pattern ↔ bốn ô bị thiếu:** Solution-first ↔ Workflow · 
 No baseline ↔ Impact · No evaluation ↔ Success Metric · No boundary ↔ Boundary + HITL. *Điền đủ 9 trường thì tự động không mắc cả bốn.*

### Ba khung quyết định

| Khung | Nội dung | Slide |
| --- | --- | --- |
| PAIR 3 bước | ① Có cần AI? (8 trường hợp AI tốt hơn vs 6 trường hợp không) → ② Automate hay Augment? → ③ Reward function & ngưỡng. Thứ tự bắt buộc: ③ phụ thuộc ② | 35–37, 43, 57 |
| Cây quyết định 5 câu | ① Tần suất/tác động đủ lớn? (không → thủ công) ② Logic rành mạch? (có → Rule) ③ Quy trình cố định? (có → Workflow) ④ Cần tự thích ứng? (có → Agent) ⑤ Giá trị vượt rủi ro? (không → HITL / Not Yet / No-Go) | 54–55 |
| Go / Not Yet / No-Go | Go = đủ căn cứ · Not Yet = bài toán có thể đúng nhưng chưa biết đủ ( phải kèm việc cụ thể + thời hạn ) · No-Go = đã đủ thông tin để kết luận không nên làm | 69–70 |

### Ba cấp độ × hai chế độ — bảng 2×3

|  | Augment (người quyết định cuối) | Automate (AI quyết định cuối) |
| --- | --- | --- |
| Rule | Checklist gợi ý | Auto-reply template · chặn spam từ khoá |
| Workflow | AI soạn nháp, người duyệt ← phổ biến nhất | Chatbot FAQ trả lời thẳng |
| Agent | Agent đề xuất, người nhấn gửi | Agent tự chạy, tự hành động |

**Rule/Workflow/Agent = cấp độ KỸ THUẬT · Automate/Augment = VAI TRÒ 
 của con người.** Hai trục vuông góc — trả lời đủ cả hai mới nói được ai chịu trách nhiệm khi sai. *Ranh giới Workflow ↔ Agent:* "lộ trình xử lý có viết trước được không?"

### Công thức và ngưỡng phải nhớ

**Precision** = TP/(TP+FP) — "trong những lần AI *có* gợi ý, bao nhiêu% đúng?" **Recall** = TP/(TP+FN) — "trong những ca *thực sự cần*, AI bắt được bao nhiêu%?"

**Base rate quyết định precision.** Cùng bộ phát hiện (recall 90%, báo nhầm 10%): 
 base rate 50% → precision 90% · base rate 10% → **50%** · base rate 2% → **15,5%**.

**Template tiêu chí thành công (PAIR):** *If {chỉ số} for {tính năng} 
 {drops below/goes above} {ngưỡng}, we will {hành động}.* — bốn ô, và ô **hành động** là ô hay bị bỏ nhất.

**Ba loại lỗi AI:** ① context error (người dùng nhận ra) · 
 ② failstate (hệ thống tự biết) · ③ **background error** (không ai nhận ra — cần QA chủ động). *Lỗi cộng dồn:* 10 bước mỗi bước đúng 95% ⇒ cả chuỗi đúng ~60%.

---

<!-- chiron-source-span: {"source_span_id":"bb8a264e-5ce3-55b3-80bf-392f05903a0d","locator":{"kind":"html_section","section_id":"gloss","order":15,"heading":"A–Z Từ điển thuật ngữ","source_file":"slide-buoi-2.html"},"checksum":"ed6e7d963bd19f5bf5038fb4a65636de7575a6591bec90b86f7542a2a5f96b47"} -->

## A–Z Từ điển thuật ngữ

Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện.

---

<!-- chiron-source-span: {"source_span_id":"a141287e-b5fe-5ab9-afb0-bee7e5d93fed","locator":{"kind":"html_section","section_id":"bloom","order":16,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-buoi-2.html"},"checksum":"2ca4f4bfed8c84e6be395c3aaf673bfcd35b2b6b83dc6f12bcf47e7d82b8a191"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab chiều kiểm tra mức 3–4; bài nộp 
 "Problem Statement nhóm" kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 9 trường PS, ba cấp độ giải pháp, ba kết luận Go/Not Yet/No-Go, và bốn anti-pattern. | Hình 3 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao "AI chatbot" chưa phải một bài toán, và vì sao ba 
 trường quyết định AI phải điền sau sáu trường bài toán. | Slide 10 · Slide 67 · ô kiểm tra chương 6 |
| 3 · Áp dụng | Cho một yêu cầu mơ hồ bất kỳ, chạy được bộ 5 câu phỏng vấn và điền đủ 9 trường. | Bài 1 → 2 → 3 · bộ 22 câu hỏi |
| 4 · Phân tích | Nhìn một đề xuất AI của người khác và chỉ ra ô nào đang thiếu cùng anti-pattern tương ứng. | Slide 24 — bảng anti-pattern ↔ ô PS |
| 5 · Đánh giá | Nói được "Not Yet" hoặc "No-Go" cho một đề xuất mà bạn thấy thú vị về mặt kỹ thuật — 
 kèm lý do có căn cứ và việc cụ thể để mở lại. | Slide 69–70 · mục áp dụng |

không phải

Ai đau? Đau bao nhiêu, bằng con số? Có cách nào đơn giản hơn không?

kèm lý do đủ rõ để lần 
 sau không phải bàn lại từ đầu
