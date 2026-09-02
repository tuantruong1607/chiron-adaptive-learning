# Chiron retrieval golden set

`golden.jsonl` là ground truth cho retrieval/citation của câu hỏi học viên chủ động hỏi tutor, không phải blueprint đề thi.

## Interaction boundary

- `user_question`: học viên hỏi để được giải thích, tìm nguồn hoặc nối kiến thức. Retriever cần lấy đúng evidence; câu trả lời nên trực tiếp và thích nghi với mức hiểu của học viên.
- `assessment_item`: câu hỏi trong luyện đề/thi thử. Loại này không được nằm trong retrieval golden set vì cần đánh giá thêm reasoning process, đáp án/rubric, cognitive level, difficulty và khả năng chống answer leakage.

Runner bắt buộc mọi case có `interaction_type=user_question`. Nếu một assessment item bị trộn vào file, validation và quality gate đều fail.

## Query classes

- `direct`: một khái niệm hoặc fact có source span chính rõ ràng.
- `prerequisite`: câu hỏi yêu cầu tìm các kiến thức nền cần học trước.
- `multi_hop`: câu hỏi cần nối từ hai source spans trở lên để trả lời trọn vẹn.

## Contract mỗi dòng

- `id`: ID ổn định của case.
- `query`: câu hỏi tiếng Việt giống cách học viên hỏi.
- `interaction_type`: phải là `user_question` trong suite này.
- `query_class`: `direct`, `prerequisite` hoặc `multi_hop`.
- `expected_concepts`: nhãn dùng để phân tích coverage; không phải retrieval key.
- `required_source_span_ids`: các UUID evidence bắt buộc để đạt required recall đầy đủ.
- `acceptable_source_span_ids`: nguồn tương đương/bổ trợ được tính relevant nhưng không thay required recall.
- `rationale`: lý do case tồn tại trong suite.
- `review_status`: `approved` sau khi product owner duyệt đúng phạm vi tương tác.
- `approval_scope`: ghi rõ đây là learner-initiated tutor query, không phải assessment item.

## Review checklist

1. Query có tự nhiên và không chứa đáp án trong câu hỏi không?
2. `required_source_span_ids` có thực sự đủ và cần thiết không?
3. Có alternate source span hợp lệ nào chưa liệt kê không?
4. Query class có đúng với số bước reasoning/retrieval không?
5. Case có trùng semantic intent với case khác không?

Source span UUID trong golden set là **runtime IDs từ PostgreSQL/Qdrant payload**. File parse manifest có thể dùng deterministic namespace khác dù checksum và locator giống nhau; không dùng manifest UUID để chấm retrieval runtime.

## Run baseline

```shell
uv run --project services/worker --python 3.12 --extra eval --extra embedding \
  python services/worker/scripts/eval_retrieval.py \
  --dataset eval/rag/golden.jsonl \
  --output eval/rag/runs/ragas-e5-adaptive-v1.json \
  --modes dense bm25 hybrid adaptive
```

Runner dùng local query embedding, tenant/course pre-filter và collection/version trong `.env`. Không gọi LLM hoặc embedding API bên ngoài.

RAGAS 0.4.x được dùng qua `SingleTurnSample` và `IDBasedContextPrecision/Recall`:

- Precision xem required + acceptable spans là relevant.
- Recall chỉ dùng required spans vì acceptable spans là nguồn thay thế, không phải evidence bắt buộc phải retrieve hết.
- MRR@K, nDCG@K, Hit@K và latency vẫn được Chiron tính deterministic bên cạnh RAGAS.

`evaluate()` cũ của RAGAS đã deprecated; runner không dùng API đó. Mỗi run ghi cả JSON chi tiết và Markdown summary, sau đó chạy quality gate so adaptive với hybrid theo từng query class.

## Human review gate

Golden set 50 case đã được product owner approve ngày 2026-08-30 với phạm vi **learner-initiated tutor query**. Approval này không áp dụng cho câu hỏi luyện đề/thi thử. Có thể tái sinh review pack cân bằng bằng lệnh:

```shell
uv run --project services/worker --python 3.12 \
  python services/worker/scripts/build_golden_review.py \
  --dataset eval/rag/golden.jsonl \
  --output eval/rag/review/review-pack-20.md
```

Baseline chính thức phải chạy với `--require-approved`. Không sử dụng approval của suite này để hợp thức hóa assessment item.

## Current P0 baseline

Artifact: `runs/ragas-e5-adaptive-v1.json` và `.md`.

- Split manifest v1 khóa bằng checksum: 35 development và 15 holdout, stratified theo query class.
- Source-span dedup diễn ra trước top-k. Production mặc định RETRIEVAL_MAX_SUBQUERIES=1; two-query expansion chỉ còn là experimental flag.
- Development: adaptive required recall 0.633 so với hybrid 0.624, P95 299.6 ms; mọi gate PASS.
- Holdout mở đúng một lần sau khi khóa cấu hình: adaptive/hybrid cùng required recall 0.600, P95 adaptive 251.3 ms; mọi gate PASS.
- Không tune tiếp trên holdout v1; thay đổi retrieval tiếp theo phải dùng development hoặc tạo split version mới trước khi xem kết quả.

## Candidate Graph-lite evaluation

- Draft graph: 34 nodes, 29 typed edges, 102 chunk links; prerequisite cycle count bằng 0.
- Traversal bị giới hạn 1 hop cho prerequisite và 2 hops cho multi-hop; direct không gọi graph.
- Architecture review PASS: traversal chỉ nhận version/link/edge/source-node/target-node cùng status; builder dọn stale candidate records và tái chạy giữ đúng 34/29/102.
- Ontology sample đã sửa thành `sli_slo part_of observability`; provenance cho Hybrid Search, RAG Evaluation và Circuit Breaker trỏ tới nội dung trực tiếp.
- Production giữ GRAPH_LITE_ENABLED=false và chỉ chấp nhận review status active.
- Candidate development run: P95 323.3 ms, direct/prerequisite không regression, multi-hop recall delta -0.033. Graph gate đang FAIL và Graph-lite holdout chưa được mở.
- 10 mẫu trong eval/graph/review-pack-10.md đã qua audit và được khuyến nghị approve. Chưa ghi `approved` vào database vì cần quyết định ký duyệt từng record; không có candidate nào active.
