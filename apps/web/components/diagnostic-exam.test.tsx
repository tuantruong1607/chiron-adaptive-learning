import {
  cleanup,
  fireEvent,
  render,
  screen,
  waitFor,
} from "@testing-library/react";
import React from "react";
import { afterEach, describe, expect, it, vi } from "vitest";

import { DiagnosticExam } from "./diagnostic-exam";

const diagnosticQuestions = Array.from({ length: 25 }, (_, index) => ({
  id: `q${index + 1}`,
  concept_id: "evaluation",
  prompt: `Câu hỏi ${index + 1}`,
  options: [
    { id: "a", text: "Lựa chọn A" },
    { id: "b", text: "Lựa chọn B" },
    { id: "c", text: "Lựa chọn C" },
    { id: "d", text: "Lựa chọn D" },
  ],
}));

function diagnosticResponse() {
  return {
    ok: true,
    json: async () => diagnosticQuestions,
  };
}

afterEach(() => {
  cleanup();
  localStorage.clear();
  vi.unstubAllGlobals();
});

describe("DiagnosticExam", () => {
  it("discards a malformed saved draft instead of crashing", async () => {
    localStorage.setItem("chiron-diagnostic-draft", "not-json");
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(diagnosticResponse()));

    render(<DiagnosticExam />);

    expect(await screen.findByText(/Câu 1 \/ 25/)).toBeInTheDocument();
    await waitFor(() =>
      expect(localStorage.getItem("chiron-diagnostic-draft")).toBe("{}"),
    );
  });

  it("shows a recoverable error when grading returns a failed payload", async () => {
    vi.stubGlobal(
      "fetch",
      vi
        .fn()
        .mockResolvedValueOnce(diagnosticResponse())
        .mockResolvedValue({
          ok: false,
          json: async () => ({ error: "upstream failed" }),
        }),
    );
    render(<DiagnosticExam />);

    await screen.findByText(/Câu 1 \/ 25/);
    for (let index = 0; index < 25; index += 1) {
      fireEvent.click(screen.getAllByRole("radio")[0]);
      fireEvent.click(
        screen.getByRole("button", {
          name: index < 24 ? /Câu tiếp/ : /Nộp bài/,
        }),
      );
    }

    expect(
      await screen.findByText(/Không thể chấm bài lúc này/),
    ).toBeInTheDocument();
    expect(screen.getByText(/Câu 25 \/ 25/)).toBeInTheDocument();
    await waitFor(() =>
      expect(screen.getByRole("button", { name: /Nộp bài/ })).toBeEnabled(),
    );
  });
});
