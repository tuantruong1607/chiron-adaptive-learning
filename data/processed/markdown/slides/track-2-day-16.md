---
schema_version: 1
course_id: rag-intensive
document_id: "b31fa62f-1ee3-51f0-b4bc-14b319bcb104"
document_version_id: "53a298b2-b71c-58b9-ad8e-b0529e39b9c2"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Cloud Infrastructure for AI"
source_file: "track 2 - day 16.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 16.pdf"
source_sha256: "7aab4f87559ed70837d0fd79b260d0f912ec9247394fa95bad7e9e48ca93bd6d"
parser_version: chiron-structured-markdown-v1
page_count: 40
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":40}"
language: vi
---

# Cloud Infrastructure for AI

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"432d042b-8757-5236-aeb4-2783df843f7c","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Cloud Infrastructure for AI","extraction_method":"pdf-text-layer"},"checksum":"04f9e00c11b3ff83aca1b169072a08326741d27d3455e10c2953b7d7672ea556"} -->

## Slide 1 - Cloud Infrastructure for AI

AICB-P2T2 · Ngày 16 · Chương 4: Hạ Tầng Giảng viên Nguyễn Hải Dương · VinUniversity · Phase 2 · Track 2 · Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"2b3f7aef-9336-5ad8-b043-1ebc3618eb25","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"\"Ai đã từng deploy model lên cloud?","extraction_method":"pdf-text-layer"},"checksum":"e1d84a3a889d541e18099d4dbd1a9a16b598e7bbe52c7bef0a7b6d6eee05dcc5"} -->

## Slide 2 - "Ai đã từng deploy model lên cloud?

AWS? GCP? Azure? Local only? Case study: Startup burn $50K/tháng GPU vì không optimize — right-size + spot instances, giảm còn $12K. Cloud native hay on-premise — quyết định nào phù hợp với stack AI của bạn?" Giữ câu hỏi này trong đầu suốt buổi học hôm nay

---

<!-- chiron-source-span: {"source_span_id":"7c0bd6b7-a0c7-5b14-adbf-49e12370cf72","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung","extraction_method":"pdf-text-layer"},"checksum":"3710bfddef0648671932359ebd5dfee197091bcf3fdd1fdfb154dc8b814c6557"} -->

## Slide 3 - Nội Dung

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 1 So sánh Cloud Providers cho AI 2 Cloud Foundation (IaaS/PaaS/AI-aaS) 3 GPU Instance Types & Chi phí 4 Terraform IaC cho AI Stack 5 Docker → Kubernetes cho AI 6 Networking & Storage Strategy 7 Agent Infrastructure 8 Layers 8 AI Serving Stack (vLLM/SGLang) 9 Bức Tranh Cloud & AI Infra Toàn Cầu 2026

---

<!-- chiron-source-span: {"source_span_id":"68f0ca8b-860d-56a6-b66e-d8cfc8bfde30","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu Buổi Học","extraction_method":"pdf-text-layer"},"checksum":"b829e2f884b810170c98b2b08257ffb8b07846dd11efc03e6e177554b9ec23a7"} -->

## Slide 4 - Mục Tiêu Buổi Học

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

### Sau buổi học này, bạn sẽ có thể
1 Lựa chọn cloud provider phù hợp với AI workload cụ thể 2 Thiết kế GPU compute environment tối ưu chi phí 3 Triển khai container orchestration cho AI serving 4 Deploy AI endpoint production-ready trên cloud Cloud providers → GPU analysis → Terraform IaC → K8s → AI Serving Stack → Demo

---

<!-- chiron-source-span: {"source_span_id":"cf227da5-baa3-58c9-b8c3-c596b904ba5c","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"c7253e01ce884abc16cdff550388df347289557e93f4fcc3b88baf8f711e47e3"} -->

## Slide 5 - Deliverable Cuối Ngày

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Cloud AI environment running + cost estimate + agent endpoint live Cloud environment (AWS/GCP) đã setup với IAM least-privilege GPU instance deployed trong private VPC qua Terraform vLLM/SGLang endpoint chạy model inference thành công Cost dashboard screenshot + cost estimate document 1 2 3 4

---

<!-- chiron-source-span: {"source_span_id":"b3c20c45-2ed5-5332-ab93-ffb79464cf39","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"1 So Sánh Cloud Providers cho AI","extraction_method":"pdf-text-layer"},"checksum":"cdede965c92d66839bd7cc0cc243b6d7becfbdb541748b899063c33ed015a225"} -->

## Slide 6 - 1 So Sánh Cloud Providers cho AI

1. AWS vs GCP vs Azure: strengths, GPU flagships, và khi nào chọn

2. Vietnam cloud options: Viettel, VNG, FPT — data residency compliance

3. Specialized GPU clouds: Lambda, RunPod, CoreWeave — rẻ hơn 40-70%

4. Multi-cloud strategy & decision framework Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"c73acf92-99af-588c-88c4-6c4abf2d7426","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Cloud Providers cho AI Workloads","extraction_method":"pdf-text-layer"},"checksum":"f60e7966c0edb75cd81c987b4e2549e8a52aaa2c464cac53354a007c5e78998f"} -->

## Slide 7 - Cloud Providers cho AI Workloads

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Provider GPU Flagship Điểm Mạnh Khi Nào Chọn AWS P5 (H100 8x), P5e (H200) Ecosystem rộng nhất, Bedrock, SageMaker HyperPod Broadest ecosystem + enterprise compliance GCP A3 Mega (H100 8x), TPU v5p PyTorch/JAX, GKE GPU auto-provisioning, Vertex AI Heavy PyTorch training + TPU interest Azure ND H100 v5, ND H200 v5 OpenAI Service exclusive, Prompt Flow LLMOps Microsoft stack + OpenAI API VN Cloud T4/V100 (Viettel, VNG, FPT) Giá 60–70% global, data residency NĐ13 Compliance ND13, data residency Specialized H100/H200 (Lambda, RunPod) Rẻ hơn 40–70%, pure GPU, GMI Cloud $2.10/hr H100 Cost-sensitive + team có infra skills Chọn dựa trên: workload type × budget × compliance × latency requirements

---

<!-- chiron-source-span: {"source_span_id":"832e796e-7656-54a7-804f-42ea8b546043","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Decision Framework: Chọn Cloud Nào?","extraction_method":"pdf-text-layer"},"checksum":"19465ea4572ca7a12c9bc9a271ce6648aa3409e472a3355e4aa5dfb3d2d1a542"} -->

## Slide 8 - Decision Framework: Chọn Cloud Nào?

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Cần broadest ecosystem? Heavy PyTorch + TPU? OpenAI exclusive? VN data residency? AWS GCP Azure Viettel/ VNG/FPT Có✓ Không →✗ Có✓ Không →✗ Có✓ Không →✗ Có✓ Lưu ý: Nhiều tổ chức dùng multi-cloud — training ở provider A (GPU rẻ nhất), serving ở provider B (latency tốt nhất), data ở provider C (compliance). Cần abstraction layer (Terraform/Pulumi) để portable.

---

<!-- chiron-source-span: {"source_span_id":"08459bb3-e88b-5fa3-849a-b370d78b1344","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Vietnam Cloud & Specialized GPU Providers","extraction_method":"pdf-text-layer"},"checksum":"0c15e94ecbfae240820e3365e4b88633152adf5e6f28af3780afa0f12a5db7d9"} -->

## Slide 9 - Vietnam Cloud & Specialized GPU Providers

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Vietnam Cloud Options Viettel Cloud: GPU T4/V100, giá ~60-70% global VNG Cloud: đang build GPU capacity FPT Cloud: data residency compliance Ưu điểm: NĐ13/PDPD data residency Limitation: chưa có H100/H200, limited AZ Specialized GPU Clouds Lambda Cloud: H100 @ $2.49/hr GMI Cloud: H100 @ $2.10/hr (cheapest!) RunPod: H100 @ $3.35/hr CoreWeave: dedicated GPU clusters Rẻ hơn 40–70% vs hyperscalers Trade-offs & Khi Nào Dùng⚖️

- Phù hợp: cost-sensitive teams, pure GPU workloads, team có infra skills

- Hạn chế: ít managed services, tự manage hơn, ít availability zones

- Rule: Specialized cloud cho training (cost), hyperscaler cho serving (managed scale + SLA)

---

<!-- chiron-source-span: {"source_span_id":"5b1f15f7-4aec-5296-8ee2-a9ea021c6bd6","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"2 Cloud Foundation cho AI","extraction_method":"pdf-text-layer"},"checksum":"5349e32893354a1ccbc92462114f025049618840ee5e4634f860378b31f84f75"} -->

## Slide 10 - 2 Cloud Foundation cho AI

1. IaaS / PaaS / AI-aaS: phân biệt và khi nào dùng gì

2. Cloud-Native vs Cloud-Hosted: hybrid approach cho AI

3. Shared Responsibility Model trong AI context

4. Landing Zone: account structure, networking, guardrails Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"fe96cfc9-2817-537b-b869-afb0754133a7","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Mô Hình Cloud cho AI Workloads","extraction_method":"pdf-text-layer"},"checksum":"aec6d6a4b1f3744bb6e244d136b57610a63142ea956464b2517decdd408283f4"} -->

## Slide 11 - Mô Hình Cloud cho AI Workloads

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 AI-aaS OpenAI API / Bedrock / Vertex AI (pay-per-token) Nhanh nhất, không cần infra PaaS SageMaker / Azure ML / AI Platform (managed training + serving) Managed scaling, ít ops IaaS EC2 GPU / GCE / Azure VM (full control, self-manage) Full GPU control, cần ops Physical On-premise / Colocation (max control, max effort) Max control, max effort AI thường hybrid: Training dùng IaaS (GPU control) → Serving dùng PaaS (managed scaling) → Prototype dùng AI-aaS (nhanh nhất)💡

---

<!-- chiron-source-span: {"source_span_id":"f88c0cdd-b9ae-5e58-8ef5-d1113153ef39","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Shared Responsibility & Landing Zone","extraction_method":"pdf-text-layer"},"checksum":"ec43f7cad98e5f57801457b045c018cf19fa5a48ffb4232290074919d9690373"} -->

## Slide 12 - Shared Responsibility & Landing Zone

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Cloud Provider chịu trách nhiệm Physical infrastructure + hypervisor Network backbone & DDoS protection Hardware maintenance & availability Team bạn chịu trách nhiệm Model security + data encryption Access control (IAM least-privilege) Prompt injection prevention Data privacy compliance (NĐ13, GDPR) Landing Zone — Setup đúng từ đầu (rework cost 10x!) Account structure: workload accounts, shared services, security account Networking: Transit Gateway hub-spoke topology, private subnets cho GPU Centralized logging: CloudTrail + CloudWatch aggregation Guardrails: SCPs (Service Control Policies) — enforce security baseline

---

<!-- chiron-source-span: {"source_span_id":"18288225-95b1-563a-9624-4666d72c14d3","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"3 GPU Instance Types & Chi Phí","extraction_method":"pdf-text-layer"},"checksum":"b2380275186bbe4b90402e6c68c13a823b52ee532c68eaed0ab1c32e46c4718a"} -->

## Slide 13 - 3 GPU Instance Types & Chi Phí

1. GPU pricing 2026: T4, L40S, A100, H100, H200, B200

2. GPU Selection Decision Tree theo task + model size

3. MIG (Multi-Instance GPU) — maximize utilization

4. Cost strategy: Spot/Preemptible vs Reserved vs On-demand Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"063b1b46-a46c-5ee5-b3b8-01452327db2d","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"GPU Pricing 2026 & So Sánh","extraction_method":"pdf-text-layer"},"checksum":"8426ca1d281b9c34065d2546facfde75a04bd57af9448dc149688e798f47e310"} -->

## Slide 14 - GPU Pricing 2026 & So Sánh

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 GPU VRAM Giá/hr Bandwidth Use Case T4 16 GB $0.35 320 GB/s Inference nhỏ (≤7B) L40S 48 GB $0.40–0.86 864 GB/s Inference vừa — sleeper pick! A10G 24 GB $1.00 600 GB/s Inference production A100 80 GB $1.79–2.70 2 TB/s Fine-tuning (giảm từ $3.0) H100 80 GB HBM3 $2.99–4.31 3.35 TB/s Pre-training (giảm từ $8.0!) H200 141 GB HBM3e $3.72–5.58 4.8 TB/s LLM 70B single GPU B200 192 GB HBM3e $6.84–8.64 8 TB/s Ultra-scale, limited avail. Rule of thumb: inference → T4/L40S/A10G | fine-tuning → A100 | pre-training → H100 cluster

---

<!-- chiron-source-span: {"source_span_id":"6ef7f1f7-e34e-5d7c-953c-f098d68c8d19","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"GPU Selection Decision Tree","extraction_method":"pdf-text-layer"},"checksum":"f12910ff498c76f8dd757a5d50eb7a6c18ffdee063f59c59243f5d38df7162d8"} -->

## Slide 15 - GPU Selection Decision Tree

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Tác vụ? Inference Fine-tune Pre-train ≤13B L40S / T4 $0.35–0.86/hr 13B–70B A100 / H100 $1.79–4.31/hr 70B+ H200 $3.72–5.58/hr A100 / H100 $1.79–4.31/hr H100 / H200 Cluster (8× nodes) Cost Strategy: Spot/Preemptible (tiết kiệm 60–70%) cho training jobs (interruptible). Reserved 1-year (giảm 40%) cho serving ổn định. Ví dụ thực tế: GPT-2 1B token fine-tune → A100 on-demand=$45 | Spot=$14 | Reserved=$27

---

<!-- chiron-source-span: {"source_span_id":"b520cf7d-fc17-5bf7-985d-5b036b48929b","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"GPU Instance Families — Dùng Dòng Nào?","extraction_method":"pdf-text-layer"},"checksum":"d7e87da9d0fb4b2326f8ecd91a8fbb6467593f85c7afcea88fee32f234c9062a"} -->

## Slide 16 - GPU Instance Families — Dùng Dòng Nào?

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Family GPU Khi Nào Dùng? Tác Vụ AI AWS P5 / P5e H100 8x / H200 Multi-GPU training cluster Pre-train, large fine-tune AWS G5 A10G Inference production Serving ≤13B models GCP A3 Mega H100 8x Distributed training PyTorch DDP, DeepSpeed GCP A3 Ultra H200 Memory-intensive training 70B+ single-node GCP TPU v5p TPU v5p JAX/XLA large-scale training Massive-scale pre-train Azure ND H100 H100 OpenAI fine-tuning Azure ML pipelines Azure ND H200 H200 High-memory inference Large model serving Karpenter (AWS): auto-provision đúng GPU type theo pod request | NAP (GCP): smarter Cluster Autoscaler | Scale-to-zero ngoài giờ: tiết kiệm 60%+ GPU idle ⚡ cost

---

<!-- chiron-source-span: {"source_span_id":"6c53a369-d5ed-5490-9bac-f460b3a56a4e","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"MIG, L40S & B200 — Advanced GPU Insights","extraction_method":"pdf-text-layer"},"checksum":"ffc32c22c61e31a8db062e4b6c7642864c91e3216a8adf5a4b03de482fedd02c"} -->

## Slide 17 - MIG, L40S & B200 — Advanced GPU Insights

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 MIG (Multi-Instance GPU) A100/H100 chia tối đa 7 instances 1× A100 80GB → 7× 10GB instances Isolated cho small model inference Maximize utilization, serve nhiều models Dùng khi: nhiều small models song song L40S — Sleeper Pick 48GB VRAM, Ada Lovelace arch FP8 Transformer Engine support Giá: $0.40–0.86/hr (3–5× rẻ hơn H100) Throughput competitive cho ≤48GB models Ideal: production inference small/medium B200 Blackwell (2026) 192GB HBM3e, 8 TB/s bandwidth Native FP4 support (mới) 11–15× inference vs H100 (promise) Giá: $6.84–8.64/hr (ramp-up 2026) Early adopter premium, stabilize ~20-30% trên H200 Reserved vs Spot — Decision Framework < 6 tháng → Spot/On-demand (linh hoạt, no commitment) 6–12 tháng → 1-year Reserved: tiết kiệm 30–40% > 12 tháng → 3-year Reserved: tiết kiệm 50–60% Training (interruptible) → Spot | Serving (stability needed) → Reserved | ROI dương sau ~6 tháng

---

<!-- chiron-source-span: {"source_span_id":"e8849d16-6647-5a5e-8331-50aca43ace62","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"4 Terraform Infrastructure-as-Code AI","extraction_method":"pdf-text-layer"},"checksum":"c23e24e7c602a2d40eb0918d608f88ba33e1973f43921ac33cd0fe0afb47f71b"} -->

## Slide 18 - 4 Terraform Infrastructure-as-Code AI

1. Terraform modules cho GPU instances, VPC, security groups

2. State management: S3 backend + DynamoDB lock

3. Workspaces: dev / staging / prod isolation

4. Alternatives: Pulumi (Python/TS), OpenTofu, AWS CDK Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"603113dd-1955-5ce8-a1d7-f573b6e61fb6","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Terraform cho AI Stack","extraction_method":"pdf-text-layer"},"checksum":"37732cf2878cf618402d0b925fc93d91c5cf0e281360f0362975d6c2f4a6f6cc"} -->

## Slide 19 - Terraform cho AI Stack

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

```text
resource "aws_instance" "gpu" {
instance_type = "g5.xlarge"
ami = "ami-nvidia-cuda-12"
root_block_device {
volume_size = 200
volume_type = "gp3"
}
tags = { Name = "ai-inference" }
}
```
Infrastructure Setup VPC: private subnet cho GPU, public cho LB Security groups: 8080 (API), 6443 (K8s), 22 (SSH jump) S3 backend + DynamoDB lock (team env) Workspaces: dev / staging / prod Alternatives to Terraform Pulumi: Python/TypeScript native — popular với AI teams OpenTofu: open-source fork (post HashiCorp BSL 2023) AWS CDK: nếu pure AWS + TypeScript team Tip: Dùng modules để reuse, workspaces để isolate

---

<!-- chiron-source-span: {"source_span_id":"797a7224-d504-56c3-9a19-707df0d84e79","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Container Orchestration: Docker →","extraction_method":"pdf-text-layer"},"checksum":"72801a0e7c7350cb328426a76e4d177f67ad9191cd12d758bce06d760f901461"} -->

## Slide 20 - Container Orchestration: Docker →

5 Kubernetes

1. Docker image optimization: multi-stage build 18GB → 6–8GB

2. NVIDIA GPU Operator: tự động install drivers + toolkit

3. Karpenter (AWS) / NAP (GCP): smart GPU node provisioning

4. Init containers, namespaces, resource limits cho ML teams Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"39954fd6-d7e1-5f61-86e8-318ad4afc866","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Kubernetes Architecture cho AI Serving","extraction_method":"pdf-text-layer"},"checksum":"5bfdcaf35b2bcecf9784c6ef7841225791aaa31d01e55b851f5ddabf8d731f81"} -->

## Slide 21 - Kubernetes Architecture cho AI Serving

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Ingress / ALB K8s Cluster vLLM Pod GPU: 1 A10G vLLM Pod GPU: 1 A10G SGLang Pod GPU: 1 H100 HPA GPU metrics GPU Operator (NVIDIA) Karpenter Auto-provision S3 Model Weights (Init container pre-download)

---

<!-- chiron-source-span: {"source_span_id":"e97f18d7-b86e-5db3-a7f3-25de3df9e223","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Docker & K8s Best Practices cho AI","extraction_method":"pdf-text-layer"},"checksum":"7d519c2eaceddf581ecf61d0443e4ab32f74bfec27bc2f137538b5a4901490e4"} -->

## Slide 22 - Docker & K8s Best Practices cho AI

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Docker Image Optimization Base: nvcr.io/nvidia/cuda:12.1-runtime Multi-stage build: 18GB → 6–8GB

```text
Cache pip layer riêng (trước COPY source)
```
.dockerignore: exclude datasets, checkpoints Result: cold start time giảm đáng kể Kubernetes GPU Config nvidia.com/gpu: 1 — requests = limits (always!) GPU Operator: auto install drivers, toolkit, plugin Init container: pre-download weights từ S3 Karpenter (AWS) / NAP (GCP): smart provisioning Scale-to-zero ngoài giờ cao điểm K8s Namespaces cho ML Teams — Best Practice ml-training/ — separate resource quotas, cost tracking ml-serving/ — separate RBAC, production isolation ml-experiments/ — sandbox, no strict limits NEVER overcommit GPU: fractional sharing phức tạp, dùng MIG thay vì overcommit⚠️

---

<!-- chiron-source-span: {"source_span_id":"5a114426-5a3a-5168-9f39-b92ff881f0eb","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"6 Networking & Storage Strategy","extraction_method":"pdf-text-layer"},"checksum":"00731ff9617a10cd2aa2232a9a304a6f021d99997fc0744256c2b3a23dcf3d14"} -->

## Slide 23 - 6 Networking & Storage Strategy

1. API Gateway patterns: rate limiting, streaming, timeout tuning

2. Service Mesh (Istio/Linkerd): mTLS, canary routing, tracing

3. GPU-to-GPU networking: NVLink 900 GB/s, InfiniBand 400 Gbps

4. Storage tiering: Hot (Redis) → Warm (S3) → Cold → Archive Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"3be0d323-05d8-5444-84d6-fc081f56c5bb","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Networking cho AI Workloads","extraction_method":"pdf-text-layer"},"checksum":"116e9cf9d8f2e4b08589fd638803e452f443d8518e1ce8f151853ec4b5e15814"} -->

## Slide 24 - Networking cho AI Workloads

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Client API Gateway (Rate limit / Queue / SSE streaming) ALB / Ingress Service Mesh (Istio / Linkerd) Inference mTLS Orchestrator mTLS Vector DB mTLS GPU-to-GPU: NVLink 900 GB/s intra-node | InfiniBand 400 Gbps inter-node (multi-node training) | EFA (AWS) alternative⚡ VPC Endpoints (PrivateLink): tránh traffic đi internet — bảo mật + tiết kiệm egress cost🔒

---

<!-- chiron-source-span: {"source_span_id":"f3725fb8-9466-596f-b65e-d767e4242119","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Storage Strategy cho AI Systems","extraction_method":"pdf-text-layer"},"checksum":"efd00d28ab564f5ed17686ae93296bff828895c3d09de51e580ff3d0d7a7c992"} -->

## Slide 25 - Storage Strategy cho AI Systems

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Hot Redis / GPU Memory sub-ms latency Active KV cache, embedding cache, session state Warm S3 Standard / EBS $0.023/GB/mo Model weights, recent checkpoints, training data Cool S3 Infrequent Access $0.0125/GB/mo Old checkpoints, infrequent datasets Archive S3 Glacier Deep Archive $0.00099/GB Compliance data, model archaeology Storage Best Practices💡 S3 versioning cho model artifacts | Lifecycle policies: auto-archive sau 90 ngày | S3 Intelligent-Tiering cho mixed patterns

---

<!-- chiron-source-span: {"source_span_id":"d1fe94ef-2f5b-5074-a6ab-3e813e22dc2b","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Agent Infrastructure: 8 Production","extraction_method":"pdf-text-layer"},"checksum":"52016ee801684d512e7ac98d55c66b959c48aa4cd42d91d98c6a1820e777ba7f"} -->

## Slide 26 - Agent Infrastructure: 8 Production

7 Layers

1. Compute: GPU cho LLM inference, CPU cho orchestration, Serverless cho tools

2. Message Queue: Redis Streams vs Kafka vs RabbitMQ

3. Cache: L1 in-process LRU → L2 Redis → L3 Embedding cache

4. Observability: OpenTelemetry, LangSmith, Prometheus KPIs Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"b7682b2f-5166-5e72-b28a-bb127fd9285f","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"8 Layers của Production AI Agent","extraction_method":"pdf-text-layer"},"checksum":"dbe540072a7a9ac96551e3f91e7b68eba594f4d2c8fc1c6cfd511f01db2fadc3"} -->

## Slide 27 - 8 Layers của Production AI Agent

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 8 Secrets & Config Vault / AWS Secrets Manager, Feature flags cho A/B testing 7 Observability OpenTelemetry → Jaeger traces, LangSmith, Prometheus KPIs 6 Networking API Gateway, gRPC internal (high perf), HTTP+SSE (MCP transport) 5 Storage PostgreSQL (conv history), pgvector (long-term), Redis (short-term TTL), S3 (tool outputs) 4 Cache L1 in-process LRU dict | L2 Redis shared (TTL) | L3 Embedding cache 3 Message Queue Redis Streams (low latency) | Kafka (high throughput, replay) | RabbitMQ 2 Orchestration LangGraph / CrewAI / AutoGen on CPU pods — manages lifecycle & retry 1 Compute GPU (LLM inference agents) + CPU (orchestrator) + Serverless (tool-calling) Design principle: Stateless agents (externalize state → Redis/Postgres) cho horizontal scaling

---

<!-- chiron-source-span: {"source_span_id":"b401fcbd-5123-5656-ae27-bc3c415199eb","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Agent Infra: Chi Tiết Chọn Công Nghệ","extraction_method":"pdf-text-layer"},"checksum":"2651943f1cf67cf51f4cb7e098441cf3a897883a0dd93ae3b200271004512e5f"} -->

## Slide 28 - Agent Infra: Chi Tiết Chọn Công Nghệ

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Compute Pattern GPU chỉ cho agents chạy LLM — orchestrator không cần GPU Pattern: supervisor agent (CPU) dispatches → specialist agent (GPU) Serverless (Lambda) cho lightweight tool-calling agents Message Queue So Sánh Redis Streams: low latency (<1ms), simple setup — best for most cases Kafka: high throughput, durability, replay — large-scale agents RabbitMQ: complex routing rules, dead letter queues Cache — Multi-Level L1: in-process LRU dict (fastest, per-instance) L2: Redis shared across agents (TTL-based) L3: Embedding cache (avoid re-embed same queries) Target: 60–80% cache hit rate → giảm LLM API calls Observability Stack OpenTelemetry → Jaeger: distributed traces across agents LangSmith / Weave: LLM-specific tracing & eval Prometheus KPIs: tasks/min, error rate, avg latency, cost/request HashiCorp Vault / Secrets Manager: API keys, credentials

---

<!-- chiron-source-span: {"source_span_id":"c21b78f7-2497-596e-a395-6f74b88b6d17","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"8 AI Serving Stack: vLLM, SGLang & More","extraction_method":"pdf-text-layer"},"checksum":"7492c5271092462f66bdbc6bba8a1c81ab21db59ccbe180696c247cfffa718ba"} -->

## Slide 29 - 8 AI Serving Stack: vLLM, SGLang & More

1. 6 serving engines 2026: vLLM, SGLang, LMDeploy, TensorRT-LLM, TGI, Ollama

2. SGLang RadixAttention: KV cache reuse — multi-turn gain 10–20%

3. LMDeploy TurboMind: 1.8× throughput vs vLLM (C++ zero overhead)

4. Deploy tips: GPU memory 80% safe zone, continuous batching always on Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"c12f6508-d8ff-5a86-879b-388ee8596ba8","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"6 Serving Engines 2026 — So Sánh","extraction_method":"pdf-text-layer"},"checksum":"86be836742ad4dd1d5c70cd863d0debdec4b83ebaa9c4d1f5b81784104d09984"} -->

## Slide 30 - 6 Serving Engines 2026 — So Sánh

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Engine Kỹ Thuật Chính Ưu Điểm Best For vLLM PagedAttention Ecosystem rộng nhất, OpenAI-compatible API Broad compatibility, easy deploy SGLang RadixAttention + Prefill-Decode disaggregation Multi-turn +20%, JSON 3× faster, 400K+ GPUs globally Agents + multi-turn chat + structured output LMDeploy TurboMind engine (C++) — zero Python overhead 1.8× throughput vs vLLM, Int4 2.4× faster Quantized models, latency- sensitive apps TensorRT-LLM NVIDIA optimized kernels 30–50% faster cho high concurrency Ultra-scale production (Perplexity- level) TGI HuggingFace native Quick deploy, Prometheus built-in Prototype nhanh, HF model ecosystem Ollama llama.cpp backend CLI + local dev, easy model switching Edge / laptop inference / development 2026 update: SGLang & LMDeploy đã vượt vLLM ~29% raw throughput cho nhiều use cases

---

<!-- chiron-source-span: {"source_span_id":"2a3ff3ff-d3b6-54c1-8cfe-e9d5af085719","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"SGLang & LMDeploy — Deep Dive 2026","extraction_method":"pdf-text-layer"},"checksum":"207d3d1edbf1ce5d0b7f2384fdba97de18bef6abb18eef77c8a9b1c6e0dce756"} -->

## Slide 31 - SGLang & LMDeploy — Deep Dive 2026

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 SGLang — RadixAttention🔷 Powers 400,000+ GPUs globally (xAI Grok 3, Azure DeepSeek R1) RadixAttention: reuse KV cache across requests có chung prefix Multi-turn gain thêm 10–20% nhờ cache hits Compressed FSM: JSON output 3× faster vs naive Prefill-Decode Disaggregation: tách GPU roles v0.4: zero-overhead batch scheduler (<2% CPU) LMDeploy — TurboMind Engine🔶 TurboMind viết hoàn toàn bằng C++ — zero Python overhead Persistent batch inference + blocked KV cache 1.8× request throughput vs vLLM baseline Int4 inference: 2.4× faster than FP16 Best: quantized model deployment Ideal: latency-sensitive production apps Practical Deploy Tips (áp dụng cho mọi engine)⚙️ GPU memory utilization 80% là safe zone — 95% gây CUDA OOM khi graph compilation Continuous batching LUÔN bật — max_model_len tune theo actual usage (đừng set 128K nếu 99% requests <4K) Health checks: /health endpoint, /v1/models verify model loaded, readiness probe 60s initial delay

---

<!-- chiron-source-span: {"source_span_id":"9713ea8f-0deb-516a-a4de-877280dae98f","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Deploy vLLM / SGLang / TGI","extraction_method":"pdf-text-layer"},"checksum":"40407da20dc7c78b82fc2a78f6bcb43520f22009dd7b65dda24973ff37e7d033"} -->

## Slide 32 - Deploy vLLM / SGLang / TGI

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

### vLLM — PagedAttention
python -m vllm.entrypoints\ .openai.api_server \ --model meta-llama/Llama-3-8B \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.80

### SGLang — RadixAttention + JSON
python -m sglang.launch_server \ --model-path MODEL_PATH \ --port 30000 \ --tp 1 Practical Tips & Health Checks✅ GPU memory utilization 80% = safe zone (95% = CUDA OOM) Continuous batching LUÔN bật | max_model_len tune theo actual usage Health: GET /health | GET /v1/models | Readiness probe: initialDelaySeconds: 60 Compare TTFT: SGLang thường thấp hơn vLLM trong multi-turn nhờ RadixAttention cache hits

---

<!-- chiron-source-span: {"source_span_id":"b17f0bb2-13ee-5150-91fb-2ea3d969b2f0","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Bức Tranh Cloud & AI Infra Toàn Cầu","extraction_method":"pdf-text-layer"},"checksum":"fe53b8f967e96a4760aa40c492802dd6728574e97275dcd81d7465d6bfec14e5"} -->

## Slide 33 - Bức Tranh Cloud & AI Infra Toàn Cầu

9 2026

1. Cloud market 2026: quy mô, doanh thu, thị phần AWS/Azure/GCP/Neocloud

2. Bigtech capex race: $725B — ai đang đổ tiền vào đâu

3. Ai thuê cloud gì, ai tự host: OpenAI, Anthropic, Google, Meta, xAI

4. Hot trends: custom silicon, GPU-as-currency, power bottleneck, VN ở đâu Giảng viên (VinUni) AICB · Ngày 16 Tuần 4

---

<!-- chiron-source-span: {"source_span_id":"28f05ab4-3c6e-5256-9398-09709780124d","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Cloud Market 2026: Quy Mô & Doanh Thu","extraction_method":"pdf-text-layer"},"checksum":"f650612ef1e596c19a28a18fc89ce9bfdf5cf6945aa8a6a9a5a14e0be2ec81e3"} -->

## Slide 34 - Cloud Market 2026: Quy Mô & Doanh Thu

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Nhóm Số Liệu 2026 Tăng Trưởng Ghi Chú AWS 28% thị phần cloud +19% YoY Dẫn đầu tuyệt đối nhưng tăng chậm nhất Azure 22% thị phần cloud +40% YoY Được đẩy bởi nhu cầu compute của OpenAI Google Cloud 15% thị phần, $24.8B/quý +82% YoY (đỉnh) TPU tự chủ giúp biên lợi nhuận tốt hơn Neocloud (CoreWeave, Lambda...) ~$20B doanh thu 2026 Backlog CoreWeave $66.8B Dự phóng đạt $180B vào 2030 Bigtech Capex (MSFT+GOOGL+A MZN+META) $725B trong 2026 +77% YoY (từ $410B) Chu kỳ đầu tư lớn nhất lịch sử doanh nghiệp Tổng doanh thu cloud infra Q2/2026: $142B (+43% YoY) | AI chiếm 19% tổng chi tiêu cloud, tăng từ 8% (2023)

---

<!-- chiron-source-span: {"source_span_id":"3b18d008-fa5e-566f-a968-00191f8a0337","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Ai Thuê Cloud Gì, Ai Tự Host?","extraction_method":"pdf-text-layer"},"checksum":"db3b87e7fa714e3658ebf58b14a2623f79473af497ab76dfbf28a44ca8d29aee"} -->

## Slide 35 - Ai Thuê Cloud Gì, Ai Tự Host?

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Người Thuê Compute (Buyers) OpenAI: chủ yếu Microsoft Azure ($17.2B chi phí 2025) + Oracle Stargate JV: ~$400B, kế hoạch 7GW Anthropic: đa nền tảng, không phụ thuộc 1 vendor AWS Trainium (Project Rainier): tới 5GW, cam kết $100B/10 năm Google TPU: tới 1M chip, mở rộng 3.5GW (Broadcom, 2027+) Người Tự Host / Bán Compute Google: tự dùng TPU Ironwood (TPUv7) là chính + bán/cho thuê ra ngoài: Anthropic, Meta, xAI, SSI Meta: tự host + chip MTIA riêng + vẫn mua GPU Nvidia và mới thuê thêm TPU Google xAI: tự xây Colossus (~770K GPU, ~1-2GW, $18B) Câu Chuyện Nổi Bật 2026🔥

- Anthropic thuê nguyên Colossus 1 của xAI: 220,000 GPU + 300MW, deal 4 năm ký 5/2026

- ~$1.25 tỷ/tháng (~$5-6 tỷ/năm) — trước đó Colossus 1 chỉ chạy ở 11% công suất

- Hai đối thủ trực tiếp trên thị trường LLM giờ là khách hàng compute của nhau — utilization > sở hữu

---

<!-- chiron-source-span: {"source_span_id":"0ba9ef59-72b9-5989-a5da-b5edf280f2e2","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Hot Trends 2026 — Định Hình Ngành AI Infra","extraction_method":"pdf-text-layer"},"checksum":"33bf06814b9508569067a175e37a1d9ae475693c91629dec74ae70ba6e069785"} -->

## Slide 36 - Hot Trends 2026 — Định Hình Ngành AI Infra

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 4 xu hướng lớn nhất định hình cuộc chơi AI infra năm 2026 1 Multi-cloud/multi-silicon là chuẩn mới — không AI lab lớn nào phụ thuộc 1 vendor 2 Custom silicon đấu Nvidia — Google TPU, AWS Trainium, Meta MTIA tăng tốc 3 "GPU-as-currency" — đối thủ thuê chéo compute nhau khi dư utilization (Anthropic ↔ xAI) 4 Power là nút thắt mới, không phải chip — đất/điện/làm mát khan hiếm hơn GPU VN cloud (Viettel/VNG/FPT) vẫn ở quy mô MW, GPU T4/V100 — chơi ngách compliance/data residency, chưa cạnh tranh scale GW của bigtech

---

<!-- chiron-source-span: {"source_span_id":"df8248bf-5ce5-5309-b323-75982901e65a","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Tổng Kết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"cadd4180eee44735a79ce7a702967245c6c6980c9857d407eac22392d561edbb"} -->

## Slide 37 - Tổng Kết — Key Takeaways

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Những ý chính cần nhớ sau buổi học hôm nay 1 Cloud provider choice phụ thuộc workload type — không có "best", chỉ có "best fit". AWS (ecosystem), GCP (PyTorch/TPU), Azure (OpenAI), VN cloud (compliance). 2 H200 (141GB HBM3e) là new standard 2026. Terraform/Pulumi + Helm = reproducible infra. Tránh "works on my machine" syndrome — mọi thứ as code. 3 Serving stack 2026: vLLM, SGLang, LMDeploy, TensorRT-LLM, Ollama — chọn theo use case. SGLang cho agents/multi- turn, LMDeploy cho max throughput.

---

<!-- chiron-source-span: {"source_span_id":"16e1d43c-80a4-54e2-b3bb-9e197c3ed612","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Tiếp Theo & Bài Tập","extraction_method":"pdf-text-layer"},"checksum":"46028d432afe0448049b1e920396758a62a8078b23272ab283978ac3aac85d43"} -->

## Slide 38 - Tiếp Theo & Bài Tập

Giảng viên (VinUni) AICB · Ngày 16 Tuần 4 Ngày 17: Data Pipeline Engineering "Airflow DAGs, Kafka streaming, ETL/ELT cho AI data — xây pipeline không để data bẩn phá model" Bài Tập & Chuẩn Bị📋 Hoàn thành Lab 16: Cloud AI Environment Setup✅ Cài đặt Docker Compose cho Airflow (pre-lab N17)✅ Đọc trước: Apache Airflow TaskFlow API docs📖 lms.vinuni.edu.vn → Slide & templates trên LMS🔗 Agenda gợi ý N17: Airflow fundamentals (60') → Kafka streaming (45') → ETL/ELT patterns (45') → Lab⏱️

---

<!-- chiron-source-span: {"source_span_id":"0d67b248-ea80-5af7-85de-f8840e5db6c8","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"c94c85a4d3fc01f6d305f825d35d749736f10698a649fc4fb35e3517bd5194dc"} -->

## Slide 39 - Hỏi & Đáp

? Câu hỏi nào về cloud providers, GPU selection, Kubernetes, hay AI serving stack?

---

<!-- chiron-source-span: {"source_span_id":"437fb637-fb77-5c22-b279-3d1dcb1c13fb","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"4622766f1d09c01b4c6742f7c94b4305a71573e5c8859d9053a469b2e778398e"} -->

## Slide 40 - Cảm ơn!

AICB-P2T2 · Ngày 16 · Cloud Infrastructure for AI
