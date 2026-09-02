---
schema_version: 1
course_id: rag-intensive
document_id: "3631b891-221c-55b3-b26e-162482e0afe6"
document_version_id: "8dba17da-5b87-5099-9493-f5e79c57c400"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Vector Store & Feature Store"
source_file: "track 2 - day 19.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 19.pdf"
source_sha256: "82181b4c289638596fefcfe44e19e2b5f0b2957ce6d68c9186b32ca5784338d0"
parser_version: chiron-structured-markdown-v1
page_count: 61
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":61}"
language: vi
---

# Vector Store & Feature Store

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"15213b4b-6bcf-5e95-a9e6-6c5950029d20","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Vector Store & Feature Store","extraction_method":"pdf-text-layer"},"checksum":"c318e3279a2515517f4a38509bf0baa304034b5bcaa64ffb0a37513d2ec515a2"} -->

## Slide 1 - Vector Store & Feature Store

AICB-P2T2 · Ngày 19 · Chương 4: Hạ Tầng Giảngviên VinUniversity · Phase 2 · Track2· Tuần4

---

<!-- chiron-source-span: {"source_span_id":"6af028d1-4993-58ee-97d5-c74e86703487","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"d78839c7aff50c5bf25f0b8b31a2edd71c0a5b802a866f24d6c0741d3564073c"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “SQL database trả về exact match. Nhưng AI cần “tương tự” — semantic search. Tại sao SQL không đủ cho AI search, và vector database thực sự lưu gì?” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"fd366a2d-dd80-5f7b-a2e2-149bd71f525a","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"6d10b38576134f362f5036d086015be6ddd8172d58e6273f4aa371a88c37d0b4"} -->

## Slide 3 - NộiDung Bài Học

1. VectorEmbeddings: Text →Số

2. VectorDB Landscape (3 tầng lưutrữ)

3. ANN,Filtered Search & Hybrid

4. RAGPipeline & Long Context

5. GraphRAG& Knowledge Graphs

6. AgenticRetrieval & Agent Memory (code)

7. FeatureEngineering & Feature Store (code)

8. Production: bảo mật, chiphí, case studies

9. Ứngdụng: Wiki /CodeWiki / DocWiki

10. Demo: Semantic Search API Giảngviên (VinUni) AICB· Ngày 19 Tuần4 1 / 56

---

<!-- chiron-source-span: {"source_span_id":"2eaf817a-b6b6-5639-99d2-ffa1d441f1b0","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mụctiêu bài học","extraction_method":"pdf-text-layer"},"checksum":"2f789fe77a22ab6336e80bea24abd1afea92586a47de0c153262bcea2aa7fa37"} -->

## Slide 4 - Mụctiêu bài học

### Saubuổi học này,bạnsẽ

1. Hiểuvector embeddings và chọn modelbằngbằng chứng(VN-MTEB)

2. Deployvàqueryvectordatabase—vàchọnđúng tầnglưutrữ (RAM/SSD/object storage)

3. Xâydựng RAG pipeline với hybrid search,filtered search và reranking

4. SetupFeast Feature Store với offline/onlinestore

5. Biếtrủi robảomật & tuân thủcủamột kho vector (OWASPLLM08,PDPL) Agendahôm nay Embeddings → Vector DB → ANN + Hybrid→ RAG → GraphRAG → Agentic & Memory →FeatureStore →Production Giảngviên (VinUni) AICB· Ngày 19 Tuần4 2 / 56

---

<!-- chiron-source-span: {"source_span_id":"2d21de34-8a8e-5fe7-b111-068eeaaeeec6","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"b0485f6e05395d752cf7b20e58737a8586241fe204c39d7ce5f1b9bf371f880e"} -->

## Slide 5 - DeliverableCuối Ngày

Artifactcần nộp Vectorsearch endpoint + Feature Storeoffline/online+ 4 mission nângcao Core(NB1–NB4)

- REST /search?q=... top-10,P99 <50ms

- Hybrid: vector + BM25,merge bằng RRF

- Feast: 3 feature views,materialize, online lookup

- Benchmarkkeyword vs semantic vs hybrid
Nângcao (NB5–NB8)

- Đorecall cliffcủa filtered search

- Agent: retrieval-as-tool + táchcâu hỏi

- Semanticcache: sweep ngưỡng+ demo rò tenant

- Featureengineering: leakage +on-demand view
Giảngviên (VinUni) AICB· Ngày 19 Tuần4 3 / 56

---

<!-- chiron-source-span: {"source_span_id":"e9e6c592-9e85-5794-bd4f-c68dc3b23eef","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Text →DenseVector: EmbeddingSpace","extraction_method":"pdf-text-layer"},"checksum":"5d4e2b3ddde0167f8eaab4953fbb0b688041d5550481206f62e985c80a6db7e2"} -->

## Slide 6 - Text →DenseVector: EmbeddingSpace

dim1 dim2 “cloudcomputing” “serverinfrastructure” “datacenter” Techcluster “nhàhàng” “ẩmthực” “mónăn” Foodcluster cos=0.92 EmbeddingModels

- text-embedding-3-small: OpenAI,
1536d

- text-embedding-3-large: 3072d,
Matryoshka

- bge-m3: BAAI, 1024d, multilingual

- nomic-embed: open-source

- PhoBERT:VN lightweight baseline (xem
bảng2026) Cosine Similarity — ⃗A·⃗B |⃗A|×|⃗B| — giá trị 0–1, >0.85= very similar Giảngviên (VinUni) AICB· Ngày 19 Tuần4 4 / 56

---

<!-- chiron-source-span: {"source_span_id":"d6999731-b0ad-5d46-9d06-a7ac74e3c3b1","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Embeddings: A Decade ofRepresentations (2013→2026)","extraction_method":"pdf-text-layer"},"checksum":"c785213d9d69e1210edc304924312e292c3ceab1251a798b58dd41adde2910f8"} -->

## Slide 7 - Embeddings: A Decade ofRepresentations (2013→2026)

word2vec FaceNet BERT Sentence- BERT OpenAI ada-002 bge-m3/ 3-large 2013 2015 2018 2019 2022 2024–26 Mikolov: word

- 300d
Schroff: 128d face + triplet loss Devlin: contextual token embeddings Reimers: sentence- level retrieval General-purpose API embedding Multilingual, Matryoshka, MTEB Keyshift over a decade 2013–2019: task-specificembeddings—mỗidomain(NLP,face,audio)trainriêng. 2020–2026: general-purpose foundation embeddings — một model, nhiều use cases, multilingual, multi-modal. Re-index cost cao⇒ chọn cẩn thậntừ đầu. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 5 / 56

---

<!-- chiron-source-span: {"source_span_id":"aca56aa4-07a2-52be-ac11-2a0c2e1afe1f","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"EmbeddingModels 2026: LựaChọn Theo Use Case","extraction_method":"pdf-text-layer"},"checksum":"9953c28a713cf7d6c7a9fd86f22d4956eb36b4eac36bce1bf963d3fd4a3bf86e"} -->

## Slide 8 - EmbeddingModels 2026: LựaChọn Theo Use Case

Model(2026) Dim Giá Chọn khi gemini-embedding-2 3072 API đaphương thức text-embedding-3-large 3072 $0.13/M chấtlượng cao text-embedding-3-small 1536 $0.02/M baselinerẻ cohere embed-v4 1536 API PDF/ảnh,VPC bge-m3 1024 self-host tiếngViệt Qwen3-Embedding 1024+ self-host OSSđa ngữ TiếngViệt: xemslide VN-MTEB tiếp theo.Bảngnày sẽ cũ trong vàituần —học cách chọn, đừng họcthuộc. Matryoshka: Giảm Index 6×

- text-embedding-3-large dùngMRL
—truncatable: 3072d →256d

- 256dvẫn thắng ada-002 @ 1536d
trênMTEB

- Tiếtkiệm RAM/disk 6×,giảm chi phí
vectorDB

- Ápdụngngaykhiscale >10Mvectors
Lưu ý: Vệ sinh benchmark:MTEB v2 (Eng) và MMTEB (đa ngữ) làhai bảng khác nhau;điểmv2khôngsođượcvớiv1. Luôn re-rank trêngolden set của bạn(Ngày 14). Đổimodel = re-index toàn bộ. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 6 / 56

---

<!-- chiron-source-span: {"source_span_id":"78887063-8854-58a8-bdfd-7a54c0e2813c","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"TiếngViệt: ChọnEmbedding Bằng Bằng Chứng (VN-MTEB)","extraction_method":"pdf-text-layer"},"checksum":"7c7f499ad3bee22ab8028bc25568ccdfe95a4ca68fbfc258e0c9eed0add7eedb"} -->

## Slide 9 - TiếngViệt: ChọnEmbedding Bằng Bằng Chứng (VN-MTEB)

Model Params Dim VN-MTEB bge-m3 568M 1024 64.90 Vietnamese_Embedding 568M 1024 63.34 halong_embedding 278M 768 61.60 vietnamese-bi-encoder 135M 768 54.89 VN-MTEB(arXiv 2507.21500, 07/2025): 41 datasets, 6 tasks,18 models. Bađiều bảng này dạy ta

1. Generalistđa ngữ (bge-m3)thắngcả bản fine-tunetiếng Việtcủachính nó trên benchmarkrộng

2. Nhưngfine-tune vẫn có thể thắngtrên domain hẹp ⇒phảiđo trên dữ liệu của bạn

3. Modeldùng RoPEvượtmodel dùng absolutepositional embedding — lý dokỹ thuật,không phải “mới hơn” Lưu ý:VN-MTEB đượcdịchtừ MTEB tiếng Anh⇒đo năng lựcngôn ngữ, chưa đovăn hoá/domain Việt Nam. Rerankertiếng Việt: ViRanker (BGE-M3). Kết luận khôngđổi:goldenset của bạn là trọngtài cuối cùng. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 7 / 56

---

<!-- chiron-source-span: {"source_span_id":"3586b48d-819b-595d-860d-7c955624145a","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"SimilarityMetrics: Cosine vsDot vs Euclidean","extraction_method":"pdf-text-layer"},"checksum":"f21d5eb1e8a44899d0868f613cad37e8fbf33acd23dbc50d84e2023a9a283099"} -->

## Slide 10 - SimilarityMetrics: Cosine vsDot vs Euclidean

CosineSimilarity cos(⃗a, ⃗b) = ( ⃗a · ⃗b)/(∥⃗a∥ ∥⃗b∥)

- Range [−1, 1],angle only

- Defaultcho text embedding

- OpenAI/BGE/e5unit-norm ⇒
dot= cosine

- Matchmetric với pretraining
objective: sai metric degrade recall10–20% DotProduct ⃗a · ⃗b = ∑ aibi

- Baogồm magnitude

- Nhanhhơn (no
division)

- ColBERT,DPR dùng
dot Euclidean( L2) d = √∑(ai − bi)2

- Triangleinequality ⇒
IVF/ kd-tree

- CLIPimage, wav2vec
audio

- Unit-norm:
d2 = 2(1 − cos) Giảngviên (VinUni) AICB· Ngày 19 Tuần4 8 / 56

---

<!-- chiron-source-span: {"source_span_id":"8bfb825f-ae9b-5bbf-872e-0de45043d634","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Multi-modalEmbeddings: VectorVượt Khỏi Text","extraction_method":"pdf-text-layer"},"checksum":"6f92dbba0bcdc09a3a348c9076f008f38d39ce9187a134897a633b1073c7b7cb"} -->

## Slide 11 - Multi-modalEmbeddings: VectorVượt Khỏi Text

Text encoder Image encoder Audio encoder Shared embedding space Contrastivelearning Models2026 CLIP(OpenAI):text+image, foundational SigLIP(Google): backbone của ColPali jina-clip-v2: multilingual incl. tiếngViệt ImageBind(Meta): 6 modalities GeminiEmbedding2 (GA04/2026): text+ảnh+ video+audio+PDFvào mộtkhônggian3072d, 100+ ngôn ngữ, MRL truncate. 1 request: 8K to- kens / 6 ảnh / 120s video / 180s audio / 6 trang PDF. Usecases 2026 Visualsearch (Tiki,Shopee)· Contentmoderation (ảnh+caption)· Videoindexing (tìmcliptheoprompt)· Medical (X-ray+reportđồng embedding). Giảngviên (VinUni) AICB· Ngày 19 Tuần4 9 / 56

---

<!-- chiron-source-span: {"source_span_id":"0f1650d7-d3e3-5b39-9dd1-c7574187a42f","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"VectorDB So Sánh","extraction_method":"pdf-text-layer"},"checksum":"053ee8172a2dcaf057ad5196ba92780856b6c7b20b98153273cb2ef1d3c48a30"} -->

## Slide 12 - VectorDB So Sánh

Feature Pinecone Weaviate Qdrant pgvector Hosting Managed Self/Cloud Self/Cloud Extension API REST/gRPC GraphQL REST/gRPC SQL Multi-modal × ✓ × × Filtering Metadata GraphQL Payload SQLWHERE P99(1M vecs) 8–22ms ∼10ms ∼5ms 15ms Quantization ✓ ✓ ✓(binary) scalar Bestfor Production Multi-modal Self-hosted HavePostgres

### Nguồn
VectorDBBench2025·1Mvectors,768dims,HNSWindex,top-10query. pgvector+pgvectorscale(TimescaleDiskANN). Giảngviên (VinUni) AICB· Ngày 19 Tuần4 10 / 56

---

<!-- chiron-source-span: {"source_span_id":"a290c9fd-df6c-55cd-99c2-0fee8ef90c5b","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"FAISS& Pre-LLM VectorApplications","extraction_method":"pdf-text-layer"},"checksum":"e016ded17dd7c8ee23814f89819d07afa284783c297a28bc5b5a242e39ca1cb0"} -->

## Slide 13 - FAISS& Pre-LLM VectorApplications

FAISS(Meta, 2017)

- Library, notadatabase — C++/Python, no
server

- GPU:1B vectors, top-K<1s

- IVF,HNSW,PQ, OPQ, IVF-PQ —cùng một
API

- In-memory+ on-disk indices

- 2026: vẫnlàembeddedtierbêntrongMilvus,
Vespa,pgvector-rs Pre-LLMUse Cases

- Facerecognition: FaceNet,ArcFace —
FaceID,photo search

- Pinterestvisual lens: CNNfeats + FAISS,
2017+

- RecSyscandidate gen:
YouTube/Spotify/TikTok— ∼1Bvectors

- Plagiarism/ dedup: Turnitin,news article
clustering

- Audiofingerprinting: Shazam,Spotify
duplicatedetection Deep Metric Learning— Pre-LLM vector retrieval dựa vào triplet loss (FaceNet), contrastive loss, ArcFace angular margin — train embedding sao chocosine (hoặc Euclidean) tách class. Đây là tiền thân của contrastive pretraining hiện đại (CLIP, SigLIP). Giảngviên (VinUni) AICB· Ngày 19 Tuần4 11/ 56

---

<!-- chiron-source-span: {"source_span_id":"6528452e-9373-5b1c-9860-b1ab9358130a","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"BaTầng Lưu TrữVector: RAM / SSD/ Object Storage","extraction_method":"pdf-text-layer"},"checksum":"78c329b8cf737c4706caefb7a65f82a84af7fe5216d4f5662c174bcb66a84e17"} -->

## Slide 14 - BaTầng Lưu TrữVector: RAM / SSD/ Object Storage

Tầng Vectornằm ở Latency Chi phí Dùngkhi In-memory(HNSW) RAM 5–20ms caonhất hot,latency-critical, ≤10M On-disk(DiskANN) SSDcục bộ ∼30ms trungbình 100M+,vẫn cần tương tác Objectstorage S3/ GCS ∼100ms thấpnhất corpuskhổng lồ, query thưa AmazonS3 Vectors(GA 12/2025)

- Objectstorage đầu tiênnativelưu+ query
vector

- 2tỷ vector/index,10.000 index/bucket

- Chiphí upload+lưu+querygiảmtới 90%

- Querythưa <1s; query thường xuyên
∼100ms

- Tíchhợp Bedrock KB, OpenSearch,
SageMaker Vìsao rẻ hơn hẳn? Không phải thuật toán — mà làgiá lưu trữ: object storage ∼$0,02/GBsovớiRAM ∼$2+/GB ⇒chênh haibậc độ lớn. Cùng tầng: turbopuffer, LanceDB (scale-to-zero khirảnh). Đánhđổi: latency caohơn, QPS thấp hơn. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 12 / 56

---

<!-- chiron-source-span: {"source_span_id":"e7bd702b-7034-5438-990b-865e9f56d1ba","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"HNSW:Hierarchical Navigable Small World","extraction_method":"pdf-text-layer"},"checksum":"97f83be41f1827bbc551eea47c4afa8fc1f40ba5e276f0e08d2db54e4ed1f49c"} -->

## Slide 15 - HNSW:Hierarchical Navigable Small World

Layer2 Layer1 Layer0 Q HNSW:Vì sao là default 2026

- Graph-based,multi-layer skip list

- Recall95%+ ở ∼10ms (in-memory)

- Params: ef=200, m=16 (defaulttốt)

- Native: Pinecone, Weaviate,Qdrant,
Milvus KhiHNSW không phải lựa chọn

- RAM-bound: >10Mvec @ 768d→tốn
∼10GB

- Update-heavycorpus: re-build chậm

- Static,billion-scale →DiskANN(slide
tiếp) Giảngviên (VinUni) AICB· Ngày 19 Tuần4 13 / 56

---

<!-- chiron-source-span: {"source_span_id":"34814a5b-3709-52a7-b847-d635496d34a1","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"HNSWvs IVF vs DiskANN: KhiNào Dùng Gì","extraction_method":"pdf-text-layer"},"checksum":"2b4d7dc5b28f917834d2a9957786d232c0d01ebdf534bdfdb9048840dfc47f5a"} -->

## Slide 16 - HNSWvs IVF vs DiskANN: KhiNào Dùng Gì

HNSW

- Graphin-memory,
multi-layerskip list

- Recall95%+ @ ∼10ms

- RAM-bound: ∼1KB/vec
(768dfp32)

- Bestfor: ≤10Mhot
vectors,latency-critical

- Params: ef=200, m=16
IVF(FAISS)

- Cluster-basedinverted
index

- LowerRAM, higher
latency( ∼30–50ms)

- Retrainingcần khi data
driftlớn

- Bestfor: batch-mode,
staticcorpus, CPU-only infra

- Params: nlist=1024,
nprobe=64 DiskANN

- Graphtrên SSD —
billion-scale1 node

- Latency ∼30ms @ 99%
recall

- 10–50×rẻhơn HNSW
ởscale lớn

- Dùngbởi: Pinecone
serverless, pgvectorscale,Azure CosmosDB

- Bestfor: >100M
vectors,cost-sensitive RaBitQ(SIGMOD2024BestPaper) — UnbiasedbinaryquantizationchoDiskANN —tíchhợptrongpgvectorscale&VectorChord. GiảmRAMthêm32 ×vớichấtlượng recalltương đương. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 14 / 56

---

<!-- chiron-source-span: {"source_span_id":"9dc2a872-5857-5c0f-9195-889453df8218","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Quantization: Bí Quyết TiếtKiệm Bộ Nhớ 32×","extraction_method":"pdf-text-layer"},"checksum":"f9591ebd75e5fcb188e297e59ae55b4f42bf6ec432c79efd4bc850b9070a62ce"} -->

## Slide 17 - Quantization: Bí Quyết TiếtKiệm Bộ Nhớ 32×

float32 4B/dim int8scalar 1B/dim binary 1bit/dim ÷4 ÷8 Recall: 100% (baseline) Recall: ∼99% RAM: 4× nhỏ hơn Recall: 95–98% RAM: 32× nhỏ hơn 100K vectors× 1536d (OpenAI):fp32 = 900MB → int8 = 225MB→ binary = 28MB AsymmetricQuantization (Qdrant 1.15)

- Binarystored (28MB) +scalarquery
(precise)

- Bestof both: cheapstorage + high recall

- Recall ≥99%với chi phí binary storage
ProductionDefault 2026

- Qdrant,Weaviate,Pinecone, Milvus: hỗ trợ
binary/scalarout-of-the-box

- Bậtquantization trướckhi ingest—không
phảisau

- Re-quantize= re-index ⇒blue-green
(ProductionPatterns) Giảngviên (VinUni) AICB· Ngày 19 Tuần4 15 / 56

---

<!-- chiron-source-span: {"source_span_id":"21aee365-ebec-5495-9bf1-cfa468c41533","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"HybridSearch: BM25 +Vector+ RRF","extraction_method":"pdf-text-layer"},"checksum":"6231676dbfd7d1b899635f8c074cc43ce9d322267500f9f22d6beb1a4d18b954"} -->

## Slide 18 - HybridSearch: BM25 +Vector+ RRF

Query BM25 / SPLADE Vector ANN (HNSW) RRFMerge k = 60 Top-K Hybrid sparse, exact-term match dense, semantic match Reciprocal Rank Fusion— score(d) = ∑ r 1 k +rankr(d) (k = 60) Rank-only: không cần normalize raw scores giữa BM25(TF-IDF) và cosine. Production2026 (Hybrid wins)

- Recall@10: hybrid >dense-only
∼10–15pp (đotrên golden set của bạn— Lab19)

- Latency+6ms (songsong) · storage1.4×

- Native: Qdrant, Weaviate,OpenSearch,
Milvus

- SPLADE:recall >BM25nhưng cần GPU
Giảngviên (VinUni) AICB· Ngày 19 Tuần4 16 / 56

---

<!-- chiron-source-span: {"source_span_id":"539e30fa-539e-5578-8e68-7449fa7c0eb5","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"FilteredSearch: Cái BẫyRecall Ít Ai Nói Đến","extraction_method":"pdf-text-layer"},"checksum":"5b5355c08d479ca3e0f4ed6bc5fb5cb98528251a783a287b27be69b1dc5a2493"} -->

## Slide 19 - FilteredSearch: Cái BẫyRecall Ít Ai Nói Đến

Post-filter ANNtrước →lọcsau.

- Xintop-100, filter khớp
2% ⇒còn2kết quả

- Recallsập khôngbáo
lỗi

- Cànglọc chặt càng tệ
Pre-filter(brute force) Lọctrước →quéttoànbộsub- set.

- Kếtquả luônđúng

- Nhưngmấtindex

- Latencytăng theo kích
thướcsubset Filtered-ANN(đúng) Indextự biết filter.

- Qdrant: filterable HNSW
payloadindex

- Milvus: partition key

- pgvector0.8: iterative
scan— tự nới rộng đến khiđủ khàng Lưu ý:“Lọc sớm cho nhanh” là bản năngsai. Filter phá tính liên thông của đồ thị HNSW⇒ đi lạc, trả về ít và kém. Bài test bắt buộc:chạy golden set với filterchọn lọc mạnh (khớp ∼1% corpus) — đây là lúc hệ thống gãy, khôngphải lúc query trống. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 17 / 56

---

<!-- chiron-source-span: {"source_span_id":"68902529-6b23-55d7-a910-68cad6f25c31","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"LateInteraction: ColBERT →ColPali(RAG cho PDF)","extraction_method":"pdf-text-layer"},"checksum":"0c8492c2a524837fca7053faa9464662ecef15eab11685e9279372535038157b"} -->

## Slide 20 - LateInteraction: ColBERT →ColPali(RAG cho PDF)

Single-vectorvs Late interaction Single-vector: cả chunk nén thànhmột vector — chitiết token bị bình quânhoá. Late interaction: giữ vector từng to-

### ken/patch, chấm điểm bằng MaxSim
score = ∑ t∈q maxd∈D cos(t, d) Mỗi token truy vấn tự tìm mảnh khớp nhất trong tài liệu ⇒bắtđược chi tiết mà single-vectorbỏ sót. ColPali: RAG không cầnOCR

- Encodeảnhtrang PDFtrựctiếp
(SigLIP-So400m)

- Lưới 32 × 32 = 1024patch/trang,mỗi patch
128d

- Bảngbiểu, biểu đồ, form scan:hếtlà bài
toántiền xử lý

- Họmodel: ColQwen2.5, ColSmolVLM,
ColInternVL Lưu ý: Chất lượng mua bằng dung lượng.1 triệu trang× 1024 patch× 128d × 4B ≈ 524GB (còn ∼30– 60GB sau quantization). Vector DB một-vector-một-documentkhông lưu nổi— cần hỗ trợ multi-vector + MaxSim (Qdrant,Milvus). Giảngviên (VinUni) AICB· Ngày 19 Tuần4 18 / 56

---

<!-- chiron-source-span: {"source_span_id":"150e9c2b-1596-5946-848b-230432593698","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"RAGPipeline: End-to-End Flow","extraction_method":"pdf-text-layer"},"checksum":"ce581ad01340b45e2888820db1f5d56f2354d0b1387e54dedac00a899d6d95ad"} -->

## Slide 21 - RAGPipeline: End-to-End Flow

Documents Chunking Embedding Vector DB 512 tokens 50 overlap text-embed-3 bge-m3 User Query Query Embed Retrieve Top-K LLM Generate

### Metadata filter
source, date≥ 2024 Giảngviên (VinUni) AICB· Ngày 19 Tuần4 19 / 56

---

<!-- chiron-source-span: {"source_span_id":"3c68387a-4057-5152-abc8-c14dd0db8804","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"ChunkingStrategies: Quyết Định80% Chất Lượng RAG","extraction_method":"pdf-text-layer"},"checksum":"826bf78485384fd4e340f74fe328362ca25acecb30179c68653f4acdb0e9a134"} -->

## Slide 22 - ChunkingStrategies: Quyết Định80% Chất Lượng RAG

4Strategies

- Fixed-size: 512tokens, baseline, ngắt giữa
câu

- Recursive: LangChain
RecursiveCharacterTextSplitter— tôn trọng câu/đoạn

- Semantic: similarity-based,nghỉ tại topic
shift— chậm + tốt nhất

- Hierarchical: parent(page) + child

```text
(paragraph),retrieve child, return parent
```
ProductionTuning

- Chunksize: 200–500tokens cho RAG, 1K+
cholong-context

- Overlap: 10–20%(~50–100 tokens)

- Tooling: LangChain,LlamaIndex,
Unstructured.io

- Vietnamese: tokenizeở sentence level,
khôngbyte-split Lưu ý: Đo bằng golden set:Recall@k cải thiện đáng kể khi switch fixed→ semantic trên benchmarks. Bad chunking= embedding tốt cũng vôdụng. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 20 / 56

---

<!-- chiron-source-span: {"source_span_id":"079504eb-fd3a-5810-81e5-f5db371c0e4f","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"RAG:Production Best Practices","extraction_method":"pdf-text-layer"},"checksum":"e04920b58be1332dc8851056f08c9aec1ab189510b0a0b0da71ddadebe4e74bb"} -->

## Slide 23 - RAG:Production Best Practices

RetrievalHyperparameters

- Top-K:5–10cho RAG, 20–50 trước reranker

- ef_search(HNSW):200 default, tăng cho
recall

- MMRdiversity: λ=0.5giảm chunks trùng

- Metadatafilter: khôngphảicứ “lọc sớm” —
xemslide Filtered Search ProductionGotchas

- Embeddingmodel consistency: train=
inference

- Queryrewriting: HyDE, multi-query
expansion

- Embeddingversioning + zero-downtime
re-index(Production Patterns)

- Monitorembedding drift hàng tuần
Lưu ý:Training và inferencephải dùng cùng embedding model version. Đổi model = re- indextoàn bộ. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 21 / 56

---

<!-- chiron-source-span: {"source_span_id":"4e75a8f4-496a-5f24-8847-ce1e26613f36","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"2-StageRetrieval: VectorSearch + Reranking","extraction_method":"pdf-text-layer"},"checksum":"9dec2c944c8cec491ad1c831d8a231ec082d2db2b82433a7961f593f1a6befae"} -->

## Slide 24 - 2-StageRetrieval: VectorSearch + Reranking

Stage1: Recall (nhanh)

- ANNsearch trả về top-100 candidates

- Bi-encoder: query & docembedriêng

- Latencythấp (<20ms), recall cao
Stage2: Precision (chínhxác)

- Cross-encoder: query + doccùnglúc

- Scorerelevance từng cặp (query,doc)

- Chọntop-10 chất lượng cao nhất
Rerankers2026 — chọn theo latencybudget

- Self-host+ GPU: bge-reranker-v2-m3,Jina
v3,Qwen3-Reranker — ∼50–200ms

- ManagedAPI: CohereRerank v4, zerank —
∼600ms, không cần GPU ⇒ Rerankcộngthẳng vào P99 EmbeddingModel Hosting

- Self-host: sentence-transformerstrên GPU
—kiểm soát, tiết kiệm ởscale lớn

- API:OpenAI text-embedding-3-small,
Cohereembed v4 + Rerank 3.5— đơn giản, triểnkhai nhanh Giảngviên (VinUni) AICB· Ngày 19 Tuần4 22 / 56

---

<!-- chiron-source-span: {"source_span_id":"4eb9aa81-1075-5f12-a239-3f5f0b6b70e1","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"“Cửasổ 1M token rồi, còncần RAG không?”","extraction_method":"pdf-text-layer"},"checksum":"339f9f1075ffb7ca50ce4c089796a86bc490b7205bfc294a36a6e5c3d0321d1f"} -->

## Slide 25 - “Cửasổ 1M token rồi, còncần RAG không?”

ContextRot (Chroma Research, 07/2025)

### 18model frontier,mở rộngtừ Needle-in-a-Haystack

- Chấtlượng giảmkhi input dài ra—kể cả task
đơngiản, và giảmkhôngđều giữacác model

- Modelcửa sổ 1M: hiệu ứngthường thấy rõ
quanh300–400Ktoken

- Multi-hop/ tổng hợp: gãysớmhơn nhiều

- Phụthuộc độ giống câu hỏi,nhiễu, cấu trúc —
đúng những biến mà retrieval kiểm soát Kinhtế học: mộtlần vs mỗi lần Nhồi cả corpus:trả tiền chotoàn bộ corpus ở mỗirequest. Retrieval: trả tiền indexmột lần, mỗi query chỉ trảcho phần đã chọn. Chênh lệch nhân theo QPS — đây là lý do RAG khôngbiến mất. Mặcđịnh 2026 Retrieve 50K–200K tokenliên quan, rồi mới để modellong-contextsuyluậntrênđó— lai,không phảichọn một. Cửasổ lớn làsứcchứa,không phảiđảmbảo. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 23 / 56

---

<!-- chiron-source-span: {"source_span_id":"9d404bc1-ed69-53a9-b78c-66cc1793a687","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"GraphRAG:Khi Quan Hệ Quan TrọngHơn Đoạn Văn","extraction_method":"pdf-text-layer"},"checksum":"7251fd8e8d0e8e9eda18f2c330d917a55218090770bd639fd513cd21cb3bc506"} -->

## Slide 26 - GraphRAG:Khi Quan Hệ Quan TrọngHơn Đoạn Văn

VectorRAG (chunks) q Top-K nearest chunks (cosine similarity) GraphRAG(entity-relation) Alice ProjectX Bob PayPal Mahle worked_on by at hired_by q Multi-hop: PayPal → Alice → Project X→ Bob → Mahle Câuhỏi mà vector RAG kém “Ai ở PayPal từng cộng tác với người được Mahle thuê?” — Vector trả về chunks về PayPal HOẶC Mahle riêng lẻ; không thể cross-document multi- hop. KG traverse 3-hoptrongµs. UseCases 2026

- P3Cdiabetes copilot(Memgraph): patient
journey+ drug interactions

- Alzheimerresearch: 1.6M edges nối
genes-drugs-trials

- M&Aintel (GlassDollar/Siemens,Mahle):
entitysearch across millions of companies F Vector RAG = “đoạn văn liên quan”. GraphRAG = “mối quan hệ kết nối nhiều entity” — chọn graphkhi câu trả lời làmộtrelationship,không phải đoạn text. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 24 / 56

---

<!-- chiron-source-span: {"source_span_id":"22fbf1d9-aec9-5eb1-a7c7-4a957d2f0a94","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"GraphRAGConstruction: Document →KnowledgeGraph","extraction_method":"pdf-text-layer"},"checksum":"ed208377bdeda758a3216f3d0ed09e90d27e8788576dadf8ae910d285ac9690d"} -->

## Slide 27 - GraphRAGConstruction: Document →KnowledgeGraph

Documents (text corpus) NER (spaCy / LLM) Entity Linking Relation Extraction Community Detection Indexed KG (Neo4j/Memgraph) “Alice”, “Project X” dedupe & canonical IDs (Alice, worked_on, Project X)

### Leiden algo
sub-graph clusters ToolingLandscape 2026

- MSGraphRAG:community summaries, chất
lượngcao, index đắt nhất

- LazyGraphRAG:hoãn extraction sang
query-time— index rẻ ngang vectorRAG

- LightRAG/Fast GraphRAG: index nhẹ

- Neo4j(Cypher)· Memgraph(in-memory,
sub-mstraversal) Vector +Graph: Layered (2026 default)

1. Start: vectorRAG cho conversational grounding

2. AddKG: domainnhiều thực thể (legal, medical,M&A)

3. Hybrid: vectorretrieve →KGexpand → LLM

4. Cost: fullextraction 5–20×;Lazy ≈vector RAG Lưu ý:Cost 2026 đã đảo chiều:LazyGraphRAG hoãn phần đắt sang query-time⇒ index bằng vector RAG (0,1% của full GraphRAG). “Graph quá đắt để thử”không còn là lý do hợp lệ— chọn theohình dạng câu hỏi, khôngtheo ngân sách index. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 25 / 56

---

<!-- chiron-source-span: {"source_span_id":"11ee80f1-3ef9-526d-80d9-4cb7a657a9f7","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"AgenticRetrieval: TruyXuất TrởThành Một CôngCụ","extraction_method":"pdf-text-layer"},"checksum":"cd5f5a130ea0ff885419ad274c6fa64fffd1b86157b4369d9f3f310efc7f2d76"} -->

## Slide 28 - AgenticRetrieval: TruyXuất TrởThành Một CôngCụ

ClassicRAG vs Agentic retrieval ClassicRAG —mộtlượt: embedquery →top-K → sinhcâu trả lời. Dùng chotra cứu đơn giản. Agentic retrieval— agentquyết định truy xuất thế nào: phântíchđộphứctạp,táchcâuhỏinhiềuphần, chọnnguồn, truy xuất nhiều vòng. Cái giá: thêm LLM call⇒ thêm latency + token. Khôngphảimặc định cho mọi query. Vònglặp agentic

1. Hiểuquery —đơn giản hay nhiều bước?

2. Lậpkế hoạch—cần nguồn nào, thứ tựnào

3. Truyxuất —vector / BM25 / KG/ SQL / API

4. Phảntỉnh —đã đủ bằng chứng chưa?

5. Lặplại nếuchưa đủ, rồi mới sinhcâu trả lời Hạ tầng đang mọc giao diện cho agent— Weaviate 1.37 (2026) nhúng sẵnMCP servertại /v1/mcp, cùng cổng với REST API — agent truy vấnvà ghi thẳng vào vector DB, không cần lớp tích hợp riêng. VectorDB không còn chỉlà thư viện phía sau, màlàmộtcông cụ agent gọi được(xemNgày 9: MCP). Giảngviên (VinUni) AICB· Ngày 19 Tuần4 26 / 56

---

<!-- chiron-source-span: {"source_span_id":"1a383c3b-df62-53b9-bab8-9f5f44e17640","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"AgentMemory & Semantic Cache: Hai Nửa Của Bài HômNay","extraction_method":"pdf-text-layer"},"checksum":"eaec0ebf64a4e52bc37d373e4b5d8f76769a17398d890f89a821a285beb1c0fe"} -->

## Slide 29 - AgentMemory & Semantic Cache: Hai Nửa Của Bài HômNay

Agentmemory = chính hai khocủa hôm nay Online storetrả lời “ta biết gì về usernày” (<10ms). Vectorstore trảlời “đã từng nói gìliên quan”.

### Bakiến trúc 2026

- Mem0: vector-first, trích “sựkiện” từ hội thoại

- Zep: knowledge graphtheo thời gian (Graphiti)

- Letta(ex-MemGPT):3 tầng core / recall/
archival Benchmark: LoCoMo, LongMemEval, BEAM. Semanticcache — đòn bẩy chiphí rẻ nhất Querymới gầnquerycũ(cosine >ngưỡng) ⇒trả lạicâu trả lời đã lưu.

### AWSđotrên63.796querythật (ngưỡng0,75)

- Chiphí inferencegiảmtới 86%

- Latencycảithiện 88%trêncache hit

- Độchính xác giữ∼91%
Lưuý: Cachesainguyhiểmhơnkhôngcache. 4kiểugãy: queryphụthuộcngữcảnh(giốngnhaunhưngcần đáp án khác) · query nhạy thời gian (trả lời cũ) ·đổi embedding model⇒ vô hiệu toàn bộ cache(đúng cái bẫy re-index)· cache nhầm một câubịa rồi phục vụ mãi. Ngưỡng similarity là tham sốphảiđo,không phải đoán. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 27 / 56

---

<!-- chiron-source-span: {"source_span_id":"7aa4ab60-d60b-52a2-aaec-63b3bc12ac42","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"RetrievalNhư Một Tool: Thứ Agent Thực Sự NhìnThấy","extraction_method":"pdf-text-layer"},"checksum":"24e50a9a710678c495fc3584107838e4b382653ee41739710e5bee0286127326"} -->

## Slide 30 - RetrievalNhư Một Tool: Thứ Agent Thực Sự NhìnThấy

```text
SEARCH_TOOL = {
```
"name": "search_docs",

### # this description IS the retrieval prompt
# the agent decides *from this text* when to call "description": ( "Search internal product docs. Use for questions " "about pricing, limits, API behaviour. Returns " "ranked chunks with source URLs." ),

```text
"input_schema": {
```
"type": "object",

```text
"properties": {
"query": { "type": "string"},
"product": { "type": "string",
"enum": [ "core", "billing", "api"]},
"top_k": { "type": "integer", "default": 8},
},
```
"required": [ "query"], }, } Bốnđiều quyết định chất lượng

- description làprompt truy
xuất—agent chỉ có nó đểquyết địnhgọi hay không. Mơ hồ⇒ gọisai lúc.

- Filterlà enum,không phải string
tựdo ⇒agentkhông bịa giá trị

- Trảvề citation + score,không
chỉtext — để LLM (vàbạn) truy nguồn

- top_kcótrần —nếu không,
agenttự làm loãng context Giảngviên (VinUni) AICB· Ngày 19 Tuần4 28 / 56

---

<!-- chiron-source-span: {"source_span_id":"dff3d5d1-e67f-50a9-a137-ca26dc1ba7ec","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"GhépNgữ Cảnh: NơiFeature Store Gặp VectorStore","extraction_method":"pdf-text-layer"},"checksum":"044a8ee9a618403ea6210c7b9fa2f3aa8c643b414d8eafb89981fb1ce78efe2d"} -->

## Slide 31 - GhépNgữ Cảnh: NơiFeature Store Gặp VectorStore

```text
def build_context(user_id: str, question: str) -> str:
# 1) WHO is this user? online store, <10 ms
f = store.get_online_features(
features=[ "user_profile:topic_affinity",
```
"user_profile:preferred_language"], entity_rows=[{ "user_id": user_id}], ).to_dict() # 2) WHAT is relevant? vector search + filter hits = vdb.search( embed(question), top_k=8, filter={ "lang": f[ "preferred_language"][0]}, ) # 3) personalise, THEN ground

```text
return PROMPT.format(
affinity=f[ "topic_affinity"][0],
docs= "\n".join(h.text for h in hits),
)
```
Haicâu hỏi khác nhau Feature storetrả lời“user này là ai” → cánhân hoá. Vectorstore trảlời “cái gì liên quan” → grounding. Cá nhân hoá mà không grounding= bịacóduyên. Groundingmàkhôngcá nhânhoá =đúngnhưng vô hồn. Ngânsách Feature lookup <10ms — gần như miễn phísovớimộtLLMcall. Đừngtiếc nó. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 29 / 56

---

<!-- chiron-source-span: {"source_span_id":"881b456f-e06a-5e19-80ed-f96f06bf1b7c","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"SemanticCache: Hiện ThựcTrong12 Dòng","extraction_method":"pdf-text-layer"},"checksum":"ed5d035edb03283dcd253a6f1b76b2d07942a205f8aa21d9c0c61b1759fa9157"} -->

## Slide 32 - SemanticCache: Hiện ThựcTrong12 Dòng

```text
def cached_answer(user_id, q, threshold=0.75):
qv = embed(q)
```
# namespace per tenant: NEVER share across tenants hit = cache.search( qv, top_k=1, filter={ "tenant": tenant_of(user_id)}, )

### if hit and hit[0].score >= threshold

```text
return hit[0].payload["answer"] # HIT
ans = llm(build_context(user_id, q)) # MISS
cache.upsert(
qv, { "answer": ans, "q": q},
ttl=3600, # must expire
)
return ans
```
Batham số, ba loại lỗi

- thresholdquáthấp ⇒trảnhầm
câutrả lời của câu hỏikhác.Phải đo, đừng đoán (AWSdùng 0,75).

- ttlthiếu ⇒câutrả lời cũ sống mãi

- namespacethiếu ⇒userA nhận
câutrả lời chứa dữ liệuuser B — đâylà lỗhổng bảo mật,không phảibug cache Lưuý: Đổiembedding model ⇒xoá sạchcache. Vectorcũvà mới không cùngkhông gian. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 30 / 56

---

<!-- chiron-source-span: {"source_span_id":"accb8a42-35b9-5339-b6e5-a0eb0269e19b","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"DebugAgent + Retrieval: TriệuChứng→CáchSửa","extraction_method":"pdf-text-layer"},"checksum":"439593eed04bf5d985e0ff1aa2dd58357c6b94ed92ddff5c49db43839fc60c86"} -->

## Slide 33 - DebugAgent + Retrieval: TriệuChứng→CáchSửa

Triệuchứng Nguyênnhân thường gặp Cáchsửa Agentgọi search5–6lầnrồi bỏcuộc description mơ hồ, hoặc filter quáchặt trả về rỗng Viết lại description; log filter thựctế agentsinh ra Trả lời chung chung dù tài liệuđúng cótrongtop-K top_k quá lớn→ context loãng (contextrot) Giảm top_k,thêm reranker Chạy đúng lúc demo, sai trênproduction Querythật khác golden set Log query thật, refresh golden set hàngtuần Câutrả lời cũ dai dẳng Semantic cache không TTL / khônginvalidate TTL + xoá cache khi tài liệu nguồn đổi Agent làm theo “lệnh” nằm trongtài liệu Prompt injection qua retrieved doc Tách data khỏi instruction; re- trieved text không được điều khiểntool Giảngviên (VinUni) AICB· Ngày 19 Tuần4 31 / 56

---

<!-- chiron-source-span: {"source_span_id":"002b154d-50a2-5b10-acd8-f8deea512362","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"FeatureEngineering: 6 HọFeature Bạn Sẽ ViếtĐi ViếtLại","extraction_method":"pdf-text-layer"},"checksum":"61e03f2081aafe6e9b2d48386fe4b6c41f76aa5597142a2e501a73d22601514b"} -->

## Slide 34 - FeatureEngineering: 6 HọFeature Bạn Sẽ ViếtĐi ViếtLại

Bốnhọ “kinh điển”

1. Aggregationtheo cửa sổ— count/sum/avg 5phút, 1giờ, 7ngày. Xương sống của fraud & recsys.

2. Tỷlệ & chuẩn hoá— amount / avg_7d của chính user đó. Bắt bất thườngtươngđối.

3. Lag& delta—giá trị kỳ trước, độthay đổi. Choxu hướng.

4. Recency— now - last_event. Feature rẻ nhấtmà mạnh bất ngờ. Haihọ “dễ sai”

5. Mãhoá categorical—one-hot (ít giá trị), frequency/targetencoding (nhiều giá trị). Targetencoding phải fit trongfold,nếu khônglà leakage.

6. Embeddinglàm feature—vector user/item đithẳng vào model. Cầu nối sang nửa đầu bàihôm nay. Mẹođặt tên <entity>_<phép tính>_<c￿ a s￿ > — ví dụ user_txn_count_7d. Tên tự mô tả cửa sổ thì PIT joinvà debug đỡ đau. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 32 / 56

---

<!-- chiron-source-span: {"source_span_id":"adda1eb1-6316-529c-b7d2-a61ea12c0eb1","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"TừÝ Tưởng ĐếnFeatureView: Code Thật (Lab19)","extraction_method":"pdf-text-layer"},"checksum":"50fe948754493bcffbdaa791b38b8044414e435e610a23f6019ff1143531683a"} -->

## Slide 35 - TừÝ Tưởng ĐếnFeatureView: Code Thật (Lab19)

```text
from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Int64
user = Entity(name= "user", join_keys=[ "user_id"])
src = FileSource(
path= "data/query_velocity.parquet",
timestamp_field= "event_timestamp", # PIT join key
)
query_velocity_features = FeatureView(
name= "query_velocity_features",
entities=[user],
ttl=timedelta(hours=1), # stale after 1h
schema=[Field(name= "queries_last_hour", dtype=Int64)],
source=src,
online=True, # -> online store
)
```
Bốnquyết định trong 20 dòng

- entities —khoá tra cứu lúc
serving

- timestamp_field —không
cónó thì không có PITjoin, vàbạn sẽ leak

- ttl—“cũ bao lâu thì vô
nghĩa”

- online=True —tốn tiền, chỉ
bậtkhi serving cần feast apply → feast materialize-incremental Giảngviên (VinUni) AICB· Ngày 19 Tuần4 33 / 56

---

<!-- chiron-source-span: {"source_span_id":"f2c229a3-28a5-5877-802b-8ea3588bc7d8","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"On-DemandFeature: Tính TạiThời Điểm Request","extraction_method":"pdf-text-layer"},"checksum":"3b937909d04866adc7b0e222d902d4ed0e1630624720c50c39dbc1823ae2f86d"} -->

## Slide 36 - On-DemandFeature: Tính TạiThời Điểm Request

```text
from feast import Field, RequestSource
from feast.types import Float64
# feast 0.65: importing this from `feast` gives the MODULE
from feast.on_demand_feature_view import on_demand_feature_view
```
# amount exists only at request time txn = RequestSource( name= "txn", schema=[Field(name= "amount", dtype=Float64)], ) @on_demand_feature_view( sources=[user_spend_stats, txn], # stored + request schema=[Field(name= "amount_vs_avg", dtype=Float64)], mode= "python", )

```text
def amount_vs_avg(inputs):
pairs = zip(inputs["amount"], inputs[ "avg_amount_7d"])
return {"amount_vs_avg":
[a / m if m else 0.0 for a, m in pairs]}
```
Vìsao cần on-demand? Số tiền giao dịch chưa tồn tại lúc materialize — không thể pre-compute. Nhưng amount/avg_7d lại là feature mạnhnhất của fraud. On-demand ghépfeature đã lưu với dữ liệu requestvàáp cùngmộtcôngthức chocả training lẫn serving.

### Lưuý
write_to_online_store=True ⇒tính lúc ghi;mặc định False ⇒lúc đọc. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 34 / 56

---

<!-- chiron-source-span: {"source_span_id":"3aaac1ac-0370-56b4-9919-eefeddb84d8a","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"FeatureStores: Uber Michelangelo→FeastLF AI&Data","extraction_method":"pdf-text-layer"},"checksum":"ca615867d9e7b6a48a84b461b308be35a9eba5e372bd5869a8ac9003633676ba"} -->

## Slide 37 - FeatureStores: Uber Michelangelo→FeastLF AI&Data

Uber Michelangelo Feast (Gojek+GCP) Tecton founded Hopsworks/ DatabricksFS VertexAI FeatureStore Feast → LFAI&Data 2017 2019Jan 2019 2020–21 2021 2024Aug Internal platform for 100+ models OSS reference implementation Ex-Uber team, enterprise SaaS Notebook-native + lakehouse FS Managed FS trên GCP Vendor-neutral open governance Whyfeature stores emerged Uber có 100+ ML models reuse cùng features (rider price, driver ETA)⇒ centralize để tránh skew + duplicate compute. LLM-era twist:feature stores giờ host cảembedding feature views (user/item vectors) bên cạnh tabular features— một hệ thống chocả ML cổ điển và RAGpersonalization. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 35 / 56

---

<!-- chiron-source-span: {"source_span_id":"f01fe43e-703b-5f7d-8258-587cc31aabc1","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"FeatureStore Architecture","extraction_method":"pdf-text-layer"},"checksum":"ffa274dbcc85c55856aae94fd17b4b28ca83ea1dc095773d79772cdc0e683972"} -->

## Slide 38 - FeatureStore Architecture

Feature Registry Offline Store S3 / BigQuery Online Store Redis / DynamoDB materialize Training Pipeline batchfeatures Inference Service <5ms lookup Single source of truth= No skew Train: df.mean() vs Serve: running_mean ⇒ bug! Giảngviên (VinUni) AICB· Ngày 19 Tuần4 36 / 56

---

<!-- chiron-source-span: {"source_span_id":"5539e72f-8cb6-5824-a320-9631c9b7d283","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Feast: Define & ServeFeatures","extraction_method":"pdf-text-layer"},"checksum":"77f7e064ee6e633e8bc23abadc8945dd8248a2bbaae2b584a1f6b8adcfee3998"} -->

## Slide 39 - Feast: Define & ServeFeatures

FeatureDefinition

- FeatureView(name="user_features")

- Entities: ["user_id"]

- TTL: timedelta(days=30)

- Source: Delta/Iceberg tables (N18)
Materialize& Freshness

- feast materialize-incremental

- Batchfeatures: daily updatelà đủ

- Streamingfeatures: cần sub-second

- Feast0.65 (07/2026,LF AI&Data — release
hàng tháng,phải pin version): Push API, on-demandtransformations (Beta), streamingtransformations (Alpha) OnlineLookup

- store.get_online_features()

- Latency: <5ms per request

- Batch: 1000 entity rowsat once
FeastAlternatives

- Tecton: fullymanaged, real-time features

- Databricks: FeatureEngineering in Unity
Catalog(WorkspaceFS đã legacy)

- VertexAI FS:GCPmanaged service

- Hopsworks: regulatedindustries, on-prem
Giảngviên (VinUni) AICB· Ngày 19 Tuần4 37 / 56

---

<!-- chiron-source-span: {"source_span_id":"5a7db014-fd85-539c-bb83-0fcae47d8011","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Onlinevs Offline Store + Point-in-TimeJoin","extraction_method":"pdf-text-layer"},"checksum":"7a7e59e077a1419490cae90d7cdb2a12f27dd036c4a575021b10b12d39fc6f8e"} -->

## Slide 40 - Onlinevs Offline Store + Point-in-TimeJoin

OfflineStore (training)

- Parquettrên S3 / Delta /Iceberg

- Snowflake/ BigQuery / Redshift

- Workload: historicalbatch, 100GB–TB

- Latency: seconds–minutes(OK for training)

- Lưu full history củamọi feature value
OnlineStore (serving)

- Redis/ DynamoDB / Cassandra /Aerospike

- Workload: per-entityKV lookup

- Latency: <10ms P99

- Lưu current value only (nohistory)

- Feast materialize() nạpoffline →online
Point-in-Time (PIT) Join — Khi build training set: lấy feature as- of timestamp của mỗi event — không dùng giá trị tương lai. Feast get_historical_features(entity_df) thực hiện PIT join trên offline store. Sai lầm:dùng LATEST value⇒ data leakage ⇒ prod accuracy thấp hơn training 20–30%. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 38 / 56

---

<!-- chiron-source-span: {"source_span_id":"ead56a73-779f-5a89-b6c6-2bed9a0c9836","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"FeatureStores 2026: Feastvs Tectonvs Hopsworks","extraction_method":"pdf-text-layer"},"checksum":"85ef16b00aa85fbbd50c6d3357c4069139842f550f26e54c571d383c71b9430a"} -->

## Slide 41 - FeatureStores 2026: Feastvs Tectonvs Hopsworks

Feast(open-source)

- LFAI&Data, cộng đồng
mạnh

- PushAPI, on-demand
transformations(Beta)

- Self-host: nhẹ, kiểm
soáthoàn toàn

- Bestfor: team
nhỏ–vừa,full control Tecton(managed)

- Real-timefeatures,
sub-secondfreshness

- DAGschedulingtựđộng

- EnterpriseSLA, RBAC,
lineage

- Bestfor: ML-heavy
productteams, latency SLAnghiêm ngặt Hopsworks

- On-prem+ cloud, data
governance

- Tíchhợp Spark + Flink
streaming

- Lineage,versioning,
GDPR-ready

- Bestfor: regulated
industries(ngân hàng, y tế) Lưuý: DatabricksWorkspaceFeatureStoređãlegacy(2024). Migratesang Feature Engineering in Unity Catalog—không tạo mới project vớiWorkspaceFS. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 39 / 56

---

<!-- chiron-source-span: {"source_span_id":"c3c30d50-0e4f-527a-9429-d7dc31a98179","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Training-ServingSkew: LỗiThầm Lặng","extraction_method":"pdf-text-layer"},"checksum":"17791820cc826e7ac455a8787d5cbec8030726833b184b6461a09d8dd1db8f82"} -->

## Slide 42 - Training-ServingSkew: LỗiThầm Lặng

Skewlà gì? Featuretính khácnhau giữatrainingvàservingdẫn đến model hoạt động kém khi deploy mà không có lỗirõ ràng. Vídụ 1: Aggregation

- Training: pd.DataFrame.mean() trêntoàn bộ
dữliệu lịch sử

- Serving: running_mean(last_N) chỉN bản
ghigần nhất

- ⇒Giátrị khác nhau, model sailệch
Vídụ 2: DateParsing

- Training: parsedatetime UTC

- Serving: parselocal timezone

- ⇒Feature“giờ trong ngày” lệch 7h(VN)
Lưuý: FeatureStoregiảiquyếtskew: mộtđịnh nghĩa duy nhấtdùng cho cả training lẫn inference —không code riêng. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 40 / 56

---

<!-- chiron-source-span: {"source_span_id":"60fae4a8-2689-56b9-b360-91f61afe047d","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"StreamingFeature Pipelines: Sub-SecondFreshness","extraction_method":"pdf-text-layer"},"checksum":"cc8fee89853d9c112935c3e8e653e5d859f98d646b008dd37b3f09eac477d36d"} -->

## Slide 43 - StreamingFeature Pipelines: Sub-SecondFreshness

OLTPDB (Postgres) CDC (Debezium) Kafka topic Flink/ SparkStream OnlineStore (Redis) Offline (S3/Delta) rawevents tumbling/slidingwindow Streamingpatterns CDC:mọiUPDATErow →Kafkaevent Aggregate: txnvelocity 5min / 1h window Feast Push API:app push trực tiếp event→ online store Khinào cần streaming Có: fraud detection, dynamic pricing, real-time rec- sys Không cần: churn prediction (daily batch OK), creditscoring Giảngviên (VinUni) AICB· Ngày 19 Tuần4 41 / 56

---

<!-- chiron-source-span: {"source_span_id":"2b376bb0-ba30-564a-8d4c-7d59a80fc955","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"FeatureStore trong ML Production: 3 Use Cases","extraction_method":"pdf-text-layer"},"checksum":"85606142352813b3220caf4035ddfeb0b2d30590892716ca63e94281335ff4d6"} -->

## Slide 44 - FeatureStore trong ML Production: 3 Use Cases

FraudDetection (PayPal, Wise)

- Latency: <10ms (per
transaction)

- Features: velocity
(txn/min),device fingerprint, amount-vs-7d-avg

- Freshness: streaming
(Kafka →Redisonline store)

- Tooling: Tecton+ Redis
cluster;Feast + Aerospike RecommendationSystems (DoorDash, Spotify)

- Latency: <50ms
(homepage personalization)

- Features: user
embedding,last-N interactions,item popularity

- Freshness: hybrid(daily
user-batch+ stream last click)

- Tooling: Tecton
(DoorDash,Atlassian); Hopsworks(regulated) DynamicPricing (Uber,Grab)

- Latency: <100ms (price
atsearch)

- Features: demand
surge,supply,competitor price,time-of-day

- Freshness: sub-second
(streamingdemand signal)

- Tooling: Tecton
end-to-endDAG, managedtransformations G Feature Store thắng ở3 dimensions: feature reuse + train/serve consistency + low-latency lookup— không tool nào khácgiải quyết cả 3. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 42 / 56

---

<!-- chiron-source-span: {"source_span_id":"d0166bac-ad7e-5027-98ae-51fce41f73d2","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"HộiTụ: Feature StoreChính Là VectorStore","extraction_method":"pdf-text-layer"},"checksum":"4bf2b51ca3317234c53bc40f65a81c1949b674bd1c6f9c1dcf6208c3a46ac0e9"} -->

## Slide 45 - HộiTụ: Feature StoreChính Là VectorStore

Feast0.65: online storecó thể là vector DB

- Onlinestore nay gồm cảQdrant,Milvus,
FAISS—bên cạnh Redis, DynamoDB, Cassandra,Postgres…

- Vectorsearch trongFeast: trạng tháiAlpha,
nằmdưới nhánh roadmap “NLP”

- On-demandtransformations (Beta),
streamingtransformations (Alpha) Nghĩalà gì với kiến trúccủa bạn?

### Mộtregistry phụcvụ đồng thời

- featuredạng bảng (txn_count_7d)

- embeddingfeature view(vectoruser/item)
…cho cùng một model, qua cùng một lần online lookup — cùng định nghĩa, cùng PIT join, cùng chốngskew. D Hainửacủabàihômnayđangnhậplàmmột: RAGcần ngữ cảnh cá nhân hoá (feature),còn MLcổđiểnngàycàngdùng embeddinglàmfeature. Đừngdựnghaihệthốngsongsongnếu mộtcái đủ. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 43 / 56

---

<!-- chiron-source-span: {"source_span_id":"41a9f0a1-beef-52c6-9f9c-7f793cc8ba7a","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"EmbeddingLà Một Feature:vector_index TrongFeast","extraction_method":"pdf-text-layer"},"checksum":"d27b2013cc07a9ddb210ac06e4f514b4a377e5cbac04f95a979bef703abc1b33"} -->

## Slide 46 - EmbeddingLà Một Feature:vector_index TrongFeast

# 1) an embedding declared like any other field document_embeddings = FeatureView( name= "embedded_documents", entities=[item], schema=[ Field(name= "vector", dtype=Array(Float32), vector_index=True, vector_search_metric= "COSINE"), Field(name= "sentence_chunks", dtype=String), ], source=rag_documents_source, ttl=timedelta(hours=24), ) # 2) retrieved by similarity, not by key ctx = store.retrieve_online_documents_v2( features=[ "embedded_documents:vector", "embedded_documents:sentence_chunks"], query=query_embedding, top_k=3, ).to_df() Điềugì vừa xảy ra? Cùng FeatureView API, cùng registry, cùng TTL — nhưng tra cứu bằngđộ tươngđồng thayvì bằngkhoá.

### RAG corpus giờ là một feature view
có schema, lineage, versioning, PIT semantics.

### online_store
type: milvus vector_enabled: true Alpha — Milvus, SQLite, Qdrant, PGVector. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 44 / 56

---

<!-- chiron-source-span: {"source_span_id":"9c67e46e-9b02-52eb-9155-059fdc96015c","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"VectorSearch: ProductionOptimization","extraction_method":"pdf-text-layer"},"checksum":"94c531e1aff80659bb1f314660b6e7a5ef1dd15a589b6b28a162edd37dade03a"} -->

## Slide 47 - VectorSearch: ProductionOptimization

Caching& Batching

- Embeddingcache: RedisTTL 24h

- Hitrate 60–80%, giảm embedding cost

- Batchembedding: 1000texts/request

- Throughput50 ×,cost giảm 90%
MonitoringSearch Quality

- Trackrelevance score distribution theo tuần

- Nếuavg similarity giảm: điều tra embedding
drift,data quality,query distribution

- P99latency + index size growth
Multi-tenancy

- Namespaceisolation (Pinecone)

- Collectionper tenant (Qdrant)

- Security+ billing separation

- Cảnhbáo: lọcbằng metadata = isolation
mềm;1 bug filter⇒ròdữ liệu chéo tenant (OWASPLLM08 — xem slide Security) IndexLifecycle Management

- CreateV1 →ingest →serve

- Update: build V2 offline→validatequality

- Blue-greenswitch →retireV1

- Rollbackngay nếu quality giảm
Giảngviên (VinUni) AICB· Ngày 19 Tuần4 45 / 56

---

<!-- chiron-source-span: {"source_span_id":"02263e11-0ca5-5b5f-a4dc-b00ac44ce1b0","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"RetrievalEvaluation & Observability","extraction_method":"pdf-text-layer"},"checksum":"6e8c54aecd2260c214408831d9d6f76ce239288aa3cedf47cd142c468877e617"} -->

## Slide 48 - RetrievalEvaluation & Observability

OfflineMetrics (Golden Set)

- Recall@k: tỷ lệ relevantdocs trong top-k

- MRR:vị trí trung bình củakết quả đúng đầu
tiên

- nDCG@k: xếp hạng chấtlượng có weight

- Build200-querygoldenset—regression-test
mỗilần đổi embedding hoặc chunkstrategy OnlineMetrics (Production)

- P99search latency + embedding latency

- Embeddingcache hit rate (target>60%)

- Querydistribution drift (alert nếu avg
similaritygiảm)

- Indexsize growth rate (trigger re-balancekhi
>120%) RAG-specific: LLM-as-Judge

- ContextRelevance: retrievedchunkscóliên
quankhông?

- AnswerRelevance: câu trả lờicó trả lời
querykhông?

- Groundedness: câu trả lờicó dựa trên
contextkhông? ⇒ RAGAS:faithfulness, answer relevancy, contextprecision ObservabilityTooling

- Langfuse(open-source,OTel): tracing +
evaltích hợp

- Phoenix/Arize: OpenTelemetry-native,RAG
tracing

- LangSmith: LangChain-native, prompt +
retrievaldebug

- Chọn1 tool — instrument từngày đầu tiên
Giảngviên (VinUni) AICB· Ngày 19 Tuần4 46 / 56

---

<!-- chiron-source-span: {"source_span_id":"86107879-9cc9-5bf7-9e43-5b2e86ef32c2","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"BảoMật & TuânThủ: VectorStore LàKho Dữ Liệu Cá Nhân","extraction_method":"pdf-text-layer"},"checksum":"0d742279f2e4efd46bca01d02ae5b062a5506d0c6c38ffa10d8eb01ca41edce2"} -->

## Slide 49 - BảoMật & TuânThủ: VectorStore LàKho Dữ Liệu Cá Nhân

OWASPLLM08:2025

- Embeddinginversion: táidựng văn bản gốc
từvector ⇒embeddingkhông phải ẩn danh hoá

- Ròchéo tenant: táchbằng metadata filter là
isolation mềm—một bug là rò toànbộ

- Retrievalpoisoning: tàiliệu độc nhét vào
corpusđể lái câu trả lời LuậtViệtNam đã có hiệulực PDPL — Luật 91/2025/QH15 (hiệu lực 01/01/2026), Nghị định 356/2025: quyền chủ thể dữ liệu,DPO bắt buộc, đánh giá tác động,báo cáoviphạmtrong72h (24hnếubịtấncônghệ thống),chếtài hình sự. Ápdụngcảtổchứcnước ngoàixử lý dữ liệu tạiVN. LuậtAI—134/2025/QH15 (hiệulực 01/03/2026), tham chiếu EU AI Act. Chuyển tiếp

### đến 01/03/2027 (y tế, giáo dục, tài chính
01/09/2027). Lưu ý:Quyền được xoá gặp index ANN bất biến.Một yêu cầu xoá phải lan tớiindex vector + mọi dòng đã materialize sang online store + semantic cache. Thiết kế đườngxoátrướckhi ingest. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 47 / 56

---

<!-- chiron-source-span: {"source_span_id":"e50a9b29-69bc-5b45-b503-278ac1cccf26","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"ChiPhí Một Hệ Retrieval: Cộng Đủ 5 Khoản","extraction_method":"pdf-text-layer"},"checksum":"28611db84df9d6a54f2f49de0504b82fce2f1e82c3b0cd36050f3418dee4d380"} -->

## Slide 50 - ChiPhí Một Hệ Retrieval: Cộng Đủ 5 Khoản

5khoản chi

1. Embedding—một lần cho corpus +delta mỗingày

2. Lưuindex —dims ×bytes ×sốvector, sau quantization

3. Querycompute —QPS ×tầnglưu trữ (RAM/SSD/S3)

4. Reranker—mỗi query,cộng thẳngvào P99

5. LLMgeneration —thườnglàkhoản lớn nhất 5đòn bẩy (theo thứ tựhiệu quả)

1. Semanticcache —cắt cả khoản 4 và5

2. Quantization—int8 4×,binary 32×trên khoản2

3. Chọnđúng tầng—object storage cho corpusít truy vấn

4. Matryoshka—cắt dims, cắt luôn RAM

5. Top-Knhỏ hơn—ít token vào LLM hơn Lưu ý:Khoản không ai lập ngân sách:re-index. Đổi embedding model = trả lạitoàn bộ khoản 1 + dựng index song song (blue-green) = tạm thờigấp đôikhoản 2. Hãy coi nó là chi phí định kỳ, không phải sự cố. (FinOps sâu hơn: Ngày 25.) Giảngviên (VinUni) AICB· Ngày 19 Tuần4 48 / 56

---

<!-- chiron-source-span: {"source_span_id":"4d26b078-d8e4-5746-8dbc-1a046e64041e","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"EnterpriseCase Studies: ROItừ Vector+ Feature Store","extraction_method":"pdf-text-layer"},"checksum":"48503bc7be85bce2941708d52d831faa75cab0cbaa027eacd43ae08e16a8aaba"} -->

## Slide 51 - EnterpriseCase Studies: ROItừ Vector+ Feature Store

40% GlassDollar (Qdrant) hạ tầng cost↓ 3× GlassDollar user en- gagement 1.6M Alzheimer KG edges (Mem- graph) <10ms PayPal fraud feature lookup Vectorwins GlassDollar (Qdrant): NL search Siemens/Mahle, 40%cost ↓,3 ×engagement. Memgraph P3C: KG 1.6M edges, sub-ms multi-hop traversalcho Alzheimer + diabetes. FeatureStore wins PayPal: Tecton+streaming,<10ms/txn fraud lookup. DoorDash: Tecton DAG, sub-second pricing cho 60M+orders/tháng. H ROIđođược: 40%cost ↓+3 ×engagement(GlassDollar)+ <10msfeaturelookup(PayPal). Khôngphải hype. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 49 / 56

---

<!-- chiron-source-span: {"source_span_id":"de9a0933-4359-5625-94bc-fde98dcdbbab","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"Vector& Feature Store: ML Era vs LLM Era","extraction_method":"pdf-text-layer"},"checksum":"76ccb9c0f709986a5c5a9d4682d5a2827c54dc1d2d885d123f40a08946214bd8"} -->

## Slide 52 - Vector& Feature Store: ML Era vs LLM Era

MLEra (2015–2022)

- Vectorstore role:candidategeneration cho
recsys;retrieval cho face / imagesearch

- Embeddings: task-specific(FaceNet,
two-towerrecsys, doc2vec); train per-app

- Indextooling: FAISS/ Annoy / NMSLIB
embeddedtrong app process

- Featurestore: tabularfeatures (counts,
ratios,lags) cho XGBoost / DNNtabular

- Freshness: daily/ hourly batch là mặcđịnh;
streamingchỉ cho fraud LLMEra (2023–2026)

- Vectorstore role:RAGretrieval, agent
memory,semantic cache

- Embeddings: foundationmodels (OpenAI,
BGE,Voyage);một model nhiềuuse case

- Indextooling: managedmulti-tenant
(Pinecone,Zilliz Cloud, VertexVector)

- Featurestore: tabular plusembedding
views;on-demand transforms cho prompt context

- Freshness: sub-secondstreaming là
baselinecho fraud, pricing, real-time recsys Giảngviên (VinUni) AICB· Ngày 19 Tuần4 50 / 56

---

<!-- chiron-source-span: {"source_span_id":"878ec397-598f-5e03-a9a1-ba2852c5937c","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"Wiki/CodeWiki/ DocWiki: RAG TrênChính Repo Của Bạn","extraction_method":"pdf-text-layer"},"checksum":"a705689b2d6c672c36705a2d9af35951b8c1a64309ea62ca84f872686f88a312"} -->

## Slide 53 - Wiki/CodeWiki/ DocWiki: RAG TrênChính Repo Của Bạn

Wiki(repo →trang) Sinh tài liệutự động từ source code. DeepWiki (Cognition): đổi github.comthành deepwiki.com là có wiki. Hơn 50.000 repo đã index (2026), kèm sơ đồ Mermaid và MCP server để agenttruy vấn (Ngày 9). CodeWiki(hỏivề code) Hỏibằngngônngữtựnhiên,trả lờikèm tríchdẫn file + dòng. “Hàm nào xử lý retry?”→ đoạn codethật, không phải đoán. Chínhlà2-stageretrieval+cita- tioncủa §4, áp lên code. DocWiki(docscho agent) Tài liệu được viết đểmáy đọc, khôngchỉ người. llms.txt, docs-as-code, mark- downthay HTML. Mintlify: gầnmộtnửa lưulượng vào trang tài liệu nay đến từ agent. E Cả bakhông phải sản phẩm mới— chúng là đúng những mảnh của hôm nay: chunk→ embed →index →hybridsearch →rerank →agenticretrieval →sinhcâutrảlờicótríchdẫn. Bạnđã đủ kiến thức đểtự dựng một cái. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 51 / 56

---

<!-- chiron-source-span: {"source_span_id":"7eade192-99ba-529f-b617-30a4a98b7a70","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"CodeWiki: Vì Sao Chunk CodeKhác Chunk Văn Bản","extraction_method":"pdf-text-layer"},"checksum":"a2098e83a6ea32856a4af2877768e0927c3c79eb589a16fb2feb162824bb4455"} -->

## Slide 54 - CodeWiki: Vì Sao Chunk CodeKhác Chunk Văn Bản

Chiatheo ký tự = hỏng

### Textsplitter cắt theo số ký tựsẽcắtđôi một hàm

- Embeddingcủa nửa hàm không mangnghĩa
gì

- Mất import,mất signature, mất scope

- Retrievevề một mảnhkhông chạy được
Vănbảnchịuđượccắtgiữacâu. Codethìkhông— nghĩanằm ởkhối,không ở dòng. Chiatheo AST = đúng Cắt tại ranh giới cú pháp(hàm, class, method) bằng tree-sitter; mỗi chunk mang theo scope chain,imports, signature. cAST (CMU, arXiv 2506.15655): chunk theo AST cho +4,3 điểm Recall@5trên RepoEval và+2,67 Pass@1trênSWE-bench. Nốilạivới§5GraphRAG — Code vốn dĩ làmộtđồthị: hàmgọihàm,moduleimportmodule,classkế thừa class. Câu hỏi “đổi hàm này thì hỏng chỗ nào?” là câu hỏimulti-hop — đúng loại mà vector RAG kém và graphtraversal mạnh. NênCodeWiki tốt = vector (tìm đoạnliên quan)+callgraph (lần theo phụ thuộc). Giảngviên (VinUni) AICB· Ngày 19 Tuần4 52 / 56

---

<!-- chiron-source-span: {"source_span_id":"72f765d8-99cf-59b8-845b-bca3bbd94144","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"DocWiki: Tài Liệu Giờ ĐượcĐọc Bởi Agent","extraction_method":"pdf-text-layer"},"checksum":"b166b916fd65f0b119419e348ec6c8de41a019179e2dd1c83aef056d6cacb08a"} -->

## Slide 55 - DocWiki: Tài Liệu Giờ ĐượcĐọc Bởi Agent

llms.txt —sitemap cho LLM Một file markdown ở/llms.txt chỉ cho agent biết nội dungnằm ở đâu, thay vìbắt nó crawl HTML.

- Phâncấp: file gốctrỏ tới index từng mục⇒
agentchỉ lấy phần cần,tốnít token hơn

- Mặcđịnh trên Mintlify,Fern,GitBook, Vercel,
Supabase

- Chưaphải chuẩnIETF/W3C— vẫn là đề xuất
cộngđồng Viếtdocs khác đi thế nào?

- MarkdownthayHTML nặng

- Mỗitrang tựđứng được—agent hiếm
khiđọc trang trước đó

```text
■ Vídụ codechạyđược,có import đầy đủ
```

- Tiêuđề mô tảnhiệm vụ,không phải
marketing Lưu ý:Đây làchunking chiến lượcở tầng tổ chức: bạn đang quyết định trước hệ thống retrieval của người khác sẽ cắt tài liệu của bạn thế nào. Trangviết rời rạc, phụ thuộc ngữ cảnh trang khác⇒chunk vô nghĩa⇒agent trảlời sai về sản phẩm của bạn. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 53 / 56

---

<!-- chiron-source-span: {"source_span_id":"5219f72a-e832-5529-95cc-0d1b11a62648","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"Demo: Semantic Search vớiWeaviate","extraction_method":"pdf-text-layer"},"checksum":"49be24888e40d7020934cdf64202f8cabae091713b6811d33c8c549058a9d565"} -->

## Slide 56 - Demo: Semantic Search vớiWeaviate

1. Ingest10,000documents VietnamesevàoWeaviatevớibge-m3embeddings (multilingual,tiếng Việtprod 2026)

2. Semanticsearch: “tìmtài liệu về cloud computing”→top5 results với similarityscores

3. Sosánh: keywordsearch vs semantic vs hybrid —semantic thắng trên paraphrasedqueries

4. FeatureStore: Feastmaterialize user features→onlinelookup trong Jupyter notebook Giảngviên (VinUni) AICB· Ngày 19 Tuần4 54 / 56

---

<!-- chiron-source-span: {"source_span_id":"649dd22b-8958-5136-9604-204f2cce46f1","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"Glossary: Vector&Feature Store Terminology","extraction_method":"pdf-text-layer"},"checksum":"c75907e8c9366d8683ef0d8e48b2852ea26cbc5648d151652116ea8298ea7510"} -->

## Slide 57 - Glossary: Vector&Feature Store Terminology

VectorStore

- Embedding: densevector biểu diễn nghĩa

- Chunk: đoạntext trước khi embed

- Index: cấutrúc ANN (HNSW,IVF,DiskANN)

- Recall@k:%relevant docs trong top-k

- Quantization: fp32 →int8/binary

- Hybridsearch: BM25+ Vector →RRF
merge

- Reranker: cross-encoderrerank top-N

- Re-index: rebuildkhi đổi embedding model

- Filtered-ANN:indexbiết filter,tránh sập
recall

- Lateinteraction: giữvector từng token,
chấmMaxSim

- Embeddinginversion: dựnglại text gốc từ
vector FeatureStore

- Entity: primarykey (user_id, item_id)

- Featureview: schema+ entity + source

- Online/ Offline store:KV <10ms/ full
history

- Materialize: batchload offline →online

- PITjoin: as-oftimestamp, no leakage

- Train-serveskew: featuremismatch bug

- PushAPI: streamevent →onlinestore

- Featureservice: bundledfeatures cho 1
model

- Registry: Feastmetadata catalog

- Embeddingfeature view: vectorlàm
feature

- Agentmemory: onlinestore + vector store
choagent

- Semanticcache: táidùng câu trả lời cho
querygần Giảngviên (VinUni) AICB· Ngày 19 Tuần4 55 / 56

---

<!-- chiron-source-span: {"source_span_id":"4ef1aafe-1e89-5131-9850-820a495fd5cf","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"239e937c6464a5d1723b7bc69a46ea0d69ea336a1601b89d5372cfa5e50de61c"} -->

## Slide 58 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 Hybrid Search (BM25 + Vector + RRF,k = 60) là mặc định production 2026 — nhưngtầng lưutrữ (RAM/SSD/objectstorage) mới là quyết địnhchi phí lớn nhất. 2 GraphRAG khi câu trả lời làrelationship(multi-hop, cross-document), không phải đoạn text. Kiếntrúc layered: vector→KG. 3 Feature Store thắng cùng lúc3 dimensions: feature reuse, train/serve consistency, low- latencyonline lookup — không toolnào khác giải quyết cả 3. Giảngviên (VinUni) AICB· Ngày 19 Tuần4 55 / 56

---

<!-- chiron-source-span: {"source_span_id":"db777331-344a-5a9f-b24a-abfa3da2bfa9","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"f1c8335f40a27ee8b3e9ca76a892550b93df152390b9197bca94abc87b667efd"} -->

## Slide 59 - Tiếptheo & Bài tập

Ngày 20: Model Serving & Infer- enceOptimization “Model accuracy 95% nhưng latency 3 giây — user đợi không nổi. Quiz + Milestone 1.”

- Hoànthành Lab 19: Vector&
FeatureStore

- Đọctrước: vLLM docs—
PagedAttentionpaper

- Ôntập Chương 4 cho Quiz N20
Giảngviên (VinUni) AICB· Ngày 19 Tuần4 56 / 56

---

<!-- chiron-source-span: {"source_span_id":"93459e31-bee4-510a-a0e2-69ff58c526b8","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"7e4d9520f936f2f56985a30256441ff9cb806afdcbae0a05f62213cd4ae5dfd3"} -->

## Slide 60 - Hỏi& Đáp

Câu hỏi về Vector DB, Hybrid Search, GraphRAG, hay Feature Store?

---

<!-- chiron-source-span: {"source_span_id":"03413cb4-6df6-5d99-9fa8-45ff13397fd0","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"a9961ba2b6516e38c637157a56d2f154fce00992d68f8710d3d7da84cf4d0f07"} -->

## Slide 61 - Cảmơn!

AICB-P2T2 · Ngày 19 Vector Store & Feature Store lms.vinuni.edu.vn · Slide & template trên LMS
