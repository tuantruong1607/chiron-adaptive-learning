# Chiron AI — Pipeline sinh và hiệu chuẩn ngân hàng câu hỏi

**Trạng thái:** proposed  
**Phạm vi:** tạo ngân hàng đề dựa trên corpus đã ingest, không phải sinh đề tự do từ web.  
**Nguồn điều khiển:** `data/courses/rag-intensive/course-spec-v1.yaml`.

## 1. Quyết định thiết kế

Chiron không coi một prompt tạo câu hỏi là một pipeline. Mỗi item được xuất bản phải là một record có thể trả lời bốn câu hỏi:

1. Câu này đo learning objective/concept nào, ở mức tư duy và độ khó nào?
2. Mọi mệnh đề chuyên môn và đáp án đúng dựa vào source span nào trong corpus?
3. Distractor hoặc rubric đang kiểm tra misconception/trade-off nào?
4. Các validator, reviewer và dữ liệu thực tế đã kết luận gì về chất lượng item?

Nguồn chuẩn là PostgreSQL. Qdrant chỉ phục vụ truy xuất evidence pack và tìm near-duplicate; không là nơi lưu item phiên bản hoặc quyết định xuất bản. Không gửi private learner data sang provider ngoài. Provider được phép nhận item spec và evidence tối thiểu cần thiết: **OpenAI (`gpt-4o-mini`) là generator chính cho batch lớn** — chọn vì trần TPM của Groq (8.000 token/phút) đẩy một batch 300 spec lên khoảng 6 giờ wall-clock; Groq (`gpt-oss-*`) giữ vai trò generator thay thế và critic độc lập. Gemini chỉ là fallback cho nội dung public/synthetic theo data policy hiện có. Corpus bài giảng được phép gửi sang generator; essay và PII của learner thì không.

## 2. Mục tiêu phát hành

| Tầng | Objective | Constructed response | Mục đích |
|---|---:|---:|---|
| Candidate | 720 | 90 | 3 biến thể cho khoảng 240 item spec objective, 2 biến thể cho 45 brief tự luận |
| Reviewed pool | 540 | 60 | pool đã qua validation và review, đủ sáu form song song |
| One exam form | 90 | 10 | 100 câu, 120 phút, theo course blueprint v1 |

Tỷ trọng thi chính thức giữ nguyên: Day 1–15: 65; Track 2: 12; Track 3: 23. Track 3 có 8 AI application, 8 AI infrastructure và 7 AI product. 90 câu objective gồm 66 single-choice, 8 ordering/matching và 16 scenario diagnosis; 10 câu tự luận bao gồm code/pseudocode, system design, tracing/monitoring, security/data governance và guardrail/incident reasoning.

## 3. Đơn vị đầu vào: item spec, không phải prompt

`BlueprintCompiler` phân rã blueprint thành item spec bất biến (JSONL + PostgreSQL). Mỗi spec chỉ định đúng một cell blueprint:

```json
{
  "spec_id": "qs-rag-apply-medium-001",
  "course_id": "rag-intensive",
  "concept_ids": ["retrieval", "citation"],
  "learning_objective": "Chọn chiến lược retrieval phù hợp với ràng buộc evidence.",
  "scope": "track-3.ai-application",
  "format": "scenario_diagnosis",
  "cognitive_level": "apply",
  "difficulty_target": "medium",
  "misconception_target": "Nhầm top-k cao với groundedness.",
  "required_evidence": {"min_source_spans": 2, "multi_hop": false},
  "generation_count": 3,
  "exposure_group": "form-set-a"
}
```

`EvidencePackBuilder` dùng hybrid retrieval đã khóa và concept/source-span provenance để lấy 3–5 evidence pack ngắn. Mỗi pack chứa text, `source_span_id`, title, locator và corpus version. Với item multi-hop, pack chỉ ghép 2–3 span đã có relation/route rõ ràng; không để model tự bịa liên kết từ toàn corpus.

## 4. Luồng pipeline đề xuất

```text
course blueprint + concepts + approved corpus
        -> BlueprintCompiler -> item specs
        -> EvidencePackBuilder -> versioned evidence packs
        -> candidate generation (fan-out)
        -> deterministic validation
        -> semantic critic + evidence verification
        -> near-duplicate / leakage / bias checks
        -> risk-based human review
        -> approved, versioned item bank
        -> form assembler -> delivery
        -> response telemetry -> CTT -> IRT when data supports it
```

Pipeline chạy bằng Celery worker + PostgreSQL outbox/job table. Đây là job fan-out có retry/idempotency rõ ràng; chưa cần LangGraph. Mỗi transition lưu `run_id`, prompt/template version, provider/model, corpus/graph version, input checksum và raw response đã redaction. Restart không tạo candidate hoặc review record trùng.

### 4.1 Sinh candidate có cấu trúc

- Generator chính: OpenAI `gpt-4o-mini`, Structured Outputs `strict: true`.
- Generator thay thế: Groq `openai/gpt-oss-20b` (`--provider groq`), dùng khi cần giữ dữ liệu trong Groq.
- Critic/rubric pass: Groq `openai/gpt-oss-120b`, độc lập với generator.
- Khi generator không khả dụng: dùng Qwen/GPT-OSS fallback nội bộ theo capability; Gemini chỉ được phép khi evidence pack được đánh dấu public/synthetic.
- Mỗi objective spec sinh 3 candidate khác nhau về bối cảnh hoặc misconception, **không** chỉ paraphrase stem. Mỗi brief tự luận sinh 2 candidate có rubric và acceptable alternatives.
- Generator chỉ nhận evidence pack, spec và format contract. System prompt yêu cầu viết tiếng Việt rõ ràng, giữ thuật ngữ kỹ thuật tiếng Anh khi cần, không chép nguyên câu slide, không đưa citation vào stem và không tiết lộ đáp án trong wording.

Ví dụ output contract objective:

```json
{
  "stem": "...",
  "options": [{"id": "A", "text": "...", "misconception": "..."}],
  "correct_option_ids": ["B"],
  "rationale": "...",
  "claim_to_evidence": [{"claim": "...", "source_span_ids": ["..."]}],
  "difficulty_rationale": "...",
  "authoring_notes": []
}
```

Tự luận bổ sung `rubric` theo criterion, score band 0–4/0–5, observable evidence, common failure modes và acceptable alternative solutions. AI grading sau này chỉ dùng rubric đã versioned, không dùng model để nghĩ rubric ngay khi chấm bài học viên.

### 4.2 Cổng xác thực bắt buộc

| Cổng | Cách thực hiện | Hành động khi fail |
|---|---|---|
| Schema/blueprint | Pydantic v2 + JSON Schema; format, số option, quota cell, language | reject và regenerate có targeted repair |
| Evidence | mọi claim trọng yếu/đáp án map tới source span cùng tenant/course/corpus version; kiểm tra source có tồn tại | reject, không cho model tự tìm web |
| Answerability | rule exact-one cho mọi objective; key hợp lệ; matching/order có canonical solution | reject |
| Distractor | mỗi distractor phải sai vì misconception xác định, không mơ hồ/đúng một phần và không có cue hình thức | critic/review queue |
| Semantic critic | model độc lập kiểm tra groundedness, uniqueness, cognitive level, difficulty fit và alternative valid answers | score/risk; reject hoặc review |
| Duplicate/leakage | lexical MinHash/3-gram + E5 nearest-neighbour qua Qdrant, sau đó cross-check semantic; closed-book solve check để phát hiện key lộ trong stem | merge/retire/rewrite |
| Fairness/security | cấm PII, prompt injection từ corpus, answer language mang tính định kiến, yêu cầu tool/knowledge ngoài scope | high-risk review |

Không dùng LLM judge làm cổng duy nhất. Validator xác định được phải chặn trước; critic là tín hiệu xếp hạng rủi ro. Ngưỡng duplicate, critic score và semantic similarity được calibration trên sample human-labeled, không hard-code như “sự thật” ngay từ đầu.

### 4.3 Review có trọng số rủi ro

- Bắt buộc expert review: toàn bộ câu tự luận, monitoring/security/guardrail system design, và mọi item có critic disagreement hoặc evidence multi-hop.
- Objective low-risk có thể auto-approve chỉ khi đủ evidence, validator pass, không duplicate, critic pass và nằm trong sample QA ngẫu nhiên.
- QA sampling theo từng blueprint cell, difficulty, track và item type để tránh chỉ review những chủ đề dễ.
- Reviewer thấy stem, đáp án/rationale, rubric, evidence excerpt/locator, validation trace và near-duplicates; không chỉ thấy một câu lẻ.

## 5. Mô hình dữ liệu cần bổ sung

| Bảng | Vai trò |
|---|---|
| `question_specs` | blueprint cell/version, concepts, objective, difficulty, misconception, desired variants |
| `evidence_packs` / `evidence_pack_spans` | snapshot span đã retrieve, checksum, corpus/graph version |
| `question_candidates` | immutable generated content, generator metadata, state, provenance |
| `question_versions` | bản đã sửa/approved/published, không overwrite candidate cũ |
| `question_concepts` | mapping item–concept với vai trò primary/prerequisite/application |
| `item_validations` | validator result, rule/version, score, findings, input checksum |
| `rubrics` / `rubric_criteria` | rubric tự luận, score bands, acceptable alternatives, grading version |
| `review_decisions` | reviewer, decision, reason code, provenance, timestamp |
| `exam_forms` / `exam_form_items` | assemble theo blueprint/exposure constraint, ordering seed |
| `item_response_stats` | aggregate không PII: p-value, point-biserial, distractor selection, timing, version |
| `item_calibration_runs` | CTT/IRT method, cohort, anchor items, uncertainty, result version |

Tất cả bảng learner-facing có `tenant_id` và RLS/tenant filter như kiến trúc hiện tại. Authoring records cũng scope theo tenant/course. `question_versions` là immutable sau publish; sửa item nghĩa là tạo version mới và retire version cũ có audit trail.

## 6. Công nghệ và kỹ thuật công khai áp dụng

| Nhu cầu | Lựa chọn Chiron | Lý do |
|---|---|---|
| Contract generation | Pydantic v2 + JSON Schema; Groq Structured Outputs khi model hỗ trợ | parse-safe, repair/retry có kiểm soát; Groq phân biệt JSON mode với schema-enforced Structured Outputs ([docs](https://console.groq.com/docs/structured-outputs)) |
| Durable orchestration | Celery + Redis + PostgreSQL job/outbox | phù hợp fan-out, retry/idempotency và hạ tầng Chiron đang có; không tăng thêm graph orchestration |
| Evidence & provenance | PostgreSQL source spans/concepts + hybrid Qdrant | chỉ sinh từ corpus có citation; Qdrant hỗ trợ candidate retrieval/near duplicate, không làm source of truth |
| Similarity / dedupe | local multilingual E5 + lexical MinHash/3-gram + semantic adjudication | kết hợp bắt literal clone và paraphrase clone, không gửi corpus ra embedding API |
| Retrieval eval | golden suite hiện hữu + RAGAS context precision/recall/noise sensitivity | RAGAS có metric cho RAG retrieval/faithfulness nhưng không thay psychometric evaluation ([RAGAS metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)) |
| Interoperability | canonical JSON nội bộ, mapping/export QTI 3 sau | QTI là chuẩn trao đổi item bank/delivery và có thiết kế accessibility/semantic HTML; không ép runtime Chiron phụ thuộc XML ngay MVP ([1EdTech QTI 3](https://www.1edtech.org/sites/default/files/media/docs/2025/WBR_040125_QTI.pdf)) |
| Post-release quality | CTT trước; IRT có anchor items sau khi đủ cohort | IRT phù hợp để ước lượng thuộc tính item, linking và theo dõi drift nhưng cần cẩn trọng với sample nhỏ ([IRT review](https://arxiv.org/abs/2108.08604), [ETS calibration study](https://www.ets.org/research/policy_research_reports/publications/report/2024/kgvw.html)) |

## 7. Evaluation đúng phạm vi

### Offline trước publish

1. **Blueprint coverage:** từng cell có candidate/reviewed/approved count; không lấy nhiều câu một concept để bù quota.
2. **Evidence coverage:** 100% published item có source provenance; reviewer spot-check correctness theo evidence pack.
3. **Quality set:** human-rated set tách development/holdout. Đo validator precision/recall, critic–human agreement, duplicate detection recall, và rubric–human agreement.
4. **Assessment reasoning:** đối với từng item, review solution chain, distractor misconception, alternative answers, expected time và answer leakage. Không áp approval của user-question RAG set sang assessment.
5. **Form equivalence:** kiểm tra coverage, type/difficulty/cognitive mix và exposure overlap trước publish.

### Sau delivery

- CTT: proportion-correct, point-biserial, distractor-selection, omit/time anomaly và version drift theo cohort.
- Tự luận: agreement giữa rubric/AI và double-scored human sample; phân tích theo criterion, không chỉ score tổng.
- Chỉ khi có cohort/anchor design phù hợp mới chạy IRT/calibration. Small-sample calibration có sai số đáng kể; không được diễn giải IRT như ground truth khi dữ liệu chưa đủ.
- Item bị lộ, ambiguous, có discrimination thấp hoặc dấu hiệu unfairness được `retired`; mastery evidence phải biết `question_version` để không làm nhiễm lịch sử.

## 8. Kế hoạch triển khai theo batch

### Batch A — Contract và pilot (P0)

1. Chốt `question_specs` schema, candidate schema, CR rubric schema và state machine.
2. Implement migrations/repositories, idempotent job/outbox và strict JSON adapter.
3. Viết evidence-pack builder dùng source-span provenance + snapshot manifest.
4. Tạo 30 objective + 6 tự luận phủ đủ 3 scope; chạy validators, critic, review pack.
5. Đặt threshold bằng review thực tế; chưa sinh mass batch.

**Exit gate:** 100% pilot có provenance/schema; không có key ambiguity/evidence failure sau expert review; reviewer xác nhận output trace đủ để quyết định.

### Batch B — Scale candidate pool (P1)

1. Dùng `data/questions/batches/batch-b-manifest-v1.yaml`: 12 wave, mỗi wave 60 objective candidate; 9 wave đầu có 8 CR candidate, 3 wave cuối có 6 CR candidate. Tổng đúng 720 objective + 90 CR.
2. Trước mỗi wave, gán concept/LO và evidence snapshot cho từng spec; không enqueue cell nào chưa có provenance hoặc có group/mutual-exclusion conflict.
3. Chạy theo wave có rate/budget caps, dedupe xuyên wave và risk routing. Mỗi objective luôn có 4 option A–D và một đáp án, kể cả `ordering_or_matching`.
4. Review có stratification; build 540 objective + 60 CR approved pool.
5. Form assembler tạo sáu form, kiểm tra blueprint/exposure/equivalence.

**Exit gate:** sáu form thỏa blueprint; mọi published item trace được về evidence/version/review; toàn bộ high-risk/CR đã review.

### Batch C — Delivery và calibration (P2)

1. Nối form delivery, autosave, timing và `question_version` response events.
2. AI grader chỉ chấm theo rubric versioned; luôn hiển thị criterion feedback/citation, cho phép appeal/review.
3. CTT dashboard, item retirement workflow và re-generation có spec/evidence mới.
4. Thiết kế anchor/pilot cohort trước khi áp IRT hoặc adaptive selection.

## 9. Những điều chưa làm ngay

- Không tự động research web để bù evidence trong item chính thức. Knowledge thiếu phải tạo content gap/curation task trước, sau đó mới tạo item.
- Không dùng một LLM vừa viết vừa tự certify chính nó.
- Không dùng RAGAS để kết luận một câu hỏi “hay”, “công bằng” hoặc psychometrically calibrated.
- Không đưa full corpus, raw essay hay learner PII vào provider fallback.
- Không sinh 720+90 trước khi Pilot P0 chứng minh validator/review loop hiệu quả.

## 10. Quyết định cần review trước khi code P0

1. Chấp nhận schema/state machine và policy: all CR + high-risk objective bắt buộc expert review.
2. Chọn 30 objective + 6 CR pilot topics từ Day 1–15 / Track 2 / Track 3.
3. Chỉ định người/nhóm làm expert reviewer và SLA review; chưa cần khóa threshold số học trước pilot.
