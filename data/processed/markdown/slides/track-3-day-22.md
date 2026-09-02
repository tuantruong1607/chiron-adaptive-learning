---
schema_version: 1
course_id: rag-intensive
document_id: "af71f010-8bb1-513a-a07f-3ceea040662f"
document_version_id: "15f90d7b-3a72-59bf-9cba-ae2ee56bff14"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "DPO, ORPO & Alignment — Từ"
source_file: "track 3 - day 22.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 22.pdf"
source_sha256: "536d9212105c1bfd6a465408e09aa872a6d1dbc9ac7455c53e1379e976eddea4"
parser_version: chiron-structured-markdown-v1
page_count: 64
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":64}"
language: vi
---

# DPO, ORPO & Alignment — Từ

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"f0ff3601-e436-5447-9928-8c80562d8ad2","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"DPO, ORPO & Alignment — Từ","extraction_method":"pdf-text-layer"},"checksum":"45c5fb8a26f6a8052ad78415dcda5dcea7773d5ee6b389b59aea691ec02c038b"} -->

## Slide 1 - DPO, ORPO & Alignment — Từ

SFT đến Preference Learning AICB-P2T3 · Ngày 22 · Chương 5 — Fine-tuning & An Toàn Giảngviên VinUniversity · Phase 2 · Track3· Tuần5

---

<!-- chiron-source-span: {"source_span_id":"96808014-74c1-5acc-9aa5-e01a5119c591","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"62a7ebf02bb5454167b0d4106d5b5f9a87986ccbdab30f616a2b22aaa0f41009"} -->

## Slide 2 - HÃYSUY NGHĨ...

? “RLHF tốn kém — DPO làm được điều tương tự mà không cần reward model?” Giữcâu hỏi này trong đầukhi học bài hôm nay

---

<!-- chiron-source-span: {"source_span_id":"eea51b6e-2dc2-5a6f-8352-13b410101b85","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nộidung bài học","extraction_method":"pdf-text-layer"},"checksum":"eef942c7149db842c17ebdbf449df5abd36e1e79199316d821d2d397da2279e8"} -->

## Slide 3 - Nộidung bài học

1. Tạisao SFT chưa đủ?

2. RLHF— Bức tranh toàn cảnh

3. DPO— Direct Preference Optimization

4. ORPO,SimPO & Alternatives

5. RLcomeback — GRPO & RLVR

6. PreferenceData & Implementation

7. ConstitutionalAI & Red-teaming

8. Đánhgiá Alignment — LLM Benchmarks

9. Demo& Thực hành

10. Bứctranh toàn cảnh — Full trainingflow Giảngviên (VinUni) AICB· Ngày 22 Tuần5 1 / 49

---

<!-- chiron-source-span: {"source_span_id":"e378896d-6aab-5667-85a6-305e53ff2a57","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Tại sao SFT chưa đủ?","extraction_method":"pdf-text-layer"},"checksum":"a7e18e61023f02f05e589dcaf3cf08c43637acef9e517f157ae59bf5119742cd"} -->

## Slide 4 - Tại sao SFT chưa đủ?

01 SFT dạy “nói gì” — nhưng ai dạy model “nói như thế nào”?

---

<!-- chiron-source-span: {"source_span_id":"03808a6f-c5a5-5a34-bcf3-27a56d22d210","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"SFTdạy format — Alignment dạyhành vi","extraction_method":"pdf-text-layer"},"checksum":"d7b29c7ba13a9e4c8a77e6ef1f6e607e2bb4892b4bfb7771c4a91a059c2cb3a7"} -->

## Slide 5 - SFTdạy format — Alignment dạyhành vi

Pre-trained (rawknowledge) SFT (format+ style) Alignment (helpful+ safe) instruction preference Biết nhiều, nói bừa Biết trả lời, chưa biết chọn Chọn câu tốt hơn

### Post-trainingpipeline hiện đại

1. SFT:Dạy model format câu trả lời (instructionfollowing)

2. Alignment: Dạy model phânbiệt tốt/xấu(helpful, harmless, honest) Practicalframing SFTdạy model “nói gì”. DPO/ORPO dạy model “nóinhư thế nào” — concise, helpful, an toàn. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 2 / 49

---

<!-- chiron-source-span: {"source_span_id":"dd270ae2-bfe7-5f12-9b79-048e5055e258","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"SFT-only: vấn đềgì xảy ra?","extraction_method":"pdf-text-layer"},"checksum":"a6b2f492411631f68ddc5bdcf8f8e325a97def58077caf0ac7c8965831d16cf1"} -->

## Slide 6 - SFT-only: vấn đềgì xảy ra?

SFT-onlyoutput Over-hedges,verbose Generic,không actionable Refusalquá mức AfterAlignment Direct,concise Actionable,helpful Balancedsafety Alignment — Quá trình dạy model phân biệt câu trả lờitốt vs xấu bằng preference data — không phải dạy thêmkiến thức mới.

### Kếtquả nổi bật
InstructGPT1.3BvớiRLHF >GPT-3175BkhôngRLHF ⇒ Alignment beats scale (Ouyanget al. 2022) Giảngviên (VinUni) AICB· Ngày 22 Tuần5 3 / 49

---

<!-- chiron-source-span: {"source_span_id":"917dad4a-eee0-592e-93ea-08343c42cb2c","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Vìsao preference data mạnh hơndemonstration data?","extraction_method":"pdf-text-layer"},"checksum":"5e31b2e4dce2f39b8eca1e24643827095479c11ac961f5fca679700318144b77"} -->

## Slide 7 - Vìsao preference data mạnh hơndemonstration data?

SFT distribution (data observed) desired SFT chỉ thấy “good” → không biết good hơn bad bao nhiêu SFT(demonstration): “Bắtchước câu này.” ⇒Họcdistributioncủadata. Preference(DPO/RLHF): “CâuA tốt hơncâuB.” ⇒Họcmargingiữagood vs bad. Informationsignal Một preference pair (yw, yl) chứa thôngtin vềcáigì KHÔNG nên nói —điềumàSFTdatakhôngbaogiờ biểulộ trực tiếp. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 4 / 49

---

<!-- chiron-source-span: {"source_span_id":"cbd52de5-7d10-526c-960d-316af47f6c88","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"RLHF — Bức tranh toàn cảnh","extraction_method":"pdf-text-layer"},"checksum":"6dbb737801415affa57e97045d05e7bdf9292a7a37ef46d097aab5404e8db785"} -->

## Slide 8 - RLHF — Bức tranh toàn cảnh

02 Hiểu RLHF để thấy tại sao DPO là bước cải tiến

---

<!-- chiron-source-span: {"source_span_id":"0d1d3dea-8984-545b-aec8-6ca2bd7a961e","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"RLHFPipeline — InstructGPT 3-Stage Architecture","extraction_method":"pdf-text-layer"},"checksum":"be6c6bed56a3590c438852466d973bdb9ec6f8fa43b086cbb95d4d0fb60cd734"} -->

## Slide 9 - RLHFPipeline — InstructGPT 3-Stage Architecture

Stage1 SFT (dạyformat) Stage2 RewardModel (humanrank pairs) Stage3 PPO (optimizepolicy) Training data cần chuẩn bị kỹ RM training unstable PPO hyperparams rất sensitive Lưu ý:RLHF pipeline phức tạp:3 models, 3 stages, nhiều hyperparams⇒chỉ frontier labs(OpenAI,Anthropic)cóđủresourcesđể dùng. Analogy RLHF =thuê giám khảo chấm điểm, rồi dùng điểm đó dạy lại modelchính. Tốn kémgấp đôi. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 5 / 49

---

<!-- chiron-source-span: {"source_span_id":"2da28f8e-85c5-574b-bdd1-75d4fb389c4d","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"RLHF:Kết quả tốt nhưng chiphí cao","extraction_method":"pdf-text-layer"},"checksum":"7d23382ae9d5f26693dda98b937f7de1ab001b74e7fde45b7c13535db924dd58"} -->

## Slide 10 - RLHF:Kết quả tốt nhưng chiphí cao

3 Models cần train đồng thời Cao PPO instability reward hacking $$$$ Chi phí tổng (infra + annotators) Câuhỏi then chốt Nếu ta có thểbỏ Reward Modelvà train trực tiếp trên preference data thì sao?⇒ Đóchính là ý tưởng củaDPO. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 6 / 49

---

<!-- chiron-source-span: {"source_span_id":"abd3491f-7313-5274-81b6-cae8960c15c9","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"DPO — Direct Preference Opti","extraction_method":"pdf-text-layer"},"checksum":"7a65899f4bdf6d4a7def6117944bc71e0e190617197ce0e1edb3eb9331a060e4"} -->

## Slide 11 - DPO — Direct Preference Opti

03 DPO — Direct Preference Opti- mization Bỏ Reward Model, train trực tiếp trên cặp tốt/xấu

---

<!-- chiron-source-span: {"source_span_id":"d422af56-3f81-5869-8898-172133d1827e","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Ýtưởng cốt lõi","extraction_method":"pdf-text-layer"},"checksum":"61b17f4c163f73c226943030cd4fc3286678be277155e1a995c3933ce90fb2d0"} -->

## Slide 12 - Ýtưởng cốt lõi

DPO(Rafailov et al. 2023) Key insight: optimal RLHF policy cóclosed-form solution. Vì vậy ta có thể train trựctiếp trên preference data màkhôngcần Reward Model. Analogy: RLHF=thuêgiámkhảochấmđiểmrồidùngđiểmđódạylại. DPO=cho model xem trực tiếp cặp tốt/xấu, tự học phân biệt— bỏ qua giám khảo trung gian. DPOloss: binary cross-entropytrên log-ratio chosen vs rejected probabilities. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 7 / 49

---

<!-- chiron-source-span: {"source_span_id":"22e650fe-c078-5025-b54d-62c3bec52646","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"DPOderivation — 3 bước từBradley-Terryđến loss","extraction_method":"pdf-text-layer"},"checksum":"747dfbd5aa74a724d88312eabea852f36b6ab64625d74d82c582bae11e6bf2d5"} -->

## Slide 13 - DPOderivation — 3 bước từBradley-Terryđến loss

1. Bradley-Terry P(yw ≻ yl | x) = σ(r(x, yw) − r(x, yl))

2. Optimal policy(KL-RL) π∗(y | x) ∝ πref(y | x) er(x,y)/β

3. Invert ⇒ DPO loss r = β log π∗ πref thay vào (1)⇒ no RM! Magictrick “Closed-formoptimalpolicy”(bước2)làchìa khóa. Nếu không có nó, ta không thể bỏ Reward Model. DPO chỉ áp dụng được cho objectivedạng KL-regularizedRL —không phảimọi RL setup.

### DPOloss (final form)
LDPO = − log σ ( β log πθ(yw) πref(yw) −β log πθ(yl) πref(yl) ) Forwardpass qua πθ và πref trên(prompt, yw, yl). Khôngrollout, không PPO clipping.(Rafailov et al. 2023) Giảngviên (VinUni) AICB· Ngày 22 Tuần5 8 / 49

---

<!-- chiron-source-span: {"source_span_id":"88b4ba9d-486a-56f7-9a17-fe03e8a45c71","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"RLHFvs DPO — So sánhPipeline","extraction_method":"pdf-text-layer"},"checksum":"a4fb29de5658b5d8f47397bfba572eafef461a9f7db137fb49b10a8842f319d4"} -->

## Slide 14 - RLHFvs DPO — So sánhPipeline

RLHF: SFT Model Reward Model PPO Training Aligned Model DPO: SFT Model DPOTraining (trựctiếp trên preference pairs) × Không cần RM Íthơn 3×components,offlinelearning, quality tương đương DPOadvantages Offlinelearning (stable) Ítcomponents: chỉ 1model + ref Quality tương đương RLHF trên benchmarks Lưu ý: Known issues: length bias (model học viết dài hơn thay vì tốt hơn), ref model dependency, over- fittingtrên small datasets. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 9 / 49

---

<!-- chiron-source-span: {"source_span_id":"9db8bb30-da0a-5c50-aa18-8b75da49efa6","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"DPOHyperparameter: β —Kiểm soát mức độ alignment","extraction_method":"pdf-text-layer"},"checksum":"e7ed2f6fa5a61931a7855570d4bde30ddd0076013b59944bebab3e27b3859779"} -->

## Slide 15 - DPOHyperparameter: β —Kiểm soát mức độ alignment

β = 0.05 Tựdo cao β = 0.1(standard) Cânbằng β = 0.2(conservative) Gầnref model Constraint tăng dần β(KLpenalty) — βcao ⇒modelbịgiữ gần ref model hơn.β thấp ⇒ model tự do “rời xa” ref model để optimize prefer- ence.

- Bắtđầu β = 0.1(default)

- Nếumodel quá conservative⇒giảm
xuống0.05

- Nếumodel “quên” kiến thức⇒tănglên
0.2 IPO:variant fix length bias —drop-in replacement cho DPO. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 10 / 49

---

<!-- chiron-source-span: {"source_span_id":"0d7b0360-1259-588c-be47-074a8e4e8949","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"DPOfailuremodes —khi training“thànhcông” nhưngmodel tệhơn","extraction_method":"pdf-text-layer"},"checksum":"c4d407da2dae9bde65404df1015862b93c640ef62ab6782bb54436baa619f117"} -->

## Slide 16 - DPOfailuremodes —khi training“thànhcông” nhưngmodel tệhơn

Lưu ý: Likelihood displacement (Razin 2024) — probcủa chosengiảmkhitrain;khichosen ≈rejected, massdồn sang tokenngượcnghĩa ⇒unalignment. Lưuý: Lengthhacking —DPOthưởngresponsedài (nhiềulog-prob mass). Học“viết dài” thay vì “viết tốt”. Lưu ý:Mode collapse / sycophancy— mọi câu mở đầu“Great question!” —over-fit preference style.

### Triệuchứng trên TRL logs

- rewards/chosen giảm ⇒likelihooddisplacement

- rewards/margins âm/co ⇒optimizationconflict

- Lengthtăng >30% ⇒lengthhacking
Mitigations Filter pairs có gap quá nhỏ; dùngSimPO/IPO; stopsớm khi rewards/chosen đảochiều. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 11/ 49

---

<!-- chiron-source-span: {"source_span_id":"45335761-45e7-50b3-9126-552c0deb05e3","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"ORPO, SimPO & Alternatives","extraction_method":"pdf-text-layer"},"checksum":"4df96bf1bb5fb32480feca77fc8bebe4629b0c985fa0fb32d910f15d53ec233d"} -->

## Slide 17 - ORPO, SimPO & Alternatives

04 Single-stage alignment — bỏ cả bước SFT riêng biệt

---

<!-- chiron-source-span: {"source_span_id":"41cd05c9-8aa8-5526-8611-21b97b876476","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Alignmenttimeline 2022 →2026— từ PPO đến RLVR","extraction_method":"pdf-text-layer"},"checksum":"16b017dc31a70d199ef328041edeb8eac395cb251e92da89ada85f55ec28b235"} -->

## Slide 18 - Alignmenttimeline 2022 →2026— từ PPO đến RLVR

2022 PPO-RLHF InstructGPT 3 models 2023 DPO No RM (Rafailov) 2024 ORPO· SimPO · KTO No ref / no SFT 1 stage Llama3 · Tulu3 Iterative DPO + RLVR 2025 GRPO· R1 RL comeback (no value model) Cốttruyện 2022: RLHFnặng,3models,PPOun- stable. 2023: DPO— toán bỏ được RM. 2024: method nở rộ, mỗi method bỏ thêm một thứ (refmodel, SFT stage, length bias). 2025: RL trở lại với GRPO/RLVR — nhưng không reward model. Lưu ý: Tooling đổi liên tục, nhưng câu hỏi không đổi: “Ai dạy model phân biệt good vs bad?” Khi câu trả lời là người → RLHF/DPO. Khi là code/regex → RLVR. Khi là chính model →Self-Rewarding/ CAI. Refs: Ouyang 2022, Rafailov 2023, Hong/Meng/Ethayarajh 2024, Tulu 3 2024, DeepSeek-R1 2025. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 12 / 49

---

<!-- chiron-source-span: {"source_span_id":"828c4f77-7d34-5c95-9bef-95d902c6ce52","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Methodmatrix — chọn alignment methodnào?","extraction_method":"pdf-text-layer"},"checksum":"03716d504361ad6d2d09f23ddfb5ca0548a4d1656aa89b959f7a0ee5e6e5a803"} -->

## Slide 19 - Methodmatrix — chọn alignment methodnào?

Method RM? Ref? Stages Khi nàodùng? RLHF(PPO) Có Có 3 Frontierlabs, max quality DPO Không Có 2 Go-toproduction alignment IPO Không Có 2 DPOover-fit deterministic prefs SimPO Không Không 2 Length-norm,less VRAM ORPO Không Không 1 Base →aligned1 stage KTO Không Có 2 Chỉcó thumbs up/down GRPO Không Có 1RL Reasoning+ RLVR Quickrules CóSFT+prefpairs ⇒DPO.NoSFT ⇒ORPO.Chỉ +1/−1 ⇒KTO.Math/code ⇒GRPO+RLVR. Lưu ý:DPO vẫn làbaseline tốt nhất2025-2026. Chuyểnmethodkhácchỉkhicólýdocụthể(VRAM, noSFT,reasoning). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 13 / 49

---

<!-- chiron-source-span: {"source_span_id":"7503feaa-7285-5cf3-9293-64c730681016","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"SimPOvs KTO— hai hướngđi sau DPO","extraction_method":"pdf-text-layer"},"checksum":"36c80b1c83545c2d9656242f92f9cb5609d40a32e4d124cb8af2b0db64ad96e2"} -->

## Slide 20 - SimPOvs KTO— hai hướngđi sau DPO

SimPO(Meng et al. 2024) Reference-free—không cần πref. Implicit reward = average log-prob củaresponse (length-normalized). +Targetmargin γ trênBradley-Terry. Kếtquả: +6.4trênAlpacaEval2,+7.5 trên Arena-Hard so với DPO (§8.3). Top SimPO model (Gemma-2-9B-it) đạt72.4% LC win-rate. Khi nào dùng: VRAM hạn chế, length bias là vấn đề lớn. KTO(Ethayarajh et al. 2024) Single-signal — không cần prefer- ence pairs. Mỗi example chỉ cần labelgood/bad (+1/−1). Loss dựa trên prospect theory (Kahneman-Tversky): mô hình loss aversion. Lợi thế thực tế: dữ liệu thumbs- up/down từ production logs dễ thu thậphơn nhiều so với ranked pairs. Khi nào dùng: có user feedback ratings từ produc- tion,không có annotators chuyên dụng. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 14 / 49

---

<!-- chiron-source-span: {"source_span_id":"a79675c9-932b-55eb-b00c-21a678d83396","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"ORPO— Single-Stage: Base→Aligned","extraction_method":"pdf-text-layer"},"checksum":"0122612e444acabe3b89c27786e1e3fa4189045ceef91c2964fc17e9f6f1fa50"} -->

## Slide 21 - ORPO— Single-Stage: Base→Aligned

Truyềnthống: Base SFT DPO ORPO: Base SFT+ Alignment (singletraining run) 50% VRAM reduction 1 stage thay vì 2 Không cần ref model

- ORPOkết hợp SFT loss +
preferenceloss trong cùng 1 objective

- Bestcase: basemodel →
alignedmodel in one step

- SkipSFT stage hoàn toàn
Lưuý: ORPOtrade-off: đơngiảnhơnnhưngít maturehơnDPO.Dùngkhimuốntraintừbase modelvà VRAM hạn chế. GRPO(DeepSeek-R1): next frontier choreasoning alignment— thay thế PPO bằnggroup relative policy, khôngcần RM. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 15 / 49

---

<!-- chiron-source-span: {"source_span_id":"43f5e3b6-5be4-5c56-9a45-1a44bdce4637","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"RL comeback — GRPO & RLVR","extraction_method":"pdf-text-layer"},"checksum":"139df1bada971a5ff3506d4f9498dad6698046bcc13fdda0acc5c9b3efb8705e"} -->

## Slide 22 - RL comeback — GRPO & RLVR

05 Năm 2025: RL trở lại cho reasoning, nhưngkhông cần reward model

---

<!-- chiron-source-span: {"source_span_id":"dabb1cad-fcc7-5afe-9df1-2979c73b9321","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"GRPO— PPO không có valuemodel","extraction_method":"pdf-text-layer"},"checksum":"3dbcd3a7340ca397edf550f60e7be2d0782be9b129249978d3a138826ad1fb9c"} -->

## Slide 23 - GRPO— PPO không có valuemodel

Prompt x y1 y2 y3 · · · yG r1 r2 r3 rG ¯r = 1 G ∑ ri (groupmean) Advantage Ai = ( ri − ¯r)/std(r) (không cần value/critic model!) GRPO — Group Relative Policy Optimization. Lấytrungbìnhreward của nhóm G samples cho cùng promptlàmbaseline—thaythếcho valuemodel trong PPO.

- PPOclipping ratio như cũ

- Bỏvalue head ⇒ 50%memory
savings

- Dùngcho DeepSeekMath, sau đó
DeepSeek-R1(Jan 2025) Refs: Shao et al. 2024 (DeepSeekMath); DeepSeek-AI 2025 (R1). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 16 / 49

---

<!-- chiron-source-span: {"source_span_id":"aa228b5d-bdbc-5fc4-bd65-f1f5491c4bdd","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"RLVR& DeepSeek-R1 — rewardthay bằngregex","extraction_method":"pdf-text-layer"},"checksum":"67fc45bd7f68cfe22e79b996378e5ac62385e05519394e04d16c69eab42054d7"} -->

## Slide 24 - RLVR& DeepSeek-R1 — rewardthay bằngregex

```text
RLVR — Reinforcement Learning from Verifiable
Rewards. Reward = kiểm tra programmatic(math
match,unit test, regex). Không có “judge” để hack.
```

### Khinào RLVRwork

- Math: ground truth trongdataset

- Code: chạy unit tests

- Format: regex / JSONschema

```text
■ Tooluse: success/error from tool
```
Lưuý: RLVR khôngthaypreferencelearningchosub- jectivetasks. Bổsung,không thay thế.

### DeepSeek-R1-Zero(Jan 2025)

- Trainbasemodel (khôngSFT cold-start)

- Reward= accuracy + format (rule-based)

- Emergent“Aha!” self-reflection
R1(full): thêmSFT cold-start nhỏ→readabilitytốt hơn,math reasoning tương đương. Hook 2023: “RLHFtốnkém,dùngDPO.”2025: “RLtrở lạichoreasoning— nhưng không reward model.” Giảngviên (VinUni) AICB· Ngày 22 Tuần5 17 / 49

---

<!-- chiron-source-span: {"source_span_id":"75747be6-64b8-5482-ba2e-15ef0c047a2c","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Khinào reasoning task cần RLchứ không phải DPO?","extraction_method":"pdf-text-layer"},"checksum":"74a6a2b03b1a0f10fc7095afba41066951dbfc2b0653751e9427a96f72c869c0"} -->

## Slide 25 - Khinào reasoning task cần RLchứ không phải DPO?

Tasktype Methodkhuyến nghị Helpfulness,style, tone DPO/ SimPO Safety,harmlessness DPO+ CAI Mathword problems GRPO+ RLVR(answer match) Codegeneration GRPO+ RLVR(unit tests) Long-formreasoning SFTcold-start + GRPO Toolcalling correctness GRPO+ RLVR(tool result) Multi-turndialogue DPO(preference pairs) Quytắc đơn giản Có ground truth có thể check pro- grammatic? →RLVR. Chỉ cójudgment của con người?→ DPO. Cả hai? → Stack: SFT → DPO → RLVR(Tulu3 recipe). Lưu ý:GRPO không miễn phí: cần generation rollouts (G ≈ 8–64 sam- plesperprompt) ⇒ 3-4×thờigianso vớiDPO.Chỉdùngkhireasoningtask thựcsự cần. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 18 / 49

---

<!-- chiron-source-span: {"source_span_id":"b6e94b5b-3c5f-523a-90da-1bde63a04bff","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Preference Data & Implementa","extraction_method":"pdf-text-layer"},"checksum":"37817ae4733a934a1c8dc415b4cbaad467a6422f02d1af6a29ebb17a7bba2b6a"} -->

## Slide 26 - Preference Data & Implementa

06 Preference Data & Implementa- tion Chuẩn bị dữ liệu preference và chạy DPO với TRL

---

<!-- chiron-source-span: {"source_span_id":"0f63f945-ed4c-574e-80ab-0daf4362dcde","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"PreferenceDataset — prompt + chosen+ rejected","extraction_method":"pdf-text-layer"},"checksum":"5fc2d209a47a0eea82f411300985a21ce5b5b1a58cb10c07f8dbb5e7d18c22e8"} -->

## Slide 27 - PreferenceDataset — prompt + chosen+ rejected

Prompt: “Giảithích AI...” Chosen: Rõràng, concise Rejected: Verbose,generic vs Khác biệt phải genuine — KHÔNG chỉ là length

### Nguồndữ liệu

- Humanannotation: pairwise
comparisonUI →JSONLexport

- Synthetic: GPT-4judgescore,
rank,tạo pairs

- Tools: Argilla, Label Studio, Prodigy
Quymô tham khảo 60Kpairs chogood alignment. Open-source: UltraFeedback (64k), Anthropic HH (160k), OpenHermes (1M). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 19 / 49

---

<!-- chiron-source-span: {"source_span_id":"b4f959a3-c407-5b22-8a57-0fcfd1885620","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"TRLDPOTrainer— Implementation","extraction_method":"pdf-text-layer"},"checksum":"cd460aae516f74d48bebf8fd3b1cc948d672f86d96608e588efdd2bba008f621"} -->

## Slide 28 - TRLDPOTrainer— Implementation

```text
from trl import DPOTrainer, DPOConfig
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(
"path/to/sft-model")
ref_model = AutoModelForCausalLM.from_pretrained(
"path/to/sft-model") # frozen
config = DPOConfig(
beta=0.1, learning_rate=5e-7,
max_length=1024, max_prompt_length=512,
)
trainer = DPOTrainer(
model=model, ref_model=ref_model,
args=config, train_dataset=pref_data,
)
trainer.train()
```

### Monitoringhealthy training

- Chosenrewards: phảităngqua
epochs

- Rejectedrewards: phảigiảmqua
epochs

- Gapgiữa 2 loại nênwidendần
Alternatives SimPO: không cầnref_model ⇒ simpler, less VRAM. ORPOTrainer: single-stage, không cần SFT trước. Lưu ý: Tokenization: verify max_prompt_length + max_length fit con- textwindow. Truncationgiảm quality. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 20 / 49

---

<!-- chiron-source-span: {"source_span_id":"5896276e-b3ab-5c92-8299-ac9fc1fe7600","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"IterativeDPO — vì sao one-shotoffline không đủ","extraction_method":"pdf-text-layer"},"checksum":"83ee145e5c0b5226a8a244924afe1aae60397ad1855146d5d24a0b2ce94ee9ac"} -->

## Slide 29 - IterativeDPO — vì sao one-shotoffline không đủ

1. TrainRM 2. Rejection sampling

3. SFT on best 4. DPO on (best,worst) Lặp lại 6 vòng (Llama 3)

### Llama3 recipe(Meta2024)

- TrainRM trên human preference +
editedresponses

- Sinh10–30 generations / prompt→
RMchọn best

- SFTtrên best, DPO trên (best vs
worst)

- Lặp6 vòngvớidata mới mỗi vòng
Tulu3 (AI2, Nov 2024) Open recipe:SFT →DPO →RLVR. RLVR thêm +1.7 MATH / +3.3 GSM8K / +1.3 IFEval trên DPOcheckpoint—transfercảraBBH,DROP,Al- pacaEval. (Định nghĩa benchmark: §8.2–8.3.) Lưu ý:Lesson: one-shot offline DPO underper- forms. Mọi 2024-2025 stackđều iterative. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 21 / 49

---

<!-- chiron-source-span: {"source_span_id":"df1c07a5-0402-5224-86c4-b48fa3a6882b","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Rewardmodels 2025 — chưa biếnmất, chỉ đổi vai trò","extraction_method":"pdf-text-layer"},"checksum":"b7aba424b24ca98cf25c6adbfb9b1b6ae31b000cf29405c57b17f5ab7ffc5e21"} -->

## Slide 30 - Rewardmodels 2025 — chưa biếnmất, chỉ đổi vai trò

TrongDPO world, RM dùnglàmgì?

- Datafilter: loại bỏ pairsgap quá nhỏ
(chosen ≈rejected)

- Rejectionsampling: chọn best-of-N
generationscho SFT next round

- Best-of-Ndecoding: tạiinference,sinh
Ncâu, pick best

- LLM-as-judgebackbone: thay GPT-4
choeval rẻ hơn Lưu ý: Đừng nhầm: “Không cần RM cho DPO loss”không có nghĩa “Không cần RM ở đâu cả”. RM vẫn ở khắp pipeline—chỉkhôngtrựctiếptronggra- dientupdate.

### Topopen RMs (2025)

- Skywork-Reward-V2(Jul2025): 8
models0.6B–8B, 26M pairs, SOTA trên7 benchmarks.

- HelpSteer2(NVIDIA):10K pairs
qualitycực cao — former SOTA.

- RewardBenchv2: standard
benchmark( §8.4). Default Skywork-Reward-V2-Llama-3.1-8B. Dùng làm fil- tercho rejection sampling + best-of-N. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 22 / 49

---

<!-- chiron-source-span: {"source_span_id":"819a0ae1-10a7-51a4-a0fb-e1d402bd44c4","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"VietnameseLLMs — ai đã làmDPO, ai chưa?","extraction_method":"pdf-text-layer"},"checksum":"2a91d4ad9136beaf76230c0ea428a76a168531a357857dc4124ec566ca9faa2c"} -->

## Slide 31 - VietnameseLLMs — ai đã làmDPO, ai chưa?

Model Base SFT DPO? Ghichú VinaLLaMA-7B-Chat LLaMA-2-7B ✓ × VNinstruction set; chỉ SFT (paper2023) PhoGPT-7B5-Instruct PhoGPT(VN scratch) ✓ × 70Kinstructions + 290K chats; nopreference stage PhoGPT-4B-Chat PhoGPT-4B ✓ × Smallerchat variant Vistral-7B-Chat Mistral-7B ✓ × CommunitySFT SeaLLM-v2/v2.5/v3 Llama-2/ Qwen ✓ ✓ DPOwith self-generated preference data (DAMO) Sailor/ Sailor2 Qwen1.5/2.5 ✓ ✓ DPO+ variants (SimPO, LN-DPO, LR-DPO)(Sea AI Lab) Pattern VN-first(VinaLLaMA,PhoGPT,Vistral)dừngởSFT. SEA-regional (SeaLLM, Sailor) chạy tới DPO.⇒ Gapcho VN-first DPO-aligned model. Lưu ý: Lab 22 có thể là DPO-aligned VN model open-source đầu tiên end-to-end của khóa — pub- lishable. Refs: VinaLLaMA 2312.11011 · PhoGPT 2311.02945 · SeaLLM 2312.00738 · Sailor (EMNLP 2024) · Sailor2 2502.12982. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 23 / 49

---

<!-- chiron-source-span: {"source_span_id":"564c7f2c-1efe-5c83-939d-623a07719756","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Xâydựng preference data tiếng Việt— 4 bước thực tế","extraction_method":"pdf-text-layer"},"checksum":"4d7f2a73ba3bcac6db1d76c7cef81b48ed46fa7f465f0c5b7a5b691f21d486c0"} -->

## Slide 32 - Xâydựng preference data tiếng Việt— 4 bước thực tế

1. Prompts: VN SFT set / VMLU stems(200 prompts)

2. Generate 2 responses: Lab21-SFT + stronger model

3. Judge: GPT-4o/ Claude Sonnet (VN-awareprompt)

4. TrainDPOtrên 200 pairs ( 20 minA100)

### Nguồndữ liệu VN sẵn có

- UltraFeedback-vi: Sailor dịch bằng
NLLB-3.3B— “đủ cho DPO” nhưng khôngnative.

- SeaLLMself-generated: prompt
SeaLLM-SFT,GPT-4judge.

- VMLU/ ViGLUE:có ground truth→
dùnglàm RLVRrewards cho academicknowledge (§8.5). Cơhội VN Chưacó nativelarge-scalepreferencedataset— labartifact đáng publish. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 24 / 49

---

<!-- chiron-source-span: {"source_span_id":"03415cb3-14a2-50ab-964f-6e74c5203b4f","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Constitutional AI & Red-teaming","extraction_method":"pdf-text-layer"},"checksum":"9f75704f8a4a5b9bad35bc45e9d66c198579d9eaa7999700b9c36cf21cb86b1c"} -->

## Slide 33 - Constitutional AI & Red-teaming

07 Tạo preference data tự động và kiểm tra an toàn

---

<!-- chiron-source-span: {"source_span_id":"199b4050-bc84-5fef-ba44-b92789642bf6","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"ConstitutionalAI (Anthropic) — Self-Improvement","extraction_method":"pdf-text-layer"},"checksum":"776e6ac13d962f4b10d1abf77673442b05a2945102702c420c129fb94115630d"} -->

## Slide 34 - ConstitutionalAI (Anthropic) — Self-Improvement

1. Generate modeloutputs

2. Critique vsconstitution

3. Revise self-improve

4. Preference Pairs (originalvs revised) Constitution: ∼16 principles ban đầu Helpfulness, Harm- lessness, Honesty CAI — Model critique own outputs vsconstitution →self-revise →dùng cặp (original, revised) làm prefer- encedata.

### Ưuđiểm

- Tạopreference datakhôngcần
humanannotators

- Scalable,consistent

- Dùngcho DPO/ORPO training
Giảngviên (VinUni) AICB· Ngày 22 Tuần5 25 / 49

---

<!-- chiron-source-span: {"source_span_id":"7eef1b3f-5858-5a3d-8750-64e5000f44be","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"RLAIF,Self-Rewarding LMs & Collective CAI —AI làm judge","extraction_method":"pdf-text-layer"},"checksum":"f13c419f07893a62c05c88f80c3fff09161f76b48c9fefc269da180dd145aa49"} -->

## Slide 35 - RLAIF,Self-Rewarding LMs & Collective CAI —AI làm judge

RLAIF — Reinforcement Learning

```text
from AI Feedback (Lee et al. 2023).
```
Thay human annotators bằng LLM- as-judge. Empirically: AI feedback ≈ human feedback ở scale, 10 × cheaper. Self-Rewarding LM — (Yuan et al., Meta 2024) Model là chính judge của mình. Lặp: generate → self-judge → formpairs →DPO.Sau3vòng,Llama- 2-70B beats Claude 2 / Gemini Pro / GPT-4-0613trên AlpacaEval 2. CollectiveConstitutional AI(Anthropic

### 2024)

- Mờipublicinput vàoconstitution
document

- Polis-styleconsensus elicitation

- Constitutionkhôngcònlà16nguyên
tắcdo Anthropic viết — mà làtinh thầncộng đồng Patternchung Ai sẽ làm judge?Human (RLHF)→ AI (RLAIF)

- Self (Self-Reward)→ Community (Coll. CAI).
Rẻhơn, scale hơn — nhưngrisk bias tăng theo. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 26 / 49

---

<!-- chiron-source-span: {"source_span_id":"c0928c65-dff6-5c16-9849-64f0b7f9d3b4","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Red-teaming— Kiểm tra an toàntrước deploy","extraction_method":"pdf-text-layer"},"checksum":"17fc31cbe36dccbef9c38e85fb0d4a108d3fcd1cdd83753b8c38c0746b8cd64d"} -->

## Slide 36 - Red-teaming— Kiểm tra an toàntrước deploy

- Probemodel choharmfuloutputs

- Findingsfeed back vào preference
dataset

- Domain-specific: medical
misinformation,legal liability AutomatedTools Garak: vulnerability scanner PyRIT(Microsoft): adversarial testing ⇒Scalable,repeatable Red-team Attack Model UnderTest Analyze Failures Update Pref. Data Continuous improvement loop Giảngviên (VinUni) AICB· Ngày 22 Tuần5 27 / 49

---

<!-- chiron-source-span: {"source_span_id":"96b14b09-4cc4-55ee-a999-7a37eb397fdd","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Đánh giá Alignment — LLM","extraction_method":"pdf-text-layer"},"checksum":"1c5707d176c4503711664173f0476203d10f6c8d175da8564c191f16aa591a9d"} -->

## Slide 37 - Đánh giá Alignment — LLM

08 Benchmarks Static suites · LLM-as-Judge · Reward Bench · Vietnamese land- scape

---

<!-- chiron-source-span: {"source_span_id":"9aa65de7-334c-5aa1-af1f-feb5a6e9f783","locator":{"kind":"page","page":38,"label":"Slide 38","section_title":"Tạisao đánh giá alignment khó?","extraction_method":"pdf-text-layer"},"checksum":"c8123bba07434dbfe1e26cee5c629e3f2a3ad80c20c7918cc28068812fc70a5c"} -->

## Slide 38 - Tạisao đánh giá alignment khó?

Vấnđề cốt lõi Aligned response là open-ended —

### khôngcó 1 ground-truth duy nhất
“Giúp tôi viết email xin nghỉ phép” →vô sốcâu trả lời đều đúng. Khác hẳn classification (1 nhãn đúng) haytranslation (BLEU vs reference). Proxyvs Target Cái tađo(helpfulness 1-5) làproxy —không phải target thật. Target thật: user retention, task completion, brand trust, không gây hại. Mọi metric chỉ là 1 lát cắt⇒ cần nhiềumetrics + human feedback. Lưu ý: 3 nhóm benchmarksẽ xuất hiện trong các slide tiếp theo:Static suites (MMLU/GSM8K — đo capability) ·Judge-based suites(MT-Bench/AlpacaEval — đoresponsequality)· RewardModelsuites (RewardBench—đochínhcácjudges). Không1 cái nào đủ một mình. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 28 / 49

---

<!-- chiron-source-span: {"source_span_id":"42a9cda4-861b-5fec-b976-d31000996d1f","locator":{"kind":"page","page":39,"label":"Slide 39","section_title":"Staticbenchmarks — đo capability củaaligned model","extraction_method":"pdf-text-layer"},"checksum":"fdb1aa64723a8f85a6782d23971bb5832ddd0630f9f0ab107901d15630cecfc9"} -->

## Slide 39 - Staticbenchmarks — đo capability củaaligned model

Benchmark Đogì Format Score Vì saoquan trọng cho aligned model MMLU Kiếnthức nền 57 subjects MCQ4-choice 0–100% Cóquên kiến thức sau alignment? GSM8K Mathgrade-school Gen+ match #### 0–100% Chat-tuningcó giảm reasoning? (alignment tax) MATH Maththi olympic Gen+ LaTeXmatch 0–100% NhưGSM8K, harder (∼50chỉ top model) IFEval Theolệnh format Gen+ programmatic 0–100% Alignedmodel có nghe “trả lời≤3câu”? HumanEval Codegeneration Rununit tests 0–100% Codealigned có chạy được không? BBH Mixedreasoning 23 tasks MCQ+ gen 0–100% Stress-testđa-nhiệm TruthfulQA Truthfulnessvs myths MCQ+ gen 0–100% Cóhallucinate “common belief” sai? Tulu3 reference Sau DPO + RLVR (xem§9.2b): +1.7 MATH · +3.3 GSM8K · +1.3 IFEval— nhưng MMLU thườngflat hoặc giảm nhẹsauchat-alignment. Tất cả đều programmatic scoring; chạy offline trên 1 GPU. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 29 / 49

---

<!-- chiron-source-span: {"source_span_id":"db819203-09aa-5d97-aaa7-520e7fc42213","locator":{"kind":"page","page":40,"label":"Slide 40","section_title":"Judge-basedbenchmarks — đo response quality","extraction_method":"pdf-text-layer"},"checksum":"948efb5f452cba38b8e1bbbcdcd3529578bb2503e39af4f86c35b249a5fa4414"} -->

## Slide 40 - Judge-basedbenchmarks — đo response quality

Benchmark #prompts Format Judge Tradeoff MT-Bench 80multi-turn Score1–10 GPT-4 Tinyset; judge có position bias AlpacaEval2 LC 805single-turn Win-ratevs gpt-4-1106 GPT-4 Length-controlled (Dubois 2024) sửa length-bias Arena-Hard 500hard prompts Win-ratevs gpt-4-0314 GPT-4 Khó cho weak models; thẩm chí gpt- 3.5cũng <30% ChatbotArena live, >3Mvotes ELOranking Ngườidùng thật Ground-truthnhất,nhưngđắt+chậm Cross-judgetip Chạycùng1promptqua 2judgeskhácnhau (gpt- 4o-mini + claude-haiku-4-5); disagreement = signal cầnxem tay. Lưuý: Lengthbias (judgesthiênvịcâudài)làfail- uremodelớnnhấtpre-2024. AlpacaEval2 LCfixes nó;MT-Benchthì chưa. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 30 / 49

---

<!-- chiron-source-span: {"source_span_id":"e534a2be-61e4-5497-a1b2-31b2ead45e02","locator":{"kind":"page","page":41,"label":"Slide 41","section_title":"RewardModels = meta-judge — vàvấn đề recursion","extraction_method":"pdf-text-layer"},"checksum":"95cbb00a6f73d6d40403806c71e9c70186c3273a516dfd6d06547189d2643979"} -->

## Slide 41 - RewardModels = meta-judge — vàvấn đề recursion

Tại sao cần benchmark cho RM/- judges? Judgecũng là 1 model⇒cóbias. RewardBench v2 (Lambert et al. 2024) test RM trên 4 categories: chat ·safety · reasoning · code. RM-Bench (Skywork 2024) thêm hardpairs phân biệt model gần nhau. Tulu 3 dùng Skywork-Reward- Gemma làm filter cho preference datatrước khi train DPO. Lưu ý:Vấn đề recursion:judge cần judge, RM cần benchmark, bench- mark cần evaluation — không có “ground truth” tuyệt đối ngoài con người + thời gian + production data. Constitutional AI (§7) là 1 cách thoát recursion: dùng explicit rules làmanchor thay vì preferences. Tronglab NB4 = judge-based,NB6 = static— 2 lăng kính khác nhau, kết quả khác nhaulà bình thường. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 31 / 49

---

<!-- chiron-source-span: {"source_span_id":"0b1b5ba2-7d3b-57c6-a7da-6897a10b7edb","locator":{"kind":"page","page":42,"label":"Slide 42","section_title":"Vietnamesebenchmark landscape — gì có,gì thiếu","extraction_method":"pdf-text-layer"},"checksum":"9647bda2088e14c90f0c8e133527c3b7867d188ad9b970aeccc4d9659244226d"} -->

## Slide 42 - Vietnamesebenchmark landscape — gì có,gì thiếu

Benchmark Đogì Status Note VMLU 10KMCQ, 58 VN subjects Active2024+ Phamet al. —“lò luyện thi” THPT + ĐH ViGLUE NLU5 tasks (NER, sentiment, NLI,QA) 2023stable Older,vẫn dùng được choNLU baseline ViMMLU MMLUdịch sang Việt 2023 NLLB-MTquality concerns; OK cho roughcheck VLSPshared tasks VariousNLP tasks Annual Academic;dataset rotates yearly VN AlpacaEval Win-rate VN GAP Chưa tồn tại! Bonus B opportunity Lưu ý: Native VN judge-based benchmark chưa tồn tại.Sailor2 dùng UltraFeedback-vi (translated). Cơ hội: ai trong cohort này build 1native VN AlpacaEval-style set 200–500 prompts⇒ publishable đầu tiên(xem BONUS-CHALLENGE.md provocation#1). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 32 / 49

---

<!-- chiron-source-span: {"source_span_id":"b3c1e267-1aa8-562f-8a3c-a317253ee9f7","locator":{"kind":"page","page":43,"label":"Slide 43","section_title":"Demo & Thực hành","extraction_method":"pdf-text-layer"},"checksum":"bbd96ddd22a0997af3ffbad632213a0d2d7d41166ef228e69b5dd313e71b764e"} -->

## Slide 43 - Demo & Thực hành

09 DPO training thực tế + đo improvement bằng GPT-4 Judge

---

<!-- chiron-source-span: {"source_span_id":"63e8b273-9d08-5d9a-8089-595f57ab8821","locator":{"kind":"page","page":44,"label":"Slide 44","section_title":"DPOTraining+ LLM-as-Judge Comparison","extraction_method":"pdf-text-layer"},"checksum":"ba8c87649782b3b0219c206521aca827cc9a5f47bf884eddd496f4a5cc0e5fea"} -->

## Slide 44 - DPOTraining+ LLM-as-Judge Comparison

1. LấySFTcheckpointtừLab21,applyDPOvới2kUltraFeedbackpairs,1epoch

2. BeforeDPO: over-hedges, generic, verbose. After DPO: direct, concise, actionable

3. GPT-4judge: helpfulnesstừ 3.2 →4.1outof 5

4. Sosánh: chosen rewardstăng, rejected rewards giảm — healthytraining signals Giảngviên (VinUni) AICB· Ngày 22 Tuần5 33 / 49

---

<!-- chiron-source-span: {"source_span_id":"52262403-818b-5002-9c6e-9782d3b56054","locator":{"kind":"page","page":45,"label":"Slide 45","section_title":"DPOImprovement — Before vs After","extraction_method":"pdf-text-layer"},"checksum":"fc5239d77d2309e0e45249427d85c10224ef5db305148ecbf913302373339b0c"} -->

## Slide 45 - DPOImprovement — Before vs After

3.2 →4.1 Helpfulness (GPT-4 judge) −40% Response length (less verbose) 1epoch Training time (∼30 min A100) Tạisao hiệu quả? DPO dạy model phân biệttrực tiếpgiữa good vs bad response — model học pref- erencesignal rất nhanh, chỉ cần 1–2epochs. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 34 / 49

---

<!-- chiron-source-span: {"source_span_id":"b54c690c-16a5-57dd-8ae0-f7450c3e6cb2","locator":{"kind":"page","page":46,"label":"Slide 46","section_title":"Tulu3 (AI2 2024) —SFT vs +DPO vs +RLVRthực tế","extraction_method":"pdf-text-layer"},"checksum":"6c0362ee104a840bf500baf63217701ac00b54ce6bdba93485ccba3160965e0d"} -->

## Slide 46 - Tulu3 (AI2 2024) —SFT vs +DPO vs +RLVRthực tế

+1.7 MATH sau RLVR (vs DPO) +3.3 GSM8K sau RLVR +1.3 IFEval sau RLVR Đọcbảng số Tulu 3 publish toàn bộ recipe + data + code. Mỗi stage thêmvài points, không phải đột phá — nhưngcộng dồn: SFT → DPO → RLVR đủ để Tulu 3-405B vượt Llama 3.1-Instruct-405BvàDeepSeek-V3trênAI2evalsuite. Đâylàbenchmarkthựctếcủa “modernalignment stack”. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 35 / 49

---

<!-- chiron-source-span: {"source_span_id":"91bbcbc4-d259-59b6-a0f7-3b73463d1976","locator":{"kind":"page","page":47,"label":"Slide 47","section_title":"Lab#22","extraction_method":"pdf-text-layer"},"checksum":"2ac0b4dfa4a498b13739acf1c75b3e9f431d8122071cfabcde418b163bb21bc1"} -->

## Slide 47 - Lab#22

Mụctiêu: DPOalignment trên SFT checkpoint + deployaligned model Deliverable: Aligned model deployed: merge adapter, quantize, serve với vLLM. Report: SFT-onlyvsSFT+DPO comparison. Thờigian: 2giờ Giảngviên (VinUni) AICB· Ngày 22 Tuần5 36 / 49

---

<!-- chiron-source-span: {"source_span_id":"a0bbe8a4-f843-57fa-8fe3-330915cdc93c","locator":{"kind":"page","page":48,"label":"Slide 48","section_title":"Lab22 — Các bước thựchành","extraction_method":"pdf-text-layer"},"checksum":"10867c8c8b1ff37829b3d905e1736619ab57cf6985d52ae90c806df9de0ca0d9"} -->

## Slide 48 - Lab22 — Các bước thựchành

1. Preparepreference dataset: human-ranked response pairs(hoặc synthetic via GPT-4judge), format prompt/chosen/rejected

2. TrainDPO adapter: trên SFT checkpointtừ Lab 21 dùng TRL DPOTrainer. Monitor chosen/rejectedrewards

3. Compare: SFT-onlyvsSFT+DPO trên safety và helpfulness metrics. Dùng GPT-4 judgecho evaluation

4. Deploy: mergeadapter,quantizeGGUF,servevớivLLM.Measurelatencyoverhead Deliverable GitHub repo + comparison report: helpfulness score trước/sau DPO, safety metrics, exampleoutputs Giảngviên (VinUni) AICB· Ngày 22 Tuần5 37 / 49

---

<!-- chiron-source-span: {"source_span_id":"1ce949be-4eed-5d60-b1da-138ddba32dc3","locator":{"kind":"page","page":49,"label":"Slide 49","section_title":"Lab22 — 2 bonus tracks(optional, +1giờ mỗi track)","extraction_method":"pdf-text-layer"},"checksum":"9619b4d37daf14f96e349a50708d85e4cd9b9af03660b5d8a047efa22776c048"} -->

## Slide 49 - Lab22 — 2 bonus tracks(optional, +1giờ mỗi track)

BonusA DPOvs ORPO head-to-head

1. Cùngbase model, cùng preferencedata

2. Train1 adapter DPOTrainer,1 ORPOTrainer

3. Sosánh: judge win-rate+ time + VRAM

4. Plot: chosen/rejected reward trajectories Outcome: hiểu trade-off “đơn giản vs mature”. BonusB Vietnamesepreference data

1. 200prompts từ VN SFT set / VMLUstems

2. 2responses: Lab21-SFT + stronger(Gemini Flash / Claude Haiku)

3. Judge: GPT-4o/Claude Sonnet (VN-awareprompt)

4. TrainDPO 200 pairs, so sánh nativevs UltraFeedback-vi Outcome: dataset + adapter publish- able— fill VN gap. Lưuý: GRPO+RLVR khôngcótronglab(compute-heavy, ≥3×DPO).Covertrong slidesonly — thử nếu có A10080GB rảnh. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 38 / 49

---

<!-- chiron-source-span: {"source_span_id":"7a2d0e67-09e3-5941-b229-784f3cfab245","locator":{"kind":"page","page":50,"label":"Slide 50","section_title":"Bức tranh toàn cảnh — Full","extraction_method":"pdf-text-layer"},"checksum":"81455494673c61e044f21582ef2ebad8d6601e68955371f1d909929873c2fabd"} -->

## Slide 50 - Bức tranh toàn cảnh — Full

10 training flow Alignment chỉ là một mảnh ghép — xem nó nằm ở đâu trong vòng đời của LLM

---

<!-- chiron-source-span: {"source_span_id":"31643143-f403-5063-824d-f95c1c8132d1","locator":{"kind":"page","page":51,"label":"Slide 51","section_title":"Pre-training →Mid-training →Post-training","extraction_method":"pdf-text-layer"},"checksum":"45e8bf7ec8a4d99e0f311dd450ec39add364c1b3a6b79b55c6d11b17f1480b7a"} -->

## Slide 51 - Pre-training →Mid-training →Post-training

Pre-training Mid-training Post-training Trillionsoftokens,next-token prediction Continued pretraining, do- main adapt, long-context ex- tension SFT → DPO → RLVR; merge,distill, optimize Cost: rất cao (MUSD) Cost: cao Cost: vừa phải Frontierlabs only Domainteams Most ML teams live here Insight 99% công việc của ML team trong industry rơi vào post-training(+mộtítmid-training). Pre-traininglà sân chơi của 5-10 lab toàn cầu (OpenAI, Anthropic, Google,Meta, Mistral, Alibaba, DeepSeek…). Lưu ý:Khi nào cần pre-training? Hầu nhưkhông bao giờcho startup/enterprise. Default: bắt đầu từ Llama / Qwen / Mistral base + post-train. Pre-

### trainingchỉkhidomainthựcsựngoàidistribution(vd
proteinsequences). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 39 / 49

---

<!-- chiron-source-span: {"source_span_id":"612fab36-09a9-5669-adbf-8d5d67cd01e9","locator":{"kind":"page","page":52,"label":"Slide 52","section_title":"Domainadaptation — DAPT vs TAPTvs LoRA fine-tune","extraction_method":"pdf-text-layer"},"checksum":"cdf44a6af6aff8ee6b85ec480da390a27befd6bb1990545ec40550ce948c55ca"} -->

## Slide 52 - Domainadaptation — DAPT vs TAPTvs LoRA fine-tune

Method Data Compute Khi nàodùng? DAPT (continued pre-training) Raw domain text (10B+ tokens) cao Domain hoàn toàn ngoài distribution (medi- cal,legal, code) TAPT (task-adaptive PT) Unlabeledtask corpus vừa Cósẵn task corpus, label chưacó SFT/LoRAfine-tune Labeledinstructionpairs thấp Đãcó format và task rõràng DPO / preference align Preferencepairs thấp Behavior alignment, không phải domain knowledge Sequentialrecipe Khi cần cả 2:DAPT → TAPT → SFT → DPO. Mỗi bước thêm vài points. (Gururangan et al. 2020 “Don’t StopPretraining”.) Lưuý: Catastrophicforgetting làrủirolớnnhất củaDAPT/TAPT.Replay50/50: trộn50%domain +50% general (Pile, RedPajama). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 40 / 49

---

<!-- chiron-source-span: {"source_span_id":"3dc50de9-0f92-5875-8d30-4b96fb27839a","locator":{"kind":"page","page":53,"label":"Slide 53","section_title":"Syntheticdata generation — 4 thếhệ kỹ thuật","extraction_method":"pdf-text-layer"},"checksum":"70c44c63367bff4b71c654d79245c1c97dc9d58be4a01a38da5683f03c316f1b"} -->

## Slide 53 - Syntheticdata generation — 4 thếhệ kỹ thuật

1. Self-Instruct(Wang2022): seed prompts,LLM tự sinh thêm. Quality thấp, scaledễ. (Alpaca lineage.)

2. Evol-Instruct(WizardLM2023): lặp promptrewritingđểtăngđộkhó(in-depth, in-breadth,deepening).

3. Persona-driven(PersonaHub 2024): 1B personas →diverseperspectives trên cùngprompt.

4. Verifiedsynthesis (2024+): LLM sinh response,sau đó kiểm tra programmatic (chạycode, regex check, tool call result) trướckhi đưa vào dataset — vd. WizardCoder,OpenMathInstruct, Tulu-3 RLVRdata. Phirecipe Phi-3/Phi-4 đặt cược vào syn- thetic “textbook-like”: structured, step-by-step. Phi-4 vượt teacher GPT-4 trên STEM — distillation khôngcòn là trần. Lưu ý: Pitfalls: mode collapse khi self-generate; license risk khi dùng GPT-4/Claude làm teacher; quality decay sau 2–3 thế hệ syn- thetic. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 41 / 49

---

<!-- chiron-source-span: {"source_span_id":"1eee5dbf-c949-5be7-8926-8bdaf80e6afc","locator":{"kind":"page","page":54,"label":"Slide 54","section_title":"Distillationlineage — Alpaca→Vicuna →Orca →Phi","extraction_method":"pdf-text-layer"},"checksum":"485cfc103b5b9c25ee181107f863781f335cd365dc83ed576a86087691d139a8"} -->

## Slide 54 - Distillationlineage — Alpaca→Vicuna →Orca →Phi

Alpaca(2023) Vicuna/WizardLM (2023) Orca(2023-24) Phi-3/Phi-4 (2024- 25) 52K Self-Instruct, GPT-3.5 teacher, imitateresponse ShareGPTlogs,Evol- Instruct,scale up GPT-4 teacher, copy reasoning traces, step-by-stepCoT Synthetic“textbooks”, curriculum-driven, surpasses teacher on STEM Tiếnhóa của distillation

### Gen 1: copy outputs. Gen 2: copy at scale. Gen 3
copy reasoning. Gen 4: synthesize structured curricu- lum →student vượtteacher. Lưu ý: Legal: OpenAI/Anthropic/Google ToS cấm dùng output để train competing model. Lab/research thường OK; commercial cần legal review. Open alternatives: Llama-3 70B, Qwen- 2.5-72B, Mixtral-8x22B teachers — license cho phépcommercial distillation. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 42 / 49

---

<!-- chiron-source-span: {"source_span_id":"45b8df49-4dc3-57d4-a920-0fc94b4c7c99","locator":{"kind":"page","page":55,"label":"Slide 55","section_title":"Hardwareoptimization — compute vs memorytrade-off","extraction_method":"pdf-text-layer"},"checksum":"aa7d84890cad5b916db8896b1b121bc65b6f1d11151d9aa3fb1c8f63978ec800"} -->

## Slide 55 - Hardwareoptimization — compute vs memorytrade-off

FlashAttention (v1/v2/v3) — Attention exact, nhưng tile-by-tile, giữ data trong SRAM thay vì HBM. 2–4× speedup, O(N) memory thay vì O(N²). v3(HopperH100) thêmasync+ FP8. Gradient checkpointing — Không lưu activations trong forward; recom- pute trong backward. Trade memory cho compute: 30–50% memory savings, 30% slower. Bắt buộc cho long-contextFT.

### Combinecả hai

- FlashAttn ⇒tăngmax sequence
length

- Gradckpt ⇒tăngmax batch size

- BF16mixed precision ⇒ 50%
memory

- NF44-bit ⇒thêm 50%
Orderkhi OOM

1. Mixed precision → 2. Grad ckpt → 3. FlashAttn 2 → 4. 4-bit (QLoRA) → 5. Gradient accumula- tion →6. ZeRO/FSDP (multi-GPU). Giảngviên (VinUni) AICB· Ngày 22 Tuần5 43 / 49

---

<!-- chiron-source-span: {"source_span_id":"87dd321b-9bc2-5323-89e7-c642f4fa41ab","locator":{"kind":"page","page":56,"label":"Slide 56","section_title":"Distributedtraining — ZeRO Stages &FSDP","extraction_method":"pdf-text-layer"},"checksum":"2e53d00a68d8493abbbd35dfefcfcea4af89f5caf36b8ccbf98fe17d4e9ac8f0"} -->

## Slide 56 - Distributedtraining — ZeRO Stages &FSDP

Stage Shard Savings Khinào dùng? Stage0 (DDP) Replicateeverything 1× 1GPU đủ memory ZeRO-1 +Optimizer state 4× 2–4GPUs cùng node ZeRO-2 +Gradients 8× 4–8GPUs cùng node (default) ZeRO-3/ FSDP +Parameters N× Model >single-GPUmemory Quickguide 1 GPU:không cần ZeRO — dùng QLoRA + grad ckpt. 2–8 GPUs: ZeRO-2 (DeepSpeed) hoặc FSDP. >8 GPUs / multi-node:FSDP + selective ckpt;Stage 3 khi cần. Lưu ý: FSDP gotcha: dùng non-reentrant acti- vation checkpointing với FSDP — legacy reentrant variantxungđộtvớiFSDPstatesync. Selectiveac- tivationckpt(PyTorch2024+)thêm 10%throughput. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 44 / 49

---

<!-- chiron-source-span: {"source_span_id":"28587e1b-557b-59b3-96aa-b5af4672c5ef","locator":{"kind":"page","page":57,"label":"Slide 57","section_title":"ModernPEFT variants — DoRA, rsLoRA,PiSSA","extraction_method":"pdf-text-layer"},"checksum":"3933a411a780c63df005f3f3f4d304be6284d8bbd8e4821ca35dfe0de1b91f7a"} -->

## Slide 57 - ModernPEFT variants — DoRA, rsLoRA,PiSSA

DoRA — Weight-Decomposed LoRA (Liu 2024). Táchupdate= magnitude+direction. TốthơnLoRA ởrank thấp. rsLoRA — Rank-Stabilized (Kalajdzievski 2023). Scaling α/√r thay vì α/r ⇒ stable gradient ở rank cao( r = 64–128). PiSSA — Principal SV Adaptation (NeurIPS 2024). Init LoRA bằng top-SVD của W0 thay vì random. +5.16%trên GSM8K (Mistral-7B). Decisionguide Default: LoRA r = 8–16, α = 16–32. Low rank (r ≤ 4): DoRA. High rank (r ≥ 32): rsLoRA.

### Convergence nhanh: PiSSA. VRAM cực hạn
QLoRA+NF4. Lưu ý: 2025: với LR tuning đúng, mọi variant peaktươngđươngvanillaLoRA(Liu2025). Tune LRtrước, đừng over-engineer. Hỗtrợ trong HuggingFace PEFT≥0.10. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 45 / 49

---

<!-- chiron-source-span: {"source_span_id":"b69fe0b6-7e07-5a9d-9129-42842514fd81","locator":{"kind":"page","page":58,"label":"Slide 58","section_title":"Modelmerging — combine fine-tunes màkhông retrain","extraction_method":"pdf-text-layer"},"checksum":"80cea5a1331d6a0e08820394b05342bd4513629aa3e21dda30f8f9c47f13cd94"} -->

## Slide 58 - Modelmerging — combine fine-tunes màkhông retrain

- SLERP:spherical linear interpolation,
merge 2 models dọcđường cầu giữ angle. Đơn giản, hiệuquả khi 2 models sharebase.

- TaskArithmetic:
θmerged = θbase + ∑ i λi(θi − θbase). Cộng/trừ“task vectors”.

- TIES(Trim,Elect Sign, Merge): trim 80%
deltanhỏ nhất, vote sign chung→giảm interference.

- DARE:drop 90–99% delta ngẫu nhiên rồi
rescale. Surprising: vẫngiữperformance.

- DARE-TIES:kết hợp 2 method trên cho
multi-modelmerge. Tooling mergekit(ArceeAI):toolkitchuẩn de-facto. YAML config, support

```text
tất cả methods. pip install
```
mergekit. Usecases Multi-skill: merge math-FT + code-FT + chat-FT. Continual learning: merge base + new- domain FT. Open LLM Leader- board: phần lớn top models 2024 làmerges. Lưu ý:Không merge khác archi- tecture. Cùng base model là điều kiệncần. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 46 / 49

---

<!-- chiron-source-span: {"source_span_id":"68366d60-7a27-5506-b834-fb205446d017","locator":{"kind":"page","page":59,"label":"Slide 59","section_title":"Quantization& serving — training xong,deploy thế nào?","extraction_method":"pdf-text-layer"},"checksum":"7a8a3aa4b12f523c6b2aa0409b5bb6dcaf7c0d8580dabe8e968b6a07ca7ce6a3"} -->

## Slide 59 - Quantization& serving — training xong,deploy thế nào?

### Quantization(training-free)

- NF4(QLoRA):4-bit normal-aware — default FT.

- GPTQ:post-training 4-bit + calibration set.

- AWQ:activation-aware, tốt hơn GPTQ ở4-bit.

- GGUF:format llama.cpp (Q4_K_M…).

### Serving

- vLLM:continuous batching, PagedAttention.

- Speculativedecoding: 2–3×throughput.

- KVcache quant: 8/4-bit cho long-context.

### Advancedtraining & mid-training

- Long-context(mid-train): RoPE scaling —NTK,
YaRN,LongRoPE →4K →128K+.

- MoEfine-tune: FT subset experts.

- Multi-tokenprediction: predictnforward.

- Curriculumlearning: easy-to-hard (Phi-4).

- Pruning: SparseGPT,Wanda—ít phổ biến.
Lưu ý: Đừng dùng tất cả cùng lúc. Thêm từng cái,đo, giữ cái work. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 47 / 49

---

<!-- chiron-source-span: {"source_span_id":"dba375d1-e385-5866-8cf7-97a18759e3ce","locator":{"kind":"page","page":60,"label":"Slide 60","section_title":"Decisiontree — chọn training strategytheo constraint","extraction_method":"pdf-text-layer"},"checksum":"b035284b450a8fad185e10978467de34abd2a1e8cf1ff9f8d5f5ae81d92ab64d"} -->

## Slide 60 - Decisiontree — chọn training strategytheo constraint

1. Cópreferencepairs? ▷ +SFTmodel →DPO/ SimPO ▷ KhôngSFT →ORPO(1-stage) ▷ Chỉ+1/−1 →KTO

2. Cóinstructiondata? →SFT(LoRA/QLoRA),rồi thu preference →DPO.

3. Chỉrawdomain text? ▷ Xabase (medical/legal/code) →DAPT

- TAPT →SFT →DPO.
▷ Gầnbase →skipDAPT,SFT với syntheticdata.

4. Math/code/groundtruth? →sauDPO thêmGRPO +RLVR (Tulu3).

5. Nhiềutask-specificFT modelscầncombine? → Modelmerging (TIES/DARE/SLERP).

6. Cầndeployefficient? →Quantize (NF4/AWQ/GGUF)+ vLLM/llama.cpp + speculative decoding. Lưuý: Reality: hầuhếtenterpriseteamschạy SFT +DPO làđủ. Phần cònlại là “nice to have”. Giảngviên (VinUni) AICB· Ngày 22 Tuần5 48 / 49

---

<!-- chiron-source-span: {"source_span_id":"ba2e5bb2-8c9c-5b8a-babd-94811dd67300","locator":{"kind":"page","page":61,"label":"Slide 61","section_title":"Tổngkết — Key Takeaways","extraction_method":"pdf-text-layer"},"checksum":"17db82cf145ca62363f851fe39aca671f59eb9f092c0dbc9e0f673160c938201"} -->

## Slide 61 - Tổngkết — Key Takeaways

Nhữngý chính cần nhớtrướckhi sang bài tiếp theo 1 DPOvẫn là go-to 2025-2026 —nhưng phảiiterative(Llama3 / Tulu3), khôngone-shot 2 Watch failure modes: likelihood displacement, length hacking.rewards/chosen đảo chiều = stop 3 ORPOkhi base→aligned1 stage; SimPO khi lengthbias là vấn đề; KTOkhichỉ có +1/−1 4 RL trở lại với GRPO + RLVR cho reasoning —không reward model. Stack: SFT→ DPO → RLVR 5 VN-firstmodels dừng ở SFT —Lab 22 Bonus B là cơhội publish DPO-aligned VN model Giảngviên (VinUni) AICB· Ngày 22 Tuần5 48 / 49

---

<!-- chiron-source-span: {"source_span_id":"e3092f58-bcd5-5f78-bc55-78ce4aba5987","locator":{"kind":"page","page":62,"label":"Slide 62","section_title":"Tiếptheo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"74adca9e265062d9be261924798058687f6c170dff7533434c7f435ca92f307a"} -->

## Slide 62 - Tiếptheo & Bài tập

Ngày 23: LangGraph & Agentic Or- chestration “Model đã aligned. Tiếp theo: orches- trate complex workflows với Lang- Graph stateful machines.”

- Hoànthành Lab 22: DPO
alignment+ deploy aligned model

- Đọc: LangGraph documentation
—State, Nodes, Edges Giảngviên (VinUni) AICB· Ngày 22 Tuần5 49 / 49

---

<!-- chiron-source-span: {"source_span_id":"12d8e49d-4c68-52e4-a004-a16a7a60da55","locator":{"kind":"page","page":63,"label":"Slide 63","section_title":"Hỏi& Đáp","extraction_method":"pdf-text-layer"},"checksum":"79e59945f2bd69dc59fac58055dc2eb29dc160b9e5546dd0c49a183f1744047e"} -->

## Slide 63 - Hỏi& Đáp

DPO hay ORPO — bạn sẽ chọn method nào cho project của mình và tại sao?

---

<!-- chiron-source-span: {"source_span_id":"20b35be1-757b-5e07-bada-79d2ffe560a3","locator":{"kind":"page","page":64,"label":"Slide 64","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"20dc3483fce29f2083633dfc1229e28d6fc90ccbe9b374caafe7c8c39fee8097"} -->

## Slide 64 - Cảmơn!

AICB-P2T3 · Ngày 22 · DPO, ORPO & Align- ment — Từ SFT đến Preference Learning github.com/VinUni-AI20k Liên hệ: instructor@vinuni.edu.vn
