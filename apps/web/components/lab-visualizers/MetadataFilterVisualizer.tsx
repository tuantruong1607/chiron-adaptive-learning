"use client";

import React from "react";
import { Funnel, ShieldCheck, ShieldWarning, TreeStructure, Database } from "@phosphor-icons/react";

interface MetadataFilterVisualizerProps {
  state: Record<string, unknown>;
}

export function MetadataFilterVisualizer({ state }: MetadataFilterVisualizerProps) {
  const tenantFilter = state.tenant_filter === true;
  const courseFilter = state.course_filter === true;
  const filterStage = String(state.filter_stage ?? "pre_filter");

  // Search space shrinkage calculation
  const totalCorpus = 5070;
  const tenantCorpus = tenantFilter ? 5070 : totalCorpus;
  const courseCorpus = courseFilter ? 1240 : tenantCorpus;
  const finalCandidates = filterStage === "pre_filter" ? 20 : 100;

  return (
    <div className="lab-visualizer-card filter-visualizer">
      <div className="visualizer-header">
        <div className="title-group">
          <Funnel size={20} weight="duotone" className="accent-icon" />
          <h4>Mô Phỏng Không Gian Tìm Kiếm & Metadata Pre-Filtering</h4>
        </div>
        <div className="status-tags">
          <span className="badge badge-accent">Giai đoạn: {filterStage.toUpperCase()}</span>
          {tenantFilter ? (
            <span className="badge badge-success">
              <ShieldCheck size={14} /> Tenant Shield: Active
            </span>
          ) : (
            <span className="badge badge-error">
              <ShieldWarning size={14} /> Chưa bật Tenant Filter
            </span>
          )}
        </div>
      </div>

      {/* Waterfall Reduction Pipeline */}
      <div className="reduction-pipeline-flow">
        {/* Stage 1 */}
        <div className="pipeline-step-node">
          <div className="node-icon-box">
            <Database size={24} weight="duotone" />
          </div>
          <span className="node-title">1. Toàn bộ Vector DB</span>
          <strong className="node-count">{totalCorpus.toLocaleString()} Chunks</strong>
          <span className="node-desc">Toàn bộ kho dữ liệu</span>
        </div>

        <div className="flow-connector-arrow">➔</div>

        {/* Stage 2 */}
        <div className={`pipeline-step-node ${tenantFilter ? "node-active" : "node-risk"}`}>
          <div className="node-icon-box">
            {tenantFilter ? <ShieldCheck size={24} weight="duotone" /> : <ShieldWarning size={24} weight="duotone" />}
          </div>
          <span className="node-title">2. Tenant Boundary</span>
          <strong className="node-count">{tenantFilter ? "chiron-demo" : "Chưa lọc (Rủi ro)"}</strong>
          <span className="node-desc">{tenantFilter ? "Cô lập theo Token session" : "Có thể lộ dữ liệu"}</span>
        </div>

        <div className="flow-connector-arrow">➔</div>

        {/* Stage 3 */}
        <div className={`pipeline-step-node ${courseFilter ? "node-active" : ""}`}>
          <div className="node-icon-box">
            <TreeStructure size={24} weight="duotone" />
          </div>
          <span className="node-title">3. Course Scope</span>
          <strong className="node-count">{courseFilter ? `${courseCorpus.toLocaleString()} Chunks` : "Toàn Tenant"}</strong>
          <span className="node-desc">{courseFilter ? "Lọc môn rag-intensive" : "Chưa giới hạn môn"}</span>
        </div>

        <div className="flow-connector-arrow">➔</div>

        {/* Stage 4 */}
        <div className="pipeline-step-node node-final">
          <div className="node-icon-box">
            <Funnel size={24} weight="duotone" />
          </div>
          <span className="node-title">4. Tập Candidate</span>
          <strong className="node-count">{finalCandidates} Chunks</strong>
          <span className="node-desc">Đưa vào prompt/reranker</span>
        </div>
      </div>

      {/* Security Analysis Box */}
      <div className="security-insight-box">
        {filterStage === "pre_filter" ? (
          <div className="insight-content success-box">
            <ShieldCheck size={20} weight="fill" className="icon-success" />
            <div>
              <strong>Pre-Filter tại Vector Database:</strong>
              <p>
                Bộ lọc được áp dụng trực tiếp trong lúc duyệt đồ thị ANN. Đảm bảo tốc độ truy vấn cao và không làm thất thoát recall của top-k.
              </p>
            </div>
          </div>
        ) : (
          <div className="insight-content warning-box">
            <ShieldWarning size={20} weight="fill" className="icon-warning" />
            <div>
              <strong>Post-Filter ở Tầng Application:</strong>
              <p>
                Rủi ro cao: Nếu vector DB trả về 20 chunks mà chỉ có 3 chunks thuộc tenant của bạn, top-k sau khi lọc sẽ bị thiếu hụt dữ liệu trầm trọng.
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
