# Chiron AI — Pilot Question Bank v1

**Trạng thái:** Candidate for expert review. Không publish, không dùng để chấm learner.  
**Phạm vi:** 30 objective + 6 constructed response; thời lượng đề pilot: **120 phút**.  
**Cách review:** kiểm tra một đáp án đúng duy nhất, độ hợp lý distractor, mức tư duy, và evidence ngay dưới từng câu.

## Objective questions (30)

### 1. Chunking — scenario diagnosis
> **Metadata:** `topic=chunking` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Một RAG trả lời thiếu ngữ cảnh vì mỗi chunk chỉ là một câu rời; tăng `top_k` làm context rất nhiễu. Can thiệp phù hợp nhất là gì?

- A. Tăng overlap giữa các chunk cố định lên 50% để câu liền kề dính vào nhau.
- B. Thêm cross-encoder rerank trên top-100 candidate trước khi đưa vào prompt.
- C. Chuyển sang semantic/hierarchical chunking, giữ trọn đoạn cùng một ý.
- D. Đổi sang embedding model có điểm VN-MTEB cao hơn model đang dùng.

**Đáp án:** C. Chunk là unit evidence: chunking hỏng thì embedding tốt, rerank tốt cũng vô dụng. Overlap 50% chỉ nối câu rời một cách máy móc, không khôi phục mạch đoạn.  
**Evidence:** `3c68387a-4057-5152-abc8-c14dd0db8804` — *Vector Store & Feature Store*, slide 22.

### 2. Embedding — single choice
> **Metadata:** `topic=embedding` · `cognitive_level=understand` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`



Vai trò cốt lõi của embedding trong dense retrieval là gì?

- A. Mã hóa text thành vector để so sánh mức tương đồng ngữ nghĩa.
- B. Chuẩn hóa score của BM25 và cosine về cùng một thang đo chung.
- C. Chấm lại mức phù hợp của từng cặp (query, doc) sau khi đã có candidate.
- D. Nén tài liệu gốc để giảm dung lượng lưu trữ trong vector database.

**Đáp án:** A. B là việc của fusion, C là cross-encoder rerank, D là nhiệm vụ của quantization.  
**Evidence:** `ab0d1e8b-88fe-5ffe-8c24-4dc8fbace6d4` — *RAG Pipeline*, slide 36.

### 3. Dense retrieval — scenario diagnosis
> **Metadata:** `topic=dense-vs-sparse-retrieval` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=Q4`



Query “cơ chế giữ version code chính xác” không tìm thấy tài liệu chứa đúng identifier `foo_bar_v2`, dù tìm thấy nhiều đoạn cùng nghĩa. Vì sao dense-only có thể hụt và nên bổ sung gì?

- A. Fine-tune embedding model trên corpus nội bộ để nó nhớ các identifier.
- B. Tăng `top_k` lên 100 rồi rerank bằng cross-encoder để kéo đoạn đúng lên.
- C. Thêm metadata filter theo trường `version` để thu hẹp search space lại.
- D. Bổ sung sparse/BM25 rồi hợp nhất hybrid; dense mù với token hiếm, chính xác.

**Đáp án:** D. Rerank chỉ xếp lại thứ hạng của candidate mà dense đã lấy — nếu đoạn chứa `foo_bar_v2` chưa từng vào top-100 thì rerank không cứu được.  
**Evidence:** `7faebd65-90b8-5ad2-a80c-92fa71f49dc6` — *RAG Pipeline*, slide 60.

### 4. BM25 — single choice
> **Metadata:** `topic=sparse-retrieval` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=Q3`



Loại query nào thường là ứng viên tốt cho sparse/BM25?

- A. Query mô tả ý định bằng từ ngữ khác hẳn tài liệu (“muốn lấy lại tiền”).
- B. Query chứa mã lỗi, tên hàm hoặc từ viết tắt chuyên ngành cần khớp đúng.
- C. Query dài nhiều mệnh đề, cần tổng hợp thông tin từ nhiều đoạn khác nhau.
- D. Query cần xếp hạng tài liệu theo độ mới thay vì theo mức độ liên quan.

**Đáp án:** B. A chính là ca BM25 trả 0 kết quả vì không trùng keyword nào — đó là điểm mù của sparse, không phải thế mạnh.  
**Evidence:** `648c675c-38de-53cc-bde4-b284d941c885` — *RAG Pipeline*, slide 57.

### 5. Hybrid + RRF — scenario diagnosis
> **Metadata:** `topic=hybrid-fusion` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Dense trả đúng đoạn giải thích, BM25 trả đúng API name. Bạn cần một ranking không phụ thuộc trực tiếp vào thang score không tương thích giữa hai retriever. Chọn gì?

- A. Reciprocal Rank Fusion trên thứ hạng của hai danh sách, với k = 60.
- B. Min-max normalize hai score về [0,1] rồi cộng lại theo trọng số đã chọn.
- C. Nhân cosine similarity với score BM25 và lấy giao của hai danh sách.
- D. Lấy top-5 của mỗi retriever rồi để LLM tự chọn đoạn phù hợp nhất.

**Đáp án:** A. B và C đều phải chạm vào giá trị score thô — đúng thứ đề bài loại trừ. RRF chỉ dùng rank nên không cần normalize.  
**Evidence:** `21aee365-ebec-5495-9bf1-cfa468c41533` — *Vector Store & Feature Store*, slide 18.

### 6. Reranking — single choice
> **Metadata:** `topic=reranking` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Trong two-stage retrieval, reranker nên được đặt ở đâu?

- A. Trước ANN search, để cross-encoder thu hẹp search space ngay từ đầu.
- B. Ngay sau bước chunk, để chấm chất lượng từng chunk lúc đang indexing.
- C. Sau khi ANN trả candidate, để cross-encoder chấm lại từng cặp query–chunk.
- D. Sau khi đã sinh câu trả lời, để chấm lại chất lượng output cho learner.

**Đáp án:** C. A bất khả thi về chi phí: cross-encoder phải nạp query cùng doc nên không quét được toàn corpus. D là LLM-as-judge, không phải rerank.  
**Evidence:** `4e75a8f4-496a-5f24-8847-ce1e26613f36` — *Vector Store & Feature Store*, slide 24.

### 7. Metadata filter — scenario diagnosis
> **Metadata:** `topic=tenant-isolation` · `cognitive_level=apply` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



Để ngăn learner A thấy tài liệu course/tenant khác, control nào thực sự chặn được và đặt đúng chỗ?

- A. Cấp mỗi tenant một collection riêng, client gửi kèm tên collection khi query.
- B. Post-filter ở application layer sau khi vector DB đã trả top-k về.
- C. Pre-filter `tenant_id` và `course_id` ngay tại vector query, lấy từ session.
- D. Chỉ dẫn trong system prompt yêu cầu không tiết lộ tài liệu ngoài khoá.

**Đáp án:** C. A vẫn để client tự khai phạm vi của mình nên chỉ cần sửa một tham số là đọc chéo được; B để dữ liệu cross-tenant rời khỏi vector DB và ăn mất recall của top-k; D là hướng dẫn, không phải enforcement.  
**Evidence:** `14900f34-494f-5fcf-99d6-d119a2617fa8` — *Production RAG*, slide 27.

### 8. HNSW — single choice
> **Metadata:** `topic=ann-indexing` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Trade-off đúng của ANN/HNSW là gì?

- A. Bảo đảm exact nearest neighbor, đổi lại tốn RAM hơn so với flat index.
- B. Giảm RAM so với flat index nhờ nén vector xuống số bit ít hơn.
- C. Cho phép corpus update-heavy rẻ hơn nhờ cấu trúc graph nhiều tầng.
- D. Đổi một phần recall tuyệt đối để lấy latency thấp và khả năng scale.

**Đáp án:** D. HNSW là RAM-bound (>10M vector @768d ≈ 10GB) và re-build chậm khi update nhiều — B là việc của quantization, C ngược với thực tế.  
**Evidence:** `e7bd702b-7034-5438-990b-865e9f56d1ba` — *Vector Store & Feature Store*, slide 15.

### 9. RAG pipeline — ordering
> **Metadata:** `topic=rag-offline-pipeline` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Chọn thứ tự hợp lý nhất: (i) retrieve evidence, (ii) ingest/chunk/index, (iii) generate grounded answer.

- A. Parse → Chunk → Clean → Embed → Metadata/Enrich → Index.
- B. Parse → Clean → Chunk → Metadata/Enrich → Embed → Index.
- C. Parse → Clean → Embed → Chunk → Metadata/Enrich → Index.
- D. Chunk → Parse → Clean → Metadata/Enrich → Embed → Index.

**Đáp án:** B. Clean phải xong trước khi cắt, vì noise lọt vào chunk là lọt vĩnh viễn; và embed luôn đứng sau chunk vì đơn vị đem đi embed chính là chunk.  
**Evidence:** `e85b1a0d-2cca-5e1d-9865-124255c24785` — *Production RAG*, slide 11.

### 10. Context precision — scenario diagnosis
> **Metadata:** `topic=context-precision` · `cognitive_level=apply` · `difficulty=medium` · `group=ragas-metrics` · `mutually_exclusive_with=none`



Top-5 đều liên quan chủ đề “RAG”, nhưng bốn chunk không giúp trả lời câu hỏi cụ thể. Metric nào cần cải thiện trước?

- A. Context precision.
- B. Context recall.
- C. Faithfulness.
- D. Answer relevancy.

**Đáp án:** A. Evidence có mặt nhưng lẫn nhiều chunk vô ích ⇒ precision. Recall chỉ hỏng khi thiếu hẳn chunk cần thiết.  
**Evidence:** `f53c8dff-7c45-5b6e-a1e7-72e6b610d406` — *AI Evaluation & Benchmarking*, slide 15.

### 11. Context recall — single choice
> **Metadata:** `topic=context-recall` · `cognitive_level=apply` · `difficulty=medium` · `group=ragas-metrics` · `mutually_exclusive_with=none`



Answer thiếu một điều kiện bắt buộc vì không có chunk cần thiết trong context. Đây chủ yếu là vấn đề gì?

- A. Context precision thấp.
- B. Faithfulness thấp.
- C. Answer relevancy thấp.
- D. Context recall thấp.

**Đáp án:** D. Thiếu hẳn chunk chứa điều kiện bắt buộc ⇒ recall. Precision là khi chunk cần thiết có mặt nhưng lẫn rác.  
**Evidence:** `29a86f69-881f-5cbe-a791-a2bd708cc9b1` — *Production RAG*, slide 35.

### 12. Faithfulness — scenario diagnosis
> **Metadata:** `topic=faithfulness` · `cognitive_level=apply` · `difficulty=medium` · `group=ragas-metrics` · `mutually_exclusive_with=none`



Context nói “chưa benchmark”, nhưng assistant trả lời “đã đạt 95%”. Chỉ số chất lượng bị vi phạm trực tiếp nhất?

- A. Answer relevancy.
- B. Faithfulness.
- C. Context precision.
- D. Context recall.

**Đáp án:** B. Claim trong output không được context support — đúng định nghĩa faithfulness. Answer relevancy vẫn cao vì câu trả lời đúng chủ đề được hỏi.  
**Evidence:** `8536b5af-6fad-5d52-bbf1-49fb2a7dda57` — *Monitoring, Logging & Observability*, slide 26.

### 13. Answer relevancy — single choice
> **Metadata:** `topic=answer-relevancy` · `cognitive_level=apply` · `difficulty=medium` · `group=ragas-metrics` · `mutually_exclusive_with=none`



Answer đúng sự thật nhưng chuyển sang giải thích fine-tuning khi user hỏi cách đánh giá retrieval. Lỗi chính là gì?

- A. Faithfulness thấp.
- B. Context recall thấp.
- C. Answer relevancy thấp.
- D. Context precision thấp.

**Đáp án:** C. Câu trả lời đúng sự thật và bám context nên faithfulness cao; cái hỏng là nó không trả lời câu được hỏi — RAGAS bắt lỗi này bằng reverse question generation.  
**Evidence:** `f7439078-7d87-5e52-aa26-f4128940df46` — *RAGAS, LLM-as-Judge & Guardrails*, slide 18.

### 14. RAG evaluation — scenario diagnosis
> **Metadata:** `topic=rag-diagnosis` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



RAGAS cho context recall thấp, faithfulness cao. Ưu tiên debug nào hợp lý?

- A. Cải thiện retrieval/chunking/query trước; generator đang bám context tốt.
- B. Tighten prompt “Only use provided context” và hạ temperature xuống 0.
- C. Thêm reranking cross-encoder, giảm `top_k` và tăng similarity threshold.
- D. Đổi judge model rồi đo lại, vì RAGAS score vốn brittle theo judge.

**Đáp án:** A. B là thuốc cho faithfulness thấp — mà faithfulness đang cao. C là thuốc cho precision thấp, không kéo recall lên được.  
**Evidence:** `75f5d2da-6f18-5e49-9f34-40adede15393` — *Production RAG*, slide 34.

### 15. Multi-hop — scenario diagnosis
> **Metadata:** `topic=multi-hop-retrieval` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=Q27`



User hỏi quan hệ giữa service A, dependency B và policy C; không span nào chứa toàn bộ đáp án. Retrieval strategy nào phù hợp nhất?

- A. Tăng `top_k` lên 50 và nới context window để LLM tự nối các mảnh lại.
- B. HyDE: sinh một câu trả lời giả rồi embed nó để đi truy xuất lại.
- C. Hierarchical chunking: retrieve child chunk rồi trả về nguyên trang parent.
- D. Traversal nhiều hop theo quan hệ, có provenance và giới hạn số hop.

**Đáp án:** D. A/B/C đều vẫn là truy xuất theo độ tương đồng của từng đoạn rời; không đoạn nào chứa đủ chuỗi quan hệ A→B→C nên nới rộng bao nhiêu cũng không nối được.  
**Evidence:** `9d404bc1-ed69-53a9-b78c-66cc1793a687` — *Vector Store & Feature Store*, slide 26.

### 16. Agent orchestration — scenario diagnosis
> **Metadata:** `topic=agent-idempotency` · `cognitive_level=apply` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



Một agent gọi tool thanh toán, timeout khi client retry và có nguy cơ charge hai lần. Control quan trọng nhất?

- A. Đặt timeout dài hơn và tăng số lần retry kèm exponential backoff.
- B. Idempotency key ổn định theo intent, backend dedup bằng Redis.
- C. Hash toàn bộ tham số của tool call làm key để loại bỏ request trùng.
- D. Bọc lời gọi tool trong một transaction của database nội bộ.

**Đáp án:** B. C là cái bẫy riêng của agent: LLM không sinh lại tham số y hệt cho cùng một ý định nên hash nội dung thô sẽ trượt. D không bao được side effect nằm ở provider bên ngoài.  
**Evidence:** `72a1c30d-3bba-502a-a1e2-b4d6c5ce13ec` — *Deployment — Đưa Agent Lên Cloud*, slide 85.

### 17. State machine — single choice
> **Metadata:** `topic=agent-state-machine` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Lợi ích chính của state machine cho workflow agent là gì?

- A. Cho phép agent tự quyết thứ tự bước mà không cần khai báo transition.
- B. Loại bỏ nhu cầu checkpoint vì state đã được biểu diễn tường minh rồi.
- C. Làm state, transition và recovery path tường minh nên debug và kiểm soát được.
- D. Giảm số token mỗi lượt gọi LLM nhờ nén lịch sử hội thoại vào state.

**Đáp án:** C. A mô tả agent tự do, ngược với state machine. B sai: state tường minh vẫn phải được persist thì mới resume được.  
**Evidence:** `10429522-3dce-5ced-bbd3-f9c0f0f7c10e` — *Multi-Agent Systems*, slide 25.

### 18. Checkpointing — scenario diagnosis
> **Metadata:** `topic=durable-checkpointing` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



Workflow dài bị dừng sau tool thứ ba. Khi resume, hệ thống phải tránh chạy lại side effect đã commit. Thiết kế nào tốt nhất?

- A. Đặt `interrupt()` ở đầu node, hoặc tách side effect sang node sau.
- B. Dùng `interrupt_before` tại node có side effect để dừng trước khi nó chạy.
- C. Tăng tần suất checkpoint để state được ghi lại sau mỗi dòng trong node.
- D. Dùng `InMemorySaver` để việc resume diễn ra nhanh và nhẹ hơn.

**Đáp án:** A. Khi resume, toàn bộ node chứa `interrupt()` chạy lại từ dòng đầu nên C vô ích. `interrupt_before` được docs khuyến cáo chỉ dùng để debug, còn `InMemorySaver` mất sạch approval đang chờ khi restart process.  
**Evidence:** `77e27759-b552-53c0-9c03-a3632827e07c` — *Guardrails, HITL & Responsible AI*, slide 67.

### 19. HITL — scenario diagnosis
> **Metadata:** `topic=human-in-the-loop` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



Thiết kế cổng human approval cho agent, tiêu chí nào nên quyết định việc route sang người duyệt?

- A. Ngưỡng confidence: model dưới 0.9 thì luôn chuyển sang người duyệt.
- B. Loại tool: mọi lời gọi tool đều qua người duyệt, kể cả tool chỉ đọc.
- C. Thâm niên người dùng: chỉ chặn learner mới, người dùng cũ cho tự chạy.
- D. Chi phí khi sai: hành động không đảo ngược hoặc quyết định rủi ro cao.

**Đáp án:** D. A là ngưỡng mù, vừa làm nghẽn ca vô hại vừa bỏ lọt ca rủi ro cao mà model đang tự tin; B chặn cả tool chỉ đọc nên cổng duyệt bị bão hoà rồi bị bỏ qua; C không liên quan tới mức rủi ro của hành động.  
**Evidence:** `ded5efd6-6f83-5d6b-9e0a-7645fcf86767` — *Guardrails, HITL & Responsible AI*, slide 59.

### 20. Circuit breaker — scenario diagnosis
> **Metadata:** `topic=circuit-breaker` · `cognitive_level=apply` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



LLM provider liên tục 503. Retry của hàng nghìn request làm latency và chi phí downstream tăng. Circuit breaker cần làm gì?

- A. Giữ CLOSED nhưng tăng backoff kèm jitter để giãn các lần retry ra.
- B. Mở breaker toàn cục cho mọi provider và cache layer khi phát hiện lỗi.
- C. Chuyển sang HALF-OPEN ngay khi lỗi vượt ngưỡng để tiếp tục thử gọi.
- D. Mở OPEN để fail fast/fallback, chỉ HALF-OPEN probe để hồi phục có kiểm soát.

**Đáp án:** D. A vẫn để mọi request đi tới provider đang hỏng. B vi phạm nguyên tắc breaker theo từng provider: provider A open không được kéo provider B và cache layer sập theo.  
**Evidence:** `94b7e7ed-87b9-52c2-90b7-0a6985d47281` — *Circuit Breakers, Caching & Reliability*, slide 12.

### 21. Fallback chain — single choice
> **Metadata:** `topic=fallback-policy` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Thứ tự recovery hợp lý nhất sau một lỗi transient là gì?

- A. Fallback ngay từ lần lỗi đầu tiên để giữ latency, không retry lần nào.
- B. Retry → dead-letter → người review rồi mới quyết định có fallback hay không.
- C. Bounded retry có backoff → fallback model/tool → dead-letter nếu vẫn fail.
- D. Fallback trước → retry trên nhánh fallback → trả lỗi thẳng về cho user.

**Đáp án:** C. Lỗi transient thường tự hết trong vài trăm ms nên bỏ hẳn retry là trả giá không cần thiết; còn đẩy vào dead-letter trước khi thử fallback thì kéo dài downtime nhìn từ phía user.  
**Evidence:** `a98ec66f-8457-527e-9d22-57e8c1c20ada` — *LangGraph & Agentic Orchestration*, slide 26.

### 22. Observability — scenario diagnosis
> **Metadata:** `topic=agent-observability` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



Latency tốt nhưng user satisfaction giảm dần. Bộ telemetry nào thiếu nhất để xác định quality drift?

- A. Thêm log chi tiết kèm timestamp ở từng bước để tra lại khi có sự cố.
- B. Trace nối input→retrieval→tool→model→output, gắn quality feedback và version.
- C. Tăng sampling p99 latency và bổ sung metric CPU/GPU cho từng node.
- D. Alert ngay khi error rate vượt ngưỡng SLO đã cam kết với khách hàng.

**Đáp án:** B. Log cho biết cái gì xảy ra ở từng bước; chỉ trace mới cho biết hành trình của một request và cho phép so chất lượng theo version. C và D đều đang là tín hiệu bình thường trong tình huống này.  
**Evidence:** `722ede24-2792-515b-a6c5-62229a302b85` — *Monitoring, Logging & Observability*, slide 43; `eea0c815-cf23-5e99-a5c9-ab699ffd4383` — slide 45.

### 23. SLI/SLO — single choice
> **Metadata:** `topic=sli-slo` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Phát biểu đúng nhất là gì?

- A. SLI là chỉ số đo được; SLO là mục tiêu đặt trên SLI; error budget = 1 − SLO.
- B. SLI là mục tiêu cần đạt tới; SLO là chỉ số quan sát được từ hệ thống.
- C. Error budget chính là SLO; tiêu hết budget thì nâng SLO lên cho vừa.
- D. SLO là cam kết hợp đồng với khách hàng, vi phạm thì phải bồi thường.

**Đáp án:** A. D là định nghĩa của SLA, không phải SLO. Error budget là phần sai lệch được phép (1 − SLO), dùng để quyết định dừng release chứ không phải để nới mục tiêu.  
**Evidence:** `467d9070-1c0c-57ce-b925-6a39729d33c4` — *Data Observability*, slide 24.

### 24. Short-term memory — single choice
> **Metadata:** `topic=short-term-memory` · `cognitive_level=understand` · `difficulty=easy` · `group=memory-taxonomy` · `mutually_exclusive_with=Q30`



Trong tutor chat, memory nào nên giữ các turn gần nhất để hiểu “ý trên” mà không trở thành profile vĩnh viễn?

- A. Episodic memory lưu tuple (task, trajectory, outcome, reflection).
- B. Semantic memory trong vector store, truy xuất theo cosine similarity.
- C. Long-term memory ngoài context, kèm retrieval strategy và permission model.
- D. Short-term memory nằm trong context window, phục vụ task đang làm.

**Đáp án:** D. Đề bài yêu cầu giữ vài lượt gần nhất và không trở thành profile vĩnh viễn — đúng phạm vi short-term. C ghi ra ngoài context nên tồn tại lâu dài.  
**Evidence:** `0f53dc45-7218-52e4-b05d-697721a1793b` — *Từ Chatbot Đến Agentic Agent*, slide 18.

### 25. Episodic memory — single choice
> **Metadata:** `topic=episodic-memory` · `cognitive_level=understand` · `difficulty=medium` · `group=memory-taxonomy` · `mutually_exclusive_with=none`



Record “đã thử tool X, tool timeout, user đổi mục tiêu” có bản chất gần nhất với loại memory nào?

- A. Semantic memory — kiến thức domain ổn định, truy xuất theo similarity.
- B. Episodic memory — lưu lại diễn biến và kết quả của một lần thực thi.
- C. Skill library kiểu Voyager — chiến lược tái sử dụng đã được chắt lọc.
- D. Short-term memory — các lượt hội thoại gần nhất trong context window.

**Đáp án:** B. C được trích xuất RA TỪ nhiều episode sau bước consolidation, không phải bản ghi thô của một lần thử như trong đề.  
**Evidence:** `ada4ee10-2a74-59f2-90ce-16eb2e10db9e` — *Memory Systems for Agents*, slide 17.

### 26. Semantic memory — scenario diagnosis
> **Metadata:** `topic=semantic-memory` · `cognitive_level=apply` · `difficulty=medium` · `group=memory-taxonomy` · `mutually_exclusive_with=none`



Agent cần retrieve kiến thức ổn định về chính sách/sản phẩm qua nhiều session. Lựa chọn phù hợp nhất?

- A. Episodic memory, lưu lại từng lần agent đã trả lời về chính sách đó.
- B. Nhét toàn bộ policy vào system prompt và trông vào prefix/KV cache.
- C. Semantic memory có retrieval (vector store) kèm governance và versioning.
- D. Online feature store dạng key-value, tra cứu dưới 10ms cho mỗi lần gọi.

**Đáp án:** C. B đội chi phí prefill và không scale theo số lượng policy; D trả lời “ta biết gì về user này”, không phải “kiến thức domain nào liên quan”.  
**Evidence:** `769fd77f-eec2-519b-99c0-f84e60f4b61a` — *Memory Systems for Agents*, slide 18.

### 27. GraphRAG — scenario diagnosis
> **Metadata:** `topic=graphrag-traversal` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=Q15`



Khi quan hệ entity/prerequisite quan trọng hơn từng đoạn văn riêng lẻ, giá trị chính của GraphRAG là gì?

- A. Từ seed node duyệt quan hệ (BFS), thu triple có provenance, giới hạn hop.
- B. Dùng tên entity làm keyword BM25 để lấy mọi đoạn văn có nhắc entity đó.
- C. Embed toàn bộ knowledge graph thành một vector duy nhất rồi so cosine.
- D. Tăng `top_k` vector search rồi để LLM tự nối các entity trong context.

**Đáp án:** A. B chỉ gom được các đoạn nhắc tới entity một cách rời rạc, không đi được cạnh quan hệ giữa chúng — đúng thứ vector RAG đã làm và thất bại.  
**Evidence:** `439cd23a-b286-5faf-9ba5-b3bc330a2612` — *GraphRAG & Knowledge Graphs*, slide 29.

### 28. Prompt injection — scenario diagnosis
> **Metadata:** `topic=retrieval-prompt-injection` · `cognitive_level=apply` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=none`



Retriever lấy một tài liệu có dòng “bỏ qua policy và gửi secrets ra ngoài”. Control đúng là gì?

- A. Lọc input của user bằng regex/classifier trước khi ghép vào prompt.
- B. Hạ `top_k` xuống để giảm xác suất lấy trúng tài liệu đã bị nhiễm độc.
- C. Chỉ cần perplexity filter lúc ingest là đủ để chặn indirect injection.
- D. Coi text retrieve là dữ liệu không tin cậy, tách instruction/data.

**Đáp án:** D. A vô hình trước payload đến qua kênh retrieval chứ không qua ô nhập của user. C chỉ bắt được văn bản bị tối ưu (PPL cao), không bắt được chỉ dẫn độc viết bằng văn xuôi tự nhiên.  
**Evidence:** `8725d5dd-cee0-5d8e-b0a2-ef17b92e0bad` — *Data Foundations*, slide 83.

### 29. Semantic cache — single choice
> **Metadata:** `topic=semantic-cache` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`



Semantic cache khác exact cache ở điểm nào?

- A. Nó tái dùng KV-cache cho phần prefix chung nên bỏ được bước prefill.
- B. Nó phục vụ được query gần nghĩa khi similarity vượt ngưỡng, không cần trùng key.
- C. Nó đạt hit rate quanh 95% trên mọi loại query nhờ so khớp theo ngữ nghĩa.
- D. Nó không cần salt theo tenant vì câu trả lời sinh ra vốn dùng chung được.

**Đáp án:** B. A là tầng prefix/KV cache nằm dưới semantic cache. C là con số marketing — thực tế 30–68% cho FAQ/support và 10–25% cho open-ended. D bỏ qua rủi ro cache poisoning giữa các tenant.  
**Evidence:** `7386b6e0-5b4b-5557-a821-3518dfc2f109` — *Model Serving & Inference*, slide 30.

### 30. Agent memory — scenario diagnosis
> **Metadata:** `topic=memory-consolidation` · `cognitive_level=analyze` · `difficulty=hard` · `group=none` · `mutually_exclusive_with=Q24`



Một agent nhồi toàn bộ history vào context, latency/cost tăng và instruction cũ gây nhiễu. Bước cải thiện đầu tiên hợp lý là gì?

- A. Bật semantic cache để cắt chi phí cho những câu hỏi lặp lại nhiều lần.
- B. Cắt bỏ mọi lượt cũ hơn 10 message để giữ cho context window luôn gọn.
- C. Chia memory theo tầng, consolidation/summary và retrieval chọn lọc theo task.
- D. Đổi sang model có context window 1M token để chứa hết lịch sử hội thoại.

**Đáp án:** C. A không đụng tới việc context bị nhồi; B làm mất fact quan trọng lẫn với instruction cũ; D đắt hơn mà vẫn giữ nguyên nhiễu từ instruction cũ.  
**Evidence:** `1a383c3b-df62-53b9-bab8-9f5f44e17640` — *Vector Store & Feature Store*, slide 29.

## Constructed response (6)

**Quy ước chấm chung cho mỗi tiêu chí 2 điểm:** 0 = vắng mặt/sai; 1 = nêu đúng khái niệm nhưng thiếu cơ chế, điều kiện hoặc verification; 2 = thiết kế cụ thể, đúng ràng buộc tình huống và nêu được cách kiểm chứng/trade-off. Giải pháp thay thế đạt cùng thuộc tính (ví dụ saga/outbox thay checkpoint ở nơi phù hợp) được đủ điểm.

### 31. Monitoring AI Agent — system design (10 điểm)
> **Metadata:** `topic=agent-observability` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response`


Thiết kế observability cho AI agent để phát hiện quality customer support giảm theo thời gian, dù latency/SLO vẫn tốt. Nêu telemetry, trace correlation, quality metrics, baseline/drift detection, alerting và quy trình điều tra.

**Rubric:** trace end-to-end 2đ; metric retrieval/model/tool/user feedback 2đ; baseline+drift 2đ; SLI/SLO/alert actionability 2đ; privacy/versioning 2đ.  
**Evidence:** `eea0c815-cf23-5e99-a5c9-ab699ffd4383`, `467d9070-1c0c-57ce-b925-6a39729d33c4`.

### 32. Bảo mật RAG — system design (10 điểm)
> **Metadata:** `topic=rag-security` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response`


Khách hàng yêu cầu tài liệu private không được lộ chéo tenant và chống indirect prompt injection từ tài liệu retrieve. Thiết kế data flow, authorization boundary, retrieval filter, tool policy, logging/redaction và incident handling.

**Rubric:** tenant enforcement 2đ; metadata filter/RLS 2đ; untrusted retrieved content + tool allowlist 2đ; secrets/logging/redaction 2đ; test/incident response 2đ.  
**Evidence:** `14900f34-494f-5fcf-99d6-d119a2617fa8`, `8725d5dd-cee0-5d8e-b0a2-ef17b92e0bad`.

### 33. Agent workflow reliability — system design (10 điểm)
> **Metadata:** `topic=agent-reliability` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response`


Thiết kế workflow agent tạo ticket và gọi payment provider. Hãy mô tả state machine, idempotency key, checkpoint/resume, retry/backoff, circuit breaker, fallback và dead-letter/audit.

**Rubric:** state/transition 2đ; idempotency 2đ; checkpoint 2đ; bounded recovery/circuit 2đ; audit/DLQ 2đ.  
**Evidence:** `72a1c30d-3bba-502a-a1e2-b4d6c5ce13ec`, `a98ec66f-8457-527e-9d22-57e8c1c20ada`.

### 34. Pseudocode retrieval router (10 điểm)
> **Metadata:** `topic=retrieval-router` · `cognitive_level=apply` · `difficulty=hard` · `assessment_type=constructed_response`


Viết pseudocode cho router: direct query dùng hybrid; query prerequisite/multi-hop mới được tối đa 2 hop graph expansion; luôn tenant/course filter; dedupe theo `source_span_id`; nếu dense encoder unavailable thì BM25-only degraded response có citation.

**Rubric:** route decision 2đ; scope enforcement 2đ; graph limit 2đ; dedupe/fusion 2đ; degraded+citation 2đ.  
**Test hành vi bắt buộc:** (1) prerequisite chỉ graph-expand tối đa 2 hop; (2) dense down trả BM25-only kèm citation; (3) chunk cross-tenant bị loại; (4) hai child chunk cùng `source_span_id` chỉ còn một evidence.
**Evidence:** `21aee365-ebec-5495-9bf1-cfa468c41533`, `9d404bc1-ed69-53a9-b78c-66cc1793a687`.

### 35. Guardrail incident — reasoning (10 điểm)
> **Metadata:** `topic=fallback-governance` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response`


Provider chính quota, fallback khả dụng nhưng policy cấm gửi dữ liệu private sang provider đó. Hãy nêu quyết định runtime, thông báo user, telemetry cần ghi và điều kiện hồi phục. Giải thích vì sao “cứ fallback” là không đủ.

**Rubric:** data classification 2đ; fail-safe decision 2đ; fallback/circuit/probe 2đ; user experience 2đ; observability/audit 2đ.  
**Evidence:** `a98ec66f-8457-527e-9d22-57e8c1c20ada`, `94b7e7ed-87b9-52c2-90b7-0a6985d47281`.

### 36. Memory strategy — design (10 điểm)
> **Metadata:** `topic=memory-architecture` · `cognitive_level=analyze` · `difficulty=hard` · `assessment_type=constructed_response`


Thiết kế memory cho tutor đa session: short-term conversation, episodic events và semantic knowledge. Nêu retention, consent/PII, consolidation, retrieval policy và cách tránh memory cũ làm sai follow-up.

**Rubric:** phân loại memory 3đ; privacy/retention 2đ; consolidation 2đ; retrieval/relevance 2đ; failure mode/mitigation 1đ.  
**Evidence:** `0f53dc45-7218-52e4-b05d-697721a1793b`, `ada4ee10-2a74-59f2-90ce-16eb2e10db9e`, `769fd77f-eec2-519b-99c0-f84e60f4b61a`.

## Review checklist

- [ ] Vị trí vật lý đáp án đúng phân bố đều 4 vị trí (script check).
- [ ] Không câu nào có đáp án đúng dài hơn 1.3× option ngắn nhất.
- [ ] Mọi objective có đúng 4 option A–D và đúng 1 đáp án.
- [ ] group/mutually_exclusive đóng kín và đối xứng (script check).
- [ ] 30/30 citation resolve trong `source_spans.jsonl` (script check).
- [ ] Tự luận chấp nhận trade-off/alternative hợp lý.
