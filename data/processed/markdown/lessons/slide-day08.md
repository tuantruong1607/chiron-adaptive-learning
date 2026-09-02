---
schema_version: 1
course_id: rag-intensive
document_id: "86bd4f05-0a33-5cc7-b680-e059ecfd13cf"
document_version_id: "3448476e-bf6f-57fe-b599-c05fbcb67df0"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "RAG Pipeline — Truy xuất & Sinh câu trả lời — phân tích & breakdown từng slide"
source_file: "slide-day08.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-day08.html"
source_sha256: "d2d5d483c7de10d1ced26637903d388ae364358726e0f1792f236df5da8ea988"
parser_version: chiron-structured-markdown-v1
html_section_count: 21
interactive_module_count: 3
interactive_control_count: 14
language: vi
---

# RAG Pipeline — Truy xuất & Sinh câu trả lời — phân tích & breakdown từng slide

> 139 slide, deck dày nhất trong kho. Nó đưa ra một khẳng định định lượng rất mạnh ngay ở 
 slide 18 — "80% lỗi do Retrieval, 20% do Generation" — mà không kèm nguồn nào. Tài 
 liệu này dựng mô hình tối thiểu để kiểm con số đó, và kiểm luôn hai khẳng định định lượng khác 
 của deck: sweet spot top-3 đến top-5 và RRF đưa tài liệu tốt-ở-cả-hai-bảng lên số 1.

<!-- chiron-source-span: {"source_span_id":"e7768c12-feb3-5253-98ba-6f2d67fa43f6","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-day08.html"},"checksum":"666cfd51522a30c796da8603d7a0fbe5ed6cb84a7a6623c13632b972a918811f"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Ngày 8 nối tiếp [Ngày 7](slide-day07.html) đúng ở chỗ Ngày 7 dừng lại. Ngày 7 kết thúc ở *"top-k chunk đã chọn"*; Ngày 8 nhận từ đó và đi tới câu trả lời cuối cùng. Nếu bạn thấy nội dung 
 về parsing, chunking hay vector store ở đây có vẻ quen, đúng là vậy — **chương 03, 04 và 05 của bài 
 này lặp lại phần lớn Ngày 7**, và tài liệu này ghi rõ chỗ nào lặp để bạn khỏi học hai lần.

| Chủ đề | Ngày 7 nói | Ngày 8 thêm gì |
| --- | --- | --- |
| Parsing PDF, bảng biểu | Rất sâu — 11 slide, có số (STC: Recall@1 0,366 → 0,754) | Gần như không thêm gì mới. Lướt nhanh chương 03 |
| Chunking | Thang 5 bậc, paper bác bỏ semantic chunking | Small-to-Big / Parent-Child — kỹ thuật mới, đáng đọc kỹ |
| Dense vs sparse, hybrid, RRF | Có, nhưng ngắn | Alpha tuning, ví dụ theo domain, và bài toán chuẩn hoá điểm — sâu hơn Ngày 7 |
| Rerank | Một slide về bất đối xứng chi phí | Kiến trúc hai giai đoạn, MMR, khi nào dùng cái nào — đây là phần mạnh nhất |
| Context injection, grounding, UX | Không có | Toàn bộ phần 3 là nội dung mới — XML tags, lost-in-the-middle, citation UX |
| Eval | recall@k, eval set không nhãn | RAGAS triad, LLM-as-judge, ma trận chẩn đoán, CI/CD gate |

Nếu thời gian eo hẹp:

09

10

11

12

hầu như không có nguồn

| Khẳng định | Slide | Mô-đun kiểm nó |
| --- | --- | --- |
| "80% lỗi do Retrieval, 20% do Generation" | 18 | Phễu ba tầng — dựng mô hình tối thiểu và tìm xem 
 tỉ lệ nào ở mỗi tầng thì cho ra đúng 80/20 |
| "Sweet spot là top-3 đến top-5" | 73 | k tối ưu — mô hình có cực trị trong, và nó rơi đúng vào khoảng đó |
| "Tài liệu top cao ở CẢ 2 bảng sẽ lên số 1 tuyệt đối" | 66 | RRF so với cộng điểm — dựng ví dụ 8 tài liệu và kiểm |

cả ba khẳng định đều đứng vững

Lượt 1 · ~15 phút

Nắm khung

- Đọc slide 14 — RAG là ba pipeline, không phải một hàm API
- Nhìn Hình 1 — toàn bộ pipeline và chỗ mỗi loại lỗi phát sinh
- Đọc slide 18 — khẳng định 80/20, rồi chạy 
 mô-đun phễu để xem nó có nghĩa gì
- Mục tiêu: nói được vì sao "sửa prompt" là phản xạ sai khi RAG trả lời sai

Lượt 2 · ~70 phút

Chương 09, 10, 11 — phần Ngày 7 không có

- Chương 09: kiến trúc hai giai đoạn, và khi nào MMR thay vì cross-encoder
- Chương 10: chạy mô-đun k — đây là chỗ có kết quả bất ngờ nhất
- Chương 11: grounding prompt và ba lỗi generation — phần này viết được thành checklist

Lượt 3 · ~25 phút

Ôn thi

- 6 hiểu lầm — hai cái đầu là hai phản xạ sai phổ biến nhất khi debug RAG
- 3 bài bậc thang — kỹ năng: đọc bảng điểm để biết sửa ở đâu
- Cheat sheet — ma trận chẩn đoán 2×2 nên thuộc

"Bạn đang thiếu model mạnh hơn, hay đang thiếu một pipeline retrieval và 
 evaluation đủ kỷ luật?"

Ngày 7

"model yếu, hay 
 không có đúng dữ liệu?"

Ngày 6

"quản lý dự án, hay quản 
 lý một tập giả định chưa kiểm chứng?"

vấn đề gần như không bao giờ nằm ở model.

---

<!-- chiron-source-span: {"source_span_id":"44528479-f393-52ea-9198-f13f0773dc5c","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu — đã có vector store, lỗi nằm ở đâu?","source_file":"slide-day08.html"},"checksum":"5b2cdf0813178553621a767866d8bb769dcc121051b172298ee14ddf42fca2f2"} -->

## 00 Mở đầu — đã có vector store, lỗi nằm ở đâu?

Câu hỏi mở bài của Ngày 8 giả định bạn đã làm xong Ngày 7. Nó hỏi tiếp: *vậy tại 
 sao vẫn sai?*

### Slide 2 Câu hỏi mở đầu — và bốn chỗ có thể hỏng

> Trích slide 
>  "HÃY SUY NGHĨ… 'Bạn đã build agent với vector store. Nhưng agent vẫn hallucinate và trả 
>  lời sai. Lỗi nằm ở đâu?' "

Câu này có bốn câu trả lời khả dĩ, và cả bài Ngày 8 là việc phân biệt chúng. Deck trả lời ở [slide 18](#s18) bằng một tỉ lệ (80/20), nhưng bốn khả năng chi tiết hơn thế:

| # | Lỗi ở đâu | Triệu chứng phân biệt | Chương xử lý |
| --- | --- | --- | --- |
| 1 | Chứng cứ không có trong index | Tìm bằng id cũng không thấy chunk chứa đáp án | 03, 04 — parsing, chunking |
| 2 | Có trong index nhưng không lọt top-k | Chunk tồn tại, nhưng retrieval xếp nó hạng 40 | 06, 07, 08 — query transform, hybrid |
| 3 | Lọt top-k nhưng bị chôn giữa context | Chunk đúng nằm trong prompt, model vẫn không dùng | 09, 10 — rerank, lost-in-the-middle |
| 4 | Model đọc được nhưng vẫn bịa | Chunk đúng ở đầu prompt, câu trả lời vẫn thêm chi tiết không có | 11 — grounding prompt, temperature |

print

formatted_context

print

Ngày 7

④

### Slide 4–5 Năm mục tiêu, và deliverable buộc phải có scorecard

> Trích slide 
>  "Giải thích được RAG như một pipeline gồm indexing, retrieval, re-ranking, và 
>  generation · Hiểu vì sao retrieval quality thường quyết định chất lượng câu trả lời 
>  nhiều hơn prompt viết đẹp · So sánh được dense, sparse, hybrid và biết khi nào cần rerank · 
>  Thiết kế được prompt grounding · Đo được chất lượng RAG bằng faithfulness, relevance, context 
>  recall " 
>  Deliverable: "1 pipeline index → retrieve → rerank/select → generate · 1 bộ câu hỏi test 
>  có expected evidence hoặc expected answer · 1 bảng điểm ngắn để so sánh 
>  baseline và bản tuning đầu tiên "

Deliverable thứ ba là deliverable phân biệt. Hai cái đầu chứng minh bạn *chạy được*; cái thứ 
 ba chứng minh bạn **biết bản tuning có thật sự tốt hơn không**.

baseline

đo trước khi sửa

Slide 123

"Chỉ thay đổi MỘT biến số trong mỗi lần 
 thử nghiệm. Nếu bạn vừa đổi kích thước chunk, vừa đổi thuật toán Hybrid, vừa đổi System Prompt → 
 không biết chính xác yếu tố nào mang lại thành công."

Ngày 7 · Bài 2 bậc thang

và

---

<!-- chiron-source-span: {"source_span_id":"2c4426af-4214-5946-97c9-002cb254dfea","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Vì sao RAG — và vì sao không phải fine-tuning","source_file":"slide-day08.html"},"checksum":"d3dbcf7160d2d7f7b815800aa479f5d3f3d062c3526052ec344a8b7a83cd7e94"} -->

## 01 Vì sao RAG — và vì sao không phải fine-tuning

Chương này chứa bảng so sánh RAG với fine-tuning mà mọi người học AI đều nên thuộc, 
 và một luận điểm về lợi thế cạnh tranh mà deck phát biểu rất gọn.

### Slide 8–9 Ba nguồn hallucination, và ba trục so sánh với fine-tuning

> Trích slide 
>  " Kiến thức bị đóng băng — LLM chỉ biết những gì đã xảy ra trước ngày training. 
>  Thông tin nội bộ hay sự kiện mới là điểm mù. · Bản chất xác suất — LLM là cỗ máy dự 
>  đoán từ tiếp theo, ưu tiên sự trôi chảy hơn tính chính xác. · Hệ quả — 
>  Hallucination: khi thiếu dữ kiện, model sẽ tự động 'bịa' ra thông tin trông rất logic và tự 
>  tin." 
>  Fine-tuning — "học phong cách. Phù hợp để thay đổi cách model nói chuyện 
>  (tone, format), nhưng cực kỳ kém và đắt đỏ nếu dùng để nhồi nhét sự kiện. Trí nhớ 
>  mạng nơ-ron rất dễ bị catastrophic forgetting." · RAG — "cung cấp tài liệu… 
>  giống như cho học sinh mang tài liệu vào phòng thi open-book exam thay vì bắt học thuộc 
>  lòng." 
>  Cost to Update: Cao (retraining) vs Thấp (update index) · Risk of 
>  Hallucination: Cao (static knowledge) vs Thấp (grounded) · Dynamic 
>  Access Control: Khó (all-in-one weights) vs Dễ (document-level 
>  permissions)

Hàng thứ ba của bảng — **access control** — là hàng ít được nhắc nhất và là hàng quyết 
 định nhất trong môi trường doanh nghiệp:

trọng số của nó chứa thông tin đó, cho mọi 
 người dùng

WHERE

kiểm toán được

Nhưng — và đây là chỗ Ngày 7 bổ sung một cảnh báo quan trọng:

trước hoặc trong

Ngày 7 · slide 84

RAG cho bạn khả năng phân quyền, nhưng cài đặt sai thì khả 
 năng đó là ảo.

học sinh mở đúng trang

retrieval

rerank

lost-in-the-middle

grounding

tệ hơn

### Slide 10–12 Ba lý do doanh nghiệp bắt buộc dùng RAG, và luận điểm data-centric

> Trích slide 
>  Quy trình ngược: "Thay vì hỏi model ngay lập tức, ta chặn câu hỏi lại → dùng nó 
>  để truy vấn cơ sở dữ liệu → lấy bài viết liên quan nhất → ép model đọc bài viết đó 
>  để trả lời." 
>  " Nguồn gốc rõ ràng (Auditability): mọi câu trả lời đều có thể đính kèm citation. 
>  Nếu AI trả lời sai, ta biết ngay là do tài liệu sai hay do AI suy diễn. · Bảo mật & phân 
>  quyền (RBAC) · Cập nhật real-time (Freshness): chỉ cần xoá file cũ / thêm 
>  file mới. Không cần train lại model." 
>  "Các model đang dần trở thành 'hàng hoá cơ bản' (commodity) với sức mạnh tương 
>  đương nhau. Sự khác biệt của một sản phẩm AI doanh nghiệp nằm ở hệ thống dữ liệu. 
>  Pipeline xử lý, làm sạch và tìm kiếm dữ liệu mới là lợi thế cạnh tranh cốt lõi. ⚠ Your LLM is 
>  only as smart as your retrieval system. "

do tài liệu sai

do AI suy diễn

khả năng chẩn đoán

mở tài liệu được trích ra 
 đọc

lỗi "tài liệu sai" không phải lỗi của team AI.

"sức mạnh tương đương nhau"

năng lực 
 tổng quát

độ dài context, giá, độ trễ, và khả năng bám 
 context

g

mô-đun phễu

đổi model cho bạn vài điểm phần trăm; sửa pipeline dữ liệu 
 cho bạn hàng chục.

---

<!-- chiron-source-span: {"source_span_id":"aec08284-ee87-5e76-8ebb-8f7702f3d098","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Ba pipeline, và nút cổ chai 80/20","source_file":"slide-day08.html"},"checksum":"e66ad03c678d7a1e894ead928c9d6f1d2b94df1a9ffc9dc6aba9c0e90a22fee4"} -->

## 02 Ba pipeline, và nút cổ chai 80/20

Chương ngắn nhưng chứa khẳng định định lượng mạnh nhất của cả deck — và nó không kèm 
 nguồn. Mô-đun cuối chương dựng mô hình để kiểm.

### Slide 14–17 RAG là ba pipeline, không phải một hàm API

> Trích slide 
>  "RAG không phải là một hàm API gọi một lần. Nó là một hệ thống phân tán gồm 3 khối kiến 
>  trúc riêng biệt chạy nối tiếp nhau: 1. Indexing — xử lý và chuẩn hoá tài 
>  liệu (chạy ngầm/offline) · 2. Retrieval — tìm kiếm và chọn lọc ngữ cảnh (real-time 
>  khi user hỏi) · 3. Generation — lắp ghép prompt và sinh ngôn ngữ (real-time)." 
>  Indexing: "quá trình ETL dành cho dữ liệu phi cấu trúc." · Retrieval: "hệ thống 
>  cũng phải mã hoá câu hỏi bằng đúng model đã dùng ở bước Indexing." · Generation: 
>  "LLM đóng vai trò biên tập viên … Nếu DB trả về kết quả rỗng, LLM phải được 
>  lập trình để xin lỗi và báo thiếu dữ liệu. "

Chữ **offline** và **real-time** là chỗ phân chia có hệ quả lớn nhất, và 
 deck không khai thác hết:

|  | Indexing (offline) | Retrieval + Generation (real-time) |
| --- | --- | --- |
| Chạy khi nào | Khi tài liệu thay đổi | Mỗi truy vấn |
| Ràng buộc | Không có SLA — chạy cả đêm cũng được | Người dùng đang ngồi chờ, 3–5 giây (slide 105) |
| Nên đầu tư gì | Chất lượng bằng mọi giá: parser nặng, VLM, LLM tóm 
 tắt bảng, contextual retrieval | Chỉ những gì chạy kịp trong ngân sách độ trễ |
| Chi phí | Trả một lần mỗi tài liệu | Trả lại mỗi truy vấn |

LLM tóm tắt bảng

slide 33

Contextual Retrieval

Parser VLM

slide 23

Query transformation

chương 06

real-time

Rerank

real-time

"việc này làm được lúc index không?"

### Slide 18 "80% lỗi do Retrieval" — khẳng định mạnh nhất, và nó không có nguồn

> Trích slide 
>  "Khi test RAG thấy kết quả sai, kỹ sư thường vội vàng nhảy vào sửa Prompt hoặc đổi model 
>  lớn hơn. Đây là sai lầm! " 
>  80% — Lỗi do Retrieval: "truy vấn tìm sai tài liệu · thiếu chứng cứ quan trọng · 
>  nhồi quá nhiều rác (noise)" 
>  20% — Lỗi do Generation: "model bỏ qua chứng cứ · ảo giác sinh thêm chi tiết · 
>  định dạng sai"

Đây là slide có ảnh hưởng lớn nhất của cả deck — nó định hướng toàn bộ thứ tự ưu tiên khi debug. Và 
 nó **không kèm nguồn, không kèm dataset, không kèm cách đo**.

tin ngay

bác bỏ 
 ngay

bộ tham số nào cho ra 80/20

Mô-đun phễu

80/20 là hợp lý, và nó tương ứng với một hệ thống có recall@50 khoảng 75%, reranker khá tốt, 
 và model bám context 90%.

đã được chăm sóc

tỉ lệ đó dịch chuyển khi bạn cải thiện từng 
 tầng.

"Kỹ sư thường vội vàng nhảy vào sửa Prompt hoặc đổi model lớn hơn. Đây là sai lầm!"

generation bị chặn trên bởi retrieval

slide 116

Context Recall

Ngày 7 · slide 75

"upper-bound cho chất 
 lượng câu trả lời cuối cùng"

Hệ quả thực dụng:

không

print(formatted_context)

_Sơ đồ: Toàn bộ pipeline RAG và bốn chỗ lỗi phát sinh - Trên cùng là ba khối kiến trúc của slide mười bốn: indexing chạy ngầm offline, retrieval và generation chạy thời gian thực. Hàng giữa là năm bước xử lý một truy vấn: biến đổi truy vấn, hybrid search lấy năm mươi ứng viên, rerank xuống ba tới năm chunk, nhồi vào prompt, và sinh câu trả lời. Dưới mỗi bước là loại lỗi phát sinh ở đó: lỗi một là chứng cứ không lọt shortlist, thuộc phía retrieval; lỗi hai là rerank đánh rơi chứng cứ, cũng thuộc phía retrieval; lỗi ba là chứng cứ bị chôn giữa context nên model không dùng; lỗi bốn là model đọc được nhưng vẫn bịa thêm. Slide mười tám gộp lỗi một và hai thành tám mươi phần trăm, lỗi ba và bốn thành hai mươi phần trăm. Dải cuối là quy trình gỡ lỗi của slide một trăm mười một: in biến formatted_context ra, nếu context có chứa đáp án thì lỗi thuộc generation, nếu không thì lỗi thuộc retrieval._

Hình 1 — Pipeline đầy đủ, và bốn chỗ lỗi phát sinh.

slide 82

slide 14

print

slide 18

đặt cả bốn 
 thứ lên cùng một hình

#### Tương tác Phễu ba tầng — con số 80/20 của slide 18 có nghĩa là gì?

Slide 18 nói **80% lỗi do Retrieval, 20% do Generation** mà không kèm 
 nguồn. Mô-đun này dựng mô hình tối thiểu của pipeline rồi hỏi ngược lại: *bộ tham số nào cho ra 
 đúng tỉ lệ đó, và tỉ lệ đó đổi thế nào khi bạn cải thiện từng tầng?*

Mặc định: recall@50 của giai đoạn 1 là **75%** · shortlist **k₁ = 50** · đưa vào prompt **k₂ = 5** · reranker đẩy đúng chứng cứ lên 
 đầu **85%** số lần · model bám context **90%**.

Đoán trước: *(a)* tỉ lệ trả lời đúng end-to-end? *(b)* phần lỗi thuộc phía tìm kiếm 
 là bao nhiêu — có ra 80% không? *(c)* tăng k₁ từ 50 lên 200 thì tốt lên hay xấu đi?

#### Kéo rồi mở

**(a) Chỉ 58,4%.** Bốn mươi hai câu trong một trăm sai — với một cấu hình mà từng 
 tầng nghe đều "khá ổn". Đây là hệ quả của việc *nhân* ba xác suất: 0,75 × 0,865 × 0,90. 
 Không tầng nào tệ, nhưng tích của ba tầng thì tệ.

**(b) 84,4% thuộc phía tìm kiếm, 15,6% thuộc generation.** Rất gần 80/20 của 
 slide 18 — nên con số đó *hợp lý*, không phải bịa. 
 Kéo "kỹ năng reranker" lên **94–95%** thì ra đúng **80/20**. Nghĩa 
 là: con số của slide tương ứng với một hệ thống đã có reranker tốt. Với hệ thống chưa có reranker, 
 tỉ lệ lệch về phía retrieval còn nhiều hơn nữa.

**(c) Xấu đi một chút, và đây là kết quả phản trực giác nhất.** Tăng k₁ từ 50 lên 
 200: tỉ lệ sống sót qua rerank giảm từ 86,5% xuống **85,4%**, độ chính xác end-to-end 
 giảm từ 58,4% xuống 57,6%. 
 Lý do: trong mô hình này, k₁ lớn hơn *không* làm recall@k₁ tăng (bạn phải kéo thanh R1 
 riêng để mô phỏng điều đó) — nó chỉ làm shortlist loãng hơn, nên phần "chọn ngẫu nhiên" của 
 reranker khó trúng hơn. 
 **Bài học thật:** tăng k₁ chỉ đáng khi nó *thật sự* nâng recall@k₁. Nếu 
 recall đã bão hoà ở k₁ = 50 thì tăng lên 200 chỉ tốn tiền rerank mà không được gì — đúng điều [Ngày 7](slide-day07.html) gọi là "tăng nprobe đến khi recall bão hoà rồi dừng".

**Thử điều đáng thử nhất — kéo "model bám context" từ 90% xuống 70%:** phần lỗi 
 generation nhảy từ 15,6% lên **36,3%**, và tỉ lệ 80/20 của slide sụp đổ. 
 Đó chính là điều xảy ra khi bạn dùng model nhỏ ( [slide 110](#s108) nói model 8B hay 
 quên rule) hoặc prompt grounding lỏng. **Con số 80/20 không phải hằng số của RAG — nó là 
 ảnh chụp một hệ thống đã được chăm sóc ở tầng generation.**

*Bài học vận hành:* đừng dùng 80/20 làm lý do bỏ qua generation. Dùng nó theo chiều đúng: **khi chưa biết lỗi ở đâu, đặt cược vào retrieval trước** — nhưng hãy đo, vì `print(formatted_context)` cho bạn câu trả lời thật trong ba giây.

- **Control - Recall@k₁ của giai đoạn 1: 75%**: min `20`, max `99`, step `1`, default `75`

- **Control - k₁ — shortlist đưa qua reranker: 50 chunk**: min `5`, max `200`, step `5`, default `50`

- **Control - k₂ — số chunk vào prompt: 5 chunk**: min `1`, max `30`, step `1`, default `5`

- **Control - Kỹ năng reranker (đẩy chứng cứ lên đầu): 85%**: min `0`, max `100`, step `1`, default `85`

- **Control - Model bám context (không bịa): 90%**: min `40`, max `100`, step `1`, default `90`

Trả lời đúng end-to-end

—

—

Lỗi phía tìm kiếm

—

—

Lỗi phía generation

—

—

Sống sót qua rerank

—

—

trả lời đúng lỗi 1 — không lọt shortlist lỗi 2 — rerank đánh rơi lỗi 3 — model bịa

#### Xem bảng: k₁ đổi thì quy lỗi đổi thế nào



#### Công thức & giới hạn của mô hình

- P(sống sót rerank) = q + (1−q)·k₂/k₁ — với xác suất q reranker đẩy 
 đúng chứng cứ lên đầu; phần còn lại coi như chọn ngẫu nhiên k₂ trong k₁. q = 0 là 
 reranker vô dụng (chọn ngẫu nhiên), q = 1 là reranker hoàn hảo.
- Đúng end-to-end = R1 · P(sống sót) · g. Ba nguồn lỗi cộng lại đúng bằng phần bù.
- Giới hạn ① — R1 không tự tăng theo k₁. Thực tế recall@k₁ tăng khi k₁ tăng 
 (bão hoà dần). Mô-đun tách hai thanh trượt để bạn thấy hai hiệu ứng ngược chiều: k₁ lớn 
 nâng R1 nhưng làm loãng shortlist. Muốn mô phỏng đầy đủ, kéo cả hai cùng lúc.
- Giới hạn ② — ba tầng coi như độc lập. Thực tế chúng tương quan: câu hỏi khó 
 thì cả retrieval lẫn generation đều dễ hỏng, nên tỉ lệ đúng thật thấp hơn tích ba xác suất.
- Giới hạn ③ — không mô hình hoá lost-in-the-middle. Ở đây "chứng cứ vào prompt" 
 coi như "model thấy được". Mô-đun thứ ba thêm chiều đó, và nó làm bức tranh 
 xấu đi thêm.
- Giới hạn ④: mô hình giả định có đúng một chứng cứ cần tìm. Câu hỏi 
 multi-hop cần nhiều chứng cứ cùng lúc thì xác suất giảm theo luỹ thừa — 
 slide 47 đề xuất query decomposition đúng vì lý do này.

---

<!-- chiron-source-span: {"source_span_id":"4f12ec2f-9558-56e4-acbb-8732b71e2bb1","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Parsing & ingestion — phần lặp lại Ngày 7","source_file":"slide-day08.html"},"checksum":"19e5623963301853504317fac1d90323ad0a5b952361565148926d2a2835e6e0"} -->

## 03 Parsing & ingestion — phần lặp lại Ngày 7

Chương này gần như trùng hoàn toàn với [Ngày 7 · chương 
 05](slide-day07.html), và Ngày 7 nói sâu hơn nhiều. Đọc lướt để nhớ vocabulary; phần đáng dừng lại chỉ có hai chỗ.

### Slide 20–22 Dữ liệu thực tế lộn xộn, PDF, và cơn ác mộng mang tên bảng biểu

> Trích slide 
>  "Các khoá học thường demo bằng file.txt sạch sẽ. Thực tế doanh nghiệp là: PDF scan 
>  (hoá đơn, hợp đồng) · email cũ (nhiều ký tự lạ) · slide thuyết trình (layout phức tạp). 
>  OCR kém sẽ đọc chữ 'I' thành số '1', làm hỏng toàn bộ keyword quan trọng. " 
>  "Chuẩn PDF sinh ra để in ấn, nó lưu toạ độ (x, y) của chữ chứ không hiểu cấu trúc 
>  ngữ nghĩa. Các parser cơ bản thường đọc từ trái sang phải, làm trộn lẫn văn bản giữa 2 cột 
>  riêng biệt thành một câu vô nghĩa." 
>  "Nếu dùng thuật toán cắt text thông thường, bảng bị xẻ làm đôi. Nửa dưới mất liên kết với 
>  Header → Vector vô dụng. Giải pháp: parser chuyên dụng (LlamaParse, Unstructured) để bóc 
>  tách thành HTML/Markdown."

Ngày 7 · slide 30–37

| Khẳng định chung | Ngày 8 nói | Ngày 7 kèm số |
| --- | --- | --- |
| Bảng bị cắt vỡ làm vector vô dụng | Định tính | Recall@1 BM25: 0,366 → 0,754 (STC vs Recursive, MAUD 39.231 bản ghi, 
 arXiv:2605.00318) |
| Parser chuyên dụng đáng dùng | Gợi ý LlamaParse, Unstructured | Bảng 7 công cụ + OmniDocBench, kèm cảnh báo "phần lớn benchmark do chính nhà cung cấp 
 chạy" |
| OCR nhầm ký tự | "I" thành "1" | Dấu thanh tiếng Việt (ma/mà/má/mã/mạ), ngưỡng 300 DPI, chuẩn hoá 
 NFC |

Nếu ôn thi:

```text
RAW TEXT "SOUP" — parser co ban
  Basic Pro Enterprise
  $9/month $29/month $99/month
  10Gb Storage 50GB Storage Unlimited Storage
  -> khong con quan he cot-hang. Vector cua doan nay vo nghia.

MARKDOWN — parser chuyen dung
  | Basic     | Pro       | Enterprise        |
  |-----------|-----------|-------------------|
  | $9/month  | $29/month | $99/month         |
  | 10Gb      | 50GB      | Unlimited Storage |
  -> quan he cot-hang duoc giu. LLM doc duoc, va chunk khong lam vo no.
```

Markdown giữ được quan hệ vì nó có ranh giới rõ ràng

|

slide 88

cấu trúc tường minh giúp model đọc đúng.

### Slide 23–25 Vision model, làm sạch, và chiến lược ingestion

> Trích slide 
>  Multimodal parsing: "ném thẳng ảnh chụp trang tài liệu cho Vision LLMs. Ưu điểm: 
>  hiểu cấu trúc siêu phức tạp, đọc được biểu đồ. Nhược điểm: tốn kém chi phí API, chạy chậm — 
>  không phù hợp cho kho dữ liệu hàng triệu trang. " 
>  Làm sạch: "gộp khoảng trắng thừa, sửa lỗi unicode (font tiếng Việt 
>  cũ), xoá control characters · Redaction: xoá CCCD, số thẻ tín dụng, số điện 
>  thoại trước khi đưa lên Cloud Vector DB (GDPR/PDPA)." 
>  Ingestion: " Batch — quét lại toàn bộ vào 12h đêm, dễ triển khai nhưng 
>  thông tin bị trễ (stale data). Event-Driven (Delta Sync) — webhook bắt sự 
>  kiện, chỉ cập nhật file vừa sửa. Idempotency: phải thiết kế hệ thống băm (hashing) nội dung 
>  để tránh lưu trùng lặp. "

thêm được

Chi phí

Trùng lặp

near-duplicate làm hỏng top-k

Ngày 7 · slide 35

Chạy lại an toàn

idempotent

Cạm bẫy khi cài đặt:

sau khi chuẩn hoá

Ngày 7 · slide 39

cloud

Ngày 7 · slide 82

đảo ngược được về gần nguyên văn

pseudonymized

vẫn là dữ liệu cá nhân

Phát biểu đúng:

---

<!-- chiron-source-span: {"source_span_id":"c20cfa42-de70-501d-84f6-f70537860434","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Chunking & Small-to-Big","source_file":"slide-day08.html"},"checksum":"4d687040ab872b5482340553d310a8291e3fe269726a8c3f86093f64e666d02d"} -->

## 04 Chunking & Small-to-Big

Ba chiến lược đầu trùng Ngày 7. Nhưng **Small-to-Big (Parent-Child)** ở 
 slide 32 là kỹ thuật mới, và nó giải quyết đúng mâu thuẫn mà Ngày 7 nêu ra rồi bỏ ngỏ.

### Slide 27–31 Ba chiến lược, và vì sao cần overlap

> Trích slide 
>  Vì sao phải chunk: " Giới hạn context window — dù Gemini 1.5 hỗ trợ 2M token, nhét 
>  cả nghìn trang vào prompt rất đắt và tốn TTFT. · Giảm nhiễu — nếu nhúng cả một chương 
>  sách vào 1 vector, các ý chính sẽ bị pha loãng." 
>  Fixed-size: "cực kỳ dễ code… Tử huyệt: rất dễ cắt ngang một câu — ví dụ 
>  cắt giữa chữ 'không' và 'được phép'." · Recursive: " tiêu chuẩn 
>  vàng mặc định trong LangChain… thử cắt theo thứ tự \n\n → \n →. " · 
>  Semantic/Structural: "cắt theo cấu trúc logic — Markdown/HTML theo thẻ H1, H2; Code 
>  dùng AST để tách từng function." 
>  Overlap: "một ý quan trọng có thể vô tình bị chia làm 2 mảnh nằm ở mép của 2 
>  chunk. Overlap thường set khoảng 10–15% tổng size. Hoạt động như chất keo 
>  dính giữ lại mạch ngữ cảnh."

"Chính sách này áp dụng cho toàn bộ nhân viên ngoại | trừ thực tập sinh."

|

"…áp dụng cho toàn bộ nhân viên ngoại"

"áp dụng cho tất cả"

"trừ thực tập sinh."

Đây là loại lỗi tệ nhất có thể có trong RAG

ngược hẳn

không tìm thấy

Đảo ngược 
 nghĩa

"ngoại trừ thực tập sinh"

① Chi phí và TTFT

kinh tế

② Giảm nhiễu — "ý chính bị pha loãng"

toán học

trung bình

Ngày 7 · slide 72

không

retrieval thu hẹp corpus lớn, rồi giao tập con cho 
 long-context model suy luận

### Slide 32 Small-to-Big — kỹ thuật mới, và nó giải đúng mâu thuẫn của Ngày 7

> Trích slide 
>  " Vấn đề: chunk nhỏ thì search chính xác nhưng thiếu ngữ cảnh. Chunk to thì search 
>  dễ trượt nhưng ngữ cảnh dồi dào." 
>  " Giải pháp Parent-Child: lưu trữ các chunk là những câu siêu ngắn (Small) để chạy 
>  Vector Search lấy độ chính xác cao. Khi tìm trúng câu nhỏ đó, hệ thống tự động móc nối và gửi 
>  toàn bộ đoạn văn lớn chứa câu đó (Parent) vào LLM Prompt."

Đây là slide có giá trị cao nhất trong ba chương đầu, vì nó giải quyết một mâu thuẫn mà [Ngày 7 · slide 43](slide-day07.html) nêu ra và *không* giải:

chunk 64–128 token tối ưu cho câu hỏi factoid 
 ngắn; 512–1024 token tốt hơn khi cần ngữ cảnh rộng.

lối thoát thứ nhất chính là 
 Small-to-Big

"index chunk nhỏ để trúng chính xác, nhưng khi trả về thì mở rộng ra 
 section chứa nó trước khi nhồi vào prompt."

Vì sao nó hoạt động — tách hai vai trò vốn bị gộp:

|  | Đơn vị để TÌM | Đơn vị để ĐỌC |
| --- | --- | --- |
| Yêu cầu | Càng hẹp càng dễ khớp với một câu hỏi cụ thể | Càng đủ ngữ cảnh càng dễ trả lời trọn vẹn |
| Chunking thường | Cùng một đơn vị — nên phải thoả hiệp, 
 và thoả hiệp nào cũng thua ở một phía |  |
| Small-to-Big | Child — câu ngắn, vector sắc | Parent — cả section, ngữ cảnh đầy đủ |

không có kích thước chunk tối ưu, vì "chunk" đang làm hai việc khác nhau.

① Nhiều child cùng trỏ về một parent.

cùng một parent năm lần

redundancy ở slide 78

② Ngân sách token phình nhanh.

slide 89

mô-đun k

③ Phải lưu hai tầng.

Khi nào đáng:

Khi nào không:

### Slide 33–34 Chunking cho bảng, và bảng đối chiếu tốt/tệ

> Trích slide 
>  "Bảng biểu không có câu văn hoàn chỉnh, vector search rất khó bắt nghĩa. 
>  Cách 1 — Row to Text: biến từng dòng thành một câu văn tự nhiên ( 'Sản phẩm 
>  iPhone 15 có giá 20 triệu, tồn kho 5 chiếc' ). Cách 2 — LLM Summarization: dùng 
>  LLM đọc toàn bộ bảng, viết một đoạn tóm tắt, lưu đoạn tóm tắt đó thành vector đại diện cho cái bảng." 
>  Chunking tệ: "cắt giữa một bảng hoặc điều khoản · quá to: nhiều ý không liên quan · quá nhỏ: mất 
>  ngữ cảnh và thiếu source." Chunking tốt: "cắt theo heading, section, paragraph tự 
>  nhiên · overlap vừa đủ · giữ source, section, date." 
>  Ví dụ chunk tốt: "Hoàn tiền — Điều kiện áp dụng / Yêu cầu được gửi trong 7 ngày… / 
>  Source: policy/refund-v4.pdf · Điều 3 "

|  | Row to Text | LLM Summarization |
| --- | --- | --- |
| Trả lời được câu hỏi | "iPhone 15 giá bao nhiêu?" — tra một ô cụ thể | "Xu hướng giá trong bảng này thế nào?" — tổng hợp toàn bảng |
| Chi phí | ~0 — chỉ là ghép chuỗi | Một lần gọi LLM mỗi bảng — nhưng 
 offline, nên chấp nhận được |
| Hỏng khi nào | Bảng có header nhiều tầng hoặc ô merge (Ngày 7 · slide 36) | Bảng quá lớn để vừa context; và tóm tắt làm mất số cụ thể |

Kiến trúc đúng: index cả hai.

và

table_id

Ngày 7

structure-aware tabular 
 chunking

Recall@1 trên BM25 tăng 2,06 lần

source, section, date

Source: policy/refund-v4.pdf · Điều 3

source

citation

slide 11

section

Small-to-Big

date

xung đột ngữ cảnh

"nếu có mâu thuẫn, ưu tiên tài liệu có ngày cập nhật mới nhất"

Ngày 7 · slide 40

"provenance giữ từ đây, không thể thêm sau"

---

<!-- chiron-source-span: {"source_span_id":"54c59e05-1d47-5db5-a8b7-2cbb78754d6d","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Embedding & metadata filter","source_file":"slide-day08.html"},"checksum":"d450a2bfc91ae123c08ab265879fd6151bb8f3a914ecbbbd029e5f4371102a3c"} -->

## 05 Embedding & metadata filter

Chương ngắn, và nó chứa một chỗ deck Ngày 8 *mâu thuẫn* với Ngày 7 — đáng ghi 
 nhận vì nó dạy cách xử lý khi hai nguồn nói khác nhau.

### Slide 37–38 Chọn model, và điểm mù của vector search

> Trích slide 
>  " Số chiều: model nhỏ (bge-micro, 384 chiều) tính toán siêu nhanh, ít tốn RAM. 
>  Model lớn (OpenAI, 1536 chiều) phân biệt nghĩa tinh tế hơn nhưng chi phí hạ tầng cao gấp 4 
>  lần. · Rào cản ngôn ngữ: đừng dùng model chuyên tiếng Anh cho văn bản tiếng 
>  Việt. Phải chọn model Multilingual (m-E5, Cohere Multilingual)." 
>  " Vector cực kỳ tồi tệ khi đối mặt với Exact Match: mã hợp đồng, ID lỗi (ERR-809), 
>  số series. Model nhúng có thể xếp ERR-809 và ERR-810 sát cạnh nhau vì cấu trúc giống 
>  nhau, dẫn đến trả lời nhầm."

4×

N × d × 4 byte

bộ nhớ

Ngày 7 · mô-đun kinh tế

chi phí embedding chiếm 0,0% chi phí vận hành hàng tháng.

$2 so với $20, trả một lần

Đúng

"ngưỡng rời Postgres là lúc index không còn fit RAM"

Gây hiểu nhầm

Cách phát biểu chặt:

hạ tầng

ngân sách API

57

60

62

lập luận trung tâm cho hybrid search

gần nghĩa

ERR-809

ERR-810

đúng như nó được dạy

Ngày 7 · slide 67

E-4471

SKU VN-2291-XL

"trong truy vấn có chuỗi nào mà sai một ký tự là đổi hoàn toàn ý nghĩa không?"

### Slide 39–41 Metadata, pre-filter so với post-filter — và chỗ deck nói quá

> Trích slide 
>  "Đừng bao giờ chỉ đẩy Raw Text vào Database. Một chunk tốt phải mang theo 'giấy tờ tuỳ 
>  thân': source_file, doc_type, date_created, department_owner. Lợi ích: cho phép 
>  cắt giảm không gian tìm kiếm trước khi chạy thuật toán vector nặng nề." 
>  Post-filtering: "search top 100 vector gần nhất, sau đó loại bỏ kết quả không 
>  thuộc năm 2026. Rủi ro: có thể bị rớt mất tài liệu quan trọng nếu nó nằm ở hạng 101. " 
>  Pre-filtering: "yêu cầu DB chỉ nhìn vào vùng không gian chứa tài liệu năm 2026, 
>  rồi mới chạy Vector Search. Nhanh hơn, an toàn hơn, và chính xác tuyệt đối. "

|  | Ngày 8 · slide 40 | Ngày 7 · slide 65 |
| --- | --- | --- |
| Post-filter | "rủi ro rớt tài liệu ở hạng 101" | " mất recall âm thầm: có thể trả về < k hoặc 0 kết quả" — kèm quan sát 
 thật trên pgvector: xin 15, nhận 11 |
| Pre-filter | "nhanh hơn, an toàn hơn, chính xác tuyệt đối " | "đúng, nhưng suy biến về brute-force; đồ thị HNSW xây cho toàn corpus phục 
 vụ kém trên subgraph nhỏ" |
| Lựa chọn thứ ba | Không nhắc | In-algorithm filtering — tốt nhất, nhưng cần engine hỗ trợ (Qdrant 
 payload-aware HNSW, Weaviate ACORN) |

Ngày 7 đúng hơn ở hai điểm.

không

khuyến nghị hành động

Cách xử lý khi hai nguồn mâu thuẫn:

quan sát cụ thể

chunk_size=1000, chunk_overlap=150

15%

slide 31

1000

512–1024 cho ngữ cảnh rộng

lớn gấp 8–15 lần

đổi embedding model là phải đo lại chunk size

điểm khởi đầu để chạy được

---

<!-- chiron-source-span: {"source_span_id":"c4f0b137-e997-5571-bb3a-31f8a3afadb2","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Query transformation — bốn kỹ thuật, và cái giá của chúng","source_file":"slide-day08.html"},"checksum":"e31b2636d8a537f927c176a165834bafb4c851698bb224cfb736c2d94c550c6f"} -->

## 06 Query transformation — bốn kỹ thuật, và cái giá của chúng

Toàn bộ chương này là nội dung **mới so với Ngày 7**. Nó cũng là chương 
 duy nhất mà deck tự đưa ra một checklist "đừng lạm dụng" — đáng đọc kỹ.

### Slide 44–45 Người dùng không bao giờ hỏi đúng — và LLM làm "màng lọc"

> Trích slide 
>  " Khoảng cách từ vựng: người dùng dùng ngôn ngữ 'đường phố' hoặc mơ hồ. Tài liệu 
>  nội bộ dùng ngôn ngữ chuyên môn trang trọng. · Thiếu ngữ cảnh: câu hỏi cụt lủn (vd: 
>  'hoàn tiền') khiến Vector DB trả về quá nhiều kết quả nhiễu. · Nếu lấy raw query đi search 
>  thẳng, Retriever sẽ thất bại ngay từ giây đầu tiên. " 
>  Ví dụ: "sao app cứ văng" ↔ tài liệu ghi "Troubleshooting Unhandled Exceptions" 
>  "Đặt một LLM nhỏ, tốc độ cao (GPT-4o-mini, Gemini Flash) làm màng lọc 
>  đứng trước Vector Database… Đây là bước đệm hoàn hảo trước khi ta biến Retriever thành một 
>  'Tool' độc lập cho các Agent (LangGraph) ở giai đoạn sau."

Ví dụ *"sao app cứ văng"* so với *"Troubleshooting Unhandled Exceptions"* là ví dụ 
 hoàn hảo cho **vocabulary mismatch** — và đáng chú ý là nó có *ba* tầng khoảng 
 cách cùng lúc, không phải một:

| Tầng khoảng cách | Người dùng | Tài liệu | Cái gì giải được |
| --- | --- | --- | --- |
| Ngôn ngữ | Tiếng Việt | Tiếng Anh | Embedding đa ngôn ngữ ( slide 37 ) — dense làm được, BM25 không |
| Đăng ký ngôn ngữ | Khẩu ngữ: "văng" | Trang trọng: "unhandled 
 exceptions" | Dense hoặc query expansion |
| Trừu tượng | Triệu chứng: "cứ văng" | Nguyên nhân kỹ thuật | Chỉ query transformation — không embedding nào 
 bắc cầu triệu chứng → nguyên nhân |

Ngày 7 · slide 13

"Cứ văng"

"unhandled exception"

bước suy luận nhân quả

vì

không phải để diễn đạt lại, mà để suy luận một 
 bước rồi mới diễn đạt lại.

Step-Back Prompting

### Slide 46–50 Bốn kỹ thuật: Expansion, Decomposition, Step-Back, HyDE

> Trích slide 
>  1. Query Expansion: "chữa lỗi chính tả và thêm từ đồng nghĩa… tăng mạnh 
>  độ phủ (Recall)." Ví dụ: "nghỉ đẻ" → ["nghỉ thai sản", "maternity leave", "chế 
>  độ phụ sản", "trợ cấp sinh con"] 
>  2. Query Decomposition: "xử lý câu hỏi phức tạp (Multi-hop). Một Vector 
>  biểu diễn tài liệu không thể đồng thời trả lời cho hai ý niệm quá khác biệt. " Ví dụ: 
>  "So sánh chính sách hoàn tiền của Shopee và Tiki" → hai truy vấn song song → gộp context 
>  3. Step-Back Prompting: "khi câu hỏi đi quá sâu vào tiểu tiết, model dễ bị lạc… 
>  LLM sinh ra câu hỏi lùi lại một bước." Ví dụ: "Lỗi 404 khi gọi API thanh toán Momo của 
>  user ID 8910" → "Kiến trúc tích hợp cổng thanh toán Momo hoạt động như thế nào?" 
>  4. HyDE: "dùng LLM 'bịa' ra một câu trả lời giả định … vì một 
>  đoạn văn bản trả lời ( dù sai sự thật ) sẽ có cấu trúc ngữ pháp, từ vựng và 'hình 
>  dáng toán học' cực kỳ giống với tài liệu thật. Ta đem vector của 'câu trả lời giả' đi tìm 
>  'câu trả lời thật'."

Bốn kỹ thuật này giải bốn vấn đề khác nhau, và chọn nhầm thì không giúp gì. Bảng phân biệt:

| Kỹ thuật | Chữa vấn đề gì | Dấu hiệu bạn cần nó | Số lần gọi retrieval |
| --- | --- | --- | --- |
| Expansion | Từ vựng khác nhau, lỗi chính tả | Recall thấp với câu hỏi ngắn, dùng khẩu ngữ | Nhiều (mỗi biến thể một lần) |
| Decomposition | Câu hỏi chứa hai ý niệm tách biệt | Câu hỏi có "so sánh", "và", "khác nhau thế nào" | Một lần mỗi ý con |
| Step-Back | Câu hỏi quá cụ thể, không tài liệu nào khớp | Có ID/số cụ thể mà tài liệu chỉ viết ở mức quy tắc chung | Hai (chung + cụ thể) |
| HyDE | Hình dạng câu hỏi khác hình dạng tài liệu | Câu hỏi ngắn tìm đoạn văn dài — tức là RAG nói chung | Một |

"Vector 'câu hỏi' và 'câu trả lời' thường nằm cách xa nhau 
 (do định dạng ngữ pháp hoàn toàn khác biệt). HyDE đóng vai trò như một phép nội suy, kéo Query Vector 
 về đúng cụm không gian chứa Document Vectors."

Ngày 7 · slide 21

asymmetric search

query:

passage:

một cách

cách khác

Và đây là lý do HyDE thường thừa nếu bạn đã dùng đúng prefix.

trong model

ngoài model

Điều cần cẩn thận:

có thể lái 
 retrieval sang chủ đề sai

"Một Vector biểu diễn tài liệu không thể đồng thời trả lời cho hai ý niệm quá khác biệt."

toán học

khoảng giữa

mô-đun phễu

một

tích của hai

### Slide 52–53 Đánh đổi, và checklist "đừng lạm dụng"

> Trích slide 
>  Được: "cải thiện cực lớn độ chính xác và Recall · xử lý được các ca người dùng 
>  'hỏi ngốc'." Mất: " tăng độ trễ vì phải gọi API LLM 1 lần trước khi đụng vào 
>  Database · tốn thêm chi phí token." 
>  Checklist cho production: " Đừng lạm dụng! Chỉ bật Query Transformation khi hệ 
>  thống gặp nhiều user queries phức tạp/mơ hồ. · Dùng model rẻ nhất có thể (GPT-4o-mini 
>  / Haiku) cho bước này để giữ Latency < 1s. · Kết hợp với Semantic 
>  Cache để không phải transform lại các câu hỏi phổ biến."

slide 14

| Offline — trả một lần | Real-time — trả mỗi truy vấn |
| --- | --- |
| Parser VLM · LLM tóm tắt bảng · Contextual Retrieval · Small-to-Big indexing | Query transformation · rerank · generation |
| Đắt bao nhiêu cũng cân nhắc được | Mỗi mili-giây và mỗi cent nhân với số truy vấn |

trước khi

bật có điều kiện

model rẻ

cache

Ngày 7 · failure mode 13

"cache trả lời sai một cách tự tin — cache key không version theo embedding model, hoặc thiếu 
 TTL."

gần giống

"chính sách nghỉ phép cho nhân viên chính thức"

"chính sách nghỉ phép cho thực tập sinh"

Quy tắc:

version của model + version của index

---

<!-- chiron-source-span: {"source_span_id":"bf2058c6-e5d8-5a33-86ad-c6df94acf172","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Dense so với sparse — và nghịch lý enterprise","source_file":"slide-day08.html"},"checksum":"418c3073f799540ef72e0d0ed2e59fb118936114b80bd5706668254a53178ec0"} -->

## 07 Dense so với sparse — và nghịch lý enterprise

Chương này lặp lại Ngày 7 về nội dung nhưng thêm một luận điểm sắc mà Ngày 7 không 
 có: *nghịch lý enterprise ở slide 62*.

### Slide 55–60 Hai trường phái, hai điểm mù đối xứng

> Trích slide 
>  Sparse (BM25): "trái tim của Elasticsearch… vector rất dài (bằng toàn bộ số từ 
>  trong từ điển) nhưng chứa toàn số 0. Nguyên lý: đánh trọng số cực cao cho 
>  các từ hiếm (Kubernetes) và phớt lờ các từ phổ biến (và, là, thì)." 
>  Tử huyệt của sparse: "cực kỳ nhạy cảm với lỗi chính tả — sai một chữ cái 
>  là Not Found. Hoàn toàn không hiểu từ đồng nghĩa." Ví dụ: user tìm "Tôi muốn đòi lại 
>  tiền", document ghi "Chính sách hoàn tiền" → BM25: 0 kết quả. 
>  Dense bù đắp: "không quan tâm bạn gõ 'hoàn tiền', 'trả tiền', hay sai chính tả 
>  'hoang tien'… Cross-lingual: user hỏi bằng tiếng Việt, vector search vẫn map đúng 
>  vào tài liệu tiếng Anh." 
>  Hai điểm mù: "Query 'Mã lỗi ERR-x09' → dense trả về general error handling docs 
>  ( miss exact ID ). Query 'Muốn lấy lại tiền' → BM25 0 kết quả."

| Truy vấn | Dense | BM25 | Vì sao |
| --- | --- | --- | --- |
| "Tôi muốn đòi lại tiền" (doc: "Chính sách hoàn tiền") | Thắng | 0 kết quả | Không từ nào trùng |
| "hoang tien" (gõ sai dấu) | Thắng | 0 kết quả | BM25 khớp chuỗi chính xác |
| Hỏi tiếng Việt, tài liệu tiếng Anh | Thắng | 0 kết quả | Embedding đa ngôn ngữ ánh xạ chung một không gian |
| "Mã lỗi ERR-x09" | Trả về ERR-x10, ERR-x11 — SAI | Thắng | Dense làm nhoè token hiếm; BM25 cho từ hiếm trọng số 
 cực cao |
| "SKU VN-2291-XL" | Sai | Thắng | Token ngoài tập huấn luyện — embedding không có gì để dựa vào |

ba dòng đầu BM25 trả về 0 kết quả — không phải kết quả kém, mà là 
 KHÔNG CÓ GÌ.

kết quả sai trông có vẻ đúng

tự tin trả lời sai

Hệ quả:

nguy hiểm hơn

Lưu trữ rẻ bất ngờ.

inverted 
 index

slide 71

Không có khái niệm "gần".

"hoàn tiền"

"đòi lại tiền"

### Slide 61–62 Bảng tổng kết, và "nghịch lý enterprise"

> Trích slide 
>  " Các tutorial YouTube chỉ dạy bạn Vector Search vì nó 'nghe có vẻ AI'. Ở môi 
>  trường Doanh nghiệp (tra cứu hợp đồng, log kỹ thuật, tài liệu luật), BM25 thường quan trọng 
>  hơn Vector. Nếu bỏ BM25, hệ thống sẽ thất bại thảm hại. " 
>  Bảng: Sparse — "tốc độ tính toán nhanh, chi phí phần cứng thấp; hiệu quả tuyệt đối với từ khoá 
>  hiếm, tên riêng, mã định danh" · Dense — "hiểu từ đồng nghĩa; đòi hỏi tài nguyên tính toán 
>  cao hơn, yêu cầu hạ tầng chuyên dụng như Vector Database và ANN."

thuật toán từ 1994 thường quan trọng hơn embedding 
 2026

Ngày 7 · slide 13

có thể thua BM25

corpus của bạn gần như chắc chắn nằm ngoài domain huấn luyện của mọi embedding model công 
 khai

không phải trường hợp hiếm; nó là trường hợp mặc định 
 của bạn.

Hành động cụ thể, rẻ, và gần như không ai làm:

Ngày 7 · slide 75

Ngày 7 · slide 51 và 63

"corpus nhỏ (vài nghìn document trở xuống) — một vector DB lúc này là over-engineering"

"dưới 10k vector… sub-ms. Bỏ qua vector DB."

30,7 MB

dưới 10 ms

100%

Phát biểu đúng:

khi corpus đủ lớn để 
 index không vừa RAM

---

<!-- chiron-source-span: {"source_span_id":"3462ef28-c140-50ed-ae29-bab268a60555","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Hybrid search & RRF — bài toán \"cam và táo\"","source_file":"slide-day08.html"},"checksum":"8c5e8dab0cd19ac14d05b50397bda13ed714896a660e0de09fdb8f22d6858bba"} -->

## 08 Hybrid search & RRF — bài toán "cam và táo"

Chương này sâu hơn Ngày 7 ở một chỗ quan trọng: nó nói rõ *vì sao* không cộng 
 thẳng hai điểm số được, và đưa ra cả hai lời giải (RRF và alpha tuning) cùng đánh đổi của mỗi cái.

### Slide 64–66 "Cam và táo", và lời giải RRF

> Trích slide 
>  "Chạy song song cả BM25 và Vector Search cho cùng một câu hỏi. Đảm bảo hệ thống 
>  không bỏ lỡ mã số (nhờ BM25) và cũng không lọt ngữ nghĩa (nhờ 
>  Vector). Trở thành tiêu chuẩn bắt buộc cho Production RAG hiện đại." 
>  Bài toán khó: "Vector Score — cosine thường nằm trong khoảng 0.0 → 
>  1.0. BM25 Score — không có giới hạn trên, có thể từ 0 → 100+. Thách thức: 
>  không thể cộng trực tiếp Score_Vector + Score_BM25 để xếp hạng." 
>  RRF: " Đừng gộp điểm số (Scores), hãy gộp Thứ hạng (Ranks). 
>  RRF = 1/(k + Rank_Dense) + 1/(k + Rank_Sparse), k thường chọn mặc định là 
>  60. Tài liệu nào nằm trong Top cao ở cả 2 bảng xếp hạng sẽ vươn lên vị trí 
>  số 1 tuyệt đối. "

Bài toán "cam và táo" nghe như một bất tiện kỹ thuật nhỏ. Nó không phải — nó là một vấn đề **không có lời giải sạch bằng cách chuẩn hoá**, và đó là lý do RRF tồn tại:

① Chuẩn hoá phụ thuộc vào chính tập kết quả của truy vấn đó.

Cùng một tài 
 liệu, cùng một điểm thô, hai truy vấn khác nhau cho hai điểm chuẩn hoá khác nhau.

② Một outlier phá cả thang đo.

③ Không có cơ sở lý thuyết để nói cosine 0,8 "bằng" BM25 chuẩn hoá 0,8.

vứt bỏ điểm số và chỉ giữ thứ hạng

k = 60

```text
hang 1 -> 1/61 = 0,016393
hang 2 -> 1/62 = 0,016129     chenh hang 1 va 2: 0,00026
hang 3 -> 1/63 = 0,015873
hang 10 -> 1/70 = 0,014286     chenh hang 1 va 10: 0,00211

NEU k = 0 (khong lam mem):
hang 1 -> 1/1 = 1,000
hang 2 -> 1/2 = 0,500         chenh hang 1 va 2: 0,500  <- ap dao
```

rất nhỏ

không

cả hai nhánh

"tài liệu nào nằm trong Top cao ở cả 2 
 bảng xếp hạng sẽ vươn lên vị trí số 1 tuyệt đối."

Mô-đun tiếp theo

k là núm vặn "cần bao nhiêu sự đồng thuận".

#### Tương tác "Cam và táo" — RRF so với cộng điểm, trên tám tài liệu thật

Slide 66 khẳng định: *"tài liệu nào nằm trong Top cao ở cả 2 bảng xếp hạng sẽ vươn 
 lên vị trí số 1 tuyệt đối."* Mô-đun này dựng một ví dụ tám tài liệu để kiểm — và để thấy ba cách 
 gộp khác nhau hỏng ở đâu.

Truy vấn: *"Mã lỗi ERR-X09 xử lý thế nào?"*. Đáp án đúng là **D3** — nó vừa 
 nói đúng chủ đề (cosine 0,83, hạng 3 dense) vừa chứa mã lỗi (BM25 28,0, hạng 2). 
 Kẻ phá đám là **D7**: một file changelog nhồi *"ERR-X09"* bốn mươi lần — 
 BM25 **95,0** (hạng 1) nhưng cosine chỉ 0,61 (hạng 7). Nó không trả lời được gì.

Đoán trước: *(a)* cộng thẳng `cosine + BM25` thì tài liệu nào lên đầu? *(b)* trộn min-max với α = 0,5 thì sao? *(c)* RRF k = 60 thì sao?

#### Kéo rồi mở

**(a) D7 lên hạng 1 — sai.** BM25 không chặn trên nên 95,0 nuốt gọn mọi cosine 
 (vốn tối đa là 1,0). Cộng thẳng hai thang đo khác đơn vị thì *thang lớn hơn quyết định tất 
 cả* — bạn thực chất đang xếp hạng thuần BM25 và tự nhủ là đang làm hybrid.

**(b) α = 0,5 vẫn để D7 hạng 1.** Min-max đã đưa cả hai về [0, 1], nhưng D7 vẫn 
 có điểm sparse tuyệt đối 1,0 — nó là max của thang. Trộn nửa-nửa thì lợi thế đó vẫn đủ để nó 
 thắng. *Chuẩn hoá không cứu được, vì vấn đề không nằm ở đơn vị mà ở việc một outlier chiếm 
 trọn đầu thang.*

**(c) RRF k = 60 đưa D3 lên hạng 1 — đúng.** Vì sao: D3 hạng 3 + hạng 2 → điểm `1/63 + 1/62 = 0,03200`. D7 hạng 7 + hạng 1 → `1/67 + 1/61 = 0,03132`. D1 
 hạng 1 + hạng 5 → `1/61 + 1/65 = 0,03177`. 
 D3 thắng **không phải vì nó đứng đầu bảng nào**, mà vì nó *khá cao ở cả 
 hai*. Đây chính xác là khẳng định của slide 66, và nó đứng vững.

**Thử điều đáng thử nhất — kéo thanh "điểm BM25 của D7" từ 95 xuống 30 rồi lên 300:** thứ hạng D3 dưới RRF **không đổi chút nào**. Còn cộng điểm thô và trộn α thì đổi liên 
 tục. 
 Lý do: RRF chỉ nhìn *thứ hạng*. D7 vẫn là hạng 1 của BM25 dù điểm là 30 hay 300 — nên 
 đóng góp của nó vào RRF giữ nguyên. **RRF miễn nhiễm với độ lớn của điểm, và đó là toàn bộ 
 lý do nó tồn tại.**

*Bài học vận hành:* nhìn đường cong — **D3 dưới RRF là một đường thẳng**, 
 không phụ thuộc α. Còn dưới trộn α, thứ hạng của D3 nhảy giữa 2 và 3 tuỳ bạn chọn α bao nhiêu, và 
 không α nào đưa nó lên hạng 1. Chọn α là một siêu tham số nữa phải tune; RRF thì không có gì để 
 tune.

- **Control - α — trọng số cho dense (slide 67): 0,50**: min `0`, max `100`, step `5`, default `50`

- **Control - k của RRF (slide 66 mặc định 60): 60**: min `1`, max `200`, step `1`, default `60`

- **Control - Điểm BM25 của D7 (file nhồi từ khoá): 95,0**: min `5`, max `300`, step `5`, default `95`

RRF — tài liệu đúng

—

—

Trộn α (min-max)

—

—

Cộng điểm thô

—

—

Chỉ dense

—

—

D3 — tài liệu đúng, trộn α D7 — nhồi từ khoá, trộn α D3 dưới RRF (không phụ thuộc α)

#### Xem bảng: tám tài liệu, hai bảng xếp hạng, và điểm RRF



#### Công thức & giới hạn của mô hình

- RRF(d) = 1/(k + rank_dense) + 1/(k + rank_bm25) — nguyên văn slide 66, k mặc định 
 60.
- Trộn α = α·norm(cosine) + (1−α)·norm(BM25), chuẩn hoá min-max trên chính tập tám 
 tài liệu — nguyên văn slide 67.
- Giới hạn ① — tám tài liệu là ví dụ do tài liệu này dựng. Điểm cosine và BM25 
 là số minh hoạ, không phải đo từ hệ thống thật. Chúng được chọn để tái hiện tình huống mà 
 slide 65 mô tả (BM25 không chặn trên) và slide 62 cảnh báo (nhồi từ khoá).
- Giới hạn ② — min-max chuẩn hoá trên tập kết quả. Đây là cách làm phổ biến và 
 cũng là nguồn gốc của tính bất ổn: cùng một tài liệu ở hai truy vấn khác nhau sẽ có điểm chuẩn hoá 
 khác nhau. Chuẩn hoá theo phân bố toàn corpus ổn định hơn nhưng đắt và ít ai làm.
- Giới hạn ③ — RRF không phải luôn thắng. Nó vứt bỏ thông tin về mức độ 
 tự tin. Nếu một nhánh thật sự chắc chắn (cosine 0,97 so với 0,55 cho phần còn lại), RRF không tận 
 dụng được điều đó. Đổi lại là tính bền vững — và với hai thang đo không so được, bền vững đáng giá 
 hơn.
- Kéo k của RRF về 1–5 để thấy điều ngược lại: khi k nhỏ, một nhánh xếp hạng 1 
 đủ áp đảo, và RRF mất tính chất "cần đồng thuận".

### Slide 67–71 Alpha tuning, hạ tầng, và cái giá của hybrid

> Trích slide 
>  Final_Score = (α × Dense_norm) + ((1 − α) × Sparse_norm) — "nếu α = 1: thuần Vector. 
>  Nếu α = 0: thuần BM25." 
>  " Chatbot FAQ: α = 0.7 – 0.9 (ưu tiên hiểu ý định mơ hồ). Tra cứu Code, 
>  Log, Luật pháp: α = 0.2 – 0.4 (ưu tiên khớp chính xác tên biến, điều khoản)." 
>  "Không phải Vector DB nào cũng hỗ trợ Hybrid chuẩn. Cần database hỗ trợ lưu cả Dense 
>  vectors và Sparse/Inverted indexes cùng lúc: Weaviate, Milvus, Qdrant, Elasticsearch." 
>  Chi phí: "phải nhân đôi tài nguyên lưu trữ (build 2 index cho cùng 1 tập dữ 
>  liệu) · tăng tải CPU khi truy vấn do phải chạy 2 thuật toán song song. 
>  Sự đánh đổi xứng đáng cho chất lượng Enterprise. "

α nên tỉ lệ nghịch với mật độ định danh 
 trong truy vấn

| Domain | Truy vấn điển hình | α gợi ý |
| --- | --- | --- |
| Chatbot FAQ, hỗ trợ khách hàng | Ngôn ngữ tự nhiên, khẩu ngữ, hầu như không có mã | 0,7 – 0,9 |
| Tra cứu chính sách nội bộ | Chủ yếu tự nhiên, đôi khi có số điều khoản | 0,6 – 0,7 |
| Hỗ trợ kỹ thuật có mã lỗi | Trộn: "app văng với lỗi ERR-X09" | 0,4 – 0,6 |
| Tra cứu code, log, luật | Tên biến, số điều, mã định danh | 0,2 – 0,4 |

Nhưng lưu ý điều mô-đun vừa cho thấy:

nhạy với outlier

dùng RRF

đã có

biết

Dense index

N × d × 4 byte

410 MB

Inverted index (BM25)

số token duy nhất

vài chục 
 MB

độ phức tạp vận hành

slide 69

tốt hơn

---

<!-- chiron-source-span: {"source_span_id":"2c45bd32-5619-51df-abf1-7bfc2c6e4c18","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 Rerank & MMR — kiến trúc hai giai đoạn","source_file":"slide-day08.html"},"checksum":"544db699754adbbbc2fa91fc7725d3ce030eaaf978ab70d20f15a91558df6dcf"} -->

## 09 Rerank & MMR — kiến trúc hai giai đoạn

Chương mạnh nhất của deck, và là phần [Ngày 7](slide-day07.html) chỉ chạm 
 qua. Nó trả lời hai câu hỏi tách biệt: *làm sao chọn đúng* (cross-encoder) và *làm sao chọn 
 không trùng* (MMR).

### Slide 73–75 Top-k không phải càng nhiều càng tốt, và kiến trúc hai giai đoạn

> Trích slide 
>  " k quá thấp (top-1, top-2): thiếu chứng cứ, recall kém. Sweet spot 
>  ( top-3 đến top-5 ): đủ chứng cứ, ít nhiễu. k quá cao (top-10 trở 
>  lên): context nhiễu, token lãng phí." 
>  " Mục tiêu của retrieval không phải là lấy nhiều, mà là lấy đúng và đủ cho generation. " 
>  "Retriever được thiết kế để quét qua hàng triệu tài liệu cực nhanh. Nó đánh giá sự liên quan một 
>  cách thô và rộng. Hệ quả: tài liệu đúng nhất có thể đang nằm ở Top 10, chứ 
>  không phải Top 1. " Ví dụ: query "Thủ tục xin visa" → Top 1: giá làm visa · 
>  Top 2: lịch sử visa · … · Top 8: các bước làm thủ tục. 
>  " Giai đoạn 1: Hybrid Search kéo nhanh Top 50–100. Nhanh nhưng 
>  nhiễu. Giai đoạn 2: đưa Top 50 qua Re-ranker để đọc kỹ và chấm điểm lại. Lấy 
>  Top 3–5 đưa cho LLM."

Ví dụ visa ở slide 74 là ví dụ giải thích toàn bộ lý do rerank tồn tại, và nó đáng phân tích kỹ:

độc lập

"Thủ tục xin visa"

giá làm visa

lịch sử visa

các bước làm thủ 
 tục

không thể

"thủ tục"

"các bước"

"giá"

nhìn cả hai cùng lúc

Slide 76

"gắn Query và Document thành một đoạn text 
 duy nhất (Query + [SEP] + Document), cho qua Transformer cùng lúc. Nhờ cơ chế Attention, model hiểu 
 chính xác sự tương tác giữa từng từ."

Nói cách khác:

|  | Giai đoạn 1 — Hybrid | Giai đoạn 2 — Rerank |
| --- | --- | --- |
| Chi phí mỗi ứng viên | Gần như 0 (tra index) | Một forward pass transformer |
| Phụ thuộc kích thước corpus | Có — nhưng ANN làm nó gần như hằng số | Không — chỉ phụ thuộc k₁ |
| Nên rộng hay hẹp | Rộng — mục tiêu là recall, đừng để sót | Hẹp — mục tiêu là precision |
| Ràng buộc | Latency của ANN, gần như miễn phí | k₁ × chi phí cross-encoder, và ngân sách token của k₂ |

Slide 77

Không bao giờ được dùng Reranker để quét toàn bộ database.

Ngày 7 · slide 71

một lần mỗi tài liệu

lặp lại mỗi truy 
 vấn

chỉ 4.545 truy vấn là khâu rerank đã tiêu hết ngân sách embed toàn bộ corpus 100M 
 token

Mô-đun phễu

giảm

### Slide 78–80 Redundancy, MMR, và khi nào dùng cái nào

> Trích slide 
>  "Re-ranker có thể đưa Top 3 tài liệu tốt nhất lên đầu. Nhưng nếu cả 3 tài liệu này đều sao 
>  chép nội dung của nhau thì sao? LLM sẽ tốn token vô ích mà không có thêm góc nhìn hay dữ kiện 
>  mới." Ví dụ: "Hoàn tiền mất 7 ngày." / "Tiền sẽ về sau 7 ngày." / "Thời gian xử 
>  lý hoàn tiền là 7 ngày." 
>  MMR: "thuật toán chọn lọc để tối đa hoá sự liên quan nhưng phạt nặng sự 
>  trùng lặp. Bước 1: chọn chunk liên quan nhất với Query. Bước 2: chọn chunk tiếp theo 
>  vừa liên quan Query, vừa có khoảng cách vector xa nhất so với chunk số 1." 
>  Maximize: [Similarity(Doc, Query)] − Penalty × [Similarity(Doc, Already_Selected)] 
>  " Cross-Encoder — dùng cho câu hỏi cần sự chính xác tuyệt đối 
>  (fact-checking, legal). MMR — dùng cho truy vấn mở, cần tổng hợp nhiều góc 
>  nhìn: 'Hãy tóm tắt các điểm rủi ro của dự án A từ tất cả các báo cáo'."

đúng

lượng thông tin

Ngày 7 · slide 35

"recall@k đo được có thể vẫn cao, nhưng lượng thông tin trong top-5 giảm năm 
 lần."

Ba tuyến phòng thủ, theo thứ tự nên làm:

Khử trùng lặp lúc index

idempotency qua hashing

MMR lúc chọn

ngữ nghĩa

Small-to-Big

Precision Focus → 
 Cross-Encoder

Diversity Focus → MMR

xếp chồng được

```text
Hybrid  ->  top-50        (rong, nhanh, muc tieu: RECALL)
   |
Cross-encoder rerank  ->  top-15   (cham diem lai, muc tieu: PRECISION)
   |
MMR chon tu 15         ->  top-5   (loai trung lap, muc tieu: DA DANG)
   |
Inject vao prompt
```

liên quan

bổ sung cho nhau

Khi nào thật sự phải chọn:

một

λ

MMR = λ·Sim(d, q) − (1−λ)·max Sim(d, đã chọn)

λ = 1

λ = 0

và có thể không 
 liên quan gì tới câu hỏi

λ ≈ 0,5–0,7

max

giống nhất

một

### Slide 81–82 Toàn cảnh pipeline retrieval, và gợi ý đóng gói thành Tool

> Trích slide 
>  Code: CohereRerank(top_n=3, model="rerank-multilingual-v3.0") bọc trong 
>  ContextualCompressionRetriever — "dùng Re-ranker as a Service là cách 
>  tiết kiệm tài nguyên hệ thống nhất." 
>  Toàn cảnh: " Query Transformation → Hybrid Search (k = 50) → Reranking (Cross-Enc/MMR) → 
>  Context (Top 5 Chunks) → LLM Generation. Gợi ý: ta có thể gói gọn pipeline này thành công cụ 
>  cho Agentic System (LangGraph) gọi tự động — Wrapped as an Agent Tool."

| Núm | Mặc định slide | Vặn lên thì | Vặn xuống thì |
| --- | --- | --- | --- |
| Bật/tắt query transform | Có điều kiện | Recall ↑, độ trễ +1s | Nhanh hơn, hỏng với câu hỏi mơ hồ |
| k₁ — shortlist | 50–100 | Recall ↑ (đến khi bão hoà), chi phí rerank ↑ tuyến tính | Rẻ hơn, dễ sót chứng cứ |
| k₂ — vào prompt | 3–5 | Ít sót hơn, nhưng nhiễu ↑ và lost-in-the-middle ↑ | Rẻ và sắc hơn, dễ thiếu chứng cứ |
| Cross-encoder / MMR | Tuỳ loại câu hỏi | — | — |

nó không đơn điệu

Mô-đun thứ ba

giảm

slide 73

một hàm Python

search_internal_docs(query: str) -> str

Slide 131

"LLM sẽ tự quyết định: à, câu hỏi này cần 
 luật nội bộ, mình sẽ gọi Tool này. Câu hỏi kia hỏi về thời tiết, mình sẽ không gọi."

Ngày 7 · slide 73

context engineering

"retrieval là một đòn bẩy, không phải toàn bộ 
 kiến trúc"

cấu trúc dữ liệu

ứng dụng RAG

một tool trong hệ multi-agent

---

<!-- chiron-source-span: {"source_span_id":"d394ee74-513f-5996-a09f-c24909964650","locator":{"kind":"html_section","section_id":"c10","order":12,"heading":"10 Context injection & Lost in the Middle","source_file":"slide-day08.html"},"checksum":"28c88bf401d0943f29daf9933e2f3ea4815391462c13ed5c46de9d785e4d834e"} -->

## 10 Context injection & Lost in the Middle

Toàn bộ chương này là nội dung **mới so với Ngày 7**, và nó chứa một thủ 
 thuật cụ thể đến bất ngờ: thứ tự nhồi chunk vào prompt là `[1, 3, 5, 4, 2]`.

### Slide 85–88 Hai pattern inject, và vì sao XML thắng

> Trích slide 
>  "Dù bạn tìm được tài liệu xuất sắc đến đâu, nếu không biết cách 'bơm' nó vào Prompt, LLM 
>  vẫn sẽ bị ảo giác … Không chỉ là nối chuỗi (text1 + text2). Cách bạn định 
>  dạng quyết định việc LLM có tôn trọng dữ liệu đó hay không." 
>  Pattern 1 — Pre-pending: "ghép tất cả các chunk thành một khối văn bản dài… Ưu: 
>  dễ code. Nhược: model không phân biệt được ranh giới giữa các tài liệu, làm mất giá trị 
>  Metadata. " 
>  Pattern 2 — XML Tags: "cách làm chuẩn Production… nhờ cấu trúc này, model 
>  dễ dàng nhận diện ID của tài liệu để làm trích dẫn (Citation)." 
>  <documents> 
>  <doc id="1" source="policy.pdf">... content document 1... </doc> 
>  <doc id="2">... content document 2... </doc> 
> </documents>

Sự khác biệt giữa hai pattern không phải thẩm mỹ. Nó quyết định **ba khả năng** mà 
 pattern 1 làm mất hoàn toàn:

| Khả năng | Pre-pending | XML tags | Vì sao |
| --- | --- | --- | --- |
| Trích dẫn | Không | Có | Model cần một định danh để trỏ tới. id="1" cho nó thứ đó |
| Giải quyết mâu thuẫn | Không | Có | Cần date trong thuộc tính để so "tài liệu nào mới hơn" 
 ( slide 108 ) |
| Nói "tôi không biết" | Khó | Dễ hơn | Ranh giới rõ giúp model nhận ra "không doc nào nói về X" thay vì trộn lẫn rồi suy diễn |
| Dễ code | Có | Cũng dễ — vài dòng f-string | — |

Không cần escape nội dung.

Thẻ đóng làm ranh giới rõ ràng.

---

##

</doc>

Thuộc tính mang metadata mà không chiếm dòng.

<doc id="3" source="policy.pdf" date="2026-01-15">

slide 34

"chunk tốt giữ source, section, date"

đến 
 được prompt

### Slide 89–91 Ngân sách token 20/60/20, Lost in the Middle, và thứ tự [1,3,5,4,2]

> Trích slide 
>  " Đừng nhồi tối đa Token chỉ vì model hỗ trợ. Càng nhiều context → càng chậm → 
>  càng đắt → càng dễ nhiễu. Phải chia ngân sách rõ ràng: 20% System Prompt/Rules, 60% 
>  Retrieved Context, 20% Headroom cho User Query và Output." 
>  " Lost in the Middle: LLM giống như con người, nó nhớ rất tốt thông tin nằm ở 
>  ĐẦU và CUỐI prompt, nhưng thường 'bỏ quên' thông tin nằm ở GIỮA nếu prompt 
>  quá dài. Nếu chunk chứa câu trả lời quan trọng nhất vô tình bị xếp ở giữa danh sách, RAG có 
>  thể thất bại." 
>  " Document Reordering: đừng ném nguyên Top K theo thứ tự 1, 2, 3, 4, 5. Sắp xếp 
>  lại theo mẫu luân phiên: đặt tài liệu tốt nhất ở đầu, tốt thứ 2 ở cuối, các tài liệu điểm 
>  thấp giấu vào giữa. Thứ tự đưa vào prompt: [1, 3, 5, 4, 2]."

Thủ thuật `[1, 3, 5, 4, 2]` nghe như mẹo vặt. Nó không phải — nó là hệ quả trực tiếp của 
 hình chữ U, và nó **miễn phí**: không thêm token, không thêm độ trễ, không thêm chi phí. 
 Chỉ là thứ tự khác khi ghép chuỗi.

```text
RANK tu reranker:   1     2     3     4     5
                    |     |     |     |     |
VI TRI trong prompt: 1     5     2     4     3
                  (dau) (cuoi) (thu2) (ap cuoi) (giua)

Doc theo vi tri:  [1] [3] [5] [4] [2]
                   ^           ^   ^
                   |           |   +-- rank 2 o CUOI (vung chu y cao)
                   |           +-- rank 4 o ap cuoi
                   +-- rank 1 o DAU (vung chu y cao nhat)

RANK 5 — tai lieu diem thap nhat — bi giau vao GIUA (vung bi bo quen)
```

đầu

cuối

tốt nhất

nên

Điều kiện để thủ thuật này có tác dụng:

Mô-đun tiếp theo

ρ

quy tắc ngón tay cái

đúng chắc chắn

phải chừa headroom

mô-đun k

k ≈ 5–6

2.000–2.400 token

1,9%

Kết luận thực dụng:

trần

mục tiêu

_Sơ đồ: Ngân sách token, hiệu ứng lost in the middle, và mẫu sắp xếp lại tài liệu - Phần trên là dải ngân sách token của slide tám mươi chín, chia ba phần: hai mươi phần trăm cho system prompt và luật, sáu mươi phần trăm cho context lấy về, hai mươi phần trăm dự phòng cho câu hỏi và câu trả lời. Phần giữa bên trái là đồ thị hình chữ U của slide chín mươi: trục ngang là vị trí trong prompt từ đầu tới cuối, trục dọc là mức độ model chú ý. Đường cong cao ở hai đầu và võng xuống ở giữa, nghĩa là thông tin đặt giữa prompt hay bị bỏ quên, và võng càng sâu khi prompt càng dài. Phần giữa bên phải giải thích mẫu sắp xếp lại của slide chín mươi mốt: tài liệu hạng một đặt ở đầu, hạng hai đặt ở cuối, hạng ba đặt ở vị trí thứ hai, hạng bốn đặt gần cuối, hạng năm là tài liệu điểm thấp nhất bị giấu vào giữa. Thứ tự đọc theo vị trí là một, ba, năm, bốn, hai. Dải cuối ghi rằng thủ thuật này miễn phí vì không thêm token cũng không thêm độ trễ, nhưng nó chỉ có tác dụng khi reranker thật sự tốt._

Hình 2 — Ngân sách token, hình chữ U, và mẫu sắp xếp lại.

slide 89, 90, 91

đặt chúng cạnh nhau

#### Tương tác k nhiều hơn có tốt hơn không? — kiểm "sweet spot top-3 đến top-5"

[Slide 73](#s73) khẳng định sweet spot là **top-3 đến top-5**, 
 và k ≥ 10 thì "context nhiễu" — không kèm số. Mô-đun này dựng mô hình từ ba thành phần mà chính deck 
 mô tả (recall bão hoà, hình chữ U của slide 90, nhiễu của slide 73) rồi tìm cực trị.

Mặc định: reranker tập trung ở mức **ρ = 0,55** · phạt "giữa" tối đa **55%** · mỗi chunk thừa gây nhiễu **4,5%** · chunk **400 
 token** · cửa sổ **16.000 token**.

Đoán trước: *(a)* k tối ưu là bao nhiêu? *(b)* ở k = 20 thì độ chính xác so với k = 
 5 thế nào? *(c)* sắp xếp lại theo `[1,3,5,4,2]` thêm được bao nhiêu?

#### Kéo rồi mở

**(a) k = 5, đạt 53,6%.** Mô hình được dựng từ ba cơ chế mà deck mô tả riêng lẻ, *không* được hiệu chỉnh để ra con số nào — và cực trị rơi đúng vào khoảng **top-3 đến top-5** mà slide 73 khẳng định. Đây là một xác nhận độc lập khá thuyết 
 phục cho một con số vốn không có nguồn.

**(b) k = 20 cho 34,3% — tệ hơn cả k = 2 (45,4%).** Đây là con số cụ thể hoá câu 
 "k quá cao → context nhiễu" của slide. 
 Nhìn ba cột trong bảng để thấy vì sao: R@k *vẫn tăng* (86,4% ở k = 20 so với 67,9% ở 
 k = 5), nhưng "không nhiễu" sụp từ 83,5% xuống 42,5%, và phạt "giữa" tăng từ 13,8% lên 31,4%. **Hai lực kéo xuống thắng một lực kéo lên.**

**(c) +1,5 điểm ở k = 5, và tối đa +2,2 điểm ở k = 10.** Nhưng con số thú vị hơn: **với sắp xếp lại, k tối ưu dịch từ 5 lên 6** và đạt 55,1%. 
 Nghĩa là thủ thuật miễn phí này không chỉ cho bạn thêm một chút chính xác — nó *nới rộng vùng an toàn*, cho phép nhồi thêm một chunk mà không bị phạt.

**Thử điều đáng thử nhất — kéo ρ từ 0,55 lên 0,95:** ρ cao nghĩa là reranker gần 
 như vô dụng (chứng cứ nằm ở hạng nào cũng như nhau). Lợi ích của việc sắp xếp lại **gần như biến mất**. 
 Đó là điều [Hình 2](#f2) ghi ở dải cuối và slide 91 không nói: *sắp xếp lại chỉ có giá trị khi thứ hạng mang thông tin.* Với retrieval chưa có reranker, 
 đừng kỳ vọng thủ thuật này giúp nhiều.

*Bài học vận hành:* ba núm vặn cho ba việc khác nhau. **Tăng k** chữa *thiếu chứng cứ*. **Rerank** chữa *chứng cứ bị chôn*. **Sắp xếp lại** chữa *lost-in-the-middle* — và nó miễn phí, nên gần như luôn 
 nên bật.

- **Control - k — số chunk nhồi vào prompt: 5 chunk**: min `1`, max `40`, step `1`, default `5`

- **Control - ρ — thứ hạng reranker tập trung đến đâu: 0,55**: min `10`, max `98`, step `1`, default `55`

- **Control - Phạt "giữa" tối đa: 55%**: min `0`, max `90`, step `5`, default `55`

- **Control - Nhiễu mỗi chunk thừa: 4,5%**: min `0`, max `150`, step `5`, default `45`

- **Control - Kích thước chunk: 400 token**: min `100`, max `1200`, step `50`, default `400`

- **Control - Cửa sổ context: 16.000 token**: min `4`, max `200`, step `4`, default `16`

Độ chính xác ở k hiện tại

—

—

k tối ưu

—

—

Sắp xếp lại thêm được

—

—

Context chiếm bao nhiêu cửa sổ

—

—

không sắp xếp lại có sắp xếp lại [1,3,5,4,2] k bạn đang chọn

#### Xem bảng: ba lực kéo ngược nhau theo k



#### Công thức & giới hạn của mô hình

- R(k) = 0,95 · k/(k+2) — recall bão hoà theo k. Lấy chứng cứ về càng nhiều càng 
 dễ, nhưng lợi ích giảm dần.
- P(chứng cứ ở hạng r) ∝ ρ^(r−1) — reranker tốt thì ρ nhỏ (chứng cứ hầu như ở hạng 
 1); ρ → 1 thì thứ hạng vô nghĩa.
- d(T) = d_max · T/(T + 6000) với T = k·chunkTok — phạt "giữa" nặng dần theo 
 độ dài prompt, đúng như slide 90 nói "nếu prompt quá dài".
- u(p, n) = 1 − d·4t(1−t), t = (p−1)/(n−1) — hình chữ U: bằng 1 ở hai 
 đầu, bằng 1−d ở chính giữa.
- nhiễu = exp(−μ·(k−1)) — mỗi chunk thừa là một chunk có thể lái model sai. Đây là 
 cách định lượng câu "context nhiễu" của slide 73.
- Giới hạn ① — bốn tham số là giả định của tài liệu này, không có trong slide. 
 Deck không cho con số nào về hình dạng hình chữ U, về mức nhiễu, hay về độ tập trung của reranker. 
 Chúng được chọn ở mức hợp lý và mô-đun cho bạn kéo để xem kết luận có bền không.
- Giới hạn ② — điều đáng tin không phải con số 53,6% mà là HÌNH DẠNG. Ba cơ chế 
 kéo ngược nhau ⇒ tồn tại cực trị trong. Cực trị đó nằm ở đâu thì phụ thuộc tham số; việc nó 
 tồn tại thì không.
- Giới hạn ③: mô hình giả định một chứng cứ duy nhất. Câu hỏi multi-hop cần 
 nhiều chứng cứ thì k tối ưu cao hơn — vì bạn cần nhiều chỗ hơn trong prompt.

---

<!-- chiron-source-span: {"source_span_id":"873b647d-d819-5b74-a4ee-6ec7e863dcc5","locator":{"kind":"html_section","section_id":"c11","order":13,"heading":"11 Grounding, UX, và ba lỗi generation","source_file":"slide-day08.html"},"checksum":"5adbbd1bec3ce7a4364d420169181b630242c48bc8b63e09c2c880ab8e521ac7"} -->

## 11 Grounding, UX, và ba lỗi generation

Phần 3 của deck, và nó là phần [Ngày 7](slide-day07.html) hoàn toàn không 
 có. Ba lỗi ở slide 108–110 đáng viết thành checklist.

### Slide 93–96 Grounding, bốn phần của prompt, và nghệ thuật nói "tôi không biết"

> Trích slide 
>  " Grounding là việc bắt buộc LLM chỉ được phép sử dụng thông tin từ 
>  context được cấp, nghiêm cấm dùng 'kiến thức học được từ Internet'. Mục tiêu: nếu 
>  đổi context sai, model cũng phải trả lời sai theo context đó. Trọng tài duy nhất là dữ liệu 
>  nội bộ." 
>  Bốn phần cốt lõi: " 1. Role — định hình nhân vật · 2. Task · 
>  3. Context · 4. Strict Constraints — quy tắc 'bàn tay sắt' (cấm 
>  bịa, bắt buộc trích dẫn)." 
>  " RAG mất đi 50% giá trị nếu model không chỉ ra được nó lấy câu trả lời từ dòng nào, tài 
>  liệu nào. " · "ALWAYS cite your sources using the <doc_id> provided." → 
>  "Nhân viên được nghỉ 12 ngày phép [doc_3]." 
>  "Đây là tính năng quan trọng nhất của RAG: biết giới hạn của mình. Nếu Top K 
>  chunks không chứa câu trả lời, model phải từ chối thay vì đoán mò." · 
>  "If the context does not contain the answer, reply EXACTLY with: 'Dữ liệu hiện tại không đủ để 
>  tôi trả lời câu hỏi này.' Do not attempt to guess."

Định nghĩa grounding ở slide 93 rất chặt và đáng nhớ vì nó cho ta một **phép kiểm thử** chứ không chỉ một khái niệm:

"Nếu đổi context sai, model cũng phải trả lời sai theo context đó."

model đang đọc 
 context

model đang dùng kiến thức có sẵn và tình cờ trùng

```text
TEST GROUNDING — 5 phut, khong can framework nao

1. Lay mot cau hoi ma model tra loi DUNG.
2. Sua context: doi mot con so quan trong thanh gia tri khac han
   (vd. "12 ngay phep" -> "27 ngay phep").
3. Hoi lai cung cau hoi do.

KET QUA:
  Model tra loi 27  -> GROUNDED. No dang doc context.
  Model tra loi 12  -> KHONG grounded. No dang doc TRI NHO cua no.
                       Prompt cua ban chua co hieu luc.
```

vốn đã biết

g

mô-đun phễu

g

"tính năng quan trọng nhất của RAG"

hữu ích

"reply EXACTLY with"

"Do not attempt to guess"

Ngày 5

false negative

false positive

Chi phí hai loại lỗi chênh nhau rất xa, nên ngưỡng phải lệch hẳn về phía từ chối.

ba

Kiểm chứng được

Chẩn đoán được

slide 11

Kiểm toán được

context injection dùng XML tags có id

chunk giữ được source từ lúc parse

Ngày 7 · slide 40

"không thể thêm sau"

Chuỗi phụ thuộc:

### Slide 97–99 Graceful degradation, CoT, và prompt template

> Trích slide 
>  "Thay vì chỉ nói 'Không biết' cụt lủn gây ức chế… hãy prompt để model gợi ý: 
>  'Tôi không tìm thấy chính sách này trong kho tài liệu HR năm 2026. Bạn có muốn tôi tìm 
>  kiếm rộng hơn hoặc liên hệ bộ phận nhân sự không? ' " 
>  BAD: "Tôi không biết." · GOOD: "Tôi chưa tìm thấy [X], nhưng bạn 
>  có thể thử hỏi lại với từ khoá [Y] hoặc tạo ticket cho IT." 
>  CoT: "yêu cầu model 'suy nghĩ ra nháp' trước khi in ra câu trả lời cuối… 'Đầu 
>  tiên, hãy lọc ra các câu liên quan trong context. Phân tích chúng trong thẻ 
>  <thought_process>.' Tăng độ chính xác đáng kể với câu hỏi so sánh hoặc suy luận 
>  logic."

| Thành phần | Ví dụ | Nó làm gì |
| --- | --- | --- |
| Phạm vi đã tìm | "trong kho tài liệu HR năm 2026" | Cho người dùng biết đã tìm ở đâu — nên họ biết chỗ nào chưa tìm |
| Lối đi tiếp | "thử lại với từ khoá [Y]" | Biến ngõ cụt thành một bước tiếp theo mà người dùng tự làm được |
| Đường thoát ra người thật | "tạo ticket cho IT" | Đảm bảo câu hỏi không chết ở đây |

fallback path

Ngày 5

low-confidence

Chi tiết quan trọng về phạm vi:

cam kết có thể sai

post-filter có thể âm thầm thu hẹp phạm vi

"Comparing doc A and B… Found conflict in dates… Reconciling…"

xung đột ngữ cảnh ở slide 108

real-time

Token output tăng

Độ trễ tăng

slide 105

Chiếm headroom

ngân sách slide 89

Dùng có chọn lọc:

quyết định bật/tắt query transformation

### Slide 101–105 UX quyết định độ tin cậy — bốn thành phần

> Trích slide 
>  "Người dùng doanh nghiệp không quan tâm bạn dùng MMR hay HNSW. Họ chỉ nhìn vào giao diện cuối 
>  cùng. Một khối text đặc chữ sẽ tạo cảm giác lười đọc và nghi ngờ. Cần thiết kế đầu 
>  ra có tính scannable." 
>  Inline citations: "giống Wikipedia… các ID này nên là hyperlink. 
>  Khi hover/click, popup ra đoạn text gốc để user đối chiếu nhanh." 
>  Source blocks: "ở cuối mỗi câu trả lời, tổng hợp lại danh sách tài liệu đã dùng… 
>  1. Chính sách bảo hành v4.0 (Tỷ lệ khớp: 92%) · 2. Ticket lỗi #8892 — Jira " 
>  Confidence tags: "nếu điểm số Re-ranker thấp: gán nhãn cảnh báo độ liên 
>  quan … ⚠ CẢNH BÁO ĐỘ TIN CẬY THẤP." 
>  Streaming: "hệ thống RAG chạy qua nhiều bước thường mất 3–5 giây, 
>  dễ làm user tưởng app bị treo. Hiển thị các bước đang chạy: Đang tìm kiếm trong kho HR… Đang đọc 
>  5 tài liệu… "

đưa nó ra cho người 
 dùng thấy

| Thành phần UX | Tín hiệu kỹ thuật đằng sau | Người dùng làm gì với nó |
| --- | --- | --- |
| Inline citation [1] | doc_id từ XML tags | Đối chiếu ngay tại chỗ, không rời màn hình |
| Source block cuối câu trả lời | Danh sách chunk đã inject + source | Đi sâu vào tài liệu gốc |
| "Tỷ lệ khớp: 92%" | Điểm reranker | Ước lượng nên tin tới đâu |
| ⚠ Cảnh báo độ tin cậy thấp | Điểm reranker dưới ngưỡng | Biết là cần kiểm lại — quản lý kỳ vọng |
| "Đang đọc 5 tài liệu…" | Trạng thái pipeline theo bước | Biết hệ thống chưa treo |

trust calibration

Ngày 5

Cái quan trọng nhất là cảnh báo độ tin cậy thấp

kiểm chứng nếu họ muốn

chủ động nói cho họ biết khi nào nên muốn

Ngày 7 · slide 20

"can yield arbitrary and meaningless similarities"

Hai cách làm an toàn hơn:

Đổi sang nhãn định tính

Chỉ hiện khi thấp

### Slide 107–111 Ba lỗi generation, và quy trình debug một dòng

> Trích slide 
>  " Good Context + Bad Prompt = Bad Answer " 
>  Lỗi 1 — Xung đột ngữ cảnh: "tài liệu A (2024) bảo nghỉ 12 ngày, tài liệu B (2026) 
>  bảo 14 ngày. LLM bị bối rối, có thể cộng gộp, báo lỗi, hoặc chọn bừa. Khắc phục: 
>  'nếu có mâu thuẫn, ưu tiên tài liệu có ngày cập nhật mới nhất, hoặc liệt kê cả 2 và chỉ ra sự mâu 
>  thuẫn'." 
>  Lỗi 2 — Over-extrapolation: "tài liệu ghi 'Miễn phí ship cho đơn trên 500k ở 
>  Hà Nội'. User hỏi 'Thế ở HCM thì sao?'. LLM tự suy diễn 'Hà Nội được thì HCM 
>  chắc cũng được' → ảo giác." 
>  Lỗi 3 — Ignored Constraints: "đã dặn model phải trích dẫn ID, nhưng model quên 
>  bẵng. Thường xảy ra với model nhỏ (8B) hoặc khi context quá dài. Khắc phục: 
>  đặt các rule quan trọng nhất ở CUỐI prompt (gần chữ Answer: nhất) · 
>  temperature = 0."

Slide 90

nếu prompt quá dài

Slide 91

tài liệu

cùng nguyên lý

luật

Answer:

"thường xảy ra khi context 
 quá dài"

Hệ quả cho cách bố trí prompt:

```text
[DAU]     Role + Task                       <- vung chu y cao
          Rules (ban day du)
          <documents>
            doc hang 1                       <- vung chu y cao
            doc hang 3
            doc hang 5                       <- vung bi bo quen
            doc hang 4
            doc hang 2                       <- vung chu y cao
          </documents>
          Question: {question}
          NHAC LAI 2 RULE QUAN TRONG NHAT     <- vung chu y cao NHAT
[CUOI]    Answer:
```

Answer:

suy luận của model là hợp lý

Lỗi 1

Lỗi 3

[doc_id]

Lỗi 2

không có dấu hiệu nào

"không tự ý suy luận các điều kiện không được đề cập rõ ràng"

①

trích dẫn cho từng mệnh đề

doc_id

②

"Nếu context chỉ nói về A mà người dùng hỏi về B, hãy trả lời: 'Tài liệu chỉ đề cập tới A; tôi 
 không có thông tin về B.'"

cụ thể

formatted_context

trước 
 tiên

Rẻ nhất.

print

Loại bỏ nhiều nhất.

Không có cách nào khác.

bốn câu chẩn đoán của Ngày 7

Hình 1

---

<!-- chiron-source-span: {"source_span_id":"0d830c5f-e22e-5b93-8c2c-62925890b264","locator":{"kind":"html_section","section_id":"c12","order":14,"heading":"12 Eval triad, A/B testing, và Lab 8","source_file":"slide-day08.html"},"checksum":"8e30c2b47ef994cea07c2b76afefaff936e125b628a6818e519bd5d4cf0b0cf1"} -->

## 12 Eval triad, A/B testing, và Lab 8

Phần 4 của deck. Nó đưa ra thứ mà [Ngày 7](slide-day07.html) chỉ gợi ý: 
 một **ma trận chẩn đoán** đọc được từ bảng điểm để biết phải sửa ở đâu.

### Slide 114–118 Vibe check không đủ, và bộ ba RAGAS

> Trích slide 
>  " Vibe check: nhập thử 3–5 câu hỏi, thấy mượt mà rồi kết luận Ready. 
>  Đây là cái bẫy chết người! Thay đổi nhỏ (ví dụ chunk 1000 → 500) có thể tốt cho 10 
>  câu này, nhưng lại làm hỏng 100 câu khác." 
>  "Không thể chấm điểm RAG bằng 1 con số duy nhất. Phải tách bạch lỗi do Retriever (tìm sai) 
>  hay lỗi do Generator (nói bậy). " 
>  Context Recall: "retriever có mang về đủ thông tin cần thiết không? Nếu 
>  câu hỏi cần 3 chứng cứ (A, B, C) nhưng chỉ tìm được A và B → Recall thấp." · Faithfulness: 
>  "câu trả lời có bám sát 100% vào tài liệu không? Nếu Context là 'A' mà LLM trả lời 'A + B', độ trung 
>  thực bị trừ điểm nặng." · Answer Relevance: "câu trả lời có đi thẳng vào vấn đề 
>  không? Đôi khi LLM trung thực với Context, nhưng Context lại không liên quan — dẫn 
>  đến câu trả lời 'đúng sự thật nhưng vô dụng'."

Ba metric này không ngang hàng — chúng đo ba mắt xích khác nhau, và **thứ tự chẩn đoán quan 
 trọng**:

| Metric | Đo mắt xích nào | Thấp thì sửa ở đâu | Tương ứng lỗi nào ở Hình 1 |
| --- | --- | --- | --- |
| Context Recall | Retriever | Chunking · hybrid · tăng k · query transform | Lỗi ① và ② |
| Faithfulness | Generator, cho trước context | Prompt grounding · ép citation · temperature = 0 | Lỗi ④ |
| Answer Relevance | Toàn hệ thống | Có thể là bất cứ đâu — dùng nó như chỉ báo tổng, không phải chẩn đoán | Lỗi ③ hoặc lỗi hiểu ý định |

"Thời gian bảo hành của sản phẩm A?"

"Sản phẩm A này rất tốt và có màu xanh."

hoàn hảo

mỗi metric chỉ đóng một cửa

overfit vào test set nhỏ

slide 120

Ngày 5

70%–97%

tune theo

Ngưỡng thực dụng:

Ngày 7 · slide 76

không cần nhãn tay, trong một buổi

### Slide 119–121 LLM-as-a-Judge và Golden Dataset

> Trích slide 
>  "Làm sao tính được 3 điểm số trên tự động cho hàng nghìn câu hỏi? Con người không thể ngồi 
>  đọc tay. Sử dụng một LLM 'Thầy Giáo' ( phải là model rất mạnh ) để đọc và 
>  chấm điểm LLM 'Học Sinh'." 
>  Golden Dataset: "chuẩn bị File Excel/CSV chứa khoảng 50–100 mẫu thử cực 
>  tốt. Cột bắt buộc: Question · Ground Truth · Contexts. Phải bao gồm đa dạng 
>  các loại câu hỏi: câu hỏi đánh đố · câu hỏi mơ hồ · câu hỏi KHÔNG CÓ trong tài liệu."

"Câu hỏi không có trong tài liệu"

khả năng nói "tôi không biết"

tính năng quan trọng nhất của RAG

có

Tỉ lệ đề xuất:

ground truth

đo được

Ngày 5

low-confidence

① Giám khảo cũng hallucinate.

sinh

② Thiên vị theo phong cách.

③ Không ổn định giữa các lần chạy.

temperature = 0

Cách dùng đúng:

so sánh tương đối

giá trị tuyệt đối

slide 123

### Slide 123–125 Cô lập biến số, case study hybrid, và ma trận chẩn đoán

> Trích slide 
>  " Nguyên tắc sống còn: chỉ thay đổi MỘT biến số trong mỗi lần thử nghiệm. Nếu bạn 
>  vừa đổi kích thước chunk, vừa đổi thuật toán Hybrid, vừa đổi System Prompt → không biết chính xác yếu 
>  tố nào mang lại thành công." 
>  Case study: chuyển từ thuần Dense sang Hybrid — " Context Recall tăng vọt 
>  từ 60% lên 90% (vì bắt được các mã lỗi chính xác). Kéo theo Faithfulness tăng." 
>  Ma trận chẩn đoán: " Recall Cao + Faithfulness Thấp: tìm đúng tài 
>  liệu nhưng model bị ảo giác → Sửa Generation. Recall Thấp + Faithfulness 
>  Cao: hệ thống đang ngoan ngoãn nói 'tôi không biết' vì không tìm thấy tài liệu → 
>  Sửa Indexing/Retrieval."

slide 18

lỗi nằm ở đâu?

Recall thấp + Faithfulness cao

đang hoạt động đúng

Đây là hệ thống trung thực nhưng vô dụng

Hình 3

hướng

độ lớn

Slide 57–60

0% recall

gần 100%

Nhưng đừng trích con số này như một kỳ vọng.

Cách duy nhất để biết là đo

_Sơ đồ: Ma trận chẩn đoán Context Recall và Faithfulness, cùng cổng chặn deploy - Bên trái là ma trận hai chiều. Trục ngang là Context Recall từ thấp tới cao, trục dọc là Faithfulness từ thấp tới cao. Ô dưới bên trái, recall thấp và faithfulness thấp, là hỏng toàn hệ thống, phải sửa cả hai. Ô dưới bên phải, recall cao nhưng faithfulness thấp, nghĩa là tìm đúng tài liệu mà model vẫn bịa, phải sửa prompt grounding, ép trích dẫn và hạ temperature về không. Ô trên bên trái, recall thấp nhưng faithfulness cao, nghĩa là hệ thống trung thực nói không biết vì không tìm thấy tài liệu, phải sửa chunking và retrieval. Ô trên bên phải, cả hai đều cao, là trạng thái sẵn sàng cho production. Bên phải là bộ ba RAGAS gồm Context Recall đo retriever, Faithfulness đo generator, Answer Relevance đo toàn hệ thống, và ghi chú rằng mỗi metric đóng một cửa nên bỏ một metric là để hở một cửa. Dải cuối mô tả cổng CI của slide một trăm hai mươi bảy: đẩy code, build, chấm điểm bằng LLM giám khảo, và chặn deploy nếu Faithfulness dưới tám mươi phần trăm._

Hình 3 — Ma trận chẩn đoán, bộ ba RAGAS, và cổng chặn deploy.

slide 125

việc phải làm

### Slide 126–127 ROI của rerank, và cổng chặn deploy

> Trích slide 
>  "Cross-encoder Reranker giúp tăng Answer Relevance thêm 5%. Nhưng nó làm thời 
>  gian phản hồi tăng từ 1s lên 4s, và chi phí Server tăng gấp đôi 
>  ( $500/month extra ). Bài toán của Kỹ sư trưởng: 5% độ chính xác đó có đáng giá với 
>  trải nghiệm chậm chạp của người dùng không? " 
>  "Code RAG không giống code Web. Khi đẩy lên Production, bạn không test hàm/logic, bạn test 
>  'Hành vi của AI'. Hãy tích hợp vòng lặp RAGAS vào GitHub Actions. Nếu điểm số 
>  Faithfulness < 80%, hệ thống tự động block lệnh Deploy. "

chi phí

khoản tiết kiệm

Ngày 7 · mô-đun kinh tế

generation chiếm 
 86,9%

giảm k

60% chi phí generation

lớn hơn

Phát biểu đầy đủ hơn của bài toán:

trả lại

mô-đun k

chất lượng cũng tăng

Phần slide nói đúng và không thay đổi:

độ trễ 1s → 4s là chi phí thật

hệ thống bắt buộc

Ngày 5

với eval set nhỏ, con số đo được có khoảng tin cậy rộng.

chặn nhầm

cho qua nhầm

Ba cách làm cổng chặn tốt hơn:

So với baseline, không so với hằng số.

Dùng cận dưới của khoảng tin cậy

Đủ mẫu.

LLM-as-a-judge

temperature = 0

### Slide 129–137 Từ RAG sang Agent, Lab 8, và khung tuning năm câu hỏi

> Trích slide 
>  "RAG truyền thống là luồng một chiều: nhận câu hỏi → tìm 1 lần → trả lời. Hạn 
>  chế: RAG không biết làm toán phức tạp và không thể tự động tìm kiếm thông tin bên ngoài. " 
>  " RAG: LLM là 'cái miệng' — tổng hợp thông tin đã được mớm sẵn. AGENT: LLM 
>  là 'bộ não' — Reasoning Engine: tự lập kế hoạch, quyết định công cụ và thực hiện vòng lặp." 
>  "Toàn bộ module Retrieval khổng lồ ta vừa học hôm nay sẽ được đóng gói lại thành một hàm 
>  Python đơn giản: search_internal_docs(query: str)." 
>  Khung tuning năm câu hỏi: "1. Index sạch chưa? 2. Retrieve đúng chưa? dense-only 
>  có đang miss keyword hay alias không? 3. Có cần rerank không? top-k hiện tại có trùng lặp nhiều 
>  không? 4. Prompt có grounded không? model có biết từ chối khi thiếu chứng cứ không? 5. Eval 
>  có nói thật không? testset đã đủ các câu khó và câu mơ hồ chưa? "

Hình 1

| Câu hỏi | Kiểm bằng cách nào | Chương |
| --- | --- | --- |
| 1. Index sạch chưa? | Mở chunk ra đọc bằng mắt; kiểm NFC, khử trùng lặp, metadata | 03, 04 |
| 2. Retrieve đúng chưa? | Chạy BM25 làm sàn; thử truy vấn có mã định 
 danh | 07, 08 |
| 3. Có cần rerank không? | Nhìn top-k: có bao nhiêu chunk nói cùng một điều? | 09 |
| 4. Prompt có grounded không? | Đổi context sai xem model có sai theo 
 không | 11 |
| 5. Eval có nói thật không? | Test set có câu không có đáp án không? | 12 |

nếu eval không nói thật thì bốn câu trên vô 
 nghĩa

"1. Index bộ tài liệu domain nhỏ với metadata rõ ràng. 2. Build baseline retrieval + answer 
 function. 3. Thử hybrid hoặc rerank ở mức tối thiểu. 4. Tạo 10 test questions với expected evidence. 
 5. Chấm kết quả theo scorecard trước và sau tuning."

"Không cần build hệ thống phức tạp. Điều quan trọng là chứng 
 minh được vì sao bản tuning tốt hơn baseline."

đo trước khi sửa

slide 123

Một lưu ý về con số 10:

slide 120

slide 114

làm quen quy trình

công thức no-labels của Ngày 7

---

<!-- chiron-source-span: {"source_span_id":"abe506af-1bb5-5c33-abc9-eef7c46db0c9","locator":{"kind":"html_section","section_id":"ladder","order":15,"heading":"▤ Luyện kỹ năng cốt lõi: đọc bảng điểm để biết sửa ở đâu","source_file":"slide-day08.html"},"checksum":"cbc06c62f0e32bdb15563b3006abc9e90c940e4be8092c4ad194d43d2539c201"} -->

## ▤ Luyện kỹ năng cốt lõi: đọc bảng điểm để biết sửa ở đâu

Ba bài giảm dần giàn giáo. Kỹ năng được luyện là kỹ năng Lab 8 chấm: *chứng minh được vì sao bản tuning tốt hơn baseline*.

print(formatted_context)

② Đọc ma trận Recall × Faithfulness

Hình 3

③ Sửa MỘT biến

slide 123

④ Đo lại trên CÙNG bộ câu hỏi

temperature = 0

#### Trợ lý tra cứu chính sách nội bộ. Người 
 dùng hỏi "Nghỉ phép năm được bao nhiêu ngày?" — bot trả lời "Nhân viên được nghỉ 12 ngày 
 phép." Nhưng chính sách 2026 đã đổi thành 14 ngày

Đọc cách *khoanh vùng*, không chỉ đáp án.

1. Bước ① — in context ra, và đọc kỹ CẢ HAI khả năng. 
 Nếu context chỉ chứa bản 2024 (12 ngày): đây là lỗi retrieval hoặc lỗi 
 data — bản 2026 có trong index không? Kiểm bằng id. Nếu không có, lỗi ở ingestion; 
 nếu có mà không lọt top-k, lỗi ở retrieval. 
 Nếu context chứa CẢ HAI bản (12 và 14 ngày): retrieval đã làm đúng việc của nó — nó 
 mang về cả hai. Đây là lỗi 1 của slide 108: xung đột ngữ cảnh. Sang bước 2. 
 Giả sử context chứa cả hai.
2. Bước ② — xác định ô trên ma trận, và ở đây nó cho một kết quả tinh tế. 
 Context Recall cao — chứng cứ đúng (bản 2026) có trong top-k. 
 Faithfulness cao — câu trả lời "12 ngày" có trong context, model không 
 bịa gì. 
 Cả hai metric đều đẹp, mà câu trả lời vẫn sai. 
 Đây là chỗ ma trận 2×2 không đủ, và nó đáng biết: xung đột ngữ cảnh rơi vào ô 
 "production ready" nhưng vẫn cho câu trả lời sai. Metric bắt được nó là 
 Answer Relevance hoặc — trung thực hơn — chấm tay.
3. Bước ③ — sửa một biến, và có ba lựa chọn xếp theo thứ tự rẻ dần. 
 a) Prompt (rẻ nhất): thêm luật của slide 108 — 
 "Nếu các tài liệu mâu thuẫn, ưu tiên tài liệu có date mới nhất, và nêu rõ có mâu 
 thuẫn." Đặt luật này ở CUỐI prompt, gần Answer:. 
 Điều kiện bắt buộc: chunk phải mang trường date và nó phải 
 đến được prompt qua thuộc tính XML. Không có nó thì luật này vô nghĩa. 
 b) Retrieval: thêm filter status = "hiệu lực" — bản 2024 không bao 
 giờ được retrieve. Sạch hơn, nhưng cần metadata đúng cho toàn corpus. 
 c) Index (sạch nhất): xoá hẳn bản hết hiệu lực khỏi index. Đây là 
 data debt theo đúng định nghĩa của Ngày 6 — và 
 Ngày 7 · slide 40 đặt "khử trùng lặp và bản hết hạn" vào bước chuẩn 
 hoá sau parse. 
 Chọn (a) trước vì nó rẻ và phản hồi nhanh, nhưng ghi (b) và (c) vào backlog — 
 (a) chỉ là băng dán.
4. Bước ④ — đo lại, và đo đúng thứ. Test set phải có ít nhất 3–5 câu hỏi mà kho 
 tài liệu có nhiều phiên bản. Nếu golden dataset không có loại câu hỏi này, bản sửa của bạn 
 không được kiểm — và bạn sẽ tin nhầm rằng nó hoạt động. 
 Đây là câu hỏi thứ 5 trong khung tuning slide 136: 
 "Eval có nói thật không?"
5. Ghi lại theo mẫu — phần này mới là phần được chấm ở Lab 8. 
 FAILURE CASE #1 
 Trieu chung: tra loi "12 ngay" trong khi chinh sach 2026 la 14 ngay 
 Buoc (1): context CHUA CA HAI ban -> khong phai loi retrieval 
 Ma tran: Recall CAO + Faithfulness CAO -> ma van sai 
 (xung dot ngu canh khong hien tren ma tran 2x2) 
 Nguyen nhan: slide 108 loi 1 — prompt khong co luat uu tien theo date 
 Sua MOT bien: them luat uu tien date, dat o CUOI prompt 
 Do lai: 5 cau hoi da phien ban, truoc/sau 
 Ket qua: 1/5 -> 5/5 dung 
 No con lai: ban 2024 van nam trong index (data debt) — backlog 
 Dòng "Nợ còn lại" là dòng phân biệt một kỹ sư với một người vá lỗi: bạn biết mình vừa dán 
 băng, và bạn ghi lại chỗ cần mổ.

#### Bạn chạy scorecard trên 60 câu hỏi. 
 Kết quả: Context Recall 91% · Faithfulness 62% · 
 Answer Relevance 71%. Sếp hỏi: sửa gì trước, và mất bao lâu?

Gợi ý ở mỗi bước; hãy tự viết trước khi mở đáp án.

1. Bạn đang ở ô nào trên ma trận? 
 Gợi ý: Hình 3, hai trục là Recall và Faithfulness.
2. Recall 91% mà Faithfulness chỉ 62% — điều đó nói gì về retrieval? 
 Gợi ý: retrieval đang làm tốt việc của nó. Vậy vấn đề nằm ở đâu?
3. Ba việc sửa được, xếp theo chi phí? 
 Gợi ý: slide 117 nêu ba cách khắc phục Faithfulness thấp.
4. Vì sao Answer Relevance (71%) nằm giữa hai con số kia? 
 Gợi ý: nó đo toàn hệ. Nếu một nửa câu trả lời bịa thêm, độ trọng tâm bị ảnh hưởng thế nào?
5. Sau khi sửa, bạn kỳ vọng con số nào tăng và con số nào KHÔNG đổi? 
 Gợi ý: sửa generation thì retrieval có thay đổi gì không?

#### Đối chiếu sau khi đã tự viết

**① Ô "Có chứng cứ mà vẫn bịa"** — góc dưới bên phải: Recall cao, Faithfulness thấp. 
 Chỉ dẫn của [slide 125](#s123): **sửa Generation**.

**② Retrieval đang tốt và đừng đụng vào nó.** Recall 91% nghĩa là 9 trên 10 câu hỏi 
 có chứng cứ đúng trong top-k. Mọi công sức bỏ vào hybrid, rerank, chunking lúc này sẽ cho lợi ích 
 rất nhỏ — bạn đang ở gần trần của tầng đó. 
 Đây chính là chỗ [con số 80/20 của slide 18 KHÔNG áp dụng](#s18). Nó là quy tắc mặc 
 định khi chưa biết gì; khi đã có bảng điểm, bảng điểm thắng.

**③ Ba việc, theo chi phí tăng dần (slide 117):** 
 **a) `temperature = 0`** — một tham số, hiệu lực ngay, không tốn gì. 
 Làm đầu tiên. 
 **b) Ép trích dẫn** — thêm luật *"mọi tuyên bố phải kèm [doc_id]"* và đặt nó [ở cuối prompt](#s108). Việc này vừa tăng faithfulness vừa cho bạn công cụ chẩn đoán: 
 câu nào không có citation là câu model đang bịa. 
 **c) Siết system prompt** — thêm mẫu câu từ chối cụ thể, thêm luật chống [over-extrapolation](#s108). 
 Cả ba đều là *prompt engineering*, đều làm trong một buổi. Đó là câu trả lời cho "mất bao 
 lâu".

**④ Answer Relevance nằm giữa vì nó chịu ảnh hưởng của cả hai tầng.** Retrieval tốt 
 kéo nó lên; bịa thêm kéo nó xuống. 71% là hợp lý cho Recall 91% + Faithfulness 62%. 
 Và nó là lý do [slide 115](#s114) nói không thể chấm RAG bằng một con số: nếu chỉ nhìn 
 Answer Relevance 71%, bạn không biết sửa ở đâu. Phải tách ra mới chẩn đoán được.

**⑤ Kỳ vọng sau khi sửa:** 
 · **Faithfulness tăng mạnh** — đây là thứ bạn đang sửa trực tiếp. 
 · **Answer Relevance tăng vừa** — ít bịa hơn thì trọng tâm hơn. 
 · **Context Recall KHÔNG đổi** — bạn không đụng gì tới retrieval. 
 **Và điểm mấu chốt: nếu Context Recall thay đổi, bạn đã đổi nhiều hơn một biến.** Đó là dấu hiệu vi phạm nguyên tắc slide 123, và bạn phải tìm ra mình đã vô tình đổi gì. 
 Con số không đổi là *bằng chứng* rằng thí nghiệm sạch — đừng bỏ qua nó.

#### Lấy pipeline RAG của chính bạn. Dựng golden 
 dataset ≥ 50 câu có đủ ba loại, chạy scorecard, định vị mình trên ma trận, sửa một biến, đo 
 lại

Không có đáp án — nhưng có bảng tự chấm.

≥ 50 câu

câu hỏi KHÔNG có đáp án trong kho

câu hỏi chứa mã định danh

câu hỏi mà kho có nhiều phiên bản

date

BM25 thuần làm sàn

test grounding

ô nào

MỘT biến

temperature = 0

không liên quan

không đổi

---

<!-- chiron-source-span: {"source_span_id":"fa2597f2-d3ee-5219-a38d-09a0a540ca8d","locator":{"kind":"html_section","section_id":"misc","order":16,"heading":"✕ 6 hiểu lầm phổ biến","source_file":"slide-day08.html"},"checksum":"9bd76bab4560a58ca73a404c9ac98c4ab1c0e57478e007821ab089a70d6d5f17"} -->

## ✕ 6 hiểu lầm phổ biến

Hai cái đầu là hai phản xạ sai phổ biến nhất khi debug RAG; bốn cái sau là những chỗ 
 deck nói đúng nhưng dễ bị đọc quá tay.

"RAG trả lời sai — chắc prompt chưa đủ tốt, hoặc cần model lớn hơn. Sửa prompt trước đã."

Slide 18

"sai lầm"

80% lỗi thuộc phía retrieval

generation bị chặn trên bởi retrieval

mô-đun phễu

đã được chăm sóc

print(formatted_context)

Hình 1

"Nhồi nhiều chunk vào prompt thì an toàn hơn — nhỡ chứng cứ nằm ở chunk thứ 8 thì sao. Model 
 context 128K mà, cứ cho k = 20."

Slide 73

top-3 đến top-5

Mô-đun k

k = 5

k = 20, độ chính xác 34,3% — tệ hơn cả k = 2 (45,4%)

phạt "giữa"

slide 90

nhiễu

rerank

"Hybrid search chỉ cần cộng điểm cosine với điểm BM25 rồi xếp hạng. Nếu lo lệch thang đo thì 
 chuẩn hoá min-max về [0,1] là xong."

Slide 65

BM25 không có giới hạn 
 trên

Mô-đun RRF

cũng không cứu được

RRF k = 60

thứ hạng

không đổi chút 
 nào

Ngày 7 · slide 69

"Faithfulness cao nghĩa là hệ thống tốt. Nếu model bám sát context 95% thì gần như xong rồi."

Ma trận slide 125

Recall thấp + Faithfulness cao

"hệ thống đang ngoan ngoãn nói tôi không biết vì không tìm thấy tài 
 liệu"

trung thực nhưng vô dụng

Slide 115

"Đã có prompt bảo 'chỉ trả lời dựa trên tài liệu được cung cấp' rồi thì model đã grounded. Không 
 cần kiểm thêm."

Slide 93

kiểm được

"nếu đổi context sai, 
 model cũng phải trả lời sai theo context đó."

vốn đã biết

g

mô-đun phễu

"Reranker làm hệ thống chậm và đắt gấp đôi để đổi lấy 5% chất lượng — theo slide 126 thì đó là 
 một đánh đổi đáng ngờ."

chi phí

khoản nó tiết kiệm

Ngày 7 · mô-đun kinh tế

generation chiếm 86,9%

mô-đun k

tăng

không phải tiền

độ trễ: 1s → 4s

"người dùng có chịu được thêm 3 giây không"

---

<!-- chiron-source-span: {"source_span_id":"ad8f481a-31a5-5c55-b0ef-d34080da3a3d","locator":{"kind":"html_section","section_id":"apply","order":17,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-day08.html"},"checksum":"b7fd25fb7b181c781acfb9ad10a99eb9bc4791428adced539256bd564f8a969d"} -->

## ◆ Áp dụng vào SmartCheck AI

Ngày 7 dựng tầng dữ liệu cho SmartCheck: 8.000 chunk, 32,8 MB, exact search, recall 
 100%. Ngày 8 xây tiếp thành một RAG hoàn chỉnh — và kết quả cho thấy **con số 80/20 của slide 18 
 KHÔNG áp dụng ở đây**.

### ① Chạy phễu ba tầng với tham số của SmartCheck

Ngày 7 kết luận corpus SmartCheck đủ nhỏ để dùng **exact search** — recall của tầng 1 
 rất cao. Đưa vào [mô-đun phễu](#m-funnel): R1 = 92%, k₁ = 50, k₂ = 4, reranker q = 85%, 
 model bám context g = 90%:

|  | Hybrid (BM25 + dense) | Dense-only | Chênh |
| --- | --- | --- | --- |
| Recall@k₁ của tầng 1 | 92,0% | 70,4% | −21,6 điểm |
| Đúng end-to-end | 71,4% | 54,6% | −16,8 điểm |
| Quy lỗi — retrieval | 27,9% | 65,2% |  |
| Quy lỗi — rerank | 44,4% | 21,4% |  |
| Quy lỗi — generation | 27,7% | 13,4% |  |
| Phía tìm kiếm / generation | 72,3% / 27,7% | 86,6% / 13,4% | slide 18 nói 80/20 |

① Bỏ BM25 làm mất 16,8 điểm độ chính xác end-to-end.

30% truy vấn của khách chứa mã booking

làm nhoè token chính xác

70,4%

nghịch lý enterprise của slide 62

"nếu bỏ BM25, hệ thống sẽ thất bại thảm hại."

② Với hybrid, tỉ lệ lỗi là 72/28, không phải 80/20 — và nút thắt là RERANK.

Quy lỗi lớn nhất là rerank: 44,4%.

không phải

cải thiện reranker hoặc nới k₂

Bài học tổng quát:

chưa biết gì

### ② k tối ưu cho SmartCheck

Chunk của SmartCheck ngắn hơn ví dụ chung (300 token thay vì 400 — chính sách và FAQ khách sạn viết 
 ngắn), và reranker chạy trên corpus hẹp nên tập trung hơn (ρ = 0,45). Chạy [mô-đun k](#m-topk):

| k | Token context | Không sắp xếp lại | Có sắp xếp lại |
| --- | --- | --- | --- |
| 3 | 900 | 51,1% | 51,6% |
| 4 | 1.200 | 53,6% | 54,6% |
| 5 | 1.500 | 54,6% ← tối ưu | 55,8% |
| 6 | 1.800 | 54,5% | 55,9% ← tối ưu |
| 8 | 2.400 | 52,9% | 54,5% |

top-3 đến top-5

slide 73

1.500–1.800 token

khoảng 1,3%

slide 89

60% là trần, không phải mục tiêu

Việc rẻ nhất nên làm ngay:

[1,3,5,4,2]

không token nào, không mili-giây nào

### ③ Prompt grounding cho kiosk — và một ràng buộc đặc thù

```text
<role>
Ban la tro ly check-in cua khach san. Tra loi NGAN GON — khach dang dung
truoc kiosk, khong ai doc mot doan van dai tren man hinh cham.
</role>

<documents>
  <doc id="1" source="noiquy_danang.pdf" property="DN" date="2026-01-10">...</doc>
  <doc id="2" source="faq_checkin.pdf"   property="ALL" date="2025-11-02">...</doc>
</documents>

Cau hoi: {question}

<rules>   <!-- dat o CUOI, gan Answer: nhat — slide 110 -->
1. Chi dung thong tin trong <documents>. Khong dung kien thuc ngoai.
2. Moi tuyen bo phai kem [doc_id].
3. Neu cac doc mau thuan: uu tien doc co date MOI NHAT, va noi ro co mau thuan.
4. Neu context chi noi ve co so khac (property khac): tra loi
   "Noi quy nay la cua co so khac. Toi khong co thong tin cho co so nay."
5. Neu khong tim thay: "Toi chua tim thay thong tin nay. Ban co the hoi le tan
   tai quay, hoac bam nut goi ho tro." — KHONG doan.
6. Toi da 3 cau. Khach dang dung.
</rules>

Answer:
```

Slide 109

"miễn phí ship cho đơn 
 trên 500k ở Hà Nội"

"Hà Nội được thì HCM chắc cũng được"

đúng cấu trúc rủi ro đó, nhân với sáu cơ sở

lối thoát cụ thể

property

provenance được giữ từ lúc parse

Và tuyến phòng thủ tốt hơn nằm ở tầng dưới:

property_id

không bao giờ

Slide 101

khách đang đứng, có người xếp hàng phía sau, màn hình cảm ứng

Câu trả lời phải rất ngắn

[1]

bắt model sinh ra

ẩn nó khỏi giao diện

Streaming quan trọng hơn nhiều.

Slide 105

bài toán ROI của slide 126

với kiosk có người đứng chờ, đó có thể là lý do đủ để 
 bỏ rerank

### ④ Golden dataset cho SmartCheck — bốn loại câu hỏi bắt buộc

| Loại | Ví dụ | Kiểm cái gì | Tỉ lệ |
| --- | --- | --- | --- |
| Tra cứu thường | "Mấy giờ được nhận phòng?" | Đường cơ bản | ~40% |
| Có mã định danh | "Đơn HN-2291-XL của tôi" | Nhánh BM25 — bỏ loại này thì không phát hiện được việc thiếu hybrid | ~25% |
| Nhầm cơ sở | Khách ở Đà Nẵng hỏi điều chỉ có trong nội quy Hà Nội | Luật 4 + pre-filter — chống over-extrapolation | ~15% |
| Không có đáp án | "Khách sạn có bể bơi nước nóng không?" (không có 
 trong kho) | Khả năng nói "tôi không biết" — slide 96 gọi 
 là tính năng quan trọng nhất | ~20% |

[1,3,5,4,2]

② Thêm nhánh BM25

71,4% và 54,6%

③ Dựng golden dataset 60 câu theo bốn loại trên

công thức no-labels của Ngày 7

④ Chạy test grounding

g

⑤ Chỉ sau đó mới cân nhắc reranker

sau khi

Chú ý thứ tự:

slide 18

---

<!-- chiron-source-span: {"source_span_id":"d017bb41-f764-5a68-af3b-a1c299b8b3e0","locator":{"kind":"html_section","section_id":"numbers","order":18,"heading":"# Con số cần kiểm chứng","source_file":"slide-day08.html"},"checksum":"2af2c3ff455690a17edd136b63c683c46234b0446cf9d5b78401d28a9b6ad05c"} -->

## # Con số cần kiểm chứng

Ngày 8 khác Ngày 7 ở một điểm quan trọng: **gần như không con số nào của deck 
 có nguồn**. Mục này tách rõ ba loại và ghi cách kiểm từng cái.

Ngày 7

bác bỏ sáu con số sai

80/20

60% → 90%

+5% Answer Relevance

$500/tháng

ngưỡng 80%

20/60/20

"mất 50% giá trị"

Điều đó không có nghĩa chúng sai.

đứng vững

đừng trích chúng như sự thật đã được đo

| Con số | Nguồn | Cần kiểm gì |
| --- | --- | --- |
| 80% lỗi do Retrieval / 20% do Generation | Của slide (18) — không có nguồn | Mô-đun phễu: 80/20 tương ứng R1 ≈ 75%, reranker q ≈ 94–95%, g = 90%. Hợp 
 lý, nhưng là ảnh chụp một hệ thống đã chăm sóc. Kéo g xuống 70% thì phần generation nhảy lên 
 36,3%. Với SmartCheck, tỉ lệ là 72/28 và nút thắt là rerank |
| Sweet spot top-3 đến top-5 · k ≥ 10 gây nhiễu | Của slide (73) — không nguồn | Mô-đun k dựng mô hình từ ba cơ chế deck mô tả riêng lẻ và tìm cực trị ở 
 k = 5. Xác nhận độc lập. Nhưng bốn tham số của mô hình là giả định của tài liệu 
 này — điều đáng tin là hình dạng (tồn tại cực trị trong), không phải con số 53,6% |
| RRF: tài liệu top cao ở CẢ 2 bảng lên số 1 · k = 60 | Của slide (66) — k = 60 là mặc định trong paper gốc Cormack et al. | Mô-đun RRF kiểm trên 8 tài liệu: D3 (hạng 3 dense + hạng 2 BM25) thắng D1 
 (hạng 1 + hạng 5) và D7 (hạng 7 + hạng 1). Khẳng định đúng. Tám tài liệu là ví dụ 
 do tài liệu này dựng, không phải đo thật |
| Context Recall 60% → 90% khi chuyển sang hybrid | Của slide (124) — không dataset, không corpus | Hướng và độ lớn khớp với BEIR mà Ngày 7 dẫn. Nhưng mức tăng phụ thuộc hoàn toàn vào tỉ 
 lệ truy vấn có định danh. Với FAQ thuần tự nhiên, hybrid có thể gần như không giúp. 
 Đừng trích như kỳ vọng |
| Rerank: +5% Answer Relevance, 1s → 4s, $500/tháng | Của slide (126) — không nguồn | Slide chỉ tính chi phí, không tính khoản tiết kiệm. Ngày 7 cho thấy generation chiếm 86,9% chi 
 phí tháng, và rerank cho phép giảm k → cắt vào dòng lớn nhất. 
 Đánh đổi thật là độ trễ, không phải tiền |
| Ngân sách token 20 / 60 / 20 | Của slide (89) — quy tắc ngón tay cái | Nguyên tắc "phải chừa headroom" thì đúng chắc chắn. Nhưng 60% là trần, không phải mục 
 tiêu: mô-đun k cho thấy tối ưu chỉ dùng 1.500–2.400 token |
| Cổng CI chặn deploy nếu Faithfulness < 80% | Của slide (127) | Ý tưởng đúng, ngưỡng cứng thì rủi ro. Với eval set 50 câu, khoảng tin cậy rộng khiến điểm dao 
 động quanh 80% giữa các lần chạy. So với baseline thay vì so với hằng số |
| Golden dataset 50–100 mẫu · overlap 10–15% · 
 shortlist 50–100 → top 3–5 | Của slide (120, 31, 75) | Đều là quy tắc ngón tay cái hợp lý. Ngày 5 tính ra rằng dưới 50 mẫu thì khoảng tin cậy quá rộng 
 để so sánh hai cấu hình — nên 50 là sàn, không phải mục tiêu |
| SmartCheck: 71,4% với hybrid so với 54,6% dense-only · 
 quy lỗi 27,9 / 44,4 / 27,7 · k tối ưu 5 (6 khi sắp xếp lại) | Tính ra từ mô hình, với giả định của tài liệu này: R1 = 92%, 
 30% truy vấn có mã booking, dense đạt 20% trên nhóm đó, chunk 300 token, ρ = 0,45 | Tỉ lệ 30% truy vấn có mã booking là ước lượng, chưa đo. Nhưng kết luận 
 "bỏ BM25 mất hai chữ số điểm phần trăm" bền vững với mọi tỉ lệ trên 15% |
| Chunk size=1000, overlap=150 (code mẫu slide 41) | Của slide | Overlap 15% khớp khuyến nghị. Nhưng 1000 lớn hơn khoảng 512–1024 mà Ngày 7 dẫn từ Bhat et al., 
 và gấp 8–15 lần khoảng 64–128 tối ưu cho câu hỏi factoid. Đây là điểm khởi đầu để chạy 
 được, không phải khuyến nghị đã đo |

139 trang

thứ tự trang PDF (1–139)

tiêu đề slide

---

<!-- chiron-source-span: {"source_span_id":"dbe1079a-407a-56a2-b821-5f155b235034","locator":{"kind":"html_section","section_id":"cheat","order":19,"heading":"▣ Cheat sheet ôn thi","source_file":"slide-day08.html"},"checksum":"096b0596efb911ae2239785891718d07cad492d03d9c73589489c2b2da14f02c"} -->

## ▣ Cheat sheet ôn thi

Những thứ nên nhớ được mà không cần mở lại tài liệu.

không phải

print(formatted_context)

Chứng cứ CÓ trong context → lỗi generation. KHÔNG → 
 lỗi retrieval.

| Danh sách | Các mục | Slide |
| --- | --- | --- |
| 3 pipeline của RAG | Indexing (offline) · Retrieval (real-time) · Generation (real-time) | 14 |
| Pipeline retrieval đầy đủ | Query Transform → Hybrid k₁=50 → Rerank/MMR → Context k₂=3–5 → LLM | 82 (+ Hình 1 ) |
| 4 kỹ thuật query transform | Expansion · Decomposition · Step-Back · HyDE | 46–50 |
| 4 phần của prompt RAG | Role · Task · Context · Strict Constraints | 94 |
| 3 lỗi generation | Xung đột ngữ cảnh · Over-extrapolation · Ignored constraints | 108–110 |
| Bộ ba RAGAS | Context Recall (retriever) · Faithfulness (generator) · Answer Relevance (toàn hệ) | 115 (+ Hình 3 ) |
| 5 câu hỏi tuning | Index sạch? · Retrieve đúng? · Cần rerank? · Prompt grounded? · Eval có nói thật? | 136 |

```text
① RRF — gop theo THU HANG, khong theo diem
   RRF(d) = 1/(k + rank_dense) + 1/(k + rank_sparse),   k = 60
   -> mien nhiem voi do lon diem. Thuong cho tai lieu tot o CA HAI bang.

② ALPHA TUNING — gop theo diem da chuan hoa
   Score = α · norm(dense) + (1−α) · norm(sparse)
   FAQ: α = 0,7–0,9    |    Code/Log/Luat: α = 0,2–0,4
   -> nhay voi outlier. Chi dung khi da co eval set de tune.

③ MMR — chon vua lien quan vua da dang
   max [ Sim(d, q) ]  −  λ · [ max Sim(d, da_chon) ]
   λ ≈ 0,5–0,7.  Luu y: max, khong phai trung binh.

④ NGAN SACH TOKEN
   20% system prompt  |  60% context (TRAN, khong phai muc tieu)  |  20% headroom

BA CON SO:
   k₁ = 50–100  (shortlist qua reranker)
   k₂ = 3–5     (vao prompt) — toi uu theo mo hinh: k = 5, hoac 6 neu sap xep lai
   thu tu nhoi = [1, 3, 5, 4, 2]  — mien phi, luon nen bat
```

|  | Context Recall THẤP | Context Recall CAO |
| --- | --- | --- |
| Faithfulness CAO | Trung thực nhưng vô dụng — nói "tôi không biết" → SỬA RETRIEVAL | Sẵn sàng production → chuyển sang tối ưu chi phí |
| Faithfulness THẤP | Hỏng toàn hệ → SỬA CẢ HAI, bắt đầu từ retrieval | Có chứng cứ mà vẫn bịa → SỬA PROMPT: grounding · citation · temp = 0 |

Lỗ hổng của ma trận:

"RAG trả lời sai, sửa gì trước?"

print(formatted_context)

một

"Vì sao cần hybrid?"

"Vì sao RRF chứ không cộng điểm?"

"k bao nhiêu là đủ?"

"Làm sao biết model có grounded không?"

"Rerank có đáng không?"

| Chủ đề | Ngày 8 | Ngày 7 | Nên theo |
| --- | --- | --- | --- |
| Pre-filter | "nhanh hơn, an toàn hơn, chính xác tuyệt đối " | "đúng, nhưng suy biến về brute-force "; và có lựa chọn thứ ba: in-algorithm | Ngày 7 — kèm quan sát thật trên pgvector |
| Dense cần hạ tầng chuyên dụng | "yêu cầu Vector Database và ANN" | "dưới 10k vector: 30 MB, <10 ms, bỏ qua vector DB" | Ngày 7 — có phép tính cụ thể |
| Mask PII | "trước khi đưa lên Cloud Vector DB" | embedding đảo ngược được — mask trước khi embed, bất kể lưu ở đâu | Ngày 7 — có paper (Morris EMNLP 2023, ALGEN 2025) |

Quy tắc chung khi hai nguồn mâu thuẫn:

quan sát cụ thể hoặc phép 
 tính

---

<!-- chiron-source-span: {"source_span_id":"05532c23-7602-5043-8c9a-34caaa289c1f","locator":{"kind":"html_section","section_id":"gloss","order":20,"heading":"☰ Từ điển thuật ngữ","source_file":"slide-day08.html"},"checksum":"7ac0fa73fcb4cd893b05ff187a89bf6a5fb8e44cc46f7d6203079675100f0937"} -->

## ☰ Từ điển thuật ngữ

Định nghĩa theo cách dùng được trong bài thi và trong công việc.

---

<!-- chiron-source-span: {"source_span_id":"166ba5d2-b1f8-5afa-9e46-5ad6885b8ea5","locator":{"kind":"html_section","section_id":"bloom","order":21,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-day08.html"},"checksum":"e0d825d6fab23160dbefd6bc54081bd55537ed10b6d7779621a97ed72b013f31"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab 8 kiểm tra mức 3–4; câu hỏi cuối deck 
 kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 3 pipeline, 4 kỹ thuật query transform, 4 phần prompt RAG, 3 lỗi generation, bộ ba 
 RAGAS, và 5 câu hỏi tuning. | Cheat sheet · Hình 1 |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao không cộng thẳng cosine với BM25 được, và vì sao 
 cross-encoder chính xác hơn bi-encoder nhưng không dùng để quét cả DB. | Slide 65 · slide 76 · mô-đun RRF |
| 3 · Áp dụng | Dựng golden dataset ≥ 50 câu đủ bốn loại, chạy scorecard, và viết prompt grounding có đủ luật 
 trích dẫn, luật ưu tiên theo ngày, và câu từ chối cụ thể. | Slide 120 · slide 94–96 · mục SmartCheck ③ |
| 4 · Phân tích | Cho một bảng điểm (Recall 91%, Faithfulness 62%), định vị được ô trên ma trận, nói được sửa gì 
 và metric nào phải không đổi sau khi sửa. | Hình 3 · Bài 2 · slide 125 |
| 5 · Đánh giá | Nhìn một con số trong deck (80/20, 60%→90%, +5% relevance) và nói được nó có nguồn không, 
 áp dụng trong điều kiện nào, và có áp dụng cho hệ thống của bạn không. | Con số cần kiểm chứng · mô-đun phễu |
| 6 · Sáng tạo | Nhận ra rằng với hệ thống của bạn, nút thắt không nằm ở chỗ deck nói — và chứng minh 
 được bằng số. Ví dụ: với SmartCheck, quy lỗi lớn nhất là rerank 44,4%, không phải 
 retrieval. | Mục SmartCheck ① |

①

print(formatted_context)

②

③

không có đáp án trong kho

slide 114

"đang thiếu một pipeline retrieval và evaluation đủ kỷ luật"
