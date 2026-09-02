---
schema_version: 1
course_id: rag-intensive
document_id: "a57659ed-0368-591d-9104-c74f2afc728d"
document_version_id: "0b722f91-c02b-5a23-be81-ec2e11e865c7"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Disaster Recovery & High Avail"
source_file: "track 2 - day 23.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 23.pdf"
source_sha256: "0233e3b8969055c62983dba1847b8683a97f5a1c45f28b33c9ef0f5d08c494de"
parser_version: chiron-structured-markdown-v1
page_count: 42
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":42}"
language: vi
---

# Disaster Recovery & High Avail

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"502b7ab5-174c-5350-a1ec-1cf7f0a1f61e","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Disaster Recovery & High Avail","extraction_method":"pdf-text-layer"},"checksum":"687ede83513f5360570d8b0d85a4fad5ac84d7bff49b0676404d9f145d83b5d7"} -->

## Slide 1 - Disaster Recovery & High Avail

Disaster Recovery & High Avail- ability cho AI Infrastructure AICB-P2T2 · Ngày 23 · Chương 5: Vận Hành Giảng viên VinUniversity · Phase 2 · Track 2 · T uần 5

---

<!-- chiron-source-span: {"source_span_id":"7ce6715b-9d36-5108-b9fd-8dfa49ead16d","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"5b2d96e6ad4e6acfeaaf9d8162116223007fe3e41f362a8d31ce653a1bd05463"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “us-east-1 vừa sập. Model serving end- point của bạn nằm ở đó. Bạn có bao nhiêu phút trước khi khách hàng nhận ra? Và quan trọng hơn — bạn có biết câu trả lời trước khi nó xảy ra không?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"95ceb063-e7ef-54f3-bd9a-73e8e135e00f","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"8aa5ec95613826ca38b9f0d97faa0f4de046eb9f0481c56ade511971a717dcb8"} -->

## Slide 3 - Nội Dung Bài Học

1. RTO/RPO cho AI Systems

2. Multi-Region Deployment Patterns

3. Stateful Component Recovery

4. Failover Automation & Runbooks

5. Chi Phí Standby Capacity

6. DR Drills & Game Days Giảng viên (VinUni) AICB · Ngày 23 T uần 5 1 / 31

---

<!-- chiron-source-span: {"source_span_id":"8a28cae2-a16d-574b-9267-457777c54288","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu","extraction_method":"pdf-text-layer"},"checksum":"da6ca0ef34d88367d2fa6151a2d1e2de069a0035739a759edbc3be7a82378b82"} -->

## Slide 4 - Mục Tiêu

### Sau buổi học này, bạn sẽ

1. Định nghĩa RTO/RPO cho từng thành phần trong AI stack (serving, vector DB, feature store)

2. Thiết kế kiến trúc multi-region active-passive / active-active cho inference

3. Lập kế hoạch backup & replication cho state (model weights, vector DB, metadata)

4. Viết runbook failover và chạy được một DR drill có đo RTO thực tế Agenda hôm nay RTO/RPO fundamentals→ Multi-region patterns→ State recovery→ Failover automation → Cost tradeoffs → Game day demo Giảng viên (VinUni) AICB · Ngày 23 T uần 5 2 / 31

---

<!-- chiron-source-span: {"source_span_id":"28f61956-0d35-58e9-8fd5-463b60917b04","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"49b2a1b88b511b666f55e7d204ab9f0204aaca7cb5584b1cd3d5199e878ccbfb"} -->

## Slide 5 - Deliverable Cuối Ngày

Artifact cần nộp DR runbook + failover demo có đo RTO thực tế + cost tradeoff analysis

- RTO/RPO table cho 4 component chính của hệ thống bạn đang xây (serving,
vector DB, feature store, metadata store)

- Terraform snippet: cross-region S3 replication cho model weights

- Runbook 1 trang: các bước failover khi region chính down

- Kết quả DR drill: RTO đo được vs RTO mục tiêu, và gap nếu có
Giảng viên (VinUni) AICB · Ngày 23 T uần 5 3 / 31

---

<!-- chiron-source-span: {"source_span_id":"b39b4d64-7cba-5ea2-be4d-2b8fcc676ac1","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"RTO/RPO cho AI Systems","extraction_method":"pdf-text-layer"},"checksum":"824b71f0a6ef452920740b69cd41cc4a48399d48f999163d2863ea494bc35795"} -->

## Slide 6 - RTO/RPO cho AI Systems

01 Vì sao AI infrastructure ”sập” khác với web app thường, và cách đo mức độ chịu đựng downtime

---

<!-- chiron-source-span: {"source_span_id":"0006fcfa-2936-575b-8da5-19ac113c52ef","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"AI Infra Khác Web App Thường Ở Đâu?","extraction_method":"pdf-text-layer"},"checksum":"3cafacf950e800abcb19336f40d98d9a214a4622f83141ba51a0a2ddeadc96b0"} -->

## Slide 7 - AI Infra Khác Web App Thường Ở Đâu?

Thành phần Web app thường AI system State cần khôi phục DB rows (KB–GB) Model weights (GB–TB) Thời gian ”khởi động lại” Vài giây Cold-start GPU pool: 5–15 phút Dữ liệu ”tươi” quan trọng Transaction log Vector DB embeddings + fea- ture store freshness Chi phí standby Rẻ (CPU instance) Đắt (GPU instance đứng chờ) Hệ quả: DR cho AI không thể copy-paste playbook từ web app — phải tính riêng chi phí GPU standby và thời gian nạp lại state. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 4 / 31

---

<!-- chiron-source-span: {"source_span_id":"24b7bce1-5914-5241-a268-bfeb0a75a3cf","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Case Study: Khi Một Region Sập Thật","extraction_method":"pdf-text-layer"},"checksum":"e3346f8e50ebd54566d801b72e38e6161d19152fa76c16f3b0068c6aad79d056"} -->

## Slide 8 - Case Study: Khi Một Region Sập Thật

AWS us-east-1, Dec 2021 Sự cố network internal khiến us-east-1 gián đoạn ∼7 giờ. Nhiều công ty AI/SaaS chạy inference tại đây bị downtime toàn phần vì không có region phụ hoặc có nhưng chưa test failover bao giờ.

### Điều đã xảy ra

- Dashboard/monitoring cũng host ở cùng region

- không biết mình đang sập

- DNS failover có sẵn nhưng chưa test → cutover
thất bại lần đầu

### Bài học cho AI infra

- Observability stack phải sống ở region khác với
workload nó theo dõi

- ”Có DR plan” và ”DR plan hoạt động” là hai việc
khác nhau Giảng viên (VinUni) AICB · Ngày 23 T uần 5 5 / 31

---

<!-- chiron-source-span: {"source_span_id":"5690dec7-6e1c-54cd-94e4-b9699155b2b9","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"RTO vs RPO — Hai Câu Hỏi Sống Còn","extraction_method":"pdf-text-layer"},"checksum":"ebf92988c3071969be12fddf2e00c243fd5e0304f1918f7892e1d14cd06ab3d4"} -->

## Slide 9 - RTO vs RPO — Hai Câu Hỏi Sống Còn

RTO — Recovery Time Objective ”Tối đa bao lâu được downtime?”

- Đo từ lúc outage bắt đầu → lúc service
phục vụ lại

- Model serving: RTO thường 5–15 phút
(SLA khách hàng)

- Training pipeline: RTO có thể vài giờ
(không real-time) RPO — Recovery Point Objective ”Tối đa mất bao nhiêu dữ liệu?”

- Đo khoảng cách giữa backup gần nhất
và lúc sập

- Vector DB: RPO vài phút (embeddings
mới liên tục ingest)

- Model registry: RPO có thể vài giờ
(model ít thay đổi) Nguyên tắc: RTO/RPO càng thấp → chi phí infra càng cao. Không có ”một RTO cho tất cả” — mỗi component cần số riêng. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 6 / 31

---

<!-- chiron-source-span: {"source_span_id":"8085d514-0f8e-5249-8bbf-165914b9d280","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"RTO/RPO Theo Từng Component","extraction_method":"pdf-text-layer"},"checksum":"d4e9e9a5af60f49166847f108ea6e77114fe9908d55228b659c29a91cd786da0"} -->

## Slide 10 - RTO/RPO Theo Từng Component

Component RTO RPO Lý do Inference API (serv- ing) 5 phút N/A (stateless) User-facing, SLA nghiêm ngặt Vector DB 15 phút 5 phút Cần fresh embeddings, nhưng replica có thể lag nhẹ Feature store 30 phút 15 phút Batch features chấp nhận lag lớn hơn Model registry / weights 1 giờ 24 giờ Model ít thay đổi giữa các lần train Số liệu minh hoạ — điều chỉnh theo SLA thực tế của hệ thống bạn Giảng viên (VinUni) AICB · Ngày 23 T uần 5 7 / 31

---

<!-- chiron-source-span: {"source_span_id":"249eb37e-bd96-5783-9b16-e56f33c07f07","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Availability Tiers — “9” Nào Là Đủ?","extraction_method":"pdf-text-layer"},"checksum":"84cccd22e2f2bf82d40d8d09be7f86cdea5638353e80de264a3bae4d252ddf8b"} -->

## Slide 11 - Availability Tiers — “9” Nào Là Đủ?

SLA Downtime/năm Y êu cầu kiến trúc Chi phí 99% 3.65 ngày Single region, backup định kỳ Thấp 99.9% 8.76 giờ Multi-AZ, automated failover Trung bình 99.95% 4.38 giờ Multi-AZ + warm standby re- gion Cao 99.99% 52.6 phút Active-active multi-region Rất cao Lưu ý: Đừng thiết kế cho 99.99% nếu SLA thực tế chỉ cần 99.9% — chi phí GPU standby tăng phi tuyến theo mỗi “9” thêm. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 8 / 31

---

<!-- chiron-source-span: {"source_span_id":"07f4de85-d14b-5052-8caa-da9c50dd93d7","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Multi-Region Deployment Pat","extraction_method":"pdf-text-layer"},"checksum":"a0f8c39a2ad3834d1971f8ffc94ecd641e16e8b54ce6e622078119e12dc1c89d"} -->

## Slide 12 - Multi-Region Deployment Pat

02 Multi-Region Deployment Pat- terns Active-passive, active-active, và cách route traffic khi một region không còn phản hồi

---

<!-- chiron-source-span: {"source_span_id":"cafdace3-c70f-5948-968c-0938cef81589","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Active-Passive vs Active-Active","extraction_method":"pdf-text-layer"},"checksum":"d5228cdbda2a41a39623190152db4f1ae6e1208723f64f69fedfa0667726b4c6"} -->

## Slide 13 - Active-Passive vs Active-Active

Active-Passive Region A ACTIVE — 100% Region B ST ANDBY — 0% replicate Active-Active Region C 50% traffic Region D 50% traffic sync Rẻ hơn, đơn giản hơn Failover mất vài phút (DNS cutover) RTO ≈ 0, nhưng đắt gấp đôi Cần conflict res- olution cho state Giảng viên (VinUni) AICB · Ngày 23 T uần 5 9 / 31

---

<!-- chiron-source-span: {"source_span_id":"5a20adb3-ab27-5074-ab6a-9e0474524b57","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Latency-Based Routing & DNS Failover","extraction_method":"pdf-text-layer"},"checksum":"80fd2f9955d205147b3c2635317db8c4660e20c88c5ad18fee0e74151676a622"} -->

## Slide 14 - Latency-Based Routing & DNS Failover

Route53 / Cloud DNS Health Check

- Health check endpoint mỗi 10–30s

- 3 lần fail liên tiếp → mark unhealthy

- DNS record TTL thấp (60s) để cutover
nhanh

- Latency-based routing: route đến region
gần nhất, tự động loại region unhealthy Giới hạn thực tế của DNS failover

- DNS cache ở client/ISP không tôn trọng
TTL → vài user vẫn miss

- Không phải ”tức thì” — cộng thêm
30–90s vào RTO

- Kết hợp với global load balancer
(Cloudflare/Anycast) để cutover nhanh hơn DNS thuần Giảng viên (VinUni) AICB · Ngày 23 T uần 5 10 / 31

---

<!-- chiron-source-span: {"source_span_id":"1cd22e46-e8bf-5a82-bf17-8684d5a91014","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Cross-Region Model Weight Replication","extraction_method":"pdf-text-layer"},"checksum":"28e2b4c580188f5a764194f093411cf82d2627dadc0523e84363b12bd560b73f"} -->

## Slide 15 - Cross-Region Model Weight Replication

# terraform: S3 Cross-Region Replication resource "aws_s3_bucket_replication_configuration" "

```text
weights" {
bucket = aws_s3_bucket.model_weights_primary.id
role = aws_iam_role.replication.arn
rule {
id = "replicate-to-standby-region"
status = "Enabled"
destination {
bucket = aws_s3_bucket.model_weights_dr.arn
storage_class = "STANDARD"
}
filter {
prefix = "checkpoints/"
}
}
}
```
Lưu ý khi replicate weights

- CRR có lag — không dùng cho RPO <
1 phút

- Checksum verify sau replicate
(model corrupt = silent failure)

- Versioning bucket bắt buộc —
rollback về checkpoint cũ Chi phí

- CRR: phí transfer + storage nhân đôi

- Model 70B fp16 ≈ 140GB → tính phí
egress kỹ trước khi bật CRR toàn bộ Giảng viên (VinUni) AICB · Ngày 23 T uần 5 11 / 31

---

<!-- chiron-source-span: {"source_span_id":"f03c5d51-41d0-57a8-81d6-12380bfa0eb0","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Active-Passive vs Active-Active — Khi Nào Dùng Gì?","extraction_method":"pdf-text-layer"},"checksum":"1176f0d1e15f2d59c7c52721dc475daf4cc8748c3002c603b6c90397adc0a2ed"} -->

## Slide 16 - Active-Passive vs Active-Active — Khi Nào Dùng Gì?

Active-Passive

- RTO mục tiêu > 5 phút chấp nhận được

- Budget GPU hạn chế — không đủ chạy 2
pool full-time

- State ít conflict (không cần
multi-master)

- Phù hợp: hầu hết AI startup / team vừa
Active-Active

- RTO mục tiêu ≈ 0 (fintech, healthcare
real-time)

- Budget cho phép double GPU capacity

- Có chiến lược conflict resolution cho
vector DB / feature store

- Phù hợp: enterprise SLA 99.99%+
Giảng viên (VinUni) AICB · Ngày 23 T uần 5 12 / 31

---

<!-- chiron-source-span: {"source_span_id":"4819eed3-dbcd-5449-a6ea-ef5eab4c77b7","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Kiến Trúc Tham Chiếu — Ghép T oàn Bộ Section Lại","extraction_method":"pdf-text-layer"},"checksum":"45ed1105aa32c48597a8e29e7f1c2c8e4ce912e3f91512778356b2f0ebc58c4a"} -->

## Slide 17 - Kiến Trúc Tham Chiếu — Ghép T oàn Bộ Section Lại

Global DNS / LB health check 15s Region A — ACTIVE Serving + Vector DB Region B — ST ANDBY Warm GPU pool S3 CRR: model weights + vector DB snapshot Postgres PITR (registry + metadata) failover Điểm mấu chốt: DNS/LB, compute, và state (S3 + Postgres) là 3 lớp cần replicate riêng — thiếu 1 lớp là failover không hoàn chỉnh. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 13 / 31

---

<!-- chiron-source-span: {"source_span_id":"9ca0edf7-ab36-5736-8eb5-be1d6a77aa82","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Stateful Component Recovery","extraction_method":"pdf-text-layer"},"checksum":"ee966ba0e8fe5de1f5c63103e0e745c13f4f36168e96ea9fa5aae9dd4dfa417a"} -->

## Slide 18 - Stateful Component Recovery

03 Backup và replication cho phần khó nhất: vector DB, model registry, và metadata store

---

<!-- chiron-source-span: {"source_span_id":"3fdf33a7-00d8-5ac2-b70f-19afd6ea42f1","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Vector DB Backup & Multi-Region Replica","extraction_method":"pdf-text-layer"},"checksum":"f61cdbcb214ef1d43f8c5af571d82ce6fb05d12fb2c4d57c7b7a5feefdcc0c11"} -->

## Slide 19 - Vector DB Backup & Multi-Region Replica

Pinecone / Weaviate multi-region

- Pinecone: replica pod ở region khác,
sync gần real-time

- Weaviate: backup snapshot → S3/GCS,
restore vào cluster mới

- Self-hosted (Qdrant/Milvus): snapshot
định kỳ + WAL shipping Điều dễ bị bỏ quên

- Re-index từ raw documents luôn là
fallback — nhưng chậm (giờ, không phải phút)

- Backup index nhưng quên backup
embedding model version → index không tương thích khi restore

- Test restore định kỳ — backup chưa test
= không có backup Giảng viên (VinUni) AICB · Ngày 23 T uần 5 14 / 31

---

<!-- chiron-source-span: {"source_span_id":"ebb5bf2f-8afc-5937-93bb-1d5ebd163b34","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Model Registry & Checkpoint Recovery","extraction_method":"pdf-text-layer"},"checksum":"5984f2bd62516542708d3acb20031a406b635d3833e0cb2047ebd66d7ea213dc"} -->

## Slide 20 - Model Registry & Checkpoint Recovery

MLflow Model Registry S3 Primary Region S3 DR Region CRR replica async replicate DR Region: registry metadata (Postgres) restore từ snapshot → point vào S3 DR bucket Nguyên tắc Registry metadata (Postgres/RDS) và model artifacts (S3) phải backupđồng bộ — registry point đến path không tồn tại là lỗi phổ biến nhất khi restore. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 15 / 31

---

<!-- chiron-source-span: {"source_span_id":"81efcb0f-96ab-50c7-a7fe-3d0081b29842","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"PITR cho Metadata Store","extraction_method":"pdf-text-layer"},"checksum":"83cb89e19ec54dfd3f98cb054268bb747c73dfda5592dbe1faef196e96dd3510"} -->

## Slide 21 - PITR cho Metadata Store

Point-in-Time Recovery

- RDS/Aurora: continuous backup +
transaction log → restore về bất kỳ giây nào trong 35 ngày

- Dùng cho: feature registry, experiment
tracking DB, model registry metadata

- Restore tạo instance mới — không
overwrite instance đang chạy Khi nào PITR không đủ

- Cross-region: PITR restore trong cùng
region — cần thêm cross-region read replica cho DR thật

- Logical corruption (bad migration) vẫn
replicate sang DR nếu dùng sync replica — cần backup point-in-time riêng, không chỉ replica Giảng viên (VinUni) AICB · Ngày 23 T uần 5 16 / 31

---

<!-- chiron-source-span: {"source_span_id":"2deb9083-7345-56bc-bc4e-fff47a829cc2","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Backup Schedule Cheatsheet","extraction_method":"pdf-text-layer"},"checksum":"7b6016a2822d3c8efd627df0b4e9fc78cbc196eeeb696a95633286254ac49f43"} -->

## Slide 22 - Backup Schedule Cheatsheet

Component Phương pháp T ần suất Retention Model weights S3 CRR + versioning Continuous 90 ngày Vector DB Snapshot → S3 Mỗi 6 giờ 30 ngày Metadata (Postgres) PITR + cross-region replica Continuous 35 ngày Feature store (offline) Table snapshot Hàng ngày 14 ngày Điều chỉnh tần suất theo RPO mục tiêu của từng component Giảng viên (VinUni) AICB · Ngày 23 T uần 5 17 / 31

---

<!-- chiron-source-span: {"source_span_id":"87f09305-f85c-5940-a42b-97a332fbddb7","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Failover Automation & Run","extraction_method":"pdf-text-layer"},"checksum":"49b6f6d67356efe988ec7d7c9ad4393c1dfa9bf70578c7fdb25c608f787c5fc5"} -->

## Slide 23 - Failover Automation & Run

04 Failover Automation & Run- books T ừ health-check đến DNS cutover đến GPU pool ấm sẵn ở region phụ

---

<!-- chiron-source-span: {"source_span_id":"35662147-88c9-59d0-9cc9-45d167f0c8c8","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Kiến Trúc Health-Check-Based Failover","extraction_method":"pdf-text-layer"},"checksum":"097d70412fa0ae88b424e2f5b50a1b38cd9b943a4b75b24cae4af2c4f2e45fa5"} -->

## Slide 24 - Kiến Trúc Health-Check-Based Failover

Health Checker mỗi 15s DNS / Global LB Region chính serving Region phụ warm standby PagerDuty / Slack: alert on-call + trigger runbook cutover Nguyên tắc: failover đầu tiên nên là bán tự động (alert + 1-click confirm), không full-auto — tránh flapping gây failover 2 chiều liên tục. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 18 / 31

---

<!-- chiron-source-span: {"source_span_id":"92dcd33d-502e-52b3-a6bd-df0dbe6305ec","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"GPU Pool Warm-Up Ở Region Phụ","extraction_method":"pdf-text-layer"},"checksum":"68c6b723804b0641e239f4c34076c3e5d9f392ec443463fd1f196bc863ee66f9"} -->

## Slide 25 - GPU Pool Warm-Up Ở Region Phụ

Vấn đề: Cold GPU = RTO chết

- Provision GPU instance mới: 3–8 phút

- Pull image + load model weights: thêm
2–10 phút

- Tổng cold-start có thể vượt RTO mục
tiêu Giải pháp: Warm standby

- Karpenter/NAP (đã học Ngày 16) giữ sẵn
1–2 node GPU “ấm” ở region phụ, scale 0→N khi failover

- Model weights pre-loaded vào node
cache, không load từ S3 lúc failover

- Trade-off: chi phí node ấm vs RTO — xem
Phần 5 Giảng viên (VinUni) AICB · Ngày 23 T uần 5 19 / 31

---

<!-- chiron-source-span: {"source_span_id":"ce5180a0-edec-5faf-8fd1-f57ea58bb150","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Runbook: Region Chính Down","extraction_method":"pdf-text-layer"},"checksum":"37253d147cd3f76d5495077913c30265e92bad0de43271e75fd0249c8f552571"} -->

## Slide 26 - Runbook: Region Chính Down

- ✓ Xác nhận outage: health check + status page của cloud provider

- ✓ Thông báo incident channel + bắt đầu tính RTO clock

- ✓ Scale GPU pool ở region phụ từ warm → full capacity

- ✓ Verify model weights + vector DB replica ở region phụ đã sync gần nhất

- ✓ DNS/LB cutover traffic sang region phụ

- ✓ Verify golden signals (latency, error rate) ở region phụ ổn định

- Post-incident: đo RTO thực tế, so với mục tiêu, viết postmortem
Giảng viên (VinUni) AICB · Ngày 23 T uần 5 20 / 31

---

<!-- chiron-source-span: {"source_span_id":"d3336946-3284-5749-8aac-779182ae34ee","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Anti-Patterns Thường Gặp","extraction_method":"pdf-text-layer"},"checksum":"fe98c8750cd75094afb4f752cb501538afaa83bfb557fac3748481a5939ac6fa"} -->

## Slide 27 - Anti-Patterns Thường Gặp

Lưu ý: Runbook chỉ tồn tại trên giấy — chưa test lần nào → 90% khả năng sai bước khi thực thi lúc hoảng loạn. Lưu ý: Failover tự động không có circuit breaker— 2 region flap qua lại liên tục khi health check không ổn định (flapping). Lưu ý: Backup DR region cùng account/cùng credentials — một sự cố IAM/billing đánh sập cả 2 re- gion cùng lúc. Lưu ý: Không ai biết RTO thực tế — chỉ có số ”lý thuyết” trên slide, chưa đo lần nào bằng drill thật. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 21 / 31

---

<!-- chiron-source-span: {"source_span_id":"2eb4cb86-f61e-533a-ad19-587754505779","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Sau Failover: Blameless Postmortem","extraction_method":"pdf-text-layer"},"checksum":"4fe53260ba7755da6b755f7bc653a438d66e06bd50196661d3091b817c840a87"} -->

## Slide 28 - Sau Failover: Blameless Postmortem

T emplate postmortem

1. Timeline: outage bắt đầu, phát hiện, alert, cutover, resolved

2. RTO đo được vs mục tiêu — gap ở bước nào?

3. Root cause (5 whys) — không đổ lỗi cá nhân

4. Action items có owner + deadline cụ thể Blameless — vì sao quan trọng

- Đổ lỗi cá nhân → lần sau người ta giấu lỗi
thay vì báo cáo sớm

- Câu hỏi đúng: ”hệ thống/process nào
cho phép lỗi này xảy ra?”

- Postmortem tốt → input trực tiếp để sửa
runbook Giảng viên (VinUni) AICB · Ngày 23 T uần 5 22 / 31

---

<!-- chiron-source-span: {"source_span_id":"db992da4-e8e2-5133-aa4e-51011666854f","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Chi Phí Standby Capacity","extraction_method":"pdf-text-layer"},"checksum":"c803db8218578728ad27b879c223eb0b3f738f4ed7ea56ced7dd792bbbb731cf"} -->

## Slide 29 - Chi Phí Standby Capacity

05 RTO thấp luôn đắt — câu hỏi là đắt bao nhiêu, và có đáng không

---

<!-- chiron-source-span: {"source_span_id":"178c7bf3-7d43-51d3-8d24-b2c0cda8bbf7","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Warm vs Cold vs Pilot-Light","extraction_method":"pdf-text-layer"},"checksum":"83115fd44281a5d3124ec5debb1e522247407602ef7221bf9f4d0ba35859e393"} -->

## Slide 30 - Warm vs Cold vs Pilot-Light

Chiến lược Mô tả RTO Chi phí GPU Cold Provision từ đầu khi failover 15–30 phút 1x (chỉ region chính) Pilot-light Giữ metadata/config, scale GPU khi cần 8–15 phút 1.1x Warm standby 1–2 node GPU ấm sẵn, scale nhanh 3–8 phút 1.3–1.5x Hot (active- active) Full capacity 2 region song song ≈ 0 2x Cost tương đối — Cold = 1x baseline Giảng viên (VinUni) AICB · Ngày 23 T uần 5 23 / 31

---

<!-- chiron-source-span: {"source_span_id":"ab818be7-e981-567a-bb18-b3fdd6bf80c3","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Decision Framework: Chọn Chiến Lược Nào?","extraction_method":"pdf-text-layer"},"checksum":"2e832d8b21b38e912795fe40d2439a9887dfce6756c6f15f3955c4ae5b43a1cb"} -->

## Slide 31 - Decision Framework: Chọn Chiến Lược Nào?

RTO mục tiêu < 5 phút? Có → Warm/Hot standby Không → tiếp câu hỏi Chấp nhận 15–30 phút downtime? Có → Cold / Pilot-light Không → tính lại budget, hoặc giảm SLA Câu hỏi thật: không phải ”RTO tốt nhất có thể” mà là ”RTO nào đủ, với chi phí công ty chấp nhận được”. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 24 / 31

---

<!-- chiron-source-span: {"source_span_id":"681bae04-779c-5228-bced-94bb2d142417","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"DR Drills & Game Days","extraction_method":"pdf-text-layer"},"checksum":"45e17a45d62470aefbd657c5bb94e6a2644b329ce81698abdf91413f1f17c0ef"} -->

## Slide 32 - DR Drills & Game Days

06 Cách duy nhất để biết RTO thật: mô phỏng outage và bấm giờ

---

<!-- chiron-source-span: {"source_span_id":"0a518788-ac67-5df7-965c-d2d80e5d34c5","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Game Day — T ại Sao Phải Diễn T ập?","extraction_method":"pdf-text-layer"},"checksum":"0f0d965afb29a691ba4885e7c00ad77767d7c811b44d0cefccbcf8f7df3da78f"} -->

## Slide 33 - Game Day — T ại Sao Phải Diễn T ập?

Sự thật khó chịu

- Runbook chưa test = giả định, không phải
sự thật

- RTO ”trên giấy” thường thấp hơn RTO
thật 2–3 lần

- Backup chưa test restore = có thể không
dùng được lúc cần Game day làm gì

- Chủ động tạo outage có kiểm soát
(không phải chờ outage thật)

- Đo RTO/RPO thực tế, so với mục tiêu

- Tìm gap trong runbook trước khi khách
hàng tìm ra Giảng viên (VinUni) AICB · Ngày 23 T uần 5 25 / 31

---

<!-- chiron-source-span: {"source_span_id":"c12c19df-df05-50e6-8b35-a29493e4621b","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Game Day — Quy Trình 4 Bước","extraction_method":"pdf-text-layer"},"checksum":"8ab28cd38fc6853e052fff8615573984f45030652541bd2adbfd81613c7d0844"} -->

## Slide 34 - Game Day — Quy Trình 4 Bước

1 Lên kế hoạch 2 Thông báo team 3 Kích hoạt outage giả 4 Đo & rút kinh nghiệm Giảng viên (VinUni) AICB · Ngày 23 T uần 5 26 / 31

---

<!-- chiron-source-span: {"source_span_id":"6bef8c4b-1dab-5f05-952c-242835b430cb","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Chaos Engineering Nhẹ Cho AI Infra","extraction_method":"pdf-text-layer"},"checksum":"bbac0c7fb068197293fa928460f078ce54c8d52a22669e47e7a63542f19e5aad"} -->

## Slide 35 - Chaos Engineering Nhẹ Cho AI Infra

Fault injection mức thấp rủi ro

- Kill 1 pod GPU serving — verify HPA/K8s
tự phục hồi

- Inject latency vào vector DB call — verify
timeout + fallback hoạt động

- Block network đến region chính (chaos
mesh) — verify DNS failover Nguyên tắc an toàn

- Luôn chạy ở staging trước, production
sau khi tự tin

- Có ”kill switch” dừng thí nghiệm ngay lập
tức

- Thông báo trước cho on-call — game
day không phải bất ngờ với người trực Giảng viên (VinUni) AICB · Ngày 23 T uần 5 27 / 31

---

<!-- chiron-source-span: {"source_span_id":"5cc13f4e-710d-5546-bff5-47a256e04350","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"DR Maturity Model — Bạn Đang Ở Đâu?","extraction_method":"pdf-text-layer"},"checksum":"b476570af0f3244e63f8ab33fa229a637eb8767212c55720f3a0ea28ea402f1c"} -->

## Slide 36 - DR Maturity Model — Bạn Đang Ở Đâu?

Level T ên Đặc điểm 0 Không có plan Backup thủ công, không ai biết RTO thật 1 Runbook viết sẵn Có tài liệu nhưng chưa test lần nào 2 Failover tự động một phần Health check + DNS cutover, cần người bấm con- firm 3 Test định kỳ (game day) Chạy DR drill hàng quý, đo RTO thực tế, cập nhật runbook 4 Chaos-engineered Fault injection thường xuyên, failover không cần con người can thiệp Mục tiêu thực tế cho hầu hết team: Level 2–3 — Level 4 chỉ đáng đầu tư khi SLA yêu cầu 99.99%+. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 28 / 31

---

<!-- chiron-source-span: {"source_span_id":"a3d17632-1805-5518-9677-ae5a73a3daf2","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Live Demo: Region Failover Drill","extraction_method":"pdf-text-layer"},"checksum":"475a4048de864b5418eddebd9e17c9614fad534ad864a30b8d99fe973d8b2124"} -->

## Slide 37 - Live Demo: Region Failover Drill

LIVE DEMO

1. Setup: 2 region (staging), model serving + vector DB replica ở cả hai

2. Trigger: chặn traffic đến region chính (simulate outage) — bắt đầu bấm giờ RTO

3. Quan sát: health check phát hiện fail → alert → DNS cutover

4. Verify: request mới được serve từ region phụ, latency/error rate ổn định

5. Kết quả: so RTO đo được với RTO mục tiêu (5 phút) — ghi lại gap Giảng viên (VinUni) AICB · Ngày 23 T uần 5 29 / 31

---

<!-- chiron-source-span: {"source_span_id":"b79044af-9712-5d00-b203-e5d0613b6d8a","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Lab #23","extraction_method":"pdf-text-layer"},"checksum":"911582a9eb90a9c454c45272294e2e903eaeb4f252f58af3212865bc10378fd3"} -->

## Slide 38 - Lab #23

LAB #23 Mục tiêu: Thiết kế RTO/RPO table cho hệ thống đang xây, viết Terraform cross-region replication cho model weights, và chạy 1 DR drill đo RTO thực tế Deliverable: RTO/RPO table + Terraform snippet + runbook 1 trang + kết quả drill (RTO đo được vs mục tiêu) Thời gian: 2h Giảng viên (VinUni) AICB · Ngày 23 T uần 5 30 / 31

---

<!-- chiron-source-span: {"source_span_id":"7d371680-d469-54bf-aa29-96072b738185","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"ded510f9e646fde46927e2acf9f8680d1e1564ac50bb8e2421154766116f8475"} -->

## Slide 39 - T ổng kết — Key T akeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 RTO/RPO phải định nghĩa riêng cho từng component — không có ”một số cho tất cả”, và AI infra có state nặng hơn (model weights, vector DB) so với web app thường. 2 Active-passive đủ cho hầu hết trường hợp; active-active chỉ đáng chi phí gấp đôi khi RTO mục tiêu thật sự cần ≈ 0. 3 Runbook chưa test qua game day = giả định, không phải kế hoạch — RTO thật chỉ biết được sau khi đo, không phải sau khi viết. Giảng viên (VinUni) AICB · Ngày 23 T uần 5 30 / 31

---

<!-- chiron-source-span: {"source_span_id":"779d7f2d-df86-50ec-aef6-95e4caeee54b","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"c92fffa7e099704afbf2507d15a7bafbdd444fbacd50e8298d6cd6e00fd8b212"} -->

## Slide 40 - Tiếp theo & Bài tập

Bài tiếp theo Ngày 24: Data Governance & Security “RBAC, encryption, PII han- dling, compliance (GDPR/ISO 27001/NĐ13) — bảo vệ data nhạy cảm trong AI pipeline” Bài tập về nhà

- Hoàn thành Lab 23: DR
Runbook + Failover Drill

- Review lại RTO/RPO table đã
làm — mang vào buổi sau để đối chiếu với governance requirements

- Đọc trước: Vietnam Decree
13/2023 về bảo vệ dữ liệu cá nhân Giảng viên (VinUni) AICB · Ngày 23 T uần 5 31 / 31

---

<!-- chiron-source-span: {"source_span_id":"b3fc4c0c-8f6b-57ff-9a4a-0f3a6cde0e99","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"65af3fe67dbfe67b6c09e45878c8a5bb769567a4c7f16f1118a69f90b20bb062"} -->

## Slide 41 - Hỏi & Đáp

Câu hỏi nào về RTO/RPO, multi- region, state recovery, hay DR drills?

---

<!-- chiron-source-span: {"source_span_id":"d5935f28-8a77-5c47-b956-978bca64ce0e","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"104a5effb0e4cf1634ead5cd1a1f596c95005954d3173394a3bc91b7f8add4e1"} -->

## Slide 42 - Cảm ơn!

AICB-P2T2 · Ngày 23 Disaster Recovery & High Availability cho AI Infrastructure lms.vinuni.edu.vn · Slide & template trên LMS
