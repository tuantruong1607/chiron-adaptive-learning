---
schema_version: 1
course_id: rag-intensive
document_id: "34304375-e980-57d3-96f2-f5a68f6c6692"
document_version_id: "ef98b9b8-b9a7-55a9-984c-c39c63279a11"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "GPU FinOps &"
source_file: "track 2 - day 25.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 25.pdf"
source_sha256: "9a7f3cf779cd463d367404eeed7c3fea690261ab82f1e0ac1202c109d7eadc17"
parser_version: chiron-structured-markdown-v1
page_count: 25
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":25}"
language: vi
---

# GPU FinOps &

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"bba12a60-5ae4-5884-a19d-2997d3299f92","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"GPU FinOps &","extraction_method":"pdf-text-layer"},"checksum":"dbb4f1991dd8c9abd8743192a55de281890cdc9dd914f3ae151464114cf37b16"} -->

## Slide 1 - GPU FinOps &

Cost Optimization AICB-P2T2 · Ngày 25 · Chương 5: Vận Hành Giảng viên VinUniversity · Phase 2 · Track2 ·Tuần5

---

<!-- chiron-source-span: {"source_span_id":"77f87448-2afd-540e-bb84-4eb69a7500a8","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃY SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"c2f9264bc4b80c69db12a250914401ecde9ae458187edc63f328edbfbe2ea480"} -->

## Slide 2 - HÃY SUY NGHĨ...

? “Bạn đang tiêu bao nhiêu cho GPU mỗi ngày?

### Và bao nhiêu% là lãng phí?Case study
4x A100 idle overnight (12h) = $144 wast- ed/day = $52,560/year. Hôm nay chúng ta học cách cắt giảm 40–60% chi phí GPU — và close Chương 5 với Quiz + Milestone 2.” Giữcâu hỏi này trong đầu khihọc bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"016b5cd4-7766-5074-a10c-a2fd68353927","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội Dung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"0a4b5111e3990446544eec29b1a79f0aa9e3369b4c87a8e00b15a91c8b360564"} -->

## Slide 3 - Nội Dung Bài Học

1. GPUCloud Cost Anatomy

2. Spot& Preemptible Instances

3. Right-Sizing& Utilization

4. InferenceCost Optimization

5. CostAllocation & Chargeback

6. SustainableAI: Carbon & Energy

7. TổngKết Chương 5

8. Quiz + Milestone 2 Giảngviên (VinUni) AICB· Ngày 25 Tuần5 1 / 20

---

<!-- chiron-source-span: {"source_span_id":"6b83f29a-3741-5e56-b77a-36efb66aacf3","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục Tiêu","extraction_method":"pdf-text-layer"},"checksum":"26642373bea04f9e22d545a05bc0a1def00aab8abc839d0d5ecccfabdad75101"} -->

## Slide 4 - Mục Tiêu

### Saubuổi học này,bạnsẽ

1. Phântích chi phí GPU cloud vàphát hiện lãng phí

2. Ápdụng spot/preemptible instances với checkpoint strategy

3. Tốiưu training cost bằng mixed precision(AMP) và autoscaling

4. Tốiưu inference cost bằng batching, caching,model cascading

5. Thiếtkế cost allocation & FinOps reviewprocess cho team Cost anatomy→ Spot strategy→ Right-sizing + Autoscaling→ Mixed precision→ Inferenceoptimization →FinOpsgovernance →Quiz+ Milestone 2 Giảngviên (VinUni) AICB· Ngày 25 Tuần5 2 / 20

---

<!-- chiron-source-span: {"source_span_id":"154b3111-ef31-5041-b3f7-1a67b4cfe36f","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Deliverable Cuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"ce417bfb9c3412e925b3d1a72fe91977fa784aa889f1130ec7a3a4353cf2a6fc"} -->

## Slide 5 - Deliverable Cuối Ngày

Labnotebook hoàn thành (8 Parts) +cost charts + Quiz + Milestone2 demo

- Parts 1–5: Mockcluster monitoring, spot savings, autoscaler,waste report

- Parts 6–7: Visualizationcharts + full FinOps workflowend-to-end

- Part 8: RealGPU training FP32 vs AMP —time/memory/cost comparison

- Quiz Chương 5: 15câu hỏi CI/CD, LLMOps, Monitoring, Governance,FinOps

- Milestone 2: Demooperations platform end-to-end
Giảngviên (VinUni) AICB· Ngày 25 Tuần5 3 / 20

---

<!-- chiron-source-span: {"source_span_id":"fc0fe561-7490-5053-89e6-3d3297e5a502","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Chi Phí GPU Cloud: Breakdown","extraction_method":"pdf-text-layer"},"checksum":"7c3ba8d2f044ff018516b5783ef68ae14e9578e7aba53f361f26e6fe9f2bebd3"} -->

## Slide 6 - Chi Phí GPU Cloud: Breakdown

Compute (GPU hours) 60% Storage 15% Net 10% Other 15%

- Hidden costs: datatransfer egress ($0.09/GB AWS),NATgateway ($0.045/GB), Secrets Manager
($0.40/secret/mo)

- Wasted spend: idleGPUs (training done, instance running),over-provisioned instances, unused reserved capacity

- FinOps maturity: Inform →Optimize →Operate— hầu hết AI teamschỉ ở Inform level
Giảngviên (VinUni) AICB· Ngày 25 Tuần5 4 / 20

---

<!-- chiron-source-span: {"source_span_id":"e8df177d-3919-5647-b168-18181e284e2c","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Wasted Spend Patterns — Tại Sao Phí Tiền?","extraction_method":"pdf-text-layer"},"checksum":"2be4e5e073e14ff0297c45232df47f4097a89bd19b28b028384eb64d2ee5675e"} -->

## Slide 7 - Wasted Spend Patterns — Tại Sao Phí Tiền?

1. GPUidle overnight — training xong nhưng instancevẫn chạy

2. Over-provisioned: dùng H100 choinference 8Bmodel (A10G đủ rồi)

3. Unusedreserved capacity mua 1 năm nhưng workloadthay đổi

4. Developmentenvironments chạy 24/7 (chỉ cầngiờ hành chính)

- 4xA100 idle 12h/day

- Chiphí: 4 ×$3.0/hr ×12h= $144/ngày

- $52,560/năm—chỉ riêng idle time!

- Fix: auto-shutdown schedule→tiếtkiệm
ngay Rule of thumb: GPUutilization <30%= cần right-size ngay Giảngviên (VinUni) AICB· Ngày 25 Tuần5 5 / 20

---

<!-- chiron-source-span: {"source_span_id":"a0ca9f43-deb9-5f63-bf9a-6aa67f3a1c52","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Spot Instances: Tiết Kiệm 60–70%","extraction_method":"pdf-text-layer"},"checksum":"eec9be89abc1c80a05ab90b05df7386875c0cd87d3ed7beafbacb3ca6df1fe56"} -->

## Slide 8 - Spot Instances: Tiết Kiệm 60–70%

- Discount60–70% so với on-demand

- 2-mintermination notice

- SpotFleet: request từnhiều AZ/instance
types

- Giảminterruption rate từ 15%→3%

- Discounttới 80%

- Terminatesau24h (Preemptible) hoặc
flexible(Spot)

- Phùhợp jobs <20h

- Tựđộng reschedule trên GKE
Mixed fleet strategy: 20%on-demand (baseline) + 80% spot(burst) — balance cost vs reliabilitySkyPilot: Multi-cloud spotabstractionlayer—tựđộngtìmcheapestspotacrossAWS/GCP/Azure. sky launch task.yaml chọnprovidertốiưu. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 6 / 20

---

<!-- chiron-source-span: {"source_span_id":"62387b1d-7410-5756-b765-1bc223e0cd50","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Checkpoint Strategy cho Spot Training","extraction_method":"pdf-text-layer"},"checksum":"daf53dbb93d79e4fcbc03ae714747043c4c36fd32b7314d7f214a500140389e3"} -->

## Slide 9 - Checkpoint Strategy cho Spot Training

Epoch 1 Train Checkpoint to S3 Epoch 2 Train Spot Terminated! New Spot Instance Load Checkpoint Epoch 2 Resume

- Savemodel state mỗi epoch (hoặc mỗi30 phút cho long epochs)

- Checkpointlưu lên S3/GCS — resume từbất kỳ instance nào

- PyTorchLightning ModelCheckpoint callbacktự động hoá

- Bestpractice: test resumeflow trướckhichạy long training
Giảngviên (VinUni) AICB· Ngày 25 Tuần5 7 / 20

---

<!-- chiron-source-span: {"source_span_id":"833cd510-afa4-5660-996e-a9854fb2b5cf","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"GPU Utilization: Mục Tiêu >70%","extraction_method":"pdf-text-layer"},"checksum":"96542e73e164234bf2070a801a8b3ed0ddc6beed56616b974648b14120748f22"} -->

## Slide 10 - GPU Utilization: Mục Tiêu >70%

Workload Typical Util Target Action nếu thấp Inference(single model) 20–40% >60% Multi-modelserving, MIG Inference(batched) 50–70% >75% Tunebatch size, queue Fine-tuning 60–80% >80% Largerbatch, gradient accum Pre-training 80–95% >90% Optimisedata loading Monitoring: nvidia-smi dmon -d 5 hoặcDCGM Exporter →Prometheus →Grafanadashboard Giảngviên (VinUni) AICB· Ngày 25 Tuần5 8 / 20

---

<!-- chiron-source-span: {"source_span_id":"252eab27-e125-5e9d-8e9b-713c9a852e12","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Multi-Model Serving & MIG","extraction_method":"pdf-text-layer"},"checksum":"41fbd35935fe3e3cb0662568b662d9360c1b9cb4330eb2ad8a1d73b7201b54d7"} -->

## Slide 11 - Multi-Model Serving & MIG

- vLLMserve Llama-3-8B + Mistral-7B trên
A10G(24GB)

- Dynamicloading: swap modelstheo request

- Utilizationtăng từ 25%→65%

- A10080GB →7isolatedinstances(3g.20gb)

- 7models chạy song song, isolation đảmbảo

- K8s: nvidia.com/gpu.shared: true

- Perfectcho inference farm
Vertical Pod Autoscaler (VPA): recommendCPU/memory limits dựa trên actualusage — avoid over-provisioning resources. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 9 / 20

---

<!-- chiron-source-span: {"source_span_id":"58167b45-ae43-5792-80ec-fc1ff66460fb","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"GPU Autoscaling: KEDA-like Approach","extraction_method":"pdf-text-layer"},"checksum":"aee893ed888cec9265ff18fb1e5fb1cdc5c5ab18eaf5dfa03fc5d6df5cc33c2b"} -->

## Slide 12 - GPU Autoscaling: KEDA-like Approach

- Scale-up: GPUutilization >80% →add
node

- Scale-down: utilization <20% →remove
idlenode

- Cooldown: 60sgiữa các scaling events

- Bounds: min1 node, max 8 nodes

- KEDA:event-driven autoscaling cho K8s

- Prefercheapest GPU type khi scale-up (T4
trướcA100)

- Scale-downidle nodes trước — tiết kiệm
ngay

- Spotinstances cho burst capacity

- Monitor: nếuidle >50%GPUs →scaledown
Key metric: Costper useful GPU-hour,khôngphải tổng spend Lab demo: Configureautoscaler policy →submitworkloads →observescale-up/down decisions →measurecost impact. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 10 / 20

---

<!-- chiron-source-span: {"source_span_id":"5968b06e-2a86-52f1-a28e-fe80a41f5659","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"5 Kỹ Thuật Giảm Chi Phí Inference","extraction_method":"pdf-text-layer"},"checksum":"f4e25de1c846a923e9964e88f0eb4596d68b2a38652256484d5ca09fef8d312f"} -->

## Slide 13 - 5 Kỹ Thuật Giảm Chi Phí Inference

Request Batching 10 req/batch → 8x throughput Redis Caching 30–40% hit rate for chatbot Model Cascading 8B handles 80%, escalate 20% Quantization AWQ 4-bit: cost/M tokens ↓34% Spot for Inference Stateless + LB failover Combined effect: Batching+ Caching + Cascading + Quantization →70–85%cost reduction so với naive deployment. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 11/ 20

---

<!-- chiron-source-span: {"source_span_id":"0fcfe23d-e1e1-5d6e-bfa9-fe8feb05d56e","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Request Batching & Caching Chi Tiết","extraction_method":"pdf-text-layer"},"checksum":"8940e92a2b1625d675d2b4f9a2c5d3d681050e47ea0f743b218d8368fc1f6e1b"} -->

## Slide 14 - Request Batching & Caching Chi Tiết

- Group10 requests mỗi batch

- Throughputtăng 8x, cost/request giảm 85%

- vLLMcontinuous batching tự động

- Tune max_num_seqs theolatency SLO

- Rediscache cho identical prompts

- Hitrate 30–40% điển hình cho chatbot

- Semanticcache: embed prompt→similarity
search

- TTL:1h cho dynamic, 24h cho staticprompts
Giảngviên (VinUni) AICB· Ngày 25 Tuần5 12 / 20

---

<!-- chiron-source-span: {"source_span_id":"a8a1b3e3-befa-5b6b-9e0e-8b8425ceac83","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Model Cascading & Quantization ROI","extraction_method":"pdf-text-layer"},"checksum":"33548086daaef4ebb4099ff75283ceedd7f30dd1e56bcd4054c0d258f136b504"} -->

## Slide 15 - Model Cascading & Quantization ROI

- Smallmodel (Llama-3-8B) xử lý 80%
requests

- Escalate20% complex queries→large
model

- Router: classify difficultybằngfast classifier

- Costreduction: 60–70%
Mode Tok/s $/M tok FP16(A10G) 1200 $0.83 AWQ4-bit 1800 $0.55 Savings 34% Spot cho inference: statelessinference servers phù hợp spot instancesnếu có load balancer automatic failover. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 13 / 20

---

<!-- chiron-source-span: {"source_span_id":"24dd29ae-8670-5958-a2e4-3e60d1fbfacf","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Mixed Precision Training: Giảm Cost & Tăng Speed","extraction_method":"pdf-text-layer"},"checksum":"c5bd1afd9e4f047a9b4b4bfb56e5180dedc9da0ba8ff07553261ca8ad499b597"} -->

## Slide 16 - Mixed Precision Training: Giảm Cost & Tăng Speed

- torch.cuda.amp.autocast: forward pass
FP16

- GradScaler: tránh underflow khibackward

- Memorygiảm ∼30–40% →batchsize lớn
hơn

- Trainingtime giảm 20–50% tuỳ model

- Accuracygần như không đổi (<0.5%drop)
Metric FP32 AMP Time/epoch 1.0x 0.6–0.8x Peakmemory 100% 60–70% Cost/run $1.00 $0.60–0.80 Savings 20–40% BF16 trên A100/H100: khôngcầnGradScaler,stablehơn FP16 Lab demo: TrainResNet-18 CIFAR-10FP32 vsAMP trên Kaggle GPU→sosánh time, memory,power,cost thực tế. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 14 / 20

---

<!-- chiron-source-span: {"source_span_id":"66ebf4b2-e2b2-5d3d-a5c7-eb71f7f90b70","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Tagging & Cost Allocation Strategy","extraction_method":"pdf-text-layer"},"checksum":"37e04824232680712d6736081f74e58100acb21110856a47e84f0bbb84c8c7fb"} -->

## Slide 17 - Tagging & Cost Allocation Strategy

- team=ml-platform

- project=rag-service

- env=production

- cost-center=engineering

- Enforcetags bằng SCP/OPApolicies

- ResourceQuota pernamespace

- Teambudget: max 4 GPUs,100GB storage

- Kubecost: per-podcost breakdown

- “RAGservice $45/day,Embedding $12/day”
AWS Cost Explorer + Budgets: alertkhi spending vượt $1,000/day→immediateinvestigation. Monthly FinOps review: sharedashboard →ownershipdrives optimization. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 15 / 20

---

<!-- chiron-source-span: {"source_span_id":"a6641e95-5ead-57d6-9b77-8f8056fc220d","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Carbon & Energy Optimization","extraction_method":"pdf-text-layer"},"checksum":"a27a8fd434189077d918025de9d89fc9276c77cb6468cca0d508f68b2ebc0248"} -->

## Slide 18 - Carbon & Energy Optimization

- Chạytraining khi grid sạch nhất

- us-west-2 (Oregonhydro) 10x greener than
us-east-1

- CodeCarbonlibrary: track CO2 per
experiment

- Scheduleheavy jobs off-peakhours

- Distilledmodels: Phi-3-mini vsGPT-4—
100xsmaller,70% accuracy

- Chain-of-thoughttăng cost 3–5x — chỉ dùng
khicần

- GreenAI metric: CO2 gramsper 1000
inferences

- Track& report cùng performance metrics
Takeaway: SustainableAI không chỉ “nice-to-have” —region selection + model selection =cost savings + carbon reductioncùng lúc. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 16 / 20

---

<!-- chiron-source-span: {"source_span_id":"fa86c651-2d7f-5baf-9580-e84fb5e4ca9b","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Live Demo: GPU FinOps Lab (Docker Compose + Kaggle GPU)","extraction_method":"pdf-text-layer"},"checksum":"cabc5ed612ef191d7b92028e3fa258b6bfb8059db3ef88b80379e1aaf0dbbf7c"} -->

## Slide 19 - Live Demo: GPU FinOps Lab (Docker Compose + Kaggle GPU)

1. Part 1–2: Clustermonitoring+workloadsubmission →đoutilization,pháthiện idleGPUs

2. Part 3: Spotbidding + preemption simulation→savingsreport (60–70% discount)

3. Part 4: Autoscalerpolicy tuning →observescale-up/down decisions

4. Part 5: Costtracker (OpenCost-like): wastereport + optimization recommendations

5. Part 6–7: Visualization+ end-to-end FinOps workflow

6. Part 8: RealGPU training FP32 vs AMP trênKaggle→đotime, memory,cost thựctế Giảngviên (VinUni) AICB· Ngày 25 Tuần5 17 / 20

---

<!-- chiron-source-span: {"source_span_id":"11f7aa04-2e24-546a-ace4-9d58bacf3c79","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Lab #25","extraction_method":"pdf-text-layer"},"checksum":"1f4c520b0823147ec5186a80e9cad94328e3b4b891742ba3082b49ca5d6a3d71"} -->

## Slide 20 - Lab #25

Mục tiêu: GPUFinOps Optimization Workshop Deliverable: Labnotebook8parts(Dockermockcluster+KagglerealGPU)+cost charts+ Milestone 2 demo Thời gian: 2.5h Giảngviên (VinUni) AICB· Ngày 25 Tuần5 18 / 20

---

<!-- chiron-source-span: {"source_span_id":"f43fc39a-e4da-5a0a-9b87-50a59e22788d","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Recap Chương 5: Vận Hành","extraction_method":"pdf-text-layer"},"checksum":"11bcc2174f84ee888f40f721dab645d1b669dab236fc8c4cfc5fd92fa0626cb4"} -->

## Slide 21 - Recap Chương 5: Vận Hành

N21 CI/CD for AI N22 LLMOps N23 Monitoring N24 Governance N25 FinOps Chương 5: Operations Layer Complete

- Key insight: operationscost thường = infrastructure costsau 6 tháng production

- FinOps quick wins: scheduleidle shutdown + quantize models+ implement caching = 40–60% reduction

- Invest early: CI/CD+ monitoring + governance +FinOps — trả nợ sớm, khôngphải trả lãi
Giảngviên (VinUni) AICB· Ngày 25 Tuần5 19 / 20

---

<!-- chiron-source-span: {"source_span_id":"3f285755-0135-5f19-9c85-46e22abed3c1","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Tổng kết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"432a481a8a1b2d7e36f56105ca6586538cc1fa304e26628190159ec37a30a3eb"} -->

## Slide 22 - Tổng kết — Key Takeaways

Những ý chính cần nhớ trướckhi sang bài tiếp theo 1 GPU cost anatomy: Compute 60% + hidden costs — audit waste trước khi optimize. Au- toscalergiúp scale-down idle nodes tựđộng. 2 Spot instances tiết kiệm 60–70% — checkpoint mỗi 30 phút. Mixed Precision (AMP) giảm thêm20–40% training cost. 3 Inference optimization: batching + caching + cascading + quantization = 70–85% cost reduc- tionso với naive deployment. Giảngviên (VinUni) AICB· Ngày 25 Tuần5 19 / 20

---

<!-- chiron-source-span: {"source_span_id":"0b185b07-21dc-5455-a42c-592a4fb4486c","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"4affc58695b31be367aae89624e9c3b1b184dc46aaabec13211c7e5b91fbe5c7"} -->

## Slide 23 - Tiếp theo & Bài tập

Chương 6: Tổng Hợp — MCP/A2A Infrastructure “Agentgọiagent—MCPserverhost- ing, A2A protocol, agentic routing cho multi-agentsystems”

- Hoànthành Lab 25 + Milestone
2demo

- Đọctrước: Anthropic MCP
specification

- Đọctrước: Google A2Aprotocol
overview Giảngviên (VinUni) AICB· Ngày 25 Tuần5 20 / 20

---

<!-- chiron-source-span: {"source_span_id":"13c99061-19aa-538a-a074-251c45612709","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"0f443666593bbc78f4b83dd8d1839e96217c8cee8fe95cc4b3a3439498cf04db"} -->

## Slide 24 - Hỏi & Đáp

Câu hỏi nào về GPU FinOps, spot instances, inference optimization, hay cost allocation?

---

<!-- chiron-source-span: {"source_span_id":"e71e162d-0fd8-56a0-aeb1-e421c6e1f7f5","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"bf3b8234fed8d4d545240ad8551a9c9fe3d686c492f97cfa932c3dc40581306a"} -->

## Slide 25 - Cảm ơn!

AICB-P2T2 · Ngày 25 GPU FinOps & Cost Optimization lms.vinuni.edu.vn · Slide & template trên LMS
