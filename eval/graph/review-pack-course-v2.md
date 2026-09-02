# Chiron Graph-lite review pack — 10 candidates

Phạm vi: 5 node + 5 edge từ graph version draft. Check `Approve`, `Edit` hoặc `Reject`; production không dùng candidate trước khi duyệt.

## Node `ai_llm_foundations` — AI & LLM Foundations

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.84`
- Summary: Khái niệm AI tạo sinh, năng lực và giới hạn cốt lõi của mô hình ngôn ngữ.
- Source: **AI IN ACTION · NGÀY 5** — `{"kind": "page", "page": 21, "label": "Slide 21", "section_title": "④a Scope the solution: mô tả user flow end-to-end", "extraction_method": "pdf-text-layer"}`
- Source span: `15247bc7-2a63-505e-a925-7318973a608c`

> ④a Scope the solution: mô tả user flow end-to-end Bao gồm cả các bước KHÔNG có AI — đừng chỉ định nghĩa đoạn AI. Ví dụ: detect scheduling intent trong email xong → tự suggest giờ luôn, hay đưa user sang calendar app để hoàn tất? Click a button User bấm nút để invoke — ví dụ: summarize một chat thread. One-shot prompt Gõ prompt một lần vào text field — Notion brainstorm ý tưởng, Canva tạo graphic cho post. Pre-set prompts Prompt có sẵn để bấm — LinkedIn gợi ý takeaway questions trên mỗi post. Automated report Tự chạy theo lịch/sự kiện — Zoom meeting summary auto-start, Slack daily recap các chat bỏ lỡ. Automated suggestions Gợi ý hiện sẵn trong flow — Superhuman tóm tắt email 1 dòng, Vanta gợ

Reviewer note:

## Node `data_pipeline` — Data Pipeline

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.84`
- Summary: Luồng ingest, làm sạch, biến đổi, kiểm tra và xuất bản dữ liệu.
- Source: **AI Evaluation & Benchmarking** — `{"kind": "page", "page": 78, "label": "Slide 78", "section_title": "5 Whys Cho AI Failures", "extraction_method": "pdf-text-layer"}`
- Source span: `ca66bf1d-8d63-5206-ba4e-7ee88d03e712`

> 5 Whys Cho AI Failures Symptom: Agent trả lời sai về refund policy Why 1: Answer không dựa trên đúng document Why 2: Retriever không lấy được policy mới nhất Why 3: Policy mới chưa được index vào vector store Why 4: Ingestion pipeline không có scheduled re-index Root cause Vấn đề thật không phải prompt hay model. Vấn đề là data pipeline. Fix đúng chỗ sẽ giải quyết hàng loạt failures tương tự. Giảng viên (VinUni) AICB · Evaluation 2026 67 / 76

Reviewer note:

## Node `multi_agent_systems` — Multi-agent Systems

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.79`
- Summary: Phân vai và giao tiếp giữa nhiều agent khi một agent đơn không đủ phù hợp.
- Source: **Production RAG** — `{"kind": "page", "page": 42, "label": "Slide 42", "section_title": "AgenticRAG — 3 Kiến trúc chính", "extraction_method": "pdf-text-layer"}`
- Source span: `7d2dcc63-aedb-5b68-8e8a-17fa3c0139b2`

> AgenticRAG — 3 Kiến trúc chính Single-Agent Multi-Agent Hierarchical Môtả 1 agent điều phối toàn bộ retrieval+ routing Nhiều agent chuyên biệt, mỗiagent 1 data source Agent cấp cao delegate xuốngagent cấp thấp Ưuđiểm Đơngiản, latency thấp Scalable, parallel pro- cessing Strategic oversight, reli- able Nhược Không scale cho multi- domain Coordinationoverhead Latencycao, phức tạp Khinào SimpleQA, routing Multi-domainsynthesis High-stakes (medical, le- gal) Multi-agentsynthesis: agentschuyênbiệtcho sum- marization, extraction, reasoning → synthesis stagetổng hợp. Outperform strong RAG baselines trên 4 bench- marks. Dùng self-knowledge của model để filter retrieved docs. RL-basedtraining →modelb

Reviewer note:

## Node `model_fine_tuning` — Model Fine-tuning

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.80`
- Summary: Điều chỉnh trọng số model bằng dữ liệu miền khi prompting hoặc retrieval chưa đủ.
- Source: **Fine-tuning LLMs — phân tích & breakdown từng slide** — `{"kind": "html_section", "order": 6, "heading": "04 Dataset & Training Pipeline", "section_id": "c4", "source_file": "track-3-day-21.html"}`
- Source span: `c309566a-3e28-52dc-9a00-22fc9b351a55`

> 04 Dataset & Training Pipeline   Slide 15–22: chuẩn bị dữ liệu, ngân sách VRAM thực chiến, FlashAttention, và setup Unsloth + TRL.       Slide 15 Section divider   Trích slide   "04 — Dataset & Training Pipeline. Từ chuẩn bị dữ liệu đến chạy training với Unsloth + TRL"     Đây là chương quyết định thành bại. Chương 2–3 có thư viện làm hộ gần hết;   chương này thì không ai làm hộ được, vì dữ liệu là thứ duy nhất chỉ bạn mới có.         Slide 16 Dataset Preparation — Quality over Quantity   Trích slide   "Raw Data → Clean & Dedup (remove short outputs, filter templates, dedup) → Format (Alpaca/ChatML — match model template) → Train/Val Split   Quy mô cần thiết: ■ Style/format: 500–2k samples c

Reviewer note:

## Node `production_reliability` — Production Reliability Architecture

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Confidence: `0.84`
- Summary: Kết hợp retry, checkpoint, timeout, fallback, observability và governance thành kiến trúc chịu lỗi.
- Source: **LangGraph & Agentic Orchestration — phân tích & breakdown từng slide** — `{"kind": "html_section", "order": 14, "heading": "! Điểm cần kiểm chứng trước khi trích dẫn", "section_id": "numbers", "source_file": "track-3-day-23.html"}`
- Source span: `74abcbf4-9858-5b04-8d71-3792065bd783`

> ! Điểm cần kiểm chứng trước khi trích dẫn   Bài này ít số hơn hai bài trước, nhưng có vài chỗ đáng cẩn thận.     Nội dung Slide Trạng thái Nên dùng thế nào   Tên bài / số ngày 1 File tên "day 23", slide ghi "Day 08"; tác giả để trống Trích theo tên bài, đừng trích theo số ngày   "Memory / SQLite / Postgres saver" 20 Đúng, nhưng API và tên lớp đổi theo phiên bản LangGraph Ghim phiên bản trong requirements.txt và đọc doc đúng phiên bản   Độ trễ ghi checkpoint (0,05 / 2,5 / 5 ms) — Số minh hoạ của tài liệu này, không có trên slide Tự đo trên hạ tầng của bạn trước khi dùng để ra quyết định   Thông lượng serialize ~400 MB/s — Ước lượng của tài liệu này Chỉ để cảm nhận bậc độ lớn   Mô hình retry "

Reviewer note:

## Edge `e006`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `ai_product_delivery` — **applies_to** → `deployment_pipeline`
- Confidence: `0.86`
- Source: **Triển khai thực tế & Định hướng** — `{"kind": "html_section", "order": 8, "heading": "06 Scaling team và platform", "section_id": "c5", "source_file": "day15-trien-khai-thuc-te-dinh-huong.html"}`
- Source span: `553bc1cb-0f2c-5c39-858c-c819264703de`

> 06 Scaling team và platform   Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path? Slide 31 Scaling team và platform · Mental model & quyết định   Trích slide Slide 31: AI Product: T ăng Trưởng Nhanh Nhưng Thiếu Cửa Junior Demand & Lương AI PM postings: +300% trong 3 năm, nhân đôi năm 2025 Lương trung vị AI PM: $194–197K (hội tụ Glassdoor & axialsearch) AI Strategist: $208K trung vị, $279K ở cấp Director OpenAI PM trung vị: ~$860K Lưu ý: Chỉ 2% postings AI PM là cấp junior — 47% là cấp… AI Strategist còn nghiêng hơn: 69– 80% là Director/VP/C-suite.. Điểm nối sang production là: platform chỉ đáng xây khi nhiều use case dùng l

Reviewer note:

## Edge `e012`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `data_pipeline` — **prerequisite_of** → `rag_pipeline`
- Confidence: `0.86`
- Source: **Production RAG — Từ Ingestion đến Eval** — `{"kind": "html_section", "order": 3, "heading": "01 Production RAG mental model", "section_id": "c0", "source_file": "track-3-day-18.html"}`
- Source span: `08ad123e-3afd-5e5c-b622-001af97fa24e`

> 01 Production RAG mental model   Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path? Slide 1 Production RAG mental model · Mental model & quyết định   Trích slide Slide 1: Production RAG AICB-P2T3 · Ngày 18 · Chương 4 — Agent Nâng Cao M.Sc Trần Minh Tú VinUniversity · Phase 2 · Track3 ·Tuần4 Production RAG AICB-P2T3 · Ngày 18 · Chương 4 — Agent Nâng Cao M.Sc Trần Minh Tú VinUniversity · Phase 2 · Track3 ·Tuần4. Điểm nối sang production là: offline và online pipeline có failure mode khác nhau. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tên công cụ c

Reviewer note:

## Edge `e029`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `multi_agent_systems` — **prerequisite_of** → `supervisor_routing`
- Confidence: `0.86`
- Source: **RAG Pipeline** — `{"kind": "page", "page": 132, "label": "Slide 132", "section_title": "Multi-Agent Systems", "extraction_method": "pdf-text-layer"}`
- Source span: `8db1b137-0ec7-5007-adbf-e365d55ebf9b`

> Multi-Agent Systems ● Khi hệ thống lớn lên, một Agent không  thể ôm đồm mọi việc (quá tải System  Prompt). ● Cần chia nhỏ thành các Worker (Nhân  sự): 1 RAG Agent chuyên đọc tài liệu, 1  SQL Agent chuyên đọc số liệu, 1  Supervisor Agent làm sếp chỉ việc. ● Ngày 09: Chúng ta sẽ dùng LangGraph  để vẽ sơ đồ giao tiếp cho các Agent này. LANGGRAPH Supervisor HR_Doc RAG Agent Finance_SQL SQL Agent Web_Search Search Agent Giảng viên (VinUni) AICB · Python Ingestion Tuần 2

Reviewer note:

## Edge `e051`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `deployment_pipeline` — **applies_to** → `observability`
- Confidence: `0.86`
- Source: **Observability — Nhìn thấy Agent trong Production** — `{"kind": "html_section", "order": 6, "heading": "04 Distributed tracing & OpenTelemetry", "section_id": "c3", "source_file": "day-13.html"}`
- Source span: `95252153-5286-56d3-b801-c3b2b5198370`

> 04 Distributed tracing & OpenTelemetry   Đọc phần này bằng câu hỏi: tín hiệu nào buộc ta đổi thiết kế, và failure mode nào xuất hiện nếu chỉ làm theo happy path? Slide 32 Distributed tracing & OpenTelemetry · Mental model & quyết định   Trích slide Slide 32: 04 Structured Logging Log không cấu trúc giống ghi chú tay — khó search, khó aggre- gate. Structured logging biến log thành DATA query được 04 Structured Logging Log không cấu trúc giống ghi chú tay — khó search, khó aggre- gate.. Điểm nối sang production là: p95/p99 quan trọng hơn average cho trải nghiệm nhiều lượt. Đây là một quyết định hệ thống: phải chỉ rõ state nằm ở đâu, bằng chứng nào được ghi lại và hành vi khi dependency lỗi; tê

Reviewer note:

## Edge `e070`

- [ ] Approve  - [ ] Edit  - [ ] Reject
- Triple: `nondeterminism` — **applies_to** → `ai_evaluation`
- Confidence: `0.58`
- Source: **Mục lục bài học** — `{"kind": "html_section", "order": 1, "heading": "P1 Foundation — Day 1–15", "section_id": "section-001", "source_file": "index.html"}`
- Source span: `7a0516df-ccb3-5d31-8942-fa5a154742d8`

> P1 Foundation — Day 1–15   Day 1 AI & LLM Foundation 83 slide · tầng A Day 2 Xác định bài toán cho AI — Problem Statement 76 slide · tầng B Day 3 Từ Chatbot đến Agentic Agent — ReAct 46 slide · tầng B Day 4 Prompt Engineering & Tool Calling 43 slide · tầng B Day 5 AI Product Thinking & Requirements 44 slide · tầng A Day 6 AI Product & Project Management 37 slide · tầng A Day 7 Data Foundations — Embedding, Chunking & Vector Store 97 slide · tầng A Day 8 RAG Pipeline — Truy xuất & Sinh câu trả lời 139 slide · tầng A Day 9 Multi-Agent & Kết nối hệ thống — MCP, A2A, LangGraph 85 slide · tầng A Day 10 Data Pipeline & Data Observability 50 slide · tầng A Day 11 Guardrails, HITL & Responsible AI 1

Reviewer note:
