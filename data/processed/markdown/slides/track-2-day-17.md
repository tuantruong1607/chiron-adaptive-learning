---
schema_version: 1
course_id: rag-intensive
document_id: "f14a9d99-de3a-5a83-9de6-ead7caf2685e"
document_version_id: "2f19650b-74ad-5642-bde4-ea926c6fdca9"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Data Pipeline Engineering"
source_file: "track 2 - day 17.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 17.pdf"
source_sha256: "8bfbc41ab1d70af7e65eaf6ceadfc307499964f772a621e0e9bb9e0088c85be6"
parser_version: chiron-structured-markdown-v1
page_count: 63
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":63}"
language: vi
---

# Data Pipeline Engineering

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"56261988-4053-5dbd-a717-e01922c44b3c","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Data Pipeline Engineering","extraction_method":"pdf-text-layer"},"checksum":"4f4cac4d458adf02c948fb604823c19ea7f6cf89b9ee29245eb566e09fd6e10c"} -->

## Slide 1 - Data Pipeline Engineering

AICB-P2T2 · Ngày 17 · Chương 4: Hạ Tầng · Xây đường ống dữ liệu nuôi AI Giảngviên VinUniversity · Phase 2 · Track2· Tuần4

---

<!-- chiron-source-span: {"source_span_id":"4799a80a-bcf0-5593-9202-e5427092a04b","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"d0d9903f768870f77ee3415eb8f6200ee57c9fc99cb92bad6bd1d6664045a071"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Team X train model trên data có 30% du- plicate records. Model memorize dupli- cates → hallucinate in production. 2 tuần + $8K GPU lãng phí — chỉ vì pipeline thiếu một bước dedup. Pipeline của bạn đang nuôi model, hay đang đầu độc nó? ” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"1093a936-ad03-564d-beb1-f63e8c9e6fe6","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"ffa52487c07a3da4de503e57ed1c3e366731d75aec46d231b0b4e6aabdd807f1"} -->

## Slide 3 - NộiDung Bài Học

1. Vìsao pipeline quyết định số phận model

2. ETLvs ELT& MedallionArchitecture

3. Ingestion: batch, CDC, dlt, unstructured→embedding

4. Orchestration: Airflow 3 & asset-based(Dagster)

5. Declarative& asset pipelines

6. Kafka& Streaming Ingestion

7. Batch/Streaming& dbt Transform

8. Validation,Quality Gates & Data Contracts

9. AI-Specific(dedup, feature parity, flywheel)

10. Thựchành: Agent trace,RAG ingest, featurestore

11. ComplexRAG & Knowledge Graph (VLM,ColPali, GraphRAG)

12. Reliability,Cost & Demo Giảngviên (VinUni) AICB· Ngày 17 Tuần4 1 / 58

---

<!-- chiron-source-span: {"source_span_id":"5a37b4c4-7d6f-5cfe-934b-534e628315ed","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"MụcTiêu","extraction_method":"pdf-text-layer"},"checksum":"1c53152ad481d2d1db32a1d89a201bb6e13bc98a393399718a8c9b681d36f78b"} -->

## Slide 4 - MụcTiêu

### Saubuổi học này,bạnsẽ

1. Thiếtkế ETL/ELTpipeline robustcho AI training & inference data

2. Orchestratedata flow bằng Airflow DAG (vàhiểu asset-based alternatives)

3. Implementstreaming ingestion với Kafka cho real-timefeatures

4. Ápdụng validation gates & data contractsngăn data bẩn vào model

5. Biếnagent trace & dữ liệu phicấu trúc thành dataset (dedup, decontaminate)nuôi eval/fine-tune& RAG/KG Pipeline mindset + ETL/ELT/Medallion (40’)→ Ingestion & Orchestration (50’)→ Streaming & Transform (50’)→Quality, Contracts & AI pipelines (40’)→Thực hành Agent/RAG& Complex RAG/KG (40’)→Demo& Lab Giảngviên (VinUni) AICB· Ngày 17 Tuần4 2 / 58

---

<!-- chiron-source-span: {"source_span_id":"9b9bf026-bf56-5ab8-b1f9-ef22dd36daa6","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"a69f6a2daa7104c720304f728079d7203252e05a11f0103e30298e60fcf3e297"} -->

## Slide 5 - DeliverableCuối Ngày

Pipelinechạyđược: ingest →validate →transform →load,vớidedup+qualitygate +dbt tests pass

- OrchestratedDAG 4+ tasks: extract→validate →transform →load

- Medallionlayers (Bronze/Silver/Gold) trên DuckDB, dedup ởSilver

- Pandera/GXvalidation suite + quarantine cho badrecords

- dbt-duckdbproject với staging & gold models,dbt test pass

- (Bonus)streaming event sim + unstructured→embeddingingestion
Giảngviên (VinUni) AICB· Ngày 17 Tuần4 3 / 58

---

<!-- chiron-source-span: {"source_span_id":"4c8fe591-6058-5807-8e62-f5ca07820398","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Data-CentricAI: Pipeline Là Lợi ThếCạnh Tranh","extraction_method":"pdf-text-layer"},"checksum":"a3cefb16d1385376f82c01a7ba56a9a3f0c05d7a14a93c36e83efefc1cf70629"} -->

## Slide 6 - Data-CentricAI: Pipeline Là Lợi ThếCạnh Tranh

```text
■ Aicũng import transformers —
```
kiếntrúc model gần như miễn phí

- Khácbiệt thật nằm ởdatabạn
đưavào

- “Garbagein →garbageout” áp
dụnggấp đôi cho AI Lưu ý: Pipeline là một dependency của model— chính xác như một thư viện. Pipeline hỏng âm thầm = model hỏng âm thầm, nhưngaccuracy dash- board vẫn xanh. Nguồndữ liệu (apps, DB, logs,docs) DATAPIPELINE ingest· validate · transform Feature/ Trainingdata Model(train & serve) Ngườidùng / Quyết định Một lỗi ở đây nhân lên toàn bộ downstream Giảngviên (VinUni) AICB· Ngày 17 Tuần4 4 / 58

---

<!-- chiron-source-span: {"source_span_id":"2cf6520d-b33a-58e1-ab2f-f82914249036","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"KhiPipeline Hỏng: HoáĐơn Thực Tế","extraction_method":"pdf-text-layer"},"checksum":"780cfa2c58fed8c17573c342b4a93553e15ae36d9df80e8bb0a489f7f09e2e4f"} -->

## Slide 7 - KhiPipeline Hỏng: HoáĐơn Thực Tế

Unity(2022) $110M ≈8%doanh thu năm Ad-targetingmodel ăn baddata từ 1 khách hànglớn

- accuracysụp đổ
ZillowOffers (2021) $304M write-downQ3 + đóng cửa BU Modelđịnh giá nhà mua hớ ≈7.000căn →cắt25% nhân sự (distributionshift / drift) Equifax(2022) 2.5Mscores creditscores sai 3 tuần Codelỗi chưa test trong scoringpipeline; <300klệch ≥25điểm. NY AGphạt $725k Mẫusố chung: khôngai bị hack. Chỉ làdata xấu đi qua một pipeline thiếu gate. Nguồn: Coralogix/Monte Carlo (Unity), SEC8-K (Zillow), NY AG (Equifax). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 5 / 58

---

<!-- chiron-source-span: {"source_span_id":"fea2b64d-6c20-5386-8579-634b7c4f7476","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"SựCố Pipeline Là Chuyện ThườngNgày","extraction_method":"pdf-text-layer"},"checksum":"4fc742eb2aa42ad8a2dcb21a825670361095c4114b99738890a973b5bbc9dd88"} -->

## Slide 8 - SựCố Pipeline Là Chuyện ThườngNgày

1/10 bảng dữ liệu gặp≥1 sự cố mỗi năm (Monte Carlo 2026, +11M bảng; xấu đi từ 1/15)

- Pipelineexecution faults —26.2%

- Real-worldvariation — 20%

- Intentionalchanges (backfills) —
14.2%

- Schemadrift — 7.8%
$3M/tháng chi phí trung bình do pipeline fail- ures (Fivetran 2026, n=500); tới $1.4M/sự cố; ~13h khắc phục Lưuý: 53%nănglựckỹsưdữliệudành cho bảo trì pipeline (Fivetran 2026). Pipelinetốtkhôngphảilàtínhnăngphụ —nó là phần lớn công việc. Hômnay ta học cách xâypipeline đểkhôngtrởthành các con số trên. Observability sâu hơn→Ngày27. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 6 / 58

---

<!-- chiron-source-span: {"source_span_id":"e6ac0ab6-bc2a-54f2-ac11-46d8ac48229b","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"ETLvs ELT:ELTLàDefault, ETL Cho Ngoại Lệ","extraction_method":"pdf-text-layer"},"checksum":"5aa3e59446834ae1e40926e088eaec60560ff4c6a0b0cb1255355d91a5db689f"} -->

## Slide 9 - ETLvs ELT:ELTLàDefault, ETL Cho Ngoại Lệ

ETL(truyền thống) Extract Transform Load ELT(cloud-native, AI) — mặcđịnh Extract LoadRaw Transform EtLT(thực tế: hybrid) Extract lightt Load Transform ELT thắng mặc định:compute lakehouse (Snowflake/- Databricks/BigQuery) rẻ→ transform tại chỗ. ETL vẫn sống cho:mask PII trước khi load (regulated→ Ngày 24), target on-prem yếu compute, transform bằng Python lib. “ETLis dead” là cường điệu— thực tế phần lớn pipelinelàEtLT:extract-time transform nhẹ, rồi heavytransform trong warehouse. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 7 / 58

---

<!-- chiron-source-span: {"source_span_id":"b1e8b6d5-fe98-57be-ad3e-63369cfb1010","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Medallion: Bronze / Silver/ Gold","extraction_method":"pdf-text-layer"},"checksum":"8a6ae2c7862cde54097ff3af156da92141977ffc26995e25af9fe592a1f38c4c"} -->

## Slide 10 - Medallion: Bronze / Silver/ Gold

Bronze Raw,append-only Khôngthay đổi GIỮMÃI MÃI Silver Cleaned& conformed Deduplicated Schemaenforced Gold Business-ready Aggregated MLfeatures validate+ clean aggregate+ feature Medalliontrả lời “tổ chức chấtlượngtăng dần thếnào” — KHÔNG phải ETL/ELT. ETL/ELTtrả lời “transform chạyở đâu”. Thực tế medallion= ELTbên trong. Rule#1: Luôngiữ Bronze (raw) — khôngbao giờ xoá data gốc. Retraining & reproducibility cần fullhistory. (Tableformat Delta/Icebergcho Bronze →Ngày18.) Giảngviên (VinUni) AICB· Ngày 17 Tuần4 8 / 58

---

<!-- chiron-source-span: {"source_span_id":"53cc04a1-8d96-522b-be2d-678c6626f7d5","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Medallion2025: Anti-Patterns &Cuộc TranhLuận “Platinum”","extraction_method":"pdf-text-layer"},"checksum":"4a93b64519eafd81fb3cb0d81b8612bdc595cf7e991b4a0601b0e00bc8826e99"} -->

## Slide 11 - Medallion2025: Anti-Patterns &Cuộc TranhLuận “Platinum”

Lưu ý: 4 anti-patterns (Data Engineering Weekly, 9/2025)

- Bronze-misuse: report thẳng từraw

- Silver-overload: nhồi business KPIvào lớp conform

- semanticsprawl

- Gold-latencymismatch: ép real-time quabatch
aggregates

- Cross-layerentanglement: đổi1schema →cascade
vỡnhiều lớp Lớpthứ4hànhđộng: MLfeaturesreal-time,personal- ization, APIs. Lý do: multi-hop Bronze→Silver→Gold thêmđộ trễ, lỡ cửa sổquyết định real-time. Databricks định nghĩa Gold là “aggregates & features sẵn sàng cho analyticsvà machine learning”→ Gold chính là nguồn cho Feature Store (xem phần AI- SpecificPipelines). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 9 / 58

---

<!-- chiron-source-span: {"source_span_id":"8115f843-f13e-5bbf-99ed-93fa4abc0913","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Trainingvs Inference Pipeline &Reverse ETL","extraction_method":"pdf-text-layer"},"checksum":"a0805151e26be564a2c7d866a4f41aa4be129265ef8a2555feed9fbd906062d9"} -->

## Slide 12 - Trainingvs Inference Pipeline &Reverse ETL

TrainingPipeline batch· scheduled · full dataset InferencePipeline real-time· per-request FeatureStore đảmbảo train=serve Chạy thỉnh thoảng (occasionally) Chạy luôn luôn (always-on) FTIarchitecture: Feature /Training/ Inference — 3pipeline độc lập, nối bằng featurestore. Đẩy data đã transform từ warehousengược về SaaS vận hành (CRM, ad tools): scores, predic- tions,segments. “Data activation”.

- Tools: Hightouch (warehouse-native, 300+
destinations)& Census (Audience Hub); cảhai ~$350/mo

- Thịtrường ~$485M (2024), tăng ~35%/năm

- Độnglực: phần lớndata warehouse nằm im,
khôngđược “kích hoạt” (số liệuvendor) Giảngviên (VinUni) AICB· Ngày 17 Tuần4 10 / 58

---

<!-- chiron-source-span: {"source_span_id":"425c3062-836d-560e-bb48-4a6540708fff","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"ExtractPatterns: Full, Incremental,CDC","extraction_method":"pdf-text-layer"},"checksum":"606aae72e7c301a454d18a61d17c5d6ad540659fdb50530da0a959b49f4ac316"} -->

## Slide 13 - ExtractPatterns: Full, Incremental,CDC

- append: chèn thêm (eventlogs)

- replace: ghi đè toànbộ (snapshot nhỏ)

- merge: upsert theo primarykey→dedup+
cậpnhật Cursor-based: theodõimax( updated_at);chỉkéobản ghi mới. Lưu cursor state giữa các lần chạy. Rẻ hơn full-extractnhiều lần. Đọc transaction log của DB (không query bảng)→ stream mọi insert/update/delete. Bắt được cả delete, độtrễ thấp, không tải DBnguồn. Debezium3.4(12/2025) — CôngcụCDClog-based chuẩn mực: biến PostgreSQL/MySQL/Mongo thành luồngsự kiện Kafka. Testedvới PostgreSQL 18. Khinào CDC?Cầnreal-time sync, cần bắt delete,hoặc khôngmuốn batch-query làm nặng DBsản xuất. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 11/ 58

---

<!-- chiron-source-span: {"source_span_id":"a649ee29-7a51-53db-b546-327a6496f539","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"ELLandscape: dlt, Airbyte,Fivetran, Singer","extraction_method":"pdf-text-layer"},"checksum":"4de50126d497af9eda317788f9cb31d37c8981327d41fa5773b08ac63290e2ac"} -->

## Slide 14 - ELLandscape: dlt, Airbyte,Fivetran, Singer

```text
import dlt
```
# Python-native EL: schema evolution tu dong @dlt.resource(write_disposition= "merge", primary_key= "id")

```text
def orders(updated_after=dlt.sources
.incremental("updated_at")):
yield from api.get_orders(
since=updated_after.last_value)
pipe = dlt.pipeline(destination= "duckdb")
pipe.run(orders) # cursor state luu tu dong
dlt1.0 (9/2024), nay 1.28; schemaevolution: evolve / freeze/ discard.
```
Tool Chọnkhi dlt Python-native,code-first Airbyte OSSself-host, kiểm soát Fivetran Fully-managed,CDC tự động Singer/Meltano Tap/targetprotocol Lưu ý:Hợp nhất thị trường:Fivetran + dbt Labs hoàn tất sáp nhập 1/6/2026 (≈$600M ARR). EL và T đang hội tụ. Coi chừng mô hình tính phí per- connectorMAR (Monthly Active Rows). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 12 / 58

---

<!-- chiron-source-span: {"source_span_id":"9f2f9202-9487-59cd-baf6-975212f149f6","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"IngestionCho LLM: Unstructured→Chunk →Embedding","extraction_method":"pdf-text-layer"},"checksum":"53c8246a31eafb78773a8349addae492165a1569888d3eed5370e56d146f9c76"} -->

## Slide 15 - IngestionCho LLM: Unstructured→Chunk →Embedding

PDF/ DOCX / HTML/ ảnh Parse Docling· unstructured ·LlamaParse Chunk recursive512 tok +overlap 10-20% Embed modelembeddings Vectorstore ANNindex Recursive~512-tokenvẫnlàdefaultmạnhnhất(~69% acc,benchmark2025-26)—semanticchunking không tựđộngtốthơn. Latechunking (embedcảdocrồimới cắt)làm fixed ≈semantic. Hierarchical/parent-child, Contextual Retrieval, late chunking, hybrid retrieval — xây index chocomplex RAG →§13. Incrementalindexing: chỉ re-embeddoc đổi (hash/version)→10-15%thay vì 100%. Vector/featurestoresâu hơn →Ngày19. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 13 / 58

---

<!-- chiron-source-span: {"source_span_id":"c788c8f9-73ca-57bf-aef9-cf80d3a0e1aa","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"AirflowDAG: Anatomy & Quarantine Branch","extraction_method":"pdf-text-layer"},"checksum":"ca9c5377838d33b54cd139aedc148d8192fd8bfed877ec945db420234b82b915"} -->

## Slide 16 - AirflowDAG: Anatomy & Quarantine Branch

ai_training_pipelineDAG S3KeySensor chờdata extract @task validate GX/Pandera transform dbtrun load tolakehouse trigger retraining quarantine badrecords fail schedule=”02 * * *” catchup=False Gotchakinh điển: catchup=True (mặcđịnh!) →deployDAG mới = chạyTẤTCẢ scheduleđã lỡ ngay lập tức. 30 backfillrun →GPUquá tải. Luônset catchup=False chotraining pipeline. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 14 / 58

---

<!-- chiron-source-span: {"source_span_id":"8249a752-ec32-5673-b2dd-f5947ecce387","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"AirflowTaskFlowAPI & DynamicMapping","extraction_method":"pdf-text-layer"},"checksum":"f1a6278751b647a8958cd062803c989218576c71906f20a4aff0361eda591aa1"} -->

## Slide 17 - AirflowTaskFlowAPI & DynamicMapping

```text
from airflow.decorators import dag, task
@dag(schedule= "0 2 * * *", catchup=False,
max_active_runs=1) # 1 run / luc
def ai_training_pipeline():
```
@task

```text
def extract():
return list_s3_files("raw/")
```
@task # fan-out runtime

```text
def process(path):
return clean_one(path)
```
@task

```text
def load(rows): write_gold(rows)
files = extract()
load(process.expand(path=files)) #.expand!
ai_training_pipeline()
```

- @taskthayPythonOperator

- .expand(): tạotaskinstancelúcruntime
(xửlý N file)

- Deferrableoperators: nhả worker slot
khichờ;triggererdùngasynciogiữhàng trămtask Lưu ý: Deferral + fan-out cực lớn (≈17k task) có thể quá tảimetadata DB. max_active_runs=1 chotraining. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 15 / 58

---

<!-- chiron-source-span: {"source_span_id":"1672da0a-a465-5e63-b1b0-82f0fb453021","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Airflow3.0 (4/2025): BướcNhảy Lớn Nhất Lịch Sử DựÁn","extraction_method":"pdf-text-layer"},"checksum":"86d50e1e027a59661ee617acac72d285bc695985a2078a03d2569560858b9c4a"} -->

## Slide 18 - Airflow3.0 (4/2025): BướcNhảy Lớn Nhất Lịch Sử DựÁn

- DAGVersioning: run hoàn tấttheo đúng
versionlúc bắt đầu, kể cảdeploy giữa chừng

- DataAssets (AIP-74)+ @assetdecorator:
Datasetsthành công dân hạng nhất

- Event-drivenscheduling: DAG kích hoạtkhi
assetbên ngoài cập nhật

- Client-server(AIP-72): TaskExecution API +
TaskSDK, task isolation

- EdgeExecutor (AIP-69): chạy task trên
remote/edgecompute

- 3.1(9/2025): Human-in-the-Loop tasks (cổng
phêduyệt cho AI/ML), Deadline Alerts(SLA)

- Stablehiện tại: 3.2.x(data-awareworkflows at
scale) Vì sao quan trọng— Airflow chuyển từ thuần “task- based” sang hỗ trợ “asset-aware” — hội tụ một phần vớimô hình của Dagster (slidekế). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 16 / 58

---

<!-- chiron-source-span: {"source_span_id":"2939dec5-36a8-537d-85ce-eb104c7cacf2","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"OrchestratorLandscape 2026: ChọnCông Cụ Nào?","extraction_method":"pdf-text-layer"},"checksum":"c49f529bfee42c335710ec98b86382959ad6eca458c2f8fc06a9916ebe4f9958"} -->

## Slide 19 - OrchestratorLandscape 2026: ChọnCông Cụ Nào?

Côngcụ Môhình Chọnkhi ApacheAirflow 3.x Task-based(+ asset-aware) Chuẩn ngành, ecosystemlớn, batch ETL Dagster1.12 Asset-based(SDA) Coidata asset là trung tâm,lineage, data-quality-aware Prefect3.0 Task+ transactions Cầnidempotency/rollback hooks, Pythonic, nhẹ Temporal Durableexecution Pipeline/agentchạy lâu, cần resume-on-crash Kestra1.x DeclarativeYAML Teamđa ngôn ngữ, không muốn DAGthuần Python Task-based (Airflow)— Bạn mô tảthứ tự các bước (how). “Chạy A rồiB rồi C.” Asset-based (Dagster SDA) — Bạn khai báo các asset & phụ thuộc(what). Dagstertựsuyrađồthịthực thi. Declarative Automation re-materialize theo fresh- ness/status. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 17 / 58

---

<!-- chiron-source-span: {"source_span_id":"ec9aaf64-4fae-568d-ad6c-7379cf85d27e","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"TừImperative DAG Sang Declarative Dataflow","extraction_method":"pdf-text-layer"},"checksum":"a00872cc3f13ad5c38917b94fcecab189c9d2ddbc259dbddfa240ce9483bda2f"} -->

## Slide 20 - TừImperative DAG Sang Declarative Dataflow

Imperative(DAG) “chạy task này rồi task kia” Declarative(asset) “đây là các bảng & phụ thuộc — giữ chúng luôn cập nhật” DatabricksmởmãDLTengine →donatechoApacheSpark (DAIS 6/2025).GA trong Spark 4.1.0 (16/12/2025). Khai báodatasetbằngdecorator,Sparktựdựngđồthị&thứtự. DLT → Lakeflow Declarative Pipelines (thương mại, GA 6/2025, code cũ chạy nguyên) vàSpark Declarative Pipelines(OSS)— chung dòng máu. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 18 / 58

---

<!-- chiron-source-span: {"source_span_id":"bb56e2af-a526-5e57-8c29-1332ad778ee8","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Declarative: Materialized ViewvsStreaming Table","extraction_method":"pdf-text-layer"},"checksum":"8d2b6a5582978e70a3db3fa32234d81844745397ecd7609e715e83ae8998f8a9"} -->

## Slide 21 - Declarative: Materialized ViewvsStreaming Table

```text
from pyspark import pipelines as dp
```
@dp.materialized_view # batch, tinh truoc

```text
def orders_clean():
return (spark.read.table("bronze.orders")
.dropDuplicates(["order_id"]))
```
@dp.table # streaming, exactly-once

```text
def orders_stream():
return (spark.readStream
.table("bronze.orders_raw"))
```
# spark-pipelines init / dry-run / run SDPtựphântíchphụthuộc&orchestrate. dry-runbắtlỗicyclic/analysistrướckhichạy.

- MaterializedView: precompute batch,
cắtcost/latency truy vấn

- StreamingTable: xử lý mỗirecord
exactly-oncetrênnguồn append-only Lưu ý:Caveat: declarative dataflow hấp thụorchestration nội bộ pipeline, nhưng KHÔNG phải scheduler. Vẫn cần Air- flow/Dagstercho when/trigger/history. “Airflow chưa chết.” Giảngviên (VinUni) AICB· Ngày 17 Tuần4 19 / 58

---

<!-- chiron-source-span: {"source_span_id":"4c7bc3f7-5b7d-538b-8762-24982524f7a5","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"DagsterSoftware-Defined Asset: DeclarativeTrongCode","extraction_method":"pdf-text-layer"},"checksum":"6e0dd7a0634a5d73ba0b2a487d06a99432d36baf16d9586d6cab64294ea9086c"} -->

## Slide 22 - DagsterSoftware-Defined Asset: DeclarativeTrongCode

```text
import dagster as dg
@dg.asset(group_name= "silver") # = 1 bang Silver
def orders_clean(orders_raw): # dep = ten tham so
return (orders_raw.dropna(subset=[ "order_id"])
.drop_duplicates("order_id"))
@dg.asset(automation_condition= # tu chay khi
dg.AutomationCondition.eager()) # upstream doi
def orders_gold(orders_clean):
return orders_clean.groupby("user_id").size()
@dg.asset_check(asset=orders_clean) # quality gate
def no_dupes(orders_clean):
dup = orders_clean[ "order_id"].duplicated().any()
return dg.AssetCheckResult(passed= not bool(dup))
Airflow: bạn viết@task & nối thứ tự (how).
```
Dagster: bạnkhaibáo asset+dependency là tên tham số — Dagster tự suy ra đồ thị (what).

- AutomationCondition =Declarative
Automation(stable 1.12) thay cron

- asset_check =quality gate gắn vào
asset—chínhlàquarantine/contract logiccủa §9/§10 Giảngviên (VinUni) AICB· Ngày 17 Tuần4 20 / 58

---

<!-- chiron-source-span: {"source_span_id":"52e7aebb-1799-5980-9956-689ef6a77fb7","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"KafkaArchitecture cho AI (KRaft, KhôngCòn ZooKeeper)","extraction_method":"pdf-text-layer"},"checksum":"c89d2a85d941d2543309d99bff0a267f071d26b7acaf720bfc8aee1e6be74d8f"} -->

## Slide 23 - KafkaArchitecture cho AI (KRaft, KhôngCòn ZooKeeper)

AppEvents DBCDC Debezium APILogs KafkaCluster KRaftmode ai-events feedback predictions SchemaRegistry Avro/Protobuf Flink stateful FeatureStore Feast Model retrain S3Sink VectorDB Analytics Kafka4.0 (18/3/2025): bảnmajor đầu tiên chạyhoàn toàn không ZooKeeper —KRaft là mode duy nhất. Cluster cũ phải migratequa 3.9 (bridge) trước khilên 4.0. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 21 / 58

---

<!-- chiron-source-span: {"source_span_id":"d59a1f73-6bb8-5acf-a99c-3ff23fb15496","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Partitions,Schema Registry,Exactly-Once &Diskless","extraction_method":"pdf-text-layer"},"checksum":"9ff22ea1c2f1e4f1c7bd753268752b855a63de579567a0b15d85246ed47d75ce"} -->

## Slide 24 - Partitions,Schema Registry,Exactly-Once &Diskless

- Partitiontheo user_id →orderingmỗi user

- Partitions= consumer parallelism

- Replicationfactor ≥3cho durability
Avro/Protobuf/JSON; compatibilityBACKWARD(mặc định), FORWARD, FULL. Bảo vệ model khỏi schema driftâm thầm. Exactly-once (EOS)— Idempotent producer (PID + sequence number) + transactions. KIP-890 chống “hangingtransactions”.

- WarpStream(Confluentmua 9/2024): ghi
thẳngS3, bỏ phí inter-AZ

- KIP-1150DisklessTopics: được chấp nhận vào
ApacheKafka (3/2026)

- Redpanda: C++ thread-per-core, không
JVM/ZooKeeper Sốliệu giảm 48-90% chi phí/ 10x latency làvendor-sourced—benchmark độc lậpkhiêm tốn hơn. Bối cảnh: IBM muaConfluent (~$11B,công bố12/2025). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 22 / 58

---

<!-- chiron-source-span: {"source_span_id":"27aaf5b8-4913-5229-a50b-79857b8218a5","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"ReferenceArchitecture: Kafka +Flink →OnlineFeature Store","extraction_method":"pdf-text-layer"},"checksum":"0cb58d9348a573aa2514dee50f8d8dd28e8a92f5ab765e828cfbe861e4044bc4"} -->

## Slide 25 - ReferenceArchitecture: Kafka +Flink →OnlineFeature Store

Kafka ingestbền vững +replay Flink statefulcompute low-latency Onlinestore Redis/Dynamo mslatency Offlinestore Parquet/Iceberg đểtrain Inference serve Training features Vìsao streaming thắng batch choAI features:(1)freshness từ phút/giờ xuống ms/giây;(2)giảmtraining-serving skew(featuretính khác nhau lúc trainvs serve) — tínhcùngfeatureliên tục, ghi vào cảonline & offlinestore. Batch vẫn rẻhơn cho feature ít đổi. (Feature store sâu hơn→Ngày19.) Giảngviên (VinUni) AICB· Ngày 17 Tuần4 23 / 58

---

<!-- chiron-source-span: {"source_span_id":"494ef4e4-e478-5466-bc49-67f4097ae654","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"FlinkSQL: Streaming Feature Job (Kafka→OnlineStore)","extraction_method":"pdf-text-layer"},"checksum":"ac83a0e18ae1cecce31cc99671ec85ad5f0067389ebb7069daf3f9921c7d05c6"} -->

## Slide 26 - FlinkSQL: Streaming Feature Job (Kafka→OnlineStore)

-- Source: Kafka topic, event-time + watermark CREATE TABLE clicks ( user_id STRING, amount DOUBLE, ts TIMESTAMP(3), WATERMARK FOR ts AS ts - INTERVAL '5' SECOND ) WITH ( 'connector'= 'kafka', 'topic'= 'ai-events', 'format'= 'avro-confluent'); -- Schema Registry -- Sink: online feature store (upsert by key) CREATE TABLE feat_5m ( user_id STRING, spend_5m DOUBLE, PRIMARY KEY (user_id) NOT ENFORCED ) WITH ( 'connector'= 'upsert-kafka',...); INSERT INTO feat_5m -- tumbling 5-min window

```text
SELECT user_id, SUM(amount)
FROM TABLE(TUMBLE(TABLE clicks, DESCRIPTOR(ts),
INTERVAL '5' MINUTES))
GROUP BY user_id, window_start, window_end;
```
Đây là cái box “Flink” trong reference architecture: feature spend_5m tính liên tục,upsertvàoonlinestore →inference đọcms-latency. Watermark — ts - INTERVAL '5' SECOND: chấp nhận trễ tối đa 5s. Event trễ hơn → late-handling.mode=filter đẩy vàoSystem Table $lateđểreprocess. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 24 / 58

---

<!-- chiron-source-span: {"source_span_id":"f566093b-d7dc-5f65-9652-1bd493db6ffc","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Batch →Micro-Batch →Streaming: Đánh Đổi","extraction_method":"pdf-text-layer"},"checksum":"3e51954fee84a4497feb6d4cf7e2320bed511ef16837dacddfced9194ba12390"} -->

## Slide 27 - Batch →Micro-Batch →Streaming: Đánh Đổi

Batch Spark/ dbt Latency: giờ/ngày Trainingdata prep Micro-Batch SparkStructured Latency: 1-5 phút Featureupdates Streaming Kafka+ Flink Latency: ms Frauddetection Latencygiảm →Complexitytăng →Costtăng Lambda: batch+ speed layer song song, servinglayer merge cả hai (mạnhnhưng phức tạp) Kappa: streamingcho mọi thứ, replaytopic = “batch” (đơn giảnhơn, trending) Hộitụ 2025: streamingtables + materialized views (declarative)làm mờ ranh giới — mộtđịnh nghĩa chạy được cả batch lẫnstreaming. Kafka +Flink xử lý cả historical replaylẫn real-time (Kappa). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 25 / 58

---

<!-- chiron-source-span: {"source_span_id":"9fa0e677-1ebd-5351-b3f7-9b1a0b7be2f0","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"dbtModel Layers & Materializations","extraction_method":"pdf-text-layer"},"checksum":"66f8699806e92db0b9c86e2d880069e9e42bc024ac17172b50936a033ed6f194"} -->

## Slide 28 - dbtModel Layers & Materializations

1. staging(stg_): 1:1 source, rename/cast, khôngjoin

2. intermediate(int_): business logic, joins

3. marts(fct_/dim_): consumption-ready,đúng grain view (dev) → table (prod) → incremental (>100M rows) → materialized_view. Chiến lược micro- batch (GA dbt 1.9) cho time-series lớn: không cần is_incremental(). Sources rawtables stg_(view) int_(table) marts(incr.) FeatureStore dbttest not_null unique ref() Goldmarts →featurestore (Feast) →modeltraining. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 26 / 58

---

<!-- chiron-source-span: {"source_span_id":"11b2dfc9-bfeb-51d4-b2d4-8f7df9d0dfb5","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"dbt2026: Fusion, UnitTests& SQLMesh","extraction_method":"pdf-text-layer"},"checksum":"1966a94250cf4a139f0f18ca43ef1887f53a40aab8b9068c8f7ae312cc440d82"} -->

## Slide 29 - dbt2026: Fusion, UnitTests& SQLMesh

# unit test (dbt 1.8+): test LOGIC # voi fixtures tinh, khong can warehouse

### unit_tests
- name: test_dedup_keeps_latest
model: stg_orders

### given
- input: ref( 'raw_orders')

### rows
- {id: 1, ts: "2026-01-01"}
- {id: 1, ts: "2026-01-02"}

### expect

### rows
- {id: 1, ts: "2026-01-02"}

- Engineviết lại bằngRust(beta5/2025):
parsenhanh tới 30x, compile 2x

- dbtCore v2.0 (6/2026): nền Fusion, runtime
nay Apache 2.0

- Mesh: ref('project','model')
cross-project;Semantic Layer (MetricFlow) SQLMesh (đối thủ)— Virtual Data Environments (env qua view, zero-copy); plan/apply kiểu Ter- raform; column-level lineage. Fivetran donate cho LinuxFoundation (3/2026). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 27 / 58

---

<!-- chiron-source-span: {"source_span_id":"b7f32b8d-30cb-5d4c-9e75-24b6d8e87fe3","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"ValidationGates: FailEarly,Quarantine Bad Records","extraction_method":"pdf-text-layer"},"checksum":"333d4764de63fab383a4226264c2c3bdb6e61af37785cfe493b42233b7c6fb5d"} -->

## Slide 30 - ValidationGates: FailEarly,Quarantine Bad Records

Extract Validate source? Transform Validate logic? Loadto Training pass pass Quarantine/ DLQ fail fail Quarantine/ DLQ (dead-letter queue) triage— 3 nhóm: Retriable(transient →replaysau) ·Fixable(schema/thiếu data →kỹsư sửa rồi replay) ·Poison(khôngbao giờ qua→archive+ alert). DLQspike = tín hiệu schemadrift / qualityregression. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 28 / 58

---

<!-- chiron-source-span: {"source_span_id":"c8bda9c2-efbe-5eb7-897a-c837cdeb834c","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"4Loại Gate: Record/ Dataframe / Suite / Contract","extraction_method":"pdf-text-layer"},"checksum":"62d076b5a5573251619c3abb894499a4f0d5a907c8caae76b83ab15f5f5f6dbc"} -->

## Slide 31 - 4Loại Gate: Record/ Dataframe / Suite / Contract

Tool Granularity Interface Chặnpipeline bằng Pydanticv2 Mỗirecord / JSON Typedcode (Rustcore, 5-50x) Raiselúc parse từng bản ghi Pandera0.3x Mỗi dataframe Typedschema (pandas/Polars/Spark) Schema-on-read, fail batch GXCore 1.0 Mỗi dataset Expectationsuite + Checkpoint Action(Slack alert / halt) SodaCore v4 Mỗi dataset YAMLSodaCL / data contract Contractverify trong CI Schema-on-read enforcement — Validate cấu trúc/type lúc consume (Polars LazyFrame / Spark read), không chỉ lúc write. Pandera check schema- levelmà không cầncollect(). GX Core 1.0 (8/2024): API viết lại, 47 expectations typed. Pandera multi-engine + Narwhals backend. Soda v4: data contracts là cách mặc định.Observ- ability runtime (MonteCarlo, anomaly) →Ngày27. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 29 / 58

---

<!-- chiron-source-span: {"source_span_id":"a9f10409-3d88-5d27-8624-4432442d9209","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"ValidationIn Code: Pandera + Quarantine","extraction_method":"pdf-text-layer"},"checksum":"19fd52922ae3e5fd1cf600a2621d6bf6072e93c832c1b8a0d6f9bfe1b092bc28"} -->

## Slide 32 - ValidationIn Code: Pandera + Quarantine

```text
import pandera.pandas as pa
schema = pa.DataFrameSchema({
"user_id": pa.Column( str, nullable=False),
"label": pa.Column( str, pa.Check.isin(
["pos", "neg"])),
"confidence": pa.Column( float,
pa.Check.in_range(0.0, 1.0)),
})
```
try: # gate: fail early clean = schema.validate(df, lazy=True)

### except pa.errors.SchemaErrors as e
bad = e.failure_cases # -> quarantine write_quarantine(bad) # DLQ, alert on spike

- Validatengay sau extract→bắtlỗi
nguồn

- Validatesau transform →bắtbug
logic

- lazy=True: gommọilỗi,không dừng
ởlỗi đầu Lưu ý: Một bad record KHÔNG được làm sập cả pipeline. Tách ra quarantine, để good records chảy tiếp. Idempotentsink →replayan toàn. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 30 / 58

---

<!-- chiron-source-span: {"source_span_id":"40277598-3da7-59b4-8979-34f807d1dc8a","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"LLM-as-JudgeData Quality: BắtLỗi Ngữ Nghĩa Rule Không Thấy","extraction_method":"pdf-text-layer"},"checksum":"ddd05a2fd2af5ef648d4736000c2f3b0fabe722c03c2d358f7b7f1d44ae17c19"} -->

## Slide 33 - LLM-as-JudgeData Quality: BắtLỗi Ngữ Nghĩa Rule Không Thấy

Lưuý: Gatedựa-trên-rule(GX/Pandera/Soda) mùvới lỗingữnghĩa—đúngkiểusựcốhook: accuracy94% mà conversion giảm 12%, monitor thống kê không thấy.

- Near-dupngữ nghĩa: “NYC”vs “New YorkCity”

- Hợp-lệ-schemanhưng vô lý: CEO sinh năm
2025

- Bấtthường ngữ cảnh trong free-text/ JSON /
log

1. Tier1 SLM/rules( ≈80%checks: schema, null, type,exact-dedup, format) — rẻ 10-30x

2. Escalate chỉcácdòng mơ hồ

3. Tier2 LLMjudge: semantic dedup,cross-field reasoning,free-text anomaly Nguyên tắc — Đừng LLM-check mọi thứ (đắt + chậm). Dùng rule làm tầng lọc, LLM cho phần rule khôngvới tới. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 31 / 58

---

<!-- chiron-source-span: {"source_span_id":"c362b598-55bb-5058-8b26-46e727845d44","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"SecurityGate: Lethal TrifectaTrongAgent Data Pipeline","extraction_method":"pdf-text-layer"},"checksum":"30b3f04195484da2348ad4212f4331a0f0ae399a4b1a063ecb17f20f2678de84"} -->

## Slide 34 - SecurityGate: Lethal TrifectaTrongAgent Data Pipeline

### Lưuý: Vớiagent,datapipeline chínhlàattacksurface
mọithứagentđọcsaunày(chunkvectorDB,tooloutput, webscrape)làvectorinjection. Qualitygatephảimởrộng thành security gate.

- PoisonedRAG:chèn vài passage độc vàovector
DB →hỏngcâu trả lời RAG

- Memorypoisoning: text độc agentscrape→ghi
vàomemory bền vững (“poison once,exploit forever”)

- Tool-outputpoisoning: response của toollà nội
dungkhông tin cậy quay lạicontext

- Provenance: gắn nguồn tin-cậycho mỗi
chunk;quarantine nguồn lạ

- Tách trustedvs untrustedngaykhi ingest

- Contract+ signature cho data vàoagent
memory KhácDay11(Guardrails): controlpointởđâylà data pipeline (provenancelúc ingest),không phải prompt. “Lethal trifecta” (Simon Willison): untrusted content+ private data + exfiltration. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 32 / 58

---

<!-- chiron-source-span: {"source_span_id":"154c63b1-365f-522a-908c-74ba9a33ae9e","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"DataContract: Giao KèoProducer ↔Consumer","extraction_method":"pdf-text-layer"},"checksum":"7775b4e44c9dab4e832daaef0afc500d45ca282a6e0022d387df7f60ee10cdd4"} -->

## Slide 35 - DataContract: Giao KèoProducer ↔Consumer

Producer teamdata nguồn DATACONTRACT machine-readable Consumer ML/ RAG / BI CIgate enforce Contractlà interface;CI thực thi nó.

1. Schema: types, constraints, nesting

2. Semantics: ý nghĩa từngfield

3. Quality: checks (not-null, ranges)

4. SLA:freshness, availability,retention Lưu ý: Vì sao quan trọng cho AI:ngăn schema drift âm thầm từ up- stream làm hỏng training data / vỡ RAG & feature pipeline. Chất lượng đượcép tại nguồn,không sửa downstream. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 33 / 58

---

<!-- chiron-source-span: {"source_span_id":"d964f76a-f951-5b99-b2fd-b5bfa8269f6a","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"ChuẩnHoá 2025-26: ODCS,datacontract CLI, Shift-Left","extraction_method":"pdf-text-layer"},"checksum":"abb0c9dd6aee0157875fcd31d333ffc325667fe252805c30ab57056fa877dd8a"} -->

## Slide 36 - ChuẩnHoá 2025-26: ODCS,datacontract CLI, Shift-Left

OpenDataContractStandard,Apache2.0,ra12/2025. Nguồn gốc: template của PayPal (2023). Head- line: Relationships (FK), strict JSON Schema, ex- ecutable SLAs. (Data Contract Specification cũ đã deprecated →dùngODCS.) datacontract CLI v1.0 (6/2026) — Một datacontract.yaml →exportradbtmodels/SodaCL / DQX checks, test trên ~12 backend (Ibis engine). “Singlesource of truth”. Bắtbreakingchange trước khi deploy,khôngphảisau khimodel hỏng.

- Gable.ai: quétsource code ứngdụng trong CI, chặn
schemachange phá vỡ contract (SeriesA $20M, 3/2025)

- Schemata: OSS schema scoring(producer-side
quality)

- SchemaRegistry (Kafka) = data contractcho
streaming Giảngviên (VinUni) AICB· Ngày 17 Tuần4 34 / 58

---

<!-- chiron-source-span: {"source_span_id":"f83523e8-b155-557a-9546-22f92e898a68","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"DataContract TrongThực Tế: ODCS v3 + CIGate","extraction_method":"pdf-text-layer"},"checksum":"6f2850aac631c33a90e485d024cae7e5d3eb52f1a6ef4def81df9fee32d2bd67"} -->

## Slide 37 - DataContract TrongThực Tế: ODCS v3 + CIGate

apiVersion: v3.0.0 # ODCS (Bitol / LF) kind: DataContract id: orders-gold

### schema
- name: orders_gold

### properties
- name: order_id
logicalType: string required: true unique: true # -> exec quality check - name: amount logicalType: number

### quality
- rule: range
mustBeBetween: [0, 100000]

### slaProperties
- property: freshness
value: 4 unit: h # executable SLA

- datacontract test
orders-gold.yaml

- datacontract changelog old new →
pháthiện breaking change, block PR

- exportradbt / SodaCL / Great
Expectations Lưu ý:Contract không còn là slogan: file nàychạy được. Schema + quality + SLA trong một interface máy kiểm tra được— copy vào repo projectcủa nhóm. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 35 / 58

---

<!-- chiron-source-span: {"source_span_id":"7f479901-44ef-5a12-b39f-72058219f088","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"AgentData Flywheel: TraceCủa Agent Là Nguồn DataCủa Bạn","extraction_method":"pdf-text-layer"},"checksum":"a747e8009e2b3eced24176e5e11aac27a51789d5813bacfa0cfab5253c0eaacf"} -->

## Slide 38 - AgentData Flywheel: TraceCủa Agent Là Nguồn DataCủa Bạn

Agentprod Day3 ReAct / Day9 multi-agent Traces OTelgen_ai.* +user feedback Pipelinehôm nay Bronze→Silver→Gold dedup+ PII redact Datasets Evalset (Day 14) SFT/DPO(Day 22) modeltốt hơn →redeploy(flywheel) TrongAICB bạn đã build agent(Day 3, Day 9). Agent đóphát ra trace. Pipeline hôm naybiến trace thành dataset:1 agentturn = 1 Bronze record(prompt,tool calls, response, feedback). Day 27 lànguồntrace;Day 14 & Day 22lànơi tiêu thụ dataset. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 36 / 58

---

<!-- chiron-source-span: {"source_span_id":"301accc3-9eec-512e-8e57-1910bf5c01c4","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Training-DataQuality: TrảLời Cho Cái Hook","extraction_method":"pdf-text-layer"},"checksum":"8a8ab9a7ab44d7f41fe0fb98a1a29b8c0ed9fa3fc77c4d8cca1661fe98ea6482"} -->

## Slide 39 - Training-DataQuality: TrảLời Cho Cái Hook

Lưuý: Vìsaoduplicatehạimodel? Model memorize bản ghi lặp→verbatim regurgitation, kém generalize. Memorizationtăng theo số lần lặp. Aquila2 & InternLM-2 bị phát hiện train trúng data GSM8K → điểm benchmark thổi phồng (arXiv 2404.18824). Dedup + decontamination là bước pipeline,không phải tuỳ chọn.

- MinHash+LSH:near-dedupchuẩnchocorpus
tỉtoken

- SemDeDup: dedup ngữ nghĩaqua embedding

- bỏ~50% data, gần như khôngmất
accuracy,train nhanh gấp đôi

- FED/SEDD(2025): GPU tăngtốc “tuần xuống
giờ” Sắcthái(FineWeb) — Deduplà empirical: FineWeb thấy per-snapshot MinHash tốt nhất, global dedup lại hại. “Nhiềuhơn”khôngluôntốthơn—đo,đừngđoán. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 37 / 58

---

<!-- chiron-source-span: {"source_span_id":"e3540024-2d32-5347-b73b-497f84631b43","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"DedupTrongCode: MinHash+LSH (lexical) & SemDeDup (semantic)","extraction_method":"pdf-text-layer"},"checksum":"a5cf892af8194f3529f771648db6ccd581b1cd554e14a4a938a15ebf0452f27c"} -->

## Slide 40 - DedupTrongCode: MinHash+LSH (lexical) & SemDeDup (semantic)

```text
from datasketch import MinHash, MinHashLSH
def sig(text, k=5, perm=128): # k-shingle
m = MinHash(num_perm=perm)
toks = text.lower().split()
for i in range(len(toks) - k + 1):
m.update(" ".join(toks[i:i+k]).encode())
return m
lsh, keep = MinHashLSH(threshold=0.8, num_perm=128), []
```
for doc_id, text in corpus: # 1 pass, streaming s = sig(text) if not lsh.query(s): # khong trung ai lsh.insert(doc_id, s); keep.append(doc_id)

- MinHash+LSH:near-dup từ vựng,
scaletỉ token

- SemDeDup: embed→cluster →bỏ
cặpcosine cao → ngữ nghĩa;bỏ ~50%data gần như không mất accuracy Chọn ngưỡng — threshold=0.8 (Jac- card): cao hơn→ ít gộp; thấp hơn→ gộp mạnhtay. Tunetheo corpus. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 38 / 58

---

<!-- chiron-source-span: {"source_span_id":"846e19ad-4b8d-5efd-8408-6371a813c2cf","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"PipelineCho Fine-Tuning: Dataset SFT/DPO Cho Ngày 22","extraction_method":"pdf-text-layer"},"checksum":"753f8907b45f42c2dcb8fa149ffff02be9562b7a5ec54e87bb2498690a253fc0"} -->

## Slide 41 - PipelineCho Fine-Tuning: Dataset SFT/DPO Cho Ngày 22

# SFT (instruction tuning) - 1 dong / vi du {"messages": [{ "role": "user", "content": "..."}, {"role": "assistant", "content": "...turn tot..."}]} # DPO / ORPO preference pair {"prompt": "...", "chosen": "...thumbs-up tu trace...", "rejected": "...thumbs-down..."} Nguồn“chosen/rejected” = feedback trong agenttrace (flywheel). Rawturns (traces / labels) GATE:schema SFT hợp lệ? Dedup(MinHash + SemDeDup) DECONTAMINATEvs eval set Format →jsonl Decontaminate: loại ví dụtrùng eval set (Day 14) khỏitrain set→ chốngđiểm thổi phồng. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 39 / 58

---

<!-- chiron-source-span: {"source_span_id":"9371b498-b372-582c-a7eb-431fe2b5d30d","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"FeaturePipelines, Versioning& Retraining","extraction_method":"pdf-text-layer"},"checksum":"ec83bcc07ab609712b503121fabcf3d5df7bc89bbc041974acef82703caa1388"} -->

## Slide 42 - FeaturePipelines, Versioning& Retraining

Training-serving skewlà nguyên nhân #1 model de- grade trong production. Feature store tồn tại chủ yếu đểdiệtnó: địnhnghĩafeaturemộtlần,servegiốnghệt chotrain (offline)& inference (online). Point-in-time correctness — As-of join theo event timestamp: mỗi training row chỉ thấy featurecó sẵn tại thời điểm đó → chống label leakage. Đặc thù AI, khôngcó trong ETL analytics cổđiển. Môhình FTI (Feature/Training/Inference): Feast (PyTorchEcosystem 2025, + vectorstorechoRAG),Chronon(Airbnb,OSS;Stripe/OpenAI/Netflix/Roku/Uber). Kiếntrúc feature/vector store sâu hơn→Ngày19. lakeFSmualạidựánOSS DVC(11/2025)—hợpnhất 2côngcụversion-controldữliệu. Git-cho-data: repro- ducetraining set chính xác. Modelcollapsecóthật,nhưngfailuremodelà thay thế data thật, không phải synthetic per se. Giữ neo data thậtcố định +tích luỹ synthetic →tránhcollapse. Retraining2025 — Từlịchcốđịnh →drift-triggered + PEFT/LoRA rolling update, gate bằng eval tự động trướckhi deploy. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 40 / 58

---

<!-- chiron-source-span: {"source_span_id":"366663c9-835f-5af9-a3f6-7b9a65cceff1","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Frontier2026: Agentic DataEngineering","extraction_method":"pdf-text-layer"},"checksum":"5f80854736ad0ee510370368dd97afcfefb92ea70dda8caba324541655a527ff"} -->

## Slide 43 - Frontier2026: Agentic DataEngineering

1. Copilot: dbt Copilot /SQLMesh AI sinh model + testtừ NL, người review diff

2. Agentdựng pipeline: từ 1 câu(“pull 7 ngày Shopify,flatten JSON, ghi BigQuery”)→tạodbt model+ test + schedule Airflow

3. Self-healingDAG:agent đọc log task fail+ lineage →đềxuất patch →mởPR NLspec Agent(LLM) dbtmodel + GE/Pandera test +schedule CIeval gate + data contract fail → re-plan Bạnsẽ giám sát agent,không chỉ viết DAG. Cáilàm nó an toàn:evalgate + datacontract củachính bài hôm nay. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 41 / 58

---

<!-- chiron-source-span: {"source_span_id":"ab3f0400-7c64-543f-92d9-0e67ebe48097","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"ThựcHành 1: AgentTrace →Bronze(Code Của Flywheel)","extraction_method":"pdf-text-layer"},"checksum":"a33433e0c44354702b1394eec1b4a6f91323dd364365117e159865d09348f21b"} -->

## Slide 44 - ThựcHành 1: AgentTrace →Bronze(Code Của Flywheel)

# 1 agent turn (OTel gen_ai span) -> 1 Bronze row

```text
def span_to_row(span):
a = span.attributes
return {
```
"trace_id": span.context.trace_id, "ts": span.start_time, "model": a["gen_ai.request.model"], "prompt": a["gen_ai.prompt"], "response": a[ "gen_ai.completion"], "tool_calls": a.get( "gen_ai.tool.calls"), "tok_in": a["gen_ai.usage.input_tokens"], "tok_out": a[ "gen_ai.usage.output_tokens"], "feedback": a.get( "user.feedback"), # up/down } # OTLP / Kafka -> append-only Bronze (partition by day) write_bronze([span_to_row(s) for s in spans]) Trace của agent Day 3/9 thành Bronze record. SchematheoOTel gen_ai.*sem- conv(GD1Day13);Day27làobservabil- ityruntime.

- Silver: PII redact +dedup theo
trace_id

- Partitiontheo ngày →incremental

- Gold: turn sạch choeval / fine-tune
Giảngviên (VinUni) AICB· Ngày 17 Tuần4 42 / 58

---

<!-- chiron-source-span: {"source_span_id":"3a47db3d-8624-5c42-9e66-5ad9c96a2e9e","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"ThựcHành 2: RAGIngestion Là Một Production DAG","extraction_method":"pdf-text-layer"},"checksum":"3be08296ec33faccb29c05616b8c285827d0a100bf8cafbd80e713533829bfe4"} -->

## Slide 45 - ThựcHành 2: RAGIngestion Là Một Production DAG

@dag(schedule= "@hourly", catchup=False)

```text
def rag_ingest():
```
@task

```text
def discover(): # incremental, KHONG full
return [d for d in list_docs()
if hash_changed(d)] # chi doc doi
```
@task #.expand: fan-out per doc

```text
def parse_embed(doc):
chunks = recursive_split(parse(doc), 512)
ok, bad = validate(chunks) # quarantine
write_quarantine(bad)
return [{"id": cid(doc, c), "vec": embed(c),
"source": doc.uri} for c in ok]
```
@task

```text
def upsert(rows): # idempotent: upsert by id
vectordb.upsert(rows) # re-run an toan
upsert(parse_embed.expand(doc=discover()))
```
Frame §3 vẽ doc →chunk→embed

### phẳng. Đây là phiên bảnorchestrated
dùngprimitivecủachínhngàyhômnay.

- Incremental: re-embed theo content
hash →10-15%,không 100%

- Idempotent: upsert by id,replay an
toàn

- source=provenance cho security gate
Vectorstore sâu hơn→Ngày19. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 43 / 58

---

<!-- chiron-source-span: {"source_span_id":"994c60b1-6720-53c7-8fdd-acd15fd78d49","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"ThựcHành 3: Gold→FeatureStore →AgentInference","extraction_method":"pdf-text-layer"},"checksum":"64da2570cbe2b862c544db02847732c7a633aefed3898f048f5f0ec8028974da"} -->

## Slide 46 - ThựcHành 3: Gold→FeatureStore →AgentInference

# Gold mart (dbt) -> Feast feature view user_fv = FeatureView( name= "user_features", entities=[user], schema=[Field( "orders_7d", Int64), Field("avg_order_value", Float32)], source=gold_user_features, # bang Gold cua Lab 17 ttl=timedelta(days=2)) # OFFLINE (train): point-in-time correct store.get_historical_features( entity_df, features).to_df() # ONLINE (agent quyet dinh, ms latency) store.get_online_features( features, [{ "user_id": uid}]) Một FeatureView phục vụ cả train (of- fline) lẫn agent inference (online)→ diệt training-servingskew.

- Gold(Lab 17) → source

- feature_ts →point-in-time

- materializeincremental
Featurestore dựng ở→Ngày19. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 44 / 58

---

<!-- chiron-source-span: {"source_span_id":"08e3e73a-7259-5b44-8160-ded97c4f09ab","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"ThựcHành 4: Eval& Preference Dataset Từ Trace","extraction_method":"pdf-text-layer"},"checksum":"cff44b41bb1357c48642c1df85524ded879eddcf1b3067ac7ce99dabfa93f5cd"} -->

## Slide 47 - ThựcHành 4: Eval& Preference Dataset Từ Trace

# Prod traces -> eval set (Day14) + DPO (Day22)

```text
def curate(traces):
golden, prefs = [], []
sample = stratified_sample( # khong bias
traces, by= "intent", n=500)
```

### for t in sample
score = llm_judge(t.prompt, t.response) golden.append({**t, "label": score}) # eval

### if t.feedback == "down" and t.regenerated
prefs.append({ # DPO pair "prompt": t.prompt, "chosen": t.regenerated, "rejected": t.response}) prefs = decontaminate(prefs, eval_set=golden)

```text
return golden, prefs
■ Goldeneval set(Day14): label
```
bằngLLM-judge, freeze

- DPOpairs (Day22): chosen =turn
ngườidùng sửa / thumbs-up Lưu ý:Decontaminate: gỡ ví dụ trùng eval set khỏi trainset — nếu không, điểmDay 14 vô nghĩa. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 45 / 58

---

<!-- chiron-source-span: {"source_span_id":"3309bebe-2954-5eaf-9703-7bcdac0c8697","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"ThựcHành 5: DataLoader Cho GPU Training(Infra)","extraction_method":"pdf-text-layer"},"checksum":"ed9d46dd3b48c5c62d17287ab94d47ebb9d4735c03a3f8249f6d03482bd12691"} -->

## Slide 48 - ThựcHành 5: DataLoader Cho GPU Training(Infra)

```text
import webdataset as wds
```
# Lakehouse Gold -> sharded tar cho multi-GPU # moi GPU stream 1 slice rieng (khong shuffle ca set) ds = (wds.WebDataset( "s3://gold/shards/{000..255}.tar", shardshuffle=True, nodesplitter=wds.split_by_node) .shuffle(1000).decode().to_tuple("json")) loader = DataLoader(ds, batch_size=32, num_workers=8, pin_memory=True) # streaming: khong materialize toan bo dataset vao RAM

### for batch in loader
train_step(batch) Outputcủapipelinephải nạp đượcvàoGPU nhanh—nếukhông,GPUđóidata,lãngphí $$.

- Shard256-512MB(đúngsmall-files target
§14!)

- Streaming: không load cảset vào RAM

- num_workers +prefetch overlap I/O với
GPUcompute

- Shardtheo node →nocross-GPU shuffle
bottleneck Modelserving / inference→Ngày20. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 46 / 58

---

<!-- chiron-source-span: {"source_span_id":"03d56cae-9336-592a-861b-f96eaf9514c0","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"ComplexUnstructured →Structured: VLM Parsing","extraction_method":"pdf-text-layer"},"checksum":"36a87641fabf96ef09d0263d116875bac538ab805686e754546b13c8febd4066"} -->

## Slide 49 - ComplexUnstructured →Structured: VLM Parsing

Lưu ý: PDF thực tế bẩn: bảng, hình, multi- column, scan. Parse phẳngread_text() → lẫn cột,mất bảng →pháretrieval ngay từ ingest. Một vision-language model làm cả layout + reading-order + OCR + bảng→ markup có cấu trúc(DocTags). Thay pipeline OCRnhiều tầng.

- Granite-Docling-258M(IBM,9/2025,
Apache2.0): nhỏ, chạylocal

- Surya2 / Marker,dots.ocr,olmOCR 2
Parser Đặcđiểm Docling/ Granite-Docling bảng phức tạp 97.9%;OSS, local LlamaParse nhanh(~6s) nhưng multi-column dễ lẫn unstructured.io rộngđịnh dạng, automation-first ColPali bỏ qua parsing(frame kế) Lưu ý:Cảnh báo benchmark:phần lớn số liệu là vendortự chấm. Con số 97.9% (Docling) từ Procycons — bên thứ ba trung lập. Tự đo trên datacủa bạn. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 47 / 58

---

<!-- chiron-source-span: {"source_span_id":"f1b11288-dc97-5bdd-84ba-f3a877cecedf","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"IndexPipeline Cho Complex RAG: HơnCả “Chunk + Embed”","extraction_method":"pdf-text-layer"},"checksum":"fdefbb50584108c0d8d31d6bf455dc6a3656dc50c676a90c1c9a333f72edaa6a"} -->

## Slide 50 - IndexPipeline Cho Complex RAG: HơnCả “Chunk + Embed”

Embed child nhỏ (100-500 tok) đểtìm chính xác, trả parent lớn (500-2000 tok) cho LLM đểđủ ngữ cảnh. Parent ≈3-5×child. (LangChainParentDocumentRe- triever/ LlamaIndex.) ThêmblurbngữcảnhdoLLMsinhvàomỗichunk trước index → retrieval-failure −49% (−67% kèm rerank). Khảthi nhờ prompt caching: ~$1.02 / triệu token doc. Embed cả doc (long-contextembedder,8ktok)rồimới cắt + pool→ mỗi chunk “thấy” toàn doc,không tốn LLM/chunk. Ingestdựng 2index trêncùngchunk: dense(vector)+ sparse(BM25/SPLADE) →mergebằngRRF →cross- encoder rerank. BM25 thắng từ hiếm (SKU, mã lỗi); densethắng paraphrase. Semantic/propositionchunking: chưacóconsensus 2026 là tốt hơnrecursive — đo,đừng mặc định. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 48 / 58

---

<!-- chiron-source-span: {"source_span_id":"d15517fa-27ee-5bb4-b347-ca650dacc456","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"Late-Interaction(ColPali): Khi ParsingLà Sai Lầm","extraction_method":"pdf-text-layer"},"checksum":"e6c9feb2ced8925377d924dd5cf78191ce13abc648fc7eec8212c88ee3f55799"} -->

## Slide 51 - Late-Interaction(ColPali): Khi ParsingLà Sai Lầm

Đừng parse text. Encode ảnh trang thành ~1024 patch-embedding (SigLIP + PaliGemma), match kiểu ColBERT MaxSim.Bỏ qua OCR/parsing hoàn toàn —giữ nguyên bảng, chart, layout. Khi nào dùng— Doc giàu hình ảnh: scan, chart, form, slide — nơi parser text làm hỏng cấu trúc. Vi- DoRe v2 (3/2025) là benchmark hiện tại (đừng trộn điểmv1/v2). Lưu ý: Cái giá ở ingest = storage blowup: ~1024 vector/trang (1 bậc lớn hơn BM25, 2 bậc hơn single- vector).

- Binarization: 128 float→16byte (~32×nhỏ
hơn)

- Token/patchpooling;HPC-ColPali (centroid)

- Vespa/ Qdrant scale tớitỉ trang
Multi-vectorđổi bài toán index, khôngchỉ retrieval→Ngày19. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 49 / 58

---

<!-- chiron-source-span: {"source_span_id":"a199d940-3cbe-580e-95ca-ca1e776e9eb3","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"KnowledgeGraph Pipeline: TríchEntity & Relation Bằng LLM","extraction_method":"pdf-text-layer"},"checksum":"fd038c3b2e33c12f3858203f0f4d98579062a2b4927d5f5b8cee0f3c5fd992fe"} -->

## Slide 52 - KnowledgeGraph Pipeline: TríchEntity & Relation Bằng LLM

```text
from langchain_experimental.graph_transformers \
import LLMGraphTransformer
tf = LLMGraphTransformer(
llm=llm,
allowed_nodes=[ "Person", "Company", "Product"],
allowed_relationships=[ "WORKS_AT", "BUILDS"],
) # schema rang buoc -> graph sach hon
docs = chunk(parse(raw_docs)) # complex parse
graph_docs = tf.convert_to_graph_documents(docs)
neo4j.add_graph_documents( # upsert nodes/rels
graph_docs, include_source=True) # giu provenance
```

1. Parse →chunk

2. LLMextract node + relation (theo schema)

3. Entityresolution: gộp “IBM” = “I.B.M.”(phần khó nhất)

4. Incrementalmerge (đừng rebuild) Neo4j LLM KG Builder (Leiden communi- ties,2/2025)·LlamaIndexPropertyGraphIn- dex(graph + vector trong 1index). Giảngviên (VinUni) AICB· Ngày 17 Tuần4 50 / 58

---

<!-- chiron-source-span: {"source_span_id":"b80721dd-6359-5136-b68b-f952416005c7","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"GraphRAG:Khi Nào Graph Thắng VectorRAG?","extraction_method":"pdf-text-layer"},"checksum":"fdd0b2ae66fcfe65b8c9aff1a4f2cf5dc6827ec61a12b9dabfe7edb16a8630f4"} -->

## Slide 53 - GraphRAG:Khi Nào Graph Thắng VectorRAG?

LLMextractentity →Leidencommunities →LLMtóm tắt community. Query: local (quanh entity), global (map-reducemọi community),DRIFT(cânbằng).

- Multi-hopreasoning (nốinhiều mẩu)

- Summarization/ global sense-making(“chủ
đềchính của cả corpus?”) Lưu ý:Khi nào graphTHUA: fact lookup đơn giản — basic RAG 60.9% vs GraphRAG 49.3%.Không phải upgrademiễn phí. Lưu ý:Cái giá = token: global search ~331k token/- queryvs vanilla ~879.

- LazyGraphRAG:index 0.1%, query rẻ>700×

- LightRAG:incremental update (không
re-index)

- fast-graphrag: PageRank thay map-reduce
Giảngviên (VinUni) AICB· Ngày 17 Tuần4 51 / 58

---

<!-- chiron-source-span: {"source_span_id":"7b5a93ce-00a1-59b8-955f-dd4b8bd6b847","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"Idempotency: TiềnĐề ChoRetry,Replay,Backfill","extraction_method":"pdf-text-layer"},"checksum":"677d0196b2da697739da872d637efb6313039a85af27f5637bf33a94608029de"} -->

## Slide 54 - Idempotency: TiềnĐề ChoRetry,Replay,Backfill

Loạipipeline Pattern idempotent Cơchế Batch Overwrite-partition Ghiđè cửa sổ reprocess (khôngappend) Merge/ CDC Upserttheo natural key order_id, txn_id Event-driven Deduptheo idempotency key Audit log các event_id đãxử lý Lưu ý: Bất biến: pipeline phải an toàn khi chạy lại / replay / backfillbao nhiêu lần cũng được mà không nhân đôi rows, không double-charge, không double- send. Exponential backoff (Airflow 3.2: multiplier cấu hình được, không còn cứng x2), bounded max_retry_delay. Calibrate theo rate-limit up- stream để tránh thundering-herd. Replay & backfill là first-classops. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 52 / 58

---

<!-- chiron-source-span: {"source_span_id":"e8cb4046-72fd-5dac-b07d-68d0b5f42c3c","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"Cost: Small-Files, Incremental, FreshnessSLO","extraction_method":"pdf-text-layer"},"checksum":"fbbfcf2a70ae724853d53e27d6e5b46ac256584f7aed111a9a18b8377837ebf9"} -->

## Slide 55 - Cost: Small-Files, Incremental, FreshnessSLO

Lưu ý: Small-files problem là failure mode cost+reliability số 1 của lakehouse. Target 256- 512MB/file Parquet; file <128MB → metadata bloat + query-planning chậm. Compaction (rewrite/optimize của table format) định kỳ là trách nhiệm scheduling củapipeline; cơ chế→Ngày18. Paxos giảm ~50% chi phí data-platform khi chuyển sangincrementalmodels(báocáocủaPaxos). Cluster nhỏ hơn, chạy thường xuyên hơn.Compute (không phảistorage) chi phối hoá đơnwarehouse. 2 loại:completion-rate (“99% job hoàn tất”) &fresh- ness (“data cập nhật trong 4h”). Tier theo độ quan trọng (vd: 99.9% payments / 99.0% analytics — con sốminh hoạ). Late data (streaming) — Watermark theo event- time; forBoundedOutOfOrderness()đặtmax-lateness. ConfluentFlink: late-handling.mode=filter đẩylate eventsvào System Table$lateđểreprocess. FinOps/ GPU cost sâu hơn→Ngày25. SLO &incident response→Ngày27. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 53 / 58

---

<!-- chiron-source-span: {"source_span_id":"acce031b-444f-5bc0-9527-bff5fd653808","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"PipelineRecipe: Skeleton Copy-Paste+ Thẻ Quyết Định","extraction_method":"pdf-text-layer"},"checksum":"319dc3880d146b3a6fe6ae4566f55cac7c9a0d0511260fcb0fbba4455eb74e6e"} -->

## Slide 56 - PipelineRecipe: Skeleton Copy-Paste+ Thẻ Quyết Định

# 1. INGEST (disposition: merge / replace / append) raw = ingest(source, primary_key= "id", disposition= "merge") # dlt / CDC / Kafka write("bronze.events", raw) # giu RAW bat bien # 2. DEDUP @ Silver (idempotent: upsert by key) silver = dedup(read( "bronze.events"), key= "id") # 3. GATE (fail early -> quarantine, KHONG sap) ok, bad = schema.validate(silver, lazy=True) write_quarantine(bad); alert_on_spike(bad) # 4. TRANSFORM (dbt: stg_ -> int_ -> marts; test) gold = dbt_build(select= "tag:ml_features") # 5. SCHEDULE (catchup= False, max_active_runs=1)

- Traindata →batchELT+ Medallion

- Real-timefeature →Kafka+ Flink

- Cầnbắt delete / low-lag sync→CDC

- Nhiềufile nhỏ →compaction
256-512MB

- Costcao →incrementalmodels
Lưu ý: Bất biến: an toàn để re-run/replay/backfill bao nhiêulần cũng được. Đây chính là Lab 17. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 54 / 58

---

<!-- chiron-source-span: {"source_span_id":"e9276702-e3c2-580d-b862-c959d2d702a1","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"LiveDemo: End-to-End DataPipeline","extraction_method":"pdf-text-layer"},"checksum":"7641bd6e8e67f7f5383005e11ec2ba9faed2e8c2b20ef948c942a774be0f7ae6"} -->

## Slide 57 - LiveDemo: End-to-End DataPipeline

1. Bước1 — Orchestrate:DAGingest S3/DuckDB →Bronze →Panderagate

- dbtrun →Gold

2. Bước2 — Dedup ở Silver:inject30% duplicate records→deduptheo key

- đếmrows giảm

3. Bước3 — Bad data:injectrecord sai schema→gatefail →quarantine/DLQ kíchhoạt

4. Bước4 — dbt test:dbt test (not_null/unique/unittest) pass; dbt docs servexemlineage

5. Bước5 — Streaming sim:producerevents →consumercập nhật feature; (bonus)doc →chunk →embedding Giảngviên (VinUni) AICB· Ngày 17 Tuần4 55 / 58

---

<!-- chiron-source-span: {"source_span_id":"8200f954-75b7-54e1-84e5-cde4db9ddaa0","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"a2663f9e5b7cc30740c56e3fbf022dea8de0581d308e27ae7513870a21836363"} -->

## Slide 58 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 Pipeline là mộtdependency của model: Medallion (Bronze/Silver/Gold), luôn giữ raw, dedup ởSilver. Pipelinehỏng âm thầm = model hỏngâm thầm. 2 Orchestrate(Airflow3/asset-basedDagster)+ingest(dlt/CDC/Kafka)+transform(dbt/declar- ative)+ validationgates =stack production-ready cho AI data. 3 Idempotency là tiền đề cho retry/replay/backfill an toàn. Data contracts ép chất lượng tại nguồn. Fail early,quarantine bad records, save compute. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 55 / 58

---

<!-- chiron-source-span: {"source_span_id":"c9238020-b4b6-5ba6-9f85-edf139b6a58b","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"Lab17 Là Hạ Tầng ChoCả Phase 2","extraction_method":"pdf-text-layer"},"checksum":"530f5bd4b1adff7165a0f196798068af5f93325b622aac5e1d99de32b6d17f0a"} -->

## Slide 59 - Lab17 Là Hạ Tầng ChoCả Phase 2

LAB17 ARTIFACT Bronze→Silver→Gold +Pandera gate + dbt tests Day18 Lakehouse Bronze →Delta/Iceberg(ACID, time-travel); dedup→MERGE Day19 Vector/Feature Goldmarts →Feastfeature views Day22 Alignment Goldturns →SFT/DPOjsonl Day14 Eval qualitygates →regressiongate Day27 Observability →nguồntrace Outputcủa Lab 17là input củacác ngày sau. Course tích luỹ: làmtốt pipeline hôm nay→mọingày sau nhẹ hơn. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 56 / 58

---

<!-- chiron-source-span: {"source_span_id":"fff0fd64-66b3-53c3-b9cf-876e255dbce0","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"f2c279876169d8113da74b4a71398af5eb75db41f9b6b98b450e74b612bc659d"} -->

## Slide 60 - Tiếptheo & Bài tập

Ngày18: DataLakehouseArchitec- ture “Delta Lake, Apache Iceberg, ACID transactions, time travel — nơi data pipeline đổ vào table format mở”

- Hoànthành Lab 17: pipeline
ingest→validate→transform→load (dedup+ gate + dbt test)

- Đọctrước: Delta Lake& Apache
Icebergdocumentation

- Suynghĩ: bài toándata storage
choproject nhóm Giảngviên (VinUni) AICB· Ngày 17 Tuần4 57 / 58

---

<!-- chiron-source-span: {"source_span_id":"69143b62-92aa-55f4-9959-709495d2e96c","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"Lab#17","extraction_method":"pdf-text-layer"},"checksum":"5ad05f7e7fb1279433d04aa807a60b30f3c08ec33c0e2d3b7aa85e97592488bd"} -->

## Slide 61 - Lab#17

Mục tiêu: Xây pipeline Medallion chạy được: DuckDB Bronze→Silver→Gold với dedup, Pandera quality gate + quarantine, dbt-duckdb models pass test, orches- tratebằng DAG thuần Python (lite) hoặcAirflow (Docker bonus). Deliverable: Pipeline+dbtproject+validationsuitetrongrepo,chạyzero-keytrên mock/DuckDB.

```text
Thời gian: Lite path: chỉ cần pip install. Docker bonus: Airflow + Redpan-
```
da/Kafka. Giảngviên (VinUni) AICB· Ngày 17 Tuần4 58 / 58

---

<!-- chiron-source-span: {"source_span_id":"b379493d-0aa0-58a2-8ffe-b382b1a2102d","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"77dc4cd295c445083d016afb3b1189cb61b8d9134521a2fc327c6ae261b72a20"} -->

## Slide 62 - Hỏi& Đáp

Câu hỏi về ETL/ELT, orchestration, Kafka, val- idation, data contracts, hay AI pipelines?

---

<!-- chiron-source-span: {"source_span_id":"38a4002f-1131-5d58-b943-e0eb005db3e5","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"1dcf5f932e9c7911b4a1fe040db6fdd4f547ec560c6adecc6ff0783ea22bf868"} -->

## Slide 63 - Cảmơn!

AICB-P2T2 · Ngày 17 Data Pipeline Engineering lms.vinuni.edu.vn · Slide & template trên LMS
