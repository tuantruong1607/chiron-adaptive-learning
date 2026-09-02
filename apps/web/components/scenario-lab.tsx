"use client";

import {
  CheckCircle,
  FloppyDisk,
  Play,
  WarningCircle,
} from "@phosphor-icons/react";
import Link from "next/link";
import type { LearningResource as LearningResourceType } from "@chiron/domain";
import React, { useEffect, useMemo, useState } from "react";
import { LearningResourceRail } from "./learning-resource";
import { LabVisualizer } from "./lab-visualizers";

type Value = boolean | number | string;
type Control = {
  id: string;
  label: string;
  kind: "range" | "toggle" | "select";
  defaultValue: Value;
  minimum?: number | null;
  maximum?: number | null;
  step?: number | null;
  options: Array<{ value: string; label: string }>;
  helpText: string;
};
type TransferPrompt = {
  id: string;
  prompt: string;
  placeholder: string;
  minLength: number;
};
type Lab = {
  id: string;
  title: string;
  objective: string;
  brief: string;
  estimatedMinutes: number;
  successThreshold: number;
  conceptId: string;
  sourceSpanIds: string[];
  scenario: string;
  learningResourceId?: string | null;
  learningResource?: LearningResourceType | null;
  controls: Control[];
  transferPrompts: TransferPrompt[];
};
type LabResult = {
  score: number;
  passed: boolean;
  feedback: string[];
  evidence_event_id: string;
  mastery_update?: {
    previous: number | null;
    current: number;
    concept_id: string;
  } | null;
  study_plan?: { id: string; planner_version: string } | null;
};

function liveMetrics(labId: string, state: Record<string, Value>) {
  const number = (key: string) => Number(state[key] ?? 0);
  const enabled = (key: string) => state[key] === true;
  switch (labId) {
    case "hybrid-search":
      return [
        [
          "Recall proxy",
          Math.round(
            58 + number("dense_weight") * 18 + number("sparse_weight") * 16,
          ),
        ],
        [
          "Estimated P95",
          `${Math.round(64 + number("rerank_depth") * 4.2)} ms`,
        ],
        ["Isolation", enabled("tenant_filter") ? "Active" : "Risk"],
      ];
    case "chunking-strategy":
      return [
        ["Strategy", state.strategy],
        ["Context window", `${number("chunk_size")} tokens`],
        ["Locator", enabled("preserve_locators") ? "Preserved" : "Lost"],
      ];
    case "rrf-ranking":
      return [
        ["Fusion", state.fusion],
        ["RRF k", number("rrf_k")],
        ["Candidates", number("candidate_depth")],
      ];
    case "metadata-filtering":
      return [
        ["Tenant scope", enabled("tenant_filter") ? "Active" : "Risk"],
        ["Course scope", enabled("course_filter") ? "Active" : "Missing"],
        ["Stage", state.filter_stage],
      ];
    case "rag-evaluation":
      return [
        ["Faithfulness", number("faithfulness_gate").toFixed(2)],
        ["Context recall", number("context_recall_gate").toFixed(2)],
        ["Regression", enabled("persist_regression") ? "Versioned" : "Missing"],
      ];
    default:
      return [
        ["Routing", state.routing],
        ["Max hops", number("max_hops")],
        ["Expansion", number("expansion_limit")],
      ];
  }
}

export function ScenarioLab({ labId }: { labId: string }) {
  const [lab, setLab] = useState<Lab | null>(null);
  const [state, setState] = useState<Record<string, Value>>({});
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [attemptKey, setAttemptKey] = useState("");
  const [result, setResult] = useState<LabResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    fetch("/api/labs", { cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) throw new Error("Không thể tải lab definition.");
        const labs = (await response.json()) as Lab[];
        const selected = labs.find((item) => item.id === labId);
        if (!selected) throw new Error("Lab không tồn tại.");
        const saved = window.localStorage.getItem(`chiron-lab:${labId}`);
        const defaults = Object.fromEntries(
          selected.controls.map((control) => [
            control.id,
            control.defaultValue,
          ]),
        );
        if (saved) {
          const parsed = JSON.parse(saved) as {
            state?: Record<string, Value>;
            answers?: Record<string, string>;
            attemptKey?: string;
          };
          setState({ ...defaults, ...parsed.state });
          setAnswers(parsed.answers ?? {});
          setAttemptKey(parsed.attemptKey ?? crypto.randomUUID());
        } else {
          setState(defaults);
          setAttemptKey(crypto.randomUUID());
        }
        setLab(selected);
      })
      .catch((reason: Error) => setError(reason.message));
  }, [labId]);

  useEffect(() => {
    if (lab && attemptKey) {
      window.localStorage.setItem(
        `chiron-lab:${labId}`,
        JSON.stringify({ state, answers, attemptKey }),
      );
    }
  }, [answers, attemptKey, lab, labId, state]);

  const metrics = useMemo(() => liveMetrics(labId, state), [labId, state]);
  const readyToSubmit =
    lab?.transferPrompts.every(
      (prompt) => (answers[prompt.id] ?? "").trim().length >= prompt.minLength,
    ) ?? false;

  async function submit() {
    setSubmitting(true);
    setError(null);
    try {
      const response = await fetch(
        `/api/labs/${encodeURIComponent(labId)}/submit`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Idempotency-Key": attemptKey,
          },
          body: JSON.stringify({
            configuration: state,
            transfer_answers: answers,
          }),
        },
      );
      const payload = await response.json();
      if (!response.ok)
        throw new Error(
          payload.detail ?? payload.error ?? "Không thể chấm lab.",
        );
      setResult(payload as LabResult);
    } catch (reason) {
      setError(
        reason instanceof Error ? reason.message : "Không thể chấm lab.",
      );
    } finally {
      setSubmitting(false);
    }
  }

  if (error && !lab)
    return <div className="glass-surface catalog-state">{error}</div>;
  if (!lab)
    return (
      <div className="lab-skeleton">
        <div />
        <div />
        <div />
      </div>
    );

  return (
    <div className="lab-layout scenario-lab-layout">
      <aside className="lab-brief">
        <span>Brief</span>
        <h2>{lab.objective}</h2>
        <p>{lab.scenario}</p>
        <h3>Evidence grounding</h3>
        <div className="lab-source-links">
          {lab.sourceSpanIds.map((source) => (
            <Link key={source} href={`/sources/${source}`}>
              Mở source locator
            </Link>
          ))}
        </div>
      </aside>
      <section className="lab-workspace" aria-labelledby="lab-workspace-title">
        <div className="lab-title">
          <div>
            <span>Scenario workspace</span>
            <h2 id="lab-workspace-title">{lab.title}</h2>
          </div>
          <span>
            <FloppyDisk size={16} /> Autosaved
          </span>
        </div>
        <p className="lab-scenario-copy">{lab.brief}</p>
        
        {/* Dynamic Interactive Lab Visualizer */}
        <LabVisualizer labId={labId} state={state} />

        {lab.learningResource && (
          <LearningResourceRail
            preferredConceptId={lab.learningResourceId ?? lab.conceptId}
            resourceOverride={lab.learningResource}
            compact
          />
        )}
        <div className="scenario-controls">
          {lab.controls.map((control) =>
            control.kind === "range" ? (
              <label className="range-control" key={control.id}>
                <span>
                  {control.label}{" "}
                  <strong>
                    {Number(state[control.id] ?? 0).toFixed(
                      (control.step ?? 1) < 1 ? 2 : 0,
                    )}
                  </strong>
                </span>
                <input
                  type="range"
                  min={control.minimum ?? 0}
                  max={control.maximum ?? 100}
                  step={control.step ?? 1}
                  value={Number(state[control.id] ?? 0)}
                  onChange={(event) =>
                    setState({
                      ...state,
                      [control.id]: Number(event.target.value),
                    })
                  }
                />
                <small>{control.helpText}</small>
              </label>
            ) : control.kind === "toggle" ? (
              <label className="toggle-control" key={control.id}>
                <input
                  type="checkbox"
                  checked={state[control.id] === true}
                  onChange={(event) =>
                    setState({ ...state, [control.id]: event.target.checked })
                  }
                />
                <span>
                  <strong>{control.label}</strong>
                  <small>{control.helpText}</small>
                </span>
              </label>
            ) : (
              <label className="select-control" key={control.id}>
                <span>{control.label}</span>
                <select
                  value={String(state[control.id] ?? control.defaultValue)}
                  onChange={(event) =>
                    setState({ ...state, [control.id]: event.target.value })
                  }
                >
                  {control.options.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </select>
                <small>{control.helpText}</small>
              </label>
            ),
          )}
        </div>
        <div className="transfer-prompts">
          {lab.transferPrompts.map((prompt) => (
            <label className="transfer-field" key={prompt.id}>
              <span>{prompt.prompt}</span>
              <textarea
                rows={4}
                value={answers[prompt.id] ?? ""}
                onChange={(event) =>
                  setAnswers({ ...answers, [prompt.id]: event.target.value })
                }
                placeholder={prompt.placeholder}
              />
            </label>
          ))}
        </div>
        <button
          className="button button-primary"
          type="button"
          onClick={() => void submit()}
          disabled={!readyToSubmit || submitting}
        >
          <Play size={17} weight="fill" />{" "}
          {submitting ? "Đang đánh giá…" : "Chạy đánh giá"}
        </button>
        {error && <p className="form-error">{error}</p>}
      </section>
      <aside className="lab-metrics">
        <span>Live metrics</span>
        {metrics.map(([label, value]) => (
          <div className="metric-number" key={String(label)}>
            <strong>{String(value)}</strong>
            <span>{String(label)}</span>
          </div>
        ))}
        <div className={`guardrail ${readyToSubmit ? "safe" : "risk"}`}>
          {readyToSubmit ? (
            <CheckCircle size={19} />
          ) : (
            <WarningCircle size={19} />
          )}
          <span>
            {readyToSubmit
              ? "Transfer checks ready"
              : "Complete transfer checks"}
          </span>
        </div>
        {result && (
          <div className={`lab-result ${result.passed ? "passed" : "failed"}`}>
            <span>Điểm rubric</span>
            <strong>{result.score}/100</strong>
            {result.feedback.map((item) => (
              <p key={item}>{item}</p>
            ))}
            {result.mastery_update && (
              <p>
                Mastery:{" "}
                {Math.round((result.mastery_update.previous ?? 0) * 100)}% →{" "}
                {Math.round(result.mastery_update.current * 100)}%
              </p>
            )}
            {result.study_plan && (
              <p>
                Study plan đã được cập nhật bằng{" "}
                {result.study_plan.planner_version}.
              </p>
            )}
          </div>
        )}
      </aside>
    </div>
  );
}
