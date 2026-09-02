# Chiron AI — Protocol review ngân hàng đề (quest-review)

**Trạng thái:** binding · **Phạm vi:** agent review item đã sinh, trước khi vào reviewed pool.
**Đọc trước:** [`QUESTION_AUTHORING_CONTRACT.md`](QUESTION_AUTHORING_CONTRACT.md) — file này không lặp lại luật authoring, nó nói **cách kiểm rằng luật đã được tuân thủ**.

Agent review **không sửa item**. Nó ra phán quyết và nêu bằng chứng. Sửa là việc của vòng sinh lại hoặc của người viết.

---

## 0. Luật tối cao của người review

**Chạy validator trước, luôn luôn.** Mọi luật cơ học đã được máy kiểm; review bằng mắt những thứ đó là lãng phí và không đáng tin hơn.

```bash
python scripts/validate_question_bank.py <file.md>
```

Validator FAIL → **dừng, trả về vòng sinh lại**. Không review nội dung của một batch chưa qua cổng cơ học.

**Không tin nhãn, chỉ tin nội dung.** Item ghi `cognitive_level=analyze` không có nghĩa nó là analyze. Evidence ghi `slide 22` không có nghĩa slide 22 nói điều đó. Mọi phán quyết phải dựa trên văn bản đã đọc, không dựa trên metadata tự khai.

**Không tự đóng WARN.** Validator phát WARN nghĩa là máy không phán được; agent review phải đọc và kết luận, ghi rõ kết luận đó vào report.

---

## 1. Phân công: máy kiểm gì, người review kiểm gì

| Luật | Ai kiểm | Ghi chú |
|---|---|---|
| R0 span tồn tại · R1 hình dạng · R2.4 cue độ dài/vị trí · R3.1 slide điều hướng · R3.4 định dạng citation · R4 đối xứng group · R5 metadata đủ trường | **validator** | không review tay |
| R3.2 span mỏng | validator phát WARN → **agent quyết** | đọc span, xem có chứa đúng mệnh đề đáp án dựa vào không |
| R2.1 distractor phi lý · R2.2 distractor "đúng kỹ thuật sai bài toán" · R2.3 misconception · R3.3 span trả lời được stem · R4 rò rỉ dạng 2 · R5 nhãn đúng mức tư duy | **agent review** | phần còn lại của tài liệu này |
| Đáp án thứ hai cũng đúng | **agent review** | §2.1, defect nguy hiểm nhất, không validator nào bắt được |

---

## 2. Sáu phép kiểm ngữ nghĩa

Làm theo đúng thứ tự. Phép 2.1 và 2.2 là chặn cứng; bốn phép còn lại phân loại revise.

### 2.1 Kiểm đáp án thứ hai — CHẶN CỨNG

Đọc từng distractor và tự hỏi: **"có tình huống hợp lý nào khiến option này cũng đúng không?"** Nếu có, item hỏng, kể cả khi đáp án được đánh dấu "đúng hơn".

Dấu hiệu:
- Distractor là một kỹ thuật thật giải quyết **cùng vấn đề** bằng đường khác (multi-query vs graph traversal cho multi-hop; cross-encoder rerank trên union vs RRF cho fusion không phụ thuộc thang score).
- Stem thiếu ràng buộc để loại distractor đó. Cách sửa thường là **siết stem**, không phải đổi distractor.
- Rationale phải viện tới ngoài evidence mới loại được distractor.

Ghi rõ: distractor nào, tình huống nào làm nó đúng, stem thiếu ràng buộc gì.

### 2.2 Kiểm evidence trả lời được stem — CHẶN CỨNG

Với mỗi item: **đọc riêng span, che stem đi, rồi tự trả lời câu hỏi chỉ bằng span đó.**

- Trả lời được → pass.
- Không trả lời được → **reject**, dù title và số slide trông hợp lý.

Đây là defect từng lọt qua nhiều vòng trong pilot v1: câu "answer relevancy" trỏ slide Recall@k/MRR/nDCG. Title đúng deck, số slide tồn tại, ID resolve — chỉ nội dung là sai.

Khi item cite nhiều span, mỗi mệnh đề trong rationale phải map được về ít nhất một span.

### 2.3 Kiểm chất lượng distractor

Cho mỗi item, đếm:

- Số distractor **phi lý** (không ai chọn: "tắt monitoring", "log secrets để debug", "retry vô hạn"). Có ≥1 → revise.
- Số distractor **"đúng kỹ thuật, sai bài toán"**. Có 0 → revise. Đây là luật R2.2, và là khác biệt giữa câu đo kiến thức với câu đo khả năng nhận diện văn phong.
- Distractor có bám **misconception mà slide gọi đích danh** không (R2.3). Nếu evidence pack chứa câu dạng "nhiều người tưởng X, thực ra Y" mà X không xuất hiện trong option → revise, item đang bỏ phí distractor tốt nhất có sẵn.

### 2.4 Kiểm cognitive_level

Đọc stem, tự hỏi **thao tác tư duy thực tế** để trả lời là gì, rồi đối chiếu nhãn:

| Nhãn | Chỉ đúng khi |
|---|---|
| `understand` | hỏi định nghĩa, phân biệt khái niệm, "phát biểu nào đúng", "khác nhau ở điểm nào" |
| `apply` | có tình huống cụ thể, chọn kỹ thuật hợp với ràng buộc đã cho |
| `analyze` | phải chẩn đoán nguyên nhân từ triệu chứng, hoặc loại trừ giữa nhiều can thiệp đều hợp lý |

Bẫy thường gặp: **distractor tinh vi không nâng được cognitive level**. Câu "Lợi ích chính của X là gì" hoặc "Phát biểu đúng nhất là gì" luôn là `understand` dù ba distractor đều sắc.

Kiểm thêm tính nhất quán: các item **cùng cấu trúc stem** phải cùng nhãn. Bốn câu "tình huống → chọn metric" không thể một câu `analyze/hard` còn ba câu `apply/medium`.

### 2.5 Kiểm rò rỉ dạng 2

Validator chỉ bắt được rò rỉ khi option trùng từ vựng. Dạng nguy hiểm hơn là **option của câu này nêu định nghĩa của đáp án câu kia**, diễn đạt khác nhau nên token overlap không thấy.

Cách làm: nhóm item theo `topic` gần nghĩa, đọc **toàn bộ option** của cả nhóm cùng lúc. Với mỗi option, hỏi: "câu nào khác trong nhóm có đáp án đúng là chính điều này?"

Ví dụ đã gặp: Q24 có distractor "Episodic memory lưu tuple (task, trajectory, outcome, reflection)" — chính là đáp án Q25; Q25 có distractor định nghĩa semantic memory — chính là đáp án Q26.

Tìm thấy → yêu cầu gán chung `group`, không yêu cầu xoá item.

### 2.6 Kiểm rationale

Rationale phải nói **vì sao distractor sai**, không lặp lại đáp án. Rationale chỉ diễn giải lại option đúng là dấu hiệu item được sinh mà không thực sự cân nhắc distractor — cờ để soi kỹ item đó bằng phép 2.1.

Rationale nhắc tới nhãn chữ cái phải khớp thứ tự option hiện tại. Sau mỗi lần hoán vị vị trí, nhãn trong rationale rất dễ lệch.

---

## 3. Kiểm cue hình thức mà validator chưa bao

Validator đo độ dài và vị trí. Hai cue còn lại phải đọc:

**Giọng văn.** Đáp án đúng không được là option duy nhất viết giọng "production-ready" với nhiều mệnh đề nối bằng dấu phẩy, trong khi ba distractor đều là câu đơn cụt.

**Độ cụ thể.** Đáp án đúng không được là option duy nhất có con số, tên tham số hoặc tên công cụ cụ thể. Learner sẽ học cách chọn option chi tiết nhất thay vì option đúng.

**Closed-book solve check.** Với batch lớn, đưa stem + option (không kèm evidence, không kèm rationale) cho một model độc lập với model đã sinh. Model chọn đúng vượt rõ mức ngẫu nhiên nghĩa là đề đang giải được bằng hình thức. Đây là tín hiệu ở **mức batch**, không dùng để phán quyết một item lẻ.

---

## 4. Lấy mẫu khi review số lượng lớn

Batch B sinh 720 objective candidate. Không đọc sâu hết được, và đọc lướt toàn bộ tệ hơn đọc kỹ một mẫu.

**Census — đọc 100%:**
- Toàn bộ item tự luận.
- Toàn bộ item `difficulty=hard` hoặc `cognitive_level=analyze`.
- Toàn bộ item thuộc topic security, tenant isolation, guardrail, HITL, monitoring.
- Toàn bộ item có evidence multi-hop hoặc validator phát WARN.
- Toàn bộ item trong một `group` nếu bất kỳ item nào của group đó fail.

**Mẫu phân tầng — phần còn lại:** tối thiểu 20% mỗi ô `(topic × cognitive_level × difficulty)`, tối thiểu 3 item mỗi ô. Lấy mẫu bằng seed cố định, ghi seed vào report để tái lập.

**Luật lan:** trong một ô, nếu tỷ lệ defect của mẫu vượt **20%**, ô đó bị **reject toàn bộ** và sinh lại — không review nốt phần còn lại từng câu. Defect ở mật độ đó là lỗi prompt/spec, không phải lỗi item lẻ.

---

## 5. Phán quyết

Mỗi item nhận đúng một trạng thái:

| Trạng thái | Khi nào | Đi đâu |
|---|---|---|
| `accept` | qua validator, qua cả sáu phép §2 | reviewed pool |
| `revise` | defect sửa được mà không đổi đáp án: distractor yếu, nhãn sai, rationale lệch, thiếu group | trả về kèm chỉ dẫn cụ thể |
| `reject` | fail §2.1 (đáp án thứ hai) hoặc §2.2 (evidence không trả lời được stem) | sinh lại từ spec |
| `escalate` | agent review không tự quyết được về mặt chuyên môn | người review |

Không có trạng thái "accept có điều kiện". Không tự sửa rồi accept.

---

## 6. Định dạng report

```markdown
## Review batch <id>

**Validator:** exit <0|1> · <n> defect · <n> WARN
**Phạm vi:** census <n> item · mẫu <n>/<N> item, seed <seed>

### Tổng hợp
| Trạng thái | Số item |
|---|---|
| accept | n |
| revise | n |
| reject | n |
| escalate | n |

### Ô vượt ngưỡng 20% (reject toàn ô)
- <topic × level × difficulty>: <n>/<n> defect — <nguyên nhân chung>

### Item cần xử lý
#### <item_id> — reject — §2.1 đáp án thứ hai
Distractor <nhãn> "<trích>" cũng đúng khi <tình huống>. Stem thiếu ràng buộc <gì>.

#### <item_id> — revise — §2.3 distractor
<n>/3 distractor phi lý: "<trích>". Không có distractor "đúng kỹ thuật sai bài toán".
Evidence có misconception chưa dùng: "<trích slide>".

### WARN đã xử lý
- <item_id> R3.2 span 153 ký tự: <chấp nhận|reject> vì <lý do>.
```

Mỗi phán quyết `reject`/`revise` phải có **trích dẫn nguyên văn** phần gây lỗi. Phán quyết không có trích dẫn bị coi là chưa review.

---

## 7. Những điều tuyệt đối không làm

- Không review nội dung khi validator còn FAIL.
- Không sửa item rồi accept chính item mình vừa sửa.
- Không dùng cùng một model vừa sinh vừa review batch đó.
- Không tin `cognitive_level`, `difficulty`, `group` do vòng sinh tự khai — kiểm lại bằng nội dung.
- Không tự đóng WARN mà không ghi kết luận.
- Không accept item mà mình không đọc được evidence span.
- Không nới ngưỡng 20% để cứu một ô sắp bị reject.
