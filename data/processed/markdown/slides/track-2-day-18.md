---
schema_version: 1
course_id: rag-intensive
document_id: "976d0c57-09e6-5862-b908-3eb76987250e"
document_version_id: "15009fa9-7fcf-5d03-b271-5e51e6141b59"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Data Lakehouse Architecture"
source_file: "track 2 - day 18.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 18.pdf"
source_sha256: "9fe50b7a5a6a1f72f1b3fbd99d9ce4f6089e3275f3fad30df38a3a6e926f49cc"
parser_version: chiron-structured-markdown-v1
page_count: 40
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":40}"
language: vi
---

# Data Lakehouse Architecture

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"70bc50ad-43b6-59a4-8078-71d5a1393ef6","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Data Lakehouse Architecture","extraction_method":"pdf-text-layer"},"checksum":"ac2ac293ddfcbc4d559f785b0980ab81e76183ed84afe90f0d65016eb501a965"} -->

## Slide 1 - Data Lakehouse Architecture

AICB-P2T2 · Ngày 18 · Chương 4: Hạ Tầng Giảngviên VinUniversity · Phase 2 · AI Infrastructure Track· Tuần4

---

<!-- chiron-source-span: {"source_span_id":"986152d1-e0ab-5708-b43b-2a24332bdf8b","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"a8d64a97f7ab547a680629ec8382a206a071effcbc4b720371055be7bf2d6486"} -->

## Slide 2 - HÃYSUY NGHĨ...

? ““Đổ tất cả vào S3” — works ở 10GB, ác mộng ở 10TB, production outage ở 10PB. Lakehouse = ACID + cheap storage + AI workloads. Câu trả lời cho 3 era: Traditional, ML, LLM.” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"e4785195-ef0b-5da5-8de0-ed07bd2c0a53","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"97ef9cf0d100f858c827f9babbd69be68a1e9675d1c2d42562f8d90becc9930a"} -->

## Slide 3 - NộiDung Bài Học

1. Evolution+ 3 Eras (Trad/ML / LLM)

2. DeltaLake: ACID +Deletion Vectors +CDF

3. TimeTravel& Data Versioning

4. ApacheIceberg: Hidden Partitioning, v3

5. QueryEngines (Spark/Trino/DuckDB)

6. StorageOptimization & Anti-Patterns

7. FormatInternals & Performance Tuning

8. Lakehousecho AI/ML Workloads

9. Streaming& CDC Ingestion

10. IndustrialDeep Dive (AI Thực Chiến)

11. ProductionOps (Catalog, DQ, Lineage,Security,FinOps)

12. Demo+ Lab repo (notebooks 01–04) Giảngviên (VinUni) AICB· Ngày 18 Tuần4 1 / 35

---

<!-- chiron-source-span: {"source_span_id":"856e3fc5-29c5-5fb5-8ae6-e7b8034fac6f","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mụctiêu bài học","extraction_method":"pdf-text-layer"},"checksum":"0f1d41c134b36222e9dc74386625adb0c564ab535c5a5bdd4e9a2407eaa3bbc2"} -->

## Slide 4 - Mụctiêu bài học

### Saubuổi học này,bạnsẽ

1. Hiểuevolution storage qua 3 era:Traditional →ML →LLM

2. Triểnkhai Delta/Iceberg: ACID,time travel, deletion vectors, CDF

3. Sosánh Delta vs Iceberg vs Hudi→chọntheo workload (append / mutate / multimodal)

4. Thiếtkế medallion Bronze/Silver/Gold cho LLM observability+ RAG corpus

5. Ápdụng production ops: catalog, data contracts, lineage, FinOps Evolution+3Eras →Delta+Iceberg →Storage&Performance →AI/LLMWorkloads

- IndustrialCases →ProductionOps →Demo
Giảngviên (VinUni) AICB· Ngày 18 Tuần4 2 / 35

---

<!-- chiron-source-span: {"source_span_id":"285eb38a-7314-5355-b196-b5cdf0bd1471","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"7430925dc829c9326632460afc9899fc9e5880ae12dab0c6ce0cef1637051775"} -->

## Slide 5 - DeliverableCuối Ngày

LakehouseBronze/Silver/Gold+DeltaACID+timetravel+benchmark—1-to-1với notebookstrong lab repo.

- NB1—Delta Lake table với schemaenforcement + transaction log

- NB2—OPTIMIZE + Z-ORDER benchmark: query time trước/sau (chứng minhsmall-file
problem)

- NB3—Timetravel: restoreToVersion +MERGE upsert

- NB4—Medallion pipeline Bronze→Silver →Goldcho LLM observability hoặc RAGcorpus
Labrepo: github.com/VinUni-AI20k/ Day18-AIInfrastructure-Lakehouse-Lab Giảngviên (VinUni) AICB· Ngày 18 Tuần4 3 / 35

---

<!-- chiron-source-span: {"source_span_id":"5b09865d-58db-5d74-8511-6ddb4508343a","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Evolutionof Data Platforms","extraction_method":"pdf-text-layer"},"checksum":"28a3a18df21581e79d32d15559bd75df81425e428a815ddaa95b33cf01709ed4"} -->

## Slide 6 - Evolutionof Data Platforms

Data Warehouse Data Lake Data Lakehouse 2000s 2010s 2020s Structured, SQL · Fast queries Đắt, kém flexible Cheap, flexible · Any format “Data swamp” ACID + cheap storage Open formats · Best of both Key Innovation:metadata layer biến S3 object storage thành transactional store. Enablers: Open table formats (Delta/Iceberg/Hudi) + cheap object storage (S3) + query engines (Spark/DuckDB/Trino). Giảngviên (VinUni) AICB· Ngày 18 Tuần4 4 / 35

---

<!-- chiron-source-span: {"source_span_id":"b4c2399e-c620-5250-893d-9ef8ac93b5f7","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"3Eras of Software: WorkloadDrives Storage","extraction_method":"pdf-text-layer"},"checksum":"de3b62c98a87668d2fd80f1b9d3dd7a9511a1a4d9093a24e1a37c8c1d86d2e2e"} -->

## Slide 7 - 3Eras of Software: WorkloadDrives Storage

Aspect Traditional(1990s–2010) ML Era ( ∼2012–2022) LLMEra (2022+) Workload OLTPtxn, BI reports Featureeng,batchtrain/infer Pretraining(T tokens), fine-tune, RAG,eval Datashape Tabular,3NF normalized Tabular+ semi-structured (JSON) Text+ multimodal + embeddings Volume GB–TB TB–PB PB+raw, 1012+tokens, billions vectors Latency ms(txn), hours (BI) Min–hours(batch ML) Hours(train) + sub-100ms (RAG) Schema Schema-on-write(rigid) Schema-on-reador hybrid Hybrid+ lineage + contracts + provenance Compliance SOX,PCI, GDPR +biasaudit, fairness +trainingdata provenance, copyright,hallucination Failuremode Schemadrift, deadlock Datadrift, train/serve skew Dedupleak, license violation, hallucination Pattern: mỗiera thêmmộtclass data mớimàera trước không có (semi-structured→multimodal+embeddings). Storagestack mởrộng,không thay thế. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 5 / 35

---

<!-- chiron-source-span: {"source_span_id":"7492bc46-0305-5ce0-9a09-ce390c6e2844","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"StorageTech ×EraFit + LLM Demands","extraction_method":"pdf-text-layer"},"checksum":"d19b6a7d9439f94a29a0f45d9aaf431fbd347046915c2808f8dea1389b7f1711"} -->

## Slide 8 - StorageTech ×EraFit + LLM Demands

Tech Traditional MLEra LLMEra OLTPDB (Postgres) Primarysystem Appbackend; CDC source for ML Appbackend; CDC; user feedback Warehouse(Snowflake) BIreporting Featureaggregation + serving BIdashboards on LLM telemetry DataLake (S3 + Hive) — Rawevents, training datasets Rawcrawls, multimodal blobs Lakehouse (Delta/Iceberg) — UnifiedBI + ML feature store Trainingcorpus + RAG + eval+ prompt logs VectorDB (Qdrant/Milvus) — Recommendation(rare) OnlineRAG (sub-100ms) Multimodal(Lance) — — Video/image/audio+ embeddings

### LLM-erademands trên Lakehouse

- Trillion-tokendedup (MinHashLSH)

- Multimodalblobs (Lance/ Iceberg)

- Embeddingversioning (doc_v ×model_v)

- Trainingdata provenance(Icebergv3)

- Licensegovernance (per-doctag)

- Evalgolden sets(Icebergtags)

- Prompt+ trace logs→Bronze
LLMera thêmtầng (vectorDB, multimodal) vàéplakehouse =dataset-of-recordcho compliance. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 6 / 35

---

<!-- chiron-source-span: {"source_span_id":"bc7457f6-7a58-5237-a885-e4310bdba5f1","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"DeltaLake TransactionLog","extraction_method":"pdf-text-layer"},"checksum":"dbc0575981eda7453013975f4c0b8d5babfd1bf74c0ba4194448d7b6eefd6344"} -->

## Slide 9 - DeltaLake TransactionLog

_delta_log/ 000.json 001.json 002.json 003.json addpart-001, part-002 addpart-003 removepart-001 addpart-004 ParquetFiles part-001 part-002 part-003 part-004 ACID: Atomicity + Consistency + Isolation + Durability trên S3 ·Concurrency: optimistic con- flict detection ·Metadata layer:JSON log biến object store→ transactional table. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 7 / 35

---

<!-- chiron-source-span: {"source_span_id":"ad729a7f-4c5f-5253-8bb3-c068f56d5fe1","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"DeltaLake: Thao TácQuan Trọng","extraction_method":"pdf-text-layer"},"checksum":"c99696ebef29ab39b11fcf562c793a7e280aefa079112e960b1d9cf5f02b02b8"} -->

## Slide 10 - DeltaLake: Thao TácQuan Trọng

- df.write.format("delta") —basic
write

- MERGE INTO... =upsert. Workshop
100K ∼2×;prod 100M+ →10–50×vs overwrite

- Schemaevolution: mergeSchema=true

- Compact →target128MB–1GB

- 10,000 ×1MB →10 ×1GB

- Z-ORDER:3–10 ×typical;100 ×bestcase

- VACUUM table RETAIN 168 HOURS

- Dài =nhiềucost, audit tốt

- Ngắn =ítcost, mất rollback window

- Regulated30+ ngày; startup 7 ngày

- Successorcho Z-ORDER: incremental
re-cluster

- Khôngcần rewrite toàn bộ table

- GADatabricks; OSS Delta 3.3+ đangmở
rộng Giảngviên (VinUni) AICB· Ngày 18 Tuần4 8 / 35

---

<!-- chiron-source-span: {"source_span_id":"b2f2fc01-f311-5733-97ac-8baa58d71da4","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"DeletionVectors& Change DataFeed","extraction_method":"pdf-text-layer"},"checksum":"7116563d90dd7c145e85266b3e9d07cd8431fd984db49527159c6c5b069c4507"} -->

## Slide 11 - DeletionVectors& Change DataFeed

Vấnđề: DELETE1row →rewritecảfile(writeam- plification1000 ×). Cáchhoạtđộng: Lưubitmapđánhdấurowsbịxoá trong sidecar file. Reader skip rows theo bitmap. Khôngrewrite Parquet.

### Lợiích

- DELETE/UPDATE/MERGE10–100 ×nhanh
hơn

- GDPR DELETE FROM... WHERE user_id=X
từgiờ →phút

- Compact-on-read;physical removal khi
OPTIMIZE Bật: ALTER TABLE... SET TBLPROPERTIES('delta.enableDeletionVectors'=true) Use case: downstream consumer cần biếtcái gì thayđổi,không phải full snapshot. Cách bật: TBLPROPERTIES (delta.enableChangeDataFeed = true)

### Đọcdeltas
spark.read.format("delta") .option("readChangeFeed","true") .option("startingVersion", 5) .table("silver.users") Output columns: _change_type (insert / up- date_pre / update_post / delete) + version + times- tamp. Pattern: BronzeCDF →SilverMERGE →Goldin- crementalrefresh =streaming-likebatch. Kếthợp: Deletion Vectors+ CDF + MERGE =canonical CDC sink pattern. Không cần custom apply logic.Giảngviên (VinUni) AICB· Ngày 18 Tuần4 9 / 35

---

<!-- chiron-source-span: {"source_span_id":"2a29674e-8da8-5e2f-af79-ac6445224774","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"TimeTravel: API","extraction_method":"pdf-text-layer"},"checksum":"f1a7cf626bfa69d322ebf4927cb3ca8555c5d5aeb3f8e5522bd9caaf11415302"} -->

## Slide 12 - TimeTravel: API

# Version-based df = spark.read. format("delta") \ .option("versionAsOf", 5).load(path) # Timestamp-based (point-in-time query) df = spark.read. format("delta") \ .option("timestampAsOf", "2025-01-15 00:00:00") \ .load(path) # Restore (rollback) --- creates new version ớvi same data as v10 DeltaTable.forPath(spark, path).restoreToVersion(10) # Audit trail spark.sql("DESCRIBE HISTORY delta.`{}`".format(path)).show() 3cách query history:versionAsOf (sốversion), timestampAsOf (point-in-time), restoreToVersion (rollback). DESCRIBE HISTORY =compliance-grade audit log đi kèmbuilt-in. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 10 / 35

---

<!-- chiron-source-span: {"source_span_id":"f34d0bf8-19a9-5965-bb7c-68da351aef91","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"TimeTravel: UseCases & Limits","extraction_method":"pdf-text-layer"},"checksum":"162786dc9182645676f6176507dfef57d326db3ef79572bf32dd84f0710b2d81"} -->

## Slide 13 - TimeTravel: UseCases & Limits

- Modelreproducibility — pin training set
version

- Rollbackbad ingestion — instant vs2+ giờ
manualfix

- A/Btest datasets — timestamp queries

- Regulatoryaudit — DESCRIBE HISTORY=
compliancelog

- Bịgiới hạn bởi VACUUMretention (default 7
ngày)

- Schema-incompatibleold versions có thể fail

- Khôiphục ̸=GDPRDELETE — VACUUM
mớixoá vĩnh viễn Lưuý: Timetravel + schema registry=DataContracts. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 11/ 35

---

<!-- chiron-source-span: {"source_span_id":"84c32c4a-d9f2-5e41-b559-b59a9488c4c3","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"DataVersioning& MLflow Integration","extraction_method":"pdf-text-layer"},"checksum":"f3f143087c048f8b4b321bbe8b12c6207eea1161bb0b9e7e1a2349351104d1f4"} -->

## Slide 14 - DataVersioning& MLflow Integration

v0 v1 v2 v3 v4 v5 Initial load Add columns Upsert 100K Bad data RESTORE tov2 New ingest MLflowrun-1 data_version=1 MLflowrun-2 data_version=3 MLflow run_id ↔Deltatable version =reproducibletraining. Full lineage: data→features →model →deploy. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 12 / 35

---

<!-- chiron-source-span: {"source_span_id":"2d9ba76e-4b8d-58d7-8919-504f8708a365","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"DeltaLake vs Iceberg vs Hudi","extraction_method":"pdf-text-layer"},"checksum":"22cb5675a9b8dbec1ff55e226bc712b643940089b5a9e48e8982965e52176cd1"} -->

## Slide 15 - DeltaLake vs Iceberg vs Hudi

Feature DeltaLake Iceberg Hudi ACIDTransactions ✓ ✓ ✓ TimeTravel ✓ ✓ ✓ DeletionVectors ✓(2.3+) ✓(v3) ✓(MOR) HiddenPartitioning × ✓ × Branching/Tagging Tagonly ✓+Nessie × Multi-enginenative viaUniForm ✓(default) ✓ Row-levelUpdates MERGE+ DV MERGE+ DV MOR(fastest) Ecosystem(origin) Databricks(2017) Netflix,Apple (2018) Uber(2016) Icebergmetadata: metadata.json → manifest list → manifests →Parquet. Apache XTableconvert Delta ↔Iceberg ↔Hudi. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 13 / 35

---

<!-- chiron-source-span: {"source_span_id":"64b00356-b957-5fa9-96cd-522c160522c4","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"IcebergHidden Partitioning (Game Changer)","extraction_method":"pdf-text-layer"},"checksum":"94fa277a08f6263f0ba6f6c0883742c4baf1392715725ac7a7b892ed561d6331"} -->

## Slide 16 - IcebergHidden Partitioning (Game Changer)

-- Need extra partition column CREATE TABLE events ( ts TIMESTAMP, ts_day DATE, -- duplicate! user_id BIGINT) PARTITIONED BY (ts_day); -- User MUST filter ts_day

```text
SELECT * FROM events
WHERE ts_day = '2026-04-01';
-- Forgot ts_day = full scan!
SELECT * FROM events
WHERE ts > '2026-04-01'; -- BAD
```
Vấnđề: ts_dayduplicatedữliệu,userdễquênfilter

- fullscan.
-- Partition is a transformation CREATE TABLE events ( ts TIMESTAMP, user_id BIGINT) PARTITIONED BY (days(ts)); -- User filters natural column

```text
SELECT * FROM events
WHERE ts > '2026-04-01';
```
-- Iceberg AUTO-prunes! Transforms: years / months / days / hours(ts), bucket(N, col), truncate(N, col). Partition Evolution: đổi days(ts) → hours(ts) khôngcần rewrite data. Tạisao quan trọng:đasố performance regression trong productionlakehouse là vì userquênpartition column. Hidden

```text
partitioningloại bỏ cả class bugsnày.LinkedInciteđây là lý do chínhmigrate Hive→Iceberg.
Giảngviên (VinUni) AICB· Ngày 18 Tuần4 14 / 35
```

---

<!-- chiron-source-span: {"source_span_id":"dbeb194f-309e-579c-acac-79e72869e77a","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"KhiNào Chọn Iceberg vs DeltaLake?","extraction_method":"pdf-text-layer"},"checksum":"11d150fa1c3a7c21aeb8a872656c7c851cd84e0d8da60f758530b3fb3f8e1a1c"} -->

## Slide 17 - KhiNào Chọn Iceberg vs DeltaLake?

- Databricksecosystem heavy

- Spark-firstworkloads

- Zerofriction với Databricks Runtime

- Teamquen thuộc Delta API

- Multi-engine: cùng 1 tablequery từ Spark,
Trino,Flink, Snowflake

- Vendorneutrality + partition evolution

- RESTCatalog: Polaris (SnowflakeOSS),
Nessie(git-like branching cho data!)

- GDPRrow-level deletes
Adoption2026: Netflix· Apple · LinkedIn ·Adobe at scale. AWSAthena/EMR default. Snowflakenative (Polaris). DatabricksIceberg v3 GA Apr 2026. Iceberg = de factoopen standard. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 15 / 35

---

<!-- chiron-source-span: {"source_span_id":"6ea088fb-9581-5960-81a1-1b21165c28da","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"QueryEngines cho Lakehouse","extraction_method":"pdf-text-layer"},"checksum":"b842f5dd03b13ead2904ac9378b0dbfb34329696d0365a1596fbfae1b834b33a"} -->

## Slide 18 - QueryEngines cho Lakehouse

Engine Sweet Spot Scale FormatSupport SparkSQL ETL,batch ML pipelines TB–PB Delta,Iceberg, Hudi (native) Trino FederatedBI, ad-hoc SQL GB–PB Iceberg(native), Delta (connector) DuckDB Single-nodeanalytics, dev MB–100GB Parquet/Delta/Icebergvia extensions Photon Databricks-onlyfast SQL TB–PB Delta,Iceberg Athena Serverlessad-hoc on S3 GB–TB Icebergnative, Delta read-only

- <100GB, 1 dev:DuckDB—zero infra

- ETLSpark-native: SparkSQL

- BImulti-source: Trino

- AWS-onlyserverless: Athena
ĐừngchạySparkclustercho5GBquery—DuckDB nhanhhơn,rẻgầnnhư 0. Chỉscale-upkhidata >1 nodeRAM. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 16 / 35

---

<!-- chiron-source-span: {"source_span_id":"6eaf5e88-19c8-5f59-9b20-93294eade437","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Columnarvs Row Storage","extraction_method":"pdf-text-layer"},"checksum":"1a89bf3ecca9fe438a62fa5035d23fcd3872d93d55ef6649e8c95a5d8f8dc101"} -->

## Slide 19 - Columnarvs Row Storage

Row-oriented(Avro/JSON) Row1 id name age city Row2 id name age city Row3 id name age city Columnar(Parquet/ORC) id v1 v2 v3 name v1 v2 v3 age v1 v2 v3 city v1 v2 v3 Readonly age!

```text
SELECT 5/100 columns→ đọc ∼5% data (Parquet) vs
100% (JSON). Compression: Snappy (default, fastest),
ZSTD (3× smaller, hơi chậm), GZIP (chậm nhất).
Giảngviên (VinUni) AICB· Ngày 18 Tuần4 17 / 35
```

---

<!-- chiron-source-span: {"source_span_id":"cb450b77-8f5e-52e4-8430-20e2e343e22a","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"PartitionStrategy cho AI Workloads","extraction_method":"pdf-text-layer"},"checksum":"948e999b34ad85db4b787135b5a6964692cdc636b8e6ec33982c816bcbcee882"} -->

## Slide 20 - PartitionStrategy cho AI Workloads

- Target: 100MB –1GB mỗi partition file

- Partitionby low-cardinality: date, region

- Khôngpartitiontheo user_id (high-card)

- Over-partition →smallfiles →slow

- Under-partition →largescans →wasteIO

- Partition: physical directory separation

- Z-ORDER:co-locate within files

- Kếthợp: partition bydate + Z-ORDER by
user_id

- DuckDB:query Parquet trực tiếp từS3

- Zeroinfra, ấn tượng cho<100GB
Giảngviên (VinUni) AICB· Ngày 18 Tuần4 18 / 35

---

<!-- chiron-source-span: {"source_span_id":"1efe7a79-b8c0-5c78-ae6c-682e9db8b24e","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"ParquetInternals: Tại SaoNhanh?","extraction_method":"pdf-text-layer"},"checksum":"fcff627003431a99bc3217ab161d56e90ae1a68bc8ab0c297214c1febe1167b1"} -->

## Slide 21 - ParquetInternals: Tại SaoNhanh?

File Header (PAR1 magic) + Schema RowGroup 1 128MB RowGroup 2 128MB RowGroup 3 128MB Footer: Schema + Stats (min/max/null) + Page Index + Bloom Filters Readerstrategy (4 levels of skip):(1)đọc footertrước (∼KB) →skipRow Groups bằng min/max stats→(2)đọc PageIndex →skippages →(3)dùng BloomFilter skipvalues chắc chắn không có→(4)đọc chỉcolumns trong SELECT. Compression: Snappy(default, fastest) · ZSTD (3×smaller,hơi chậm) · GZIP(chậm nhất).Quytắc: Bronze=Snappy(fast write); Gold=ZSTD(slow write OK, fast read). Practicalimpact: WHERE user_id=42 trên1TB Parquet với bloomfilter→đọc ∼50MB. Cùng query CSV/JSON

- full1TB. 20,000×I/Oreduction.
Giảngviên (VinUni) AICB· Ngày 18 Tuần4 19 / 35

---

<!-- chiron-source-span: {"source_span_id":"e50ecf3b-f986-565f-aee6-4fad724fc85a","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"SchemaEvolution Playbook","extraction_method":"pdf-text-layer"},"checksum":"59737194870d24ea260e019a4377e315f29f5d9090942d09311cb756e88835c8"} -->

## Slide 22 - SchemaEvolution Playbook

Change Safe? How Notes Addcolumn (nullable) ✓ ADDCOLUMN; mergeSchema=true Existingrows =NULL Addcolumn (with default) ✓ Icebergv3 native Delta: backfill MERGE Renamecolumn ∼ Iceberg: RENAME (field ID) Delta: cần column mapping Dropcolumn ∼ DROPCOLUMN OPTIMIZEphysical remove Typewiden (int →bigint) ✓ ALTERCOLUMN TYPE Compatiblecast Typenarrow(double →int) × —không cho phép DATALOSS Changepartition column ∼ Icebergpartition evolution Delta: rewrite Movecolumn position ✓ ALTERCOLUMN... AFTER Cosmetic,an toàn Patternan toàn: (1)Deploy reader code biết columnmới NULL-able→(2)Add column →(3)Backfill →(4)Update writer. Đảo thứtự=productionoutage. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 20 / 35

---

<!-- chiron-source-span: {"source_span_id":"e1bb9466-e9a0-5dde-925c-4f038d04a34c","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"MedallionArchitecture cho AI","extraction_method":"pdf-text-layer"},"checksum":"01c1d61e18d66a43071c14a65651f374a22f0a9e6b8a0aca4230d29a2c5c1cd3"} -->

## Slide 23 - MedallionArchitecture cho AI

Bronze Raw / Ingested Silver Cleaned / Validated Gold Aggregated / Feature-ready deduplicate,PII-scrub aggregate,feature eng. Raw LLM outputs User inputs (JSON) Synthetic data Deduplicated, validated PII removed Schema enforced Feature tables, metrics Doc chunks + embeddings RAG-ready datasets Streaming Ingestion RAGPipeline Embeddings MLTraining FeatureStore Giảngviên (VinUni) AICB· Ngày 18 Tuần4 21 / 35

---

<!-- chiron-source-span: {"source_span_id":"c205a0e4-c859-551f-8825-419e635da529","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Medallion: Schema Cụ Thể(LLM Observability)","extraction_method":"pdf-text-layer"},"checksum":"984f82302d4f0269a8beac15663c6cc986f2ab50fcdb0924264dce72096503e7"} -->

## Slide 24 - Medallion: Schema Cụ Thể(LLM Observability)

Layer Bronze(raw) Silver(clean) Gold(analytics) Schema request_id, ts, raw_json request_id, ts, model, prompt_tokens, completion_tokens, latency_ms, user_id, status date, model, p50/p95_latency, total_tokens, cost_usd, error_rate Cardinality 1row per LLM call 1row per call (validated) 1row per (date, model) Partition ingest_date date date(Z-ORDER model) Retention 30ngày 1năm 5năm Consumer Replay/ debug Featurestore, RAG corpus Dashboards,alerts, FinOps Quytắc: Bronzeappend-only (immutable audit), Silver upsert(MERGE), Gold rebuild-from-Silver (idempotent). Schemarõ ràng mỗi layer=datacontract giữa teams. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 22 / 35

---

<!-- chiron-source-span: {"source_span_id":"a0bbc4e1-7847-56ad-8bec-3ffce7a75361","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Lakehouse+ AI: Production Patterns","extraction_method":"pdf-text-layer"},"checksum":"9c9edc270bdeb45554e7dd5a5377a202926e4c04febc33d644891a46b31da9b7"} -->

## Slide 25 - Lakehouse+ AI: Production Patterns

- Raw →processed →model →deploy
versionchain

- RAG:doc chunks + embeddings lưuGold

- Embeddinggắn doc version=fullytraceable

- PinDelta version trong MLflow runcho
reproducibility

- S3Intelligent-Tieringcho cold Bronze data

- Glaciersau 90 ngày→ −60%storage cost

- Unity/Polaris: fine-grained access +audit

- Inferencereq/resp →Bronze(raw JSON,
30d)

- Dedup+ parse tokens/latency→Silver

- Aggregate(date, model) metrics→Gold

- LLMgenerate →Bronze(output + prompt)

- Qualityfilter + MinHash dedup→Silver

- Curatedset + license tags→Gold
Giảngviên (VinUni) AICB· Ngày 18 Tuần4 23 / 35

---

<!-- chiron-source-span: {"source_span_id":"0eb95711-0133-5ea6-addb-d5d44ede676c","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"CDCPattern: Postgres →Lakehouse","extraction_method":"pdf-text-layer"},"checksum":"d2815312f92416fb2b104226d3c2a925d1bb4b6f06e616c37d52258561bf8953"} -->

## Slide 26 - CDCPattern: Postgres →Lakehouse

Postgres MySQL Debezium WAL reader Kafka + Schema Reg. Hudi/Delta Streamer Bronze Table binlog/WAL Avromsg durablebuffer MERGEupsert Source DB CDC connector Decouple uptime Apply CDC Lakehouse

### 3 failure modes phổ biến
(1) Kafka full→ Postgres WAL fills→ DB outage.Fix: alert on Debezium lag + Kafka retention dài. (2) Source schema change breaks pipeline.Fix: Schema Registry +mergeSchema=true ở sink. (3) Out-of-order events tạo bad updates.Fix: MERGE... WHEN MATCHED AND src.ts > tgt.ts. Vietnamcontext: chuẩncho fintech VN (MoMo, VNPay,Cake) — Postgres OLTP→Iceberg/Deltaanalytics. End-to-endfreshness 1–5 phút, không impactOLTP. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 24 / 35

---

<!-- chiron-source-span: {"source_span_id":"fc010e45-e316-5a07-a7b2-be2787739494","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"CaseStudies: Lakehouse ởQuy Mô Production","extraction_method":"pdf-text-layer"},"checksum":"92f272c23a2c2f6d2ecc19f0450edba4b9f8d4ade3d63df094b43b8a04978d6e"} -->

## Slide 27 - CaseStudies: Lakehouse ởQuy Mô Production

Côngty Format & Scale Sốliệu công khai Uber Hudi· 350 PB 6T rows/day · 19,500 datasets· freshness 24h

- 1h
Netflix Iceberg+ Lance Atlasquery planning 9.6 min→42sec · Media DataLake multimodal Apple Iceberg “Foundationcho lakehouse on all divisions”(MB

- PB)
LinkedIn Iceberg MigrateHive →Icebergvì hidden partitioning + queryplanning Shopify Iceberg+ Trino Openlakehouse, multi-engine BI + ML

- Append-mostly(logs, events) →
Delta/Iceberg

- Mutation-heavy(orders, sessions) →Hudi

- Multimodal(video, embeddings) →Lance+
Iceberg

### MoMo,Zalo,ShopeeVN →TB–PB.Patternchuẩn
Postgres → Debezium → Kafka → Iceberg/MinIO. Decree13 →on-premMinIO khả thi. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 25 / 35

---

<!-- chiron-source-span: {"source_span_id":"72217fbe-5cf0-5231-94c5-17550ee863f1","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"FormatWar2024–2026: Đã Kết Thúc","extraction_method":"pdf-text-layer"},"checksum":"c5476abd86dd6d1c2ed1f24886c3c73358c78ddc359ad791f3f5a75bea7483ae"} -->

## Slide 28 - FormatWar2024–2026: Đã Kết Thúc

Delta Lake +UniForm Apache Iceberg v3 Apache Hudi UniForm XTable Key events:Databricks acquires Tabular $1B+ (2024) · Snowflake→ Iceberg native + Polaris catalog · Iceberg v3 GA on Databricks (Apr 2026): deletion vectors + row lineage + VARIANT · Result:30% giảm DE workload.

- AWSGlue (∼39%share) — default AWS

- UnityCatalog — Databricks OSS 2024

- ApachePolaris — top-level 2025

- ProjectNessie — git-like branching

- Lakekeeper— Rust, K8s-native
RESTCatalog spec =linguafranca 2026. nessie tag create v1-prod nessie branch create exp-2026 #...train + evaluate on branch... nessie merge → main

### “ModelXdùngdatanào?” → nessie tag list
trảlời 1 command, thay vìConfluence rotting. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 26 / 35

---

<!-- chiron-source-span: {"source_span_id":"ab90fe64-4452-5951-bce9-341c0097e336","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Lakehousecho AI/LLM Workloads","extraction_method":"pdf-text-layer"},"checksum":"7fee5e48e1d1840b6a7a4c44f207dee7e1bb8db65f6b3fdd162de8069f389651"} -->

## Slide 29 - Lakehousecho AI/LLM Workloads

RedPajama-V2: 30Ttokens · MinHashLSH dedup Dolma(Ai2): 3Ttokens · two-stage Bloom filter Pipeline: 64CPU cores, ∼1.4TB peak RAM Lakehouse: Bronze(raw) →Silver(dedup) →Gold (train-ready). Timetravelrevert dedup mistakes. Embedding version= doc_v × model_v → pin via Iceberg/Deltaversion + MLflowrun_id. Vector DB (Qdrant/Milvus) = derived index, re- buildable,không phải system of record.

- Randomaccess ∼2000×fasterthanParquet

- NativeHNSW vector index; first-class blobs

- Built-inversioning
Netflix Media Data Lake:Parquet → Lance cho videoframes.

- Iceberg/Delta →tabularfeatures + lineage

- Lance →embeddings+ multimodal blobs

- VectorDB →onlineANN (sub-100ms)
Bổtrợ, không thay thế nhau. AIThực Chiến VN:fine-tunecorpus (Wiki-VI + ZNews)→applyRedPajama-style MinHash trước. Repo: togethercomputer/RedPajama-Data. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 27 / 35

---

<!-- chiron-source-span: {"source_span_id":"8310cfc4-97e5-5992-be49-1488a3c626bb","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"CatalogLayer: REST Standard2026","extraction_method":"pdf-text-layer"},"checksum":"bd6921425712006808d805e98e8dcdb4160f888ff5fe158702d1716845c56ffb"} -->

## Slide 30 - CatalogLayer: REST Standard2026

Catalog Origin Killerfeature Khinào dùng AWSGlue AWS,2017 DefaultAWS, ∼39%share Đãở AWS UnityCatalog Databricks,OSS 2024 Fine-grainedgovernance Databricks-native ApachePolaris Snowflake,top-level 2025 Vendor-neutralREST Multi-cloud ProjectNessie Dremio,2020 Git-likebranching/tagging MLversioning Lakekeeper OSS2024 (Rust) Lightweight,K8s-native Self-hosted Standard HTTP API cho Iceberg metadata (cre- ateTable,loadTable,commit, listNamespaces). Lợi: engine (Spark, Trino, Flink, Snowflake, DuckDB)plug-and-playvớibấtkỳcatalogimplement spec. 2026 default. Catalog-levelcommit =atomicupdatenhiềutables. Use case:Bronze + Silver + Gold update phải all- or-nothing. Nessienative(gitcommit);Polarisđangimplement. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 28 / 35

---

<!-- chiron-source-span: {"source_span_id":"e0de02f9-aa84-5b59-896f-6a7a303fbd30","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"DataQuality & Contracts: 3-ToolStack","extraction_method":"pdf-text-layer"},"checksum":"fbeddcd8ff2b9a0a605b40b3e23cba6b57a39c76c36bb9023ee2566e71ffe596"} -->

## Slide 31 - DataQuality & Contracts: 3-ToolStack

Where: Bronzeingestion What: validateraw data Strength: 50+expectations expect_column_values_to_be_in_set( column="status", value_set=["ok", "rate_limited","error"]) Where: Silver/Goldtransforms What: structuralcorrectness Strength: SQL-native # schema.yml - name: customer_id

### tests
- unique
- not_null

### - relationships
to: ref('dim_customers') Where: Prodmonitoring What: continuous,anomaly Strength: SodaCLDSL

### checks for gold.metrics
- row_count >= 1000
- freshness < 1h
- anomaly_score
< 0.7 for cost_usd DataContract: schema+ constraints + freshness SLA+ ownership; run trong CI (pre-merge)vàruntime(per-batch). Bể contract →blockpipeline. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 29 / 35

---

<!-- chiron-source-span: {"source_span_id":"da76f390-f474-5b45-a983-659cb6e8bb14","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"DataLineage: OpenLineage +Marquez","extraction_method":"pdf-text-layer"},"checksum":"288c7149b7292e3a1f610e9859815d4fed6444bca99c3a98426b19340e085e75"} -->

## Slide 32 - DataLineage: OpenLineage +Marquez

Bronze.events Sparkjob clean+dedup Silver.events dbtmodel aggregate Gold.metrics Dashboard MLfeature OpenLineage: OSS standard — Spark/Airflow/dbt/Flink emit lineage events tự động.Mar- quez: reference server (graph DB + UI). Trả lời: “Drop column X→ ai bị ảnh hưởng?” · “Gold metric Y sai→ truy ngược về Bronze nào?” Pattern: bậtOpenLineage từngày1. Spark: spark.openlineage.transport.type=http +MarquezURL. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 30 / 35

---

<!-- chiron-source-span: {"source_span_id":"6011da1b-a4ea-5598-a750-fc0c048bace7","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Security& Governance cho Lakehouse","extraction_method":"pdf-text-layer"},"checksum":"b8a714fef5e3ad305886bab248d90347e597b9ce1036a2f1308ffaa4f4362848"} -->

## Slide 33 - Security& Governance cho Lakehouse

- RBAC:role-based(admin/analyst/eng)

- ABAC:attribute-based(region,
classification)— Unity/Polaris

- Row-levelsecurity: dynamicfilter

- Columnmasking: hash/redactPII

- TokenizePII at Bronze landing

- Encryptat field level (Iceberg v3native)

- Right-to-forget: DELETE + VACUUMsau
30dgrace

- Auditlog mọi PII column access

### Decree13/2023/NĐ-CP (eff. 2023-07-01)

- Personaldata: basic vssensitive

- Dataresidency: sensitive ởVN

- Cross-border: consent + DPI

- Right-to-forget: 72h SLA
Impact: sensitive data → on-prem MinIO + Ice- berg.

- Everyread/write →Bronzeaudit table

- Iceberg: system.snapshots table

- Retention365+ ngày cho regulated
Giảngviên (VinUni) AICB· Ngày 18 Tuần4 31 / 35

---

<!-- chiron-source-span: {"source_span_id":"84ae754c-94dd-59d8-bd78-e5390f76f348","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Cost& FinOps cho Lakehouse","extraction_method":"pdf-text-layer"},"checksum":"61f9ff05b6f0510dd7a1094e3a7e9481f3834734ef006bd45db48c53f65127d2"} -->

## Slide 34 - Cost& FinOps cho Lakehouse

Component(100 TB/tháng) Snowflake Iceberg+ Trino/ S3 Databricks Storage $4,000 $2,300(S3) $2,300(S3) Compute(BI) $15,000 $8,000(TrinoEC2) $11,000(DBU) Compute(ETL) $5,000 $2,000(Spark EMR) $4,000(DBU) Catalog/gov included $500(Polaris OSS) included(Unity) Total $24,000 $12,800(–47%) $17,300(–28%)

- Per-layerbudget: Bronze →Glaciersau 30d

- Auto-OPTIMIZEnightly cron

- Tagclusters: team, purpose,
expires_at

- Spotcho ETL, on-demand cho BI

- Top-10query review hàng tháng

- Cloudera: TPC-DS 24s→1.8s(13 ×),
storage −36%

- ClickHousevs Snowflake: ∼4×lowerTCO

- NetflixIceberg: planning9.6min →42s(14 ×)

- NoOPTIMIZE: 10×moreexpensivethan
DW Quytắc: savingschỉmaterializenếu actively optimize. Forget OPTIMIZE→small-filetax giết economics. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 32 / 35

---

<!-- chiron-source-span: {"source_span_id":"d120e85d-e96e-5f3a-928e-03948f4303e6","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Top5 Lakehouse Anti-Patterns","extraction_method":"pdf-text-layer"},"checksum":"780414733779ff10a0d4a1c664fc8b63e2c567fc1bd6c934b827edada2e48aa3"} -->

## Slide 35 - Top5 Lakehouse Anti-Patterns

# Anti-pattern Hậuquả & Fix 1 “Đổ tất cảvào S3” (raw JSON,no schema) Dataswamp →enforceschema từ Bronze; dùng Delta/Icebergngay từ đầu 2 Partition theo high-cardinality(vd. user_id) Triệupartition nhỏ →partitionby date/region, Z-ORDER user_id 3 Bỏ qua OPTIMIZE → small-fileproblem 10Kfiles ×1MB →query10 ×chậm →daily OPTIMIZEcron 4 VACUUM 0 HOURS để“tiết kiệmstorage” Mấttime travel + concurrent readersfail→giữtối thiểu168h (7 ngày,default) 5 Spark cluster choquery 5GB Lãngphí 10×chiphí →DuckDB/ Athena cho <100GB; chỉ scale-up khi>1node RAM 80%lakehouse pain trong production=mộttrong 5 anti-patterns này. Audit checklist trước khideploy. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 33 / 35

---

<!-- chiron-source-span: {"source_span_id":"490dd6ee-6264-5076-8def-d1ab5f50b7eb","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Demo: Delta Lake TimeTravel& MERGE","extraction_method":"pdf-text-layer"},"checksum":"582e30fa4c453a45a5d65a205dfd7b65cb1b872d848c12c993557f83b45c5565"} -->

## Slide 36 - Demo: Delta Lake TimeTravel& MERGE

- Small-fileproblem —ingest 1M rows (200 batches)→OPTIMIZE+ Z-ORDER →
benchmarktrước/sau (target ≥3×)

- Timetravel rollback—inject bad data→ restoreToVersion() trong30s vs ∼2h
manual

- MERGEupsert —100K rows (∼2×fasterworkshop; 10–50×productionscale)

- Audittrail — DESCRIBE HISTORY listmọi operation
Labrepo: VinUni-AI20k/Day18-AIInfrastructure-Lakehouse-Lab Notebooks01–04 + Docker stack hoặclightweight DuckDB + delta-rs path. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 34 / 35

---

<!-- chiron-source-span: {"source_span_id":"39b7f78a-1cfe-51d4-bf13-3a26978a5597","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"37af20ce7e54f43b41b4c7a617cdaad8b9a3dca854221f7da5d176adc4dc83f7"} -->

## Slide 37 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 Lakehouse = ACID + object storage + open formats. Foundation chung cho 3 era: Tradi- tional,ML, LLM. 2 Formatwarkếtthúc. Iceberg+DeltaUniForm=defactostandard. On-diskParquetidentical, chọntheo tooling fit. 3 Time travel + branching(Nessie) = “git checkout” cho dataset.OPTIMIZE + Z-ORDER + DeletionVectors bắtbuộc cho production. 4 LLMeracầnthêmtầng: VectorDB(RAG),Lance(multimodal),embeddingversioning,train- ingdata provenance. 5 Productionops trifecta: Catalog + DataContracts + Lineage. Bậttừ ngày 1. Giảngviên (VinUni) AICB· Ngày 18 Tuần4 34 / 35

---

<!-- chiron-source-span: {"source_span_id":"9eb00b3e-964b-5fb0-a4cc-698e89859266","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"a9a763d90a8fd386cd6ac3afda72516b1900c5baaabfeee1f2c9a2ceacea3063"} -->

## Slide 38 - Tiếptheo & Bài tập

Ngày 19: Vector Store & Feature Store “SQLtrảexactmatch. AIcầntươngtự —semantic search thay đổi mọi thứ.”

- Hoànthành Lab 18 (4
notebooks): VinUni-AI20k/ Day18-AIInfrastructure-Lakehouse-Lab

- Đọctrước: case studies(Netflix,
Uber,Apple Iceberg) + Lance multimodaldocs

- Càisẵn Docker + Qdrant image
choNgày 19 (VectorStore + ANN) Giảngviên (VinUni) AICB· Ngày 18 Tuần4 35 / 35

---

<!-- chiron-source-span: {"source_span_id":"f0904fce-9dd7-5f59-9518-17adbfd9795f","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"064bd5681cb55eaa2a5d7887451e6e72b60eccd6a6caf675ab51dc9fe6de2b15"} -->

## Slide 39 - Hỏi& Đáp

Câu hỏi về Lakehouse, Delta/Iceberg, Medallion, Catalog, Data Contracts, hay AI/LLM workloads?

---

<!-- chiron-source-span: {"source_span_id":"493b1e77-2df9-5444-97aa-abb8a4b8b18f","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"4ca93b6eb3316b7feba34c2effdb07d23fded9c1983b28aeba11b5d5942aac0a"} -->

## Slide 40 - Cảmơn!

AICB-P2T2 · Ngày 18 Data Lakehouse Architecture lms.vinuni.edu.vn · Lab repo + slides trên LMS
