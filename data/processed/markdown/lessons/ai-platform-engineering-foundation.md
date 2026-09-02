---
schema_version: 1
course_id: rag-intensive
document_id: "5a495aaf-bbad-5f53-8a52-f94c7d989d80"
document_version_id: "180af068-557c-5e1f-871b-bef5908c3741"
document_kind: interactive_lesson
source_type: course_html
authority: primary
title: "AI Platform Engineering, từ mô hình đến production"
source_file: "ai-platform-engineering-foundation.html"
source_path: "C:\\Users\\banka\\Documents\\Multi Agent\\ontap\\out\\ai-platform-engineering-foundation.html"
source_sha256: "edbce5c52eda6de54458377a4a3ec43832cd6d5fb6cbf26a6322b4b14ec93108"
parser_version: chiron-structured-markdown-v1
html_section_count: 10
interactive_module_count: 0
interactive_control_count: 0
language: vi
---

# AI Platform Engineering, từ mô hình đến production

> Nắm nền tảng để ôn thi, hiểu toàn hệ thống và bước vào chuyên đề sâu mà không học rời từng công nghệ.

<!-- chiron-source-span: {"source_span_id":"cf9862d6-eef9-550c-972b-546ff2532948","locator":{"kind":"html_section","section_id":"study","order":1,"heading":"Đọc để nhớ, không chỉ đọc để thấy quen","source_file":"ai-platform-engineering-foundation.html"},"checksum":"bd90988545eaceccae249c7aef2e566725c9a8299e531fa557a0a956795822a7"} -->

## Đọc để nhớ, không chỉ đọc để thấy quen

Ba lượt học, mỗi lượt có một đầu ra rõ để bạn biết mình đã thực sự hiểu.

20 phút

Lấy bản đồ

Kể lại 5 lớp

60 phút

Nối nguyên nhân

Chẩn đoán kiến trúc

30 phút

Active recall

Đạt 9/12 mục

---

<!-- chiron-source-span: {"source_span_id":"cc36fcb2-40b0-55cb-8f8a-acc7571d38f3","locator":{"kind":"html_section","section_id":"overview","order":2,"heading":"Bức tranh toàn hệ thống","source_file":"ai-platform-engineering-foundation.html"},"checksum":"bc79b1a3bb8d6e2004f230de11b5c0b3c4f2526fac711a429f5ec77eaf1dc7f1"} -->

## Bức tranh toàn hệ thống

AI production là chuỗi quyết định có thể đo, kiểm soát và truy vết. Model chỉ là một thành phần.

Problem

→

Data

→

Intelligence

→

Control

→

Operations

### Quality, latency, cost luôn kéo nhau

Model lớn, reranker, debate và judge đều có lợi ích nhưng phải đo trên workload thật.

Nhớ:

### Không baseline thì không biết AI tạo giá trị

Đo hiện trạng, offline eval trước deploy và online sample sau deploy.

Nhớ:

---

<!-- chiron-source-span: {"source_span_id":"1d438409-2516-5b4a-a672-c6d3da809be4","locator":{"kind":"html_section","section_id":"foundation","order":3,"heading":"LLM và Agent: hiểu đúng bộ não","source_file":"ai-platform-engineering-foundation.html"},"checksum":"fc8f7c2687f3b4d7dc41421079c0a50725f7cd9b4bcc05f5a32fc5bdacec6b7c"} -->

## LLM và Agent: hiểu đúng bộ não

Nền tảng là next-token prediction, vòng đời huấn luyện và lớp ứng dụng bọc model bằng state, tool, memory.

### AI chứa ML, ML chứa Deep Learning

Generative AI tạo dữ liệu mới. LLM là foundation model xử lý token.

Bẫy thi:

### LLM dự đoán token tiếp theo

Predict, append, rerun. Văn bản trôi chảy không bảo đảm sự thật.

Hệ quả:

### Từ foundation model đến trợ lý

Pre-training

→

SFT

→

Alignment

→

Test-time

Phân biệt:

### Prompt production là hợp đồng

Role, Task, Context, Format. System prompt thêm capabilities, constraints, handler, output contract.

### LLM không tự chạy tool

Model sinh yêu cầu. Ứng dụng validate, thực thi và trả tool result về context.

---

<!-- chiron-source-span: {"source_span_id":"7a7c4013-2d3d-584d-aca0-cdbe64de0ece","locator":{"kind":"html_section","section_id":"product","order":4,"heading":"Bài toán và sản phẩm: chọn mức tự động hóa thấp nhất đủ dùng","source_file":"ai-platform-engineering-foundation.html"},"checksum":"42021adc3a1a34cf3529043fe99f5b05e32a5af8f13d61b5050c92e793a97a53"} -->

## Bài toán và sản phẩm: chọn mức tự động hóa thấp nhất đủ dùng

Xác định pain point, impact of error và quyền tự chủ trước khi chọn công nghệ.

Tiêu chí

Rule

Workflow

Agent

Dùng khi

Logic rõ, ổn định.

Input linh hoạt, flow đã biết.

Mục tiêu rõ, đường đi đổi.

Điều phối

`if/else`

Code định bước.

Model chọn bước.

Rủi ro

Thiếu ngoại lệ.

Luồng cứng.

Loop, cost, action sai.

Ưu tiên

Mặc định.

Khi input khó.

Khi tự chủ tạo giá trị.

### Chín trường cần rõ

1. Actor, workflow
2. Bottleneck, cost
3. Impact of error, boundary
4. AI intervention, AI level
5. HITL

Câu khóa:

### Thiết kế đường sai trước đường đúng

Build slice có một user, task, quyết định AI, failure path. Khi bất định: Detect, Route, Recover, Learn.

### Augmentation, Copilot, Automation

Quyền tự chủ tăng theo bằng chứng, không theo niềm tin của đội build.

### PoC chứng minh kỹ thuật, MVE chứng minh trải nghiệm

MVP đến sau feasibility và value. ROI cần kịch bản bảo thủ, thực tế, lạc quan.

---

<!-- chiron-source-span: {"source_span_id":"9d63b3d7-3e4c-5ece-94cc-19d5c4f10eb3","locator":{"kind":"html_section","section_id":"rag","order":5,"heading":"Data và RAG: chất lượng bắt đầu trước lúc gọi model","source_file":"ai-platform-engineering-foundation.html"},"checksum":"4e2ca92a92ad29b2397e1f4d711363af0d296e2f7afd896fa98eb312494ad144"} -->

## Data và RAG: chất lượng bắt đầu trước lúc gọi model

RAG là hệ thống retrieval có generation ở cuối. Bằng chứng sai khiến câu trả lời sai thuyết phục hơn.

Transform

→

Retrieve

→

Rerank

→

Assemble

→

Generate

Debug:

### Knowledge, operational, contextual

Ba loại dữ liệu có nguồn sự thật và vòng đời khác nhau.

### Vector biểu diễn nghĩa, không lưu sự thật

Similarity cao không chứng minh nội dung đúng, mới hoặc đủ relevant.

### Chunk nhỏ để tìm, context lớn để hiểu

Fixed, recursive, semantic, parent-child là các mức đánh đổi context và precision.

### Đổi RAM và recall lấy tốc độ

IVF thu hẹp cụm, PQ nén, HNSW nhanh và recall cao nhưng tốn RAM.

### Pipeline phải chạy lại an toàn

Idempotency ngăn trùng, backpressure bảo vệ downstream, DLQ cách ly lỗi.

### Đo retrieval và generation riêng

Faithfulness đo bám nguồn, Relevancy đo trọng tâm, Context Recall đo đủ bằng chứng.

Học sâu:

Day 24 về RAGAS và LLM-as-Judge

---

<!-- chiron-source-span: {"source_span_id":"4ce177da-f63f-5aa1-80be-7459d4dea374","locator":{"kind":"html_section","section_id":"agents","order":6,"heading":"Kiến trúc Agent: state quan trọng hơn số lượng agent","source_file":"ai-platform-engineering-foundation.html"},"checksum":"9926754a5b9ac4239c55a759c3284963e1740dea0bc3811b3c369e46b17cbae6"} -->

## Kiến trúc Agent: state quan trọng hơn số lượng agent

Bắt đầu bằng loop nhỏ có giới hạn. Chỉ thêm pattern khi failure mode yêu cầu.

### Năm thành phần

Goal 
 ↓ 
 Reason → Act → Observe 
 ↑　　　　↓ 
 Memory ← State

Goal định hướng, reasoning chọn bước, perception đọc môi trường, action tác động và memory giữ thông tin.

Routing

Phân loại request và chuyển nhánh. Rẻ, nhanh, dễ kiểm soát.

Orchestrator-Worker

Phân rã, chạy phần độc lập, merge có quy tắc.

Debate và Critic

Cùng blind spot thì nhiều phiếu không thêm bằng chứng.

Autonomous loop

Cần max iterations, budget, timeout, policy, escalation.

### Node đổi State, Edge chọn đường

Persistence giúp resume. Interrupt tạo điểm chờ HITL.

### MCP nối tool, A2A nối agent

Interoperability không tự giải quyết orchestration, safety hay quality.

### Reflexion học trace, LATS tìm nhiều nhánh

Kiểm baseline Plan, Act, Verify trước search tree phức tạp.

### Bốn tầng, bốn mục đích

Short-term, episodic, semantic, user profile. Mọi write cần provenance và policy.

Học sâu:

Day 20 Multi-Agent

Day 23 LangGraph

---

<!-- chiron-source-span: {"source_span_id":"a3dbe7d0-0daf-57e4-bccc-6f4f5085e601","locator":{"kind":"html_section","section_id":"production","order":7,"heading":"Production: bảo vệ, quan sát, học từ lỗi","source_file":"ai-platform-engineering-foundation.html"},"checksum":"fea4100e99ef820f0f7aeb83da232338a2dbc6ee4521655393ca16f94c8fc3cc"} -->

## Production: bảo vệ, quan sát, học từ lỗi

Agent có state, chạy lâu và chờ I/O nên cần runtime, checkpoint và failure budget phù hợp.

### Reproducible image, task resume được

Multi-stage build, lock version, queue, checkpoint và timeout phù hợp.

### Gateway là biên kiểm soát

Rate limit, spending cap, tenant quota ngăn loop lỗi thành sự cố tài chính.

### Defense-in-depth bốn lớp

Input

Đồng bộ

Model

Không đứng một mình

Output

Trước hành động

Audit

Có thể async

### Risk và reversibility quyết định điểm xin phép

Confidence chỉ là tín hiệu. High-impact hoặc khó hoàn tác luôn cần policy override.

### Metrics báo có lỗi, trace nói lỗi ở đâu

Log cần trace_id, model, prompt version. Pillar thứ tư là online evaluation.

L1 Heuristic

L2 LLM Judge

L3 User signal

L4 Outcome

---

<!-- chiron-source-span: {"source_span_id":"cd58649d-1626-5bfb-81d7-22829c1d0575","locator":{"kind":"html_section","section_id":"eval","order":8,"heading":"Evaluation và alignment: biến cảm giác thành bằng chứng","source_file":"ai-platform-engineering-foundation.html"},"checksum":"69793db60f5685b6ebc8e2d3e411503b3c738df1f66daa426fb03939462ccf5a"} -->

## Evaluation và alignment: biến cảm giác thành bằng chứng

Cần dataset đại diện, rubric rõ, calibration với người và gate hồi quy.

### Đề thi phải giống traffic và có ca khó

Lấy mẫu theo intent, risk, tần suất. Version dataset cùng prompt và model.

### Vibe check khám phá, offline chặn, online tìm drift

Manual hiểu lỗi, offline bảo vệ thay đổi, online đo traffic thật.

### Judge cũng có bias

- Đảo thứ tự giảm position bias.
- Rubric giảm length và style bias.
- Model khác họ giảm self-enhancement.
- Calibration với người bằng kappa.

### Chọn theo khoảng cách cần sửa

RAG bổ sung knowledge; SFT/LoRA học task và format; DPO/ORPO học preference.

Học sâu:

Day 21 LoRA

Day 22 DPO/ORPO

Day 24 Evaluation

---

<!-- chiron-source-span: {"source_span_id":"c34f3c7e-5db0-5b76-9b08-76e73d9f252a","locator":{"kind":"html_section","section_id":"exam","order":9,"heading":"Active recall: trả lời trước khi mở đáp án","source_file":"ai-platform-engineering-foundation.html"},"checksum":"04033419d4a9665f495080dc50cf371e91648f9ef70a9c0db72ba89cb420d0cb"} -->

## Active recall: trả lời trước khi mở đáp án

Đánh dấu mục bạn giải thích được. Tiến độ lưu trên trình duyệt.

0/12

Next-token và hallucination

Rule, Workflow, Agent

9 trường Problem Statement

Pipeline RAG và reranker

Ba metric RAGAS

Năm thành phần Agent

Node, Edge, State

Bốn tầng memory

Bốn lớp guardrail

Risk và reversibility

Metrics, logs, traces, online eval

Bốn bias của Judge

#### Vì sao Agent không phải model mới?

Agent là ứng dụng đặt LLM trong control loop có goal, state, memory và tool.

#### Khi nào không nên dùng Agent?

Khi rule rõ, flow cố định, hậu quả khó giám sát, hoặc quyền tự quyết không tạo đủ giá trị.

#### Retrieval đúng nhưng answer sai, kiểm gì?

Context assembly, thứ tự, truncation, grounding, generation và output verification.

#### Nhiều Agent luôn tốt hơn?

Không. Lỗi tương quan khiến debate tăng cost nhưng không thêm bằng chứng độc lập.

#### Confidence cao đủ bỏ HITL?

Không. High-impact hoặc khó hoàn tác vẫn cần phê duyệt theo policy.

#### Offline và online eval khác gì?

Offline kiểm phiên bản trên tập chuẩn. Online đo traffic thật và drift.

---

<!-- chiron-source-span: {"source_span_id":"48df5719-af16-5324-8ebb-c2e68e48a6a2","locator":{"kind":"html_section","section_id":"advanced","order":10,"heading":"Cầu nối sang học chuyên sâu","source_file":"ai-platform-engineering-foundation.html"},"checksum":"1890b59fe29589d3c59498e7c89ecaeefa04cdb22cebd19ac022438885611301"} -->

## Cầu nối sang học chuyên sâu

Chọn chuyên đề theo failure mode bạn cần hiểu sâu.

### Multi-Agent Systems

Routing, supervisor, debate, shared state, failure budget.

### LoRA và QLoRA

Fine-tune ROI, adapter và VRAM.

### DPO, ORPO và Alignment

Preference learning và chosen-rejected.

### LangGraph Orchestration

State graph, checkpoint và interrupt.

### RAGAS, Judge và Guardrails

Evaluation triad, judge bias và safety.

Không tìm thấy. Thử “RAG”, “HITL” hoặc “memory”.
