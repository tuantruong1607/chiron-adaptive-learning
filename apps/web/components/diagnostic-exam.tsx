"use client";

import {
  ArrowLeft,
  ArrowRight,
  Check,
  CloudCheck,
} from "@phosphor-icons/react";
import React, { useEffect, useState } from "react";

type DiagnosticQuestion = {
  id: string;
  concept_id: string;
  prompt: string;
  options: Array<{ id: string; text: string }>;
};

type Result = {
  score: number;
  total: number;
  mastery_updates: Array<{
    concept_id: string;
    previous: number;
    current: number;
  }>;
  answer_reviews?: Array<{
    question_id: string;
    concept_id: string;
    selected_option_id: string;
    correct_option_id: string;
    correct: boolean;
    explanation: string;
  }>;
};

function isResult(value: unknown): value is Result {
  if (!value || typeof value !== "object") return false;
  const candidate = value as Partial<Result>;
  return (
    typeof candidate.score === "number" &&
    typeof candidate.total === "number" &&
    Array.isArray(candidate.mastery_updates)
  );
}

export function DiagnosticExam() {
  const [questions, setQuestions] = useState<DiagnosticQuestion[]>([]);
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [ready, setReady] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<Result | null>(null);
  const [error, setError] = useState<string | null>(null);
  const question = questions[index];
  const masterySummary = result
    ? Object.values(
        result.mastery_updates.reduce<
          Record<string, Result["mastery_updates"][number]>
        >((summary, update) => {
          const existing = summary[update.concept_id];
          summary[update.concept_id] = {
            ...update,
            previous: existing?.previous ?? update.previous,
          };
          return summary;
        }, {}),
      )
    : [];
  const missedReviews =
    result?.answer_reviews?.filter((review) => !review.correct) ?? [];

  useEffect(() => {
    const saved = localStorage.getItem("chiron-diagnostic-draft");
    if (saved) {
      try {
        const parsed: unknown = JSON.parse(saved);
        if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
          setAnswers(parsed as Record<string, string>);
        } else {
          localStorage.removeItem("chiron-diagnostic-draft");
        }
      } catch {
        localStorage.removeItem("chiron-diagnostic-draft");
      }
    }
    fetch("/api/diagnostic", { cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) throw new Error("Diagnostic unavailable");
        return response.json();
      })
      .then((payload: DiagnosticQuestion[]) => {
        setQuestions(payload);
        setReady(true);
      })
      .catch(() => {
        setError("Không thể tải bài đánh giá đầu vào. Hãy thử tải lại trang.");
        setReady(true);
      });
  }, []);

  useEffect(() => {
    if (ready)
      localStorage.setItem("chiron-diagnostic-draft", JSON.stringify(answers));
  }, [answers, ready]);

  async function submit() {
    setSubmitting(true);
    setError(null);
    try {
      const response = await fetch("/api/diagnostic", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Idempotency-Key": crypto.randomUUID(),
        },
        body: JSON.stringify({
          answers: Object.entries(answers).map(([questionId, optionId]) => ({
            questionId,
            optionId,
          })),
        }),
      });
      const data: unknown = await response.json().catch(() => null);
      if (!response.ok || !isResult(data)) {
        throw new Error("Diagnostic request failed");
      }
      setResult(data);
      localStorage.removeItem("chiron-diagnostic-draft");
      window.dispatchEvent(new Event("chiron:diagnostic-completed"));
    } catch {
      setError(
        "Không thể chấm bài lúc này. Câu trả lời của bạn vẫn được lưu; hãy thử lại.",
      );
    } finally {
      setSubmitting(false);
    }
  }

  if (!ready)
    return (
      <div className="exam-skeleton" aria-label="Đang tải bài diagnostic">
        <div />
        <div />
        <div />
        <div />
      </div>
    );
  if (!questions.length)
    return (
      <p className="form-error" role="alert">
        {error}
      </p>
    );
  if (result)
    return (
      <section className="diagnostic-result">
        <span>Đã hoàn thành đánh giá đầu vào</span>
        <h2>
          {result.score}/{result.total}
        </h2>
        <p>
          Chiron đã cập nhật {masterySummary.length} nhóm kiến thức
          và sắp xếp lại kế hoạch hôm nay.
        </p>
        <div className="result-updates">
          {masterySummary.map((update) => (
            <div key={update.concept_id}>
              <span>{conceptLabel(update.concept_id)}</span>
              <strong>
                {Math.round(update.previous * 100)}% →{" "}
                {Math.round(update.current * 100)}%
              </strong>
            </div>
          ))}
        </div>
        {missedReviews.length ? (
          <details className="diagnostic-review">
            <summary>
              Xem giải thích {missedReviews.length} câu cần học lại
            </summary>
            <div aria-label="Giải thích đáp án">
              {missedReviews.map((review) => (
                <div className="review-missed" key={review.question_id}>
                  <strong>
                    Cần học lại · {conceptLabel(review.concept_id)}
                  </strong>
                  <p>{review.explanation}</p>
                  <a
                    href={`/learn?concept=${encodeURIComponent(review.concept_id)}`}
                  >
                    Mở micro-lesson →
                  </a>
                </div>
              ))}
            </div>
          </details>
        ) : null}
        <a className="button button-primary" href="/map?from=diagnostic">
          Xem điểm yếu trên bản đồ <ArrowRight size={18} />
        </a>
      </section>
    );
  return (
    <section className="exam-surface">
      <div className="exam-topline">
        <span>
          Bước 1/3 · Câu {index + 1} / {questions.length}
        </span>
        <span>
          <CloudCheck size={17} /> Đã lưu trên thiết bị
        </span>
      </div>
      <div
        className="question-progress"
        aria-label={`Đã hoàn thành ${Object.keys(answers).length} trên ${questions.length} câu`}
      >
        {questions.map((item, questionIndex) => (
          <button
            key={item.id}
            className={`${questionIndex === index ? "current" : ""} ${answers[item.id] ? "answered" : ""}`}
            onClick={() => setIndex(questionIndex)}
            aria-label={`Đi tới câu ${questionIndex + 1}`}
          >
            {answers[item.id] && <Check size={12} weight="bold" />}
          </button>
        ))}
      </div>
      <div className="question-body">
        <p>Chủ đề: {conceptLabel(question.concept_id)}</p>
        <h2>{question.prompt}</h2>
        <div
          className="answer-options"
          role="radiogroup"
          aria-label="Các lựa chọn"
        >
          {question.options.map((option) => (
            <button
              type="button"
              role="radio"
              aria-checked={answers[question.id] === option.id}
              key={option.id}
              className={answers[question.id] === option.id ? "selected" : ""}
              onClick={() =>
                setAnswers((current) => ({
                  ...current,
                  [question.id]: option.id,
                }))
              }
            >
              <span>{option.id.toUpperCase()}</span>
              {option.text}
            </button>
          ))}
        </div>
      </div>
      <div className="exam-actions">
        <button
          className="button button-secondary"
          disabled={index === 0}
          onClick={() => setIndex((value) => value - 1)}
        >
          <ArrowLeft size={18} /> Câu trước
        </button>
        {index < questions.length - 1 ? (
          <button
            className="button button-primary"
            disabled={!answers[question.id]}
            onClick={() => setIndex((value) => value + 1)}
          >
            Câu tiếp <ArrowRight size={18} />
          </button>
        ) : (
          <button
            className="button button-primary"
            disabled={
              Object.keys(answers).length !== questions.length || submitting
            }
            onClick={submit}
          >
            {submitting ? "Đang chấm" : "Nộp bài"} <ArrowRight size={18} />
          </button>
        )}
      </div>
      {error && (
        <p className="form-error" role="alert">
          {error}
        </p>
      )}
    </section>
  );
}

function conceptLabel(id: string) {
  return (
    {
      rrf: "Reciprocal Rank Fusion",
      chunking: "Hierarchical chunking",
      dense: "Dense retrieval",
      sparse: "Sparse retrieval",
      reranking: "Cross-encoder reranking",
      "graph-routing": "Graph-lite routing",
      citation: "Citation verification",
      evaluation: "RAG evaluation",
      "metadata-filtering": "Metadata filtering",
    }[id] ?? id
  );
}
