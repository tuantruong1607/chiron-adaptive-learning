"use client";

import React from "react";
import { ShieldCheck, ShieldWarning, Sparkle } from "@phosphor-icons/react";

interface HybridSearchVisualizerProps {
  state: Record<string, unknown>;
}

export function HybridSearchVisualizer({ state }: HybridSearchVisualizerProps) {
  const denseWeight = Number(state.dense_weight ?? 0.5);
  const sparseWeight = Number(state.sparse_weight ?? 0.5);
  const rerankDepth = Number(state.rerank_depth ?? 20);
  const tenantFilter = state.tenant_filter === true;

  const recallProxy = Math.min(99, Math.round(55 + denseWeight * 22 + sparseWeight * 18));
  const estimatedLatency = Math.round(45 + rerankDepth * 3.8);
  const precisionProxy = Math.min(98, Math.round(60 + (rerankDepth / 70) * 25 + (tenantFilter ? 10 : 0)));

  // Simulated candidate chunks
  const candidates = [
    {
      id: "chunk-01",
      title: "RAG Pipeline — Section 3: Dense & Sparse Fusion",
      denseScore: (0.88 * denseWeight).toFixed(2),
      sparseScore: (0.92 * sparseWeight).toFixed(2),
      combinedRank: 1,
      locator: "Slide 36 · Page 12",
      isTenantMatch: true,
    },
    {
      id: "chunk-02",
      title: "Vector Store — HNSW Indexing & Precision",
      denseScore: (0.94 * denseWeight).toFixed(2),
      sparseScore: (0.35 * sparseWeight).toFixed(2),
      combinedRank: 2,
      locator: "Slide 22 · Page 8",
      isTenantMatch: true,
    },
    {
      id: "chunk-03",
      title: "Evaluation — Context Recall & Precision Gates",
      denseScore: (0.62 * denseWeight).toFixed(2),
      sparseScore: (0.85 * sparseWeight).toFixed(2),
      combinedRank: 3,
      locator: "Slide 45 · Page 18",
      isTenantMatch: tenantFilter,
    },
  ];

  return (
    <div className="lab-visualizer-card hybrid-visualizer">
      <div className="visualizer-header">
        <div className="title-group">
          <Sparkle size={20} weight="duotone" className="accent-icon" />
          <h4>Mô Phỏng Trực Quan: Hybrid Search & Rank Fusion</h4>
        </div>
        <div className="status-tags">
          {tenantFilter ? (
            <span className="badge badge-success">
              <ShieldCheck size={14} weight="bold" /> Tenant Filter: Active
            </span>
          ) : (
            <span className="badge badge-error">
              <ShieldWarning size={14} weight="bold" /> Rủi ro lộ dữ liệu Tenant
            </span>
          )}
        </div>
      </div>

      {/* Metrics Gauge Row */}
      <div className="metrics-visual-grid">
        <div className="metric-gauge-item">
          <div className="metric-header-row">
            <span>Recall Proxy (Độ bao phủ)</span>
            <strong>{recallProxy}%</strong>
          </div>
          <div className="progress-track">
            <div
              className="progress-fill recall-fill"
              style={{ width: `${recallProxy}%` }}
            />
          </div>
          <small>Dựa trên cân bằng trọng số Dense ({denseWeight}) & Sparse ({sparseWeight})</small>
        </div>

        <div className="metric-gauge-item">
          <div className="metric-header-row">
            <span>Precision Proxy (Độ chính xác)</span>
            <strong>{precisionProxy}%</strong>
          </div>
          <div className="progress-track">
            <div
              className="progress-fill precision-fill"
              style={{ width: `${precisionProxy}%` }}
            />
          </div>
          <small>Tối ưu bởi Rerank Depth ({rerankDepth})</small>
        </div>

        <div className="metric-gauge-item">
          <div className="metric-header-row">
            <span>Ước tính P95 Latency</span>
            <strong className={estimatedLatency > 200 ? "text-danger" : "text-success"}>
              {estimatedLatency} ms
            </strong>
          </div>
          <div className="progress-track">
            <div
              className="progress-fill latency-fill"
              style={{
                width: `${Math.min(100, (estimatedLatency / 300) * 100)}%`,
                backgroundColor: estimatedLatency > 200 ? "var(--danger)" : "var(--accent)",
              }}
            />
          </div>
          <small>Rerank top {rerankDepth} candidates</small>
        </div>
      </div>

      {/* Simulated Results Preview */}
      <div className="candidates-preview-section">
        <h5>Danh sách Chunks trích xuất (Top Candidates sau Fusion & Rerank):</h5>
        <div className="candidate-cards-list">
          {candidates.map((c) => (
            <div key={c.id} className="candidate-card-item">
              <div className="candidate-rank-badge">#{c.combinedRank}</div>
              <div className="candidate-info">
                <div className="candidate-title-row">
                  <strong>{c.title}</strong>
                  <span className="locator-tag">{c.locator}</span>
                </div>
                <div className="candidate-score-bars">
                  <div className="score-mini-bar">
                    <span>Dense Score:</span>
                    <div className="mini-track">
                      <div className="mini-fill dense" style={{ width: `${Math.min(100, Number(c.denseScore) * 100)}%` }} />
                    </div>
                    <span>{c.denseScore}</span>
                  </div>
                  <div className="score-mini-bar">
                    <span>BM25 Score:</span>
                    <div className="mini-track">
                      <div className="mini-fill sparse" style={{ width: `${Math.min(100, Number(c.sparseScore) * 100)}%` }} />
                    </div>
                    <span>{c.sparseScore}</span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
