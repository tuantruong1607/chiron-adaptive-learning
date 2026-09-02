---
schema_version: 1
course_id: rag-intensive
document_id: "be548f9f-33b3-5eb5-9f81-9770b2213386"
document_version_id: "df6a5f02-f7e8-5d3d-8463-e71a50fe8c95"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "DPO, ORPO & Alignment — phân tích & breakdown từng slide"
source_file: "track-3-day-22.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-22.html"
source_sha256: "02f5caef192b01e277ee28fdbf870942b45fe58eb6ecbdea55d2c083aae41f68"
parser_version: chiron-structured-markdown-v1
html_section_count: 20
interactive_module_count: 3
interactive_control_count: 2
language: vi
---

# DPO, ORPO & Alignment — phân tích & breakdown từng slide

> 64 slide, từ vì sao SFT chưa đủ đến toàn cảnh vòng đời huấn luyện LLM. 
 Bài nối thẳng từ Ngày 21: SFT dạy model nói gì, alignment dạy model 
 nói như thế nào.

<!-- chiron-source-span: {"source_span_id":"930065b5-489e-5988-b3af-cb5e0e0d2c74","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"track-3-day-22.html"},"checksum":"c6d06b12eb802da9e09e39f6afa4e92d056f276d2483e1fd88a1324c8cf66b08"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Bài này dài (64 slide) và chia làm **hai nửa rất khác nhau**. Nửa đầu (chương 1–7) 
 là nội dung cốt lõi về alignment. Nửa sau (chương 8–10) là khảo sát rộng — benchmark, distillation, 
 distributed training, model merging. Đừng đọc hai nửa với cùng một cường độ.

Lượt 1 · ~15 phút

Nắm mạch chính

- Đọc slide 7, 12, 15, 19, 61
- Chạy mô-đun β — 2 phút, giải thích trọn một siêu tham số
- Mục tiêu: nói được vì sao preference data mạnh hơn demonstration data

Lượt 2 · ~60 phút

Chương 1–7 kỹ, 8–10 lướt

- Làm hết phần "Dự đoán trước khi kéo" ở 3 mô-đun
- 3 bài tập bậc thang theo thứ tự
- Chương 10 chỉ cần nắm cây quyết định slide 60

Lượt 3 · ~25 phút

Trước quiz

- 6 hiểu lầm — vùng ra đề nhiều nhất
- Chọn method + cheat sheet
- Từ điển — bài này dày viết tắt hơn mọi bài khác

"Ai dạy model phân biệt good vs bad?"

---

<!-- chiron-source-span: {"source_span_id":"57965699-5e33-53f0-a9ad-6533500526e6","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"track-3-day-22.html"},"checksum":"8e9cb0aecd44184750bd1ca5edf194b36c2c6c6470269c09ef0ba9ebd860fe35"} -->

## 00 Mở đầu

Slide 1–3: vị trí bài học và câu hỏi dẫn dắt.

### Slide 1–2 Trang bìa và câu hỏi dẫn dắt

> Trích slide 
>  "DPO, ORPO & Alignment — Từ SFT đến Preference Learning. 
>  AICB-P2T3 · Ngày 22 · Chương 5 — Fine-tuning & An Toàn" 
>  "RLHF tốn kém — DPO làm được điều tương tự mà không cần reward model?"

Câu hỏi dẫn có một chữ đáng chú ý: **"tương tự"**. Nó không hỏi DPO có *tốt hơn* RLHF không — nó hỏi DPO có đạt *chất lượng tương đương* với chi phí thấp hơn 
 nhiều không. Đó là câu hỏi kỹ thuật đúng, và câu trả lời của bài là "có, phần lớn trường hợp".

"SFT dạy format — DPO/ORPO dạy alignment 
 (helpful + safe). RLHF tốn kém — DPO có thể thay thế?"

tệ hơn

### Slide 3 Nội dung bài học

> Trích slide 
>  "1. Tại sao SFT chưa đủ? 2. RLHF — Bức tranh toàn cảnh 3. DPO — Direct Preference Optimization 
>  4. ORPO, SimPO & Alternatives 5. RL comeback — GRPO & RLVR 6. Preference Data & Implementation 
>  7. Constitutional AI & Red-teaming 8. Đánh giá Alignment — LLM Benchmarks 9. Demo & Thực hành 
>  10. Bức tranh toàn cảnh — Full training flow"

Mười chương, nhưng **trọng lượng rất không đều**. Đọc theo bảng này để phân bổ thời gian:

| Chương | Slide | Vai trò | Mức ưu tiên |
| --- | --- | --- | --- |
| 1–3 · SFT chưa đủ, RLHF, DPO | 4–16 | Lõi của bài. Mọi thứ sau đều tham chiếu về đây | Cao nhất |
| 4 · ORPO/SimPO/KTO | 17–21 | Bảng chọn method — nội dung ra đề nhiều | Cao |
| 5 · GRPO & RLVR | 22–25 | Xu hướng 2025; không có trong lab | Trung bình |
| 6 · Preference data | 26–32 | Phần thực hành; có mục Việt Nam đáng chú ý | Cao |
| 7 · CAI & Red-teaming | 33–36 | Cách tạo preference data không cần người | Trung bình |
| 8 · Đánh giá alignment | 37–42 | Khảo sát benchmark — nhiều tên, ít khái niệm mới | Trung bình |
| 9 · Demo & Lab | 43–49 | Hướng dẫn lab | Cao nếu làm lab |
| 10 · Toàn cảnh | 50–60 | Khảo sát rộng — DAPT, distillation, ZeRO, merging, quantization | Lướt, trừ slide 60 |

mười chủ đề độc lập

slide 51

slide 60

---

<!-- chiron-source-span: {"source_span_id":"92f9c288-bcb8-5b5a-a7d5-6be16c5e13a1","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Tại sao SFT chưa đủ?","source_file":"track-3-day-22.html"},"checksum":"60d3590b184110c61ff00a8f02927361c6020e38e1d84fe9ccbd406e78f6b852"} -->

## 01 Tại sao SFT chưa đủ?

Slide 4–7: SFT dạy "nói gì", alignment dạy "nói như thế nào" — và vì sao 
 preference data chứa thông tin mà demonstration data không bao giờ có.

### Slide 4–5 SFT dạy format — Alignment dạy hành vi

> Trích slide 
>  "Pre-trained (raw knowledge) → instruction → SFT (format + style) → preference → Alignment (helpful + safe) 
>  Biết nhiều, nói bừa · Biết trả lời, chưa biết chọn · Chọn câu tốt hơn 
>  Post-training pipeline hiện đại: 1. SFT: Dạy model format câu trả lời (instruction following). 
>  2. Alignment: Dạy model phân biệt tốt/xấu (helpful, harmless, honest) 
>  SFT dạy model "nói gì". DPO/ORPO dạy model "nói như thế nào" — concise, helpful, an toàn. "

_Sơ đồ: Ba giai đoạn post-training và thứ mỗi giai đoạn dạy được - Model pre-trained có kiến thức thô nhưng nói bừa. SFT dùng dữ liệu instruction để dạy format, cho ra model biết trả lời nhưng chưa biết chọn. Alignment dùng dữ liệu preference để dạy model chọn câu tốt hơn, cho ra model helpful và safe._

Hình 1 — Ba giai đoạn post-training (slide 5).

không nên

### Slide 6 SFT-only: vấn đề gì xảy ra?

> Trích slide 
>  " SFT-only output: Over-hedges, verbose · Generic, không actionable · Refusal quá mức 
>  After Alignment: Direct, concise · Actionable, helpful · Balanced safety 
>  Alignment — Quá trình dạy model phân biệt câu trả lời tốt vs xấu bằng preference data — 
>  không phải dạy thêm kiến thức mới. 
>  InstructGPT 1.3B với RLHF > GPT-3 175B không RLHF ⇒ Alignment beats scale (Ouyang et al. 2022)"

Con số cuối slide là con số đáng nhớ nhất của cả bài: **một model nhỏ hơn 134 lần 
 được align tốt thắng một model khổng lồ không được align**.

alignment là một trục cải thiện khác với scale

human preference trên tác vụ instruction-following

"không phải dạy thêm kiến thức mới"

Hình 1

Ba triệu chứng của SFT-only đáng thuộc, vì chúng là thứ bạn sẽ *nhìn thấy* trong lab:

| Triệu chứng | Nghĩa là gì | Vì sao SFT gây ra |
| --- | --- | --- |
| Over-hedges, verbose | Rào trước đón sau, dài dòng | Dữ liệu SFT thường là câu trả lời "an toàn"; model bắt chước cả sự dài dòng |
| Generic, không actionable | Đúng nhưng vô dụng | Model học phân phối trung bình của data — trung bình thì luôn chung chung |
| Refusal quá mức | Từ chối cả câu hỏi vô hại | Không có tín hiệu nào nói "từ chối chỗ này là quá đà " — SFT chỉ thấy ví dụ từ chối đúng |

### Slide 7 Vì sao preference data mạnh hơn demonstration data

> Trích slide 
>  "SFT chỉ thấy 'good' → không biết good hơn bad bao nhiêu 
>  SFT (demonstration): "Bắt chước câu này." ⇒ Học distribution của data. 
>  Preference (DPO/RLHF): "Câu A tốt hơn câu B." ⇒ Học margin giữa good vs bad. 
>  Information signal: Một preference pair (y_w, y_l) chứa thông tin về cái gì KHÔNG nên nói — 
>  điều mà SFT data không bao giờ biểu lộ trực tiếp. "

**Đây là slide quan trọng nhất của chương 1**, và cặp từ *distribution* vs *margin* là cặp từ đáng học thuộc.

Dạy ai đó viết email chuyên nghiệp:

**Cách SFT:** đưa 1.000 email hay và nói "viết như thế này". 
 Người học bắt chước được *trung bình* của 1.000 email đó. Nhưng nếu 300 email trong đó 
 dài dòng một cách vô hại, người học cũng học luôn cái dài dòng — vì không ai nói rằng nó dở.

**Cách preference:** đưa 1.000 *cặp*, mỗi cặp một email hay và một email dở 
 cho cùng tình huống, nói "cái này tốt hơn cái kia". Bây giờ người học thấy được **chiều của sự cải thiện**, không chỉ đích đến.

Cùng công sức thu thập, cặp thứ hai chứa nhiều thông tin hơn hẳn — vì nó mã hoá được 
 cái mà chỉ nhìn ví dụ tốt thì không bao giờ suy ra được.

N cặp so sánh thường giá trị hơn N câu trả lời mẫu

dễ gán nhãn hơn

KTO

thumbs up / thumbs down

#### Ô kiểm tra — Chương 1

Trả lời thành tiếng trước khi mở đáp án.

**1.** Vì sao một preference pair chứa nhiều thông tin hơn một câu trả lời mẫu, 
 dù cả hai đều tốn công gán nhãn tương đương? Hiểu

#### Đáp án

Vì nó mã hoá được **cái KHÔNG nên nói**. Demonstration data chỉ chứa ví dụ tốt, 
 nên model học được *phân phối* của dữ liệu — nó biết đích đến nhưng không biết 
 chiều nào là cải thiện.

Preference pair cho model thấy **margin** giữa tốt và xấu. Cùng một prompt, 
 hai câu trả lời, một cái hơn — đó là thông tin về *hướng*, không chỉ về vị trí.

*Điểm cộng nếu bạn nói thêm:* gán nhãn so sánh còn *dễ và nhất quán hơn* việc tự viết câu trả lời hoàn hảo, nên trên thực tế cùng ngân sách sẽ thu được nhiều cặp hơn 
 là số câu mẫu chất lượng cao.

**2.** "InstructGPT 1.3B > GPT-3 175B" có nghĩa là scale không quan trọng? Đánh giá

#### Đáp án

**Không.** Nó nói alignment là một *trục cải thiện khác* với scale, 
 và ở thời điểm đó trục ấy chưa ai khai thác.

Phép đo là **human preference trên tác vụ instruction-following**. GPT-3 175B 
 vẫn biết nhiều hơn nhiều — nó chỉ *trả lời* tệ hơn. Nếu đo bằng MMLU (kiến thức) 
 thay vì preference, kết quả sẽ ngược lại.

**Bài học chuyển giao:** luôn hỏi *"đo bằng gì?"* trước khi diễn giải một 
 so sánh model. Đây cũng đúng cho mọi con số ở [chương 8](#c8).

**3.** Model của bạn từ chối cả những câu hỏi vô hại. Thêm dữ liệu SFT 
 có sửa được không? Áp dụng

#### Đáp án

**Rất khó.** "Refusal quá mức" là hành vi *quá đà theo một chiều*. 
 Dữ liệu SFT chỉ cho model thấy ví dụ tốt — bạn có thể thêm ví dụ "trả lời thay vì từ chối", 
 nhưng model không có cách nào biết ranh giới nằm ở đâu, vì không có tín hiệu nói 
 "từ chối *ở chỗ này* là quá".

**Cách đúng:** preference pair với cùng prompt — chosen = trả lời hữu ích, 
 rejected = từ chối không cần thiết. Bây giờ model thấy được ranh giới.

*Đây là ví dụ trực tiếp của cột "Refusal quá mức" ở [slide 6](#s6)* — 
 và cũng là lý do slide gọi alignment là dạy "balanced safety" chứ không phải "more safety".

---

<!-- chiron-source-span: {"source_span_id":"c35ed2b5-a6db-59a9-b4b1-62f1082e4f53","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 RLHF — Bức tranh toàn cảnh","source_file":"track-3-day-22.html"},"checksum":"e55889dac3352dee9ed008b79e54d9a1032ed2b3da66ff633d741eb63477d6e5"} -->

## 02 RLHF — Bức tranh toàn cảnh

Slide 8–10: hiểu RLHF để thấy vì sao DPO là bước cải tiến, chứ không phải 
 một method song song.

### Slide 9 RLHF Pipeline — kiến trúc 3 giai đoạn của InstructGPT

> Trích slide 
>  "Stage 1 SFT (dạy format) → Stage 2 Reward Model (human rank pairs) → Stage 3 PPO (optimize policy) 
>  Training data cần chuẩn bị kỹ · RM training unstable · PPO hyperparams rất sensitive 
>  RLHF pipeline phức tạp: 3 models, 3 stages, nhiều hyperparams ⇒ chỉ frontier labs 
>  (OpenAI, Anthropic) có đủ resources để dùng. 
>  Analogy: RLHF = thuê giám khảo chấm điểm, rồi dùng điểm đó dạy lại model chính. 
>  Tốn kém gấp đôi."

Phép so sánh "thuê giám khảo" là phép so sánh trung tâm của cả bài — DPO sẽ được định nghĩa 
 chính xác bằng cách *bỏ giám khảo đi*. Đáng bóc tách kỹ ba giai đoạn:

| Giai đoạn | Làm gì | Rủi ro riêng của giai đoạn |
| --- | --- | --- |
| 1 · SFT | Dạy model format câu trả lời | Ít rủi ro nhất — đây là phần Ngày 21 đã làm |
| 2 · Reward Model | Train một model riêng để chấm điểm câu trả lời, học từ human ranking | RM training unstable. Và RM là một model có thể bị hack — xem reward hacking ở slide 10 |
| 3 · PPO | Dùng điểm của RM làm reward, tối ưu policy bằng RL | PPO hyperparams rất sensitive. RL online, cần rollout, dễ sụp |

3 model theo 3 giai đoạn

thời điểm chạy PPO

mô-đun bộ nhớ

### Slide 10 RLHF: kết quả tốt nhưng chi phí cao

> Trích slide 
>  " 3 Models cần train đồng thời · Cao PPO instability, reward hacking · 
>  $$$$ Chi phí tổng (infra + annotators) 
>  Câu hỏi then chốt: Nếu ta có thể bỏ Reward Model và train trực tiếp trên preference data thì sao? 
>  ⇒ Đó chính là ý tưởng của DPO. "

model

điểm của RM

chất lượng thật

RLVR ở slide 24

kiểm tra programmatic

không có "judge" để hack

---

<!-- chiron-source-span: {"source_span_id":"f63333cc-69ed-519d-85f7-2eb06fec0fe4","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 DPO — Direct Preference Optimization","source_file":"track-3-day-22.html"},"checksum":"27ac399de33d5555bf17ee71ccbef01e5902c5c8ec090792263634988632b7bb"} -->

## 03 DPO — Direct Preference Optimization

Slide 11–16: bỏ reward model, train trực tiếp trên cặp tốt/xấu — và ba kiểu 
 hỏng mà "training thành công" vẫn che giấu được.

### Slide 11–12 Ý tưởng cốt lõi

> Trích slide 
>  "DPO (Rafailov et al. 2023) — Key insight: optimal RLHF policy có closed-form solution. 
>  Vì vậy ta có thể train trực tiếp trên preference data mà không cần Reward Model. 
>  Analogy: RLHF = thuê giám khảo chấm điểm rồi dùng điểm đó dạy lại. DPO = cho model xem trực tiếp 
>  cặp tốt/xấu, tự học phân biệt — bỏ qua giám khảo trung gian. 
>  DPO loss: binary cross-entropy trên log-ratio chosen vs rejected probabilities."

_Sơ đồ: So sánh pipeline RLHF ba thành phần với DPO hai thành phần - RLHF đi từ SFT model qua reward model rồi PPO training mới ra aligned model. DPO đi thẳng từ SFT model qua một bước DPO training trên preference pairs ra aligned model, bỏ hoàn toàn reward model._

Hình 2 — RLHF vs DPO (slide 9 + 14).

lớp lỗi

### Slide 13 Suy dẫn DPO — 3 bước từ Bradley-Terry đến loss

> Trích slide 
>  "1. Bradley-Terry: P(y_w ≻ y_l | x) = σ(r(x,y_w) − r(x,y_l)) 
>  2. Optimal policy (KL-RL): π*(y|x) ∝ π_ref(y|x)·e^{r(x,y)/β} 
>  3. Invert ⇒ DPO loss: r = β·log(π*/π_ref), thay vào (1) ⇒ no RM! 
>  Magic trick: "Closed-form optimal policy" (bước 2) là chìa khoá. Nếu không có nó, ta không thể 
>  bỏ Reward Model. DPO chỉ áp dụng được cho objective dạng KL-regularized RL — không phải mọi RL setup. 
>  L_DPO = − log σ( β·log[π_θ(y_w)/π_ref(y_w)] − β·log[π_θ(y_l)/π_ref(y_l)] )"

#### Đọc ba bước bằng lời — không cần giải phương trình

1. Bradley-Terry là mô hình cổ điển cho so sánh cặp: xác suất A thắng B 
 là hàm sigmoid của hiệu điểm giữa hai bên. Nó cho ta một cách viết 
 "preference" thành công thức, với điều kiện có hàm điểm r.
2. Optimal policy có dạng đóng. Với bài toán RL bị phạt KL (đúng dạng RLHF dùng), 
 policy tối ưu không cần đi tìm — nó có công thức: bằng ref model nhân với 
 e^(r/β). Đây là bước duy nhất cần toán, và là bước làm nên tất cả.
3. Đảo ngược. Nếu π* tính được từ r, thì ngược lại r cũng tính được từ π*: 
 r = β·log(π*/π_ref). Thay biểu thức này của r vào công thức Bradley-Terry 
 ở bước 1 → r biến mất khỏi bài toán. Không cần train reward model nữa, 
 vì reward đã được biểu diễn qua chính policy.

"DPO chỉ áp dụng được cho objective dạng KL-regularized RL — không phải mọi RL setup."

không

riêng

GRPO ở chương 5

`L = − log σ( β·Δ )` trong đó `Δ = log[π_θ(y_w)/π_ref(y_w)] − log[π_θ(y_l)/π_ref(y_l)]`.

**Δ là "margin"**: model hiện tại đã đẩy xác suất câu *chosen* lên 
 (so với ref) nhiều hơn bao nhiêu so với câu *rejected*.

• Δ > 0 → model đang phân biệt đúng chiều. Δ càng lớn, loss càng nhỏ. 
 • Δ = 0 → model chưa phân biệt được. `σ(0)=0,5`, loss = `−log 0,5 ≈ 0,69`. 
 • Δ < 0 → model đang ưu tiên câu *xấu*. Loss lớn, gradient đẩy mạnh.

**β nhân vào Δ** — nó điều khiển sigmoid bão hoà nhanh hay chậm. 
 Đó chính là nội dung của [slide 15](#s15) và của mô-đun ngay dưới đây.

Và chú ý dòng cuối slide: *"Forward pass qua π_θ và π_ref trên (prompt, y_w, y_l). 
 Không rollout, không PPO clipping."* — DPO là **supervised learning** trên dữ liệu tĩnh, không phải RL. Đó là nguồn gốc của tính ổn định.

### Slide 14–15 β — siêu tham số kiểm soát mức độ alignment

> Trích slide 
>  "β = 0.05 Tự do cao · β = 0.1 (standard) Cân bằng · β = 0.2 (conservative) Gần ref model 
>  β (KL penalty) — β cao ⇒ model bị giữ gần ref model hơn. β thấp ⇒ model tự do "rời xa" ref model 
>  để optimize preference. 
>  ■ Bắt đầu β = 0.1 (default) ■ Nếu model quá conservative ⇒ giảm xuống 0.05 
>  ■ Nếu model "quên" kiến thức ⇒ tăng lên 0.2 
>  IPO: variant fix length bias — drop-in replacement cho DPO. 
>  DPO advantages: Offline learning (stable) · Ít components: chỉ 1 model + ref · 
>  Quality tương đương RLHF trên benchmarks 
>  Known issues: length bias, ref model dependency, overfitting trên small datasets. "

Slide nói β cao thì "giữ gần ref hơn", nhưng không nói *vì sao*. Lý do nằm ngay trong 
 công thức reward ngầm ở slide 13: `r = β·log(π_θ/π_ref)`.

khoảng cách reward

β·Δ

Δ cần thiết = (mức reward mong muốn) ÷ β

độ lệch log-xác suất so với ref model

#### Tương tác β kiểm soát ràng buộc với ref model như thế nào

Trục ngang là **Δ** — độ lệch log-xác suất giữa chosen và rejected so với 
 ref model. Trục dọc là `σ(β·Δ)`, tức mức độ model đã "chắc chắn" rằng chosen tốt hơn.

Với **β = 0,1** (mặc định), model cần Δ khoảng **22** để đạt độ chắc chắn 90%. 
 Đoán trước: đổi sang **β = 0,2** (conservative) thì Δ cần thiết thành bao nhiêu?

#### Kéo β lên 0,20 rồi mở

**Còn khoảng 11 — đúng một nửa.** Quan hệ là nghịch đảo tuyến tính: `Δ = ln(9)/β ≈ 2,197/β`.

**Vì sao đây là ý nghĩa thật của "conservative":** β cao *không* làm model 
 học chậm hơn. Nó làm model **đạt mục tiêu bằng cách lệch khỏi ref ít hơn**. 
 Cùng một mức phân biệt chosen/rejected, nhưng π_θ ở gần π_ref hơn — nên kiến thức từ SFT 
 ít bị xáo trộn.

Ngược lại β = 0,05 cần Δ ≈ 44 — gấp bốn lần β = 0,2. Model phải rời xa 
 ref nhiều hơn hẳn, và đó chính xác là lúc slide cảnh báo model có thể *"quên" kiến thức*.

**Bài học mang đi — cách đọc lời khuyên của slide:**

• *"Model quá conservative ⇒ giảm β xuống 0,05"* = cho phép model lệch xa hơn để 
 thoả preference. 
 • *"Model quên kiến thức ⇒ tăng β lên 0,2"* = buộc model bám ref, đánh đổi bằng việc 
 alignment nông hơn.

β không phải "learning rate của alignment". Nó là **bán kính cho phép đi khỏi model gốc**.

*Thử thêm:* kéo β về 0,05 và nhìn đường cong gần như phẳng ở nửa trái biểu đồ. 
 Gradient nhỏ trên một dải Δ rất rộng — model bị đẩy đi rất xa trước khi loss "hài lòng". 
 Đó là cơ chế vật chất của hiện tượng *quên kiến thức*.

- **Control - β 0,10**: min `5`, max `50`, step `1`, default `10`

- **Control - Ngưỡng chắc chắn mục tiêu 90%**: min `55`, max `99`, step `1`, default `90`

Δ cần để đạt ngưỡng

—

độ lệch log-xác suất khỏi ref

So với β = 0,10

—

cần lệch nhiều hay ít hơn

Chế độ

—

—

Gradient tại Δ = 0

—

lực đẩy ban đầu = β/2

β hiện tại β = 0,10 (chuẩn) ngưỡng mục tiêu

#### Xem dạng bảng



#### Công thức & giới hạn của mô hình

- Từ chính DPO loss ở slide 13: L = −log σ(β·Δ), nên xác suất ngầm mà model 
 gán cho "chosen thắng" là σ(β·Δ).
- Δ cần để đạt ngưỡng p: Δ = logit(p)/β = ln(p/(1−p))/β. 
 Với p = 0,9 thì logit = 2,197.
- Gradient theo Δ: dL/dΔ = −β·σ(−β·Δ), độ lớn tại Δ=0 bằng β/2.
- Đây là mô hình một cặp, không phải mô phỏng training. Nó cho thấy quan hệ 
 β ↔ độ lệch cần thiết, không dự đoán được model của bạn sẽ đạt Δ bao nhiêu sau bao nhiêu bước.
- Đơn vị của Δ là log-xác suất cộng dồn trên cả response, nên giá trị tuyệt đối phụ thuộc 
 độ dài câu — chính điều này dẫn tới length bias ở slide 16.

### Slide 16 DPO failure modes — khi training "thành công" nhưng model tệ hơn

> Trích slide 
>  " Likelihood displacement (Razin 2024) — prob của chosen giảm khi train; 
>  khi chosen ≈ rejected, mass dồn sang token ngược nghĩa ⇒ unalignment. 
>  Length hacking — DPO thưởng response dài (nhiều log-prob mass). Học "viết dài" 
>  thay vì "viết tốt". 
>  Mode collapse / sycophancy — mọi câu mở đầu "Great question!" — over-fit preference style. 
>  Triệu chứng trên TRL logs: ■ rewards/chosen giảm ⇒ likelihood displacement 
>  ■ rewards/margins âm/co ⇒ optimization conflict ■ Length tăng >30% ⇒ length hacking 
>  Mitigations: Filter pairs có gap quá nhỏ; dùng SimPO/IPO; stop sớm khi rewards/chosen đảo chiều. "

**Đây là slide dễ ra đề nhất của chương 3**, vì nó là chỗ duy nhất mô tả những kiểu hỏng 
 mà loss vẫn giảm đẹp. Ba failure mode, đọc theo cơ chế:

| Failure mode | Cơ chế | Triệu chứng trên log | Xử lý |
| --- | --- | --- | --- |
| Likelihood displacement | DPO chỉ tối ưu hiệu Δ. Hạ xác suất rejected cũng làm Δ tăng — nên model có thể hạ cả hai, miễn rejected hạ nhiều hơn | rewards/chosen giảm | Stop sớm; lọc cặp có gap quá nhỏ |
| Length hacking | Δ là tổng log-prob trên cả câu. Câu dài có nhiều token hơn ⇒ nhiều "mass" hơn ⇒ dễ đẩy Δ lên bằng cách viết dài | Độ dài tăng > 30% | SimPO (length-normalized) hoặc IPO |
| Mode collapse / sycophancy | Over-fit phong cách của preference data thay vì nội dung. Mọi câu mở đầu giống nhau | Output đồng dạng bất thường | Đa dạng hoá dữ liệu; giảm epoch |

Trực giác nói: train DPO thì xác suất câu tốt phải *tăng*. Nhưng loss chỉ quan tâm tới **hiệu** `Δ = (log-ratio chosen) − (log-ratio rejected)`.

Có *hai* cách làm Δ tăng: đẩy chosen lên, hoặc **dìm rejected xuống**. 
 Cách thứ hai thường rẻ hơn về mặt gradient. Nếu chosen và rejected quá giống nhau, 
 dìm rejected sẽ kéo chosen xuống theo — và xác suất bị đẩy sang những token *chẳng liên quan gì tới cả hai*. Slide gọi đúng tên: *"mass dồn sang token ngược nghĩa 
 ⇒ unalignment"*.

**Vì sao mitigation là "filter pairs có gap quá nhỏ":** cặp mà chosen ≈ rejected 
 chính là cặp gây ra hiện tượng này. Chúng cũng là cặp mang ít thông tin nhất — 
 loại đi vừa an toàn vừa không mất mát gì.

DPOTrainer

trước

rewards/chosen

tăng

rewards/rejected

giảm

rewards/margins

nở rộng dần

#### Ô kiểm tra — Chương 3

**1.** Vì sao DPO bỏ được reward model, và vì sao mẹo đó không áp dụng 
 cho mọi bài toán RL? Hiểu

#### Đáp án

Vì bài toán RLHF là **KL-regularized RL**, và dạng đó có *closed-form optimal policy*: `π* ∝ π_ref·e^(r/β)`. Có công thức đó thì đảo ngược được 
 thành `r = β·log(π*/π_ref)` — reward được biểu diễn **qua chính policy**, 
 nên thay vào Bradley-Terry là r biến mất.

**Không tổng quát** vì bước 2 mới là chìa khoá, và nó chỉ đúng cho objective 
 dạng KL-regularized. Slide nói thẳng: *"DPO chỉ áp dụng được cho objective dạng 
 KL-regularized RL — không phải mọi RL setup."*

*Hệ quả:* bài toán reasoning ở chương 5 không có dạng đó, nên GRPO vẫn phải là RL thật.

**2.** Training chạy 3 epoch, loss giảm đều, nhưng `rewards/chosen` đi xuống. Chuyện gì đang xảy ra và làm gì? Phân tích

#### Đáp án

**Likelihood displacement.** Loss chỉ tối ưu *hiệu* Δ, nên model đang làm 
 Δ tăng bằng cách *dìm rejected xuống mạnh hơn* thay vì đẩy chosen lên — và kéo chosen 
 xuống theo.

Khi chosen ≈ rejected, xác suất bị đẩy sang token không liên quan tới cả hai — 
 slide gọi là *unalignment*. Model tệ hơn cả trước khi train.

**Xử lý theo slide:** ① dừng sớm ngay khi `rewards/chosen` đảo chiều; 
 ② lọc bỏ cặp có gap quá nhỏ (chính chúng gây ra); ③ chuyển sang IPO hoặc SimPO.

*Nguyên tắc mang đi:* với DPO, **loss không phải chỉ số sức khoẻ**. 
 Ba đường `rewards/*` mới là.

**3.** Model sau DPO trả lời dài hơn 45% so với trước, và judge chấm điểm cao hơn. 
 Đây là thành công? Đánh giá

#### Đáp án

**Rất nhiều khả năng là length hacking**, không phải cải thiện thật. 
 Slide đặt ngưỡng cảnh báo ở **> 30%**; 45% vượt xa.

Hai cơ chế cộng hưởng: ① Δ là tổng log-prob trên cả câu nên câu dài dễ đẩy Δ lên; 
 ② [judge cũng thiên vị câu dài](#s40) (slide 40 gọi length bias là failure mode 
 lớn nhất của judge trước 2024). Nên bạn đang đo một cái bias bằng một cái bias khác.

**Cách kiểm chứng:** chấm lại bằng **AlpacaEval 2 LC** — 
 bản length-controlled (Dubois 2024) sinh ra chính để sửa lỗi này. Nếu điểm sụp khi 
 kiểm soát độ dài, bạn đã có câu trả lời.

**Sửa:** SimPO (length-normalized reward) hoặc IPO.

---

<!-- chiron-source-span: {"source_span_id":"d4e18fc5-4876-5212-b63b-e85026f6d22a","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 ORPO, SimPO & Alternatives","source_file":"track-3-day-22.html"},"checksum":"116893dd6f664aad9fadbfd42843648cc363a012bbf00073221c1ce0a2cb0527"} -->

## 04 ORPO, SimPO & Alternatives

Slide 17–21: dòng thời gian alignment, bảng chọn method, và ba hướng đi sau DPO — 
 mỗi cái bỏ thêm một thành phần.

### Slide 17–18 Dòng thời gian 2022 → 2026

> Trích slide 
>  " 2022 PPO-RLHF · InstructGPT · 3 models — 2023 DPO · No RM (Rafailov) — 
>  2024 ORPO · SimPO · KTO · No ref / no SFT · 1 stage · Llama 3 · Tulu 3 · Iterative DPO + RLVR — 
>  2025 GRPO · R1 · RL comeback (no value model) 
>  Cốt truyện: 2022: RLHF nặng, 3 models, PPO unstable. 2023: DPO — toán bỏ được RM. 
>  2024: method nở rộ, mỗi method bỏ thêm một thứ (ref model, SFT stage, length bias). 
>  2025: RL trở lại với GRPO/RLVR — nhưng không reward model. 
>  Tooling đổi liên tục, nhưng câu hỏi không đổi: "Ai dạy model phân biệt good vs bad?" 
>  Khi câu trả lời là người → RLHF/DPO. Khi là code/regex → RLVR. Khi là chính model → 
>  Self-Rewarding / CAI. "

_Sơ đồ: Dòng thời gian alignment từ 2022 đến 2025 - Năm 2022 RLHF dùng PPO với ba model. Năm 2023 DPO bỏ reward model. Năm 2024 ORPO, SimPO và KTO bỏ thêm ref model và giai đoạn SFT. Năm 2025 GRPO và RLVR đưa RL trở lại nhưng bỏ value model._

Hình 3 — Dòng thời gian alignment (slide 18).

bỏ đi

### Slide 19 Method matrix — chọn alignment method nào?

> Trích slide 
>  "RLHF (PPO) — RM Có · Ref Có · 3 stages · Frontier labs, max quality 
>  DPO — RM Không · Ref Có · 2 · Go-to production alignment 
>  IPO — Không · Có · 2 · DPO over-fit deterministic prefs 
>  SimPO — Không · Không · 2 · Length-norm, less VRAM 
>  ORPO — Không · Không · 1 · Base → aligned 1 stage 
>  KTO — Không · Có · 2 · Chỉ có thumbs up/down 
>  GRPO — Không · Có · 1 RL · Reasoning + RLVR 
>  Quick rules: Có SFT + pref pairs ⇒ DPO. No SFT ⇒ ORPO. Chỉ +1/−1 ⇒ KTO. 
>  Math/code ⇒ GRPO + RLVR. 
>  DPO vẫn là baseline tốt nhất 2025-2026. Chuyển method khác chỉ khi có lý do cụ thể 
>  (VRAM, no SFT, reasoning). "

**Đây là slide ra đề nhiều nhất của cả bài.** Bảng gốc có 4 cột; 
 thêm cột "bỏ đi cái gì" thì nó tự giải thích được:

| Method | RM? | Ref? | Stage | Bỏ đi cái gì so với bậc trước | Dùng khi |
| --- | --- | --- | --- | --- | --- |
| RLHF (PPO) | Có | Có | 3 | — (điểm khởi đầu) | Frontier lab, cần chất lượng tối đa |
| DPO | Không | Có | 2 | reward model | Mặc định cho production |
| IPO | Không | Có | 2 | — (sửa length bias của DPO) | DPO over-fit preference tất định |
| SimPO | Không | Không | 2 | ref model | VRAM hạn chế · length bias là vấn đề |
| ORPO | Không | Không | 1 | ref model + giai đoạn SFT | Đi thẳng từ base model, không có SFT |
| KTO | Không | Có | 2 | yêu cầu dữ liệu dạng cặp | Chỉ có thumbs up/down từ production |
| GRPO | Không | Có | 1 RL | value/critic model | Reasoning có ground truth (math, code) |

mặc định là DPO

lý do cụ thể

### Slide 20–21 SimPO vs KTO vs ORPO — ba hướng đi sau DPO

> Trích slide 
>  SimPO (Meng et al. 2024) — Reference-free, không cần π_ref. Implicit reward = 
>  average log-prob của response (length-normalized). + Target margin γ. Kết quả: +6.4 trên 
>  AlpacaEval 2, +7.5 trên Arena-Hard so với DPO. Top SimPO model (Gemma-2-9B-it) đạt 
>  72.4% LC win-rate. Khi nào dùng: VRAM hạn chế, length bias là vấn đề lớn. 
>  KTO (Ethayarajh et al. 2024) — Single-signal, không cần preference pairs. 
>  Mỗi example chỉ cần label good/bad (+1/−1). Loss dựa trên prospect theory (Kahneman-Tversky). 
>  Lợi thế thực tế: dữ liệu thumbs-up/down từ production logs dễ thu thập hơn nhiều so với ranked pairs. 
>  ORPO — Base → SFT+Alignment trong một training run. 50% VRAM reduction · 
>  1 stage thay vì 2 · không cần ref model. Trade-off: đơn giản hơn nhưng ít mature hơn DPO.

**SimPO giải ràng buộc *bộ nhớ và length bias*.** Bằng cách chuẩn hoá reward 
 theo độ dài (average log-prob thay vì tổng), nó cắt đúng cơ chế gây length hacking ở slide 16 — 
 và bỏ luôn ref model nên nhẹ hơn.

**KTO giải ràng buộc *dữ liệu*.** Nó không cần cặp. Nếu bạn có log 
 thumbs-up/down từ người dùng thật — thứ mà mọi sản phẩm đều có — thì KTO dùng được ngay, 
 còn DPO thì không.

**ORPO giải ràng buộc *quy trình*.** Nó gộp SFT và alignment vào một lần chạy. 
 Dùng khi bạn đi thẳng từ base model và không muốn (hoặc không có) một checkpoint SFT riêng.

Ba câu hỏi khác nhau: *thiếu VRAM?* · *thiếu dữ liệu dạng cặp?* · *thiếu bước SFT?* Trả lời đúng câu hỏi thì chọn đúng method.

của chính bài báo SimPO

mature hơn

mục con số cần kiểm chứng

#### Tương tác Chọn method — theo đúng cây quyết định của slide 19 & 60

Trả lời ba câu hỏi về ràng buộc của bạn. Kết quả là method mà slide khuyến nghị, 
 kèm lý do và slide tham chiếu — dùng để tự kiểm trước quiz.

Bạn có gì làm điểm xuất phát?

Đã có SFT checkpoint

Chỉ có base model, chưa SFT

Dữ liệu phản hồi ở dạng nào?

Cặp so sánh (chosen / rejected)

Chỉ có thumbs up / down (+1 / −1)

Có ground truth kiểm được bằng code

Chưa có gì

Ràng buộc lớn nhất?

Không có ràng buộc đặc biệt

VRAM hạn chế

Model viết dài lê thê (length bias)

Cần chất lượng tối đa, không quan tâm chi phí

Method khuyến nghị

—

—

Số stage

—

—

Cần ref model?

—

ảnh hưởng trực tiếp tới VRAM

Slide tham chiếu

—

quay lại đọc khi cần

#### Luật quyết định lấy từ đâu

- Quick rules nguyên văn slide 19: "Có SFT + pref pairs ⇒ DPO. No SFT ⇒ ORPO. 
 Chỉ +1/−1 ⇒ KTO. Math/code ⇒ GRPO + RLVR."
- Cây quyết định slide 60, mục 1–4.
- Nhánh "VRAM hạn chế / length bias ⇒ SimPO" từ slide 20; "chất lượng tối đa ⇒ RLHF-PPO" từ slide 19.
- Đây là gợi ý theo slide, không phải chân lý. Slide 19 nhấn mạnh: DPO là baseline, 
 đổi method chỉ khi có lý do cụ thể.

---

<!-- chiron-source-span: {"source_span_id":"d5ce993a-d9c4-549a-b1e1-5095b985bfed","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 RL comeback — GRPO & RLVR","source_file":"track-3-day-22.html"},"checksum":"c14d275cd4075da9e824007c5ab1756bfb316bb6ac143418cc22a78ffe603060"} -->

## 05 RL comeback — GRPO & RLVR

Slide 22–25: năm 2025 RL trở lại cho reasoning, nhưng không còn reward model — 
 và không thay thế preference learning.

### Slide 22–23 GRPO — PPO không có value model

> Trích slide 
>  "Prompt x → y₁ y₂ y₃ … y_G → r₁ r₂ r₃ … r_G → r̄ = (1/G)·Σrᵢ (group mean) → 
>  Advantage Aᵢ = (rᵢ − r̄)/std(r) — không cần value/critic model! 
>  GRPO — Group Relative Policy Optimization. Lấy trung bình reward của nhóm G samples cho cùng prompt 
>  làm baseline — thay thế cho value model trong PPO. 
>  ■ PPO clipping ratio như cũ ■ Bỏ value head ⇒ 50% memory savings 
>  ■ Dùng cho DeepSeekMath, sau đó DeepSeek-R1 (Jan 2025)"

_Sơ đồ: GRPO dùng trung bình nhóm làm baseline thay cho value model - Một prompt sinh ra nhóm nhiều đáp án, mỗi đáp án được chấm một reward. Trung bình reward của cả nhóm đóng vai trò baseline, và advantage của mỗi đáp án là độ lệch chuẩn hoá so với trung bình đó. Nhờ vậy không cần value model như PPO._

Hình 4 — GRPO (slide 23).

### Slide 24–25 RLVR — reward thay bằng kiểm tra programmatic

> Trích slide 
>  "RLVR — Reinforcement Learning from Verifiable Rewards. Reward = kiểm tra programmatic 
>  (math match, unit test, regex). Không có "judge" để hack. 
>  Khi nào RLVR work: ■ Math: ground truth trong dataset ■ Code: chạy unit tests 
>  ■ Format: regex / JSON schema ■ Tool use: success/error from tool 
>  RLVR không thay preference learning cho subjective tasks. Bổ sung, không thay thế. 
>  DeepSeek-R1-Zero (Jan 2025): train base model (không SFT cold-start), 
>  reward = accuracy + format (rule-based), emergent "Aha!" self-reflection. 
>  GRPO không miễn phí: cần generation rollouts (G ≈ 8–64 samples per prompt) ⇒ 3-4× thời gian 
>  so với DPO. Chỉ dùng khi reasoning task thực sự cần. "

**Bảng ánh xạ task → method ở slide 25 là bảng đáng thuộc**, vì nó cho quy tắc 
 một câu để phân biệt hai thế giới:

| Loại task | Method | Ai làm "judge"? |
| --- | --- | --- |
| Helpfulness, style, tone | DPO / SimPO | Con người |
| Safety, harmlessness | DPO + CAI | Con người + hiến pháp |
| Math word problems | GRPO + RLVR | So khớp đáp án |
| Code generation | GRPO + RLVR | Unit test |
| Long-form reasoning | SFT cold-start + GRPO | Hỗn hợp |
| Tool calling correctness | GRPO + RLVR | Kết quả tool |
| Multi-turn dialogue | DPO | Con người |

Có ground truth kiểm được bằng code? → RLVR. Chỉ có phán đoán của con người? → DPO.

có thể bị hack

"Bổ sung, không thay thế."

SFT → DPO → RLVR

3–4× thời gian

mỗi

đổi bộ nhớ lấy thời gian

"Chỉ dùng khi reasoning task thực sự cần"

#### Ô kiểm tra — Chương 4 & 5

**1.** Bạn có SFT checkpoint và 5.000 cặp preference. Đồng nghiệp đề xuất dùng 
 SimPO vì "bài báo báo cáo +6.4 so với DPO". Phản hồi thế nào? Đánh giá

#### Đáp án

Ba điểm, theo đúng slide:

**① Slide 19 chốt DPO là baseline** cho 2025-2026, và đổi method chỉ khi có *lý do cụ thể*: VRAM, không có SFT, hoặc reasoning. "Bài báo báo +6.4" không nằm trong ba lý do đó.

**② Con số +6.4 là kết quả trong setup của chính bài báo SimPO**, trên 
 AlpacaEval 2 với model của họ. Nó không chuyển giao tự động sang dữ liệu của bạn.

**③ Slide 20 ghi rõ điều kiện dùng SimPO:** "VRAM hạn chế, length bias là vấn đề lớn." 
 Nếu bạn *đang* gặp length hacking (độ dài tăng >30%), thì đó mới là lý do chính đáng — 
 và lúc đó SimPO thắng vì nó chuẩn hoá reward theo độ dài.

*Câu trả lời đúng:* "Chạy DPO trước, đo. Nếu thấy length hacking hoặc thiếu VRAM 
 thì chuyển SimPO — có lý do đo được, không phải theo con số của bài báo."

**2.** Đội bạn có 40.000 log thumbs-up/down từ người dùng thật, không có cặp so sánh nào. 
 Dùng method gì? Áp dụng

#### Đáp án

**KTO.** Quick rule của slide 19: *"Chỉ +1/−1 ⇒ KTO."*

KTO không cần preference pairs — mỗi mẫu chỉ cần một nhãn good/bad. Loss dựa trên 
 prospect theory (Kahneman-Tversky), mô hình hoá loss aversion.

**Vì sao đây là lựa chọn thực dụng:** slide 20 nói thẳng — dữ liệu thumbs-up/down 
 từ production log *dễ thu thập hơn nhiều* so với ranked pairs. Bạn đã có 40.000 mẫu; 
 biến chúng thành cặp sẽ cần gán nhãn lại từ đầu.

*Phương án thay thế nếu vẫn muốn DPO:* ghép mẫu +1 và −1 *cùng prompt* thành cặp. 
 Nhưng thường không có đủ prompt trùng nhau, nên bạn sẽ mất phần lớn dữ liệu.

**3.** GRPO "tiết kiệm 50% memory" nhưng lại "chậm hơn DPO 3–4×". 
 Hai câu này có mâu thuẫn không? Phân tích

#### Đáp án

**Không** — chúng nói về hai tài nguyên khác nhau, và đó chính là bản chất của GRPO: *đổi bộ nhớ lấy thời gian*.

**Tiết kiệm bộ nhớ** đến từ việc bỏ value/critic model. PPO cần một model riêng 
 để đoán baseline; GRPO lấy baseline = trung bình reward của nhóm.

**Tốn thời gian** đến từ chính cái nhóm đó: phải sinh G ≈ 8–64 đáp án cho *mỗi* prompt. Đó là rollout — thứ mà DPO hoàn toàn không có (DPO là offline supervised).

*Hệ quả khi ra quyết định:* nghẽn VRAM → GRPO là món hời. Nghẽn GPU-giờ hoặc deadline → 
 món đắt. Slide chốt "chỉ dùng khi reasoning task thực sự cần", và không đưa GRPO vào Lab 22.

---

<!-- chiron-source-span: {"source_span_id":"d659c525-5b89-5b20-8c3c-77f4890fa955","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Preference Data & Implementation","source_file":"track-3-day-22.html"},"checksum":"8ba5af40afa28bd45260ecb1efa4f9031c08ee25b2eef6c51eede113152388c1"} -->

## 06 Preference Data & Implementation

Slide 26–32: chuẩn bị dữ liệu, chạy DPO bằng TRL, vì sao one-shot không đủ, 
 và một khoảng trống rất cụ thể của tiếng Việt.

### Slide 26–27 Preference dataset — prompt + chosen + rejected

> Trích slide 
>  "Prompt: 'Giải thích AI…' · Chosen: Rõ ràng, concise · Rejected: Verbose, generic 
>  Khác biệt phải genuine — KHÔNG chỉ là length 
>  Nguồn dữ liệu: ■ Human annotation: pairwise comparison UI → JSONL export 
>  ■ Synthetic: GPT-4 judge score, rank, tạo pairs ■ Tools: Argilla, Label Studio, Prodigy 
>  Quy mô tham khảo: 60K pairs cho good alignment. Open-source: UltraFeedback (64k), 
>  Anthropic HH (160k), OpenHermes (1M). "

"Khác biệt phải genuine — KHÔNG chỉ là length."

viết ngắn hơn

từ phía dữ liệu

slide 16

2.000 cặp

200 cặp

chất lượng cao, đúng domain

### Slide 28 TRL DPOTrainer — implementation

> Trích slide 
>  model = AutoModelForCausalLM.from_pretrained("path/to/sft-model") 
>  ref_model = AutoModelForCausalLM.from_pretrained("path/to/sft-model") # frozen 
>  config = DPOConfig(beta=0.1, learning_rate=5e-7, max_length=1024, max_prompt_length=512) 
>  trainer = DPOTrainer(model=model, ref_model=ref_model, args=config, train_dataset=pref_data) 
>  Monitoring healthy training: ■ Chosen rewards: phải tăng qua epochs 
>  ■ Rejected rewards: phải giảm ■ Gap giữa 2 loại nên widen dần 
>  Tokenization: verify max_prompt_length + max_length fit context window. Truncation giảm quality.

Hai chi tiết trong đoạn code này đáng dừng lại:

| Tham số | Giá trị slide | Vì sao đáng chú ý |
| --- | --- | --- |
| learning_rate | 5e-7 | Nhỏ hơn LR của SFT (Ngày 21: 2e-4) khoảng 400 lần. DPO tinh chỉnh hành vi trên một model đã tốt — LR lớn sẽ phá kiến thức SFT ngay |
| ref_model | bản copy thứ hai của SFT model | Đây là bản copy đóng băng. Nó là lý do DPO cần gấp đôi bộ nhớ so với SimPO/ORPO — và có mẹo bỏ được, xem mô-đun dưới |
| beta | 0.1 | Mặc định chuẩn. Xem mô-đun β để biết con số này ràng buộc model chặt tới mức nào |
| max_length / max_prompt_length | 1024 / 512 | Tổng phải vừa context window. Truncation cắt mất phần cuối câu trả lời — chính là phần thường phân biệt chosen với rejected |

không cần giữ bản copy thứ hai của model

chính model đang train khi tắt adapter đi

ref_model=None

#### Tương tác Bộ nhớ theo method — vì sao RLHF chỉ dành cho frontier lab

Điều quyết định VRAM không phải thuật toán, mà là **số bản model phải nằm 
 đồng thời trong bộ nhớ**. Bảng này đếm chúng.

Model **7B**, train bằng LoRA. Đoán trước hai con số:

1. DPO cần bao nhiêu VRAM, và RLHF-PPO gấp mấy lần?
2. Bật công tắc "LoRA: tắt adapter làm ref" — DPO tiết kiệm được bao nhiêu?

#### Kéo xong rồi mở

**① DPO ≈ 33 GB · RLHF-PPO ≈ 64 GB — gấp gần 2 lần.** Không phải vì thuật toán nặng hơn, mà vì PPO phải giữ *bốn* bản model cùng lúc: 
 policy (đang train) · ref (đóng băng, tính KL) · reward model (đóng băng, chấm điểm) · 
 value/critic (đang train, ước lượng baseline).

**② Bật mẹo LoRA: DPO tụt xuống ≈ 18 GB** — tiết kiệm 
 khoảng 15 GB, tức **gần một nửa**. Đó là ranh giới giữa "cần A100 40GB" 
 và "chạy được trên RTX 3090 24GB".

**Vì sao mẹo này hoạt động:** π_ref chỉ là model gốc chưa có adapter. 
 Với LoRA, model gốc *vẫn nằm nguyên trong bộ nhớ* — adapter chỉ là phần cộng thêm. 
 Tắt adapter đi là có ngay π_ref, không cần copy.

**Bài học mang đi:** khi đọc bảng method ở [slide 19](#s19), 
 cột *"Ref?"* không phải chi tiết học thuật — nó là **cột quyết định VRAM**. 
 SimPO và ORPO ghi "Không" ở cột đó, và đó chính là lý do slide 21 nói ORPO giảm 50% VRAM.

*Thử thêm:* đổi sang model 70B. RLHF vượt xa mọi GPU đơn lẻ; ngay cả DPO cũng cần 
 nhiều GPU. Đây là lý do vật chất khiến câu *"chỉ frontier labs có đủ resources"* ở 
 slide 9 là mô tả thực tế chứ không phải cách nói.

RLHF (PPO)

DPO

KTO

GRPO

SimPO

ORPO

Kích thước model

7B (Qwen2.5-7B · 7,62 tỷ)

8B (Llama-3.1-8B · 8,03 tỷ)

13B

70B

Mẹo LoRA — tắt adapter làm ref

Không dùng (giữ bản copy ref riêng)

Có dùng (ref = model gốc, tắt adapter)

Tổng VRAM

—

—

Số bản model thường trú

—

—

GPU nhỏ nhất vừa

—

—

So với DPO

—

cùng model, cùng cấu hình

Trọng số model (các bản thường trú) Gradient + optimizer của adapter Activations + CUDA overhead

#### Xem dạng bảng



#### Giả định của mô hình — đọc trước khi trích số

- Trọng số: bf16, 2 byte/tham số, nhân số bản thường trú.
- Số bản thường trú tại giai đoạn train chính: RLHF-PPO 4 (policy, ref, RM, value) · 
 DPO / KTO / GRPO 2 (policy, ref) · SimPO / ORPO 1 (chỉ policy). 
 Slide 10 đếm "3 models" theo 3 giai đoạn (SFT, RM, PPO); 
 con số 4 ở đây là số bản nằm trong VRAM tại thời điểm chạy PPO — hai cách đếm khác nhau, 
 cùng mô tả một pipeline.
- Adapter LoRA: r=16 gắn toàn bộ layer ≈ 0,53% tham số model 
 (con số đo được từ Qwen2.5-7B ở tài liệu Ngày 21). Gradient 2 byte + AdamW 12 byte = 14 byte/tham số train.
- Activations + CUDA overhead: gộp thành 2 GB cố định. Thực tế phụ thuộc 
 batch và seq_len — xem mô-đun VRAM ở tài liệu Ngày 21 để tính phần này cho đúng.
- Bỏ qua: chi phí rollout buffer của GRPO (đáng kể), KV cache khi sinh mẫu, 
 và khả năng RM/value model nhỏ hơn policy. Con số thật cho RLHF/GRPO sẽ cao hơn, không thấp hơn.

### Slide 29–30 Iterative DPO, và reward model chưa hề biến mất

> Trích slide 
>  " Llama 3 recipe (Meta 2024): Train RM → sinh 10–30 generations/prompt → RM chọn best → 
>  SFT trên best → DPO trên (best vs worst) → lặp 6 vòng với data mới mỗi vòng. 
>  Tulu 3 (AI2, Nov 2024): SFT → DPO → RLVR. RLVR thêm +1.7 MATH / +3.3 GSM8K / +1.3 IFEval 
>  trên DPO checkpoint. 
>  Lesson: one-shot offline DPO underperforms. Mọi 2024-2025 stack đều iterative. 
>  Trong DPO world, RM dùng làm gì? ■ Data filter: loại pairs gap quá nhỏ 
>  ■ Rejection sampling: chọn best-of-N ■ Best-of-N decoding tại inference ■ LLM-as-judge backbone 
>  Đừng nhầm: "Không cần RM cho DPO loss" không có nghĩa "Không cần RM ở đâu cả". 
>  RM vẫn ở khắp pipeline — chỉ không trực tiếp trong gradient update. "

Chương 3 dạy "DPO bỏ được reward model". Slide 30 nói thêm: **bỏ khỏi gradient update, 
 không phải bỏ khỏi pipeline.**

Trong recipe Llama 3, RM vẫn được train — nhưng dùng để *lọc và chọn dữ liệu* (rejection sampling, best-of-N), chứ không phải để tính reward trong loss. 
 Nó chuyển từ vai trò **huấn luyện viên** sang vai trò **người tuyển chọn**.

Nếu quiz hỏi "DPO có cần reward model không?" thì câu trả lời đầy đủ là: *không cần cho loss, nhưng stack production hiện đại vẫn dùng RM ở nhiều chỗ khác.*

một vòng

iterative

"kết quả một vòng; bước tiếp theo là iterative — sinh generation mới từ checkpoint vừa train, 
 dùng judge chọn best/worst, train vòng hai."

### Slide 31–32 LLM tiếng Việt — ai đã làm DPO, ai chưa

> Trích slide 
>  "VinaLLaMA-7B-Chat · SFT ✓ · DPO ✕ — PhoGPT-7B5-Instruct · ✓ · ✕ — PhoGPT-4B-Chat · ✓ · ✕ — 
>  Vistral-7B-Chat · ✓ · ✕ — SeaLLM-v2/v2.5/v3 · ✓ · ✓ — Sailor/Sailor2 · ✓ · ✓ 
>  Pattern: VN-first (VinaLLaMA, PhoGPT, Vistral) dừng ở SFT. 
>  SEA-regional (SeaLLM, Sailor) chạy tới DPO. ⇒ Gap cho VN-first DPO-aligned model. 
>  Lab 22 có thể là DPO-aligned VN model open-source đầu tiên end-to-end của khoá — publishable. 
>  Bước xây preference data tiếng Việt: 1. 200 prompts từ VN SFT set / VMLU stems 
>  2. Generate 2 responses: Lab21-SFT + stronger model 3. Judge: GPT-4o / Claude Sonnet (VN-aware prompt) 
>  4. Train DPO trên 200 pairs (~20 phút A100) 
>  Chưa có native large-scale preference dataset — lab artifact đáng publish. "

Đây là slide có giá trị *ngoài kỳ thi* lớn nhất của cả bài — nó chỉ ra một khoảng trống 
 cụ thể và một con đường bốn bước để lấp.

Model VN-first dừng ở SFT không phải vì kỹ thuật khó, mà vì **preference data 
 tiếng Việt gần như không có**. SFT data (instruction pairs) thì dịch được; 
 preference data cần *phán đoán* về cái nào tốt hơn *trong ngữ cảnh tiếng Việt*.

Sailor dùng UltraFeedback-vi — bản dịch máy bằng NLLB-3.3B. Slide gọi là *"đủ cho DPO nhưng không native"*. Dịch máy giữ được nội dung nhưng không giữ được 
 những thứ mà preference đo: sắc thái, độ tự nhiên, cách xưng hô.

**Bốn bước ở slide 32 là con đường rẻ nhất để tạo dữ liệu native:** không dịch, 
 mà sinh trực tiếp bằng tiếng Việt rồi để LLM judge chấm. 200 cặp, ~20 phút train. 
 Quy mô nhỏ nhưng *native* — và đó là thứ chưa ai công bố.

---

<!-- chiron-source-span: {"source_span_id":"8d1213d7-ba3a-5a8e-b285-360b0173a010","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Constitutional AI & Red-teaming","source_file":"track-3-day-22.html"},"checksum":"91605adc05368fd7d90a85737583e426869d445e6829d79f3b95509469e852aa"} -->

## 07 Constitutional AI & Red-teaming

Slide 33–36: tạo preference data không cần người, và kiểm tra an toàn trước deploy.

### Slide 33–35 CAI, RLAIF, Self-Rewarding — ai làm judge?

> Trích slide 
>  " Constitutional AI (Anthropic): 1. Generate model outputs → 2. Critique vs constitution 
>  → 3. Revise (self-improve) → 4. Preference Pairs (original vs revised). 
>  Constitution: ~16 principles ban đầu — Helpfulness, Harmlessness, Honesty. 
>  RLAIF (Lee et al. 2023): thay human annotators bằng LLM-as-judge. 
>  Empirically: AI feedback ≈ human feedback ở scale, 10× cheaper. 
>  Self-Rewarding LM (Yuan et al., Meta 2024): model là judge của chính mình. 
>  Sau 3 vòng, Llama-2-70B beats Claude 2 / Gemini Pro / GPT-4-0613 trên AlpacaEval 2. 
>  Collective CAI (Anthropic 2024): mời public input vào constitution, Polis-style consensus. 
>  Pattern chung: Ai sẽ làm judge? Human (RLHF) → AI (RLAIF) → Self (Self-Reward) → 
>  Community (Coll. CAI). Rẻ hơn, scale hơn — nhưng risk bias tăng theo. "

**Câu "Pattern chung" ở cuối slide 35 là câu tổng kết hay nhất của cả bài.** Nó biến bốn kỹ thuật rời rạc thành một trục duy nhất:

| Judge là ai | Method | Chi phí | Rủi ro đi kèm |
| --- | --- | --- | --- |
| Con người | RLHF / DPO | Cao nhất — thuê annotator | Chậm, khó scale, người cũng không nhất quán |
| AI khác | RLAIF | ~10× rẻ hơn | Kế thừa bias của model judge |
| Chính model đó | Self-Rewarding | Rẻ nhất | Vòng lặp tự khen — model tự xác nhận thiên kiến của mình |
| Cộng đồng | Collective CAI | Cao (tổ chức lấy ý kiến) | Chậm; nhưng tính chính danh cao nhất |
| Code / test | RLVR (slide 24) | Rất rẻ sau khi viết test | Chỉ dùng được khi có ground truth |

quy tắc viết rõ ra

khi không tin được judge, 
 hãy viết luật ra giấy và chấm theo luật.

### Slide 36 Red-teaming — kiểm tra an toàn trước deploy

> Trích slide 
>  "■ Probe model cho harmful outputs ■ Findings feed back vào preference dataset 
>  ■ Domain-specific: medical misinformation, legal liability 
>  Automated Tools: Garak (vulnerability scanner) · PyRIT (Microsoft, adversarial testing) 
>  ⇒ Scalable, repeatable 
>  Vòng lặp: Red-team Attack → Model Under Test → Analyze Failures → Update Pref. Data → (lặp lại)"

"Findings feed back vào preference dataset"

cặp preference mới

một vòng lặp

---

<!-- chiron-source-span: {"source_span_id":"55a37451-7f26-5ca8-a3e7-2e189b14cab6","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Đánh giá Alignment — Benchmarks","source_file":"track-3-day-22.html"},"checksum":"a71d92351d2de392508db49209f60479786c1d66dbabe6b900ab26052716e665"} -->

## 08 Đánh giá Alignment — Benchmarks

Slide 37–42: ba họ benchmark, vấn đề đệ quy của judge, và bối cảnh tiếng Việt. 
 Chương này nhiều tên riêng — nắm *ba họ* là đủ, đừng học thuộc từng cái.

### Slide 37–38 Vì sao đánh giá alignment khó

> Trích slide 
>  "Aligned response là open-ended — không có 1 ground-truth duy nhất: 
>  'Giúp tôi viết email xin nghỉ phép' → vô số câu trả lời đều đúng. Khác hẳn classification 
>  (1 nhãn đúng) hay translation (BLEU vs reference). 
>  Proxy vs Target: Cái ta đo (helpfulness 1-5) là proxy — không phải target thật. 
>  Target thật: user retention, task completion, brand trust, không gây hại. 
>  Mọi metric chỉ là 1 lát cắt ⇒ cần nhiều metrics + human feedback. 
>  3 nhóm benchmark: Static suites (MMLU/GSM8K — đo capability) · Judge-based (MT-Bench/AlpacaEval — 
>  đo response quality) · Reward Model suites (RewardBench — đo chính các judges). Không 1 cái nào đủ một mình. "

| Họ benchmark | Đo gì | Đại diện | Điểm mù |
| --- | --- | --- | --- |
| Static suites | Capability — model còn biết gì sau alignment | MMLU, GSM8K, MATH, IFEval, HumanEval, BBH, TruthfulQA | Không đo được chất lượng trả lời open-ended |
| Judge-based | Response quality — câu trả lời có hay không | MT-Bench, AlpacaEval 2 LC, Arena-Hard, Chatbot Arena | Judge có bias (đặc biệt là length bias) |
| Reward Model suites | Chính các judge — RM có đáng tin không | RewardBench v2, RM-Bench | Lại cần một chuẩn để đánh giá chính nó — vòng đệ quy |

không phải

lát cắt

gãy

nhiều metric + human feedback

### Slide 39–41 Static, judge-based và vấn đề đệ quy

> Trích slide 
>  Static: MMLU (kiến thức nền, 57 subjects) · GSM8K (math grade-school) · 
>  MATH (olympic) · IFEval (theo lệnh format) · HumanEval (chạy unit test) · BBH · TruthfulQA. 
>  Tất cả đều programmatic scoring. 
>  Judge-based: MT-Bench (80 multi-turn, GPT-4 judge, tiny set, position bias ) · 
>  AlpacaEval 2 LC (805 prompts, length-controlled — Dubois 2024 sửa length bias ) · 
>  Arena-Hard (500 hard prompts) · Chatbot Arena (ELO, người dùng thật — ground-truth nhất nhưng đắt + chậm). 
>  Length bias (judge thiên vị câu dài) là failure mode lớn nhất pre-2024. AlpacaEval 2 LC fixes nó; 
>  MT-Bench thì chưa. 
>  Cross-judge tip: chạy cùng 1 prompt qua 2 judge khác nhau; disagreement = signal cần xem tay. 
>  Vấn đề đệ quy: judge cần judge, RM cần benchmark — không có "ground truth" tuyệt đối ngoài 
>  con người + thời gian + production data.

**① "Alignment tax" là lý do static benchmark tồn tại trong bài này.** Cột cuối bảng slide 39 hỏi những câu như *"Có quên kiến thức sau alignment?"*, *"Chat-tuning có giảm reasoning?"*. MMLU thường *phẳng hoặc giảm nhẹ* sau chat-alignment — 
 bạn chạy static suite để phát hiện mình vừa đánh đổi mất cái gì.

**② AlpacaEval 2 *LC* — chữ LC là length-controlled.** Nếu bạn nghi ngờ length hacking ( [slide 16](#s16) ), đây là công cụ kiểm chứng đúng. 
 MT-Bench không kiểm soát độ dài, nên điểm MT-Bench tăng sau DPO có thể chỉ là câu dài hơn.

### Slide 42 Bối cảnh benchmark tiếng Việt

> Trích slide 
>  "VMLU — 10K MCQ, 58 VN subjects — Active 2024+ · ViGLUE — NLU 5 tasks — 2023 stable · 
>  ViMMLU — MMLU dịch sang Việt — NLLB-MT quality concerns · VLSP shared tasks — annual · 
>  VN AlpacaEval — Win-rate VN — GAP — Chưa tồn tại! 
>  Native VN judge-based benchmark chưa tồn tại. Sailor2 dùng UltraFeedback-vi (translated). 
>  Cơ hội: build 1 native VN AlpacaEval-style set 200–500 prompts ⇒ publishable đầu tiên. "

chưa có VN-first DPO-aligned model.

chưa có native VN judge-based benchmark.

hai mặt của cùng một vấn đề

200–500 prompt tiếng Việt do người Việt viết

---

<!-- chiron-source-span: {"source_span_id":"2d2e20a2-939d-51b6-ab1e-3db3a8a7e977","locator":{"kind":"html_section","section_id":"c9","order":11,"heading":"09 Demo & Lab 22","source_file":"track-3-day-22.html"},"checksum":"af2cc4b4e4308fefdd53c4d9a6c446376d7199c8c05da72be9afca10cf7825f3"} -->

## 09 Demo & Lab 22

Slide 43–49: DPO thực tế trên checkpoint của Lab 21, và hai bonus track.

### Slide 43–46 Demo: DPO training + LLM-as-Judge

> Trích slide 
>  "1. Lấy SFT checkpoint từ Lab 21, apply DPO với 2k UltraFeedback pairs, 1 epoch 
>  2. Before DPO: over-hedges, generic, verbose. After DPO: direct, concise, actionable 
>  3. GPT-4 judge: helpfulness từ 3.2 → 4.1 out of 5 
>  4. Chosen rewards tăng, rejected rewards giảm — healthy training signals 
>  −40% response length · 1 epoch (~30 phút A100) 
>  DPO dạy model phân biệt trực tiếp giữa good vs bad — model học preference signal rất nhanh, 
>  chỉ cần 1–2 epochs. 
>  Tulu 3 thực tế: +1.7 MATH · +3.3 GSM8K · +1.3 IFEval sau RLVR (so với DPO). 
>  Mỗi stage thêm vài points, không phải đột phá — nhưng cộng dồn."

slide 16

tăng

giảm

"over-hedges, verbose"

chiều của thay đổi cho biết bạn đang gặp 
 cải thiện hay hacking

ba failure mode ở slide 16

over-training

biện pháp phòng ngừa

### Slide 47–49 Lab 22 và hai bonus track

> Trích slide 
>  " Mục tiêu: DPO alignment trên SFT checkpoint + deploy aligned model. 
>  Deliverable: merge adapter, quantize, serve với vLLM. Report: SFT-only vs SFT+DPO. 2 giờ. 
>  1. Prepare preference dataset (human-ranked hoặc synthetic via GPT-4 judge), format prompt/chosen/rejected 
>  2. Train DPO adapter trên SFT checkpoint từ Lab 21 dùng TRL DPOTrainer. Monitor chosen/rejected rewards 
>  3. Compare SFT-only vs SFT+DPO trên safety và helpfulness. Dùng GPT-4 judge 
>  4. Deploy: merge adapter, quantize GGUF, serve vLLM. Measure latency overhead 
>  Bonus A: DPO vs ORPO head-to-head — cùng base, cùng data, so judge win-rate + time + VRAM 
>  Bonus B: Vietnamese preference data — 200 prompts, 2 responses, GPT-4o judge, train DPO 
>  GRPO+RLVR không có trong lab (compute-heavy, ≥3× DPO). "

| Bonus | Làm gì | Kết quả thu được | Đáng làm khi |
| --- | --- | --- | --- |
| A — DPO vs ORPO | Train hai adapter trên cùng base + cùng data, so win-rate, thời gian, VRAM | Hiểu đánh đổi "đơn giản vs mature" bằng số của mình | Bạn muốn củng cố phần slide 19 và có sẵn compute |
| B — Preference data tiếng Việt | 200 prompt VN → 2 response → judge → DPO | Dataset + adapter publishable — lấp khoảng trống ở slide 31 và 42 | Bạn muốn một artifact có giá trị ngoài lớp học |

chưa tồn tại

trước/sau

rewards/chosen

rewards/rejected

rewards/margins

%

one-shot, chưa iterative

---

<!-- chiron-source-span: {"source_span_id":"0ba179cb-7956-5573-8a43-3dbeb3c58bda","locator":{"kind":"html_section","section_id":"c10","order":12,"heading":"10 Bức tranh toàn cảnh — Full training flow","source_file":"track-3-day-22.html"},"checksum":"f3a85966ca8d6c81edeaf5975eb7968ecc3cc8d8ed2b9b704950f0c7999e7328"} -->

## 10 Bức tranh toàn cảnh — Full training flow

Slide 50–60: alignment nằm ở đâu trong vòng đời LLM. Chương khảo sát — 
 đọc để biết cái gì tồn tại, không cần học sâu từng mục.

### Slide 50–51 Pre-training → Mid-training → Post-training

> Trích slide 
>  " Pre-training: trillions of tokens, next-token prediction · Cost rất cao (M USD) · Frontier labs only 
>  Mid-training: continued pretraining, domain adapt, long-context extension · Cost cao · Domain teams 
>  Post-training: SFT → DPO → RLVR; merge, distill, optimize · Cost vừa phải · Most ML teams live here 
>  99% công việc của ML team trong industry rơi vào post-training. Pre-training là sân chơi của 5-10 lab toàn cầu. 
>  Khi nào cần pre-training? Hầu như không bao giờ cho startup/enterprise. Default: bắt đầu từ 
>  Llama / Qwen / Mistral base + post-train. "

đều nằm trong post-training

"hầu như không bao giờ cần pre-training"

### Slide 52–60 Khảo sát: từ domain adaptation tới deployment

> Trích slide (rút gọn) 
>  52 · Domain adaptation: DAPT (raw domain text 10B+ tokens) → TAPT (task corpus) → 
>  SFT/LoRA → DPO. Catastrophic forgetting là rủi ro lớn nhất của DAPT/TAPT. Replay 50/50. 
>  53 · Synthetic data — 4 thế hệ: Self-Instruct → Evol-Instruct → Persona-driven → 
>  Verified synthesis (kiểm tra programmatic trước khi đưa vào dataset). 
>  54 · Distillation lineage: Alpaca (copy outputs) → Vicuna/WizardLM (copy at scale) → 
>  Orca (copy reasoning ) → Phi-3/Phi-4 (synthesize curriculum, vượt teacher ). 
>  Legal: ToS của OpenAI/Anthropic/Google cấm dùng output để train competing model. 
>  55 · Hardware: FlashAttention (2–4×, O(N) memory) + gradient checkpointing (30–50% memory, 30% chậm). 
>  Thứ tự khi OOM: mixed precision → grad ckpt → FlashAttn → 4-bit → grad accumulation → ZeRO/FSDP. 
>  56 · Distributed: ZeRO-1 (optimizer) → ZeRO-2 (+gradients, default 4–8 GPU) → 
>  ZeRO-3/FSDP (+parameters, khi model > 1 GPU). 
>  57 · PEFT variants: DoRA (rank thấp) · rsLoRA (rank cao) · PiSSA (hội tụ nhanh). 
>  2025: với LR tuning đúng, mọi variant peak tương đương vanilla LoRA. Tune LR trước, đừng over-engineer. 
>  58 · Model merging: SLERP · Task Arithmetic · TIES · DARE · DARE-TIES. Tool: mergekit. 
>  Không merge khác architecture. 
>  59 · Quantization & serving: NF4 · GPTQ · AWQ · GGUF; vLLM, speculative decoding, KV cache quant. 
>  Đừng dùng tất cả cùng lúc. Thêm từng cái, đo, giữ cái work.

**Chín slide, chín chủ đề độc lập.** Cách đọc hiệu quả nhất là gom chúng theo *câu hỏi mà chúng trả lời*:

| Câu hỏi | Slide | Câu trả lời một dòng |
| --- | --- | --- |
| Domain của tôi quá xa base model? | 52 | DAPT → TAPT → SFT → DPO. Nhớ replay 50/50 chống quên |
| Không đủ dữ liệu? | 53–54 | Synthetic data (4 thế hệ) hoặc distillation — kiểm ToS trước |
| Hết VRAM? | 55 | Theo đúng thứ tự 6 bước, đừng nhảy cóc |
| Model không vừa 1 GPU? | 56 | ZeRO-2 cho 4–8 GPU; ZeRO-3/FSDP khi model lớn hơn 1 GPU |
| Dùng LoRA variant nào? | 57 | Tune LR trước. Variant chỉ đáng đổi khi rank rất thấp hoặc rất cao |
| Có nhiều model fine-tune, gộp được không? | 58 | mergekit — nhưng phải cùng base architecture |
| Deploy thế nào? | 59 | Quantize (NF4/AWQ/GGUF) + vLLM. Thêm từng tối ưu, đo từng cái |

**① Slide 57:** *"Với LR tuning đúng, mọi PEFT variant peak tương đương vanilla LoRA. 
 Tune LR trước, đừng over-engineer."* — DoRA/rsLoRA/PiSSA nghe hấp dẫn, nhưng phần lớn 
 cải thiện mà người ta gán cho chúng thực ra đến từ việc chỉnh learning rate.

**② Slide 59:** *"Đừng dùng tất cả cùng lúc. Thêm từng cái, đo, giữ cái work."* — 
 áp dụng cho mọi danh sách tối ưu trong chương này.

**③ Slide 54:** ToS của OpenAI/Anthropic/Google **cấm** dùng output 
 để train model cạnh tranh. Đây là ràng buộc *pháp lý*, không hiện trong loss curve — 
 nhưng nó chặn được cả sản phẩm ở khâu cuối. Alternative có license cho phép: 
 Llama-3 70B, Qwen-2.5-72B, Mixtral-8x22B.

1. Có preference pairs? → có SFT: **DPO/SimPO** · không SFT: **ORPO** · 
 chỉ +1/−1: **KTO**

2. Có instruction data? → **SFT** (LoRA/QLoRA), rồi thu preference → DPO

3. Chỉ có raw domain text? → xa base: **DAPT → TAPT → SFT → DPO** · 
 gần base: skip DAPT

4. Math/code/ground truth? → sau DPO thêm **GRPO + RLVR**

5. Nhiều model task-specific cần gộp? → **model merging**

6. Cần deploy hiệu quả? → **quantize + vLLM + speculative decoding**

**Và câu chốt của slide:** *"Reality: hầu hết enterprise teams 
 chạy SFT + DPO là đủ. Phần còn lại là nice to have."* — nếu quiz hỏi một câu tổng kết chương 10, 
 đây là câu đó.

---

<!-- chiron-source-span: {"source_span_id":"78cddbe5-b6d7-5e8d-ab4f-e632b2c04f73","locator":{"kind":"html_section","section_id":"c11","order":13,"heading":"11 Tổng kết","source_file":"track-3-day-22.html"},"checksum":"db00d45bb3ca5ad3f7326fea392232525cd354aa2d6c6c35182e5c1654c2e1b7"} -->

## 11 Tổng kết

Slide 61–64.

### Slide 61 Key Takeaways

> Trích slide 
>  "1 DPO vẫn là go-to 2025-2026 — nhưng phải iterative (Llama 3 / Tulu 3), không one-shot 
>  2 Watch failure modes: likelihood displacement, length hacking. rewards/chosen đảo chiều = stop 
>  3 ORPO khi base→aligned 1 stage; SimPO khi length bias là vấn đề; KTO khi chỉ có +1/−1 
>  4 RL trở lại với GRPO + RLVR cho reasoning — không reward model. Stack: SFT → DPO → RLVR 
>  5 VN-first models dừng ở SFT — Lab 22 Bonus B là cơ hội publish DPO-aligned VN model"

Năm takeaway đọc như một chuỗi quyết định, không phải năm ý rời:

```text
① Chọn method       →  DPO là mặc định. Đổi chỉ khi có lý do đo được.
        ↓
② Nhưng phải lặp    →  one-shot underperforms. Llama 3 lặp 6 vòng.
        ↓
③ Và phải canh chừng →  rewards/chosen đảo chiều = DỪNG. Loss không phải chỉ số sức khoẻ.
        ↓
④ Nếu có ground truth →  thêm RLVR sau DPO. Bổ sung, không thay thế.
        ↓
⑤ Nếu làm tiếng Việt →  khoảng trống còn nguyên. Đây là cơ hội, không phải bài tập.
```

"rewards/chosen đảo chiều = stop"

chọn gì

khi nào dừng lại

### Slide 62–64 Tiếp theo & Hỏi đáp

> Trích slide 
>  " Ngày 23: LangGraph & Agentic Orchestration — 'Model đã aligned. 
>  Tiếp theo: orchestrate complex workflows với LangGraph stateful machines.' 
>  ■ Hoàn thành Lab 22 ■ Đọc: LangGraph documentation — State, Nodes, Edges 
>  Hỏi & Đáp: DPO hay ORPO — bạn sẽ chọn method nào cho project của mình và tại sao? "

"DPO hay ORPO?"

điều kiện

"Tôi chọn DPO vì đã có SFT checkpoint từ Lab 21 và có preference pairs — đúng quick rule 
 của slide 19, và DPO là baseline mature nhất. Tôi sẽ chuyển sang ORPO nếu phải đi thẳng 
 từ base model không qua SFT, hoặc nếu VRAM không đủ giữ hai bản model — vì ORPO bỏ được 
 cả ref model lẫn giai đoạn SFT. Điều làm tôi đổi ý là một con số cụ thể: nếu đo thấy VRAM 
 không đủ, hoặc nếu DPO cho thấy length hacking thì tôi cân nhắc SimPO trước ORPO."

chọn gì · vì sao theo điều kiện hiện tại · điều gì làm bạn đổi ý

---

<!-- chiron-source-span: {"source_span_id":"76fb4c62-4826-50ab-943a-06b08381a676","locator":{"kind":"html_section","section_id":"ladder","order":14,"heading":"▤ Luyện kỹ năng cốt lõi: chọn method và đọc tín hiệu training","source_file":"track-3-day-22.html"},"checksum":"5e03a630bdec09fa1cf3f7aedadc5f16a7e48325b303d05fd955ee100e8c24c6"} -->

## ▤ Luyện kỹ năng cốt lõi: chọn method và đọc tín hiệu training

Ba bài giảm dần giàn giáo. Làm đúng thứ tự.

① Vấn đề là kiến thức, format, hay hành vi?

② Dữ liệu phản hồi của tôi ở dạng nào?

③ Ràng buộc lớn nhất?

④ Tôi sẽ nhìn chỉ số nào để biết nó hỏng?

#### Chatbot hỗ trợ nội bộ trả lời đúng nhưng dài dòng và hay từ chối quá mức

Đọc cách *lập luận*, không chỉ đáp án.

1. Vấn đề là hành vi, không phải kiến thức hay format. Model trả lời đúng sự thật 
 và đúng cấu trúc; nó chỉ chọn sai cách nói — rào đón thừa và từ chối những câu vô hại. 
 Đây đúng hai trong ba triệu chứng SFT-only ở slide 6. 
 Cách phân biệt: nếu bạn tự viết lại câu trả lời được mà không cần tra cứu gì thêm, 
 vấn đề không phải kiến thức.
2. Dữ liệu: có thể tạo cặp. Cùng một prompt, chosen = câu trả lời trực tiếp và 
 hữu ích, rejected = câu trả lời hiện tại của model. Nguồn rẻ nhất: lấy chính output của model 
 làm rejected, để người sửa lại thành chosen — đúng ý tưởng Constitutional AI ở 
 slide 34 (original vs revised).
3. Ràng buộc: không có gì đặc biệt. Có SFT checkpoint, có cặp 
 ⇒ DPO, theo quick rule slide 19. Không cần SimPO/ORPO vì không gặp 
 length bias hay thiếu VRAM.
4. Chỉ số theo dõi: ① ba đường rewards/chosen ↑, 
 rewards/rejected ↓, margins nở rộng; ② độ dài trung bình — 
 kỳ vọng giảm (như demo slide 45 giảm 40%), nếu tăng >30% thì là length hacking; 
 ③ tỷ lệ từ chối trên một tập câu hỏi vô hại — đây là metric riêng cho triệu chứng của bạn, 
 không có sẵn trong TRL.

Câu chốt kiểu vấn đáp "Đây là vấn đề hành vi nên SFT thêm không giải được — model không có tín hiệu nào nói 
 'từ chối chỗ này là quá'. Em dùng DPO vì đã có SFT checkpoint và tạo được cặp từ chính output 
 của model rồi cho người sửa. Em theo dõi ba đường rewards, độ dài trung bình, và một metric riêng 
 là tỷ lệ từ chối trên tập câu hỏi vô hại. Nếu rewards/chosen đảo chiều thì em dừng ngay."

#### Sau DPO, judge chấm cao hơn nhưng người dùng thật phàn nàn model "nói nhiều hơn trước"

Hai bước đầu cho sẵn. Hai bước sau tự viết rồi mới mở.

1. Vấn đề là hành vi, và có mâu thuẫn giữa hai nguồn đánh giá: 
 judge nói tốt hơn, người dùng nói tệ hơn. Khi hai nguồn mâu thuẫn, một trong hai đang đo sai thứ.
2. Dữ liệu: đã có cặp và đã train DPO xong. Vấn đề không nằm ở việc chọn method 
 mà ở việc chẩn đoán cái vừa xảy ra.
3. ③ Nghi ngờ đầu tiên là gì, và kiểm chứng bằng cách nào? 
 (gợi ý: có hai nguồn cùng thiên vị một hướng — một ở phía loss, một ở phía judge)
4. ④ Nếu xác nhận đúng nghi ngờ, sửa bằng gì? 
 (gợi ý: hai hướng — sửa dữ liệu, hoặc đổi method)

#### Đáp án hai bước còn lại

**③ Nghi ngờ: length hacking, cộng hưởng với length bias của judge.**

Hai cơ chế độc lập cùng đẩy về một hướng: 
 • *Phía loss* ( [slide 16](#s16) ): Δ là tổng log-prob trên cả câu, câu dài có nhiều 
 mass hơn ⇒ dễ đẩy Δ lên bằng cách viết dài. 
 • *Phía judge* ( [slide 40](#s40) ): length bias là "failure mode lớn nhất pre-2024" — 
 judge thiên vị câu dài.

Nên judge và loss *đồng thuận với nhau* mà cả hai cùng sai — còn người dùng thì đúng.

**Kiểm chứng — ba bước, rẻ dần:** 
 ① Đo% thay đổi độ dài trung bình. Ngưỡng cảnh báo của slide 16 là **>30%**. 
 ② Chấm lại bằng **AlpacaEval 2 LC** — bản length-controlled sinh ra chính để sửa lỗi này. 
 Nếu điểm sụp khi kiểm soát độ dài ⇒ xác nhận. 
 ③ Cross-judge (mẹo slide 40): chạy cùng prompt qua hai judge khác nhau; bất đồng = tín hiệu cần xem tay.

**④ Sửa — hai hướng, nên làm cả hai:**

*Sửa dữ liệu:* vẽ phân bố độ dài của chosen vs rejected trong dataset 
 ( [slide 27](#s27): "khác biệt phải genuine — KHÔNG chỉ là length"). 
 Nếu chosen luôn dài hơn rejected, dataset đang mã hoá độ dài chứ không phải chất lượng — 
 phải cân bằng lại.

*Đổi method:* **SimPO** dùng average log-prob (length-normalized) thay vì tổng, 
 cắt đúng cơ chế này. **IPO** cũng được slide 15 giới thiệu là "variant fix length bias, 
 drop-in replacement cho DPO".

*Đối chiếu bài 1:* cùng khung 4 câu, nhưng ở đây câu ④ (chỉ số theo dõi) mới là câu 
 giải được bài — vì vấn đề không phải chọn method mà là **đọc tín hiệu cho đúng**.

#### SmartCheck AI — có nên alignment gì không?

Không có bước nào làm sẵn. Đây là dự án của bạn.

lịch sự nhưng vòng vo

cả ba

Viết ra rồi mới mở. Nếu bạn kết luận được và bảo vệ được kết luận đó, bạn đã đạt mức 
 "Đánh giá" của bài học này.

#### Đáp án tham khảo — so với bài của bạn, không thay thế nó

**Cả ba quan sát đều là vấn đề HÀNH VI** — không phải kiến thức, không phải format. 
 Đúng loại mà alignment giải. Cụ thể chúng khớp gần như một-một với ba triệu chứng SFT-only 
 ở [slide 6](#s6): vòng vo = *over-hedges/verbose*, dài dòng khi bàn giao = *generic, không actionable*, từ chối câu vô hại = *refusal quá mức*.

**Nhưng kết luận vẫn là: chưa alignment.** Ba lý do, xếp theo sức nặng:

**① Không có dữ liệu preference, và ở 300 lượt/ngày thì thu rất chậm.** Slide 27 nói 60K cặp cho alignment tốt; ngay cả quy mô lab (2.000 cặp) cũng cần vài tháng 
 log nếu chỉ lấy ca có vấn đề.

**② Có giải pháp rẻ hơn nhiều cho cả ba.** Cả ba đều là vấn đề *văn phong 
 trong một số ít loại câu* — mà kiosk chỉ có khoảng năm loại tình huống. 
 Few-shot với 2–3 ví dụ mẫu cho mỗi loại (câu hỏi lại, câu bàn giao) giải quyết được phần lớn, 
 với chi phí bằng không và sửa được trong 10 phút.

**③ Quan sát ⑶ có thể không phải vấn đề alignment.** "Từ chối vì không có trong 
 tài liệu" có thể là *hành vi đúng* của một hệ grounded — hoặc là RAG không tìm được tài liệu 
 vốn có. Phải phân biệt trước: nếu tài liệu *có* mà không tìm ra thì đó là lỗi retrieval, 
 alignment không cứu được.

**Nhưng đây là phần đáng làm ngay — và nó đến từ slide 20:**

KTO chỉ cần **+1 / −1**, và slide 20 nói thẳng dữ liệu thumbs-up/down từ 
 production log *dễ thu thập hơn nhiều* so với ranked pairs. Kiosk của bạn **đã sinh ra tín hiệu đó rồi** mà chưa ai lưu:

• Phiên kết thúc bằng check-in thành công, khách không cần lễ tân → **+1** 
 • Phiên phải escalate, hoặc khách bỏ đi giữa chừng → **−1**

**Việc cần làm bây giờ không phải train, mà là *ghi lại*:** thêm một trường `outcome_label` vào audit log của mỗi phiên. Chi phí gần bằng không. 
 Sáu tháng sau bạn có một dataset KTO-ready từ dữ liệu thật của chính mình — 
 thứ mà không mua được và không dịch được.

**Bẫy trong đề:** nếu bạn kết luận "dùng DPO để sửa văn phong" thì đúng về *loại* vấn đề nhưng sai về *thứ tự*. Alignment là bậc cao; few-shot là bậc thấp 
 và chưa thử. Đây vẫn là khuôn mẫu "start simplest" của cả khoá — chỉ đổi tên trục.

---

<!-- chiron-source-span: {"source_span_id":"2c603d24-903b-5fa8-bbf2-70e4b4a943fc","locator":{"kind":"html_section","section_id":"misc","order":15,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"track-3-day-22.html"},"checksum":"be1f415fe09e5afad534ee20c5a9ceffc08aa42aab8a382af6277bf7ccbb3f1e"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Mỗi thẻ: niềm tin phổ biến, lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng.

*Vì sao nghe hợp lý:* model sau alignment trả lời tốt hơn hẳn, nên cảm giác như nó 
 "biết nhiều hơn". Và cụm "train thêm" gợi ý đúng như vậy.

Slide 6 nói thẳng: alignment là *"dạy model phân biệt câu trả lời tốt vs xấu bằng preference data — **không phải dạy thêm kiến thức mới** "*.

Ba trục tách bạch: kiến thức từ **pre-training**, format từ **SFT**, 
 hành vi từ **alignment**. Không trục nào thay được trục nào. Đây chính là bài học 
 "fine-tune không sửa knowledge gap" của Ngày 21, nói lại ở một tầng cao hơn.

[Hình 1](#s5) — ba giai đoạn với hai loại dữ liệu khác nhau · [Slide 6](#s6) nguyên văn.

*Vì sao nghe hợp lý:* đúng với gần như mọi bài supervised learning khác. 
 Đường loss đi xuống mượt mà là hình ảnh của thành công trong mọi tutorial.

DPO loss chỉ tối ưu **hiệu** Δ giữa chosen và rejected. Có hai cách làm Δ tăng: 
 đẩy chosen lên, hoặc *dìm rejected xuống* — và cách thứ hai có thể kéo chosen xuống theo. 
 Đó là **likelihood displacement**: loss đẹp, model tệ hơn.

Chỉ số sức khoẻ thật là ba đường `rewards/chosen` (phải tăng), `rewards/rejected` (phải giảm), `rewards/margins` (phải nở rộng).

[Slide 16](#s16) — "rewards/chosen giảm ⇒ likelihood displacement" · [Takeaway 2 slide 61](#s61): "rewards/chosen đảo chiều = stop".

*Vì sao nghe hợp lý:* β là một số nhỏ, chỉnh nó thì model học "mạnh" hay "nhẹ" hơn — 
 nghe y hệt learning rate. Và slide đúng là có `learning_rate` riêng bên cạnh.

β là **bán kính cho phép đi khỏi ref model**. Vì reward ngầm là `r = β·log(π/π_ref)`, nên để đạt cùng một mức reward, β cao ⇒ cần lệch khỏi ref *ít hơn*.

Cụ thể: β = 0,2 cần Δ ≈ 11 để đạt độ chắc chắn 90%; β = 0,05 cần Δ ≈ 44 — **gấp bốn lần**. Đó là lý do β thấp làm model "quên" kiến thức: nó bị đẩy đi xa hơn.

[Mô-đun β](#m-beta) — kéo và xem Δ cần thiết thay đổi theo nghịch đảo của β.

*Vì sao nghe hợp lý:* đó đúng là điểm bán hàng chính của DPO, và [Hình 2](#s12) vẽ hẳn một ô đỏ bị xoá đi.

Slide 30 nói rõ: *"'Không cần RM cho DPO loss' không có nghĩa 'Không cần RM ở đâu cả'. 
 RM vẫn ở khắp pipeline — chỉ không trực tiếp trong gradient update."*

Trong recipe Llama 3, RM vẫn được train và dùng để: lọc cặp có gap quá nhỏ · rejection sampling 
 chọn best-of-N · best-of-N decoding lúc inference · làm backbone cho LLM-as-judge. 
 Nó chuyển từ **huấn luyện viên** sang **người tuyển chọn**.

[Slide 30](#s29) — bốn vai trò của RM trong DPO world.

*Vì sao nghe hợp lý:* judge là GPT-4, và GPT-4 giỏi. Điểm tăng thì phải là tiến bộ.

Judge cũng là một model, nên nó có bias. Slide 40 gọi **length bias** là 
 "failure mode lớn nhất pre-2024" — judge thiên vị câu dài. Mà DPO cũng thiên vị câu dài 
 (slide 16). Hai bias cùng hướng ⇒ điểm tăng mà chất lượng không tăng.

Ngoài ra slide 38 phân biệt **proxy vs target**: helpfulness 1–5 chỉ là lát cắt, 
 không phải thứ bạn thật sự muốn (user retention, task completion).

[Slide 40](#s40) — AlpacaEval 2 **LC** (length-controlled) sinh ra 
 chính để sửa lỗi này · mẹo cross-judge: chạy qua hai judge, bất đồng = tín hiệu.

*Vì sao nghe hợp lý:* [Hình 3](#s18) vẽ một dòng thời gian tiến hoá rõ ràng, 
 mỗi mốc bỏ đi một thứ. Trực giác nói mốc sau tốt hơn mốc trước.

Slide 19 chốt: *"DPO vẫn là baseline tốt nhất 2025-2026. Chuyển method khác chỉ khi có 
 lý do cụ thể (VRAM, no SFT, reasoning)."*

Mỗi method sau DPO **bỏ đi một thứ để đổi lấy một ràng buộc được nới** — 
 không phải để tốt hơn toàn diện. SimPO nới VRAM và length bias. ORPO nới yêu cầu về giai đoạn SFT. 
 KTO nới yêu cầu về dạng dữ liệu. Nếu bạn không bị ràng buộc nào trong số đó, bạn không được lợi gì 
 mà mất đi độ chín của tooling.

[Mô-đun chọn method](#m-pick): để mọi ràng buộc ở "không có gì đặc biệt" — 
 kết quả luôn là DPO · Cùng khuôn mẫu với "đừng thêm agent" (Ngày 20) và 
 "đừng fine-tune" (Ngày 21).

---

<!-- chiron-source-span: {"source_span_id":"3196e2fd-c041-5274-97bd-b55cdeac7688","locator":{"kind":"html_section","section_id":"apply","order":16,"heading":"→ Áp dụng vào SmartCheck AI","source_file":"track-3-day-22.html"},"checksum":"c97262cbaaf53fd4fb6277820bb628359872697dcfb5ecac55ffda176520d0ef"} -->

## → Áp dụng vào SmartCheck AI

Kết luận: **chưa alignment** — nhưng có *một việc nên làm ngay hôm nay* với chi phí gần bằng không.

### Ba quan sát, một chẩn đoán

| Quan sát từ lễ tân | Loại vấn đề | Triệu chứng slide 6 tương ứng | Giải pháp rẻ nhất |
| --- | --- | --- | --- |
| Câu hỏi lại vòng vo, khách đọc hai lần | Hành vi | Over-hedges, verbose | Few-shot 2–3 mẫu câu hỏi lại trong prompt |
| Escalate dài dòng thay vì bàn giao gọn | Hành vi | Generic, không actionable | Template cứng cho câu bàn giao |
| Từ chối câu vô hại về toà nhà | Cần phân biệt trước | Refusal quá mức — hoặc không phải | Kiểm retrieval trước: tài liệu có mà không tìm ra thì đó là lỗi RAG |

hành vi đúng

có

retrieved_documents

### Vì sao chưa alignment — và việc nên làm thay vào đó

| Điều kiện của slide | SmartCheck AI | Kết luận |
| --- | --- | --- |
| Vấn đề là hành vi, không phải kiến thức/format | ✓ Đúng với quan sát ⑴ và ⑵ | Đúng loại bài toán |
| Đã thử bậc thấp hơn (few-shot) chưa? | ✕ Chưa | Chặn ở đây — kiosk chỉ có ~5 loại tình huống, few-shot phủ được |
| Có preference data? | ✕ Không có | 300 lượt/ngày, thu 2.000 cặp mất nhiều tháng |

Slide 20 nói KTO chỉ cần **+1 / −1**, và dữ liệu thumbs-up/down từ production log *dễ thu thập hơn nhiều* so với ranked pairs.

**Kiosk của bạn đã sinh ra tín hiệu đó rồi — chỉ chưa ai lưu:**

• Phiên kết thúc bằng check-in thành công, không cần lễ tân → **+1** 
 • Phiên phải escalate, hoặc khách bỏ dở giữa chừng → **−1**

```text
class CheckInState(TypedDict):
    ...
    outcome_label: int | None      # +1 | -1 | None — gán ở node finalize
```

Chi phí: một trường trong state, vài dòng ở node cuối. Sáu tháng sau bạn có một dataset **KTO-ready từ dữ liệu thật của chính mình** — thứ không mua được và không dịch được. 
 Nếu lúc đó vẫn chưa cần alignment thì cũng không mất gì; nếu cần thì bạn đã đi trước sáu tháng.

> Câu trả lời phỏng vấn dựng sẵn 
>  "Ba vấn đề em quan sát được đều là vấn đề hành vi — đúng loại mà alignment giải, và khớp 
>  ba triệu chứng SFT-only trong tài liệu. Nhưng em chưa alignment vì hai lý do: em chưa thử bậc thấp hơn 
>  là few-shot, mà kiosk chỉ có khoảng năm loại tình huống nên few-shot phủ được phần lớn; 
>  và em không có preference data — ở 300 lượt/ngày thì thu đủ cặp mất nhiều tháng. 
>  
>  Thứ em làm ngay là ghi nhãn kết quả từng phiên: check-in thành công là +1, phải escalate hoặc 
>  khách bỏ dở là −1. Đó chính là dạng dữ liệu mà KTO cần, và kiosk vốn đã sinh ra nó — 
>  chỉ là chưa ai lưu. Sau vài tháng em sẽ có preference data native từ chính hệ của mình, 
>  thay vì phải dịch UltraFeedback."

---

<!-- chiron-source-span: {"source_span_id":"cbfa070e-4867-5c68-afff-9e6d9bd92694","locator":{"kind":"html_section","section_id":"numbers","order":17,"heading":"! Con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"track-3-day-22.html"},"checksum":"76412c51c1e6346932419198179160b087717fbb49468f3bf8da8b1fee3a78fd"} -->

## ! Con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài này nhiều con số từ bài báo. Phần lớn có nguồn rõ, nhưng đều là kết quả *trong setup của tác giả* — không phải cam kết cho dữ liệu của bạn.

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| InstructGPT 1.3B RLHF > GPT-3 175B | 6 | Có nguồn (Ouyang 2022) | Đúng trên human preference cho instruction-following. Không đúng nếu đo kiến thức (MMLU) |
| SimPO +6.4 AlpacaEval 2, +7.5 Arena-Hard | 20 | Từ bài báo SimPO, so với DPO trong setup của họ | Không chuyển giao tự động. Slide 19 vẫn chốt DPO là baseline |
| ORPO "50% VRAM reduction" | 21 | So với pipeline SFT-rồi-DPO | Tự tính ở mô-đun bộ nhớ — với 7B ra ~46%, cùng bậc độ lớn |
| GRPO "50% memory savings" | 23 | Từ việc bỏ value model | Đúng về bộ nhớ, nhưng tốn 3–4× thời gian (slide 25). Hai tài nguyên khác nhau |
| RLAIF "10× cheaper" | 35 | Có nguồn (Lee 2023), nhưng phụ thuộc giá annotator và giá API tại thời điểm đo | Dùng để cảm nhận bậc độ lớn; tự tính lại theo giá hiện tại |
| Demo: helpfulness 3.2 → 4.1, length −40% | 44–45 | Kết quả demo của giảng viên, 2k pairs, 1 epoch | Là mốc tham khảo cho lab. Kết quả của bạn sẽ khác — ghi số thật |
| Tulu 3: +1.7 MATH / +3.3 GSM8K / +1.3 IFEval | 46 | Có nguồn (AI2, publish cả recipe + data + code) | Trích được. Chú ý đây là mức tăng của RLVR trên checkpoint đã DPO, không phải của DPO |
| "60K pairs cho good alignment" | 27 | Quy mô tham khảo, không phải ngưỡng | Lab dùng 2.000, Bonus B dùng 200 — vẫn cho hiệu ứng đo được |
| Ngưỡng chẩn đoán: length tăng >30% | 16 | Quy tắc kinh nghiệm, không có nguồn trên slide | Dùng làm cờ cảnh báo, rồi kiểm chứng bằng AlpacaEval 2 LC |
| Số bản model thường trú trong mô-đun bộ nhớ | — | Ước lượng của tài liệu này, không có trên slide | Slide 10 đếm "3 models" theo 3 giai đoạn; mô-đun đếm bản thường trú lúc chạy PPO. Đọc kỹ mục giả định |

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark 
 thực tế đã chạy."

helpfulness score của bạn

---

<!-- chiron-source-span: {"source_span_id":"20726853-efb1-550e-8d8e-75e6d22644c3","locator":{"kind":"html_section","section_id":"cheat","order":18,"heading":"✓ Cheat sheet ôn thi","source_file":"track-3-day-22.html"},"checksum":"f279bb9b2c2f85549a9f103f9953dc47c22e3576bdd8bac00c83407bdf88064e"} -->

## ✓ Cheat sheet ôn thi

Nén 64 slide xuống một trang.

### Bảng method — cột "bỏ đi cái gì" là cách nhớ nhanh nhất

| Method | RM? | Ref? | Stage | Bỏ đi | Dùng khi |
| --- | --- | --- | --- | --- | --- |
| RLHF (PPO) | Có | Có | 3 | — | Frontier lab, chất lượng tối đa |
| DPO | Không | Có | 2 | reward model | MẶC ĐỊNH |
| IPO | Không | Có | 2 | (sửa length bias) | DPO over-fit pref tất định |
| SimPO | Không | Không | 2 | ref model | VRAM · length bias |
| ORPO | Không | Không | 1 | ref + SFT stage | Đi thẳng từ base |
| KTO | Không | Có | 2 | yêu cầu dữ liệu cặp | Chỉ có +1/−1 |
| GRPO | Không | Có | 1 RL | value model | Reasoning có ground truth |

**Quick rules (slide 19):** Có SFT + cặp ⇒ DPO · Không SFT ⇒ ORPO · 
 Chỉ +1/−1 ⇒ KTO · Math/code ⇒ GRPO + RLVR.

### Ba thứ phải nhớ chính xác

| Chủ đề | Nội dung |
| --- | --- |
| Suy dẫn DPO — 3 bước | ① Bradley-Terry: P(y_w≻y_l) = σ(r_w − r_l) → ② KL-RL có closed-form: π* ∝ π_ref·e^(r/β) → ③ đảo: r = β·log(π*/π_ref), thay vào ① ⇒ RM biến mất. Chỉ đúng cho objective KL-regularized |
| β | Không phải learning rate. Là bán kính cho phép rời ref. Δ cần ≈ 2,197/β để đạt 90%. β↑ ⇒ lệch ít hơn ⇒ giữ kiến thức tốt hơn nhưng align nông hơn. Mặc định 0,1 |
| 3 failure mode | Likelihood displacement ( rewards/chosen giảm) · Length hacking (dài >30%) · Mode collapse (mọi câu mở đầu giống nhau) |

Loss giảm không đảm bảo model tốt lên

rewards/*

β cao = model bị giữ GẦN ref hơn

DPO bỏ RM khỏi loss, không bỏ khỏi pipeline

### Checklist trước khi bấm train DPO

1. Vấn đề có thật sự là hành vi không? (kiến thức → RAG · format → SFT)
2. Đã thử few-shot chưa? Bậc thấp trước.
3. Dataset: chosen và rejected có khác nhau thật, hay chỉ khác độ dài? Vẽ phân bố độ dài.
4. Đã lọc bỏ cặp có gap quá nhỏ chưa? (chống likelihood displacement)
5. beta = 0.1, learning_rate = 5e-7 (nhỏ hơn SFT ~400 lần)
6. max_prompt_length + max_length có vừa context window không?
7. Dùng LoRA? → ref_model=None, tiết kiệm gần nửa VRAM
8. Chỉ train 1–2 epoch. Nhiều hơn là mời gọi failure mode.
9. Đã bật log rewards/chosen, rewards/rejected, rewards/margins chưa?
10. Có tập eval riêng và biết sẽ đo bằng AlpacaEval 2 LC (length-controlled) không?

SFT dạy model NÓI GÌ. Alignment dạy model NÓI NHƯ THẾ NÀO.

hiệu

---

<!-- chiron-source-span: {"source_span_id":"bb203224-ee6e-5520-b14b-469908ad17df","locator":{"kind":"html_section","section_id":"gloss","order":19,"heading":"A–Z Từ điển thuật ngữ","source_file":"track-3-day-22.html"},"checksum":"5016ee345c9907e2ae1fc08d93ab83a0a41dd8112fbe1ce1d9f16c99a7d367d8"} -->

## A–Z Từ điển thuật ngữ

Bài này dày viết tắt nhất trong cả khoá. Mỗi mục: một câu dễ hiểu, rồi chỗ nó xuất hiện.

---

<!-- chiron-source-span: {"source_span_id":"f0d97943-09cc-5705-b644-89e1446fa7ee","locator":{"kind":"html_section","section_id":"bloom","order":20,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-22.html"},"checksum":"0145c3183b73ba36f43dfd72dd82b410954c48f8b4e7175f74578ef8f3c80326"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Quiz kiểm tra mức 2–3; câu hỏi cuối bài 
 (slide 63) kiểm tra mức 5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được 3 giai đoạn post-training, 3 failure mode của DPO, và quick rules chọn method. | Slide 5 · 16 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao preference data mạnh hơn demonstration data, 
 và vì sao β cao giữ model gần ref hơn. | Ô kiểm tra chương 1 và 3 · mô-đun β |
| 3 · Áp dụng | Cho một tình huống mới, chạy khung 4 câu hỏi và chọn được method kèm chỉ số sẽ theo dõi. | Bài 1 → 2 → 3 · mô-đun chọn method |
| 4 · Phân tích | Nhìn log training của người khác và chỉ ra failure mode nào đang xảy ra — trước khi họ deploy. | Slide 16 · Bài 2 phần điền khuyết |
| 5 · Đánh giá | Trả lời "DPO hay ORPO cho project của bạn?" bằng điều kiện — chọn gì, vì sao theo 
 ràng buộc hiện tại, và điều gì sẽ làm bạn đổi ý. | Slide 63 · Câu trả lời dựng sẵn |

không đi tìm cái tốt nhất

chứng minh được
