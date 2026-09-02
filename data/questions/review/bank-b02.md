# Chiron AI — Question Bank B-02 (human-authored)

**Trạng thái:** Candidate for expert review. Không publish, không dùng để chấm learner.
**Phạm vi:** 20 objective, soạn tay theo `docs/QUESTION_AUTHORING_CONTRACT.md`.
**Nguồn:** slide có nội dung thật, ưu tiên slide tự gọi tên misconception (contract §2.3).
**Không trùng pilot:** mọi `source_span_id` ở đây chưa được `pilot-v1.md` dùng.

## Objective questions (20)

### 1. HITL anti-pattern — scenario diagnosis
> **Metadata:** `topic=hitl-gating` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Đội đặt cổng duyệt cho mọi tool call của agent. Người duyệt thấy đầy đủ context từng request, nhưng sau hai tuần tỉ lệ approve là 98% và họ bắt đầu bấm duyệt không đọc. Vấn đề cốt lõi là gì?

- A. Cổng duyệt đặt quá rộng nên bão hoà, biến review thành rubber stamp.
- B. Người duyệt thiếu context nên không đánh giá được từng request một.
- C. Chưa có feedback loop nên agent không cải thiện được theo thời gian.
- D. Chưa đo tỉ lệ approve/reject nên không biết cổng đang hoạt động ra sao.

**Đáp án:** A. B bị đề bài loại trừ vì người duyệt đã có đủ context. C và D là anti-pattern thật nhưng không giải thích được vì sao 98% request lọt qua: nguyên nhân là cổng chặn cả những ca vô hại.  
**Evidence:** `ecd98cfc-e747-5961-8939-7a76606c9558` — *Guardrails, HITL & Responsible AI*, slide 62.

### 2. Confidence gating — scenario diagnosis
> **Metadata:** `topic=confidence-calibration` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`

Một thiết kế HITL route sang người khi model báo `confidence < 0.7`. Vì sao đây là cổng yếu?

- A. Ngưỡng 0.7 quá thấp; nâng lên 0.9 sẽ bắt được nhiều ca rủi ro hơn hẳn.
- B. Confidence model tự nói thường lệch cao; nên route theo loại hành động.
- C. Nên lấy trung bình confidence của ba lần chạy để giảm phương sai đi.
- D. Nên bỏ hẳn HITL vì confidence không bao giờ đo được một cách đáng tin.

**Đáp án:** B. Verbalized confidence có xu hướng lệch cao — model nói “95% chắc chắn” cho cả câu trả lời sai — nên A chỉ dời một con số vốn đã không đáng tin. C giảm phương sai chứ không sửa được bias. Chưa đo calibration thì mọi ngưỡng đều là con số bịa cho có vẻ khoa học.  
**Evidence:** `fcb73a48-a31c-5d2b-9992-13ad52cd4acd` — *Guardrails, HITL & Responsible AI*, slide 73.

### 3. Tool permission — single choice
> **Metadata:** `topic=tool-permission` · `cognitive_level=understand` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`

Agent đang chạy ở chế độ `bypassPermissions`. Cấu hình nào thực sự chặn cứng được một tool nguy hiểm?

- A. Bỏ tool đó khỏi `allowed_tools` để nó không còn được cấp quyền nữa.
- B. Đặt permission mode chặt hơn ngay tại thời điểm gọi tool đó.
- C. Khai tool đó trong `disallowed_tools`, hoặc chặn bằng PreToolUse hook.
- D. Thêm allow rule hẹp hơn, vì allow rules chạy sau permission mode.

**Đáp án:** C. `allowed_tools` không ràng buộc được `bypassPermissions` — tool không nằm trong danh sách vẫn lọt theo mode, nên A và D đều vô hiệu. Riêng PreToolUse hook chặn được kể cả khi `bypassPermissions` đang bật.  
**Evidence:** `08203f6e-0435-5e6f-83ce-5e60baf561e0` — *Guardrails, HITL & Responsible AI*, slide 69.

### 4. MCP OAuth — single choice
> **Metadata:** `topic=mcp-oauth` · `cognitive_level=understand` · `difficulty=hard` · `group=mcp-oauth` · `mutually_exclusive_with=none`

Spec MCP cấm server nhận token không được cấp riêng cho nó. Tác hại chính của token passthrough là gì?

- A. Làm token hết hạn sớm hơn dự kiến ở service phía sau proxy.
- B. Buộc client phải đăng ký lại theo Dynamic Client Registration.
- C. Khiến discovery phải fallback về `.well-known` thay vì dùng header.
- D. Vô hiệu hoá rate limiting và audit trail ở service phía sau.

**Đáp án:** D. B và C đều là chi tiết có thật của spec OAuth cho MCP nhưng thuộc bẫy khác: DCR đang bị khai tử, còn thay đổi discovery là hệ quả của RFC 9728. Không cái nào là lý do spec dùng chữ MUST NOT.  
**Evidence:** `eaacc828-fb95-5f81-8c24-4d7602342f99` — *Deployment — Đưa Agent Lên Cloud*, slide 52.

### 5. Confused deputy — scenario diagnosis
> **Metadata:** `topic=mcp-oauth` · `cognitive_level=apply` · `difficulty=hard` · `group=mcp-oauth` · `mutually_exclusive_with=none`

Một MCP proxy xác thực đúng user rồi chuyển tiếp mọi `client_id` nhận được. Lỗ hổng ở đây là gì?

- A. Token của user bị chuyển tiếp nguyên vẹn sang service phía sau.
- B. Discovery không còn dùng `WWW-Authenticate` theo RFC 9728 nữa.
- C. Thiếu khai `application_type` tại thời điểm đăng ký client mới.
- D. Xác thực đúng user không đồng nghĩa uỷ quyền cho client đó.

**Đáp án:** D. Proxy phải giữ registry `client_id` đã duyệt theo từng user và kiểm tra trước mỗi flow. A mô tả bẫy token passthrough, một lỗi khác; B và C là chi tiết discovery và đăng ký, không liên quan tới việc client chưa được uỷ quyền.  
**Evidence:** `eaacc828-fb95-5f81-8c24-4d7602342f99` — *Deployment — Đưa Agent Lên Cloud*, slide 52.

### 6. Health probe — scenario diagnosis
> **Metadata:** `topic=health-probes` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Container agent bị restart liên tục dù process vẫn phục vụ được; chỉ có vector store đang chậm. Sai cấu hình nằm ở đâu?

- A. Đưa kiểm tra dependency vào liveness thay vì vào readiness probe.
- B. Đặt startup probe gate hai probe còn lại khi container boot chậm.
- C. Trả về `status: degraded` thay vì `ok` trong health endpoint.
- D. Thiếu trường `uptime`, `version` và `dependencies` trong payload health.

**Đáp án:** A. Liveness fail thì restart container, readiness fail chỉ gỡ khỏi load balancer — nhầm hai cái tạo restart loop vô ích. B là cấu hình đúng cho boot chậm; C và D không gây restart.  
**Evidence:** `6660a2f8-4825-5f55-8d5c-a89e323c90e2` — *Deployment — Đưa Agent Lên Cloud*, slide 64.

### 7. Durable execution — single choice
> **Metadata:** `topic=durable-execution` · `cognitive_level=understand` · `difficulty=hard` · `group=durable-execution` · `mutually_exclusive_with=none`

Agent crash ở bước 7 sau khi đã gọi 4 tool. Durable execution tránh trả tiền LLM lần nữa bằng cách nào?

- A. Giảm nhiệt độ về 0 để lần chạy lại cho ra kết quả giống hệt lần đầu.
- B. Ghi output LLM vào journal; khi replay thì đọc lại, không gọi model.
- C. Lưu checkpoint ở mức node để node đã xong không phải chạy lại nữa.
- D. Bọc toàn bộ workflow trong một transaction có khả năng rollback.

**Đáp án:** B. C là cơ chế có thật của LangGraph nhưng giải bài toán khác: checkpoint ở mức node, nên node chưa xong vẫn gọi lại cả LLM call. A làm output ổn định hơn nhưng vẫn tốn tiền gọi model.  
**Evidence:** `6d327e5f-4376-51c0-96b4-e025f931548c` — *Deployment — Đưa Agent Lên Cloud*, slide 86.

### 8. Checkpoint vs durable — scenario diagnosis
> **Metadata:** `topic=durable-execution` · `cognitive_level=analyze` · `difficulty=hard` · `group=durable-execution` · `mutually_exclusive_with=none`

Vì sao “checkpoint” của LangGraph không tương đương durable execution?

- A. Vì checkpoint chỉ ghi state vào bộ nhớ chứ không ghi xuống đĩa.
- B. Vì checkpoint không lưu được kết quả của tool call ra hệ thống ngoài.
- C. Vì checkpoint ở mức node: node chưa xong sẽ gọi lại cả LLM call.
- D. Vì checkpoint không hỗ trợ resume sau khi process bị restart lại.

**Đáp án:** C. A sai vì production dùng PostgresSaver ghi xuống đĩa; D sai vì resume chính là mục đích của checkpoint. Điểm khác biệt nằm ở độ hạt: journal ghi từng call, checkpoint ghi từng node.  
**Evidence:** `6d327e5f-4376-51c0-96b4-e025f931548c` — *Deployment — Đưa Agent Lên Cloud*, slide 86.

### 9. Session lifetime — scenario diagnosis
> **Metadata:** `topic=session-lifetime` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Agent trên AgentCore chờ human approval 20 phút; quay lại thì mất sạch state. Nguyên nhân và cách tránh?

- A. Session chạm trần 8 giờ; nên chia workflow thành nhiều session ngắn.
- B. MicroVM bị huỷ khi deploy bản mới; nên khoá deploy trong giờ cao điểm.
- C. Timeout mặc định của Modal là 5 phút; nên khai `timeout=` lớn hơn.
- D. Session chết vì idle 15 phút; phải externalize state ra ngoài runtime.

**Đáp án:** D. A nhầm trần tổng với idle timeout — 20 phút chưa chạm 8 giờ. C là con số có thật nhưng của Modal Sandbox, không phải AgentCore. State nằm ngoài runtime thì trần nào cũng vượt được.  
**Evidence:** `eb7ecd35-3d78-5ae1-9321-763a454380f2` — *Deployment — Đưa Agent Lên Cloud*, slide 42.

### 10. Framework vs runtime — single choice
> **Metadata:** `topic=framework-vs-runtime` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Vì sao tài liệu vendor hay bị so sánh nhầm tầng khi chọn nền tảng agent?

- A. Vì mọi hãng đều đặt tên hai tầng giống hệt nhau nên rất khó phân biệt.
- B. Vì tầng framework luôn đóng nguồn còn tầng runtime thì luôn mở nguồn.
- C. Vì đổi framework và đổi runtime tốn công như nhau nên không cần tách.
- D. Vì framework quyết định code bạn viết, runtime quyết định ai trực sự cố.

**Đáp án:** D. B sai ngay với ví dụ trong bảng: Strands Agents và deepagents đều mở nguồn ở tầng framework. C sai vì đổi framework là refactor còn đổi runtime chỉ là re-deploy — chi phí khác hẳn nhau.  
**Evidence:** `2ece7f49-59ee-55cd-a0fd-bd668aaf1697` — *Deployment — Đưa Agent Lên Cloud*, slide 41.

### 11. Memory lifecycle — single choice
> **Metadata:** `topic=memory-lifecycle` · `cognitive_level=understand` · `difficulty=easy` · `group=memory-basics` · `mutually_exclusive_with=none`

Theo khung Capture–Filter–Store–Retrieve, thứ nào KHÔNG tự động trở thành memory?

- A. Toàn bộ chat history được giữ lại theo kiểu “lưu cho chắc”.
- B. Sự kiện đã qua bước filter về PII, chất lượng và relevance.
- C. Profile người dùng được truy lại khi có ích cho câu hỏi hiện tại.
- D. Trạng thái người dùng được giữ liên tục qua nhiều phiên làm việc.

**Đáp án:** A. Prompt dài hơn, file PDF upload một lần không truy lại có chủ đích, và toàn bộ chat history đều tạo nhiễu nhiều hơn là hữu ích. B, C, D đều đã đi qua đủ ba thành phần data + policy + retrieval.  
**Evidence:** `cf63e42e-9e92-53a5-943f-58d50e5c60b3` — *Data Foundations*, slide 10.

### 12. Memory vs retrieval — scenario diagnosis
> **Metadata:** `topic=memory-vs-retrieval` · `cognitive_level=analyze` · `difficulty=hard` · `group=memory-basics` · `mutually_exclusive_with=none`

Agent “quên” mất context vừa retrieve ở lượt kế tiếp. Nhầm lẫn khái niệm nào gây ra chuyện này?

- A. Nhầm working memory với episodic memory trong vocab chuẩn.
- B. Nhầm retrieval — context cho câu hỏi này — với memory giữ trạng thái.
- C. Nhầm bước Capture với bước Filter nên sự kiện không được lưu lại.
- D. Nhầm semantic memory với procedural memory lúc thiết kế store.

**Đáp án:** B. Retrieval tìm context cho câu hỏi hiện tại; memory giữ trạng thái người dùng qua thời gian. A và D là nhầm lẫn trong nội bộ vocab memory, không giải thích được vì sao context biến mất sau một lượt.  
**Evidence:** `cf63e42e-9e92-53a5-943f-58d50e5c60b3` — *Data Foundations*, slide 10.

### 13. Multi-agent — single choice
> **Metadata:** `topic=multi-agent-design` · `cognitive_level=understand` · `difficulty=easy` · `group=multi-agent-myths` · `mutually_exclusive_with=none`

Phát biểu nào đúng về việc tăng số lượng agent trong một hệ thống?

- A. Nhiều agent giúp context được quản lý tự động ở từng worker.
- B. Nhiều agent luôn cho kết quả tốt hơn một agent đơn lẻ.
- C. Nhiều agent đồng nghĩa nhiều phức tạp, chỉ dùng khi thật cần.
- D. Nhiều agent cho phép supervisor dùng model nhỏ hơn hẳn.

**Đáp án:** C. A là hiểu lầm phổ biến: context vẫn phải được quản lý cẩn thận ở từng worker. B đảo ngược đánh đổi thực tế. D trộn hai chuyện khác nhau — cỡ model của supervisor không phụ thuộc số worker.  
**Evidence:** `92f6a307-eb7d-5e02-add8-2bc5302e2461` — *Multi-Agent & Kết Nối Hệ Thống*, slide 73.

### 14. MCP vs A2A — single choice
> **Metadata:** `topic=mcp-vs-a2a` · `cognitive_level=understand` · `difficulty=medium` · `group=multi-agent-myths` · `mutually_exclusive_with=none`

MCP và A2A khác nhau ở điểm nào?

- A. MCP dành cho agent nội bộ, A2A dành cho agent của bên thứ ba.
- B. MCP là chuẩn mở, còn A2A là giao thức riêng của một hãng.
- C. MCP chạy trên stdio, còn A2A bắt buộc phải chạy trên HTTP.
- D. MCP là tích hợp tool, còn A2A là uỷ quyền giữa các agent.

**Đáp án:** D. A và B chia theo ranh giới tổ chức và giấy phép, không phải theo chức năng. C lấy một chi tiết transport có thật của MCP rồi suy diễn thành ranh giới giữa hai giao thức.  
**Evidence:** `92f6a307-eb7d-5e02-add8-2bc5302e2461` — *Multi-Agent & Kết Nối Hệ Thống*, slide 73.

### 15. Supervisor sizing — scenario diagnosis
> **Metadata:** `topic=supervisor-routing` · `cognitive_level=apply` · `difficulty=medium` · `group=multi-agent-myths` · `mutually_exclusive_with=none`

Chọn model cho supervisor trong một hệ multi-agent, nguyên tắc nào đúng?

- A. Supervisor phải là model lớn nhất vì nó chịu trách nhiệm cuối cùng.
- B. Supervisor nên dùng chung model với mọi worker cho thật nhất quán.
- C. Supervisor chỉ cần đủ năng lực để route đúng sang worker phù hợp.
- D. Supervisor nên là model rẻ nhất vì nó không trực tiếp sinh nội dung.

**Đáp án:** C. A là hiểu lầm mà bài gọi tên. D đúng hướng tiết kiệm nhưng lật sang cực ngược lại: rẻ nhất mà route sai thì cả hệ hỏng. Tiêu chí là đủ để route đúng, không phải lớn nhất hay rẻ nhất.  
**Evidence:** `92f6a307-eb7d-5e02-add8-2bc5302e2461` — *Multi-Agent & Kết Nối Hệ Thống*, slide 73.

### 16. Hai kiểu sai — scenario diagnosis
> **Metadata:** `topic=error-types` · `cognitive_level=apply` · `difficulty=medium` · `group=precision-recall` · `mutually_exclusive_with=none`

Hệ kiểm duyệt nội dung của bạn chặn nhầm nhiều bài hợp lệ. Đây là kiểu sai nào và thiệt hại chính?

- A. False positive: tạo việc thừa và làm người dùng mất niềm tin.
- B. False negative: để lọt nội dung độc hại khỏi tầm kiểm soát.
- C. False positive: làm giảm recall nên bỏ sót ca thật sự cần bắt.
- D. False negative: khiến precision tụt vì báo nhầm quá nhiều lần.

**Đáp án:** A. C gọi đúng tên kiểu sai nhưng gán nhầm hệ quả: báo nhầm ảnh hưởng precision, không phải recall. B và D mô tả kiểu sai ngược lại với triệu chứng đề bài.  
**Evidence:** `61ae3e8c-b1e1-5679-b774-cda7dfc88c2b` — *AI IN ACTION · DAY 05 BATCH 02*, slide 22.

### 17. Precision & recall — single choice
> **Metadata:** `topic=precision-recall` · `cognitive_level=apply` · `difficulty=medium` · `group=precision-recall` · `mutually_exclusive_with=none`

AI quét 1.000 giao dịch, báo “đáng ngờ” 40 lần và đúng 30 lần. Thực tế có 50 giao dịch xấu. Precision và recall là bao nhiêu?

- A. Precision 60%, recall 75%.
- B. Precision 75%, recall 60%.
- C. Precision 30%, recall 50%.
- D. Precision 40%, recall 30%.

**Đáp án:** B. Precision = 30/40 = 75% (số báo đúng chia tổng số lần báo “có”); recall = 30/50 = 60% (số bắt được chia tổng số ca thật sự cần bắt). A hoán đổi hai chỉ số — đây là lỗi phổ biến nhất.  
**Evidence:** `154b4f78-509e-5e5a-8966-365196dda5ea` — *AI IN ACTION · DAY 05 BATCH 02*, slide 23.

### 18. Output variance — single choice
> **Metadata:** `topic=nondeterminism` · `cognitive_level=understand` · `difficulty=medium` · `group=nondeterminism` · `mutually_exclusive_with=none`

Cùng một input, hai lần chạy cho hai output khác nhau. Nên coi đây là gì?

- A. Một bug cần sửa bằng cách khoá seed và nhiệt độ của model.
- B. Một edge case hiếm, chỉ cần xử lý khi có user phàn nàn.
- C. Hành vi mặc định của hệ probabilistic, cần thiết kế quanh nó.
- D. Dấu hiệu behavioral drift do model vừa được nhà cung cấp cập nhật.

**Đáp án:** C. Nondeterminism là constraint để thiết kế vòng tránh, giống latency, chứ không phải bug để sửa. D là loại failure khác: drift là lệch dần theo thời gian, không phải khác nhau giữa hai lần chạy liền kề.  
**Evidence:** `894e7ed1-438c-5a73-bc2c-237f0eba9572` — *AI IN ACTION · NGÀY 5*, slide 23.

### 19. Behavioral drift — scenario diagnosis
> **Metadata:** `topic=nondeterminism` · `cognitive_level=analyze` · `difficulty=hard` · `group=nondeterminism` · `mutually_exclusive_with=none`

Release thì đúng, vài tuần sau lệch, và đội chỉ biết chuyện đó qua complaint của user. Sai lầm thiết kế nào lộ ra ở đây?

- A. Acceptance criteria nhị phân: vài test case xanh đã coi là đủ để ship.
- B. Giấu variance: không có nút regenerate và không framing confidence.
- C. Fallback là ý sau cùng: spec chỉ có một dòng hiện thông báo lỗi.
- D. Reasoning-level failure: các bước đều đúng nhưng tổ hợp ra kết quả sai.

**Đáp án:** A. Vài test case là demo chứ không phải distribution, nên chúng giấu mất messy input và drift. B và C là hai sai lầm thiết kế khác trong cùng bài, còn D là một loại failure chứ không phải sai lầm thiết kế.  
**Evidence:** `894e7ed1-438c-5a73-bc2c-237f0eba9572` — *AI IN ACTION · NGÀY 5*, slide 23.

### 20. Reasoning-level failure — scenario diagnosis
> **Metadata:** `topic=nondeterminism` · `cognitive_level=analyze` · `difficulty=hard` · `group=nondeterminism` · `mutually_exclusive_with=none`

Retrieval đúng, tool call đúng, dashboard toàn xanh, nhưng người dùng vẫn nhận câu trả lời sai. Đây là loại failure nào?

- A. Output variance: hai lần chạy cho ra hai kết quả khác nhau.
- B. Reasoning-level failure: từng bước đúng nhưng tổ hợp ra kết quả sai.
- C. Behavioral drift: chất lượng lệch dần sau vài tuần chạy trong production.
- D. Fallback thiếu: hệ chỉ hiện một dòng thông báo lỗi khi gặp sự cố.

**Đáp án:** B. Đúng câu “monitoring shows all green, but the product fails”. A và C đều là loại failure có thật nhưng để lại dấu vết khác: variance lộ khi chạy lại, drift lộ khi so theo thời gian. D không phải loại failure mà là thiếu sót ở đường phục hồi.  
**Evidence:** `894e7ed1-438c-5a73-bc2c-237f0eba9572` — *AI IN ACTION · NGÀY 5*, slide 23.

## Review checklist

- [ ] Vị trí vật lý đáp án đúng phân bố đều 4 vị trí (script check).
- [ ] Không câu nào có đáp án đúng dài hơn 1.3× option ngắn nhất.
- [ ] Mỗi câu đúng 4 option và đúng 1 đáp án.
- [ ] group/mutually_exclusive đóng kín và đối xứng (script check).
- [ ] Mọi citation resolve trong `source_spans.jsonl` (script check).
- [ ] Đã chạy §2 của `QUESTION_REVIEW_PROTOCOL.md` (đáp án thứ hai, evidence trả lời được stem).
