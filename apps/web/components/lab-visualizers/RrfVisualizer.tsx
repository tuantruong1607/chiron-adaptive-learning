"use client";

import React from "react";
import { ArrowsMerge, Calculator } from "@phosphor-icons/react";

interface RrfVisualizerProps {
  state: Record<string, unknown>;
}

export function RrfVisualizer({ state }: RrfVisualizerProps) {
  const fusion = String(state.fusion ?? "rrf");
  const rrfK = Number(state.rrf_k ?? 60);
  const candidateDepth = Number(state.candidate_depth ?? 50);

  // Sample items with ranks in dense and sparse lists
  const items = [
    { id: "doc-A", title: "Chunk A (RAG Overview)", denseRank: 1, sparseRank: 4 },
    { id: "doc-B", title: "Chunk B (BM25 Keywords)", denseRank: 8, sparseRank: 1 },
    { id: "doc-C", title: "Chunk C (Hybrid Tuning)", denseRank: 2, sparseRank: 3 },
    { id: "doc-D", title: "Chunk D (Evaluation Metrics)", denseRank: 3, sparseRank: 9 },
  ];

  // Calculate RRF score for each item: 1 / (k + rank_dense) + 1 / (k + rank_sparse)
  const calculatedItems = items
    .map((item) => {
      const denseComponent = 1 / (rrfK + item.denseRank);
      const sparseComponent = 1 / (rrfK + item.sparseRank);
      const score = denseComponent + sparseComponent;
      return {
        ...item,
        score,
        denseComponent,
        sparseComponent,
      };
    })
    .sort((a, b) => b.score - a.score);

  return (
    <div className="lab-visualizer-card rrf-visualizer">
      <div className="visualizer-header">
        <div className="title-group">
          <ArrowsMerge size={20} weight="duotone" className="accent-icon" />
          <h4>Mô Phỏng Thuật Toán: Reciprocal Rank Fusion (RRF)</h4>
        </div>
        <div className="status-tags">
          <span className="badge badge-accent">Thuật toán: {fusion.toUpperCase()}</span>
          <span className="badge badge-neutral">Hệ số k = {rrfK}</span>
          <span className="badge badge-neutral">Độ sâu: {candidateDepth}</span>
        </div>
      </div>

      {/* Formula Explanation Bar */}
      <div className="math-formula-box">
        <div className="formula-line">
          <Calculator size={18} weight="duotone" />
          <span>Công thức tính điểm RRF:</span>
          <code>RRF(d) = 1 / (k + rank_dense) + 1 / (k + rank_sparse)</code>
        </div>
        <small>Hệ số k = {rrfK} giúp làm mượt và giảm độ dốc suy giảm điểm số giữa các vị trí rank cao.</small>
      </div>

      {/* Dual Lane Fusion Chart */}
      <div className="dual-lane-chart">
        <div className="lane-column">
          <h5>Rank Dense Retrieval</h5>
          <div className="lane-items">
            {items
              .slice()
              .sort((a, b) => a.denseRank - b.denseRank)
              .map((it) => (
                <div key={it.id} className="lane-item dense-item">
                  <span className="lane-rank">#{it.denseRank}</span>
                  <span className="lane-name">{it.title}</span>
                </div>
              ))}
          </div>
        </div>

        <div className="fusion-center-arrow">
          <div className="fusion-glow-icon">
            <ArrowsMerge size={28} weight="bold" />
          </div>
          <span>Rank Fusion (k={rrfK})</span>
        </div>

        <div className="lane-column">
          <h5>Rank Sparse (BM25)</h5>
          <div className="lane-items">
            {items
              .slice()
              .sort((a, b) => a.sparseRank - b.sparseRank)
              .map((it) => (
                <div key={it.id} className="lane-item sparse-item">
                  <span className="lane-rank">#{it.sparseRank}</span>
                  <span className="lane-name">{it.title}</span>
                </div>
              ))}
          </div>
        </div>
      </div>

      {/* Final Fused Table */}
      <div className="fused-results-table-section">
        <h5>Kết Quả Xếp Hạng Hợp Nhất (Final Fused Ranking):</h5>
        <div className="fused-list">
          {calculatedItems.map((it, idx) => (
            <div key={it.id} className="fused-card-row">
              <div className="final-rank-badge">Top {idx + 1}</div>
              <div className="fused-doc-details">
                <strong>{it.title}</strong>
                <span className="score-breakdown">
                  RRF Score = <strong>{it.score.toFixed(4)}</strong> (Dense: +{it.denseComponent.toFixed(4)} | Sparse: +{it.sparseComponent.toFixed(4)})
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
