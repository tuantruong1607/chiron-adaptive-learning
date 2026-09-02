import {
  cleanup,
  fireEvent,
  render,
  screen,
  waitFor,
  within,
} from "@testing-library/react";
import React from "react";
import { afterEach, describe, expect, it, vi } from "vitest";

import { KnowledgeMapExplorer } from "./knowledge-map";

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
});

describe("KnowledgeMapExplorer", () => {
  it("renders a citation link that targets the exact source span", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          courseId: "rag-intensive",
          version: "graph-2026.08",
          nodes: [
            {
              id: "evaluation",
              name: "RAG evaluation",
              summary: "Measure retrieval and answer quality.",
              objective: "Choose grounded metrics.",
              mastery: 0.4,
              confidence: 0.8,
              examWeight: 0.9,
              band: "developing",
              x: 25,
              y: 30,
              citations: [
                {
                  sourceSpanId: "span/with spaces",
                  title: "Course PDF",
                  locator: "Slide 69",
                  excerpt: "Evaluation evidence.",
                },
              ],
            },
          ],
          edges: [],
        }),
      }),
    );

    render(<KnowledgeMapExplorer />);

    const link = await screen.findByRole("link", {
      name: /Course PDF Slide 69/,
    });
    expect(link).toHaveAttribute("href", "/sources/span%2Fwith%20spaces");
  });

  it("shows an authenticated loading failure instead of demo graph data", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: false }));
    render(<KnowledgeMapExplorer />);
    expect(
      await screen.findByText("Không thể tải bản đồ kiến thức."),
    ).toBeInTheDocument();
  });

  it("shows directed, labelled relationships and lets the learner follow a neighbor", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          courseId: "rag-intensive",
          version: "graph-2026.08",
          nodes: [
            {
              id: "evaluation",
              name: "RAG evaluation",
              summary: "Đo chất lượng hệ thống.",
              objective: "Thiết kế eval gate.",
              mastery: 0.18,
              confidence: 0.57,
              examWeight: 0.92,
              band: "new",
              x: 78,
              y: 65,
              citations: [],
            },
            {
              id: "citation",
              name: "Citation verification",
              summary: "Kiểm tra bằng chứng.",
              objective: "Đo citation precision.",
              mastery: 0.67,
              confidence: 0.75,
              examWeight: 0.94,
              band: "secure",
              x: 84,
              y: 37,
              citations: [],
            },
            {
              id: "graph-routing",
              name: "Graph-lite routing",
              summary: "Điều hướng multi-hop.",
              objective: "Chọn quan hệ phù hợp.",
              mastery: 0.22,
              confidence: 0.61,
              examWeight: 0.79,
              band: "developing",
              x: 57,
              y: 59,
              citations: [],
            },
          ],
          edges: [
            {
              id: "e1",
              source: "citation",
              target: "evaluation",
              relation: "part_of",
              weight: 0.82,
            },
            {
              id: "e2",
              source: "graph-routing",
              target: "evaluation",
              relation: "applies_to",
              weight: 0.74,
            },
          ],
        }),
      }),
    );

    const { container } = render(<KnowledgeMapExplorer />);

    expect(
      await screen.findByRole("img", {
        name: "2 quan hệ có hướng giữa các concept",
      }),
    ).toBeInTheDocument();
    expect(container.querySelector("#arrow-part_of")).toBeInTheDocument();
    expect(screen.getByText("2 liên kết trực tiếp")).toBeInTheDocument();
    expect(screen.getAllByText("Thuộc về").length).toBeGreaterThan(0);
    expect(screen.getAllByText("Áp dụng vào").length).toBeGreaterThan(0);

    const evaluationDrawer = screen.getByLabelText("Chi tiết RAG evaluation");
    fireEvent.click(
      within(evaluationDrawer).getByRole("button", {
        name: /Citation verification/,
      }),
    );
    expect(
      screen.getByLabelText("Chi tiết Citation verification"),
    ).toBeInTheDocument();
  });

  it("provides an adjacency-list alternative to the visual graph", async () => {
    vi.stubGlobal(
      "matchMedia",
      vi.fn().mockReturnValue({
        matches: true,
        addEventListener: vi.fn(),
        removeEventListener: vi.fn(),
      }),
    );
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          courseId: "rag-intensive",
          version: "graph-2026.08",
          nodes: [
            {
              id: "retrieval",
              name: "Hybrid retrieval",
              summary: "Kết hợp lexical và semantic retrieval.",
              objective: "Chọn chiến lược truy hồi.",
              mastery: 0.52,
              confidence: 0.8,
              examWeight: 0.8,
              band: "developing",
              x: 30,
              y: 30,
              citations: [],
            },
          ],
          edges: [],
        }),
      }),
    );

    const { container } = render(<KnowledgeMapExplorer />);
    await screen.findAllByRole("button", { name: /Hybrid retrieval/ });
    fireEvent.click(screen.getByRole("button", { name: "Danh sách" }));

    expect(
      container.querySelector(".map-canvas.view-list"),
    ).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Danh sách" })).toHaveAttribute(
      "aria-pressed",
      "true",
    );
    expect(
      screen.getByRole("heading", { name: "Danh sách quan hệ" }),
    ).toBeInTheDocument();

    const conceptButton = container.querySelector<HTMLButtonElement>(
      ".adjacency-node-summary",
    );
    expect(conceptButton).not.toBeNull();
    fireEvent.click(conceptButton!);
    await waitFor(() =>
      expect(
        screen.getByRole("heading", { name: "Hybrid retrieval" }),
      ).toHaveFocus(),
    );

    fireEvent.keyDown(window, { key: "Escape" });
    await waitFor(() => expect(conceptButton).toHaveFocus());
  });

  it("routes an edge around an unrelated node on the direct path", async () => {
    const concept = (id: string, name: string, x: number) => ({
      id,
      name,
      summary: `${name} summary`,
      objective: `${name} objective`,
      mastery: 0.5,
      confidence: 0.8,
      examWeight: 0.8,
      band: "developing",
      x,
      y: 44,
      citations: [],
    });
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          courseId: "rag-intensive",
          version: "graph-routing-test",
          nodes: [
            concept("source", "Source", 10),
            concept("blocker", "Blocker", 50),
            concept("target", "Target", 90),
          ],
          edges: [
            {
              id: "edge-around-blocker",
              source: "source",
              target: "target",
              relation: "prerequisite_of",
              weight: 0.8,
            },
          ],
        }),
      }),
    );

    const { container } = render(<KnowledgeMapExplorer />);
    await screen.findByRole("img", {
      name: "1 quan hệ có hướng giữa các concept",
    });

    const routedEdge = container.querySelector(
      '[data-obstacle-collisions="0"]',
    );
    expect(routedEdge).toBeInTheDocument();
    expect(routedEdge?.querySelector("path")?.getAttribute("d")).not.toContain(
      "Q 50 44",
    );
  });

  it("uses domain drill-down and global search for the full-course taxonomy", async () => {
    const ids = [
      "ai_llm_foundations",
      "transformer_generation",
      "prompt_engineering",
      "tool_calling",
      "react_reasoning",
      "ai_problem_framing",
      "ai_product_delivery",
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
      "agent_memory",
      "short_term_memory",
      "episodic_memory",
      "semantic_memory",
      "memory_consolidation",
      "self_improving_agents",
      "knowledge_graph",
      "graphrag_multi_hop",
      "confidence_calibration",
      "retrieval_prompt_injection",
      "owasp_llm_security",
      "pii_governance",
      "guardrails",
      "fallback_governance",
      "audit_retention_redaction",
      "deployment_pipeline",
      "health_probes",
      "observability",
      "sli_slo",
      "incident_diagnosis",
      "circuit_breaker",
      "fallback_policy",
      "semantic_cache",
      "ai_evaluation",
      "online_offline_evaluation",
      "error_types_metrics",
      "context_precision_recall",
      "faithfulness_grounding",
      "answer_relevancy",
      "golden_dataset",
      "llm_as_judge",
      "rag_evaluation",
      "model_fine_tuning",
      "lora_qlora",
      "supervised_fine_tuning",
      "preference_alignment",
      "dpo_orpo",
      "simpo_kto",
      "nondeterminism",
      "retrieval_router",
      "production_reliability",
    ];
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          courseId: "rag-intensive",
          version: "course-knowledge-v2",
          nodes: ids.map((id, index) => ({
            id,
            name: id === "graphrag_multi_hop" ? "GraphRAG" : id,
            summary: `${id} summary`,
            objective: `${id} objective`,
            mastery: 0,
            confidence: 0.8,
            examWeight: 0.5,
            band: "new",
            x: 10 + (index % 5) * 20,
            y: 10 + Math.floor(index / 5) * 11,
            citations: [],
          })),
          edges: [],
        }),
      }),
    );

    const { container } = render(<KnowledgeMapExplorer />);
    await screen.findByRole("searchbox", {
      name: "Tìm concept trong toàn bộ bản đồ",
    });

    expect(container.querySelectorAll(".map-node")).toHaveLength(7);
    fireEvent.click(
      screen.getByRole("button", { name: "Memory & Graph 8" }),
    );
    await waitFor(() =>
      expect(container.querySelectorAll(".map-node")).toHaveLength(8),
    );

    fireEvent.change(
      screen.getByRole("searchbox", {
        name: "Tìm concept trong toàn bộ bản đồ",
      }),
      { target: { value: "GraphRAG" } },
    );
    await waitFor(() =>
      expect(container.querySelectorAll(".map-node")).toHaveLength(1),
    );
    expect(screen.getByText("1 kết quả trên toàn bộ bản đồ")).toBeInTheDocument();
  });
});
