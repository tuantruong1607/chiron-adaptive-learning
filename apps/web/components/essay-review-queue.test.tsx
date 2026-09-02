import {
  cleanup,
  fireEvent,
  render,
  screen,
  waitFor,
} from "@testing-library/react";
import React from "react";
import { afterEach, describe, expect, it, vi } from "vitest";

import { EssayReviewQueue } from "./essay-review-queue";

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
});

describe("EssayReviewQueue", () => {
  it("releases an instructor-reviewed score and removes the queue item", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce({
        ok: true,
        json: async () => [
          {
            id: "essay-1",
            prompt: "Thiết kế pipeline RAG an toàn",
            answer: "Tenant filter trước retrieval và verify citation.",
            score: 6,
            max_score: 10,
            confidence: 0.5,
            feedback: "Cần bổ sung trade-off.",
            rubric_version: "system-design-v1",
            criterion_scores: { grounding: 3, reasoning: 2, transfer: 1 },
            created_at: "2026-08-31T10:00:00Z",
          },
        ],
      })
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({ status: "graded" }),
      });
    vi.stubGlobal("fetch", fetchMock);

    render(<EssayReviewQueue />);
    expect(
      await screen.findByRole("heading", {
        name: "Thiết kế pipeline RAG an toàn",
      }),
    ).toBeInTheDocument();
    fireEvent.click(
      screen.getByRole("button", { name: /Xác nhận và release/i }),
    );

    expect(
      await screen.findByRole("heading", { name: "Review queue đã sạch" }),
    ).toBeInTheDocument();
    await waitFor(() => expect(fetchMock).toHaveBeenCalledTimes(2));
    expect(fetchMock.mock.calls[1][0]).toBe("/api/essays/essay-1/review");
    expect(JSON.parse(fetchMock.mock.calls[1][1].body)).toMatchObject({
      score: 6,
      max_score: 10,
      criterion_scores: { grounding: 3, reasoning: 2, transfer: 1 },
    });
  });
});
