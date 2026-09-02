---
schema_version: 1
course_id: rag-intensive
document_id: "31d833e3-2e14-5256-8244-d85448318677"
document_version_id: "231ec4c1-1cd6-55ed-9825-900c827fbffc"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Observability — Nhìn thấy Agent trong Production"
source_file: "day-13.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\day-13.html"
source_sha256: "93f4f8844df981f724701cdf66e0b897e63e481fd759e8c39d14e3447cb8af8e"
parser_version: chiron-structured-markdown-v1
html_section_count: 21
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# Observability — Nhìn thấy Agent trong Production

> Biến log, trace, metric và eval thành khả năng trả lời: lỗi ở đâu, ảnh hưởng ai và có nên rollback không.

<!-- chiron-source-span: {"source_span_id":"cba93775-2c97-5d76-82c4-8d3bd2d46be7","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"day-13.html"},"checksum":"42a58870c5b50b77b247599aa327c1917a4d1cb15e078831f25f20d139995340"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: monitoring báo cái đã biết, observability giúp hỏi cái chưa biết. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"b740e7b1-d21c-5618-bcd6-b2c6932af338","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"day-13.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

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

<!-- chiron-source-span: {"source_span_id":"c7e9448c-bebc-50ef-bb94-8bcbbba8c126","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Observability khác monitoring","source_file":"day-13.html"},"checksum":"81404858145e80200ff5c28c174069de6231d0ec8baa155e28a9450b7108291e"} -->

## 01 Observability khác monitoring

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Observability khác monitoring · Mental model & quyết định

> Trích slide Slide 1: Monitoring, Logging & Observability AICB-P1· Ngày 13 · Biếtagent đang chạy thế nào trướckhi user phàn nàn TênGiảng Viên VinUniversity · Phase 1 · 2026

Monitoring, Logging & Observability AICB-P1· Ngày 13 · Biếtagent đang chạy thế nào trướckhi user phàn nàn Tên. Điểm nối sang production là: monitoring báo cái đã biết, observability giúp hỏi cái chưa biết. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- 3 ngày sau: latency tăng gấp đôi, cost tăng 300 phần trăm, và 1 trên 20 câu trả lời là bịa.
- Đó là cách tệ nhất, và đắt nhất, để phát hiện vấn đề.” Giữcâu hỏi này trong đầukhi học bài hôm nay
- Remember—liệt kê3pillars (metrics,logs, traces) +pillarthứ 4(continuouseval) và 6 nhómAI-specific metrics

#### Tự kiểm tra · Với observability khác monitoring, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là monitoring báo cái đã biết, observability giúp hỏi cái chưa biết.

### Slide 6 Observability khác monitoring · Evidence & failure lens

> Trích slide Slide 6: 01 Vì Sao Agent Cần Observability “It works” không đủ cho production — cần biết nó chạy TỐT đến đâu, chậm ở đâu, tốn bao nhiêu, và khi nào sắp hỏng

**Đọc như kỹ sư:** 01 Vì Sao Agent Cần Observability “It works” không đủ cho production — cần biết nó chạy TỐT đến đâu, chậm ở đâu, tốn bao nhiêu, và khi nào sắp hỏng

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 6 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 10 Observability khác monitoring · Evidence & failure lens

> Trích slide Slide 10: Costof Not Monitoring Agenttrảlờisainhưngkhôngaibiết. User mấtniềmtindần. Đếnkhipháthiệnthìđã mấtuser. Tokencosttăngdầnmàkhôngalert. Cuối tháng nhận bill gấp 5 lần. Đốt hết budget trướckhi kịp react. Latency P95 tăng 10ms mỗi tuần. 6 tuần sau: chậm gấp đôi. Không ai để ý vì khôngcó baseline. Bug report: “agent sai hôm qua.”…

**Đọc như kỹ sư:** Costof Not Monitoring Agenttrảlờisainhưngkhôngaibiết.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Bug report: “agent sai hôm qua.” Không log,khôngtrace.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 10 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"653f824a-21b9-573b-aea9-4dcf15a37625","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Ba trụ log–metric–trace","source_file":"day-13.html"},"checksum":"f2fcb13c43294aa20d1ad416e4cd4c88ddeb7b0a8563b56a5de8669eaaf3fd59"} -->

## 02 Ba trụ log–metric–trace

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 11 Ba trụ log–metric–trace · Mental model & quyết định

> Trích slide Slide 11: Observability: Vài Cột Mốc 1 Logs (text) 2 Metrics & Prometheus 2012 3 Grafana 2014 4 Tracing & OTel 2019 5 LLM-native 2023+ Giảngviên (VinUni) AICB· Monitoring 2026 8/ 96

Observability: Vài Cột Mốc 1 Logs (text) 2 Metrics & Prometheus 2012 3 Grafana 2014 4 Tracing & OTel 2019 5 LLM-native 2023+. Điểm nối sang production là: một request phải có correlation id xuyên model, retrieval và tool. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- ControlTheory — Observability Là MộtFeedback Loop Agent System Observe metrics Analyze compare Act fix/scale Feedbackloop Mean Time To Detect: từ khi sự cố xảy rađến khi phát hiện.
- MeanTimeToRecover: từkhipháthiện đếnkhi fix xong.
- Observabilitytốt=giảm MTTDxuốngphút,khôngphảingày.

#### Tự kiểm tra · Với ba trụ log–metric–trace, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là một request phải có correlation id xuyên model, retrieval và tool.

### Slide 16 Ba trụ log–metric–trace · Evidence & failure lens

> Trích slide Slide 16: TạiSao Chỉ Logs Là KhôngĐủ? Chỉcó logs ■ biếtrequest nào fail ■ nhưngkhông biết fail rate bao nhiêu ■ khôngbiết latency đang tăng dần ■ khôngbiết bottleneck ở đâu Đủpillars ■ metricscho biết trend (tăng/giảm) ■ logscho biết chi tiết từngrequest ■ tracescho biết chậm ở bướcnào ■ evalcho biết chất lượng còntốt không Logs giống…

**Đọc như kỹ sư:** evalcho biết chất lượng còntốt không Logs giống camera an ninh.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Traces giống bản đồ GPS.Eval giống người kiểm định chấtlượng.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 16 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 20 Ba trụ log–metric–trace · Evidence & failure lens

> Trích slide Slide 20: 4Golden Signals + 2 ChoAI Agent GoogleSRE — 4 Golden Signals 1. Latency—thời gian phản hồi 2. Traffic—request rate (QPS) 3. Errors—error rate 4. Saturation—tài nguyên còn bao nhiêu AIagent cần thêm 2 5. Cost—$/request, $/user,token usage 6. Quality—hallucination rate, CSAT, groundedness Lưuý:…

**Đọc như kỹ sư:** 4Golden Signals + 2 ChoAI Agent GoogleSRE — 4 Golden Signals 1.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Saturation—tài nguyên còn bao nhiêu AIagent cần thêm 2 5.
- Quality—hallucination rate, CSAT, groundedness Lưuý: Agentcóthể“up”(traffic/latency/errorOK)nhưng trảlờisaivàđốttiền.
- Đây là2 failure mode riêng của AImà monitoring truyền thống bỏ qua.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 20 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"4ccaa007-4d9c-5d6a-a04a-0dc72348d77a","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Structured logging cho agent","source_file":"day-13.html"},"checksum":"5eb5b7b85284c93fa82caa6c74b89b802494d611e26913124e49423819e1b814"} -->

## 03 Structured logging cho agent

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 21 Structured logging cho agent · Mental model & quyết định

> Trích slide Slide 21: REDvs USE — Hai PhươngPháp Observability RED(request-centric) ■ Rate— requests/giây ■ Errors— error rate ■ Duration— latency P50/P95/P99 Gócnhìn user: tôigửi request, được gì? USE(resource-centric) ■ Utilization— tài nguyên dùng% ■ Saturation— có queue/chờ không? ■ Errors— lỗi của resource Gócnhìn resource: LLMAPI, queue đang…

REDvs USE — Hai PhươngPháp Observability RED(request-centric). Điểm nối sang production là: log prompt nguyên văn có thể tạo rò rỉ dữ liệu. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Duration— latency P50/P95/P99 Gócnhìn user: tôigửi request, được gì?
- Errors— lỗi của resource Gócnhìn resource: LLMAPI, queue đang làm gì?
- Agentchậm(RED:DurationP95tăng) →debugbằngUSE(LLMrate-limitutilization 95%)→bịthrottle →upgradetier hoặc fallback.

#### Tự kiểm tra · Với structured logging cho agent, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là log prompt nguyên văn có thể tạo rò rỉ dữ liệu.

### Slide 26 Structured logging cho agent · Evidence & failure lens

> Trích slide Slide 26: Hallucination— Phát Hiện Thế Nào? Hallucination — Agenttrảlời“rấttựtin”nhưngsaisựthật. Khôngcó1metricduy nhất→cầncombo 4 patterns. Mỗi claim trong output→ check có trong retrieved contextkhông. Tool: RAGAS faithfulness, TruLens. Gọi LLM 3 lần (temp 0.7); 3 câu mâu thuẫn→ nghi ngờ. Cost 3x→chỉsample 1%. Extract entities (tên,…

**Đọc như kỹ sư:** Hallucination — Agenttrảlời“rấttựtin”nhưngsaisựthật.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Mỗi claim trong output→ check có trong retrieved contextkhông.
- Gọi LLM 3 lần (temp 0.7); 3 câu mâu thuẫn→ nghi ngờ.
- Extract entities (tên, số, dates) → cross-check DB/API.Cho finance, medical.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 26 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 31 Structured logging cho agent · Evidence & failure lens

> Trích slide Slide 31: MetricNào Cho Ai? Stakeholder Quantâm Metrics Engineering Systemhealth, debug Latency P95, error rate,tool-call failure Product Userexperience Satisfaction, task com- pletion, hallucination rate Finance/ Ops Costcontrol Cost/ngày, tokens/re- quest,cost by model Leadership ROIoverview Adoption, cost vs value,uptime Dashboard…

**Đọc như kỹ sư:** MetricNào Cho Ai? Stakeholder Quantâm Metrics Engineering Systemhealth, debug Latency P95, error rate,tool-call failure Product Userexperience Satisfaction, task com- pletion, hallucination rate Finance/ Ops Costcontrol Cost/ngày, tokens/re- quest,cost by mode

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 31 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"2c939e7f-a828-5350-ab18-79dd4d16e8a8","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Distributed tracing & OpenTelemetry","source_file":"day-13.html"},"checksum":"2c334a3dc45f964ba98571271f338e18fc510c86ac37ccb8d39b66c9753842e5"} -->

## 04 Distributed tracing & OpenTelemetry

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 32 Distributed tracing & OpenTelemetry · Mental model & quyết định

> Trích slide Slide 32: 04 Structured Logging Log không cấu trúc giống ghi chú tay — khó search, khó aggre- gate. Structured logging biến log thành DATA query được

04 Structured Logging Log không cấu trúc giống ghi chú tay — khó search, khó aggre- gate.. Điểm nối sang production là: p95/p99 quan trọng hơn average cho trải nghiệm nhiều lượt. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Structured logging biến log thành DATA query được
- Quánhiều DEBUG ở production Lưu ý:Log PII = vi phạm PDPL (Việt Nam) / GDPR.Redact trước khi log, không phảisau khi bị audit.
- NER/ entity detection: tên người, địachỉ (Microsoft Presidio)

#### Tự kiểm tra · Với distributed tracing & opentelemetry, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là p95/p99 quan trọng hơn average cho trải nghiệm nhiều lượt.

### Slide 37 Distributed tracing & OpenTelemetry · Evidence & failure lens

> Trích slide Slide 37: LogLevels Đúng Cách Level Khinào dùng Vídụ DEBUG Devonly,rất chi tiết Full prompt, intermediate state INFO Normalflow,milestone Request received, re- sponsesent WARN Degradednhưng vẫn chạy Retrysucceeded,fallback used ERROR Failed,cần attention Tooltimeout, LLM error Productionchạy INFOlevel. Khidebugissuecụthể, tạmbậtDEBUG…

**Đọc như kỹ sư:** Khidebugissuecụthể, tạmbậtDEBUG cho1requestID,xong tắtlại.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 37 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 41 Distributed tracing & OpenTelemetry · Evidence & failure lens

> Trích slide Slide 41: LogAggregation Stacks Stack Khinào dùng Cost/ tier ELK Full-text search mạnh, complex queries Tựhost, OSS Loki Label-based (giống Prometheus),rẻ Tựhost, OSS DatadogLogs Setupnhanh,alerttốt,đắtởscale SaaS ∼ $0.10/GB CloudWatch Đã ở AWS,tíchhợp IAM ∼ $0.50/GBingest BigQuery AnalyticsSQL, long retention ∼ $0.02/GBscan…

**Đọc như kỹ sư:** Scaleupmớicần ELK/ Loki — đừng dựngcluster Elasticsearch cho MVP.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 41 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"31d6df07-bc86-5e38-bc4f-69c55616c1d8","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 Metric riêng của AI","source_file":"day-13.html"},"checksum":"dc3bf73c525e3cf640785d6661f022cacfac3a2a6f9737a4c6171d94e16ccae8"} -->

## 05 Metric riêng của AI

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 42 Metric riêng của AI · Mental model & quyết định

> Trích slide Slide 42: AuditLog — Tách Biệt VớiApp Log Audit log— Recordwho did what whencho compliance, legal, security — khác hẳnapp log dùng để debug. Applog ■ Mụcđích: debug, performance ■ Retention: 30–90 ngày ■ Cóthể sample, sửa/xóa ■ Truycập: devteam Auditlog ■ Mụcđích: compliance, forensics ■ Retention: 2–7 năm (tùyngành) ■ Khôngsample;…

AuditLog — Tách Biệt VớiApp Log Audit log— Recordwho did what whencho compliance, legal, security — khác hẳnapp log dùng để debug.. Điểm nối sang production là: trace phải tách span retrieval, LLM và tool. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Truycập: restricted(compliance) Lưuý: Trộnauditvàoapplog →khicầninvestigatebịthiếudata.
- Táchriêngtừngày đầu: S3bucketvới ObjectLock,hoặcdedicatedauditservice.
- 05 Distributed Tracing Cho Agent Log cho biết gì xảy ra ở từng bước; trace cho biết hành trình của 1 request qua LLM→ tool→ LLM và mất bao lâu ở mỗi bước

#### Tự kiểm tra · Với metric riêng của ai, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là trace phải tách span retrieval, LLM và tool.

### Slide 47 Metric riêng của AI · Evidence & failure lens

> Trích slide Slide 47: OTelGenAI Semantic Conventions (gen_ai.*) Attribute Ýnghĩa gen_ai.operation.name chat/ execute_tool / invoke_agent gen_ai.provider.name openai/ anthropic (thay gen_ai.system cũ) gen_ai.request.model modelđược yêu cầu gen_ai.usage.input_tokens inputtokens (thay prompt_tokens) gen_ai.usage.output_tokens outputtokens (thay…

**Đọc như kỹ sư:** Tên cũ prompt_tokens/completion_tokens/gen_ai.system đãdeprecated nhưng nhiều tutorial cũvẫn dùng.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 47 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 51 Metric riêng của AI · Evidence & failure lens

> Trích slide Slide 51: 4Bottleneck Patterns TrongTrace A→B→C, tổng = sum. Fix: parallelize A, B nếu khôngphụ thuộc. LoopgọiAPI/DBnhiềulần →nhiềuspanngắncùng tên. Fix: batch / pre-fetch. Span dài nhưng CPU idle (LLM API, DB, network). Fix: parallelize, cache, timeout. Nhiều span retry trong 1 trace; backoff quá ngắn, không jitter. Fix: exponential…

**Đọc như kỹ sư:** 4Bottleneck Patterns TrongTrace A→B→C, tổng = sum.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- LoopgọiAPI/DBnhiềulần →nhiềuspanngắncùng tên.
- Span dài nhưng CPU idle (LLM API, DB, network).
- Nhiều span retry trong 1 trace; backoff quá ngắn, không jitter.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 51 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"a867ffcd-1187-5a48-bc86-9302d91b3540","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Continuous evaluation","source_file":"day-13.html"},"checksum":"2280ab8fd29c8e96b3f53daf8bf67b3cd11bc2b7b7deb09a773d02a132bfcaf6"} -->

## 06 Continuous evaluation

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 52 Continuous evaluation · Mental model & quyết định

> Trích slide Slide 52: 06 Bộ Công Cụ LLM-Observability 2026 Có cả một hệ sinh thái — chọn đúng theo nhu cầu: open-source hay SaaS, dùng framework gì, self-host hay cloud

06 Bộ Công Cụ LLM-Observability 2026 Có cả một hệ sinh thái — chọn đúng theo nhu cầu: open-source hay SaaS, dùng framework gì, self-host hay cloud. Điểm nối sang production là: SLO cần gắn với điều người dùng cảm nhận. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Cần eval/trajectory sâu & đã dùng LangChain:LangSmith.
- Muốnkhông lock-in: instrumentbằng OTel/OpenLLMetryrồigửi đi đâu cũng được.
- @observe() vẫnlàidiomđúng—nhưngimportlà from langfuse import observe (KHÔNGphải langfuse.decorators kiểuv2 cũ).

#### Tự kiểm tra · Với continuous evaluation, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là SLO cần gắn với điều người dùng cảm nhận.

### Slide 57 Continuous evaluation · Evidence & failure lens

> Trích slide Slide 57: ChọnCông Cụ Nào Khi Nào? ■ MVP/ lab / startup: Langfuse free tier(cloud) hoặc self-host docker — đủtracing + cost + dashboard. ■ Đãdùng LangChain/LangGraph, cần eval sâu: LangSmith. ■ Cầndata ở lại on-prem /VN (compliance): self-host Langfuse hoặcPhoenix. ■ Khôngmuốn lock-in: instrument bằng OTel(OpenLLMetry)→đổibackend tùy ý.…

**Đọc như kỹ sư:** MVP/ lab / startup: Langfuse free tier(cloud) hoặc self-host docker — đủtracing + cost + dashboard.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Đãdùng LangChain/LangGraph, cần eval sâu: LangSmith.
- Cầndata ở lại on-prem /VN (compliance): self-host Langfuse hoặcPhoenix.
- Khôngmuốn lock-in: instrument bằng OTel(OpenLLMetry)→đổibackend tùy ý.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 57 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 62 Continuous evaluation · Evidence & failure lens

> Trích slide Slide 62: Instrument1 AI Service (prometheus_client) from prometheus_client import Counter, Histogram, start_http_server REQS = Counter( "agent_requests_total", "Requests", [ "model", "status"]) LAT = Histogram( "agent_latency_seconds", "Latency", [ "model"]) TOKS = Counter( "agent_tokens_total", "Tokens", [ "model", "direction"]) def…

**Đọc như kỹ sư:** Instrument1 AI Service (prometheus_client) from prometheus_client import Counter, Histogram, start_http_server REQS = Counter( "agent_requests_total", "Requests", [ "model", "status"]) LAT = Histogram( "agent_latency_seconds", "Latency", [ "model"]) TOKS = Cou

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 62 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"1dca1156-4efb-5ca4-aa51-df25749741b9","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Prometheus & Grafana","source_file":"day-13.html"},"checksum":"0f7e71fda7c8ade96313b980d02e4ff9324c49172f8ed6896f982069777ad0fb"} -->

## 07 Prometheus & Grafana

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 63 Prometheus & Grafana · Mental model & quyết định

> Trích slide Slide 63: Cardinality: Kẻ Đốt TiềnThầm Lặng Cardinality — Sốtổhợpgiátrịlabelcủa1metric. Mỗitổhợp=1time-seriesriêng phảilưu. Label giátrị tự do (user_id, request_id, rawprompt)→bùngnổ series. LabelAN TOÀN(thấp) ■ model, status, tool_name ■ direction (in/out) LabelNGUY HIỂM (cao) ■ user_id, request_id ■ prompt, session_id Lưu ý:Bài học…

Cardinality: Kẻ Đốt TiềnThầm Lặng Cardinality — Sốtổhợpgiátrịlabelcủa1metric.. Điểm nối sang production là: alert phải actionable và có owner. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Label giátrị tự do (user_id, request_id, rawprompt)→bùngnổ series.
- prompt, session_id Lưu ý:Bài học thật: Coinbase từng nhận hóa đơn Datadog$65 triệu(2022), phần lớn do custom metrics cardinality cao.
- High-cardinality thuộc vềlogs/traces, không phảimetric label.

#### Tự kiểm tra · Với prometheus & grafana, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là alert phải actionable và có owner.

### Slide 68 Prometheus & Grafana · Evidence & failure lens

> Trích slide Slide 68: 6Panel Bắt Buộc Cho AIService 1. Request rate (traffic) 2. Latency P50/P95/P99+ TTFT 3. Error rate (bytype) 4. Cost / token usage(in/out) 5. Tool-call successrate 6. Quality / eval score(sampled) Sovớiservicethường,agentthay“CPU/GPUpanel”bằng tool-callsuccess vàeval score—vì failure mode của agent nằmở đó. Giảngviên (VinUni)…

**Đọc như kỹ sư:** Quality / eval score(sampled) Sovớiservicethường,agentthay“CPU/GPUpanel”bằng tool-callsuccess vàeval score—vì failure mode của agent nằmở đó.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 68 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 72 Prometheus & Grafana · Evidence & failure lens

> Trích slide Slide 72: 09 Alerting & SLO Metrics chỉ có giá trị nếu có người nhìn. Alert sai cách còn tệ hơn không có. SLO cho bạn một ngân sách lỗi để quyết định khi nào cần lo

**Đọc như kỹ sư:** 09 Alerting & SLO Metrics chỉ có giá trị nếu có người nhìn.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- SLO cho bạn một ngân sách lỗi để quyết định khi nào cần lo

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 72 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"8df78a47-9f6d-5556-bef3-ea3669ffdb93","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Dashboard theo hành trình user","source_file":"day-13.html"},"checksum":"246a91a54dca92f318fa51255223db0f69b74b774f736f94c78bd58c2ffb2e0b"} -->

## 08 Dashboard theo hành trình user

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 73 Dashboard theo hành trình user · Mental model & quyết định

> Trích slide Slide 73: AlertRules Cho AI Agent Metric Threshold Severity Channel LatencyP95 >5 giây Warning Slack Errorrate >5% Critical Slack+ Email Dailycost >budget ngày Critical Email+ SMS Tool-callfailure >10% Warning Slack Evalscore tụt> 10% Warning Slack Uptime <99% Critical PagerDuty Alertphải actionable. Nếu nhận alertmà không biết làm gì,…

Nếu nhận alertmà không biết làm gì, alertđó cần redesign hoặc bỏ.. Điểm nối sang production là: error budget biến reliability thành quyết định release. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Symptom-Basedvs Cause-Based Alerting Symptom-based(NÊN page) Alerttrên cáiusercảm nhận được.
- Ítfalse positive, luôn thật Bốn golden signals: Latency, Traffic, Er- rors,Saturation.
- Cause-based(để DEBUG) Alerttrên nguyênnhân cóthể.

#### Tự kiểm tra · Với dashboard theo hành trình user, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là error budget biến reliability thành quyết định release.

### Slide 78 Dashboard theo hành trình user · Evidence & failure lens

> Trích slide Slide 78: On-CallCơ Bản Severity& escalation ■ SEV1(down/critical) →pagengay ■ SEV2(degraded) →Slack,giờ làm ■ SEV3(minor) →ticket ■ Escalation: primary→secondary→ lead MTTD = thời gian phát hiện.MTTR = thời gian khắc phục. Mục tiêu observability: giảmcả hai. Lưuý: BốicảnhVN:lịchon-calltheo UTC+7;tránhdeploylớndịp Tết;nhớnghĩavụ báocáo…

**Đọc như kỹ sư:** Escalation: primary→secondary→ lead MTTD = thời gian phát hiện.MTTR = thời gian khắc phục.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Lưuý: BốicảnhVN:lịchon-calltheo UTC+7;tránhdeploylớndịp Tết;nhớnghĩavụ báocáo sự cố dữ liệu72giờ theoPDPL (§13).

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 78 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 82 Dashboard theo hành trình user · Evidence & failure lens

> Trích slide Slide 82: VìSao Cost Là First-Class Metric CostAI khác cost phần mềm ■ Tỉlệ vớitoken,không phải request ■ Mộtloop bug đốt budget trong vàigiờ ■ Outputđắt 5–6x input ■ Costtăng tuyến tính với traffic Tokens (in/out), cost/request, cost/task, cost/ngày,cost/user,cost/feature,cachehit rate. Rollup + dailybudget alert.…

**Đọc như kỹ sư:** VìSao Cost Là First-Class Metric CostAI khác cost phần mềm

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Costtăng tuyến tính với traffic Tokens (in/out), cost/request, cost/task, cost/ngày,cost/user,cost/feature,cachehit rate.
- Haiku$1/$5·Sonnet$3/$15·Opus$5/$25·GPT-5.5$5/$30·Gemini3.1Pro$2/$12 (mỗi1M token in/out).

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 82 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"d3f4a16e-b978-5b68-a62f-085d8cd81dc5","locator":{"kind":"html_section","section_id":"c8","order":11,"heading":"09 Alert, SLO & error budget","source_file":"day-13.html"},"checksum":"2cf9cf731a8f9c0c73c4b67f41835f2cb1f6cd4bcc1b5e7d57629681bff3030d"} -->

## 09 Alert, SLO & error budget

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 83 Alert, SLO & error budget · Mental model & quyết định

> Trích slide Slide 83: ĐoCost Ở Đâu Và ThếNào Côngthức — cost = input_tokens 106 ×Pin[model] + output_tokens 106 ×Pout[model] ■ Tínhcost tạimỗi LLM calltừtoken usage (provider trả về sẵn) ■ Gắnnhãn theo model / feature /user→rolluptheo ngày ■ Setdailybudget alert: cost hôm nay> ngưỡng→báongay ■ Theodõi cachehit ratenhưmột cost SLI Lưu…

ĐoCost Ở Đâu Và ThếNào Côngthức — cost = input_tokens 106 ×Pin[model] + output_tokens 106 ×Pout[model]. Điểm nối sang production là: quality metric phải theo segment, không chỉ điểm trung bình. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Tínhcost tạimỗi LLM calltừtoken usage (provider trả về sẵn)
- Gắnnhãn theo model / feature /user→rolluptheo ngày
- Setdailybudget alert: cost hôm nay> ngưỡng→báongay

#### Tự kiểm tra · Với alert, slo & error budget, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là quality metric phải theo segment, không chỉ điểm trung bình.

### Slide 88 Alert, SLO & error budget · Evidence & failure lens

> Trích slide Slide 88: CaseStudy — Notion AI CostOptimization Bốicảnh — NotionAIphụcvụhàngtriệuuser(summary,Q&A,writingassist). Cost OpenAIban đầu∼30%revenue. Monitoring insight: ■ 70%queries là “summarize” với promptgiống nhau ■ 15%user chiếm 60% cost (powerusers, doc dài) ■ Regeneraterate cao ở feature “writingassist” Actions(theo thứ tự…

**Đọc như kỹ sư:** CaseStudy — Notion AI CostOptimization Bốicảnh — NotionAIphụcvụhàngtriệuuser(summary,Q&A,writingassist).

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- 70%queries là “summarize” với promptgiống nhau
- Regeneraterate cao ở feature “writingassist” Actions(theo thứ tự ROI):promptcache system prompt (−40%input)→route“summary” qua modelnhỏ(Haikutier, −60%)→per-userratelimitchofreetier →cảithiệnprompt“writingassist” (−35%regenerate).
- Cost/MAU giảm58% trong3tháng,khônggiảmquality.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 88 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 93 Alert, SLO & error budget · Evidence & failure lens

> Trích slide Slide 93: RootCause + Fix + Postmortem Một index filter của vector store bị bỏ trong deploy hạ tầng 8h45→ mỗi truy vấn quét toànbộ. Khớp đúngthời điểm P95 nhảy. Timeline · tác động (MTTD/MTTR) · root cause · cái gì đã giúp phát hiện · ac- tion items. Trách hệ thống, không trách người. Cùngquytrìnhmetric →log→tracedùngchomọiincident.…

**Đọc như kỹ sư:** RootCause + Fix + Postmortem Một index filter của vector store bị bỏ trong deploy hạ tầng 8h45→ mỗi truy vấn quét toànbộ.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Timeline · tác động (MTTD/MTTR) · root cause · cái gì đã giúp phát hiện · ac- tion items.
- Cùngquytrìnhmetric →log→tracedùngchomọiincident.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 93 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"397457fe-15f7-5175-a918-761bae5ba162","locator":{"kind":"html_section","section_id":"c9","order":12,"heading":"10 Cost observability","source_file":"day-13.html"},"checksum":"c9932dafdb7dc10490c5dffa3c01bccfd4c8fdc8f7122527bb18bd0423c41d84"} -->

## 10 Cost observability

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 94 Cost observability · Mental model & quyết định

> Trích slide Slide 94: BàiHọc Từ Sự Cố Thật(2024–2025) ■ ReplitAI agent (7/2025): agent xoá DBproduction dù đang “code freeze” —mất dữ liệu 1.206lãnh đạo + 1.196 côngty. Tệ hơn: agentbịa4.000user giả và nói rollbackbất khả thi (thựcra rollback được).⇒Least-privilege+ tách dev/prod; tin telemetry/backupđộc lập, KHÔNGtin agent tự thuật. ■ AirCanada…

ReplitAI agent (7/2025): agent xoá DBproduction dù đang “code freeze” —mất dữ liệu 1.206lãnh đạo + 1.196 côngty.. Điểm nối sang production là: telemetry cũng có chi phí và cần sampling có chủ đích. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Tệ hơn: agentbịa4.000user giả và nói rollbackbất khả thi (thựcra rollback được).⇒Least-privilege+ tách dev/prod; tin telemetry/backupđộc lập, KHÔNGtin agent tự thuật.
- Air Canada, 2024): chatbot bịa chínhsách vé tang lễ; toà buộc hãngbồi thường CA$650 — “chatbotlà thực thể riêng” bị bác.⇒Câutrả lời sai = trách nhiệmpháp lý; phải monitor chấtlượng output.
- Klarna: dồn AI thay700 agent rồiquayxe thuêlại người vì chất lượng.⇒Tỉlệ “AI xử lý X%”(mean) che giấu variance ởtail — theo dõi phân phối,không chỉ trung bình.

#### Tự kiểm tra · Với cost observability, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là telemetry cũng có chi phí và cần sampling có chủ đích.

### Slide 99 Cost observability · Evidence & failure lens

> Trích slide Slide 99: Feedback→Dataset→CảiThiện (và Cẩn Trọng) Câutrảlờitệ(thumbs-down/judgethấp) → gom thành dataset→ thành test case cho Day14 →sửaprompt/model →đolại. Lưu ý: Judge drift: LLM-judge cũng thayđổitheothờigian/phiênbản. Theo dõi phân phốiđiểm (không chỉ mean); định kỳ kiểm bằng gold set người chấm.…

**Đọc như kỹ sư:** Feedback→Dataset→CảiThiện (và Cẩn Trọng) Câutrảlờitệ(thumbs-down/judgethấp) → gom thành dataset→ thành test case cho Day14 →sửaprompt/model →đolại.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Lưu ý: Judge drift: LLM-judge cũng thayđổitheothờigian/phiênbản.
- Theo dõi phân phốiđiểm (không chỉ mean); định kỳ kiểm bằng gold set người chấm.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 99 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 103 Cost observability · Evidence & failure lens

> Trích slide Slide 103: Retention,Access & Audit Đặt TTL theo loại data. Trace chi tiết: ngắn (7–30 ngày). Metric tổng hợp: dài. Retention dài = tốn tiền+ rủi ro. Ai xem được log/trace chứa data người dùng? RBAC+ chỉ cấp khi cần. Ghi lại ai truy cập teleme- try. Hỗtrợquyềnxoá/truy cậpcủa user.…

**Đọc như kỹ sư:** Retention,Access & Audit Đặt TTL theo loại data.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Retentionlàmộttrụctínhtiền(vdLangSmithtínhriêng“extendedtraces”400ngày).

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 103 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"f7afa485-e1fc-5c9b-8cef-cd3e2ca9a078","locator":{"kind":"html_section","section_id":"c10","order":13,"heading":"11 Debug incident & Lab 13","source_file":"day-13.html"},"checksum":"de911caa7b84dd0c2af1555c980e4589e117eaf35f6e62592b641f572cd06a8f"} -->

## 11 Debug incident & Lab 13

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 104 Debug incident & Lab 13 · Mental model & quyết định

> Trích slide Slide 104: Compliance: ViệtNam +Quốc Tế ■ ViệtNam: Nghị định 13/2023(PDPD, hiệu lực 1/7/2023) nay đượcnâng lênLuật Bảovệ Dữ liệu Cá nhân(PDPL,Luật 91/2025, hiệu lực1/1/2026). ■ Báocáo vi phạm dữ liệu trong72giờ tớiBộ Công an (A05). Chuyển dữ liệu xuyên biêngiới cầnhồsơ đánh giá tác động (TIA),nộp trong 60 ngày. ■ Phạtnặng: vi phạmchuyển…

ViệtNam: Nghị định 13/2023(PDPD, hiệu lực 1/7/2023) nay đượcnâng lênLuật Bảovệ Dữ liệu Cá nhân(PDPL,Luật 91/2025, hiệu lực1/1/2026).. Điểm nối sang production là: monitoring báo cái đã biết, observability giúp hỏi cái chưa biết. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Báocáo vi phạm dữ liệu trong72giờ tớiBộ Công an (A05).
- Chuyển dữ liệu xuyên biêngiới cầnhồsơ đánh giá tác động (TIA),nộp trong 60 ngày.
- Phạtnặng: vi phạmchuyển xuyên biên giới có thểtới5%doanh thunămtrước.

#### Tự kiểm tra · Với debug incident & lab 13, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là monitoring báo cái đã biết, observability giúp hỏi cái chưa biết.

### Slide 109 Debug incident & Lab 13 · Evidence & failure lens

> Trích slide Slide 109: Observathon— Cuộc Thi Observability (Capstone) Một agent e-commercehộp đen, im lặng, đầy bug(không phát log/metric/trace). Muốnthắng: tựgắn observabilityđểbắt bug rồi sửa. Nộp3 thứ ■ Findings: bug gì +bằng chứng ■ Configđãsửa (agent mis-config) ■ Wrapper: retry/cache/route/guardrail Điểm= 1 con số ■ correctness+ LLM-eval…

**Đọc như kỹ sư:** Observathon— Cuộc Thi Observability (Capstone) Một agent e-commercehộp đen, im lặng, đầy bug(không phát log/metric/trace).

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Muốnthắng: tựgắn observabilityđểbắt bug rồi sửa.
- Wrapper: retry/cache/route/guardrail Điểm= 1 con số
- Publictest(giờ2,leaderboard) →private(3.5h,held-out+1bugẩn)xếp hạng.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 109 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 114 Debug incident & Lab 13 · Evidence & failure lens

> Trích slide Slide 114: Hỏi& Đáp Monitoring tốt nghĩa là bạn biết agent có vấn đề trước khi user phàn nàn.

**Đọc như kỹ sư:** Hỏi& Đáp Monitoring tốt nghĩa là bạn biết agent có vấn đề trước khi user phàn nàn.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 114 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"9451c363-329b-5271-91c4-1c3d62ccb8bb","locator":{"kind":"html_section","section_id":"ladder","order":14,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"day-13.html"},"checksum":"84f0f5c05d72793c87f1ae5a646a86ce3447702d809323c2164bbabb6b2dff91"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của Observability & SLO bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"ee9d671c-19a5-5bb2-875b-a9beaa462331","locator":{"kind":"html_section","section_id":"section-015","order":15,"heading":"∑ Phòng mô phỏng quyết định","source_file":"day-13.html"},"checksum":"50fb2c54a9a9f0883614476be4f372dc5287d937bc35c38e071c2edc23336307"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Tail latency — một phiên dài có tránh được đuôi chậm?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Tỷ lệ request đuôi:**: min `1`, max `30`, step `1`, default `5`

- **Control - Lượt/phiên:**: min `1`, max `30`, step `1`, default `10`

- **Control - Phiên/ngày:**: min `100`, max `20000`, step `100`, default `3000`

- **Control - P95 latency:**: min `1`, max `90`, step `1`, default `18`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Error budget & burn rate — còn được phép lỗi bao lâu?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - SLO:**: min `900`, max `999`, step `1`, default `990`

- **Control - Cửa sổ:**: min `7`, max `90`, step `1`, default `30`

- **Control - Error hiện tại:**: min `1`, max `100`, step `1`, default `20`

- **Control - Đã cháy:**: min `1`, max `168`, step `1`, default `12`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Telemetry cost — sample bao nhiêu là có ích?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Request/ngày:**: min `1000`, max `500000`, step `1000`, default `50000`

- **Control - Span/request:**: min `1`, max `80`, step `1`, default `15`

- **Control - Sampling:**: min `1`, max `100`, step `1`, default `20`

- **Control - Giá/triệu span:**: min `1`, max `100`, step `1`, default `18`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"ffa423ee-88fe-555e-876d-ef7a09310312","locator":{"kind":"html_section","section_id":"misc","order":16,"heading":"✕ Hiểu lầm phổ biến","source_file":"day-13.html"},"checksum":"f525c979774849a2b493f80ddc4ef905ba3f97660c3caa5382fe75d54030d56e"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai observability khác monitoring là phần còn lại tự động an toàn và ổn định.

Sửa lại Monitoring báo cái đã biết, observability giúp hỏi cái chưa biết.

Vì sao quan trọng · slide 1 · 6 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai ba trụ log–metric–trace là phần còn lại tự động an toàn và ổn định.

Sửa lại Một request phải có correlation id xuyên model, retrieval và tool.

Vì sao quan trọng · slide 11 · 16 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai structured logging cho agent là phần còn lại tự động an toàn và ổn định.

Sửa lại Log prompt nguyên văn có thể tạo rò rỉ dữ liệu.

Vì sao quan trọng · slide 21 · 26 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai distributed tracing & opentelemetry là phần còn lại tự động an toàn và ổn định.

Sửa lại P95/p99 quan trọng hơn average cho trải nghiệm nhiều lượt.

Vì sao quan trọng · slide 32 · 37 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai metric riêng của ai là phần còn lại tự động an toàn và ổn định.

Sửa lại Trace phải tách span retrieval, LLM và tool.

Vì sao quan trọng · slide 42 · 47 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai continuous evaluation là phần còn lại tự động an toàn và ổn định.

Sửa lại SLO cần gắn với điều người dùng cảm nhận.

Vì sao quan trọng · slide 52 · 57 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"2d511dd7-9ba9-5c28-b97c-ec6def8a3e1d","locator":{"kind":"html_section","section_id":"apply","order":17,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"day-13.html"},"checksum":"aa84fde1e380d386f09aa36d4bbafe580c6dcfd39c30f1bcb2ebe54cbd164c87"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI có latency tăng nhưng CPU bình thường; đội phải tìm bottleneck ở retrieval, model hay tool.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Observability khác monitoring | Monitoring báo cái đã biết, observability giúp hỏi cái chưa biết. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 6 |
| Ba trụ log–metric–trace | Một request phải có correlation id xuyên model, retrieval và tool. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 11 · 16 |
| Structured logging cho agent | Log prompt nguyên văn có thể tạo rò rỉ dữ liệu. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 21 · 26 |
| Distributed tracing & OpenTelemetry | P95/p99 quan trọng hơn average cho trải nghiệm nhiều lượt. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 32 · 37 |
| Metric riêng của AI | Trace phải tách span retrieval, LLM và tool. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 42 · 47 |
| Continuous evaluation | SLO cần gắn với điều người dùng cảm nhận. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 52 · 57 |
| Prometheus & Grafana | Alert phải actionable và có owner. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 63 · 68 |
| Dashboard theo hành trình user | Error budget biến reliability thành quyết định release. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 73 · 78 |

---

<!-- chiron-source-span: {"source_span_id":"04ad1711-4ea9-56d5-b3ee-8262d59ce095","locator":{"kind":"html_section","section_id":"numbers","order":18,"heading":"# Con số cần kiểm chứng","source_file":"day-13.html"},"checksum":"f255adee742c20289a262ccda8ef10fef285336e5d5325d59aa5b55ea51cee6b"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 3 ngày | ? HÃYSUY NGHĨ... “Agent bạn deploy hôm Day 12 chạy ngon. 3 ngày sau: latency tăng gấp đôi, cost tăng 300 phần trăm, và 1 trên 20 câu trả lời là bịa. Bạn biết những điều này khi nào? — Khi user phàn nàn. Đó là cách | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 2 |
| 10ms | Cuối tháng nhận bill gấp 5 lần. Đốt hết budget trướckhi kịp react. Latency P95 tăng 10ms mỗi tuần. 6 tuần sau: chậm gấp đôi. Không ai để ý vì khôngcó baseline. Bug report: “agent sai hôm qua.” Không log,khôngtrace. Khôngreproduceđược. Khô | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 10 |
| 2 M | Observability: Vài Cột Mốc 1 Logs (text) 2 Metrics & Prometheus 2012 3 Grafana 2014 4 Tracing & OTel 2019 5 LLM-native 2023+ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 11 |
| 4 M | 02 3 Pillars + Pillar Thứ 4 Metrics nói bao nhiêu / bao lâu, logs nói chuyện gì xảy ra, traces nói tại sao — và với AI có pillar thứ 4: câu trả lời có còn ĐÚNG không | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 0% | trả lời bịa ■ Latencythấp kháchữuích — trả lời nhanh nhưngsai còn tệ hơn ■ Errorrate 0%kháckhôngđốt tiền — chi phí vẫncó thể tăng vọt Day 13 đo chất lượngliên tục trên production(online). Day 14 đo chất lượngcó hệthống bằng benchmark(off | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 15 |
| 95% | e đang làm gì? Agentchậm(RED:DurationP95tăng) →debugbằngUSE(LLMrate-limitutilization 95%)→bịthrottle →upgradetier hoặc fallback. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 21 |
| 2.5s | Latency: Percentiles + TTFT P50 ≈2.5s(nửa số request nhanh hơn) P95 ≈5s(95% request nhanh hơn) P99 ≈8s+ TTFT (Time To First Token)— Thời gian từ lúc gửi request đến token đầu tiên. Quyếtđ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 22 |
| 5s | Latency: Percentiles + TTFT P50 ≈2.5s(nửa số request nhanh hơn) P95 ≈5s(95% request nhanh hơn) P99 ≈8s+ TTFT (Time To First Token)— Thời gian từ lúc gửi request đến token đầu tiên. Quyếtđịnh cảm giác “nhanh”. Điển hình 20 | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 22 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"66bfe9b0-ffc2-5c60-b1da-5711f751089d","locator":{"kind":"html_section","section_id":"cheat","order":19,"heading":"▣ Cheat sheet ôn thi","source_file":"day-13.html"},"checksum":"2faa8b301656f9ba723fd3471768a4d6238fd015140a084c10dc2a6e27372770"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp observability khác monitoring | monitoring báo cái đã biết, observability giúp hỏi cái chưa biết | 1 · 6 |
| Khi gặp ba trụ log–metric–trace | một request phải có correlation id xuyên model, retrieval và tool | 11 · 16 |
| Khi gặp structured logging cho agent | log prompt nguyên văn có thể tạo rò rỉ dữ liệu | 21 · 26 |
| Khi gặp distributed tracing & opentelemetry | p95/p99 quan trọng hơn average cho trải nghiệm nhiều lượt | 32 · 37 |
| Khi gặp metric riêng của ai | trace phải tách span retrieval, LLM và tool | 42 · 47 |
| Khi gặp continuous evaluation | SLO cần gắn với điều người dùng cảm nhận | 52 · 57 |
| Khi gặp prometheus & grafana | alert phải actionable và có owner | 63 · 68 |
| Khi gặp dashboard theo hành trình user | error budget biến reliability thành quyết định release | 73 · 78 |
| Khi gặp alert, slo & error budget | quality metric phải theo segment, không chỉ điểm trung bình | 83 · 88 |
| Khi gặp cost observability | telemetry cũng có chi phí và cần sampling có chủ đích | 94 · 99 |

---

<!-- chiron-source-span: {"source_span_id":"62978704-e346-58d1-ab4e-866a0b439a33","locator":{"kind":"html_section","section_id":"gloss","order":20,"heading":"☰ Từ điển thuật ngữ","source_file":"day-13.html"},"checksum":"9dcf984331da52bc7f2e8985e4fd4b386510bf474b0d8a8adf20fe59e8eb7d6a"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"8e01eb50-fbe7-5175-a141-749242cf8ea5","locator":{"kind":"html_section","section_id":"bloom","order":21,"heading":"◉ Bạn đang ở mức nào?","source_file":"day-13.html"},"checksum":"bf905021b97f944c74332ac50edbddf7338518610818ad2be47c0a3eaaff18d4"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 6 · 10 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 11 · 16 · 20 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 21 · 26 · 31 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 32 · 37 · 41 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 42 · 47 · 51 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 52 · 57 · 62 |
