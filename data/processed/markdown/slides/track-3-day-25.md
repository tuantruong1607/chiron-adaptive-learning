---
schema_version: 1
course_id: rag-intensive
document_id: "947a31c5-3d06-50df-b7c7-2988c1be0236"
document_version_id: "a30418cf-0556-5c0a-9a84-373e90fff621"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Circuit Breakers, Caching & Reliability"
source_file: "track 3 - day 25.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 25.pdf"
source_sha256: "ab3a45c9dd3f15fa537f52aa1a93fc1ec38cc088f1f128afd9e2cd8bb345cfba"
parser_version: chiron-structured-markdown-v1
page_count: 34
sparse_page_count: 1
extraction_methods: "{\"pdf-text-layer\":33,\"pdf-text-layer-sparse\":1}"
language: vi
---

# Circuit Breakers, Caching & Reliability

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"259cdf40-2c2d-5d3f-8219-d64bc2e2fc4d","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Circuit Breakers, Caching & Re","extraction_method":"pdf-text-layer"},"checksum":"789dc1b69409e97f742b11abb11b1cbfb12d720c955d5a9161335956221eccc1"} -->

## Slide 1 - Circuit Breakers, Caching & Re

Circuit Breakers, Caching & Re- liability for Production Agents AICB-P2T3 · Day 10 · Agent Production-Ready Instructor VinUniversity · Phase2·Track3·Week5

---

<!-- chiron-source-span: {"source_span_id":"8931792d-3705-5d3f-83a3-8e64e7892cf7","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"0c1b5474f8462705e65299b2f663c4130d73766eb7c591fd040a350c7c31b8ea"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Khi LLM provider timeout trong production, agent của bạn sẽ tự phục hồi hay làm sập cả workflow?” Giữcâuhỏinàytrongđầukhihọcbàihômnay

---

<!-- chiron-source-span: {"source_span_id":"462d66c9-c6f6-560e-85af-1e211f92dd64","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội dung bài học","extraction_method":"pdf-text-layer"},"checksum":"0590c0f19d9dde3fd65a28cde22485699382706278a1b9f16523012f217bfa2d"} -->

## Slide 3 - Nội dung bài học

1. Mụctiêu&timeline2giờ

2. FailureModes

3. CircuitBreaker&Fallback

4. Caching&CostBudgeting

5. Observability&SLO

6. Lab: ReliabilityEngineering

7. Tổngkết Instructor (VinUni) AICB·Day10 Week5 1/23

---

<!-- chiron-source-span: {"source_span_id":"5d6368df-36c7-5c7f-9ee3-e2fe4fcbfe5f","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục tiêu & timeline 2 giờ","extraction_method":"pdf-text-layer"},"checksum":"de0935b9750695ed48f5ffac5bd0a0a27ee41350fdae4063bba71ec6ccead911"} -->

## Slide 4 - Mục tiêu & timeline 2 giờ

01 Tậptrungvàoreliabilityprimitives: circuitbreaker,fall- back,cache,metrics,chaostest.

---

<!-- chiron-source-span: {"source_span_id":"c85b0d37-fa16-58e5-84c0-a7046288741c","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Sau buổi học, học viên làm được gì?","extraction_method":"pdf-text-layer"},"checksum":"b9a6335f8b069e2aaba5a3273667b31500f78e0bf81587b73fec73106bce6352"} -->

## Slide 5 - Sau buổi học, học viên làm được gì?

Conceptual outcomes

- Nhậndiện6nhómlỗiproduction
củaLLMagent.

- Giảithích3trạngtháicircuit
breaker.

- Phânbiệtexactcache,semantic
cache,tool-resultcache.

- ThiếtkếSLI/SLO/SLAchoagent.
Practical outcomes

- Xâygatewaycófallbackchain.

- Loglatency/cost/cachehit/circuit
state.

- Chạychaostestvàloadtestnhỏ.

- Viếtreportcómetricđểchấm
điểm. Trong lớp: hoàn thành baseline reliability harness. Bài lab mở rộng 4 giờ giúpphânloạinhómhoànthànhsớmvànhómđàosâu. Instructor (VinUni) AICB·Day10 Week5 2/23

---

<!-- chiron-source-span: {"source_span_id":"d0fd5ed1-a6a4-5ccf-a497-80931851e77b","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Timeline trên lớp: 2 giờ","extraction_method":"pdf-text-layer"},"checksum":"9b84a755b9765a8c5a048db3c5e1d7106462bf52452936b6fe2aa7bb7c3bea69"} -->

## Slide 6 - Timeline trên lớp: 2 giờ

00:00 00:20 00:45 01:10 01:35 02:00 Failuremodes+CB Cache+budget Observability Labkickoff Lý thuyết có tương tác

- 20’reliabilityfailuremap

- 25’circuitbreaker+fallback

- 25’caching+costbudget

- 25’metrics+chaosthinking
Lab kickoff trong lớp

- 10’repowalkthrough

- 15’teamplanning+firstrun

- Saulớp: hoànthiện4hlab/report
Instructor (VinUni) AICB·Day10 Week5 3/23

---

<!-- chiron-source-span: {"source_span_id":"8be4673c-a956-55e6-be1d-7645617958f8","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Failure Modes","extraction_method":"pdf-text-layer"},"checksum":"40db1f0c2c647a8d35b888a5c67f2eb09c9760d632d523e267a519829eae2799"} -->

## Slide 7 - Failure Modes

02 Reliabilitybắtđầutừviệcgọiđúngtênlỗi: transient,out- age,degraded,stale,costly,unsafe.

---

<!-- chiron-source-span: {"source_span_id":"581e8fb7-cf96-5906-b41c-0cd2566ac7d6","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Production agent fail như thế nào?","extraction_method":"pdf-text-layer"},"checksum":"08d5bc56d5cf3e640bb933b843e8528cba9ee7e9fb5941df3c51ed30ca07a33e"} -->

## Slide 8 - Production agent fail như thế nào?

UserRequest LLMGateway ProviderA ProviderB Cache/ToolAPIs Lỗi có thể xuất hiện ở provider, gateway,cache,tool,hoặcbusi- ness action. Reliability làsys- tem property,khôngphảichỉlà thêmretry. 6 loại lỗi cần monitor

1. Providertransient: 429/500/timeout.

2. Degradedlatency: P95tăngmạnh.

3. Fulloutage: providerkhôngphản hồi.

4. Orchestrationloop: state/retrysai.

5. Tool/cachefailure: stale/schema/auth.

6. Businessactionsai: sideeffect khôngrollback. Instructor (VinUni) AICB·Day10 Week5 4/23

---

<!-- chiron-source-span: {"source_span_id":"a3c17a2e-f8b6-5a3e-8878-530fcf5e5673","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Case: cascading failure từ retry vô tội vạ","extraction_method":"pdf-text-layer"},"checksum":"d7f5b13e860ca383cb0fcd2f0b81792797c34ff8909ff35629f47dc879813bf4"} -->

## Slide 9 - Case: cascading failure từ retry vô tội vạ

Providertimeout Clientretry3lần Quota/rate limitcạn Workflowoutage Think-pair-share: 5phút Hãychọnmộtsảnphẩmagentbạnbiết. Nếuproviderchínhbịtimeout30 giây, người dùng sẽ thấy gì? Nhóm đề xuất một cáchcontain, isolate, recover. Retrychỉlàbướcđầu. Nếukhôngcócircuitbreaker+fallback+budget, retrycóthểbiếnlỗinhỏthànhoutagelớn. Instructor (VinUni) AICB·Day10 Week5 5/23

---

<!-- chiron-source-span: {"source_span_id":"1307d8d1-87ef-5564-bf78-47e59c4c8332","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Silent degradation: không lỗi nhưng chất lượng giảm","extraction_method":"pdf-text-layer"},"checksum":"c7d4b4ba0612abf1c5fb39c393b6976a332ec545755abb5c29cee5cd891c0789"} -->

## Slide 10 - Silent degradation: không lỗi nhưng chất lượng giảm

time quality errorrate=0% faithfulness giảmdần Nguyên nhân thường gặp

- Providercậpnhậtmodel
silently.

- Prompt/schemathayđổi
nhưngevalkhôngđổi.

- Knowledgebasestalehoặc
retrievalyếu.

- Cachetrảcâuđúngcũnhưng
saihiệntại. Lưu ý: Quality SLO phải đi cùnguptimeSLO.Errorrate= 0%khôngđủ. Instructor (VinUni) AICB·Day10 Week5 6/23

---

<!-- chiron-source-span: {"source_span_id":"0a4c1fee-0757-551e-b461-3344a88c7f3d","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Circuit Breaker & Fallback","extraction_method":"pdf-text-layer"},"checksum":"ddd88df0c2bc4a2c9f8404c7208b828cafacb187e29307af5b9392d845014161"} -->

## Slide 11 - Circuit Breaker & Fallback

03 Circuitbreakerngắtgọiproviderđanghỏng;fallback chaingiữtrảinghiệmuserởmứcchấpnhậnđược.

---

<!-- chiron-source-span: {"source_span_id":"94b7e7ed-87b9-52c2-90b7-0a6985d47281","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Circuit Breaker: 3 trạng thái","extraction_method":"pdf-text-layer"},"checksum":"0c61571564ef2f7767530b7f0da45cb358bc77ad487d2413a5e49833c67a84bb"} -->

## Slide 12 - Circuit Breaker: 3 trạng thái

CLOSED normalcalls OPEN failfast HALF-OPEN probecall failurethreshold resettimeout success fail Nêncóbreakertheotừngprovider/model/task. ProviderAopenkhôngnên kéoproviderBhoặccachelayersậptheo. Instructor (VinUni) AICB·Day10 Week5 7/23

---

<!-- chiron-source-span: {"source_span_id":"3a6b92d2-4dc4-520e-8068-298cf98e7715","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Circuit breaker ở mức code","extraction_method":"pdf-text-layer"},"checksum":"1d8cd4072bbd155fb38dbc3a45a84d0ff904edfce3e291b8e4b29244a026180d"} -->

## Slide 13 - Circuit breaker ở mức code

```text
class CircuitBreaker:
def call(self, fn, *args, **kwargs):
if self.state == "OPEN":
if not self.ready_to_probe():
raise CircuitOpenError()
self.state = "HALF_OPEN"
```

### try
result = fn(*args, **kwargs) self.record_success()

```text
return result
```

### except Exception
self.record_failure() raise Các tham số chính

- failure_threshold

- reset_timeout_seconds

- success_threshold

- exceptionnàođượctínhlà
failure Lưu ý: Production multi- instance: state nên có backend chung như Redis, khôngchỉin-memory. Instructor (VinUni) AICB·Day10 Week5 8/23

---

<!-- chiron-source-span: {"source_span_id":"f58837d7-7ebe-5982-be98-9c589ea7c000","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Fallback ladder: graceful degradation","extraction_method":"pdf-text-layer"},"checksum":"a1feebae0a0236e74f7b7383ee9bac81f4a052fcec157564da2bc6e986ad7e1b"} -->

## Slide 14 - Fallback ladder: graceful degradation

Bestmodel highestquality Backupprovider samefeatureset Cheaper/smallermodel limitedquality Cachedresponse Staticfallbackmessage Fallbackkhôngchỉlàđổimodel. Cầnkiểmtra feature compatibil- ity: JSONmode,toolcalling,context length,latency/cost,policybehavior. Instructor (VinUni) AICB·Day10 Week5 9/23

---

<!-- chiron-source-span: {"source_span_id":"1cf5092b-a826-5ee1-aa4f-96971eeb627d","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Interactive: thiết kế fallback policy","extraction_method":"pdf-text-layer"},"checksum":"6020c01a8eca3dd4ef40f65ab92db9d8a5dcf28566f52d6d775e8718144ede08"} -->

## Slide 15 - Interactive: thiết kế fallback policy

Nhóm3người-8phút Mỗinhómchọn1task:customersupport,codereview,medicaltriage,hoặc internalHRchatbot. Thiếtkếfallbackladder4bậcvànêutasknào không được phép fallbacksangmodelyếuhơn. Gợi ý trade-off

- Qualityvslatency

- Costvssafety

- Cachedanswervsfreshness

- Staticresponsevsusertrust
Output cần nộp

- Ladder4bậc

- Điềukiệnchuyểnbậc

- Metricđểkiểmchứng

- Rủirolớnnhất
Instructor (VinUni) AICB·Day10 Week5 10/23

---

<!-- chiron-source-span: {"source_span_id":"7f6f01e3-485b-50a0-b0ea-d4fd00fed3bb","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Caching & Cost Budgeting","extraction_method":"pdf-text-layer"},"checksum":"1fc018efce44d6ea40a0db86002cc839d40a1e48a3e9436d6407320ed6ea67f6"} -->

## Slide 16 - Caching & Cost Budgeting

04 Cacheđúngchỗcóthểgiảmlatency/cost;cachesaichỗ tạostaleanswervàhallucinationổnđịnh.

---

<!-- chiron-source-span: {"source_span_id":"703db486-69d6-57d3-92d2-2809f92d57a3","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"3 tầng cache cho LLM applications","extraction_method":"pdf-text-layer"},"checksum":"6147cb6bce90e2d33c3793295a92bda6d5f903288f7ba1c79b00d1ff255891fb"} -->

## Slide 17 - 3 tầng cache cho LLM applications

1. Providerprompt/prefixcache: giảmcostkhiprefixdàiđượcreuse

2. Appsemanticresponsecache: querytươngtự →reuseresponse

3. Tool/resultcache: API/DB/re- sultexpensivenhưngdeterministic cachestack Cache deterministic và low-risk trước. Với semantic response cache, cần threshold,TTL,invalidation,vàallowlisttheotask. Instructor (VinUni) AICB·Day10 Week5 11/23

---

<!-- chiron-source-span: {"source_span_id":"1277e60e-bfcf-591a-ba64-29e1a910d7f4","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Semantic cache flow","extraction_method":"pdf-text-layer"},"checksum":"506f04858c0c9c0a901df0ada7285620eaf6ee383862d311ec365f82b1fd2c35"} -->

## Slide 18 - Semantic cache flow

Userquery Embed Vectorsearch HIT returncache MISS callLLM Storeresult sim >threshold sim <threshold Lưu ý: Cache poisoning: hai query cosine gần nhau nhưng intent khác nhau. Metricquantrọng: hitrate vàfalse-hitrate. Instructor (VinUni) AICB·Day10 Week5 12/23

---

<!-- chiron-source-span: {"source_span_id":"a44d4f45-d1a3-56ba-84fe-2e7661ae03a4","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Cost budgeting: reliability của ví tiền","extraction_method":"pdf-text-layer"},"checksum":"54efdffa94cbeb38e7f39ff2b2e3989f373529444de450f675cb323c5203b965"} -->

## Slide 19 - Cost budgeting: reliability của ví tiền

3 lớp control

1. Per-requestcap: maxtokens, maxtools,timeout.

2. Per-user/appratelimit: token bucket.

3. Monthlybudget: warn80%,hard stop/routecheapat100%. Metric cần log

- provider,model,routereason

- input/outputtokens,estimated
cost

- cachehit/miss,similarityscore

- latency,status,circuitstate
Đừng chỉ tổng cost theo ngày. Cần cost theo feature/user/model để tìm đườngcallđắtvàtốiưuđúngnơi. Instructor (VinUni) AICB·Day10 Week5 13/23

---

<!-- chiron-source-span: {"source_span_id":"135bf620-1431-519c-98fa-768c0e55f628","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Interactive: cache hay không cache?","extraction_method":"pdf-text-layer"},"checksum":"4cbb41530d0de3ed64822ab191c37d2d402253d15b5ada9fd2b6aaa03870c46b"} -->

## Slide 20 - Interactive: cache hay không cache?

Usecase Cachedecision Rủirochính FAQadmissions nêncachesemantic thôngtindeadlinestale Accountbalance khôngcacheresponse privacy+freshness Codeexplanation cachecóđiềukiện contextkhácnhau Weathertoday toolcacheTTLngắn staletheothờigian Policysummary cache+eventinvalidation policyupdate Votenhanh-5phút Vớimỗidòng,giơtay: cache/khôngcache/cachecóđiềukiện. Giảngviênchọn 2ýkiếntráichiềuđểtranhluận. Instructor (VinUni) AICB·Day10 Week5 14/23

---

<!-- chiron-source-span: {"source_span_id":"04a75040-4ef9-50f2-827f-56ac564ecbe9","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Observability & SLO","extraction_method":"pdf-text-layer"},"checksum":"cbb94165135327e14d9b0bed2c57fa168526edbac9e73d14c69287042f1bb119"} -->

## Slide 21 - Observability & SLO

05 Khôngđothìkhôngbiếtsystemđangtốt,chậm,đắt,hay đangtrảlờisai.

---

<!-- chiron-source-span: {"source_span_id":"6db6ccd7-2c00-5b9e-96ff-3d04b8e4c1d5","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"SLI, SLO, SLA cho LLM agent","extraction_method":"pdf-text-layer"},"checksum":"23d20ed77905161f3e302d6f572027e40cebf36342405f5ff95719f4e2f04922"} -->

## Slide 22 - SLI, SLO, SLA cho LLM agent

Kháiniệm Ýnghĩa Vídụtronglab SLI metricđođược availability,P95latency,cache hitrate,false-hitrate SLO targetnộibộ availability ≥99%,P95 <2.5s, fallbacksuccess ≥95% SLA camkếtbênngoài 99.5% uptime/tháng cho customer-facingAPI Errorbudget mứclỗiđượcphép nếuburnratecao →freezefea- ture,ưutiênreliability Lưu ý: LLMagentcầnthêmqualitySLO:faithfulness,safetypassrate,escalation correctness. Instructor (VinUni) AICB·Day10 Week5 15/23

---

<!-- chiron-source-span: {"source_span_id":"98681337-45ce-596f-a833-16c5badc2a3f","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Metrics instrumentation tối thiểu","extraction_method":"pdf-text-layer"},"checksum":"8df78f528dfc9e54f462fbdfc8a2df4f3f085c4c436ce64fbfbb8ae97085f3d2"} -->

## Slide 23 - Metrics instrumentation tối thiểu

REQUESTS = Counter( "agent_requests_total", [ "provider", "status", "route"]) LATENCY = Histogram( "agent_latency_seconds", [ "provider", "route"]) CACHE_HITS = Counter( "cache_hits_total", [ "cache_type"]) CIRCUIT_STATE = Gauge( "circuit_state", [ "provider"]) # 0 closed, 1 open, 2 half-open Report cần có

- LatencyP50/P95/P99.

- Availability/errorrate.

- Fallbacksuccessrate.

- Cachehitratevàfalse-hit
examples.

- Recoverytimetrongchaos
test. Instructor (VinUni) AICB·Day10 Week5 16/23

---

<!-- chiron-source-span: {"source_span_id":"76feae99-972f-5bd0-a8f7-6b6e2b0c9cd7","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Chaos testing: cố tình làm hỏng","extraction_method":"pdf-text-layer"},"checksum":"0f86d41fad02f0831cf65ff79ad9dbced22ca0e9ccd9ac938ab924cb7cd966aa"} -->

## Slide 24 - Chaos testing: cố tình làm hỏng

Chaos scenarios trong lab

1. Primaryprovidertimeout100%.

2. Primaryproviderintermittent 50%.

3. Cachereturnsstalecandidate.

4. Costcapgầncạn. Expected evidence

- CircuitchuyểnCLOSED →OPEN.

- Gatewayroutesangfallback.

- Khôngretrystorm.

- Metrics/reportghirõrecovery
time. Minidesignreview-7phút Mỗinhómviết1chaosscenariomớivàmetricchứngminhsystemrecover. Nhómkhácphảnbiện: scenariođócósideeffectkhông? Instructor (VinUni) AICB·Day10 Week5 17/23

---

<!-- chiron-source-span: {"source_span_id":"c4317134-6fbe-56b5-9f93-8c4969367063","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Lab: Reliability Engineering","extraction_method":"pdf-text-layer"},"checksum":"c7ece5b3a7cc08672ed7ba1a29be7d05297c3f05775d835a7563600906587697"} -->

## Slide 25 - Lab: Reliability Engineering

06 Labđượcthiếtkế4giờ;trênlớpkickoff2giờ. Họcviên giỏicóthểhoànthànhcoresớmvàlàmstretchtasks.

---

<!-- chiron-source-span: {"source_span_id":"24575540-10a7-5411-bbe7-2cb26867991b","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Lab #10","extraction_method":"pdf-text-layer"},"checksum":"3f2927c29a6f2c6d55d2ab40d703b0a7a7c2b186c681722b1c4dee0772610bff"} -->

## Slide 26 - Lab #10

Mục tiêu: Buildreliabilitygateway:circuitbreaker+semantic/toolcache +metrics+chaosreport Deliverable:Repohoànchỉnh,metricsJSON/CSV,reportMarkdown/PDF, democommandchạyđược Thời gian: 2giờtrênlớp+2giờmởrộng Instructor (VinUni) AICB·Day10 Week5 18/23

---

<!-- chiron-source-span: {"source_span_id":"b2c6125e-03b2-54f0-a9ad-c33cec08affa","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Lab milestones: 4 giờ nhưng timeline lớp 2 giờ","extraction_method":"pdf-text-layer"},"checksum":"31876401c7f0fe42a11e7f0a90964d120c26383168257038eef723ca3490ac22"} -->

## Slide 27 - Lab milestones: 4 giờ nhưng timeline lớp 2 giờ

Thờigian Việccầnlàm Deliverable 0–30’ Setup repo, chạy tests baseline, đọc TODO screenshot/testlog 30–75’ Implement circuit breaker + fallback router statetransitionlog 75–120’ Implement metrics + run mini chaos test metrics.jsonlần1 120–180’ Implementcache+TTL/thresholdtun- ing cachecomparisontable 180–240’ Loadtest+report+rubricself-check finalreport+plots/CSV Corepasskhoảng2giờchonhómmạnh. Stretch2giờcònlại: false-hitanalysis, costsimulation,reportchấtlượngcao,vàtestcoverage. Instructor (VinUni) AICB·Day10 Week5 19/23

---

<!-- chiron-source-span: {"source_span_id":"dd355b02-0e8e-573e-9285-4c890770d6f2","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Metric & report bắt buộc để chấm điểm","extraction_method":"pdf-text-layer"},"checksum":"e2fd081a13adbd7190a87b9be33c760ea7ecaf3ce2fb3acb2654f85db2a147f8"} -->

## Slide 28 - Metric & report bắt buộc để chấm điểm

Metrics bắt buộc

- availability,errorrate

- latencyP50/P95/P99

- fallbacksuccessrate

- circuitopencount+recoverytime

- cachehitrate+estimatedcost
saved

- chaosscenariopass/fail
Report bắt buộc

- architecturediagramngắn

- configtable

- experimentsetup

- metricstabletrước/saucache

- failureanalysis

- nextsteps
Lưu ý: Reportkhôngcómetricđịnhlượng=khôngđạtphầngrading. Instructor (VinUni) AICB·Day10 Week5 20/23

---

<!-- chiron-source-span: {"source_span_id":"a49eef31-54cf-52ea-ac35-bb68a49afac8","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Rubric tổng quan","extraction_method":"pdf-text-layer"},"checksum":"d0e96f5415a2a856a7a3bbfa21dca1424701c59eb905c9159cd3cc4853393d2d"} -->

## Slide 29 - Rubric tổng quan

Hạngmục Điểm Kỳvọng Circuitbreaker/fallback 25 state machine đúng, không retry storm, fallbackcóroutereason Cache/cost 20 hitrate/costsavedrõ,TTL/thresholdcógiải thích,false-hitexamples Observability/metrics 20 P50/P95/P99, availability, circuit state, cachemetricsreproducible Chaos/loadtest 20 ítnhất3scenarios,córecoveryevidence Report/codequality 15 READMErõ,tests,typehints,config,report dễchấm Instructor (VinUni) AICB·Day10 Week5 21/23

---

<!-- chiron-source-span: {"source_span_id":"8fd5c7a2-ab58-5fe2-b757-394319b3a12f","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Demo cuối buổi / cuối lab","extraction_method":"pdf-text-layer"},"checksum":"bbd8382f0cf2d6cd50f3649b46a82f60909cd55aec75f670a1f3d3b087a1eb3c"} -->

## Slide 30 - Demo cuối buổi / cuối lab

1. Chạymộtcommandtạometrics: make run-chaos hoặctươngđương.

2. Chỉrabreakerchuyểnstatekhiprimaryfail.

3. Sosánhlatency/costcócachevàkhôngcache.

4. Mởreportvàgiảithích1failuremodecòntồntại.

5. Nêu1configbạnsẽđổinếudeployproduction. Instructor (VinUni) AICB·Day10 Week5 22/23

---

<!-- chiron-source-span: {"source_span_id":"304aff62-99ca-5fc5-8049-ff0bc9dcdca2","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Tổng kết","extraction_method":"pdf-text-layer"},"checksum":"f94849219c39a68ebe1b779c2fe64cfa20e6e0efc3f2a2f2f65b1f840e498abf"} -->

## Slide 31 - Tổng kết

07 Reliabilityengineeringgiúpagentfailgracefully,đođược, vàcóthểcảithiệnbằngdữliệu.

---

<!-- chiron-source-span: {"source_span_id":"3fe853b1-cf18-5084-be9c-e1e5ee4a9e9f","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Tổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"e6cb384a3eee9180cb269d220048d2aced115a8539aa5ec2c119318f59a8e050"} -->

## Slide 32 - Tổng kết — Key T akeaways

Những ý chính cần nhớ trướckhisangbàitiếptheo 1 Circuitbreaker+fallbacklàminimumviablereliabilitychoagentproduction. 2 CachecóROIcaonhưngcầnguardrail: TTL,threshold,invalidation,false-hittrack- ing. 3 Metricsphảibaophủlatency,availability,cost,cache,circuitstatevàquality. 4 Chaos/loadtestbiếngiảđịnhthànhbằngchứng;reportđịnhlượnggiúpchấmđiểm côngbằng. Instructor (VinUni) AICB·Day10 Week5 22/23

---

<!-- chiron-source-span: {"source_span_id":"ef3e1b26-954a-56a8-89d8-ede5c9aa81d3","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"References","extraction_method":"pdf-text-layer"},"checksum":"39d1bd98da8b84d7243069500228263c0233475da51d6cc2a12d9c62c8636fba"} -->

## Slide 33 - References

1. MicrosoftAzureArchitectureCenter: CircuitBreakerpattern.

2. ReleaseIt! DesignandDeployProduction-ReadySoftware,MichaelNygard.

3. PrometheusclientPython: Counter,Gauge,Histogramdocs.

4. LiteLLMdocumentation: routing,retries,fallbacks.

5. Langfusedocumentation: LLMobservability,traces,costandlatencymetrics. Instructor (VinUni) AICB·Day10 Week5 23/23

---

<!-- chiron-source-span: {"source_span_id":"856fa90f-d9ef-5b90-8e24-b51f1a795951","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer-sparse","page_image":"../../assets/page-images/ab3a45c9dd3f/page-0034.png","visual_fallback":true},"checksum":"85d68bfe7e22254d451986cab9a83fa61967c5c9a265bdb543377a3c5017c42a"} -->

## Slide 34 - Hỏi & Đáp

![Visual fallback - track 3 - day 25 - slide 34](../../assets/page-images/ab3a45c9dd3f/page-0034.png)

> Trang này được giữ dưới dạng ảnh vì text layer/OCR không đủ để biểu diễn nội dung trực quan.
