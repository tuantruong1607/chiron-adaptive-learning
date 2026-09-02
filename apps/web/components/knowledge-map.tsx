"use client";

import {
  ArrowRight,
  ArrowSquareOut,
  Funnel,
  MagnifyingGlass,
  X,
} from "@phosphor-icons/react";
import type {
  ConceptEdge,
  ConceptNode,
  KnowledgeMap,
  MasteryBand,
  RelationType,
} from "@chiron/domain";
import { AnimatePresence, motion, useReducedMotion } from "motion/react";
import Link from "next/link";
import React, { useEffect, useMemo, useRef, useState } from "react";

const filterLabels: Record<"all" | MasteryBand, string> = {
  all: "Tất cả",
  new: "Mới",
  developing: "Đang phát triển",
  secure: "Vững",
  mastered: "Thành thạo",
};

const relationLabels: Record<RelationType, string> = {
  prerequisite_of: "Tiên quyết",
  part_of: "Thuộc về",
  contrasts_with: "Đối chiếu",
  applies_to: "Áp dụng vào",
  causes: "Dẫn đến",
};

const relationOrder: RelationType[] = [
  "prerequisite_of",
  "applies_to",
  "part_of",
  "contrasts_with",
  "causes",
];

type KnowledgeDomain =
  | "foundations_product"
  | "data_retrieval"
  | "agents_orchestration"
  | "memory_graph"
  | "safety_governance"
  | "deployment_operations"
  | "evaluation"
  | "fine_tuning_alignment"
  | "production_architecture";

const knowledgeDomains: Array<{
  id: KnowledgeDomain;
  label: string;
  description: string;
  stages: [string, string, string, string];
  concepts: Set<string>;
}> = [
  {
    id: "foundations_product",
    label: "Nền tảng & SP",
    description: "AI/LLM, prompting, tool calling, problem framing và delivery.",
    stages: ["1. Nền tảng & Bài toán", "2. Prompting & Tạo văn bản", "3. Tool calling & Reasoning", "4. Sản phẩm & Delivery"],
    concepts: new Set([
      "ai_llm_foundations",
      "transformer_generation",
      "prompt_engineering",
      "tool_calling",
      "react_reasoning",
      "ai_problem_framing",
      "ai_product_delivery",
    ]),
  },
  {
    id: "data_retrieval",
    label: "Dữ liệu & RAG",
    description: "Data pipeline, chunking, embedding, hybrid retrieval và filtering.",
    stages: ["1. Nguồn & Data Pipeline", "2. Chunking & Embeddings", "3. Tìm kiếm & Lọc", "4. Hybrid & RAG Pipeline"],
    concepts: new Set([
      "data_foundations",
      "data_pipeline",
      "etl_elt",
      "change_data_capture",
      "dead_letter_queue",
      "pipeline_idempotency",
      "rag_pipeline",
      "chunking",
      "embeddings",
      "vector_database",
      "dense_retrieval",
      "sparse_retrieval",
      "hybrid_search_rrf",
      "reranking_mmr",
      "metadata_filtered_search",
    ]),
  },
  {
    id: "agents_orchestration",
    label: "Agent & điều phối",
    description: "State, retry, HITL, multi-agent, MCP/A2A và quyền công cụ.",
    stages: ["1. Kiến trúc & Giao thức", "2. Runtime & OAuth", "3. Phân quyền & Điều phối", "4. Bền vững & Idempotency"],
    concepts: new Set([
      "agent_architecture",
      "agent_idempotency",
      "durable_execution",
      "human_in_loop",
      "multi_agent_systems",
      "supervisor_routing",
      "mcp_a2a",
      "mcp_oauth",
      "tool_permissions",
      "framework_runtime_session",
    ]),
  },
  {
    id: "memory_graph",
    label: "Memory & Graph",
    description: "Memory agent, self-improvement, knowledge graph và multi-hop.",
    stages: ["1. Cơ chế Bộ nhớ & Graph", "2. Short-term & Episodic", "3. Semantic & GraphRAG", "4. Tự củng cố & Nâng cấp"],
    concepts: new Set([
      "agent_memory",
      "short_term_memory",
      "episodic_memory",
      "semantic_memory",
      "memory_consolidation",
      "self_improving_agents",
      "knowledge_graph",
      "graphrag_multi_hop",
    ]),
  },
  {
    id: "safety_governance",
    label: "An toàn",
    description: "Calibration, injection, OWASP, PII, guardrails và governance.",
    stages: ["1. Rủi ro & OWASP", "2. Prompt Injection & PII", "3. Guardrails & Audit", "4. Fallback & Governance"],
    concepts: new Set([
      "confidence_calibration",
      "retrieval_prompt_injection",
      "owasp_llm_security",
      "pii_governance",
      "guardrails",
      "fallback_governance",
      "audit_retention_redaction",
    ]),
  },
  {
    id: "deployment_operations",
    label: "Vận hành",
    description: "Deploy, health, observability, SLO, incident và resilience.",
    stages: ["1. CI/CD & Health Probes", "2. Observability & Cache", "3. SLI/SLO & Circuit Breaker", "4. Chẩn đoán & Fallback"],
    concepts: new Set([
      "deployment_pipeline",
      "health_probes",
      "observability",
      "sli_slo",
      "incident_diagnosis",
      "circuit_breaker",
      "fallback_policy",
      "semantic_cache",
    ]),
  },
  {
    id: "evaluation",
    label: "Đánh giá AI",
    description: "Eval design, metrics, grounding, golden set và LLM-as-a-Judge.",
    stages: ["1. Thiết kế Eval & Golden set", "2. Online/Offline & Metrics", "3. Grounding & Relevancy", "4. RAG Eval & LLM Judge"],
    concepts: new Set([
      "ai_evaluation",
      "online_offline_evaluation",
      "error_types_metrics",
      "context_precision_recall",
      "faithfulness_grounding",
      "answer_relevancy",
      "golden_dataset",
      "llm_as_judge",
      "rag_evaluation",
    ]),
  },
  {
    id: "fine_tuning_alignment",
    label: "Fine-tuning",
    description: "Fine-tuning, LoRA/QLoRA, SFT và preference alignment.",
    stages: ["1. Mục tiêu Fine-tuning", "2. LoRA / QLoRA & SFT", "3. Preference Alignment & DPO", "4. SimPO & KTO"],
    concepts: new Set([
      "model_fine_tuning",
      "lora_qlora",
      "supervised_fine_tuning",
      "preference_alignment",
      "dpo_orpo",
      "simpo_kto",
    ]),
  },
  {
    id: "production_architecture",
    label: "Kiến trúc",
    description: "Nondeterminism, retrieval routing và reliability production.",
    stages: ["1. Nondeterminism", "2. Router & Điều hướng", "3. Production Reliability", "4. Tối ưu Hệ thống"],
    concepts: new Set([
      "nondeterminism",
      "retrieval_router",
      "production_reliability",
    ]),
  },
];

const domainStageMap: Record<string, string[][]> = {
  foundations_product: [
    ["ai_llm_foundations", "ai_problem_framing"],
    ["transformer_generation", "prompt_engineering"],
    ["tool_calling", "react_reasoning"],
    ["ai_product_delivery"],
  ],
  data_retrieval: [
    ["data_foundations", "chunking", "metadata_filtered_search"],
    ["data_pipeline", "embeddings", "vector_database"],
    ["etl_elt", "change_data_capture", "dead_letter_queue", "dense_retrieval", "sparse_retrieval", "pipeline_idempotency"],
    ["hybrid_search_rrf", "reranking_mmr", "rag_pipeline"],
  ],
  agents_orchestration: [
    ["agent_architecture", "mcp_a2a"],
    ["framework_runtime_session", "mcp_oauth", "durable_execution", "multi_agent_systems"],
    ["tool_permissions", "human_in_loop", "supervisor_routing"],
    ["agent_idempotency"],
  ],
  memory_graph: [
    ["agent_memory", "knowledge_graph"],
    ["short_term_memory", "episodic_memory"],
    ["semantic_memory", "graphrag_multi_hop"],
    ["memory_consolidation", "self_improving_agents"],
  ],
  safety_governance: [
    ["confidence_calibration", "owasp_llm_security", "retrieval_prompt_injection", "pii_governance"],
    ["guardrails", "audit_retention_redaction"],
    ["fallback_governance"],
  ],
  deployment_operations: [
    ["deployment_pipeline", "semantic_cache"],
    ["health_probes", "observability", "circuit_breaker", "fallback_policy"],
    ["sli_slo", "incident_diagnosis"],
  ],
  evaluation: [
    ["golden_dataset", "error_types_metrics", "context_precision_recall", "faithfulness_grounding", "answer_relevancy"],
    ["ai_evaluation", "rag_evaluation"],
    ["online_offline_evaluation", "llm_as_judge"],
  ],
  fine_tuning_alignment: [
    ["model_fine_tuning"],
    ["supervised_fine_tuning", "lora_qlora"],
    ["preference_alignment", "dpo_orpo"],
    ["simpo_kto"],
  ],
  production_architecture: [
    ["nondeterminism"],
    ["retrieval_router"],
    ["production_reliability"],
  ],
};

function domainForConcept(conceptId: string): KnowledgeDomain {
  return (
    knowledgeDomains.find((domain) => domain.concepts.has(conceptId))?.id ??
    "foundations_product"
  );
}

function layoutVisibleNodes(
  nodes: ConceptNode[],
  edges: ConceptEdge[],
  domainId?: KnowledgeDomain,
  searchQuery = "",
  forceLayout = false,
): ConceptNode[] {
  if (!forceLayout && nodes.length <= 1) return nodes;

  const nodeMap = new Map(nodes.map((n) => [n.id, n]));
  const visibleIds = new Set(nodes.map((n) => n.id));

  // If viewing a full domain without search query, use structured domain stages for cleanest flow
  if (domainId && domainStageMap[domainId] && !searchQuery.trim()) {
    const stageDefs = domainStageMap[domainId];
    const colX = [14, 38, 62, 86];
    const result: ConceptNode[] = [];

    stageDefs.forEach((stageConcepts, colIdx) => {
      const colNodes = stageConcepts
        .map((id) => nodeMap.get(id))
        .filter((n): n is ConceptNode => Boolean(n));

      const count = colNodes.length;
      colNodes.forEach((node, rowIdx) => {
        const x = colX[colIdx];
        const minY = 16;
        const maxY = 72;
        const y = count === 1 ? 44 : minY + (rowIdx * (maxY - minY)) / Math.max(count - 1, 1);
        result.push({ ...node, x, y });
      });
    });

    // Handle any extra nodes not in preset stage list
    const placedIds = new Set(result.map((n) => n.id));
    nodes.forEach((n) => {
      if (!placedIds.has(n.id)) {
        result.push({ ...n, x: 50, y: 44 });
      }
    });

    return result;
  }

  // Fallback / Dynamic DAG topological layering
  const relevantEdges = edges.filter(
    (e) => visibleIds.has(e.source) && visibleIds.has(e.target),
  );

  const inEdges = new Map<string, string[]>();
  nodes.forEach((n) => inEdges.set(n.id, []));

  relevantEdges.forEach((e) => {
    inEdges.get(e.target)?.push(e.source);
  });

  const memoDepth = new Map<string, number>();
  function getDepth(nodeId: string, visited: Set<string>): number {
    if (memoDepth.has(nodeId)) return memoDepth.get(nodeId)!;
    if (visited.has(nodeId)) return 0;
    visited.add(nodeId);

    const parents = inEdges.get(nodeId) ?? [];
    if (parents.length === 0) {
      memoDepth.set(nodeId, 0);
      return 0;
    }

    let maxP = 0;
    for (const p of parents) {
      maxP = Math.max(maxP, getDepth(p, new Set(visited)) + 1);
    }
    memoDepth.set(nodeId, maxP);
    return maxP;
  }

  nodes.forEach((n) => getDepth(n.id, new Set()));

  const depths = Array.from(memoDepth.values());
  const maxDepth = depths.length ? Math.max(...depths) : 0;
  const numColumns = Math.min(Math.max(maxDepth + 1, nodes.length <= 3 ? nodes.length : 2), 4);

  const columns: ConceptNode[][] = Array.from({ length: numColumns }, () => []);

  nodes.forEach((node) => {
    const rawD = memoDepth.get(node.id) ?? 0;
    const colIdx =
      maxDepth === 0
        ? nodes.indexOf(node) % numColumns
        : Math.min(
            Math.floor((rawD / (maxDepth + 0.0001)) * numColumns),
            numColumns - 1,
          );
    columns[colIdx].push(node);
  });

  const colX =
    numColumns === 1
      ? [50]
      : numColumns === 2
      ? [28, 72]
      : numColumns === 3
      ? [18, 50, 82]
      : [14, 38, 62, 86];

  const result: ConceptNode[] = [];

  columns.forEach((colNodes, colIdx) => {
    colNodes.sort((a, b) => a.name.localeCompare(b.name, "vi"));
    const count = colNodes.length;
    colNodes.forEach((node, rowIdx) => {
      const x = colX[colIdx];
      const minY = 16;
      const maxY = 72;
      const y = count === 1 ? 44 : minY + (rowIdx * (maxY - minY)) / Math.max(count - 1, 1);
      result.push({ ...node, x, y });
    });
  });

  return result;
}

const GRAPH_HEIGHT = 88;
type ViewMode = "graph" | "list";

type EdgeGeometry = {
  path: string;
  labelX: number;
  labelY: number;
  obstacleCollisions: number;
  routeType: "curve" | "detour";
};

type GraphPoint = {
  x: number;
  y: number;
};

type NodeBounds = {
  halfX: number;
  halfY: number;
};

type NodeBoundsLookup = Record<string, NodeBounds>;

const DEFAULT_NODE_BOUNDS: NodeBounds = { halfX: 6.2, halfY: 5.8 };

function pointOnCubic(
  p0: GraphPoint,
  p1: GraphPoint,
  p2: GraphPoint,
  p3: GraphPoint,
  t: number,
): GraphPoint {
  const inv = 1 - t;
  const inv2 = inv * inv;
  const inv3 = inv2 * inv;
  const t2 = t * t;
  const t3 = t2 * t;
  return {
    x: inv3 * p0.x + 3 * inv2 * t * p1.x + 3 * inv * t2 * p2.x + t3 * p3.x,
    y: inv3 * p0.y + 3 * inv2 * t * p1.y + 3 * inv * t2 * p2.y + t3 * p3.y,
  };
}

function pointOnNodeBoundary(
  node: ConceptNode,
  toward: GraphPoint,
  bounds: NodeBounds,
): GraphPoint {
  const dx = toward.x - node.x;
  const dy = toward.y - node.y;
  const safeDx = Math.max(Math.abs(dx), 0.001);
  const safeDy = Math.max(Math.abs(dy), 0.001);
  const scale = Math.min(
    (bounds.halfX + 0.45) / safeDx,
    (bounds.halfY + 0.55) / safeDy,
  );

  return {
    x: node.x + dx * scale,
    y: node.y + dy * scale,
  };
}

function countObstacleCollisionsCubic(
  p0: GraphPoint,
  p1: GraphPoint,
  p2: GraphPoint,
  p3: GraphPoint,
  sourceId: string,
  targetId: string,
  nodes: ConceptNode[],
  boundsLookup: NodeBoundsLookup,
): number {
  return nodes.reduce((count, node) => {
    if (node.id === sourceId || node.id === targetId) return count;
    const bounds = boundsLookup[node.id] ?? DEFAULT_NODE_BOUNDS;
    const intersects = Array.from({ length: 31 }, (_, sample) => sample / 30)
      .slice(2, -2)
      .some((t) => {
        const point = pointOnCubic(p0, p1, p2, p3, t);
        return (
          Math.abs(point.x - node.x) <= bounds.halfX + 1.25 &&
          Math.abs(point.y - node.y) <= bounds.halfY + 1.25
        );
      });
    return count + (intersects ? 1 : 0);
  }, 0);
}

function segmentClearsObstacles(
  start: GraphPoint,
  end: GraphPoint,
  obstacles: Array<{ node: ConceptNode; bounds: NodeBounds }>,
): boolean {
  const distance = Math.hypot(end.x - start.x, end.y - start.y);
  const samples = Math.max(2, Math.ceil(distance / 0.65));
  return !Array.from(
    { length: samples - 1 },
    (_, index) => (index + 1) / samples,
  ).some((t) => {
    const point = {
      x: start.x + (end.x - start.x) * t,
      y: start.y + (end.y - start.y) * t,
    };
    return obstacles.some(
      ({ node, bounds }) =>
        Math.abs(point.x - node.x) <= bounds.halfX + 1.25 &&
        Math.abs(point.y - node.y) <= bounds.halfY + 1.25,
    );
  });
}

function findDetourRoute(
  source: ConceptNode,
  target: ConceptNode,
  nodes: ConceptNode[],
  boundsLookup: NodeBoundsLookup,
): GraphPoint[] | null {
  const obstacles = nodes
    .filter((node) => node.id !== source.id && node.id !== target.id)
    .map((node) => ({
      node,
      bounds: boundsLookup[node.id] ?? DEFAULT_NODE_BOUNDS,
    }));
  const points: GraphPoint[] = [
    { x: source.x, y: source.y },
    { x: target.x, y: target.y },
  ];

  obstacles.forEach(({ node, bounds }) => {
    const halfX = bounds.halfX + 2;
    const halfY = bounds.halfY + 2;
    points.push(
      { x: Math.max(1, node.x - halfX), y: Math.max(2, node.y - halfY) },
      { x: Math.min(99, node.x + halfX), y: Math.max(2, node.y - halfY) },
      {
        x: Math.max(1, node.x - halfX),
        y: Math.min(GRAPH_HEIGHT - 2, node.y + halfY),
      },
      {
        x: Math.min(99, node.x + halfX),
        y: Math.min(GRAPH_HEIGHT - 2, node.y + halfY),
      },
    );
  });

  const distances = points.map(() => Number.POSITIVE_INFINITY);
  const previous = points.map(() => -1);
  const visited = points.map(() => false);
  distances[0] = 0;

  for (let step = 0; step < points.length; step += 1) {
    let current = -1;
    for (let index = 0; index < points.length; index += 1) {
      if (
        !visited[index] &&
        (current === -1 || distances[index] < distances[current])
      ) {
        current = index;
      }
    }
    if (current === -1 || !Number.isFinite(distances[current])) break;
    if (current === 1) break;
    visited[current] = true;

    for (let neighbor = 0; neighbor < points.length; neighbor += 1) {
      if (
        neighbor === current ||
        visited[neighbor] ||
        !segmentClearsObstacles(points[current], points[neighbor], obstacles)
      ) {
        continue;
      }
      const candidate =
        distances[current] +
        Math.hypot(
          points[neighbor].x - points[current].x,
          points[neighbor].y - points[current].y,
        );
      if (candidate < distances[neighbor]) {
        distances[neighbor] = candidate;
        previous[neighbor] = current;
      }
    }
  }

  if (!Number.isFinite(distances[1])) return null;
  const route: GraphPoint[] = [];
  for (let cursor = 1; cursor !== -1; cursor = previous[cursor]) {
    route.unshift(points[cursor]);
  }
  return route;
}

function midpointOnPolyline(points: GraphPoint[]): GraphPoint {
  const lengths = points
    .slice(1)
    .map((point, index) =>
      Math.hypot(point.x - points[index].x, point.y - points[index].y),
    );
  const halfway = lengths.reduce((sum, length) => sum + length, 0) / 2;
  let walked = 0;
  for (let index = 0; index < lengths.length; index += 1) {
    const length = lengths[index];
    if (walked + length >= halfway) {
      const t = length ? (halfway - walked) / length : 0;
      return {
        x: points[index].x + (points[index + 1].x - points[index].x) * t,
        y: points[index].y + (points[index + 1].y - points[index].y) * t,
      };
    }
    walked += length;
  }
  return points[points.length - 1];
}

function getEdgeGeometry(
  edge: ConceptEdge,
  source: ConceptNode,
  target: ConceptNode,
  index: number,
  nodes: ConceptNode[],
  boundsLookup: NodeBoundsLookup,
): EdgeGeometry {
  const sourceBounds = boundsLookup[source.id] ?? DEFAULT_NODE_BOUNDS;
  const targetBounds = boundsLookup[target.id] ?? DEFAULT_NODE_BOUNDS;

  const dx = target.x - source.x;
  const dy = target.y - source.y;

  let start: GraphPoint;
  let end: GraphPoint;
  let p1: GraphPoint;
  let p2: GraphPoint;
  let path = "";
  let labelX = (source.x + target.x) / 2;
  let labelY = (source.y + target.y) / 2;
  let collisions = 0;
  
  // Stagger label along the curve so overlapping edges don't stack their labels!
  const t = 0.38 + ((index % 3) * 0.12);

  if (dx > 8) {
    // Forward Flow (Left -> Right): Source Right Edge to Target Left Edge
    start = { x: source.x + sourceBounds.halfX, y: source.y };
    end = { x: target.x - targetBounds.halfX, y: target.y };
    const curveDx = Math.max(dx * 0.45, 5);
    p1 = { x: start.x + curveDx, y: start.y };
    p2 = { x: end.x - curveDx, y: end.y };
    path = `M ${start.x} ${start.y} C ${p1.x} ${p1.y}, ${p2.x} ${p2.y}, ${end.x} ${end.y}`;
    const pt = pointOnCubic(start, p1, p2, end, t);
    labelX = Math.min(Math.max(pt.x, start.x + 4), end.x - 4);
    labelY = pt.y - 2.2;
    collisions = countObstacleCollisionsCubic(start, p1, p2, end, source.id, target.id, nodes, boundsLookup);
  } else if (Math.abs(dx) <= 8) {
    // Same Column: Vertical Connection with gentle side arc
    const isDownward = dy >= 0;
    start = isDownward
      ? { x: source.x, y: source.y + sourceBounds.halfY }
      : { x: source.x, y: source.y - sourceBounds.halfY };
    end = isDownward
      ? { x: target.x, y: target.y - targetBounds.halfY }
      : { x: target.x, y: target.y + targetBounds.halfY };

    const arcOffset = (index % 2 === 0 ? 1 : -1) * 7.5;
    p1 = { x: start.x + arcOffset, y: (start.y * 2 + end.y) / 3 };
    p2 = { x: end.x + arcOffset, y: (start.y + end.y * 2) / 3 };
    path = `M ${start.x} ${start.y} C ${p1.x} ${p1.y}, ${p2.x} ${p2.y}, ${end.x} ${end.y}`;
    const pt = pointOnCubic(start, p1, p2, end, 0.5);
    labelX = pt.x + (arcOffset > 0 ? 3.5 : -3.5);
    labelY = pt.y;
    collisions = countObstacleCollisionsCubic(start, p1, p2, end, source.id, target.id, nodes, boundsLookup);
  } else {
    // Backward Flow (Right -> Left): Arch over top or under bottom
    const goTop = source.y + target.y < GRAPH_HEIGHT;
    start = goTop
      ? { x: source.x, y: source.y - sourceBounds.halfY }
      : { x: source.x, y: source.y + sourceBounds.halfY };
    end = goTop
      ? { x: target.x, y: target.y - targetBounds.halfY }
      : { x: target.x, y: target.y + targetBounds.halfY };

    const yArch = goTop
      ? Math.max(Math.min(start.y, end.y) - 8, 16)
      : Math.min(Math.max(start.y, end.y) + 8, GRAPH_HEIGHT - 10);
    p1 = { x: start.x - 4, y: yArch };
    p2 = { x: end.x + 4, y: yArch };
    path = `M ${start.x} ${start.y} C ${p1.x} ${p1.y}, ${p2.x} ${p2.y}, ${end.x} ${end.y}`;
    const pt = pointOnCubic(start, p1, p2, end, 0.5);
    labelX = pt.x;
    labelY = yArch + (goTop ? -2.2 : 2.6);
    collisions = countObstacleCollisionsCubic(start, p1, p2, end, source.id, target.id, nodes, boundsLookup);
  }

  if (collisions > 0) {
    const detour = findDetourRoute(source, target, nodes, boundsLookup);
    if (detour && detour.length > 1) {
      const detourPoints = [...detour];
      detourPoints[0] = pointOnNodeBoundary(
        source,
        detourPoints[1],
        sourceBounds,
      );
      detourPoints[detourPoints.length - 1] = pointOnNodeBoundary(
        target,
        detourPoints[detourPoints.length - 2],
        targetBounds,
      );
      const labelPoint = midpointOnPolyline(detourPoints);
      return {
        path: detourPoints
          .map(
            (point, pointIndex) =>
              `${pointIndex === 0 ? "M" : "L"} ${point.x} ${point.y}`,
          )
          .join(" "),
        labelX: labelPoint.x,
        labelY: labelPoint.y - 2.8,
        obstacleCollisions: 0,
        routeType: "detour",
      };
    }
  }

  return {
    path,
    labelX,
    labelY,
    obstacleCollisions: collisions,
    routeType: "curve",
  };
}

function RelationList({
  title,
  edges,
  selectedId,
  lookup,
  onSelect,
}: {
  title: string;
  edges: ConceptEdge[];
  selectedId: string;
  lookup: Record<string, ConceptNode>;
  onSelect: (node: ConceptNode, trigger?: HTMLElement) => void;
}) {
  if (!edges.length) return null;

  return (
    <section className="relation-group">
      <h4>{title}</h4>
      <div className="relation-list">
        {edges.map((edge) => {
          const neighborId =
            edge.source === selectedId ? edge.target : edge.source;
          const neighbor = lookup[neighborId];
          if (!neighbor) return null;
          return (
            <button
              type="button"
              className={`relation-item relation-${edge.relation}`}
              key={edge.id}
              onClick={(event) => onSelect(neighbor, event.currentTarget)}
            >
              <span>{relationLabels[edge.relation]}</span>
              <strong>{neighbor.name}</strong>
              <small>
                {lookup[edge.source]?.name}{" "}
                <ArrowRight size={12} aria-hidden="true" />{" "}
                {lookup[edge.target]?.name}
              </small>
            </button>
          );
        })}
      </div>
    </section>
  );
}

function AdjacencyList({
  nodes,
  edges,
  selectedId,
  lookup,
  onSelect,
}: {
  nodes: ConceptNode[];
  edges: ConceptEdge[];
  selectedId?: string;
  lookup: Record<string, ConceptNode>;
  onSelect: (node: ConceptNode, trigger?: HTMLElement) => void;
}) {
  return (
    <div className="adjacency-view">
      <div className="adjacency-heading">
        <div>
          <span>Chế độ dễ đọc</span>
          <h2>Danh sách quan hệ</h2>
        </div>
        <p>
          Mỗi concept hiển thị đầy đủ quan hệ vào và ra, không phụ thuộc vào màu
          sắc hoặc thao tác kéo.
        </p>
      </div>
      <div className="adjacency-grid">
        {nodes.map((node) => {
          const nodeEdges = edges.filter(
            (edge) => edge.source === node.id || edge.target === node.id,
          );
          return (
            <article
              className={`adjacency-card ${selectedId === node.id ? "selected" : ""}`}
              key={node.id}
            >
              <button
                type="button"
                className="adjacency-node-summary"
                onClick={(event) => onSelect(node, event.currentTarget)}
                aria-pressed={selectedId === node.id}
              >
                <span>{filterLabels[node.band]}</span>
                <strong>{node.name}</strong>
                <small>{Math.round(node.mastery * 100)}% nắm vững</small>
              </button>
              <div className="adjacency-edges">
                {nodeEdges.length ? (
                  nodeEdges.map((edge) => {
                    const neighborId =
                      edge.source === node.id ? edge.target : edge.source;
                    const neighbor = lookup[neighborId];
                    if (!neighbor) return null;
                    const direction =
                      edge.source === node.id ? "Đi tới" : "Đi từ";
                    return (
                      <button
                        type="button"
                        key={edge.id}
                        className={`adjacency-edge relation-${edge.relation}`}
                        onClick={(event) =>
                          onSelect(neighbor, event.currentTarget)
                        }
                      >
                        <span>{relationLabels[edge.relation]}</span>
                        <strong>
                          {direction} {neighbor.name}
                        </strong>
                        <small>
                          {lookup[edge.source]?.name} →{" "}
                          {lookup[edge.target]?.name}
                        </small>
                      </button>
                    );
                  })
                ) : (
                  <p>Chưa có quan hệ đã được duyệt.</p>
                )}
              </div>
            </article>
          );
        })}
      </div>
    </div>
  );
}

export function KnowledgeMapExplorer() {
  const [map, setMap] = useState<KnowledgeMap | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selected, setSelected] = useState<ConceptNode | null>(null);
  const [hoveredNode, setHoveredNode] = useState<ConceptNode | null>(null);
  const [hoveredEdgeId, setHoveredEdgeId] = useState<string | null>(null);
  const [filter, setFilter] = useState<"all" | MasteryBand>("all");
  const [domain, setDomain] = useState<KnowledgeDomain>("foundations_product");
  const [search, setSearch] = useState("");
  const [focusRelationships, setFocusRelationships] = useState(false);
  const [viewMode, setViewMode] = useState<ViewMode>("graph");
  const drawerTitleRef = useRef<HTMLHeadingElement>(null);
  const lastTriggerRef = useRef<HTMLElement | null>(null);
  const stageRef = useRef<HTMLDivElement>(null);
  const nodeElementRefs = useRef(new Map<string, HTMLButtonElement>());
  const [nodeBounds, setNodeBounds] = useState<NodeBoundsLookup>({});
  const reduce = useReducedMotion();

  useEffect(() => {
    if (window.matchMedia?.("(max-width: 560px)").matches) {
      setViewMode("list");
    }
  }, []);

  useEffect(() => {
    fetch("/api/knowledge-map", { cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) throw new Error("knowledge map unavailable");
        return (await response.json()) as KnowledgeMap;
      })
      .then((payload) => {
        setMap(payload);
        const compact = window.matchMedia?.("(max-width: 820px)").matches;
        setSelected(
          compact || payload.nodes.length > 12
            ? null
            : (payload.nodes.find((item) => item.id === "evaluation") ??
                payload.nodes[0] ??
                null),
        );
      })
      .catch(() => setError("Không thể tải bản đồ kiến thức."));
  }, []);

  useEffect(() => {
    if (!selected || !window.matchMedia?.("(max-width: 1080px)").matches) {
      return;
    }
    drawerTitleRef.current?.focus();
  }, [selected]);

  useEffect(() => {
    if (!selected) return;

    function closeDrawerOnEscape(event: KeyboardEvent) {
      if (event.key !== "Escape") return;
      setSelected(null);
      requestAnimationFrame(() => lastTriggerRef.current?.focus());
    }

    window.addEventListener("keydown", closeDrawerOnEscape);
    return () => window.removeEventListener("keydown", closeDrawerOnEscape);
  }, [selected]);

  const lookup = useMemo(
    () =>
      Object.fromEntries(
        (map?.nodes ?? []).map((node) => [node.id, node]),
      ) as Record<string, ConceptNode>,
    [map],
  );

  const filteredNodes = useMemo(
    () => {
      const nodes = map?.nodes ?? [];
      const useDomains = nodes.length > 12;
      const query = search.trim().toLocaleLowerCase("vi");
      return nodes.filter(
        (node) =>
          (!useDomains || Boolean(query) || domainForConcept(node.id) === domain) &&
          (filter === "all" || node.band === filter) &&
          (!query ||
            node.name.toLocaleLowerCase("vi").includes(query) ||
            node.summary.toLocaleLowerCase("vi").includes(query)),
      );
    },
    [domain, filter, map, search],
  );

  const activeFocusNode = hoveredNode || selected;

  const incidentEdges = useMemo(
    () =>
      activeFocusNode && map
        ? map.edges.filter(
            (edge) =>
              edge.source === activeFocusNode.id || edge.target === activeFocusNode.id,
          )
        : [],
    [activeFocusNode, map],
  );

  const selectedIncidentEdges = useMemo(
    () =>
      selected && map
        ? map.edges.filter(
            (edge) =>
              edge.source === selected.id || edge.target === selected.id,
          )
        : [],
    [map, selected],
  );

  const relatedIds = useMemo(
    () => new Set(incidentEdges.flatMap((edge) => [edge.source, edge.target])),
    [incidentEdges],
  );

  const visible = useMemo(
    () => {
      const isFocusRelationship = focusRelationships && selected;
      const nodes =
        isFocusRelationship
          ? (map?.nodes ?? []).filter(
              (node) => node.id === selected.id || relatedIds.has(node.id),
            )
          : filteredNodes;
      return layoutVisibleNodes(
        nodes,
        map?.edges ?? [],
        isFocusRelationship ? undefined : (map?.nodes.length ?? 0) > 12 ? domain : undefined,
        search,
        true,
      );
    },
    [domain, filteredNodes, focusRelationships, map, relatedIds, search, selected],
  );

  const visibleLookup = useMemo(
    () =>
      Object.fromEntries(
        visible.map((node) => [node.id, node]),
      ) as Record<string, ConceptNode>,
    [visible],
  );

  useEffect(() => {
    const currentStage = stageRef.current;
    if (!currentStage || viewMode !== "graph") return;
    const stage: HTMLDivElement = currentStage;

    function measureNodes() {
      const stageRect = stage.getBoundingClientRect();
      if (!stageRect.width || !stageRect.height) return;
      const nextBounds = Object.fromEntries(
        visible.flatMap((node) => {
          const element = nodeElementRefs.current.get(node.id);
          if (!element) return [];
          const rect = element.getBoundingClientRect();
          return [
            [
              node.id,
              {
                halfX: (rect.width / 2 / stageRect.width) * 100,
                halfY: (rect.height / 2 / stageRect.height) * GRAPH_HEIGHT,
              },
            ],
          ];
        }),
      ) as NodeBoundsLookup;

      setNodeBounds((current) => {
        const keys = Object.keys(nextBounds);
        const unchanged =
          keys.length === Object.keys(current).length &&
          keys.every(
            (key) =>
              Math.abs(nextBounds[key].halfX - current[key].halfX) < 0.05 &&
              Math.abs(nextBounds[key].halfY - current[key].halfY) < 0.05,
          );
        return unchanged ? current : nextBounds;
      });
    }

    const frame = requestAnimationFrame(measureNodes);
    if (typeof ResizeObserver === "undefined") {
      return () => cancelAnimationFrame(frame);
    }
    const observer = new ResizeObserver(measureNodes);
    observer.observe(stage);
    nodeElementRefs.current.forEach((element) => observer.observe(element));
    return () => {
      cancelAnimationFrame(frame);
      observer.disconnect();
    };
  }, [viewMode, visible]);

  const visibleIds = useMemo(
    () => new Set(visible.map((node) => node.id)),
    [visible],
  );

  const visibleEdges = useMemo(
    () =>
      (map?.edges ?? []).filter(
        (edge) => visibleIds.has(edge.source) && visibleIds.has(edge.target),
      ),
    [map, visibleIds],
  );

  const relationTypes = useMemo(
    () =>
      relationOrder.filter((relation) =>
        visibleEdges.some((edge) => edge.relation === relation),
      ),
    [visibleEdges],
  );

  const incomingPrerequisites = selectedIncidentEdges.filter(
    (edge) =>
      edge.target === selected?.id && edge.relation === "prerequisite_of",
  );
  const outgoingPrerequisites = selectedIncidentEdges.filter(
    (edge) =>
      edge.source === selected?.id && edge.relation === "prerequisite_of",
  );
  const otherRelationships = selectedIncidentEdges.filter(
    (edge) => edge.relation !== "prerequisite_of",
  );

  function selectNode(node: ConceptNode, trigger?: HTMLElement) {
    if (trigger) lastTriggerRef.current = trigger;
    if ((map?.nodes.length ?? 0) > 12) {
      setDomain(domainForConcept(node.id));
      setSearch("");
    }
    setSelected(node);
    if (filter !== "all" && node.band !== filter) setFilter("all");
  }

  function applyDomain(nextDomain: KnowledgeDomain) {
    setDomain(nextDomain);
    setSearch("");
    setFocusRelationships(false);
    if (selected && domainForConcept(selected.id) !== nextDomain) {
      setSelected(null);
    }
  }

  function closeDrawer() {
    setSelected(null);
    requestAnimationFrame(() => lastTriggerRef.current?.focus());
  }

  function applyFilter(nextFilter: "all" | MasteryBand) {
    setFilter(nextFilter);
    if (nextFilter !== "all" && selected && selected.band !== nextFilter) {
      setSelected(map?.nodes.find((node) => node.band === nextFilter) ?? null);
    }
  }

  if (error) return <div className="glass-surface">{error}</div>;
  if (!map)
    return (
      <div className="glass-surface" aria-label="Đang tải bản đồ kiến thức">
        Đang tải bản đồ kiến thức…
      </div>
    );

  const usesDomainNavigation = map.nodes.length > 12;
  const activeDomain = knowledgeDomains.find((item) => item.id === domain)!;

  return (
    <div
      className={`map-explorer ${selected ? "has-selection" : ""} ${usesDomainNavigation ? "full-taxonomy" : ""}`}
    >
      <section
        className={`map-canvas view-${viewMode}`}
        aria-label="Bản đồ kiến thức tương tác"
      >
        <div className="map-toolbar glass-surface">
          <Funnel size={17} aria-hidden="true" />
          {(Object.keys(filterLabels) as Array<keyof typeof filterLabels>).map(
            (key) => (
              <button
                type="button"
                className={filter === key ? "active" : ""}
                key={key}
                onClick={() => applyFilter(key)}
                aria-pressed={filter === key}
              >
                {filterLabels[key]}
              </button>
            ),
          )}
          <span className="toolbar-divider" aria-hidden="true" />
          <button
            type="button"
            className={focusRelationships ? "active" : ""}
            onClick={() => setFocusRelationships((current) => !current)}
            aria-pressed={focusRelationships}
            disabled={!selected}
          >
            Tập trung quan hệ
          </button>
          <span className="toolbar-divider" aria-hidden="true" />
          <div className="map-view-switch" aria-label="Chế độ hiển thị">
            <button
              type="button"
              className={viewMode === "graph" ? "active" : ""}
              onClick={() => setViewMode("graph")}
              aria-pressed={viewMode === "graph"}
            >
              Sơ đồ
            </button>
            <button
              type="button"
              className={viewMode === "list" ? "active" : ""}
              onClick={() => setViewMode("list")}
              aria-pressed={viewMode === "list"}
            >
              Danh sách
            </button>
          </div>
        </div>

        {usesDomainNavigation ? (
          <div className="map-domain-bar glass-surface">
            <div className="map-search-field">
              <MagnifyingGlass size={16} aria-hidden="true" />
              <label className="sr-only" htmlFor="knowledge-map-search">
                Tìm concept trong toàn bộ bản đồ
              </label>
              <input
                id="knowledge-map-search"
                type="search"
                value={search}
                onChange={(event) => setSearch(event.target.value)}
                placeholder={`Tìm trong ${map.nodes.length} concept…`}
              />
            </div>
            <nav className="map-domain-tabs" aria-label="Lĩnh vực kiến thức">
              {knowledgeDomains.map((item) => {
                const nodeCount = map.nodes.filter((node) =>
                  item.concepts.has(node.id),
                ).length;
                return (
                  <button
                    type="button"
                    key={item.id}
                    className={domain === item.id && !search ? "active" : ""}
                    onClick={() => applyDomain(item.id)}
                    aria-pressed={domain === item.id && !search}
                    title={item.description}
                  >
                    {item.label} <span>{nodeCount}</span>
                  </button>
                );
              })}
            </nav>
            <p className="map-domain-description">
              {search
                ? `${visible.length} kết quả trên toàn bộ bản đồ`
                : activeDomain.description}
            </p>
          </div>
        ) : null}

        <div className="map-overview" aria-label="Tổng quan graph">
          <span>{map.version}</span>
          <strong>
            {visible.length}/{map.nodes.length} node
          </strong>
          <strong>{visibleEdges.length} quan hệ</strong>
        </div>

        <div className="map-stage" ref={stageRef}>
          {viewMode === "graph" && usesDomainNavigation && !search && (
            <div className="map-stage-columns" aria-hidden="true">
              {activeDomain.stages.map((stageTitle, sIdx) => (
                <div key={sIdx} className="stage-column-guide">
                  <span className="stage-guide-title">{stageTitle}</span>
                </div>
              ))}
            </div>
          )}

          <svg
            className="map-lines"
            viewBox={`0 0 100 ${GRAPH_HEIGHT}`}
            preserveAspectRatio="none"
            role="img"
            aria-label={`${visibleEdges.length} quan hệ có hướng giữa các concept`}
          >
            <title>Bản đồ quan hệ kiến thức</title>
            <desc>
              Mũi tên đi từ concept nguồn đến concept đích. Chọn hoặc di chuột vào một node để làm
              nổi các quan hệ đầu vào và đầu ra.
            </desc>
            <defs>
              {relationOrder.map((relation) => (
                <marker
                  id={`arrow-${relation}`}
                  key={relation}
                  className={`edge-marker edge-${relation}`}
                  markerWidth="1.6"
                  markerHeight="1.6"
                  refX="1.3"
                  refY="0.8"
                  orient="auto"
                  markerUnits="userSpaceOnUse"
                >
                  <path d="M 0 0 L 1.6 0.8 L 0 1.6 z" />
                </marker>
              ))}
            </defs>
            {visibleEdges.map((edge, index) => {
              const source = visibleLookup[edge.source];
              const target = visibleLookup[edge.target];
              if (!source || !target) return null;
              const geometry = getEdgeGeometry(
                edge,
                source,
                target,
                index,
                visible,
                nodeBounds,
              );
              const isDirectlyHovered = hoveredEdgeId === edge.id;
              const isConnectedToFocus = activeFocusNode
                ? edge.source === activeFocusNode.id || edge.target === activeFocusNode.id
                : false;
              const isActive = isDirectlyHovered || (activeFocusNode ? isConnectedToFocus : true);
              const isLabelVisible = isDirectlyHovered;

              return (
                <g
                  key={edge.id}
                  className={`map-edge edge-${edge.relation} ${isActive ? "active" : "muted"} ${isLabelVisible ? "label-visible" : "idle"}`}
                  data-relation={edge.relation}
                  data-source={edge.source}
                  data-target={edge.target}
                  data-obstacle-collisions={geometry.obstacleCollisions}
                  data-route={geometry.routeType}
                  onMouseEnter={() => setHoveredEdgeId(edge.id)}
                  onMouseLeave={() => setHoveredEdgeId(null)}
                >
                  <path
                    d={geometry.path}
                    markerEnd={`url(#arrow-${edge.relation})`}
                  />
                  {isLabelVisible && (
                    <g
                      className="edge-label"
                      transform={`translate(${geometry.labelX} ${geometry.labelY})`}
                    >
                      <rect
                        x="-6"
                        y="-2"
                        width="12"
                        height="4"
                        rx="2"
                      />
                      <text textAnchor="middle" dominantBaseline="central">
                        {relationLabels[edge.relation]}
                      </text>
                    </g>
                  )}
                </g>
              );
            })}
          </svg>

          {visible.map((node, index) => {
            const nodeEdges = map.edges.filter(
              (edge) => edge.source === node.id || edge.target === node.id,
            );
            const incomingCount = nodeEdges.filter(
              (edge) => edge.target === node.id,
            ).length;
            const outgoingCount = nodeEdges.length - incomingCount;
            const isSelected = selected?.id === node.id;
            const isHovered = hoveredNode?.id === node.id;
            const isRelated = activeFocusNode
              ? activeFocusNode.id === node.id || relatedIds.has(node.id)
              : true;
            const upstream = incidentEdges.some(
              (edge) => edge.source === node.id && edge.target === activeFocusNode?.id,
            );
            const downstream = incidentEdges.some(
              (edge) => edge.target === node.id && edge.source === activeFocusNode?.id,
            );
            return (
              <motion.button
                layout
                ref={(element) => {
                  if (element) nodeElementRefs.current.set(node.id, element);
                  else nodeElementRefs.current.delete(node.id);
                }}
                type="button"
                key={node.id}
                className={`map-node node-${node.band} ${isSelected ? "selected" : ""} ${isHovered ? "hovered" : ""} ${isRelated ? "related" : "muted"} ${upstream ? "upstream" : ""} ${downstream ? "downstream" : ""}`}
                style={{
                  left: `${node.x}%`,
                  top: `${(node.y / GRAPH_HEIGHT) * 100}%`,
                }}
                onClick={(event) => selectNode(node, event.currentTarget)}
                onMouseEnter={() => setHoveredNode(node)}
                onMouseLeave={() => setHoveredNode(null)}
                initial={reduce ? false : { opacity: 0, scale: 0.75 }}
                animate={{
                  opacity: activeFocusNode && !isRelated ? 0.35 : 1,
                  scale: isSelected ? 1.03 : 1,
                }}
                transition={{ delay: reduce ? 0 : index * 0.02 }}
                aria-label={`${node.name}, mức độ nắm vững ${Math.round(node.mastery * 100)}%, ${nodeEdges.length} quan hệ`}
                aria-pressed={isSelected}
              >
                <span className="map-node-meta">{filterLabels[node.band]}</span>
                <span className="map-node-degree">
                  {incomingCount} vào · {outgoingCount} ra
                </span>
                <span className="map-node-title">{node.name}</span>
                <span className="map-node-progress" aria-hidden="true">
                  <i style={{ width: `${Math.round(node.mastery * 100)}%` }} />
                </span>
                <strong>{Math.round(node.mastery * 100)}%</strong>
                {(upstream || downstream) && (
                  <em>{upstream ? "Cần trước" : "Mở khóa"}</em>
                )}
              </motion.button>
            );
          })}
        </div>

        <div
          className="map-legend glass-surface"
          aria-label="Chú giải loại quan hệ"
        >
          <span>Quan hệ có hướng</span>
          {relationTypes.map((relation) => (
            <div key={relation} className={`legend-item edge-${relation}`}>
              <i aria-hidden="true" />
              {relationLabels[relation]}
            </div>
          ))}
        </div>
        <AdjacencyList
          nodes={visible}
          edges={visibleEdges}
          selectedId={selected?.id}
          lookup={lookup}
          onSelect={selectNode}
        />
      </section>

      <AnimatePresence>
        {selected && (
          <motion.aside
            className="concept-drawer"
            initial={reduce ? false : { opacity: 0, x: 30 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 30 }}
            aria-label={`Chi tiết ${selected.name}`}
          >
            <button
              className="drawer-close icon-button"
              type="button"
              onClick={closeDrawer}
              aria-label="Đóng chi tiết"
            >
              <X size={19} aria-hidden="true" />
            </button>
            <span className="concept-status">
              {filterLabels[selected.band]} ·{" "}
              {Math.round(selected.confidence * 100)}% tin cậy
            </span>
            <h2 ref={drawerTitleRef} tabIndex={-1}>
              {selected.name}
            </h2>
            <p>{selected.summary}</p>

            <div className="mastery-number">
              <strong>{Math.round(selected.mastery * 100)}%</strong>
              <span>mức độ nắm vững hiện tại</span>
            </div>

            <div className="relationship-inspector">
              <div className="drawer-section-heading">
                <h3>Mối quan hệ</h3>
                <span>{selectedIncidentEdges.length} liên kết trực tiếp</span>
              </div>
              {selectedIncidentEdges.length ? (
                <>
                  <RelationList
                    title="Cần học trước"
                    edges={incomingPrerequisites}
                    selectedId={selected.id}
                    lookup={lookup}
                    onSelect={selectNode}
                  />
                  <RelationList
                    title="Mở khóa tiếp theo"
                    edges={outgoingPrerequisites}
                    selectedId={selected.id}
                    lookup={lookup}
                    onSelect={selectNode}
                  />
                  <RelationList
                    title="Liên hệ khác"
                    edges={otherRelationships}
                    selectedId={selected.id}
                    lookup={lookup}
                    onSelect={selectNode}
                  />
                </>
              ) : (
                <p className="relation-empty">
                  Concept này chưa có quan hệ đã được duyệt.
                </p>
              )}
            </div>

            <h3>Mục tiêu học tập</h3>
            <p>{selected.objective}</p>
            <h3>Nguồn bằng chứng</h3>
            {selected.citations.map((citation) => (
              <Link
                className="citation-link"
                href={`/sources/${encodeURIComponent(citation.sourceSpanId)}`}
                key={citation.sourceSpanId}
              >
                <span>
                  {citation.title}
                  <small>{citation.locator}</small>
                </span>
                <ArrowSquareOut size={18} />
              </Link>
            ))}
            <Link
              className="button button-secondary concept-learn-link"
              href={`/learn?concept=${encodeURIComponent(selected.id)}`}
            >
              Học micro-lesson về concept này <ArrowSquareOut size={16} />
            </Link>
          </motion.aside>
        )}
      </AnimatePresence>
    </div>
  );
}
