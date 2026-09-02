---
schema_version: 1
course_id: rag-intensive
document_id: "09a9cec9-2225-5427-b062-faac6e2e9273"
document_version_id: "2ed91ebb-a6b8-58b7-8a1d-bc5850a378ef"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "AI Product & Project Management — phân tích & breakdown từng slide"
source_file: "day-06.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\day-06.html"
source_sha256: "dc51194b05cd74d9219faa1aea50d27e8b48e2575eb223d2e5fb583c40ba8ef8"
parser_version: chiron-structured-markdown-v1
html_section_count: 18
interactive_module_count: 3
interactive_control_count: 16
language: vi
---

# AI Product & Project Management — phân tích & breakdown từng slide

> Ngày 5 hỏi xây cái gì. Ngày 6 hỏi một câu khó hơn nhiều: 
 lấy tiền và thời gian ở đâu để xây, và làm sao biết lúc nào nên dừng. Deck Ngày 6 nói thẳng 
 ở slide 21 rằng "ROI cho AI phải có số cụ thể, giả định rõ, và timeline rõ" — rồi 
 không đưa một con số nào. Tài liệu này đưa số đó vào, bằng công thức, và ghi rõ số nào là giả định của 
 ai.

<!-- chiron-source-span: {"source_span_id":"dba21170-6f4f-5e43-80d6-3ca55e699641","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"day-06.html"},"checksum":"38f09a833fb4ae58df6b49dc7f152768423471c604cc67b26b9dca55d75d6a86"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Ngày 6 là bài **mỏng nhất** trong 15 ngày Foundation: 37 slide, một deck duy nhất, và 
 gần như không có một con số nào. Điều đó dễ khiến người học lướt qua. Nhưng nó lại là bài duy nhất dạy 
 thứ quyết định dự án AI sống hay chết trong tổ chức thật — *ai trả tiền, trả bao nhiêu, và dựa vào 
 đâu mà quyết*.

"ROI cho AI phải có số cụ thể, giả định rõ, và timeline rõ."

tên hạng mục

không có trục số

hình dạng

cách tính

Tài liệu này lấp khoảng trống đó bằng ba mô-đun tính toán được

giả định của tài liệu này, không phải của slide

Con số cần kiểm chứng

| Bạn có gì sau Ngày 5 | Ngày 6 biến nó thành gì |
| --- | --- |
| Problem statement, JTBD, north star metric | Slide 1 của pitch deck: vấn đề & pain point |
| PRD 8 phần, user story, 4 paths | PRD final + Definition of Done cho từng AI feature |
| Risk register 5 nhóm, ma trận likelihood × impact | Slide 6 của pitch deck: risks + mitigation |
| Ngưỡng chất lượng, eval flow ba giai đoạn | Đầu vào của cột chi phí Operate trong mô hình ROI |
| Go / conditional-go / no-go | Slide 7 của pitch deck: decision ask |

Ngày 5

bắt đầu bằng cách 
 mở lại PRD của Lab 5

Lượt 1 · ~12 phút

Nắm luận điểm trung tâm

- Đọc slide 36 — "bạn đang quản lý một AI project, hay đang quản lý một 
 tập giả định chưa được kiểm chứng?" Cả bài là câu trả lời cho câu này
- Nhìn Hình 1 — vòng sprint AI và ba lối ra mà slide 8 vẽ thiếu một
- Đọc slide 12 — bảng phân biệt MVE / MVP / PoC theo mục tiêu, 
 không theo quy mô
- Mục tiêu: nói được vì sao "chúng ta làm PoC" là một câu chưa đủ nghĩa

Lượt 2 · ~55 phút

Chương 3, 6, 7 — phần bạn phải viết ra được

- Chạy mô-đun ROI trước, rồi mô-đun độ nhạy — cái 
 thứ hai đọc thẳng tham số bạn vừa đặt ở cái thứ nhất
- Chạy mô-đun PoC và tìm cho ra vùng p mà PoC vô giá trị — có hai 
 vùng như thế, ở hai đầu, và lý do khác nhau
- Viết thử ROI model cho chính sản phẩm của bạn ở Lab 5

Lượt 3 · ~25 phút

Ôn thi

- 6 hiểu lầm — bốn trong sáu cái là hiểu lầm về tiền, và đó là 
 vùng người học AI hay yếu nhất
- 3 bài bậc thang — kỹ năng được luyện: biến một câu định tính thành một 
 dòng có số
- Cheat sheet + từ điển

rõ

mỗi lần gặp chữ "rõ", tự viết ra con số hoặc câu điều kiện nào sẽ làm nó rõ.

"timebox rõ"

rõ

05

---

<!-- chiron-source-span: {"source_span_id":"5e95a301-1768-5a6e-b0d4-0f9ad36a3467","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu — bạn đang quản lý cái gì?","source_file":"day-06.html"},"checksum":"75e7f28e154bda053e4e86b2044b4eb6b681702d93e58af9a3a8694f7524de3a"} -->

## 00 Mở đầu — bạn đang quản lý cái gì?

Deck mở bằng một tình huống và đóng bằng một câu hỏi. Hai slide đó cách nhau 34 slide 
 nhưng nói cùng một điều, và nếu chỉ nhớ được hai slide của Ngày 6 thì nên nhớ hai slide này.

### Slide 2 Tình huống mở đầu: đã build 3 tuần thì stakeholder đổi requirement

> Trích slide 
>  "HÃY SUY NGHĨ… 'Team đã build 3 tuần. Nhưng stakeholder muốn đổi requirements. Làm sao xử 
>  lý?' Giữ câu hỏi này trong đầu khi học bài hôm nay."

Phản xạ đầu tiên của hầu hết người học là tìm cách *chặn* việc đổi: khoá scope, ký PRD, bắt 
 stakeholder cam kết. Cả bài Ngày 6 nói ngược lại. Nếu requirement đổi sau 3 tuần, có ba khả năng, và 
 chỉ một trong ba là lỗi của stakeholder:

| Nguyên nhân | Dấu hiệu nhận ra | Bài này chữa bằng gì |
| --- | --- | --- |
| Team đã học được điều gì đó trong 3 tuần và bản thân họ cũng nên đổi | Prototype cho thấy chất lượng thực tế khác xa giả định ban đầu | AI Sprint Model — đổi sau khi học là kết quả mong đợi, không phải 
 sự cố |
| Giả định ban đầu chưa bao giờ được kiểm chứng, chỉ được viết ra | Không ai nhớ nổi bằng chứng nào dẫn tới requirement cũ | MVE / PoC — kiểm chứng trước khi build 3 tuần |
| Stakeholder hiểu sai AI làm được gì ngay từ đầu | Yêu cầu mới dạng "cho nó tự xử lý luôn" hoặc "sao nó không chính xác 100%" | Expectation setting — và đây là cái đáng trách, nhưng trách team chứ không 
 trách stakeholder |

Đừng chống việc đổi requirement — hãy làm cho việc đổi rẻ đi.

slide 14

Wizard of Oz

slide 13

tại thời điểm tuần thứ ba

rút ngắn khoảng cách

ba thứ cụ thể

Slide 8

### Slide 36 · Q&A Câu hỏi đóng bài — và nó là luận điểm trung tâm

> Trích slide 
>  " Bạn đang quản lý một AI project, hay đang quản lý một tập giả định chưa được kiểm 
>  chứng? "

Đây là slide hay nhất của deck và nó bị đặt ở trang áp chót, sau phần Q&A, nơi phần lớn người 
 học đã đóng file. Nhưng nó là mệnh đề nối toàn bộ 7 chương lại:

| Chương | Nó xử lý giả định loại nào |
| --- | --- |
| Agile / sprint model | Giả định về effort — việc này mất bao lâu |
| MVE / MVP / PoC | Giả định về value — có ai thật sự muốn thứ này không |
| Low-code | Giả định về workflow fit — quy trình có chịu được không |
| PoC Canvas | Giả định về feasibility — làm được ở mức chất lượng nào |
| ROI | Giả định về economics — có đáng tiền không |
| Stakeholder communication | Giả định về alignment — người ký duyệt có 
 đang hiểu cùng một thứ với bạn không |

"cái này đang được làm vì ta đã biết, hay vì ta 
 đang đoán?"

đối xử với hai loại đó giống 
 nhau

timebox

slide 8

Research Spike

Build

### Slide 4–5 Mục tiêu và deliverable — đọc kỹ ba ràng buộc ẩn

> Trích slide 
>  "Hiểu cách quản lý dự án AI trong điều kiện uncertainty cao · Biết cách dùng 
>  Agile + hypothesis-driven delivery thay vì plan cứng · Chọn đúng mức đầu tư giữa 
>  MVE, MVP, và PoC · Tính được ROI có cơ sở và trình bày được với stakeholder." 
>  "Deliverable cuối ngày: PRD final + ROI spreadsheet / model + stakeholder slide deck + 
>  5 phút pitch rehearsal. Dùng lại product đã xác lập ở Day 05 · ROI phải có kịch bản 
>  conservative / realistic / optimistic · Pitch deck phải đủ rõ cho stakeholder quyết 
>  định go / pilot / no-go."

Ba chữ trong hai slide này là ba ràng buộc thật, không phải khẩu hiệu:

| Chữ | Ràng buộc nó áp lên bạn |
| --- | --- |
| hypothesis-driven | Mỗi sprint phải phát biểu được một giả định có thể sai. Một sprint mà mọi kết 
 quả đều được coi là thành công thì không phải hypothesis-driven. |
| ba kịch bản | Bạn không được nộp một con số ROI. Ba kịch bản buộc bạn nói ra 
 giả định nào phân biệt chúng — và đó mới là nội dung thật của mô hình. |
| go / pilot / no-go | Ba lựa chọn, không phải hai. Pilot là lối thoát mà phần lớn bài nộp bỏ quên — 
 và thường là câu trả lời đúng nhất, vì nó mua thêm thông tin thay vì cam kết toàn bộ. |

go / pilot / no-go

mô-đun 
 PoC

go

no-go

pilot

---

<!-- chiron-source-span: {"source_span_id":"c4fc9f3c-a36d-5774-abe9-23d2ed8b35df","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Vì sao AI project không chạy được bằng plan cứng","source_file":"day-06.html"},"checksum":"73d5c3802a4241da3ab075c51193021f9375e8888fead6c57509a7ed1c456f03"} -->

## 01 Vì sao AI project không chạy được bằng plan cứng

Deck khẳng định Agile "gần như bắt buộc" với AI. Chương này tách khẳng định đó ra 
 thành lý do cụ thể, rồi chỉ ra chỗ sơ đồ sprint của slide 8 vẽ thiếu.

### Slide 7 Ba lý do Agile gần như bắt buộc với AI

> Trích slide 
>  "Chất lượng đầu ra phụ thuộc vào dữ liệu, prompt, tool reliability, và user behavior 
>  nên unknowns nhiều hơn software thường. · Nhiều giả định chỉ được kiểm chứng sau khi có 
>  prototype hoặc sau vài vòng eval thực tế. · Requirement cho AI thường cần 
>  calibration chứ không chỉ implementation." 
>  "Lưu ý: Nếu team đối xử với AI project như một backlog feature thông thường, họ sẽ đánh 
>  giá sai effort, sai risk, và sai Definition of Done. "

Chữ đắt nhất trong slide này là **calibration**. Nó nói rằng requirement cho AI không 
 phải một thứ bạn *viết ra rồi thực hiện*, mà là một thứ bạn *điều chỉnh dần cho khớp với 
 năng lực thực tế của hệ thống*. Đó là một khác biệt lớn về bản chất công việc:

|  | Phần mềm thường | Sản phẩm AI |
| --- | --- | --- |
| Requirement | Là đầu vào của việc build | Là đầu ra của vài vòng thử — bạn không biết ngưỡng nào khả thi cho tới khi đo |
| "Xong" nghĩa là | Code chạy đúng đặc tả | Chạy đúng đặc tả trên một phân bố đầu vào — cần bộ eval mới trả lời được |
| Rủi ro lớn nhất | Ước lượng sai thời gian | Xây đúng thứ mình định xây, nhưng thứ đó không đủ tốt để dùng |
| Nguồn của unknown | Độ phức tạp của code | Dữ liệu, prompt, độ tin cậy của tool, và hành vi người dùng — ba trong bốn 
 cái nằm ngoài repo |

dữ liệu · prompt · tool reliability · user behavior

prompt

chạm vào thế giới bên 
 ngoài

Hệ quả:

lấy mẫu thực tế

Research Spike

"sai effort, sai risk, và sai Definition of Done"

Sai effort

Sai risk

Sai Definition of Done

tệ nhất

Slide 10

### Slide 8 AI Sprint Model — và ba câu hỏi bắt buộc mỗi sprint

> Trích slide 
>  " Research Spike → Hypothesis → Build → Eval → Iterate (refine scope / prompt 
>  / data) " 
>  "Mỗi sprint phải trả lời: đã học được gì, giả định nào bị bác bỏ, 
>  và tiếp tục đầu tư hay dừng ở đâu."

Năm ô, nhưng phần quan trọng nhất là dòng chữ bên dưới. Ba câu hỏi đó biến một sprint thành một *thí nghiệm*. Và câu thứ ba — *"tiếp tục đầu tư hay dừng ở đâu"* — là câu mà sơ đồ phía 
 trên nó **không có chỗ để trả lời**: mũi tên duy nhất đi ra khỏi *Eval* là *Iterate*, quay ngược về. Không có lối ra.

iterate

escalation of commitment

slide 14

"tiêu chí dừng"

slide 19

"next decision: nếu đạt / không đạt thì làm gì tiếp"

Hình 1

Đọc kỹ thứ tự năm ô cũng đáng: *Research Spike* đứng **trước** *Hypothesis*. Đó không phải lỗi sắp xếp. Nó nói rằng bạn chưa đủ hiểu bài toán để phát biểu một 
 giả định tốt cho tới khi đã chạm vào dữ liệu thật — ngược với thói quen "họp lấy requirement rồi mới 
 làm".

| Ô | Sản phẩm cụ thể của ô đó | Timebox gợi ý |
| --- | --- | --- |
| Research Spike | Mẫu dữ liệu thật + danh sách unknown, không phải code | 2–3 ngày |
| Hypothesis | Một câu có thể sai, kèm ngưỡng số để phán quyết | nửa ngày |
| Build | Bản đủ chạy để đo, không phải bản đủ đẹp để ship | 3–5 ngày |
| Eval | Con số trên bộ case đã chốt trước khi build | 1 ngày |
| Quyết định | Iterate · Scale · Kill — kèm lý do viết ra | nửa ngày |

"tuần này bọn em đã thử thêm 
 re-ranking và cải thiện prompt."

đã làm gì

đã học được 
 gì

"Giả định 'người dùng sẽ tự viết lại câu hỏi khi bot hỏi lại' đã bị bác bỏ — 
 trong 30 phiên thử, 22 phiên người dùng bỏ giữa chừng thay vì trả lời. Nên chuyển sang gợi ý sẵn ba 
 lựa chọn."

_Sơ đồ: Vòng sprint AI với ba lối ra: iterate, scale và kill - Năm hộp xếp ngang theo thứ tự research spike, hypothesis, build, eval, và quyết định. Research spike sinh ra mẫu dữ liệu thật và danh sách điều chưa biết. Hypothesis là một câu có thể sai kèm ngưỡng số. Build tạo bản đủ chạy để đo. Eval cho con số trên bộ case đã chốt trước. Hộp quyết định ở cuối có ba mũi tên đi ra. Mũi tên iterate quay ngược về hộp hypothesis, nghĩa là tinh chỉnh phạm vi, prompt hoặc dữ liệu rồi thử lại. Mũi tên scale đi lên trên, nghĩa là giả định đã đứng vững nên đầu tư tiếp. Mũi tên kill đi xuống dưới, nghĩa là giả định bị bác bỏ nên dừng và ghi lại bài học. Sơ đồ gốc trên slide chỉ có mũi tên iterate; hai lối ra còn lại được vẽ thêm ở đây._

Hình 1 — Vòng sprint AI và ba lối ra.

slide 8

Quyết định

Scale

Kill

---

<!-- chiron-source-span: {"source_span_id":"c76f4b3e-0081-515d-a63f-e9dd49d88f27","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Ước lượng và Definition of Done dưới bất định","source_file":"day-06.html"},"checksum":"b6f690feb00a65b294d22b48ecfa1005be41efb3b4233f70ee6a70779fb298cd"} -->

## 02 Ước lượng và Definition of Done dưới bất định

Hai slide, hai lỗi kinh điển. Slide 9 nói về việc ước lượng sai vì bỏ quên phần 
 không nhìn thấy. Slide 10 nói về việc đánh dấu "xong" cho một thứ chưa xong.

### Slide 9 Story point cho AI task — bốn loại việc, bốn cách ước lượng sai

> Trích slide 
>  Prompt / behavior tuning — sai lầm: coi như task nhỏ cố định → cách ước 
>  lượng thực dụng: thêm buffer cho iteration và eval 
>  Tool integration — sai lầm: chỉ tính phần code → tính cả error 
>  handling và retries 
>  Data / retrieval work — sai lầm: chỉ tính setup ban đầu → tính thêm 
>  cleaning, coverage, edge cases 
>  UX / trust calibration — sai lầm: bỏ quên hoàn toàn → dành sprint 
>  time cho test với user thật 
>  " Unknowns must be priced in. "

Bốn dòng này có một cấu trúc chung mà slide không nói ra: **mọi sai lầm đều là việc ước lượng 
 phần dễ nhìn thấy và bỏ qua phần chỉ lộ ra khi chạm thực tế.**

| Loại việc | Phần nhìn thấy được (bị ước lượng) | Phần vô hình (bị bỏ) |
| --- | --- | --- |
| Prompt / behavior tuning | Viết prompt — vài giờ | Số vòng phải lặp cho tới khi đạt ngưỡng. Không ai biết trước là 3 vòng hay 12 |
| Tool integration | Gọi API, parse response | Tool sai kiểu gì, timeout bao lâu, retry mấy lần, và bot nói gì với user khi tool 
 chết |
| Data / retrieval | Nạp tài liệu, tạo index | Tài liệu bẩn, trùng lặp, hết hạn; và câu hỏi mà kho không có câu trả lời |
| UX / trust calibration | — | Toàn bộ. Slide ghi thẳng "bỏ quên hoàn toàn" — đây là loại duy nhất trong bốn 
 loại thường không có dòng nào trong backlog |

Priced in

① Ước lượng bằng khoảng, không bằng điểm.

② Đổi công việc thành timebox thay vì ước lượng.

"5 ngày cho việc này; hết 5 ngày mà chưa đạt 
 ngưỡng thì đưa ra quyết định, không tự động gia hạn."

slide 14

ước lượng thiếu

bỏ quên

Ngày 5

một 
 dòng nào

### Slide 10 Definition of Done cho AI feature — và ba loại nợ

> Trích slide 
>  "Không chỉ là 'code chạy'; phải có quality threshold, latency, fallback, 
>  và monitoring signal." 
>  "Ví dụ: support agent chỉ được xem là done khi citation coverage đủ, escalation path rõ, 
>  và test set đạt ngưỡng." 
>  "Backlog AI nên nhìn cả feature debt, data debt, và technical debt."

Bốn thành phần của Definition of Done không phải bốn ô tick ngang hàng — chúng bảo vệ bốn thứ khác 
 nhau, và bỏ cái nào thì hỏng theo kiểu khác nhau:

| Thành phần | Trả lời câu hỏi | Bỏ nó thì hỏng kiểu gì | Viết ra thế nào cho đo được |
| --- | --- | --- | --- |
| Quality threshold | Đủ tốt là bao nhiêu? | "Xong" trở thành ý kiến cá nhân, tranh cãi mỗi lần release | ≥ 85% câu trả lời có trích dẫn đúng nguồn, trên bộ 150 case đã chốt |
| Latency | Nhanh đến mức nào thì còn dùng được? | Chất lượng đạt nhưng người dùng bỏ giữa chừng vì chậm | p95 < 6 giây từ lúc gửi tới lúc hiện chữ đầu tiên |
| Fallback | Khi không chắc hoặc hỏng thì làm gì? | Hệ thống bịa, hoặc trả lỗi thô cho người dùng cuối | Confidence < ngưỡng → hiện 3 câu hỏi gợi ý + nút chuyển người thật |
| Monitoring signal | Sau khi ship thì biết nó còn tốt bằng cách nào? | Chất lượng tụt dần mà không ai phát hiện cho tới khi có người khiếu nại | Log tỉ lệ escalation, tỉ lệ gõ lại câu hỏi, tỉ lệ bỏ giữa chừng — theo tuần |

| Loại nợ | Ví dụ | Đặc điểm |
| --- | --- | --- |
| Feature debt | Ship phần trả lời nhưng chưa ship phần trích nguồn | Nhìn thấy được, có trong backlog, ai cũng nhớ |
| Data debt | Kho tài liệu còn 3 bản chính sách hết hạn; 40% tài liệu chưa gắn ngày ban hành | Vô hình và tự lớn lên. Không ai được giao, không có ticket, và mỗi tuần nó 
 tệ đi một chút vì tài liệu mới vẫn được thêm vào theo cách cũ |
| Technical debt | Prompt hard-code trong code, không có version, không rollback được | Kỹ sư biết và than phiền — nên ít nhất nó có người bảo vệ |

data debt

nó không gây lỗi

đo nó

"citation coverage đủ, escalation path rõ, và test set đạt ngưỡng"

```text
DONE khi và chỉ khi cả 6 điều đúng:
  1. Citation coverage  >= 90% câu trả lời kèm >= 1 nguồn có thể mở được
  2. Citation accuracy  >= 85% nguồn được trích thật sự chứa câu trả lời
                             (chấm tay trên mẫu 50 câu)
  3. Test set           >= 85% pass trên bộ 150 case đã đóng băng trước sprint
  4. Latency            p95 < 6s tới token đầu tiên
  5. Fallback           mọi nhánh trong 4 paths có UI đã test:
                             happy · low-confidence · failure · correction
  6. Monitoring         4 tín hiệu đang chảy vào dashboard trước khi mở cho user:
                             escalation · rephrase · abandon · thumbs
```

Coverage

accuracy

tệ hơn

---

<!-- chiron-source-span: {"source_span_id":"149b94f4-cad8-5c85-8514-6847a4b8332c","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 MVE · MVP · PoC — chọn đúng mức đầu tư","source_file":"day-06.html"},"checksum":"bbece3b6bb31a6320be2187332b588cbce881d2aa43c406fe7200f425e41424f"} -->

## 03 MVE · MVP · PoC — chọn đúng mức đầu tư

Ba từ hay bị dùng lẫn. Deck phân biệt chúng theo *mục tiêu*, không theo quy 
 mô — và đó là cách phân biệt đúng. Chương này kết thúc bằng câu hỏi mà deck đặt ra nhưng không tính: *một PoC thì đáng chi bao nhiêu tiền?*

### Slide 12 Ba mức, ba câu hỏi khác nhau

> Trích slide 
>  MVE — mục tiêu: test giả định giá trị nhanh nhất · câu hỏi: 
>  "user có thật sự muốn thứ này không?" 
>  MVP — mục tiêu: ship phiên bản nhỏ có thể dùng được · câu hỏi: 
>  "workflow có vận hành được không?" 
>  PoC — mục tiêu: giảm bất định cho stakeholder / sponsor · câu hỏi: 
>  "có đáng đầu tư thêm không?" 
>  " Đừng dùng 3 từ này lẫn lộn. Nếu mục tiêu là học nhanh, hãy ưu tiên MVE. Nếu mục 
>  tiêu là xin phê duyệt tiếp, hãy thiết kế PoC."

Điều tinh tế nhất trong bảng này: **ba mức khác nhau ở chỗ ai là người phải bị thuyết 
 phục.**

| Mức | Người phải bị thuyết phục | Bằng chứng họ chấp nhận | Có cần code không? |
| --- | --- | --- | --- |
| MVE | Người dùng | Họ hành động — bấm, quay lại, chờ, trả tiền, hỏi khi nào có | Không. Landing page, form, hoặc người làm tay phía sau là đủ |
| MVP | Quy trình vận hành | Một workflow thật chạy hết từ đầu đến cuối, có người thật dùng, có lỗi thật xảy ra | Có, nhưng hẹp — một luồng, một nhóm user |
| PoC | Người ký duyệt ngân sách | Một con số so với một ngưỡng đã hứa trước khi chạy | Tuỳ. PoC có thể là một phân tích dữ liệu, không nhất thiết là phần mềm |

PoC

Cách tự kiểm trong 10 giây:

"Sau khi làm xong việc 
 này, [tên người] sẽ quyết định [quyết định gì], dựa trên [con số nào]."

chi phí để học một đơn vị thông tin

① MVE

có ai muốn không

② PoC

có làm nổi ở mức chất lượng cần không

③ MVP

quy trình có chịu được không

slide 2

### Slide 13 Wizard of Oz — và câu đính chính quan trọng ở cuối slide

> Trích slide 
>  Khi nào nên dùng: "Chưa chắc user value có thật · Chưa cần đầu tư model / 
>  integration lớn · Muốn test workflow hoặc adoption risk sớm" 
>  Ví dụ: "'AI support agent' nhưng backend thật ra là human draft response 
>  · 'AI sales assistant' nhưng qualification do BA làm thủ công phía sau" 
>  "Lưu ý: Wizard of Oz không phải 'giả vờ để lừa user'. Nó là cách kiểm chứng value 
>  và workflow trước khi đầu tư sâu vào hệ thống."

Câu đính chính cuối slide đáng đọc kỹ, vì ranh giới giữa "kiểm chứng" và "lừa" là ranh giới thật và 
 có hệ quả pháp lý ở một số ngành. Ranh giới đó nằm ở ba chỗ:

| Câu hỏi | Wizard of Oz hợp lệ | Đã thành lừa dối |
| --- | --- | --- |
| Người dùng có bị thiệt hại nếu câu trả lời sai không? | Không — nội bộ, phi rủi ro, có thể sửa | Có — quyết định y tế, tài chính, pháp lý dựa trên đó |
| Dữ liệu người dùng đi đâu? | Người xử lý là nhân sự nội bộ, đã có quyền xem dữ liệu đó theo vai trò | Dữ liệu nhạy cảm được chuyển cho người vốn không được phép xem |
| Bạn có hứa gì cụ thể không? | Không hứa "do AI xử lý"; chỉ hứa kết quả và thời gian | Quảng cáo là "AI tự động" trong khi 100% là người làm — đây là quảng cáo sai sự thật |

bốn

① Có ai dùng không

② Họ hỏi cái gì

phân bố câu hỏi 
 thật

③ Mất bao lâu để làm đúng

phút xử lý thủ công

mô hình ROI

mô-đun độ nhạy

④ Có bao nhiêu phần trăm ca là ca khó

Nghĩa là Wizard of Oz không chỉ 
 kiểm chứng value — nó là cách hợp lệ duy nhất để có baseline trước khi có sản phẩm.

DoorDash

Fireflies

khi nào thì nên chọn nó thay vì MVP

### Slide 14 Timebox và kỷ luật ngân sách — bốn ô, và ô thứ tư hay bị bỏ

> Trích slide 
>  "Mỗi thử nghiệm cần có giả định, thời hạn, budget ceiling, và tiêu chí dừng." 
>  "Ví dụ: 'Trong 2 tuần, test internal policy assistant cho 20 câu hỏi lặp lại; nếu 
>  time-to-answer không giảm đáng kể, dừng.' " 
>  " Đầu tư nhỏ nhưng học nhanh tốt hơn đầu tư lớn rồi mới biết không có user value."

Ví dụ của slide gần đúng nhưng còn một lỗ hổng, và lỗ hổng đó là lỗi phổ biến nhất khi viết tiêu chí 
 dừng: **"không giảm đáng kể" không phải một tiêu chí.** Nó là một câu sẽ được diễn giải 
 lại sau khi có kết quả — nghĩa là nó không ràng buộc gì cả.

| Ô | Ví dụ của slide | Bản viết chặt lại |
| --- | --- | --- |
| Giả định | (ngầm) trợ lý chính sách giúp trả lời nhanh hơn | "Nhân viên HR tra chính sách trung bình 12 phút/câu; trợ lý đưa được xuống dưới 4 phút cho 
 nhóm câu hỏi lặp lại" |
| Thời hạn | 2 tuần | 2 tuần, kết thúc 14/03, review lúc 10:00 ngày 14/03 |
| Budget ceiling | (không có) | 60 triệu — gồm 2 người × 2 tuần + chi phí API. Vượt trần thì dừng, không xin thêm |
| Tiêu chí dừng | "không giảm đáng kể" | "Nếu trung vị time-to-answer trên 20 câu không giảm ít nhất 40%, hoặc dưới 12/20 câu 
 có câu trả lời đúng nguồn, thì dừng." |

"đúng là chưa giảm nhiều, nhưng bọn em học được rất nhiều và lần 
 sau sẽ nhanh hơn."

trước

Success criteria — chốt trước với stakeholder

slide 19

budget ceiling

trần đó nên là bao nhiêu?

"giảm bất định"

giảm được bao nhiêu bất định thì đáng bao nhiêu tiền?

giá trị của thông tin

hai vùng

#### Tương tác PoC đáng chi bao nhiêu tiền — và khi nào thì đáng đúng bằng không

Slide 14 yêu cầu mỗi thử nghiệm có *"budget ceiling"*. Slide 18 nói PoC tốt 
 phải *"giảm bất định"*. Ghép hai câu đó lại thì được một bài toán tính được: **giá của 
 việc giảm bất định**. Mô-đun này tính ngân sách PoC tối đa còn đáng chi, theo lý thuyết giá trị 
 thông tin.

Mặc định: bạn tin ý tưởng đúng khoảng **50%**. Nếu đúng, dự án tạo **800 triệu** giá trị ròng; nếu sai, bạn mất **350 triệu**. PoC của bạn 
 bắt được ý tưởng tốt **85%** số lần và loại đúng ý tưởng tồi **80%** số 
 lần. Bạn định chi **60 triệu** cho PoC.

Đoán trước ba điều: *(a)* PoC này đáng chi tối đa bao nhiêu? *(b)* Nếu bạn tin tới 
 85% thay vì 50%, ngân sách tối đa tăng hay giảm? *(c)* Nếu PoC của bạn kém đi một chút — 
 70% / 65% thay vì 85% / 80% — thì ngân sách tối đa còn bao nhiêu?

#### Kéo rồi mở

**(a) Tối đa 80,0 triệu.** Bạn định chi 60 triệu, nên PoC này *đáng chạy* — 
 lãi ròng kỳ vọng 20 triệu. Trần tuyệt đối (nếu có một PoC hoàn hảo, biết chắc đúng sai) là **175,0 triệu**, nên PoC của bạn thu được **45,7%** lượng bất định có 
 thể xoá.

**(b) Giảm, và giảm về 0.** Ở p = 85%, ngân sách tối đa là **0 đồng**. 
 Lý do không phải "vì bạn đã chắc rồi nên thông tin ít giá trị hơn" — mà mạnh hơn thế: *kể cả khi PoC cho kết quả xấu, EV của việc build vẫn dương, nên bạn vẫn build.* Một phép 
 thử mà không kết quả nào làm bạn đổi quyết định thì **giá trị của nó bằng đúng không**, 
 bất kể nó tốn bao nhiêu.

**(c) Cũng bằng 0 — và đây là kết quả gây sốc nhất của mô-đun.** Với PoC 
 70% / 65%, ngân sách tối đa rơi từ 80 triệu xuống **đúng 0**, không phải "thấp hơn 
 một chút". Vì ở chất lượng đó, ngay cả một kết quả âm cũng để lại hậu nghiệm 31,6% — vẫn trên 
 ngưỡng hoà vốn 30,4% — nên bạn vẫn build. *Một phép thử lỏng không phải là phép thử rẻ; nó 
 không phải phép thử.*

**Điều đáng ngạc nhiên thứ tư — hãy kéo thanh p từ trái sang phải và nhìn đường xanh:** giá trị của PoC bằng 0 ở *cả hai đầu* và đạt đỉnh ở giữa. Với các tham số mặc định, cửa sổ 
 mà PoC còn đáng chạy là **p từ 9,3% đến 70,0%**, đỉnh **158,3 triệu** tại 
 p = 30,4%. Ngoài cửa sổ đó, bạn đã biết câu trả lời — chỉ là chưa thừa nhận.

*Bài học vận hành:* đỉnh nằm đúng tại p* = L / (V + L) = 30,4% — điểm mà bạn hoàn toàn 
 phân vân giữa build và không build. **PoC có giá trị cao nhất ở đúng chỗ bạn khó chịu 
 nhất.** Và đó là lý do PoC hay bị chạy sai chỗ: người ta chạy PoC cho những ý tưởng ai cũng 
 thích (p cao, giá trị ≈ 0, chỉ để hợp thức hoá) thay vì cho những ý tưởng gây tranh cãi.

- **Control - Tin tưởng ban đầu p — "ý tưởng này đúng": 50%**: min `2`, max `98`, step `1`, default `50`

- **Control - Giá trị ròng V nếu ý tưởng đúng: 800 triệu đ**: min `100`, max `3000`, step `50`, default `800`

- **Control - Thiệt hại L nếu ý tưởng sai: 350 triệu đ**: min `50`, max `2000`, step `25`, default `350`

- **Control - Độ nhạy Se — PoC bắt được ý tưởng tốt: 85%**: min `50`, max `100`, step `1`, default `85`

- **Control - Độ đặc hiệu Sp — PoC loại đúng ý tưởng tồi: 80%**: min `50`, max `100`, step `1`, default `80`

- **Control - Chi phí PoC bạn định chi: 60 triệu đ**: min `10`, max `500`, step `5`, default `60`

Ngân sách PoC tối đa

—

—

Trần thông tin hoàn hảo

—

—

Xoá được bao nhiêu bất định

—

—

Phán quyết

—

—

PoC của bạn PoC hoàn hảo — trần tuyệt đối mức tin tưởng bạn đang đặt

#### Xem bảng: chất lượng PoC đổi ngân sách tối đa thế nào



#### Công thức & giới hạn của mô hình

- Bài toán quyết định hai hành động: EV(build) = p·V − (1−p)·L và 
 EV(không build) = 0. Cơ sở so sánh là max của hai giá trị đó.
- PoC cho tín hiệu nhị phân. Theo Bayes: P(+) = p·Se + (1−p)(1−Sp), 
 p⁺ = p·Se / P(+), p⁻ = p(1−Se) / P(−). Với mỗi kết quả bạn chọn hành động 
 tốt hơn, nên EV(có PoC) = Σ P(kết quả) · max(0, EV build theo hậu nghiệm).
- Giá trị thông tin VoI = EV(có PoC) − cơ sở. Đó chính là ngân sách 
 tối đa: chi nhiều hơn VoI thì thà không thử.
- EVPI (trần) = p·V − cơ sở — giá của một phép thử hoàn hảo. Không 
 PoC nào vượt được con số này, nên nó là kiểm tra tỉnh táo hữu ích trước mọi đề xuất ngân sách.
- Ngưỡng hoà vốn của hậu nghiệm là p* = L / (V + L). Cửa sổ mà PoC có giá trị dương 
 là khoảng p mà ít nhất một kết quả của PoC đẩy hậu nghiệm qua ngưỡng đó. Đỉnh của đường 
 cong nằm đúng tại p = p*.
- Giới hạn ①: mô hình coi kết quả PoC là nhị phân (đạt / không đạt). PoC thật 
 cho ra một dải kết quả, và phần lớn thông tin thật nằm ở vì sao chứ không ở đạt hay không. 
 Nghĩa là mô hình này đánh giá thấp giá trị của một PoC được thiết kế tốt.
- Giới hạn ②: V và L là hai con số bạn cũng đang đoán. Không sao — mục đích của 
 mô-đun không phải cho ra một con số chính xác, mà cho thấy hình dạng của câu trả lời: giá 
 trị thông tin bằng 0 ở hai đầu, đỉnh ở giữa, và sụp nhanh khi chất lượng phép thử giảm.
- Giới hạn ③: bỏ qua giá trị lựa chọn của việc trì hoãn, chi phí cơ hội khi 
 timebox chiếm mất người, và khả năng PoC tự nó tạo ra giá trị (ví dụ thu được eval set thật — 
 xem slide 13 ). Cả ba đều đẩy giá trị thật lên cao hơn con số hiển thị.

---

<!-- chiron-source-span: {"source_span_id":"383e3ba3-9e2c-589a-97e0-24a7001c954d","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Low-code / no-code cho PoC","source_file":"day-06.html"},"checksum":"563305204c5e706388e0ae36f9b3a89c115410006dbe8cbef3f8c919330ecf55"} -->

## 04 Low-code / no-code cho PoC

Hai slide ngắn, một thông điệp lặp lại hai lần: low-code dùng để *validate*, 
 không dùng để *quyết định thay*. Chương này tách ra vì sao ranh giới đó dễ bị vượt qua.

### Slide 16 Ba công cụ, ba chỗ đứng trong lifecycle

> Trích slide 
>  Assistants API — phù hợp: PoC nhanh với tool calls cơ bản · giới hạn: 
>  chưa thay cho architecture production 
>  Dify — phù hợp: demo workflow, RAG, và app UI nhanh · giới hạn: 
>  không giải hết bài toán enterprise phức tạp 
>  LangFlow — phù hợp: giải thích flow agent theo cách trực quan · giới hạn: 
>  không thay cho product discovery đầy đủ 
>  "Low-code nên được dùng để demo nhanh, kiểm chứng workflow, và hỗ trợ PoC; không 
>  nên thay cho product discovery hay production planning."

Ba giới hạn của slide nghe giống nhau nhưng thực ra là ba loại giới hạn khác nhau hẳn — và biết 
 đúng loại nào giúp bạn biết cái gì *chuyển được* sang production, cái gì không:

| Công cụ | Loại giới hạn | Cái gì chuyển được sang production |
| --- | --- | --- |
| Assistants API | Kỹ thuật — thiếu quyền kiểm soát: version của prompt, retry policy, quan sát nội bộ, 
 chi phí ở quy mô lớn | Prompt, định nghĩa tool, và bộ case bạn đã thử. Phần orchestration thì viết lại |
| Dify | Phạm vi — chạy tốt tới một mức phức tạp rồi dừng: phân quyền, dữ liệu nhiều nguồn, 
 audit trail, tích hợp hệ thống nội bộ | Thiết kế workflow, chiến lược chunking, và số liệu retrieval quan sát được |
| LangFlow | Nhận thức — nó là công cụ giải thích, không phải công cụ khám phá. 
 Nó cho thấy flow bạn đã nghĩ ra trông thế nào, không cho biết flow đó có đúng không | Bản vẽ dùng cho tài liệu và cho buổi họp với stakeholder |

cấu hình

ba tài sản không phụ thuộc công cụ

Bộ câu hỏi thật

Danh sách failure mode

Số đo baseline

mô hình ROI

### Slide 17 Khi nào PM / BA nên tự dùng low-code

> Trích slide 
>  "Khi cần stakeholder demo trong thời gian ngắn · Khi muốn test workflow 
>  fit trước khi team engineer build sâu · Khi muốn minh hoạ rõ user journey và điểm 
>  gãy của experience" 
>  "Low-code giúp validate nhanh, nhưng không thay thế việc viết PRD rõ, risk register rõ, 
>  và success metrics rõ."

Ba tình huống của slide có một điểm chung: cả ba đều là tình huống mà **thứ bạn cần là một 
 vật thể để người khác phản ứng lại**, chứ không phải một hệ thống chạy được. Đó là lý do 
 low-code hợp — nó tạo ra vật thể đó nhanh gấp nhiều lần.

"vậy là gần 
 xong rồi."

thiết 
 kế cho lúc AI sai

51,2%

Cách xử lý — nói trước khi demo, không nói sau:

"đây là 5 case chọn sẵn; chúng tôi chưa biết tỉ lệ đúng trên phân bố thật, và đó chính là thứ 
 PoC tiếp theo sẽ đo."

PRD rõ · risk register rõ · success metrics rõ

tài liệu về quyết 
 định

ai dùng, sai thì ai chịu, 
 bao nhiêu thì đủ tốt.

Ngày 5

---

<!-- chiron-source-span: {"source_span_id":"91abbfb6-b806-5c2d-8d4d-51ecbd2c6b8d","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 PoC Canvas — và PoC không phải là gì","source_file":"day-06.html"},"checksum":"5e86a44937660600bccfc1ad0171335bf444be14e51a613453e2e3669f573254"} -->

## 05 PoC Canvas — và PoC không phải là gì

Năm ô phải chốt trước khi bắt đầu. Chương này điền thử cả năm ô cho một PoC thật, và 
 chỉ ra ô nào bị bỏ trống thường xuyên nhất.

### Slide 19 PoC Canvas — năm ô, và ô cuối là ô quan trọng nhất

> Trích slide 
>  Key hypothesis — giả định giá trị hoặc feasibility cần kiểm chứng 
>  Scope — 1 workflow hẹp, 1 nhóm user hẹp, 1 bộ dữ liệu hẹp 
>  Success criteria — metric đo được, chốt trước với stakeholder 
>  Timebox — 2–4 tuần, có điểm review rõ 
>  Next decision — nếu đạt / không đạt thì làm gì tiếp

Ô *Next decision* là ô bị bỏ trống nhiều nhất, và nó là ô duy nhất khiến bốn ô kia có nghĩa. 
 Lý do rất người: điền ô đó buộc bạn viết ra **"nếu không đạt thì chúng ta dừng"** — và 
 không ai muốn viết câu đó về chính dự án mình đang xin ngân sách.

Nhưng bỏ trống nó có một hệ quả tính được. Theo [mô-đun PoC](#m-voi): nếu cả kết quả 
 đạt lẫn không đạt đều dẫn tới cùng một hành động, thì **giá trị thông tin của PoC bằng đúng 
 không**. Ô *Next decision* chính là chỗ bạn chứng minh rằng con số đó khác không.

```text
KEY HYPOTHESIS
  "Nhân viên HR mất trung bình 12 phút để tra một câu hỏi chính sách lặp lại.
   Một trợ lý RAG trên kho tài liệu nội bộ đưa được xuống dưới 4 phút,
   với ít nhất 85% câu trả lời trích đúng nguồn."
   → giả định có thể SAI ở hai chỗ: 12 phút có thể là số bịa, và 85% có thể bất khả thi

SCOPE
  1 workflow : tra cứu chính sách nghỉ phép + bảo hiểm (không gồm lương, kỷ luật)
  1 nhóm user: 8 nhân viên HR ở một chi nhánh
  1 bộ dữ liệu: 42 văn bản chính sách hiện hành, đã lọc bản hết hạn

SUCCESS CRITERIA  (chốt với Trưởng phòng HR + CFO trước ngày bắt đầu)
  - trung vị time-to-answer  <= 4 phút   (baseline đo trước: 12 phút)
  - citation accuracy        >= 85%      (chấm tay, 50 câu, 2 người chấm độc lập)
  - tỉ lệ câu bot từ chối trả lời <= 25% (cao hơn = kho tài liệu chưa đủ)

TIMEBOX
  3 tuần · bắt đầu 03/03 · review 10:00 ngày 21/03 · trần ngân sách 60 triệu
  đo baseline trong tuần 1, KHÔNG phải sau khi có sản phẩm

NEXT DECISION
  đạt cả 3          -> GO: xin ngân sách build, mở rộng sang 3 chi nhánh
  đạt 2/3, hụt citation -> PILOT: 6 tuần nữa, chỉ làm chất lượng nguồn, không thêm scope
  hụt time-to-answer    -> NO-GO: giả định giá trị sai, dừng và viết lại problem statement
  từ chối > 40%         -> NO-GO NHƯNG đổi bài toán: vấn đề là kho tài liệu, không phải AI
```

Một:

trong tuần 1

Hai:

phát hiện rằng bài toán nằm ở chỗ khác

quy kết được nguyên nhân

điều kiện để phép thử có sức 
 phân giải

mô-đun PoC

### Slide 20 PoC không nên làm gì — ba điều, và điều thứ ba là điều nguy hiểm nhất

> Trích slide 
>  PoC nên làm: "giảm bất định chính · đo giá trị ban đầu · kiểm chứng workflow hẹp" 
>  PoC không nên làm: "ôm toàn bộ scope tương lai · hứa production readiness · 
>  dùng demo đẹp để che metric yếu "

| Điều không nên | Hỏng ở đâu | Ai chịu hậu quả |
| --- | --- | --- |
| Ôm toàn bộ scope tương lai | Timebox vỡ; và kết quả không quy kết được về nguyên nhân nào | Team — họ mất 3 tháng cho một câu trả lời đáng lẽ mất 3 tuần |
| Hứa production readiness | PoC được đưa thẳng vào vận hành vì "nó chạy rồi mà" | Người dùng cuối và đội vận hành |
| Dùng demo đẹp để che metric yếu | Quyết định đầu tư được đưa ra trên thông tin sai | Tổ chức — và hậu quả xuất hiện sau 6–12 tháng, khi không còn ai nhớ buổi demo |

①

②

③

Cách chặn, đặt vào quy trình chứ không dựa vào thiện chí:

một case thất bại có thật

chính

một

mô-đun PoC

đúng 0 đồng

một

---

<!-- chiron-source-span: {"source_span_id":"bda8e1d5-d687-52ee-b460-f2c1702f6599","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Giải phẫu chi phí và giá trị","source_file":"day-06.html"},"checksum":"91d3c1c5217070be90ae6e2b8a0e7676cd37c15b96b514232179930e28248709"} -->

## 06 Giải phẫu chi phí và giá trị

Ba slide liên tiếp (22, 23, 24) là trung tâm của cả bài — và cả ba đều không có một 
 con số nào. Chương này giữ nguyên cấu trúc của chúng rồi đưa số vào.

### Slide 22 Cost anatomy và value anatomy — bốn hàng, và một ô trống đáng chú ý

> Trích slide 
>  Build — cost: dev effort, setup, integration · value: launch nhanh 
>  hơn, tạo năng lực mới 
>  Run — cost: API cost, compute, storage · value: throughput cao hơn, 
>  bớt việc tay 
>  Operate — cost: human review, monitoring, maintenance · value: giữ 
>  chất lượng, giảm rủi ro 
>  Business impact — cost: — · value: time saved, revenue, cost 
>  avoidance 
>  " ROI starts with anatomy, not optimism. "

Bảng này đúng và hữu ích. Nhưng có một ô đáng nói: hàng *Business impact* có cột cost là **một dấu gạch ngang**. Slide đang nói rằng việc tạo ra tác động kinh doanh không tốn gì. 
 Điều đó không đúng, và khoản chi phí bị bỏ sót đó thường lớn hơn cả API cost.

"time saved"

thật sự đổi cách làm việc

| Chi phí bị bỏ trong ô "—" | Ví dụ cụ thể |
| --- | --- |
| Change management & đào tạo | Buổi hướng dẫn cho 8 nhân viên HR, tài liệu, người hỗ trợ trong tháng đầu |
| Thiết kế lại quy trình | Ai duyệt câu trả lời trước khi gửi ra ngoài? Quy trình cũ không có bước đó |
| Chi phí adoption chậm | Ba tháng đầu chỉ 30% người dùng chuyển sang — nhưng bạn đã trả 100% chi phí vận hành |
| Chi phí chạy song song | Quy trình cũ vẫn phải duy trì cho tới khi đủ tin — nghĩa là trả tiền hai lần |

Mô hình ROI

trần adoption

ramp

mô-đun độ nhạy

Ba hàng đầu cũng đáng phân biệt theo một trục mà slide không vẽ: **trả một lần hay trả 
 mãi**. Đó là trục quyết định hình dạng của đường break-even.

| Hàng | Kiểu chi | Ảnh hưởng lên đường break-even |
| --- | --- | --- |
| Build | Một lần | Đẩy điểm xuất phát của đường chi phí lên cao; không đổi độ dốc. Cắt build chỉ dời điểm 
 hoà vốn, không cứu được dự án lỗ |
| Run | Theo lượng dùng | Thêm độ dốc, tỉ lệ với adoption — nghĩa là càng thành công càng tốn |
| Operate | Phần cố định + phần theo lượng dùng | Phần cố định là phần độc hại nhất: nó chạy từ tháng 1 kể cả khi chưa ai dùng |

lãi ròng mỗi tháng khi bão hoà

mô hình ROI

Conservative

4,3 triệu/tháng

không hoà vốn trong 24 tháng

_Sơ đồ: Bốn tầng chi phí và bốn tầng giá trị, với ô chi phí bị bỏ trống ở hàng tác động kinh doanh - Bảng hai cột. Cột trái là chi phí, cột phải là giá trị, xếp theo bốn hàng. Hàng build có chi phí là công sức phát triển, thiết lập và tích hợp, trả một lần, và giá trị là ra mắt nhanh hơn cùng năng lực mới. Hàng run có chi phí là gọi mô hình, tính toán và lưu trữ, trả theo lượng dùng, và giá trị là thông lượng cao hơn, bớt việc tay. Hàng operate có chi phí là người kiểm duyệt, giám sát và bảo trì, gồm phần cố định và phần theo lượng dùng, và giá trị là giữ chất lượng, giảm rủi ro. Hàng thứ tư là tác động kinh doanh: ô giá trị ghi thời gian tiết kiệm, doanh thu và chi phí tránh được, nhưng ô chi phí trên slide gốc chỉ là một dấu gạch ngang. Ô đó được tô nổi bật và liệt kê bốn khoản bị bỏ sót: quản trị thay đổi và đào tạo, thiết kế lại quy trình, chi phí do adoption chậm, và chi phí duy trì song song quy trình cũ._

Hình 2 — Bảng giải phẫu của slide 22, và ô mà nó để trống.

Business impact · chi phí

### Slide 23 Ba kịch bản — và điều chúng thật sự dùng để làm

> Trích slide 
>  Conservative — adoption chậm · cost cao hơn · value thấp hơn 
>  Realistic — baseline hợp lý · dựa trên pilot và benchmark nội bộ 
>  Optimistic — adoption tốt · workflow fit cao · ít friction hơn dự kiến 
>  "Stakeholder cần thấy phạm vi kết quả có thể xảy ra, không chỉ một con số đẹp 
>  duy nhất."

Ba kịch bản hay bị hiểu sai thành *"đưa ba con số để nếu sai còn có chỗ lùi"*. Đó là cách 
 dùng phòng thủ và nó không tạo ra thông tin gì. Cách dùng đúng nằm ở chỗ khác: **ba kịch bản 
 buộc bạn phát biểu ra *giả định nào* phân biệt chúng.**

| Tham số bị đổi | Conservative | Realistic | Optimistic |
| --- | --- | --- | --- |
| Trần adoption | ×0,60 | ×1 | ×1,25 |
| Số tháng để đạt trần (ramp) | 6 | 3 | 2 |
| % thời gian tiết kiệm được | ×0,80 | ×1 | ×1,15 |
| API cost mỗi truy vấn | ×1,30 | ×1 | ×0,80 |
| Tỉ lệ cần human review | ×1,40 | ×1 | ×0,70 |
| Chi phí build | ×1,25 | ×1 | ×0,90 |
| Vận hành cố định | ×1,20 | ×1 | ×0,90 |

Đây mới là nội dung thật của "ba kịch bản".

"tôi nghĩ adoption chậm hơn ×0,60 nhiều"

"tôi nghĩ ROI không tới 18%"

các giả định xấu có xu hướng đi cùng nhau

xấu hơn nhiều

−57,2%

+96,2%

### Slide 24 Break-even logic — một đồ thị không có trục số

> Trích slide 
>  Đồ thị: trục hoành Tháng, trục tung Giá trị tích luỹ / Chi phí, hai đường 
>  Cost và Value cắt nhau tại Break-even point. 
>  " Dự án đạt break-even ở tháng nào, dưới kịch bản nào, và giả định nào có thể đẩy mốc này 
>  ra xa hơn? "

Câu hỏi dưới đồ thị là câu hỏi hay nhất của cả deck, vì nó hỏi đúng ba thứ và theo đúng thứ tự: *tháng nào* (kết quả) · *dưới kịch bản nào* (điều kiện) · *giả định nào đẩy nó xa 
 hơn* (độ nhạy). Ba câu đó là ba mục tiếp theo của tài liệu này.

Vẽ đúng ①:

không

Vẽ đúng ②:

Vẽ thiếu:

một

"dưới kịch bản nào"

ba

5

10

không bao giờ trong 24 tháng

khi nào tiền quay lại

bao nhiêu

①

Lãi ròng mỗi tháng khi bão hoà

②

Điểm hoà vốn

③

Lãi ròng tích luỹ 24 tháng

④

Độ nhạy

giả định nào có thể lật ba số trên

#### Tương tác ROI ba kịch bản và điểm hoà vốn — slide 22, 23, 24 với số thật

Ba slide vừa đọc đưa ra cấu trúc nhưng không đưa con số nào. Mô-đun này chạy đúng cấu 
 trúc đó trên một ví dụ cụ thể: **trợ lý tra cứu chính sách nội bộ**, cùng sản phẩm dùng 
 xuyên suốt Ngày 5 và Ngày 6. Mọi tham số mặc định là giả định của tài liệu, không phải của slide.

Mặc định: 4.000 truy vấn/tháng · mỗi truy vấn hiện tốn 12 phút của con người · chi phí lao động 
 150 nghìn đ/giờ · AI tiết kiệm 70% thời gian · trần adoption 60% · build 250 triệu · API 900 đ/truy 
 vấn · 25% cần người kiểm · vận hành cố định 12 triệu/tháng.

Đoán trước: *(a)* dự án hoà vốn ở tháng thứ mấy? *(b)* trong tổng chi phí 12 tháng, 
 API chiếm bao nhiêu phần trăm? *(c)* kịch bản Conservative hoà vốn ở tháng thứ mấy?

#### Kéo rồi mở

**(a) Tháng 10** ở kịch bản Realistic. ROI 12 tháng là **+18,6%** — 
 dương, nhưng không ấn tượng, và đó là con số trung thực cho một dự án AI nội bộ có quy mô này. 
 Sau 24 tháng, lãi ròng tích luỹ là **468,0 triệu**.

**(b) API chỉ chiếm 5,1%** tổng chi phí 12 tháng — 23,8 triệu trên 467,3 triệu. 
 Trong khi build chiếm **53,5%**, vận hành cố định **30,8%**, và *human review chiếm 10,6% — hơn gấp đôi API*. 
 Đây là kết quả đáng nhớ nhất của mô-đun. Chi phí token là dòng chi được nói tới nhiều nhất 
 trong mọi cuộc họp về AI, và nó là dòng **nhỏ nhất** trong bốn dòng.

**(c) Không bao giờ** — trong 24 tháng, kịch bản Conservative không hoà vốn. ROI 
 12 tháng là **−57,2%**. Lý do nằm ở lãi ròng khi bão hoà: chỉ **4,3 triệu/tháng** so với 31,7 triệu ở Realistic. Với 4,3 triệu/tháng, riêng việc trả lại 312,5 triệu chi 
 phí build đã mất hơn sáu năm.

**Thử điều đáng thử nhất — kéo "phút xử lý thủ công" từ 12 xuống 9:** chỉ giảm 
 3 phút, và dự án chuyển từ hoà vốn tháng 10 sang *không hoà vốn trong 24 tháng*. Con số 12 
 phút đó là một con số bạn **đoán** hay một con số bạn **đo**? Nếu là 
 đoán, toàn bộ mô hình đang đứng trên nó. Đó chính là lý do [Wizard of Oz](#s13) đáng làm — nó là cách rẻ nhất để biến con số này từ đoán thành đo.

*Bài học vận hành:* khoảng ROI 12 tháng đi từ **−57,2%** tới **+96,2%**. Nếu bạn trình bày cho CFO *một* con số trong khoảng đó, bạn không 
 đang báo cáo — bạn đang chọn. Đó chính xác là điều slide 23 muốn chặn.

Conservative

Realistic

Optimistic

- **Control - Số truy vấn mỗi tháng: 4.000**: min `500`, max `20000`, step `250`, default `4000`

- **Control - Phút xử lý thủ công mỗi truy vấn: 12 phút**: min `2`, max `45`, step `1`, default `12`

- **Control - Chi phí lao động: 150 nghìn đ/giờ**: min `50`, max `500`, step `10`, default `150`

- **Control - % thời gian AI tiết kiệm được: 70%**: min `10`, max `95`, step `5`, default `70`

- **Control - Trần adoption: 60%**: min `10`, max `95`, step `5`, default `60`

- **Control - Chi phí build (một lần): 250 triệu đ**: min `50`, max `1500`, step `25`, default `250`

- **Control - API cost mỗi truy vấn: 900 đ**: min `100`, max `8000`, step `100`, default `900`

- **Control - Tỉ lệ cần human review: 25%**: min `0`, max `100`, step `5`, default `25`

- **Control - Vận hành cố định mỗi tháng: 12 triệu đ**: min `0`, max `80`, step `2`, default `12`

Điểm hoà vốn

—

—

ROI 12 tháng

—

—

Lãi ròng 24 tháng

—

—

Lãi ròng/tháng khi bão hoà

—

—

giá trị tích luỹ chi phí tích luỹ điểm hoà vốn

Và đây là [bảng giải phẫu của slide 22](#s22) với 
 số thật — bốn dòng chi phí 12 tháng đặt cạnh dòng giá trị chúng tạo ra:

build (một lần) vận hành cố định human review API / compute

#### Xem bảng: ba kịch bản cạnh nhau



#### Công thức & giới hạn của mô hình

- adoption(m) = trần × min(1, m / ramp) — tăng tuyến tính tới trần rồi giữ nguyên. 
 Thực tế đường adoption thường có dạng chữ S; tuyến tính là xấp xỉ đủ dùng cho chân trời 24 tháng.
- giá trị(m) = Q · adoption(m) · (T/60) · D · W — giờ công tiết kiệm được nhân chi 
 phí lao động.
- chi phí(m) = Q·adoption(m)·api + Q·adoption(m)·R·(3/60)·W + M. Thời gian review 
 cố định 3 phút mỗi ca cần kiểm.
- Chi phí build B được tính hết vào tháng 0. Hoà vốn = tháng đầu tiên mà giá trị 
 tích luỹ ≥ chi phí tích luỹ.
- Giới hạn ①: không chiết khấu dòng tiền. Với chân trời 24 tháng và 
 lãi suất thực dương, điểm hoà vốn thật sẽ muộn hơn con số này một chút.
- Giới hạn ②: giả định giờ tiết kiệm được quy thẳng ra tiền. Điều đó 
 chỉ đúng nếu tổ chức thật sự dùng số giờ đó vào việc khác có giá trị, hoặc giảm được biên chế. 
 Nếu không, đây là "giá trị mềm" và cần nói rõ với CFO — slide 25 chính là chỗ 
 nói.
- Giới hạn ③: bỏ qua chi phí change management và chi phí chạy song song quy 
 trình cũ — hai khoản nằm trong ô mà Hình 2 chỉ ra là slide để trống. Nghĩa là 
 mô hình này vẫn lạc quan hơn thực tế.
- Giới hạn ④: chất lượng model coi như cố định suốt 24 tháng. Thực tế nó trôi 
 (drift) theo dữ liệu và theo thay đổi chính sách, nên chi phí Operate có xu hướng tăng 
 dần chứ không phẳng.

---

<!-- chiron-source-span: {"source_span_id":"a0fb9fbb-fa99-589a-afa4-f7749e4e9600","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Nói ROI với người ký duyệt","source_file":"day-06.html"},"checksum":"8e7cf43a5f76b272ce0e00b10f2b596420c3bfcc9f253fd007369036e20a4b4f"} -->

## 07 Nói ROI với người ký duyệt

Slide 25 đưa một cấu trúc bốn bước để nói chuyện với CFO, và yêu cầu nêu "các giả 
 định nhạy cảm nhất". Chương này tính ra *chính xác* giả định nào nhạy cảm nhất — và câu trả lời 
 không phải cái mọi người nghĩ.

### Slide 25 Cấu trúc bốn bước — và bốn giả định slide gọi tên

> Trích slide 
>  "Tránh nói chung chung như 'AI sẽ giúp hiệu quả hơn'." 
>  "Nói bằng cấu trúc: baseline hôm nay → giả định thay đổi → giá trị 3–6–12 tháng → điều 
>  kiện để giá trị xảy ra." 
>  "Luôn nêu rõ các giả định nhạy cảm nhất: adoption rate, review cost, API cost, error 
>  handling cost."

Bốn bước của cấu trúc đều cần thiết, nhưng bước **①** và bước **④** là hai 
 bước hay bị bỏ nhất — và chúng là hai bước quyết định độ tin cậy của cả bài trình bày:

| Bước | Dạng câu đúng | Bỏ nó thì nghe thành |
| --- | --- | --- |
| ① Baseline hôm nay | "8 nhân viên HR xử lý 4.000 câu hỏi/tháng, trung vị 12 phút/câu — đo trong 2 tuần tháng 2" | Toàn bộ phần sau treo lơ lửng: tiết kiệm 70% của cái gì? |
| ② Giả định thay đổi | "Trợ lý xử lý được 60% số câu, giảm 70% thời gian cho phần đó" | Nghe như lời hứa thay vì giả định — và lời hứa thì không phản biện được |
| ③ Giá trị 3–6–12 tháng | Ba mốc, ba kịch bản — chín con số, kèm điểm hoà vốn | Một con số duy nhất, và người nghe không biết nó nằm ở đâu trong dải khả dĩ |
| ④ Điều kiện để giá trị xảy ra | "Cần: 8 người được đào tạo trong tuần 1 · kho 42 tài liệu được cập nhật · một người sở hữu 
 chất lượng nội dung" | Nguy hiểm nhất. Giá trị được cam kết mà không ai cam kết điều kiện — rồi sáu 
 tháng sau, dự án bị coi là thất bại |

adoption rate · review cost · API cost · error handling cost

adoption rate

mô-đun ngay dưới đây

năm giả định nhạy cảm nhất trong chín giả định của mô hình đều nằm ở phía giá trị

API cost

cuối bảng

① "Giờ tiết kiệm được thì đi đâu?"

không

Chọn trước một trong ba, và nói ra.

② "Nếu tôi cắt một nửa ngân sách thì sao?"

không

③ "Ai chịu trách nhiệm nếu nó không xảy ra?"

#### Tương tác Hai giả định nhạy cảm nhất — bài tập slide 34, tính ra bằng số

Bài tập về nhà ở [slide 34](#s34) viết: *"rà lại pitch deck và chỉ ra 2 
 giả định ROI nhạy cảm nhất."* Đây là cách trả lời nó mà không phải đoán: lay từng giả định 
 ±25%, tính lại lãi ròng 12 tháng, rồi xếp hạng. Mô-đun đọc **đúng bộ tham số bạn đang đặt ở [mô-đun ROI](#m-roi)** phía trên — đổi ở trên thì bảng dưới đổi theo.

Chín giả định, lay mỗi cái ±25%, giữ nguyên tám cái còn lại. Slide 25 gợi ý bốn cái đáng lo: *adoption rate, review cost, API cost, error handling cost*.

Đoán trước: hai giả định nào lay mạnh nhất? Và *API cost* — dòng chi mà mọi cuộc họp về AI 
 đều dành nhiều thời gian nhất — xếp thứ mấy trong chín?

#### Kéo rồi mở

**Hai giả định mạnh nhất là "phút xử lý thủ công mỗi truy vấn" và "% thời gian AI tiết 
 kiệm được"**, hai cái này *đồng hạng chính xác* — chúng nhân vào cùng một chỗ trong công thức giá trị, nên thứ tự giữa chúng trên thẻ là tuỳ ý. Mỗi cái lay lãi ròng 12 tháng một khoảng **277,2 triệu** — từ **−51,5 triệu** tới **+225,7 triệu**. Cả hai *đủ để đổi dấu lãi 
 thành lỗ*. Cả hai đều nằm ở phía **giá trị**, không phải chi phí.

**API cost xếp thứ chín trên chín** — cuối bảng. Nó lay lãi ròng đúng **11,9 triệu**. Tỉ lệ giữa giả định mạnh nhất và yếu nhất là **23,3×**. 
 Nói cách khác: một team dành hai tuần tối ưu chi phí token và không dành một buổi nào đi đo 
 xem công việc hiện tại thật sự mất bao lâu, đang tối ưu vào biến số ít quan trọng hơn **hai mươi ba lần**.

**Năm giả định đầu bảng đều ở phía giá trị:** phút xử lý ·% tiết kiệm · chi phí 
 lao động · trần adoption · số truy vấn. Bốn giả định cuối bảng đều ở phía chi phí. Đây không phải 
 sự trùng hợp — nó là hệ quả cấu trúc: *chi phí bị chặn trên bởi những gì bạn quyết định chi, 
 còn giá trị thì không bị chặn và phụ thuộc vào thế giới bên ngoài.*

**Vì sao "chi phí lao động/giờ" (252,4 triệu) hơi thấp hơn hai cái đầu (277,2 triệu)** dù cả ba đều nhân vào giá trị? Vì nó xuất hiện ở *cả hai vế*: lương cao hơn làm giá trị tiết 
 kiệm tăng, nhưng cũng làm chi phí human review tăng. Hai tác động ngược chiều, và tác động thứ 
 hai ăn mất khoảng 9% của tác động thứ nhất.

*Bài học vận hành:* hai giả định đầu bảng đều là những thứ bạn **đo được trong một 
 tuần** — bấm giờ vài chục ca thật, và làm một Wizard of Oz để xem AI thật sự cắt được bao 
 nhiêu. Đó là hành động rẻ nhất có tác động lớn nhất lên độ tin cậy của cả mô hình. Chín giả định, 
 và bạn chỉ cần đi đo hai.

- **Control - Biên độ lay mỗi giả định: ±25%**: min `5`, max `60`, step `5`, default `25`

Lãi ròng 12 tháng (cơ sở)

—

—

Giả định nhạy cảm nhất

—

—

Nhạy cảm thứ hai

—

—

Mạnh nhất / yếu nhất

—

—

hai giả định nhạy cảm nhất đủ sức đổi dấu lãi/lỗ còn lại

#### Xem bảng: chín giả định, khoảng lãi ròng của từng cái



#### Công thức & giới hạn của mô hình

- Đây là phân tích độ nhạy một chiều (one-at-a-time): mỗi lần chỉ đổi một tham 
 số, giữ nguyên tám tham số kia, ở kịch bản Realistic. Đồ thị cột xếp giảm dần theo độ rộng — đó là 
 dạng "tornado chart" viết theo chiều dọc.
- độ rộng = |lãi ròng 12 tháng khi tham số ×(1+s) − khi ×(1−s)|.
- Giới hạn ①: phân tích một chiều không thấy tương tác. Trong thực tế 
 adoption thấp thường đi cùng review cao và% tiết kiệm thấp; ba cái lệch cùng lúc gây tác động lớn 
 hơn tổng ba tác động riêng lẻ. Đó chính là điều kịch bản Conservative ở 
 mô-đun ROI mô phỏng, và vì thế hai công cụ bổ sung cho nhau chứ không thay 
 nhau.
- Giới hạn ②: lay đều ±25% cho mọi tham số là giả định rằng mọi tham số đều 
 không chắc như nhau. Không đúng: số truy vấn/tháng bạn có thể biết khá chắc từ log, còn 
 "% thời gian AI tiết kiệm được" thì gần như thuần đoán. Bản chuẩn xác hơn sẽ lay mỗi tham số theo 
 độ bất định riêng của nó — nhưng để làm thế, bạn phải viết ra độ bất định đó, và việc viết ra 
 mới là phần có giá trị.
- Giới hạn ③: đo tác động lên lãi ròng 12 tháng. Xếp hạng có thể đổi nếu đo 
 trên chân trời 24 tháng — chi phí build là một lần nên ảnh hưởng của nó loãng dần theo thời gian, 
 còn các dòng theo lượng dùng thì không.

### Slide 27 Technical deck và executive deck — cùng sản phẩm, hai bài trình bày

> Trích slide 
>  Technical team — quan tâm chính: architecture, eval, risks, dependencies 
>  · nên nhấn mạnh: scope, flow, Definition of Done 
>  Executive / sponsor — quan tâm chính: ROI, timeline, adoption, risk 
>  exposure · nên nhấn mạnh: business value, scenario, decision ask

Khác biệt thật giữa hai bài không phải "đơn giản hoá cho sếp". Nó là khác biệt về **câu hỏi 
 mà người nghe cần trả lời sau khi bạn nói xong**:

|  | Technical | Executive |
| --- | --- | --- |
| Câu hỏi họ cần trả lời | "Tôi build cái này thế nào, và khi nào coi là xong?" | "Tôi có duyệt không, và tôi đang chịu rủi ro gì?" |
| Đơn vị của bằng chứng | Metric, kiến trúc, phụ thuộc | Tiền, thời gian, và ai chịu trách nhiệm |
| Sự bất định được xử lý thế nào | Liệt kê ra: nêu unknown, nêu spike cần làm | Đóng gói lại: ba kịch bản, kèm điều kiện |
| Lỗi hay gặp | Bỏ qua Definition of Done, chỉ nói kiến trúc | Trình bày kiến trúc cho người không cần biết, rồi hết giờ trước slide decision ask |

slide cuối

"khoan, để làm gì?"

"Xin 3 tuần và 60 triệu để 
 chạy PoC trên 8 nhân viên HR. Nếu time-to-answer giảm dưới 4 phút, tháng 4 xin tiếp 250 triệu để 
 build. Nếu không, dừng."

### Slide 28 Expectation setting — và vì sao đây là việc bảo vệ chính team

> Trích slide 
>  "Cần nói rõ AI làm tốt điều gì, chưa làm tốt điều gì, và cần human review ở đâu." 
>  "Khi stakeholder hiểu sai capability, team sẽ bị áp scope không thực tế." 
>  "Communication tốt giúp giảm kỳ vọng ảo và tăng cơ hội dự án sống sót lâu hơn."

Câu giữa là câu quan trọng nhất, và nó lật ngược một trực giác phổ biến. Nhiều người coi việc nói ra 
 hạn chế của AI là *làm yếu bài trình bày*. Slide nói ngược lại: **không nói ra hạn chế 
 chính là cách team tự nhận một scope không thể đạt.**

| Kỳ vọng sai của stakeholder | Scope không thực tế nó tạo ra | Câu nói lại cho đúng |
| --- | --- | --- |
| "AI trả lời chính xác 100%" | Không ai cấp ngân sách cho fallback, escalation, hay human review — vì lý thuyết là không cần | "Chúng tôi nhắm 85% đúng nguồn. 15% còn lại cần đường thoát, và đường thoát đó là một phần của 
 sản phẩm chứ không phải chắp vá" |
| "Xong rồi thì nó tự chạy" | Không có ngân sách vận hành từ năm thứ hai — trong khi Operate là 30,8% chi phí | "Cần 12 triệu/tháng vận hành và một người sở hữu chất lượng nội dung, liên tục" |
| "Cho nó làm luôn khâu duyệt cho nhanh" | Bỏ human review — mà đó là biện pháp kiểm soát rủi ro duy nhất đang có | "Bỏ được, nhưng phải đổi bằng ngưỡng chất lượng cao hơn nhiều và cơ chế undo. Xem chi phí lỗi" |
| "Con bot của công ty X làm được mà" | So sánh với một sản phẩm khác dữ liệu, khác rủi ro, khác quy mô | "Họ làm trên dữ liệu công khai và sai thì không ai mất tiền. Ta thì khác ở hai điểm đó" |

người dùng

người ký duyệt

Stakeholder overtrust

Stakeholder distrust

cho họ thấy hệ thống sai kiểu gì, trước khi họ tự phát hiện.

slide 20

---

<!-- chiron-source-span: {"source_span_id":"9e348869-96d3-5c7e-a4a8-08cec93cb83f","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Pitch deck 5–7 slide","source_file":"day-06.html"},"checksum":"a797199092d38452026ea9fb1d3e3e9426943cb227db54f6d71138a5bca1c8ba"} -->

## 08 Pitch deck 5–7 slide

Slide 29 liệt kê bảy mục cho một deck "5–7 slide". Bảy mục cho tối đa bảy slide 
 nghĩa là ở bản 5 slide, bạn phải cắt hai. Chương này trả lời câu hỏi slide không hỏi: *cắt cái nào.*

### Slide 29 Bảy mục — nguồn của từng mục, và hai mục cắt được

> Trích slide 
>  " 1. Problem / pain point · 2. Target user và current workflow · 
>  3. Proposed AI solution · 4. Metrics và expected value · 
>  5. ROI / 3-scenario view · 6. Risks + mitigation · 
>  7. Decision ask: go / pilot / no-go"

Điều đầu tiên đáng nhận ra: **không mục nào trong bảy mục này là nội dung mới.** Cả bảy 
 đều là thứ bạn đã có sau Ngày 2, Ngày 5 và Ngày 6 — pitch deck chỉ là việc *sắp xếp lại cho người 
 ký duyệt*. Nếu bạn thấy mình đang *tạo* nội dung khi làm deck, có nghĩa là một artifact 
 trước đó còn thiếu.

Điều thứ hai: bảy mục cho một deck "5–7 slide". Ở bản 5 slide, ba mục là **không được 
 cắt** vì thiếu chúng thì buổi họp không thể ra quyết định:

Mục 1 (Problem)

trước

Mục 4 (Metrics & expected value)

Mục 7 (Decision ask)

slide đầu tiên

Hai mục cắt được:

nó làm được gì

nó được xây thế nào

rút gọn

kể chuyện

7 → 1 → 4 → 5 → 6

người nghe

_Sơ đồ: Bảy mục của pitch deck, nguồn của từng mục, và mục nào cắt được khi rút xuống năm slide - Bảng bảy hàng, mỗi hàng một mục của pitch deck. Mục một là vấn đề và pain point, nguồn từ problem statement của ngày hai và JTBD của ngày năm, không bao giờ cắt. Mục hai là người dùng mục tiêu và quy trình hiện tại, nguồn từ persona và user research của ngày năm, gộp được vào mục một. Mục ba là giải pháp AI đề xuất, nguồn từ PRD và bốn nhánh xử lý của ngày năm, rút thành một đoạn trong mục bốn. Mục bốn là metrics và giá trị kỳ vọng, nguồn từ north star metric của ngày năm và mô hình ROI của ngày sáu, không bao giờ cắt. Mục năm là ROI ba kịch bản, nguồn từ mô hình ROI và bảng độ nhạy của ngày sáu, giữ nhưng có thể gộp vào mục bốn. Mục sáu là rủi ro và biện pháp, nguồn từ risk register năm nhóm của ngày năm, rút gọn còn ba dòng chứ không bỏ. Mục bảy là đề nghị quyết định go, pilot hay no-go, nguồn từ khung go no-go của ngày năm và ngân sách PoC tối đa của ngày sáu, không bao giờ cắt._

Hình 3 — Bảy mục pitch deck, nguồn của từng mục, và cái gì cắt được.

slide 29

nguồn

ở bản 5 slide

---

<!-- chiron-source-span: {"source_span_id":"96515504-f44d-5e7b-a57d-ae8dd6ab4b09","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 Lab 6, assessment và tổng kết","source_file":"day-06.html"},"checksum":"6b23c9ee531f8ddd1b803fcbc7959accd496f3d7dfbc1cc009544ca7b30f234a"} -->

## 09 Lab 6, assessment và tổng kết

Bốn slide cuối. Phần đáng đọc kỹ là tiêu chí chấm — nó nói rõ bài này được đánh giá 
 theo cái gì, và cái đó không phải chất lượng prototype.

### Slide 31–32 Cách chạy Lab 6 và tiêu chí chấm

> Trích slide 
>  " 1. Hoàn thiện PRD final từ Day 05. 2. Lập ROI model 3–6–12 
>  tháng với 3 kịch bản. 3. Chuẩn bị stakeholder deck 5–7 slides. 4. 
>  Rehearsal 5 phút pitch: một người trình bày, một người đóng vai sponsor hỏi lại." 
>  "Lưu ý: Lab này chấm theo mức độ rõ quyết định, rõ giả định, và rõ điều kiện để tiếp tục 
>  đầu tư." 
>  "Assessment: PRD final đủ scope, metrics, risks, go-forward logic · ROI sheet có cost 
>  side, value side, break-even, 3 scenarios · Pitch deck gọn, logic, nói được với stakeholder 
>  không kỹ thuật · 5-min pitch trình bày được decision ask rõ ràng."

Ba chữ "rõ" trong tiêu chí chấm dịch thẳng thành ba câu hỏi kiểm tra bài nộp của chính bạn:

| Tiêu chí | Câu hỏi tự kiểm | Đạt trông như thế nào |
| --- | --- | --- |
| Rõ quyết định | Sau khi nghe xong, người ký duyệt biết chính xác họ đang được hỏi cái gì chưa? | Một câu duy nhất, có số tiền và có thời hạn: "Xin 60 triệu và 3 tuần cho PoC" |
| Rõ giả định | Bảng phân biệt ba kịch bản có tồn tại không, và ai cũng phản biện được từng dòng chứ? | Bảng tham số × kịch bản như ở slide 23, kèm nguồn của mỗi con số: 
 đo được, benchmark, hay đoán |
| Rõ điều kiện tiếp tục | Có câu nào trong bài bắt đầu bằng "nếu không đạt … thì dừng" không? | Ô Next decision của PoC Canvas, viết đủ cả nhánh xấu |

① ROI chỉ có một con số.

② Không có baseline.

③ Không có nhánh no-go.

go-forward logic

④ Deck kỹ thuật đội lốt deck executive.

slide 27

"Một người đóng vai sponsor hỏi lại"

"Con số này ở đâu ra?"

"Giờ tiết kiệm được thì đi đâu?"

slide 25

"Điều gì sẽ khiến em quay lại nói với anh là dự án này không nên tiếp tục?"

Next decision

### Slide 33–35 Tổng kết, bài tập về nhà, và tài liệu tham khảo

> Trích slide 
>  " 1 AI project management hiệu quả là Agile cộng scientific method: thử, 
>  đo, học, rồi mới đầu tư tiếp. 2 MVP first và PoC đúng nghĩa giúp team validate value 
>  trước khi commit quá nhiều thời gian và chi phí. 3 ROI cho AI phải có 
>  số cụ thể, giả định rõ, và timeline rõ; không thể chỉ nói 'AI sẽ tốt hơn'. 4 
>  Stakeholder communication quyết định dự án có được tiếp tục đầu tư hay không, không chỉ chất 
>  lượng prototype." 
>  Tài liệu tham khảo: Stanford HAI — AI Index Report 2025 · McKinsey Global Institute — 
>  The Economic Potential of Generative AI · Dify Docs — Build LLM Apps with Low-code / 
>  No-code

Vế sau của takeaway số 4 là câu thẳng thắn nhất trong cả deck: *"không chỉ chất lượng 
 prototype"*. Nó thừa nhận một điều mà người làm kỹ thuật thường không muốn nghe — **một 
 prototype tốt hơn không tự động thắng một prototype được trình bày tốt hơn.** Đó không phải lời 
 khuyên nên đánh bóng; đó là mô tả về cách tổ chức thật ra quyết định, và biết điều đó là một phần của 
 nghề.

2 giả định ROI nhạy cảm nhất

lời giải tính được

mô-đun độ nhạy

phút xử lý thủ công mỗi truy 
 vấn

% thời gian AI tiết kiệm được

API cost

cuối bảng trong chín giả định

23,3 lần

Stanford HAI · AI Index

đặt bối cảnh

McKinsey · Economic Potential of Generative AI

quy mô nền kinh tế

không

Dify Docs

benchmark ngành dùng để kiểm tra xem con số của bạn có vô lý không; nó 
 không thay được con số của bạn.

---

<!-- chiron-source-span: {"source_span_id":"eec28f6d-716f-5331-8312-9b91983006ac","locator":{"kind":"html_section","section_id":"ladder","order":12,"heading":"▤ Luyện kỹ năng cốt lõi: biến một câu định tính thành một quyết định có số","source_file":"day-06.html"},"checksum":"0c2d04cae1023b9d6a2f67ecebb60a0e2fe7f5ee390cdc38519014b3b9d48f5c"} -->

## ▤ Luyện kỹ năng cốt lõi: biến một câu định tính thành một quyết định có số

Ba bài giảm dần giàn giáo. Kỹ năng được luyện là kỹ năng bị chấm trong Lab 6: *rõ quyết định · rõ giả định · rõ điều kiện tiếp tục*.

Hôm nay [ai] làm [việc gì], [bao nhiêu lần/tháng], mất [bao lâu mỗi lần] — đo bằng [cách nào]. 
 Nếu [thay đổi gì] thì [chỉ số nào] đi từ [X] xuống [Y]. Giá trị 3–6–12 tháng là [ba con số], hoà vốn 
 ở [tháng nào], dưới kịch bản [nào]. Điều đó chỉ xảy ra nếu [điều kiện 1, 2, 3] — và [ai] chịu trách 
 nhiệm cho từng điều kiện.

đo bằng cách nào

dưới kịch bản nào

ai chịu trách nhiệm

#### Một trưởng phòng nói trong cuộc họp: 
 "Làm con AI trả lời khách hàng đi, chắc chắn tiết kiệm được khối tiền." Biến câu đó thành một 
 đề nghị mà CFO có thể duyệt hoặc từ chối

Đọc cách *lập luận*, không chỉ đáp án.

1. Đừng đi tìm số ngay — trước hết hỏi câu này thuộc loại nào. Câu của trưởng 
 phòng chứa một giả định về value ("tiết kiệm được khối tiền") nhưng chưa có giả định nào về 
 feasibility. Theo slide 12, giả định value được kiểm rẻ nhất bằng 
 MVE, không phải bằng PoC và cũng không phải bằng cách build. 
 Nhưng ở đây có một điều kiện tiên quyết còn thiếu: chưa ai biết hôm nay tốn bao nhiêu. 
 Không có baseline thì cả MVE lẫn PoC đều không phán quyết được điều gì. Nên bước một không phải xây 
 gì cả — mà là đo.
2. Đo baseline, và đo bốn số chứ không phải một. Đây chính là bốn số mà 
 Wizard of Oz sinh ra: 
 ① bao nhiêu ca/tháng → lấy từ log hệ thống ticket, 3 tháng gần nhất, dùng trung vị chứ 
 không dùng trung bình (một tháng khuyến mãi sẽ kéo lệch); 
 ② mất bao lâu mỗi ca → bấm giờ 40 ca thật trong 2 tuần, ghi cả trung vị lẫn phân vị 90; 
 ③ bao nhiêu phần trăm là ca lặp lại → phân loại tay 100 ca gần nhất; 
 ④ chi phí lao động thật mỗi giờ → lấy từ nhân sự, gồm cả phụ cấp và chi phí gián tiếp, 
 không phải chỉ lương gộp chia giờ. 
 Tại sao bốn số này trước mọi thứ khác: vì 
 mô-đun độ nhạy cho thấy ba trong bốn số đó nằm trong nhóm năm giả định mạnh 
 nhất của toàn bộ mô hình. Một tuần đi đo có tác động lớn hơn một tháng tối ưu prompt.
3. Viết giả định thay đổi ra thành hai con số riêng, không phải một. "Tiết kiệm 
 được khối tiền" gộp hai thứ khác nhau: bao nhiêu phần trăm số ca AI xử lý được (trần 
 adoption) và trong số đó tiết kiệm được bao nhiêu phần trăm thời gian. Chúng độc lập với 
 nhau và hỏng theo hai cách khác nhau — AI có thể xử lý 90% số ca nhưng chỉ tiết kiệm 20% thời gian 
 vì người ta vẫn phải đọc lại toàn bộ. 
 Giả sử sau khi đo được: 4.000 ca/tháng · 12 phút/ca · 150 nghìn đ/giờ. Đặt giả định: trần 
 adoption 60%, tiết kiệm 70% thời gian cho phần đó.
4. Chạy ba kịch bản, và báo cáo dải chứ không báo cáo điểm. Với chi phí build 250 
 triệu, API 900 đ/ca, 25% cần người kiểm, vận hành 12 triệu/tháng — 
 mô hình cho: 
 Realistic: hoà vốn tháng 10, ROI 12 tháng 
 +18,6%, lãi ròng 24 tháng 468,0 triệu. 
 Optimistic: hoà vốn tháng 5, ROI 12 tháng +96,2%. 
 Conservative: không hoà vốn trong 24 tháng, ROI 12 tháng −57,2%. 
 Và nói ra dòng quan trọng nhất: "khoảng ROI 12 tháng đi từ −57% tới +96%. Con số đó rộng vì 
 chúng ta chưa đo hai giả định lớn nhất."
5. Chuyển từ báo cáo sang đề nghị — và đề nghị phải là cái rẻ nhất. Với dải rộng 
 như trên, đề nghị đúng không phải "duyệt 250 triệu để build". Nó là: 
 ĐỀ NGHỊ: 3 tuần, 60 triệu, PoC trên 1 nhóm 8 người. 
 Mục tiêu duy nhất: đo hai giả định lớn nhất trên dữ liệu thật. 
 Đạt (time-to-answer <= 4 phút VÀ citation accuracy >= 85%) 
 -> tháng sau xin 250 triệu để build 
 Không đạt time-to-answer -> DỪNG, giả định giá trị sai 
 Không đạt citation -> PILOT 6 tuần, chỉ làm chất lượng nguồn 
 Vì sao 60 triệu là con số hợp lý: theo 
 mô-đun PoC, với mức tin tưởng ban đầu 50% và dải giá trị/thiệt hại như trên, 
 ngân sách PoC tối đa còn đáng chi là 80,0 triệu. Chi 60 thì còn lãi kỳ vọng 20 
 triệu. Chi 150 triệu cho một PoC "cho chắc" thì đã lỗ ngay từ trước khi bắt đầu — và đó là một cách 
 lỗ mà không bảng tính nào của tổ chức phát hiện ra.

#### Sau 3 tuần PoC, kết quả về: 
 time-to-answer trung vị giảm từ 12 xuống 5,5 phút (mục tiêu là ≤ 4), citation accuracy 
 88% (mục tiêu ≥ 85%), tỉ lệ bot từ chối trả lời 31% (mục tiêu ≤ 25%). 
 Bạn nói gì trong buổi review?

Gợi ý có sẵn ở mỗi bước; hãy tự viết câu trả lời trước khi đọc.

1. Phán quyết theo tiêu chí đã chốt là gì? Gợi ý: đọc lại ô 
 Next decision trong PoC Canvas. Ba mục tiêu, đạt mấy? Và cái hụt có phải cái 
 được ghi là "dừng" không?
2. 5,5 phút so với 12 phút — có phải là thất bại không? 
 Gợi ý: chạy lại mô hình ROI với% thời gian tiết kiệm = 54% thay vì 70% 
 (5,5/12 nghĩa là tiết kiệm 54%). Điểm hoà vốn dời đi đâu? Lãi ròng khi bão hoà còn dương không?
3. Tỉ lệ từ chối 31% nói lên điều gì — về AI hay về cái khác? 
 Gợi ý: bot từ chối vì không tìm được nguồn đạt ngưỡng. Đó là lỗi của model, hay là phát hiện về 
 kho tài liệu? Xem nhánh thứ tư trong ví dụ PoC Canvas.
4. Bạn đề nghị gì — và giữ đúng kỷ luật của tiêu chí đã hứa? 
 Gợi ý: đừng diễn giải lại tiêu chí sau khi thấy kết quả (xem slide 14 ). Nhưng 
 "không đạt" cũng không tự động bằng "no-go" — có nhánh thứ ba, và nó tên là gì?
5. Điều gì đã học được, viết thành một câu có thể sai? 
 Gợi ý: mẫu ở slide 8 — "giả định X đã bị bác bỏ vì [số liệu]; nên [hành 
 động]".

#### Đối chiếu sau khi đã tự viết

**① Phán quyết:** đạt 1/3. Citation đạt; time-to-answer và tỉ lệ từ chối đều hụt. 
 Theo ô *Next decision* đã chốt trước: hụt time-to-answer → **NO-GO**, và tỉ lệ 
 từ chối 31% nằm giữa 25% và 40% nên chưa kích hoạt nhánh "đổi bài toán". Đây là kết quả xấu, và 
 việc đầu tiên phải làm là *nói ra như thế*, không phải tìm góc nhìn tích cực.

**② Nhưng 5,5 phút không phải con số vô giá trị.** Tiết kiệm 54% thay vì 70%: chạy 
 lại mô hình với D = 54% cho lãi ròng khi bão hoà khoảng **21 triệu/tháng** thay vì 31,7 
 — vẫn dương, và điểm hoà vốn dời từ tháng 10 ra khoảng tháng 13–14. Dự án vẫn có lãi, chỉ là chậm 
 hơn và mỏng hơn nhiều. 
 *Đây là chỗ dễ mắc lỗi nhất:* hai câu trên đều đúng cùng lúc. Tiêu chí đã hứa nói dừng; 
 kinh tế học nói vẫn có lãi. Cách xử lý trung thực là **trình bày cả hai và để người ký duyệt 
 quyết**, kèm câu: *"chúng ta đã hứa ngưỡng 4 phút và không đạt. Tôi không đề nghị hạ ngưỡng 
 sau khi biết kết quả. Nhưng đây là con số nếu các anh muốn cân nhắc lại ngưỡng — quyết định đó là của 
 các anh, không phải của tôi."* Nói thế giữ được cả tính kỷ luật lẫn tính hữu ích.

**③ Tỉ lệ từ chối 31% là phát hiện về kho tài liệu, không phải về model.** Bot từ 
 chối khi không có nguồn nào đạt ngưỡng — nghĩa là gần một phần ba câu hỏi thật *không có câu trả 
 lời trong 42 văn bản*. Không có mức cải thiện model nào sửa được điều đó. 
 Và đây là kết quả **giá trị nhất** của cả PoC, dù nó không nằm trong mục tiêu nào: 
 bạn vừa phát hiện ra tổ chức thiếu tài liệu cho một phần ba nhu cầu tra cứu — một vấn đề tồn tại từ 
 trước, không liên quan gì tới AI, và giờ mới lần đầu được đo.

**④ Đề nghị: PILOT, không phải go cũng không phải no-go.** Cụ thể: 6 tuần, ngân sách 
 hẹp, *không thêm scope*, mục tiêu duy nhất là bổ sung tài liệu cho nhóm câu hỏi bị từ chối 
 nhiều nhất rồi đo lại. Lý do: hai trong ba chỉ số hụt đều có nguyên nhân chung là độ phủ của kho tài 
 liệu (thiếu nguồn → bot từ chối → người dùng phải tự tra → time-to-answer không giảm được nhiều). 
 Sửa một nguyên nhân có thể cải thiện cả hai chỉ số.

**⑤ Câu học được:** *"Giả định 'kho 42 văn bản phủ được nhu cầu tra cứu chính 
 sách' đã bị bác bỏ — 31% câu hỏi thật không có nguồn nào đạt ngưỡng. Nút thắt là độ phủ nội dung, 
 không phải chất lượng model. Đề nghị pilot 6 tuần chỉ làm nội dung, đo lại cả ba chỉ số."* 
 Câu này có thể sai (có thể sau khi bổ sung tài liệu, time-to-answer vẫn không giảm), nó dựa trên 
 số liệu, và nó dẫn thẳng tới một hành động có timebox. Đủ ba tính chất của một kết quả sprint tốt 
 theo [slide 8](#s8).

#### Lấy sản phẩm của chính bạn ở Lab 5. Viết 
 trọn vẹn: baseline có nguồn · bảng bảy tham số × ba kịch bản · ba con số 3–6–12 tháng · hai giả định 
 nhạy cảm nhất · một decision ask có số tiền và có nhánh dừng

Không có đáp án — nhưng có bảng tự chấm.

nguồn

tham số × kịch bản

không

lãi ròng khi bão hoà

tính ra

nhỏ hơn

số tiền

thời hạn

"nếu không đạt … thì dừng"

điều kiện

"giờ tiết kiệm được thì đi đâu?"

---

<!-- chiron-source-span: {"source_span_id":"f54649f3-9e57-5469-83e7-b4011c5e9e2e","locator":{"kind":"html_section","section_id":"misc","order":13,"heading":"✕ 6 hiểu lầm phổ biến","source_file":"day-06.html"},"checksum":"ef723ca761f8d21ece7a13b446b99471c4392148106542a5a11f390aa4f2a932"} -->

## ✕ 6 hiểu lầm phổ biến

Mỗi ô: điều nhiều người tin → điều slide (hoặc phép tính) thật sự nói → vì sao khác 
 biệt quan trọng. Bốn trong sáu là hiểu lầm về *tiền* — vùng người học AI hay yếu nhất.

"Chi phí lớn nhất của một sản phẩm AI là chi phí gọi model. Tối ưu token là việc quan trọng 
 nhất để dự án có lãi."

mô hình 12 tháng

5,1%

nhỏ nhất trong bốn dòng

human review 10,6% — hơn gấp đôi API

bảng độ nhạy

thứ chín trên chín

23,3 lần

Đây là cách phổ biến nhất để một team kỹ thuật tối ưu chăm chỉ vào đúng biến số ít quan trọng 
 nhất. Hai tuần rút prompt ngắn lại có tác động nhỏ hơn một buổi chiều đi bấm giờ xem công việc hiện 
 tại thật sự mất bao lâu.

"PoC càng kỹ càng tốt. Nếu ngân sách cho phép thì cứ làm rộng ra, thử nhiều thứ cùng lúc, thu 
 được nhiều thông tin hơn."

EVPI

mô-đun PoC

175,0 triệu

80,0 triệu

tệ hơn

đúng 0 đồng

PoC Canvas

"Một PoC luôn là bước đi thận trọng và có trách nhiệm. Chạy PoC trước khi build thì không bao 
 giờ sai."

hai vùng

9,3% – 70,0%

0 đồng

giá trị bằng đúng 
 không

Next decision

PoC Canvas

trước

"Ba kịch bản ROI là để phòng thân: nếu con số realistic không đạt thì vẫn còn conservative để 
 đỡ."

viết ra bảng tham số phân biệt chúng

slide 23

không

−57,2%

+96,2%

"tôi nghĩ adoption chậm hơn ×0,60 nhiều"

"Dự án đang lỗ thì cắt bớt chi phí build là được. Làm gọn lại, dùng công cụ rẻ hơn, thuê ít 
 người hơn."

một lần

không đổi độ dốc

slide 22

lãi ròng mỗi tháng khi bão hoà

4,3 triệu/tháng

thứ tự đọc

trước

"Nói ra hạn chế của AI trước stakeholder làm yếu đề xuất. Nên nhấn mạnh cái nó làm được, phần 
 còn lại tính sau."

Slide 28

team sẽ bị áp scope không thực tế

trust calibration

Ngày 5

trước

---

<!-- chiron-source-span: {"source_span_id":"8210729b-f7af-5ab7-a910-45754d33f9fe","locator":{"kind":"html_section","section_id":"apply","order":14,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"day-06.html"},"checksum":"30439f9c17aa3f1f282bdb65945d6bc77dcae3a3c16570ab88617625bb908119"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI là agent check-in tại kiosk khách sạn, dựng trên LangGraph. Ngày 5 đã 
 cho nó một PRD. Ngày 6 hỏi câu tiếp theo: *nó có đáng tiền không?* Phần này chạy đủ quy trình — 
 và kết quả không phải kết quả dễ chịu.

"AI sẽ giúp check-in hiệu quả hơn"

### ① Baseline — bốn con số, và ghi rõ cái nào là đoán

| Số | Giá trị dùng trong mô hình | Nguồn | Độ tin |
| --- | --- | --- | --- |
| Lượt check-in mỗi tháng | 4.500 | PMS của khách sạn, 3 tháng gần nhất, trung vị | Đo được — số này đáng tin |
| Thời gian lễ tân xử lý mỗi lượt | 6 phút | Bấm giờ 40 lượt trong 2 tuần, trung vị | Đo được — nhưng phân vị 90 là 14 phút, và điều đó quan trọng, xem mục ④ |
| Chi phí lao động lễ tân | 90 nghìn đ/giờ | Nhân sự cung cấp, gồm phụ cấp ca đêm và chi phí gián tiếp | Đo được |
| % lượt kiosk xử lý trọn vẹn (trần adoption) | 55% | Đoán — chưa có kiosk nên chưa có dữ liệu | Giả định — phải ghi rõ là giả định trong mọi slide |
| % thời gian tiết kiệm cho lượt kiosk xử lý | 65% | Đoán | Giả định |

### ② Chạy mô hình — và kết quả nói không

Với build 180 triệu, API 1.200 đ/lượt, 20% lượt cần lễ tân can thiệp, vận hành cố định 9 triệu/tháng 
 (khấu hao phần cứng kiosk + monitoring + bảo trì), [mô hình](#m-roi) cho:

| Kịch bản | Hoà vốn | ROI 12 tháng | Lãi ròng 24 tháng | Lãi ròng/tháng khi bão hoà |
| --- | --- | --- | --- | --- |
| Conservative | không hoà vốn | −83,3% | −424,8 triệu | −8,0 triệu |
| Realistic | không hoà vốn | −53,9% | −182,5 triệu | +0,3 triệu |
| Optimistic | tháng 22 | −24,2% | +17,1 triệu | +7,8 triệu |

+0,3 triệu/tháng

hiểu lầm 5

không mức chi 
 phí build nào cứu được

### ③ Vì sao — kinh tế học của một lượt check-in

```text
MỖI LƯỢT KIOSK XỬ LÝ:
  giá trị   6 phút × 65% × 90.000 đ/giờ  =  5.850 đ
  chi phí   API                          = −1.200 đ
            lễ tân can thiệp 20% × 3 phút = −900 đ
  ----------------------------------------------------
  lãi gộp mỗi lượt                       =  3.750 đ

CHI PHÍ CỐ ĐỊNH:  9.000.000 đ / tháng
ĐIỂM HOÀ VỐN VẬN HÀNH:  9.000.000 / 3.750  =  2.400 lượt/tháng
THỰC TẾ CÓ:             4.500 × 55%        =  2.475 lượt/tháng

BIÊN AN TOÀN: 3%
```

6 phút nhân 90 nghìn đ/giờ là một con số nhỏ

mô-đun ROI

3,3 lần

Đây là bài học tổng quát của Ngày 6:

### ④ Hai giả định nhạy cảm nhất — và một phát hiện về cách định giá trị

Lay từng giả định ±25% ở kịch bản Realistic, xếp theo độ rộng của lãi ròng 12 tháng:

| # | Giả định | Độ rộng | Ghi chú |
| --- | --- | --- | --- |
| 1 | Chi phí build | 90,0 triệu | Đứng đầu chỉ vì lãi vận hành gần bằng 0 — khi không có dòng tiền, mọi thứ còn lại là chi 
 phí chìm |
| 2 | Phút xử lý mỗi lượt /% thời gian tiết kiệm | 79,6 triệu | Đồng hạng — chúng nhân vào cùng một chỗ trong công thức |
| 4 | Chi phí lao động/giờ | 67,4 triệu |  |
| 5 | Vận hành cố định | 54,0 triệu | Cao bất thường so với ví dụ trợ lý chính sách — dấu hiệu của một mô hình mỏng biên |
| 8 | API cost | 16,3 triệu | Vẫn gần cuối bảng, dù ở đây nó chiếm 9,5% chi phí |
| 9 | Tỉ lệ lễ tân can thiệp | 12,3 triệu | Cuối bảng |

phút lễ tân tiết kiệm được, tính theo trung vị

phân vị 90 là 14 phút

không phải

① Năng lực giờ cao điểm.

không phải 
 tuyển thêm người cho ba tiếng mỗi ngày

lớn hơn toàn bộ lãi gộp hiện tại

② Thời gian xếp hàng của khách.

③ Ca đêm.

Hệ quả:

problem statement

Ngày 5

### ⑤ Điều gì làm mô hình đảo chiều — chạy thử ở quy mô chuỗi

Chi phí cố định 9 triệu/tháng là thứ ăn hết biên. Cách khác để xử lý nó là chia nó cho nhiều hơn một 
 khách sạn. Chạy lại với 6 cơ sở (27.000 lượt/tháng), build 320 triệu dùng chung, vận hành 24 triệu/tháng:

| Kịch bản | Hoà vốn | ROI 12 tháng | Lãi ròng 24 tháng | Lãi ròng/tháng khi bão hoà |
| --- | --- | --- | --- | --- |
| Conservative | không hoà vốn | −59,8% | −734,9 triệu | −12,2 triệu |
| Realistic | tháng 12 | +0,5% | +384,8 triệu | +31,7 triệu |
| Optimistic | tháng 5 | +62,0% | +1,43 tỷ | +73,8 triệu |

Ở quy mô chuỗi, mô hình chuyển từ "không hoà vốn" sang "hoà vốn tháng 12". Nhưng hãy đọc dòng 
 Conservative: **vẫn âm 12,2 triệu/tháng**. Quy mô sửa được vấn đề chi phí cố định; nó *không* sửa được rủi ro adoption. Nếu chỉ 33% khách chịu dùng kiosk thay vì 55%, chuỗi 6 cơ sở 
 vẫn lỗ.

### ⑥ PoC Canvas — và ngân sách tối đa cho nó

```text
KEY HYPOTHESIS
  "Ở giờ cao điểm 15:00-18:00, kiosk xử lý trọn vẹn >= 55% lượt check-in
   mà không cần lễ tân can thiệp, và giảm thời gian xếp hàng trung vị
   từ 9 phút xuống dưới 4 phút."
  -> đổi trục giá trị từ 'tiết kiệm lương' sang 'năng lực giờ cao điểm'

SCOPE
  1 khách sạn · 1 khung giờ (15:00-18:00) · khách lẻ đã đặt trước, không đoàn

SUCCESS CRITERIA   (chốt với GM + kế toán trưởng trước ngày bắt đầu)
  - tỉ lệ hoàn tất không cần lễ tân   >= 55%
  - thời gian xếp hàng trung vị        <  4 phút   (baseline đo trước: 9 phút)
  - không có sự cố nào lộ dữ liệu khách sang màn hình người kế tiếp

TIMEBOX
  4 tuần · 1 kiosk · trần ngân sách 35 triệu
  tuần 1 CHỈ đo baseline, chưa bật kiosk

NEXT DECISION
  đạt cả 3          -> xin build cho 6 cơ sở (mô hình chuỗi ở mục ⑤)
  hoàn tất < 40%    -> NO-GO: giả định adoption sai, và quy mô không cứu được
  hoàn tất 40-55%   -> PILOT: 6 tuần, chỉ làm luồng hỏng nhiều nhất
  lộ dữ liệu        -> DỪNG NGAY, bất kể hai chỉ số kia
```

45%

400 triệu

150 triệu

Mô-đun

39,0 triệu

47,3%

35 < 39 — nên chạy, nhưng biên rất mỏng.

giá trị của thông tin

27,3%

### ⑦ Decision ask — một câu, có số, có nhánh dừng

không

35 triệu và 4 tuần

năng lực giờ cao 
 điểm

320 triệu

6 cơ sở

chúng tôi sẽ đề nghị dừng

rõ quyết định, rõ giả định, rõ điều kiện tiếp tục

Lab 6

từ chối chính đề xuất ban đầu của mình

---

<!-- chiron-source-span: {"source_span_id":"410cfe66-f3f4-5eff-87f1-0f3ee97702a5","locator":{"kind":"html_section","section_id":"numbers","order":15,"heading":"# Con số cần kiểm chứng","source_file":"day-06.html"},"checksum":"38377cd3f8ef3ee11cf83e4fe882794f74cb60ec378f056bb8d9c5a09a333b78"} -->

## # Con số cần kiểm chứng

Ranh giới giữa *số của slide* và *số của tài liệu này* — và ở bài Ngày 6, 
 ranh giới đó đặc biệt rõ.

"2 tuần"

"20 câu hỏi lặp lại"

"2–4 tuần"

"3–6–12 tháng"

"5–7 slides"

"5 phút"

Nghĩa là: mọi con số tiền trong tài liệu này đều đến từ tài liệu này, không đến từ 
 slide.

cấu trúc

con số

| Con số | Nguồn | Cần kiểm gì trước khi dùng |
| --- | --- | --- |
| 4.000 truy vấn/tháng · 12 phút/truy vấn · 150 nghìn đ/giờ · 70% tiết kiệm · trần adoption 60% 
 · build 250 triệu · API 900 đ · 25% review · vận hành 12 triệu/tháng | Giả định của tài liệu này cho ví dụ trợ lý chính sách. Không có trong slide | Toàn bộ là tham số minh hoạ. Dùng số của tổ chức bạn; con số ở đây chỉ để bạn thấy 
 hình dạng của kết quả |
| Hoà vốn tháng 10 · ROI 12 tháng +18,6% · lãi ròng 24 tháng 468,0 triệu · lãi bão hoà 31,7 
 triệu/tháng | Tính ra từ các giả định trên | Đúng theo công thức đã ghi ở phần "Công thức & giới hạn". Không chiết khấu dòng tiền |
| Cơ cấu chi phí 12 tháng: build 53,5% · vận hành 30,8% · human review 10,6% · API 
 5,1% | Tính ra | Tỉ lệ này rất nhạy với chi phí build và với API cost. Ở sản phẩm dùng model đắt hoặc lượng truy 
 vấn rất lớn, API có thể lên trên 20% — xem chính mục 
 SmartCheck, nơi nó là 9,5% |
| ROI 12 tháng đi từ −57,2% (Conservative) tới +96,2% (Optimistic) | Tính ra, với bảy hệ số kịch bản ghi ở slide 23 | Bảy hệ số đó (×0,60 · ×0,80 · ×1,30 …) là lựa chọn của tài liệu này. Đổi chúng thì dải 
 đổi. Điều không đổi là hình dạng: dải rộng vì các giả định xấu tương quan dương |
| Độ nhạy: hai giả định mạnh nhất lay 277,2 triệu; API cost lay 11,9 triệu; tỉ lệ 23,3× | Tính ra, lay ±25% một chiều | Xếp hạng phụ thuộc vào bộ tham số cơ sở. Nhưng kết luận cấu trúc — năm giả định đầu bảng 
 đều ở phía giá trị — bền vững với mọi bộ tham số hợp lý, vì chi phí bị chặn trên còn giá trị thì 
 không |
| PoC: ngân sách tối đa 80,0 triệu · EVPI 175,0 triệu · xoá 45,7% bất định | Tính ra từ p = 50%, V = 800 triệu, L = 350 triệu, Se = 85%, Sp = 80% — tất cả 
 là giả định của tài liệu này | V và L là hai con số bạn cũng đang đoán. Mô-đun không nhằm cho ra con số chính xác mà cho thấy 
 hình dạng: bằng 0 ở hai đầu, đỉnh ở giữa |
| Cửa sổ PoC có giá trị: p ∈ (9,3%; 70,0%) · đỉnh 158,3 triệu tại p = 30,4% | Tính ra, có dạng đóng: đỉnh nằm đúng tại p* = L/(V+L) | Hai mép cửa sổ phụ thuộc Se và Sp. Kết luận "có hai vùng vô giá trị ở hai đầu" thì đúng 
 với mọi Se, Sp < 100% |
| PoC 70%/65% → ngân sách tối đa đúng 0 đồng | Tính ra | Kiểm được bằng tay: ở chất lượng đó, hậu nghiệm sau kết quả xấu là 31,6% — vẫn trên ngưỡng 
 27,3%…30,4% — nên bạn build dù kết quả thế nào |
| SmartCheck: lãi gộp 3.750 đ/lượt · hoà vốn vận hành 2.400 lượt/tháng · thực tế 2.475 lượt · 
 biên an toàn 3% | Tính ra từ baseline giả định cho SmartCheck | Ba trong năm số baseline được đánh dấu "đo được" chỉ là mô tả cách nên đo — chưa ai đo 
 thật. Trước khi dùng kết luận này, hãy đo thật |
| SmartCheck chuỗi 6 cơ sở: hoà vốn tháng 12 · Conservative vẫn −12,2 triệu/tháng | Tính ra | Giả định chi phí build 320 triệu dùng chung và vận hành 24 triệu/tháng cho cả 6 cơ sở. Nếu mỗi cơ 
 sở cần phần cứng riêng thì vận hành tăng gần tuyến tính và kết luận đảo ngược |
| "2 tuần · 20 câu hỏi lặp lại" · "2–4 tuần" · "3–6–12 tháng" · "5–7 slides" · "5 phút" | Của slide (14, 19, 4/25, 5/29, 5/31) | Đây là toàn bộ con số có thật trong deck. Chúng là gợi ý về độ lớn, không phải chuẩn 
 mực |

"23 / 25"

thứ tự trang PDF

---

<!-- chiron-source-span: {"source_span_id":"9da5fd37-7ed8-5f60-8f1f-f43d1bd8c6d8","locator":{"kind":"html_section","section_id":"cheat","order":16,"heading":"▣ Cheat sheet ôn thi","source_file":"day-06.html"},"checksum":"7cd8b974d858c6d72afe7907b2bf4bd289cb12469369c328ce7d3ba6e8b3f20d"} -->

## ▣ Cheat sheet ôn thi

Những thứ nên nhớ được mà không cần mở lại tài liệu.

| Danh sách | Các mục | Slide |
| --- | --- | --- |
| AI Sprint Model (5 ô + 3 lối ra) | Research Spike → Hypothesis → Build → Eval → Quyết định; ba lối ra: 
 Iterate · Scale · Kill | 8 (+ Hình 1 ) |
| Ba câu hỏi mỗi sprint | Đã học được gì · Giả định nào bị bác bỏ · Tiếp tục đầu tư hay dừng ở đâu | 8 |
| Definition of Done cho AI (4) | Quality threshold · Latency · Fallback · Monitoring signal | 10 |
| Ba loại nợ | Feature debt · Data debt · Technical debt | 10 |
| MVE · MVP · PoC | Có ai muốn không · Workflow chạy được không · Có đáng đầu tư thêm không | 12 |
| Timebox 4 ô | Giả định · Thời hạn · Budget ceiling · Tiêu chí dừng | 14 |
| PoC Canvas 5 ô | Key hypothesis · Scope · Success criteria · Timebox · Next decision | 19 |
| Cost / value anatomy 4 hàng | Build · Run · Operate · Business impact | 22 (+ Hình 2 ) |
| Ba kịch bản | Conservative · Realistic · Optimistic | 23 |
| Bốn bước nói ROI | Baseline hôm nay → Giả định thay đổi → Giá trị 3–6–12 tháng → Điều kiện để giá trị xảy ra | 25 |
| Pitch deck 7 mục | Problem · Target user · Solution · Metrics · ROI 3 kịch bản · Risks · Decision ask | 29 (+ Hình 3 ) |

```text
① GIÁ TRỊ MỖI THÁNG
   Q · adoption(m) · (T/60) · D · W
   Q = lượt/tháng · T = phút thủ công · D = % tiết kiệm · W = chi phí lao động/giờ

② HOÀ VỐN VẬN HÀNH  (câu hỏi phải hỏi TRƯỚC điểm hoà vốn)
   lãi gộp mỗi lượt = giá trị/lượt − API/lượt − chi phí review/lượt
   số lượt cần      = chi phí cố định mỗi tháng / lãi gộp mỗi lượt
   -> lãi gộp <= 0  =>  không mức build nào cứu được

③ NGƯỠNG HẬU NGHIỆM ĐỂ BUILD
   p* = L / (V + L)          L = thiệt hại nếu sai · V = giá trị nếu đúng
   -> đỉnh giá trị của PoC nằm đúng tại p = p*

④ GIÁ TRỊ THÔNG TIN CỦA PoC  (= ngân sách tối đa)
   cơ sở  = max(0, p·V − (1−p)·L)
   P(+)   = p·Se + (1−p)(1−Sp) ;  p⁺ = p·Se / P(+)
   VoI    = Σ P(kết quả) · max(0, EV theo hậu nghiệm)  −  cơ sở
   EVPI   = p·V − cơ sở        (trần tuyệt đối)
```

"Stakeholder đổi requirement sau 3 tuần build — làm sao?"

slide 2

"Nên làm MVE, MVP hay PoC?"

ai phải bị thuyết phục

"Ước lượng một AI task thế nào?"

"Chi phí lớn nhất của sản phẩm AI là gì?"

"Khi nào PoC không đáng chạy?"

"Deck cho CFO khác deck cho team ở đâu?"

câu hỏi người nghe phải 
 trả lời sau khi bạn nói xong

① "Giả định nào nhạy cảm nhất trong mô hình ROI?"

năm giả định mạnh nhất đều ở phía giá trị

② "PoC càng kỹ có tốt hơn không?"

③ "Dự án đang lỗ thì cắt chi phí build?"

lãi ròng khi bão hoà

---

<!-- chiron-source-span: {"source_span_id":"f6467c76-5c24-5ad8-a164-7bced8d19749","locator":{"kind":"html_section","section_id":"gloss","order":17,"heading":"☰ Từ điển thuật ngữ","source_file":"day-06.html"},"checksum":"017cc2bed1c942fd717be02229162e2c47c951c29c3d2ef1a650bc650170e705"} -->

## ☰ Từ điển thuật ngữ

Định nghĩa theo cách dùng được trong bài thi và trong công việc, không phải theo 
 cách tra từ điển.

---

<!-- chiron-source-span: {"source_span_id":"4c1c03fc-ff5e-511c-97ab-6e87793a180a","locator":{"kind":"html_section","section_id":"bloom","order":18,"heading":"◉ Bạn đang ở mức nào?","source_file":"day-06.html"},"checksum":"254bd9242a86bd3c74e9a8d0765cf9217c5c76c4931980ea45b4d64a9a2e7071"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab 6 kiểm tra mức 3–4; câu hỏi ở [slide 36](#s36) kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 5 ô sprint model, 4 phần Definition of Done, 3 mức MVE/MVP/PoC, 4 ô timebox, 5 ô PoC 
 Canvas, 4 hàng cost anatomy, 4 bước nói ROI, 7 mục pitch deck. | Cheat sheet · Hình 1 · Hình 3 |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao MVE, MVP và PoC khác nhau ở ai phải bị thuyết 
 phục chứ không ở quy mô; và vì sao "không giảm đáng kể" không phải một tiêu chí dừng. | Slide 12 · slide 14 · hiểu lầm 3 |
| 3 · Áp dụng | Điền trọn năm ô PoC Canvas cho sản phẩm của bạn, có ngưỡng số ở ô Success criteria và 
 đủ cả nhánh xấu ở ô Next decision. Dựng được một mô hình ROI ba kịch bản có bảng tham số. | Slide 19 · Bài 1 · mô-đun ROI |
| 4 · Phân tích | Cho một mô hình ROI, chỉ ra được hai giả định nhạy cảm nhất bằng tính toán chứ không 
 bằng trực giác; và đọc được lãi ròng khi bão hoà trước điểm hoà vốn để biết dự án có cứu được không. | Mô-đun độ nhạy · Bài 2 · hiểu lầm 5 |
| 5 · Đánh giá | Nhìn một đề xuất PoC và nói được nó có đáng chạy không — kể cả khi câu trả lời là "đừng 
 chạy, bạn đã biết câu trả lời rồi". Và biết khi nào một dự án nên bị từ chối bởi chính người đề 
 xuất. | Mô-đun PoC · mục SmartCheck · slide 20 |
| 6 · Sáng tạo | Nhận ra rằng vấn đề không nằm ở mô hình mà ở cách định nghĩa giá trị, rồi viết lại 
 problem statement để mô hình đo đúng thứ đáng đo — như mục ④ của phần SmartCheck. | Mục SmartCheck ④ · Ngày 5 |

①

đo

②

③

slide 36
