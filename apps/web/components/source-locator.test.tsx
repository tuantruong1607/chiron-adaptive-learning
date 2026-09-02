import { cleanup, render, screen, waitFor } from "@testing-library/react";
import React from "react";
import { afterEach, describe, expect, it, vi } from "vitest";

import { SourceLocator } from "./source-locator";

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
});

describe("SourceLocator", () => {
  it("loads and renders the requested structured locator", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        sourceSpanId: "span/69",
        title: "Course PDF",
        locator: "Slide 69",
        excerpt: "RRF combines ranked lists.",
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
      }),
    });
    vi.stubGlobal("fetch", fetchMock);

    render(<SourceLocator sourceSpanId="span/69" />);

    expect(
      await screen.findByRole("heading", { name: "Course PDF" }),
    ).toBeInTheDocument();
    expect(screen.getByText("Reciprocal Rank Fusion")).toBeInTheDocument();
    expect(screen.getByText("RRF combines ranked lists.")).toBeInTheDocument();
    expect(fetchMock).toHaveBeenCalledWith(
      "/api/source-spans/span%2F69",
      expect.objectContaining({ cache: "no-store" }),
    );
  });

  it("renders the API locator error", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: false,
        json: async () => ({
          error: "Không tìm thấy nguồn trong graph hiện tại.",
        }),
      }),
    );
    render(<SourceLocator sourceSpanId="missing" />);
    await waitFor(() =>
      expect(screen.getByRole("alert")).toHaveTextContent(
        "Không tìm thấy nguồn",
      ),
    );
  });
});
