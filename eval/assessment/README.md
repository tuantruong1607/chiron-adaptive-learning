# Chiron assessment reasoning evaluation

Track này dành riêng cho câu hỏi luyện đề và thi thử. Nó không dùng retrieval accuracy làm tín hiệu chất lượng duy nhất.

## Khác với user question

Một `user_question` ưu tiên truy xuất đúng evidence và giải thích dễ hiểu. Một `assessment_item` phải buộc học viên tự suy luận, không để tutor tiết lộ đáp án trước khi nộp, và cần chấm cả kết quả lẫn tiến trình tư duy.

## Contract dự kiến

- `id`, `course_id`, `concept_ids`, `source_span_ids`.
- `interaction_type=assessment_item`.
- `question_type`: multiple choice, short answer hoặc essay.
- `cognitive_level`: remember, understand, apply, analyze, evaluate hoặc create.
- `difficulty` và `estimated_time_seconds`.
- `prompt`, `constraints`, `gold_answer` và `solution_steps`.
- `rubric_dimensions`: correctness, reasoning, evidence use, assumptions và communication.
- `common_misconceptions`, `acceptable_alternatives`, `fatal_errors`.
- `answer_leakage_policy`: những evidence/hint không được hiển thị trước khi submit.
- `review_status`, `reviewed_by`, `reviewed_at`.

## Evaluation layers

1. Deterministic grading cho đáp án có cấu trúc hoặc multiple choice.
2. LLM-as-judge theo rubric cho short answer/essay, kèm critic pass và calibration trên bài đã được người thật chấm.
3. Reasoning coverage: có nêu giả định, nối đủ bước và dùng evidence đúng hay không.
4. Pedagogy: feedback chỉ ra lỗi tư duy và bài cần ôn, không chỉ đưa đáp án.
5. Reliability: agreement với human grader, score drift, cost và latency.

Golden assessment set chỉ được approve sau khi người ra đề kiểm tra độ khó, đáp án, rubric và nguy cơ leakage.
