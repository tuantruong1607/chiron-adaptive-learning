"use client";

import { useEffect, useRef, useState } from "react";

type Essay = {
  id: string;
  status: "pending_ai_grading" | "graded" | "needs_human_review";
  score?: number | null;
  max_score?: number | null;
  confidence?: number | null;
  feedback?: string | null;
  criterion_scores?: Record<string, number>;
  human_review_required?: boolean;
};

const statusLabels: Record<Essay["status"], string> = {
  pending_ai_grading: "Đang chờ chấm",
  graded: "Đã chấm",
  needs_human_review: "Cần giảng viên review",
};

export function EssayEditor() {
  const [prompt, setPrompt] = useState(
    "Thiết kế một pipeline RAG có kiểm chứng nguồn và tenant isolation.",
  );
  const [answer, setAnswer] = useState("");
  const [essay, setEssay] = useState<Essay | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);
  const pollRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(
    () => () => {
      if (pollRef.current) clearInterval(pollRef.current);
    },
    [],
  );

  async function refresh(id: string) {
    const response = await fetch(`/api/essays/${id}`, { cache: "no-store" });
    if (!response.ok) throw new Error("Không thể tải trạng thái bài tự luận.");
    const payload = (await response.json()) as Essay;
    setError(null);
    setEssay(payload);
    if (payload.status !== "pending_ai_grading" && pollRef.current) {
      clearInterval(pollRef.current);
      pollRef.current = null;
    }
  }

  async function submit() {
    setSubmitting(true);
    setError(null);
    try {
      const response = await fetch("/api/essays", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Idempotency-Key": crypto.randomUUID(),
        },
        body: JSON.stringify({ prompt, answer, rubric_id: "system-design-v1" }),
      });
      const payload = await response.json();
      if (!response.ok)
        throw new Error(payload.detail ?? payload.error ?? "Submit thất bại.");
      setEssay(payload);
      if (payload.status === "pending_ai_grading") {
        pollRef.current = setInterval(() => {
          void refresh(payload.id).catch((reason: Error) =>
            setError(reason.message),
          );
        }, 3000);
      }
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "Submit thất bại.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="essay-layout">
      <section className="glass-surface essay-form">
        <p className="eyebrow">Constructed response</p>
        <h2>Viết câu trả lời có evidence</h2>
        <label>
          Prompt
          <textarea
            value={prompt}
            onChange={(event) => setPrompt(event.target.value)}
            rows={4}
          />
        </label>
        <label>
          Câu trả lời
          <textarea
            value={answer}
            onChange={(event) => setAnswer(event.target.value)}
            rows={12}
            placeholder="Nêu thiết kế, trade-off, source span/citation và cách kiểm chứng..."
          />
        </label>
        <button
          className="button button-primary"
          type="button"
          disabled={submitting || answer.trim().length < 1}
          onClick={() => void submit()}
        >
          {submitting ? "Đang gửi…" : "Gửi bài để chấm"}
        </button>
        {error && <p className="form-error">{error}</p>}
      </section>
      <aside className="glass-surface essay-result" aria-live="polite">
        <p className="eyebrow">Grading status</p>
        {!essay && (
          <p className="muted-copy">
            Bài sẽ được lưu riêng theo tài khoản và có thể xem lại sau khi gửi.
          </p>
        )}
        {essay && (
          <>
            <span className="concept-status">{statusLabels[essay.status]}</span>
            {essay.score != null && (
              <div className="mastery-number">
                <strong>
                  {essay.score}/{essay.max_score}
                </strong>
                <span>rubric score</span>
              </div>
            )}
            {essay.confidence != null && (
              <p className="muted-copy">
                Confidence: {Math.round(essay.confidence * 100)}%
              </p>
            )}
            {essay.feedback && <p>{essay.feedback}</p>}
            {essay.human_review_required && (
              <p className="review-note">
                Điểm chưa được release tự động; cần người review.
              </p>
            )}
            {essay.criterion_scores &&
              Object.keys(essay.criterion_scores).length > 0 && (
                <ul className="criterion-list">
                  {Object.entries(essay.criterion_scores).map(
                    ([key, value]) => (
                      <li key={key}>
                        <span>{key}</span>
                        <strong>{value}</strong>
                      </li>
                    ),
                  )}
                </ul>
              )}
          </>
        )}
      </aside>
    </div>
  );
}
