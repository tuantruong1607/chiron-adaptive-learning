---
schema_version: 1
course_id: rag-intensive
document_id: "645b7617-1187-58ba-a727-6f912dfea598"
document_version_id: "43ccc705-21ca-5ffe-b229-96bcc748a867"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Platform Engineering &"
source_file: "track 2 - day 28.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 28.pdf"
source_sha256: "b7c93f09f2b6bbe6dc3f4763b31e0d34aa5b0c069de7b887ab860c2e8407dcee"
parser_version: chiron-structured-markdown-v1
page_count: 22
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":22}"
language: vi
---

# Platform Engineering &

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"5a95a964-b0b8-54af-bd00-6064d229d7dc","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Platform Engineering &","extraction_method":"pdf-text-layer"},"checksum":"5be8b538f38de8dbbd918fe109fc596e4a76f9bde7a4cc12b59dc068a26fbd50"} -->

## Slide 1 - Platform Engineering &

Documentation AICB-P2T2 · Ngày 28 · Chương 6: Tổng Hợp Giảng viên VinUniversity Phase 2 · Track 2 · Tuần 6

---

<!-- chiron-source-span: {"source_span_id":"c2bc1b31-a913-58fb-aed0-4116e10ca6a2","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃY SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"0151d9babec9001c135537845dbd329b306676bababc1eb4f56879e88f4c0d62"} -->

## Slide 2 - HÃY SUY NGHĨ...

? “Từng piece hoạt động riêng lẻ — nhưng khi ghép lại thành platform, thách thức mới xuất hiện ở đâu? Milestone 3: Hôm nay team

```text
demo end-to-end AI platform — from data
```
ingestion to model serving với full observability.” Giữ câu hỏi này trong đầu khi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"e54b5fe0-6747-5f9e-a8a2-77de435b7ca2","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"7c18fe29771b51747830a7bf803222e7ea2a0b33a590264b968b92710749650b"} -->

## Slide 3 - Nội Dung Bài Học

1. CP2 Platform Architecture Review

2. Integration Patterns & Anti-patterns

3. End-to-End Request Flow

4. Integration T esting Strategy

5. Performance Profiling

6. Production Readiness Checklist

7. Milestone 3: Full Platform Demo

8. Labs: Platform Integration Sprint Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 1 / 17

---

<!-- chiron-source-span: {"source_span_id":"017dd799-d92b-5e41-bed4-8390d3a083bb","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu","extraction_method":"pdf-text-layer"},"checksum":"691ed280045d48a2df68f92717113ffb263ee446cb2ee6dfe9ecd620b36d66be"} -->

## Slide 4 - Mục Tiêu

### Sau buổi học này, bạn sẽ

1. Tích hợp toàn bộ infrastructure stack thành platform hoàn chỉnh

2. Demo end-to-end AI platform: data ingestion → model serving

3. Hoàn thành production readiness checklist cho platform

4. Present Milestone 3 demo cho instructors & peers Architecture review (30 min) → Integration workshop (90 min) → Demo & Labs (còn lại) Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 2 / 17

---

<!-- chiron-source-span: {"source_span_id":"d53b5f69-e895-55f8-ba96-3dfa8462776b","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"a8dec76aa468d493bc2bcbca5c4e67cbe0e08bfb5d9410603897b022f632ebac"} -->

## Slide 5 - Deliverable Cuối Ngày

```text
Full AI infrastructure platform demo — from data ingestion to model serving với full
```
observability

- End-to-end flow: ingest data → pipeline → model update → serving responds

- 5 smoke tests passing cho critical user journeys

- Production readiness checklist >80% complete

- Milestone 3 demo recording hoặc live presentation
Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 3 / 17

---

<!-- chiron-source-span: {"source_span_id":"19032111-60a5-5913-bdb3-0d510fa3aced","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"5 Layers of the AI Platform","extraction_method":"pdf-text-layer"},"checksum":"7ad15b62ff362c9726d1661191b6fd022c8bff36b591e39414ee90bda2365d8c"} -->

## Slide 6 - 5 Layers of the AI Platform

- Layer 5 — Governance: RBAC + PII pipeline + encryption + compliance automation

- Layer 4 — Ops: GitHub Actions CI/CD + LangSmith LLMOps + Prometheus/Grafana

- Layer 3 — ML: MLflow experiments + DVC versioning + Feature Store (Feast)

- Layer 2 — Data: Lakehouse (Delta Lake) + Airflow + Kafka + Vector Store

- Layer 1 — Compute: Kubernetes + GPU nodes + vLLM serving + auto-scaling
Key insight: Mỗi layer đã build riêng — hôm nay ghép lại thành platform hoàn chỉnh. Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 4 / 17

---

<!-- chiron-source-span: {"source_span_id":"fad6f48a-012e-5fa3-8de9-35e2037afe19","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Anti-patterns vs Patterns","extraction_method":"pdf-text-layer"},"checksum":"d06d4d9afeadb0ec0c05dca666c5adb26176d64dfa8b50bd36449a84c854d9a2"} -->

## Slide 7 - Anti-patterns vs Patterns

Anti-pattern Pattern Tool Tightly coupled components — fail- ure cascades Event-driven integration — Kafka decouples producers/consumers Kafka, Redis Streams Hardcoded config — connection strings in code GitOps — all config in Git, deployed via ArgoCD ArgoCD, Helm Shared mutable state — race condi- tions Immutable events + event sourcing — append-only log Kafka topics Manual deployment — “works on my machine” CI/CD pipeline — automated build, test, deploy GitHub Actions Failure cascading across services Bulkhead pattern — tách critical path (inference) khỏi non-critical (batch training) K8s namespaces, re- source quotas Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 5 / 17

---

<!-- chiron-source-span: {"source_span_id":"225a41c8-09e8-5dfd-982b-4661aeff4159","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Event-Driven Architecture cho AI Platform","extraction_method":"pdf-text-layer"},"checksum":"e758f49390b5dfd6283b6c422995247ffa2c58cb84a098e28b82aa6908ddfef1"} -->

## Slide 8 - Event-Driven Architecture cho AI Platform

- Producers: Data Ingestion, Airflow DAG, Model Training

- Kafka: data.raw, data.processed, model.events

- Consumers: Data Pipeline, Vector Store, Model Serving
Benefit: Producers và consumers hoàn toàn decoupled — add new consumer không impact existing pipeline. Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 6 / 17

---

<!-- chiron-source-span: {"source_span_id":"6418ece8-c1e2-50ad-a726-76f728a27a1c","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Anatomy of a Production AI Request","extraction_method":"pdf-text-layer"},"checksum":"8e9edf86588f07b310d7d2da9c011e87a0b6a18629047fa77da177626933f531"} -->

## Slide 9 - Anatomy of a Production AI Request

- User Request → API Gateway → Routing Layer → Agent Orchestrator

- Parallel calls: Feature Store (<5ms), Vector Search (<50ms), LLM Inference
(<500ms)

- Guardrails (PII check) → Response (total <1s)

- All calls traced: OpenT elemetry → Jaeger → LangSmith
Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 7 / 17

---

<!-- chiron-source-span: {"source_span_id":"c2d5fba0-8b93-561c-83c7-84cd37bf40f4","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Request Audit Trail","extraction_method":"pdf-text-layer"},"checksum":"043eebdee49478f3e93857c06d8809bf91cf50ff893a4be20d06f083fc784211"} -->

## Slide 10 - Request Audit Trail

- Input hash (privacy-safe)

- Output hash + response length

- End-to-end latency breakdown

- T oken cost per component

- Model version used

- API Gateway: 5ms

- Feature Store lookup: 5ms

- Vector search: 50ms

- LLM inference: 500ms

- Guardrails check: 20ms

- Total budget: 1000ms
Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 8 / 17

---

<!-- chiron-source-span: {"source_span_id":"0c6523a9-947c-5e01-b3ee-4e6a41197c6f","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Integration Testing cho AI Platform","extraction_method":"pdf-text-layer"},"checksum":"9f381d04d036f8308d7a506543a5a5ac6fd378fcdcfdc027ddbe633164d62117"} -->

## Slide 11 - Integration Testing cho AI Platform

- Ensure API contracts giữa services không bị
break

- Consumer-driven: consumers define
expected interface

- Run in CI — block merge nếu contract
violated

- Lightweight K8s: Kind or k3d

- All services running locally

- Seeded test datasets với known expected
outputs

- Testcontainers: spin up real Postgres,
Redis, Kafka trong Docker cho integration tests — thay vì mock

- Post-deploy test suite: 5 critical user journeys

- Fail fast trên production

- Run automatically after every deployment

- T est cảgolden path (happy flow) VÀ failure
path (error handling, timeout, retry)

- Inject latency between services

- Kill pods randomly

- Corrupt input data

- Verify graceful degradation
Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 9 / 17

---

<!-- chiron-source-span: {"source_span_id":"9313e9d5-a536-58fe-b455-758bebae9c4f","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Profiling Tools & Techniques","extraction_method":"pdf-text-layer"},"checksum":"b72faf60f85efb808f1310b47991cd882d891e757d989aea4d7b71356293d0dd"} -->

## Slide 12 - Profiling Tools & Techniques

Tool Target Khi nào dùng Jaeger (request waterfall) E2E latency breakdown Identify parallel vs sequential calls cProfile / py-spy CPU profiling Hot spots trong preprocessing tracemalloc Memory allocation Memory leaks trong long-running services EXPLAIN ANALYZE Database queries Slow queries, missing indexes tc (traffic control) Network latency Simulate high latency, test resilience

1. Jaeger trace → find bottleneck service 2. cProfile/py-spy → find hot function 3. Fix → re-profile → verify improve- ment Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 10 / 17

---

<!-- chiron-source-span: {"source_span_id":"995f0b24-b3e8-56d0-a336-89cd075af303","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Performance Profiling: Code Example","extraction_method":"pdf-text-layer"},"checksum":"762c5b7d88ba301d232fc9d6087bac682f124c74a48b23842cf22978c6481561"} -->

## Slide 13 - Performance Profiling: Code Example

### py-spy — Profile running process
# Attach to running process py-spy top --pid 12345 # Generate flamegraph py-spy record \ -o profile.svg \ --pid 12345

### tracemalloc — Memory tracking

```text
import tracemalloc
tracemalloc.start()
```
#... run code... snapshot = tracemalloc.take_snapshot() top = snapshot.statistics( 'lineno')

### for stat in top[:5]
print(stat)

- P50, P95, P99 latency per service

- Memory usage over time (leak?)

- CPU utilization per pod

- GPU utilization & memory

- Network I/O between services

- Synchronous DB calls in hot path

- Missing connection pooling

- Oversized model loading

- Unoptimized vector search
Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 11 / 17

---

<!-- chiron-source-span: {"source_span_id":"4ab88180-d0b3-5594-891c-3c0d84edf41b","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Production Readiness: 5 Pillars","extraction_method":"pdf-text-layer"},"checksum":"073cd8577e4e2b43f23980b59530095238283efd96da087731633f945f5966de"} -->

## Slide 14 - Production Readiness: 5 Pillars

- Reliability

- Observability

- Security

- Performance

- Operations
Rule: Checklist phải được automated — không rely vào human memory. CI pipeline check mỗi deploy. Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 12 / 17

---

<!-- chiron-source-span: {"source_span_id":"51cbccd7-ecb4-59c5-9bc4-b2914aa46b88","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Production Readiness Checklist Detail","extraction_method":"pdf-text-layer"},"checksum":"24276d8f233b0a6c68e86d84eaf9de5c441dc52af142047c1dc90bf8ae4dbed2"} -->

## Slide 15 - Production Readiness Checklist Detail

- Health checks (liveness + readiness)

- Circuit breakers configured

- Retries with exponential backoff

- Graceful shutdown handles in-flight

- Logs: structured JSON

- Metrics: Prometheus exported

- Traces: OpenT elemetry configured

- Alerts: P0/P1/P2 set

- Secrets in Vault/KMS

- RBAC configured per service

- PII pipeline handling

- Security scan passing

- Runbooks for top 5 incidents

- Backup/restore tested

- Disaster recovery plan

- Load tested at 2x peak
Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 13 / 17

---

<!-- chiron-source-span: {"source_span_id":"8907d688-b3c3-5648-a12e-65a4042cf824","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Milestone 3 Demo Requirements","extraction_method":"pdf-text-layer"},"checksum":"5722c813f3e2fca7ac4d5f60370720397e65306183e5940d1597ffa1b046fc3a"} -->

## Slide 16 - Milestone 3 Demo Requirements

End-to-end flow: ingest new data → pipeline runs → model updated → serving re- sponds

### Integration checklist: 10 integration points must work together

1. Data ingestion → Kafka

2. Kafka → Airflow pipeline

3. Pipeline → Delta Lake / Lakehouse

4. Lakehouse → Feature Store (Feast)

5. Data → Vector Store (embeddings)

6. MLflow → Model Registry

7. Model → vLLM/SGLang serving

8. Serving → API Gateway

9. All components → Prometheus/Grafana

10. All components → LangSmith tracing Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 14 / 17

---

<!-- chiron-source-span: {"source_span_id":"ecfea582-36ad-5279-8636-68112277c88e","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Milestone 3 Rubric","extraction_method":"pdf-text-layer"},"checksum":"c272efb52700286e81f548e7c6dc4e8e9f263c51df70440572f1a265ba2b3a1e"} -->

## Slide 17 - Milestone 3 Rubric

Criteria Weight Description Integration Completeness 40% All 10 integration points working, data flows end-to-end Observability 25% Logs, metrics, traces visible; alerts configured; SLO dashboard Performance 20% Latency within SLO; load tested; no memory leaks Architecture Quality 15% Clean separation, GitOps config, documented decisions Config drift between environments | Missing error handling at integration points | Incomplete monitoring coverage | No rollback strategy Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 15 / 17

---

<!-- chiron-source-span: {"source_span_id":"b54753c4-315a-57fb-8676-93a07c6b405a","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Team Presentation Format","extraction_method":"pdf-text-layer"},"checksum":"c75eec67151b98ff95abe86679457837dd053843111848ade5986d502cd77877"} -->

## Slide 18 - Team Presentation Format

1. Architecture overview (2 min)

2. Live demo: happy path (5 min)

3. Live demo: error scenario (3 min)

4. Observability walkthrough (3 min)

```text
5. Q&A from instructors/peers (2 min)
```

- Script the demo flow trước

- T est all happy paths AND key error scenarios

- Have fallback: pre-recorded video nếu live
fails

- Show Grafana dashboard real-time

- Highlight architectural decisions & trade-offs
Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 16 / 17

---

<!-- chiron-source-span: {"source_span_id":"02a26476-340e-5094-9196-cb789674d9d9","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Lab #28","extraction_method":"pdf-text-layer"},"checksum":"8332414523113469cf5db6205726de079c7c042b8f091adb2171d83e891427f4"} -->

## Slide 19 - Lab #28

Mục tiêu: Full Platform Integration Sprint Deliverable: Connect all components, write smoke tests, complete checklist, pre- pare demo Thời gian: 2h Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 17 / 17

---

<!-- chiron-source-span: {"source_span_id":"1940d54b-14ca-5f13-8f84-a60a60b5f4a8","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Tổng kết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"4e157d8477d7eaab0a93c68684a11129723c8aaa3a08950889c84ee4b0fb479b"} -->

## Slide 20 - Tổng kết — Key Takeaways

Những ý chính cần nhớ trước khi sang bài tiếp theo 1 Integration là nơi “works on my machine” meets reality — test integration surfaces trước khi production. 2 Production readiness checklist phải được automated — không rely vào human memory, CI pipeline check mỗi deploy. 3 Platform nghĩa là team khác dùng được — API contracts, documentation, SLAs quan trọng hơn internal code quality. Giảng viên (VinUni) AICB · Ngày 28 Tuần 6 17 / 17

---

<!-- chiron-source-span: {"source_span_id":"bc4102d1-c5ed-52a0-bb7e-faf09eee60d0","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"b3c9e3206ee757f39aad93d79bcae20a33010821238b577cce9f0ed4d4f4fbeb"} -->

## Slide 21 - Hỏi & Đáp

Câu hỏi nào về platform integration, pro- duction readiness, hay Milestone 3 demo?

---

<!-- chiron-source-span: {"source_span_id":"f7afc0db-4ce3-57df-b200-67bb32781a39","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"052063c57e2084cd7601002cbb99df50dcf9fd1e775c8a64eb470d479b436afa"} -->

## Slide 22 - Cảm ơn!

AICB-P2T2 · Ngày 28 Platform Engineering & Documentation lms.vinuni.edu.vn · Slide & template trên LMS
