---
schema_version: 1
course_id: rag-intensive
document_id: "e2d7f096-db89-53f3-8311-9204617eb204"
document_version_id: "cd8bd548-d9ce-568f-b736-6ebf15bd5d15"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Data Observability"
source_file: "track 2 - day 27.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 27.pdf"
source_sha256: "bec0bb5fcd2ca2699b96b994f68ff90ad28098f6ce9e1116eec13587c14c961b"
parser_version: chiron-structured-markdown-v1
page_count: 36
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":36}"
language: vi
---

# Data Observability

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"1df0965a-1016-592a-a386-037bb15c743f","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Data Observ","extraction_method":"pdf-text-layer"},"checksum":"122cb4c315ae05874c816f1c395c6b241de07e0dcab60c54ff1305c2217a2206"} -->

## Slide 1 - Data Observ

Data Observ- ability & Lineage AICB-P2T2 · Ngày 27 · Chương 6: Tổng Hợp Giảng viên VinUniversity · Phase 2 · Track 2 · T uần 6

---

<!-- chiron-source-span: {"source_span_id":"d1467d79-2547-5170-8b59-2aa0117a46ad","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"01304647aac0e2b49ba4e8e07ebdf47763a96269904a079633d4a620472b465e"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Pipeline chạy thành công nhưng data

### sai — làm sao bạn biết? Case study
Một team phát hiện model accuracy giảm 15% — sau 3 ngày mới biết up- stream data bị schema change. Data observability phát hiện trong 60 giây.” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"44f271f8-fc31-5b8b-8c4c-d93e62bb5507","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"ad060908449bb1a341bc5c877564afd2eecbaf9ac671894f56f62ed9bcbd9f0b"} -->

## Slide 3 - Nội Dung Bài Học

1. Data Observability vs Pipeline Monitoring

2. Great Expectations: Suites & Checkpoints

3. Monte Carlo & Anomaly Detection

4. dbt Tests: Unit & Integration

5. SLO Engineering cho Data & AI

6. Incident Response cho Data Systems

7. Live Demo: Incident Detection

8. Labs: Data Observability Implementation Giảng viên (VinUni) AICB · Ngày 27 T uần 6 1 / 31

---

<!-- chiron-source-span: {"source_span_id":"30c83589-ba2d-519f-a8a7-97b0f3d733b1","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu","extraction_method":"pdf-text-layer"},"checksum":"5e1b68840e7055aca37d3e35d31c90584b15aa96d8a86ed1dce04dfb080132e7"} -->

## Slide 4 - Mục Tiêu

### Sau buổi học này, bạn sẽ

1. Master data observability với Great Expectations + Monte Carlo

2. Thiết kế advanced Grafana dashboards cho data quality

3. Implement SLO engineering cho data & AI services

4. Xây dựng incident response workflow cho data incidents Data observability concepts (20 min) → Great Expectations (45 min) → Monte Carlo / dbt tests (30 min) → SLOs (30 min) → Demo & Labs Giảng viên (VinUni) AICB · Ngày 27 T uần 6 2 / 31

---

<!-- chiron-source-span: {"source_span_id":"8471eeeb-ed88-5b2b-8cc3-df5a6c165de2","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"b4756481cd5af7380ada0690e5a27e594229a6080a70fd1ab2194548f0acb42b"} -->

## Slide 5 - Deliverable Cuối Ngày

GE checkpoint suite + Monte Carlo-style anomaly detection + SLO dashboard

- Great Expectations Checkpoint chạy trong Airflow DAG

- Z-score anomaly detection script với Slack alert

- 3 SLOs cho data platform + Grafana dashboard với error budget panel

- Incident response runbook document
Giảng viên (VinUni) AICB · Ngày 27 T uần 6 3 / 31

---

<!-- chiron-source-span: {"source_span_id":"566d9859-6e6e-5a42-8996-9189da0eac27","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"T ại Sao Pipeline Thành Công Không Đủ?","extraction_method":"pdf-text-layer"},"checksum":"63027ba24049a4bbf2beebf4ca164b3c4d1702e21c8141da4b6aeadb8430324c"} -->

## Slide 6 - T ại Sao Pipeline Thành Công Không Đủ?

Job Airflow báo Success. Logs sạch. CPU bình thường. Nhưng dashboard doanh thu sai 40%.

### Ba lỗi âm thầm phổ biến

- Source API bị rate-limit → chỉ lấy
được 10% records

- Cột price đổi từ USD sang VND
không thông báo

- Join bảng dimension fail ngầm vì
customer_id đổi kiểu dữ liệu T ại sao pipeline không phát hiện?

- Pipeline chỉ quan tâm tiến trình có
chạy xong không

- Không quan tâm kết quả có đúng
không

- Airflow success = job finished,
không phải data correct Kết luận: Lỗi nguy hiểm nhất không phải crash — mà là silent failure: hệ thống chạy bình thường nhưng dữ liệu sai. AI/ML và analytics chết vì silent bad data nhiều hơn vì service down. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 4 / 31

---

<!-- chiron-source-span: {"source_span_id":"33ad847c-74ac-56e2-878f-76bfc6e0b6b4","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Pipeline Monitoring vs Data Observability","extraction_method":"pdf-text-layer"},"checksum":"202e96e1a8f752e586a005443bc993967c1a0c89dc1ffb3c449b760969f12f30"} -->

## Slide 7 - Pipeline Monitoring vs Data Observability

### Nhìn từ góc hạ tầng

- Job có chạy xong không?

- Chạy mất bao lâu?

- Có lỗi kỹ thuật không?

- CPU, memory có ổn không?
⇒ Trả lời câu hỏi: “Máy có chạy không?”

### Nhìn từ góc chất lượng dữ liệu

- Data có đúng không?

- Data có mới (fresh) không?

- Data có đầy đủ không?

- Data có nhất quán không?
⇒ Trả lời câu hỏi: “Data có đáng tin không?” Cả hai đều cần thiết và bổ sung cho nhau. Monitoring bảo vệ hạ tầng. Observability bảo vệ niềm tin vào dữ liệu — thứ mà dashboard, ML model, và AI service phụ thuộc vào mỗi ngày. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 5 / 31

---

<!-- chiron-source-span: {"source_span_id":"e5e22ede-f701-5e13-88e6-c5bec25ea03b","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"5 Trụ Cột Data Observability (Monte Carlo Framework)","extraction_method":"pdf-text-layer"},"checksum":"de6c057853e035bd6472f987131b06facb91c6c372ca3263919e810ba7f51afc"} -->

## Slide 8 - 5 Trụ Cột Data Observability (Monte Carlo Framework)

Freshness Dữ liệu có cập nhật đúng cadence? Volume Số records có bất thường, đột biến? Distribution Phân phối giá trị có thay đổi? Schema Cột bảng có bị đổi tên/kiểu? Lineage Khi incident, bảng nào bị kéo theo? Mỗi trụ cột = một chiều rủi ro: Freshness phát hiện delay, Volume phát hiện mất data, Distribution phát hiện giá trị bất thường, Schema phát hiện breaking changes, Lineage giúp trace root cause. Chi phí thực tế: 10+ giờ/tuần data downtime, $15M/năm thiệt hại từ bad data (Gartner) — observability đánh đổi đầu tư nhỏ để tránh thiệt hại lớn. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 6 / 31

---

<!-- chiron-source-span: {"source_span_id":"78fd987b-f43d-5065-b0a3-35291945bcb4","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Mô Hình Trưởng Thành: Từ Reactive Đến Self-Healing","extraction_method":"pdf-text-layer"},"checksum":"5640622e3fb27f54c06483248a49fccbcd9c906693e64591d9c7aeee438009e0"} -->

## Slide 9 - Mô Hình Trưởng Thành: Từ Reactive Đến Self-Healing

Level 0

### Reactive
user báo mới biết Level 1 Rules: GX, dbt, threshold Level 2

### Anomaly
Z-score, Prophet Level 3

### Predictive
phát hiện trước Level 4

### Self-healing
tự động sửa Hiểu từng Level để biết mình đang ở đâu: L0 — check bằng mắt, user báo mới biết (nguy hiểm nhất). L1 — rules rõ ràng, tự động, bắt known problems. L2 — học từ lịch sử, phát hiện unknown unknowns. L3–4 — predictive & self-healing, cần đầu tư lớn hơn. Hầu hết teams ở Level 0–1. Mục tiêu khóa này: đạt Level 2 và hiểu lộ trình lên Level 3–4. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 7 / 31

---

<!-- chiron-source-span: {"source_span_id":"af6f6613-48fd-5561-b983-e0422bfa89f4","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Quan Sát Dữ Liệu AI và Phi Cấu Trúc","extraction_method":"pdf-text-layer"},"checksum":"2d29e6d32e08801e59fba1accd58a6f95f3b994479fd3fdd158ff495f15818cb"} -->

## Slide 10 - Quan Sát Dữ Liệu AI và Phi Cấu Trúc

Dữ liệu text, ảnh, embedding không có schema rõ ràng — không thể check null rate hay value range trực tiếp. Cần cách tiếp cận khác.

### Giải pháp: trích xuất derived features rồi monitor chúng

- Embedding drift: cosine similarity giữa batch mới vs
baseline giảm → retrieval quality suy giảm

- Phân phối token: độ dài text đổi đột ngột → upstream
source có vấn đề

- Chất lượng ảnh: blur score, resolution distribution đổi bất
thường

- RAG metrics: chunk count, retrieval hit rate, answer length
distribution Không monitor raw content. Monitor measurable features trích xuất từ content. Công cụ: KL divergence, KS test, cosine similarity. T ư duy: “biến thứ không đo được thành thứ đo được”. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 8 / 31

---

<!-- chiron-source-span: {"source_span_id":"8e47e85e-39c6-5d59-8b43-4057fcab2b3d","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Từ Giả Định Trong Đầu Đến Kiểm Tra Chạy Được","extraction_method":"pdf-text-layer"},"checksum":"c1d00dd1a8bc30d6bf6fe38e71ec08a47eea82e8a5fae0ef8db9ac587a7c7bac"} -->

## Slide 11 - Từ Giả Định Trong Đầu Đến Kiểm Tra Chạy Được

Mọi data engineer đều có giả định ngầm về dữ liệu — nhưng chúng chỉ nằm trong đầu, không được kiểm tra tự động. Khi dữ liệu sai, không ai biết cho đến khi user phàn nàn.

### Ví dụ giả định ngầm trong hệ thống

- Email của user không bao giờ null

- T uổi người dùng nằm trong khoảng
0–150

- Cột status chỉ có 3 giá trị hợp lệ

- Mỗi ngày có ít nhất 50K đơn hàng
Great Expectations (GX) biến chúng

### thành

- Kiểm tra tự động chạy được bằng
máy

- Lưu trong Git cùng pipeline code

- Tái sử dụng trên dev/staging/prod

- Báo cáo HTML tự động cho
stakeholders Phép so sánh: Expectation = assert; suite = file test cho một bảng; checkpoint = bước CI chạy cả bộ test. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 9 / 31

---

<!-- chiron-source-span: {"source_span_id":"f28e8f05-a7ab-59db-aca9-e58bba4fbfc2","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Thiết Kế Expectation Suite Hiệu Quả","extraction_method":"pdf-text-layer"},"checksum":"d32819471b6ca59564ff3ad469b1d9e9c458d108c83e700396ef7de5d372951c"} -->

## Slide 12 - Thiết Kế Expectation Suite Hiệu Quả

- Completeness: cột critical không null,
row count > 0

- Uniqueness: primary key không trùng

- Validity: giá trị trong range hoặc đúng
format

- Consistency: tổng chi tiết khớp tổng
aggregate

- Freshness-like: ngày mới nhất không
quá cũ

### Hard fail — block pipeline ngay

- Primary key bị duplicate

- Source table hoàn toàn rỗng

- Thiếu cột bắt buộc

### Soft fail — chỉ cảnh báo, tiếp tục

- Null rate tăng nhẹ

- Distribution hơi lệch

- Text description bất thường
Nguyên tắc thiết kế: Expectation quá lỏng (age 0^-999 ) thì vô dụng. Quá chặt thì tạo false alarm liên tục. Hãy gắn từng rule với business semantics thật, không phải kỹ thuật thuần túy. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 10 / 31

---

<!-- chiron-source-span: {"source_span_id":"b3a41376-cccd-5a4e-abfc-80fd0ef77bc1","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Great Expectations: Code Example","extraction_method":"pdf-text-layer"},"checksum":"98d124034397b887b2d5d0f06b5ca88755ab7f835a9f2f5f2cb4dd780ac446d9"} -->

## Slide 13 - Great Expectations: Code Example

```text
import great_expectations as gx
context = gx.get_context()
suite = context.add_expectation_suite( "users_suite")
suite.add_expectation(
gx.expectations.ExpectColumnValuesToNotBeNull(
column="email"
)
)
suite.add_expectation(
gx.expectations.ExpectColumnValuesToBeBetween(
column="age", min_value=0, max_value=150
)
)
■ get_context(): khởi tạo GX
```
workspace

- add_suite: tạo bộ rules cho asset

- Expectation 1: email phải luôn có giá
trị (completeness)

- Expectation 2: tuổi nằm trong
khoảng hợp lý (validity) Giảng viên (VinUni) AICB · Ngày 27 T uần 6 11 / 31

---

<!-- chiron-source-span: {"source_span_id":"7e6bbe9a-de9b-52ef-9621-420ef398fe1f","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Checkpoint: Đưa Validation Vào Production Pipeline","extraction_method":"pdf-text-layer"},"checksum":"556c88807c26e3f140ed2c54595275395f3c705c727c519060abd43a5679d89b"} -->

## Slide 14 - Checkpoint: Đưa Validation Vào Production Pipeline

Checkpoint = Suite + Datasource + Actions

- Suite: bộ rules đã định nghĩa cho asset

- Datasource: batch dữ liệu thực tế cần
validate

- Actions: việc cần làm sau khi chạy
validation

### Actions phổ biến khi fail

- SlackNotificationAction: gửi alert tức
thì

- StoreEvaluationParameters: lưu metrics
để track

- Block pipeline: không để data xấu đi
tiếp downstream Source / Ingest ↓ GX Checkpoint ↙ ↘ fail → Slack pass ↓ Transform (dbt) ↓ Serving Table T ự động sinh HTML report để stakeholder xem pass/- fail mà không cần đọc code. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 12 / 31

---

<!-- chiron-source-span: {"source_span_id":"31add682-e941-5e7a-b783-99b62c533701","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Hai Lớp Phòng Thủ: Rules vs Anomaly Detection","extraction_method":"pdf-text-layer"},"checksum":"0b45d12055c95f9bf8883d88e66f3af0f7bf58891e43fe0b1d32fd7058a3ebe6"} -->

## Slide 15 - Hai Lớp Phòng Thủ: Rules vs Anomaly Detection

Câu hỏi: “Data có vi phạm rule đã biết không?” Ví dụ: email null, price âm, status ngoài tập cho phép Ưu điểm: rõ ràng, deterministic, không tranh cãi Nhược điểm: chỉ bắt được thứ đã nghĩ ra trước Câu hỏi: “Dữ liệu hôm nay có cư xử lạ không?” Ví dụ: row count giảm 50%, phân phối đột ngột đổi Ưu điểm: bắt được unknown unknowns Nhược điểm: có false positives, cần người re- view Phép so sánh trực quan: Rules-based giống kiểm tra cửa ra vào với danh sách điều kiện. Anomaly detection giống camera an ninh nhìn hành vi — không cần biết rule cụ thể, chỉ cần thấy “hôm nay trông khác hôm thường”. Production tốt nhất: kết hợp cả hai lớp. Không thay thế lẫn nhau. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 13 / 31

---

<!-- chiron-source-span: {"source_span_id":"b0fc5dac-373d-5040-a71f-b1e0f621e162","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Monte Carlo: Nền T ảng Anomaly Detection Quy Mô Lớn","extraction_method":"pdf-text-layer"},"checksum":"bc5bdde657e4ad3da894d74f8213b2fd0b1ee1e910d274f37473c3118f26de94"} -->

## Slide 16 - Monte Carlo: Nền T ảng Anomaly Detection Quy Mô Lớn

- Kết nối warehouse → tự động monitor
200+ metrics

- ML-based anomaly detection không cần
cấu hình thủ công

- Incident timeline: dùng lineage tìm root
cause trong vài phút

- Alert qua Slack, PagerDuty, email

### ⇒ Đại diện cho loại platform observability
mua SaaS thay vì tự xây từ đầu

- ydata-profiling: profile metrics và
statistics

- Z-score: abs(current - mean) / std > 3

- Time-series: Prophet dự đoán expected
value

- Alert khi actual > 3σ deviation

- Export metrics sang
Prometheus/Grafana ⇒ Linh hoạt hơn, nhưng cần engineering & maintenance liên tục Giảng viên (VinUni) AICB · Ngày 27 T uần 6 14 / 31

---

<!-- chiron-source-span: {"source_span_id":"efc82124-89d1-552c-8d6b-0060d14d6701","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Z-Score Anomaly Detection: Cách Hoạt Động","extraction_method":"pdf-text-layer"},"checksum":"10baa5b1be94f0782cdf65860c3b5ae0633e08fd13f336691daf953a7461e870"} -->

## Slide 17 - Z-Score Anomaly Detection: Cách Hoạt Động

```text
import numpy as np
def detect_anomaly(current_value, history, threshold=3):
mean = np.mean(history)
std = np.std(history)
if std == 0:
return False, 0.0
z_score = abs(current_value - mean) / std
return z_score > threshold, z_score
daily_counts = [10200, 10150, 10300, 10180, 10250]
today_count = 5100 # ảgim 50%!
anomaly, score = detect_anomaly(today_count, daily_counts)
# anomaly=True, score=7.2 -> ALERT!
```

- mean: hành vi trung bình lịch sử

- std: độ biến động bình thường

- z_score: lệch bao nhiêu standard
deviation

- > 3σ: rất bất thường → alert

- Metric có seasonality (cuối tuần vs
ngày thường)

- Sự kiện đặc biệt (flash sale, chiến
dịch)

- Lịch sử quá ngắn < 14 ngày

- ⇒ Cần Prophet hoặc segment
baseline Giảng viên (VinUni) AICB · Ngày 27 T uần 6 15 / 31

---

<!-- chiron-source-span: {"source_span_id":"10c62af8-376c-5df7-b8f0-9e42f3f13a0a","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Khi Nào Dùng Rules, Khi Nào Dùng Anomaly Detection?","extraction_method":"pdf-text-layer"},"checksum":"1b0dcb6fce4490cc933ac570230eef4d6a173fdb0b1b0330c50c3c44320af88b"} -->

## Slide 18 - Khi Nào Dùng Rules, Khi Nào Dùng Anomaly Detection?

- Biết rõ giá trị hợp lệ là gì

- Cần hard fail — block pipeline ngay

- Muốn kết quả deterministic, rõ ràng

- Ví dụ: primary key, null rate critical,
accepted values

- Muốn bắt pattern bất thường chưa được
viết rule

- Metric có lịch sử đủ dài để học baseline

- Chấp nhận false positives và có người
review

- Ví dụ: row count, null rate trend,
embedding drift Alert quá nhạy → nhiều false positives → team mệt mỏi, mất tin tưởng vào alert system. Alert quá lỏng → bỏ sót anomaly thật → data xấu đi sâu vào downstream mà không ai hay. Cần tuning liên tục và human review — anomaly detection không thể hoàn toàn thay con người. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 16 / 31

---

<!-- chiron-source-span: {"source_span_id":"9d5b6b86-0603-571c-ae86-7bfa79143790","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"T ại Sao Transformation Layer Cần Bảo Vệ Riêng?","extraction_method":"pdf-text-layer"},"checksum":"85ffeb2ebf2f8f3927ac5ef5e23627b1fc79be637637441464e92f6998e02a5e"} -->

## Slide 19 - T ại Sao Transformation Layer Cần Bảo Vệ Riêng?

Logic business sống trong SQL — một join sai hoặc filter sai thường không crash gì cả, data vẫn ra nhưng sai hoàn toàn

### Ví dụ lỗi âm thầm trong dbt

- Join bảng orders với customers
bằng key sai → doanh thu bị inflate lên

- Filter nhầm status = 'completed'
bỏ sót đơn hàng → báo cáo thấp hơn thực tế

- SCD logic sai → nhiều version
active cùng lúc cho cùng 1 customer

### dbt tests là lớp bảo vệ sát nhất

- Sống cạnh SQL model, chạy cùng
dbt build

- Phát hiện ngay sau khi transform
xong

- Trước khi serving table xuống
downstream

- Không cần tool bên ngoài thêm
Giảng viên (VinUni) AICB · Ngày 27 T uần 6 17 / 31

---

<!-- chiron-source-span: {"source_span_id":"cbccebf9-f9f9-5398-b6e6-3d5c12b0d076","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"dbt T est Pyramid","extraction_method":"pdf-text-layer"},"checksum":"1478a78f6e4d07989a97be8e39c733c903e7cec5b47fd1344d4b7e29d4b058ec"} -->

## Slide 20 - dbt T est Pyramid

Unit T ests (nhanh, gần model) Integration T ests E2E Data Validation not_null, unique, accepted_values, relationships Custom SQL tests, cross-table checks Full pipeline output validation Nguyên tắc kim tự tháp: Càng lên cao (Unit), test càng nhanh và gần model — chạy liên tục mỗi lần build. Càng xuống dưới (E2E), phạm vi rộng nhưng tốn kém hơn. Đừng bỏ Unit tests rồi kỳ vọng E2E cứu hết. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 18 / 31

---

<!-- chiron-source-span: {"source_span_id":"45d3b535-5b86-5e8b-9b9f-a1fda2a63634","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"dbt T ests: Built-in & Custom","extraction_method":"pdf-text-layer"},"checksum":"626d73932b4d50959c14095a03caea58109fdac38883362f150926be3f0ca00b"} -->

## Slide 21 - dbt T ests: Built-in & Custom

- not_null — cột critical không có NULL

- unique — primary key không bị trùng

- accepted_values — chỉ chấp nhận tập giá
trị định sẵn

- relationships — foreign key phải tồn tại ở
bảng cha ⇒ Miễn phí, nhanh, thiết yếu — chạy mỗi dbt test

- Custom SQL: query trả 0 rows = pass, có
rows = fail

- dbt-expectations: port mindset GX vào
dbt

- Elementary: observability quanh dbt —
trend, anomaly, dashboard

### Ví dụ custom test
“Không có user nào vừa inactive vừa có subscription active” Giảng viên (VinUni) AICB · Ngày 27 T uần 6 19 / 31

---

<!-- chiron-source-span: {"source_span_id":"c813855e-db6c-5e0d-aec2-54658b9b79af","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Phân Công Vai Trò: GX, dbt T ests và Anomaly Detection","extraction_method":"pdf-text-layer"},"checksum":"9960a27dd369e2a442f5ca46886731f4dabdf40257dbea53b134013c67f61c49"} -->

## Slide 22 - Phân Công Vai Trò: GX, dbt T ests và Anomaly Detection

Source/Ingest Anomaly detect. + basic GX checks

- 
Transform (dbt layer) dbt built-in + custom tests

- Serving T ables
GX checkpoint + SLO monitor

- Dashboard/Model
Downstream trust + incident resp.

### Không có tool nào làm hết mọi thứ — mỗi tool có chỗ đứng riêng

- GX: validation tổng quát, report HTML, dùng tốt ở boundary giữa layers

- dbt tests: sống cạnh SQL model, rất tự nhiên trong analytics engineering workflow

- Anomaly detection: bắt pattern chưa biết, cần baseline lịch sử, cần human review

- SLO + Incident: quản lý reliability theo thời gian, ứng phó khi có sự cố
Giảng viên (VinUni) AICB · Ngày 27 T uần 6 20 / 31

---

<!-- chiron-source-span: {"source_span_id":"2f079a52-df11-5695-88b1-87e0440ef943","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"T ại Sao Data Platform Cũng Cần SLO?","extraction_method":"pdf-text-layer"},"checksum":"a339073be20e7e918dad58096bc8e86203e938ee12f9bb304c9bab5ed70e8446"} -->

## Slide 23 - T ại Sao Data Platform Cũng Cần SLO?

Dữ liệu cũng có user — dashboard, ML model, AI service đều phụ thuộc vào data. Khi data không đáp ứng kỳ vọng, downstream user bị ảnh hưởng.

### Kỳ vọng thực tế của data users

- Dashboard CEO phải có data
trước 8:00 sáng

- Feature table cho fraud model
không stale quá 30 phút

- Null rate ở cột billing phải gần
bằng 0

- RAG indexing cập nhật tài liệu mới
trong 30 phút SLO biến kỳ vọng thành cam kết đo

### được

- Không còn tranh luận “chắc vẫn
ổn”

- Có số liệu rõ ràng để ưu tiên

- Khi breach thì biết cần làm gì tiếp
theo

- Tạo văn hóa: reliability là trách
nhiệm team, không phải may rủi Giảng viên (VinUni) AICB · Ngày 27 T uần 6 21 / 31

---

<!-- chiron-source-span: {"source_span_id":"467d9070-1c0c-57ce-b925-6a39729d33c4","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"SLI / SLO / Error Budget — Ba Khái Niệm Cốt Lõi","extraction_method":"pdf-text-layer"},"checksum":"e1addfb0bbdffabbbc9d97ad68e9f40a8f5cf52cc5d61bd31bb652815c359581"} -->

## Slide 24 - SLI / SLO / Error Budget — Ba Khái Niệm Cốt Lõi

SLI Service Level Indicator

### Chỉ số đo được
freshness_minutes, null_rate, p99_latency đo − − → SLO Service Level Objective

### Mục tiêu cụ thể
“freshness < 60 min 99.5% thời gian” tính − − → Error Budget 1 − SLO = budget

### Burn nhanh
dừng feature release, ưu tiên fix reliability Ví dụ cụ thể: SLO = 99.5% freshness < 60 phút ⇒ Error budget = 0.5% = 3.6 giờ/tháng được phép stale. Ba câu hỏi nền tảng: (1) Ta đo cái gì? → SLI (2) Ta muốn tốt tới mức nào? → SLO (3) Khi xấu thì làm gì khác? → Error budget policy Giảng viên (VinUni) AICB · Ngày 27 T uần 6 22 / 31

---

<!-- chiron-source-span: {"source_span_id":"6ea74747-744a-5bad-92aa-35abd3d9c6d5","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Error Budget Burn Rate & Alerting","extraction_method":"pdf-text-layer"},"checksum":"b5a125138440ac41fb97f0b5928e81f5b70e992dc71c63084334c5ebd71d4d5f"} -->

## Slide 25 - Error Budget Burn Rate & Alerting

### Burn rate — tốc độ tiêu hao error budget

- Fast burn: đốt 2% budget/giờ → P0
alert, phản ứng ngay

- Slow burn: đốt 5% budget/6h → P1
alert, điều tra trong ca

- Burn rate phát hiện sớm hơn chờ breach
cuối tháng

### SLO Dashboard nên hiển thị

- Giá trị SLI hiện tại vs target SLO

- Remaining error budget (%)

- Burn rate ngắn hạn (1h) và dài hạn (7
ngày) SLO buộc team ưu tiên reliability trước feature mới. Budget còn nhiều → release nhanh được. Budget đang cháy → dừng release, tập trung fix. SLO không chỉ là số học — nó là cơ chế quản trị quyết định khi nào ưu tiên sta- bility. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 23 / 31

---

<!-- chiron-source-span: {"source_span_id":"e8ce3c11-a724-5b91-8ce0-12f71134b81a","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Thiết Kế SLO Cho Data/AI Platform","extraction_method":"pdf-text-layer"},"checksum":"0a03b33cd7c8d60803dd7c7b36fb374c2ce85dd2ed0d4c942802a3d15a06dd76"} -->

## Slide 26 - Thiết Kế SLO Cho Data/AI Platform

SLI tốt: đo được tự động, gắn với trải nghiệm down- stream user thật sự, ổn định về định nghĩa theo thời gian. SLI kém: “dashboard trông có vẻ ổn”, “model có vẻ đang chạy tốt”

### Ví dụ SLI phù hợp

- freshness_minutes: phút kể từ lần update cuối

- null_rate: tỷ lệ null của cột critical

- p99_latency: latency inference API

- schema_violations: số lần schema drift
SLO càng cao → chi phí engineering, alerting, on-call, redundancy càng lớn. Chỉ đặt SLO gần 100% cho critical con- tract như billing, AI serving trong pro- duction. SLO nên phản ánh business criticality thật, không phải kỳ vọng lý tưởng. SLA vs SLO: SLO là mục tiêu nội bộ để vận hành. SLA là cam kết chính thức với khách hàng, thường nghiêm ngặt hơn và có hậu quả pháp lý. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 24 / 31

---

<!-- chiron-source-span: {"source_span_id":"c0eeb60c-3227-517a-a75d-96ac02dd956a","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Vòng Đời Một Data Incident: 6 Giai Đoạn","extraction_method":"pdf-text-layer"},"checksum":"d1bc30f2938da5dffdef5e541c814c8e76ac4f4c81004666e0e8dc6200ecd04c"} -->

## Slide 27 - Vòng Đời Một Data Incident: 6 Giai Đoạn

1. Phát hiện (Detection)

- 2. Phân loại
(Triage)

- 3. Giảm thiểu
(Mitigation)

- 4. Root Cause
Analysis

- 5. Xác nhận
Phục hồi

- 6. Postmortem
(Học lại) T ại sao cần quy trình rõ ràng? Alert mà không ai phản hồi thì vô dụng. Có người phản hồi nhưng không có runbook thì chậm. Có runbook nhưng không có severity thì hỗn loạn. Observability chỉ có giá trị khi team biết phản ứng — detection là hiệp 1, operations mới là những hiệp còn lại tạo ra giá trị thực sự. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 25 / 31

---

<!-- chiron-source-span: {"source_span_id":"65e550a0-2781-58b6-9c37-01f089a4db3e","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Phân Loại Mức Độ Nghiêm Trọng (Severity)","extraction_method":"pdf-text-layer"},"checksum":"77f4562d1a72b6240fcdcdd7fb4a55412f5035e6ecb18ba06a4aee25c2d9ad4c"} -->

## Slide 28 - Phân Loại Mức Độ Nghiêm Trọng (Severity)

Mức Mô tả Thời gian phản ứng Ví dụ P0 Hệ thống ngừng hoạt động 5 phút Pipeline dừng, không có data nào chạy P1 Dữ liệu sai 30 phút Giá trị sai ở serving table, model lỗi P2 Chất lượng giảm sút 2 giờ SLO bị vi phạm, freshness chậm P3 Vấn đề nhỏ Ngày làm việc tiếp theo Thiếu tài liệu, cảnh báo thấp

- PagerDuty: định tuyến on-call,
escalation

- Rundeck: chạy diagnostic scripts tự
động

- Slack war room: phối hợp realtime
Service down thì dễ thấy ngay. Data sai có thể âm thầm ảnh hưởng dashboard, billing, model trong nhiều giờ hoặc nhiều ngày mà không ai biết — thiệt hại âm thầm và sâu hơn. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 26 / 31

---

<!-- chiron-source-span: {"source_span_id":"e1426f86-a605-5623-ab51-0d9d5258259b","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Runbook: Cấu Trúc Phản Ứng Có Hệ Thống","extraction_method":"pdf-text-layer"},"checksum":"0d6684941bd7727638812d2e1c0faa7cc53b3132a7498af650f8c9fe2515ea29"} -->

## Slide 29 - Runbook: Cấu Trúc Phản Ứng Có Hệ Thống

Runbook = hướng dẫn thao tác chuẩn khi

### có incident

1. Xác nhận incident và xác định severity

2. Kiểm tra upstream ingestion có đang chạy không

3. So sánh row count source vs destination

4. Kiểm tra schema changes trong 24 giờ gần nhất

5. Dùng lineage: asset downstream nào bị ảnh hưởng?

6. Quyết định: rerun, rollback, hay suppress publication

7. Verify recovery và thông báo stakeholders

- Giảm thời gian chẩn đoán khi
đang áp lực

- Giảm sai sót do stress và thiếu ngủ

- Junior engineer xử lý được P2/P3

- Tạo baseline để cải thiện sau
postmortem Dashboard sai → schema đổi → thiếu schema check → source contract mơ hồ

- ownership không rõ ràng. Hỏi tại sao
liên tiếp đến khi thấy systemic cause. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 27 / 31

---

<!-- chiron-source-span: {"source_span_id":"bd6bba6a-7954-5bd3-8171-6e20ea1a1f01","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Chaos Engineering & Blameless Postmortem","extraction_method":"pdf-text-layer"},"checksum":"a9a1dcea9a80ee21ecff62178913a17e9218e9c558f308eeb6ebc63c4c6d643a"} -->

## Slide 30 - Chaos Engineering & Blameless Postmortem

Chủ động inject failure có kiểm soát để test hệ

### thống và team

- Kill Airflow worker giữa task đang chạy

- Inject schema change đột ngột vào
upstream

- Corrupt một phần source data

- Simulate network partition giữa
components Game day (diễn tập định kỳ): luyện phản xạ trong môi trường an toàn thay vì học lần đầu trên incident thật.

- Detection → Triage → Mitigation

- Root Cause → Verify → Postmortem
Không phải: “ai đã làm sai” → đổ lỗi cá nhân Đúng hơn: “tại sao hệ thống để điều này xảy ra?” → fix systemic issue

### Postmortem tốt luôn có

- Timeline đầy đủ sự kiện

- 5 Whys root cause analysis

- Action items có owner và deadline cụ thể
Blameless ̸= không có accountability. Nó là cách học thật sự từ incident để ngăn tái diễn. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 28 / 31

---

<!-- chiron-source-span: {"source_span_id":"efcb42ca-87d8-5867-945e-731200857d92","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Live Demo: Data Incident Detection & Resolution","extraction_method":"pdf-text-layer"},"checksum":"cf19d6dae111d522feb5e57c8ebd2bfaf48f99661ef9bf05a8f083cf333b8e2c"} -->

## Slide 31 - Live Demo: Data Incident Detection & Resolution

1. Demo 1: Inject schema change vào upstream data → GE checkpoint fails → Slack alert trong 60 giây

2. Demo 2: Inject volume anomaly (10% of normal) → Z-score detection

- PagerDuty alert

3. Demo 3: dbt test failure → lineage graph identify upstream source of corruption

4. Demo 4: SLO dashboard — show error budget consumption, burn rate alert kích hoạt

5. Resolution flow: alert → runbook → auto-diagnostic → root cause → fix → verify Giảng viên (VinUni) AICB · Ngày 27 T uần 6 29 / 31

---

<!-- chiron-source-span: {"source_span_id":"0ceb8d83-b49e-5e54-92a4-bd44cb9910b7","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Lab #27","extraction_method":"pdf-text-layer"},"checksum":"2a174301dea13d09e69c7eb467557bbd4a48c613536b2a456eedc97b65e68b0a"} -->

## Slide 32 - Lab #27

Mục tiêu: Data Observability Implementation Deliverable: Setup GX Suite với Profiler; build Checkpoint tích hợp Airflow DAG; implement Z-score anomaly detection cho 5 key metrics với Slack alerts; define 3 SLOs và build Grafana SLO dashboard. Thời gian: 2.5h Giảng viên (VinUni) AICB · Ngày 27 T uần 6 30 / 31

---

<!-- chiron-source-span: {"source_span_id":"7670d5c6-4fa6-54d4-868a-6c7d1cf71f6f","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"2cf7840a8aaee8eb76075577090afaef6841eb602fb79f30e10bed99396d5ace"} -->

## Slide 33 - T ổng kết — Key T akeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Data observability ̸= pipeline monitoring — cần cả hai, focus khác nhau. Pipeline suc- ceeded không có nghĩa data đúng. 2 SLOs buộc team prioritize reliability over features — cultural shift quan trọng hơn tool- ing. 3 Automated anomaly detection phải có human review — false positives cần training models over time. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 30 / 31

---

<!-- chiron-source-span: {"source_span_id":"fa13b23b-01b7-5a0a-b322-aca3cb33b657","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"97a8c64b73a13fa7dbd34a14b72e476348d96ec59606c866b8bb1547df0ae59a"} -->

## Slide 34 - Tiếp theo & Bài tập

Ngày 28: Integration Workshop — Full Platform Demo “Tích hợp toàn bộ infrastructure stack, demo end-to-end platform, hoàn thành Milestone 3”

- Hoàn thành Lab 27: Data
Observability Implementation

- Review toàn bộ components
từ N16–N27

- Chuẩn bị Milestone 3 demo
script Giảng viên (VinUni) AICB · Ngày 27 T uần 6 31 / 31

---

<!-- chiron-source-span: {"source_span_id":"07cf424f-eb0e-5f2d-a96c-98325f127ca9","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"dcd1f0e1ce6afb1122e69627dd25ef813b8ff9556c18e61c4e67deb2f294a906"} -->

## Slide 35 - Hỏi & Đáp

Câu hỏi nào về data observability, Great Ex- pectations, SLOs, hay incident response?

---

<!-- chiron-source-span: {"source_span_id":"bc9da9d6-0f08-561f-a74e-868e328e6b47","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"63d30044c80375db2856c78eded84682a607530a74b587e2615b985916da8d98"} -->

## Slide 36 - Cảm ơn!

AICB-P2T2 · Ngày 27 Data Observability & Lineage lms.vinuni.edu.vn · Slide & template trên LMS
