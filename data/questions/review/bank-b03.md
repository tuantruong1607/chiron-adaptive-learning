# Chiron AI — Question Bank B-03 (human-authored)

**Trạng thái:** Candidate for expert review. Không publish, không dùng để chấm learner.
**Phạm vi:** 14 objective, soạn tay theo `docs/QUESTION_AUTHORING_CONTRACT.md`.
**Mục tiêu quota:** bù recall/easy/single_choice đang thiếu nặng sau B-01+B-02 (xem báo cáo kèm theo).
**Không trùng batch trước:** mọi `source_span_id` chưa được `pilot-v1.md` hay `bank-b02.md` dùng.

## Objective questions (14)

### 1. Ba loại evaluation — single choice
> **Metadata:** `topic=evaluation-types` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Loại evaluation nào chạy liên tục trên traffic thật của production, không phải trên golden dataset?

- A. Offline evaluation.
- B. Human evaluation.
- C. Online evaluation.
- D. A/B testing evaluation.

**Đáp án:** C. Offline chạy batch trên golden dataset mỗi release; human evaluation là expert review theo mẫu hàng tuần. Chỉ online mới theo dõi continuous trên real traffic.  
**Evidence:** `df0c48dd-5a3f-569d-b2da-e8a5b7e4334f` — *AI Evaluation & Benchmarking*, slide 10.

### 2. Chỉ dùng một loại eval — scenario diagnosis
> **Metadata:** `topic=evaluation-types` · `cognitive_level=analyze` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một team chỉ chạy offline evaluation trên golden dataset trước mỗi release, không có gì khác. Rủi ro chính là gì?

- A. Golden dataset sẽ nhanh chóng bị data contamination do dùng lại nhiều lần.
- B. Không biết được chất lượng thực tế đang diễn ra trên production.
- C. RAGAS không tương thích với việc chạy offline theo batch.
- D. Human reviewer sẽ không còn việc gì để làm trong quy trình.

**Đáp án:** B. A là rủi ro thật của golden dataset nhưng không phải hệ quả của việc thiếu online eval. Chỉ offline eval không cho biết chất lượng đang trôi dạt thế nào khi gặp traffic thật, đó là lý do bài học yêu cầu kết hợp cả ba loại.  
**Evidence:** `df0c48dd-5a3f-569d-b2da-e8a5b7e4334f` — *AI Evaluation & Benchmarking*, slide 10.

### 3. Công thức faithfulness — single choice
> **Metadata:** `topic=faithfulness-formula` · `cognitive_level=recall` · `difficulty=easy` · `group=ragas-formula` · `mutually_exclusive_with=none`

Faithfulness được tính bằng công thức nào?

- A. Số claims trong answer được context support, chia tổng số claims trong answer.
- B. Số chunks relevant trong top-k, chia tổng số chunk đã retrieve.
- C. Cosine similarity trung bình giữa câu hỏi gốc và các câu hỏi reverse.
- D. Số claims trong ground truth có mặt trong context, chia tổng claims ground truth.

**Đáp án:** A. B mô tả context precision, C mô tả answer relevancy, D mô tả context recall — cả ba đều là công thức thật trong cùng bài nhưng của metric khác.  
**Evidence:** `9b80c195-80d5-542e-9322-9a0aeb2d5e94` — *AI Evaluation & Benchmarking*, slide 19.

### 4. Faithfulness không đo gì — scenario diagnosis
> **Metadata:** `topic=faithfulness-formula` · `cognitive_level=analyze` · `difficulty=hard` · `group=ragas-formula` · `mutually_exclusive_with=none`

Context của một RAG chứa thông tin sai từ nguồn gốc, nhưng answer bám sát đúng context đó. Faithfulness score sẽ ra sao?

- A. Faithfulness vẫn cao, vì nó chỉ đo grounded vào context, không đo sự thật.
- B. Faithfulness thấp, vì claim sai sẽ luôn bị đánh dấu không được support.
- C. Faithfulness không tính được vì context bị sai ngay từ khi ingest.
- D. Faithfulness sẽ tự động cộng thêm điểm context precision để bù trừ.

**Đáp án:** A. Faithfulness chỉ kiểm claim có được context support hay không, không kiểm context đó đúng sự thật hay chưa — nên context sai mà answer bám sát vẫn cho faithfulness cao. Đây là giới hạn của metric, không phải lỗi tính toán.  
**Evidence:** `9b80c195-80d5-542e-9322-9a0aeb2d5e94` — *AI Evaluation & Benchmarking*, slide 19.

### 5. Answer relevancy — công thức — single choice
> **Metadata:** `topic=answer-relevancy-formula` · `cognitive_level=recall` · `difficulty=medium` · `group=ragas-formula` · `mutually_exclusive_with=none`

RAGAS tính Answer Relevancy bằng cách nào?

- A. Đếm claim trong answer có mặt trong context, chia tổng số claim đó.
- B. Cho LLM sinh nhiều câu hỏi ngược từ answer, đo cosine với câu hỏi gốc.
- C. Đếm số chunk liên quan trong top-k rồi chia đều cho k.
- D. Cho hai LLM chấm điểm answer song song rồi lấy trung bình.

**Đáp án:** B. A là công thức context recall, C là context precision — cùng nằm trong bộ bốn metric RAGAS nhưng đo thứ khác. Answer relevancy dùng reverse question generation rồi so cosine với câu hỏi gốc.  
**Evidence:** `1993b471-cb06-52da-b98e-35720b07f5dc` — *AI Evaluation & Benchmarking*, slide 20.

### 6. Golden dataset — single choice
> **Metadata:** `topic=golden-dataset` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Theo hướng dẫn xây golden dataset cho production, cỡ tối thiểu hợp lý là bao nhiêu?

- A. 5–10 cặp câu hỏi, miễn có đủ expert review kỹ.
- B. 20 cặp câu hỏi, dùng chung cho lab và production.
- C. 50–100 cặp câu hỏi, expert viết, ít nhất hai người review.
- D. Càng nhiều càng tốt, không có ngưỡng dưới tối thiểu.

**Đáp án:** C. Dưới 20 test case được nói rõ là quá ít để kết luận có ý nghĩa thống kê; 20 chỉ đủ cho lab, còn production cần 50–100 với rule ít nhất hai expert review mỗi câu.  
**Evidence:** `5dbe408a-509c-5a17-b34a-cd694d2d5dac` — *AI Evaluation & Benchmarking*, slide 24.

### 7. LLM-as-Judge bias — scenario diagnosis
> **Metadata:** `topic=llm-judge-bias` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một judge dựa trên GPT-4 liên tục chấm output của chính GPT-4 cao hơn output tương đương của model khác. Đây là bias nào và cách fix đúng?

- A. Verbosity bias; fix bằng cách thêm rubric yêu cầu câu trả lời ngắn gọn.
- B. Position bias; fix bằng cách đảo ngẫu nhiên thứ tự hai câu trả lời.
- C. Self-preference bias; fix bằng cách dùng judge khác family model.
- D. Authority bias; fix bằng cách bỏ khung “Expert said” khỏi câu trả lời.

**Đáp án:** C. A, B, D đều là bias thật trong cùng danh sách nhưng mô tả triệu chứng khác: dài hơn được điểm cao (verbosity), ưu tiên câu trả lời xuất hiện trước (position), bị ấn tượng bởi khung uy quyền (authority). Judge thiên vị output từ cùng họ model là self-preference.  
**Evidence:** `a82a5bcf-4030-5b08-86d0-784423f24fac` — *AI Evaluation & Benchmarking*, slide 40.

### 8. Vì sao cần chunking — single choice
> **Metadata:** `topic=chunking-rationale` · `cognitive_level=understand` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Dù model đã hỗ trợ context window vài triệu token, vì sao vẫn cần chunking tài liệu trước khi đưa vào vector search?

- A. Vì context window dài vẫn luôn rẻ hơn khi nhét nguyên văn bản vào prompt.
- B. Vì nhúng cả một chương vào một vector làm loãng ý chính, khó khớp câu hỏi cụ thể.
- C. Vì hầu hết vector database từ chối nhận input dài hơn một ngưỡng cố định.
- D. Vì LLM sẽ tự động bỏ qua phần văn bản nằm ngoài 4.000 token đầu tiên.

**Đáp án:** B. A ngược với lý do thật: nhét nguyên văn bản vào prompt đắt và chậm hơn, không rẻ hơn. Chunking giải quyết bài toán mật độ ý nghĩa của vector search, không phải giới hạn kỹ thuật của DB hay của model.  
**Evidence:** `47619d4d-8fc1-52f4-9843-dc09b49bd1fd` — *RAG Pipeline*, slide 27.

### 9. Overlap giữa các chunk — single choice
> **Metadata:** `topic=chunk-overlap` · `cognitive_level=understand` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Overlap giữa hai chunk liền kề giải quyết vấn đề gì?

- A. Giảm tổng số chunk cần lưu trữ trong vector database.
- B. Tăng tốc độ embedding vì chunk có phần trùng nhau xử lý nhanh hơn.
- C. Giữ mạch ngữ cảnh cho một ý bị cắt ngang qua ranh giới hai chunk.
- D. Cho phép reranker so sánh trực tiếp hai chunk liền kề với nhau.

**Đáp án:** C. Một ý quan trọng có thể vô tình bị chia làm hai mảnh nằm ở mép của hai chunk; overlap cho đoạn cuối chunk trước lặp lại ở đầu chunk sau, hoạt động như chất keo giữ mạch ngữ cảnh. Nó không giảm số chunk hay đổi tốc độ embedding.  
**Evidence:** `bafd4302-ec2a-5f52-abd9-fc45c26799dc` — *RAG Pipeline*, slide 31.

### 10. Vấn đề của top-K — scenario diagnosis
> **Metadata:** `topic=top-k-limitation` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Query "thủ tục xin visa" trả về top-8 kết quả, nhưng đoạn chứa đúng các bước thủ tục nằm ở vị trí thứ 8 chứ không phải thứ 1. Đây là biểu hiện của vấn đề gì?

- A. Retriever quét thô và rộng nên tài liệu đúng có thể chìm sâu.
- B. Chunking sai nên tài liệu đúng bị cắt rời khỏi phần chứa từ khoá "visa".
- C. Embedding model chưa fine-tune trên domain hành chính công.
- D. Overlap giữa chunk quá thấp nên chunk thứ 8 bị lạc chủ đề.

**Đáp án:** A. Retriever được thiết kế để đánh giá liên quan một cách thô và rộng trên hàng triệu tài liệu, nên tài liệu đúng nhất có thể nằm ở top-10 chứ không phải top-1 — đây là đặc tính vốn có, không phải lỗi chunking hay embedding.  
**Evidence:** `df099fed-7427-5f92-ac2f-fbfb17aef822` — *RAG Pipeline*, slide 74.

### 11. MMR — single choice
> **Metadata:** `topic=mmr-diversity` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

MMR (Maximum Marginal Relevance) tối ưu hoá điều gì khi chọn chunk?

- A. Chỉ tối đa hoá độ liên quan với query, bỏ qua các chunk đã chọn trước đó.
- B. Tối đa hoá liên quan với query, đồng thời phạt nặng sự trùng lặp với chunk đã chọn.
- C. Tối thiểu hoá khoảng cách vector giữa các chunk được chọn với nhau.
- D. Chọn ngẫu nhiên trong top-K sau khi đã lọc theo ngưỡng similarity.

**Đáp án:** B. A mô tả retrieval thường, chưa phải MMR. Công thức MMR trừ đi một penalty tỉ lệ với similarity giữa candidate và các chunk đã chọn, nên nó chủ động đẩy các chunk được chọn ra xa nhau — ngược với C.  
**Evidence:** `76d94cb2-d8fd-5dc3-8451-3d506b3cc82f` — *RAG Pipeline*, slide 79.

### 12. HNSW vs IVF vs DiskANN — scenario diagnosis
> **Metadata:** `topic=ann-index-choice` · `cognitive_level=apply` · `difficulty=medium` · `group=ann-index` · `mutually_exclusive_with=none`

Một hệ thống cần index hơn 100 triệu vector, ưu tiên chi phí thấp hơn latency cực nhỏ. Lựa chọn ANN index nào phù hợp nhất?

- A. HNSW, vì recall 95%+ ở khoảng 10ms là mức tốt nhất có thể đạt.
- B. IVF, vì cluster-based index luôn rẻ hơn graph-based index ở mọi quy mô.
- C. DiskANN, vì rẻ hơn HNSW 10–50 lần ở quy mô lớn nhờ chạy trên SSD.
- D. Không index nào phù hợp; phải chuyển sang brute-force full scan.

**Đáp án:** C. HNSW là lựa chọn tốt nhưng bị giới hạn bởi RAM ở quy mô dưới 10M vector, không phù hợp với 100M+. B khẳng định sai — IVF chỉ tốt hơn cho batch-mode và corpus tĩnh, không phải "mọi quy mô". DiskANN được thiết kế đúng cho billion-scale với chi phí thấp hơn nhiều.  
**Evidence:** `34814a5b-3709-52a7-b847-d635496d34a1` — *Vector Store & Feature Store*, slide 16.

### 13. Quantization — scenario diagnosis
> **Metadata:** `topic=vector-quantization` · `cognitive_level=apply` · `difficulty=medium` · `group=ann-index` · `mutually_exclusive_with=none`

Một team cần giảm RAM lưu vector nhiều nhất có thể và chấp nhận đánh đổi một phần recall. Nên chọn hướng nào?

- A. Binary quantization, giảm RAM 32 lần, chấp nhận recall còn 95–98%.
- B. int8 scalar quantization, vì đây là lựa chọn tiết kiệm RAM nhiều nhất.
- C. Giữ nguyên float32, chỉ giảm số chiều embedding để tiết kiệm RAM.
- D. Asymmetric quantization, vì nó luôn rẻ hơn binary quantization thuần.

**Đáp án:** A. B chỉ tiết kiệm 4 lần, ít hơn nhiều so với binary. D mô tả sai: asymmetric là "best of both" giữa lưu trữ rẻ và query chính xác, không hẳn rẻ hơn binary thuần — nó đánh đổi khác, không phải luôn thắng về chi phí lưu trữ.  
**Evidence:** `9dc2a872-5857-5c0f-9195-889453df8218` — *Vector Store & Feature Store*, slide 17.

### 14. Filtered search — scenario diagnosis
> **Metadata:** `topic=filtered-search` · `cognitive_level=analyze` · `difficulty=hard` · `group=ann-index` · `mutually_exclusive_with=none`

Một hệ RAG áp metadata filter khớp khoảng 1% corpus. Sau khi lọc, recall sập mạnh mà không có lỗi nào được log. Nguyên nhân nhiều khả năng nhất là gì?

- A. Metadata field sai kiểu dữ liệu nên filter không khớp gì cả.
- B. Đang dùng post-filter: ANN lấy top-100 rồi mới lọc, lọc chặt còn rất ít.
- C. Vector database đang quá tải nên trả về kết quả không đầy đủ.
- D. Threshold similarity đặt quá cao nên kết quả bị loại trước khi lọc.

**Đáp án:** B. Post-filter xin top-100 rồi lọc sau; filter khớp 1% có thể chỉ còn 1 kết quả từ 100, và càng lọc chặt càng tệ — đúng cơ chế "recall sập không báo lỗi". Filtered-ANN đúng cách sẽ để index tự biết filter, tránh chính vấn đề này.  
**Evidence:** `539e30fa-539e-5578-8e68-7449fa7c0eb5` — *Vector Store & Feature Store*, slide 19.

## Review checklist

- [ ] Vị trí vật lý đáp án đúng phân bố đều 4 vị trí (script check).
- [ ] Không câu nào có đáp án đúng dài hơn 1.3× option ngắn nhất.
- [ ] Mỗi câu đúng 4 option và đúng 1 đáp án.
- [ ] group/mutually_exclusive đóng kín và đối xứng (script check).
- [ ] Mọi citation resolve trong `source_spans.jsonl` (script check).
- [ ] Đã chạy §2 của `QUESTION_REVIEW_PROTOCOL.md` (đáp án thứ hai, evidence trả lời được stem).
