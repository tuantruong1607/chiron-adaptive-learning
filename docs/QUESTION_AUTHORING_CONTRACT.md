# Chiron AI — Contract sinh câu hỏi (tuân thủ tuyệt đối)

**Trạng thái:** binding · **Phạm vi:** mọi agent/model sinh item cho ngân hàng đề `rag-intensive`.
**Quan hệ với tài liệu khác:** [`QUESTION_BANK_GENERATION_PIPELINE.md`](QUESTION_BANK_GENERATION_PIPELINE.md) định nghĩa kiến trúc, bảng dữ liệu và cổng pipeline. File này định nghĩa **nội dung item phải trông như thế nào**. Sau khi sinh, item được audit theo [`QUESTION_REVIEW_PROTOCOL.md`](QUESTION_REVIEW_PROTOCOL.md). Khi hai file mâu thuẫn, pipeline doc thắng về hạ tầng, file này thắng về authoring.

Contract này được rút ra từ vòng review `data/questions/review/pilot-v1.md`. Mỗi luật dưới đây tương ứng với một defect đã thực sự xảy ra và đã bị bắt trong pilot — không có luật nào là phòng xa.

---

## 0. Luật tối cao

**Agent không tự tuyên bố item đạt.** Item chỉ đạt khi `scripts/validate_question_bank.py` trả exit code 0. Mọi câu "tôi đã kiểm tra và thấy ổn" không có output validator kèm theo đều bị coi là chưa kiểm tra.

```bash
python scripts/validate_question_bank.py data/questions/review/pilot-v1.md
```

Validator phân biệt hai mức. **Defect** chặn cứng, exit 1 — agent phải sửa item, tuyệt đối không sửa validator để item lọt. **WARN** không chặn nhưng bắt buộc người review xác nhận; đó là các luật mà máy không phán được (ví dụ R3.2: span ngắn có thể hợp lệ nếu nó chứa đúng mệnh đề đáp án dựa vào). Agent không được tự đóng một WARN.

**Không bịa `source_span_id`.** ID phải được tra ra từ `data/manifests/source_spans.jsonl`. Nếu không tra được, dừng và báo — tuyệt đối không sinh chuỗi có hình dạng UUID. Trong pilot v1, 30/30 citation ban đầu là ID không tồn tại; đây là defect nghiêm trọng nhất từng gặp và nó phát sinh vì model sinh ID cho *đúng định dạng*.

**Không sinh kiến thức ngoài evidence pack.** Mọi mệnh đề chuyên môn trong stem, option và rationale phải truy được về span đã cấp. Thiếu kiến thức thì tạo content-gap task, không tra web, không dùng trí nhớ nội tại.

---

## 1. Hình dạng bắt buộc của một item objective

```markdown
### <n>. <Chủ đề> — <format>
> **Metadata:** `topic=<slug>` · `cognitive_level=<recall|understand|apply|analyze>` · `difficulty=<easy|medium|hard>` · `group=<slug|none>` · `mutually_exclusive_with=<Qx,Qy|none>`

<stem — không chứa citation, không chứa từ khoá lộ đáp án>

- A. <option>
- B. <option>
- C. <option>
- D. <option>

**Đáp án:** <nhãn>. <rationale nói vì sao distractor sai, không lặp lại đáp án>  
**Evidence:** `<source_span_id>` — *<document title>*, slide <N>.
```

Dòng `**Đáp án:**` phải kết thúc bằng **hai dấu cách** (markdown line break). Nhãn option luôn theo thứ tự A→D từ trên xuống.

---

## 2. Luật distractor

### 2.1 Cấm distractor phi lý

Distractor phải là thứ một learner học nửa vời **thực sự sẽ chọn**. Cấm tuyệt đối các mẫu sau, vốn chiếm quá nửa option của pilot v1 và khiến đề giải được mà không cần biết gì về RAG:

| Cấm | Vì sao |
|---|---|
| "Tắt monitoring", "Xóa log sau mỗi call", "Log secrets để debug" | không ai chọn; chỉ để lấp chỗ |
| "Retry vô hạn", "Tăng context vô hạn" | phi lý về mặt kỹ thuật |
| "Chỉ cần sinh ảnh", "Rút ngắn mọi tài liệu thành một token" | lạc đề hoàn toàn |
| "Tăng temperature" khi câu hỏi về retrieval | dùng làm distractor mặc định cho mọi câu |

### 2.2 Mỗi câu phải có ít nhất một distractor "đúng kỹ thuật, sai bài toán"

Distractor mạnh nhất là một kỹ thuật **có thật, được dạy trong khoá, hợp lý ở tình huống khác**, nhưng không giải quyết đúng thứ stem đang hỏi. Ví dụ đã dùng trong pilot:

- Câu về chunking mất mạch ngữ nghĩa → distractor "thêm cross-encoder rerank trên top-100" (rerank chỉ xếp lại candidate đã lấy).
- Câu về dense miss token hiếm → distractor "tăng `top_k` lên 100 rồi rerank" (đoạn đúng chưa từng vào top-100).
- Câu RAGAS recall thấp/faithfulness cao → distractor "tighten prompt + hạ temperature" (đó là thuốc cho faithfulness, đang cao sẵn).
- Câu circuit breaker → distractor "tăng backoff kèm jitter" (vẫn để request đi tới provider hỏng).

### 2.3 Ưu tiên misconception mà slide gọi đích danh

Khi evidence pack có câu dạng "nhiều người tưởng X, thực ra Y", **X phải trở thành distractor**. Đây là distractor chất lượng cao nhất vì nó được chứng thực bởi chính người dạy. Ví dụ trong corpus:

- Slide answer relevancy: "Common misunderstanding: đo cosine similarity giữa Q và A. Sai!" → distractor.
- Slide idempotency: "LLM không sinh lại tham số y hệt → hash nội dung thô sẽ trượt" → distractor "hash toàn bộ tham số tool call".
- Slide `interrupt()`: "`interrupt_before` không recommended cho HITL, chỉ để debug" → distractor.
- Slide SLI/SLO: SLA là khái niệm thứ tư → distractor "SLO là cam kết hợp đồng, vi phạm thì bồi thường".
- Slide semantic cache: "95% là marketing, thực tế 30–68%" → distractor.

### 2.4 Cấm cue hình thức

- **Độ dài:** trong một câu, option dài nhất không quá **1.3×** option ngắn nhất, tính trên các option dài ≥25 ký tự. Đáp án đúng không được là option dài nhất một cách hệ thống. Pilot v1 trước khi sửa: 26/28 câu đáp án đúng là option dài nhất — tự nó đủ để đoán ~80% đề.
- **Vị trí:** phân bố vị trí vật lý của đáp án đúng phải đều trên 4 vị trí (lệch tối đa ±2 giữa vị trí nhiều nhất và ít nhất trên mỗi 30 câu). **Không đủ nếu chỉ đổi nhãn chữ cái** — phải hoán vị chính dòng option. Pilot v1 từng có phân bố nhãn hoàn hảo A/B/C/D nhưng đáp án đúng vẫn nằm ở dòng đầu trong 25/28 câu.
- **Giọng văn:** không để đáp án đúng là option duy nhất viết giọng "production-ready" với nhiều mệnh đề nối bằng dấu phẩy.
- **Số option:** mọi item objective có đúng 4 option và đúng 1 đáp án. Form đề không dùng multi-select; item nào có 2 đáp án trở lên đều bị validator chặn.

---

## 3. Luật evidence

1. Mỗi item trỏ tới span **có nội dung thật**. Cấm trỏ tới slide mục lục, slide bìa mục, slide "Mục tiêu bài học", slide "Agenda", slide "Hỏi & Đáp", slide "Cảm ơn".
2. Span phải dài **≥260 ký tự**, trừ khi span ngắn đó chứa nguyên văn mệnh đề mà đáp án dựa vào (ví dụ slide phân biệt log vs trace dài 153 ký tự vẫn dùng được vì đó chính là điểm phân biệt).
3. Nội dung span phải **thực sự trả lời được stem**. Kiểm bằng cách đọc riêng span đó và tự trả lời câu hỏi; nếu không trả lời được thì span sai, dù title và số slide trông hợp lý. Pilot v1 từng có câu "answer relevancy" trỏ tới slide Recall@k/MRR/nDCG.
4. Citation ghi dạng `` `<uuid>` — *<title>*, slide <N> `` để người review mở lại được, và để `remap_question_citations.py` tái tạo được UUID khi corpus regenerate.

---

## 4. Luật chống rò rỉ giữa các câu

Rò rỉ xảy ra khi câu A tiết lộ đáp án câu B trong cùng một đề. Hai dạng đã gặp:

**Dạng 1 — chung bộ option.** Q10–Q13 cùng dùng bốn metric RAGAS làm option. Bất kỳ hai câu nào đứng cạnh nhau đều thu hẹp lựa chọn cho nhau.
→ Gán chung `group=<slug>`. Form assembler lấy **tối đa 1 câu mỗi group**.

**Dạng 2 — option của câu này định nghĩa đáp án câu kia.** Q24 có distractor "Episodic memory lưu tuple (task, trajectory, outcome, reflection)" — chính là đáp án Q25.
→ Cũng gán chung `group`. Dạng này **không tự phát hiện được bằng token overlap** vì cách diễn đạt khác nhau; agent phải chủ động rà và khai báo.

**Luật:** khi viết một câu mới, đọc option của mọi câu cùng `topic` gần nghĩa. Nếu một option của câu mới *nêu định nghĩa* của đáp án câu cũ (hoặc ngược lại), gán chung group. `mutually_exclusive_with` chỉ dùng cho cặp lẻ và **phải đối xứng hai chiều**.

---

## 5. Luật metadata

`cognitive_level` mô tả thao tác tư duy **thực tế** để trả lời, không phải độ khó cảm tính:

| Level | Dấu hiệu | Ví dụ |
|---|---|---|
| `recall` | gọi lại một thuật ngữ/con số/định nghĩa đơn lẻ đúng nguyên văn slide, không cần so sánh hay tình huống | "HNSW là viết tắt của gì?" |
| `understand` | hỏi định nghĩa, phân biệt khái niệm, "phát biểu nào đúng", "khác nhau ở điểm nào" | "Semantic cache khác exact cache ở điểm nào?" |
| `apply` | có tình huống cụ thể, chọn kỹ thuật phù hợp với ràng buộc đã cho | "Dense trả đúng đoạn giải thích, BM25 trả đúng API name, chọn gì?" |
| `analyze` | phải chẩn đoán nguyên nhân từ triệu chứng, hoặc loại trừ giữa nhiều can thiệp đều hợp lý | "RAGAS recall thấp, faithfulness cao — ưu tiên debug nào?" |

Cảnh báo thường gặp: câu bắt đầu bằng "Lợi ích chính của X là gì" hoặc "Phát biểu đúng nhất là gì" **luôn là `understand`**, kể cả khi distractor rất tinh vi. Distractor hay không nâng được cognitive level.

Các câu cùng cấu trúc phải cùng nhãn. Bốn câu "tình huống → chọn metric" không thể một câu `analyze/hard` còn ba câu `apply/medium`.

---

## 6. Luật câu tự luận

1. Mỗi tiêu chí rubric có anchor **0/1/2** tường minh: 0 = vắng mặt hoặc sai; 1 = nêu đúng khái niệm nhưng thiếu cơ chế/điều kiện/verification; 2 = thiết kế cụ thể, đúng ràng buộc tình huống, nêu được cách kiểm chứng hoặc trade-off.
2. Bắt buộc có câu: giải pháp thay thế đạt cùng thuộc tính được đủ điểm (saga/outbox thay checkpoint, token bucket thay circuit breaker). Không có câu này thì rubric liệt-kê-thành-phần sẽ trừ oan học viên giỏi.
3. Câu yêu cầu code/pseudocode phải có **test hành vi**, không chấm bằng rubric văn xuôi. Mỗi test nêu input và hành vi bắt buộc quan sát được.
4. Tự luận cũng mang dòng `Metadata:` như objective.

---

## 7. Ngân sách thời lượng

Objective ~1.5 phút/câu. Tự luận system design ~15 phút/câu. Đề 30 objective + 6 tự luận = ~135 phút, làm tròn 120 phút chỉ hợp lệ nếu đề ghi rõ đáp án mong đợi là bullet list. Không đặt thời lượng bằng cảm tính.

---

## 8. Quy trình bắt buộc mỗi lần sinh

```
1. Nhận item spec + evidence pack (không tự chọn evidence)
2. Đọc TOÀN VĂN từng span; span nào không trả lời được stem thì trả lại spec, không viết bừa
3. Viết stem → đáp án → rationale
4. Viết distractor: >=1 "đúng kỹ thuật sai bài toán", ưu tiên misconception slide gọi tên
5. Cân độ dài option, hoán vị vị trí dòng
6. Rà group/mutually_exclusive với các câu cùng topic
7. Chạy scripts/validate_question_bank.py
8. Fail -> quay lại bước tương ứng. KHÔNG nộp kèm lời giải thích thay cho việc sửa.
```

---

## 9. Những điều tuyệt đối không làm

- Không sinh `source_span_id` mà không tra manifest.
- Không tuyên bố đạt khi chưa có output validator exit 0.
- Không "shuffle" bằng cách đổi nhãn chữ cái mà giữ nguyên thứ tự dòng.
- Không dùng slide mục lục/bìa mục/agenda làm evidence.
- Không nâng `cognitive_level` vì distractor khó.
- Không viết distractor phi lý để lấp cho đủ 4 option.
- Không sửa validator để item pass; sửa item.
