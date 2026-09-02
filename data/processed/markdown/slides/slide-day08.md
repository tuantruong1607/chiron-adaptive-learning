---
schema_version: 1
course_id: rag-intensive
document_id: "8505565d-0cae-5464-aac1-75d927bb72dd"
document_version_id: "708c7cc5-e99b-5bb5-91af-f1184fcd4451"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "RAG Pipeline"
source_file: "slide day08.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\slide day08.pdf"
source_sha256: "4cd13a547566e2b0305bcd8b3240581cb309d1ef6e615ea738079a1653c323c4"
parser_version: chiron-structured-markdown-v1
page_count: 139
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":139}"
language: vi
---

# RAG Pipeline

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"7a0029e5-7a73-57d8-9f6c-42b3adb57ed4","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"RAG Pipeline","extraction_method":"pdf-text-layer"},"checksum":"29cffb5fb419f6bca0fc731f4467ff4b10819fac8a96d8e315a3cc1f071591cf"} -->

## Slide 1 - RAG Pipeline

AICB-P1 · Ngày 8 · Truy Xuất & Sinh Câu Trả Lời Tên Giảng Viên VinUniversity · Phase 1 · Tuần 2 · 2026

---

<!-- chiron-source-span: {"source_span_id":"2e550d79-1049-5dd5-b7d4-89ec22bc6f66","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃY SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"59cb14119c23dde8737bf3d1d6258576aca5ae3a343bacf7a5ed25fb3b2e9bdd"} -->

## Slide 2 - HÃY SUY NGHĨ...

? “Bạn đã build agent với vector store. Nhưng agent vẫn hallucinate và trả lời sai. Lỗi nằm ở đâu?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"22065a33-75ad-5b1f-8488-f209b97be57f","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"8c00734dec46c762d56e2bcf2c604ccf82b0371b7c442570cf10514b4683cb1b"} -->

## Slide 3 - Nội Dung Bài Học

1. The RAG Paradigm & Indexing Architecture

2. Query Processing & Advanced Retrieval

3. Generation, Grounding & UX

4. The RAG Evaluation Triad

5. Lab 8 + deliverable Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 1 / 32

---

<!-- chiron-source-span: {"source_span_id":"1f41d354-a5b8-50b8-bb3e-6426c96bfd5e","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu Ngày 8","extraction_method":"pdf-text-layer"},"checksum":"8577baf7b0be5203b23f9dfb2b7237413e1048377501df06cceb77f3f3f1a6ef"} -->

## Slide 4 - Mục Tiêu Ngày 8

- Giải thích được RAG như một pipeline gồm indexing, retrieval,
re-ranking, và generation

- Hiểu vì sao retrieval quality thường quyết định chất lượng câu trả lời
nhiều hơn prompt viết đẹp

- So sánh được dense, sparse, hybrid retrieval và biết khi nào cần rerank

- Thiết kế được prompt grounding để model trả lời từ context thay vì bịa
thêm

- Đo được chất lượng RAG bằng faithfulness, relevance,
context recall/completeness Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 2 / 32

---

<!-- chiron-source-span: {"source_span_id":"823cd3f1-e509-52b8-b0a4-c6ec3d6b240f","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"6f4674e784be6011492dd0ae940ab0f102b736ec645742aaf111f2cb54c51be3"} -->

## Slide 5 - Deliverable Cuối Ngày

Full RAG pipeline với index, retrieval, answer function, 10 test questions, và scorecard đánh giá chất lượng

- 1 pipeline index → retrieve → rerank/select → generate

- 1 bộ câu hỏi test có expected evidence hoặc expected answer

- 1 bảng điểm ngắn để so sánh baseline và bản tuning đầu tiên
Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 3 / 32

---

<!-- chiron-source-span: {"source_span_id":"5e328842-f5e0-5c42-bdc9-fc4098c2de36","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"The RAG Paradigm","extraction_method":"pdf-text-layer"},"checksum":"afb5285d80ae80c0006dfd8597487dfb62ce6db996fc816534cb3bb6c254d50a"} -->

## Slide 6 - The RAG Paradigm

1 & Indexing Architecture RAG is not just adding context; it is a synergistic orchestration of indexing, retrieval, and generation systems to ensure factual grounding and accuracy.

---

<!-- chiron-source-span: {"source_span_id":"12df3848-ac94-59b0-bfdd-c1824979d0fc","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"1.1 The Need for RAG","extraction_method":"pdf-text-layer"},"checksum":"af5bedaab07b64eeba98308289d61353171b3a4107fa8871844bc811de715870"} -->

## Slide 7 - 1.1 The Need for RAG

Understanding why standard LLMs fall short and how RAG bridging the gap between static knowledge and dynamic, factual accuracy.

---

<!-- chiron-source-span: {"source_span_id":"9c664a51-13d3-5276-9c95-c770f6564956","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Ảo Giác Của LLM (The Illusion of Knowledge)","extraction_method":"pdf-text-layer"},"checksum":"02962e90e0ca30052137225007e7d25c432cfa994dc2d3bed554966fd2fe5cea"} -->

## Slide 8 - Ảo Giác Của LLM (The Illusion of Knowledge)

Kiến thức bị đóng băng (Knowledge Cutoff) LLM chỉ biết những gì đã xảy ra trước ngày training. Thông tin nội bộ hay sự kiện mới là điểm mù. Bản chất xác suất (Probabilistic Nature) LLM là cỗ máy dự đoán từ tiếp theo, ưu tiên sự trôi chảy (fluency) hơn tính chính xác (factual accuracy). Hệ quả - Hallucination Khi thiếu dữ kiện, model sẽ tự động "bịa" ra thông tin trông rất logic và tự tin để làm hài lòng người dùng. Giảng viên AICB · Ngày 8 Tuần 2AICB · Ngày 8 8 Tuần 2 4 / 32

---

<!-- chiron-source-span: {"source_span_id":"23a4ed47-3fd0-52e2-8f16-cb264a693249","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Fine-tuning vs. RAG (Hai Cách Tiếp Cận Khác Nhau)","extraction_method":"pdf-text-layer"},"checksum":"9139c6b657996797bba4859dae3ce461ffb20fecf8d894ae4f3081f18c39d66a"} -->

## Slide 9 - Fine-tuning vs. RAG (Hai Cách Tiếp Cận Khác Nhau)

Fine-tuning (Học phong cách) Phù hợp để thay đổi cách model nói chuyện (tone, format), nhưng cực kỳ kém và đắt đỏ nếu dùng để nhồi nhét sự kiện (facts). Trí nhớ mạng nơ-ron rất dễ bị "catastrophic forgetting". RAG (Cung cấp tài liệu) Phù hợp để truy xuất thông tin thực tế. Giống như việc cho học sinh mang tài liệu vào phòng thi "Open-book exam" thay vì bắt học thuộc lòng. Metric Fine-tuning RAG Cost to Update Cao (Retraining required) Thấp (Update index) Risk of Hallucination Cao (Static knowledge) Thấp (Grounded in facts) Dynamic Access Control Khó (All-in-one weights) Dễ (Document-level permissions) Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"dd70ce07-0eab-5433-b335-077725700cfb","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"RAG Là Gì? (Retrieval-Augmented Generation)","extraction_method":"pdf-text-layer"},"checksum":"98023b44326dee7db49f70eecdadbf6f6ff2a8561367ebc5c7a6fa9656ce6259"} -->

## Slide 10 - RAG Là Gì? (Retrieval-Augmented Generation)

### Sự kết hợp của 2 cỗ máy
RAG ghép nối sức mạnh tìm kiếm của một Search Engine với khả năng tổng hợp ngôn ngữ của LLM.

### Quy trình ngược
Thay vì hỏi model ngay lập tức, ta chặn câu hỏi lại → dùng nó để truy vấn cơ sở dữ liệu → lấy bài viết liên quan nhất → ép model đọc bài viết đó để trả lời. User Question Search DB Extract Context Prompt LLM Grounded Answer Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"06383fb2-7303-5569-94b7-5f5ac048c642","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Vì Sao Doanh Nghiệp Bắt Buộc Phải Dùng RAG?","extraction_method":"pdf-text-layer"},"checksum":"95e356995a8734171a3f95a68b5f6917bcd3573fd5113a9a13813b7f27080b98"} -->

## Slide 11 - Vì Sao Doanh Nghiệp Bắt Buộc Phải Dùng RAG?

 Nguồn gốc rõ ràng (Auditability): Mọi câu trả lời đều có thể đính kèm đường link trích dẫn (citation). Nếu AI trả lời sai, ta biết ngay là do tài liệu sai hay do AI suy diễn.  Bảo mật & Phân quyền (Access Control / RBAC): LLM không lưu dữ liệu. Người dùng A ở phòng Marketing chỉ được phép search (retrieve) các tài liệu mà họ có quyền xem.  Cập nhật Real-time (Freshness): Khi chính sách thay đổi, chỉ cần xóa file cũ / thêm file mới vào Vector DB. Không cần train lại model. Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"2b8db04f-1531-56a6-b030-ba2126097d8e","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Data-Centric AI Trong Kỷ Nguyên LLM","extraction_method":"pdf-text-layer"},"checksum":"d45f303a930ece009dec8bb51e8eae7e7ba27c747c5dec698c03071a92bcf4eb"} -->

## Slide 12 - Data-Centric AI Trong Kỷ Nguyên LLM

 Các model (GPT-4, Gemini, Claude) đang dần trở thành "hàng hóa cơ bản" (commodity) với sức mạnh tương đương nhau.  Sự khác biệt của một sản phẩm AI doanh nghiệp nằm ở hệ thống dữ liệu. Pipeline xử lý, làm sạch và tìm kiếm dữ liệu mới là lợi thế cạnh tranh cốt lõi.  "Rác vào, rác ra" (Garbage In, Garbage Out): Nếu retrieval mang về thông tin nhiễu, prompt kỹ thuật đến đâu cũng vô dụng. ⚠ Your LLM is only as smart as your retrieval system. Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"4671d6e5-a0e3-5ff6-a1f3-2c1424851b19","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"1.2 High-level RAG Architecture","extraction_method":"pdf-text-layer"},"checksum":"557ac7b4a45e6fbe3f4236de619fe0b5f6833e0a8c4b47fdea0ae551db1684b2"} -->

## Slide 13 - 1.2 High-level RAG Architecture

The anatomy of a RAG pipeline: How Indexing, Retrieval, and Generation work together to build a reliable search-and-synthesize engine.

---

<!-- chiron-source-span: {"source_span_id":"a05bce73-c655-5e39-a326-22635cf727c8","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"RAG = 3 Pipeline Phối Hợp","extraction_method":"pdf-text-layer"},"checksum":"cb65438e69bf02944b34de6f3eb8050a4ca82a5d5b360bc73ac26ce66c8bfb2b"} -->

## Slide 14 - RAG = 3 Pipeline Phối Hợp

RAG không phải là một hàm API gọi một lần. Nó là một hệ thống phân tán gồm 3 khối kiến trúc

### riêng biệt chạy nối tiếp nhau

1. Indexing Xử lý và chuẩn hóa tài liệu (Chạy ngầm/Offline).

2. Retrieval Tìm kiếm và chọn lọc ngữ cảnh (Chạy Real-time khi user hỏi).

3. Generation Lắp ghép prompt và sinh ngôn ngữ (Chạy Real-time). Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"9e1b6bc9-760c-5e11-ad8d-e692bd990c01","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Bước 1 - Indexing Pipeline (Xây Nền Móng)","extraction_method":"pdf-text-layer"},"checksum":"456e1874259f9b5eb798781c1b6b04aaa6ea91a65b16d1eeee581e8d6684edfd"} -->

## Slide 15 - Bước 1 - Indexing Pipeline (Xây Nền Móng)

- Đây là quá trình ETL (Extract, Transform, Load) dành cho dữ liệu phi cấu trúc.

- Mục tiêu: Biến các file PDF, Word, HTML khổng lồ thành các đoạn thông tin nhỏ (chunks),
mã hóa chúng thành số (vectors), và lưu vào Database chuyên dụng.

1. Shredding (Chunking)

2. AI Embedding

3. Vector DB Storage Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"2ad8cb8a-5f43-51af-9911-a3efa024d0a6","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Bước 2 - Retrieval Pipeline (Động Cơ Tìm Kiếm)","extraction_method":"pdf-text-layer"},"checksum":"9dad2ad66f78e2439b70c1ce8a9246f78ce445c85e196a17f9e2060b95fce0cc"} -->

## Slide 16 - Bước 2 - Retrieval Pipeline (Động Cơ Tìm Kiếm)

- Khi user đặt câu hỏi, hệ thống cũng phải mã hóa câu hỏi đó thành vector
bằng đúng model đã dùng ở bước Indexing.

- Sử dụng thuật toán k-NN (K-Nearest Neighbors) hoặc ANN (Approximate
Nearest Neighbors) để tính khoảng cách trong không gian toán học, từ đó rút ra top K đoạn văn bản gần nghĩa nhất. Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"fe4f61bf-e7fd-5c7d-8719-9d8622956417","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Bước 3 - Generation Pipeline (Tổng Hợp & Trình Bày)","extraction_method":"pdf-text-layer"},"checksum":"3ee31865ff7ef4ec7dcda1b46f0f7c13f06a96d3e894317df2e9c98c773a95ce"} -->

## Slide 17 - Bước 3 - Generation Pipeline (Tổng Hợp & Trình Bày)

- Thông tin thô từ DB rất lộn xộn và khó đọc. LLM đóng vai trò là "biên tập viên".

- Đưa toàn bộ ngữ cảnh tìm được vào System Prompt kèm theo lệnh giới hạn nghiêm
ngặt: "Chỉ trả lời dựa trên tài liệu được cung cấp".

- Xử lý ngoại lệ: Nếu DB trả về kết quả rỗng, LLM phải được lập trình để xin lỗi và báo
thiếu dữ liệu. Raw Chunks (Metadata) {id: 104, score: 0.89, txt: "quy trình..."} {id: 205, score: 0.82, txt: "mã hóa..."} {id: 091, score: 0.78, txt: "vector DB..."} Retrieved Information

### AI Response

- Quy trình gồm 3 bước chính.

- Dữ liệu được mã hóa vector.

- Lưu trữ tại cơ sở dữ liệu.
Cohesive Answer Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"2dc49524-a4a4-56ed-aa03-e48650584824","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Nút Cổ Chai Thực Sự Nằm Ở Đâu?","extraction_method":"pdf-text-layer"},"checksum":"5b0c9b089becb0908d2b118cadade703dbbe9d00a1b45f2b3a72e80d94bcace5"} -->

## Slide 18 - Nút Cổ Chai Thực Sự Nằm Ở Đâu?

Khi test RAG thấy kết quả sai, kỹ sư thường vội vàng nhảy vào sửa Prompt hoặc đổi model lớn hơn. Đây là sai lầm! 80% Lỗi do Retrieval

- Truy vấn tìm sai tài liệu

- Thiếu chứng cứ quan trọng

- Nhồi quá nhiều rác (noise)
20% Lỗi do Generation

- Model bỏ qua chứng cứ

- Ảo giác sinh thêm chi tiết

- Định dạng sai
Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"1d6c2fe1-86dc-558d-86b1-31c2a60693a1","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"1.3 Document Parsing & Ingestion","extraction_method":"pdf-text-layer"},"checksum":"bfc5f4e58f1b1243e01004a183214ce8c0c59e06e17d1ababaab96d7411cbde4"} -->

## Slide 19 - 1.3 Document Parsing & Ingestion

Tackle the complexities of parsing multi-column PDFs, extracting nested tables, and building a robust ingestion pipeline to feed your database.

---

<!-- chiron-source-span: {"source_span_id":"598e2654-a570-5055-9828-67e249586957","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Dữ Liệu Thực Tế Luôn Lộn Xộn","extraction_method":"pdf-text-layer"},"checksum":"287c682f04143be080be12122fe2d7c56749c2b20944f84147e1370e6cfea27b"} -->

## Slide 20 - Dữ Liệu Thực Tế Luôn Lộn Xộn

Các khóa học thường demo bằng file

### .txt sạch sẽ. Thực tế doanh nghiệp là

- PDF scan (hóa đơn, hợp đồng)

- Email cũ (nhiều ký tự lạ)

- Slide thuyết trình (layout phức
tạp) Giảng viên AICB · Ngày 8 Tuần 2 Thách thức OCR OCR kém sẽ đọc chữ "I" thành số "1", làm hỏng toàn bộ keyword quan trọng.

---

<!-- chiron-source-span: {"source_span_id":"1d368ec4-81a6-5dd2-b421-5df5f733d95a","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Thử Thách Parse PDF (Vấn đề Layout)","extraction_method":"pdf-text-layer"},"checksum":"affd9358d505ee772b1b86cc4b670b4729d8307cb1b588db5e59f081059b7054"} -->

## Slide 21 - Thử Thách Parse PDF (Vấn đề Layout)

Vấn Đề Kỹ Thuật

- Chuẩn PDF sinh ra để in ấn, nó lưu tọa độ (x, y) của chữ chứ không
hiểu cấu trúc ngữ nghĩa (đâu là tiêu đề, đâu là đoạn văn).

- Lỗi layout: Các parser cơ bản thường đọc từ trái sang phải, làm trộn
lẫn văn bản giữa 2 cột riêng biệt thành một câu vô nghĩa.

- Nhiễu Header/Footer: Số trang và tiêu đề lặp lại ở mọi trang sẽ làm
bẩn database nếu không được gỡ bỏ. Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"e3961c03-3682-5beb-9884-a84140b6d4e8","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Cơn Ác Mộng Mang Tên \"Bảng Biểu\" (Tables)","extraction_method":"pdf-text-layer"},"checksum":"a1ad75decfb42323a47d4ee091f25218047a949b0872e9d8e3b91b0f156b55f4"} -->

## Slide 22 - Cơn Ác Mộng Mang Tên "Bảng Biểu" (Tables)

Nếu dùng thuật toán cắt text thông thường, bảng bị xẻ làm đôi. Nửa dưới mất liên kết với Header → Vector vô dụng. Giải pháp tối ưu: Phải dùng parser chuyên dụng (LlamaParse, Unstructured) để bóc tách thành HTML/Markdown. Original PDF Table Raw Text "Soup" Basic Pro Enterprise $9/month $29/month $99/month 10Gb Storage 50GB Storage Unlimited Storage Markdown/HTML | Basic | Pro | Enterprise | |$9/month | $29/month | $99/month | |---|---|---| |10Gb Storage | 50GB Storage | Unlimited Storage | Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"02a1ac12-5fbd-55bb-8bdb-fcb076967e7a","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Multimodal Parsing (Dùng Vision Model)","extraction_method":"pdf-text-layer"},"checksum":"b3a0d2681691065e28233387445b4309511b16d3c3127867900878514878a31f"} -->

## Slide 23 - Multimodal Parsing (Dùng Vision Model)

Thay vì dùng công cụ bóc chữ truyền thống, ta ném thẳng ảnh chụp trang tài liệu cho Vision LLMs (như Gemini 1.5 Pro hoặc GPT-4o).

### Ưu điểm

- Hiểu được cấu trúc siêu phức tạp.

- Đọc được biểu đồ (charts).

- Lưu lại được diễn giải hình ảnh.

### Nhược điểm

- Tốn kém chi phí API.

- Chạy chậm (không phù hợp cho kho dữ liệu
hàng triệu trang). Visual Pipeline Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"f72ef810-bc3d-5b03-a175-33c3377634d8","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Làm Sạch Dữ Liệu (Data Cleaning)","extraction_method":"pdf-text-layer"},"checksum":"e0e52f1327b4ca250ce41cb1b3dbd6ec0b2082aef7cc2d9d2278e7aa2a4e4823"} -->

## Slide 24 - Làm Sạch Dữ Liệu (Data Cleaning)

Chuẩn hóa (Normalization): Gộp các khoảng trắng thừa, sửa lỗi unicode (font tiếng Việt cũ), xóa các ký tự điều khiển (control characters) làm rối model. Redaction (Che mờ PII): Xóa thông tin cá nhân (CCCD, số thẻ tín dụng, số điện thoại) trước khi đưa lên Cloud Vector DB để đảm bảo tuân thủ bảo mật (GDPR/PDPA). Ví dụ minh họa (Example)

### "KH Nguy ễn Văn A, \n\n SDT
0901234567"

### Cleaned: "KH [REDACTED], SDT
[REDACTED]" Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"7954485c-cce6-560d-90f0-7415144c8b21","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Chiến Lược Ingestion Dữ Liệu","extraction_method":"pdf-text-layer"},"checksum":"e361a456020f2980085f4f55534fae2fe115e3151991ed51796e15d00e0adcf7"} -->

## Slide 25 - Chiến Lược Ingestion Dữ Liệu

Batch Processing Cập nhật định kỳ (VD: quét lại toàn bộ Google Drive vào 12h đêm). Dễ triển khai nhưng thông tin bị trễ (stale data). Event-Driven (Delta Sync) Dùng Webhook bắt sự kiện. Chỉ khi nào có user sửa file trên Confluence, hệ thống mới trigger job cập nhật riêng file đó. Idempotency: Phải thiết kế hệ thống băm (hashing) nội dung để tránh việc lưu trùng lặp một chunk văn bản nhiều lần. Visual Workflow: Event-Driven Pipeline User Edits CMS Webhook Trigger Hash Check (Is content new?) Parse & Embed Upsert DB Giảng viên AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"58555e7c-1bbf-51e4-adc9-7699d1e0c45d","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"1.4 Advanced Chunking Strategies","extraction_method":"pdf-text-layer"},"checksum":"eb9b04550c5fed6816c44d8098afac61f133c1ca2277304a4764b4c28c7f33f0"} -->

## Slide 26 - 1.4 Advanced Chunking Strategies

Beyond naive character splitting: Exploring recursive, structural, and semantic chunking strategies to preserve document context and maximize retrieval accuracy.

---

<!-- chiron-source-span: {"source_span_id":"47619d4d-8fc1-52f4-9843-dc09b49bd1fd","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Chunking Là Gì? Tại Sao Không Lưu Cả Bài?","extraction_method":"pdf-text-layer"},"checksum":"89a4e28713388c2d61602d6e881c6773fa055a1ab0f196aea5d1703e1229a3ad"} -->

## Slide 27 - Chunking Là Gì? Tại Sao Không Lưu Cả Bài?

Giới hạn Context Window Dù LLM hiện nay hỗ trợ ngữ cảnh dài (ví dụ Gemini 1.5 hỗ trợ 2M tokens), việc nhét cả nghìn trang tài liệu vào prompt rất đắt tiền và tốn thời gian phản hồi (TTFT). Giảm nhiễu (Noise) Vector Search tìm "mật độ" ý nghĩa. Nếu nhúng cả một chương sách vào 1 vector, các ý chính sẽ bị pha loãng, rất khó khớp với câu hỏi cụ thể của user. Giảng viên (VinUni) AICB · Ngày 8 Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"4efaa260-3cde-5e58-b143-977cccecd69e","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Chiến Lược 1 - Cắt Theo Kích Thước (Fixed-Size)","extraction_method":"pdf-text-layer"},"checksum":"e0a503330e8cc077ebd31f1a417423bed8d4d7207c0319fb507f3b5f584703e2"} -->

## Slide 28 - Chiến Lược 1 - Cắt Theo Kích Thước (Fixed-Size)

Đặc điểm & Đánh giá

- Cắt cơ học theo số lượng ký tự hoặc token (Ví
dụ: Cứ 500 ký tự thì chém 1 nhát).

### Ưu điểm
Cực kỳ dễ code, chạy nhanh, dự đoán được chính xác dung lượng database.

### Nhược điểm (Tử huyệt)
Rất dễ cắt ngang một câu, làm đứt đoạn ngữ nghĩa (ví dụ: cắt giữa chữ "không" và "được phép"). Chính sách này áp dụng cho toàn bộ nhân viên ngoại | trừ thực tập sinh. Nghĩa của câu bị chia đôi tại điểm cắt Giảng viên (VinUni) AICB · Chiến lược Chunking Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"6f64e168-820a-504e-8cc1-445bb378d2df","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Chiến Lược 2 - Cắt Đệ Quy (Recursive Chunking)","extraction_method":"pdf-text-layer"},"checksum":"09001f5e11726d5b250a6176fce5e68b54003e14f396a6bad0da0af7db0490bc"} -->

## Slide 29 - Chiến Lược 2 - Cắt Đệ Quy (Recursive Chunking)

Đặc điểm & Cách hoạt động

- Đây là tiêu chuẩn vàng mặc định (Default
standard) trong LangChain. Thay vì cắt mù quáng, nó cố gắng tôn trọng ranh giới ngôn ngữ bằng cách thử cắt theo thứ tự ưu

### tiên

1. Cắt ở khoảng trống giữa 2 đoạn văn (\n\n).

2. Nếu đoạn vẫn quá dài, cắt ở ký tự xuống dòng (\n).

3. Nếu vẫn dài, cắt ở dấu chấm câu (.). Fallback Logic Tree Split by Paragraph (\n\n) Fallback: Sentence (\n or.) Fallback: Word / Character Giảng viên (VinUni) AICB · Chiến lược Chunking Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"307b1ef1-9382-54a9-8935-3969fb1575e6","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Chiến Lược 3 - Cắt Theo Cấu Trúc (Semantic/Structural)","extraction_method":"pdf-text-layer"},"checksum":"209585a5ab6c25dd3af658eb99620a5369cd979fd0cad82054535006c9852168"} -->

## Slide 30 - Chiến Lược 3 - Cắt Theo Cấu Trúc (Semantic/Structural)

Đặc điểm & Ứng dụng

- Không quan tâm độ dài, chỉ cắt dựa trên cấu
trúc logic của tài liệu.

- Markdown/HTML: Tách riêng các phần dưới
thẻ <H1>, <H2>.

- Code: Dùng AST (Abstract Syntax Tree) để tách
riêng từng function (hàm) hoặc class, đảm bảo không một hàm Python nào bị cắt đứt làm đôi. # Heading 1 ............................ .................................. ## Sub-heading A ............................ ................... ## Sub-heading B ............................ .................................. Giảng viên (VinUni) AICB · Chiến lược Chunking Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"bafd4302-ec2a-5f52-abd9-fc45c26799dc","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Tại Sao Cần Overlap (Phần Gối Nhau)?","extraction_method":"pdf-text-layer"},"checksum":"b14e7eb767105c1fae56b542c4af8644d3d9e85ea4e18e80e2c1d0c497ecd854"} -->

## Slide 31 - Tại Sao Cần Overlap (Phần Gối Nhau)?

- Khi chia văn bản, một ý quan trọng có thể
vô tình bị chia làm 2 mảnh nằm ở mép của 2 chunk khác nhau.

- Overlap (Khoảng lặp lại): Cho phép
đoạn cuối của Chunk 1 được lặp lại ở đoạn đầu của Chunk 2 (thường set khoảng 10-15% tổng size).

- Việc này hoạt động như chất "keo dính"
giữ lại mạch ngữ cảnh. Chunk 1 ... nội dung văn bản phần đầu... Overlap Chunk 2 ... tiếp nối nội dung từ overlap... Overlap Giảng viên (VinUni) AICB · Chiến lược Chunking Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"0347b674-2df5-589d-8338-966f3f8dcae7","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Small-to-Big Retrieval (Parent-Child Indexing)","extraction_method":"pdf-text-layer"},"checksum":"95f7d4d4b8830c7ce65eb0140375608724c5b4a5d4624e4983806fb99cf9e55d"} -->

## Slide 32 - Small-to-Big Retrieval (Parent-Child Indexing)

- Vấn đề: Chunk nhỏ thì search chính xác
nhưng thiếu ngữ cảnh. Chunk to thì search dễ trượt nhưng ngữ cảnh dồi dào.

- Giải pháp Parent-Child: Lưu trữ các chunk
là những câu siêu ngắn (Small) để chạy Vector Search lấy độ chính xác cao.

- Khi tìm trúng câu nhỏ đó, hệ thống sẽ tự
động móc nối và gửi toàn bộ đoạn văn lớn chứa câu đó (Parent) vào LLM Prompt. Parent Chunk Child 1 (Small) Child 2 (Search Hit) Child 3 (Small) Search To LLM Prompt (Full Context Included) Giảng viên (VinUni) AICB · Small-to-Big Retrieval Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"72aa2e7f-759b-5f95-9b2a-109d03be67c2","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Xử Lý Chunking Riêng Cho Bảng Biểu","extraction_method":"pdf-text-layer"},"checksum":"9ba9e668fa98934ddcaeed61b9e12676c7e5a187c2e9c2416c3ed44e73aaf074"} -->

## Slide 33 - Xử Lý Chunking Riêng Cho Bảng Biểu

- Bảng biểu không có câu văn hoàn chỉnh,
vector search rất khó bắt nghĩa.

- Cách 1 - Row to Text: Biến từng dòng của
bảng thành một câu văn tự nhiên (VD: "Sản phẩm iPhone 15 có giá 20 triệu, tồn kho 5 chiếc").

- Cách 2 - LLM Summarization: Dùng LLM
đọc toàn bộ bảng, viết 1 đoạn tóm tắt ý chính của bảng đó, và lưu đoạn tóm tắt đó thành vector đại diện cho cái bảng. Giảng viên (VinUni) AICB · Chunking cho Bảng biểu Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"61c1d88b-1996-5979-be1b-1e5f2d23c5fb","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Chunking Tốt Và Chunking Tệ","extraction_method":"pdf-text-layer"},"checksum":"882dcd619be92c77fe4ca53a982fd88a0618806d3a17d9624fa227a322503f78"} -->

## Slide 34 - Chunking Tốt Và Chunking Tệ

Chunking tệ

- cắt giữa một bảng hoặc
điều khoản

- quá to: nhiều ý không liên
quan

- quá nhỏ: mất ngữ cảnh và
thiếu source

### Ví dụ
Điều kiện hoàn tiền được áp dụng khi... ... khách hàng gửi yêu cầu trong vòng 7 ngày làm việc kể từ thời điểm xác nhận... Chunking tốt

- cắt theo heading,
section, paragraph tự nhiên

- có overlap vừa đủ

- giữ source, section, date

- retriever hiểu ngữ nghĩa trọn
vẹn hơn

### Ví dụ
Hoàn tiền - Điều kiện áp dụng Yêu cầu được gửi trong 7 ngày... Source: policy/refund-v4.pdf · Điều 3 Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 8 / 32

---

<!-- chiron-source-span: {"source_span_id":"00d3b8e5-aaf1-5b7f-94a8-c5bd41726003","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"1.5 Embeddings & Metadata","extraction_method":"pdf-text-layer"},"checksum":"6120c26974dda1f950c5749b853f6e2c1353efa70399cfad2b3a0996e3275022"} -->

## Slide 35 - 1.5 Embeddings & Metadata

Beyond naive character splitting: Exploring recursive, structural, and semantic chunking strategies to preserve document context and maximize retrieval accuracy.

---

<!-- chiron-source-span: {"source_span_id":"ab0d1e8b-88fe-5ffe-8c24-4dc8fbace6d4","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Embedding Là Gì? (Biến Chữ Thành Số)","extraction_method":"pdf-text-layer"},"checksum":"efa17e74abb2666e77f0a423aeddfd52cedbbbe57eda1f3069f2b67f4ec26463"} -->

## Slide 36 - Embedding Là Gì? (Biến Chữ Thành Số)

Bản chất của Embedding Mô hình máy học không hiểu được ngôn ngữ của con người. Embedding là phép biến đổi toán học chuyển một câu thành một dải số (Vector). Không gian ngữ nghĩa Các câu có ý nghĩa giống nhau (dù dùng từ vựng hoàn toàn khác nhau) sẽ có điểm tọa độ nằm sát nhau trong không gian đa chiều (Semantic space). Giảng viên (VinUni) AICB · Chunking cho Bảng biểu Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"e90d7f51-e5cb-52a7-acc1-fc95f4de5e8f","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Lựa Chọn Embedding Model Cho Production","extraction_method":"pdf-text-layer"},"checksum":"cb15d8802b72eb3b8ae9fc6af3d5aa1a2ca08ca53e5f52ccba07045148926f05"} -->

## Slide 37 - Lựa Chọn Embedding Model Cho Production

Số chiều (Dimensions) Model nhỏ (như bge-micro, 384 chiều) tính toán siêu nhanh, ít tốn RAM. Model lớn (OpenAI, 1536 chiều) phân biệt nghĩa tinh tế hơn nhưng chi phí hạ tầng cao gấp 4 lần. Rào cản ngôn ngữ Đừng dùng model chuyên tiếng Anh cho văn bản tiếng Việt. Phải chọn các model Multilingual (m-E5, Cohere Multilingual) để mapping ngôn ngữ tốt. Giảng viên (VinUni) AICB · Lựa chọn Model Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"7c2ebea5-43ba-5565-9297-d141ac27758c","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Điểm Mù Của Vector Search","extraction_method":"pdf-text-layer"},"checksum":"0ce6557b8703c3affe12258666f26de46996140c58444604e01938d4d36d6cfb"} -->

## Slide 38 - Điểm Mù Của Vector Search

Hạn chế của Vector Search

- Vector hoàn hảo trong việc hiểu "ý
nghĩa" và "diễn đạt lại".

- Tuy nhiên, Vector cực kỳ tồi tệ khi đối

### mặt với Exact Match (Khớp chính xác)
Mã hợp đồng, ID lỗi (ERR-809), số series.

- Model nhúng có thể xếp ERR-809 và
ERR-810 sát cạnh nhau vì cấu trúc giống nhau, dẫn đến trả lời nhầm. Giảng viên (VinUni) AICB · Vector Search Blindspots Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"68df94a2-2ef2-5f22-8d7f-5437cb3d7bcf","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Metadata - Cứu Tinh Của Khả Năng Lọc (Filtering)","extraction_method":"pdf-text-layer"},"checksum":"5cf0a868ed9faaa97ac02b189517f54560aa702b9f434c827f7b445326e56f3a"} -->

## Slide 39 - Metadata - Cứu Tinh Của Khả Năng Lọc (Filtering)

Tại sao Metadata lại quan trọng?

- Đừng bao giờ chỉ đẩy "Raw Text" vào
Database. Việc gắn thẻ dữ liệu (Tagging/Metadata) là bắt buộc.

- Một chunk tốt phải mang theo "giấy tờ
tùy thân": source_file, doc_type, date_created, department_owner.

- Lợi ích: Cho phép cắt giảm không gian
tìm kiếm trước khi chạy thuật toán vector nặng nề. // JSON Object Payload Example

```text
{
```
"text": "Nội dung đi ều kho ản...",

```text
"metadata": {
```
"source": "hr_policy.pdf", "year": 2026, "access": "internal" } } Giảng viên (VinUni) AICB · Metadata Filter Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"84ef999d-efcb-55aa-8673-8eda4370c652","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Pre-filtering vs. Post-filtering","extraction_method":"pdf-text-layer"},"checksum":"3c3b85aad922e2f39f0a9aa7c6b4b6c365ca0c947efa5f45accf9252c5877058"} -->

## Slide 40 - Pre-filtering vs. Post-filtering

Post-filtering (Lọc sau) Search top 100 vector gần nhất, sau đó loại bỏ những kết quả không thuộc năm 2026. Rủi ro: Có thể bị rớt mất tài liệu quan trọng nếu nó nằm ở hạng 101. Pre-filtering (Lọc trước) Yêu cầu DB chỉ nhìn vào vùng không gian chứa tài liệu năm 2026, rồi mới chạy Vector Search. Nhanh hơn, an toàn hơn, và chính xác tuyệt đối. Vector Search Filter Filter Vector Search Giảng viên (VinUni) AICB · Filtering Architectures Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"59ff3e27-227e-5cd7-a487-976c9737e6e3","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Code Ingestion Tối Thiểu (Python)","extraction_method":"pdf-text-layer"},"checksum":"f9bf9672ea8e1fe542ddedeaba01cdd14028f3312701a5a2ab2c25f4c90cee7c"} -->

## Slide 41 - Code Ingestion Tối Thiểu (Python)

Một kịch bản chuẩn bị dữ liệu tiêu chuẩn sử dụng TextSplitter và Vectorstore. # Import các th ư vi ện c ần thi ết

```text
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
```
# Thi ết l ập c ắt đ ệ quy kèm overlap text_splitter = RecursiveCharacterTextSplitter( chunk_size=1000, chunk_overlap=150 ) # C ắt doc và nh ồi metadata chunks = text_splitter.split_documents(raw_documents)

### for chunk in chunks
chunk.metadata["source"] = "Q1_Report" # L ưu vào Vector DB vectorstore = Chroma.from_documents( documents=chunks, embedding=embeddings ) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"7b4becd8-8779-5207-94d7-880da257aca3","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Query Processing & Advance","extraction_method":"pdf-text-layer"},"checksum":"77bd88eac342e7317c65eb048cf3c75bdbbccec63ac67ef014e34c88c331e3e4"} -->

## Slide 42 - Query Processing & Advance

2 Retrieval Moving beyond basic semantic search: How to transform ambiguous user queries, leverage the power of hybrid retrieval, and use cross-encoder re-ranking to extract the highest quality context.

---

<!-- chiron-source-span: {"source_span_id":"e2609c1b-2c23-5d91-a4ce-7ab9539ff19d","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"2.1 Query Transformation","extraction_method":"pdf-text-layer"},"checksum":"3e12dc7515aa606ab9f49b3acac90f8a8b362b0cd8083934041d401b8b3dbb5f"} -->

## Slide 43 - 2.1 Query Transformation

Learn how to intercept, expand, decompose, and transform ambiguous user inputs into highly optimized search queries using LLMs.

---

<!-- chiron-source-span: {"source_span_id":"4f375c3f-a45f-538d-9b01-61b3ead627d2","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Người Dùng Không Bao Giờ Hỏi Đúng","extraction_method":"pdf-text-layer"},"checksum":"8690cf0beaab149d426c5a359576c552a559a7618cd88ddfca243403105ee64b"} -->

## Slide 44 - Người Dùng Không Bao Giờ Hỏi Đúng

Khoảng cách từ vựng Người dùng dùng ngôn ngữ "đường phố" hoặc mơ hồ. Tài liệu nội bộ dùng ngôn ngữ chuyên môn trang trọng. Thiếu ngữ cảnh Câu hỏi cụt lủn (vd: "hoàn tiền") khiến Vector DB trả về quá nhiều kết quả nhiễu. Kết luận: Nếu lấy raw query đi search thẳng, Retriever sẽ thất bại ngay từ giây đầu tiên. "sao app cứ văng" Troubleshooting Unhandled Exceptions Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"5acca033-64d1-55c3-a899-58edce169590","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Giảng viên (VinUni) AICB · Python Ingestion Tuần 2","extraction_method":"pdf-text-layer"},"checksum":"b7933e76106f319e3942b07f05fc9cba08f5b21d279d35a19bee7745bacf9511"} -->

## Slide 45 - Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

Query Transformation Là Gì?

- Đặt một LLM nhỏ, tốc độ cao (như GPT-4o-mini, Gemini Flash) làm "màng lọc" đứng trước Vector
Database.

- LLM này đóng vai trò như một người biên tập, diễn dịch lại ý định của người dùng thành các truy vấn
tối ưu cho máy học.

- Đây là bước đệm hoàn hảo trước khi ta biến Retriever thành một "Tool" độc lập cho các Agent
(LangGraph) ở giai đoạn sau. Raw User Query LLM Router / Transformer Optimized Queries Vector Database

---

<!-- chiron-source-span: {"source_span_id":"0660ae8a-adae-53c3-9d24-1ae3a25aaa2e","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"Kỹ Thuật 1 - Query Expansion (Mở Rộng & Sửa Lỗi)","extraction_method":"pdf-text-layer"},"checksum":"8499c37def45bcc83f285b6f8f7d00a0af60e1f1bdd2742c1c8cac61c1ac9f43"} -->

## Slide 46 - Kỹ Thuật 1 - Query Expansion (Mở Rộng & Sửa Lỗi)

- Chữa lỗi chính tả và thêm các từ đồng nghĩa (synonyms) hoặc thuật ngữ chuyên ngành có
cùng nghĩa.

- Tăng mạnh độ phủ (Recall), giúp hệ thống không bỏ sót tài liệu chỉ vì người dùng dùng sai từ.
VÍ DỤ

### Raw User Query
"nghỉ đẻ"

### LLM Expanded Queries
["nghỉ thai sản", "maternity leave", "chế độ phụ sản", "trợ cấp sinh con"] Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"265b29f1-109e-50d6-bdf6-c8982c5dcd83","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Kỹ Thuật 2 - Query Decomposition (Chia Để Trị)","extraction_method":"pdf-text-layer"},"checksum":"8114e48daa4281a9b61e32a03dc7300888cfb31208e9b3f606548770ca2fba9c"} -->

## Slide 47 - Kỹ Thuật 2 - Query Decomposition (Chia Để Trị)

- Xử lý các câu hỏi phức tạp (Multi-hop). Một Vector biểu diễn tài liệu không thể đồng thời trả lời
cho hai ý niệm quá khác biệt.

- Phân tách câu hỏi lớn thành nhiều câu hỏi nhỏ, chạy tìm kiếm song song (parallel retrieval), sau
đó gộp context lại. VÍ DỤ Q: "So sánh chính sách hoàn tiền của Shopee và Tiki" Q1: "Chính sách hoàn tiền Shopee" Q2: "Chính sách hoàn tiền Tiki" Gộp Context Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"a752b7af-8991-56f0-a62f-d348194acdfe","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"Kỹ Thuật 3 - Step-Back Prompting","extraction_method":"pdf-text-layer"},"checksum":"3b5f51abd87b5f98e710732c386da2c3613e47ca6e3e8d23fbc8f34ff03d6d3d"} -->

## Slide 48 - Kỹ Thuật 3 - Step-Back Prompting

- Khi câu hỏi đi quá sâu vào tiểu tiết, model dễ bị "lạc" và không tìm thấy tài liệu chính xác (do
quá cụ thể).

- LLM tự động sinh ra một câu hỏi "lùi lại một bước" (abstract/high-level) để lấy được ngữ cảnh
quy tắc chung trước khi giải quyết ca cụ thể. VÍ DỤ User: "Lỗi 404 khi gọi API thanh toán Momo của user ID 8910"

### Step-back Q
"Kiến trúc tích hợp cổng thanh toán Momo hoạt động như thế nào?" Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"c8141831-b030-58b0-a965-169e594ddf52","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Kỹ Thuật 4 - HyDE (Hypothetical Document Embeddings)","extraction_method":"pdf-text-layer"},"checksum":"e1812fafe91c9481af44e8304699f1cfebe9e34f4e3806637ed4c81d3e050f83"} -->

## Slide 49 - Kỹ Thuật 4 - HyDE (Hypothetical Document Embeddings)

- Khái niệm: Dùng LLM "bịa" ra một câu trả lời giả định dựa trên câu hỏi của người dùng.

- Tại sao? Vì một đoạn văn bản trả lời (dù sai sự thật) sẽ có cấu trúc ngữ pháp, từ vựng và "hình
dáng toán học" cực kỳ giống với tài liệu thật đang nằm trong DB. Ta đem vector của "câu trả lời giả" đi tìm "câu trả lời thật". SƠ ĐỒ KHÁI NIỆM Question (Câu hỏi) LLM Hallucinates Sinh ra câu trả lời giả định (3 câu) Embed Hallucination Mã hóa vector Search DB Tìm "câu trả lời thật" Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"68746f1f-c506-5331-89b1-8ae41a6b3c21","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"Trực Quan Hóa Không Gian Vector Của HyDE","extraction_method":"pdf-text-layer"},"checksum":"02295d45487c79898ae3582a427de65b231ce65e70bf205b72069659b865d890"} -->

## Slide 50 - Trực Quan Hóa Không Gian Vector Của HyDE

- Vector "Câu hỏi" và "Câu trả lời" thường nằm cách xa nhau (do định dạng ngữ pháp hoàn toàn khác
biệt).

- HyDE đóng vai trò như một "phép nội suy", kéo Query Vector về đúng cụm (cluster) không gian chứa
Document Vectors. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"7505fcf3-1a61-5700-87b6-c152c0a05e31","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"Code - Query Transformation (LangChain)","extraction_method":"pdf-text-layer"},"checksum":"1feabde3816d3428c0d35f12a33191f3784b4556839367658a8050c980382b1c"} -->

## Slide 51 - Code - Query Transformation (LangChain)

- Khởi tạo MultiQueryRetriever để tự động sinh nhiều câu hỏi từ 1 prompt gốc.
Python

```text
from langchain.retrievers.multi_query import MultiQueryRetriever
prompt_template = "You are an AI assistant. Generate 3 alternative search queries for: {question}"
retriever = MultiQueryRetriever.from_llm(
retriever=vectorstore.as_retriever(),
llm=chat_model,
prompt=prompt_template
)
Giảng viên (VinUni) AICB · Python Ingestion Tuần 2
```

---

<!-- chiron-source-span: {"source_span_id":"d3ad5d9a-41c5-5983-b27b-aea2d0010397","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"Đánh Đổi Hiệu Năng (The Trade-offs)","extraction_method":"pdf-text-layer"},"checksum":"497ad288a34efc8b2c4fb91f2b699e64b80d7bbcdb94115858b74774a5e4497d"} -->

## Slide 52 - Đánh Đổi Hiệu Năng (The Trade-offs)

Được (Benefits)

- Cải thiện cực lớn độ chính xác và Recall.

- Xử lý được các ca người dùng "hỏi ngốc".
Mất (Costs)

- Tăng độ trễ (Latency) vì phải gọi API LLM
1 lần trước khi đụng vào Database.

- Tốn thêm chi phí (Token cost).
Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"d22108d7-2469-59fd-94e2-843e17e3969d","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"Checklist Cho Production","extraction_method":"pdf-text-layer"},"checksum":"ed7cc07de4cf89e92648c33ab7cc78442665767dd05057d78d8d956ae77a1bac"} -->

## Slide 53 - Checklist Cho Production

 Đừng lạm dụng! Chỉ bật Query Transformation khi hệ thống gặp nhiều user queries phức tạp/mơ hồ.  Dùng model rẻ nhất có thể (GPT-4o-mini / Haiku) cho bước này để giữ Latency < 1s.  Kết hợp với Semantic Cache để không phải transform lại các câu hỏi phổ biến. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"bde874a5-21ad-522a-b527-2788250b43e7","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"2.2 Dense vs. Sparse Retrieval","extraction_method":"pdf-text-layer"},"checksum":"bb0706890fd6283ab0414a24b3ee84b4f5d1c5ab43ab9b0ea7003bf09960998a"} -->

## Slide 54 - 2.2 Dense vs. Sparse Retrieval

Meaning vs. Keywords: Comparing the semantic understanding of dense vector embeddings against the exact-match precision of sparse retrieval algorithms like BM25.

---

<!-- chiron-source-span: {"source_span_id":"603008c7-a969-5e24-8e9e-0e0a2483dd37","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"Hai Trường Phái Tìm Kiếm Cốt Lõi","extraction_method":"pdf-text-layer"},"checksum":"cbe4680f7c2d7161c860d3204851e6386ec472774317560d3798ab5fa02b290f"} -->

## Slide 55 - Hai Trường Phái Tìm Kiếm Cốt Lõi

Dense Retrieval (Tân binh AI) Tìm theo "Ý Nghĩa" (Semantic). Mã hóa văn bản thành mảng vector dày đặc (ví dụ 1536 chiều). Sparse Retrieval (Lão làng) Tìm theo "Từ Khóa". Dựa trên tần suất xuất hiện của từ (BM25, TF-IDF, Inverted Index). Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"96f5eb17-1d2f-51bd-aa45-bfd5ac34520a","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"Mổ Xẻ Sparse Retrieval (Thuật Toán BM25)","extraction_method":"pdf-text-layer"},"checksum":"223c13c011aade6e397d5cbf07168658ea729a068def6820f91d54e1bfa5746f"} -->

## Slide 56 - Mổ Xẻ Sparse Retrieval (Thuật Toán BM25)

- Trái tim của Elasticsearch và các hệ thống
search truyền thống.

- Sparse = Vector rất dài (bằng toàn bộ số
từ trong từ điển) nhưng chứa toàn số 0.

- Nguyên lý: Đánh trọng số cực cao cho các
từ hiếm (VD: "Kubernetes") và phớt lờ các từ phổ biến (VD: "và", "là", "thì"). Sparse Vector Representation 0 0 1.2 0 0 0 5.8 0 Hầu hết các chiều là 0 (sparse). Chỉ các từ khoá xuất hiện mới có trọng số khác 0. Inverted Index Mechanism Kubernetes Doc 1 Doc 42 Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 KubernetesDocker

---

<!-- chiron-source-span: {"source_span_id":"648c675c-38de-53cc-bde4-b284d941c885","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"Khi Nào Sparse Search Xưng Vương?","extraction_method":"pdf-text-layer"},"checksum":"d87caffe31467177c20ee74d54772196537d954e96bc72885dfd4a6af19e74e8"} -->

## Slide 57 - Khi Nào Sparse Search Xưng Vương?

Vô địch Exact Match

- Khớp chính xác: Mã số thuế, ID nhân
viên, mã lỗi hệ thống (ERR-x09), từ viết tắt chuyên ngành.

- Vượt qua giới hạn tập train của LLM.

- Vector nhúng thường bị "mù" trước các
chuỗi ký tự vô nghĩa hoặc chuyên biệt này. CASE STUDY: SEARCH QUERY "ERR-X09" BM25 (Sparse) Bắn trúng ngay tài liệu chứa mã lỗi chính xác. Vector Search (Dense) Loay hoay tìm "ý nghĩa" của x09 và đưa ra kết quả noise. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"f54c2f32-2b55-5892-90cb-cc9fc24a3bff","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"Tử Huyệt Của Sparse Search","extraction_method":"pdf-text-layer"},"checksum":"eebd393d7d7abd0aa072dc9f8b0bad45c3c7b008559e19ec3a119c640f852914"} -->

## Slide 58 - Tử Huyệt Của Sparse Search

- Cực kỳ nhạy cảm với lỗi chính tả
(Typo). Sai một chữ cái là "Not Found".

- Hoàn toàn không hiểu từ đồng nghĩa
(Synonyms) hoặc diễn đạt lại (Paraphrase). VISUAL EXAMPLE: SEMANTIC GAP BM25 Result: 0 Results User searches: "Tôi muốn đòi lại tiền" Document: "Chính sách hoàn tiền" Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"caa99f8a-4830-5b21-b6a8-8429bd468a9a","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"Nhắc Lại Dense Search (Vector)","extraction_method":"pdf-text-layer"},"checksum":"010963c5f2a1c46276bb6e038eb2d93cd7c18c8db419eb050c3ab83446b16607"} -->

## Slide 59 - Nhắc Lại Dense Search (Vector)

- Bù đắp mọi điểm yếu của BM25.
Không quan tâm bạn gõ "hoàn tiền", "trả tiền", hay sai chính tả "hoang tien". Nó hiểu "ý niệm" đằng sau chuỗi ký tự.

- Khả năng Cross-lingual: User hỏi
bằng tiếng Việt, vector search vẫn map đúng vào tài liệu tiếng Anh. VISUAL EXAMPLE: DENSE SEARCH POWER Vector Search: Success User searches: "hoang tien" (Typo) Document Found: "Refund Policy" Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"7faebd65-90b8-5ad2-a80c-92fa71f49dc6","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"Điểm Mù (Blind Spots)","extraction_method":"pdf-text-layer"},"checksum":"57d0b8a78690ab7cdde5265739b16e14991b1dc846a78c06bd2acaa6ca0ecd52"} -->

## Slide 60 - Điểm Mù (Blind Spots)

- Vector Search: Tìm ý nghĩa tốt nhưng
hụt keyword.

- BM25: Tìm keyword tốt nhưng hụt ý
nghĩa. BLIND SPOT ANALYSIS Scenario 1: Dense Retrieval (Vector) Query: "Mã lỗi ERR-x09" Result: Returns general error handling docs (Misses exact ID). Scenario 2: Sparse Retrieval (BM25) Query: "Muốn lấy lại tiền" Doc: "Chính sách hoàn trả" Result: 0 Results (No keyword match). Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"9b48f03e-9536-5366-a0d8-05ab55cd0031","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"Kết Luận","extraction_method":"pdf-text-layer"},"checksum":"ccd8f2befc541ffdb7b465626165de21b6c52e6511e7e6426d2aa91c2b75c233"} -->

## Slide 61 - Kết Luận

Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Tiêu chí Sparse Retrieval (Truy xuất thưa thớt) Dense Retrieval (Truy xuất dày đặc) Cơ chế cốt lõi So khớp từ khóa chính xác (Lexical/Keyword matching). Dựa trên tần suất xuất hiện của từ. Tìm kiếm theo ngữ nghĩa và ngữ cảnh (Semantic search). Dựa trên khoảng cách giữa các vector. Biểu diễn Vector Vector có số chiều rất lớn (bằng kích thước toàn bộ từ vựng), chứa chủ yếu là các giá trị 0 (sparse). Vector có số chiều thấp và cố định (VD: 384, 768, 1536 chiều), chứa các số thực (dense). Thuật toán/Mô hình TF-IDF, BM25. Các mô hình nhúng (Embedding Models) như BERT, OpenAI Embeddings, Cohere. Điểm mạnh - Tốc độ tính toán nhanh, chi phí phần cứng thấp.- Hiệu quả tuyệt đối với các từ khóa hiếm, tên riêng, mã định danh (ID), hoặc các thuật ngữ chuyên ngành đặc thù. - Hiểu được từ đồng nghĩa, khái niệm tương đương và cấu trúc câu.- Truy xuất tốt ngay cả khi câu hỏi của người dùng và tài liệu gốc không dùng chung hệ thống từ vựng. Điểm yếu - Không hiểu được ý nghĩa của câu (sẽ thất bại nếu người dùng sử dụng từ đồng nghĩa hoặc cách diễn đạt khác).- Dễ bị nhiễu bởi các từ phổ biến nếu không lọc kỹ (stop words). - Đòi hỏi tài nguyên tính toán cao hơn (thường cần GPU để tạo embedding ở quy mô lớn).- Yêu cầu hạ tầng chuyên dụng như Vector Database và các thuật toán tìm kiếm xấp xỉ (ANN) để đảm bảo tốc độ. Ứng dụng thực tiễn Tìm kiếm chính xác các mã lỗi, tên khách hàng cụ thể, hoặc các tham số kỹ thuật trong tài liệu. Nhận diện ý định và trả lời các câu hỏi tự nhiên phức tạp của người dùng trong các hệ thống hỏi đáp (Q&A).

---

<!-- chiron-source-span: {"source_span_id":"5566570b-71ae-5e30-8931-2ad35dadb15f","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Nghịch Lý Enterprise RAG","extraction_method":"pdf-text-layer"},"checksum":"0557a7a9b7e045f892291940d93f090bbe268fd3568991f27986e33d57421ec3"} -->

## Slide 62 - Nghịch Lý Enterprise RAG

- Các tutorial YouTube chỉ dạy bạn
Vector Search vì nó "nghe có vẻ AI".

- Ở môi trường Doanh nghiệp (tra
cứu hợp đồng, log kỹ thuật, tài liệu luật), BM25 thường quan trọng hơn Vector.

- Nếu bỏ BM25, hệ thống sẽ
thất bại thảm hại. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"70efe109-1352-552c-860b-449f2440a45b","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"2.3 Hybrid Search Deep Dive","extraction_method":"pdf-text-layer"},"checksum":"dc244700d9fef720677c30d463855a02017c284e46caf2dc55a44e09d63eea3c"} -->

## Slide 63 - 2.3 Hybrid Search Deep Dive

The best of both worlds: A deep dive into Hybrid Search, combining dense semantic vectors with sparse exact-match keywords using Reciprocal Rank Fusion (RRF) and Alpha-tuning.

---

<!-- chiron-source-span: {"source_span_id":"3bb233bf-bf9e-5609-ab3c-1cf0ef561941","locator":{"kind":"page","page":64,"label":"Slide 64","section_title":"Hybrid Search: Lấy Tinh Hoa Của Cả Hai","extraction_method":"pdf-text-layer"},"checksum":"0562f440d5988becaf57d24e2250cf8019350065ba2a45525950165f3e5fdbd7"} -->

## Slide 64 - Hybrid Search: Lấy Tinh Hoa Của Cả Hai

- Khái niệm: Chạy song song cả
BM25 và Vector Search cho cùng một câu hỏi.

- Đảm bảo hệ thống không bỏ lỡ mã
số (nhờ BM25) và cũng không lọt ngữ nghĩa (nhờ Vector).

- Trở thành tiêu chuẩn bắt buộc cho
Production RAG hiện đại. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"876b9aad-d62a-5dc6-b187-65841417dff5","locator":{"kind":"page","page":65,"label":"Slide 65","section_title":"Bài Toán Khó: \"Cam và Táo\" (Score Normalization)","extraction_method":"pdf-text-layer"},"checksum":"bb9f5a9db530eac956ca135cd4ffbb13999dd07c2f3e284126e6d09cc404e704"} -->

## Slide 65 - Bài Toán Khó: "Cam và Táo" (Score Normalization)

Vector Score Cosine Similarity thường nằm trong khoảng 0.0 → 1.0 BM25 Score Không có giới hạn trên, có thể từ 0 → 100+ Thách thức Không thể cộng trực tiếp Score_Vector + Score_BM25 để xếp hạng. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"889d5abc-ccef-5d61-bd96-567ef4493a22","locator":{"kind":"page","page":66,"label":"Slide 66","section_title":"Thuật Toán Giải Quyết: RRF (Reciprocal Rank Fusion)","extraction_method":"pdf-text-layer"},"checksum":"73a1079eead480467d19ab531cabf4c3c7dfd4c315a8923a4ba76488c61db71e"} -->

## Slide 66 - Thuật Toán Giải Quyết: RRF (Reciprocal Rank Fusion)

- Đừng gộp điểm số (Scores), hãy gộp Thứ hạng (Ranks).
RRF = 1/(k + Rank_Dense) + 1/(k + Rank_Sparse) (Giá trị hằng số k thường được chọn mặc định là 60)

- Tài liệu nào nằm trong Top cao ở cả 2 bảng xếp hạng sẽ vươn lên vị trí số 1 tuyệt
đối. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"9940e328-43ee-5ee8-a688-3c2436bfd777","locator":{"kind":"page","page":67,"label":"Slide 67","section_title":"Trọng Số Alpha (Alpha Tuning)","extraction_method":"pdf-text-layer"},"checksum":"5a664b90acb088de3ab89099f9e754f11d61958b3153cdc8a4ac719d364fb743"} -->

## Slide 67 - Trọng Số Alpha (Alpha Tuning)

- Kiểm soát hệ thống nghiêng về bên nào thông qua trọng số α (0.0 đến 1.0).

- Nếu α = 1: Thuần Vector. Nếu α = 0: Thuần BM25.
Final_Score = (α × Dense_Score_norm) + ((1 - α) × Sparse_Score_norm) α = 0 α = 1 Sparse (BM25) Dense (Vector) α = 0.8 Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"b5e6822d-106a-5dc8-a7d0-38b2a51e1e88","locator":{"kind":"page","page":68,"label":"Slide 68","section_title":"Chọn Alpha Cho Từng Domain Cụ Thể","extraction_method":"pdf-text-layer"},"checksum":"bc1eae9ffb517665326d26f17a5cfbc8a5d619c30f4aaebc0ea0a689c2c9b445"} -->

## Slide 68 - Chọn Alpha Cho Từng Domain Cụ Thể

- Hệ thống Chatbot FAQ: α = 0.7 - 0.9 (Ưu tiên hiểu ý định mơ hồ của người dùng).

- Tra cứu Code, Log, Luật pháp: α = 0.2 - 0.4 (Ưu tiên khớp chính xác tên biến,
điều khoản). Chatbot FAQ α = 0.8 (Semantic) 0 1 Code / Luật pháp α = 0.3 (Keyword) 0 1 Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"09111e68-475c-5850-a18b-ee1be3ef7de0","locator":{"kind":"page","page":69,"label":"Slide 69","section_title":"Kiến Trúc Hạ Tầng Hybrid","extraction_method":"pdf-text-layer"},"checksum":"948623fe507a42034b8f05fce1734304df2ba75345dc9e4ee63ad8de10e2292e"} -->

## Slide 69 - Kiến Trúc Hạ Tầng Hybrid

- Không phải Vector DB nào cũng hỗ trợ Hybrid chuẩn. Cần database hỗ trợ lưu cả Dense
vectors và Sparse/Inverted indexes cùng lúc. Các hệ thống nổi bật hiện nay: Weaviate, Milvus, Qdrant, Elasticsearch (kết hợp plugin). Hybrid Database Cluster User Query Vector Engine Keyword Engine RRF Module Top K Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"eddff05e-b5e9-5b1b-852d-af7864781cab","locator":{"kind":"page","page":70,"label":"Slide 70","section_title":"Code Python Tối Thiểu (Chạy Local)","extraction_method":"pdf-text-layer"},"checksum":"7d3b3bfe28cc1bfb3abcf82cddc464164d333de74e88d0c4970e31003dfcb211"} -->

## Slide 70 - Code Python Tối Thiểu (Chạy Local)

- Khởi tạo Hybrid Retriever trong LangChain sử dụng thuật toán gộp.

```text
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
```
# Khởi tạo 2 bộ máy độc lập bm25_retriever = BM25Retriever.from_documents(docs) vector_retriever = faiss_index.as_retriever() # Gộp lại với trọng số Alpha (VD: 30% Keyword, 70% Vector) hybrid_retriever = EnsembleRetriever( retrievers=[bm25_retriever, vector_retriever], weights=[0.3, 0.7] ) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"68d89f92-f55c-5bef-b333-21998a05e54e","locator":{"kind":"page","page":71,"label":"Slide 71","section_title":"Lưu Ý Về Tài Nguyên & Chi Phí","extraction_method":"pdf-text-layer"},"checksum":"c35a2d8c6ebed1808f0845794b01fa075a700190acd58b5d362b242291a76d1f"} -->

## Slide 71 - Lưu Ý Về Tài Nguyên & Chi Phí

Lưu trữ (Storage) Phải nhân đôi tài nguyên lưu trữ (Build 2 index khác nhau cho cùng 1 tập dữ liệu). Hiệu năng (CPU Load) Tăng tải CPU khi truy vấn do phải chạy 2 thuật toán song song. Sự đánh đổi xứng đáng cho chất lượng Enterprise. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"2b343393-2100-5963-a692-dd7f6de9f241","locator":{"kind":"page","page":72,"label":"Slide 72","section_title":"2.4 Re-ranking","extraction_method":"pdf-text-layer"},"checksum":"9d922c6c66b7226d09b9632e312d3ccd866a08e772bda99051af0b98fa457da3"} -->

## Slide 72 - 2.4 Re-ranking

Broad search is not enough. Discover how cross-encoders score relevance with sniper precision, and how MMR eliminates redundant context to optimize your LLM's token budget.

---

<!-- chiron-source-span: {"source_span_id":"aa8969b9-758c-571b-85ff-d84cb26e2cfd","locator":{"kind":"page","page":73,"label":"Slide 73","section_title":"Top-k Không Phải Càng Nhiều Càng Tốt","extraction_method":"pdf-text-layer"},"checksum":"27fe97b872db82934720e4f290643b6d524e3cce376fdb584bfaf5a737d3033c"} -->

## Slide 73 - Top-k Không Phải Càng Nhiều Càng Tốt

k quá thấp Ví dụ: top-1 hoặc top-2 Triệu chứng: thiếu chứng cứ, recall kém Sweet spot Ví dụ: top-3 đến top-5 Triệu chứng: đủ chứng cứ, ít nhiễu k quá cao Ví dụ: top-10 trở lên Triệu chứng: context nhiễu, token lãng phí Lưu ý: Mục tiêu của retrieval không phải là lấy nhiều, mà là lấy đúng và đủ cho generation. Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 15 / 32

---

<!-- chiron-source-span: {"source_span_id":"df099fed-7427-5f92-ac2f-fbfb17aef822","locator":{"kind":"page","page":74,"label":"Slide 74","section_title":"Vấn Đề Của Top-K (Nhìn Xa Mù Gần)","extraction_method":"pdf-text-layer"},"checksum":"2d374ec4bd16b80caab1c9ed3d9c61c876f7506ba384d464fad5dc8c91889235"} -->

## Slide 74 - Vấn Đề Của Top-K (Nhìn Xa Mù Gần)

Đặc tính Retriever

- Retriever (Vector/Hybrid) được thiết
kế để quét qua hàng triệu tài liệu cực nhanh. Nó đánh giá sự liên quan một cách "thô và rộng".

- Hệ quả: Chứa rất nhiều ngữ cảnh
tương đồng nhưng không trực tiếp trả lời câu hỏi. Tài liệu đúng nhất có thể đang nằm ở Top 10, chứ không phải Top 1. Trực quan: Query & Results Query: "Thủ tục xin visa" Top 1: Giá làm visa Top 2: Lịch sử visa ... Top 8: Các bước làm thủ tục Dữ liệu đúng bị "chìm" sâu Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"5e376773-1e5c-50f8-af1a-271b72f52a8f","locator":{"kind":"page","page":75,"label":"Slide 75","section_title":"Kiến Trúc 2 Giai Đoạn (Retrieve-and-Rerank)","extraction_method":"pdf-text-layer"},"checksum":"09cfcebda122d1b2268d99a27cd18d319f174be8f5f7a8d2515adb076e7f7fb6"} -->

## Slide 75 - Kiến Trúc 2 Giai Đoạn (Retrieve-and-Rerank)

Quy trình xử lý

- Giai đoạn 1: Dùng Hybrid Search kéo nhanh
về Top 50-100 tài liệu. Nhanh nhưng nhiễu.

- Giai đoạn 2: Đưa Top 50 này qua một mô
hình AI khác (Re-ranker) để đọc kỹ và chấm điểm lại sự liên quan. Lấy Top 3-5 đưa cho LLM. Rerank Funnel Visual Search Broad Top-100 Rerank Top-6 Select Top-3 Input to LLM Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"eeac1b18-392c-53bc-9390-8382c1ba4d35","locator":{"kind":"page","page":76,"label":"Slide 76","section_title":"Bi-Encoder vs. Cross-Encoder","extraction_method":"pdf-text-layer"},"checksum":"7e1e94a578849418de7f973397aaf6a2875890ab9f3a69728733323f86b8e31d"} -->

## Slide 76 - Bi-Encoder vs. Cross-Encoder

Bi-Encoder (Vector DB)

- Query và Document đi qua hai luồng
nhúng riêng biệt.

- Chỉ tính khoảng cách lúc cuối. Rất nhanh.
Cross-Encoder (Reranker)

- Gắn Query và Document thành một đoạn
text duy nhất (Query + [SEP] + Document).

- Cho qua Transformer cùng lúc. Nhờ cơ
chế Attention, model hiểu chính xác sự tương tác giữa từng từ. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"31ca5e0c-bada-593c-b93b-e12a881d2523","locator":{"kind":"page","page":77,"label":"Slide 77","section_title":"Hiệu Năng vs. Độ Chính Xác","extraction_method":"pdf-text-layer"},"checksum":"5de62187dd801e63dfaad04b1ce286a176d24870dea3dd5027edb0d255587a3a"} -->

## Slide 77 - Hiệu Năng vs. Độ Chính Xác

Đặc điểm mô hình

- Cross-Encoder chấm điểm cực kỳ chính
xác (như một người đọc kiểm tra chéo).

- Nhưng nó quá chậm và tốn compute.
Không bao giờ được dùng Reranker để quét toàn bộ database.

- Chỉ dùng cho list nhỏ đã lọt qua vòng 1.
Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"373240b4-f7d6-5181-ae29-20111f500b05","locator":{"kind":"page","page":78,"label":"Slide 78","section_title":"Vấn Đề Redundancy (Trùng Lặp Thông Tin)","extraction_method":"pdf-text-layer"},"checksum":"1c52d366d46112f906e5d4b4a24e64955b633582a4c59ce17a78d7482b3d4508"} -->

## Slide 78 - Vấn Đề Redundancy (Trùng Lặp Thông Tin)

Hạn chế của Re-ranker

- Re-ranker có thể đưa Top 3 tài liệu tốt
nhất lên đầu. Nhưng nếu cả 3 tài liệu này đều sao chép nội dung của nhau thì sao?

- LLM sẽ tốn token vô ích mà không có
thêm góc nhìn hay dữ kiện mới. Minh họa Redundancy Chunk 1 "Hoàn tiền mất 7 ngày." Chunk 2 "Tiền sẽ về sau 7 ngày." Chunk 3 "Thời gian xử lý hoàn tiền là 7 ngày." Redundant Context Window! Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"76d94cb2-d8fd-5dc3-8451-3d506b3cc82f","locator":{"kind":"page","page":79,"label":"Slide 79","section_title":"Tối Ưu Hóa Sự Đa Dạng (MMR)","extraction_method":"pdf-text-layer"},"checksum":"c4b39ca48b5d3967f2dce84ed1670e10a9e5bb93783d7a835695ffb0e461cb54"} -->

## Slide 79 - Tối Ưu Hóa Sự Đa Dạng (MMR)

Cơ chế hoạt động của MMR

- MMR (Maximum Marginal Relevance): Thuật toán chọn lọc để tối đa hóa sự liên quan (Relevance)
nhưng phạt nặng sự trùng lặp (Redundancy).

- Bước 1: Chọn chunk liên quan nhất với Query.

- Bước 2: Chọn chunk tiếp theo vừa liên quan Query, vừa có khoảng cách vector xa nhất so với chunk số
1. Công thức MMR Maximize: [Similarity(Doc, Query)] - Penalty × [Similarity(Doc, Already_Selected_Docs)] Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"2d59753a-2ce8-5ba8-8c05-b6f437a32d85","locator":{"kind":"page","page":80,"label":"Slide 80","section_title":"Khi Nào Dùng MMR vs. Cross-Encoder","extraction_method":"pdf-text-layer"},"checksum":"fbdab0614080b250471200921bb19670e7ead39e8ce3c09d54b3553d4d77f2da"} -->

## Slide 80 - Khi Nào Dùng MMR vs. Cross-Encoder

Precision Focus Cross-Encoder Dùng cho các câu hỏi cần sự chính xác tuyệt đối (Fact-checking, Legal).

### Ví dụ
"Các yêu cầu an toàn khi lắp đặt máy phát điện là gì, và những lời khuyên về bảo trì là gì?" Diversity Focus MMR Dùng cho các truy vấn mở, cần tổng hợp nhiều góc nhìn.

### Ví dụ
"Hãy tóm tắt các điểm rủi ro của dự án A từ tất cả các báo cáo" Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"fca6cfb3-1202-5091-9a45-971709d7064c","locator":{"kind":"page","page":81,"label":"Slide 81","section_title":"Code Tích Hợp Reranker","extraction_method":"pdf-text-layer"},"checksum":"b3bec490c7611b661fd8f75837590c5327d9af728b673deb487e63530a5a7e82"} -->

## Slide 81 - Code Tích Hợp Reranker

Sử dụng Re-ranker as a Service (như Cohere) là cách tiết kiệm tài nguyên hệ thống nhất. # Python

```text
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank
# G ọi API Reranker (VD model multilingual cho ti ếng Vi ệt)
compressor = CohereRerank(top_n=3, model="rerank-multilingual-v3.0")
```
# B ọc retriever cũ b ằng layer rerank rerank_retriever = ContextualCompressionRetriever( base_compressor=compressor, base_retriever=hybrid_retriever ) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"983c9191-5473-546f-87c3-51dd2837151f","locator":{"kind":"page","page":82,"label":"Slide 82","section_title":"Bức Tranh Toàn Cảnh (The Complete Retrieval Pipeline)","extraction_method":"pdf-text-layer"},"checksum":"4e6ff80d7929cc2a9dff374cff7261000a0de6ff26ba9957921729a91c3a13d6"} -->

## Slide 82 - Bức Tranh Toàn Cảnh (The Complete Retrieval Pipeline)

Tổng hợp toàn bộ Module 2: Lộ trình từ Query đầu vào đến kết quả cuối cùng thông qua các kỹ thuật tối ưu hóa retrieval đã học. Query Transformation Hybrid Search k = 50 Reranking Cross-Enc/MMR Context Top 5 Chunks LLM Generation Wrapped as an Agent Tool Gợi ý Ta có thể gói gọn pipeline này thành công cụ cho Agentic System (LangGraph) gọi tự động. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"da257d15-0fee-5e1a-a92a-5e673c80ab64","locator":{"kind":"page","page":83,"label":"Slide 83","section_title":"Generation, Grounding & UX","extraction_method":"pdf-text-layer"},"checksum":"c14d48e7f8600219114a46a293ca2373f71a738bd7b1c89630a212a7f47853f7"} -->

## Slide 83 - Generation, Grounding & UX

3 The final mile of RAG: Mastering context injection, enforcing strict LLM grounding to eliminate hallucinations, and crafting an output UX that users actually trust.

---

<!-- chiron-source-span: {"source_span_id":"3c8076ff-5789-5f8f-a30b-a66532cc623d","locator":{"kind":"page","page":84,"label":"Slide 84","section_title":"3.1 Context Injection Patterns","extraction_method":"pdf-text-layer"},"checksum":"ec2f58502e90912f9f12ecb6c158c887f2bd5737faebff5fca3a644f3e7efc8b"} -->

## Slide 84 - 3.1 Context Injection Patterns

The art of context injection: How to structure and format retrieved data within the LLM's prompt window to maximize retention and conquer the 'Lost in the Middle' effect.

---

<!-- chiron-source-span: {"source_span_id":"c354f725-297d-504d-805b-805a972150d6","locator":{"kind":"page","page":85,"label":"Slide 85","section_title":"Nếu Indexing là \"xây kho\", Retrieval là","extraction_method":"pdf-text-layer"},"checksum":"8aadaa5ede33e61e1a0ebc98d88355f99f34254e29d9d276f1c4aee93c31df57"} -->

## Slide 85 - Nếu Indexing là "xây kho", Retrieval là

"người thủ thư tìm sách", thì Generation là "biên tập viên" tổng hợp thông tin. Dù bạn tìm được tài liệu xuất sắc đến đâu, nếu không biết cách "bơm" (inject) nó vào Prompt, LLM vẫn sẽ bị ảo giác hoặc trả lời sai định dạng. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Generation - Chặng Cuối Của Pipeline

---

<!-- chiron-source-span: {"source_span_id":"59eebbeb-cd01-59a5-b9bb-5a2d7e4cadf0","locator":{"kind":"page","page":86,"label":"Slide 86","section_title":"Là nghệ thuật sắp xếp và định dạng các","extraction_method":"pdf-text-layer"},"checksum":"8b08c3727712a38c415964f140c26f1cd60cba81aa3f294d43465de5dbe112b7"} -->

## Slide 86 - Là nghệ thuật sắp xếp và định dạng các

chunk dữ liệu (đã retrieve) vào trong Context Window của LLM để nó dễ đọc, dễ hiểu nhất. Không chỉ là nối chuỗi (text1 + text2). Cách bạn định dạng quyết định việc LLM có tôn trọng dữ liệu đó hay không. [System Rules] [Retrieved Documents] [User Question] THE PROMPT Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Context Injection Là Gì?

---

<!-- chiron-source-span: {"source_span_id":"2bd6c769-2aa3-5046-9105-facbe995f91d","locator":{"kind":"page","page":87,"label":"Slide 87","section_title":"Cách làm sơ khai nhất: Ghép tất cả các chunk","extraction_method":"pdf-text-layer"},"checksum":"4767a8d6c693a0e111ee0916500f8a8fc1353aa68fb7e0dbd8424f0db27babcd"} -->

## Slide 87 - Cách làm sơ khai nhất: Ghép tất cả các chunk

thành một khối văn bản dài và đặt lên đầu câu hỏi.

- Ưu điểm: Dễ code (chỉ cần hàm.join()).

- Nhược điểm: Model không phân biệt được
ranh giới giữa các tài liệu, làm mất giá trị Metadata. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Pattern 1 - Pre-pending (Chèn Thô)

---

<!-- chiron-source-span: {"source_span_id":"ac85bbf4-d4b5-5223-ba20-0b6b6407c888","locator":{"kind":"page","page":88,"label":"Slide 88","section_title":"Cách làm chuẩn Production: Sử dụng thẻ XML","extraction_method":"pdf-text-layer"},"checksum":"78982a4703beb7dd91b2fcdf581ffa3e09caa6066836bf712d4e5f80abec8447"} -->

## Slide 88 - Cách làm chuẩn Production: Sử dụng thẻ XML

hoặc định dạng JSON/Markdown để phân tách rõ ràng từng nguồn dữ liệu. Nhờ cấu trúc này, model dễ dàng nhận diện ID của tài liệu để làm trích dẫn (Citation) sau này. <documents> <doc id="1" source="policy.pdf"> ... content document 1... </doc> <doc id="2"> ... content document 2... </doc> </documents> Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Pattern 2 - Structured Snippets & XML Tags

---

<!-- chiron-source-span: {"source_span_id":"954f512f-a7e5-56ca-810d-cc67117aeafb","locator":{"kind":"page","page":89,"label":"Slide 89","section_title":"● Đừng nhồi tối đa Token chỉ vì model hỗ trợ. Càng nhiều context → Càng chậm → Càng","extraction_method":"pdf-text-layer"},"checksum":"f96e45bafdbb3148479b2a6b2a4860a7aa68ad2e100dac2c7d487295dfe56cb2"} -->

## Slide 89 - ● Đừng nhồi tối đa Token chỉ vì model hỗ trợ. Càng nhiều context → Càng chậm → Càng

đắt → Càng dễ nhiễu.

- Phải chia ngân sách rõ ràng: 20% cho System Prompt/Rules, 60% cho Retrieved Context, 20% dự
phòng (Headroom) cho User Query và Output. 20% System Prompt & Rules 60% Retrieved Context 20% Headroom (Query & Output) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Quản Lý Token Budget (Ngân Sách Ngữ Cảnh)

---

<!-- chiron-source-span: {"source_span_id":"371dc3b8-6023-5e88-b9d5-fdd751bed82b","locator":{"kind":"page","page":90,"label":"Slide 90","section_title":"● Các nghiên cứu chỉ ra: LLM giống như con","extraction_method":"pdf-text-layer"},"checksum":"d5bb8bcc4dab7223a1aeec66f1ec69cd18761ec70e9f57a7a6a8f2d5a0078207"} -->

## Slide 90 - ● Các nghiên cứu chỉ ra: LLM giống như con

người, nó nhớ rất tốt thông tin nằm ở ĐẦU và CUỐI prompt, nhưng thường "bỏ quên" thông tin nằm ở GIỮA nếu prompt quá dài.

- Nếu chunk chứa câu trả lời quan trọng nhất
vô tình bị xếp ở giữa danh sách, RAG có thể thất bại. Recall Performance Position in Prompt ĐẦU CUỐI GIỮA (Lost) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Hiện Tượng "Lost in the Middle"

---

<!-- chiron-source-span: {"source_span_id":"16801477-89be-5e85-854a-91a58f374a90","locator":{"kind":"page","page":91,"label":"Slide 91","section_title":"● Đừng ném nguyên Top K từ Reranker vào","extraction_method":"pdf-text-layer"},"checksum":"d1d5179ff648d975c9ec51460add939bde8db3e6bae078de28409409d906b208"} -->

## Slide 91 - ● Đừng ném nguyên Top K từ Reranker vào

prompt theo thứ tự 1, 2, 3, 4, 5.

- Thủ thuật Document Reordering: Sắp xếp
lại theo mẫu luân phiên. Đặt tài liệu tốt nhất ở đầu, tốt thứ 2 ở cuối, các tài liệu điểm thấp giấu vào giữa.

- Thứ tự đưa vào prompt: [1, 3, 5, 4, 2]
Document Reordering Strategy Block 1 (Top 1) Block 3 Block 5 Block 4 Block 2 (Top 2) Re-rank ĐẦU CUỐI GIỮA Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Giải Pháp Cho "Lost in the Middle"

---

<!-- chiron-source-span: {"source_span_id":"1748e621-5eb7-5267-9a2e-357302aa4853","locator":{"kind":"page","page":92,"label":"Slide 92","section_title":"3.2 Prompt Engineering for Strict Grounding","extraction_method":"pdf-text-layer"},"checksum":"9a16400c729a616579341a5ce5811125dc07806028e40355eb1a8c0c30e4132e"} -->

## Slide 92 - 3.2 Prompt Engineering for Strict Grounding

Taming the LLM: Discover how to construct robust system prompts that enforce strict citations, prevent hallucinations, and gracefully handle knowledge gaps.

---

<!-- chiron-source-span: {"source_span_id":"67a83168-decb-5763-b3fa-7f2ef5deb6f6","locator":{"kind":"page","page":93,"label":"Slide 93","section_title":"Grounding Là Gì?","extraction_method":"pdf-text-layer"},"checksum":"fd49c8c19b22096971ce58ba8fbdd31d08572e34309f3d3dbee5592711a982c9"} -->

## Slide 93 - Grounding Là Gì?

- Grounding (Tiếp đất / Neo dữ kiện) là việc
bắt buộc LLM chỉ được phép sử dụng thông tin từ context được cấp, nghiêm cấm dùng "kiến thức học được từ Internet" để chém gió.

- Mục tiêu: Nếu đổi context sai, model cũng
phải trả lời sai theo context đó. Trọng tài duy nhất là dữ liệu nội bộ. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"9fee016c-ca5b-5016-ab83-23598323690d","locator":{"kind":"page","page":94,"label":"Slide 94","section_title":"Anatomy Của Một Prompt RAG Chuẩn","extraction_method":"pdf-text-layer"},"checksum":"bbe5ea2327d3e583f81fbc9372483d6501baef2fa49ebb4149e42a9342da881f"} -->

## Slide 94 - Anatomy Của Một Prompt RAG Chuẩn

### Một System Prompt tốt cho RAG cần 4 phần cốt lõi

1. Role Định hình nhân vật (VD: "Bạn là trợ lý pháp chế nội bộ...").

2. Task Trả lời câu hỏi người dùng.

3. Context Cung cấp tài liệu từ hệ thống Retrieval.

4. Strict Constraints Quy tắc "bàn tay sắt" (Cấm bịa, bắt buộc trích dẫn). Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"7f51e80b-ba83-56e4-9433-3ffc83b35abb","locator":{"kind":"page","page":95,"label":"Slide 95","section_title":"Ép Buộc Trích Dẫn (Forcing Citations)","extraction_method":"pdf-text-layer"},"checksum":"7cefd6fbdd93e6c902958ba7e226486b2125a29db7d939ab5dfd1113ed6a1994"} -->

## Slide 95 - Ép Buộc Trích Dẫn (Forcing Citations)

- RAG mất đi 50% giá trị nếu model không
chỉ ra được nó lấy câu trả lời từ dòng nào, tài liệu nào.

- Trong Constraint, cần chỉ thị rõ: "Khi đưa
ra một tuyên bố, phải trích dẫn ID của document trong ngoặc vuông, ví dụ [doc_1]." PROMPT SNIPPET ALWAYS cite your sources using the <doc_id> provided. RESULTING OUTPUT "Nhân viên được nghỉ 12 ngày phép [doc_3]." Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"3067ff93-4b38-5383-8ef6-f4e6fa3fab58","locator":{"kind":"page","page":96,"label":"Slide 96","section_title":"Nghệ Thuật Nói \"Tôi Không Biết\"","extraction_method":"pdf-text-layer"},"checksum":"7f7aadf6af7251fe57a93af8893d24a68fd288f98fbcfee6fc982d4fb6d33858"} -->

## Slide 96 - Nghệ Thuật Nói "Tôi Không Biết"

- Đây là tính năng quan trọng nhất của RAG:
Biết giới hạn của mình (Graceful Degradation).

- Nếu Top K chunks mang về không chứa câu
trả lời, model phải từ chối thay vì cố gắng đoán mò. PROMPT LINE If the context does not contain the answer, reply EXACTLY with: "Dữ liệu hiện tại không đủ để tôi trả lời câu hỏi này." Do not attempt to guess. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"fa2c312a-19f2-521e-ab68-dff78d8c7fff","locator":{"kind":"page","page":97,"label":"Slide 97","section_title":"Graceful Degradation","extraction_method":"pdf-text-layer"},"checksum":"54883e199c3c857a4e51e9fd860360ada016100a075c56fcf2f8d3b159632be2"} -->

## Slide 97 - Graceful Degradation

- Thay vì chỉ nói "Không biết" cụt lủn
gây ức chế cho người dùng.

- Hãy prompt để model gợi ý: "Tôi không
tìm thấy chính sách này trong kho tài liệu HR năm 2026. Bạn có muốn tôi tìm kiếm rộng hơn hoặc liên hệ bộ phận nhân sự không?" BAD CHATBOT "Tôi không biết." GOOD CHATBOT "Tôi chưa tìm thấy [X], nhưng bạn có thể thử hỏi lại với từ khóa [Y] hoặc tạo ticket cho IT." Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"cbe075ca-a349-5387-adbc-688966b4a2ee","locator":{"kind":"page","page":98,"label":"Slide 98","section_title":"Chain of Thought (CoT) Trong Generation","extraction_method":"pdf-text-layer"},"checksum":"4e1260dbe1a5628c86e86451865c7d7a40ae6267605daa05232406d7530ea8b7"} -->

## Slide 98 - Chain of Thought (CoT) Trong Generation

- Yêu cầu model "suy nghĩ ra nháp" trước khi in
ra câu trả lời cuối.

- Chỉ thị: "Đầu tiên, hãy lọc ra các câu liên
quan trong context. Phân tích chúng trong thẻ <thought_process>. Sau đó mới tổng hợp thành câu trả lời."

- Tăng độ chính xác lên đáng kể đối với các câu
hỏi so sánh hoặc suy luận logic từ tài liệu. INTERNAL REASONING <thought_process>

1. Comparing doc A and B...

2. Found conflict in dates...

3. Reconciling...</thought_process> FINAL ANSWER Dựa trên phân tích tài liệu, câu trả lời chính xác nhất là phương án B vì các lý do sau đây:... Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"39b1b8e7-c2ce-59c7-9dbc-c04e37604fa4","locator":{"kind":"page","page":99,"label":"Slide 99","section_title":"Code Snippet: LangChain Prompt Template","extraction_method":"pdf-text-layer"},"checksum":"b39238209af8632ac994014a63127850ab30aa65576b3aa23b3817a34dc9d693"} -->

## Slide 99 - Code Snippet: LangChain Prompt Template

- Cách lắp ghép linh động các thành phần Context và User Question vào trong Prompt.
PYTHON SNIPPET rag_prompt_template = """ You are a strictly grounded assistant. Answer the user's question using ONLY the context below. If you cannot answer, say "I don't know". Always cite the [source_id]. <context> {formatted_context} </context> Question: {question}

### Answer
""" Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"96126201-844c-5cc3-8323-ae936011c73a","locator":{"kind":"page","page":100,"label":"Slide 100","section_title":"3.3 Output Formatting & UX","extraction_method":"pdf-text-layer"},"checksum":"75b2946ac9ac26dd4378e4e51ac7d831ad24e3d0c9d14a14b7512572e1c0e76c"} -->

## Slide 100 - 3.3 Output Formatting & UX

Learn how to design an enterprise-grade Output UX, featuring inline citations, transparent source blocks, and fluid streaming states that build user trust.

---

<!-- chiron-source-span: {"source_span_id":"0135b3f3-b7d2-5afc-916c-caeda77d7871","locator":{"kind":"page","page":101,"label":"Slide 101","section_title":"UX Trong RAG Quyết Định Độ Tin Cậy","extraction_method":"pdf-text-layer"},"checksum":"c46fd080df530b3832fc6cab6ea7832e3ac9792f5d766062637e1abb4dd6f9a4"} -->

## Slide 101 - UX Trong RAG Quyết Định Độ Tin Cậy

Người dùng doanh nghiệp không quan tâm bạn dùng thuật toán MMR hay HNSW. Họ chỉ nhìn vào giao diện cuối cùng. Một khối text đặc chữ sẽ tạo cảm giác lười đọc và nghi ngờ. Cần thiết kế đầu ra có tính "scannable" (dễ quét mắt). CÁCH CŨ: KHÓ THEO DÕI Dựa trên báo cáo quý 3, doanh thu đạt 5.2 tỷ USD, tăng 12% so với cùng kỳ năm ngoái nhờ vào việc tối ưu hóa chi phí vận hành tại khu vực Đông Nam Á trong khi đó tỷ lệ giữ chân khách hàng vẫn duy trì ở mức 85% mặc dù có sự cạnh tranh gay gắt từ các đối thủ mới nổi và kế hoạch cho quý 4 sẽ tập trung vào việc mở rộng mảng dịch vụ đám mây với mục tiêu tăng trưởng thêm 15% thông qua các gói ưu đãi dành cho khách hàng trung thành đã sử dụng dịch vụ trên 2 năm. CÁCH MỚI: SCANNABLE UX

### Kết quả kinh doanh Quý 3

- Doanh thu: 5.2 tỷ USD (+12% YoY)

- Động lực chính: Tối ưu vận hành tại Đông
Nam Á.

- Khách hàng: Tỷ lệ giữ chân ổn định ở mức
85%.

### Kế hoạch Quý 4

- Mở rộng dịch vụ đám mây (Mục tiêu +15%).

- Ưu đãi cho khách hàng trung thành (>2
năm). Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"d493cddf-eff5-5782-a9a6-5d6d3f91a647","locator":{"kind":"page","page":102,"label":"Slide 102","section_title":"Inline Citations (Trích Dẫn Trong Dòng)","extraction_method":"pdf-text-layer"},"checksum":"3887f94a1e806568b73e4dc3817a0549c1e9b901a5024c4ca636dafaedeaa464"} -->

## Slide 102 - Inline Citations (Trích Dẫn Trong Dòng)

- Giống Wikipedia: Đặt các
reference ID ngay sát bên cạnh thông tin kiện.

- Góc độ UI/UX: Các ID này (ví dụ
[1], [2]) nên là hyperlink. Khi hover/click vào, nó sẽ popup ra đoạn text gốc để user đối chiếu nhanh. AI ASSISTANT MOCKUP Hoàn tiền diễn ra trong 7 ngày [1] Source: Refund_Policy.pdf Section 3: All verified claims are processed within 7 business days. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"9e0bee61-5152-5be5-b522-1dee5e33f901","locator":{"kind":"page","page":103,"label":"Slide 103","section_title":"Source Blocks / Footnotes (Khối Nguồn Tham Khảo)","extraction_method":"pdf-text-layer"},"checksum":"87aec7691fc7e1da455be70e599766a09daaa4f971f6cfd0af5e42b1e6543813"} -->

## Slide 103 - Source Blocks / Footnotes (Khối Nguồn Tham Khảo)

- Ở cuối mỗi câu trả lời, luôn tổng
hợp lại một danh sách các tài liệu đã được sử dụng.

- Cung cấp URL hoặc nút "Mở tài liệu
gốc" để người dùng đi sâu vào nghiên cứu nếu cần. AI ASSISTANT MOCKUP Theo tài liệu v4.0, thiết bị của bạn được bảo hành 12 tháng kể từ ngày kích hoạt.

### Nguồn tham khảo

1. Chính sách bảo hành v4.0 (Tỷ lệ khớp: 92%)

2. Ticket lỗi #8892 - Jira ➜ Mở tài liệu gốc Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"8703780e-3e38-5f93-b719-ca06f0ee1e3d","locator":{"kind":"page","page":104,"label":"Slide 104","section_title":"Hiển Thị Mức Độ Tự Tin (Confidence Score/Tags)","extraction_method":"pdf-text-layer"},"checksum":"54ba1f93ab1702cafee1f93c7c397f31e6e920f33fb27df831e8002d827f8b19"} -->

## Slide 104 - Hiển Thị Mức Độ Tự Tin (Confidence Score/Tags)

- Đưa thêm tín hiệu từ hệ thống
Retrieval ra thẳng UI.

- Nếu điểm số Re-ranker thấp: Gán
nhãn cảnh báo độ liên quan.

- Giúp quản lý kỳ vọng của người
dùng. AI ASSISTANT MOCKUP Dựa trên các tài liệu tìm thấy, quy trình hoàn tiền mất khoảng 7 ngày làm việc. ⚠ CẢNH BÁO ĐỘ TIN CẬY THẤP Dữ liệu tìm thấy có độ liên quan thấp, câu trả lời có thể không chính xác. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"0cddc18c-45f3-5313-b228-47be05424d78","locator":{"kind":"page","page":105,"label":"Slide 105","section_title":"Trải Nghiệm Streaming & \"Working\" State","extraction_method":"pdf-text-layer"},"checksum":"0772dbf182af7e44870498bc5941259c1a09c362aca03cb0842f370e2503926b"} -->

## Slide 105 - Trải Nghiệm Streaming & "Working" State

- Hệ thống RAG chạy qua nhiều
bước thường mất 3-5 giây, dễ làm user tưởng app bị treo.

- Giải pháp UX: Hiển thị các bước
đang chạy và dùng chế độ Streaming khi có text. AI ASSISTANT MOCKUP Đang tìm kiếm trong kho HR... Đang đọc 5 tài liệu... Dựa trên chính sách nghỉ phép năm 2026... Nhân viên có hơn 3 năm thâm niên được hưởng 15 ngày phép | Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"7fb1a40f-cbfd-509f-8bd7-7ff66ce46814","locator":{"kind":"page","page":106,"label":"Slide 106","section_title":"3.4 Generation Failures","extraction_method":"pdf-text-layer"},"checksum":"d08c4a6429ed8db5ad9aabd63f5728ba424c21cf51738d99bde61b25f16d463d"} -->

## Slide 106 - 3.4 Generation Failures

Learn to diagnose and troubleshoot common generation failures,

```text
from conflicting documents to dangerous LLM
```
over-extrapolation.

---

<!-- chiron-source-span: {"source_span_id":"bf01ab74-d7ab-5917-a980-23d09016f6e6","locator":{"kind":"page","page":107,"label":"Slide 107","section_title":"Khi Generation Đổ Vỡ Dù Retrieval Làm Tốt","extraction_method":"pdf-text-layer"},"checksum":"a08a3aba9a89873f026ef32129a9239382fd062a3a5b7fd2613904aed7804f7b"} -->

## Slide 107 - Khi Generation Đổ Vỡ Dù Retrieval Làm Tốt

- Không phải lúc nào lỗi cũng do DB. Có những lúc hệ thống tìm về
đúng tài liệu xuất sắc, nhưng LLM vẫn "vấp ngã" ở bước cuối.

- Đây là lúc phải Debug Prompt và Temperature của model.
"Good Context + Bad Prompt = Bad Answer" Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"b40362a8-70ec-5d72-b4ca-7740082d4a7f","locator":{"kind":"page","page":108,"label":"Slide 108","section_title":"Lỗi 1 - Xung Đột Ngữ Cảnh (Conflicting Context)","extraction_method":"pdf-text-layer"},"checksum":"088e7b1fe6d4dde09596b1a7feb805ff0dcf2cce6f7d8a2bab58405672d333f2"} -->

## Slide 108 - Lỗi 1 - Xung Đột Ngữ Cảnh (Conflicting Context)

Tình huống: Retriever mang về 2 tài liệu. Tài liệu A (năm 2024) bảo nghỉ 12 ngày. Tài liệu B (năm 2026) bảo nghỉ 14 ngày. Hệ quả: LLM bị bối rối, có thể cộng gộp, báo lỗi, hoặc chọn bừa. Khắc phục: Dặn dò trong prompt: "Nếu có mâu thuẫn, ưu tiên tài liệu có ngày cập nhật mới nhất, hoặc liệt kê cả 2 và chỉ ra sự mâu thuẫn." Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"827805a7-66c8-5de5-80a1-f0f72fdf98c1","locator":{"kind":"page","page":109,"label":"Slide 109","section_title":"Lỗi 2 - Over-extrapolation (Suy Diễn Quá Đà)","extraction_method":"pdf-text-layer"},"checksum":"df7989e11eb7bf4025de3b758b3c81b169b6ad1aefa84e098e68b41da4f0d12d"} -->

## Slide 109 - Lỗi 2 - Over-extrapolation (Suy Diễn Quá Đà)

Giảng viên (VinUni) AICB · Python Ingestion Tuần 2 Khắc phục: Strict Grounding: "Không tự ý suy luận các điều kiện không được đề cập rõ ràng." Tình huống: Tài liệu ghi "Miễn phí ship cho đơn trên 500k ở Hà Nội". Người dùng hỏi "Thế ở HCM thì sao?". Hệ quả: Tài liệu không nói về HCM, nhưng LLM tự suy diễn logic "Hà Nội được thì HCM chắc cũng được" → Ảo giác (Hallucination).

---

<!-- chiron-source-span: {"source_span_id":"a1a03d45-c8b4-5576-8bc2-68a270e2eb61","locator":{"kind":"page","page":110,"label":"Slide 110","section_title":"Lỗi 3 - Bỏ Qua Rào Cản (Ignored Constraints)","extraction_method":"pdf-text-layer"},"checksum":"6dd3e0010f57bdbddb8ccab357e1f92e908742e04d239c9c24d28cb10e8a7473"} -->

## Slide 110 - Lỗi 3 - Bỏ Qua Rào Cản (Ignored Constraints)

Tình huống: Đã dặn model phải trích dẫn ID, nhưng khi sinh ra text, model quên bẵng mất tiêu. Thường xảy ra với model nhỏ (ví dụ 8B tham số) hoặc khi context quá dài.

### Khắc phục

- Đặt các rule quan trọng nhất ở CUỐI prompt (gần chữ Answer: nhất).

- Giảm tham số temperature = 0 (làm cho output deterministic và bớt sáng tạo).
Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"5523fe35-8eee-5ad8-a406-fc6f7f0cecaf","locator":{"kind":"page","page":111,"label":"Slide 111","section_title":"Troubleshooting Generation (Quy Trình Debug)","extraction_method":"pdf-text-layer"},"checksum":"2d5d5e294582995a826fbc2dfcfddd442742f52f727fa61d8a6ec4e416c87d19"} -->

## Slide 111 - Troubleshooting Generation (Quy Trình Debug)

- Nếu app trả lời sai, hãy in log (print) biến formatted_context ra console trước tiên.

- Nếu context có chứa đáp án → Lỗi do Generation (Sửa prompt, thêm CoT, đổi model).

- Nếu context KHÔNG chứa đáp án → Lỗi do Retrieval (Quay lại Phần 2).
Is the answer in the retrieved context? No YesFix Retrieval/ Chunking Fix Prompt Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"bec23d74-16a6-5376-89a8-a1d246c34e45","locator":{"kind":"page","page":112,"label":"Slide 112","section_title":"Evaluation, Production & Next Steps","extraction_method":"pdf-text-layer"},"checksum":"3bdaa1984d1504ce486493d43dd1f373dca3a61abc1ec3298cccdd2c965f7358"} -->

## Slide 112 - Evaluation, Production & Next Steps

4 Learn how to quantitatively evaluate your RAG pipeline using the Evaluation Triad, and preview the transition into complex, multi-agent workflows.

---

<!-- chiron-source-span: {"source_span_id":"5797d6e1-6bd5-5849-8c47-f1e427490bfb","locator":{"kind":"page","page":113,"label":"Slide 113","section_title":"4.1 The RAG Evaluation Triad","extraction_method":"pdf-text-layer"},"checksum":"ed6439299dfef7b586380151476a8ceed60608bb76653c7f49dffb1bd6c0f07c"} -->

## Slide 113 - 4.1 The RAG Evaluation Triad

Discover the RAG Evaluation Triad—Context Recall, Faithfulness, and Answer Relevance—to quantitatively measure and debug your system's true performance.

---

<!-- chiron-source-span: {"source_span_id":"e0213f56-3bc0-5b20-9edc-e3cae2035199","locator":{"kind":"page","page":114,"label":"Slide 114","section_title":"\"Vibe check\": Nhập thử 3-5 câu hỏi,","extraction_method":"pdf-text-layer"},"checksum":"829445e022a971cffe4273a81f85fc713144a0e91d5277aebae11cc673c70581"} -->

## Slide 114 - "Vibe check": Nhập thử 3-5 câu hỏi,

thấy mượt mà rồi kết luận Ready. Đây là cái bẫy chết người! Thay đổi nhỏ (ví dụ chunk 1000 ➔ 500) có thể tốt cho 10 câu này, nhưng lại làm hỏng 100 câu khác. Phải có Framework định lượng (Automated Metrics) Hình minh họa: Rủi ro khi chỉ kiểm thử thủ công Vibe Check Là Không Đủ (Why Evaluate?) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"86ad5c9a-9659-5309-8a55-1509b391004b","locator":{"kind":"page","page":115,"label":"Slide 115","section_title":"Khung Đánh Giá RAGAS (RAG Assessment)","extraction_method":"pdf-text-layer"},"checksum":"c32af35d6ead428c29819e63d290a91758e890fa940ce50a5329272fb5c48dc9"} -->

## Slide 115 - Khung Đánh Giá RAGAS (RAG Assessment)

- Không thể chấm điểm RAG bằng 1 con số
duy nhất. Phải tách bạch lỗi do Retriever (tìm sai) hay lỗi do Generator (nói bậy).

- Khung RAGAS chia thành 3 trục cốt lõi
(The Triad): Context Recall, Faithfulness, và Answer Relevance. Answer Relevance Context Recall Faithfulness RAGAS Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"9bf9f5c4-a783-59e9-84c8-74ad866e7e8d","locator":{"kind":"page","page":116,"label":"Slide 116","section_title":"Context Recall (Độ Phủ Ngữ Cảnh)","extraction_method":"pdf-text-layer"},"checksum":"3077efdeadc43170d3ad9b786bc847b7f1741a4afea45982919e14cd17c325a0"} -->

## Slide 116 - Context Recall (Độ Phủ Ngữ Cảnh)

Định nghĩa Retriever có mang về đủ thông tin cần thiết để trả lời trọn vẹn câu hỏi không? Bài toán Nếu câu hỏi cần 3 chứng cứ (A, B, C), nhưng hệ thống chỉ tìm được A và B → Recall thấp. Cách khắc phục

- Tối ưu hóa Vector DB

- Dùng Hybrid Search

- Tăng Top-K
Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"0dce6c35-14e2-5e87-90f7-0d2da7b73c57","locator":{"kind":"page","page":117,"label":"Slide 117","section_title":"Faithfulness (Độ Trung Thực)","extraction_method":"pdf-text-layer"},"checksum":"96025f6f1e4cc6ba22fffaa1b9cbe45661f556620cbb5b5c8861bd79c485b354"} -->

## Slide 117 - Faithfulness (Độ Trung Thực)

Định nghĩa Câu trả lời có bám sát 100% vào tài liệu không, hay đang tự bịa thêm (Hallucinate)? Nguyên lý Nếu Context là "A", mà LLM trả lời "A + B", độ trung thực sẽ bị trừ điểm nặng nề. Cách khắc phục

- Tinh chỉnh System Prompt

- Ép buộc trích dẫn (Citations)

- Giảm Temperature về 0
Ví dụ

### Context
"Sản phẩm A màu đỏ."

### LLM Answer
"Sản phẩm A màu đỏ và được bảo hành 1 năm." ⚠ Lỗi Hallucination (Bịa thông tin) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"d91a7e0d-35dd-5a7a-999d-a1dcb6c607b2","locator":{"kind":"page","page":118,"label":"Slide 118","section_title":"Answer Relevance (Độ Trọng Tâm)","extraction_method":"pdf-text-layer"},"checksum":"907875fd290f6980316feb8638d1752040be9c3262f11ff4f2ec17bf4f37cc87"} -->

## Slide 118 - Answer Relevance (Độ Trọng Tâm)

Định nghĩa Câu trả lời có đi thẳng vào vấn đề người dùng hỏi không, hay đang trả lời vòng vo, dông dài? Vấn đề Đôi khi LLM trung thực với Context, nhưng Context lại không liên quan đến câu hỏi, dẫn đến một câu trả lời "đúng sự thật nhưng vô dụng". Ví dụ

### User Question
"Thời gian bảo hành của sản phẩm A?"

### LLM Answer
"Sản phẩm A này rất tốt và có màu xanh,..." ⚠ Trả lời không đúng trọng tâm (Low Relevance) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"2fb7fe69-d742-5f41-97c3-b1a5023f37a6","locator":{"kind":"page","page":119,"label":"Slide 119","section_title":"Mô Hình LLM-as-a-Judge (Dùng AI Chấm Điểm AI)","extraction_method":"pdf-text-layer"},"checksum":"5d34372a9cb03a569926abcb3c7b5b621d6c27e7bd01917aeaf8f09154b9e377"} -->

## Slide 119 - Mô Hình LLM-as-a-Judge (Dùng AI Chấm Điểm AI)

Vấn đề & Giải pháp

- Làm sao để tính được 3 điểm số trên
tự động cho hàng nghìn câu hỏi? Con người không thể ngồi đọc tay.

- Sử dụng một LLM "Thầy Giáo" (phải
là model rất mạnh như GPT-4o hoặc Claude 3.5 Sonnet) để đọc và chấm điểm LLM "Học Sinh" (hệ thống RAG của bạn). LLM-as-a-Judge Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"15f45250-03cb-5002-8ee4-3555cde57d73","locator":{"kind":"page","page":120,"label":"Slide 120","section_title":"Golden Dataset (Xây Dựng Bộ Câu Hỏi Vàng)","extraction_method":"pdf-text-layer"},"checksum":"12ebe2250be72479613cb4d13e5dcbb5f129bdb332898b19b84a46fcf137146d"} -->

## Slide 120 - Golden Dataset (Xây Dựng Bộ Câu Hỏi Vàng)

Chuẩn bị dữ liệu Để chạy RAGAS, bạn cần chuẩn bị một File Excel/CSV chứa khoảng 50-100 mẫu thử cực tốt. Các cột bắt buộc

- Question: Câu hỏi

- Ground Truth: Câu trả lời đúng mà
con người kỳ vọng

- Contexts: Tài liệu gốc chứa đáp án
Yêu cầu nội dung Phải bao gồm đa dạng các loại câu hỏi để

### đánh giá toàn diện hệ thống

- Câu hỏi đánh đố

- Câu hỏi mơ hồ

- Câu hỏi không có trong tài liệu
Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"e290ffcb-9b57-5b56-8e32-95cb180860cb","locator":{"kind":"page","page":121,"label":"Slide 121","section_title":"Code Tối Thiểu - Chạy Vòng Lặp Eval (Ragas)","extraction_method":"pdf-text-layer"},"checksum":"80a5d9a0b295000cb6fd818abb1b6559482f341b14b02be6dc5bd6c823c02a08"} -->

## Slide 121 - Code Tối Thiểu - Chạy Vòng Lặp Eval (Ragas)

Ví dụ Python cách nạp dữ liệu và xuất bảng điểm báo cáo tự động.

```text
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevance, context_recall
```
# dataset ch ứa câu h ỏi, câu tr ả l ời sinh ra, và context result = evaluate( dataset, metrics=[context_recall,faithfulness,answer_relevance], llm=gpt4_judge) print(result.to_pandas()) Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"31254054-06a1-5f67-b24a-8a86213ee778","locator":{"kind":"page","page":122,"label":"Slide 122","section_title":"4.2 A/B Testing & Scorecards","extraction_method":"pdf-text-layer"},"checksum":"fbfc20dcb618c6fff3e0f7e268bf19b0a77e9032019e07830029810152db44b7"} -->

## Slide 122 - 4.2 A/B Testing & Scorecards

Learn how to isolate variables through rigorous A/B testing and interpret evaluation scorecards to drive data-backed improvements in your RAG pipeline.

---

<!-- chiron-source-span: {"source_span_id":"f037d978-b23b-5c6f-88e8-650b3ff7d25d","locator":{"kind":"page","page":123,"label":"Slide 123","section_title":"Kỷ Luật Tuning (Cô Lập Biến Số)","extraction_method":"pdf-text-layer"},"checksum":"4d7053ef46619203cc19552aad63017125b2c75d7d87a7a9910a5a94a25124c8"} -->

## Slide 123 - Kỷ Luật Tuning (Cô Lập Biến Số)

Nguyên tắc sống còn Chỉ thay đổi MỘT biến số trong mỗi lần thử nghiệm (A/B Test). Nếu bạn vừa đổi kích thước chunk, vừa đổi thuật toán Hybrid, vừa đổi System Prompt → Không biết chính xác yếu tố nào mang lại thành công. Trình bày & So sánh

- Trình bày kết quả trực quan cho các Stakeholder (Sếp/PM) xem.

- So sánh điểm số trung bình của toàn bộ 100 câu test trước và sau khi thay đổi thuật
toán. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"78fc7470-9ed6-57f8-b604-b4600a3ceb17","locator":{"kind":"page","page":124,"label":"Slide 124","section_title":"Case Study: Đưa Hybrid Search Lên Bàn Cân","extraction_method":"pdf-text-layer"},"checksum":"f03f108cad766407b3d437465a49bb4fc9b008723e6fe5543432fa93fca94218"} -->

## Slide 124 - Case Study: Đưa Hybrid Search Lên Bàn Cân

Ví dụ thực tế Chuyển từ Thuần Vector (Dense) sang Hybrid (BM25 + Vector). Kết quả trên bảng điểm

- Context Recall tăng vọt từ 60%
lên 90% (vì bắt được các mã lỗi chính xác).

- Kéo theo Faithfulness tăng.
So Sánh Hiệu Suất Context Recall 60% 90% V1: Dense Only V2: Hybrid 100% 50% 0% Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"ebe12b3f-b16b-5d6d-a7de-565dfb0223b6","locator":{"kind":"page","page":125,"label":"Slide 125","section_title":"Đọc Vị Lỗi Qua Bảng Điểm (Diagnostics)","extraction_method":"pdf-text-layer"},"checksum":"77acf54a82fd9a569f84804e76aebe9d82eb165b36ec266d796f2fe5d76374d7"} -->

## Slide 125 - Đọc Vị Lỗi Qua Bảng Điểm (Diagnostics)

Nhìn vào điểm số để bắt bệnh

- Recall Cao + Faithfulness Thấp:
Tìm đúng tài liệu, nhưng model bị ảo giác hoặc bị lú vì prompt viết quá dở.

- Sửa Generation.

- Recall Thấp + Faithfulness Cao: Hệ
thống đang ngoan ngoãn nói "Tôi không biết" vì không tìm thấy tài liệu.

- Sửa Indexing/Retrieval.
Context Recall (Thấp → Cao) Faithfulness (Thấp → Cao) Fix Search Recall thấp Fix Prompt Faithfulness thấp Optimal Production Ready System Failure Fix Both Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"636586f1-485c-5952-98c5-c256a91ad8a2","locator":{"kind":"page","page":126,"label":"Slide 126","section_title":"ROI Của RAG (Chi Phí vs. Chất Lượng)","extraction_method":"pdf-text-layer"},"checksum":"e4b891c1b983386f6dceef74a4112beb0c1dc0bd570a7ced9eba14f997b52d5c"} -->

## Slide 126 - ROI Của RAG (Chi Phí vs. Chất Lượng)

Phân tích kỹ thuật & kinh tế

- Kỹ thuật Cross-encoder Reranker giúp
tăng Answer Relevance thêm 5%.

- Nhưng nó làm thời gian phản hồi
(Latency) tăng từ 1s lên 4s, và chi phí Server tăng gấp đôi.

- Bài toán của Kỹ sư trưởng: 5% độ
chính xác đó có đáng giá với trải nghiệm chậm chạp của người dùng không? 5% Quality Boost $500/month extra + 3s latency delay Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"66a88c3e-7b26-5e9a-88e6-41db3379c779","locator":{"kind":"page","page":127,"label":"Slide 127","section_title":"Tự Động Hóa CI/CD Cho Dữ Liệu","extraction_method":"pdf-text-layer"},"checksum":"46239d035f45ea994c587bb0b328dab7587c3c4c751d443a1d0da7c790c79623"} -->

## Slide 127 - Tự Động Hóa CI/CD Cho Dữ Liệu

Kiểm soát hành vi AI trong Pipeline

- Code RAG không giống code
Web. Khi đẩy code RAG lên Production, bạn không test hàm/logic, bạn test "Hành vi của AI".

- Hãy tích hợp vòng lặp RAGAS
vào GitHub Actions. Nếu điểm số Faithfulness < 80%, hệ thống tự động block lệnh Deploy. Push Build LLM Judge Evaluation Deploy Block if Fail Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"75bbeacb-420d-5c86-85a0-0e0ed6e9a06c","locator":{"kind":"page","page":128,"label":"Slide 128","section_title":"4.3 Preview: The Agentic Future","extraction_method":"pdf-text-layer"},"checksum":"fdc81c6dc2e35e412f3990773ef1cbce0d1c53760dec6d09775bb51bdea2a962"} -->

## Slide 128 - 4.3 Preview: The Agentic Future

Prepare for the agentic future where the LLM evolves into a reasoning engine, and your complex retrieval pipeline becomes just one tool in a multi-agent workflow.

---

<!-- chiron-source-span: {"source_span_id":"c2efafd4-7fb7-5c70-900c-ac5b34732c4e","locator":{"kind":"page","page":129,"label":"Slide 129","section_title":"Giới Hạn Của Single-Pass RAG (Tại sao phải tiến hóa?)","extraction_method":"pdf-text-layer"},"checksum":"dcf0673a0e924ae4be994b65b1851f2440c202043a28b852d8fc58c7372203b4"} -->

## Slide 129 - Giới Hạn Của Single-Pass RAG (Tại sao phải tiến hóa?)

RAG truyền thống là luồng một chiều: Nhận câu hỏi → Tìm 1 lần → Trả lời. "Dựa vào báo cáo tài chính quý 1, hãy lấy doanh thu trừ đi chi phí nhân sự và so sánh tỷ lệ đó với đối thủ Apple" Hạn chế: RAG không biết làm toán phức tạp và không thể tự động tìm kiếm thông tin bên ngoài. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"a9806928-dc16-59b3-8076-73ea66d66fd9","locator":{"kind":"page","page":130,"label":"Slide 130","section_title":"Chuyển Đổi Mô Hình: Từ RAG Sang Agent","extraction_method":"pdf-text-layer"},"checksum":"5cb90c63bcab89efc0c1f7ea0d1b98a5b9315b4586269d4904854cb15ee2144f"} -->

## Slide 130 - Chuyển Đổi Mô Hình: Từ RAG Sang Agent

RAG LLM là "Cái miệng" Tổng hợp thông tin đã được mớm sẵn từ hệ thống truy xuất. AGENT LLM là "Bộ não" Reasoning Engine: Tự lập kế hoạch, quyết định công cụ và thực hiện vòng lặp (Loop) xử lý. Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"10d5c552-5302-54ab-b66f-9a33041de30e","locator":{"kind":"page","page":131,"label":"Slide 131","section_title":"Retriever Giờ Chỉ Là Một \"Công Cụ\"","extraction_method":"pdf-text-layer"},"checksum":"e59c14d36ae2a77a30e39e4d851280ba5bc432efd51d4a412b6f332eff4d4c91"} -->

## Slide 131 - Retriever Giờ Chỉ Là Một "Công Cụ"

- Trong thế giới Agent, toàn bộ module
Retrieval khổng lồ ta vừa học hôm nay sẽ được đóng gói lại thành một hàm

### Python đơn giản
search_internal_docs(query: str).

- LLM sẽ tự quyết định: "À, câu hỏi này
cần luật nội bộ, mình sẽ gọi Tool này. Câu hỏi kia hỏi về thời tiết, mình sẽ không gọi Tool này." Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"d16443ca-37af-563b-965f-7d6224199d07","locator":{"kind":"page","page":132,"label":"Slide 132","section_title":"Multi-Agent Systems","extraction_method":"pdf-text-layer"},"checksum":"a4080475c8d3c1906b905d7fb41c63b3c4ec06c0e8a2655d7c9a4eb28ab8e84a"} -->

## Slide 132 - Multi-Agent Systems

- Khi hệ thống lớn lên, một Agent không
thể ôm đồm mọi việc (quá tải System Prompt).

- Cần chia nhỏ thành các Worker (Nhân
sự): 1 RAG Agent chuyên đọc tài liệu, 1 SQL Agent chuyên đọc số liệu, 1 Supervisor Agent làm sếp chỉ việc.

- Ngày 09: Chúng ta sẽ dùng LangGraph
để vẽ sơ đồ giao tiếp cho các Agent này. LANGGRAPH Supervisor HR_Doc RAG Agent Finance_SQL SQL Agent Web_Search Search Agent Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

---

<!-- chiron-source-span: {"source_span_id":"a2d402a7-1f1b-56a7-b0a5-3937316fa33d","locator":{"kind":"page","page":133,"label":"Slide 133","section_title":"Hands-on 8","extraction_method":"pdf-text-layer"},"checksum":"588d4313851a55d094385eebc3fdd9cdbaf780f9c1ce1ae634103529bc5a3a8f"} -->

## Slide 133 - Hands-on 8

5 Biến artifact Day 07 thành full RAG pipeline có retrieval, prompt grounding, test set.

---

<!-- chiron-source-span: {"source_span_id":"fbe6160c-075c-5041-8bb7-180b9f448596","locator":{"kind":"page","page":134,"label":"Slide 134","section_title":"Lab 8: Full RAG Pipeline","extraction_method":"pdf-text-layer"},"checksum":"41ac43de81a0a61f490d303d719a4108297733cd11dcf3cf2f5396787d7de64a"} -->

## Slide 134 - Lab 8: Full RAG Pipeline

Nâng cấp hệ thống Day 07 để trả lời grounded hơn, đo được hơn, và dễ giải thích hơn với stakeholder kỹ thuật lẫn sản phẩm.

1. Index bộ tài liệu domain nhỏ với metadata rõ ràng

2. Build baseline retrieval + answer function

3. Thử hybrid hoặc rerank ở mức tối thiểu nếu phù hợp

4. Tạo 10 test questions với expected evidence

5. Chấm kết quả theo scorecard trước và sau tuning Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 28 / 32

---

<!-- chiron-source-span: {"source_span_id":"006e92d4-8345-5478-b1b3-1f597902886e","locator":{"kind":"page","page":135,"label":"Slide 135","section_title":"Deliverable Cần Nộp","extraction_method":"pdf-text-layer"},"checksum":"0342aea2bd617ccf262465eda580c3c998d4506848ac260a4a9bc7f7e7cb7886"} -->

## Slide 135 - Deliverable Cần Nộp

Code + data

- script indexing

- retrieval / answer
function

- bộ docs nhỏ đã index
Eval artifact

- 10 test questions

- expected answer / evidence

- scorecard trước và sau
tuning Lưu ý: Không cần build hệ thống phức tạp. Điều quan trọng là chứng minh được vì sao bản tuning tốt hơn baseline. Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 29 / 32

---

<!-- chiron-source-span: {"source_span_id":"8eaf9d76-1449-573f-9fd0-18d539278580","locator":{"kind":"page","page":136,"label":"Slide 136","section_title":"Khung Nghĩ Để Tuning RAG Sau Buổi Học","extraction_method":"pdf-text-layer"},"checksum":"083e449737cd51a507336df6701ba0577ef0b6e8f2d7ccaef7d9208974c88fee"} -->

## Slide 136 - Khung Nghĩ Để Tuning RAG Sau Buổi Học

1. Index sạch chưa? text, metadata, freshness ổn chưa?

2. Retrieve đúng chưa? dense-only có đang miss keyword hay alias không?

3. Có cần rerank không? top-k hiện tại có trùng lặp nhiều không?

4. Prompt có grounded không? model có biết từ chối khi thiếu chứng cứ không?

5. Eval có nói thật không? testset đã đủ các câu khó và câu mơ hồ chưa? Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 30 / 32

---

<!-- chiron-source-span: {"source_span_id":"055ab5e4-c040-59ee-885e-60730891956d","locator":{"kind":"page","page":137,"label":"Slide 137","section_title":"Tổng kết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"65075535790c8d591ffd1e844b34c3a0d6bef0904b141b284a8759f804b5fd05"} -->

## Slide 137 - Tổng kết — Key Takeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 RAG là sự phối hợp giữa indexing, retrieval, và generation; thiếu bước nào cũng dễ làm hệ thống trả lời sai. 2 Retrieval quality > generation polish trong nhiều bài toán thực tế. Search sai thì prompt đẹp đến đâu cũng khó cứu. 3 Hybrid retrieval và rerank là hai đòn bẩy rất thực dụng khi dense-only bắt đầu bộc lộ giới hạn. 4 RAG muốn tốt lên phải có test set + scorecard + A/B tuning, không thể dựa vào cảm giác. Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 30 / 32

---

<!-- chiron-source-span: {"source_span_id":"e3ef00c5-a7a2-5038-8d9a-b5b4a98b7562","locator":{"kind":"page","page":138,"label":"Slide 138","section_title":"Tài Liệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"5af19055d2b150590df2b8d76bad55fbc699c4d45e57e15634574fb50af9b38f"} -->

## Slide 138 - Tài Liệu Tham Khảo

1. Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.

2. OpenAI Docs, Retrieval Guide và File Search Guide.

```text
3. LangChain, RAG from Scratch notebooks.
```

4. LlamaIndex Docs, Starter Example.

5. RAGAS Docs, Evaluation metrics for RAG systems.

6. Cohere Docs, Rerank overview. Giảng viên (VinUni) AICB · Ngày 8 Tuần 2 32 / 32

---

<!-- chiron-source-span: {"source_span_id":"503eb234-dd51-54d2-8249-e28824748d6d","locator":{"kind":"page","page":139,"label":"Slide 139","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"5f943bc6aa341cbe8300cbfa67488ca7ab88f83be197c55c42572ae4461e7f6c"} -->

## Slide 139 - Hỏi & Đáp

Bạn đang thiếu model mạnh hơn, hay đang thiếu một pipeline retrieval và evaluation đủ kỷ luật?
