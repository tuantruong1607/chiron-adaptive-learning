# Kế hoạch dữ liệu học tập và Knowledge Map — Chiron AI

## 1. Mục tiêu và nguyên tắc

Mục tiêu của phase này là biến corpus đã index thành closed loop có thể kiểm chứng:

```text
course source
  -> taxonomy + source provenance
  -> blueprint + question/rubric bank
  -> learner attempt/evidence
  -> mastery + recommendation
  -> interactive knowledge map + targeted practice
```

Nguyên tắc:

- Không đưa câu AI sinh thẳng vào đề chính thức. Mọi item phải có source, concept, objective, đáp án/rubric và review state.
- Không suy ra mastery chỉ từ chat. Mastery chỉ cập nhật từ diagnostic, exam, lab, explain-back hoặc recheck có rubric.
- Source span là bằng chứng/citation; concept là đơn vị tri thức; question là đơn vị đo lường.
- Một version được publish phải bất biến. Thay đổi source, graph, blueprint hoặc rubric tạo version mới.

## 2. Hiện trạng dữ liệu

| Lớp dữ liệu | Trạng thái | Khoảng trống cần đóng |
| --- | --- | --- |
| Corpus | 69 tài liệu, 2.817 source spans, 5.070 child chunks đã index | Thiếu source tier và learning-objective mapping hoàn chỉnh |
| Graph taxonomy | 34 nodes, 29 edges, 102 chunk-concept links đã approved qua deterministic quality gate | Graph version vẫn draft và chưa qua multi-hop quality gate để active retrieval |
| Golden tutor retrieval | 50 câu, split development/holdout, hybrid baseline pass | Không thay thế evaluation cho đề thi hoặc rubric tư duy |
| Diagnostic/demo | Vertical slice/seed tồn tại | Chưa có blueprint thi thật, question bank và coverage toàn corpus |
| Essay grading | Provider/router, rubric contract và LLM-as-Judge có validation output sẵn sàng | Cần rubric versioned theo dạng bài, score audit và calibration tự động |
| Learner evidence | Schema, evidence ledger, mastery state, study plan đã có | Chưa có dữ liệu learner thật, consent/retention policy và calibration cohort |
| Practice labs | Hybrid-search lab/HTML nguồn đã parse | Chưa có catalog 6 lab với learning evidence nhất quán |

## 3. Workstream A — Course specification và taxonomy

### A1. Course specification v1

Tạo `data/courses/rag-intensive/course-spec-v1.yaml` gồm:

- Course, kỳ thi, ngày thi, thời lượng và target score.
- Exam blueprint: số câu, tỷ trọng recall/application/reasoning, MCQ/short answer/essay, độ khó easy/medium/hard.
- Danh sách learning objectives có mã ổn định `LO-xxx`.
- Quy tắc pass, partial credit và prerequisite policy.
- Danh sách source document/version được phép dùng làm ground truth.

Exit gate: product owner xác nhận blueprint trước khi sinh hoặc nhập question bank.

### A2. Taxonomy v1

Mỗi concept phải có:

```text
concept_id, canonical_name, summary_vi, learning_objective_ids,
exam_weight, prerequisite_ids, misconception_ids,
source_span_ids, review_status, graph_version
```

Quy trình:

1. Deterministic quality gate đã pass trên toàn bộ taxonomy: provenance, confidence, relation whitelist, tenant/course scope và prerequisite DAG.
2. Chuẩn hóa relation ontology; chỉ dùng `prerequisite_of`, `part_of`, `contrasts_with`, `applies_to` trong map MVP.
3. Kiểm tra cycle, provenance coverage và source conflict.
4. Tạo graph version `reviewed`, chưa active.
5. Chỉ activate sau graph evaluation mới đạt multi-hop gate.

Exit gate: 20–40 concept approved, 100% node/edge có evidence source span, prerequisite DAG không cycle.

## 4. Workstream B — Question bank và exam blueprint

### B1. Question data contract

Mỗi question phải lưu tối thiểu:

```text
question_id, course_id, version, type, cognitive_level, difficulty,
concept_ids, learning_objective_ids, source_span_ids, stem, choices,
answer_key, rationale, misconception_target, rubric_id,
estimated_minutes, review_status, authoring_method
```

`type`: `single_choice`, `ordering_or_matching`, `scenario_diagnosis`, `code_or_pseudocode`, `system_design`, `tracing_and_monitoring_diagnosis`, `security_and_data_governance`, `guardrail_or_incident_reasoning`. Mọi objective có đúng bốn option A–D và một đáp án; không dùng multi-select.

`cognitive_level`: recall, understand, apply, analyze, evaluate.

### B2. Bank construction pipeline

1. Nhập bất kỳ đề cũ/đề mẫu do chủ dự án cung cấp; lưu nguyên bản và provenance.
2. Map từng câu vào concept + LO + độ khó + cognitive level.
3. Dùng LLM chỉ để sinh candidate/biến thể khi thiếu coverage.
4. Validator kiểm tra answerability từ source, duplicate, answer leakage, ambiguity và coverage.
5. Human review theo batch; chỉ `approved` mới vào mock exam.
6. Blueprint assembler chọn câu theo quota, không chọn hai câu cùng misconception trừ khi deliberate recheck.

### B3. Blueprint đã chốt cho course RAG-intensive

Source of truth: `data/courses/rag-intensive/course-spec-v1.yaml`.

| Scope | Tổng | Objective | Tự luận | Ý nghĩa |
| --- | ---: | ---: | ---: | --- |
| Day 1–15 | 65 | 61 | 4 | Kiến thức và tư duy AI nền tảng |
| Track 2 | 12 | 11 | 1 | Mở rộng breadth và nối nền tảng với production |
| Track 3 | 23 | 18 | 5 | Ưu tiên AI application, AI infra và AI product |
| **Tổng** | **100** | **90** | **10** | **120 phút** |

Track 3 chia 8 câu AI application, 8 câu AI infrastructure, 7 câu AI product. Dù chỉ chiếm 23% tổng số câu, Track 3 nhận 5/10 câu tự luận để đo năng lực thiết kế và judgment thay vì học thuộc.

90 câu objective gồm 66 single-choice, 8 ordering/matching và 16 scenario diagnosis. Cognitive mix là 15 recall, 25 understand, 35 apply và 15 analyze. Difficulty mix là 25 easy, 45 medium, 20 hard.

10 câu tự luận gồm 2 code/pseudocode, 3 system design, 2 tracing/monitoring diagnosis, 2 security/data governance và 1 guardrail/incident reasoning. Hai scenario bắt buộc là monitoring chất lượng Agent theo thời gian và kiến trúc bảo vệ dữ liệu khách hàng nhạy cảm.

### B4. Mốc dữ liệu

- P0 diagnostic: 20–30 câu, bao phủ concept trọng tâm.
- P1 bank candidate rộng: 720 objective + 90 constructed-response, sinh/import có provenance và validator.
- P2 reviewed pool: 540 objective + 60 constructed-response; đủ sáu parallel form có reuse được kiểm soát.
- P3 mock exam: 100 câu theo blueprint đã duyệt; mỗi concept quan trọng có easy/medium/hard và recall/reasoning coverage.

Exit gate P0: 100% diagnostic question có source, concept, đáp án/rubric và review. Exit gate P1: blueprint coverage đạt 100%, không leakage/duplicate nghiêm trọng.

## 5. Workstream C — Essay rubric và golden grading set

### C1. Rubric library

Tạo rubric theo dạng bài, không tạo một rubric chung. Mỗi rubric có:

```text
rubric_id, task_type, criteria, weight, score_band_descriptors,
required_reasoning_steps, acceptable_alternatives,
common_errors, source_span_ids, human_review_threshold
```

Ví dụ criterion: correctness, reasoning chain, evidence use, assumption handling, trade-off, clarity.

### C2. Golden set

- 10–20 câu tự luận trọng tâm.
- Mỗi câu có 8–15 bài làm đại diện: xuất sắc, thiếu bước, misconception, lạc đề, answer dài nhưng rỗng, lời giải khác nhưng đúng.
- LLM-as-Judge chấm theo rubric versioned, strict JSON và criterion evidence; lưu score, confidence, provider/model và feedback để audit.
- Không gửi private learner answer sang Gemini Free.

Exit gate: rubric rõ partial credit; judge output hợp lệ, score nằm trong range, confidence/audit đầy đủ. Điểm confidence thấp được đánh dấu để learner thấy đó là đánh giá cần kiểm tra lại.

## 6. Workstream D — Practice-lab catalogue và learner evidence

### D1. Lab catalogue

Mỗi lab định nghĩa:

```text
lab_id, concepts, objective, scenario, initial_state, interactions,
deterministic_checks, rubric, transfer_question, source_span_ids,
evidence_signal, expected_minutes
```

Ưu tiên 6 lab đầu:

1. Chunking strategy.
2. Dense/sparse/hybrid retrieval.
3. RRF và ranking trade-off.
4. Metadata/tenant filtering.
5. RAG evaluation diagnosis.
6. Graph-lite routing và hop/cost control.

### D2. Learner data collection

Lưu event tối thiểu: attempt started/submitted, answer score, criterion score, lab action, recheck outcome, tutor citation click. Không log raw private data vào observability.

Thêm consent/retention policy trước pilot; tách demo/synthetic/learner thật.

Exit gate: một learner đi qua diagnostic → weak concept → source/lab/recheck → evidence/mastery update → revised plan.

## 7. Workstream E — Interactive Knowledge Map

### E0. Trạng thái hiện tại

Đã có map SVG frontend với 8 node/9 edge demo, filter mastery, click node và citation drawer. Chưa có runtime graph data hoặc interaction canvas đầy đủ.

### E1. Data-connected map (P0)

1. Tạo BFF route gọi authenticated `GET /api/v1/courses/{course}/knowledge-map`.
2. API trả graph version, node/edge review status, learner mastery/confidence, exam weight, citations và recommended action.
3. Bỏ `demo-data.ts` khỏi `/map`; page header lấy count/version thật.
4. Node drawer mở source locator, hiển thị prerequisite/downstream, weak reason và CTA `Học`, `Làm recheck`, `Mở lab`.
5. Chỉ hiển thị `active` graph cho learner; review UI là route admin riêng.

Exit gate: learner chỉ thấy graph của tenant/course được enroll; click node mở citation và action thật.

### E2. Spatial interaction và accessibility (P1)

Khi map đạt 20–40 node, dùng `@xyflow/react` thay SVG thủ công để có:

- Zoom/pan, fit view, minimap và keyboard navigation.
- Search concept; filter mastery/relation/source tier.
- Focus neighborhood 1–2 hop, highlight prerequisite path và weak-concept path.
- Layout deterministic bằng DAG/ELK hoặc dagre chạy server/build-time, không tính layout mỗi render.
- Reduced motion, node text readable, màu không là tín hiệu duy nhất.

Không cần graph database chỉ để render map; API read model từ PostgreSQL đủ cho course graph nhỏ-vừa.

### E3. Personalization and explainability (P2)

- Node size theo exam weight; color/badge theo mastery + evidence confidence.
- Edge style theo relation và review/source strength.
- “Why this next?” hiển thị evidence, prerequisite và thời gian còn lại đến exam.
- Compare current mastery với prior snapshot, không dùng animation thay số liệu.

Exit gate: learner tìm được phần yếu, hiểu lý do và đi được tới resource/practice trong tối đa ba thao tác.

## 8. Thứ tự thực thi đề xuất

| Thứ tự | Deliverable | Phụ thuộc | Quyết định/review cần có |
| --- | --- | --- | --- |
| 1 | Course specification + exam blueprint v1 | Đã có `course-spec-v1.yaml` | Duyệt phân bổ 65/12/23 và cognitive mix |
| 2 | Review taxonomy graph còn lại | Corpus hiện có | Duyệt batch node/edge |
| 3 | Diagnostic 20–30 câu + question schema/importer | Blueprint + taxonomy | Duyệt sample 10 câu |
| 4 | Data-connected map E1 | Active read graph hoặc reviewed read model | UX/source drawer review |
| 5 | Rubric library + essay golden set | Form tự luận thật | Duyệt rubric và sample chấm |
| 6 | Sáu practice labs + evidence contract | Taxonomy + source spans | Review pedagogical quality |
| 7 | Mock exam 100 câu + parallel forms | Các bước 1–6 | Blueprint/QA sign-off |
| 8 | Map E2/E3 và Graph-lite activation experiment | Graph RAGAS uplift | Chỉ activate khi eval pass |

## 9. Việc cần từ chủ dự án

Để bắt đầu Workstream B, cần một mô tả ngắn của đề thi: môn/phạm vi, tỷ lệ MCQ–tự luận, số câu mỗi dạng, thang điểm, thời lượng, và 3–5 ví dụ câu tiêu biểu nếu có. Không cần format file cố định; Chiron sẽ chuyển thành `course-spec-v1` có version/review.
