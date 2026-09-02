# Review batch question-bank-v1

**Nguồn:** `data/questions/review/question-bank-v1.md`  
**Validator:** exit 0 · 100 item · 90 objective · 0 defect · 1 WARN (Q22/R3.2)  
**Phạm vi:** census 100/100 item; không lấy mẫu.  
**Kết luận:** chỉ các item `accept` được đưa vào approved pool; không item nào được publish.

## Tổng hợp

| Trạng thái | Số item |
|---|---:|
| accept | 72 |
| revise | 13 |
| reject | 15 |
| escalate | 0 |

**Accept:** Q1–Q2, Q4, Q6, Q8, Q10–Q13, Q15–Q21, Q23–Q25, Q29, Q31–Q32,
Q34–Q43, Q45–Q50, Q53, Q55–Q63, Q65–Q69, Q72–Q75, Q77–Q78, Q80–Q84,
Q86–Q87, Q89–Q90, Q97–Q100.

**Revise:** Q5, Q9, Q33, Q44, Q52, Q54, Q64, Q70, Q71, Q76, Q79, Q85, Q88.

**Reject:** Q3, Q7, Q14, Q22, Q26–Q28, Q30, Q51, Q91–Q96.

## Item cần xử lý

### Reject — evidence không trả lời đủ stem/rationale (§2.2)

- **Q3:** rationale nói “nếu đoạn chứa `foo_bar_v2` chưa từng vào top-100 thì rerank không cứu được”; span chỉ chứng minh dense hụt exact ID và BM25 tìm keyword, không nói về candidate set/reranker.
- **Q7:** stem hỏi tenant isolation và session-derived authorization; span chỉ nói metadata pre-filter theo `year` để giảm search space/tăng precision.
- **Q14:** span chỉ định nghĩa bốn metric RAGAS; không hỗ trợ các can thiệp “cải thiện retrieval/chunking/query”, “tighten prompt” hoặc “reranking/threshold”.
- **Q22:** xem mục WARN bên dưới.
- **Q26:** span hỗ trợ semantic memory bằng vector retrieval, nhưng không hỗ trợ “governance và versioning” hoặc các so sánh trong rationale về KV cache/feature store.
- **Q27:** span hỗ trợ “BFS” và “thu thập triples”, nhưng không hỗ trợ “provenance” và “giới hạn hop” trong đáp án.
- **Q28:** span mô tả kênh indirect injection nhưng nói rõ cơ chế phòng thủ thuộc bài khác; không chứng minh control “tách instruction/data” hay giới hạn của perplexity filter trong rationale.
- **Q30:** span nói về online/vector memory store và semantic cache, không trả lời giải pháp “consolidation/summary và retrieval chọn lọc”.
- **Q91:** evidence chỉ hỗ trợ trace latency và SLI/SLO/error budget; thiếu quality metrics, baseline/drift, privacy và versioning.
- **Q92:** evidence thiếu tenant authorization/RLS, tool allowlist, logging/redaction và incident response.
- **Q93:** evidence thiếu state transitions, checkpoint/resume, circuit breaker và audit.
- **Q94:** evidence thiếu giới hạn 2 hop, tenant/course filter, dedupe `source_span_id` và BM25-only degraded mode.
- **Q95:** evidence thiếu data classification, policy cấm private-data fallback, user messaging và telemetry/audit.
- **Q96:** evidence thiếu consent/PII, retention và cơ chế tránh memory cũ làm sai follow-up.

### Reject — đáp án thứ hai hợp lý (§2.1)

- **Q51:** distractor D “A/B testing evaluation” cũng có thể chạy trên production traffic thật. Stem cần giới hạn vào taxonomy ba loại trong evidence hoặc phân biệt continuous monitoring với online experiment.

### Revise — stem/metadata/group

- **Q9:** stem hỏi thứ tự retrieve/ingest/generate, nhưng option chỉ sắp Parse/Clean/Chunk/Metadata/Embed/Index; sửa stem để hỏi ingestion pipeline.
- **Q5 + Q71:** Q71 định nghĩa RRF “theo vị trí rank, không theo score thô”, làm lộ Q5; gán cùng group `rrf-fusion`.
- **Q44 + Q85:** Q44 định nghĩa A2A là uỷ quyền giữa agent, làm lộ scenario Q85; gán cùng group.
- **Q52 + Q79:** hai câu tiết lộ định nghĩa offline/online cho nhau; gán group `evaluation-modes`. Q52 nên là `apply`, không phải `analyze`.
- **Q64 + Q70:** cùng hỏi post-filter làm recall sập âm thầm; gán group `filtered-ann`. Q70 nên là `analyze`, không phải `apply`.
- **Q33:** tình huống cụ thể chọn cấu hình chặn tool → `apply`, không phải `understand`.
- **Q54:** áp dụng trực tiếp định nghĩa faithfulness → `apply`, không phải `analyze`.
- **Q76:** tình huống batch replay chọn pattern idempotent → `apply`, không phải `understand`.
- **Q88:** phân biệt SFT với alignment → `understand`, không phải `recall`.

## WARN đã xử lý

- **Q22 — R3.2, span 153 ký tự: reject.** Span đủ để phân biệt log với trace hành trình/latency, nhưng không chứa mệnh đề quyết định về “quality feedback”, version comparison hoặc quality drift. Đây đồng thời là lỗi chặn §2.2.

## Kiểm tra bổ sung Q100

Các claim pháp lý nhạy thời gian đã được đối chiếu ngoài evidence: Luật Bảo vệ dữ liệu cá nhân
91/2025/QH15 có hiệu lực từ 01/01/2026; Điều 20 yêu cầu hồ sơ đánh giá tác động chuyển dữ
liệu xuyên biên giới trong 60 ngày; Điều 23 quy định thông báo vi phạm đủ điều kiện trong 72
giờ; Điều 8 quy định trần phạt 5% doanh thu năm trước cho tổ chức vi phạm chuyển dữ liệu cá
nhân xuyên biên giới. Q100 được accept.

Chi tiết máy đọc cho toàn bộ 100 quyết định nằm tại `question-bank-v1-review.json`.
