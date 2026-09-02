---
schema_version: 1
course_id: rag-intensive
document_id: "79e16cb3-bd84-57cf-b3e6-6a9aec783d71"
document_version_id: "b233a8e0-df4a-5353-a74d-e233a26ff67e"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Deployment — Đưa Agent lên Cloud"
source_file: "day-12.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\day-12.html"
source_sha256: "b2256af949cb0f6caa8bc4b408b4a9ec8188a1b5fda5fb649541b56599a6a81c"
parser_version: chiron-structured-markdown-v1
html_section_count: 22
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# Deployment — Đưa Agent lên Cloud

> Từ một demo chạy trên laptop đến dịch vụ có thể chịu tải, quan sát và kiểm soát chi phí.

<!-- chiron-source-span: {"source_span_id":"1964bfc3-1ee6-591b-81d6-b887996f35d9","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"day-12.html"},"checksum":"bb96419c0caf3de06296d8dbb4af563974c25b70c068872cb9255eb9c9fcfb2a"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: externalize state thay vì dùng sticky session. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"65a8cf42-e7a9-5489-9be7-cea6ebdc817c","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"day-12.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

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

<!-- chiron-source-span: {"source_span_id":"520d65b2-baa3-5a87-b89e-2b8b0e7c7a4d","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Localhost → production gap","source_file":"day-12.html"},"checksum":"82128e16a3dcd8199c9d73ec366f36c5b4ac25f685a3e75d4da0e31a92db98d3"} -->

## 01 Localhost → production gap

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Localhost → production gap · Mental model & quyết định

> Trích slide Slide 1: Deployment — Đưa Agent Lên Cloud AICB-P1 · Ngày 12 · Từ localhost đến production URL TênGiảng Viên VinUniversity · Phase 1 · 2026

Deployment — Đưa Agent Lên Cloud AICB-P1 · Ngày 12 · Từ localhost đến production URL Tên. Điểm nối sang production là: externalize state thay vì dùng sticky session. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- “Bạn demo cho sếp thấy agent chạy trên laptop.
- — và liệu nó có ngốn hết ngân sách không?” Giữcâu hỏi này trong đầukhi học bài hôm nay
- Hiểugapgiữa dev và production: dependencies, config, secrets,networking

#### Tự kiểm tra · Với localhost → production gap, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là externalize state thay vì dùng sticky session.

### Slide 5 Localhost → production gap · Evidence & failure lens

> Trích slide Slide 5: DeliverableCuối Ngày Artifactpack cần nộp Agent đã được containerize và deploy lên cloud, có health check endpoint, basic authentication,cost guard, và accessible qua publicURL ■ 1Dockerfile (multi-stage, uv, <500MB)+ docker-compose cho agent + dependencies ■ 1deployed instance trên Railway hoặc Render ■ 1health check endpoint…

**Đọc như kỹ sư:** DeliverableCuối Ngày Artifactpack cần nộp Agent đã được containerize và deploy lên cloud, có health check endpoint, basic authentication,cost guard, và accessible qua publicURL

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- 1Dockerfile (multi-stage, uv, <500MB)+ docker-compose cho agent + dependencies
- 1health check endpoint (/health)+ streaming endpoint (SSE)
- 1public URL mà bất kỳ aicũng có thể truy cập vàdùng agent

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 5 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 8 Localhost → production gap · Evidence & failure lens

> Trích slide Slide 8: DevEnvironment ̸=ProductionEnvironment Khíacạnh Dev(localhost) Production Dependencies “pipinstall” thủ công Đónggói cùng container Config.envfile trên máy Environment variables, secrets manager Networking localhost:8000 HTTPS,domain, load balancer Users 1(chính mình) Nusers đồng thời Failure Restartthủ công…

**Đọc như kỹ sư:** DevEnvironment ̸=ProductionEnvironment Khíacạnh Dev(localhost) Production Dependencies “pipinstall” thủ công Đónggói cùng container Config.envfile trên máy Environment variables, secrets manager Networking localhost:8000 HTTPS,domain, load balancer Users 1(ch

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 8 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"933f9b10-e9fd-55d8-a3e2-3c468d3d7b8c","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Agent khác web app truyền thống","source_file":"day-12.html"},"checksum":"f88074d5c1a465e5fa465bd99aedae72dcec65186fe83d3d1feb305763bb2153"} -->

## 02 Agent khác web app truyền thống

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 9 Agent khác web app truyền thống · Mental model & quyết định

> Trích slide Slide 9: AgentKhông Phải WebApp BìnhThường MộtCRUDapptrảlờitrong <1s. Agentthìkhácvềbảnchất—vàđólànguồngốccủamọithách thứcdeploy hôm nay. 1. Long-running Reasoning loop chạy 10–60s+ (có khi vài phút). Phá vỡ timeout 29–60s của gate- way/proxy. 2. Stateful Có conversation mem- ory + tool history. Mâu thuẫnvớiquytắc“state- less process”…

AgentKhông Phải WebApp BìnhThường MộtCRUDapptrảlờitrong <1s.. Điểm nối sang production là: timeout của gateway phải dài hơn p95 hoặc chuyển tác vụ sang async. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Agentthìkhácvềbảnchất—vàđólànguồngốccủamọithách thứcdeploy hôm nay.
- Long-running Reasoning loop chạy 10–60s+ (có khi vài phút).
- Stateful Có conversation mem- ory + tool history.

#### Tự kiểm tra · Với agent khác web app truyền thống, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là timeout của gateway phải dài hơn p95 hoặc chuyển tác vụ sang async.

### Slide 13 Agent khác web app truyền thống · Evidence & failure lens

> Trích slide Slide 13: Before/ After — Monolith CRUDvs Agent AppCRUD truyền thống AIAgent Kiểmthử Unittest, assert chính xác Eval gate(golden set, LLM-judge), gatetheo điểm Chiphí CPU/RAM-hour, đoán trước được Token/request,chỉbiếtsaukhichạy Latency Mili-giây,đồng bộ Giây–phút, streaming (SSE) + async State DBrows Hộithoại / memory (checkpointer)…

**Đọc như kỹ sư:** Before/ After — Monolith CRUDvs Agent AppCRUD truyền thống AIAgent Kiểmthử Unittest, assert chính xác Eval gate(golden set, LLM-judge), gatetheo điểm Chiphí CPU/RAM-hour, đoán trước được Token/request,chỉbiếtsaukhichạy Latency Mili-giây,đồng bộ Giây–phút, stre

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 13 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 17 Agent khác web app truyền thống · Evidence & failure lens

> Trích slide Slide 17: ContainerLà Gì? Container Application code Dependencies (Python,libs) Runtime config MinimalOS layer (Debian slim /distroless) Laptop CloudVM Kubernetes Ýchính: Container= app + deps +runtime đóng gói thành 1 unit.Build1 lần, chạy ở mọinơi. Giảngviên (VinUni) AICB· Deployment 2026 12/ 84

**Đọc như kỹ sư:** Container Application code Dependencies (Python,libs) Runtime config MinimalOS layer (Debian slim /distroless) Laptop CloudVM Kubernetes Ýchính: Container= app + deps +runtime đóng gói thành 1 unit.Build1 lần, chạy ở mọinơi.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 17 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"800a0c90-ebdf-52a3-a37a-11b0f828a86e","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Container & image hygiene","source_file":"day-12.html"},"checksum":"604ac808a2761039e0f71a8df61ecc87cfcdf90d1af6bd1b4b464d086f959e60"} -->

## 03 Container & image hygiene

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 18 Container & image hygiene · Mental model & quyết định

> Trích slide Slide 18: Dockerfile2026 — Multi-Stage +uv # Stage 1: build deps with uv (Rust-fast, ~10x pip) FROM python:3.12-slim AS builder COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ WORKDIR /app ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0 RUN --mount= type=cache,target=/root/.cache/uv \ --mount= type=…

ENV PATH= "/app/.venv/bin:$PATH" RUN useradd -m app && chown -R app /app USER app # non-root CMD [ "fastapi", "run", "main.py", "--host", "0.0.0.0"] Lưuý: Target <500MB: uv+cache, --locked,non-root,.dockerignore.. Điểm nối sang production là: container tạo environment parity nhưng không tự tạo reliability.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- ImageSecurity — Scan, Non-Root, SBOM 3việc bắt buộc 1.
- ScanCVE: Trivy/ Docker Scout / Grypetrước khi deploy 2.
- Non-root: USER app,không chạy roottrong container 3.

#### Tự kiểm tra · Với container & image hygiene, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là container tạo environment parity nhưng không tự tạo reliability.

### Slide 22 Container & image hygiene · Evidence & failure lens

> Trích slide Slide 22: HìnhHài Một Agent Service TốiThiểu from fastapi import FastAPI from sse_starlette.sse import EventSourceResponse app = FastAPI() @app.get("/healthz") # health check for LB / Cloud Run def healthz(): return {"status": "ok"} @app.post("/chat") # streaming is the default, not the exception async def chat(req: ChatRequest): async…

**Đọc như kỹ sư:** HìnhHài Một Agent Service TốiThiểu from fastapi import FastAPI from sse_starlette.sse import EventSourceResponse app = FastAPI() @app.get("/healthz") # health check for LB / Cloud Run def healthz(): return {"status": "ok"} @app.post("/chat") # streaming is the

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 22 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 26 Container & image hygiene · Evidence & failure lens

> Trích slide Slide 26: KhiQuá Lâu — Chuyển SangAsync Job Client API (submit) JobQueue (Redis/Celery) Worker (agentloop) POST job_id poll/ webhook ■ Submit-and-poll: APItrả job_idngay,client hỏi kết quảsau (hoặc nhận webhook) ■ Tool:Celery(broker),RQ(Redis),CloudTasks (managed) ■ Batchlớn không gấp?BatchAPI rẻhơn 50%: OpenAI trả trong24h;Anthropic…

**Đọc như kỹ sư:** KhiQuá Lâu — Chuyển SangAsync Job Client API (submit) JobQueue (Redis/Celery) Worker (agentloop) POST job_id poll/ webhook

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Submit-and-poll: APItrả job_idngay,client hỏi kết quảsau (hoặc nhận webhook)
- Tool:Celery(broker),RQ(Redis),CloudTasks (managed)
- Batchlớn không gấp?BatchAPI rẻhơn 50%: OpenAI trả trong24h;Anthropic cũng 50% nhưngphần lớn xongdưới1 giờ

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 26 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"06789b5f-2e32-5854-81b9-5bad2d999518","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Long-running và streaming","source_file":"day-12.html"},"checksum":"1cd0ce565fde161b8c4ecda8e51fceac006c53f187ebdcf50c674e4566d962bf"} -->

## 04 Long-running và streaming

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 27 Long-running và streaming · Mental model & quyết định

> Trích slide Slide 27: Statefulness— Mâu Thuẫn Với “Stateless” 12-factornói agent phải stateless đểscale. Nhưng agentcómemory. Giải pháp:externalize state,không giữ trên instance. Externalizeở đâu ■ Conversation/session →Redis/ Postgres ■ LangGraphcheckpointer (PostgresSaver)keyed bằng thread_id ■ Bấtkỳ instance nào cũng phụcvụ đượcrequest →scaletự…

Statefulness— Mâu Thuẫn Với “Stateless” 12-factornói agent phải stateless đểscale.. Điểm nối sang production là: health phải tách liveness khỏi readiness. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Giải pháp:externalize state,không giữ trên instance.
- LangGraphcheckpointer (PostgresSaver)keyed bằng thread_id
- Bấtkỳ instance nào cũng phụcvụ đượcrequest →scaletự do Durableexecution (2025–26) Cho agent chạy nhiều bước/nhiều ngày, resumesau crash

#### Tự kiểm tra · Với long-running và streaming, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là health phải tách liveness khỏi readiness.

### Slide 31 Long-running và streaming · Evidence & failure lens

> Trích slide Slide 31: ĐiểmMấu Chốt: “Client-Side”Hiếm Khi Là Keyless Browser (UIagent) Backendproxy (BFF) LLMprovider (OpenAI/Claude) request +API key keythêm ở đây, KHÔNGbao giờ xuống browser Lưu ý:Build toolnhúngbiến VITE_/NEXT_PUBLIC_ thẳng vào JS bundle→key ship xuốngtrìnhduyệtvà bịlấycắp. Vìvậyngaycảagent“client-side”vớimodelfrontier vẫn cần…

**Đọc như kỹ sư:** Vìvậyngaycảagent“client-side”vớimodelfrontier vẫn cần backend proxy(Backend-for-Frontend) + rate limit.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Chỉon-device / in- browsermodel mớithật sự keyless.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 31 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 34 Long-running và streaming · Evidence & failure lens

> Trích slide Slide 34: 4TierDeployment (2026) Tier0 Managedagent runtime Tier1 Railway/ Render Fly.io Tier2 CloudRun / ECSFargate Tier3 Kubernetes self-managed Khôngquản infra AgentCore/Vertex (Tier0) <10phút deploy MVP/ demo Auto-scale Production Fullcontrol Large-scale Chokhoá học Bắt đầu Tier 1 (Railway/Render). Hiểu flow deploy trước, migrate…

**Đọc như kỹ sư:** Hiểu flow deploy trước, migrate lên Tier 2/3 khi businesscần, hoặc Tier0 nếumuốn bỏ qua việc quản hạtầng.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 34 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"d312fabd-27a7-5c29-92a5-b4625d520680","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 State, session & durability","source_file":"day-12.html"},"checksum":"69ca82f48e0b7867f57e8a0f66f4e8e1dfc809f09ed83000cc431851cefb7f49"} -->

## 05 State, session & durability

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 35 State, session & durability · Mental model & quyết định

> Trích slide Slide 35: SoSánh Platform — Theo TrụcTimeout Platform Maxrequest/runtime Scale-to-0 GPU Agentfit Railway 15phút / ∞private Không Không OK(route nội bộ) Render ∼100phút (?) Freetier Không OK Fly.io 60sidle (stream reset) Có Có OK+ streaming CloudRun 60phút Có(cả GPU) L4 Mạnh AWSApp Runner ∼120s Provisioned Không Deprecated ECSFargate…

Con số∼100 phút của Renderkhông có trongdocs chính thức(chỉtrong bài so sánh marketing)— đừng thiết kế dựa vàonó.. Điểm nối sang production là: retry chỉ an toàn khi tool call idempotent. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- ServerlessFunctions — Tại Sao KhôngHợp Agent Vercel/ Lambda functions
- Hardcap 5phút (Hobby/mặc định);GA 800s, beta 1800s→rồi 504
- Stateless— mất context giữa các invoke Container-basedhợp hơn

#### Tự kiểm tra · Với state, session & durability, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là retry chỉ an toàn khi tool call idempotent.

### Slide 39 State, session & durability · Evidence & failure lens

> Trích slide Slide 39: 07 Managed Agent Runtimes (Tier 0) Danh mục mới hẳn của 2025–26: deploy agent màkhông phải quản container— runtime, memory, identity đều managed

**Đọc như kỹ sư:** 07 Managed Agent Runtimes (Tier 0) Danh mục mới hẳn của 2025–26: deploy agent màkhông phải quản container— runtime, memory, identity đều managed

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 39 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 43 State, session & durability · Evidence & failure lens

> Trích slide Slide 43: Tier0 Tính TiềnThế Nào— TrụcChi Phí ThứBa Tier0 thêmđồnghồ thứ haibêncạnh token: thờigian thựccủasession. Platform Đồnghồ tính tiền AWSAgentCore $0,0895/vCPU-giờ + $0,00945/GB-giờ — chỉ tính computeactive; idle& I/O-waitmiễnphí. Gateway $0,005/1.000 invocation Claude Managed Agents Giátoken chuẩn+$0,08/session-giờ,chỉ tính khi…

**Đọc như kỹ sư:** Tier0 Tính TiềnThế Nào— TrụcChi Phí ThứBa Tier0 thêmđồnghồ thứ haibêncạnh token: thờigian thựccủasession.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Platform Đồnghồ tính tiền AWSAgentCore $0,0895/vCPU-giờ + $0,00945/GB-giờ — chỉ tính computeactive; idle& I/O-waitmiễnphí.
- Chọn Tier 0 chỉ cần hỏimột câu: đồng hồ có chạy khi agent đang chờ không?

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 43 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"21af0341-e687-583a-a0ee-d4adabbf8e68","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Cloud deployment options","source_file":"day-12.html"},"checksum":"41a9c2487f20d63ff1e54a8d43862240e10b949ef3b41b1661b3d6e8045b1a50"} -->

## 06 Cloud deployment options

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 44 Cloud deployment options · Mental model & quyết định

> Trích slide Slide 44: RuntimeCũng Là Dependency Bạn KhôngKiểm Soát Bằngchứng trong chính bài này ■ OpenAIAgent Builderđóng 30/11/2026—vòng đời13tháng. Lối thoát: Agents SDK. ■ OpenAIEvals cùnglịch →trỏsang Promptfoo. ■ AWSApp Runner →ECSExpress Mode. ■ LangGraphPlatform →LangSmith Deployment: đổi tên cũnglà rủi ro — docs/IaCcủa bạn trỏ tên cũ.…

RuntimeCũng Là Dependency Bạn KhôngKiểm Soát Bằngchứng trong chính bài này. Điểm nối sang production là: cost guard là control plane chứ không phải prompt. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- OpenAIAgent Builderđóng 30/11/2026—vòng đời13tháng.
- LangGraphPlatform →LangSmith Deployment: đổi tên cũnglà rủi ro — docs/IaCcủa bạn trỏ tên cũ.
- Thoátbằng đường nào?Export đượcstate/config không?

#### Tự kiểm tra · Với cloud deployment options, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là cost guard là control plane chứ không phải prompt.

### Slide 48 Cloud deployment options · Evidence & failure lens

> Trích slide Slide 48: “OpenSource” Không Có Nghĩa LàTự Host Được Miễn Phí Bạntự host để tránh lock-in. Nhưng licence củaserverthườngkhác licence củalibrary. Thànhphần Giấyphép Ràngbuộc khi self-host LangGraph(library lõi) MIT Tựdo langgraph-api (server) Elastic-2.0 Cầnlicensekey+egresstới beacon.langchain.com (cóchế độ air-gapped) n8n Sustainable…

**Đọc như kỹ sư:** “OpenSource” Không Có Nghĩa LàTự Host Được Miễn Phí Bạntự host để tránh lock-in.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nhưng licence củaserverthườngkhác licence củalibrary.
- —VàOSS cóthểđóng lại: Daytona đóng mãlớp sandbox ngày11/6/2026.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 48 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 52 Cloud deployment options · Evidence & failure lens

> Trích slide Slide 52: OAuth2.1 Cho MCP — BaCái Bẫy Spec Gọi Tên Bẫy1 — Tokenpassthrough ServerMUSTNOT nhậntokenkhôngđược cấpriêng cho nó. Speccấmrõ ràng. Vìsaonguyhiểm: nó vôhiệuhoáratelim- itingvà audit trailởservice phía sau. Bẫy2 — Confused deputy Proxyphảigiữregistry client_idđãduyệt theotừng user,kiểm tra trước mỗi flow. Xácthực đúng user…

**Đọc như kỹ sư:** OAuth2.1 Cho MCP — BaCái Bẫy Spec Gọi Tên Bẫy1 — Tokenpassthrough ServerMUSTNOT nhậntokenkhôngđược cấpriêng cho nó.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Vìsaonguyhiểm: nó vôhiệuhoáratelim- itingvà audit trailởservice phía sau.
- Bẫy2 — Confused deputy Proxyphảigiữregistry client_idđãduyệt theotừng user,kiểm tra trước mỗi flow.
- Bẫy3 — Discovery đã đổi Từ 2025-11-25 theo RFC 9728: WWW-Authenticate nay tuỳ chọn, fall- backvề.well-known.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 52 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"0823f034-f414-5798-86a2-0f0ed4f70287","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 Managed agent runtimes","source_file":"day-12.html"},"checksum":"deaa6878707e69951a48ec2a76f6b541f03884732049b367bc09130a89a1aeb4"} -->

## 07 Managed agent runtimes

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 53 Managed agent runtimes · Mental model & quyết định

> Trích slide Slide 53: ServerMCP Là API Thật —Ba CVE Đã Chứng Minh CVE Bàihọc deploy CVE-2026-33032 nginx-ui,CVSS 9,8 đang bị khai thác /mcp có AuthRequired(), /mcp_message thì không → 12 tool khôngcần credential, chiếm server trong2request. → Xác thực MỌI route.Lỗi deploy kinh điển, không phải lỗi protocol. CVE-2025-6514 mcp-remote,9,6 Command…

ServerMCP Là API Thật —Ba CVE Đã Chứng Minh CVE Bàihọc deploy CVE-2026-33032 nginx-ui,CVSS 9,8 đang bị khai thác /mcp có AuthRequired(), /mcp_message thì không → 12 tool khôngcần credential, chiếm server trong2request.. Điểm nối sang production là: scale theo concurrency và token throughput, không chỉ CPU.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- → Xác thực MỌI route.Lỗi deploy kinh điển, không phải lỗi protocol.
- CVE-2025-6514 mcp-remote,9,6 Command injection trong chínhOAuth proxy: chỉ cần kết nối tớiserver độc hại là RCEtrên máy client.
- CVE-2025-68143/4/5 GitMCP server (Anthropic) Pathtraversal + argument injection;git_init bịgỡ hẳn.

#### Tự kiểm tra · Với managed agent runtimes, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là scale theo concurrency và token throughput, không chỉ CPU.

### Slide 57 Managed agent runtimes · Evidence & failure lens

> Trích slide Slide 57: AuthenticationPatterns APIKey Đơngiản nhất. Header: X-API-Key Dùng khi:internal, MVP, B2B(M2M) JWTToken Statelessauth. Bearertoken + expiry Dùng khi: user-facing app,microservices OAuth2.1 Delegatedauth + PKCE. Chuẩn cho MCP/agent remote Dùng khi: platform, re- moteMCP Lưu ý:Cho MVP:API keylà đủ. Đừng over-engineer auth trước…

**Đọc như kỹ sư:** Header: X-API-Key Dùng khi:internal, MVP, B2B(M2M) JWTToken Statelessauth.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Bearertoken + expiry Dùng khi: user-facing app,microservices OAuth2.1 Delegatedauth + PKCE.
- Chuẩn cho MCP/agent remote Dùng khi: platform, re- moteMCP Lưu ý:Cho MVP:API keylà đủ.
- Đừng over-engineer auth trước khi có user thật.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 57 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 60 Managed agent runtimes · Evidence & failure lens

> Trích slide Slide 60: DữLiệu Chạy Ở Đâu —Residency,ZDR & Compliance Gatewaylo auth, rate limit, cost. Còn một trục nữanhiều team chỉ phát hiện lúcký hợp đồng:dữ liệunằm ở đâu và tồntại bao lâu. OpenAI ■ 11region lưutrữ at-rest, nhưng chỉ US/ EU / UAExửlý inference trong vùng ■ Bậttheo project bằngprefixdomain (eu.api.openai.com);phụphí 10% ■…

**Đọc như kỹ sư:** DữLiệu Chạy Ở Đâu —Residency,ZDR & Compliance Gatewaylo auth, rate limit, cost.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Còn một trục nữanhiều team chỉ phát hiện lúcký hợp đồng:dữ liệunằm ở đâu và tồntại bao lâu.
- 11region lưutrữ at-rest, nhưng chỉ US/ EU / UAExửlý inference trong vùng
- Bậttheo project bằngprefixdomain (eu.api.openai.com);phụphí 10%

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 60 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"f85bbe8b-c511-582c-89e2-304f3884aaa6","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 MCP server hosting","source_file":"day-12.html"},"checksum":"009a91387100b23d49861501a61327c73755b7b7ea2fded589b63ac9ff9a977e"} -->

## 08 MCP server hosting

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 61 MCP server hosting · Mental model & quyết định

> Trích slide Slide 61: HardCap Thật Sự Nằm ỞĐâu? Nhàcung cấp Hard cap native? Cơ chế Bẫy OpenAI Có, phải bật thủ công HardSpendLimitở cảorglẫnproject, trả429 “Spend alert” và trường monthly- budgetcũ chỉbáo, không chặn Anthropic Có,thật sự cứng Trần theo tier ($500 / $1.000 / $200.000); chạm trần → API tạm dừngtới tháng sau Có spend limittheo…

“Cứng theo thiết kế” ̸= “cứng ở version bạn đang deploy” — hãy tự test.. Điểm nối sang production là: secrets phải ở secret manager, không nằm trong image. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- 10 Scaling & Reliability Agent MVP không cần Kubernetes — nhưng cần hiểu cơ bản về scaling và reliability để hệ thống không chết khi có nhiều user hơn
- HorizontalScaling — Scale Theo Concurrency,Không Phải CPU Users Load Balancer Instance1 Instance2 Instance3 Shared State(DB) Lưu ý: Agent làI/O-bound: một instance có thể đầy request đang chờ LLM mà CPUvẫnthấp.
- →Autoscaletheo concurrency/queuedepth (Knative,KEDAtheo tínhiệuvLLM num_requests_running,RayServe target_ongoing_requests),không theoCPU.

#### Tự kiểm tra · Với mcp server hosting, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là secrets phải ở secret manager, không nằm trong image.

### Slide 65 MCP server hosting · Evidence & failure lens

> Trích slide Slide 65: Zero-DowntimeDeploy & Graceful Shutdown Step1 Startnew instancev2 Step2 Healthcheck passes Step3 Routetraffic tov2 Step4 Drain+ stop v1(SIGTERM) Lưu ý: Graceful shutdown cho agent:khi nhận SIGTERM, phảidrain request đangchạydở(mộtagentturncóthểdài). Đặt terminationGracePeriodSeconds lớn hơnworst-case agent turn,nếu không…

**Đọc như kỹ sư:** Zero-DowntimeDeploy & Graceful Shutdown Step1 Startnew instancev2 Step2 Healthcheck passes Step3 Routetraffic tov2 Step4 Drain+ stop v1(SIGTERM) Lưu ý: Graceful shutdown cho agent:khi nhận SIGTERM, phảidrain request đangchạydở(mộtagentturncóthểdài).

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Đặt terminationGracePeriodSeconds lớn hơnworst-case agent turn,nếu không request bị cắt giữachừng.
- Nângcao Rainbow deployment(Anthropic): dịch traffic dần sang version mới nhưnggiữ cả hai cùng chạy, để không cắt ngang agent đang chạy dở — vì agent là hệ thống stateful chạy gần như liên tục.
- Argo Rollouts: shift traffic + AnalysisRun tự rollback.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 65 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 69 MCP server hosting · Evidence & failure lens

> Trích slide Slide 69: Model: Gọi API HayTự Phục Vụ? —Quyết Định Deploy Thứ Hai Bốnlực đẩy sang tự host ■ Residency/ compliance: dữ liệu khôngđược rời lãnh thổ hoặcVPC ■ Sởhữu adapterfine-tune(Bedrock CustomModel Importlàmmờ ranh giới) ■ Kinhtế theo volume: chỉ thắng khi GPUđủ bận (hoà vốn: Day 25);trần nănglực khôngcòn là rào — slide sau Balực giữ…

**Đọc như kỹ sư:** —Quyết Định Deploy Thứ Hai Bốnlực đẩy sang tự host

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Residency/ compliance: dữ liệu khôngđược rời lãnh thổ hoặcVPC
- Sởhữu adapterfine-tune(Bedrock CustomModel Importlàmmờ ranh giới)
- Kinhtế theo volume: chỉ thắng khi GPUđủ bận (hoà vốn: Day 25);trần nănglực khôngcòn là rào — slide sau Balực giữ ở hosted API

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 69 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"bbef0ad1-bf63-5681-a8ce-26b802d79020","locator":{"kind":"html_section","section_id":"c8","order":11,"heading":"09 API gateway & security","source_file":"day-12.html"},"checksum":"e0ad199217b44f7bd3b0d44e6b85d83719ac4f26f3676cb6a2c4fca87c95cea9"} -->

## 09 API gateway & security

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 70 API gateway & security · Mental model & quyết định

> Trích slide Slide 70: NếuTự Host: ChọnModel Mở Nào, Engine Nào Modelmở đáng deploy (8/2026) ■ gpt-oss-120b —117Btổng / 5,1Bactive (MoE),Apache-2.0, vừamộtGPU 80GBnhờ MXFP4 ■ gpt-oss-20b —chạy trong16GB:tầng phần cứngphổ thông ■ Qwen3-235B-A22B—235B/22B, Apache-2.0 ■ DeepSeek-V3.2-Exp—685B, MIT ■ KimiK2 —1T/32B, Modified MIT,thiết kế cho…

NếuTự Host: ChọnModel Mở Nào, Engine Nào Modelmở đáng deploy (8/2026). Điểm nối sang production là: eval gate bổ sung cho unit test, không thay thế unit test. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- gpt-oss-120b —117Btổng / 5,1Bactive (MoE),Apache-2.0, vừamộtGPU 80GBnhờ MXFP4
- gpt-oss-20b —chạy trong16GB:tầng phần cứngphổ thông
- KimiK2 —1T/32B, Modified MIT,thiết kế cho agentictool-use MoE: VRAM quyết bởi active params, không phải tổng.

#### Tự kiểm tra · Với api gateway & security, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là eval gate bổ sung cho unit test, không thay thế unit test.

### Slide 74 API gateway & security · Evidence & failure lens

> Trích slide Slide 74: PrefixCaching + Speculative Decoding Prefix/ prompt caching Prefill của prefix chung tínhmột lần, dùng lạicho nhiều request. ■ Prefillcủa prefix tínhmộtlần rồitái dùng →đặtphần tĩnh(system, few-shot,RAG) lênđầuprompt. (Giá cache: mục Cache ở slide trước.) Speculativedecoding Model nháp nhỏ đề xuất 5–8 token, model đíchxácminh…

**Đọc như kỹ sư:** PrefixCaching + Speculative Decoding Prefix/ prompt caching Prefill của prefix chung tínhmột lần, dùng lạicho nhiều request.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Prefillcủa prefix tínhmộtlần rồitái dùng →đặtphần tĩnh(system, few-shot,RAG) lênđầuprompt.
- (Giá cache: mục Cache ở slide trước.) Speculativedecoding Model nháp nhỏ đề xuất 5–8 token, model đíchxácminh song song.
- Tậndụng GPU đang rảnh,khôngđổi phânphối output

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 74 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 78 API gateway & security · Evidence & failure lens

> Trích slide Slide 78: EvalGate TrongThực Tế— Bốn Công Cụ, Một Khuôn Côngcụ Cơchế gate Kếtquả trên PR promptfoo promptfoo eval --fail-on-error ; chặt hơn: fail khi stats.failures > 0 promptfoo-action comment pass/fail + linkviewer DeepEval assert_test()(khôngphải evaluate())—raisekhi score <threshold pytest-native,fail như test thường Langfuse…

**Đọc như kỹ sư:** Mẫuđã hội tụ Cả bốn công cụ đi tới cùng một chỗ: so vớirun của nhánh baseline, không chỉ so với một ngưỡng tuyệt đối — ngưỡng tuyệt đối không phát hiện được “tụt 4 điểm nhưng vẫn trên ngưỡng”.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Phương pháp đánh giá → Day 14; quan sát production → Day 13.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 78 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"bca19b6f-9d3e-5dfb-b67e-8a7b8c7c123d","locator":{"kind":"html_section","section_id":"c9","order":12,"heading":"10 Scaling và GPU economics","source_file":"day-12.html"},"checksum":"6bf935a20e31d5f0437f1d16e473bd9804c9c994c950d855eb340ba121017567"} -->

## 10 Scaling và GPU economics

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 79 Scaling và GPU economics · Mental model & quyết định

> Trích slide Slide 79: Shadow →Canary →100%— Ramp Cho Agent Shadow mirrortraffic, output BỎ ĐI Canary5% outputTHẬT tới user Ramp 10 →25 →100% ■ Shadow(mirror): nhânđôitrafficsangversionmới, khôngbaogiờ trảoutputchouser. Rủi rouser = 0. ■ Canary: địnhtuyến một% traffic thậtvà có trảoutput — bán kính thiệthại giới hạn. ■ Auto-rollbacklàprimitive có…

Shadow →Canary →100%— Ramp Cho Agent Shadow mirrortraffic, output BỎ ĐI Canary5% outputTHẬT tới user Ramp 10 →25 →100%. Điểm nối sang production là: streaming cải thiện perceived latency nhưng không giảm compute. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Shadow(mirror): nhânđôitrafficsangversionmới, khôngbaogiờ trảoutputchouser.
- Canary: địnhtuyến một% traffic thậtvà có trảoutput — bán kính thiệthại giới hạn.
- Auto-rollbacklàprimitive có thật: Argo RolloutsAnalysisRun queryPrometheus theo lịch, tựrollback khi metric fail.

#### Tự kiểm tra · Với scaling và gpu economics, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là streaming cải thiện perceived latency nhưng không giảm compute.

### Slide 83 Scaling và GPU economics · Evidence & failure lens

> Trích slide Slide 83: AgentCó Nhiều “Hình Dạng” —Mỗi Cái Deploy Khác Nhau Hìnhdạng Trigger Vòngđời Scale State Chatbotđồng bộ userrequest giây(timeout) per-request sessionstore Cron/ nền scheduler phút thấp,định kỳ jobstate Batch dataset/queue dài,async fan-out per-item idempo- tent Autonomous“chạy mãi” loop liên tục vôhạn 1actor/goal phải sống qua…

**Đọc như kỹ sư:** Multi-agent: tốn∼15× token; nguyên tắc vàng “read thì song song được, write thì không”— scale 1 agent trước,chỉ tách khi chạm trần thật.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 83 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 86 Scaling và GPU economics · Evidence & failure lens

> Trích slide Slide 86: DurableExecution — Ghi Lại QuyếtĐịnh, Đừng Chạy Lại Model Agentcrash ở bước 7 (sau4 tool call). Chạylại từ đầu =trảtiền LLM lần nữa+lặp tool đã ghi đĩa. Durable execution giảiquyết bằng một mẹo tinh tế: Journal+ replay Temporal / Restate / Inngest: ghioutput của LLMvàojournalởlầnđầu;khireplaythì đọc lạibản ghi,KHÔNGgọi lại…

**Đọc như kỹ sư:** DurableExecution — Ghi Lại QuyếtĐịnh, Đừng Chạy Lại Model Agentcrash ở bước 7 (sau4 tool call).

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Chạylại từ đầu =trảtiền LLM lần nữa+lặp tool đã ghi đĩa.
- Durable execution giảiquyết bằng một mẹo tinh tế: Journal+ replay Temporal / Restate / Inngest: ghioutput của LLMvàojournalởlầnđầu;khireplaythì đọc lạibản ghi,KHÔNGgọi lại model.
- Bướcđã xong được memoize, bỏqua Lưu ý:LangGraph là ngoại lệ:check- point ở mứcnode, không phải từng call → node chưa xong sẽchạy lại cả LLM call.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 86 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"a42c3915-130b-5506-b930-fe93c6621563","locator":{"kind":"html_section","section_id":"c10","order":13,"heading":"11 CI/CD với eval gate","source_file":"day-12.html"},"checksum":"ab2a16f9ddc8a8c2f535c2094ab55f53a7896906800674a0dfa308c5371deb12"} -->

## 11 CI/CD với eval gate

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 87 CI/CD với eval gate · Mental model & quyết định

> Trích slide Slide 87: Saga& Hành Động Không ThểHoàn Tác Giữchỗ Trừtiền Gửivé (pivot) Ghilog compensate(undo) ■ Saga: mỗibước có một bướcbùtrừ (undo)— không có rollback tựđộng, phải tự code ■ Bướckhônghoàn tác được(gửimail/vé) =pivot: đặtcuối+gate bằnghumanapproval ■ Vấnđề: agent tựchọn thứ tự hành động —runtime có nêncấmnóxếp việc bất khả hoàn…

Saga& Hành Động Không ThểHoàn Tác Giữchỗ Trừtiền Gửivé (pivot) Ghilog compensate(undo). Điểm nối sang production là: externalize state thay vì dùng sticky session. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Saga: mỗibước có một bướcbùtrừ (undo)— không có rollback tựđộng, phải tự code
- Bướckhônghoàn tác được(gửimail/vé) =pivot: đặtcuối+gate bằnghumanapproval
- Vấnđề: agent tựchọn thứ tự hành động —runtime có nêncấmnóxếp việc bất khả hoàn trướcpivot?

#### Tự kiểm tra · Với ci/cd với eval gate, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là externalize state thay vì dùng sticky session.

### Slide 91 CI/CD với eval gate · Evidence & failure lens

> Trích slide Slide 91: DanhTính Cho Agent — SPIFFEVà Agent Identity Cơchế đang thành chuẩn Service account không đủ: agent phù du, bán kính lớn, key chung không truy vết được. ■ SPIFFE(CNCF):X.509SVID ngắn hạn,có attestation. ■ GoogleAgent Identity(4/2026): principalhạngnhất,tách khỏi human lẫnservice account; cert xoay vòng, hạn24h. Mộtagent phải…

**Đọc như kỹ sư:** DanhTính Cho Agent — SPIFFEVà Agent Identity Cơchế đang thành chuẩn Service account không đủ: agent phù du, bán kính lớn, key chung không truy vết được.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- SPIFFE(CNCF):X.509SVID ngắn hạn,có attestation.
- GoogleAgent Identity(4/2026): principalhạngnhất,tách khỏi human lẫnservice account; cert xoay vòng, hạn24h.
- Tớitài nguyêncủauser: 3-legged OAuth;tới agentkhác: mTLS+ DPoP Lưuý: OAuth2.1thuần khôngdiễnđạtđược “agent nàohànhđộngthayusernày”.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 91 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 95 CI/CD với eval gate · Evidence & failure lens

> Trích slide Slide 95: 15 Phụ Lục Thực Hành — Lệnh & Code Gói lại thành thứ gõ được ngay: lệnh deploy thật, và một cost- guard tối thiểu — để rời lớp học là deploy được

**Đọc như kỹ sư:** 15 Phụ Lục Thực Hành — Lệnh & Code Gói lại thành thứ gõ được ngay: lệnh deploy thật, và một cost- guard tối thiểu — để rời lớp học là deploy được

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 95 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"4db1d6c3-5aba-5ef9-8add-6e07db49d8c7","locator":{"kind":"html_section","section_id":"c11","order":14,"heading":"12 Production checklist & Lab 12","source_file":"day-12.html"},"checksum":"d932313811271b1e755d4805253673bf34dc2d0a78dfcd731451bf771474ec4f"} -->

## 12 Production checklist & Lab 12

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 96 Production checklist & Lab 12 · Mental model & quyết định

> Trích slide Slide 96: DeployThật — Cloud Run &Railway # A) Google Cloud Run: build from source, then deploy gcloud run deploy agent-svc -- source. \ --port 8080 --concurrency 8 --memory 1Gi \ --region asia-southeast1 --allow-unauthenticated \ --set-env-vars MODEL_ID=claude-...,MAX_USD_PER_REQ=0.05 \ --set-secrets…

DeployThật — Cloud Run &Railway # A) Google Cloud Run: build from source, then deploy gcloud run deploy agent-svc -- source.. Điểm nối sang production là: timeout của gateway phải dài hơn p95 hoặc chuyển tác vụ sang async. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- " \ --set "ANTHROPIC_API_KEY= sk-..." Lưuý: --concurrencyđểthấpchoagent: mỗirequestgiữmộtconnectionstreaming dài.
- Secret tiêm qua --set-secrets / Variables tab —không bao giờnhét vào image.
- Cost-GuardTối Thiểu — Chặn TrướcKhi Gọi MAX_USD = float(os.environ["MAX_USD_PER_REQ"]) # e.g.

#### Tự kiểm tra · Với production checklist & lab 12, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là timeout của gateway phải dài hơn p95 hoặc chuyển tác vụ sang async.

### Slide 100 Production checklist & Lab 12 · Evidence & failure lens

> Trích slide Slide 100: BlueprintCần Nộp Container ■ Dockerfile(multi-stage, uv, <500MB) ■ docker-compose.yml+.dockerignore ■ Healthcheck + streaming endpoint ■ Trivyscan sạch (no high CVE) Deployment ■ PublicURL hoạt động (HTTPS) ■ Envvars đúng cách (không hardcode) ■ Basicauth (API key) + costguard ■ Demorequest/response streaming Lưu ý: Không cần…

**Đọc như kỹ sư:** Demorequest/response streaming Lưu ý: Không cần enterprise-grade.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Điều cần chứng minh là bạnbiết cách đưa agenttừ localhost lên cloud,nó hoạt động, vàkhôngđốt tiền.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 100 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 104 Production checklist & Lab 12 · Evidence & failure lens

> Trích slide Slide 104: Hỏi& Đáp Từ hôm nay, agent không còn chỉ chạy trên máy bạn. Nó đã là một service thật sự — có URL, có bảo vệ, và không đốt sạch ngân sách.

**Đọc như kỹ sư:** Hỏi& Đáp Từ hôm nay, agent không còn chỉ chạy trên máy bạn.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Nó đã là một service thật sự — có URL, có bảo vệ, và không đốt sạch ngân sách.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 104 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"89c96d0b-3ea4-5db4-a26e-06be9d3da8eb","locator":{"kind":"html_section","section_id":"ladder","order":15,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"day-12.html"},"checksum":"9a76528c5c45c523962f0e7c14d5bc4edfd157051604c6740480ae6f70fde189"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của Production deployment bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"9a973857-2b94-5e95-8f76-49f735049ff3","locator":{"kind":"html_section","section_id":"section-016","order":16,"heading":"∑ Phòng mô phỏng quyết định","source_file":"day-12.html"},"checksum":"ed8d7ff7a683bac97da4cb324059b8fd0d57e4ce908c5d04ea380b276f5b78d3"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Capacity & queue — khi nào agent bắt đầu nghẽn?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Lưu lượng:**: min `1`, max `100`, step `1`, default `20`

- **Control - Thời gian xử lý:**: min `1`, max `60`, step `1`, default `12`

- **Control - Worker:**: min `1`, max `200`, step `1`, default `80`

- **Control - Mục tiêu sử dụng:**: min `40`, max `95`, step `5`, default `70`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Cost guard — một thay đổi prompt đáng giá bao nhiêu?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Input token/request:**: min `200`, max `20000`, step `100`, default `4000`

- **Control - Output token/request:**: min `50`, max `5000`, step `50`, default `800`

- **Control - Retry:**: min `0`, max `200`, step `5`, default `15`

- **Control - Request/ngày:**: min `100`, max `100000`, step `100`, default `5000`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Deployment shape — serverless, container hay async worker?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - P95 thời gian:**: min `1`, max `180`, step `1`, default `35`

- **Control - Mức state:**: min `0`, max `100`, step `5`, default `60`

- **Control - Rủi ro tác vụ:**: min `0`, max `100`, step `5`, default `45`

- **Control - Độ biến động tải:**: min `0`, max `100`, step `5`, default `70`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"12e29152-a65d-5370-a77d-65ee418d6363","locator":{"kind":"html_section","section_id":"misc","order":17,"heading":"✕ Hiểu lầm phổ biến","source_file":"day-12.html"},"checksum":"d8a91d576055fef958cd565dfca5767f10bc69294cdf6a86c33acc13f876017a"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai localhost → production gap là phần còn lại tự động an toàn và ổn định.

Sửa lại Externalize state thay vì dùng sticky session.

Vì sao quan trọng · slide 1 · 5 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai agent khác web app truyền thống là phần còn lại tự động an toàn và ổn định.

Sửa lại Timeout của gateway phải dài hơn p95 hoặc chuyển tác vụ sang async.

Vì sao quan trọng · slide 9 · 13 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai container & image hygiene là phần còn lại tự động an toàn và ổn định.

Sửa lại Container tạo environment parity nhưng không tự tạo reliability.

Vì sao quan trọng · slide 18 · 22 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai long-running và streaming là phần còn lại tự động an toàn và ổn định.

Sửa lại Health phải tách liveness khỏi readiness.

Vì sao quan trọng · slide 27 · 31 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai state, session & durability là phần còn lại tự động an toàn và ổn định.

Sửa lại Retry chỉ an toàn khi tool call idempotent.

Vì sao quan trọng · slide 35 · 39 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai cloud deployment options là phần còn lại tự động an toàn và ổn định.

Sửa lại Cost guard là control plane chứ không phải prompt.

Vì sao quan trọng · slide 44 · 48 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"3a14c373-bf5d-5b92-b914-6c1c7bb98853","locator":{"kind":"html_section","section_id":"apply","order":18,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"day-12.html"},"checksum":"501abc05efe0f71e6dad066b924dfedaf7566e561f30ac69c5e1979900b26491"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI cần phục vụ đồng thời nhiều kiosk nhưng vẫn giữ session, streaming và ngân sách token.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Localhost → production gap | Externalize state thay vì dùng sticky session. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 5 |
| Agent khác web app truyền thống | Timeout của gateway phải dài hơn p95 hoặc chuyển tác vụ sang async. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 9 · 13 |
| Container & image hygiene | Container tạo environment parity nhưng không tự tạo reliability. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 18 · 22 |
| Long-running và streaming | Health phải tách liveness khỏi readiness. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 27 · 31 |
| State, session & durability | Retry chỉ an toàn khi tool call idempotent. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 35 · 39 |
| Cloud deployment options | Cost guard là control plane chứ không phải prompt. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 44 · 48 |
| Managed agent runtimes | Scale theo concurrency và token throughput, không chỉ CPU. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 53 · 57 |
| MCP server hosting | Secrets phải ở secret manager, không nằm trong image. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 61 · 65 |

---

<!-- chiron-source-span: {"source_span_id":"540a5739-09dd-5214-8538-79925154a9ac","locator":{"kind":"html_section","section_id":"numbers","order":19,"heading":"# Con số cần kiểm chứng","source_file":"day-12.html"},"checksum":"7b60f20c12018227b1b1ade50e8d7c805db6ed441e2fc1ecc5b4ac33802932b3"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 500MB | hentication,cost guard, và accessible qua publicURL ■ 1Dockerfile (multi-stage, uv, <500MB)+ docker-compose cho agent + dependencies ■ 1deployed instance trên Railway hoặc Render ■ 1health check endpoint (/health)+ streaming endpoint (SSE) | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 5 |
| 11ngày | Recap: Agent Đã HoànChỉnh Nhưng Chỉ Ở Local 11ngày đã build ■ LLMAPI + prompt engineering ■ RAGpipeline grounded ■ Multi-agent+ MCP ■ UX+ trust layer ■ Guardrails+ safety Nhưngđang chạy trên ■ localho | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 7 |
| 1s | AgentKhông Phải WebApp BìnhThường MộtCRUDapptrảlờitrong <1s. Agentthìkhácvềbảnchất—vàđólànguồngốccủamọithách thứcdeploy hôm nay. 1. Long-running Reasoning loop chạy 10–60s+ (có khi vài phút). Phá vỡ timeout 29 | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 60s | vàđólànguồngốccủamọithách thứcdeploy hôm nay. 1. Long-running Reasoning loop chạy 10–60s+ (có khi vài phút). Phá vỡ timeout 29–60s của gate- way/proxy. 2. Stateful Có conversation mem- ory + tool history. Mâu thuẫnvớiquytắc“state- less pr | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 1000× | cess” của 12- factor. 3. Costly Mỗicallgửilạicảhistory → cost tăngsiêu tuyến tính(50–1000×tokenso vớichat). Lưuý: Giữ3tínhchấtnàytrongđầusuốtcảbài. Mỗisectionsaugiảiquyếtmộthệquảcủa chúng. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 2026 M | Sản Phẩm —Sáu Lớp Bọc Quanh Lời GọiModel Lớp Harnessphải cung cấp Trongcoding agent 2026 Mục Vònglặp + tools Loop,toolschema,retry,giớihạnlượt Cùng một loop, ba mặt: CLI / SDK / hosted §1 Côlập FS + network làhai lớp bật-tắt độc lập,ép ở tầ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 14 |
| 60ngày | c củadeploy ■ PinmodelID +tắt auto-upgrade (như deployartifact) ■ Providerbáo trước ≥60ngày rồi requestfail ■ Thựctế: AssistantsAPI gỡ 26/8/2026; gpt-4o/4-turbo/3.5tắt 23/10/2026 Ratelimit = trần thông lượng ■ RPM/ TPM theotiercủanhà cung cấ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 15 |
| 500 RPM | = trần thông lượng ■ RPM/ TPM theotiercủanhà cung cấp ■ VDGPT-4o: rate-limit tier 1= 500 RPM →tier5 = 10k ■ Trầndo vendorđặt,không phải autoscalercủa bạn ■ →retry/backoff+ nhiều key (mục Scaling) Lưu ý:Lịch khai tử modelcủa nhà cung cấp là mộ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 15 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"645d1c41-8b17-5cbb-906d-147a09c60be0","locator":{"kind":"html_section","section_id":"cheat","order":20,"heading":"▣ Cheat sheet ôn thi","source_file":"day-12.html"},"checksum":"80721f5d0cc54e709699a77775b2bb5cbd2256529540c5ac7e8771733846b1d3"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp localhost → production gap | externalize state thay vì dùng sticky session | 1 · 5 |
| Khi gặp agent khác web app truyền thống | timeout của gateway phải dài hơn p95 hoặc chuyển tác vụ sang async | 9 · 13 |
| Khi gặp container & image hygiene | container tạo environment parity nhưng không tự tạo reliability | 18 · 22 |
| Khi gặp long-running và streaming | health phải tách liveness khỏi readiness | 27 · 31 |
| Khi gặp state, session & durability | retry chỉ an toàn khi tool call idempotent | 35 · 39 |
| Khi gặp cloud deployment options | cost guard là control plane chứ không phải prompt | 44 · 48 |
| Khi gặp managed agent runtimes | scale theo concurrency và token throughput, không chỉ CPU | 53 · 57 |
| Khi gặp mcp server hosting | secrets phải ở secret manager, không nằm trong image | 61 · 65 |
| Khi gặp api gateway & security | eval gate bổ sung cho unit test, không thay thế unit test | 70 · 74 |
| Khi gặp scaling và gpu economics | streaming cải thiện perceived latency nhưng không giảm compute | 79 · 83 |

---

<!-- chiron-source-span: {"source_span_id":"81ef606b-9379-5573-9d9f-1acb69fe4422","locator":{"kind":"html_section","section_id":"gloss","order":21,"heading":"☰ Từ điển thuật ngữ","source_file":"day-12.html"},"checksum":"48c77028e73a38766236b8a37d0b3f615deb67207383c476a503139476f5cfbd"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"b2578c5c-9ecd-5f5e-b981-4c413bfe3df0","locator":{"kind":"html_section","section_id":"bloom","order":22,"heading":"◉ Bạn đang ở mức nào?","source_file":"day-12.html"},"checksum":"b1bf5f4b7a3fe52a0f31167cca83b85071b7060058cb4e72e0fe523b7c3162a5"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 5 · 8 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 9 · 13 · 17 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 18 · 22 · 26 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 27 · 31 · 34 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 35 · 39 · 43 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 44 · 48 · 52 |
