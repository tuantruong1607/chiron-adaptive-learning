import { describe, expect, it } from "vitest";

import { toKnowledgeMap, toSourceLocator } from "./api";

describe("knowledge map API adapter", () => {
  it("maps source citations and graph edges without demo data", () => {
    const result = toKnowledgeMap({
      course_id: "rag-intensive",
      version: "graph-2026.08",
      nodes: [
        {
          id: "rrf",
          name: "Reciprocal Rank Fusion",
          summary: "Fuse ranked lists",
          objective: "Explain rank normalization",
          mastery: 0.31,
          confidence: 0.65,
          exam_weight: 0.9,
          band: "developing",
          x: 52,
          y: 31,
          citations: [
            {
              source_span_id: "span-rrf",
              title: "Track 3 Day 07",
              locator: "Trang 69",
              excerpt: "RRF uses rank.",
            },
          ],
        },
      ],
      edges: [],
    });
    expect(result.courseId).toBe("rag-intensive");
    expect(result.nodes[0].citations[0]).toEqual({
      sourceSpanId: "span-rrf",
      title: "Track 3 Day 07",
      locator: "Trang 69",
      excerpt: "RRF uses rank.",
    });
  });

  it("preserves the structured source locator returned by the API", () => {
    expect(toSourceLocator({
      source_span_id: "span-rrf",
      title: "Track 3 Day 07",
      locator: "Slide 69",
      excerpt: "RRF uses rank.",
      source_type: "course_pdf",
      locator_kind: "page",
      label: "Slide 69",
      page: 69,
      section_title: "Reciprocal Rank Fusion",
      heading: null,
      section_id: null,
      source_file: null,
      order: null,
      extraction_method: "pdf-text-layer",
    })).toEqual({
      sourceSpanId: "span-rrf",
      title: "Track 3 Day 07",
      locator: "Slide 69",
      excerpt: "RRF uses rank.",
      sourceType: "course_pdf",
      locatorKind: "page",
      label: "Slide 69",
      page: 69,
      sectionTitle: "Reciprocal Rank Fusion",
      heading: null,
      sectionId: null,
      sourceFile: null,
      order: null,
      extractionMethod: "pdf-text-layer",
    });
  });
});
