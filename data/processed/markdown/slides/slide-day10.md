---
schema_version: 1
course_id: rag-intensive
document_id: "f066b8b8-3181-5aa8-8215-8dcc078b4a9e"
document_version_id: "65ab32f9-e609-5811-a6fa-3f3779188512"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Data Pipeline & Data Observability"
source_file: "slide day10.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\slide day10.pdf"
source_sha256: "349ff67056b0cd4a08b61e5eaeefaf236bcd523c302f7003a113d65fab6d2108"
parser_version: chiron-structured-markdown-v1
page_count: 50
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":50}"
language: vi
---

# Data Pipeline & Data Observability

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"32954264-1016-5785-9274-ef5871e990e5","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Data Pipeline & Data Observability","extraction_method":"pdf-text-layer"},"checksum":"13f0c371490b971a418c6e91e01e11c9f47d37e87e9131e98d3d81b4db74d6cb"} -->

## Slide 1 - Data Pipeline & Data Observability

AICB-P1 · Garbage in → garbage out — fix thế nào? T ên Giảng Viên VinUniversity · Phase 1 · 2026

---

<!-- chiron-source-span: {"source_span_id":"7c3b7a4a-44f3-563d-9bf0-7f5aa157c400","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"86a50dd47140dd8c2493544ebd0fe36a23f45d604eb8a7bfd8d15490599213de"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Agent của bạn dùng data từ database công ty. Đột nhiên data sai — agent hallucinate. Bạn có biết không?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"8ae94f85-428d-5e40-bb5d-4d6b71d5ce61","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội dung bài học","extraction_method":"pdf-text-layer"},"checksum":"7d4df27136cbdd2aa68e6b612ec65c4f23db58ba6ba17f543aff51b67f5efc20"} -->

## Slide 3 - Nội dung bài học

1. Data Pipeline Fundamentals

2. Ingestion — Thu Thập Data T ừ Nhiều Nguồn

3. Transform — Làm Sạch & Chuẩn Hóa Data

4. Data Quality — 6 Dimensions

5. Data Observability

6. ETL Automation & Orchestration Giảng viên (VinUni) AICB · Data Pipeline 2026 1 / 39

---

<!-- chiron-source-span: {"source_span_id":"cea226dd-a6d4-5f3b-91d1-34d9ca935e1c","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"T ại Sao Data Pipeline Là Nền T ảng Của Mọi AI Product?","extraction_method":"pdf-text-layer"},"checksum":"6f2b8aa0bebeef7f053627bb813bef85160a91a6639fecb953cf57226b5b37f3"} -->

## Slide 4 - T ại Sao Data Pipeline Là Nền T ảng Của Mọi AI Product?

- 60–80% thời gian trong AI project thực
tế là data work — không phải model

- Một agent RAG xuất sắc vẫn hallucinate
nếu vector store được nạp data bẩn

- Garbage in → garbage out: quality của
output tỷ lệ thuận với quality của input data

- Observability = cơ chế phát hiện data sai
trước khi user phàn nàn

### Thực tế dự án AI
20% — xây model/agent 80% — data collection, cleaning, pipeline, monitoring Agenda: Pipeline Fundamentals → Ingestion → Transform for AI → Quality Gates → Observability & Debugging → Orchestration → Lab Giảng viên (VinUni) AICB · Data Pipeline 2026 2 / 39

---

<!-- chiron-source-span: {"source_span_id":"9e3774aa-ad90-58ac-9c30-9a49dd825b05","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Data Pipeline Fundamentals","extraction_method":"pdf-text-layer"},"checksum":"999cd1f74b461241b6ab2a3d32eede8a88f436302c250377dc71a2560626cbd0"} -->

## Slide 5 - Data Pipeline Fundamentals

01 Hiểu chuỗi xử lý từ nguồn đến agent — ETL, EL T, Batch, Streaming

---

<!-- chiron-source-span: {"source_span_id":"8196635d-2189-5e33-8d36-347c2d9272d5","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Data Pipeline Là Gì?","extraction_method":"pdf-text-layer"},"checksum":"27e94f0329fa3e600d97f0fdf5fdbec6d69db5d53f949bf0d9ce762447a8f625"} -->

## Slide 6 - Data Pipeline Là Gì?

Data Pipeline — Chuỗi các bước tự động hóa việc thu thập, xử lý, và phân phối data từ nguồn đến đích

### AI Data Stack điển hình
Sources Pipeline Storage Serving Agent Sources: DB, API, files, streams Pipeline: ingest + transform Storage: warehouse, vector store Serving: API, cache layer Agent: LLM + tools + RAG Giảng viên (VinUni) AICB · Data Pipeline 2026 3 / 39

---

<!-- chiron-source-span: {"source_span_id":"c9d75be8-d023-5410-a2c2-c6887833f2c5","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Modern AI Data Stack 2026 — T ech Stack Thực T ế","extraction_method":"pdf-text-layer"},"checksum":"947164b4092381c385b4e0adf5c08fb54dcc283917eaec0de29a44c130fb75cd"} -->

## Slide 7 - Modern AI Data Stack 2026 — T ech Stack Thực T ế

Layer T ools 2026 Ingestion Airbyte / Fivetran (managed) + Debezium (CDC, chuẩn mở) Storage Lakehouse: S3/GCS + Iceberg hoặc Delta Lake (chi tiết: Day 18) Transform dbt (+ Fusion engine mới, viết lại bằng Rust) — contracts enforce schema Orchestration Airflow 3.0 (event-driven scheduling) hoặc Dagster (asset-centric, lineage sẵn có) Observability Monte Carlo / Elementary + OpenLineage (chuẩn in- terop bên dưới) Activation (optional) Reverse ETL (Census/Hightouch) — giống Serving→Agent, nhưng cho CRM Fivetran mua Census + sáp nhập dbt Labs; Datadog mua Metaplane — thị trường đang gộp lại quanh vài platform lớn. Giảng viên (VinUni) AICB · Data Pipeline 2026 4 / 39

---

<!-- chiron-source-span: {"source_span_id":"e0fdffa2-c975-592b-9ef3-a37477396df7","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Minh Họa — Pipeline Cho Một Agent Hỏi Đáp Nội Bộ","extraction_method":"pdf-text-layer"},"checksum":"cda2b1b3584702405fc6a23288c0617e211e5bf2b40f811233e0c6097db4237a"} -->

## Slide 8 - Minh Họa — Pipeline Cho Một Agent Hỏi Đáp Nội Bộ

Scenario: Agent trả lời câu hỏi về chính sách công ty, ticket hỗ trợ và SOP nội bộ. Docs Notion/PDF Ingest sync/OCR Transform clean/chunk Index embed/store Retrieve top-k Agent answer

- Nếu ingestion fail: tài liệu mới không vào store

- agent trả lời cũ

- Nếu transform sai: chunk xấu, metadata thiếu

- retrieve nhầm

- Nếu index lỗi: embed thiếu hoặc duplicate →
context méo

### Điểm khác với dashboard BI
BI sai → số sai trên báo cáo Agent sai → hành động hoặc trả lời sai trực tiếp với user

### Vì vậy pipeline cho AI cần thêm
chunking, metadata, embeddings, retrieval checks, trace logs Giảng viên (VinUni) AICB · Data Pipeline 2026 5 / 39

---

<!-- chiron-source-span: {"source_span_id":"363a27b6-6203-55ad-87f6-dc08768ed3f2","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Mini-Quest — ETL Hay EL T?","extraction_method":"pdf-text-layer"},"checksum":"8219e6604040e8296c9211efabbc3968cdbf1eed0fdb00888ad5ac34082080e3"} -->

## Slide 9 - Mini-Quest — ETL Hay EL T?

Trước khi học tiếp: ETL và EL Tkhác nhau ở đâu? Mỗi loại thường dùng công nghệ/tool gì? Khi nào bạn sẽ chọn ETL, khi nào chọn EL T cho một hệ thống AI/agent? Cá nhân — 8 phút tự tìm hiểu/nhớ lại (dùng phone hoặc kiến thức sẵn có) + 1–2 bạn chia sẻ. Gợi ý nếu bí: nghĩ theo hướng “transform trước hay sau khi lưu”. Giảng viên (VinUni) AICB · Data Pipeline 2026 6 / 39

---

<!-- chiron-source-span: {"source_span_id":"12b9033d-b314-5fdc-946b-30904cfe5d61","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"ETL vs. EL T — Khi Nào Dùng Cái Nào?","extraction_method":"pdf-text-layer"},"checksum":"bf09b2bbe800cfe7415e1f61334c2fd2c0d874905e6b3e660144879c2bffbd73"} -->

## Slide 10 - ETL vs. EL T — Khi Nào Dùng Cái Nào?

ETL (Extract → Transform → Load)

- Transformtrước khi load vào kho

- Phù hợp: data nhạy cảm, cần mask
trước khi lưu

- Ví dụ: redact PII trong ticket support
trước khi embed cho agent

- Tools: Talend, Informatica, custom
scripts EL T (Extract → Load → Trans- form)

- Load raw data, transform sau trong
kho

- Phù hợp: big data, cloud data
warehouses

- Ví dụ: load raw docs/logs trước, rồi
chunk + enrich trong lakehouse

- Tools: Spark SQL, BigQuery, custom
Python jobs Giảng viên (VinUni) AICB · Data Pipeline 2026 7 / 39

---

<!-- chiron-source-span: {"source_span_id":"3c307c74-c6f2-5d14-ab7f-089c250177aa","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Minh Họa ETL vs. EL T Trong Hệ AI","extraction_method":"pdf-text-layer"},"checksum":"328e820d22121b20db10b58d78456fe81a77306d2978e88c01816c48bb26515d"} -->

## Slide 11 - Minh Họa ETL vs. EL T Trong Hệ AI

ETL flow Sources Transform clean + mask Load warehouse / store

- Dùng khi cần lọc/ràng buộc trước khi lưu

- Hợp với data nhạy cảm, dữ liệu production
cho agent

- Ví dụ: redact PII rồi mới tạo embeddings
EL T flow Sources Load Raw lake / bronze Transform chunk + enrich

- Dùng khi cần giữ raw để replay, backfill,
thử nghiệm

- Hợp với RAG/ML có nhiều nguồn và logic
transform thay đổi liên tục

- Ví dụ: lưu raw docs trước, sau đó thử nhiều
chiến lược chunking Giảng viên (VinUni) AICB · Data Pipeline 2026 8 / 39

---

<!-- chiron-source-span: {"source_span_id":"0b2105bb-fd8f-50c3-bf8d-1befc5d8961f","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"AI/LLM/ML T eam Thường Chọn ETL Hay EL T?","extraction_method":"pdf-text-layer"},"checksum":"be648baace18d4486899ff32420131c6ab9c60e45dae81ecf23af0c35aa6b027"} -->

## Slide 12 - AI/LLM/ML T eam Thường Chọn ETL Hay EL T?

Chọn ETL nếu

- cần mask PII trước

- schema khá ổn định

- data đi vào agent phải
rất sạch

- muốn giảm rủi ro lưu raw
nhạy cảm Chọn EL T nếu

- nhiều nguồn, nhiều định
dạng

- phải backfill / replay
thường xuyên

- còn đang thử chunking,
labeling, feature engineering

- cần giữ raw cho audit
và experiment Thực tế Nhiều team dùng hy-

### brid
Load raw trước, nhưng ETL các phần nhạy cảm như PII, secrets, dữ liệu pháp lý trước khi index hoặc serve cho agent. Giảng viên (VinUni) AICB · Data Pipeline 2026 9 / 39

---

<!-- chiron-source-span: {"source_span_id":"58e6b383-c47c-583e-b3dc-ea38f5c4090e","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Batch vs. Streaming — Trade-offs","extraction_method":"pdf-text-layer"},"checksum":"7f90bad8a165424e974a9aa0688d9003897177ae18b507295d7e0b21531ed913"} -->

## Slide 13 - Batch vs. Streaming — Trade-offs

Batch Processing

- Xử lý theo lô, theo lịch (hourly/daily)

- Ưu: đơn giản, cost thấp, dễ debug

- Nhược: latency cao (data trễ vài
giờ)

- Dùng khi: training data, daily
reports, ETL Streaming Processing

- Xử lý realtime khi data xuất hiện

- Ưu: latency thấp (ms–giây)

- Nhược: phức tạp hơn, cost cao hơn

- Dùng khi: fraud detection, live agent
context Giảng viên (VinUni) AICB · Data Pipeline 2026 10 / 39

---

<!-- chiron-source-span: {"source_span_id":"b0b55588-2c6e-5522-ab4e-ef4ef8353d53","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Streaming Stack Cho Agent Real-Time Context","extraction_method":"pdf-text-layer"},"checksum":"02b906e6238143a2a927135b8de3d70c971c41050b5bb251e56097d61c6753a7"} -->

## Slide 14 - Streaming Stack Cho Agent Real-Time Context

### Kafka và các lựa chọn thay thế

- Kafka: vẫn là incumbent, ecosystem lớn
nhất

- Redpanda: Kafka-API-compatible, viết
bằng C++, ops đơn giản hơn, chi phí thấp hơn

- WarpStream: Kafka-API-compatible, lưu
trên object storage, tính phí theo usage

- Confluent (chủ Kafka) đang chuyển hướng
messaging sang Apache Flink như chuẩn stream processing

### Data quality cho streaming

- Schema Registry: chặn event sai format
ngay lúc ingest, không đợi batch check

- Flink / ksqlDB: viết rule kiểm tra realtime
— giá trị bất thường, thiếu ID, volume spike

- Khác batch: không thể chạy Great
Expectations suite hàng đêm trên stream vô hạn Case study thật: Grab Engineering dùng FlinkSQL để convert data contracts thành rule kiểm tra realtime — chạy production, không phải lý thuyết. Giảng viên (VinUni) AICB · Data Pipeline 2026 11 / 39

---

<!-- chiron-source-span: {"source_span_id":"f1ee0240-72a4-5ea2-9631-2c77e11223d1","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Ingestion — Thu Thập Data Từ","extraction_method":"pdf-text-layer"},"checksum":"6885b74013daf311b43f4cd0c6046bbf0e90492cbc6c32c72c73cc8b5db22cf4"} -->

## Slide 15 - Ingestion — Thu Thập Data Từ

02 Nhiều Nguồn Kết nối nguồn data đa dạng vào pipeline một cách đáng tin cậy

---

<!-- chiron-source-span: {"source_span_id":"0215bb37-a4e1-5524-a9d5-43bd24f05eec","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Các Loại Nguồn Data Phổ Biến","extraction_method":"pdf-text-layer"},"checksum":"9fc151c7653a25f17921df0d09aff2864000d3ec155db5550df6a939343bc965"} -->

## Slide 16 - Các Loại Nguồn Data Phổ Biến

Structured sources

- Databases (PostgreSQL, MySQL): CDC
để capture changes

- Data warehouses: Snowflake, BigQuery

- REST / GraphQL APIs: rate limits cần xử lý
Unstructured sources

- Files: CSV, JSON, Parquet, PDF, Word

- Object storage: S3, GCS, Azure Blob

- Web scraping: HTML → text extraction
Event streams

- Kafka / Kinesis: high-throughput event
bus

- Webhooks: push từ external services

- IoT sensors: time-series data
CDC — Change Data Capture — detect & capture mọi IN- SERT/UPDATE/DELETE trong database để sync realtime thay vì full scan. Debezium (build trên Kafka Connect) là tool mã nguồn mở chuẩn phổ biến nhất. Giảng viên (VinUni) AICB · Data Pipeline 2026 12 / 39

---

<!-- chiron-source-span: {"source_span_id":"b6c92100-ae3c-57fa-908c-e1f93958c0c6","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Ingestion Trong Hệ AI/Agentic","extraction_method":"pdf-text-layer"},"checksum":"775fe1185b8fb03cfa0761fc758e285e162139339245ca3bb5b5ede7c8d9c623"} -->

## Slide 17 - Ingestion Trong Hệ AI/Agentic

Trong hệ AI/agentic, ingestion thường

### lấy từ

- Knowledge sources: Notion, Confluence,
PDF, Word, SharePoint

- Transactional data: CRM, ticketing, order
DB, HR systems

- Logs + feedback: chat transcripts, tool
calls, thumbs up/down, escalation notes

### Thiết kế ingestion tốt cần

- Incremental sync: chỉ lấy phần changed
since last run

- Idempotent upsert: chạy lại không tạo
duplicate chunks

- Source versioning: biết bản nào mới nhất,
sync lúc nào Rate limiting: source API giới hạn req/min → cần exponential backoff Backpressure: consumer xử lý chậm hơn producer → cần buffer hoặc pause signal Retry logic: dead-letter queue cho failed records Thực tế AI: 1 file sync fail có thể khiến policy mới không tới agent Giảng viên (VinUni) AICB · Data Pipeline 2026 13 / 39

---

<!-- chiron-source-span: {"source_span_id":"fd656426-5b33-5e6a-b08c-49b063386f05","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Minh Họa Ingestion — Agent CSKH Nội Bộ","extraction_method":"pdf-text-layer"},"checksum":"2bbb533c9a8612bdf52a71ac7172e7eaa8f7f10e00dc82c911be391e32e09280"} -->

## Slide 18 - Minh Họa Ingestion — Agent CSKH Nội Bộ

Câu hỏi user: “Chính sách hoàn tiền mới nhất là gì?”

### Agent cần data từ nhiều nguồn

- CRM: đơn hàng, trạng thái giao dịch

- Policy docs: chính sách hoàn tiền theo từng
tháng

- Ticket history: case tương tự đã được xử lý ra
sao

- Escalation notes: khi nào agent phải chuyển
người thật Nếu ingestion thiếu 1 nguồn quan trọng, agent có

### thể

- trả lời bằng policy cũ

- không biết ngoại lệ business

- đề xuất hành động không đúng với trạng thái
đơn hàng

### Checklist ingestion cho AI

1. Có lấy đúng nguồn không?

2. Có lấy đủ bản mới nhất không?

3. Có biết record nào thất bại không?

4. Có log được run ID và thời gian sync không? Giảng viên (VinUni) AICB · Data Pipeline 2026 14 / 39

---

<!-- chiron-source-span: {"source_span_id":"1dc5b939-c460-5733-bb25-999cc7b69a76","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Transform — Làm Sạch &","extraction_method":"pdf-text-layer"},"checksum":"48f79b8e982b5b341e84b276feecd0af053b35d4369f6ea35f3d93093af3531b"} -->

## Slide 19 - Transform — Làm Sạch &

03 Chuẩn Hóa Data Biến raw data thành data agent có thể tin tưởng và sử dụng được

---

<!-- chiron-source-span: {"source_span_id":"00caea5c-9ec9-5998-ba42-1dba7a867e5d","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Data Cleaning — Các Vấn Đề Phổ Biến","extraction_method":"pdf-text-layer"},"checksum":"ad746a8016006c7f50e41c95ff3b0039e5c68d733f44c9293dd1a488d3692110"} -->

## Slide 20 - Data Cleaning — Các Vấn Đề Phổ Biến

- Missing values: NULL, empty string, “N/A”
— drop, impute, hoặc flag

- Outliers: giá trị bất thường ảnh hưởng
embedding quality

- Duplicates: cùng record xuất hiện nhiều
lần → dedup bằng hash hoặc fuzzy match

- Wrong formats: date “31/12/2024” vs
“2024-12-31” → standardize

- Encoding issues: UTF-8 vs Latin-1 → luôn
enforce UTF-8

### T ext normalization cho AI

- Lowercasing: tùy model, không phải lúc
nào cũng cần

- Unicode normalization: NFC/NFD cho
tiếng Việt

- Whitespace: collapse multiple spaces,
strip trailing

- HTML stripping: loại bỏ tags trước khi
embed

- Language detection: tách chunks theo
ngôn ngữ Schema validation: enforce data con- tracts — reject records không đúng schema thay vì để lọt vào model Giảng viên (VinUni) AICB · Data Pipeline 2026 15 / 39

---

<!-- chiron-source-span: {"source_span_id":"f37ff6b4-2586-51fa-9a51-539b7f80143d","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"dbt — Transformation as Code","extraction_method":"pdf-text-layer"},"checksum":"bc1a5b430618aa5e77c1660ceccf4430f0e4bff92d53dc75018be5fed028a03d"} -->

## Slide 21 - dbt — Transformation as Code

dbt (data build tool) — SQL transformation được version control, test và document — biến SQL thành software engineering workflow

### T ại sao dbt quan trọng

- Modularity: mỗi transform là một.sql
model riêng

- Lineage: tự động sinh DAG
dependency graph

- T esting: built-in tests (not-null,
unique, accepted-values)

- Documentation: auto-generate data
catalog

- Version control: PR review cho data
logic -- models/cleaned_docs.sql WITH raw AS (

```text
SELECT * FROM {{ ref( 'raw_documents') }}
),
cleaned AS (
```
SELECT id, TRIM(LOWER(content)) AS content, created_at::date AS doc_date FROM raw WHERE content IS NOT NULL AND LENGTH(content) > 50 )

```text
SELECT * FROM cleaned
Giảng viên (VinUni) AICB · Data Pipeline 2026 16 / 39
```

---

<!-- chiron-source-span: {"source_span_id":"93f77eac-157e-5132-a8c6-9adadea0af9f","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Transform Cho AI/RAG Khác BI Ở Điểm Nào?","extraction_method":"pdf-text-layer"},"checksum":"33bfa113b1138ae5cea92b80cd62c9eb1b3e53ba134bcf444070d0316ed11640"} -->

## Slide 22 - Transform Cho AI/RAG Khác BI Ở Điểm Nào?

Ý chính — BI thường transform để báo cáo; AI transform để model hiểu đúng ngữ cảnh và retrieve đúng evidence Các bước transform thường gặp

### trong AI

- Clean text: bỏ HTML, ký tự lỗi, OCR
noise

- Chunking: chia tài liệu thành đoạn
vừa ngữ nghĩa, vừa token budget

- Metadata enrichment: gắn source,
owner, version, effective date

- Redaction: loại PII/secrets trước khi
embed

- Canonicalization: chuẩn hóa tên sản
phẩm, mã đơn hàng, timestamp doc = load_pdf( "refund-policy.pdf") text = clean_text(doc.text) chunks = chunk(text, size=500, overlap=80)

### for i, chunk in enumerate(chunks)
write_record({ "chunk_id": f "{doc.id}:{i}", "content": chunk, "source_doc": doc. id, "version": doc.updated_at, "department": "support" }) Giảng viên (VinUni) AICB · Data Pipeline 2026 17 / 39

---

<!-- chiron-source-span: {"source_span_id":"dcba9811-dc14-553a-b810-38e85849b514","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Chunking & Metadata — Vì Sao Agentic Systems Cần Kỹ?","extraction_method":"pdf-text-layer"},"checksum":"8603cb54c89d339a06328fc32beb29efdc57bc0f0f9ed8b7c8b223677ea99e8a"} -->

## Slide 23 - Chunking & Metadata — Vì Sao Agentic Systems Cần Kỹ?

### Chunk quá to

- chứa nhiều chủ đề → retrieval mơ hồ

- tốn token, giảm chỗ cho reasoning

### Chunk quá nhỏ

- mất context quan trọng

- câu trả lời thiếu điều kiện hoặc ngoại lệ

### Metadata tốt giúp agent

- filter theo phòng ban, ngày hiệu lực, loại
tài liệu

- hiển thị citation đúng nguồn

- trace ngược về document gốc khi có lỗi
Chunk tốt thường cần content chunk_id source_doc_id section / title effective_date owner / department version / updated_at Lưu ý: Nhiều team chỉ embed “text thuần” mà quên metadata — re- trieve đúng đoạn nhưng không biết nó từ bản policy nào. Giảng viên (VinUni) AICB · Data Pipeline 2026 18 / 39

---

<!-- chiron-source-span: {"source_span_id":"1e98e430-bc81-52a6-8cfc-8b20ab1b43ac","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Data Quality — 6 Dimensions","extraction_method":"pdf-text-layer"},"checksum":"ddcc3113704ad450a69b7a955e4d68e3077c7e1f5b0bf0a2e68078bb731dfab9"} -->

## Slide 24 - Data Quality — 6 Dimensions

04 Đo lường chất lượng data trước khi nó đến tay agent

---

<!-- chiron-source-span: {"source_span_id":"ff550411-2fd8-562b-a7d2-18301744bd43","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"6 Dimensions Of Data Quality","extraction_method":"pdf-text-layer"},"checksum":"826f913f1605c9dd8cd11116c384cceba8f324b8024b6c78a21f7da479fd135c"} -->

## Slide 25 - 6 Dimensions Of Data Quality

1. Completeness Không thiếu records hoặc fields quan trọng. Check:% NULL, row count so với expected

2. Accuracy Data đúng với thực tế. Check: validate với nguồn gốc, business rules

3. Consistency Cùng entity, cùng format across systems. Check: cross-system reconciliation

4. Timeliness Data đủ fresh cho use case. Check: max age, last-updated timestamp

5. Validity Data theo đúng format và domain rules. Check: regex patterns, range checks

6. Uniqueness Không có duplicates. Check: dedup rate, composite key uniqueness Giảng viên (VinUni) AICB · Data Pipeline 2026 19 / 39

---

<!-- chiron-source-span: {"source_span_id":"0677530c-1856-53dc-9f9c-293ecc07e57a","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Great Expectations — Data Quality as Code","extraction_method":"pdf-text-layer"},"checksum":"f41bb8c08c20e185d4e8c8e286da8b0b3e80e1bb1cfd6e91e8e2494b2eda31b3"} -->

## Slide 26 - Great Expectations — Data Quality as Code

Great Expectations — Framework Python để viết, run và document data quality checks — “expectations” là assertions về data

### Workflow cơ bản

1. Profile data: tự động suggest expectations

2. Write expectations: not-null, unique, in-range, regex

3. Validate trước khi data vào pipeline

4. Report: HTML data docs tự động sinh

5. Alert: fail pipeline nếu expectations không pass

```text
import great_expectations as gx
context = gx.get_context()
batch = context.sources.pandas_default\
.read_csv("docs.csv")
batch.expect_column_values_to_not_be_null(
```
"content" ) batch.expect_column_value_lengths_to_be_between( "content", min_value=50 ) results = batch.validate() print(results["success"]) # True / False Giảng viên (VinUni) AICB · Data Pipeline 2026 20 / 39

---

<!-- chiron-source-span: {"source_span_id":"56f2c362-61b4-525c-9c50-e485ef40a8f6","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Quality Gates Trước Khi Data Đến Agent","extraction_method":"pdf-text-layer"},"checksum":"a62341dca2c73996e03f87fe79e9eb15478875c9cd378381c56e8d9a88b3b152"} -->

## Slide 27 - Quality Gates Trước Khi Data Đến Agent

Ý chính — Trong AI pipeline, data quality không chỉ bảo vệ warehouse mà còn bảo vệ retrieval, tool use và final answer

### Các quality gates nên có

- Schema gate: có đủ content, doc_id,
updated_at

- Freshness gate: policy quá cũ thì
reject hoặc cảnh báo

- Content gate: text đủ dài, OCR
confidence không quá thấp

- Dedup gate: cùng chunk không được
nạp nhiều lần

- PII gate: không embed số thẻ, mật
khẩu, access token

```text
def validate(record):
assert record["content"].strip()
assert record["updated_at"] >= cutoff_date
assert len(record["content"]) >= 80
assert not contains_secret(record["content"])
```
assert record["chunk_id"] not in seen_ids

### for record in cleaned_records
validate(record) Giảng viên (VinUni) AICB · Data Pipeline 2026 21 / 39

---

<!-- chiron-source-span: {"source_span_id":"237c0fc0-7a62-5233-8680-31459667728d","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Nếu Quality Kém, Agent Sẽ Sai Kiểu Gì?","extraction_method":"pdf-text-layer"},"checksum":"87bbed017e1620d46341195a8ebb1ad1ff4cd5e87571acb954cdd40f0c2c09ca"} -->

## Slide 28 - Nếu Quality Kém, Agent Sẽ Sai Kiểu Gì?

Data issue

- Missing documents

- Outdated version

- Duplicate chunks

- Wrong metadata

- Secret leakage
Agent symptom

- không tìm thấy bằng chứng liên quan

- trả lời dựa trên policy cũ

- lặp lại cùng một ý nhiều lần

- cite sai phòng ban / sai ngày hiệu lực

- làm lộ dữ liệu nhạy cảm cho user
Điểm dạy học quan trọng: nhiều lỗi nhìn giống “model hallucination” nhưng gốc rễ thực ra là data pipeline bug. Giảng viên (VinUni) AICB · Data Pipeline 2026 22 / 39

---

<!-- chiron-source-span: {"source_span_id":"39aeaf6e-26d6-5209-83df-22c0f6ea9fdf","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Data Observability","extraction_method":"pdf-text-layer"},"checksum":"1737db0411591ad1a2ec2c5de64791b72b0814f5cdfc837a3406a5702fb70796"} -->

## Slide 29 - Data Observability

05 Monitor, alert và debug data problems trước khi agent bị ảnh hưởng

---

<!-- chiron-source-span: {"source_span_id":"2046ea83-030a-5d4d-9684-4d9038144829","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Mini-Quest — Agent Trả Lời Sai, Bạn Check Gì Trước?","extraction_method":"pdf-text-layer"},"checksum":"7a976b7c2f03e932c3ed852b15dc9634cfec111fffea06a5f35c1dd275eaf3d2"} -->

## Slide 30 - Mini-Quest — Agent Trả Lời Sai, Bạn Check Gì Trước?

Agent RAG của bạn đang trả lời sai — thông tin cũ, khách hàng phàn nàn. Bạn có 10 phút, agent này không có logging/observability nào cả. Bạn sẽ kiểm tra những gì đầu tiên để tìm nguyên nhân? Liệt kê ý tưởng của bạn. Cá nhân — 8 phút brainstorm + 2–3 bạn chia sẻ ý tưởng. Gợi ý nếu bí: nghĩ theo hướng “data có mới không, có đủ không, có lỗi gì không”. Giảng viên (VinUni) AICB · Data Pipeline 2026 23 / 39

---

<!-- chiron-source-span: {"source_span_id":"4c3dbc0d-e252-543b-8b58-516bc11ea590","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"5 Pillars Of Data Observability","extraction_method":"pdf-text-layer"},"checksum":"e22f16f31fe0fabc3b571f3731edeaf595c686ef7e939da0d79ade5be6a6a5ea"} -->

## Slide 31 - 5 Pillars Of Data Observability

Freshness — Data có đang được update theo đúng lịch? Distribution — Giá trị phân phối có bất thường không? (null rate, range) Volume — Số lượng records tăng/giảm bất thường? Schema — Cột bị đổi tên, thêm, xóa không? Lineage — Data đến từ đâu, đi qua transform nào? Data Lineage — Track hành trình data từ nguồn gốc→ pipeline

- chunk/index → retrieved con-
text → model output Muốn debug được, phải log ít

### nhất

- question / session ID

- retrieved chunk IDs

- source document version

- embedding/index version

- pipeline run ID
Giảng viên (VinUni) AICB · Data Pipeline 2026 24 / 39

---

<!-- chiron-source-span: {"source_span_id":"d245cd3b-c2c0-54fc-88af-ebe026719468","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Observability in Practice — Phát Hiện Data Issues Sớm","extraction_method":"pdf-text-layer"},"checksum":"0842231e3aea2636fb9fd3169403011adf7a187d9751a5c79c398504f61417f4"} -->

## Slide 32 - Observability in Practice — Phát Hiện Data Issues Sớm

Scenario: RAG agent trả lời sai

1. User phàn nàn agent đưa thông tin cũ

2. Check answer trace: agent đã retrieve chunk nào?

3. Check Freshness: chunk đó thuộc policy version ngày nào?

4. Check Volume: số documents embed hôm nay có drop về 0 không?

5. Trace Lineage: ingestion run 2am fail ở bước sync policy

6. Root cause: API timeout, retry/backoff chưa cấu hình đúng

### Monitoring metrics cần theo dõi

- Pipeline SLA:% runs hoàn thành đúng
giờ

- Row count delta: ∆ records qua các
runs

- Null rate per column: alert nếu tăng đột
biến

- Schema drift: tự động detect column
changes

- Data freshness: max age của records
trong store

- Embedding coverage:% chunks đã
được embed Không có observability: phát hiện sau 8 giờ, 500 users bị ảnh hưởng Giảng viên (VinUni) AICB · Data Pipeline 2026 25 / 39

---

<!-- chiron-source-span: {"source_span_id":"ac9f628b-408f-5800-a90a-168b397a4041","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Debug Agent Sai — Trace Từ Output Ngược Về Data","extraction_method":"pdf-text-layer"},"checksum":"95776f283f55dd30f6d6a840e94150320a261606d20ce12aad6744b8aa9e3db0"} -->

## Slide 33 - Debug Agent Sai — Trace Từ Output Ngược Về Data

### Quy trình debug nên đi theo 5 lớp

1. Output layer: agent trả lời gì, cite gì, confidence ra sao?

2. Retrieval layer: top-k chunks nào được lấy ra? có zero-hit không?

3. Index layer: chunk đó được embed bằng model/version nào?

4. Pipeline layer: run nào sinh ra chunk? pass/fail quality gates nào?

5. Source layer: tài liệu gốc có đúng, mới và đầy đủ không? Lưu ý: Nếu bạn chỉ nhìn final an- swer mà không trace được về chunk và source document, bạn đang debug trong bóng tối.

### Fields nên có trong trace log

- request_id

- pipeline_run_id

- retrieved_chunk_ids

- source_doc_ids

- source_version

- embedding_model

- latency_ms

- fallback_used
Giảng viên (VinUni) AICB · Data Pipeline 2026 26 / 39

---

<!-- chiron-source-span: {"source_span_id":"ba052122-822f-5031-97dd-044e0b7daeb0","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Observability Cho Agentic Systems — Không Chỉ Là Data Metrics","extraction_method":"pdf-text-layer"},"checksum":"53f2de7e8bc68ce3722f606cfc98746f7ec2bd48238ea445e47360b4622c5271"} -->

## Slide 34 - Observability Cho Agentic Systems — Không Chỉ Là Data Metrics

Pipeline / data signals

- freshness của knowledge base

- failed sync count, dead-letter queue size

- duplicate chunk rate

- missing metadata rate

- embedding queue lag
Agent / product signals

- retrieval hit rate

- % answers có citation hợp lệ

- user correction / escalation rate

- tool-call failure rate

- abandoned conversations sau câu trả lời
sai Quan điểm thực chiến: observability tốt phải nối đượcdata issue → retrieval issue → business impact. Giảng viên (VinUni) AICB · Data Pipeline 2026 27 / 39

---

<!-- chiron-source-span: {"source_span_id":"63a43af7-15d4-5d46-b8d9-547deae22306","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"AI Agent Observability — Data Đâu Dừng, Model Tiếp Tục","extraction_method":"pdf-text-layer"},"checksum":"4a1f400f24b196f405a38e88dae8c7aeacc8aa9d3a311c6cca7263a9f956c1e6"} -->

## Slide 35 - AI Agent Observability — Data Đâu Dừng, Model Tiếp Tục

Trace & Span — Trace = một lần agent chạy end-to-end; Span = một bước bên trong (1 LLM call, 1 tool call, 1 retrieval) — cùng ý tưởng fresh- ness/volume/schema bạn vừa học, chỉ khác tầng đo: model thay vì pipeline

### Kiến trúc thực tế

- Agent call → instrument bằng
OpenTelemetry GenAI spans

- Gửi trace về Langfuse (self-host,
open-source), Phoenix (open-source, OpenInference), hoặc LangSmith (managed, free tier 5k trace/tháng)

- Score tự động bằng RAGAS (faithfulness,
context precision/recall)

- Alert khi quality hoặc cost drift
Lưu ý chọn tool: Helicone đã bị Mintlify mua (03/2026), giờ chỉ maintenance mode — không còn phát triển tính năng mới. Ưu tiên Langfuse/Phoenix nếu cần self-host lâu dài. Giảng viên (VinUni) AICB · Data Pipeline 2026 28 / 39

---

<!-- chiron-source-span: {"source_span_id":"13140814-4681-530d-8c5e-4597a3cd826d","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Demo: Trace Một RAG Call Với Langfuse","extraction_method":"pdf-text-layer"},"checksum":"827ceca154c166f9306d62687dc480eabd208e597ce7583a2c4bf63b32cecaa2"} -->

## Slide 36 - Demo: Trace Một RAG Call Với Langfuse

### Mỗi trace ghi lại

- Prompt gửi đi, response nhận về

- Token usage, latency, cost

- T ừng tool/retrieval step lồng bên
trong (nested spans) Agent trả lời sai → mở trace → xem span nào chậm/sai: retrieval hay generation?

```text
from langfuse import Langfuse
langfuse = Langfuse()
trace = langfuse.trace(
name="rag-query", input={"question": q}
)
retrieval = trace.span(name= "retrieval")
chunks = vector_store.search(q, top_k=5)
retrieval.end(output={"chunk_ids":
[c.id for c in chunks]})
generation = trace.generation(
name="generation", model= "gpt-4o-mini",
input=chunks,
usage={"input": 512, "output": 128},
)
Giảng viên (VinUni) AICB · Data Pipeline 2026 29 / 39
```

---

<!-- chiron-source-span: {"source_span_id":"d4f9fd54-0874-5f2e-b377-5680092f4e7a","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Đo Faithfulness Với RAGAS & Vector Store Health","extraction_method":"pdf-text-layer"},"checksum":"402998f590201eb87f873fe5e7daae8f164e26713d693f324007c47ab7acc729"} -->

## Slide 37 - Đo Faithfulness Với RAGAS & Vector Store Health

```text
from ragas.metrics import (
```
faithfulness, answer_relevancy )

```text
from ragas import evaluate
result = evaluate(
```
dataset, metrics=[faithfulness, answer_relevancy] ) # {'faithfulness': 0.83, # 'answer_relevancy': 0.91}

### Vector store health

- Qdrant / Weaviate: expose
Prometheus metrics (/metrics) — recall, latency, memory

- Embedding drift: retrieval quality
giảm dù “embedding coverage” vẫn 100% Lưu ý: Cost/token là trục alert riêng: 1 agent loop lỗi có thể x100 chi phí trong vài phút mà không hề có anomaly ở row count hay schema — track $/request và token delta giống cách bạn track row count delta. Giảng viên (VinUni) AICB · Data Pipeline 2026 30 / 39

---

<!-- chiron-source-span: {"source_span_id":"699091ad-d530-5e33-8f95-4c34db5477f4","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"ETL Automation &","extraction_method":"pdf-text-layer"},"checksum":"28a50c7474f53f456debaec6c4e19aabe0b83ba13b79793b86fb6f5b6881914f"} -->

## Slide 38 - ETL Automation &

06 Orchestration Đưa pipeline vào vận hành tự động, đáng tin cậy với error handling đúng chuẩn

---

<!-- chiron-source-span: {"source_span_id":"9f92b225-c46a-54e2-a08b-f98efc3cf58c","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Apache Airflow — DAG-Based Orchestration","extraction_method":"pdf-text-layer"},"checksum":"61378051dde6f6f275d8205031324dafe024287defa47580ce48d1659f4f4284"} -->

## Slide 39 - Apache Airflow — DAG-Based Orchestration

### Core concepts

- DAG (Directed Acyclic Graph): định nghĩa
thứ tự task

- Operator: đơn vị thực thi
(PythonOperator, BashOperator, …)

- Scheduler: trigger DAGs theo cron hoặc
event — Airflow 3.0 (2025) thêm event-driven native + DAG versioning

- Executor: chạy tasks (Local, Celery,
Kubernetes)

- XCom: truyền data nhỏ giữa tasks

### Khi nào dùng Airflow

- Batch pipeline phức tạp với nhiều
dependencies

- Team đã có Python skills

- Cần visibility đầy đủ qua UI

### Modern alternatives
Prefect Python-native, ít boilerplate hơn Airflow. Flows = Python functions. Phù hợp team muốn nhanh. Dagster Asset-centric orchestration — model data assets, không phải tasks. Built-in lineage & observability. Phù hợp data-heavy teams. Giảng viên (VinUni) AICB · Data Pipeline 2026 31 / 39

---

<!-- chiron-source-span: {"source_span_id":"3337f0ed-8974-5ca3-847b-a16e92ce1e55","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Orchestration Face-off 2026 — Chọn T ool Nào?","extraction_method":"pdf-text-layer"},"checksum":"a86f582598767026a166d1782c7e459e222b6066762a3f871eb76547f05eebee"} -->

## Slide 40 - Orchestration Face-off 2026 — Chọn T ool Nào?

T ool Best for 2026 update Airflow 3.0 Batch DAG phức tạp, ecosystem lớn Event-driven scheduling + DAG versioning (mới — trước đây chỉ cron/deps) Dagster Asset-centric, cần lin- eage/observability sẵn có Vẫn là lựa chọn nếu muốn lineage “miễn phí” Prefect Python-native, setup nhanh Positioning không đổi Mage AI Low-code, onboarding nhanh Entrant mới, đáng nhắc tên Kestra Workflow orchestration rộng hơn (không chỉ data asset) Entrant mới, đáng nhắc tên Giảng viên (VinUni) AICB · Data Pipeline 2026 32 / 39

---

<!-- chiron-source-span: {"source_span_id":"2bd97c40-a40e-5a5b-9472-051ef53208ed","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"AI/LLM/ML Systems Thường Dùng Gì Để Orchestrate?","extraction_method":"pdf-text-layer"},"checksum":"fe2db7a2d11999bb9ba6b212727786849e7b47b7c8770901ad4d0e3be90520ae"} -->

## Slide 41 - AI/LLM/ML Systems Thường Dùng Gì Để Orchestrate?

Airflow

### Hay dùng cho
batch ETL, retraining theo lịch, multi-step jobs

### Lý do
mature, nhiều operator, UI quen thuộc Prefect

### Hay dùng cho
Python pipelines, startup teams, flows cần code nhanh

### Lý do
ít boilerplate, local-to- cloud dễ Dagster

### Hay dùng cho
asset-heavy pipelines, lineage rõ, data platform teams

### Lý do
asset model hợp với tables, features, indexes Góc nhìn thực tế: hệ RAG/agent nhỏ thường bắt đầu bằng cron + Python; khi số bước, số nguồn, và số team tăng lên thì mới nâng lên Airflow / Prefect / Dagster. Giảng viên (VinUni) AICB · Data Pipeline 2026 33 / 39

---

<!-- chiron-source-span: {"source_span_id":"4fe79471-2666-5ffa-b42a-6426b5f2a97e","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Ví Dụ Orchestration Cho RAG / Agent Pipeline","extraction_method":"pdf-text-layer"},"checksum":"3451f2ba800fe0881d0b9ceb950a77871b7211fc5700e8e02c59f7a5cecfa04c"} -->

## Slide 42 - Ví Dụ Orchestration Cho RAG / Agent Pipeline

Sync docs/API Quality gate Chunk + metadata Embed Upsert vector store Smoke test retrieval Notify / alert

### Cách dùng trong thực tế

- Trigger: mỗi giờ, khi có file mới,
hoặc khi policy đổi

- Fail fast: quality gate fail thì không
cho index tiếp

- Smoke test: chạy vài câu hỏi chuẩn
để check retrieval

- Notify: báo Slack nếu index mới làm
hit rate giảm Lưu ý: Trong AI pipeline, or- chestration không chỉ “chạy jobs” mà còn kiểm soát chất lượng đầu vào trước khi agent dùng data mới. Giảng viên (VinUni) AICB · Data Pipeline 2026 34 / 39

---

<!-- chiron-source-span: {"source_span_id":"e4efd086-b507-5dfb-a2ec-3e14d7f54cab","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Mini-Quest — Pipeline Này Có Gì Sai?","extraction_method":"pdf-text-layer"},"checksum":"ddd196ca3ca4f7023d93d7bb410fae74b78119c9c6ec63b687b571e20be11669"} -->

## Slide 43 - Mini-Quest — Pipeline Này Có Gì Sai?

Sync docs/API Chunk + metadata Embed Upsert vector store Smoke test retrieval Notify / alert Đây là pipeline production của một startup X. Nhìn kỹ — so với những gì ta vừa học, pipeline này đang thiếu bước quan trọng nào? Điều gì sẽ xảy ra trong thực tế nếu một tài liệu bị lỗi (OCR hỏng, thiếu field) đi qua pipeline này? Cá nhân — 8 phút quan sát/tìm lỗi + 2–3 bạn chia sẻ. Giảng viên (VinUni) AICB · Data Pipeline 2026 35 / 39

---

<!-- chiron-source-span: {"source_span_id":"2e913efe-34a1-5762-ad48-fbba9b57f96b","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Error Handling & Scheduling Trong Pipeline","extraction_method":"pdf-text-layer"},"checksum":"e95512e0404f28644cfcc2a27432851e19f693c366821cb9261c8f566e267ede"} -->

## Slide 44 - Error Handling & Scheduling Trong Pipeline

### Scheduling strategies

- Cron-based: 0 2 * * * = 2am mỗi ngày —
đơn giản, predictable

- Event-driven: trigger khi file mới upload
hoặc webhook nhận được

- Dependency-based: chỉ chạy khi upstream
pipeline xong

- Backfill: chạy lại pipeline cho historical
dates

### Error handling patterns

- Retry với backoff: attempt 1 → 30s →
attempt 2 → 2m → …

- Dead Letter Queue: failed records
không bị mất, xử lý sau

- Partial failure: idempotent tasks để
re-run an toàn

- Alerting: Slack/email khi pipeline fail

- SLA breach: alert khi pipeline trễ so với
deadline Lưu ý: Idempotency là bắt buộc: chạy lại pipeline 2 lần phải cho kết quả giống chạy 1 lần. Thiếu idempotency dẫn đến duplicate data trong vector store. Giảng viên (VinUni) AICB · Data Pipeline 2026 36 / 39

---

<!-- chiron-source-span: {"source_span_id":"48359265-7733-51c8-a7b0-be75e519efd8","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Lab #10","extraction_method":"pdf-text-layer"},"checksum":"1f74efd60fad9c04eaa3cc2047817983504ffad657ee3d287c86a6d03aeec0b3"} -->

## Slide 45 - Lab #10

Mục tiêu: Build AI data pipeline hoàn chỉnh: thu thập raw docs, làm sạch, chunk, enrich metadata, embed và nạp vào vector store cho agent. Simu- late data corruption để đo impact lên retrieval và câu trả lời. Deliverable: (1) Pipeline script: raw → cleaned → chunked → embedded; (2) Quality gates cho schema/freshness/duplicates; (3) Trace log để debug agent answers; (4) So sánh response quality trước/sau fix data Thời gian: 4 giờ (Vibe Coding 1.5h + Lab 2.5h) Giảng viên (VinUni) AICB · Data Pipeline 2026 37 / 39

---

<!-- chiron-source-span: {"source_span_id":"0d205b7b-5051-50c4-b892-bc031956d2fb","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"6f83d1a0193b3e6fdc2938b78862af29a3bee6d1fd0e5a76251914b1c5507d73"} -->

## Slide 46 - T ổng kết — Key T akeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Data pipeline làhệ tuần hoàn của mọi AI product — agent mạnh đến đâu cũng vô dụng nếu data vào bị bẩn 2 Pipeline cho AI khác BI ở chỗ phải tối ưu cho retrieval, context quality, citations và khả năng debug agent 3 Data quality gates phải chặn thiếu dữ liệu, dữ liệu cũ, duplicate chunks, metadata sai và secret leakage 4 Observability tốt cho phép trace từ câu trả lời sai ngược về chunk, pipeline run và source document — và tiếp tục vào tận trace/span của model call Giảng viên (VinUni) AICB · Data Pipeline 2026 37 / 39

---

<!-- chiron-source-span: {"source_span_id":"383e22d5-a964-5e4f-804f-15ee20e981b9","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"6d349f3f4e6d595e14e5cb12f4cecc437b39865ad57f429df93ffdf87829c3ae"} -->

## Slide 47 - Tiếp theo & Bài tập

Guardrails & AI Safety “Agent hoạt động đúng không có nghĩa là an toàn — cần lớp bảo vệ ở mọi cấp”

- Đọc: OWASP Top 10 for LLMs
(owasp.org)

- Thực hành: Thêm
input/output validation vào ETL pipeline từ Lab 10

- Suy nghĩ: Agent của bạn có
thể bị poisoned data attack không? Giảng viên (VinUni) AICB · Data Pipeline 2026 38 / 39

---

<!-- chiron-source-span: {"source_span_id":"3fa07432-fc12-54b5-b078-33cb3f0e1cff","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"T ài Liệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"cf8844dd77720fddfdfbde8743a8186302c069e1ccd3521e4462b03d652984e7"} -->

## Slide 48 - T ài Liệu Tham Khảo

1. Hidden T echnical Debt in Machine Learning Systems— Sculley et al., Google, NeurIPS 2015. Giải thích tại sao 80% thời gian AI = data work. Kinh điển, đọc trước lớp (30 phút).

2. Designing Data-Intensive Applications — Martin Kleppmann. Nền tảng cực tốt để hiểu ingestion, streaming, idempotency, backpressure, và consistency trong hệ thống data.

3. Designing Machine Learning Systems — Chip Huyen. Góc nhìn production cho data pipelines, data quality, monitoring và feedback loops trong AI systems. Giảng viên (VinUni) AICB · Data Pipeline 2026 39 / 39

---

<!-- chiron-source-span: {"source_span_id":"4cfba56a-7805-5d84-a3c6-55500b337c8c","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"e881e30042f9d229c04304ea5526c769f272f53050d975e921bb4d13e9cfc30b"} -->

## Slide 49 - Hỏi & Đáp

Garbage in → garbage out. Bạn kiểm soát data quality bằng cách nào trong project của mình?

---

<!-- chiron-source-span: {"source_span_id":"07b7c4c3-67bc-5704-8b4c-a322e87c6cdb","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"4c24b11a8f01d09e87e43393f7a6842193ef57d86d76fee0d5aa80ee5b81d5c8"} -->

## Slide 50 - Cảm ơn!

Ngày tiếp theo: Guardrails & AI Safety labs + source code: github.com/vbi-academy/aicb-phase1
