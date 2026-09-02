---
schema_version: 1
course_id: rag-intensive
document_id: "4601d9e3-479e-5796-be14-d42a94900f91"
document_version_id: "30e36300-8e63-55dd-9b39-46a3f28e5bad"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "Multi-Agent Systems — phân tích & breakdown từng slide"
source_file: "track-3-day-20.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\track-3-day-20.html"
source_sha256: "588fdd1c2ed60567a09cd0b2f10d9aa34972111fff9f4ec2370ebe020c060509"
parser_version: chiron-structured-markdown-v1
html_section_count: 18
interactive_module_count: 5
interactive_control_count: 16
language: vi
---

# Multi-Agent Systems — phân tích & breakdown từng slide

> Đọc lại toàn bộ 37 slide của buổi Ngày 20, giải thích cặn kẽ từng khái niệm, và 
 ánh xạ mỗi bài học sang một ví dụ thực tế — chủ yếu là dự án SmartCheck AI 
 (agentic check-in kiosk) mà bạn đang làm.

<!-- chiron-source-span: {"source_span_id":"0c13089e-6c78-5546-a2d5-5d1dcd6073d3","locator":{"kind":"html_section","section_id":"howto","order":1,"heading":"Đọc tài liệu này thế nào cho hiệu quả","source_file":"track-3-day-20.html"},"checksum":"b42a57e0ca2650148607d5af56aef53439397b2cdb7d72985290f91844ea72fa"} -->

### Đọc tài liệu này thế nào cho hiệu quả

Tài liệu dài. Đừng đọc tuần tự từ đầu đến cuối trong một lần — hãy đọc **ba lượt với ba mục tiêu khác nhau**. 
 Não chỉ giữ được kiến thức khi nó được *lấy ra* nhiều lần, không phải khi nó được *đọc vào* nhiều lần.

Lượt 1 · ~15 phút

Trước khi vào lab

- Đọc slide 6, 11, 16, 34
- Chạy Trình mô phỏng, bấm thử 6 tab
- Mục tiêu: trả lời được "khi nào KHÔNG dùng multi-agent"

Lượt 2 · ~60 phút

Để làm được, không chỉ hiểu

- Chương 1–5, làm hết phần "Dự đoán trước khi kéo"
- Làm 3 bài tập bậc thang theo thứ tự
- Dừng ở mỗi Ô kiểm tra cuối chương, trả lời trước khi mở đáp án

Lượt 3 · ~30 phút

Trước quiz / phỏng vấn

- 5 hiểu lầm phổ biến — đây là chỗ quiz hay hỏi nhất
- Cheat sheet + Từ điển thuật ngữ
- Tự chấm bằng thang tự đánh giá

Luôn dự đoán trước khi kéo thanh trượt.

predict-before-demo

slide 27

chính là

---

<!-- chiron-source-span: {"source_span_id":"fc686aed-b6bf-5811-b0bc-1add5fbb7ca2","locator":{"kind":"html_section","section_id":"c0","order":2,"heading":"00 Mở đầu","source_file":"track-3-day-20.html"},"checksum":"66e0a1a5ae7e285b4fc38d2967ff0f3dd0e3a17da2a2af21549fe19f2dac1f5f"} -->

## 00 Mở đầu

Slide 1–3: khung buổi học và câu hỏi dẫn dắt.

### Slide 1 Trang bìa — Multi-Agent Systems

> Trích slide 
>  "Multi-Agent Systems — AICB-P2T3 · Ngày 20 · Chương 4 — Agent Nâng Cao. VinUniversity · Phase 2 · Track 3 · Tuần 4"

**Đọc vị trí trong chương trình.** Đây là bài cuối của Chương 4 "Agent Nâng Cao". 
 Bốn bài trước (N16–N19) lần lượt là Reflexion, Memory Systems, Production RAG, GraphRAG — tất cả đều 
 là kỹ thuật làm *một* agent mạnh hơn. Ngày 20 là bài đầu tiên đặt câu hỏi ngược lại: 
 khi nào thì *thêm agent* mới là câu trả lời, và cái giá phải trả là gì.

sau

### Slide 2 Câu hỏi dẫn dắt

> Trích slide 
>  "HÃY SUY NGHĨ… — Khi một agent không đủ — Supervisor, Debate, Parallel patterns giải quyết bài toán như thế nào? Giữ câu hỏi này trong đầu khi học bài hôm nay."

Ba từ khoá trong câu hỏi chính là ba pattern trục của buổi học, và mỗi pattern giải một loại 
 bottleneck khác nhau. Ghi nhớ cặp *pattern → bottleneck* này là đủ để trả lời 70% câu hỏi quiz:

| Pattern | Giải bottleneck | Cái giá phải trả |
| --- | --- | --- |
| Supervisor | Một agent phải làm quá nhiều loại việc → prompt phình to, tool nhiều, chọn sai tool | Thêm 1 lượt LLM cho mỗi lần route; nguy cơ routing loop |
| Debate | Câu trả lời sai mà nghe rất thuyết phục (hallucination) | 2–3× cost, latency cộng dồn |
| Parallel | Latency — nhiều subtask độc lập chạy tuần tự | Merge conflict, state race, khó debug |

grounding

latency

### Slide 3 Nội dung bài học

> Trích slide 
>  "1. Tại sao cần nhiều Agent? 2. 5 Agentic Workflow Patterns (Anthropic) 3. Supervisor Pattern — Orchestration 4. Debate Agents — Adversarial Collaboration 5. Parallel Execution & Shared State 6. Multi-Agent Frameworks 7. Demo & Thực hành"

Cấu trúc buổi học đi theo trình tự **quyết định → mẫu thiết kế → thực thi → công cụ → đo đạc**. 
 Chương 1 dạy bạn *khi nào không nên* dùng multi-agent; chương 2 đưa ra thang leo 5 mức; 
 chương 3–5 là ba pattern nặng ký nhất; chương 6 là chọn framework; chương 7 bắt bạn chứng minh bằng benchmark.

---

<!-- chiron-source-span: {"source_span_id":"2704eba2-25ea-55ab-bbea-1384c5f43ae1","locator":{"kind":"html_section","section_id":"c1","order":3,"heading":"01 Tại sao cần nhiều Agent?","source_file":"track-3-day-20.html"},"checksum":"7f3c8adf32c69728b1dd7e8b2561b3a1da9714eeccdeee5d54150e1bdbf93f89"} -->

## 01 Tại sao cần nhiều Agent?

Slide 4–9: taxonomy, failure modes, và nguyên tắc "Start simplest".

### Slide 4 Section divider

> Trích slide 
>  "01 — Tại sao cần nhiều Agent? Taxonomy, failure modes, và nguyên tắc Start simplest "

"Start simplest" là nguyên tắc xuyên suốt, lấy trực tiếp từ bài *Building Effective Agents* của Anthropic. Diễn giải kỹ thuật: mỗi agent bạn thêm vào hệ thống 
 làm tăng **số điểm có thể hỏng** theo cấp số nhân, chứ không phải cộng tuyến tính — vì 
 ngoài lỗi của từng agent còn có lỗi *giữa* các agent (handoff, context loss, tranh chấp state).

### Slide 5 Trực giác cốt lõi — Multi-Agent = Team dự án

> Trích slide 
>  "Multi-agent giống team dự án: có PM (supervisor), specialists (workers), shared document (state). 
>  Single agent = 1 người làm hết: research, phân tích, viết báo cáo. Tốt cho task đơn giản. 
>  Multi-agent = team 3 người: researcher tìm data, analyst phân tích, writer viết — mỗi người master 1 việc. 
>  Nhưng: Team cũng có overhead — họp, miscommunication, conflict. Chỉ scale khi 1 người không đủ."

**Phép so sánh này ánh xạ 1-1 sang kỹ thuật**, và đây là bảng ánh xạ đáng học thuộc:

| Team người | Hệ multi-agent | Chi tiết kỹ thuật |
| --- | --- | --- |
| PM | Supervisor node | Một lượt LLM chỉ để quyết định "gọi ai tiếp theo", thường dùng tool-calling để ép output có cấu trúc |
| Specialist | Worker node | Prompt hẹp + bộ tool riêng + (tuỳ chọn) model riêng |
| Tài liệu chung | Shared state | TypedDict trong LangGraph — mọi node đọc/ghi vào đây |
| Cuộc họp | Handoff / routing turn | Tốn token và latency mà không sinh ra nội dung mới |
| Hiểu nhầm | Context loss | Worker chỉ nhận được một phần state → trả lời lệch |
| Xung đột | Merge conflict | Hai worker song song cùng ghi một key trong state |

4 lần

Một phép so sánh tốt giúp bạn hiểu nhanh, nhưng nếu không biết nó *hỏng ở chỗ nào*, 
 chính nó sẽ tạo ra hiểu lầm mới. Ba chỗ phép so sánh "team dự án" gãy:

**1 · Người có trí nhớ liên tục; agent thì không.** Một thành viên team nhớ cuộc họp 
 tuần trước. Mỗi lượt gọi LLM là *một người hoàn toàn mới* vừa được đưa cho tập hồ sơ và bảo 
 "xử lý đi". Mọi thứ không nằm trong hồ sơ đó thì không tồn tại.

**2 · Người biết tự hỏi khi mơ hồ; agent mặc định đoán.** Một analyst thật sẽ nhắn PM 
 "đề bài này nghĩa là gì?". Agent sẽ chọn một cách hiểu và chạy tiếp một cách tự tin.

**3 · Người chịu trách nhiệm; agent thì không.** Khi output sai, không có agent nào 
 bị khiển trách. Trách nhiệm nằm nguyên vẹn ở người thiết kế hệ thống — tức là bạn.

Chúng giải thích chính xác vì sao ba nhóm lỗi MAST ở [slide 9](#s9) tồn tại: 
 chỗ gãy 1 sinh ra *context loss*, chỗ gãy 2 sinh ra *specification failure*, 
 chỗ gãy 3 sinh ra *thiếu verification*. Nói cách khác: mọi thứ bạn mặc nhiên trông cậy ở một 
 đồng nghiệp người, bạn phải **tự tay xây** trong hệ multi-agent.

thật sự cần bộ tool hoặc prompt khác nhau

### Slide 6 Multi-Agent Taxonomy — quy tắc 80%

> Trích slide 
>  "3 lý do chính để multi-agent: 1. Specialization: mỗi agent master 1 domain — 2. Parallelization: concurrent subtasks, giảm latency — 3. Cross-checking: consensus giảm hallucination. 
>  Decision rule: nếu single agent đạt trên 80% accuracy thì KHÔNG thêm agents — complexity không justify. 
>  Nhiều agents + không clear decomposition = chaos ( "Bag of Agents" )"

Đây là slide quan trọng nhất của chương 1. Ba điểm cần hiểu đúng:

#### 1 · Ba lý do là ba bằng chứng phải đưa ra, không phải ba cái cớ

- Specialization — bằng chứng: prompt của single agent đã quá dài, hoặc số tool 
 vượt ngưỡng model chọn đúng (thực tế thường bắt đầu suy giảm rõ khi vượt ~10–15 tool). Tách agent 
 chính là cách thu nhỏ không gian tool cho mỗi lần quyết định.
- Parallelization — bằng chứng: có ≥2 subtask độc lập dữ liệu (không cái nào 
 cần output của cái kia) và mỗi subtask tốn latency đáng kể.
- Cross-checking — bằng chứng: lỗi hiện tại là loại "sai một cách thuyết phục", 
 và bạn có cách để agent thứ hai phát hiện ra (khác model, khác nguồn dữ liệu). Nếu agent thứ hai 
 chỉ là bản sao của agent thứ nhất, nó sẽ gật đầu đồng ý với chính lỗi đó.

#### 2 · Quy tắc 80% — cách áp dụng cho đúng

Ngưỡng 80% không phải hằng số vật lý; nó là cách nói rằng **bạn phải đo baseline trước**. 
 Quy trình đúng:

1. Xây eval set (30–80 case) cho bài toán của bạn.
2. Chạy single agent → được con số accuracy X.
3. Nếu X đã cao, phần lỗi còn lại thường là ambiguity trong đề bài hoặc nhãn eval sai, 
 chứ không phải thiếu agent. Thêm agent lúc này chỉ tăng cost mà không đụng được vào nguyên nhân.
4. Nếu X thấp, hãy phân loại lỗi trước: lỗi retrieval → sửa RAG; lỗi chọn tool → sửa 
 tool description; lỗi lý luận nhiều bước → lúc này mới cân nhắc tách agent.

context.md

một LangGraph workflow có state

"Bài toán check-in là workflow xác định, có DB làm ground truth. 
 Bottleneck của tôi là grounding và validation, không phải specialization. Tôi đo intent accuracy 
 và tool-selection accuracy trước; chỉ khi single-graph không vượt ngưỡng thì việc thêm agent mới 
 được biện minh."

#### 3 · "Bag of Agents" — phản mẫu số một

Là khi bạn có nhiều agent nhưng không có *decomposition rõ ràng*: ranh giới trách nhiệm chồng 
 lấn, không ai sở hữu kết quả cuối, và không có điều kiện dừng. Triệu chứng dễ nhận:

- Hai agent trở lên có mô tả nhiệm vụ mà bạn không phân biệt được bằng một câu.
- Không trả lời được câu "agent nào chịu trách nhiệm nếu output cuối sai?".
- Không có max_iterations hoặc điều kiện dừng tường minh.

### Slide 7 Ví dụ thực tiễn — bảng 6 use case

> Trích slide (rút gọn) 
>  Customer support triage — Triage agent route sang Billing/Refund/FAQ agent (OpenAI Agents SDK handoffs). "Đây là routing pattern dễ hiểu nhất; sai route thì user nhận câu trả lời sai." 
>  Code review assistant — Planner chia task, Code agent sửa, Test agent chạy test, Reviewer critique (GitHub Agent HQ). "Hữu ích khi cần plan–implement–verify, nhưng phải có test/CI làm ground truth." 
>  Research report — Searcher / Analyst / Writer / Critic (Anthropic workflows). "Phù hợp lab hôm nay vì dễ so sánh single vs multi-agent theo quality, latency, cost." 
>  Enterprise workflow — ADK agent teams + tools + observability. "Production không chỉ là prompt: cần deploy, evaluate, trace, auth, guardrails." 
>  Role-based automation — CrewAI crews: role, goal, tools, task. 
>  Conversational collaboration — AutoGen group chat. "Dùng để minh hoạ debate, human-in-loop, multi-turn coordination." 
>  Câu hỏi bắt buộc: "agent roles là gì? shared state chứa gì? failure mode nguy hiểm nhất là gì?"

Ba câu hỏi ở cuối slide chính là **template thiết kế** — mọi hệ multi-agent đều phải trả lời 
 được ba câu này trước khi viết dòng code đầu tiên. Áp dụng thử cho từng use case:

| Use case | Roles | Shared state chứa gì | Failure mode nguy hiểm nhất |
| --- | --- | --- | --- |
| Support triage | Triage → Billing / Refund / FAQ | intent, customer_id, ticket history | Mis-route im lặng: refund bị đẩy sang FAQ, khách nhận link help center thay vì tiền |
| Code review | Planner, Coder, Tester, Reviewer | diff, test results, review comments | Coder tự đánh giá code mình — không có test làm ground truth thì cả hệ tự khen nhau |
| Research report | Searcher, Analyst, Writer, Critic | sources[], insights[], draft, critique | Writer bịa nguồn khi Analyst trả về ít insight; citation trỏ tới tài liệu không tồn tại |
| Enterprise workflow | Agent team + tools | business entities, audit log | Thiếu auth/guardrail: agent thao tác dữ liệu ngoài quyền hạn |
| Role-based (CrewAI) | role + goal + tools + task | task outputs chuyền tay | Role chồng lấn → hai agent làm cùng một việc, tốn đôi cost |
| Group chat (AutoGen) | N agent hội thoại tự do | toàn bộ transcript | Không có điều kiện dừng → chat vô hạn, đốt token |

chính là

mis-route im lặng

context.md

intent accuracy + precision/recall/F1

### Slide 8 Hoạt động 1 — Single hay multi?

> Trích slide 
>  "Nhiệm vụ nhóm (8 phút): 1. Với mỗi task, chọn: single agent, workflow, hay multi-agent. 2. Giải thích bottleneck chính: accuracy, latency, cost, hay ownership. 3. Nêu ít nhất 1 lỗi mới nếu dùng nhiều agent. 
>  Task: FAQ đơn giản; research report; refund workflow; code migration. 
>  Mục tiêu không phải chọn multi-agent càng nhiều càng tốt; mục tiêu là biết khi nào KHÔNG nên dùng. "

Chú ý lựa chọn **ba mức**, không phải hai: *single agent* / *workflow* / *multi-agent*. "Workflow" là mức ở giữa và cũng là mức bị bỏ quên nhiều nhất — các bước do *bạn* viết cứng, LLM chỉ điền vào chỗ trống. Đa số bài toán doanh nghiệp dừng ở mức này.

**Đáp án đề xuất cho 4 task:**

| Task | Chọn | Bottleneck | Lỗi mới nếu dùng nhiều agent |
| --- | --- | --- | --- |
| FAQ đơn giản | Single agent (+ RAG) | Accuracy của retrieval, không phải reasoning | Thêm agent chỉ thêm latency cho câu hỏi 1 câu là xong; user cảm nhận rõ độ trễ |
| Research report | Multi-agent (hoặc orchestrator-workers) | Latency (nhiều nguồn) + quality (cần fact-check) | Writer tổng hợp từ context bị cắt xén → bịa nguồn; các searcher trùng nhau, tốn cost |
| Refund workflow | Workflow — các bước cứng, LLM chỉ trích xuất | Ownership & auditability: tiền thật, cần log ai duyệt | Không xác định được agent nào ra quyết định hoàn tiền → không audit được, rủi ro compliance |
| Code migration | Multi-agent có test làm ground truth | Accuracy trên quy mô lớn; cần vòng lặp verify | Coder và Reviewer cùng một model → cùng blind spot, cùng bỏ sót một lỗi |

business transaction

ownership và audit

context.md

"LLM quyết định intent / tool / routing; business tool thực thi 
 hành động đã được validate"

### Slide 9 MAST — lỗi đến từ thiết kế hệ thống

> Trích slide 
>  " 14 failure modes identified · 3 nhóm lỗi: spec, alignment, verification · 150+ tasks được phân tích. 
>  Why Do Multi-Agent LLM Systems Fail? (arXiv:2503.13657) chỉ ra nhiều lỗi đến từ 
>  specification / system design, inter-agent misalignment, và 
>  verification / termination. Vì vậy cần define roles, stop condition, và rubric trước khi code."

Thông điệp quan trọng nhất của cả bài: **phần lớn lỗi multi-agent không phải lỗi model**. 
 Đổi sang model mạnh hơn không sửa được chúng. Ba nhóm lỗi, diễn giải chi tiết:

| Nhóm | Bản chất | Ví dụ cụ thể | Cách phòng |
| --- | --- | --- | --- |
| Specification (thiết kế hệ thống) | Vai trò mơ hồ, nhiệm vụ chồng lấn, agent không tuân thủ ràng buộc của đề bài | Analyst được giao "phân tích dữ liệu" nhưng cũng tự đi search vì thấy dữ liệu thiếu → trùng việc với Searcher, mâu thuẫn kết quả | Mỗi agent: 1 câu mô tả nhiệm vụ, danh sách tool đóng, và ghi rõ không được làm gì |
| Inter-agent misalignment | Mất context khi bàn giao, agent nói lệch nhau, phớt lờ input của agent khác | Searcher trả 8 nguồn, nhưng handoff chỉ mang theo 3 dòng tóm tắt; Writer viết kết luận mà nguồn không hề nói | Handoff mang tham chiếu đến state đầy đủ, không phải chỉ tóm tắt; schema cố định cho mỗi lần bàn giao |
| Verification & termination | Dừng quá sớm, dừng quá muộn, hoặc verify hời hợt | Reviewer trả về "Looks good" cho mọi input; hoặc supervisor route A→B→A vô hạn | max_iterations, timeout, và rubric verify có thể fail — verifier phải có khả năng nói "không đạt" kèm lý do |

Vòng đời một phiên multi-agent — và chỗ hỏng của mỗi nhóm lỗi 1 · Specification 2 · Misalignment 3 · Verification Vai trò mơ hồ, nhiệm vụ chồng lấn, phớt lờ ràng buộc Context mất khi bàn giao, agent nói lệch nhau Dừng sớm / không dừng, verify hời hợt TRƯỚC khi code TRONG lúc chạy LÚC kết thúc Fix: 1 câu nhiệm vụ /agent, tool đóng, ghi rõ điều cấm Fix: handoff theo schema, ràng buộc giữ nguyên văn Fix: max_iterations, timeout, rubric có quyền nói "không đạt" Không nhóm nào trong ba nhóm này được sửa bằng cách đổi sang model mạnh hơn — đó là toàn bộ thông điệp của bài MAST.

Hình 3 — Ba nhóm lỗi MAST định vị theo vòng đời (slide 9).

(1) define roles → (2) define stop condition → 
 (3) define rubric → (4) mới code

- Specification: node "Extract visitor info" và node "Collect missing information" cùng 
 đụng đến visitor_info — nếu không định nghĩa rõ ai được ghi field nào, bạn sẽ có hai 
 node ghi đè nhau.
- Misalignment: node RAG trả về citation nhưng node trả lời cuối chỉ nhận đoạn text đã tóm 
 tắt → citation không khớp nội dung. Đây đúng là "context loss across handoffs".
- Termination: vòng lặp hỏi lại thông tin thiếu ( missing_fields ) bắt 
 buộc phải có giới hạn số lượt, nếu không kiosk sẽ hỏi mãi một khách không chịu cung cấp số 
 điện thoại. Giới hạn đó chính là ngòi nổ cho requires_human = True.

#### Ô kiểm tra — Chương 1

Trả lời thành tiếng hoặc viết ra trước khi mở đáp án. Việc *cố nhớ lại* mới tạo ra trí nhớ — 
 đọc lại thì không.

**1.** Một nhóm khoe: "hệ của bọn em có 5 agent nên thông minh hơn hệ 1 agent." 
 Câu này sai ở chỗ nào? Hiểu

#### Đáp án

Sai ở giả định ngầm rằng *số lượng agent* là thước đo năng lực. Thêm agent không thêm tri thức — 
 các agent vẫn dùng cùng model, cùng dữ liệu. Thứ nó thêm vào là **khả năng chuyên môn hoá** (prompt hẹp hơn, ít tool hơn cho mỗi quyết định) và **một loại lỗi hoàn toàn mới**: 
 lỗi nằm *giữa* các agent — handoff, context loss, tranh chấp state.

Câu hỏi đúng để hỏi lại nhóm đó: *"Baseline 1 agent của các bạn đạt bao nhiêu, và 5 agent đạt bao nhiêu?"* Nếu họ chưa đo baseline, họ chưa biết mình có thông minh hơn hay không.

**2.** Single agent của bạn đạt 62% trên eval set. Có nên thêm agent không? Áp dụng

#### Đáp án

**Chưa biết — và đó là câu trả lời đúng.** 62% dưới ngưỡng nên "được phép" cân nhắc, 
 nhưng trước hết phải **phân loại 38% lỗi kia**:

• Lỗi retrieval (không tìm ra tài liệu đúng) → sửa RAG. Thêm agent không giúp gì. 
 • Lỗi chọn tool → sửa mô tả tool. Thêm agent không giúp gì. 
 • Lỗi định dạng / schema → thêm validation. Thêm agent không giúp gì. 
 • Lỗi lý luận nhiều bước, prompt đã quá tải → *đây* mới là chỗ tách agent có lý.

Nhảy thẳng sang multi-agent khi lỗi thuộc ba loại đầu là cách chắc chắn để tốn gấp ba tiền 
 mà accuracy vẫn 62%.

**3.** Trong ba nhóm lỗi MAST, nhóm nào *không* sửa được bằng cách viết prompt tốt hơn? Phân tích

#### Đáp án

**Cả ba, ở mức độ khác nhau — nhưng nhóm 3 (verification & termination) thì gần như hoàn toàn không.**

Prompt hay có thể giảm nhóm 1 (specification) và nhóm 2 (misalignment) phần nào. 
 Nhưng "supervisor lặp vô hạn" không phải vấn đề ngôn từ — nó là vấn đề **kiến trúc**. 
 Không câu prompt nào ngăn được một vòng lặp; chỉ có bộ đếm và điều kiện dừng trong code mới ngăn được.

Đây là lý do slide 9 nói lỗi đến từ *system design*: có những lớp lỗi mà lời lẽ không chạm tới được.

---

<!-- chiron-source-span: {"source_span_id":"a9e3cb03-2873-5915-89dd-4b45a80f76bb","locator":{"kind":"html_section","section_id":"c2","order":4,"heading":"02 5 Agentic Workflow Patterns (Anthropic)","source_file":"track-3-day-20.html"},"checksum":"666e2e91c6086da4f4f27bb2d95abd3e1c27dc376636c120e2549165a5b354ca"} -->

## 02 5 Agentic Workflow Patterns (Anthropic)

Slide 10–13: thang leo từ đơn giản đến phức tạp.

### Slide 10 Section divider

> Trích slide 
>  "02 — 5 Agentic Workflow Patterns (Anthropic). Từ đơn giản đến phức tạp — escalate dần"

Năm pattern này lấy từ bài *Building Effective Agents* (Anthropic, 12/2024). Điểm cốt lõi 
 của bài gốc: bốn trong năm pattern thực chất là **workflow** (đường đi do người viết cứng), 
 chỉ pattern cuối mới tiến gần tới *agent* thật sự (LLM tự quyết định đường đi).

### Slide 11 5 Patterns — Escalation Ladder

> Trích slide 
>  "1. Prompt Chaining (Sequential, validate each) → 2. Routing (Classify, route) → 3. Parallel (Sectioning, Voting) → 4. Orchestrator-Workers (Supervisor delegates) → 5. Evaluator-Optimizer (Generate, critique loop). Complexity + Failure modes tăng. 
>  Start simplest. Only add agents when measurably needed. Thử Prompt Chaining trước. Chỉ escalate khi có bằng chứng cần. 
>  Sectioning: split tasks → parallel workers. Voting: same task → multiple LLMs → aggregate."

tuần tự + gate phân loại → nhánh sectioning / voting phân rã runtime sinh → chấm → sửa 1 2 3 4 5 Prompt Chaining Routing Parallel Orchestrator –Workers Evaluator –Optimizer Complexity + failure modes tăng

Hình 1 — Thang leo 5 pattern (slide 11).

và

Giải thích từng bậc thang, kèm dấu hiệu nhận biết "khi nào cần leo lên bậc tiếp theo":

#### Bậc 1 · Prompt Chaining

Chia một task thành các bước tuần tự cố định, output bước trước là input bước sau, và **chèn kiểm tra (gate) giữa các bước**. Đây là pattern bị đánh giá thấp nhất nhưng 
 giải quyết được nhiều việc nhất.

```text
Input → [LLM: trích xuất] → gate: schema hợp lệ? → [LLM: viết] → gate: đủ mục? → Output
                                     │ fail                            │ fail
                                     └────────► retry / escalate ◄─────┘
```

*Leo lên bậc 2 khi:* input có nhiều loại rõ rệt và mỗi loại cần cách xử lý khác nhau — nhồi 
 hết vào một chuỗi làm prompt phình to và chất lượng tụt.

#### Bậc 2 · Routing

Phân loại input trước, rồi gửi tới handler chuyên biệt. Ưu điểm lớn nhất: mỗi handler được tối ưu 
 riêng mà không làm hỏng handler khác — điều bất khả thi khi tất cả nằm trong một prompt.

*Leo lên bậc 3 khi:* có nhiều subtask độc lập và latency là vấn đề.

#### Bậc 3 · Parallel — hai biến thể khác nhau về bản chất

phần khác nhau

Mục tiêu: giảm latency.

Cùng một task

Mục tiêu: tăng độ tin cậy.

**Đừng nhầm hai cái này** — đây là câu hỏi quiz kinh điển. Sectioning chia *công việc*; 
 Voting nhân bản *cùng một công việc*. Sectioning làm nhanh hơn; Voting làm chậm hơn nhưng chắc hơn.

#### Bậc 4 · Orchestrator-Workers (Supervisor)

Khác Parallel ở chỗ: số lượng và loại subtask **không biết trước** — LLM orchestrator 
 tự phân rã tại runtime. Đây là chỗ bắt đầu có "agentic" thật sự, và cũng là chỗ bắt đầu có 
 routing loop.

#### Bậc 5 · Evaluator-Optimizer

Một LLM sinh ra kết quả, một LLM khác chấm theo rubric và trả về feedback, vòng lặp cho tới khi đạt 
 hoặc hết số vòng. Chỉ hiệu quả khi thoả **hai điều kiện**: (a) có tiêu chí đánh giá rõ ràng, 
 và (b) feedback thật sự làm bản sau tốt hơn bản trước. Nếu thiếu (a), evaluator sẽ trả về "khá tốt rồi" 
 ở mọi vòng.

context.md

bậc 2 (Routing) lồng trong bậc 1 (Prompt Chaining)

bậc 3 Sectioning

Áp dụng

### Slide 12 Hoạt động 2 — Pattern Card Sorting

> Trích slide 
>  "Chia nhóm 3 người, mỗi nhóm nhận 1 case: ■ Tổng hợp review khách hàng từ 1.000 comment ■ Xử lý ticket refund/billing/technical support ■ Viết báo cáo thị trường có fact-check nguồn ■ Migrate codebase và đảm bảo test pass. 
>  Nhiệm vụ: chọn 1 trong 5 patterns, vẽ flow trong 4 phút. Mỗi nhóm nói 30 giây: pattern, lý do, metric đo thành công, failure guard. 
>  Không được mặc định "supervisor cho mọi thứ". Hãy chứng minh pattern đơn giản hơn chưa đủ. "

**Đáp án đề xuất** — chú ý mỗi case ứng với đúng một pattern, đây là thiết kế có chủ ý 
 của giảng viên:

| Case | Pattern | Lý do | Metric thành công | Failure guard |
| --- | --- | --- | --- | --- |
| 1.000 comment | Parallel — Sectioning | 1.000 comment là các phần độc lập; không cần suy luận chéo | Latency tổng, cost/comment, độ ổn định của tập theme khi chia lô khác nhau | Giới hạn concurrency theo rate limit; retry lô lỗi; kiểm tra merge không mất comment nào |
| Ticket refund/billing/tech | Routing | Ba loại rõ rệt, mỗi loại có tool và quy định riêng | Routing accuracy, đặc biệt recall của nhánh refund (bỏ sót refund là tốn tiền thật) | Ngưỡng confidence; dưới ngưỡng thì chuyển người thật thay vì đoán |
| Báo cáo thị trường có fact-check | Evaluator-Optimizer (hoặc Orchestrator + Critic) | Cần vòng critique để mọi khẳng định có nguồn | Citation coverage, unsupported-claim rate | max_rounds = 2–3; evaluator phải có quyền fail kèm lý do cụ thể |
| Code migration | Orchestrator-Workers + test làm ground truth | Không biết trước bao nhiêu file cần sửa → phân rã tại runtime | % test pass, số file migrate xong, số lần rollback | Test suite chạy sau mỗi thay đổi; giới hạn số lần thử mỗi file; DLQ cho file thất bại |

trông có vẻ

for

### Slide 13 Routing Pattern — Cost Optimization

> Trích slide 
>  "Routing — Classify input rồi chuyển đến specialized handler. Easy queries dùng small model, hard queries dùng large model. 
>  ■ 70% queries easy = small model (GPT-4o-mini) ■ 30% queries hard = large model (GPT-4o) ■ Giảm 50%+ chi phí tổng thể 
>  Khi workload có bimodal difficulty — nhiều query đơn giản + ít query phức tạp. 
>  Routing chỉ hiệu quả khi phân loại chính xác. Sai phân loại = query hard gửi cho small model = kết quả kém. "

Slide này biến routing từ "kỹ thuật tổ chức code" thành **đòn bẩy chi phí**. Hãy làm rõ 
 phép tính, vì con số "giảm 50%+" chỉ đúng với một số giả định cụ thể.

#### Phép tính minh hoạ

Giả sử 10.000 query/tháng, mỗi query ~2.000 token vào + 500 token ra. Lấy một cặp giá tương đối 
 (model nhỏ rẻ hơn model lớn khoảng 15–20 lần — hãy thay bằng bảng giá thật tại thời điểm bạn tính):

| Phương án | Cách chạy | Chi phí tương đối |
| --- | --- | --- |
| Không routing | 10.000 query × model lớn | 100% |
| Có routing | 7.000 × model nhỏ (≈1/16 giá) + 3.000 × model lớn + 10.000 lượt phân loại bằng model nhỏ | ≈ 35–40% |

**Chi tiết dễ quên:** bản thân bước phân loại cũng tốn tiền. Nó chỉ rẻ khi bạn phân loại 
 bằng model nhỏ với prompt ngắn (hoặc bằng classifier không phải LLM). Nếu bạn phân loại bằng chính 
 model lớn, bạn đã trả full giá cho mọi query rồi mới bắt đầu tiết kiệm — lợi ích bốc hơi.

#### Tương tác Máy tính chi phí Routing

Kéo thanh trượt để thấy khoản tiết kiệm của routing bốc hơi ra sao khi tỷ lệ phân loại sai tăng — 
 và quan trọng hơn: thiệt hại thật không nằm ở tiền.

Giữ nguyên mọi thứ, chỉ kéo **"% query khó bị phân loại nhầm" từ 5% lên 40%** — 
 tức là cứ 5 query khó thì 2 bị đẩy nhầm sang model nhỏ. Đoán trước:

1. Ô Tiết kiệm sẽ tụt bao nhiêu điểm phần trăm?
2. Ô Chi phí có routing sẽ tăng hay giảm?

#### Kéo xong rồi mở

**Tiết kiệm chỉ tụt từ 64% xuống 63%** — đúng 1 điểm phần trăm. 
 Chi phí nhích từ $36 lên $37. Gần như không có gì xảy ra trên hoá đơn.

**Vì sao:** query bị phân loại nhầm được gửi cho model *rẻ hơn*. Sai lầm này 
 làm bạn *tiết kiệm* tiền chứ không tốn thêm. Chỉ phần retry mới tốn, và nó nhỏ.

**Nhưng nhìn ô cuối:** số query khó bị model nhỏ trả lời nhảy từ 150 lên 1.200 mỗi tháng — **tăng 8 lần**. 
 Đó là 1.200 người dùng nhận câu trả lời kém mỗi tháng.

**Bài học mang đi:** hoá đơn API không phải hệ thống cảnh báo chất lượng. 
 Một hệ routing đang hỏng nặng trông y hệt một hệ routing đang chạy tốt, nếu bạn chỉ nhìn cost. 
 Muốn biết, phải đo *routing accuracy* trên một tập có nhãn — đúng thứ [slide 13](#s13) cảnh báo bằng một câu ngắn mà rất dễ đọc lướt qua.

- **Control - Query / tháng 10.000**: min `1000`, max `100000`, step `1000`, default `10000`

- **Control - % query dễ 70%**: min `0`, max `100`, step `5`, default `70`

- **Control - Model lớn đắt gấp 16×**: min `2`, max `40`, step `1`, default `16`

- **Control - % query khó bị phân loại nhầm 5%**: min `0`, max `60`, step `1`, default `5`

Không routing

—

mọi query dùng model lớn

Có routing

—

gồm cả chi phí phân loại

Tiết kiệm

—

so với baseline

Query khó bị model nhỏ trả lời

—

mỗi tháng — thiệt hại thật

Phân loại Model nhỏ Model lớn ⚠ Lãng phí do retry

#### Xem dạng bảng



#### Giả định của mô hình — sửa được, đừng tin mù

- 1 lượt model lớn = $0,010 (2.000 token vào × $2,5/M + 500 token ra × $10/M). Thay bằng bảng giá thật của bạn.
- 1 lượt model nhỏ = giá model lớn ÷ hệ số "đắt gấp".
- Bước phân loại tốn 25% một lượt model nhỏ (prompt ngắn hơn nhiều).
- Query khó bị phân loại nhầm được giả định là có phát hiện ra và retry bằng model lớn → lượt model nhỏ ban đầu là lãng phí thuần.
- Trong thực tế phần lớn misroute không bị phát hiện — nên ô "Query khó bị model nhỏ trả lời" mới là con số đáng lo, không phải ô tiết kiệm.

#### "Bimodal difficulty" nghĩa là gì

Phân phối độ khó có *hai đỉnh*: một cụm rất dễ, một cụm rất khó, ít cái ở giữa. Routing ăn tiền 
 ở đúng hình dạng phân phối này. Nếu độ khó phân bố đều (đa số query trung bình), ranh giới phân loại 
 mờ, tỷ lệ sai tăng, và lợi ích tiết kiệm bị nuốt bởi chi phí sửa lỗi.

không

- Hard bị gán nhãn easy → model nhỏ trả lời sai → user chịu hậu quả. Đắt.
- Easy bị gán nhãn hard → model lớn trả lời đúng, chỉ tốn thêm tiền. Rẻ.

thiên về "hard"

- Dễ (~75%): "giờ làm việc?", "gửi xe ở đâu?", "CSKH tầng mấy?" — chỉ cần intent 
 classification + RAG một lượt. Hoàn toàn dùng được model nhỏ.
- Khó (~25%): trích xuất thông tin khách từ câu nói lẫn lộn ("em là Lan, hẹn anh 
 Minh phòng kỹ thuật lúc 2h chiều nhưng chắc trễ 15 phút"), giải quyết trường hợp nhiều appointment 
 trùng, xử lý yêu cầu mơ hồ. Cần model lớn.

node Intent Router luôn dùng model nhỏ

node Visitor Information Extractor dùng model lớn

context.md

cost/session

#### Ô kiểm tra — Chương 2

Ba câu này bao trọn phần thang leo 5 pattern.

**1.** Sectioning và Voting đều nằm trong bậc "Parallel". Khác nhau ở đâu, 
 và mỗi cái tối ưu điều gì? Hiểu

#### Đáp án

**Sectioning chia công việc** — mỗi worker làm một *phần khác nhau*, rồi ghép lại. 
 Tối ưu **latency**. Ví dụ: 1.000 comment chia 10 lô.

**Voting nhân bản công việc** — nhiều LLM làm *cùng một việc*, rồi tổng hợp. 
 Tối ưu **độ tin cậy**. Ví dụ: "đoạn code này có lỗ hổng không?" hỏi 3 lần.

**Mẹo nhớ:** Sectioning làm bạn *nhanh hơn*; Voting làm bạn *chậm hơn nhưng 
 chắc hơn*. Nếu bạn nói được một pattern làm chậm đi mà vẫn đáng dùng, bạn đã hiểu đúng nó.

**2.** Bạn phải viết báo cáo thị trường, mọi khẳng định đều cần có nguồn kiểm chứng. 
 Chọn pattern nào — và tại sao *không* chọn Supervisor? Áp dụng

#### Đáp án

**Evaluator-Optimizer** (bậc 5). Bài toán cần một vòng lặp: viết → chấm theo rubric 
 ("mọi khẳng định có nguồn chưa?") → sửa. Hai điều kiện cần đều thoả: tiêu chí đánh giá rõ ràng, 
 và feedback thực sự cải thiện bản sau.

**Vì sao không Supervisor:** Supervisor giải bài toán *"gọi ai làm gì tiếp theo"* khi không biết trước cần bao nhiêu subtask. Ở đây bạn *biết chính xác* các bước: 
 thu thập nguồn → viết → fact-check → sửa. Không có gì để phân rã tại runtime. 
 Dùng Supervisor ở đây là trả tiền cho một LLM để quyết định một thứ bạn đã biết từ trước.

**3.** Slide 13 nói routing "giảm 50%+ chi phí". Những điều kiện nào phải đúng 
 để con số đó thành hiện thực? Đánh giá

#### Đáp án

Bốn điều kiện, thiếu một là con số sụp:

**① Workload thật sự bimodal** — nhiều query rất dễ, ít query rất khó. 
 Nếu đa số ở mức trung bình, ranh giới phân loại mờ và tỷ lệ sai tăng. 
 **② Bước phân loại phải rẻ** — dùng model nhỏ với prompt ngắn. Phân loại bằng model lớn 
 là đã trả full giá trước khi bắt đầu tiết kiệm. 
 **③ Chênh lệch giá giữa hai model đủ lớn** — kéo thanh "đắt gấp" về 2× trong [máy tính chi phí](#m-route) để thấy phần tiết kiệm teo lại thế nào. 
 **④ Model nhỏ thật sự làm được query dễ** — nếu không, bạn không tiết kiệm, bạn chỉ 
 đang trả lời tệ đi với giá rẻ hơn.

---

<!-- chiron-source-span: {"source_span_id":"0f67ba34-54c7-5868-a2d0-05254ea052fa","locator":{"kind":"html_section","section_id":"c3","order":5,"heading":"03 Supervisor Pattern — Orchestration","source_file":"track-3-day-20.html"},"checksum":"9ebc3cbcc99ce415396cad279fef1440bf636cda1d25b3d70cb681547faf66eb"} -->

## 03 Supervisor Pattern — Orchestration

Slide 14–16: kiến trúc hub-spoke và cài đặt bằng LangGraph.

### Slide 14 Section divider

> Trích slide "03 — Supervisor Pattern — Orchestration. Hub-spoke delegation với LangGraph"

**Hub-spoke** (trục bánh xe): mọi luồng đi qua tâm. Đối lập với nó là *mesh* (agent nói chuyện trực tiếp với nhau, kiểu AutoGen group chat). Hub-spoke đắt hơn một chút về số lượt 
 LLM, nhưng đổi lại bạn có **một điểm duy nhất để log, để đặt guard, và để debug** — 
 đó là lý do nó được gọi là "most practical" ở slide tổng kết.

### Slide 15 Hub-Spoke Architecture

> Trích slide 
>  "Supervisor (LLM Router) → delegate → Search Agent / Analysis Agent / Writer Agent / Code Agent. Shared State: messages, worker_results, final_answer. 
>  Supervisor — LLM router: nhận task, decompose, route đến workers, aggregate results. 
>  ■ Mỗi worker là node riêng với own tools ■ Supervisor quyết định: gọi ai, theo thứ tự nào ■ Cost insight: cheap model cho routing, expensive model cho workers "

SUPERVISOR decompose · route · aggregate model rẻ worker xong → quay lại hub (mọi vòng đều đi qua tâm) delegate Search Analysis Writer Code tool riêng tool riêng tool riêng tool riêng 4 worker · model mạnh · prompt hẹp — không nói chuyện trực tiếp với nhau SHARED STATE messages · next_worker · worker_results · final_answer · steps 1 nơi để log

Hình 2 — Hub-spoke (slide 15).

một

steps

#### Bốn nhiệm vụ của supervisor

1. Nhận task — đọc yêu cầu người dùng.
2. Decompose — chia thành subtask. Đây là phần khó nhất và cũng là nguồn lỗi 
 "specification" của MAST.
3. Route — chọn worker tiếp theo. Nên ép bằng tool call chứ không parse text.
4. Aggregate — gộp worker_results thành final_answer.

#### "Cheap model cho routing" — vì sao hợp lý

Routing là bài toán **phân loại trên tập hữu hạn nhãn** (gọi worker nào trong 4 worker), 
 không phải bài toán sinh nội dung. Model nhỏ làm tốt việc này khi mô tả worker rõ ràng. Trong khi đó 
 worker phải thực sự viết/phân tích — chỗ đó mới cần model mạnh. Vì supervisor bị gọi *nhiều lần* (mỗi worker xong lại gọi lại), tiết kiệm ở đây được nhân lên.

Cái bẫy ngược lại Nếu mô tả worker mơ hồ ("agent xử lý dữ liệu" vs "agent phân tích dữ liệu"), model nhỏ sẽ route sai 
 thường xuyên và bạn kết luận nhầm rằng "model nhỏ không đủ". Sửa mô tả worker trước, đổi model sau — 
 routing accuracy phụ thuộc vào chất lượng mô tả nhiều hơn vào kích thước model.

### Slide 16 SupervisorState — LangGraph Implementation

> Trích slide 
>  " class SupervisorState(TypedDict): messages, next_worker, worker_results, final_answer … graph = StateGraph(SupervisorState); graph.add_node("supervisor", supervisor); graph.add_node("search", search_agent) … 
>  State gồm 4 thành phần: 1. messages: conversation context 2. next_worker: ai được gọi tiếp 3. worker_results: output từ mỗi worker 4. final_answer: kết quả tổng hợp 
>  Failure modes: #1 infinite routing loop (A → B → A). #2 wrong worker selection. Cần max iterations guard. "

#### Vì sao đúng 4 trường này

| Trường | Vai trò | Nếu thiếu thì sao |
| --- | --- | --- |
| messages | Ngữ cảnh hội thoại chung | Worker mất context, không biết user thật sự hỏi gì → chính là "context loss" của MAST |
| next_worker | Quyết định routing của supervisor | Không có edge có điều kiện; graph không biết đi đâu tiếp |
| worker_results | dict kết quả theo tên worker | Không aggregate được; và không biết worker nào đã chạy → dễ gọi lặp |
| final_answer | Đầu ra tổng hợp | Không có ranh giới rõ giữa "đang làm" và "đã xong" |

Chú ý `worker_results` là `dict[str, str]` chứ không phải `list`: 
 khoá theo tên worker giúp trả lời ngay câu "worker này chạy chưa?" — vừa là dữ liệu, vừa là *bộ nhớ chống lặp*.

#### Cài đặt tối thiểu nhưng đủ guard

```text
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

class SupervisorState(TypedDict):
    messages: list
    next_worker: str
    worker_results: dict[str, str]
    final_answer: str
    steps: int                      # ← guard: đếm số lần route

MAX_STEPS = 8                       # chặn infinite loop (failure mode #1)

def supervisor(state: SupervisorState):
    if state["steps"] >= MAX_STEPS:                 # hết ngân sách vòng lặp
        return {"next_worker": "FINISH"}
    done = list(state["worker_results"])            # worker đã chạy
    resp = llm_small.invoke(                        # model rẻ cho routing
        system=f"Route to next worker. Đã xong: {done}. "
               f"Trả về FINISH khi đủ thông tin.",
        tools=[search, analyze, write],
        messages=state["messages"],
    )
    return {"next_worker": resp.tool, "steps": state["steps"] + 1}

def route(state) -> Literal["search", "analyze", "write", "__end__"]:
    return END if state["next_worker"] == "FINISH" else state["next_worker"]

g = StateGraph(SupervisorState)
g.add_node("supervisor", supervisor)
g.add_node("search", search_agent)
g.add_node("analyze", analysis_agent)
g.add_node("write", writer_agent)
g.set_entry_point("supervisor")
g.add_conditional_edges("supervisor", route)
for w in ("search", "analyze", "write"):
    g.add_edge(w, "supervisor")     # ← mỗi worker xong quay lại hub
app = g.compile()
```

Ba chi tiết đáng chú ý so với code trên slide:

- steps + MAX_STEPS — guard mà slide yêu cầu. Không có nó, một lỗi prompt 
 nhỏ đủ để đốt hết quota trong vài phút.
- Đưa done (danh sách worker đã chạy) vào prompt — cách rẻ nhất để chặn A→B→A, vì 
 supervisor nhìn thấy mình đã gọi ai rồi.
- add_edge(worker, "supervisor") — chính là hình dạng hub-spoke: mọi worker quay về tâm, 
 không nói chuyện trực tiếp với nhau.

Ba lớp phòng thủ

max_iterations

#### Tương tác Ngân sách vòng lặp — vì sao max_iterations không phải tuỳ chọn

Mỗi lần supervisor được gọi lại, nó phải nạp lại toàn bộ kết quả worker đã tích luỹ. 
 Chi phí mỗi lượt *tăng dần*, nên tổng chi phí tăng theo hàm bậc hai — không tuyến tính.

Với `max_iterations = 8`, một bug làm supervisor lặp vô hạn sẽ chạy khoảng 200 lượt 
 trước khi chạm rate limit. Đoán trước: **hệ không có guard tốn gấp bao nhiêu lần hệ có guard?**

Phản xạ tự nhiên là lấy 200 ÷ 8 = **25×**. Hãy viết con số bạn đoán ra, rồi kéo.

#### Kéo xong rồi mở

**Đáp án: 453×**, không phải 25×. Lệch **18 lần** so với phép chia trực giác.

**Vì sao:** phép chia 200÷8 ngầm giả định *mọi lượt tốn như nhau*. Nhưng lượt 
 routing thứ k phải nạp lại toàn bộ kết quả worker đã tích luỹ, nên nó đắt hơn lượt thứ k−1. 
 Tổng của một dãy tăng dần không tỉ lệ với số phần tử — nó tỉ lệ với *bình phương*. 
 Nhìn biểu đồ cột: các cột không cao bằng nhau, chúng dốc lên.

**Bài học mang đi:** trực giác tuyến tính là sai lầm phổ biến nhất khi ước lượng chi phí 
 agent. Bất cứ khi nào một vòng lặp *tích luỹ context*, hãy nghĩ "bậc hai", không phải "nhân lên". 
 Đây cũng là lý do `max_iterations` không phải một tuỳ chọn cấu hình — nó là cái van an toàn.

*Thử thêm:* kéo "context phình thêm mỗi lượt" về 0%. Tỷ lệ tụt về đúng 25× — 
 xác nhận rằng chính sự phình context, chứ không phải số vòng lặp, mới là thứ gây nổ chi phí.

- **Control - max_iterations 8**: min `1`, max `20`, step `1`, default `8`

- **Control - Context phình thêm mỗi lượt 60%**: min `0`, max `150`, step `10`, default `60`

Trần chi phí 1 phiên

—

phần supervisor, khi chạm guard

Nếu KHÔNG có guard

—

loop 200 lượt trước khi chạm rate limit

Đắt gấp

—

so với trần có guard

Trong ngân sách Bị guard chặn

#### Xem dạng bảng



#### Giả định của mô hình

- Lượt routing thứ k có input = base × (1 + g×(k−1)), với g là mức phình context.
- Base = 1.500 token vào + 100 token ra, giá model nhỏ ($0,15/M vào, $0,60/M ra) ≈ $0,00029/lượt.
- Chỉ tính phần supervisor. Chi phí worker không đổi theo số vòng nên không làm rõ được điểm này.
- "200 lượt" là con số minh hoạ cho việc loop chạy tới khi chạm rate limit — thực tế phụ thuộc hạn mức của bạn.

mô tả

CheckInState

context.md

messages

intent

visitor_info

appointment

missing_fields

confidence

requires_human

messages

worker_results

next_worker

intent

Thứ bạn nên bổ sung ngay: trường đếm vòng lặp.

```text
class CheckInState(TypedDict):
    ...
    clarify_attempts: int          # ← đếm số lần đã hỏi lại

MAX_CLARIFY = 2

def need_more_info(state):
    if not state["missing_fields"]:
        return "register"
    if state["clarify_attempts"] >= MAX_CLARIFY:
        return "escalate"          # hỏi 2 lần không xong → gọi lễ tân
    return "ask_clarification"
```

guard chống vòng lặp và cơ chế escalation là cùng một thứ.

#### Ô kiểm tra — Chương 3

Supervisor là pattern bạn nhiều khả năng phải cài đặt trong Lab 20.

**1.** Vì sao supervisor nên dùng model *rẻ*, còn worker dùng model mạnh? Hiểu

#### Đáp án

Vì hai bên làm hai *loại* bài toán khác nhau. Supervisor giải bài toán **phân loại trên tập hữu hạn nhãn** ("gọi worker nào trong 4 worker") — model nhỏ làm tốt 
 khi mô tả worker rõ ràng. Worker phải **thực sự sinh nội dung** — chỗ đó mới cần năng lực.

Và khoản tiết kiệm được *nhân lên*: supervisor bị gọi lại sau mỗi worker, nên nó là thành phần 
 chạy nhiều lần nhất trong hệ.

**2.** Viết ra ba lớp phòng thủ chống infinite routing loop, theo thứ tự nên cài đặt. Áp dụng

#### Đáp án

**① Bộ đếm cứng** — `steps` trong state + `MAX_STEPS`. 
 Cài trước tiên vì nó là thứ duy nhất *đảm bảo* dừng, không phụ thuộc vào việc LLM có ngoan không.

**② Đưa lịch sử vào prompt** — cho supervisor biết nó đã gọi những worker nào rồi. 
 Rẻ, và xử lý được đa số trường hợp trước khi chạm bộ đếm.

**③ Chặn gọi trùng** — so hash của (worker, tham số); nếu trùng lần gọi trước thì từ chối.

*Thứ tự quan trọng:* ① là cái van an toàn, ②③ là cái làm hệ chạy đẹp. Đừng bao giờ dựa 
 vào ②③ mà bỏ ①.

**3.** Supervisor của bạn liên tục route sai worker. Bạn thử theo thứ tự nào? Phân tích

#### Đáp án

**① Đọc lại mô tả worker.** Nếu hai mô tả mà bạn không phân biệt được bằng một câu, 
 model cũng không phân biệt được. Đây là nguyên nhân của đa số ca.

**② Thêm 2–3 ví dụ** vào prompt supervisor.

**③ Đo routing accuracy** trên một tập nhỏ có nhãn — để biết mình đang sửa cái gì, 
 thay vì cảm giác.

**④ Cuối cùng mới đổi model lớn hơn.**

*Sai lầm phổ biến là làm ngược từ ④.* Nó tốn tiền, che mất nguyên nhân thật, và bạn sẽ 
 gặp lại đúng lỗi đó khi thêm worker thứ 5.

---

<!-- chiron-source-span: {"source_span_id":"c442928d-0603-513c-a9bc-c26139aa04e8","locator":{"kind":"html_section","section_id":"c4","order":6,"heading":"04 Debate Agents — Adversarial Collaboration","source_file":"track-3-day-20.html"},"checksum":"679349fadfd4e6a682c3eb1b242899558ef5914bad68d3d0c5ddd9e6de772b3e"} -->

## 04 Debate Agents — Adversarial Collaboration

Slide 17–19: giảm hallucination bằng tranh luận có kiểm soát.

### Slide 17 Section divider

> Trích slide "04 — Debate Agents — Adversarial Collaboration. Giảm hallucination qua tranh luận có kiểm soát"

Từ khoá là **"có kiểm soát"**: số vòng cố định, vai trò cố định, và có judge quyết định 
 cuối. Tranh luận tự do không giới hạn là công thức đốt token.

### Slide 18 Debate Pattern

> Trích slide 
>  "Agent A (GPT-4o) và Agent B (Claude) → Answer A / Answer B → critique lẫn nhau → Judge → Synthesize → Final Answer. 
>  Flow: 1. Agent A & B answer independently 2. Critique nhau (adversarial) 3. Judge synthesize final answer. 
>  Debate giảm hallucination 15–25%. Hiệu quả nhất cho ambiguous queries, high-stakes decisions. 
>  "Collective delusion": cả hai đồng ý sai → Judge không catch. Fix: dùng diverse models. "

Bước 1 — trả lời ĐỘC LẬP (chạy song song, chưa ai thấy đáp án của ai) Agent A model nhà A Agent B model nhà B — khác training data Answer A Answer B critique chéo Bước 2 — mỗi bên tìm lỗi của bên kia Judge Bước 3 — synthesize Final Answer ⚠ Collective delusion A và B cùng model = cùng blind spot → Judge không catch được 5 lượt LLM tổng cộng nhưng chỉ 3 chặng tuần tự

Hình 4 — Debate với critique chéo (slide 18).

#### Vì sao bước "independently" ở đầu là bắt buộc

A và B phải trả lời **trước khi nhìn thấy đáp án của nhau**. Nếu B thấy đáp án của A rồi 
 mới trả lời, B bị *neo* (anchoring) vào lập luận của A — và bạn mất chính cái thứ mình đang mua: 
 hai góc nhìn độc lập. Đây là chi tiết cài đặt rất hay bị làm sai.

#### Vì sao "adversarial" hiệu quả

Sinh nội dung và phê bình nội dung là hai bài toán khác nhau. Khi được giao vai *critic* với 
 chỉ dẫn rõ ("tìm khẳng định không có nguồn"), model kiểm tra tốt hơn hẳn so với khi tự đọc lại bài của 
 chính mình. Bản chất giống code review: người viết code là người tệ nhất để tìm bug của chính mình.

cùng blind spot

xác nhận

tin

debate không thay thế được ground truth

#### Tương tác Debate có thật sự cứu bạn không? — mô hình tương quan lỗi

Gộp nhiều ý kiến chỉ có lợi khi lỗi của chúng *ít tương quan*. 
 Kéo thanh "tương quan lỗi" lên cao để thấy đúng lúc debate ngừng giúp — và bắt đầu gây hại bằng cách 
 khiến câu trả lời sai trông như đã được đồng thuận.

Ba agent, mỗi agent đúng 70%. Đoán trước hai trường hợp cực đoan:

1. Kéo tương quan lỗi về 0% (ba model hoàn toàn khác nhau, lỗi độc lập). 
 Độ chính xác sau debate là bao nhiêu?
2. Kéo tương quan lỗi lên 100% (ba instance của cùng một model). 
 Độ chính xác là bao nhiêu — và ô "Sai mà cả hệ nhất trí" thay đổi thế nào?

#### Kéo xong rồi mở

**Tương quan 0%:** chính xác lên 78,4% (+8,4 điểm phần trăm). 
 Tỷ lệ sai mà cả hệ nhất trí chỉ 2,7%. Debate hoạt động đúng như quảng cáo.

**Tương quan 100%:** chính xác về đúng 70,0% — **bằng y hệt một agent**, cải thiện 0,0 điểm. Nhưng tỷ lệ sai mà cả hệ nhất trí **nhảy từ 2,7% lên 30,0%**.

**Vì sao đây là kết quả tệ nhất có thể:** bạn trả **7× số lượt LLM** để 
 nhận lại đúng độ chính xác cũ — nhưng bây giờ mỗi câu trả lời sai đều đi kèm sự đồng thuận tuyệt đối 
 của ba agent. Judge nhìn thấy 3/3 phiếu thuận và kết luận "chắc chắn đúng". Bạn không chỉ lãng phí tiền, 
 bạn đã *mua thêm sự tự tin cho những câu trả lời sai*.

**Bài học mang đi:** debate không tạo ra tri thức mới. Nó chỉ *khai thác sự khác biệt* giữa các agent. Không có khác biệt thì không có gì để khai thác — và giá vẫn phải trả đủ. 
 Đây chính là cơ chế đằng sau "collective delusion" ở [slide 18](#s18), và là lý do [slide 19](#s19) nhấn mạnh model đa dạng chứ không phải nhiều model.

*Thử thêm — so hai cách "đầu tư":* kéo số agent từ 3 lên 9 (chi phí 7× → 19×) ở hai mức 
 tương quan khác nhau. Ở tương quan **20%**, bạn được thêm ~9 điểm phần trăm. 
 Ở tương quan **80%** — tức là các agent na ná nhau, đúng tình huống thực tế khi bạn 
 dùng cùng một nhà cung cấp — bạn chỉ được thêm ~2 điểm, vẫn với giá 19×. 
 Nói cách khác: tiền mua *sự khác biệt* luôn có lãi hơn tiền mua *số lượng*.

- **Control - Độ chính xác 1 agent 70%**: min `40`, max `95`, step `1`, default `70`

- **Control - Số agent tranh luận 3**: min `3`, max `9`, step `2`, default `3`

- **Control - Tương quan lỗi (cùng blind spot) 20%**: min `0`, max `100`, step `5`, default `20`

1 agent

—

baseline

Sau debate

—

majority vote

Cải thiện

—

điểm phần trăm

⚠ Sai mà cả hệ nhất trí

—

judge không catch được

Chi phí

—

so với 1 agent

Độ chính xác sau debate Tỷ lệ sai mà cả hệ nhất trí Baseline 1 agent

#### Xem dạng bảng



#### Giả định của mô hình — đây là mô hình dạy học, không phải kết quả đo

- Với xác suất ρ (tương quan), tất cả agent rơi vào cùng một kết cục — cùng đúng hoặc cùng sai. 
 Với xác suất 1−ρ, chúng độc lập và hệ lấy đa số phiếu.
- Độ chính xác đa số phiếu = Σ k>N/2 C(N,k)·a k ·(1−a) N−k.
- "Sai mà cả hệ nhất trí" = ρ·(1−a) + (1−ρ)·(1−a) N — trường hợp judge nhận được sự đồng thuận tuyệt đối cho một câu trả lời sai.
- Chi phí tính theo số lượt LLM: N lượt trả lời + N lượt critique + 1 lượt judge.
- Đây là mô hình xác suất đơn giản để xây trực giác. Con số "giảm hallucination 15–25%" trên slide 
 không đến từ mô hình này và cũng không có nguồn — xem mục 
 Các con số cần kiểm chứng.

#### Cấu trúc chi phí

| Bước | Số lượt LLM | Ghi chú |
| --- | --- | --- |
| Trả lời độc lập | 2 | Có thể chạy song song → không cộng latency |
| Critique chéo | 2 | Cũng song song được, nhưng phải chờ bước 1 xong |
| Judge tổng hợp | 1 | Tuần tự, và prompt dài (chứa cả 4 output trước) |
| Tổng | 5 | ≈ 2–3× cost so với 1 lượt; latency ≈ 3 chặng nếu tận dụng song song |

đáng

Đáng:

Không đáng:

SELECT

Với SmartCheck AI:

có

escalate cho lễ tân

### Slide 19 Society of Mind — Heterogeneous Agents

> Trích slide 
>  "Researcher — GPT-4o — Broad knowledge · Analyst — Claude — Nuanced reasoning · Critic — Gemini — Different training data · Judge — Best-of — Final synthesis. 
>  Mỗi model có blind spots khác nhau do training data diversity. GPT-4 + Claude + Gemini → better coverage hơn 3 instances GPT-4. 
>  Trade-off: thêm latency (sequential critique) + cost (3 models). Chỉ justify cho high-stakes. "

"Society of Mind" là khái niệm của Marvin Minsky: trí tuệ nổi lên từ nhiều tiến trình đơn giản 
 tương tác nhau. Ở đây được vay mượn theo nghĩa hẹp và thực dụng: **đa dạng nguồn lỗi**.

Nguyên lý thống kê đằng sau: gộp N ý kiến chỉ có lợi khi các lỗi *ít tương quan*. Ba instance 
 của cùng một model có lỗi tương quan gần như hoàn toàn → gộp lại gần như không được gì (chỉ giảm được 
 nhiễu do sampling). Ba model khác nhà, khác dữ liệu huấn luyện → lỗi ít tương quan hơn → gộp mới có 
 giá trị thật.

vận hành

- Đa dạng prompt: cùng model nhưng khác persona ("bạn là người hoài nghi, chuyên 
 tìm khẳng định thiếu nguồn").
- Đa dạng ngữ cảnh: agent A chỉ được xem tài liệu, agent B chỉ được xem dữ liệu 
 có cấu trúc — lỗi của chúng khác nhau vì đầu vào khác nhau.
- Đa dạng nhiệt độ: hiệu quả yếu nhất, chủ yếu tạo nhiễu chứ không tạo góc nhìn.

departments

rất

#### Ô kiểm tra — Chương 4

Debate là pattern dễ bị dùng sai nhất, vì nó nghe rất thuyết phục.

**1.** Vì sao A và B *bắt buộc* phải trả lời trước khi nhìn thấy đáp án của nhau? Hiểu

#### Đáp án

Vì nếu B thấy đáp án của A trước, B bị **neo** vào lập luận của A (anchoring) — 
 và bạn mất chính thứ đang bỏ tiền ra mua: *hai góc nhìn độc lập*.

Cách kiểm tra bạn đã hiểu: nếu B chỉ nhận xét bài của A chứ không tự trả lời, bạn không có debate — 
 bạn có **Evaluator-Optimizer** với thêm một bước thừa. Hai pattern khác nhau, giá khác nhau.

**2.** Bài toán rất quan trọng, hậu quả sai rất lớn. Khi nào vẫn *không* nên dùng debate? Đánh giá

#### Đáp án

**Khi có ground truth kiểm chứng được.** Nếu câu trả lời nằm trong database, trong test 
 suite, hoặc trong một tài liệu chính thức — hãy *tra cứu*, đừng bỏ phiếu.

Debate là công cụ cho vùng **mơ hồ**: không có nguồn xác định để đối chiếu. 
 Cho hai LLM tranh luận về một sự kiện đã có trong bảng dữ liệu là biến một phép tra cứu xác định 
 thành một trò tung xúc xắc đắt tiền.

*Ứng dụng ngay:* gần như toàn bộ luồng check-in của SmartCheck AI có ground truth trong 
 PostgreSQL → debate không phù hợp, dù "check-in sai người" nghe rất high-stakes.

**3.** Bạn chỉ có ngân sách cho một nhà cung cấp model. Tạo "đa dạng" bằng cách nào? Áp dụng

#### Đáp án

Xếp theo hiệu quả giảm dần:

**① Đa dạng ngữ cảnh (mạnh nhất)** — agent A chỉ được xem tài liệu, agent B chỉ được xem 
 dữ liệu có cấu trúc. Lỗi của chúng khác nhau vì *đầu vào* khác nhau, không phải vì model khác nhau.

**② Đa dạng prompt/persona** — "bạn là người hoài nghi, chuyên tìm khẳng định thiếu nguồn".

**③ Đa dạng nhiệt độ (yếu nhất)** — chủ yếu tạo nhiễu, không tạo góc nhìn.

*Vì sao ① mạnh nhất:* nó tấn công đúng gốc của tương quan lỗi. Hai agent cùng model, cùng 
 dữ liệu vào thì sai giống nhau; đổi dữ liệu vào là đổi nguồn lỗi. Với SmartCheck AI, khi nhánh RAG 
 và nhánh DB mâu thuẫn nhau, đó là tín hiệu escalate *và* là dấu hiệu tài liệu đã lỗi thời.

---

<!-- chiron-source-span: {"source_span_id":"8fbcdf0c-4640-5613-a046-5ff71c0150c4","locator":{"kind":"html_section","section_id":"c5","order":7,"heading":"05 Parallel Execution & Shared State","source_file":"track-3-day-20.html"},"checksum":"be8e51d3194f8a31509f139df74af1d9c58b01425a6145426bed9c291ceac4d3"} -->

## 05 Parallel Execution & Shared State

Slide 20–23: map-reduce, coordination, và concurrency ở mức production.

### Slide 20 Section divider

> Trích slide "05 — Parallel Execution & Shared State. Map-reduce, AsyncIO, và coordination patterns"

Chương này là chương "kỹ sư" nhất của bài: ba mục đều là vấn đề hệ phân tán kinh điển 
 (song song hoá, chia sẻ trạng thái, xử lý lỗi), chỉ đổi worker từ tiến trình sang lời gọi LLM.

### Slide 21 Map-Reduce — LangGraph Send API

> Trích slide 
>  "Task → Worker 1 / Worker 2 / … / Worker N (concurrent) → Merge → Aggregate Result. 
>  LangGraph Send API: Dynamic fan-out + parallel branches — built-in parallelism. Mỗi worker chạy concurrent, merge khi tất cả done. 
>  "Parallel ≠ always faster": DAG dependencies, shared state locks, merge conflicts có thể negate speedup. Đo trước khi assume. "

Điểm mấu chốt của **Send API** là "dynamic fan-out": số worker *không cần biết trước* lúc dựng graph. Bạn tính ra danh sách công việc tại runtime rồi phát ra N nhánh.

```text
from langgraph.types import Send

def fan_out(state):
    # Số lô phụ thuộc dữ liệu runtime → không thể hardcode lúc build graph
    return [Send("summarize_batch", {"batch": b}) for b in chunk(state["comments"], 100)]

g.add_conditional_edges("split", fan_out)   # 1.000 comment → 10 nhánh song song
g.add_edge("summarize_batch", "merge")      # tất cả nhánh hội tụ về merge
```

0s 1s 2s 3s 4s 5s 6s 7s Tuần tự search 1 search 2 search 3 merge 6,7s Song song search 1 search 2 search 3 merge 3,4s chặn bởi worker CHẬM NHẤT (2,2s), không phải trung bình merge LUÔN tuần tự → phần này không bao giờ song song hoá được 3 worker song song nhưng chỉ nhanh gấp 1,97× — không phải 3×. Đó là toàn bộ ý nghĩa của "parallel ≠ always faster".

Hình 5 — Timeline tuần tự vs song song (slide 21).

#### Tương tác Trần tăng tốc — định luật Amdahl cho agent

Thêm worker không mua thêm tốc độ mãi mãi. Phần *không* song song hoá được 
 (routing, merge, các bước phụ thuộc nhau) đặt một trần cứng lên toàn bộ nỗ lực của bạn.

70% công việc song song hoá được, merge tốn 10%. Bạn đang chạy **4 worker** và được 
 tăng tốc 1,74×. Sếp duyệt ngân sách cho **16 worker** — gấp 4 lần tài nguyên. 
 Đoán trước: **tăng tốc sẽ lên bao nhiêu?**

#### Kéo "Số worker" từ 4 lên 16 rồi mở

**Từ 1,74× lên 2,25×** — nhanh thêm đúng **29%**, đổi lấy **gấp 4 lần** tài nguyên. Hiệu suất sụp từ 43% xuống 14%.

**Vì sao:** 30% công việc không song song hoá được, cộng 10% merge — tổng 40% thời gian *không hề bị ảnh hưởng* bởi số worker. Dù bạn có vô hạn worker, phần đó vẫn phải chạy. 
 Trần lý thuyết là 2,50×, và ở 16 worker bạn đã đứng sát trần rồi.

**Cách đọc biểu đồ:** nhìn đường cong *phẳng dần*. Ô "Worker đáng tiền cuối cùng" 
 chỉ ra worker thứ 5 — sau đó mỗi worker thêm mang lại dưới 5% tốc độ. 
 Từ worker 6 đến 16, bạn trả tiền cho 11 worker để mua vài phần trăm.

**Bài học mang đi:** câu hỏi đúng không phải "thêm bao nhiêu worker?" mà là **"phần tuần tự của tôi là bao nhiêu, và cắt nó xuống được không?"** Kéo thanh "% song song hoá được" từ 70% lên 90% mà giữ nguyên 4 worker — bạn sẽ thấy nó ăn đứt 
 việc tăng gấp 4 số worker. Tối ưu phần tuần tự luôn có lãi hơn mua thêm song song.

- **Control - % công việc song song hoá được 70%**: min `0`, max `100`, step `5`, default `70`

- **Control - Chi phí merge (% thời gian gốc) 10%**: min `0`, max `60`, step `5`, default `10`

- **Control - Số worker đang dùng 4**: min `1`, max `16`, step `1`, default `4`

Tăng tốc thực tế

—

tại số worker hiện tại

Trần lý thuyết

—

dù có vô hạn worker

Worker "đáng tiền" cuối cùng

—

sau đó mỗi worker thêm < 5% tốc độ

Hiệu suất

—

tăng tốc ÷ số worker

Có chi phí merge (thực tế) Không chi phí merge (lý tưởng) Trần lý thuyết

#### Xem dạng bảng



#### Giả định của mô hình

- Tăng tốc = 1 / (s + p/N + o), với s = phần tuần tự, p = phần song song, o = chi phí merge, N = số worker.
- Giả định các worker có thời gian chạy bằng nhau. Trong thực tế worker chậm nhất quyết định pha song song 
 (xem Hình 5), nên con số thực tế còn thấp hơn đường xanh này.
- Bỏ qua rate limit. Khi N vượt hạn mức concurrent của nhà cung cấp, đường cong đi xuống vì retry — xem slide 23.

#### Ba lý do "parallel ≠ always faster" — giải thích cụ thể

1. DAG dependencies — nếu Analysis cần output của Search, hai cái đó 
 không song song được. Nhiều pipeline trông có vẻ song song hoá được nhưng thực chất là chuỗi 
 trá hình. Hãy vẽ đồ thị phụ thuộc trước; chỉ những node không có cạnh nối nhau mới song song được thật.
2. Shared state locks — khi các nhánh cùng ghi vào một khoá của state, LangGraph cần 
 một chiến lược gộp. Nếu bạn tuần tự hoá phần ghi, phần song song teo lại. Đây là định luật Amdahl: 
 tốc độ tối đa bị chặn bởi tỷ lệ phần không song song hoá được.
3. Merge conflicts — 10 worker mỗi cái trả 5 chủ đề, tổng 50 chủ đề trùng lặp lẫn 
 nhau. Bước merge có thể phải gọi thêm một lượt LLM để khử trùng lặp — bạn vừa "tiết kiệm" 9 lượt song 
 song rồi trả lại một lượt đắt tiền ở cuối.

- Concat — nối danh sách. Rẻ nhất, dùng khi các phần độc lập (ví dụ: trích dẫn nguồn).
- Reduce có luật — max/min/union, hoặc "ưu tiên record có timestamp mới nhất". 
 Xác định, test được, không tốn LLM.
- LLM merge — chỉ khi cần tổng hợp ngữ nghĩa. Đắt và có thể tạo lỗi mới; dùng cuối cùng.

Annotated[list, operator.add]

"Em có hẹn với anh Minh lúc 2h, mà cho hỏi gửi xe ở đâu ạ?"

độc lập dữ liệu

search_appointment

retrieve_building_policy

P95 latency

context.md

register_visitor

generate_visitor_pass

notify_host

không

### Slide 22 Shared State — Coordination Architecture

> Trích slide 
>  " Shared state (blackboard) — Agents read/write central state — simple, cần locks cho concurrent writes. LangGraph dùng TypedDict state mặc định. 
>  Message passing — Async queue (Redis Pub/Sub, Kafka) — decoupled, scalable, thêm network latency. Tốt cho distributed systems. 
>  Context loss across handoffs: biggest coordination failure. Mỗi agent nhận partial context, quality giảm. 
>  Multi-agent without tracing = impossible to debug. Dùng LangSmith hoặc Langfuse cho mọi multi-agent system. 
>  Failure handling: supervisor detect timeout thì retry different worker hoặc fallback."

#### Hai mô hình phối hợp — so sánh

|  | Shared state (blackboard) | Message passing |
| --- | --- | --- |
| Cách hoạt động | Mọi agent đọc/ghi một cấu trúc trung tâm | Agent gửi tin nhắn qua hàng đợi, không biết ai xử lý |
| Ưu | Đơn giản; ai cũng thấy toàn cảnh; dễ debug (chụp state là thấy hết) | Tách rời (decoupled); scale ngang; agent có thể ở máy khác |
| Nhược | Ghi đồng thời cần khoá; state phình to; khó tách máy | Thêm latency mạng; không có "một chỗ nhìn thấy tất cả"; cần hạ tầng (Redis/Kafka) |
| Khi nào chọn | Một tiến trình, dưới ~10 agent — đa số project | Nhiều dịch vụ, cần bền bỉ qua restart, khối lượng lớn |

LangGraph mặc định là blackboard ( `TypedDict` ). Đó là lựa chọn đúng cho hầu hết trường hợp — 
 đừng dựng Kafka cho một hệ 4 agent chạy trong một tiến trình.

#### Context loss — "biggest coordination failure"

Cơ chế: mỗi lần bàn giao, bạn phải quyết định mang theo bao nhiêu ngữ cảnh. Mang *tất cả* thì 
 prompt phình, tốn token, và model bị nhiễu. Mang *tóm tắt* thì mất chi tiết — và chi tiết bị mất 
 thường chính là ràng buộc quan trọng nhất.

không

Cách phòng:

constraints: list[str]

luôn

#### Tracing — không phải "nice to have"

Câu "multi-agent without tracing = impossible to debug" nên hiểu theo nghĩa đen. Trong single agent, 
 bạn đọc một prompt và một response. Trong hệ 4 agent chạy 8 bước, khi kết quả sai bạn cần biết: 
 bước nào đã sai, worker nào nhận được ngữ cảnh gì, tốn bao nhiêu token, mất bao lâu. Không có trace, 
 bạn chỉ có thể đoán.

context.md

trace_id, session_id, intent, tools_called, 
 tool_arguments, retrieved_documents, latency, token_usage, final_status, human_escalation, error

chính là

### Slide 23 AsyncIO & Agent Pools — Production Concurrency

> Trích slide 
>  "True concurrent execution cho multiple agents. asyncio.gather(agent1(), agent2()) → Parallel API calls, shared event loop. 
>  Pre-initialize N instances, use queue → Amortize init cost, control concurrency. Giống thread pool nhưng cho LLM agents. 
>  Production failure handling: ■ Supervisor detect timeout → retry hoặc fallback ■ Circuit breaker: fail 3 lần → skip, log, backup ■ Dead letter queue: failed tasks lưu lại để debug. 
>  Pool size = concurrent API rate limit. Quá nhiều agents → rate limit errors. "

#### Vì sao asyncio là đúng công cụ (chứ không phải threads)

Gọi LLM là tác vụ **I/O-bound**: 99% thời gian là ngồi chờ mạng, gần như không tốn CPU. 
 Đây đúng là kịch bản asyncio sinh ra để giải — một event loop quản lý hàng trăm lời gọi đang chờ, 
 không cần thread riêng cho mỗi cái. Threads sẽ tốn bộ nhớ và context switch vô ích.

```text
import asyncio

async def run_workers(state):
    # Cùng chờ 2 lời gọi mạng → tổng thời gian ≈ cái chậm nhất, không phải tổng
    search, policy = await asyncio.gather(
        search_agent(state),
        policy_agent(state),
    )
    return {"worker_results": {"search": search, "policy": policy}}

# Chặn quá tải bằng semaphore = rate limit của nhà cung cấp
sem = asyncio.Semaphore(10)          # ponytail: số cứng, đọc từ config khi lên production
async def guarded(coro):
    async with sem:
        return await asyncio.wait_for(coro, timeout=30)   # timeout bắt buộc
```

#### Ba cơ chế chống lỗi — phân biệt cho rõ

| Cơ chế | Giải quyết | Hành vi | Không có thì sao |
| --- | --- | --- | --- |
| Timeout + retry | Lỗi thoáng qua (mạng chập, 503) | Chờ tối đa N giây, thử lại (nên có backoff) | Một worker treo làm cả phiên treo theo |
| Circuit breaker | Lỗi kéo dài (nhà cung cấp sập) | Hỏng 3 lần liên tiếp → ngắt mạch, bỏ qua worker đó, dùng phương án dự phòng | Retry storm: bạn đập vào một dịch vụ đã chết, làm nó chết lâu hơn và trả tiền cho mỗi lần thất bại |
| Dead letter queue | Task thất bại vĩnh viễn | Lưu task + lỗi + context ra một nơi để điều tra sau | Mất luôn dấu vết; không bao giờ biết vì sao 2% request hỏng |

gather

phải đọc từ config

đứng đợi

- Timeout: mỗi lời gọi LLM ≤ 5s. Quá thì hiện "đang kết nối lễ tân" thay vì spinner 
 vô tận — đúng yêu cầu "loading state rõ ràng, error state rõ ràng" trong context.md.
- Circuit breaker: LLM API hỏng 3 lần liên tiếp → chuyển toàn bộ kiosk sang 
 chế độ form (nhập tên/SĐT trực tiếp, tra DB, in pass). Business logic của bạn chạy được 
 không cần LLM (yêu cầu Week 1) — nên fallback này không chỉ là lý thuyết, nó 
 đã tồn tại trong kiến trúc. Đây là điểm mạnh rất đáng nói khi phỏng vấn.
- DLQ: mọi phiên escalate hoặc lỗi tool được ghi lại kèm trace_id → 
 đây chính là nguồn nguyên liệu để mở rộng bộ eval 80 case bằng ca thất bại thật, thay vì ca tự nghĩ ra.

#### Ô kiểm tra — Chương 5

Chương kỹ sư nhất của bài — cũng là chương dễ áp dụng vào code ngay nhất.

**1.** Kể ba nguyên nhân khiến "parallel ≠ always faster". Nhớ / Hiểu

#### Đáp án

**① Phụ thuộc DAG** — nếu B cần output của A thì hai cái đó không song song được. 
 Nhiều pipeline trông song song hoá được nhưng thực chất là chuỗi trá hình.

**② Phần tuần tự chặn trần** — routing, merge, các bước phụ thuộc. Định luật Amdahl: 
 tốc độ tối đa bị chặn bởi tỷ lệ phần *không* song song hoá được.

**③ Chi phí merge** — 10 worker mỗi cái trả 5 chủ đề = 50 chủ đề trùng lặp; 
 bước khử trùng lặp có thể phải gọi thêm một lượt LLM đắt tiền.

*Nguyên nhân thứ tư ít ai nhắc:* worker **chậm nhất** quyết định pha song song, 
 không phải worker trung bình. Xem [Hình 5](#s21).

**2.** User dặn "tóm tắt báo cáo Q3, *đừng* nhắc tới sáp nhập". Writer vẫn viết về 
 sáp nhập. Không agent nào hallucinate. Sửa thế nào? Áp dụng

#### Đáp án

Đây là **context loss**, không phải hallucination. Ràng buộc bị bốc hơi khi supervisor 
 tóm tắt yêu cầu cho Writer.

**Cách sửa:** tách ràng buộc ra *một khoá riêng* trong state 
 ( `constraints: list[str]` ) và **luôn chèn nguyên văn** vào mọi worker prompt.

**Nguyên tắc tổng quát:** *ngữ cảnh có thể tóm tắt; ràng buộc thì không bao giờ.* Đây là một dòng luật đáng dán lên tường — nó chặn nguyên một nhóm lỗi MAST.

**3.** Timeout, circuit breaker, dead letter queue — mỗi cái giải quyết loại lỗi nào? 
 Vì sao không thể thay thế nhau? Phân tích

#### Đáp án

**Timeout + retry → lỗi thoáng qua** (mạng chập, 503). Chờ tối đa N giây rồi thử lại. 
 Không có nó: một worker treo làm cả phiên treo theo.

**Circuit breaker → lỗi kéo dài** (nhà cung cấp sập). Hỏng 3 lần liên tiếp thì ngắt mạch. 
 Không có nó: retry storm — bạn đập vào một dịch vụ đã chết, làm nó chết lâu hơn, và *trả tiền cho 
 mỗi lần thất bại*.

**DLQ → lỗi vĩnh viễn**. Lưu task + lỗi + context để điều tra sau. 
 Không có nó: mất dấu vết, không bao giờ biết vì sao 2% request hỏng.

**Vì sao không thay thế nhau:** chúng khác nhau ở *thang thời gian* — 
 giây, phút, và "sau này". Retry mà không có circuit breaker sẽ biến một sự cố ngắn thành hoá đơn dài.

---

<!-- chiron-source-span: {"source_span_id":"c1e9f957-2287-53c6-a916-4a305620f128","locator":{"kind":"html_section","section_id":"c6","order":8,"heading":"06 Multi-Agent Frameworks","source_file":"track-3-day-20.html"},"checksum":"0c1dbec3b51342d3fb9bca3d9a4161110ab382bc5a17f50694e98ba187939684"} -->

## 06 Multi-Agent Frameworks

Slide 24–25: chọn công cụ theo use case, không theo độ nổi tiếng.

### Slide 24 Section divider

> Trích slide "06 — Multi-Agent Frameworks. LangGraph, AutoGen, CrewAI — chọn đúng công cụ"

### Slide 25 Framework Comparison

> Trích slide 
>  "LangGraph — Flexibility Cao, Setup Trung bình, Best for Production — State machines, full control. 
>  CrewAI — Trung bình / Dễ / Prototype — Role-based, nhanh onboard. 
>  AutoGen — Cao / Trung bình / Code exec — GroupChat, human-in-loop. 
>  OpenAI SDK — Thấp / Rất dễ / Simple — Lightweight, tool-use focused. 
>  Google ADK — Trung bình / Trung bình / GCP — Vertex AI, A2A protocol. 
>  AutoGen/CrewAI tốt cho prototype nhanh. LangGraph cho production — full state control, debugging, conditional routing. Migrate khi cần scale. "

Đọc bảng này theo trục **đánh đổi giữa tốc độ khởi động và mức kiểm soát**. Framework càng 
 dễ dùng thì càng quyết định thay bạn nhiều thứ — tiện lúc prototype, vướng lúc production khi bạn cần 
 can thiệp vào đúng thứ nó đã giấu đi.

| Framework | Trừu tượng cốt lõi | Chọn khi | Đau ở đâu |
| --- | --- | --- | --- |
| LangGraph | Máy trạng thái: node, edge có điều kiện, state có kiểu | Cần luồng xác định, checkpoint, human-in-the-loop, và debug được | Phải tự viết nhiều thứ; đường học dốc hơn |
| CrewAI | Role + goal + tools + task | Demo nhanh, minh hoạ khái niệm "agent như một vai trò" | Ít kiểm soát luồng; khó chèn guard tuỳ biến |
| AutoGen | Hội thoại giữa các agent (GroupChat) | Cần thực thi code, human-in-loop, mô phỏng debate | Hội thoại tự do khó chặn; điều kiện dừng phải tự lo |
| OpenAI Agents SDK | Agent + handoff + guardrail | Routing đơn giản, gắn chặt hệ sinh thái OpenAI | Ít linh hoạt cho luồng phức tạp |
| Google ADK | Agent team + A2A protocol | Đã ở trên GCP/Vertex AI | Buộc chặt vào nền tảng |

đã biết

(1)

(2)

(3)

(4)

---

<!-- chiron-source-span: {"source_span_id":"0476ef71-4bc2-55ba-a99a-c5a82eb8b777","locator":{"kind":"html_section","section_id":"c7","order":9,"heading":"07 Demo & Thực hành","source_file":"track-3-day-20.html"},"checksum":"9de61ba08991e306a66502ce921d86dac28b65b211a01ed33d1412ce09c3e734"} -->

## 07 Demo & Thực hành

Slide 26–31: predict-before-demo, live demo, Lab 20 và rubric peer review.

### Slide 26 Section divider

> Trích slide "07 — Demo & Thực hành. Multi-Agent Research System + 2 giờ lab có peer review"

### Slide 27 Predict-before-demo

> Trích slide 
>  "Cho học viên xem task: Research GraphRAG state-of-the-art, write 500-word summary. Hỏi: agent nào nên chạy trước? bước nào có thể parallel? 
>  So sánh dự đoán với LangSmith trace: route có đúng không? worker nào tốn token nhất? lỗi nào cần guardrail? 
>  Biến demo từ "giảng viên biểu diễn" thành "học viên debug một hệ thống thật". "

Đây là kỹ thuật sư phạm nhưng cũng là **thói quen kỹ thuật rất tốt**: viết dự đoán ra *trước* khi xem trace. Lý do — khi đã nhìn thấy kết quả, bộ não sẽ tự thuyết phục rằng "tôi biết 
 trước rồi mà" (hindsight bias), và bạn mất cơ hội học từ chỗ mình đoán sai.

**Dự đoán mẫu cho task GraphRAG** để bạn tự đối chiếu khi làm lab:

- Agent chạy trước: Search — vì Analysis và Writer đều phụ thuộc dữ liệu của nó.
- Bước song song được: nhiều truy vấn search khác nhau ("GraphRAG benchmark", "GraphRAG vs 
 vector RAG", "Microsoft GraphRAG paper") — độc lập nhau. Analysis và Writer thì không.
- Worker tốn token nhất: gần như chắc chắn là Writer — nó phải nạp toàn bộ insight của 
 Analysis và sinh ra 500 từ. Đây là chỗ đáng dùng model lớn nhất, và cũng là chỗ đáng cắt bớt 
 context nhất.
- Guardrail cần thiết: giới hạn số vòng của supervisor; kiểm tra Writer không trích nguồn 
 nào ngoài danh sách Search trả về (chống bịa citation).

### Slide 28 Multi-Agent Research System — Live Demo

> Trích slide 
>  "1. Pipeline: Supervisor + Search Agent + Analysis Agent + Writer Agent 2. Task: Research GraphRAG state-of-the-art, write 500-word summary — supervisor coordinates 3. LangSmith trace: routing decisions, parallel timeline, worker outputs, final synthesis 4. So sánh: single-agent vs multi-agent trên cùng task — quality, latency, cost"

Điểm 4 là điểm quan trọng nhất và cũng dễ bị làm qua loa nhất. Để so sánh *công bằng*, phải cố 
 định: cùng bộ truy vấn, cùng model cho phần sinh nội dung, cùng tiêu chí chấm chất lượng, cùng điều kiện 
 mạng. Nếu single agent dùng model nhỏ còn multi-agent dùng model lớn thì bạn không đo pattern — bạn đo model.

| Metric | Single agent | Multi-agent | Ghi chú đo |
| --- | --- | --- | --- |
| Quality (rubric 0–5) | — | — | Chấm mù: người chấm không biết output nào của hệ nào |
| Citation coverage | — | — | % khẳng định có nguồn kiểm chứng được |
| Latency P50 / P95 | — | — | Chạy ≥5 lần; một lần chạy là giai thoại, không phải dữ liệu |
| Tokens (in/out) | — | — | Tách riêng token của supervisor để thấy chi phí điều phối |
| Cost / query | — | — | Theo bảng giá thật tại thời điểm chạy |

context.md

Baseline vs Version 1 vs Final

### Slide 29 Lab #20

> Trích slide 
>  "Mục tiêu: Build 3-agent research system: Researcher + Analyst + Writer với LangGraph. 
>  Deliverable: Benchmark report: single-agent vs multi-agent (accuracy, latency, cost) + LangSmith traces. Thời gian: 2 giờ"

Chú ý deliverable: **không phải "hệ thống chạy được"** mà là *benchmark report + traces*. 
 Nghĩa là tiêu chí chấm nằm ở khả năng *đo và giải thích*, không phải ở việc code chạy. Một hệ 
 multi-agent thua single agent nhưng có báo cáo phân tích rõ vì sao thua sẽ được điểm cao hơn một hệ 
 chạy đẹp mà không đo gì.

### Slide 30 Lab 20 — 6 milestone trong 2 giờ

> Trích slide 
>  "1. 0–15' Setup: clone starter, set API key, chạy single-agent baseline. 2. 15–45' Build supervisor: LangGraph state machine, routing via tool calls. 3. 45–75' Add 3 workers: Search/Analysis/Writer Agent; lưu output vào shared state. 4. 75–95' Trace & benchmark: single vs multi trên 3–5 research queries; đo quality, latency, cost. 5. 95–115' Peer review: đổi nhóm, đọc trace của nhau, tìm 1 failure mode và đề xuất fix. 6. 115–120' Exit ticket: mỗi nhóm ghi 1 điều nên dùng multi-agent và 1 điều không nên dùng. 
>  GitHub repo + benchmark report + 1 LangSmith/Langfuse trace screenshot. Bonus: thêm Critic Agent để fact-check."

**Milestone 1 chạy baseline trước** — đây không phải bước khởi động cho có. Nếu hết giờ ở 
 milestone 3, bạn vẫn còn một baseline để nộp kèm phân tích. Và nó ép bạn có con số đối chứng *trước khi* bị cuốn vào việc xây kiến trúc.

làm supervisor 
 giả trước

```text
def supervisor_stub(state):          # chạy được trong 2 phút, không tốn API
    order = ["search", "analyze", "write"]
    done = state["worker_results"]
    nxt = next((w for w in order if w not in done), "FINISH")
    return {"next_worker": nxt}
```

baseline routing

**Milestone 6 (exit ticket)** lặp lại đúng thông điệp của slide 6 và 8: giá trị của buổi học 
 nằm ở việc biết *khi nào không nên* dùng multi-agent.

### Slide 31 Peer Review Rubric

> Trích slide 
>  "Role clarity — Mỗi agent có nhiệm vụ rõ, không overlap quá nhiều không? (0–2) · State design — Shared state có đủ thông tin để handoff mà không mất context không? (0–2) · Failure guard — Có max iterations, timeout, retry/fallback, hoặc validation không? (0–2) · Benchmark — Có so sánh single vs multi-agent bằng metric cụ thể không? (0–2) · Trace explanation — Nhóm giải thích được trace: ai làm gì, tốn bao nhiêu, sai ở đâu không? (0–2) 
>  Mỗi nhóm review 1 nhóm khác trong 8 phút, sau đó owner có 5 phút sửa nhanh."

Rubric 10 điểm này ánh xạ **chính xác** vào ba nhóm lỗi MAST ở slide 9 — không phải trùng 
 hợp, đây là thiết kế khoá học liền mạch:

| Tiêu chí rubric | Nhóm lỗi MAST | Cách ăn trọn 2 điểm |
| --- | --- | --- |
| Role clarity | Specification | Mỗi agent một câu mô tả nhiệm vụ + danh sách tool đóng + ghi rõ điều không được làm |
| State design | Inter-agent misalignment | Chỉ ra được ràng buộc nào được giữ nguyên văn qua handoff, không bị tóm tắt |
| Failure guard | Verification & termination | Chỉ thẳng vào dòng code có max_iterations, timeout, nhánh fallback |
| Benchmark | (phương pháp) | Bảng số thật, ghi rõ chạy bao nhiêu lần, cùng điều kiện gì |
| Trace explanation | (quan sát được) | Mở trace, chỉ vào một bước cụ thể và nói được vì sao nó tốn nhiều token nhất |

context.md

- Role clarity 2/2 — 8 node có tên và trách nhiệm rõ ràng, không chồng lấn.
- State design 2/2 — CheckInState có kiểu tường minh, không nhồi 
 object thừa (bạn đã ghi rõ nguyên tắc này).
- Failure guard ~1/2 — có requires_human, timeout, retry giới hạn; 
 thiếu bộ đếm vòng lặp cho khâu hỏi lại thông tin. Thêm clarify_attempts ở 
 slide 16 là đủ 2/2.
- Benchmark 2/2 — bảng Baseline vs Final đã được lên kế hoạch (miễn là điền 
 số thật, theo đúng quy tắc của bạn).
- Trace explanation 2/2 — danh sách log tối thiểu đã đủ để trace end-to-end.

---

<!-- chiron-source-span: {"source_span_id":"f6a06d88-2c2b-566f-a982-a36a4fe0cc18","locator":{"kind":"html_section","section_id":"c8","order":10,"heading":"08 Quiz, tài liệu & tổng kết","source_file":"track-3-day-20.html"},"checksum":"ec49df2fc65e1923c80856639a7f049b1f8cb7bf2675b03e86fb016547bbc55c"} -->

## 08 Quiz, tài liệu & tổng kết

Slide 32–37.

### Slide 32 Quiz Chương 4 + Milestone 1

> Trích slide 
>  "10 câu trắc nghiệm + short answer. Scope: Reflexion, Memory Systems, Production RAG, GraphRAG, Multi-Agent. Format: 7 MC + 3 short answer. Câu hỏi test understanding, không test nhớ syntax. 
>  Submit portfolio từ N16–N20: Lab 16 Reflexion agent · Lab 17 Memory system · Lab 18 Production RAG · Lab 19 GraphRAG · Lab 20 Multi-agent system. Deadline: 1 tuần sau N20."

"Test understanding, không test nhớ syntax" cho biết dạng câu hỏi sẽ là *khi nào dùng cái gì và 
 vì sao*. Ba câu short answer nhiều khả năng rơi vào đúng ba trục của bài — dưới đây là bộ câu hỏi 
 tự luyện kèm ý chính cần có:

| Câu hỏi khả năng cao | Ý phải nêu để được điểm trọn |
| --- | --- |
| Khi nào không nên dùng multi-agent? | Single agent đã đạt ngưỡng chấp nhận được (slide 6 nêu ~80%); task không phân rã được rõ ràng; bottleneck là retrieval/validation chứ không phải specialization; ràng buộc latency chặt; cần audit trail đơn giản |
| Phân biệt Sectioning và Voting | Sectioning chia công việc khác nhau → giảm latency; Voting nhân bản cùng công việc → tăng độ tin cậy, tốn thêm cost |
| Hai failure mode của Supervisor và cách phòng | Infinite routing loop → max_iterations + lịch sử worker trong prompt; wrong worker selection → mô tả worker không chồng lấn, few-shot, đo routing accuracy |
| Vì sao debate cần model đa dạng? | Cùng model = cùng blind spot = collective delusion; gộp ý kiến chỉ có lợi khi lỗi ít tương quan |
| MAST chỉ ra điều gì về nguyên nhân lỗi? | Phần lớn lỗi đến từ thiết kế hệ thống (spec, misalignment, verification/termination), không phải từ năng lực model → phải định nghĩa role, stop condition, rubric trước khi code |
| "Parallel ≠ always faster" — vì sao? | Phụ thuộc DAG, khoá trên shared state, chi phí merge; phần tuần tự chặn trần tăng tốc (Amdahl) |

### Slide 33 Reference links

> Trích slide 
>  "Anthropic: Building effective agents · OpenAI: Agents SDK orchestration + handoffs · LangGraph supervisor library · AutoGen · CrewAI · Google ADK · MAST paper: Why Do Multi-Agent LLM Systems Fail? (arxiv.org/abs/2503.13657) 
>  Gợi ý đọc: học viên chỉ cần đọc Anthropic + OpenAI handoffs trước lab; các link còn lại dùng khi chọn framework cho project. "

Thứ tự đọc theo mức độ hoàn vốn:

1. Anthropic — Building effective agents. Nguồn gốc của 5 pattern ở slide 11. Đọc kỹ 
 phần phân biệt workflow và agent — đây là ranh giới mà slide chỉ lướt qua.
2. OpenAI — Agents SDK orchestration & handoffs. Cách một framework thật cài đặt 
 handoff; hữu ích để hiểu "context loss" xảy ra ở tầng nào.
3. MAST paper. Slide 35 giao đọc bài này như bài tập về nhà. Đáng đọc phần taxonomy 
 14 failure mode để dùng làm checklist khi thiết kế.
4. Còn lại (LangGraph supervisor, AutoGen, CrewAI, ADK): đọc khi cần chọn công cụ, không phải đọc trước.

### Slide 34 Key Takeaways

> Trích slide 
>  "1. Supervisor là most practical multi-agent architecture — clear ownership, easy debug, production-ready. 
>  2. Debate giảm hallucination 15–25% nhưng tốn 2–3× cost — chỉ dùng cho high-stakes decisions. 
>  3. Parallel execution cắt latency nhưng cần careful state merge strategy — parallel ≠ always faster. 
>  4. Buổi học giữ lý thuyết trong 2 giờ; 2 giờ còn lại build, trace, benchmark, peer review."

Ba takeaway đầu là ba pattern × ba đánh đổi. Đọc chúng như một **cây quyết định**:

NẾU BOTTLENECK LÀ… → PATTERN GUARD BẮT BUỘC METRIC CHỨNG MINH Một agent phải làm quá nhiều loại việc prompt phình, quá nhiều tool SUPERVISOR chậm nhất trong 6 max_iterations cứng + lịch sử worker trong prompt supervisor Routing accuracy trên tập có nhãn Câu trả lời sai mà nghe rất thuyết phục và KHÔNG có ground truth DEBATE 2–3× cost Model / ngữ cảnh đa dạng — không có thì bỏ debate Tỷ lệ sai mà cả hệ nhất trí Nhiều subtask ĐỘC LẬP dữ liệu, và chờ lâu đồ thị phụ thuộc không có cạnh PARALLEL merge, race Giới hạn concurrency + kiểm tra toàn vẹn P95 latency + tỷ lệ kết quả thiếu phần Không rơi vào 3 loại trên — đây là đa số trường hợp, kể cả khi không có cảm giác vậy ĐỪNG thêm agent sửa RAG / prompt Đo baseline TRƯỚC khi làm bất cứ gì khác Accuracy baseline + phân loại lỗi Cột 3 và 4 là phần phân biệt người đã làm với người mới đọc: ai cũng nêu được pattern, rất ít người nêu được guard bắt buộc và metric dùng để chứng minh lựa chọn đó là đúng.

Hình 7 — Bảng quyết định dùng được trong phỏng vấn.

bắt buộc

phụ thuộc rất mạnh vào loại 
 task

bậc độ lớn của đánh đổi

context.md

### Slide 35 Tiếp theo & Bài tập

> Trích slide 
>  "Ngày 21: Fine-tuning LLMs — LoRA/QLoRA. Khi nào nên fine-tune — và khi nào prompt engineering đủ rồi? 
>  ■ Hoàn thành Lab 20 + submit Milestone 1 portfolio ■ Đọc: MAST paper (NeurIPS 2025) — multi-agent failure taxonomy"

Câu hỏi dẫn của Ngày 21 lặp lại đúng khuôn mẫu tư duy của Ngày 20: *"khi nào nên X, và khi nào 
 thứ đơn giản hơn đã đủ?"* — hôm nay là "thêm agent", hôm sau là "fine-tune". Cùng một thang leo: 
 prompt → RAG/tool → agent → fine-tune, và ở mỗi bậc, bằng chứng đo đạc mới là thứ cho phép leo tiếp.

### Slide 36 Hỏi & Đáp

> Trích slide 
>  "Supervisor vs Debate vs Parallel — khi nào dùng pattern nào? Single agent có khi nào đủ?"

Trả lời gọn cho câu thứ hai — và đây là câu trả lời "đúng" theo tinh thần cả bài: **single agent đủ trong đa số trường hợp.** Cụ thể là khi task có một mục tiêu rõ, dưới 
 khoảng 10 tool, không có subtask nào thật sự song song, và lỗi hiện tại thuộc loại sửa được bằng 
 retrieval/prompt/validation. Multi-agent là ngoại lệ cần biện minh, không phải mặc định cần biện hộ.

### Slide 37 Cảm ơn

> Trích slide 
>  "Cảm ơn! AICB-P2T3 · Ngày 20 · Multi-Agent Systems — github.com/vinuni-aicb — Liên hệ: instructor@vinuni.edu.vn"

---

<!-- chiron-source-span: {"source_span_id":"20f2cb3a-94f0-5adc-a839-6095547d1480","locator":{"kind":"html_section","section_id":"sim","order":11,"heading":"⚙ Trình mô phỏng kiến trúc","source_file":"track-3-day-20.html"},"checksum":"c1ff37bebbb0c338518d2c3a36b2edac7c92c81daa7430d7afb352d0d7df92d7"} -->

## ⚙ Trình mô phỏng kiến trúc

Chọn pattern, chỉnh tham số, và xem ngay tác động lên số lượt LLM, chi phí, độ trễ 
 và bề mặt lỗi. Đây là cách nhanh nhất để cảm nhận vì sao "start simplest" không phải lời khuyên đạo đức 
 mà là kết luận số học.

#### Tương tác So sánh 6 kiến trúc trên cùng một workload

Sáu kiến trúc chạy cùng một khối lượng công việc. Chi phí và độ trễ được tính từ 
 cấu trúc lượt gọi của từng pattern — không phải số bịa.

Giữ nguyên mặc định (10.000 query, 3 worker). Trước khi bấm qua 6 tab, hãy đoán:

1. Kiến trúc nào chậm nhất — Debate (5 lượt LLM) hay Supervisor (7 lượt)?
2. Kiến trúc nào đắt nhất — Parallel (4 lượt) hay Supervisor (7 lượt)?

#### Bấm hết 6 tab rồi mở

**Câu 1 — Supervisor chậm nhất: 10,1s** so với Debate 6,6s, dù Debate cũng tốn nhiều lượt.

*Vì sao:* Debate chạy được **2 trong 3 chặng song song** (hai agent trả lời cùng lúc, 
 rồi critique cùng lúc) → chỉ 3 chặng tuần tự. Supervisor thì **mọi lượt đều tuần tự**: 
 route → worker → route → worker → route → worker → tổng hợp = 7 chặng. Số lượt LLM giống nhau 
 nhưng *hình dạng* khác nhau.

**Câu 2 — Parallel đắt nhất trong hai: $475** so với Supervisor $325, dù Parallel chỉ dùng 4 lượt còn Supervisor dùng 7.

*Vì sao:* cả 4 lượt của Parallel đều là model **mạnh**, và lượt merge phải nạp 
 toàn bộ output của 3 worker. Supervisor dùng model **rẻ** cho 4 lượt điều phối, 
 chỉ 3 lượt worker là model mạnh. Đây chính là "cost insight" của [slide 15](#s15) hiện ra bằng số.

**Bài học mang đi — hai điều đếm lượt gọi không cho bạn biết:**

① **Độ trễ phụ thuộc số *chặng tuần tự*, không phải số lượt gọi.** Muốn nhanh, hãy hỏi "chặng nào gộp lại chạy song song được?", không phải "bớt được lượt nào?".

② **Chi phí phụ thuộc *model nào × context bao nhiêu*, không phải số lượt gọi.** Bảy lượt rẻ có thể rẻ hơn bốn lượt đắt.

*Thử thêm:* kéo "Số worker" từ 3 lên 6 và xem Supervisor. Chi phí và độ trễ đều tăng gần gấp đôi — 
 vì mỗi worker thêm vào *kéo theo* một lượt routing nữa. Trong hub-spoke, thêm chuyên gia 
 không bao giờ chỉ là thêm một chuyên gia.

Single agent

Prompt Chaining

Routing

Parallel

Supervisor

Debate

- **Control - Query / tháng 10.000**: min `1000`, max `100000`, step `1000`, default `10000`

- **Control - % query dễ (chỉ Routing) 70%**: min `0`, max `100`, step `5`, default `70`

- **Control - Số worker / subtask 3**: min `2`, max `6`, step `1`, default `3`

- **Control - Độ trễ 1 lượt model lớn 2,2s**: min `5`, max `50`, step `1`, default `22`

Lượt LLM / query

—

—

Chi phí / tháng

—

—

Độ trễ đường găng

—

—

Chất lượng

phải tự đo

không có mô hình nào đoán hộ được

Chất lượng thì không.

benchmark report

#### Chi phí / tháng theo kiến trúc

#### Độ trễ một query theo kiến trúc

#### Bề mặt lỗi bạn phải tự xử lý

#### Xem dạng bảng (đầy đủ mọi kiến trúc)



#### Cấu trúc lượt gọi & giả định giá — đọc trước khi trích số

- Single: 1 lượt model lớn. — Chaining: 3 lượt tuần tự, context tích luỹ ×1 / ×1,3 / ×1,6.
- Routing: 1 lượt phân loại (model nhỏ, prompt ngắn) + 1 lượt xử lý (nhỏ nếu dễ, lớn nếu khó).
- Parallel: W lượt lớn đồng thời + 1 lượt merge với context ×(1+0,5W).
- Supervisor: W lượt worker (lớn) xen kẽ W+1 lượt routing (nhỏ), context supervisor phình 60% mỗi lượt.
- Debate: 2 lượt trả lời song song + 2 lượt critique song song + 1 lượt judge (context ×3).
- Giá: model lớn $2,50/M token vào, $10/M ra. Model nhỏ $0,15/M vào, $0,60/M ra. Mỗi lượt 2.000 token vào, 500 ra. 
 Thay bằng bảng giá thật tại thời điểm bạn tính.
- Độ trễ model nhỏ = 40% model lớn. Độ trễ đường găng = tổng của các chặng tuần tự; các lượt trong cùng một chặng chạy đồng thời.
- Bỏ qua: rate limit, retry, cache. Cả ba đều làm con số thực tế lệch đi — theo hướng xấu hơn cho các pattern nhiều lượt gọi.

---

<!-- chiron-source-span: {"source_span_id":"89cfd3e8-f814-5030-b513-0106917ad82a","locator":{"kind":"html_section","section_id":"ladder","order":12,"heading":"▤ Luyện kỹ năng cốt lõi: chọn pattern và bảo vệ lựa chọn","source_file":"track-3-day-20.html"},"checksum":"48866705fc8ffa9c4cb115f5353e55418e758d15365a65f7818041f6600993c2"} -->

## ▤ Luyện kỹ năng cốt lõi: chọn pattern và bảo vệ lựa chọn

Đây là kỹ năng duy nhất mà quiz, lab và phỏng vấn đều hỏi. Ba bài dưới đây **giảm dần sự trợ giúp**: bài 1 làm sẵn từng bước cho bạn xem, bài 2 làm hộ một nửa, 
 bài 3 bạn tự làm. Làm đúng thứ tự — nhảy thẳng vào bài 3 là cách nhanh nhất để nản.

① Bottleneck thật sự là gì?

② Có subtask độc lập không?

thấp nhất

④ Failure mode mới nào vừa xuất hiện?

⑤ Guard nào bắt buộc, và đo bằng metric gì?

quen thuộc nhất

thấp nhất đủ dùng

#### Tổng hợp 1.000 review khách hàng thành 5 chủ đề chính

Đọc kỹ cách *lập luận*, đừng chỉ đọc đáp án. Bài 2 và 3 sẽ yêu cầu bạn lặp lại đúng mạch này.

1. Bottleneck: latency. Không phải accuracy — tóm tắt review là việc LLM làm tốt. 
 Vấn đề là khối lượng: nhồi 1.000 review vào một prompt thì vỡ context window; chạy 1.000 lượt tuần tự 
 thì mất hàng giờ. Cách nhận ra: hỏi "nếu model thông minh gấp đôi, vấn đề có biến mất không?" 
 Không → bottleneck không phải accuracy.
2. Subtask độc lập: có, rõ ràng. Review số 7 không cần biết gì về review số 350. 
 Không có cạnh phụ thuộc nào trong đồ thị.
3. Bậc thấp nhất đủ dùng: bậc 3 — Parallel/Sectioning. 
 Bậc 1 (Chaining) và bậc 2 (Routing) không đụng được vào latency — chúng sắp xếp công việc chứ không 
 chạy đồng thời. Bậc 4 (Supervisor) là thừa: bạn đã biết trước cần chia bao nhiêu lô, không có gì 
 để một LLM phân rã tại runtime. Trả tiền cho supervisor ở đây là trả tiền để quyết định một việc 
 mà vòng for đã quyết được.
4. Failure mode mới: ⑴ merge trùng lặp — 10 lô × 5 chủ đề = 50 chủ đề chồng chéo; 
 ⑵ mất dữ liệu âm thầm nếu một lô lỗi mà không ai kiểm; ⑶ rate limit khi bung quá nhiều lô cùng lúc.
5. Guard + metric: giới hạn concurrency bằng semaphore theo rate limit thật; retry lô lỗi; 
 assert tổng số review vào = tổng số review được xử lý (guard rẻ nhất và bắt được lỗi nguy hiểm nhất). 
 Metric: latency tổng, cost/review, và độ ổn định của tập chủ đề khi đổi cách chia lô — 
 nếu chia lô khác ra chủ đề khác, kết quả của bạn là ngẫu nhiên chứ không phải phân tích.

Câu chốt kiểu phỏng vấn "Sectioning, vì bottleneck là latency và các review độc lập dữ liệu. Tôi không dùng supervisor vì 
 số lô biết trước, không cần phân rã runtime. Guard chính là giới hạn concurrency và kiểm tra toàn vẹn 
 số lượng; metric là latency tổng và độ ổn định của tập chủ đề giữa các cách chia lô."

#### Hệ xử lý ticket: refund / billing / technical support

Hai bước đầu đã làm sẵn. Ba bước sau bạn tự viết ra giấy rồi mới mở đáp án.

1. Bottleneck: ownership và accuracy của việc phân loại. Ba loại ticket có quy định, 
 tool và hậu quả pháp lý khác nhau. Refund động tới tiền thật.
2. Subtask độc lập: không hẳn — mỗi ticket chỉ đi vào một nhánh. 
 Đây là bài toán chọn nhánh, không phải bài toán chia việc.
3. ③ Bậc thấp nhất đủ dùng là bậc mấy? Và vì sao không phải bậc 4? 
 (gợi ý: xem lại bài 1 — điều gì phân biệt "chọn nhánh" với "phân rã runtime"?)
4. ④ Failure mode mới nào xuất hiện? 
 (gợi ý: loại lỗi nào ở đây tốn tiền thật, và nó có kêu lên không?)
5. ⑤ Guard và metric? 
 (gợi ý: hai loại lỗi phân loại có ngang giá nhau không?)

#### Đáp án ba bước còn lại

**③ Bậc 2 — Routing.** Ba loại rõ rệt, mỗi loại có tool và quy định riêng; phân loại xong 
 là xong việc điều phối. Không phải bậc 4 vì *không có gì để phân rã*: một ticket không bị chia 
 thành nhiều subtask do LLM tự nghĩ ra. Supervisor giải bài toán "gọi ai *tiếp theo* "; 
 ở đây chỉ có "gọi ai", một lần.

**④ Failure mode mới: mis-route im lặng.** Một ticket refund bị đẩy sang nhánh FAQ 
 → khách nhận link help center thay vì tiền. Điểm chết người: *hệ thống không báo lỗi*. 
 Không exception, không log đỏ, response 200. Bạn chỉ biết khi khách khiếu nại.

**⑤ Guard:** ngưỡng confidence — dưới ngưỡng thì chuyển người thật thay vì đoán. 
 Và *ngưỡng phải bất đối xứng*: nghi ngờ là refund thì cứ route sang refund (chỉ tốn thời gian 
 nhân viên); nghi ngờ là FAQ mà thực ra là refund thì mất tiền và mất khách.

**Metric:** không phải accuracy tổng, mà **recall của riêng nhánh refund**. 
 Một hệ đạt 95% accuracy tổng vẫn có thể bỏ sót một nửa số refund nếu refund chỉ chiếm 8% lưu lượng. 
 Accuracy tổng là con số dễ chịu nhất và ít thông tin nhất trong mọi bài toán phân loại lệch lớp.

*Đối chiếu với bài 1:* cùng khung 5 bước, nhưng bottleneck khác nên bậc thang khác, 
 và metric khác. Đó là toàn bộ kỹ năng cần học.

#### SmartCheck AI — khách nói ba việc trong một lượt

Không có bước nào làm sẵn. Đây là tình huống thật trong dự án của bạn.

"Em hẹn anh Minh lúc 2h, mà cho hỏi gửi xe ở đâu ạ, với lại 
 em cần mang giấy tờ gì để lên tầng?"

Viết ra đủ 5 bước rồi mới mở. Nếu bạn viết được cả 5 bước một cách thuyết phục, bạn đã đạt 
 mức "Áp dụng" của bài học này.

#### Đáp án tham khảo — so với bài của bạn, không thay thế nó

**① Bottleneck: latency.** Khách đang *đứng đợi trước kiosk*. Accuracy không phải 
 vấn đề — cả ba yêu cầu đều có nguồn xác định (PostgreSQL cho lịch hẹn, pgvector cho hai câu hỏi chính sách).

**② Subtask độc lập: có, cả ba.** Tra lịch hẹn không cần biết chính sách gửi xe; 
 hai truy vấn RAG không cần biết nhau. Đồ thị phụ thuộc rỗng.

**③ Bậc 3 — Sectioning**, lồng trong Routing sẵn có. Cụ thể: một `asyncio.gather` cho `search_appointment` + hai lần `retrieve_building_policy`. Tuần tự tốn ~300 + 400 + 400 = 1.100ms; song song còn ~400ms.

**④ Failure mode mới:** ⑴ một nhánh lỗi trong khi hai nhánh kia thành công — trả lời *một phần* nguy hiểm hơn không trả lời, vì khách tưởng đã xong; 
 ⑵ hai truy vấn RAG có thể lấy về cùng một tài liệu → câu trả lời lặp; 
 ⑶ thứ tự trả lời không còn xác định, khiến log khó đọc.

**⑤ Guard + metric:** dùng `asyncio.gather(..., return_exceptions=True)` để 
 một nhánh hỏng không giết cả phiên; nhánh nào hỏng thì nói thẳng với khách phần đó cần gặp lễ tân — *không im lặng bỏ qua*. Khử trùng lặp tài liệu theo `doc_id` trước khi dựng context. 
 Metric: P95 latency (mục tiêu chính), và **tỷ lệ phiên trả lời thiếu một trong các yêu cầu** — 
 metric này không có sẵn trong danh sách của `context.md` và chỉ xuất hiện *vì* bạn 
 song song hoá. Mỗi guard mới sinh ra một metric mới; đó là dấu hiệu bạn đang thiết kế đúng.

**Bẫy trong đề:** nếu bạn định nghĩa mỗi yêu cầu thành một "agent" riêng thì bạn đã 
 leo lên bậc 4 không cần thiết. Ba lời gọi tool đồng thời *không phải* ba agent — 
 chúng không có prompt riêng, không tự quyết định gì, không cần điều phối. Phân biệt được 
 "gọi song song" với "nhiều agent" là ranh giới giữa hiểu bài và thuộc bài.

---

<!-- chiron-source-span: {"source_span_id":"83fdd5f7-acd6-5672-8dd4-9d1ea5f3022e","locator":{"kind":"html_section","section_id":"apply","order":13,"heading":"→ Áp dụng vào SmartCheck AI","source_file":"track-3-day-20.html"},"checksum":"dab4536d3c187fc31ac6d9e84ee6a5dab58d6220989d86bd8f9065e7c637e903"} -->

## → Áp dụng vào SmartCheck AI

Tổng hợp: bài học Ngày 20 ánh xạ sang dự án kiosk của bạn, và những thay đổi cụ thể đáng làm.

### Kết luận chính: giữ nguyên kiến trúc single-graph

Slide 6 ("nếu single agent đủ tốt thì đừng thêm agent"), slide 9 (lỗi đến từ thiết kế hệ thống), 
 slide 11 ("start simplest") và slide 25 (LangGraph cho production) **đều ủng hộ ADR-01 của bạn**. 
 Buổi học này không yêu cầu bạn đổi kiến trúc SmartCheck AI — nó cung cấp *ngôn ngữ và bằng chứng* để bảo vệ kiến trúc hiện tại trong phỏng vấn.

### 4 thay đổi cụ thể đáng làm

START Classify intent model rẻ — chọn 1 trong ~5 nhãn 3 Extract visitor info model mạnh — structured output 3 Thiếu field bắt buộc? Ask clarification clarify_attempts++ 1 hỏi lại quá 2 lần → escalate không thiếu 2 chạy ĐỒNG THỜI — asyncio.gather search_appointment retrieve_policy Confidence đủ? không đủ Human escalation gọi lễ tân ADR-05: feature, không phải lỗi đủ register → pass → notify_host tuần tự bắt buộc — pass cần visitor_id END 4 Circuit breaker LLM hỏng 3 lần → chế độ form thuần DB kiosk vẫn chạy Vòng tròn cam = 4 thay đổi đề xuất. Tất cả đều nằm trong một graph — không thêm agent nào, đúng ADR-01.

Hình 6 — SmartCheck AI sau 4 thay đổi.

| # | Thay đổi | Từ slide | Chi phí | Lợi ích |
| --- | --- | --- | --- | --- |
| 1 | Thêm clarify_attempts + MAX_CLARIFY vào CheckInState, quá ngưỡng thì escalate | 16, 9 | ~5 dòng | Chặn vòng lặp hỏi lại vô hạn; ăn trọn điểm "Failure guard" của rubric |
| 2 | Chạy song song search_appointment và retrieve_building_policy khi intent hỗn hợp | 21, 23 | 1 asyncio.gather | Cắt ~300ms P95; không rủi ro merge (ghi vào hai khoá khác nhau) |
| 3 | Model nhỏ cho Intent Router, model lớn cho Extractor và các node sinh nội dung | 13, 15 | 1 dòng config | Giảm cost/session; có số thật để đưa vào bảng benchmark |
| 4 | Circuit breaker: LLM hỏng 3 lần → chuyển kiosk sang chế độ form thuần DB | 23 | ~20 dòng | Kiosk vẫn phục vụ được khi LLM API sập — điểm nhấn rất mạnh khi phỏng vấn |

Debate agents

Supervisor LLM đứng trên các node

Heterogeneous multi-model

### Câu trả lời phỏng vấn dựng sẵn

*"Sao project của bạn không dùng multi-agent?"*

> Trả lời mẫu 
>  "Vì bottleneck của tôi không nằm ở specialization. Ba lý do chính đáng để multi-agent là 
>  specialization, parallelization và cross-checking. Ở bài toán check-in, dữ liệu nghiệp vụ nằm trong 
>  PostgreSQL nên cross-checking đã có ground truth xác định — không cần consensus giữa các model. 
>  Specialization thì tôi giải bằng các node chuyên biệt trong một graph có state, vẫn được prompt hẹp và 
>  tool riêng cho từng bước mà không phải trả giá cho routing loop và context loss giữa các agent. 
>  Parallelization tôi có áp dụng có chọn lọc — chạy song song RAG retrieval với appointment lookup. 
>  Bài MAST cho thấy phần lớn lỗi multi-agent đến từ specification, misalignment và termination chứ không 
>  phải từ model, nên với một hệ giao dịch cần audit, tôi ưu tiên deterministic workflow. Và tôi đo trước 
>  khi quyết: nếu số liệu cho thấy single-graph không đạt ngưỡng, việc thêm agent mới được biện minh."

---

<!-- chiron-source-span: {"source_span_id":"9173b051-b020-516b-8f9d-ff0d305fc43e","locator":{"kind":"html_section","section_id":"numbers","order":14,"heading":"! Các con số trên slide — cần kiểm chứng trước khi trích dẫn","source_file":"track-3-day-20.html"},"checksum":"fd7a3d2fec41233fd4607777f159fdca3282f1a11f49062b2c174e1d14a0fc99"} -->

## ! Các con số trên slide — cần kiểm chứng trước khi trích dẫn

Bài giảng đưa ra vài con số không kèm nguồn trực tiếp. Đây là cách đọc chúng cho đúng.

| Con số | Slide | Trạng thái | Nên dùng thế nào |
| --- | --- | --- | --- |
| Ngưỡng 80% accuracy để "không thêm agent" | 6 | Quy tắc kinh nghiệm, không phải hằng số | Hiểu là "phải đo baseline trước". Ngưỡng thật phụ thuộc bài toán — hệ y tế có thể cần 99% |
| Routing giảm 50%+ chi phí (70/30) | 13 | Đúng về mặt số học với giả định cụ thể | Tự tính lại theo bảng giá hiện hành và phân phối traffic thật của bạn; nhớ cộng chi phí bước phân loại |
| Debate giảm hallucination 15–25% | 18, 34 | Không nêu nguồn; phụ thuộc mạnh vào loại task | Chỉ dùng để cảm nhận bậc độ lớn. Không trích vào README/CV như kết quả của mình |
| Debate tốn 2–3× cost | 34 | Khớp với phép đếm lượt LLM (5 lượt vs 1) | Có thể dùng khi ước lượng, nhưng nói rõ là ước lượng theo số lượt gọi |
| MAST: 14 failure modes, 3 nhóm, 150+ tasks | 9 | Có nguồn cụ thể (arXiv:2503.13657) | Trích dẫn được, nhưng nên đọc bài gốc trước khi dẫn chi tiết |

context.md

"Không ghi số liệu giả vào README/CV. Chỉ cập nhật khi benchmark thực tế 
 đã chạy."

---

<!-- chiron-source-span: {"source_span_id":"6e9203a6-7a6a-506c-bdab-29b5df276243","locator":{"kind":"html_section","section_id":"misc","order":15,"heading":"✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý","source_file":"track-3-day-20.html"},"checksum":"049e1c7a47beffaddbf67d915a5345adc1ab84c8f92b9e864ced4b8766d654ff"} -->

## ✕ 6 hiểu lầm phổ biến — và vì sao chúng nghe rất hợp lý

Kiến thức sai không biến mất khi bạn đọc kiến thức đúng — nó chỉ biến mất khi bạn *nhìn thấy nó sai ở đâu*. Mỗi thẻ dưới đây nêu niềm tin phổ biến, lý do nó nghe thuyết phục, 
 thực tế, và chỗ bạn có thể tự kiểm chứng ngay trong tài liệu này. Đây cũng là vùng quiz hay khai thác nhất.

*Vì sao nghe hợp lý:* ở con người thì đúng thật — một team giỏi hơn một cá nhân. 
 Phép so sánh "team dự án" ở slide 5 lại càng củng cố cảm giác này.

Thêm agent **không thêm tri thức** — vẫn cùng model, cùng dữ liệu huấn luyện. 
 Thứ nó thêm là khả năng chuyên môn hoá (prompt hẹp hơn cho mỗi quyết định) và **một họ lỗi hoàn toàn mới nằm giữa các agent**: context loss, handoff sai, tranh chấp state. 
 Với con người, "họp" là chi phí ai cũng biết; với agent, chi phí đó vô hình cho tới khi bạn đo.

[Ba chỗ phép so sánh team gãy](#s5) · [Trình mô phỏng](#m-sim): Supervisor 3 worker 
 tốn 7 lượt LLM và 10,1s cho công việc mà single agent làm trong 1 lượt, 2,2s.

*Vì sao nghe hợp lý:* 4 worker làm 4 việc cùng lúc thì phải nhanh gấp 4 chứ. 
 Trực giác này đúng với công việc tay chân, và sai với hệ có phần tuần tự.

Phần *không* song song hoá được đặt một trần cứng. Với 70% song song hoá được và 10% chi phí merge, 
 trần là **2,5×** — dù bạn có vô hạn worker. Thêm nữa: pha song song bị chặn bởi worker **chậm nhất**, không phải trung bình.

[Trần tăng tốc](#m-amdahl): từ 4 lên 16 worker (gấp 4 tài nguyên) chỉ nhanh thêm 29%, 
 hiệu suất tụt từ 43% xuống 14% · [Hình 5](#s21): 3 worker song song chỉ được 1,97× chứ không phải 3×.

*Vì sao nghe hợp lý:* tranh luận đúng là cách con người lọc ý tưởng sai. 
 Và con số "giảm hallucination 15–25%" trên slide nghe rất chắc chắn.

Debate **không tạo ra tri thức mới** — nó chỉ *khai thác sự khác biệt* giữa các agent. 
 Nếu các agent giống nhau, không có gì để khai thác, và bạn vẫn trả đủ tiền. Tệ hơn: khi chúng cùng sai, 
 judge nhận được sự đồng thuận tuyệt đối cho một câu trả lời sai và kết luận "chắc chắn đúng".

[Mô hình tương quan lỗi](#m-debate): kéo tương quan lên 100% — độ chính xác về đúng 70% 
 (bằng một agent) nhưng tỷ lệ "sai mà cả hệ nhất trí" nhảy từ 2,7% lên 30%. Bạn trả 7× tiền để mua 
 thêm sự tự tin cho những câu trả lời sai.

*Vì sao nghe hợp lý:* nó *thật sự* tổng quát — supervisor giải được mọi bài trong bài học này. 
 Slide 34 còn gọi nó là "most practical". Vậy sao không dùng luôn?

"Most practical *trong nhóm multi-agent* " không có nghĩa là "nên dùng mặc định". 
 Supervisor nằm ở bậc 4/5 trên thang leo — nghĩa là nó mang theo **nhiều failure mode nhất** (routing loop, chọn sai worker, context loss) và độ trễ cao nhất. Slide 12 nói thẳng: 
 "Không được mặc định supervisor cho mọi thứ. Hãy chứng minh pattern đơn giản hơn chưa đủ."

[Trình mô phỏng](#m-sim): Supervisor có độ trễ **cao nhất trong cả 6 kiến trúc** (10,1s) · [Bài 1 và bài 2](#ladder) đều là những bài mà supervisor giải được nhưng là lựa chọn sai.

*Vì sao nghe hợp lý:* đếm lượt gọi là cách ước lượng dễ nhất, và nó đúng… trong trường hợp 
 mọi lượt gọi giống nhau. Nhưng chúng không giống nhau.

**Chi phí** phụ thuộc *model nào × context bao nhiêu*, không phải số lượt. **Độ trễ** phụ thuộc số *chặng tuần tự*, không phải số lượt. 
 Bảy lượt rẻ có thể rẻ hơn bốn lượt đắt; năm lượt chia làm ba chặng nhanh hơn bảy lượt tuần tự.

[Trình mô phỏng](#m-sim), mặc định: Parallel **4 lượt → $475** nhưng 
 Supervisor **7 lượt → $325** (rẻ hơn dù nhiều lượt hơn). 
 Debate **5 lượt → 6,6s** nhưng Supervisor **7 lượt → 10,1s**.

*Vì sao nghe hợp lý:* với single agent thì thường đúng thật. Bản năng đầu tiên khi hệ trả lời 
 sai là nâng cấp model — và nó cho cảm giác đang tiến bộ mà không phải nghĩ.

Bài MAST phân tích 150+ task và chỉ ra phần lớn lỗi đến từ **specification, inter-agent 
 misalignment, và verification/termination** — tức là từ *thiết kế hệ thống*. 
 Không model nào ngăn được một vòng lặp vô hạn; chỉ bộ đếm trong code mới ngăn được. 
 Không model nào khôi phục được một ràng buộc đã bị cắt mất khi handoff.

[Hình 3](#s9): ba nhóm lỗi định vị theo vòng đời — cả ba đều nằm ngoài tầm với của model · [Ngân sách vòng lặp](#m-guard): một bug loop tốn 453× trần có guard, và model mạnh hơn 
 chỉ làm nó tốn nhanh hơn.

---

<!-- chiron-source-span: {"source_span_id":"81f600e6-0956-52fe-a7da-7f4c96901422","locator":{"kind":"html_section","section_id":"cheat","order":16,"heading":"✓ Cheat sheet ôn thi","source_file":"track-3-day-20.html"},"checksum":"5eee793c4455b2d77a0e77ba64e9d0d4e5fbbeb4a22e80b6da3c197015c37bed"} -->

## ✓ Cheat sheet ôn thi

Nén toàn bộ 37 slide xuống một trang.

### Thang leo 5 pattern

| # | Pattern | Một câu định nghĩa | Dấu hiệu phải leo lên bậc sau |
| --- | --- | --- | --- |
| 1 | Prompt Chaining | Các bước tuần tự cố định + gate kiểm tra giữa các bước | Input có nhiều loại rõ rệt cần xử lý khác nhau |
| 2 | Routing | Phân loại rồi gửi tới handler chuyên biệt | Có subtask độc lập và latency là vấn đề |
| 3 | Parallel | Sectioning: chia việc → nhanh hơn. Voting: nhân bản việc → chắc hơn | Không biết trước cần bao nhiêu/loại subtask nào |
| 4 | Orchestrator-Workers | LLM phân rã task tại runtime, giao worker, tổng hợp | Chất lượng đầu ra cần vòng critique lặp lại |
| 5 | Evaluator-Optimizer | Sinh → chấm theo rubric → sửa, lặp có giới hạn | (bậc cao nhất) |

### Checklist trước khi build bất kỳ hệ multi-agent nào

1. Đã có baseline single-agent kèm số đo chưa?
2. Mỗi agent mô tả được nhiệm vụ trong một câu không chồng lấn chưa?
3. Shared state gồm những khoá nào, ai được ghi khoá nào?
4. Ràng buộc của người dùng được giữ nguyên văn qua mọi handoff chưa?
5. Điều kiện dừng là gì? max_iterations bằng bao nhiêu?
6. Timeout mỗi worker? Hỏng thì fallback đi đâu?
7. Trace đã bật chưa? Nhìn trace có trả lời được "ai làm gì, tốn bao nhiêu" không?
8. Đo quality, latency, cost — chạy ít nhất 5 lần, cùng điều kiện.
9. Nếu multi-agent thua baseline: bạn có sẵn sàng vứt nó đi không?

Thêm agent là quyết định phải có bằng chứng, không phải mặc định.

giữa

---

<!-- chiron-source-span: {"source_span_id":"284c8230-9822-5d17-b04c-f32f0e282ffa","locator":{"kind":"html_section","section_id":"gloss","order":17,"heading":"A–Z Từ điển thuật ngữ","source_file":"track-3-day-20.html"},"checksum":"ef3f16183c49e90230d753b62ca3340cbaf6177ca76124f660cb58711edcee96"} -->

## A–Z Từ điển thuật ngữ

Rất nhiều người tưởng mình chưa hiểu khái niệm, trong khi thực ra chỉ đang vướng từ vựng. 
 Mỗi mục dưới đây: một câu tiếng Việt dễ hiểu, rồi chỗ nó xuất hiện trong bài.

---

<!-- chiron-source-span: {"source_span_id":"678f33ea-fdfe-5156-a5cf-e8c76ad4e194","locator":{"kind":"html_section","section_id":"bloom","order":18,"heading":"◉ Bạn đang ở mức nào?","source_file":"track-3-day-20.html"},"checksum":"0b9c2e150f6741d2ad2108d0e91e294f01909b963249a78bcd7a6561916fe52b"} -->

## ◉ Bạn đang ở mức nào?

Tự chấm trung thực. Mỗi mức là một *việc làm được*, không phải một cảm giác — 
 "tôi thấy mình hiểu rồi" không nằm trong bảng này. Quiz kiểm tra mức 2–3; lab kiểm tra mức 3–4; 
 phỏng vấn kiểm tra mức 4–5.

| Mức | Bạn làm được điều này chưa? | Nếu chưa, quay lại |
| --- | --- | --- |
| 1 · Nhớ | Kể tên 5 pattern theo đúng thứ tự thang leo, và 3 lý do chính đáng để multi-agent. | Slide 11 · Cheat sheet |
| 2 · Hiểu | Giải thích bằng lời của bạn vì sao Sectioning và Voting khác nhau, và vì sao debate cần model đa dạng — 
 không dùng lại nguyên văn câu trên slide. | Các Ô kiểm tra cuối chương 2 và 4 |
| 3 · Áp dụng | Cho một bài toán mới chưa từng thấy, chạy hết khung 5 bước và chọn được pattern kèm lý do. | Bài 1 → 2 → 3, làm đúng thứ tự |
| 4 · Phân tích | Nhìn một hệ multi-agent của người khác và chỉ ra được failure mode nguy hiểm nhất cùng chỗ thiếu guard. 
 Đây chính là việc peer review ở slide 31 yêu cầu. | Rubric slide 31 · Hình 3 — MAST |
| 5 · Đánh giá | Bảo vệ được một lựa chọn kiến trúc trước người phản biện — kể cả khi lựa chọn đó là 
 " không dùng multi-agent" — bằng số liệu chứ không bằng sở thích. | Câu trả lời phỏng vấn dựng sẵn · 6 hiểu lầm |

từ chối

chứng minh được
