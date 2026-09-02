import { describe, expect, it } from "vitest";
import { concepts, edges, questions } from "./demo-data";

describe("vertical-slice fixtures", () => {
  it("keeps source provenance on every concept", () => {
    expect(concepts.every((concept) => concept.citations.length > 0)).toBe(true);
  });

  it("does not expose an answer field to the browser", () => {
    expect(questions.every((question) => !("answer" in question))).toBe(true);
  });

  it("does not create self-referencing edges", () => {
    expect(edges.every((edge) => edge.source !== edge.target)).toBe(true);
  });
});
