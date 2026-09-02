"use client";

import { ArrowSquareOut, Check, Lightbulb } from "@phosphor-icons/react";
import type { LearningResource as LearningResourceType } from "@chiron/domain";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

const aliases: Record<string, string> = {
  reciprocal_rank_fusion: "rrf",
  rag_evaluation: "evaluation",
  multi_hop_retrieval: "graph-routing",
  metadata_filtering: "metadata-filtering",
};

export function LearningResourceRail({
  preferredConceptId,
  compact = false,
  resourceOverride,
}: {
  preferredConceptId?: string;
  compact?: boolean;
  resourceOverride?: LearningResourceType;
}) {
  const [resources, setResources] = useState<LearningResourceType[]>([]);
  const [selectedId, setSelectedId] = useState<string>(
    aliases[preferredConceptId ?? ""] ?? preferredConceptId ?? "evaluation",
  );
  const [recall, setRecall] = useState("");
  const [showHint, setShowHint] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (resourceOverride) {
      setResources([resourceOverride]);
      setSelectedId(resourceOverride.conceptId);
      return;
    }
    fetch("/api/learning-resources", { cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) throw new Error("Không thể tải tài nguyên học.");
        return (await response.json()) as Array<Record<string, unknown>>;
      })
      .then((payload) => {
        const mapped = payload.map(mapResource);
        setResources(mapped);
        setSelectedId((current) =>
          mapped.some((item) => item.conceptId === current)
            ? current
            : (mapped[0]?.conceptId ?? current),
        );
      })
      .catch((reason: Error) => setError(reason.message));
  }, [resourceOverride]);

  useEffect(() => {
    if (!preferredConceptId) return;
    setSelectedId(aliases[preferredConceptId] ?? preferredConceptId);
    setRecall("");
    setShowHint(false);
  }, [preferredConceptId]);

  const selected = useMemo(
    () =>
      resources.find((item) => item.conceptId === selectedId) ?? resources[0],
    [resources, selectedId],
  );

  if (error)
    return (
      <section className="learning-resource-panel glass-surface">
        {error}
      </section>
    );
  if (!selected)
    return (
      <section
        className="learning-resource-panel glass-surface"
        aria-label="Đang tải tài nguyên học"
      >
        Đang tải tài nguyên học…
      </section>
    );

  if (compact) {
    return (
      <section
        className="learning-resource-compact"
        aria-labelledby="lab-learning-title"
      >
        <div>
          <span className="resource-kicker">
            Đọc nhanh trước khi thực hành · {selected.estimatedMinutes} phút
          </span>
          <h3 id="lab-learning-title">{selected.title}</h3>
          <p>{selected.learningOutcome}</p>
        </div>
        <ul className="resource-list">
          {selected.keyIdeas.map((idea) => (
            <li key={idea}>{idea}</li>
          ))}
        </ul>
        <Link
          href={`/sources/${encodeURIComponent(selected.citations[0].sourceSpanId)}`}
        >
          Kiểm chứng source trước khi chạy lab <ArrowSquareOut size={15} />
        </Link>
      </section>
    );
  }

  const recalled = recall.trim().length >= 15;
  return (
    <section
      className="learning-resource-panel glass-surface"
      aria-labelledby="learning-resource-title"
    >
      <div className="resource-heading">
        <div>
          <span className="eyebrow">
            Learning studio · {selected.estimatedMinutes} phút
          </span>
          <h2 id="learning-resource-title">Học để hiểu, rồi mới làm</h2>
        </div>
        <Lightbulb size={25} />
      </div>
      <div
        className="resource-tabs"
        role="tablist"
        aria-label="Chọn concept để học"
      >
        {resources.map((resource) => (
          <button
            type="button"
            role="tab"
            aria-selected={resource.conceptId === selected.conceptId}
            className={
              resource.conceptId === selected.conceptId ? "active" : ""
            }
            key={resource.conceptId}
            onClick={() => {
              setSelectedId(resource.conceptId);
              setRecall("");
              setShowHint(false);
            }}
          >
            {shortTitle(resource.title)}
          </button>
        ))}
      </div>
      <div className="resource-intro">
        <div>
          <span className="resource-kicker">Đang học</span>
          <h3>{selected.title}</h3>
          <p>{selected.whyItMatters}</p>
        </div>
        <div className="resource-outcome">
          <span>Đầu ra</span>
          <strong>{selected.learningOutcome}</strong>
        </div>
      </div>
      <div className="resource-columns">
        <div>
          <h3>Ba ý cần nhớ</h3>
          <ul className="resource-list">
            {selected.keyIdeas.map((idea) => (
              <li key={idea}>{idea}</li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Ví dụ đã giải</h3>
          <ol className="resource-steps">
            {selected.workedExample.map((step) => (
              <li key={step.title}>
                <strong>{step.title}</strong>
                <span>{step.explanation}</span>
                <small>{step.example}</small>
              </li>
            ))}
          </ol>
        </div>
      </div>
      <div className="resource-practice">
        <div>
          <span className="resource-kicker">Tự kiểm tra trước khi làm lab</span>
          <h3>{selected.retrievalPrompt}</h3>
          <textarea
            value={recall}
            onChange={(event) => setRecall(event.target.value)}
            rows={3}
            placeholder="Viết bằng lời của bạn, không chép nguyên văn…"
          />
          <div className="resource-practice-actions">
            <button
              type="button"
              className="button button-secondary"
              onClick={() => setShowHint((current) => !current)}
            >
              {showHint ? "Ẩn gợi ý" : "Xem gợi ý"}
            </button>
            {recalled && (
              <span className="resource-ready">
                <Check size={16} /> Đã có một lần tự nhớ lại
              </span>
            )}
          </div>
          {showHint && (
            <p className="resource-hint">
              Đối chiếu với: {selected.keyIdeas.join(" · ")}
            </p>
          )}
        </div>
        <div className="resource-mistakes">
          <h3>Tránh các lỗi này</h3>
          <ul>
            {selected.commonMistakes.map((mistake) => (
              <li key={mistake}>{mistake}</li>
            ))}
          </ul>
        </div>
      </div>
      <div className="resource-sources">
        <span>Nguồn để kiểm chứng</span>
        {selected.citations.map((citation) => (
          <Link
            href={`/sources/${encodeURIComponent(citation.sourceSpanId)}`}
            key={citation.sourceSpanId}
          >
            {citation.title} · {citation.locator} <ArrowSquareOut size={15} />
          </Link>
        ))}
      </div>
    </section>
  );
}

function mapResource(raw: Record<string, unknown>): LearningResourceType {
  return {
    conceptId: String(raw.concept_id),
    title: String(raw.title),
    whyItMatters: String(raw.why_it_matters),
    estimatedMinutes: Number(raw.estimated_minutes),
    learningOutcome: String(raw.learning_outcome),
    keyIdeas: Array.isArray(raw.key_ideas) ? raw.key_ideas.map(String) : [],
    workedExample: Array.isArray(raw.worked_example)
      ? (raw.worked_example as LearningResourceType["workedExample"])
      : [],
    commonMistakes: Array.isArray(raw.common_mistakes)
      ? raw.common_mistakes.map(String)
      : [],
    retrievalPrompt: String(raw.retrieval_prompt),
    citations: Array.isArray(raw.citations)
      ? raw.citations.map((citation) => {
          const item = citation as Record<string, unknown>;
          return {
            sourceSpanId: String(item.source_span_id),
            title: String(item.title),
            locator: String(item.locator),
            excerpt: String(item.excerpt),
          };
        })
      : [],
  };
}

function shortTitle(title: string) {
  return title.split(":")[0].split("—")[0].trim();
}
