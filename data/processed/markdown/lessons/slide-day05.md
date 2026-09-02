---
schema_version: 1
course_id: rag-intensive
document_id: "2594c19d-b7d2-5766-90e8-5775bb108f2a"
document_version_id: "2f32ef50-17f1-50e7-adbb-6cbf6b1ed84a"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "AI Product Thinking & Requirements — phân tích & breakdown từng slide"
source_file: "slide-day05.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-day05.html"
source_sha256: "679b5dedb21aa25d0d77d9e15f578febdc8eed926194352772c55b0906973f61"
parser_version: chiron-structured-markdown-v1
html_section_count: 21
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# AI Product Thinking & Requirements — phân tích & breakdown từng slide

> Ngày 5 có ba bộ slide chứ không phải một, và chúng bổ sung cho nhau chứ 
 không trùng lặp. Tài liệu này gộp cả ba thành một mạch duy nhất, quanh một luận điểm chung: 
 AI product không hứa "không bao giờ sai" — nó hứa rằng khi không chắc hoặc khi sai, hệ thống vẫn 
 dẫn người dùng đi đúng hướng.

<!-- chiron-source-span: {"source_span_id":"103248ad-dc8b-5658-a102-644de3b05a97","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-day05.html"},"checksum":"d7465a00e7d3340760bc90092c92dfc89b064a222e013c25841939c947480ab4"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Ngày 5 là **bài đầu tiên không dạy bạn build gì cả**. Ngày 1–4 xây khả năng kỹ thuật: 
 model, bài toán, vòng lặp ReAct, prompt và tool. Ngày 5 đặt một câu hỏi khó chịu ngay lên đầu: *agent chạy được rồi — vậy tại sao có thể không ai dùng?*

ba file

| Deck | Tên & số slide | Mạnh nhất ở | Thiếu gì |
| --- | --- | --- | --- |
| A | AI Product Thinking & Requirements AICB-P1 · 44 slide | Cấu trúc: 8 phần PRD, 5 trụ Responsible AI, risk taxonomy 5 nhóm, ma trận rủi ro, go/no-go | Không có ví dụ thật, không có con số |
| B | Thiết kế sản phẩm AI cho sự không chắc chắn AI in Action · 62 slide | Quy trình 6 bước viết PRD của Ailian Gan (Zoom), thang prototype/MVP, HAX & PAIR, trust 
 calibration, eval flow | Ít nói về rủi ro tổ chức và go/no-go |
| C | Tìm vấn đề thật, thiết kế cho lúc AI sai AI20K batch 02 · 39 slide | Ba lớp bất định, automation ladder, failure taxonomy, bug→decision→spec, 4 paths | Không đi sâu vào cấu trúc tài liệu PRD |

deck A cho khung, deck B cho quy trình, deck C cho tư duy failure

Lượt 1 · ~15 phút

Nắm luận điểm trung tâm

- Đọc deck C slide 5 & 7 — "vấn đề không phải AI yếu, vấn đề là ta 
 đối xử với AI như phần mềm thường"
- Nhìn Hình 1 — ba lớp bất định và đường đi của lỗi
- Đọc deck A slide 8 — bảng bốn khác biệt giữa software và AI product
- Mục tiêu: nói được vì sao "AI trả lời đúng" không phải một 
 acceptance criterion

Lượt 2 · ~60 phút

Chương 4, 5, 6, 8, 9

- Đây là phần bạn viết được ra giấy trong Lab 5
- Chạy cả ba mô-đun tương tác — 
 chúng lần lượt trả lời ba câu hỏi định lượng mà cả ba deck đều đặt ra nhưng không tính
- Viết thử một requirement theo mẫu deck A slide 23 rồi soi lại bằng 
 deck B slide 24

Lượt 3 · ~20 phút

Trước quiz

- 6 hiểu lầm — hiểu lầm 1 và 4 rất hay bị hỏi vấn đáp
- Cheat sheet — 8 phần PRD, 6 bước, 5 nhóm risk, 4 paths, 3 giai đoạn eval
- Từ điển — JTBD, north star, trust calibration, drift, quality gate

"Bạn đã build agent đẹp. Nhưng user không dùng. Tại sao?"

"PRD của bạn đang giúp team quyết định nhanh hơn, hay chỉ làm file dài hơn?"

tài liệu không phải mục tiêu

quyết định

---

<!-- chiron-source-span: {"source_span_id":"9663b6c5-f023-5897-a46a-8cf627fe04ac","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu — ba deck, một câu hỏi","source_file":"slide-day05.html"},"checksum":"2a188a56d6531789e5723089ee233fa9b2e5b8b48040d3c16d31bb189ad4d18e"} -->

## 00 Mở đầu — ba deck, một câu hỏi

Deck A slide 1–5 · deck B slide 1–3 · deck C slide 1–5: cả ba mở đầu bằng cùng một 
 nghịch lý, và đó không phải trùng hợp.

### Deck A · slide 2–5 Mục tiêu và deliverable: năm câu phải trả lời được

> Trích deck A 
>  " Bạn đã build agent đẹp. Nhưng user không dùng. Tại sao? " 
>  "Cuối buổi này, học viên phải trả lời được: cho ai, giá trị gì, đo bằng gì, rủi ro nào, và 
>  khi nào go/no-go. " 
>  " Deliverable: 1 PRD dài 3–5 trang + 1 Risk Matrix cho sản phẩm AI đang đề xuất. 
>  […] Risk matrix phải có ít nhất 5 rủi ro: hallucination, bias, privacy, cost, adoption"

Năm câu hỏi đó là **cấu trúc thật của cả ngày**, và đáng thuộc lòng vì chúng ánh xạ 
 gần một-một sang tám phần của PRD:

| Câu hỏi | Phần PRD tương ứng | Chương ở đây | Hỏng thì hậu quả |
| --- | --- | --- | --- |
| Cho ai? | Problem · Target User | 02 | Build the wrong thing — đúng chức năng, không ai quay lại |
| Giá trị gì? | Success Metrics tầng Business | 02 | Không chứng minh được ROI, dự án bị cắt ở quý sau |
| Đo bằng gì? | Acceptance Criteria · Non-functional | 05 · 09 | Không ai biết thế nào là done; tranh cãi kéo dài sang lúc ship |
| Rủi ro nào? | Risks | 10 | Bàn về bias và privacy lần đầu tiên vào tuần triển khai |
| Khi nào go/no-go? | — | 10 | Không có điểm dừng; sản phẩm trôi ra production vì quán tính |

Go/no-go không nằm trong 8 phần PRD.

quyết định đọc từ PRD

ta định làm gì và ở điều kiện nào

"decision note"

### Deck C · slide 3–5 Luận điểm trung tâm: vấn đề không nằm ở model

> Trích deck C 
>  "Agent chạy được rồi. Vậy tại sao có thể không ai dùng? DEMO LÀ KHẢ NĂNG KỸ THUẬT · PRODUCT 
>  LÀ GIÁ TRỊ TRONG BỐI CẢNH THẬT " 
>  " Vấn đề không phải AI yếu. Vấn đề là ta đang đối xử AI như phần mềm thường. 
>  Model ngày càng mạnh, nhưng product chỉ hữu ích khi interface, workflow và accountability giúp user 
>  khai thác đúng năng lực đó." 
>  "Insight: cùng công nghệ AI, sản phẩm khác nhau ở nơi đặt ranh giới, cách sửa output và 
>  ai chịu trách nhiệm khi AI sai. "

Câu cuối là câu đắt nhất của cả ngày. Nó nói rằng *khác biệt cạnh tranh giữa hai sản phẩm AI 
 không nằm ở model* — hai team có thể gọi cùng một API — mà ở ba quyết định sản phẩm thuần tuý. 
 Deck C minh hoạ bằng ba case mở đầu, và đáng đọc kỹ vì mỗi case hỏng ở một trong ba chỗ đó:

| Case | Chuyện gì xảy ra | Hỏng ở đâu trong ba chỗ |
| --- | --- | --- |
| Google Bard | "Một câu sai có giá thị trường" — một factual error trước công chúng thành rủi ro thương hiệu, 
 cổ phiếu và niềm tin | Ranh giới: đưa một câu chưa kiểm chứng vào một bối cảnh (demo ra mắt) mà độ 
 chịu lỗi bằng không |
| Gamma / Slide AI | "Tạo được nhưng sửa không được" — 0→80% rất nhanh, nhưng 20% cuối phải regenerate, sửa layout, 
 sửa dữ liệu → user quay lại công cụ cũ | Cách sửa output: AI tiết kiệm 80% công nhưng làm 20% còn lại đắt hơn cách 
 cũ |
| Air Canada | Chatbot bịa chính sách hoàn tiền; toà buộc hãng phải thực hiện đúng như bot đã nói | Trách nhiệm: "bot trên website là một phần của hệ thống chịu trách nhiệm" |

Gamma mới là kiểu thất bại bạn có nhiều khả 
 năng gặp nhất

không tiết kiệm được thời 
 gian thật

0,4

năm

1,0

chi phí kiểm tra

chương 07

khả năng sửa

excessive agency

Ngày 4

hành động của tổ chức

Ngày 3

---

<!-- chiron-source-span: {"source_span_id":"672c66b3-d833-5711-a7da-34991a274b52","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Vì sao AI product khác phần mềm thường","source_file":"slide-day05.html"},"checksum":"08440e93f4434bf2dbae1144b4ed5de483bbec7f23d74324c40807cfb973e8f7"} -->

## 01 Vì sao AI product khác phần mềm thường

Deck A slide 7–8 · deck B slide 29 · deck C slide 7–11. Ba deck nói cùng một điều 
 bằng ba mức độ chi tiết khác nhau — ghép lại thành bảng đầy đủ nhất.

### Deck A · slide 7–8 Hai kiểu thất bại, và bốn khác biệt

> Trích deck A 
>  " Build the wrong thing: không hiểu job-to-be-done · chọn sai persona mục tiêu · 
>  user không thấy giá trị đủ lớn để quay lại. 
>  Build the thing wrong: requirements mơ hồ · không có acceptance criteria đo được · 
>  không lường trước risk và edge cases." 
>  "Lưu ý: Với AI product, value clarity và requirement quality quan trọng không kém model 
>  quality. " 
>  "Đừng viết requirement cho AI như viết requirement cho một CRUD form. AI cần thêm 
>  quality bands, fallbacks, và trust design. "

Bảng bốn khác biệt của deck A là xương sống. Tôi giữ nguyên bốn dòng gốc và thêm cột thứ tư — *hệ quả cụ thể lên việc bạn phải viết gì*, vì đó là chỗ deck A dừng lại:

| Khía cạnh | Software thường | AI product | Phải thêm gì vào tài liệu |
| --- | --- | --- | --- |
| Output | deterministic hơn | xác suất, có biến thiên | Acceptance criteria dạng tỉ lệ, không phải nhị phân ( deck B slide 24 ) |
| Kỳ vọng user | ít mơ hồ hơn | dễ kỳ vọng quá mức hoặc hiểu sai | Capability cue, disclosure, trust calibration ( chương 07 ) |
| Definition of done | pass/fail khá rõ | cần threshold chất lượng, SLA, fallback | Quality gate + failure modes section ( chương 09 ) |
| Iteration loop | build rồi ship | build, test, observe, calibrate, re-ship | Feedback mechanism + eval set lớn dần ( chương 09 ) |

build → ship

hai

observe

calibrate

bạn phải cấp ngân sách kỹ sư 
 cho giai đoạn sau khi ship

### Deck C · slide 7–9 Ba lớp bất định, và drift khi không đổi một dòng code

> Trích deck C 
>  " INPUT UNCERTAINTY — user hỏi rất bẩn: thiếu context · dùng từ mơ hồ · đổi ý 
>  giữa chừng · cố tình prompt injection. 
>  OUTPUT UNCERTAINTY — câu trả lời không cố định: cùng intent có nhiều cách trả lời · 
>  model update làm đổi style · RAG/tool trả dữ liệu khác. 
>  PROCESS UNCERTAINTY — khó thấy vì sao: model tự suy luận · tool chain nhiều bước · 
>  user khó biết nguồn đúng/sai." 
>  " Ngay cả khi không đổi code, product vẫn có thể đổi hành vi. MODEL UPDATE: bản mới 
>  có thể giỏi hơn trung bình nhưng lệch task cũ. CONTEXT DRIFT: policy, giá, tài liệu, lịch bay, thuốc, 
>  đơn hàng thay đổi. USER DRIFT: user thật hỏi lệch scope, thiếu thông tin, dùng slang. 
>  PROMPT DRIFT: team thêm rule nhỏ, cuối cùng behavior khó đoán." 
>  "Thiết kế đúng: biến uncertainty thành quyết định product — hỏi lại lúc nào, hiện 
>  nguồn ở đâu, chuyển người khi nào, log correction ra sao."

Deck B nói cùng ý bằng một câu trích rất gọn (slide 29): *"Bạn không biết user sẽ tương tác thế 
 nào, và cũng không biết LLM sẽ phản hồi ra sao — **input, output, process, cả ba đều không chắc 
 chắn.** "* Nhưng bản của deck C hơn ở chỗ nó gán cho mỗi lớp một *thao tác thiết kế cụ 
 thể*. Đó là toàn bộ giá trị của khung này:

| Lớp bất định | Biểu hiện | Quyết định product tương ứng | Nếu bỏ qua |
| --- | --- | --- | --- |
| Input | Câu hỏi bẩn, mơ hồ, ngoài phạm vi, có ý đồ xấu | Hỏi lại lúc nào — low-confidence path, clarifying question, refusal có kiểm soát | Agent đoán bừa và trả lời trôi chảy cho một câu nó không hiểu |
| Output | Cùng input, hai lần chạy hai kết quả | Hiện nguồn ở đâu — citation, nút thử lại, đưa nhiều lựa chọn thay vì một đáp án | User báo "bug" cho một hành vi đúng về mặt kỹ thuật |
| Process | Không ai — kể cả team — biết vì sao ra kết quả đó | Chuyển người khi nào + log correction ra sao — escalation, trace, audit | Không debug được, không cải thiện được, không giải trình được |

Prompt drift đến từ 
 chính team

eval set

cách duy nhất

rổ token của Ngày 4

một

dễ xử lý nhất

thiết kế giao diện

logging và citation

### Deck C · slide 10–11 AI product không xoá lỗi — nó thiết kế đường đi cho lỗi

> Trích deck C 
>  " DETECT — biết lúc không chắc: confidence, thiếu field, dữ liệu stale, request 
>  ngoài scope. → ROUTE — chọn đường an toàn: hỏi lại, gợi ý nhiều lựa chọn, human 
>  review, từ chối. → RECOVER — cho user sửa: undo, edit, report, correction path, 
>  fallback manual. → LEARN — lưu signal: approve/reject, edit distance, retry, 
>  handoff, reason." 
>  " Nếu prototype chỉ có happy path, đó chưa phải AI product. Ít nhất phải show một 
>  path khi AI không chắc hoặc sai." 
>  Về spam filter: " Product decision: trước khi tối ưu model, phải trả lời sai kiểu nào tệ 
>  hơn với user, và hệ thống cho user recover thế nào. "

Chuỗi bốn bước này là **đóng góp gọn nhất của cả ngày** và đáng thuộc lòng, vì nó là 
 checklist duy nhất bạn cần khi đọc lại spec của chính mình. Ba lỗi thường gặp, mỗi lỗi là bỏ một mắt 
 xích:

| Bỏ mắt xích nào | Triệu chứng | Ví dụ cụ thể |
| --- | --- | --- |
| Bỏ DETECT | Hệ thống không bao giờ biết mình đang không chắc — mọi câu 
 trả lời đều tự tin như nhau | Bot trả lời câu hỏi ngoài phạm vi bằng giọng y hệt câu trong phạm vi (case Air Canada) |
| Bỏ ROUTE | Có phát hiện được nhưng chỉ có một đường: hoặc trả lời, 
 hoặc báo lỗi | Spec ghi đúng một dòng "display error message" — deck B gọi đây là sai lầm thứ ba |
| Bỏ LEARN | User sửa output mỗi ngày, và không ai biết họ sửa cái gì | Sản phẩm chạy sáu tháng, eval set vẫn là 20 case viết tay lúc đầu |

Deck C dùng **spam filter** làm ví dụ nền, và nó chọn khéo vì đây là hệ AI mà ai cũng 
 dùng hàng ngày, đủ lâu để có trực giác về cả hai kiểu sai:

|  | False positive — mail thật vào spam | False negative — spam vào inbox |
| --- | --- | --- |
| Thiệt hại | "User không thấy mail quan trọng · có thể mất cơ hội, lịch hẹn, hoá đơn" | "User thấy và xoá được · gây phiền nhưng recover dễ hơn" |
| Ai phát hiện | Không ai — mail nằm im trong thư mục 
 không ai mở | Chính user, ngay lập tức |
| RECOVER là gì | "Cần undo, whitelist, review folder" | Nút "báo spam" — đã có sẵn |
| Ngoại lệ | — | "Rủi ro tăng nếu phishing/lừa đảo" — lúc đó FN cũng thành nguy hiểm |

"ai phát hiện"

tồn tại

vô hình

loại lỗi mà user không tự phát hiện được thì phải 
 được thiết kế một bề mặt để nhìn thấy.

"User THẤY & sửa được"

"User KHÔNG thấy"

chương 08

_Sơ đồ: Ba lớp bất định của AI product và chuỗi bốn bước xử lý lỗi - Phần trên: ba lớp bất định xếp theo dòng chảy của một yêu cầu — input uncertainty khi user hỏi mơ hồ hoặc thiếu context, process uncertainty khi model suy luận qua nhiều bước tool mà không ai nhìn thấy, và output uncertainty khi cùng một yêu cầu cho ra các câu trả lời khác nhau. Mỗi lớp được gán một quyết định sản phẩm tương ứng: hỏi lại, ghi log và hiện nguồn, và cho phép thử lại. Phần dưới: chuỗi bốn bước xử lý lỗi gồm detect khi hệ thống nhận ra mình không chắc, route để chọn đường an toàn như hỏi lại hoặc chuyển người thật, recover để user sửa được kết quả, và learn để lưu tín hiệu sửa chữa quay về bộ đánh giá. Một mũi tên khép vòng từ learn trở lại detect cho thấy đây là chu trình chứ không phải đường thẳng._

Hình 1 — ba lớp bất định, và bốn bước xử lý lỗi.

correction phải chảy ngược về eval set

**Kiểm tra 1** Một team nói: "Chúng tôi đã xử lý bất định rồi — đặt temperature = 0 
 nên output ổn định." Họ đã bịt được lớp nào và bỏ sót lớp nào?

#### Xem đáp án

Họ bịt được **một phần** của lớp output — và cũng chỉ một phần: temperature 0 làm giảm 
 biến thiên ở cùng một model, nhưng không cứu được *model update* hay *RAG trả dữ liệu 
 khác*, hai nguồn biến thiên còn lại mà deck C liệt kê ở chính lớp đó.

Họ **không đụng gì** tới hai lớp còn lại: user vẫn hỏi mơ hồ (input), và vẫn không ai 
 nhìn được vì sao ra kết quả đó (process). Temperature là một nút vặn của model; hai lớp kia cần *thiết kế giao diện* và *logging*.

*Cách trả lời gọn khi vấn đáp:* "Temperature 0 chỉ chạm lớp output, và chỉ chạm phần biến 
 thiên trong một model cố định. Input uncertainty phải giải bằng UI — hỏi lại, pre-set prompt. 
 Process uncertainty phải giải bằng citation và trace. Không nút vặn nào của model làm hộ hai việc đó."

---

<!-- chiron-source-span: {"source_span_id":"d2847296-bcda-5885-bf81-1b18082ff081","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Tìm đúng bài toán trước khi build","source_file":"slide-day05.html"},"checksum":"ed023e15e965850e7999fb621b9c9768c0886f1ad9b340362ddb7dddc6798378"} -->

## 02 Tìm đúng bài toán trước khi build

Deck A slide 9–11 · deck B slide 18–19 · deck C slide 33–35. Ba cách tiếp cận khác 
 nhau tới cùng một việc: chọn cái đinh trước khi vung búa.

### Deck A · slide 9–10 Jobs-to-be-Done: ba chiều, không chỉ chiều chức năng

> Trích deck A 
>  " User muốn hoàn thành việc gì? Ví dụ: trả lời ticket nhanh hơn. 
>  User muốn cảm thấy thế nào? Tự tin hơn, ít sợ sai hơn. 
>  User muốn được nhìn nhận ra sao? Trông chuyên nghiệp hơn, phản hồi nhanh hơn." 
>  "Lưu ý: Nếu chỉ nhìn functional job, bạn dễ build một agent 'đúng chức năng' nhưng không 
>  được dùng lại. " 
>  "Ưu tiên use case trả lời được 4 câu: ai dùng, đau ở đâu, thành công đo bằng gì, fail gây 
>  hại gì. "

Ba chiều JTBD (functional · emotional · social) không phải trang trí. Với AI product chúng dự đoán 
 được *hành vi từ chối* — thứ mà chiều chức năng hoàn toàn không nhìn thấy:

| Chiều | Câu hỏi | Nếu bỏ qua, triệu chứng là gì |
| --- | --- | --- |
| Functional | Hoàn thành việc gì? | Agent giải sai bài toán — dễ phát hiện nhất, và cũng ít gặp nhất |
| Emotional | Muốn cảm thấy thế nào? | Agent đúng nhưng user vẫn kiểm tra lại từ đầu. Nếu JTBD là "ít sợ sai hơn" mà AI không 
 cho citation, user vẫn phải mở văn bản gốc — công việc không giảm, chỉ đổi hình 
 dạng |
| Social | Muốn được nhìn nhận ra sao? | User không dám dùng vì sợ mang tiếng "để AI làm hộ". Rất thật trong các nghề mà chất lượng cá 
 nhân là danh tiếng — luật sư, bác sĩ, giáo viên |

Agent 1

Agent 2

functional

emotional

citation không phải một "tính năng thêm"

Bốn câu sàng lọc use case của deck A đáng dùng làm bộ lọc thật. Áp thử vào bốn use case mà chính 
 deck A nêu:

| Use case | Ai dùng | Đau ở đâu | Thành công đo bằng gì | Fail gây hại gì |
| --- | --- | --- | --- | --- |
| AI support agent | Nhân viên hỗ trợ | Trả lời chậm, không nhất quán giữa người | First-response resolution rate | Trả lời sai cho khách → uy tín, có thể pháp lý |
| Tra cứu chính sách nội bộ | HR staff, line manager | Tìm văn bản lâu, hỏi lặp lại | Time-to-answer đúng nguồn | Diễn giải sai chính sách → tranh chấp lao động |
| Ticket routing | Ops lead | Queue sai nhóm, thời gian chờ dài | Đúng nhóm ngay lần đầu | Ticket khẩn vào nhầm queue → SLA vỡ |
| AI sales assistant | Sales rep | Sàng lead thủ công | Tỉ lệ lead đủ điều kiện | Bỏ sót lead tốt → mất doanh thu (âm thầm) |

không

hữu hình và có người phát hiện

vô hình

chương 08

trong bước chọn use case

### Deck A · slide 11 North star metric — và cảnh báo đi kèm mỗi cái

> Trích deck A 
>  "AI support agent → first-response resolution rate · cảnh báo: đừng chỉ đo số 
>  lượng trả lời. 
>  Tra cứu văn bản → time-to-answer đúng nguồn · đừng chỉ đo độ dài câu trả lời. 
>  Ticket routing → đúng nhóm ngay từ lần đầu · đừng chỉ đo tốc độ phân loại. 
>  AI sales assistant → tỷ lệ lead đủ điều kiện · đừng chỉ đo số lead được chấm 
>  điểm." 
>  " Define success before scope "

Bốn cảnh báo này có **một cấu trúc chung** mà deck A không chỉ ra, và một khi thấy rồi 
 thì bạn tự sinh được cảnh báo cho use case của mình:

```text
Metric xấu  = đếm HOẠT ĐỘNG của AI   (số trả lời, độ dài, tốc độ, số lead chấm điểm)
Metric tốt  = đếm KẾT QUẢ cho user   (giải quyết xong, đúng nguồn, đúng nhóm, đủ điều kiện)

Dấu hiệu nhận ra metric xấu: AI có thể làm nó tăng mà không cần đúng.
    "số lượng trả lời"  ↑ bằng cách trả lời cả câu không nên trả lời
    "độ dài câu trả lời" ↑ bằng cách viết dài dòng
    "tốc độ phân loại"   ↑ bằng cách đoán bừa
    "số lead chấm điểm"  ↑ bằng cách chấm hết mọi lead
```

chậm

ngay lập tức và triệt để

AI trả lời cả những câu nó 
 không nên trả lời

deck C slide 20

tạo ra

### Deck B · slide 18–19 Bước ① và ② của Ailian Gan: tìm đinh, rồi phát biểu vấn đề không nhắc chữ AI

> Trích deck B 
>  " ① Identify good use cases: AI là cây búa đi tìm cái đinh. Team thường được giao 
>  sẵn 'cây búa' AI rồi mới đi tìm bài toán. Hãy tìm đinh tốt — đừng đóng lỗ lung tung." 
>  " B · BRAINSTORM THEO LLM SKILLS — User need nào cải thiện được bằng các skill của 
>  LLM: summarization · question-answering · content generation · personalization · data processing · 
>  predictive insights." 
>  " C · CHỌN THEO GIÁ TRỊ + MOAT — Cái nào tạo competitive moat: data nào (để train, 
>  để generate output) mà đối thủ có model tốt cũng không copy được?" 
>  " ② Articulate the problem: đừng nhắc chữ AI. Problem statement KHÔNG được nhắc chữ 
>  AI — vấn đề của user không phải là 'đời tôi thiếu AI'."

Ví dụ Zoom mà deck B dùng xuyên suốt là ví dụ dạy học tốt vì nó cho thấy *vì sao ba use case kia 
 bị loại*, chứ không chỉ vì sao cái thắng được chọn:

| Use case cân nhắc | Đánh giá của PM Zoom | Điều kiện còn thiếu |
| --- | --- | --- |
| Scheduling | "khả thi, nhưng cần biết availability & preferences của mọi người" | Dữ liệu — Zoom không có |
| Draft agendas | "khả thi, nhưng cần input data đủ tốt mới đề xuất được agenda hay" | Chất lượng input — rác vào, rác ra |
| Brainstorm ideas | "khả thi, nhưng Zoom đã có sẵn sản phẩm whiteboard" | Chỗ trống — trùng sản phẩm sẵn có |
| Extract takeaways | THẮNG — "Zoom đã có sẵn transcript · LLM rất giỏi tóm tắt · app bên thứ ba đang 
 bán note-taking → market demand rõ ràng" | — (đủ cả ba: dữ liệu sẵn · kỹ năng khớp · nhu cầu đã được chứng minh) |

① Dữ liệu bạn đã có sẵn

moat

② Kỹ năng LLM khớp thẳng với việc

③ Nhu cầu đã được ai đó chứng minh bằng tiền

duy nhất

Bước ② — ba mức độ của một problem statement — là phần đáng chép nguyên vào sổ tay:

| Mức | Problem statement | Vì sao ở mức đó |
| --- | --- | --- |
| ✕ Bad | "Users don't have an automated AI notetaker for all their meetings." | " Phát biểu thiếu solution = vấn đề. Giả định user cần một AI notetaker — nhưng tại sao? 
 Không mô tả vấn đề nền hay mục tiêu của user." |
| ◐ Good | "Users want a record of the key points from their meetings, but it is tedious and distracting to 
 take thorough manual notes for every meeting." | " Tưởng tượng được nhiều giải pháp: thuê intern ghi note? Bắt cả team ghi note chung? 
 AI chỉ là phương án scalable và rẻ hơn." |
| ✓ Even better | "…a record of discussion topics, key decisions, and action items … In addition, 
 users sometimes cannot attend a meeting, and they want a quick way to catch up." | Gợi ý nội dung cần focus, use case phụ (người vắng mặt), và cách consume — "phải nhanh, dễ đọc" |

Xoá mọi từ liên quan tới AI khỏi câu. Nếu câu còn lại vô nghĩa, bạn chưa có problem 
 statement — bạn có một solution statement.

thiếu

chật vật

"thiếu công cụ X"

"việc Y 
 đang tốn kém"

### Deck C · slide 33–35 Research toolkit và chuỗi Evidence → Insight → Opportunity → Build slice

> Trích deck C 
>  " 1 · TỰ TRẢI NGHIỆM — mở app, làm task thật, ghi lại moment mình kẹt. Nhanh nhất 
>  nhưng chỉ là một góc nhìn. 2 · TÌM USER THẬT — tìm nơi user than phiền; hỏi 'lần gần 
>  nhất bạn bị kẹt là khi nào?'. 3 · CÀO REVIEW — lấy 30–50 review App Store/Play, dùng 
>  AI gom nhóm than phiền, chọn top failure mode có bằng chứng." 
>  "Câu neo: bạn không phải lúc nào cũng là user thật. " 
>  " EVIDENCE (quote, screenshot, review cluster) → INSIGHT (user 
>  không thiếu thông tin; họ thiếu hướng dẫn quyết định) → OPPORTUNITY (hỏi 3 câu, gợi 
>  2–3 lựa chọn, cho user sửa) → BUILD SLICE (một flow: input → AI → output → failure 
>  path)" 
>  "Không nhận: 'AI assistant cho healthcare'. Nhận: 'người mới khám không biết chọn chuyên 
>  khoa, AI hỏi 3 câu và gợi 2 chuyên khoa, red flag chuyển người'."

Cặp *"không nhận / nhận"* ở cuối là bài kiểm tra tốt nhất trong cả deck C. Bốn thứ được thêm 
 vào khi đi từ trái sang phải, và **thiếu bất kỳ thứ nào thì vẫn là "AI assistant cho 
 healthcare"**:

| # | Thứ được thêm | Trong ví dụ | Nếu thiếu |
| --- | --- | --- | --- |
| 1 | Một user cụ thể | "người mới khám" (không phải "bệnh nhân") | Không biết thiết kế cho ai — AI literacy, ngưỡng chấp nhận sai đều khác nhau |
| 2 | Một task cụ thể | "không biết chọn chuyên khoa" | Scope trôi; mỗi tuần thêm một tính năng |
| 3 | Một AI decision cụ thể | "hỏi 3 câu và gợi 2 chuyên khoa" | Không biết eval cái gì, không biết đo cái gì |
| 4 | Một failure path cụ thể | "red flag chuyển người" | Prototype chỉ có happy path → "chưa phải AI product" (slide 11) |

hai

truyền đạt sự không chắc chắn mà không cần hiện con số

"User không cần biết 0.71 hay 0.84 — user cần thấy hệ 
 thống cư xử khác nhau khi độ chắc khác nhau."

chính là

chương 07

AI literacy

Why Johnny Can't Prompt

khái quát hoá quá mức từ một vài lỗi nhỏ và bỏ cuộc sớm

### Deck A · slide 17–19 User research đặc thù cho AI: bốn câu hỏi, hai chiều persona, ba loại tín hiệu

> Trích deck A 
>  " 1. User muốn AI tự làm đến mức nào, và ở bước nào họ muốn giữ quyền kiểm soát? 
>  2. User tin AI dựa trên điều gì: tốc độ, citation, confidence, hay kết quả thực tế? 
>  3. Khi AI sai, user muốn fallback nào: chỉnh tay, escalate người thật, hay thử lại? 
>  4. User đang kỳ vọng AI là trợ lý, copilot, hay người thay thế?" 
>  "Lưu ý: Nhiều AI product fail vì team ngầm giả định user muốn 'full automation', trong khi 
>  thực tế user chỉ muốn decision support. " 
>  " Persona cho AI cần thêm: AI literacy level · mức sẵn sàng tin automation · 
>  ngưỡng chấp nhận sai · mức độ muốn explainability." 
>  " Explicit feedback (thumbs up/down, rating) — xác định chất lượng user cảm nhận. 
>  Behavioral signal (copy, rephrase, override, abandon) — phát hiện trust, friction, và 
>  điểm nghẽn. Outcome signal (resolved, booked, escalated) — nối AI quality với business 
>  value." 
>  " Nếu không biết sẽ thu feedback gì sau khi launch, bạn đang viết requirement cho một hệ 
>  thống khó học và khó cải thiện. "

Bốn câu hỏi này hỏi đúng bốn tham số mà các chương sau sẽ dùng để tính toán — đây là chỗ chúng được *thu thập*:

| Câu hỏi research | Nó xác định tham số nào | Dùng ở đâu trong tài liệu này |
| --- | --- | --- |
| 1 · Tự làm đến mức nào? | Mức tự chủ mong muốn — act / ask / inaction | Mô-đun act/ask · chương 04 |
| 2 · Tin AI dựa trên điều gì? | Cơ chế explainability cần xây | Chương 07 — trust calibration |
| 3 · Khi AI sai, muốn fallback nào? | Chọn tầng fallback nào trong ba tầng | Deck B slide 24 · chương 07 |
| 4 · Kỳ vọng AI là gì? | C — chi phí khi sai, và cả kỳ vọng ban đầu | Chương 04 · Hình 2 |

thái độ

ràng buộc

trong cùng một sản phẩm

Hệ quả:

hỏi user họ đang làm gì

| Loại | Ví dụ | Độ phủ | Độ tin |
| --- | --- | --- | --- |
| Explicit | Thumbs up/down, rating | Rất thấp — chỉ vài% user bấm, và lệch về người rất hài lòng hoặc rất bực | Trung bình — nói được cảm nhận, không nói được vì sao |
| Behavioral | Copy, rephrase, override, abandon | 100% — mọi user đều tạo ra tín hiệu này mà không cần làm gì thêm | Cao — hành vi không nói dối |
| Outcome | Resolved, booked, escalated | Cao | Cao nhất, nhưng chậm và bị nhiễu bởi nhiều yếu tố khác |

yếu nhất

"nếu không biết sẽ thu feedback gì sau khi 
 launch, bạn đang viết requirement cho một hệ thống khó học và khó cải thiện."

"ta sẽ log gì"

---

<!-- chiron-source-span: {"source_span_id":"5e7becce-f6fc-5c41-b310-5ffce45f28cf","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Prototype & MVP — cách rẻ nhất để test một giả thuyết","source_file":"slide-day05.html"},"checksum":"07176333ee6f22c2dede9b8d4b748ba3131a0ccdf9a5ed16b87660d3cdcc2022"} -->

## 03 Prototype & MVP — cách rẻ nhất để test một giả thuyết

Deck B slide 4–16. Đây là phần deck A và C hoàn toàn không có, và là phần thực dụng 
 nhất của cả ngày.

### Deck B · slide 5–8 Leap of faith assumptions, và thang fidelity đã dịch chuyển

> Trích deck B 
>  " Leap of Faith Assumptions (The Lean Startup): Will the customer buy this, or 
>  choose to use it? ( Value risk ) · Can the user figure out how to use it? ( Usability 
>  risk ) · Can we build it? ( Feasibility risk ) · Does this solution work for our business? 
>  ( Business viability risk )" 
>  " Build software: từ rất đắt → rẻ hơn nhiều. Toàn bộ product lifecycle được thiết 
>  kế quanh việc 'build là đắt' — khi build rẻ đi, lifecycle đó phải đổi theo. Cùng một thang 'signal vs 
>  effort' — MVP và prototype giờ nằm ở chỗ trước đây chỉ có wireframe. " 
>  " Double diamond không đổi — tốc độ đi qua nó thay đổi hoàn toàn. Nhiều ý tưởng 
>  giải pháp hơn · đồng thuận stakeholder nhanh hơn · deliver nhanh hơn, lấy feedback nhanh hơn." 
>  " If you aren't prototyping with AI, you're doing it wrong " — Microsoft CPO

Bốn loại rủi ro của Lean Startup đáng nhớ vì **chúng cần bốn loại prototype khác nhau**, 
 và nhầm lẫn giữa chúng là lý do người ta build một prototype đẹp mà không học được gì:

| Rủi ro | Câu hỏi | Test rẻ nhất là gì | Prototype đẹp có trả lời được không |
| --- | --- | --- | --- |
| Value | Khách có chọn dùng không? | Landing page + ads · Wizard of Oz · bán trước khi có sản phẩm | Không. Người xem demo luôn gật đầu lịch sự |
| Usability | User tự biết cách dùng không? | Clickable prototype, test với 5 người, không hướng dẫn gì | Có — đây đúng là việc của prototype |
| Feasibility | Ta build được không? | Technical spike: chạy thử 20 case thật qua model, xem chất lượng | Không — prototype UI không nói gì về chất lượng AI |
| Business viability | Hợp với business không? | Tính cost/request × volume; kiểm tra ràng buộc pháp lý, data residency | Không. Đây là bảng tính, không phải màn hình |

nhị phân

phân bố

"chất lượng đạt bao nhiêu phần trăm trên loại input nào"

technical spike cho AI phải chạy trên dữ liệu thật, không phải dữ 
 liệu mẫu.

chương 09

một test case là demo, một distribution mới là product

Thang fidelity bốn bậc là thứ nên thuộc, và deck B thêm một quan sát quan trọng — *các bậc vẫn 
 còn nguyên nhưng chi phí của chúng đã sụp đổ*:

| Bậc | Kiểm tra điều gì | Câu hỏi trả lời được |
| --- | --- | --- |
| 01 Sketch | Ý tưởng thô | Có đáng theo đuổi không? |
| 02 Wireframe functional · structure | Luồng & cấu trúc | "Đúng luồng / workflow chưa?" |
| 03 Mockup style · color | Hình thức | "Người dùng có thấy rõ tính năng không?" · "Mô phỏng trông như thật" |
| 04 Prototype interactive · clickable | Trải nghiệm | "Test với người dùng cuối" |

"Toàn bộ product lifecycle được thiết kế quanh việc 'build là đắt' — khi build rẻ đi, lifecycle 
 đó phải đổi theo."

chỉ vì

tranh luận về nó tốn hơn 
 là build nó

build giao diện

không

### Deck B · slide 11–16 Wizard of Oz: hai case, và vì sao chúng thuyết phục

> Trích deck B 
>  " DoorDash — 'Palo Alto Delivery' 2013. Giả định: 'Có ai cần giao đồ ăn từ quán 
>  địa phương không?'. MVP: một trang web tĩnh + PDF menu 8 quán (không xin phép), để một số Google 
>  Voice chung (đổ chuông máy cả 4 founder). Có cuộc gọi → tự gọi đặt món, tự lái đi giao, lấy $6. Dán 
>  tờ rơi quanh Stanford — đơn đầu tiên từ khách lạ qua Google sau 45 phút. " 
>  " AI Wizard of Oz MVP. Giả định rủi ro nhất: 'Người ta có trả tiền cho AI ghi 
>  chú họp không?' MVP: 2 founder tham gia vào cuộc họp dưới danh nghĩa một bot AI tên 'Fred' 
>  (giả kiểu Siri), ngồi gõ note bằng tay. Làm tay hơn 100 cuộc họp, thu 
>  $100/tháng cho AI. Kết quả: seed $5M 10/2019 → kỳ lân $1 tỷ 6/2025." 
>  " Lát cắt mỏng xuyên suốt, không phải một tầng hoàn chỉnh. Không build 'bánh xe 
>  trước, xe hơi sau'. Build chiếc xe đạp chạy được ngay — nhỏ nhưng đủ cả 4 tầng."

Cả hai case đều có **một đặc điểm chung mà slide không tô đậm**: giả thuyết được test là *value risk*, và cách test là **lấy tiền thật**. Không khảo sát, không phỏng vấn, 
 không demo. DoorDash lấy $6 mỗi đơn; Fireflies thu $100/tháng.

value risk

nói thích

để lại email

dùng thử miễn phí

trả tiền

trả tiếp tháng thứ hai

"this $1 billion AI 
 startup claimed to use AI, but its 'AI' was just two founders taking notes by hand"

Wizard of Oz hợp lệ khi con người làm thay việc mà máy sẽ làm. Nó không hợp lệ khi 
 khách hàng chịu rủi ro dựa trên một tuyên bố sai về hệ thống.

"AI đã kiểm tra hợp đồng này"

"AI đã sàng lọc hồ sơ tín dụng này"

transparency

deck A slide 13–15

"PDF menu 8 quán (không xin phép)"

"một flow: input → AI → output → failure path"

failure path nằm trong lát cắt mỏng nhất

lỗi là hành vi mặc định của hệ 
 thống

---

<!-- chiron-source-span: {"source_span_id":"c7eeb615-8554-5527-bbd2-47862ca442d3","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Automate hay augment — quyết định sản phẩm, không phải quyết định kỹ thuật","source_file":"slide-day05.html"},"checksum":"f2e1e37061f067f4578b57c79eda7a1f6ff49b70fccc35236613e6d824339357"} -->

## 04 Automate hay augment — quyết định sản phẩm, không phải quyết định kỹ thuật

Deck B slide 39–43 · deck C slide 12–16. Chương này có mô-đun định lượng, vì deck B 
 slide 40 nói thẳng rằng đây là một bài toán *expected value*.

### Deck B · slide 39–40 Mixed-initiative: act, ask, hay không làm gì

> Trích deck B 
>  " Augmentation — cần phán đoán, sáng tạo hoặc sở thích cá nhân · ý định và yêu cầu 
>  của user còn mơ hồ · user phải chịu trách nhiệm cho quyết định cuối cùng · sai sót có hậu quả 
>  lớn, khó phục hồi · workflow kéo dài, nhiều bước, thường xuyên thay đổi." 
>  " Automation — lặp lại, tốn thời gian hoặc ít giá trị sáng tạo · quy trình rõ ràng; 
>  input và output dễ xác định · hệ thống có thể thực hiện ổn định với ít giám sát · 
>  nếu AI sai, hậu quả thấp, dễ phát hiện hoặc dễ hoàn tác." 
>  " Inaction — chưa đủ chắc user muốn gì · sai một lần là rất đắt · giữ quyền quyết 
>  định cho người dùng. Ask — có tín hiệu đúng, nhưng còn mơ hồ · một câu hỏi ngắn giảm 
>  rủi ro lớn. Act — đủ chắc user muốn gì · làm sai vẫn dễ sửa hoặc undo." 
>  " Mixed initiative như một bài toán quyết định giữa act, ask, hay not act dựa trên expected 
>  value, chứ không chỉ là sở thích thiết kế. Ask thường là trạng thái thông minh nhất nhưng 
>  lại hay bị bỏ quên nhất. " — Eric Horvitz, Principles of Mixed-Initiative User Interfaces, 
>  CHI 1999 
>  "Copilot: 30% acceptance rate mà 4,7 triệu paid users (1/2026) — 
>  augmentation đúng chuẩn."

Slide 40 làm một việc mà hiếm slide product nào làm: nó nói rằng lựa chọn này *có công thức*. 
 Hãy viết công thức đó ra, vì nó ngắn và nó trả lời được câu hỏi "khi nào thì được tự động hoá" bằng một 
 con số thay vì bằng cảm tính.

```text
Gọi:  p = xác suất AI hiểu đúng ý user
      V = giá trị mang lại khi làm đúng
      C = chi phí khi làm sai   (bao gồm cả công user phải sửa và mất niềm tin)
      I = chi phí làm phiền user một câu hỏi

EV(inaction) = 0
EV(act)      = p·V − (1−p)·C
EV(ask)      = V − I            (hỏi xong thì gần như chắc chắn làm đúng)

ACT thắng ASK  khi  p·V − (1−p)·C  >  V − I
                ⟺  p·(V + C)      >  V + C − I
                ⟺  p  >  1 − I/(V + C)          ← ngưỡng p*

ASK thắng INACTION khi  V > I      (hỏi có lời chừng nào giá trị lớn hơn phiền phức)
```

Công thức `p* = 1 − I/(V+C)` gọn đến bất ngờ và nó nói ba điều, cả ba đều khớp chính xác 
 với các gạch đầu dòng của slide 39:

| Công thức nói gì | Slide 39 nói gì |
| --- | --- |
| C tăng ⇒ p* tăng. Sai càng đắt, càng phải chắc mới được tự động làm | "Sai sót có hậu quả lớn, khó phục hồi" → augmentation |
| C nhỏ ⇒ p* thấp. Sai rẻ thì cứ làm, kể cả khi không chắc lắm | "Nếu AI sai, hậu quả thấp, dễ phát hiện hoặc dễ hoàn tác" → automation |
| I nhỏ ⇒ p* tăng gần 100%. Hỏi càng rẻ, càng nên hỏi thay vì đoán | "Ask: một câu hỏi ngắn giảm rủi ro lớn" |

30% acceptance rate

C gần bằng 0

"tiếp tục gõ là gợi ý biến mất; cost gần 0"

act

Bài học tổng quát:

"60% có thể vẫn hữu dụng nếu user chỉ cần duyệt; 99,5% vẫn nguy hiểm nếu AI 
 tự động hành động sai."

#### Tương tác Act · Ask · Inaction — ngưỡng để được phép tự động hoá

Mô-đun này hiện thực đúng câu của Horvitz mà deck B slide 40 trích: chọn giữa *act*, *ask* và *không làm gì* là một bài toán expected value. Kéo bốn thanh và xem 
 ngưỡng `p*` dịch chuyển.

Mặc định: AI chắc **90%** · làm đúng đáng giá **100** · làm sai tốn **100** · hỏi lại một câu tốn **10**.

Đoán trước: ở độ chắc 90%, nên *act* hay nên *ask*? Và nếu chi phí khi sai tăng từ 
 100 lên **1.000** (ví dụ: tự động hoàn tiền thay vì gợi ý câu trả lời), ngưỡng `p*` nhảy lên bao nhiêu?

#### Kéo rồi mở

**Mặc định: ASK thắng.** EV(act) = 0,9×100 − 0,1×100 = **80**; 
 EV(ask) = 100 − 10 = **90**. Ngưỡng `p* = 1 − 10/200 = 95%` — độ chắc 90% *chưa đủ* để được tự động làm.

Đây chính là điều Horvitz nói và là điều bị bỏ quên nhiều nhất: ở vùng 85–95%, **ask 
 không phải giải pháp nửa vời — nó là lựa chọn tối ưu**. Team thường nhảy thẳng từ "chưa 
 đủ tốt, chưa làm gì" sang "đủ tốt rồi, tự động luôn" mà bỏ hẳn trạng thái giữa.

**Tăng chi phí sai lên 1.000: p* = 1 − 10/1.100 = 99,1%.** Một thay đổi về *hậu quả* — không phải về model, không phải về prompt — đã đẩy yêu cầu độ chắc từ 95% lên 
 hơn 99%. Đó là toàn bộ lý do vì sao "tự động hoàn tiền" và "gợi ý câu trả lời" phải là hai quyết 
 định sản phẩm khác nhau dù dùng chung một model.

**Thử điều đáng thử nhất — kéo chi phí hỏi lại xuống 2:** p* lên tới 99% ngay cả 
 với C = 100. Nghĩa là *làm cho việc hỏi rẻ đi* (một dòng gợi ý inline thay vì một hộp thoại 
 chặn màn hình) là cách **tăng an toàn mà không cần model tốt hơn**. Ngược lại, nếu 
 hỏi rất phiền (I = 60), p* rơi xuống 70% — hệ thống nên đoán bừa còn hơn cứ chặn user lại.

*Bài học vận hành:* ba đại lượng trong công thức thì **hai đại lượng là do bạn 
 thiết kế**, không phải do model quyết định. C giảm được bằng undo và preview; I giảm được 
 bằng cách hỏi nhẹ hơn. Chỉ có p là việc của model — và nó thường là thứ đắt nhất để cải thiện.

- **Control - Độ chắc AI hiểu đúng ý: 90%**: min `50`, max `100`, step `1`, default `90`

- **Control - Giá trị khi làm đúng (V): 100**: min `10`, max `300`, step `10`, default `100`

- **Control - Chi phí khi làm sai (C): 100**: min `0`, max `2000`, step `50`, default `100`

- **Control - Chi phí hỏi lại một câu (I): 10**: min `0`, max `80`, step `1`, default `10`

Lựa chọn tối ưu

—

—

Ngưỡng p*

—

—

Khoảng cách act ↔ ask

—

—

Chi phí sai tối đa cho phép

—

—

ngưỡng p* với chi phí hỏi hiện tại ngưỡng p* nếu hỏi rẻ hơn 4 lần

#### Xem bảng năm mức tự chủ theo chi phí khi sai



#### Công thức & giới hạn của mô hình

- EV(inaction) = 0 · EV(act) = p·V − (1−p)·C · 
 EV(ask) = V − I. Act thắng ask khi p > 1 − I/(V+C).
- Giả định mạnh nhất: hỏi xong thì làm đúng gần như chắc chắn. Thực tế user cũng 
 trả lời mơ hồ, nên EV(ask) thật thấp hơn — nghĩa là ngưỡng p* thật thấp hơn mô-đun này 
 tính. Kết luận định tính không đổi.
- V, C, I là đơn vị tuỳ ý cùng thang (phút tiết kiệm, đồng, hay điểm hài lòng). 
 Chỉ tỉ lệ giữa chúng có ý nghĩa — nhân cả ba với 10 thì p* không đổi.
- Mô hình một lượt. Nó không tính chi phí tích luỹ của việc hỏi quá nhiều lần 
 trong một phiên, thứ mà thực tế làm user bỏ cuộc — deck B slide 46 gọi đây là "khi AI không chắc, 
 bớt làm đi thường là UX tốt hơn", nhưng bớt quá thì cũng hỏng.
- Slide 40 chỉ phát biểu "mixed initiative như một bài toán quyết định… dựa trên expected 
 value". Công thức và mọi con số ở đây là diễn giải của tài liệu này, viết 
 theo đúng khung Horvitz 1999; slide không đưa công thức. Xem 
 Con số cần kiểm chứng.

### Deck C · slide 13–16 Tách task, thang tự động hoá, và bốn vai của con người

> Trích deck C 
>  " Augmentation không phải bản kém của automation. Nó thường là bước đúng để giảm 
>  rủi ro, thu dữ liệu thật và học trước khi tăng tự động hóa." 
>  " Đừng hỏi 'product này automate được không?' Hãy tách thành task. FAQ deadline: 
>  task hẹp, câu trả lời ổn định, nguồn rõ → có thể conditional automation. Debug project: task mở, 
>  nhiều context, dễ dẫn nhóm đi sai → nên augment. Chấm rubric: rủi ro công bằng/accountability cao → 
>  AI hỗ trợ checklist, người quyết cuối. Routing câu hỏi: AI phân loại và ưu tiên queue; case không 
>  chắc phải để người xem lại." 
>  " Không có mốc accuracy chung cho mọi domain. 60% có thể vẫn hữu dụng nếu user chỉ 
>  cần duyệt; 99,5% vẫn nguy hiểm nếu AI tự động hành động sai." 
>  " Cách tăng automation: tăng quyền hành động sau khi có signal thật. 
>  Approve/reject, correction log, case bị handoff và lỗi lặp lại là dữ liệu để nâng mức tự động hóa." 
>  " SPEC check: nếu viết 'human review' mà không nói human làm vai trò nào và output 
>  review đi đâu, thì chưa đủ. REVIEWER: AI draft, người approve/edit/reject. DECIDER: AI đưa options, 
>  người chịu trách nhiệm chọn. TRAINER: correction, label, rank, reason đi vào eval set. 
>  RESCUER: low-confidence, safety risk, escalation, handoff."

"Tách thành task" là lời khuyên có sức nặng nhất trong chương này. Lý do: **một sản phẩm gần 
 như không bao giờ có một mức tự chủ duy nhất** — nó có nhiều task, mỗi task có C khác nhau, nên 
 mỗi task có `p*` khác nhau. Áp mô-đun ở trên vào chính bốn task deck C nêu:

| Task | C — sai thì mất gì | Mức tự chủ hợp lý | Vai của con người |
| --- | --- | --- | --- |
| FAQ deadline | Thấp — user hỏi lại là xong, và có nguồn để đối chiếu | Conditional automation — tự trả lời khi khớp nguồn, không chắc thì im | — (chỉ xem log) |
| Routing câu hỏi | Trung bình — sai queue làm chậm, nhưng phát hiện được | Automation có ngưỡng — dưới ngưỡng thì đẩy sang người | RESCUER cho case không chắc |
| Debug project | Cao và âm thầm — dẫn cả nhóm đi sai hướng vài ngày | Augmentation — summary + suggested next step | DECIDER — người chọn hướng |
| Chấm rubric | Cao và có tính công bằng/pháp lý | Augmentation — AI dựng checklist | REVIEWER + DECIDER, và bắt buộc TRAINER |

"có human review"

| Vai | Phải xây gì | Ai làm, tần suất nào |
| --- | --- | --- |
| REVIEWER | Giao diện approve/edit/reject trước khi output đi ra | Người trong luồng, mọi case → tốn nhân lực tuyến tính theo volume |
| DECIDER | Giao diện đưa 2–3 options, ghi lại ai chọn gì | Người trong luồng, mọi case — nhưng nhẹ hơn reviewer |
| TRAINER | Correction log + đường ống đưa correction vào eval set | Có thể là chính hai vai trên, miễn là dữ liệu được lưu |
| RESCUER | Ngưỡng confidence + hàng đợi escalation + SLA cho hàng đợi đó | Ngoài luồng, chỉ case khó → chỉ vai này scale được |

chỉ RESCUER là mô hình tự động hoá thật

signal do TRAINER thu chính là thứ cho phép 
 chuyển

thực nghiệm

approve rate

mô-đun demo vs phân bố

70–97%

85–93%

**Kiểm tra 2** Một team đề xuất: "Agent của chúng tôi đạt 94% accuracy trên eval 
 set, cao hơn ngưỡng 90% ta đặt ra, nên bật chế độ tự động gửi email trả lời khách." Dùng khung của 
 chương này, hãy chỉ ra *hai* chỗ lập luận thiếu.

#### Xem đáp án

**Thiếu thứ nhất — accuracy không phải đại lượng quyết định.** Câu hỏi đúng không 
 phải "đủ 90% chưa" mà " *sai thì mất gì* ". Gửi email cho khách là hành động **khó undo** (email đã gửi không rút lại được), nên C rất cao — và theo `p* = 1 − I/(V+C)`, C cao thì ngưỡng phải cao hơn nhiều so với 90%. Deck C nói thẳng: 
 "99,5% vẫn nguy hiểm nếu AI tự động hành động sai."

**Thiếu thứ hai — họ bỏ qua trạng thái ask.** Lựa chọn không phải nhị phân 
 "tự động gửi" vs "không làm gì". Có ít nhất hai mức trung gian rất rẻ: soạn sẵn draft cho nhân viên 
 bấm gửi (REVIEWER), hoặc tự gửi những loại thư an toàn và đẩy phần còn lại sang người (RESCUER có 
 ngưỡng). Cả hai đều thu được signal để sau này nâng mức tự chủ có căn cứ.

*Và một chỗ thứ ba nếu muốn nói thêm:* "94% trên eval set" là con số điểm, không có khoảng 
 tin cậy. Nếu eval set chỉ có 50 case thì khoảng tin cậy 95% khoảng **84–98%** — nghĩa là 
 chưa loại trừ được khả năng model thật chỉ đúng 84%.

---

<!-- chiron-source-span: {"source_span_id":"7e7b9411-a380-53e5-8a74-a0cda9db405c","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Requirements đo được — chỗ AI khác CRUD form nhiều nhất","source_file":"slide-day05.html"},"checksum":"a95844aeaaa01254afb94532a633088cd30165f1353f9a957a3dac3871f9c001"} -->

## 05 Requirements đo được — chỗ AI khác CRUD form nhiều nhất

Deck A slide 21–23 · deck B slide 23–24 · deck C slide 18–19. Ba deck hội tụ vào cùng 
 một kết luận: *acceptance criteria nhị phân là sai lầm gốc*.

### Deck A · slide 21–23 Từ mơ hồ đến đo được, và bốn thành phần của acceptance criteria

> Trích deck A 
>  " Requirement mơ hồ: 'Agent phải trả lời nhanh, chính xác, và thông minh.' 
>  Requirement đo được: 'Agent phải trả lời trong dưới 5 giây ở p95, trích dẫn đúng 
>  nguồn nội bộ, và escalate sang người thật khi confidence thấp.'" 
>  "Lưu ý: Nếu engineer không biết cách test, thì requirement đó chưa đủ rõ. " 
>  " 3 nhóm requirement: Functional (tóm tắt ticket, phân loại lead) — mô tả AI phải 
>  làm việc gì · Non-functional (latency SLA, uptime, cost budget) — bảo vệ trải nghiệm và khả năng vận 
>  hành · AI-specific (hallucination threshold, explainability, fallback) — phản ánh 
>  bản chất rủi ro của AI" 
>  " When X happens, the agent should Y within Z seconds, and if failure condition occurs, it 
>  should fallback behavior. "

Câu mẫu ở cuối có bốn ô trống, và deck A slide 23 liệt kê đúng bốn thứ phải điền. Bảng dưới tách rõ 
 và thêm một cột — *kiểm chứng bằng cách nào* — vì đó là phép thử "engineer có biết cách test 
 không":

| Thành phần | Ví dụ của deck A | Test bằng cách nào |
| --- | --- | --- |
| Trigger rõ | "Khi user hỏi về chính sách hoàn tiền…" | Viết 10 câu hỏi khớp trigger + 10 câu gần khớp nhưng không phải → kiểm phân loại |
| Hành vi mong đợi | "agent phải trích dẫn văn bản nguồn và trả lời bằng tiếng Việt lịch sự" | Citation: kiểm tự động được (có link, link đúng tài liệu). Giọng điệu: cần rubric + người chấm |
| Ngưỡng đo được | "trong dưới 6 giây; nếu thiếu thông tin thì agent phải hỏi lại" | Latency: đo p95, không đo trung bình. "Hỏi lại": cần một tập case thiếu thông tin để chạy |
| Failure handling | "nếu không tìm thấy nguồn phù hợp, agent phải nói rõ giới hạn và chuyển hướng" | Chủ động dựng case không có nguồn (hỏi về chính sách chưa tồn tại) → kiểm agent không 
 bịa |

"trả lời trong dưới 5 giây ở p95"

đo được hoàn toàn

"trích dẫn đúng nguồn nội bộ"

chưa đủ.

tự động

Chất lượng AI cũng là 
 một phân bố y hệt latency

hallucination threshold

explainability

fallback

"AI PRD thiếu acceptance threshold section = chưa 
 phải AI PRD."

### Deck B · slide 23–24 Nondeterminism là mặc định, và ba ca chuyển đổi của spec

> Trích deck B 
>  " ① Output variance — cùng một input, hai lần chạy ra hai output khác nhau. Đây là 
>  hành vi mặc định của mọi hệ probabilistic. ② Behavioral drift — release thì đúng, 
>  vài tuần sau lệch. Team biết qua complaint của user, không qua monitoring của mình. 
>  ③ Reasoning-level failure — retrieval đúng, tool call đúng, model trả lời trôi chảy 
>  — nhưng tổ hợp các bước ra kết quả sai. 'Monitoring shows all green. But the product fails.' " 
>  " Sai lầm ① — Giấu variance. Không nút regenerate, không confidence framing → user 
>  báo 'bug' cho hành vi đúng kỹ thuật. Sai lầm ② — Acceptance criteria nhị phân. 
>  'AI trả lời đúng' + 3 test case xanh → ship. Nhưng vài test case là demo, không phải 
>  distribution. Sai lầm ③ — Fallback là ý sau cùng. Spec chỉ có 1 dòng 'display 
>  error message'." 
>  " ① Từ expected output → acceptance criteria dạng tỉ lệ. ✕ 'The AI returns a 
>  correct summary.' → ✓ ' The AI produces a summary that passes this rubric on 90% of a 
>  representative input set. '" 
>  " ② Từ test cases → test distributions. Một test case là demo. Một distribution mới 
>  là product. Bắt đầu bằng 20 case phản ánh input thật (messy, edge, ambiguous — 
>  không chỉ happy path), lớn dần từ production traces, không phải từ trực giác." 
>  " ③ Từ 'works' → 'fails by design'. Spec phải có Failure Modes 
>  section: confidence thấp thì sao? tool timeout thì sao? output ngoài ngưỡng chấp nhận thì 
>  user thấy gì? Đây là quyết định product — viết vào spec, không phải thread Slack 3 tuần sau 
>  launch. " 
>  " FALLBACK 3 TẦNG (chọn là quyết định product, ghi vào PRD): Soft 
>  fallback — output đơn giản/hẹp hơn khi confidence thấp · Human handoff — 
>  case rủi ro cao/mơ hồ chuyển người thật · Silent skip — không làm gì, nhưng cũng 
>  không làm sai." 
>  " Nondeterminism không phải bug để sửa — là constraint để thiết kế vòng tránh, như latency 
>  hay kích thước màn hình. "

Câu cuối là câu hay nhất của deck B. Phép so sánh với *latency* và *kích thước màn 
 hình* chính xác đến mức nên dùng làm cách giải thích cho stakeholder:

| Constraint | Cách sai | Cách đúng |
| --- | --- | --- |
| Kích thước màn hình | Thiết kế cho một màn hình 1440px rồi coi mọi thứ khác là lỗi | Responsive: thiết kế cho một dải kích thước |
| Latency mạng | Giả định mạng luôn nhanh; treo giao diện khi chậm | Loading state, timeout, retry, offline mode |
| Nondeterminism | Giả định AI trả lời đúng; xử lý trường hợp sai như 
 exception | Thiết kế cho một dải chất lượng: ngưỡng, fallback ba tầng, nút thử lại, 
 đường sửa |

Ba ca chuyển đổi là phần đáng chép nguyên. Chúng thay đổi ba thứ hoàn toàn khác nhau:

| Ca | Đổi cái gì | Trước | Sau | Hệ quả lên công việc |
| --- | --- | --- | --- | --- |
| ① | Cách viết acceptance criteria | "AI returns a correct summary" | "passes this rubric on 90% of a representative input set" | Phải có rubric — tức phải định nghĩa "đủ tốt" trước khi build |
| ② | Cách kiểm chứng | 3 test case | 20 case phản ánh input thật, lớn dần từ production traces | Phải có đường ống đưa case thật từ production về eval set |
| ③ | Cách cấu trúc spec | 1 dòng "display error message" | Một section riêng: Failure Modes | Phải quyết định fallback nào cho case nào — quyết định sản phẩm, không phải kỹ thuật |

ngưỡng bắt đầu

Để tìm ra failure mode

1,2%

Để làm quality gate

70–97%

mô-đun demo vs phân bố

51,2%

| Tầng | Khi nào dùng | User thấy gì |
| --- | --- | --- |
| Soft fallback | Confidence thấp nhưng vẫn làm được việc hẹp hơn | Câu trả lời ngắn hơn, dè dặt hơn, hoặc chỉ trích nguồn mà không diễn giải |
| Human handoff | Rủi ro cao hoặc mơ hồ | Chuyển sang người thật, kèm ngữ cảnh đã thu thập |
| Silent skip | Không đủ chắc để nói gì, và không nói cũng không sao | Không thấy gì cả |

Silent skip

spurious

"AI tốt không phải AI luôn có câu trả lời."

"Retrieval đúng, tool call đúng, model trả lời trôi chảy — nhưng tổ hợp các bước ra kết quả sai. 
 Monitoring shows all green. But the product fails."

không một metric hạ tầng nào bắt được

eval trên kết quả 
 cuối

tín hiệu hành vi của user

Ngày 24 của Track 3

faithfulness

context precision/recall

Ngày 25

### Deck C · slide 18–19 Ba trụ: requirement, UX, eval — và câu hỏi tương ứng

> Trích deck C 
>  " 1 · REQUIREMENT — không chỉ feature. Trước: 'Click X → Y'. Giờ: 
>  'Hỏi X → Y khoảng 85%; dưới 60% thì hỏi lại user'. Spec phải có ngưỡng, lúc không 
>  chắc và failure behavior. → Sai thế nào là chấp nhận được? " 
>  " 2 · UX — không chỉ màn hình đẹp. Trước: thiết kế cho lúc đúng. Giờ: thiết kế cho 
>  lúc sai: user thấy sai, sửa được, và tin lại được. → Sai thì user làm gì? " 
>  " 3 · EVAL — không chỉ pass/fail. Giờ: chạy 100 lần → bao nhiêu% 'đủ tốt', lỗi nào 
>  không được vượt ngưỡng? PM quyết định quality distribution, không chỉ QA. → 
>  Bao nhiêu% sai là chấp nhận được? " 
>  " AI SPEC: Outcome + threshold + fallback. Nếu đủ dữ liệu: trả lời có nguồn. Nếu 
>  thiếu hoặc dưới ngưỡng: hỏi lại / chuyển người."

Câu mẫu *"Hỏi X → Y khoảng 85%; dưới 60% thì hỏi lại user"* gọn hơn câu mẫu của deck A và 
 đáng dùng làm khuôn, vì nó chứa **hai** ngưỡng chứ không phải một — và hai ngưỡng đó có 
 vai trò hoàn toàn khác nhau:

| Ngưỡng | Là gì | Ai dùng nó | Đo lúc nào |
| --- | --- | --- | --- |
| 85% | Quality gate — tỉ lệ đạt trên eval set | Team, trước khi release | Offline, trên tập cố định |
| 60% | Confidence threshold — ngưỡng runtime, mỗi request | Hệ thống, trong lúc chạy | Online, từng lượt một |

đơn vị

tỉ lệ trên tập

xác suất cho một câu hỏi cụ thể

không được hiệu chỉnh

với LLM sinh văn bản thuần tuý, bạn 
 thường không có sẵn một "confidence" đáng tin nào cả.

---

<!-- chiron-source-span: {"source_span_id":"18e422c6-c76d-52f2-a4cf-e1c159b9b675","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 PRD anatomy — 8 phần của deck A, 6 bước của deck B","source_file":"slide-day05.html"},"checksum":"c76aaf62db130477a7c1ceb838d4cb469e455692cf368a541800602603db0a43"} -->

## 06 PRD anatomy — 8 phần của deck A, 6 bước của deck B

Deck A slide 25–27 · deck B slide 17–22, 27. Hai cách nhìn: một cái là *mục lục tài liệu*, một cái là *thứ tự công việc*. Chúng khớp nhau và bổ sung cho nhau.

### Deck A · slide 25–27 Tám phần, ba tầng metric, năm anti-pattern

> Trích deck A 
>  " 8 phần: 1. Problem · 2. Target User · 3. Success Metrics · 4. Technical 
>  Architecture · 5. Feature Requirements · 6. Non-functional · 7. Acceptance Criteria · 8. Risks" 
>  "Lưu ý: Đừng xem PRD là file để 'điền cho đủ'. PRD tốt phải làm rõ quyết định, giảm tranh 
>  cãi mơ hồ, và giúp team biết thế nào là done. " 
>  " Success Metrics Hierarchy: Business KPI (cost saved, revenue, CSAT) — sản phẩm 
>  này tạo giá trị gì? · Product metric (task completion, repeat usage, escalation rate) — 
>  user có thực sự dùng và hoàn thành việc không? · AI metric (accuracy, latency, citation 
>  rate) — hệ AI có vận hành đủ tốt để nâng product metric không? " 
>  " Anti-patterns: chỉ mô tả tính năng, không mô tả problem và target user · viết 
>  metric kiểu 'càng cao càng tốt', không có baseline hay threshold · thiếu non-functional requirements · 
>  không có risk section nên đến lúc triển khai mới tranh luận về bias, privacy, adoption · 
>  viết solution quá sớm, chưa chứng minh user value hoặc workflow fit "

Tầng metric là phần đáng dừng lại lâu nhất. Câu hỏi gắn với tầng thứ ba — *"hệ AI có vận hành đủ tốt để **nâng product metric** không?"* — chứa một khẳng 
 định mạnh mà deck A không mở ra: **AI metric chỉ có giá trị nếu nó truyền được lên tầng 
 trên**. Và mối liên hệ đó thường xuyên đứt:

| Tầng | Ví dụ | Đo được lúc nào | Chỗ mối nối hay đứt |
| --- | --- | --- | --- |
| Business KPI | Cost saved, revenue, CSAT | Sau vài tháng, nhiễu bởi hàng chục yếu tố khác | — |
| Product metric | Task completion, repeat usage, escalation rate | Sau vài tuần | ↑ Đứt khi: user dùng nhưng công việc thật không giảm (case Gamma: 
 user hoàn thành task, nhưng tự sửa hết 20% cuối) |
| AI metric | Accuracy, latency, citation rate | Ngay lập tức, mỗi lần build | ↑ Đứt khi: accuracy tăng trên eval set nhưng user không đổi hành vi — eval set 
 không phản ánh input thật |

Đo

Nhưng chứng minh giá trị thì phải từ trên xuống

"metric càng cao càng tốt, không có baseline hay threshold"

lý do

Escalation rate

sai

dải

Năm anti-pattern nên đọc như một checklist ngược — đọc PRD của mình và tìm dấu hiệu:

| Anti-pattern | Dấu hiệu nhận ra trong 30 giây |
| --- | --- |
| Chỉ tính năng, không problem/target user | Trang 1 mở đầu bằng một mô tả màn hình hoặc một sơ đồ kiến trúc |
| Metric "càng cao càng tốt" | Không có số nào trong mục Success Metrics, hoặc có số mà không có baseline hiện tại |
| Thiếu non-functional | Ctrl-F "latency", "cost", "privacy", "escalation" → không thấy chữ nào |
| Không có risk section | Mục lục dừng ở Acceptance Criteria |
| Viết solution quá sớm | Problem statement có chứa chữ "AI", "chatbot", "agent" — đúng phép thử của 
 deck B slide 19 |

đương nhiên

phát biểu vấn đề mà không 
 nhắc chữ AI

### Deck B · slide 20–22, 27 Sáu bước của Ailian Gan: goals, scope, và bốn mục PRD riêng của AI

> Trích deck B 
>  " ③ Define goals: goals · non-goals · success metrics. Goals là outcome định tính 
>  gắn với problem statement — không phải solution, và cũng không nhắc AI. Bài toán có thể giải tốt 
>  nhất mà không cần AI — goal không gắn với công nghệ. " 
>  " SUCCESS METRICS — 3 TẦNG. Usage:% accounts enable base setting · MAU của meeting 
>  summaries ·% meetings chạy summary. Quality:% thumbs up vs thumbs down. 
>  Impact (khó đo → dùng proxy): thời gian tiết kiệm khi không cần người ghi note ·% meetings user vắng mặt nhưng đọc summary." 
>  " ④a Scope the solution: mô tả user flow end-to-end. Bao gồm cả các bước KHÔNG có 
>  AI — đừng chỉ định nghĩa đoạn AI." 
>  " ⚠ Đừng bắt đầu bằng chatbot. User gõ gì cũng được → quality khó kiểm soát; lại 
>  dính cold start — user không biết hỏi gì, hỏi thế nào, probe tiếp ra sao. Cân nhắc các interaction 
>  non-chatbot trước." 
>  " ④b AI-specific requirements — phần PRD không có ở feature thường: 
>  ① User input & contextual data — phải định ranh giới data rõ ràng · 
>  ② LLM output spec — mô tả length · tone · format · exclusion độc lập ví dụ · 
>  ③ Feedback mechanism · ④ Quality evaluation — bar phụ thuộc risk " 
>  Ví dụ Zoom, mục "Next Steps": " chỉ action sau cuộc họp (không gồm việc trong meeting) · 
>  1 action/bullet · có tên assignee · tối đa 8 · tone professional "

Sáu bước của deck B và tám phần của deck A không mâu thuẫn — chúng là *trục thời gian* và *trục mục lục* của cùng một thứ:

| Bước (deck B) — thứ tự làm | Phần PRD (deck A) — chỗ ghi vào |
| --- | --- |
| ① Identify good use cases | (trước PRD — là bước chọn có làm hay không) |
| ② Articulate the problem | 1. Problem · 2. Target User |
| ③ Define goals · non-goals · success metrics | 3. Success Metrics |
| ④a Scope the solution — user flow end-to-end | 5. Feature Requirements |
| ④b AI-specific requirements | 6. Non-functional + 7. Acceptance Criteria — và đây là chỗ deck A mỏng nhất |
| ④c Privacy & controls | 8. Risks (một phần) |
| ⑤ Align engineering | 4. Technical Architecture |
| ⑥ GTM | (sau PRD) |

"chỉ action sau cuộc họp (không gồm việc trong meeting) · 1 action/bullet · có tên assignee · 
 tối đa 8 · tone professional"

length · tone · format · exclusion

| Ràng buộc | Loại | Kiểm tự động được không |
| --- | --- | --- |
| "không gồm việc trong meeting" | Exclusion — ranh giới nội dung | Khó — cần người hoặc LLM-as-judge |
| "1 action/bullet" | Format | Được — parse bullet |
| "có tên assignee" | Format — trường bắt buộc | Được — kiểm sự hiện diện của tên |
| "tối đa 8" | Length | Được — đếm |
| "tone professional" | Tone | Khó — cần rubric |

kiểm được tự động

độc lập ví dụ

exclusion

một câu phủ định tường 
 minh

Ngày 4

sáu

cuối cùng

| Kiểu | Ai kích hoạt | Kiểm soát chất lượng | Ví dụ của slide |
| --- | --- | --- | --- |
| Click a button | User, chủ động | Cao nhất — input cố định | Nút "tóm tắt chat thread này" |
| Pre-set prompts | User, chọn từ danh sách | Cao | LinkedIn gợi ý takeaway questions |
| One-shot prompt | User, tự do | Trung bình | Notion, Canva |
| Automated report | Hệ thống, theo lịch | Cao — input biết trước | Zoom summary tự chạy, Slack daily recap |
| Automated suggestions | Hệ thống, trong luồng | Trung bình | Superhuman tóm tắt email 1 dòng |
| Chatbot | User, hoàn toàn tự do | Thấp nhất | Intercom "Fin", Duolingo Roleplay |

quality khó kiểm soát

cold start

chương 08

chương 11

xoá sạch ba loại trigger error

Disclosure

Default off

Kill switch

Retention

Không train trên dữ liệu khách

hai

liên tục

xoá

giữa cuộc họp

free kèm meetings license

"muốn AI phổ biến rộng, không để IT admin phải chọn ai được dùng 
 AI"

adoption

deck A

**Kiểm tra 3** PRD của bạn có mục Success Metrics viết: *"Tăng accuracy của 
 agent lên trên 90%."* Nêu *ba* vấn đề với dòng này, dựa trên chương 05 và 06.

#### Xem đáp án

**① Đây là AI metric mồ côi.** Nó nằm ở tầng thấp nhất trong ba tầng và không nối 
 lên tầng nào. Thiếu câu trả lời: accuracy tăng thì *product metric* nào tăng (escalation rate 
 giảm? task completion tăng?), và điều đó đẩy *business KPI* nào?

**② Không có baseline.** Đúng anti-pattern "càng cao càng tốt". Hiện tại là bao 
 nhiêu? Nếu đang 88% thì 90% là một cải thiện nhỏ; nếu đang 60% thì đó là một dự án khác hẳn về quy mô.

**③ "Accuracy" chưa định nghĩa được — đo trên tập nào, bằng rubric nào?** Theo deck B 
 ca ①, câu phải có dạng " *đạt rubric X trên 90% của một tập input đại diện* ". Thiếu tập, thiếu 
 rubric thì con số 90% không kiểm chứng được, và tệ hơn: nó có thể tăng chỉ bằng cách đổi eval set.

*Điểm thưởng:* dòng này cũng không nói gì về **failure behavior**. 10% còn lại 
 thì sao — sai âm thầm, hay hỏi lại, hay chuyển người? Với AI product, chính 10% đó mới quyết định sản 
 phẩm dùng được hay không.

### Deck A · slide 29–31 User story cho AI: template, ba ví dụ, và ba lớp phải đi kèm

> Trích deck A 
>  " As [persona], I want [AI capability], so that [business value]. 
>  · Persona phải là người dùng thật, không phải 'hệ thống' 
>  · AI capability phải mô tả hành vi, không phải tên model 
>  · Business value phải nối được sang KPI hoặc pain point" 
>  " As an HR staff member, I want AI to answer policy questions with source citation, so that I 
>  can respond consistently and reduce manual lookup time. " 
>  " Happy path — trả lời đúng nguồn trong dưới 6 giây → định nghĩa kết quả mong đợi. 
>  Edge case — câu hỏi mơ hồ, câu hỏi thiếu dữ liệu, tiếng lóng → 
>  tránh ảo tưởng coverage. 
>  Error state — không có nguồn, tool timeout, confidence thấp → 
>  buộc thiết kế fallback & escalation."

Ba ràng buộc của template đều là ràng buộc *chống lại một lỗi cụ thể*:

| Ràng buộc | Chặn lỗi gì | Ví dụ vi phạm |
| --- | --- | --- |
| Persona là người thật, không phải "hệ thống" | Chặn việc viết requirement kỹ thuật dưới lốt user story | "As the system, I want to cache embeddings, so that latency drops" — đây là task, không phải story |
| Mô tả hành vi, không phải tên model | Chặn việc khoá spec vào một giải pháp cụ thể | "I want GPT-4 to summarise…" — nếu đổi model thì story phải viết lại, dù nhu cầu không đổi |
| Business value nối được sang KPI | Chặn tính năng mồ côi | "so that the assistant is smarter" — không nối được sang bất kỳ metric nào |

consistently

consistently

reduce manual lookup time

with source citation

| Deck A slide 31 | Deck C slide 37 | Ghi chú |
| --- | --- | --- |
| Happy path | Happy | Giống nhau |
| Edge case — "tránh ảo tưởng coverage" | Low-confidence | Deck C đặt tên theo trạng thái hệ thống, deck A theo loại input — hai cách 
 nhìn cùng một vùng |
| Error state — "buộc thiết kế fallback & escalation" | Failure | Giống nhau |
| — | Correction | Deck A thiếu. Không có lớp nào hỏi "user sửa rồi, dữ liệu đi đâu" |

"tránh ảo tưởng coverage"

trông như

bốn

correction

---

<!-- chiron-source-span: {"source_span_id":"f162d705-4750-51f4-af02-99d5a623d726","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 UX cho sự bất định — thiết kế cho lúc AI sai","source_file":"slide-day05.html"},"checksum":"6ed1ef4591bf39715331176f295d6c28e6afed512b49c85e86d451ff984f1e99"} -->

## 07 UX cho sự bất định — thiết kế cho lúc AI sai

Deck B slide 30–54 · deck C slide 26–28. Phần dài nhất của deck B, và là phần trả lời 
 câu hỏi trụ thứ hai của deck C: *"Sai thì user làm gì?"*

### Deck B · slide 34–38 Trust calibration: overtrust và distrust đều là lỗi thiết kế

> Trích deck B 
>  " Don't let your UI write a check that your AI can't cash. " — Eytan Adar, 2018 
>  " ✕ Auto-resolve customer issue vs ✓ Draft reply for human review " 
>  " Overtrust = user tin cao hơn năng lực thật của AI. Ví dụ: AI chỉ nên gợi ý, nhưng 
>  UI làm user tưởng nó có thể tự quyết. Nguy hiểm vì user dễ giao việc quá mức, bỏ qua kiểm tra. 
>  Distrust = user tin thấp hơn năng lực thật. Ví dụ: AI thực ra giúp tốt, nhưng user 
>  không dám dùng hoặc bỏ qua hoàn toàn. Hậu quả là underuse: có giá trị nhưng không được tận 
>  dụng. " 
>  " Trust calibration = expectation + explainability + control. 
>  Expectation: nói rõ AI làm được gì, làm tốt tới đâu, khi nào dễ sai. 
>  Explainability: giúp user hiểu vì sao AI ra output này và khi nào nên nghi ngờ. 
>  Control: cho user sửa, bỏ qua, undo, preview, hoặc duyệt trước khi commit."

Điểm quan trọng nhất của khung này: **mục tiêu không phải "tăng trust"** — mục tiêu là *hiệu chỉnh* trust về đúng mức. Đây là chỗ rất nhiều team đi sai hướng, vì "user tin sản phẩm 
 của mình" nghe như một điều tốt vô điều kiện.

|  | Overtrust | Distrust |
| --- | --- | --- |
| Trạng thái | Trust > năng lực | Trust < năng lực |
| Hành vi user | Giao việc quá mức, bỏ qua kiểm tra | Không dùng, hoặc dùng rồi tự làm lại từ đầu |
| Hậu quả | Lỗi lọt ra ngoài — có thể nghiêm trọng | Underuse — sản phẩm chết lặng lẽ |
| Ai phát hiện | Thường là khách hàng cuối, sau khi đã muộn | Không ai — chỉ thấy qua metric adoption thấp |
| Sửa bằng | Hạ kỳ vọng: capability cue trung thực, không precision giả, 
 thêm bước duyệt | Nâng kỳ vọng có căn cứ: explainability, citation, cho thử ở rủi ro thấp |

lời hứa mà giao 
 diện phát ra

kết quả cuối

một bản nháp

mô-đun act/ask

C

Cùng một p, hai giá trị C khác nhau, hai quyết định sản phẩm khác nhau.

"Nhiều AI product fail vì team ngầm giả định 
 user muốn 'full automation', trong khi thực tế user chỉ muốn decision support."

không có cách nào để kiểm tra nhanh

chương 02

Phép đo distrust rẻ nhất

behavioral signal

_Sơ đồ: Trust calibration: vùng overtrust, vùng distrust và đường hiệu chỉnh đúng - Biểu đồ hai trục: trục ngang là năng lực thật của hệ thống AI, trục dọc là mức độ tin tưởng của người dùng. Đường chéo từ gốc lên góc trên phải là trạng thái trust được hiệu chỉnh đúng, nơi niềm tin khớp với năng lực. Vùng phía trên đường chéo là overtrust, nơi người dùng tin nhiều hơn năng lực thật, dẫn tới giao việc quá mức và bỏ qua kiểm tra. Vùng phía dưới đường chéo là distrust, nơi người dùng tin ít hơn năng lực thật, dẫn tới không sử dụng dù sản phẩm có giá trị. Ba mũi tên ở dưới cho thấy ba công cụ kéo trust về đúng chỗ: expectation đặt kỳ vọng ban đầu, explainability giúp hiểu vì sao, và control cho phép sửa và hoàn tác._

Hình 2 — trust calibration.

Designing Human-Centric AI Experiences

khả năng bị phát hiện

### Deck B · slide 44–50 Bốn nguyên tắc HAX đầu tiên, và "precision giả" là một lỗi thiết kế

> Trích deck B 
>  " Make clear what the system can do. Design patterns: use explanations · 
>  expose system controls (làm lộ các nút, menu, tùy chọn để người dùng nhìn vào là hiểu hệ 
>  thống có những khả năng nào) · demonstrate possible inputs (ví dụ prompt, ví dụ câu hỏi). 
>  Capability cue là một phần của interaction design — không chỉ là onboarding copy. " 
>  " Make clear how well the system can do what it can do. 
>  🍱 Food Scanner: ✓ Khoảng '350–430 kcal' + nói rõ là ước tính vì ảnh hơi mờ. ✕ Một con số exact 
>  '387 kcal' — precision giả. 
>  📄 Resume Screener: ✓ 'Danh sách phù hợp để bạn xem trước' + nêu giới hạn dữ liệu đầu vào. 
>  ✕ Auto loại ứng viên ('Đã loại') trước khi con người xem. 
>  🧠 Mental Health Journaling AI: ✓ 'Đây là quan sát từ nhật ký, không phải chẩn đoán'. 
>  ✕ Gắn nhãn 'Burnout giai đoạn 2' như chẩn đoán chắc chắn." 
>  " Scope services when in doubt. Khi AI không chắc để hiểu người dùng, nó nên hỏi 
>  lại — thay vì cố giải quyết một câu hỏi mơ hồ. Khi AI không chắc, bớt làm đi thường là UX tốt 
>  hơn. " 
>  " Hiển thị kết quả theo mức độ tự tin. User không cần biết 0.71 hay 0.84 — user cần 
>  thấy hệ thống cư xử khác nhau khi độ chắc khác nhau. Kayak từng hiển thị 'Confidence 79%' 
>  (2013–2019) — nay đã bỏ số%: confidence không nhất thiết là một con số."

Bốn ví dụ "do / don't" ở slide 45 hay vì chúng cho thấy **mỗi domain cần một cách nói khác 
 nhau** — và cả bốn đều hỏng theo cùng một cơ chế: *trình bày một ước lượng như thể nó là một 
 sự kiện*.

| Domain | Cách "don't" hỏng | Cách "do" sửa bằng cơ chế gì |
| --- | --- | --- |
| Trip Planner | Nói "phù hợp nhất" + tổng chi phí như chắc chắn | Gắn điều kiện thời điểm: "giá thực tế có thể thay đổi khi đặt" |
| Food Scanner | "387 kcal" — precision giả | Đổi từ điểm sang khoảng: "350–430 kcal", + lý do bất định ("ảnh hơi mờ") |
| Resume Screener | Tự loại ứng viên trước khi người xem | Đổi hành động: từ quyết định sang xếp hạng để người xem trước |
| Mental Health | Nhãn "Burnout giai đoạn 2" — mượn giọng chẩn đoán y khoa | Đổi thể loại phát ngôn: "quan sát từ nhật ký, không phải chẩn đoán" |

Số chữ số bạn hiển thị là một lời hứa về độ chính xác.

Cách sửa mang tính hệ thống:

khoảng

hạng

hành vi

một màn hình chào 
 mừng

hiện diện thường trực trong luồng

"pre-set prompt gợi ý ở mỗi bước + vẫn cho gõ 
 free text → khỏi viết prompt từ đầu, template chất lượng hơn"

### Deck C · slide 26–28 · deck B slide 51–54 Bốn câu UX, graceful failure, và trả quyền cho user

> Trích deck C 
>  " 4 câu mỗi AI product phải trả lời: 
>  1 · Khi đúng — user thấy gì? Copilot: gợi code màu xám, bấm Tab để chấp nhận. 
>  2 · Khi không chắc — hệ thống làm gì? Copilot: gợi ngắn hơn, ít tự tin hơn, user tự viết tiếp. 
>  3 · Khi sai — user sửa thế nào? Copilot: tiếp tục gõ là gợi ý biến mất; cost gần 
>  0. 
>  4 · Khi mất tin — gỡ thế nào? Copilot: tắt cho file/ngôn ngữ này, bật lại khi muốn." 
>  " Vì sao Copilot accuracy không cần hoàn hảo mà vẫn dùng được? Vì sai thì ít thiệt hại, sửa 
>  nhanh, và user giữ quyền quyết định. Microsoft Tay là phản ví dụ: không có recovery path khi 
>  bị user tấn công hành vi." 
>  " Graceful failure không phải câu 'AI có thể sai'. Nó là cơ chế cụ thể để user thấy sai, sửa 
>  được, và quay lại tin sản phẩm. Đưa nhiều lựa chọn, không chỉ một đáp án tuyệt đối · cho user 
>  sửa output trực tiếp · fallback sang manual hoặc human review · 
>  ghi correction để biến lỗi thành signal."

> Trích deck B slide 52–54 
>  " Nếu AI không hoàn hảo, đừng bắt user làm lại từ đầu. Cho phép user chỉnh sửa kết 
>  quả · Undo / Rollback." 
>  " Màn hình lỗi là cơ hội để hướng dẫn cách dùng đúng · Lỗi là cơ hội để xin feedback. 
>  Error state là lúc user sẵn sàng học nhất — và cũng sẵn sàng phản hồi nhất." 
>  " Trả quyền kiểm soát cho người dùng. Chuyển sang người thật · gợi ý bước tiếp theo 
>  · có chế độ cho user tự chỉnh. AI tốt không phải AI luôn có câu trả lời — AI tốt biết đưa user 
>  sang con đường khác khi mình không đủ khả năng. "

Bốn câu hỏi của deck C là **checklist hoàn chỉnh nhất trong cả ba deck** cho phần UX, và 
 câu thứ tư là câu ít ai nghĩ tới. Đối chiếu với ba fallback của deck B và bốn bước của deck C:

| Câu hỏi | Ứng với bước nào (deck C slide 11) | Ví dụ Copilot | Chi phí xây |
| --- | --- | --- | --- |
| 1 · Khi đúng, user thấy gì? | — | Gợi code màu xám, Tab để nhận | Đây là phần ai cũng làm |
| 2 · Khi không chắc, hệ thống làm gì? | DETECT + ROUTE | Gợi ngắn hơn, ít tự tin hơn — soft fallback | Cần một tín hiệu confidence — thường là phần khó nhất |
| 3 · Khi sai, user sửa thế nào? | RECOVER | Gõ tiếp là gợi ý biến mất; cost gần 0 | Rẻ nếu thiết kế từ đầu, rất đắt nếu thêm sau |
| 4 · Khi mất tin, gỡ thế nào? | — (nằm ngoài bốn bước) | Tắt cho file/ngôn ngữ này, bật lại khi muốn | Rẻ, và gần như luôn bị bỏ quên |

chống lại

nó giữ user ở lại sản phẩm.

theo file và theo ngôn ngữ

"không có recovery path khi bị user tấn công hành vi."

không có DETECT và không có ROUTE

input uncertainty

deck C slide 8

cố tình prompt injection

Ngày 24 của Track 3

đang chú ý nhất

có động lực nhất

dạy cách dùng đúng

xin feedback

---

<!-- chiron-source-span: {"source_span_id":"693ceba3-aa8c-53c6-be23-f0a3a341ef54","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Sai kiểu nào tệ hơn — precision, recall, và chi phí lỗi","source_file":"slide-day05.html"},"checksum":"dd89d354b83957c8f3e10ef47d4cef67dd9e745032939944e87de482281b4e06"} -->

## 08 Sai kiểu nào tệ hơn — precision, recall, và chi phí lỗi

Deck B slide 49, 56–58 · deck C slide 10, 22–25. Đây là phần định lượng nhất của 
 Ngày 5, và cũng là phần [Ngày 2](slide-buoi-2.html) đã đặt nền.

### Deck B · slide 56–57 Ví dụ lọc video trẻ em, và trục "user có thấy không"

> Trích deck B 
>  "AI lọc video cho app trẻ em — 100 video, 10 video xấu thật. AI đánh dấu XẤU 13 · AI cho qua 87. 
>  8 ✓ chặn đúng · 5 ✗ báo nhầm (video tốt bị gỡ oan) · 2 ✗ BỎ SÓT (trẻ thấy nội dung xấu) · 
>  85 ✓ cho qua đúng. 
>  PRECISION 8/13 ≈ 62% — khi AI nói CÓ, đúng bao nhiêu? 
>  RECALL 8/10 = 80% — trong số cần tìm, AI tìm được bao nhiêu?" 
>  " Cái nào tệ hơn? Lọt 2 video xấu (trẻ thấy) tệ hơn gỡ oan 5 video tốt → cần RECALL cao. " 
>  " User act theo kết quả sai — FP tệ hơn → PRECISION (Legal RAG chatbot: user thấy 
>  câu trả lời, nhưng sai mà act theo → hậu quả pháp lý nặng). 
>  Bỏ lọt = mất giá trị — FN tệ hơn → RECALL (Copilot, FAQ chatbot: gợi ý nhiều, user tự 
>  lọc — bỏ lọt gợi ý hay = mất giá trị). 
>  Sai mà user KHÔNG BIẾT → thường cần Precision (spam filter, auto-send email). 
>  Nhưng bỏ lọt = thảm họa → Recall bất kể user thấy hay không (content mod trẻ em, 
>  fraud)."

Con số của slide 56 kiểm lại đúng: precision = 8/13 = **61,5%** (slide làm tròn 62%), 
 recall = 8/10 = **80%**. Deck C slide 23 cho một ví dụ thứ hai cũng khớp: quét 1.000 giao 
 dịch, báo 40 lần đúng 30 → precision **75%**; thực có 50 giao dịch xấu, bắt 30 → recall **60%**.

Nhưng phần giá trị nhất là ma trận 2×2 ở slide 57, vì nó thêm một trục mà công thức không có: **user có nhìn thấy lỗi hay không**.

|  | FP tệ hơn (báo nhầm) → Precision | FN tệ hơn (bỏ lọt) → Recall |
| --- | --- | --- |
| User THẤY & sửa được | Legal RAG chatbot — user thấy câu trả lời nhưng act theo, hậu quả pháp lý nặng | Copilot, FAQ chatbot — gợi ý nhiều, user tự lọc; bỏ lọt gợi ý hay = mất giá trị |
| User KHÔNG thấy | Spam filter, auto-send email — "sai mà không ai biết = nguy hiểm" | Content mod trẻ em, fraud — "bỏ lọt = thảm hoạ" |

"Sai mà user KHÔNG BIẾT → thường cần Precision. Nhưng bỏ lọt = thảm 
 hoạ → Recall bất kể user thấy hay không."

hai

thắng

Hậu quả không hồi phục được?

loại nào user không tự phát hiện

không

nhìn thấy

Ngày 2

10%

Mô-đun ngay dưới

ngưỡng báo động nên đặt ở 
 đâu khi đã biết hai loại lỗi đắt khác nhau bao nhiêu?

#### Tương tác Ngưỡng báo động tối ưu khi hai loại lỗi có giá khác nhau

Deck B và deck C đều hỏi "sai kiểu nào tệ hơn" rồi dừng ở câu trả lời định tính. Mô-đun 
 này đi tiếp một bước: nếu bạn *định giá* được hai loại lỗi, ngưỡng báo động tối ưu có công thức — 
 và nó thường thấp hơn nhiều so với trực giác.

Bối cảnh mặc định: **10.000 câu hỏi/tháng**, **5%** thật sự cần chuyển 
 người thật. Escalate nhầm một ca tốn **50 nghìn đ** (công của người xử lý). Bỏ sót một ca 
 cần escalate tốn **1 triệu đ** (khiếu nại, mất khách).

Đoán trước: hệ thống nên báo động khi khả năng "ca này cần người" vượt bao nhiêu phần trăm? Và 
 precision khi đó là bao nhiêu?

#### Kéo rồi mở

**Ngưỡng tối ưu là 4,76%, không phải 50%.** Công thức là `τ* = c FP / (c FP + c FN )` = 50 / (50 + 1.000) = 4,76%. 
 Nghĩa là: *hệ thống nên chuyển người ngay khi mới có 5% khả năng ca này cần người*.

Lý do trực quan: bỏ sót đắt gấp **20 lần** báo nhầm, nên đổi 20 lần báo nhầm để 
 tránh 1 lần bỏ sót vẫn hoà. Ngưỡng hoà vốn chính là 1/21 ≈ 4,76%.

**Và đây là phần khó chịu: precision tại ngưỡng tối ưu chỉ khoảng 30%.** Bảy trên 
 mười lần escalate là "không cần thiết". Nếu bạn đánh giá hệ thống bằng precision, bạn sẽ kết luận 
 nó tệ — trong khi nó đang ở đúng điểm rẻ nhất có thể.

**So sánh với ngưỡng 50%** (phản xạ mặc định: "chỉ báo khi chắc hơn không"): 
 precision đẹp hơn hẳn — **78,6%** — nhưng recall rơi xuống 52,9% và tổng chi phí là **239,2 triệu đ/tháng** so với **103,0 triệu đ**. Ngưỡng "trông hợp lý" 
 đắt gấp **2,3 lần** ngưỡng tối ưu.

**Thử điều đáng thử nhất — kéo tỉ lệ ca thật từ 5% xuống 1%:** ngưỡng tối ưu *không đổi* (nó chỉ phụ thuộc tỉ lệ chi phí), nhưng precision rơi thảm hại. Đây đúng là 
 nghịch lý tỉ lệ nền của [Ngày 2](slide-buoi-2.html), và nó cho thấy vì sao precision là 
 một chỉ tiêu tồi để đặt vào PRD: *nó thay đổi theo tỉ lệ nền, thứ bạn không kiểm soát được.*

*Bài học vận hành:* ba con số bạn cần trước khi đặt bất kỳ ngưỡng nào là **giá của một lần báo nhầm, giá của một lần bỏ sót, và tỉ lệ nền**. Không có ba số đó, 
 mọi ngưỡng đều là phỏng đoán — và phỏng đoán mặc định của con người (50%) gần như luôn sai theo 
 hướng đắt.

- **Control - Chất lượng model (d′): 2,5**: min `5`, max `40`, step `1`, default `25`

- **Control - Tỉ lệ ca thật sự cần bắt: 5,0%**: min `5`, max `300`, step `5`, default `50`

- **Control - Giá một lần báo nhầm: 50 nghìn đ**: min `10`, max `500`, step `10`, default `50`

- **Control - Giá một lần bỏ sót: 1,0 triệu đ**: min `50`, max `5000`, step `50`, default `1000`

- **Control - Số ca mỗi tháng: 10.000**: min `1000`, max `50000`, step `1000`, default `10000`

Ngưỡng báo động tối ưu

—

—

Precision / Recall khi đó

—

—

Chi phí lỗi mỗi tháng

—

—

Tiết kiệm so với ngưỡng 50%

—

—

chính sách cực đoan ngưỡng 50% — phản xạ mặc định ngưỡng 20% ngưỡng tối ưu

#### Xem bảng quét ngưỡng



#### Công thức & giới hạn của mô hình

- Ngưỡng tối ưu theo quy tắc Bayes: báo động khi P(cần bắt | dữ liệu) 
 vượt τ* = c FP / (c FP + c FN ). Đây là kết quả chuẩn và 
 không phụ thuộc tỉ lệ nền — chỉ phụ thuộc tỉ lệ hai chi phí.
- Precision, recall và chi phí thì có phụ thuộc tỉ lệ nền, và được tính 
 từ một mô hình ROC binormal đẳng phương sai: điểm số của ca "thật sự có" phân phối 
 N(d′, 1), ca "thật sự không" phân phối N(0, 1). Đây là mô hình chuẩn 
 trong lý thuyết phát hiện tín hiệu; d′ ≈ 2,5 tương ứng một classifier khá tốt (AUC ≈ 0,96).
- Không có con số nào trong mô-đun này lấy từ slide. Cả deck B và deck C đều dừng 
 ở phân tích định tính "sai kiểu nào tệ hơn". Bối cảnh 10.000 ca/tháng, 5% tỉ lệ nền, 50 nghìn đ và 
 1 triệu đ là giả định minh hoạ của tài liệu này. Xem 
 Con số cần kiểm chứng.
- Mô hình giả định chi phí là hằng số cho mọi ca. Thực tế phân bố lệch nặng: hầu 
 hết ca bỏ sót tốn ít, một vài ca tốn cực nhiều. Khi phân bố lệch như vậy, dùng chi phí 
 trung bình vẫn cho ngưỡng đúng về mặt kỳ vọng, nhưng không bảo vệ bạn khỏi ca đuôi — và ca 
 đuôi mới là ca lên báo.
- Mô hình không tính chi phí gián tiếp của precision thấp: người xử lý bị ngập 
 cảnh báo sai sẽ dần bỏ qua cảnh báo (alert fatigue), làm recall thực tế sụp đổ. Đây là lý do ngưỡng 
 tối ưu về mặt toán học đôi khi vẫn cần được nâng lên vì lý do vận hành — 
 một quyết định sản phẩm, không phải một phép tính.

### Deck C · slide 24–25 Từ "lỗi nào đắt hơn" sang "prototype phải xử lý path nào"

> Trích deck C 
>  " Báo nhầm đắt hơn → prototype cần confirmation, source, confidence, human review 
>  hoặc undo rõ. Bỏ sót đắt hơn → prototype cần cảnh báo sớm, hỏi thêm, escalation hoặc 
>  checklist bắt buộc. Cả hai đều đắt → không automate vội. Dùng augmentation: AI đề 
>  xuất, người quyết, log correction. Cả hai đều nhẹ → có thể cho AI thử nhiều hơn, 
>  nhưng vẫn cần cách user sửa nhanh và report lỗi." 
>  " Gợi ý viết code: gợi ý sai — lập trình viên bỏ qua hoặc sửa, cái giá thấp. Bỏ lỡ 
>  một gợi ý hữu ích — chỉ là mất một cơ hội. → Báo nhầm rẻ → recall cao chấp nhận được. " 
>  " Không có đáp án chung: chọn ưu tiên precision hay recall là một quyết định sản phẩm, 
>  phụ thuộc lỗi nào gây hậu quả nặng hơn cho chính người dùng của mình."

Bảng 2×2 của slide 24 là bảng dùng được nhất trong cả deck C, vì nó chuyển thẳng từ phân tích sang *việc phải build*. Ghép nó với công thức ở [mô-đun act/ask](#m-ev) thì thấy nó là cùng 
 một điều nói bằng hai ngôn ngữ:

| Tình huống | Deck C bảo build gì | Trong ngôn ngữ act/ask |
| --- | --- | --- |
| Báo nhầm đắt hơn | Confirmation, source, confidence, human review, undo | Hạ C bằng undo và preview, hoặc chuyển sang ask |
| Bỏ sót đắt hơn | Cảnh báo sớm, hỏi thêm, escalation, checklist bắt buộc | Hạ ngưỡng báo động (đúng mô-đun chi phí lỗi ) và chấp nhận precision thấp |
| Cả hai đều đắt | Không automate vội — augmentation, log correction | Chọn ask: cả EV(act) lẫn EV(inaction) đều tệ, ask thắng |
| Cả hai đều nhẹ | Cho AI thử nhiều hơn, vẫn cần cách sửa nhanh | C nhỏ ⇒ p* thấp ⇒ act ở độ chắc thấp vẫn có lời |

và công bằng

thường nghiêng 
 precision

"và công bằng"

tác hại lên cá nhân bị từ chối

fairness

deck A slide 13–14

khung chi phí kỳ vọng là chưa đủ

rơi vào 
 ai

guardrail và audit sample của Ngày 24

---

<!-- chiron-source-span: {"source_span_id":"eaf56db3-81f5-57b8-adde-8ab8083110ba","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 Eval flow ba giai đoạn — vì sao là chu trình, không phải một lần chấm","source_file":"slide-day05.html"},"checksum":"d4e7d3b077c1867fd8fa697c45a228c7fe5ea74aa22ac6946f6d884f5f30e274"} -->

## 09 Eval flow ba giai đoạn — vì sao là chu trình, không phải một lần chấm

Deck B slide 59–62 · deck C slide 21. Đây là phần nối Ngày 5 với [Ngày 24 của Track 3](track-3-day-24.html), và là phần trả lời trụ thứ ba của deck C: *"Bao nhiêu% sai là chấp nhận được?"*

### Deck B · slide 59–60 Eval khác test phần mềm ở ba chỗ

> Trích deck B 
>  " Lúc demo — mọi thứ trong tầm kiểm soát: 10–20 case do team tự chọn · input 
>  'sạch', đúng kịch bản đã chuẩn bị · chạy vài lần thấy ổn → kết luận 'xong'. 
>  Lúc user thật dùng — không còn kiểm soát được input: hàng nghìn câu hỏi mỗi ngày · 
>  user hỏi theo cách team chưa từng nghĩ tới · AI chắc chắn sẽ có lúc sai — vấn đề là sai bao nhiêu, 
>  sai ở đâu. " 
>  " Chất lượng AI là một phân bố — đúng bao nhiêu%, trên loại case nào. Muốn biết 
>  con số đó thì phải đo, và phải đo liên tục." 
>  " Kết quả: test thường — cùng input, cùng output, pass hoặc fail rõ ràng; eval — 
>  cùng input, mỗi lần một khác, 'đúng' là chuyện mức độ. 
>  Bộ câu hỏi: test thường — viết một lần, chạy mãi; eval — phải lớn dần theo case 
>  thật từ user, không bao giờ 'đủ'. 
>  Khi nào đo: test thường — trước khi release; eval — trước release và liên tục sau 
>  release."

Ba dòng khác biệt này có ba hệ quả tổ chức rất cụ thể, và chúng là lý do eval hay bị bỏ:

| Khác biệt | Hệ quả lên công việc | Vì sao hay bị bỏ |
| --- | --- | --- |
| "Đúng" là chuyện mức độ | Phải có rubric — ai đó phải định nghĩa "đủ tốt" bằng chữ | Viết rubric là việc khó, mơ hồ, và không ai muốn nhận |
| Bộ câu hỏi phải lớn dần | Phải có đường ống từ production traces về eval set | Đây là hạ tầng, không phải tính năng — không xuất hiện trên roadmap |
| Đo liên tục sau release | Phải có ngân sách vận hành sau khi ship, và người sở hữu nó | Team thường bị điều sang dự án tiếp theo ngay sau launch |

"do team tự chọn"

mô hình tinh thần của team về user

messy, edge, 
 ambiguous

không phải từ trực 
 giác

#### Tương tác Demo xanh không phải bằng chứng — bao nhiêu case mới đủ?

Deck B chê "3 test case xanh → ship" và đề nghị bắt đầu bằng 20 case. Mô-đun này tính 
 xem hai con số đó thật sự nói lên điều gì: xác suất demo qua sạch, và độ rộng của khoảng tin cậy khi bạn 
 kết luận từ n case.

Mặc định: model thật sự đúng **80%** số lần. Bạn demo **3** case và 
 eval set có **20** case.

Đoán trước: xác suất cả 3 case demo đều xanh là bao nhiêu? Và nếu thấy 16/20 case đạt, bạn kết luận 
 được model đúng trong khoảng nào?

#### Kéo rồi mở

**Xác suất 3 case demo đều xanh: 51,2%** (0,8³). Nghĩa là một model sai một phần 
 năm số lần vẫn qua được buổi demo *hơn một nửa số lần*. Đây chính xác là cái deck B gọi là 
 "vài test case là demo, không phải distribution".

**Cần 14 case** mới có 95% khả năng bắt được ít nhất một lỗi ở model 80% 
 ( `ln 0,05 / ln 0,8 = 13,4 → 14` ). Con số 20 của deck B nằm ngay trên ngưỡng này — hợp lý 
 cho mục đích *tìm ra failure mode*.

**Nhưng 20 case không đủ làm quality gate.** Thấy 16/20 thì khoảng tin cậy 95% là **58% – 92%** — rộng tới 34 điểm. Bạn không phân biệt nổi một model 60% với một model 
 90%. Bảng bên dưới cho thấy cần khoảng **150 case** để thu khoảng còn ±5 điểm, và 
 khoảng **870 case** để còn ±2 điểm.

**Thử điều đáng thử nhất — kéo tỉ lệ đúng lên 95%:** giờ cần **59** case mới có 95% khả năng thấy một lỗi. *Model càng tốt, càng cần nhiều case để phát hiện nó tệ 
 đi.* Đây là lý do eval set phải lớn dần theo chất lượng sản phẩm — một bộ 20 case đủ dùng ở 
 tháng đầu sẽ mù hoàn toàn ở tháng thứ sáu.

*Bài học vận hành:* hai con số phục vụ hai mục đích khác nhau và đừng lẫn. **Tìm lỗi** cần vài chục case đa dạng. **Chặn regression** cần vài trăm 
 case, vì bạn đang cố phát hiện một thay đổi *vài điểm phần trăm* — và một khoảng tin cậy 
 rộng 30 điểm không thấy được điều đó.

- **Control - Tỉ lệ đúng thật của model: 80%**: min `50`, max `99`, step `1`, default `80`

- **Control - Số case demo: 3**: min `1`, max `20`, step `1`, default `3`

- **Control - Kích thước eval set: 20**: min `5`, max `500`, step `5`, default `20`

Xác suất demo qua sạch

—

—

Số case cần để thấy lỗi

—

—

Khoảng tin cậy 95%

—

—

Độ rộng khoảng

—

—

model của bạn model 95% model 70%

#### Xem bảng: eval set bao nhiêu case thì đủ làm gì



#### Công thức & giới hạn của mô hình

- P(k case đều đạt) = p^k. Số case cần để có 95% khả năng thấy ít nhất một lỗi: 
 k ≥ ln(0,05) / ln(p).
- Khoảng tin cậy dùng công thức Wilson (chính xác hơn công thức chuẩn Wald ở n 
 nhỏ và p gần 0 hoặc 1 — Wald cho khoảng vượt ra ngoài đoạn 0–1, còn Wilson thì không).
- Giả định độc lập: mọi case rút độc lập từ cùng một phân bố. Thực tế eval set 
 thường có case tương quan (nhiều biến thể của cùng một câu hỏi), nên khoảng tin cậy thật 
 rộng hơn con số mô-đun đưa ra. Nói cách khác: mô-đun này đã là ước lượng lạc quan.
- Mô hình một tỉ lệ duy nhất. Thực tế chất lượng khác nhau theo loại case, và đó 
 mới là thông tin hữu ích: 90% tổng thể có thể là 98% trên câu dễ và 40% trên câu mơ hồ — hai sản 
 phẩm hoàn toàn khác nhau. Deck C slide 21 gọi đúng việc này: "phân loại lỗi trước khi sửa".
- Con số 20 case và 3 test case là của deck B (slide 24). Mọi phép tính xác suất 
 và khoảng tin cậy ở đây là bổ sung của tài liệu này; slide không tính. Xem 
 Con số cần kiểm chứng.

### Deck B · slide 61–62 · deck C slide 21 Ba giai đoạn, và mũi tên khép vòng

> Trích deck B 
>  " 01 · Vibe Check (chấm tay, cảm tính) — chạy thử 10–30 case rồi tự chấm tay. Mục 
>  đích: hiểu AI hay sai kiểu gì — chưa cần con số chính thức. Khi nào: lúc còn prototype — trước cả 
>  khi viết PRD. " 
>  " 02 · Offline Eval (chấm tự động, trước ra mắt) — có bộ câu hỏi chuẩn (reference 
>  dataset). Mỗi lần đổi prompt / model → chạy lại toàn bộ, so với phiên bản hiện tại. Qua 
>  'cổng chất lượng' (quality gate) mới được release. Cái từng chạy tốt nay tệ đi = 
>  regression (lỗi quay đầu). " 
>  " 03 · Online Monitoring (theo dõi sau ra mắt) — user thật tạo case mới không lường 
>  trước. Gom tín hiệu: thumbs up/down, user gõ lại prompt, bỏ giữa chừng. 
>  Case lạ → đưa ngược về bộ câu hỏi chuẩn. " 
>  " Case thật từ online chảy ngược về bộ câu hỏi offline — bộ câu hỏi ngày càng chuẩn. Vì vậy 
>  gọi là chu trình, không phải chấm một lần. "

Ba giai đoạn ứng đúng với ba pha của sản phẩm, và điều đáng chú ý là **giai đoạn 1 diễn ra 
 trước cả khi viết PRD** — deck B nói thẳng điều đó, và nó đảo ngược thứ tự mà nhiều người giả 
 định:

| Giai đoạn | Pha sản phẩm | Chấm bằng gì | Trả lời câu hỏi gì | Đầu ra dùng vào đâu |
| --- | --- | --- | --- | --- |
| 01 Vibe Check | Prototype — trước khi viết PRD | Người, chấm tay, 10–30 case | "AI hay sai kiểu gì?" | Viết được failure modes section của PRD |
| 02 Offline Eval | Build | Tự động, trên reference dataset | "Bản mới có tệ đi so với bản cũ không?" | Quality gate — được release hay không |
| 03 Online Monitoring | Production | Tín hiệu hành vi user + audit sample | "Có drift không? Có failure mode mới không?" | Case mới chảy ngược về giai đoạn 02 |

không biết trước AI sẽ 
 sai kiểu gì

chạy tay vài chục case

rồi mới viết failure modes section có nội dung thật

"Tip: prototype câu trả lời 
 bằng ChatGPT/Claude (upload transcript → generate)"

trước

lỗi đó không bao giờ được phép quay lại mà không ai biết

regression test

tín hiệu hành vi

explicit · behavioral · outcome

_Sơ đồ: Chu trình eval ba giai đoạn với dòng chảy ngược từ production về bộ câu hỏi chuẩn - Ba hộp xếp ngang theo pha sản phẩm. Hộp một là vibe check ở pha prototype, chấm tay mười tới ba mươi case để hiểu AI sai kiểu gì, và đầu ra của nó là mục failure modes trong tài liệu spec. Hộp hai là offline eval ở pha build, chạy tự động trên bộ câu hỏi chuẩn mỗi lần đổi prompt hoặc model, và đóng vai trò cổng chất lượng quyết định có được phát hành hay không. Hộp ba là online monitoring ở pha production, thu tín hiệu từ người dùng thật gồm đánh giá tốt xấu, việc gõ lại câu hỏi và việc bỏ giữa chừng. Một mũi tên cong đi ngược từ hộp ba về hộp hai thể hiện case lạ từ production được đưa trở lại bộ câu hỏi chuẩn, biến quy trình thành một chu trình khép kín thay vì một đường thẳng._

Hình 3 — chu trình eval ba giai đoạn.

"case thật từ online chảy ngược về bộ câu hỏi offline"

---

<!-- chiron-source-span: {"source_span_id":"effc8b4e-f0c8-54d9-919f-bdcc06f0b2e6","locator":{"kind":"html_section","section_id":"c10","order":12,"heading":"10 Responsible AI, risk register & go/no-go","source_file":"slide-day05.html"},"checksum":"c00cdd10102400ab081f6366944e290554bd5bbed846ac5cf5821bc5f7b04a3f"} -->

## 10 Responsible AI, risk register & go/no-go

Deck A slide 12–15, 32–35. Phần này gần như chỉ có ở deck A, và là phần trực tiếp 
 phục vụ nửa sau của deliverable Lab 5.

### Deck A · slide 13–15 Năm trụ Responsible AI — dịch sang ngôn ngữ requirement

> Trích deck A 
>  " 5 trụ cột: không thiên lệch bất hợp lý · đủ ổn định để user tin dùng · chỉ dùng 
>  dữ liệu thật sự cần thiết · phù hợp với nhiều nhóm người dùng · biết AI làm gì và giới hạn ở đâu. 
>  Các nguyên tắc này cần được chuyển thành product decisions, requirements, và risk items. " 
>  " Bias — hỏi khi discovery: 'AI có đối xử khác nhau giữa các nhóm user không?' → 
>  requirement: test set đa dạng, human review cho case nhạy cảm. 
>  Privacy — 'Có PII / dữ liệu nhạy cảm không?' → data minimization, masking, 
>  retention policy. 
>  Transparency — 'User có biết đây là AI và khi nào nên override không?' → 
>  disclosure, citation, escalation path." 
>  " AI Act EU 2024: Không cần học thuộc luật; cần hiểu rằng một số use case AI sẽ bị 
>  yêu cầu risk management, documentation, và human oversight chặt hơn. Với PM/BA, tác 
>  động thực tế là: requirement, logging, disclosure, exception handling, và review process phải 
>  được nghĩ từ đầu. Khi sản phẩm đi vào ngành nhạy cảm như tuyển dụng, tín dụng, y tế, giáo 
>  dục, mức độ cẩn trọng phải tăng mạnh." 
>  "Lưu ý: Responsible AI không chỉ là 'đúng về mặt đạo đức', mà còn là giảm rủi ro vận hành 
>  và pháp lý. "

Bảng slide 14 là bảng hữu ích nhất trong nhóm này vì nó có cột thứ ba: *"phải đi vào requirement 
 nào"*. Đó chính là thao tác biến một nguyên tắc thành một dòng có thể kiểm chứng. Tôi thêm cột thứ 
 tư — **ai kiểm và kiểm bằng gì** — vì đó là chỗ dòng requirement thường chết:

| Vấn đề | Hỏi gì khi discovery | Đi vào requirement nào | Kiểm bằng gì |
| --- | --- | --- | --- |
| Bias | AI có đối xử khác nhau giữa các nhóm user không? | Test set đa dạng · human review cho case nhạy cảm | Chạy eval tách theo nhóm, so tỉ lệ đạt giữa các nhóm — con số tổng thể che mất chênh 
 lệch |
| Privacy | Có PII / dữ liệu nhạy cảm không? | Data minimization · masking · retention policy | Kiểm log xem PII có bị ghi không; kiểm job xoá có chạy đúng hạn không |
| Transparency | User có biết đây là AI và khi nào nên override không? | Disclosure · citation · escalation path | Citation kiểm tự động được (tỉ lệ có nguồn); disclosure kiểm bằng review giao diện |

có nhãn nhóm trên eval set

xung đột

Điểm cần nhớ cho vấn đáp:

chúng đánh đổi với nhau

"Responsible AI không chỉ là 'đúng về mặt đạo đức', mà còn là giảm rủi ro vận hành và pháp lý."

ba nghĩa vụ

risk management, documentation, human oversight

### Deck A · slide 32–35 Năm nhóm risk, ma trận likelihood × impact, ba mức go/no-go

> Trích deck A 
>  " Technical — hallucination, tool failure, latency spike → eval, fallback, timeouts, 
>  monitoring. Data — PII leak, stale source, bad labeling → masking, access control, 
>  data QA. Business — adoption thấp, unclear ROI, wrong workflow fit → pilot, success 
>  metrics, JTBD validation. Ethical — unfair outcome, opaque decision → human review, 
>  disclosure, audit sample. Regulatory — logging thiếu, compliance gap → 
>  documentation, approval flow, policy review." 
>  " Risk Matrix: Likelihood × Impact — vùng Monitor · Mitigate · Reduce · 
>  Escalate/Go-No-Go. 1: Privacy leak · 2: Hallucination on sensitive advice · 3: Cost spike · 
>  4: Adoption risk · 5: Minor wording inconsistency" 
>  " Go: risk cao đã có mitigation rõ, acceptance criteria đo được, owner rõ. 
>  Conditional go: pilot giới hạn, human-in-the-loop, guardrails chặt, scope hẹp. 
>  No-go: chưa xử lý privacy / compliance risk lớn, chưa có fallback, hoặc chưa chứng 
>  minh user value." 
>  " Risk register giúp team biết build trong điều kiện nào, ship ở mức nào, và khi nào phải 
>  dừng. "

Năm nhóm risk đáng thuộc, và điều đáng chú ý là **chúng được phát hiện ở những thời điểm rất 
 khác nhau** — thứ tự đó quyết định bạn phải chuẩn bị gì trước:

| Nhóm | Ví dụ | Mitigation của slide | Phát hiện được lúc nào |
| --- | --- | --- | --- |
| Technical | Hallucination, tool failure, latency spike | Eval, fallback, timeouts, monitoring | Sớm nhất — ngay ở vibe check |
| Data | PII leak, stale source, bad labeling | Masking, access control, data QA | Lúc thiết kế đường ống dữ liệu |
| Ethical | Unfair outcome, opaque decision | Human review, disclosure, audit sample | Chỉ khi chủ động đi tìm — eval tách theo nhóm, audit mẫu |
| Regulatory | Logging thiếu, compliance gap | Documentation, approval flow, policy review | Thường lúc review pháp lý — quá muộn để đổi kiến trúc |
| Business | Adoption thấp, unclear ROI, wrong workflow fit | Pilot, success metrics, JTBD validation | Muộn nhất — chỉ biết sau khi ship, đôi khi sau vài tháng |

hai trong ba case (Gamma, và cả 
 "user không dùng" của deck A) là business risk

pilot, success metrics, JTBD 
 validation

trước khi build

Ma trận likelihood × impact của slide 34 xếp năm rủi ro cụ thể vào bốn vùng. Slide không ghi ngưỡng 
 số, nhưng logic thì rõ và có thể đọc ra được từ vị trí năm điểm:

| Rủi ro | Likelihood | Impact | Vùng | Nghĩa là phải làm gì |
| --- | --- | --- | --- | --- |
| 1 · Privacy leak | Thấp | Rất cao | Escalate / Go-No-Go | Không phải team quyết — phải đưa lên cấp có thẩm quyền, và có thể là lý do no-go |
| 2 · Hallucination on sensitive advice | Cao | Cao | Reduce | Phải giảm bằng thiết kế: guardrail, citation bắt buộc, thu hẹp phạm vi trả lời |
| 3 · Cost spike | Trung bình | Trung bình | Mitigate | Có biện pháp giảm nhẹ: budget alert, rate limit, cache |
| 4 · Adoption risk | Cao | Trung bình | Mitigate | Pilot hẹp, đo sớm, sẵn sàng đổi hướng |
| 5 · Minor wording inconsistency | Cao | Rất thấp | Monitor | Ghi nhận, theo dõi, không tốn công xử lý |

hiếm

nhỏ nhưng thường xuyên

rủi ro impact rất cao là rủi ro không hồi phục 
 được

"Escalate / Go-No-Go"

một quyết định thuộc thẩm quyền khác

Quy tắc rút ra:

thắng

chương 08

mô-đun act/ask

| Mức | Điều kiện của slide | Nói cách khác |
| --- | --- | --- |
| Go | Risk cao đã có mitigation rõ · acceptance criteria đo được · 
 owner rõ | Ba thứ, và owner là thứ hay thiếu nhất |
| Conditional go | Pilot giới hạn · human-in-the-loop · guardrails 
 chặt · scope hẹp | Bốn cách thu nhỏ rủi ro mà không phải huỷ dự án |
| No-go | Chưa xử lý privacy/compliance risk lớn · chưa có fallback · 
 hoặc chưa chứng minh user value | Điều kiện thứ ba không phải kỹ thuật — và là điều kiện hay bị bỏ qua nhất |

Conditional go là mức làm cho risk register trở nên hữu ích

bốn cách hạ C

p* = 1 − I/(V+C)

chương 04

**Kiểm tra 4** Risk register của bạn có dòng: *"Hallucination — likelihood: 
 cao, impact: cao, mitigation: cải thiện prompt."* Nêu *hai* vấn đề, và viết lại dòng đó cho 
 đúng chuẩn deck A.

#### Xem đáp án

**① Mitigation không kiểm chứng được.** "Cải thiện prompt" không có tiêu chí hoàn 
 thành, không đo được, và — theo [deck C slide 9](#sc8) — chính nó là nguồn *prompt drift*. Slide 33 gợi ý mitigation cho nhóm Technical là "eval, fallback, timeouts, 
 monitoring": bốn thứ có thể xác nhận là đã có hay chưa.

**② Không có owner.** Deck A slide 35 nêu ba điều kiện của "Go" và owner là một trong 
 ba. Một rủi ro không có tên người là một rủi ro không ai xử lý.

*Còn một vấn đề thứ ba nếu muốn nói thêm:* "hallucination" quá rộng để làm một dòng risk. 
 Bịa số liệu, bịa chính sách, và bịa nguồn trích dẫn là ba rủi ro có impact và mitigation khác hẳn nhau.

**Viết lại:** *"Bịa nội dung chính sách khi câu hỏi nằm ngoài kho tài liệu — 
 likelihood: cao (đã thấy ở vibe check, 6/30 case) · impact: cao (cam kết sai với khách, tiền lệ Air 
 Canada) · vùng: Reduce · mitigation: ① bắt buộc trả lời kèm citation, không có nguồn thì từ chối có 
 kiểm soát; ② eval riêng 20 case ngoài phạm vi, quality gate ≥ 95% từ chối đúng; ③ log mọi câu không 
 tìm được nguồn để review hàng tuần · owner: [tên] · kiểm lại: mỗi lần đổi prompt hoặc model."*

---

<!-- chiron-source-span: {"source_span_id":"b4f47386-38f6-589e-9592-ee9da7d846ee","locator":{"kind":"html_section","section_id":"c11","order":13,"heading":"11 Từ bug đến spec — failure taxonomy và công thức debrief","source_file":"slide-day05.html"},"checksum":"b75019243d5ad36705d3d103b118ff3fc8b2b2acab90159ac0fe35a5cc7fa56e"} -->

## 11 Từ bug đến spec — failure taxonomy và công thức debrief

Deck C slide 20, 29–31, 37–38 · deck B slide 25–26. Đây là phần thao tác nhất của 
 Ngày 5: biến một quan sát "bot lỗi" thành một dòng trong tài liệu.

### Deck C · slide 20 Failure mode library — liệt kê cách hỏng trước khi viết tính năng

> Trích deck C 
>  " Trước khi viết feature, liệt kê cách product có thể sai. 
>  Hỏi ngoài phạm vi → bot bịa chính sách hoặc điều khoản → từ chối có kiểm soát, 
>  dẫn tới nguồn chính thức hoặc người thật. 
>  Input mơ hồ → hiểu sai intent, trả lời đúng format nhưng sai nhu cầu → hỏi lại, 
>  đưa lựa chọn, không tự đoán quá sâu. 
>  Dữ liệu cũ hoặc thiếu → output tự tin nhưng sai thực tế → hiện thời điểm cập 
>  nhật, confidence, fallback lookup. 
>  Prompt injection → user kéo bot ra khỏi vai trò hoặc policy → instruction 
>  hierarchy, refusal, log red flag." 
>  " Bài học Air Canada: vấn đề không chỉ là 'bot cần thông minh hơn', mà là product cần biết 
>  khi nào không được trả lời. "

Bảng ba cột *trigger → hậu quả → mitigation* là khuôn đơn giản nhất mà vẫn đủ dùng. Bốn dòng 
 của deck C phủ đúng bốn hạng mục của [lớp input uncertainty](#sc8) — không phải trùng hợp:

| Trigger | Ứng với hạng mục input nào | Mitigation thuộc bước nào (DETECT/ROUTE/…) |
| --- | --- | --- |
| Hỏi ngoài phạm vi | — | DETECT (nhận ra ngoài phạm vi) + ROUTE (từ chối có kiểm soát, 
 dẫn tới nguồn chính thức) |
| Input mơ hồ | "dùng từ mơ hồ" | ROUTE — hỏi lại, đưa lựa chọn |
| Dữ liệu cũ hoặc thiếu | "thiếu context" | DETECT (biết dữ liệu stale) + hiện thời điểm cập nhật cho user |
| Prompt injection | "cố tình prompt injection" | DETECT + ROUTE (refusal) + LEARN (log red flag) |

Từ chối

Có kiểm soát

đường đi tiếp

silent skip

human handoff

deck B slide 24

"AI tốt không phải AI luôn có câu trả 
 lời"

"Chính sách hoàn tiền tôi không tra được; 
 đây là link trang chính thức và số hotline"

đã thấy

bốn hạng mục tổng quát

Microsoft HAX Playbook

"Playbook tự suy ra các kiểu lỗi, kịch bản cần 
 test"

bề mặt lỗi suy ra được từ cấu hình, trước khi hệ thống tồn tại.

### Deck B · slide 25–26 Case BatchBuddy: bản đồ chín kịch bản, và một dòng đáng nhớ

> Trích deck B 
>  "Chatbot kênh #batch02-general · source of truth: deadline 20:00 22/06/2026 · trigger: bot tự đoán 
>  khi nào nói. 
>  Correct operation (1) — user hỏi deadline → bot trả đúng; không nói khi không cần. 
>  Input errors (1) — typo trong câu hỏi (truncation, substitution, insertion, 
>  swapping). Trigger errors (3) — missed: đáng nói thì im · spurious: 
>  không ai hỏi vẫn nói · delayed: nói quá trễ. Delimiter errors (0) — 
>  '0' cũng là một câu trả lời có ý nghĩa — lớp này được xét và loại trừ, không phải bị quên. 
>  Response generation (4) — ambiguities · implausible · plausible-but-incorrect 
>  · inappropriate." 
>  " ⚠ Ví dụ SCN08 — plausible-but-incorrect. User hỏi deadline, bot trả '18:00 22/06' 
>  — nghe hợp lý nhưng sai (đúng: 20:00). Kiểu sai nguy hiểm nhất: hợp lý nên khó bị phát hiện. " 
>  " Nếu có nút bấm để hỏi thay vì tự đoán → 3 lỗi trigger biến mất. Cấu hình quyết định bề mặt 
>  rủi ro. "

Case này nhỏ nhưng là case dạy học tốt nhất trong deck B, vì ba lý do:

| Chi tiết | Vì sao đáng chú ý |
| --- | --- |
| "Delimiter errors: 0" — và ghi rõ "lớp này được xét và loại trừ, không 
 phải bị quên" | Đây là dấu hiệu của một bản đồ lỗi làm nghiêm túc. Ghi số 0 có giải thích khác hẳn với 
 bỏ trống: nó chứng minh lớp đó đã được cân nhắc |
| "plausible-but-incorrect" — 18:00 thay vì 20:00 | Loại lỗi nguy hiểm nhất vì nó vượt qua mọi kiểm tra bằng cảm giác. Không sai định dạng, 
 không sai ngữ pháp, không vô lý — chỉ sai |
| "Nút bấm thay vì tự đoán → 3 lỗi trigger biến mất" | Một thay đổi cấu hình tương tác xoá sạch một phần ba bản đồ lỗi. Không cần model tốt 
 hơn, không cần prompt tốt hơn |

"Cấu hình quyết định bề mặt rủi ro."

chỉ tồn tại vì bot tự quyết định 
 khi nào nói

không còn khả năng xảy ra

act

Cách dùng thực tế:

có thay đổi cấu hình nào xoá sạch một nhóm không?

### Deck C · slide 29–31, 37–38 Năm lớp taxonomy, công thức bug→decision, và 4 paths

> Trích deck C 
>  " Bug chỉ là bằng chứng. Framework mới biến bug thành quyết định. 
>  Promise — user kỳ vọng gì? · Intent — AI hiểu đúng ý định không? · 
>  Data/Tool — có nguồn và tool đúng không? · Safety/Behavior — AI có hành vi rủi ro 
>  không? · UX Recovery — user recover thế nào?" 
>  " Mỗi finding phải được viết lại thành một product decision: Khi user [trigger], 
>  AI/product [failure], hậu quả là [impact], lỗi thuộc layer [taxonomy], nên sửa bằng 
>  [requirement / eval / UX / data / automation], đo bằng [metric hoặc signal]." 
>  " Công thức debrief: đừng ghi 'bot lỗi'. Hãy ghi: finding → layer → product decision → 
>  SPEC field → test/failure path. " 
>  " User Stories của AI product là 4 paths, không phải một dòng happy path: 
>  Happy — AI đúng và tự tin, user thấy gì? · Low-confidence — AI không chắc, có hỏi 
>  lại không? · Failure — AI sai, user recover thế nào? · Correction — user sửa, data 
>  đi vào đâu?"

Năm lớp taxonomy hữu ích vì chúng **chỉ thẳng tới người phải sửa** — và đó là toàn bộ 
 lý do phân loại lỗi trước khi sửa:

| Lớp | Ví dụ của deck C | Ai sửa | Sửa bằng cách gì |
| --- | --- | --- | --- |
| Promise | "NEO trông như bot tra chuyến bay, nhưng cần mã chuyến bay" | PM + designer | Đổi capability cue, đổi copy, đổi onboarding — không đụng model |
| Intent | "'linh tinh' bị hiểu như keyword thay vì khái niệm mơ hồ" | PM + engineer | Low-confidence path: hỏi lại tiêu chí, đưa 2–3 lựa chọn |
| Data / Tool | "Trả link chung, không tra được dữ liệu cần thiết" | Engineer / data | Thêm nguồn, sửa tool, sửa retrieval |
| Safety / Behavior | "Prompt injection, đồng ý với user dù dữ liệu mâu thuẫn" | Engineer + policy | Instruction hierarchy, guardrail, refusal |
| UX Recovery | "Không typing indicator, duplicate response, không correction loop" | Designer + engineer | Trạng thái, nút thử lại/huỷ, đường sửa |

user correction rate

lần sau

ngay lần này

"đo bằng"

user correction rate

behavioral signal

deck A slide 19

Bảng "map vào SPEC" ở slide 31 là bảng nên copy nguyên vào quy trình debrief của team. Nó có bốn 
 dòng, và cột thứ ba — *"ghi vào SPEC như thế nào"* — là cột làm nên giá trị:

| Finding thấy được | Nghĩa product thật sự | Ghi vào SPEC như thế nào |
| --- | --- | --- |
| Prompt injection | "User có thể kéo AI ra khỏi vai trò. Đây không phải 'bug vui', mà là lỗi boundary + safety" | "Top failure mode: khi user yêu cầu bỏ qua policy, AI phải từ chối, giải thích phạm vi và 
 handoff/log red flag" |
| Keyword "linh tinh" | "AI hiểu chữ, nhưng không hiểu intent mơ hồ. Vấn đề nằm ở low-confidence path" | "4 paths: với query mơ hồ, AI hỏi lại tiêu chí hoặc đưa 2–3 lựa chọn; thêm eval case 
 cho input mơ hồ " |
| Không có typing indicator | "User không biết AI đang xử lý, bị treo hay đã hỏng. Lỗi trust + latency signal" | "UX recovery: hiện trạng thái, bước đang làm, thời gian chờ, nút thử lại/huỷ/chuyển người" |
| Kỳ vọng lệch / trả trùng | "Promise không khớp khả năng thật; lỗi lặp lại chứng tỏ thiếu regression test " | "Trust + Eval: viết rõ boundary ngay onboarding; thêm test case 'không lặp câu trả lời' và 
 metric report/correction" |

log red flag

thêm eval case

nút thử lại

test case + metric

sau khi viết xong, có ai kiểm được là đã làm 
 hay chưa không?

| Path | Câu hỏi | Ví dụ quyết định UX | Ai được lợi |
| --- | --- | --- | --- |
| Happy | AI đúng và tự tin, user thấy gì? | Gợi ý hiện rõ, accept một thao tác | User, ngay lập tức |
| Low-confidence | AI không chắc, có hỏi lại không? | Hiện 2–3 lựa chọn hoặc yêu cầu thêm thông tin | User, ngay lập tức |
| Failure | AI sai, user recover thế nào? | Undo, sửa trực tiếp, chuyển người thật | User, ngay lập tức |
| Correction | User sửa, data đi vào đâu? | Correction log, cập nhật rule/test set | User trong tương lai — không ai thấy lợi ích ngay |

vĩnh viễn không tốt lên

"Nếu không thu signal, product AI không tốt lên."

approve rate, edit distance, 
 retry, handoff, time-to-resolution, report sai

edit distance

---

<!-- chiron-source-span: {"source_span_id":"cbde3276-8314-57aa-817b-496a56c7271e","locator":{"kind":"html_section","section_id":"c12","order":14,"heading":"12 Lab 5, deliverable & tổng kết","source_file":"slide-day05.html"},"checksum":"b981a3c4c91c628fd00e183414dc4e86dfdeaa72ff594c33e70de05254259e53"} -->

## 12 Lab 5, deliverable & tổng kết

Deck A slide 36–44 · deck C slide 36, 39. Phần này nói bạn phải nộp gì và bài học 
 nào nên mang đi.

### Deck A · slide 37–39 Cách chạy lab, PRD skeleton, và tiêu chí chấm

> Trích deck A 
>  "1. Chọn artifact chính: multi-agent system Day 04 hoặc 1 use case quen thuộc. 2. Viết 
>  Problem, Target User, Success Metrics, Architecture ở mức đủ để team hiểu scope. 
>  3. Viết ít nhất 3 user stories với acceptance criteria và edge cases. 4. Lập 
>  risk matrix cho 5 rủi ro chính: hallucination, bias, privacy, cost, adoption." 
>  "Lưu ý: Lab này không chấm 'văn hay'. Lab này chấm mức độ rõ, đo được, hành động 
>  được. " 
>  " Deliverable: PRD 3–5 trang gồm đủ 8 phần cốt lõi · Risk Matrix likelihood × 
>  impact · 3 user stories có acceptance criteria và failure handling · Decision note: đề xuất 
>  go / conditional go / no-go và lý do." 
>  " Có target user rõ chưa? Metric có đo được chưa? Non-functional có đủ chưa? Risk có owner 
>  và mitigation chưa? " 
>  PRD skeleton mẫu — Internal Policy Assistant: "Problem: HR team mất nhiều thời gian trả lời câu hỏi 
>  lặp lại về chính sách. Target User: HR staff và line managers. Success Metrics: 
>  time-to-answer giảm 50% · citation coverage > 95% · escalation rate < 15%. 
>  Risks: hallucination on policy interpretation · PII leakage in uploaded documents."

PRD skeleton mẫu ở slide 39 rất ngắn nhưng ba metric của nó được chọn khéo — chúng phủ đúng ba tầng 
 của [hierarchy slide 26](#sa25), và mỗi cái bảo vệ một thứ khác nhau:

| Metric | Tầng | Bảo vệ chống lại điều gì | Nếu chỉ có metric này thì hỏng thế nào |
| --- | --- | --- | --- |
| Time-to-answer giảm 50% | Product / Business | Chống lại case Gamma — sản phẩm dùng được nhưng không tiết kiệm thời gian thật | Đạt được bằng cách trả lời nhanh và sai |
| Citation coverage > 95% | AI | Chống lại hallucination và chống lại chiều emotional của JTBD (user vẫn phải tự tra) | Đạt được bằng cách trích một nguồn bất kỳ, kể cả nguồn không liên quan |
| Escalation rate < 15% | Product | Chống lại một hệ thống "an toàn" bằng cách đẩy hết sang người | Đạt được bằng cách không bao giờ escalate — và đó là hỏng nặng hơn |

bị chơi được

escalation rate < 15% vẫn còn thiếu một nửa

"escalation rate trong khoảng 3–15%"

mọi metric mà "càng thấp càng tốt" nghe có vẻ 
 đúng đều nên được kiểm tra xem giá trị 0 có phải là hỏng không.

"Có target user rõ chưa? Metric có đo được chưa? Non-functional có đủ chưa? Risk có owner và 
 mitigation chưa?"

chỉ vào một dòng cụ thể

### Deck C · slide 36, 39 AI Product Canvas một trang, và năm nguyên tắc

> Trích deck C 
>  " AI Product Canvas là một trang giữ product không trôi về demo. 
>  VALUE — cho ai, đau ở đâu? User cụ thể, pain cụ thể, AI giải gì mà cách hiện tại chưa giải 
>  tốt. TRUST — khi AI sai thì sao? User biết, sửa, undo, handoff và regain trust bằng cách nào. 
>  FEASIBILITY — có đáng build không? Cost/request, latency, data, risk chính và 
>  ngưỡng kill." 
>  " Learning signal: user correction đi vào đâu? Product tốt lên bằng signal nào: 
>  approve, edit, retry, handoff, report sai?" 
>  " Năm nguyên tắc: 01 AI = uncertainty — không giả định AI luôn đúng. 02 Augment ≠ 
>  kém hơn automate — nó thường là điểm bắt đầu đúng. 03 Lỗi nào đắt hơn? — quyết định UX và failure 
>  path. 04 UX là safety net — hỏi lại, sửa, undo, handoff. 05 SPEC rõ trước khi build — evidence, 
>  scope, quyết định, failure path."

Canvas ba ô của deck C là bản rút gọn tốt của cả ngày, và nó có một chi tiết mà PRD 8 phần của deck A **không có**: *ngưỡng kill*.

| Ô canvas | Câu hỏi | Ứng với phần nào của PRD deck A |
| --- | --- | --- |
| VALUE | Cho ai, đau ở đâu? | 1. Problem · 2. Target User · 3. Success Metrics |
| TRUST | Khi AI sai thì sao? | 7. Acceptance Criteria (phần failure handling) — và phần lớn chương 07 |
| FEASIBILITY | Có đáng build không? | 4. Technical Architecture · 6. Non-functional · 8. Risks — cộng ngưỡng kill |

lúc bắt đầu

lúc dừng

trước khi bắt đầu

"Nếu sau pilot 6 tuần với 30 nhân viên HR, tỉ lệ câu hỏi được 
 giải quyết không cần tra tay dưới 40%, hoặc citation coverage không đạt 90%, thì dừng và chuyển sang 
 phương án tìm kiếm truyền thống."

có mốc thời gian

có phương án thay thế

AI = uncertainty

augment thường là điểm bắt đầu đúng

lỗi nào đắt hơn

UX vẫn phải là safety net

được viết vào SPEC trước khi build

"PRD của bạn đang giúp team quyết định nhanh hơn, hay chỉ làm file dài hơn?"

---

<!-- chiron-source-span: {"source_span_id":"b73dcdb6-2bbb-57c4-a172-362a8a69c4e5","locator":{"kind":"html_section","section_id":"ladder","order":15,"heading":"▤ Luyện kỹ năng cốt lõi: biến một quan sát thành một dòng spec","source_file":"slide-day05.html"},"checksum":"62005f87c82aefec01df07d74cdd105334bac8a3208902d19faee9e5db64c0f5"} -->

## ▤ Luyện kỹ năng cốt lõi: biến một quan sát thành một dòng spec

Ba bài giảm dần giàn giáo. Kỹ năng được luyện là kỹ năng bị chấm trong Lab 5: *rõ, đo được, hành động được*.

Khi user [trigger], AI/product [failure], hậu quả là [impact], lỗi thuộc layer [taxonomy], nên 
 sửa bằng [requirement / eval / UX / data / automation], đo bằng [metric hoặc signal].

layer

nên sửa bằng

đo bằng

#### Trợ lý tra cứu chính sách nội bộ. Một nhân 
 viên HR hỏi "nghỉ phép năm chưa dùng hết thì sao?" — bot trả lời trôi chảy rằng ngày phép được 
 chuyển sang năm sau tối đa 5 ngày. Thực tế công ty không có quy định đó

Đọc cách *lập luận*, không chỉ đáp án.

1. Khoanh vùng trước: lỗi thuộc layer nào? Chạy thử: câu hỏi này 
 không có trong kho tài liệu — công ty chưa ban hành quy định về chuyển ngày phép. Vậy đây 
 không phải lỗi Intent (bot hiểu đúng câu hỏi) và không phải 
 lỗi Data/Tool theo nghĩa retrieval hỏng (retrieval chạy đúng, chỉ là không có gì để trả). 
 Đây là Promise + Safety/Behavior: bot trông như biết mọi chính sách (promise sai), 
 và khi không có nguồn thì nó bịa thay vì từ chối (behavior sai). 
 Cách nhận ra: retrieval không trả về chunk nào đạt ngưỡng, mà câu trả lời vẫn được sinh ra.
2. Định impact — và định cho đúng mức. Không phải "user khó chịu". Đây là 
 plausible-but-incorrect (deck B slide 26): nghe hợp lý, đúng giọng văn chính sách, không có 
 dấu hiệu nào để nghi ngờ. Nhân viên HR có thể trả lời lại cho đồng nghiệp, đồng nghiệp sắp xếp nghỉ 
 theo đó. Tiền lệ Air Canada cho thấy hậu quả có thể là một cam kết mà tổ chức phải thực 
 hiện.
3. Sửa ở đâu — và ở chỗ rẻ nhất trước. Ba lớp, theo thứ tự giá: 
 · Requirement (rẻ nhất): thêm một dòng vào failure modes — "khi không có 
 chunk nào vượt ngưỡng tương đồng, agent phải trả lời rằng chưa có quy định về việc này trong kho tài 
 liệu, kèm link trang chính sách và đầu mối HR — không được suy luận." 
 · UX: mọi câu trả lời đều phải có citation hiển thị; câu không có citation thì 
 hiển thị khác hẳn về mặt thị giác, để user thấy ngay. 
 · Eval: thêm một nhóm case "ngoài kho tài liệu" — 20 câu hỏi về chính 
 sách công ty không có, với tiêu chí đạt là từ chối đúng.
4. Đo bằng gì. Hai chỉ số: tỉ lệ từ chối đúng trên nhóm eval mới (quality 
 gate ≥ 95%) và citation coverage trên toàn bộ câu trả lời production (≥ 95%, đúng con số 
 trong PRD skeleton của deck A slide 39 ).

Câu chốt kiểu vấn đáp "Bot hiểu đúng câu hỏi và retrieval chạy đúng, nên lỗi không nằm ở Intent hay Data — nó nằm ở Promise 
 và Safety: giao diện hứa bot biết mọi chính sách, và khi không có nguồn thì bot bịa thay vì từ chối. 
 Em sửa bằng ba lớp: một dòng failure mode bắt buộc từ chối có kiểm soát khi không có chunk vượt 
 ngưỡng, một quy tắc UX là mọi câu trả lời phải hiện citation, và một nhóm eval 20 câu ngoài phạm vi 
 với quality gate 95% từ chối đúng. Em đo bằng tỉ lệ từ chối đúng và citation coverage."

#### Cùng sản phẩm đó. Sau sáu tuần, log cho 
 thấy 34% số câu trả lời bị user copy ra rồi sửa trước khi dùng, nhưng thumbs-down chỉ 
 2%. Viết finding này thành một product decision

Gợi ý theo thứ tự: đây là loại tín hiệu nào? · nó mâu thuẫn với tín hiệu nào? · lỗi thuộc 
 layer nào? · sửa ở lớp nào?

1. Hai tín hiệu này thuộc loại nào theo phân loại ba tín hiệu của 
 deck A slide 19, và cái nào đáng tin hơn — vì sao?
2. Vì sao chúng mâu thuẫn? Nếu một phần ba câu trả lời phải sửa, vì 
 sao gần như không ai bấm thumbs-down? (Gợi ý: nghĩ về chi phí của mỗi hành động đối với 
 user.)
3. Layer nào? Đây có phải lỗi chất lượng model không, hay là một thứ 
 khác? Xét cả năm layer của deck C slide 29 trước khi chọn.
4. Sửa bằng gì và đo bằng gì? Viết đủ sáu ô của công thức debrief.

#### Xem lời giải

**① Loại tín hiệu.** Thumbs-down là *explicit feedback*; "copy ra rồi sửa" là *behavioral signal* — cụ thể là **edit distance**, đúng chỉ số mà deck C slide 38 
 liệt kê. Behavioral đáng tin hơn nhiều: nó phủ 100% user và không phụ thuộc việc ai đó chịu khó bấm 
 nút.

**② Vì sao mâu thuẫn.** Vì hai hành động có chi phí rất khác nhau đối với user. Sửa 
 một câu trả lời là việc họ *phải* làm để hoàn thành công việc. Bấm thumbs-down là việc thêm, 
 không mang lại lợi ích gì ngay cho họ. Nên tỉ lệ thumbs-down thấp **không phải bằng chứng của 
 chất lượng** — nó là bằng chứng của việc bấm nút tốn công.

**③ Layer.** Chưa đủ dữ liệu để kết luận, và *đó chính là phát hiện*. 34% có 
 thể là *Intent* (hiểu sai ý), *Data/Tool* (nguồn cũ), hoặc thậm chí không phải lỗi gì cả 
 — có thể user chỉ đang đổi giọng văn cho hợp ngữ cảnh. Ba nguyên nhân, ba cách sửa khác nhau. 
 Nhưng có **một** layer chắc chắn có lỗi: **UX Recovery**. Việc user phải *copy ra ngoài* để sửa nghĩa là sản phẩm không có chỗ sửa tại chỗ — đúng điều deck B slide 52 
 cảnh báo: "nếu AI không hoàn hảo, đừng bắt user làm lại từ đầu".

**④ Sáu ô.** *"Khi user nhận được câu trả lời (trigger), 34% trường hợp họ phải 
 copy ra ngoài và chỉnh sửa trước khi dùng (failure); hậu quả là giá trị tiết kiệm thời gian thấp hơn 
 nhiều so với báo cáo, và ta không biết vì sao (impact); lỗi thuộc layer UX Recovery — và có thể cả 
 Intent hoặc Data, chưa xác định được (taxonomy); sửa bằng ① cho phép sửa trực tiếp trong sản phẩm và 
 lưu bản gốc lẫn bản sửa, ② phân loại 50 cặp gốc/sửa gần nhất để xác định nguyên nhân thật (UX + 
 eval); đo bằng edit distance trung bình và tỉ lệ câu trả lời dùng được không cần sửa."*

*Điểm mấu chốt:* việc sửa đầu tiên không phải cải thiện model — mà là **làm cho việc 
 sửa xảy ra bên trong sản phẩm**. Chỉ khi đó bạn mới có dữ liệu để biết cần sửa cái gì. Đây đúng 
 là bước LEARN trong [Hình 1](#f1), và là path thứ tư ( *correction* ) mà deck C nói 
 hay bị cắt nhất.

#### Bạn được đề nghị: "Bật chế độ để bot tự 
 động trả lời trực tiếp cho nhân viên qua chat, không cần HR duyệt nữa. Eval set 200 case đang đạt 
 91%." Viết decision note: go / conditional go / no-go, kèm lý do

Không có gợi ý. Dùng: công thức act/ask, ba mức go/no-go, ma trận risk, và mô-đun eval.

#### Xem một lời giải tham khảo

**Kết luận: conditional go** — và lý do nên viết theo bốn bước.

**① 91% trên 200 case nghĩa là gì.** Khoảng tin cậy 95% là khoảng **86–94%**. Đủ hẹp để nói "trên 85%", không đủ hẹp để nói "trên 90%". Nếu quality gate 
 đặt ở 90% thì kết quả này *chưa đạt một cách chắc chắn* — nó chỉ vượt ở giá trị điểm.

**② Sai thì mất gì.** Câu trả lời sai đi thẳng tới nhân viên, không ai chặn, và *không ai biết là nó sai* — đây là ô nguy hiểm nhất trong ma trận [deck B slide 57](#sb56): user thấy câu trả lời nhưng không kiểm chứng được. Với chính 
 sách nhân sự, một câu sai có thể thành cam kết (tiền lệ Air Canada). Vậy **C cao**, mà `p* = 1 − I/(V+C)` thì C cao đẩy ngưỡng lên rất gần 100% — cao hơn 91% rất nhiều.

**③ Nhưng no-go cũng sai.** Bắt HR duyệt mọi câu là mô hình REVIEWER — tốn nhân lực 
 tuyến tính theo volume, và chính nó là vấn đề ban đầu. Điều kiện no-go của deck A không thoả: có 
 fallback, có user value đã chứng minh, chưa có vi phạm privacy lớn.

**④ Conditional go — bốn điều kiện, đúng bốn cách hạ C:** 
 · *Scope hẹp:* chỉ tự động trả lời nhóm câu hỏi đã có nguồn rõ và đã đạt ≥ 97% trên eval 
 tách riêng (ví dụ: giờ làm việc, số ngày phép tiêu chuẩn). Câu về diễn giải chính sách vẫn qua người. 
 · *Guardrails chặt:* không có citation thì không được trả lời tự động — chuyển sang HR. 
 · *Human-in-the-loop dạng RESCUER thay vì REVIEWER:* người chỉ xử lý case dưới ngưỡng, chứ 
 không duyệt mọi case. Đây là thay đổi giúp mô hình scale được. 
 · *Pilot giới hạn:* 4 tuần, một phòng ban, kèm **ngưỡng kill** — nếu tỉ lệ 
 khiếu nại về thông tin sai vượt 1% hoặc citation coverage tụt dưới 95% thì tắt tự động, quay lại chế 
 độ duyệt.

**Và một dòng cuối phải có:** owner của quyết định này là ai, và ngày nào review lại. 
 Không có hai thứ đó thì "conditional go" sẽ lặng lẽ biến thành "go" sau vài tuần không ai để ý.

---

<!-- chiron-source-span: {"source_span_id":"b7075075-feb7-57b7-bcc9-08c5fae40c6d","locator":{"kind":"html_section","section_id":"misc","order":16,"heading":"✕ 6 hiểu lầm phổ biến","source_file":"slide-day05.html"},"checksum":"00c7e373bbbd69ab9144046a2e799fed8b1a44839dff15b38e6a34f7f813690c"} -->

## ✕ 6 hiểu lầm phổ biến

Mỗi ô: điều nhiều người tin → điều slide thật sự nói → vì sao khác biệt quan trọng.

"AI product khác software product ở chỗ output không đoán trước được — nên phải test kỹ hơn."

ba lớp

"test kỹ hơn"

không phải bug để sửa mà là constraint để thiết kế 
 vòng tránh

chương 01

"Augmentation là bước đệm vì AI chưa đủ giỏi. Khi accuracy đủ cao thì chuyển sang automation."

"augmentation không phải bản kém của automation"

chi phí khi sai

"60% có thể vẫn hữu 
 dụng nếu user chỉ cần duyệt; 99,5% vẫn nguy hiểm nếu AI tự động hành động sai."

p* = 1 − I/(V+C)

hai trong ba biến là do bạn thiết kế

"Có eval set 20 case rồi, đủ để đặt quality gate."

tìm ra

chặn

70–97%

150 case

cảm giác

mô-đun demo vs phân bố

"Nên đặt ngưỡng báo động ở mức 'chắc hơn 50%' — dưới đó thì báo động không đáng tin."

FP

FP

FN

4,76%

đó là kết quả đúng, không phải hệ thống hỏng

mô-đun chi phí lỗi

2,3 lần

"PRD có mục 'human review' là đã xử lý xong phần rủi ro con người."

"nếu viết 'human review' mà không nói human làm vai trò nào và output review 
 đi đâu, thì chưa đủ."

chỉ RESCUER là mô hình scale được

bay hơi

"Mục tiêu thiết kế là làm user tin tưởng AI."

hiệu chỉnh

khó phát hiện

trông đáng tin hơn

Hình 2

chương 07

---

<!-- chiron-source-span: {"source_span_id":"f1c3aff0-cb0a-52e5-acff-5f6ff16851a9","locator":{"kind":"html_section","section_id":"apply","order":17,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-day05.html"},"checksum":"c47ea551b74190f6281a54b29336d7dd9bcff51f0c9a101cfe66c554fed27c6c"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI là agent check-in kiosk chạy trên LangGraph — có tool tra cứu booking, 
 có node approval, có scenario test. Ngày 5 là ngày đầu tiên bắt nó trả lời câu hỏi *sản phẩm*, chứ 
 không phải câu hỏi kỹ thuật.

cho ai, giá trị gì, đo bằng gì, rủi ro nào, khi nào 
 go/no-go

| Câu hỏi | Hiện trạng SmartCheck AI | Thiếu gì |
| --- | --- | --- |
| Cho ai? | "Khách check-in tại kiosk" — có persona ngầm, chưa viết ra | Chưa có ngưỡng chấp nhận sai và AI literacy — hai chiều persona riêng của AI |
| Giá trị gì? | Giảm thời gian check-in, giảm tải quầy lễ tân | Chưa có baseline: hiện check-in tay mất bao lâu? |
| Đo bằng gì? | Có metrics.py và scenario test | Đo kỹ thuật, chưa đo product metric hay business KPI — 
 đúng chứng "AI metric mồ côi" |
| Rủi ro nào? | Có approval node cho một số ca | Chưa có risk register. Chưa ai viết ra năm nhóm risk và ai sở hữu chúng |
| Khi nào go/no-go? | — | Chưa có ngưỡng kill, chưa có decision note |

trụ thứ nhất

một phần trụ thứ ba

### ① Problem statement — viết lại theo phép thử của deck B

Phép thử: *xoá mọi từ liên quan tới AI; nếu câu còn lại vô nghĩa thì đó là solution statement*.

| Mức | Câu | Nhận xét |
| --- | --- | --- |
| ✕ Bad | "Khách sạn chưa có AI agent tự động hoá quy trình check-in tại kiosk." | Xoá "AI agent" thì còn "chưa có tự động hoá" — vẫn là mô tả thứ đang thiếu, không phải 
 việc đang tốn kém |
| ◐ Good | "Khách đến nhận phòng vào giờ cao điểm phải xếp hàng chờ lễ tân, trong khi phần lớn thao tác 
 check-in chỉ là xác nhận thông tin đã có sẵn trong hệ thống." | Đứng vững không cần AI. Gợi ra nhiều phương án: thêm quầy, app tự check-in, kiosk không AI, AI |
| ✓ Even better | "…Ngoài ra, khách đặt qua nhiều kênh khác nhau nên thông tin không đồng nhất, và khách không nói 
 tiếng địa phương thường mất thêm thời gian ở bước xác minh giấy tờ." | Chỉ ra đâu là phần khó thật — và đó chính là chỗ AI có lợi thế so với một kiosk quy tắc 
 cứng |

không cần AI

không dùng AI

thông tin không đồng nhất giữa 
 các kênh

rào cản ngôn ngữ

chương 02

problem 
 statement viết tốt là thứ chứng minh AI là lựa chọn đúng, thay vì giả định điều đó.

### ② Bốn paths cho tính năng tra cứu booking

Hiện tại `lookup_booking` đã có schema và error mode (từ [Ngày 
 4](slide-day-4.html) ). Nhưng đó là spec *kỹ thuật*. Bốn paths của deck C là spec *sản phẩm* cho cùng tính 
 năng đó:

| Path | Điều kiện | Hệ thống làm gì | Khách thấy gì trên màn hình kiosk |
| --- | --- | --- | --- |
| Happy | Tìm được đúng một booking khớp | Hiện thông tin, xin xác nhận | Tên, ngày, loại phòng + nút "Đúng rồi" / "Không phải tôi" |
| Low-confidence | Tìm được nhiều booking khớp, hoặc khớp một phần (tên gần giống) | Hỏi lại một câu duy nhất — không đoán | "Bạn cho mình xin 4 số cuối điện thoại" — không hiện danh sách khách khác 
 (lộ thông tin người khác) |
| Failure | Không tìm thấy, hoặc tool timeout, hoặc dữ liệu mâu thuẫn | Chuyển người thật, mang theo ngữ cảnh đã thu | "Mình chuyển bạn sang quầy lễ tân, thông tin bạn vừa nhập đã được gửi sang" + số thứ tự |
| Correction | Khách bấm "Không phải tôi", hoặc nhân viên sửa sau đó | Ghi lại cặp (câu hỏi, kết quả sai, kết quả đúng) vào correction log | Không thấy gì — nhưng đây là path duy nhất làm sản phẩm tốt lên |

hiện danh sách cho user chọn

tên của những khách khác

một

data minimization

trụ privacy của deck A slide 14

quyết định này được đưa ra lúc 
 thiết kế low-confidence path, không phải lúc audit.

### ③ Risk register — năm rủi ro theo chuẩn Lab 5

| Rủi ro | Nhóm | L × I | Vùng | Mitigation kiểm chứng được |
| --- | --- | --- | --- | --- |
| Xác nhận nhầm booking cho sai người | Technical + Ethical | Thấp × Rất cao | Escalate | Bắt buộc bước xác minh thứ hai trước khi cấp thẻ phòng; eval riêng 20 case tên gần giống, gate 100% 
 không tự quyết |
| Bịa chính sách khách sạn (giờ trả phòng, phí huỷ) | Technical | Cao × Cao | Reduce | Chỉ trả lời khi có citation từ kho tài liệu; không có nguồn thì chuyển lễ tân; eval 20 case ngoài 
 phạm vi |
| Rò rỉ thông tin khách khác qua màn hình kiosk | Data | Trung bình × Rất cao | Escalate | Không bao giờ hiện danh sách nhiều khách; log kiểm tra định kỳ; xoá màn hình sau 30 giây không thao tác |
| Chi phí token vượt ngân sách giờ cao điểm | Business | Trung bình × Trung bình | Mitigate | Cảnh báo ngân sách theo ngày; cache câu hỏi lặp 
 ( Ngày 25 Track 3 ); rate limit |
| Khách không dùng kiosk, vẫn xếp hàng ở quầy | Business | Cao × Trung bình | Mitigate | Pilot một sảnh trong 4 tuần; đo tỉ lệ khách chọn kiosk; ngưỡng kill dưới 25% thì dừng |

không phải việc của team

agent không được phép là 
 khâu cuối cùng trước khi cấp thẻ phòng

công thức p*

approval_node

đúng

### ④ Việc rẻ nhất nên làm ngay

deck C slide 20

Vì sao đây là việc đáng làm trước mọi việc khác:

đầu vào

khi agent không chắc, nó làm gì?

chạy vibe check 30 case

bẩn

vibe check trước khi viết PRD

---

<!-- chiron-source-span: {"source_span_id":"257ae4e0-4a3b-5aae-a339-48e0f2d1f245","locator":{"kind":"html_section","section_id":"numbers","order":18,"heading":"# Con số cần kiểm chứng","source_file":"slide-day05.html"},"checksum":"f44c177ecca819af1e4e5b2647b58a9b55c44f382cfae72c5c40804622033fb9"} -->

## # Con số cần kiểm chứng

Phân biệt rõ: cái gì có trên slide, cái gì tôi tính ra, và cái gì là giả định minh 
 hoạ của tài liệu này.

| Con số | Nguồn | Trạng thái |
| --- | --- | --- |
| Precision 8/13 ≈ 62%, recall 8/10 = 80% (lọc video trẻ em) | Deck B slide 56 | Đã kiểm. 8/13 = 61,54% — slide làm tròn lên 62%. 8/10 = 80% chính xác |
| Precision 30/40 = 75%, recall 30/50 = 60% (quét giao dịch) | Deck C slide 23 | Đã kiểm, khớp hoàn toàn |
| Copilot: 30% acceptance rate, 4,7 triệu paid users (1/2026) | Deck B slide 39 | Của slide, dẫn nguồn GitHub · Microsoft earnings. Chưa kiểm độc lập — nếu dùng 
 trong bài nộp thì phải tự tra lại |
| Fireflies: 100+ cuộc họp làm tay, $100/tháng, seed $5M 10/2019, kỳ lân $1 tỷ 6/2025 | Deck B slide 15 | Của slide, dẫn TechStartups 12/11/2025 + Fireflies Blog. Chưa kiểm độc lập |
| DoorDash: đơn đầu tiên sau 45 phút, $6/đơn, 8 quán | Deck B slide 14 | Của slide, dẫn Founders Podcast. Chưa kiểm độc lập |
| PRD skeleton: time-to-answer giảm 50%, citation coverage > 95%, escalation rate < 15% | Deck A slide 39 | Của slide, là ví dụ minh hoạ chứ không phải benchmark ngành. Đừng chép vào PRD thật mà 
 chưa có baseline của chính bạn |
| BatchBuddy: deadline "2000 22/06", bot trả "1800 22/06" | Deck B slide 26 | Bản trích từ PDF mất dấu hai chấm; tôi đọc là 20:00 và 18:00. 
 Nếu cần trích chính xác, xem lại slide gốc |
| 0,8³ = 51,2% · 0,8²⁰ = 1,2% · cần 14 case ở p = 80%, 59 case ở p = 95% | Tính trong tài liệu này | Đã kiểm bằng máy. ln(0,05)/ln(0,8) = 13,43 → 14; 
 ln(0,05)/ln(0,95) = 58,40 → 59 |
| Khoảng tin cậy: 18/20 → 70–97% · 16/20 → 58–92% · 182/200 → 86–94% · 150 case cho ±5 điểm · 
 870 case cho ±2 điểm | Tính trong tài liệu này | Đã kiểm bằng máy, dùng công thức Wilson, z = 1,96 |
| Ngưỡng tối ưu τ* = 4,76% · precision 30,2% · recall 89,8% · 103,0 triệu đ vs 239,2 triệu đ · 
 đắt gấp 2,3 lần | Tính trong tài liệu này từ giả định minh hoạ | Công thức τ* = c FP /(c FP +c FN ) là kết quả chuẩn của lý 
 thuyết quyết định Bayes. Nhưng bối cảnh (10.000 ca/tháng, tỉ lệ nền 5%, 50 nghìn đ, 
 1 triệu đ, d′ = 2,5) là giả định của tài liệu này, không có trên slide |
| p* = 1 − I/(V+C) · 95% ở C = 100 · 99,1% ở C = 1.000 · 70% ở I = 60 | Tính trong tài liệu này | Slide 40 của deck B chỉ phát biểu rằng đây là bài toán expected value (dẫn Horvitz, 
 CHI 1999). Công thức và mọi con số là diễn giải của tài liệu này; slide không đưa 
 công thức nào |
| Ngưỡng vùng của risk matrix (Monitor / Mitigate / Reduce / Escalate) | Deck A slide 34 | Slide có bốn tên vùng và vị trí năm rủi ro, nhưng 
 không có ngưỡng số. Việc gán mức likelihood/impact cho từng rủi ro trong bảng ở 
 chương 10 là đọc từ vị trí trên hình, không phải số của slide |
| Bảng năm mức tự chủ trong mô-đun act/ask (C = 0,1V đến 50V) | Giả định minh hoạ | Các mức chi phí là ước lượng tương đối để minh hoạ hình dạng của ngưỡng, không phải số liệu ngành |
| Toàn bộ phần SmartCheck AI: 30 giây xoá màn hình, 4 tuần pilot, ngưỡng kill 25%, 2–3 giờ viết 
 failure mode library | Đề xuất của tài liệu này | Không có số nào lấy từ slide hay từ đo đạc thật. Phải thay bằng số của dự án trước khi dùng |

không có mô-đun nào tái hiện một con số của slide

lấy một khẳng định 
 định tính của slide và tính xem nó có nghĩa gì bằng số

kết luận định tính đến từ slide, mọi con số đến từ tài liệu này.

---

<!-- chiron-source-span: {"source_span_id":"0189c4e4-c884-513d-8445-88910e66bc6f","locator":{"kind":"html_section","section_id":"cheat","order":19,"heading":"▣ Cheat sheet ôn thi","source_file":"slide-day05.html"},"checksum":"c4d55c1df7637e35fc0d603e7156924bfbc67700ffd095b6b3e0c36caa5a8d9d"} -->

## ▣ Cheat sheet ôn thi

Bảy danh sách và một công thức. Nếu chỉ có 10 phút trước quiz, đọc mục này.

| Khung | Nội dung | Nguồn |
| --- | --- | --- |
| 5 câu hỏi của ngày | Cho ai · giá trị gì · đo bằng gì · rủi ro nào · khi nào go/no-go | Deck A slide 4 |
| 3 lớp bất định | Input (hỏi bẩn) · Process (không thấy vì sao) · Output (mỗi lần một khác) | Deck C slide 8 |
| 4 bước đường đi của lỗi | DETECT → ROUTE → RECOVER → LEARN | Deck C slide 11 |
| 8 phần PRD | Problem · Target User · Success Metrics · Technical Architecture · Feature Requirements · 
 Non-functional · Acceptance Criteria · Risks | Deck A slide 25 |
| 6 bước viết PRD cho AI feature | ① Identify use case · ② Articulate problem (không nhắc AI) · ③ Goals/non-goals/metrics · 
 ④ Scope (a: user flow · b: AI-specific · c: privacy) · ⑤ Align engineering · ⑥ GTM | Deck B slide 17–27 (Ailian Gan) |
| 3 tầng success metric | Business KPI → Product metric → AI metric. Đo từ dưới lên, chứng minh từ trên xuống | Deck A slide 26 |
| 3 nhóm requirement | Functional · Non-functional · AI-specific (hallucination threshold, 
 explainability, fallback) | Deck A slide 22 |
| 4 thành phần acceptance criteria | Trigger rõ · hành vi mong đợi · ngưỡng đo được · failure handling | Deck A slide 23 |
| 3 ca chuyển đổi của spec | ① expected output → tỉ lệ · ② test cases → test distributions · ③ "works" → "fails by design" | Deck B slide 24 |
| 3 tầng fallback | Soft fallback · Human handoff · Silent skip | Deck B slide 24 |
| 3 lựa chọn tự chủ | Inaction · Ask · Act. "Ask thường là trạng thái thông minh nhất nhưng hay bị 
 bỏ quên nhất" | Deck B slide 40 (Horvitz) |
| 4 vai của con người | REVIEWER · DECIDER · TRAINER · RESCUER (vai duy nhất scale được) | Deck C slide 16 |
| 3 trụ trust calibration | Expectation · Explainability · Control | Deck B slide 38 |
| 4 paths của user story AI | Happy · Low-confidence · Failure · Correction | Deck C slide 37 |
| 3 giai đoạn eval | Vibe Check (trước PRD) · Offline Eval (quality gate) · Online Monitoring 
 ( case chảy ngược về offline ) | Deck B slide 61–62 |
| 5 nhóm risk | Technical · Data · Business · Ethical · Regulatory | Deck A slide 33 |
| 3 mức go/no-go | Go · Conditional go (pilot hẹp, HITL, guardrail chặt, scope hẹp) · No-go | Deck A slide 35 |
| 5 layer failure taxonomy | Promise · Intent · Data/Tool · Safety/Behavior · UX Recovery | Deck C slide 29 |
| 3 loại tín hiệu feedback | Explicit (thumbs) · Behavioral (copy, rephrase, override, abandon) · Outcome | Deck A slide 19 |

```text
CÔNG THỨC DUY NHẤT CẦN NHỚ

  p* = 1 − I / (V + C)      ngưỡng độ chắc tối thiểu để được TỰ ĐỘNG làm
                            V = giá trị khi đúng · C = chi phí khi sai · I = chi phí hỏi lại

  C tăng  →  p* tăng        sai càng đắt, càng phải chắc mới được tự động
  I giảm  →  p* tăng        hỏi càng rẻ, càng nên hỏi thay vì đoán

VÀ MỘT CÔNG THỨC PHỤ (chương 08)

  τ* = c_FP / (c_FP + c_FN)   ngưỡng báo động tối ưu
                              bỏ sót đắt gấp 20 lần báo nhầm  →  τ* = 1/21 ≈ 4,8%

BA CÂU HỎI THAY THẾ CHO "ACCURACY BAO NHIÊU LÀ ĐỦ"

  1. Sai kiểu nào tệ hơn — báo nhầm hay bỏ sót?
  2. Ai phát hiện ra lỗi đó — user, hay không ai cả?
  3. Sai rồi thì hồi phục được không?
```

"Nondeterminism không phải bug để sửa — là constraint để thiết kế vòng tránh, như latency hay 
 kích thước màn hình."

"AI product không cố hứa 'không bao giờ sai'; nó hứa 'khi không chắc hoặc sai, hệ thống vẫn 
 dẫn user đi đúng hướng'."

"Cấu hình quyết định bề mặt rủi ro."

---

<!-- chiron-source-span: {"source_span_id":"460574ee-e0ab-5ec1-ac12-5dce7ac2aa1d","locator":{"kind":"html_section","section_id":"gloss","order":20,"heading":"≡ Từ điển thuật ngữ","source_file":"slide-day05.html"},"checksum":"42dba97b6c44d8b3340347c99f0396dfe7277277502aa51fa7699d67d2af6123"} -->

## ≡ Từ điển thuật ngữ

**Jobs-to-be-Done (JTBD)**

: Khung mô tả việc user đang cố hoàn thành, gồm ba chiều: functional (làm được việc gì), 
 emotional (muốn cảm thấy thế nào), social (muốn được nhìn nhận ra sao). Bỏ hai chiều 
 sau là lý do một agent "đúng chức năng" vẫn không được dùng lại.

**North star metric**

: Một chỉ số duy nhất đại diện cho giá trị cốt lõi của sản phẩm. Dấu hiệu nhận ra north star 
 tồi: AI có thể làm nó tăng mà không cần đúng.

**Leap of faith assumption**

: Giả định mà cả sản phẩm phụ thuộc vào nhưng chưa có bằng chứng. Bốn loại: value risk, usability 
 risk, feasibility risk, business viability risk — mỗi loại cần một kiểu prototype khác nhau.

**Wizard of Oz MVP**

: Cho con người làm thay phần việc mà máy sẽ làm, trong khi user tưởng đang dùng hệ thống tự động — 
 để test value risk trước khi build. Hợp lệ khi user vẫn nhận đúng thứ họ trả tiền; không hợp lệ 
 khi họ chịu rủi ro dựa trên một tuyên bố sai về hệ thống.

**Behavioral drift**

: Hệ thống đổi hành vi mà không ai đổi code — do model update, dữ liệu nguồn thay đổi, cách user hỏi 
 thay đổi, hoặc prompt drift (team thêm rule vặt tới lúc không ai dám xoá dòng nào).

**Trust calibration**

: Đưa mức tin tưởng của user về đúng năng lực thật của hệ thống. Hai kiểu lệch: overtrust 
 (giao việc quá mức) và distrust (không dùng dù có giá trị). Ba công cụ: expectation, 
 explainability, control.

**Precision giả (false precision)**

: Hiển thị nhiều chữ số hơn độ chính xác thật của hệ thống — "387 kcal" thay vì "350–430 kcal". 
 Số chữ số bạn hiện là một lời hứa; hứa quá là một lỗi thiết kế, không phải một chi tiết thẩm mỹ.

**Graceful failure**

: Không phải câu "AI có thể sai" trong điều khoản, mà là cơ chế cụ thể để user thấy sai, 
 sửa được, và quay lại tin sản phẩm: nhiều lựa chọn, sửa trực tiếp, fallback sang người, và ghi 
 correction.

**Mixed-initiative**

: Khung của Horvitz (CHI 1999): hệ thống chọn giữa act, ask và không làm gì 
 dựa trên expected value, thay vì cố định một mức tự chủ. Trạng thái ask hay bị bỏ quên nhất.

**Quality gate**

: Ngưỡng tỉ lệ đạt trên eval set mà một bản build phải vượt qua mới được release. Khác hẳn 
 confidence threshold — ngưỡng runtime áp cho từng request một.

**Regression (trong eval)**

: Cái từng chạy tốt nay tệ đi. Chỉ phát hiện được nếu có reference dataset đủ lớn và chạy lại toàn bộ 
 sau mỗi thay đổi prompt hoặc model.

**Plausible-but-incorrect**

: Câu trả lời nghe hợp lý, đúng định dạng, đúng giọng — nhưng sai. Loại lỗi nguy hiểm nhất vì nó vượt 
 qua mọi kiểm tra bằng cảm giác; chỉ citation hoặc đối chiếu nguồn mới bắt được.

**Silent skip**

: Tầng fallback thứ ba: không làm gì, nhưng cũng không làm sai. Cách xử lý đúng cho lỗi 
 spurious trigger — hệ thống nói khi không ai hỏi.

**Edit distance (như learning signal)**

: Đo mức độ user sửa output trước khi dùng. Tín hiệu tinh tế hơn approve/reject: một draft bị sửa 80% 
 vẫn tính là "được chấp nhận" trong khi thực tế nó không giúp gì.

**Ngưỡng kill**

: Điều kiện định trước để dừng một dự án, viết ra trước khi bắt đầu. Dùng được thì phải có 
 mốc thời gian và một phương án thay thế — thiếu phương án thay thế thì không ai dám bấm nút dừng.

**Conditional go**

: Mức giữa của quyết định triển khai: pilot giới hạn, human-in-the-loop, guardrail chặt, scope hẹp. 
 Chính là bốn cách hạ C trong công thức p* = 1 − I/(V+C).

---

<!-- chiron-source-span: {"source_span_id":"4d15fd6a-5f6b-5b60-a9e2-87612f237f80","locator":{"kind":"html_section","section_id":"bloom","order":21,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-day05.html"},"checksum":"1f6ffeb743aead38c3f4717d754eebf6092893337f6160f4c031b526e33ba0b9"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab 5 kiểm tra mức 3–4; câu hỏi cuối deck A 
 kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 8 phần PRD, 3 lớp bất định, 4 bước đường đi của lỗi, 5 nhóm risk, 3 giai đoạn eval, 
 4 paths. | Cheat sheet · Hình 1 · Hình 3 |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao "AI trả lời đúng" không phải một acceptance criterion, 
 và vì sao augmentation không phải bản kém của automation. | Deck B slide 24 · chương 04 · hiểu lầm 2 |
| 3 · Áp dụng | Viết được một problem statement không nhắc chữ AI, ba user story với đủ bốn paths, và một risk 
 register năm dòng có owner và mitigation kiểm chứng được. | Mục áp dụng · Bài 1 · deck A slide 29–31 |
| 4 · Phân tích | Cho một quan sát "bot lỗi", khoanh được nó vào một trong năm layer, và nói được ai phải sửa cùng 
 cách đo đã sửa xong. | Deck C slide 29–31 · Bài 2 |
| 5 · Đánh giá | Nhìn một PRD hoặc một đề xuất triển khai của người khác và chỉ ra chỗ sẽ hỏng — bao gồm 
 cả những chỗ con số nghe có vẻ thuyết phục nhưng không chịu nổi một khoảng tin cậy. | Năm anti-pattern · mô-đun eval · 
 Bài 3 |

"model đạt 94% rồi, bật tự động thôi"

không phải

"Sai thì mất gì, và hồi phục được không?"

"Ai phát hiện ra khi nó sai?"

"94% trên bao nhiêu case?"
