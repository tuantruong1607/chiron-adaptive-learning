---
schema_version: 1
course_id: rag-intensive
document_id: "bf384927-ccc1-59e4-bac6-3405e50f5536"
document_version_id: "b60826df-8885-5b94-8ba9-b34ef934c995"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Deployment — Đưa Agent Lên Cloud"
source_file: "DAY 12.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\DAY 12.pdf"
source_sha256: "0b6c4d2197f01d029a3b525be765da1a79b1e0b459b797d6e601edbd77239f4d"
parser_version: chiron-structured-markdown-v1
page_count: 104
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":104}"
language: vi
---

# Deployment — Đưa Agent Lên Cloud

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"869f8a1c-12e5-502e-bf41-e11370342c57","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Deployment — Đưa Agent Lên Cloud","extraction_method":"pdf-text-layer"},"checksum":"7967b5ce8b3806554993b403d348d95c3af86d4a3370aa288b7148c67556db9d"} -->

## Slide 1 - Deployment — Đưa Agent Lên Cloud

AICB-P1 · Ngày 12 · Từ localhost đến production URL TênGiảng Viên VinUniversity · Phase 1 · 2026

---

<!-- chiron-source-span: {"source_span_id":"1e145f28-1a4d-58c0-a775-ebcf4875e14a","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"fecee23c9858206b1dc524b71c0d0269e08167fcdbd898ff44222331a163c2ef"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Bạn demo cho sếp thấy agent chạy trên laptop. Sếp hỏi: khi nào 100 người dùng được? — và liệu nó có ngốn hết ngân sách không?” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"791cc438-4f75-5458-8c77-a0501bc707e0","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"c0d559d14ed0ed7f57364635c8383cb77dd2d3de1ac73edb480077001874b22d"} -->

## Slide 3 - NộiDung Bài Học

1. Từlocalhost đến production

2. Agentvs deploy truyền thống

3. Docker& containerization (2026)

4. Tháchthức riêng của agent

5. Agentchạy ở đâu: server/client/on-device

6. Cloudoptions + managed runtimes (Tier 0)

7. HostingMCP servers

8. APIgateway & security

9. Scaling+ frontier-scale serving

10. CI/CD& eval gates

11. Nângcao: production-grade(tùychọn)

12. Checklist+ phụ lục lệnh/code

13. Lab12 + preview Day 13 Giảngviên (VinUni) AICB· Deployment 2026 1/ 84

---

<!-- chiron-source-span: {"source_span_id":"db6a58cd-d103-56c7-8586-a549725022e5","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"MụcTiêuNgày 12","extraction_method":"pdf-text-layer"},"checksum":"2499fcde56671d6b161d0da0ac2b141d486f7e40315ba398360d7dd55fea6134"} -->

## Slide 4 - MụcTiêuNgày 12

- Hiểugapgiữa dev và production: dependencies, config, secrets,networking

- ViếtDockerfilehiệnđại (multi-stage +uv+slim/distroless) để đóng gói agent

- Nắm3thứ agent phá vỡ webinfra thông thường: long-running, stateful, cost

- Sosánh cloudoptions theotrục quan trọng nhất vớiagent:requesttimeout

- Biếtvề managedagent runtimesmới(Bedrock AgentCore, VertexAgentEngine)

- Thiếtkế APIgateway +cost protection và deploy agentcópublicURL hoạtđộng
Giảngviên (VinUni) AICB· Deployment 2026 2/ 84

---

<!-- chiron-source-span: {"source_span_id":"0249bce5-8fd7-57fb-9cdd-5fe8bffa4ebb","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"b514dec454232df63a82d6622b787f77e53dc94bf4f4f88e4567967834d502a5"} -->

## Slide 5 - DeliverableCuối Ngày

Artifactpack cần nộp Agent đã được containerize và deploy lên cloud, có health check endpoint, basic authentication,cost guard, và accessible qua publicURL

- 1Dockerfile (multi-stage, uv, <500MB)+ docker-compose cho agent +
dependencies

- 1deployed instance trên Railway hoặc Render

- 1health check endpoint (/health)+ streaming endpoint (SSE)

- 1public URL mà bất kỳ aicũng có thể truy cập vàdùng agent
Giảngviên (VinUni) AICB· Deployment 2026 3/ 84

---

<!-- chiron-source-span: {"source_span_id":"33c5f767-2e6c-5a92-bf9d-58a622970c79","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Từ Localhost Đến Production","extraction_method":"pdf-text-layer"},"checksum":"90f5479681cefd36e3d0acb7d2dcbed8d009ffe49e6946d80d76372ab24313bc"} -->

## Slide 6 - Từ Localhost Đến Production

01 Agent chạy trên máy mình khác rất xa với agent chạy cho 100 người — gap đó không chỉ là “copy code lên server”

---

<!-- chiron-source-span: {"source_span_id":"5d58cc66-d009-5086-862f-3e456978760b","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Recap: Agent Đã HoànChỉnh Nhưng Chỉ Ở Local","extraction_method":"pdf-text-layer"},"checksum":"01dabaf85133413f46adf6b24b62b212f4bf68db1df6aabbcecbaf8f2268101f"} -->

## Slide 7 - Recap: Agent Đã HoànChỉnh Nhưng Chỉ Ở Local

11ngày đã build

- LLMAPI + prompt engineering

- RAGpipeline grounded

- Multi-agent+ MCP

- UX+ trust layer

- Guardrails+ safety
Nhưngđang chạy trên

- localhost:8000

- APIkeys trong.env file

- Chỉ1 user (chính mình)

- Khônghealth check

- Tắtlaptop = agent chết
Lưu ý: “It works on my machine” là câu nói nổi tiếng nhất trong lịch sử software engineering. Day 12 giảiquyết đúng vấn đề này. Giảngviên (VinUni) AICB· Deployment 2026 4/ 84

---

<!-- chiron-source-span: {"source_span_id":"179adb5c-9e62-5dce-b722-5aede6c127ef","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"DevEnvironment ̸=ProductionEnvironment","extraction_method":"pdf-text-layer"},"checksum":"d5d930cee761e08989c4af7fcba889857b696cf17ef86d8d7958cf74c25dd808"} -->

## Slide 8 - DevEnvironment ̸=ProductionEnvironment

Khíacạnh Dev(localhost) Production Dependencies “pipinstall” thủ công Đónggói cùng container Config.envfile trên máy Environment variables, secrets manager Networking localhost:8000 HTTPS,domain, load balancer Users 1(chính mình) Nusers đồng thời Failure Restartthủ công Auto-restart,health check Nguyêntắc Environmentparity: dev/staging/prod cànggiống nhau càng ít bugkhideploy. Giảngviên (VinUni) AICB· Deployment 2026 5/ 84

---

<!-- chiron-source-span: {"source_span_id":"74826874-35ec-5789-8643-e25905133515","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"AgentKhông Phải WebApp BìnhThường","extraction_method":"pdf-text-layer"},"checksum":"35b604724c4884a799d29e020f51a271b79adfbc190a069c5a2898195be0f569"} -->

## Slide 9 - AgentKhông Phải WebApp BìnhThường

MộtCRUDapptrảlờitrong <1s. Agentthìkhácvềbảnchất—vàđólànguồngốccủamọithách thứcdeploy hôm nay.

1. Long-running Reasoning loop chạy 10–60s+ (có khi vài phút). Phá vỡ timeout 29–60s của gate- way/proxy.

2. Stateful Có conversation mem- ory + tool history. Mâu thuẫnvớiquytắc“state- less process” của 12- factor.

3. Costly Mỗicallgửilạicảhistory

- cost tăngsiêu tuyến
tính(50–1000×tokenso vớichat). Lưuý: Giữ3tínhchấtnàytrongđầusuốtcảbài. Mỗisectionsaugiảiquyếtmộthệquảcủa chúng. Giảngviên (VinUni) AICB· Deployment 2026 6/ 84

---

<!-- chiron-source-span: {"source_span_id":"ca9ae2e4-6417-5246-aa86-10aa47ac5322","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"12-FactorApp — Áp Dụng ChoAI Agent","extraction_method":"pdf-text-layer"},"checksum":"7bced9aec889994e4c913ca292f9d780ac6d9c406a8d1aa481fda96ab235bec7"} -->

## Slide 10 - 12-FactorApp — Áp Dụng ChoAI Agent

4nguyên tắc quan trọng nhất

1. Configinenv: khônghardcodeAPI keys

2. Statelessprocesses: agentkhông giữstate trên instance

3. Portbinding: exportservice via port

4. Dev/prodparity: giữgap nhỏ nhất Deploymentchecklist

- Secretsmanagement

- Healthcheck endpoint

- Structuredlogging

- Monitoringendpoint

- Gracefulshutdown
Lưu ý:Factor VI (stateless) nói “không dùng sticky session”. Agent có memory→ externalize state (mục Thách Thức Riêng Của Agent ),không bỏ nguyên tắc. Giảngviên (VinUni) AICB· Deployment 2026 7/ 84

---

<!-- chiron-source-span: {"source_span_id":"e18590d7-eb28-50d0-a4bc-3407c63f46b8","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Agent Deploy vs Deploy Phần","extraction_method":"pdf-text-layer"},"checksum":"e12087e2dc78e691694baa1f4e0065c324cb446e3a3d950c84effebbf951ab31"} -->

## Slide 11 - Agent Deploy vs Deploy Phần

02 Mềm Truyền Thống Tin tốt: bạn ship agent bằngđúng cỗ máyđã có (CI/CD, con- tainer, load balancer). Tin cần nhớ: có 3 thứ bịđịnh nghĩa lại — và đó là nơi agent khác biệt

---

<!-- chiron-source-span: {"source_span_id":"0754ca63-c6ed-571f-8d7a-0abd55edd7ba","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"CùngCỗ Máy Ship, Khác CáiHộp Bên Trong","extraction_method":"pdf-text-layer"},"checksum":"7b8e2b8e3384166e80e792e2b8d31a50cbd7d52a8e9cc2fa46e101eb3e806060"} -->

## Slide 12 - CùngCỗ Máy Ship, Khác CáiHộp Bên Trong

Giữnguyên (đừng phát minh lại)

- CI/CDpipeline, build artifact

- Immutableimage, canary/rolling

- IaC(Terraform)

- Loadbalancer,health check

- 12-factor,stateless web tier
Bịđịnh nghĩa lại (cái mới)

- Test: evalgate, không phải
exact-match

- Hoáđơn: tokenruntime, không
CPU-hour

- Dependency: modelngoài, rate-limit,
deprecate

- State: hộithoại, không DB row

- GPUeconomics: khôngCPU/RAM
Câuthần chú Cùngcái hộp;cáibên trongvàcáchquyết định “đạt”mớilà phần khác. Giảngviên (VinUni) AICB· Deployment 2026 8/ 84

---

<!-- chiron-source-span: {"source_span_id":"c9ba5ad1-ee8f-5739-b309-a33a7d1a4cbe","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Before/ After — Monolith CRUDvs Agent","extraction_method":"pdf-text-layer"},"checksum":"79dbc5f18c568f91bc9c9dc52b1834b9a4d8a2e40abcc5436ea54358bd0bffcd"} -->

## Slide 13 - Before/ After — Monolith CRUDvs Agent

AppCRUD truyền thống AIAgent Kiểmthử Unittest, assert chính xác Eval gate(golden set, LLM-judge), gatetheo điểm Chiphí CPU/RAM-hour, đoán trước được Token/request,chỉbiếtsaukhichạy Latency Mili-giây,đồng bộ Giây–phút, streaming (SSE) + async State DBrows Hộithoại / memory (checkpointer) Dependency Bạnkiểm soát & tự version Modelbênngoài: rate-limit,bịdep- recate Scalingunit CPU/RAM GPU+ VRAM Lưu ý: Luận điểm: dùngcùng machinery(CI/CD, canary, immutable image, IaC, LB) — nhưngđịnh nghĩa lạithetest, the bill, the dependency. Giảngviên (VinUni) AICB· Deployment 2026 9/ 84

---

<!-- chiron-source-span: {"source_span_id":"5a4a53c5-01c3-5021-b781-80d099de0c93","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"HarnessMới Là Sản Phẩm —Sáu Lớp Bọc Quanh Lời GọiModel","extraction_method":"pdf-text-layer"},"checksum":"a7bce5270ec16911c41f80b06939cc564130a5ad32bc5c7d10f06730a15f4381"} -->

## Slide 14 - HarnessMới Là Sản Phẩm —Sáu Lớp Bọc Quanh Lời GọiModel

Lớp Harnessphải cung cấp Trongcoding agent 2026 Mục Vònglặp + tools Loop,toolschema,retry,giớihạnlượt Cùng một loop, ba mặt: CLI / SDK / hosted §1 Côlập FS + network làhai lớp bật-tắt độc lập,ép ở tầng OS Seatbelt (macOS), bub- blewrap+seccomp(Linux) §13 Chínhsách quyền allow / ask / deny, cưỡng chếngoài model opencode chỉ có lớp policy, không sandboxOS §13 Cấu hình theo repo Fileđi cùng git, thứ tựưu tiên rõ ràngAGENTS.md (gần nhất thắng) / CLAUDE.md §12 Phiên(state) Session ID, resume, lưungoài pro- cess Transcripttrênđĩa;hostedlưuserver- side §4 Cổng không tươngtác Exit code + JSON + chi phí mỗi lần chạy claude -p ; opencode serve + Ope- nAPI §12 Điểmmấu chốt Lờigọimodelchỉlà mộtdòngtrongsáu. Promptkhôngphải biêngiớibảomật: chỉ dẫntrong prompt/CLAUDE.md “khôngthay đổi những gì Claude Codecho phép”. Giảngviên (VinUni) AICB· Deployment 2026 10/ 84

---

<!-- chiron-source-span: {"source_span_id":"30401aff-75c6-5155-b626-1b2d7cf9ad65","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"ModelLà Dependency Bạn Không KiểmSoát","extraction_method":"pdf-text-layer"},"checksum":"51b77f036c75438761bc93cebe8ce9a28f3fb57a2c3c3e3dcff71ea2e2622cec"} -->

## Slide 15 - ModelLà Dependency Bạn Không KiểmSoát

Khácthưviệnbạnpintrong requirements.txt: modelsốngtrênservercủangườikhác,cóthểbị khaitử vàcó trầnthông lượngdonhà cung cấp đặt. Pin& deprecation là việc củadeploy

- PinmodelID +tắt auto-upgrade (như
deployartifact)

- Providerbáo trước ≥60ngày rồi
requestfail

- Thựctế: AssistantsAPI gỡ
26/8/2026; gpt-4o/4-turbo/3.5tắt 23/10/2026 Ratelimit = trần thông lượng

- RPM/ TPM theotiercủanhà cung
cấp

- VDGPT-4o: rate-limit tier 1= 500
RPM →tier5 = 10k

- Trầndo vendorđặt,không phải
autoscalercủa bạn

- →retry/backoff+ nhiều key (mục
Scaling) Lưu ý:Lịch khai tử modelcủa nhà cung cấp là một forcing function lên release calendar củabạn. Giảngviên (VinUni) AICB· Deployment 2026 11/ 84

---

<!-- chiron-source-span: {"source_span_id":"61f37c59-8602-5e37-8058-aaf2853ed3fd","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Docker — Đóng Gói Agent","extraction_method":"pdf-text-layer"},"checksum":"00f8438d60e5b98ac4c69b95e02b78aa5a3c07f55dc486eeb7bd24dbf07546e5"} -->

## Slide 16 - Docker — Đóng Gói Agent

03 Thành Container Container giải quyết “it works on my machine” bằng cách đóng gói mọi thứ agent cần thành 1 unit chạy được ở bất kỳ đâu

---

<!-- chiron-source-span: {"source_span_id":"76b0bb9a-37da-57fa-aa91-202d1bcb1fe5","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"ContainerLà Gì?","extraction_method":"pdf-text-layer"},"checksum":"120f7aa20876ae68b4ec5690b42c626e5f50ac9d19789af816f5150595b4660f"} -->

## Slide 17 - ContainerLà Gì?

Container Application code Dependencies (Python,libs) Runtime config MinimalOS layer (Debian slim /distroless) Laptop CloudVM Kubernetes Ýchính: Container= app + deps +runtime đóng gói thành 1 unit.Build1 lần, chạy ở mọinơi. Giảngviên (VinUni) AICB· Deployment 2026 12/ 84

---

<!-- chiron-source-span: {"source_span_id":"c2dc78e6-16bd-548d-913c-74749271a69f","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Dockerfile2026 — Multi-Stage +uv","extraction_method":"pdf-text-layer"},"checksum":"bc123e77f212b917fbb6a5b791fdfc213c17a47532ad1c6e91c9ba9b97004318"} -->

## Slide 18 - Dockerfile2026 — Multi-Stage +uv

```text
# Stage 1: build deps with uv (Rust-fast, ~10x pip)
```
FROM python:3.12-slim AS builder COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/ WORKDIR /app ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0 RUN --mount= type=cache,target=/root/.cache/uv \ --mount= type= bind,source=uv.lock,target=uv.lock \ --mount= type= bind,source=pyproject.toml,target=pyproject.toml \

```text
uv sync --locked --no-install-project --no-editable
```
FROM python:3.12-slim # Stage 2: slim runtime WORKDIR /app COPY --from=builder /app/.venv /app/.venv COPY.. ENV PATH= "/app/.venv/bin:$PATH" RUN useradd -m app && chown -R app /app USER app # non-root CMD [ "fastapi", "run", "main.py", "--host", "0.0.0.0"] Lưuý: Target <500MB: uv+cache, --locked,non-root,.dockerignore. Giảngviên (VinUni) AICB· Deployment 2026 13/ 84

---

<!-- chiron-source-span: {"source_span_id":"03f818cb-fdaf-5fc7-8e08-761366325907","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"BaseImage Showdown — Đừng ChọnSai","extraction_method":"pdf-text-layer"},"checksum":"e0cf5f37a61d470fa9916cd077ae353e94bc403a54fe0ca5f39532b921a01014"} -->

## Slide 19 - BaseImage Showdown — Đừng ChọnSai

Baseimage Size(giảinén, trênđĩa) Ghichú cho AI agent python:3.12 ∼1.0GB Full— thừa toolchain, attack surfacelớn python:3.12-slim ∼150MB Defaulttốt choMLPython(glibc,manylinuxwheels) distroless ∼66MB Gọnnhất + an toàn; khôngshell (debug khó) python:3.12-alpine ∼55MB TRÁNHcho ML—xem cảnh báo Lưu ý đơn vị: size “nén khi pull” nhỏ hơn ∼3–4× con số trên đĩa (vd python:3.14-slim-trixie ≈41 MB khi tải). Đừng so hai đơn vị với nhau. Lưuý: Alpinedùng musllibc →packagekhôngcówheel musllinuxphảicompiletừsource (benchmark cũ pandas+matplotlib: slim 30s vs Alpine 26 phút).2026 đã đỡ hơn: numpy 2.5.1 / pandas 3.0.5 / matplotlib 3.11.1 đều đã có wheelmusllinux cho CPython 3.12–3.14 —nhưng matplotlib chưa có aarch64, nên Alpine trên Apple Silicon/Gravitonvẫnbuild từ source. Vẫn nên chọnslim. Giảngviên (VinUni) AICB· Deployment 2026 14/ 84

---

<!-- chiron-source-span: {"source_span_id":"afff1d18-b203-5da2-9c86-040a7b9f37fb","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"ImageSecurity — Scan, Non-Root, SBOM","extraction_method":"pdf-text-layer"},"checksum":"3d6755c89e8ceaa03ef97a7e01f0d6dafe5102ae19692d9514b3d8923ff9ae67"} -->

## Slide 20 - ImageSecurity — Scan, Non-Root, SBOM

3việc bắt buộc

1. ScanCVE: Trivy/ Docker Scout / Grypetrước khi deploy

2. Non-root: USER app,không chạy roottrong container

3. Pindigest: FROM...@sha256:... thayvì tag mềm SBOM— giấy tờ thành phần SBOM (SPDX/CycloneDX): liệt kê mọi packagetrong image.

```text
Sinhbằng syft/ docker buildx --sbom.
Giờ làyêu cầu pháp lý(US EO 14028,
EUCRA).
```
Mốc gần nhất: 11/9/2026— CRA buộc báo ENISAtrong 24h. Nghĩa vụ đầy đủ +SBOM: 11/12/2027. Lưu ý:Distroless ít CVE hơn nhưngkhông phải zero. Scan là việc lặp lại, không phảimột lần. Giảngviên (VinUni) AICB· Deployment 2026 15/ 84

---

<!-- chiron-source-span: {"source_span_id":"0cdc3272-d909-5b69-8733-1bd2fa2b5751","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"DockerCompose — Multi-Service Setup","extraction_method":"pdf-text-layer"},"checksum":"5eb65d1f8836d85e74486b054bce34e28a7b20e9cbeaddb8e84c8998f98f6c43"} -->

## Slide 21 - DockerCompose — Multi-Service Setup

Agentstack điển hình

- Agentservice: FastAPI+ LLM logic

- Vectorstore: Qdrant(6333/6334)

- Cache: Redis(6379) cho
session/ratelimit

- Reverseproxy: Nginx(optional)
Compose2026

```text
■ docker compose up (V2,không
gạchnối)
■ Bỏkey version: (đãobsolete)
```

- depends_on: condition:
service_healthy

- Servicegọi nhau bằng tên (DNS):
qdrant:6333 Cholab Bắt đầu với 2 services:agent + vector store. Thêm Redis và Nginx khi hệ thống cầnscale. Giảngviên (VinUni) AICB· Deployment 2026 16/ 84

---

<!-- chiron-source-span: {"source_span_id":"3102eff9-7572-5a65-8d26-55efab4daf58","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"HìnhHài Một Agent Service TốiThiểu","extraction_method":"pdf-text-layer"},"checksum":"a95eef5aaf70cc966a95385dd90097bb330148c34191b9ccfc2cd29acdf2198a"} -->

## Slide 22 - HìnhHài Một Agent Service TốiThiểu

```text
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
app = FastAPI()
@app.get("/healthz") # health check for LB / Cloud Run
def healthz():
return {"status": "ok"}
@app.post("/chat") # streaming is the default, not the exception
async def chat(req: ChatRequest):
async def gen():
async for chunk in run_agent(req.messages):
yield { "event": "token", "data": chunk}
yield { "event": "done", "data": "[DONE]"}
return EventSourceResponse(gen())
```
Lưuý: /healthz chohạ tầng biết agent sống;/chatstreamtokenqua SSE. Giảngviên (VinUni) AICB· Deployment 2026 17/ 84

---

<!-- chiron-source-span: {"source_span_id":"710326d7-3f03-5ddc-bd59-307345be106e","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Thách Thức Riêng Của Agent","extraction_method":"pdf-text-layer"},"checksum":"e3439bf599ae8a8c4b6db08a9eeaa46f4845df16c5861b326c971339783d50c0"} -->

## Slide 23 - Thách Thức Riêng Của Agent

04 Long-running + stateful = web infra thông thường “gãy”. Đây là phần mà một bài deploy bình thường bỏ qua — nhưng agent thì không thể

---

<!-- chiron-source-span: {"source_span_id":"92664fea-9dc0-51d4-91de-d35792b6ab23","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"VấnĐề Timeout— Agent ChạyLâu Hơn Gateway Cho Phép","extraction_method":"pdf-text-layer"},"checksum":"007ee2b1b50887df7f01aa9528d7ea0bdd11db1970081eb747f1127fd17d67c5"} -->

## Slide 24 - VấnĐề Timeout— Agent ChạyLâu Hơn Gateway Cho Phép

Reasoningloop của agent thường lâuhơn timeout mặc định của hạtầng. Request bị cắtgiữa chừng →userthấy lỗi 504. Hạtầng Timeoutmặc định Ghichú AWSAPI Gateway 29s →504 Cóthể nâng (từ 6/2024) Herokurouter 30s(initial byte) Khôngchỉnh được AWSALB (idle) 60s Cắtstream im lặng nginx proxy_read_timeout 60s Giữa2 lần đọc Fly.ioproxy (idle) 60s Streamingreset timer Railwaypublic HTTP 15phút Privatenetwork: vô hạn Lưuý: 2cáchvượt: (1) streamtừngtoken;(2)routequa privatenetwork hoặcasyncjob. Bảng đầy đủ theo platform: mục Cloud Deployment Options. Giảngviên (VinUni) AICB· Deployment 2026 18/ 84

---

<!-- chiron-source-span: {"source_span_id":"19262b31-b0c9-53b0-b36e-628f1a803887","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"StreamingBằng SSE — Chuẩn De-FactoCho LLM","extraction_method":"pdf-text-layer"},"checksum":"e0be2206fba403a8b45b2735c82f2320e77a582796da99e4310c14457bcc59de"} -->

## Slide 25 - StreamingBằng SSE — Chuẩn De-FactoCho LLM

Tạisao SSE, không phải WebSocket?

- Tokenstreaming mộtchiều
(server→client),chạy trên HTTP/1.1 thường

- EventSource tựreconnect +
Last-Event-ID

- OpenAI& Anthropic đều dùng SSE
(stream:true)

### Lưuý: 2cái bẫy proxy hay gặp

- nginx proxy_buffering on (mặcđịnh) gom
tokenlại →tắtnó, hoặc header X-Accel-Buffering: no

- Agentim lặng >60s →heartbeat: ping
mỗi ∼15sđể không bị cắt idle Streamđứt giữa chừng? BuffertokenvàoRedistheo streamId →reloadthì replaytừchỗđứt. Giớihạn: chỉ cứureload trang. Giảngviên (VinUni) AICB· Deployment 2026 19/ 84

---

<!-- chiron-source-span: {"source_span_id":"acc3fd78-ffb0-572f-9588-8e17c8a8f488","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"KhiQuá Lâu — Chuyển SangAsync Job","extraction_method":"pdf-text-layer"},"checksum":"e313510690afaaaabfb05a79017ce1272602821d4020fa2347342c8aa9020517"} -->

## Slide 26 - KhiQuá Lâu — Chuyển SangAsync Job

Client API (submit) JobQueue (Redis/Celery) Worker (agentloop) POST job_id poll/ webhook

- Submit-and-poll: APItrả job_idngay,client hỏi kết quảsau (hoặc nhận webhook)

- Tool:Celery(broker),RQ(Redis),CloudTasks (managed)

- Batchlớn không gấp?BatchAPI rẻhơn 50%: OpenAI trả trong24h;Anthropic cũng 50%
nhưngphần lớn xongdưới1 giờ Giảngviên (VinUni) AICB· Deployment 2026 20/ 84

---

<!-- chiron-source-span: {"source_span_id":"2ba36247-028e-5cc7-bb33-1d5346b55289","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Statefulness— Mâu Thuẫn Với “Stateless”","extraction_method":"pdf-text-layer"},"checksum":"3280db3602370b3a3bfd70dc4dbe5d1828f53b57c7de0430548583ec18f0b85d"} -->

## Slide 27 - Statefulness— Mâu Thuẫn Với “Stateless”

12-factornói agent phải stateless đểscale. Nhưng agentcómemory. Giải pháp:externalize state,không giữ trên instance. Externalizeở đâu

- Conversation/session →Redis/
Postgres

- LangGraphcheckpointer
(PostgresSaver)keyed bằng thread_id

- Bấtkỳ instance nào cũng phụcvụ
đượcrequest →scaletự do Durableexecution (2025–26) Cho agent chạy nhiều bước/nhiều ngày,

### resumesau crash

- Temporal(replay)· DBOS(MIT,
Postgres)

- Inngest(stepmemoization)

- LangSmithDeployment (têncũ
LangGraph Platform)— managed persistence Lưuý: “Stickysession”chỉlà best-effort—CloudRunphávỡnókhiinstancebịkill. Exter- nalizestate mới chắc. Giảngviên (VinUni) AICB· Deployment 2026 21/ 84

---

<!-- chiron-source-span: {"source_span_id":"b26554b0-f8b6-5b3c-aebb-c125fd3d241f","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Concurrency& Cold Start","extraction_method":"pdf-text-layer"},"checksum":"fb2ab6ecc7beac981df9601d8a4bef1cdbac0ca52492373ca3258dd2bf65c074"} -->

## Slide 28 - Concurrency& Cold Start

Concurrency: dùng async Mỗi request giữ workerrất lâu → dễ cạn workerpool.

- async def: 1 worker phụcvụ nhiều
requestkhi awaitI/O

- Bẫy: blockingcall trong async def
làmnghẽncả event loop

- CloudRun concurrency: mặcđịnh 80,
max1000/instance Coldstart: ML depsnặng Load model/embeddings lúc khởi động→ coldstart chậm.

- Mininstances (CloudRun) /
provisionedconcurrency (Lambda) giữinstance ấm

- Lazy-loadobjecthiếm dùng ra khỏi
coldpath Nguyêntắc agent AgentI/O-bound(đợiLLM) →tăngconcurrencytiếtkiệminstance;giữblockingcode trong defthường. Giảngviên (VinUni) AICB· Deployment 2026 22/ 84

---

<!-- chiron-source-span: {"source_span_id":"4ee264e1-0376-5cc3-8b35-fc8f29c6235b","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Agent Chạy Ở Đâu? Server /","extraction_method":"pdf-text-layer"},"checksum":"1d5c9c8e32e407f85d492850bd18edeaddd4e67ff649c516aaf8117226edaac3"} -->

## Slide 29 - Agent Chạy Ở Đâu? Server /

05 Client / On-Device Một trục kiến trúc deploy mà nhiều người bỏ qua: vòng lặp agent + tools + API key thực sựchạy ở đâu? Câu trả lời quyết định bảo mật, chi phí, và quyền riêng tư

---

<!-- chiron-source-span: {"source_span_id":"4f2ee9c5-ce2b-59be-b557-3c60740c3203","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"PhổVị Trí— LoopChạy Ở Đâu","extraction_method":"pdf-text-layer"},"checksum":"85d0a9efd323ed6abd63ca1dac421b25e8adfba871df28e3247d7f6767384db3"} -->

## Slide 30 - PhổVị Trí— LoopChạy Ở Đâu

Vịtrí Loopchạy ở APIkey Cost/token Nănglực Server-side Backendcủa bạn Antoàn (server) Bạn trả hết Frontier Client(chỉ UI) Trình duyệt, call qua proxy Vẫncần proxy Bạntrả hết Frontier Local-first(BYOK) Máyuser (CLI/IDE) Keycủauser Usertrả Frontier In-browsermodel Trìnhduyệt (WebGPU) Khôngcần Bằng0 ∼1–3B On-device NPU/GPUthiết bị Khôngcần Bằng0 ∼3B Edge Nodebiên (WorkersAI) Ở provider Pay-per-call ∼7B+ Hybrid On-device → escalate cloud Cloudtin cậy Rẻ→đắt Nhỏ→frontier Mặcđịnh Đa số agent production làserver-side: loop + tools + key ở backend, client chỉ là lớp mỏng gửi message. Đổi lại: mọitoken đi vòng qua serverbạn, bạn trả toàn bộ compute. Giảngviên (VinUni) AICB· Deployment 2026 23/ 84

---

<!-- chiron-source-span: {"source_span_id":"32c4786d-d170-5d7f-af59-c39f607b3e77","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"ĐiểmMấu Chốt: “Client-Side”Hiếm Khi Là Keyless","extraction_method":"pdf-text-layer"},"checksum":"d71e4b76e39427f3fceaee45187932dc9e1e404e912cf7a9fc7b41100b4f887b"} -->

## Slide 31 - ĐiểmMấu Chốt: “Client-Side”Hiếm Khi Là Keyless

Browser (UIagent) Backendproxy (BFF) LLMprovider (OpenAI/Claude) request +API key keythêm ở đây, KHÔNGbao giờ xuống browser Lưu ý:Build toolnhúngbiến VITE_/NEXT_PUBLIC_ thẳng vào JS bundle→key ship xuốngtrìnhduyệtvà bịlấycắp. Vìvậyngaycảagent“client-side”vớimodelfrontier vẫn cần backend proxy(Backend-for-Frontend) + rate limit. Chỉon-device / in- browsermodel mớithật sự keyless. Giảngviên (VinUni) AICB· Deployment 2026 24/ 84

---

<!-- chiron-source-span: {"source_span_id":"624f52e5-4e4c-579a-9148-62284576a4db","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"On-Device& Edge — Keyless ThậtSự","extraction_method":"pdf-text-layer"},"checksum":"00a2379d64988d609808c84da04e0c2d240a074ebf65608f9d942487d34e6004"} -->

## Slide 32 - On-Device& Edge — Keyless ThậtSự

On-device(2025–26)

- AppleFoundation Models(∼3B,
on-device,offline,free)

- ChromeGemini Nano/Prompt API
(Chrome138, không gửi data đi)

- MSPhi Silica(NPU,Copilot+ PC)

- WebLLM/ transformers.js
(WebGPUtrong browser) Edge Cloudflare Workers AI: inference trên GPU ở 200+ thành phố, pay-per-call, OpenAI- SDKcompatible. Đánhđổi: privacy+offline+cost0,nhưng năng lực ∼1–3B, tốn pin, và cold load weightslần đầu. Hybrid(mẫu hay nhất) Modelnhỏon-deviceloviệcthường →escalatelênmodellớntrêncloudkhikhó(VD Apple: ∼3B →PrivateCloudCompute). Tiêuchíđịnhtuyếnthường không công bố. Giảngviên (VinUni) AICB· Deployment 2026 25/ 84

---

<!-- chiron-source-span: {"source_span_id":"0892874e-8102-5276-a57e-44612315fc91","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Cloud Deployment Options","extraction_method":"pdf-text-layer"},"checksum":"b1c166aefe357e0e4c45959a3d67af5974a5eb2c9d12c972c1fb59b0fc08087e"} -->

## Slide 33 - Cloud Deployment Options

06 Không có 1 platform đúng cho mọi trường hợp — và với agent, trục quan trọng nhất làrequest timeout, không phải giá

---

<!-- chiron-source-span: {"source_span_id":"f0feb902-0aef-5012-9a31-08053e57a560","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"4TierDeployment (2026)","extraction_method":"pdf-text-layer"},"checksum":"8cd45390b5e540a47cc5c4d0ea263fcd3d43a04b01f59be2de987154bfa4ab50"} -->

## Slide 34 - 4TierDeployment (2026)

Tier0 Managedagent runtime Tier1 Railway/ Render Fly.io Tier2 CloudRun / ECSFargate Tier3 Kubernetes self-managed Khôngquản infra AgentCore/Vertex (Tier0) <10phút deploy MVP/ demo Auto-scale Production Fullcontrol Large-scale Chokhoá học Bắt đầu Tier 1 (Railway/Render). Hiểu flow deploy trước, migrate lên Tier 2/3 khi businesscần, hoặc Tier0 nếumuốn bỏ qua việc quản hạtầng. Giảngviên (VinUni) AICB· Deployment 2026 26/ 84

---

<!-- chiron-source-span: {"source_span_id":"1c32a04a-9673-517c-ac02-60afd8b906f6","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"SoSánh Platform — Theo TrụcTimeout","extraction_method":"pdf-text-layer"},"checksum":"377ff58ac83e3810b1ad1d7556b26ef69571596ca3c3b016c3b7d2114ed54afd"} -->

## Slide 35 - SoSánh Platform — Theo TrụcTimeout

Platform Maxrequest/runtime Scale-to-0 GPU Agentfit Railway 15phút / ∞private Không Không OK(route nội bộ) Render ∼100phút (?) Freetier Không OK Fly.io 60sidle (stream reset) Có Có OK+ streaming CloudRun 60phút Có(cả GPU) L4 Mạnh AWSApp Runner ∼120s Provisioned Không Deprecated ECSFargate Khônggiới hạn Không — Mạnh(always-on) Modal 24h(mặcđịnh 5phút) Có(snapshot) H100/A100 Mạnh (GPU) Vercelfunctions 5 phút Hobby · 800s GA (Pro) Có Không Kém Lưuý: Cậpnhật2026: Railwaybỏfreetier (giờ $5trialcredit);AWSAppRunner deprecated(Mar2026) →ECS Express Mode; Cloud Run GPUGA (6/2025, scale-to-zero,∼5s start). Con số∼100 phút của Renderkhông có trongdocs chính thức(chỉtrong bài so sánh marketing)— đừng thiết kế dựa vàonó. Giảngviên (VinUni) AICB· Deployment 2026 27/ 84

---

<!-- chiron-source-span: {"source_span_id":"e74bece4-2627-5390-997c-7faec5364a66","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"ServerlessFunctions — Tại Sao KhôngHợp Agent","extraction_method":"pdf-text-layer"},"checksum":"f3aff7b3b4c337d3c5859386bb1899413c76d1442a236da50b43c7a6d4eacb71"} -->

## Slide 36 - ServerlessFunctions — Tại Sao KhôngHợp Agent

Vercel/ Lambda functions

- Hardcap 5phút (Hobby/mặc
định);GA 800s, beta 1800s→rồi 504

- Bodycap 4.5 MB

- Stateless— mất context giữa các
invoke Container-basedhợp hơn

- Giữđược connection cho
streamingdài

- Min-instancegiữ ấm, tránh cold
start Lưuý: Câucũ“serverlesscoldstart5–15s”giờ lỗithời: CloudRunGPUstart ∼5s, Modalsnapshotnhanh ∼10×. Vấnđềthậtcủaserverlessvớiagentlà timeoutcap, khôngphải cold start. Giảngviên (VinUni) AICB· Deployment 2026 28/ 84

---

<!-- chiron-source-span: {"source_span_id":"42622fad-d13c-53e7-aef9-cf6cd1026179","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Railway— Deploy Trong5Phút","extraction_method":"pdf-text-layer"},"checksum":"68157568f6b8532e4cdb2cb3c098d37284ebb4183a55d9cd49048893d691df44"} -->

## Slide 37 - Railway— Deploy Trong5Phút

Cácbước

1. Kếtnối GitHub repo

2. Railwaytự detect Dockerfile (builder Railpack2026)

3. Setenvironment variables

4. ClickDeploy

5. Nhậnpublic URL Tạisao chọn cho lab

- Auto-detectDockerfile

- Environmentvariables UI

- Customdomain + SSL miễn phí

- Logsreal-time

- $5trialcredit (đủ cho lab)
Lưuý: Hếtfreetier: Railwaytínhtheousage;newusercó $5trialcredit(khôngcần thẻ)hếthạnsau30ngày. Hếttrial →vềgóiFree: chỉ $1credit/tháng(khôngcộng dồn),vàRailway xoávolume củatàikhoảntrial30ngàysauđó → sao lưu trước khi hết hạn. Bind đúng0.0.0.0:$PORT. Giảngviên (VinUni) AICB· Deployment 2026 29/ 84

---

<!-- chiron-source-span: {"source_span_id":"ed949129-b23c-5582-a437-32e10bb84127","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"KhiRequest/Response Không Còn Là MôHình","extraction_method":"pdf-text-layer"},"checksum":"2f67d80c78bbe504012d616369be50199140c543810203652a6a785020f0517a"} -->

## Slide 38 - KhiRequest/Response Không Còn Là MôHình

Chạydài, không qua HTTP

- CloudRun WorkerPools (GA
4/2026): instance chạy dàipull từ queue— khôngcó trần request timeout. Cột “60 phút”không áp dụng.

- VercelWorkflows: durable execution
—resume đúng điểm cũ, sốngqua deploy/crash.

- OpenAIResponses APIbackground
mode. Trầncũ vẫn còn nguyên

- AWSLambda: trần cứng vẫn900s.
APIGateway 29schặthơn, nằm phía trướcnó.

- Lambdaresponse streaming: native
chỉchoNode.js —Python khôngcó. Ýchính 2026 platform mở lối thoát ở tầng hạ tầng:bỏ hẳn mô hình request/response. Chọn plat- formgiờ là chọnmode. Giảngviên (VinUni) AICB· Deployment 2026 30/ 84

---

<!-- chiron-source-span: {"source_span_id":"6a9c8943-7df6-59de-89ec-05624bfb00ac","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Managed Agent Runtimes (Tier","extraction_method":"pdf-text-layer"},"checksum":"b23be87cf66b919319e35319001d3950b9ee883ab181caaa1e1540946f187fb3"} -->

## Slide 39 - Managed Agent Runtimes (Tier

07 0) Danh mục mới hẳn của 2025–26: deploy agent màkhông phải quản container— runtime, memory, identity đều managed

---

<!-- chiron-source-span: {"source_span_id":"f35af86c-0044-51db-b390-4f6bd85fd160","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Tier0 — Bạn Chỉ MangAgent, Cloud Lo Phần Còn Lại","extraction_method":"pdf-text-layer"},"checksum":"edf39f95b8a62da2481e556569623f40c7e2684016516c852a180769a6ece3a1"} -->

## Slide 40 - Tier0 — Bạn Chỉ MangAgent, Cloud Lo Phần Còn Lại

Bạnkhông viết Dockerfile, không loscaling. Platform cấp sẵnruntime + session + memory + identity,tính theo tiêu thụ. Sảnphẩm GA Điểmnhấn AWS Bedrock Agent- Core Oct2025 8giờ/session,microVMcôlậpmỗisession Agent Runtime (tên mới của Vertex AI AgentEngine) Mar2025 Sessions +Memory Bank+ Code Execu- tion+ Example Store Azure AI Foundry Agent May2025 No-code+hosted; miễnphíservice (trảto- ken) OpenAIAgentKit Oct2025 Agent Builder đóng 30/11/2026→ Agents SDK;ChatKit vẫn còn Đặcđiểm chung Framework-agnostic(LangGraph,CrewAI,ADK...),hỗtrợMCP/A2A(A2Anaylàchuẩn v1.0 doLinuxFoundation quản,150+ tổ chức), session isolation.Cách tính tiền: slide sau. Giảngviên (VinUni) AICB· Deployment 2026 31/ 84

---

<!-- chiron-source-span: {"source_span_id":"2ece7f49-59ee-55cd-a0fd-bd668aaf1697","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Frameworkvs Runtime — Hai TầngBạn Đang Chọn","extraction_method":"pdf-text-layer"},"checksum":"30d2df984e0bf90799363ee2bc0b43b79d267e103a6b824559356b3e96906481"} -->

## Slide 41 - Frameworkvs Runtime — Hai TầngBạn Đang Chọn

“Framework-agnostic”ở slide trước nghĩa làgì? Mọi hãng lớnshiphaitầng riêng biệt—và bạn chọntừng tầng độc lập. Hãng Tầngframework (bạnviết agent) Tầngmanaged runtime(họchạy) Anthropic ClaudeAgent SDK (Python/TS) ClaudeManaged Agents (public beta) OpenAI AgentsSDK AgentKit;ChatKit là surface UI Google ADK(5 ngôn ngữ, OSS) Agent Runtime(tên mới của Vertex AI Agent Engine) AWS StrandsAgents (Apache-2.0) BedrockAgentCore Microsoft Agent Framework (AutoGen + Semantic Kernel) AzureAI Foundry Agent Service LangChain deepagents(MIT) LangSmith Deployment · Managed Deep Agents Vìsao phải tách Frameworkquyếtđịnh codebạnviết ;runtimequyếtđịnh aibịđánhthứclúc3hsáng. Đổi framework = refactor. Đổi runtime = re-deploy. So sánh nhầm tầng là lỗi phổ biến nhất khi đọctài liệu vendor. Giảngviên (VinUni) AICB· Deployment 2026 32/ 84

---

<!-- chiron-source-span: {"source_span_id":"eb7ecd35-3d78-5ae1-9321-763a454380f2","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"SessionLà Đơn Vị Vận HànhCủa Tier0","extraction_method":"pdf-text-layer"},"checksum":"12589bc33a818454ba73a05bcb99b233b685e92a01b263f4b6f99f2b87fbbdf6"} -->

## Slide 42 - SessionLà Đơn Vị Vận HànhCủa Tier0

ỞTier0, requestkhôngcòn là đơn vị —sessionmớilà. Và sessioncó trần riêng. Trầnsession từng platform

- AWSAgentCore: tối đa8giờ,chết
khiidle15 phút;mỗi session một microVMriêng, huỷ = wipe sạch.

- ModalSandbox: mặc định5phút —
phải timeout= mớilên 24h.

- ClaudeManaged Agents: session tự
chủhàng giờ, không công bố trần cứng. Khicần vượt trần

- ModalFilesystemSnapshot →
restorevào Sandbox mới.

- AgentCoremanagedsession
storagegiữstate qua session.

- Nguyêntắc cũ vẫn đúng: state nằm
ngoàiruntimethì trần nào cũng vượt được. Lưu ý:Idle timeout là bẫy chi phí lẫn bẫy đúng-đắn:agent chờ human approval 20 phút

- sessionchết, state mất nếu chưaexternalize.
Giảngviên (VinUni) AICB· Deployment 2026 33/ 84

---

<!-- chiron-source-span: {"source_span_id":"d88a6a35-81d0-5c42-b772-3deb063fe812","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Tier0 Tính TiềnThế Nào— TrụcChi Phí ThứBa","extraction_method":"pdf-text-layer"},"checksum":"2c03ffceb9b28ff24f23ba2588fd5f4e4fdc868e9e8a7d9ca93f8da1900ff7a6"} -->

## Slide 43 - Tier0 Tính TiềnThế Nào— TrụcChi Phí ThứBa

Tier0 thêmđồnghồ thứ haibêncạnh token: thờigian thựccủasession. Platform Đồnghồ tính tiền AWSAgentCore $0,0895/vCPU-giờ + $0,00945/GB-giờ — chỉ tính computeactive; idle& I/O-waitmiễnphí. Gateway $0,005/1.000 invocation Claude Managed Agents Giátoken chuẩn+$0,08/session-giờ,chỉ tính khi status =running Cloudflare ActiveCPUpricing —chỉtínhchukỳCPUthựcchạy;thờigiannằm chờLLM miễnphí Azure AI Foundry Agent Servicekhôngtính phí riêng—chỉ trả cho model +tài nguyên nền Rútra Agent là workloadidle-heavy (phần lớn thời gian là đợi LLM). Chọn Tier 0 chỉ cần hỏimột câu: đồng hồ có chạy khi agent đang chờ không? (Tốiưu chi phí ở quymô→Day25.) Giảngviên (VinUni) AICB· Deployment 2026 34/ 84

---

<!-- chiron-source-span: {"source_span_id":"aca2ee2b-cc4c-52f2-ba6c-d170a2fba4e8","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"RuntimeCũng Là Dependency Bạn KhôngKiểm Soát","extraction_method":"pdf-text-layer"},"checksum":"585c7fcd871510d6a8748ce2ba897f677e397bf46726f95378f1bebe34783e8a"} -->

## Slide 44 - RuntimeCũng Là Dependency Bạn KhôngKiểm Soát

Bằngchứng trong chính bài này

- OpenAIAgent Builderđóng
30/11/2026—vòng đời13tháng. Lối thoát: Agents SDK.

- OpenAIEvals cùnglịch →trỏsang
Promptfoo.

- AWSApp Runner →ECSExpress
Mode.

- LangGraphPlatform →LangSmith
Deployment: đổi tên cũnglà rủi ro — docs/IaCcủa bạn trỏ tên cũ. Bacâu hỏi trước khi chọn

- Pincái gì? SDKversion, API version,
imagebase.

- Thoátbằng đường nào?Export
đượcstate/config không?

- Mấtbao lâu? Ướclượng thật.
Lưuý: Cùngcâuhỏibạnđãhỏivề model,giờhỏivề runtime: pin cái gì, thoát bằng đường nào, mất bao lâu? Giảngviên (VinUni) AICB· Deployment 2026 35/ 84

---

<!-- chiron-source-span: {"source_span_id":"f3849069-9473-5f01-95ae-f18437d8222d","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Tier0 vs Tự Deploy —Khi Nào Chọn Gì","extraction_method":"pdf-text-layer"},"checksum":"acd09c7bcf9b5c36451ef445d42a2e7313e0c47faf0008d5b8b187c7f51c69dc"} -->

## Slide 45 - Tier0 vs Tự Deploy —Khi Nào Chọn Gì

ChọnTier0 khi

- Muốnship nhanh, không có team
infra

- Cầnsession isolation + memory
sẵn

- Agentchạy rất lâu (AgentCore 8h)

- Đãở sẵn hệ sinh thái
AWS/GCP/Azure Tựdeploy (Tier1–3) khi

- Cầnkiểm soát đầy đủ stack

- Tránhvendor lock-in

- Tốiưu cost ở quy môlớn

- Yêucầu compliance/networking
riêng Lưu ý:Cho lab 12, ta vẫntự containerize + deploy(Tier 1) để hiểu cơ chế. Tier 0 làlựa chọn production khi không muốnquản hạ tầng — biết làđủ. Giảngviên (VinUni) AICB· Deployment 2026 36/ 84

---

<!-- chiron-source-span: {"source_span_id":"2892c0e2-7d61-57d7-837e-f48214f558ea","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"DeepAgents — Thang 3 BậcCủa Chính LangChain","extraction_method":"pdf-text-layer"},"checksum":"8c97e6dade56313cec25cc447303ef54a86e963bfbd15d77614c69a1d22809ae"} -->

## Slide 46 - DeepAgents — Thang 3 BậcCủa Chính LangChain

LangChainmô tả sản phẩm củahọ như mộtthang,không phải lựa chọn nhịphân — và nó ánh xạgần 1–1 vào Tier0–3ở đầu mục này. Bậc Bạnsở hữu Đánhđổi OSSdeepagents(MIT) Toànbộ hosting Kiểm soát tối đa;tự cấu hình persis- tence LangSmithDeployment Application+ server code Choteamcầnrouteriêng,authnângcao, scalelớn ManagedDeep Agents Chỉ agent code, tools, middleware, in- structions LangChain lo backend, store, check- pointer,memory,skills, sandbox,identity Lưuý: ManagedDeepAgentsđangPRIVATEBETA:vàobằng waitlist,chỉchạyởregion UScủa LangSmith Cloud,CLI-first, docs ghi rõ “behavior may change before general avail- ability”,và chưacông bố giá. Biết là đủ— đừng thiết kế kiến trúcquanh nó. Giảngviên (VinUni) AICB· Deployment 2026 37/ 84

---

<!-- chiron-source-span: {"source_span_id":"0f0c61eb-9bb4-52cd-bba6-49a6ca0be107","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"DeployDeep Agents — Bốn QuyếtĐịnh Hạ Tầng","extraction_method":"pdf-text-layer"},"checksum":"2ca06f3d86b154a2620d769bf68923c83fbe199ca6b1d7809d2f79d8348739e5"} -->

## Slide 47 - DeployDeep Agents — Bốn QuyếtĐịnh Hạ Tầng

Filesystembackend = quyết định infra

- StateBackend(mặcđịnh): theo
thread,khôngchiasẻ cross-thread

- StoreBackend/
CompositeBackend: chia sẻ cross-thread

- FilesystemBackendvà
LocalShellBackendtruycập thẳng host— docs: đừngdùng trongagent đãdeploy Sandbox& secret

- Thread-scoped: sandbox mới mỗi
hộithoại, dọn khi hết TTL

- Assistant-scoped: dùng chung→
tíchtụ file & package→phảiđặtTTL

- Authproxy chèncredential vào
requestđi ra →secretkhôngvào sandbox Lưu ý:Hai bẫy còn lại:(1) LangSmith Deploymenttự cấu hình persistent checkpointer — self-hostthìbạnphảitựlàm,đâylàdeltalocal →prodlớnnhất. (2) Sharedmemory làvector promptinjection —scope namespace theo user (Day11). Giảngviên (VinUni) AICB· Deployment 2026 38/ 84

---

<!-- chiron-source-span: {"source_span_id":"b5520b5e-a948-5ca1-88a2-264ed66879a0","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"“OpenSource” Không Có Nghĩa LàTự Host Được Miễn Phí","extraction_method":"pdf-text-layer"},"checksum":"a651e05a124ebdcc0ccbb0c4d288f0905c0a29b36801496942301fecac23d2c5"} -->

## Slide 48 - “OpenSource” Không Có Nghĩa LàTự Host Được Miễn Phí

Bạntự host để tránh lock-in. Nhưng licence củaserverthườngkhác licence củalibrary. Thànhphần Giấyphép Ràngbuộc khi self-host LangGraph(library lõi) MIT Tựdo langgraph-api (server) Elastic-2.0 Cầnlicensekey+egresstới beacon.langchain.com (cóchế độ air-gapped) n8n Sustainable Use Li- cense Chỉnội bộ / phi thươngmại Dify Apache2.0 sửađổi Cấmchạy multi-tenant SaaS; cấm gỡlogo ClaudeCode Proprietary Anthropic Commercial ToS —không phải open source CodexCLI · opencode · goose Apache-2.0 · MIT · Apache-2.0 Khôngràng buộc Crush FSL-1.1-MIT Đọc được mã nhưngcấm dùng cạnh tranh; MIT sau2 năm Lưu ý:Ba câu hỏi khi thấy chữ “open source”:licence củaserver có giống licence của library? Cóthưmục ee/? Cóphảigọivềnhà đểxácthựclicence? —VàOSS cóthểđóng lại: Daytona đóng mãlớp sandbox ngày11/6/2026. Giảngviên (VinUni) AICB· Deployment 2026 39/ 84

---

<!-- chiron-source-span: {"source_span_id":"0be6a5b8-9c9a-5da4-9e8f-9eea2ab685ba","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Hosting MCP Servers","extraction_method":"pdf-text-layer"},"checksum":"748df7fc3a1696f353d3fbcb5f8dda098909c3bddcb0de07af63649d63acc63c"} -->

## Slide 49 - Hosting MCP Servers

08 Day 9 dạy agent gọi MCP tools. Khi MCP server cần chạyre- mote cho nhiều client, nó cũng là một service phải deploy — và phải bảo mật đúng

---

<!-- chiron-source-span: {"source_span_id":"0e5241ab-0b9c-5142-a5bb-c2df627316eb","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"stdiovs Streamable HTTP — HaiTransportCủa MCP","extraction_method":"pdf-text-layer"},"checksum":"b04af74c813a646142bbb911a9e165f4cf94d4d99b71bc820e9ea9a57f83dcd0"} -->

## Slide 50 - stdiovs Streamable HTTP — HaiTransportCủa MCP

stdio(local) Client spawn server làm subprocess, nóichuyện qua stdin/stdout.

- Chạycùng máy với agent

- Khôngcần OAuth — lấy credential
từenv

- Hợpdev / desktop
StreamableHTTP (remote) Mộtendpoint(vd /mcp),POST+GET,SSE bên trong.

- Processđộc lập, phục vụ nhiều
client

- Thaythế transportHTTP+SSE cũ
(2024-11-05)

- Phảihost + bảo mật nhưAPI thật
Lưu ý: Remote MCP server (spec2026-07-28) phải dùngOAuth 2.1. stdio thì KHÔNGcần. Ba cái bẫy spec gọi tên: slide sau. Giảngviên (VinUni) AICB· Deployment 2026 40/ 84

---

<!-- chiron-source-span: {"source_span_id":"602c38e3-b3b5-5a52-ad34-5b7f77194ad2","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"MCP2026-07-28 — Protocol TrởThành Stateless","extraction_method":"pdf-text-layer"},"checksum":"b07ef3be5beed76e28c058363041ddfd1d05a29b5855039c15196e3ef40c0ac1"} -->

## Slide 51 - MCP2026-07-28 — Protocol TrởThành Stateless

Thayđổi lớn nhất

- Babản: 2025-06-18 →2025-11-25 →
2026-07-28.

- “MakeMCP stateless”: bỏ handshake
initialize +header Mcp-Session-Id.

- TransportHTTP+SSEcũdeprecated
(12tháng chuyển tiếp).

- Header Mcp-Method/Mcp-Name: router
khỏiparse JSON body. Hệquả deploy Mọi request rơi vàobất kỳ instance

### nào sau LB round-robin thường
không sticky session, không session store,scale-to-zero thoải mái. Đúng bài học mục Statefulness: ex- ternalize state → tự do scale. Lưuý chuyển tiếp Server đã deploy vẫn phảitương thích ngượcvới client bản 2025 trong suốt giai đoạn chuyểntiếp — đừng xoá codecũ ngay. Giảngviên (VinUni) AICB· Deployment 2026 41/ 84

---

<!-- chiron-source-span: {"source_span_id":"eaacc828-fb95-5f81-8c24-4d7602342f99","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"OAuth2.1 Cho MCP — BaCái Bẫy Spec Gọi Tên","extraction_method":"pdf-text-layer"},"checksum":"824b2b783c24501eeabacc856f8b8c36be824b7e3b1343ec4ab7306295b3aea4"} -->

## Slide 52 - OAuth2.1 Cho MCP — BaCái Bẫy Spec Gọi Tên

Bẫy1 — Tokenpassthrough ServerMUSTNOT nhậntokenkhôngđược cấpriêng cho nó. Speccấmrõ ràng. Vìsaonguyhiểm: nó vôhiệuhoáratelim- itingvà audit trailởservice phía sau. Bẫy2 — Confused deputy Proxyphảigiữregistry client_idđãduyệt theotừng user,kiểm tra trước mỗi flow. Xácthực đúng user ̸=uỷquyền cho client. Bẫy3 — Discovery đã đổi

### Từ 2025-11-25 theo RFC 9728
WWW-Authenticate nay tuỳ chọn, fall- backvề.well-known. Siếtthêm ở bản 2026-07-28

- Validate isstheoRFC 9207

- Khai application_type lúcđăng ký

- DCRđangbị khai tử→CIMD
Lưu ý:stdio không cần OAuth. Nhưng khoảnh khắc bạn đưa server ra remote, nó làmột APIcông khai với đầy đủnghĩa vụ. Giảngviên (VinUni) AICB· Deployment 2026 42/ 84

---

<!-- chiron-source-span: {"source_span_id":"8545466a-634b-5ef6-94dd-403d0e43580e","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"ServerMCP Là API Thật —Ba CVE Đã Chứng Minh","extraction_method":"pdf-text-layer"},"checksum":"8760e69e675dd7ef3e4df3ce09e5a8fffe4ebd33559b3162fe765147123899fb"} -->

## Slide 53 - ServerMCP Là API Thật —Ba CVE Đã Chứng Minh

CVE Bàihọc deploy CVE-2026-33032 nginx-ui,CVSS 9,8 đang bị khai thác /mcp có AuthRequired(), /mcp_message thì không → 12 tool khôngcần credential, chiếm server trong2request.

- Xác thực MỌI route.Lỗi deploy kinh điển, không phải lỗi
protocol. CVE-2025-6514 mcp-remote,9,6 Command injection trong chínhOAuth proxy: chỉ cần kết nối tớiserver độc hại là RCEtrên máy client.

- Lớpproxy cũnglàattack surface.
CVE-2025-68143/4/5 GitMCP server (Anthropic) Pathtraversal + argument injection;git_init bịgỡ hẳn.

- Ngaycảserverthamchiếucủa người tạo protocol cũngcólỗ
hổng. Lưu ý:Rất nhiều MCP server chỉ làlớp bọc mỏng quanh một CLI. Deploy remote = phơi CLIđó ra Internet→container,non-root, egress allowlist. Giảngviên (VinUni) AICB· Deployment 2026 43/ 84

---

<!-- chiron-source-span: {"source_span_id":"d41c1674-d168-5862-90f9-5aeb758cde80","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"DeployMCP Ở Đâu — Registry,Gateway,Runtime","extraction_method":"pdf-text-layer"},"checksum":"34348b3ec10b7bdb9c8ba35b52ef862a84d109220a0b8832da9e86a9526de25c"} -->

## Slide 54 - DeployMCP Ở Đâu — Registry,Gateway,Runtime

Lớp Vaitrò Côngcụ 2026 Registry Để tìm Official MCP Registry: server.json + namespace reverse-DNS.Chỉlàmetadata—KHÔNGphảihost- ing;giải quyết discovery,không giải quyếttrust Gateway Để gom& kiểm soát Docker MCP Gateway(mỗi server một container cô lập,secrettậptrung); AWSAgentCoreGateway (gom Lambda/REST/MCPvề một endpoint có governance) Runtime Để chạy Cloudflare Workers + OAuth 2.1 qua workers-oauth-provider; hoặc chính container bạnđã học ở mục Docker Mẫu2026 Registryđểtìm →Gatewayđểgom+kiểmsoát →Runtimeđểchạy. Đừngđểmỗiagent tựcắm thẳng vào 20 serverrời rạc. Giảngviên (VinUni) AICB· Deployment 2026 44/ 84

---

<!-- chiron-source-span: {"source_span_id":"cdd1b114-29d5-5554-b01d-414a9b397f0e","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"API Gateway & Security","extraction_method":"pdf-text-layer"},"checksum":"afdbf645ce3f4f7603e514119a545a82d9e4f3228b74c8e4170a31ded15662b5"} -->

## Slide 55 - API Gateway & Security

09 Agent trên cloud cần lớp bảo vệ trước khi request đến logic — authentication, rate limiting, vàcost protection(nơi nhiều startup đã “cháy túi”)

---

<!-- chiron-source-span: {"source_span_id":"a83b6fe8-5932-5567-8b80-c16550311d1b","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"APIGateway Architecture","extraction_method":"pdf-text-layer"},"checksum":"fb93b5891d688de17b1bba472c66b020b68778092bc628ff211894f377606570"} -->

## Slide 56 - APIGateway Architecture

Client Request Auth Check Rate Limiter Input+ Budget Agent 401/ 429 Reject Nguyêntắc Mỗirequestphảiqua auth →ratelimit →validate+budgetcheck trướckhiagent xửlý. Reject sớm= tiết kiệm tokens và tiền. Giảngviên (VinUni) AICB· Deployment 2026 45/ 84

---

<!-- chiron-source-span: {"source_span_id":"1b928688-a1e1-514c-bf7b-0f9ce97830d3","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"AuthenticationPatterns","extraction_method":"pdf-text-layer"},"checksum":"7b2547141848c855d6c4c2b3c089256c457edbe01671746f88e033200c1b6bb3"} -->

## Slide 57 - AuthenticationPatterns

APIKey Đơngiản nhất. Header: X-API-Key Dùng khi:internal, MVP, B2B(M2M) JWTToken Statelessauth. Bearertoken + expiry Dùng khi: user-facing app,microservices OAuth2.1 Delegatedauth + PKCE. Chuẩn cho MCP/agent remote Dùng khi: platform, re- moteMCP Lưu ý:Cho MVP:API keylà đủ. Đừng over-engineer auth trước khi có user thật. Nhưngnếu hostremoteMCP server,OAuth 2.1 là bắt buộc theospec. Giảngviên (VinUni) AICB· Deployment 2026 46/ 84

---

<!-- chiron-source-span: {"source_span_id":"5f6aee61-d21c-5771-893f-54573adeafbb","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"CostProtection — Đừng Để AgentĐốt Hết Tiền","extraction_method":"pdf-text-layer"},"checksum":"9a9df8bf07a27fdcfb5bfd56cca8bcb6acdef030142569c91a5d4db2141e17d7"} -->

## Slide 58 - CostProtection — Đừng Để AgentĐốt Hết Tiền

Rủiro (có thật)

- $47.000trong 11ngày: 4agent retry vô
hạn,có log nhưng không cóhard limit

- $96.000Vercel: appCara tăng
100k→900kuser trong vài ngày

- Promptinjection →tokenexplosion

- APIkey bị lộ→hackerxài
Bảovệ

- Pre-calladmission control: check
budgetcòn lại trước khi gọiLLM, từ chối nếuvượt

- Per-tenantbudget: keytheo (tenant,
workload,model)

- Ratelimiting: tokenbucket (rate + burst)

- Circuitbreaker: tắtkhi anomaly
Lưuý: Bẫylớn: “spend alert”chỉ thôngbáo,KHÔNGchặn. Hardcaplàtínhnăng riêng, phảibật thủ công. Alert của provider làphản ứng sau → vẫn phải tự build admissioncontrol chặn trước. Giảngviên (VinUni) AICB· Deployment 2026 47/ 84

---

<!-- chiron-source-span: {"source_span_id":"66a76adc-1dff-5a51-bd77-0e65fd1a86fd","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"HTTPS,Secrets & OWASP","extraction_method":"pdf-text-layer"},"checksum":"c431512501cb0913e4969aff72fef56402dbf58c11279fce3f334d3f6e3da26e"} -->

## Slide 59 - HTTPS,Secrets & OWASP

Securitybasics

- HTTPS:Railway/Rendercấp SSL tự động

- CORS:chỉlà kiểm soáttrình duyệt —
KHÔNGphải authz, API vẫn cầnauth

- Secrets: dùngsecret manager (Doppler,
Infisical...) thay.env—có rotation + audit

- GitHub: pushprotectionmặcđịnh;keylộbị
auto-revoke OWASPLLM Top10(2026)

- LLM01Prompt Injection

- LLM02Sensitive Info Disclosure

- LLM06Excessive Agency

- LLM10Unbounded Consumption
(cost/DoS)

- Agentcó tool: AgenticApps 2026—
ASI03(Identity)+ ASI04(Supply Chain). Đầy đủ: Day 11 Lưu ý:Kiểm tra ngay:.env có trong.gitignore? Key có lỡ commit lên GitHub? Nếucó →revokevà tạo key mới ngay lậptức. Giảngviên (VinUni) AICB· Deployment 2026 48/ 84

---

<!-- chiron-source-span: {"source_span_id":"2c89be2a-25bc-5a3b-9865-f2a5a8bf15e3","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"DữLiệu Chạy Ở Đâu —Residency,ZDR & Compliance","extraction_method":"pdf-text-layer"},"checksum":"1ed491b26896344c54e91dec13ff9785c85b1187705194bf158475da429926c8"} -->

## Slide 60 - DữLiệu Chạy Ở Đâu —Residency,ZDR & Compliance

Gatewaylo auth, rate limit, cost. Còn một trục nữanhiều team chỉ phát hiện lúcký hợp đồng:dữ liệunằm ở đâu và tồntại bao lâu. OpenAI

- 11region lưutrữ at-rest, nhưng chỉ
US/ EU / UAExửlý inference trong vùng

- Bậttheo project bằngprefixdomain
(eu.api.openai.com);phụphí 10%

- ZDRloạinội dung khỏi log,ép
store=false,phải duyệt trước Anthropic

- ClaudeManaged Agents KHÔNG
đủđiềukiệnZDRlẫnHIPAABAA — vìnó cố ý lưuhistory,sandbox state, outputở server

- ClaudePlatform on AWS̸=
Bedrock: hạ tầng doAnthropicvận hành;ZDR xin được Lưu ý:Việt Nam không nằm trong danh sách region→ mặc định dữ liệurời lãnh thổ. Nếu hồ sơ pháp lý buộc dữ liệu ở lại, lựa chọn còn lại làself-host — chính là quyết định ở mụcsau. Giảngviên (VinUni) AICB· Deployment 2026 49/ 84

---

<!-- chiron-source-span: {"source_span_id":"722a1326-40f0-574d-953b-59f3809e62a9","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"HardCap Thật Sự Nằm ỞĐâu?","extraction_method":"pdf-text-layer"},"checksum":"b7f97e10ddb69f59c1554e4d4d8d843ca491ecdcc1cff07f5060601b5184e7a3"} -->

## Slide 61 - HardCap Thật Sự Nằm ỞĐâu?

Nhàcung cấp Hard cap native? Cơ chế Bẫy OpenAI Có, phải bật thủ công HardSpendLimitở cảorglẫnproject, trả429 “Spend alert” và trường monthly- budgetcũ chỉbáo, không chặn Anthropic Có,thật sự cứng Trần theo tier ($500 / $1.000 / $200.000); chạm trần → API tạm dừngtới tháng sau Có spend limittheo Workspace, rút từhạn mức chung của org AWSBedrock KHÔNG Tự ráp: Budgets + CloudWatch → Lambdathu hồi IAM Circuitbreaker phảnứngsau,không phảiadmission control LiteLLM Cótheothiết kế Virtual key max_budget → 429 BudgetExceededError Đãcóissue bypasshoàntoàn ởmột bảnrelease Kếtluận Enforcement của providerkhông đồng nhấtvà không phải lúc nào cũng hoạt động

- admissioncontrolphíabạnlàlớpduynhấtbạnkiểmsoát. “Cứng theo thiết kế” ̸=
“cứng ở version bạn đang deploy” — hãy tự test. Giảngviên (VinUni) AICB· Deployment 2026 50/ 84

---

<!-- chiron-source-span: {"source_span_id":"71725e4e-eb55-5fb0-8dab-f5fa673d63f8","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Scaling & Reliability","extraction_method":"pdf-text-layer"},"checksum":"7bcf4c6cd7bd78e1a279e87e77d236615fe0c96b53f908169840111230f907e5"} -->

## Slide 62 - Scaling & Reliability

10 Agent MVP không cần Kubernetes — nhưng cần hiểu cơ bản về scaling và reliability để hệ thống không chết khi có nhiều user hơn

---

<!-- chiron-source-span: {"source_span_id":"c4602483-b174-5c5c-836e-887eccc9d463","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"HorizontalScaling — Scale Theo Concurrency,Không Phải CPU","extraction_method":"pdf-text-layer"},"checksum":"3130ecb9f3cdc02ab7ac5947de9bfa2dea87483a29f9f8e27d022b75d1324cbe"} -->

## Slide 63 - HorizontalScaling — Scale Theo Concurrency,Không Phải CPU

Users Load Balancer Instance1 Instance2 Instance3 Shared State(DB) Lưu ý: Agent làI/O-bound: một instance có thể đầy request đang chờ LLM mà CPUvẫnthấp. →Autoscaletheo concurrency/queuedepth (Knative,KEDAtheo tínhiệuvLLM num_requests_running,RayServe target_ongoing_requests),không theoCPU. Điều kiện tiên quyết: agentstateless,state ở DB/Redis. Giảngviên (VinUni) AICB· Deployment 2026 51/ 84

---

<!-- chiron-source-span: {"source_span_id":"6660a2f8-4825-5f55-8d5c-a89e323c90e2","locator":{"kind":"page","page":64,"label":"Slide 64","section_title":"HealthChecks — 3 Loại Probe","extraction_method":"pdf-text-layer"},"checksum":"65affd3e0db6af21957d13dfec93feef16e1298189b1c05c2d3e465352f8e1eb"} -->

## Slide 64 - HealthChecks — 3 Loại Probe

3loại probe

- Liveness—“còn sống?” Fail→
restartcontainer( GET /health )

- Readiness—“sẵn sàng nhận
request?” Fail→gỡkhỏi LB, KHÔNGrestart

- Startup—cho boot chậm (load
weights);gate 2 probe kia đếnkhi pass Healthendpoint mẫu

### GET /health trảvề

- status: “ok” / “degraded”

- uptime: seconds

- version: app version

- dependencies: DB, vector store,
LLMreachable? Lưuý: Livenessrestart,readinesschỉngắttraffic—cấuhìnhnhầmreadinessthành liveness= restart loop vô ích. Giảngviên (VinUni) AICB· Deployment 2026 52/ 84

---

<!-- chiron-source-span: {"source_span_id":"4d8e2999-2155-57ea-97bc-fee25295af4b","locator":{"kind":"page","page":65,"label":"Slide 65","section_title":"Zero-DowntimeDeploy & Graceful Shutdown","extraction_method":"pdf-text-layer"},"checksum":"ef48b4a3c5b14f5ee099224bc10d56a2032e2226588274f52b8f70516b3be120"} -->

## Slide 65 - Zero-DowntimeDeploy & Graceful Shutdown

Step1 Startnew instancev2 Step2 Healthcheck passes Step3 Routetraffic tov2 Step4 Drain+ stop v1(SIGTERM) Lưu ý: Graceful shutdown cho agent:khi nhận SIGTERM, phảidrain request đangchạydở(mộtagentturncóthểdài). Đặt terminationGracePeriodSeconds lớn hơnworst-case agent turn,nếu không request bị cắt giữachừng. Nângcao Rainbow deployment(Anthropic): dịch traffic dần sang version mới nhưnggiữ cả hai cùng chạy, để không cắt ngang agent đang chạy dở — vì agent là hệ thống stateful chạy gần như liên tục. Argo Rollouts: shift traffic + AnalysisRun tự rollback. Railway/Renderhỗ trợ rolling sẵn. Giảngviên (VinUni) AICB· Deployment 2026 53/ 84

---

<!-- chiron-source-span: {"source_span_id":"e6d6f013-e0ed-561f-8842-13a988d243d7","locator":{"kind":"page","page":66,"label":"Slide 66","section_title":"LLMGateway / Router — MộtCửa, Nhiều Provider","extraction_method":"pdf-text-layer"},"checksum":"d0091466a5ec3e3118a117749fb07174c22bf38fa068020b2284e61bfd7dc2c2"} -->

## Slide 66 - LLMGateway / Router — MộtCửa, Nhiều Provider

Agent LLMGateway (LiteLLM) OpenAI Anthropic Local/ OSS

- 1endpoint, format OpenAIchohàng trăm model —LiteLLM(tựhost, không markup) vs
OpenRouter(managed,phí nạp credit 5,5%)

- Fallback& failover: modellỗi / rate-limit→tựnhảy nhóm dự phòng; load-balancenhiều
key,retry/backoff,cost tracking mộtchỗ Vìsao cần Router vượt trầnrate-limit của vendor bằng nhiều key/nhiều provider, và sống sót khimột provider hỏng. Giảngviên (VinUni) AICB· Deployment 2026 54/ 84

---

<!-- chiron-source-span: {"source_span_id":"b12a2130-1d5a-5b3a-920d-e6161abab312","locator":{"kind":"page","page":67,"label":"Slide 67","section_title":"CacheĐể Cắt Cost & Latency","extraction_method":"pdf-text-layer"},"checksum":"d8341be60087653c67f210cad3844227a3e6c615f3ae114486298c96a143e559"} -->

## Slide 67 - CacheĐể Cắt Cost & Latency

Promptcaching (provider) Tái dùng KV-cache củaprefix chung (sys- temprompt, RAG context).

- Anthropic: cache read∼0.1×(∼90%
rẻhơn), cần khai báo breakpoint;ghi cache1.25 ×–2×

- OpenAI:tựđộng vớiprefix ≥1024
token,cache read ∼0.1×(∼90%rẻ hơn);từ GPT-5.6có thêmphíghi cache1.25× Semanticcache (của bạn) Trả lại câu trả lời cũ cho câu hỏitương tự vềnghĩa (soembedding).

- GPTCache: lưu embedding query
trongRedis

- Tránhgọi LLM lặp→cắtcả cost lẫn
latency

- Cẩnthận: trả lờicũ có thể lỗi thời
Lưu ý:Prompt cacheso khớp prefix từng byte;semantic cacheso khớp ý nghĩa —mạnh hơn nhưng có thể trảcâu cũ đã lỗi thời. Giảngviên (VinUni) AICB· Deployment 2026 55/ 84

---

<!-- chiron-source-span: {"source_span_id":"47811730-5516-5942-b4d5-672f63bbe4ae","locator":{"kind":"page","page":68,"label":"Slide 68","section_title":"Deploy Model — Gọi API Hay Tự","extraction_method":"pdf-text-layer"},"checksum":"bb332e43018b13ed90b1a96f9771c6029ef2e3a459f49d948e207107fc5a87fc"} -->

## Slide 68 - Deploy Model — Gọi API Hay Tự

11 Phục Vụ? Trước hết: có tự host model không? Nếu có, phần sau giải thích

### vì sao cost & latency lại như vậy— một sợi chỉ đỏ duy nhất
giữ GPU bận, đừng phí KV cache

---

<!-- chiron-source-span: {"source_span_id":"d8d16cf2-0aa3-5eca-85e4-ff60a5a87d95","locator":{"kind":"page","page":69,"label":"Slide 69","section_title":"Model: Gọi API HayTự Phục Vụ? —Quyết Định Deploy Thứ Hai","extraction_method":"pdf-text-layer"},"checksum":"fd3c2498f5fd11c5437e5e814a22eeb3b617ae819496882e50e18c0cd9085ac5"} -->

## Slide 69 - Model: Gọi API HayTự Phục Vụ? —Quyết Định Deploy Thứ Hai

Bốnlực đẩy sang tự host

- Residency/ compliance: dữ liệu
khôngđược rời lãnh thổ hoặcVPC

- Sởhữu adapterfine-tune(Bedrock
CustomModel Importlàmmờ ranh giới)

- Kinhtế theo volume: chỉ thắng khi
GPUđủ bận (hoà vốn: Day 25);trần nănglực khôngcòn là rào — slide sau Balực giữ ở hosted API

- Khôngcó GPU-hour rảnh: hosted
trảtheotoken;tựhosttrảtheo giờ,kể cảkhi rảnh

- Bậcmua năng lực: Fastmode (2×),
ScaleTier (SLA99,9%)

- Ngượclại: AzurePTUtínhtheogiờ
dùkhôngcótoken —đúngcáiTier0 tránhđược Balớp, không phải hai Hosted API → managed self-hosting(bạn mang weight, họ lo serving stack)→ tự dựng. Câu hỏi không phải “model nào giỏi hơn” (Day 14) mà “tôi có muốn vận hành thêm một serviceGPU không”. Giảngviên (VinUni) AICB· Deployment 2026 56/ 84

---

<!-- chiron-source-span: {"source_span_id":"fe40290e-7cbd-5899-ae47-ac3da747f166","locator":{"kind":"page","page":70,"label":"Slide 70","section_title":"NếuTự Host: ChọnModel Mở Nào, Engine Nào","extraction_method":"pdf-text-layer"},"checksum":"874ade3ab905b2cec033f079de9d747f52d25d0daa5584bcd8712761dce528bb"} -->

## Slide 70 - NếuTự Host: ChọnModel Mở Nào, Engine Nào

Modelmở đáng deploy (8/2026)

- gpt-oss-120b —117Btổng / 5,1Bactive
(MoE),Apache-2.0, vừamộtGPU 80GBnhờ MXFP4

- gpt-oss-20b —chạy trong16GB:tầng phần
cứngphổ thông

- Qwen3-235B-A22B—235B/22B, Apache-2.0

- DeepSeek-V3.2-Exp—685B, MIT

- KimiK2 —1T/32B, Modified MIT,thiết kế cho
agentictool-use MoE: VRAM quyết bởi active params, không phải tổng. Enginechọn theo hình dạng tải

- vLLM—mặc định đa phần cứng
(NVIDIA/ROCm/Intel/TPU),server OpenAI-compatible

- SGLang—khi prefix được dùng lạinhiều
(RadixAttention) →rấtđúng với agent

- TensorRT-LLM—đỉnh trên NVIDIA, đổi lại
phảicompile engine riêng

- llama.cpp+ GGUF—CPU/edge/consumer,
quantize1,5–8 bit Quantization không thay nhau:GGUF (CPU/edge) ̸=AWQ/GPTQ(GPU) ̸=FP8(H100/Blackwell). Lưu ý: Ship fine-tune bằngmulti-LoRA trên một base, không phải một GPU cho mỗi adapter. Cơ chế bên trong engine, benchmark, sharding đa GPU: Day 20. Giảngviên (VinUni) AICB· Deployment 2026 57/ 84

---

<!-- chiron-source-span: {"source_span_id":"fcee1077-1c11-5fc7-a9b2-27f0a3d75e72","locator":{"kind":"page","page":71,"label":"Slide 71","section_title":"TựHost = Bạn Có ThêmMột Service Phải Deploy","extraction_method":"pdf-text-layer"},"checksum":"ec031fe2568f97b6352f30668b3e7aa3e6c6691e0d7cf2b462d09f3b4855b74d"} -->

## Slide 71 - TựHost = Bạn Có ThêmMột Service Phải Deploy

Vậnhành đổi luật

- Coldstart không còn tính bằng
giây: nạp weight hàngchục GB→ phút

- Readinessprobe phảiđợi weight
nạpxong, không chỉ đợi portmở

- Autoscaletheo queuedepth,không
theoCPU

- GPUrảnh vẫn tính tiền—ngược
hẳnđồng hồ idle-free của Tier0 Artifactdeploy có thêm trục thứtư NhớbaartifactrollbackởmụcCI/CD— im-

### age · prompt · model ID? Tự host thêm
weight(repo+revision) ·địnhdạng/quan- tization ·phiên bản engine. Hỏi trước khi deploy: “rollback” ở đây nghĩa là rollback cái nào? Lưuý: Tựhostkhôngphảilà“bỏvendor”—là đổivendorlock-inlấycôngviệcvậnhành. Mọi mục hôm nay (health check, scaling, rollback, cost guard) đều phải làm lại cho service GPUnày. Giảngviên (VinUni) AICB· Deployment 2026 58/ 84

---

<!-- chiron-source-span: {"source_span_id":"20a6d8c6-e1d7-56cb-9518-8ecfacfb06d4","locator":{"kind":"page","page":72,"label":"Slide 72","section_title":"SợiChỉ Đỏ: GiữGPU Bận + Continuous Batching","extraction_method":"pdf-text-layer"},"checksum":"7a313cb4f986e19cc8ac629575775cce6798eef3ecedddbbbb042a765b62fe6e"} -->

## Slide 72 - SợiChỉ Đỏ: GiữGPU Bận + Continuous Batching

Staticbatching Cả batch chờ requestdài nhất xong → GPU ngồi không khi các request ngắn đã xong. Continuous(in-flight) batching Lên lịch lại batchmỗi bước decode: re- questxongthìthayngayrequestmớivào. Tácđộng Orca(OSDI’22)giớithiệuiteration-levelscheduling,báocáotới 36.9×throughputso với baseline ở cùng latency. Đây là “unlock” lớn nhất của GPU utilization khi serve LLM. Lưuý: Mọikỹthuậtsauphụcvụmộtý: khôngphíKVcache,GPUkhôngbaogiờ rảnh—vì GPU-hourquyếtđịnh cost serve agent. Giảngviên (VinUni) AICB· Deployment 2026 59/ 84

---

<!-- chiron-source-span: {"source_span_id":"f196e4ec-7733-5bc0-bd35-5e25543c6e13","locator":{"kind":"page","page":73,"label":"Slide 73","section_title":"PagedAttention— Quản KV Cache NhưOS Quản RAM","extraction_method":"pdf-text-layer"},"checksum":"c89e6e84491d9bfd89a9418bace45b06d14a7bd4b3d0be25640b3ab63cd1ead6"} -->

## Slide 73 - PagedAttention— Quản KV Cache NhưOS Quản RAM

Mỗitoken sinh ra cần lưuKey/Value(KV cache). Cấp phát liền mạch→phânmảnh, phí bộ nhớ. PagedAttention(vLLM,SOSP’23) chia KV cache thànhblockcố định, không liền mạch—y nhưvirtual memory paging của hệđiều hành.

- Gầnzerolãngphí KV →batchlớn hơn trong cùng VRAM

- Chiasẻ KV giữa request (parallelsampling, beam) qua copy-on-write

- vLLMbáo cáo2–4×throughputso với hệ trước ởcùng latency
Vìsao bạn quan tâm KV cache là lý do context dàitốn bộ nhớvà vì sao prompt caching (slide trước) tiết kiệm được— nó tái dùng đúngnhững block KV này. Giảngviên (VinUni) AICB· Deployment 2026 60/ 84

---

<!-- chiron-source-span: {"source_span_id":"4862c773-fbb6-567d-bca9-e445496b781c","locator":{"kind":"page","page":74,"label":"Slide 74","section_title":"PrefixCaching + Speculative Decoding","extraction_method":"pdf-text-layer"},"checksum":"94c85e88243c91d78f2bde327c718f2570d786cbd807d925e2a5eff9e8c5cdd8"} -->

## Slide 74 - PrefixCaching + Speculative Decoding

Prefix/ prompt caching Prefill của prefix chung tínhmột lần, dùng lạicho nhiều request.

- Prefillcủa prefix tínhmộtlần rồitái
dùng →đặtphần tĩnh(system, few-shot,RAG) lênđầuprompt. (Giá cache: mục Cache ở slide trước.) Speculativedecoding Model nháp nhỏ đề xuất 5–8 token, model đíchxácminh song song.

- Tậndụng GPU đang rảnh,khôngđổi
phânphối output

- ∼2–3×giảmlatency; EAGLE-3 báo
cáotới ∼4.8×(Llama-3.3-70B) Liênhệ thực tế Haikỹthuậtnàylàlýdocùngmộtcâuhỏigửilần2(cachehit) rẻvànhanhhơn hẳn —thiết kế prompt để tận dụng. Giảngviên (VinUni) AICB· Deployment 2026 61/ 84

---

<!-- chiron-source-span: {"source_span_id":"98b1eecb-f534-5e1d-acbd-5f0dc441a2e6","locator":{"kind":"page","page":75,"label":"Slide 75","section_title":"DisaggregatedPrefill / Decode","extraction_method":"pdf-text-layer"},"checksum":"ebbd93c4404e15f5326de399722df1dd88d062da87955b81d75c5487b9096821"} -->

## Slide 75 - DisaggregatedPrefill / Decode

Prefillpool compute-bound (xửlý prompt) Decodepool memory-bound (sinhtoken) KVcache Prefill(đọc cả prompt, song song→ compute-bound)và decode (sinh từng token→memory-bandwidth-bound)có hồ sơ tài nguyênkhác nhau →táchra 2 pool GPUscaleđộc lập.

- DistServe(OSDI’24): tới 7.4×nhiềurequest hơn trong cùng SLO

- Mooncake(Kimi, FAST’25): KV-cache-centric,>100Btoken/ngày

- NVIDIADynamo (GTC 3/2025): prefill/decode là first-class, KV-awarerouter
Giảngviên (VinUni) AICB· Deployment 2026 62/ 84

---

<!-- chiron-source-span: {"source_span_id":"c5c04be1-0c2a-5a68-8888-51f42c7bf337","locator":{"kind":"page","page":76,"label":"Slide 76","section_title":"CI/CD & Eval Gates","extraction_method":"pdf-text-layer"},"checksum":"79cb29a2a4f6faeebc64d15f61a79433d88c67b80052474ebc38eee06ab45080"} -->

## Slide 76 - CI/CD & Eval Gates

12 Deploy bằng tay sẽ quên bước, sẽ sai. Tự động hoá build→push→deploy — và thêm lớpeval gateriêng của AI: chặn deploy nếu chất lượng tụt

---

<!-- chiron-source-span: {"source_span_id":"a94d4d18-0693-5451-ab04-dfd158d8ad1a","locator":{"kind":"page","page":77,"label":"Slide 77","section_title":"Pipeline: Build→Push →Deploy →EvalGate","extraction_method":"pdf-text-layer"},"checksum":"2d41c67c729e300d0f869054d6478cc935946230d894b29e7d314424d4054bdd"} -->

## Slide 77 - Pipeline: Build→Push →Deploy →EvalGate

#.github/workflows/deploy.yml

### steps
- uses: actions/checkout@v4
# build + push image to GHCR (needs packages: write) - uses: docker/build-push-action@v6 # scan image for CVEs, fail the build on high severity - uses: aquasecurity/trivy-action@master - run: promptfoo eval --fail-on-error # <- EVAL GATE - run: railway up # deploy iff evals pass Evalgate — lớp đặc trưngcủa AI Agent non-deterministic → không thể chỉ dựa unit testexit 0. Gate deploy theo điểmeval ≥ngưỡng(promptfoo/DeepEval/Braintrust). ĐâylàcầunốitớiDay14 (Evaluation). Giảngviên (VinUni) AICB· Deployment 2026 63/ 84

---

<!-- chiron-source-span: {"source_span_id":"c0d22d23-fa0f-5b77-83ef-89b1c9ecf9ce","locator":{"kind":"page","page":78,"label":"Slide 78","section_title":"EvalGate TrongThực Tế— Bốn Công Cụ, Một Khuôn","extraction_method":"pdf-text-layer"},"checksum":"46a6620ae7f96a0afe2e59e6f6bf0055a6d5f661dfac143fd74293def8a4ec75"} -->

## Slide 78 - EvalGate TrongThực Tế— Bốn Công Cụ, Một Khuôn

Côngcụ Cơchế gate Kếtquả trên PR promptfoo promptfoo eval --fail-on-error ; chặt hơn: fail khi stats.failures > 0 promptfoo-action comment pass/fail + linkviewer DeepEval assert_test()(khôngphải evaluate())—raisekhi score <threshold pytest-native,fail như test thường Langfuse experiment-action chạytrên dataset có version Commentkết quả lên PR Braintrust eval-action chặnmerge khi dưới ngưỡng Diffview sovới run của nhánh baseline Lưu ý:Đừng pintemperature=0: Anthropic deprecatetemperature/top_p/top_k từ Opus 4.7trởđi—setkhácmặcđịnhtrả 400. Mọiharnessđangpin temperature=0 sẽgãythẳng. Mẫuđã hội tụ Cả bốn công cụ đi tới cùng một chỗ: so vớirun của nhánh baseline, không chỉ so với một ngưỡng tuyệt đối — ngưỡng tuyệt đối không phát hiện được “tụt 4 điểm nhưng vẫn trên ngưỡng”. Phương pháp đánh giá → Day 14; quan sát production → Day 13. Giảngviên (VinUni) AICB· Deployment 2026 64/ 84

---

<!-- chiron-source-span: {"source_span_id":"6d179860-0103-5f99-8f39-ea56cd77e15a","locator":{"kind":"page","page":79,"label":"Slide 79","section_title":"Shadow →Canary →100%— Ramp Cho Agent","extraction_method":"pdf-text-layer"},"checksum":"e28af26cf50e4277de40f67c66d47d31f4ddd21768358b65a9e3e121196b53b0"} -->

## Slide 79 - Shadow →Canary →100%— Ramp Cho Agent

Shadow mirrortraffic, output BỎ ĐI Canary5% outputTHẬT tới user Ramp 10 →25 →100%

- Shadow(mirror): nhânđôitrafficsangversionmới, khôngbaogiờ trảoutputchouser. Rủi
rouser = 0.

- Canary: địnhtuyến một% traffic thậtvà có trảoutput — bán kính thiệthại giới hạn.

- Auto-rollbacklàprimitive có thật: Argo RolloutsAnalysisRun queryPrometheus theo lịch,
tựrollback khi metric fail. Lưu ý: Thuế riêng của agent:shadow chạy cả hai version cho mọi request → nhân đôi hoá đơn token. Với agent: shadowmột mẫu 5–10%, không phải 100%. Vàshadowchỉantoànkhitoolcallcủaversionmới bịchặnsideeffect —nếukhông, “khôngtrả output” vẫntrừtiền thật. Giảngviên (VinUni) AICB· Deployment 2026 65/ 84

---

<!-- chiron-source-span: {"source_span_id":"1e82fe15-e8aa-5a3f-9e06-d03fd7b26d3d","locator":{"kind":"page","page":80,"label":"Slide 80","section_title":"RollbackKhông Nhất Thiết Là MộtLần Deploy","extraction_method":"pdf-text-layer"},"checksum":"702cb98fedb608960194d6bc6448a0262e7249f88ced62a52334593550c8863c"} -->

## Slide 80 - RollbackKhông Nhất Thiết Là MộtLần Deploy

Baartifact, ba vòng đời Một“bảndeploy”củaagentthựcragồm ba

### thứrollback độc lập

- Container image

- Promptversion

- ModelID
Ba đường rollback khác nhau — đừng gộp làmmột. Mẫuđã hội tụ ở 6vendor Prompt version là artifact bất biến, content-addressed; một label di động (prod) được trỏ lại để promote hoặc roll- back.

- Rollbackprompt/modelxấu= dichuyển
một label, tính bằnggiây: không deploy, khôngchạy CI. Giới hạn: label chỉ cứu prompt/config — codevà image vẫn đi quapipeline. Lưuý: Nếupromptcủabạnnằmtrong.pyvàđicùngimage,bạn khôngcó rollbacknhanh —bạn có một lần deploy.Táchprompt ra khỏi code làmột quyết định deploy. Giảngviên (VinUni) AICB· Deployment 2026 66/ 84

---

<!-- chiron-source-span: {"source_span_id":"d66e469b-f5a5-532c-8e6d-4f8604b613f0","locator":{"kind":"page","page":81,"label":"Slide 81","section_title":"AgentLà Một Job TrongCI — Hợp Đồng Tối Thiểu","extraction_method":"pdf-text-layer"},"checksum":"f3aa0c805f2a2ccd7fd0854739c835bf2cc0ca823ea76924a37d80b6ddd0a2a5"} -->

## Slide 81 - AgentLà Một Job TrongCI — Hợp Đồng Tối Thiểu

Hợpđồng gọi (callable contract)

- Exit 0/khác 0đểscript rẽ nhánh;
--output-format json trả total_cost_usd mỗilần chạy

- Chếđộ bare: bỏ auto-discovery
hook/skill/MCP →CIchạy giống nhaumọi máy

- Đừngparse transcript nội bộ —
formatkhôngổn định Aiđược kích hoạt, với quyềngì

- Gatedanhtính người kích hoạt
trướcgate tool: writeaccess + phải là người

- Bẫy: trigger schedule khôngcó tác
giả → bỏ qua checkwrite-access

- Automationmode: zerotool mặc
định;OIDCfederation thaysecret APIkey tĩnh trong repo Lưu ý: Job agent cóhai trục chi phí độc lập— compute-minute và token — phải chặn cứngcảhai( --max-turns,workflowtimeout,concurrencylimit). Vàtách pha: cấpsecretcho setupscript rồigỡtrước khivònglặp agent đọc nội dungkhông tin cậy. Giảngviên (VinUni) AICB· Deployment 2026 67/ 84

---

<!-- chiron-source-span: {"source_span_id":"e4127847-c4e7-5b81-9f90-fbe89033b665","locator":{"kind":"page","page":82,"label":"Slide 82","section_title":"Nâng Cao — Deploy Cấp Pro","extraction_method":"pdf-text-layer"},"checksum":"cfb5fefca284f4e71f03bd10d943712f0e9382fce07d99f1fc494f73bc909c12"} -->

## Slide 82 - Nâng Cao — Deploy Cấp Pro

13 Nâng Cao — Deploy Cấp Pro- duction (tùy chọn) Đưa 1 agent lên URL an toàn mới là 20% dễ. 80% khó là khi agent bền bỉ, lặp lại, và hành động không hoàn tác được— phần này phác qua những vấn đề đó

---

<!-- chiron-source-span: {"source_span_id":"4115b1bf-2576-5b1d-b5e2-8379d8035029","locator":{"kind":"page","page":83,"label":"Slide 83","section_title":"AgentCó Nhiều “Hình Dạng” —Mỗi Cái Deploy Khác Nhau","extraction_method":"pdf-text-layer"},"checksum":"f4ffbf9a6fdc8a98ee3879d3752036ac63135be0769e539ef1c516b35c0d4e4b"} -->

## Slide 83 - AgentCó Nhiều “Hình Dạng” —Mỗi Cái Deploy Khác Nhau

Hìnhdạng Trigger Vòngđời Scale State Chatbotđồng bộ userrequest giây(timeout) per-request sessionstore Cron/ nền scheduler phút thấp,định kỳ jobstate Batch dataset/queue dài,async fan-out per-item idempo- tent Autonomous“chạy mãi” loop liên tục vôhạn 1actor/goal phải sống qua restart Copilotnhúng in-appevent giây theoapp app/session Ambient/ sự kiện webhook/event bursts,ngủ lâu scale-to-zero bềnqua giấc ngủ Lưu ý:State-durability là trục phân biệt chính.“Autonomous chạy mãi” phá vỡ mô hình request/response→ buộc dùng durable runtime. Multi-agent: tốn∼15× token; nguyên tắc vàng “read thì song song được, write thì không”— scale 1 agent trước,chỉ tách khi chạm trần thật. Giảngviên (VinUni) AICB· Deployment 2026 68/ 84

---

<!-- chiron-source-span: {"source_span_id":"338383ec-ba0a-5879-a76a-a4d8f6f8bf99","locator":{"kind":"page","page":84,"label":"Slide 84","section_title":"“JustRetry” Rất Nguy Hiểm VớiAgent","extraction_method":"pdf-text-layer"},"checksum":"157a6ba30a5724c3350b2df9b3de98b77aeaa48a4bff3486241ebe2e73b2764d"} -->

## Slide 84 - “JustRetry” Rất Nguy Hiểm VớiAgent

Webapp thường: lỗithì retry. Nhưng agent cósideeffect thật(gửimail, trừ tiền, đặt vé). Retry mù= làmhai lần. AgentA AgentB (chargecard)

1. charge

2. reply chậm

3. timeout→retry →CHARGELẦN 2 Lưuý: Timeoutkhôngphânbiệt được“thấtbại”với“thànhcôngnhưngreplychậm” →caller bắn lại side effect. Sự thật phũ phàng:không có “exactly-once”cho hành động ngoài hệ thống— chỉ cóat-least-once+ consumer idempotent. Giảngviên (VinUni) AICB· Deployment 2026 69/ 84

---

<!-- chiron-source-span: {"source_span_id":"72a1c30d-3bba-502a-a1e2-b4d6c5ce13ec","locator":{"kind":"page","page":85,"label":"Slide 85","section_title":"IdempotencyKey — Và Cái BẫyRiêng Của Agent","extraction_method":"pdf-text-layer"},"checksum":"0c9d9a6654f5e067065c373bd9b96f6f3a06d1ffd01cc604fa8addb62d116b5e"} -->

## Slide 85 - IdempotencyKey — Và Cái BẫyRiêng Của Agent

Mẫuchuẩn (Stripe) Client gửi headerIdempotency-Key (UUID) kèmrequest mutating.

- Serverlưu kết quả lầnđầutheokey

- Retrycùng key →trảlại y nguyên (kể
cảlỗi đã cache)

- Stripelà chuẩn de-facto,khôngphải
RFC(IETFdraft đã hết hạn) Bẫyvới LLM agent LLM không sinh lại tham số y hệtcho cùngmộtýđịnh →hashnộidungthô trượt.

- Cầndeduptheo ngữ nghĩa / ýđịnh

- “Cùngintent”,khôngphải“cùngbytes”

- Ailà trọng tài quyết 2hành động là
“một”? Thựchành Mọitoolcallcósideeffectnênmangmộtidempotencykeyổnđịnh(vd order_id),và backenddedup bằng RedisSET NX +TTL. Giảngviên (VinUni) AICB· Deployment 2026 70/ 84

---

<!-- chiron-source-span: {"source_span_id":"6d327e5f-4376-51c0-96b4-e025f931548c","locator":{"kind":"page","page":86,"label":"Slide 86","section_title":"DurableExecution — Ghi Lại QuyếtĐịnh, Đừng Chạy Lại Model","extraction_method":"pdf-text-layer"},"checksum":"fedd7e3015e77fd9938ce5c45d1d1991854be51f1c6f0fc89ca4b166a4bc072f"} -->

## Slide 86 - DurableExecution — Ghi Lại QuyếtĐịnh, Đừng Chạy Lại Model

Agentcrash ở bước 7 (sau4 tool call). Chạylại từ đầu =trảtiền LLM lần nữa+lặp tool đã ghi

### đĩa. Durable execution giảiquyết bằng một mẹo tinh tế
Journal+ replay Temporal / Restate / Inngest: ghioutput của LLMvàojournalởlầnđầu;khireplaythì đọc lạibản ghi,KHÔNGgọi lại model.

- “Phầnthông minh” không bao giờchạy
lại

- Bướcđã xong được memoize, bỏqua
Lưu ý:LangGraph là ngoại lệ:check- point ở mứcnode, không phải từng call

- node chưa xong sẽchạy lại cả LLM
call. “Checkpoints̸=durableexecution”. Lưu ý:“Exactly-once” của các framework thực ra là “exactly-oncetrên datastore của họ ”. Hànhđộngrahệthốngngoàivẫncầnidempotent. Câuhỏihay: agentđược resumecócòn “suynghĩ” không, hay chỉ đangđọclại quákhứ? Giảngviên (VinUni) AICB· Deployment 2026 71/ 84

---

<!-- chiron-source-span: {"source_span_id":"b8542100-8cd3-500c-9d4d-bbe67efa0494","locator":{"kind":"page","page":87,"label":"Slide 87","section_title":"Saga& Hành Động Không ThểHoàn Tác","extraction_method":"pdf-text-layer"},"checksum":"d723e0e49b17ef33b8bbd807b6747f4eee4b78e7b84af7447b7a718646402733"} -->

## Slide 87 - Saga& Hành Động Không ThểHoàn Tác

Giữchỗ Trừtiền Gửivé (pivot) Ghilog compensate(undo)

- Saga: mỗibước có một bướcbùtrừ (undo)— không có rollback tựđộng, phải tự code

- Bướckhônghoàn tác được(gửimail/vé) =pivot: đặtcuối+gate bằnghumanapproval

- Vấnđề: agent tựchọn thứ tự hành động —runtime có nêncấmnóxếp việc bất khả hoàn
trướcpivot? Lưu ý:HITL nghịch lý: Temporal cho agentchờ 3 tuần tốn 0 compute— nhưng giữ chỗ / báo giá / tokenvẫn hỏng dầnngoài đời. Resume một quyết định đã cũ = durabilitythành gánh nặng. Giảngviên (VinUni) AICB· Deployment 2026 72/ 84

---

<!-- chiron-source-span: {"source_span_id":"72e6aa4d-63bd-5746-97a1-67db3da208c9","locator":{"kind":"page","page":88,"label":"Slide 88","section_title":"Security: Egress Là ĐiểmKiểm Soát","extraction_method":"pdf-text-layer"},"checksum":"192b7be4e063634f546ba1a518376e5e57a2f6f0d19a0a0bc215231e32256d6f"} -->

## Slide 88 - Security: Egress Là ĐiểmKiểm Soát

Đâylàmặt hạtầng củaantoàn(khácDay11—mặthànhvi). Toolcủaagentgọirangoài=kênh ròrỉ. Lethaltrifecta (Willison)

### Ròrỉ data cần 3 thứcùnglúc

- datariêng tư

- +nội dung không tin cậy

- +kênh gửi ra ngoài
Bỏmột cái = chặn được. 4sự cố 2025, cùng 1cơ chế EchoLeak · CamoLeak · GitLab Duo · AgentFlayer — đềurender ảnh/HTML tới URLkẻtấncông vàđềufixbằng chặnren- der/ giới hạn egress. Lưu ý:Egress allowlist là phòng thủ mạnh nhất — nhưngkênh rò rỉ thường là kênh tin cậy: CamoLeak tuồn data qua chính proxy Camo của GitHub. Không thể allowlist khỏi nhà cungcấp bạn đang tin. Giảngviên (VinUni) AICB· Deployment 2026 73/ 84

---

<!-- chiron-source-span: {"source_span_id":"2c306df7-59e6-5e36-9e0f-1d0bf0c60097","locator":{"kind":"page","page":89,"label":"Slide 89","section_title":"Sandbox& Bài Học “Fail-Open”","extraction_method":"pdf-text-layer"},"checksum":"df64eeaa610505eef0ba5eec39c05987c6bf7c9945f760eee0bfbfe597c9fb22"} -->

## Slide 89 - Sandbox& Bài Học “Fail-Open”

OSnamespace Docker+seccomp, bubblewrap Syscallintercept gVisor,Modal microVM Firecracker· E2B V8isolate Cloudflare Workers côlập mạnh hơn→(startupchậm hơn, gần như ngượclại) Lưuý: CVE-2025-66479(ClaudeCode): cấuhình allowedDomains: [] (ýđịnh chặt nhất)lại fail-open(mởtoangegress)vìcodecheck length > 0. Ýđịnhantoànnhất không biểu diễn được. → Ngữ nghĩa mặc định CHÍNH LÀ thuộc tính bảo mật (fail-closed,không phải fail-open). Nhãn đúng 2026: Cloudflare Sandboxes (GA 13/4/2026) chạy trênContainers, khôngphải V8 isolate — V8 isolatechỉ đúng choWorkers. Giảngviên (VinUni) AICB· Deployment 2026 74/ 84

---

<!-- chiron-source-span: {"source_span_id":"eddde06d-b704-5ef5-abe5-e236b1f61d58","locator":{"kind":"page","page":90,"label":"Slide 90","section_title":"Least-Privilege— Mỗi Agent Một DanhTính","extraction_method":"pdf-text-layer"},"checksum":"95220e1c514a1cb59bc23dc30feae35070e86d6a642131e50571cd98e5401525"} -->

## Slide 90 - Least-Privilege— Mỗi Agent Một DanhTính

Rủiro

- OWASPLLM06Excessive Agency:
quánhiều quyền →hànhđộng phá hoại

- Confuseddeputy: agent bị lừadùng
quyềncủa nó cho kẻ khác

- 1“god-key” chung = 1 điểmsụp đổ
Phòngthủ

- Mỗiagent mộtidentityriêng,scope
hẹp

- Tokenngắnhạn,theo từng task

- Audience-boundtoken (MCP OAuth
2.1)

- VD:Microsoft Entra Agent ID
Lưu ý: Khoảng cách thực tế:∼91% tổ chức chạy agent ở production, nhưng chỉ ∼10% quản chúngnhư một danh tính. Per-agent identity ở quy mô lớn là bài toán vậnhành chưa được giải tốt. Giảngviên (VinUni) AICB· Deployment 2026 75/ 84

---

<!-- chiron-source-span: {"source_span_id":"f02ea4de-6c0c-54ef-9b40-fef556f929d4","locator":{"kind":"page","page":91,"label":"Slide 91","section_title":"DanhTính Cho Agent — SPIFFEVà Agent Identity","extraction_method":"pdf-text-layer"},"checksum":"30ce646ffdb29945d35e7ee1243875d013483b2d2a053363c88cbac7e4ab65fa"} -->

## Slide 91 - DanhTính Cho Agent — SPIFFEVà Agent Identity

Cơchế đang thành chuẩn Service account không đủ: agent phù du, bán kính lớn, key chung không truy vết được.

- SPIFFE(CNCF):X.509SVID ngắn
hạn,có attestation.

- GoogleAgent Identity(4/2026):
principalhạngnhất,tách khỏi human lẫnservice account; cert xoay vòng, hạn24h. Mộtagent phải xác thực về4 hướng

- Tớidịchvụ cloud: bound token gắn
cert

- Tớitool/MCPngoài: API key /OAuth

- Tớitài nguyêncủauser: 3-legged
OAuth;tới agentkhác: mTLS+ DPoP Lưuý: OAuth2.1thuần khôngdiễnđạtđược “agent nàohànhđộngthayusernày”. Draft làdraft —nhớ Idempotency-Key: thiếtkế đểthayđược cơchế uỷ quyền. Giảngviên (VinUni) AICB· Deployment 2026 76/ 84

---

<!-- chiron-source-span: {"source_span_id":"08770cd1-a37f-57c3-ab6c-e279fb4508d8","locator":{"kind":"page","page":92,"label":"Slide 92","section_title":"Deployment Checklist","extraction_method":"pdf-text-layer"},"checksum":"f662c0508985cb8705472fdb8b8580dc1166fd170a21bc28159145bad40003cb"} -->

## Slide 92 - Deployment Checklist

14 Một trang để soi trước khi bấm deploy — gói lại mọi thứ đã học hôm nay

---

<!-- chiron-source-span: {"source_span_id":"17ce6ec0-de32-5d96-ae1b-61f6db6087bc","locator":{"kind":"page","page":93,"label":"Slide 93","section_title":"ProductionReadiness Checklist","extraction_method":"pdf-text-layer"},"checksum":"246b535d1aa2c75cc25f1e9bb6761d1934f681bedf97e31982ee384ab767ccdd"} -->

## Slide 93 - ProductionReadiness Checklist

Container,Deploy & Agent

- Multi-stage+ uv, <500MB,non-root

- .dockerignore +scan CVE (Trivy)

- PublicURL + HTTPS hoạt động

- Envvars (không hardcode secret)

- Streaming(SSE) cho response dài

- Stateexternalized (Redis/Postgres)
Security,Cost & Reliability

- Auth(API key / JWT)

- Ratelimit +spendingcap
(admissioncontrol)

- Per-project/per-tenantbudget

- /health(liveness+ readiness)

- Gracefulshutdown (drain)

- Rollbackplan <2phút

- Pinmodel ID+tắt auto-upgrade

- Router/fallbackkhi provider lỗi
Giảngviên (VinUni) AICB· Deployment 2026 77/ 84

---

<!-- chiron-source-span: {"source_span_id":"3b6e2ecb-9ced-5a8f-b9ad-67dbcf1ef133","locator":{"kind":"page","page":94,"label":"Slide 94","section_title":"HoạtĐộng: Agent CủaBạn Deploy Ở Đâu? — 20 Phút","extraction_method":"pdf-text-layer"},"checksum":"f58a829e327e5e7eb6e4b678348d094bbaeb2d057292266f75f0c10a0fd17204"} -->

## Slide 94 - HoạtĐộng: Agent CủaBạn Deploy Ở Đâu? — 20 Phút

Bước1 — Chọn một usecase

- Chatbotbánhàng—demosau1tuần

- Agentnghiên cứu — 45 phút/tácvụ

- Trợlý ngân hàng — datakhông rời
VN

- Hoáđơn — 10 user,2 lần/ngày

- Apphọc — 100k user,dồn buổi tối

- Hoặc: agent của chínhnhóm bạn
Bước2 — Trìnhbày(tự do)

### Chỉbắtbuộc 2 điều

1. Deployởđâu?

2. VÌSAO —ràng buộc nào quyết định? Vẽsơđồ,slide,haynóimiệng— không cómẫu. Lưuý: “Chúngtôi chọn vì.” Viếtđược câunày là xong. Giảngviên (VinUni) AICB· Deployment 2026 78/ 84

---

<!-- chiron-source-span: {"source_span_id":"322a8258-96b0-5753-b1ff-a813c421456b","locator":{"kind":"page","page":95,"label":"Slide 95","section_title":"Phụ Lục Thực Hành — Lệnh &","extraction_method":"pdf-text-layer"},"checksum":"f6da30cd8fd62cfd7671e612849c3b8bb7edb2128d6325c74205475d85bb2e08"} -->

## Slide 95 - Phụ Lục Thực Hành — Lệnh &

15 Code Gói lại thành thứ gõ được ngay: lệnh deploy thật, và một cost- guard tối thiểu — để rời lớp học là deploy được

---

<!-- chiron-source-span: {"source_span_id":"e44887af-bcbe-5cad-9c7b-57d88783677b","locator":{"kind":"page","page":96,"label":"Slide 96","section_title":"DeployThật — Cloud Run &Railway","extraction_method":"pdf-text-layer"},"checksum":"e5a9f6f20da5f28cb7fb7d4a9e7eaef01e718b3fb52e91fb20d042bef27bdb0d"} -->

## Slide 96 - DeployThật — Cloud Run &Railway

```text
# A) Google Cloud Run: build from source, then deploy
```
gcloud run deploy agent-svc -- source. \ --port 8080 --concurrency 8 --memory 1Gi \ --region asia-southeast1 --allow-unauthenticated \ --set-env-vars MODEL_ID=claude-...,MAX_USD_PER_REQ=0.05 \ --set-secrets ANTHROPIC_API_KEY=anthropic-key:latest # B) Railway: deploy + set environment variables railway up # streams build + deploy logs railway variables -- set "MODEL_ID=... " \ --set "ANTHROPIC_API_KEY= sk-..." Lưuý: --concurrencyđểthấpchoagent: mỗirequestgiữmộtconnectionstreaming dài. Secret tiêm qua --set-secrets / Variables tab —không bao giờnhét vào image. Giảngviên (VinUni) AICB· Deployment 2026 79/ 84

---

<!-- chiron-source-span: {"source_span_id":"ab08842f-85ad-5f69-ba3a-7f373fc60977","locator":{"kind":"page","page":97,"label":"Slide 97","section_title":"Cost-GuardTối Thiểu — Chặn TrướcKhi Gọi","extraction_method":"pdf-text-layer"},"checksum":"eb0748355615c104ea1ee4cef91830c733813e7e222398146716d2208e53eeed"} -->

## Slide 97 - Cost-GuardTối Thiểu — Chặn TrướcKhi Gọi

MAX_USD = float(os.environ["MAX_USD_PER_REQ"]) # e.g. 0.05

```text
def guard(messages, model, user_id):
in_tok = count_tokens(messages, model) # count tokens
est = in_tok/1e6*IN_PRICE + MAX_OUT/1e6*OUT_PRICE
```
if est > MAX_USD: # admission control raise BudgetExceeded(f"${est:.3f} > ${MAX_USD}") metrics.tag(user=user_id, feature= "chat", usd=est)

```text
return est
```
3đòn bẩy FinOps Tag mọi call, đếm token có thẩm quyền,ép budget trước khi gọi LLM. Nhớ: alert củaprovider là phản ứngsau;admission control chặntrước. Giảngviên (VinUni) AICB· Deployment 2026 80/ 84

---

<!-- chiron-source-span: {"source_span_id":"a664e3c5-4dd5-5120-a3ea-559eb5b8618c","locator":{"kind":"page","page":98,"label":"Slide 98","section_title":"Hands-on & Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"b9b3f6b07e13960f4863bfe01faabfd7f2b518f4e4f593976a867f0d2b7a8567"} -->

## Slide 98 - Hands-on & Key Takeaways

16 Mục tiêu cuối cùng rất cụ thể: agent có public URL, ai cũng truy cập được, có health check, có basic auth, có cost guard

---

<!-- chiron-source-span: {"source_span_id":"64184113-0eff-55fd-9cba-d137c68ea60c","locator":{"kind":"page","page":99,"label":"Slide 99","section_title":"Lab12: Containerize &Deploy","extraction_method":"pdf-text-layer"},"checksum":"ce530ff23c5607fccbf3fbb6d0e8e7462bee26dfd0b9d3f9f87caf2bf255b7ab"} -->

## Slide 99 - Lab12: Containerize &Deploy

Mụctiêu lab Đónggói agent thành container,deploylên cloud, và có public URLhoạt động.

1. ViếtDockerfile (multi-stage +uv,slim base, non-root,<500MB)

```text
2. Build& test container locally:docker build → docker run →scanbằng Trivy
3. Thêmstreaming endpoint (SSE) + healthcheckGET /health
```

4. Deploylên Railway hoặc Render: connect repo→setenv vars →deploy

5. Thêmbasic auth (API key) +một rate limit / spending guardđơn giản

6. Demo: gửi request tớipublic URL, nhận response streaming từagent Giảngviên (VinUni) AICB· Deployment 2026 81/ 84

---

<!-- chiron-source-span: {"source_span_id":"29ac1981-1cca-5cbb-9fb3-5fbfa07b8a2b","locator":{"kind":"page","page":100,"label":"Slide 100","section_title":"BlueprintCần Nộp","extraction_method":"pdf-text-layer"},"checksum":"06468abc2472012c684afa743e5b2723d8876c5775a6e5943bdc21ef6696cd58"} -->

## Slide 100 - BlueprintCần Nộp

Container

- Dockerfile(multi-stage, uv,
<500MB)

- docker-compose.yml+
.dockerignore

- Healthcheck + streaming endpoint

- Trivyscan sạch (no high CVE)
Deployment

- PublicURL hoạt động (HTTPS)

- Envvars đúng cách (không
hardcode)

- Basicauth (API key) + costguard

- Demorequest/response streaming
Lưu ý: Không cần enterprise-grade. Điều cần chứng minh là bạnbiết cách đưa agenttừ localhost lên cloud,nó hoạt động, vàkhôngđốt tiền. Giảngviên (VinUni) AICB· Deployment 2026 82/ 84

---

<!-- chiron-source-span: {"source_span_id":"ca7eb87d-d605-5de9-a4d8-150184c379f2","locator":{"kind":"page","page":101,"label":"Slide 101","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"6e5d3cd7e4851c97caa6b3750ed0dd6e8eec328b04f734e7ca75f7be85c8b206"} -->

## Slide 101 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 Cùngcỗmáy,kháccáihộp: shipnhưthường—nhưng thetest (evalgate), thebill (token), thedependency (model)đều bị định nghĩa lại.

```text
2 Container 2026:multi-stage + uv + slim/distroless, non-root, scan CVE; SSE + externalize
```
state. 3 Chạyởđâu=quyếtđịnhdeploy: server-sidemặcđịnh;“client-side”cầnBFFproxy;keyless chỉkhi on-device. 4 Platform theo timeout, scale theo concurrency;router failover + cache cắt cost. Budget KHÔNGtựchặn →admissioncontrol + eval gate trongCI. 5 Đừng mặc định:framework và runtime làhai tầng tách rời; “model là API ngoài” làlựa chọn,không phải định luật. Giảngviên (VinUni) AICB· Deployment 2026 82/ 84

---

<!-- chiron-source-span: {"source_span_id":"43225db6-af32-5902-83ea-b714c0fbb0a6","locator":{"kind":"page","page":102,"label":"Slide 102","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"4365e07985172e70ef2d2be64a13b3fb9af106429b998e666f745b4a0c01bb5e"} -->

## Slide 102 - Tiếptheo & Bài tập

Monitoring, Logging & Observabil- ity “Agent deploy xong, 3 ngày sau: la- tency tăng gấp đôi, cost tăng 300%. Bạn không biết cho đến khi user phàn nàn. ”

- Đọctrước: LangSmith hoặc
Langfusequickstart (20 phút)

- Chuẩnbị: agentdeployedtừLab
12cần có endpoint để gắn monitoring

- Suynghĩ: metrics nàoquan
trọngnhất cho AI agent trên production? Giảngviên (VinUni) AICB· Deployment 2026 83/ 84

---

<!-- chiron-source-span: {"source_span_id":"69c80dd8-6aef-5ea7-a1ae-fd3ee6137678","locator":{"kind":"page","page":103,"label":"Slide 103","section_title":"TàiLiệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"04b8fc6f2be6d62691e34399b6c2b8b60149e66d1ef04a9a446b43bdffb1545d"} -->

## Slide 103 - TàiLiệu Tham Khảo

```text
1. Astral, Using uv in Docker —docs.astral.sh/uv/guides/integration/docker/. Multi-stage buildhiện đại
```
choPython.

2. GoogleCloud, Cloud Run request timeout & concurrency —cloud.google.com/run/docs. 60 phútmax, concurrency80/1000.

3. ModelContext Protocol, Transports & Authorization ( 2026-07-28)—modelcontextprotocol.io. StreamableHTTP stateless+OAuth 2.1 + security bestpractices.

4. OWASP, Top 10 for LLM Applications 2026 (3/8/2026;75% vote + 25% từ6.639 sự cố thật) &Top 10 for Agentic Applications 2026 —genai.owasp.org. LLM10; ASI03/ASI04.

5. AdamWiggins, The Twelve-Factor App —12factor.net. FactorVI (stateless processes). Giảngviên (VinUni) AICB· Deployment 2026 84/ 84

---

<!-- chiron-source-span: {"source_span_id":"04418ae3-f85e-5aed-a656-65b9158f6afa","locator":{"kind":"page","page":104,"label":"Slide 104","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"36ba1a0b75fb13332c4ec08b65e602df9001925d8498963fe9ae89440efe91c8"} -->

## Slide 104 - Hỏi& Đáp

Từ hôm nay, agent không còn chỉ chạy trên máy bạn. Nó đã là một service thật sự — có URL, có bảo vệ, và không đốt sạch ngân sách.
