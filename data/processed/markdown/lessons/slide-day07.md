---
schema_version: 1
course_id: rag-intensive
document_id: "dc00e14e-5667-515d-a31b-e9ec1989d88f"
document_version_id: "24702510-362d-5e10-8497-6adda42dc779"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Data Foundations — Embedding, Chunking & Vector Store — phân tích & breakdown từng slide"
source_file: "slide-day07.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\slide-day07.html"
source_sha256: "c1efa60a1791c7135a448a4d80d4b5cb9c474eca20056886eb0faa65c106f79d"
parser_version: chiron-structured-markdown-v1
html_section_count: 21
interactive_module_count: 3
interactive_control_count: 15
language: vi
---

# Data Foundations — Embedding, Chunking & Vector Store — phân tích & breakdown từng slide

> 97 slide, và là deck dày số nhất của cả Foundation: có công thức, có 
 benchmark, có trích dẫn arXiv đến từng bài. Luận đề trung tâm nằm ở slide 80 và nó đủ sắc để nhớ cả 
 năm: 6 trong 14 failure mode của Ngày 7 không ném ra một exception nào. Hệ thống trả HTTP 200, 
 không log lỗi, và sai hoàn toàn.

<!-- chiron-source-span: {"source_span_id":"a3ec05cd-9d89-5dac-98ab-e6e9aae1144c","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"slide-day07.html"},"checksum":"f5641dd2da8202df73524768d4c1509ebabe5a68c8ffe3e4dc56c95f5604afd8"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Ngày 7 khác mọi bài trước ở một điểm quan trọng: **deck này có số thật**. Ngày 6 nói 
 "ROI phải có số cụ thể" rồi không đưa số nào; Ngày 7 thì đưa công thức bộ nhớ, tỷ lệ nén, giá API đến 
 từng cent, và trích dẫn arXiv cho gần như mọi khẳng định định lượng — kèm cả những chỗ nó *bác bỏ* con số đang lan truyền trên mạng.

tự dựng

tái hiện đúng công thức của slide trước, rồi mới mở rộng

| Mô-đun | Tái hiện con số nào của slide | Mở rộng sang đâu |
| --- | --- | --- |
| Bộ nhớ ANN index | 61,4 GB cho 10M×1536 (slide 51) · nén 64× của PQ (slide 53) · 6.144 B + 256 B đồ thị HNSW 
 (slide 55) · ~15 tỷ phép tính mỗi query (slide 50) | Kéo N, d, M, kích thước mã PQ và trần RAM để thấy ngưỡng rời khỏi từng họ index |
| Post-filter sập recall | Quan sát thật trên pgvector 0.8.0-pg17: xin 15 láng giềng, nhận 11 dòng, không 
 exception (slide 65) | Mô hình nhị thức cho biết vì sao đúng là 11, và cần ef_search bao nhiêu mới hết thiếu |
| Kinh tế pipeline | $2 và $13 cho 100M token (slide 77) · bất đối xứng embed-một-lần / rerank-mỗi-truy-vấn 
 (slide 71) | Tính cả bốn khâu — và khâu đắt nhất không phải khâu nào trong hai khâu slide nói tới |

"6/14 failure mode ở bảng trên hoàn toàn không raise exception nào."

"cái này hỏng thế nào mà không ai biết"

query:

passage:

max_seq_len

normalize_L2

embedding_function

Lượt 1 · ~20 phút

Nắm trục xương sống

- Nhìn Hình 1 — sáu mắt xích Document → Chunk → Embed → Store → Query → 
 Inject, và chỗ 14 failure mode chui vào
- Đọc slide 8 — ba loại data, và vì sao chỉ một loại hợp với vector store
- Đọc slide 80 — luận đề "không lỗi ≠ đúng"
- Mục tiêu: nói được vì sao câu hỏi "tổng doanh thu quý 2" không nên 
 đi qua vector search

Lượt 2 · ~90 phút

Chương 5, 6, 7, 9 — phần bị hỏi nhiều nhất

- Chương 05 (bóc text) và 06 (chunking) quyết định trần chất lượng — không kỹ thuật nào 
 ở sau cứu được
- Chương 07 là chương duy nhất có toán; chạy mô-đun bộ nhớ song song với 
 khi đọc
- Chương 09 chứa lỗi production kinh điển nhất — chạy mô-đun filter

Lượt 3 · ~30 phút

Ôn thi

- 6 hiểu lầm — bốn cái trong đó chính deck đã tự bác bỏ bằng paper
- 3 bài bậc thang — kỹ năng: chẩn đoán một pipeline hỏng im lặng
- Cheat sheet — bảng ANN và bảng silent truncation nên thuộc

"Day 7 là cấu trúc dữ liệu bên dưới retrieval: text thành vector thế nào, vector được lưu và search 
 ra sao, và pipeline đó fail thầm lặng ở đâu. Xây ứng dụng RAG là Day 8. Vận hành vector store trong 
 production là Day 19."

query rewriting

citation UX

RAGAS

GraphRAG

"top-k chunk đã chọn"

"Tầng dữ liệu sai thì không kỹ thuật nào ở Day 8 cứu được."

---

<!-- chiron-source-span: {"source_span_id":"69290f34-a372-58fc-9b78-28a90bb21a48","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu — model yếu, hay không có đúng dữ liệu?","source_file":"slide-day07.html"},"checksum":"a8e891d5d8be8fc2762b4036f73ed56c4d037eb5e3cb8acb3dd046f458ffdb38"} -->

## 00 Mở đầu — model yếu, hay không có đúng dữ liệu?

Câu hỏi mở bài của Ngày 7 là câu hỏi phân định trách nhiệm. Trả lời sai câu này thì 
 cả quý sau đó đi tối ưu nhầm chỗ.

### Slide 2 Câu hỏi mở đầu — và vì sao nó không phải câu hỏi tu từ

> Trích slide 
>  "HÃY SUY NGHĨ… 'Agent trả lời sai vì model yếu, hay vì nó không có đúng dữ liệu để suy 
>  luận?' Giữ câu hỏi này trong đầu khi học bài hôm nay."

Câu này có một đáp án được deck khẳng định thẳng ở slide 93: *"Data quality thường quan trọng hơn 
 đổi sang model đắt hơn."* Nhưng để câu trả lời có sức nặng, phải thấy nó **rẻ hơn bao 
 nhiêu**:

| Hành động | Chi phí | Cải thiện điển hình |
| --- | --- | --- |
| Đổi từ text-embedding-3-small sang -3-large | $2 → $13 cho 100M token ( slide 77 ) | Vài điểm phần trăm recall, và không có bằng chứng vượt trội so với đối thủ rẻ hơn 
 ( slide 25 ) |
| Chunk bảng theo cấu trúc thay vì cắt theo ký tự | Công sức viết parser, ~0 chi phí vận hành | Recall@1 trên BM25: 0,366 → 0,754 — hơn gấp đôi ( slide 37 ) |
| Thêm đúng prefix query: / passage: | Một dòng code | 1–5% (model card Qwen3-Embedding-8B, slide 21 ) |
| Thêm nhánh BM25 cho mã lỗi / SKU | Một index lexical | Từ không tìm được thành tìm được — không đo bằng phần trăm được 
 ( slide 67 ) |

gấp 2,06 lần Recall@1

bóc text

chunking

trước

### Slide 4–5 Bảy mục tiêu và cái deliverable ép bạn phải đo

> Trích slide 
>  "Phân biệt được knowledge data, operational data, contextual data · Hiểu embedding là lớp biểu 
>  diễn nghĩa — cơ chế, cách huấn luyện, và giới hạn · Bóc được text ra khỏi file thật — PDF, Excel, 
>  HTML — và biết cái gì bị mất im lặng · Chọn được chunking strategy và giải thích 
>  được đánh đổi · Giải thích được ANN index (IVF, PQ, HNSW) đủ để chỉnh tham số, không chỉ gọi 
>  API · Nhận diện được các failure mode im lặng — lỗi không ném exception 
>  nhưng phá recall · Build được một mini retrieval integration" 
>  Deliverable: "1 bộ dữ liệu mẫu đã chunk và index · 1 script semantic search có trả kết quả liên 
>  quan · 1 hàm trả lời dùng context retrieve được thay vì hỏi LLM 'chay' · 1 bảng đo 
>  recall@5 trên tối thiểu 10 câu hỏi tự sinh "

Ba trong bảy mục tiêu chứa cùng một chữ: *im lặng* hoặc *đủ để chỉnh tham số*. Đó 
 không phải trùng lặp — đó là chủ đề.

một cái gì đó

một câu

một con số recall@5

slide 76

mà không cần ai gán nhãn tay

10 câu hỏi

N ≥ 100

làm quen quy trình

không

vặn núm nào khi recall thấp

vặn núm ấy đổi lấy cái gì

efSearch

nprobe

M

slide 53

sai

---

<!-- chiron-source-span: {"source_span_id":"b7feffd9-cce3-538f-95fb-d523196f3f2e","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Data strategy & agent memory","source_file":"slide-day07.html"},"checksum":"4bcfcfe11186220c4c97ca5b53a87251577a338aa374a76e292b999ff272692e"} -->

## 01 Data strategy & agent memory

Trước khi chọn embedding model, phải trả lời được: *dữ liệu nào đáng đưa vào 
 vector store, và dữ liệu nào đưa vào là sai ngay từ đầu.*

### Slide 7–8 Ba loại data — và chỉ một loại hợp với vector store

> Trích slide 
>  Knowledge — ít thay đổi, dạng text dài, cần chunk + embed · FAQ, SOP, chính sách, 
>  hợp đồng, tài liệu kỹ thuật · Retrieval fit: Rất cao — lý tưởng cho vector store 
>  Operational — thay đổi liên tục, dạng structured (SQL / JSON / logs) · trạng thái 
>  đơn hàng, CRM, ticket, tồn kho · Retrieval fit: Thấp — dùng function calling / 
>  SQL, không embed 
>  Contextual — gắn với session / user hiện tại, ngắn gọn · user profile, lịch sử 
>  hội thoại gần nhất, giỏ hàng · Retrieval fit: Trung bình — inject trực tiếp, ít 
>  khi cần semantic search 
>  Và trước đó: "Garbage in, garbage out. Dữ liệu bẩn/thiếu: PDF scan lỗi OCR · policy cũ chưa cập 
>  nhật · chunk cắt giữa câu · không có metadata → agent hallucinate."

Bảng này là bộ lọc đầu tiên và nó loại bỏ phần lớn ý tưởng tồi trước khi chúng tốn tiền. Cách dùng 
 thực dụng: với mỗi nguồn dữ liệu, hỏi **"câu hỏi về nó có phải câu hỏi ngữ nghĩa không?"**

| Câu hỏi thật của người dùng | Loại data | Công cụ đúng | Vì sao vector search sai |
| --- | --- | --- | --- |
| "Chính sách hoàn tiền nói gì?" | Knowledge | Vector search | — |
| "Đơn hàng #4471 của tôi tới đâu rồi?" | Operational | Function call / SQL | Cần giá trị chính xác, không phải cái gần giống. Và trạng thái đổi mỗi giờ — index sẽ 
 luôn cũ |
| "Tổng doanh thu quý 2 theo vùng" | Operational | Text-to-SQL | Không embedding nào cộng được số ( slide 38 ) |
| "Lúc nãy tôi nói gì về ngân sách?" | Contextual | Inject thẳng vào prompt | Corpus chỉ vài chục lượt — semantic search trên đó là over-engineering |

Slide 38

"Embed toàn bộ bảng giao dịch thành vector là 
 anti-pattern tốn kém và kém chính xác."

①

②

WHERE

làm sập recall

③

SELECT

Kiến trúc đúng theo slide: router, không phải chọn một.

PDF scan lỗi OCR · policy cũ chưa cập nhật · chunk cắt giữa câu · không có 
 metadata

chính bạn tạo ra

không cái nào ném exception

### Slide 9 Governance & PII masking — làm trước khi embed, không phải sau

> Trích slide 
>  "Governance trước khi index: ai sở hữu & cập nhật dữ liệu · ai được truy cập (ACL vs public 
>  nội bộ) · bao lâu re-index · PII có cần mask không — không 'cứ nạp hết vào vector DB 
>  đã'." 
>  Tên cá nhân → [PERSON], rủi ro trung bình · Số điện thoại → regex replace, 
>  cao · Email → hash hoặc remove, cao · CMND/CCCD → xoá hoàn toàn, 
>  rất cao · Địa chỉ → generalize, trung bình 
>  "Mask trước khi embed — không bao giờ lưu raw PII trong vector store. Vector không phải dữ 
>  liệu đã ẩn danh — embedding có thể bị đảo ngược gần đúng nguyên văn (Morris et al., EMNLP 
>  2023; ALGEN 2025)."

Câu cuối là câu quan trọng và nó được nhắc lại đầy đủ ở [chương 12](#s82). Ở đây chỉ cần 
 giữ một hệ quả vận hành: **thứ tự không đảo ngược được.**

xoá và tạo lại toàn bộ index

rẻ về tiền

cộng với

ai được truy cập

slide 84

trong

Ngày 5

plausible-but-incorrect

Ngày 6

data debt

### Slide 10 Memory ≠ retrieval — và bốn thứ KHÔNG phải memory

> Trích slide 
>  " Capture → Filter → Store → Retrieve. Sự kiện nào đáng lưu? · PII? quality? 
>  relevance? · vector / DB / profile · truy khi có ích cho câu hỏi hiện tại" 
>  " KHÔNG tự động là memory: prompt dài hơn · file PDF upload một lần không truy lại 
>  có chủ đích · toàn bộ chat history · 'lưu cho chắc' — những thứ này thường tạo nhiễu hơn là hữu ích." 
>  "Memory là data + policy + retrieval; thiếu một trong ba thì hệ thống khó ổn định. 
>  Retrieval tìm context cho câu hỏi hiện tại (relevance, grounding); memory giữ 
>  trạng thái người dùng qua thời gian (continuity). Nhầm hai khái niệm là lý do agent 'quên' 
>  context vừa retrieve ở lượt sau. Vocab chuẩn: working / episodic / semantic / procedural."

Phân biệt *retrieval* và *memory* là phân biệt về **trục thời gian**, và 
 nó giải thích một triệu chứng rất cụ thể mà nhiều team gặp:

|  | Retrieval | Memory |
| --- | --- | --- |
| Trả lời câu hỏi | "Thông tin nào liên quan tới câu này?" | "Người dùng này là ai, và ta đã thống nhất điều gì?" |
| Vòng đời | Sống trong đúng một lượt | Bắc qua nhiều phiên, nhiều tuần |
| Nguồn | Corpus dùng chung | Riêng từng người dùng |
| Hỏng thì thấy gì | Trả lời sai hoặc "không có thông tin" | Agent lặp lại câu hỏi đã hỏi, hoặc quên điều vừa thống nhất |

"Nhầm hai khái niệm là lý do agent 'quên' context vừa retrieve ở lượt sau."

chỉ lượt 1

không

Cách chữa

bổ sung tầng còn 
 thiếu

Query rewriting là nội dung Ngày 8

"Lưu cho chắc"

Filter

cạnh tranh vị trí top-k

bài tập về nhà của slide 95

"rà lại knowledge base của nhóm, bỏ 20% nội dung nhiễu nhất."

xoá

### Slide 11 Trục xương sống: Document → Chunk → Embed → Store → Query → Inject

> Trích slide 
>  " Document → Chunk → Embed → Store → Query → Inject. PDF, docs, HTML · chia theo 
>  section / token · vector hoá · index + metadata · semantic search · prompt grounded" 
>  " Đây là trục xương sống của cả Ngày 7. Mọi phần tiếp theo hôm nay chỉ đào sâu 
>  một mắt xích trong pipeline này."

Sáu mắt xích, và deck tự ánh xạ từng chương vào từng mắt xích. Nhưng có một cách đọc thứ hai hữu 
 ích hơn cho việc ôn thi và cho việc gỡ lỗi thật: **ánh xạ 14 failure mode của [slide 78–79](#s78) vào cùng sáu mắt xích đó.** Khi đó pipeline trở thành một bản đồ 
 chẩn đoán.

"câu trả lời sai, nhưng không có 
 lỗi nào"

khoanh vùng theo mắt xích

①

②

③

④

bài của Ngày 8

Hình 1

6/14

3

4

5

6

normalize_L2

7

10

11

không ném lỗi

bảy

ước lượng dè dặt

_Sơ đồ: Sáu mắt xích của pipeline dữ liệu và các failure mode chui vào ở từng mắt xích - Sáu hộp xếp ngang theo thứ tự document, chunk, embed, store, query, inject. Hộp document nhận PDF, HTML và Office, và mất mát ở đây gồm thứ tự đọc sai, bảng bị phá vỡ và OCR hỏng dấu tiếng Việt. Hộp chunk chia theo section hoặc token, chứa failure mode số bốn là cắt âm thầm và số chín là kích thước chunk sai. Hộp embed vector hoá, chứa failure mode số ba là thiếu prefix và số mười là dùng nhầm model mặc định. Hộp store là index cộng metadata, chứa failure mode số năm là đổi model mà không embed lại, số sáu là quên chuẩn hoá L2, số bảy là post-filter trả thiếu kết quả, số mười một là lệch embedding function sau khi khởi động lại, và số mười hai là tombstone của HNSW. Hộp query là semantic search, chứa failure mode số một là lệch từ vựng và số hai là mã lỗi bị làm nhoè. Hộp inject đưa vào prompt, chứa failure mode số tám là lấy quá nhiều và bị lạc giữa ngữ cảnh. Bên dưới là bốn câu hỏi chẩn đoán nhị phân, mỗi câu loại bỏ một phần pipeline. Một dải cuối ghi rằng ranh giới của ngày bảy dừng ở top-k chunk đã chọn, phần sau thuộc ngày tám._

Hình 1 — Sáu mắt xích, và chỗ từng failure mode chui vào.

slide 11

bảng failure mode

---

<!-- chiron-source-span: {"source_span_id":"e85479e4-d068-58dd-a348-1bf67ad95df5","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 Từ TF-IDF đến dense — 50 năm trong một bảng","source_file":"slide-day07.html"},"checksum":"03a60047b2f825a20adb2836b5a581642b8ae2b066a84933c165cf9bb9c9cf44"} -->

## 02 Từ TF-IDF đến dense — 50 năm trong một bảng

Chương lịch sử này không phải phần trang trí. Nó chứa hai kết luận vận hành: vì sao 
 BM25 vẫn sống năm 2026, và vì sao vector store phải precompute embedding.

### Slide 13–14 Vocabulary mismatch — vấn đề gốc, và mốc thời gian giải nó

> Trích slide 
>  "Lexical search (TF-IDF, BM25) chỉ khớp khi đúng từ xuất hiện ở cả query lẫn 
>  document. Ví dụ thất bại — Query: 'chính sách hoàn tiền'. Document chỉ viết: 'quy định 
>  đổi trả sản phẩm'. Không từ nào trùng khớp ⇒ BM25/TF-IDF không tìm ra, dù nghĩa gần như giống 
>  hệt." 
>  "Lưu ý: BM25 không 'lỗi thời': BEIR (2021, 18 dataset) cho thấy đây vẫn là 
>  baseline mạnh — một dense model fine-tune trên MS MARCO có thể thua BM25 khi ra ngoài domain 
>  huấn luyện." 
>  Mốc: 1972 IDF (Spärck Jones) · 1975 Vector Space Model (Salton) · 1990 LSA/LSI (Deerwester) · 
>  1994 BM25 (Robertson, TREC-3) · 2013 word2vec (Mikolov) · 2016 HNSW (Malkov & Yashunin) · 
>  2018/19 BERT (Devlin) · 2019 SBERT (Reimers & Gurevych) · 2020 DPR (Karpukhin, 
>  +9 đến +19% top-20 accuracy ) · 2025–26 decoder-LLM embedder + MRL + quantization

Bảng 50 năm này có một cấu trúc mà slide không nói ra, nhưng rất đáng nhớ: **hình học không 
 đổi từ 1975; cái đổi là vector đến từ đâu.** Salton đã dùng "văn bản = vector, so bằng hình học" 
 từ nửa thế kỷ trước. Cosine similarity năm 2026 vẫn là đúng công thức đó.

| Thời kỳ | Vector đến từ đâu | Chiều | Giới hạn |
| --- | --- | --- | --- |
| 1972–1994 · lexical | Đếm từ có trọng số IDF | = kích thước từ vựng (chục nghìn), thưa | Vocabulary mismatch — không khớp từ thì không tìm ra |
| 1990 · latent | SVD nén ma trận đếm còn ~100 chiều "khái niệm" | ~100, đặc | Tuyến tính, không có ngữ cảnh, phải tính lại toàn bộ khi thêm tài liệu |
| 2013–2019 · dense | Mạng nơ-ron học được từ dữ liệu | 384–1024, đặc | Chỉ mạnh trong domain đã huấn luyện — đây là điểm BEIR chỉ ra |
| 2025–26 | Decoder LLM + Matryoshka + lượng tử hoá | tới 4096, cắt được xuống 32 | Vẫn không xử lý được token ngoài từ vựng huấn luyện |

"Một dense model fine-tune trên MS MARCO có thể thua BM25 khi ra ngoài domain huấn luyện."

slide 75

luôn thêm BM25 làm sàn

hybrid search

ngoài

trường hợp BEIR mô tả không phải trường hợp 
 hiếm; nó là trường hợp mặc định của bạn.

cách biểu diễn nghĩa

2016 · HNSW

cách tìm nhanh

Slide 50

~15 tỷ phép nhân–cộng cho một query

biểu diễn

tìm kiếm

chương 07

### Slide 15 Vì sao BERT thô tệ cho similarity — và con số 65 giờ so với 5 giây

> Trích slide 
>  Cross-encoder (BERT gốc): "Muốn so hai câu ⇒ phải đưa cả cặp qua BERT cùng lúc. 
>  So khớp giữa 10.000 câu ⇒ ~50 triệu phép suy luận. ~65 giờ trên GPU 
>  để tìm cặp giống nhau nhất. Train cho masked-LM, không cho pooled similarity — không báo lỗi, 
>  chỉ cho vector không so sánh được." 
>  Bi-encoder (SBERT 2019): "Encode mỗi câu một lần, độc lập ⇒ vector cố định, 
>  precompute trước. So sánh bằng cosine similarity, không cần chạy lại BERT. Cùng bài toán: 
>  ~5 giây — độ chính xác tương đương trên STS."

Kiểm lại con số: 10.000 câu, số cặp là `10.000 × 9.999 / 2 = 49.995.000` ≈ **50 triệu**. Khớp chính xác với slide.

65 × 3600 / 5 = 46.800

hình dạng của 
 độ phức tạp

|  | Cross-encoder | Bi-encoder |
| --- | --- | --- |
| Số lần chạy model để so N câu đôi một | O(N²) | O(N) — mỗi câu 
 một lần, xong là xong |
| Thêm một tài liệu mới | Phải so với toàn bộ N câu cũ | Encode một lần, thêm vào index |
| Thêm một query mới | N lần chạy model | Một lần encode + một lần tìm ANN |

Đây chính là lý do vector store tồn tại.

tách chi phí tài liệu ra khỏi chi phí truy vấn

slide 71

là

không

Mô-đun kinh tế pipeline

đầu tiên

.encode()

BERT được fine-tune bằng contrastive 
 learning trên NLI để hình học similarity trở nên có nghĩa

---

<!-- chiron-source-span: {"source_span_id":"f00c8e38-cc0c-566a-b0a9-6248fb34498e","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Embeddings — bản chất, không phải phép màu","source_file":"slide-day07.html"},"checksum":"0f62f2961880d11e783689b99e68eaa7a59af0587c071b1081be5265cfa61632"} -->

## 03 Embeddings — bản chất, không phải phép màu

Ba slide trong chương này chứa ba thứ hiếm gặp trong tài liệu dạy RAG: một công thức 
 đủ đơn giản để tính tay, một paper bác bỏ niềm tin phổ biến nhất về cosine, và một cái bẫy khiến recall 
 tụt mà không ai biết.

### Slide 17–18 Ba bước thật của embedding, và pooling không trung lập

> Trích slide 
>  " Embedding — hàm học được biến dữ liệu thô thành vector số cùng chiều, sao cho 
>  'gần nghĩa' → 'gần hình học'. Một pipeline cụ thể: 1. Tokenize — cắt câu thành 
>  subword token · 2. Encoder — token qua nhiều lớp Transformer self-attention → vector 
>  theo ngữ cảnh · 3. Pooling — gộp vector token thành một vector câu: mean, 
>  last-token, hoặc [CLS]" 
>  " Pooling không trung lập. jina-embeddings-v5: mean pooling (v4) → last-token — 
>  mất Late Chunking, vốn cần vector theo token. Đổi pooling là đổi cả model." 
>  Cosine: cos(A,B) = (A·B) / (‖A‖‖B‖) — "1 = cùng hướng, 0 = vuông góc, −1 = ngược 
>  hướng". Euclidean: d(A,B) = √Σ(Aᵢ−Bᵢ)² — "0 = trùng nhau, càng lớn = càng xa".

Bước 3 là bước ít được nói tới nhất và là bước có hệ quả kiến trúc lớn nhất. Ghi chú về Jina v5 là 
 một ví dụ cụ thể đắt giá:

Late Chunking

slide 46

đã mang ngữ cảnh toàn tài liệu

mean-pool trong từng nhóm

vector câu phải là trung bình của vector token

last-token pooling

không còn định nghĩa được

Bài học tổng quát:

âm thầm gỡ bỏ

bài tập slide 19

cosine bỏ qua độ dài vector, Euclidean thì không.

cùng một thứ tự

d² = 2 − 2·cos

FAISS

### Slide 19–20 Bài tập tính tay, và paper bác bỏ niềm tin về cosine

> Trích slide 
>  Cặp 1: A = [1,2,3], B = [2,4,6]. Cặp 2: C = [1,0,0], 
>  D = [0,1,0]. "Lưu ý: Cặp 1 có cosine = 1.0 dù B = 2A. Vì sao? Điều này 
>  nói gì về cosine similarity so với Euclidean distance?" 
>  "Steck, Ekanadham & Kallus (Netflix + Cornell), Is Cosine-Similarity of Embeddings Really 
>  About Similarity?, WWW 2024: cosine similarity của embedding đã học 'can yield arbitrary 
>  and meaningless similarities' — với linear model regularized, cosine không xác định duy 
>  nhất. Regularization deep learning tác động 'implicit và unintended' lên cosine. Một số trường hợp, 
>  cosine tệ hơn dot product chưa chuẩn hoá." 
>  "Cách dạy đúng: Cosine là convention hiệu quả, không phải sự thật về ý nghĩa. 
>  'Metric mặc định' là lựa chọn kỹ thuật, không phải luật tự nhiên."

Đáp án bài tập, tính đầy đủ:

```text
CẶP 1 —  A = [1,2,3]   B = [2,4,6]
  A·B    = 1×2 + 2×4 + 3×6 = 2 + 8 + 18 = 28
  ‖A‖    = √(1+4+9)   = √14  ≈ 3,7417
  ‖B‖    = √(4+16+36) = √56  ≈ 7,4833
  cos    = 28 / (3,7417 × 7,4833) = 28 / 28 = 1,000
  d(A,B) = √((2−1)² + (4−2)² + (6−3)²) = √(1+4+9) = √14 ≈ 3,742   ← KHÔNG bằng 0

CẶP 2 —  C = [1,0,0]   D = [0,1,0]
  C·D    = 0        →  cos = 0        (vuông góc)
  d(C,D) = √2 ≈ 1,414
```

B nằm đúng trên tia của A

hướng

độ lớn

Khi nào điều này thành lỗi thật:

chủ động vứt bỏ

lựa chọn

bug #1 của FAISS

không

linear matrix factorization model có regularization

đổi cosine tuỳ ý

Cách dùng đúng kết luận này trong công việc:

không

xếp hạng

ngưỡng tuyệt đối

### Slide 21 Asymmetric search và cái bẫy prefix — 1–5% biến mất trong im lặng

> Trích slide 
>  Symmetric — query và document cùng loại (câu ↔ câu); tìm câu trùng lặp, STS. 
>  Asymmetric — câu hỏi ngắn tìm đoạn văn dài. "Đây chính là RAG." 
>  "Model được huấn luyện khác nhau cho hai phía — nên expose prefix hoặc instruction riêng: E5 dùng 
>  query: / passage:; Nomic v2 dùng search_query: / 
>  search_document:." 
>  "Lưu ý: Bỏ prefix không báo lỗi — nó âm thầm tạo ra embedding lệch calibration, 
>  xếp hạng sai. Model card Qwen3-Embedding-8B: dùng instruction cải thiện 1% đến 5% so 
>  với không dùng."

Đây là failure mode số 3 trong [bảng slide 78](#s78), và nó đáng phân tích kỹ vì nó là 
 mẫu mực cho cả nhóm "hỏng im lặng":

| Câu hỏi | Trả lời |
| --- | --- |
| Triệu chứng là gì? | Recall thấp hơn kỳ vọng khoảng 1–5%. Đủ nhỏ để đổ cho "model 
 chưa đủ tốt", đủ lớn để đáng tiền |
| Vì sao không có lỗi? | Prefix chỉ là chuỗi ký tự nối vào đầu text. Thiếu nó, 
 model vẫn nhận một chuỗi hợp lệ và vẫn trả về vector đúng số chiều |
| Vì sao nó lại quan trọng? | Model được huấn luyện với prefix đó có mặt. Nó là 
 tín hiệu phân biệt "đây là câu hỏi" với "đây là đoạn tài liệu" — hai phía được đẩy vào hai vùng 
 khác nhau của không gian trong lúc train |
| Cách phát hiện | Prefix-ablation test (slide 78 gọi đúng tên): chạy 
 eval hai lần, có và không có prefix, so recall@k. Chênh lệch chính là câu trả lời |
| Cách chống tái diễn | Bọc encode() trong một hàm của riêng bạn, prefix 
 nằm bên trong hàm đó. Không bao giờ gọi thẳng API của thư viện từ code ứng dụng |

nhất quán

một

passage:

query:

normalize_L2

embedding_function

index và query được tạo bằng hai quy trình khác nhau, và không có gì kiểm tra 
 rằng chúng khớp nhau.

Đối sách chung cho cả ba:

cấu hình embedding vào metadata của 
 collection

assert

slide 43

Contextual Retrieval

Late Chunking

slide 46

không

---

<!-- chiron-source-span: {"source_span_id":"71a0ee6e-d303-56fb-9a33-95eb6392b0bd","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Bức tranh embedding model 2026","source_file":"slide-day07.html"},"checksum":"ac39561499071670d7542d763f3328134dfbdec06bf58e99bcaf93cb64456ff8"} -->

## 04 Bức tranh embedding model 2026

Chương này có giá trị đặc biệt vì nó dành phần lớn dung lượng để *bác bỏ* — 
 bác bỏ "OpenAI là mặc định tốt nhất", bác bỏ cách đọc điểm MTEB, bác bỏ việc chọn model tiếng Việt theo 
 điểm tiếng Anh.

### Slide 24–25 Bảng model, bảng giá, và lầm tưởng về OpenAI

> Trích slide 
>  Open-weight: Qwen3-Embedding 0,6–8B, tới 4096 chiều (MRL → 32), 32K 
>  token cả 3 size, Apache-2.0 · EmbeddingGemma 308M, 768 (MRL → 128), 2K, Gemma terms · 
>  BGE-M3 ~568M, dense+sparse+multi-vector, 8192, MIT · Nomic Embed Text v2 MoE 
>  475M/305M active, 768 (MRL → 256), chỉ 512 token · Jina v4 3,8B, 2048 
>  API: OpenAI -3-large tới 3072, 8191, $0.13 /1M · 
>  -3-small tới 1536, 8191, $0.02 · Google 
>  gemini-embedding-2 MRL native, 8192, $0.20 ($0.10 batch) · Voyage 
>  voyage-3.5 2048/1024/512/256, $0.06 · Cohere embed-v4 
>  256–1536, 128K token 
>  "Lầm tưởng: 'OpenAI embeddings là mặc định tốt nhất.' -3-large / 
>  -3-small phát hành 25/1/2024, chưa cập nhật ~2,5 năm trong khi 
>  Google/Voyage/Jina ra nhiều thế hệ mới. -3-large: $0.13/M so với 
>  voyage-3.5: $0.06/M — không có bằng chứng vượt trội."

Ba chi tiết trong hai bảng này đáng nhớ hơn phần còn lại, và cả ba đều đi ngược trực giác:

Nomic Embed Text v2 (MoE, 2025) chỉ nhận 512 token

16 lần

64 lần

cắt âm thầm

Quy tắc rút ra:

trục sàng lọc đầu tiên

Slide 28

trước khi

-3-large

voyage-3.5

-3-small

gemini-embedding-2

10 
 lần

mô-đun kinh tế pipeline

$2 so với $20 — trả một lần

hàng trăm đô mỗi tháng

Kết luận thực dụng:

chất lượng retrieval

đó

dense + sparse + multi-vector

Slide 68

"Vậy 'hybrid chỉ là 3 hệ thống ghép 
 lại' còn đúng không? Ở SOTA (BGE-M3), không còn đúng nữa."

không

code mẫu của deck

### Slide 26 Một model, ba board, ba con số — và con số bị dùng sai

> Trích slide 
>  "MTEB đã tách thành nhiều board không so sánh được với nhau: MTEB(Eng, v2), 
>  MTEB(Multilingual)/MMTEB, MTEB(Code)... Điểm v2 không so được với v1." 
>  Cùng một model (Gemini Embedding), ba con số: "MTEB(Multilingual) Mean(Task): 
>  68.32 — con số được quảng bá làm headline · MTEB(Eng, v2) Mean(Task): 
>  73.28 · Task-Type Mean: 59.64 " 
>  "Lầm tưởng: '68.32 là điểm MTEB tiếng Anh.' Sai — đó là điểm MULTILINGUAL. Điểm 
>  English v2 thật là 73.28. Lỗi này lan qua nhiều trang tổng hợp, tạo ra so sánh tự mâu thuẫn (vd. đặt 
>  jina-v5-small 71.7 'vượt' Gemini 68.32, trong khi English thật của Gemini là 73.28)." 
>  " Một con số MTEB vô nghĩa nếu thiếu board + version + aggregation + ngày. "

Ví dụ so sánh sai trong slide đáng dựng lại đầy đủ, vì nó cho thấy lỗi này lật ngược kết luận chứ 
 không chỉ làm nó lệch:

| So sánh | Con số được dùng | Kết luận rút ra | Đúng hay sai |
| --- | --- | --- | --- |
| jina-v5-small vs Gemini Embedding | 71.7 vs 68.32 | "jina-v5-small vượt Gemini" | Sai — 68.32 là điểm đa ngôn ngữ của Gemini |
| Cùng cặp, cùng board | 71.7 vs 73.28 | Gemini cao hơn | Đây mới là so sánh cùng thước đo |

Board

version

aggregation

8,7 điểm

ngày

59.64

Và ngay cả khi đủ bốn thứ, con số vẫn chỉ là để lập shortlist.

Slide 28

50–100 query từ chính corpus của bạn

"Từ 2025–26 MTEB đã chuyển sang kết quả verified, không còn thuần self-reported."

slide 33

với mọi bảng xếp hạng, hỏi ai chạy nó trước khi hỏi ai đứng đầu.

### Slide 27–28 Tiếng Việt: VN-MTEB, RoPE, và quy trình chọn model 20 phút

> Trích slide 
>  " VN-MTEB (EACL 2026 Findings): benchmark embedding tiếng Việt chuẩn hoá đầu tiên — 
>  41 dataset, 6 loại task. Phát hiện đáng chú ý: model dùng RoPE vượt trội hơn 
>  model dùng absolute positional embedding trên task tiếng Việt, ở nhóm model cùng quy mô. 
>  Trước VN-MTEB, nhóm phát triển thường chọn model tiếng Việt theo điểm MTEB tiếng Anh và hy vọng 
>  transfer tốt — không đảm bảo." 
>  " AITeamVN/Vietnamese_Embedding v2: fine-tune từ BGE-M3 trên ~1,1 triệu triplet tiếng 
>  Việt; 2048 max sequence, 1024 dims, Apache-2.0. Đường đi thực dụng: không dùng thẳng model đa 
>  ngôn ngữ, cũng không train từ đầu — fine-tune model đa ngôn ngữ mạnh trên domain triplet. " 
>  Quy trình 20 phút: "1. Viết độ dài chunk tối đa và dạng query (có exact code/SKU/ID không?) — 
>  loại bớt ứng viên trước khi benchmark. 2. Shortlist 2–3 model theo license + 
>  deployment. 3. Xây bộ eval 50–100 query từ chính corpus của bạn. 4. Đo recall@k, 
>  dùng đúng prefix cho từng model. 5. Chỉ sau đó mới tinh chỉnh dimension và quantization. "

Bước 1 loại ứng viên trước khi tốn công benchmark.

biết trước

Bước 5 đặt quantization ở CUỐI, và đó là chi tiết quan trọng nhất.

đánh đổi

"luôn build Flat trước"

đo trần trước, nén sau.

diễn giải

một "từ" thường trải trên nhiều token

tương đối

một giả thuyết nhất quán với quan sát

phát hiện

lời giải thích

---

<!-- chiron-source-span: {"source_span_id":"f0868888-779c-5d08-86a1-27f923a378c1","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Bóc text ra khỏi file thật","source_file":"slide-day07.html"},"checksum":"013cdd86761924b65921da2d88bd1839a2932de148a7fa7dc88b3df5dd32c418"} -->

## 05 Bóc text ra khỏi file thật

Chương dài nhất của deck, và deck nói thẳng vì sao: *"đây là khâu quyết định trần 
 chất lượng của cả pipeline."* Mọi kỹ thuật ở các chương sau chỉ giúp bạn tiến gần trần đó — không có 
 cách nào vượt qua nó.

### Slide 30–31 Ba nhóm dữ liệu, và vì sao PDF khó hơn bạn nghĩ

> Trích slide 
>  Unstructured (PDF scan, ảnh, chữ viết tay, audio) → OCR/VLM parsing → text + 
>  layout · Semi-structured (HTML, DOCX, PPTX, Markdown, email) → bóc boilerplate, giữ 
>  cây heading · Structured (Excel, CSV, SQL, JSON, log) → thường KHÔNG nên 
>  embed thô 
>  " PDF là định dạng mô tả CÁCH VẼ trang, không mô tả NỘI DUNG. Nó lưu 'đặt glyph 
>  này tại toạ độ (x,y)' — không lưu 'đây là ô thứ 3 của hàng thứ 2 trong bảng'." 
>  "Born-digital vs scanned · Reading order: 2 cột, sidebar, chú thích — 
>  pdftotext đọc theo thứ tự vẽ, có thể trộn cột trái với cột phải thành câu vô nghĩa · 
>  Header/footer lặp · Bảng: mất quan hệ hàng–cột là lỗi tốn kém nhất · 
>  công thức, biểu đồ, hình" 
>  "'PDF là text, chỉ cần pdftotext ' — đúng với đúng một loại tài liệu: born-digital, 
>  một cột, không bảng. Với corpus thật, đây là giả định sai đắt nhất trong cả pipeline."

Câu định nghĩa PDF là câu đáng thuộc lòng, vì nó giải thích cả năm vấn đề bên dưới bằng một nguyên 
 nhân duy nhất: **thông tin cấu trúc chưa bao giờ được lưu, nên không có gì để "đọc ra" — chỉ có 
 thể suy đoán lại.**

| Triệu chứng | Cái gì đã mất | Nó lộ ra ở đâu trong retrieval |
| --- | --- | --- |
| Reading order lộn xộn | Không có khái niệm "cột", chỉ có toạ độ | Chunk chứa câu ghép từ hai cột — vector mô tả một ý không tồn tại |
| Header/footer lặp | Không có nhãn "đây là header" | Tên công ty + số trang chèn vào mọi chunk → mọi vector bị kéo về cùng một hướng, giảm 
 độ phân biệt |
| Bảng vỡ | Không có quan hệ hàng–cột | Header ở chunk này, giá trị ở chunk kia — không kỹ thuật nào ghép lại được |
| Công thức, biểu đồ | Thông tin nằm trong pixel | Câu hỏi về nội dung đó không bao giờ có câu trả lời trong index |

pdftotext

slide 33

"lấy 20 trang khó nhất trong corpus của bạn, chạy qua 2–3 công cụ, và đọc bằng mắt."

### Slide 32–33 Công cụ 2026, và vì sao bảng xếp hạng gần như vô dụng

> Trích slide 
>  Docling (IBM, MIT) — DocLayNet layout + TableFormer, mạnh về bảng phức tạp · 
>  MinerU — 2.5-Pro đứng đầu OmniDocBench v1.6 theo báo cáo của chính nhóm tác 
>  giả · Marker — nhanh, benchmark v2 do chính Datalab chạy · 
>  Unstructured — 30+ định dạng, có sẵn chunking · LlamaParse — hosted, 
>  trả phí theo trang · olmOCR (AI2) — VLM 7B, 82.4 trên olmOCR-Bench · 
>  MarkItDown (MS) — nhẹ, không GPU, yếu với PDF scan 
>  "OmniDocBench (CVPR 2025, 1.355 trang, 9 loại tài liệu ) chấm 4 trục: text (edit 
>  distance), công thức (CDM), bảng (TEDS), reading order. Trên v1.5: GLM-OCR 94,6% 
>  (SOTA), PaddleOCR-VL-1.5 >94%, Gemini 3 Pro 90,3%. MinerU 2.5-Pro báo cáo 95,69 
>  trên v1.6, Table TEDS 93,42." 
>  "Khi nhiều hệ vượt 94%, phần tăng thêm chủ yếu là 'vá edge case', không còn phản ánh chất lượng 
>  thực tế trên corpus của bạn. Tệ hơn: các bảng xếp hạng mâu thuẫn nhau — cùng bộ công 
>  cụ, đổi bộ tài liệu là đổi thứ hạng. Và phần lớn benchmark được chạy bởi chính nhà cung cấp 
>  công cụ."

① Bão hoà.

1,09 điểm

② Xung đột.

độ khớp giữa công cụ và bộ tài liệu benchmark

③ Xung đột lợi ích.

"Lấy 20 trang khó nhất trong corpus của bạn (scan mờ, bảng lồng, 2 cột), chạy qua 2–3 công cụ, và 
 đọc bằng mắt. Đó là benchmark duy nhất có giá trị quyết định."

30 phút

Cách chọn "20 trang khó nhất":

slide 31

Slide 34

"Chạy trafilatura trước cho toàn bộ corpus; chỉ chuyển sang parser nặng cho những trang mà cấu 
 trúc thực sự quan trọng. Đừng trả giá GPU cho 100% corpus để cứu 5% trang."

tự động phát 
 hiện

tỉ lệ ký tự trên diện tích trang thấp 
 bất thường

có ≥ 2 khối text tách biệt theo trục x

có 
 nhiều đường kẻ ngang/dọc

phần khó của corpus

### Slide 34–35 HTML, Office, email — cái bạn mất khi convert

> Trích slide 
>  " 80% trang web không phải nội dung. Menu, banner, ad, footer, 'bài liên quan' — 
>  nếu embed thẳng HTML thô, phần lớn vector mô tả giao diện, không phải nội dung." 
>  " Trafilatura — heuristic nhiều tầng, không ML, không GPU, khoảng 
>  14–22 ms/trang · ReaderLM-v2 (Jina) — transformer 1,54B, cấu trúc 
>  trung thực hơn nhưng cần GPU và chậm hơn nhiều bậc · justext — bóc theo mật độ 
>  stopword. Trang đã convert đúng thường dùng ít hơn khoảng 65% token so với HTML thô." 
>  DOCX — giữ được cây heading (rất quý cho chunking); mất comment, tracked 
>  changes, footnote. "Một hợp đồng mà phần thương lượng nằm ở comment thì bản parse là 
>  bản sai." · PPTX — thứ tự đọc theo thứ tự tạo shape chứ không theo 
>  thị giác; speaker notes thường là phần có giá trị nhất và thường bị bỏ quên · 
>  Email — chữ ký, disclaimer, thread reply lồng nhau khiến cùng một đoạn văn bị index 
>  hàng chục lần ⇒ near-duplicate làm hỏng top-k 
>  "Với mỗi định dạng, hỏi hai câu: (1) cấu trúc nào đáng giữ để chunk theo? (2) nội dung nào 
>  bị mất im lặng khi convert? Câu hai quan trọng hơn — vì không có exception nào được ném ra."

Con số **65% token** là con số hiếm khi được nói tới và nó đáng đưa vào mô hình chi 
 phí. Nó không chỉ tiết kiệm tiền embed:

① Chi phí.

② Chất lượng vector — đây mới là phần chính.

giống hệt nhau trên mọi trang

③ Ngân sách context.

Mô-đun kinh tế

| Định dạng | Cấu trúc đáng giữ | Mất im lặng cái gì | Khi nào điều đó là thảm hoạ |
| --- | --- | --- | --- |
| DOCX | Cây heading — dùng thẳng cho structure-aware chunking | Comment · tracked changes · footnote | Hợp đồng đang thương lượng: điều khoản thật nằm trong comment |
| PPTX | Nhóm shape theo slide | Speaker notes · thứ tự đọc thị giác | Slide chỉ có bullet 3 chữ; toàn bộ lập luận nằm trong notes |
| Email | Cây thread, người gửi, thời gian | Ranh giới giữa nội dung mới và phần quote lại | Một câu bị index 20 lần → chiếm sạch top-k, đẩy hết nội dung khác ra |
| HTML | Cây heading h1–h6 | Nội dung render bằng JavaScript | Trang SPA: parser thấy một khung rỗng, không lỗi, chunk rỗng vào index |

"một hợp đồng mà phần thương lượng nằm ở comment thì bản parse là bản sai"

không

tính đúng đắn

giảm

rất tốt

một

lượng thông tin

slide 75

recall@k cần nhưng chưa đủ

slide 40

### Slide 36–37 Bảng là điểm hỏng im lặng số một — và con số chứng minh

> Trích slide 
>  Excel: "Ô merge ⇒ NaN rải rác, phải fill-down · header nhiều tầng (2–3 dòng) ⇒ 
>  tên cột thật là ghép của các tầng: 'Q2 2026 · Doanh thu · VND' · một sheet có thể chứa nhiều 
>  bảng rời + ô ghi chú tự do · formula vs value — với retrieval, gần như luôn là kết quả 
>  · số, ngày tháng, đơn vị: định dạng hiển thị khác giá trị thật (1.234,56 vs 1234.56)" 
>  " Định dạng serialize quyết định recall. Một hàng nên trở thành một đơn vị 
>  tự đủ nghĩa: "Q2 2026 | Doanh thu | 4,2 tỷ VND" — không phải một ô '4.2' trôi 
>  nổi không có header." 
>  "Khi chunker cắt một bảng theo ký tự, quan hệ hàng–cột biến mất: header 'Doanh thu Q2 2026' rơi vào 
>  chunk này, giá trị '4,2 tỷ' rơi vào chunk khác. Không kỹ thuật retrieval nào ghép lại 
>  được. " 
>  Structure-aware Tabular Chunking (STC) vs RecursiveCharacterTextSplitter, trên MAUD 
>  (39.231 bản ghi hợp đồng M&A từ SEC EDGAR), ngân sách 512 token: 
>  MRR (hybrid) 0,358 → 0,595 · Recall@1 (hybrid) 0,347 → 0,539 · 
>  Recall@1 (BM25) 0,366 → 0,754 · số chunk sinh ra ít hơn ~40%. 
>  Guttal et al., arXiv:2605.00318.

Bảng số này là bằng chứng định lượng mạnh nhất trong cả deck, và đáng đọc theo tỉ lệ chứ không theo 
 hiệu số:

| Chỉ số | Recursive | STC | Tỉ lệ | Nghĩa là gì |
| --- | --- | --- | --- | --- |
| MRR (hybrid) | 0,358 | 0,595 | 1,66× | Kết quả đúng đầu tiên leo từ khoảng hạng 3 lên khoảng hạng 1,7 |
| Recall@1 (hybrid) | 0,347 | 0,539 | 1,55× | Từ 1/3 số truy vấn trúng ngay kết quả đầu, lên hơn một nửa |
| Recall@1 (BM25) | 0,366 | 0,754 | 2,06× | Nhánh lexical hưởng lợi nhiều nhất — xem ghi chú bên dưới |
| Số chunk | — | ít hơn ~40% | — | Rẻ hơn để embed, index nhỏ hơn, ít nhiễu hơn trong top-k |

token chính xác

không chunk nào chứa đủ cả hai token của truy vấn

2,06×

Bài học tổng quát:

không độc lập

và

nửa 
 vời

Cái giá:

bảng ở slide 2

```text
SAI  — ô trôi nổi, không có ngữ cảnh
  "4.2"
  "1.234,56"

SAI  — cắt theo ký tự, header rơi mất
  "...Doanh thu | Chi phí | Lợi nhuận\nQ1 2026 | 3,8 | 2,1 |"
  "...1,7\nQ2 2026 | 4,2 | 2,4 | 1,8..."      ← chunk này không biết cột nào là cột nào

ĐÚNG — mỗi hàng tự đủ nghĩa, header ghép từ mọi tầng
  "Q2 2026 | Doanh thu | 4,2 tỷ VND"
  "Q2 2026 | Chi phí   | 2,4 tỷ VND"
  "Q2 2026 | Lợi nhuận | 1,8 tỷ VND"

  + metadata: {sheet: "BCTC", bang: "Ket qua kinh doanh", hang: 7, nguon: "bctc_2026.xlsx"}
```

ghép lại

tỷ VND

provenance

### Slide 38 Khi nào KHÔNG nên embed — ba câu hỏi, ba công cụ

> Trích slide 
>  "'Tổng doanh thu quý 2 theo vùng' — cần aggregation, không phải similarity. 
>  Không embedding nào cộng được số. · 'Đơn hàng mới nhất của khách X' — cần 
>  sort + filter chính xác, đúng thế mạnh của SQL · 'Chính sách hoàn tiền nói gì?' — 
>  đây mới là việc của vector search." 
>  "Kiến trúc thực dụng: định tuyến, không chọn một. Một router quyết định: câu hỏi 
>  số liệu → text-to-SQL; câu hỏi khái niệm → vector search; câu hỏi quan hệ → graph. Nhiều hệ production 
>  2026 chạy cả ba song song rồi hợp nhất kết quả." 
>  "Trước khi embed bất cứ thứ gì, hỏi: câu hỏi này có phải câu hỏi ngữ nghĩa không? "

Câu *"không embedding nào cộng được số"* ngắn nhưng nó đóng một cánh cửa hoàn toàn. Đáng mở 
 rộng thành một bảng phân loại dùng được:

| Động từ trong câu hỏi | Ví dụ | Công cụ | Vì sao vector search không làm được |
| --- | --- | --- | --- |
| Tổng / trung bình / đếm | "Doanh thu quý 2 là bao nhiêu?" | SQL | Phép cộng không tồn tại trong không gian cosine. Similarity không phải số học |
| Mới nhất / cũ nhất / top N | "Đơn hàng gần nhất của khách X" | SQL | Cần thứ tự tuyệt đối theo một cột, không phải thứ tự theo độ giống |
| Đúng bằng / thuộc danh sách | "Đơn có mã VN-2291-XL" | SQL hoặc BM25 | Dense embedding làm nhoè token chính xác — slide 67 |
| Ai liên quan tới ai | "Công ty nào cùng tập đoàn với X?" | Graph | Quan hệ nhiều bước không nằm trong một vector nào |
| Nói gì về / quy định thế nào | "Chính sách hoàn tiền nói gì?" | Vector search | — |

Router phân loại rồi chọn một nhánh

bạn không biết

Chạy cả ba song song rồi hợp nhất

RRF

rank

chạy nhánh rẻ trước, và có tiêu chí rõ 
 để leo thang

### Slide 39–40 Tiếng Việt hỏng riêng ở đâu, và bước chuẩn hoá ai cũng quên

> Trích slide 
>  " Dấu thanh và dấu phụ mang nghĩa: OCR nhầm một dấu là đổi hẳn từ (ma / mà / má / 
>  mã / mạ). Tesseract mặc định yếu ở đúng điểm này. · Độ phân giải scan tối thiểu 300 
>  DPI — dưới ngưỡng đó, o/ô/ơ và a/ă/â bắt đầu lẫn. · Chuẩn hoá Unicode bắt 
>  buộc: cùng một chữ 'ế' có thể mã hoá dựng sẵn (NFC) hoặc tổ hợp (NFD). Hai dạng 
>  không khớp nhau khi so chuỗi và tạo ra chunk trùng lặp mà mắt thường không phân biệt 
>  được. Chuẩn hoá NFC toàn corpus ngay sau khi parse." 
>  Chuẩn hoá sau parse: "Unicode NFC · bỏ header/footer lặp · nối từ bị gạch nối cuối dòng 
>  (de-hyphenation) và gộp dòng thành đoạn · xoá trang trắng, mục lục, trang bìa · khử trùng 
>  lặp — cùng một tài liệu thường tồn tại nhiều bản (v1, v2, final, final-2)." 
>  " Provenance: giữ từ đây, không thể thêm sau. Mỗi đoạn text nên mang theo tên file, 
>  số trang, đường dẫn heading ngay từ lúc parse. Đây là thứ cho phép câu trả lời trích nguồn 'theo 
>  trang 14 của hợp đồng A'. Nếu không giữ ở khâu này, không khâu nào sau đó tạo lại được. "

ế

U+1EBF

e

hiển thị giống hệt nhau

"ế" == "ế"

False

hai vector khác nhau cho cùng 
 một từ

gần như chắc chắn

Cách chữa là một dòng, và phải chạy ngay sau parse:

```text
import unicodedata
text = unicodedata.normalize("NFC", text)   # chay TRUOC moi buoc khac
```

thông tin "đoạn này đến từ 
 trang 14" đã bị phá huỷ

"mọi câu trả lời phải trích được nguồn"

parse lại toàn bộ corpus

Chi phí giữ provenance ngay từ đầu:

| Bước | Hay bị quên? | Hậu quả nếu bỏ |
| --- | --- | --- |
| Unicode NFC | Gần như luôn | Chunk trùng lặp vô hình, vector lệch, BM25 không khớp |
| Khử trùng lặp (v1, v2, final, final-2) | Rất thường | Top-k bị chiếm bởi các bản của cùng một tài liệu — và có thể là bản cũ |
| Bỏ header/footer lặp | Thường | Mọi vector bị kéo về cùng hướng, giảm độ phân biệt |
| De-hyphenation + gộp dòng | Thỉnh thoảng | "chính sá-\nch" thành hai token rác; câu bị cắt giữa chừng ở mọi dòng |
| Xoá trang bìa, mục lục, trang trắng | Ít | Mục lục khớp mọi truy vấn (nó chứa mọi tiêu đề) — nhiễu top-k rất mạnh |

chinhsach_v1

chinhsach_final

ngữ nghĩa

còn hiệu lực

data debt

Ngày 6

---

<!-- chiron-source-span: {"source_span_id":"ff4da065-2e3b-5c8c-b9ad-fb400e501c3e","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Chunking — và ba con số bị deck bác bỏ","source_file":"slide-day07.html"},"checksum":"0869bc4dec727b206010d7477d077955d071d04024b6cb81e449333a69fa53f1"} -->

## 06 Chunking — và ba con số bị deck bác bỏ

Chương này đáng chú ý vì nó dành nhiều dung lượng để *gỡ bỏ* niềm tin sai hơn 
 là để dạy kỹ thuật mới: con số 512 không phải quy luật, semantic chunking không tự động tốt hơn, và hai 
 con số đang lan truyền trên mạng thì **không tồn tại trong nguồn nào**.

### Slide 42–43 Quá to hay quá nhỏ đều trả giá — và "512" đến từ đâu

> Trích slide 
>  Chunk quá to (>1000 token): "dính nhiều chủ đề vào cùng một vector" → "retrieve trúng nhưng 
>  inject rất nhiễu". Chunk hợp lý (200–500): "một ý / một section trọn vẹn, overlap với chunk liền kề". 
>  Chunk quá nhỏ (<50): "mất ngữ cảnh, retrieve nhiều mảnh rời rạc" → "khó tổng hợp thành câu trả lời 
>  đầy đủ". 
>  " BERT (2018) có bảng positional embedding giới hạn cứng ở 512 token — đây là giới 
>  hạn kiến trúc của một model cụ thể năm 2018, không phải một quy luật retrieval. Con 
>  số này sống sót qua vô số tutorial RAG như một 'default' bất di bất dịch — lâu hơn hẳn lý do kỹ thuật 
>  ban đầu. Embedder 2026 đã bỏ xa nó: BGE-M3 / Jina 8K; Qwen3-Embedding 32K; Cohere Embed v4 128K." 
>  " Không có ngưỡng '512 token' phổ quát. Bhat, Rudat, Spiekermann & Flores-Herr 
>  (arXiv:2505.21700, 2025): chunk 64–128 token tối ưu cho câu hỏi factoid ngắn; 
>  512–1024 token tốt hơn khi cần hiểu ngữ cảnh rộng — và tối ưu còn phụ thuộc 
>  embedding model (Stella lợi với chunk lớn, Snowflake lợi với chunk nhỏ, tập trung entity)." 
>  "Hệ quả: Đổi embedding model ⇒ phải đo lại chunk size. Đừng copy con số của deck 
>  khác sang model khác."

Câu chuyện "512" là một ví dụ mẫu mực về **ràng buộc kỹ thuật hoá thành tín điều**: 
 một giới hạn kiến trúc năm 2018 sống sót thành mặc định mặc nhiên năm 2026, sau khi lý do tồn tại của 
 nó đã biến mất từ lâu.

| Loại câu hỏi | Ví dụ | Chunk tối ưu | Vì sao |
| --- | --- | --- | --- |
| Factoid ngắn | "Đổi trả trong bao nhiêu ngày?" | 64–128 token | Câu trả lời nằm gọn trong một câu. Chunk lớn pha loãng nó với chín câu không liên quan |
| Ngữ cảnh rộng | "Quy trình xử lý khiếu nại diễn ra thế nào?" | 512–1024 token | Câu trả lời là một quy trình nhiều bước; cắt nhỏ thì mỗi chunk là một mảnh vô nghĩa |

Hệ quả mà slide không nói ra:

cả hai

không

① Index hai tầng.

mở rộng

② Chunk theo cấu trúc, không theo số.

slide 44

"Đổi embedding model ⇒ phải đo lại chunk size."

đo lại chunk size

bảng slide 78

"recall dao động 
 mạnh giữa các loại tài liệu"

Cách phòng:

ba

### Slide 44–45 Thang chiến lược, và paper bác bỏ semantic chunking

> Trích slide 
>  Fixed-size split ~free, baseline · + Overlap ~free, giảm mất ngữ 
>  cảnh tại điểm cắt · Recursive character splitting (thử \n\n → \n → space → ký 
>  tự ) ~free, "gần như luôn thắng fixed-size, chuẩn mặc định" · Structure-aware 
>  ~free–cheap, tài liệu có cấu trúc rõ · Semantic (breakpoint) — 1 lượt embed/câu, 
>  "chỉ khi đã đo thấy gap thật" 
>  " Càng lên cao chi phí càng tăng — chỉ leo khi đã đo được một gap retrieval thật. " 
>  "Qu, Tu & Bao (Vectara/UW-Madison/Penn), Is Semantic Chunking Worth the Computational 
>  Cost?, arXiv:2410.13070, NAACL 2025 Findings: chi phí tính toán 'not justified by 
>  consistent performance gains'." 
>  "Con số ' semantic chunking 87% vs fixed-token 50% ' (một 'clinical study') 
>  không tồn tại trong nguồn nào — đừng dùng. Con số ' chậm hơn ~14× ' 
>  là benchmark throughput của Chonkie, không phải từ paper. Nhãn 'Vectara 2024' và 
>  'Qu 2025' là cùng một paper bị đếm hai lần."

Ba đính chính trong slide 45 đáng đọc kỹ, vì chúng là ba dạng lỗi thông tin khác nhau — và cả ba đều 
 rất phổ biến trong tài liệu về RAG:

| Dạng lỗi | Ví dụ trong slide | Cách tự phát hiện |
| --- | --- | --- |
| Con số bịa — không có nguồn nào | "87% vs 50%" của một "clinical study" | Tìm ngược nguồn gốc. Nếu chuỗi trích dẫn dừng ở một blog dẫn một blog khác, con số không tồn 
 tại |
| Con số đúng, gán sai nguồn | "chậm hơn 14×" là throughput của Chonkie, bị gán cho paper | Mở đúng paper và tìm con số. Nó hoặc có, hoặc không |
| Một nguồn bị đếm hai lần | "Vectara 2024" và "Qu 2025" là cùng một paper | So tác giả và tiêu đề, không so nhãn năm — preprint và bản hội nghị khác năm nhau |

hai

thật sự

khi trích một con số, ghi kèm ai chạy nó, trên bộ dữ liệu nào, năm nào.

MTEB

benchmark parser

Contextual Retrieval

"Chỉ leo khi đã đo được một gap retrieval thật."

```text
BAC 1  Recursive character splitting, chunk 400, overlap 50
       -> do recall@5 tren bo eval khong nhan (slide 76). DAY LA SAN.

BAC 2  Tai lieu co heading ro? -> chunk theo heading
       -> do lai. Neu khong tang: DUNG, giu bac 1.

BAC 3  Corpus co bang? -> structure-aware tabular chunking
       -> day la buoc co bang chung manh nhat: MRR 1,66x (slide 37)

BAC 4  Van con gap, va gap nam o tai lieu dai co tham chieu chao?
       -> thu Late Chunking hoac Contextual Retrieval (slide 46)

BAC 5  Semantic breakpoint chunking
       -> chi khi 4 buoc tren da het, VA ban do duoc gap con lai
```

một phép đo

### Slide 46 Late Chunking và Contextual Retrieval — hai cách nghĩ lại, một bài học về vendor eval

> Trích slide 
>  Late Chunking (Jina, arXiv:2409.04701): "Đảo ngược thứ tự: embed toàn văn bản 
>  bằng long-context model trước, chunk ngay trước mean pooling. Chunk vector vẫn giữ 
>  ngữ cảnh toàn tài liệu (vd. resolve pronoun xuyên ranh giới chunk). Không cần fine-tune riêng." 
>  Phụ thuộc mean pooling — Jina v5 đổi sang last-token pooling nên mất khả năng này. 
>  Contextual Retrieval (Anthropic, 2024): "Prepend 50–100 token ngữ cảnh do LLM 
>  sinh vào mỗi chunk, trước khi embed và index BM25. Top-20 failure rate: 5,7% (baseline) → 
>  3,7% (−35%, +contextual embed) → 2,9% (−49%, +BM25) → 1,9% (−67%, +rerank). Chi phí: 
>  $1.02/triệu token tài liệu (prompt caching)." 
>  " Lưu ý: eval riêng của Anthropic (vendor). Reproduction độc lập (Merola & Singh, ECIR 
>  2025): NDCG@5 0.317 vs 0.312 — thật nhưng nhỏ hơn nhiều so với 49%. "

Cặp con số ở dòng cuối là bài học phương pháp luận đắt nhất của cả chương. Tính ra: `0,317 / 0,312 − 1 = **1,6%**` cải thiện tương đối — so với **49%** giảm failure rate mà vendor báo cáo.

hai thứ khác nhau, trên hai bộ dữ liệu khác nhau, bằng hai thước đo khác nhau

|  | Anthropic | Merola & Singh (ECIR 2025) |
| --- | --- | --- |
| Đo cái gì | Giảm failure rate ở top-20 | NDCG@5 |
| Kiểu con số | Tương đối, trên một đại lượng nhỏ (5,7%) | Tuyệt đối, trên một đại lượng ở giữa thang |
| Ai chạy | Chính nhà cung cấp | Bên thứ ba |

Mẹo thống kê ẩn trong con số 49%:

94,3% → 97,1%

tăng 2,8 điểm phần trăm

Quy tắc rút ra:

"phần trăm của cái gì, và giá trị tuyệt đối đi từ đâu đến đâu?"

$1.02/M token

-3-small

$0.02/M

51 lần

$102

thang chiến lược

đo được

mỗi lần re-index

"Jina v5 đổi sang last-token pooling nên mất khả năng này."

slide 17

một quyết định nội tại của model (đổi cách pooling) làm biến 
 mất một kỹ thuật ở tầng pipeline

Đối sách:

ghi nó ra thành một dòng trong tài liệu kiến 
 trúc

Ngày 6

### Slide 47–48 Silent truncation — bảng nên thuộc lòng, và demo chunk xấu/tốt

> Trích slide 
>  Nomic Embed Text v2 MoE 512 · mxbai-embed-large ~512 · EmbeddingGemma 
>  2.048 · gemini-embedding-001 2.048 · BGE-M3 / Arctic-Embed 2.0 / nomic-embed-text-v1.5 
>  / Jina v2–v3 8.192 · Qwen3-Embedding (cả 3 size) 32.768 · 
>  jina-embeddings-v5-text 32K · Cohere Embed v4 128K 
>  " Text vượt max_seq_len bị cắt âm thầm bởi hầu hết client library — không 
>  raise lỗi. Không có bản Qwen3-Embedding 40K; model card ghi rõ 32K cho cả ba size." 
>  Demo — chunk xấu, cosine 0.61: "…giao hàng miễn phí đơn trên 500k. Đổi trả 
>  trong 30 ngày. Liên hệ hotline 1900…" → trả lời nhiễu, thiếu chi tiết. 
>  Chunk tốt (theo section + metadata), cosine 0.89: "Chính sách đổi trả: khách 
>  hàng có 30 ngày kể từ ngày nhận hàng để yêu cầu đổi trả. Sản phẩm phải còn nguyên tem." → chính 
>  xác, có nguồn.

① Không có tín hiệu nào.

② Hỏng có chọn lọc.

③ Không thể phát hiện sau.

Cách chống duy nhất là chống trước:

trước

encode()

assert

```text
MAX = 8192   # doc tu model card, KHONG doan
n = len(tokenizer.encode(text))
if n > MAX:
    raise ValueError(f"chunk {cid}: {n} token > {MAX} — se bi cat am tham")
```

có chứa câu trả lời đúng

tỉ lệ tín hiệu trên nhiễu bên trong chunk

Đây là lý do recall@k không đủ để kết luận

slide 75

metadata

provenance giữ ở khâu parse

"Không có bản Qwen3-Embedding 40K; model card ghi rõ 32K cho cả ba size."

slide 45

thông số kỹ 
 thuật bị nhớ sai và lan truyền

đọc model card, không đọc bài tổng hợp.

max input · số chiều · prefix

---

<!-- chiron-source-span: {"source_span_id":"361bb392-0797-53ad-945e-525569f7fe8d","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Bên trong vector store — thuật toán ANN","source_file":"slide-day07.html"},"checksum":"333781b80571775dd04a2ba982a00eca06a0be5f8ff52a48742207409b008a21"} -->

## 07 Bên trong vector store — thuật toán ANN

Chương duy nhất có toán, và deck đặt mục tiêu rất rõ: hiểu *"đủ để chỉnh tham số, 
 không chỉ gọi API"*. Nguyên lý xuyên suốt nằm gọn trong một câu ở slide 50.

### Slide 50–51 Ba đồng tiền, và vì sao luôn phải build Flat trước

> Trích slide 
>  "Exact k-NN: O(N · d) mỗi query — với N = 10 triệu, d = 1536: 
>  ~15 tỷ phép nhân–cộng cho MỘT query." 
>  " Recall — tìm đúng láng giềng thật hay không · Latency — trả lời 
>  trong bao lâu · Memory — index chiếm bao nhiêu RAM/disk" 
>  "Nguyên lý xuyên suốt: Mọi kỹ thuật ANN chỉ là một cách không nhìn hết corpus. Mỗi index 
>  tiêu một trong ba đồng tiền trên để mua đồng tiền còn lại — không index nào thắng cả ba. " 
>  Flat: "Recall 100% theo định nghĩa — đây là ground truth để đo recall của mọi 
>  index khác. Memory: N × d × 4 bytes. N = 10M, d = 1536 ⇒ ~61,4 GB. Khi nào dùng 
>  thẳng: corpus nhỏ (vài nghìn document trở xuống) — một vector DB lúc này là 
>  over-engineering." 
>  " Luôn build Flat trước tiên trong lab. Không có ground truth thì 'recall' là một từ vô 
>  nghĩa. "

Kiểm lại hai con số: `10.000.000 × 1.536 = 15,36 tỷ` phép tính ✓ · `10.000.000 × 1.536 × 4 = 61,44 GB` ✓. Cả hai khớp slide chính xác.

tỉ lệ láng giềng đúng nằm trong kết quả trả về

đúng

đúng theo exact search

nghĩ

recall so với nhãn của người

recall so với ANN ground truth

| Đo cái gì | Ground truth là | Trả lời câu hỏi |
| --- | --- | --- |
| Recall của index | Kết quả Flat trên cùng embedding | "Index có bỏ sót láng giềng mà embedding đã tìm đúng không?" |
| Recall của hệ thống | Nhãn người, hoặc pseudo-label 
 ( slide 76 ) | "Pipeline có tìm được tài liệu trả lời được câu hỏi không?" |

efSearch

30,7 MB

dưới 10 ms

100%

không có

Hình 1

Slide 63

"Dưới 10k vector… Sub-ms. Bỏ qua vector DB."

### Slide 52–53 IVF và PQ — hai cách "không nhìn hết", hai đồng tiền khác nhau

> Trích slide 
>  IVF: "k-means chia corpus thành nlist cell (Voronoi partition). 
>  Query: tìm nprobe centroid gần nhất, chỉ scan vector trong các cell đó. Analogy: sơ đồ 
>  tầng thư viện — tìm đúng khu kệ trước, rồi mới đọc sách trên khu đó." 
>  "Một cấu hình cụ thể (Pinecone, IVF256, PQ32x8): nprobe=1 → 30% recall @ 136µs; 
>  nprobe=8 → 74% recall @ 729µs. Bắt buộc train: IVF cần một pass train() trên 
>  sample đại diện để học centroid — Chroma/pgvector giấu bước này, FAISS thô thì không." 
>  " 'Dùng nprobe = 8–16 cho 1–10M vector' không có trong docs FAISS hay bài Pinecone. 
>  Bài học thật: tăng nprobe đến khi recall bão hoà so với Flat ground truth — không có 
>  công thức." 
>  PQ: "128-dim float32 = 512 bytes → 8 subspace × 16-dim, mã 8-bit 
>  = 8 bytes → tỷ lệ nén 64×. M lớn hơn giữ độ chính xác tốt 
>  hơn nhưng ăn mòn CẢ tỷ lệ nén LẪN tốc độ — 'M càng lớn càng tốt' là sai. OPQ: học một ma 
>  trận xoay trực giao, áp dụng TRƯỚC khi chia subspace."

Hai cấu hình nprobe của Pinecone là một minh hoạ hoàn hảo cho "ba đồng tiền", và đáng tính ra tỉ lệ 
 đánh đổi:

|  | nprobe = 1 | nprobe = 8 | Đánh đổi |
| --- | --- | --- | --- |
| Recall | 30% | 74% | +44 điểm phần trăm |
| Latency | 136 µs | 729 µs | chậm hơn 5,4× |
| Memory | không đổi | nprobe là núm vặn lúc query, không 
 rebuild |  |

dưới một phần nghìn giây

ở phần lớn ứng dụng RAG, latency của ANN không 
 phải điểm nghẽn.

nprobe

efSearch

"nprobe = 8–16 cho 1–10M vector"

nlist ≈ 4√N

"điểm khởi đầu"

phân bố của chính vector của bạn

Quy trình đúng, ba dòng:

đúng cho corpus của bạn

M

Mã dài ra.

M × bits / 8

ăn mòn chính lý do bạn dùng PQ

Cộng khoảng cách chậm hơn.

"số subspace PQ"

mô-đun bộ nhớ

OPQ là cách thoát khỏi đánh đổi này mà không tốn thêm bộ nhớ:

"không có con số cải thiện đáng tin cậy — chỉ 'thường tốt hơn ở cùng kích thước mã'"

### Slide 54–56 HNSW, bảng so sánh, và cheatsheet bảy bước

> Trích slide 
>  HNSW: "multi-layer proximity graph. Lớp trên thưa (bước nhảy xa), lớp dưới dày 
>  (chi tiết); lớp đáy chứa toàn bộ điểm. Analogy: hệ thống cao tốc. Ai dùng: FAISS 
>  IndexHNSWFlat, hnswlib (chính là index nền của ChromaDB), Qdrant, 
>  Weaviate, Milvus, pgvector." 
>  M: memory ↑, recall ↑ — thường 16 · efConstruction: 
>  thời gian build ↑ — thường 200 · efSearch: latency ↑, recall ↑ — 
>  tuỳ SLA 
>  Bảng so sánh: Flat 100% recall, 6.144 B /vector · HNSW-Flat ~95–99%, 
>  6.144 B + 256 B graph · IVF-PQ lossy, vài chục byte (nén 64×) · 
>  DiskANN 95%+ recall@1, <3ms, >5000 QPS · Quantize (int8/binary) + rescore 
>  ~lossless / ~96%, nhỏ hơn 4× hoặc 32× 
>  Cheatsheet: "1. Build Flat trước. 2. RAM dư, ≤10M vector → HNSW; 
>  RAM là điểm nghẽn, ≥100M → IVF-PQ hoặc DiskANN; <10k → Flat, bỏ luôn 
>  vector DB. 3. HNSW: M=16, efConstruction=200; chỉ tune efSearch lúc query — núm vặn 
>  duy nhất không cần rebuild. 4. IVF: nlist ≈ 4√N khởi đầu. 5. PQ: M phải chia hết d, mã 
>  8-bit. 6. Quantize sau cùng, luôn kèm rescoring. int8 mặc định an toàn; binary chỉ 
>  khi d ≥ 1024. 7. Đo recall@k so với Flat, ở k thật, với filter thật đang dùng."

Kiểm con số HNSW: `1536 × 4 = 6.144 B` cho vector, cộng `M × 16 = 16 × 16 = 256 B` cho cạnh đồ thị ✓. Đồ thị chỉ thêm **4,2%** bộ nhớ — rẻ đến bất ngờ so với lợi ích tốc độ.

efSearch

| Tham số | Đổi được lúc chạy? | Nếu muốn đổi thì phải làm gì |
| --- | --- | --- |
| efSearch (HNSW) | CÓ | Đổi một biến, hiệu lực ngay |
| nprobe (IVF) | CÓ | Đổi một biến, hiệu lực ngay |
| M, efConstruction (HNSW) | Không | Rebuild toàn bộ index |
| nlist (IVF) | Không | Train lại centroid + reindex |
| Số chiều, model, mã PQ | Không | Re-embed + rebuild |

chọn thận trọng ở ba dòng dưới

thoải mái thử ở hai dòng trên

k thật

với filter thật đang dùng

"k thật"

"với filter thật"

chương 09

"chỉ lộ ra khi filter thật lên production, không phải trong demo"

Mô-đun post-filter

không phải benchmark có kiểm soát

gần như mọi bảng số trong lĩnh vực này đều được ghép từ các nguồn không cùng điều kiện.

hiểu hình dạng đánh đổi

_Sơ đồ: Cây quyết định chọn họ index ANN, và thứ tự chỉnh tham số - Bước không: luôn build index Flat trước để có ground truth, vì không có ground truth thì từ recall không có nghĩa. Câu hỏi thứ nhất: số vector có dưới mười nghìn không. Nếu có thì dùng Flat trong RAM hoặc một mảng NumPy và bỏ hẳn vector database. Nếu không thì sang câu hỏi thứ hai: số vector nhân số chiều nhân bốn byte có vừa RAM không. Nếu vừa thì dùng HNSW với M bằng mười sáu và efConstruction bằng hai trăm. Nếu không vừa thì sang câu hỏi thứ ba: có từ một trăm triệu vector trở lên không. Nếu có thì dùng DiskANN hoặc IVF-PQ. Nếu không thì dùng IVF-PQ hoặc lượng tử hoá int8 kèm rescoring. Phần dưới liệt kê thứ tự chỉnh tham số gồm bảy bước, và ghi chú rằng mỗi index tiêu một trong ba đồng tiền recall, latency, memory để mua hai đồng tiền còn lại._

Hình 2 — Chọn họ index, và thứ tự vặn núm.

slide 56

slide 50

#### Tương tác Bộ nhớ & nén của ANN index — công thức slide 51, 53, 55 chạy được

Ba slide đưa ba công thức và vài con số mẫu. Mô-đun này chạy chúng trên bộ tham số bạn 
 đặt, để thấy **ngưỡng rời khỏi từng họ index** — thứ mà cây quyết định ở Hình 2 hỏi nhưng 
 không tính được.

Mặc định là đúng ví dụ của slide: **10 triệu vector, 1536 chiều**, HNSW **M = 16**, PQ **96 byte** /vector, máy có **64 GB RAM**.

Đoán trước: *(a)* Flat chiếm bao nhiêu? *(b)* đồ thị HNSW thêm bao nhiêu phần trăm? *(c)* ở 1536 chiều, `int8` nén được mấy lần, và `binary` mấy lần?

#### Kéo rồi mở

**(a) 61,44 GB** — khớp chính xác con số "~61,4 GB" của slide 51. `10.000.000 × 1.536 × 4 = 61,44 × 10⁹ byte`. Với 64 GB RAM thì *vừa vặn một cách nguy hiểm*: chỉ còn 2,5 GB cho hệ điều hành, cho chính process, và cho 
 mọi thứ khác. Thực tế đây đã là "không vừa".

**(b) Chỉ 4,2%.** Đồ thị thêm `M × 16 = 256 B` lên 6.144 B — **2,56 GB** trên tổng 64 GB. Đây là con số đáng nhớ: *HNSW cho bạn tốc độ gần như 
 miễn phí về bộ nhớ.* Nó đắt ở chỗ khác — thời gian build, và không xoá được rẻ 
 ( [FAISS `IndexHNSWFlat` không hỗ trợ `remove_ids()`](#s58) ).

**(c) int8 nén đúng 4×** (4 byte → 1 byte mỗi chiều) và **binary nén 32×** (4 byte → 1 bit). Cả hai con số này *không phụ thuộc số chiều* — chúng là tỉ lệ giữa kiểu dữ 
 liệu, nên luôn đúng. Đó là lý do slide 56 gọi `int8` là "mặc định an toàn": lợi ích cố 
 định, dễ dự đoán, và gần như lossless *khi có rescoring*.

**Thử điều đáng thử nhất — kéo số chiều từ 1536 xuống 256:** Flat rơi từ 61,44 GB 
 xuống **10,24 GB** — vừa RAM thoải mái, và bạn không cần ANN index nào cả. 
 Đây chính là *Matryoshka Representation Learning* mà [slide 24](#s24) nhắc 
 tới: nhiều model 2026 cho phép **cắt bớt chiều mà vẫn dùng được** (Qwen3 tới 4096 → 
 32; EmbeddingGemma 768 → 128). Giảm chiều là núm vặn bộ nhớ mạnh nhất trong bảng — mạnh hơn cả đổi 
 họ index. Nhưng theo [slide 28](#s27), nó là **bước 5**: chỉ vặn sau khi 
 đã đo trần chưa nén.

*Bài học vận hành:* nhìn cột "B / vector" chứ đừng nhìn tổng. Tổng đổi theo N, nhưng **byte mỗi vector là đặc trưng của lựa chọn kiến trúc** — và nó cho bạn biết ngay 
 corpus của bạn phình tới đâu thì vỡ RAM.

- **Control - Số vector N: 10,0 triệu**: min `30`, max `95`, step `1`, default `70`

- **Control - Số chiều d: 1536 chiều**: min `64`, max `4096`, step `64`, default `1536`

- **Control - HNSW M (số cạnh mỗi nút): 16**: min `4`, max `64`, step `4`, default `16`

- **Control - PQ — số subspace (mã 8-bit): 96**: min `8`, max `256`, step `8`, default `96`

- **Control - RAM của máy: 64 GB**: min `4`, max `512`, step `4`, default `64`

Flat (ground truth)

—

—

HNSW

—

—

IVF-PQ

—

—

Phép tính nếu quét hết

—

—

Flat — chuẩn so sánh index giữ vector nguyên bản lượng tử hoá + rescore PQ — nén mạnh nhất, lossy

#### Xem bảng: sáu họ index ở cấu hình hiện tại



#### Công thức & giới hạn của mô hình

- Flat = N · d · 4 byte (float32) — công thức nguyên văn của slide 51.
- HNSW = N · d · 4 + N · M · 16 — slide 55 ghi 6.144 B + 256 B graph ở d=1536, 
 M=16; hệ số 16 B mỗi cạnh là ước lượng phổ biến cho id 32-bit cộng overhead cấu trúc.
- IVF-PQ = N · (M_pq · bits / 8) — slide 53: 8 subspace × 8 bit = 8 B cho vector 
 128 chiều, nén 64×.
- int8 = N · d · binary = N · d / 8 — nén 4× và 32×, không phụ thuộc d.
- Giới hạn ①: chỉ tính vector và cấu trúc index. Không tính document 
 gốc, metadata, hay bản sao trong quá trình build — thực tế cần thêm đáng kể, và lúc rebuild có thể 
 cần gấp đôi vì index cũ và mới cùng tồn tại.
- Giới hạn ②: IVF-Flat cộng ~2% overhead danh sách là con số xấp xỉ, phụ thuộc 
 nlist và cài đặt cụ thể.
- Giới hạn ③: mô-đun không mô hình hoá recall. Nén 32× nghe hấp dẫn cho 
 tới khi bạn đo recall — và slide 55 ghi binary "~96% giữ lại" khi có rescore. Bộ nhớ là 
 đồng tiền dễ tính nhất trong ba đồng tiền; hai đồng còn lại phải đo.

---

<!-- chiron-source-span: {"source_span_id":"79264062-5396-55f1-ac4b-a07e6f26ea62","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 FAISS, ChromaDB & landscape 2026","source_file":"slide-day07.html"},"checksum":"1682a21c1efd991718fd7a85e29138bc7dbc23e525454b2c0fdf8e8526311527"} -->

## 08 FAISS, ChromaDB & landscape 2026

Ba slide trong chương này chứa ba cái bẫy cụ thể đến mức có thể copy thẳng vào 
 checklist code review — và cả ba đều là failure mode im lặng.

### Slide 58–59 FAISS là library, không phải database — và bug #1

> Trích slide 
>  "FAISS là index + search kernel tối ưu tốc độ và memory — không hơn. Không có 
>  persistence ngoài write_index / read_index ra file · không có metadata 
>  schema, không có where filter tích hợp · không CRUD/transaction, không multi-tenancy, 
>  không access control · IndexHNSWFlat không hỗ trợ remove_ids() 
>  — raise lỗi, kể cả khi wrap thành IDMap2. Ngược lại, họ IVF (IVFFlat, IVFPQ) có hỗ 
>  trợ remove_ids trực tiếp." 
>  " FAISS không có METRIC_COSINE. Chỉ có METRIC_L2 và 
>  METRIC_INNER_PRODUCT. Cosine phải được giả lập bằng cách normalize vector trước khi dùng 
>  inner product." 
>  faiss.normalize_L2(vectors) # in-place, before index.add -- half 1 of 2 
> index = faiss.IndexFlatIP(d) 
> index = faiss.IndexIDMap(index) 
> index.add_with_ids(vectors, ids) 
>  
> faiss.normalize_L2(query) # ALSO before search -- the forgotten half 
> D, I = index.search(query, k) 
>  " Quên normalize không raise lỗi. Nó lặng lẽ suy biến thành xếp hạng theo dot-product thô 
>  — ưu tiên vector dài hơn. "

Chú thích trong code — *"the forgotten half"* — chỉ đúng chỗ đau. Lỗi hầu như không bao giờ 
 là quên cả hai; nó là quên **một**.

Quên cả hai:

nhất quán

Quên một nửa:

‖q‖ · cos(q, d)

‖q‖

thứ hạng vẫn đúng

giá trị tuyệt 
 đối của điểm

ngưỡng

slide 20

remove_ids()

IndexHNSWFlat

không xoá được

| Corpus của bạn | Chọn | Vì sao |
| --- | --- | --- |
| Tài liệu tĩnh, cập nhật theo lô hàng tháng | HNSW | Rebuild định kỳ là chuyện bình thường — không cần xoá lẻ |
| Ticket / nội dung người dùng, xoá thường xuyên | IVF | remove_ids hoạt động trực tiếp |
| Có yêu cầu "xoá dữ liệu của tôi" (GDPR/PDPL) | IVF hoặc DB có xoá thật | Nghĩa vụ pháp lý không chờ lịch rebuild — xem slide 85 |

tombstone

vẫn bị duyệt qua rồi lọc bỏ

### Slide 60–62 ChromaDB: "default là một cái bẫy"

> Trích slide 
>  Kiến trúc: " PersistentClient chạy trong process của bạn, ghi thẳng ra đĩa. Rust core 
>  từ v1.0 (1/3/2025). Index dùng hnswlib (HNSW) bên dưới. Metadata lưu trong 
>  SQLite. Bản hiện hành: chromadb 1.5.9 (5/5/2026)." 
>  "Default embedding function của Chroma — all-MiniLM-L6-v2, 384 chiều, 
>  chạy local qua ONNX, không cần API key. Truncate ở 256 word-piece, nhỏ, nhanh, thiên 
>  về tiếng Anh — xa mức frontier. Vì chạy ngay không cần config, team thường ship 
>  thẳng lên production mà không nhận ra. Kết quả: recall kém, và không ai giải thích được tại sao." 
>  " Bug thường gặp nhất trong Chroma: tạo collection với embedding_function 
>  riêng, sau đó gọi get_collection() mà không truyền lại nó — default 384 chiều 
>  âm thầm thế chỗ. Luôn truyền cùng embedding_function mỗi lần."

Ba cái bẫy trong một chương, và cả ba cùng một hình dạng: **một mặc định tiện lợi thay thế 
 một lựa chọn có chủ ý, không báo gì.**

| # | Bẫy | Triệu chứng | Chống thế nào |
| --- | --- | --- | --- |
| 10 | Dùng default all-MiniLM-L6-v2 mà không biết | Recall trung bình dai dẳng, "chưa đổi gì cả" | Luôn truyền embedding_function tường minh; assert số chiều |
| 11 | get_collection() thiếu embedding_function | Query trả về rỗng sau khi restart | Bọc việc mở collection trong một hàm duy nhất của bạn |
| — | Truncate ở 256 word-piece | Chunk dài mất đuôi — cùng họ với failure mode 4 | Biết giới hạn model; đếm token trước khi add |

1024 chiều

get_collection()

embedding_function

384 chiều

Điều đáng chú ý là thời điểm nó xảy ra:

ef

process khác

Lỗi không xuất hiện trong lúc phát triển; nó xuất hiện lúc deploy.

Cách chống dứt điểm — một hàm duy nhất:

```text
EF = embedding_functions.SentenceTransformerEmbeddingFunction("BAAI/bge-m3")
DIM = 1024

def open_kb(client, name="lab7_kb"):
    col = client.get_or_create_collection(name, embedding_function=EF)
    probe = EF(["kiem tra so chieu"])[0]
    assert len(probe) == DIM, f"embedding function sai: {len(probe)} != {DIM}"
    return col
```

AssertionError

"Vì chạy ngay không cần config, team thường ship thẳng lên production mà không nhận 
 ra."

thiết kế API

demo

production

Ngày 6

ship một thứ chưa được suy 
 nghĩ

biến lựa chọn ngầm thành lựa chọn tường minh

### Slide 63 Chọn vector store nào — bảy tình huống, và ngưỡng rời Postgres

> Trích slide 
>  "1. Dưới 10k vector, single process, không có ops budget → FAISS Flat trong RAM 
>  hoặc Chroma PersistentClient. Sub-ms. Bỏ qua vector DB. · 2. Đã dùng Postgres, dưới 
>  ~10M vector, index fit RAM → pgvector. Một hệ thống, metadata transactional miễn phí. 
>  · 3. Postgres, 10M–vài trăm triệu → pgvectorscale (StreamingDiskANN). · 4. Filter 
>  phức tạp mà không được mất recall, hoặc ColBERT multi-vector, hoặc per-tenant isolation là 
>  first-class → Qdrant / Weaviate. · 5. Corpus trong lakehouse → Milvus 3.0 External 
>  Collection — vẫn Public Preview, chưa GA. · 6. Workload bursty, cost là ưu tiên số 1 → 
>  turbopuffer / AWS S3 Vectors. · 7. Dạy học / prototype → ChromaDB + FAISS (để thấy 
>  index internals mà Chroma giấu đi)." 
>  "Hai cạm bẫy của đường Postgres: MVCC bloat (mỗi UPDATE là delete+insert — nặng 
>  khi re-embed) và không có filter pushdown vào graph traversal. 
>  Ngưỡng rời Postgres không phải số vector, mà là lúc index không còn fit RAM. "

"Ngưỡng rời Postgres không phải số vector, mà là lúc index không còn fit RAM."

mô-đun bộ nhớ

| 10 triệu vector | Bộ nhớ Flat | Máy 64 GB |
| --- | --- | --- |
| d = 384 (all-MiniLM) | 15,4 GB | Thoải mái |
| d = 1024 (BGE-M3) | 41,0 GB | Vừa, nhưng chật |
| d = 1536 (OpenAI) | 61,4 GB | Không vừa |
| d = 3072 (-3-large full) | 122,9 GB | Không vừa, cần gấp đôi RAM |

Quyết định chọn model ở chương 04 quyết định kiến trúc hạ tầng ở chương 08

quy trình 20 phút

UPDATE

DELETE

INSERT

VACUUM

6 KB mỗi hàng

mô-đun kinh tế

rẻ về tiền API

không rẻ về vận hành

slide 77

chưa đầy đủ

---

<!-- chiron-source-span: {"source_span_id":"7ca2875c-f679-52bc-8a05-e5dc5ad9e257","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 Metadata filter & hybrid search","source_file":"slide-day07.html"},"checksum":"36242da00500f8c2a2450f1284539e8dd9e92fd61b7e18cb0fe7ec65dcab25f8"} -->

## 09 Metadata filter & hybrid search

Chương chứa lỗi production kinh điển nhất của cả Ngày 7 — và deck đưa ra một quan 
 sát thật, có số, trên pgvector. Mô-đun cuối chương tính lại chính con số đó.

### Slide 65 Ba chiến lược filter, ba kiểu hỏng — và 11 dòng thay vì 15

> Trích slide 
>  Post-filter — ANN trên toàn corpus, rồi loại bỏ chunk không khớp → 
>  "Mất recall âm thầm: có thể trả về < k hoặc 0 kết quả nếu filter chọn lọc" 
>  Pre-filter — thu hẹp tập con khớp filter, search trong đó → "Đúng, nhưng 
>  suy biến về brute-force; đồ thị HNSW xây cho toàn corpus phục vụ kém trên subgraph nhỏ" 
>  In-algorithm — traversal của index tự nhận biết filter → "Tốt nhất, nhưng 
>  cần engine hỗ trợ (Qdrant payload-aware HNSW, Weaviate ACORN, Pinecone merged index)" 
>  "Trên pgvector 0.8.0-pg17: truy vấn 15 nearest neighbour màu green chỉ trả về 11 
>  dòng — không exception, không log. Cơ chế vá hnsw.iterative_scan đã tồn tại từ 
>  0.8.0 nhưng mặc định TẮT." 
>  "Cái sai chỉ lộ ra khi filter thật (per-tenant, per-permission) lên production, 
>  không phải trong demo."

Quan sát "15 xin, 11 nhận" là con số cụ thể nhất trong cả chương, và nó giải thích được bằng một mô 
 hình đơn giản. [Mô-đun dưới đây](#m-filter) dựng lại mô hình đó và cho thấy con số 11 không 
 phải ngẫu nhiên.

| Chiến lược | Đúng? | Nhanh? | Hỏng khi nào |
| --- | --- | --- | --- |
| Post-filter | Không — trả thiếu | Nhanh | Filter chọn lọc: fraction nhỏ → gần như luôn trả thiếu |
| Pre-filter | Có | Chậm dần khi tập con nhỏ | Tập con nhỏ: đồ thị HNSW mất tác dụng, suy biến về quét tuyến tính |
| In-algorithm | Có | Nhanh | Không phải engine nào cũng có — đây là ràng buộc chọn sản phẩm, không phải chọn 
 tham số |

Điều tinh tế:

hỏng ngược chiều nhau

lúc chọn vector 
 store

Slide 63

đã có

hnsw.iterative_scan

bản vá đã nằm sẵn trong binary họ đang chạy

đọc release note kỹ

đo recall với filter thật đang dùng

cheatsheet mục 7

#### Tương tác Post-filter làm sập recall — dựng lại quan sát pgvector 11/15

Slide 65 ghi một quan sát thật: xin **15** láng giềng có filter, nhận về **11** dòng, không exception. Mô-đun này mô hình hoá cơ chế đó và trả lời hai câu slide 
 không trả lời: *vì sao đúng là 11*, và *phải lấy bao nhiêu ứng viên mới hết thiếu*.

Mặc định dựng lại đúng tình huống của slide: bạn xin **k = 15**, filter khớp **27,5%** corpus, và index lấy **ef_search = 40** ứng viên trước khi lọc — 
 đây là mặc định của pgvector.

Đoán trước: *(a)* trung bình trả về bao nhiêu dòng? *(b)* xác suất đủ 15 dòng là bao 
 nhiêu? *(c)* phải nâng ef_search lên bao nhiêu để 95% chắc đủ 15?

#### Kéo rồi mở

**(a) Đúng 11,0 dòng.** `40 × 0,275 = 11,0` — khớp chính xác quan sát 
 "11 dòng" của slide 65. Con số đó không phải trùng hợp: nó là *kỳ vọng của phân phối nhị 
 thức*, và mô hình đơn giản nhất có thể đã dự đoán đúng nó.

**(b) Chỉ 11,0%.** Nghĩa là **gần chín trên mười truy vấn trả về thiếu kết 
 quả** — và không truy vấn nào trong số đó báo lỗi. Hệ thống đơn giản trả ít hơn bạn xin, 
 và tầng phía trên coi đó là "không có gì thêm để trả".

**(c) ef_search ≥ 76** — gấp **5,1 lần** k. Đây là con số phải nhớ: 
 với filter chọn lọc, *số ứng viên cần lấy tăng nhanh hơn nhiều so với trực giác*.

**Thử điều đáng thử nhất — kéo độ chọn lọc của filter xuống 5%:** giờ cần **ef_search ≥ 434** để 95% chắc đủ 15 kết quả — gấp **28,9 lần** k. Ở 1%, 
 con số là **≥ 2.185**, gấp **145,7 lần** k. 
 Và đó chính là chỗ post-filter *tự huỷ*: lấy 2.185 ứng viên từ đồ thị HNSW đã gần bằng 
 quét tuyến tính — bạn vừa mất hết lợi ích của ANN, **và vẫn không chắc đủ kết quả**. 
 Đây là lý do slide 65 nói pre-filter "suy biến về brute-force": cả hai đường đều dẫn tới đó, chỉ 
 khác chỗ bạn nhận ra.

*Bài học vận hành:* filter càng chọn lọc thì post-filter càng vô dụng. Và filter thật 
 trên production — **per-tenant, per-permission** — thường cực kỳ chọn lọc: một khách 
 hàng trong một nghìn khách hàng là f = 0,1%. Đó đúng là điều slide cảnh báo: *"chỉ lộ ra khi filter thật lên production, không phải trong demo"* — vì demo chạy trên một 
 tenant duy nhất, nơi f = 100%.

- **Control - k — số kết quả bạn xin: 15 kết quả**: min `1`, max `50`, step `1`, default `15`

- **Control - Filter khớp bao nhiêu corpus: 27,5%**: min `5`, max `1000`, step `5`, default `275`

- **Control - ef_search — ứng viên lấy trước khi lọc: 40 ứng viên**: min `10`, max `400`, step `10`, default `40`

Trung bình trả về

—

—

Xác suất đủ k kết quả

—

—

ef_search cần cho 95%

—

—

Gấp mấy lần k

—

—

filter của bạn filter khớp 30% filter khớp 5% ef_search hiện tại

#### Xem bảng: độ chọn lọc của filter đổi mọi thứ thế nào



#### Công thức & giới hạn của mô hình

- ANN lấy ef ứng viên trên toàn corpus, rồi mới áp filter. Nếu tư cách filter độc 
 lập với thứ hạng similarity thì số sống sót ~ Nhị thức(ef, f), kỳ vọng 
 ef · f.
- P(đủ k) = Σ_{i≥k} C(ef, i) · f^i · (1−f)^(ef−i) — tính bằng log-gamma để không 
 tràn số ở ef lớn.
- Giới hạn ① — giả định độc lập. Thực tế filter thường 
 tương quan với nội dung: tài liệu của một phòng ban cũng nói về chủ đề của phòng ban đó, 
 nên chúng có xu hướng cùng nằm gần query. Khi tương quan dương, thực tế 
 tốt hơn mô hình này; khi tương quan âm (filter theo ngày, theo tenant ngẫu nhiên), 
 thực tế khớp mô hình.
- Giới hạn ② — ef_search không phải chính xác "số ứng viên trả về". 
 Trong HNSW nó là kích thước hàng đợi ưu tiên trong lúc duyệt; số ứng viên thực tế xem xét lớn hơn. 
 Mô hình dùng nó như xấp xỉ bậc nhất — đủ để giải thích quan sát 11/15 và đủ để định hướng, không 
 đủ để dự báo chính xác trên một engine cụ thể.
- Giới hạn ③: mô hình không tính chi phí. Nâng ef_search làm latency tăng gần 
 như tuyến tính — nên "cứ nâng ef lên" không phải giải pháp miễn phí, mà là đổi đồng tiền 
 latency lấy đồng tiền recall, đúng như slide 50 mô tả.
- Giải pháp đúng vẫn là pre-filter hoặc in-algorithm filtering, không phải nâng 
 ef. Mô-đun này tồn tại để cho thấy cái giá của việc không làm thế.

### Slide 66–67 Năm truy vấn, một corpus — và ranh giới dense/BM25

> Trích slide 
>  " my package never showed up " → Dense (doc ghi "shipment did not arrive") 
>  · " can I get my money back " → Dense · " the app crashes when I open 
>  settings " → Dense · " error code E-4471 " → BM25 
>  ("dense trả về mã tương tự nhưng SAI") · " SKU VN-2291-XL " → BM25 
>  ("token ngoài từ vựng huấn luyện — chỉ inverted index tìm ra") 
>  "Truy vấn 1–3: xây dense index. Truy vấn 4–5: giữ BM25 — đó là lý do hybrid search tồn 
>  tại, và vì sao RRF (fuse theo rank, không phải score) là cách kết hợp đúng." 
>  Cú pháp Chroma: where (metadata) dùng $eq $ne $gt $gte $lt $lte $and $or $in 
>  $nin · where_document (full-text) dùng $contains $not_contains $regex 
>  $not_regex, case-sensitive. "Dễ nhầm: $contains cũng tồn tại 
>  bên trong where như toán tử array — khác hoàn toàn với 
>  $contains full-text của where_document."

Bảng năm truy vấn là bài kiểm tra tự đánh giá tốt nhất trong deck. Điều đáng rút ra không phải danh 
 sách, mà **quy tắc phân loại đằng sau nó**:

"Trong truy vấn có chuỗi ký tự nào mà việc sai một ký tự sẽ đổi hoàn toàn ý nghĩa 
 không?"

E-4471

BM25.

VN-2291-XL

BM25.

package never showed up

Dense.

"dense embedding làm nhoè token chính xác"

không phải khuyết điểm

chính xác điều embedding được 
 huấn luyện để làm

Hệ quả thiết kế:

bất kỳ

không phải tuỳ 
 chọn

quy trình 20 phút

$contains

| Viết ở đâu | Nghĩa | Ví dụ |
| --- | --- | --- |
| where_document={"$contains": "E-4471"} | Full-text — nội dung chunk có chứa chuỗi này không | Tìm chunk nhắc tới mã lỗi |
| where={"tags": {"$contains": "urgent"}} | Array membership — metadata dạng list có phần tử này không | Lọc theo nhãn |

case-sensitive

$contains: "e-4471"

"E-4471"

dạng chuẩn hoá Unicode

### Slide 68–69 Hybrid, SPLADE, BGE-M3 — và RRF với con số bị bỏ

> Trích slide 
>  " SPLADE (learned sparse): sparse vector trên vocabulary BERT (~30.522 token) — 
>  nhưng cần forward pass transformer ở cả index-time lẫn query-time (thêm 
>  ~100–300 ms latency), và vẫn không phủ được token ngoài tập huấn luyện 
>  — vì vậy BM25 vẫn giữ chỗ năm 2026." 
>  " BGE-M3: một model xuất cùng lúc dense + sparse + multi-vector, huấn luyện bằng 
>  self-knowledge distillation. 100+ ngôn ngữ, input tới 8.192 token. Vậy 'hybrid chỉ là 3 hệ thống ghép 
>  lại' còn đúng không? Ở SOTA (BGE-M3), không còn đúng nữa. " 
>  RRF: RRF(d) = Σ 1/(k + rank_r(d)), k = 60. 
>  "Fuse theo vị trí rank, không theo score thô — né bài toán chuẩn hoá score chéo hệ 
>  (BM25 và cosine không cùng thang đo). Hỗ trợ native: Elasticsearch · OpenSearch · Weaviate (mặc 
>  định) · Qdrant · ChromaDB." 
>  "' Hybrid tăng accuracy 26–31% so với dense-only ' — số này chỉ xuất hiện trong blog 
>  vendor, không kèm benchmark hay dataset nào. Bỏ số này. Dùng kết luận BEIR: BM25 là 
>  baseline mạnh ngoài miền huấn luyện; kết hợp các họ retrieval mua được robustness, không 
>  phải một% cố định."

không có đơn vị chung

thứ hạng

k = 60

1/61 − 1/62 = 0,00026

nhiều

Đó chính là tính chất bạn muốn:

đồng thuận giữa các 
 họ retrieval

| Con số | Ở đâu | Vấn đề |
| --- | --- | --- |
| "semantic chunking 87% vs 50%" | slide 45 | Không tồn tại trong nguồn nào |
| "chậm hơn 14×" | slide 45 | Đúng, nhưng của Chonkie, không phải của paper |
| "nprobe = 8–16 cho 1–10M vector" | slide 52 | Không có trong docs FAISS hay bài Pinecone |
| "hybrid tăng 26–31%" | slide 69 | Chỉ có trong blog vendor, không có dataset |
| "Qwen3-Embedding 40K token" | slide 47 | Model card ghi 32K |
| "68.32 là điểm MTEB tiếng Anh" | slide 26 | Đó là điểm đa ngôn ngữ; English thật là 73.28 |

Sáu con số trong một deck.

giữ lại

Thói quen nên mang theo:

---

<!-- chiron-source-span: {"source_span_id":"44b647fe-60c3-5ad0-bef1-39a7411b3112","locator":{"kind":"html_section","section_id":"c10","order":12,"heading":"10 Frontier 2025–26 — reranking, long context, và ranh giới","source_file":"slide-day07.html"},"checksum":"4896d49f692f44b4333d69e59be86e7b15693c6552e5aaca5aa1a636cafcf8c0"} -->

## 10 Frontier 2025–26 — reranking, long context, và ranh giới

Chương này chứa một bất đối xứng chi phí quan trọng mà deck nêu bằng lời nhưng không 
 tính ra, và một huyền thoại được bác bỏ bằng bốn nguồn.

### Slide 71 Reranking — và bất đối xứng "một lần / mỗi lần"

> Trích slide 
>  "Bi-encoder (hoặc BM25) lấy top-50/100 rẻ; cross-encoder mã hoá đồng thời 
>  query+passage, rerank xuống top-5/10 thực sự đưa vào prompt." 
>  "Chi phí: O(k) forward pass trên shortlist, không phụ thuộc kích thước corpus N — 
>  index tăng lên hàng triệu tài liệu mà không đổi hoá đơn reranker." 
>  " Bất đối xứng: embedding là chi phí MỘT LẦN mỗi tài liệu; reranking là chi phí LẶP LẠI mỗi 
>  truy vấn. " 
>  " jina-reranker-v3 — listwise, chỉ 0.6B tham số trên backbone 
>  Qwen3-0.6B, xử lý tới 64 tài liệu trong context 131K token, 61.94 
>  nDCG@10 trên BEIR. Điểm dạy: một model listwise vỏn vẹn 0.6B tham số cạnh tranh được làm 
>  câu chuyện 'listwise thắng pointwise' thuyết phục hơn hẳn một con số nDCG đơn lẻ."

Reranking chính là [cross-encoder của slide 15](#s15) quay lại — cùng kiến trúc mà SBERT 
 đã né để đạt 5 giây thay vì 65 giờ. Điểm khác biệt: giờ nó chỉ chạy trên **50 ứng viên** thay vì toàn corpus, nên O(N²) trở thành O(k).

① Không phụ thuộc N.

không đổi

② Sửa đúng chỗ retrieval yếu.

độc lập

③ Trả tiền lại ở MỖI truy vấn.

mô-đun kinh 
 tế

~22.000 token

2,2 tỷ token mỗi tháng

một lần duy nhất

chỉ 4.545 truy vấn là khâu rerank đã tiêu hết ngân sách embed toàn bộ 
 corpus.

"Một model listwise vỏn vẹn 0.6B tham số cạnh tranh được làm câu chuyện 'listwise thắng 
 pointwise' thuyết phục hơn hẳn một con số nDCG đơn lẻ."

cách đọc bằng chứng

một model nhỏ hơn nhiều lần mà vẫn 
 cạnh tranh

phương pháp

#### Tương tác Kinh tế của pipeline retrieval — bốn khâu, và khâu đắt nhất không phải khâu bạn nghĩ

Slide 77 tính chi phí embed ($2 và $13 cho 100M token). Slide 71 nêu bất đối xứng 
 một-lần / mỗi-lần nhưng không tính. Mô-đun này ghép cả hai lại và thêm hai khâu còn thiếu — *embed query* và *token nhồi vào prompt*.

Mặc định: corpus **100M token** (đúng ví dụ slide 77), **100.000 truy 
 vấn/tháng**, rerank top- **50**, nhồi **5** chunk vào prompt, chunk **400 token**, giá embed **$0.02** /1M (= `-3-small` ), giá 
 generation **$1.25** /1M input.

Đoán trước: *(a)* embed toàn corpus tốn bao nhiêu? *(b)* trong chi phí *hàng 
 tháng*, khâu nào chiếm phần lớn nhất, và bao nhiêu phần trăm? *(c)* re-embed toàn corpus 
 khi đổi model tốn bao nhiêu phần trăm của một tháng vận hành?

#### Kéo rồi mở

**(a) $2,00** — khớp chính xác slide 77. Trả một lần, cho toàn bộ 100M token.

**(b) Generation, chiếm 86,9%.** Đây là kết quả đáng nhớ nhất của mô-đun. 
 · embed query: **0,0%** ($0,08/tháng) 
 · rerank top-50: **13,1%** ($44/tháng) 
 · **generation: 86,9%** ($293/tháng) — token nhồi vào prompt mỗi truy vấn 
 
 Nghĩa là: *khâu mà mọi cuộc thảo luận về RAG dành nhiều thời gian nhất — chọn embedding 
 model — chiếm 0,0% chi phí vận hành.* Và khâu gần như không ai đưa vào bảng tính — **số token bạn nhồi vào prompt** — chiếm gần chín phần mười.

**(c) 0,68% của một tháng.** Re-embed bằng model rẻ tốn $2 trên $337 chi phí tháng. 
 Kể cả re-embed bằng `-3-large` ($13) cũng chỉ là **3,9%**. 
 Điều này *chứng minh bằng số* câu kết luận của slide 77: **"Vì rẻ vậy, re-embed 
 toàn corpus khi đổi model là khả thi — không phải lý do né nâng cấp."**

**Thử điều đáng thử nhất — kéo "số chunk nhồi vào prompt" từ 5 xuống 3:** chi phí 
 generation giảm khoảng một phần ba, và đó là *khoản tiết kiệm lớn nhất có thể có trong toàn bộ 
 pipeline*. Đây chính là lý do [reranking](#s71) có ROI cao: nó cho phép bạn nhồi ít 
 chunk hơn **mà không mất chất lượng**, vì 3 chunk đã rerank tốt hơn 5 chunk chưa rerank. 
 Rerank không chỉ cải thiện chất lượng — *nó tự trả tiền cho mình* bằng cách cắt ngân 
 sách generation.

*Bài học vận hành:* hình dạng này giống hệt phát hiện của [Ngày 6](day-06.html) — ở đó API cost chỉ chiếm 5,1% tổng chi phí trong khi ai cũng lo 
 về nó. Cơ chế khác nhau, kết luận giống nhau: **dòng chi được bàn nhiều nhất thường không 
 phải dòng chi lớn nhất.** Cách chữa cũng giống nhau: viết cả bốn dòng ra rồi mới xếp hạng.

- **Control - Corpus: 100M token**: min `5`, max `1000`, step `5`, default `100`

- **Control - Truy vấn mỗi tháng: 100.000 truy vấn/tháng**: min `1`, max `1000`, step `1`, default `100`

- **Control - Shortlist đưa qua reranker: 50 chunk**: min `0`, max `200`, step `5`, default `50`

- **Control - Số chunk nhồi vào prompt: 5 chunk**: min `1`, max `30`, step `1`, default `5`

- **Control - Kích thước chunk: 400 token**: min `64`, max `1200`, step `32`, default `400`

- **Control - Giá embed / rerank: $0,020 / 1M token**: min `5`, max `300`, step `5`, default `20`

- **Control - Giá generation (input): $1.25 / 1M token**: min `10`, max `1500`, step `5`, default `125`

Embed corpus (một lần)

—

—

Chi phí mỗi tháng

—

—

Phần của generation

—

—

Số truy vấn hoà với embed

—

—

embed (corpus + query) rerank generation — token nhồi vào prompt

#### Xem bảng: bốn khâu, nhịp trả tiền, và phần của mỗi khâu



#### Công thức & giới hạn của mô hình

- embed corpus = corpusTok · giá — trả một lần. Giá mặc định $0.02/1M là 
 text-embedding-3-small, lấy từ slide 25.
- rerank = Q · k_shortlist · (chunkTok + queryTok) · giá mỗi tháng.
- generation = Q · (k_inject · chunkTok + queryTok + outTok) · giá, với queryTok = 40 
 và outTok = 300 cố định.
- Giới hạn ① — giá reranker. Mô-đun dùng cùng giá với embedding cho 
 reranker. Đây là cận dưới: reranker là cross-encoder nên đắt hơn embedder trên 
 mỗi token. Nghĩa là phần của rerank trong thực tế cao hơn con số hiển thị — nhưng kết 
 luận (generation chiếm phần lớn) chỉ mạnh thêm khi bạn dùng giá thật.
- Giới hạn ② — giá generation là giả định của tài liệu này, không có trong slide. 
 $1.25/1M input là mức tầm trung năm 2026. Kéo thanh trượt để xem kết luận đổi ra sao — nó vẫn giữ 
 hình dạng cho tới khi giá generation xuống dưới khoảng $0,15/1M.
- Giới hạn ③: bỏ qua chi phí output token (thường đắt hơn input 3–5 lần), chi 
 phí hạ tầng, và prompt caching. Caching có thể cắt mạnh phần generation nếu phần lớn prompt lặp 
 lại — nhưng chunk retrieve được thì không lặp lại giữa các truy vấn khác nhau, nên phần 
 đó không cache được.
- Giới hạn ④: không mô hình hoá chất lượng. Giảm k_inject tiết 
 kiệm tiền và có thể giảm chất lượng — trừ khi bạn bù bằng rerank. Đó chính là đánh đổi mà 
 slide 71 gọi là "ROI cao nhất".

### Slide 72–73 "Long context đã giết chết RAG" — bốn nguồn nói không

> Trích slide 
>  "Nhiều bài viết 2025–26 tựa đề thẳng 'RAG is dead.' Bằng chứng kiểm soát không 
>  ủng hộ. " 
>  Context Rot (Chroma, 7/2025): "Hiệu năng giảm phi tuyến khi 
>  input dài ra, kể cả tác vụ đơn giản." · arXiv:2501.01880: "Long context thắng RAG 
>  hầu hết QA (đặc biệt Wikipedia); RAG thắng hội thoại." · Lost in the 
>  Middle (2307.03172): "Chính xác hình chữ U — tệ nhất ở giữa. Tăng k không 
>  rerank có thể tệ hơn." · CAG (2412.15605, WWW'25): "Nạp toàn corpus, 
>  KV-cache một lần — nhưng phải vừa context window." 
>  "Tổng hợp 2026: Vector retrieval thu hẹp corpus lớn, giao tập con cho long-context model 
>  suy luận (đồng thuận thực hành, không phải kết luận 2501.01880)." 
>  Slide 73: "Day 7 = đưa dữ liệu vào đúng hình dạng. Day 8 = dùng nó để 
>  trả lời. Tầng dữ liệu sai thì không kỹ thuật nào ở Day 8 cứu được. "

đầu

cuối

giữa

"tăng k không rerank có thể tệ hơn"

bảng slide 78

"chất lượng câu trả lời giảm khi tăng 
 k"

Vì sao rerank sửa được:

mô-đun kinh tế

rerank rồi nhồi 3 chunk tốt hơn nhồi thẳng 10 chunk — vừa chính xác hơn, vừa rẻ hơn.

"Long context thắng RAG hầu hết QA (đặc biệt 
 Wikipedia); RAG thắng hội thoại."

thật sự tốt hơn

chống lại

Ranh giới thực dụng rút ra:

| Tình huống | Chọn |
| --- | --- |
| Corpus vừa context window, hỏi–đáp một tài liệu | Nạp thẳng (hoặc CAG với KV-cache) — RAG là phức tạp thừa |
| Corpus lớn hơn context window nhiều lần | Retrieval thu hẹp trước, rồi giao cho long-context |
| Hội thoại nhiều lượt | RAG — theo chính 2501.01880 |

Context Rot

phi tuyến

"Tầng dữ liệu sai thì không kỹ thuật nào ở Day 8 cứu được."

Unicode vẫn chưa chuẩn hoá

slide 2

2,06×

những gì retrieval đã trả về

---

<!-- chiron-source-span: {"source_span_id":"21839917-ab9f-5c9a-a0f0-301958cedb14","locator":{"kind":"html_section","section_id":"c11","order":13,"heading":"11 Đo lường, chi phí & failure mode","source_file":"slide-day07.html"},"checksum":"a02e652e9b119db72b422349479b83cbee0945161c205af60f014ba9148fbdd4"} -->

## 11 Đo lường, chi phí & failure mode

Chương chốt của Ngày 7, và nó chứa hai thứ đáng mang đi làm nhất: một công thức làm 
 eval set không cần nhãn, và một bảng 14 dòng nên in ra dán tường.

### Slide 75 Bốn metric, và câu "recall@k cần nhưng chưa đủ"

> Trích slide 
>  " Recall@k: bao nhiêu doc relevant nằm trong top-k — upper-bound cho chất 
>  lượng câu trả lời cuối cùng · Precision@k: kiểm soát nhiễu, context budget · 
>  nDCG@k: thứ hạng tốt không (log-discount theo vị trí) · MRR: vị trí 
>  nghịch đảo kết quả relevant đầu tiên" 
>  " Luôn thêm BM25 làm sàn: dense model fine-tune trên MS MARCO có thể thua BM25 thô 
>  ngoài miền huấn luyện (BEIR: 18 dataset, 9 tác vụ)." 
>  " Recall@k cần nhưng chưa đủ. Đúng passage ở rank 18/20 vẫn có thể ra câu trả lời 
>  sai — lost-in-the-middle. Recall giới hạn cái có thể xảy ra; precision/nDCG/reranker quyết 
>  định cái thực sự xảy ra. "

Câu cuối là cách phát biểu chính xác nhất về vai trò của recall mà tài liệu này gặp trong cả series, 
 và nó xứng đáng được mở rộng thành một quy tắc chọn metric:

| Bạn đang hỏi | Dùng metric | Vì sao |
| --- | --- | --- |
| "Pipeline có khả năng trả lời đúng không?" | Recall@k | Bằng chứng không có trong top-k thì mọi thứ sau đó vô ích. Đây là trần |
| "Bằng chứng có ở vị trí model chú ý không?" | nDCG@k hoặc MRR | Phạt việc đặt đúng passage ở rank 8 thay vì rank 1 — đúng vấn đề lost-in-the-middle |
| "Context có bị pha loãng không?" | Precision@k | Nhiễu trong prompt vừa tốn tiền vừa làm model phân tâm |
| "Hệ thống có tốt hơn không làm gì không?" | BM25 baseline | Sàn bắt buộc. Không có nó thì "85% recall" không có ý nghĩa so sánh |

rank_bm25

① Dense thắng rõ.

② Xấp xỉ nhau.

③ BM25 thắng.

nhóm truy vấn 4–5 của slide 67

"build Flat trước"

### Slide 76 Làm eval set KHÔNG cần nhãn — năm bước, và hai thiên lệch phải nói ra

> Trích slide 
>  "Mục tiêu: đo recall@k trên corpus của chính mình, trong một buổi, không cần ai gán nhãn 
>  tay." 
>  "1. Sample chunk theo tỉ lệ giữa các loại tài liệu ( N ≥ 100 để ước lượng có ý 
>  nghĩa). 2. Sinh câu hỏi bằng LLM, chỉ dựa trên đúng chunk đó, kèm persona ('khách so 
>  gói cước', 'kiểm toán viên nội bộ'). 3. Nhãn: chunk nguồn chính là positive — mẹo 
>  citation-as-weak-label. 4. Chạy retrieval, tính recall@k và MRR. 5. Người kiểm tra tay 
>  ~10% để loại câu hỏi vô nghĩa hoặc quá dễ." 
>  "Hai thiên lệch phải nói rõ: (1) câu hỏi LLM sinh lặp lại đúng từ ngữ của chunk — 
>  thổi phồng recall@k so với người dùng thật; (2) cách này chỉ đo được 'có tìm lại đúng chunk 
>  đã sinh câu hỏi không' — thiên về trùng từ khoá. Đây là floor check, không thay thế 
>  nhãn thật. "

Đây là kỹ thuật đáng mang đi làm nhất của cả Ngày 7, vì nó gỡ bỏ lý do phổ biến nhất khiến không ai 
 đo retrieval: *"chúng ta không có dữ liệu gán nhãn."*

một

là

recall đo được là ước lượng dưới

mục đích của con số này là để so sánh

chênh lệch

```text
KHONG persona
  chunk: "Khach hang co 30 ngay ke tu ngay nhan hang de yeu cau doi tra."
  cau hoi sinh ra: "Khach hang co bao nhieu ngay de yeu cau doi tra?"
  -> trung gan het tu khoa. recall se cao gia tao.

CO persona "khach hang buc minh, khong biet thuat ngu"
  cau hoi sinh ra: "Mua hom truoc gio muon tra lai co duoc khong,
                    lau qua roi thi sao?"
  -> khong trung tu nao. Day moi la thu do duoc kha nang xu ly
     vocabulary mismatch (slide 13).
```

Gợi ý thực dụng:

hai

thước đo mức độ hệ thống của bạn phụ thuộc vào trùng từ khoá

10 câu hỏi

Câu hỏi vô nghĩa

tiện thể kiểm tra chất lượng chunking

Câu hỏi quá dễ

cảm giác về việc corpus của bạn 
 thật sự chứa gì

### Slide 77 Chi phí embedding — rẻ hơn sinh viên tưởng, và hệ quả chiến lược

> Trích slide 
>  " $2 — corpus 100M token, -3-small ($0.02/1M), một lần duy 
>  nhất. $13 — cùng corpus, -3-large ($0.13/1M token)." 
>  "100M token ≈ 75M từ — cỡ document store doanh nghiệp vừa. Rẻ hơn generation 2–3 bậc độ 
>  lớn. " 
>  "Hệ quả chiến lược: Vì rẻ vậy, re-embed toàn corpus khi đổi model là khả thi — không phải 
>  lý do né nâng cấp. "

Câu "rẻ hơn generation 2–3 bậc độ lớn" là khẳng định duy nhất trong slide không kèm phép tính. [Mô-đun kinh tế](#m-cost) kiểm nó và kết quả còn mạnh hơn slide nói:

| Khâu | Nhịp trả tiền | Chi phí ở cấu hình mặc định | Phần của chi phí tháng |
| --- | --- | --- | --- |
| Embed corpus | Một lần | $2,00 | — |
| Embed query | Mỗi truy vấn | $0,08/tháng | 0,0% |
| Rerank top-50 | Mỗi truy vấn | $44/tháng | 13,1% |
| Generation | Mỗi truy vấn | $293/tháng | 86,9% |

① Đừng chọn embedding model theo giá.

bảng slide 25

chất lượng retrieval trên corpus của bạn

quy trình 20 phút

② Nâng cấp model không có rào cản tài chính.

3,9%

rào cản vận hành

③ Chỗ tối ưu chi phí thật là số token nhồi vào prompt.

chunk size

k

rerank

một con số đúng dẫn tới ba quyết định

1 từ ≈ 1,33 token

tiếng Anh

tiếng Việt thì tỉ lệ cao hơn đáng kể

ước lượng chi phí cho corpus tiếng Việt bằng tỉ lệ tiếng Anh sẽ 
 thấp hơn thực tế.

giới hạn token của model

max input 512

Cách làm đúng:

### Slide 78–80 Bảng 14 failure mode, và luận đề của cả bài

> Trích slide 
>  1 "xe hơi" bỏ sót "ô tô" → lệch từ vựng → hybrid + RRF · 2 mã 
>  E-4471 trả về mã khác → dense làm nhoè token → thêm BM25 · 3 recall thấp hơn 5–15%, 
>  không lỗi → thiếu prefix → prefix-ablation test · 4 đuôi chunk không bao giờ khớp → 
>  silent truncation → đếm token trước khi embed · 5 ranking sai lệch 
>  toàn index → đổi model không re-embed → rebuild toàn bộ, version hoá index · 6 FAISS 
>  ưu tiên document dài → quên normalize_L2 · 7 filtered search trả về ít 
>  hơn k → post-filtering → pre-filter hoặc in-algorithm 
>  8 chất lượng giảm khi tăng k → over-retrieval + lost-in-the-middle → rerank · 
>  9 recall dao động giữa loại tài liệu → sai chunk size → tinh chỉnh mỗi khi đổi model 
>  · 10 recall trung bình dai dẳng → Chroma default all-MiniLM-L6-v2 · 
>  11 query rỗng sau restart → lệch embedding function · 12 latency 
>  tăng dần → HNSW tombstone → compaction định kỳ · 13 cache trả lời 
>  sai một cách tự tin → cache key không version theo model · 14 demo tốt production tệ 
>  → eval overfit cách diễn đạt của nguồn 
>  " 6/14 failure mode ở bảng trên hoàn toàn không raise exception nào. Một pipeline 
>  retrieval có thể trả HTTP 200, không log lỗi, không stacktrace — và vẫn hoàn toàn sai. Đây là myth 
>  phổ biến nhất và cũng là luận điểm cốt lõi: 'nếu nó không báo lỗi thì nó chạy đúng' là 
>  sai." 
>  "Antidote duy nhất: đo recall@k trên ground truth và benchmark BM25 làm sàn — đừng suy 
>  luận từ việc hệ thống không crash. "

| Cách phát hiện | Dòng | Chi phí kiểm |
| --- | --- | --- |
| Assert lúc index / khởi động | 3 (prefix) · 4 (truncation) · 
 10, 11 (embedding function) | Vài dòng code, một lần |
| So với Flat ground truth | 5 (không re-embed) · 6 (normalize) · 
 7 (post-filter) | Một lần build Flat |
| Chỉ thấy khi đo recall trên eval set | 1, 2 (từ vựng, mã) · 
 9 (chunk size) · 14 (overfit) | Một buổi, theo slide 76 |
| Chỉ thấy qua monitoring theo thời gian | 12 (tombstone) · 
 13 (cache) | Dashboard latency + tỉ lệ cache hit |
| Chỉ thấy khi đọc câu trả lời cuối | 8 (lost-in-the-middle) | Chấm tay, hoặc LLM-as-judge — Ngày 8 |

tôi phải xây gì để những lỗi 
 này không im lặng nữa?

vài dòng assert

một index 
 Flat

một bộ eval 100 câu

một dashboard bốn chỉ số

"Cache trả lời sai một cách tự tin. Cache key không version theo embedding model, hoặc thiếu 
 TTL."

kém đi

sai một cách bền 
 vững

Version theo embedding model

TTL theo độ biến động của fact

chương bảo mật

cache là chỗ duy nhất trong pipeline mà một lỗi 
 nhất thời trở thành lỗi vĩnh viễn.

---

<!-- chiron-source-span: {"source_span_id":"2ffad5b8-a670-596e-9da6-c802617c332e","locator":{"kind":"html_section","section_id":"c12","order":14,"heading":"12 Bảo mật, Lab 7 & tổng kết","source_file":"slide-day07.html"},"checksum":"089c4804d7041f041093d535b4392a4b3007b400ece6299ba33723c7b25c0903"} -->

## 12 Bảo mật, Lab 7 & tổng kết

Chương này lật ngược một giả định mà gần như ai cũng mang theo: *vector chỉ là số 
 thực, nên nó vô hại.* Ba dòng nghiên cứu nói ngược lại.

### Slide 82 Vector KHÔNG phải dữ liệu đã ẩn danh — ba bước leo thang

> Trích slide 
>  " 2020 — Song & Raghunathan: khôi phục một phần bag-of-words từ 
>  embedding. EMNLP 2023 (Morris et al., arXiv:2310.06816), Text Embeddings Reveal 
>  (Almost) As Much As Text — khôi phục câu gần như nguyên văn. 2025 
>  — ALGEN (arXiv:2502.11308): không gian embedding của các encoder khác nhau gần như isomorphic 
>  ở mức câu ⇒ một phép linear alignment, học từ chỉ ~1.000 mẫu rò rỉ, đảo 
>  ngược được embedding black-box, transfer xuyên domain và ngôn ngữ." 
>  " Membership Inference — không cần khôi phục nội dung, chỉ cần biết 
>  một passage có tồn tại trong retrieval DB hay không (Anderson et al., 
>  arXiv:2405.20446). Riêng sự hiện diện đã nhạy cảm: 'hệ thống RAG của bệnh viện này có hồ sơ nhắc 
>  đến bệnh hiếm X'." 
>  " Không thể coi vector-only index là dữ liệu đã de-identify. Inversion rò rỉ 
>  nội dung; membership inference rò rỉ sự hiện diện. Nếu văn bản gốc nhạy 
>  cảm, vector của nó cũng nhạy cảm. "

Ba mốc này là một đường leo thang rõ ràng, và mốc 2025 là mốc đổi bản chất vấn đề:

| Năm | Khôi phục được gì | Cần gì để tấn công | Ý nghĩa thực tế |
| --- | --- | --- | --- |
| 2020 | Một phần túi từ | Truy cập model | Đáng lo về lý thuyết |
| 2023 | Câu gần như nguyên văn | Truy cập model | Vector = văn bản, với ai có model |
| 2025 (ALGEN) | Câu, từ embedding black-box | ~1.000 mẫu rò rỉ, không cần biết model | Vector = văn bản, với gần như bất kỳ ai lấy được index |

biết model nào đã tạo ra vector

gần như isomorphic

~1.000 cặp (văn bản, vector) bị rò rỉ

transfer xuyên domain và ngôn ngữ

Hệ quả cho mô hình đe doạ của bạn:

slide 9

trước

"Mask trước khi embed — không bao giờ lưu raw PII trong vector 
 store."

nội dung

một tài liệu có nằm trong index hay không

"hệ thống RAG của bệnh viện này có hồ sơ nhắc đến bệnh 
 hiếm X"

Trong cả ba, sự hiện diện là toàn bộ thông tin.

### Slide 83–84 Kênh retrieval là một đường tấn công — và filter quyền phải nằm TRONG ANN

> Trích slide 
>  Corpus poisoning (PoisonedRAG) — Zou et al., arXiv:2402.07867, USENIX Security 
>  2025: " 90% attack success rate khi văn bản độc được tối ưu đồng thời để 
>  được retrieve và để lái câu trả lời. Điều kiện: 5 văn bản độc cho MỖI câu hỏi mục 
>  tiêu — không phải '90% với 5 tài liệu' nói chung. Phòng thủ rẻ: perplexity 
>  filtering (văn bản bị tối ưu thường có PPL cao)." 
>  Indirect prompt injection: "Vô hình với bộ lọc chỉ kiểm tra input của user — 
>  payload đến qua kênh retrieval. Nội dung retrieve được ngầm tin cậy 
>  vì đến từ pipeline của chính hệ thống. Blast radius nhân bản: một tài liệu độc ảnh 
>  hưởng mọi user tương lai." 
>  Slide 84: " Yêu cầu kiến trúc, không phải tính năng thêm: filter theo quyền của user 
>  TRƯỚC hoặc TRONG lúc chạy ANN search — không bao giờ chỉ filter sau. Vector DB không kế 
>  thừa permission của data store gốc ⇒ vector index là mục tiêu tái định danh tập trung."

MỖI câu hỏi mục tiêu

chọn trước câu hỏi mục tiêu

từng

có hình dạng

trích con số kèm điều kiện của 
 nó.

input của người dùng

chỉ có một đường vào

nội dung retrieve được cũng đi vào prompt

Vô hình với bộ lọc input

Bị tin cậy mặc định

Blast radius nhân bản

"Day 7 chỉ cần thấy kênh retrieval là một đường tấn công"

từ lúc thiết kế pipeline

"Filter theo quyền của user TRƯỚC hoặc TRONG lúc chạy ANN search — không bao giờ chỉ filter sau."

Chương 09

làm mất recall

Mô-đun filter

157 lần k

filter quyền

ANN đã duyệt qua tài liệu người dùng không được xem

Về mặt bảo mật, đó là một khác biệt thật.

post-filter vừa sai về chất lượng vừa sai về bảo mật, và cả hai đều im 
 lặng.

slide 63 mục 4

_Sơ đồ: Kênh retrieval như một bề mặt tấn công: hai đường vào và hai đường rò rỉ - Ở giữa là pipeline năm bước: nguồn tài liệu, chunk và embed, vector index, retrieve top-k, và prompt gửi cho agent. Phía trên là hai đường tấn công đi vào. Thứ nhất là corpus poisoning, theo PoisonedRAG đạt chín mươi phần trăm tỉ lệ thành công khi dùng năm văn bản độc cho mỗi câu hỏi mục tiêu, và nó đi vào ở bước nguồn tài liệu; phòng thủ rẻ là lọc theo perplexity. Thứ hai là indirect prompt injection, chỉ dẫn độc nằm trong tài liệu được retrieve nên vô hình với bộ lọc chỉ kiểm input của người dùng, và nó đi vào ở bước prompt. Phía dưới là hai đường rò rỉ đi ra. Thứ ba là embedding inversion, khôi phục văn bản gần như nguyên văn từ vector, theo Morris năm 2023 và ALGEN năm 2025 vốn chỉ cần khoảng một nghìn mẫu rò rỉ và hoạt động với embedding black-box; nó rò ra từ vector index. Thứ tư là membership inference, chỉ cần biết một passage có tồn tại trong cơ sở dữ liệu hay không, và riêng sự hiện diện đã nhạy cảm; nó rò ra từ bước retrieve. Dải cuối ghi hai quy tắc: filter theo quyền phải nằm trước hoặc trong đường đi ANN chứ không bao giờ chỉ ở bước dọn dẹp cuối, và nếu văn bản gốc nhạy cảm thì vector của nó cũng nhạy cảm._

Hình 3 — Kênh retrieval là bề mặt tấn công hai chiều.

slide 82

84

đặt cả bốn lên cùng một pipeline

### Slide 85 PDPL 91/2025 và GDPR — vector có phải dữ liệu cá nhân?

> Trích slide 
>  PDPL 91/2025 (VN): "Hiệu lực 1/1/2026; 'tailored safeguards' cho 
>  AI/big data/cloud; bảo vệ riêng biometric data; báo vi phạm trong 72h." — Câu hỏi 
>  mở: "Embedding của dữ liệu cá nhân có invertible — có thuộc phạm vi PDPL dù 'trông chỉ là số'? 
>  Chưa có hướng dẫn. " 
>  GDPR (EU): "Recital 26: test là re-identification có 'reasonably 
>  likely' hay không; pseudonymized vẫn là personal data (Art. 4(5))." — " 
>  Literature về inversion từ 2025 trả lời có ⇒ coi embedding đã lưu là 
>  pseudonymized, không phải anonymized." 
>  "Khung nghĩ đúng cho sản phẩm: Lưu embedding của dữ liệu cá nhân thì hãy thiết kế như đang 
>  lưu chính dữ liệu đó — về mặt kỹ thuật, gần như là vậy. "

①

anonymized

không "reasonably likely"

②

là

③

pseudonymized

vẫn là dữ liệu cá nhân

Hệ quả vận hành, cụ thể:

khả năng xoá theo yêu cầu

giới hạn kỹ thuật của FAISS

IndexHNSWFlat

remove_ids()

Đây là chỗ chương 07 và chương 12 gặp nhau, và deck không nối hai chỗ đó lại.

Chắc chắn:

1/1/2026

72 giờ

Chưa rõ:

"chưa có hướng dẫn"

thiết kế như thể câu trả lời là "có"

mask PII trước khi embed

Tài liệu này ghi rõ: đây là lập luận kỹ thuật–pháp lý theo đúng cách deck trình bày, 
 không phải tư vấn pháp lý. Slide cũng ghi chú như vậy, và nói thêm rằng chưa có phán quyết ràng buộc 
 riêng cho embedding.

### Slide 88–92 Lab 7 — bốn bước, và bước 4 là bước phân biệt

> Trích slide 
>  "Mục tiêu: nối một bộ dữ liệu riêng (FAQ/SOP/policy) vào pipeline chunk → embed → store → 
>  retrieve → inject tối thiểu nhưng đúng bản chất, rồi tự đo recall@5 bằng no-labels 
>  recipe — không đoán mà đo." 
>  Deliverable: "Script chunk + embed + index chạy được, demo semantic search với ≥3 câu hỏi test, 
>  một mini answer function dùng retrieved context, và một con số recall@5 kèm 1–2 failure case 
>  tự tìm ra." 
>  Code: RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50, separators=["\n\n", 
>  "\n", ". ", " ", ""]) · PersistentClient + EF tường minh 
>  BAAI/bge-m3 · where={"category": {"$eq": "support"}} — 
>  metadata filter TRƯỚC ANN · recall_at_k với 
>  citation-as-weak-label.

chạy được pipeline

hiểu nó hỏng thế nào

①

②

bốn câu hỏi chẩn đoán của Hình 1

③

bảng failure mode

| Dòng code | Nó chống failure mode nào |
| --- | --- |
| model_name="BAAI/bge-m3" — EF tường minh | Dòng 10 và 11: default 384 chiều âm thầm thế chỗ 
 ( slide 61 ) |
| where={"category": {"$eq": "support"}} — chú thích "TRƯỚC ANN" | Dòng 7: post-filter trả về ít hơn k ( slide 65, 
 mô-đun filter ) |
| chunk_overlap=50 trên chunk_size=400 — 12,5% | Mất ngữ cảnh tại điểm cắt ( slide 44, mức 10–20% mà deck khuyến nghị) |

không

col.add()

### Slide 93–95 Bốn takeaway, và bài tập về nhà là một bài tập xoá

> Trích slide 
>  " 1 'Không lỗi' không có nghĩa là 'đúng.' 6/14 failure mode học 
>  hôm nay không hề raise exception — luận đề thật sự của Day 07. 2 
>  Data quality thường quan trọng hơn đổi sang model đắt hơn — pipeline tốt giải quyết 
>  phần lớn vấn đề trước. 3 Embedding dịch ngôn ngữ sang không gian so sánh được nghĩa — 
>  cosine là quy ước, không phải chân lý. 4 Retrieval pipeline là cầu 
>  nối từ dữ liệu riêng tới câu trả lời grounded — luôn đo recall trước khi đổ lỗi cho model."

Rà lại knowledge base của nhóm, bỏ 20% nội dung nhiễu nhất

chunk_size

chunk_overlap

bài tập xoá

thêm

Vì sao xoá lại làm recall tăng:

không mất gì

Cách chọn "20% nhiễu nhất" mà không phải đoán:

slide 40

① Không lỗi ≠ đúng

"đo bằng gì?"

② Data quality > model đắt hơn

"chúng ta đã bóc text đúng chưa, chunk đúng chưa?"

③ Cosine là quy ước

④ Luôn đo recall trước khi đổ lỗi cho model

"bằng chứng đúng có nằm trong top-k 
 không?"

Hình 1

---

<!-- chiron-source-span: {"source_span_id":"28a1a6bf-9186-503e-bef0-2fff313634a1","locator":{"kind":"html_section","section_id":"ladder","order":15,"heading":"▤ Luyện kỹ năng cốt lõi: chẩn đoán một pipeline hỏng im lặng","source_file":"slide-day07.html"},"checksum":"aef04553f1f1e9a2777110fe57bbd5b1c0fc32e20729648f11bddd60d9ff1b54"} -->

## ▤ Luyện kỹ năng cốt lõi: chẩn đoán một pipeline hỏng im lặng

Ba bài giảm dần giàn giáo. Kỹ năng được luyện là kỹ năng Ngày 7 tồn tại để dạy: *không có exception nào, vẫn phải tìm ra chỗ hỏng.*

① Text gốc có đúng không?

② Chunk đúng có trong index 
 không?

③ Nó có trong top-k không?

④ Có trong top-k mà trả lời vẫn sai?

#### Trợ lý chính sách nội bộ. Nhân viên hỏi 
 "nghỉ phép năm chưa dùng hết thì sao?" — bot trả lời "Không có thông tin". Nhưng bạn 
 biết chắc chính sách đó có trong file chinhsach_nhansu_2026.pdf, trang 14

Đọc cách *khoanh vùng*, không chỉ đáp án.

1. Câu ① — mở chunk ra đọc, và đọc bằng mắt. Tìm mọi chunk có 
 metadata.source == "chinhsach_nhansu_2026.pdf" và page == 14. 
 Nếu không có chunk nào: lỗi ở khâu parse hoặc provenance — dừng ở đây, đừng đụng tới 
 retrieval. Kiểm xem trang 14 có phải trang scan không ( slide 31 ), có phải 2 cột 
 không, và provenance có được giữ từ lúc parse không. 
 Nếu có chunk nhưng nội dung là rác ("Điề u kho ản ngh ỉ ph ép…"): đây là lỗi OCR hoặc 
 thiếu chuẩn hoá NFC. Cũng dừng ở đây. 
 Giả sử tìm thấy chunk và nội dung đọc được đúng. Sang câu ②.
2. Câu ② — chunk có trong index không, và nó có ĐÚNG số chiều không. 
 rec = col.get(ids=[chunk_id], include=["embeddings", "documents"]) 
print(len(rec["embeddings"][0])) # phai la 1024 voi BGE-M3 
print(len(EF([rec["documents"][0]])[0])) # encode lai NGAY BAY GIO 
 Hai con số này phải bằng nhau. Nếu vector lưu là 1024 mà encode lại ra 384 → 
 failure mode 10/11: embedding function đã bị thay bằng default. 
 Nếu bằng nhau nhưng giá trị khác nhau nhiều → failure mode 5: đã đổi model 
 mà không re-embed. 
 Đây là hai lỗi phổ biến nhất và cả hai được loại bỏ trong ba dòng code.
3. Câu ③ — nó ở hạng mấy? Và đây là chỗ phải cẩn thận với filter. Chạy retrieval 
 hai lần: một lần không filter, một lần với đúng filter production 
 đang dùng. 
 Không filter thì thấy, có filter thì mất → failure mode 7. Đây chính 
 là trường hợp mô-đun post-filter mô tả: xin k, nhận ít hơn k, không lỗi. 
 Kiểm ngay len(res["ids"][0]) — nếu nó nhỏ hơn n_results bạn xin, bạn vừa 
 xác nhận được lỗi. 
 Cả hai lần đều không thấy trong top-20 → sang bước 4.
4. Vẫn ở câu ③, nhưng giờ là lỗi xếp hạng — bốn nghi phạm, kiểm theo thứ tự rẻ dần. 
 a) Prefix. Có dùng query: / passage: không, và có 
 dùng cả hai phía không? Chạy prefix-ablation: encode query có và không có prefix, so thứ 
 hạng. (failure mode 3 — slide 21 ) 
 b) Truncation. len(tokenizer.encode(chunk_text)) — có vượt max 
 input của model không? Nếu chunk 900 token trên model 512, câu trả lời nằm ở phần đuôi đã biến mất. 
 (failure mode 4 — slide 47 ) 
 c) Vocabulary mismatch. Câu hỏi dùng "nghỉ phép năm", tài liệu viết "ngày phép 
 tồn". Chạy BM25 xem có tìm ra không — nếu BM25 cũng không, thì đúng là lệch từ vựng và cần 
 hybrid. (failure mode 1) 
 d) Chunk size. Câu hỏi factoid ngắn nhưng chunk 1.000 token → nội dung bị pha 
 loãng. (failure mode 9 — slide 43 )
5. Kết luận và ghi lại theo mẫu — phần này mới là phần được chấm. Giả sử bước 4a 
 cho kết quả: không có prefix ở phía query. 
 FAILURE CASE #1 
 Trieu chung: "Khong co thong tin" cho cau hoi co dap an trong corpus 
 Khoanh vung: cau (3) — chunk co trong index, dung so chieu, 
 nhung khong lot top-20 
 Nguyen nhan: thieu prefix "query:" o phia truy van (E5-style model) 
 Bang chung: prefix-ablation — co prefix: hang 2 | khong prefix: hang 34 
 Dong trong bang: #3 (slide 78) 
 Cach sua: boc encode() trong ham rieng, prefix nam ben trong ham 
 Do bang: recall@5 tren bo eval 100 cau, truoc/sau 
 Ket qua: 0,71 -> 0,79 
 Bảy dòng. Dòng bằng chứng là dòng phân biệt một chẩn đoán với một phỏng đoán — nó ghi lại 
 phép thử cụ thể đã chạy và con số nó cho ra.

#### Hệ thống chạy tốt ba tháng. 
 Tuần này, đội hạ tầng nâng chromadb lên bản mới và đồng thời team đổi embedding 
 model từ all-MiniLM-L6-v2 sang BAAI/bge-m3. Sau khi deploy: recall@5 tụt từ 
 0,78 xuống 0,12, và một số truy vấn trả về rỗng

Gợi ý ở mỗi bước; hãy tự viết trước khi mở đáp án.

1. Trước khi chẩn đoán bất cứ gì — vấn đề về phương pháp là gì? 
 Gợi ý: hai thay đổi cùng lúc. Điều đó ảnh hưởng thế nào tới khả năng quy kết nguyên nhân?
2. Con số 0,12 và "trả về rỗng" — hai triệu chứng này gợi ý gì? 
 Gợi ý: 0,12 không phải "kém hơn một chút". Nó gần với mức ngẫu nhiên. Và "rỗng" là triệu chứng 
 của đúng một dòng trong bảng 14 dòng.
3. Chạy phép kiểm ba dòng của Bài 1 bước 2 — bạn kỳ vọng thấy gì? 
 Gợi ý: 384 và 1024.
4. Có ai đã re-embed corpus chưa? 
 Gợi ý: failure mode 5. Cosine giữa hai không gian vẫn tính được — nó chỉ vô 
 nghĩa.
5. Viết quy trình để lần sau không tái diễn. 
 Gợi ý: một assert, một quy tắc về deploy, và một thứ lưu trong metadata của 
 collection.

#### Đối chiếu sau khi đã tự viết

**① Lỗi phương pháp: hai thay đổi cùng một lần deploy.** Không thể quy kết nguyên 
 nhân — có thể là bản Chroma mới, có thể là model mới, có thể là tương tác giữa hai cái. 
 Việc đầu tiên *không* phải chẩn đoán mà là **rollback một trong hai**, hoặc 
 dựng lại môi trường cũ và đổi từng thứ một. Đây là kỷ luật cơ bản nhưng bị bỏ thường xuyên nhất khi 
 hệ thống đang hỏng và mọi người vội.

**② Hai triệu chứng chỉ về hai dòng khác nhau, và cả hai đều là lỗi lệch cấu hình 
 embedding.** 
 · **recall 0,12** — gần mức ngẫu nhiên, nghĩa là vector query và vector document *không cùng một không gian*. Đây là **failure mode 5**. 
 · **trả về rỗng** — **failure mode 11**, lệch số chiều giữa lúc tạo và 
 lúc mở collection ( [slide 61](#s61) ). 
 Việc có *cả hai* triệu chứng là dấu hiệu mạnh: index vẫn chứa vector 384 chiều cũ, trong 
 khi code query giờ sinh vector 1024 chiều.

**③ Phép kiểm cho: vector lưu 384 chiều, encode lại ra 1024.** Xác nhận giả thuyết 
 trong ba dòng code, không cần đọc thêm log nào.

**④ Không ai re-embed.** Đây là nguyên nhân gốc. Đổi embedding model **không phải** một thay đổi cấu hình — nó là một thay đổi *dữ liệu*. Mọi vector 
 trong index phải được sinh lại. 
 Và [theo mô-đun kinh tế](#m-cost), việc đó tốn **$2** cho corpus 100M 
 token — *0,68% của một tháng vận hành*. Sự cố này không xảy ra vì chi phí; nó xảy ra vì **không ai biết là cần**.

**⑤ Ba biện pháp, theo thứ tự hiệu lực:** 
 **a)** *Lưu cấu hình embedding vào metadata của collection* — tên model, số 
 chiều, prefix, ngày index. Và `assert` nó lúc mở collection (xem [hàm `open_kb`](#s61) ). Điều này biến cả failure mode 5, 10 và 11 thành một `AssertionError` lúc khởi động. 
 **b)** *Một thay đổi mỗi lần deploy* — hoặc ít nhất, không bao giờ gộp thay 
 đổi hạ tầng với thay đổi model. 
 **c)** *Đưa recall@5 vào smoke test sau deploy*. Bộ eval 100 câu chạy trong 
 vài giây; nếu nó rơi từ 0,78 xuống 0,12 thì deploy tự động dừng. Đây chính là *quality gate* mà [Ngày 5](slide-day05.html) gọi tên trong eval flow ba giai đoạn.

*Ghi chú:* cả ba biện pháp cộng lại mất chưa tới một ngày công. Sự cố này — recall tụt 85% 
 trên production — gần như chắc chắn tốn nhiều hơn thế.

#### Lấy corpus của chính bạn. Dựng bộ eval 
 no-labels 100 câu theo slide 76, đo recall@5, tìm 2 failure case, ánh xạ chúng vào 
 bảng 14 dòng, và sửa một cái

Không có đáp án — nhưng có bảng tự chấm.

Flat / exact search

BM25 làm sàn

≥ 100 câu

persona

với filter thật đang dùng

len(res["ids"][0])

assert

Tôi đã đếm token của chunk dài nhất và so với max input của model

chuẩn hoá NFC

ánh xạ được

đo lại

---

<!-- chiron-source-span: {"source_span_id":"fcd1b58b-4016-5fcc-9e95-6157c9003966","locator":{"kind":"html_section","section_id":"misc","order":16,"heading":"✕ 6 hiểu lầm phổ biến","source_file":"slide-day07.html"},"checksum":"6b33707d4bafbd867f14273c2cc2d22f85417adbc2c4015a84b6f1cc312e8c98"} -->

## ✕ 6 hiểu lầm phổ biến

Bốn trong sáu cái dưới đây *chính deck đã bác bỏ bằng paper* — đó là điều làm 
 Ngày 7 khác các bài trước.

"Pipeline chạy không lỗi, HTTP 200, không có gì trong log — nghĩa là retrieval đang hoạt động 
 đúng."

Slide 80

6/14 failure mode không raise exception nào

bảy

normalize_L2

"luận điểm cốt lõi"

không mang thông tin gì

đo recall@k trên ground truth và 
 benchmark BM25 làm sàn

bốn câu chẩn đoán ở Hình 1

"Cải thiện chất lượng RAG nghĩa là chọn embedding model tốt hơn. Đó là quyết định quan trọng 
 nhất."

cắt bảng

Recall@1 trên BM25: 0,366 → 0,754 — gấp 2,06 lần

slide 37

bảng landscape 2026

mô-đun kinh tế

0,0%

bóc text

chunking

trước

Takeaway số 2

"data quality thường quan trọng hơn đổi sang model 
 đắt hơn"

"Cosine similarity 0,87 nghĩa là rất liên quan; 0,31 nghĩa là không liên quan. Đó là thang đo độ 
 giống nhau."

WWW 2024

"can yield arbitrary and meaningless similarities"

cosine không xác định duy nhất

"cosine là convention hiệu quả, không phải sự thật về ý nghĩa."

ngưỡng similarity tuyệt đối

calibrate riêng cho từng model và từng corpus

xếp hạng

"Semantic chunking là bản nâng cấp của fixed-size chunking. Nếu đủ ngân sách tính toán thì luôn 
 nên dùng."

NAACL 2025 Findings

"not justified by consistent performance gains"

"semantic chunking 
 87% vs fixed-token 50%"

không tồn tại trong nguồn nào

"chậm hơn 14×"

nguyên tắc leo thang

khi đã đo được một gap thật

"Metadata filter chỉ là thu hẹp kết quả. Nó không ảnh hưởng tới chất lượng retrieval — cùng lắm 
 là trả về ít kết quả hơn, và đó là điều mình muốn."

làm sập recall trong im lặng

slide 65

15

11 dòng

Mô-đun

11,0%

ef_search ≥ 76

gấp 145,7 lần k

chỉ lộ ra trên production

slide 84

quyền

"Vector store chỉ chứa số thực. Nó không phải dữ liệu gốc, nên lưu embedding của dữ liệu nhạy 
 cảm là an toàn — coi như đã ẩn danh."

slide 82

câu gần như nguyên văn

ALGEN 2025

black-box

~1.000 mẫu rò rỉ

membership inference

sự hiện diện

pseudonymized — vẫn là dữ liệu cá nhân

mask PII trước khi embed

xoá được

IndexHNSWFlat

remove_ids()

---

<!-- chiron-source-span: {"source_span_id":"e1ad0a53-2a37-5e1d-ae7c-30d8b582c4a2","locator":{"kind":"html_section","section_id":"apply","order":17,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"slide-day07.html"},"checksum":"c9ac249dea1d4a1b6b19009d45d192cb0134056832e8e6e20adc2b7337c7c010"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI là agent check-in tại kiosk khách sạn, dựng trên LangGraph. Ngày 5 cho 
 nó một PRD, Ngày 6 cho nó một mô hình ROI. Ngày 7 hỏi: *agent này được phép biết gì, và dữ liệu nào 
 thì không bao giờ nên đi vào vector store?*

### ① Phân loại dữ liệu trước khi embed bất cứ thứ gì

Đây là bước đầu tiên của [slide 8](#s8), và với SmartCheck nó loại bỏ ngay phần lớn ý 
 tưởng tồi:

| Dữ liệu | Loại | Cách xử lý đúng | Vì sao KHÔNG embed |
| --- | --- | --- | --- |
| Chính sách nhận/trả phòng, nội quy, FAQ, mô tả loại phòng, hướng dẫn quanh khách sạn | Knowledge | Chunk + embed + index | — |
| Trạng thái booking, phòng còn trống, giá đêm nay, hoá đơn dịch vụ | Operational | Function call vào PMS | Đổi mỗi phút. Index sẽ luôn cũ, và cần giá trị chính xác chứ không phải cái gần giống |
| Tên khách, số CCCD/hộ chiếu, số điện thoại, mã booking | PII | Không bao giờ vào vector store | Embedding đảo ngược được — ALGEN 2025 làm được với black-box, ~1.000 mẫu |
| Khách đang đứng ở kiosk là ai, đã trả lời gì trong phiên này | Contextual | Inject thẳng vào prompt của phiên | Corpus vài lượt — semantic search trên đó là over-engineering |

slide 9

"không 'cứ nạp hết vào vector DB đã'"

①

Vector đảo ngược được

②

GDPR Art. 4(5) / PDPL 91/2025

pseudonymized

vẫn là dữ liệu cá nhân

HNSW thì không xoá được

③

không phải câu hỏi ngữ nghĩa

SELECT

Kiến trúc đúng:

chỉ

### ② Tính quy mô corpus — và kết luận gây bất ngờ

Chuỗi 6 cơ sở, kho tri thức gồm chính sách, nội quy, FAQ, mô tả phòng và hướng dẫn địa phương: khoảng **850 tài liệu ≈ 3,2 triệu token**. Chunk 400 token → khoảng **8.000 chunk**. 
 Dùng BGE-M3 (1024 chiều, đa ngôn ngữ, có sẵn nhánh sparse):

```text
BO NHO INDEX (Flat, float32)
  8.000 chunk x 1.024 chieu x 4 byte  =  32,8 MB

CHI PHI MOT QUERY (exact k-NN, khong ANN)
  8.000 x 1.024  =  8,2 trieu phep nhan-cong  ->  duoi 1 ms voi NumPy

CHI PHI EMBED TOAN CORPUS (mot lan)
  3,2 trieu token x $0,02/1M  =  $0,064        <- sau xu
  cung corpus voi -3-large    =  $0,42
```

recall 100% theo định 
 nghĩa

không có failure mode nào trong nhóm Store

Hình 1

efSearch

nprobe

slide 51

"corpus nhỏ (vài nghìn document 
 trở xuống) — một vector DB lúc này là over-engineering"

slide 63 mục 1

"Dưới 10k vector… Sub-ms. Bỏ qua vector DB."

Và con số $0,064 làm toàn bộ cuộc tranh luận "chọn embedding model nào" trở nên nhỏ 
 bé.

36 xu

chất lượng đo được trên corpus của mình

quy trình 20 
 phút

Ngưỡng phải xem lại:

slide 63

lúc index không còn fit RAM

### ③ Nhưng filter theo cơ sở thì lại là vấn đề thật

Khách ở cơ sở Đà Nẵng không được nhận câu trả lời theo nội quy của cơ sở Hà Nội. Nghĩa là mọi truy vấn 
 phải filter theo `property_id`. Với 6 cơ sở, filter khớp khoảng **16,7%** corpus. [Mô-đun post-filter](#m-filter) cho:

| Cấu hình | E[trả về] | P(đủ k) | ef_search cần cho 95% |
| --- | --- | --- | --- |
| k = 5, ef_search = 40 | 6,7 | 81,9% | 53 |
| k = 5, ef_search = 20 | 3,3 | 23,1% | 53 |
| k = 10, ef_search = 40 | 6,7 | 11,7% | 91 |
| Filter chặt hơn: cơ sở + loại tài liệu (f ≈ 4%) | 1,60 | 2,1% | 227 |

Hàng 2

ef_search

23,1%

không lỗi, không log

Hàng cuối

2,1%

227

Nhưng với SmartCheck, cả bảng này có một lối thoát đơn giản

pre-filter

1,4 triệu phép tính, vẫn dưới một mili-giây, và recall vẫn 100%

pre-filter không tốn gì, 
 nên toàn bộ họ failure mode về filter biến mất

slide 84

trước

### ④ Ba thứ đặc thù SmartCheck phải xử lý riêng

| Vấn đề | Vì sao SmartCheck gặp phải | Xử lý |
| --- | --- | --- |
| Mã booking trong truy vấn | Khách gõ "đơn HN-2291-XL của tôi". Dense embedding làm nhoè token chính xác — 
 sẽ trả về mã tương tự nhưng SAI | Nhánh BM25 bắt buộc, hợp nhất bằng RRF. BGE-M3 có sẵn nhánh sparse nên không 
 cần dựng thêm hệ thống |
| Tài liệu tiếng Việt | Nội quy có bản scan; dấu thanh mang nghĩa; nguồn tài liệu trộn macOS/Windows | NFC toàn corpus ngay sau parse · scan tối thiểu 300 DPI · cân nhắc 
 AITeamVN/Vietnamese_Embedding (fine-tune từ chính BGE-M3) |
| Nội quy khác nhau giữa các cơ sở | Cùng một tiêu đề "Chính sách nhận phòng", 6 nội dung khác nhau → near-duplicate ở mức 
 cao | Pre-filter theo property_id (mục ③) · và đừng khử trùng lặp mù 
 quáng — ở đây các bản gần giống nhau là đúng, không phải rác |

Slide 40

không phải 
 trùng lặp

Quy tắc:

trong từng phạm vi

property_id

provenance

### ⑤ Việc nên làm tuần này — theo đúng thứ tự

① Dựng bộ eval no-labels 100 câu

slide 76

② Chạy BM25 làm sàn

③ Chuẩn hoá NFC + kiểm token count

④ Bỏ vector DB, dùng Flat + pre-filter

giảm

⑤ Chỉ sau khi có ④, mới bàn tới embedding model nào.

Chú ý thứ tự:

slide 2

takeaway số 2

---

<!-- chiron-source-span: {"source_span_id":"5308ee66-8ee4-5f85-af31-b5b9b106c2d9","locator":{"kind":"html_section","section_id":"numbers","order":18,"heading":"# Con số cần kiểm chứng","source_file":"slide-day07.html"},"checksum":"a7b4b38389434fb96eeb110bd6f394a9775fbc4b4443fc6e4bcc014eb24ba099"} -->

## # Con số cần kiểm chứng

Ngày 7 khác Ngày 6 ở chỗ **phần lớn con số là của slide**, có nguồn, có 
 năm. Mục này tách rõ ba loại: *của slide* · *tính lại từ công thức của slide* · *giả định của tài liệu này*.

sáu

giữ

| Con số | Nguồn | Cần kiểm gì trước khi dùng |
| --- | --- | --- |
| ~15 tỷ phép nhân–cộng mỗi query (10M × 1536) · 61,4 GB cho Flat | Của slide (50, 51) | Tính lại: 10⁷ × 1536 = 15,36 tỷ ✓ · ×4 byte = 61,44 GB ✓. Cả hai khớp chính xác |
| PQ: 512 B → 8 B, nén 64× · HNSW 6.144 B + 256 B đồ thị | Của slide (53, 55) | Khớp: 128×4 = 512; 8 subspace × 8 bit = 8 B. 1536×4 = 6.144; M=16 × 16 B = 256 ✓ |
| IVF: nprobe=1 → 30% recall @136 µs · nprobe=8 → 74% @729 µs | Của slide (52) — cấu hình Pinecone IVF256, PQ32x8 | Đây là một cấu hình cụ thể, không phải quy luật. Slide nói rõ "không có công thức" |
| STC vs Recursive: MRR 0,358 → 0,595 · R@1 BM25 0,366 → 0,754 
 · ít hơn ~40% chunk | Của slide (37) — Guttal et al., arXiv:2605.00318, MAUD 39.231 bản ghi, ngân sách 
 512 token | Tỉ lệ 1,66× / 2,06× là tính lại từ số của slide. Corpus MAUD là hợp đồng M&A — 
 corpus ít bảng hơn sẽ hưởng lợi ít hơn |
| Contextual Retrieval: 5,7% → 3,7% → 2,9% → 1,9% (−35/−49/−67%) · $1.02/M token | Của slide (46) — eval riêng của Anthropic, vendor | Deck kèm sẵn phản chứng: reproduction độc lập (Merola & Singh, ECIR 2025) cho NDCG@5 
 0,317 vs 0,312 = +1,6%. Dùng cả hai con số, đừng dùng một |
| Embed 100M token: $2 (-3-small) · $13 (-3-large) | Của slide (77), giá xác minh 2026-07-30 | Tính lại: 100 × $0,02 = $2 ✓ · 100 × $0,13 = $13 ✓. Giá API đổi theo thời gian — kiểm lại tại 
 trang vendor |
| pgvector 0.8.0-pg17: xin 15 láng giềng, nhận 11 dòng | Của slide (65) — quan sát thật, Franck Pachot | Mô-đun tính ra ef_search 40 × f 27,5% = 11,0 — khớp. Nhưng f = 27,5% là suy ra 
 ngược từ con số 11, không phải số slide cho |
| PoisonedRAG 90% ASR · SPLADE thêm 100–300 ms · trafilatura 
 14–22 ms/trang · trang convert dùng ít hơn ~65% token | Của slide (83, 68, 34) | 90% ASR chỉ đúng với điều kiện 5 văn bản độc cho MỖI câu hỏi mục tiêu — deck 
 đính chính rõ chỗ này |
| Xác suất đủ k khi post-filter · ef_search cần cho 95% · các bội số 5,1× / 21× / 157× | Tính ra bằng mô hình nhị thức, không có trong slide | Giả định tư cách filter độc lập với thứ hạng similarity. Thực tế filter thường tương 
 quan dương với nội dung → thực tế tốt hơn mô hình. Xem mục "Giới hạn" của mô-đun |
| Generation chiếm 86,9% chi phí tháng · rerank 13,1% · embed query 0,0% · 
 4.545 truy vấn để rerank tiêu hết ngân sách embed | Tính ra từ giá của slide 25/77 + giả định của tài liệu này: 
 100.000 truy vấn/tháng, k=50, inject 5, chunk 400 token, generation $1.25/1M | Giá generation không có trong slide. Giá reranker cũng vậy — mô-đun dùng giá 
 embedding làm cận dưới, nên phần rerank thực tế cao hơn. Kết luận về hình dạng vẫn giữ |
| SmartCheck: 8.000 chunk · 32,8 MB · 8,2 triệu phép tính · $0,064 
 · f = 16,7% → P(đủ 5) = 81,9% | Tính ra từ giả định của tài liệu này về quy mô corpus 
 (850 tài liệu ≈ 3,2M token, 6 cơ sở) | Quy mô corpus là ước lượng, chưa ai đếm thật. Nhưng kết luận "dưới 10k chunk thì bỏ vector 
 DB" bền vững kể cả khi corpus lớn gấp 4 lần |
| Hệ số 16 byte mỗi cạnh đồ thị HNSW | Ước lượng của tài liệu này để khớp con số 256 B của slide 55 ở M=16 | Cài đặt thật khác nhau giữa các thư viện. Dùng để so sánh tương đối, không để dự toán chính xác |
| "1 từ ≈ 1,33 token" (từ "100M token ≈ 75M từ") | Của slide (77) | Tỉ lệ này là cho tiếng Anh. Tiếng Việt viết rời âm tiết nên tỉ lệ cao hơn đáng 
 kể — đừng ước lượng token từ số từ; chạy chính tokenizer của bạn trên mẫu thật |

97 trang

thứ tự trang PDF (1–97)

tiêu đề slide

---

<!-- chiron-source-span: {"source_span_id":"90154804-a464-5ac0-845e-01f1217ce2d3","locator":{"kind":"html_section","section_id":"cheat","order":19,"heading":"▣ Cheat sheet ôn thi","source_file":"slide-day07.html"},"checksum":"30f194147d9fb77c67db8d9240347331c144295b43f8ce0ddf4dad06f50a1cdf"} -->

## ▣ Cheat sheet ôn thi

Những thứ nên nhớ được mà không cần mở lại tài liệu.

"Không lỗi" không có nghĩa là "đúng."

đo recall@k trên 
 ground truth, và luôn có BM25 làm sàn.

| Danh sách | Các mục | Slide |
| --- | --- | --- |
| Pipeline 6 mắt xích | Document → Chunk → Embed → Store → Query → Inject | 11 (+ Hình 1 ) |
| 3 loại data | Knowledge (embed) · Operational (SQL/function) · Contextual (inject thẳng) | 8 |
| 3 bước của embedding | Tokenize → Encoder → Pooling (mean / last-token / [CLS]) | 17 |
| 3 đồng tiền của ANN | Recall · Latency · Memory — không index nào thắng cả ba | 50 (+ Hình 2 ) |
| Thang chunking 5 bậc | Fixed → +Overlap → Recursive → Structure-aware → Semantic | 44 |
| 3 chiến lược filter | Post-filter (sai) · Pre-filter (đúng, chậm) · In-algorithm (đúng, nhanh, cần engine) | 65 |
| 5 bước eval không nhãn | Sample ≥100 → sinh câu hỏi có persona → chunk nguồn là positive → đo recall@k → 
 kiểm tay 10% | 76 |

```text
① BO NHO INDEX
   Flat    = N · d · 4 byte
   HNSW    = N · d · 4  +  N · M · 16
   IVF-PQ  = N · (M_pq · bits / 8)
   int8    = N · d          binary = N · d / 8      (nen 4x va 32x)

② CHI PHI MOT QUERY NEU QUET HET
   O(N · d)      vd. 10M x 1536 = 15,4 ty phep nhan-cong

③ COSINE
   cos(A,B) = (A·B) / (‖A‖ ‖B‖)
   Neu da chuan hoa L2: d² = 2 − 2·cos  ->  cung thu tu xep hang

④ POST-FILTER TRA VE BAO NHIEU
   so song sot ~ Nhi thuc(ef_search, f)      E = ef · f
   -> f cang nho, ef can cang tang PHI TUYEN (5x, 21x, 157x lan k)

⑤ KINH TE PIPELINE
   embed corpus = corpusTok · gia          <- MOT LAN
   rerank/thang = Q · k_short · chunkTok · gia   <- MOI TRUY VAN
   gen/thang    = Q · k_inject · chunkTok · gia  <- MOI TRUY VAN, ~87%
```

| Model | Max input | Ghi nhớ |
| --- | --- | --- |
| Nomic Embed Text v2 (MoE) | 512 | Model 2025 nhưng input ngắn nhất bảng — bẫy dễ mắc nhất |
| EmbeddingGemma · gemini-embedding-001 | 2.048 |  |
| BGE-M3 · Jina v2–v3 · Arctic 2.0 | 8.192 | Mặc định an toàn cho phần lớn corpus |
| Qwen3-Embedding (cả 3 size) | 32.768 | KHÔNG có bản 40K — model card ghi 32K |
| Cohere Embed v4 | 128K |  |

max_seq_len

encode()

"Recall thấp, sửa thế nào?"

Hình 1

"Chọn index nào?"

luôn build Flat trước

"Chunk bao nhiêu token?"

đổi model là phải đo lại

"Khi nào cần BM25?"

làm nhoè

"Filter đặt ở đâu?"

Trước hoặc trong

"Embedding có phải dữ liệu cá nhân không?"

pseudonymized, tức vẫn là dữ liệu cá nhân

trước

| Con số | Sự thật |
| --- | --- |
| "semantic chunking 87% vs fixed-token 50%" | Không tồn tại trong nguồn nào |
| "semantic chunking chậm hơn 14×" | Benchmark throughput của Chonkie, không phải của paper |
| "nprobe = 8–16 cho 1–10M vector" | Không có trong docs FAISS hay bài Pinecone |
| "hybrid tăng accuracy 26–31%" | Chỉ có trong blog vendor, không kèm dataset |
| "Qwen3-Embedding 40K token" | Model card ghi 32K cho cả ba size |
| "Gemini Embedding 68.32 điểm MTEB tiếng Anh" | 68.32 là điểm đa ngôn ngữ; 
 English v2 thật là 73.28 |

một con số MTEB vô nghĩa nếu thiếu board + version + aggregation + 
 ngày.

---

<!-- chiron-source-span: {"source_span_id":"70dc730e-d873-5f56-9514-8748e7f98fd2","locator":{"kind":"html_section","section_id":"gloss","order":20,"heading":"☰ Từ điển thuật ngữ","source_file":"slide-day07.html"},"checksum":"b79c51430f5aff68801cefb04b1bf6cb49f7946015053f680f0dd4f640693f2b"} -->

## ☰ Từ điển thuật ngữ

Định nghĩa theo cách dùng được trong bài thi và trong công việc.

---

<!-- chiron-source-span: {"source_span_id":"285b3281-dbf5-5d93-aed5-0dcc4f581cb3","locator":{"kind":"html_section","section_id":"bloom","order":21,"heading":"◉ Bạn đang ở mức nào?","source_file":"slide-day07.html"},"checksum":"10609f19206907a6e39cdc3f843151c9b8c3a80de55059d0e34d8f546e5c3db0"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Lab 7 kiểm tra mức 3–4; luận đề ở [slide 80](#s78) kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 6 mắt xích pipeline, 3 loại data, 3 bước embedding, 3 đồng tiền ANN, 5 bậc chunking, 
 3 chiến lược filter, 5 bước eval không nhãn. | Cheat sheet · Hình 1 · Hình 2 |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao "512 token" không phải quy luật, vì sao cosine là quy 
 ước chứ không phải chân lý, và vì sao BM25 vẫn sống năm 2026. | Slide 43 · slide 20 · slide 13 |
| 3 · Áp dụng | Dựng được bộ eval no-labels 100 câu, đo recall@5 với filter thật, và tính được index của 
 bạn chiếm bao nhiêu RAM ở số chiều đang dùng. | Slide 76 · mô-đun bộ nhớ · Bài 3 |
| 4 · Phân tích | Cho một triệu chứng ("recall tụt, không lỗi"), khoanh được nó vào một mắt xích bằng bốn câu chẩn 
 đoán, rồi ánh xạ vào một trong 14 dòng — kèm phép thử chứng minh. | Bài 1 và Bài 2 · slide 78–80 |
| 5 · Đánh giá | Nhìn một con số trong tài liệu về RAG và nói được nó có dùng được không — ai chạy, trên 
 dataset nào, board nào, phiên bản nào. Và nhận ra khi một cải thiện "49%" thực chất là 2,8 điểm 
 phần trăm. | Slide 26 · slide 45 · slide 46 |
| 6 · Sáng tạo | Nhận ra rằng giải pháp đúng là bỏ bớt công nghệ — corpus dưới 10k chunk thì Flat + 
 pre-filter cho recall 100%, dưới 1 ms, và xoá sạch cả một họ failure mode. | Mục SmartCheck ② và ③ · slide 51 |

①

ai đã đo

②

③

slide 80
