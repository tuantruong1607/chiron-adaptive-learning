import { cleanup, render, screen } from "@testing-library/react";
import React from "react";
import { afterEach, describe, expect, it } from "vitest";

import { MockExam } from "./mock-exam";

afterEach(() => {
  cleanup();
  localStorage.clear();
});

describe("MockExam", () => {
  it("presents four clear 100-question exam forms", async () => {
    render(<MockExam />);

    expect(
      screen.getByRole("heading", { level: 2 }),
    ).toHaveTextContent("100 Câu");
    expect(screen.getAllByRole("button", { name: /Bắt đầu/ })).toHaveLength(4);
    expect(
      screen.getAllByText(/90 câu trắc nghiệm/i).length,
    ).toBeGreaterThan(0);
  });
});
