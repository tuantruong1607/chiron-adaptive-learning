# Chiron AI — Question Bank B-05 (human-authored)

**Trạng thái:** Candidate for expert review. Không publish, không dùng để chấm learner.
**Phạm vi:** 12 objective, soạn tay theo `docs/QUESTION_AUTHORING_CONTRACT.md`.
**Mục tiêu quota:** hoàn thiện 90 objective sau B-01..B-04 — recall/easy/apply/understand, không thêm analyze/hard.
**Không trùng batch trước:** mọi `source_span_id` chưa được các batch trước dùng.

## Objective questions (12)

### 1. Online vs offline evaluation — single choice
> **Metadata:** `topic=online-offline-eval` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Offline evaluation chạy khi nào và trên dữ liệu gì?

- A. Trước khi deploy, mỗi PR, trên dataset cố định.
- B. Sau deploy, continuous, trên mẫu traffic thật của production.
- C. Chỉ chạy một lần duy nhất khi mới ra mắt sản phẩm.
- D. Chạy song song với online eval trên cùng tập traffic.

**Đáp án:** A. B mô tả đúng online evaluation — chạy sau deploy, liên tục, trên mẫu traffic thật. Offline eval dùng làm CI gate và regression detection trước mỗi lần đổi code, trên một dataset cố định chứ không phải traffic sống.  
**Evidence:** `4cdcb3ba-d32b-55b4-85c9-61388476118f` — *RAGAS, LLM-as-Judge & Guardrails*, slide 10.

### 2. Position bias của judge — scenario diagnosis
> **Metadata:** `topic=judge-position-bias` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một golden eval set (n=100) dùng GPT-4 làm judge so sánh cặp câu trả lời A/B. Cách giảm position bias hiệu quả nhất cho tập golden này là gì?

- A. Đánh giá cả hai chiều (A,B) và (B,A) rồi lấy trung bình điểm.
- B. Cho phép judge trả lời "tie" để giảm buộc phải chọn một bên.
- C. Random hoá thứ tự mỗi lần gọi eval và gộp qua nhiều lần chạy.
- D. Chỉ dùng một chiều cố định (A,B) để tiết kiệm chi phí gọi API.

**Đáp án:** A. C là lựa chọn hợp lý cho continuous monitoring vì rẻ hơn, nhưng với tập golden cố định (n=100) thì swap-and-average loại bỏ hoàn toàn bias dù tốn gấp đôi chi phí — đây là khuyến nghị riêng cho golden eval, không phải cho theo dõi liên tục.  
**Evidence:** `fa9f7207-9516-54a5-8b35-a0087edf243b` — *RAGAS, LLM-as-Judge & Guardrails*, slide 30.

### 3. Prompt injection trực tiếp vs gián tiếp — single choice
> **Metadata:** `topic=prompt-injection-types` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Vì sao indirect prompt injection được coi là nguy hiểm hơn direct injection?

- A. Vì indirect injection dùng payload dài hơn nên khó bị input validator chặn.
- B. Vì indirect injection chỉ xảy ra khi hệ thống không có RAG.
- C. Vì user không thấy được attack, và agent có thể âm thầm rò rỉ dữ liệu.
- D. Vì indirect injection luôn nhắm vào system prompt thay vì dữ liệu.

**Đáp án:** C. Direct injection nằm trong input của chính user nên còn nhìn thấy được; indirect injection nằm trong tài liệu hoặc kết quả tool mà agent retrieve, nên vô hình với user trong khi agent vẫn "obey" theo nội dung độc.  
**Evidence:** `49d90e88-5904-52d0-ab4f-d1408a2f716d` — *RAGAS, LLM-as-Judge & Guardrails*, slide 49.

### 4. OWASP LLM Top 10 — single choice
> **Metadata:** `topic=owasp-llm-top10` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Theo danh sách OWASP LLM Top 10 (2025), "Excessive Agency" thuộc rủi ro nào và mitigation chính là gì?

- A. LLM03 Supply Chain; mitigation là pin phiên bản model và audit vendor.
- B. LLM01 Prompt Injection; mitigation là input filter theo chiều sâu.
- C. LLM09 Misinformation; mitigation là faithfulness check và citation.
- D. LLM06 Excessive Agency; mitigation là giới hạn quyền của tool và thêm HITL.

**Đáp án:** D. A, B, C đều là rủi ro thật trong cùng danh sách OWASP nhưng ứng với mã và mitigation khác — mỗi rủi ro trong bảng có mã và cách chống riêng, không thể hoán đổi.  
**Evidence:** `111e552a-5b8e-59db-80be-4a07024775db` — *RAGAS, LLM-as-Judge & Guardrails*, slide 50.

### 5. Over-filtering trap — scenario diagnosis
> **Metadata:** `topic=over-filtering-trap` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một chatbot có refuse rate vượt 10%, người dùng bắt đầu học cách viết lại câu hỏi để né guardrail. Đây là dấu hiệu của vấn đề gì và hướng fix đúng?

- A. Guardrail đang hoạt động đúng như thiết kế; refuse rate cao là chấp nhận được.
- B. Đây là lỗi của model nền tảng, cần đổi sang model khác để giảm refuse rate.
- C. Cần bổ sung thêm một lớp guardrail nữa để chặn chặt hơn các câu hỏi né tránh.
- D. Topic scope hoặc safety classifier quá nhạy; nên đo refuse rate và target về dưới khoảng 3%.

**Đáp án:** D. A sai vì refuse rate cao gây trải nghiệm tệ và khiến user bỏ sang đối thủ — "guardrail mạnh" không đồng nghĩa "guardrail tốt". C càng làm trầm trọng hơn triệu chứng, ngược hướng cần thiết là đo và siết lại ngưỡng, không phải chặn chặt thêm.  
**Evidence:** `52c04a6e-389c-508a-9962-58fc67a2bd00` — *RAGAS, LLM-as-Judge & Guardrails*, slide 59.

### 6. Giới hạn của single-agent — single choice
> **Metadata:** `topic=single-agent-limits` · `cognitive_level=understand` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Khi một agent phải giữ quá nhiều mục tiêu, tool output và state trong cùng một lần suy luận, giới hạn nào của single-agent đang bộc lộ?

- A. Specialization trade-off — agent ôm nhiều vai thì khó giỏi đều.
- B. Reliability yếu — lỗi ở đầu luồng kéo lệch toàn bộ hệ thống.
- C. Parallelism hạn chế — agent chạy tuần tự nên latency tăng.
- D. Context bottleneck — context window có giới hạn cứng.

**Đáp án:** D. A, B, C đều là giới hạn thật của single-agent nhưng mô tả triệu chứng khác: A là về việc ôm nhiều vai trong prompt, C là về việc chạy tuần tự, B là về lan truyền lỗi. Triệu chứng "giữ quá nhiều thứ trong một lần suy luận" khớp đúng với giới hạn context window.  
**Evidence:** `3c437620-ad5a-54a2-9627-2225c8c75482` — *Multi-Agent & Kết Nối Hệ Thống*, slide 10.

### 7. MCP vs A2A — scenario diagnosis
> **Metadata:** `topic=mcp-vs-a2a-boundary` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một hệ thống cần một agent giao việc cho agent khác, để agent kia tự quyết định cách thực hiện. Nên thiết kế theo giao thức nào?

- A. MCP, vì MCP kết nối agent với mọi loại năng lực bên ngoài.
- B. A2A, vì phía nhận việc có thể tự quyết định, không chỉ thực thi.
- C. MCP, vì MCP có trọng tâm là message contract rõ ràng giữa hai bên.
- D. Cả hai đều tương đương nên chọn giao thức nào cũng được.

**Đáp án:** B. MCP trả lời câu hỏi "agent lấy năng lực ở đâu" — phía tool không có agency, chỉ thực thi. A2A trả lời câu hỏi "agent giao việc cho ai" — phía nhận việc có thể ra quyết định, đúng với yêu cầu của tình huống.  
**Evidence:** `a10a0f77-7957-5e63-a9cf-1115a7207f6b` — *Multi-Agent & Kết Nối Hệ Thống*, slide 43.

### 8. Routing pattern — scenario diagnosis
> **Metadata:** `topic=routing-pattern-cost` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một hệ thống có 70% câu hỏi đơn giản và 30% câu hỏi phức tạp. Routing pattern tiết kiệm chi phí bằng cách nào, và rủi ro chính là gì?

- A. Luôn dùng model lớn cho mọi câu hỏi để đảm bảo chất lượng đồng đều.
- B. Phân loại câu hỏi, gửi easy sang model nhỏ và hard sang model lớn để tối ưu chi phí.
- C. Chia đôi ngẫu nhiên số câu hỏi cho hai model bất kể độ khó thật sự.
- D. Dùng model lớn phân loại rồi vẫn xử lý toàn bộ bằng chính model lớn đó.

**Đáp án:** B. A không tiết kiệm được chi phí — đó chính là vấn đề routing giải quyết. Routing chỉ hiệu quả khi phân loại chính xác; phân loại sai nghĩa là câu hard bị gửi cho model nhỏ, kết quả kém — đây là rủi ro thật được nêu rõ trong bài.  
**Evidence:** `a1828386-30ee-591e-a794-b0b6a4c6123f` — *Multi-Agent Systems*, slide 13.

### 9. Supervisor pattern — single choice
> **Metadata:** `topic=supervisor-hub-spoke` · `cognitive_level=understand` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Trong kiến trúc Supervisor hub-spoke, vai trò của supervisor là gì?

- A. Thực thi trực tiếp mọi tác vụ thay vì các worker chuyên biệt.
- B. Chỉ lưu trữ shared state, không tham gia quyết định điều phối.
- C. Nhận task, decompose, route đến worker phù hợp và aggregate kết quả.
- D. Là một worker có tool riêng giống hệt các worker khác.

**Đáp án:** C. Supervisor là một LLM router — nó không tự làm việc của worker như A, không chỉ lưu state thụ động như B, và không phải một worker ngang hàng như D. Nó quyết định gọi ai, theo thứ tự nào, rồi tổng hợp kết quả.  
**Evidence:** `d411e20a-b17f-557e-a7c8-ab6ffbfd46cc` — *Multi-Agent Systems*, slide 15.

### 10. SFT vs Alignment — single choice
> **Metadata:** `topic=sft-vs-alignment` · `cognitive_level=recall` · `difficulty=easy` · `group=none` · `mutually_exclusive_with=none`

Theo pipeline post-training hiện đại, SFT và alignment (DPO/ORPO) dạy model những gì khác nhau?

- A. SFT dạy model format câu trả lời; alignment dạy model phân biệt tốt/xấu.
- B. SFT dạy model an toàn; alignment dạy model đúng ngữ pháp.
- C. SFT và alignment dạy đúng một thứ, chỉ khác nhau về thuật toán tối ưu.
- D. SFT dạy model phân biệt tốt/xấu; alignment dạy model format câu trả lời.

**Đáp án:** A. D đảo ngược đúng thứ tự thật của pipeline. SFT dạy model "nói gì" theo đúng format, còn alignment dạy model "nói như thế nào" — chọn câu trả lời tốt hơn giữa các lựa chọn khả dĩ.  
**Evidence:** `03808a6f-c5a5-5a34-bcf3-27a56d22d210` — *DPO, ORPO & Alignment*, slide 5.

### 11. Preference data vs demonstration data — single choice
> **Metadata:** `topic=preference-vs-demonstration` · `cognitive_level=understand` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Vì sao preference data (dùng cho DPO) mang tín hiệu thông tin mạnh hơn demonstration data (dùng cho SFT)?

- A. Vì preference data có kích thước lớn hơn demonstration data.
- B. Vì preference data rẻ hơn để thu thập từ người dùng thật.
- C. Vì preference cho biết cái gì KHÔNG nên nói, điều SFT không biểu lộ.
- D. Vì preference data không cần con người gán nhãn như demonstration data.

**Đáp án:** C. SFT chỉ thấy ví dụ "good" nên không biết good hơn bad bao nhiêu; một cặp preference (yw, yl) trực tiếp dạy model margin giữa câu tốt và câu tệ — đây là tín hiệu SFT không thể biểu lộ, không liên quan gì tới kích thước tập dữ liệu hay chi phí thu thập.  
**Evidence:** `917dad4a-eee0-592e-93ea-08343c42cb2c` — *DPO, ORPO & Alignment*, slide 7.

### 12. SimPO vs KTO — scenario diagnosis
> **Metadata:** `topic=simpo-vs-kto` · `cognitive_level=apply` · `difficulty=medium` · `group=none` · `mutually_exclusive_with=none`

Một team chỉ có dữ liệu thumbs-up/thumbs-down từ production logs, không có annotator xếp hạng theo cặp. Phương pháp alignment nào phù hợp hơn?

- A. SimPO, vì nó reference-free nên không cần bất kỳ nhãn nào từ dữ liệu.
- B. KTO, vì nó chỉ cần label good/bad cho từng example, không cần preference pairs.
- C. DPO chuẩn, vì nó luôn cho kết quả tốt hơn cả SimPO lẫn KTO trong mọi trường hợp.
- D. SimPO, vì VRAM hạn chế luôn là ràng buộc quan trọng hơn định dạng nhãn.

**Đáp án:** B. A hiểu sai "reference-free" — SimPO vẫn cần preference pairs, chỉ là không cần policy tham chiếu πref. KTO được thiết kế đúng cho dữ liệu single-signal dạng +1/−1, khớp với tín hiệu thumbs-up/down từ production mà đề bài mô tả.  
**Evidence:** `7503feaa-7285-5cf3-9293-64c730681016` — *DPO, ORPO & Alignment*, slide 20.

## Review checklist

- [ ] Vị trí vật lý đáp án đúng phân bố đều 4 vị trí (script check).
- [ ] Không câu nào có đáp án đúng dài hơn 1.3× option ngắn nhất.
- [ ] Mỗi câu đúng 4 option và đúng 1 đáp án.
- [ ] group/mutually_exclusive đóng kín và đối xứng (script check).
- [ ] Mọi citation resolve trong `source_spans.jsonl` (script check).
- [ ] Đã chạy §2 của `QUESTION_REVIEW_PROTOCOL.md` (đáp án thứ hai, evidence trả lời được stem).
