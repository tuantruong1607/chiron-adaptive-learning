---
schema_version: 1
course_id: rag-intensive
document_id: "252ca2cc-8e1a-52d4-980e-fbed5736833b"
document_version_id: "6c9462ab-953f-52da-895d-994101b229ba"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Model Serving & Inference"
source_file: "track 2 - day 20.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 20.pdf"
source_sha256: "b1653d0696c5a6c71e3cbe3c23f3d587eda9f7c3cd9eb54859723d23dedd197e"
parser_version: chiron-structured-markdown-v1
page_count: 46
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":46}"
language: vi
---

# Model Serving & Inference

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"5023de34-3e1b-5a20-bab0-d3f9742c0ea0","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Model Serving & In","extraction_method":"pdf-text-layer"},"checksum":"c3dbb01daf75341c57ae7bddb721b3c1d4cc628595a196bfc0ddd9b42b66de20"} -->

## Slide 1 - Model Serving & In

Model Serving & In- ference Optimization AICB-P2T2 · Ngày 20 · Chương 4: Hạ Tầng Giảngviên VinUniversity · Phase 2 · Track2· Tuần4

---

<!-- chiron-source-span: {"source_span_id":"d7a15daa-9973-52e4-b8ff-9bf65f0ea3fc","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"a82e5c45a685e516778f70718aac2407ab1b6cb56cdb94ac305e36ca8aa69c1b"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Model accuracy 95% nhưng latency 3 giây. User đợi không nổi, churn tăng 40%. Model tốt nhưng serve chậm = product thất bại.” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"6e3af1fd-bc22-5f4a-978c-b32fb3f2a28d","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"NộiDung Bài Học","extraction_method":"pdf-text-layer"},"checksum":"aa7447c36779152dd864cd4e7ebf7f7dd623b254a6d65873d8b1cc51fe4cc4e3"} -->

## Slide 3 - NộiDung Bài Học

1. BốiCảnh & Vocabulary(latency, pre-LLMera)

2. Quantization: FP16/FP8/AWQ/GGUF/NVFP4

3. KVCache & Attention Optimization

4. Single-NodeServing Stack 2026 (8 engines)

5. Distributed& Multi-TenantServing

6. ServingRegimes 2026 (VLM, embed, cache,route, power,security)

7. Auto-scaling& Operations

8. Edge& Hardware Landscape

9. ProductionSLA (Goodput@SLO)

10. Lab20 + Milestone 1 Giảngviên (VinUni) AICB· Ngày 20 Tuần4 1 / 40

---

<!-- chiron-source-span: {"source_span_id":"304ab178-62eb-596b-a2e1-877ae85bfce3","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mụctiêu bài học","extraction_method":"pdf-text-layer"},"checksum":"2419dc04afcf9fb967abcd415f668564afe5df083e9ae86372db99f6151317f8"} -->

## Slide 4 - Mụctiêu bài học

### Saubuổi học này,bạnsẽ

1. Phânbiệt Throughputvs Goodput@SLO,đọc TTFT/TPOT trên dashboard production

2. Ápdụng quantization (FP16/FP8/AWQ4-bit/NVFP4/GGUF) đểgiảm memory & tăng throughput

3. HiểuKV Cache, PagedAttention, RadixAttention, FlashAttention 3/4,MHA→MLA

4. Sosánh 8 serving engines (vLLM, SGLang,NVIDIA Dynamo, llm-d, LMDeploy, TensorRT-LLM,Ollama, llama.cpp)

5. Chọnđúng parallelism strategy (TP/PP/EP/DP) cho workloaddistributed

6. Hoànthành Lab 20 (llama.cpp tuning bonus)và submit Milestone 1 Foundations → Quantization → KV/Attention → Single-Node → Distributed → Regimes2026 →Auto-scale →Edge →SLA →Lab20 Giảngviên (VinUni) AICB· Ngày 20 Tuần4 2 / 40

---

<!-- chiron-source-span: {"source_span_id":"28ec80c8-0de0-5b86-a7c4-e31f96c65106","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"DeliverableCuối Ngày","extraction_method":"pdf-text-layer"},"checksum":"d5865fc71819cae4aa8225f0fea3d97cec01d43d3c131d68dbfd98049400ec8a"} -->

## Slide 5 - DeliverableCuối Ngày

Optimizedinference stack + Lab 20 report+ Milestone 1 demo

- Benchmarkreport: GGUF quantsweep (Q2_K→Q8_0)+ continuous batching,
P50/P95/P99

- Loadtest: 10 &50 concurrent users (locust) trênllama-server

- Lab20 report (benchmarks/results.md vớiP50/P95/P99 + bonus tuning notes)

- Milestone1: AI infrastructureplatform demo (N16–N19)
Giảngviên (VinUni) AICB· Ngày 20 Tuần4 3 / 40

---

<!-- chiron-source-span: {"source_span_id":"b505b48e-db3f-5c96-8154-da2ad657cbc4","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"LatencyTaxonomy: TTFT· TPOT · Goodput","extraction_method":"pdf-text-layer"},"checksum":"ae90ed843cbaf8017b14bf3d9488fabd5c56220dd01c304f9e82afbba8117c37"} -->

## Slide 6 - LatencyTaxonomy: TTFT· TPOT · Goodput

- TTFT(TimeToFirstToken): từ request đến
tokenđầu tiên — phụ thuộcprefill compute + queuewait

- TPOT(TimePerOutput Token) =ITL:
khoảngcách đều giữa mỗi outputtoken

- E2ELatency =TTFT+TPOT ×(N–1);SLO
thườngở P95/P99

- Throughput: tokens/s toàn hệthống ở
saturation,không có SLO constraint

- Goodput: req/sthỏamãn TTFT+TPOTSLO
—metricproduction quan trọng nhất

- QueueDepth: requests đang chờprefill —
chỉbáo saturation Ví dụ thực tế— H100 · Llama-3-70B · batch32:TTFT ≈450ms ·TPOT ≈25ms · Throughput1,800tok/s · Goodput@SLO(TTFT<1s,TPOT <50ms) ≈1,200tok/s Lưu ý:Throughput@saturation ̸= Goodput@SLO. Báo cáo chỉ throughput mà bỏ qua SLOconstraint là misleading — luônreport goodput cho production. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 4 / 40

---

<!-- chiron-source-span: {"source_span_id":"ece2b7df-ae8f-5fd3-997b-f7eb97cefb77","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Pre-LLMEra: Serving Infrastructure2017–2022","extraction_method":"pdf-text-layer"},"checksum":"c9e3f43ac0719c830313d5a5d84ea324bafee046c38a1b4b46fd2e173e38f6b7"} -->

## Slide 7 - Pre-LLMEra: Serving Infrastructure2017–2022

- TFServing (Google2017): SavedModel,
gRPC,versioned endpoints, static batch

- TritonInference Server(NVIDIA2019):
multi-framework,dynamicbatchingpermodel

- ONNXRuntime (2019): cross-framework
export,CPU/GPU/NPU optimized kernels

- TorchServe(Facebook2020): MAR
archives,REST API, multi-model serving

- BentoML(2020): Python-native packaging,
pluggableruntimes

- Memoryfragmentation: KV cache cần
contiguousblock cố định — 60–80%VRAM waste

- Staticbatching: chờ đủ batch,thêm
200–500ms latency

- Notoken streaming: client chờ toànbộ
responsetrước khi nhận

- Nocontinuous batching: 1 long request
blocktoàn queue

- Fixed-lengthI/O:không xử lý được
variable-lengthgeneration The Shift (Jun 2023)— vLLM PagedAttention: KV cache qua virtual memory pages(non-contiguous,nofragmentation)+ continuousbatching (requestsvào/ra liêntục) →LLMserving era. 24×throughputvs naive HF Transformers. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 5 / 40

---

<!-- chiron-source-span: {"source_span_id":"f6c0b549-d2f0-5c72-b3e6-1d885ba26ee8","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Quantization: Precision vs Performance","extraction_method":"pdf-text-layer"},"checksum":"503035215abd2fbc2d1b885b2e519cbfdb8dec0f5e32b75dd84420d9063a29dd"} -->

## Slide 8 - Quantization: Precision vs Performance

VRAMUsage (Llama-3-8B) FP32 31.6GB FP16 15.8GB FP8 7.9GB — Hopper/Blackwell native INT8 7.9GB AWQ4-bit 4.5GB FP8: <1% drop, 2× mem- ory vs FP16 (Hopper+ native) AWQ 4-bit: ∼1pt MMLU drop trên 8B+, lớn hơn với<7B NVFP4 (Blackwell): 3.5× vs

### FP16, 1.8× vs FP8,<1% lossChọn quantization
Production Hopper: FP8 / AWQ 4-bit Production Blackwell: NVFP4 (default) Max quality: BF16 / FP16 Edge/laptop: GGUF Q4_K_M (i-quants nếu <Q4) Giảngviên (VinUni) AICB· Ngày 20 Tuần4 6 / 40

---

<!-- chiron-source-span: {"source_span_id":"77ba126d-0afe-5420-8988-3dac03c8de10","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Quantizationfor Memory: GGUF· NF4 · GPTQ · AWQ","extraction_method":"pdf-text-layer"},"checksum":"5b44b8bd3dfb1e99c90b59eceef72f0641968da0ea4a3f7cb1cb083b7bb284a2"} -->

## Slide 9 - Quantizationfor Memory: GGUF· NF4 · GPTQ · AWQ

Format BPW 8BVRAM 70B VRAM Quality FP16 16 15.8GB 140GB Baseline FP8 8 7.9GB 70GB <1%drop AWQ4-bit 4.5 4.5GB 40GB ∼1ptMMLU GPTQ4-bit 4.0 4.0GB 35GB ∼1ptMMLU GGUFQ4_K_M 4.5 4.8GB 43GB ∼1ptMMLU GGUFQ2_K 2.6 2.7GB 24GB Noticeable NF4(bnb) 4.0 4.0GB 36GB ∼1ptMMLU

- GPTQ:inverse Hessian layer-by-layer (128
calib.samples). Chậm quantize,nhanh inference.

- AWQ:tìm salient weights (high activation
magnitude),scale trước INT4 rounding. Acc> GPTQcùng bits.

- NF4(bitsandbytes): 4-bit NormalFloat, optimal

### chonormal-distributed weights. Doublequant
constantsFP32 →FP8.

- GGUFk-quant: Q4_K_M = mixedQ4/Q6 per
tensor(attn vs FFN).k=betterquant, m=medium size.

- GPUcloud (Hopper): FP8—best
quality/perf

- GPUVRAM tight: AWQ4-bit —tốt nhất ở
4-bit

- CPU-onlyinference: GGUFQ4_K_M —
recommended

- Cựckỳ constrained: GGUFQ2_K —last
resort

- Fine-tunetrên 1 GPU:NF4+ QLoRA
Lưu ý: <7B models mất quality nhanh hơn 13B+. Benchmark perplexity saukhi quantize.Giảngviên (VinUni) AICB· Ngày 20 Tuần4 7 / 40

---

<!-- chiron-source-span: {"source_span_id":"8dcdfc51-c034-56de-b6b2-eb6cb37530f9","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"KVCache & PagedAttention","extraction_method":"pdf-text-layer"},"checksum":"a4493608248ce44316ea59fe603b9fb5aba1ac169f7e31e139ffb586241396e1"} -->

## Slide 10 - KVCache & PagedAttention

Traditional: Contiguous Wasted! PagedAttention: Paged PageTable Nowaste

- KVcache như virtual memory pages

- 24×vsnaive HF Transformers

- Dynamicmemory allocation

- Táisử dụng KV qua radixtree (prefix
sharing)

- Lýtưởng cho RAG, multi-turn, agents

- Engineeringchi tiết: xem§3 Prefix
Caching Giảngviên (VinUni) AICB· Ngày 20 Tuần4 8 / 40

---

<!-- chiron-source-span: {"source_span_id":"633930ea-84aa-5836-a03c-ed55a43e33bf","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"AttentionArchitecture: MHA →MLA& Long-Context","extraction_method":"pdf-text-layer"},"checksum":"20e9c2e46f24e5b996dabdaa7267c6c6fc92237cab998bafa00e55951c94b544"} -->

## Slide 11 - AttentionArchitecture: MHA →MLA& Long-Context

MHA GQA MQA MLA KV:1× KV:4×less KV:8×less KV:10×less Standard LLaMA-2/3 GPT-3era DeepSeek-V3

- CompressQ/K/V xuống latent vector nhỏtrước
attention

- DeepSeek-V3: 10×ítKV memory vs standard
MHA

- Kernel: FlashMLA, CutlassMLA, FlashInfer
(2025)

- Chophép context dài hơn trêncùng VRAM

- YaRN:RoPE interpolation, không cần
retrain

- StreamingLLM:attention sinks, ∞context

- Jamba(AI21Labs): SSM/Transformer
hybrid,256K ctx

- FA3+ MLA backends→kernelcho context
dài(xem §3) Giảngviên (VinUni) AICB· Ngày 20 Tuần4 9 / 40

---

<!-- chiron-source-span: {"source_span_id":"01eeedd8-5111-56ae-8341-79875dc1471a","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"SpeculativeDecoding & Continuous Batching","extraction_method":"pdf-text-layer"},"checksum":"037d2b03684e3838951e7f42a5f66e95e3a5bf6a69d742392b50859f56d6048e"} -->

## Slide 12 - SpeculativeDecoding & Continuous Batching

- Draftmodel sinh 4–8 tokens, targetverify
songsong trên cùng 1 forwardpass

- EAGLE-3(NeurIPS’25): 3.0–6.5×,
+20–40%so EAGLE-2

- DeepSeekMTP (Multi-TokenPrediction):
∼1.8×,acceptance 85–90%(DeepSeek eval)

- LookaheadDecoding: self-drafting khi
khôngcó draft model

- Tíchhợp sẵn trong vLLM, SGLang,
TensorRT-LLM

- Staticbatching (legacy): chờ đủ batch→
+200–500ms padding

- Continuousbatching: requests vào/ra mỗi
step,no padding →5×latencygiảm

- Tokenstreaming: client nhận từngtoken —
TTFTcảm giác ↓

- vLLM(continuous batching), TensorRT-LLM
(in-flightbatching) —thuật ngữtương đương

- SGLangpiecewiseCUDA graphcho
variable-lengthbatch Spec-Decode CLI (SGLang) — --speculative-algorithm EAGLE3 --speculative-num-steps 5 --speculative-eagle-topk 4. Yêu cầu draft model checkpointhoặc model có MTP head. Lưu ý: Spec decoding làlatency tool(memory-bound, batch 1–4). Ở batch≥24, verify-overhead có thể làm chậmhơn( ∼0.93×)— engine tự tắt qua--speculative-disable-by-batch-size. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 10 / 40

---

<!-- chiron-source-span: {"source_span_id":"70a27438-ac96-54ca-9307-8e2f982773b4","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"FlashAttention: IO-AwareAttention (FA1→FA4)","extraction_method":"pdf-text-layer"},"checksum":"e0a03e304d1a1508fc08addd21f20cdb8da1f81287f6ef48361b123e4f902bcf"} -->

## Slide 13 - FlashAttention: IO-AwareAttention (FA1→FA4)

FlashAttn-1 (Dao2022) FlashAttn-2 (2023) FlashAttn-3 (2024) FlashAttn-4 (2025) NeurIPS’22 arXivJul ’23 Hopper Blackwell Tiling + SRAM O(N) mem, 3–4× Seq parallelism 2× FA1 speed TMA async, FP8 warp specialization FP4 KV cache B200 native

- Standardattn: Q×K(N2×d)viết HBM →đọc
lạisoftmax →đọclại ×V— 3 HBM round trips

- FA:tile Q/K/V vào SRAM,online softmax, ghi
output1lần duy nhất

- Memory: O(N) thay vìO(N2)— context dài
khôngOOM

- FA3: Hopper TMAasync pipeline + FP8. FA4:
BlackwellFP4 KV,SGLang auto-selects

- torch.nn.attention.flex_attention:
BlockMaskAPI

- Express: causal, sliding window,document
boundary,prefix+causal

- Compilequa torch.compile →Triton
kernel,không cần CUDA custom

- Tíchhợp: PyTorch
F.scaled_dot_product_attention,vLLM, SGLangcustom patterns Giảngviên (VinUni) AICB· Ngày 20 Tuần4 11/ 40

---

<!-- chiron-source-span: {"source_span_id":"6161a63b-d9b6-5a78-a773-a3fedd3ee35a","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"ModelCompilation: torch.compile +CUDA Graphs + TensorRT","extraction_method":"pdf-text-layer"},"checksum":"21dac4987e4eb6fcef9e7ae4277c1e3c8f26904fa173b6ed4325a1e4eb113288"} -->

## Slide 14 - ModelCompilation: torch.compile +CUDA Graphs + TensorRT

- Capturecomputation graph quatorch.fx;
TorchInductortạo Tritonkernels

- Kernelfusion: nhiều element-wiseops →1
kernel,ít HBM reads hơn

- mode="max-autotune": tìm optimal kernel
config(compile chậm, run nhanh)

- mode="reduce-overhead": loại Python
overheadnhanh

- dynamic=True: variable shapes khôngtrigger
recompile

- Speedup: 1.1–1.5×trênLLM decode phase

- Record: chạy 1 forwardpass, capture GPU
commandstream

- Replay: skip Python overheadmọi lần sau
(0.5–2ms/step tiết kiệm)

- LLMdecode = cùng ops lặpN_tokens lần→
CUDAgraph lý tưởng

- vLLMv1: decode dùng CUDAgraph replay;
prefillchạy eager (variable shape)

- SGLang: ”piecewise CUDA graph”cho
mixedstatic/dynamic batch sizes

- Cộngthêm 10–20% throughput trên mọi
optimizationkhác TensorRT Compilation— ONNX → layer fusion→ kernel selection→ FP8/INT8 calibration →.trtengine. 3–5×vsvanillaPyTorch. Compiletime: 5–30min/model. Dùngtrong TensorRT-LLMvà NVIDIA TritonInference Server. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 12 / 40

---

<!-- chiron-source-span: {"source_span_id":"8ad21826-752b-5d46-ba4f-61adb74c4670","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"ServingStack 2026: 8Engines That Matter","extraction_method":"pdf-text-layer"},"checksum":"d2878716b6017ae8aa86b7dd75c46af489d13b7b7d50a0bf653f438043600396"} -->

## Slide 15 - ServingStack 2026: 8Engines That Matter

Engine Ưuđiểm chính Bestfor API vLLM PagedAttention,Auto Prefix Cache + chunkedprefill LLM production OpenAI-compat SGLang RadixAttention,structured gen, MLA backend Multi-turn/ chat OpenAI-compat NVIDIADynamo DisaggregatedP/D orchestrator (GA 1.0) Multi-tenantcloud OpenAI-compat llm-d K8s-native,KV-awarerouting Productionat scale OpenAI-compat LMDeploy TurboMindengine, hiệu suất cao Highthroughput OpenAI-compat TensorRT-LLM NVIDIAnative, FP8/FP4 optimized NVIDIAGPU fleet Tritonbackend Ollama 1lệnh: ollama run (wrapsllama.cpp) Localdev/testing REST llama.cpp GGUFnative, CPU+GPU mixed offload,AppleMetal Local/ CPU / edge REST/ OpenAI-compat Lưu ý: Production 2026: vLLM v1 hoặc SGLang. Disaggregated scale: llm-d / Dynamo. LocalCPU/Mac: llama.cpp. Container: Ollama. NVIDIA fleet: TensorRT-LLM. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 13 / 40

---

<!-- chiron-source-span: {"source_span_id":"97e7578e-fb8a-582a-a8fd-e10f935a0f80","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"InferenceEngine Evolution: 2020→2025","extraction_method":"pdf-text-layer"},"checksum":"b6698586c79a39f96badf70465db64bdfd253762d08831d72ab8543921674763"} -->

## Slide 16 - InferenceEngine Evolution: 2020→2025

HF Transformers DeepSpeed Inference Faster- Transformer vLLM PagedAttn SGLang RadixAttn vLLMv1 Disagg. era 2020 2021 2021 Jun2023 Jan2024 Jan2025 Manual batching inference scripts Tensor parallel, ZeRO-Inference Optimized CUDA kernels PagedAttn, continuous batching RadixAttention, prefix sharing APC default, disaggregated P/D 2020–2022: manual/static batching, CUDA kernels — framework-level optimizations.Jun 2023:PagedAttention

- continuous batching→ 24× throughput jump, ecosystem convergence. 2024–25: prefix sharing + disaggre-
gatedP/D →TTFTvà goodput là SLO first-class. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 14 / 40

---

<!-- chiron-source-span: {"source_span_id":"fa1479c7-7022-5add-b0dd-f9c233f2c4b4","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"PagedAttention: vLLM v0→v1Deep Dive","extraction_method":"pdf-text-layer"},"checksum":"c4c03f3000746e9527a948c4ae27069394486b43506015dd01ae8faade1c151a"} -->

## Slide 17 - PagedAttention: vLLM v0→v1Deep Dive

LogicalKV PhysicalPages L0 L1 L2 L3 P0 P3 P1 P5 Page Table Sequential Non-contig.

- PagedAttention: KV như virtualmemory pages,24×
vsHF naive

- Blocksize: 16 tokens/page(default). FCFS scheduler
+preemption

- Continuousbatching: requests join/leave
mid-generation

- Prefixcaching opt-in (--enable-prefix-caching)

- Unifiedmemory pool: KVcache + activations trong
cùngpool

- APCON by default: Automatic Prefix Caching,
khôngcần flag

- Chunkedprefill default: chiaprefill thành chunks,
interleavevới decode

- Prefix-awarescheduler. 1.7×v0throughput.
Key Commands — vllm serve MODEL · --tensor-parallel-size N · --gpu-memory-utilization 0.9 · --max-model-len 8192 Giảngviên (VinUni) AICB· Ngày 20 Tuần4 15 / 40

---

<!-- chiron-source-span: {"source_span_id":"73592678-b49a-5af4-9648-a9a246c8aead","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"PrefixCaching: RadixAttention, APC,HiCache & Pricing","extraction_method":"pdf-text-layer"},"checksum":"e9c693130011852236f6523b542cfa7bda46d7f546f20af2412fc2223115dbc1"} -->

## Slide 18 - PrefixCaching: RadixAttention, APC,HiCache & Pricing

- vLLMv1 APC:Automatic Prefix Caching,
ONmặc định

- RadixAttention(SGLang): radix-tree (prefix
trie),cache hit = skip prefilltoàn bộ shared prefix

- LMCache: cross-instance KV sharing
(CPU/disk)

- MooncakeKVCache: global pool trên
disaggregatedcluster

- Tiếtkiệm prefill: −70%TTFT trên repeated
systemprompts (RAG, agents, multi-turn)

- Anthropic: cached read−90%(Claude
Opus4.8 / Haiku 4.5)

- DeepSeek: cache-hit∼98%off(V4 Flash
$0.14/$0.28/M)

- OpenAI:cached input −75%(GPT-4.1/
GPT-5.x)

- Google: cached read−90%(Gemini2.5 /
3.x) Tier1 GPUVRAM(active,hot) →Tier2 HostRAM(spillover) →Tier3 Externalstorage(HF3FS,Mooncake,disk). Attach/detach backend không cần restart. Long-context: vượt GPU VRAM limit. Multi-turn: reuse KV qua nhiều turns. Takeaway — Prefix caching = engineering optimizationvà pricing tier. Thiết kế promptvới system prompt/context cố định ởđầu để tối đa cache-hit rate. Lưuý: Cachemiss vẫn tính full price. Monitor cache-hit rate trongproduction dashboard. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 16 / 40

---

<!-- chiron-source-span: {"source_span_id":"465e814f-8296-571c-8fc8-74ef535994fe","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"AttentionBackend Selection: FA3/ FA4/ FlashInfer/ FlashMLA","extraction_method":"pdf-text-layer"},"checksum":"3bd5bf4b73ab2beebf97bb1a7e4904aa4f4bba1e489f0998e7c0e7e19ad55d68"} -->

## Slide 19 - AttentionBackend Selection: FA3/ FA4/ FlashInfer/ FlashMLA

- H100/H200(Hopper,CUDA 12.3+) → fa3

- B200(Blackwell) → trtllm_mha hoặc fa4

- A100/A40 → flashinfer

- DeepSeekV3/R1 MLA → flashmla
(page=64)

- ROCm/ Ascend / CPU→ triton
(cross-platformfallback) Override: --attention-backend {fa3|fa4|flashinfer|trtllm_mha|flashmla|triton}

- FA3: TMA async, FP8KV,warp
specialization— Hopper native

- FA4: FP4 KV cache— Blackwell SM100
(2025)

- FlashInfer: page-size>1,FP8 KV,
spec-decodetopk >1,sliding window

- TRTLLM-MLA:DeepSeek MLA optimized,
verifiedspec-decode

- Triton: cross-platform fallback (ROCm,
Ascend,NPU, CPU) MLA Backends (DeepSeek V3/R1)— FlashMLA · CutlassMLA · FlashInfer-MLA · TRTLLM-MLA —3.1× throughput vs MHA,10× less KV memory. Tự động chọn theoGPU + model; override chỉ khibenchmark/debug. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 17 / 40

---

<!-- chiron-source-span: {"source_span_id":"cfce8bd1-54fe-5cf9-8255-8a47e3ffe277","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"StructuredGeneration: XGrammar,Tool& Reasoning Parsers","extraction_method":"pdf-text-layer"},"checksum":"655d7770350b76a3f8c0f54096f3d7d90606ddb5b77c91f8126e9dd9f66fe6f6"} -->

## Slide 20 - StructuredGeneration: XGrammar,Tool& Reasoning Parsers

- Formats: JSON Schema, EBNF,Regex,
Pydanticmodel

- Grammarbackends: XGrammar(default,
fastest),Outlines, Llguidance

- Enginesupport: SGLang --grammar-backend
xgrammar,vLLM --guided-decoding-backend xgrammar

- API:OpenAI-compat
response_format={json_schema}

- Reasoningmodels: constraint ápdụng sau
<think>...</think>

- ToolParser --tool-call-parser [model]:
15+models (DeepSeek, Llama-3.1/4, Qwen, Mistral,Kimi-K2); streaming args incrementally

- ReasoningParser --reasoning-parser

### [model](deepseek-r1,qwen3, kimi_k2)
trích <think> → reasoning_content + contenttáchbiệt

- Kếthợp: --reasoning-parser deepseek-r1
--tool-call-parser kimi_k2 Workflow — Prompt → <think>(freereasoning) →grammar-constrainedoutput → response: reasoning_content + contentquaOpenAI-compatible API. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 18 / 40

---

<!-- chiron-source-span: {"source_span_id":"d094281b-7c88-5199-a22b-a3313eb30003","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"ProductionTuning: Memory,Scheduling & Observability","extraction_method":"pdf-text-layer"},"checksum":"14c1c56b830f0aa671ade7490471384ee489884ec8d8559ad8c3bce2e54d9b49"} -->

## Slide 21 - ProductionTuning: Memory,Scheduling & Observability

- --mem-fraction-static (SGLang)/
--gpu-memory-utilization (vLLM):chừa 5–8GB baseline; quá thấp→OOM

- --chunked-prefill-size: giảm 2048–4096
khiprefill OOM (default 8192)

- --max-running-requests / --max-num-seqs:
capburst để tránh decode OOM

- --schedule-conservativeness: 0.3
aggressive· 1.0 default · 1.3conservative

- Queuedepth target: 100–2,000(saturation
>2K)

- --enable-metrics →Prometheusendpoint
:30000/metrics

- Keymetrics: num_running_reqs,
num_queue_reqs,TTFT/TPOT histograms, cache-hitrate

- Scrape →Grafanadashboard; vLLM expose
tươngtự qua prometheus_client

- --log-requests (basic/full);crashdump:
rolling5-phút buffer

- Replay: replay_request_dump.py để
reproducelỗi Tuning + Debug Flow— Start conservativeness=1.0 → monitor queue depth→ Grafanaanomaly → --log-requests trace →crashdump replay →fix+ redeploy. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 19 / 40

---

<!-- chiron-source-span: {"source_span_id":"b53dc3af-75a9-5567-9f97-a166f58d1d0f","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"DisaggregatedPrefill/Decode Serving","extraction_method":"pdf-text-layer"},"checksum":"42fafb2dc11361d0fa4e5b82b6d44e027c73eb1808ad5f2781258f2674383229"} -->

## Slide 22 - DisaggregatedPrefill/Decode Serving

Monolithic(vLLM v0) GPUA P+D GPUB P+D prefillcontends withdecode Disaggregated Prefill Pool Prefill Pool KVTransfer (NVLink/IB) Decode Pool Decode Pool

- NVIDIADynamo 1.0(GA2026): cross-engine
orchestrator,KV-awarerouter,NIXL

- Mooncake(Kimi,FAST’25): 100B+tok/day,global KV
pool,RDMA zero-copy

- llm-d: K8s-native P/D (vLLM+ Gateway API + NIXL),
scale-to-zero

- DistServe(OSDI’24)/ Splitwise(ISCA’24): foundational
papers Lưu ý: KV transfer overhead ∼10GB/s. Lợi ích rõ khi work- load prefill-heavy (long context, RAG). Khôngđáng cho short unique prompts. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 20 / 40

---

<!-- chiron-source-span: {"source_span_id":"d234cdaa-a225-5195-a350-c334e4ec3d94","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Multi-LoRAServing","extraction_method":"pdf-text-layer"},"checksum":"8c4a16a5a4c654cd3f33f21f83646595344584cdf41926dc47bf1afd25929eff"} -->

## Slide 23 - Multi-LoRAServing

BaseModel (7B–70B) LoRA-1 SQL LoRA-2 Med LoRA-3 Code LoRA-N 1GPU Instance

- Punica/SGMVkernels: fused
batched-adapterGEMM (vLLM, SGLang)

- S-LoRA:paged LoRA weights, swap per
request

- vLLM --enable-lora: Nadapters/ 1
endpoint

- SageMakerLMI-Dist: managedmulti-LoRA
hosting

- 12×throughputvs Nseparatesingle-model
servers

- Overhead: +2ms/token cho adapter
application

- SGLang: Chunked SGMV (20–80%lat↓);
LoRAoverlap loading (35% TTFT↓) Usecase — 1basemodel+nhiềudomainadapters(SQL,ytế,code,finance)trên 1GPU — tiết kiệm VRAM vàserving cost so vớiNindependentdeployments. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 21 / 40

---

<!-- chiron-source-span: {"source_span_id":"92ab8ad3-4b4e-55d1-8f0d-b232537bcce1","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"ExpertParallelism: MoE Scaling","extraction_method":"pdf-text-layer"},"checksum":"fbe51833fa29ba9a809eb2ddcd664c1926399c0c4c7ce0639e51f066851f9bf1"} -->

## Slide 24 - ExpertParallelism: MoE Scaling

- ChiaMoE expert weights qua nhiềuGPUs
(khôngreplicate)

- Forwardpipeline: dispatch →pre-permute

- corerunner →combine

- A2A(All-to-All) backends:
--moe-a2a-backend deepep (NVLink/IB), mooncake,nixl

- MoErunner: --moe-runner-backend
deep_gemm hoặccutlass

- Constraint: hầu hết backendsyêu cầu
ep_size = tp_size

- Two-BatchOverlap (TBO):
--enable-two-batch-overlap —xen kẽ A2A/GEMM →+27–35%prefill

- EPLB: --enable-eplb —load balancer giảm
GPUutilization variance

- DeepEPmode: --deepep-mode auto /
normal/ low_latency

- DeepSeek-V3/R1671B:prefill EP32/decode
EP144+DeepEP + EPLB (∼$0.20/1Mout) Two-Batch Overlap (TBO)— TBO xen kẽ A2A communication và GEMM compu- tation trên 2 micro-batches — giấu all-to-all latency→ +27–35% prefill throughput, −50%peak memory (SGLang). Giảngviên (VinUni) AICB· Ngày 20 Tuần4 22 / 40

---

<!-- chiron-source-span: {"source_span_id":"6599be07-eaa6-55d6-807e-2eccd06aaa3d","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"DataParallelism: DP,DPA& Cache-AwareRouter","extraction_method":"pdf-text-layer"},"checksum":"771f4ffa27d3ed02495b44ea26fab296b179348437b5be33374720bda3ec8eff"} -->

## Slide 25 - DataParallelism: DP,DPA& Cache-AwareRouter

- DP:replicate toàn bộ model +KV cache→
memoryduplication

- DPA:chỉ replicate attention; MoE/FC layers
chiasẻ qua EP→khôngduplicate KV cache

- MLAbenefit: DPA+MLA = batch size lớn
hơn,VRAM tiết kiệm đáng kể(DeepSeek V3/R1)

- Flags: --dp-size N --enable-dp-attention

- Gửirequest đến instance có KVprefix cache
phùhợp nhất

- Benchmark8 ×A10080GB: throughput
+92%,cache hit+275%(20% →75%)

- Flags: --router-policy cache_aware
--cache-threshold 0.5

- sgl-router: Rust-based, production-grade
(thaynative DP router) DeepSeek-V3 DP+EP Config — --tp 8 --dp-size 8 --ep 8 --enable-dp-attention kết hợp DPA + Expert Parallelism + cache-aware routing

- +92%throughput.
Giảngviên (VinUni) AICB· Ngày 20 Tuần4 23 / 40

---

<!-- chiron-source-span: {"source_span_id":"b6ad03ba-eff4-5b4b-b8c6-2e875163be7c","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"DistributedInference: Parallelism StrategyGuide","extraction_method":"pdf-text-layer"},"checksum":"295be2cc879c4af4da02665e3c0f4a63ba3cb4a35ee2838bbecb5da78df1cc74"} -->

## Slide 26 - DistributedInference: Parallelism StrategyGuide

Strategy Split Bestfor Tradeoff DataParallelism (DP) Requests Multi-user,replicated model NoKV cache sharing TensorParallelism (TP) Weights/layer Largemodel, single-node All-reducesync mỗi layer PipelineParallelism (PP) Layers Multi-node,128K+ context Bubblelatency,micro-batch ExpertParallelism (EP) MoEexperts Mixtral/ DeepSeek-V3 671B Expertrouting overhead DisaggregatedP/D Prefill/Decode LongRAG, prefill-heavy KVtransfer bandwidth cost

- ray start --head / ray start
--address=... mỗinode

- --tensor-parallel-size 4
--pipeline-parallel-size 2 →8GPU / 2 nodes

- NCCLcollective ops; Ray tự quảnlý device
mesh

- NCCL_IB_HCA=mlx5 choInfiniBand NIC

- TPwithin node: NVLink 900GB/s —
all-reducekhông bottleneck

- PPacross nodes: P2P activation chịuđược
IBlatency

- KhôngTP qua nodestrừNVLink fabric
(NVL72/GB200)

- EP:mỗi GPU giữ subset experts,A2A
routingon-demand RuleofThumb — TP ≤GPUs/node;PP=nodes;EPchoMoE.Vídụ: --tp 4 --pp 2 --ep 8 →cluster2 nodes ×4GPU phục vụ DeepSeek-V3 671B fullprecision. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 24 / 40

---

<!-- chiron-source-span: {"source_span_id":"a140a199-46c6-5ec1-8b63-5d2fb92f744c","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"PipelineParallelism: Ultra-Long Context","extraction_method":"pdf-text-layer"},"checksum":"fc85c1358dfe3a1615feb4870fb475f283fefd5c2232506bc0c58bb5231e295e"} -->

## Slide 27 - PipelineParallelism: Ultra-Long Context

- Chiamodel layers qua nhiều pipelinestages
vớiP2P communication

- Chunkedprefill: các nodesxử lý token
chunksđồng thời →giảmTTFT long context

- --pp-size N:số stages; --nnodes M:số
nodes

- --enable-dynamic-chunking: tự điều chỉnh
theoprefix length

```text
■ Smoothfactor env var (default 0.75,range
0.6–0.85)
```

- DeepSeek-V3.1: 4K fixed hoặc12K dynamic
(smooth=0.65)

- Qwen3-235B:6K fixed hoặc 18K dynamic
(smooth=0.8)

- Dynamic: dùng initial chunk2–3×baseline
đểamortize overhead

- PiecewiseCUDA Graph (PCG) tự độngtắt
khibật PP

- Usecase: 128K+ contexttrên multi-node
GPUcluster PPvsTP — PP ̸=TP:dùngPPkhimodelquálớnchosingle-nodeTP(DeepSeek- V3.1 full precision) hoặc cần 128K+ context — tận dụng multi-node inter-connect bandwidth. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 25 / 40

---

<!-- chiron-source-span: {"source_span_id":"45e38da4-3ceb-5c52-ab4d-6f80dac32646","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Multimodal(VLM) Serving: Encode–Prefill–Decode","extraction_method":"pdf-text-layer"},"checksum":"25471fbcb92e45eba163ed73cf9904d3017ceaebfc05f678d0489fc65464f37c"} -->

## Slide 28 - Multimodal(VLM) Serving: Encode–Prefill–Decode

- 1ảnh 10242 ≈1,100–4,100tokens
(Qwen3-VL ∼1,139,Pixtral 4,096)

- Video30FPS ≈350Kvisual tokens/phút
(pre-compression)

- TTFTgiờ là hàm củasốảnh,không phải
outputlength

- Visionencoder (ViT)khônghưởnglợi từ TP
—chậm đi ở TP=8

- Tách3pha: Encode (ViT)→Prefill →
Decode,scale độc lập

- SGLang2E1P: ∼6–8×TTFT↓trên
Qwen3-VL-235B

- vLLMv0.11+: --mm-encoder-tp-mode data
(encoderdisagg)

- CPUAMX encode song song GPU
prefill/decode(Xeon) Multimodal prefix caching — Hash trên pixel/image-embedding (SHA-256) → cachehit: 18s →1sTTFT(LMCache). Early-fusion(Llama4)bỏluônencoderstage riêng. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 26 / 40

---

<!-- chiron-source-span: {"source_span_id":"6100b51b-8744-51ba-a66c-e82940c7fd5f","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Embedding& Reranker Serving: The Retrieval Half","extraction_method":"pdf-text-layer"},"checksum":"4db64990f20fea47863fbb3412e892dcfd7fa3278106820e6e2bfaaa9761b744"} -->

## Slide 29 - Embedding& Reranker Serving: The Retrieval Half

- Prefill-bound: 1 forward pass,khôngKV
cache,khôngdecodeloop

- Throughputqua largestatic batch
(token-sorted),không phải continuous batching

- Cross-encoderreranker: chấm điểm(query,
doc)— nặng hơn bi-encoder embedding

- FP8: ∼50%throughput ↑ở >99%cosine
similarity

- HFTEI:Rust, phục vụ cả embedding+
reranker(Qwen3, ModernBERT)

- SnowflakeArctic Inference: 16×vLLM
(disaggtokenize + FP8)

- Models: Qwen3-Embedding-8B (MTEB rank
1),BGE-M3 (dense+sparse+ColBERT)

- MRL:cắt chiều embedding linh hoạt;late
chunkinggiữ context Lưu ý:RAG/agent inference =một nửa là retrieval. Self-host break-even∼50–100M tokens/tháng so với API (OpenAI/Voyage). Giảngviên (VinUni) AICB· Ngày 20 Tuần4 27 / 40

---

<!-- chiron-source-span: {"source_span_id":"7386b6e0-5b4b-5557-a821-3518dfc2f109","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"SemanticCaching: The StackIs 3 Caches Deep","extraction_method":"pdf-text-layer"},"checksum":"8da65a66aeae6b2242d832a3a488d7723ec76b196a69c9fd66b7f5a2e9af969d"} -->

## Slide 30 - SemanticCaching: The StackIs 3 Caches Deep

- 1. Semantic cache(meaning-based): hit→
100%compute saved

- 2. Prefix / KVcache: hit→skipprefill cho
sharedprefix

- 3. Full inference: cache miss hoàntoàn

- Semantic= embed prompt→vectorsearch →
trảresponse cũ nếu sim>threshold

- Hitrate thực: 30–68%FAQ/support,
10–25%open-ended (“95%” là marketing)

- vCache(ICLR’26): threshold thích ứng
per-prompt+ error bound

- AWSElastiCache+Bedrock, Azure APIM
llm-semantic-cache

- Bảomật: cache-poisoning (NDSS’26
∼90%)+ KV timing side-channel Takeaway — Semanticcacheđứng trênKVcache—bắtđượccâuhỏi paraphrase, khôngchỉexactprefix. Đổilại: staleanswers+collisionrisk →đặtthresholdcẩnthận, saltcache per-tenant. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 28 / 40

---

<!-- chiron-source-span: {"source_span_id":"01c40f94-80e5-51b2-83ca-19d3f677ffbe","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"ModelRouting & Cascades: Cross-Model Cost","extraction_method":"pdf-text-layer"},"checksum":"2e96aa4e6bd9763c3fbcea346dba2109ad874b7b34b498aa9ac906e9546fc270"} -->

## Slide 31 - ModelRouting & Cascades: Cross-Model Cost

- Routing(pre-generation): classifier chọn
modeltrướckhisinh

- Cascade: chạy model rẻtrước,deferlên
modelmạnh khi confidence thấp

- RouteLLM(ICLR’25): −85%chi phí GPT-4
ở95% MT-Bench

- FrugalGPT:cascade match GPT-4ở −98%
cost

- nano(∼$0.10/M)classify →mid($1–3/M)
draft →frontier($10–15/M)hard tail

- −60–80%cost, <5%routing latency

- AzureAI Foundry Model Router (GA),
OpenRouterAuto

- 2026: pre-genrouting >cascade(cascade
trảtiền sinh model rẻ trướckhi defer) Costlever — Routinglà đònbẩychiphílớnnhấtởservinglayer —khôngphải mọi query cần frontier model. Reasoning model tốn 13–25× energy/query → route “easy”sang model nhỏ. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 29 / 40

---

<!-- chiron-source-span: {"source_span_id":"e897054a-07f5-5fe9-868e-353ba045d13c","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Tokens-per-Joule& The Power Wall","extraction_method":"pdf-text-layer"},"checksum":"88dacecc039bf68eb4cbf49162c4abf9c614e5d5eaf81c28de23006cce8a34c3"} -->

## Slide 32 - Tokens-per-Joule& The Power Wall

- GB200NVL72 120–132kW/rack;GB300
135–150kW;VeraRubinNVL144 ∼190kW

- Datacenterđiện: IEA dựbáo ∼485 →950TWh
(2025→2030)

- Tokens-per-joulegiờlà first-class metric
(MLPerfPower v5.1)

- Medianthực: ∼0.31Wh/query (ước tính cũ thổi
phồng4–20 ×)

- FP8 ∼ −30%energy (ở batch≥64);FP4
25–50×vsH100 FP16

- MoEsparsity: GPT-OSS-20B−26%
energy/1Ktok vs dense 32B

- GreenLLM:phase-specific DVFS,
−10–34%energy, <3.5%SLO miss

- Carbon-awaretemporal shifting: bùtới
∼70%carbon Lưu ý: Reasoning model (15× tokens) → median energy 0.31→ 3.91Wh/query (13×). Power, không phải FLOPs,là ràng buộc scale 2026. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 30 / 40

---

<!-- chiron-source-span: {"source_span_id":"41a890ed-6552-5e07-8b5b-ecbc1acd8c8c","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"ConfidentialInference: TEE &the Attack Surface","extraction_method":"pdf-text-layer"},"checksum":"3e910414f17e9b34f3cd35561852da700ebe3c911d470b0fd2e7d1e67312add2"} -->

## Slide 33 - ConfidentialInference: TEE &the Attack Surface

- TEEtrên GPU: data mã hoácả khi đang tính
(in-use)

- HopperPPCIE(8-GPU HGX, 2025) — nhưng
NVLinkplaintext

- Blackwell: NVLink encryption +TEE-I/O
(multi-GPUmã hoá đầu tiên)

- Overhead: <9%throughputmodel lớn (∼0%
Llama-70B), ∼19%TTFT

- KVtiming side-channel(PROMPTPEEK,
NDSS’25): 99% reconstruct promptqua TTFTprobing trên shared APC

- StanfordICML’25: 7/8caching API chia sẻ
cachecross-user

- Mitigation: cachesalting per-tenant
(vLLM),SafeKV

- ZK-proofinference vẫn chậm 104–105×
Khi nào cần— Regulated industry (y tế, tài chính, chính phủ) — giờ khả thi với <9% overhead. Kết hợp prefix-cache: bật cache salting để chặn cross-tenant KV leak. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 31 / 40

---

<!-- chiron-source-span: {"source_span_id":"6a3576f8-fada-5c3b-8500-b0438396f643","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Auto-scalingArchitecture","extraction_method":"pdf-text-layer"},"checksum":"6d8e55214f4cbe668ab13940861c082d9047ff2bdaa95b57b6276b63be8def47"} -->

## Slide 34 - Auto-scalingArchitecture

Clients (100 RPS) Load Balancer GPU1 GPU2 GPU3 GPUN (auto) KEDA Autoscaler GPU util>80%: scale out Queue depth>10: scale out GPU util<30%: scale in Least-busyrouting Giảngviên (VinUni) AICB· Ngày 20 Tuần4 32 / 40

---

<!-- chiron-source-span: {"source_span_id":"550ce3cd-0705-5082-95a0-51d2b6d721b2","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"ScalingStrategies","extraction_method":"pdf-text-layer"},"checksum":"254c78d34cfe690b37bf7ae85a246c990f4c9baa4322ebfcd8ba0c306a8cca3b"} -->

## Slide 35 - ScalingStrategies

- GPUutilization >80%: scale out

- Queuedepth >10requests

- KEDA+ Knative: Event-DrivenAutoscaling

- Scale-to-zero: 0 replicas khino traffic— tiết
kiệmchi phí đáng kể

- Least-busyrouting: +30% vsround-robin

- Requestbatching: 50ms window,+40%
throughput

- Warmpool: Nidle instances cho spikes

- Trade-off: cost vscold start latency
Giảngviên (VinUni) AICB· Ngày 20 Tuần4 33 / 40

---

<!-- chiron-source-span: {"source_span_id":"ba03a8f4-ed59-50d5-9000-08305692d02f","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"EdgeDeployment Flow","extraction_method":"pdf-text-layer"},"checksum":"b9db5c20523972c8496fd80a1fda06841a87cade7a3d274edc4b418db73a0638"} -->

## Slide 36 - EdgeDeployment Flow

PyTorch Model ONNX Export GGUF (llama.cpp) TensorRT (NVIDIA) Ollama (Container) GPU Server Edge / Laptop 3–5× faster FP8/INT8 calibration GGUF Q4_K_M Llama-3, Qwen-3, Phi-3 GGUFLevels: Q2_K(extreme, quality drop)· Q4_K_M(recommended) ·Q6_K (near-lossless) · Q8_0 (maxquality) Models: Llama-3-8B,Qwen-3-8B, Phi-3-mini | Ollama: ollama run llama3 —1 lệnh duy nhất Giảngviên (VinUni) AICB· Ngày 20 Tuần4 34 / 40

---

<!-- chiron-source-span: {"source_span_id":"133101cc-96da-5594-9374-e9086771926e","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"HardwareLandscape 2026: BeyondH100","extraction_method":"pdf-text-layer"},"checksum":"280fbe043cd227b322f6d8e3ed9bf7b1bfc592410b99ce06fb294c9737b7fabf"} -->

## Slide 37 - HardwareLandscape 2026: BeyondH100

Chip FP4/FP8peak Memory Niche/ 2026 Status NVIDIAH200 SXM FP8(no FP4) 141GB HBM3e Cost-effectivebaseline; +43% decode vs H100 NVIDIAB200 9PFLOPS FP4 192GB HBM3e FP4native; GB200 NVL72 = 72-GPUNVLink domain NVIDIAB300/GB300 15PFLOPS FP4 288GB HBM3e BlackwellUltra —currentgold standard NVIDIAVeraRubin 50PFLOPS NVFP4 288GB HBM4 Productionat CES’26; ships H2’26 AMDMI355X 20PFLOPS FP4 288GB HBM3e B200parity (MLPerf v6.0); GA Oct’25 GoogleTPU v7 4,614TFLOPS FP8 192GB HBM3e Ironwood;powers Anthropic Claude AWSTrainium3 2.52PFLOPS FP8 144GB HBM3e GADec’25; ∼50%cost cut (Uber) Lưuý: HBMbandwidth,khôngphảiFLOPs,làbottleneck —nguồncungHBM2026sold

### out; memory bandwidth quyết định decode throughput. Frontier labs đa dạng hoá silicon
Anthropicchạy Claude trên Google TPUv7 Ironwood + AWSTrainium,không chỉ NVIDIA. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 35 / 40

---

<!-- chiron-source-span: {"source_span_id":"47b30506-f6c0-509b-b864-cd02ec0c1d2b","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"SLADashboard: Key Metrics","extraction_method":"pdf-text-layer"},"checksum":"31e69a622a82bb04cc941c1603d3946a7b90caf0171ad46c7841115c9b1e2db8"} -->

## Slide 38 - SLADashboard: Key Metrics

120ms P50Latency Target: <200ms 380ms P95Latency Target: <500ms 850ms P99Latency Target: <1000ms 1,800 tokens/sper GPU Benchmark: k6/locust 99.9% Uptime =8.7h downtime/year Giảngviên (VinUni) AICB· Ngày 20 Tuần4 36 / 40

---

<!-- chiron-source-span: {"source_span_id":"4b59d46f-b606-5b29-a310-77f5f3af7667","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"ProductionSLA: Best Practices","extraction_method":"pdf-text-layer"},"checksum":"b2ebcd18eb706efb9b0478c12c166aaf6bf8ac6ff7e28ffcfe3323760dd52e33"} -->

## Slide 39 - ProductionSLA: Best Practices

- Multi-AZdeployment + health checks

- Timeout10–60s cho LLM generation

- Circuitbreaker: fallback khioverloaded

- Gracefuldegradation: trả cached/shorter
response,route sang smaller model

- Costper 1M tokens: liên tục optimize

- Spotinstances cho batch inference

- Scale-to-zerokhi no traffic(KEDA)

- Right-sizeGPU: đừng dùng A100 cho7B
Lưuý: Benchmarkvới locust/k6trướckhiproduction. Không đoánlatency — đo thực tế. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 37 / 40

---

<!-- chiron-source-span: {"source_span_id":"385a8bd4-dcd0-58fb-ba03-3854faea1d37","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Lab20: Model Serving& Inference Optimization","extraction_method":"pdf-text-layer"},"checksum":"98454d85c8e42c4cdb5eaa8e8608b834ab8537bec934438110955a17a2396626"} -->

## Slide 40 - Lab20: Model Serving& Inference Optimization

Day20-Track2-ModelServing-Lab/—chạyđượctrênWindows/macOS/Linux,low- speclaptop OK

- 00-setup: hardware detection +
cross-platforminstall

- 01-quickstart: llama-cpp-python baseline
P50/P95/P99

- 02-server: OpenAI-compatllama-server +
Prometheus+ locust load test

- 03-milestone-integration: nối endpoint với
N16–N19

- llama.cpptuning: build flags
(AVX2/AVX-512,NEON), thread sweep, ctx-lensweep, GPU offload (Metal/CUDA/Vulkan),quant tradeoffQ2_K

- Q8_0

- MLX(macOS):Apple Silicon native runtime,
optional Lưuý: Low-speclaptop(8GBRAM,noGPU)?Vẫnchạyđượctoànbộcoretracks. Bonustrackhoạtđộngtrên mọiCPU— càng ”yếu” càng họcđược nhiều về tối ưu. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 38 / 40

---

<!-- chiron-source-span: {"source_span_id":"390b40a0-6498-5e7a-9382-9508eba01555","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"Milestone1: AI InfrastructurePlatform","extraction_method":"pdf-text-layer"},"checksum":"7f6e9aa386ddc4c8674bc3d1c2ba7ca42e8ca9a5eb768cf2f4a1445de5192261"} -->

## Slide 41 - Milestone1: AI InfrastructurePlatform

Tíchhợp N16–N19 thành coherent AI infrastructureplatform demo

1. Cloudsetup: IaC +K8s cluster

2. Datapipeline: ingestion +processing

3. Lakehouse: Delta Lake +Medallion

4. Vectorstore: semanticsearch API

5. Featurestore: online/offline

6. Modelserving: optimized endpoint

7. Benchmarkreport: latency +cost

8. Livedemo: end-to-end flow Lưuý: Submittrên LMS trước hết ngày. Demo live choinstructor trong lab session. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 39 / 40

---

<!-- chiron-source-span: {"source_span_id":"c9bc76d0-2776-5f37-845f-5e454e4ef131","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Chương4 Recap: HạTầng AI","extraction_method":"pdf-text-layer"},"checksum":"f4f0d122a30e0fec46789f2fb0f05935712f8a48c5a2ffe813656ee654e9494b"} -->

## Slide 42 - Chương4 Recap: HạTầng AI

Cloud Infra Data Pipelines Lakehouse Vector & Feature Model Serving N16 N17 N18 N19 N20 Common mistakes:Skip validation→ data quality issues · No time travel→ no rollback · Static batching→ poor throughput Giảngviên (VinUni) AICB· Ngày 20 Tuần4 40 / 40

---

<!-- chiron-source-span: {"source_span_id":"fb310a2b-c4a1-579e-9971-6ceb7005fd04","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"8f6f18cba5be7f54adfb96819d380d74df8be94cd5cac4e7d324b0203d1b13b7"} -->

## Slide 43 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 Quantization 2026: FP8/NVFP4 (Hopper+/Blackwell) cho production cloud, AWQ 4-bit cho general,GGUF Q4_K_M cho edge. 2 Serving 2026: vLLM v1 + SGLang core;P/D disaggregation(Dynamo 1.0 / llm-d) là default ở scale; serving giờ gồm cả VLM, embedding, semantic cache, routing, power & confidential inference. 3 Goodput@SLO(khôngphảithroughput@peak)quyếtđịnhproductionsuccess—benchmark P50/P95/P99trước khi deploy. Giảngviên (VinUni) AICB· Ngày 20 Tuần4 40 / 40

---

<!-- chiron-source-span: {"source_span_id":"df2be274-e1fe-5300-b413-9dd504c7a759","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"9e9f33eea9b498fb4cb5584adb147b333f9e9febdef16d8d2de847223acc5a9f"} -->

## Slide 44 - Tiếptheo & Bài tập

Chương5: CI/CD forAI Systems “Từ hạ tầng sang vận hành — deploy AImodels an toàn, tự động, liêntục.”

- SubmitMilestone 1 đúng
deadline

- Đọctrước: MLOps Principles—
GoogleCloud

- Càisẵn GitHub Actions runner

---

<!-- chiron-source-span: {"source_span_id":"7ecee04b-53d0-5577-b364-401d6be44c99","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"3b5ab18ca6657606c9aa1915cd537081685e925e1eea99e991d5252a77abb103"} -->

## Slide 45 - Hỏi& Đáp

Câu hỏi nào về Quantization, vLLM/SGLang, SLA, hay Milestone 1?

---

<!-- chiron-source-span: {"source_span_id":"3024710a-ae9d-5a0a-8e83-31b73292954e","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"1517c7877ae7c60f868a463750358d44857c6e6f500d4823dd339949de992966"} -->

## Slide 46 - Cảmơn!

AICB-P2T2 · Ngày 20 Model Serving & Inference Optimization lms.vinuni.edu.vn · Slide & template trên LMS
