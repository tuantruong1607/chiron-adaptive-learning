---
schema_version: 1
course_id: rag-intensive
document_id: "c20a6706-afb1-52d2-9f05-e4c2d699b1e4"
document_version_id: "f65a73cf-2488-5beb-8c86-ae5b2b9be954"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Fine-tuning LLMs — Từ Full Fine-tuning đến LoRA/QLoRA"
source_file: "track 3 - day 21.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 21.pdf"
source_sha256: "3e89c9a32b4de56d91cbc48216dc9580678098e7dba4e08903b1dd9bcfc941b9"
parser_version: chiron-structured-markdown-v1
page_count: 31
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":31}"
language: vi
---

# Fine-tuning LLMs — Từ Full Fine-tuning đến LoRA/QLoRA

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"4d8ac652-8808-5893-b264-2040bd70ce94","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Fine-tuning LLMs — Từ Full","extraction_method":"pdf-text-layer"},"checksum":"7104a53bbda6c3fdc903e3ee57093a6dfd92e6ea497769357236b7dd045354da"} -->

## Slide 1 - Fine-tuning LLMs — Từ Full

Fine-tune đến LoRA/QLoRA AICB-P2T3 · Ngày 21 · Chương 5 — Fine-tuning & An Toàn NguyễnKhánh Linh VinUniversity · Phase 2 · Track3 ·Tuần5

---

<!-- chiron-source-span: {"source_span_id":"0fbbc756-d9d8-5978-ac91-70efe97d2a0b","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"03a49cfcd29db9c320120481c29f27b86be097e9e1f69edddd3456db6393d659"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “Khi nào nên fine-tune — và khi nào prompt engineering đủ rồi?” Giữcâu hỏi này trong đầu khihọc bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"aa844012-b780-585a-b706-6a7ad8f9b549","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nộidung bài học","extraction_method":"pdf-text-layer"},"checksum":"93099e7898d5cb1a3e6995f3c5122eb69cddec99484e680a1da041903b834672"} -->

## Slide 3 - Nộidung bài học

1. Khinào cần Fine-tune?

2. LoRA— Cơ chế hoạt động

3. QLoRA— Fine-tune trên GPU nhỏ

4. Dataset& TrainingPipeline

5. Demo& Thực hành NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 1 / 21

---

<!-- chiron-source-span: {"source_span_id":"584890fa-1dfa-557f-bec1-6cfdd2e06ce3","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Khi nào cần Fine-tune?","extraction_method":"pdf-text-layer"},"checksum":"5d9a6db0459c1c9c66fc4b4980a6b3bac5149354c7f6177e6dec60aa7190b7b7"} -->

## Slide 4 - Khi nào cần Fine-tune?

01 Prompt Engineering đã đủ chưa — hay cần huấn luyện thêm?

---

<!-- chiron-source-span: {"source_span_id":"980ea298-4a53-5a5c-9c7b-c9ba27e6fe6d","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Bốicảnh 2025–2026: FrontierModels đủ tốt?","extraction_method":"pdf-text-layer"},"checksum":"d3666dafcca5ed58b6140a2ff63f3fb57025d4636fc8d6ac492a9ce5b5baadd0"} -->

## Slide 5 - Bốicảnh 2025–2026: FrontierModels đủ tốt?

PromptEng. RAG Fine-tune khôngđủ? vẫnthiếu? 80%+ tasks giải quyết được Thêm knowledge cập nhật liên tục Style, format, latency, cost

- Frontiermodels (GPT-4o,Claude
3.5,Gemini 2) đủ tốt chohầuhết tasks

- Fine-tunechỉ khi thực sự cần:
formatriêng, domain jargon, giảm costat scale

- Modeloptions: Qwen2.5-7Bhoặc
Gemma-2-9B Lưu ý: Fine-tune KHÔNG fix knowledgegaps—dùngRAGcho knowledge. Fine-tune fixstyle và format. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 2 / 21

---

<!-- chiron-source-span: {"source_span_id":"c9822985-2798-59b6-9178-72bde2b914ba","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"DecisionTree— Prompt vs RAGvs Fine-tune","extraction_method":"pdf-text-layer"},"checksum":"b15399a908048f9645cf9fd8df3019c7057f7acf472d86fa81797ff9c1508bdf"} -->

## Slide 6 - DecisionTree— Prompt vs RAGvs Fine-tune

Few-shotprompt đạt80%+ accuracy? Promptđủ rồi Cầnknowledge mới/ cập nhật? DùngRAG Volume> 50k/day hoặclatency-critical? Fine-tune ROIpositive APIfine-tune (OpenAI/Anthropic) Có Không Có Không Không Có Prototype bằng prompting, đo gap. Nếugap > 15% và volume > 50k req/day⇒ fine-tuningcó ROI dương. Luôn thử prompt→RAGtrước khi tới fine-tune. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 3 / 21

---

<!-- chiron-source-span: {"source_span_id":"e5249357-42e4-5118-88da-84dde86f2bc1","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"APIFine-tuning vs Self-hosted LoRA/QLoRA","extraction_method":"pdf-text-layer"},"checksum":"1805f737821e6fe188558cdcef929f348019022b023aacab88e98253307d5633"} -->

## Slide 7 - APIFine-tuning vs Self-hosted LoRA/QLoRA

Tiêuchí APIFT (OpenAI/Anthropic) Self-host LoRA/QLoRA Inframanagement Khôngcần — managed Tựsetup GPU + pipeline Control Hạnchế (hyperparam) Toànquyền(rank, layers, data) Costper token Cao($$$) Thấpkhi volume lớn Latency Mạng+ queue Self-hostvLLM, sub-200ms Dataprivacy Gửiqua API provider On-premhoàn toàn Timeto production Vàigiờ Vàingày Prototype nhanh, volume nhỏ–vừa, không có team ML ops, dữ liệu non- sensitive. Volume >50k/day, dữ liệu nhạy cảm, cần custom rank/layers, cần multi- tenantadapters. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 4 / 21

---

<!-- chiron-source-span: {"source_span_id":"827741ae-9b34-5338-8f0c-7140a6b53f9d","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"LoRA — Cơ chế hoạt động","extraction_method":"pdf-text-layer"},"checksum":"289461a74811f2d3736771ee100b3675530731038b68df83249b65bfcc6aac94"} -->

## Slide 8 - LoRA — Cơ chế hoạt động

02 Low-Rank Adaptation: thêm ghi chú vào sách, không sửa sách gốc

---

<!-- chiron-source-span: {"source_span_id":"03bd5c2f-56bb-5261-9157-6ae2ed043528","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Ýtưởng cốt lõi","extraction_method":"pdf-text-layer"},"checksum":"b41cd4ad577ec3ae5915da00e531c6f81f2370107ee51419a6ec3c7efdbd162b"} -->

## Slide 9 - Ýtưởng cốt lõi

LoRA(Hu et al. 2021) Freeze toàn bộ base weights (hàng tỷ tham số), chỉ inject thêmlow-rank update ∆W =B ·A—train phần rất nhỏ tham số. Analogy: LoRAgiống thêmstickynotesvàosáchgiáokhoa —khôngsửasách gốc,chỉthêmghichúnhỏ. Khideploy,“dán”ghichúvàosách ⇒zeroaddedlatency. Inference: merge adapter vào base weights:W = W0 +B ·A — không tốn thêm thờigian khichạy. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 5 / 21

---

<!-- chiron-source-span: {"source_span_id":"464a37ab-4249-59fc-b9a5-c907c7a05dde","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Kiếntrúc LoRA — Frozen Weights+ Adapters","extraction_method":"pdf-text-layer"},"checksum":"d36e8f88b5be951e5ade0b48b5cce629b272efa24fe17a51e921ff634f5afa65"} -->

## Slide 10 - Kiếntrúc LoRA — Frozen Weights+ Adapters

x W0 (frozen) A d ×r B r ×k h + Hàng tỷ tham số Rank r (≪ d) Không update khi training Chỉ train A và B

### Toánhọc
h =W0x +B ·A| {z } ∆W ·x Rankr ≪ min(d,k). Thường r ∈ {8, 16, 32, 64}. lora_alpha/r = 1 hoặc 2. Alpha cao ⇒ adapter ảnh hưởng mạnhhơn.

### Targetlayers (2025 best practice)
ALLattention + MLP layers q_proj + v_proj alonethiếu capacity NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 6 / 21

---

<!-- chiron-source-span: {"source_span_id":"a1b506ae-011c-5633-b2ab-f4790b29c1a3","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"RankrvsAccuracy — Trade-off","extraction_method":"pdf-text-layer"},"checksum":"d68a896be1faf86a4de0ee4be3803f483101d8db9e26963d7a5ef803e8e76be5"} -->

## Slide 11 - RankrvsAccuracy — Trade-off

r=8 0.1% params Nhẹ, tiết kiệm r=16 Standard Cân bằng tốt r=64 Near full FT Tốn VRAM hơn Bắt đầur = 16. Nếu accuracy chưa đủ⇒ tăng lên 32, 64. Nếu VRAM hạn chế⇒ giảmxuống 8. Variantsmới: DoRA,rsLoRA—cải thiện nhẹ, cùng nguyên lý. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 7 / 21

---

<!-- chiron-source-span: {"source_span_id":"48995b70-939c-5397-b420-671f19e7a968","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"QLoRA — Fine-tune trên GPU","extraction_method":"pdf-text-layer"},"checksum":"92ef814747e288ef951f10ab6289d11feca0b78ce9ec7e51832dcd22f36468bd"} -->

## Slide 12 - QLoRA — Fine-tune trên GPU

03 nhỏ 4-bit quantization + LoRA = huấn luyện 7B trên RTX 3090

---

<!-- chiron-source-span: {"source_span_id":"e6565e78-1940-58e9-855d-7b5ef31e205b","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"QLoRA— 4-bit NF4 + LoRA Adapters","extraction_method":"pdf-text-layer"},"checksum":"8a04a5d4983106cb97b8769c1e91dc2175d0f55a003f54fc291ec6563966c8b0"} -->

## Slide 13 - QLoRA— 4-bit NF4 + LoRA Adapters

BaseModel 4-bitNF4 (frozen) LoRA bf16adapters PagedAdamW CPUoffloadkhi OOM MergedModel deploy-ready forward VRAM giảm ∼3× vs fp16 QLoRA (Dettmers et al. 2023) — Quantize base model xuống 4-bit NF4, thêm bf16 LoRA adapters. Chỉ train adapters.

- PagedAdamW:offloadoptimizer
statessang CPU RAM khi GPU hếtbộ nhớ

- Doublequantization: quantize cả
quantizationconstants — tiết kiệm thêm

- Qualitydrop: chỉ ∼2–5%vs LoRA
16-bit NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 8 / 21

---

<!-- chiron-source-span: {"source_span_id":"3897188a-0a35-5075-8e81-bd752baebfc6","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Sosánh chi phí: Full FT vs LoRA vs QLoRA","extraction_method":"pdf-text-layer"},"checksum":"42e1c62febc602335db03d1ad9e58f89f3133d0afd6f1de3e588b1e58ecad6c6"} -->

## Slide 14 - Sosánh chi phí: Full FT vs LoRA vs QLoRA

Phươngpháp VRAM (7B) Params train Thời gian GPU tối thiểu FullFine-tune ∼60GB 100% $$$$ A10080GB LoRA(fp16) ∼28GB ∼1% $$ A10040GB QLoRA(4-bit) ∼10GB ∼1% $$ RTX3090 24GB Train QLoRA → merge adapter → quantizeGGUF/AWQ →deployvLLM /llama.cpp 1 base model + nhiều LoRA adapters

- serve nhiều domains cùng lúc trên
1GPU NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 9 / 21

---

<!-- chiron-source-span: {"source_span_id":"6272b25a-fa62-53fa-b267-96e9dfff8afd","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Dataset & Training Pipeline","extraction_method":"pdf-text-layer"},"checksum":"9adb6a6d721da6bb247ccbd97bba97c74de8d83d6375604b1f2be4a9085f456d"} -->

## Slide 15 - Dataset & Training Pipeline

04 Từ chuẩn bị dữ liệu đến chạy training với Unsloth + TRL

---

<!-- chiron-source-span: {"source_span_id":"709f56a9-ae7f-5852-91c9-1f3b3b746d6e","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"DatasetPreparation — Quality over Quantity","extraction_method":"pdf-text-layer"},"checksum":"1127289ae7d88502ae4e3c60e1a8199698b07fe322d6541684756410305a1413"} -->

## Slide 16 - DatasetPreparation — Quality over Quantity

RawData Clean& Dedup Format(Alpaca/ChatML) Train/ ValSplit Remove short outputs, filter templates, dedup Match model template (instruction/input/output)

### Quymô cần thiết

- Style/format: 500–2ksampleschất
lượngcao

- Domainadaptation: 10k+samples

- Rule: 500perfect > 10k noisy
Lưu ý: Data contamination: verify testsetKHÔNGoverlaptrainingdata. Đâylà“silentkiller”củaevalreliability. Syntheticdata: GPT-4Evol-Instructcho 10×expansion. Cẩnthận modelcollapse nếulạm dụng. Distillation: generate training datatừ strong model (GPT-4,Claude) →fine-tuneweaker model. Hiệuquả — nhưngkiểmtra ToScủaprovider trước. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 10 / 21

---

<!-- chiron-source-span: {"source_span_id":"6360467f-a342-5173-bebf-f72e79b859c7","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"TrainingPipeline — Full Workflow","extraction_method":"pdf-text-layer"},"checksum":"b00d6b06e1af979e9581b2bcb0bd9a3a1eb10ae4ca5d43859927a46de0c481bd"} -->

## Slide 17 - TrainingPipeline — Full Workflow

1. Dataset Prep& Clean

2. Config PEFT+ QLoRA

3. Train Unsloth/TRL

4. Eval Merge& Deploy Alpaca/ChatML dedup, balance r=16, alpha=32 target_modules lr=2e-4, cosine packing=True Merge adapter GGUF → vLLM Model + Optimizer + Activations + Gradients. QLoRAgiảm ∼60%vs full fp16. Flash Attention 2: bắt buộc — 2–4× speedup. RTX3090 (24GB):7B QLoRA A100(40GB):13B QLoRA H100(80GB):70B QLoRA Grad. checkpoint: −60%VRAM, +20%time NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 11/ 21

---

<!-- chiron-source-span: {"source_span_id":"5df9e110-9626-512c-997a-bc276f242f8b","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"TrainingInfrastructure — VRAM Math& Practical Settings","extraction_method":"pdf-text-layer"},"checksum":"2e8880b9d693032190fd067ab6bc49ef50249dc3f1ce86929f7bbc8e897b0910"} -->

## Slide 18 - TrainingInfrastructure — VRAM Math& Practical Settings

### VRAMbudget breakdown
Vtot =Vmodel +Voptim +Vact +Vgrad

- FlashAttention 2: bắt buộc —2–4×
speedup,giảm activations memory đángkể

- Gradientcheckpointing: recompute
activationskhi backward → −60% VRAM, +20%time

- QLoRA +FlashAttn 2 +grad
checkpoint ⇒ ∼10GB cho7B model Phân tích token distribution của dataset → set max_seq_length = p95. Tránhpadding lãngphí. batcheff =batch ×grad_accum Khi VRAM hạn chế: batch=1, grad_accum=4--8 Mụctiêu: batcheff ∈ [16, 64] Lưuý: OOMdebugging: giảm max_seq_lengthtrước,sauđóbậtgradcheckpointing, cuốicùng giảm rank. Đừng chỉ giảm batch size —ảnh hưởng convergence.NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 12 / 21

---

<!-- chiron-source-span: {"source_span_id":"f12cd97a-04c3-5d7c-b9da-43be9b7993ef","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"FlashAttention— IO-AwareExact Attention","extraction_method":"pdf-text-layer"},"checksum":"590ef73c00880c608a44d8b7a46eaaa20621386599c5a115cd4416e27e055981"} -->

## Slide 19 - FlashAttention— IO-AwareExact Attention

Daoet al. 2022,FA2(2023), FA3(2024) Vanillaattentionđọc/ghimatrận N ×NquaHBM(slow) ⇒memory-bound. FlashAt- tention dùngtiling + recomputation: tải block nhỏ vào SRAM (on-chip,∼20 MB nhưng ∼10×nhanh hơn HBM), tính softmax theo từng block, tránh materialize ma trậnattention N ×N. Kết quả: exact attention(không xấp xỉ) — nhưng2–4× nhanh hơnvà memory O(N)thayvì O(N2). NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 13 / 21

---

<!-- chiron-source-span: {"source_span_id":"e05321e0-18c7-534c-b1c7-0e45d6578605","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"FlashAttention— Memory Hierarchy & Tiling","extraction_method":"pdf-text-layer"},"checksum":"ebe81f1ff68d73e49fca7102b3bbb0dfd455a714a93d128221ac2a7925a4c1df"} -->

## Slide 20 - FlashAttention— Memory Hierarchy & Tiling

SRAM(on-chip) ∼20MB · ∼19TB/s HBM(GPU memory) 40–80GB · ∼2TB/s DRAM(CPU RAM) >100GB · ∼50GB/s ∼10×nhanh chậmhơn chậmnhất Tiling: Q, K, Vchia khối nhỏ Qtile Ktile Vtile Otile Vìsao nhanh hơn?

- Vanilla: ghi matrậnN ×NvàoHBM

- memory-bound

- FA:streaming tiles qua SRAM→
compute-bound

- Backward: recomputeattentionthay
vìstore →tiếtkiệm activation memory FA1(2022): tiling cơ bản FA2(2023): betterparallelism, +2× speed FA3(2024): HopperTMA,FP8,cho H100 NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 14 / 21

---

<!-- chiron-source-span: {"source_span_id":"4fcb46c8-98ae-5e40-b3d6-b1e12096b76c","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"FlashAttention— Khi nào dùng & Cáchbật","extraction_method":"pdf-text-layer"},"checksum":"5c58fdd1af3408efe49c19b71850d059a18b48d4948322fa5f72d8bb18b9d763"} -->

## Slide 21 - FlashAttention— Khi nào dùng & Cáchbật

### Hardwarerequirements

- Ampere+: A100, RTX30xx,RTX
40xx(FA2OK)

- Hopper: H100, H200 (FA3mới nhất,
FP8)

- Khônghỗ trợ: V100, T4 (chỉTuring)

### Sequencelength sweet spot

- Short( <512): speedup nhỏ, vẫnnên
bật

- Medium(1k–4k): 2–3×speedup

- Long(8k+): 4×+speedup,memory
tiếtkiệm rất lớn

### Cáchbật trong code
from_pretrained( ..., attn_implementation= "flash_attention_2" ) TựđộngbậtFA2ngaykhiloadmodel 4-bit. Không cần config.

```text
Install: pip install flash-attn --no-build-isolation
(cầnCUDA toolkit + nvcc, build∼10phút)
```
Lưu ý: Common pitfall: nếu thấy ”flash_attn not installed” warning → Hug- gingFace fallback về SDPA (chậm hơn 2×). Luôn verify FA đã active bằng model.config._attn_implementation. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 15 / 21

---

<!-- chiron-source-span: {"source_span_id":"7025f2ef-4f88-58cb-ba48-3022f800df77","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Unsloth+ TRL SFTTrainer— ProductionSetup","extraction_method":"pdf-text-layer"},"checksum":"97f753f2932232350b8b849049abd8d98e73f187c335e87b06d5c7e81092eb4d"} -->

## Slide 22 - Unsloth+ TRL SFTTrainer— ProductionSetup

```text
from unsloth import FastLanguageModel
from trl import SFTTrainer
model, tok = FastLanguageModel.from_pretrained(
```
"unsloth/Qwen2.5-7B-bnb-4bit", max_seq_length=2048, load_in_4bit=True) model = FastLanguageModel.get_peft_model( model, r=16, lora_alpha=32, target_modules=[ "q_proj","k_proj", "v_proj","o_proj","gate_proj", "up_proj","down_proj"]) trainer = SFTTrainer( model=model, train_dataset=dataset, dataset_text_field= "text", packing=True) # 2x throughput trainer.train()

### Keysettings

- Unsloth: custom CUDA kernels
—2 ×faster,60% less VRAM

- packing: gộp samples vào1
sequence— 2×throughput

- LR: 2e-4 → 5e-5,cosine schedule

- Warmup: 5–10% totalsteps
Lưu ý:Overfitting: eval loss tăng + train loss giảm⇒ dừng train- ing,giảm epochs hoặc tăng data. NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 16 / 21

---

<!-- chiron-source-span: {"source_span_id":"84d32819-d8d6-59a0-8862-ab7278be955b","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Demo & Thực hành","extraction_method":"pdf-text-layer"},"checksum":"02f63e5d3f5a2655674e4ddbd8a9abba7024cfd825b538c29f91fb72fb9adb48"} -->

## Slide 23 - Demo & Thực hành

05 Xem fine-tuning hoạt động thực tế trên domain Việt Nam

---

<!-- chiron-source-span: {"source_span_id":"5e6c5564-8285-5ecc-8c11-a626b62bd39a","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Fine-tunetrên VietnameseDomain Dataset","extraction_method":"pdf-text-layer"},"checksum":"7cb01af87bdfd299f1382025f5b82821444f1fa8668979dc5add6f645e17611e"} -->

## Slide 24 - Fine-tunetrên VietnameseDomain Dataset

1. Dataset: 1k VietnameseQApairs (Alpaca format). Training: 3 epochs,∼25 minon A100

2. Before: base model trảlời generic. After: dùng domain terminology chính xác

3. LoRAadapter swap: loadkhác adapters cho khác domains — multi-tenant serving

4. GGUFdemo: merge adapter→convert →runllama.cpp — deployment ready NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 17 / 21

---

<!-- chiron-source-span: {"source_span_id":"8b7bb6db-6e8a-5975-80e3-e10a1ae357fd","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Lab#21","extraction_method":"pdf-text-layer"},"checksum":"a07c01991e27869185a54dada227bd3f0d8e07f225c5fdc27f820d19a93469b7"} -->

## Slide 25 - Lab#21

Mụctiêu: Fine-tuneQwen2.5-7BvớiLoRA/QLoRAtrêncustomVietnamesedataset (dùngUnsloth + TRL) Deliverable: LoRAadaptercheckpoint+evaluationreport: perplexitydelta,5qual- itativebefore/after examples, training cost — sosánh rankr = 8 vsr = 64 Thờigian: 2giờ NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 18 / 21

---

<!-- chiron-source-span: {"source_span_id":"f62012e2-6c6d-50ac-b013-2e590b727a65","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Lab21 — Các bước thực hànhchi tiết","extraction_method":"pdf-text-layer"},"checksum":"2032825016f9b9bc88be71f7a2620088e5240cc2667905296389c2b27beaaa52"} -->

## Slide 26 - Lab21 — Các bước thực hànhchi tiết

1. Dataprep (15p): chuẩn bị 100–500examples Alpaca format từ domain. Clean, tokenize,verify max_seq_length (p95),split 90/10 train/eval

2. ConfigurePEFT (10p): r=16, alpha=32,target q_proj+v_proj. Setup QLoRA 4-bit vớiUnsloth FastLanguageModel

3. Trainbaseline (40p): TRLSFTTrainer,3 epochs, packing=True,cosine LR, warmup10%. Monitor losscurve — detect overfitting (eval loss rising)

4. Rankexperiment (30p): train 2 thêmadapters vớir=8 và r=64 trêncùng dataset. Sosánh: training time,VRAM usage, eval perplexity,qualitativeoutput

5. Evaluate(15p): perplexity trên evalset,generate 20 test prompts, qualitatively comparefine-tuned vs base model

### GitHubrepo + evaluation report
(1) LoRA adapter checkpoints (3 ranks) (2) Bảng perplexity delta + training cost (3) 5qualitative before/after examples (4) Kết luận vềrank selection trade-off NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 19 / 21

---

<!-- chiron-source-span: {"source_span_id":"bb54ebc1-71a9-5e8f-9190-fa61d90aaf11","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Lab21 — Rank Experiment Worksheet","extraction_method":"pdf-text-layer"},"checksum":"2315e9ddd21336abd6489908c25d264ebb30fb09c2e01b3716d9c6ceab8f8cb5"} -->

## Slide 27 - Lab21 — Rank Experiment Worksheet

Cấuhình Traintime PeakVRAM Eval PPL Qualitative Base(no FT) — —? generic LoRAr = 8???? LoRAr = 16???? LoRAr = 64???? Rank nào cho ROI tốt nhất trên dataset của bạn? Khi nào tăng rank không còn cải thiệnperplexity (diminishingreturns)? Khi nào nênchọnr = 8 thayvì r = 16? NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 20 / 21

---

<!-- chiron-source-span: {"source_span_id":"f4ff5a97-9d34-5d53-b016-02e947fd0712","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"265a97b62a867c6b88097d594b0170c00cc581299e825aeebee2424cf60dbc4a"} -->

## Slide 28 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 QLoRAdemocratize fine-tuning — consumer GPU(RTX3090) đủ cho 7B–8B models 2 Datasetquality là yếu tố quantrọng nhất — 500 perfect >10k noisy 3 Sequencepacking là free 2×speedup— luôn bậtpacking=True 4 LoRAadapters are composable — servenhiều adapters cùng lúc trên 1base model NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 20 / 21

---

<!-- chiron-source-span: {"source_span_id":"4def24ca-ce67-54c9-afa9-8f68b2d5bcf2","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"be8276173a0fb44bf2a160d45d8e4b77bf14bdb9706c52b0fd3fe372e79c0c87"} -->

## Slide 29 - Tiếptheo & Bài tập

Ngày22: DPO, ORPO& Alignment “SFT dạy format — DPO/ORPO dạy alignment (helpful + safe). RLHF tốn kém— DPO có thể thay thế?”

- Hoànthành Lab 21: LoRA
fine-tune+ benchmark report

- Đọc: Rafailov et al. “Direct
PreferenceOptimization” (2023) NguyễnKhánh Linh (VinUni) AICB· Ngày 21 Tuần5 21 / 21

---

<!-- chiron-source-span: {"source_span_id":"b400ac6e-1034-5803-8d2f-03a5f78b4f2c","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"17d7b330832a5652fc67d9f2b9c3f59ecb69e94d2f9f87d3185080561872dd33"} -->

## Slide 30 - Hỏi& Đáp

Khi nào thì fine-tune thực sự cần thiết? Bạn có use case cụ thể nào muốn thảo luận?

---

<!-- chiron-source-span: {"source_span_id":"336f9e39-ac4c-5fe9-864a-8f46b4353d48","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"07a6ee4f973d04f2b27a063c96be8e66428ece783e0b71b8c3b0febdb62a5558"} -->

## Slide 31 - Cảmơn!

AICB-P2T3 · Ngày 21 · Fine-tuning LLMs — Từ Full Fine-tune đến LoRA/QLoRA github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn
