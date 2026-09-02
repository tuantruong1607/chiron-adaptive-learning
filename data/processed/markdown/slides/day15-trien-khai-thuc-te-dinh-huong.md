---
schema_version: 1
course_id: rag-intensive
document_id: "af3f3f4a-1e68-51b9-97b1-24ed64e50002"
document_version_id: "76119d3e-abec-59bf-8e89-ab8225e6ed61"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Triển Khai Thực T ế, Chi Phí Vận"
source_file: "day15-trien-khai-thuc-te-dinh-huong.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\day15-trien-khai-thuc-te-dinh-huong.pdf"
source_sha256: "74ae212063fc0db3288547f59c7d972fc462dd2e3a81ac7862c611c97be195b3"
parser_version: chiron-structured-markdown-v1
page_count: 55
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":55}"
language: vi
---

# Triển Khai Thực T ế, Chi Phí Vận

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"59d5fd00-985e-5754-9eb2-6b2d90e39423","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Triển Khai Thực T ế, Chi Phí Vận","extraction_method":"pdf-text-layer"},"checksum":"45eed96221b56f027d1c56dd1e70813faf0b20d0ff152c2376b53d1407a9fab7"} -->

## Slide 1 - Triển Khai Thực T ế, Chi Phí Vận

Hành & Định Hướng Chuyên Sâu AICB-P1 · Ngày 15 · Ngày cuối Phase 1 T ên Giảng Viên VinUniversity · Phase 1 · 2026

---

<!-- chiron-source-span: {"source_span_id":"29d46dd4-a560-5e68-86ab-0ff23dd32855","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"2a734c42c02dfefcd3e6b4d87f042e81dd375b657aa69811f1f3341dd4ee5f28"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “15 ngày trước bạn chưa biết LLM hoạt động thế nào. Hôm nay bạn đã có agent deployed, monitored, và evaluated. Câu hỏi bây giờ: đi sâu hướng nào?” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"e62f5afb-ad18-5411-9b67-ada051c733ed","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"d965fd644704eff1930edde30c6eee7e6d1cbe7a3b4006a267a3ac618d0b60ad"} -->

## Slide 3 - Nội Dung Bài Học

1. 15 ngày nhìn lại

2. Triển khai enterprise

3. Cost anatomy

4. Cost optimization

5. Scaling production

6. Skills map recap

7. 3 Track Phase 2

8. Career paths & AMA Giảng viên (VinUni) AICB · Ngày 15 2026 1 / 41

---

<!-- chiron-source-span: {"source_span_id":"14340663-ce0e-534f-930d-6744fa029033","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu Ngày 15","extraction_method":"pdf-text-layer"},"checksum":"403e0575d422e23687437f305d1548afeacee822b3d01c1cfedd0fde55ac5510"} -->

## Slide 4 - Mục Tiêu Ngày 15

- Hiểu thách thức triển khai enterprise: security, compliance, legacy systems

- Phân tích cost anatomy của AI system và biết cách tối ưu chi phí

- Nắm cost optimization strategies: model routing, semantic caching, prompt
compression

- Nhìn lại skills map đã tích luỹ qua 15 ngày

- Chọn track Phase 2 phù hợp với mục tiêu nghề nghiệp
Giảng viên (VinUni) AICB · Ngày 15 2026 2 / 41

---

<!-- chiron-source-span: {"source_span_id":"573e22aa-c3b4-5d03-a07f-6c665c74b9f3","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"15 Ngày Nhìn Lại","extraction_method":"pdf-text-layer"},"checksum":"1d3e5ac2e3c7dd80bca873d57aff0e786a47f8ef82238c16a52ea87d6129e47b"} -->

## Slide 5 - 15 Ngày Nhìn Lại

01 T ừ “AI là gì?” đến agent deployed, monitored, evaluated — một hành trình 15 ngày xây dựng năng lực thực chiến

---

<!-- chiron-source-span: {"source_span_id":"a7c6f255-349a-516c-b723-456d51bd4268","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Timeline: Hành Trình 15 Ngày","extraction_method":"pdf-text-layer"},"checksum":"6b1032b1f38b0b8fae69215a825ff6a1a7a20cdb12b2299405aee5174a230720"} -->

## Slide 6 - Timeline: Hành Trình 15 Ngày

N1 LLM N2 Bài toán N3 Agent N4 T ool Call N5 Product N6 PM N7 Data N8 RAG N9 Multi N10 UX N11 Safety N12 Deploy N13 Monitor N14 Eval N15 Wrap-up Nền tảng Xây dựng Production 3 giai đoạn: Hiểu nền tảng (N1–5) → Xây dựng hệ thống (N6–10) → Đưa lên production (N11–15) Giảng viên (VinUni) AICB · Ngày 15 2026 3 / 41

---

<!-- chiron-source-span: {"source_span_id":"4c6c7938-dc17-5332-be5a-0f0cf56dde65","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Milestones Đã Đạt Được","extraction_method":"pdf-text-layer"},"checksum":"b5119ea41c3d76ab7bae3192e6c47cf5413d90ff3e415e2c1865e40014dee06f"} -->

## Slide 7 - Milestones Đã Đạt Được

Kỹ thuật

- Gọi LLM API, so sánh models

- Build ReAct agent + tool calling

- RAG pipeline grounded

- Multi-agent + MCP

- Guardrails + safety testing
Sản phẩm

- Problem statement + PRD

- UX với trust layer

- Deployed trên cloud

- Monitoring + alerting

- Evaluation + benchmark
Thông điệp Bạn không chỉ học lý thuyết. Bạn đã build, deploy, monitor, và evaluate một AI product thật. Giảng viên (VinUni) AICB · Ngày 15 2026 4 / 41

---

<!-- chiron-source-span: {"source_span_id":"2ed272b4-2a0d-5ec4-ba81-a2aea6dadcfb","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Triển Khai Enterprise","extraction_method":"pdf-text-layer"},"checksum":"e2d8028841778549e6c735405023a9330acaee4f328dec17506b54a41c3c2ebf"} -->

## Slide 8 - Triển Khai Enterprise

02 Lab deploy lên Railway là bước đầu. Enterprise có thêm security policies, compliance, legacy systems, và network restrictions

---

<!-- chiron-source-span: {"source_span_id":"77341e74-87c7-566a-b581-1ffc7b0dbe47","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Enterprise Challenges","extraction_method":"pdf-text-layer"},"checksum":"58be4561e7c7135f9e13f17f5047fd5d815ac328973cb526f4dc483311ebd319"} -->

## Slide 9 - Enterprise Challenges

Security & Compliance

- Data không được rời khỏi VN

- PII phải encrypted at rest

- Audit trail cho mọi AI decision

- Compliance: PDPA, ngành tài
chính T echnical Constraints

- Legacy systems, mainframe

- Network restrictions,
air-gapped

- On-premise infrastructure only

- Limited GPU resources
Lưu ý: Enterprise deploy khác startup deploy. Không phải mọi thứ đều “push lên cloud” được. Đôi khi LLM phải chạy on-premise. Giảng viên (VinUni) AICB · Ngày 15 2026 5 / 41

---

<!-- chiron-source-span: {"source_span_id":"a0c7cc39-db6d-5fa3-bf85-4d18b3b31460","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"On-Premise vs Cloud vs Hybrid","extraction_method":"pdf-text-layer"},"checksum":"18f028fa91aeab43c9825d5a3a41109d679fe9ea0a096734c1115834a7a29ab9"} -->

## Slide 10 - On-Premise vs Cloud vs Hybrid

Cloud API On-Premise Hybrid Data control Thấp Cao nhất T uỳ chọn Setup time Phút T uần–tháng T uần Cost model Per-token Capex + GPU Mixed Performance Nhanh T uỳ hardware T uỳ routing Best for MVP, startup Bank, gov Enterprise Trend 2025–2026 Hybrid đang trở thành default cho enterprise VN: sensitive data on-prem, non- sensitive qua cloud API. Giảng viên (VinUni) AICB · Ngày 15 2026 6 / 41

---

<!-- chiron-source-span: {"source_span_id":"7460c724-ca3b-5aa9-b950-44c78def678b","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Self-Hosted LLM: vLLM & Ollama","extraction_method":"pdf-text-layer"},"checksum":"a13ff742a5c3173e91422c678f87eeac57b0555f1b266e0750b224cadc5dd102"} -->

## Slide 11 - Self-Hosted LLM: vLLM & Ollama

vLLM Production-grade inference. PagedAttention, continuous batch- ing. Dùng khi: cần throughput cao, có GPU server Ollama Run models locally, dễ setup. Download model, chạy 1 lệnh. Dùng khi: dev, demo, edge deploy- ment Lưu ý: Self-hosted tiết kiệm khi volume cao (> 1M tokens/ngày). Dưới mức đó, cloud API rẻ hơn khi tính cả chi phí GPU, ops, và maintenance. Giảng viên (VinUni) AICB · Ngày 15 2026 7 / 41

---

<!-- chiron-source-span: {"source_span_id":"f353aae8-9e67-5a33-9e43-97d15a99eef6","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Cost Anatomy Của AI System","extraction_method":"pdf-text-layer"},"checksum":"a0885a089c71ca26d388e2dcf57de7ea4698b3e9d6911bd42690cbb5d66ca616"} -->

## Slide 12 - Cost Anatomy Của AI System

03 AI agent production không chỉ tốn tiền token. Hiểu đầy đủ cost structure mới optimize đúng chỗ

---

<!-- chiron-source-span: {"source_span_id":"8ccaeea7-76f5-573b-99b4-0e35e4dcc0a6","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Cost Breakdown","extraction_method":"pdf-text-layer"},"checksum":"515049b996bda8aad2838325009a01b7c675ae6687515549ce59b0787237a954"} -->

## Slide 13 - Cost Breakdown

API T okens Input + Output Compute CPU/GPU Storage Vector DB Human Review Ops Monitor 40–60% 15–25% 5–10% 10–15% 5–10% Insight API tokens chiếm 40–60% cost. Optimize token usage là ROI cao nhất cho hầu hết AI systems. Giảng viên (VinUni) AICB · Ngày 15 2026 8 / 41

---

<!-- chiron-source-span: {"source_span_id":"6e4359cd-6fd1-5ce6-a649-3ff20a39b5ca","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"LLM API Cost Calculator","extraction_method":"pdf-text-layer"},"checksum":"a78cd8778e1810294c25bcaab18549af25be111953efba0fe6dc48e2c3a2c671"} -->

## Slide 14 - LLM API Cost Calculator

Công thức Monthly cost = (avg input tokens + avg output to- kens) × price per token × requests per day × 30 ngày Ví dụ thực tế 1000 tokens/request $3/1M input tokens (Sonnet) 500 requests/ngày = 1000 × $0.000003 × 500 × 30 = $45/tháng chỉ LLM API Lưu ý: Hidden costs thường gấp 1.5–2x API cost: retry overhead, guardrails LLM calls, monitoring, eval pipeline. Budget phải tính tổng, không chỉ API. Giảng viên (VinUni) AICB · Ngày 15 2026 9 / 41

---

<!-- chiron-source-span: {"source_span_id":"ffd8c390-39bc-5161-9614-d2005b8189f7","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Budget Planning: 3-Tier Model","extraction_method":"pdf-text-layer"},"checksum":"6c319d2e05b7daec2e7ecb54bd6d722601a9aa1acb0618e95e07193be79e7169"} -->

## Slide 15 - Budget Planning: 3-Tier Model

Tier Traffic Estimated cost Stack MVP < 100 req/ngày $50– 200/tháng Cloud API + Rail- way Growth 100–5K req/ngày $200– 2K/tháng Cloud API + ECS/Cloud Run Scale > 5K req/ngày $2K+/tháng Hybrid / self- hosted Nguyên tắc Bắt đầu MVP tier. Chỉ upgrade khi traffic thật sự đòi hỏi. Premature optimization is the root of all evil. Giảng viên (VinUni) AICB · Ngày 15 2026 10 / 41

---

<!-- chiron-source-span: {"source_span_id":"447f3e60-4c46-5582-9f30-280315761cef","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Cost Optimization Strategies","extraction_method":"pdf-text-layer"},"checksum":"21980d3c49fafd04273ad3b8e0509b1f40a6223d4c19f0571fe869a45b0a0e7e"} -->

## Slide 16 - Cost Optimization Strategies

04 Khi cost bắt đầu đáng kể, 4 strategies sau giúp giảm 30– 70% chi phí mà không ảnh hưởng chất lượng

---

<!-- chiron-source-span: {"source_span_id":"92b59ce0-d35f-584b-9fd7-8370d051d06f","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"4 Strategies Chính","extraction_method":"pdf-text-layer"},"checksum":"904737272491b72e18e849662bf1128fe63a9c16612ab6ccd7371c44595944fd"} -->

## Slide 17 - 4 Strategies Chính

1. Model Routing Cheap model (Haiku) cho simple tasks. Expensive model (Opus) chỉ cho complex. Tiết kiệm: 40–60% token cost

2. Semantic Caching Cache LLM responses cho similar queries. Dùng embedding similarity để match. Tiết kiệm: 20–40% nếu queries lặp nhiều

3. Prompt Compression Tóm tắt context trước khi gửi LLM. Giảm token count mà giữ thông tin. Tiết kiệm: 15–30% input tokens

4. Self-Hosted Models vLLM, Ollama cho high-volume. Break-even: khoảng 1M+ to- kens/ngày. Tiết kiệm: 50–80% so với API khi scale Giảng viên (VinUni) AICB · Ngày 15 2026 11 / 41

---

<!-- chiron-source-span: {"source_span_id":"124b295f-b95b-53a3-9430-e8272c94d688","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Model Routing — Chi Tiết","extraction_method":"pdf-text-layer"},"checksum":"8cb2ba995f47501335555f300032bdfe40f003080f276f87ec811ef8ec4a6b67"} -->

## Slide 18 - Model Routing — Chi Tiết

User Request Complexity Classifier Haiku / GPT-4o-mini Fast + Cheap Opus / GPT-4o Strong + Expensive simple complex 70% traffic 30% traffic Kết quả Nếu 70% requests dùng cheap model (10x rẻ hơn), tổng cost giảm khoảng50% mà quality gần như không đổi trên simple tasks. Giảng viên (VinUni) AICB · Ngày 15 2026 12 / 41

---

<!-- chiron-source-span: {"source_span_id":"5637e3d7-cef8-51e0-a401-797730bbdf1f","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Scaling & Reliability Produc","extraction_method":"pdf-text-layer"},"checksum":"656a6f184b7d12f39863d309c4a48e07ed1974f2d73c039be51ac81b6bcb2754"} -->

## Slide 19 - Scaling & Reliability Produc

05 Scaling & Reliability Produc- tion Khi agent phục vụ enterprise, cần thêm queue, circuit breaker, và SLA commitment

---

<!-- chiron-source-span: {"source_span_id":"aac7a0ff-e0fd-5720-9100-ac0cd0895530","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Production Patterns","extraction_method":"pdf-text-layer"},"checksum":"c824dd9ff6bd13def78a694dde530940556946821f965c3433760d18e54d4d27"} -->

## Slide 20 - Production Patterns

Queue-Based Processing High load → request queue → smooth out spikes. User nhận “đang xử lý” thay vì timeout. T ool:Redis Queue, Celery, Bull Circuit Breaker Khi LLM API down, degrade grace- fully. Trả cached response hoặc fallback message. Pattern: closed → open → half-open Horizontal Scaling Stateless agent → N instances. Day 12: đã design cho stateless. Scale: thêm instances khi load tăng SLA Considerations Enterprise cần uptime commitment. 99.9% = max 8.7h downtime/năm. Cần: redundancy, failover, monitor- ing Giảng viên (VinUni) AICB · Ngày 15 2026 13 / 41

---

<!-- chiron-source-span: {"source_span_id":"a82da1e2-baf8-58b1-89cb-6168def48ce4","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Skills Map Sau 15 Ngày","extraction_method":"pdf-text-layer"},"checksum":"947077576fef8c4a712715fe3ae9edcde4f078057eb3b37087fcad662ae15e47"} -->

## Slide 21 - Skills Map Sau 15 Ngày

06 3 competency pillars đã được xây dựng — mỗi pillar mở ra một career direction khác nhau

---

<!-- chiron-source-span: {"source_span_id":"1547f5fd-68f9-560e-800a-8960ab5c458a","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Skills Map — 3 Pillars","extraction_method":"pdf-text-layer"},"checksum":"3fd4d7c702a831201aa38c8b61af00e64573d6d3b9befbfcac87daf93203ba4f"} -->

## Slide 22 - Skills Map — 3 Pillars

CP3: AI Engineering

- LLM API

- ReAct Agent

- Prompt Engineering

- Tool Calling

- Embedding

- RAG Pipeline

- Multi-Agent

- Guardrails

- Evaluation
CP2: Infrastructure

- Vector Store

- Data Pipeline

- Docker

- Cloud Deploy

- Monitoring

- Structured Logging

- Tracing
CP1: Business

- Problem Statement

- AI Readiness

- PRD

- Risk Assessment

- ROI Analysis

- UX Design

- Cost Analysis
Sau 15 ngày: bạn đã có deployed, monitored, evaluated AI product + skills across 3 pillars. Giảng viên (VinUni) AICB · Ngày 15 2026 14 / 41

---

<!-- chiron-source-span: {"source_span_id":"da064bf2-c4c1-513e-a114-b4cc2a111fdb","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Market Intelligence & Định","extraction_method":"pdf-text-layer"},"checksum":"1328b17342069341e31724db245d5fb7dd411f67dd403c3974b4b6bfdad64b7c"} -->

## Slide 23 - Market Intelligence & Định

07 Hướng Nghề Nghiệp Sâu Trước khi chọn track Phase 2, hãy nhìn thị trường việc làm AI toàn cầu qua lăng kính của WEF, McKinsey, Stanford HAI, và chính các AI lab lớn nhất thế giới

---

<!-- chiron-source-span: {"source_span_id":"9352f62f-a4ca-5846-acb7-c2b662794720","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Thị Trường Việc Làm AI T oàn Cầu Đến 2030","extraction_method":"pdf-text-layer"},"checksum":"c496551d073e75136c7358848217cb51148206fbc8cec08d5f99ca8836c149cb"} -->

## Slide 24 - Thị Trường Việc Làm AI T oàn Cầu Đến 2030

170M Việc làm mới được tạo ra 92M Việc làm bị mất đi +78M Tăng trưởng ròng (+7%) Bức tranh lớn 86% nhà tuyển dụng kỳ vọng AI sẽ biến đổi doanh nghiệp của họ đến 2030. Nhưng 63% coi khoảng cách kỹ năng là rào cản lớn nhất — cơ hội không tự động biến thành việc làm nếu thiếu kỹ năng đúng. Nguồn: World Economic Forum, Future of Jobs Report 2025 Giảng viên (VinUni) AICB · Ngày 15 2026 15 / 41

---

<!-- chiron-source-span: {"source_span_id":"08495677-e43c-5438-bf87-34cb6b291f4f","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Việt Nam Trong Bức Tranh T oàn Cầu","extraction_method":"pdf-text-layer"},"checksum":"d4f7571112822c91589748a08cdb83993bcb496155a37fc9a73335daf0f53a60"} -->

## Slide 25 - Việt Nam Trong Bức Tranh T oàn Cầu

Chỉ số Việt Nam T oàn cầu Tổ chức có chương trình AI đang chạy 96% 88% Skills gap là rào cản chuyển đổi 78% 63% Kế hoạch cắt giảm nhân sự vì AI 58% 41% Kế hoạch reskilling để làm cùng AI 52% 77% Cải thiện phát triển nhân tài nội bộ ≈0% 84% Đọc vị: nhu cầu AI ở Việt Nam cao hơn thế giới, nhưng năng lực đào tạo lại nội bộ yếu hơn nhiều — vừa là cơ hội vừa là lời cảnh báo cho sinh viên được đào tạo bài bản. Nguồn: World Economic Forum, Future of Jobs Report 2025 — Vietnam Country Profile Giảng viên (VinUni) AICB · Ngày 15 2026 16 / 41

---

<!-- chiron-source-span: {"source_span_id":"838bc9ac-215a-5d61-9bcc-df6c36dd9761","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Nghịch Lý 2025–2026: Đầu Tư T ối Đa, Cắt Giảm T ối Đa","extraction_method":"pdf-text-layer"},"checksum":"72b43511f090be7a268f8defd4411a83952f7f23b2ab85b498ce2a847c475ae1"} -->

## Slide 26 - Nghịch Lý 2025–2026: Đầu Tư T ối Đa, Cắt Giảm T ối Đa

Đầu tư kỷ lục

- Big Tech capex 2025: ~$325 tỷ
(+46% Y oY)

- Hướng dẫn 2026: $725 tỷ (+77%)

- Đầu tư AI doanh nghiệp toàn cầu:
$252.3 tỷ (2024) → $581.7 tỷ (2025, +130%) Nguồn: Stanford HAI AI Index 2025/2026; CNBC Cắt giảm song song

- Amazon: cắt 14.000 + 16.000 vị
trí (2025–2026)

- Meta: cắt 8.000 (10% nhân sự)

- Microsoft: 8.750 nghỉ hưu tự
nguyện “Chúng tôi sẽ cần ít người hơn cho một số công việc đang làm hôm nay.” — Andy Jassy, CEO Amazon Nguồn: CNBC (2025–2026) Giảng viên (VinUni) AICB · Ngày 15 2026 17 / 41

---

<!-- chiron-source-span: {"source_span_id":"32dbe21b-23de-5c9a-9519-ecc2a14d621a","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"T ốc Độ Áp Dụng AI Đang T ăng T ốc","extraction_method":"pdf-text-layer"},"checksum":"045014c52460b6f2ba1d273bd214a37a5320ece460b2e2398ff0082397d15477"} -->

## Slide 27 - T ốc Độ Áp Dụng AI Đang T ăng T ốc

88% Tổ chức dùng AI ở ít nhất 1 chức năng (McKinsey 2025) 72% Dùng generative AI — tăng vọt từ 33% năm 2024 300%+ Tăng trưởng AI hiring toàn cầu trong 8 năm (LinkedIn) 20x Số người thêm AI skill vào hồ sơ từ 2016 (LinkedIn) Nguồn: McKinsey State of AI 2025; LinkedIn Work Change Report 2025 Giảng viên (VinUni) AICB · Ngày 15 2026 18 / 41

---

<!-- chiron-source-span: {"source_span_id":"7600ea36-0f11-5854-99b6-3d7b52a9cd39","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Ba Nhóm Nghề AI: Từ Nghiên Cứu Đến Sản Phẩm","extraction_method":"pdf-text-layer"},"checksum":"9bd3bc8a3ac8cd441dfdff77f89ee0f4daf32f7599fa34f2ff8062b40c551495"} -->

## Slide 28 - Ba Nhóm Nghề AI: Từ Nghiên Cứu Đến Sản Phẩm

Sau khi thấy bức tranh vĩ mô, hãy đi sâu vào 3 nhóm nghề cụ thể mà 3 track Phase 2 dẫn tới — mỗi nhóm có tốc độ tăng trưởng, mức lương, và rào cản gia nhập khác nhau. AI Engineer #1 fastest-growing job title (LinkedIn, 2 năm liên tiếp) AI Infrastructure Kỹ năng khó tuyển #1 toàn cầu (ManpowerGroup 2026) AI Product Tăng trưởng +300%/3 năm, nhưng thiếu cửa junior Giảng viên (VinUni) AICB · Ngày 15 2026 19 / 41

---

<!-- chiron-source-span: {"source_span_id":"b8dd5b15-f1b5-5e7b-b743-a86dbebbb0fc","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"AI Engineer / AI Researcher","extraction_method":"pdf-text-layer"},"checksum":"a08583982192a495210d4f0067e5e93c4d5197ba7160765b0d3e55ab1275afa1"} -->

## Slide 29 - AI Engineer / AI Researcher

Demand & Lương #1 fastest-growing job title 2 năm liên tiếp (LinkedIn) ML Engineer trung vị: $272.5K (lev- els.fyi) Frontier lab: OpenAI SWE $253K– $1.27M+ Case cực đoan: gói đãi ngộ re- searcher tới $1.5 tỷ (Meta, bị từ chối) Rào Cản Gia Nhập Research track: gần như bắt buộc PhD (OpenAI/DeepMind/FAIR) Applied track: cử nhân/thạc sĩ + portfolio mạnh là đủ PhD mới tại Mỹ/Canada tăng 22% (2022–2024) nhưng phần lớn vào academia, không phải industry Nguồn: LinkedIn Jobs on the Rise 2025; levels.fyi; Stanford HAI AI Index 2025; TechCrunch Giảng viên (VinUni) AICB · Ngày 15 2026 20 / 41

---

<!-- chiron-source-span: {"source_span_id":"7253de02-8a09-5e47-8acc-6361a900b29f","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"AI Infrastructure: Nhóm Khó Tuyển Nhất Thế Giới","extraction_method":"pdf-text-layer"},"checksum":"52e30705838dec215a2732b58f030b769aa8089817ff6a6cc5e468ec0d0672b0"} -->

## Slide 30 - AI Infrastructure: Nhóm Khó Tuyển Nhất Thế Giới

Demand & Lương MLOps: tăng trưởng 9.8x trong 5 năm (LinkedIn Emerging Jobs) Senior/staff MLOps: $257K–$312K Chi tiêu hạ tầng AI toàn cầu: $334 tỷ (2025) → $497 tỷ (2026) → vượt $1.000 tỷ vào 2029 (IDC) Khan Hiếm Nhân Sự “AI Model & Application Develop- ment” là kỹ năng khó tìm #1 toàn cầu — vượt qua mọi ngành kỹ thuật truyền thống 20% nhà tuyển dụng toàn cầu xác nhận đây là kỹ năng khó tìm nhất 72% doanh nghiệp toàn cầu khó tuyển được nhân sự phù hợp Nguồn: ManpowerGroup 2026 Global Talent Shortage Survey; IDC AI Infrastructure Spending; LinkedIn Emerging Jobs Giảng viên (VinUni) AICB · Ngày 15 2026 21 / 41

---

<!-- chiron-source-span: {"source_span_id":"4743f92c-1fd6-59cf-8204-3bec567a0c81","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"AI Product: T ăng Trưởng Nhanh Nhưng Thiếu Cửa Junior","extraction_method":"pdf-text-layer"},"checksum":"1676a77234dc75bee5ce15250174c15d836b0455353713442dc277cf9c208045"} -->

## Slide 31 - AI Product: T ăng Trưởng Nhanh Nhưng Thiếu Cửa Junior

Demand & Lương AI PM postings: +300% trong 3 năm, nhân đôi năm 2025 Lương trung vị AI PM: $194–197K (hội tụ Glassdoor & axialsearch) AI Strategist: $208K trung vị, $279K ở cấp Director OpenAI PM trung vị: ~$860K Lưu ý: Chỉ 2% postings AI PM là cấp junior — 47% là cấp Manager+. AI Strategist còn nghiêng hơn: 69– 80% là Director/VP/C-suite. Thị trường “nóng nhưng chưa có lộ trình sự nghiệp rõ ràng cho người mới bắt đầu”. Nguồn: axialsearch Labor Market Analysis 2026; Glassdoor; levels.fyi Giảng viên (VinUni) AICB · Ngày 15 2026 22 / 41

---

<!-- chiron-source-span: {"source_span_id":"d93bf034-66f3-5d10-8d52-33313dd9e7f4","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"So Sánh T ổng Hợp: 3 Nhóm Nghề","extraction_method":"pdf-text-layer"},"checksum":"e9fe549cc82910af175dc09569d18d64e8a1c3996e15c111d7f5c222ceff3c41"} -->

## Slide 32 - So Sánh T ổng Hợp: 3 Nhóm Nghề

Tiêu chí Engineer/Researcher Infrastructure Product Tăng trưởng #1 fastest-growing title (2 năm) 9.8x/5 năm (MLOps) +300%/3 năm Lương trung vị $272.5K (ML Engineer) $257–312K (senior) $194–208K Rào cản gia nhập PhD (research) / portfolio (applied) 2–3 năm kinh nghiệm liền kề Portfolio sản phẩm, ít đòi bằng cấp sâu Độ khó tuyển Cao ở tier elite Khó nhất thế giới (Man- powerGroup #1) Thiếu cửa junior, không thiếu ứng viên Nguồn: Tổng hợp LinkedIn, levels.fyi, ManpowerGroup, axialsearch (2025–2026) Giảng viên (VinUni) AICB · Ngày 15 2026 23 / 41

---

<!-- chiron-source-span: {"source_span_id":"521861aa-bc40-5048-90a7-1b66e9f041fd","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Nghề Nào Được Lợi, Nghề Nào Chịu Rủi Ro?","extraction_method":"pdf-text-layer"},"checksum":"9d7e7105aeabb71b860b74c7eab0ede19820af540c1ffc493b04d041db4e87c5"} -->

## Slide 33 - Nghề Nào Được Lợi, Nghề Nào Chịu Rủi Ro?

Các báo cáo lớn dùng nhiều khái niệm dễ nhầm lẫn. Hiểu đúng 3 khái niệm sau trước khi đọc số liệu. Exposure (phơi nhiễm) — bao nhiêu% nhiệm vụ có thể được AI hỗ trợ/thực hiện — KHÔNG đồng nghĩa mất việc Automation vs Augmentation — AI thay thế hoàn toàn nhiệm vụ, hay hỗ trợ con người làm tốt hơn Net employment change — số liệu thực tế việc làm tăng/giảm — con số quan trọng nhất nhưng khó đo nhất Giảng viên (VinUni) AICB · Ngày 15 2026 24 / 41

---

<!-- chiron-source-span: {"source_span_id":"50a26dd1-4627-5f0d-bbf4-2686acf3a368","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Nghề T ăng Trưởng: Được AI Khuếch Đại","extraction_method":"pdf-text-layer"},"checksum":"010b5ff340ccec07a954463042c88fe40d9618d4bc54e458b3fa318ba956dd55"} -->

## Slide 34 - Nghề T ăng Trưởng: Được AI Khuếch Đại

T op nghề tăng trưởng (WEF)

1. Big Data Specialists

2. FinTech Engineers

3. AI/ML Specialists

4. Software Developers

5. DevOps Engineers Vì sao tăng trưởng Wage premium kỹ năng AI: 56% trung bình (PwC), có ngành tới 118% Việc làm cần kỹ năng AI tăng nhanh gấp 8 lần thị trường chung

### Năng suất ngành phơi nhiễm AI cao
tăng gần 4 lần (2018–2024) Lưu ý Việc làm vẫn tăng ngay cả ở nghề dễ tự động hoá nhất (PwC) — nỗi lo mất việc hàng loạt chưa xảy ra trên diện rộng. Nguồn: World Economic Forum 2025; PwC Global AI Jobs Barometer 2025 Giảng viên (VinUni) AICB · Ngày 15 2026 25 / 41

---

<!-- chiron-source-span: {"source_span_id":"133d671f-150b-5948-b110-a274fadcdcd8","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Nghề Suy Giảm: Bị AI Thay Thế","extraction_method":"pdf-text-layer"},"checksum":"625374bd822b53a204e80bf1df773c5c85867921ffce6a2be774208ff24dc8aa"} -->

## Slide 35 - Nghề Suy Giảm: Bị AI Thay Thế

T op nghề suy giảm (WEF)

1. Postal Service Clerks (–40%)

2. Bank Tellers (–35%)

3. Data Entry Clerks (–34%)

4. Cashiers/Ticket Clerks

5. Administrative Assistants Mức độ phơi nhiễm 40% việc làm toàn cầu phơi nhiễm AI (IMF): 60% (nước phát triển), 40% (mới nổi), 26% (thu nhập thấp) 80% lực lượng lao động Mỹ có ≥10% nhiệm vụ bị ảnh hưởng (Eloundou et al., Science 2024) Nghề phơi nhiễm cao nhất: biên phiên dịch viên Lưu ý: Nghịch lý: nghề lương cao có xu hướng phơi nhiễm AI cao hơn nghề lương thấp — ngược với làn sóng tự động hoá/robot trước đây. Nguồn: IMF SDN/2024/001; Eloundou et al. 2024, ScienceGiảng viên (VinUni) AICB · Ngày 15 2026 26 / 41

---

<!-- chiron-source-span: {"source_span_id":"9a277015-bd23-5773-8957-9d716d423801","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Case Study Cân Bằng: Tự Động Hoá Không Phải Lúc Nào Cũng Thắng","extraction_method":"pdf-text-layer"},"checksum":"0149b6011295dc286603c0980af9f2dc0f7972f4f12b9412b3c8fa0100fbc6bc"} -->

## Slide 36 - Case Study Cân Bằng: Tự Động Hoá Không Phải Lúc Nào Cũng Thắng

Klarna: Cắt Rồi Phải Tuyển Lại Cắt từ 5.500 xuống 3.400 nhân sự, thay bằng chatbot AI (2024) Sau đó: chất lượng dịch vụ giảm, khách hàng phàn nàn → tuyển lại người “Luôn phải rõ ràng với khách hàng rằng sẽ luôn có một con người nếu bạn muốn.” — Sebastian Siemiatkowski, CEO Klarna Nguồn: Fast Company; Entrepreneur (2025) Lập Trình Viên Trẻ: T ác Động Đã Xảy Ra Thật

### Việc làm lập trình viên 22–25 tuổi
giảm ~20% so với 2024

### Tỷ lệ thất nghiệp SV mới ra trường CS
6.1% vs 4.3% trung bình Mỹ “Tại sao thuê junior $90K khi GitHub Copilot chỉ tốn $10?” — kỹ sư senior, khảo sát CIO.com Nguồn: Stanford HAI AI Index 2026; CIO.com Giảng viên (VinUni) AICB · Ngày 15 2026 27 / 41

---

<!-- chiron-source-span: {"source_span_id":"4998fd41-635d-5e48-ad2c-05c381a8f4a4","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Việt Nam: Ngành Nào Phơi Nhiễm AI Cao Nhất?","extraction_method":"pdf-text-layer"},"checksum":"f4a5f0cbaa17593c7199a8c4e6bbc345c2020a3e71d5107bc98470fc212b64e5"} -->

## Slide 37 - Việt Nam: Ngành Nào Phơi Nhiễm AI Cao Nhất?

Ngành Mức độ phơi nhiễm AI Tài chính & Bảo hiểm 82.6% Bán buôn & Bán lẻ 76.3% Thông tin & Truyền thông 74.3% Đọc vị: phơi nhiễm cao không đồng nghĩa mất việc — đây là ngành có nhiều nhiệm vụ có thể được AI hỗ trợ, cơ hội để tăng năng suất nếu biết dùng AI đúng cách, thay vì lo sợ bị thay thế. Nguồn: IMF SDN/2024/001, phân tích theo ngành cho Việt Nam Giảng viên (VinUni) AICB · Ngày 15 2026 28 / 41

---

<!-- chiron-source-span: {"source_span_id":"96daf7fb-ddba-5169-a65c-3e9fd45a1c96","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Tương Lai & Chọn Track Cho Chính Bạn","extraction_method":"pdf-text-layer"},"checksum":"0c5f87c40c4cc0cf5cd292c39671aff7ced007715cc44bdcf38af8238621338b"} -->

## Slide 38 - Tương Lai & Chọn Track Cho Chính Bạn

Ngay cả những người tạo ra AI cũng đang tranh luận về tương lai việc làm. Đừng hoảng loạn theo một tuyên bố đơn lẻ — hãy nhìn toàn cảnh và tự quyết định.

### 4 câu hỏi sẽ giúp bạn chọn đúng track

1. Chuyên gia AI nói gì — và họ có thực sự đồng thuận không?

2. Việc làm junior có thực sự bị đe doạ?

3. Kỹ năng nào vẫn bền vững dù AI phát triển đến đâu?

4. Track nào phù hợp với sở thích, khả năng, và mức độ chấp nhận rủi ro của bạn? Giảng viên (VinUni) AICB · Ngày 15 2026 29 / 41

---

<!-- chiron-source-span: {"source_span_id":"b2fef24d-7311-5e68-984d-8811723d1be7","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Ngay Cả Chuyên Gia Cũng Thay Đổi Quan Điểm","extraction_method":"pdf-text-layer"},"checksum":"153e9965bd829da4d2048c3941b278ae0e6c4cba19f44997e26f27f0b9c013f3"} -->

## Slide 39 - Ngay Cả Chuyên Gia Cũng Thay Đổi Quan Điểm

5/2025 — Cảnh báo mạnh “AI có thể xoá sổ 50% việc làm văn phòng entry-level, thất nghiệp có thể lên 10–20%.” — Dario Amodei, CEO Anthropic (Axios) 1/2026 — Giữ nguyên lập trường Amodei tiếp tục cảnh báo trong essay “The Adolescence of Technology”; dự báo AGI có thể chỉ còn 1–2 năm 5/2026 — Đổi giọng cùng lúc với Altman “T ự động hoá 90% công việc nghĩa là con người làm 10% còn lại nhưng năng suất tăng gấp 10 lần.” — Amodei viện dẫn Jevons Paradox (Fortune). Cùng tuần, Sam Altman thừa nhận: “trực giác của tôi đã sai” về tác động entry-level (Time) Nguồn: Axios 5/2025; darioamodei.com 1/2026; Fortune & Time 5/2026 Giảng viên (VinUni) AICB · Ngày 15 2026 30 / 41

---

<!-- chiron-source-span: {"source_span_id":"353a62c9-cbaf-5232-80b3-7d858a0775cf","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Cuộc Tranh Luận: Có Nên Lo Về Việc Làm Junior?","extraction_method":"pdf-text-layer"},"checksum":"4c6cb16bec54be3c05993cefeadb33ce1ea98fae2485d8985fe1245526227cdd"} -->

## Slide 40 - Cuộc Tranh Luận: Có Nên Lo Về Việc Làm Junior?

Phe Cắt Giảm “Chúng tôi sẽ không tuyển thêm kỹ sư phần mềm năm sau vì năng suất đã tăng hơn 30% nhờ AI.” — Marc Benioff, CEO Salesforce 22% CHRO xác nhận có lãnh đạo đã ngừng tuyển entry-level vì AI (Gart- ner) Nguồn: Salesforce Ben; Gartner 2025–2026 Phe Phản Bác “Ý tưởng AI thay thế lập trình viên junior là một trong những điều ngu ngốc nhất tôi từng nghe.” — Matt Garman, CEO AWS IBM: tăng gấp 3 lần tuyển dụng entry- level tại Mỹ năm 2026 Nguồn: phát biểu công khai Matt Garman; IBM (Arvind Krishna), 2026 Giảng viên (VinUni) AICB · Ngày 15 2026 31 / 41

---

<!-- chiron-source-span: {"source_span_id":"b2268e52-904d-53dc-a076-9e22dcd2f257","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Kỹ Năng Bền Vững Trong Kỷ Nguyên AI","extraction_method":"pdf-text-layer"},"checksum":"4bc7f110991cac19883edfc63e0844903743ddc9d952dd8a779ba34e50409944"} -->

## Slide 41 - Kỹ Năng Bền Vững Trong Kỷ Nguyên AI

Dữ liệu thực đo, không chỉ là quan điểm Lao động 15+ năm kinh nghiệm đánh giá năng lực AI hiện tại thấp hơn ~10 điểm% so với lao động năm đầu — vì AI “thiếu phán đoán, nhận thức ngữ cảnh, và suy luận tình huống” (Anthropic Economic Index, 6/2026) Khảo sát ngành nhân sự

### Khi được hỏi kỹ năng con người nào quan trọng hơn khi AI đảm nhận nhiều việc hơn
kiểm soát chất lượng đầu ra AI (50%) và tư duy phản biện (46%) đứng đầu (Korn Ferry TA Trends 2026) Andrew Ng “Chỉ một phần nhỏ công việc của kỹ sư phần mềm là viết code.” — kỹ năng còn giá trị: thu thập yêu cầu, thiết kế hệ thống, giao tiếp liên chức năng. Nguồn: Ai4 2026 conference; Anthropic Economic Index; Korn Ferry Giảng viên (VinUni) AICB · Ngày 15 2026 32 / 41

---

<!-- chiron-source-span: {"source_span_id":"fd87c73f-e311-5905-bb72-7154876d5e0c","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Chọn Track: Framework Cá Nhân Hoá","extraction_method":"pdf-text-layer"},"checksum":"d61227caec100fd86c28c82e43d14084484ca9689cb733d46bc229bc6d000560"} -->

## Slide 42 - Chọn Track: Framework Cá Nhân Hoá

Trục Track 1 — Product Track 2 — Infra Track 3 — Application Cơ hội thị trường Tăng nhanh (+300%/3 năm), ít cửa junior Khó tuyển nhất thế giới (ManpowerGroup) #1 fastest-growing title 2 năm liên tiếp Độ khó gia nhập Thấp–trung bình: portfo- lio hơn bằng cấp Trung bình–cao: cần nền tảng hệ thống Cao (research) / trung bình (applied) Phù hợp sở thích Kinh doanh, chiến lược, giao tiếp đa bên Hệ thống, vận hành, độ tin cậy quy mô lớn Thuật toán, xây dựng sản phẩm kỹ thuật Rủi ro AI tác động ngược Thấp — vai trò phán đoán khó tự động hoá Thấp — vẫn cần giám sát hạ tầng dài hạn Trung bình ở phần code cơ bản (junior dev bị ảnh hưởng nhiều nhất) Việt Nam 2030 — cơ hội cho chính bạn Chiến lược AI Quốc gia đặt mục tiêu đào tạo 500.000 lao động có kỹ năng AI, trong đó 50.000 chuyên gia trình độ cao — đến 2030. Không có track “đúng tuyệt đối”; chọn theo giao điểm sở thích, năng lực, và mức độ sẵn sàng của chính bạn. Nguồn: Vietnam National Strategy on AI to 2030; Digital Policy Alert Giảng viên (VinUni) AICB · Ngày 15 2026 33 / 41

---

<!-- chiron-source-span: {"source_span_id":"e050bdb1-0c40-545e-af29-75ea30d47ed1","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"3 Track Giai Đoạn 2","extraction_method":"pdf-text-layer"},"checksum":"252d768fd822abce647477ae72b77a2e31ddeb3fca1ce8461d48d3b961b158c5"} -->

## Slide 43 - 3 Track Giai Đoạn 2

08 Phase 1 cho nền tảng chung. Phase 2 đi sâu theo hướng bạn chọn — mỗi track 3 tuần chuyên sâu

---

<!-- chiron-source-span: {"source_span_id":"af5e9556-d21f-516f-8096-89082f0134bf","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Track 1 — AI Business & Product","extraction_method":"pdf-text-layer"},"checksum":"92c77fcfb201b30486f5c4e1e8e79ad58fcba2a7e2eefebbab2c4543b452396a"} -->

## Slide 44 - Track 1 — AI Business & Product

Nội dung chính

- Product Strategy cho AI products

- Financial Modeling & ROI

- AI Governance & Compliance

- AI Act & regulatory landscape

- Go-to-market cho AI products
Phù hợp với ai

### Người muốn làm
AI Product Manager AI Business Analyst AI Strategist Output Business plan cho AI product + financial model + compliance checklist + go- to-market strategy. Giảng viên (VinUni) AICB · Ngày 15 2026 34 / 41

---

<!-- chiron-source-span: {"source_span_id":"5dbf12d6-7493-5cc5-b158-e8f827ec298e","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Track 2 — AI Infrastructure & Data","extraction_method":"pdf-text-layer"},"checksum":"d30e9b696df237e55b33bf730b6c96347903dc752641a6bd8bb1b26ee087002d"} -->

## Slide 45 - Track 2 — AI Infrastructure & Data

Nội dung chính

- Lakehouse & Feature Store

- vLLM deployment & optimization

- CI/CD cho AI (LLMOps)

- GPU FinOps & cost management

- Production data pipeline
Phù hợp với ai

### Người muốn làm
AI Data Engineer Platform Engineer MLOps Engineer Output Production-grade data pipeline + self-hosted LLM + CI/CD pipeline + moni- toring dashboard. Giảng viên (VinUni) AICB · Ngày 15 2026 35 / 41

---

<!-- chiron-source-span: {"source_span_id":"e232bd59-129f-5b5e-80a7-a05c508b563f","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"Track 3 — AI Application","extraction_method":"pdf-text-layer"},"checksum":"a679ce184552a07cc4e8781109c2ccb5ea13038a3aec5fa2efda3e7e023326ba"} -->

## Slide 46 - Track 3 — AI Application

Nội dung chính

- Advanced Agent patterns

- Memory & long-term context

- GraphRAG & knowledge graphs

- Fine-tuning & model customization

- Production evaluation systems
Phù hợp với ai

### Người muốn làm
AI Engineer LLM Engineer AI Agent Developer Output Advanced agent system + custom fine-tuned model + production eval pipeline + technical portfolio. Giảng viên (VinUni) AICB · Ngày 15 2026 36 / 41

---

<!-- chiron-source-span: {"source_span_id":"cd1fb4eb-958d-5993-8d01-22990038ba77","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Chọn Track Như Thế Nào?","extraction_method":"pdf-text-layer"},"checksum":"dea74a5738a53f284b84385ff7f7adfa44d38eee7de7558daea62fa34ed726fa"} -->

## Slide 47 - Chọn Track Như Thế Nào?

Thích business hay technical? Track 1 Business Thích infra hay app? Track 2 Infra Track 3 Application business technical infra app Lưu ý: Không có track “đúng” hay “sai”. Chọn theo mục tiêu nghề nghiệp và hứng thú cá nhân. Có thể đổi track sau tuần đầu nếu cần. Giảng viên (VinUni) AICB · Ngày 15 2026 37 / 41

---

<!-- chiron-source-span: {"source_span_id":"b3839849-29ce-5573-9ca8-8c1b1c87d674","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"Career Paths & Kết Thúc","extraction_method":"pdf-text-layer"},"checksum":"f45f256cc4dc8e6dc39413312ebce0cc2c2be6fc5e7ae4be29c6eae0a08193d7"} -->

## Slide 48 - Career Paths & Kết Thúc

09 Phase 1 15 ngày, 15 labs, 1 deployed product. Bạn không còn là beginner — bạn là builder

---

<!-- chiron-source-span: {"source_span_id":"7b97c3d9-7f41-5b4d-a90b-abe32eba5308","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Career Paths Sau Khoá Học","extraction_method":"pdf-text-layer"},"checksum":"d18d3062104e26badf3a8f12a059ab537efc295a1dbd21ba0e16e7495e4d1f27"} -->

## Slide 49 - Career Paths Sau Khoá Học

Pillar Roles Track Demand CP1 AI PM, AI BA, AI Strategist Track 1 Cao, khan hiếm CP2 AI Data Engi- neer, Platform Eng, MLOps Track 2 Rất cao CP3 AI Engineer, LLM En- gineer, Agent Dev Track 3 Cao nhất VSF Internship T ừ portfolio khóa học→ dự án thực tế tại Vingroup. Portfolio mạnh = cánh cửa mở. Giảng viên (VinUni) AICB · Ngày 15 2026 38 / 41

---

<!-- chiron-source-span: {"source_span_id":"3602a9c1-d994-5de5-9c21-259055216c64","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"AMA — Ask Me Anything","extraction_method":"pdf-text-layer"},"checksum":"b41636056a0cc45b83c3d613323a7e71d12989e1c1157977017f66f00afaf2f6"} -->

## Slide 50 - AMA — Ask Me Anything

Open Q&A Session Mọi câu hỏi về kỹ thuật, career, track selection, hoặc bất kỳ điều gì bạn muốn hỏi.

### Câu hỏi hay gặp nhất

- “Track nào dễ xin việc hơn?” — Cả 3 đều thiếu người. Chọn theo thế mạnh.

- “Fine-tuning có cần không?” — 80% use cases không cần. RAG + prompt đủ.

- “AI sẽ thay lập trình viên không?” — AI thay code, không thay builder.
Giảng viên (VinUni) AICB · Ngày 15 2026 39 / 41

---

<!-- chiron-source-span: {"source_span_id":"a50be892-01df-54aa-be45-ea85c2eba441","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"Final Assignment","extraction_method":"pdf-text-layer"},"checksum":"427b496284b1f575c3a7507364e0bd17ab455c4195b7429caed39d90c494c4ed"} -->

## Slide 51 - Final Assignment

Trước Ngày 16

1. Hoàn thành track selection form

2. Submit portfolio link (GitHub/demo URL)

3. Cost analysis cho agent (Lab 15)

4. Final presentation (10 phút) Portfolio nên có

- Deployed agent URL

- Monitoring dashboard
screenshot

- Evaluation report + RAGAS
scores

- README giải thích architecture

- Cost analysis
Giảng viên (VinUni) AICB · Ngày 15 2026 40 / 41

---

<!-- chiron-source-span: {"source_span_id":"50e75088-dd39-55ed-8f4c-3f16997ffe0c","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"9decede73ba40254e40f74c4d44880b74caf5f912cbdc1e3563e61d868aa4953"} -->

## Slide 52 - T ổng kết — Key T akeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Enterprise deploykhác startup: security, compliance, on-premise, hybrid. Hiểu con- text trước khi chọn architecture. 2 Cost optimization: model routing, semantic caching, prompt compression. API to- kens chiếm 40–60% cost — optimize đúng chỗ. 3 3 pillars, 3 tracks: CP1 (Business) → Track 1, CP2 (Infra)→ Track 2, CP3 (Application)

- Track 3. Chọn theo mục tiêu.
4 Y ou are no longer beginners — you are builders.15 ngày, 15 labs, 1 deployed product. Phase 2 đi sâu hơn. Giảng viên (VinUni) AICB · Ngày 15 2026 40 / 41

---

<!-- chiron-source-span: {"source_span_id":"fe2d9793-de58-5082-9300-f67bc1714422","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"T ài Liệu Tham Khảo","extraction_method":"pdf-text-layer"},"checksum":"b2e0879838805b63260eab482206c7ce5122773c53add491d88b19fbf73fa59a"} -->

## Slide 53 - T ài Liệu Tham Khảo

1. Anthropic & OpenAI Pricing Docs — anthropic.com/pricing, platform.openai.com/tokenizer. Cost calculator.

2. vLLM Documentation — docs.vllm.ai. Self-hosted LLM inference, PagedAttention, quantization.

3. Strubell et al. (2019), Energy and Policy Considerations for Deep Learning in NLP — arXiv:1906.02243.

4. Market Intelligence (Section 7): WEF Future of Jobs Report 2025, McKinsey State of AI 2025, Stanford HAI AI Index 2025/2026, LinkedIn Work Change Report, IMF SDN/2024/001, PwC AI Jobs Barometer 2025, Goldman Sachs, Anthropic Economic Index, ManpowerGroup 2026, Gartner, IDC — danh mục đầy đủ tại day15-career-market-research.md. Giảng viên (VinUni) AICB · Ngày 15 2026 41 / 41

---

<!-- chiron-source-span: {"source_span_id":"6d09619b-379f-5d65-bf94-a14eaf2a180d","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"f90978592269780ba63ba7af7c6b57322c477f6dddf9f0a02f95ca11ac725594"} -->

## Slide 54 - Hỏi & Đáp

15 ngày từ zero đến deployed AI product. Phase 2 bắt đầu hành trình chuyên sâu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"6606007b-b157-5d04-949d-0748ab559f9c","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"8ab86689be299fcecb2e4a82b65e3f4155afe94506c62896425c9e37c80edfe5"} -->

## Slide 55 - Cảm ơn!

Tên Giảng Viên Email: a.nguyen@vinuni.edu.vn Tài liệu: github.com/vinuni/aicb-materials Chúc mừng hoàn thành Phase 1!
