---
schema_version: 1
course_id: rag-intensive
document_id: "c9ce87e4-d8e2-54c8-9bbf-6dab10b707af"
document_version_id: "14bb9a61-066d-5681-82d8-6fa56b20c61e"
document_kind: slide_deck
source_type: course_pdf
authority: primary
title: "Multi-Agent Systems"
source_file: "track 3- day 20.pdf"
source_path: "C:\\Users\\banka\\Documents\\slide bài học\\track 3- day 20.pdf"
source_sha256: "519da7ddb2a719b2d7e65a640709950802dfb303f9bae80d05b8f9132e3d96ea"
parser_version: chiron-structured-markdown-v1
page_count: 37
sparse_page_count: 0
extraction_methods: "{\"pdf-text-layer\":37}"
language: vi
---

# Multi-Agent Systems

> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking.

<!-- chiron-source-span: {"source_span_id":"4bb4a781-b1e7-5c64-bf66-0cb02c289d8a","locator":{"kind":"page","page":1,"label":"Slide 1","section_title":"Multi-AgentSystems","extraction_method":"pdf-text-layer"},"checksum":"fbc1f7c13a6c0dcd243074a06bd34c0570459950aa60536e9253e19138b481eb"} -->

## Slide 1 - Multi-AgentSystems

AICB-P2T3·Ngày20·Chương4—AgentNângCao VinUniversity VinUniversity · Phase2·Track3·Tuần4

---

<!-- chiron-source-span: {"source_span_id":"8408fa8e-81fa-54f3-82e9-7580967e3001","locator":{"kind":"page","page":2,"label":"Slide 2","section_title":"HÃYSUYNGHĨ...","extraction_method":"pdf-text-layer"},"checksum":"e37e4fba0ea13804802bb48483704d6ef58fe691654bbc1c637279e546fbafab"} -->

## Slide 2 - HÃYSUYNGHĨ...

? “Khimộtagentkhôngđủ—Su- pervisor,Debate,Parallelpatterns giảiquyếtbàitoánnhưthếnào?” Giữcâuhỏinàytrongđầukhihọcbàihômnay

---

<!-- chiron-source-span: {"source_span_id":"3d727ec1-7af0-53d0-91b5-7506061a016e","locator":{"kind":"page","page":3,"label":"Slide 3","section_title":"Nộidungbàihọc","extraction_method":"pdf-text-layer"},"checksum":"276fad0240acbc7741232ec18a46ab40fe624f9e840b4d7ffdd42b8c7cd63c71"} -->

## Slide 3 - Nộidungbàihọc

1. TạisaocầnnhiềuAgent?

2. 5AgenticWorkflowPatterns(Anthropic)

3. SupervisorPattern—Orchestration

4. DebateAgents—AdversarialCollaboration

5. ParallelExecution&SharedState

6. Multi-AgentFrameworks

7. Demo&Thựchành VinUniversity (VinUni) AICB·Ngày20 Tuần4 1/25

---

<!-- chiron-source-span: {"source_span_id":"a362c39b-6e73-577e-adba-0cd8133fe7c2","locator":{"kind":"page","page":4,"label":"Slide 4","section_title":"TạisaocầnnhiềuAgent?","extraction_method":"pdf-text-layer"},"checksum":"0ea025841dedd42f2584118506044bd18b1ad40bb1aebbc702c0c2b8dcc353c4"} -->

## Slide 4 - TạisaocầnnhiềuAgent?

01 Taxonomy,failuremodes,vànguyêntắc“Startsimplest”

---

<!-- chiron-source-span: {"source_span_id":"becb03b5-1715-5956-8836-c3b28a9800b7","locator":{"kind":"page","page":5,"label":"Slide 5","section_title":"Trựcgiáccốtlõi","extraction_method":"pdf-text-layer"},"checksum":"5d658dffacc9e8b230a6d70df55d1e3eca11a856f8da54b663053d4076a4799a"} -->

## Slide 5 - Trựcgiáccốtlõi

Multi-Agent=Teamdựán Multi-agentgiốngteamdựán:có PM(supervisor),specialists(workers), shareddocument (state). Singleagent =1ngườilàmhết: research,phântích,viếtbáocáo. Tốt chotaskđơngiản. Multi-agent = team 3 người: researcher tìm data, analyst phân tích, writerviết—mỗingườimaster1việc. Nhưng:Teamcũngcóoverhead—họp,miscommunication,conflict. Chỉ scalekhi1ngườikhôngđủ. VinUniversity (VinUni) AICB·Ngày20 Tuần4 2/25

---

<!-- chiron-source-span: {"source_span_id":"4cc6d6d6-3e2a-56bb-a086-5efa3be32736","locator":{"kind":"page","page":6,"label":"Slide 6","section_title":"Multi-AgentTaxonomy—KhinàocầnnhiềuAgent?","extraction_method":"pdf-text-layer"},"checksum":"5dfb26814c1e244c58fd7fdcdecbf1c2fde09bad3b98bd94696e38161d42e833"} -->

## Slide 6 - Multi-AgentTaxonomy—KhinàocầnnhiềuAgent?

SingleAgent Specialization Parallelization Cross-checking “BagofAgents” dưới80% latency hallucination Nhiềuagents+khôngcleardecomposition=chaos

### 3lýdochínhđểmulti-agent

1. Specialization: mỗiagent master1domain

2. Parallelization: concurrent subtasks,giảmlatency

3. Cross-checking: consensus giảmhallucination Lưuý: Decisionrule: nếusin- gle agent đạt trên 80% accu- racythì KHÔNGthêmagents —complexitykhôngjustify. VinUniversity (VinUni) AICB·Ngày20 Tuần4 3/25

---

<!-- chiron-source-span: {"source_span_id":"f0d9a235-2f7d-5834-a260-8998d4a9b74d","locator":{"kind":"page","page":7,"label":"Slide 7","section_title":"Vídụthựctiễn—multi-agentgiảiquyếtvấnđềgì?","extraction_method":"pdf-text-layer"},"checksum":"07f6faf982b74089ce99f0ef1bf7cb236289c0f620dc675a8811e7934c7ef61a"} -->

## Slide 7 - Vídụthựctiễn—multi-agentgiảiquyếtvấnđềgì?

Usecase Cấutrúcagent Điểmhọcviêncầnnhớ Customer support triage TriageagentroutesangBilling/Refund/ FAQagent. Reference: OpenAIAgents SDKhandoffs, https://developers.openai. com/api/docs/guides/agents/orchestration Đâylàroutingpatterndễhiểunhất: mỗi intentcóspecialistriêng;sairoutethì usernhậncâutrảlờisai. Code review assis- tant Plannerchiatask,Codeagentsửa,Test agentchạytest,Revieweragentcritique. Reference: GitHubAgentHQ/coding agentsdiscussion, https://github.blog/ Multi-agenthữuíchkhicần plan–implement–verify,nhưngphảicó test/CIlàmgroundtruth. Researchreport Searcherthuthậpnguồn,Analysttrích insight,Writerviết,Criticfact-check. Reference: Anthropicworkflows, https://www.anthropic.com/engineering/ building-effective-agents Phùhợplabhômnayvìdễsosánhsingle vsmulti-agenttheoquality,latency, cost. Enterprise work- flow ADKagentteamsphốihợpvớitoolsvà observability. Reference: GoogleADK, https://adk.dev/ Productionkhôngchỉlàprompt: cần deploy,evaluate,trace,auth,guardrails. Role-based au- tomation CrewAIcrews: role,goal,tools,task. Reference: https://crewai.com/ Tốtđểprototypenhanhkhimuốnhọc viênthấy“agentnhưmộtvaitròtrong team”. Conversationalcol- laboration AutoGengroupchat/agent

### conversations. Reference:https
//microsoft.github.io/autogen/stable/ Dùngđểminhhọadebate, human-in-loop,multi-turncoordination. Mỗinhómchọn1vídụ,trảlời: agentroleslàgì? sharedstatechứagì? failuremodenguyhiểmnhấtlàgì? VinUniversity (VinUni) AICB·Ngày20 Tuần4 4/25

---

<!-- chiron-source-span: {"source_span_id":"f31d5151-f5a1-5767-82e7-f95a6bbb33a7","locator":{"kind":"page","page":8,"label":"Slide 8","section_title":"Hoạtđộng1—Singleagenthaymulti-agent?","extraction_method":"pdf-text-layer"},"checksum":"1a9eb8f281f653fbbf40cfe1a7698c078cb71c4e0a2ac3ab6a720bf3596c2fc1"} -->

## Slide 8 - Hoạtđộng1—Singleagenthaymulti-agent?

### Nhiệmvụnhóm(8phút)

1. Vớimỗitask,chọn: singleagent, workflow,hay multi-agent.

2. Giảithíchbottleneckchính: accuracy, latency,cost,hayownership.

3. Nêuítnhất1lỗimớinếudùngnhiều agent. Task:FAQđơngiản;researchreport; refundworkflow;codemigration. “Nếu dùng nhiều agent, lỗi mớinàoxuấthiện? Nếudùng một agent, lỗi nào khó kiểm soát?” Lưu ý:Mục tiêu không phải chọnmulti-agentcàngnhiều càngtốt;mụctiêulàbiết khi nàokhôngnêndùng. VinUniversity (VinUni) AICB·Ngày20 Tuần4 5/25

---

<!-- chiron-source-span: {"source_span_id":"fae884e5-b818-506a-b3a0-830c4421afab","locator":{"kind":"page","page":9,"label":"Slide 9","section_title":"MAST: lỗi thường đến từ thiết kế hệ thống, không chỉ từ model","extraction_method":"pdf-text-layer"},"checksum":"be53e5a35a9d21d27b4cc5a35d8320a3a6d8ed7ee1825961b3debb2040870452"} -->

## Slide 9 - MAST: lỗi thường đến từ thiết kế hệ thống, không chỉ từ model

14 Failuremodes identified 3

### Nhómlỗi
spec,align- ment,verification 150+ Tasksđược phântích “WhyDoMulti-AgentLLMSystemsFail?” (arXiv:2503.13657)chỉranhiều lỗiđến từspecification / system design,inter-agent misalignment, vàverification/termination. Vìvậycầndefineroles,stopcondition,và rubrictrướckhicode. VinUniversity (VinUni) AICB·Ngày20 Tuần4 6/25

---

<!-- chiron-source-span: {"source_span_id":"578723e6-10c5-5c2b-b15e-3898f5d54cf1","locator":{"kind":"page","page":10,"label":"Slide 10","section_title":"5AgenticWorkflowPat","extraction_method":"pdf-text-layer"},"checksum":"6401de3aa688c367c0db95938c96941f4c3bae5494a828bc1ee743e555b50204"} -->

## Slide 10 - 5AgenticWorkflowPat

02 5AgenticWorkflowPat- terns(Anthropic) Từđơngiảnđếnphứctạp—escalatedần

---

<!-- chiron-source-span: {"source_span_id":"e12f0c22-c81b-5227-8173-24ad95eaa3db","locator":{"kind":"page","page":11,"label":"Slide 11","section_title":"5Patterns—EscalationLadder","extraction_method":"pdf-text-layer"},"checksum":"18cd9496db32981cde8c62e012a1510b97adae00d2254a7ba99d43464c09753c"} -->

## Slide 11 - 5Patterns—EscalationLadder

1. Prompt Chaining 2. Routing 3. Parallel 4. Orchestrator Workers

5. Evaluator Optimizer Complexity+Failuremodestăng Sequential validateeach Classify route Sectioning Voting Supervisor delegates Generate critiqueloop “Start simplest. Only add agents whenmeasurablyneeded.” Thử PromptChainingtrước. Chỉesca- latekhicóbằngchứngcần. Sectioning: splittasks →parallel workers Voting: same task → multiple LLMs →aggregate VinUniversity (VinUni) AICB·Ngày20 Tuần4 7/25

---

<!-- chiron-source-span: {"source_span_id":"21f54597-3095-5fb4-8c72-e9072af9fb96","locator":{"kind":"page","page":12,"label":"Slide 12","section_title":"Hoạtđộng2—PatternCardSorting","extraction_method":"pdf-text-layer"},"checksum":"c46ef8e4574f0afde488bfd6d264174ec79edbc2e1fd02b32049de416a66b1f7"} -->

## Slide 12 - Hoạtđộng2—PatternCardSorting

Chianhóm3người,mỗinhómnhận

### 1case

- Tổnghợpreviewkháchhàngtừ
1.000comment

- Xửlýticketrefund/billing/
technicalsupport

- Viếtbáocáothịtrườngcófact-check
nguồn

- Migratecodebasevàđảmbảotest
pass Nhiệmvụ: chọn1trong5patterns,vẽ flowtrong4phút. Mỗinhómnói30giây: pattern, lý do, metric đo thành công, failureguard. Lưu ý:Không được mặc định “supervisorchomọithứ”. Hãy chứng minh pattern đơn giản hơnchưađủ. VinUniversity (VinUni) AICB·Ngày20 Tuần4 8/25

---

<!-- chiron-source-span: {"source_span_id":"a1828386-30ee-591e-a794-b0b6a4c6123f","locator":{"kind":"page","page":13,"label":"Slide 13","section_title":"RoutingPattern—CostOptimization","extraction_method":"pdf-text-layer"},"checksum":"82fc2501e3e973179cf5ada6795426679154655e8048a5dec3086576fba36c32"} -->

## Slide 13 - RoutingPattern—CostOptimization

Routing — Classify input rồi chuyển đến specialized handler. Easy queries dùng small model, hardqueriesdùnglargemodel.

- 70%querieseasy=smallmodel
(GPT-4o-mini)

- 30%querieshard=largemodel
(GPT-4o)

- Giảm50%+chiphítổngthể
Khi workload cóbimodal diffi- culty — nhiều query đơn giản + ítqueryphứctạp. Lưu ý:Routing chỉ hiệu quả khi phânloạichínhxác. Saiphânloại =queryhardgửichosmallmodel =kếtquảkém. VinUniversity (VinUni) AICB·Ngày20 Tuần4 9/25

---

<!-- chiron-source-span: {"source_span_id":"20544fc8-f529-50ac-96c9-c0a19c1c8f14","locator":{"kind":"page","page":14,"label":"Slide 14","section_title":"SupervisorPattern—Or","extraction_method":"pdf-text-layer"},"checksum":"98ada6a8f5f0946b4e0917d83929b6228a02e4197b4b3f871b08e8ce1b035d02"} -->

## Slide 14 - SupervisorPattern—Or

03 SupervisorPattern—Or- chestration Hub-spokedelegationvớiLangGraph

---

<!-- chiron-source-span: {"source_span_id":"d411e20a-b17f-557e-a7c8-ab6ffbfd46cc","locator":{"kind":"page","page":15,"label":"Slide 15","section_title":"SupervisorPattern—Hub-SpokeArchitecture","extraction_method":"pdf-text-layer"},"checksum":"c31cc2cae41c573d456d7e32daf85f3cb17d4889ef4f601305e203358ff2f30e"} -->

## Slide 15 - SupervisorPattern—Hub-SpokeArchitecture

Supervisor (LLMRouter) Search Agent Analysis Agent Writer Agent Code Agent SharedState messages,worker_results,final_answer delegate delegate delegate delegate

### Supervisor — LLM router
nhận task, decompose, route đến workers, aggregate re- sults

- Mỗiworkerlànoderiêngvới
owntools

- Supervisorquyếtđịnh: gọiai,
theothứtựnào

- Costinsight: cheapmodel
chorouting,expensivemodel choworkers VinUniversity (VinUni) AICB·Ngày20 Tuần4 10/25

---

<!-- chiron-source-span: {"source_span_id":"d4143c5f-c708-59f5-930e-cc28dede7bc4","locator":{"kind":"page","page":16,"label":"Slide 16","section_title":"SupervisorState—LangGraphImplementation","extraction_method":"pdf-text-layer"},"checksum":"30063b28bab298faacc79c315adcf4701c85f2ccf858fe487460d36b606acadf"} -->

## Slide 16 - SupervisorState—LangGraphImplementation

```text
class SupervisorState(TypedDict):
```
messages: list[BaseMessage] next_worker: str worker_results: dict[str, str] final_answer: str # Supervisor routing via tool calls

```text
def supervisor(state):
response = llm.invoke(
system= "Route task to workers",
tools=[search, analyze, write],
messages=state[ "messages"]
)
return {"next_worker": response.tool}
```
# Build graph graph = StateGraph(SupervisorState) graph.add_node("supervisor", supervisor) graph.add_node("search", search_agent) graph.add_node("analyze", analysis_agent)

### Stategồm4thànhphần

1. messages: conversation context

2. next_worker: aiđượcgọitiếp

3. worker_results: outputtừmỗi worker

4. final_answer: kếtquảtổng hợp Lưu ý:Failure modes:#1in- finite routing loop (A→ B → A).#2wrongworkerselection. Cầnmaxiterations guard. VinUniversity (VinUni) AICB·Ngày20 Tuần4 11/25

---

<!-- chiron-source-span: {"source_span_id":"87eb5d8a-d33f-5d88-8f76-3783923809db","locator":{"kind":"page","page":17,"label":"Slide 17","section_title":"DebateAgents—Adversar","extraction_method":"pdf-text-layer"},"checksum":"7e1b5501175b5117dcd5854ada529c41d9f6639782d6ef1b12a9b23972b1c21e"} -->

## Slide 17 - DebateAgents—Adversar

04 DebateAgents—Adversar- ialCollaboration Giảmhallucinationquatranhluậncókiểmsoát

---

<!-- chiron-source-span: {"source_span_id":"5744b31f-85ae-51ea-9cb4-bf1186f49d94","locator":{"kind":"page","page":18,"label":"Slide 18","section_title":"DebatePattern—AdversarialCollaboration","extraction_method":"pdf-text-layer"},"checksum":"1c1164d77bdae1eeed1fc1aef0176d100bc0f2339bc63f2c7d6386a06c973521"} -->

## Slide 18 - DebatePattern—AdversarialCollaboration

AgentA (GPT-4o) AgentB (Claude) AnswerA AnswerB critique critique Judge Synthesize FinalAnswer

### Flow

1. AgentA&Banswer independently

2. Critiquenhau(adversarial)

3. Judgesynthesizefinalanswer Debategiảmhallucination 15– 25%. Hiệu quả nhất cho am- biguous queries, high-stakes decisions. Lưuý: “Collectivedelusion”: cảhaiđồngýsai

- Judgekhôngcatch. Fix: dùngdiverse
models. VinUniversity (VinUni) AICB·Ngày20 Tuần4 12/25

---

<!-- chiron-source-span: {"source_span_id":"0b666858-8ec3-5886-8792-51915e316098","locator":{"kind":"page","page":19,"label":"Slide 19","section_title":"SocietyofMind—HeterogeneousAgents","extraction_method":"pdf-text-layer"},"checksum":"204a64a87821850901ad8c77f7894a39a383648ab360d94e96a3f7798630873f"} -->

## Slide 19 - SocietyofMind—HeterogeneousAgents

Agent Model Strength Researcher GPT-4o Broadknowledge Analyst Claude Nuancedreasoning Critic Gemini Differenttrainingdata Judge Best-of Finalsynthesis Mỗi model cóblind spots khác nhaudo training data diversity. GPT-4 + Claude + Gemini

- better coverage hơn 3 in-
stancesGPT-4. Trade-off: thêmlatency(sequential critique)+cost(3models). Chỉjustifycho high-stakes. VinUniversity (VinUni) AICB·Ngày20 Tuần4 13/25

---

<!-- chiron-source-span: {"source_span_id":"0495885a-3bbd-583b-bf1b-36bb292ceb65","locator":{"kind":"page","page":20,"label":"Slide 20","section_title":"ParallelExecution&Shared","extraction_method":"pdf-text-layer"},"checksum":"8f7c33656082aab6dd76819655b2b497dc15cae50342b88bdde1e60c224dc0c1"} -->

## Slide 20 - ParallelExecution&Shared

05 State Map-reduce,AsyncIO,vàcoordinationpatterns

---

<!-- chiron-source-span: {"source_span_id":"90381a21-7188-527e-9ad3-3a13179d9549","locator":{"kind":"page","page":21,"label":"Slide 21","section_title":"ParallelAgentExecution—Map-Reduce","extraction_method":"pdf-text-layer"},"checksum":"8aebb07b836e9234906dd73c1286a167dab758688a864226a4e8a9fd510e25dc"} -->

## Slide 21 - ParallelAgentExecution—Map-Reduce

Task Worker1 Worker2 WorkerN Merge Aggregate Result ... concurrent LangGraphSendAPI Dynamic fan-out + parallel branches — built-in parallelism. Mỗi worker chạy concurrent, mergekhitấtcảdone.

### Lưuý: “Parallel ̸=alwaysfaster”
DAG dependencies, shared state locks, merge conflicts có thể negatespeedup. Đotrướckhias- sume. VinUniversity (VinUni) AICB·Ngày20 Tuần4 14/25

---

<!-- chiron-source-span: {"source_span_id":"28fe1b16-09e5-5966-8064-d76c36b0daa6","locator":{"kind":"page","page":22,"label":"Slide 22","section_title":"SharedState—CoordinationArchitecture","extraction_method":"pdf-text-layer"},"checksum":"e5449743e8e150c407fc2e0abcff611e649c542fe4b3af4c5f72c42eb36ba766"} -->

## Slide 22 - SharedState—CoordinationArchitecture

Shared state (blackboard)— Agents read/write central state — simple, cần locks cho con- current writes. LangGraph dùng TypedDictstatemặcđịnh. Message passing — Async queue (Redis Pub/Sub, Kafka) — decoupled, scalable, thêm net- worklatency. Tốtchodistributed systems. Lưuý: Contextlossacrosshand- offs: biggest coordination failure. Mỗi agent nhận partial context, qualitygiảm. Multi-agent without tracing = im- possible to debug. Dùng Lang- Smith hoặc Langfuse cho mọi multi-agentsystem. Failurehandling: supervisordetecttimeoutthì retrydifferentworkerhoặcfallback. VinUniversity (VinUni) AICB·Ngày20 Tuần4 15/25

---

<!-- chiron-source-span: {"source_span_id":"76bbaa6e-8ddc-5fc0-a54c-846edead10ad","locator":{"kind":"page","page":23,"label":"Slide 23","section_title":"AsyncIOvàAgentPools—ProductionConcurrency","extraction_method":"pdf-text-layer"},"checksum":"24314281e9fcda000d830bca1cd18a618561c7f7ebfe87436ba6a2de23be3773"} -->

## Slide 23 - AsyncIOvàAgentPools—ProductionConcurrency

Trueconcurrentexecutionchomultipleagents. asyncio.gather(agent1(), agent2())

- ParallelAPIcalls,sharedeventloop
Pre-initializeNinstances,usequeue

- Amortizeinitcost,controlconcurrency
GiốngthreadpoolnhưngchoLLMagents

### Productionfailurehandling

- Supervisordetect timeout →retryhoặc
fallback

- Circuitbreaker: fail3lần →skip,log,
backup

- Deadletterqueue: failedtaskslưulạiđể
debug Lưuý: Poolsize=concurrentAPI rate limit. Quá nhiều agents→ ratelimiterrors. VinUniversity (VinUni) AICB·Ngày20 Tuần4 16/25

---

<!-- chiron-source-span: {"source_span_id":"755edae0-2350-5548-a977-cfcb65206bf7","locator":{"kind":"page","page":24,"label":"Slide 24","section_title":"Multi-AgentFrameworks","extraction_method":"pdf-text-layer"},"checksum":"4c648d33fc3ca03920e1ba755422623f8d380360e65276b5b53c7eece301cc0e"} -->

## Slide 24 - Multi-AgentFrameworks

06 LangGraph,AutoGen,CrewAI—chọnđúngcôngcụ

---

<!-- chiron-source-span: {"source_span_id":"10429522-3dce-5ced-bbd3-f9c0f0f7c10e","locator":{"kind":"page","page":25,"label":"Slide 25","section_title":"FrameworkComparison—Chọntheousecase","extraction_method":"pdf-text-layer"},"checksum":"0410f3ae97f8a6f8f716a8439982289dbbf35afd0cf61858c7e9e5e08120e7b4"} -->

## Slide 25 - FrameworkComparison—Chọntheousecase

Framework Flexibility Setup Bestfor Ghichú LangGraph Cao Trungbình Production Statemachines,fullcontrol CrewAI Trungbình Dễ Prototype Role-based,nhanhonboard AutoGen Cao Trungbình Codeexec GroupChat,human-in-loop OpenAISDK Thấp Rấtdễ Simple Lightweight,tool-usefocused GoogleADK Trungbình Trungbình GCP VertexAI,A2Aprotocol AutoGen/CrewAItốtchoprototypenhanh. LangGraphchoproduction — fullstatecontrol,debugging,conditionalrouting. Migratekhicầnscale. VinUniversity (VinUni) AICB·Ngày20 Tuần4 17/25

---

<!-- chiron-source-span: {"source_span_id":"580c66fc-355e-51af-b7e9-c09763568b73","locator":{"kind":"page","page":26,"label":"Slide 26","section_title":"Demo&Thựchành","extraction_method":"pdf-text-layer"},"checksum":"ec9512750b1896149ce97b9c7d92ecacfe345a44af1106ff55d46843695a0ba0"} -->

## Slide 26 - Demo&Thựchành

07 Multi-AgentResearchSystem+2giờlabcópeerreview

---

<!-- chiron-source-span: {"source_span_id":"8d12bd99-b5bc-5cd0-bb02-379bf45319de","locator":{"kind":"page","page":27,"label":"Slide 27","section_title":"Predict-before-demo—họcviênđoántracetrước","extraction_method":"pdf-text-layer"},"checksum":"619246bc7d4fac1ca844b2508ada50bf48f6d33fd09f1a8ab6194fe525c8788f"} -->

## Slide 27 - Predict-before-demo—họcviênđoántracetrước

Cho học viên xem task: “Re- search GraphRAG state-of-the-art,

### write 500-word summary”. Hỏi
agent nào nên chạy trước? bước nàocóthểparallel? SosánhdựđoánvớiLangSmith trace: route có đúng không? worker nào tốn token nhất? lỗi nàocầnguardrail? Biếndemotừ“giảngviênbiểudiễn”thành“họcviêndebugmộthệthống thật”. VinUniversity (VinUni) AICB·Ngày20 Tuần4 18/25

---

<!-- chiron-source-span: {"source_span_id":"ce571ebe-3408-594c-a066-1dd1697ff702","locator":{"kind":"page","page":28,"label":"Slide 28","section_title":"Multi-AgentResearchSystem—LiveDemo","extraction_method":"pdf-text-layer"},"checksum":"8f7af52e2fecd19cf3aafd3094925ed778296946dc5109d4d86bb44b8c898c91"} -->

## Slide 28 - Multi-AgentResearchSystem—LiveDemo

1. Pipeline: Supervisor+SearchAgent+AnalysisAgent+WriterAgent

2. Task: “ResearchGraphRAGstate-of-the-art,write500-word summary”—supervisorcoordinates

3. LangSmithtrace: routingdecisions,paralleltimeline,workeroutputs, finalsynthesis

4. Sosánh: single-agentvsmulti-agenttrêncùngtask—quality, latency,cost VinUniversity (VinUni) AICB·Ngày20 Tuần4 19/25

---

<!-- chiron-source-span: {"source_span_id":"9ba107ab-97de-5a37-b723-03048ad5796d","locator":{"kind":"page","page":29,"label":"Slide 29","section_title":"Lab#20","extraction_method":"pdf-text-layer"},"checksum":"827189979d76f1c89779dd10e8afc0aff2d6e2c78b5aecfa69bcab30cf647937"} -->

## Slide 29 - Lab#20

Mụctiêu: Build3-agentresearchsystem: Researcher+Analyst+Writer vớiLangGraph Deliverable: Benchmarkreport: single-agentvsmulti-agent(accuracy, latency,cost)+LangSmithtraces Thờigian: 2giờ VinUniversity (VinUni) AICB·Ngày20 Tuần4 20/25

---

<!-- chiron-source-span: {"source_span_id":"3a89197f-aad3-54f7-b659-f75a59a5618b","locator":{"kind":"page","page":30,"label":"Slide 30","section_title":"Lab20—2giờthựchànhtheomilestone","extraction_method":"pdf-text-layer"},"checksum":"0a1d54db0b619f5dc41dd8aa0930157ecd86072d60271fe7c1838e0919be21a9"} -->

## Slide 30 - Lab20—2giờthựchànhtheomilestone

1. 0–15’Setup: clonestarter,setAPIkey,chạysingle-agentbaseline.

2. 15–45’Buildsupervisor: LangGraphstatemachine,routingviatoolcalls.

3. 45–75’Add3workers: SearchAgent,AnalysisAgent,WriterAgent;lưu outputvàosharedstate.

4. 75–95’Trace&benchmark: singlevsmultitrên3–5researchqueries;đo quality,latency,cost.

5. 95–115’Peerreview: đổinhóm,đọctracecủanhau,tìm1failuremodevà đềxuấtfix.

6. 115–120’Exitticket: mỗinhómghi1điềunêndùngmulti-agentvà1điều khôngnêndùng. GitHubrepo+benchmarkreport+1LangSmith/Langfusetracescreenshot. Bonus: thêmCriticAgentđểfact-check. VinUniversity (VinUni) AICB·Ngày20 Tuần4 21/25

---

<!-- chiron-source-span: {"source_span_id":"e37c5756-bace-5b96-a8d5-188527eff982","locator":{"kind":"page","page":31,"label":"Slide 31","section_title":"Peer Review Rubric — giảm nhàm chán, tăng chất lượng lab","extraction_method":"pdf-text-layer"},"checksum":"ea4ca91a2402c19cb3af1aa415c64f359e426c9927d456d20540a137b463784a"} -->

## Slide 31 - Peer Review Rubric — giảm nhàm chán, tăng chất lượng lab

Tiêuchí Câuhỏipeerreviewerphảitrảlời Điểm Roleclarity Mỗiagentcónhiệmvụrõ,khôngoverlapquá nhiềukhông? 0–2 Statedesign Sharedstatecóđủthôngtinđểhandoffmàkhông mấtcontextkhông? 0–2 Failureguard Cómaxiterations,timeout,retry/fallback,hoặc validationkhông? 0–2 Benchmark Cósosánhsinglevsmulti-agentbằngmetriccụ thểkhông? 0–2 Traceexplanation Nhómgiảithíchđượctrace: ailàmgì,tốnbao nhiêu,saiởđâukhông? 0–2 Mỗinhómreview1nhómkháctrong8phút, sauđóownercó5phútsửa nhanh. VinUniversity (VinUni) AICB·Ngày20 Tuần4 22/25

---

<!-- chiron-source-span: {"source_span_id":"e0f22e1c-cd29-5115-be5a-25f13bea59a9","locator":{"kind":"page","page":32,"label":"Slide 32","section_title":"QUIZChương4+MILESTONE1","extraction_method":"pdf-text-layer"},"checksum":"c8a69feb43cd67245866eb3280c89f75645198be33bde3c1288234f26b782770"} -->

## Slide 32 - QUIZChương4+MILESTONE1

10 câu trắc nghiệm + short an-

### swer
Scope: Reflexion, Memory Sys- tems,ProductionRAG,GraphRAG, Multi-Agent Format: 7MC+3shortanswer Câu hỏi test understanding, không test nhớ syntax

### SubmitportfoliotừN16–N20

- Lab16: Reflexionagent

- Lab17: Memorysystem

- Lab18: ProductionRAG

- Lab19: GraphRAG

- Lab20: Multi-agentsystem
Deadline: 1tuầnsauN20 VinUniversity (VinUni) AICB·Ngày20 Tuần4 23/25

---

<!-- chiron-source-span: {"source_span_id":"649094ad-0b80-508e-bb5a-d12584ef0760","locator":{"kind":"page","page":33,"label":"Slide 33","section_title":"Referencelinkschohọcviêntựđọcthêm","extraction_method":"pdf-text-layer"},"checksum":"e13255fee897600522f333a22b46ca72d7d1b22a5de55243342dc78768c9faa6"} -->

## Slide 33 - Referencelinkschohọcviêntựđọcthêm

Anthropic: Buildingeffectiveagents anthropic.com/engineering/building-effective-agents OpenAI: Agents SDK orchestration +handoffs developers.openai.com/.../orchestration LangGraphsupervisorlibrary reference.langchain.com/python/langgraph-supervisor

### AutoGen
microsoft.github.io/autogen CrewAI: crewai.com GoogleADK: adk.dev MASTpaper:WhyDoMulti-AgentLLM SystemsFail? arxiv.org/abs/2503.13657 Lưuý: Gợiýđọc: họcviênchỉcầnđọcAnthropic+OpenAIhandoffstrước lab;cáclinkcònlạidùngkhichọnframeworkchoproject. VinUniversity (VinUni) AICB·Ngày20 Tuần4 24/25

---

<!-- chiron-source-span: {"source_span_id":"6c423cab-ab90-53ba-92c6-41eb2620275f","locator":{"kind":"page","page":34,"label":"Slide 34","section_title":"Tổngkết—KeyTakeaways","extraction_method":"pdf-text-layer"},"checksum":"d57eb3da74736ba504b6204bf1c77cca98481039a4c9c9cca2f83bce0f4d6f62"} -->

## Slide 34 - Tổngkết—KeyTakeaways

Nhữngýchínhcầnnhớ trướckhisangbàitiếptheo 1 Supervisorlàmostpracticalmulti-agentarchitecture—clearownership,easyde- bug,production-ready 2 Debate giảm hallucination 15–25% nhưng tốn 2–3× cost — chỉ dùng cho high- stakesdecisions 3 Parallelexecutioncắtlatencynhưngcầncarefulstatemergestrategy—“parallel ̸=alwaysfaster” 4 Buổihọcgiữlýthuyếttrong2giờ;2giờcònlạibuild,trace,benchmark,peerreview VinUniversity (VinUni) AICB·Ngày20 Tuần4 24/25

---

<!-- chiron-source-span: {"source_span_id":"fb55a779-b17b-5fb9-a284-20e828425093","locator":{"kind":"page","page":35,"label":"Slide 35","section_title":"Tiếptheo&Bàitập","extraction_method":"pdf-text-layer"},"checksum":"82a899396bc319197a2905c5968e761e89e1ca93a68852665cb450adb29118ca"} -->

## Slide 35 - Tiếptheo&Bàitập

Ngày21: Fine-tuningLLMs— LoRA/QLoRA “Khi nào nên fine-tune — và khi nàopromptengineeringđủrồi?”

- HoànthànhLab20+submit
Milestone1portfolio

- Đọc: MASTpaper(NeurIPS
2025)—multi-agentfailure taxonomy VinUniversity (VinUni) AICB·Ngày20 Tuần4 25/25

---

<!-- chiron-source-span: {"source_span_id":"93c939e4-22d5-53f2-914f-607c84722d96","locator":{"kind":"page","page":36,"label":"Slide 36","section_title":"Hỏi&Đáp","extraction_method":"pdf-text-layer"},"checksum":"5b15986f67697082998a9937adfe4426211429eb27e1431ebefcb25e5c0955e4"} -->

## Slide 36 - Hỏi&Đáp

SupervisorvsDebatevsParallel—khinào dùngpatternnào? Singleagentcókhinàođủ?

---

<!-- chiron-source-span: {"source_span_id":"b9f6079d-6bef-5124-b8b0-52478c8abe1b","locator":{"kind":"page","page":37,"label":"Slide 37","section_title":"Cảmơn!","extraction_method":"pdf-text-layer"},"checksum":"0ac639e5e5f5bf87c116113082818dd282f4a71b03261768f36c9117798d2edd"} -->

## Slide 37 - Cảmơn!

AICB-P2T3·Ngày20·Multi-AgentSystems github.com/vinuni-aicb Liênhệ: instructor@vinuni.edu.vn
