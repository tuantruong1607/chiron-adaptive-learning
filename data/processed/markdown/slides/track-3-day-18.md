---
schema_version: 1
course_id: rag-intensive
document_id: "bba55eab-7aad-56fc-9ccf-989f4d333875"
document_version_id: "30c719df-c96d-54e0-b841-baa88fd43609"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Production RAG"
source_file: "track 3 - day 18.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 18.pdf"
source_sha256: "8f74d016e7d16d9d26e938595fa8b885445f68f5da7129b55a9e91b9dfef64bb"
parser_version: chiron-structured-markdown-v1
page_count: 57
sparse_page_count: 1
extraction_methods: "{\"pdf-text-layer\":56,\"pdf-text-layer-sparse\":1}"
language: vi
---

# Production RAG

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"48199f7a-8abe-5477-b5da-77161d8c304c","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Production RAG","extraction_method":"pdf-text-layer"},"checksum":"2525cf7b5aaa48f0c942f0662dd6ecd8810e57eb1c52c5c6e955123927ca1e1c"} -->

## Slide 1 - Production RAG

AICB-P2T3 · Ngày 18 · Chương 4 — Agent Nâng Cao M.Sc Trần Minh Tú VinUniversity · Phase 2 · Track3 ·Tuần4

---

<!-- chiron-source-span: {"source_span_id":"d6de3323-4214-511c-82fe-d22c72dffbfd","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"b7572a51e351ff800ea2445a63f4b1b3f08413b00f47f6825c475066e75de5b2"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Tại sao RAG pipeline demo chạy tốt nhưng production accuracy chỉ đạt 60% — ingestion hay retrieval đang giết bạn?” Giữcâu hỏi này trong đầu khihọc bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"2c14c930-f325-55a9-93b6-2774d9433b30","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nộidung bài học","extraction_method":"pdf-text-layer"},"checksum":"99d03c66eb8af1ecb4731669340aae8d687858afb2ec925e58d5fd658af89552"} -->

## Slide 3 - Nộidung bài học

1. Tạisao Basic RAG thất bại?

2. FixOFFLINE — Ingestion Pipeline

3. EnrichmentPipeline

4. FixONLINE — PreRAG

5. FixONLINE — Retrieval & Augment

6. FixONLINE — Generate & PostRAG

7. Evaluation— Đo lường RAG Pipeline

8. AgenticRAG

9. RAGvẫn chưa giải quyết đượcmọi thứ

10. Demo& Thực hành M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 1 / 42

---

<!-- chiron-source-span: {"source_span_id":"25b61ad6-12ea-5719-930d-e133b31dacbc","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Tại sao Basic RAG thất bại?","extraction_method":"pdf-text-layer"},"checksum":"52dc65f596a940441177c3d32f9dc5c4a2a6434d5edcd9b40305028c3a2f3b2b"} -->

## Slide 4 - Tại sao Basic RAG thất bại?

01 Ingestion & Retrieval — failure nằm ở đâu trong pipeline?

---

<!-- chiron-source-span: {"source_span_id":"217f3dce-01c2-52fa-b078-b2241ce4307a","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"RAGPipeline — Tổng quan ONLINE &OFFLINE","extraction_method":"pdf-text-layer"},"checksum":"a06854977a73da21c8be116918f8b391fb183e08c96fcdd21792e4b075d0bdac"} -->

## Slide 5 - RAGPipeline — Tổng quan ONLINE &OFFLINE

Output Query/ Question RAG StorageLayer ONLINE OFFLINE Data Data Processing Data → Data Processing → Storage Layer. Chạy 1 lần (hoặc khi data thay đổi). “Garbage in, garbageout.” Query → RAG → Output. Chạy mỗi query. Production accuracy chỉ 55– 65%—tại sao? M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 2 / 42

---

<!-- chiron-source-span: {"source_span_id":"74d4e711-27de-5c58-8750-cd5ebede8302","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"OFFLINEPipeline — Failure ở đâu?","extraction_method":"pdf-text-layer"},"checksum":"8b0459aa0e83a636e84e969b3d4fb804deca288b1acbe83112ee2e2e4217bc33"} -->

## Slide 6 - OFFLINEPipeline — Failure ở đâu?

Data Data Processing StorageLayer

- Datasai

- Datacó chất
lượngthấp

- Chunking
Mismatch

- Embedding
Mismatch

- Metadatathiếu

- Parsingchưa tốt

- Frameworkquản
trịchưa tốt Lưuý: Trongthựctế: chỉcóingestionpipelinelàchưađủ. EnrichmentPipeline sẽ giúpchúngtalàmgiàuthêmthôngtin(contextualembeddings,metadataextraction, datacleaning). M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 3 / 42

---

<!-- chiron-source-span: {"source_span_id":"123fb9f0-1732-5a4d-81f1-794c6abfd200","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"ONLINEPipeline — Nguyên nhân output saiở từng bước","extraction_method":"pdf-text-layer"},"checksum":"8be6d1b9e4e9bfa2c9459cea1be869ab6f9860b98486961c44e96709879ac6e4"} -->

## Slide 7 - ONLINEPipeline — Nguyên nhân output saiở từng bước

StorageLayer Query/ Question PreRAG R A G PostRAG Output Bước Vaitrò Nguyênnhân output sai PreRAG Xửlý query Querymơ hồ · Không rewrite· Vocabularygap · Thiếuinput guardrails R Tìmchunks Chỉ1 method · BM25 misssynonyms · Dense miss keywords ·Thiếu metadata filter A Ghépcontext Quánhiều chunks · Lost inthe middle · Context overflow ·Thiếu reranking G LLMtrả lời Hallucinate· Prompt yếu · Temperaturecao· Model không phù hợp PostRAG Validateoutput Outputkhôngquakiểmduyệt·Thiếuevaluationpipeline·Khôngcómonitoring/feedback loop Lưuý: Mỗibước đều có thể khiếnoutput sai. Production RAGcần fixtoànbộ chuỗi,không chỉ 1 bước. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 4 / 42

---

<!-- chiron-source-span: {"source_span_id":"bcf47140-b7f4-55ca-809b-96fca09ae13e","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"ErrorTreeAnalysis — Log từngbước, tìm đúng chỗ sai","extraction_method":"pdf-text-layer"},"checksum":"199827f84916d5d65e1958fa1b80e81c5bce15eb348cbf40eca8a7dde3d56507"} -->

## Slide 8 - ErrorTreeAnalysis — Log từngbước, tìm đúng chỗ sai

Query PreRAG R·A·G PostRAG Output Log: raw query Log: rewritten query+ intent Log: chunks +scores Log: answer +eval scores Log: output +feedback Output đúng? OK Yes Context đúng? No FixG:prompt model/ temperature Yes Query rewriteOK? No FixR/A:chunking search/ reranking Yes FixPreRAG:query rewrite/ HyDE No FixIngestion: data quality/ parsing vẫn sai?

1. Log mọi bước (query, chunks, scores, answer, feedback)→ 2. Output sai? Đi ngược: PostRAG→ R·A·G → PreRAG →Data →3. Dừngở bước đầu tiên cóvấn đề→fixđúng chỗ. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 5 / 42

---

<!-- chiron-source-span: {"source_span_id":"6b63ede8-5364-5fc0-816e-60ce4aed64e1","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Bằngchứng: Gap giữaNaive và Production RAG","extraction_method":"pdf-text-layer"},"checksum":"dbf764cf899d59c9dddc8405d089ac1974afeb95989085b755838c904f3cd851"} -->

## Slide 9 - Bằngchứng: Gap giữaNaive và Production RAG

60% Naive RAG Accuracy 85%+ Production RAG Accuracy +25% Improvement khi optimize Metric NaiveRAG Production RAG Nguyên nhâncải thiện Faithfulness ∼0.70 ≥0.85 Betterprompt + reranking ContextRecall ∼0.55 ≥0.75 Hybridsearch + enrichment ContextPrecision ∼0.50 ≥0.75 Reranking+ metadata filter AnswerRelevancy ∼0.65 ≥0.80 Queryrewrite + augmentation M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 6 / 42

---

<!-- chiron-source-span: {"source_span_id":"c54ed283-83c0-547b-9954-25317180962a","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Fix OFFLINE — Ingestion","extraction_method":"pdf-text-layer"},"checksum":"d81d503b91b3fdc53b9d209b51035da8ac4fedf7994eb78a47cb8c393bf03077"} -->

## Slide 10 - Fix OFFLINE — Ingestion

02 Pipeline Data Processing: Chunking, Embedding & Enrichment

---

<!-- chiron-source-span: {"source_span_id":"e85b1a0d-2cca-5e1d-9865-124255c24785","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"IngestionPipeline — Mỗi bước fix 1failure từ Section 1","extraction_method":"pdf-text-layer"},"checksum":"2f135b83683bc8656c36b800e39464da15e33be72e5e06297fdccf3fe3309a47"} -->

## Slide 11 - IngestionPipeline — Mỗi bước fix 1failure từ Section 1

Document PDF/HTML/MD Parse extracttext Clean noiseremoval Chunk hierarchical Metadata date,source Enrich LLMcontext Fix: Parsing chưa tốt Fix: Data chất lượng thấp Fix: Chunking Mismatch Fix: Metadata thiếu Fix: Embedding Mismatch Embed text→vector Index VectorDB Slide1.2 liệt kê 5 OFFLINE failures.

### Pipelinenày fixtừngfailure một
Parse →Clean →Chunk →Metadata

- Enrich.
Bỏ bước nào = để lọt failure đó vào VectorDB. Lưu ý: “Garbage in, garbage out” — mỗi bước bỏ qua sẽtích lũy lỗi. Parse sai → chunk sai → embed sai

- retrievesai →outputsai.
M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 7 / 42

---

<!-- chiron-source-span: {"source_span_id":"31bddba5-93b6-5e86-954c-33e7b2d7cb7c","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"3Chunking Strategies — So sánh","extraction_method":"pdf-text-layer"},"checksum":"9bf2c3f6c488faec93575d60c35ac9e0318ec47150ae0105384c8a35e63958a6"} -->

## Slide 12 - 3Chunking Strategies — So sánh

Fixed-size Chunk1 Chunk2 Chunk3 cắt giữa câu! Semantic Chủđề A Chủđề B Chủđề C nhóm theo similarity Hierarchical Parentchunk (full context) Child1 Child2 Child3

```text
retrieve child, return parent
Hierarchical (parent-child) nên làde-
```
fault: chunks nhỏ cho retrieval preci- sion+ chunks lớn cho LLM context. Fixed: 512 tokens, overlap64 Semantic: cosine threshold 0.85 Hierarchical: parent 2048, child256 M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 8 / 42

---

<!-- chiron-source-span: {"source_span_id":"054cc3ad-a2b9-5aae-af71-5a0180ed9b55","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"AdvancedChunking — Structure-Aware& LateChunking","extraction_method":"pdf-text-layer"},"checksum":"659d4fa12fa8cd3407d32eb00c0c2832f9b161c987634465d1eb8e8c05f0bb64"} -->

## Slide 13 - AdvancedChunking — Structure-Aware& LateChunking

Parse markdown headers, HTML tags, PDF sections rồi chunk theo logicalstructure. Giữ nguyên tables, code blocks, lists —không cắt giữa chừng. Ưutiênkhicorpuscó structureddoc- uments(docs,API refs, manuals). Dùng long-context embedding model, chạy qua toàn bộ document

- thu được token-level embed-
dingscófull context. Pool token embeddings theo chunk boundaries → mỗi chunk embedding mangcontext của cả document. Khácnaive: embedtừngchunkriênglẻ →“orphan”, khôngbiết xung quanh nói gì. Yêu cầu: jina-embeddings-v2, nomic-embed. Trade-off: tốn memory + latency cao hơn khi indexing. Lưuý: Chunkingstrategycó impactlớnnhất lênRAGaccuracy. LuônA/Btestchunkingtrướckhioptimizeretrieval haygeneration. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 9 / 42

---

<!-- chiron-source-span: {"source_span_id":"4f0a4955-4a5c-5122-8836-0e0332337dc2","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"EmbeddingModel Selection — Chọn đúng modelcho use case","extraction_method":"pdf-text-layer"},"checksum":"d6d81df34a013523b1ce1751390674bd6ebff75ac4c89fddb60d8b58d730f116"} -->

## Slide 14 - EmbeddingModel Selection — Chọn đúng modelcho use case

Model Dims TiếngViệt Max Tokens Cost text-embedding-3-small 1536 OK 8191 $0.02/1M text-embedding-3-large 3072 Tốt 8191 $0.13/1M Cohereembed-v3 1024 Tốt 512 $0.10/1M bge-m3(open-source) 1024 Rấttốt 8192 Free multilingual-e5-large 1024 Rấttốt 512 Free Tiếng Việt → bge-m3 hoặc multilingual-e5-large Budgetcó →text-embedding-3-large Production → Cohere embed-v3 (built-intypes) Lưu ý: Đổi embedding model =re- index toàn bộ. Chọn kỹ từ đầu! Benchmark trên MTEB multilingual leaderboard. Note: Cohere Embed v4 đã hỗ trợ 128K tokens — cânnhắc nếu cần long-context. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 10 / 42

---

<!-- chiron-source-span: {"source_span_id":"9197e4b4-8593-5b39-8211-bab7d497582e","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"ContextualEmbeddings — Anthropic’sContextual Retrieval","extraction_method":"pdf-text-layer"},"checksum":"ba76436cfc5e5e830e85e4ad95fbd83422ac7a618c919f8fa23d83efcd396c63"} -->

## Slide 15 - ContextualEmbeddings — Anthropic’sContextual Retrieval

Chunkgốc “Nhânviên được nghỉ 12 ngày/năm.” LLMprepend context ClaudeHaiku / GPT-4o-mini Contextualchunk “TríchChương 3 — Chính sáchnghỉ phép Sổtay VinUni2024. NV được nghỉ 12 ngày/năm.” Embed →Index Ýtưởng(Anthropic,Sep2024) — Trước khi embed mỗi chunk, dùng LLM prepend 1 đoạn context ngắn giải thích chunk nằm ở đâu trong document. Retrievalfailure giảm49%(alone) Giảm 67% khi kết hợp Contextual BM25+ Reranking Lưuý: Trade-off: +1LLMcall/chunkkhiindexing (one-time). Dùng model rẻ(Haiku, GPT-4o-mini). M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 11/ 42

---

<!-- chiron-source-span: {"source_span_id":"5a985054-d7b9-5564-a1bf-dfc1b9a71e15","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"MultimodalEmbeddings — Shared Latent Space","extraction_method":"pdf-text-layer"},"checksum":"2d155d7b02e9b7e6b4fa9119db96e46bd00db862c0c946d48f46a67f5870ea3e"} -->

## Slide 16 - MultimodalEmbeddings — Shared Latent Space

Multimodal Embedding là gì? — Chuyển data từ nhiều modalities (text,image,audio)thành densevec- torstrongcùng 1 latent space. Vídụ: ảnhconchóvàtext“ahappygoldenretriever”

- 2vectors gầnnhau trongshared space.
Cho phép: text query→retrieve cả text chunks lẫn images. Model Modalities Note CLIP/ SigLIP Text+Image Contrastivelearning JinaCLIP v2 Text+Image Multilingual ColPali/ColQwen2 Fullpage Doc-native VoyageMM 3 Text+Image API-based

1. Describe then Embed: Image→VLM mô tả→ embedtext. + Dùng existing text pipeline.– Mất spatial/visual nuance.

2. Native Multimodal: Image+Text→ shared vec- torspace (CLIP-style). +Giữvisualinfo,cross-modalretrieval. –Alignment chưaperfect.

3. Document-as-Image(ColPali): Render page→ embedtoàn bộ page image. Bypass OCR. + Giữ layout/tables/figures. – Tốn storage, cần GPU. Lưu ý: Chỉ cần khi corpus có>20% visual con- tent. Text-to-imageretrievalaccuracythấphơntext- to-text15–20%. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 12 / 42

---

<!-- chiron-source-span: {"source_span_id":"1dc1c6e6-da80-59a7-aad3-23da818be1fc","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Enrichment Pipeline","extraction_method":"pdf-text-layer"},"checksum":"c5dbeac625a5b25d514b615ab750cd855b4b909f1f97603469fb673449703908"} -->

## Slide 17 - Enrichment Pipeline

03 Làm giàu chunks trước khi embed — Summarize, HyQA, Meta- data

---

<!-- chiron-source-span: {"source_span_id":"e895bfd5-0fb5-558b-96c4-1a87edd41c54","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"EnrichmentPipeline — Tại sao cần “làmgiàu” chunks?","extraction_method":"pdf-text-layer"},"checksum":"f795e44b2a795838b452a8c4b9f9bc79993404fd070b66a1c6e0ff819248c931"} -->

## Slide 18 - EnrichmentPipeline — Tại sao cần “làmgiàu” chunks?

Raw Chunk Summarize HypothesisQ&A Contextual Prepend AutoMetadata Enriched Chunk Song song — LLM-powered, one-time, offline Raw chunks thiếu context→ embed- dingchỉ capture surface meaning. Enrichment = thêm thông tintrước khi embedđể vector representations phongphú hơn. 4 techniquesđộc lập→chạy parallel trênmỗi chunk. Output merge: enriched_text + sum- mary+questions+metadata →1en- richedchunk. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 13 / 42

---

<!-- chiron-source-span: {"source_span_id":"a7426482-5aea-5c97-9b01-724d1e1d453d","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"EnrichmentTechniques— 4 kỹthuật chính","extraction_method":"pdf-text-layer"},"checksum":"43cc6e3cf6697a106a2c4851a01b1818ca86073452327a61d3cc158ede5cab1a"} -->

## Slide 19 - EnrichmentTechniques— 4 kỹthuật chính

LLMtạo summaryngắn chomỗi chunk. Embedsummarythayvì(hoặccùngvới)rawchunk. Ưuđiểm: giảm noise,focus vào key info. Dùngkhi: chunks dài,nhiều filler text. LLMgenerate câuhỏi mà chunk có thể trảlời. Index cả questions lẫn chunk→ query match tốt hơn. Ưu điểm: bridge vocabulary gap (giống HyDE nhưngoffline). Dùng khi: user queries khác ngôn ngữ với docu- ments. Prepend context giải thích chunk nằm ở đâu trong document. Đãcover ở slide Contextual Embeddings. Giảm49% retrieval failure (alone). LLM extract: topic, entities, date_range, sentiment. Gắnvào chunk metadata→enablerich filtering. Dùngkhi: corpus lớn,cần multi-faceted search. Lưu ý: Enrichment =one-time costkhi indexing. Dùng model rẻ (GPT-4o-mini, Haiku). ROI cao vì cảithiện mọiquery sauđó. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 14 / 42

---

<!-- chiron-source-span: {"source_span_id":"537eda7f-1319-549b-bba0-1605e2bc3aa6","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Fix ONLINE — PreRAG","extraction_method":"pdf-text-layer"},"checksum":"12b5fe3fb1457fc6992d6c4ca2842ac4952ebae33c2a3f995bf4f08878a5ce33"} -->

## Slide 20 - Fix ONLINE — PreRAG

04 Query Transform, Corrective RAG — fix trước khi search

---

<!-- chiron-source-span: {"source_span_id":"84402109-609c-539b-9af8-bba5c5f70b41","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"QueryTransform— HyDE & Multi-Query","extraction_method":"pdf-text-layer"},"checksum":"74a485573da37f31baff0556851fb20000c679621b6c89181d02145186f65fed"} -->

## Slide 21 - QueryTransform— HyDE & Multi-Query

HyDE Query HypotheticalAnswer Embed& Search LLMgen Multi-Query ComplexQuery Sub-Q1 Sub-Q2 Sub-Q3 MergeResults HyDE — Generate hypothetical answer, embed answer thayvì query. Bridges vocabulary gap. Multi-Query — Decompose query thành sub- queries, retrieve mỗi cái, merge. Recall tăng cho multi-hop. Lưu ý: HyDE tốn thêm 1 LLM call/query. Chỉ dùngkhi vocabulary mismatch nghiêm trọng. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 15 / 42

---

<!-- chiron-source-span: {"source_span_id":"bca777c1-6d7b-58e8-97b6-e2a10815b047","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"CorrectiveRAG & Adaptive Retrieval","extraction_method":"pdf-text-layer"},"checksum":"8b72f0c6b2a0d80ed8de6b5ef8b97f7cb3e598fc61565c9edecce2dba6494ee1"} -->

## Slide 22 - CorrectiveRAG & Adaptive Retrieval

Query Retrieve EvaluateQuality Generate WebSearch orRewrite good low

### Nếuretrieval quality thấp

1. Triggerwebsearch (fallback)

2. Hoặcqueryrewrite rồiretry

3. Rồi mới generate Tránhgenerate trên bad context

### Routequeries theo complexity
Simple →directLLM (no RAG) Medium →standardRAG Complex →fullpipeline + rerank Giảmlatency 40%trungbình M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 16 / 42

---

<!-- chiron-source-span: {"source_span_id":"12377e1c-cd5f-5da5-9827-cbffb05f77c5","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Fix ONLINE — Retrieval & Aug","extraction_method":"pdf-text-layer"},"checksum":"d44ab92ebdb6dfaef2577e38d8f51c17105320b5902bbf005765ab8e97b1043c"} -->

## Slide 23 - Fix ONLINE — Retrieval & Aug

05 Fix ONLINE — Retrieval & Aug- ment Hybrid Search, Metadata Filtering & Reranking — fix R và A

---

<!-- chiron-source-span: {"source_span_id":"e8093c14-05a8-55f5-939e-80ea84d8026f","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"HybridSearch — BM25 + Dense VectorFusion","extraction_method":"pdf-text-layer"},"checksum":"2e365c7644d1d81ec639e5765bc6b652fd3b679d90db451f78aa9022a20aaa1e"} -->

## Slide 24 - HybridSearch — BM25 + Dense VectorFusion

UserQuery BM25 exactkeywords RankA DenseVector semanticmatch RankBRRFFusion Top-KResults Không cần GPU Cần embedding model Merge rankings đơn giản: score(d) = ∑ 1 k+ranki(d). Không cần training, production standard. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 17 / 42

---

<!-- chiron-source-span: {"source_span_id":"5412ce88-861d-5ee7-96a3-665401e09423","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"BM25vs Dense — Khi nào dùngcái nào?","extraction_method":"pdf-text-layer"},"checksum":"8366977893fb1ee0ad7068100c491638fb58cc14d31ab8e25d164586046060a7"} -->

## Slide 25 - BM25vs Dense — Khi nào dùngcái nào?

Tiêuchí BM25 DenseVector Hybrid Exactkeywords Tốt Yếu Tốt Synonyms/ paraphrase Yếu Tốt Tốt Multilingual Yếu Tốt Tốt GPUrequired Không Có Có Latency <5ms ∼20ms ∼25ms Lưu ý:BM25 cho tiếng Việt: cầnword segmentation(underthesea, VnCoreNLP) trướckhi index. Thiếubước này→BM25gần vôdụng chotiếng Việt. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 18 / 42

---

<!-- chiron-source-span: {"source_span_id":"b7749e74-ce6a-5fbf-9d4a-3503b03d8046","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"BeyondRRF — TensorFusion,Late Interaction & Learned Sparse","extraction_method":"pdf-text-layer"},"checksum":"10978b9babab4a12d1b13d529ee1a2296c0a52a8f4788ef39e60a3bb1244885a"} -->

## Slide 26 - BeyondRRF — TensorFusion,Late Interaction & Learned Sparse

Tensor Fusion là gì? — Thay vì concatenate vectors (ghép nối), tensor fusion tính outer product giữa feature vectors từ các modali- ties/signalskhác nhau. Tạo ra tensor đa chiều mapmọi tương tácgiữa features của BM25 signal và Dense signal→ cap- turecross-signal interactions mà RRF bỏ lỡ. Query tokens↔ doc tokens→ MaxSim per query token. Token-levelmatchingchính xác hơn single-vector. Pre-computedoc embeddings →vẫnfast retrieval. Cóthể thaythế cảbi-encoder + cross-encoder. Method Precision Latency How RRF Baseline ∼1ms Rankmerge WeightedScore +2–3% ∼1ms Scoremerge SPLADE +5–8% ∼15ms Learnedsparse ColBERT +8–12% ∼50ms Lateinteract TensorFusion +10–15% ∼80ms Outerproduct ThayBM25 bằnglearnedsparse vectors. Kếthợp: exact match+ learned term expansion. Dùnginverted index →fastnhư BM25. Lưu ý: Tensor fusion cần labeled data (query-doc pairs)đểtrainouterproductlayer. Khôngcó →RRF +cross-encoder làđủ tốt. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 19 / 42

---

<!-- chiron-source-span: {"source_span_id":"14900f34-494f-5fcf-99d6-d119a2617fa8","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"MetadataFiltering — Pre-filter trước khi search","extraction_method":"pdf-text-layer"},"checksum":"6a5f0f47cc1e9650fc867fe38dc91ce8e85675638fabab31b0bbc8ab62e018e9"} -->

## Slide 27 - MetadataFiltering — Pre-filter trước khi search

Gắn metadata vào mỗi chunk khi in- dexing. Filtertrướckhivectorsearch →giảm searchspace, tăng precision.

### Metadataphổ biến

- source: tên file/URL gốc

- date: ngày tạo/cập nhật

- category: policy,FAQ,manual…

- language: ngôn ngữ

- section: chapter/heading
# Qdrant metadata filtering client.search( collection_name= "docs", query_vector=embedding, query_filter=Filter( must=[FieldCondition( key= "year", match=MatchValue(value=2024) )] ), limit=20 ) Lưu ý: Metadata filtering phụ thuộc vector DB. Qdrant,Weaviate,Pineconehỗtrợtốt. Chromahạn chếhơn. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 20 / 42

---

<!-- chiron-source-span: {"source_span_id":"c6a578af-8052-54f9-bc7b-9abfb8c14941","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"VectorDB cho Production RAG","extraction_method":"pdf-text-layer"},"checksum":"539c56bec8e4ee9e50af2fbc4ceac16cbf7ecb8a9d3e81e618c8ec4fb0877d80"} -->

## Slide 28 - VectorDB cho Production RAG

DB HybridSearch Metadata Filter Khi nào? Qdrant Built-in Rich Defaultpick Weaviate Built-in Rich GraphQLfans Pinecone Sparse+ Good Managed/SaaS Milvus Built-in Rich Large-scale,GPU Neo4j Vector+Graph Cypher GraphRAG pgvector Manual SQL AlreadyPostgres Chroma — Basic Prototype FAISS — — Researchonly Production: QdranthoặcMilvus(open-source,hybrid+metadata). Pinecone(man- aged, zero-ops). GraphRAG: Neo4j (vector + graph traversal).Lab: Qdrant local (Docker). M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 21 / 42

---

<!-- chiron-source-span: {"source_span_id":"ed03b5a7-d0d3-53fa-88eb-27b67c54eed8","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Reranking— Highest ROI Optimization","extraction_method":"pdf-text-layer"},"checksum":"2fd74949c6c5961c176ab4105ba01c597a96cec8ca78b44a6291502be648dc4a"} -->

## Slide 29 - Reranking— Highest ROI Optimization

Retrievetop-20 Cross-Encoder rerank Passtop-3 →LLM ∼1ms ∼50ms +15–25% precision Bi: encoderiêng,fast( ∼1ms),nointeraction Cross: encode cùng, chậm (∼50ms), accu- ratehơn nhiều

### RerankingModels — So sánh
Model Cost Note CohereRerank v3.5 API Productiondefault bge-reranker-v2-m3 Free Multilingual,tiếng Việttốt ms-marco-MiniLM-L-12 Free Nhẹ,nhanh, English JinaReranker v2 API Multilingual,8K context Flashrank Free Ultra-light, <5ms LLM-as-Reranker $$$ GPT-4o/Claudererank Retrieve top-20 → Rerank → Keep top-3

- LLMgenerate
Lưu ý: 30–50ms overhead đổi lấy +15–25% precision. Highest ROI trong RAG pipeline. Tiếng Việt → bge- reranker-v2-m3. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 22 / 42

---

<!-- chiron-source-span: {"source_span_id":"3ed9018b-6ce0-594d-9575-2134355be8f0","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Augmentation— Nâng cao context trước khiđưa vào LLM","extraction_method":"pdf-text-layer"},"checksum":"df05fa23a02f15347041942bed4977e46dde1a1751155e7a4ca1f22586a6cc35"} -->

## Slide 30 - Augmentation— Nâng cao context trước khiđưa vào LLM

NLImodelkiểmtra entailmentgiữaqueryvàchunk. Filterchunks contradict →giảmhallucination. Tools: cross-encoder/nli-deberta-v3-base. Gắnsourcereference vàocontext. Prompt: “Cite sources using[1], [2]...” Output: answer + citations+ source links. Mergechunks từnhiềusources (DB,web, API). Resolveconflicts: newest winshoặc LLM arbitrate. Ref: MASS-RAG (multi-agent synthesis). Chunksquá dài →compresstrướckhi LLM. Extractive: giữ relevant sentences. Abstractive: LLM summarize context. Tools: LongLLMLingua, ContextualCompression. Lưuý: Augmentation=bướcgiữaRetrievalvàGeneration. Thườngbịskipnhưngimpactlớnlênanswerquality+ giảmtoken cost. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 23 / 42

---

<!-- chiron-source-span: {"source_span_id":"4761945e-0f83-5664-8a80-89ae54785913","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Fix ONLINE — Generate & Pos","extraction_method":"pdf-text-layer"},"checksum":"cf2782e26d16bad8708935c73fb8846047efdc621a7c9d1f0aff4d3501684ced"} -->

## Slide 31 - Fix ONLINE — Generate & Pos

06 Fix ONLINE — Generate & Pos- tRAG Self-RAG, RAG-Fusion, Semantic Cache — fix G và validate out- put

---

<!-- chiron-source-span: {"source_span_id":"8401e319-a2e6-56e7-ada0-a5a6ac43a811","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Self-RAG,RAG-Fusion & Semantic Caching","extraction_method":"pdf-text-layer"},"checksum":"0d922b4f03d3bc90f6358a21c615f1ffd289a0dbfd5a564ec5628347c529d8e9"} -->

## Slide 32 - Self-RAG,RAG-Fusion & Semantic Caching

Self-RAG — LLMtựquyết khinàoretrieve. Fine- tune model output special tokens ( [Retrieve], [IsRel], [IsSup]). Không hoạt động out-of-the- box.

1. Generatemultiplequery variants

2. Retrieve cho mỗivariant→3. RRF merge Semantic Cache— Cache theo semantic similar- ity. Query mới similar>0.95 → trả cache. Giảm 30–50%LLMcalls. Pattern Cost Khi nào? HyDE $$ Vocabmismatch Multi-query $$ Multi-hopQ CRAG $$ Unreliableretrieval Self-RAG $$$ Fine-tunedmodel RAG-Fusion $$$ Maxrecall Sem.Cache $ Repeatedqueries Lưu ý: Đừng dùng tất cả cùng lúc! Chọn pattern theofailuremode cụ thểcủapipeline. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 24 / 42

---

<!-- chiron-source-span: {"source_span_id":"beb16b53-048d-5757-9252-f941a2f305c6","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Evaluation — Đo lường RAG","extraction_method":"pdf-text-layer"},"checksum":"cfe560f908265b91ebfaabc71251143cb2931fa0c3bde67c36b20ce3ad42d05b"} -->

## Slide 33 - Evaluation — Đo lường RAG

07 Pipeline Measure first, optimize second — RAGAS, TruLens & DeepEval

---

<!-- chiron-source-span: {"source_span_id":"75f5d2da-6f18-5e49-9f34-40adede15393","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"RAGAS— 4 metrics đánh giá RAGquality","extraction_method":"pdf-text-layer"},"checksum":"749587557d994f0363ec1bb94d9dc7c9f0970e14786fccc5264ba0a8d5c7acb7"} -->

## Slide 34 - RAGAS— 4 metrics đánh giá RAGquality

Faithfulness Answerclaims được contextsupport không? Target: ≥0.85 AnswerRelevancy Q&Acosine similarity Target: ≥0.80 ContextPrecision Chunksretrieved có relevantkhông? Target: ≥0.75 ContextRecall Đãretrieve đủ infocần thiết chưa? Target: ≥0.75 Generation quality Generation quality Retrieval quality Retrieval quality Lưu ý:RAGAS phụ thuộc judge model — scoresbrittle khi đổi judge. Luôn report judgemodel version cùng với scores. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 25 / 42

---

<!-- chiron-source-span: {"source_span_id":"29a86f69-881f-5cbe-a791-a2bd708cc9b1","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"RAGASDiagnostic — Score thấp thì fixở đâu?","extraction_method":"pdf-text-layer"},"checksum":"3bd3c77e21b3e867be0e964eb7759d04799d1b899be8b9410d1b5fc03c0697db"} -->

## Slide 35 - RAGASDiagnostic — Score thấp thì fixở đâu?

Contextchứa info đúng nhưng LLM bịathêm

- Tightenprompt (“Only use provided context”)

- Giảmtemperature, model ít hallucinate hơn
Contextkhông chứa info cần thiết

- Thựcra là Context Recall problem↓
Chunksđúng tồn tại nhưng không đượcretrieve

- Đổichunking (hierarchical)

- ThêmBM25 (hybrid search)

- ThửHyDE hoặc Multi-Query
Chunksđúng KHÔNG tồn tại trong DB

- Reviewchunking pipeline (cắt mất info)

- Documentchưa được ingest
Retrievequá nhiều irrelevant chunks

- Thêmreranking (cross-encoder)

- Giảmtop-K, tăng similarity threshold

- Metadatafiltering
LLMtrả lời đúng nhưng không matchcâu hỏi

- Improveprompt template

- Kiểmtra context window overflow
Lưuý: Luônfailureanalysis (bottom-10questions) trước khi nhìn aggregate scores. Aggregate che giấufailure patterns. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 26 / 42

---

<!-- chiron-source-span: {"source_span_id":"34284a0e-d0dc-5206-add7-d0befa338fc5","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"RAGASEvaluation — Code Pattern","extraction_method":"pdf-text-layer"},"checksum":"4370a740eca01c9f61885ad91de60a84ecc9a807dd4fc311aabeadd15c9cfb4b"} -->

## Slide 36 - RAGASEvaluation — Code Pattern

```text
from ragas import evaluate
from ragas.metrics import (
```
faithfulness, answer_relevancy, context_precision, context_recall, )

```text
dataset = {
```
"question": questions, "answer": answers, "contexts": retrieved_chunks, "ground_truth": ground_truths, } result = evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision, context_recall]) print(result) # DataFrame

### Workflowchuẩn

1. ChạyRAGAS baselinetrước

2. Xembottom-5(failureanalysis)

3. Optimizetheo failure mode cụ thể

4. Re-runRAGAS, so sánh Faithfulness ≥0.85,AnswerRele- vancy ≥0.80 ContextRecall ≥0.75 Luônfailure analysis trước aggregate M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 27 / 42

---

<!-- chiron-source-span: {"source_span_id":"4ac114d5-aa9d-57f4-b0c8-02852a8ff88e","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"EvaluationFrameworks — RAGAS vs TruLensvs DeepEval","extraction_method":"pdf-text-layer"},"checksum":"2d3a548958a811987858001e03862c4b55f7394ab55fd99b89863151b22976e0"} -->

## Slide 37 - EvaluationFrameworks — RAGAS vs TruLensvs DeepEval

Dimension RAGAS TruLens DeepEval Focus RAGpipeline eval Eval+ Tracing(OTel) RAG+ Agents + Chatbot Metrics 4core metrics RAGTriad 50+metrics Custom Hạnchế Feedbackfunctions G-Eval,DAG, BaseMetric Tracing Minimal OpenTelemetryspans @observedecorator CI/CD Manualsetup Moderate NativePytest Groundtruth Khôngcần Khôngcần Cảhai Setup ⋆Dễnhất ⋆⋆Trungbình ⋆⋆Trungbình GitHub ∼13kstars ∼3kstars ∼15kstars Usedby AWS,Databricks Snowflake,Equinix OpenAI,Google, Microsoft Cả 3 đều open-source, LLM-as-a-Judge, reference-free. Cost = LLM API calls cho judgemodel. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 28 / 42

---

<!-- chiron-source-span: {"source_span_id":"22d54082-788a-5f6a-95d3-c6d9ed1ff499","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"ChọnEvaluation Framework nào?","extraction_method":"pdf-text-layer"},"checksum":"33eeaa01b5a0efcae897dfb50ff584c1876201e3a28bdb6e7f3be58216fee6c9"} -->

## Slide 38 - ChọnEvaluation Framework nào?

### Khinào

- FocusRAG quality

- Setupnhanh 5 phút

- Teamnhỏ,MVP

### Khôngphù hợp
×Multi-agent,chatbot ×CI/CDphức tạp

### Khinào

- Cầntracing + eval

- Debugchính xác step fail

- Agenticmulti-hop

### Khôngphù hợp
×Quickprototype ×Teamkhông cần tracing

### Khinào

- AIstack phức tạp

- CI/CDgate (Pytest)

- Safety,MCP metrics

### Khôngphù hợp
×Chỉeval RAG đơn giản Prototype: RAGAS (nhanh, đủ dùng)→ Debug: +TruLens (tracing tìm bottleneck)

- CI/CD: +DeepEval (regression gate). Các frameworkkhông loại trừ nhau—
nhiềuteam dùng kết hợp. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 29 / 42

---

<!-- chiron-source-span: {"source_span_id":"fc97b51a-fde8-50da-8e4e-3023a0dbcec2","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"CostEstimation — 1M documents, bao nhiêutiền?","extraction_method":"pdf-text-layer"},"checksum":"a75af9df7daed392583ef066bc5f83d5c63ffd5a90d27c119e366d5dbf8fbbc4"} -->

## Slide 39 - CostEstimation — 1M documents, bao nhiêutiền?

Embedding 1M chunks × $0.02/1M tokens ≈$10–50 Contextual embeddings: +$50–200 (GPT-4o-mini) Vector DB storage: ∼$20–50/month (QdrantCloud)

### Embedding: ∼$0.00002 · Reranking
∼$0.001 LLMgeneration: ∼$0.01–0.05 Total: ∼$0.01–0.06/query NaiveRAG: ∼$1,500/month Production RAG: ∼$2,200/month (+47%) Accuracy85%vs60% →ítescalation ROIdương sau 2–3 tháng DùngGPT-4o: chiphí ×10–15. Lưu ý: Semantic caching giảm 30– 50%LLMcalls →tiếtkiệmđángkểkhi nhiềuuser hỏi tương tự. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 30 / 42

---

<!-- chiron-source-span: {"source_span_id":"a4efea04-1182-5064-aa55-d0619dc6c8f7","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Agentic RAG","extraction_method":"pdf-text-layer"},"checksum":"6a7ed96a02f81e2802ed076417bc258d039d30407825b233431c58fe1e9b8b94"} -->

## Slide 40 - Agentic RAG

08 Khi agent điều khiển RAG pipeline — từ static sang autonomous

---

<!-- chiron-source-span: {"source_span_id":"c9b2714f-a6b2-547b-b731-ded393b57fd1","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"RAGEvolution — Từ Naive đến Agentic","extraction_method":"pdf-text-layer"},"checksum":"6716d6b39e7a9e7976e02d779c88fd0582082957ef22ff3b02a2b62aa8f05247"} -->

## Slide 41 - RAGEvolution — Từ Naive đến Agentic

NaiveRAG staticpipeline AdvancedRAG hybrid+ rerank ModularRAG composable AgenticRAG autonomous Hôm nay: đây Next level Agentic RAG là gì? — Agent tự quyết định khi nào retrieve, query nào,bao nhiêu lần, dùng tool nào. 4 agentic patterns:Reflection, Plan- ning,Tool Use,Multi-Agent Collab- oration. Ref: Ehteshametal.,“AgenticRetrieval-Augmented Generation”(2025, arxiv 2501.09136)

### Staticpipeline không đủ khi

- Querycần multi-hopreasoning

- Retrieval lần 1 không đủ→ cần it-
erative

- Cầnkếthợp nhiềusources (DB+
web+ API)

- Cần self-correction khi context
kém M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 31 / 42

---

<!-- chiron-source-span: {"source_span_id":"f545eb99-7559-5e31-91e6-f1a607c7ee8e","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"AgenticRAG — 3 Kiến trúc chính","extraction_method":"pdf-text-layer"},"checksum":"2a753579f7f6edcae57a83d85a03e46385013d8c0b206a56c81baea9fae4804b"} -->

## Slide 42 - AgenticRAG — 3 Kiến trúc chính

Single-Agent Multi-Agent Hierarchical Môtả 1 agent điều phối toàn bộ retrieval+ routing Nhiều agent chuyên biệt, mỗiagent 1 data source Agent cấp cao delegate xuốngagent cấp thấp Ưuđiểm Đơngiản, latency thấp Scalable, parallel pro- cessing Strategic oversight, reli- able Nhược Không scale cho multi- domain Coordinationoverhead Latencycao, phức tạp Khinào SimpleQA, routing Multi-domainsynthesis High-stakes (medical, le- gal) Multi-agentsynthesis: agentschuyênbiệtcho sum- marization, extraction, reasoning → synthesis stagetổng hợp. Outperform strong RAG baselines trên 4 bench- marks. Dùng self-knowledge của model để filter retrieved docs. RL-basedtraining →modelbiết“mìnhbiếtgì,không biếtgì”. Giảminput documents + tăng generation quality. Lưu ý: Khác với Skill-RAG (Wei 2026) ở Section 9 — paper khác, cùngtên. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 32 / 42

---

<!-- chiron-source-span: {"source_span_id":"ceb0f6fb-3c2b-5a23-b2a7-34332bb3752b","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"AgenticRAG — Corrective & Adaptive (đãhọc) + mới","extraction_method":"pdf-text-layer"},"checksum":"c59404eaeaf7ec2a685d765a234faa1d873e08e331737bdab8cfd5605b253b16"} -->

## Slide 43 - AgenticRAG — Corrective & Adaptive (đãhọc) + mới

- CRAG=Corrective RAG (slide PreRAG)

- AdaptiveRetrieval =route by complexity

- Self-RAG=LLM tự quyết retrieve

- RAG-Fusion=multi-query + RRF
Đâychính làbuildingblocks củaAgentic RAG! Production RAG + Agent orchestration = Agentic RAG.

1. Reflection: Agent tự đánh giá output, retry nếu kém

2. Planning: Decomposecomplexquerythànhsub- tasks

3. ToolUse: GọiSQL,websearch,APIdynamically

4. Multi-Agent: Agents chuyên biệtcollaborate Workflow patterns: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator- Optimizer. Lưu ý: Agentic RAG không phải lúc nào cũng cần. Simple queries → Production RAG đủ. Chỉ dùngkhi multi-hop, multi-source, iterative. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 33 / 42

---

<!-- chiron-source-span: {"source_span_id":"f6695c96-a41f-5525-96b7-fc38b5cddac0","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"RAG vẫn chưa giải quyết được","extraction_method":"pdf-text-layer"},"checksum":"73e7cedd7c82145ca8a471df403b3d16e2b1977574c8d71867480a9f08cfa966"} -->

## Slide 44 - RAG vẫn chưa giải quyết được

09 mọi thứ Hidden State of Embeddings — khi vector similarity không đủ

---

<!-- chiron-source-span: {"source_span_id":"5821bf18-508a-5c21-b7e4-0cd245626f61","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Tạisao RAG không thể đạt 100%accuracy?","extraction_method":"pdf-text-layer"},"checksum":"bb8cc9afae6360881c7935df6cf5d1c3381b9b58f962835da5319f762e07233a"} -->

## Slide 45 - Tạisao RAG không thể đạt 100%accuracy?

Nhiềuretrievalfailures khôngphải vìthiếuevidence trongcorpus. Nguyên nhân thực:alignment gapgiữa query và evidencespace. Queryformulationkhôngmatchcáchevidenceđược biểudiễntrongvectorspace →cosinesimilaritycao nhưngsemanticmismatch. “Query-evidence misalignment is a typed rather than monolithic phenomenon” — có nhiều loại mis- alignmentkhác nhau. Skill-RAG dùnghidden-state prober(lightweight) đểdetect failure statetrướckhi generate. Khi detect failure → Skill Router chọn 1 trong 4

### skills

1. QueryRewriting

2. QuestionDecomposition

3. EvidenceFocusing

4. Exit(truly irreducible) Mỗi skill chiếmvùng riêng biệttrong failure state space →cóthể phân loại và xử lýtargeted. Lưu ý:Implication: Không phải cứ thêm data hoặc đổi embedding model là fix được. Cầndiagnose loại failure trướcrồi mới chọn đúng skill/technique. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 34 / 42

---

<!-- chiron-source-span: {"source_span_id":"e7037aa9-24f9-57a6-a0c7-eb42d14349b0","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"FundamentalLimitations — Embedding không capture hết","extraction_method":"pdf-text-layer"},"checksum":"8c6ed1e7ae241815e514f4b2fb96c6a18ee3ee2fee19245d8cf86e9f17be1bd0"} -->

## Slide 46 - FundamentalLimitations — Embedding không capture hết

1. Temporalblindness: Vectorkhôngcóchiềuthời gian →doc2022 và 2024 cùng score.

2. Entity-swap: “capital of France” vs “capital of Germany” →embeddingsgần nhau!

3. Negation insensitivity: “Approved” vs “Not ap- proved” →cosinesimilarity cao.

4. Stale embeddings: Model version drift→ vec- torsincompatible. Embedding-based hallucination detection cócerti- fiedlimits (arxiv2512.15068). NLI+ similaritykhôngđủ chosafety-critical.

- Metadatafiltering (temporal, source)

- NLIverification (post-retrieval)

- Failure-awarerouting (Skill-RAG)

- GraphRAGcho relational queries

- Human-in-the-loopcho high-stakes
RAGlà powerfulnhưngkhôngperfect. Hiểulimitations →designđúng: khinàoRAGđủ,khinàocầnGraphRAG, khinào cần human review. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 35 / 42

---

<!-- chiron-source-span: {"source_span_id":"3d96e556-a600-5177-921c-777d0a83f2c3","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Demo & Thực hành","extraction_method":"pdf-text-layer"},"checksum":"a7f59ad9fce8e7c39d1a9795b19a9ad9849aea356be13863a7bd35754478fd8e"} -->

## Slide 47 - Demo & Thực hành

10 Cá nhân implement modules — Nhóm ghép thành Production RAG System

---

<!-- chiron-source-span: {"source_span_id":"3e83e8da-f538-5134-87d2-69843e2b6966","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"Thựchành — Bức tranh lớn","extraction_method":"pdf-text-layer"},"checksum":"98e1b82498e809f679f447922a04103f705ef558b3efbfc747774cde18904a11"} -->

## Slide 48 - Thựchành — Bức tranh lớn

### Cánhân
Module1 Chunking Module2 Search Module3 Rerank Module4 Eval Module5 Enrichment Nhóm: ProductionRAG System = M1 +M2 + M3 + M4 +M5 + Deploy Mỗi người implement1 modulehoàn chỉnh. Cóscaffoldcode + TODOmarkers. Chạytest riêng cho từng module. Mụcđích: hiểu sâu1 phần, không bị overwhelm. Ghépmodules thànhfullpipeline. ChạyRAGASend-to-end,sosánhvới basicbaseline. Failureanalysis+presentation5phút. Mụcđích: thấy bứctranh lớn, teamwork. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 36 / 42

---

<!-- chiron-source-span: {"source_span_id":"dc94741c-a602-5430-b07d-36b595ed02a0","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"LiveDemo — Naive vs Production RAG","extraction_method":"pdf-text-layer"},"checksum":"e9e2963ad5184ef2946e43798cbc319805f4895560bdedce8f629888defd579a"} -->

## Slide 49 - LiveDemo — Naive vs Production RAG

1. PipelineA (basic): paragraph chunking +dense-only→chạyRAGAS

2. PipelineB (production): hierarchical chunks +hybrid search + Cohere Rerank

- chạyRAGAS

3. PipelineC (bonus): thêm contextual embeddings→sosánh thêm

4. Failureanalysis: zoom bottom-5 questions— dùng Diagnostic Treemap failure →fix M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 37 / 42

---

<!-- chiron-source-span: {"source_span_id":"724c71ae-cc16-5df9-9fa0-cefa83566f59","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"Bài tập cá nhân — 5 Modules (chọn 1, implement 1.5 giờ)","extraction_method":"pdf-text-layer"},"checksum":"610d8767fcb307e4ecf8bdca32e967f6251b754ab6cf500ec6d0521d874d6981"} -->

## Slide 50 - Bài tập cá nhân — 5 Modules (chọn 1, implement 1.5 giờ)

Module TODO Testpass criteria Điểm M1: Chunking Semantic, hierarchical, structure-aware. A/B test vsbasic baseline. 3 advanced outputs + com- parison table. Hierarchical có parent/child. 20 M2: Hybrid Search BM25 (Vietnamese segmenta- tion) + Dense + RRF fusion. Metadatafilter. Retrieve top-20 cho 10 queries. BM25 + Dense + Hybridscores. 20 M3: Reranking Integrate cross-encoder reranker. Top-20 → top-3. Latencybenchmark. Precision@3 improvement ≥15%. Latency<100ms. 20 M4: Evaluation RAGAS eval pipeline. 4 met- rics. Failure analysis bottom- 10. RAGAS report + diagnostic mappingchobottom-10ques- tions. 20 M5: Enrichment Summarize, HyQA,contextual prepend, auto metadata ex- traction. Enrichedchunks cósummary +questions + metadata. 20 Mỗi module có file riêng: m1_chunking.py, m2_search.py, m3_rerank.py, m4_eval.py, m5_enrichment.py. Mỗi file có# TODO: markers chỉ rõ cần implement gì. Nhóm5 người →mỗingười 1 module. Nhóm4 →gộpM5 vào người làm M1. Nhóm3 →gộpM4+M5, M1 do người mạnh nhất. Làm1 mình →chọnM1 hoặc M2 (core nhất). M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 38 / 42

---

<!-- chiron-source-span: {"source_span_id":"0a43eba0-73c5-5b4f-9a01-b9fe9c8892a5","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"Bàitập nhóm — Ghép thành ProductionRAG System (30 phút)","extraction_method":"pdf-text-layer"},"checksum":"2f5c58f852160986ef9933425a5edefd31304b8a830be2facd8bc68b220769a1"} -->

## Slide 51 - Bàitập nhóm — Ghép thành ProductionRAG System (30 phút)

### Cácbước ghép

1. Integrate: ghép M1→M5 →M2 →M3 thànhpipeline

2. RunM4: RAGAS eval end-to-end

3. Compare: basic baseline vsproduction pipeline

4. Failureanalysis: bottom-5, map vào ErrorTree

5. Present: 5 phút/nhóm —scores + 1 failurecase study Lưuý: Nếu1modulechưaxong →dùngfallbackimple- mentation trong scaffold (basic version có sẵn). Nhóm vẫnchạy được full pipeline.

### GitHubrepo chứa
├── m1_chunking.py ├── m2_search.py ├── m3_rerank.py ├── m4_eval.py ├── m5_enrichment.py ├── pipeline.py (ghép) ├── ragas_report.json ├── failure_analysis.md └── README.md

1. RAGAS scores (basicvs production)

2. Biggest improvement ởmodule nào?

3. 1 failure casestudy (Error Tree)

4. Nếu có thêm1 giờ, sẽ optimize gì? M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 39 / 42

---

<!-- chiron-source-span: {"source_span_id":"5e375d25-bddb-5066-a10f-30e0301de696","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"Hệthống chấm điểm — Cá nhân+ Nhóm","extraction_method":"pdf-text-layer"},"checksum":"bc96dbc0d3dec405f890a6a6c32f61139cf6469083a4a185c8850cfb97c67343"} -->

## Slide 52 - Hệthống chấm điểm — Cá nhân+ Nhóm

### Điểmcá nhân (60%)
Tiêuchí Điểm Moduleimplementation đúng 15 Testpass criteria đạt 15 Vietnamese-specifichandling 10 Codequality + comments 10 TODOmarkers hoàn thành 10 Subtotalcá nhân 60 Mỗimodule có test_m*.py. Chạy pytest test_m1.py →pass/fail. CIcheck: rufflint+ type hints.

### Điểmnhóm (40%)
Tiêuchí Điểm Pipelinechạy end-to-end 10 RAGAS ≥0.75(any metric) 10 Failureanalysis có insight 10 Presentationrõ ràng 10 Subtotalnhóm 40 +5: RAGAS Faithfulness≥0.85 +3: Structure-aware chunking integrated +2: Latency breakdown report Lưu ý: Tổng: 100 + 10 bonus. Cá nhân 60% + Nhóm40%. Đảm bảoai cũng contribute. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 40 / 42

---

<!-- chiron-source-span: {"source_span_id":"e01a1b56-7335-5811-a34a-8865a96710f4","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"StarterCode & Setup — Bắt đầungay","extraction_method":"pdf-text-layer"},"checksum":"4c2b4333917f79c1885c2d92faf9202e0a6805222658aae663369b60e558b288"} -->

## Slide 53 - StarterCode & Setup — Bắt đầungay

git clone github.com/vinuni-aicb/lab18 ├── main.py (entrypoint) ├── check_lab.py (kiểmtra) ├── data/ (samplecorpus) ├── test_set.json (20Q&A) ├── src/m1..m5_*.py (TODO) ├── src/pipeline.py (ghép) ├── tests/test_m*.py (auto-grade) ├── analysis/ (reports) └── naive_baseline.py (basic)

```text
1. docker compose up -d (Qdrant)
2. pip install -r requirements.txt
3. python naive_baseline.py (basic)
```

4. M￿ src/m*_*.py → tìm TODO

5. Implement → pytest tests/ Lưuý: Chạy naive_baseline.pyTRƯỚCđểcóba- sic scores. Mọi improvement so sánh với baseline này. M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 41 / 42

---

<!-- chiron-source-span: {"source_span_id":"e20a1646-4953-5f54-8747-c398b3b97fe2","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"799b885011607801981da2fb115d1769b22916faa35ef8b474069bc8d0346ee7"} -->

## Slide 54 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 RAG =OFFLINE(Ingestion + Enrichment) +ONLINE(PreRAG →R →A →G →PostRAG) —biết failure ở bước nàomới fix đúng chỗ 2 Fix OFFLINE: Chunking (hierarchical) + Embedding (chọn đúng model) + Enrichment Pipeline(summarize,HyQA, contextual) = nền tảng 3 Fix ONLINE: PreRAG (query rewrite)→ Hybrid Search + Reranking→ Augmentation (NLI, citation,fusion) →Generate+ PostRAG 4 Measure: RAGAS→ErrorTree →DiagnosticTree →đúngeval framework 5 Beyond: AgenticRAG(agent-controlledpipeline)+RAGcó fundamentallimits (embedding alignmentgap) →cầndiagnose failure typeM.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 41 / 42

---

<!-- chiron-source-span: {"source_span_id":"c5e70f83-f9e1-53f6-b7c5-7cfea4929cd7","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"48f2ba539891adacb33d22a01ca5ecdeff7d63e6f53dd0270eb990b331f2c53a"} -->

## Slide 55 - Tiếptheo & Bài tập

Ngày 19: GraphRAG & Knowledge Graphs “Khi user hỏi về mối quan hệ giữa 5 entities — flat RAG trả lời sai, GraphRAG trả lời đúng — tại sao?”

- Hoànthành Lab 18: Production
RAGpipeline + RAGAS report

- Đọc: Microsoft GraphRAG paper
(2024)

- Optional: Skill-RAG (arxiv
2604.15771),SKILL-RAG (arxiv 2509.20377),MASS-RAG (arxiv 2604.18509) M.ScTrầnMinh Tú (VinUni) AICB· Ngày 18 Tuần4 42 / 42

---

<!-- chiron-source-span: {"source_span_id":"0744f162-aae9-5d1f-b01b-43ac1ebfa785","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer-sparse","page_image":"../../assets/page-images/8f74d016e7d1/page-0056.png","visual_fallback":true},"checksum":"ddafff7d95a561eaa9df8fdb6a18ffc6f4535eae4281d4d9b6c9a93c6c52bd52"} -->

## Slide 56 - Hỏi& Đáp

![Visual fallback - track 3 - day 18 - slide 56](../../assets/page-images/8f74d016e7d1/page-0056.png)

> Trang này được giữ dưới dạng ảnh vì text layer/OCR không đủ để biểu diễn nội dung trực quan.

---

<!-- chiron-source-span: {"source_span_id":"1223f73b-38af-5057-a3ec-dc0c5c03a9d8","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"2f76d458775fb2217e20b9ced7dc4ae6887744b1a1c8cb6f9b27620fd1d70651"} -->

## Slide 57 - Cảmơn!

AICB-P2T3 · Ngày 18 · Production RAG
