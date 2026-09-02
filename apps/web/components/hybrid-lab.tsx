"use client";

import {
  CheckCircle,
  FloppyDisk,
  Play,
  WarningCircle,
} from "@phosphor-icons/react";
import { useEffect, useMemo, useState } from "react";

type LabState = {
  denseWeight: number;
  sparseWeight: number;
  rerankDepth: number;
  tenantFilter: boolean;
  transferAnswer: string;
};
const initial: LabState = {
  denseWeight: 0.5,
  sparseWeight: 0.5,
  rerankDepth: 20,
  tenantFilter: false,
  transferAnswer: "",
};

export function HybridLab() {
  const [state, setState] = useState(initial);
  const [attemptKey, setAttemptKey] = useState("");
  const [ready, setReady] = useState(false);
  const [result, setResult] = useState<{
    score: number;
    passed: boolean;
    feedback: string[];
    evidence_event_id?: string;
    study_plan?: { id: string } | null;
  } | null>(null);
  const retrievalScore = useMemo(
    () =>
      Math.round(
        58 +
          state.denseWeight * 18 +
          state.sparseWeight * 16 +
          (state.rerankDepth >= 10 && state.rerankDepth <= 40 ? 7 : -8),
      ),
    [state],
  );
  const latency = useMemo(
    () => Math.round(64 + state.rerankDepth * 4.2),
    [state.rerankDepth],
  );

  useEffect(() => {
    const saved = localStorage.getItem("chiron-hybrid-lab");
    if (saved) setState(JSON.parse(saved));
    setAttemptKey(
      localStorage.getItem("chiron-hybrid-lab-attempt") ?? crypto.randomUUID(),
    );
    setReady(true);
  }, []);
  useEffect(() => {
    if (ready) {
      localStorage.setItem("chiron-hybrid-lab", JSON.stringify(state));
      localStorage.setItem("chiron-hybrid-lab-attempt", attemptKey);
    }
  }, [attemptKey, ready, state]);

  async function scoreLab() {
    const response = await fetch("/api/lab", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Idempotency-Key": attemptKey,
      },
      body: JSON.stringify(state),
    });
    setResult(await response.json());
  }

  if (!ready)
    return (
      <div className="lab-skeleton">
        <div />
        <div />
        <div />
      </div>
    );
  return (
    <div className="lab-layout">
      <aside className="lab-brief">
        <span>Brief</span>
        <h2>Phục hồi exact term mà không mất semantic recall.</h2>
        <p>
          Một tenant báo các mã lỗi hiếm không xuất hiện trong top-10. Hãy cấu
          hình pipeline an toàn trong 220 ms.
        </p>
        <h3>Điều kiện đạt</h3>
        <ul>
          <li>Tenant isolation trước retrieval</li>
          <li>Fusion weights hợp lệ</li>
          <li>Rerank depth có kiểm soát</li>
          <li>Giải thích được lựa chọn RRF</li>
        </ul>
      </aside>
      <section className="lab-workspace" aria-labelledby="lab-workspace-title">
        <div className="lab-title">
          <div>
            <span>Pipeline workspace</span>
            <h2 id="lab-workspace-title">Hybrid retrieval</h2>
          </div>
          <span>
            <FloppyDisk size={16} /> Autosaved
          </span>
        </div>
        <div className="pipeline">
          <div>
            <span>Query</span>
            <strong>ERR_CONN_04 timeout</strong>
          </div>
          <i />
          <div>
            <span>Dense + sparse</span>
            <strong>RRF fusion</strong>
          </div>
          <i />
          <div>
            <span>Final stage</span>
            <strong>Rerank top {state.rerankDepth}</strong>
          </div>
        </div>
        <label className="range-control">
          <span>
            Dense weight <strong>{state.denseWeight.toFixed(2)}</strong>
          </span>
          <input
            type="range"
            min="0"
            max="1"
            step="0.05"
            value={state.denseWeight}
            onChange={(event) =>
              setState({ ...state, denseWeight: Number(event.target.value) })
            }
          />
        </label>
        <label className="range-control">
          <span>
            Sparse weight <strong>{state.sparseWeight.toFixed(2)}</strong>
          </span>
          <input
            type="range"
            min="0"
            max="1"
            step="0.05"
            value={state.sparseWeight}
            onChange={(event) =>
              setState({ ...state, sparseWeight: Number(event.target.value) })
            }
          />
        </label>
        <label className="range-control">
          <span>
            Rerank depth <strong>{state.rerankDepth}</strong>
          </span>
          <input
            type="range"
            min="1"
            max="70"
            value={state.rerankDepth}
            onChange={(event) =>
              setState({ ...state, rerankDepth: Number(event.target.value) })
            }
          />
        </label>
        <label className="toggle-control">
          <input
            type="checkbox"
            checked={state.tenantFilter}
            onChange={(event) =>
              setState({ ...state, tenantFilter: event.target.checked })
            }
          />
          <span>Áp dụng tenant filter trước retrieval</span>
        </label>
        <label className="transfer-field">
          <span>Vì sao dùng RRF thay vì cộng raw score?</span>
          <textarea
            rows={4}
            value={state.transferAnswer}
            onChange={(event) =>
              setState({ ...state, transferAnswer: event.target.value })
            }
            placeholder="Giải thích bằng lời của bạn"
          />
        </label>
        <button
          className="button button-primary"
          onClick={scoreLab}
          disabled={state.transferAnswer.trim().length < 12}
        >
          <Play size={17} weight="fill" /> Chạy đánh giá
        </button>
      </section>
      <aside className="lab-metrics">
        <span>Live metrics</span>
        <div className="metric-number">
          <strong>{retrievalScore}</strong>
          <span>Recall proxy</span>
        </div>
        <div className="metric-number">
          <strong>{latency} ms</strong>
          <span>Estimated P95</span>
        </div>
        <div className={`guardrail ${state.tenantFilter ? "safe" : "risk"}`}>
          {state.tenantFilter ? (
            <CheckCircle size={19} />
          ) : (
            <WarningCircle size={19} />
          )}
          <span>
            {state.tenantFilter ? "Tenant scope active" : "Cross-tenant risk"}
          </span>
        </div>
        {result && (
          <div className={`lab-result ${result.passed ? "passed" : "failed"}`}>
            <span>Điểm rubric</span>
            <strong>{result.score}/100</strong>
            {result.feedback.map((item) => (
              <p key={item}>{item}</p>
            ))}
          </div>
        )}
      </aside>
    </div>
  );
}
