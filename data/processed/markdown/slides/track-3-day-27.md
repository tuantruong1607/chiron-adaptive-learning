---
schema_version: 1
course_id: rag-intensive
document_id: "fc905930-37a4-56ff-964d-de6effd03819"
document_version_id: "8f09c61f-abdf-55b2-adfe-8e2019ed608f"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Human-in-the"
source_file: "track 3 - day 27.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 27.pdf"
source_sha256: "831bbd76267b32ca7dd76a46283f751843c227e20a200076835dc3308da6e45a"
parser_version: chiron-structured-markdown-v1
page_count: 29
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":29}"
language: vi
---

# Human-in-the

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"0fabc80a-993e-54b0-96a2-d756272b830a","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Human-in-the","extraction_method":"pdf-text-layer"},"checksum":"59293bb62cbd76ff12c366d6683c709bbbabd60266a46dfb7f931329ea22f527"} -->

## Slide 1 - Human-in-the

Human-in-the- Loop UX — Khi Nào Agent Cần Xin Phép? AICB-P2T3 · Ngày 27 · Chương 6 — Agent trong Production Giảng viên VinUniversity · Phase 2 · Track 3 · T uần 6

---

<!-- chiron-source-span: {"source_span_id":"35e19a55-fb62-5b78-bb49-8f4eeeb5c9d8","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"8ad60942ab412aafb462a6598e760de46820ea8bbced1682fb8ee5b72472884e"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Agent tự quyết hay hỏi người dùng — ranh giới nào là an toàn và không làm phiền?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

---

<!-- chiron-source-span: {"source_span_id":"1516224e-764a-5ac8-8d8f-b5703651dbe4","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội dung vận hành","extraction_method":"pdf-text-layer"},"checksum":"7b6f7a7946bd941f3a2bf973c97448228836170e670b454b45e61b2dd8d4275c"} -->

## Slide 3 - Nội dung vận hành

1. Tại sao Full Autonomy nguy hiểm?

2. HITL Taxonomy — 5 Interaction Patterns

3. Confidence Routing — Khi nào interrupt?

4. Approval Workflows & Implementation

5. Feedback Loops & Audit Trails

6. HITL UX Best Practices

7. Demo & Thực hành Giảng viên (VinUni) AICB · Ngày 27 T uần 6 1 / 17

---

<!-- chiron-source-span: {"source_span_id":"113a7c0c-cf5d-552f-82c2-e837d35814a7","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"T ại sao Full Autonomy nguy","extraction_method":"pdf-text-layer"},"checksum":"7e742cda5299da5273335db8086b4fff91e4a9afe77956f39bd184aa9ed4951a"} -->

## Slide 4 - T ại sao Full Autonomy nguy

01 hiểm? T ừ sự cố thực tế đến nhu cầu Human-in-the-Loop

---

<!-- chiron-source-span: {"source_span_id":"7c4ae26f-7d60-5682-ad2e-54da31028361","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Agent tự ý hành động — chuyện gì xảy ra?","extraction_method":"pdf-text-layer"},"checksum":"6ca75ad5709b8e6fc7795863c6f881c6305e34891955ddb305775560495808d4"} -->

## Slide 5 - Agent tự ý hành động — chuyện gì xảy ra?

User request Agent suy luận Xoá database Mất dữ liệu confidence 62% không ai kiểm tra! Không có approval gate

### Sự cố thực tế

- Agent CS auto-refund $50K
không cần duyệt

- Code agent xoá branch
production

- Email agent gửi nội bộ ra ngoài
Lưu ý: Full autonomy chỉ an toàn khi mọi action đều reversible và low-cost. Trong thực tế, rất ít action thoả mãn cả hai. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 2 / 17

---

<!-- chiron-source-span: {"source_span_id":"bb2c1838-af21-55d1-af7b-624960806e1b","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Analogy: Quy trình duyệt chi công ty","extraction_method":"pdf-text-layer"},"checksum":"8b315dc54898a244d49cf5bbfc9f48dc9eb93e9371eedc137d62fa1c786497ad"} -->

## Slide 6 - Analogy: Quy trình duyệt chi công ty

< 5 triệu T ự duyệt 5–50 triệu Trưởng phòng ký > 50 triệu Giám đốc duyệt Auto-approve 1 approval Multi-level Dưới threshold → agent tự xử lý Vùng trung gian → cần 1 lần duyệt Rủi ro cao → phải escalate lên người có thẩm quyền Cùng nguyên tắc: chi phí sai lầm quyết định mức kiểm soát Giảng viên (VinUni) AICB · Ngày 27 T uần 6 3 / 17

---

<!-- chiron-source-span: {"source_span_id":"eda32c86-731e-56b6-8669-0f7090f1c45b","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"HITL T axonomy — 5 Interac","extraction_method":"pdf-text-layer"},"checksum":"90656d58bb88a8e8f463609d65f60462d8cb9840e4f756851f8a8365a246dc6f"} -->

## Slide 7 - HITL T axonomy — 5 Interac

02 HITL T axonomy — 5 Interac- tion Patterns Phân loại cách con người tham gia vào quyết định của agent

---

<!-- chiron-source-span: {"source_span_id":"822f4519-61fc-5b0f-8fc0-be7d2f26e07a","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Autonomy Spectrum — Từ tự động đến kiểm soát hoàn toàn","extraction_method":"pdf-text-layer"},"checksum":"93d74be58219cf5ce5b936061ea4a8a8dfd022f727a55d266037221f75501b57"} -->

## Slide 8 - Autonomy Spectrum — Từ tự động đến kiểm soát hoàn toàn

Full Manual Người làm hết HITL Strict Duyệt mọi action HITL Bal- anced Duyệt theo risk HITL Light Chỉ audit log Full Auto Agent tự quyết An toàn cao Tốc độ caoSweet spot Không có vị trí “đúng” cố định — sweet spot phụ thuộc vàodomain risk, agent maturity, và user tolerance. Bắt đầu strict, nới dần khi trust được xây dựng. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 4 / 17

---

<!-- chiron-source-span: {"source_span_id":"ab78e8a7-30c6-5b8f-b8fc-822343fb84b1","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"5 HITL Interaction Patterns","extraction_method":"pdf-text-layer"},"checksum":"5818e8feaa5f61717998760eec93f17d766f8eeba64de927b93ff5e6c43a15db"} -->

## Slide 9 - 5 HITL Interaction Patterns

# Pattern Khi nào? Ví dụ 1 Approval Action cao rủi ro Deploy, xoá data, gửi email 2 Clarification Input mơ hồ “Bạn muốn report Q1 hay Q2?” 3 Escalation Vượt khả năng Câu hỏi pháp lý, tài chính 4 Review Checkpoint Kết quả cần kiểm Draft email, code PR 5 Edit / Correction User muốn chỉnh Sửa nội dung trước gửi Read-only = auto Write/Update = log + optional approval Delete/Deploy = mandatory ap- proval Review: approve/reject nguyên bản Edit: human chỉnh sửa nội dung Common cho content generation tasks Giảng viên (VinUni) AICB · Ngày 27 T uần 6 5 / 17

---

<!-- chiron-source-span: {"source_span_id":"573b07f8-a9c8-58ad-ab27-6982a9183a55","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Confidence Routing — Khi nào","extraction_method":"pdf-text-layer"},"checksum":"1647991931cff03a1ed0d05b47fd18129316f8f48390270ad3992fa9f366f9d8"} -->

## Slide 10 - Confidence Routing — Khi nào

03 interrupt? Agent tự đánh giá confidence để quyết định hỏi hay tự làm

---

<!-- chiron-source-span: {"source_span_id":"3d4d45dd-5949-59b7-946a-fb0ca93d7bf7","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Confidence Routing — Luồng quyết định","extraction_method":"pdf-text-layer"},"checksum":"9ff9c56c916b8ec8a6769f10c0d581ab58640eb1835bb7a6ff4bd4b9681a8a6a"} -->

## Slide 11 - Confidence Routing — Luồng quyết định

Agent Action Confidence? Auto-execute (log only) Suggest + Wait (user confirms) Ask Human (full context) ≥ 0.85 0.70–0.85 < 0.70 Policy Override delete/deploy/PII

- always ask
Lưu ý: Dù confidence = 0.99, agent vẫn PHẢI dừng nếu action vi phạm policy cố định (dữ liệu nhạy cảm, email external, deploy production). Giảng viên (VinUni) AICB · Ngày 27 T uần 6 6 / 17

---

<!-- chiron-source-span: {"source_span_id":"d1cc6a38-1007-57e8-b51f-78c00e25cdd1","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Nguyên tắc: Cost of Interrupt vs Cost of Error","extraction_method":"pdf-text-layer"},"checksum":"7bf17664f08c3784975499f83b8250e8cc3e3f2ace182786288a858af8b9cd63"} -->

## Slide 12 - Nguyên tắc: Cost of Interrupt vs Cost of Error

$10 Cost of error thấp → đừng hỏi 0.70 Confidence threshold mặc định $10K Cost of error cao → luôn hỏi Đo accuracy vs confidencetrên historical data. Nếu confidence 0.80 mà ac- curacy chỉ 60% → threshold quá thấp, cần nâng lên. Đây là empirical tuning, không có magic number. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 7 / 17

---

<!-- chiron-source-span: {"source_span_id":"71da6305-4e52-5e07-acb5-2963709ed6f8","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Approval Workflows & Imple","extraction_method":"pdf-text-layer"},"checksum":"347651d3dde3db365622ebf2929a583d8db5d7390a1e20d37733d4fdbcd73b93"} -->

## Slide 13 - Approval Workflows & Imple

04 Approval Workflows & Imple- mentation LangGraph interrupt/resume và Streamlit approval UI

---

<!-- chiron-source-span: {"source_span_id":"01e19e87-7740-55d6-a228-8bb9470bff70","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"LangGraph HITL — Interrupt & Resume","extraction_method":"pdf-text-layer"},"checksum":"a812756540ad34c704ef154099fc62441dba9e49f1cd6023bde199a1373cf4a2"} -->

## Slide 14 - LangGraph HITL — Interrupt & Resume

plan act INTERRUPT human review resume END destructive approve reject → abort

### Hai loại interrupt

- interrupt_before: pause trước
destructive action

- interrupt_after: pause sau draft
generation (review trước send)

1. Xem pending action + confi- dence

2. Human approve/reject/edit

3. Update state → continue graph

4. Multi-step: nhiều interrupt points Giảng viên (VinUni) AICB · Ngày 27 T uần 6 8 / 17

---

<!-- chiron-source-span: {"source_span_id":"cf857298-96e8-533a-873c-a344f0ad4e57","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"LangGraph HITL — Code-Level","extraction_method":"pdf-text-layer"},"checksum":"a957aaf013d9fed6da3c5c056c383933edb12953103df5308cac316cf71c6b21"} -->

## Slide 15 - LangGraph HITL — Code-Level

# Compile with interrupt graph = builder. compile( interrupt_before=["delete_action"], checkpointer=MemorySaver(), ) # Run until interrupt state = graph.invoke( input, config) print(state["pending_action"]) # => {"action": "delete_user", # "confidence": 0.62} # Human approves -> resume graph.update_state( config, { "approved": True} ) result = graph.invoke(None, config)

### 3 bước implement

1. Define interrupt nodes: liệt kê tất cả destructive actions

2. State inspection: pending action + confidence + reasoning

3. Resume logic: update approved/rejected rồi continue Lưu ý: Luôn dùng checkpointer — không có persistence, graph “quên” state khi interrupt. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 9 / 17

---

<!-- chiron-source-span: {"source_span_id":"98500d9b-646d-5d46-a147-e89ffcd459ac","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Streamlit HITL UI — Approval Interface","extraction_method":"pdf-text-layer"},"checksum":"62cafa0b0ee48cfa1f3846f2976ff6c0ec7d5effd7142feba00bea2487495c52"} -->

## Slide 16 - Streamlit HITL UI — Approval Interface

Agent Approval Request Action: delete_user(id=42) Confidence: 62% (below threshold) Reason: “User inactive 2 years” - user: {id: 42, name: “Nguyên”, status: active} Approve Reject Edit

### UI components

1. Action card: hiển thị pending action + confidence

2. Reasoning: giải thích tại sao agent muốn làm

3. Diff view: proposed changes highlighted

4. 3 buttons: Approve / Reject / Edit Mobile: Telegram bot approve/re- ject Batch: group low-risk actions → approve in bulk để giảm fatigue Giảng viên (VinUni) AICB · Ngày 27 T uần 6 10 / 17

---

<!-- chiron-source-span: {"source_span_id":"3e5f3b5d-3940-5e4b-a0ca-35fd9d86c123","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Feedback Loops & Audit Trails","extraction_method":"pdf-text-layer"},"checksum":"e833ca963521492e21d06dceb29ac722fe7f0e3cbb6999c144b65433c54f7029"} -->

## Slide 17 - Feedback Loops & Audit Trails

05 Thu thập phản hồi, ghi log, và tăng autonomy dần

---

<!-- chiron-source-span: {"source_span_id":"1bbb8de1-bdcb-58fd-8826-432d1e35dd8a","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Audit Trail — Mỗi quyết định đều được ghi lại","extraction_method":"pdf-text-layer"},"checksum":"52444e72281b9c5ad4962f42078d564430cef4953c80dc6a73647b6dd1d20a36"} -->

## Slide 18 - Audit Trail — Mỗi quyết định đều được ghi lại

```text
class AuditEntry(BaseModel):
```
timestamp: datetime agent_id: str action: str confidence: float risk_level: str # low/med/high reviewer_id: str | None decision: str # auto/approve/reject reason: str | None execution_time_ms: int # Immutable: append-only PostgreSQL # Backup: S3 daily snapshot # Replay: reconstruct full session

### Mỗi event ghi

- Who: agent nào, reviewer nào

- What: action gì, confidence bao
nhiêu

- When: timestamp chính xác

- Why: reasoning của agent +
decision Lưu ý: Audit trail là compliance requirement (GDPR, SOC2).

```text
Build from day one — cannot
```
retrofit sau khi đã production. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 11 / 17

---

<!-- chiron-source-span: {"source_span_id":"c7c15010-d94e-5505-839b-99523da46042","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Decision Analytics — Đo lường để cải thiện","extraction_method":"pdf-text-layer"},"checksum":"f5d6436b1061e7156323b4b7041a942245c2498aba36791b4c66dd27264aecb6"} -->

## Slide 19 - Decision Analytics — Đo lường để cải thiện

Approval rate 87% approved Response time median 45s Override rate 3% auto-rejected Agent đáng tin cậy

- nới threshold

### 3 metrics quan trọng

1. Approval rate: cao → agent đáng tin, nới dần autonomy

2. Response time: lâu → UI gây phiền, cần batch approval

3. Override rate: cao → confidence calibration sai Track metrics theo thời gian. Approval rate ổn định > 90% → tăng auto threshold. Trust builds incrementally. Giảng viên (VinUni) AICB · Ngày 27 T uần 6 12 / 17

---

<!-- chiron-source-span: {"source_span_id":"7350885a-c8fa-51b9-8f97-6e5442cc779d","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"HITL UX Best Practices","extraction_method":"pdf-text-layer"},"checksum":"52a29cf466dd2a8532b3ec3c154a93f3c9d08ec6d24ee4cd21cd1024345327ef"} -->

## Slide 20 - HITL UX Best Practices

06 Thiết kế trải nghiệm không làm phiền user

---

<!-- chiron-source-span: {"source_span_id":"fe70d418-7781-53db-a135-a7a23b5ed7fd","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"HITL UX — 5 Nguyên tắc vàng","extraction_method":"pdf-text-layer"},"checksum":"d32e7e4cb03802f4645dfa0b5ec42348278fccc2adb7c25968a6249c317247dd"} -->

## Slide 21 - HITL UX — 5 Nguyên tắc vàng

1 Start strict, loosen gradually — bắt đầu duyệt mọi thứ, nới dần khi agent chứng minh tin cậy 2 Preemptive clarification — detect ambiguity ở đầu vào, không phải giữa chừng execution 3 Explainable proposals — “Confidence 65% because [X]” giúp human quyết nhanh hơn 4 Batch approvals — group low-risk actions → approve in bulk để giảm interrupt fatigue 5 Progressive autonomy — track approval rate over time, auto-adjust threshold Giảng viên (VinUni) AICB · Ngày 27 T uần 6 13 / 17

---

<!-- chiron-source-span: {"source_span_id":"686894d3-5a70-5cbb-9a14-6e5f0244a63b","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Demo & Thực hành","extraction_method":"pdf-text-layer"},"checksum":"a9055fb4dabee66874272304fcce7791d03135ea6daf3a40c69dd5f3432f0ae5"} -->

## Slide 22 - Demo & Thực hành

07 HITL Code Review Agent + Lab hands-on

---

<!-- chiron-source-span: {"source_span_id":"f1e6fc83-086f-53cb-a983-8339b2c8c048","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"HITL Code Review Agent — Side-by-side","extraction_method":"pdf-text-layer"},"checksum":"82337e0d13d841e9a3af12437ac0e3295353d62d17bf0ef1a948ef6b53c0d091"} -->

## Slide 23 - HITL Code Review Agent — Side-by-side

1. Agent đọc PR, phân tích code changes, đề xuất review comments

2. Confidence 72%: hiển thị diff + reasoning → user Approve → agent commit

3. Confidence 58%: escalate — hiển thị context + câu hỏi cụ thể cho reviewer

4. Mỗi interaction ghi vào PostgreSQL audit trail — replay full session Giảng viên (VinUni) AICB · Ngày 27 T uần 6 14 / 17

---

<!-- chiron-source-span: {"source_span_id":"b94376d2-7b4a-5884-8659-e35caabd43bb","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Lab #27","extraction_method":"pdf-text-layer"},"checksum":"f2f671d0ee8c368c717d28e05a6f5391a64aa19c5701b399acb4f76f9a1eb8f2"} -->

## Slide 24 - Lab #27

Mục tiêu: Build HITL agent với LangGraph interrupt + Streamlit approval UI Deliverable: HITL agent + approval UI + confidence-based routing + Post- greSQL audit trail Thời gian: 2 giờ Giảng viên (VinUni) AICB · Ngày 27 T uần 6 15 / 17

---

<!-- chiron-source-span: {"source_span_id":"66731157-4451-5b46-adc8-5c8b65a1f106","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Lab 27 — Các bước thực hành","extraction_method":"pdf-text-layer"},"checksum":"fd0fbf0cbf6ee676b5d9322a8d11d497d2285024e2b45dc687225ee33d191813"} -->

## Slide 25 - Lab 27 — Các bước thực hành

1. Approval workflow: LangGraph interrupt_before cho delete/deploy actions

2. Confidence routing: auto khi ≥ 0.85, suggest khi 0.70–0.85, ask khi < 0.70

3. Streamlit UI: action card + diff view + Approve/Reject/Edit buttons

4. Audit trail: PostgreSQL append-only log, replay session, export report A/B test: full-auto vs HITL — đo user trust score và task success rate trên 20 test cases Giảng viên (VinUni) AICB · Ngày 27 T uần 6 16 / 17

---

<!-- chiron-source-span: {"source_span_id":"340790ac-6886-58bd-8701-0e504a52b811","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"ffa3118ea4db31c1b3ea89eb9165755a1a3c4f5c271783d03399320f73f4747e"} -->

## Slide 26 - T ổng kết — Key T akeaways

Những ý chính cần nhớ sau buổi học hôm nay 1 HITL là responsible deployment — xây dựng trust incrementally, không phải dấu hiệu yếu kém 2 Confidence routing: 3 vùng (auto / suggest / ask) + policy override cho high-risk ac- tions 3

```text
Audit trail là compliance requirement — build from day one, cannot retrofit sau khi
```
production 4 Progressive autonomy: start strict, đo metrics, nới dần — approval rate > 90% là tín hiệu tốt Giảng viên (VinUni) AICB · Ngày 27 T uần 6 16 / 17

---

<!-- chiron-source-span: {"source_span_id":"7570dc32-6d13-59c4-b2f3-da7f7aad94b8","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"a975c6973dc954966b4f71aae72a888a4fbd8c43752804913540aff38b498436"} -->

## Slide 27 - Tiếp theo & Bài tập

Ngày 28: Workshop T ổng Hợp — Full Production Agent System “Tất cả components đã build xong — N28 là ngày ghép lại thành hệ thống production hoàn chỉnh”

- Hoàn thành Lab 27: HITL
agent + audit trail

- Review lại tất cả labs
N16–N27 — chuẩn bị integration Giảng viên (VinUni) AICB · Ngày 27 T uần 6 17 / 17

---

<!-- chiron-source-span: {"source_span_id":"8472191c-fbbf-5a92-9252-441f23faf39f","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"f75b3a0a276e63b5d0548f82784e461073895c0c203a050238add3a3666bc5c8"} -->

## Slide 28 - Hỏi & Đáp

HITL có làm chậm agent không? Khi nào nên bỏ approval gate?

---

<!-- chiron-source-span: {"source_span_id":"98b1b01d-da61-5530-b6dc-22f0b2c453ed","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"ef6b6aced3a3a94494029dedb77136e942d6cc11377aea4174f403b05ea9a8d5"} -->

## Slide 29 - Cảm ơn!

AICB-P2T3 · Ngày 27 · Human-in-the-Loop UX github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn
