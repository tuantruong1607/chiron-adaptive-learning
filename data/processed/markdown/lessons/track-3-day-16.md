---
schema_version: 1
course_id: rag-intensive
document_id: "4de26bb0-32aa-5db0-8b94-87868ea1d34d"
document_version_id: "f78c9573-8379-5df5-aec6-0319473f3b0a"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Self-Improving Agents — Reflexion, LATS & Voyager"
source_file: "track-3-day-16.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-16.html"
source_sha256: "cdeea6db87666dd6d12c76398c6c4c485595d373de8e3e8966915c51ffa4f846"
parser_version: chiron-structured-markdown-v1
html_section_count: 18
interactive_module_count: 3
interactive_control_count: 12
language: vi
---

# Self-Improving Agents — Reflexion, LATS & Voyager

> Phân biệt retry mù với phản tư có bằng chứng, và biết khi nào chi phí search mang lại giá trị.

<!-- chiron-source-span: {"source_span_id":"8cca4475-4c59-5a64-83c0-68b5800b0297","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc bài này như một kỹ sư production","source_file":"track-3-day-16.html"},"checksum":"786ac029a37d444697c8d9001d8c6662873563efb01e76e7443a317f2d41d6bd"} -->

### Đọc bài này như một kỹ sư production

Bài học được tổ chức theo một chuỗi quyết định thay vì danh sách công cụ. Trước hết xác định ràng buộc và failure mode; tiếp theo chọn cơ chế; cuối cùng buộc cơ chế tạo ra evidence có thể đo, audit và rollback. Mental model này giúp phân biệt ‘agent chạy được’ với ‘hệ thống vận hành được’.

Trục ôn thi là giải thích tại sao: retry mù lặp lại cùng policy nên thường lặp lại cùng lỗi. Khi trả lời tự luận, luôn đi theo cấu trúc context → decision → trade-off → evidence → residual risk.

Chu trình 45–60 phút ① Scan mental model và ba hình. ② Đọc trích slide trước diễn giải. ③ Dừng ở câu tự kiểm. ④ Làm mô-đun theo Predict–Observe–Explain. ⑤ Chốt bằng case study và Bloom.

---

<!-- chiron-source-span: {"source_span_id":"f7450053-3339-5ba7-b3c9-7e305f499008","locator":{"kind":"html_section","section_id":"section-002","order":2,"heading":"◎ Bản đồ tư duy trước khi học","source_file":"track-3-day-16.html"},"checksum":"18b308db74b8a7c3302189bfe8a94daacafce28993edfeb4e0d2ad3375919b5d"} -->

## ◎ Bản đồ tư duy trước khi học

Ba hình dưới đây là khung nối kiến thức với quyết định vận hành; chúng không thay thế nội dung slide.

| Tín hiệu đầu vào | Cơ chế quyết định | Đầu ra cần kiểm |
| --- | --- | --- |
| Yêu cầu, state, ràng buộc | Chuẩn hóa → đánh giá → route | Kết quả + evidence + telemetry |
| Failure hoặc uncertainty | Retry có giới hạn / escalation | Trạng thái bền vững, không nhân đôi tác dụng phụ |

Hình 1 — Mental model production: dữ liệu đi qua quyết định có kiểm soát, không đi thẳng vào model.

| Lớp | Câu hỏi phải trả lời | Failure mode nếu bỏ qua |
| --- | --- | --- |
| Quality | Đầu ra có đúng và grounded? | Demo đẹp nhưng sai ngầm |
| Reliability | Restart, timeout, retry có an toàn? | Mất state hoặc tác dụng phụ trùng |
| Economics | Latency và chi phí ở p95 là bao nhiêu? | Pilot được nhưng không scale |
| Governance | Ai có quyền làm gì, audit ở đâu? | Không thể vận hành có trách nhiệm |

Hình 2 — Bốn lăng kính dùng để đọc mọi quyết định trong bài.

| Mức bằng chứng | Dùng để làm gì | Không được suy diễn |
| --- | --- | --- |
| Trích slide | Nhắc lại định nghĩa và con số | Không biến ví dụ thành benchmark chung |
| Phép tính mô-đun | Phân tích độ nhạy của giả định | Không gọi là số đo production |
| Telemetry thực | Ra quyết định deploy/rollback | Không thay thế đánh giá nhân quả |

Hình 3 — Tách nguồn slide, mô hình tính và dữ liệu vận hành để không tạo “độ chính xác giả”.

---

<!-- chiron-source-span: {"source_span_id":"8ecaf798-76f6-5074-9668-33e58877b21d","locator":{"kind":"html_section","section_id":"c0","order":3,"heading":"01 Từ retry đến self-improvement","source_file":"track-3-day-16.html"},"checksum":"cdc211b751dd5ff66caadbb64b61219ba4cc6ad2ac112b3e545ee2898c5f4fef"} -->

## 01 Từ retry đến self-improvement

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 1 Từ retry đến self-improvement · Mental model & quyết định

> Trích slide Slide 1: VinUniversity Advanced Agent Architectures AICB-P2T3 · Ngày 16 · Chương 4 — Agent Nâng Cao Giảng viên VinUniversity · Phase2·Track3·Tuần4

VinUniversity Advanced Agent Architectures AICB-P2T3 · Ngày 16 · Chương 4 — Agent Nâng Cao. Điểm nối sang production là: retry mù lặp lại cùng policy nên thường lặp lại cùng lỗi. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Hook Tại sao Reflexion agent giải quyết được bài toán mà ReAct không làm được?
- Hômnaytasẽtrảlờicâuhỏinàybằngbenchmark,patternvà democode.
- 2 Reflexion: thêmself-evaluationvàoloop 3 LATS,Voyagervàdecisionmatrix 4 Kỹthuậtnângcaotrướckhivàolab 5 Demo+lab+auto-grading AICB·Ngày16 2

#### Tự kiểm tra · Với từ retry đến self-improvement, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là retry mù lặp lại cùng policy nên thường lặp lại cùng lỗi.

### Slide 3 Từ retry đến self-improvement · Evidence & failure lens

> Trích slide Slide 3: Agenda 1 Khinàosingle-agentthấtbại? 2 Reflexion: thêmself-evaluationvàoloop 3 LATS,Voyagervàdecisionmatrix 4 Kỹthuậtnângcaotrướckhivàolab 5 Demo+lab+auto-grading AICB·Ngày16 2

**Đọc như kỹ sư:** 2 Reflexion: thêmself-evaluationvàoloop 3 LATS,Voyagervàdecisionmatrix 4 Kỹthuậtnângcaotrướckhivàolab 5 Demo+lab+auto-grading AICB·Ngày16 2

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 3 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 5 Từ retry đến self-improvement · Evidence & failure lens

> Trích slide Slide 5: ReAct — Reasoning + Acting Thought Action Observation suyluận gọitool kếtquả Lặp đến khi có câu trả lời • Xenkẽ Reasoning(suynghĩ)+ Acting(hànhđộng) • Agenttựquyếtđịnh: gọitoolnào, khinàodừng • ĐãhọcởGĐ1—nềntảngcho mọiagentpattern Nhắc lại ReAct = “Think before you act” — mỗibướcagentgiảithíchlýdotrước khihànhđộng AICB·Ngày16 4

**Đọc như kỹ sư:** ReAct — Reasoning + Acting Thought Action Observation suyluận gọitool kếtquả Lặp đến khi có câu trả lời • Xenkẽ Reasoning(suynghĩ)+ Acting(hànhđộng) • Agenttựquyếtđịnh: gọitoolnào, khinàodừng • ĐãhọcởGĐ1—nềntảngcho mọiagentpattern Nhắc lại ReAct = “Think befor

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 5 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"2d6aba7a-77d9-5789-a35b-950a7032eddd","locator":{"kind":"html_section","section_id":"c1","order":4,"heading":"02 Reflexion loop","source_file":"track-3-day-16.html"},"checksum":"bcfa4b7827c10001e0cba1c4098f6ee19ec0228909bdaf6a3fe9f38b7d9d66a7"} -->

## 02 Reflexion loop

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 6 Reflexion loop · Mental model & quyết định

> Trích slide Slide 6: ReAct thất bại khi nào? Thought: tìmX Search(X) Kếtquảsai Thought: dùngX Lookup(X) Saitiếp Thought: kếtluận TrảlờiSAI Không detect lỗi! 3 failure modes chính: 1 Lỗi lan tỏa: Saiởbước1→sai hếtchuỗi 2 Infinite loop: Tooltrảnoise→ agentlặpmãi 3 Không backtrack: Đisaiđường nhưngkhôngquaylại Lưu ý Rootcause:ReActkhông có cơ chế tự…

Thought: tìmX Search(X) Kếtquảsai Thought: dùngX Lookup(X) Saitiếp Thought: kếtluận TrảlờiSAI Không detect lỗi!. Điểm nối sang production là: reflection tốt phải chỉ ra failure, evidence và thay đổi tiếp theo. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- 3 failure modes chính: 1 Lỗi lan tỏa: Saiởbước1→sai hếtchuỗi 2 Infinite loop: Tooltrảnoise→ agentlặpmãi 3 Không backtrack: Đisaiđường nhưngkhôngquaylại Lưu ý Rootcause:ReActkhông có cơ chế tự đánh giá.
- Khi đi sai, không có signal nào báo “dừng lại, suy nghĩ lại”.
- Hãychọnpatterntheomức độ cần thiếtcủataskvàchiphívậnhành.

#### Tự kiểm tra · Với reflexion loop, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là reflection tốt phải chỉ ra failure, evidence và thay đổi tiếp theo.

### Slide 9 Reflexion loop · Evidence & failure lens

> Trích slide Slide 9: Bằng chứng: ReAct struggle với multi-hop reasoning 35.1% ReActEM trênHotpotQA Cao Failrate trênmulti-hop 0 Sốlần agenttựsửalỗi Câu hỏi then chốt Nếuthêmchoagentkhảnăng tự đánh giá kếtquảvà rút bài học từsailầm thìsao? →Đóchínhlàýtưởngcủa Reflexion. AICB·Ngày16 8

**Đọc như kỹ sư:** Bằng chứng: ReAct struggle với multi-hop reasoning 35.1% ReActEM trênHotpotQA Cao Failrate trênmulti-hop 0 Sốlần agenttựsửalỗi Câu hỏi then chốt Nếuthêmchoagentkhảnăng tự đánh giá kếtquảvà rút bài học từsailầm thìsao?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 9 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 11 Reflexion loop · Evidence & failure lens

> Trích slide Slide 11: Ý tưởng cốt lõi Reflexion (Shinn et al. 2023) Thêm2thànhphầnvàoReAct: Evaluator(đánhgiákếtquả)và Reflector (rút bài học). Agent thử, đánh giá, suy ngẫm, rồi thử lại — giống cách con ngườihọctừsailầm. Analogy: Nhưsinhviênlàmbàithi. Lần1sai→xemđápán,hiểutạisaosai →lần2làmđúng. ReActchỉlàm1lầnrồinộp. Reflexionchophép“xemlại…

**Đọc như kỹ sư:** 2023) Thêm2thànhphầnvàoReAct: Evaluator(đánhgiákếtquả)và Reflector (rút bài học).

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Agent thử, đánh giá, suy ngẫm, rồi thử lại — giống cách con ngườihọctừsailầm.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 11 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"4b058f22-e767-5111-9879-929da27b79e8","locator":{"kind":"html_section","section_id":"c2","order":5,"heading":"03 Evaluator feedback","source_file":"track-3-day-16.html"},"checksum":"a3d8915a59f8a5c821a2383ddc86c8f1f3130ef7e467f4d7cade5256c549e0ba"} -->

## 03 Evaluator feedback

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 12 Evaluator feedback · Mental model & quyết định

> Trích slide Slide 12: Kiến trúc Reflexion — 4 bước 1. Generate Actor 2. Evaluate Evaluator 3. Reflect Reflector 4. Retry Actor ReflectionMemory“Saiởđâu? thửgìtiếp?” Lặp tới khi đúng hoặc hết attempts score=1? score=0 3 vai trò LLM Actor: sinhhànhđộng Evaluator: chấmđúng/sai Reflector: rútbàihọc Điểm khác biệt vs ReAct Dùngtext…

thửgìtiếp?” Lặp tới khi đúng hoặc hết attempts score=1?. Điểm nối sang production là: evaluator cần độc lập đủ để không chia sẻ blind spot. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- score=0 3 vai trò LLM Actor: sinhhànhđộng Evaluator: chấmđúng/sai Reflector: rútbàihọc Điểm khác biệt vs ReAct Dùngtext feedbackthayvìgradient.
- Critique bằng ngôn ngữ tự nhiên nên dễ parse,debugvàbenchmark.
- Lưu ý Dùng sliding window: quá ngắn thì quên, quá dài thì tốn context.

#### Tự kiểm tra · Với evaluator feedback, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là evaluator cần độc lập đủ để không chia sẻ blind spot.

### Slide 14 Evaluator feedback · Evidence & failure lens

> Trích slide Slide 14: Reflexion trong LangGraph act success? END reflect Yes No append reflection, reset, attempt++ max attempts? → END Node “reflect” 1. Lấytrajectory(đãlàmgì?) 2. GọiReflectorLLM(saiởđâu?) 3. Appendreflectionvàomemory 4. Resetmessages,tăngattempt T ermination Dừng khi:success=True Hoặc:attempt≥max(default3)…

**Đọc như kỹ sư:** END reflect Yes No append reflection, reset, attempt++ max attempts?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Resetmessages,tăngattempt T ermination Dừng khi:success=True Hoặc:attempt≥max(default3) Tránhinfiniteloop—cáimàReActgặpphải AICB·Ngày16 13

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 14 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 16 Evaluator feedback · Evidence & failure lens

> Trích slide Slide 16: Reflection memory: ghi gì, bỏ gì? • Nên ghi: failurereason,lesson,nextstrategy,evidencetitles • Không nên ghi: toànbộtracedàidòngnếukhônggiúplầnthửsau • Cóthểdùng sliding windowhoặcmemory compression T eaching point Memorytốtlàmemory ngắn, cụ thể, hành động được. Khôngphảimemorycàng dàicàngtốt. AICB·Ngày16 15

**Đọc như kỹ sư:** • Nên ghi: failurereason,lesson,nextstrategy,evidencetitles • Không nên ghi: toànbộtracedàidòngnếukhônggiúplầnthửsau • Cóthểdùng sliding windowhoặcmemory compression T eaching point Memorytốtlàmemory ngắn, cụ thể, hành động được.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 16 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"e501acae-85a6-5327-9a30-f738b49a7a5f","locator":{"kind":"html_section","section_id":"c3","order":6,"heading":"04 Reflection memory","source_file":"track-3-day-16.html"},"checksum":"650e0d88127ba01ad3cb16bae8a9ff6c6d9323de1a80d09caa676d529e2d1d65"} -->

## 04 Reflection memory

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 17 Reflection memory · Mental model & quyết định

> Trích slide Slide 17: Reflexion failure modes trong production 1 Evaluator bias: tựchấmquádễhoặcquákhắtkhe 2 Reflection drift: bàihọcchungchung,khônggiúpđượcattemptsau 3 Context bloat: reflectionmemorychiếmhếtcontextwindow 4 Cost blow-up: accuracytăngítnhưngchiphítăngmạnh Thông điệp Reflexion không miễn phí. Cần đánh giáaccuracy gain so với…

Cần đánh giáaccuracy gain so với cost/latency in- crease.. Điểm nối sang production là: memory reflection phải có scope và expiry. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Reflexion cải thiện đáng kể 91% HumanEval (codegen) 80% HotpotQA (multi-hopQA) +20–30% Cảithiện vsReAct Tại sao hiệu quả?
- Reflexiondùng episodic memory—agent“nhớ”bàihọctừcáclầnthửtrước trong cùng episode.
- Giống cách bạn nhớ “lần trước đã thử cách này không được,lầnnàythửkhác”.

#### Tự kiểm tra · Với reflection memory, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là memory reflection phải có scope và expiry.

### Slide 20 Reflection memory · Evidence & failure lens

> Trích slide Slide 20: LATS — Khi cần tìm đường tối ưu S0 A1 A2 A3 B1 B2 B3 UCT chọnnhánh tốt •Highvalue •Lowvalue LATS MCTS + LLM: mỗi node là một trạng thái suy luận;LLMđóngvai policy, valuevà simulation. • ChínhxáchơnReflexion(92.7%vs91%) • Nhưngtốngấp3–5 ×compute • Cầnenvironmentchophép undo Lưu ý Chỉđángdùngkhitaskcógiátrịcaovàcó…

**Đọc như kỹ sư:** LATS — Khi cần tìm đường tối ưu S0 A1 A2 A3 B1 B2 B3 UCT chọnnhánh tốt •Highvalue •Lowvalue LATS MCTS + LLM: mỗi node là một trạng thái suy luận;LLMđóngvai policy, valuevà simulation.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- • ChínhxáchơnReflexion(92.7%vs91%) • Nhưngtốngấp3–5 ×compute • Cầnenvironmentchophép undo Lưu ý Chỉđángdùngkhitaskcógiátrịcaovàcó thểrollback,nhưcodegenhoặcgame.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 20 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 22 Reflection memory · Evidence & failure lens

> Trích slide Slide 22: Khi nào dùng pattern nào? Pattern Memory Chi phí Accuracy Khi nào dùng? ReAct Không $ Baseline Taskđơngiản,1bước Reflexion Episodic $$ +20–30% Multi-step,cầnself-correct LATS Tree $$$$$ +∼2% High-stakes,chophépundo Voyager Persistent $$$ N/A Open-ended,cầntíchlũy Lưu ý Nhiềubàitoánthựctế không cần agent:…

**Đọc như kỹ sư:** Pattern Memory Chi phí Accuracy Khi nào dùng?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Đọc:“ AI Agents That Matter”(2024)—đừngover-engineer.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 22 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"6ca30937-8206-5a1c-8b5c-1f1ae851d291","locator":{"kind":"html_section","section_id":"c4","order":7,"heading":"05 LATS search","source_file":"track-3-day-16.html"},"checksum":"6348f148a5956b79b6e650a7f4e38a57d55ffebd05a8a52f39802f754638936f"} -->

## 05 LATS search

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 23 LATS search · Mental model & quyết định

> Trích slide Slide 23: Case study mới: multi-agent research system • Mộtplanneragentchiacâuhỏithànhnhiềusub-questions • Cácworkeragentstìmthôngtinsongsong • Mộtsynthesizeragenthợpnhấtvàviếtcâutrảlờicuốicùng • Patternnàyhợpvới open-ended research,khôngphảimọibusinessworkflow Lesson Multi-agent có ý nghĩa khi bài toánmở, khó dự đoán trước các bước, và…

Checklist triển khai an toàn cho agent nâng cao 1 Có max_attempts 2 Cóstructuredoutputschoevaluator/tools 3 Cótraceđểdebugtừsớm 4 Toolcàngdeterministiccàngtốt 5 Cóhumanreviewchoactionrủiro Production mindset Promptchỉlà1phần.. Điểm nối sang production là: LATS đổi latency lấy exploration nên cần budget.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Cònlạilàstate,toolquality,tracing,evalvàguardrails.
- Kỹ thuật nâng cao trước khi vào lab Cácpatternproductiongiúpagentổnđịnh,dễdebugvàdễđánh giáhơn
- Chỉ thêm lớp mới khi đo được lỗi hoặcthấybottleneckrõràng.

#### Tự kiểm tra · Với lats search, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là LATS đổi latency lấy exploration nên cần budget.

### Slide 25 LATS search · Evidence & failure lens

> Trích slide Slide 25: Kỹ thuật nâng cao trước khi vào lab Cácpatternproductiongiúpagentổnđịnh,dễdebugvàdễđánh giáhơn

**Đọc như kỹ sư:** Kỹ thuật nâng cao trước khi vào lab Cácpatternproductiongiúpagentổnđịnh,dễdebugvàdễđánh giáhơn

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 25 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 27 LATS search · Evidence & failure lens

> Trích slide Slide 27: Evaluator tốt quyết định chất lượng Reflexion Evaluator nên chấm 4 thứ 1 Correctness: câutrảlờicóđúng không? 2 Grounding: cóbámevidence/tool outputkhông? 3 Completeness: đãtrảlờiđủcácphần chưa? 4 Actionability: reflectioncóthểsửa đượckhông? Anti-pattern Nếu evaluator chỉ nói``incorrect''thì re- flectorrấtkhósinhbàihọchữuích.…

**Đọc như kỹ sư:** Evaluator tốt quyết định chất lượng Reflexion Evaluator nên chấm 4 thứ 1 Correctness: câutrảlờicóđúng không?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- 4 Actionability: reflectioncóthểsửa đượckhông?
- Anti-pattern Nếu evaluator chỉ nói``incorrect''thì re- flectorrấtkhósinhbàihọchữuích.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 27 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"35850698-3def-5f3d-9a0e-f1db03696ebd","locator":{"kind":"html_section","section_id":"c5","order":8,"heading":"06 Voyager & skill library","source_file":"track-3-day-16.html"},"checksum":"6c326fd114a90a16b49f25c62f448acc9fecd6f93acc049ee3bb6b6dfdb82c5c"} -->

## 06 Voyager & skill library

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 28 Voyager & skill library · Mental model & quyết định

> Trích slide Slide 28: Reflection memory: lưu bài học, không lưu nguyên chat history Memory entry nên ngắn và thao tác được lesson: “Luônverifythựcthểởhop2trước khitrảlời” trigger:“Câuhỏi2-hopcóentitydễnhầm” fix: “Search thêm 1 bước và so khớp tên riêng” • Mỗientrychỉ1lỗi+1cáchsửa • Ưutiênmemorycócấutrúchơn free-formdài • Nêncó…

Ifambiguityremains,askorabstain Compressedmemory: “Verifyevidencebeforefinalanswer” Điểm dạy học quan trọng Memorytốtlàm giảm lặp lỗi,nhưngmem- ory dài quá lại làm prompt noisy và tăng cost.. Điểm nối sang production là: skill library cần version và tiêu chí tái sử dụng.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- Multi-hopQA,code/debug,dataextraction nhiềubước,workflowcóexternalstate.
- Prompt/tool contract Good: “Nếu search không trả evi- dence rõ ràng, không được đoán; trả về insufficient.
- Bad: “Cốgắngtrảlờibằngmọigiá.” Nhìn dưới góc dạy học Sinh viên thường tối ưu prompt trước, nhưngbugthựctếhaynằmởtoolschema, parser,timeout,retryvàsideeffects.

#### Tự kiểm tra · Với voyager & skill library, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là skill library cần version và tiêu chí tái sử dụng.

### Slide 31 Voyager & skill library · Evidence & failure lens

> Trích slide Slide 31: Observability + eval flywheel: cách agent tiến bộ sau mỗi lần demo T race runs Label failures Build eval set Run gradersFix prompt/tool/stateRe-test / redeploy • Đừngchỉlogfinalanswer • Hãylogcảdecision,toolcalls, retryvàfailuremodes • Từtracemớisinhradataset chấmtựđộngcóích Liên hệ với lab report.json, runs.jsonlvàbreak- down…

**Đọc như kỹ sư:** Observability + eval flywheel: cách agent tiến bộ sau mỗi lần demo T race runs Label failures Build eval set Run gradersFix prompt/tool/stateRe-test / redeploy • Đừngchỉlogfinalanswer • Hãylogcảdecision,toolcalls, retryvàfailuremodes • Từtracemớisinhradataset

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 31 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 33 Voyager & skill library · Evidence & failure lens

> Trích slide Slide 33: Khi multi-agent bắt đầu đáng tiền Dấu hiệu phù hợp •Nhiềudomaintoolrấtkhácnhau •Cầnparallel explorationcho open-endedresearch •Cầntáchvaitròplanner / worker / judge / synthesizer •Cầntáchread/write agentsđểgiảm risk Ví dụ phù hợp Research system, code review + synthe- sis,opsassistantcóapprovalworkflow. Quy tắc an toàn…

**Đọc như kỹ sư:** Quy tắc an toàn Càngnhiềuagent,càngcầnhandoffcon- tract rõ ràng: input schema, output schema, stop condition, ownership của state.

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Thông điệp cuối phần lý thuyết Phứctạphơnkhôngmặcđịnhtốthơn.
- Chỉlênmulti-agentkhisingle-agent + tools + eval + memoryđãchạmtrầnrõràng.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 33 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"41ad6b8e-08da-559a-b65c-13c0a04008c4","locator":{"kind":"html_section","section_id":"c6","order":9,"heading":"07 So sánh pattern","source_file":"track-3-day-16.html"},"checksum":"2b6615e7eb66083e39a52727276dd6d8ba882b3cd4a8c13eb2132d7b8bee7185"} -->

## 07 So sánh pattern

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 34 So sánh pattern · Mental model & quyết định

> Trích slide Slide 34: Demo & Thực hành XemReflexionhoạtđộngthựctế

Lab 16: Implement Reflexion agent từ scratch với LangGraph Mục tiêu: Reflexionagentrepo+benchmarkreport(EMcomparison, costanalysis,failurecategorization) Thời lượng: 2giờ AICB·Ngày16 35. Điểm nối sang production là: self-improvement runtime không đồng nghĩa model tự huấn luyện.

Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- self-improvement runtime không đồng nghĩa model tự huấn luyện

#### Tự kiểm tra · Với so sánh pattern, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là self-improvement runtime không đồng nghĩa model tự huấn luyện.

### Slide 36 So sánh pattern · Evidence & failure lens

> Trích slide Slide 36: Lab 16: Implement Reflexion agent từ scratch với LangGraph Mục tiêu: Reflexionagentrepo+benchmarkreport(EMcomparison, costanalysis,failurecategorization) Thời lượng: 2giờ AICB·Ngày16 35

**Đọc như kỹ sư:** Lab 16: Implement Reflexion agent từ scratch với LangGraph Mục tiêu: Reflexionagentrepo+benchmarkreport(EMcomparison, costanalysis,failurecategorization) Thời lượng: 2giờ AICB·Ngày16 35

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 36 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 38 So sánh pattern · Evidence & failure lens

> Trích slide Slide 38: Lab roadmap 120 phút 1 30 phút: chạyReActbaselinevàhiểutrace 2 35 phút: thêmEvaluatordạngstructuredoutput 3 25 phút: thêmReflector+reflectionmemory 4 30 phút: benchmark,viếtreport,sinhartifactđểauto-grade Instructor tip Chohọcviênchạymockmodetrướcđểhiểuformatoutput,sauđómớithayprovider thật. AICB·Ngày16 37

**Đọc như kỹ sư:** Lab roadmap 120 phút 1 30 phút: chạyReActbaselinevàhiểutrace 2 35 phút: thêmEvaluatordạngstructuredoutput 3 25 phút: thêmReflector+reflectionmemory 4 30 phút: benchmark,viếtreport,sinhartifactđểauto-grade Instructor tip Chohọcviênchạymockmodetrướcđểhiểuformato

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 38 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"7a24f884-c926-550b-8136-06f30b298011","locator":{"kind":"html_section","section_id":"c7","order":10,"heading":"08 Production guardrails & Lab","source_file":"track-3-day-16.html"},"checksum":"5796fe09ad42a772e0e6194250f83fd351f9368ddaac95e81ecace11795ac336"} -->

## 08 Production guardrails & Lab

Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path?

### Slide 39 Production guardrails & Lab · Mental model & quyết định

> Trích slide Slide 39: Bonus tasks để phân hoá học viên • adaptivemaxattempts • memorycompression • evidence-groundedevaluator • mini-LATSbranching(2candidates/step) • plan-then-executetrướckhireflect Cách chấm Khôngchỉchấm“cólàmđượckhông”màchấmthêm thí nghiệm, trade-off và giải thích. AICB·Ngày16 38

Tổng kết T akeaway 1 Reflexion là nâng cấp hợp lý khi ReAct thấtbại: costvừaphải,accuracytăngrõ.. Điểm nối sang production là: mọi loop phải có stop condition và cost cap. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ chỉ là implementation detail.

- T akeaway 2 LATS và Voyager đổi compute lấy opti- malityhoặcgenerality;chỉdùngkhitask thậtsựcần.
- T akeaway 3 Cẩnthận“degeneration-of-thought”: re- flectionkéodàicóthểlàmoutputtệhơn.
- T akeaway 4 Xuhướngproduction:structuredoutputs, tracingvàevalquantrọnghơnfree-form reasoning.

#### Tự kiểm tra · Với production guardrails & lab, vì sao một demo đúng chưa đủ chứng minh hệ thống sẵn sàng production?

Vì demo thường chỉ kiểm happy path. Câu trả lời đạt phải nêu ít nhất một ràng buộc, một telemetry/evidence và một failure mode; nguyên tắc trọng tâm là mọi loop phải có stop condition và cost cap.

### Slide 42 Production guardrails & Lab · Evidence & failure lens

> Trích slide Slide 42: Ngày 17: Memory Systems for Agents Agentđãbiếtreasoning—nhưngtạisaonóquênhếtsaumỗi conversation? • HoànthànhLab16: Reflexionagent+benchmark • Đọc: Anthropic“BuildingEffectiveAgents” AICB·Ngày16 41

**Đọc như kỹ sư:** Ngày 17: Memory Systems for Agents Agentđãbiếtreasoning—nhưngtạisaonóquênhếtsaumỗi conversation?

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- • HoànthànhLab16: Reflexionagent+benchmark • Đọc: Anthropic“BuildingEffectiveAgents” AICB·Ngày16 41

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 42 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

### Slide 44 Production guardrails & Lab · Evidence & failure lens

> Trích slide Slide 44: Cảm ơn! AICB-P2T3·Ngày16·AdvancedAgentArchitectures github.com/vinuni-aicb Liênhệ: instructor@vinuni.edu.vn

**Đọc như kỹ sư:** AICB-P2T3·Ngày16·AdvancedAgentArchitectures github.com/vinuni-aicb Liênhệ: instructor@vinuni.edu.vn

Không dừng ở việc nhận diện thuật ngữ. Hãy chuyển nội dung này thành một quyết định có điều kiện: khi giả định thay đổi, kiến trúc, SLO hoặc control nào phải đổi theo?

- Xác định input, output và boundary của cơ chế.
- Nêu telemetry chứng minh cơ chế hoạt động.
- Chỉ ra điều kiện cần rollback hoặc escalation.

#### Tự kiểm tra · Điều gì có thể làm kết luận ở slide 44 không còn đúng?

Nêu ít nhất một thay đổi về scale, data sensitivity, latency budget hoặc độ tin cậy dependency; sau đó chỉ rõ telemetry để phát hiện thay đổi đó.

---

<!-- chiron-source-span: {"source_span_id":"3271d04b-6ad2-5c03-b30c-845b3bd2ce9d","locator":{"kind":"html_section","section_id":"ladder","order":11,"heading":"▤ Luyện kỹ năng cốt lõi","source_file":"track-3-day-16.html"},"checksum":"a101db9c2a230d1f3d7f380b3e242a6248b22f64784306426abfda44bbc82433"} -->

## ▤ Luyện kỹ năng cốt lõi

Ba nhiệm vụ giảm dần giàn giáo: giải thích → phân tích → thiết kế và bảo vệ quyết định.

### Bậc 1 Giải thích mental model của Reflection patterns bằng một sơ đồ input → decision → evidence.

**Gợi ý:** Dùng ba chương đầu và không nêu tên công cụ trước khi nêu trách nhiệm.

Tiêu chí tự chấm Đạt khi có boundary, state, failure path và ít nhất hai slide làm bằng chứng.

### Bậc 2 Phân tích case SmartCheck: chọn một thiết kế, sau đó steelman phương án đối lập.

**Gợi ý:** Dùng một mô-đun để kiểm độ nhạy của giả định quan trọng nhất.

Tiêu chí tự chấm Đạt khi nêu trade-off định lượng, điều kiện đổi quyết định và rủi ro còn lại.

### Bậc 3 Viết mini design review production-ready và kế hoạch kiểm chứng trước rollout.

**Gợi ý:** Chốt SLO/eval gate, telemetry, rollback, owner và cost cap.

Tiêu chí tự chấm Đạt khi người khác có thể triển khai, quan sát, dừng và audit hệ thống từ tài liệu của bạn.

---

<!-- chiron-source-span: {"source_span_id":"d385dc6c-1f80-5d97-bfd4-a789dac00ffb","locator":{"kind":"html_section","section_id":"section-012","order":12,"heading":"∑ Phòng mô phỏng quyết định","source_file":"track-3-day-16.html"},"checksum":"e3d3b584891e6b8d0ae47bc897129ac9e971def8f98a21a7e9319c8c7300a2c6"} -->

## ∑ Phòng mô phỏng quyết định

Mọi con số mặc định là giả định để học độ nhạy, không phải benchmark production.

#### Tương tác Mô-đun 1 — Reflexion — thêm lần thử có còn sinh lợi?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Success ban đầu:**: min `10`, max `95`, step `1`, default `55`

- **Control - Tỷ lệ sửa/lần:**: min `5`, max `90`, step `5`, default `40`

- **Control - Số lần thử:**: min `1`, max `8`, step `1`, default `3`

- **Control - Chi phí/lần:**: min `1`, max `100`, step `1`, default `12`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 2 — Evaluator — bắt lỗi tốt hay chỉ tạo false retry?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Tỷ lệ run lỗi:**: min `1`, max `80`, step `1`, default `25`

- **Control - Sensitivity:**: min `40`, max `100`, step `1`, default `85`

- **Control - Specificity:**: min `40`, max `100`, step `1`, default `90`

- **Control - Run/ngày:**: min `100`, max `50000`, step `100`, default `5000`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

#### Tương tác Mô-đun 3 — Pattern fit — ReAct, Reflexion hay LATS?

Thay đổi giả định, dự đoán hướng biến thiên trước, rồi đối chiếu kết quả. Mục tiêu không phải nhớ một con số mặc định mà là hiểu biến nào thực sự điều khiển quyết định.

**Predict:** trước khi kéo thanh, hãy ghi dự đoán. **Observe:** tìm điểm gãy trên chỉ số và biểu đồ. **Explain:** dùng công thức để giải thích vì sao trực giác đúng hoặc sai.

- **Control - Độ phức tạp:**: min `0`, max `100`, step `5`, default `65`

- **Control - Mức stakes:**: min `0`, max `100`, step `5`, default `70`

- **Control - Ngân sách latency:**: min `0`, max `100`, step `5`, default `45`

- **Control - Tool reliability:**: min `0`, max `100`, step `5`, default `75`

Kết quả 1

Kết quả 2

Kết quả 3

Kết quả 4

---

<!-- chiron-source-span: {"source_span_id":"32c5afa9-1a1d-5776-9b5a-413d3234cdd1","locator":{"kind":"html_section","section_id":"misc","order":13,"heading":"✕ Hiểu lầm phổ biến","source_file":"track-3-day-16.html"},"checksum":"e82be22946b09b6b798268a3028bc43b0906bf08e0cfd4831dcaafef96b85f1f"} -->

## ✕ Hiểu lầm phổ biến

Hiểu lầm Chỉ cần triển khai từ retry đến self-improvement là phần còn lại tự động an toàn và ổn định.

Sửa lại Retry mù lặp lại cùng policy nên thường lặp lại cùng lỗi.

Vì sao quan trọng · slide 1 · 3 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai reflexion loop là phần còn lại tự động an toàn và ổn định.

Sửa lại Reflection tốt phải chỉ ra failure, evidence và thay đổi tiếp theo.

Vì sao quan trọng · slide 6 · 9 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai evaluator feedback là phần còn lại tự động an toàn và ổn định.

Sửa lại Evaluator cần độc lập đủ để không chia sẻ blind spot.

Vì sao quan trọng · slide 12 · 14 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai reflection memory là phần còn lại tự động an toàn và ổn định.

Sửa lại Memory reflection phải có scope và expiry.

Vì sao quan trọng · slide 17 · 20 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai lats search là phần còn lại tự động an toàn và ổn định.

Sửa lại LATS đổi latency lấy exploration nên cần budget.

Vì sao quan trọng · slide 23 · 25 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

Hiểu lầm Chỉ cần triển khai voyager & skill library là phần còn lại tự động an toàn và ổn định.

Sửa lại Skill library cần version và tiêu chí tái sử dụng.

Vì sao quan trọng · slide 28 · 31 Cách hiểu cũ biến một cơ chế thành lời bảo đảm. Trong production phải đo outcome và thiết kế đường lỗi, không suy từ việc có component sang việc hệ thống đúng.

---

<!-- chiron-source-span: {"source_span_id":"76777855-2489-56b5-a6dd-113165a66712","locator":{"kind":"html_section","section_id":"apply","order":14,"heading":"◆ Áp dụng vào SmartCheck AI","source_file":"track-3-day-16.html"},"checksum":"93bec098587c38fa74271b6dab9c4b949fa7e99c73c114acd290a91e1171bb5d"} -->

## ◆ Áp dụng vào SmartCheck AI

SmartCheck AI thất bại khi xử lý ngoại lệ đặt phòng; evaluator phải tạo phản hồi đủ cụ thể cho lần chạy sau.

| Quyết định | Khuyến nghị | Bằng chứng cần có | Slide |
| --- | --- | --- | --- |
| Từ retry đến self-improvement | Retry mù lặp lại cùng policy nên thường lặp lại cùng lỗi. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 1 · 3 |
| Reflexion loop | Reflection tốt phải chỉ ra failure, evidence và thay đổi tiếp theo. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 6 · 9 |
| Evaluator feedback | Evaluator cần độc lập đủ để không chia sẻ blind spot. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 12 · 14 |
| Reflection memory | Memory reflection phải có scope và expiry. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 17 · 20 |
| LATS search | LATS đổi latency lấy exploration nên cần budget. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 23 · 25 |
| Voyager & skill library | Skill library cần version và tiêu chí tái sử dụng. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 28 · 31 |
| So sánh pattern | Self-improvement runtime không đồng nghĩa model tự huấn luyện. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 34 · 36 |
| Production guardrails & Lab | Mọi loop phải có stop condition và cost cap. | Theo dõi outcome, latency/cost, failure mode và lưu evidence đủ để tái hiện quyết định. | 39 · 42 |

---

<!-- chiron-source-span: {"source_span_id":"26c89ba0-1428-57e7-ba1f-27cfdb58bf58","locator":{"kind":"html_section","section_id":"numbers","order":15,"heading":"# Con số cần kiểm chứng","source_file":"track-3-day-16.html"},"checksum":"789169df2208b1ed1529c58f0f261753dccbb090e6257755f25d3a3adad2c4bc"} -->

## # Con số cần kiểm chứng

Chỉ ghi số có trong nguồn; caveat đi cùng con số để tránh học thuộc sai ngữ cảnh.

| Giá trị | Ý nghĩa | Giới hạn diễn giải | Slide |
| --- | --- | --- | --- |
| 1 K | Agenda 1 Khinàosingle-agentthấtbại? 2 Reflexion: thêmself-evaluationvàoloop 3 LATS,Voyagervàdecisionmatrix 4 Kỹthuậtnângcaotrướckhivàolab 5 Demo+lab+auto-gradin | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 3 |
| 4 K | agentthấtbại? 2 Reflexion: thêmself-evaluationvàoloop 3 LATS,Voyagervàdecisionmatrix 4 Kỹthuậtnângcaotrướckhivàolab 5 Demo+lab+auto-grading AICB·Ngày16 2 | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 3 |
| 3 K | nh: 1 Lỗi lan tỏa: Saiởbước1→sai hếtchuỗi 2 Infinite loop: Tooltrảnoise→ agentlặpmãi 3 Không backtrack: Đisaiđường nhưngkhôngquaylại Lưu ý Rootcause:ReActkhông có cơ chế tự đánh giá. Khi đi sai, không có signal nào báo “dừng lại, suy nghĩ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 6 |
| 35.1% | Bằng chứng: ReAct struggle với multi-hop reasoning 35.1% ReActEM trênHotpotQA Cao Failrate trênmulti-hop 0 Sốlần agenttựsửalỗi Câu hỏi then chốt Nếuthêmchoagentkhảnăng tự đánh giá kếtquảvà rút bài học từsai | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 9 |
| 1 m | se: {error}'' ``lesson: {lesson}'' ``next strategy: {strategy}'' 5 thành phần state: 1 messages: hộithoạihiệntại 2 trajectory: lịchsửhànhđộng 3 reflection_memory: bàihọc rútra 4 attempt_count: sốlầnthử 5 success: đãđúngchưa? Lưu ý Dùng sl | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 13 |
| 91% | Reflexion cải thiện đáng kể 91% HumanEval (codegen) 80% HotpotQA (multi-hopQA) +20–30% Cảithiện vsReAct Tại sao hiệu quả? Reflexiondùng episodic memory—agent“nhớ”bàihọctừcáclầnthửtr | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 18 |
| 80% | Reflexion cải thiện đáng kể 91% HumanEval (codegen) 80% HotpotQA (multi-hopQA) +20–30% Cảithiện vsReAct Tại sao hiệu quả? Reflexiondùng episodic memory—agent“nhớ”bàihọctừcáclầnthửtrước trong cùng episode. | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 18 |
| 30% | Reflexion cải thiện đáng kể 91% HumanEval (codegen) 80% HotpotQA (multi-hopQA) +20–30% Cảithiện vsReAct Tại sao hiệu quả? Reflexiondùng episodic memory—agent“nhớ”bàihọctừcáclầnthửtrước trong cùng episode. Giống cách bạn nhớ “lần trước đ | Chỉ áp dụng trong ngữ cảnh ví dụ/điều kiện nêu ở slide; kiểm nguồn cập nhật trước khi dùng như benchmark. | 18 |

Số do mô-đun tính Các kết quả tương tác là phép tính từ giả định người học chọn, không phải số liệu của slide hay production.

---

<!-- chiron-source-span: {"source_span_id":"568e43b7-ef4e-5d38-aabd-c343387c4189","locator":{"kind":"html_section","section_id":"cheat","order":16,"heading":"▣ Cheat sheet ôn thi","source_file":"track-3-day-16.html"},"checksum":"58f5b9b10eee73dc26ec47eca68fb6233bb3aebd5e0aa731d939c4d3bca16360"} -->

## ▣ Cheat sheet ôn thi

| Trigger | Quy tắc quyết định | Slide |
| --- | --- | --- |
| Khi gặp từ retry đến self-improvement | retry mù lặp lại cùng policy nên thường lặp lại cùng lỗi | 1 · 3 |
| Khi gặp reflexion loop | reflection tốt phải chỉ ra failure, evidence và thay đổi tiếp theo | 6 · 9 |
| Khi gặp evaluator feedback | evaluator cần độc lập đủ để không chia sẻ blind spot | 12 · 14 |
| Khi gặp reflection memory | memory reflection phải có scope và expiry | 17 · 20 |
| Khi gặp lats search | LATS đổi latency lấy exploration nên cần budget | 23 · 25 |
| Khi gặp voyager & skill library | skill library cần version và tiêu chí tái sử dụng | 28 · 31 |
| Khi gặp so sánh pattern | self-improvement runtime không đồng nghĩa model tự huấn luyện | 34 · 36 |
| Khi gặp production guardrails & lab | mọi loop phải có stop condition và cost cap | 39 · 42 |
| Khi gặp từ retry đến self-improvement | đánh giá success phải tính cả side effect | 1 · 3 |

---

<!-- chiron-source-span: {"source_span_id":"0efecbd8-8076-5d50-b264-3ada724912f5","locator":{"kind":"html_section","section_id":"gloss","order":17,"heading":"☰ Từ điển thuật ngữ","source_file":"track-3-day-16.html"},"checksum":"2daee24b09d4a248b84bb08cd07bd93a61f90039ee698df22c1bad5d5c161c9f"} -->

## ☰ Từ điển thuật ngữ

---

<!-- chiron-source-span: {"source_span_id":"15d041e1-2e6a-50d4-b4d6-e3c38932c750","locator":{"kind":"html_section","section_id":"bloom","order":18,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-16.html"},"checksum":"daa792e15dd4fe4a0d61b3a89ddd403669ea01ff1586be7a5f13f3a8d7cb55ca"} -->

## ◉ Bạn đang ở mức nào?

| Mức Bloom | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể lại các thành phần và định nghĩa chính. | slide 1 · 3 · 5 |
| 2 · Hiểu | Giải thích quan hệ nhân quả và failure mode. | slide 6 · 9 · 11 |
| 3 · Áp dụng | Áp dụng quy tắc vào một case có ràng buộc. | slide 12 · 14 · 16 |
| 4 · Phân tích | So sánh hai kiến trúc trên cùng tiêu chí. | slide 17 · 20 · 22 |
| 5 · Đánh giá | Bảo vệ quyết định bằng evidence và bác bỏ phản ví dụ. | slide 23 · 25 · 27 |
| 6 · Sáng tạo | Thiết kế hệ thống, eval và rollback hoàn chỉnh. | slide 28 · 31 · 33 |
