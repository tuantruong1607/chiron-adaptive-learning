---
schema_version: 1
course_id: rag-intensive
document_id: "33fe77e8-51fb-5f84-b937-6a2fda23ea50"
document_version_id: "d4537311-e6c4-500c-b06b-a2a895dea8c7"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Fine-tuning LLMs — phân tích & breakdown từng slide"
source_file: "track-3-day-21.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-21.html"
source_sha256: "990b2cbf94120a156aec6a4f61a885d3b9bdf4f3e5f156b2ff5d72bf41e7de72"
parser_version: chiron-structured-markdown-v1
html_section_count: 15
interactive_module_count: 4
interactive_control_count: 10
language: vi
---

# Fine-tuning LLMs — phân tích & breakdown từng slide

> Đọc lại toàn bộ 31 slide của buổi Ngày 21 (Nguyễn Khánh Linh, VinUni), giải thích cặn kẽ 
 từ LoRA đến QLoRA và FlashAttention, kèm 4 mô-đun tính toán tương tác và ví dụ neo theo dự án 
 SmartCheck AI — nơi kết luận đúng nhất của bài học này là đừng fine-tune.

<!-- chiron-source-span: {"source_span_id":"cd1a3bb9-4331-5444-9524-2069e3aea326","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"track-3-day-21.html"},"checksum":"e1f05b4ff5920d03f71872734cb9db3e481c5003f66538de5b72037a3369cb76"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Bài Ngày 21 khác Ngày 20 ở một điểm quan trọng: nó nặng **số**. VRAM, rank, tham số, 
 chi phí — và những con số này chỉ vào đầu khi bạn *tự tính*, không phải khi bạn đọc. 
 Bốn mô-đun trong trang đều là máy tính thật, dùng công thức thật.

Lượt 1 · ~15 phút

Trước khi vào lab

- Đọc slide 5, 6, 9, 28
- Chạy Ngân sách VRAM với GPU bạn có
- Mục tiêu: biết fine-tune không sửa được cái gì

Lượt 2 · ~60 phút

Để làm được, không chỉ hiểu

- Chương 1–4, làm hết phần "Dự đoán trước khi kéo"
- Làm 3 bài tập bậc thang theo thứ tự
- Dừng ở mỗi Ô kiểm tra cuối chương

Lượt 3 · ~30 phút

Trước quiz / phỏng vấn

- 6 hiểu lầm phổ biến — vùng quiz khai thác nhiều nhất
- Cheat sheet + Từ điển thuật ngữ
- Tự chấm bằng thang tự đánh giá

rất hấp dẫn

vấn đề của tôi có thật sự là vấn đề mà fine-tuning giải được không?

fine-tune KHÔNG sửa lỗ hổng kiến thức

---

<!-- chiron-source-span: {"source_span_id":"90ef28f0-3210-5d35-85d0-7a81afade23c","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"track-3-day-21.html"},"checksum":"fc58a3d0892806ac72a07958812a0a0b6e9cdd48e7c05ede48d34cc76136c10e"} -->

## 00 Mở đầu

Slide 1–3: vị trí bài học và câu hỏi dẫn dắt.

### Slide 1 Trang bìa — Fine-tuning LLMs

> Trích slide 
>  "Fine-tuning LLMs — Từ Full Fine-tune đến LoRA/QLoRA. AICB-P2T3 · Ngày 21 · Chương 5 — 
>  Fine-tuning & An Toàn. Nguyễn Khánh Linh. VinUniversity · Phase 2 · Track 3 · Tuần 5"

**Đọc vị trí trong chương trình.** Đây là bài *mở màn* Chương 5, ngay sau khi 
 Chương 4 khép lại bằng Multi-Agent. Bốn bài Chương 4 (Reflexion, Memory, RAG, GraphRAG, Multi-Agent) 
 đều làm model *mạnh hơn mà không đụng vào trọng số*. Ngày 21 là lần đầu tiên chương trình 
 cho phép bạn sửa chính trọng số của model.

sau cùng

câu trả lời sai

### Slide 2 Câu hỏi dẫn dắt

> Trích slide 
>  "HÃY SUY NGHĨ… — Khi nào nên fine-tune — và khi nào prompt engineering đủ rồi? 
>  Giữ câu hỏi này trong đầu khi học bài hôm nay"

Chú ý cấu trúc câu hỏi: nó **giống hệt** câu hỏi dẫn của Ngày 20 
 ("khi nào một agent không đủ?"). Đây là cùng một khuôn mẫu tư duy, chỉ đổi đối tượng — 
 và đó là thứ đáng học hơn cả nội dung kỹ thuật:

```text
Prompt  →  RAG / Tool  →  Agent  →  Fine-tune
   rẻ nhất                          đắt nhất, khó rollback nhất

Ở MỖI bậc, câu hỏi luôn giống nhau:
  "Bậc hiện tại đã đủ chưa — và tôi CHỨNG MINH bằng số nào?"
```

"nếu single agent đạt trên 80% thì đừng thêm agent"

"nếu few-shot prompt đạt 80%+ thì prompt đủ rồi"

phải đo baseline trước

### Slide 3 Nội dung bài học

> Trích slide 
>  "1. Khi nào cần Fine-tune? 2. LoRA — Cơ chế hoạt động 3. QLoRA — Fine-tune trên GPU nhỏ 
>  4. Dataset & Training Pipeline 5. Demo & Thực hành"

Cấu trúc đi theo trình tự **quyết định → cơ chế → tối ưu tài nguyên → dữ liệu & vận hành → thực hành**. 
 Chương 1 dạy bạn *khi nào không nên*; chương 2–3 là toán và bộ nhớ; chương 4 là nơi 
 phần lớn thất bại thật sự xảy ra (dataset); chương 5 bắt bạn đo.

dễ nhất

Chương 4 (dataset) mới là nơi project chết.

---

<!-- chiron-source-span: {"source_span_id":"796b039f-b240-59cc-a311-c9a19bd15378","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Khi nào cần Fine-tune?","source_file":"track-3-day-21.html"},"checksum":"da00c3a2e9a059c292e35358cc3e23aad055c5f5e8358a0e7a5cc1253a2c95ba"} -->

## 01 Khi nào cần Fine-tune?

Slide 4–7: cây quyết định, và ranh giới giữa API fine-tuning và self-host.

### Slide 4 Section divider

> Trích slide 
>  "01 — Khi nào cần Fine-tune? Prompt Engineering đã đủ chưa — hay cần huấn luyện thêm?"

### Slide 5 Bối cảnh 2025–2026 — Frontier models đủ tốt?

> Trích slide 
>  "Prompt Eng. (80%+ tasks giải quyết được) → không đủ? → RAG (thêm knowledge cập nhật liên tục) 
>  → vẫn thiếu? → Fine-tune (style, format, latency, cost) 
>  ■ Frontier models (GPT-4o, Claude 3.5, Gemini 2) đủ tốt cho hầu hết tasks 
>  ■ Fine-tune chỉ khi thực sự cần: format riêng, domain jargon, giảm cost at scale 
>  ■ Model options: Qwen2.5-7B hoặc Gemma-2-9B 
>  Lưu ý: Fine-tune KHÔNG fix knowledge gaps — dùng RAG cho knowledge. Fine-tune fix style và format. "

#### Câu quan trọng nhất của cả bài học

**"Fine-tune KHÔNG fix knowledge gaps."** Đây là câu bạn phải hiểu tới tận cơ chế, 
 không phải học thuộc. Lý do:

- Fine-tuning dạy phân phối, không dạy sự kiện. Khi bạn train trên 
 1.000 mẫu, model học "câu trả lời trong domain này trông như thế nào " — giọng văn, cấu trúc, 
 thuật ngữ, độ dài. Nó không tạo ra một chỗ để tra cứu.
- Sự kiện học qua fine-tuning thì mờ và không kiểm chứng được. Model có thể nhớ 
 "giờ làm việc là 8h–17h" sau khi thấy nó 50 lần, nhưng bạn không biết nó nhớ chính xác đến đâu, 
 không sửa được khi giờ thay đổi, và không có citation.
- Kiến thức thay đổi; trọng số thì không. Chính sách sửa hôm nay thì RAG cập nhật 
 trong 5 giây. Fine-tune thì phải train lại và deploy lại.

**Sai:** "Model không biết quy định công ty tôi, nên tôi sẽ fine-tune nó trên tài liệu nội bộ."

**Đúng:** "Model không *tra cứu được* quy định công ty tôi → RAG. 
 Model trả lời *đúng nhưng sai giọng / sai format / quá dài* → fine-tune."

Phép thử một câu: *nếu ngày mai dữ liệu thay đổi, bạn có phải train lại không?* Nếu có → đó là knowledge → dùng RAG.

#### Ba lý do chính đáng để fine-tune

| Lý do | Triệu chứng cụ thể | Vì sao prompt/RAG không giải được |
| --- | --- | --- |
| Format / style riêng | Cần output đúng một khuôn cứng, mọi lần, không lệch — SOAP note, biên bản, JSON nghiệp vụ có ràng buộc lạ | Prompt dài dòng vẫn trôi; few-shot ăn context window mỗi request |
| Domain jargon | Model dùng từ phổ thông thay vì thuật ngữ ngành; dịch sai từ chuyên môn | RAG đưa được tài liệu vào nhưng không đổi được cách nói của model |
| Giảm cost / latency at scale | Volume lớn, prompt few-shot dài, hoặc cần <200ms | Prompt càng dài càng đắt; API luôn có latency mạng |

cả ba

máy tính ROI

### Slide 6 Decision Tree — Prompt vs RAG vs Fine-tune

> Trích slide 
>  "Few-shot prompt đạt 80%+ accuracy? — Có → Prompt đủ rồi / Không → Cần knowledge mới, cập nhật? 
>  — Có → Dùng RAG / Không → Volume > 50k/day hoặc latency-critical? — Có → Fine-tune ROI positive / 
>  Không → API fine-tune (OpenAI/Anthropic) 
>  Prototype bằng prompting, đo gap. Nếu gap > 15% và volume > 50k req/day ⇒ fine-tuning có ROI dương. 
>  Luôn thử prompt → RAG trước khi tới fine-tune. "

_Sơ đồ: Cây quyết định Prompt, RAG hay Fine-tune - Ba câu hỏi rẽ nhánh nối tiếp nhau: few-shot đạt 80% chưa, có cần kiến thức cập nhật không, và volume có vượt 50 nghìn request mỗi ngày không — dẫn tới bốn kết luận: dùng prompt, dùng RAG, self-host fine-tune, hoặc API fine-tune._

Hình 1 — Cây quyết định (slide 6).

Dùng RAG

#### Ba cổng, đọc cho đúng

1. Cổng 1 — "few-shot đạt 80%+?" Chú ý chữ few-shot: bạn phải thử 
 prompt có ví dụ trước khi kết luận prompt không đủ. Rất nhiều người thử zero-shot, 
 thấy kém, rồi nhảy thẳng sang fine-tune.
2. Cổng 2 — "cần knowledge cập nhật?" Đây là cổng lọc mạnh nhất. Phép thử một câu 
 đã nêu ở slide 5: dữ liệu đổi thì có phải train lại không?
3. Cổng 3 — "volume > 50k/day hoặc latency-critical?" Cổng này quyết định 
 self-host hay API, không quyết định có fine-tune hay không. Đọc nhầm chỗ này là lỗi phổ biến.

phép hội

máy tính ROI

### Slide 7 API Fine-tuning vs Self-hosted LoRA/QLoRA

> Trích slide 
>  "Infra management: Không cần — managed / Tự setup GPU + pipeline · Control: Hạn chế (hyperparam) / 
>  Toàn quyền (rank, layers, data) · Cost per token: Cao ($$$) / Thấp khi volume lớn · 
>  Latency: Mạng + queue / Self-host vLLM, sub-200ms · Data privacy: Gửi qua API provider / On-prem hoàn toàn · 
>  Time to production: Vài giờ / Vài ngày 
>  API: Prototype nhanh, volume nhỏ–vừa, không có team ML ops, dữ liệu non-sensitive. 
>  Self-host: Volume >50k/day, dữ liệu nhạy cảm, cần custom rank/layers, cần multi-tenant adapters. "

Bảng này thực chất có **hai trục quyết định riêng biệt** bị trộn vào một bảng. 
 Tách ra thì dễ dùng hơn nhiều:

| Trục | Đẩy bạn về API khi… | Đẩy bạn về self-host khi… | Loại ràng buộc |
| --- | --- | --- | --- |
| Kinh tế | Volume nhỏ–vừa; chi phí cố định của GPU chưa được khấu hao | Volume lớn; chi phí/token thấp bù được tiền GPU | Có thể tính ra tiền — thương lượng được |
| Ràng buộc cứng | Dữ liệu không nhạy cảm; không cần chỉnh rank/layers | Dữ liệu không được rời khỏi hạ tầng; cần multi-tenant adapters | Không thương lượng được — thắng mọi tính toán kinh tế |

không được gửi ra ngoài

không được xét đến

context.md

"Không dùng dữ liệu cá nhân thật cho public demo"

"Seed data phải là synthetic data"

không

Nhưng nếu đây là hệ thật đặt trong toà nhà doanh nghiệp

#### Tương tác Máy tính ROI — bao giờ self-host mới rẻ hơn API?

Slide 6 đưa ra ngưỡng "50k request/ngày". Con số đó chỉ có nghĩa khi bạn nói rõ *đang thay thế API nào*. Đổi bậc model API và xem ngưỡng hoà vốn nhảy đi đâu.

Ngưỡng hoà vốn mặc định (thay thế model API **frontier** ) là bao nhiêu request/ngày? 
 Rồi bấm sang bậc **mini** và đoán tiếp: ngưỡng đó tăng lên bao nhiêu lần?

#### Bấm đổi bậc API rồi mở

**Thay thế frontier: hoà vốn ở khoảng 7.400 request/ngày** — 
 thấp hơn ngưỡng 50k của slide tới **gần 7 lần**.

**Thay thế mini: hoà vốn ở khoảng 124.000 request/ngày** — **cao gấp 2,5 lần** ngưỡng 50k.

**Vì sao:** chi phí self-host gần như *cố định* (tiền thuê GPU chạy 24/7), 
 còn chi phí API *tuyến tính theo volume*. Điểm cắt của một đường thẳng dốc với một đường nằm ngang 
 phụ thuộc hoàn toàn vào **độ dốc** — tức là giá mỗi request của API bạn đang thay. 
 Giá frontier đắt hơn mini khoảng 17 lần, nên ngưỡng hoà vốn cũng thấp hơn khoảng 17 lần.

**Bài học mang đi:** "50k/ngày" không phải hằng số. Câu hỏi đúng không phải *"volume của tôi có đủ lớn không?"* mà là **"model 7B fine-tune của tôi có thay được 
 đúng cái model API tôi đang trả tiền không?"** Nếu bạn đang dùng model mini và định thay bằng 
 7B self-host, bạn cần volume gấp 17 lần mới hoà vốn — và có khi chất lượng còn không bằng.

*Thử thêm:* kéo "Giá thuê GPU" từ $1 xuống $0,3/giờ (spot instance). Ngưỡng hoà vốn tụt 
 khoảng 3 lần. Tối ưu hạ tầng ăn thẳng vào ngưỡng ROI — nhưng nhớ rằng spot có thể bị thu hồi giữa chừng.

Thay model frontier ($2,50 / $10 per M)

Thay model mini ($0,15 / $0,60 per M)

- **Control - Volume 50.000 /ngày**: min `1000`, max `300000`, step `1000`, default `50000`

- **Control - Giá thuê GPU $1,00 /giờ**: min `20`, max `500`, step `10`, default `100`

- **Control - 1 GPU phục vụ 200.000 req/ngày**: min `50000`, max `600000`, step `10000`, default `200000`

- **Control - Chi phí train một lần $50**: min `0`, max `1000`, step `10`, default `50`

Chi phí API / tháng

—

tuyến tính theo volume

Self-host / tháng

—

—

Tiết kiệm / tháng

—

âm nghĩa là đang lỗ

Hoà vốn tại

—

req/ngày — dưới mức này thì dùng API

Chi phí API Chi phí self-host Volume hiện tại

#### Xem dạng bảng



#### Giả định của mô hình — thay bằng số của bạn trước khi dùng để ra quyết định

- Mỗi request: 500 token vào + 200 token ra. Prompt few-shot dài sẽ đẩy con số này lên nhiều.
- GPU chạy 24/7. Nếu tắt được ngoài giờ, chi phí self-host giảm tương ứng và ngưỡng hoà vốn tụt.
- Chi phí train một lần được khấu hao đều trong 12 tháng.
- Self-host là hàm bậc thang: vượt throughput một GPU thì phải thuê thêm GPU.
- Bỏ qua hoàn toàn: lương kỹ sư vận hành, thời gian debug, chi phí downtime, và 
 rủi ro chất lượng khi 7B không thay nổi frontier. Trong thực tế những khoản này thường 
 lớn hơn tiền GPU — mô hình này vì thế lạc quan có hệ thống về phía self-host.

#### Ô kiểm tra — Chương 1

Ba câu này là toàn bộ giá trị thực dụng của chương 1.

**1.** Sếp nói: "Model không biết quy trình nội bộ của công ty mình, fine-tune nó 
 trên bộ tài liệu quy trình đi." Bạn trả lời thế nào? Hiểu

#### Đáp án

Đây là **knowledge gap**, và slide 5 nói thẳng fine-tune không sửa được nó.

Cách trả lời không làm mất lòng ai: *"Vấn đề là model không tra cứu được quy trình, chứ không phải 
 nó nói sai giọng. Fine-tuning dạy model **cách nói**, RAG cho model **cái để đọc**. 
 Nếu tháng sau quy trình sửa, RAG cập nhật trong 5 giây còn fine-tune phải train lại."*

**Phép thử một câu** để đưa cho sếp: *dữ liệu này có thay đổi theo thời gian không?* Có → RAG. Không bao giờ đổi và vấn đề là văn phong/định dạng → mới đến fine-tune.

**2.** Gap so với yêu cầu là 25%, volume 3.000 request/ngày. Fine-tune hay không? Áp dụng

#### Đáp án

**Không** — theo đúng điều kiện của slide 6. Điều kiện là *gap > 15% **VÀ** volume > 50k/ngày*. Ở đây gap đạt nhưng volume thiếu tới 17 lần.

**Nhưng đừng dừng ở "không".** Gap 25% là một vấn đề thật cần giải. Thứ tự nên thử: 
 few-shot tốt hơn → RAG → nếu vẫn thiếu và bản chất là format/style thì **API fine-tune** (nhánh cuối cùng bên phải của cây quyết định) — vì nó không bắt bạn 
 gánh chi phí cố định của GPU. Cây quyết định không nói "đừng fine-tune"; nó nói "đừng *self-host* ".

**3.** Dữ liệu là hồ sơ bệnh án. Volume chỉ 2.000 request/ngày. API rẻ hơn self-host 
 rất nhiều. Chọn gì? Đánh giá

#### Đáp án

**Self-host** — và phép tính chi phí *không được đem ra bàn*.

Bảng slide 7 trộn hai loại ràng buộc rất khác nhau: ràng buộc *kinh tế* (thương lượng được) 
 và ràng buộc *cứng* (không thương lượng được). Data privacy thuộc loại thứ hai. 
 Khi dữ liệu không được rời khỏi hạ tầng, mọi con số ROI đều vô nghĩa vì phương án API **không nằm trong tập lựa chọn** ngay từ đầu.

*Kỹ năng thật sự được kiểm tra ở đây:* nhận ra khi nào một bài toán tối ưu thực chất là 
 một bài toán ràng buộc. Hỏi "cái gì bị cấm?" trước khi hỏi "cái gì rẻ nhất?".

---

<!-- chiron-source-span: {"source_span_id":"9fe6e618-e915-5020-8126-8ee863be981b","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 LoRA — Cơ chế hoạt động","source_file":"track-3-day-21.html"},"checksum":"688bff972c3306b1b15ca03a4ab257d69864be244048468da3e85e7c80ca22ce"} -->

## 02 LoRA — Cơ chế hoạt động

Slide 8–11: low-rank adaptation, kiến trúc, và đánh đổi theo rank.

### Slide 8 Section divider

> Trích slide 
>  "02 — LoRA — Cơ chế hoạt động. Low-Rank Adaptation: thêm ghi chú vào sách, không sửa sách gốc"

### Slide 9 Ý tưởng cốt lõi — LoRA (Hu et al. 2021)

> Trích slide 
>  "Freeze toàn bộ base weights (hàng tỷ tham số), chỉ inject thêm low-rank update 
>  ∆W = B · A — train phần rất nhỏ tham số. 
>  Analogy: LoRA giống thêm sticky notes vào sách giáo khoa — không sửa sách gốc, chỉ thêm ghi chú nhỏ. 
>  Khi deploy, "dán" ghi chú vào sách ⇒ zero added latency. 
>  Inference: merge adapter vào base weights: W = W₀ + B · A — không tốn thêm thời gian khi chạy."

#### Tại sao "low-rank" lại đủ — trực giác toán học

Câu hỏi tự nhiên: nếu chỉ train 0,5% tham số mà vẫn hiệu quả, tại sao người ta lại từng train 100%? 
 Câu trả lời nằm ở giả thuyết trung tâm của bài báo LoRA:

lượng thay đổi cần thiết

hạng nội tại thấp

Đây là giả thuyết, không phải định lý.

kém đúng

#### Phép so sánh "sticky note" — đúng đến đâu, gãy từ đâu

**Sách gốc không bị sửa.** Base weights đóng băng hoàn toàn — bạn luôn quay lại được. **Ghi chú thì nhỏ.** Adapter chỉ vài chục MB so với 15 GB của model. **Nhiều bộ ghi chú cho cùng một cuốn sách.** Đây là điều làm nên multi-tenant serving 
 ở slide 14: một base model + nhiều adapter cho nhiều domain.

**1 · Sticky note nằm *bên cạnh* chữ; LoRA thì *cộng vào* chữ.** Công thức là W = W₀ + B·A — một phép cộng vào chính trọng số, không phải một chú thích đọc thêm. 
 Đó là lý do sau khi merge thì không còn dấu vết gì của adapter và latency bằng đúng model gốc.

**2 · Ghi chú của người đọc thì có thể mâu thuẫn với sách; LoRA thì không "biết" mình đang sửa gì.** Nó không thêm sự kiện mới, nó nghiêng phân phối đầu ra. Đây lại là lý do fine-tune ≠ knowledge.

**3 · Dán nhiều tờ ghi chú chồng lên nhau không cộng dồn sạch sẽ.** Merge hai adapter vào cùng một base thường làm hỏng cả hai — muốn phục vụ nhiều domain thì phải *hoán đổi* adapter lúc chạy, không phải merge hết vào.

một

giống hệt

Cái giá:

merge

giữ tách

### Slide 10 Kiến trúc LoRA — Frozen Weights + Adapters

> Trích slide 
>  "x → W₀ (frozen, hàng tỷ tham số, không update khi training) và A (d×r) → B (r×k) → h, cộng lại. 
>  Toán học: h = W₀x + B·A·x (phần B·A là ∆W). Rank r ≪ min(d,k). Thường r ∈ {8, 16, 32, 64}. 
>  lora_alpha/r = 1 hoặc 2. Alpha cao ⇒ adapter ảnh hưởng mạnh hơn. 
>  Target layers (2025 best practice): ALL attention + MLP layers. q_proj + v_proj alone thiếu capacity. "

_Sơ đồ: Kiến trúc LoRA với trọng số đóng băng và adapter hạng thấp - Đầu vào x đi song song qua hai nhánh: nhánh trọng số gốc W0 đã đóng băng, và nhánh adapter gồm ma trận A rồi ma trận B; hai kết quả cộng lại thành đầu ra h. Chỉ A và B được huấn luyện._

Hình 2 — Kiến trúc LoRA (slide 10).

#### Ba siêu tham số, và cái nào thật sự quan trọng

| Tham số | Ý nghĩa | Giá trị nên dùng | Mức quan trọng |
| --- | --- | --- | --- |
| r (rank) | Bề rộng của "nút thắt" — quyết định adapter có bao nhiêu năng lực | Bắt đầu 16 | Vừa — xem slide 11 |
| lora_alpha | Hệ số nhân của ∆W. Thực tế ∆W được nhân với alpha/r | alpha = 2r (tỷ lệ 2) hoặc = r | Thấp — giữ tỷ lệ cố định khi đổi r |
| target_modules | Layer nào được gắn adapter | TẤT CẢ attention + MLP | Cao nhất |

"q_proj + v_proj alone thiếu capacity"

chuyển từ q+v sang toàn bộ layer làm số tham số 
 train tăng khoảng 8 lần

một

q_proj+v_proj

#### Tương tác Đếm tham số LoRA — rank hay target_modules quan trọng hơn?

Công thức thật: mỗi layer tuyến tính d×k được gắn adapter sẽ thêm `r × (d + k)` tham số. Cộng qua mọi layer là ra con số bạn thật sự train.

Qwen2.5-7B, rank 16, chỉ gắn `q_proj + v_proj` → khoảng 5 triệu tham số train. 
 Đoán trước hai cách "tăng năng lực":

1. Giữ q+v, tăng rank 16 → 64 (gấp 4). Được bao nhiêu tham số?
2. Giữ rank 16, đổi sang TẤT CẢ layer. Được bao nhiêu?

#### Bấm thử cả hai rồi mở

**① Tăng rank 16 → 64 (q+v): 5,0M → 20,2M** — gấp 4, đúng như trực giác.

**② Giữ rank 16, đổi sang TẤT CẢ layer: 5,0M → 40,4M** — 
 gấp **8 lần**, tức là gấp đôi phương án ①.

**Vì sao:** các layer MLP ( `gate_proj`, `up_proj`, `down_proj` ) 
 có chiều intermediate rất lớn — với Qwen2.5-7B là 18.944 so với hidden 3.584. 
 Ba layer MLP đó một mình đã chiếm **khoảng 75%** tổng tham số adapter khi bật full. 
 Bỏ qua chúng là bỏ qua ba phần tư năng lực.

**Bài học mang đi:** "tăng rank" là nút mà ai cũng biết vặn, nên nó được vặn trước. 
 Nhưng nút có đòn bẩy lớn hơn là `target_modules` — và nó *miễn phí về mặt VRAM cho 
 base model*, chỉ tốn thêm ở optimizer states vốn đã rất nhỏ. Đây đúng là điều slide 10 gọi là 
 "2025 best practice: ALL attention + MLP layers".

*Thử thêm:* đổi sang Llama-3.1-8B ở cùng rank 16 full. Adapter ra 41,9M — gần như bằng Qwen 7B ( 40,4M ) mặc dù model 
 lớn hơn 5% về tổng tham số. Lý do: Llama có intermediate nhỏ hơn (14.336 so với 18.944) nhưng nhiều 
 layer hơn (32 so với 28), và hai yếu tố gần như triệt tiêu nhau. Kích thước adapter phụ thuộc **hình dạng** của model — hidden, intermediate, số layer — chứ không phụ thuộc tổng số 
 tham số của nó.

Qwen2.5-7B

Llama-3.1-8B

q_proj + v_proj

Toàn bộ attention

TẤT CẢ (attention + MLP)

- **Control - Rank r 16**: min `2`, max `128`, step `2`, default `16`

- **Control - lora_alpha 32 (alpha/r = 2 )**: min `2`, max `256`, step `2`, default `32`

Tham số train

—

—

% của model

—

so với toàn bộ trọng số

File adapter

—

bf16, chưa nén

VRAM cho optimizer

—

AdamW fp32 — phần này mới là tiết kiệm thật

Nhóm đang chọn Nhóm khác

#### Xem dạng bảng (mọi rank)



#### Công thức & cấu hình tham chiếu

- Mỗi layer tuyến tính d×k gắn adapter thêm r·(d+k) tham số (ma trận A là d×r, B là r×k).
- Qwen2.5-7B: hidden 3.584 · intermediate 18.944 · 28 layer · kv_dim 512 (GQA) · tổng ≈ 7,62B.
- Llama-3.1-8B: hidden 4.096 · intermediate 14.336 · 32 layer · kv_dim 1.024 (GQA) · tổng ≈ 8,03B.
- Do GQA, k_proj và v_proj hẹp hơn q_proj / o_proj — đã tính đúng trong công thức.
- Hãy đối chiếu với config.json của model bạn dùng trước khi đem con số này đi đâu.
- VRAM optimizer = tham số train × 12 byte (AdamW: m 4 + v 4 + master fp32 4).

### Slide 11 Rank r vs Accuracy — Trade-off

> Trích slide 
>  "r=8 — 0.1% params — Nhẹ, tiết kiệm · r=16 — Standard — Cân bằng tốt · r=64 — Near full FT — Tốn VRAM hơn 
>  Bắt đầu r = 16. Nếu accuracy chưa đủ ⇒ tăng lên 32, 64. Nếu VRAM hạn chế ⇒ giảm xuống 8. 
>  Variants mới: DoRA, rsLoRA — cải thiện nhẹ, cùng nguyên lý. "

Slide đưa ra một quy trình rất hợp lý: **bắt đầu 16, chỉ đổi khi có lý do**. 
 Nhưng có ba điều đáng nói thêm mà slide không kịp nêu:

1. Con số "0,1% params" phụ thuộc hoàn toàn vào target_modules. 
 Với Qwen2.5-7B: r=8 chỉ gắn q+v cho ra 0,033%; r=8 gắn toàn bộ layer cho ra 0,27%. 
 Chênh nhau 8 lần — nên "0,1%" chỉ là con số minh hoạ, không phải hằng số. Kiểm chứng ở 
 máy tính tham số.
2. Tăng rank tốn VRAM ít hơn bạn tưởng. Từ r=16 lên r=64 với Qwen 7B full-target: 
 tham số train tăng từ 40M lên 161M, VRAM optimizer tăng từ ~0,5 GB lên ~1,9 GB. 
 Trên tổng ngân sách ~10 GB thì đó là chuyện nhỏ. Rank hiếm khi là thứ làm bạn OOM — 
 đó là lý do slide 18 xếp "giảm rank" ở cuối cùng trong quy trình chống OOM.
3. Rank cao hơn không tự động tốt hơn. Với dataset nhỏ (500–2k mẫu như slide 16 khuyến nghị), 
 rank lớn dễ overfit hơn: nhiều năng lực hơn để ghi nhớ dữ liệu train thay vì học quy luật. 
 Đây chính là lý do Lab 21 bắt so sánh r=8, 16, 64 — và vì sao kết quả có thể khiến bạn ngạc nhiên.

"r=64 không cải thiện so với r=16, thậm chí eval loss cao hơn"

tốt

"khi nào tăng rank không còn cải thiện perplexity?"

#### Ô kiểm tra — Chương 2

Chương này là phần "toán" của bài — nhưng câu hỏi thi lại thiên về trực giác.

**1.** Vì sao LoRA *không* làm inference chậm đi, trong khi các phương pháp 
 adapter cổ điển thì có? Hiểu

#### Đáp án

Vì ∆W = B·A được **cộng thẳng vào** trọng số gốc khi deploy: W = W₀ + B·A. 
 Sau khi merge, model chỉ còn *một* ma trận cùng kích thước ban đầu — không có phép nhân nào 
 được thêm vào đồ thị tính toán.

Adapter cổ điển thì chèn *module thật* nối tiếp giữa các layer, nên mỗi forward pass 
 phải chạy qua chúng → latency thật.

*Điều kiện:* "zero added latency" chỉ đúng **sau khi merge**. Nếu bạn giữ 
 adapter tách rời để hoán đổi nhiều domain (multi-LoRA serving), sẽ có một chút overhead — 
 đổi lại được khả năng phục vụ nhiều adapter trên một GPU.

**2.** Bạn bị OOM khi train. Slide 18 nói thứ tự xử lý là: giảm max_seq_length → 
 bật gradient checkpointing → cuối cùng mới giảm rank. Vì sao rank xếp cuối? Phân tích

#### Đáp án

Vì **rank gần như không ảnh hưởng tới VRAM**. Với Qwen 7B, đi từ r=64 xuống r=8 
 chỉ tiết kiệm khoảng 1,7 GB optimizer states — trong khi giảm `max_seq_length` từ 4096 xuống 2048 cắt activations đi *một nửa*, thường là nhiều GB.

Ba thành phần chiếm VRAM, xếp theo độ lớn với QLoRA: **base model** (cố định, không giảm được 
 trừ khi quantize sâu hơn) → **activations** (tỷ lệ với batch × seq_len, giảm được nhiều) → **optimizer states** (đã rất nhỏ nhờ LoRA).

*Và slide còn dặn thêm:* "đừng chỉ giảm batch size — ảnh hưởng convergence". 
 Vì batch hiệu dụng nhỏ làm gradient nhiễu hơn. Cách đúng là giữ `batch × grad_accum` không đổi.

**3.** Chỉ được chỉnh *một* thứ để tăng năng lực adapter: rank hay target_modules? Áp dụng

#### Đáp án

**target_modules**, rõ ràng. Chuyển từ `q_proj+v_proj` sang toàn bộ 
 attention + MLP làm tham số train tăng **~8 lần** ở cùng rank — nhiều hơn cả việc 
 nhân tư rank (4 lần).

Lý do nằm ở hình dạng model: ba layer MLP có chiều intermediate lớn hơn hidden nhiều lần 
 (Qwen 7B: 18.944 so với 3.584), nên chúng chiếm khoảng **ba phần tư** tổng tham số adapter 
 khi bật đầy đủ. Bỏ qua MLP là bỏ qua phần lớn năng lực.

Đó là toàn bộ nội dung của câu "2025 best practice: ALL attention + MLP layers" ở slide 10 — 
 và cũng là lý do cấu hình mặc định trong Lab 21 (chỉ q+v) đáng để bạn đặt câu hỏi.

---

<!-- chiron-source-span: {"source_span_id":"1926e103-0ec7-5167-9400-a9fe861f15ba","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 QLoRA — Fine-tune trên GPU nhỏ","source_file":"track-3-day-21.html"},"checksum":"de743004e5af022353e276634e438981b97a22aceae671842aa2a20346b30977"} -->

## 03 QLoRA — Fine-tune trên GPU nhỏ

Slide 12–14: 4-bit NF4, paged optimizer, và bảng chi phí ba phương pháp.

### Slide 12 Section divider

> Trích slide 
>  "03 — QLoRA — Fine-tune trên GPU nhỏ. 4-bit quantization + LoRA = huấn luyện 7B trên RTX 3090"

Đây là slide có sức nặng thực tiễn lớn nhất của cả bài: nó là ranh giới giữa 
 "fine-tuning là việc của phòng lab có A100" và "fine-tuning là việc sinh viên làm được trên máy ở nhà".

### Slide 13 QLoRA — 4-bit NF4 + LoRA Adapters

> Trích slide 
>  "Base Model 4-bit NF4 (frozen) → forward → LoRA bf16 adapters → Paged AdamW (CPU offload khi OOM) → Merged Model (deploy-ready). VRAM giảm ∼3× vs fp16. 
>  QLoRA (Dettmers et al. 2023) — Quantize base model xuống 4-bit NF4, thêm bf16 LoRA adapters. Chỉ train adapters. 
>  ■ Paged AdamW: offload optimizer states sang CPU RAM khi GPU hết bộ nhớ 
>  ■ Double quantization: quantize cả quantization constants — tiết kiệm thêm 
>  ■ Quality drop: chỉ ∼2–5% vs LoRA 16-bit "

_Sơ đồ: Ba thành phần của QLoRA và đường đi tới model deploy - Base model được nén xuống 4-bit và đóng băng, adapter LoRA giữ ở bf16 và là phần duy nhất được huấn luyện, optimizer Paged AdamW đẩy trạng thái sang RAM CPU khi GPU đầy; cuối cùng adapter được gộp vào base thành model sẵn sàng deploy._

Hình 3 — QLoRA (slide 13).

#### Vì sao NF4 chứ không phải int4 thường

NF4 = *4-bit NormalFloat*. Ý tưởng: trọng số của một mạng neural đã train 
 phân bố xấp xỉ **chuẩn (normal)** quanh 0 — không phải phân bố đều. 
 Lượng tử hoá đều (int4) sẽ phí phạm các mức biểu diễn ở vùng đuôi hiếm gặp và thiếu độ phân giải ở vùng 
 giữa dày đặc. NF4 đặt 16 mức của nó theo *phân vị của phân phối chuẩn*, nên mỗi mức 
 "gánh" xấp xỉ cùng một lượng trọng số. Kết quả: sai số nhỏ hơn hẳn ở cùng số bit.

**① Quantize base xuống 4-bit** — mẹo lớn nhất, cắt bộ nhớ model từ ~15 GB xuống ~4 GB.

**② Double quantization** — nén cả các hằng số dùng để nén. Tiết kiệm thêm khoảng 
 0,4 bit/tham số, tức là vài trăm MB. Nhỏ, nhưng miễn phí.

**③ Paged AdamW** — *không* tiết kiệm bộ nhớ. Nó là **van an toàn**: 
 khi GPU sắp tràn, optimizer states được đẩy tạm sang RAM CPU thay vì crash. Đổi lại là chậm hơn.

Phân biệt được ③ với ①② là dấu hiệu đã hiểu bài: hai cái đầu làm bạn *cần ít VRAM hơn*, 
 cái thứ ba chỉ làm bạn *không chết khi thiếu VRAM*.

bậc độ lớn

tự đo trên eval set của mình

### Slide 14 So sánh chi phí — Full FT vs LoRA vs QLoRA

> Trích slide 
>  "Full Fine-tune — VRAM (7B) ∼60GB — Params train 100% — $$$$ — A100 80GB 
>  LoRA (fp16) — ∼28GB — ∼1% — $$ — A100 40GB 
>  QLoRA (4-bit) — ∼10GB — ∼1% — $$ — RTX 3090 24GB 
>  Train QLoRA → merge adapter → quantize GGUF/AWQ → deploy vLLM / llama.cpp 
>  1 base model + nhiều LoRA adapters → serve nhiều domains cùng lúc trên 1 GPU"

Bảng này là lý do QLoRA tồn tại. Nhưng ba con số VRAM ở đây **không phải hằng số** — 
 chúng phụ thuộc batch size, độ dài chuỗi, optimizer, và việc bạn có bật gradient checkpointing hay không. 
 Mô-đun dưới đây tính lại chúng từ công thức để bạn thấy chúng dao động ra sao.

"1 base model + nhiều LoRA adapters → serve nhiều domains cùng lúc trên 1 GPU."

một

"làm sao phục vụ 10 khách hàng với 10 model riêng mà không phá sản?"

#### Tương tác Ngân sách VRAM — vì sao mọi nguồn ghi một con số khác nhau

V tổng = V model + V optimizer + V activations + V gradients. 
 Slide 18 đưa công thức này rồi dừng lại. Đây là nó được tính đầy đủ.

Mặc định: Qwen2.5-7B, QLoRA, batch 1, seq 2048, đã bật FA2 + gradient checkpointing. 
 Đoán trước hai điều:

1. Thành phần nào chiếm nhiều VRAM nhất — base model, optimizer, hay activations?
2. Kéo seq_len từ 2048 lên 8192 (gấp 4). Tổng VRAM tăng bao nhiêu? 
 Rồi tắt gradient checkpointing và đoán lại.

#### Kéo xong rồi mở

**① Base model áp đảo.** Với QLoRA, base 4-bit chiếm khoảng 4,2 GB trong tổng ~7 GB. Optimizer + gradients của adapter chỉ khoảng 0,6 GB — *nhỏ hơn cả phần overhead của CUDA*. Đây là điều LoRA đã thay đổi hoàn toàn: ở full fine-tune, 
 optimizer mới là thành phần lớn nhất.

**② Có gradient checkpointing:** seq 2048 → 8192 chỉ tăng vài GB — activations vẫn 
 tuyến tính và nhỏ. **Tắt checkpointing:** activations bùng lên và con số nhảy dựng đứng.

**Bài học mang đi:** thành phần *chi phối* VRAM khác nhau tuỳ phương pháp:

• **Full FT** → optimizer states chi phối (14 byte cho *mỗi* tham số của model). 
 • **LoRA / QLoRA** → base model chi phối khi seq ngắn, **activations** chi phối khi seq dài.

Biết thành phần nào đang chi phối là biết phải vặn nút nào. Đây chính là cơ sở của quy trình 
 chống OOM ở slide 18: giảm seq_len (đánh vào activations) → bật checkpointing (đánh vào activations) 
 → cuối cùng mới giảm rank (đánh vào optimizer, phần bé nhất).

*Thử thêm — giải thích luôn con số 60GB của slide:* chọn **Full fine-tune** và 
 đổi optimizer sang **AdamW 8-bit**. Con số tụt từ 124 GB xuống 78 GB — hơn một phần ba. Slide ghi "~60GB" là đang 
 ngầm giả định optimizer 8-bit; với AdamW fp32 mặc định thì con số thật gấp đôi. Không nguồn nào sai — 
 họ chỉ không nói ra giả định.

Full fine-tune

LoRA (base bf16)

QLoRA (base 4-bit)

Model

Qwen2.5-7B (7,62B)

Llama-3.1-8B (8,03B)

13B (hidden 5120)

70B (hidden 8192)

Tối ưu bộ nhớ

Không bật gì

FlashAttention 2

FA2 + gradient checkpointing

Optimizer

AdamW fp32 (mặc định)

AdamW 8-bit (bitsandbytes)

- **Control - Batch size 1**: min `1`, max `8`, step `1`, default `1`

- **Control - max_seq_length 2048**: min `512`, max `8192`, step `512`, default `2048`

Tổng VRAM

—

—

GPU nhỏ nhất vừa

—

—

Thành phần chi phối

—

vặn nút này trước khi vặn nút khác

Tham số train

—

—

Base model Optimizer + gradients Activations CUDA overhead

#### Xem dạng bảng



#### Công thức & giả định — đọc trước khi tin con số

- Base: tham số × 2 byte (bf16) hoặc × 0,55 byte (NF4 4-bit + hằng số nén).
- Optimizer + gradients: tham số train × (2 byte gradient + 12 byte AdamW fp32 
 hoặc 6 byte AdamW 8-bit). Với LoRA/QLoRA, "tham số train" là adapter r=16 gắn toàn bộ layer.
- Activations theo công thức của Korthikanti et al. (2022): 
 mỗi layer ≈ s·b·h·(34 + 5·a·s/h) byte. Số hạng 5·a·s/h chính là ma trận 
 attention N×N — FlashAttention làm số hạng này biến mất. 
 Gradient checkpointing thay toàn bộ bằng s·b·h·2 mỗi layer cộng một layer để tính lại.
- CUDA overhead: cố định 1,5 GB (context, phân mảnh, workspace cuBLAS).
- Cấu hình 13B và 70B dùng hình dạng phổ biến của họ Llama; hãy đối chiếu config.json thật.
- Đây là ước lượng bậc độ lớn, không thay thế cho việc chạy thử và đọc 
 nvidia-smi. Nó tồn tại để bạn biết vặn nút nào, không phải để bạn khỏi phải đo.

#### Ô kiểm tra — Chương 3

**1.** QLoRA có ba mẹo: 4-bit NF4, double quantization, paged optimizer. 
 Mẹo nào *không* tiết kiệm VRAM? Hiểu

#### Đáp án

**Paged AdamW.** Nó không làm bạn cần ít VRAM hơn — nó chỉ ngăn bạn crash khi thiếu, 
 bằng cách đẩy tạm optimizer states sang RAM CPU. Đổi lại: chậm hơn do phải chuyển dữ liệu qua lại.

Đây là một **van an toàn**, không phải một kỹ thuật tối ưu. Nếu bạn thấy training 
 chậm bất thường, hãy kiểm tra xem có phải paging đang bị kích hoạt liên tục không — 
 đó là dấu hiệu cấu hình đang vượt quá GPU chứ không phải "QLoRA vốn chậm".

**2.** Cùng một model 7B, hai bài blog ghi VRAM cho full fine-tune là 60GB và 120GB. 
 Cả hai đều không sai. Giải thích. Phân tích

#### Đáp án

Khác nhau ở **optimizer states**, thành phần chi phối của full fine-tune.

AdamW fp32 giữ 3 bản sao fp32 cho mỗi tham số (momentum, variance, master weight) = 12 byte, 
 cộng 2 byte gradient → **14 byte × 7,62 tỷ ≈ 107 GB** chỉ riêng phần này. 
 AdamW 8-bit nén momentum và variance xuống 1 byte mỗi cái → **8 byte × 7,62 tỷ ≈ 61 GB**.

Cộng thêm base model, activations và overhead thì ra hai con số rất khác nhau — từ cùng một model.

**Bài học chung:** mọi con số VRAM trên internet đều kèm một tập giả định *không được viết ra*: optimizer nào, batch bao nhiêu, seq dài bao nhiêu, có checkpointing không. 
 Đừng bao giờ chép một con số VRAM mà không hỏi bốn câu đó.

**3.** Bạn cần phục vụ 8 khách hàng, mỗi khách một domain riêng. Chỉ có 1 GPU 24GB. 
 Làm thế nào? Áp dụng

#### Đáp án

**1 base model + 8 LoRA adapter, hoán đổi lúc chạy.**

Phép tính: base 7B ở 4-bit ≈ 4,2 GB, mỗi adapter (r=16, full target) ≈ 40M tham số × 2 byte ≈ 80 MB. Tám adapter = 640 MB. Tổng khoảng 5 GB, thừa chỗ trên 24 GB — 
 còn dư cho KV cache phục vụ nhiều request đồng thời.

Phương án sai: merge mỗi adapter vào một bản base riêng → 8 model × 4,2 GB = 34 GB → không vừa, 
 và mất luôn khả năng thêm khách hàng thứ 9 mà không mua GPU.

*Công cụ:* vLLM hỗ trợ multi-LoRA serving sẵn. Đây là ý nghĩa thực dụng của 
 "LoRA adapters are composable" ở slide 28.

---

<!-- chiron-source-span: {"source_span_id":"f8f02d88-fdd0-5a4a-b652-f09091bb3b5a","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Dataset & Training Pipeline","source_file":"track-3-day-21.html"},"checksum":"23fdbd18a5a719a6929645f5a7d58ba99834501f7cec6d74d86bfb7f163a8424"} -->

## 04 Dataset & Training Pipeline

Slide 15–22: chuẩn bị dữ liệu, ngân sách VRAM thực chiến, FlashAttention, và setup Unsloth + TRL.

### Slide 15 Section divider

> Trích slide 
>  "04 — Dataset & Training Pipeline. Từ chuẩn bị dữ liệu đến chạy training với Unsloth + TRL"

**Đây là chương quyết định thành bại.** Chương 2–3 có thư viện làm hộ gần hết; 
 chương này thì không ai làm hộ được, vì dữ liệu là thứ duy nhất chỉ bạn mới có.

### Slide 16 Dataset Preparation — Quality over Quantity

> Trích slide 
>  "Raw Data → Clean & Dedup (remove short outputs, filter templates, dedup) → Format (Alpaca/ChatML — match model template) → Train/Val Split 
>  Quy mô cần thiết: ■ Style/format: 500–2k samples chất lượng cao ■ Domain adaptation: 10k+ samples ■ Rule: 500 perfect > 10k noisy 
>  Lưu ý: Data contamination: verify test set KHÔNG overlap training data. Đây là "silent killer" của eval reliability. 
>  Synthetic data: GPT-4 Evol-Instruct cho 10× expansion. Cẩn thận model collapse nếu lạm dụng. 
>  Distillation: generate training data từ strong model (GPT-4, Claude) → fine-tune weaker model. Hiệu quả — nhưng kiểm tra ToS của provider trước."

_Sơ đồ: Pipeline chuẩn bị dữ liệu fine-tuning - Dữ liệu thô đi qua bốn bước: làm sạch và khử trùng lặp, định dạng theo template của model, chia train và validation, rồi kiểm tra rò rỉ dữ liệu giữa hai tập._

Hình 4 — Pipeline dữ liệu (slide 16).

cổng kiểm tra

#### "500 perfect > 10k noisy" — vì sao đúng, và khi nào sai

Trong SFT, model học *bắt chước* từng mẫu. Một mẫu sai cũng được bắt chước y như một mẫu đúng — 
 không có cơ chế nào để model "biết" mẫu này kém. Với 10k mẫu nhiễu, bạn đang dạy model **bắt chước cả cái nhiễu đó** một cách nhất quán.

500–2k

10k+

- Style/format = học một khuôn. Khuôn thì lặp lại, nên vài trăm ví dụ đủ để model nắm được.
- Domain adaptation = học cả một vùng ngôn ngữ. Vùng thì rộng, cần nhiều mẫu để phủ.

giống

#### Data contamination — vì sao gọi là "silent killer"

Nếu một mẫu xuất hiện ở cả train và val, model đã *thấy đáp án*. Eval loss sẽ đẹp, 
 perplexity sẽ thấp, biểu đồ sẽ mượt — và **không có bất kỳ tín hiệu lỗi nào**. 
 Bạn chỉ phát hiện ra khi model gặp dữ liệu thật và trả lời tệ.

**① Chia split *sau* khi tăng cường dữ liệu.** Nếu bạn paraphrase mỗi mẫu thành 
 3 bản rồi mới chia, các bản của cùng một mẫu gốc sẽ rơi vào cả hai tập. *Chặn:* luôn chia split **trước**, rồi mới augment riêng từng tập.

**② Trùng lặp gần đúng.** Khử trùng lặp bằng so khớp chính xác sẽ bỏ sót các cặp chỉ 
 khác dấu câu hoặc khoảng trắng. *Chặn:* chuẩn hoá text rồi hash, hoặc dùng MinHash cho trùng lặp mờ.

**③ Cùng một nguồn bị tách nhỏ.** Một tài liệu dài cắt thành 20 đoạn, các đoạn rơi 
 vào cả hai tập. *Chặn:* chia theo **nhóm nguồn**, không chia theo dòng.

*Với SmartCheck AI:* nếu sau này bạn xây eval set từ log thật, mỗi phiên check-in phải nằm 
 trọn trong một tập — không được để lượt 1 của phiên ở train còn lượt 3 ở val.

**Model collapse:** nếu bạn train trên dữ liệu do chính lớp model đó sinh ra, qua nhiều 
 vòng lặp phân phối sẽ thu hẹp dần — model mất đuôi phân phối, chỉ còn nói những thứ "trung bình". 
 Slide nói "cẩn thận nếu lạm dụng"; quy tắc thực dụng là luôn giữ một tỷ lệ dữ liệu *người viết*.

**ToS của provider:** slide dặn "kiểm tra ToS trước" khi dùng GPT-4/Claude sinh dữ liệu 
 để train model khác. Đây là một ràng buộc *pháp lý*, không phải kỹ thuật — nó không hiện ra 
 trong loss curve, nhưng nó có thể chặn cả sản phẩm ở khâu cuối. Kiểm tra trước khi sinh 10k mẫu, 
 không phải sau.

### Slide 17 Training Pipeline — Full Workflow

> Trích slide 
>  "1. Dataset Prep & Clean (Alpaca/ChatML, dedup, balance) → 2. Config PEFT + QLoRA (r=16, alpha=32, target_modules) → 3. Train Unsloth/TRL (lr=2e-4, cosine, packing=True) → 4. Eval, Merge & Deploy (merge adapter, GGUF → vLLM) 
>  Model + Optimizer + Activations + Gradients. QLoRA giảm ∼60% vs full fp16. Flash Attention 2: bắt buộc — 2–4× speedup. 
>  RTX 3090 (24GB): 7B QLoRA · A100 (40GB): 13B QLoRA · H100 (80GB): 70B QLoRA · Grad. checkpoint: −60% VRAM, +20% time"

Bốn bước, nhưng công sức **không** chia đều. Phân bổ thực tế trong một project thật:

| Bước | % thời gian thực tế | Vì sao |
| --- | --- | --- |
| 1 · Dataset prep | ~70% | Thu thập, làm sạch, gán nhãn, khử trùng, kiểm rò rỉ — không thư viện nào làm hộ |
| 2 · Config PEFT | ~5% | Vài chục dòng, có sẵn giá trị mặc định tốt |
| 3 · Train | ~10% | Chủ yếu là chờ. Trừ khi OOM — rồi thì xem slide 18 |
| 4 · Eval, merge, deploy | ~15% | Eval nghiêm túc tốn công hơn người ta tưởng |

vui nhất

### Slide 18 Training Infrastructure — VRAM Math & Practical Settings

> Trích slide 
>  "VRAM budget breakdown: V tot = V model + V optim + V act + V grad 
>  ■ Flash Attention 2: bắt buộc — 2–4× speedup, giảm activations memory đáng kể 
>  ■ Gradient checkpointing: recompute activations khi backward → −60% VRAM, +20% time 
>  ■ QLoRA + FlashAttn 2 + grad checkpoint ⇒ ∼10GB cho 7B model 
>  Phân tích token distribution của dataset → set max_seq_length = p95. Tránh padding lãng phí. 
>  batch eff = batch × grad_accum. Khi VRAM hạn chế: batch=1, grad_accum=4--8. Mục tiêu: batch eff ∈ [16, 64] 
>  Lưu ý: OOM debugging: giảm max_seq_length trước, sau đó bật grad checkpointing, cuối cùng giảm rank. 
>  Đừng chỉ giảm batch size — ảnh hưởng convergence. "

#### Mẹo bị chôn giữa slide mà đáng lẽ phải in đậm: max_seq_length = p95

Đặt `max_seq_length` theo **phân vị 95 của độ dài token trong dataset**, 
 không phải theo con số tròn quen thuộc (2048, 4096). Lý do:

- Activations tỷ lệ tuyến tính với seq_len (và tỷ lệ bậc hai 
 nếu chưa bật FlashAttention). Đặt 4096 khi p95 của bạn là 900 nghĩa là bạn trả tiền cho hơn 4 lần 
 lượng bộ nhớ mà bạn dùng.
- Phần dư là padding — token vô nghĩa mà GPU vẫn phải tính.
- 5% mẫu dài hơn p95 sẽ bị cắt bớt. Đó là đánh đổi có ý thức, và thường rẻ hơn nhiều so với việc 
 nhân đôi bộ nhớ cho toàn bộ dataset.

```text
import numpy as np
lens = [len(tok(x["text"])["input_ids"]) for x in dataset]
print(f"p50={np.percentile(lens,50):.0f}  p95={np.percentile(lens,95):.0f}  max={max(lens)}")
```

max_seq_length=2048

#### Quy trình chống OOM — và vì sao thứ tự lại như vậy

| Thứ tự | Việc làm | Đánh vào thành phần nào | Cái giá |
| --- | --- | --- | --- |
| 1 | Giảm max_seq_length | Activations — thường là thành phần co giãn lớn nhất | Cắt bớt mẫu dài |
| 2 | Bật gradient checkpointing | Activations — cắt ~60% | Chậm hơn ~20% |
| 3 | Giảm rank | Optimizer states — phần nhỏ nhất | Mất năng lực adapter |
| ✕ | Giảm batch size một mình | Activations, nhưng… | Hỏng convergence — batch hiệu dụng nhỏ làm gradient nhiễu |

Thứ tự này là hệ quả trực tiếp của việc *thành phần nào đang chi phối* — thứ mà [máy tính VRAM](#m-vram) ở trên cho bạn thấy bằng số. Nếu bắt buộc phải giảm batch, 
 hãy tăng `grad_accum` tương ứng để giữ `batch_eff` trong khoảng 16–64.

### Slide 19 FlashAttention — IO-Aware Exact Attention

> Trích slide 
>  "Dao et al. 2022, FA2 (2023), FA3 (2024) 
>  Vanilla attention đọc/ghi ma trận N×N qua HBM (slow) ⇒ memory-bound. FlashAttention dùng tiling + recomputation: 
>  tải block nhỏ vào SRAM (on-chip, ∼20 MB nhưng ∼10× nhanh hơn HBM), tính softmax theo từng block, 
>  tránh materialize ma trận attention N×N. 
>  Kết quả: exact attention (không xấp xỉ) — nhưng 2–4× nhanh hơn và memory O(N) thay vì O(N²). "

Hai chữ quan trọng nhất trong slide: **"exact attention"** và **"IO-aware"**.

xấp xỉ

kết quả giống hệt

"bắt buộc"

ngồi chờ dữ liệu

sắp xếp lại

### Slide 20 FlashAttention — Memory Hierarchy & Tiling

> Trích slide 
>  "SRAM (on-chip) ∼20MB · ∼19TB/s — ∼10× nhanh · HBM (GPU memory) 40–80GB · ∼2TB/s — chậm hơn · DRAM (CPU RAM) >100GB · ∼50GB/s — chậm nhất 
>  Tiling: Q, K, V chia khối nhỏ 
>  Vì sao nhanh hơn? ■ Vanilla: ghi ma trận N×N vào HBM → memory-bound ■ FA: streaming tiles qua SRAM → compute-bound ■ Backward: recompute attention thay vì store → tiết kiệm activation memory 
>  FA1 (2022): tiling cơ bản · FA2 (2023): better parallelism, +2× speed · FA3 (2024): Hopper TMA, FP8, cho H100"

_Sơ đồ: Phân cấp bộ nhớ GPU và ý tưởng tiling của FlashAttention - Ba tầng bộ nhớ xếp theo tốc độ: SRAM trên chip nhanh nhất nhưng chỉ khoảng 20 megabyte, HBM là bộ nhớ GPU 40 đến 80 gigabyte chậm hơn khoảng 10 lần, DRAM của CPU lớn nhất và chậm nhất. FlashAttention giữ các khối nhỏ trong SRAM thay vì ghi ma trận attention đầy đủ xuống HBM._

Hình 5 — Phân cấp bộ nhớ (slide 20).

đưa gì lên thanh trên cùng, và giữ nó ở đó bao lâu

#### Tương tác FlashAttention xoá số hạng nào — và xoá được bao nhiêu

Bộ nhớ activation mỗi layer ≈ `s·b·h·(34 + 5·a·s/h)` byte 
 (Korthikanti et al. 2022). Số hạng thứ hai chính là ma trận attention N×N — thứ FlashAttention làm biến mất. 
 Kéo độ dài chuỗi và nhìn nó bùng nổ.

Qwen2.5-7B, batch 1, độ dài chuỗi **2048**: activation vanilla khoảng 23 GB. 
 Đoán trước: kéo lên **8192** (gấp 4 độ dài) thì vanilla thành bao nhiêu?

#### Kéo xong rồi mở

**Không phải gấp 4. Gần gấp 12** — từ ~23 GB lên ~290 GB.

**Vì sao:** công thức có hai số hạng với hai hành vi khác nhau. Số hạng `34` tuyến tính theo `s`; số hạng `5·a·s/h` làm cho phần đó **bậc hai** theo `s`. Ở chuỗi ngắn, phần tuyến tính còn đáng kể; 
 ở chuỗi dài, phần bậc hai nuốt tất cả.

Với FlashAttention, số hạng bậc hai *biến mất hoàn toàn* — không phải giảm bớt, mà là 
 không bao giờ được tạo ra. Bộ nhớ trở lại tuyến tính: gấp 4 độ dài thì gấp 4 bộ nhớ, đúng như trực giác.

**Bài học mang đi:** đây là lý do FlashAttention không phải "một tối ưu hay ho" 
 mà là **điều kiện cần** để train chuỗi dài. Không có nó, ngưỡng 8k token đơn giản là 
 bất khả thi trên mọi GPU đơn lẻ — kể cả H100 80GB. Slide 18 gọi nó là "bắt buộc" theo đúng nghĩa đen.

*Thử thêm:* bật thêm gradient checkpointing. Đường thứ ba tụt xuống gần như phẳng — 
 đó là tổ hợp mà slide 18 nói cho ra "~10GB cho 7B model". Ba kỹ thuật cộng dồn: 
 4-bit cắt base, FlashAttention cắt số hạng bậc hai, checkpointing cắt phần tuyến tính còn lại.

Model

Qwen2.5-7B

Llama-3.1-8B

13B

70B

- **Control - Batch size 1**: min `1`, max `8`, step `1`, default `1`

- **Control - Độ dài chuỗi 2048**: min `512`, max `8192`, step `512`, default `2048`

Vanilla attention

—

O(N²) — bậc hai theo độ dài

FlashAttention 2

—

O(N) — tuyến tính

FA2 + checkpointing

—

tổ hợp của slide 18

FlashAttention tiết kiệm

—

phần ma trận N×N không bao giờ được tạo ra

Vanilla (bậc hai) FlashAttention 2 FA2 + gradient checkpointing

#### Xem dạng bảng



#### Công thức & giới hạn của mô hình

- Activations mỗi layer ≈ s·b·h·(34 + 5·a·s/h) byte — Korthikanti et al. 2022, cho transformer bf16.
- FlashAttention loại bỏ số hạng 5·a·s/h (ma trận attention N×N không bao giờ được materialize).
- Gradient checkpointing thay bằng s·b·h·2 mỗi layer, cộng một layer đầy đủ để tính lại lúc backward.
- Đây là ước lượng: cài đặt thật khác nhau ở chi tiết (fused kernel, cách lưu residual…). 
 Dùng nó để hiểu hình dạng của đường cong, không phải để dự đoán chính xác tới từng MB.
- Con số tốc độ "2–4×" ở slide phụ thuộc phần cứng và độ dài chuỗi; mô-đun này chỉ mô hình bộ nhớ, không mô hình tốc độ.

### Slide 21 FlashAttention — Khi nào dùng & Cách bật

> Trích slide 
>  "Hardware: ■ Ampere+: A100, RTX 30xx, RTX 40xx (FA2 OK) ■ Hopper: H100, H200 (FA3 mới nhất, FP8) ■ Không hỗ trợ: V100, T4 (chỉ Turing) 
>  Sequence length sweet spot: ■ Short (<512): speedup nhỏ, vẫn nên bật ■ Medium (1k–4k): 2–3× speedup ■ Long (8k+): 4×+ speedup, memory tiết kiệm rất lớn 
>  Cách bật: from_pretrained(..., attn_implementation="flash_attention_2") — tự động bật FA2 ngay khi load model 4-bit. 
>  Install: pip install flash-attn --no-build-isolation (cần CUDA toolkit + nvcc, build ∼10 phút) 
>  Common pitfall: nếu thấy "flash_attn not installed" warning → HuggingFace fallback về SDPA (chậm hơn 2×). 
>  Luôn verify FA đã active bằng model.config._attn_implementation. "

HuggingFace **không báo lỗi** khi không cài được flash-attn. Nó chỉ in một dòng warning 
 rồi âm thầm chuyển sang SDPA. Training vẫn chạy, loss vẫn giảm, không có gì hỏng — 
 bạn chỉ đơn giản là chạy **chậm gấp đôi** mà không biết.

Và cái bẫy đặc biệt hiểm ở chỗ: dòng warning bị chôn giữa hàng chục dòng log khởi động.

**Một dòng để kiểm tra, chạy nó mọi lần:**

```text
print(model.config._attn_implementation)   # phải in ra: flash_attention_2
```

Nếu nó in `sdpa` hoặc `eager` thì FlashAttention *không* hoạt động, 
 bất kể bạn đã truyền tham số gì.

V100 và T4 không hỗ trợ

Google Colab bản miễn phí

!nvidia-smi

### Slide 22 Unsloth + TRL SFTTrainer — Production Setup

> Trích slide 
>  " FastLanguageModel.from_pretrained("unsloth/Qwen2.5-7B-bnb-4bit", max_seq_length=2048, load_in_4bit=True) → 
>  get_peft_model(model, r=16, lora_alpha=32, target_modules=["q_proj","k_proj","v_proj","o_proj","gate_proj","up_proj","down_proj"]) → 
>  SFTTrainer(..., packing=True) # 2x throughput 
>  Key settings: ■ Unsloth: custom CUDA kernels — 2× faster, 60% less VRAM ■ packing: gộp samples vào 1 sequence — 2× throughput ■ LR: 2e-4 → 5e-5, cosine schedule ■ Warmup: 5–10% total steps 
>  Lưu ý: Overfitting: eval loss tăng + train loss giảm ⇒ dừng training, giảm epochs hoặc tăng data. "

Chú ý một điều thú vị: **đoạn code trên slide này liệt kê đủ 7 target module** (q, k, v, o, gate, up, down) — tức là đúng "2025 best practice" của slide 10. 
 Nhưng [slide 26](#s26) lại hướng dẫn lab dùng `q_proj+v_proj`. 
 Hai chỗ mâu thuẫn nhau, và code trên slide 22 mới là chỗ đúng cho production.

#### Sequence packing — "free 2× speedup" nghĩa là gì

Không packing: mỗi mẫu là một sequence, ngắn hơn `max_seq_length` thì độn padding. 
 Nếu p50 dataset của bạn là 220 token mà `max_seq_length=2048`, 
 thì **gần 90% mỗi batch là padding** — GPU tính toán trên số không.

Có packing: nhiều mẫu được nối lại cho đầy một sequence 2048 token, ngăn cách bằng token đặc biệt. 
 Cùng lượng tính toán, nhưng gần như toàn bộ là dữ liệu thật.

packing=True

Một lưu ý nhỏ nhưng thật:

không liên quan

#### Dấu hiệu overfitting — và vì sao nó rất dễ xảy ra ở đây

Slide đưa dấu hiệu kinh điển: **eval loss tăng trong khi train loss vẫn giảm**. 
 Với fine-tuning LoRA trên dataset nhỏ (500–2k mẫu như khuyến nghị), điều này xảy ra *rất nhanh* — 
 thường ngay trong epoch thứ 2 hoặc 3.

```text
train loss ↓   eval loss ↓     → đang học. Tiếp tục.
train loss ↓   eval loss phẳng → gần bão hoà. Chuẩn bị dừng.
train loss ↓   eval loss ↑     → ĐANG GHI NHỚ, không học nữa. DỪNG.
train loss →   eval loss →     → learning rate quá thấp, hoặc adapter thiếu năng lực
                                 (kiểm tra target_modules trước khi tăng rank)
```

eval set

eval_steps

load_best_model_at_end

#### Ô kiểm tra — Chương 4

Chương dài nhất, và cũng là chương chứa nhiều bẫy thực chiến nhất.

**1.** Training chạy được, loss giảm đẹp, nhưng chậm gấp đôi dự kiến. 
 Nghi phạm số một là gì? Áp dụng

#### Đáp án

**FlashAttention không thật sự được bật.** HuggingFace âm thầm fallback về SDPA 
 khi không import được `flash_attn`, chỉ in một dòng warning giữa hàng chục dòng log.

Kiểm tra bằng một dòng: `print(model.config._attn_implementation)` — 
 phải là `flash_attention_2`.

*Nghi phạm số hai:* quên `packing=True`, nên phần lớn mỗi batch là padding. *Nghi phạm số ba:* GPU là T4/V100, vốn không hỗ trợ FA2 — lúc đó không phải lỗi cấu hình 
 mà là giới hạn phần cứng.

**2.** Eval loss của bạn rất đẹp nhưng model trả lời tệ trên dữ liệu thật. 
 Nguyên nhân khả dĩ nhất? Phân tích

#### Đáp án

**Data contamination** — eval set trùng với training data. Slide 16 gọi đây là 
 "silent killer" vì nó không tạo ra bất kỳ tín hiệu lỗi nào: loss đẹp, biểu đồ mượt, không có exception.

Ba nguồn rò rỉ hay gặp: ① augment dữ liệu *trước* khi chia split; ② khử trùng lặp chỉ bằng 
 so khớp chính xác nên bỏ sót trùng lặp gần đúng; ③ một tài liệu dài bị cắt nhỏ rồi các đoạn rơi vào cả hai tập.

*Cách kiểm tra nhanh:* chuẩn hoá text rồi hash mọi mẫu ở cả hai tập, đếm phần giao. 
 Kỳ vọng là 0. Nếu khác 0, mọi con số eval của bạn phải làm lại.

**3.** Dataset của bạn có p50 = 180 token, p95 = 620, mẫu dài nhất 7.400. 
 Đặt `max_seq_length` bằng bao nhiêu, và vì sao không phải 8192? Đánh giá

#### Đáp án

**Khoảng 640–768** — bám theo p95, làm tròn lên, theo đúng khuyến nghị slide 18.

**Vì sao không phải 8192:** activations tỷ lệ tuyến tính với `seq_len` (và bậc hai nếu chưa có FlashAttention). Đặt 8192 khi p95 là 620 nghĩa là bạn trả hơn **13 lần** bộ nhớ activations để phục vụ đúng vài mẫu ngoại lệ — trong khi phần dư 
 chỉ là padding mà GPU vẫn phải tính.

**Cái giá:** 5% mẫu dài hơn 620 sẽ bị cắt bớt. Đó là đánh đổi có ý thức và 
 gần như luôn đáng — dùng chỗ VRAM tiết kiệm được để tăng batch, gradient sẽ ổn định hơn.

*Cái bẫy:* con số 7.400 rất dễ khiến bạn hoảng và đặt 8192 "cho chắc". 
 Đó chính xác là lý do slide bảo dùng **p95** chứ không phải **max**.

---

<!-- chiron-source-span: {"source_span_id":"3c984bd5-4a0b-536c-a3f6-53b82bd5039b","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Demo & Thực hành","source_file":"track-3-day-21.html"},"checksum":"5a3d4eb1b9240c5f90aa81b8e127baa2b16dd71f23297e3c3bc5a6a45c8eb798"} -->

## 05 Demo & Thực hành

Slide 23–27: demo domain tiếng Việt, Lab 21 và bảng thí nghiệm rank.

### Slide 23 Section divider

> Trích slide 
>  "05 — Demo & Thực hành. Xem fine-tuning hoạt động thực tế trên domain Việt Nam"

### Slide 24 Fine-tune trên Vietnamese Domain Dataset

> Trích slide 
>  "1. Dataset: 1k Vietnamese QA pairs (Alpaca format). Training: 3 epochs, ∼25 min on A100 
>  2. Before: base model trả lời generic. After: dùng domain terminology chính xác 
>  3. LoRA adapter swap: load khác adapters cho khác domains — multi-tenant serving 
>  4. GGUF demo: merge adapter → convert → run llama.cpp — deployment ready"

Chú ý demo này minh hoạ đúng **loại vấn đề mà fine-tuning giải được**: 
 "trả lời generic" → "dùng domain terminology chính xác". Đó là *cách nói*, không phải *sự kiện*. 
 Nếu demo là "model không biết luật X" → "model biết luật X" thì nó đã minh hoạ sai bài học của slide 5.

không phải một dự án hàng tuần

nên

một

Điểm 3 ( *adapter swap* ) là phần đáng xem nhất của demo, vì nó là thứ khó hình dung nhất từ lý thuyết: 
 cùng một base model nằm trong VRAM, đổi adapter là đổi hẳn "tính cách" và vốn từ của model — 
 trong vài trăm mili-giây, không phải nạp lại 15 GB.

### Slide 25 Lab #21

> Trích slide 
>  "Mục tiêu: Fine-tune Qwen2.5-7B với LoRA/QLoRA trên custom Vietnamese dataset (dùng Unsloth + TRL) 
>  Deliverable: LoRA adapter checkpoint + evaluation report: perplexity delta, 5 qualitative before/after examples, 
>  training cost — so sánh rank r = 8 vs r = 64. Thời gian: 2 giờ"

Giống Lab 20, deliverable **không phải "model chạy được"** mà là *evaluation report*. Ba thành phần được yêu cầu bổ trợ nhau và không thay thế nhau được:

| Thành phần | Trả lời câu hỏi gì | Điểm mù của nó |
| --- | --- | --- |
| Perplexity delta | Model có khớp hơn với phân phối domain không? | Perplexity thấp không đảm bảo câu trả lời hữu ích. Model có thể học vẹt văn phong mà nội dung vẫn sai. |
| 5 ví dụ before/after | Con người có thấy khác biệt không? | Chỉ 5 mẫu — dễ vô tình chọn toàn mẫu thuận lợi. Hãy chọn trước khi train. |
| Training cost | Có đáng tiền không? | Không nói gì về chi phí vận hành sau này, vốn thường lớn hơn. |

Chọn 5 prompt before/after TRƯỚC khi train, và ghi lại.

### Slide 26 Lab 21 — 5 bước thực hành chi tiết

> Trích slide 
>  "1. Data prep (15p): 100–500 examples Alpaca format. Clean, tokenize, verify max_seq_length (p95), split 90/10 
>  2. Configure PEFT (10p): r=16, alpha=32, target q_proj+v_proj. Setup QLoRA 4-bit với Unsloth FastLanguageModel 
>  3. Train baseline (40p): TRL SFTTrainer, 3 epochs, packing=True, cosine LR, warmup 10%. Monitor loss curve — detect overfitting 
>  4. Rank experiment (30p): train 2 adapters với r=8 và r=64 trên cùng dataset. So sánh: training time, VRAM, eval perplexity, qualitative output 
>  5. Evaluate (15p): perplexity trên eval set, generate 20 test prompts, so sánh fine-tuned vs base 
>  Deliverable: (1) 3 adapter checkpoints (2) bảng perplexity delta + training cost (3) 5 ví dụ before/after (4) kết luận về rank selection trade-off"

Slide 10 nói: *"2025 best practice: ALL attention + MLP layers. q_proj + v_proj alone thiếu capacity."* 
 Slide 26 hướng dẫn lab: *"target q_proj+v_proj"*. 
 Slide 22 (code production) lại liệt kê đủ 7 module.

**Đây không phải lỗi.** Lab bị ép trong 2 giờ và phải train *ba* adapter, 
 nên cấu hình nhẹ là lựa chọn thực tế. Nhưng nếu perplexity của bạn cải thiện ít, 
 đây là nghi phạm số một chứ không phải rank.

**Cách biến mâu thuẫn này thành điểm cộng:** nếu còn thời gian, train thêm *một* adapter r=16 với đủ 7 target module, và đưa nó vào bảng so sánh như một dòng thứ tư. 
 Kết luận kiểu *"đổi target_modules cải thiện nhiều hơn nhân tư rank"* — nếu số liệu của bạn 
 nói vậy — là loại phát hiện phân biệt một báo cáo làm cho xong với một báo cáo có suy nghĩ.

#### Rủi ro thời gian: bước 1 chỉ được cấp 15 phút

Slide 17 ngầm nói dataset chiếm phần lớn công sức thật; lab lại chỉ cấp 15 phút cho nó. 
 Đây là ràng buộc của lớp học, không phải của thực tế — nhưng nó tạo ra một rủi ro cụ thể: **bạn sẽ bị cám dỗ bỏ qua bước kiểm tra rò rỉ.**

```text
norm = lambda s: " ".join(s.lower().split())
tr = {norm(x["output"]) for x in train}
ov = [x for x in val if norm(x["output"]) in tr]
print(f"Rò rỉ: {len(ov)}/{len(val)} mẫu val trùng train")   # kỳ vọng: 0
```

### Slide 27 Lab 21 — Rank Experiment Worksheet

> Trích slide 
>  "Cấu hình | Train time | Peak VRAM | Eval PPL | Qualitative — Base (no FT): —, —,?, generic · 
>  LoRA r=8:???? · LoRA r=16:???? · LoRA r=64:???? 
>  Rank nào cho ROI tốt nhất trên dataset của bạn? Khi nào tăng rank không còn cải thiện perplexity 
>  (diminishing returns)? Khi nào nên chọn r = 8 thay vì r = 16? "

Ba câu hỏi cuối slide là ba câu hỏi **bạn phải trả lời bằng số của mình**, không phải 
 bằng lý thuyết. Dưới đây là những gì nên dự đoán trước khi chạy — để sau đó biết mình sai ở đâu:

| Cột | Dự đoán hợp lý | Nếu kết quả khác dự đoán thì nghĩa là gì |
| --- | --- | --- |
| Train time | Gần như không đổi giữa r=8 và r=64 — rank chỉ thêm vài phép nhân gầy | Nếu chênh nhiều: có thể bạn vô tình đổi cả seq_len hoặc batch giữa các lần chạy |
| Peak VRAM | Chênh vài trăm MB, không phải vài GB | Nếu chênh nhiều GB: nghi ngờ có yếu tố khác thay đổi — rank không đủ sức làm điều đó |
| Eval PPL | r=8 → r=16 cải thiện rõ; r=16 → r=64 cải thiện ít hoặc xấu đi | r=64 xấu hơn = overfitting trên dataset nhỏ. Đây là kết quả tốt, hãy viết vào báo cáo |
| Qualitative | Khác biệt lớn nhất là base vs bất kỳ FT nào, không phải giữa các rank | Nếu không phân biệt được base với FT: kiểm tra adapter đã thật sự được load chưa |

khi dataset nhỏ và r=16 đã có dấu hiệu overfit

năng lực

bộ nhớ

---

<!-- chiron-source-span: {"source_span_id":"5090ccc1-b6ab-59f1-9aad-43bc8055694f","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Tổng kết, tài liệu & bài tiếp theo","source_file":"track-3-day-21.html"},"checksum":"ade7ad2d386c336b9cb72c5b8b8b8dbc0d98382f43bddd2e6d072469b3116d22"} -->

## 06 Tổng kết, tài liệu & bài tiếp theo

Slide 28–31.

### Slide 28 Key Takeaways

> Trích slide 
>  "1 QLoRA democratize fine-tuning — consumer GPU (RTX 3090) đủ cho 7B–8B models 
>  2 Dataset quality là yếu tố quan trọng nhất — 500 perfect > 10k noisy 
>  3 Sequence packing là free 2× speedup — luôn bật packing=True 
>  4 LoRA adapters are composable — serve nhiều adapters cùng lúc trên 1 base model"

Bốn takeaway này nói về bốn thứ rất khác nhau, và đáng đọc theo trục "cái gì thay đổi được nhờ bài học này":

| # | Thay đổi điều gì | Hệ quả thực tế |
| --- | --- | --- |
| 1 | Ai được fine-tune | Từ "phòng lab có A100" thành "bất kỳ ai có RTX 3090". Đây là thay đổi về tiếp cận, không phải kỹ thuật. |
| 2 | Công sức đổ vào đâu | Dồn vào dữ liệu, không dồn vào siêu tham số. Ngược với bản năng. |
| 3 | Tốc độ, miễn phí | Một tham số, gấp đôi throughput. Không có mặt trái ⇒ không có gì để cân nhắc. |
| 4 | Kiến trúc phục vụ | Nhiều domain trên một GPU. Đây là takeaway có giá trị kinh doanh lớn nhất. |

Fine-tune không sửa knowledge gap.

### Slide 29 Tiếp theo & Bài tập

> Trích slide 
>  "Ngày 22: DPO, ORPO & Alignment — SFT dạy format — DPO/ORPO dạy alignment (helpful + safe). 
>  RLHF tốn kém — DPO có thể thay thế? 
>  ■ Hoàn thành Lab 21: LoRA fine-tune + benchmark report 
>  ■ Đọc: Rafailov et al. "Direct Preference Optimization" (2023)"

Câu dẫn của Ngày 22 định vị rất gọn thứ Ngày 21 *không* làm được:

```text
SFT (Ngày 21)          → dạy model "câu trả lời trông NHƯ THẾ NÀO"
                          học từ ví dụ ĐÚNG, bắt chước từng mẫu

DPO / ORPO (Ngày 22)   → dạy model "câu trả lời nào TỐT HƠN câu nào"
                          học từ CẶP so sánh (chosen vs rejected)

Khác biệt cốt lõi: SFT không có khái niệm "tệ hơn".
Nó chỉ thấy mẫu tốt và bắt chước — nên không học được cách TRÁNH.
```

cái gì tệ hơn cái gì

### Slide 30 Hỏi & Đáp

> Trích slide 
>  "Khi nào thì fine-tune thực sự cần thiết? Bạn có use case cụ thể nào muốn thảo luận?"

Trả lời gọn cho câu thứ nhất, gộp cả bài lại thành ba điều kiện phải **đồng thời** đúng:

1. Vấn đề là style/format/jargon, không phải kiến thức (slide 5).
2. Few-shot prompt và RAG đã thử và vẫn thiếu > 15% — có số đo, không phải cảm giác (slide 6).
3. Có đủ dữ liệu chất lượng: 500–2k mẫu sạch cho style, 10k+ cho domain (slide 16).

Thiếu bất kỳ điều nào trong ba điều trên thì câu trả lời là "chưa". Điều kiện về volume 
 (> 50k/ngày) chỉ quyết định *self-host hay API*, không quyết định *có fine-tune hay không*.

### Slide 31 Cảm ơn

> Trích slide 
>  "Cảm ơn! AICB-P2T3 · Ngày 21 · Fine-tuning LLMs — Từ Full Fine-tune đến LoRA/QLoRA — 
>  github.com/vinuni-aicb — Liên hệ: instructor@vinuni.edu.vn"

---

<!-- chiron-source-span: {"source_span_id":"6ade7e2e-4545-5d5e-b26d-913cf620dbbe","locator":{"kind":"html_section","section_id":"ladder","order":9,"heading":"▤ Luyện kỹ năng cốt lõi: chẩn đoán trước khi kê đơn","source_file":"track-3-day-21.html"},"checksum":"8b0f134f82c376cdd3ead1d5a2a5e2d49e56cef895b130a8eccde7811026d423"} -->

## ▤ Luyện kỹ năng cốt lõi: chẩn đoán trước khi kê đơn

Kỹ năng mà quiz, lab và phỏng vấn đều hỏi không phải "LoRA hoạt động thế nào" — 
 mà là **"vấn đề này có phải vấn đề fine-tuning giải được không"**. 
 Ba bài dưới đây giảm dần sự trợ giúp. Làm đúng thứ tự.

① Triệu chứng chính xác là gì?

② Có phải knowledge gap không?

thấp nhất

④ Nếu fine-tune: dữ liệu ở đâu, bao nhiêu, sạch không?

⑤ Đo bằng gì, và dừng ở đâu?

#### Chatbot CSKH trả lời đúng nội dung nhưng dài dòng và không theo mẫu công ty

Đọc kỹ cách *lập luận*. Bài 2 và 3 sẽ yêu cầu bạn lặp lại đúng mạch này.

1. Triệu chứng: sai format và giọng, KHÔNG sai nội dung. Model trả lời đúng sự thật 
 nhưng viết 6 đoạn trong khi công ty muốn 3 gạch đầu dòng và một câu chốt. 
 Cách phân biệt: nếu bạn tự viết lại câu trả lời của model theo mẫu mà không cần tra cứu gì thêm, 
 thì nội dung vốn đã đúng — vấn đề là hình thức.
2. Không phải knowledge gap. Phép thử: nếu ngày mai chính sách công ty đổi, 
 bạn có phải train lại không? Không — mẫu trình bày không đổi theo chính sách.
3. Bậc thấp nhất đủ giải: thử few-shot trước, và nó thường đủ. 
 3–5 ví dụ đúng mẫu trong prompt giải quyết được phần lớn bài toán format. 
 Chỉ leo lên fine-tune khi: (a) few-shot vẫn trôi mẫu ở các ca lạ, và (b) prompt few-shot 
 quá dài đang ăn tiền ở mọi request — lúc đó fine-tune vừa sửa format vừa cắt cost.
4. Dữ liệu: đây là bài toán style/format nên chỉ cần 500–2k mẫu. 
 Nguồn tốt nhất: lịch sử ticket đã được nhân viên giỏi trả lời — sẵn có, đúng giọng công ty, người viết. 
 Làm sạch: bỏ output quá ngắn, lọc câu trả lời mẫu tự động, khử trùng lặp.
5. Đo & dừng: perplexity không phải metric chính ở đây. 
 Metric đúng là tỷ lệ output đúng mẫu — viết một hàm kiểm tra cấu trúc và chấm tự động 
 trên 200 mẫu eval. Dừng khi eval loss quay đầu (thường epoch 2–3 với dataset cỡ này).

Câu chốt kiểu phỏng vấn "Triệu chứng là format chứ không phải nội dung, nên RAG không giúp được. Tôi thử few-shot trước và đo 
 tỷ lệ đúng mẫu; nó đạt 82% nhưng prompt dài 1.200 token cho mọi request. Fine-tune LoRA trên 800 ticket 
 lịch sử đưa tỷ lệ lên 96% và cắt prompt xuống còn 150 token — nên nó thắng ở cả chất lượng lẫn chi phí."

#### Model dịch tài liệu pháp lý, dùng sai thuật ngữ chuyên ngành

Hai bước đầu đã làm sẵn. Ba bước sau bạn tự viết ra giấy rồi mới mở đáp án.

1. Triệu chứng: sai jargon. Model dịch "consideration" trong hợp đồng thành 
 "sự cân nhắc" thay vì "đối ứng"/"nghĩa vụ đối ứng". Ngữ pháp đúng, nghĩa thông thường đúng, 
 nghĩa pháp lý sai.
2. Ranh giới mờ giữa style và knowledge. Thuật ngữ vừa là cách nói 
 (thuộc về fine-tune) vừa có thể tra được trong từ điển chuyên ngành (thuộc về RAG). 
 Đây chính là chỗ khiến bài này khó hơn bài 1.
3. ③ Bậc thấp nhất nào đủ giải? 
 (gợi ý: có cách nào đưa từ điển thuật ngữ vào mà không train không? nó hỏng ở đâu?)
4. ④ Nếu fine-tune: cần bao nhiêu dữ liệu, và vì sao khác bài 1? 
 (gợi ý: slide 16 phân biệt hai quy mô — bài này thuộc quy mô nào?)
5. ⑤ Đo bằng gì? 
 (gợi ý: BLEU có phát hiện được một thuật ngữ sai trong một câu dài không?)

#### Đáp án ba bước còn lại

**③ Thử glossary-in-prompt trước, nhưng chuẩn bị sẵn tinh thần fine-tune.** Cách rẻ: đưa từ điển thuật ngữ vào prompt hoặc dùng RAG lấy đúng vài mục liên quan. *Nó hỏng ở đâu:* từ điển chỉ giúp khi model *nhận ra* đây là thuật ngữ cần tra — 
 mà lỗi ở đây chính là model **không nhận ra**, vì "consideration" trông như một từ 
 thông thường. RAG không được kích hoạt vì không có gì báo hiệu cần tra cứu. 
 Đây là ca hiếm hoi mà fine-tune thắng RAG: nó đổi *mặc định* của model trong domain này.

**④ Cần 10k+ mẫu — đây là domain adaptation, không phải style.** Bài 1 chỉ dạy một cái khuôn (lặp lại, vài trăm mẫu là đủ). Bài này dạy cả một vùng ngôn ngữ: 
 hàng nghìn thuật ngữ, mỗi thuật ngữ cần xuất hiện trong đủ ngữ cảnh để model học được khi nào dùng. 
 Nguồn: kho văn bản pháp lý song ngữ đã được dịch chuẩn.

**⑤ BLEU là metric sai ở đây.** Một thuật ngữ sai trong câu 40 từ gần như không làm 
 BLEU nhúc nhích — nhưng nó làm hỏng cả bản dịch về mặt pháp lý. 
 Metric đúng: **độ chính xác thuật ngữ** — lập danh sách 200 thuật ngữ quan trọng, 
 đo tỷ lệ dịch đúng từng cái. Cộng thêm đánh giá của chuyên gia pháp lý trên một mẫu nhỏ.

*Đối chiếu với bài 1:* cùng khung 5 bước, nhưng vì triệu chứng khác nên quy mô dữ liệu 
 khác 20 lần và metric hoàn toàn khác. **Metric sai làm hỏng cả dự án đúng** — 
 đây là bài học lớn hơn cả chuyện chọn rank.

#### SmartCheck AI — có nên fine-tune gì không?

Không có bước nào làm sẵn. Đây là dự án của bạn, và câu trả lời đúng có thể không phải câu bạn muốn nghe.

300 lượt/ngày

Viết ra đủ 5 bước cho *cả ba* quan sát rồi mới mở. Nếu bạn kết luận được và bảo vệ được 
 kết luận đó, bạn đã đạt mức "Đánh giá" của bài học này.

#### Đáp án tham khảo — so với bài của bạn, không thay thế nó

**Quan sát ⑴ — route nhầm intent.** Triệu chứng: sai phân loại, không phải sai giọng. 
 Không phải knowledge gap. **Bậc thấp nhất: few-shot tốt hơn + mô tả nhãn rõ hơn.** Đây đúng là bài học Ngày 20 (slide 16: "sửa mô tả worker trước, đổi model sau"). 
 Nếu vẫn kém sau khi đã đo *intent accuracy* trên tập có nhãn, thì API fine-tune một classifier 
 nhỏ là hợp lý — nhưng chỉ sau khi có số. **Kết luận: chưa fine-tune.**

**Quan sát ⑵ — JSON thiếu trường.** Triệu chứng: sai format. Nghe rất giống bài 1, 
 nên đây là bẫy. **Nhưng có giải pháp rẻ hơn nhiều và chắc chắn hơn nhiều: structured output + 
 Pydantic validation + retry.** `context.md` đã yêu cầu điều này 
 ("Mọi LLM output quan trọng phải có schema/validation"). Fine-tune cho ra format đúng *thường xuyên hơn*; schema validation cho ra format đúng *luôn luôn*, vì cái gì sai thì bị chặn. **Kết luận: không fine-tune — dùng ràng buộc cứng, không dùng xác suất.**

**Quan sát ⑶ — chi phí cao.** Đây là lý do chính đáng thứ ba của slide 5 
 ("giảm cost at scale"). Chạy cổng 3 của cây quyết định: **300 lượt/ngày**. 
 Ngưỡng hoà vốn thấp nhất mà [máy tính ROI](#m-roi) cho ra — khi thay một model frontier — 
 là khoảng **7.400 request/ngày**. Bạn đang ở mức thấp hơn **25 lần**. **Kết luận: self-host fine-tune lỗ nặng.** Cách giảm cost đúng cho quy mô này là 
 routing model rẻ/đắt theo intent (Ngày 20, slide 13) và cắt prompt, không phải fine-tune.

**Kết luận tổng: SmartCheck AI không nên fine-tune gì cả** — và điều đó *xác nhận* thiết kế hiện tại chứ không phủ định nó. Kiến thức toà nhà nằm ở RAG (đúng ADR-03), 
 format nằm ở schema validation (đúng nguyên tắc "LLM không trực tiếp thực hiện business transaction"), 
 chi phí giải bằng routing.

**Vậy làm Lab 21 trên dữ liệu gì?** `context.md` nhắc bạn có một project 
 healthcare/SOAP Note khác domain. **SOAP note là ứng viên fine-tune gần như hoàn hảo:** format cứng (S/O/A/P đúng thứ tự, đúng mục), thuật ngữ lâm sàng dày đặc, và output phải nhất quán 
 tuyệt đối. Nó thoả cả lý do 1 và 2 của slide 5. Dùng nó cho Lab 21 sẽ cho ra một báo cáo *có ý nghĩa* thay vì một bài tập chạy cho xong.

**Và đây là bullet CV mạnh hơn:** *"Đánh giá fine-tuning cho hệ check-in kiosk bằng 
 phân tích ROI có định lượng; xác định ngưỡng hoà vốn cao hơn volume thực tế 25 lần và chọn 
 routing + schema validation thay thế, tiết kiệm toàn bộ chi phí hạ tầng GPU."* Nhà tuyển dụng gặp rất nhiều người fine-tune được. Họ gặp rất ít người **biết khi nào không nên**.

---

<!-- chiron-source-span: {"source_span_id":"aedacae2-62c3-5e9e-b3a1-3e34813c783e","locator":{"kind":"html_section","section_id":"misc","order":10,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"track-3-day-21.html"},"checksum":"364431f6e0ba34eb94dd72c9f7cb0547e076b9b41f57005e3f05a44f96800233"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Mỗi thẻ: niềm tin phổ biến, lý do nó thuyết phục, thực tế, và chỗ tự kiểm chứng 
 ngay trong trang này. Đây là vùng quiz khai thác nhiều nhất.

*Vì sao nghe hợp lý:* "training on our data" nghe hiển nhiên là cách làm model biết dữ liệu đó. 
 Cụm từ "train on your data" trong quảng cáo sản phẩm càng củng cố cảm giác này.

Fine-tuning dạy **phân phối**, không dạy **sự kiện**. Model học "câu trả lời 
 trong domain này trông như thế nào" — giọng, cấu trúc, thuật ngữ — chứ không tạo ra một chỗ để tra cứu. 
 Sự kiện học qua trọng số thì mờ, không kiểm chứng được, không có citation, và không sửa được 
 khi dữ liệu đổi.

[Slide 5](#s5) nói thẳng câu này · Phép thử một câu: *dữ liệu đổi thì có phải train lại không?* Có → đó là knowledge → dùng RAG.

*Vì sao nghe hợp lý:* nhiều tham số hơn = nhiều năng lực hơn = tốt hơn. 
 Và slide 11 ghi r=64 là "near full FT", nghe như đích đến.

Trên dataset nhỏ (500–2k mẫu — đúng quy mô slide 16 khuyến nghị), rank cao **dễ overfit hơn**: 
 nhiều năng lực hơn để *ghi nhớ* dữ liệu train thay vì học quy luật. Và rank gần như **không ảnh hưởng VRAM** — nên "giảm rank" bị slide 18 xếp *cuối cùng* trong quy trình chống OOM.

[Đếm tham số](#m-lora): r=16→64 chỉ thêm ~1,4 GB optimizer trên tổng ~10 GB · [Slide 27](#s27) hỏi thẳng "khi nào tăng rank không còn cải thiện?" — vì câu trả lời thường là "sớm hơn bạn nghĩ".

*Vì sao nghe hợp lý:* rank là con số nổi bật, có mặt trong mọi tutorial, và dễ vặn. `target_modules` là một danh sách chuỗi trông như boilerplate.

Đổi từ `q_proj+v_proj` sang toàn bộ attention + MLP làm tham số train tăng **~8 lần** ở cùng rank — nhiều hơn cả nhân tư rank. Ba layer MLP chiếm khoảng **ba phần tư** tổng tham số adapter, vì chiều intermediate lớn hơn hidden nhiều lần.

[Đếm tham số](#m-lora): Qwen 7B r=16 — q+v cho 5,0M, toàn bộ cho 40,4M · [Slide 10](#s10): "q_proj + v_proj alone thiếu capacity".

*Vì sao nghe hợp lý:* đúng với pretraining, và đúng với hầu hết machine learning cổ điển. 
 Bản năng "gom thêm data" rất khó cưỡng.

Trong SFT, model **bắt chước từng mẫu** — và không có cơ chế nào để nó biết mẫu nào kém. 
 10k mẫu nhiễu dạy model bắt chước cả cái nhiễu đó một cách nhất quán. Slide 16: **"500 perfect > 10k noisy"**.

*Nhưng chú ý sắc thái:* 500 mẫu chỉ đủ cho **style/format**. 
 Domain adaptation vẫn cần 10k+. Hai con số không mâu thuẫn — chúng nói về hai mục tiêu khác nhau.

[Slide 16](#s16) nêu cả hai quy mô · [Bài 1 vs bài 2](#ladder) trong phần bài tập 
 là đúng hai trường hợp đó.

*Vì sao nghe hợp lý:* slide 14 in nó trong một bảng, cạnh tên GPU cụ thể. 
 Bảng thì trông như sự thật.

Con số VRAM là hàm của **bốn** biến không được ghi trong bảng: batch size, 
 max_seq_length, có bật gradient checkpointing không, và optimizer nào. Đổi seq từ 2048 lên 8192 
 là con số nhân lên nhiều lần. Đây cũng là lý do mọi nguồn trên internet ghi một số khác nhau 
 cho cùng một model.

[Ngân sách VRAM](#m-vram): đổi optimizer sang 8-bit và xem con số full fine-tune 
 tụt từ 124 GB xuống 78 GB — đó chính là giả định ngầm phía sau "~60GB" của slide.

*Vì sao nghe hợp lý:* đường loss đi xuống mượt mà là hình ảnh của thành công trong mọi 
 tutorial ML. Nó cho cảm giác hoàn thành rất mạnh.

Nếu eval set bị rò rỉ từ train set, loss sẽ đẹp *chính xác vì* model đã thấy đáp án — 
 và **không có bất kỳ tín hiệu lỗi nào**. Slide 16 gọi đây là "silent killer". 
 Ngoài ra, perplexity thấp không đảm bảo câu trả lời hữu ích: model có thể học vẹt văn phong 
 trong khi nội dung vẫn sai.

[Đoạn code kiểm tra rò rỉ 30 giây](#s26) ở slide 26 · [Slide 25](#s25) yêu cầu *ba* loại bằng chứng (perplexity + ví dụ định tính + chi phí) 
 chính vì không loại nào một mình đủ tin.

---

<!-- chiron-source-span: {"source_span_id":"31d3ce5a-3423-5fff-95aa-d2fdbd5edbdb","locator":{"kind":"html_section","section_id":"apply","order":11,"heading":"→ Áp dụng vào SmartCheck AI","source_file":"track-3-day-21.html"},"checksum":"5c197a33ac8640df958e238f44a99e46bc5495fe42a88441040ad577a69fac1b"} -->

## → Áp dụng vào SmartCheck AI

Kết luận ngắn gọn: **không fine-tune gì cả** — và đó là kết quả tốt, 
 không phải kết quả đáng tiếc.

### Chạy cây quyết định cho SmartCheck AI

| Cổng | Câu hỏi | SmartCheck AI | Kết luận |
| --- | --- | --- | --- |
| 1 | Few-shot đạt 80%+? | Intent classification trên ~5 nhãn với few-shot — gần như chắc chắn đạt | Dừng ở prompt |
| 2 | Cần knowledge cập nhật? | Chính sách toà nhà, giờ làm việc, quy định gửi xe — đổi theo thời gian | RAG — đúng như ADR-03 đã chọn |
| 3 | Volume > 50k/ngày? | ~300 lượt/ngày — thấp hơn ngưỡng hoà vốn thấp nhất khoảng 25 lần | Self-host lỗ nặng |

"pgvector chỉ cho knowledge — vì RAG phù hợp text semantic retrieval."

knowledge thì dùng RAG, fine-tune không giải được

### Ba "cơ hội fine-tune" và vì sao cả ba đều không nên

| Cơ hội | Nghe hợp lý vì | Giải pháp đúng, rẻ hơn |
| --- | --- | --- |
| Fine-tune Intent Router cho chính xác hơn | Phân loại là bài toán fine-tune kinh điển | Sửa mô tả nhãn + few-shot; đo intent accuracy trước. Nếu vẫn thiếu thì API fine-tune một model nhỏ — không self-host |
| Fine-tune để JSON luôn đúng schema | Đây là "format", đúng loại việc fine-tune giỏi | Structured output + Pydantic validation + retry. Fine-tune cho đúng thường xuyên hơn; validation cho đúng luôn luôn |
| Fine-tune model 7B để cắt chi phí API | Slide 5 nêu "giảm cost at scale" | Routing model rẻ/đắt theo intent (Ngày 20, slide 13) + cắt prompt. Ở 300 lượt/ngày, tiền GPU vượt xa tiền API |

format

tôi có thể biến nó thành ràng buộc cứng thay vì 
 xác suất không?

### Vậy làm Lab 21 trên gì — và câu trả lời phỏng vấn

**Đề xuất: làm Lab 21 trên dataset SOAP note** (project healthcare mà `context.md` nhắc tới), không phải trên SmartCheck AI. Lý do: SOAP note thoả *hai* trong ba lý do chính đáng của slide 5 cùng lúc — format cứng (S/O/A/P đúng thứ tự, 
 đúng mục) và thuật ngữ lâm sàng dày đặc. Đó là ứng viên fine-tune gần như hoàn hảo, 
 nên báo cáo của bạn sẽ có nội dung thật để phân tích.

> Câu trả lời phỏng vấn dựng sẵn 
>  "Tôi có đánh giá fine-tuning cho hệ kiosk và quyết định không dùng. Ba lý do chính đáng để fine-tune là 
>  format, jargon và cost-at-scale. Kiến thức toà nhà là dữ liệu thay đổi thường xuyên nên thuộc về RAG, 
>  không phải trọng số — fine-tune không sửa được knowledge gap. Vấn đề format tôi giải bằng structured 
>  output với Pydantic validation, cho đảm bảo tuyệt đối thay vì xác suất cao. Còn về cost: tôi tính 
>  ngưỡng hoà vốn giữa self-host và API theo giá thật, và ngay cả kịch bản thuận lợi nhất — thay thế một 
>  model frontier — cũng cần khoảng 7.400 request/ngày, trong khi kiosk chạy 300. Tôi giảm chi phí bằng 
>  routing model rẻ/đắt theo intent thay vì mua GPU. Tôi có làm fine-tuning LoRA/QLoRA trên một domain 
>  khác nơi nó thật sự phù hợp, nên quyết định này đến từ việc đã so sánh chứ không phải né tránh."

---

<!-- chiron-source-span: {"source_span_id":"38c882be-f90e-5839-974a-10deb7238c04","locator":{"kind":"html_section","section_id":"numbers","order":12,"heading":"! Các con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"track-3-day-21.html"},"checksum":"008a1747c8531b9369075fc934f8a9374a95f00b5489ac3c2e4bc4e52cf92438"} -->

## ! Các con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài này nhiều số hơn Ngày 20, và phần lớn số đều kèm giả định ngầm. Đây là cách đọc chúng cho đúng.

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| "r=8 → 0.1% params" | 11 | Phụ thuộc hoàn toàn vào target_modules | Với Qwen 7B: q+v cho 0,033%; toàn bộ layer cho 0,27%. Tự tính ở máy tính tham số |
| Full FT 7B ≈ 60GB | 14 | Ngầm giả định optimizer 8-bit | Với AdamW fp32 mặc định thì gấp đôi. Kiểm ở ngân sách VRAM |
| QLoRA 7B ≈ 10GB | 14, 18 | Đúng cho batch 1, seq 2048, FA2 + checkpointing | Đổi bất kỳ biến nào trong bốn biến đó là con số đổi theo |
| QLoRA quality drop 2–5% | 13 | Từ bài báo QLoRA, đo trên benchmark chuẩn | Hiểu là bậc độ lớn ("vài phần trăm"). Trên dataset của bạn phải tự đo |
| FlashAttention 2–4× speedup | 19, 21 | Phụ thuộc phần cứng và độ dài chuỗi — slide 21 đã nêu dải | Ngắn (<512) thì nhỏ; dài (8k+) thì lớn. Đừng trích một con số duy nhất |
| Gradient checkpointing −60% VRAM, +20% time | 17, 18 | Xấp xỉ, phụ thuộc kiến trúc và cài đặt | Dùng để ước lượng đánh đổi, không dùng làm cam kết |
| Unsloth "2× faster, 60% less VRAM" | 22 | Số của nhà cung cấp, không có nguồn độc lập trong slide | Tự đo trên cấu hình của bạn trước khi đưa vào báo cáo |
| "Volume > 50k/day ⇒ ROI dương" | 6 | Chỉ có nghĩa khi nói rõ đang thay API nào | Thay frontier: hoà vốn ~7,4k/ngày. Thay mini: ~124k/ngày. Tự tính ở máy tính ROI |
| Cấu hình Qwen2.5-7B / Llama-3.1-8B trong các mô-đun | — | Cấu hình tham chiếu do tài liệu này dùng, không có trên slide | Đối chiếu config.json thật của model bạn dùng trước khi trích số |

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực tế đã chạy."

---

<!-- chiron-source-span: {"source_span_id":"252d2821-80b3-5900-b55a-dc21f4d3c967","locator":{"kind":"html_section","section_id":"cheat","order":13,"heading":"✓ Cheat sheet ôn thi","source_file":"track-3-day-21.html"},"checksum":"89583554f39e9bf3446fc61e3ae7df68e2361a00bf0fe391d8457a28fea5b55f"} -->

## ✓ Cheat sheet ôn thi

Nén toàn bộ 31 slide xuống một trang.

### Thang leo: prompt → RAG → fine-tune

| Bậc | Giải triệu chứng gì | Không giải được gì | Điều kiện leo lên bậc sau |
| --- | --- | --- | --- |
| Zero-shot prompt | Tác vụ phổ thông | Format riêng, jargon | Chưa thử few-shot thì chưa được leo |
| Few-shot prompt | Format, giọng, ví dụ mẫu | Kiến thức model không có | Đo trên eval set, dưới 80% |
| RAG | Kiến thức — mới, thay đổi, cần citation | Cách nói, format cứng | Đã có RAG mà gap vẫn > 15% |
| API fine-tune | Format + jargon, không cần hạ tầng | Dữ liệu nhạy cảm; custom rank/layers | Volume > 50k/ngày, hoặc dữ liệu không được rời hạ tầng |
| Self-host LoRA/QLoRA | Format + jargon + cost at scale + privacy | Vẫn không sửa knowledge gap | (bậc cao nhất) |

### Ba con số phải nhớ, và bốn giả định đi kèm

| Phương pháp | VRAM 7B (điều kiện chuẩn) | Tham số train | GPU tối thiểu |
| --- | --- | --- | --- |
| Full fine-tune | ~60 GB (với optimizer 8-bit) | 100% | A100 80GB |
| LoRA fp16 | ~28 GB | ~1% | A100 40GB |
| QLoRA 4-bit | ~10 GB | ~1% | RTX 3090 24GB |

max_seq_length

### Checklist trước khi bấm trainer.train()

1. Đã chạy phép thử knowledge chưa? ( dữ liệu đổi thì có phải train lại không? )
2. Đã đo baseline few-shot và có con số gap chưa?
3. Dataset đã khử trùng lặp và kiểm rò rỉ train/val chưa? (kỳ vọng: 0)
4. max_seq_length đã đặt theo p95 của dataset chưa — không phải theo số tròn?
5. target_modules đã bật toàn bộ attention + MLP chưa?
6. packing=True chưa? (2× throughput, miễn phí)
7. FlashAttention đã thật sự active chưa? ( model.config._attn_implementation )
8. Có eval set tách biệt và eval_steps đủ dày để thấy overfitting chưa?
9. Đã chọn và ghi lại 5 prompt before/after trước khi train chưa?
10. batch × grad_accum có nằm trong khoảng 16–64 không?

Fine-tune dạy model NÓI NHƯ THẾ NÀO, không dạy model BIẾT CÁI GÌ.

---

<!-- chiron-source-span: {"source_span_id":"a8101d26-8752-5859-b521-f4b5f30230c8","locator":{"kind":"html_section","section_id":"gloss","order":14,"heading":"A–Z Từ điển thuật ngữ","source_file":"track-3-day-21.html"},"checksum":"0ee4425c26b4889d238ae424939999ebc877f342fbe70e3a8ac29e2fa8590a78"} -->

## A–Z Từ điển thuật ngữ

Bài này dày thuật ngữ hơn Ngày 20. Mỗi mục: một câu tiếng Việt dễ hiểu, rồi chỗ nó xuất hiện.

---

<!-- chiron-source-span: {"source_span_id":"79e2349f-56f2-5d7f-b1ef-c3ba446cbc34","locator":{"kind":"html_section","section_id":"bloom","order":15,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-21.html"},"checksum":"03be6e258901c95c19080e0fde17dadd849dac495fdb8554d6326702b10c9d18"} -->

## ◉ Bạn đang ở mức nào?

Mỗi mức là một *việc làm được*. Quiz kiểm tra mức 2–3; lab kiểm tra mức 3–4; 
 phỏng vấn kiểm tra mức 4–5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể được ba lý do chính đáng để fine-tune, ba con số VRAM của Full/LoRA/QLoRA, và công thức W = W₀ + B·A. | Slide 5 · 14 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao fine-tune không sửa knowledge gap, và vì sao FlashAttention không phải một sự đánh đổi. | Ô kiểm tra chương 1 và 4 |
| 3 · Áp dụng | Cho một triệu chứng mới, chạy hết khung 5 bước và quyết định được prompt / RAG / API FT / self-host FT — kèm quy mô dữ liệu cần thiết. | Bài 1 → 2 → 3, làm đúng thứ tự |
| 4 · Phân tích | Nhìn một cấu hình training của người khác và chỉ ra chỗ lãng phí — max_seq_length quá lớn, thiếu packing, FlashAttention chưa active, target_modules thiếu MLP. | Slide 18 · 22 · Ngân sách VRAM |
| 5 · Đánh giá | Bảo vệ được quyết định không fine-tune bằng phân tích ROI có số — và nói được điều gì sẽ làm bạn đổi ý. | Câu trả lời phỏng vấn dựng sẵn · Máy tính ROI |

có vẻ

có bằng chứng
