"use client";

import { CheckCircle, ClockCountdown } from "@phosphor-icons/react";
import React, { useCallback, useEffect, useState } from "react";

type Essay = {
  id: string;
  prompt: string;
  answer: string;
  score?: number | null;
  max_score?: number | null;
  confidence?: number | null;
  feedback?: string | null;
  rubric_version?: string | null;
  criterion_scores: Record<string, number>;
  created_at: string;
};

type ReviewDraft = {
  score: number;
  maxScore: number;
  feedback: string;
  criterionScores: Record<string, number>;
};

function ReviewCard({
  essay,
  onReleased,
}: {
  essay: Essay;
  onReleased: (id: string) => void;
}) {
  const [draft, setDraft] = useState<ReviewDraft>({
    score: essay.score ?? 0,
    maxScore: essay.max_score ?? 10,
    feedback: essay.feedback ?? "",
    criterionScores: essay.criterion_scores,
  });
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function release() {
    setSaving(true);
    setError(null);
    try {
      const response = await fetch(`/api/essays/${essay.id}/review`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          score: draft.score,
          max_score: draft.maxScore,
          feedback: draft.feedback,
          criterion_scores: draft.criterionScores,
        }),
      });
      const payload = await response.json();
      if (!response.ok)
        throw new Error(
          payload.detail ?? payload.error ?? "Không thể release điểm.",
        );
      onReleased(essay.id);
    } catch (reason) {
      setError(
        reason instanceof Error ? reason.message : "Không thể release điểm.",
      );
    } finally {
      setSaving(false);
    }
  }

  return (
    <article className="glass-surface review-card">
      <div className="review-card-meta">
        <span>
          <ClockCountdown size={16} />{" "}
          {new Date(essay.created_at).toLocaleString("vi-VN")}
        </span>
        <strong>{essay.rubric_version ?? "Rubric chưa xác định"}</strong>
      </div>
      <h2>{essay.prompt}</h2>
      <div className="review-answer">{essay.answer}</div>
      {essay.confidence != null && (
        <p className="muted-copy">
          AI confidence: {Math.round(essay.confidence * 100)}%
        </p>
      )}
      <div className="review-score-grid">
        <label>
          Điểm
          <input
            type="number"
            min="0"
            max={draft.maxScore}
            step="0.5"
            value={draft.score}
            onChange={(event) =>
              setDraft({ ...draft, score: Number(event.target.value) })
            }
          />
        </label>
        <label>
          Điểm tối đa
          <input
            type="number"
            min="1"
            step="1"
            value={draft.maxScore}
            onChange={(event) =>
              setDraft({ ...draft, maxScore: Number(event.target.value) })
            }
          />
        </label>
      </div>
      {Object.keys(draft.criterionScores).length > 0 && (
        <div className="review-criteria">
          {Object.entries(draft.criterionScores).map(([criterion, value]) => (
            <label key={criterion}>
              {criterion}
              <input
                type="number"
                min="0"
                step="0.5"
                value={value}
                onChange={(event) =>
                  setDraft({
                    ...draft,
                    criterionScores: {
                      ...draft.criterionScores,
                      [criterion]: Number(event.target.value),
                    },
                  })
                }
              />
            </label>
          ))}
        </div>
      )}
      <label className="review-feedback">
        Nhận xét
        <textarea
          rows={4}
          value={draft.feedback}
          onChange={(event) =>
            setDraft({ ...draft, feedback: event.target.value })
          }
        />
      </label>
      <button
        className="button button-primary"
        type="button"
        disabled={
          saving || !draft.feedback.trim() || draft.score > draft.maxScore
        }
        onClick={() => void release()}
      >
        <CheckCircle size={17} weight="fill" />{" "}
        {saving ? "Đang release…" : "Xác nhận và release"}
      </button>
      {error && <p className="form-error">{error}</p>}
    </article>
  );
}

export function EssayReviewQueue() {
  const [essays, setEssays] = useState<Essay[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadQueue = useCallback(async () => {
    setError(null);
    const response = await fetch("/api/essays/review-queue", {
      cache: "no-store",
    });
    const payload = await response.json();
    if (!response.ok)
      throw new Error(
        payload.detail ?? payload.error ?? "Không thể tải review queue.",
      );
    setEssays(payload as Essay[]);
  }, []);

  useEffect(() => {
    void loadQueue()
      .catch((reason: Error) => setError(reason.message))
      .finally(() => setLoading(false));
  }, [loadQueue]);

  if (loading)
    return (
      <div className="glass-surface catalog-state">Đang tải review queue…</div>
    );
  if (error) return <div className="glass-surface catalog-state">{error}</div>;
  if (!essays.length)
    return (
      <div className="glass-surface review-empty">
        <CheckCircle size={28} />
        <h2>Review queue đã sạch</h2>
        <p>Không có bài confidence thấp hoặc quá SLA.</p>
      </div>
    );

  return (
    <section className="review-queue" aria-label="Essay review queue">
      {essays.map((essay) => (
        <ReviewCard
          key={essay.id}
          essay={essay}
          onReleased={(id) =>
            setEssays((current) => current.filter((item) => item.id !== id))
          }
        />
      ))}
    </section>
  );
}
