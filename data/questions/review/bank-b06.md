# Chiron AI — Question Bank B-06 (human-authored, constructed response)

**Trạng thái:** Candidate for expert review. Không publish, không dùng để chấm learner.
**Phạm vi:** 4 câu tự luận, soạn tay theo `docs/QUESTION_AUTHORING_CONTRACT.md` §6.
**Mục tiêu quota:** hoàn thiện 10 CR theo `constructed_response_blueprint` — sau pilot (6 câu) còn thiếu 1 code_or_pseudocode, 1 system_design, 1 tracing_and_monitoring_diagnosis, 1 security_and_data_governance.
**Không trùng batch trước:** mọi `source_span_id` chưa được các batch trước dùng.

**Quy ước chấm chung cho mỗi tiêu chí 2 điểm:** 0 = vắng mặt/sai; 1 = nêu đúng khái niệm nhưng thiếu cơ chế, điều kiện hoặc verification; 2 = thiết kế cụ thể, đúng ràng buộc tình huống và nêu được cách kiểm chứng/trade-off. Giải pháp thay thế đạt cùng thuộc tính (ví dụ compensation action khác thay saga step, ở nơi phù hợp) được đủ điểm.

### 1. Pseudocode retry an toàn cho agent — code_or_pseudocode (10 điểm)
> **Metadata:** `topic=agent-safe-retry` · `cognitive_level=apply` · `difficulty=hard` · `assessment_type=constructed_response` · `format=code_or_pseudocode`

Một agent gọi tool `charge_card(order_id, amount)` để trừ tiền. Timeout không phân biệt được "request thất bại" với "request thành công nhưng reply chậm" — retry mù có thể trừ tiền hai lần. Viết pseudocode cho một action executor bọc quanh lời gọi tool có side effect, đảm bảo an toàn khi retry, khi resume sau crash, và khi gặp một hành động không thể hoàn tác (ví dụ gửi vé, gửi email).

**Rubric:** idempotency key ổn định theo ý định (không theo tham số thô) 2đ; kiểm tra kết quả đã ghi trước khi thực thi lại (at-least-once + consumer idempotent) 2đ; phân biệt bước có compensation (undo) với bước pivot không thể hoàn tác 2đ; đặt pivot ở cuối chuỗi và gate bằng human approval trước khi vượt qua pivot 2đ; audit log ghi lại quyết định retry/resume 2đ.

**Test hành vi bắt buộc:**
1. Gọi lại executor với cùng `order_id` sau khi request trước đã thành công nhưng client timeout → không charge lần hai.
2. Crash giữa chừng ở bước "giữ chỗ" (trước pivot) → resume chỉ replay các bước có compensation, không tự động chạy bước pivot.
3. Đến bước pivot (gửi vé) → executor dừng lại chờ approval, không tự thực thi.
4. Một compensation (undo) chạy lỗi → ghi vào trạng thái cần con người can thiệp, không âm thầm retry vô hạn.

**Đáp án tham chiếu ngắn gọn:** idempotency key theo ý định (ví dụ `order_id` cố định, không hash tham số) tra trong bảng kết quả đã ghi trước khi gọi tool; mỗi bước có compensation ghi cặp (action, undo); bước pivot được đánh dấu và chỉ chạy sau khi có approval ghi trong audit log; resume đọc lại state đã ghi, không gọi lại các bước đã completed.

**Đáp án chấp nhận khác:** dùng saga orchestration của một framework durable execution (Temporal, Restate) thay vì tự viết state machine, miễn giữ đủ ba thuộc tính: idempotency theo ý định, tách rõ compensation vs pivot, và gate người trước pivot.

**Evidence:** `338383ec-ba0a-5879-a76a-a4d8f6f8bf99`, `b8542100-8cd3-500c-9d4d-bbe67efa0494` — *Deployment — Đưa Agent Lên Cloud*, slide 84 và 87.

---

### 2. Deploy an toàn cho agent service — system_design (10 điểm)
> **Metadata:** `topic=agent-deployment-pipeline` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response` · `format=system_design`

Agent là hệ thống stateful chạy gần như liên tục — một lượt agent có thể kéo dài, và cắt ngang giữa chừng làm hỏng trải nghiệm. Thiết kế pipeline deploy một bản cập nhật cho agent service từ lúc merge code tới khi phục vụ 100% traffic. Nêu rõ: cách tránh cắt ngang request đang chạy dở, thứ tự ramp traffic, gate chất lượng trước khi tăng traffic, và cách xử lý khi bản mới có tool call gây side effect thật.

**Rubric:** graceful shutdown/rolling: `terminationGracePeriodSeconds` lớn hơn worst-case agent turn, không cắt ngang request đang chạy 2đ; ramp theo thứ tự shadow (mirror, bỏ output) → canary (% nhỏ, output thật) → 100%, không nhảy thẳng lên canary lớn 2đ; eval gate so với baseline của nhánh (không phải ngưỡng tuyệt đối), chặn merge/promote khi dưới ngưỡng 2đ; kiểm soát side effect khi shadow — chặn tool call có side effect thật của version mới trong pha shadow, nếu không "không trả output" vẫn tốn tiền/trừ tiền thật 2đ; auto-rollback dựa trên metric (ví dụ AnalysisRun theo dõi Prometheus) thay vì chỉ theo dõi thủ công 2đ.

**Đáp án chấp nhận khác:** dùng blue-green thay rolling nếu vẫn giữ được thuộc tính không cắt ngang request đang chạy (ví dụ rainbow deployment giữ cả hai version chạy song song thay vì switch tức thời).

**Evidence:** `4d8e2999-2155-57ea-97bc-fee25295af4b`, `6d179860-0103-5f99-8f39-ea56cd77e15a`, `c0d22d23-fa0f-5b77-83ef-89b1c9ecf9ce` — *Deployment — Đưa Agent Lên Cloud*, slide 65, 79 và 78.

---

### 3. Chẩn đoán sự cố latency qua trace — tracing_and_monitoring_diagnosis (10 điểm)
> **Metadata:** `topic=incident-latency-diagnosis` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response` · `format=tracing_and_monitoring_diagnosis`

9h sáng, user báo agent phản hồi chậm gấp đôi bình thường. Không có deploy nào rõ ràng gần đây. Bạn có quyền truy cập metric, log và trace. Mô tả quy trình điều tra từ lúc nhận báo cáo tới lúc xác định root cause, và giải thích vì sao thứ tự đó — không phải thứ tự khác — là đúng.

Trace của một request chậm hôm nay trông như sau:

```
invoke_agent ecommerce-agent 5100ms (trước: 2500ms)
|- chat claude-sonnet-4-6 (plan) 400ms
|- execute_tool rag_retrieve 2800ms (trước: 600ms)
|- chat claude-sonnet-4-6 (plan) 300ms
'- chat claude-sonnet-4-6 (synthesize) 1400ms
```

**Rubric:** thứ tự điều tra đúng metric (khoanh vùng "có gì đó chậm, từ khi nào") → log (lọc theo correlation_id, tìm "request nào") → trace (tìm "chậm ở bước nào"), giải thích được vì sao đảo thứ tự — ví dụ lao thẳng vào đọc log thô hàng nghìn request — là sai lầm thường gặp 3đ; đọc đúng trace mẫu và chỉ ra `rag_retrieve` là root cause (chậm 4.6× so với trước, còn các bước LLM vẫn bình thường) 3đ; đề xuất bước điều tra tiếp theo hợp lý sau khi khoanh vùng vào `rag_retrieve` (ví dụ kiểm tra vector store, index, hoặc downstream dependency của bước retrieve) 2đ; nêu được vì sao không có trace thì phải đoán mò giữa LLM/network/tool, còn có trace thì xác định trong thời gian ngắn 2đ.

**Đáp án tham chiếu ngắn gọn:** Metric trả lời "có gì đó chậm, từ khi nào"; log trả lời "request nào"; trace trả lời "chậm ở bước nào" — ba tầng bổ sung cho nhau nên phải đi theo đúng thứ tự từ khoanh vùng rộng tới hẹp. Với trace mẫu, `execute_tool rag_retrieve` là root cause rõ ràng: 2800ms so với baseline 600ms (chậm 4.6 lần), trong khi ba bước `chat` vẫn ở mức bình thường — nên bước điều tra tiếp theo phải đi vào vector store/index, không phải nghi ngờ model.

**Evidence:** `6186099a-2b90-57b0-ad13-86353228a572`, `367274c2-e95e-5a5f-be49-e066c99057cb` — *Monitoring, Logging & Observability*, slide 90 và 92.

---

### 4. PII trong observability xuyên biên giới — security_and_data_governance (10 điểm)
> **Metadata:** `topic=observability-pii-governance` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response` · `format=security_and_data_governance`

Sản phẩm của bạn phục vụ người dùng Việt Nam, agent nhận input tự do (có thể chứa tên, SĐT, CCCD, thông tin tài chính), và team dùng một nền tảng observability SaaS đặt ở nước ngoài để lưu trace/log. Thiết kế chính sách logging/tracing cho hệ thống này: những gì được capture, cách xử lý PII, thời hạn lưu trữ, kiểm soát truy cập, và nghĩa vụ pháp lý khi dữ liệu rời khỏi Việt Nam.

**Rubric:** capture có chọn lọc — mặc định KHÔNG capture raw prompt/completion, chỉ opt-in khi thật cần; dùng template id thay vì log nguyên văn khi có thể 2đ; kỹ thuật xử lý PII cụ thể — redact/mask tại điểm phát sinh, allowlist field được log, hash định danh thay vì lưu gốc (không chỉ nói chung chung "ẩn danh hoá") 2đ; retention có chủ đích theo loại dữ liệu — trace chi tiết lưu ngắn (ví dụ 7–30 ngày), metric tổng hợp lưu dài hơn, gắn với lý do chi phí và rủi ro pháp lý 2đ; kiểm soát truy cập và audit — RBAC chỉ cấp khi cần, ghi lại ai đã xem trace chứa dữ liệu người dùng, hỗ trợ quyền xoá/truy cập của user 2đ; nhận diện đúng nghĩa vụ pháp lý khi chuyển dữ liệu PII sang SaaS nước ngoài — cần hồ sơ đánh giá tác động khi chuyển xuyên biên giới, báo cáo vi phạm dữ liệu trong khung thời gian luật định, và nêu được rủi ro nếu bỏ qua 2đ.

**Đáp án chấp nhận khác:** tự host observability stack (Prometheus/Grafana/self-hosted tracing) để tránh hoàn toàn bài toán chuyển dữ liệu xuyên biên giới, miễn vẫn giữ đủ kỹ thuật xử lý PII và retention có chủ đích ở trong nước.

**Evidence:** `078d5052-24c1-57a6-9b1f-6e3c10a2efe6`, `a5d3995f-9d05-5fe5-b9c4-f244abad1cc2`, `8728c7b9-4504-5fc8-9ac2-2c0c591de395`, `9f37fb60-67ab-57bf-a4c7-32b6effd22a5` — *Monitoring, Logging & Observability*, slide 101–104.

## Review checklist

- [ ] Mỗi tiêu chí rubric có anchor 0/1/2 hoặc mô tả đủ cụ thể để chấm nhất quán.
- [ ] Có câu chấp nhận giải pháp thay thế đạt cùng thuộc tính.
- [ ] Câu code/pseudocode có test hành vi quan sát được, không chấm bằng rubric văn xuôi thuần.
- [ ] Mọi citation resolve trong `source_spans.jsonl`.
- [ ] Không trùng span với pilot-v1 hoặc B-02..B-05.
