"use client";

import React from "react";
import { HybridSearchVisualizer } from "./HybridSearchVisualizer";
import { ChunkingVisualizer } from "./ChunkingVisualizer";
import { RrfVisualizer } from "./RrfVisualizer";
import { MetadataFilterVisualizer } from "./MetadataFilterVisualizer";
import { RagEvaluationVisualizer } from "./RagEvaluationVisualizer";
import { GraphRoutingVisualizer } from "./GraphRoutingVisualizer";

interface LabVisualizerProps {
  labId: string;
  state: Record<string, unknown>;
}

export function LabVisualizer({ labId, state }: LabVisualizerProps) {
  switch (labId) {
    case "hybrid-search":
      return <HybridSearchVisualizer state={state} />;
    case "chunking-strategy":
      return <ChunkingVisualizer state={state} />;
    case "rrf-ranking":
      return <RrfVisualizer state={state} />;
    case "metadata-filtering":
      return <MetadataFilterVisualizer state={state} />;
    case "rag-evaluation":
      return <RagEvaluationVisualizer state={state} />;
    case "graph-lite-routing":
      return <GraphRoutingVisualizer state={state} />;
    default:
      return <HybridSearchVisualizer state={state} />;
  }
}

export {
  HybridSearchVisualizer,
  ChunkingVisualizer,
  RrfVisualizer,
  MetadataFilterVisualizer,
  RagEvaluationVisualizer,
  GraphRoutingVisualizer,
};
