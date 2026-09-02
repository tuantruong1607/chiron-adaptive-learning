# Chiron AI — Question Bank B-04 (human-authored)

**Trạng thái:** Candidate for expert review. Không publish, không dùng để chấm learner.
**Phạm vi:** 14 objective, soạn tay theo `docs/QUESTION_AUTHORING_CONTRACT.md`.
**Mục tiêu quota:** recall/easy/understand/apply — không thêm analyze/hard (đã đủ quota sau B-01..B-03).
**Không trùng batch trước:** mọi `source_span_id` chưa được các batch trước dùng.

## Objective questions (14)

### 1. Cosine similarity — myth — single choice
> **Metadata:** `topic=cosine-similarity-myth` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Nghiên cứu Steck, Ekanadham & Kallus (WWW 2024) kết luận gì về cosine similarity của embedding đã học?

- A. Cosine similarity luôn là lựa chọn tối ưu cho mọi embedding model hiện đại.
- B. Cosine similarity có thể cho kết quả tuỳ tiện và vô nghĩa với linear model regularized.
- C. Cosine similarity chỉ sai khi dùng cho văn bản tiếng Việt chưa chuẩn hoá.
- D. Cosine similarity luôn tốt hơn dot product chưa chuẩn hoá trong mọi trường hợp.

**Đáp án:** B. Cosine là một convention hiệu quả, không phải sự thật về ý nghĩa — nghiên cứu chỉ ra một số trường hợp cosine còn tệ hơn dot product chưa chuẩn hoá, ngược hẳn với D.  
**Evidence:** `cff3bf02-c83e-5fa7-b334-727f58378cc5` — *Data Foundations*, slide 20.

### 2. Asymmetric search — scenario diagnosis
> **Metadata:** `topic=asymmetric-search` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một hệ RAG dùng E5 embedding nhưng không thêm prefix `query:` / `passage:` khi encode. Hệ quả là gì?

- A. Model sẽ báo lỗi ngay lập tức vì thiếu tham số bắt buộc.
- B. Không có gì thay đổi vì prefix chỉ ảnh hưởng tốc độ encode.
- C. Embedding lệch calibration âm thầm, khiến xếp hạng sai mà không báo lỗi.
- D. Retrieval sẽ chuyển tự động sang chế độ symmetric search.

**Đáp án:** C. Bỏ prefix không báo lỗi — nó âm thầm tạo ra embedding lệch calibration và xếp hạng sai. Model không tự chuyển chế độ hay báo lỗi; nó vẫn chạy nhưng cho kết quả tệ hơn.  
**Evidence:** `57af8aed-6f00-5c8f-aab7-30c7d7a71bf7` — *Data Foundations*, slide 21.

### 3. Chunking bảng biểu — single choice
> **Metadata:** `topic=table-chunking` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Khi chunker cắt một bảng theo ký tự thông thường, chuyện gì xảy ra với quan hệ hàng–cột?

- A. Header và giá trị có thể rơi vào hai chunk khác nhau, khó ghép lại đúng.
- B. Quan hệ hàng–cột được giữ nguyên nhờ Unicode table markers.
- C. Bảng tự động được chuyển thành Markdown table trước khi chunk.
- D. Chunker sẽ từ chối cắt bảng và giữ nguyên toàn bộ trong một chunk.

**Đáp án:** A. Đây là "điểm hỏng im lặng số một": header "Doanh thu Q2 2026" có thể rơi vào chunk này, giá trị "4,2 tỷ" rơi vào chunk khác — mất quan hệ mà không có cách nào ở tầng retrieval khôi phục lại.  
**Evidence:** `453e8f31-ffea-56e9-8db5-f33d22b9029a` — *Data Foundations*, slide 37.

### 4. Chunk quá to hay quá nhỏ — single choice
> **Metadata:** `topic=chunk-size-tradeoff` · `cognitive_level=understand` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Chunk dưới 50 token thường gây hậu quả gì khi retrieve?

- A. Mất ngữ cảnh, phải retrieve nhiều mảnh rời rạc mới đủ thông tin.
- B. Retrieve trúng nhưng context bị nhiễu vì dính nhiều chủ đề.
- C. Chunk quá nhỏ khiến vector database từ chối index hoàn toàn.
- D. Không ảnh hưởng gì vì chunk nhỏ luôn tăng precision của retrieval.

**Đáp án:** A. B là hệ quả của chunk quá to (>1000 token), không phải quá nhỏ. Chunk quá nhỏ làm mất ngữ cảnh và bắt hệ thống phải ghép nhiều mảnh rời rạc mới ra câu trả lời đầy đủ.  
**Evidence:** `216858ca-ab76-5147-841a-83b8e4703841` — *Data Foundations*, slide 42.

### 5. Vì sao 512 token — single choice
> **Metadata:** `topic=chunk-size-512` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Con số "512 token" từng phổ biến trong tutorial RAG có nguồn gốc từ đâu?

- A. Giới hạn cứng của bảng positional embedding trong kiến trúc BERT năm 2018.
- B. Kết quả benchmark tối ưu trên tập dữ liệu retrieval đa ngôn ngữ BEIR.
- C. Khuyến nghị chính thức từ tài liệu kỹ thuật của OpenAI cho mọi embedding model.
- D. Giới hạn băng thông mạng khi truyền vector qua API vector database.

**Đáp án:** A. Đây là giới hạn kiến trúc của một model cụ thể ra đời 2018, không phải một quy luật retrieval — nó sống sót qua vô số tutorial như một "default" lâu hơn hẳn lý do kỹ thuật ban đầu, dù embedder hiện đại đã vượt xa con số này.  
**Evidence:** `d84631a2-96f0-5da5-9ba4-40c76fbca01c` — *Data Foundations*, slide 43.

### 6. Filter làm sập recall — scenario diagnosis
> **Metadata:** `topic=filter-recall-collapse` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Trên pgvector, một truy vấn xin 15 nearest neighbour có filter per-tenant chỉ trả về 11 dòng, không có exception, không có log lỗi. Cơ chế nào giải thích đúng nhất?

- A. Post-filter chạy ANN trên toàn corpus rồi loại bỏ chunk không khớp, có thể mất recall âm thầm.
- B. Pre-filter thu hẹp tập con trước rồi mới search, luôn cho kết quả chính xác tuyệt đối.
- C. In-algorithm traversal đã tự nhận biết filter nên không thể xảy ra tình huống này.
- D. Đây là bug của riêng pgvector, các vector database khác không gặp vấn đề này.

**Đáp án:** A. B mô tả đúng pre-filter nhưng nó cho kết quả đúng (dù suy biến hiệu năng), không giải thích được triệu chứng thiếu dòng không báo lỗi. Cơ chế `hnsw.iterative_scan` tồn tại để vá lỗi post-filter này nhưng mặc định đang tắt — đây không phải bug riêng của một DB.  
**Evidence:** `1a3da951-5e82-5cb5-9565-cadc14194465` — *Data Foundations*, slide 65.

### 7. RRF — single choice
> **Metadata:** `topic=rrf-formula` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

RRF (Reciprocal Rank Fusion) hợp nhất kết quả của các retriever dựa trên đại lượng nào?

- A. Điểm số thô (raw score) đã được chuẩn hoá về cùng một thang đo.
- B. Trung bình cộng của cosine similarity và điểm BM25.
- C. Thứ hạng (rank) của tài liệu trong từng danh sách kết quả.
- D. Số lần một tài liệu xuất hiện trong top-1 của mỗi retriever.

**Đáp án:** C. RRF fuse theo vị trí rank, không theo score thô — chính vì vậy nó né được bài toán chuẩn hoá score chéo hệ giữa BM25 và cosine, thứ mà A và B đều đòi hỏi phải giải quyết trước.  
**Evidence:** `bfb2240d-e03f-5eb2-bbbf-62947ef4d6c2` — *Data Foundations*, slide 69.

### 8. PII trước khi embed — single choice
> **Metadata:** `topic=pii-masking` · `cognitive_level=understand` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Vì sao cần mask PII trước khi embed, thay vì mask sau khi đã lưu vào vector store?

- A. Vì vector database không cho phép xoá hoặc sửa dữ liệu sau khi đã index.
- B. Vì việc mask sau khi embed sẽ làm tăng đáng kể độ trễ truy vấn.
- C. Embedding có thể bị đảo ngược gần đúng, nên vector không phải dữ liệu ẩn danh.
- D. Vì các quy định pháp lý chỉ áp dụng cho dữ liệu ở dạng văn bản thô.

**Đáp án:** C. Nghiên cứu được trích dẫn (Morris et al., EMNLP 2023) cho thấy embedding không phải dữ liệu đã ẩn danh — nó có thể bị đảo ngược gần đúng nguyên văn, nên PII phải bị mask từ trước khi embed, không phải xử lý sau.  
**Evidence:** `100b1e8e-2a8b-5317-a825-da3e65b24f78` — *Data Foundations*, slide 9.

### 9. ETL vs ELT — single choice
> **Metadata:** `topic=etl-vs-elt` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Theo xu hướng pipeline hiện đại trên cloud lakehouse, mô hình nào là mặc định và vì sao?

- A. ETL, vì transform trước khi load luôn an toàn hơn cho dữ liệu nhạy cảm.
- B. EtLT, vì đây là chuẩn duy nhất được các nhà cung cấp cloud khuyến nghị.
- C. ELT, vì compute trên lakehouse rẻ nên transform thực hiện tại chỗ sau khi load raw.
- D. Không có mặc định cố định; lựa chọn hoàn toàn tuỳ ý theo sở thích riêng của đội ngũ.

**Đáp án:** C. ETL vẫn có chỗ đứng cho việc mask PII trước khi load hoặc khi compute yếu, nhưng đó là ngoại lệ chứ không phải mặc định. Thực tế phần lớn pipeline là EtLT — extract-time transform nhẹ rồi heavy transform trong warehouse — chứ không phải một chuẩn cứng nhắc.  
**Evidence:** `e6ac0ab6-bc2a-54f2-ac11-46d8ac48229b` — *Data Pipeline Engineering*, slide 9.

### 10. CDC — single choice
> **Metadata:** `topic=change-data-capture` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

CDC (Change Data Capture) log-based hoạt động bằng cách nào?

- A. Query định kỳ toàn bộ bảng rồi so sánh khác biệt với lần trước.
- B. Chỉ theo dõi cột `updated_at` để lọc bản ghi mới thay đổi.
- C. Yêu cầu ứng dụng gọi webhook mỗi khi có thay đổi dữ liệu.
- D. Đọc transaction log của database để stream mọi insert/update/delete.

**Đáp án:** D. B mô tả cursor-based incremental extract, một pattern khác nhẹ hơn nhưng không bắt được delete. CDC log-based đọc trực tiếp transaction log nên bắt được cả delete, độ trễ thấp và không tải nặng DB nguồn.  
**Evidence:** `425c3062-836d-560e-bb48-4a6540708fff` — *Data Pipeline Engineering*, slide 13.

### 11. Dead-letter queue — scenario diagnosis
> **Metadata:** `topic=dlq-triage` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một bản ghi vào pipeline bị thiếu trường bắt buộc do lỗi schema ở nguồn, cần kỹ sư sửa tay rồi mới xử lý lại được. Bản ghi này thuộc nhóm DLQ nào?

- A. Retriable — hệ thống sẽ tự động replay sau một khoảng thời gian ngắn.
- B. Không thuộc nhóm nào vì lỗi schema không đi qua validation gate.
- C. Poison — không bao giờ được xử lý, chỉ archive và gửi alert.
- D. Fixable — cần kỹ sư sửa schema hoặc dữ liệu thiếu rồi mới replay lại.

**Đáp án:** D. Retriable dành cho lỗi transient tự hết; Poison dành cho bản ghi không bao giờ qua được, chỉ archive. Lỗi schema thiếu trường cần con người can thiệp sửa rồi mới replay được, đúng định nghĩa Fixable.  
**Evidence:** `b7f32b8d-30cb-5d4c-9e75-24b6d8e87fe3` — *Data Pipeline Engineering*, slide 30.

### 12. Idempotency trong pipeline — single choice
> **Metadata:** `topic=pipeline-idempotency` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một pipeline batch cần an toàn khi bị chạy lại nhiều lần mà không nhân đôi dữ liệu. Pattern idempotent phù hợp là gì?

- A. Append thêm dữ liệu mới vào cuối bảng ở mỗi lần chạy.
- B. Chỉ ghi log mà không thực sự ghi dữ liệu khi phát hiện trùng lặp.
- C. Tăng tần suất chạy pipeline để giảm khối lượng mỗi lần ghi.
- D. Overwrite-partition: ghi đè cửa sổ dữ liệu thay vì append thêm.

**Đáp án:** D. A chính là cách gây nhân đôi rows khi replay — ngược hẳn với yêu cầu idempotent. Overwrite-partition ghi đè toàn bộ cửa sổ đang reprocess, nên chạy lại bao nhiêu lần cũng không nhân đôi dữ liệu.  
**Evidence:** `7b5a93ce-00a1-59b8-955f-dd4b8bd6b847` — *Data Pipeline Engineering*, slide 54.

### 13. temperature=0 — scenario diagnosis
> **Metadata:** `topic=temperature-zero-myth` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một team đặt `temperature=0` và tin rằng output sẽ giống hệt nhau mỗi lần chạy, nhưng vẫn thấy khác biệt khi đổi batch size. Nguyên nhân là gì?

- A. `temperature=0` chỉ hoạt động đúng khi kèm theo một seed cố định.
- B. Đổi batch size làm đổi thứ tự cộng floating-point, cho kết quả khác nhau.
- C. Đây là lỗi triển khai riêng của một provider, không phải đặc tính chung.
- D. `temperature=0` chỉ áp dụng cho request đơn lẻ, không áp dụng khi chạy song song.

**Đáp án:** B. Đây không phải lỗi seed — bạn không "sửa" được từ phía application. Vì vậy đội ops nên gate trên "% pass ≥ ngưỡng" kèm khoảng tin cậy, không gate trên so khớp chuỗi chính xác.  
**Evidence:** `f1d2a967-29ca-59be-a43a-2610b56200ab` — *LLMOps & Prompt Versioning*, slide 9.

### 14. Prompt cache invalidation — scenario diagnosis
> **Metadata:** `topic=prompt-cache-invalidation` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một agent chỉ đổi nội dung của message hiện tại (không đổi tool definitions, system prompt hay model). Điều gì xảy ra với cache?

- A. Toàn bộ cache bị huỷ, kể cả phần cache cho tools và system message.
- B. Cache cho tools và system message vẫn giữ nguyên; chỉ phần cache mới nhất bị huỷ.
- C. Không phần cache nào bị ảnh hưởng vì message không nằm trong phạm vi cache.
- D. Cache tự động được rebuild lại hoàn toàn từ đầu, bất kể thay đổi lớn hay nhỏ ra sao.

**Đáp án:** B. Theo thứ bậc huỷ cache: đổi model hoặc tool definitions mới huỷ toàn bộ như A mô tả. Nội dung message chỉ huỷ phần cache liên quan tới message, còn tools và system message vẫn giữ nguyên.  
**Evidence:** `67fdbbf2-d41e-5a00-b89e-c76b8a00a5fe` — *LLMOps & Prompt Versioning*, slide 44.

## Review checklist

- [ ] Vị trí vật lý đáp án đúng phân bố đều 4 vị trí (script check).
- [ ] Không câu nào có đáp án đúng dài hơn 1.3× option ngắn nhất.
- [ ] Mỗi câu đúng 4 option và đúng 1 đáp án.
- [ ] group/mutually_exclusive đóng kín và đối xứng (script check).
- [ ] Mọi citation resolve trong `source_spans.jsonl` (script check).
- [ ] Đã chạy §2 của `QUESTION_REVIEW_PROTOCOL.md` (đáp án thứ hai, evidence trả lời được stem).
