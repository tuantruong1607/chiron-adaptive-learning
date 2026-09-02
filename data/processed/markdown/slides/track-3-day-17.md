---
schema_version: 1
course_id: rag-intensive
document_id: "760f2400-7f41-5d32-a7d4-55c3c7ab6e53"
document_version_id: "129047d4-3bd8-5c01-be3f-0ce5fbff1bd2"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Memory Systems for Agents"
source_file: "track 3 - day 17.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 17.pdf"
source_sha256: "0c956555eb8a5677c6abb27eee2a03dedc4d78c151c84d3f3ceca92163f607ff"
parser_version: chiron-structured-markdown-v1
page_count: 30
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":30}"
language: vi
---

# Memory Systems for Agents

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"e3f8dfc3-0367-5ac7-aa69-0f7ec0d68f86","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Memory Systems for Agents","extraction_method":"pdf-text-layer"},"checksum":"e18ddbc1b738e9410ef3c593309f81ef50d4881d9a8758c037ff3d27dfa70ee1"} -->

## Slide 1 - Memory Systems for Agents

AICB-P2T3 · Ngày 17 · Chương 4 — Agent Nâng Cao Giảng viên VinUniversity · Phase 2 · Track 3 · T uần 4

---

<!-- chiron-source-span: {"source_span_id":"63d120e7-56ae-5842-9345-03d15ab49937","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"5956009bf2eea0862bece7682e7caa95ecc9d07b100324287c450cf7297f3741"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Tại sao agent của bạn quên mọi thứ sau mỗi conversation — và làm sao fix nó đúng cách?” Giữ câu hỏi này trong đầu suốt buổi học hôm nay

---

<!-- chiron-source-span: {"source_span_id":"1ed68be8-c350-592b-a035-6cca6bcd62b8","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội dung vận hành","extraction_method":"pdf-text-layer"},"checksum":"622f2c304fd3bbf30671f673fcb78cf1979ea8c58c8a0280b8f7161d8a5f82a0"} -->

## Slide 3 - Nội dung vận hành

1. Tại sao Agent “quên”?

2. Context Engineering Framework

3. Cognitive Memory Model — 4 loại Memory

4. Implementation Deep-Dive

5. Frameworks chuyên dụng & Privacy

6. Demo & Thực hành Giảng viên (VinUni) AICB · Ngày 17 T uần 4 1 / 19

---

<!-- chiron-source-span: {"source_span_id":"664eb68b-0abc-5191-bf42-add0dfdd9f26","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"T ại sao Agent “quên”?","extraction_method":"pdf-text-layer"},"checksum":"521886adc424073c162d04af0c07474ad902bd3e50527bfcf9b61d6672f809fd"} -->

## Slide 4 - T ại sao Agent “quên”?

01 Context window có giới hạn — và hầu hết agent không có bộ nhớ ngoài

---

<!-- chiron-source-span: {"source_span_id":"badd9a18-a9eb-5117-b69b-7fb5c31a17cc","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Agent hiện tại — Stateless by default","extraction_method":"pdf-text-layer"},"checksum":"a5516533417e84caf953d697cb9f5abe1ef8080bec28bb11759cdaddc078da89"} -->

## Slide 5 - Agent hiện tại — Stateless by default

Session 1 LLM context Session 2 LLM context mới không truyền Mỗi session bắt đầu từ zero

- LLM không có persistent state
— mỗi API call là một request độc lập

- User nói “tôi thích Python” ở
session 1 → session 2 agent không nhớ

- Conversation dài >50 turns →
hit context limit Lưu ý: Đây là vấn đề #1 khi de- ploy agent thực tế: user kỳ vọng agent “nhớ” — nhưng nó không. Giảng viên (VinUni) AICB · Ngày 17 T uần 4 2 / 19

---

<!-- chiron-source-span: {"source_span_id":"5c218c1c-58b0-54ca-b80d-576c57a26a93","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Analogy: Bộ nhớ Agent giống não người","extraction_method":"pdf-text-layer"},"checksum":"6fac26ae55f4a3e61126a643aac6351776e6f1f8d037845fdcf187fbb29f998e"} -->

## Slide 6 - Analogy: Bộ nhớ Agent giống não người

Não người Working Memory Long-term Memory consolidation Agent Context Window External Store persist facts tương đương tương đương Context Window = RAM — Nhanh, tạm thời, giới hạn dung lượng ( ∼128K tokens) External Store = Ổ cứng — Chậm hơn, bền vững, gần như vô hạn (Redis, Vector DB) Agent cần cả hai: fast access cho conversa- tion hiện tại + persistent storage cho knowl- edge qua sessions Giảng viên (VinUni) AICB · Ngày 17 T uần 4 3 / 19

---

<!-- chiron-source-span: {"source_span_id":"6cf90464-0cda-5abf-b78c-ea9d08dc3978","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Context Engineering Frame","extraction_method":"pdf-text-layer"},"checksum":"6f0ec3caaa82f79ad312eb4a7a293be5a8dcedef75fda361e500b7d4594ec64b"} -->

## Slide 7 - Context Engineering Frame

02 Context Engineering Frame- work 7 layers of context — quản lý những gì agent “thấy”

---

<!-- chiron-source-span: {"source_span_id":"e8ca1eb4-7ec1-52d5-b3f9-448fa629b31a","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"7 Context Layers — Kiến trúc thông tin cho Agent","extraction_method":"pdf-text-layer"},"checksum":"b5f9e87adeec06c209ff2259585a75b913a1cf50ea2b0b31fc922277e9002d5e"} -->

## Slide 8 - 7 Context Layers — Kiến trúc thông tin cho Agent

Policy Context — Guardrails, safety rules T ool Context — Function outputs, API responses Retrieval Context — RAG results, documents Memory Context — Recalled facts, episodes User Context — Preferences, history T ask Context — Objective, instructions System Context — Persona, constraints Priority khi trim Khi gần token limit: trim từ dưới lên. Policy context trim cuối cùng (safety không bao giờ bỏ). Lưu ý: Conflict resolution: user preference mâu thuẫn policy con- straint → policy luôn thắng. Cần explicit rules trong system design. Giảng viên (VinUni) AICB · Ngày 17 T uần 4 4 / 19

---

<!-- chiron-source-span: {"source_span_id":"a8b41ac7-4a1b-5857-9e1c-896207813f39","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"T oken Budget — Phân bổ context window","extraction_method":"pdf-text-layer"},"checksum":"ac259062f0dc50439679b35b491dfd9c64e37910429a3ed75af6e2b521fff312"} -->

## Slide 9 - T oken Budget — Phân bổ context window

10% Short-term memory 4% Long-term facts 3% Episodic memory 3% Semantic knowledge Phần còn lại dành cho system prompt, task instructions, tool outputs, và out- put generation. Vượt 20% → context bị nhiễu, accuracy giảm. Giảng viên (VinUni) AICB · Ngày 17 T uần 4 5 / 19

---

<!-- chiron-source-span: {"source_span_id":"dc8f73cc-5ca2-51b5-ad71-df33426339d3","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"Cognitive Memory Model — 4","extraction_method":"pdf-text-layer"},"checksum":"661c582118ff306204ab478ea5d2936054f702261e4fc94ca1fc652e12f8c637"} -->

## Slide 10 - Cognitive Memory Model — 4

03 loại Memory Short-term, Long-term, Episodic, Semantic

---

<!-- chiron-source-span: {"source_span_id":"1de5866e-8afc-5225-9c4d-f5df340bb057","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"4 loại Memory — Cognitive Model cho AI Agents","extraction_method":"pdf-text-layer"},"checksum":"f285b2b71f63335f5bf1337a8dceb48ae1ddb492cd252ceca3c770a9a49f964c"} -->

## Slide 11 - 4 loại Memory — Cognitive Model cho AI Agents

Short-term (Working) Context window buffer Nhanh, tạm thời, ∼128K tokens Long-term (Declarative) Redis, PostgreSQL User prefs, facts qua sessions Episodic Log trải nghiệm có thứ tự “Lần trước tôi đã làm gì?” Semantic Embeddings + Vector DB Domain knowledge retrieval Tạm thời Bền vững Cá nhân Tri thức Working memory ↔ Short-term | Declarative memory ↔ Long-term | Episodic & Semantic tương tự tên gọi Giảng viên (VinUni) AICB · Ngày 17 T uần 4 6 / 19

---

<!-- chiron-source-span: {"source_span_id":"b04da091-149c-5384-95c1-adcb5488605a","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Short-term Memory — Context Window Management","extraction_method":"pdf-text-layer"},"checksum":"313ef8e4fd3ece1b958860c676b32c57fd8608256fc5b80b88aadc97dd1bea29"} -->

## Slide 12 - Short-term Memory — Context Window Management

Buffer M1 M2 M3 M4 M5 limit! Summary Summary M4 M5 Sliding System Sum. M4 M5 Best!

### 3 strategies chính

1. Buffer: giữ tất cả — đơn giản nhưng hit limit sau ∼50 turns

2. Summary: LLM tóm tắt history cũ — ổn định nhưng tốn thêm LLM calls

3. Sliding window: system + summary + last K turns — best tradeoff cho production Short-term memory nên chiếm tối đa 10% context window. Trim khi vượt — keep recent N tokens, discard oldest. Giảng viên (VinUni) AICB · Ngày 17 T uần 4 7 / 19

---

<!-- chiron-source-span: {"source_span_id":"a869dab4-16fe-5b16-88c9-718dd3036a41","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"Long-term Memory với Redis — Persistent Cross-Session","extraction_method":"pdf-text-layer"},"checksum":"51bbec3529258262d7a8e40580d439c3b73305a417e3d85a878494be1b5769ba"} -->

## Slide 13 - Long-term Memory với Redis — Persistent Cross-Session

Conversation LLM Extract Redis Next Session kết thúc key facts load profile TTL: prefs 90d, facts 30d, sessions 7d

### Ý tưởng

- Sau mỗi conversation, LLM
extract key facts rồi store vào Redis với TTL

- Session mới: load user profile vào
system prompt trước khi user nói Hash: preferences (language, style) Set: facts (“biết Python, học ML”) List: session history (recent) Tất cả O(1) reads — production- ready Giảng viên (VinUni) AICB · Ngày 17 T uần 4 8 / 19

---

<!-- chiron-source-span: {"source_span_id":"256fd8e4-9824-5256-a2bb-4ac3c17ca2f8","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"Memory Management Flow — Buffer → Summarize → Store","extraction_method":"pdf-text-layer"},"checksum":"907579deeb8d7cb8fdfc13186ea0e15bed3f8b7edde9a10a2bf921e9bb9728cd"} -->

## Slide 14 - Memory Management Flow — Buffer → Summarize → Store

1. Buffer (Context Window)

2. Summarize (LLM call)

3. Extract (Key facts)

4. Persist (External store) Redis long-term facts Chroma semantic embeddings Trigger: token count > threshold Chỉ persist sau task completion — không write giữa chừng để tránh inconsistent state Lưu ý: Conflict resolution: long- term fact mâu thuẫn short-term info → recency wins, flag for re- view. Giảng viên (VinUni) AICB · Ngày 17 T uần 4 9 / 19

---

<!-- chiron-source-span: {"source_span_id":"167a46da-8d38-5bed-ab9e-a081c2602146","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Implementation Deep-Dive","extraction_method":"pdf-text-layer"},"checksum":"2b2fe84c24dfb62506774250e0e19d8b5cf723c2c746a18031defe945cec5617"} -->

## Slide 15 - Implementation Deep-Dive

04 Code-level: LangGraph nodes cho mỗi memory type

---

<!-- chiron-source-span: {"source_span_id":"787b3a18-8b25-5f3d-9214-96d25669425e","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"LangGraph Memory State — Code-Level","extraction_method":"pdf-text-layer"},"checksum":"04b4d7e8ea0b675a59350e0d6dc98a803837dcef3ef54bf023a138ad5ed79882"} -->

## Slide 16 - LangGraph Memory State — Code-Level

```text
class MemoryState(TypedDict):
```
messages: list[BaseMessage] user_profile: dict # long-term episodes: list[dict] # episodic semantic_hits: list[str] # semantic memory_budget: int # tokens left # Memory router: ọchn ạloi phù ợhp

```text
def retrieve_memory(state):
query = state[ "messages"][-1].content
return {
"user_profile": redis.hgetall(uid),
"episodes": find_similar(query, k=3),
"semantic_hits": chroma.query(query),
}
```

### Integration pattern

1. Node load_memory: đọc 3 loại memory khi bắt đầu

2. Inject vào system prompt theo priority

3. Node save_memory: ghi khi kết thúc

1. Short-term (gần nhất)

2. Long-term facts (user prefs)

3. Relevant episodes

4. Semantic knowledge Giảng viên (VinUni) AICB · Ngày 17 T uần 4 10 / 19

---

<!-- chiron-source-span: {"source_span_id":"ada4ee10-2a74-59f2-90ce-16eb2e10db9e","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Episodic Memory — Learning từ Past Trajectories","extraction_method":"pdf-text-layer"},"checksum":"a252e3e0faa4f2ff29489c79ca26aeb1dd9fa0bf89fdb90319f5c17da50d45f4"} -->

## Slide 17 - Episodic Memory — Learning từ Past Trajectories

Task: debug API Trajectory: tried X, Y Outcome: Y worked Reflection: X fails vì... New similar task similarity search

### Lưu tuple mỗi episode

- (task, trajectory, outcome,
reflection)

- Agent biết: “approach X đã fail
vì Y trong task tương tự” LRU: xóa episode ít dùng nhất Importance decay: score giảm theo thời gian Consolidation: merge episodes tương tự Voyager-style: extract reusable strategy → skill li- brary Giảng viên (VinUni) AICB · Ngày 17 T uần 4 11 / 19

---

<!-- chiron-source-span: {"source_span_id":"769fd77f-eec2-519b-99c0-f84e60f4b61a","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Semantic Memory — Vector DB cho Knowledge Retrieval","extraction_method":"pdf-text-layer"},"checksum":"5f5e5a45d470b59d563323f9ea38862dbec787f2f6c55d2f2ba209712bc08eb6"} -->

## Slide 18 - Semantic Memory — Vector DB cho Knowledge Retrieval

Domain Docs Embed Chroma DB Agent Query T op-K vectors cosine sim

- Encode domain knowledge →
embeddings → Chroma/Pinecone

- Query = task description → cosine
similarity → top-k chunks

- Agent discover facts mới → add
vào DB với metadata (source, confidence, timestamp) Agent tự mở rộng knowledge base qua interactions — incremental knowledge growth Giảng viên (VinUni) AICB · Ngày 17 T uần 4 12 / 19

---

<!-- chiron-source-span: {"source_span_id":"8754ed76-5e7a-5657-968a-8789a2b1d0aa","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Memory Architecture — Combining All 4 Types","extraction_method":"pdf-text-layer"},"checksum":"166e9da4016e705ba3ce481f5a3ad965c4fc1abb133ac2cbdb4985bcb692e83d"} -->

## Slide 19 - Memory Architecture — Combining All 4 Types

Agent retrieve(query) Short-term Long-term Episodic Semantic priority 1 priority 2 priority 3 priority 4 Merged context → LLM Lưu ý: Unified interface: retrieve(query, types=["all"]) trả về merged con- text từ cả 4 loại memory, đã trim theo token budget. Giảng viên (VinUni) AICB · Ngày 17 T uần 4 13 / 19

---

<!-- chiron-source-span: {"source_span_id":"20d76280-fcd0-5bd6-8c91-a3f27fa43198","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Frameworks chuyên dụng &","extraction_method":"pdf-text-layer"},"checksum":"c7aa0e050c0e1ecc7a6c56791a5a6bfe6b29e6be357203b9b93be5f19f29a58e"} -->

## Slide 20 - Frameworks chuyên dụng &

05 Privacy Mem0, Zep — và khi nào dùng framework có sẵn

---

<!-- chiron-source-span: {"source_span_id":"1787c9dc-d14d-503d-b109-cac1521e1fad","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Mem0 & Zep — Managed Memory Layers","extraction_method":"pdf-text-layer"},"checksum":"920da3f8263ae0a2c02d0fa3a8f7fd6d887b9baed041c2bcd9b3ee7e82f1d869"} -->

## Slide 21 - Mem0 & Zep — Managed Memory Layers

- Auto-classify memory types

- Smart retrieval: relevance +
recency ranking

- Claim: 90% token reduction,
91% faster retrieval

- API-first, nhanh
go-to-market

- Entity extraction +
progressive summarization

- T ự build user knowledge
graph qua sessions

- Multi-level summaries: turn →
session → cross-session

- Giảm context size tối ưu
Tiêu chí Mem0 / Zep Custom (Redis + Chroma)

```text
Setup time Nhanh (API) Chậm (build from scratch)
```
Control Hạn chế Full control Khi nào dùng MVP, go-to-market Production, đặc thù domain Giảng viên (VinUni) AICB · Ngày 17 T uần 4 14 / 19

---

<!-- chiron-source-span: {"source_span_id":"c9c46b43-52ba-51c9-922f-56ab169cafd5","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Quyền riêng tư, Bảo mật & GDPR","extraction_method":"pdf-text-layer"},"checksum":"ab5c55079f462d16cd3ce20764b1856c0c3f95f82a8435d1e9355fd4af6503ff"} -->

## Slide 22 - Quyền riêng tư, Bảo mật & GDPR

Privacy-by-Design — Mặc định không lưu PII. User phải explicit opt-in trước khi agent ghi nhớ thông tin cá nhân. Right to be Forgotten — User yêu cầu xóa → xóa tất cả memory en- tries liên quan → confirm deletion.

### Lưu ý: Federated Forgetting
trong multi-agent system, dele- tion request phải propagate đến tất cả agents có copy.

- ✓ Data minimization

- ✓ Purpose limitation

- ✓ Storage limitation (TTL)

- ✓ Consent management

- ✓ Deletion verification
Giảng viên (VinUni) AICB · Ngày 17 T uần 4 15 / 19

---

<!-- chiron-source-span: {"source_span_id":"b8dbb1ef-e6c1-51cb-a3ad-455964c8cf6d","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Demo & Thực hành","extraction_method":"pdf-text-layer"},"checksum":"7c5939d1ff2814cca15be9250adc64f98e17f67fd6ffeca1ae6917deff014576"} -->

## Slide 23 - Demo & Thực hành

06 Xem agent nhớ user preferences qua 3 sessions

---

<!-- chiron-source-span: {"source_span_id":"d0c7b46e-e2a6-5b91-a167-d61dccbbb1bd","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Agent nhớ User Preferences qua 3 Sessions","extraction_method":"pdf-text-layer"},"checksum":"bf0bdcf176b09d19a4e3c360c61619dc992e6e8c80ac4889f771872443093dd9"} -->

## Slide 24 - Agent nhớ User Preferences qua 3 Sessions

1. Session 1: User nói “tôi thích Python, không thích Java” → agent ghi vào Redis

2. Session 2 (new process): Agent load memory → proactively suggest Python solution mà không cần hỏi lại

3. Session 3: Agent recall episode “user bị confused async/await” → tự thêm explanation

4. So sánh: agent có memory vs không memory — response relevance, user satisfaction Giảng viên (VinUni) AICB · Ngày 17 T uần 4 16 / 19

---

<!-- chiron-source-span: {"source_span_id":"2bab9a97-834f-5cbf-ad9d-393ced5b105e","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"Lab #17","extraction_method":"pdf-text-layer"},"checksum":"d6c75a08a5a6c89b28fa004c7c96f4a7501d63fed947a84615921e1e9d08d13d"} -->

## Slide 25 - Lab #17

Mục tiêu: Build Multi-Memory Agent với LangGraph Deliverable: Agent với full memory stack + benchmark report: so sánh agent có/không memory trên 10 multi-turn conversations Thời gian: 2 giờ Giảng viên (VinUni) AICB · Ngày 17 T uần 4 17 / 19

---

<!-- chiron-source-span: {"source_span_id":"7a35f0bd-48ee-5c4c-887b-50665842b28b","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Lab 17 — Các bước thực hành","extraction_method":"pdf-text-layer"},"checksum":"4d214aa2eeac268490fd73b88633212a2c097d6ea548b566c65583e11717d431"} -->

## Slide 26 - Lab 17 — Các bước thực hành

1. Implement 4 memory backends: ConversationBufferMemory (short-term), Redis (long-term), JSON episodic log, Chroma (semantic)

2. Build memory router: chọn memory type phù hợp dựa trên query intent — user preference vs factual recall vs experience recall

3. Context window management: auto-trim khi gần limit, priority-based eviction theo 4-level hierarchy

4. Benchmark: so sánh agent có/không memory trên 10 multi-turn conversations — đo response relevance, context utilization, token efficiency GitHub repo + benchmark report: bảng so sánh metrics, memory hit rate anal- ysis, token budget breakdown Giảng viên (VinUni) AICB · Ngày 17 T uần 4 18 / 19

---

<!-- chiron-source-span: {"source_span_id":"cb48d952-a393-5635-8507-803070b7abee","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"T ổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"8f89d9d8d6dd375a3ea4e2619fcb600dffb7787d300f958db2ca0a37d20849d5"} -->

## Slide 27 - T ổng kết — Key T akeaways

Những ý chính cần nhớ sau buổi học hôm nay 1 Không có “one size fits all” — production agent cần ít nhất short-term + long-term, thêm episodic/semantic tùy use case 2 Memory retrieval quality quyết định agent quality — bad retrieval = irrelevant context = wrong answer 3 Memory write-back cần careful design: nhớ gì, khi nào ghi, xử lý conflict ra sao, TTL bao lâu 4 Privacy không phải afterthought — GDPR compliance cần thiết kế từ đầu (Privacy- by-Design) Giảng viên (VinUni) AICB · Ngày 17 T uần 4 18 / 19

---

<!-- chiron-source-span: {"source_span_id":"d0cbf205-2070-503e-b75a-5a44db28738e","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Tiếp theo & Bài tập","extraction_method":"pdf-text-layer"},"checksum":"8adb6bee30c5e1b65a3303edca837e1e54c93a7acca60051d658cfa3295593fc"} -->

## Slide 28 - Tiếp theo & Bài tập

Ngày 18: Production RAG “Agent đã có memory, tiếp theo cần knowledge retrieval tốt hơn — tại sao RAG pipeline demo chạy tốt nhưng production chỉ đạt 60%?”

- Hoàn thành Lab 17:
Multi-Memory Agent + benchmark

- Đọc: Anthropic “Building
Effective Agents” (mục Context Engineering) Giảng viên (VinUni) AICB · Ngày 17 T uần 4 19 / 19

---

<!-- chiron-source-span: {"source_span_id":"1f7011c6-39ab-549a-b81b-939bb218d81a","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer"},"checksum":"195b156b2f38dfa51b2a01a3dbafcf1da594069ffb318988e1f3dcb86e5109f4"} -->

## Slide 29 - Hỏi & Đáp

Memory nào là “must-have” cho production agent? Khi nào thì dùng framework (Mem0, Zep) vs tự build?

---

<!-- chiron-source-span: {"source_span_id":"c9a88b6d-3703-59f8-8475-af5dcf7ab4b6","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Cảm ơn!","extraction_method":"pdf-text-layer"},"checksum":"8d9a77903f64f827f4dad2fdfdc863e301cbf422f093067ab053a3b7d92817da"} -->

## Slide 30 - Cảm ơn!

AICB-P2T3 · Ngày 17 · Memory Systems for Agents github.com/vinuni-aicb Liên hệ: instructor@vinuni.edu.vn
