"use client";

import React from "react";
import { Graph, GitFork, CheckCircle } from "@phosphor-icons/react";

interface GraphRoutingVisualizerProps {
  state: Record<string, unknown>;
}

export function GraphRoutingVisualizer({ state }: GraphRoutingVisualizerProps) {
  const maxHops = Number(state.max_hops ?? 2);
  const prerequisiteExpansion = state.prerequisite_expansion !== false;
  const provenanceRequired = state.provenance_required !== false;

  return (
    <div className="lab-visualizer-card graph-visualizer">
      <div className="visualizer-header">
        <div className="title-group">
          <Graph size={20} weight="duotone" className="accent-icon" />
          <h4>Mô Phỏng Đồ Thị Khái Niệm: Graph-lite Routing (1–2 Hops)</h4>
        </div>
        <div className="status-tags">
          <span className="badge badge-accent">Giới hạn: {maxHops} Hops</span>
          {prerequisiteExpansion && (
            <span className="badge badge-success">
              <CheckCircle size={14} /> Mở rộng Prerequisite DAG
            </span>
          )}
          {provenanceRequired && (
            <span className="badge badge-neutral">100% Provenance có Source</span>
          )}
        </div>
      </div>

      {/* Interactive mini graph canvas */}
      <div className="mini-graph-container">
        <div className="graph-nodes-flex">
          {/* Hop 0: Entry Point */}
          <div className="hop-column">
            <span className="hop-col-title">Query Concept (Hop 0)</span>
            <div className="node-pill entry-node">
              <span className="node-dot" />
              <strong>Chunking Strategy</strong>
              <small>Anchor node</small>
            </div>
          </div>

          <div className="hop-arrow">➔ (Hop 1)</div>

          {/* Hop 1 Nodes */}
          <div className="hop-column">
            <span className="hop-col-title">Quan Hệ Trực Tiếp (Hop 1)</span>
            <div className="nodes-stack">
              <div className="node-pill active-node">
                <span className="node-dot" />
                <strong>Vector Embedding</strong>
                <small>PREREQUISITE_OF</small>
              </div>
              <div className="node-pill active-node">
                <span className="node-dot" />
                <strong>Dense Retrieval</strong>
                <small>APPLIES_TO</small>
              </div>
            </div>
          </div>

          <div className="hop-arrow">➔ (Hop 2)</div>

          {/* Hop 2 Nodes */}
          <div className="hop-column">
            <span className="hop-col-title">Quan Hệ Mở Rộng (Hop 2)</span>
            <div className="nodes-stack">
              <div className={`node-pill ${maxHops >= 2 ? "active-node" : "disabled-node"}`}>
                <span className="node-dot" />
                <strong>RRF Fusion</strong>
                <small>{maxHops >= 2 ? "PART_OF (Active)" : "Pruned (Giới hạn hop)"}</small>
              </div>
              <div className={`node-pill ${maxHops >= 2 ? "active-node" : "disabled-node"}`}>
                <span className="node-dot" />
                <strong>Cross-Encoder Rerank</strong>
                <small>{maxHops >= 2 ? "PREREQUISITE_OF" : "Pruned (Giới hạn hop)"}</small>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Safety DAG Insight */}
      <div className="graph-safety-box">
        <GitFork size={20} weight="duotone" className="accent-icon" />
        <div>
          <strong>Bảo đảm Đồ thị Không Chu trình (Cycle-Free DAG):</strong>
          <p>
            Các quan hệ `PREREQUISITE_OF` được xác thực bằng giải thuật topological sort trước khi nạp vào runtime.
            Thuật toán chỉ mở rộng tối đa <strong>{maxHops} hop</strong> để tránh hiện tượng bùng nổ ngữ cảnh (context explosion).
          </p>
        </div>
      </div>
    </div>
  );
}
