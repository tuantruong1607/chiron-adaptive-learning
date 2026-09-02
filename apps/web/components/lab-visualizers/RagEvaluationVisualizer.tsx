"use client";

import React from "react";
import { ChartPolar, CheckCircle, WarningCircle, Sparkle } from "@phosphor-icons/react";

interface RagEvaluationVisualizerProps {
  state: Record<string, unknown>;
}

export function RagEvaluationVisualizer({ state }: RagEvaluationVisualizerProps) {
  const faithfulnessGate = Number(state.faithfulness_gate ?? 0.85);
  const contextRecallGate = Number(state.context_recall_gate ?? 0.80);
  const sampleSize = Number(state.sample_size ?? 50);
  const persistRegression = state.persist_regression !== false;

  // Simulated metrics based on thresholds
  const metrics = [
    {
      name: "Faithfulness (Độ trung thực)",
      target: faithfulnessGate,
      current: 0.92,
      passed: 0.92 >= faithfulnessGate,
      desc: "Tỷ lệ khẳng định có bằng chứng kiểm chứng trong context",
    },
    {
      name: "Context Recall (Độ bao phủ)",
      target: contextRecallGate,
      current: 0.84,
      passed: 0.84 >= contextRecallGate,
      desc: "Tỷ lệ thông tin ground-truth được tìm thấy trong context",
    },
    {
      name: "Context Precision (Độ chính xác rank)",
      target: 0.75,
      current: 0.88,
      passed: 0.88 >= 0.75,
      desc: "Mức độ ưu tiên đưa chunks liên quan lên vị trí đầu",
    },
    {
      name: "Answer Relevancy (Bám sát câu hỏi)",
      target: 0.80,
      current: 0.89,
      passed: 0.89 >= 0.80,
      desc: "Mức độ trực diện và đúng trọng tâm của câu trả lời",
    },
  ];

  const allPassed = metrics.every((m) => m.passed);

  return (
    <div className="lab-visualizer-card rag-eval-visualizer">
      <div className="visualizer-header">
        <div className="title-group">
          <ChartPolar size={20} weight="duotone" className="accent-icon" />
          <h4>Bảng Điều Khiển Chất Lượng RAGAS: 4 Trục Chỉ Số Cốt Lõi</h4>
        </div>
        <div className="status-tags">
          <span className="badge badge-neutral">Mẫu: {sampleSize} câu</span>
          {allPassed ? (
            <span className="badge badge-success">
              <CheckCircle size={14} /> Quality Gate: PASS
            </span>
          ) : (
            <span className="badge badge-error">
              <WarningCircle size={14} /> Quality Gate: FAIL
            </span>
          )}
        </div>
      </div>

      {/* Metric Bars Grid */}
      <div className="ragas-metrics-grid">
        {metrics.map((m) => (
          <div key={m.name} className={`ragas-metric-card ${m.passed ? "metric-pass" : "metric-fail"}`}>
            <div className="metric-top-row">
              <strong>{m.name}</strong>
              <div className="score-badge">
                <span className="current-val">{m.current.toFixed(2)}</span>
                <span className="target-val">/ Ngưỡng: {m.target.toFixed(2)}</span>
              </div>
            </div>

            <div className="metric-bar-track">
              <div
                className="metric-bar-fill"
                style={{
                  width: `${m.current * 100}%`,
                  backgroundColor: m.passed ? "var(--secure)" : "var(--danger)",
                }}
              />
              <div
                className="threshold-line"
                style={{ left: `${m.target * 100}%` }}
                title={`Ngưỡng: ${m.target}`}
              />
            </div>

            <div className="metric-bottom-row">
              <span className="metric-desc">{m.desc}</span>
              <span className="metric-status-tag">
                {m.passed ? "✓ Đạt chuẩn" : "✗ Dưới ngưỡng"}
              </span>
            </div>
          </div>
        ))}
      </div>

      {/* Regression Check Notice */}
      <div className="regression-notice-box">
        <Sparkle size={20} weight="duotone" className="accent-icon" />
        <div>
          <strong>Chính sách lưu vết phiên bản (Regression Persistence):</strong>
          <p>
            {persistRegression
              ? "Đang lưu trữ artifact đánh giá vào bảng `eval_runs` trong PostgreSQL để so sánh độ lệch (drift) qua các lần release."
              : "Cảnh báo: Chưa bật lưu trữ regression artifact. Dữ liệu đánh giá sẽ bị mất khi restart container."}
          </p>
        </div>
      </div>
    </div>
  );
}
