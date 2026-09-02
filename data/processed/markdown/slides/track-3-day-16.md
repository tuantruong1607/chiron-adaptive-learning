---
schema_version: 1
course_id: rag-intensive
document_id: "9fabfcc7-e0b2-51f7-8c51-a2bd9283be79"
document_version_id: "94bcbc99-002e-5444-a7da-c25065438745"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "VinUniversity"
source_file: "track 3 - day 16.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 16.pdf"
source_sha256: "c9346df023f57bb98842e7b43d93b423b58dedc8221ec1b07aa489c620e89534"
parser_version: chiron-structured-markdown-v1
page_count: 44
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":44}"
language: vi
---

# VinUniversity

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"13f00167-2403-5e62-9e8e-ae82b373375d","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"VinUniversity","extraction_method":"pdf-text-layer"},"checksum":"e06da08e02cea73843c200b2ab98fe2ceac06323bf28f1daade3094a1be8abeb"} -->

## Slide 1 - VinUniversity

Advanced Agent Architectures AICB-P2T3 · Ngày 16 · Chương 4 — Agent Nâng Cao Giảng viên VinUniversity · Phase2·Track3·Tuần4

---

<!-- chiron-source-span: {"source_span_id":"438a8913-34a5-5e2c-8905-0165e116a06c","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"Hook","extraction_method":"pdf-text-layer"},"checksum":"f8e659abfef1f1612021f4437fcce7c27a8f5c49710fb9051f768b707bd3ce50"} -->

## Slide 2 - Hook

Tại sao Reflexion agent giải quyết được bài toán mà ReAct không làm được? Hômnaytasẽtrảlờicâuhỏinàybằngbenchmark,patternvà democode. AICB·Ngày16 1

---

<!-- chiron-source-span: {"source_span_id":"7f8d7338-96a0-53d3-b090-4a0d9910b26d","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Agenda","extraction_method":"pdf-text-layer"},"checksum":"6e6e43f10fd6a13d9c4c597f62168b0740996d1dc04a8e6d674f21ba995aac88"} -->

## Slide 3 - Agenda

1 Khinàosingle-agentthấtbại? 2 Reflexion: thêmself-evaluationvàoloop 3 LATS,Voyagervàdecisionmatrix 4 Kỹthuậtnângcaotrướckhivàolab 5 Demo+lab+auto-grading AICB·Ngày16 2

---

<!-- chiron-source-span: {"source_span_id":"abe8e71e-631c-5585-9c0d-952310d65a5a","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Khi nào Single Agent thất","extraction_method":"pdf-text-layer"},"checksum":"146e93659a8c264dd08ac7fb091ed4546fcf64ddba967fda79146766a734138f"} -->

## Slide 4 - Khi nào Single Agent thất

bại? ReAct—mạnhnhưngkhôngbiếtsửalỗi

---

<!-- chiron-source-span: {"source_span_id":"d65a0b78-2bbf-59c8-9a0c-dfb04456baf1","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"ReAct — Reasoning + Acting","extraction_method":"pdf-text-layer"},"checksum":"7c9d496f0319765463999405726a6c0f0408c847ea5faa8c6eb3cc1d54d1e403"} -->

## Slide 5 - ReAct — Reasoning + Acting

Thought Action Observation suyluận gọitool kếtquả Lặp đến khi có câu trả lời

- Xenkẽ Reasoning(suynghĩ)+
Acting(hànhđộng)

- Agenttựquyếtđịnh: gọitoolnào,
khinàodừng

- ĐãhọcởGĐ1—nềntảngcho
mọiagentpattern Nhắc lại ReAct = “Think before you act” — mỗibướcagentgiảithíchlýdotrước khihànhđộng AICB·Ngày16 4

---

<!-- chiron-source-span: {"source_span_id":"08c977b4-af3f-5cbf-b567-a6689800ffbf","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"ReAct thất bại khi nào?","extraction_method":"pdf-text-layer"},"checksum":"6366e4b7d4b369dc6920c36790a8958fd6797c3dec97b2e4b0f2bb357426837c"} -->

## Slide 6 - ReAct thất bại khi nào?

Thought: tìmX Search(X) Kếtquảsai Thought: dùngX Lookup(X) Saitiếp Thought: kếtluận TrảlờiSAI Không detect lỗi!

### 3 failure modes chính
1 Lỗi lan tỏa: Saiởbước1→sai hếtchuỗi 2 Infinite loop: Tooltrảnoise→ agentlặpmãi 3 Không backtrack: Đisaiđường nhưngkhôngquaylại Lưu ý Rootcause:ReAct không có cơ chế tự đánh giá. Khi đi sai, không có signal nào báo “dừng lại, suy nghĩ lại”. AICB·Ngày16 5

---

<!-- chiron-source-span: {"source_span_id":"7b2229ff-749a-5e76-9c76-381ee426a567","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Bài học production 2025–2026: đừng nâng cấp agent quá sớm","extraction_method":"pdf-text-layer"},"checksum":"067853ed1db9ec58993e62e90f51b953616058dd1473a0351973820a43f1daf5"} -->

## Slide 7 - Bài học production 2025–2026: đừng nâng cấp agent quá sớm

- Nhiềubàitoánthựctếchỉcần retrieval + tools + structured output

- Bắtđầubằng single-agenthoặcworkflowđơngiản,sauđómớithêmcomplexity

- Chỉchuyểnsangmulti-agentkhicó tool overload,promptquánhiềunhánh
logic,hoặccần specialist ownership Thông điệp cho học viên Đừnghọcpatterntheokiểu“càngnhiềuagentcàngtốt”. Hãychọnpatterntheo mức độ cần thiết củataskvàchiphívậnhành. AICB·Ngày16 6

---

<!-- chiron-source-span: {"source_span_id":"99b51058-425d-5367-a8fb-320d1ed02fee","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Ví dụ thực tiễn: PR review agent bị lỗi lan tỏa thế nào?","extraction_method":"pdf-text-layer"},"checksum":"d36a580f5c619f50e1580fbdb3b64332f847452e9b831191902af097bda87319"} -->

## Slide 8 - Ví dụ thực tiễn: PR review agent bị lỗi lan tỏa thế nào?

1 Agentđọcsaimoduletrongdiffngaytừbướcđầu 2 Gọichecker/searchtrênfilekhôngliênquan 3 Tổnghợpevidencesainhưngvẫntựtinkếtluận 4 ReActthườngkhôngcósignalrõđểtựdừngvàsửa Vì sao Reflexion giúp hơn? Evaluatorcóthểchấm: “kếtluậnchưagroundedvàodiffvàtestlogs”. Reflectorbiến lỗiđóthànhchiếnlượcmớicholầnchạytiếptheo. AICB·Ngày16 7

---

<!-- chiron-source-span: {"source_span_id":"80e94d61-c039-5081-bc95-8aeb4a9bd0fc","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Bằng chứng: ReAct struggle với multi-hop reasoning","extraction_method":"pdf-text-layer"},"checksum":"e132c022044d6044b5a5c12063de757a91e55eb29a48ef339e669d321ed42aa0"} -->

## Slide 9 - Bằng chứng: ReAct struggle với multi-hop reasoning

35.1% ReActEM trênHotpotQA Cao Failrate trênmulti-hop 0 Sốlần agenttựsửalỗi Câu hỏi then chốt Nếuthêmchoagentkhảnăng tự đánh giá kếtquảvà rút bài học từsailầm thìsao? →Đóchínhlàýtưởngcủa Reflexion. AICB·Ngày16 8

---

<!-- chiron-source-span: {"source_span_id":"f02bed82-517f-5104-b7dd-ac6b14772502","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Reflexion — Dạy Agent tự","extraction_method":"pdf-text-layer"},"checksum":"d77fb74eab6ef9e357de96d91ed3c1f17933f75774f733499d9aeead7d26e984"} -->

## Slide 10 - Reflexion — Dạy Agent tự

phản tỉnh Thêmself-evaluationvàoreasoningloop

---

<!-- chiron-source-span: {"source_span_id":"0c6b6896-6008-5bfc-a266-1a70aeee1df2","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Ý tưởng cốt lõi","extraction_method":"pdf-text-layer"},"checksum":"56f0bb8a4ffe7c11be1219b8d8de40b51ef8ec3091a78a76c590b7812dea0907"} -->

## Slide 11 - Ý tưởng cốt lõi

Reflexion (Shinn et al. 2023) Thêm2thànhphầnvàoReAct: Evaluator(đánhgiákếtquả)và Reflector (rút bài học). Agent thử, đánh giá, suy ngẫm, rồi thử lại — giống cách con ngườihọctừsailầm. Analogy: Nhưsinhviênlàmbàithi. Lần1sai→xemđápán,hiểutạisaosai

- lần2làmđúng. ReActchỉlàm1lầnrồinộp. Reflexionchophép“xemlại
bài”vàsửa. AICB·Ngày16 10

---

<!-- chiron-source-span: {"source_span_id":"121ed5dc-5f12-50e3-b80f-5148ce6f1473","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Kiến trúc Reflexion — 4 bước","extraction_method":"pdf-text-layer"},"checksum":"69c8e535abd8c5855fc0731fba1652c6c08cccc9e1df1650da99aa639a528882"} -->

## Slide 12 - Kiến trúc Reflexion — 4 bước

1. Generate Actor

2. Evaluate Evaluator

3. Reflect Reflector

4. Retry Actor ReflectionMemory “Saiởđâu? thửgìtiếp?” Lặp tới khi đúng hoặc hết attempts score=1? score=0 3 vai trò LLM Actor: sinhhànhđộng Evaluator: chấmđúng/sai Reflector: rútbàihọc Điểm khác biệt vs ReAct Dùng text feedback thayvìgradient. Critique bằng ngôn ngữ tự nhiên nên dễ parse,debugvàbenchmark. AICB·Ngày16 11

---

<!-- chiron-source-span: {"source_span_id":"ba2830fd-f40c-5fee-a797-c8e20d8fb55f","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Reflexion State — Code-Level","extraction_method":"pdf-text-layer"},"checksum":"bbb1724898abc0bc915b87ba0408ec421484ec90e3a4f20f82e3674e6aceaa91"} -->

## Slide 13 - Reflexion State — Code-Level

Python schema

```text
class ReflexionState(TypedDict):
```
messages: list[BaseMessage] trajectory: list[str] reflection_memory: list[str] attempt_count: int success: bool REFLECT = ``failed because: {error}'' ``lesson: {lesson}'' ``next strategy: {strategy}''

### 5 thành phần state
1 messages: hộithoạihiệntại 2 trajectory: lịchsửhànhđộng 3 reflection_memory: bàihọc rútra 4 attempt_count: sốlầnthử 5 success: đãđúngchưa? Lưu ý Dùng sliding window: quá ngắn thì quên, quá dài thì tốn context. AICB·Ngày16 12

---

<!-- chiron-source-span: {"source_span_id":"05ff195b-227f-5881-86a8-4c29f4e11176","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Reflexion trong LangGraph","extraction_method":"pdf-text-layer"},"checksum":"f8d7a79aaa560610d381efde428fba12d44f52744d180d023af039e496e1e78b"} -->

## Slide 14 - Reflexion trong LangGraph

act success? END reflect Yes No append reflection, reset, attempt++ max attempts? → END Node “reflect”

1. Lấytrajectory(đãlàmgì?)

2. GọiReflectorLLM(saiởđâu?)

3. Appendreflectionvàomemory

4. Resetmessages,tăngattempt T ermination Dừng khi: success=True Hoặc: attempt ≥max(default3) Tránhinfiniteloop—cáimàReActgặpphải AICB·Ngày16 13

---

<!-- chiron-source-span: {"source_span_id":"6e3b1de2-a021-5a04-b7be-d3dad731089b","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Evaluator prompt nên được thiết kế thế nào?","extraction_method":"pdf-text-layer"},"checksum":"e484d58ad1597d34c868eb85d85c17f7da47e5d1a456940d6eedb97aa10ade52"} -->

## Slide 15 - Evaluator prompt nên được thiết kế thế nào?

```text
class JudgeResult(BaseModel):
```
score: int reason: str missing_evidence: list[str] spurious_claims: list[str]

- Outputnênlà structured
thayvìfree-form

- Scorephảiđikèm reasonvà
evidence gap

- Nếuevaluatorquávague,
reflectionsẽkhông actionable Best practice Dùng Pydantic/JSON schema để labdễparse,benchmarkvàauto- grade. AICB·Ngày16 14

---

<!-- chiron-source-span: {"source_span_id":"126d4197-84ba-516b-9683-5ae883f1fe12","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Reflection memory: ghi gì, bỏ gì?","extraction_method":"pdf-text-layer"},"checksum":"695ade0962d731e94e0c42193f0771bdccfdcc70845bc6ace9a7e75fa97b14df"} -->

## Slide 16 - Reflection memory: ghi gì, bỏ gì?

- Nên ghi: failurereason,lesson,nextstrategy,evidencetitles

- Không nên ghi: toànbộtracedàidòngnếukhônggiúplầnthửsau

- Cóthểdùng sliding window hoặc memory compression
T eaching point Memorytốtlàmemory ngắn, cụ thể, hành động được. Khôngphảimemorycàng dàicàngtốt. AICB·Ngày16 15

---

<!-- chiron-source-span: {"source_span_id":"84107fd1-cac5-5fd1-baca-515a21f8156d","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Reflexion failure modes trong production","extraction_method":"pdf-text-layer"},"checksum":"0dd1119ccbe0a2b600c7f00f627e68245079e9214b23e9ab90b0fdf66120cca5"} -->

## Slide 17 - Reflexion failure modes trong production

1 Evaluator bias: tựchấmquádễhoặcquákhắtkhe 2 Reflection drift: bàihọcchungchung,khônggiúpđượcattemptsau 3 Context bloat: reflectionmemorychiếmhếtcontextwindow 4 Cost blow-up: accuracytăngítnhưngchiphítăngmạnh Thông điệp Reflexion không miễn phí. Cần đánh giáaccuracy gain so với cost/latency in- crease. AICB·Ngày16 16

---

<!-- chiron-source-span: {"source_span_id":"4fb1bad1-7a64-5beb-a1dc-941da1962570","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Reflexion cải thiện đáng kể","extraction_method":"pdf-text-layer"},"checksum":"814364752a0e8c9bee49f1bca545beea1e5f20f0ee431addc60b30c54eab860b"} -->

## Slide 18 - Reflexion cải thiện đáng kể

91% HumanEval (codegen) 80% HotpotQA (multi-hopQA) +20–30% Cảithiện vsReAct Tại sao hiệu quả? Reflexiondùng episodic memory—agent“nhớ”bàihọctừcáclầnthửtrước trong cùng episode. Giống cách bạn nhớ “lần trước đã thử cách này không được,lầnnàythửkhác”. AICB·Ngày16 17

---

<!-- chiron-source-span: {"source_span_id":"e34c5c2d-c66f-536c-9749-b774ba8d1c54","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Bức tranh rộng hơn","extraction_method":"pdf-text-layer"},"checksum":"9ae085d80c01ee7cd4bba1c079f773ece0be86fe9c27bc30c7c7fc7c876e202e"} -->

## Slide 19 - Bức tranh rộng hơn

LATS,Voyagervàkhinàonêndùngagentphứctạp

---

<!-- chiron-source-span: {"source_span_id":"3700b283-b3e1-5910-9cef-7a1413fe48a4","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"LATS — Khi cần tìm đường tối ưu","extraction_method":"pdf-text-layer"},"checksum":"076a4180e821f9d0e5486557ae33f78f7f7bde97a4d30795b74193c57b705589"} -->

## Slide 20 - LATS — Khi cần tìm đường tối ưu

S0 A1 A2 A3 B1 B2 B3 UCT chọn nhánh tốt

- Highvalue •Lowvalue
LATS MCTS + LLM: mỗi node là một trạng thái suy luận;LLMđóngvai policy, valuevà simulation.

- ChínhxáchơnReflexion(92.7%vs91%)

- Nhưngtốngấp3–5 ×compute

- Cầnenvironmentchophép undo
Lưu ý Chỉđángdùngkhitaskcógiátrịcaovàcó thểrollback,nhưcodegenhoặcgame. AICB·Ngày16 19

---

<!-- chiron-source-span: {"source_span_id":"69af30db-9155-5003-9869-9b29aae7531c","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Voyager — Agent tích lũy kỹ năng","extraction_method":"pdf-text-layer"},"checksum":"2023955fce1f2fd15422b0354a6414a76297053991283a3c3b236ee9d91f5a84"} -->

## Slide 21 - Voyager — Agent tích lũy kỹ năng

Auto Curriculum Code Generator Verify & DebugSkillLibrary(DB) task verifiedskill retrieve skills

- Agenttựđặtmụctiêu,viếtcode,lưu
skillđãverified

- Skillmớixâytrênskillcũ
(compound learning)

- Sau3h: 63skillsvs7củaAutoGPT
Ứng dụng thực tế Hợp với code generation, DevOps au- tomationvàcácdomaincầntíchlũy“thư việnkinhnghiệm”quanhiềuepisode. AICB·Ngày16 20

---

<!-- chiron-source-span: {"source_span_id":"2b3b7f20-e893-5ad2-a8f8-b5ad433a358b","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Khi nào dùng pattern nào?","extraction_method":"pdf-text-layer"},"checksum":"2d780ec9d694eb565f48151b5cef9c1c28a7f811f95ead7b05cbe370d68b1851"} -->

## Slide 22 - Khi nào dùng pattern nào?

Pattern Memory Chi phí Accuracy Khi nào dùng? ReAct Không $ Baseline Taskđơngiản,1bước Reflexion Episodic $$ +20–30% Multi-step,cầnself-correct LATS Tree $$$$$ +∼2% High-stakes,chophépundo Voyager Persistent $$$ N/A Open-ended,cầntíchlũy Lưu ý Nhiềubàitoánthựctế không cần agent: retrieval,templatefill,structuredoutput đãđủ. Đọc: “ AI Agents That Matter”(2024)—đừngover-engineer. AICB·Ngày16 21

---

<!-- chiron-source-span: {"source_span_id":"c35dca85-056f-5cd3-a53a-64f450e0b100","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Case study mới: multi-agent research system","extraction_method":"pdf-text-layer"},"checksum":"7375759b167870a06a26beda4b782464311b781bf1030fa2b859d35a45b1b857"} -->

## Slide 23 - Case study mới: multi-agent research system

- Mộtplanneragentchiacâuhỏithànhnhiềusub-questions

- Cácworkeragentstìmthôngtinsongsong

- Mộtsynthesizeragenthợpnhấtvàviếtcâutrảlờicuốicùng

- Patternnàyhợpvới open-ended research,khôngphảimọibusinessworkflow
Lesson Multi-agent có ý nghĩa khi bài toánmở, khó dự đoán trước các bước, và có lợi từ parallelexploration. AICB·Ngày16 22

---

<!-- chiron-source-span: {"source_span_id":"3cb97649-2e43-505f-b105-b7be0b1a8de6","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Checklist triển khai an toàn cho agent nâng cao","extraction_method":"pdf-text-layer"},"checksum":"f6f0976a2206bff555c5fe8e4e34dfd3bee199d46afcd3f1134607c4e959055f"} -->

## Slide 24 - Checklist triển khai an toàn cho agent nâng cao

1 Có max_attempts 2 Cóstructuredoutputschoevaluator/tools 3 Cótraceđểdebugtừsớm 4 Toolcàngdeterministiccàngtốt 5 Cóhumanreviewchoactionrủiro Production mindset Promptchỉlà1phần. Cònlạilàstate,toolquality,tracing,evalvàguardrails. AICB·Ngày16 23

---

<!-- chiron-source-span: {"source_span_id":"a0f3c7fb-103d-5ed8-8848-afd23b29d67f","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Kỹ thuật nâng cao trước khi","extraction_method":"pdf-text-layer"},"checksum":"c2d29c4dd50a08ca0fb54a04df9012941372e521e6e93d9b7d9e97de578c5ca9"} -->

## Slide 25 - Kỹ thuật nâng cao trước khi

vào lab Cácpatternproductiongiúpagentổnđịnh,dễdebugvàdễđánh giáhơn

---

<!-- chiron-source-span: {"source_span_id":"27c6d947-64c0-530b-a668-73ef9537970b","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"T emplate kiến trúc agent production-ready","extraction_method":"pdf-text-layer"},"checksum":"9b8d1e7a87dbbd2f9aac0e64d65b4c88c76d4774ed28c097290d6566475a782a"} -->

## Slide 26 - T emplate kiến trúc agent production-ready

User task + context Plan / Route Act with tools Verify / JudgeReflect / Update memoryFinal answer or escalate Tracing+evaldatasetGuardrails+humanreview retry

- Đừngdừngởprompt+tool
loop

- Thêm judge, memory, trace
và guardrails

- Táchrõphần reasoningvới
phần execution

- Chuẩnhóastateđểbenchmark
vàauto-gradedễhơn Rule of thumb Bắtđầutừpipelineđơngiảnnhất. Chỉ thêm lớp mới khi đo được lỗi hoặcthấybottleneckrõràng. AICB·Ngày16 25

---

<!-- chiron-source-span: {"source_span_id":"2ecdf707-23b9-580e-b302-9a9fa91c4bf5","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Evaluator tốt quyết định chất lượng Reflexion","extraction_method":"pdf-text-layer"},"checksum":"86ea4f20ae81ec7b811642bc5eb33e9a84247d859db891174aaac39d4d901ef3"} -->

## Slide 27 - Evaluator tốt quyết định chất lượng Reflexion

Evaluator nên chấm 4 thứ 1 Correctness: câutrảlờicóđúng không? 2 Grounding: cóbámevidence/tool outputkhông? 3 Completeness: đãtrảlờiđủcácphần chưa? 4 Actionability: reflectioncóthểsửa đượckhông? Anti-pattern Nếu evaluator chỉ nói``incorrect'' thì re- flectorrấtkhósinhbàihọchữuích. Ví dụ output có cấu trúc

```text
{
```
"is_correct": false, "failure_mode": "missed-hop", "evidence_used": ["wiki:person_a"], "feedback": "Bạn đã đúng hop 1 nhưng chưa verify hop 2.", "next_action": "search_second_hop" } Thiết kế tốt Structuredoutputgiúplog,filtertheofail- ure mode và chuyển thẳng sang auto- grading/reporting. AICB·Ngày16 26

---

<!-- chiron-source-span: {"source_span_id":"9f35025a-4d69-5fa4-8ce9-cf13fce97a06","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Reflection memory: lưu bài học, không lưu nguyên chat history","extraction_method":"pdf-text-layer"},"checksum":"e664d05de0e4acfcc0c1540f2601522d09a9fe5101461d399be9dc5ef2be7af5"} -->

## Slide 28 - Reflection memory: lưu bài học, không lưu nguyên chat history

Memory entry nên ngắn và thao tác được lesson: “Luônverifythựcthểởhop2trước khitrảlời” trigger:“Câuhỏi2-hopcóentitydễnhầm” fix: “Search thêm 1 bước và so khớp tên riêng”

- Mỗientrychỉ1lỗi+1cáchsửa

- Ưutiênmemorycócấutrúchơn
free-formdài

- Nêncó compression/evictionkhi
episodedài

1. Verifyhop2entitybeforeanswer

2. Usetoolresult,notpriorbelief

3. Ifambiguityremains,askorabstain Compressedmemory: “Verifyevidencebeforefinalanswer” Điểm dạy học quan trọng Memorytốtlàm giảm lặp lỗi,nhưngmem- ory dài quá lại làm prompt noisy và tăng cost. AICB·Ngày16 27

---

<!-- chiron-source-span: {"source_span_id":"41eaf0fc-e523-5584-9efd-9eca78a05fb7","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Plan - Act - Verify tách bạch sẽ ổn định hơn loop “nghĩ rồi làm","extraction_method":"pdf-text-layer"},"checksum":"9c5a5da4fcbc0dce0e9c63047b8ea93bbdc07e96e3c1bb17ad3a5b9889779343"} -->

## Slide 29 - Plan - Act - Verify tách bạch sẽ ổn định hơn loop “nghĩ rồi làm

luôn” Plan subgoals Act / call tool Verify observation Next step or finish badevidence

- Plan: liệtkê2–4subgoalsquansát
được

- Act: chỉgọi1toolphùhợpchomỗi
subgoal

- Verify: kiểmtraoutputcóthậtsựgiải
quyếtsubgoalkhông

- Tránhđểmodel“nhảycóc”từplan
sangfinalanswer Khi nào rất hữu ích? Multi-hopQA,code/debug,dataextraction nhiềubước,workflowcóexternalstate. AICB·Ngày16 28

---

<!-- chiron-source-span: {"source_span_id":"f9105ce0-bf10-5cf3-9c6b-ff13382ab8ca","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Độ tin cậy của tool quan trọng không kém độ mạnh của model","extraction_method":"pdf-text-layer"},"checksum":"5ba27f1f3625c59b4cfd1e1c796b6be9cccdb336e2398c11005871ab63ebc539"} -->

## Slide 30 - Độ tin cậy của tool quan trọng không kém độ mạnh của model

5 kỹ thuật tăng reliability 1 Schemachặtchoinput/outputtool 2 Retrycóđiềukiệncholỗitạmthời 3 Idempotentactionchothaotácghidữ liệu 4 Timeout+fallbackkhitooltreo 5 Risktiering: read-onlyvs write/high-impact Production rule Tool nào ghi dữ liệu, gửi email, thanh toán, xóabảnghi... nêncóhumancheckpointhoặc approvalgate. Prompt/tool contract Good: “Nếu search không trả evi- dence rõ ràng, không được đoán; trả về insufficient. Bad: “Cốgắngtrảlờibằngmọigiá.” Nhìn dưới góc dạy học Sinh viên thường tối ưu prompt trước, nhưngbugthựctếhaynằmởtoolschema, parser,timeout,retryvàsideeffects. AICB·Ngày16 29

---

<!-- chiron-source-span: {"source_span_id":"95f06198-e0c4-518b-98f7-a7c40c1abf40","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Observability + eval flywheel: cách agent tiến bộ sau mỗi lần","extraction_method":"pdf-text-layer"},"checksum":"ead14ab01560a1c0b8ca54504334d2546ba8107e7e6240e915dce56509ed6c5b"} -->

## Slide 31 - Observability + eval flywheel: cách agent tiến bộ sau mỗi lần

demo T race runs Label failures Build eval set Run gradersFix prompt/tool/stateRe-test / redeploy

- Đừngchỉlogfinalanswer

- Hãylogcảdecision,toolcalls,
retryvàfailuremodes

- Từtracemớisinhradataset
chấmtựđộngcóích Liên hệ với lab report.json, runs.jsonlvàbreak- down failure modes chính là phiên bảnminicủaevalflywheelnày. AICB·Ngày16 30

---

<!-- chiron-source-span: {"source_span_id":"159a0123-761e-5101-a38c-d658401742f7","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Khi chưa cần multi-agent","extraction_method":"pdf-text-layer"},"checksum":"9a57c325ccfa84e8922eda934cfc1f68c6660fcc48f0a5314820b21448ad4839"} -->

## Slide 32 - Khi chưa cần multi-agent

Thử 4 bước này trước 1 Routerhoặctoolpolicytốthơn 2 Plan-then-act+verifier 3 Reflexion+memory+eval 4 Guardrails+approvalgateschotoolcó sideeffects Vì sao? Nhiềulỗitưởnglàdo“thiếuagentchuyêngia” nhưng thực ra đến từ tool schema kém, thiếu evaluatorhoặcthiếutrace.

- Nếuchỉcó1domaintoolchính,hãy
giữsingle-agent

- Nếutasklàworkflowcốđịnh,prompt
chaininghoặcroutingthườngđủ

- Nếulỗichínhlàhallucination,hãy
sửagrounding/evaluatortrước Heuristic Complexitychỉnêntăngsaukhibạnđã cóbenchmarkbaselinevàbiếtrõbottle- necknằmởđâu. AICB·Ngày16 31

---

<!-- chiron-source-span: {"source_span_id":"847015e3-514f-5d49-b8fc-604f6fe2ec5a","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Khi multi-agent bắt đầu đáng tiền","extraction_method":"pdf-text-layer"},"checksum":"08cde0883298498e4a255462e3c867d5308e03f42e0d4f2207c0a569e0d9ce3f"} -->

## Slide 33 - Khi multi-agent bắt đầu đáng tiền

Dấu hiệu phù hợp

- Nhiềudomaintoolrấtkhácnhau

- Cần parallel exploration cho
open-endedresearch

- Cầntáchvaitrò planner / worker /
judge / synthesizer

- Cầntách read/write agents đểgiảm
risk Ví dụ phù hợp Research system, code review + synthe- sis,opsassistantcóapprovalworkflow. Quy tắc an toàn Càngnhiềuagent,càngcầnhandoffcon- tract rõ ràng: input schema, output schema, stop condition, ownership của state. Thông điệp cuối phần lý thuyết Phứctạphơnkhôngmặcđịnhtốthơn. Chỉlênmulti-agentkhi single-agent + tools + eval + memory đãchạmtrầnrõràng. AICB·Ngày16 32

---

<!-- chiron-source-span: {"source_span_id":"67a75e29-6648-5cc4-bd0f-3608da8b1bf0","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Demo & Thực hành","extraction_method":"pdf-text-layer"},"checksum":"482e63fdba567a450600b25b445b012bd9378b0a91848e9ab2e998310f76169a"} -->

## Slide 34 - Demo & Thực hành

XemReflexionhoạtđộngthựctế

---

<!-- chiron-source-span: {"source_span_id":"8ed155e9-bc64-55f9-a110-c8e83eedce10","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Demo: ReAct vs Reflexion — Side-by-side trên HotpotQA","extraction_method":"pdf-text-layer"},"checksum":"ab965659c97ea838c99b3c0e833848d6796027c59098b24cddbe60dbf1bfd863"} -->

## Slide 35 - Demo: ReAct vs Reflexion — Side-by-side trên HotpotQA

- Cùngcâuhỏi2-hop,chạycảhaiagentvớiLangSmithtracing

- ReAct: saientityởhop1,lỗilantỏa,trảlờisai

- Reflexion: attempt1sai→Evaluatorchoscore=0→Reflectorsinh
bàihọc→attempt2đúng

- Sosánh: trace,accuracy,cost/query
AICB·Ngày16 34

---

<!-- chiron-source-span: {"source_span_id":"45975bdd-31d5-5001-8658-c11c4500d080","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Lab 16: Implement Reflexion agent từ scratch với LangGraph","extraction_method":"pdf-text-layer"},"checksum":"5b1efccf4ae0fa5c95694ee0db1450ea9722dcedfd402dc3518444b5af3e9f3b"} -->

## Slide 36 - Lab 16: Implement Reflexion agent từ scratch với LangGraph

Mục tiêu: Reflexionagentrepo+benchmarkreport(EMcomparison, costanalysis,failurecategorization) Thời lượng: 2giờ AICB·Ngày16 35

---

<!-- chiron-source-span: {"source_span_id":"75fb5acf-9386-54ee-ac2f-e5c839952d30","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Lab 16 — Các bước thực hành","extraction_method":"pdf-text-layer"},"checksum":"542e1c64036a1a08eb18ef2e0a86dc21edde7d574e20e15b2dc62d72dcd5f175"} -->

## Slide 37 - Lab 16 — Các bước thực hành

1 Build state machine: nodes=[act,evaluate,reflect,terminate],edgescó conditionalrouting 2 Build Evaluator: LLM-as-Judge,promptyêucầuscore0–1+reason,parse outputPydantic 3 Add reflection memory: mỗientry=(attempt_id,failure_reason,lesson, strategy_next) 4 Benchmark: ChạyReflexionvsReActtrên20câuHotpotQA—đoEM,attempts, tokencost Deliverable GitHubrepo+benchmarkreport: bảngsosánhEM,phântíchcost,phânloạifailure modes AICB·Ngày16 36

---

<!-- chiron-source-span: {"source_span_id":"14410226-001f-54ee-a455-d691b6e746ee","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Lab roadmap 120 phút","extraction_method":"pdf-text-layer"},"checksum":"794b5d220bea348ab3e7f2cb4091307bd599797cd772c8525fcb0a77fadf027c"} -->

## Slide 38 - Lab roadmap 120 phút

1 30 phút: chạyReActbaselinevàhiểutrace 2 35 phút: thêmEvaluatordạngstructuredoutput 3 25 phút: thêmReflector+reflectionmemory 4 30 phút: benchmark,viếtreport,sinhartifactđểauto-grade Instructor tip Chohọcviênchạymockmodetrướcđểhiểuformatoutput,sauđómớithayprovider thật. AICB·Ngày16 37

---

<!-- chiron-source-span: {"source_span_id":"073bb3a9-68b7-5c3c-8be6-3f543e2568a5","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Bonus tasks để phân hoá học viên","extraction_method":"pdf-text-layer"},"checksum":"5914716dd17b393883369dad5ebc4ded6f3a416807de642bde88503e5ec60211"} -->

## Slide 39 - Bonus tasks để phân hoá học viên

- adaptivemaxattempts

- memorycompression

- evidence-groundedevaluator

- mini-LATSbranching(2candidates/step)

- plan-then-executetrướckhireflect
Cách chấm Khôngchỉchấm“cólàmđượckhông”màchấmthêm thí nghiệm, trade-off và giải thích. AICB·Ngày16 38

---

<!-- chiron-source-span: {"source_span_id":"dc9f0202-4113-50a8-99c8-f6a5ac644e11","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Deliverable schema để dễ chấm tự động","extraction_method":"pdf-text-layer"},"checksum":"e1968ea57f673d66df51aa08a61760f2226b3f4b1b8f8caffc7ca71469e38f0c"} -->

## Slide 40 - Deliverable schema để dễ chấm tự động

- report.json: metrictổnghợp

- report.md: narrativeanalysis

- react_runs.jsonl, reflexion_runs.jsonl: tracetheotừngcâuhỏi

- GiữschemaổnđịnhđểTAchấmobjectivenhanh
Outcome Sinhviênvừahọcpatternagent,vừahọctưduy evaluation-driven engineering. AICB·Ngày16 39

---

<!-- chiron-source-span: {"source_span_id":"8e9007fe-c626-5755-86de-a379e1d3840d","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Tổng kết","extraction_method":"pdf-text-layer"},"checksum":"62d487800d0a2476c61fe8a207f762c9d10dc22f774ed1a7c1ab62acbd6ddced"} -->

## Slide 41 - Tổng kết

T akeaway 1 Reflexion là nâng cấp hợp lý khi ReAct thấtbại: costvừaphải,accuracytăngrõ. T akeaway 2 LATS và Voyager đổi compute lấy opti- malityhoặcgenerality;chỉdùngkhitask thậtsựcần. T akeaway 3 Cẩnthận“degeneration-of-thought”: re- flectionkéodàicóthểlàmoutputtệhơn. T akeaway 4 Xuhướngproduction:structuredoutputs, tracingvàevalquantrọnghơnfree-form reasoning. AICB·Ngày16 40

---

<!-- chiron-source-span: {"source_span_id":"63f5265c-e13d-5135-b050-9893540e8569","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Ngày 17: Memory Systems for Agents","extraction_method":"pdf-text-layer"},"checksum":"2d4aed13193584f302675ad239b7439c55445ec2cca581b3efb01d8c3fd9f1d4"} -->

## Slide 42 - Ngày 17: Memory Systems for Agents

Agentđãbiếtreasoning—nhưngtạisaonóquênhếtsaumỗi conversation?

- HoànthànhLab16: Reflexionagent+benchmark

- Đọc: Anthropic“BuildingEffectiveAgents”
AICB·Ngày16 41

---

<!-- chiron-source-span: {"source_span_id":"58932e15-05da-5776-aea7-d511941ea964","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Reflexion có phải luôn tốt hơn ReAct? Khi nào","extraction_method":"pdf-text-layer"},"checksum":"e9c460b65d0d642c29447b95980c50dd47428f9b49be79446efc5e20ebe75cf7"} -->

## Slide 43 - Reflexion có phải luôn tốt hơn ReAct? Khi nào

Q&A nên dùng cách nào? AICB·Ngày16 42

---

<!-- chiron-source-span: {"source_span_id":"e01b9647-c9ee-53d9-84d9-a3f1a3763cbb","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"2c70078449b6159fc0f4d5907af99c81e332d7654c401670899395bc53bd5fac"} -->

## Slide 44 - Cảm ơn!

AICB-P2T3·Ngày16·AdvancedAgentArchitectures github.com/vinuni-aicb Liênhệ: instructor@vinuni.edu.vn
