---
schema_version: 1
course_id: rag-intensive
document_id: "20ee8b8a-2175-5018-9e8e-671ae6abf2eb"
document_version_id: "a689b9c7-3869-51f1-8f84-e790c37530a5"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Monitoring, Logging & Observability"
source_file: "day 13.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\day 13.pdf"
source_sha256: "adbab4fca3a443166b1c71d1446257c8a1353dcc1433954fdd5928d323e24ab0"
parser_version: chiron-structured-markdown-v1
page_count: 114
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":114}"
language: vi
---

# Monitoring, Logging & Observability

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"e10dd9e8-c9fd-5b8f-aaaf-1323737d757b","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Monitoring, Logging & Observability","extraction_method":"pdf-text-layer"},"checksum":"1c9fb482147535c9ecc5c4c96ea7e4f1afa12d867f1c2f7a7857f84d41b03136"} -->

## Slide 1 - Monitoring, Logging & Observability

AICB-P1· Ngày 13 · Biếtagent đang chạy thế nào trướckhi user phàn nàn TênGiảng Viên VinUniversity · Phase 1 · 2026

---

<!-- chiron-source-span: {"source_span_id":"263c49f8-ae0d-5587-89ed-e0acf536a56b","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"641243ebd868d5caea154071ef4e1550de75be09dd44402109fcc060bda26347"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Agent bạn deploy hôm Day 12 chạy ngon. 3 ngày sau: latency tăng gấp đôi, cost tăng 300 phần trăm, và 1 trên 20 câu trả lời là bịa. Bạn biết những điều này khi nào? — Khi user phàn nàn. Đó là cách tệ nhất, và đắt nhất, để phát hiện vấn đề.” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"ec98d5be-2d97-5983-a980-da8e935104ed","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"0d71886f0a88444c3744c2d239c13b2e33f77b2eeb057af8fadd23c8beb410b2"} -->

## Slide 3 - NộiDung Bài Học

1. Vìsao agent cần observability

2. 3pillars + pillar thứ 4

3. AI-specificmetrics

4. Structuredlogging

5. Distributedtracing cho agent

6. Bộcông cụ LLM-observability 2026

7. Productionstack: Prometheus +Grafana

8. Dashboarddesign

9. Alerting& SLO

10. Costmonitoring & optimization

11. Debug1 incident bằng trace

12. Humanfeedback & online eval

13. Privacy& compliance khi logging

14. Checklist,Lab 13 & tổng kết Giảngviên (VinUni) AICB· Monitoring 2026 1/ 96

---

<!-- chiron-source-span: {"source_span_id":"f23fce17-40f8-56c5-b85b-8429af31d647","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"MụcTiêuNgày 13 (Bloom’sTaxonomy)","extraction_method":"pdf-text-layer"},"checksum":"d81142448517ed6f7d089cbd206f447364c17cb69fde07b366c6be64a5ef56b4"} -->

## Slide 4 - MụcTiêuNgày 13 (Bloom’sTaxonomy)

- Remember—liệt kê3pillars (metrics,logs, traces) +pillarthứ 4(continuouseval) và 6
nhómAI-specific metrics

- Understand—giải thích vì saoP99quan trọng hơn average,và SLO khác SLA thếnào

- Apply—implement structuredlogging (JSON+ correlation ID + PIIredaction) cho agent
đangdeploy

- Analyze—đọc tracewaterfall vàxác định bottleneck trong agentpipeline nhiều bước

- Evaluate—so sánh Langfuse / LangSmith/ Phoenix / Helicone cho usecase cụ thể

- Create—thiết kếmonitoringblueprint vớiSLO, alert rules (symptom-based) và
dashboard3 layers Giảngviên (VinUni) AICB· Monitoring 2026 2/ 96

---

<!-- chiron-source-span: {"source_span_id":"0157806a-54fe-5d54-9115-961c004f1b75","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"a2b2f30cb0c086b85f47208ec3b012fd8335aec94e7941611a2cdfb627b0c8c2"} -->

## Slide 5 - DeliverableCuối Ngày

Agentcó observability đầy đủ: bạn biết nó chạy thếnào màkhôngcần hỏi user.

- Structuredlogging pipeline: JSON,correlation ID, input/output đãredactPII

- Tracing: Langfuse (hoặc backendzero-key) connected,≥ 10traces

- Dashboard: latency P50/95/99 +TTFT,cost/ngày,error rate, token usage,tool-call
success

- ≥ 3alertrules →Slack;1 SLO + error budget; 1incident note đọc từ trace
Giảngviên (VinUni) AICB· Monitoring 2026 3/ 96

---

<!-- chiron-source-span: {"source_span_id":"67820d4b-ad5c-548b-9dc0-37d594f9b8d4","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Vì Sao Agent Cần Observability","extraction_method":"pdf-text-layer"},"checksum":"62950a071b48690e1d47b01b1a659700237643c0961f67d4494ea34fa405cca6"} -->

## Slide 6 - Vì Sao Agent Cần Observability

01 “It works” không đủ cho production — cần biết nó chạy TỐT đến đâu, chậm ở đâu, tốn bao nhiêu, và khi nào sắp hỏng

---

<!-- chiron-source-span: {"source_span_id":"291689ce-627d-5612-9ac7-e84f964dc3eb","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"TừArtifact Day 12 Sang ProductionReality","extraction_method":"pdf-text-layer"},"checksum":"bd50cb6a13a7c862c152c7cc63802ce3aec690e55777965891550a2fab5e3a0a"} -->

## Slide 7 - TừArtifact Day 12 Sang ProductionReality

Day12 đã làm được

- Agentdeployed trên cloud

- PublicURL hoạt động

- Healthcheck endpoint

- Basicauthentication
Nhưngchưa trả lời được

- Agentđang chậm hay nhanh?

- Tốnbao nhiêu tiền mỗi ngày?

- Baonhiêu request fail (hoặc trả lời
sai)?

- Khinào cần scale up?
Lưu ý:Không có monitoring, bạn chỉ biết agent hỏngkhi user phàn nàn. Health check“200 OK” không có nghĩa câutrả lời đúng. Giảngviên (VinUni) AICB· Monitoring 2026 4/ 96

---

<!-- chiron-source-span: {"source_span_id":"d4ecff07-5e98-5bbf-8ce1-1c804e7bb1c9","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Monitoringvs Observability — Hai KháiNiệm Khác Nhau","extraction_method":"pdf-text-layer"},"checksum":"6c1d52807f8048cff28d806a4eff81c815fbc3aedec5f68c396baa5d73df06c9"} -->

## Slide 8 - Monitoringvs Observability — Hai KháiNiệm Khác Nhau

Monitoring Theodõi các câu hỏiđãbiết trước.

- Dashboard+ alert dựng sẵn

- Trảlời: “Xcó hỏng không?”

- Tốtcho failure mode đã lườngtrước

- “Known-knowns”
Observability Thuộctính củahệthống: hỏicâu mớimà khôngcần deploy code.

- Telemetryđủ giàu (metrics + logs +
traces)

- Trảlời: “TẠISAO X hỏng?”

- Tốtcho failure modechưatừng
gặp

- “Unknown-unknowns”
Giảngviên (VinUni) AICB· Monitoring 2026 5/ 96

---

<!-- chiron-source-span: {"source_span_id":"9cfc9457-8666-5a29-85f3-be233fa9deb9","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"ObservabilityAI Khác Gì Monitoring PhầnMềm TruyềnThống?","extraction_method":"pdf-text-layer"},"checksum":"366733b49a24df83c0dc305b3a1675b7e1f739c73006debab03c742a3891e56d"} -->

## Slide 9 - ObservabilityAI Khác Gì Monitoring PhầnMềm TruyềnThống?

Cùng input, output khác nhau mỗi lần. Khôngthểtestbằng“sosánhstring”. Phải đochấtlượng,không chỉ pass/fail. App không “crash” — nó vẫn trả 200 OK nhưng câu trả lời tệ dần. Không có ex- ceptionđể bắt. Mỗi request tốn tiền theo số token. Một bug loop có thể đốt budget trong vài giờ —CPU/RAM không nói cho bạnbiết. Hallucinated tool args, vòng lặp vô tận, context overflow, prompt injection — nhữnglỗimàAPMtruyềnthốngkhôngcó kháiniệm. Giảngviên (VinUni) AICB· Monitoring 2026 6/ 96

---

<!-- chiron-source-span: {"source_span_id":"5053c8f4-ca8c-5869-9ceb-5d0888549488","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Costof Not Monitoring","extraction_method":"pdf-text-layer"},"checksum":"28411912134814a60e45a79e420c5b85d9a5ed765c7d18c39eb24a84e1700a23"} -->

## Slide 10 - Costof Not Monitoring

Agenttrảlờisainhưngkhôngaibiết. User mấtniềmtindần. Đếnkhipháthiệnthìđã mấtuser. Tokencosttăngdầnmàkhôngalert. Cuối tháng nhận bill gấp 5 lần. Đốt hết budget trướckhi kịp react. Latency P95 tăng 10ms mỗi tuần. 6 tuần sau: chậm gấp đôi. Không ai để ý vì khôngcó baseline. Bug report: “agent sai hôm qua.” Không log,khôngtrace. Khôngreproduceđược. Khôngfix được. Giảngviên (VinUni) AICB· Monitoring 2026 7/ 96

---

<!-- chiron-source-span: {"source_span_id":"181cb06b-0d20-5d5b-a762-a16405bfb944","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Observability: Vài Cột Mốc","extraction_method":"pdf-text-layer"},"checksum":"ecd2fd3fcadf6d2d618deb31a7d88dffc05537ce37686d510b8f165aea0308ca"} -->

## Slide 11 - Observability: Vài Cột Mốc

1 Logs (text) 2 Metrics & Prometheus 2012 3 Grafana 2014 4 Tracing & OTel 2019 5 LLM-native 2023+ Giảngviên (VinUni) AICB· Monitoring 2026 8/ 96

---

<!-- chiron-source-span: {"source_span_id":"3e77830a-09f4-523b-a48f-46cbed384b80","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"ControlTheory — Observability Là MộtFeedback Loop","extraction_method":"pdf-text-layer"},"checksum":"719de90d2857aa6b1edcfc456c14c0747ce82c4aab22be8d3b8d5f2fa444fa2c"} -->

## Slide 12 - ControlTheory — Observability Là MộtFeedback Loop

Agent System Observe metrics Analyze compare Act fix/scale Feedbackloop Mean Time To Detect: từ khi sự cố xảy rađến khi phát hiện. MeanTimeToRecover: từkhipháthiện đếnkhi fix xong. Observabilitytốt=giảm MTTDxuốngphút,khôngphảingày. Khôngcóobservability, MTTD= thời gianuserphản ánh. Giảngviên (VinUni) AICB· Monitoring 2026 9/ 96

---

<!-- chiron-source-span: {"source_span_id":"295d085a-4b36-54bf-9689-9bb6302cc073","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"3 Pillars + Pillar Thứ 4","extraction_method":"pdf-text-layer"},"checksum":"6f60fb2509a20ddef282844ba50baf615c7e6794517257308b2519510f400744"} -->

## Slide 13 - 3 Pillars + Pillar Thứ 4

02 Metrics nói bao nhiêu / bao lâu, logs nói chuyện gì xảy ra, traces nói tại sao — và với AI có pillar thứ 4: câu trả lời có còn ĐÚNG không

---

<!-- chiron-source-span: {"source_span_id":"9c5d6a79-3dd5-50a6-972c-b9c421adc825","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"3Pillars of Observability","extraction_method":"pdf-text-layer"},"checksum":"1bddbaddec5e8ae21e1b0f65907aa788e4f706dc9edd0ca1cd3706adea8bc8d1"} -->

## Slide 14 - 3Pillars of Observability

Metrics Đolường Logs Ghichép Traces Theodõi Bao nhiêu? Bao lâu? Latency, error rate, cost per day Gì xảy ra? Input, output, errors, timestamps Tại sao? End-to-end journey, bottleneck, root cause Logsnóichuyện gì xảy ra.Metricsnóibao nhiêu và bao lâu.Tracesnóitại sao. Giảngviên (VinUni) AICB· Monitoring 2026 10/ 96

---

<!-- chiron-source-span: {"source_span_id":"0ee676ec-9c27-5371-8262-d6aaf5b5157c","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"PillarThứ 4: Continuous/ Online Eval","extraction_method":"pdf-text-layer"},"checksum":"3f68332ef4b69a3c9fa3e76a27028ecf53feb8acf3f58f5eb28e75cd29b95f9b"} -->

## Slide 15 - PillarThứ 4: Continuous/ Online Eval

Pillarthứ4 — VớiAIsystem,bapillartruyềnthốngkhôngtrảlờiđượccâuhỏiquan trọng nhất:câu trả lời có còn đúng không?Pillar thứ 4 = đochất lượng output liêntục trên production.

- HTTP200 kháccorrectness— request “thành công” vẫn cóthể là câu trả lời bịa

- Latencythấp kháchữuích — trả lời nhanh nhưngsai còn tệ hơn

- Errorrate 0%kháckhôngđốt tiền — chi phí vẫncó thể tăng vọt
Day 13 đo chất lượngliên tục trên production(online). Day 14 đo chất lượngcó hệthống bằng benchmark(offline). Cả hai bổsung cho nhau. Giảngviên (VinUni) AICB· Monitoring 2026 11/ 96

---

<!-- chiron-source-span: {"source_span_id":"2f213d4b-a45b-5e62-b422-16b006d2cf1c","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"TạiSao Chỉ Logs Là KhôngĐủ?","extraction_method":"pdf-text-layer"},"checksum":"fe9d4af5845ffb370e7208ebba862da5987ab0c59384a3a60f08299822850bf1"} -->

## Slide 16 - TạiSao Chỉ Logs Là KhôngĐủ?

Chỉcó logs

- biếtrequest nào fail

- nhưngkhông biết fail rate bao
nhiêu

- khôngbiết latency đang tăng dần

- khôngbiết bottleneck ở đâu
Đủpillars

- metricscho biết trend (tăng/giảm)

- logscho biết chi tiết từngrequest

- tracescho biết chậm ở bướcnào

- evalcho biết chất lượng còntốt
không Logs giống camera an ninh. Metrics giống bảng điều khiển xe. Traces giống bản đồ GPS.Eval giống người kiểm định chấtlượng. Cần cảbốn đểláian toàn. Giảngviên (VinUni) AICB· Monitoring 2026 12/ 96

---

<!-- chiron-source-span: {"source_span_id":"d35b33d8-7ba7-584e-9442-6543820754aa","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"PillarNào TrảLời CâuHỏi Nào?","extraction_method":"pdf-text-layer"},"checksum":"1d11c46cc5710e36e3df159a643393f35117d8b900ba67ca294950610d89ef03"} -->

## Slide 17 - PillarNào TrảLời CâuHỏi Nào?

Câuhỏi Pillar Côngcụ ví dụ “Errorrate có tăng không?” Metrics Prometheus,Grafana “Request req-abcđãlàm gì?” Logs Loki,JSON logs “Chậm ở bước nào trong agent loop?” Traces Langfuse,Tempo “Câutrả lời còn đúng không?” Eval (4th) LLM-judge,RAGAS Chọn pillar theo câu hỏi bạn cần trả lời. Đừng thu thập telemetry chỉ vì có thể — mỗi data pointđều tốn tiền lưu trữ(xem §10). Giảngviên (VinUni) AICB· Monitoring 2026 13/ 96

---

<!-- chiron-source-span: {"source_span_id":"a1f09b92-0e4c-5dab-9a09-e19fac20368e","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"AI-Specific Metrics","extraction_method":"pdf-text-layer"},"checksum":"8064a562156fbc9655cb65dac18c85a478780e9abc5d0a14e509d5a385e7724c"} -->

## Slide 18 - AI-Specific Metrics

03 Monitoring truyền thống đo CPU, RAM, uptime — AI agent cần thêm: token, cost, TTFT, chất lượng, tool-call success, retrieval quality

---

<!-- chiron-source-span: {"source_span_id":"2878d8ce-9fe2-50e8-ac1f-0f12398bf01c","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"4Nhóm Metrics Cho AI Agent","extraction_method":"pdf-text-layer"},"checksum":"5dc7ae33799c9ff6e7a39e2e4216bb06104aab5d0300149fdbd316f40141d0a3"} -->

## Slide 19 - 4Nhóm Metrics Cho AI Agent

Performance

- LatencyP50 / P95 / P99

- Timeto first token (TTFT)

- Throughput(req/s, tokens/s)

- LLMcall duration
Quality(pillar 4)

- Hallucination/ faithfulness

- Taskcompletion rate

- Thumbsup/down, regenerate rate

- Guardrailtrigger rate
Cost

- Tokensper request (in / out)

- Costper request / per task

- Costper day / per user/ per feature

- Cachehit rate
Reliability

- Errorrate, uptime

- Tool-callsuccess / failure rate

- Retryrate, loop rate

- Retrievalrecall / empty-result rate
Giảngviên (VinUni) AICB· Monitoring 2026 14/ 96

---

<!-- chiron-source-span: {"source_span_id":"d0778391-0637-59b2-b90f-43727d6f1cc1","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"4Golden Signals + 2 ChoAI Agent","extraction_method":"pdf-text-layer"},"checksum":"011e2552da52a1c8c01be467fc6ff0168255fb5e8997f2477adc8ef64fd5f2c9"} -->

## Slide 20 - 4Golden Signals + 2 ChoAI Agent

GoogleSRE — 4 Golden Signals

1. Latency—thời gian phản hồi

2. Traffic—request rate (QPS)

3. Errors—error rate

4. Saturation—tài nguyên còn bao nhiêu AIagent cần thêm 2

5. Cost—$/request, $/user,token usage

6. Quality—hallucination rate, CSAT, groundedness Lưuý: Agentcóthể“up”(traffic/latency/errorOK)nhưng trảlờisaivàđốttiền. Đây là2 failure mode riêng của AImà monitoring truyền thống bỏ qua. Giảngviên (VinUni) AICB· Monitoring 2026 15/ 96

---

<!-- chiron-source-span: {"source_span_id":"d4388af7-4392-503e-b770-80b05034476a","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"REDvs USE — Hai PhươngPháp Observability","extraction_method":"pdf-text-layer"},"checksum":"dc652536d4d1fdb497b62f497fca0f9339709ea6dafcab1115aaa6dc682e86ab"} -->

## Slide 21 - REDvs USE — Hai PhươngPháp Observability

RED(request-centric)

- Rate— requests/giây

- Errors— error rate

- Duration— latency P50/P95/P99
Gócnhìn user: tôigửi request, được gì? USE(resource-centric)

- Utilization— tài nguyên dùng%

- Saturation— có queue/chờ
không?

- Errors— lỗi của resource
Gócnhìn resource: LLMAPI, queue đang làm gì? Agentchậm(RED:DurationP95tăng) →debugbằngUSE(LLMrate-limitutilization 95%)→bịthrottle →upgradetier hoặc fallback. Giảngviên (VinUni) AICB· Monitoring 2026 16/ 96

---

<!-- chiron-source-span: {"source_span_id":"1c82b73d-1cfb-5c89-b251-444bac84075c","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Latency: Percentiles + TTFT","extraction_method":"pdf-text-layer"},"checksum":"04e1d7cf13ba2dcdc649b422251c9653ad6ebd3f153a8a46c5c431fb61a6405a"} -->

## Slide 22 - Latency: Percentiles + TTFT

P50 ≈2.5s(nửa số request nhanh hơn) P95 ≈5s(95% request nhanh hơn) P99 ≈8s+ TTFT (Time To First Token)— Thời gian từ lúc gửi request đến token đầu tiên. Quyếtđịnh cảm giác “nhanh”. Điển hình 2026: P50≈0.5–1.0s,P95 ≈1.5–2.5s. Lưu ý:Trung bình (average) ẩn long tail. P95 mới là trải nghiệm thật.Reasoning modelàlớp latency riêng (chậm hơn 5–30x)— tách ra khi đo. Giảngviên (VinUni) AICB· Monitoring 2026 17/ 96

---

<!-- chiron-source-span: {"source_span_id":"819bfe3d-7d31-5e18-a738-925d633bf468","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"PercentileMath — Vì Sao P99Quan Trọng","extraction_method":"pdf-text-layer"},"checksum":"13d085c12e81b5f9841191fab794d7772366171553faaa9830e8e13da2299694"} -->

## Slide 23 - PercentileMath — Vì Sao P99Quan Trọng

Bài toán — Agent có P99 = 5s, user

### chat10 lượt. Xácsuất gặp≥ 1lần > 5s
P = 1− 0.9910≈ 9.6%

- 1/10user sẽ gặp lag rất tệ

- 1.000user/ngày →96user bứcxúc

- Họlà người tweet negative, churn
“Every 100ms of latency cost 1% of sales.”→optimizetail,khôngchỉav- erage. P99 / P99.9 là KPI chính thức tạiAmazon, Google, Meta. Lưu ý:Tail latencycompoundstrong agentic workflow nhiều bước — 5 bước, mỗi bướccóP99riêng →gầnnhưchắcchắn1bướcchạmtail. ĐoP99cho cảpipeline, khôngchỉ từng call. Giảngviên (VinUni) AICB· Monitoring 2026 18/ 96

---

<!-- chiron-source-span: {"source_span_id":"436b1805-d7a3-5f68-b88d-1ab44612645b","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Token& Cost Metrics —Output Đắt Hơn Input","extraction_method":"pdf-text-layer"},"checksum":"bdb3d9c64042baed6a6023f365ed0dacced0a6ce1623bf090ab8ffd6dc81a97e"} -->

## Slide 24 - Token& Cost Metrics —Output Đắt Hơn Input

Model(2026) Input$/1M Output $/1M Tỉ lệ out:in ClaudeHaiku 4.5 1 5 5x ClaudeSonnet 4.6 3 15 5x ClaudeOpus 4.8 5 25 5x OpenAIGPT-5.5 5 30 6x Gemini3.1 Pro 2 12 6x cost-per-task̸= cost-per-LLM-call — 1 task của agent có thể gọi LLM nhiều lần (plan + tool+synthesize). Đocosttheo taskvàrolluptheongày/user/feature,khôngchỉtheotừng call. Lưu ý:Output token đắt 5–6x input. Một agent “nói nhiều” tốn tiền hơn nhiều so với độ dài promptgợi ý⇒dashboardtoken phảitáchinput vs output. Giảngviên (VinUni) AICB· Monitoring 2026 19/ 96

---

<!-- chiron-source-span: {"source_span_id":"0b9eddd2-936d-5eb0-b36a-35881437f7bf","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"QualityMetrics — Kim Tự Tháp4 Tầng","extraction_method":"pdf-text-layer"},"checksum":"9da55c9d68138cfc6da4170cff095b993b61838ad326e9cc351241b20ccbfc00"} -->

## Slide 25 - QualityMetrics — Kim Tự Tháp4 Tầng

L4: Outcome Tasksuccess, revenue, retention L3: User Signal Thumbsup/down, CSAT,follow-up L2: LLM-as-Judge Relevance,faithfulness (RAGAS) L1: Automated Heuristic Format,length, toxicity,PII leak L1 rẻ, realtime nhưng không nói được quality thực. L4 là ground truth nhưng lag hàngtuần. Production cầncả 4: L1/L2 đểalert,L3/L4 đểconfirmtrend. Giảngviên (VinUni) AICB· Monitoring 2026 20/ 96

---

<!-- chiron-source-span: {"source_span_id":"8536b5af-6fad-5d52-bbf1-49fb2a7dda57","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Hallucination— Phát Hiện Thế Nào?","extraction_method":"pdf-text-layer"},"checksum":"aa6916c6bfd0bc5ed3bf013a85989df87682b5f5b0d21c93603b662690443cd4"} -->

## Slide 26 - Hallucination— Phát Hiện Thế Nào?

Hallucination — Agenttrảlời“rấttựtin”nhưngsaisựthật. Khôngcó1metricduy nhất→cầncombo 4 patterns. Mỗi claim trong output→ check có trong retrieved contextkhông. Tool: RAGAS faithfulness, TruLens. Gọi LLM 3 lần (temp 0.7); 3 câu mâu thuẫn→ nghi ngờ. Cost 3x→chỉsample 1%. Extract entities (tên, số, dates) → cross-check DB/API.Cho finance, medical. “Wasthishelpful?” +regenerateclick=tínhiệuhal- lucination. Chậm nhưng rẻvà thật. Lưu ý: Air Canada (2024): chatbot bịa chính sách bereavement fare. Nếu có groundednesscheck vớipolicy DB→blocktừ đầu, tránh kiện tụng. Giảngviên (VinUni) AICB· Monitoring 2026 21/ 96

---

<!-- chiron-source-span: {"source_span_id":"0dff2a5b-c884-572f-80f6-cada0a1746b8","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"QualityMetrics — Đo Cái KhóĐo","extraction_method":"pdf-text-layer"},"checksum":"8588822419d7b2b778d692e30324d1a9176c9c8ff1a3fd334f6b2d0efd7fead9"} -->

## Slide 27 - QualityMetrics — Đo Cái KhóĐo

Tínhiệu trực tiếp

- Hallucinationrate (bịa thông tin)

- Faithfulness/ groundedness (bám
nguồn)

- Task-completionrate
Tínhiệu gián tiếp (từ user)

- Thumbsup / down

- Regenerate/ rephrase rate

- Abandon/ escalate-to-human rate
Khôngthểchấmtaymọirequest. Sample1%→chấmbằngLLM-as-judge/RAGAS

- đẩythành 1 metric (gauge)→alertkhi tụt. Chitiết về eval có hệ thống:Day14.
Giảngviên (VinUni) AICB· Monitoring 2026 22/ 96

---

<!-- chiron-source-span: {"source_span_id":"498331d2-8712-50c4-9ea9-db21b12b61d5","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Tool-Call& Retrieval Metrics","extraction_method":"pdf-text-layer"},"checksum":"b25dc74759a5320999284c89d22af775b2c0a9e55fefed4b0a4ac896c5238d2a"} -->

## Slide 28 - Tool-Call& Retrieval Metrics

Toolcalls

- Successrate / schema-fail rate

- Timeoutrate

- Looprate (gọi lặp lại)

- Argshallucination (bịa tham số)
Retrieval(RAG)

- Recall@k(proxy)

- Empty-resultrate

- Chunkrelevance

- Retrievallatency
Đây là các failure moderiêng của agent. Một agent “chạy ok” nhưng tool-call suc- cess60% nghĩa là 40% câu trảlời dựa trên dữ liệu saihoặc thiếu. Giảngviên (VinUni) AICB· Monitoring 2026 23/ 96

---

<!-- chiron-source-span: {"source_span_id":"5d93c27a-6e82-51bf-9783-f925429da547","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Reliability— Error Taxonomy","extraction_method":"pdf-text-layer"},"checksum":"1a1323a4b2f64c431f7af402bc1e506c169dd39d20582e323edc29e7dcfad918"} -->

## Slide 29 - Reliability— Error Taxonomy

Loạilỗi Nguyênnhân Cáchhandle LLMAPI 5xx Providerdown / rate limit Retry exponential backoff, fall- backmodel LLMtimeout Slowprovider,network Circuit breaker, client timeout < server Toolcall failed ExternalAPI lỗi Retry,graceful degradation Toolschema invalid LLM sinh JSON lỗi Re-promptvới error feedback Guardrailblock Contentpolicy vi phạm Log + user-friendly message Emptyresponse LLMrefuse / filter Alternate prompt, escalate to hu- man Contextoverflow Input >limit Truncate,summarize history Track error_type trong mỗi log. Alert fire→ biết ngay gọi ai: LLM provider? tool owner? prompt engineer? “Error rate 5%”không có taxonomy = không fixđược. Giảngviên (VinUni) AICB· Monitoring 2026 24/ 96

---

<!-- chiron-source-span: {"source_span_id":"f334667f-8058-5a82-85f0-3b5a3220a6c8","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Drift— Khi Data/Model Thay ĐổiÂm Thầm","extraction_method":"pdf-text-layer"},"checksum":"54941c10a7c232661611eeab621aa82bdb5ab400657e84882e366a59e6d05cb1"} -->

## Slide 30 - Drift— Khi Data/Model Thay ĐổiÂm Thầm

3loại drift cần monitor

- Datadrift —input distribution đổi (user hỏi
kiểumới)

- Conceptdrift —mapping input→output
đổi(luật mới)

- Modeldrift —provider update model,
behaviorđổi Pháthiện: PSI, KL-divergence, embeddingdrift (cosine). PSI = ∑ i (pi−qi) ln pi qi < 0.1 stable · 0.1–0.25 mild · > 0.25 signifi- cant(cần retrain). Lưu ý:2024: OpenAI silently update GPT-4→ format output đổi→ nhiều pipeline breaksâm thầm. Khôngdrift monitoring = không biết chođến khi user bỏ đi. Giảngviên (VinUni) AICB· Monitoring 2026 25/ 96

---

<!-- chiron-source-span: {"source_span_id":"2280320d-cad1-59a5-b0e1-b6f711f86cf5","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"MetricNào Cho Ai?","extraction_method":"pdf-text-layer"},"checksum":"41f35a75127e707889db1018b9a3035f6a2e0d6614ba3de9f7ccfc5dd23bfd83"} -->

## Slide 31 - MetricNào Cho Ai?

Stakeholder Quantâm Metrics Engineering Systemhealth, debug Latency P95, error rate,tool-call failure Product Userexperience Satisfaction, task com- pletion, hallucination rate Finance/ Ops Costcontrol Cost/ngày, tokens/re- quest,cost by model Leadership ROIoverview Adoption, cost vs value,uptime Dashboard cho stakeholder phải nói bằngngôn ngữ business, không phải ngôn ngữ kỹ thuật. Giảngviên (VinUni) AICB· Monitoring 2026 26/ 96

---

<!-- chiron-source-span: {"source_span_id":"e48e07af-a667-5fbd-836d-36f6dc5f1e7f","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Structured Logging","extraction_method":"pdf-text-layer"},"checksum":"57c69467bc13a5bbb6c806fd8b0659bd6c7378018d79ed755ec8cd6f7879cb00"} -->

## Slide 32 - Structured Logging

04 Log không cấu trúc giống ghi chú tay — khó search, khó aggre- gate. Structured logging biến log thành DATA query được

---

<!-- chiron-source-span: {"source_span_id":"1d6d5f7a-99ae-575b-8cbc-db61e091e562","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Unstructuredvs Structured Log","extraction_method":"pdf-text-layer"},"checksum":"b3785f1b85595dc7ee5c8c136efaabf28d7c119b3c4651c7a8e278de6f15c9ee"} -->

## Slide 33 - Unstructuredvs Structured Log

# Unstructured: kho search / filter / aggregate # 10:23:45 INFO Agent responded 10:23:46 ERROR Tool failed # Structured JSON: query/aggregate/correlate duoc

```text
log = {
```
"ts": "2026-03-18T10:23:45Z", "level": "INFO", "correlation_id": "req-abc123", "event": "agent_response", "latency_ms": 1250, "input_tokens": 640, "output_tokens": 250, "cost_usd": 0.0057, "model": "claude-sonnet-4-6", } Query được như data:filter theo field, aggregate, correlate across services— điềutext log không làm được. Giảngviên (VinUni) AICB· Monitoring 2026 27/ 96

---

<!-- chiron-source-span: {"source_span_id":"f8635191-8535-57d3-a533-6084882e9197","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"LogGì Cho 1 LLM Call?","extraction_method":"pdf-text-layer"},"checksum":"db9b69b6912cd3e0c847f0b460f702ae071c6e3e22aef425b9057a7e147d6d2c"} -->

## Slide 34 - LogGì Cho 1 LLM Call?

- ✓ correlation_id(nối mọi log của 1request)

- ✓ model+ version, provider

- ✓ prompttemplate id (KHÔNG log rawprompt chứa PII)

- ✓ input_tokens/ output_tokens, latency_ms, TTFT

- ✓ toolcalls + kết quả (đãsanitize), finish_reason

- ✓ cost_usd(tính từ token)

- ✓ evalscore (nếu có), error +stack trace
Giảngviên (VinUni) AICB· Monitoring 2026 28/ 96

---

<!-- chiron-source-span: {"source_span_id":"e1b7eaf1-0110-5a16-b738-6cea2f17605c","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"LogGì Và Không Log Gì?","extraction_method":"pdf-text-layer"},"checksum":"ad3a8506b82d24b857af556580e9519dbc8f864acc3d99254ab585e8560d5e3a"} -->

## Slide 35 - LogGì Và Không Log Gì?

Nênlog

- Input(đã sanitize)

- Outputsummary

- Toolcalls + results

- Latency,tokens, cost

- Errors+ stack traces

- CorrelationID
KHÔNGlog

- PII(tên, SĐT,CCCD, email)

- Fullprompts chứa sensitive data

- APIkeys, tokens, secrets

- Rawuser data chưa sanitize

- Quánhiều DEBUG ở production
Lưu ý:Log PII = vi phạm PDPL (Việt Nam) / GDPR.Redact trước khi log, không phảisau khi bị audit. Chi tiết: §13. Giảngviên (VinUni) AICB· Monitoring 2026 29/ 96

---

<!-- chiron-source-span: {"source_span_id":"ed1fc47c-5a07-5001-9d19-568ea340be4f","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"PIIRedaction TrongThực Tế","extraction_method":"pdf-text-layer"},"checksum":"346155a4af4b58912cfe0b03ad29bbd87356c97a137a555cfa1e562cc22a47a6"} -->

## Slide 36 - PIIRedaction TrongThực Tế

Kỹthuật

- Regex: email, SĐT,thẻ, CCCD

- NER/ entity detection: tên người,
địachỉ (Microsoft Presidio)

- Hashing/ tokenization: giữ tính duy
nhất,bỏ giá trị gốc

- Allowlist: chỉ log fieldđã duyệt
OSS (MIT) của Microsoft: phát hiện 50+ loại PII (email, thẻ, SĐT, SSN...). Redact / mask / hash qua “operators”. Lưu ý: hỗ trợ tiếng Việt yếu — cần custom recog- nizercho CCCD/SĐT VN. Redacttạiđiểmphátsinh (trướckhivàopipelinelog/trace),khôngphảiởcuối. Nối vớiguardrails Day 11. Giảngviên (VinUni) AICB· Monitoring 2026 30/ 96

---

<!-- chiron-source-span: {"source_span_id":"6e3807b1-d44c-5ac1-9c8f-22e2edde65a7","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"LogLevels Đúng Cách","extraction_method":"pdf-text-layer"},"checksum":"e021d8cac85ef43575216ba1aaaf6ecaa70fc0381cda0d225bcd18b4f6d040bd"} -->

## Slide 37 - LogLevels Đúng Cách

Level Khinào dùng Vídụ DEBUG Devonly,rất chi tiết Full prompt, intermediate state INFO Normalflow,milestone Request received, re- sponsesent WARN Degradednhưng vẫn chạy Retrysucceeded,fallback used ERROR Failed,cần attention Tooltimeout, LLM error Productionchạy INFOlevel. Khidebugissuecụthể, tạmbậtDEBUG cho1requestID,xong tắtlại. Giảngviên (VinUni) AICB· Monitoring 2026 31/ 96

---

<!-- chiron-source-span: {"source_span_id":"eaa951eb-c5b9-5033-af9c-bfd78840588c","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"CorrelationID — Nối Tất CảLại","extraction_method":"pdf-text-layer"},"checksum":"11311c32f65bda1853279c9135687c3f51c7317c19f42224d82cbf42da62a03e"} -->

## Slide 38 - CorrelationID — Nối Tất CảLại

```text
import uuid
def handle_request(user_input):
req_id = str(uuid.uuid4())[:8] # 1 id cho toan bo request
log.info("request_received",
correlation_id=req_id,
input_length= len(user_input))
result = agent.run(user_input, req_id=req_id)
log.info("response_sent",
correlation_id=req_id,
latency_ms=result.latency,
output_tokens=result.output_tokens)
return result
```
CorrelationID nốimọi log entry của 1request, dù đi qua nhiều service. Nó cũng làmầmcủa trace_id —cầu nối sang distributed tracing(§5). Giảngviên (VinUni) AICB· Monitoring 2026 32/ 96

---

<!-- chiron-source-span: {"source_span_id":"09f31004-49af-5d14-a0c6-5dc86185e938","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"structlog+ contextvars — Correlation IDTự Động","extraction_method":"pdf-text-layer"},"checksum":"61f97c6fb7679bcb8450e6235fb9dd544a9be96c93b5c1c211ca90cce4d7abc5"} -->

## Slide 39 - structlog+ contextvars — Correlation IDTự Động

```text
import structlog, uuid
from structlog.contextvars import bind_contextvars, clear_contextvars
structlog.configure(processors=[
```
structlog.contextvars.merge_contextvars, # tu dong chen context structlog.processors.add_log_level, structlog.processors.TimeStamper(fmt= "iso", utc=True), structlog.processors.JSONRenderer(), # -> JSON moi dong ]) log = structlog.get_logger()

```text
async def handle_request(req):
clear_contextvars()
bind_contextvars(correlation_id= str(uuid.uuid4())[:8],
user_id=req.user_id, feature=req.feature)
```
# Tu day: moi log.* tu dong co 3 fields tren log.info("request_received", query_len= len(req.query))

```text
return await agent.run(req.query)
```
contextvars an toàn vớiasyncio — mỗi request có context riêng, không lẫn giữa concurrentrequests. Idiomproductionthaychoviệctruyền req_idthủcôngquamọi hàm(§5 nâng lêntrace_id). Giảngviên (VinUni) AICB· Monitoring 2026 33/ 96

---

<!-- chiron-source-span: {"source_span_id":"721f5af4-80c0-54ed-96e2-ad42f3916c76","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"LogSampling — Khi VolumeQuá Cao","extraction_method":"pdf-text-layer"},"checksum":"a729bcb804cc4d6a209a46377c1e8e99cb2d0ab79bcdcff94d114077cf6c0827"} -->

## Slide 40 - LogSampling — Khi VolumeQuá Cao

Bài toán — 100k req/ngày× 10 log/req = 1M entries/ngày. Datadog∼ $0.10/1k

- $100/ngàychỉ riêng log. Không scalable.
Strategies

- Head—quyết định ngay đầu trace (rẻ,
cóthể miss errors)

- Tail—quyếtđịnhsaukhixong(đắt,giữ
100%errors)

- Reservoir—giữ N mẫu uniform
100%ERROR+WARN ·10%INFO ·1%DEBUG · 100% request > 10s (tail-on-latency) · 100% cost > $1/req(outliers). Lưu ý:Sampling giảm cost 10–100x nhưng mất visibility vào normal pattern. Giữ 100%errors lànon-negotiable — đó là data debugquan trọng nhất. Giảngviên (VinUni) AICB· Monitoring 2026 34/ 96

---

<!-- chiron-source-span: {"source_span_id":"b6512dbe-90fb-5b12-a006-5f10ec281123","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"LogAggregation Stacks","extraction_method":"pdf-text-layer"},"checksum":"deddfe75adb3319a29081ea058e6d80a0c3ccd4a30c3ea14fcecf67301fb0195"} -->

## Slide 41 - LogAggregation Stacks

Stack Khinào dùng Cost/ tier ELK Full-text search mạnh, complex queries Tựhost, OSS Loki Label-based (giống Prometheus),rẻ Tựhost, OSS DatadogLogs Setupnhanh,alerttốt,đắtởscale SaaS ∼ $0.10/GB CloudWatch Đã ở AWS,tíchhợp IAM ∼ $0.50/GBingest BigQuery AnalyticsSQL, long retention ∼ $0.02/GBscan LangfusetựlàlogstorechoLLMcall(freetier). Devlocal: stdoutJSON+ jqlàđủ. Scaleupmớicần ELK/ Loki — đừng dựngcluster Elasticsearch cho MVP. Giảngviên (VinUni) AICB· Monitoring 2026 35/ 96

---

<!-- chiron-source-span: {"source_span_id":"7b0fe9df-f073-5e21-8c5b-7bd20da285c5","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"AuditLog — Tách Biệt VớiApp Log","extraction_method":"pdf-text-layer"},"checksum":"6692eb6e200bca113c995a86bcf7b2bdd0a3ea8cceffdcc64c63c2a0ff955cc1"} -->

## Slide 42 - AuditLog — Tách Biệt VớiApp Log

Audit log— Recordwho did what whencho compliance, legal, security — khác hẳnapp log dùng để debug. Applog

- Mụcđích: debug, performance

- Retention: 30–90 ngày

- Cóthể sample, sửa/xóa

- Truycập: devteam
Auditlog

- Mụcđích: compliance, forensics

- Retention: 2–7 năm (tùyngành)

- Khôngsample; append-only

- Truycập: restricted(compliance)
Lưuý: Trộnauditvàoapplog →khicầninvestigatebịthiếudata. Táchriêngtừngày đầu: S3bucketvới ObjectLock,hoặcdedicatedauditservice. LiênquanPDPL§13. Giảngviên (VinUni) AICB· Monitoring 2026 36/ 96

---

<!-- chiron-source-span: {"source_span_id":"722ede24-2792-515b-a6c5-62229a302b85","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Distributed Tracing Cho Agent","extraction_method":"pdf-text-layer"},"checksum":"93afeb9379eafd4395d2d6a77adde3f29f70c44299a4cc6611a4e257c660d798"} -->

## Slide 43 - Distributed Tracing Cho Agent

05 Log cho biết gì xảy ra ở từng bước; trace cho biết hành trình của 1 request qua LLM→ tool→ LLM và mất bao lâu ở mỗi bước

---

<!-- chiron-source-span: {"source_span_id":"52392b86-b7a6-529f-af86-b0cdfbfdaf9b","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Trace,Span, Parent–Child","extraction_method":"pdf-text-layer"},"checksum":"7818c1339bffca160768c3fa86b226d650669fb6778ed3beb8af8f846d6ac045"} -->

## Slide 44 - Trace,Span, Parent–Child

0ms 2500ms TotalRequest (trace): 2500ms Parse50ms Retrieval600ms LLMCall 1400ms Embed200ms Search350ms Generate1200ms Mỗihàng ngang là 1span. Tất cả spancủa 1 request tạo thành 1trace. Span con lồngtrong spancha. Nhìn tracebiết ngaybottleneckở đâu. Giảngviên (VinUni) AICB· Monitoring 2026 37/ 96

---

<!-- chiron-source-span: {"source_span_id":"eea0c815-cf23-5e99-a5c9-ab699ffd4383","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"TraceCho Agent Pipeline (Multi-StepLoop)","extraction_method":"pdf-text-layer"},"checksum":"0df1d637500b6e62f9427c242b4fe63c890b1621b779d35f922b1aca087216cf"} -->

## Slide 45 - TraceCho Agent Pipeline (Multi-StepLoop)

User Request LLM Plan Tool check_stock LLM Plan LLM Synthesize Response 400ms 600ms 300ms 1200ms Agent loop = chuỗi LLM↔tool. Trace cho thấy mỗi vòng tốn bao lâu. Ở đây 2 LLM callchiếm 64% latency⇒tốiưu prompt / model trước. Giảngviên (VinUni) AICB· Monitoring 2026 38/ 96

---

<!-- chiron-source-span: {"source_span_id":"d64fa239-abda-517e-873b-454e59e803b9","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"OpenTelemetry— Chuẩn TrungLập (Vendor-Neutral)","extraction_method":"pdf-text-layer"},"checksum":"4e6c71d82f063dce816e8f28ebf9061973b80ef62882da65d25703a494289c96"} -->

## Slide 46 - OpenTelemetry— Chuẩn TrungLập (Vendor-Neutral)

OpenTelemetry (OTel)— Chuẩn mở để sinh và xuất telemetry (traces, metrics, logs). Instrumentcode mộtlần bằngOTel→gửitới bấtkỳbackendnào (đổiback- endkhông sửa code). AIService (OTelSDK) OTel Collector Backend Langfuse/ Tempo/ Datadog Tránhvendorlock-in. Cùng1tracecóthểvàoLangfuse(UIchoLLM)vàTempo(lưu trữrẻ) song song. Giảngviên (VinUni) AICB· Monitoring 2026 39/ 96

---

<!-- chiron-source-span: {"source_span_id":"2323485f-9ec5-51e8-b3c0-9ee4c4ee751a","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"OTelGenAI Semantic Conventions (gen_ai.*)","extraction_method":"pdf-text-layer"},"checksum":"bb0b0fed9179d4913765682b7eebc8e2266cd07469973d152c13359099f8ac35"} -->

## Slide 47 - OTelGenAI Semantic Conventions (gen_ai.*)

Attribute Ýnghĩa gen_ai.operation.name chat/ execute_tool / invoke_agent gen_ai.provider.name openai/ anthropic (thay gen_ai.system cũ) gen_ai.request.model modelđược yêu cầu gen_ai.usage.input_tokens inputtokens (thay prompt_tokens) gen_ai.usage.output_tokens outputtokens (thay completion_tokens) gen_ai.response.finish_reasons ["stop"], ["length"] gen_ai.tool.name têntool (trên execute_tool span) Lưu ý: Vẫn ở trạng thái Development (experimental) giữa 2026 — tên attribute còn có thể đổi. Tên cũ prompt_tokens/completion_tokens/gen_ai.system đãdeprecated nhưng nhiều tutorial cũvẫn dùng. Giảngviên (VinUni) AICB· Monitoring 2026 40/ 96

---

<!-- chiron-source-span: {"source_span_id":"691bd21c-24a9-5d4f-8e48-f54581d91c2c","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"Đọc1 TraceMulti-Step","extraction_method":"pdf-text-layer"},"checksum":"8cf799025993282eeaaeb7de04a5cb0fd2bd4b3eecf6d44225e29691fbd6156e"} -->

## Slide 48 - Đọc1 TraceMulti-Step

# Span tree cua 1 agent run (ten span = "{operation} {model/tool}") invoke_agent ecommerce-agent 2500ms |- chat claude-sonnet-4-6 (plan) 400ms |- execute_tool check_stock 600ms <-- cham! |- chat claude-sonnet-4-6 (plan) 300ms '- chat claude-sonnet-4-6 (synthesize) 1200ms # Doc: tong 2500ms; check_stock 600ms la I/O cham, # 2 lan synthesize chiem 1600ms -> toi uu prompt/model truoc. Đọctrace=đọccâyspan: bướcnàolâunhất,bướcnàolỗi,bướcnàolặp. Đâylàkỹ năngdùng lại ở §11(debug incident). Giảngviên (VinUni) AICB· Monitoring 2026 41/ 96

---

<!-- chiron-source-span: {"source_span_id":"791d36f3-812c-5cee-9eeb-1be9ded94f04","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Sampling— Giữ TraceNào?","extraction_method":"pdf-text-layer"},"checksum":"88194388669b38ff6c2e4fba117e2f3e31d9c23fce6cdc9a86dbe1c25fdea8fa"} -->

## Slide 49 - Sampling— Giữ TraceNào?

Quyết định giữ/bỏngay đầurequest (vd giữ10%). Rẻ,đơngiản,nhưngcóthểbỏ sóttrace lỗi. Quyết địnhsau khi xongrequest: luôn giữ trace lỗi / chậm, sample bớt trace “bình thường”. Thông minh hơn, tốn bufferhơn. Lưuý: Labgiữ100%(datanhỏ). Khiscale,samplinglàcáchgiảmchiphílưutrace —nhưng đừngbao giờ sample bỏ trace lỗi. Giảngviên (VinUni) AICB· Monitoring 2026 42/ 96

---

<!-- chiron-source-span: {"source_span_id":"283f754b-f2ab-5aeb-a01f-869075907c6f","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"Trace,Span, Context — Terminology","extraction_method":"pdf-text-layer"},"checksum":"bac683ef912f144f768b6aa34a36601612632d97079af6e9171408c97c7b7e0d"} -->

## Slide 50 - Trace,Span, Context — Terminology

Kháiniệm cốt lõi

- Trace—toàn bộ request end-to-end,
có trace_id duynhất

- Span—1 đơn vị công việc, có
span_id, parent_span_id

- Contextpropagation —truyền
trace_id quaboundaries (HTTP header,queue) name (vd llm.generate) · start_time, duration · attributes (model, tokens) · status (OK/ER- ROR) · events (log gắn vào span)· links (vd retry). Trace=cây. Rootspan =entrypoint(HTTPrequest). Childspans =cácbướccon (RAGretrieve, LLM call, tool call). Nhìn cây biết bottleneck. Giảngviên (VinUni) AICB· Monitoring 2026 43/ 96

---

<!-- chiron-source-span: {"source_span_id":"659b2806-934b-5eb6-8bd2-76d93e7994bd","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"4Bottleneck Patterns TrongTrace","extraction_method":"pdf-text-layer"},"checksum":"7824eef6885acedff3260646ca373dd318fc5d66bd23755f846f48921048ee48"} -->

## Slide 51 - 4Bottleneck Patterns TrongTrace

A→B→C, tổng = sum. Fix: parallelize A, B nếu khôngphụ thuộc. LoopgọiAPI/DBnhiềulần →nhiềuspanngắncùng tên. Fix: batch / pre-fetch. Span dài nhưng CPU idle (LLM API, DB, network). Fix: parallelize, cache, timeout. Nhiều span retry trong 1 trace; backoff quá ngắn, không jitter. Fix: exponential backoff + circuit breaker. Nhìn span dài nhất→ “parallelize được không?”. Nhìnnhiều span ngắn lặp→ “batchđược không?”. Haicâu hỏi này giải quyết phầnlớn bottleneck. Giảngviên (VinUni) AICB· Monitoring 2026 44/ 96

---

<!-- chiron-source-span: {"source_span_id":"41fedc59-4b1d-59d0-a437-e17e4e5e7cb3","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"Bộ Công Cụ LLM-Observability","extraction_method":"pdf-text-layer"},"checksum":"23a4571c4978202794d0dc745dfe48ff01bf59ca6e0bc4bbfbaf359a08ec8aa7"} -->

## Slide 52 - Bộ Công Cụ LLM-Observability

06 2026 Có cả một hệ sinh thái — chọn đúng theo nhu cầu: open-source hay SaaS, dùng framework gì, self-host hay cloud

---

<!-- chiron-source-span: {"source_span_id":"1a0cdf4b-d7de-5138-bb7c-6edc49023ed0","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"BảnĐồ Công Cụ","extraction_method":"pdf-text-layer"},"checksum":"24ae12ef481ab8fdeea3ce9afe81b30deb27a71fa8e64d1b12d6768b39351384"} -->

## Slide 53 - BảnĐồ Công Cụ

Tool Kiểu Mạnhở License/ Note LangSmith SaaS(self-host EE) Eval, trajectory, prompt hub Devfree 5k traces/th Langfuse OSSself-host + cloud Tracing, cost, prompt mgmt MIT,self-host free Phoenix(Arize) OSSself-host Tracing + eval, notebook→prod ElasticLicense 2.0 Helicone Proxy/gateway1-dòng Cost, cache Apache-2.0, mainte- nancemode ’26 OpenLLMetry OTelauto-instrument Vendor-neutral, mọi backend Apache-2.0 Bắt đầu MVP:Langfuse (free, self-host hoặc cloud). Cần eval/trajectory sâu & đã dùng LangChain:LangSmith. Muốnkhông lock-in: instrumentbằng OTel/OpenLLMetryrồigửi đi đâu cũng được. Giảngviên (VinUni) AICB· Monitoring 2026 45/ 96

---

<!-- chiron-source-span: {"source_span_id":"41bb797a-3df7-5c60-a786-fc00eb9c811e","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"Langfusevs LangSmith","extraction_method":"pdf-text-layer"},"checksum":"30d1163b37f59dba81194ab763ebbf8eb8901def8c7a6e2635f568e2202ce2f4"} -->

## Slide 54 - Langfusevs LangSmith

Langfuse

- Opensource (MIT),self-host miễn
phí

- CloudHobby: 50k units/thángfree

- Framework-agnostic

- SDKPython v4(2026),OTel-based

- Tracing,cost, prompt mgmt, eval
LangSmith

- SaaS;self-host chỉEnterprise

- Devfree: 5k traces/tháng,14 ngày

- Hoạtđộng độc lập (không buộc
LangChain)

- Mạnh: eval +trajectoryeval,
prompthub

- Onlineeval production-ready
Giảngviên (VinUni) AICB· Monitoring 2026 46/ 96

---

<!-- chiron-source-span: {"source_span_id":"0bb18e9f-a0d0-5c96-ad92-646c976de680","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"LangfuseIntegration — Vài Dòng Code(SDK v4, 2026)","extraction_method":"pdf-text-layer"},"checksum":"9b6c455f1ca5fbe5bf428204a518855f29fabbf6d94263e269f5de7e8342afb2"} -->

## Slide 55 - LangfuseIntegration — Vài Dòng Code(SDK v4, 2026)

# Cach 1: drop-in OpenAI wrapper (it code nhat)

```text
from langfuse.openai import openai # chi doi import
resp = openai.chat.completions.create(
model= "gpt-4o", messages=[{ "role": "user", "content": "Hi"}])
```
# -> tu dong capture prompt, output, latency, tokens, cost # Cach 2: decorator cho ham bat ky (van la idiom hien hanh)

```text
from langfuse import observe
@observe(as_type= "generation")
def call_llm(prompt):
return agent.run(prompt)
Lưu ý: SDK Python hiện làv4 (3/2026), dựa trên OpenTelemetry. @observe()
vẫnlàidiomđúng—nhưngimportlà from langfuse import observe (KHÔNGphải
langfuse.decorators kiểuv2 cũ).
Giảngviên (VinUni) AICB· Monitoring 2026 47/ 96
```

---

<!-- chiron-source-span: {"source_span_id":"21101e4e-ea5a-5cee-860f-b0fe5ab21934","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"LLMGateway — Quan Sát +Cost Một Chỗ","extraction_method":"pdf-text-layer"},"checksum":"716d0a61a5d2ccf3e611e3eb83f0f5057f0de6088c4026b31181d665556c0e88"} -->

## Slide 56 - LLMGateway — Quan Sát +Cost Một Chỗ

LLM Gateway / Proxy— Một lớp đứng trước mọi LLM call (đổibase_url). Tập trung observability, cost tracking, caching, rate-limit, budget — cho nhiều provider quamộtinterface. OSS, 1 API kiểu OpenAI cho 100+ model. Budget/rate-limit theo key/team/user; “bud- gethết →chặn”. Gateway thương mại: observability + guardrails + semantic cache. Helicone tích hợp1 dòng (đang maintenance mode). Gateway=điểmnghẽn(choke-point)đểápcost&policymộtchỗ,thayvìrảiráctrong code. Giảngviên (VinUni) AICB· Monitoring 2026 48/ 96

---

<!-- chiron-source-span: {"source_span_id":"c347ae59-be76-5dbe-ad71-6e8afffe5762","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"ChọnCông Cụ Nào Khi Nào?","extraction_method":"pdf-text-layer"},"checksum":"58d7868bb6ae737b78450a9964fab3d638c62a97a9024a435e93aaf6a2bdca01"} -->

## Slide 57 - ChọnCông Cụ Nào Khi Nào?

```text
■ MVP/ lab / startup: Langfuse free tier(cloud) hoặc self-host docker — đủtracing + cost +
```
dashboard.

- Đãdùng LangChain/LangGraph, cần eval sâu: LangSmith.

- Cầndata ở lại on-prem /VN (compliance): self-host Langfuse hoặcPhoenix.

- Khôngmuốn lock-in: instrument bằng OTel(OpenLLMetry)→đổibackend tùy ý.

- Tậptrung cost nhiều provider: thêm LLM gateway(LiteLLM).
Lưu ý:Đừng tự build observability từ đầu khi free tier đã đủ. Build dashboard customsau khicó đủ data và biếtcâu hỏi cần trả lời. Giảngviên (VinUni) AICB· Monitoring 2026 49/ 96

---

<!-- chiron-source-span: {"source_span_id":"cd4ab603-eb41-54e5-8b86-ab345cac0cc6","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"DecisionFramework — Chọn ToolThế Nào?","extraction_method":"pdf-text-layer"},"checksum":"6227a413065cbce9b09e02fe5afbee430d2dead3824be9c5799c40ed0ffb3a89"} -->

## Slide 58 - DecisionFramework — Chọn ToolThế Nào?

Q1: Teamsize? Q3: Existing stack? Q5: Skill set? 1–5: SaaS free tier Datadog: stay + AIaddon Python-heavy: Langfuse 5–50: SaaS paid LangChain: LangSmith Infra ops: Grafana 50+: hybrid/self-host Agnostic: Langfuse Non-dev: Datadog Q2: Compliance? Q4: Budget/tháng? Q6: Evaluation? HIPAA/PCI:self-host $0: Langfuse cloud free Quality: Phoenix/Lang- Smith GDPR/PDPL: EU/VN re- gion $100–500: Lang- Smith/Helicone Costonly: Helicone None: bất kỳ $500+: Datadog full Fullstack: Langfuse Lưuý: Khôngcó“besttool”,chỉcóbesttoolcho team+usecase+budget củabạn. Đừngcopystack củaFAANG— họ cóinfra team 50 người. Giảngviên (VinUni) AICB· Monitoring 2026 50/ 96

---

<!-- chiron-source-span: {"source_span_id":"aa44186f-594f-554c-b583-1f196ee8d2c1","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"Production Stack: Prometheus +","extraction_method":"pdf-text-layer"},"checksum":"beea6a83d8b10a54d9317a05c1e68c004b5639c29282d22fbb12e5857afc8bf7"} -->

## Slide 59 - Production Stack: Prometheus +

07 Grafana + OTel Prometheus thu metrics, Grafana vẽ dashboard, OTel Collector kết nối tất cả — bộ stack open-source kinh điển, nay có thêm lớp LLM

---

<!-- chiron-source-span: {"source_span_id":"c0d21381-afdc-5f6a-a52f-e4c5d5025aa2","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"KiếnTrúcStack","extraction_method":"pdf-text-layer"},"checksum":"6ebf19f644c83d8006962c888b1434e5e6968668fb1e6b73c397bc123e2ce075"} -->

## Slide 60 - KiếnTrúcStack

AIService OTelSDK OTel Collector Prometheus (metrics) Loki (logs) Tempo (traces) Grafana (dashboards) Langfuse (LLMUI) Instrument 1 lần (OTel)→ Collector fan-out: metrics→Prometheus, logs→Loki, traces→Tempo,Grafanavẽ tất cả; Langfuse nhận traceLLM song song. Giảngviên (VinUni) AICB· Monitoring 2026 51/ 96

---

<!-- chiron-source-span: {"source_span_id":"48018d2a-9d7c-5c48-9e40-2b5778e81eb9","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"Prometheus: Metric Types+ Pull Model","extraction_method":"pdf-text-layer"},"checksum":"2459e54f8157575b33ee46428d8eb4bef3d13027613aca869c36e3e635c75c92"} -->

## Slide 61 - Prometheus: Metric Types+ Pull Model

Type Dùngcho Counter Chỉtăng(requests,errors, tokens) Gauge Lên/xuống (active reqs, queuedepth, eval score) Histogram Phân phối (latency → P50/P95/P99) Prometheus scrape /metrics của ser- vicemỗi15s(khôngphảiservicepush).

### PromQLví dụ
histogram_quantile(0.95,...) cho P95. Counter/Gauge cho con số đơn; Histogram chia bucket để tính P95/P99 — thứ bạn cầncho latency SLO. Giảngviên (VinUni) AICB· Monitoring 2026 52/ 96

---

<!-- chiron-source-span: {"source_span_id":"33424e76-a43a-5bf1-a0fb-da2e662cbe4c","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Instrument1 AI Service (prometheus_client)","extraction_method":"pdf-text-layer"},"checksum":"14ae6df9e799e5278864a75656f80d3a67ac02f4d8022fd957e68ab7dd0f93ae"} -->

## Slide 62 - Instrument1 AI Service (prometheus_client)

```text
from prometheus_client import Counter, Histogram, start_http_server
REQS = Counter( "agent_requests_total", "Requests", [ "model", "status"])
LAT = Histogram( "agent_latency_seconds", "Latency", [ "model"])
TOKS = Counter( "agent_tokens_total", "Tokens", [ "model", "direction"])
def handle(req, model):
with LAT.labels(model=model).time(): # do latency -> histogram
resp = agent.run(req)
REQS.labels(model=model, status= "ok").inc()
TOKS.labels(model=model, direction= "output").inc(resp.output_tokens)
return resp
start_http_server(8000) # expose /metrics cho Prometheus scrape
```
Lưu ý: Giữ label cardinality THẤP: model/status ok; đừng đặt user_id hay request_id làmlabel — sẽ nổ số series(xem slide sau). Giảngviên (VinUni) AICB· Monitoring 2026 53/ 96

---

<!-- chiron-source-span: {"source_span_id":"4e06f8db-dd03-5bde-a172-7e26d8fcd8eb","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"Cardinality: Kẻ Đốt TiềnThầm Lặng","extraction_method":"pdf-text-layer"},"checksum":"c9c45e17b4b6340fd147ae1973e9672331831fa208c605068cb70e95daf18d53"} -->

## Slide 63 - Cardinality: Kẻ Đốt TiềnThầm Lặng

Cardinality — Sốtổhợpgiátrịlabelcủa1metric. Mỗitổhợp=1time-seriesriêng phảilưu. Label giátrị tự do (user_id, request_id, rawprompt)→bùngnổ series. LabelAN TOÀN(thấp)

- model, status, tool_name

- direction (in/out)
LabelNGUY HIỂM (cao)

- user_id, request_id

- prompt, session_id
Lưu ý:Bài học thật: Coinbase từng nhận hóa đơn Datadog$65 triệu(2022), phần lớn do custom metrics cardinality cao. High-cardinality thuộc vềlogs/traces, không phảimetric label. Giảngviên (VinUni) AICB· Monitoring 2026 54/ 96

---

<!-- chiron-source-span: {"source_span_id":"edce0251-6d59-5a75-b882-33cc95096a15","locator":{"kind":"page","page":64,"label":"Slide 64","section_title":"GrafanaDashboard-as-Code","extraction_method":"pdf-text-layer"},"checksum":"566f574031ace10a78a7955304cd02595e0b1d8e260f7935152bc27cb3055839"} -->

## Slide 64 - GrafanaDashboard-as-Code

# Dashboard luu duoi dang JSON/YAML, version trong git -> review qua PR # provisioning/dashboards/agent.yaml apiVersion: 1

### providers
- name: agent-dashboards
folder: "AI Agents" type: file

### options
path: /var/lib/grafana/dashboards # JSON dashboards o day Dashboardtronggit=cóversion,reviewquaPR,táitạođược,không“clickchuộtrồi mất”. Cùng triết lývới IaC ở Day 12. Giảngviên (VinUni) AICB· Monitoring 2026 55/ 96

---

<!-- chiron-source-span: {"source_span_id":"4291322f-c956-5c0a-b318-95830eecf48b","locator":{"kind":"page","page":65,"label":"Slide 65","section_title":"Self-Hostvs SaaS vs LLM-Tool","extraction_method":"pdf-text-layer"},"checksum":"89fc0f31aa9637bddf06104fa3392d179d892a400f8f86de1638d9f245e6541f"} -->

## Slide 65 - Self-Hostvs SaaS vs LLM-Tool

Lựachọn Khinào Đánhđổi Prometheus+Grafana (self-host) Có infra ops, muốn kiểm soát+ rẻ ở quy mô Tự vận hành, tự build LLMview Datadog / New Relic(SaaS) Cầnnhanh, có budget Đắt khi scale (cardinal- ity!) Langfuse / Phoenix (LLM- tool) Cần LLM-native (trace, cost,eval) Bổ sung, không thay metricstack Nhiều team dùngkết hợp: Prometheus/Grafana cho metric hạ tầng + Langfuse cho LLM trace/cost. OTellà lớp keogiữa chúng. Giảngviên (VinUni) AICB· Monitoring 2026 56/ 96

---

<!-- chiron-source-span: {"source_span_id":"04faed6a-aaf8-5e4d-b710-989883074324","locator":{"kind":"page","page":66,"label":"Slide 66","section_title":"Dashboard Design","extraction_method":"pdf-text-layer"},"checksum":"33e38297193df73c80756eea82d7a5e553e0b6cdb2360fd76bee50d2b31ab945"} -->

## Slide 66 - Dashboard Design

08 Mỗi stakeholder một câu hỏi, một dashboard — nhồi mọi thứ vào một màn hình là cách chắc chắn không ai nhìn

---

<!-- chiron-source-span: {"source_span_id":"4d05ff64-9daa-53f2-b28a-3a114789aec9","locator":{"kind":"page","page":67,"label":"Slide 67","section_title":"Dashboard— 3 Layers","extraction_method":"pdf-text-layer"},"checksum":"1deda6d43ad12db5d6b22400e907aef5c54543e9737286948b0fdb4462f1fb8e"} -->

## Slide 67 - Dashboard— 3 Layers

Layer1: Overview —Health, uptime, key alerts Layer2: Detail —Latency,cost, error rate, tokens Layer3: Drill-down —Traces,log search, root cause Choleadership Choengineering Chodebugging Mỗistakeholderchỉnhìn1layer. Leadershipcầnoverview,khôngcầntrace. Engineer cầndrill-down, không cần revenue chart. Giảngviên (VinUni) AICB· Monitoring 2026 57/ 96

---

<!-- chiron-source-span: {"source_span_id":"468ed4cf-4919-51c6-8551-5bc3088e150e","locator":{"kind":"page","page":68,"label":"Slide 68","section_title":"6Panel Bắt Buộc Cho AIService","extraction_method":"pdf-text-layer"},"checksum":"1344d58fe2e34f4dcaa7361f004e815e4bff2f2283311bb85d86d1aebdab6517"} -->

## Slide 68 - 6Panel Bắt Buộc Cho AIService

1. Request rate (traffic)

2. Latency P50/P95/P99+ TTFT

3. Error rate (bytype)

4. Cost / token usage(in/out)

5. Tool-call successrate

6. Quality / eval score(sampled) Sovớiservicethường,agentthay“CPU/GPUpanel”bằng tool-callsuccess vàeval score—vì failure mode của agent nằmở đó. Giảngviên (VinUni) AICB· Monitoring 2026 58/ 96

---

<!-- chiron-source-span: {"source_span_id":"eb6805cf-df8a-5584-9255-9a9a385a2d5f","locator":{"kind":"page","page":69,"label":"Slide 69","section_title":"PanelTypeNào Khi Nào?","extraction_method":"pdf-text-layer"},"checksum":"224118ac46be61d2b12a4984ba818045d5eed2781a53cc802f353a7f12348da8"} -->

## Slide 69 - PanelTypeNào Khi Nào?

Paneltype Dùngcho Vídụ Timeseries (line) Trendtheo thờigian Latency P95, cost/ngày Stat/ single value 1 con số hiện tại Uptime%, error rate Heatmap Phânphối theo thời gian Latency distribution Table Top-N,breakdown Costbymodel/feature Lưu ý:Một dashboard = một câu hỏi. Tối đa 6–9 panel/màn. Nhiều hơn nữa thì không ai đọcđược — tách thành dashboardriêng. Giảngviên (VinUni) AICB· Monitoring 2026 59/ 96

---

<!-- chiron-source-span: {"source_span_id":"237945b4-dfe3-520d-aa8e-e7f3346e2bde","locator":{"kind":"page","page":70,"label":"Slide 70","section_title":"DashboardTools","extraction_method":"pdf-text-layer"},"checksum":"90cfb72c1311494b2e052e51e5f5b05dd0c4fdbfbe5ea5942f68031f7996657f"} -->

## Slide 70 - DashboardTools

Open source, mạnh. Kết nối mọi data source.Khi nào: teamcó infra ops. LLM-native: trace, cost, eval sẵn. Khi nào: cần LLM dashboard nhanh choMVP. All-in-one SaaS. Nhanh,

### đắt khi scale. Khi nào
cầnnhanh, có budget. Lưu ý: Cho lab: Langfuse dashboardđủ cho MVP. Đừng dành thời gian build Grafanacustom trước khi có đủ data. Giảngviên (VinUni) AICB· Monitoring 2026 60/ 96

---

<!-- chiron-source-span: {"source_span_id":"2d70e80a-1b4d-5d8d-98bd-df3f953d5620","locator":{"kind":"page","page":71,"label":"Slide 71","section_title":"DashboardAnti-patterns — 5 Điều NênTránh","extraction_method":"pdf-text-layer"},"checksum":"24ecc3691a05a32af84631fdd913f0a47f6044a8700cb827522008a36d40509a"} -->

## Slide 71 - DashboardAnti-patterns — 5 Điều NênTránh

1. “Wallof metrics”—30 panel, không ai nhìnhết. Giới hạn 6–8panel/layer.

2. Timerangemặcđịnhquádài —default1giờchoops,khôngphải1tháng(chemấtspike).

3. Khôngcó baseline/threshold line—P95 = 2.1s tốt hayxấu? Luôn vẽ đườngSLO lên chart.

4. Metrickhông có đơn vị/context—“Cost: 1250” làgì? USD? ngày? Luôn label đầy đủ.

5. Khôngauto-refresh —ops dashboard cần realtime (15–30s);monthly report thì khác. Đưa dashboard cho người ngoài team xem 30s→ họ nói được “hệ thống OK” hay “có vấn đềở X” không? Nếu không, redesign. Giảngviên (VinUni) AICB· Monitoring 2026 61/ 96

---

<!-- chiron-source-span: {"source_span_id":"c941a255-3dbf-52a0-877f-b75e482599fe","locator":{"kind":"page","page":72,"label":"Slide 72","section_title":"Alerting & SLO","extraction_method":"pdf-text-layer"},"checksum":"4cd9f6096682b077801f43040ae03348b8d3ed9182609a2456488d09a90c8455"} -->

## Slide 72 - Alerting & SLO

09 Metrics chỉ có giá trị nếu có người nhìn. Alert sai cách còn tệ hơn không có. SLO cho bạn một ngân sách lỗi để quyết định khi nào cần lo

---

<!-- chiron-source-span: {"source_span_id":"eba7ee2a-cdbf-5daf-824e-579642c45ae0","locator":{"kind":"page","page":73,"label":"Slide 73","section_title":"AlertRules Cho AI Agent","extraction_method":"pdf-text-layer"},"checksum":"8c96fdc6bd3827f1f5dcca52d293bb228e75c0dee844229ed2470763e7c90130"} -->

## Slide 73 - AlertRules Cho AI Agent

Metric Threshold Severity Channel LatencyP95 >5 giây Warning Slack Errorrate >5% Critical Slack+ Email Dailycost >budget ngày Critical Email+ SMS Tool-callfailure >10% Warning Slack Evalscore tụt> 10% Warning Slack Uptime <99% Critical PagerDuty Alertphải actionable. Nếu nhận alertmà không biết làm gì, alertđó cần redesign hoặc bỏ. Giảngviên (VinUni) AICB· Monitoring 2026 62/ 96

---

<!-- chiron-source-span: {"source_span_id":"2e12f85b-b4f6-5001-a3fa-f89cba3d0056","locator":{"kind":"page","page":74,"label":"Slide 74","section_title":"Symptom-Basedvs Cause-Based Alerting","extraction_method":"pdf-text-layer"},"checksum":"9921daf9e1e93e6c61989ef57dbfea0b5351a96969030afc335999a63b0f00e6"} -->

## Slide 74 - Symptom-Basedvs Cause-Based Alerting

Symptom-based(NÊN page) Alerttrên cáiusercảm nhận được.

- Errorrate / latency vượt SLO

- “Câutrả lời sai tăng vọt”

- Ítfalse positive, luôn thật
Bốn golden signals: Latency, Traffic, Er- rors,Saturation. Cause-based(để DEBUG) Alerttrên nguyênnhân cóthể.

- “CPU80%”, “cache miss cao”

- Cóthể chưa ảnh hưởng user

- Nhiềunoise nếu để page
Dùng cho chẩn đoán, không phải để gọi người. Giảngviên (VinUni) AICB· Monitoring 2026 63/ 96

---

<!-- chiron-source-span: {"source_span_id":"8ee410cf-7517-58e1-8fbd-54422002cebf","locator":{"kind":"page","page":75,"label":"Slide 75","section_title":"AlertFatigue — Khi Alert QuáNhiều","extraction_method":"pdf-text-layer"},"checksum":"2e26d71fe600a97e23f918ce81e579b089c29b329b4f9f4e14ff9ededf0dc9ac"} -->

## Slide 75 - AlertFatigue — Khi Alert QuáNhiều

Alertfatigue xảy ra khi

- quánhiều alert không quan trọng

- mọingười bắt đầu ignore

- alertthật bị lẫn trong noise

- teammất tin tưởng hệ thống
Cáchtránh (Google SRE)

- chỉpage khi cầnhànhđộng ngay

- mỗipage phải đòitrítuệ (không
robotic)

- pagevề vấn đềmới,chưa từng thấy

- phầncòn lại→ticket/ dashboard
Lưu ý:Nếu team ignore alert thường xuyên, hệ thống alerting đangtệ hơn không có. Nguy hiểm nhất: 1 page thật bịche lấp trong noise. Giảngviên (VinUni) AICB· Monitoring 2026 64/ 96

---

<!-- chiron-source-span: {"source_span_id":"9940f657-ee4b-5e75-895d-3e6b06bdbc67","locator":{"kind":"page","page":76,"label":"Slide 76","section_title":"SLI/ SLO / SLA —Định Nghĩa Chính Xác","extraction_method":"pdf-text-layer"},"checksum":"d5e9fa80ea53c70ee0d183cebf8d393848be232b52b459e2be4b68ac0840b924"} -->

## Slide 76 - SLI/ SLO / SLA —Định Nghĩa Chính Xác

SLI — Indicator —

### con số bạn đo. Vd
% request < 5s; error rate. SLO — Objective — mục tiêu cho SLI. Vd: 99.9% request < 5s/tháng. SLA — Agreement — hợp đồngcó hậu quả nếu miss (hoàn tiền, phạt). Hỏi “điều gì xảy ra nếu không đạt?” Không có hậu quả rõ ràng⇒ đó là SLO, không phảiSLA. SLI = số đo, SLO= mục tiêu, SLA = lờihứa. Giảngviên (VinUni) AICB· Monitoring 2026 65/ 96

---

<!-- chiron-source-span: {"source_span_id":"dc3ca402-9b31-518e-9008-b31b3b1c04fe","locator":{"kind":"page","page":77,"label":"Slide 77","section_title":"ErrorBudget — Math Cụ Thể","extraction_method":"pdf-text-layer"},"checksum":"b02dd0b613c7785530564e1ab753ed797656939fe929b8622036dc6f8fd4a3c5"} -->

## Slide 77 - ErrorBudget — Math Cụ Thể

Error budget— = (1−SLO)× cửa sổ thời gian. Đó là “ngân sách lỗi” bạn được phéptiêu. Còn budget→shipnhanh; hết budget→đóngbăng, lo độ ổn định. SLO Downtime/tháng (30 ngày) 99.5% 3.6giờ (216 phút) 99.9% 43.2phút ←“threenines” 99.95% 21.6phút Page khiburn 14.4x trong 1h(tiêu 2% budget) hoặc6x trong 6h(5%); mởticket khi 1x trong3 ngày. Long+short window = vừa chính xácvừa reset nhanh. Giảngviên (VinUni) AICB· Monitoring 2026 66/ 96

---

<!-- chiron-source-span: {"source_span_id":"4e3eeba9-d11f-5cce-b467-929253833903","locator":{"kind":"page","page":78,"label":"Slide 78","section_title":"On-CallCơ Bản","extraction_method":"pdf-text-layer"},"checksum":"40ac543bbf744a8ac4772299fee98881a6356693cec46b82d04d3b8a4b05cba2"} -->

## Slide 78 - On-CallCơ Bản

Severity& escalation

- SEV1(down/critical) →pagengay

- SEV2(degraded) →Slack,giờ làm

- SEV3(minor) →ticket

- Escalation: primary→secondary→
lead MTTD = thời gian phát hiện.MTTR = thời

### gian khắc phục. Mục tiêu observability
giảmcả hai. Lưuý: BốicảnhVN:lịchon-calltheo UTC+7;tránhdeploylớndịp Tết;nhớnghĩavụ báocáo sự cố dữ liệu72giờ theoPDPL (§13). Giảngviên (VinUni) AICB· Monitoring 2026 67/ 96

---

<!-- chiron-source-span: {"source_span_id":"f9974df4-909a-5f09-9daa-422563324a7e","locator":{"kind":"page","page":79,"label":"Slide 79","section_title":"Multi-WindowMulti-Burn-RateAlerting","extraction_method":"pdf-text-layer"},"checksum":"0f331fc8cdff4b12793d6824bbe7939e931ea8aa16c1e4d9ad7c1c9264df4576"} -->

## Slide 79 - Multi-WindowMulti-Burn-RateAlerting

Bàitoán — Alertđơn“error > 1%trong5phút” →firequánhanh(noise)hoặcquá chậm(miss incident). Giảipháp Google: kết hợp2 window với 2 burn rate. Severity Shortwin Longwin Burn rate (vs SLO) Page(critical) 5phút 1giờ 14.4x Ticket(warn) 30phút 6giờ 6x “14.4x”: giữmứcnàythìburnhếterrorbudgetthángtrong2ngày. Alertfirekhi cả2window cùngvượt→shortreactnhanhvớispikethật,longfilternoisengắn. (GoogleSREWorkbook Ch.5.) Giảngviên (VinUni) AICB· Monitoring 2026 68/ 96

---

<!-- chiron-source-span: {"source_span_id":"231bf496-ff85-5548-8365-ed2a87b6e503","locator":{"kind":"page","page":80,"label":"Slide 80","section_title":"AlertAnatomy — Alert Tốt CóGì?","extraction_method":"pdf-text-layer"},"checksum":"04b2481c426783382b389a21d6dfae4e472299cb0b3320f30f469215cad203dc"} -->

## Slide 80 - AlertAnatomy — Alert Tốt CóGì?

### Templatecho mỗi alert

- Titlerõ: “[P1] Agent P95latency> 5scho feature=summary ”

- Severity: P1 (page ngay)/ P2 (giờ hành chính) /P3 (ticket)

- Impact: “5% user đangbị chậm> 5s”

- Currentvalue: “P95 = 6.3s,bình thường 1.8s, threshold 5s”

- Dashboardlink (pre-filtered)+ Tracelink (top10 chậm nhất)

- Runbooklink (playbookfix) +On-callowner
Lưuý: Alertkhôngcó runbook=alertkhôngthểxửlýlúc3hsáng. Viếtrunbooklàmộtphần củawork “tạo alert”, không phảinice-to-have. Giảngviên (VinUni) AICB· Monitoring 2026 69/ 96

---

<!-- chiron-source-span: {"source_span_id":"4a8c223c-d513-59ca-8604-3d4b3c86f886","locator":{"kind":"page","page":81,"label":"Slide 81","section_title":"Cost Monitoring & Optimization","extraction_method":"pdf-text-layer"},"checksum":"bbacf942b98444e0ed699d0be960fde4405209e7085653bba43c4b1de22f6789"} -->

## Slide 81 - Cost Monitoring & Optimization

10 Token cost là dòng chi phí lớn nhất và dễ mất kiểm soát nhất của một AI agent — phải đo như một metric hạng nhất

---

<!-- chiron-source-span: {"source_span_id":"3b7589f7-36a8-571e-acd8-1d70d9e625f3","locator":{"kind":"page","page":82,"label":"Slide 82","section_title":"VìSao Cost Là First-Class Metric","extraction_method":"pdf-text-layer"},"checksum":"3fa2dc90a0c0224d5c7d38b7fb0caf775cd676c4607e9974ff6ca955dd54fe2e"} -->

## Slide 82 - VìSao Cost Là First-Class Metric

CostAI khác cost phần mềm

- Tỉlệ vớitoken,không phải request

- Mộtloop bug đốt budget trong vàigiờ

- Outputđắt 5–6x input

- Costtăng tuyến tính với traffic
Tokens (in/out), cost/request, cost/task, cost/ngày,cost/user,cost/feature,cachehit rate. Rollup + dailybudget alert. Haiku$1/$5·Sonnet$3/$15·Opus$5/$25·GPT-5.5$5/$30·Gemini3.1Pro$2/$12 (mỗi1M token in/out). Chọn đúng model là đòn bẩycost lớn nhất. Giảngviên (VinUni) AICB· Monitoring 2026 70/ 96

---

<!-- chiron-source-span: {"source_span_id":"b7b2775a-0e78-5bf3-8925-c79e1c0cc75a","locator":{"kind":"page","page":83,"label":"Slide 83","section_title":"ĐoCost Ở Đâu Và ThếNào","extraction_method":"pdf-text-layer"},"checksum":"1a45cb718a475839d090fe6df5f5b12d9d2e8ced6eadb011fc04c977aa047edd"} -->

## Slide 83 - ĐoCost Ở Đâu Và ThếNào

Côngthức — cost = input_tokens 106 ×Pin[model] + output_tokens 106 ×Pout[model]

- Tínhcost tạimỗi LLM calltừtoken usage (provider trả về sẵn)

- Gắnnhãn theo model / feature /user→rolluptheo ngày

- Setdailybudget alert: cost hôm nay> ngưỡng→báongay

- Theodõi cachehit ratenhưmột cost SLI
Lưu ý:Cost-per-LLM-call rẻ (∼$0.005) nhưng một agent task gọi nhiều lần. Luôn rollup— con số đáng lo làtổng theo ngày/user,không phảitừng call. Giảngviên (VinUni) AICB· Monitoring 2026 71/ 96

---

<!-- chiron-source-span: {"source_span_id":"eb2374c7-6ea2-5991-b1aa-3a859bca7a3e","locator":{"kind":"page","page":84,"label":"Slide 84","section_title":"4Chiến Lược Giảm Cost","extraction_method":"pdf-text-layer"},"checksum":"0483661eb5a1b568f29210167e655c3ab44025561c98a3bbd27eede2a98a6dc1"} -->

## Slide 84 - 4Chiến Lược Giảm Cost

Dùng model nhỏ nhất đủ tốt cho mỗi bước. HaikurẻhơnOpus5x. Route: việc dễ→modelrẻ. Bớtfew-shotthừa,tómtắtlịchsử,chỉđưa contextcần thiết (RAG top-k nhỏ). Câu hỏi gần giống→ trả lời từ cache, khônggọi LLM.∼70%hit cho FAQ. Cache system prompt / tool defs / RAG context dùng lại→ cache read rẻ 90% (Anthropic). Mỗichiếnlượccầnmộtmetric: cost-by-model,promptlength, cachehitrate. Không đothì không biết có hiệu quả. Giảngviên (VinUni) AICB· Monitoring 2026 72/ 96

---

<!-- chiron-source-span: {"source_span_id":"6f74c8e3-04e3-5e3c-92e1-40d29e8eae59","locator":{"kind":"page","page":85,"label":"Slide 85","section_title":"SemanticCache + Prompt Cache","extraction_method":"pdf-text-layer"},"checksum":"768c227569b6879de29b645eef68beaef2bd3b8b1189cc0b4bbabc440e6ffae6"} -->

## Slide 85 - SemanticCache + Prompt Cache

Semanticcache — Embedcâuhỏi → socosinevớicâucũ →trùng(vd ≥ 0.8) thì trả lời từ cache. Benchmark: hit ∼60–70%,giảmcost ∼70%,nhanhhơn nhiều. Prompt cache (prefix) — Provider cache phần đầu prompt lặp lại. An- thropic: cache read =0.1xgiá input (rẻ 90%), write 1.25x/2x. OpenAI tự động, Gemini90% (2.5+). Lưu ý:Semantic cache đánh đổiđộ chính xác: ngưỡng similarity quá thấp→ trả lời cũ/sai cho biến thể tinh tế. Phải theo dõi cache hit ratevà chất lượng câu trả lời từcache. Giảngviên (VinUni) AICB· Monitoring 2026 73/ 96

---

<!-- chiron-source-span: {"source_span_id":"466c1ffc-a798-57f7-abf7-04e5f8e7ee9f","locator":{"kind":"page","page":86,"label":"Slide 86","section_title":"CostAnti-Patterns","extraction_method":"pdf-text-layer"},"checksum":"527942344a9da06d74566c42fbdb78b876d22f089b7a04524c094d8fb3ac85c3"} -->

## Slide 86 - CostAnti-Patterns

Lưu ý: Không tách input vs output

- khôngthấyoutput(đắt5–6x)làthủ
phạm. Lưu ý:Không có cost-per-feature→ khôngbiết feature nào đốt tiền. Lưu ý: “Đo mọi thứ” với label car- dinality cao → bill observability nổ (Coinbase$65M). Lưuý: Khôngcódailybudgetalert → pháthiện khi nhận hóa đơn. Quan sát chính nó cũng tốn tiền (lưu metric/log/trace). Cân bằng: đủ telemetry để trảlời câu hỏi, không nhiều đếnmức bill quan sát vượt billLLM. Giảngviên (VinUni) AICB· Monitoring 2026 74/ 96

---

<!-- chiron-source-span: {"source_span_id":"3b7984fc-4b97-5db5-98af-869370cf4484","locator":{"kind":"page","page":87,"label":"Slide 87","section_title":"CostAttribution — TiềnĐi Đâu?","extraction_method":"pdf-text-layer"},"checksum":"ee9ad69343def30148e087ae9b7a9a999e0537fc7e25f4ba1ea320e92f3db95c"} -->

## Slide 87 - CostAttribution — TiềnĐi Đâu?

Dimension Taggắn vào trace Dùngđể... Peruser user_id Biếtpower user,tính pricing Perfeature feature="summary" Prioritizeoptimization Permodel model="sonnet-4-6" Sosánh cost/value các model Pertenant tenant_id Multi-tenantbilling Perenv env="prod" Táchdev/staging noise Percohort plan="enterprise" Marginanalysis Mọi LLM call phải cóuser_id + feature + model. Thiếu 1 trong 3→ khi CFO hỏi “$50k tháng này ai tốn?” bạn không trảlời được, và ngân sách bịcắt. Giảngviên (VinUni) AICB· Monitoring 2026 75/ 96

---

<!-- chiron-source-span: {"source_span_id":"e78209ef-4e4d-512c-b367-0c689e3c8f00","locator":{"kind":"page","page":88,"label":"Slide 88","section_title":"CaseStudy — Notion AI CostOptimization","extraction_method":"pdf-text-layer"},"checksum":"95f8f1c1d66ff3619cd2f7784a2227d89207972168620ddcee5eeeee01a48668"} -->

## Slide 88 - CaseStudy — Notion AI CostOptimization

Bốicảnh — NotionAIphụcvụhàngtriệuuser(summary,Q&A,writingassist). Cost

### OpenAIban đầu∼30%revenue. Monitoring insight

- 70%queries là “summarize” với promptgiống nhau

- 15%user chiếm 60% cost (powerusers, doc dài)

- Regeneraterate cao ở feature “writingassist”
Actions(theo thứ tự ROI):promptcache system prompt (−40%input)→route“summary” qua modelnhỏ(Haikutier, −60%)→per-userratelimitchofreetier →cảithiệnprompt“writingassist” (−35%regenerate). Cost/MAU giảm58% trong3tháng,khônggiảmquality. Làmđượcvìcómonitoring chitiết theofeature+ user + model(xemCost Attribution). Giảngviên (VinUni) AICB· Monitoring 2026 76/ 96

---

<!-- chiron-source-span: {"source_span_id":"3477d042-d9b9-50c2-9000-36536f3126c5","locator":{"kind":"page","page":89,"label":"Slide 89","section_title":"Debug 1 Incident Bằng Trace","extraction_method":"pdf-text-layer"},"checksum":"d8d1cf87997996ab5cd911533ecfb3c470fbeef3a5b3177f0de4bc44d7290ff3"} -->

## Slide 89 - Debug 1 Incident Bằng Trace

11 Khi có observability, bạn tìm root cause trong vài phút thay vì vài ngày — đi từ metric, tới log, tới trace

---

<!-- chiron-source-span: {"source_span_id":"6186099a-2b90-57b0-ad13-86353228a572","locator":{"kind":"page","page":90,"label":"Slide 90","section_title":"SựCố: “Agent ChậmGấp Đôi Từ Sáng Nay”","extraction_method":"pdf-text-layer"},"checksum":"4d9467aee5c48f93a900644133a4660a48e456eeae9d35c3744e38e7d2dc073b"} -->

## Slide 90 - SựCố: “Agent ChậmGấp Đôi Từ Sáng Nay”

User báo agent phản hồi rất chậm từ 9h sáng. Không có deploy nào rõ ràng. Bạn bắtđầu từ đâu?

- Sailầm thường gặp: lao vào đọclog thô của hàng nghìn request.

- Đúng: bắtđầutừ metric(khoanhvùng) →log(lọctheocorrelation_id) →trace(tìm
bướcchậm). Metric trả lời “có gì đó chậm, từ khi nào”. Log trả lời “request nào”. Trace trả lời “chậmở bước nào” — đây làlý do cần cả ba. Giảngviên (VinUni) AICB· Monitoring 2026 77/ 96

---

<!-- chiron-source-span: {"source_span_id":"1a527833-3dca-5208-85dc-9bae35ee8517","locator":{"kind":"page","page":91,"label":"Slide 91","section_title":"Bước1–2: Metric KhoanhVùng→LogLọc","extraction_method":"pdf-text-layer"},"checksum":"8ad0e2f2f85dc8baa5d34e106e53bbcdc650c5be0a180bde04094ba7fdf941f5"} -->

## Slide 91 - Bước1–2: Metric KhoanhVùng→LogLọc

Dashboard: P95latencynhảytừ2.5s →5s lúc9h. Token/requestkhôngđổi. Errorrate bình thường. ⇒ không phải LLM, không phảilỗi — là một bướcnào đó chậm đi. Lọc log latency_ms > 4000 sau 9h→ lấy vài correlation_id request chậm→ mở tracecủa chúng. Mỗi pillar thu hẹp không gian tìm kiếm cho pillar sau. Từ “cả hệ thống”→ “request này”→“spannày”. Giảngviên (VinUni) AICB· Monitoring 2026 78/ 96

---

<!-- chiron-source-span: {"source_span_id":"367274c2-e95e-5a5f-be49-e066c99057cb","locator":{"kind":"page","page":92,"label":"Slide 92","section_title":"Bước3: Mở TraceCủa 1 Request Chậm","extraction_method":"pdf-text-layer"},"checksum":"a4cbab5f9e8691c5e9dfd66fa0dde737150c5179ee395278d3aadfd2d70a3577"} -->

## Slide 92 - Bước3: Mở TraceCủa 1 Request Chậm

### # Trace HOM NAY cua 1 request cham
invoke_agent ecommerce-agent 5100ms (truoc: 2500ms) |- chat claude-sonnet-4-6 (plan) 400ms |- execute_tool rag_retrieve 2800ms <== ROOT CAUSE | (truoc: 600ms) |- chat claude-sonnet-4-6 (plan) 300ms '- chat claude-sonnet-4-6 (synthesize) 1400ms # LLM van binh thuong. rag_retrieve cham 4.6x -> dieu tra vector store. Không có trace: bạn đoán mò giữa LLM, network, tool. Có trace: thấy ngay rag_retrieve làthủ phạm trong 30 giây. Giảngviên (VinUni) AICB· Monitoring 2026 79/ 96

---

<!-- chiron-source-span: {"source_span_id":"d6d27945-1a47-524e-a684-0b49e3d11d07","locator":{"kind":"page","page":93,"label":"Slide 93","section_title":"RootCause + Fix + Postmortem","extraction_method":"pdf-text-layer"},"checksum":"bd7e7d330c80294ed0293c2e670159241f4af78b78aa62058bee2a51d4852e06"} -->

## Slide 93 - RootCause + Fix + Postmortem

Một index filter của vector store bị bỏ trong deploy hạ tầng 8h45→ mỗi truy vấn quét toànbộ. Khớp đúngthời điểm P95 nhảy. Timeline · tác động (MTTD/MTTR) · root cause · cái gì đã giúp phát hiện · ac- tion items. Trách hệ thống, không trách người. Cùngquytrìnhmetric →log→tracedùngchomọiincident. Observabilitytốt=MTTD vàMTTR thấp. Giảngviên (VinUni) AICB· Monitoring 2026 80/ 96

---

<!-- chiron-source-span: {"source_span_id":"1a4b8742-f4a4-524f-9cb0-e7ddfcac9315","locator":{"kind":"page","page":94,"label":"Slide 94","section_title":"BàiHọc Từ Sự Cố Thật(2024–2025)","extraction_method":"pdf-text-layer"},"checksum":"cd7b3d9e5b4fd98489e30dbf3ac84a3ee370bc2b6de142751d1f7e0d04fbea80"} -->

## Slide 94 - BàiHọc Từ Sự Cố Thật(2024–2025)

- ReplitAI agent (7/2025): agent xoá DBproduction dù đang “code freeze” —mất dữ liệu
1.206lãnh đạo + 1.196 côngty. Tệ hơn: agentbịa4.000user giả và nói rollbackbất khả thi (thựcra rollback được).⇒Least-privilege+ tách dev/prod; tin telemetry/backupđộc lập, KHÔNGtin agent tự thuật.

- AirCanada (Moffatt v. Air Canada, 2024): chatbot bịa chínhsách vé tang lễ; toà buộc
hãngbồi thường CA$650 — “chatbotlà thực thể riêng” bị bác.⇒Câutrả lời sai = trách nhiệmpháp lý; phải monitor chấtlượng output.

- Klarna: dồn AI thay700 agent rồiquayxe thuêlại người vì chất lượng.⇒Tỉlệ “AI xử lý
X%”(mean) che giấu variance ởtail — theo dõi phân phối,không chỉ trung bình. Giảngviên (VinUni) AICB· Monitoring 2026 81/ 96

---

<!-- chiron-source-span: {"source_span_id":"051fa843-e4bc-519a-a003-43dd2e3dbea0","locator":{"kind":"page","page":95,"label":"Slide 95","section_title":"Human Feedback & Online Eval","extraction_method":"pdf-text-layer"},"checksum":"b430c86c77e8121c1c78c0148660056e1309c8b83660dccd0f237d11535b2f8c"} -->

## Slide 95 - Human Feedback & Online Eval

12 Trong Production Pillar thứ 4 khi vận hành: đo chất lượng trên dữ liệu thật, liên tục, để bắt suy thoái trước khi user bỏ đi

---

<!-- chiron-source-span: {"source_span_id":"3113be66-cd65-5735-958c-c75be34c3d2c","locator":{"kind":"page","page":96,"label":"Slide 96","section_title":"OfflineEval vs Online Eval","extraction_method":"pdf-text-layer"},"checksum":"10f9d9ed1b5818f0f2cf94ba2033cc37f0755e2bfa713697c9fe79eb4c296420"} -->

## Slide 96 - OfflineEval vs Online Eval

Offline(Day 14)

- Testsetcốđịnh,expectedanswers

- Chạytrước khi ship (CI gate)

- Bắtregression
Online(Day 13)

- Trafficthật, không có groundtruth

- Chạyliên tục trên production

- Bắtsuy thoái + drift
Modelkhông“crash”khisuythoái—nóvẫntrả200OK.Chỉonlineeval(pillar4)mới pháthiện chất lượng tụt trên dữliệu thật. Giảngviên (VinUni) AICB· Monitoring 2026 82/ 96

---

<!-- chiron-source-span: {"source_span_id":"d6f878d7-5de3-51af-9384-2d58a029cbb7","locator":{"kind":"page","page":97,"label":"Slide 97","section_title":"ThuHuman Feedback","extraction_method":"pdf-text-layer"},"checksum":"38b184def11ebcd940f469f8e6c1fb080611fbbd67ae75314eb15f3b411a0516"} -->

## Slide 97 - ThuHuman Feedback

Thumbs up/down, rating sao, “câu trả lời nàycóhữuích?”. Rõràngnhưngtỉlệphản hồithấp. Regenerate, copy, rời đi, hỏi lại, escalate- to-human. Nhiều tín hiệu,cần diễn giải. Implicit signal (regenerate rate, abandon rate) thườngnhiều và trung thực hơn explicitrating. Log cảhai, gắn vào trace. Giảngviên (VinUni) AICB· Monitoring 2026 83/ 96

---

<!-- chiron-source-span: {"source_span_id":"e54da9ac-cc65-5011-bdd1-b49ffe203c7a","locator":{"kind":"page","page":98,"label":"Slide 98","section_title":"Eval-as-MetricLoop","extraction_method":"pdf-text-layer"},"checksum":"85f2e2c8270cfbb2b6b698b230146056e4aa656bc644b2d8b5cdfbfb0d0d5e29"} -->

## Slide 98 - Eval-as-MetricLoop

Sample1% production LLM-judge /RAGAS Gauge metric Alertnếu tụt Lấymẫunhỏ →chấmtựđộng →đẩythànhgaugetrêndashboard →alertkhigiảm. Chấtlượng trở thành metric như latency. Lưu ý:LLM-judge cũng tốn tiền→ sample (1%) thay vì chấm 100%. Đây là lý do “đochất lượng” phải cân với cost(§10). Giảngviên (VinUni) AICB· Monitoring 2026 84/ 96

---

<!-- chiron-source-span: {"source_span_id":"f92800a2-fbbc-53e3-9f53-f80f46aadda9","locator":{"kind":"page","page":99,"label":"Slide 99","section_title":"Feedback→Dataset→CảiThiện (và Cẩn Trọng)","extraction_method":"pdf-text-layer"},"checksum":"fe76bc7c5c1bf3f52e9f9cf80d1976423e56f5db1fb2070f3eb5a4733ffa2ef5"} -->

## Slide 99 - Feedback→Dataset→CảiThiện (và Cẩn Trọng)

Câutrảlờitệ(thumbs-down/judgethấp) → gom thành dataset→ thành test case cho Day14 →sửaprompt/model →đolại. Lưu ý: Judge drift: LLM-judge cũng thayđổitheothờigian/phiênbản. Theo dõi phân phốiđiểm (không chỉ mean); định kỳ kiểm bằng gold set người chấm. Observability→eval→cảithiện→observability. ĐâylàvònglặpsảnphẩmAItrưởng thành. Giảngviên (VinUni) AICB· Monitoring 2026 85/ 96

---

<!-- chiron-source-span: {"source_span_id":"e4e2f30f-5fb0-59c4-83d5-66c7059ef65b","locator":{"kind":"page","page":100,"label":"Slide 100","section_title":"Privacy & Compliance Khi Log","extraction_method":"pdf-text-layer"},"checksum":"aa8a31f4767511993cac9f014840bb8c279630c4ecf8946bff3dd9cbe2dc510c"} -->

## Slide 100 - Privacy & Compliance Khi Log

13 Privacy & Compliance Khi Log- ging Log và trace là nơi PII rò rỉ nhiều nhất — full tracing vô tình biến hệ thống quan sát thành một kho dữ liệu cá nhân

---

<!-- chiron-source-span: {"source_span_id":"078d5052-24c1-57a6-9b1f-6e3c10a2efe6","locator":{"kind":"page","page":101,"label":"Slide 101","section_title":"VìSao AI Logging Rủi RoPII Cao","extraction_method":"pdf-text-layer"},"checksum":"fffb108fe352eba8ed69b8ec621e2a36e98569acb76bdd5c78b2257de33a10a1"} -->

## Slide 101 - VìSao AI Logging Rủi RoPII Cao

- Usergõ tựdo vàoprompt: tên, SĐT,CCCD,bệnh án, thông tin tài chính

- Fulltracing capturecảprompt lẫn output→khoPII ngoài ý muốn

- Trace/logthường gửi sangSaaSnước ngoài(Datadog,LangSmith) = chuyển dữ
liệuxuyên biên giới Lưu ý:Trong OTel GenAI semconv,gen_ai.tool.call.arguments và prompt/com- pletionlà opt-inđúngvì lý do PII — mặcđịnh KHÔNG capture nội dung nhạycảm. Giảngviên (VinUni) AICB· Monitoring 2026 86/ 96

---

<!-- chiron-source-span: {"source_span_id":"a5d3995f-9d05-5fe5-b9c4-f244abad1cc2","locator":{"kind":"page","page":102,"label":"Slide 102","section_title":"PIITrongLogs/Traces—Làm Gì","extraction_method":"pdf-text-layer"},"checksum":"f917d0d2d6e1f7138543fa2a45dc4b890656f2b2a0d51ea6c4d5fb8139531c24"} -->

## Slide 102 - PIITrongLogs/Traces—Làm Gì

Kỹthuật

- Redact/ mask tại điểm phát sinh

- Allowlistfield được log

- Logtemplateid,không log raw prompt

- Hashđịnh danh thay vì lưu gốc
Microsoft Presidio (detect + anonymize), guardrails Day 11, OTel content-capture opt-in. Tự viết recognizer cho CCCD/SĐT VN. Khôngcapturecáibạnkhôngcần. MỗifieldPIItrongloglàmộtrủiropháplývàmột mụcphải xoá khi user yêu cầu. Giảngviên (VinUni) AICB· Monitoring 2026 87/ 96

---

<!-- chiron-source-span: {"source_span_id":"8728c7b9-4504-5fc8-9ac2-2c0c591de395","locator":{"kind":"page","page":103,"label":"Slide 103","section_title":"Retention,Access & Audit","extraction_method":"pdf-text-layer"},"checksum":"49296cd3a217ed3488d7dca659fe778a5dc3f942c6ab8b4b2f7bae0c69c3ba15"} -->

## Slide 103 - Retention,Access & Audit

Đặt TTL theo loại data. Trace chi tiết: ngắn (7–30

### ngày). Metric tổng hợp
dài. Retention dài = tốn tiền+ rủi ro. Ai xem được log/trace chứa data người dùng? RBAC+ chỉ cấp khi cần. Ghi lại ai truy cập teleme- try. Hỗtrợquyềnxoá/truy cậpcủa user. Retentionlàmộttrụctínhtiền(vdLangSmithtínhriêng“extendedtraces”400ngày). Giữít hơn, lâu hơn một cáchcó chủ đích. Giảngviên (VinUni) AICB· Monitoring 2026 88/ 96

---

<!-- chiron-source-span: {"source_span_id":"9f37fb60-67ab-57bf-a4c7-32b6effd22a5","locator":{"kind":"page","page":104,"label":"Slide 104","section_title":"Compliance: ViệtNam +Quốc Tế","extraction_method":"pdf-text-layer"},"checksum":"546c815215f4bb8f7e3e1e054749b5b3dda1cfdca09bf515ccf2bec888910abf"} -->

## Slide 104 - Compliance: ViệtNam +Quốc Tế

- ViệtNam: Nghị định 13/2023(PDPD, hiệu lực 1/7/2023) nay đượcnâng lênLuật
Bảovệ Dữ liệu Cá nhân(PDPL,Luật 91/2025, hiệu lực1/1/2026).

- Báocáo vi phạm dữ liệu trong72giờ tớiBộ Công an (A05). Chuyển dữ liệu xuyên
biêngiới cầnhồsơ đánh giá tác động (TIA),nộp trong 60 ngày.

- Phạtnặng: vi phạmchuyển xuyên biên giới có thểtới5%doanh thunămtrước.

- Quốctế: GDPR (EU), PDPA(Singapore/khu vực) — nguyên tắctương tự.
Lưu ý:Gửi log/trace chứa PII của user VN sang observability SaaS nước ngoài = chuyểndữ liệu xuyên biên giới→cầnhồ sơ + cơ sở pháplý. Đi sâuởDay24. Giảngviên (VinUni) AICB· Monitoring 2026 89/ 96

---

<!-- chiron-source-span: {"source_span_id":"57b9f9eb-9b07-5e7a-8d01-af28e828d0e7","locator":{"kind":"page","page":105,"label":"Slide 105","section_title":"Checklist, Lab & Tổng Kết","extraction_method":"pdf-text-layer"},"checksum":"c214aaf5de929256d4fcfcbf4c514babbf9127ecd9cf7df280d7100cf3f2d66d"} -->

## Slide 105 - Checklist, Lab & Tổng Kết

14 Mục tiêu cuối: agent deployed có observability đầy đủ — bạn biết nó chạy thế nào mà không cần hỏi user

---

<!-- chiron-source-span: {"source_span_id":"9d83fe39-2d77-58b6-bac8-13a4447c01a8","locator":{"kind":"page","page":106,"label":"Slide 106","section_title":"MonitoringChecklist","extraction_method":"pdf-text-layer"},"checksum":"016633a06f454219a5523640032080a2efedb307831e5d89dcc4b4b737e67e55"} -->

## Slide 106 - MonitoringChecklist

Logging

- ✓ StructuredJSON, correlation ID □✓ PIIredacted, log levels đúng
Metrics

- ✓ LatencyP50/95/99 + TTFT □✓ Tokenin/out + cost □✓ Tool-callsuccess
Tracing

- ✓ Traceper request (span tree) □✓ OTel gen_ai.* attributes
Alerting& SLO

- ✓ ≥ 3alertactionable □✓ 1SLO + error budget □✓ Symptom-basedpaging
Cost& Privacy

- ✓ Dailybudget alert □✓ Cachehit rate □✓ Retention+ cross-border check
Giảngviên (VinUni) AICB· Monitoring 2026 90/ 96

---

<!-- chiron-source-span: {"source_span_id":"8e00d681-3ec6-53c2-bdcb-9a2522a0795a","locator":{"kind":"page","page":107,"label":"Slide 107","section_title":"Lab#13","extraction_method":"pdf-text-layer"},"checksum":"d7f3154e19d1a1869d61fdeb14efdbbc4fa6879ddf95474650caa25049651a30"} -->

## Slide 107 - Lab#13

Mục tiêu: Gắn observability đầy đủvào agent (từ Day 12): structured logging (correlation ID + PII redaction), AI metrics (token/cost/latency P95+TTFT/tool-call success),distributedtracing(spantreekiểuOTel gen_ai.*),gửitớibackend(Lang- fusehoặc backend zero-key offline),dashboard+ alert + 1 SLO. Deliverable: Monitoringstackchạyđược: ≥ 10traces,dashboard6panel, ≥ 3alert rule→Slack,1 SLO + error budget, 1incident note đọc từ trace thật. Thờigian: ∼2giờ Giảngviên (VinUni) AICB· Monitoring 2026 91/ 96

---

<!-- chiron-source-span: {"source_span_id":"8d94f8e7-4a1d-5a79-91a2-cea0b86c52fa","locator":{"kind":"page","page":108,"label":"Slide 108","section_title":"ArtifactCần Nộp","extraction_method":"pdf-text-layer"},"checksum":"f679ba5debe5f3bf2500fe15a42bc1ffaa8885b0abfe570832f724548566800a"} -->

## Slide 108 - ArtifactCần Nộp

Logging& Tracing

- StructuredJSON logs + correlation
ID

- Input/outputđã redact PII

- Trace(≥ 10): span tree đọcđược

- Cost& token per request
Dashboard,Alert & SLO

- Dashboard: latency,cost,errors,
tool-success

- ≥ 3alertrule + 1 SLO/error budget

- Screenshotdashboard có data

- 1incident note
(metric→log→trace) Lưu ý: Không cần enterprise monitoring. Cần chứng minh bạnbiết agent đang chạythế nàomàkhông phải hỏi user. Giảngviên (VinUni) AICB· Monitoring 2026 92/ 96

---

<!-- chiron-source-span: {"source_span_id":"f7124851-9c8c-5800-a8f5-5d815c5aae9f","locator":{"kind":"page","page":109,"label":"Slide 109","section_title":"Observathon— Cuộc Thi Observability (Capstone)","extraction_method":"pdf-text-layer"},"checksum":"a3b294332718af2f5527df4bda044dbf2a9adc727949d9806de6b31b74c391ed"} -->

## Slide 109 - Observathon— Cuộc Thi Observability (Capstone)

Một agent e-commercehộp đen, im lặng, đầy bug(không phát log/metric/trace). Muốnthắng: tựgắn observabilityđểbắt bug rồi sửa. Nộp3 thứ

- Findings: bug gì +bằng chứng

- Configđãsửa (agent mis-config)

- Wrapper: retry/cache/route/guardrail
Điểm= 1 con số

- correctness+ LLM-eval quality

- latency/ cost / error /drift↓

- +thưởng theo chẩn đoán
Đội,∼4h. Publictest(giờ2,leaderboard) →private(3.5h,held-out+1bugẩn)xếp hạng. Nộp quagitpush;model tự do (mock / local/ cloud). Giảngviên (VinUni) AICB· Monitoring 2026 93/ 96

---

<!-- chiron-source-span: {"source_span_id":"1ac0b469-dec8-560f-a70d-79c3eca4131e","locator":{"kind":"page","page":110,"label":"Slide 110","section_title":"7Anti-patterns Từ Industry","extraction_method":"pdf-text-layer"},"checksum":"092f3a9382296879f800ccf636623f2b2efbc8f53e7b39ebafc171a2bdf66143"} -->

## Slide 110 - 7Anti-patterns Từ Industry

1. “We’lladd monitoring later”—later = never. Add ngay từ MVP.

2. Logfull prompts + responses—vi phạm GDPR/PDPL, storage billnổ. Sanitize + sample.

3. Alerttrên mọi metric “quan trọng”—50 alert→alertfatigue →ignore.

4. Khôngcó runbook—alert fire 3h sáng, engineertrẻ lost, escalate lên senior.

5. Monitoringdev ̸=prodconfig —prod có issue không reproduceđược vì dev khác setup.

6. Chỉđo performance, quên cost—đến cuối tháng mới biếtđốt tiền.

7. Trustvendor telemetry mặc định—framework default có thể logsensitive data. Đọc docs trướckhi deploy. Lưuý: Anti-pattern#1phổbiếnvàtaihạinhất. Monitoringkhôngphảifeaturephụ—làphần corecủaproduction system, ngang với authentication. Giảngviên (VinUni) AICB· Monitoring 2026 94/ 96

---

<!-- chiron-source-span: {"source_span_id":"8a871082-03c5-569f-a555-6eef89bb6301","locator":{"kind":"page","page":111,"label":"Slide 111","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"f9a26ec7a55f65fcafcf405af0a6a462e6ec9ed14a5a83a4cb70ef950bffbc2c"} -->

## Slide 111 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 4pillars. Metrics+logs+traces+ eval(cònđúngkhông). Chỉlogslàkhôngđủ;AIcầnpillar thứ4. 2 AI-specific metrics. Token & cost (output đắt 5–6x input), P95 + TTFT, tool-call success. “HTTP200” khác “trả lời đúng”. 3 Logging+tracing. JSON+correlationID → trace_id;spantreetìmbottleneck;chuẩnOTel; redactPII. 4 Alert+SLO+cost. Pagetheosymptom&SLOburn,khôngtheocause. Đocostnhưmetric hạngnhất; cache để giảm. 5 Onlineeval. Sample →judge →gauge →alert. Debug incident: metric→log →trace. Giảngviên (VinUni) AICB· Monitoring 2026 94/ 96

---

<!-- chiron-source-span: {"source_span_id":"05f89f66-e7aa-54bb-a1c7-869690b25ca5","locator":{"kind":"page","page":112,"label":"Slide 112","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"dca0d7ffb8bb968bc5e7ad11feb05d7f35ce5f209932e97edb3ccd784f0158af"} -->

## Slide 112 - Tiếptheo & Bài tập

AIEvaluation & Benchmarking “Day 13 đo “chất lượng có còn đúng không” trên production. Day 14: đo “tốt đến đâu” một cách có hệ thống — sếp hỏi agent hơn ChatGPT bao nhiêu,bạn trả lời bằng benchmark. ”

- Chuẩnbị: 10 câuhỏi mẫu +
expectedanswer cho agent của bạn

- Đọctrước: tài liệuRAGAS (20
phút)

- Suynghĩ: từ onlineeval hôm
nay,quality metric nào quan trọngnhất cho use case của bạn? Giảngviên (VinUni) AICB· Monitoring 2026 95/ 96

---

<!-- chiron-source-span: {"source_span_id":"13a9708e-4198-5930-9de9-d071257505fb","locator":{"kind":"page","page":113,"label":"Slide 113","section_title":"TàiLiệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"1cb7ad354e00e06af3324a86eabab0f409a60d7b114a57da764bf6449a615368"} -->

## Slide 113 - TàiLiệu Tham Khảo

1. OpenTelemetryGenAI Semantic Conventions — github.com/open-telemetry/semantic-conventions-genai (trạngthái Development, 2026).

2. Langfuse—langfuse.com(OSS/MIT,SDKPythonv4,OTel-based). LangSmith—docs.langchain.com.

3. ArizePhoenix & OpenInference; OpenLLMetry (Traceloop)— OTel-nativeLLM instrumentation.

4. GoogleSRE Book & SRE Workbook— sre.google (SLI/SLO/SLA, error budget, multi-burn-rate alerting,golden signals).

5. Prometheus& Grafana — prometheus.io, grafana.com. Microsoft Presidio — microsoft.github.io/presidio(PII redaction).

6. VietnamPDPL (Luật 91/2025, hiệu lực1/1/2026); Anthropic/OpenAI/Google pricing & prompt-caching docs. Giảngviên (VinUni) AICB· Monitoring 2026 96/ 96

---

<!-- chiron-source-span: {"source_span_id":"906730f3-4ad1-5db7-a1f2-bb6701b563b0","locator":{"kind":"page","page":114,"label":"Slide 114","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"08f46fb29b96db037562327d9bb2577845a45800dcf350c991b2a9ba5778829a"} -->

## Slide 114 - Hỏi& Đáp

Monitoring tốt nghĩa là bạn biết agent có vấn đề trước khi user phàn nàn.
