---
schema_version: 1
course_id: rag-intensive
document_id: "914f77bb-c2bb-5330-a68d-2a457ac2d815"
document_version_id: "f6e0fdb2-2e93-5fdc-b02b-45f4323b95e4"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Data Pipeline & Data Observability — phân tích & breakdown từng slide"
source_file: "slide-day10.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-day10.html"
source_sha256: "db6b8542ba5045c75446072411bb041c0fab5f353fd7a34abbc36bb5bc9cf233"
parser_version: chiron-structured-markdown-v1
html_section_count: 21
interactive_module_count: 3
interactive_control_count: 18
language: vi
---

# Data Pipeline & Data Observability — phân tích & breakdown từng slide

> 50 slide, và luận đề của deck nằm gọn trong một dòng ở slide 28: 
 "nhiều lỗi nhìn giống model hallucination nhưng gốc rễ thực ra là data pipeline bug." 
 Đây là bài duy nhất trong Foundation nói rằng vấn đề bạn thấy ở model thường không ở model. Tài liệu 
 này tái lập con số định lượng duy nhất của deck — "8 giờ, 500 users" ở slide 32 — rồi 
 tính hai thứ deck chỉ cảnh báo bằng lời: một dòng insert thay vì upsert làm 
 một nửa kho vector thành rác sau bao nhiêu ngày, và gate thứ năm trong năm 
 quality gate có đáng thêm không.

<!-- chiron-source-span: {"source_span_id":"17c3caeb-fce1-50af-a23b-e97db1eadb34","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-day10.html"},"checksum":"32f151026d0965535c8e7fe4c85ba754390f662752c5b7c0161c84f4b093d5dc"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Ngày 10 đứng ở một vị trí lạ trong Foundation: nó là bài **duy nhất nói rằng ba bài trước có 
 thể đã sai địa chỉ**. [Ngày 7](slide-day07.html) dạy chọn index và đo recall, [Ngày 8](slide-day08.html) dạy rerank và đo faithfulness, [Ngày 9](slide-day09.html) dạy chia vai và đọc trace. Cả ba đều giả định *dữ liệu trong kho là đúng*. Slide 28 của Ngày 10 
 nói thẳng rằng giả định đó hay sai, và khi nó sai thì mọi phép đo ở ba bài kia đều đo nhầm thứ.

model hallucination

data pipeline bug

Ngày 9 · slide 64

"status: ok chỉ có nghĩa là bước này không 
 văng exception."

Ngày 7

"'không lỗi' không có nghĩa là 'đúng'."

triệu chứng xuất hiện xa nơi nguyên nhân 
 nằm

không một phép đo 
 nào ở ba bài trước phát hiện được

8 giờ

500 users

Mô-đun 3

nếu có một cron job kiểm freshness mỗi giờ thì còn bao nhiêu 
 người?

63

8,5 lần

Con số cần kiểm chứng

**Ba đường đọc, tuỳ bạn có bao nhiêu thời gian:**

| Bạn có | Đọc gì | Bỏ được gì |
| --- | --- | --- |
| 30 phút | Chương 06 (6 chiều + 5 gate) · chương 08 (5 trụ) · 
 Hình 2 · cheat sheet | Chương 03, 10, 11 — công cụ, thay đổi theo năm |
| 2 giờ | Thêm ba mô-đun và ba Mini-Quest. Đây là phần đắt nhất về mặt hiểu và rẻ nhất về mặt thời gian | Bảng so sánh tool ở chương 01 và 11 — tra khi cần |
| Nửa ngày | Đọc tuần tự, và làm Bài 2 trên pipeline thật của bạn | Không bỏ gì |

"Fivetran mua Census + sáp nhập dbt 
 Labs; Datadog mua Metaplane"

"Helicone đã bị Mintlify mua (03/2026), giờ chỉ 
 maintenance mode"

hết hạn nhanh nhất trong cả bài

không

hình dạng của bài toán

---

<!-- chiron-source-span: {"source_span_id":"7a3796b2-79eb-5bbe-a2dc-97aef5d025e8","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu — vì sao 80% công việc nằm ở data","source_file":"slide-day10.html"},"checksum":"c2a271d00aba75bb95f266dd964a96cf61267402cfaa06d22fcaa3f0aaddd028"} -->

## 00 Mở đầu — vì sao 80% công việc nằm ở data

Hai slide đầu đặt ra một câu hỏi mà phần lớn người học AI chưa từng phải trả lời: *làm sao bạn biết dữ liệu đã sai?*

### Slide 2 · 4 Câu hỏi mở bài, và tỷ lệ 80/20

> Trích slide 
>  " Agent của bạn dùng data từ database công ty. Đột nhiên data sai — agent hallucinate. 
>  Bạn có biết không? " 
>  " 60–80% thời gian trong AI project thực tế là data work — không phải model · 
>  một agent RAG xuất sắc vẫn hallucinate nếu vector store được nạp data bẩn · 
>  Garbage in → garbage out: quality của output tỷ lệ thuận với quality của input 
>  data · Observability = cơ chế phát hiện data sai trước khi user phàn nàn " 
>  "Thực tế dự án AI: 20% — xây model/agent · 80% — data collection, cleaning, pipeline, 
>  monitoring "

Câu hỏi mở bài kết thúc bằng ba chữ *"Bạn có biết không?"* — và đó là ba chữ mang toàn bộ 
 trọng lượng của bài. Không phải "data có sai không" (chắc chắn có lúc sai), mà **bạn có cơ chế để biết không**.

|  | Hệ có observability | Hệ không có |
| --- | --- | --- |
| Ai phát hiện data sai | Alert | Khách hàng |
| Phát hiện sau bao lâu | Phút | Giờ tới ngày |
| Bao nhiêu người bị ảnh hưởng | Vài chục | 500 (slide 32) |
| Debug bằng gì | Trace ngược về source doc | Đoán, và thường đoán là "model kém" |
| Kết luận rút ra | "Ingestion run 2 giờ sáng fail" | "Chắc phải đổi sang model xịn hơn" |

model kém

không cái nào chạm tới nguyên nhân

"tiếc thật, giá mà được 
 làm model nhiều hơn."

80% thời gian nằm ở data vì đó là nơi 80% kết quả được quyết 
 định.

là

Sculley et al. (2015), "Hidden Technical Debt in 
 Machine Learning Systems"

nhỏ nhất

---

<!-- chiron-source-span: {"source_span_id":"29b9b7ca-da29-5089-8f99-531e81ffbba8","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Pipeline fundamentals & AI data stack","source_file":"slide-day10.html"},"checksum":"f015d1fd4fd6d6df9fdbca853f5f4821fb24cfd8b7c3ba4bfd6cbd2587ba2274"} -->

## 01 Pipeline fundamentals & AI data stack

Chương này có một slide đáng học và một slide sẽ hết hạn trong mười hai tháng. Đáng 
 học là [slide 8](#s8) — nó nói pipeline cho AI khác pipeline cho BI ở chỗ nào.

### Slide 6 · 7 Năm tầng của AI data stack, và bảng tool 2026

> Trích slide 
>  " Data Pipeline — chuỗi các bước tự động hoá việc thu thập, xử lý, và phân phối 
>  data từ nguồn đến đích." 
>  AI Data Stack điển hình: " Sources → Pipeline → Storage → Serving → Agent · 
>  Sources: DB, API, files, streams · Pipeline: ingest + transform · Storage: warehouse, vector store · 
>  Serving: API, cache layer · Agent: LLM + tools + RAG" 
>  Bảng tool 2026: "Ingestion — Airbyte/Fivetran (managed) + Debezium (CDC, chuẩn mở) · 
>  Storage — Lakehouse: S3/GCS + Iceberg hoặc Delta Lake · Transform — dbt (+ Fusion engine mới, viết 
>  lại bằng Rust) · Orchestration — Airflow 3.0 (event-driven scheduling) hoặc Dagster (asset-centric, 
>  lineage sẵn có) · Observability — Monte Carlo/Elementary + OpenLineage (chuẩn interop bên 
>  dưới) " 
>  " Fivetran mua Census + sáp nhập dbt Labs; Datadog mua Metaplane — thị trường đang gộp lại 
>  quanh vài platform lớn. "

vai trò

| Vai trò | Nó trả lời câu hỏi gì | Bỏ nó thì hỏng ra sao |
| --- | --- | --- |
| Ingestion | Data vào bằng đường nào, và biết nó vào chưa? | Tài liệu mới không tới agent — agent trả lời bằng bản cũ |
| Storage | Giữ raw ở đâu để còn replay được? | Không backfill được khi đổi chiến lược chunking |
| Transform | Làm sạch, chunk, gắn metadata ở đâu? | Chunk xấu, thiếu metadata — retrieve nhầm, cite sai |
| Orchestration | Ai chạy các bước, theo thứ tự nào, khi nào? | Chạy tay, quên chạy, chạy trùng |
| Observability | Làm sao biết một trong bốn cái trên 
 hỏng? | Khách hàng là người báo cho bạn |
| Activation | Đẩy ngược kết quả về CRM/hệ nghiệp vụ | Không hỏng gì — đây là hàng tuỳ chọn, deck cũng ghi "optional" |

Chú ý hàng thứ năm.

bạn không biết là mình đang 
 thiếu

"OpenLineage (chuẩn interop bên dưới)"

Helicone bị Mintlify mua

chuẩn

MCP ở Ngày 9

nó tách quyết định "ghi gì" khỏi quyết 
 định "dùng tool nào để đọc"

### Slide 8 Pipeline cho AI khác pipeline cho BI ở đâu — slide quan trọng nhất chương này

> Trích slide 
>  Luồng: " Docs (Notion/PDF) → Ingest (sync/OCR) → Transform (clean/chunk) → Index 
>  (embed/store) → Retrieve (top-k) → Agent (answer) " 
>  "Nếu ingestion fail: tài liệu mới không vào store → agent trả lời cũ · 
>  nếu transform sai: chunk xấu, metadata thiếu → retrieve nhầm · nếu 
>  index lỗi: embed thiếu hoặc duplicate → context méo " 
>  "Điểm khác với dashboard BI: BI sai → số sai trên báo cáo. Agent sai → hành động hoặc trả 
>  lời sai trực tiếp với user. Vì vậy pipeline cho AI cần thêm: chunking, metadata, 
>  embeddings, retrieval checks, trace logs."

tốc độ

vòng lặp phát hiện 
 dài bao lâu

|  | Dashboard BI sai | Agent sai |
| --- | --- | --- |
| Ai nhìn thấy đầu tiên | Một analyst, người có bối cảnh | Khách hàng, người không có bối cảnh |
| Họ có nghi ngờ không | Có — "số này trông lạ" | Không — câu trả lời trôi chảy và tự tin |
| Có hành động ngay không | Không — báo cáo được xem lại | Có — user làm theo, hoặc agent gọi tool |
| Sửa xong thì thiệt hại còn không | Gần như không | Còn — người đã hành động rồi |

Ngày 9 · Mini-Quest 3

hoàn toàn bịa

lấp đầy ô trống

trace logs

biết

_Sơ đồ: Sáu bước của pipeline AI, ba điểm gãy, và bảng ánh xạ lỗi dữ liệu sang triệu chứng của agent - Hàng trên là sáu bước nối tiếp nhau: tài liệu nguồn, ingest đồng bộ và OCR, transform làm sạch và chia chunk, index tạo embedding và lưu, retrieve lấy top-k, và agent trả lời. Ba bước ở giữa được đánh dấu là điểm gãy: ingestion hỏng thì tài liệu mới không vào kho nên agent trả lời bằng bản cũ; transform sai thì chunk xấu và thiếu metadata nên retrieve nhầm; index lỗi thì embedding thiếu hoặc trùng nên context bị méo. Phần dưới là bảng năm hàng ánh xạ từ lỗi dữ liệu sang triệu chứng quan sát được ở agent: thiếu tài liệu dẫn tới không tìm thấy bằng chứng liên quan; bản cũ dẫn tới trả lời theo chính sách hết hiệu lực; chunk trùng dẫn tới lặp lại cùng một ý nhiều lần; metadata sai dẫn tới trích dẫn sai phòng ban hoặc sai ngày hiệu lực; và rò rỉ bí mật dẫn tới làm lộ dữ liệu nhạy cảm cho người dùng. Dòng cuối nhấn mạnh rằng cả năm triệu chứng này đều dễ bị chẩn đoán nhầm thành model hallucination, trong khi gốc rễ nằm ở pipeline dữ liệu._

Hình 1 — Sáu bước, ba điểm gãy, và năm triệu chứng.

slide 8

slide 28

hai nửa của cùng một bảng

---

<!-- chiron-source-span: {"source_span_id":"1c7af583-39e6-5c5f-8bfa-d4affcc4c001","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Mini-Quest 1 — ETL hay ELT?","source_file":"slide-day10.html"},"checksum":"f2870e888817ab4d14a1eeaf51a4f74671fa352b3621664e382ac3dbead11d67"} -->

## 02 Mini-Quest 1 — ETL hay ELT?

Deck cho 8 phút tự nghĩ trước khi lật đáp án. Nếu bạn đang đọc một mình, hãy dừng ở 
 đây thật — phần thưởng của Mini-Quest nằm ở chỗ bạn *sai trước* rồi mới đọc.

### Slide 9 Đề bài

> Trích slide 
>  " ETL và ELT khác nhau ở đâu? Mỗi loại thường dùng công nghệ/tool gì? Khi nào bạn sẽ chọn 
>  ETL, khi nào chọn ELT cho một hệ thống AI/agent? " 
>  "Cá nhân — 8 phút tự tìm hiểu/nhớ lại + 1–2 bạn chia sẻ. Gợi ý nếu bí: nghĩ theo hướng 
>  'transform trước hay sau khi lưu'. "

transform trước khi lưu

mất

lưu raw rồi mới transform

nhận

### Slide 10 · 11 · 12 Đáp án — và vì sao AI team thường không chọn một trong hai

> Trích slide 
>  ETL (Extract → Transform → Load): "transform trước khi load vào kho · 
>  phù hợp: data nhạy cảm, cần mask trước khi lưu · ví dụ: redact PII trong ticket 
>  support trước khi embed cho agent · tools: Talend, Informatica, custom scripts" 
>  ELT (Extract → Load → Transform): "load raw data, transform sau trong 
>  kho · phù hợp: big data, cloud data warehouses · ví dụ: load raw docs/logs trước, rồi chunk 
>  + enrich trong lakehouse · tools: Spark SQL, BigQuery, custom Python jobs" 
>  Chọn ETL nếu: "cần mask PII trước · schema khá ổn định · data đi vào agent phải rất sạch · muốn 
>  giảm rủi ro lưu raw nhạy cảm" · Chọn ELT nếu: "nhiều nguồn, nhiều định dạng · 
>  phải backfill/replay thường xuyên · còn đang thử chunking, labeling, 
>  feature engineering · cần giữ raw cho audit và experiment" 
>  " Thực tế: nhiều team dùng hybrid — load raw trước, nhưng ETL các phần nhạy cảm như PII, 
>  secrets, dữ liệu pháp lý trước khi index hoặc serve cho agent. "

|  | ETL — transform trước | ELT — transform sau |
| --- | --- | --- |
| Bạn giữ được gì | Kho luôn sạch, không chứa thứ không nên chứa | Bản raw — replay và backfill được |
| Bạn mất gì | Không quay lại được — đổi cách chunk phải đi lấy lại 
 từ nguồn | Kho chứa cả thứ nhạy cảm, phạm vi rủi ro rộng hơn |
| Đắt ở đâu | Mỗi lần đổi logic = một lần re-ingest toàn bộ | Lưu trữ (rẻ) + kỷ luật quản trị truy cập (không rẻ) |
| Hợp với giai đoạn | Logic đã ổn định | Còn đang thử nghiệm |

Với một hệ RAG đang xây, gần như luôn là ELT

Ngày 8

còn

"load raw trước, nhưng ETL các phần nhạy cảm như PII, secrets, dữ liệu pháp lý 
 trước khi index."

chỉ

pháp lý và bảo mật

"cái gì mà việc lưu bản raw của nó tự nó đã là rủi ro"

---

<!-- chiron-source-span: {"source_span_id":"cd319db3-7832-5760-b46b-dc36bb4ece35","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Batch, streaming & schema registry","source_file":"slide-day10.html"},"checksum":"2118dbd8f61c6cd1bad13e2d2f4cc07d0577e74e074345842d949aef73ef5b1f"} -->

## 03 Batch, streaming & schema registry

Chương ngắn, và điểm đáng học không nằm ở bảng so sánh Kafka mà ở một câu về *vì sao data quality cho stream khác hẳn cho batch*.

### Slide 13 · 14 Batch so với streaming, và cái bẫy của quality check trên stream

> Trích slide 
>  Batch: "xử lý theo lô, theo lịch · ưu: đơn giản, cost thấp, dễ 
>  debug · nhược: latency cao · dùng khi: training data, daily reports, ETL" · 
>  Streaming: "xử lý realtime · ưu: latency thấp (ms–giây) · nhược: phức tạp hơn, cost 
>  cao hơn · dùng khi: fraud detection, live agent context " 
>  Data quality cho streaming: " Schema Registry: chặn event sai format 
>  ngay lúc ingest, không đợi batch check · Flink/ksqlDB: viết rule kiểm tra 
>  realtime — giá trị bất thường, thiếu ID, volume spike · Khác batch: không thể chạy Great 
>  Expectations suite hàng đêm trên stream vô hạn " 
>  " Case study thật: Grab Engineering dùng FlinkSQL để convert data contracts thành rule 
>  kiểm tra realtime — chạy production, không phải lý thuyết. "

cổng đứng sau

|  | Batch | Streaming |
| --- | --- | --- |
| Check chạy khi nào | Sau khi có đủ dữ liệu | Lúc từng record đi qua |
| Check được cái gì | Cả thống kê tập hợp — null rate, row count delta, phân phối | Chỉ từng record, cộng cửa sổ trượt |
| Sai thì làm gì | Fail cả run, chưa có gì bị nhiễm | Record hỏng đã đi tiếp — cần dead-letter queue |
| Sửa rồi chạy lại | Được — data còn đó | Chỉ được nếu có lưu raw (lại là ELT ) |

Hàng cuối là hàng nối ngược về Mini-Quest 1.

tài liệu nguồn của bạn đổi bao nhiêu lần mỗi ngày?

thừa

Mô-đun 1

tần suất sync có ảnh hưởng tới tốc độ tích rác hay không phụ thuộc vào việc bạn có 
 incremental sync hay không.

tốc độ đổi tài liệu

đúng cùng một kết quả

tần suất 
 sync

một giờ

slide 17

---

<!-- chiron-source-span: {"source_span_id":"4b64f384-6315-5ec0-a3cc-f29e4100e226","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Ingestion — và cái bẫy idempotency","source_file":"slide-day10.html"},"checksum":"479fb7f5be47717fcea45b229294c2edbab91c0b33fc36b163439657fe2354a0"} -->

## 04 Ingestion — và cái bẫy idempotency

Chương này chứa hai gạch đầu dòng nằm cạnh nhau ở [slide 17](#s17) mà deck 
 trình bày như hai thói quen tốt độc lập. Mô-đun 1 cho thấy chúng **nhân với nhau**, và 
 khoảng cách giữa "có cả hai" và "không có cái nào" là ba bậc độ lớn.

### Slide 16 Ba nhóm nguồn, và CDC

> Trích slide 
>  Structured: "Databases (PostgreSQL, MySQL): CDC để capture changes · 
>  Data warehouses: Snowflake, BigQuery · REST/GraphQL APIs: rate limits cần xử lý " · 
>  Unstructured: "Files: CSV, JSON, Parquet, PDF, Word · Object storage: S3, GCS · 
>  Web scraping" · Event streams: "Kafka/Kinesis · Webhooks · IoT sensors" 
>  " CDC — Change Data Capture — detect & capture mọi INSERT/UPDATE/DELETE trong 
>  database để sync realtime thay vì full scan. Debezium (build trên Kafka Connect) là 
>  tool mã nguồn mở chuẩn phổ biến nhất."

"mọi INSERT/UPDATE/DELETE"

bỏ quên cái thứ ba

thu hồi

không

Mô-đun 1

không xoá

Đối sách rẻ nhất:

source_doc_id

### Slide 17 · 18 Ba yêu cầu thiết kế, và checklist bốn câu

> Trích slide 
>  Thiết kế ingestion tốt cần: " Incremental sync: chỉ lấy phần changed since last 
>  run · Idempotent upsert: chạy lại không tạo duplicate chunks · 
>  Source versioning: biết bản nào mới nhất, sync lúc nào" 
>  " Rate limiting: source API giới hạn req/min → cần exponential backoff · 
>  Backpressure: consumer xử lý chậm hơn producer · Retry logic: 
>  dead-letter queue cho failed records" 
>  " Thực tế AI: 1 file sync fail có thể khiến policy mới không tới agent. " 
>  Checklist ingestion cho AI: "1. Có lấy đúng nguồn không? 2. Có lấy đủ bản mới 
>  nhất không? 3. Có biết record nào thất bại không? 4. Có log được 
>  run ID và thời gian sync không?"

"record nào 
 thất bại"

"run ID"

chủ động ghi chúng lại lúc chạy

khả năng quan sát phải được quyết định lúc bạn viết bước ingest

chương 09

sau

không tạo ra bất kỳ tín hiệu 
 nào

status: success

Ngày 9 · slide 64

"status: ok chỉ có nghĩa là 
 bước này không văng exception."

đúng là

Cái sửa được:

trụ Volume

#### Tương tác Mô-đun 1 — Idempotency: kho vector mục ruỗng nhanh cỡ nào?

[Slide 17](#s17) đặt *"incremental sync"* và *"idempotent 
 upsert"* cạnh nhau như hai thói quen tốt độc lập; [slide 44](#s42) nói thiếu idempotency 
 thì có duplicate. Không slide nào nói việc đó xảy ra *nhanh tới mức nào* — và câu trả lời phụ 
 thuộc vào việc bạn thiếu *một* hay *cả hai*. Ba chế độ dưới đây cách nhau ba bậc độ lớn.

Mặc định: 2.000 tài liệu × 8 chunk = 16.000 chunk · 2,0% tài liệu đổi nội dung mỗi ngày · 
 sync 24 lần/ngày · nhìn ở mốc 30 ngày · retrieval top-5.

Đoán trước: *(a)* với **incremental sync + insert thuần**, sau bao nhiêu ngày 
 thì một nửa kho là bản cũ? *(b)* tăng tần suất sync từ 1 lên 24 lần/ngày có làm con số đó tệ 
 đi không? *(c)* nếu **không** có incremental sync — mỗi lần chạy nạp lại toàn bộ 
 — thì bao lâu?

#### Kéo rồi mở

**(a) 50 ngày.** Công thức là `t½ = 1/g` với g là tỷ lệ tài liệu đổi mỗi 
 ngày — *không phụ thuộc số tài liệu lẫn số chunk mỗi tài liệu*. Kho 2.000 hay 200.000 tài 
 liệu đều mục ruỗng đúng cùng một nhịp.

**(b) Không, không hề.** Đây là phần phản trực giác. Với incremental sync, số lần 
 chèn bằng *số sự kiện tài liệu đổi*, không phải số lần chạy pipeline. Chạy 24 lần/ngày và 
 chạy 1 lần/ngày cho ra **đúng cùng một tỷ lệ rác**. Kéo thanh "số lần sync" để tự 
 kiểm — đường màu cam không nhúc nhích.

**(c) Một giờ.** Không có incremental sync thì mỗi lần chạy chèn lại toàn bộ kho, 
 và `t½ = 1/R`. Ở 24 lần/ngày, kho đã **96% là rác sau đúng một ngày**. 
 Đây là điểm chính của mô-đun: **hai gạch đầu dòng của slide 17 không độc lập — chúng nhân 
 với nhau.** Thiếu upsert mà còn incremental sync thì bạn có 50 ngày để phát hiện; thiếu cả 
 hai thì bạn có một giờ.

- **Control - Số tài liệu trong kho:**: min `2`, max `200`, step `2`, default `20`

- **Control - Chunk mỗi tài liệu:**: min `2`, max `40`, step `1`, default `8`

- **Control - Số lần sync:**: min `1`, max `48`, step `1`, default `24`

- **Control - Tốc độ đổi tài liệu:**: min `1`, max `150`, step `1`, default `20`

- **Control - Nhìn ở mốc:**: min `1`, max `180`, step `1`, default `30`

- **Control - Retrieval:**: min `1`, max `20`, step `1`, default `5`

upsert theo chunk_id (đúng)

incremental sync + insert thuần

full re-sync + insert thuần

Tỷ lệ kho là bản cũ

Nửa kho thành rác sau

Chunk hiệu lực trong top-k

Xác suất agent lặp ý

"incremental sync + insert thuần"

37,5%

3,13

61,9%

"lặp lại cùng một ý nhiều 
 lần"

slide 28

"full re-sync"

một giờ

Điều đáng lấy đi:

---

<!-- chiron-source-span: {"source_span_id":"5ccb65b8-b68f-5d3f-b871-ada382b038bf","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Transform, chunking & metadata","source_file":"slide-day10.html"},"checksum":"c92b07f9e2ddc9b06bb17e95e95f1ea6405bb6d5174021707243cee27dbae1b3"} -->

## 05 Transform, chunking & metadata

Chương này có một danh sách bảy trường ở [slide 23](#s22) đáng chép ra 
 giấy dán lên màn hình — và một câu cảnh báo giải thích vì sao phần lớn hệ RAG tự dựng đều thiếu nó.

### Slide 20 · 21 Năm vấn đề làm sạch, chuẩn hoá text, và dbt

> Trích slide 
>  " Missing values: NULL, empty string, 'N/A' · Outliers: giá trị 
>  bất thường ảnh hưởng embedding quality · Duplicates: dedup bằng hash hoặc fuzzy 
>  match · Wrong formats: date '31/12/2024' vs '2024-12-31' · Encoding 
>  issues: UTF-8 vs Latin-1 → luôn enforce UTF-8 " 
>  Text normalization cho AI: "Lowercasing: tuỳ model, không phải lúc nào cũng cần · 
>  Unicode normalization: NFC/NFD cho tiếng Việt · Whitespace: collapse multiple 
>  spaces · HTML stripping · Language detection: tách chunks theo ngôn ngữ" 
>  " Schema validation: enforce data contracts — reject records không đúng schema thay vì để 
>  lọt vào model. " 
>  dbt: "Modularity · Lineage: tự động sinh DAG dependency graph · Testing: 
>  built-in tests (not-null, unique, accepted-values) · Documentation · Version control: PR 
>  review cho data logic "

ệ

hai

e

trông giống hệt 
 nhau trên màn hình

khác nhau khi so sánh byte

Dedup không bắt được:

Mô-đun 1

song song

Tokenizer cắt khác nhau:

Keyword search trượt:

Ngày 7

Đối sách:

unicodedata.normalize("NFC", text)

cả

và

làm mất thông tin

với embedding thì đừng lowercase; với keyword/BM25 thì lowercase 
 cả hai vế.

khác nhau cho từng nhánh

### Slide 22 · 23 Năm bước transform cho AI, và bảy trường của một chunk tốt

> Trích slide 
>  " BI thường transform để báo cáo; AI transform để model hiểu đúng ngữ cảnh và retrieve 
>  đúng evidence. " Năm bước: "Clean text · Chunking · Metadata 
>  enrichment: gắn source, owner, version, effective date · Redaction: loại 
>  PII/secrets trước khi embed · Canonicalization: chuẩn hoá tên sản phẩm, mã đơn 
>  hàng, timestamp" 
>  chunks = chunk(text, size=500, overlap=80) 
> for i, chunk in enumerate(chunks): 
>  write_record({ 
>  "chunk_id": f"{doc.id}:{i}", 
>  "content": chunk, 
>  "source_doc": doc.id, 
>  "version": doc.updated_at, 
>  "department": "support" 
>  }) 
>  Chunk quá to: "chứa nhiều chủ đề → retrieval mơ hồ · tốn token, giảm chỗ cho 
>  reasoning" · Chunk quá nhỏ: " mất context quan trọng · câu trả lời thiếu điều kiện 
>  hoặc ngoại lệ" 
>  Chunk tốt thường cần: " content · chunk_id · source_doc_id · section/title · 
>  effective_date · owner/department · version/updated_at " 
>  " Lưu ý: Nhiều team chỉ embed 'text thuần' mà quên metadata — retrieve đúng đoạn nhưng 
>  không biết nó từ bản policy nào. "

| Trường | Không có nó thì mất khả năng gì | Triệu chứng ở agent |
| --- | --- | --- |
| chunk_id | Upsert — không có khoá thì chỉ insert được | Kho mục ruỗng ( Mô-đun 1 ) |
| source_doc_id | Trace ngược về tài liệu gốc; xoá theo tài liệu | Không debug được, không gỡ được tài liệu đã thu hồi |
| version / updated_at | Biết chunk này thuộc bản nào | Trả lời theo chính sách cũ mà không ai biết |
| effective_date | Freshness gate và lọc theo hiệu lực | Cite tài liệu chưa có hiệu lực hoặc đã hết hạn |
| owner / department | Lọc theo quyền và theo phòng ban | Cite sai phòng ban; lộ tài liệu ngoài phạm vi |
| section / title | Citation người đọc hiểu được | Trích dẫn chỉ ra "tài liệu X" mà không rõ chỗ nào |
| content | — | — |

Sáu trên bảy trường không phải để cải thiện retrieval.

vận hành

chunk_id

Mô-đun 1

slide 17

không cài đặt được

có

Ngày 8

đạt đỉnh rồi giảm

trong

Phép thử thực dụng thay cho việc chỉnh mò:

đọc

print(formatted_context)

---

<!-- chiron-source-span: {"source_span_id":"96fdb1d8-989c-5965-bf48-b8c753ed4871","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Data quality — 6 chiều & 5 gate","source_file":"slide-day10.html"},"checksum":"da4490a476cb356e9dfe4ec7576e5ab7fe470fab97892f6ba245e1a87d5c39ad"} -->

## 06 Data quality — 6 chiều & 5 gate

Deck liệt kê năm quality gate như thể chúng đều thuần lợi. Mô-đun 2 hỏi câu deck 
 không hỏi: *mỗi gate cũng chặn oan record tốt — vậy gate thứ năm còn đáng thêm không?* Câu trả lời 
 ở tham số mặc định là **không**.

### Slide 25 · 26 Sáu chiều chất lượng và Great Expectations

> Trích slide 
>  " 1. Completeness — không thiếu records hoặc fields quan trọng. Check:% NULL, 
>  row count so với expected · 2. Accuracy — đúng với thực tế. Check: validate với 
>  nguồn gốc, business rules · 3. Consistency — cùng entity, cùng format across 
>  systems · 4. Timeliness — đủ fresh cho use case. Check: max age, last-updated · 
>  5. Validity — đúng format và domain rules. Check: regex, range checks · 
>  6. Uniqueness — không duplicates. Check: dedup rate, composite key" 
>  Great Expectations: "1. Profile data: tự động suggest expectations · 2. Write expectations · 
>  3. Validate trước khi data vào pipeline · 4. Report: HTML data docs · 5. Alert: 
>  fail pipeline nếu expectations không pass "

chiều thứ hai không cùng loại với năm chiều 
 kia

| Chiều | Kiểm bằng gì | Cần gì bên ngoài data |
| --- | --- | --- |
| Completeness | Đếm NULL, so row count | Không |
| Accuracy | So với thực tế | Một nguồn chân lý ngoài hệ — hoặc một con người |
| Consistency | Đối chiếu chéo hệ thống | Không |
| Timeliness | So timestamp với ngưỡng | Không |
| Validity | Regex, range | Không |
| Uniqueness | Dedup rate, composite key | Không |

thuộc tính nội tại của dữ liệu

vẫn nói sai sự thật

Hệ quả thực tế:

không

owner

slide 23

"status: ok"

### Slide 27 · 28 Năm quality gate, và bảng lỗi → triệu chứng

> Trích slide 
>  "Trong AI pipeline, data quality không chỉ bảo vệ warehouse mà còn bảo vệ retrieval, tool 
>  use và final answer." Năm gate: " Schema gate: có đủ content, doc_id, 
>  updated_at · Freshness gate: policy quá cũ thì reject hoặc cảnh báo · 
>  Content gate: text đủ dài, OCR confidence không quá thấp · Dedup 
>  gate: cùng chunk không được nạp nhiều lần · PII gate: không embed số thẻ, 
>  mật khẩu, access token" 
>  def validate(record): 
>  assert record["content"].strip() 
>  assert record["updated_at"] >= cutoff_date 
>  assert len(record["content"]) >= 80 
>  assert not contains_secret(record["content"]) 
>  assert record["chunk_id"] not in seen_ids 
>  " Điểm dạy học quan trọng: nhiều lỗi nhìn giống 'model hallucination' nhưng gốc rễ thực ra 
>  là data pipeline bug. "

Năm gate này được trình bày như một danh sách kiểm — càng nhiều càng tốt. Nhưng mỗi `assert` trong đoạn code trên cũng *ném bỏ* record, và một số record bị ném bỏ là 
 record tốt. Mô-đun 2 tính cả hai chiều:

#### Tương tác Mô-đun 2 — Năm quality gate: gate thứ năm có đáng thêm không?

Mỗi gate bắt được một phần record bẩn đi qua nó, nhưng cũng **chặn oan** một phần record tốt. Record bẩn lọt vào làm agent trả lời sai; record tốt bị chặn làm agent *không tìm thấy bằng chứng* — cũng là một câu trả lời hỏng, chỉ hỏng theo chiều ngược lại 
 ( [slide 28](#s27), hàng "missing documents"). Mô-đun cộng cả hai chiều thành một con số 
 duy nhất: **số câu trả lời hỏng mỗi ngày**.

Mặc định: nạp 16.000 chunk · 3,0% record bẩn · mỗi gate bắt được 70% phần bẩn đi qua nó và chặn 
 oan 0,50% record tốt · 2.000 truy vấn/ngày · retrieval top-5.

Đoán trước: *(a)* bật đủ 5 gate thì còn bao nhiêu câu hỏng mỗi ngày? *(b)* con số 
 đó tốt hơn hay tệ hơn khi chỉ bật 3 gate? *(c)* số gate tối ưu là mấy?

#### Kéo rồi mở

**(a) 48,7 câu/ngày** — trong đó chỉ **0,7** câu là do chunk bẩn lọt, 
 còn **48,0** câu là do record tốt bị chặn oan. Gần như toàn bộ thiệt hại đã đổi 
 chiều.

**(b) Tệ hơn.** Ba gate cho **37,0** câu hỏng/ngày — tốt hơn năm 
 gate. Thậm chí *hai* gate (46,2) cũng đã tốt hơn năm gate.

**(c) Ba.** Và đây là điểm chính: **gate không miễn phí, nên "càng nhiều 
 càng tốt" là sai.** Nhưng chú ý điều quyết định không phải số gate mà là *tỷ lệ chặn oan*: kéo thanh đó từ 0,50% xuống 0,02% thì tối ưu chuyển thành **năm** gate. Nghĩa là câu hỏi đúng không phải "nên có mấy gate" mà **"gate của tôi chặn oan bao nhiêu, và tôi có đo không?"**

- **Control - Số chunk nạp vào:**: min `2`, max `100`, step `2`, default `16`

- **Control - Tỷ lệ record bẩn:**: min `2`, max `200`, step `2`, default `30`

- **Control - Mỗi gate bắt được:**: min `20`, max `95`, step `5`, default `70`

- **Control - Mỗi gate chặn oan:**: min `1`, max `100`, step `1`, default `50`

- **Control - Lưu lượng:**: min `2`, max `200`, step `2`, default `20`

- **Control - Retrieval:**: min `1`, max `20`, step `1`, default `5`

- **Control - Số gate đang bật:**: min `0`, max `5`, step `1`, default `5`

Tổng câu hỏng mỗi ngày

Chunk bẩn lọt vào kho

Record tốt bị chặn oan

Số gate tối ưu

hai màu đổi chỗ cho nhau.

đi lên

3 gate

Ba điều cần lấy đi:

Gate đầu tiên gần như luôn đáng làm

65%

assert

Gate thứ năm thì không

tệ hơn

Nhưng ② không phải lời khuyên bỏ bớt gate — nó là lời khuyên đo tỷ lệ chặn 
 oan.

chính xác

chúng không ngang 
 giá

với bốn gate đầu — schema, freshness, content, 
 dedup — phép cân bằng số là hợp lý

PII gate thì không cân

nhóm tool không đảo ngược của Ngày 9

Kết luận đúng:

chính xác hơn

nghiêm hơn

---

<!-- chiron-source-span: {"source_span_id":"b7054618-fd3f-540f-b004-46dc98ff368f","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Mini-Quest 2 — agent trả lời sai, bạn check gì trước?","source_file":"slide-day10.html"},"checksum":"83667ad7900f830f3f040649705f8dd47290657da1dd9d94ba854c1d24b9f15c"} -->

## 07 Mini-Quest 2 — agent trả lời sai, bạn check gì trước?

### Slide 30 Đề bài — và ràng buộc mới là phần hay nhất

> Trích slide 
>  "Agent RAG của bạn đang trả lời sai — thông tin cũ, khách hàng phàn nàn. Bạn có 10 phút, 
>  agent này không có logging/observability nào cả. Bạn sẽ kiểm tra những gì đầu tiên để tìm 
>  nguyên nhân?" 
>  "Gợi ý nếu bí: nghĩ theo hướng 'data có mới không, có đủ không, có lỗi gì không'."

Hai ràng buộc trong đề — *10 phút* và *không có logging* — không phải để làm khó. Chúng 
 tái tạo chính xác tình huống mà phần lớn người đọc sẽ gặp lần đầu tiên: bạn thừa hưởng một hệ đang chạy, 
 nó bắt đầu sai, và không ai đã nghĩ tới observability.

theo thứ tự

mỗi việc bạn liệt kê có loại trừ được một 
 nhóm nguyên nhân không?

### Slide 32 Đáp án — sáu bước, và con số duy nhất của cả deck

> Trích slide 
>  "1. User phàn nàn agent đưa thông tin cũ · 2. Check answer trace: agent đã 
>  retrieve chunk nào? · 3. Check Freshness: chunk đó thuộc policy version ngày nào? · 
>  4. Check Volume: số documents embed hôm nay có drop về 0 không? · 5. 
>  Trace Lineage: ingestion run 2am fail ở bước sync policy · 6. Root cause: 
>  API timeout, retry/backoff chưa cấu hình đúng " 
>  Monitoring metrics: "Pipeline SLA · Row count delta · Null rate per column · 
>  Schema drift · Data freshness · Embedding coverage " 
>  " Không có observability: phát hiện sau 8 giờ, 500 users bị ảnh hưởng. "

câu trả lời

cấu hình retry

| Bước | Ở tầng nào | Nó loại trừ được gì |
| --- | --- | --- |
| 2. Chunk nào được retrieve | Retrieval | Nếu chunk đúng mà trả lời sai → lỗi ở generation, không phải data |
| 3. Chunk đó thuộc version nào | Index | Nếu version mới → data ổn, lỗi ở chỗ khác |
| 4. Số document embed hôm nay | Pipeline | Drop về 0 → gần như chắc chắn ingestion, dừng đoán |
| 5. Run nào fail, ở bước nào | Lineage | Khoanh vào một bước cụ thể |
| 6. Vì sao bước đó fail | Cấu hình | Nguyên nhân gốc |

Bước 4 là bước rẻ nhất và mạnh nhất

Ngày 9 · Mini-Quest 3

result_count == 0

Trong hệ dữ liệu, phép đếm là công cụ chẩn đoán mạnh nhất trên mỗi đơn 
 vị công sức.

"không có observability nào cả"

đòi

đáng lẽ

---

<!-- chiron-source-span: {"source_span_id":"6b8611d2-43a4-5b43-a3eb-864d43b21b3d","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Năm trụ observability & bán kính vụ nổ","source_file":"slide-day10.html"},"checksum":"2e4d89d8a5bf87f94e31bc80bedcbb60e66159c9262fa23319a34b8d2cf511db"} -->

## 08 Năm trụ observability & bán kính vụ nổ

Chương này chứa con số định lượng duy nhất của cả deck. Mô-đun 3 tái lập nó rồi hỏi 
 tiếp: *một cron job kiểm freshness mỗi giờ đáng bao nhiêu tiền?*

### Slide 31 Năm trụ, và năm trường tối thiểu để trace được

> Trích slide 
>  " Freshness — data có đang được update theo đúng lịch? · Distribution 
>  — giá trị phân phối có bất thường không? (null rate, range) · Volume — số lượng 
>  records tăng/giảm bất thường? · Schema — cột bị đổi tên, thêm, xoá không? · 
>  Lineage — data đến từ đâu, đi qua transform nào?" 
>  " Data Lineage — track hành trình data từ nguồn gốc → pipeline → 
>  chunk/index → retrieved context → model output " 
>  "Muốn debug được, phải log ít nhất: question/session ID · retrieved chunk IDs · source 
>  document version · embedding/index version · pipeline run ID "

| Trụ | Trả lời câu hỏi | Bắt được lỗi nào ở Hình 1 | Chi phí dựng |
| --- | --- | --- | --- |
| Freshness | Data có mới không? | Sync fail, tài liệu cũ | Một truy vấn MAX(updated_at) |
| Volume | Số record có bình thường không? | Sync thiếu (199/200), embed drop về 0 | Một phép đếm mỗi run |
| Distribution | Giá trị có bất thường không? | OCR hỏng, chunk rỗng, null tăng vọt | Vừa — cần baseline |
| Schema | Cột có đổi không? | Nguồn đổi API, mất field metadata | Vừa — cần schema snapshot |
| Lineage | Vì sao nó hỏng? | Không bắt lỗi nào — nó giúp truy nguyên | Cao — phải xuyên suốt mọi bước |

Hai trụ đầu rẻ đến mức không có lý do gì để không có.

Mô-đun 3

hơn tám lần

chính là

slide 23

#### Tương tác Mô-đun 3 — Bán kính vụ nổ: tái lập "8 giờ, 500 users"

[Slide 32](#s32) đưa ra con số định lượng duy nhất trong 50 slide: *"không có observability: phát hiện sau 8 giờ, 500 users bị ảnh hưởng."* Nó tự nhất quán — 
 500 ÷ 8 = 62,5 người mỗi giờ — và mô-đun này tái lập đúng nó, rồi tính điều deck không tính: mỗi mức 
 giám sát cắt được bao nhiêu, và bao lâu thì khoản đầu tư hoàn vốn.

Mặc định: 250 truy vấn/giờ · 25% trong số đó chạm vùng dữ liệu hỏng · sửa mất 30 phút sau khi 
 phát hiện · chi phí dựng giám sát 40 triệu đ một lần · thiệt hại 30 nghìn đ mỗi người bị ảnh hưởng.

Đoán trước: *(a)* mô hình có ra đúng 500 người ở mốc 8 giờ không? *(b)* một cron job 
 kiểm freshness **mỗi giờ** thì còn bao nhiêu người? *(c)* khoản 40 triệu hoàn vốn 
 sau mấy lần sự cố?

#### Kéo rồi mở

**(a) Có — đúng 500.** 250 × 25% = 62,5 người/giờ, nhân 8 giờ ra 500. Con số của 
 deck nhất quán, nên ta có thể tin phần còn lại của mô hình.

**(b) 63 người.** Kiểm mỗi giờ nghĩa là phát hiện trung bình sau *nửa* giờ 
 (sự cố rơi ngẫu nhiên trong chu kỳ), cộng 30 phút sửa. So với 531 người ở mốc 8 giờ, đó là **giảm 8,5 lần** — đổi lại một câu `SELECT MAX(updated_at)` chạy trong 
 cron.

**(c) 2,8 lần.** Mỗi lần sự cố, cách giám sát này cứu được 469 người × 30 nghìn đ 
 ≈ 14,1 triệu đ. Bốn mươi triệu chia cho 14,1 ra **chưa tới ba lần sự cố**. 
 Nói cách khác: **nếu hệ của bạn có nhiều hơn ba sự cố dữ liệu trong đời, giám sát đã có 
 lãi.** Và nếu bạn nghĩ hệ mình sẽ có ít hơn ba, hãy hỏi lại — bạn có cách nào biết đã có 
 bao nhiêu rồi không?

- **Control - Lưu lượng:**: min `2`, max `200`, step `1`, default `25`

- **Control - Tỷ lệ chạm vùng hỏng:**: min `1`, max `100`, step `1`, default `25`

- **Control - Thời gian sửa:**: min `5`, max `240`, step `5`, default `30`

- **Control - Chi phí dựng giám sát:**: min `5`, max `300`, step `5`, default `40`

- **Control - Thiệt hại mỗi người:**: min `2`, max `300`, step `2`, default `30`

Không có gì — chờ user phàn nàn

Freshness check mỗi 4 giờ

Freshness check mỗi 1 giờ

Alert realtime

Tốc độ nhiễm

Người bị ảnh hưởng

Cứu được so với slide 32

Hoàn vốn sau

thiệt hại tỷ lệ tuyến tính với thời gian phát 
 hiện

lag

5 điểm 
 phần trăm

Kết luận thực dụng:

tuần này

bảng ở slide 31

---

<!-- chiron-source-span: {"source_span_id":"167d9daf-4790-5d4c-9f57-8c719cf21bb1","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 Debug ngược 5 lớp","source_file":"slide-day10.html"},"checksum":"de73f35439daadca2f6c3f750e05a233ebd46085db49e77e8887e928183967d2"} -->

## 09 Debug ngược 5 lớp

[Slide 33](#s33) đưa ra quy trình debug năm lớp và một câu cảnh báo sắc: *"nếu bạn chỉ nhìn final answer mà không trace được về chunk và source document, bạn đang debug trong 
 bóng tối."*

### Slide 33 · 34 Năm lớp, tám trường trace, và hai nhóm tín hiệu

> Trích slide 
>  "1. Output layer: agent trả lời gì, cite gì, confidence ra sao? · 2. 
>  Retrieval layer: top-k chunks nào được lấy ra? có zero-hit không? · 
>  3. Index layer: chunk đó được embed bằng model/version nào? · 4. Pipeline 
>  layer: run nào sinh ra chunk? pass/fail quality gates nào? · 5. Source layer: 
>  tài liệu gốc có đúng, mới và đầy đủ không?" 
>  " Lưu ý: Nếu bạn chỉ nhìn final answer mà không trace được về chunk và source document, 
>  bạn đang debug trong bóng tối. " 
>  Fields nên có trong trace log: " request_id · pipeline_run_id · retrieved_chunk_ids · 
>  source_doc_ids · source_version · embedding_model · latency_ms · fallback_used " 
>  Pipeline signals: "freshness · failed sync count, dead-letter queue size · 
>  duplicate chunk rate · missing metadata rate · embedding queue lag" · 
>  Agent signals: " retrieval hit rate ·% answers có citation hợp lệ · 
>  user correction/escalation rate · tool-call failure rate · abandoned conversations" 
>  " Observability tốt phải nối được data issue → retrieval issue → business impact. "

tám trường trace không phải danh sách "nên 
 có cho đẹp" — chúng là chìa khoá của năm lớp, mỗi lớp một chìa.

| Lớp | Trường mở được nó | Thiếu trường thì bạn kẹt ở đâu |
| --- | --- | --- |
| 1 · Output | request_id, fallback_used | Không nối được câu trả lời với lần chạy nào |
| 2 · Retrieval | retrieved_chunk_ids | Không biết agent đã đọc gì — mọi suy đoán từ đây là mù |
| 3 · Index | embedding_model, source_version | Không biết chunk thuộc bản nào, không phát hiện được embedding drift |
| 4 · Pipeline | pipeline_run_id | Không biết run nào sinh ra chunk này, không kiểm được gate |
| 5 · Source | source_doc_ids | Không mở được tài liệu gốc ra đối chiếu |

Lớp 2 là lớp gãy đầu tiên và đắt nhất.

retrieved_chunk_ids

không tìm được bằng chứng

tìm được mà dùng sai

bộ ba RAGAS của Ngày 8

"có zero-hit không?"

Mini-Quest 3 của Ngày 9

status: ok

hai

| Tầng | Chỉ số | Ai quan tâm |
| --- | --- | --- |
| Data | freshness · failed sync · duplicate chunk rate · missing metadata | Kỹ sư data |
| Retrieval | retrieval hit rate ·% answer có citation hợp lệ · tool-call failure | Kỹ sư AI |
| Business | user correction/escalation rate · abandoned conversations | Người quyết định ngân sách |

Hai chỉ số ở tầng thứ ba là hai chỉ số duy nhất trong cả bài mà người ngoài đội kỹ thuật 
 hiểu được ngay

Ngày 6

"tỷ lệ khách phải hỏi lại tăng từ 8% lên 19% trong ba tuần, và nó bắt đầu đúng ngày pipeline sync 
 fail"

_Sơ đồ: Năm lớp debug ngược từ câu trả lời sai về tài liệu gốc, và trường trace mở được mỗi lớp - Năm băng ngang xếp chồng, đọc từ trên xuống theo hướng debug. Lớp một là output: agent trả lời gì và cite gì, mở được bằng trường request_id và fallback_used. Lớp hai là retrieval: top-k chunk nào được lấy ra và có zero-hit không, mở được bằng trường retrieved_chunk_ids; đây là lớp gãy đầu tiên và đắt nhất vì thiếu nó thì không biết agent đã đọc gì. Lớp ba là index: chunk được embed bằng model và version nào, mở được bằng embedding_model và source_version. Lớp bốn là pipeline: run nào sinh ra chunk và nó qua hay trượt quality gate nào, mở được bằng pipeline_run_id. Lớp năm là source: tài liệu gốc có đúng, mới và đầy đủ không, mở được bằng source_doc_ids. Bên trái là một mũi tên lớn chỉ xuống ghi hướng debug đi từ triệu chứng về nguyên nhân. Dòng cuối trích slide 33: nếu chỉ nhìn final answer mà không trace được về chunk và source document thì bạn đang debug trong bóng tối._

Hình 2 — Năm lớp debug, và chìa khoá của từng lớp.

slide 33

việc ghép từng trường vào đúng lớp nó mở

---

<!-- chiron-source-span: {"source_span_id":"e2b0d01a-14ca-56bd-895f-ca3bbaffc2e7","locator":{"kind":"html_section","section_id":"c10","order":12,"heading":"10 Trace, span & observability cho agent","source_file":"slide-day10.html"},"checksum":"2647cd1c46a743fc24607a52acf491774531e6a1ad0876f64c850475d2e16407"} -->

## 10 Trace, span & observability cho agent

Ba slide nối Ngày 10 với Ngày 9: cùng ý tưởng freshness/volume/schema, nhưng đo ở 
 tầng model thay vì tầng pipeline. Và một cảnh báo về chi phí mà không chỉ số nào ở trên bắt được.

### Slide 35 · 36 Trace và span — "data đâu dừng, model tiếp tục"

> Trích slide 
>  " Trace = một lần agent chạy end-to-end; Span = một bước bên 
>  trong (1 LLM call, 1 tool call, 1 retrieval) — cùng ý tưởng freshness/volume/schema bạn vừa 
>  học, chỉ khác tầng đo: model thay vì pipeline " 
>  "Agent call → instrument bằng OpenTelemetry GenAI spans → gửi trace về 
>  Langfuse (self-host, open-source), Phoenix (open-source, 
>  OpenInference), hoặc LangSmith (managed, free tier 5k trace/tháng) → score tự động 
>  bằng RAGAS → alert khi quality hoặc cost drift" 
>  " Lưu ý chọn tool: Helicone đã bị Mintlify mua (03/2026), giờ chỉ maintenance mode — không 
>  còn phát triển tính năng mới. Ưu tiên Langfuse/Phoenix nếu cần self-host lâu dài. " 
>  Mỗi trace ghi lại: "Prompt gửi đi, response nhận về · Token usage, latency, cost · 
>  từng tool/retrieval step lồng bên trong (nested spans)"

slide 31

| Trụ | Ở tầng pipeline | Ở tầng model / agent |
| --- | --- | --- |
| Freshness | Data update đúng lịch không? | Prompt template, index version còn là bản mới nhất không? |
| Volume | Số record mỗi run | Số trace mỗi giờ · số token mỗi request |
| Distribution | Null rate, range | Phân phối điểm faithfulness · phân phối latency |
| Schema | Cột bị đổi tên không? | Output có đúng schema không (chính là 
 expected_output của Ngày 9 ) |
| Lineage | Data đi qua transform nào? | Trace và span lồng nhau — cùng khái niệm, cùng tên |

lineage

trace

là cùng một thứ

OpenLineage ở slide 7

bài học rút ra thì không

bạn

langfuse.trace(...)

khoá vào một SDK cụ thể

ghi theo chuẩn, đọc bằng công 
 cụ.

### Slide 37 RAGAS, vector store health — và một trục cảnh báo không giống các trục khác

> Trích slide 
>  result = evaluate(dataset, metrics=[faithfulness, answer_relevancy]) 
> # {'faithfulness': 0.83, 'answer_relevancy': 0.91} 
>  Vector store health: "Qdrant/Weaviate: expose Prometheus metrics (/metrics) — recall, latency, 
>  memory · Embedding drift: retrieval quality giảm dù 'embedding coverage' vẫn 100% " 
>  " Lưu ý: Cost/token là trục alert riêng: 1 agent loop lỗi có thể ×100 chi phí trong vài 
>  phút mà không hề có anomaly ở row count hay schema — track $/request và token delta giống cách bạn 
>  track row count delta. "

mọi thứ khác đều trông bình 
 thường

cao

một

Chỉ có hai thứ hiện lên: $/request và số token mỗi trace.

Ngày 9

×100 trong vài phút, không do thiết kế mà do một vòng lặp không có điểm dừng.

hard cap

Embedding coverage

đã được embed

hoàn toàn mù

embedding_model

slide 33

trường duy nhất

một

---

<!-- chiron-source-span: {"source_span_id":"4d2939a2-8cc3-51b7-bbcc-6337cd9cdeb3","locator":{"kind":"html_section","section_id":"c11","order":13,"heading":"11 Orchestration & Mini-Quest 3","source_file":"slide-day10.html"},"checksum":"b9419b7c8fdc7c68d2dede4ccf6d6a5fedc280414d3deeb382c41b6023635f2a"} -->

## 11 Orchestration & Mini-Quest 3

Chương cuối về kỹ thuật, và nó khép lại vòng: [slide 42](#s42) vẽ pipeline 
 đúng, [slide 43](#s43) đưa cùng pipeline đó với một bước bị gỡ đi và hỏi bạn thiếu gì.

### Slide 39 · 40 · 41 Airflow, Dagster, Prefect — và lời khuyên đúng ở cuối

> Trích slide 
>  Airflow: " DAG · Operator · Scheduler — Airflow 3.0 (2025) thêm 
>  event-driven native + DAG versioning · Executor · XCom" · Prefect: 
>  "Python-native, ít boilerplate hơn. Flows = Python functions" · Dagster: 
>  " Asset-centric orchestration — model data assets, không phải tasks. Built-in lineage & 
>  observability " 
>  " Góc nhìn thực tế: hệ RAG/agent nhỏ thường bắt đầu bằng cron + Python; khi số bước, số 
>  nguồn, và số team tăng lên thì mới nâng lên Airflow / Prefect / Dagster. "

"bắt đầu bằng cron + Python"

lời khuyên "JSON log tự viết trước, LangSmith sau" của Ngày 9

Phép thử để biết khi nào nên nâng cấp — ba dấu hiệu, cần ít nhất hai:

Bạn cần chạy lại một khoảng ngày trong quá khứ

Một bước phụ thuộc bước khác ở pipeline khác

Nhiều hơn một người cần biết pipeline đang ở đâu

UI là tính năng chứ không phải trang trí

"asset-centric — model data assets, không phải tasks. Built-in lineage 
 & observability"

"lineage sẵn có"

trụ đắt nhất trong năm trụ

asset

task

Hình 2

Nhưng đừng đổi công cụ chỉ vì lý do này.

pipeline_run_id

### Slide 43 Mini-Quest 3 — pipeline này thiếu gì?

> Trích slide 
>  Pipeline của startup X: " Sync docs/API → Chunk + metadata → Embed → Upsert vector store → 
>  Smoke test retrieval → Notify/alert " 
>  "Nhìn kỹ — so với những gì ta vừa học, pipeline này đang thiếu bước quan trọng 
>  nào? Điều gì sẽ xảy ra trong thực tế nếu một tài liệu bị lỗi (OCR hỏng, thiếu field) 
>  đi qua pipeline này? "

slide 42

tài liệu OCR hỏng đó sẽ dừng 
 lại ở bước nào?

"bước này có phát hiện được không?"

### Slide 42 · 44 Đáp án — và vì sao "smoke test" không cứu được

> Trích slide 
>  Pipeline đúng (slide 42): "Sync docs/API → Quality gate → Chunk + metadata → 
>  Embed → Upsert vector store → Smoke test retrieval → Notify/alert" 
>  " Fail fast: quality gate fail thì không cho index tiếp · Smoke test: chạy vài câu 
>  hỏi chuẩn để check retrieval · Notify: báo Slack nếu index mới làm hit rate giảm" 
>  " Trong AI pipeline, orchestration không chỉ 'chạy jobs' mà còn kiểm soát chất lượng đầu 
>  vào trước khi agent dùng data mới. " 
>  Error handling: " Retry với backoff · Dead Letter Queue: failed 
>  records không bị mất · Partial failure: idempotent tasks để re-run an toàn · 
>  Alerting · SLA breach" 
>  " Idempotency là bắt buộc: chạy lại pipeline 2 lần phải cho kết quả giống chạy 1 lần. 
>  Thiếu idempotency dẫn đến duplicate data trong vector store. "

không bước nào trong sáu 
 bước phát hiện ra nó.

| Bước | Nó làm gì với tài liệu OCR hỏng | Có chặn không |
| --- | --- | --- |
| Sync | Tải về thành công — file có tồn tại và đọc được | Không |
| Chunk + metadata | Chia đều thành chunk. Ký tự rác cũng là ký tự | Không |
| Embed | Sinh vector bình thường — model embed được mọi thứ, kể cả rác | Không |
| Upsert | Ghi vào kho thành công | Không |
| Smoke test retrieval | Chạy "vài câu hỏi chuẩn" — và chúng không hỏi về tài liệu này | Không |
| Notify | Báo "pipeline thành công" | Không |

Hàng thứ năm là hàng dễ bị hiểu nhầm nhất.

trông

mô hình embedding không bao giờ 
 báo lỗi.

"status: ok"

Ngày 9

trước

bắt buộc

Mô-đun 1

chunk_id

50 ngày

một giờ

retry chỉ an toàn nếu task idempotent

tệ hơn

chunk_id

slide 23

_Sơ đồ: Pipeline của startup X thiếu quality gate, so với pipeline đúng, và đường đi của một tài liệu OCR hỏng - Hàng trên là pipeline đúng ở slide 42 gồm bảy bước: sync tài liệu, quality gate, chunk và metadata, embed, upsert vào vector store, smoke test retrieval, và notify. Hàng dưới là pipeline của startup X ở slide 43, giống hệt nhưng ô quality gate bị bỏ trống, vẽ bằng nét đứt màu đỏ ghi là thiếu. Bên dưới là đường đi của một tài liệu bị OCR hỏng qua sáu bước của pipeline thiếu gate: sync tải về thành công vì file vẫn đọc được, chunk chia đều vì ký tự rác cũng là ký tự, embed sinh vector bình thường vì mô hình embedding không bao giờ báo lỗi, upsert ghi vào kho thành công, smoke test không phát hiện vì vài câu hỏi chuẩn không hỏi về tài liệu này, và notify báo pipeline thành công. Kết luận: không bước nào trong sáu bước chặn được nó, nên quality gate phải đứng trước bước chunk chứ không phải sau bước embed, vì sau đó thì rác đã có vector và trông y hệt dữ liệu thật._

Hình 3 — Mini-Quest 3: một hộp bị gỡ, và hậu quả.

slide 42

slide 43

đáp án cho câu hỏi thứ hai của đề

không bước nào chặn

---

<!-- chiron-source-span: {"source_span_id":"008c016d-87e8-594f-899b-f97ed8ba26b8","locator":{"kind":"html_section","section_id":"c12","order":14,"heading":"12 Lab 10 & tổng kết","source_file":"slide-day10.html"},"checksum":"1820558d8a2f0d38054eeef65e932b8007254b595d901775a0821fa4068e5a8d"} -->

## 12 Lab 10 & tổng kết

Lab 10 có một yêu cầu mà chín Lab trước không có, và nó là yêu cầu hay nhất trong cả 
 Foundation: *cố tình làm hỏng dữ liệu của chính mình rồi đo xem agent hỏng theo.*

### Slide 45 Lab 10 — bốn deliverable, và cái thứ tư là cái đáng làm nhất

> Trích slide 
>  "Mục tiêu: Build AI data pipeline hoàn chỉnh: thu thập raw docs, làm sạch, chunk, enrich metadata, 
>  embed và nạp vào vector store cho agent. Simulate data corruption để đo impact lên retrieval 
>  và câu trả lời. " 
>  Deliverable: "(1) Pipeline script: raw → cleaned → chunked → embedded; (2) Quality gates 
>  cho schema/freshness/duplicates; (3) Trace log để debug agent answers; 
>  (4) So sánh response quality trước/sau fix data " 
>  "Thời gian: 4 giờ (Vibe Coding 1.5h + Lab 2.5h)"

xây một thứ và cho thấy nó chạy

phá thứ mình vừa xây, theo cách có kiểm soát, và đo mức hỏng

demo

thí nghiệm

đáng bao nhiêu

Bốn cách phá đáng thử, xếp theo độ khó phát hiện tăng dần:

| Cách phá | Mô phỏng lỗi thật nào | Bạn kỳ vọng thấy gì |
| --- | --- | --- |
| Xoá 20% chunk ngẫu nhiên | Sync fail một phần | Zero-hit tăng; agent nói "không tìm thấy" — dễ thấy |
| Nhân đôi 30% chunk | Thiếu idempotency ( Mô-đun 1 ) | Câu trả lời lặp ý; top-k ít thông tin thật hơn |
| Thay 15% chunk bằng bản cũ của chính nó | Không có upsert | Agent trả lời trôi chảy và SAI — khó nhất |
| Xoá trường effective_date | Metadata drift | Citation vẫn có nhưng không kiểm chứng được hạn |

Hàng thứ ba là hàng đáng làm nhất

không

source_version

đo cùng một thứ hai lần

trước

10 câu có đáp án rõ trong một tài liệu

10 câu cần ghép hai tài liệu

10 câu mà tài liệu KHÔNG có đáp án

Mini-Quest 3 của Ngày 9

mọi

### Slide 46 · 47 · 49 Bốn takeaway, và câu khép lại

> Trích slide 
>  " 1 Data pipeline là hệ tuần hoàn của mọi AI product — agent mạnh đến đâu cũng vô 
>  dụng nếu data vào bị bẩn · 2 Pipeline cho AI khác BI ở chỗ phải tối ưu cho 
>  retrieval, context quality, citations và khả năng debug agent · 3 
>  Data quality gates phải chặn thiếu dữ liệu, dữ liệu cũ, duplicate chunks, metadata sai và 
>  secret leakage · 4 Observability tốt cho phép trace từ câu trả lời 
>  sai ngược về chunk, pipeline run và source document — và tiếp tục vào tận trace/span của model 
>  call " 
>  Ngày tiếp theo: " Guardrails & AI Safety — agent hoạt động đúng không có nghĩa 
>  là an toàn · Đọc: OWASP Top 10 for LLMs · Thực hành: thêm input/output validation vào ETL 
>  pipeline từ Lab 10 · Suy nghĩ: Agent của bạn có thể bị poisoned data attack 
>  không? " 
>  Slide 49: " Garbage in → garbage out. Bạn kiểm soát data quality bằng cách nào trong 
>  project của mình? "

"…và tiếp tục vào tận trace/span của model call."

Ngày 9

là một đường liên tục, không phải hai hệ thống

| Đoạn đường | Bài nào dạy | Khoá nối |
| --- | --- | --- |
| Tài liệu gốc → pipeline run → chunk | Ngày 10 | source_doc_id, pipeline_run_id |
| Chunk → retrieved context | Ngày 8 & 10 | retrieved_chunk_ids |
| Retrieved context → LLM call → câu trả lời | Ngày 9 | request_id, span lồng nhau |

slide 32

một

Đó là lý do đáng gộp cả hai bài thành một checklist duy nhất

Bài 3

"Agent của bạn có thể bị poisoned data attack không?"

Mô-đun 2

ngẫu nhiên

chọn

r

Nghĩa là kết luận "ba gate là tối ưu" của Mô-đun 2 chỉ đúng cho lỗi ngẫu nhiên.

---

<!-- chiron-source-span: {"source_span_id":"ece5112f-3ac8-5e68-b6b4-1f7f8cda6c1b","locator":{"kind":"html_section","section_id":"ladder","order":15,"heading":"▤ Luyện kỹ năng cốt lõi: trace ngược từ một câu trả lời sai về nguyên nhân","source_file":"slide-day10.html"},"checksum":"b2f6eeecbed4ab5a558fb54c5bd9b0d20cab0677e3f8ba3deebb9bf659a406e1"} -->

## ▤ Luyện kỹ năng cốt lõi: trace ngược từ một câu trả lời sai về nguyên nhân

Ba bài giảm dần giàn giáo. Kỹ năng được luyện là kỹ năng Lab 10 chấm: *quality gate có thật · trace log dùng được · đo được trước/sau*.

Agent trả lời [sai thế nào]. Nó đã retrieve [chunk id nào] — kiểm bằng [trường trace nào]. 
 Chunk đó thuộc [bản nào], sinh ra bởi [run id nào], qua/trượt [gate nào]. Tài liệu gốc [đúng/cũ/thiếu]. 
 Nguyên nhân gốc là [cái gì], và nó đáng lẽ đã hiện lên nếu có [chỉ số nào].

#### Khách hàng báo: "Chatbot nói phí huỷ 
 phòng là 50%, nhưng chính sách mới đã đổi thành 30% từ tháng trước." Bạn có trace log đầy đủ. 
 Tìm nguyên nhân gốc

Đọc cách *lập luận*, không chỉ đáp án.

1. Đừng mở prompt ra sửa — trước hết hỏi agent đã đọc gì. Cám dỗ đầu tiên luôn là 
 "model không đọc kỹ, thêm câu 'hãy dùng bản mới nhất' vào prompt". Nhưng theo 
 Hình 2, lớp 1 chưa loại trừ được gì cả. 
 Lấy request_id từ khiếu nại, tra ra retrieved_chunk_ids. Đây là bước 
 rẻ nhất và nó chia bài toán làm đôi: 
 · Chunk trả về nói 30% mà agent trả lời 50% → lỗi ở generation. Đây mới là lúc sửa 
 prompt. 
 · Chunk trả về nói 50% → lỗi ở data, và mọi công sức sửa prompt là lãng phí. 
 Giả sử ta rơi vào trường hợp thứ hai.
2. Hỏi chunk đó thuộc bản nào — và đây là chỗ có ba nhánh, không phải một. 
 Đọc source_version của chunk. Ba khả năng, và chúng đòi ba cách sửa khác nhau: 
 · Chỉ có bản cũ trong kho → tài liệu mới chưa bao giờ vào. Vấn đề ingestion. 
 · Có CẢ hai bản → thiếu idempotent upsert. Đây là ca của 
 Mô-đun 1, và nó là ca hay gặp nhất. 
 · Chỉ có bản mới, nhưng nội dung vẫn nói 50% → tài liệu nguồn sai. Vấn đề nằm 
 ngoài kỹ thuật, ở quy trình duyệt nội dung. 
 Đếm số bản của cùng một source_doc_id trong kho là một câu truy vấn, và nó phân 
 biệt được cả ba.
3. Nếu là nhánh hai, đừng dừng ở việc xoá bản cũ. Xoá xong thì hết triệu chứng 
 của tài liệu này, còn nguyên nhân thì vẫn ở đó và mọi tài liệu khác vẫn đang tích rác. 
 Chạy phép đo: SELECT source_doc_id, COUNT(DISTINCT source_version) FROM chunks GROUP BY 1 
 HAVING COUNT(*) > 1. Con số trả về là tỷ lệ rác thật của kho bạn — 
 và Mô-đun 1 cho biết nó sẽ đi tới đâu nếu không sửa gốc.
4. Sửa gốc: thêm chunk_id ổn định và đổi insert thành 
 upsert. chunk_id phải tất định — f"{doc.id}:{i}" như 
 slide 22, không phải UUID sinh mới mỗi lần chạy. Nếu bạn đang dùng UUID, đó 
 chính là nguyên nhân gốc: upsert không thể hoạt động khi khoá đổi mỗi lần. 
 Rồi chạy lại toàn bộ một lần để dọn — sau khi upsert đúng, một lần re-ingest đầy đủ sẽ hội tụ về 
 đúng một bản cho mỗi chunk.
5. Ô thứ năm: thêm chỉ số đáng lẽ đã bắt được nó. Ở đây là 
 duplicate chunk rate — có sẵn trong danh sách pipeline signal của 
 slide 34. Một truy vấn, chạy mỗi ngày, alert nếu vượt 5%. 
 Và thêm trường effective_date vào filter lúc retrieve nếu chưa có, để bản hết hiệu 
 lực không lọt vào top-k ngay cả khi nó còn nằm trong kho.
6. Câu trả lời hoàn chỉnh, gói trong bốn câu: 
 "Agent retrieve đúng nhưng chunk là bản tháng 6, vì kho có cả hai bản — pipeline dùng insert 
 chứ không upsert, và chunk_id là UUID sinh mới nên upsert không thể hoạt động. Kho hiện có 14% chunk 
 là bản trùng, không riêng tài liệu này. Sửa: chunk_id tất định theo doc_id:index, đổi sang upsert, và 
 chạy lại một lần để dọn. Thêm duplicate chunk rate vào alert hằng ngày để lần sau nó tự hiện lên 
 thay vì đợi khách hàng báo."

#### Lấy pipeline thật của bạn. Trả lời bốn 
 câu của checklist slide 18 — và mỗi câu phải trả lời bằng một lệnh chạy 
 được, không phải bằng "chắc là có"

Bốn gợi ý, mỗi gợi ý chỉ về một câu truy vấn cụ thể.

1. "Có lấy đúng nguồn không?" — So tập source_doc_id trong vector 
 store với danh sách tài liệu ở nguồn. Hai tập này lệch nhau bao nhiêu? Phần dư trong kho là tài liệu 
 đã bị xoá ở nguồn mà chưa gỡ — ca DELETE ở slide 16. Phần thiếu là tài 
 liệu chưa bao giờ vào.
2. "Có lấy đủ bản mới nhất không?" — SELECT MAX(updated_at) FROM chunks. 
 Nếu con số đó cũ hơn tài liệu mới nhất ở nguồn, bạn vừa tìm ra một sự cố đang diễn ra. Đây chính là 
 trụ Freshness, và nó là một dòng.
3. "Có biết record nào thất bại không?" — Câu này thường không trả lời được, và 
 chính việc không trả lời được là câu trả lời. Nếu pipeline của bạn không có dead-letter 
 queue, mọi record fail đều đã biến mất không dấu vết. Đếm: run gần nhất xử lý bao nhiêu record đầu 
 vào, ghi ra bao nhiêu chunk? Tỷ lệ đó có khớp kỳ vọng không?
4. "Có log được run ID và thời gian sync không?" — Mở một chunk bất kỳ trong kho ra 
 xem. Nó có pipeline_run_id không? Nếu không, lớp 4 của Hình 2 là ngõ 
 cụt với bạn, và Bài 1 ở trên không làm được trên hệ của bạn.
5. Tự chấm: bao nhiêu trong bốn câu bạn trả lời được bằng một lệnh trong dưới năm 
 phút? Bốn là tốt. Hai là bình thường. Không câu nào thì bạn đang ở đúng tình huống của 
 Mini-Quest 2 — và điều đó sửa được trong một buổi chiều.

#### Dựng pipeline Lab 10 cho artifact của bạn, 
 rồi cố tình phá dữ liệu và đo mức hỏng — checklist dưới đây gộp cả trace của Ngày 9 
 và Ngày 10 thành một đường liên tục

Không có đáp án — nhưng có bảng tự chấm.

bảy trường

slide 23

chunk_id

tất định

doc_id:index

upsert

incremental sync

trước

đã đo tỷ lệ chặn oan

Mô-đun 2

dead-letter queue

Freshness

Volume

tám trường

slide 33

đi thử một lần

bộ 30 câu hỏi cố định

không

phá dữ liệu có kiểm soát

bảng chương 12

chỉ số nào lẽ ra phải kêu

embedding_model

---

<!-- chiron-source-span: {"source_span_id":"a22c335a-73b1-59bf-907f-62fc18b9eeb7","locator":{"kind":"html_section","section_id":"misc","order":16,"heading":"✕ 6 hiểu lầm phổ biến","source_file":"slide-day10.html"},"checksum":"82778d960f7f4c0c2bd7a42086f1e4643a5c0d1966ba82b99555e516e7842247"} -->

## ✕ 6 hiểu lầm phổ biến

Mỗi ô: điều nhiều người tin → điều slide (hoặc phép tính) thật sự nói → vì sao khác 
 biệt quan trọng. Ba ô cuối là hiểu lầm mà *chỉ phép tính mới lộ ra*.

"Agent trả lời sai thì vấn đề nằm ở model hoặc prompt. Đổi model tốt hơn, hoặc viết prompt kỹ 
 hơn, là hướng sửa đúng."

Slide 28

"nhiều lỗi nhìn giống model hallucination nhưng gốc 
 rễ thực ra là data pipeline bug."

Hình 1

không cái nào sửa được 
 bằng prompt

retrieved_chunk_ids

Hình 2

"Sync càng thường xuyên càng tốt — chạy mỗi giờ thì data luôn mới, không có nhược điểm gì."

hai

slide 17

Mô-đun 1

không ảnh hưởng gì

cả hai

một giờ

nhân với nhau

Sửa idempotency trước, 
 tăng tần suất sau.

"Quality gate càng nhiều càng an toàn. Năm gate ở slide 27 là danh sách tối thiểu, có thêm thì 
 càng tốt."

chặn oan

Mô-đun 2

48,7

37,0

Tối ưu là ba.

không

đo tỷ lệ chặn oan

chính xác

nghiêm

PII gate không đi qua phép tính kỳ 
 vọng

"Pipeline chạy xong báo success, dashboard xanh hết, nghĩa là data trong kho dùng được."

Slide 17

"1 file sync fail có thể 
 khiến policy mới không tới agent"

Mini-Quest 3

cả sáu bước

Slide 37

100%

"status: ok"

Ngày 9

mô hình embedding không bao giờ báo lỗi

trước

"Observability là dự án lớn — cần nền tảng, cần ngân sách, để làm sau khi hệ đã ổn định."

Freshness

MAX(updated_at)

Volume

Mô-đun 3

63 người

88%

93%

5 điểm phần trăm

tuyến tính

rút ngắn lag

hai câu truy vấn là việc của chiều nay; nền 
 tảng là việc của quý sau.

"Hệ ít người dùng thì ít cần giám sát — khách hàng sẽ báo cho mình, và thiệt hại cũng nhỏ."

Ngược lại ở vế thứ nhất.

0,86 người/giờ

11,6 giờ

chậm hơn

slide 32

tệ hơn

giá trị mỗi lượt

Với hệ lưu lượng thấp và giá trị mỗi lượt 
 cao — kiosk, y tế, tài chính — giám sát tự động không phải tuỳ chọn, vì bạn không có đủ người dùng 
 để làm cảm biến.

---

<!-- chiron-source-span: {"source_span_id":"a9ac178f-2dff-5c15-a347-3fa2f07cb4dd","locator":{"kind":"html_section","section_id":"apply","order":17,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-day10.html"},"checksum":"1471f64730e5c840d28f80e3828790b3a2700967e3a6a5a999d0692e8e330d59"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI là agent check-in tại kiosk khách sạn, dựng trên LangGraph. Ngày 10 hỏi 
 câu chưa bài nào hỏi: *dữ liệu vào nó đến từ đâu, và làm sao biết khi nào nó sai?* Câu trả lời 
 khác hẳn mẫu RAG tài liệu mà deck lấy làm ví dụ — và khác ở chỗ quan trọng.

tài liệu

quan trọng nhất

SLA freshness của SmartCheck không thể là một con số duy nhất.

slide 32

### ① Bốn nguồn, bốn SLA khác nhau tới ba bậc độ lớn

| Nguồn | Dữ liệu cũ bao lâu thì bắt đầu gây hại | SLA freshness | Hỏng thì khách thấy gì |
| --- | --- | --- | --- |
| PMS — trạng thái đặt phòng | Phút — khách vừa đổi phòng qua tổng đài | < 2 phút — nên đọc trực tiếp, không cache | Kiosk cấp thẻ cho phòng đã có người |
| Phòng trống / dọn xong | Phút tới chục phút | < 5 phút | Khách được xếp phòng chưa dọn |
| Chính sách, phụ phí | Ngày | < 24 giờ | Báo sai phí huỷ, sai giờ nhận phòng |
| SOP, hướng dẫn nội bộ | Tuần | < 7 ngày | Hướng dẫn lỗi thời, ít ảnh hưởng khách |

**Đọc bảng này:** hai hàng trên và hai hàng dưới là *hai kiến trúc khác nhau*, không 
 phải hai ngưỡng khác nhau của cùng một pipeline. Hai hàng trên không nên đi qua vector store chút nào — 
 chúng phải là **tool call đọc trực tiếp PMS** tại thời điểm hỏi. Hai hàng dưới mới là RAG.

tất cả

Nó hỏng theo cách tệ nhất có thể:

không có chỉ số nào ở chương 08 bắt được

Quy tắc rút ra:

giá trị của nó thay đổi nhanh hơn chu kỳ 
 sync

slide 13

không

đọc trực tiếp

### ② Lưu lượng thấp — và vì sao điều đó làm phát hiện KHÓ hơn

Chạy [Mô-đun 3](#m-obs) với tham số SmartCheck (2.475 lượt/tháng = 82,5 lượt/ngày, 25% 
 chạm vùng dữ liệu hỏng):

| Chỉ số | Ví dụ của deck (slide 32) | SmartCheck |
| --- | --- | --- |
| Lưu lượng | 250 truy vấn/giờ | 3,4 lượt/giờ (7,2 lúc cao điểm) |
| Người bị ảnh hưởng mỗi giờ | 62,5 | 0,86 |
| Thời gian tới khiếu nại đầu tiên (giả định 1/10 người khiếu nại) | — | 11,6 giờ |
| Người bị ảnh hưởng nếu chờ khiếu nại | 500 | 10 người |
| Nếu có freshness check mỗi giờ | 63 | 0,9 người |

Đọc theo cột "người bị ảnh hưởng":

Đọc theo hàng "thời gian tới khiếu nại":

chậm hơn

bạn có ít cảm biến người hơn

Cái quyết định là giá trị mỗi lượt, không phải số lượt.

Ngày 6

năng lực giờ cao điểm

Kết luận đúng:

hơn

### ③ Quality gate — và một gate không có trong danh sách năm gate

| Gate | Áp cho SmartCheck thế nào | Cân được bằng phép tính không |
| --- | --- | --- |
| Schema | Chunk chính sách phải có effective_date và property_id | Có |
| Freshness | Bốn ngưỡng khác nhau theo bảng ① — không phải một | Có |
| Content | OCR confidence của bản scan chính sách | Có |
| Dedup | chunk_id = doc_id:index, upsert | Có |
| PII | Không embed số CCCD, số thẻ, số điện thoại khách | Không — hậu quả không đảo ngược |
| Property scope (thêm) | Chunk của khách sạn A không được lọt vào truy vấn của khách sạn B | Không — cùng loại với PII |

Ngày 6

6 cơ sở

chunk của 
 khách sạn A trả lời cho khách của khách sạn B

trông hoàn toàn hợp lệ

khớp ngữ nghĩa rất tốt

ưu tiên

con số

Đối sách:

property_id

hard filter ở tầng truy 
 vấn

Ngày 7

pre-filter

### ④ Khuyến nghị

① Chuyển dữ liệu PMS ra khỏi vector store — tuần này.

không

property_id

③ Hai truy vấn giám sát, chạy trong cron.

từng nguồn

11,6 giờ

nửa giờ

chunk_id

Mô-đun 1

Không làm:

slide 41

"hệ RAG/agent nhỏ thường bắt đầu bằng cron + 
 Python."

---

<!-- chiron-source-span: {"source_span_id":"84a863f0-80d2-5c05-a1a5-bf98e2e924b0","locator":{"kind":"html_section","section_id":"numbers","order":18,"heading":"# Con số cần kiểm chứng","source_file":"slide-day10.html"},"checksum":"c5a6244df765f9033d6450f97e73e4df0134eb3a10c27a6f5197c99a22d1ede4"} -->

## # Con số cần kiểm chứng

Ranh giới giữa *số của slide* và *số của tài liệu này*. Ngày 10 là bài 
 hiếm hoi có một con số gốc đáng dùng — và đúng một con số.

Slide 32

8 giờ

500 users

Mô-đun 3

latency_ms

slide 33

Không có con số nào về tỷ lệ lỗi, tốc độ tích rác, hay chi phí giám sát.

| Con số | Nguồn | Cần kiểm gì trước khi dùng |
| --- | --- | --- |
| 8 giờ · 500 users · 62,5 người/giờ | Slide 32 — hai số đầu là của deck, số thứ ba là phép chia | Deck không nói hệ đó lớn cỡ nào. 62,5 người/giờ ngụ ý khoảng 250 truy vấn/giờ nếu 25% chạm vùng 
 hỏng — nhưng tỷ lệ 25% là giả định của tài liệu này |
| Freshness check mỗi giờ → 63 người, giảm 8,5 lần · 
 realtime → 36 người | Tính ra | Giả định: sự cố rơi ngẫu nhiên đều trong chu kỳ kiểm, nên lag trung bình = T/2. Nếu sự 
 cố hay xảy ra ngay sau lần kiểm (ví dụ luôn ở run 2 giờ sáng) thì lag thật tiến tới T, không phải 
 T/2 — và con số xấu đi gấp đôi |
| Hoàn vốn sau 2,8 lần sự cố | Tính ra | Rất nhạy với thiệt hại mỗi người — tham số bịa đặt nhất trong cả tài liệu. 30 nghìn đ 
 chỉ là một điểm neo để thấy hình dạng; hãy thay bằng con số của bạn (chi phí xử lý một khiếu nại, 
 hoặc giá trị vòng đời khách hàng nhân xác suất rời bỏ) |
| Nửa kho là rác sau 50 ngày (incremental + insert) hoặc 
 1 giờ (full re-sync + insert) | Tính ra — t½ = 1/g và t½ = 1/R | Giả định: mỗi tài liệu đổi thì toàn bộ chunk của nó được chèn lại. Nếu pipeline chỉ chèn 
 lại chunk đã thay đổi thì chậm hơn. Ngược lại, giả định "tài liệu đổi độc lập với nhau" hay sai — 
 thực tế hay có một đợt cập nhật hàng loạt làm tích rác thành bậc thang chứ không mượt |
| 2,0% tài liệu đổi mỗi ngày · 24 lần sync/ngày · 2.000 tài liệu × 8 chunk | Giả định của tài liệu này | Tham số minh hoạ. Tỷ lệ tài liệu đổi mỗi ngày là con số bạn phải tự đo — một 
 truy vấn COUNT(*) WHERE updated_at > now() - 1 day ở nguồn |
| Sau 30 ngày: 37,5% rác · 3,13/5 chunk còn hiệu lực · 
 61,9% khả năng lặp ý | Tính ra | Con số "khả năng lặp ý" giả định các chunk trong top-k độc lập về việc là bản 
 cũ hay mới. Thực tế bản cũ và bản mới của cùng tài liệu có điểm tương đồng gần như bằng nhau 
 nên hay cùng vào top-k — làm con số thật CAO hơn ước lượng này |
| 5 gate → 48,7 câu hỏng/ngày · 3 gate → 37,0 · 
 tối ưu là ba gate | Tính ra | Ba giả định đáng ngờ: ① các gate độc lập — thực tế chúng chồng lấn, nên hiệu quả biên 
 giảm nhanh hơn; ② mọi gate có cùng recall và cùng tỷ lệ chặn oan — sai rõ, PII gate khác hẳn schema 
 gate; ③ một câu sai vì chunk bẩn ngang giá một câu hỏng vì thiếu bằng chứng — điều 
 này không đúng với PII gate và không đúng với gate ranh giới dữ liệu |
| 3,0% record bẩn · mỗi gate bắt 70%, chặn oan 0,50% · 2.000 truy vấn/ngày | Giả định của tài liệu này | Tỷ lệ chặn oan là tham số quyết định toàn bộ kết luận và gần như không ai đo nó. 
 Cách đo: lấy 200 record mà gate đã chặn, đọc tay, đếm bao nhiêu cái thật ra không sao. Một buổi 
 chiều, và nó đổi hẳn câu trả lời "nên có mấy gate" |
| SmartCheck: 82,5 lượt/ngày · 0,86 người/giờ · khiếu nại đầu tiên sau 
 11,6 giờ | Tính ra từ 2.475 lượt/tháng của Ngày 6 | Giả định 1/10 người bị ảnh hưởng sẽ khiếu nại — con số này là phỏng đoán và 
 thay đổi rất mạnh theo kênh: khách đứng trước kiosk hỏng lúc nửa đêm khiếu nại nhiều hơn nhiều so 
 với người dùng chat gặp câu trả lời hơi sai |
| SmartCheck: 25% lượt chạm vùng dữ liệu hỏng · 4 ngưỡng freshness (2 phút / 5 phút / 24 giờ / 
 7 ngày) | Giả định của tài liệu này | Bốn ngưỡng là suy luận từ bản chất từng nguồn, không phải số đo. Nhưng việc chúng phải khác 
 nhau thì không phải giả định — đó là hệ quả trực tiếp của việc trạng thái đặt phòng đổi theo phút 
 còn SOP đổi theo tuần |

① Tỷ lệ tài liệu đổi mỗi ngày ở nguồn.

Mô-đun 1

đủ

source_doc_id

GROUP BY source_doc_id HAVING COUNT(*) > kỳ vọng

③ Tỷ lệ chặn oan của từng gate.

Mô-đun 2

embedding_model

một

embedding drift ở slide 37

---

<!-- chiron-source-span: {"source_span_id":"ad09a4b7-e663-5e3a-9b41-d6f4b4d8d1ee","locator":{"kind":"html_section","section_id":"cheat","order":19,"heading":"▣ Cheat sheet ôn thi","source_file":"slide-day10.html"},"checksum":"a4e8f5d6c3cc6fe57fda34bb7f4f07536701392194f51268adb2c75a29fbea12"} -->

## ▣ Cheat sheet ôn thi

Những thứ nên nhớ được mà không cần mở lại tài liệu.

| Danh sách | Các mục | Slide |
| --- | --- | --- |
| AI data stack (5 tầng) | Sources → Pipeline → Storage → Serving → Agent | 6 |
| Pipeline RAG (6 bước) | Docs → Ingest → Transform → Index → Retrieve → Agent | 8 (+ Hình 1 ) |
| ETL / ELT | Transform trước khi lưu / sau khi lưu · hybrid: ETL riêng phần nhạy cảm | 10–12 |
| Ingestion tốt (3) | Incremental sync · Idempotent upsert · Source versioning | 17 (+ Mô-đun 1 ) |
| Chunk tốt (7 trường) | content · chunk_id · source_doc_id · section/title · effective_date · 
 owner/department · version/updated_at | 23 |
| 6 chiều chất lượng | Completeness · Accuracy · Consistency · Timeliness · Validity · Uniqueness | 25 |
| 5 quality gate | Schema · Freshness · Content · Dedup · PII | 27 (+ Mô-đun 2 ) |
| 5 trụ observability | Freshness · Distribution · Volume · Schema · Lineage | 31 |
| 5 lớp debug | Output → Retrieval → Index → Pipeline → Source | 33 (+ Hình 2 ) |
| 8 trường trace | request_id · pipeline_run_id · retrieved_chunk_ids · source_doc_ids · 
 source_version · embedding_model · latency_ms · fallback_used | 33 |

"Nhiều lỗi nhìn giống model hallucination nhưng gốc rễ thực ra là data pipeline 
 bug."

"BI sai → số sai trên báo cáo. Agent sai → hành động hoặc trả lời sai trực tiếp với user."

"Nếu bạn chỉ nhìn final answer mà không trace được về chunk và source document, bạn đang 
 debug trong bóng tối."

"Idempotency là bắt buộc: chạy lại pipeline 2 lần phải cho kết quả giống chạy 1 lần."

"Observability tốt phải nối được data issue → retrieval issue → business impact."

| Câu hỏi | Con số | Nguồn |
| --- | --- | --- |
| Không giám sát thì bao nhiêu người bị ảnh hưởng? | 500 trong 8 giờ = 62,5/giờ | Slide 32 (số gốc) |
| Cron kiểm freshness mỗi giờ cắt được bao nhiêu? | Còn 63 người — giảm 8,5 lần (88%) | Mô-đun 3 |
| Nền tảng realtime hơn cron mỗi giờ bao nhiêu? | 93% so với 88% — hơn 5 điểm phần trăm | Mô-đun 3 |
| Thiếu upsert, còn incremental sync → nửa kho mục sau? | 50 ngày ( t½ = 1/g ) | Mô-đun 1 |
| Thiếu cả hai → nửa kho mục sau? | 1 giờ ( t½ = 1/R ) · 96% sau một ngày | Mô-đun 1 |
| Tăng tần suất sync có làm rác nhanh hơn không? | Không — nếu có incremental sync. Có, nếu không | Mô-đun 1 |
| Nên có mấy quality gate? | Ba ở tỷ lệ chặn oan 0,50% · năm ở 0,02% | Mô-đun 2 |

① "Sáu chiều chất lượng đều kiểm được bằng Great Expectations."

Accuracy

② "Quality gate đặt ở đâu cũng được, miễn có."

trước

mô hình embedding không bao giờ báo lỗi

③ "Smoke test retrieval là lưới an toàn cuối."

Hình 3

④ "Embedding coverage 100% nghĩa là index khoẻ."

đã embed chưa

embed bằng gì

embedding_model

---

<!-- chiron-source-span: {"source_span_id":"eff76b38-af34-5557-b90f-3b94afe7ec6f","locator":{"kind":"html_section","section_id":"gloss","order":20,"heading":"☰ Từ điển thuật ngữ","source_file":"slide-day10.html"},"checksum":"282b1d124d95b665b3b6b1ff19df23d4574d96cb82e0ea2fcee4ad7b026ade11"} -->

## ☰ Từ điển thuật ngữ

Định nghĩa theo cách dùng được trong bài thi và trong công việc, không phải theo cách 
 tra từ điển.

---

<!-- chiron-source-span: {"source_span_id":"2d9f5858-6021-500d-b610-d33469dfc891","locator":{"kind":"html_section","section_id":"bloom","order":21,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-day10.html"},"checksum":"bd9589d8ccddecb8acee3e1f62835149a77eec786dd1ed7c3ad75bd0a3278bbb"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab 10 chấm mức 3–4; deliverable thứ tư 
 (so sánh trước/sau khi phá dữ liệu) chạm mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 6 bước pipeline RAG, 6 chiều chất lượng, 5 quality gate, 5 trụ observability, 5 lớp 
 debug, 7 trường của một chunk, 8 trường trace. | Cheat sheet · Hình 1 · Hình 2 |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao ELT hợp với hệ RAG đang xây; và vì sao quality gate 
 phải đứng trước bước chunk chứ không phải sau bước embed. | Slide 10–12 · Hình 3 · hiểu lầm 4 |
| 3 · Áp dụng | Dựng pipeline có chunk_id tất định, upsert, quality gate đặt đúng chỗ, và trace log 
 đủ 8 trường. Trả lời được cả bốn câu của checklist slide 18 bằng lệnh chạy được. | Slide 17–18 · Bài 2 · chương 05 |
| 4 · Phân tích | Cho một câu trả lời sai, trace ngược năm lớp và chỉ ra lớp nào là gốc — rồi nói được 
 cần thêm chỉ số nào để lần sau nó tự hiện lên thay vì đợi khách hàng báo. | Hình 2 · Mini-Quest 2 · Bài 1 |
| 5 · Đánh giá | Nhìn một đề xuất "thêm quality gate" hoặc "dựng nền tảng observability" và nói được nó 
 có đáng không — bằng số: cắt được bao nhiêu phần trăm thiệt hại, chặn oan 
 bao nhiêu, hoàn vốn sau mấy lần sự cố. | Mô-đun 2 · Mô-đun 3 · 
 hiểu lầm 3 và 5 |
| 6 · Sáng tạo | Nhận ra rằng dữ liệu thay đổi nhanh hơn chu kỳ sync thì không thuộc về vector store chút 
 nào — nó phải là tool call — và thiết kế lại luồng theo tốc độ đổi của từng nguồn thay vì theo một 
 SLA chung. | Mục SmartCheck ① · slide 13 |

①

SELECT MAX(updated_at) FROM chunks

(Trụ Freshness, một dòng.)

②

source_doc_id

Đáp án đúng: một.

③

embedding_model

Đáp án đúng: một.

④

source_doc_id

Đáp án đúng: hai tập bằng nhau.

không chạy được

Mini-Quest 2
