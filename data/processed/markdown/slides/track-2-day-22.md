---
schema_version: 1
course_id: rag-intensive
document_id: "d37320f5-e1db-58a7-bdb5-48b171a11405"
document_version_id: "04a184cf-4b90-5d6e-bd99-32a2f993f389"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "LLMOps & Prompt Versioning"
source_file: "track 2 - day 22.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 22.pdf"
source_sha256: "b3311fa62cb21ac19ee51b4b91479903a31859e6e6a9446737a9ab1687a9fae7"
parser_version: chiron-structured-markdown-v1
page_count: 75
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":75}"
language: vi
---

# LLMOps & Prompt Versioning

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"3575e3b8-2068-5169-a06a-87f26d4c3bcc","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"LLMOps & Prompt Versioning","extraction_method":"pdf-text-layer"},"checksum":"ebe06bc904e791fb5296c51f44b058a21c53baef2fea6b1cbc3496d27f0c7adb"} -->

## Slide 1 - LLMOps & Prompt Versioning

AICB-P2T2 · Ngày 22 · Chương 5: Vận Hành Giảngviên VinUniversity · Phase 2 · Track2· Tuần5

---

<!-- chiron-source-span: {"source_span_id":"d4aaae08-bb40-53c9-b137-44b6b7ae75a7","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"ac2525051cdfdaf28e0130460a978bf407072db1b2d472e3249667563de6ef7c"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Prompt thay đổi = behavior thay đổi. Bạn có đang version control prompts như code không? Case study: Team sửa một dòng trong system prompt — latency tăng 3x vì output dài hơn, cost tăng 200%. Không ai biết, vì prompt không có version, không có owner, không có rollback. Hôm nay ta biến prompt từ string literal thànhartifact có vòng đời.” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"3608084f-5946-51ed-b13b-2e646c2bad9e","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"0384068bb33ef0b1e69b38d81ee94b01fe95a26cf21f7e425b301e57cb49c77d"} -->

## Slide 3 - NộiDung Bài Học

1. MLOps →LLMOps: artifact đổi

2. Promptlà Artifact, không phải String

3. PromptRegistry: version &label

4. Git-nativevs Registry & rủi rovendor

5. Runtime: fetch mà khôngphụ thuộc cứng

6. Environments& Promotion

7. Testprompt trong CI: regression gate

8. Release: A/B & canarycho prompt

9. Rollback& Incident drill

10. ModelDeprecation Treadmill

11. PromptCaching: version LÀcache prefix

12. CostTracking& Attribution

13. Guardrailconfig như artifact

14. LLMOpsStack 2026

15. Đónggói bundle thành file

16. Phântầng context: luônnạp vs lười

17. Contrỏ có quản trị: tên & quyền

18. Demo,Lab & Tổng kết Giảngviên (VinUni) AICB· Ngày 22 Tuần5 1 / 52

---

<!-- chiron-source-span: {"source_span_id":"e2547415-f8f7-52e7-afba-a06cd032dff4","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"MụcTiêu","extraction_method":"pdf-text-layer"},"checksum":"412aaa3226db8d630f5b1ca1f01e6b76219c8c8240a34d1ce5ba58bfa8882af1"} -->

## Slide 4 - MụcTiêu

### Saubuổi học này,bạnsẽ

1. Môtả đượcđầyđủ mộtprompt artifact gồm những gì (khôngchỉ chuỗi text)

2. Viếtđượcfile artifact cho prompt của mình,vàphântầng contextđể không huỷ cacheoan

3. Thiếtkế promptregistry: immutable version+ movablelabel +rollback trongvài giây

4. Wiremột evalgate vàoCI để chặn prompt regression trướckhi merge

5. Sốngsót quamodeldeprecation màkhông phải viết lại prompt library

6. Đođược costper prompt versionvàper user — trước khi hoáđơn về Ranhgiới bài học Hômnayhọc vòngđời củaartifact. Cáchchấmđiểm chấtlượng →Day14. Cáchtrace/dashboard →Day13&23. Guardrails →Day11. CI/CDtổng quát →Day21. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 2 / 52

---

<!-- chiron-source-span: {"source_span_id":"b20d137e-4ba2-58e2-aa2f-3344f52c073e","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"6546ee0b2133f911472753885117b6af7578c1c75a6f60c8386be3f6cae400ea"} -->

## Slide 5 - DeliverableCuối Ngày

Artifactcần nộp Mộtpromptartifactcóversion,cóevalgatetrongCI,cólabel prodrollbackđược,và cóbáo cáo cost theo từng version

- Promptregistry (Langfuse hoặc LangSmith) với≥3versions + commit message rõràng

- CIjob chạy regression suite,failPR khiđiểm tụt quá ngưỡng

- Label prodtrỏversion đã pass; demo rollback<60giây

- Bảngcost/latency theoprompt version+cache hit rate
Ngưỡngchất lượng & cách chọnmetric: dùng lại khungDay 14 — hôm nay talo phần gate, không lo phầnchấm. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 3 / 52

---

<!-- chiron-source-span: {"source_span_id":"3e4c72d5-c486-5885-9069-2fad4b881de1","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Từ MLOps Đến LLMOps: Arti","extraction_method":"pdf-text-layer"},"checksum":"bfdc9b9cd29bb3d5ad7450464a380310e32af5df5d78d8e3807dbf167450f6f9"} -->

## Slide 6 - Từ MLOps Đến LLMOps: Arti

01 Từ MLOps Đến LLMOps: Arti- fact Đổi Thì Vòng Đời Đổi Khi artifact chính không còn là weights mà là prompt + context, mọi quy trình vận hành phải viết lại — không phải vì công cụ mới, mà vì thứ bạn version hoá đã khác

---

<!-- chiron-source-span: {"source_span_id":"f46fbdee-7fd3-57cd-8d8f-c9cd031addeb","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"MLOpsvs LLMOps: SoSánh","extraction_method":"pdf-text-layer"},"checksum":"ee6efe467669c6770598440a350b9de06cb9e0e525069b90a875211d5f97eaf7"} -->

## Slide 7 - MLOpsvs LLMOps: SoSánh

Khíacạnh MLOpstruyền thống LLMOps Artifactchính Modelweights + dataset Prompt + context + model pin (thườngkhôngtrain) Tracking Hyperparams,train/eval metrics Tracetừng LLM call, token cost Output Deterministic,reproducible Non-deterministic, chất lượng chủ quan Versioning Modelweights, data +Prompts,toolschema,modelsnap- shot Evaluation Accuracy,F1, AUC Faithfulness,relevance,hallucination Cost Train-heavy,inference rẻ Inference/token-heavy Drift Datadrift, concept drift + Prompt / embedding / model- versiondrift Điểmmấu chốt: MLOps sởhữu toàn bộ vòng đờihuấnluyện. LLMOps giả địnhđã có foundation model — việccủa bạn làquảntrị thứ bạn gửi vàomodel,chứ không phải trọng sốbên trong nó. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 4 / 52

---

<!-- chiron-source-span: {"source_span_id":"8c5c6159-032b-54f1-9955-145851bf44e7","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"ĐơnVị Vận Hành Mới: Compound AI System","extraction_method":"pdf-text-layer"},"checksum":"572c772986c7c69447f42f164fcfac0a5778120c6ca935402c42fc104d7d2b14"} -->

## Slide 8 - ĐơnVị Vận Hành Mới: Compound AI System

Hệthống >model BAIR (Zaharia et al., 02/2024): kết quả SOTA đến từ hệ thốngnhiều thành phần — nhiều lần gọi model + retriever+ tools — chứ khôngtừ một model đơn lẻ. Hệ quả vận hành: đơn vị để version hoá, để test, để rollbacklàcả pipeline,không phải một model. ∼60%ứng dụng LLM dùng mộtdạng RAG nào đó (số liệu BAIR2024). Câu hỏi tự kiểm — “Phiên bản hiện đangchạy trên production là gì?” Nếu câu trả lời chỉ là một git SHA củacode, bạn đang thiếu 80% thông tin: prompt nào, model snapshot nào, index version nào, tool schema nào. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 5 / 52

---

<!-- chiron-source-span: {"source_span_id":"f1d2a967-29ca-59be-a43a-2610b56200ab","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"BẫyNền Tảng: temperature=0 KhôngPhải Reproducible","extraction_method":"pdf-text-layer"},"checksum":"f627877aa570638e710f6e9a74f561ac1304b6a2c21871d74fa482d5aa6ad963"} -->

## Slide 9 - BẫyNền Tảng: temperature=0 KhôngPhải Reproducible

Lưu ý:Bẫy: temperature=0 không đảm bảo cùng output. Thay đổibatch size⇒ thứtựcộngfloating-pointđổi ⇒kếtquảkhác. Đâykhôngphảilỗiseed,vàbạnkhông “sửa”được từ phía application. Quy tắc Ops— Pin ngưỡng eval, đừng pin output. Gate trên “% pass ≥ X” kèm khoảng tin cậy — không gate trên so khớp chuỗi. Một test so sánh string bằng nhau sẽ đỏ ngẫu nhiên và team sẽ học cáchbỏ qua nó. Vìsao điều này thuộc Day22 Non-determinism là lý do prompt cầnversion chứ không chỉ cần diff. Bạn không thể chứng minh “promptmớitốthơn”bằngcáchchạymộtlần—bạn cần một artifact cố định để chạy lại nhiều lần trên cùngmột bộ dữ liệu. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 6 / 52

---

<!-- chiron-source-span: {"source_span_id":"50fa9a63-2b14-56d7-b7f5-bf21191fc987","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Prompt Là Artifact, Không Phải","extraction_method":"pdf-text-layer"},"checksum":"4619170ce1df1c481d91c3c30e4439bf60a7e02fa8769b9c1c74d7b2fd055696"} -->

## Slide 10 - Prompt Là Artifact, Không Phải

02 String Literal Nếu prompt của bạn là một chuỗi nằm trong ba file và một lời cầu nguyện, thì bạn không có hệ thống — bạn có một quả bom hẹn giờ

---

<!-- chiron-source-span: {"source_span_id":"b6e1282c-fa77-5902-ad25-8f377f1fb3a8","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"PhảnVí Dụ: “StringLiteral TrongBa File”","extraction_method":"pdf-text-layer"},"checksum":"95a474c4b5a5778af0e8bff267de702218e5f00ea6a03948e2e2b8932efa43dd"} -->

## Slide 11 - PhảnVí Dụ: “StringLiteral TrongBa File”

Lưuý: Câuchuyệncóthật: chiếnlược deploy cho prompt và model là“một stringliteralnằmtrongbafilevàmột hyvọng” —vàchỉbịpháthiệnkhinhà cung cấp thông báo khai tử model với thờihạn 60 ngày.

### Triệuchứng nhận biết trong codebasecủa bạn

- grepra3 bản copy hơi khácnhau của cùng một
systemprompt

- Khôngai biết bản nào đangchạy thật

- Sửaprompt = deploy lại toànbộ app

- Rollbackprompt = revert commit +chờ CI 20 phút
Bốncâu hỏi kiểm tra độtrưởng thành

1. Promptđang chạy trên prod cóIDkhông?

2. Aiđổi nólầncuối,và vì sao?

3. Rollbackmất bao lâu?

4. Versiontrước có cònchạyđược không? Câu4 là câu khó nhất— và là lý do có§10. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 7 / 52

---

<!-- chiron-source-span: {"source_span_id":"ab0bf6df-d538-550f-99d0-413566935284","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"MộtPrompt Artifact Thật Sự GồmNhững Gì","extraction_method":"pdf-text-layer"},"checksum":"9b171adcc3182e6c5229990632a1d45be3042b75c903079278ee3a0c6b33e753"} -->

## Slide 12 - MộtPrompt Artifact Thật Sự GồmNhững Gì

CONTEXTBUNDLE = đơn vị đượcversion hoá Systemprompt Few-shotexamples Tool/ function schema Outputschema ModelID + snapshot Decodingparams Retrievalconfig Guardrailconfig VersionID + owner Sailầm phổ biến nhất:versionhoá ôđầu tiênrồiđể tám ô còn lạitrôi tự do. Đổimodel snapshot mà không đổi version ID ⇒haihệ thống khác nhau mangcùng một cái tên. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 8 / 52

---

<!-- chiron-source-span: {"source_span_id":"7cf5934c-a043-514d-af09-cdd3fd2272cf","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"VìSao “Model ID” Phải NằmTrongArtifact","extraction_method":"pdf-text-layer"},"checksum":"eb5f98ae565c4a6c3adf180c5db4470b70315a847a589d1b666741b2443ca50b"} -->

## Slide 13 - VìSao “Model ID” Phải NằmTrongArtifact

Promptkhông tồn tại độc lập Mộtpromptđược tunechomộtmodelcụthể. Cùng chuỗitextđógửisangmodelkháclàmột thínghiệm chưatừng chạy,không phải “cùng một prompt”. Vì vậy cặp (prompt_version, model_snapshot) mớilàđơnvịcóýnghĩa—khôngphảiriêngcáinào. Hệquả trực tiếp—

- Kếtquả eval chỉ có giátrịtrênđúng cặpđó

- Rollbackprompt mà model đã bịkhai tử⇒
khôngrollback được

- Đổimodel ⇒mấttoàn bộ prompt cache
(§11) Bahệ quả này là basection riêng phía sau — chúngđều bắt nguồn từ đúng mộtquyết định thiết kế ở đây. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 9 / 52

---

<!-- chiron-source-span: {"source_span_id":"3669433b-da8d-53de-a9ec-226338ff0314","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Prompt Registry: Immutable Ver","extraction_method":"pdf-text-layer"},"checksum":"83c83a324262490b31f419e193624b6fa1f4e4907888586a6bc3a7a1ce767c7a"} -->

## Slide 14 - Prompt Registry: Immutable Ver

03 Prompt Registry: Immutable Ver- sion + Movable Label Một ý tưởng duy nhất giải quyết cả versioning lẫn rollback: bản ghi thì bất biến, còn cái tên “production” chỉ là một con trỏ

---

<!-- chiron-source-span: {"source_span_id":"4ea61b99-d002-5d5b-a0e2-3acc992d7d6c","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"MôHình Chuẩn: VersionBất Biến, Label Di Động","extraction_method":"pdf-text-layer"},"checksum":"a0208df137cec40419513c8498f3a21a604102bd8744f3483d1d993fb8c67900"} -->

## Slide 15 - MôHình Chuẩn: VersionBất Biến, Label Di Động

v1 a3f9c2 v2 7b1e04 v3 c8d5a1 v4 e2f770 append-only production staging rollback= dời con trỏ Mỗilần sửatạomột versionbấtbiến vớiID tự sinh.Label(production, staging)là contrỏ màSDK phân giải lúc fetch. Deploy= trỏ label sang versionmới.Rollback= trỏ ngược lại—không build lại, không deploylại code. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 10 / 52

---

<!-- chiron-source-span: {"source_span_id":"579fd5b2-56ce-501d-8e9c-5156cc1f33d9","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"HaiHiện Thực Phổ Biến","extraction_method":"pdf-text-layer"},"checksum":"e0bd011be97ad726679645f21d1e3155fa87dfc52ffbfdd3808fa628f845ff11"} -->

## Slide 16 - HaiHiện Thực Phổ Biến

LangSmithPrompt Hub—commit hash + tag

```text
from langsmith import Client
client = Client()
# Pin an exact version (commit hash)
prompt = client.pull_prompt(
"my-org/rag-system:c8d5a1")
```
# Or resolve through a tag prompt = client.pull_prompt( "my-org/rag-system:prod") # New version = new commit client.push_prompt( "my-org/rag-system", object=new_prompt_template) Langfuse(OSS) — label pointer

- Versionbất biến + autoversion ID

- Protectedlabels: chỉ admin đổiđược
production

- Versiondiff viewđểreview

- GitHubsync qua webhook→triggerCI
Lưuý: Promptđổi khôngcầndeployapp —đó là ưu điểm lớn nhấtvà là rủi ro quản trị lớn nhất. Xem§6. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 11/ 52

---

<!-- chiron-source-span: {"source_span_id":"2f3356b9-9f08-521a-8385-01b0b82bfb10","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"CommitMessage Cho Prompt: ViếtGì Mới Hữu Ích","extraction_method":"pdf-text-layer"},"checksum":"590fd59f9d32a9373d4ce06d0d5a9079527724453be5cc90e849f7eba2a33a86"} -->

## Slide 17 - CommitMessage Cho Prompt: ViếtGì Mới Hữu Ích

### Lưuý: Vôdụng
"update prompt" "fix" "try again" Sáu tháng sau không ai biết vì sao dòng đó tồn tại —và sẽ không ai dámxoá. Hữuích "Thêm ràng buộc JSON-only vì 3% output làm h￿ ng parser (ticket #4412). Eval: faithfulness 0.81→0.83, cost +4%." Khuônmẫu 3 phần— (1)Đổi gì—(2)Vì sao / bằng chứngnào—(3)Đánh đổi đo được. Promptlàcode,nhưngkháccodeởmộtđiểm: bạn khôngđọcrađược ýđịnhtừdiff. Mộtdòng“Answerconcisely.” khôngtự nói rằng nó tồntại để cắt 40% token cost. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 12 / 52

---

<!-- chiron-source-span: {"source_span_id":"361a576d-e4db-5ae3-bfcb-0e2fbd4eb7fc","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Git-native Hay Registry? Và Rủi","extraction_method":"pdf-text-layer"},"checksum":"e1dc4160727e913a01618bd0dde842052b620cd0212e602e8ffb5b8e9eb2e886"} -->

## Slide 18 - Git-native Hay Registry? Và Rủi

04 Ro Nhà Cung Cấp Không có lựa chọn đúng tuyệt đối — nhưng có một tiêu chí không được nhân nhượng: bạn phải xuất được dữ liệu ra

---

<!-- chiron-source-span: {"source_span_id":"47182ab6-c14b-5d4d-9147-8e540e7e7a42","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"MaTrậnQuyết Định","extraction_method":"pdf-text-layer"},"checksum":"5cb3d64dfbb39629a3058ac1dfa55fce2b8ed5d5852c70ba6ecb1e6b9b25eb4d"} -->

## Slide 19 - MaTrậnQuyết Định

Tiêuchí Git-native(YAMLtrong repo) Registry (SaaS/OSS) Reviewflow PRreview sẵn có, quen thuộc UIriêng, cần dạy lại team Aisửa được Chỉngười biết git PM/SMEsửa được Đổiprompt Cầndeploy lại app Khôngcần deploy Rollback Revert+ CI (phút) Dờilabel (giây) Audit Gitlog Auditlog + protected label Rủiro vendor Không Có— phải xuất được Phùhợp Monorepo,team engineer Teamđa vai trò, đổi nhanh Lựachọn thực tế phổ biếnnhất là lai:promptsốngtrongregistry để PM sửa nhanh,nhưng đượcsyncngược về gitquawebhook — git là bảnsao lưu và là nơiCI đọc. Bạn đượccả tốc độ lẫn khả năngthoát. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 13 / 52

---

<!-- chiron-source-span: {"source_span_id":"2766a0d7-c528-53f6-93af-c1911106a992","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"RủiRo Nhà Cung Cấp LàCó Thật","extraction_method":"pdf-text-layer"},"checksum":"118ea68afca9ca48314d59a3457d86e0e7eb22410202e7c1c60319a7220a38d3"} -->

## Slide 20 - RủiRo Nhà Cung Cấp LàCó Thật

Nềntảng Điềuđã xảy ra Đườngditrúdo chínhvendorđềxuất Humanloop Đóng cửa 08/09/2025 (Anthropicacqui-hiređội ngũ) W&BWeave OpenAIEvals Read-only 31/10/2026, tắt30/11/2026 Cookbook chính chủ: chuyển sang Promptfoo OpenAI Prompt Objects (/v1/prompts) Tắt30/11/2026 “Đưa nội dung prompt vào applica- tioncode” OpenAIAgent Builder Tắt30/11/2026 AgentsSDK / WorkspaceAgents Đọckỹdòngthứba—rồirútraquytắc — LờikhuyênditrúcủachínhOpenAIchoprompttrên platform là“đưa prompt vào code ứng dụng của bạn”— thừa nhận bởi đúng nhà cung cấp hưởng lợi nhất từ việckhoáchân. Suyra: mộtregistrybạnkhông exportđượcrafilephẳnglàmộttìnhhuốngcontin. Hãythử xuấtprompt+version+labelraJSON/YAMLvàdựnglạihệthống chỉtừfileđó. Nghịchlý: OpenAImuaPromptfoo (09/03/2026,vẫnOSS)rồichỉngườidùngEvalssangđó— côngcụOSSsốnglâuhơnnềntảnghosted (bảnđồ côngcụ: §14). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 14 / 52

---

<!-- chiron-source-span: {"source_span_id":"63d8789b-8490-5ba7-b5b7-6e807574e9bf","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Runtime: Fetch Prompt Mà","extraction_method":"pdf-text-layer"},"checksum":"c97efada2aa0ceee1bcbb39fc3a2f57d497475448b2b5244adc65342f0f90bb4"} -->

## Slide 21 - Runtime: Fetch Prompt Mà

05 Không Tạo Phụ Thuộc Cứng “Registry sập thì app sập” là một lỗi kiến trúc tự gây ra — và nó có lời giải chuẩn, chỉ vài dòng cấu hình

---

<!-- chiron-source-span: {"source_span_id":"7df66982-38bf-5467-906f-6aca715bf9de","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"VấnĐề: Một NetworkCall TrênĐường Đi CủaRequest","extraction_method":"pdf-text-layer"},"checksum":"5350a932c28833f2717baccf2223724981dd20fa49a4b578ae10cc29094a0e79"} -->

## Slide 22 - VấnĐề: Một NetworkCall TrênĐường Đi CủaRequest

NAIVE— registry nằm trên criticalpath Request Fetchprompt +80–300ms LLMcall Response registrysập ⇒appsập ĐÚNG— cache cục bộ +revalidate nền Request Localcache ∼0ms LLMcall Response Registry revalidatenền Giảngviên (VinUni) AICB· Ngày 22 Tuần5 15 / 52

---

<!-- chiron-source-span: {"source_span_id":"cd7e8398-5b09-5d70-af02-12fa05bfcf6f","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"BaLớp Phòng Vệ","extraction_method":"pdf-text-layer"},"checksum":"7d1aac229d3672583737643b47a1340c2ce1f51d4af3093682ebaa1574773e2f"} -->

## Slide 23 - BaLớp Phòng Vệ

# 1) Local cache (default 60s TTL) prompt = langfuse.get_prompt( "rag-system", cache_ttl_seconds=300) # 2) Fallback when cache is empty # AND registry is unreachable prompt = langfuse.get_prompt( "rag-system", fallback=BUILTIN_PROMPT) # 3) Pre-fetch at startup # -> first request never waits

```text
def on_startup():
langfuse.get_prompt("rag-system")
```
Cơchế

- TTLmặc định60giây

- HếtTTL: trảbản cũ ngay lập tức,revalidate
ởbackground (stale-while-revalidate)

- ⇒userkhôngbao giờchờnetwork

- cache_ttl_seconds=0 tắtcache—dùngởdev
đểluôn lấy bản mới nhất Đánh đổi cần nói rõ— TTL càng dài, prompt mới lan ra càng chậm. TTL= thời gian tối đađể một lầnrollbackcóhiệulựctoàncụm. ChọnTTLchínhlà chọnRTOcủa bạn. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 16 / 52

---

<!-- chiron-source-span: {"source_span_id":"30d9e609-ea63-55a1-bca0-8918ac64f023","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Environments, Promotion & Ai","extraction_method":"pdf-text-layer"},"checksum":"3f136210fa21d666d9720771e868ec323083c7ac45d03ca7b5f8743d8db63bd6"} -->

## Slide 24 - Environments, Promotion & Ai

06 Được Pushprod Khi prompt đổi được mà không cần deploy, con đường tới pro- duction vừa mất luôn mọi chốt kiểm soát mà code đang có

---

<!-- chiron-source-span: {"source_span_id":"61c9f407-87f9-511a-8fe3-f984ebbd94f5","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"ĐườngThăng Cấp Của Một Prompt","extraction_method":"pdf-text-layer"},"checksum":"8f182a3fb751f63cc8b3c18ce2206fab860e7397b92ff51f2006ea68ec49c1de"} -->

## Slide 25 - ĐườngThăng Cấp Của Một Prompt

dev cacheTTL = 0 eval gate staging shadowtraffic canary +review production protectedlabel rollback: dời label Dùngresourcetag (Environment: dev | prod )thay vì tách workspace riêng— để artifactdùngchung và thăng cấpđược giữacác môi trường.Committag quyếtđịnh version nào code đangtham chiếu. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 17 / 52

---

<!-- chiron-source-span: {"source_span_id":"dbde4a9a-499e-5da5-a946-5a76e7343d69","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"PromptSupply Chain: ChốtKiểm Soát Đã Biến Mất","extraction_method":"pdf-text-layer"},"checksum":"e6e1bde981e55cb1022362c8e26d5b65a9a47a9cb20b5af60b62884f3526a31d"} -->

## Slide 26 - PromptSupply Chain: ChốtKiểm Soát Đã Biến Mất

Lưu ý: Prompt đổikhông qua CI, không qua code review, không qua deploy. Nếuregistrychophépbấtkỳaidờilabel production,bạnvừatạoramộtđườngđẩy codethẳng lên prod mà không aigác. Kiểmsoát tối thiểu

- Protectedlabel: chỉ role đượccấp mới dời
production

- Bắtbuộc evalgate passtrướckhi dời

- Auditlog: ai, khi nào,version nào, lý do

- Cảnhbáo khi labelprodđổi
Câu hỏi diễn tập— “Một người vừa nghỉ việctuầntrước. Họcònquyềndờilabel production không?” Với code, offboarding đã có quy trình. Với prompt registry — thường là chưa. Đây là khoảng trống quảntrị mới mà LLMOps tạora. ChitiếtRBAC/IAM,phânquyềnvàtuânthủ: Day24. Ởđâytachỉchỉrarằngpromptregistrylàmộtbềmặtquyềnmớicần đượcđưa vào cùng khung. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 18 / 52

---

<!-- chiron-source-span: {"source_span_id":"6357b76f-f374-5825-87a6-f61ee54aff15","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Test Prompt Trong CI: Regres","extraction_method":"pdf-text-layer"},"checksum":"efce770586d2b0556115d768febe0912964f03892c20807b1e5e39a15a84731c"} -->

## Slide 27 - Test Prompt Trong CI: Regres

07 Test Prompt Trong CI: Regres- sion Gate Prompt là code, nên nó phải có test chạy tự động và chặn được merge — phần khó không phải chấm điểm, mà là nối dây

---

<!-- chiron-source-span: {"source_span_id":"03ca8315-e4ae-511e-a519-f3d12ce09cd4","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"EvalGate Nằm Ở Đâu TrongPipeline","extraction_method":"pdf-text-layer"},"checksum":"057f5dd3d14849d9b7cdd2365778235e7870a1aed6e7918e1d76771cb431a760"} -->

## Slide 28 - EvalGate Nằm Ở Đâu TrongPipeline

Sửaprompt MởPR Chạyeval trêngolden set Sovới baseline Merge pass fail ⇒chặnmerge +comment điểm số lên PR Điểmmấuchốt: gatechạytrên mọiPRchạmvàoprompt,model,hoặcretrievalconfig—khôngchỉPRchạmcode. Đólà lýdo prompt phải nằm ởnơi CI đọc được (git, hoặcregistry có webhook sync). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 19 / 52

---

<!-- chiron-source-span: {"source_span_id":"84c59ebf-d279-5f23-8f9b-bfa3a92440c9","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Promptfoo: Regression Suite KhaiBáo","extraction_method":"pdf-text-layer"},"checksum":"4dca34c62ce0028053606f42ff9019b6aa1029abb91b19fd4803915b28fc5f2e"} -->

## Slide 29 - Promptfoo: Regression Suite KhaiBáo

prompts: [file:// prompts/rag_v3.txt]

### providers
- openai:gpt-4o-mini
- anthropic:claude-sonnet-4-6

### tests
- vars: {question: "Refund policy?"}

### assert
- type: contains-json
- type: llm-rubric
value: "Answer grounded in context, no invented figures" - type: latency threshold: 2000 - type: cost threshold: 0.01 Vìsao chọn dạng khai báo

- Testlà data,không phải code→PM
reviewđược

- Chạynhiềuprovider cùnglúc →chuẩnbị
sẵncho §10

- GitHubAction failjob khitụt điểm và
commentdiff lênPR Bốicảnh: OpenAImua Promptfoo (09/03/2026); công cụvẫnopen source. DeepEval là lựachọn kiểupytest (assert_test,ngưỡng chặn deploy). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 20 / 52

---

<!-- chiron-source-span: {"source_span_id":"335c8d47-6eeb-50dd-84b7-8089b556dd2b","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"GoldenSet: Ít MàTinh","extraction_method":"pdf-text-layer"},"checksum":"1b9eb290f7e73acf8d67473370bd4954afca4372a955131817fdb41e48a27168"} -->

## Slide 30 - GoldenSet: Ít MàTinh

Côngthức 2026

- Bắtđầu ∼100case,tối đa ∼500

- Gánnhãn tay,tin được

- 3–5metric tươngquanvớihànhvisảnphẩm

- Bổsung từtraceproduction thật
Lưuý: Chấtlượng >sốlượng. Sinhhàngloạt case bằng LLM rồi không lọc= “AI slop”: suite to, chạy lâu, tốn tiền, vàkhôngphát hiện được regres- sionthật. Ranh giới với Day 14— Cách chọn metric, cách thiết kế benchmark, LLM-as-judge, độ tin cậy thống kê→ Day 14.Hôm nay ta chỉ quan tâm: bộ eval đó đượcgắn vào cổngnào, chặn được cái gì, và ai có quyềnbỏ qua nó. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 21 / 52

---

<!-- chiron-source-span: {"source_span_id":"9b03339d-842d-5877-930e-3f5d79e0e5a5","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Release: A/B & Canary Cho","extraction_method":"pdf-text-layer"},"checksum":"b1ff1d6828544d9e4c3da990a75941a687d8f6197691124ead617f7943cb6ccd"} -->

## Slide 31 - Release: A/B & Canary Cho

08 Prompt Version Eval offline nói prompt mới tốt hơn trên 100 case bạn tự chọn — production nói nó tốt hơn hay không trên phần còn lại của thế giới

---

<!-- chiron-source-span: {"source_span_id":"c26ac80a-2ecc-5f32-944a-955f2f09dadd","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"CơChế Định TuyếnTheoVersion","extraction_method":"pdf-text-layer"},"checksum":"8fe091a328abc11bdb153b04d3c5c40b69430972884a37c5ab7ebf707745f696"} -->

## Slide 32 - CơChế Định TuyếnTheoVersion

Router hash(user_id)— sticky prompt:c8d5a1 control— 90% prompt:e2f770 canary— 10% Mọitrace gắn tagprompt_version 90% 10% Sosánh quality · latency ·cost · cache hit ratetheo version Stickytheouser,khôngrandomtheorequest—nếukhông,cùngmộtngườisẽthấygiọngvănđổigiữachừngtrongmột hộithoại. Đây làkhác biệt so với A/B testmột nút bấm. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 22 / 52

---

<!-- chiron-source-span: {"source_span_id":"779db4af-5e62-570b-9fe8-896414556953","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"BaĐiều Kiện Để Con SốSo Sánh Có Nghĩa","extraction_method":"pdf-text-layer"},"checksum":"0d2689b3f69dff43c1c3927b69cc3c495f1f93d952ae84077cc017c962b13475"} -->

## Slide 33 - BaĐiều Kiện Để Con SốSo Sánh Có Nghĩa

1. Chỉđổi một biến.Đổiprompt vàmodelcùng lúc thì kết quảkhông quy được cho cái nào. Đâylà lý do model IDphải nằm trong artifact (§2).

2. Tagđủ chiều ngay từcall site.Thiếutag prompt_version trêntrace ⇒khôngthể tách số liệuvề sau. Dữliệu không tag được thìvĩnhviễn mất.

3. Đocả cost và latency,không chỉ chất lượng.Prompt“tốt hơn” mà dài gấpđôi có thể vẫn làmột bước lùi — đúngnhư case study mở đầu buổihọc. Ranhgiới — ToánhọccủaA/B (Welch’st-test,CUPED,SPRT,bandit)vàcác mẫushadow/canary →Day 23§14vàDay14. Hômnaytalophần nốidây: làmsaomộtrequestbiếtnóđangdùngversionnào,vàlàmsaosố liệuquay về đúng version đó. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 23 / 52

---

<!-- chiron-source-span: {"source_span_id":"84f61319-0ee8-5a58-b2ba-90915f72caab","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Rollback & Diễn Tập Sự Cố","extraction_method":"pdf-text-layer"},"checksum":"473809defea97846b3f7b9863f039180c872d09b67203fe9833b8aa549e944de"} -->

## Slide 34 - Rollback & Diễn Tập Sự Cố

09 Rollback không phải là một nút bấm — nó là một tính chất của hệ thống, và nó hỏng âm thầm nếu bạn không diễn tập

---

<!-- chiron-source-span: {"source_span_id":"46db7d96-698e-5a89-9890-bc24290c8f5c","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"RollbackNhanh — Nhưng Chỉ KhiBạn Đã Chuẩn Bị","extraction_method":"pdf-text-layer"},"checksum":"e01df416e92f8963a4b79d6c78a2c2e37f3daf6aa363c958c9505ee0a95d8f79"} -->

## Slide 35 - RollbackNhanh — Nhưng Chỉ KhiBạn Đã Chuẩn Bị

Điềukiện đủ để rollback được

1. Versioncũ còntồn tại(immutable,không bị ghiđè)

2. Modelsnapshot củanó còn phục vụ

3. Toolschema / output schema cũ còntương thíchvới code đang chạy

4. TTLcache đủ ngắn để labelmới lan ra kịp Lưu ý: Điều kiện(2) là cái hỏng thường xuyên nhất và ít ai kiểm tra. Prompt v2 của bạn vẫn nằm nguyêntrongregistry—nhưngmodelnóđượctune chođãbịkhaitửbathángtrước. Rollbackthấtbại đúnglúc bạn cần nó nhất. Thờigian rollback thực tế=thờigian dời label+TTL cache. Nếu TTL là300s, RTOcủa bạn là5 phút, không phải“tức thì”. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 24 / 52

---

<!-- chiron-source-span: {"source_span_id":"dd36b631-5aee-5d54-be63-abda0be8b99f","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"DiễnTập: Bốn Bước,Làm TrướcKhi Cần","extraction_method":"pdf-text-layer"},"checksum":"7ce97bf16c401c80cbd2aaf7b28b8ee0411f55cc2aa96e99bce98045499b58ff"} -->

## Slide 36 - DiễnTập: Bốn Bước,Làm TrướcKhi Cần

1. Pháthiện —alert nào sẽ kêu? (chất lượng tụt, cost vọt,JSON parse fail, cache hit raterơi về0)

2. Quytrách nhiệm—trace có tagprompt_version không? Bạn có biếtversion nào gây ra không?

3. Rollback—dời label. Bấmgiờ. So với consố bạntưởng.

4. Xácnhận —metric có thực sự trởlại mức cũ không? Nếu không, nguyên nhân không phải prompt. Bàitậptạichỗ — Đẩymộtpromptcốýtệlên staging,rồibấmgiờtoànbộbốnbước. Gầnnhưmọiteam lầnđầu làm việc này đềuphát hiện họ thiếu bước(2)—trace không đủ tag đểbiếtversionnào đanggây lỗi. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 25 / 52

---

<!-- chiron-source-span: {"source_span_id":"a432093a-f77b-567e-8d7b-ee28070ddd9d","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Model Deprecation Treadmill","extraction_method":"pdf-text-layer"},"checksum":"c545933fa8cb5a0fef263b244cb264cc1ec6dfea451fceb1d072715ad9b12880"} -->

## Slide 37 - Model Deprecation Treadmill

10 Model bạn đang chạy sẽ bị khai tử. Câu hỏi không phải “nếu” mà là “bạn phát hiện lúc nhận email, hay ba tháng trước đó”

---

<!-- chiron-source-span: {"source_span_id":"6c19e4c4-15b5-575e-bd2f-891544116f60","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"VìSao Đây Là ViệcCủaDay 22","extraction_method":"pdf-text-layer"},"checksum":"6868810d536f3fa1bab8388878966c67cd3d2483ce892024082aa553c977803b"} -->

## Slide 38 - VìSao Đây Là ViệcCủaDay 22

Bốicảnh Khai tử model từng là chuyện phiền mỗi năm một lần; 2026 nó là một mục thường trựctrên roadmap nền tảng. Thời hạn báo trước dao động từkhoảng một quýđến một năm. Lưu ý: Silent behavioral regression: trỏ sang snapshotmới,endpoint vẫntrả200,nhưngđịnhdạng tool-callđổi,độtuânthủJSONlỏngra,ranhgiớitừchối dịchchuyển. Khôngcó exception nào trong log. Trườnghợpđượcbáocáo — Một nhà cung cấp dịch vụ y tế buộc phải chuyển từ

### Gemini1.5 sang 2.5 Flash

- outputdài ∼5×sốtoken

- hạtầng parse JSONhỏnghoàn toàn

- >400giờ táithiết kế prompt library
Nguồnthứ cấp, không nêu têntổ chức — dùng như mộtgiai thoại minh hoạ,không phải số liệu chuẩn. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 26 / 52

---

<!-- chiron-source-span: {"source_span_id":"88e855f7-0293-58e9-a9bb-8c71c7e7ef36","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"KỷLuật Phòng Ngừa: Eval Trênn+1","extraction_method":"pdf-text-layer"},"checksum":"9d20f87c1e2f9d5318c195576ac5d1a65d88aee5680fb275ecf188885058cb9e"} -->

## Slide 39 - KỷLuật Phòng Ngừa: Eval Trênn+1

PROD model n—pinned nightly: modeln+1 nightly: modeln+2 Bảngchênh lệch quality· cost · format Khiemail khai tử đến, bạnđãbiếtcần sửa gì — vàmất bao lâu Nguyêntắc: mỗicall site production chạy bộeval của nókhôngchỉ trênmodel đang pin, màliêntục trên các ứng viên n+1. Chiphílàmộtjobnightlytrên ∼100case—rẻhơn400giờtáithiếtkế rấtnhiều. Đâycũnglàlýdobộtestở§7nên khaibáo nhiều provider ngay từđầu: hạ tầng sosánh chéo model đã sẵn sàngtrước khi bạn cần đến nó. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 27 / 52

---

<!-- chiron-source-span: {"source_span_id":"f798e2d4-e73e-5bee-816d-64c0a73402b5","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Prompt Caching: Version Của","extraction_method":"pdf-text-layer"},"checksum":"2fb5f06db03663d284bf1b2e311050d4d211bc1384209b29f166dc4d11c7d398"} -->

## Slide 40 - Prompt Caching: Version Của

11 Bạn LÀ Cache Prefix Prompt versioning và kinh tế học cache là cùng một bài toán — mỗi lần bạn sửa một chữ trong system prompt, bạn vứt đi toàn bộ cache phía sau nó

---

<!-- chiron-source-span: {"source_span_id":"f95cca70-3f17-527f-8e89-8133f27025d0","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"BấtBiến Duy Nhất Cần Nhớ","extraction_method":"pdf-text-layer"},"checksum":"fc1cb882e67862ab71044ea9a46493cb41ccfe7cca9db9d00fc685a450bba486"} -->

## Slide 41 - BấtBiến Duy Nhất Cần Nhớ

Nguyênlý — Promptcachinglàsokhớp tiền tố(prefixmatch). Bấtkỳthayđổi nàoở byte thứ N cũng huỷcache của mọi thứ từ Ntrở đi. tools system messages ổnđịnh nhất biếnđộng nhất thứtự render sửa1 byte ở đây⇒huỷtoàn bộ bên phải Vìthứ tự render làtools → system → messages,hãy đặt nội dungổnđịnh trước, biến động sau. Đây là mộtquyết định thiếtkế prompt,không phải một tuỳ chọncấu hình. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 28 / 52

---

<!-- chiron-source-span: {"source_span_id":"1d227e64-e17d-516b-b231-0555288aea65","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"KinhTế Học: ĐọcRẻ, Ghi Đắt","extraction_method":"pdf-text-layer"},"checksum":"cca55985a5febc7b37e95296c7e89697d9b4aa95b4a74c321037da4781158946"} -->

## Slide 42 - KinhTế Học: ĐọcRẻ, Ghi Đắt

Thaotác Giá(sovớiinputthường) Ghi chú Cacheread ∼0.1× CảAnthropic và OpenAI Cachewrite (5 phút) 1.25× Anthropic,TTL mặc định Cachewrite (1 giờ) 2× Anthropic,TTL mở rộng Điểmhoà vốn TTL5 phút: hoàvốn ở2request (1.25 + 0.1 = 1.35×sovới 2×nếukhông cache) TTL1 giờ: cần ≥3request (2 + 0.2 = 2.2×sovới 3×) Lưuý: Sốliệumultiplierởtrênlàcủa Anthropic. Mỗinhàcungcấpmộtkhác—OpenAIbậtcache tự động cho prompt ≥1.024 token, vòng đời 30 phút (GPT-5.6+), tối đa 24 giờ với extended retention. Luônkiểm tra pricing hiện hành. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 29 / 52

---

<!-- chiron-source-span: {"source_span_id":"cec84651-6f14-55e3-b80a-5cfb944cb1fb","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"NgưỡngTối Thiểu Không Tăng ĐềuTheo Đời Model","extraction_method":"pdf-text-layer"},"checksum":"b9b0c7d4bcaf4b32d6542b026c0215eec5d0b7973537a6708135ce2cca10e1c5"} -->

## Slide 43 - NgưỡngTối Thiểu Không Tăng ĐềuTheo Đời Model

Model(Anthropic) Prefixtối thiểu ClaudeOpus 5, Fable 5, Mythos5 512token Opus 4.8, Sonnet 5, Sonnet 4.6, Sonnet 4.5, Opus 4.1/4, Sonnet4 1.024token Opus4.7, Haiku 3.5 2.048token Opus4.6, Opus 4.5, Haiku 4.5 4.096token Lưu ý:Ngưỡng không đơn điệu theo thế hệ.Một prompt 3K tokencócache trên Opus 5 / Opus 4.8 / Sonnet 4.5, nhưngim lặng không cachetrên Opus 4.6 hay

### Haiku 4.5. Không có lỗi nào được ném ra — chỉ làcache_creation_input_tokens
0. ⇒Đổimodel cũngđổingưỡng cache. Mộtlần “tối ưu chi phí” bằngcách hạ cấp model có thểtắtcache hoàn toànvà làmchi phítăng. Tối đa4breakpoint mỗirequest. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 30 / 52

---

<!-- chiron-source-span: {"source_span_id":"67fdbbf2-d41e-5a00-b89e-c76b8a00a5fe","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"ThứBậc Huỷ Cache: Cái Gì Huỷ Cái Gì","extraction_method":"pdf-text-layer"},"checksum":"bea2e9e6e6c7d0e85cba030c6c245b247147e225cb9d3e8981325652cf19d4e7"} -->

## Slide 44 - ThứBậc Huỷ Cache: Cái Gì Huỷ Cái Gì

Thayđổi tools system messages Tooldefinitions (thêm/bớt/đổi thứ tự) huỷ huỷ huỷ Đổimodel huỷ huỷ huỷ Nộidung system prompt giữ huỷ huỷ tool_choice,images, bật/tắt thinking giữ giữ huỷ Nộidung message giữ giữ huỷ Nốingượcvề§10 — Đổimodelkhôngcó đường thoát— cache gắn theo model. Ngày bạn buộc phải migrate vì deprecation, bạn mấttoàn bộ cache cùng lúc: chi phí input tăng vọtđúng lúc bạn đangchữa cháy. Tintốt tool_choicevàbật/tắtthinking khôngphácache tools+system—đừnglolắngthừavềchúng. Chỉ tool definitionsvà model mới buộc dựng lại từ đầu. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 31 / 52

---

<!-- chiron-source-span: {"source_span_id":"62fd3406-d371-5bb4-a5aa-fd3775e1b386","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"SilentInvalidators: Danh SáchCần grep","extraction_method":"pdf-text-layer"},"checksum":"0ae852aecef347f69cbf1345926f66ca7d386b598d226098beb600c416708736"} -->

## Slide 45 - SilentInvalidators: Danh SáchCần grep

# BAD: prefix changes EVERY request system = f "Today: {datetime.now()}" # BAD: ID early in the content system = f "[req {uuid4()}] You are..." # BAD: non-deterministic dump system = json.dumps(cfg) # missing # sort_keys= True # BAD: per-user prefix system = f "User: {user.name}..." # BAD: each flag combo = new prefix if beta: system += EXTRA_RULES # BAD: tool set varies per user tools = build_tools(user) Cáchkiểm chứng Đọc usage.cache_read_input_tokens. Nếunó bằng0 quanhiềurequestcócùngprefix ⇒có mộtsilent invalidator. Bẫy đọc số: input_tokens chỉ làphần chưa cache. Tổng prompt = input_tokens + cache_creation + cache_read. Cách sửa — Chuyển phần động ra sau breakpoint cuối, làm nó xác định (sort keys), hoặcxoá nếu không thực sựcần. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 32 / 52

---

<!-- chiron-source-span: {"source_span_id":"ee97d31e-d67c-5f04-b7fa-b1b29f14c773","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"HaiCái Bẫy Ít Người Biết","extraction_method":"pdf-text-layer"},"checksum":"9378ef6e8b3de4a5f576f29d2826e17962bb80040a2486cd7bf268da33fcd03a"} -->

## Slide 46 - HaiCái Bẫy Ít Người Biết

Cửasổ nhìn lại 20 block Mỗi breakpoint chỉ dò ngượctối đa 20 content blockđểtìmcachecũ. Mộtlượtagentcónhiềucặp tool_use/tool_result dễ vượt 20 block⇒request kếtiếp misstrong im lặng. Sửa: đặtbreakpointtrunggianmỗi ∼15blocktrong cáclượt dài. Requestsong song Mộtcacheentrychỉ đọcđược saukhiresponseđầu tiênbắtđầustream. BắnNrequestgiốnghệtnhau cùnglúc ⇒cảN đều trả giá đầyđủ. Sửa (fan-out): gửi 1 request, chờ token đầu tiên, rồimới bắn N−1cái còn lại. Lưu ý:Kết luận của cả section:một chỉnh sửa “vô hại” về câu chữ trong system prompt là mộtsự kiện chi phí gấp∼10 lầncho tới khi cache đầy lại. Hãygộp các thay đổi prompt thành lô, đừng rải rác cả ngày — và đừng bao giờ nhét timestamp vàosystem prompt. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 33 / 52

---

<!-- chiron-source-span: {"source_span_id":"79582aa2-c536-5c1e-83b3-9c13c50a8ff0","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Cost Tracking & Attribution","extraction_method":"pdf-text-layer"},"checksum":"2a79f47e763b0bf33fb887522317bd54dc03cedaaad3d1169a7c49a34e090dcb"} -->

## Slide 47 - Cost Tracking & Attribution

12 Câu hỏi “vì sao hoá đơn tháng này gấp đôi” chỉ trả lời được nếu bạn đã gắn tag từ trước — dữ liệu không tag được thì mất vĩnh viễn

---

<!-- chiron-source-span: {"source_span_id":"b20bc844-9298-59b0-89a0-616f10a2a179","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"GắnTagTại Call Site: ViệcCó ĐònBẩy Cao Nhất","extraction_method":"pdf-text-layer"},"checksum":"ed1ceee396fbbb7c3cd1429fce75d6df6f0a342bcaef5c239147f51552c7761b"} -->

## Slide 48 - GắnTagTại Call Site: ViệcCó ĐònBẩy Cao Nhất

App +metadata Gateway virtualkey,budget LLMprovider Spanclose gen_ai.usage prompt_version· user · tenant ·feature · agent_run Chiphí tính lúc đóng span,theo bảng giá có version Gatewaynằm gần request nhất—nó gắn tag vàcưỡngchế ngânsách theo thời gian thực,tạo dữ liệu attribution sạch ngaytại biên,trước khi chi phí kịpchạm dashboard. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 34 / 52

---

<!-- chiron-source-span: {"source_span_id":"c14abf99-5b17-5164-830e-963f83165e7e","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"BốnQuy Tắc Vận Hành","extraction_method":"pdf-text-layer"},"checksum":"d6bdfd1ea60a0bf05b1ea2d451ae9af77ecb52a4993f8a068d181cce6fed7566"} -->

## Slide 49 - BốnQuy Tắc Vận Hành

1. Gắnmetadata ở mọicallsite — ngay hôm nay.Header/fieldmetadata là bước có đòn bẩycao nhất vàtươngthích tiến: dữ liệu bắtđầu tích luỹ trên trace từđúng thời điểm bạn bậtnó. Không thểtruy hồi cho quá khứ.

2. Sosánh cost/request và token deltatheopromptVersion trongcùng một cửa sổ thời gian. Đâychính là thứ phát hiệncase study mở đầu buổi học—trướckhihoá đơn về.

3. Chặntrước, tối ưu sau.Đặthard cap và throttle theouser/tenant trước; tối ưu prompt sau. Mộtuser vượt ngân sách ngàyphải bị chặn, không phải bịghi nhận.

4. Bảnggiáphảicóversion. Giáthayđổitheothờigian;dữliệulịchsử khôngđược địnhgiá lạitheo bảng giá hôm nay,nếu không mọi so sánhtheo thời gian đều sai. Chiphí tầng GPU (MFU/MBU, kinhtế học instance)→Day25. Dashboard vàalerting →Day13 & 23. Ở đây chỉ làquy nguyên nhân về đúng artifact. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 35 / 52

---

<!-- chiron-source-span: {"source_span_id":"e63de442-3f43-5bca-8d77-c8306b7743ff","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"ThêmMột Chiều Bắt Buộc: Cache Hit Rate","extraction_method":"pdf-text-layer"},"checksum":"48101418e7d85cc44e8374c0378fbcc4342ca9456eaa0ffd69451649cc513c70"} -->

## Slide 50 - ThêmMột Chiều Bắt Buộc: Cache Hit Rate

Vìsao phải đo cùng nhau Costperrequesttăngcóthể khôngphảivìpromptdài hơn, mà vìcache hit rate rơi. Hai nguyên nhân này

### cầnhai cách chữa hoàn toànkhác nhau

- promptdài hơn →sửanội dung

- hitrate rơi →tìmsilent invalidator (§11)
Khôngtách được hai cái thìbạn sẽ tối ưu nhầm chỗ. Bảngtối thiểu theo version—

- cost/ request

- tokenin / out

- cacheread%

- latencyP50 / P95

- điểmchất lượng
Nămcộtnày,cắt theo prompt_version,trảlời đượcgần nhưmọi câu hỏi vận hànhcủa một LLM app. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 36 / 52

---

<!-- chiron-source-span: {"source_span_id":"21582806-3d6f-5ef0-b7e9-6153bd7c405e","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"Guardrail Config Cũng Là Một","extraction_method":"pdf-text-layer"},"checksum":"dd2c47adaf3eedfbe078dcd7d7601a086edc0b6730f285f7c760824714b414aa"} -->

## Slide 51 - Guardrail Config Cũng Là Một

13 Artifact Có Version Guardrail là một phần của context bundle — nới một ngưỡng cũng là một thay đổi hành vi cần review, cần eval, cần rollback

---

<!-- chiron-source-span: {"source_span_id":"8adc1194-2b0d-5008-a608-79826662a25a","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"GócNhìn Day 22 Về Guardrails","extraction_method":"pdf-text-layer"},"checksum":"d2ba3c3991e17220d19ce6cdccb03eb2b44cb3bfb690587d79db3878da761be1"} -->

## Slide 52 - GócNhìn Day 22 Về Guardrails

Guardrailconfig phải đi cùng prompt Ngưỡng toxicity, danh sách PII entity, schema JSON bắt buộc, hành vion_fail — tất cả đều làtham số quyếtđịnhhànhvi. Chúngthuộcvềcùngmộtversion vớiprompt. Táchrờichúng ⇒promptv3chạyvớiguardrailconfig củav1, và không ai biết. Lưu ý: Nới một ngưỡng từ 0.7 xuống 0.5 không phải “chỉnh cấu hình” — đó là mộtthay đổi hành vi an toàn, phải qua đúng cổng như một thay đổi prompt: review, eval, audit log, roll- backđược. Ranh giới rõ ràng với Day 11— Day 11(20 section) sở hữu toàn bộ nội dung guardrails: attack vector, prompt injection, jailbreak, defense in depth, tooling, red-teaming, HITL.Day 24sở hữu PII, RBAC và tuân thủ. Day22chỉbổsungđúngmộtđiều: nhữngcấuhìnhđólàartifact—vàphảiđượcversionhoá,thăngcấp,rollback theocùng một vòng đời vớiprompt. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 37 / 52

---

<!-- chiron-source-span: {"source_span_id":"d17e63db-ddcc-5ea9-b6a6-9af3a519bf5d","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"Defensein Depth — Nhắc LạiMột Slide","extraction_method":"pdf-text-layer"},"checksum":"7b4907d74c823c8a0c07eba73d3eff56781b3fd4abd22244bc30cda6f72cc540"} -->

## Slide 53 - Defensein Depth — Nhắc LạiMột Slide

User Input InputGuards PII,injection, jailbreak LLM modelpin từ contextbundle OutputGuards toxicity,format, factualgrounding Safe Response Block Reask/Block Cảnăm hộp trên đều nằmtrong context bundle của §2.Đổibất kỳ hộp nào màkhông tăng version⇒bạncó một hệ thốngkhác mang cùng một cáitên.Cơchế củatừng hộp: Day11. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 38 / 52

---

<!-- chiron-source-span: {"source_span_id":"1d4d7514-5e60-507b-b432-d902f5680485","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"LLMOps Stack 2026","extraction_method":"pdf-text-layer"},"checksum":"5f373a2c9c8235d73fde838bec09def1459e4d27752c842563db336eb078ccd1"} -->

## Slide 54 - LLMOps Stack 2026

14 Bản đồ công cụ — chọn theo ràng buộc của bạn, không theo độ nổi tiếng

---

<!-- chiron-source-span: {"source_span_id":"a8710869-4d8e-5efc-beca-e836588b5265","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"NămTầng Của Stack","extraction_method":"pdf-text-layer"},"checksum":"6aee54778c3b5cb017a9fe67c009f98eb12a6d76d8c2e4822c26b6c05d6ff771"} -->

## Slide 55 - NămTầng Của Stack

Safety— Guardrails AI, Llama Guard,NeMo Guardrails(Day 11) Evaluation— Promptfoo, DeepEval, Ragas(Day 14) Tracing— LangSmith, Langfuse, W&BWeave,Phoenix (Day 13, 23) PromptManagement — Langfuse, LangSmith Hub,MLflow Prompt Registry,Agenta, YAML+Git Gateway& Cost — Portkey,Helicone, OpenMeter(Day 23, 25) Tầngđược khoanh đỏ là phầnDay 22 sở hữu.Bốntầng còn lại được dạyở các ngày khác — ởđây chỉ để bạn thấy promptmanagement ngồiở đâutrongbức tranh, và nó chạmvào cái gì. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 39 / 52

---

<!-- chiron-source-span: {"source_span_id":"b377f4b6-224d-532d-96a6-7ea04361cbc6","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"ChọnCông Cụ Theo Ràng Buộc","extraction_method":"pdf-text-layer"},"checksum":"ac06220b2b0260abfbcbd90cbe9dc86422553c53e2bb6aefae6b4fe7d31e9df3"} -->

## Slide 56 - ChọnCông Cụ Theo Ràng Buộc

Ràngbuộc của bạn Hướngchọn Khôngđược để dữ liệu rangoài Langfuseself-host, hoặc YAMLtronggit PM/SMEphải sửa được prompt Registrycó UI: Langfuse, Agenta, PromptLayer Đãdùng LangChain sẵn LangSmith(tracing + Prompt Hub liềnmạch) Muốngiấy phép rộng nhất Agenta(MIT) Ưutiên regression suite trong CI Promptfoo(YAML+ GitHub Action) Đãdùng Databricks / lakehouse MLflowPrompt RegistrytrongUnity Catalog Sợvendor biến mất Bấtkỳ lựa chọn nào —miễn làexportđược Lờikhuyênduynhấtkhôngphụthuộccôngcụ — Bắtđầubằng git+mộtfileYAML+một suite promptfoo. Nó giải quyết 80% nhu cầu, không tốn tiền, không có rủi ro vendor, và dạy team đúng thói quen. Chuyển sang registrykhibạn có nhu cầu cụ thể: người không biết git cần sửa prompt, hoặc cần rollback trong vài giây. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 40 / 52

---

<!-- chiron-source-span: {"source_span_id":"7251396c-e08e-510a-ace4-2e4015b7b4c6","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"Đóng Gói Context Bundle Thành","extraction_method":"pdf-text-layer"},"checksum":"b6bb9983d2982110dc68268339b6a4b01217007e272107d7c46d66d81edd3cb9"} -->

## Slide 57 - Đóng Gói Context Bundle Thành

15 File Sơ đồ chín ô ở §2 chỉ có ích khi nó trở thành một file thật — và ba nhà cung cấp frontier đã hội tụ về gần như cùng một tập trường

---

<!-- chiron-source-span: {"source_span_id":"c5104a45-85b5-5365-89b4-b688cb969658","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"BaCách Lưu, Gần Như MộtTập Trường","extraction_method":"pdf-text-layer"},"checksum":"f7eaf9da3475ce83f943c1d15ed4450275fdf34e82a0c740cf869b3cece7f367"} -->

## Slide 58 - BaCách Lưu, Gần Như MộtTập Trường

Trườngcần lưu ClaudeCode SKILL.md MLflow Prompt Registry YAMLtronggit

### Nộidung chỉ dẫn Thânfile Markdown template Khối prompt
Địnhdanh name catalog.schema.name Đườngdẫn file

### Khinào dùng description — description

### Modelpin model Tag model

### Toolschema allowed-tools — tools
Lýdo thay đổi Commit message của git commit_message Commit message củagit Phiênbản GitSHA Sốtự tăng GitSHA Contrỏ deploy Branch/ tag alias Branch/ tag Ô—khôngphảilời khẳng định rằng sảnphẩm thiếu tính năng; nó chỉcó nghĩa là tài liệu khôngmô tả mộtchỗdành riêng chotrường đó, nên bạn phảitự chọn nơi lưu. Và đó chính là điểm cầnthấy:mộttrường không có chỗ lưuthì không biếnmất — nó chuyển thànhtri thức ngầm trong đầu mộtngười.Vìsao không có cột OpenAI:lựa chọn “sống trong platform” đãbị tắt 30/11/2026,và đường di trú dochính OpenAI đề xuất là “đưanội dung prompt vào application code”— tức là đúng cột thứtư (§4). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 41 / 52

---

<!-- chiron-source-span: {"source_span_id":"54e7538e-3547-50d0-862f-9e5afa9bd783","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"ĐọcMột Artifact File Thật: Từng TrườngLàm Gì","extraction_method":"pdf-text-layer"},"checksum":"9b0111c96bc20a7c02fe4e2de79573733d4fc6de0c7fe7e1216f9f89bd089eb2"} -->

## Slide 59 - ĐọcMột Artifact File Thật: Từng TrườngLàm Gì

--- name: deploy-check description: Pre-deploy checks. Use when the user asks about a release or a rollout. model: claude-opus-5 # model pin effort: high allowed-tools: Read Grep Bash disallowed-tools: WebFetch paths: services/** # when to # activate license: Apache-2.0 compatibility: needs kubectl --- Instruction body goes here... Đốichiếu với §2

- model →modelpin

- allowed-tools →toolschema

- paths →điềukiện kích hoạt

- description →khinào dùng

- license, compatibility →metadatađể
mangđi nơi khác Điểm cần thấy — Đây không phải “một file prompt”. Đây là context bundle của §2 dưới dạngmộtđịnhdạngfile —vànónằmtronggit, nên nó thừa hưởng miễn phí review, version và rollbackcủa git. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 42 / 52

---

<!-- chiron-source-span: {"source_span_id":"a0fe8d21-a011-5e67-89b8-8dc3fde11bb7","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"TựThiết Kế: TậpTrườngTối Thiểu Của Bạn","extraction_method":"pdf-text-layer"},"checksum":"1a5af3902ac6ecc2a1312270f430b5cad20efe7bd2220f43548010cdc5f1b71d"} -->

## Slide 60 - TựThiết Kế: TậpTrườngTối Thiểu Của Bạn

# prompts/support-triage.yaml name: support-triage version: 7 # immutable description: Route a ticket to the right queue. model: claude-sonnet-5 # pin temperature: 0 tools: [lookup_order] output_schema: schemas/triage.json guardrails: guards/pii-strict.yaml

### retrieval
index: kb-2026-08 top_k: 3 owner: platform-team commit_message: >

### Add queue "billing-dispute"
6% fell through to catch-all (ticket 4412). Eval 0.88 -> 0.91. Chínô, mười mấy dòng YAML Đọc ngược lại sơ đồ §2: nếu một ôkhông có dòng tương ứng ở đây, hãy hỏi“nó đang nằm ởđâu?” —câutrảlờigầnnhưluônlà“rảitrong code”. Batrường hay bị bỏ quênnhất—

- model—thiếu nó thì kết quảeval vô
nghĩa(§2)

- retrieval.index —đổi index là đổi hệ
thống

- guardrails —xem §13
Filenày chính làđầuvào của Lab 22: thứ bạn push lênregistry ở bước 1. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 43 / 52

---

<!-- chiron-source-span: {"source_span_id":"3fb9cebc-7866-50d4-9f71-26cbd6989c24","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"Phân Tầng Context: Luôn Nạp","extraction_method":"pdf-text-layer"},"checksum":"e01a52be973c30c4de5abc038ac9fe249168bf6fda58a13d918608203838a4ea"} -->

## Slide 61 - Phân Tầng Context: Luôn Nạp

16 vs Nạp Lười Không phải thứ gì trong bundle cũng đáng nằm trong mọi re- quest — và tầng bạn chọn quyết định luôn cả hoá đơn cache ở §11

---

<!-- chiron-source-span: {"source_span_id":"88eeb086-7e7e-513d-99bb-87836aeb4fb6","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"HaiTầng, Hai Hoá Đơn RấtKhác Nhau","extraction_method":"pdf-text-layer"},"checksum":"3ff63c4026d999f1af36c66e7b9cf528a3e686077653e2da9e82533fdf3c4f9a"} -->

## Slide 62 - HaiTầng, Hai Hoá Đơn RấtKhác Nhau

TẦNG1 — LUÔN NẠP ·mọi request đều trả tiền ·nằm ở ĐẦU cache prefix Systemprompt Facts/ memory Toolschema TẦNG2 — NẠP KHI CẦN· chỉ request liên quan mớitrả tiền Procedures Tàiliệu tham khảo Few-shottheo loại Quytắc phân loại: fact(luônđúng, luôn liên quan)→tầng1. Procedure(chỉđúng trong một loại việc)→tầng2. ClaudeCode hiện thực đúng haitầng này bằngCLAUDE.md (luônnạp) và thânSKILL.md (nạplười) — nhưng phép chiathì ápcho mọiLLMapp. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 44 / 52

---

<!-- chiron-source-span: {"source_span_id":"244aeb63-a567-5c2d-a609-82bc90fdfe3e","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"KinhTế Học Của ViệcNạpLười","extraction_method":"pdf-text-layer"},"checksum":"3733ea818b6ee26c87c4854c45c0de1be4a1eff92e4d97bfc1fc1b18c92b07a6"} -->

## Slide 63 - KinhTế Học Của ViệcNạpLười

Nguyêntắc thiết kế Tài liệu Claude Code nói thẳng:“phần thân của một skill chỉ được nạp khi nó được dùng, nên tài liệu tham khảodàigầnnhưkhôngtốngìchotớilúcbạncầnđến.” Ngaycả phầnmôtả cũngbịgiớihạn 1.536kýtự trong danhsáchskill—tàiliệughirõlýdolà “đểgiảmdùng context”. Áp dụng ngoài Claude Code—

### Cùngphép tính đó cho appcủa bạn

- Few-shotdài →nạptheo loạitruyvấn

- Toolschema →chỉnạp tool thật sự dùng
được

- Chínhsách / quy trình→đưavào
retrieval,đừng nhét hết vào system prompt Lưuý: Nốithẳngvề§11: contextluôn-nạpnằmở đầuprefix. Sửamộtdòngởtầng 1 ⇒ đổi prefix⇒ huỷ cache của mọi thứ phía sau. Nội dung tầng 2 không gây ra điều đó.Phân tầng không chỉ tiết kiệm token — nó quyết định cache của bạn ổnđịnh đến đâu. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 45 / 52

---

<!-- chiron-source-span: {"source_span_id":"93096ea6-48e1-5c6f-ad6a-159a4eb5c891","locator":{"kind":"page","page":64,"label":"Slide 64","section_title":"Con Trỏ Có Quản Trị: Từ Tên","extraction_method":"pdf-text-layer"},"checksum":"14b00a6fcadef11d39fbbb5b393ce1976701d0375c79081ec5d0b82d2703d116"} -->

## Slide 64 - Con Trỏ Có Quản Trị: Từ Tên

17 Gọi Đến Quyền §3 nói label là một con trỏ, §6 nói con trỏ đó phải có người gác — phần này là cách hiện thực cả hai bằng đúng một hệ định danh

---

<!-- chiron-source-span: {"source_span_id":"fd2c9e79-34e2-5b16-8256-10aca3f9a77b","locator":{"kind":"page","page":65,"label":"Slide 65","section_title":"ĐặtTên Trước,Phân QuyềnSau","extraction_method":"pdf-text-layer"},"checksum":"0da20c775e8a4c7ca2e1677f814930aacd012830dd67245247d5300dc21827ed"} -->

## Slide 65 - ĐặtTên Trước,Phân QuyềnSau

Kháiniệm HiệnthựctrongMLflowPromptRegistry Tương ứng §3 Prompt Named entity, định danh ba cấp catalog.schema.name Promptrepo Version Immutablesnapshot,số tự tăng Versionbất biến Alias Mutable pointer tới một version (production, staging) Labeldi động Tag Key–valuegắn theo từng version Metadataversion Vì sao “định danh ba cấp” mới là điểm đáng học— catalog.schema.name không phải là “têndàihơn”. Nóđặtpromptvào cùngkhônggiantênvớitablevàmodel —nêncâuhỏi“aiđượcsửacáinày?” đượctrả lời bằng hạ tầngquyềnđãcó,chứ không phải một hệquyền thứ hai dựng riêng choprompt. Tàiliệu nói thẳng về tínhbất biến: “một khiversion đã được tạo, template, commitmessage ban đầu và metadata củanó khôngthể sửa.” Đâychính xác là mô hình §3,đóng gói thành sản phẩm doanhnghiệp. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 46 / 52

---

<!-- chiron-source-span: {"source_span_id":"1f554a2e-b0a2-50b8-9387-c73314eacac3","locator":{"kind":"page","page":66,"label":"Slide 66","section_title":"PhânGiải Con Trỏ: Code Không Bao Giờ ChứaSố Version","extraction_method":"pdf-text-layer"},"checksum":"fce0ca4c9efebf8e5130677daaddac43242ed009f157a5edcb89a4d849397a94"} -->

## Slide 66 - PhânGiải Con Trỏ: Code Không Bao Giờ ChứaSố Version

```text
import mlflow
# 1) Register -> immutable version
mlflow.genai.register_prompt(
name= "main.genai.support_prompt",
template= "Answer: {{question}}",
commit_message= "Initial support prompt")
# 2) Load by alias (no version no.)
p = mlflow.genai.load_prompt(
"prompts:/main.genai.support_prompt@production")
# 3) Deploy / rollback = move alias
mlflow.genai.set_prompt_alias(
name= "main.genai.support_prompt",
alias= "production",
version=2)
```
Badạng URI prompts:/name@latest prompts:/name/3 prompts:/name@production Kỷ luật cần nhớ— Chỉ dạngthứ bađược xuấthiệntrongcodeproduction. Haidạngkia dành cho debug và cho eval — nơi bạncố ý ghimmột version. Langfusehiện thực cùng ý tưởngbằnglabel= ; LangSmithbằng:tag. Cú pháp khácnhau,kỷluật giốnghệt nhau. Chúý: biến trongtemplate MLflow dùng ngoặc kép {{question}}. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 47 / 52

---

<!-- chiron-source-span: {"source_span_id":"1c9047cd-5283-560b-a488-3829c4424dd4","locator":{"kind":"page","page":67,"label":"Slide 67","section_title":"QuyềnLà Quyền Của Bề MặtBạn Đã Có","extraction_method":"pdf-text-layer"},"checksum":"92b2d5c027954775631c41a59ff2743fde0dca34fdb798518de430b53ed19ff5"} -->

## Slide 67 - QuyềnLà Quyền Của Bề MặtBạn Đã Có

Táisử dụng, đừng dựng cáithứ hai Để tạo/xem prompt, bạn cần một Unity Catalog schemavớiquyền CREATE FUNCTION, EXECUTE, MANAGE. Nghĩa là câu hỏi “ai được push lênprod?” (§6) trở thành mộtcatalog grant— cùng bề mặt phân quyền vớitable, model và feature. VìsaoTrack2nênchúý — Prompt trở thành một object có quản trị trong lake- housecatalog,nằmcạnhtablevàmodel—đúng tinhthần catalog-as-control-planecủaDay18. Bạn không phải dựng hệ quyền thứ hai cho prompt. Bạndùnglạicáiđãcó—kểcảquytrình offboardingmà§6 đã chỉ ra làhay thiếu. Đánhđổi: bạnbị buộc vào hệ sinhthái Databricks/Unity Catalog. Nhưngnếu tổ chức đã ở đó(Day 17–19), đây là con đườngít ma sát nhất đểprompt có audit trail cấp doanhnghiệp mà không phải tự xây.Nguyêntắc mang đi được:chọn bềmặt phân quyền mà tổchức bạnđãvậnhành tốt. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 48 / 52

---

<!-- chiron-source-span: {"source_span_id":"23fc6d03-6576-5655-aba1-7dd763b06e41","locator":{"kind":"page","page":68,"label":"Slide 68","section_title":"BaNơi Artifact Có Thể Sống","extraction_method":"pdf-text-layer"},"checksum":"e23bbf5ff7f6b7a9774c99d2f4257df2d4d483d60efb018fe638fd4f5f1c5bb3"} -->

## Slide 68 - BaNơi Artifact Có Thể Sống

Artifact sống ở đâu Vídụ Exportđược? Contrỏ dời được? Trongrepo ClaudeCode (.claude/) Có— là git Có— git revert Trongcatalog MLflow Prompt Registry +UC Có— API + UC Có— alias Trongplatform OpenAIPrompt Objects Khôngbền Đãtắt Bàikiểmtrahaicâuhỏi—chạynó trướckhicamkết — (1)Artifactcó exportđượcra file phẳng không? (2) Con trỏ códờiđược không?Claude Code có cả hai miễn phí nhờ git. Databricks cho cả hai cộng thêm ACL của catalog. Bản hosted của OpenAI không giữ được cái nào một cách bền vững — và đã bị khaitử (§4). Balựa chọn đều hợp lệ. Hãy chọn theo ràngbuộc của bạn (§14) — nhưngđừng chọn cái trượt bài kiểmtra hai câu hỏi trên. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 49 / 52

---

<!-- chiron-source-span: {"source_span_id":"664475e6-de8b-58ff-a633-47bb602634cd","locator":{"kind":"page","page":69,"label":"Slide 69","section_title":"Demo, Lab & Tổng Kết","extraction_method":"pdf-text-layer"},"checksum":"744d919b30c9b71ad801217bf6127c05c2918fac8bb4cb7ccb602aea8e9e0cd1"} -->

## Slide 69 - Demo, Lab & Tổng Kết

18 Mục tiêu cuối: một prompt artifact có version, có cổng chặn, roll- back được, và biết nó tốn bao nhiêu

---

<!-- chiron-source-span: {"source_span_id":"6777da8a-ec24-5ae1-82a5-aa6606e61c1a","locator":{"kind":"page","page":70,"label":"Slide 70","section_title":"LiveDemo: Vòng ĐờiĐầy Đủ Của Một Prompt Version","extraction_method":"pdf-text-layer"},"checksum":"b7fd2e4e4823d190f35087def9d30ccc9033234d2536541f2d4048961970c486"} -->

## Slide 70 - LiveDemo: Vòng ĐờiĐầy Đủ Của Một Prompt Version

LIVEDEMO

1. Demo1: Pushprompt v2 vào registry→xemversion ID bất biến + diffso với v1

2. Demo2: MởPR →promptfoochạy trong CI→failvìtụt điểm →xem commenttrên PR

3. Demo3: Sửaprompt, pass gate→dờilabel staging →canary10% traffic

4. Demo4: Nhét datetime.now() vàosystem prompt →xem cache_read_input_tokens rơivề 0 và cost/request nhảy vọt

5. Demo5: Sựcố →rollbackbằng cách dời label→bấmgiờ tới khi metric hồi phục Giảngviên (VinUni) AICB· Ngày 22 Tuần5 50 / 52

---

<!-- chiron-source-span: {"source_span_id":"4a2837dd-5258-5fdf-95e5-4f3e7152e37f","locator":{"kind":"page","page":71,"label":"Slide 71","section_title":"Lab#22","extraction_method":"pdf-text-layer"},"checksum":"97a4e88eaab527c55b1d4450e0c10c4304ec26962c8c44bc3302ed9684ba9651"} -->

## Slide 71 - Lab#22

LAB#22 Mụctiêu: PromptArtifact Có Vòng Đời Đầy Đủ

### Deliverable

1. Dựngpromptregistry(Langfuseself-hosthoặcLangSmith): tạo ≥3versioncócommitmessage theokhuôn mẫu 3 phần

2. Viếtsuite promptfoo (∼20case) + GitHub Action chặnmerge khi tụt điểm; chứng minhbằng mộtPR bịchặn

3. Wirefetch có cache TTL +fallback prompt; tắt registry và chứngminh appvẫnchạy

4. Gắntag prompt_version vàotrace; xuất bảng cost/latency/cache-hit theotừng version

5. Diễntập rollback 4 bước; ghilại thời gian thực tế từlúc phát hiện tới lúc metrichồi phục Thờigian: 2giờ Giảngviên (VinUni) AICB· Ngày 22 Tuần5 51 / 52

---

<!-- chiron-source-span: {"source_span_id":"c7961353-320a-5c5e-a45f-c310449bddf8","locator":{"kind":"page","page":72,"label":"Slide 72","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"7d4622e7fe61826d59bbc94634fb220050ab1d578e44ac4d2337b2ff30176f0f"} -->

## Slide 72 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 Promptlà artifact,khôngphảistring —gồmcảmodel pin,toolschema,retrieval vàguardrail config. Thiếu một mảnhlà chưa version hoá. 2 Version bất biến + label di độnglo cả versioning lẫn rollback — nhưng rollback chỉ chạy đượcnếu model snapshot cũ cònsống. 3 Promptversionchínhlàcacheprefix. Mỗilầnsửalàmộtsựkiệnchiphí—đo cache_read cùngvới cost. 4 Gắntag ngayhôm nay. Dữ liệu attributionkhông truy hồi được cho quákhứ. 5 Repo,cataloghayplatformđềuđược—miễnlà artifactexportđượcvàcontrỏdờiđược. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 51 / 52

---

<!-- chiron-source-span: {"source_span_id":"9a29011d-2b82-56cd-ad8e-806690368efd","locator":{"kind":"page","page":73,"label":"Slide 73","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"588549dfb8a8b041236346ec09e857b1160547b5ca869fd7eea3abd257f1cec9"} -->

## Slide 73 - Tiếptheo & Bài tập

Bàitiếp theo Ngày 23: Monitoring & Observabil- ityStack “Prometheus, Grafana, OpenTeleme- try và SLO — từ “prompt nào đang chạy” sang “toàn hệ thống đang khoẻ đếnđâu”” Bàitập về nhà

- Hoànthành Lab 22: prompt
artifactcó eval gate + rollback + costreport

- Càiđặt Docker Compose cho
Prometheus+ Grafana (pre-lab N23)

- Đọctrước: OpenTelemetry
Pythoninstrumentation guide Giảngviên (VinUni) AICB· Ngày 22 Tuần5 52 / 52

---

<!-- chiron-source-span: {"source_span_id":"484a9822-6825-5bc7-bebf-8e6a42e6329b","locator":{"kind":"page","page":74,"label":"Slide 74","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"745dbfcd3eecb2622e73e7a9004cc5d3315e58bf48fae1ccb7b35c8497f2859b"} -->

## Slide 74 - Hỏi& Đáp

Câu hỏi nào về prompt registry, eval gate trong CI, model deprecation, hay cache economics?

---

<!-- chiron-source-span: {"source_span_id":"2817eaa2-5ede-5a7b-841d-2f765464f47b","locator":{"kind":"page","page":75,"label":"Slide 75","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"d440fe283f43fb360e62be5a86140d432a1df254af33ab01863b72bba9ba3488"} -->

## Slide 75 - Cảmơn!

AICB-P2T2 · Ngày 22 LLMOps & Prompt Versioning lms.vinuni.edu.vn · Slide & template trên LMS
