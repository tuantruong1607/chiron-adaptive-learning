---
schema_version: 1
course_id: rag-intensive
document_id: "acc7eba9-c60d-5779-b7c0-599e39174cc2"
document_version_id: "47e791b1-5891-5e46-85b0-11697c434d24"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "LangGraph & Agentic Orchestration"
source_file: "track 3 - day 23.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3 - day 23.pdf"
source_sha256: "098a68cfc9f5148df9aafd8a7b28c7e76bfd394a233419abf8ea79abbaa61e65"
parser_version: chiron-structured-markdown-v1
page_count: 36
sparse_page_count: 1
extraction_methods: "{\"pdf-text-layer\":35,\"pdf-text-layer-sparse\":1}"
language: vi
---

# LangGraph & Agentic Orchestration

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"3e658c77-18f5-5e15-a1c0-d27225b98d35","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"LangGraph & Agentic Orchestration","extraction_method":"pdf-text-layer"},"checksum":"8767ed74b9a7dda1361e86c3684fea291f77e2da5e46e68d58eb88150abf1d30"} -->

## Slide 1 - LangGraph & Agentic Orchestration

Day 08 · State Machines cho Agents · 2h theory + 2h guided lab Instructor VinUniversity · Phase2·Track3·Week5

---

<!-- chiron-source-span: {"source_span_id":"84b03715-c538-5287-84ff-ebf76e66f13b","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃ Y SUY NGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"77e61cd11200646d94d852ffc5c7054bbbe304bcbe22a9f7cf9e09609384c21b"} -->

## Slide 2 - HÃ Y SUY NGHĨ...

? “Khi agent cần loop, retry, human approval và resume sau crash, chain một chiều còn đủ không?” Giữcâuhỏinàytrongđầukhihọcbàihômnay

---

<!-- chiron-source-span: {"source_span_id":"3782244f-8816-5e0c-b7ad-a672f0aa2560","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nội dung bài học","extraction_method":"pdf-text-layer"},"checksum":"474a8b925c47b3ebc63daf047055a50a6573bde35c492a50c3fc75f9870e54c1"} -->

## Slide 3 - Nội dung bài học

1. Mụctiêu&lịchhọc

2. Khinàochainkhôngđủ?

3. CoreAPI

4. Persistence&TimeTravel

5. Human-in-the-Loop&ErrorRecovery

6. Lab4giờ

7. Takeaways Instructor (VinUni) AICB·Day08 Week5 1/25

---

<!-- chiron-source-span: {"source_span_id":"e3fbdef5-8148-5bd6-b4ac-badc79402d4d","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"Mục tiêu & lịch học","extraction_method":"pdf-text-layer"},"checksum":"7d6022d6cbb61bdc92d8b73f3a5c6baa034c5153d755518c325f3da37a9c97cd"} -->

## Slide 4 - Mục tiêu & lịch học

01 2giờlýthuyếtcôđọng,2giờlabcóhướngdẫn;bàilab thiếtkếđủ4giờđểphânloạinănglực.

---

<!-- chiron-source-span: {"source_span_id":"79a6cd51-7987-5108-ab9d-3165c0989ef2","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Sau buổi học, học viên làm được gì?","extraction_method":"pdf-text-layer"},"checksum":"77cbbdfbc953ee4b82c5e7ffd7e5806e34e8816768ca88faf9090c60285c5797"} -->

## Slide 5 - Sau buổi học, học viên làm được gì?

Conceptual outcomes

- PhânbiệtLCELchain,agentloop
vàstatefulgraph.

- Thiếtkếstate,node,edge,
reducertrongLangGraph.

- Hiểucheckpointing,timetravel,
HITLvàerrorrecovery. Practical outcomes

- Xâydựngworkflowcóconditional
routing,retryvàinterrupt.

- Ghitrace/metricphụcvụchấm
điểm.

- Viếtreportkỹthuậtngắntheo
rubricproduction. Checkpoint: Cuối buổi: mỗi nhóm demo một graph chạy được trên test casecơbản;họcviêngiỏihoànthiệnthêmcrashrecoveryvàreport. Instructor (VinUni) AICB·Day08 Week5 2/25

---

<!-- chiron-source-span: {"source_span_id":"04349397-45c4-5fd5-8d01-70cb262f0d12","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Timeline 4 giờ","extraction_method":"pdf-text-layer"},"checksum":"b28e90dabbbdac68e70e280cea0fda7e7dfaf10cb6874af3ec0543429de49f40"} -->

## Slide 6 - Timeline 4 giờ

00:00 01:00 02:00 03:00 04:00 Lý thuyết + tương tác Lab 4h: core + extension 2h lý thuyết

- 20’LCELgap+statemachine

- 30’StateGraphAPI

- 25’persistence+checkpointing

- 25’HITL+errorrecovery

- 20’metric/reportbriefing
2h trên lớp + 2h mở rộng

- 0-2h: buildrunnablecoregraph

- 2-3h: persistence+crash-resume

- 3-4h: metrics,report,polish
Instructor (VinUni) AICB·Day08 Week5 3/25

---

<!-- chiron-source-span: {"source_span_id":"24251326-702f-5c14-a3b6-f3d449c075fc","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Khi nào chain không đủ?","extraction_method":"pdf-text-layer"},"checksum":"6672cbaaa347c7656712d03ff94ef9b586eaf6d919bde6ef53fea3677fb4075f"} -->

## Slide 7 - Khi nào chain không đủ?

02 LCELphùhợppipelinemộtchiều;agentproduction thườngcầntrạngthái,nhánh,vònglặpvàkiểmsoátlỗi.

---

<!-- chiron-source-span: {"source_span_id":"31a25ff0-2d39-5266-8ff1-fe9db9531e72","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"LCEL Chain: con đường một chiều","extraction_method":"pdf-text-layer"},"checksum":"c23dcdbff20869864232d20b2a18320bc8a2c9897432cafe530c8931fe7ebc66"} -->

## Slide 8 - LCEL Chain: con đường một chiều

Retrieve LLM Output khó loop lại khó pause cho human khó resume sau crash

### Chain đủ khi

- taskđơngiản,single-shot;

- khôngcầnretrythôngminh;

- khôngcầnhumanapproval;

- khôngcầnlưustatedàihạn.
Workflowcủabạncócầnquyết định bước tiếp theo dựa trên kếtquảbướctrướckhông?Nếu có,hãynghĩtớigraph. Instructor (VinUni) AICB·Day08 Week5 4/25

---

<!-- chiron-source-span: {"source_span_id":"e76a92dc-9705-5bd6-8536-b9e8b975488d","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"Production gap: 5 vấn đề thường gặp","extraction_method":"pdf-text-layer"},"checksum":"d3323f370dd49fa5dceefef5be7319bef6073d3e82b18079b8af03a83125768c"} -->

## Slide 9 - Production gap: 5 vấn đề thường gặp

Retrylogic Loop+con- ditionaledge Humanapproval interrupt+resume Dynamicrouting conditionaledges Crashrecovery checkpointing Parallelwork fan-out+reducer LCEL gap LangGraph pattern Minipoll-4phút Trongsảnphẩmbạntừnglàm,vấnđềnàoxuấthiệnnhiềunhất: retry,rout- ing,humanapproval,crashrecoveryhayparallelwork? Instructor (VinUni) AICB·Day08 Week5 5/25

---

<!-- chiron-source-span: {"source_span_id":"8ec6f056-e743-56db-86d7-eb5ea7cf9d28","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"LangGraph trong một câu","extraction_method":"pdf-text-layer"},"checksum":"2794e64e15ae3fee138711a9e8ed8c7ad8f27239f4974cf1138fdc4fcf5c01d7"} -->

## Slide 10 - LangGraph trong một câu

LangGraph — Framework orchestration theo graph:typed state + node functions + edges/conditional edges + checkpointingđểxây workflowagentcóloop,interrupt,persistencevàfaulttolerance. Khi dùng

- agentcầnnhiềubướcvàquyết
địnhđộng;

- cầnhuman-in-the-loop;

- cầnkhôiphụcsaulỗi;

- cầntrace/debug.
Khi chưa cần

- promptđơnlẻ;

- ETLtuyếntính;

- khôngcóstate;

- khôngcầnapprovalhoặcaudit.
docs.langchain.com/oss/python/langgraph/overview Instructor (VinUni) AICB·Day08 Week5 6/25

---

<!-- chiron-source-span: {"source_span_id":"eaf7cb60-e1dc-53e6-868e-1337bc702bb3","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"Ví dụ thực tế: support ticket triage","extraction_method":"pdf-text-layer"},"checksum":"eb014326b9fecedb2c8fd3ee1f143f2af68eb3644ee2d745d67ae7521fc333fa"} -->

## Slide 11 - Ví dụ thực tế: support ticket triage

Flow

1. Nhậnticket.

2. Classify: billing,bug,policy,urgent.

3. Nếuthiếuthôngtin: hỏilạikhách.

4. Nếurủirocao: dừngđểhuman approve.

5. Nếutoollỗi: retryhoặcdead-letter. Routing, loop hỏi lại, HITL và retryđềuphụthuộcstatehiện tại. Một chain tuyến tính sẽ nhanhtrởnênkhómaintain. Think-pair-share-5phút Viết 1 state field cần có cho ticketworkflowvàlýdo. Instructor (VinUni) AICB·Day08 Week5 7/25

---

<!-- chiron-source-span: {"source_span_id":"5c5db4d4-9508-55de-996f-f2230728f1ed","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Core API","extraction_method":"pdf-text-layer"},"checksum":"facc7aa7a3d02495f449d732aeefc3d47e3db5c0451c982a487bd6ff9852da5f"} -->

## Slide 12 - Core API

03 State,node,edge,reducerlàbốnkháiniệmnềntảngcủa StateGraph.

---

<!-- chiron-source-span: {"source_span_id":"a92a1022-3916-51f6-aa85-43bf2f266307","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"State Machine: khái niệm cốt lõi","extraction_method":"pdf-text-layer"},"checksum":"6d67fa5adfd928b949971fe0334ab32e136220c76d56d11a0700ebca2aff7ebb"} -->

## Slide 13 - State Machine: khái niệm cốt lõi

START plan execute done? END yes no: retry State: {messages,plan,tool_results, attempt,status,pending_approval} Pythonfunctionđọcstatevàtrảvề partialupdate. Đường chuyển bước; có thể cố địnhhoặcconditional. Instructor (VinUni) AICB·Day08 Week5 8/25

---

<!-- chiron-source-span: {"source_span_id":"4537077e-e77e-5715-9c36-568de6cf1bdb","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"State design: code-level","extraction_method":"pdf-text-layer"},"checksum":"2a73bcd7827d05fc50579aeefbdbcd0fa53a4c6fe95fcfce24e2495469f91393"} -->

## Slide 14 - State design: code-level

```text
from typing import Annotated, TypedDict
from operator import add
class AgentState(TypedDict):
```
messages: Annotated[ list[str], add] query: str route: str attempt: int tool_results: Annotated[ list[str], add] final_answer: str | None errors: Annotated[ list[str], add] 5 quy tắc thiết kế state

1. Flat,ítnesteddict.

2. Reducerrõcholist.

3. Typedvàvalidateđược.

4. Lean: khônglưubloblớn.

5. Versionedkhischemathay đổi. Lưu ý: Default reducer là overwrite. Nếu2nodecùng ghi một field list mà không khaibáoreducer,rấtdễmất dữliệu. Instructor (VinUni) AICB·Day08 Week5 9/25

---

<!-- chiron-source-span: {"source_span_id":"cc6c6a34-e80f-5d9d-b3e4-b58850769c89","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"Reducer: luật merge state","extraction_method":"pdf-text-layer"},"checksum":"6a06610187aed2e8336dddce720afc8117d9bb000dc1dcb6cbf4cb5b4495def6"} -->

## Slide 15 - Reducer: luật merge state

Overwrite phù hợp cho

- statushiệntại;

- routehiệntại;

- finalanswer;

- counternếuchỉmộtnodeghi.
Append phù hợp cho

- messages;

- toolresults;

- errors;

- auditevents;

- metricrecords.
Quickcheck-3phút Field audit_lognênoverwritehayappend? Vìsao? Instructor (VinUni) AICB·Day08 Week5 10/25

---

<!-- chiron-source-span: {"source_span_id":"fd949c44-9c8c-56c2-8a41-5ab3c327e6ac","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"Node function: nguyên tắc production","extraction_method":"pdf-text-layer"},"checksum":"814765430a15bb611aa9b46cd843c5cec4e61964615521215c55c5be2142b475"} -->

## Slide 16 - Node function: nguyên tắc production

```text
def classify_node(state: AgentState) -> dict:
# TODO(student): implement routing policy
route = classify_query(state[ "query"])
return {
```
"route": route, "messages": [f "classified:{route}"], }

```text
def tool_node(state: AgentState) -> dict:
```
# Nodes should be small and testable result = run_tool(state[ "query"])

```text
return {"tool_results": [result]}
```
Checklist

- Pure-ish: khôngsideeffect
nếutránhđược.

- Idempotentchoretry.

- Returnpartialupdate,
khôngmutatetoànstate.

- Logđủchoaudit.

- Timeoutvàerrortyped.
Instructor (VinUni) AICB·Day08 Week5 11/25

---

<!-- chiron-source-span: {"source_span_id":"6ba6ed64-d4aa-5c05-8848-3d28194be9a3","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"Conditional edges: dynamic routing","extraction_method":"pdf-text-layer"},"checksum":"2d4dcfe23946286de57b139a34772700dff751115628d30be9d3715e7bfbdefd"} -->

## Slide 17 - Conditional edges: dynamic routing

classify route simple_qa rag_search full_agent output easy medium hard Nhậnstate,trảvềtênnhánh tiếp theo. Dùng để tối ưu cost,latencyvàrisk.

- Easyquery: cheappath.

- Missinginfo: askuser.

- Riskyaction: approval.

- Repeatederror:
fallback/dead-letter. Instructor (VinUni) AICB·Day08 Week5 12/25

---

<!-- chiron-source-span: {"source_span_id":"191b0a88-510e-5b2d-b06e-3fbcedf8de1d","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"Graph wiring: từ node sang runnable graph","extraction_method":"pdf-text-layer"},"checksum":"5e041a1be8b58faa46d04e1e4a903e3334ce556e1cf233acf8f519fa17421461"} -->

## Slide 18 - Graph wiring: từ node sang runnable graph

```text
from langgraph.graph import StateGraph, START, END
graph = StateGraph(AgentState)
graph.add_node("classify", classify_node)
graph.add_node("answer", answer_node)
graph.add_node("tool", tool_node)
graph.add_edge(START, "classify")
graph.add_conditional_edges(
```
"classify", route_next, {"simple": "answer", "tool": "tool"}, ) graph.add_edge("answer", END) compiled = graph. compile(checkpointer=saver) Build order

1. Definestateschema.

2. Implementnodes.

3. Implementroute functions.

4. Addedges.

5. Compilewith checkpointer.

6. Invokewiththreadid. Instructor (VinUni) AICB·Day08 Week5 13/25

---

<!-- chiron-source-span: {"source_span_id":"2d835646-5c18-5ee1-a180-4db4cd8b8ce7","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"Persistence & Time T ravel","extraction_method":"pdf-text-layer"},"checksum":"7aec81a0a197ef5d78bdb281ba6f25832577d31b930992c40d4e14654af68da2"} -->

## Slide 19 - Persistence & Time T ravel

04 Checkpointingbiếngraphthànhworkflowcóthểpause, resume,replayvàdebug.

---

<!-- chiron-source-span: {"source_span_id":"3af36b02-6c86-5830-912e-7294e8ba865e","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"Checkpointing: state snapshot mỗi bước","extraction_method":"pdf-text-layer"},"checksum":"d6027878b772704c9e6a429173ed55cf30c3b92969d9580ae6391860ea5d7466"} -->

## Slide 20 - Checkpointing: state snapshot mỗi bước

plan C1 execute C2 CRASH resume output loadcheckpoint

### Memory saver
nhanh, không bền saurestart. SQLite saver: persis- tent,dễdemo. Postgres saver: phù hợp service nhiều thread. Lưu ý: Largestate=checkpointlớn=chậm. Lưureferencesthayvìfull document/blob. Instructor (VinUni) AICB·Day08 Week5 14/25

---

<!-- chiron-source-span: {"source_span_id":"f7dee79a-b166-546c-8e81-e29e308e6cb9","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"Thread, checkpoint, time travel","extraction_method":"pdf-text-layer"},"checksum":"7b8071f9f75db8c217c15131bf5fe1a22afac5ab75d5cbdddb7a04c7616757f7"} -->

## Slide 21 - Thread, checkpoint, time travel

- Thread: mộtphiênworkflow,vídụmộtuserrequesthoặcmộtticket.

- Checkpoint: snapshotstatesaumỗisuper-stepkhigraphcó
checkpointer.

- Replay: chạylạitừmộtcheckpointđểdebughoặcA/Btestroutekhác.

- Update state: chỉnhstatetạicheckpointtrướckhiresume,hữuíchcho
HITL. Khikháchbáo“agentgửisaiemail”,bạncầnstatehistoryđểbiếtnodenào quyếtđịnhsai,inputlúcđólàgì,humanđãapprovehaychưa. docs.langchain.com/oss/python/langgraph/persistence Instructor (VinUni) AICB·Day08 Week5 15/25

---

<!-- chiron-source-span: {"source_span_id":"594242dd-9979-57cd-afa5-18a4e48ee6df","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"Invoke với thread id","extraction_method":"pdf-text-layer"},"checksum":"076878be1fe912ccca4e3ad2a0b72f6c9bd4444c28acf0339f06c9f0efb8e913"} -->

## Slide 22 - Invoke với thread id

config = { "configurable": { "thread_id": "ticket-123"}} result = compiled.invoke( {"query": "Refund request for order 42"}, config=config, ) snapshot = compiled.get_state(config) history = list(compiled.get_state_history(config)) Lab metric liên quan

- Cóthreadidriêngcho
mỗirun.

- Cóstatehistorysaurun.

- Cótraceeventsđủđể
tínhnodecount,retry count,approvalcount. Instructor (VinUni) AICB·Day08 Week5 16/25

---

<!-- chiron-source-span: {"source_span_id":"2c2087c7-4747-52cb-abe7-48798e5a54d3","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"Human-in-the-Loop & Error","extraction_method":"pdf-text-layer"},"checksum":"6202a0bb15ba5723d014387b6039d6c0d9b3e026f066463181b81c1661f25faa"} -->

## Slide 23 - Human-in-the-Loop & Error

05 Recovery Agentproductionphảibiếtkhinàotựlàm,khinàohỏi người,khinàodừngantoàn.

---

<!-- chiron-source-span: {"source_span_id":"d3fa437c-dca1-5e02-9b9e-f7b1dfb59413","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Human-in-the-loop: interrupt và resume","extraction_method":"pdf-text-layer"},"checksum":"b6fef92df2065d821e3637bdbbfe1c24bbbe4eb27a7c2384c34518b9efdac858"} -->

## Slide 24 - Human-in-the-loop: interrupt và resume

draft INTERRUPT send/action END approve edit/reject Approvaltrướcdestructiveaction; clarification khi thiếu thông tin; escalationkhivượtquyền;review trướcpublish. Graphpause,lưustate;humantrả lời;graphresumetừđúngvịtrívới statemới. Role-play-6phút Một bạn đóng agent, một bạn đóng reviewer. Reviewer chỉ được approve khistatecóđủevidence. Instructor (VinUni) AICB·Day08 Week5 17/25

---

<!-- chiron-source-span: {"source_span_id":"92bfaa25-2f54-5f0d-8615-556b66b50baa","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"HITL code skeleton","extraction_method":"pdf-text-layer"},"checksum":"34eccb329f7dd97c1b1e9727da105c91798628b18e19d2e2c2ad4dffd68e6113"} -->

## Slide 25 - HITL code skeleton

```text
from langgraph.types import interrupt, Command
def approval_node(state: AgentState) -> dict:
decision = interrupt({
```
"action": state[ "proposed_action"], "risk": state[ "risk_level"], "evidence": state[ "tool_results"], })

```text
return {"approval": decision}
```

### # Resume later
compiled.invoke(Command(resume={ "approved": True}), config) Chấm điểm lab

- Cóinterruptobjectrõ
ràng.

- Córoute
approve/reject/edit.

- Reportghisốlần
approvalvàkếtquả.

- Khôngexecute
destructiveactionkhi chưaapprove. Instructor (VinUni) AICB·Day08 Week5 18/25

---

<!-- chiron-source-span: {"source_span_id":"a98ec66f-8457-527e-9d22-57e8c1c20ada","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Error recovery: retry, fallback, dead-letter","extraction_method":"pdf-text-layer"},"checksum":"2ed3ad74f9cfd539814d3c56b53ace10b69930f9faf8d329515803c7fa7875f3"} -->

## Slide 26 - Error recovery: retry, fallback, dead-letter

llm/toolcall error? next fallback dead-letter no retry maxretry fail 3 tầng

1. Retryvớibackoffvàmax attempts.

2. Fallbackmodel/tool.

3. Dead-letterđểmanualreview. Lưu ý: Node retry phải idem- potent. Gửiemail,chargepay- ment, update database cần idempotencykey. Instructor (VinUni) AICB·Day08 Week5 19/25

---

<!-- chiron-source-span: {"source_span_id":"782653c6-8b09-52f9-a3db-252b18244bc9","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Observability: trace, metric, report","extraction_method":"pdf-text-layer"},"checksum":"cc6cdfbaf6104bacaac57d585a202c8d954dde2b3dae927f8c5da7147d191c40"} -->

## Slide 27 - Observability: trace, metric, report

Metrics bắt buộc

- tasksuccessrate;

- nodesvisited;

- retrycount;

- interruptcount;

- statevalidationerrors;

- latencyperrun;

- resumesuccess.
Report bắt buộc

- architecturediagram;

- stateschema;

- testcases;

- metricstable;

- failureanalysis;

- improvementplan.
Checkpoint:Labsẽchấmbằngcảcodechạyđược,metricsJSONvàreport markdown. Instructor (VinUni) AICB·Day08 Week5 20/25

---

<!-- chiron-source-span: {"source_span_id":"f6c9ab46-7de3-5721-821e-2eadec5ffdb1","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Lab 4 giờ","extraction_method":"pdf-text-layer"},"checksum":"441dbb471e00b948dfaf9ae15bab44638b1c9ad425bc227895b2279f16a7dcac"} -->

## Slide 28 - Lab 4 giờ

06 XâyLangGraphworkflowchoagentxửlýyêucầusupport córouting,HITL,retryvàmetricreport.

---

<!-- chiron-source-span: {"source_span_id":"0c8d64b7-ef95-5ed8-9ece-ed10199adbe9","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Lab objective","extraction_method":"pdf-text-layer"},"checksum":"16ee200e39c754a02f67a194b2e4661d28db06ee11d636c8fcb3535d838dc9ef"} -->

## Slide 29 - Lab objective

- Hoànthiệnproductionskeletonrepo: stateschema,nodes,graphwiring,
persistenceadapter.

- Chạy6testscenarios: simple,tool,missing-info,risky-action,
transient-error,max-error.

- XuấtfilemetricsJSONvàreportmarkdowntheotemplate.

- Họcviêngiỏihoànthànhextension: crash-resume,time-traveldebug
hoặcparallelfan-out. Skeletonđãcóvùng TODO(student). Khôngcầnviếtlạikiếntrúcrepo; tập trunghoànthiệnlogicvàbằngchứngchấmđiểm. Instructor (VinUni) AICB·Day08 Week5 21/25

---

<!-- chiron-source-span: {"source_span_id":"e7fee46c-1b2e-58c4-aa61-a2a08de82ee9","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Lab milestones 4 giờ","extraction_method":"pdf-text-layer"},"checksum":"da78186161415c3d27e0656ed63c8d592cdb611f3bfd8e7ae2bf899bec1c4186"} -->

## Slide 30 - Lab milestones 4 giờ

Thờigian Việccầnlàm Deliverable 0-30’ Setup repo, chạy tests baseline, đọc stateschema screenshot/testslog 30-75’ Implementcorenodes+graphwiring coretestspass 75-120’ Conditionalrouting+retry+HITLmock 6scenariosrun 120-180’ Persistence/checkpoint+crash-resume extension traceJSON/history 180-225’ Metricsrunner+reporttemplate metrics.json + re- port.md 225-240’ Demo,cleanup,self-assessment finalzip/repo Instructor (VinUni) AICB·Day08 Week5 22/25

---

<!-- chiron-source-span: {"source_span_id":"8e9f929a-07e9-54a1-bc03-fd883254bc61","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Scoring rubric","extraction_method":"pdf-text-layer"},"checksum":"aa7f5170365ba3e9aaf3624d8694f5e2c775285595ab1210f34fcf383eb47f99"} -->

## Slide 31 - Scoring rubric

Hạngmục Điểm Tiêuchí Architecture&state 20 Typed state, reducer đúng, node nhỏ và testable Graphbehavior 25 Routingđúng,retrycógiớihạn,HITLhoạt động Persistence&recovery 15 Checkpoint,threadid,resumehoặcmock tươngđương Metrics&tests 20 Metrics JSON hợp lệ, 6 scenarios, tests pass Report&demo 15 Report rõ, failure analysis, dia- gram/screenshot Productionhygiene 5 README,config,typing,lint,envhandling Instructor (VinUni) AICB·Day08 Week5 23/25

---

<!-- chiron-source-span: {"source_span_id":"7e5cdfdb-45fc-5ae3-b193-bd53b243ce77","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"Demo format cuối lab","extraction_method":"pdf-text-layer"},"checksum":"b0e1c5c4704186fb94e97d87366236a8ebc991e691eac1b164feed70743e7b16"} -->

## Slide 32 - Demo format cuối lab

1. Graphcủabạncónhữngnodenàovàstatefieldquantrọngnhấtlàgì?

2. Mộttestcaseđiquaroutenào? Córetry/interruptkhông?

3. MetricsJSONchothấysuccessrate,retrycount,interruptcountlàbao nhiêu?

4. Bạnđãchứngminhresume/crashrecoverythếnào?

5. Nếuthêm1ngày,bạnsẽproductionizephầnnàotrước? Instructor (VinUni) AICB·Day08 Week5 24/25

---

<!-- chiron-source-span: {"source_span_id":"1d5ca670-6358-5073-89dd-6f90932ed42c","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"T akeaways","extraction_method":"pdf-text-layer"},"checksum":"d98ed4d3d856be97df42dd03313645d21c43d4a25cbc3ae3ffaee29b7dccaab1"} -->

## Slide 33 - T akeaways

07 LangGraphkhôngchỉlàthưviệnorchestration;nólàcách thiếtkếagentnhưmộtsystemcóstate,auditvàrecovery.

---

<!-- chiron-source-span: {"source_span_id":"0f83a72a-286d-5e5e-ac38-030f37d6185b","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Tổng kết — Key T akeaways","extraction_method":"pdf-text-layer"},"checksum":"219d749b4fc553f16f7e3052b78305e86d8a55c3f913c4ccae94d3f87f7f10cd"} -->

## Slide 34 - Tổng kết — Key T akeaways

Những ý chính cần nhớ trướckhisangbàitiếptheo

- DùngLCELchopipelinetuyếntính;dùngLangGraphkhicóloop,
conditionalroute,persistencehoặcHITL.

- Stateschemavàreducerquyếtđịnhđộổnđịnhcủagraph.

- CheckpointinglànềntảngchoHITL,memory,timetravelvàfault
tolerance.

- Productionagentcầnmetric,tracevàreport,khôngchỉdemochạyđược.
Instructor (VinUni) AICB·Day08 Week5 24/25

---

<!-- chiron-source-span: {"source_span_id":"3f3a5931-e01b-534b-9506-b2747fa09248","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"References","extraction_method":"pdf-text-layer"},"checksum":"a0c5c53b3ec2c4de3070fe87fac5971634b0f22c0d09108d40a82f513f31540a"} -->

## Slide 35 - References

1. LangGraphdocumentation: Persistence,Human-in-the-loop,FunctionalAPI. docs.langchain.com/oss/python/langgraph

2. LangGraphreference: StateGraph,interrupt,Command,checkpointers. reference.langchain.com

3. LangChainblog/docsexamplesforagentworkflowsanddeployment. langchain.com Instructor (VinUni) AICB·Day08 Week5 25/25

---

<!-- chiron-source-span: {"source_span_id":"5935ad3a-a717-5bec-bf93-2d0fbcbb7e3a","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Hỏi & Đáp","extraction_method":"pdf-text-layer-sparse","page_image":"../../assets/page-images/098a68cfc9f5/page-0036.png","visual_fallback":true},"checksum":"85d68bfe7e22254d451986cab9a83fa61967c5c9a265bdb543377a3c5017c42a"} -->

## Slide 36 - Hỏi & Đáp

![Visual fallback - track 3 - day 23 - slide 36](../../assets/page-images/098a68cfc9f5/page-0036.png)

> Trang này được giữ dưới dạng ảnh vì text layer/OCR không đủ để biểu diễn nội dung trực quan.
