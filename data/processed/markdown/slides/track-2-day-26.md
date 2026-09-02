---
schema_version: 1
course_id: rag-intensive
document_id: "96a82a4d-ea1a-5c1b-aa2c-8c8a2ea7a620"
document_version_id: "a47cc1c5-d9c0-5b9b-8e4f-126f872ed497"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "© VinUniversity | All rights reserved"
source_file: "track 2 - day 26.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 2 - day 26.pdf"
source_sha256: "6ca604ba4e7bcee36c88db6e98431630fa16f57fc15aec70f9f875c66fd3f050"
parser_version: chiron-structured-markdown-v1
page_count: 17
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":17}"
language: vi
---

# © VinUniversity | All rights reserved

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"e816b48a-4968-59cf-bd87-ba78f8fc1f39","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"© VinUniversity | All rights reserved","extraction_method":"pdf-text-layer"},"checksum":"9491e03a4ec598d99224c17eb517596623205768404ad8427ae67c4f49267355"} -->

## Slide 1 - © VinUniversity | All rights reserved

MCP & A2A Infrastructure

---

<!-- chiron-source-span: {"source_span_id":"1da08506-596a-5ccb-9b7a-52db6bd14b3a","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"Mục tiêu bài học","extraction_method":"pdf-text-layer"},"checksum":"974d81b222c95347f922f385257cc8fb1c4ac0b55ce578ee349975fea4bc600d"} -->

## Slide 2 - Mục tiêu bài học

Knowledge — Skills — Lộ trình 5 phần 🧠 Kiến thức (Knowledge)

- Phân biệt monolithic LLM vs multi-agent system

- Khái niệm A2A: AgentCard, Task, Message, Part, Artifact

- Vai trò của MCP — bổ trợ A2A như thế nào

- Khi nào dùng A2A vs khi nào dùng MCP
🛠️Kỹ năng (Skills)

- Đọc và triển khai AgentCard JSON đúng chuẩn

- Dùng LangGraph StateGraph + Send API để fan-out song song

- Cấu hình service discovery động qua Registry

- Trace một yêu cầu xuyên qua nhiều agent với trace_id
Lộ trình 5 phần Phần 1. Bối cảnh — vì sao multi-agent? Lộ trình tiến hoá LLM Phần 2. MCP — chuẩn cho LLM kết nối công cụ và dữ liệu Phần 3. A2A — chuẩn cho các agent giao tiếp với nhau Phần 4. So sánh A2A vs MCP — khi nào dùng cái nào? Phần 5. Case study: hệ thống tư vấn pháp lý phân tán

---

<!-- chiron-source-span: {"source_span_id":"ce0b5818-16f3-5fdd-9e57-04c6d1ec9e28","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Lộ trình tiến hoá LLM (Stage 1 → 5)","extraction_method":"pdf-text-layer"},"checksum":"d4c22a3c087ed76bd7fba82ace1ffcd5afc497166b8cd7e51ddb951a3b73e08d"} -->

## Slide 3 - Lộ trình tiến hoá LLM (Stage 1 → 5)

Từ gọi API đơn giản đến mạng lưới agent phân tán

---

<!-- chiron-source-span: {"source_span_id":"2debec18-de3d-50cb-b8ff-cd8565cfe6ff","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Vì sao cần Multi-Agent?","extraction_method":"pdf-text-layer"},"checksum":"972a013c1eb42a02d6caa960ff4c89dad5b076cde40c3b1b2158b940646828bd"} -->

## Slide 4 - Vì sao cần Multi-Agent?

Hạn chế của LLM đơn lẻ và lợi thế của hệ chuyên gia

---

<!-- chiron-source-span: {"source_span_id":"a470b0f6-23ef-5325-be88-071d25af26e6","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Hai chuẩn mới của thế hệ AI Agent","extraction_method":"pdf-text-layer"},"checksum":"e1b5cd28ef45d1b507d7cb8621e3dbf74796cd56551b647fed4b2970dbac2bb1"} -->

## Slide 5 - Hai chuẩn mới của thế hệ AI Agent

A2A và MCP — bổ sung lẫn nhau, không thay thế 🔌 MCP — Model Context Protocol Do Anthropic giới thiệu (2024) “USB-C cho AI” — chuẩn để LLM kết nối với nguồn dữ liệu và công cụ.

- Client–Server architecture

- Server cung cấp: resources, tools, prompts

- LLM (client) gọi tool, đọc file, query DB qua chuẩn chung

- Quan hệ: LLM ↔ Tool / Data
🤝 A2A — Agent-to-Agent Protocol Do Google giới thiệu (2025) Chuẩn để các agent độc lập giao tiếp như những đối tác bình đẳng.

- Peer-to-peer architecture

- Server công bố: AgentCard, skills, tasks

- Agent có thể uỷ thác (delegate) công việc cho agent khác

- Quan hệ: Agent ↔ Agent
Phép loại suy MCP ≈ USB-C → 1 thiết bị (LLM) cắm với nhiều phụ kiện (DB, API, file). A2A ≈ TCP/IP → nhiều máy độc lập trên mạng nói chuyện với nhau. 💡 Thực tế dùng cả hai: một agent A2A bên trong vẫn có thể dùng nhiều MCP server để truy cập dữ liệu.

---

<!-- chiron-source-span: {"source_span_id":"856d98a5-7850-5447-ac95-5844eb2579e2","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"MCP — Model Context Protocol","extraction_method":"pdf-text-layer"},"checksum":"d3b2d8f1ca5dc817656552e404340b9e93ddafa5bf650233d93627b5c26990ee"} -->

## Slide 6 - MCP — Model Context Protocol

Chuẩn hoá kết nối giữa LLM với thế giới bên ngoài Vấn đề MCP giải quyết Trước MCP: mỗi ứng dụng AI tự viết tích hợp riêng cho từng công cụ. Bài toán N × M: N ứng dụng × M công cụ = N × M tích hợp. Với MCP: mỗi công cụ chỉ cần một MCP Server, mỗi ứng dụng AI chỉ cần một MCP Client. Tổng tích hợp giảm xuống N + M. ┌──────────────┐ stdio / SSE / HTTP ┌──────────────────┐ │ │ ◄───────────────────► │ │ │ MCP Host │ JSON-RPC 2.0 │ MCP Server │ │ (Claude, │ │ (filesystem, │ │ Cursor, │ │ GitHub, DB, │ │ IDE…) │ │ Slack…) │ └──────────────┘ └──────────────────┘ ▲ │ │ user prompt ▼ │ ┌──────────────────┐ └──── LLM gọi tools ◄──────────────│ Resource / Tool /│ │ Prompt │ └──────────────────┘ 3 thành phần cốt lõi của MCP Server

- Resources — dữ liệu chỉ đọc (file, log, snapshot DB)

- Tools — hàm có side-effect (gửi email, chạy SQL, tạo PR)

- Prompts — mẫu prompt tái sử dụng (templates)
Khi nào dùng MCP

- Cần cho LLM quyền truy cập dữ liệu / công cụ nội bộ

- Muốn tách phần kết nối khỏi logic agent (loose coupling)

- Reuse cùng một MCP server cho nhiều IDE / app khác nhau

- Cần kiểm soát quyền: phê duyệt từng lần gọi tool

---

<!-- chiron-source-span: {"source_span_id":"ff09d188-1950-5d00-ae63-fa35cb5fe628","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Agent2Agent (A2A) Protocol","extraction_method":"pdf-text-layer"},"checksum":"6f907189a6edf38496afe3c5eb6c811cc6fedd78990b118031dfebd6f021af78"} -->

## Slide 7 - Agent2Agent (A2A) Protocol

Chuẩn mở của Google cho giao tiếp giữa các AI agent

---

<!-- chiron-source-span: {"source_span_id":"bb22e689-c733-5378-a50e-fb52b87f6faa","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"A2A — Khái niệm cốt lõi","extraction_method":"pdf-text-layer"},"checksum":"d76dcb3a393418c280b92c5a1a383134788d5e915b236e6f0b9bb26e8d5bd6c3"} -->

## Slide 8 - A2A — Khái niệm cốt lõi

AgentCard · Task · Message · Part · Artifact · Context

---

<!-- chiron-source-span: {"source_span_id":"dc1e9911-97fe-562d-8a6b-dc56fbbfa749","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Multi-Agent: Traditional vs A2A","extraction_method":"pdf-text-layer"},"checksum":"01a60a6bf62664842ed82ec57981d16a13d7cfeaca6ef5567bdc1019c87dbdb4"} -->

## Slide 9 - Multi-Agent: Traditional vs A2A

Từ in-process sang HTTP services độc lập

---

<!-- chiron-source-span: {"source_span_id":"13904862-9790-5910-a524-0798d8302c10","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"A2A Interaction & Task Lifecycle","extraction_method":"pdf-text-layer"},"checksum":"dbaa00e344e177b9bea8091fc1577dc96d181fa7594d84048259a030fee54806"} -->

## Slide 10 - A2A Interaction & Task Lifecycle

Discover → Authenticate → Delegate → Stream → Complete

---

<!-- chiron-source-span: {"source_span_id":"b87685d8-5588-5d46-9ddd-5eb46892d087","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"A2A vs MCP — So sánh có hệ thống","extraction_method":"pdf-text-layer"},"checksum":"77f4691e517619d135b9656464cd7f21b5c5fd51b0d8aa3bb09f2e9ae87538b5"} -->

## Slide 11 - A2A vs MCP — So sánh có hệ thống

Hai chuẩn không cạnh tranh — chúng giải quyết hai bài toán khác nhau MCP — Model Context Protocol A2A — Agent-to-Agent Protocol Tổ chức công bố Anthropic (2024) Google (2025) Mục đích Kết nối LLM với công cụ và dữ liệu Kết nối các agent với nhau Quan hệ Client – Server (bất đối xứng) Peer – Peer (đối xứng) Đơn vị giao tiếp Resource, Tool, Prompt Task, Message, Artifact Tự chủ (autonomy) Tool thụ động — chỉ thực thi khi được gọi Agent chủ động — tự lập kế hoạch, gọi agent khác State / Lifecycle Stateless — 1 lệnh = 1 response Stateful Task: submitted → working → completed Discovery Cấu hình tĩnh trong host (mcp.json) Động qua AgentCard ở /.well-known/agent.json Transport stdio · SSE · HTTP (JSON-RPC 2.0) HTTP + JSON-RPC + Server-Sent Events Streaming Có (qua SSE) Có — bắt buộc trong specification

- Quy tắc nhớ: MCP cho mọi thứ không phải agent · A2A cho mọi thứ là agent.
Kết hợp thực tế → một Customer Agent (A2A Server) bên trong dùng nhiều MCP server (filesystem · postgres · github), đồng thời uỷ thác qua A2A đến Law / Tax / Compliance Agent.

---

<!-- chiron-source-span: {"source_span_id":"fe3fbba9-1e02-50c6-b775-2512b67bdca2","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"A2A trong dự án Pháp lý","extraction_method":"pdf-text-layer"},"checksum":"18353a8be158e59f1257955b967cfc41d2736baa74f5f7937fce6f6007ea7618"} -->

## Slide 12 - A2A trong dự án Pháp lý

AgentCard · Task lifecycle · Message — áp dụng cụ thể

---

<!-- chiron-source-span: {"source_span_id":"43874785-7fef-5075-b473-2f52c635e11a","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Kiến trúc hệ thống Pháp lý","extraction_method":"pdf-text-layer"},"checksum":"3eaed8aa28ae1ed6f58fd212814d0b30441e279dbfab858ec7e15687a2a30dd9"} -->

## Slide 13 - Kiến trúc hệ thống Pháp lý

5 service · A2A + LangGraph · OpenRouter LLM

---

<!-- chiron-source-span: {"source_span_id":"e5667bc0-2885-5bb6-a709-bf69d02879b7","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Law Agent — LangGraph StateGraph","extraction_method":"pdf-text-layer"},"checksum":"13735b51faed27804671a84ec962cfb644683f9a6852f18dbc0434884879e5fb"} -->

## Slide 14 - Law Agent — LangGraph StateGraph

Parallel delegation · State merging · Depth guards

---

<!-- chiron-source-span: {"source_span_id":"5e678411-41a2-51c1-bba7-50440301dddf","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"End-to-End Request Flow","extraction_method":"pdf-text-layer"},"checksum":"bb8644c95fcdc629a2bc6982fc3e32cd0c9632658984a39d10c0742084d41abb"} -->

## Slide 15 - End-to-End Request Flow

Theo dấu một câu hỏi xuyên qua 5 service

---

<!-- chiron-source-span: {"source_span_id":"9951337a-14ad-5b6d-a922-170934a73b22","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Tổng kết & Bài tập thực hành","extraction_method":"pdf-text-layer"},"checksum":"671fd08dee975e2d201a955d18cd8f6736de447b833ed364949fd402e97099fa"} -->

## Slide 16 - Tổng kết & Bài tập thực hành

Những điểm cốt lõi cần ghi nhớ và bài tập về nhà 5 điểm cốt lõi (Take-aways)

1. LLM đơn lẻ → multi-agent là bước tiến tự nhiên khi domain phức tạp và cần song song hoá.

2. MCP chuẩn hoá cách LLM tiêu thụ công cụ và dữ liệu.

3. A2A chuẩn hoá cách các agent cộng tác như những peer độc lập.

4. Cả hai cùng tồn tại: A2A bên ngoài, MCP bên trong.

5. Observability bằng trace_id là bắt buộc với hệ phân tán. 📚 Bài tập cá nhân (về nhà)

- Đọc spec A2A tại github.com/google/A2A

- Đọc spec MCP tại modelcontextprotocol.io

- Vẽ lại sơ đồ AgentCard của Law Agent từ __main__.py

- Đối chiếu StateGraph trong law_agent/graph.py với SVG 05
🧪 Bài tập nhóm (project)

- Thêm một agent mới (vd. Finance Agent) — đăng ký với Registry

- Sửa Law Agent để uỷ thác sang Finance Agent khi câu hỏi về tài chính

- Bổ sung 1 MCP server (vd. filesystem) cho Tax Agent

- Báo cáo: vẽ sơ đồ + bảng so sánh hiệu năng có/không có parallel
Tài liệu tham khảo

- A2A spec: github.com/google/A2A • MCP spec: modelcontextprotocol.io • LangGraph: langchain-ai.github.io/langgraph
❓ Hỏi – Đáp ❓

---

<!-- chiron-source-span: {"source_span_id":"32048b3d-4520-5978-9ba4-e20f0e936323","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"THANK","extraction_method":"pdf-text-layer"},"checksum":"619d71229cb4ceceefd9b80870c40297ca39fb004ce34031cadcbddbe39fb310"} -->

## Slide 17 - THANK

YOU © VinUniversity | All rights reserved
