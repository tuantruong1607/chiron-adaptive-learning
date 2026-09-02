"use client";

import React from "react";
import { CheckCircle, WarningCircle, Stack } from "@phosphor-icons/react";

interface ChunkingVisualizerProps {
  state: Record<string, unknown>;
}

export function ChunkingVisualizer({ state }: ChunkingVisualizerProps) {
  const strategy = String(state.strategy ?? "hierarchical");
  const chunkSize = Number(state.chunk_size ?? 500);
  const overlap = Number(state.overlap ?? 50);
  const preserveLocators = state.preserve_locators !== false;

  const maxModelLimit = 512;
  const isOverflow = chunkSize > maxModelLimit;
  const overlapPercent = Math.round((overlap / chunkSize) * 100);

  return (
    <div className="lab-visualizer-card chunking-visualizer">
      <div className="visualizer-header">
        <div className="title-group">
          <Stack size={20} weight="duotone" className="accent-icon" />
          <h4>Mô Phỏng Phân Đoạn Tài Liệu: Parent-Child Chunking</h4>
        </div>
        <div className="status-tags">
          <span className="badge badge-accent">Chiến lược: {strategy.toUpperCase()}</span>
          {preserveLocators ? (
            <span className="badge badge-success">
              <CheckCircle size={14} /> Giữ nguyên Source Locators
            </span>
          ) : (
            <span className="badge badge-error">
              <WarningCircle size={14} /> Mất liên kết Heading/Page
            </span>
          )}
        </div>
      </div>

      {/* Token Budget Gauge */}
      <div className="token-budget-bar-section">
        <div className="token-header-row">
          <span>Kích thước Chunk mục tiêu: <strong>{chunkSize} tokens</strong> (Overlap: {overlap} tokens / {overlapPercent}%)</span>
          <span className={isOverflow ? "text-danger" : "text-success"}>
            Giới hạn Model E5: 512 tokens
          </span>
        </div>
        <div className="token-track">
          <div
            className={`token-fill ${isOverflow ? "overflow-danger" : "normal-fill"}`}
            style={{ width: `${Math.min(100, (chunkSize / 1000) * 100)}%` }}
          />
          <div className="limit-marker" style={{ left: "51.2%" }}>
            <span className="marker-label">512 token limit</span>
          </div>
        </div>
        {isOverflow && (
          <p className="warning-note">
            ⚠️ Cảnh báo: Chunk dài hơn 512 tokens sẽ bị mô hình Embedding cắt bớt phần đuôi (truncation), gây mất mát thông tin.
          </p>
        )}
      </div>

      {/* Visual Hierarchy Tree */}
      <div className="chunk-hierarchy-preview">
        <h5>Cấu trúc Phân Tầng Phân Đoạn (Parent-Child Hierarchy):</h5>
        
        {/* Parent Block */}
        <div className="parent-chunk-box">
          <div className="parent-chunk-header">
            <span className="badge badge-parent">Parent Chunk #1024</span>
            <span className="parent-meta">Phạm vi: Toàn bộ Section 4.2 · 850 tokens</span>
            {preserveLocators && <span className="locator-badge">Source: `docs/retrieval.md:L45-L120`</span>}
          </div>
          <p className="parent-summary-text">
            &quot;Parent chunk lưu trữ toàn vẹn ngữ cảnh của chương, được trả về cho LLM khi cần mở rộng ngữ cảnh câu trả lời...&quot;
          </p>

          {/* Child Chunks Grid */}
          <div className="child-chunks-grid">
            <div className="child-chunk-card">
              <div className="child-header">
                <strong>Child Chunk #1024.1</strong>
                <span className="token-tag">~{chunkSize} tokens</span>
              </div>
              <p className="child-text">
                &quot;Khái niệm Dense Retrieval và cách thức ánh xạ token sang không gian vector...&quot;
              </p>
              <div className="overlap-band">
                <span>Vùng Overlap ({overlap} tokens) ⇄</span>
              </div>
            </div>

            <div className="child-chunk-card">
              <div className="child-header">
                <strong>Child Chunk #1024.2</strong>
                <span className="token-tag">~{chunkSize} tokens</span>
              </div>
              <p className="child-text">
                &quot;...so sánh hiệu năng giữa mô hình BM25 truyền thống và các phương pháp Hybrid Fusion...&quot;
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
