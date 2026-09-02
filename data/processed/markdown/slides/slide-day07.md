---
schema_version: 1
course_id: rag-intensive
document_id: "39e02b2f-c12c-5c7b-8bae-328336686b2a"
document_version_id: "72932e06-9e68-5002-8ed2-e91184b07550"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Data Foundations"
source_file: "SLIDE DAY07.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\SLIDE DAY07.pdf"
source_sha256: "6d7611d322fde88e4435feedfddcd2d2533f3f46217b6784eb446f045e632c3a"
parser_version: chiron-structured-markdown-v1
page_count: 97
sparse_page_count: 2
extraction_methods: "{\"pdf-text-layer\":95,\"pdf-text-layer-sparse\":2}"
language: vi
---

# Data Foundations

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"b139359b-dd1e-5923-8b86-e7d23abfbf78","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Data Foundations","extraction_method":"pdf-text-layer"},"checksum":"29e9762d1db922abc3b1dd5c05eecb2eb0c08bb53a63b6fa41b76bdd9b1e357b"} -->

## Slide 1 - Data Foundations

AICB-P1 · Ngày 7 · Embedding, Chunking & Vector Store TênGiảng Viên VinUniversity · Phase 1 · Tuần1· 2026

---

<!-- chiron-source-span: {"source_span_id":"35b714f7-9f83-512f-9371-e27e0949f54f","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"b3dba90239ebfbf65758d4580d471e9760d94a6d6f387d81dac256c39bebd211"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Agent trả lời sai vì model yếu, hay vì nó không có đúng dữ liệu để suy luận?” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"d61978fe-2d17-5fb7-a64c-60c35ab6c53e","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"ce78dda0d1667441ea534085cb3297d81d4931a766c592f82f3c62c6b604e183"} -->

## Slide 3 - NộiDung Bài Học

1. Datastrategy & agent memory

2. Lịchsử: từ TF-IDFđến embedding

3. Embeddings— bản chất

4. Embeddingmodel landscape 2026

5. Documentextraction (PDF,Excel, HTML…)

6. Chunking& chuẩn bị tài liệu

7. Vectorstore internals (ANN)

8. FAISS,ChromaDB & landscape

9. Metadatafilter & hybrid search

10. Frontier2025–26

11. Đolường, chi phí & failuremodes

12. Bảomật & quyền riêng tư

13. Lab7 + Key takeaways Giảngviên (VinUni) AICB· Ngày 7 Tuần1 1 / 79

---

<!-- chiron-source-span: {"source_span_id":"d5d26cbe-a798-53fe-809f-08ed2cef027f","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"MụcTiêuNgày 7","extraction_method":"pdf-text-layer"},"checksum":"3ae04a7651bd3259636df4c65329adfa8990c5dc51f59af749eb417576b9f379"} -->

## Slide 4 - MụcTiêuNgày 7

- Phânbiệt đượcknowledgedata, operational data, contextual data

- Hiểuembeddinglàlớp biểu diễn nghĩa —cơ chế, cách huấn luyện, vàgiới hạn

- Bócđược text ra khỏi filethật—PDF,Excel, HTML — và biếtcái gì bị mất im lặng

- Chọnđược chunkingstrategy vàgiải thích được đánh đổicủa nó

- Giảithích đượcANNindex (IVF,PQ, HNSW) đủ để chỉnh thamsố, không chỉ gọi API

- Nhậndiện được cácfailuremode im lặng—lỗi không ném exception nhưngphá recall

- Buildđược mộtminiretrieval integrationnốiagent với dữ liệu riêng
Giảngviên (VinUni) AICB· Ngày 7 Tuần1 2 / 79

---

<!-- chiron-source-span: {"source_span_id":"b1d4a2bd-f7c2-5d54-a919-d6a91e7df84c","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"784f63eb054d939fcd5c16251ab83d036dddb5d142cea6a219980547c3997828"} -->

## Slide 5 - DeliverableCuối Ngày

Artifactpack cần nộp Datainventory+chunking/embeddingscript+vectorstoreindex+semanticsearch demo+ retrieval-enabled answer function

- 1bộ dữ liệu mẫu đã đượcchunk và index

- 1script truy vấn semantic search cótrả kết quả liên quan

- 1hàm trả lời sử dụng contextretrieve được thay vì hỏi LLM“chay”

- 1bảng đorecall@5trêntối thiểu 10 câu hỏi tựsinh
Giảngviên (VinUni) AICB· Ngày 7 Tuần1 3 / 79

---

<!-- chiron-source-span: {"source_span_id":"9b64ae5f-ec52-5511-967c-22f1cc167c7a","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Data Strategy Cho Sản Phẩm AI","extraction_method":"pdf-text-layer"},"checksum":"00b496329578b7aa7965c2cfb61cb87407cdc2a1853caf599498ebcaad62f1a1"} -->

## Slide 6 - Data Strategy Cho Sản Phẩm AI

01 Khi ai cũng gọi được model mạnh qua API, câu hỏi đã đổi từ “dùng model nào? sang “agent được phép biết gì, và có đúng dữ liệu để suy luận không?

---

<!-- chiron-source-span: {"source_span_id":"f8cb74f5-a306-5cfc-867c-fbaac0b6c76a","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"GarbageIn, Garbage Out — DataQuyết Định Output","extraction_method":"pdf-text-layer"},"checksum":"7fb7c7780763a4a2f8cce0b052aa55e00df584355caf26e942dfe5b36c65269f"} -->

## Slide 7 - GarbageIn, Garbage Out — DataQuyết Định Output

Dữliệu bẩn / thiếu

- PDFscan lỗi OCR

- Policycũ, chưa cập nhật

- Chunkcắt giữa câu

- Khôngcó metadata
Kếtquả: agenthallucinate,trảlờisai, usermất niềm tin. Dữliệu sạch / đầy đủ

- Textđã chuẩn hóa, metadata đầy
đủ

- Nguồnrõ ràng, có version

- Chunktheo section hợp lý

- Filterđược theo category +
freshness Kết quả: retrieve đúng, answer grounded,có trích nguồn. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 4 / 79

---

<!-- chiron-source-span: {"source_span_id":"4316c4c5-26a7-5184-8bff-f380f5e2a95b","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"3Loại Data Agent Cần","extraction_method":"pdf-text-layer"},"checksum":"29feadf9cb33bb75f5c7f261b886c6ad9d00305a11b8e97d5eab55aea692a41d"} -->

## Slide 8 - 3Loại Data Agent Cần

Loạidata Đặcđiểm Vídụ Retrievalfit Knowledge Ítthayđổi,dạngtextdài, cầnchunk + embed FAQ,SOP,chínhsách,hợp đồng,tài liệu kỹ thuật Rất cao — lý tưởng chovector store Operational Thay đổi liên tục, dạng structured (SQL / JSON /logs) Trạngtháiđơnhàng,CRM, ticket,tồn kho Thấp — dùng func- tion calling / SQL, khôngembed Contextual Gắn với session / user hiệntại, ngắn gọn User profile, lịch sử hội thoạigần nhất, giỏ hàng Trung bình — inject trực tiếp, ít khi cần semanticsearch Knowledge data phù hợp retrieval; operational data cần query có kiểm soát; contextual data nên inject ngắn và đúng lúc Giảngviên (VinUni) AICB· Ngày 7 Tuần1 5 / 79

---

<!-- chiron-source-span: {"source_span_id":"100b1e8e-2a8b-5317-a825-da3e65b24f78","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"DataGovernance & PII Masking TrướcKhi Embed","extraction_method":"pdf-text-layer"},"checksum":"f07087780af902c062c717e930ee602acbcf6cf6a1d61370f24f7c0cd3ee269a"} -->

## Slide 9 - DataGovernance & PII Masking TrướcKhi Embed

Governancetrước khi index:aisở hữu & cập nhậtdữ liệu·aiđược truy cập (ACL vspublic nội bộ)·baolâu re-index · PIIcó cần mask không —□ không“cứ nạp hết vào vectorDB đã”. LoạiPII Vídụ Kỹthuật mask Rủi ro nếu bỏ qua Têncá nhân “NguyễnVăn A” Thaybằng [PERSON] Trungbình Sốđiện thoại “0912-xxx-xxx” Regexreplace Cao Email “user@email.com” Hashhoặc remove Cao CMND/ CCCD “012345678901” Xóahoàn toàn Rấtcao Địachỉ “123Lê Lợi, Q.1” Generalize thành “Q.1, HCM” Trungbình Masktrước khi embed—không bao giờ lưu rawPII trong vector store.Vector không phải dữ liệu đã ẩn danh — embedding có thể bị đảo ngược gần đúng nguyên văn (Morris et al., EMNLP 2023; ALGEN 2025). Đầy đủ ở §11 — Bảo mật & Compliance. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 6 / 79

---

<!-- chiron-source-span: {"source_span_id":"cf63e42e-9e92-53a5-943f-58d50e5c60b3","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"MemoryLifecycle & Cái Gì KHÔNGPhải Memory","extraction_method":"pdf-text-layer"},"checksum":"4f483ef5f41c86e3de46e26e8ffd872e03c405930db84a5e96575fd6f042fece"} -->

## Slide 10 - MemoryLifecycle & Cái Gì KHÔNGPhải Memory

Capture Filter Store Retrieve Sự kiện nào đáng lưu? PII? quality? relevance? vector / DB / profile truy khi có ích cho câu hỏi hiện tại KHÔNGtự động là memory: promptdài hơn ·filePDF upload một lần khôngtruy lại có chủ đích·toànbộ chat history·“lưucho chắc” — nhữngthứ này thường tạo nhiễuhơn là hữu ích. Khungnghĩ đúng — và đừngnhầm với retrieval Memorylà data+policy+retrieval ;thiếumộttrongbathìhệthốngkhóổnđịnh. Retrievaltìmcontextchocâuhỏi hiện tại (relevance, grounding);memory giữ trạng thái người dùng qua thời gian (continuity). Nhầm hai khái niệm làlý do agent “quên” contextvừa retrieve ở lượt sau. Vocabchuẩn:working/ episodic / semantic /procedural. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 7 / 79

---

<!-- chiron-source-span: {"source_span_id":"012b6a56-558f-5556-b9a8-8be431c1da8c","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Document →Chunk →Embed →Store →Query →Inject","extraction_method":"pdf-text-layer"},"checksum":"d01f38df65706f7b1a009904ad30c149025294178510127db38eb12ebb31c14b"} -->

## Slide 11 - Document →Chunk →Embed →Store →Query →Inject

Document Chunk Embed Store Query Inject PDF, docs, HTML chia theo section / token vector hóa index + metadata semantic search prompt grounded Đâylà trục xương sống củacả Ngày 7 Mọi phần tiếp theo hôm nay chỉ đào sâumột mắt xíchtrong pipeline này:Chunk

- phầnChunking, Embed →phầnEmbeddings, Store →phầnVectorStore(Chro-
maDB/FAISS)vàANNinternals, Query →phầnRetrieval&HybridSearch, Inject → phầnKết nối Agent với Data vàEval. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 8 / 79

---

<!-- chiron-source-span: {"source_span_id":"70b0f8b3-72d0-5abd-b385-2b1ca575cbd4","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Lịch Sử: Từ TF-IDF Đến Embed","extraction_method":"pdf-text-layer"},"checksum":"f2eef5a1bf55886c4b0655313b8bf6b065a3b0589b122cd4a9c9c35615dc26f4"} -->

## Slide 12 - Lịch Sử: Từ TF-IDF Đến Embed

02 Lịch Sử: Từ TF-IDF Đến Embed- ding Embedding + cosine similarity là ý tưởng từ 1975 — cái thay đổi là vector đến từ đâu, không phải hình học

---

<!-- chiron-source-span: {"source_span_id":"a600d312-98d4-5987-8cdc-a1f8100e6f77","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"VấnĐề Gốc: VocabularyMismatch","extraction_method":"pdf-text-layer"},"checksum":"94a13f9cef88b53e059ad672ef0c14a9b7981bde17bec9bd7783990da1ea1598"} -->

## Slide 13 - VấnĐề Gốc: VocabularyMismatch

- Lexicalsearch (TF-IDF,BM25) chỉ
khớpkhi đúngtừ xuấthiện ở cả querylẫn document.

- IDF(SpärckJones, 1972): từhiếm
đượctính trọng số cao hơn từphổ biến— nền tảng của TF-IDF.

- BM25(Robertson& Spärck Jones,
giớithiệu tại TREC-3,1994)— vẫn là baselinelexical chuẩn mực đến 2026. Vídụ thất bại Query: “chính sách hoàn tiền”. Doc- ument chỉ viết: “quy định đổi trả sản phẩm”. Không từ nào trùng khớp⇒ BM25/TF-IDF không tìm ra, dù nghĩa gầnnhư giống hệt. Lưuý: BM25không“lỗithời”: BEIR(2021,18dataset)chothấyđâyvẫnlàbaseline mạnh—mộtdensemodelfine-tunetrênMSMARCOcóthể thuaBM25khirangoài domainhuấn luyện. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 9 / 79

---

<!-- chiron-source-span: {"source_span_id":"4512a7e2-76aa-58a0-bcd7-b86bec677a07","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"MộtBảng, 50 Năm: Lexical→Latent →Dense","extraction_method":"pdf-text-layer"},"checksum":"bfe41f81a446de66b622df0ded72b1060a0d138149d8a34f63632a521ae8051b"} -->

## Slide 14 - MộtBảng, 50 Năm: Lexical→Latent →Dense

Năm Cộtmốc Ýnghĩa 1972 SpärckJones — IDF Từhiếm đáng giá hơn từphổ biến 1975 Salton— VectorSpace Model Vănbản/query = vector,sobằng hình học 1990 Deerwester— LSA/LSI SVDnéncòn ∼100chiều“kháiniệm”—tổtiên củadense embedding 1994 Robertson— BM25 (TREC-3) Baselinelexical chuẩn mực đến hômnay 2013 Mikolov— word2vec Denseword vector đầu tiên ởquy mô web 2016 Malkov& Yashunin— HNSW GraphANN—defaultindexcủahầuhếtvector storehôm nay 2018/19 Devlin— BERT Contextualencoder,giới hạn 512token 2019 Reimers& Gurevych — SBERT Sửa hình học similarity mà BERT thô không làmđược 2020 Karpukhin— DPR DenseretrievalvượtBM25(+9đến+19%top- 20accuracy) 2025–26 Decoder-LLMembedder + MRL + quantization “Table stakes”: Qwen3-Embedding, Gemini Embedding2, Voyage4 Bỏ bớt các mốc phụ để giữ một trang; chi tiết từng mốc nằm ở các frame sau và trong RESEARCH companion Giảngviên (VinUni) AICB· Ngày 7 Tuần1 10 / 79

---

<!-- chiron-source-span: {"source_span_id":"97e78224-ae33-588a-a918-7788d44447f8","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"VìSao Raw BERT Tệ ChoSimilarity Search?","extraction_method":"pdf-text-layer"},"checksum":"531378961b5aee441628abf90544a7e7dbbcc11a71e7c767852d1da9b5bae1af"} -->

## Slide 15 - VìSao Raw BERT Tệ ChoSimilarity Search?

Cross-encoder: BERT gốc So hai câu ⇒ BERT (2018/19) — 512- tokencap — cần joint attention.

- Muốnsohaicâu ⇒phảiđưa cảcặp
quaBERTcùng lúc.

- Sokhớp giữa 10.000 câu⇒ ∼50
triệuphép suy luận.

- ∼65giờ trênGPU để tìm cặp giống
nhaunhất. Train cho masked-LM, không cho pooled similarity — không báo lỗi, chỉ cho vector không so sánh được. Bi-encoder: SBERT (2019)

### Reimers & Gurevych (EMNLP 2019)
siamese network, contrastive fine-tune trênNLI.

- Encodemỗi câumộtlần,độc lập ⇒
vectorcố định, precompute trước.

- Sosánh bằng cosine similarity,
khôngcần chạy lại BERT.

- Cùngbài toán: ∼5giây —độ chính
xáctương đương trên STS. Đây là lý do vector store precompute em- bedding tài liệu một lần rồi query nhanh. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 11/ 79

---

<!-- chiron-source-span: {"source_span_id":"76277956-6a7b-57ff-a4e3-6f3ad9054127","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Embeddings — Bản Chất","extraction_method":"pdf-text-layer"},"checksum":"b0370e992c7e2f400655d5f316d4ed7022cb58e2be7c85f9f6abba73db1b68d9"} -->

## Slide 16 - Embeddings — Bản Chất

03 Embedding không phải phép màu; nó là một hàm học được, và hình học của nó là sản phẩm phụ của mục tiêu huấn luyện

---

<!-- chiron-source-span: {"source_span_id":"f00f6149-8c8e-5d48-984e-650a3ffffc96","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"EmbeddingLà Gì — Cơ ChếThật, Không Phải Phép Màu","extraction_method":"pdf-text-layer"},"checksum":"8182af4900cd84b03018716f535e99366050c61505850fd46bb044bf4614a016"} -->

## Slide 17 - EmbeddingLà Gì — Cơ ChếThật, Không Phải Phép Màu

Embedding — Hàm học được biến dữ liệu thô (text, ảnh, audio) thànhvector số cùngchiều,sao cho “gần nghĩa”→“gầnhình học”.

### Mộtpipeline cụ thể, chạy trên GPU/CPUcủa ai đó

1. Tokenize: cắt câu thànhsubword token

2. Encoder: token qua nhiềulớp Transformerself-attention→vector theo ngữ cảnh

3. Pooling: gộp vector tokenthànhmộtvectorcâu — mean, last-token, hoặc[CLS] Poolingkhông trung lập jina-embeddings-v5: meanpooling(v4) →last-token—mấtLateChunking,vốncần vectortheo token. Đổipooling là đổi cả model. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 12 / 79

---

<!-- chiron-source-span: {"source_span_id":"40be9303-c687-5fcf-b69f-c4fa425995e8","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"CôngThức: Đừng Sợ,Chỉ Có 2 Dòng","extraction_method":"pdf-text-layer"},"checksum":"3a17a37ae4ba762b23f18a0958068f5d2e5b436caaa91f46c3c412593e91b255"} -->

## Slide 18 - CôngThức: Đừng Sợ,Chỉ Có 2 Dòng

CosineSimilarity cos(⃗A, ⃗B) = ⃗A · ⃗B ∥⃗A∥ ∥⃗B∥

- Tử: tích vô hướng(dot product)

- Mẫu: tích hai độdài đã chuẩn hoá

- 1=cùng hướng, 0=vuông góc, −1=
ngượchướng EuclideanDistance d(⃗A, ⃗B) = vuut nX i=1 (Ai − Bi)2

- Khoảngcách “đường chim bay”n
chiều

- 0=trùng nhau, càng lớn = càngxa
Khôngcần tự code Hầuhếtvectorstoremặcđịnhdùngcosine—hiểuscore 0.87sovới 0.31nghĩalàgì (framesau). Giảngviên (VinUni) AICB· Ngày 7 Tuần1 13 / 79

---

<!-- chiron-source-span: {"source_span_id":"a59f4b54-6ac8-5b02-9f53-65ea408dd8e0","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"BàiTập Nhanh: TínhCosine Similarity Bằng Tay","extraction_method":"pdf-text-layer"},"checksum":"e655bc5b5921dc8836cf1911f28314455f3efd9c3286ab5760cc301e7b1ac8ae"} -->

## Slide 19 - BàiTập Nhanh: TínhCosine Similarity Bằng Tay

Cặp1 ⃗A = [1, 2, 3] ⃗B = [2, 4, 6] cos(⃗A, ⃗B) =? Gợiý: ⃗A · ⃗B = 1×2 + 2×4 + 3×6 Cặp2 ⃗C = [1, 0, 0] ⃗D = [0, 1, 0] cos(⃗C, ⃗D) =? Gợiý: hai vectornày có điểm chung nào không? Tính trên giấy hoặc máy tính (3 phút), so đáp án với người bên cạnh. Lưuý: Cặp1cócosine = 1.0dù ⃗B = 2⃗A. Vìsao? Điềunàynóigìvềcosinesimilarity sovới Euclidean distance? Giảngviên (VinUni) AICB· Ngày 7 Tuần1 14 / 79

---

<!-- chiron-source-span: {"source_span_id":"cff3bf02-c83e-5fa7-b334-727f58378cc5","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Myth: “Cosine Similarity =Độ Liên Quan Thật”","extraction_method":"pdf-text-layer"},"checksum":"f10dea5c11bd84c27a302378aa13f10d17acb97f1f710597fb0f473baddf6ae3"} -->

## Slide 20 - Myth: “Cosine Similarity =Độ Liên Quan Thật”

Lưuý: Steck,Ekanadham&Kallus(Netflix+Cornell), Is Cosine-Similarity of Embed- dings Really About Similarity?,WWW2024: cosinesimilaritycủaembeddingđãhọc “canyieldarbitraryandmeaninglesssimilarities” —vớilinearmodelregularized, cosinekhôngxác định duy nhất. Nguồn: arXiv:2403.05440, WWW’24.

- Regularizationdeep learning tác động “implicit vàunintended” lên cosine.

- Mộtsố trường hợp, cosine tệ hơndot product chưa chuẩn hoá.
Cáchdạy đúng Cosinelà conventionhiệuquả,khôngphải sựthật vềýnghĩa. “Metricmặcđịnh”là lựachọn kỹ thuật, không phải luậttự nhiên. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 15 / 79

---

<!-- chiron-source-span: {"source_span_id":"57af8aed-6f00-5c8f-aab7-30c7d7a71bf7","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Asymmetricvs Symmetric Search: Cái Bẫy Prefix","extraction_method":"pdf-text-layer"},"checksum":"551222e45ad8008019ebf78a666a227b0600fec5d1a16d236c57ca44d70325b9"} -->

## Slide 21 - Asymmetricvs Symmetric Search: Cái Bẫy Prefix

Symmetric

- Queryvà documentcùngloại (câu ↔
câu)

- Vídụ: tìm câutrùng lặp, STS
Asymmetric

- Câuhỏi ngắntìmđoạn văndài

- Đâychính là RAG
Modelđược huấn luyện khác nhau chohai phía — nên exposeprefixhoặcinstruction riêng: E5 dùngquery: / passage:;Nomic v2 dùngsearch_query: / search_document:. Lưu ý:Bỏ prefixkhông báo lỗi— nó âm thầm tạo ra embedding lệch calibration, xếp hạng sai. Model card Qwen3-Embedding-8B: dùng instruction cải thiện1% đến 5%sovới không dùng. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 16 / 79

---

<!-- chiron-source-span: {"source_span_id":"ee44ddf4-13cf-57fe-9a08-33da861e9014","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Code: Encode + CosineSimilarity (sentence-transformers)","extraction_method":"pdf-text-layer"},"checksum":"69e7128586d158c120e930b31a3b8e248fe68990f2f0a7a6c04fedf13d4e3183"} -->

## Slide 22 - Code: Encode + CosineSimilarity (sentence-transformers)

# pin the version -- 5.6.1 shipped one week before this lecture

```text
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
model = SentenceTransformer( "BAAI/bge-m3")
texts = [ "Chinh sach hoan tien", "Quy dinh doi tra"]
embeddings = model.encode(texts, normalize_embeddings=True)
score = cos_sim(embeddings[0], embeddings[1])
print(score.item())
normalize_embeddings=True đãchuẩnhoáL2ngaytrong.encode()—nên cos_simởđâytương
```
đươngcosine, không lệch bởi magnitude. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 17 / 79

---

<!-- chiron-source-span: {"source_span_id":"86515cdf-508f-5b28-abae-11f60a8d9dc6","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Bức Tranh Embedding Model","extraction_method":"pdf-text-layer"},"checksum":"ec238e70c23955f7db37459e314ffe9c9a2c47fe69ac68ec3ec71cbe40770c12"} -->

## Slide 23 - Bức Tranh Embedding Model

04 2026 Không có model “tốt nhất”; chỉ có model đúng cho trục quali- ty/speed/size/cost mà bạn cần

---

<!-- chiron-source-span: {"source_span_id":"9a88bba8-adac-5985-9d3a-7a7237533a3f","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Open-WeightModels — Vài Đại Diện","extraction_method":"pdf-text-layer"},"checksum":"395dbdc3d241bebea886e0de8aa33ff2aab07cf2fbd5263ee67d69c0547710b2"} -->

## Slide 24 - Open-WeightModels — Vài Đại Diện

Model Params Outputdims Maxinput License Qwen3-Embedding (0.6B/4B/8B) 0.6–8B tới 4096, MRL

- 32
32K (cả 3 size) Apache-2.0 EmbeddingGemma 308M 768, MRL → 128 2K Gemmaterms BGE-M3 ∼568M dense+sparse +multi-vec 8192 MIT NomicEmbedTextv2 (MoE) 475M/305M active 768, MRL → 256 512 Apache-2.0 JinaEmbeddings v4 3.8B 2048 (hoặc multi-vector) long-context — Số liệu verbatim từ HF model card / arXiv của từng model, chốt 2026-07-30. BGE-M3 tạo cả ba biểu diễn dense+sparse+multi-vector cùng lúc — hybrid retrieval SOTA là một model, không phải ba hệ thống ghép lại. Nomic v2 max input chỉ 512 token, ngắn hơn nhiều embedder cũ dù là model 2025. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 18 / 79

---

<!-- chiron-source-span: {"source_span_id":"2658b81e-850e-5879-987d-99b1f7df0284","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"CommercialAPIs","extraction_method":"pdf-text-layer"},"checksum":"c48775ed591a8224be91746db11dfb9a8d32e973ffce59af281e5fc00c3ca4a2"} -->

## Slide 25 - CommercialAPIs

Model Dims Maxinput Giá /1Mtoken input OpenAI text-embedding-3-large tới3072 8191 $0.13 OpenAI text-embedding-3-small tới1536 8191 $0.02 Google gemini-embedding-2 MRLnative 8192 $0.20($0.10 batch) Voyage voyage-3.5 2048/1024/512/256 — $0.06 Cohere embed-v4 256/512/1024/1536 128K giá chưa xác minh được Giá xác minh trên trang chính thức từng vendor, 2026-07-30. Không có tier giá batch chính thức — chỉ “khoảng nửa giá” qua Batch API, không có số cụ thể. Lưu ý:Lầm tưởng: “OpenAI embeddings là mặc định tốt nhất.”-3-large/-small phát hành 25/1/2024, chưa cập nhật ∼2.5 năm trong khi Google/Voyage/Jina ra nhiều thế hệ mới.-3-large: $0.13/M so với voyage-3.5: $0.06/M— không có bằng chứngvượt trội.gemini-embedding-001 (giớihạn 2K token) đã bịthay bởi-2. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 19 / 79

---

<!-- chiron-source-span: {"source_span_id":"9648569a-7f48-51db-a9e0-3e8603dab9e9","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"MTEB:Một Model, Ba Board, BaCon Số","extraction_method":"pdf-text-layer"},"checksum":"b8bef6ee6aa2af14527f99f7518e6f588bf7464d19a8e16144ee5e3c24d9a10e"} -->

## Slide 26 - MTEB:Một Model, Ba Board, BaCon Số

MTEBđã tách thành nhiều boardkhôngso sánh được với nhau: MTEB(Eng, v2), MTEB(Multilingual)/MMTEB, MTEB(Code)... Điểm v2 khôngso được với v1.

### Vídụ thật,cùngmột model(GeminiEmbedding), ba con số

- MTEB(Multilingual)Mean(Task): 68.32—con số được quảng bálàm headline

- MTEB(Eng,v2) Mean(Task):73.28

- Task-TypeMean: 59.64
Lưuý: Lầmtưởng: “68.32làđiểmMTEBtiếngAnh.” Sai—đólàđiểm MULTILINGUAL.ĐiểmEnglishv2thậtlà 73.28. Lỗinày lanqua nhiềutrang tổnghợp, tạora sosánh tựmâuthuẫn (vd.đặt jina-v5-small71.7 “vượt”Gemini 68.32,trong khi English thật củaGemini là 73.28). Quytắc cho lớp Một con số MTEBvô nghĩanếu thiếu board + version + aggregation + ngày. (Cập nhật: từ 2025–26 MTEB đã chuyểnsang kết quảverified,không còn thuần self-reported.) Giảngviên (VinUni) AICB· Ngày 7 Tuần1 20 / 79

---

<!-- chiron-source-span: {"source_span_id":"304752f9-d3f9-5c4b-a2f8-3cb6dd3ef813","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"ĐaNgôn Ngữ Và TiếngViệt","extraction_method":"pdf-text-layer"},"checksum":"dfe2536be01a1239e33341d12b5da6ed11f2d854e516f51f9065138958e4ced7"} -->

## Slide 27 - ĐaNgôn Ngữ Và TiếngViệt

- VN-MTEB(EACL 2026 Findings): benchmark embedding tiếngViệtchuẩn hóa đầu
tiên— 41 dataset, 6 loại task(retrieval, reranking, classification, clustering, pair classification,STS).

- Pháthiện đáng chú ý: model dùngRoPEvượttrội hơn model dùng absolute
positionalembedding trên task tiếng Việt,ở nhóm model cùng quy mô.

- TrướcVN-MTEB, nhóm phát triển thườngchọn model tiếng Việttheo điểmMTEB
tiếngAnh vàhy vọng transfer tốt — khôngđảm bảo. Modelchuyên biệt tiếng Việt AITeamVN/Vietnamese_Embedding v2: fine-tune từ BGE-M3 trên ∼1.1 triệu triplet (query, positive, negative) tiếng Việt; 2048 max sequence, 1024 dims, Apache-2.0. Đườngđithựcdụng: khôngdùngthẳngmodelđangônngữ,cũngkhôngtraintừđầu —fine-tunemodel đa ngôn ngữ mạnh trêndomain triplet. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 21 / 79

---

<!-- chiron-source-span: {"source_span_id":"0a8b06cc-1b48-52d5-b569-bd9071289b02","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"ChọnEmbedding Model Trong20Phút","extraction_method":"pdf-text-layer"},"checksum":"8577a02bb40a4ecd60ddf2d4548985fc098fa75fb4efebb14dd1fcae9a85e27c"} -->

## Slide 28 - ChọnEmbedding Model Trong20Phút

5trục quyết định, không phải1 thứ hạng leaderboard:deployment,max input, dimension/precision, ngôn ngữ,query shape,license.

### Quytrình 20 phút

1. Viếtđộdàichunktốiđa vàdạngquery (cóexactcode/SKU/IDkhông?) —loạibớtứngviêntrướckhibenchmark.

2. Lậpshortlist 2–3 model theolicense+deployment(on-device/air-gappedhay API được phép?).

3. Xâybộ eval 50–100 query từchính corpus của bạn —khôngchỉdựa MTEB.

4. Đorecall@k trên bộ eval, dùngđúng prefix/instruction cho từng model.

5. Chỉsau đó mới tinh chỉnhdimension và quantization (MRL, int8/binary). 2lưu ý nhanh sau khichọn (1) SKU/code trong query: dense embedding thuần blur token chính xác — cần sparse (BGE-M3 có sẵn) hoặc hybrid BM25 (§9). (2) Đa phương thức: Cohere embed-v4 / Google gemini-embedding-2 nhúng text+image(+audio/video) vào cùng một vector space — vẫn áp dụng đủ 4 trục + license; Lab 7 vẫn dùng em- beddingtext thuần. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 22 / 79

---

<!-- chiron-source-span: {"source_span_id":"be16a410-7414-51e5-8acc-d57eef4a45d9","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Document Extraction: Từ File","extraction_method":"pdf-text-layer"},"checksum":"6f656db07375944262289c275bceb3fec6a933b05cb4e8daf8a4df446667524b"} -->

## Slide 29 - Document Extraction: Từ File

05 Thật Đến Text Trước khi có chunk, có embedding, có vector store — bạn phải lấy được text ra khỏi file. Đây là khâu quyết định trần chất lượng của cả pipeline

---

<!-- chiron-source-span: {"source_span_id":"77c56560-22d7-5878-81fc-514104c08536","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"BảnĐồ Dữ Liệu: Ba Nhóm, Ba Con Đường","extraction_method":"pdf-text-layer"},"checksum":"6a747d22349de34d6000fa081aa655083444e2d740cd21bcf90ffa3aeaedcbce"} -->

## Slide 30 - BảnĐồ Dữ Liệu: Ba Nhóm, Ba Con Đường

Nhóm Vídụ Cáchxử lý đúng Unstructured PDF scan, ảnh, chữ viết tay,audio transcript OCR / VLM parsing→ text + layout, rồi chunk theo cấu trúc Semi- structured HTML, DOCX, PPTX, Markdown,email Bóc boilerplate, giữ cây heading → chunk theo heading Structured Excel, CSV, SQL table, JSON,log Thường KHÔNG nên em- bedthô —text-to-SQLhoặc serialize theo hàng (§5, cuối section) Ba nhóm cần ba đường xử lý khác nhau — đừng ép tất cả qua cùng một parser Giảngviên (VinUni) AICB· Ngày 7 Tuần1 23 / 79

---

<!-- chiron-source-span: {"source_span_id":"18fe9eaf-b1f9-589e-8554-db247fb1a708","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"PDF:Vì Sao Khó Hơn BạnNghĩ","extraction_method":"pdf-text-layer"},"checksum":"7c683ad4420a2303a33837fd30cf2f212498a625c578202ecab56db37071456e"} -->

## Slide 31 - PDF:Vì Sao Khó Hơn BạnNghĩ

PDFlà định dạng mô tảCÁCH VẼ trang, không mô tảNỘI DUNG.Nólưu “đặt glyph này tại toạđộ (x,y)” — không lưu“đây là ô thứ 3 củahàng thứ 2 trong bảng”.

- Born-digitalvsscanned: filesinhtừWordcósẵntextlayer;filescanchỉlàảnh ⇒bắtbuộc
OCR.

- Readingorder: 2cột, sidebar,chú thích— pdftotext đọctheo thứ tự vẽ, cóthể trộn cột
tráivới cột phải thành câuvô nghĩa.

- Header/footerlặp: têncông ty + số trangchèn vào giữa mọi chunk, làmnhiễu embedding.

- Bảng: mấtquan hệ hàng–cột là lỗitốn kém nhất (frame riêng ởsau).

- Côngthức, biểu đồ, hình:thôngtin nằm trong pixel, khôngcó trong text layer.
Lưu ý:“PDF là text, chỉ cầnpdftotext” — đúng với đúng một loại tài liệu: born-digital, một cột,không bảng. Vớicorpus thật, đây là giả địnhsai đắt nhất trong cả pipeline. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 24 / 79

---

<!-- chiron-source-span: {"source_span_id":"1d88185a-74db-5102-b43b-71515402cb18","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"CôngCụ Parse Tài Liệu 2026","extraction_method":"pdf-text-layer"},"checksum":"b66bc81f86a20fd18214ad1911c85b783be8fb7c504a0051aeabb8177f5e3a70"} -->

## Slide 32 - CôngCụ Parse Tài Liệu 2026

Côngcụ Loại Ghichú thực dụng Docling(IBM) Pipeline,MIT license DocLayNet layout + TableFormer; mạnh vềbảng phức tạp; ra Markdown/JSON MinerU Pipelinehoặc VLM Bản 2.5-Pro đứng đầu OmniDocBench v1.6 theo báo cáo của chính nhóm tác giả Marker(Datalab) Pipeline Nhanh; benchmark v2 do chính Datalab chạy Unstructured Pipeline,hosted 30+ định dạng (kể cả email, HTML); có sẵnchunking LlamaParse Hosted Trả phí theo trang; tiện khi không muốn tựvận hành olmOCR(AI2) VLM7B ChuyênlinearizePDFchodatapipeline; 82.4trên olmOCR-Bench MarkItDown(MS) Chuyển đổi nhẹ Office-heavy, không GPU; hợp proto- type,yếu với PDF scan Nguồn: Docling arXiv:2501.17887 · olmOCR github.com/allenai/olmocr · dots.mocr arXiv:2512.02498 · DeepSeek-OCR arXiv:2510.18234 Giảngviên (VinUni) AICB· Ngày 7 Tuần1 25 / 79

---

<!-- chiron-source-span: {"source_span_id":"fdfdd519-29f4-5a4d-add8-c8674cef5fe2","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"OmniDocBench: Benchmark Đã GầnBão Hoà","extraction_method":"pdf-text-layer"},"checksum":"6fd19db18f6c4eeb76bde6d2d155af344025d726b5acbc5ad2467474cbb28a52"} -->

## Slide 33 - OmniDocBench: Benchmark Đã GầnBão Hoà

OmniDocBench(CVPR 2025, 1.355 trang, 9loại tài liệu) chấm 4 trục:text(editdistance), công thức(CDM),bảng(TEDS),readingorder.

- Trênv1.5: GLM-OCR94,6% (SOTA),PaddleOCR-VL-1.5 >94%,Gemini3 Pro 90,3%.

- MinerU2.5-Probáo cáo95,69trênv1.6, TableTEDS 93,42—con số từ chính papercủa
nhómtác giả. Lưu ý:Khi nhiều hệ vượt 94%, phần tăng thêm chủ yếu là “vá edge case”, không còn phản ánh chất lượng thực tế trên corpus củabạn. Tệ hơn: các bảng xếp hạngmâu thuẫn nhau — cùng bộ công cụ, đổi bộ tài liệu là đổi thứ hạng. Và phần lớn benchmark được chạy bởi chínhnhà cung cấp công cụ. Việccần làm thay vì tinbảng xếp hạng Lấy20trangkhónhất trongcorpuscủabạn(scanmờ,bảnglồng,2cột),chạyqua2–3công cụ,và đọcbằng mắt. Đó là benchmarkduy nhất có giá trị quyếtđịnh. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 26 / 79

---

<!-- chiron-source-span: {"source_span_id":"cfc6626a-93fd-51e2-96f8-d0e25a86704c","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"HTML:80% TrangWebKhôngPhải Nội Dung","extraction_method":"pdf-text-layer"},"checksum":"49e1d310b285fd6a36694bfa8a199b3c5ea1e6999b4b0053e4f62d03c383d07b"} -->

## Slide 34 - HTML:80% TrangWebKhôngPhải Nội Dung

Menu,banner,ad, footer,“bài liên quan” — nếu embedthẳng HTML thô, phần lớn vectormô tả giaodiện,không phải nội dung.

- Trafilatura—pipeline heuristic nhiều tầng,khôngML, không GPU,khoảng 14–22
ms/trang. Mặc định hợplý cho quy mô lớn.

- ReaderLM-v2(Jina)—transformer 1,54BhuấnluyệnriêngchoHTML →Markdown: cấutrúc
trungthực hơn, nhưng cần GPUvà chậm hơn nhiều bậc.

- justext—bóc boilerplate theo mật độstopword ở mức đoạn văn.

- Trangđã convert đúng thường dùngíthơn khoảng 65% tokensovới HTML thô⇒giảm
thẳngchi phí embed. Chiếnlược hai tầng thực dụng Chạytrafilaturatrướcchotoànbộcorpus;chỉchuyểnsangparsernặng(ReaderLM/html-to- markdown) cho những trang mà cấu trúc thực sự quan trọng. Đừng trả giá GPU cho 100% corpusđể cứu 5% trang. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 27 / 79

---

<!-- chiron-source-span: {"source_span_id":"f61c9b35-fded-56b5-9f0b-6ded3c957353","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Office& Email: CáiBạn Mất Khi Convert","extraction_method":"pdf-text-layer"},"checksum":"93ac173c7a4611e90c457a378b76f9f4c4e77b150c43cce273937ca78aed414a"} -->

## Slide 35 - Office& Email: CáiBạn Mất Khi Convert

- DOCX—giữ được cây heading (rấtquý cho chunking);mấtcomment,tracked changes,
footnotenếu parser không xử lýriêng. Một hợp đồngmà phần thương lượng nằm ở commentthì bản parse là bảnsai.

- PPTX—text trong shape thường rờirạc, thứ tự đọc theo thứtự tạo shape chứ không theo
thịgiác; speakernotes thườnglà phần có giá trịnhất và thường bị bỏ quên.

- Email—chữ ký, disclaimer pháp lývà thread reply lồng nhau khiếncùng một đoạn văn bị
indexhàngchục lần ⇒near-duplicatelàm hỏng top-k. Quytắc Với mỗi định dạng, hỏi hai câu:(1) cấu trúc nào đáng giữ để chunk theo?(2) nội dung nào bịmấtimlặngkhiconvert? Câuhaiquantrọnghơn—vìkhôngcóexceptionnàođượcném ra. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 28 / 79

---

<!-- chiron-source-span: {"source_span_id":"a1f3bdc3-fcf2-559a-90b9-62e1d2659bbe","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Excel& CSV:Sheet KhôngPhải Là Table","extraction_method":"pdf-text-layer"},"checksum":"1b1150a8da6344b8866989099c0d03040f18e5a447fff0e32cf2c58903764d46"} -->

## Slide 36 - Excel& CSV:Sheet KhôngPhải Là Table

Sailầm phổ biến: coi mỗi sheet là một bảngsạch và đẩy thẳng vàopandas.read_excel.

- Ômerge ⇒ NaNrảirác; phảifill-downđểkhôi phục quan hệ hàng.

- Headernhiều tầng(2–3dòng) ⇒têncột thật làghépcủacác tầng: “Q22026 ·Doanhthu ·
VND”.

- Mộtsheet có thể chứanhiềubảng rời+ô ghi chú tự do;ranh giới bảng phải tự dò.

- Formulavs value: lưu công thứchay kết quả? Vớiretrieval, gần như luôn làkếtquả.

- Số,ngày tháng, đơn vị: định dạng hiển thị khácgiá trị thật (1.234,56 vs 1234.56).

### Lưuý: Địnhdạngserializequyếtđịnhrecall. Mộthàngnêntrởthànhmộtđơnvị tựđủnghĩa
"Q2 2026 | Doanh thu | 4,2 t￿ VND" —không phải một ô “4.2”trôi nổi không có header. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 29 / 79

---

<!-- chiron-source-span: {"source_span_id":"453e8f31-ffea-56e9-8db5-f33d22b9029a","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"BảngLà Điểm Hỏng Im LặngSố Một","extraction_method":"pdf-text-layer"},"checksum":"b8e6f5b1f3d1d28b4235f7faf7709119726a10bfe957a7b559c7c835c1c96d3e"} -->

## Slide 37 - BảngLà Điểm Hỏng Im LặngSố Một

Khichunker cắt một bảng theoký tự, quan hệ hàng–cột biếnmất: header“Doanh thu Q2 2026” rơivào chunk này,giátrị “4,2 tỷ” rơivào chunk khác. Không kỹ thuật retrieval nào ghéplại được. Bằngchứng định lượng—Structure-aware TabularChunking (STC) so với RecursiveCharacterTextSplitter,trên MAUD (39.231 bản ghihợp đồng M&A từ SEC EDGAR),

### ngânsách 512 token
Chỉsố Recursive STC MRR(hybrid) 0,358 0,595 Recall@1(hybrid) 0,347 0,539 Recall@1(BM25) 0,366 0,754 Sốchunk sinh ra — íthơn ∼40% Nguồn: Guttal et al., “Structure-Aware Chunking for Tabular Data in RAG”, arXiv:2605.00318 (5/2026). Giảngviên (VinUni) AICB· Ngày 7 Tuần1 30 / 79

---

<!-- chiron-source-span: {"source_span_id":"04212fad-4f30-5f06-96f1-7fa2207f97a9","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"DữLiệu Có Cấu Trúc: Khi Nào KHÔNG NênEmbed","extraction_method":"pdf-text-layer"},"checksum":"601fb4e16501132263a231339b5193d8b2c62bddf746324d25e99b1d39fec17c"} -->

## Slide 38 - DữLiệu Có Cấu Trúc: Khi Nào KHÔNG NênEmbed

### Vớidữ liệu đã nằm trongbảng SQL, vector search thường làcông cụsai

- “Tổngdoanh thu quý 2 theovùng” — cầnaggregation,không phải similarity. Không
embeddingnào cộng được số.

- “Đơnhàng mới nhất của kháchX” — cầnsort+ filter chính xác,đúng thế mạnh của SQL.

- “Chínhsách hoàn tiền nói gì?” —đâymớilà việc của vector search.
Kiếntrúc thực dụng: định tuyến, không chọn một Một router quyết định: câu hỏi số liệu→ text-to-SQL; câu hỏi khái niệm→ vector search; câu hỏi quan hệ→graph. Nhiều hệ production 2026 chạy cả ba song song rồi hợp nhất kết quả. Lưuý: Embedtoànbộbảnggiaodịchthànhvectorlàanti-patterntốnkémvàkémchínhxác. Trướckhi embed bất cứ thứgì, hỏi:câuhỏi này có phải câuhỏi ngữ nghĩa không? Giảngviên (VinUni) AICB· Ngày 7 Tuần1 31 / 79

---

<!-- chiron-source-span: {"source_span_id":"8b6ae0dc-3bce-52fe-8b78-1ad33ccc0ddb","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"TàiLiệu TiếngViệt: Những Gì Hỏng Riêng","extraction_method":"pdf-text-layer"},"checksum":"c39fe9cb7ae60da82d2eab1abebaee5483e6e923665386e286e512e6bc064699"} -->

## Slide 39 - TàiLiệu TiếngViệt: Những Gì Hỏng Riêng

- Dấuthanh và dấu phụmangnghĩa: OCR nhầmmột dấu là đổi hẳn từ(ma / mà / má / mã /
mạ). Tesseractmặc định yếuở đúng điểm này.

- Độphân giải scan tối thiểu300 DPI—dưới ngưỡng đó,o/ô/ơvà a/ă/âbắtđầu lẫn.

- Chuẩnhoá Unicode bắt buộc: cùng một chữ“ế” có thể mã hoá dựngsẵn (NFC) hoặc tổ
hợp(NFD). Hai dạngkhôngkhớp nhaukhiso chuỗi và tạo rachunk trùng lặp mà mắt thườngkhông phân biệt được. Chuẩn hoá NFC toàn corpusngay sau khi parse.

- Côngcụ chuyên biệt tồn tại(VietOCR,PaddleOCR fine-tune cho tiếng Việt);các VLM đa
ngônngữ mới cũng đã kháhơn đáng kể. Nguồn: “A Survey on Vietnamese Document Analysis and Recognition”, arXiv:2506.05061 · Sino-Vietnamese PaddleOCRv5, arXiv:2510.04003. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 32 / 79

---

<!-- chiron-source-span: {"source_span_id":"7c110620-41c8-525f-9f9d-5589c68f3266","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"ChuẩnHoá Sau Parse — BướcAi Cũng Quên","extraction_method":"pdf-text-layer"},"checksum":"8394bfe43382eea5cb576a21f9ec3664ceef0ef06decb629caf31c6471c80309"} -->

## Slide 40 - ChuẩnHoá Sau Parse — BướcAi Cũng Quên

### Parsexong chưaphảilà xong. Trướckhi chunk

- UnicodeNFC chotoàn bộ text (đặc biệtquan trọng với tiếng Việt).

- Bỏheader/footer lặp—dò chuỗi xuất hiện ởcùng vị trí trên hầu hếttrang.

- Nốitừ bị gạch nối cuốidòng(de-hyphenation)và gộp dòng thành đoạn.

- Xoátrang trắng, mục lục, trangbìanếukhông mang thông tin truyvấn được.

- Khửtrùng lặp—cùng một tài liệu thườngtồn tại nhiều bản (v1, v2,final, final-2).
Provenance: giữ từ đây,không thể thêm sau Mỗiđoạntextnênmangtheo tênfile,sốtrang,đườngdẫnheading ngaytừlúcparse. Đây làthứchophépcâutrảlờitríchnguồn“theotrang14củahợpđồngA”.Nếukhônggiữởkhâu này,không khâu nào sauđó tạo lại được. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 33 / 79

---

<!-- chiron-source-span: {"source_span_id":"4cb98377-b1ec-572f-8266-e5aa30f62494","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Chunking & Chuẩn Bị Tài Liệu","extraction_method":"pdf-text-layer"},"checksum":"63fed4f8ff79f2f69f27978af8ed0b21d7103fbefad12371df6d2cffdd246c18"} -->

## Slide 41 - Chunking & Chuẩn Bị Tài Liệu

06 Chunk sai thì mọi retrieval xây trên top-k đều sai theo — không mô hình embedding nào cứu được một chunk tồi

---

<!-- chiron-source-span: {"source_span_id":"216858ca-ab76-5147-841a-83b8e4703841","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Chunking: Quá ToHay Quá Nhỏ Đều TrảGiá","extraction_method":"pdf-text-layer"},"checksum":"1970180e9b5e087fc627d1d3be830e6d77160c756b08a89cdbfff15b012343ba"} -->

## Slide 42 - Chunking: Quá ToHay Quá Nhỏ Đều TrảGiá

Chunking — Chiatàiliệudàithànhđoạn(chunk)nhỏhơn,embed/index riêng lẻ— tránhvượt giới hạn token, giúp retrievaltrúng đúngđoạnthayvì cả file. Chunkquá to Chunkhợp lý Chunkquá nhỏ Kíchthước >1000tokens 200–500tokens <50tokens Vấnđề Dính nhiều chủ đề vào cùngmột vector Một ý / một section trọn vẹn, overlap với chunk liềnkề Mất ngữ cảnh, retrieve nhiềumảnh rời rạc Hệquả khi retrieve Retrieve trúng nhưng in- jectrất nhiễu Cânbằngprecision/com- pleteness Khó tổng hợp thành câu trảlời đầy đủ Rule of thumb: bắt đầu đơn giản với chunk theo section/heading, tối ưu sau bằng eval — không đoán cảm tính Giảngviên (VinUni) AICB· Ngày 7 Tuần1 34 / 79

---

<!-- chiron-source-span: {"source_span_id":"d84631a2-96f0-5da5-9ba4-40c76fbca01c","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"“TạiSao Lại Là 512 Token?”","extraction_method":"pdf-text-layer"},"checksum":"2966e6fbdc89901da217e3f701bd153e01ffa80710843a4383916ab9993705f0"} -->

## Slide 43 - “TạiSao Lại Là 512 Token?”

BERT(2018) có bảng positional embeddinggiới hạn cứng ở512token —đây là giới hạnkiến trúccủamột model cụ thể năm2018, không phải một quy luậtretrieval.

- Consố này sống sót quavô số tutorial RAG như một“default” bất di bất dịch —lâu hơn hẳn
lýdo kỹ thuật ban đầu.

- Embedder2026 đã bỏ xa nó: BGE-M3 / Jina v2–v3tới 8K token; Qwen3-Embedding tới
32K;Cohere Embed v4 tới 128K. Lưu ý:Không có ngưỡng “512 token” phổ quát. Bhat, Rudat, Spiekermann & Flores-Herr (arXiv:2505.21700, 2025): chunk64–128 tokentối ưu cho câu hỏi factoid ngắn;512–1024 tokentốthơnkhicầnhiểungữcảnhrộng—vàtốiưucònphụthuộc embedding model(Stella lợivới chunk lớn, Snowflake lợivới chunk nhỏ, tập trung entity). Hệquả Đổiembeddingmodel ⇒phảiđolạichunksize. Đừngcopyconsốcủadeckkhácsangmodel khác. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 35 / 79

---

<!-- chiron-source-span: {"source_span_id":"385d5ebc-28db-5c12-bc3c-e98f8cf46cc5","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"ThangChiến Lược Chunking","extraction_method":"pdf-text-layer"},"checksum":"d2084eb66f8ec08224c51cd075efa0bcbd824a1e6d71d385c9497f8e89855717"} -->

## Slide 44 - ThangChiến Lược Chunking

Chiếnlược Cáchhoạt động Chiphí Khinào dùng Fixed-sizesplit Cắt theo số ký tự/token cố định, không quan tâm ranh giới ~Free Baselinekhởi điểm +Overlap Chồng lấn N câu/token giữa cácchunk liền kề ~Free Giảm mất ngữ cảnh tại điểmcắt Recursive character splitting Thử tách theo\n\n → \n → space → ký tự, đệ quy khi vẫnquá dài ~Free Gần như luôn thắng fixed-size, chuẩn mặc định Structure-aware Cắt theo heading, section, bảng,code block ~Free–cheap Tài liệu có cấu trúc rõ (docs,FAQ,policy) Semantic (break- point) Embedtừngcâu,cắttạiđiểm cosinesimilarity giảm mạnh 1 lượt em- bed/câu Chỉ khi đã đo thấy gap thật(xem myth kế tiếp) Càng lên cao chi phí càng tăng — chỉ leo khi đã đo được một gap retrieval thật Giảngviên (VinUni) AICB· Ngày 7 Tuần1 36 / 79

---

<!-- chiron-source-span: {"source_span_id":"9f61dfd5-7fef-5f8f-afbd-d814a67bbe7c","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Myth: Semantic Chunking LuônTốt Hơn","extraction_method":"pdf-text-layer"},"checksum":"fca3da7b1e1507c013c6b07b16963ddd61692e2e4d98652833331c577d43b568"} -->

## Slide 45 - Myth: Semantic Chunking LuônTốt Hơn

Nhiềututorial RAG coi semantic (embedding-breakpoint)chunking là upgradetự động sovới fixed-size. Lưuý: Qu,Tu&Bao(Vectara/UW-Madison/Penn), Is Semantic Chunking Worth the Com- putational Cost?,arXiv:2410.13070, NAACL2025Findings: chiphítínhtoán“ notjustified by consistent performance gains” — trên document retrieval, evidence retrieval, retrieval- basedQA.

- Consố “semantic chunking 87% vsfixed-token 50%” (một “clinical study”)khôngtồn tại
trongnguồn nào—đừng dùng.

- Consố “chậm hơn∼14×”là benchmark throughput củaChonkie,không phải từ paper —
ghiđúng nguồn. Nguồn Qu et al., NAACL 2025 Findings (2025.findings-naacl.114) — nhãn “Vectara 2024” và “Qu 2025”là cùng một paper bịđếm hai lần. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 37 / 79

---

<!-- chiron-source-span: {"source_span_id":"f35c5e14-e854-5ef0-9361-cfe2a8166f33","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"Frontier: Hai Cách NghĩLại Về Chunking","extraction_method":"pdf-text-layer"},"checksum":"a69d736ea4f5c4c7906d751ab77bef600cf535c4d4fdfec2ea729829f23404ac"} -->

## Slide 46 - Frontier: Hai Cách NghĩLại Về Chunking

LateChunking (Jina, 2024) Đảongượcthứtự: embed toànvănbản bằng long-context model trước, chunkngay trước meanpooling.

- Chunkvector vẫn giữ ngữ cảnhtoàn tài
liệu(vd. resolve pronounxuyên ranh giớichunk).

- Khôngcần fine-tune riêng, chạy vớibất
kỳlong-context embedder nào. arXiv:2409.04701 (Günther et al.) Phụ thuộc mean pooling — Jina v5 đổi sang last- token pooling nên mất khả năng này. Contextual Retrieval (Anthropic, 2024) Prepend 50–100 token ngữ cảnh do LLM sinh vào mỗi chunk, trước khi embed và index BM25.

- Top-20failure rate: 5.7% (baseline)→
3.7%( −35%,+contextual embed) → 2.9%( −49%,+BM25) →1.9%( −67%, +rerank).

- Chiphí: $1.02/triệu tokentài liệu
(promptcaching). Lưu ý: eval riêng của Anthropic (vendor). Reproduc- tion độc lập (Merola & Singh, ECIR 2025): NDCG@5 0.317 vs 0.312 — thật nhưng nhỏ hơn nhiều so với 49%. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 38 / 79

---

<!-- chiron-source-span: {"source_span_id":"ff96e2b9-dbb7-5023-bbd7-7e149fc32534","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"SilentTruncation— Gotcha NguyHiểm Nhất","extraction_method":"pdf-text-layer"},"checksum":"9a0261b9290c078f1bd79ba28c95070fcdaab771c10c721e055d13820ab24731"} -->

## Slide 47 - SilentTruncation— Gotcha NguyHiểm Nhất

Model Maxinput NomicEmbed Textv2 MoE 512 mxbai-embed-large ∼512 EmbeddingGemma 2,048 gemini-embedding-001 2,048 BGE-M3 / Arctic-Embed 2.0 / nomic-embed-text- v1.5/ Jina v2–v3 8,192 Qwen3-Embedding(0.6B / 4B / 8B) 32,768(cả 3 size) jina-embeddings-v5-text 32K CohereEmbed v4 128K Lưu ý:Text vượtmax_seq_len bị cắtâm thầmbởi hầu hết client library — không raise lỗi. Không có bản Qwen3- Embedding40K; model card ghi rõ32K cho cả ba size. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 39 / 79

---

<!-- chiron-source-span: {"source_span_id":"7ce20ddb-034a-50c7-9696-c6792c151619","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"FailureDemo: Chunk Xấuvs Chunk Tốt","extraction_method":"pdf-text-layer"},"checksum":"e39b4efb165e6da1f9054a6f8c394bc0136535279451a6435cc87950ba0073a8"} -->

## Slide 48 - FailureDemo: Chunk Xấuvs Chunk Tốt

Chunkxấu (raw,không section) Query: “Chính sách đổi trả áp dụng trong bao lâu?” Retrieved(cosine0.61): “…giaohàngmiễnphí đơn trên 500k. Đổi trả trong 30 ngày. Liên hệ hotline1900…” LLManswer: “Bạncóthểđổitrảvàliênhệhot- line1900…” — nhiễu, thiếu chi tiết Chunktốt(theosection+metadata) Query: “Chính sách đổi trả áp dụng trong bao lâu?”

### Retrieved (cosine 0.89): “Chính sách đổi trả
khách hàng có 30 ngày kể từ ngày nhận hàng đểyêucầuđổitrả. Sảnphẩmphảicònnguyên tem.” LLM answer: “30 ngày kể từ ngày nhận, sản phẩm còn nguyên tem.” — chính xác, có nguồn Giảngviên (VinUni) AICB· Ngày 7 Tuần1 40 / 79

---

<!-- chiron-source-span: {"source_span_id":"57fa5b96-c0ec-5801-99ea-15dfc3c0dbd4","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Bên Trong Vector Store: Thuật","extraction_method":"pdf-text-layer"},"checksum":"f0460febee5ec31a7ad96b117a141ff03c8a0ce37806da7bf4dc647c9e3fa555"} -->

## Slide 49 - Bên Trong Vector Store: Thuật

07 Toán ANN Vector store không “tìm kiếm ma thuật” — nó đánh đổi recall, la- tency và memory theo những cách rất cụ thể

---

<!-- chiron-source-span: {"source_span_id":"f4005613-5143-5b22-a6f9-4c53d74bc5a5","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"VìSao Exact Nearest Neighbour KhôngScale?","extraction_method":"pdf-text-layer"},"checksum":"302a78c8502459c0d545f7f39fe19c92b619126bd659a42c390aef912fe2559d"} -->

## Slide 50 - VìSao Exact Nearest Neighbour KhôngScale?

Mỗirecordlưu id+ vector+ document+ metadata—phầncònlạicủasectionnàychỉthayđổiCỘT vector. Exactk-NN: O(N · d)mỗiquery — vớiN=10triệu, d=1536: ~15tỷ phépnhân–cộng cho MỘTquery. Recall Tìm đúng láng giềng thật hay không Latency Trả lời trong bao lâu Memory Index chiếm bao nhiêu RAM/disk Nguyênlý xuyên suốt section Mọi kỹ thuật ANN chỉ là một cáchkhông nhìn hết corpus. Mỗi index tiêu một trong bađồng tiền trên để mua đồngtiền còn lại — không indexnào thắng cả ba. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 41 / 79

---

<!-- chiron-source-span: {"source_span_id":"7a36295f-c020-5431-9ee7-e7ed7267ef93","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"Flat(Brute Force) — Baseline BắtBuộc Phải Đo","extraction_method":"pdf-text-layer"},"checksum":"cde9c686855381db739bc53c070f475f1c555b8db86a31c2d3f34199bb8a7ef3"} -->

## Slide 51 - Flat(Brute Force) — Baseline BắtBuộc Phải Đo

- Cơchế: lưumọi vector nguyên bản (uncompressed);tính khoảng cách tới TẤT CẢ;sắp
xếp. FAISS:IndexFlatL2 / IndexFlatIP.

- Recall: 100% theo địnhnghĩa—đây làgroundtruth đểđo recall của mọi indexkhác.

- Memory: N × d × 4bytes(float32). N=10M, d=1536 ⇒~61.4GB.

- Khinàodùngthẳng: corpusnhỏ(khoảngvàinghìndocumenttrởxuống)—FlattrongRAM
đãđủ nhanh, một vector DBlúc này là over-engineering. Lưu ý:Luôn build Flat trước tiên trong lab. Không có ground truth thì “recall” là một từ vô nghĩa. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 42 / 79

---

<!-- chiron-source-span: {"source_span_id":"5a4ef2a5-9c4a-5e7d-b1fb-62cdcc8883ae","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"IVF— Inverted File / CoarseQuantization","extraction_method":"pdf-text-layer"},"checksum":"a712f9b947ddf660a02c875c5d3fd7a97987f6e8ec24a52ca8e140647d561dd6"} -->

## Slide 52 - IVF— Inverted File / CoarseQuantization

- Cơchế: k-meanschia corpus thànhnlistcell(Voronoipartition). Query: tìm nprobe
centroidgần nhất, chỉ scan vectortrong các cell đó.

- Analogy: sơđồtầngthưviện—tìmđúngkhukệtrước,rồimớiđọcsáchtrênkhuđó. Flat=
đọchết cả thư viện.

- nprobelànúm vặn recall:nprobe ↑ ⇒ scannhiều cell hơn⇒recall ↑,latency ↑. Một cấu
hìnhcụ thể (Pinecone,IVF256,PQ32x8): nprobe=1→30%recall @ 136µs; nprobe=8→ 74%recall @ 729µs.

- Bắtbuộc train: IVFcần một passtrain()trênsample đại diện để họccentroid —
Chroma/pgvectorgiấu bước này,FAISSthô thì không. Lưu ý: “Dùng nprobe = 8–16 cho 1–10M vector” không có trong docs FAISS hay bài Pinecone. Bài học thật:tăng nprobe đến khi recall bão hoàso với Flat ground truth — khôngcó công thức. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 43 / 79

---

<!-- chiron-source-span: {"source_span_id":"b8eb990b-c486-59f7-a477-7e4fd8af836d","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"PQ— Product Quantization: Phép ToánBộ Nhớ","extraction_method":"pdf-text-layer"},"checksum":"95acb072cfed358c78ea399803eb75060bc734ca96ffc76cd3c898a20d5c8c37"} -->

## Slide 53 - PQ— Product Quantization: Phép ToánBộ Nhớ

Cơchế: chiamỗi vector thànhMsub-vector;k-means riêng từng subspace thànhcodebook riêng;chỉ lưuchỉsố centroidmỗisubspace. Khoảng cáchước lượng qua bảng tra sẵn(ADC). Bước Kíchthước 128-dimfloat32 (gốc) 512bytes 8subspace ×16-dim,mã 8-bit (256 centroid) 8bytes Tỷlệ nén 64× Trade-offthật (không đơn điệu)— và OPQ M lớn hơn giữ độ chính xác tốt hơn nhưng ăn mòn CẢ tỷ lệ nén LẪN tốc độ cộng khoảng cách — “M càng lớn càngtốt”làsai. OPQ(OptimizedPQ): họcmộtmatrậnxoaytrựcgiao,ápdụngTRƯỚCkhichiasubspace,đểcân bằng phương sai giữa subspace (trục chia PQ vốn tuỳ ý — sai với chiều tương quan). Chi phí: một phép nhân ma trận/vector, rẻ so với recall thu được. FAISS: tiền tốOPQ<M>_<d> trước chuỗi PQ/IVFPQ. Không có con số cải thiện đángtin cậy — chỉ “thườngtốt hơn ở cùng kích thướcmã”. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 44 / 79

---

<!-- chiron-source-span: {"source_span_id":"d9a5d57c-99a4-5e48-a434-363c1740ff15","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"HNSW— Graph Nhiều Lớp ĐằngSau Hầu Hết VectorDB","extraction_method":"pdf-text-layer"},"checksum":"ffc9891452266b3d63494a2ff561b9cb3edfc4b6611a083793db834fb4edbfd3"} -->

## Slide 54 - HNSW— Graph Nhiều Lớp ĐằngSau Hầu Hết VectorDB

- Cơchế: multi-layerproximity graph. Lớptrên thưa (bước nhảy xa), lớpdưới dày (chi tiết);
lớpđáy chứa toàn bộ điểm. Tìm kiếm greedy đitừ đỉnh xuống đáy.

- Analogy: hệthống cao tốc — vàođường cao tốc (lớp thưa trênđỉnh), ra nhánh nhỏ dần
(lớpdày) khi tới gần đích.

- Aidùng: FAISS IndexHNSWFlat,hnswlib(chính là index nền củaChromaDB),Qdrant,
Weaviate,Milvus, pgvector hnsw. Thamsố Ảnhhưởng khi tăng Giá trị thường gặp M memory ↑, kết nối đồ thị↑, recall ↑ 16 efConstruction thời gian build↑, chất lượng đồ thị ↑ 200 efSearch latency ↑,recall ↑ tuỳSLA Giảngviên (VinUni) AICB· Ngày 7 Tuần1 45 / 79

---

<!-- chiron-source-span: {"source_span_id":"2e1ad96c-a10d-506e-bbda-de60141a85cf","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"Recallvs Latency vs Memory —So Sánh Các Họ Index","extraction_method":"pdf-text-layer"},"checksum":"7a59b934392db06886efd8d9fa959b24208f8737c0930629fc4b5e87a28c388c"} -->

## Slide 55 - Recallvs Latency vs Memory —So Sánh Các Họ Index

Index Recall Latency Memory/vector (d=1536) Bestcho Flat 100%(ground truth) O(N·d) — chậm nhất 6,144B <10k doc; đo recall của mọiindex khác IVF-Flat tune qua nprobe (vd. 30%→74%) µs–ms 6,144B + list overhead mid-scale,RAM đủ IVF-PQ lossy,phụ thuộc config nhanhnhất/vector vàichụcbyte(nén64 ×) tỷ vector,RAM hạn chế HNSW-Flat ~95–99%(M/efSearchhợp lý) ms đơn vị ở scale 1M 6,144B + 256 B graph recall/latencytốtnhấtkhi RAMđủ,khôngcầntrain DiskANN/Vamana 95%+ recall@1 <3ms, >5000 QPS PQ trong RAM + full vectortrên SSD tỷvector trên 1 máy ScaNN tốt hơn PQ thường, cùng codesize — cỡPQ MIPS,Google stack Quantize (int8/binary) +rescore ~lossless/ ~96% giữ lại int MAC / XOR+popcount 4×hoặc32 ×nhỏhơn production tối ưu chi phí Số liệu lấy từ các nguồn được trích tại mỗi cấu hình cụ thể — so sánh giữa các hàng mang tính minh hoạ, không phải benchmark có kiểm soát Giảngviên (VinUni) AICB· Ngày 7 Tuần1 46 / 79

---

<!-- chiron-source-span: {"source_span_id":"f727bfde-563f-50b9-9d55-17e84d513220","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"Cheatsheet: Chỉnh Tham SốANN (Lưu Lại Slide Này)","extraction_method":"pdf-text-layer"},"checksum":"e882603bfb8215430441123317b3577c5ffa08ea3c2dd6bf0f215b9cfdcbd237"} -->

## Slide 56 - Cheatsheet: Chỉnh Tham SốANN (Lưu Lại Slide Này)

1. BuildFlat trước. Khôngcó ground truth thì khôngthể nói từ “recall”.

2. Chọnhọ index theo ràng buộcchính:RAMdư, ≤10Mvector →HNSW.RAM là điểm nghẽn, ≥100Mvector →IVF-PQhoặcDiskANN. <10kvector →Flat,bỏ luôn vector DB.

3. HNSW:bắtđầu M=16, efConstruction= 200. Chỉ tuneefSearch lúcquery — núm vặn duynhất khôngcần rebuild.

4. IVF: nlist ≈ 4 √ Nlàmđiểmkhởiđầu;sauđó tăngnprobeđếnkhirecallbãohoà sovớiFlat. Không cócông thức.

5. PQ: Mphảichia hết d. Bắt đầu vớimã 8-bit. Nhớ điểmngọt —Mlớnhơn không luôn tốt hơn.

6. Quantizesau cùng, luôn kèm rescoring.int8là mặc định an toàn;binary chỉ khid ≥ 1024.

7. Đođúng thứ bạn quan tâm:recall@kso với Flat, ởkthật,với filter thật đang dùng. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 47 / 79

---

<!-- chiron-source-span: {"source_span_id":"4741f70f-c0dc-5aca-8ecb-d23b48bebc54","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"FAISS, ChromaDB & Landscape","extraction_method":"pdf-text-layer"},"checksum":"c7d2a6c24b4252dd1060368debc9e924e4d67041c1f5546d6823bcd3f9c52f32"} -->

## Slide 57 - FAISS, ChromaDB & Landscape

08 2026 FAISS là engine tốc độ, Chroma là developer experience — nhưng landscape 2026 rộng hơn nhiều hai cái tên quen thuộc đó

---

<!-- chiron-source-span: {"source_span_id":"78678242-098b-581d-a9a5-84186294d876","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"FAISSLà Một Library,Không Phải Database","extraction_method":"pdf-text-layer"},"checksum":"0d6799e0de336bd1c1edad37fd72ca821ff1960a2fd4b2cc89d9968fda9902e6"} -->

## Slide 58 - FAISSLà Một Library,Không Phải Database

- ✓ Làindex+ search kerneltốiưu tốc độ và memory —không hơn.

- Khôngcó persistence ngoàiwrite_index/read_index rafile.

- Khôngcó metadata schema, không cówherefiltertích hợp sẵn.

- Khôngcó CRUD/transaction, không multi-tenancy,không access control.

- IndexHNSWFlat không hỗ trợremove_ids() — raise lỗi, kể cả khi wrap thành
IDMap2,HNSW32,Flat.

- ✓ Ngượclại, họ IVF(IVFFlat, IVFPQ)cóhỗtrợ remove_ids trựctiếp.
Nguồn: FAISS wiki “Guidelines to choose an index”; GitHub issue #3339. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 48 / 79

---

<!-- chiron-source-span: {"source_span_id":"fc945180-1a9c-56ad-9bf4-e92a6024164a","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"Bug#1 Của FAISS:CosineSimilarity","extraction_method":"pdf-text-layer"},"checksum":"cd19f79b70be0d1a69d57c445b59c9262cce6c79670d411b9339ef7f2dc18456"} -->

## Slide 59 - Bug#1 Của FAISS:CosineSimilarity

Lưu ý: FAISS không có METRIC_COSINE. Chỉ có METRIC_L2 và METRIC_INNER_PRODUCT. Cosine phải được giả lập bằng cách normalize vector trướckhi dùng inner product. faiss.normalize_L2(vectors) # in-place, before index.add -- half 1 of 2 index = faiss.IndexFlatIP(d) index = faiss.IndexIDMap(index) # map back to chunk ids index.add_with_ids(vectors, ids) faiss.normalize_L2(query) # ALSO before search -- the forgotten half D, I = index.search(query, k) Quênnormalize khôngraise lỗi. Nó lặng lẽsuy biến thành xếp hạng theodot-product thô — ưu tiênvector dài hơn. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 49 / 79

---

<!-- chiron-source-span: {"source_span_id":"bfd665ef-522d-5f08-b0b0-9419ec1dc099","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"ChromaDB:Kiến TrúcHiện Tại","extraction_method":"pdf-text-layer"},"checksum":"bc819109ae1497502280f5f04a0968f820f632f71ec52636921ebfb8556ceeaf"} -->

## Slide 60 - ChromaDB:Kiến TrúcHiện Tại

Embedded(local)

- PersistentClient chạytrong
processcủa bạn, ghi thẳng ra đĩa.

- Rustcore từv1.0 (1/3/2025) —
“4×”nhanh hơn cho write/query phổbiến.

- Indexdùng hnswlib(HNSW)
bêndưới.

- Metadatalưu trongSQLite(từ
v0.4.0,7/2023). ChromaCloud

- Táchstoragekhỏiquery
execution.

- Write-aheadlog + indexed state

- đọcstrongly consistent.

- Dùngchung Rust core 1.0 làm
nềntảng local và cloud. Bản hiện hành: chromadb 1.5.9 (5/5/2026). Giảngviên (VinUni) AICB· Ngày 7 Tuần1 50 / 79

---

<!-- chiron-source-span: {"source_span_id":"465d8e24-7a0e-58ea-8cc3-24570d84b8db","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"“DefaultLà Một Cái Bẫy”","extraction_method":"pdf-text-layer"},"checksum":"32c5a9fb1847dea4b6a64983ee9714a0f2a61ad110251e832d2be0f733a5a6db"} -->

## Slide 61 - “DefaultLà Một Cái Bẫy”

Default embedding function của Chroma — sentence-transformers all-MiniLM-L6-v2,384 chiều, chạy local qua ONNX,không cần API key.

- Truncateở 256 word-piece, nhỏ, nhanh,thiên về tiếng Anh — xamức frontier.

- Vìchạyngay không cần config,team thường ship thẳng lên productionmà không
nhậnra.

- Kếtquả: recall kém,và không ai giải thích đượctại sao.
Lưu ý:Bug thường gặp nhất trong Chroma: tạo collection vớiembedding_function riêng,sauđógọi get_collection()màkhôngtruyềnlạinó—default384chiềuâm thầmthế chỗ. Luôntruyền cùngembedding_function mỗilần. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 51 / 79

---

<!-- chiron-source-span: {"source_span_id":"e363d417-1414-592c-84e1-802d433918ea","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Chroma: Flow Đầy Đủ2026 — Add + Query +Inject","extraction_method":"pdf-text-layer"},"checksum":"8a50a0a5d7ddf0a095bf10913989ba97399c639f195121194a94fe40aff3751e"} -->

## Slide 62 - Chroma: Flow Đầy Đủ2026 — Add + Query +Inject

```text
import chromadb
from chromadb.utils import embedding_functions
client = chromadb.PersistentClient(path= "./chroma_db") # durable immediately
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
model_name= "BAAI/bge-m3") # EXPLICIT, never the default
col = client.get_or_create_collection( "tickets", embedding_function=ef)
col.add(ids=[...], documents=[...], metadatas=[...])
res = col.query(
query_texts=[ "package never showed up"], n_results=5,
where={ "team": { "$eq": "support"}},
where_document={ "$contains": "E-4471"},
)
context = "\n".join(res["documents"][0]) # inject into the prompt
Giảngviên (VinUni) AICB· Ngày 7 Tuần1 52 / 79
```

---

<!-- chiron-source-span: {"source_span_id":"8a7743c0-fb05-5e48-9e3b-6681decee940","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"ChọnVectorStore Nào?","extraction_method":"pdf-text-layer"},"checksum":"c45da725d14e5cf1659e580171770c841c034da4058f7938c387ec8f153a24cc"} -->

## Slide 63 - ChọnVectorStore Nào?

1. Dưới10k vector,single process,không có ops budget→FAISSFlat in RAMhoặcChroma PersistentClient. Sub-ms. Bỏ qua vectorDB.

2. ĐãdùngPostgres,dướikhoảng10Mvector,indexfitRAM →pgvector. Mộthệthống,metadatatransactionalmiễn phí.

3. Postgres,từ 10M đến hàng trămtriệu→pgvectorscale(StreamingDiskANN),disk-resident, label-aware filtering.

4. Cầnfilter phức tạp mà khôngđược mất recall, hoặc ColBERT/ColPalimulti-vector,hoặc per-tenant isolation là first-class →QdranthoặcWeaviate.

5. Corpusđã nằm trong lakehouse (Iceberg/Lance/Parquet),không muốn ETL ra ngoài→Milvus3.0 External Collection—nhưng vẫn Public Preview,chưa GA.

6. Workloadbursty/idle nhiều, cost là ưutiên số 1, chấp nhận cold-start→turbopufferhoặcAWSS3 Vectors.

7. Dạyhọc / prototype / labcủa khoá này→ChromaDB(embedded,zero-config, có hybrid BM25+SPLADE) +FAISS (đểthấy index internals mà Chromagiấu đi). Lưu ý: Hai cạm bẫy của đường Postgres:MVCC bloat(mỗi UPDATE là delete+insert — nặng khi re-embed) và không có filter pushdownvào graph traversal (§9). Ngưỡng rời Postgres không phải số vector, mà làlúc index khôngcòn fit RAM. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 53 / 79

---

<!-- chiron-source-span: {"source_span_id":"75552703-a56f-5b7f-90ac-c39eadc23360","locator":{"kind":"page","page":64,"label":"Slide 64","section_title":"Metadata Filtering & Hybrid","extraction_method":"pdf-text-layer"},"checksum":"454f84220ece75c640ff70f452e240839b106a171f9ac6e6e2e7fd539ebbacc5"} -->

## Slide 64 - Metadata Filtering & Hybrid

09 Search Similarity thôi chưa đủ: filter đặt sai chỗ làm sập recall trong im lặng, và một số truy vấn chỉ BM25 mới giải được

---

<!-- chiron-source-span: {"source_span_id":"1a3da951-5e82-5cb5-9565-cadc14194465","locator":{"kind":"page","page":65,"label":"Slide 65","section_title":"FilterLàm Sập Recall — TrongIm Lặng","extraction_method":"pdf-text-layer"},"checksum":"56d699bf125b6adf852c0f4b0ceb2c0e55cf832c7d2139b37596a09a59a6e625"} -->

## Slide 65 - FilterLàm Sập Recall — TrongIm Lặng

Bachiến lược áp filter,ba cơ chế thất bại khácnhau — và cái sai chỉlộ ra khi filter thật (per-tenant,per-permission) lên

### production,khôngphải trong demo
Chiếnlược Cơchế Thấtbại Post-filter ANNtrêntoàncorpus,rồiloạibỏ chunkkhông khớp Mất recall âm thầm: có thể trả về <k hoặc 0 kết quả nếu filter chọn lọc Pre-filter Thu hẹp tập con khớp filter, searchtrong đó Đúng, nhưng suy biến về brute- force; đồ thị HNSW xây cho toàn corpusphụcvụkémtrênsubgraph nhỏ In-algorithm Traversalcủaindextựnhậnbiết filter Tốt nhất, nhưng cần engine hỗ trợ (Qdrant payload-aware HNSW, Weaviate ACORN, Pinecone mergedindex) Lưuý: Trênpgvector0.8.0-pg17: truyvấn15nearestneighbourmàu greenchỉtrảvề 11dòng —khôngexception, khônglog. Cơ chếvá hnsw.iterative_scan đãtồn tại từ 0.8.0 nhưngmặcđịnh TẮT. Nguồn: Franck Pachot (dev.to, pgvector 0.8.0-pg17) · ACORN, Patel et al., SIGMOD 2024, arXiv:2403.04871. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 54 / 79

---

<!-- chiron-source-span: {"source_span_id":"6b9ca93e-dad2-5a13-8e45-c28cae15b59a","locator":{"kind":"page","page":66,"label":"Slide 66","section_title":"Chroma— Cú Pháp Filter (Verbatim,Không Bịa)","extraction_method":"pdf-text-layer"},"checksum":"4d8f4f929e64bb2130a1b8daeb1b975051282210def6376428e72961c1de3a37"} -->

## Slide 66 - Chroma— Cú Pháp Filter (Verbatim,Không Bịa)

collection.query( query_texts=[ "shipment did not arrive"], n_results=5, where={ "$and": [ {"source": { "$eq": "tickets"}}, {"page": { "$gt": 5}}, ]}, where_document={ "$contains": "E-4471"}, )

- where(metadata): sosánh $eq $ne $gt $gte $lt $lte ·logic $and $or ·tậphợp $in $nin.
{"page": 10} là sugarcho $eq.

- where_document (full-text): $contains $not_contains $regex $not_regex —
case-sensitive.

- Dễnhầm: $contains/$not_contains cũngtồn tại bên trongwherenhưtoán tử array(kiểm
tra1 giá trị có nằmtrong metadata dạng list) — kháchoàn toàn với$contains full-textcủa where_document. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 55 / 79

---

<!-- chiron-source-span: {"source_span_id":"9685685c-e4f4-5d5e-b3eb-de0b7701ad9c","locator":{"kind":"page","page":67,"label":"Slide 67","section_title":"5TruyVấn, Một CorpusSupport Ticket","extraction_method":"pdf-text-layer"},"checksum":"1df1da0660ba5ee60ea4a7bc72b23bcc2418ff3281155b6402991f0475b53d0f"} -->

## Slide 67 - 5TruyVấn, Một CorpusSupport Ticket

Truyvấn Thắng Vìsao “mypackage never showed up” Dense doc ghi “shipment did not arrive” — khôngtrùng từ nào “canI get my money back” Dense doc ghi “refund policy for returned merchandise” “the app crashes when I open set- tings” Dense docghi“applicationterminatesunex- pectedlyin the preferences pane” “errorcode E-4471” BM25 densetrảvềmãtươngtựnhưng SAI “SKUVN-2291-XL” BM25 token ngoài từ vựng huấn luyện — chỉinverted index tìm ra Điểmchốt Truy vấn 1–3: xây dense index. Truy vấn 4–5: giữ BM25 — đó là lý do hybrid search tồn tại, và vì sao RRF (fuse theorank,không phải score) là cáchkết hợp đúng. BEIR: “BM25 is a robust baseline” — Thakur et al., arXiv:2104.08663 Giảngviên (VinUni) AICB· Ngày 7 Tuần1 56 / 79

---

<!-- chiron-source-span: {"source_span_id":"91704982-9bd0-5c67-8ab7-c389a610adc4","locator":{"kind":"page","page":68,"label":"Slide 68","section_title":"HybridSearch: BM25 +Dense, SPLADE, và BGE-M3","extraction_method":"pdf-text-layer"},"checksum":"958d45d99f6f3168da1bcbfa1b8dc74301556b7b48c43a1647c37efcf7e75db9"} -->

## Slide 68 - HybridSearch: BM25 +Dense, SPLADE, và BGE-M3

- Densethắng vocabulary mismatch: “package never showedup”↔“shipmentdid not arrive”.

- Lexical(BM25) thắng token chính xác: mã lỗi, SKU,tên riêng — embedding học cách“làm mờ” đúng những thứ
này.

- SPLADE(learnedsparse): sparse vectortrên vocabulary BERT(∼30,522token) — nhưng cần forwardpass
transformerở cảindex-timelẫn query-time (thêm∼100–300mslatency), và vẫn không phủđược token ngoài tập huấnluyện — vì vậy BM25vẫn giữ chỗ năm 2026.

- BGE-M3(BAAI,arXiv:2402.03216): một modelxuất cùnglúc dense+ sparse + multi-vector,huấn luyện bằng
self-knowledgedistillation—scorecủa3modelàmtínhiệuteacherchonhau. 100+ngônngữ,inputtới8,192token.

- Vậy“hybrid chỉ là 3 hệthống ghép lại” còn đúng không? Ở SOTA(BGE-M3),không còn đúng nữa.
Giảngviên (VinUni) AICB· Ngày 7 Tuần1 57 / 79

---

<!-- chiron-source-span: {"source_span_id":"bfb2240d-e03f-5eb2-bbbf-62947ef4d6c2","locator":{"kind":"page","page":69,"label":"Slide 69","section_title":"RRF— Reciprocal Rank Fusion","extraction_method":"pdf-text-layer"},"checksum":"15e9ae318e0e73c3cab32d00beb1c094e199e2fb81342bf84d7a0fce9f3a4bdc"} -->

## Slide 69 - RRF— Reciprocal Rank Fusion

RRF(d) = X r∈R 1 k +rankr(d), k = 60 (mặcđịnh)

- Fusetheo vịtrí rank,không theo score thô — nébài toán chuẩn hóa score chéohệ
(BM25và cosine không cùng thang đo).

- Hỗtrợ native: Elasticsearch (rrfretriever) ·OpenSearch(hybrid pipeline) ·
Weaviate(mặc định) ·Qdrant( Fusion.RRF) ·ChromaDB.

- k = 60: mặc định papergốc (Cormack et al.), cũng làmặc định Elastic/OpenSearch.
Lưu ý:“Hybrid tăng accuracy 26–31% so với dense-only” — số này chỉ xuất hiện trong blog vendor,không kèm benchmark hay dataset nào. Bỏ số này. Dùng kết luận BEIR: BM25 là baseline mạnh ngoài miền huấn luyện; kết hợp các họ retrieval muađược robustness,không phải một% cố định. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 58 / 79

---

<!-- chiron-source-span: {"source_span_id":"9db126cd-68d8-5a70-93b0-fef427431a69","locator":{"kind":"page","page":70,"label":"Slide 70","section_title":"Frontier 2025–2026","extraction_method":"pdf-text-layer"},"checksum":"74ea7698bfb9dba6352c613a32e2b4246a5d9411223006635a739626974b6a66"} -->

## Slide 70 - Frontier 2025–2026

10 Reranking, long-context vs RAG — và vì sao retrieval chỉ là một tool trong context engineering

---

<!-- chiron-source-span: {"source_span_id":"e641b77b-a64d-5684-8fbf-81adbea4aae3","locator":{"kind":"page","page":71,"label":"Slide 71","section_title":"Reranking— Nâng Cấp ROI CaoNhất","extraction_method":"pdf-text-layer"},"checksum":"1f333629234baacede2a0326c6dbe5788613e7fc05bc44ad219de1ae75e56912"} -->

## Slide 71 - Reranking— Nâng Cấp ROI CaoNhất

- Bi-encoder(hoặc BM25) lấy top-50/100 rẻ;cross-encodermãhóa đồng thời
query+passage,rerank xuống top-5/10 thực sự đưavào prompt.

- Chiphí: O(k)forwardpass trên shortlist,khôngphụ thuộckíchthước corpus N—
indextăng lên hàng triệu tài liệumà không đổi hoá đơn reranker.

- Bấtđối xứng: embeddinglà chi phímộtlần mỗitài liệu; reranking là chi phílặplại
mỗitruy vấn.

- Modelđáng chú ý: BGE-reranker-v2-m3 (open, multilingual, tự host nhẹ)·Cohere
Rerankv3.5(hosted) ·jina-reranker-v3—listwise,chỉ0.6Bthamsốtrênbackbone Qwen3-0.6B,xử lý tới 64 tài liệutrong context 131K token, 61.94 nDCG@10trên BEIR(arXiv:2509.25085).

- Điểmdạy: một modellistwise vỏn vẹn 0.6B tham sốcạnh tranh được làm câu
chuyện“listwise thắng pointwise” thuyết phục hơnhẳn một con số nDCG đơnlẻ. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 59 / 79

---

<!-- chiron-source-span: {"source_span_id":"25bf914e-3f91-58b9-871d-1f83fd3a44e8","locator":{"kind":"page","page":72,"label":"Slide 72","section_title":"HuyềnThoại: “Long ContextĐã Giết Chết RAG”","extraction_method":"pdf-text-layer"},"checksum":"22f3c351428e58d62b4c1e2076e66111754277be88aa7fe8f9d6fe1229e1e43c"} -->

## Slide 72 - HuyềnThoại: “Long ContextĐã Giết Chết RAG”

Lưu ý:Nhiều bài viết 2025–26 tựa đề thẳng “RAG is dead.” Bằng chứng kiểm soát khôngủnghộ. Bằngchứng Pháthiện ContextRot(Chroma, 7/2025) Hiệunănggiảmphituyếnkhiinputdàira,kểcảtácvụđơn giản. arXiv:2501.01880 Long contextthắngRAG hầu hết QA (đặc biệt Wikipedia); RAG thắng hội thoại. Summarization-retrieval tiệm cận long-context;chunk thô thua. Lost in the Middle (2307.03172) Chính xác hình chữ U — tệ nhất ở giữa. Tăngk không rerankcó thểtệhơn. CAG (2412.15605, WWW’25) Nạp toàn corpus, KV-cachemột lần— nhưng phảivừa contextwindow. Tổnghợp 2026 Vector retrieval thu hẹp corpus lớn, giao tập con cho long-context model suy luận (đồng thuận thực hành, không phảikết luận 2501.01880). Giảngviên (VinUni) AICB· Ngày 7 Tuần1 60 / 79

---

<!-- chiron-source-span: {"source_span_id":"96395c9a-482b-5762-98ca-80b5230a53c1","locator":{"kind":"page","page":73,"label":"Slide 73","section_title":"Capstone: Retrieval Là MộtTool— Và Day 8Đi TiếpTừ Đây","extraction_method":"pdf-text-layer"},"checksum":"129cc69a68693c594e5d6ca26c9af028781d03af4a3c0dda28f9a3152bbc9d8b"} -->

## Slide 73 - Capstone: Retrieval Là MộtTool— Và Day 8Đi TiếpTừ Đây

Contextengineering — Anthropic, 29/9/2025 “Chiếnlược chọn lọc và duytrìbộtoken tối ưutrongcontext khi LLM inference.”

- Just-in-timecontext loading: agent giữ địnhdanh nhẹ (đường dẫn, query đãlưu) và nạp
dữliệu lúcchạy quatool. Retrieval làmộtđòn bẩy,không phải toàn bộ kiếntrúc.

- Day8 (RAG)nhậntiếp từ ranh giới “top-kchunkđã chọn”: lateinteraction
(ColBERTv2/PLAID),query rewriting & agentic retrieval(Self-RAG, CRAG), GraphRAG, promptassembly & citation UX.

- Day9 (MCP):server expose corpus như mộttool chuẩn hoá — agent tựquyết định khi nào
gọiretrieval. Ranhgiới Day7= đưadữliệuvàođúnghìnhdạng. Day8= dùngnóđểtrảlời. Tầngdữliệusaithì khôngkỹ thuật nào ở Day8 cứu được. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 61 / 79

---

<!-- chiron-source-span: {"source_span_id":"28e11e3f-0bff-5edd-bfdc-4bc81d8ff5d2","locator":{"kind":"page","page":74,"label":"Slide 74","section_title":"Đo Lường, Chi Phí & Failure","extraction_method":"pdf-text-layer"},"checksum":"d9b56dd1d2a4352eb2fe62cac1d1c3819958146b7fa44694abc6900058ef4a3f"} -->

## Slide 74 - Đo Lường, Chi Phí & Failure

11 Modes Nếu không đo được recall thì không biết đang tối ưu cái gì — và không lỗi không có nghĩa là đúng

---

<!-- chiron-source-span: {"source_span_id":"125de517-d3d9-5b8b-975e-da087c998546","locator":{"kind":"page","page":75,"label":"Slide 75","section_title":"ĐoRetrieval Quality: Recall@k& BEIR Baseline","extraction_method":"pdf-text-layer"},"checksum":"0a0d0fce847a7454d5585df0007c3516050a6221eef94eb902616e40842276b8"} -->

## Slide 75 - ĐoRetrieval Quality: Recall@k& BEIR Baseline

- Recall@k: bao nhiêu docrelevant nằm trong top-k —upper-boundcho chất lượng câu
trảlời cuối cùng.

- Precision@k: trong top-k, baonhiêu thực sự relevant — kiểmsoát nhiễu, context budget.

- nDCG@k: thứ hạng tốtkhông (log-discount theo vị trí) —phạt đúng passage ở rank 8thay
vìrank 1.

- MRR:vị trí nghịch đảo kếtquả relevant đầu tiên — hợptruy vấn kiểu single-answer.

- Luônthêm BM25 làm sàn: dense model fine-tunetrên MS MARCO có thểthuaBM25 thô
ngoàimiền huấn luyện (BEIR: 18dataset, 9 tác vụ). Nuancehay bị bỏ qua Recall@kcần nhưng chưa đủ. Đúng passage ở rank 18/20 vẫn có thể ra câu trả lời sai — lost-in-the-middle. Recall giới hạn cáicó thể xảy ra; precision/nDCG/reranker quyết định cái thực sự xảy ra. Nguồn: Thakur et al., arXiv:2104.08663 (BEIR). Giảngviên (VinUni) AICB· Ngày 7 Tuần1 62 / 79

---

<!-- chiron-source-span: {"source_span_id":"f844b128-1cfa-54ac-b4fb-644a1ddaea82","locator":{"kind":"page","page":76,"label":"Slide 76","section_title":"CôngThức Làm Eval Set KHÔNGCần Nhãn","extraction_method":"pdf-text-layer"},"checksum":"0bba0c2eec0a2a41a175d0afc2f3cbe2e5859b9e8cdbeb981a53ef0afab53e30"} -->

## Slide 76 - CôngThức Làm Eval Set KHÔNGCần Nhãn

Mụctiêu: đorecall@k trên corpus của chính mình,trong một buổi,khôngcần ai gán nhãntay.

1. Samplechunktheo tỉ lệ giữa các loạitài liệu (N≥100để ước lượng có ý nghĩa).

2. Sinhcâu hỏibằngLLM, chỉ dựa trên đúng chunkđó, kèmpersona(“kháchso gói cước”,“kiểm toán viên nội bộ”).

3. Nhãn: chunknguồn chính là positive — đâylà mẹocitation-as-weak-label.

4. Chạyretrieval,tính recall@k và MRR so vớicác pseudo-label này.

5. Ngườikiểm tra tay∼10%để loại câu hỏi vô nghĩahoặc quá dễ. Lưuý: Haithiênlệchphảinóirõ,khôngthìsinhviêntựtinquámứcvàoconsốcủa mình: (1)câuhỏiLLM-sinhlặplạiđúngtừngữcủachunk—thổiphồngrecall@kso vớingườidùngthật(diễngiảilại,hỏimulti-hop);(2)cáchnàychỉđođược“cótìmlại đúng chunk đã sinh câu hỏi không” — thiên về trùng từ khoá.Đây là floor check, khôngthay thế nhãn thật. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 63 / 79

---

<!-- chiron-source-span: {"source_span_id":"c0db8b4b-2fcc-5b87-9394-ad05bb7ecdbd","locator":{"kind":"page","page":77,"label":"Slide 77","section_title":"ChiPhí Embedding: RẻHơn Sinh ViênTưởng","extraction_method":"pdf-text-layer"},"checksum":"f87ac5610eb35dbe8719e8ee659f10e91227aeae52aff12e8f4e6b32ede63a0c"} -->

## Slide 77 - ChiPhí Embedding: RẻHơn Sinh ViênTưởng

$2 Corpus 100M token,-3-small ($0.02/1M), một lần duy nhất $13 Cùng corpus, -3-large ($0.13/1M token) 100Mtoken ≈75Mtừ — cỡ document storedoanh nghiệp vừa. Rẻhơn generation2–3bậc độ lớn. Hệquả chiến lược Vìrẻ vậy,re-embed toàncorpus khi đổi model làkhảthi —không phải lý do nénâng cấp. Nguồn: developers.openai.com/api/docs/pricing. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 64 / 79

---

<!-- chiron-source-span: {"source_span_id":"618a0781-342c-5ffc-bfdb-9eaaea810d2b","locator":{"kind":"page","page":78,"label":"Slide 78","section_title":"Failure-ModeTable— Retrieval &Embed (1/2)","extraction_method":"pdf-text-layer"},"checksum":"5449e9472948782ede1fd942b3f86fd901982f86f9e737bab296c482bef72de0"} -->

## Slide 78 - Failure-ModeTable— Retrieval &Embed (1/2)

# Triệuchứng Nguyênnhân Cáchsửa Giaiđoạn 1 Query “xe hơi” bỏ sót doc ghi“ô tô” Lệch từ vựng — retrieval lexical thuần Hybrid BM25+dense với RRF,hoặc query expansion Retrieval 2 Query mãE-4471 trả về mã khácnhưnggiống nghĩa Dense embedding làm nhoè to- kenchính xác ThêmnhánhBM25(xửlýtốt tokenOOV) Retrieval 3 Recall thấp hơn kỳ vọng 5– 15%,không lỗi Thiếuprefix query:/passage: của E5/BGE — train-in, không phải cosmetic Áp đúng prefix cả hai phía; chạyprefix-ablation test Embed 4 Chunk dài retrieve kém, đuôi chunk không bao giờ khớp Silent truncation tại max se- quencelength—clientlibraryâm thầmcắt bỏ phần dư Kiểm tra token count trước khi embed; biết giới hạn model Chunk/Embed 5 Ranking nhìn hợp lý nhưng sailệch trên toàn index Đổi embedding model màkhông re-embed — cosine giữa hai khônggianvẫntínhđược,nhưng vônghĩa Re-embed + rebuild index toànbộ; version hoá index Ops 6 FAISSưutiêndocumentdài hơn Quên normalize_L2 — suy biến vềdot product thô Normalize cả lúc add và lúc queryvới IndexFlatIP Store 7 Filtered search trả về ít hơn k,hoặc 0 Post-filteringvới predicate chọn lọc — neighbour đúng chưa từng làcandidate Pre-filter, hoặc in-algorithm filtering Store Mỗi dòng có đặc điểm chung: không crash, không exception Giảngviên (VinUni) AICB· Ngày 7 Tuần1 65 / 79

---

<!-- chiron-source-span: {"source_span_id":"033c90fa-777f-5830-afdf-cc551f6f13e2","locator":{"kind":"page","page":79,"label":"Slide 79","section_title":"Failure-ModeTable— Chunk, Store& Ops (2/2)","extraction_method":"pdf-text-layer"},"checksum":"55a1a953582443c7add7b6c3fb53d3dbd44dca8f172cc7eb8cf669721c92119d"} -->

## Slide 79 - Failure-ModeTable— Chunk, Store& Ops (2/2)

# Triệuchứng Nguyênnhân Cáchsửa Giaiđoạn 8 Chất lượng câu trả lờigiảm khităng k Over-retrieval+lost-in-the-middle — đúng nội dung nhưng bị chôn giữacontext Rerank để đẩy bằng chứng lênđầu; giảm k Retrieve→Gen 9 Recall dao động mạnh giữa cácloại tài liệu Saichunksizecholoạitruyvấn— 64–128tokencâuhỏingắn,512– 1024 ngữ cảnh rộng, tuỳ embed- dingmodel Tinh chỉnh chunk size mỗi khiđổi embedding model Chunk 10 Recall trung bình dai dẳng, “chưađổi gì cả” Chroma default all-MiniLM-L6-v2 âm thầm được dùng (384-dim, cắt 256 word-piece) Truyền embedding_function tường minh;assert chiều vector Embed 11 Query trả về rỗng sau khi restart Lệch embedding function — collectiontạovớifntuỳchỉnh,mở lạibằng default Luôn truyền cùng embedding_function cho get_or_create_collection Store 12 Latency tăng dần giữa các lầncompaction HNSW tombstone— vector đã xoámềmvẫnchiếmbộnhớvàbị duyệtqua rồi lọc Lênlịchcompaction/rebuild định kỳ; dùng IVF nếu xoá thườngxuyên Ops 13 Cachetrảlờisaimộtcách tự tin Cache key không version theo embedding model, hoặc thiếu TTL Version cache key; TTL theođộ biến động của fact Ops 14 Demo tốt, production tệ Eval tổng hợp overfit cách diễn đạtcủanguồn—ngườidùngthật diễngiải lại, hỏi multi-hop Sinh câu hỏi có persona + refreshbằng query log thật Eval Mỗi dòng có đặc điểm chung: không crash, không exception Giảngviên (VinUni) AICB· Ngày 7 Tuần1 66 / 79

---

<!-- chiron-source-span: {"source_span_id":"57ae1bb9-e476-5b0c-83fe-e9f3ef29f3e5","locator":{"kind":"page","page":80,"label":"Slide 80","section_title":"“KhôngLỗi” Không Có Nghĩa Là“Đúng”","extraction_method":"pdf-text-layer"},"checksum":"79a7229b22d5c80f458aa9bbb8a5a99a0e7becd40c36c79869ccd1fcec2fdfd2"} -->

## Slide 80 - “KhôngLỗi” Không Có Nghĩa Là“Đúng”

6/14 failure mode ở bảng trên hoàn toànkhông raise exception nào Mộtpipeline retrieval có thể trảHTTP200,không log lỗi, không stacktrace — và vẫn hoàn toàn sai. Đây là mythphổ biến nhất và cũng làluậnđiểm cốt lõicủatoàn bộ phần này:“nếu nó không báo lỗi thì nó chạy đúng” làsai. Lưu ý:Antidote duy nhất là những gì vừa học ở đầu section: đo recall@k trên ground truth và benchmark BM25 làm sàn —đừng suy luận từ việc hệ thống không crash.(Quy lỗi retrieval-vs-generationbằng RAGAS là nội dungDay 8.) Giảngviên (VinUni) AICB· Ngày 7 Tuần1 67 / 79

---

<!-- chiron-source-span: {"source_span_id":"52d71e87-82af-5c6c-a35c-0a499dbad422","locator":{"kind":"page","page":81,"label":"Slide 81","section_title":"Bảo Mật & Quyền Riêng Tư","extraction_method":"pdf-text-layer"},"checksum":"833dfb8de2e42cffb8e3d84ed5d395fd3e69ef51dda786a3f157c1dad0d0cdd6"} -->

## Slide 81 - Bảo Mật & Quyền Riêng Tư

12 Vector store trông vô hại vì toàn số thực — nhưng số thực đó có thể bị đảo ngược lại thành văn bản gốc

---

<!-- chiron-source-span: {"source_span_id":"9d57d4ae-4649-5dbb-98e1-256efc838e45","locator":{"kind":"page","page":82,"label":"Slide 82","section_title":"VectorKHÔNG Phải Dữ LiệuĐã Ẩn Danh","extraction_method":"pdf-text-layer"},"checksum":"6b04af46f68ee3ae3b825382388d90b8e80e36ad9d876cb6018976cbd4e2e8e3"} -->

## Slide 82 - VectorKHÔNG Phải Dữ LiệuĐã Ẩn Danh

### Babước leo thang trong nghiêncứu inversion

- 2020— Song & Raghunathan: khôi phụcmộtphần bag-of-wordstừembedding.

- EMNLP2023 (Morris et al., arXiv:2310.06816),“Text Embeddings Reveal (Almost) As Much As Text” —khôi phục
câugần nhưnguyênvăn.

- 2025— ALGEN (arXiv:2502.11308): không gian embedding của cácencoderkhácnhau gầnnhư isomorphic ở
mứccâu ⇒mộtphép linearalignment,học từchỉ~1.000 mẫuròrỉ, đảo ngược được embeddingblack-box, transferxuyên domain và ngôn ngữ. Rủirothứhai,táchbiệt—MembershipInference — Khôngcầnkhôiphụcnộidung,chỉcầnbiết mộtpassage có tồn tạitrong retrieval DB hay không (Anderson et al., arXiv:2405.20446). Riêng sự hiện diện đã nhạy cảm:“hệ thống RAG của bệnh viện này có hồ sơ nhắc đến bệnh hiếm X”. Headlinecho slide Không thể coi vector-only index là dữ liệu đã de-identify.Inversion rò rỉnội dung; membership inferencerò rỉsự hiện diện. Nếu văn bảngốc nhạy cảm, vector của nócũng nhạy cảm. Nguồn: Song & Raghunathan (2020) · Morris et al., EMNLP 2023, arXiv:2310.06816 · ALGEN, arXiv:2502.11308 · Anderson et al., arXiv:2405.20446. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 68 / 79

---

<!-- chiron-source-span: {"source_span_id":"8725d5dd-cee0-5d8e-b0a2-ef17b92e0bad","locator":{"kind":"page","page":83,"label":"Slide 83","section_title":"TấnCông Qua Kênh Retrieval: Poisoning & Indirect Injection","extraction_method":"pdf-text-layer"},"checksum":"aae5dd1d798327fdf1e6dabf81e442bc25226c033b80da995eb3b67c083d4807"} -->

## Slide 83 - TấnCông Qua Kênh Retrieval: Poisoning & Indirect Injection

1. Corpus poisoning (PoisonedRAG)—Zou et al., arXiv:2402.07867, USENIXSecurity 2025:

- 90%attack success ratekhivăn bản độc được tốiưu đồng thời đểđược retrieve vàđể lái
câu trả lời.

- Điềukiện: 5văn bản độc cho MỖIcâu hỏi mục tiêu—không phải “90% với 5tài liệu” nói
chung.

- Phòngthủ rẻ: perplexityfiltering (vănbản bị tối ưu thườngcó PPL cao).

2. Indirect prompt injection—chỉ dẫn độc nằm trongtài liệu được retrieve:

- Vôhình vớibộ lọc chỉ kiểm trainput của user — payload đếnqua kênh retrieval.

- Nộidung retrieve đượcngầmtin cậyvìđến từ pipeline của chínhhệ thống.

- Blastradius nhân bản: một tài liệuđộc ảnh hưởng mọi user tươnglai; kẻ tấn công chỉ cần
đưatài liệu vào bất kỳnguồn nào corpus có index. Lưuý: Cơchếphòngthủ(spotlighting,instructionhierarchy,CaMeL,lethaltrifecta)thuộcvề Day11— Guardrails. Day 7 chỉcần thấykênhretrieval là một đường tấncông. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 69 / 79

---

<!-- chiron-source-span: {"source_span_id":"26b5938f-1042-5b29-8740-b9695be11242","locator":{"kind":"page","page":84,"label":"Slide 84","section_title":"Access-control-awareRetrieval: Filter TRƯỚCANN","extraction_method":"pdf-text-layer"},"checksum":"4f60f6cfcac4ba58f5486e58cecdd2befdd169bcf32f30c7d9c974241acd9b55"} -->

## Slide 84 - Access-control-awareRetrieval: Filter TRƯỚCANN

Yêucầu kiến trúc, không phải tínhnăng thêm:filtertheo quyền của usertrướchoặc tronglúcchạy ANN search — không baogiờ chỉ filtersau.

- Post-filterdướimộtpredicatechọnlọccóthể âmthầmtrảvềíthơnhoặc0kếtquả
(nhắclại frame filtered-ANN ở §9).

- VectorDB không kế thừa permissioncủa data store gốc⇒vectorindex là mục tiêu
táiđịnh danh tập trung, theo đúngrủi ro inversion ở đầu sectionnày. Patterncụ thể pgvector+Postgres row-levelsecurity ·Pineconenamespace-per-tenant ·pgvec- torscalelabel-aware in-index filtering. Capstonecủa Section 11 Đây là nơi §8 (filtered ANN), isolation opt-in và inversion gặp nhau: filter quyền hạn PHẢInằm trong đường đi ANN, khôngphải bước dọn dẹp sau cùng. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 70 / 79

---

<!-- chiron-source-span: {"source_span_id":"bd603708-03bf-54d4-8c6b-2f0f768d50d0","locator":{"kind":"page","page":85,"label":"Slide 85","section_title":"QuyĐịnh: VectorCó Phải Dữ Liệu Cá Nhân?","extraction_method":"pdf-text-layer"},"checksum":"b84bb7eebbd95f2415643b66be06ccedad12ea42428d68628f89652c931845e9"} -->

## Slide 85 - QuyĐịnh: VectorCó Phải Dữ Liệu Cá Nhân?

Khungpháp lý Nội dung chính Câuhỏi mở với embedding PDPL 91/2025 (VN) Hiệu lực 1/1/2026; “tailored safe- guards”choAI/bigdata/cloud;bảo vệ riêng biometric data; báo vi phạmtrong 72h Embeddingcủadữliệucánhâncó invertible (đầu section này) — có thuộcphạmviPDPLdù“trôngchỉ làsố”? Chưacó hướng dẫn. GDPR(EU) Recital 26: test là re-identification có “reasonably likely” hay không; pseudonymized vẫn là personal data(Art. 4(5)) Literaturevềinversiontừ2025trả lời có ⇒ coi embedding đã lưu là pseudonymized, không phải anonymized Khungnghĩ đúng cho sản phẩm Lưu embedding của dữ liệu cá nhân thì hãy thiết kế như đang lưu chính dữ liệu đó — về mặt kỹ thuật, gần như là vậy. (EU AIAct: xem Day11.) Nguồn: PDPL Luật 91/2025/QH15 (Tilleke & Gibbins) · GDPR Art. 4(5) & Recital 26 — lập luận kỹ thuật-pháp lý, không phải tư vấn pháp lý; chưa có phán quyết ràng buộc riêng cho embedding Giảngviên (VinUni) AICB· Ngày 7 Tuần1 71 / 79

---

<!-- chiron-source-span: {"source_span_id":"190c4de8-98a1-5c7b-b305-b50de57d0bf2","locator":{"kind":"page","page":86,"label":"Slide 86","section_title":"Kết Nối Agent Với Data","extraction_method":"pdf-text-layer"},"checksum":"7942c349b56304b80f462ae52749b00b53c55dcde10c1bf5aaf6c64fa4eca26b"} -->

## Slide 86 - Kết Nối Agent Với Data

13 Retrieval pipeline là chiếc cầu nối giữa dữ liệu riêng và hành vi của agent

---

<!-- chiron-source-span: {"source_span_id":"b8d1ca47-486b-5588-9786-29782102c457","locator":{"kind":"page","page":87,"label":"Slide 87","section_title":"Day7 vs Day 8 vsDay 19: Ai DạyCái Gì?","extraction_method":"pdf-text-layer"},"checksum":"dd99b098401a9f227a18d129a94d35fa4bb93545a2694f6e21013171ee6bdcc9"} -->

## Slide 87 - Day7 vs Day 8 vsDay 19: Ai DạyCái Gì?

Day7 (hôm nay) Data structure bên dưới re- trieval: text → vector, lưu & search thế nào, mọi cách pipelinelỗi thầmlặng. Day8 — RAG Xây ứng dụng RAG hoàn chỉnh: query rewriting, prompt assembly, answer synthesis,citation UX. Day19—VectorStore Vận hànhvector store trong production: deploy, scale, feature-store song song, Docker. Câucarve một dòng “Day 7 là cấu trúc dữ liệu bên dưới retrieval: text thành vector thế nào, vector được lưuvàsearchrasao,vàpipelineđófailthầmlặngởđâu. XâyứngdụngRAGlàDay

8. Vận hành vectorstore trong production là Day 19.” Giảngviên (VinUni) AICB· Ngày 7 Tuần1 72 / 79

---

<!-- chiron-source-span: {"source_span_id":"b60265fb-a893-55e0-815f-12c8d1af8769","locator":{"kind":"page","page":88,"label":"Slide 88","section_title":"Lab#7","extraction_method":"pdf-text-layer"},"checksum":"6ba38351c2b6037ed2637ffe5b0078bbc980b536db314c86347b4e64d4d0d1e2"} -->

## Slide 88 - Lab#7

LAB#7 Mụctiêu: Nốimộtbộdữliệuriêng(FAQ/SOP/policy)vàopipelinechunk →embed

- store →retrieve →injecttốithiểunhưngđúngbảnchất,rồitựđorecall@5bằng
no-labelsrecipe — không đoán mà đo. Deliverable: Script chunk + embed + index chạy được, demo semantic search với ≥3 câu hỏi test, một mini answer function dùng retrieved context, và một con số recall@5kèm 1–2 failure case tự tìmra. Thờigian: Buổilab, làm cá nhân trước rồiso sánh strategy theo nhóm. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 73 / 79

---

<!-- chiron-source-span: {"source_span_id":"69fed651-904a-5860-8418-0a0cc3f7dad6","locator":{"kind":"page","page":89,"label":"Slide 89","section_title":"LabStep 1: ChunkDữ Liệu","extraction_method":"pdf-text-layer"},"checksum":"c0c9fe0f83bc062e17a42b84cacf3b5ad203f28c74b24f1ce2999568e9a318d2"} -->

## Slide 89 - LabStep 1: ChunkDữ Liệu

```text
from langchain_text_splitters import RecursiveCharacterTextSplitter
# 2026 import path; langchain.text_splitter la shim da deprecated
splitter = RecursiveCharacterTextSplitter(
chunk_size=400, # tune theo embedding model, xem Sec 3/5
chunk_overlap=50, # 10-20% overlap giu ngu canh o bien chunk
separators=[ "\n\n", "\n", ". ", " ", ""]
)
chunks = []
for doc in load_documents("./data/"): # loader tu viet
parts = splitter.split_text(doc[ "text"])
for i, part in enumerate(parts):
chunks.append({
"id": f "{doc['source']}_chunk_{i}",
```
"text": part, "metadata": { "source": doc[ "source"], "category": doc[ "category"]}, }) Giảngviên (VinUni) AICB· Ngày 7 Tuần1 74 / 79

---

<!-- chiron-source-span: {"source_span_id":"605867a2-db21-52d6-811e-d56ab57528f2","locator":{"kind":"page","page":90,"label":"Slide 90","section_title":"LabStep 2: Embed& Store — Đúng API 2026","extraction_method":"pdf-text-layer"},"checksum":"648421a52ed4986d035736719043103afa4d08caab542b1d788202be894ec964"} -->

## Slide 90 - LabStep 2: Embed& Store — Đúng API 2026

```text
import chromadb
from chromadb.utils import embedding_functions
client = chromadb.PersistentClient(path= "./lab7_db") # ghi durable ngay lap tuc
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
model_name= "BAAI/bge-m3") # EXPLICIT - khong bao gio de mac dinh
col = client.get_or_create_collection( "lab7_kb", embedding_function=ef)
```

### for c in chunks
col.add(ids=[c[ "id"]], documents=[c[ "text"]], metadatas=[c[ "metadata"]]) # embeddings= khong can truyen - ef tu tinh Lưuý: Lỗi#1củaChroma: tạocollectionvới embedding_function tườngminh,sau đó mở lại bằngget_collection() khôngtruyền lạief— defaultall-MiniLM-L6-v2 (384-dim)âm thầm thế chỗ, query khônglỗi nhưng recall tụt. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 75 / 79

---

<!-- chiron-source-span: {"source_span_id":"f398742e-27e6-5c24-84a6-66881b02bb5a","locator":{"kind":"page","page":91,"label":"Slide 91","section_title":"LabStep 3: SemanticSearch + Answer WithContext","extraction_method":"pdf-text-layer"},"checksum":"1eb4ad3ee27f432e565de3b2580863343073d7ca7f2470fa57edfc00518b0334"} -->

## Slide 91 - LabStep 3: SemanticSearch + Answer WithContext

```text
def answer_with_context(query, collection, k=3):
res = collection.query(
query_texts=[query], n_results=k,
where={ "category": { "$eq": "support"}}, # metadata filter TRUOC ANN
)
context = "\n---\n".join(res["documents"][0])
prompt = f """Dua tren nguon sau, tra loi ngan gon.
```
Neu khong tim thay, noi 'Khong co thong tin'.

### Nguon
{context} Cau hoi: {query}"""

```text
return call_llm(prompt) # client LLM tu chon
Giảngviên (VinUni) AICB· Ngày 7 Tuần1 76 / 79
```

---

<!-- chiron-source-span: {"source_span_id":"ecd79007-3ab0-5057-9f4e-b3dc33f19fc2","locator":{"kind":"page","page":92,"label":"Slide 92","section_title":"LabStep 4: ĐoRecall@5 — Không Đoán, Đo","extraction_method":"pdf-text-layer"},"checksum":"5a0e74ce36d43049433ebe29ddd777fa40eca5bf64b35ed52aff9cf9f362316d"} -->

## Slide 92 - LabStep 4: ĐoRecall@5 — Không Đoán, Đo

# No-labels recall@5: chunk nguon = positive label # (citation-as-weak-label, xem Sec 9)

```text
def recall_at_k(collection, pseudo_queries, k=5):
hits = 0
```

### for query, source_chunk_id in pseudo_queries
res = collection.query(query_texts=[query], n_results=k)

### if source_chunk_id in res["ids"][0]
hits += 1

```text
return hits / len(pseudo_queries)
```
# pseudo_queries: nho LLM sinh 1-3 cau hoi CHO TUNG chunk, # chi dua tren noi dung chunk do -> chunk do la positive Lưu ý:Đây là floor check, không thay thế nhãn thật: câu hỏi do LLM sinh bám sát vănphongcủachunkgốc,nênrecallđođượcthường caohơn recallthựctếkhiuser diễnđạt lại. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 77 / 79

---

<!-- chiron-source-span: {"source_span_id":"3d82f307-51dd-55d4-ad8c-5098e8c1b5c6","locator":{"kind":"page","page":93,"label":"Slide 93","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"4256e8f85da9fd2bf32f9f3b06e0d51ddde7df1392c6c399053327f4ebb06aaa"} -->

## Slide 93 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 “Không lỗi” không có nghĩa là “đúng.”6/14 failure mode học hôm nay không hề raise exception— luận đề thật sựcủa Day 07. 2 Data qualitythường quan trọng hơn đổi sang model đắt hơn — pipeline tốt giải quyết phần lớnvấn đề trước. 3 Embeddingdịchngônngữsangkhônggiansosánhđượcnghĩa—cosinelàquyước,không phảichân lý. 4 Retrieval pipelinelà cầu nối từ dữ liệu riêng tới câu trả lời grounded — luônđorecall trước khiđổ lỗi cho model. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 77 / 79

---

<!-- chiron-source-span: {"source_span_id":"11c83d42-3e63-5f32-a555-c702fff6361e","locator":{"kind":"page","page":94,"label":"Slide 94","section_title":"TàiLiệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"69d13d4b4578aec4e03bf0b91a51e7a9e0477cef83e040fd9984e2918c2e15a2"} -->

## Slide 94 - TàiLiệu Tham Khảo

1. Malkov& Yashunin, Efficient and Robust Approximate Nearest Neighbor Using HNSW Graphs — arXiv:1603.09320,IEEE TPAMI2018/2020.

2. Steck,Ekanadham & Kallus,Is Cosine-Similarity of Embeddings Really About Similarity? — arXiv:2403.05440,WWW ’24.

3. Qu,Tu& Bao, Is Semantic Chunking Worth the Computational Cost? —arXiv:2410.13070, NAACL 2025Findings.

4. AnthropicEngineering, Contextual Retrieval —anthropic.com/engineering/contextual-retrieval (2024).

5. Kusupatiet al., Matryoshka Representation Learning —arXiv:2205.13147, NeurIPS 2022.

6. Thakuret al., BEIR: A Heterogeneous Benchmark for Zero-shot Retrieval —arXiv:2104.08663.

7. Zou,Geng, Wang& Jia, PoisonedRAG—arXiv:2402.07867, USENIX Security 2025.

8. Wu,Wang,Zhang, Zhang, Niu,Wu& Zhang, Semantic Cache Poisoning and Its Countermeasures — NDSS2026.

9. ChromaDocumentation, Collections / Query / Embedding Functions —docs.trychroma.com.

10. VietnamPDPL, Law No. 91/2025/QH15,hiệu lực 2026-01-01. Giảngviên (VinUni) AICB· Ngày 7 Tuần1 78 / 79

---

<!-- chiron-source-span: {"source_span_id":"ebea2a9a-9e38-595f-8d82-a845db9a2950","locator":{"kind":"page","page":95,"label":"Slide 95","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"91cd3622b60a84b0c6b2e7a540356abc6cb7c5fb6a681c6f5f04e8cfe10d1776"} -->

## Slide 95 - Tiếptheo & Bài tập

Bàitiếp theo BàiTiếpTheo: RAG “Hôm nay dừng ở “top-k chunk đã sẵn sàng.” Ngày 8 đi tiếp thành một ứng dụng RAG hoàn chỉnh: query rewrit- ing, prompt assembly, answer synthe- sis, citation UX, đánh giá end-to-end. ” Bàitập về nhà

- Ràlại knowledge base của
nhóm,bỏ 20% nội dung nhiễu nhất

- Chạyno-labels recall@5 trên
chínhcorpus của nhóm, ghi lại 2 failurecase

- Thửđổi chunk_size và
chunk_overlap,so sánh recall trước/sau Giảngviên (VinUni) AICB· Ngày 7 Tuần1 79 / 79

---

<!-- chiron-source-span: {"source_span_id":"b1c6c0e9-7aeb-5da1-a29d-7dc5dd8f4cb9","locator":{"kind":"page","page":96,"label":"Slide 96","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer-sparse","page_image":"../../assets/page-images/6d7611d322fd/page-0096.png","visual_fallback":true},"checksum":"ddafff7d95a561eaa9df8fdb6a18ffc6f4535eae4281d4d9b6c9a93c6c52bd52"} -->

## Slide 96 - Hỏi& Đáp

![Visual fallback - SLIDE DAY07 - slide 96](../../assets/page-images/6d7611d322fd/page-0096.png)

> Trang này được giữ dưới dạng ảnh vì text layer/OCR không đủ để biểu diễn nội dung trực quan.

---

<!-- chiron-source-span: {"source_span_id":"5ec1c6d2-d01e-5708-b9f4-072e3abe6ae7","locator":{"kind":"page","page":97,"label":"Slide 97","section_title":"Cảmơn!","extraction_method":"pdf-text-layer-sparse","page_image":"../../assets/page-images/6d7611d322fd/page-0097.png","visual_fallback":true},"checksum":"75ad71e3371b5cc37c70eab59eec9d416546d87315cd3a3d0ba5845ea4ec18c7"} -->

## Slide 97 - Cảmơn!

Cảm ơn!

![Visual fallback - SLIDE DAY07 - slide 97](../../assets/page-images/6d7611d322fd/page-0097.png)

> Trang này được giữ dưới dạng ảnh vì text layer/OCR không đủ để biểu diễn nội dung trực quan.
