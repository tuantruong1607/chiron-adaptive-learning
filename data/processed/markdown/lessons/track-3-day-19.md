---
schema_version: 1
course_id: rag-intensive
document_id: "295b7e08-655f-53ef-a97a-583b81f02b6b"
document_version_id: "876b0310-c8cf-5ae1-a673-f10d35d723fb"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "GraphRAG — Truy xuất theo Quan hệ"
source_file: "track-3-day-19.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-19.html"
source_sha256: "15dee3e2660ee3ec15e2786e031aa6e3e2791e0201c546f399ed10d5fcf1150a"
parser_version: chiron-structured-markdown-v1
html_section_count: 19
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# GraphRAG — Truy xuất theo Quan hệ

> Biết khi nào quan hệ nhiều bước biện minh cho graph, cách chặn traversal explosion và kết hợp vector retrieval.

<!-- chiron-source-span: {"source_span_id":"602e652e-3db2-5bfb-9b24-970506cd95a2","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"track-3-day-19.html"},"checksum":"dad95da968988392ec853184747cbab97d14279a5e000f087624ba0e79098ed9"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: graph chỉ đáng giá khi query cần quan hệ hoặc tổng hợp nhiều bước. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"aa5f3789-6de5-53f5-aba3-088a39299c43","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"track-3-day-19.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

## ◎ Bản đồ tư duy trước khi học

Ba hình dưới đây là khung nối kiến thức với quyết định vận hành; chúng không thay thế nội dung slide.

| Tín hiệu đầu vào | Cơ chế quyết định | Đầu ra cần kiểm |
| --- | --- | --- |
| Yêu cầu, state, ràng buộc | Chuẩn hóa → đánh giá → route | Kết quả + evidence + telemetry |
| Failure hoặc uncertainty | Retry có giới hạn / escalation | Trạng thái bền vững, không nhân đôi tác dụng phụ |

Hình 1 — Mental model production: dữ liệu đi qua quyết định có kiểm soát, không đi thẳng vào model.

| Lớp | Câu hỏi phải trả lời | Failure mode nếu bỏ qua |
| --- | --- | --- |
| Quality | Đầu ra có đúng và grounded? | Demo đẹp nhưng sai ngầm |
| Reliability | Restart, timeout, retry có an toàn? | Mất state hoặc tác dụng phụ trùng |
| Economics | Latency và chi phí ở p95 là bao nhiêu? | Pilot được nhưng không scale |
| Governance | Ai có quyền làm gì, audit ở đâu? | Không thể vận hành có trách nhiệm |

Hình 2 — Bốn lăng kính dùng để đọc mọi quyết định trong bài.

| Mức bằng chứng | Dùng để làm gì | Không được suy diễn |
| --- | --- | --- |
| Trích slide | Nhắc lại định nghĩa và con số | Không biến ví dụ thành benchmark chung |
| Phép tính mô-đun | Phân tích độ nhạy của giả định | Không gọi là số đo production |
| Telemetry thực | Ra quyết định deploy/rollback | Không thay thế đánh giá nhân quả |

Hình 3 — Tách nguồn slide, mô hình tính và dữ liệu vận hành để không tạo “độ chính xác giả”.

---

<!-- chiron-source-span: {"source_span_id":"cf4c54c9-200b-503a-886a-77fed5fec1c5","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Khi vector search thiếu quan hệ","source_file":"track-3-day-19.html"},"checksum":"02b9108a47ec0693b3c8ac322e842eb5e83c093c87fcd0078c253b86fc359471"} -->

## 01 Khi vector search thiếu quan hệ

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Khi vector search thiếu quan hệ · Mental model & quyết định

> Trích slide Slide 1: GraphRAG & Knowledge Graphs AICB-P2T3 · Ngày 19 · Chương 4 — Agent Nâng Cao Giảng viên: Ngô Thanh Tùng VinUniversity · Phase 2 · Track 3 · Tuần 4

GraphRAG & Knowledge Graphs AICB-P2T3 · Ngày 19 · Chương 4 — Agent Nâng Cao. Điểm nối sang production là: graph chỉ đáng giá khi query cần quan hệ hoặc tổng hợp nhiều bước. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- “Khi user hỏi về mối quan hệ giữa 5 entities — flat RAG trả lời sai, GraphRAG trả lời đúng — tại sao?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay
- Vấn đề của RAG: Khi Vector Search thất bại 2.
- Kiến trúc SOTA (Microsoft GraphRAG, LightRAG) 5.

#### Tự kiểm tra · Với khi vector search thiếu quan hệ, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là graph chỉ đáng giá khi query cần quan hệ hoặc tổng hợp nhiều bước.

### Slide 4 Khi vector search thiếu quan hệ · Evidence & failure lens

> Trích slide Slide 4: 1 Khi nào Flat RAG thất bại? Giới hạn của vector search khi cần suy luận quan hệ

**Đọc như kỹ sư:** Giới hạn của vector search khi cần suy luận quan hệ

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 4 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 7 Khi vector search thiếu quan hệ · Evidence & failure lens

> Trích slide Slide 7: Câu trả lời từ Flat RAG Kết quả: Sinh ra ảo giác (Hallucination) Hoặc trả lời "Tôi không có đủ thông tin" Tại sao? Flat RAG truy xuất các đoạn văn bản (chunks) có sự tương đồng về ngữ nghĩa. Nó có thể lấy ra một đoạn về Google, một đoạn về Transformer, và một đoạn về startup AI, nhưng thiếu đi mối liên kết giữa chúng. Câu hỏi…

**Đọc như kỹ sư:** Câu trả lời từ Flat RAG Kết quả: Sinh ra ảo giác (Hallucination) Hoặc trả lời "Tôi không có đủ thông tin" Tại sao?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Flat RAG truy xuất các đoạn văn bản (chunks) có sự tương đồng về ngữ nghĩa.
- Nó có thể lấy ra một đoạn về Google, một đoạn về Transformer, và một đoạn về startup AI, nhưng thiếu đi mối liên kết giữa chúng.
- Câu hỏi Chunk A (Google) Chunk B (Transformer) Chunk C (Startup) Thiếu link giữa các entities!

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 7 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"0b84b051-9d22-5012-ab2d-e1e3a7e427a5","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Knowledge graph primitives","source_file":"track-3-day-19.html"},"checksum":"6be86b3321c628d984a5f05cbf1535c8c26d8c36f1df6480a7a4bd17bc94c326"} -->

## 02 Knowledge graph primitives

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 8 Knowledge graph primitives · Mental model & quyết định

> Trích slide Slide 8: Nguyên nhân gốc rễ: Tương đồng vs. Cấu trúc Vector RAG (Flat RAG) Tìm kiếm sự tương đồng về mặt ngữ nghĩa (Semantic similarity). Nó tìm các từ và khái niệm giống nhau trong các đoạn văn bản riêng lẻ. Hạn chế  Không thể tự động duyệt qua các mối quan hệ. Giống như việc bạn tìm thấy 3 trang bách khoa toàn thư nhưng không đọc…

Cấu trúc Vector RAG (Flat RAG) Tìm kiếm sự tương đồng về mặt ngữ nghĩa (Semantic similarity).. Điểm nối sang production là: entity không có canonicalization sẽ tạo graph phân mảnh. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Nó tìm các từ và khái niệm giống nhau trong các đoạn văn bản riêng lẻ.
- Hạn chế  Không thể tự động duyệt qua các mối quan hệ.
- Giống như việc bạn tìm thấy 3 trang bách khoa toàn thư nhưng không đọc phần tham chiếu chéo.

#### Tự kiểm tra · Với knowledge graph primitives, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là entity không có canonicalization sẽ tạo graph phân mảnh.

### Slide 11 Knowledge graph primitives · Evidence & failure lens

> Trích slide Slide 11: Bằng chứng: GraphRAG vượt trội trên relational queries +40% Comprehensiveness vs Flat RAG 2–3× Multi-hop accuracy gain OK Flat RAG vẫn tốt cho factoid Benchmark trên community questions: GraphRAG +40% comprehensiveness. Nhưng single-doc factoid, Flat RAG nhanh hơn và rẻ hơn. Không phải lúc nào cũng cần graph.

**Đọc như kỹ sư:** Bằng chứng: GraphRAG vượt trội trên relational queries +40% Comprehensiveness vs Flat RAG 2–3× Multi-hop accuracy gain OK Flat RAG vẫn tốt cho factoid Benchmark trên community questions: GraphRAG +40% comprehensiveness.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nhưng single-doc factoid, Flat RAG nhanh hơn và rẻ hơn.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 11 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 14 Knowledge graph primitives · Evidence & failure lens

> Trích slide Slide 14: Graph Theory 101 Nodes (Đỉnh/Thực thể): Các thực thể trong dữ liệu Edges (Cạnh/Mối quan hệ): Kết nối giữa các nodes Properties (Thuộc tính): Metadata gắn với nodes hoặc edges Sam Altman OpenAI GPT-4 co-founded developed • Node Property: age=38 • Edge Property: year=2015 Node Edge Giảng viên (VinUni) AICB · Ngày 19

**Đọc như kỹ sư:** Graph Theory 101 Nodes (Đỉnh/Thực thể): Các thực thể trong dữ liệu Edges (Cạnh/Mối quan hệ): Kết nối giữa các nodes Properties (Thuộc tính): Metadata gắn với nodes hoặc edges Sam Altman OpenAI GPT-4 co-founded developed • Node Property: age=38 • Edge Property:

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 14 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"aeae3e93-e0e8-55c6-8cfe-31dad86afd8b","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Entity & relationship extraction","source_file":"track-3-day-19.html"},"checksum":"a9e07b614a4f61cf84923cf0bcc56437e12bac68181d198ccd77f035116f9825"} -->

## 03 Entity & relationship extraction

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 15 Entity & relationship extraction · Mental model & quyết định

> Trích slide Slide 15: Bộ ba (The Triple) - Đơn vị cốt lõi Giảng viên (VinUni) AICB · Ngày 19 Knowledge Graphs được xây dựng từ các Triples (Bộ ba). Đây là nguyên tử cơ bản để cấu trúc hóa kiến thức nhân loại.  Cấu trúc: (Chủ thể) → [Vị ngữ / Mối quan hệ] → (Tân ngữ) Ví dụ 1: (Sam Altman) → [CEO_OF] → (OpenAI) Ví dụ 2: (OpenAI) → [DEVELOPED] →…

Đây là nguyên tử cơ bản để cấu trúc hóa kiến thức nhân loại.. Điểm nối sang production là: mỗi edge cần provenance về chunk nguồn. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

-  Cấu trúc: (Chủ thể) → [Vị ngữ / Mối quan hệ] → (Tân ngữ) Ví dụ 1: (Sam Altman) → [CEO_OF] → (OpenAI) Ví dụ 2: (OpenAI) → [DEVELOPED] → (GPT-4)  Hàng triệu Triples này kết nối lại tạo thành một Knowledge Graph khổng lồ.
- Vô hướng (Undirected) Đồ thị có hướng Các cạnh có hướng cụ thể (đường một chiều).
- Person City BORN_IN Ví dụ: Chiều ngược lại không đúng.

#### Tự kiểm tra · Với entity & relationship extraction, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là mỗi edge cần provenance về chunk nguồn.

### Slide 18 Entity & relationship extraction · Evidence & failure lens

> Trích slide Slide 18: Cypher: Ngôn ngữ truy vấn Graph (SQL của Graph)  Cách chúng ta truy vấn cơ sở dữ liệu đồ thị. MATCH Tìm kiếm mẫu (pattern). WHERE Lọc dữ liệu. RETURN Trả về kết quả. MATCH (p:Person)-[:CO_FOUNDED]->(c:Company) WHERE c.name = 'OpenAI' RETURN p.name Giảng viên (VinUni) AICB · Ngày 19

**Đọc như kỹ sư:** Cypher: Ngôn ngữ truy vấn Graph (SQL của Graph)  Cách chúng ta truy vấn cơ sở dữ liệu đồ thị.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- MATCH (p:Person)-[:CO_FOUNDED]->(c:Company) WHERE c.name = 'OpenAI' RETURN p.name

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 18 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 21 Entity & relationship extraction · Evidence & failure lens

> Trích slide Slide 21: Coreference Resolution  Văn bản: "Sam Altman là một doanh nhân. Ông đã thành lập OpenAI." Nếu không quy chiếu "Ông" → "Sam Altman", đồ thị sẽ tạo ra một node bị cô lập tên là "Ông". Bỏ qua bước này làm mất 30-40% các mối quan hệ quan trọng trong đồ thị. Trước (Rời rạc) Sam Altman Doanh nhân Ông OpenAI Sau (Đã kết nối) Sam…

**Đọc như kỹ sư:** Coreference Resolution  Văn bản: "Sam Altman là một doanh nhân.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Ông đã thành lập OpenAI." Nếu không quy chiếu "Ông" → "Sam Altman", đồ thị sẽ tạo ra một node bị cô lập tên là "Ông".
- Bỏ qua bước này làm mất 30-40% các mối quan hệ quan trọng trong đồ thị.
- Trước (Rời rạc) Sam Altman Doanh nhân Ông OpenAI Sau (Đã kết nối) Sam Altman Doanh nhân OpenAI

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 21 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"8ca5afb9-cece-5488-8bde-69dfb1944096","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Graph construction & provenance","source_file":"track-3-day-19.html"},"checksum":"fd5ad030bcfc1b721fbfcb0bea9a41da8a851a70e4d3059e59188cdfdf5074f8"} -->

## 04 Graph construction & provenance

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 22 Graph construction & provenance · Mental model & quyết định

> Trích slide Slide 22: Entity Disambiguation  Ngôn ngữ có tính mơ hồ “Apple báo cáo doanh số iPhone kỷ lục.” “Apple (quả táo) là một loại trái cây ngon.”  Disambiguation đảm bảo hệ thống tạo ra hai node riêng biệt dựa trên ngữ cảnh lúc trích xuất. Apple_Inc Apple_Fruit Giảng viên (VinUni) AICB · Ngày 19

Entity Disambiguation  Ngôn ngữ có tính mơ hồ “Apple báo cáo doanh số iPhone kỷ lục.” “Apple (quả táo) là một loại trái cây ngon.”  Disambiguation đảm bảo hệ thống tạo ra hai node riêng biệt dựa trên ngữ cảnh lúc trích xuất.. Điểm nối sang production là: traversal phải có depth và edge cap.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Entity Deduplication  Nhiều đoạn văn bản có thể gọi cùng một thực thể theo các cách khác nhau.
-  Giải pháp: Thêm bước chuẩn hóa (normalization) Sử dụng các kỹ thuật sau để gộp chúng thành một node duy nhất
- Đọc các đoạn văn bản (Chunks) Phân tích và nạp dữ liệu thô từ nguồn tài liệu.

#### Tự kiểm tra · Với graph construction & provenance, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là traversal phải có depth và edge cap.

### Slide 25 Graph construction & provenance · Evidence & failure lens

> Trích slide Slide 25: Building Knowledge Graph — NetworkX vs Neo4j ACID Không Có Algorithms Có (BFS, PageRank) Full library Best for Prototype Production NetworkX Neo4j Thêm embeddings cho mỗi node + source chunk refer- Setup pip install Docker/Cloud ences → enable hybrid search (graph + vector)Scale ∼100K nodes Millions+ ■ Bulk insert: batch thay…

**Đọc như kỹ sư:** Bulk insert: batch thay vì từng triple — 10× faster

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Beyond 100K: switch Neo4j hoặc FalkorDB (Redis-based)

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 25 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 28 Graph construction & provenance · Evidence & failure lens

> Trích slide Slide 28: Bước 1 & 2: Trích xuất & Khởi tạo Node gốc (Seed)  Câu hỏi "Ai đồng sáng lập Microsoft?"  Trích xuất LLM lấy ra các thực thể quan trọng: [Microsoft]  Seeding (Khởi tạo) Hệ thống tìm trong Graph DB node khớp hoàn toàn hoặc có ngữ nghĩa tương đồng với "Microsoft". → Đây là điểm xuất phát cho quá trình duyệt đồ thị. Giảng viên…

**Đọc như kỹ sư:** → Đây là điểm xuất phát cho quá trình duyệt đồ thị.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 28 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"694ae965-9781-5e64-887b-8278fdc6a810","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 Traversal và multi-hop","source_file":"track-3-day-19.html"},"checksum":"0d9643f718527ae639229dd65f437c6ac0d1af01e1e4585907d8e34fe33f8f6a"} -->

## 05 Traversal và multi-hop

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 29 Traversal và multi-hop · Mental model & quyết định

> Trích slide Slide 29: Bước 3: Duyệt Đồ thị (Breadth-First Search - BFS)  Thuật toán duyệt Từ seed node, hệ thống dùng thuật toán Tìm kiếm theo chiều rộng (BFS) để lấy các nodes và edges lân cận.  Kết quả thu thập (Triples) Nó thu thập tất cả Triples nối với node gốc: ● (Bill Gates)—[CO_FOUNDED]→(Microsoft) ● (Paul Allen)—[CO_FOUNDED]→(Microsoft)…

Bước 3: Duyệt Đồ thị (Breadth-First Search - BFS)  Thuật toán duyệt Từ seed node, hệ thống dùng thuật toán Tìm kiếm theo chiều rộng (BFS) để lấy các nodes và edges lân cận.. Điểm nối sang production là: community summary phục vụ global question nhưng tốn index.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

-  Kết quả thu thập (Triples) Nó thu thập tất cả Triples nối với node gốc
- Độ sâu Duyệt (Traversal Depth)  Depth = 1: Quá nông Chỉ lấy hàng xóm trực tiếp, dễ trượt mất ngữ cảnh "multi-hop".
-  Depth = 3+: Quá nhiễu Kéo theo dữ liệu không liên quan, làm quá tải Context Window của LLM và gây ra ảo giác.

#### Tự kiểm tra · Với traversal và multi-hop, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là community summary phục vụ global question nhưng tốn index.

### Slide 33 Traversal và multi-hop · Evidence & failure lens

> Trích slide Slide 33: Hybrid Search (Sự kết hợp hoàn hảo)  Bổ trợ thay vì thay thế GraphRAG không nên thay thế Vector Search; nó nên đóng vai trò bổ trợ lẫn nhau.  Hybrid Search Chúng ta lưu trữ vector embeddings bên trong các node của đồ thị.  Cơ chế hoạt động Dùng Semantic Search để tìm seed node, sau đó dùng Graph Traversal để tìm quan hệ,…

**Đọc như kỹ sư:** Hybrid Search (Sự kết hợp hoàn hảo)  Bổ trợ thay vì thay thế GraphRAG không nên thay thế Vector Search; nó nên đóng vai trò bổ trợ lẫn nhau.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

-  Hybrid Search Chúng ta lưu trữ vector embeddings bên trong các node của đồ thị.
-  Cơ chế hoạt động Dùng Semantic Search để tìm seed node, sau đó dùng Graph Traversal để tìm quan hệ, kết hợp cả ngữ cảnh cấu trúc lẫn phi cấu trúc.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 33 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 36 Traversal và multi-hop · Evidence & failure lens

> Trích slide Slide 36: Các Lỗi thường gặp (Failure Modes)  Super-nodes (Node quá tải) Một node như "USA" có thể có 100,000 kết nối. Duyệt nó sẽ làm sập context window.  Đồ thị rời rạc Trích xuất thất bại không nối được các subgraph. Tạo ra các "hòn đảo" dữ liệu (Disconnected Components).  Ngữ cảnh nghèo nàn Bước textualization lược bỏ quá nhiều…

**Đọc như kỹ sư:** Các Lỗi thường gặp (Failure Modes)  Super-nodes (Node quá tải) Một node như "USA" có thể có 100,000 kết nối.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

-  Đồ thị rời rạc Trích xuất thất bại không nối được các subgraph.
- Tạo ra các "hòn đảo" dữ liệu (Disconnected Components).
-  Ngữ cảnh nghèo nàn Bước textualization lược bỏ quá nhiều sắc thái từ tài liệu gốc.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 36 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"0edbe92c-f10d-5340-a0b7-02782244ef3c","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 GraphRAG architecture","source_file":"track-3-day-19.html"},"checksum":"5d517b4c2b2e7e56d4818a55610f023a77824b921d32cf7563069ebb5fdfb887"} -->

## 06 GraphRAG architecture

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 37 GraphRAG architecture · Mental model & quyết định

> Trích slide Slide 37: Best Practices  Luôn duy trì một con trỏ (pointer) từ Graph Node ngược về Document Chunk gốc.  Đặt giới hạn duyệt (VD: "duyệt 2 hop, nhưng tối đa 50 cạnh").  Liên tục tinh chỉnh prompt NER.

Best Practices  Luôn duy trì một con trỏ (pointer) từ Graph Node ngược về Document Chunk gốc.. Điểm nối sang production là: vector retrieval tốt cho similarity, graph tốt cho structure. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

-  Đặt giới hạn duyệt (VD: "duyệt 2 hop, nhưng tối đa 50 cạnh").
- 4 Các Kiến trúc SOTA (State-of-the-Art) Các ông lớn công nghệ đang scale GraphRAG như thế nào.
- Sự trỗi dậy của Advanced GraphRAG  GraphRAG cơ bản dựa trên trích xuất Triple đơn giản.

#### Tự kiểm tra · Với graphrag architecture, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là vector retrieval tốt cho similarity, graph tốt cho structure.

### Slide 40 GraphRAG architecture · Evidence & failure lens

> Trích slide Slide 40: Microsoft GraphRAG  Phát hành giữa năm 2024  Thiết kế cho Sensemaking Tạo dựng ý nghĩa trên toàn bộ tập dữ liệu.  Triết lý cốt lõi Không chỉ để trả lời câu hỏi cụ thể, mà để hỏi hệ thống: "Tập dữ liệu này nói về bức tranh tổng thể gì?"

**Đọc như kỹ sư:** Microsoft GraphRAG  Phát hành giữa năm 2024  Thiết kế cho Sensemaking Tạo dựng ý nghĩa trên toàn bộ tập dữ liệu.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

-  Triết lý cốt lõi Không chỉ để trả lời câu hỏi cụ thể, mà để hỏi hệ thống: "Tập dữ liệu này nói về bức tranh tổng thể gì?"

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 40 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 43 GraphRAG architecture · Evidence & failure lens

> Trích slide Slide 43: MS GraphRAG: Truy vấn Local vs. Global  Local Search Cho câu hỏi cụ thể ("Ai kết nối X với Y?"). Duyệt qua các nodes.  Global Search Cho câu hỏi chủ đề ("Đâu là rủi ro chính trong các hợp đồng này?"). Đọc các Báo cáo Cộng đồng đã tạo sẵn thay vì duyệt node thô. Giảng viên (VinUni) AICB · GraphRAG

**Đọc như kỹ sư:** Global  Local Search Cho câu hỏi cụ thể ("Ai kết nối X với Y?").

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

-  Global Search Cho câu hỏi chủ đề ("Đâu là rủi ro chính trong các hợp đồng này?").
- Đọc các Báo cáo Cộng đồng đã tạo sẵn thay vì duyệt node thô.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 43 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"eeb545fa-bdc8-50f1-9f4d-ba5bc7efaf6e","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Hybrid graph–vector retrieval","source_file":"track-3-day-19.html"},"checksum":"b7893336465592d4542feaa58a5a0e6dcde95206cc2351787b029c6bda69afe5"} -->

## 07 Hybrid graph–vector retrieval

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 44 Hybrid graph–vector retrieval · Mental model & quyết định

> Trích slide Slide 44: Điểm yếu của MS GraphRAG  ● Chi phí cực đắt: Việc tạo tóm tắt cho mọi cộng đồng trên kho dữ liệu lớn ngốn một lượng token khổng lồ trong quá trình indexing. ● Index 1 triệu token có thể tốn $10–$50+ chỉ để xây đồ thị.  Không phù hợp cho dữ liệu thay đổi liên tục. Giảng viên (VinUni) AICB · GraphRAG

Chi phí cực đắt: Việc tạo tóm tắt cho mọi cộng đồng trên kho dữ liệu lớn ngốn một lượng token khổng lồ trong quá trình indexing.. Điểm nối sang production là: hybrid router tránh trả graph cost cho mọi query. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Index 1 triệu token có thể tốn $10–$50+ chỉ để xây đồ thị.
-  Không phù hợp cho dữ liệu thay đổi liên tục.
- LightRAG (Kẻ thách thức tối ưu)  Tối ưu hiệu năng Giải quyết vấn đề chi phí và sự cồng kềnh của MS GraphRAG.

#### Tự kiểm tra · Với hybrid graph–vector retrieval, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là hybrid router tránh trả graph cost cho mọi query.

### Slide 47 Hybrid graph–vector retrieval · Evidence & failure lens

> Trích slide Slide 47: Bảng So sánh (MS GraphRAG vs. LightRAG vs. Flat RAG) Chi phí Index Khả năng Global Multi-hop Flat RAG  Rất Rẻ  Kém  Kém MS GraphRAG  Rất Đắt  Xuất sắc  Xuất sắc LightRAG  Trung bình  Tốt  Xuất sắc (Triển khai nhanh) Giảng viên (VinUni) AICB · GraphRAG

**Đọc như kỹ sư:** Flat RAG) Chi phí Index Khả năng Global Multi-hop Flat RAG  Rất Rẻ  Kém  Kém MS GraphRAG  Rất Đắt  Xuất sắc  Xuất sắc LightRAG  Trung bình  Tốt  Xuất sắc (Triển khai nhanh)

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 47 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 50 Hybrid graph–vector retrieval · Evidence & failure lens

> Trích slide Slide 50: 5 Chiến lược Doanh nghiệp & ROI Cách chứng minh giá trị của GraphRAG với stakeholder

**Đọc như kỹ sư:** 5 Chiến lược Doanh nghiệp & ROI Cách chứng minh giá trị của GraphRAG với stakeholder

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 50 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"6b6052ae-7236-536f-9465-5516b214fd55","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Microsoft GraphRAG & LightRAG","source_file":"track-3-day-19.html"},"checksum":"369d2786a1c8e95ed95f807befdd035a76773cc230060f15d3dfc4349c720849"} -->

## 08 Microsoft GraphRAG & LightRAG

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 51 Microsoft GraphRAG & LightRAG · Mental model & quyết định

> Trích slide Slide 51: Thực tế về Chi phí: Indexing vs. Querying  Flat RAG • Rẻ khi xây dựng • Rẻ khi truy vấn  GraphRAG • Rất đắt khi xây dựng (vì LLM trích xuất triples) • Truy vấn khá rẻ và cực kỳ chính xác  Rule of thumb Đừng dùng GraphRAG cho các tài liệu dùng một lần. Hãy dùng nó cho tri thức cốt lõi của doanh nghiệp.

Querying  Flat RAG • Rẻ khi xây dựng • Rẻ khi truy vấn  GraphRAG • Rất đắt khi xây dựng (vì LLM trích xuất triples) • Truy vấn khá rẻ và cực kỳ chính xác  Rule of thumb Đừng dùng GraphRAG cho các tài liệu dùng một lần.. Điểm nối sang production là: extraction error lan truyền vào mọi câu trả lời phía sau.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Hãy dùng nó cho tri thức cốt lõi của doanh nghiệp.
- Decision Framework: Khi nào dùng Flat RAG  Flat RAG Optimization
- Tra cứu tài liệu IT Support (Factoid lookup).

#### Tự kiểm tra · Với microsoft graphrag & lightrag, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là extraction error lan truyền vào mọi câu trả lời phía sau.

### Slide 54 Microsoft GraphRAG & LightRAG · Evidence & failure lens

> Trích slide Slide 54: Vector RAG vs GraphRAG — So sánh trực quan Vector RAG Query Chunk A Chunk B Chunk C Chunk D Chunk E Top-K similarity GraphRAG Q A B C D E Graph traversal (2 hops) Single-doc factoid → Flat RAG. Multi-entity relations → GraphRAG. Thematic overview → GraphRAG global. Hybrid: detect query type rồi route tương ứng.

**Đọc như kỹ sư:** Vector RAG vs GraphRAG — So sánh trực quan Vector RAG Query Chunk A Chunk B Chunk C Chunk D Chunk E Top-K similarity GraphRAG Q A B C D E Graph traversal (2 hops) Single-doc factoid → Flat RAG.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Hybrid: detect query type rồi route tương ứng.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 54 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 57 Microsoft GraphRAG & LightRAG · Evidence & failure lens

> Trích slide Slide 57: Use Case 3: Rủi ro Chuỗi cung ứng (Supply Chain)  Ánh xạ thế giới vật lý  Graph Traversal giúp xác định ngay lập tức các điểm nghẽn và tác động dây chuyền khi một mắt xích trong chuỗi cung ứng gặp sự cố. Nhà cung cấp A [CUNG_CẤP] Linh kiện B [LẮP_RÁP] Sản phẩm C Câu hỏi: "Nếu Nhà cung cấp A ngừng hoạt động, sản phẩm nào bị…

**Đọc như kỹ sư:** Use Case 3: Rủi ro Chuỗi cung ứng (Supply Chain)  Ánh xạ thế giới vật lý  Graph Traversal giúp xác định ngay lập tức các điểm nghẽn và tác động dây chuyền khi một mắt xích trong chuỗi cung ứng gặp sự cố.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nhà cung cấp A [CUNG_CẤP] Linh kiện B [LẮP_RÁP] Sản phẩm C Câu hỏi: "Nếu Nhà cung cấp A ngừng hoạt động, sản phẩm nào bị trễ?"

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 57 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"79a4c222-61cb-557c-b464-70ad8238c314","locator":{"kind":"html_section","section_id":"c8","order":11,"heading":"09 Cost, ROI & Lab","source_file":"track-3-day-19.html"},"checksum":"56a14490c1c994cccc85b87f5daa5239fba381a15dfb7b54e5847ed37f341c94"} -->

## 09 Cost, ROI & Lab

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 58 Cost, ROI & Lab · Mental model & quyết định

> Trích slide Slide 58: 6 Demo & Thực hành

Corpus: 100 Wikipedia articles AI companies, extract entities → Neo4j graph 2.. Điểm nối sang production là: đánh giá GraphRAG phải tách indexing cost và query uplift. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Query 1 (flat RAG OK): “What is OpenAI?” — cả hai pipeline đúng 3.
- Query 2 (multi-hop): “AI companies co-founded by former Google employees” — flat RAG hallucinate, GraphRAG đúng 4.
- Visualization: Neo4j Browser hiển thị subgraph, highlight answer nodes

#### Tự kiểm tra · Với cost, roi & lab, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là đánh giá GraphRAG phải tách indexing cost và query uplift.

### Slide 62 Cost, ROI & Lab · Evidence & failure lens

> Trích slide Slide 62: Tổng kết — Key Takeaways Những ý chính cần nhớ sau buổi học hôm nay 1 Knowledge graphs enable multi-hop reasoning mà flat RAG không làm được — dùng cho relational queries 2 Entity extraction quality là bottleneck — invest NER + coreference resolution trước khi build graph 3 “Graph quality beats Graph size” — 1000 high-quality…

**Đọc như kỹ sư:** Tổng kết — Key Takeaways Những ý chính cần nhớ sau buổi học hôm nay 1 Knowledge graphs enable multi-hop reasoning mà flat RAG không làm được — dùng cho relational queries 2 Entity extraction quality là bottleneck — invest NER + coreference resolution trước khi

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 62 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 65 Cost, ROI & Lab · Evidence & failure lens

> Trích slide Slide 65: Cảm ơn! AICB-P2T3 · Ngày 19 · GraphRAG & Knowledge Graphs github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn

**Đọc như kỹ sư:** AICB-P2T3 · Ngày 19 · GraphRAG & Knowledge Graphs github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 65 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"16f0687b-529d-51ea-baf6-f1fdb469a348","locator":{"kind":"html_section","section_id":"ladder","order":12,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"track-3-day-19.html"},"checksum":"e57752503b437799e1cf380a0c9f4487573df4f827ce95def5dd7ae9a1ebdca3"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của GraphRAG & knowledge graph bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"c3d46b62-b0d8-5b36-80b1-953c2c713ee4","locator":{"kind":"html_section","section_id":"section-013","order":13,"heading":"∑ Phòng mô phỏng quyết định","source_file":"track-3-day-19.html"},"checksum":"d93aebe793d00f9ce3f46670faa1f9f7e80cfec116f1fedd4fac22f654884826"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Traversal explosion — thêm một hop đắt đến đâu?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Bậc trung bình:**: min `2`, max `20`, step `1`, default `6`

- **Control - Độ sâu:**: min `1`, max `6`, step `1`, default `3`

- **Control - Giới hạn cạnh:**: min `10`, max `5000`, step `10`, default `500`

- **Control - Token/triple:**: min `5`, max `100`, step `5`, default `30`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — GraphRAG ROI — indexing có đáng với câu hỏi quan hệ?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Số chunk:**: min `1000`, max `500000`, step `1000`, default `100000`

- **Control - Index/1.000 chunk:**: min `1`, max `100`, step `1`, default `12`

- **Control - Query quan hệ/tháng:**: min `100`, max `100000`, step `100`, default `10000`

- **Control - Uplift chính xác:**: min `0`, max `50`, step `1`, default `18`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Retrieval router — flat, graph hay hybrid?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Cần quan hệ:**: min `0`, max `100`, step `5`, default `70`

- **Control - Tính factoid:**: min `0`, max `100`, step `5`, default `25`

- **Control - Rủi ro sai:**: min `0`, max `100`, step `5`, default `65`

- **Control - Ngân sách:**: min `0`, max `100`, step `5`, default `55`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"62921811-b38f-5b5f-b196-a1888c4bc51d","locator":{"kind":"html_section","section_id":"misc","order":14,"heading":"✕ Hiểu lầm phổ biến","source_file":"track-3-day-19.html"},"checksum":"990e0d42db88a16b339a43b25f7be77553c0ad66574b3d219f53208237d8d476"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai khi vector search thiếu quan hệ là phần còn lại tự động an toàn và ổn định.

Sửa lại Graph chỉ đáng giá khi query cần quan hệ hoặc tổng hợp nhiều bước.

Vì sao quan trọng · slide 1 · 4 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai knowledge graph primitives là phần còn lại tự động an toàn và ổn định.

Sửa lại Entity không có canonicalization sẽ tạo graph phân mảnh.

Vì sao quan trọng · slide 8 · 11 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai entity & relationship extraction là phần còn lại tự động an toàn và ổn định.

Sửa lại Mỗi edge cần provenance về chunk nguồn.

Vì sao quan trọng · slide 15 · 18 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai graph construction & provenance là phần còn lại tự động an toàn và ổn định.

Sửa lại Traversal phải có depth và edge cap.

Vì sao quan trọng · slide 22 · 25 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai traversal và multi-hop là phần còn lại tự động an toàn và ổn định.

Sửa lại Community summary phục vụ global question nhưng tốn index.

Vì sao quan trọng · slide 29 · 33 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai graphrag architecture là phần còn lại tự động an toàn và ổn định.

Sửa lại Vector retrieval tốt cho similarity, graph tốt cho structure.

Vì sao quan trọng · slide 37 · 40 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"6bf57570-8b82-5af7-9e1f-b6c1d8be9d03","locator":{"kind":"html_section","section_id":"apply","order":15,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"track-3-day-19.html"},"checksum":"59922d007fce463e96b701e8e38b7eb1b5a2fad5257f1b4196cdc837a7a9636e"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI cần trả lời câu hỏi nối khách–đặt phòng–chính sách–quyền lợi mà vector search đơn thuần bỏ mất cạnh.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Khi vector search thiếu quan hệ | Graph chỉ đáng giá khi query cần quan hệ hoặc tổng hợp nhiều bước. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 4 |
| Knowledge graph primitives | Entity không có canonicalization sẽ tạo graph phân mảnh. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 8 · 11 |
| Entity & relationship extraction | Mỗi edge cần provenance về chunk nguồn. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 15 · 18 |
| Graph construction & provenance | Traversal phải có depth và edge cap. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 22 · 25 |
| Traversal và multi-hop | Community summary phục vụ global question nhưng tốn index. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 29 · 33 |
| GraphRAG architecture | Vector retrieval tốt cho similarity, graph tốt cho structure. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 37 · 40 |
| Hybrid graph–vector retrieval | Hybrid router tránh trả graph cost cho mọi query. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 44 · 47 |
| Microsoft GraphRAG & LightRAG | Extraction error lan truyền vào mọi câu trả lời phía sau. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 51 · 54 |

---

<!-- chiron-source-span: {"source_span_id":"bd1e2359-00d9-579a-a1c9-6240d2bef658","locator":{"kind":"html_section","section_id":"numbers","order":16,"heading":"# Con số cần kiểm chứng","source_file":"track-3-day-19.html"},"checksum":"0717e9a438913e0930220dcdfb891cb1ee10322c4c1b91e364fe1baf550ad4b7"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 1 K | 1 Khi nào Flat RAG thất bại? Giới hạn của vector search khi cần suy luận quan hệ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 4 |
| 40% | Bằng chứng: GraphRAG vượt trội trên relational queries +40% Comprehensiveness vs Flat RAG 2–3× Multi-hop accuracy gain OK Flat RAG vẫn tốt cho factoid Benchmark trên community questions: GraphRAG +40% comprehe | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 11 |
| 3× | ứng: GraphRAG vượt trội trên relational queries +40% Comprehensiveness vs Flat RAG 2–3× Multi-hop accuracy gain OK Flat RAG vẫn tốt cho factoid Benchmark trên community questions: GraphRAG +40% comprehensiveness. Nhưng single-doc factoid | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 11 |
| 2 K | 2 Knowledge Graph Fundamentals Nodes, Edges, Triples — nền tảng của graph-based retrieval | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 12 |
| 4M | Knowledge Graph — Nodes, Edges, Triples Sam Altman OpenAI GPT-4Microsoft Google co-founded developedinvested worked at Triple: (Sam Altman, co-founded, OpenAI) KnowledgeGraph — Directed labeled graph: Entity (node) | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 100K | - Setup pip install Docker/Cloud ences → enable hybrid search (graph + vector)Scale ∼100K nodes Millions+ ■ Bulk insert: batch thay vì từng triple — 10× faster ■ Beyond 100K: switch Neo4j hoặc FalkorDB (Redis-based) | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 25 |
| 10× | raph + vector)Scale ∼100K nodes Millions+ ■ Bulk insert: batch thay vì từng triple — 10× faster ■ Beyond 100K: switch Neo4j hoặc FalkorDB (Redis-based) | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 25 |
| 3 M | ông liên quan, làm quá tải Context Window của LLM và gây ra ảo giác. Hop 1 Hop 2 Hop 3 Mô phỏng ranh giới truy vấn | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 30 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"3f3fb300-1fe1-537e-a4e8-1e84ff045539","locator":{"kind":"html_section","section_id":"cheat","order":17,"heading":"▣ Cheat sheet ôn thi","source_file":"track-3-day-19.html"},"checksum":"e303c37deac114fb85218db05701fe7d57122a9cba3dbd8364e01eb82944fa6c"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp khi vector search thiếu quan hệ | graph chỉ đáng giá khi query cần quan hệ hoặc tổng hợp nhiều bước | 1 · 4 |
| Khi gặp knowledge graph primitives | entity không có canonicalization sẽ tạo graph phân mảnh | 8 · 11 |
| Khi gặp entity & relationship extraction | mỗi edge cần provenance về chunk nguồn | 15 · 18 |
| Khi gặp graph construction & provenance | traversal phải có depth và edge cap | 22 · 25 |
| Khi gặp traversal và multi-hop | community summary phục vụ global question nhưng tốn index | 29 · 33 |
| Khi gặp graphrag architecture | vector retrieval tốt cho similarity, graph tốt cho structure | 37 · 40 |
| Khi gặp hybrid graph–vector retrieval | hybrid router tránh trả graph cost cho mọi query | 44 · 47 |
| Khi gặp microsoft graphrag & lightrag | extraction error lan truyền vào mọi câu trả lời phía sau | 51 · 54 |
| Khi gặp cost, roi & lab | đánh giá GraphRAG phải tách indexing cost và query uplift | 58 · 62 |

---

<!-- chiron-source-span: {"source_span_id":"d6400c83-2494-5571-932f-4ddd15d64bd4","locator":{"kind":"html_section","section_id":"gloss","order":18,"heading":"☰ Từ điển thuật ngữ","source_file":"track-3-day-19.html"},"checksum":"c4d1f76d89eba78b6bffb9e729d345b9e491823babbb04baccb0c595c01e4b83"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"6e8cf38d-0369-5d4b-8724-d51fc725f611","locator":{"kind":"html_section","section_id":"bloom","order":19,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-19.html"},"checksum":"18b4a383ca69f2c8b140ae640e60a111e86c0125570d7c2a6b82f9d2c729274f"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 4 · 7 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 8 · 11 · 14 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 15 · 18 · 21 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 22 · 25 · 28 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 29 · 33 · 36 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 37 · 40 · 43 |
