import {
  cleanup,
  fireEvent,
  render,
  screen,
  waitFor,
} from "@testing-library/react";
import React from "react";
import { afterEach, describe, expect, it, vi } from "vitest";

import { ScenarioLab } from "./scenario-lab";

afterEach(() => {
  cleanup();
  window.localStorage.clear();
  vi.unstubAllGlobals();
});

describe("ScenarioLab", () => {
  it("loads a scenario definition, resumes state and submits evidence", async () => {
    const fetchMock = vi.fn().mockImplementation((url: string) => {
      if (url === "/api/labs") {
        return Promise.resolve({
          ok: true,
          json: async () => [
            {
              id: "graph-lite-routing",
              title: "Graph-lite Routing",
              objective:
                "Route only relationship queries through graph expansion.",
              brief: "Protect direct facts.",
              estimatedMinutes: 20,
              successThreshold: 75,
              conceptId: "multi_hop_retrieval",
              sourceSpanIds: ["span-graph"],
              scenario: "A prerequisite query needs bounded traversal.",
              controls: [
                {
                  id: "routing",
                  label: "Routing mode",
                  kind: "select",
                  defaultValue: "adaptive",
                  options: [{ value: "adaptive", label: "Adaptive" }],
                  helpText: "Intent",
                },
                {
                  id: "direct_fallback",
                  label: "Direct fallback",
                  kind: "toggle",
                  defaultValue: true,
                  options: [],
                  helpText: "Guard",
                },
              ],
              transferPrompts: [
                {
                  id: "routing",
                  prompt: "Khi nào mở graph?",
                  placeholder: "Giải thích",
                  minLength: 12,
                },
              ],
            },
          ],
        });
      }
      return Promise.resolve({
        ok: true,
        json: async () => ({
          score: 100,
          passed: true,
          feedback: ["Passed"],
          evidence_event_id: "event-1",
          mastery_update: {
            previous: 0.2,
            current: 0.6,
            concept_id: "multi_hop_retrieval",
          },
          study_plan: { id: "plan-1", planner_version: "cram-planner-v1" },
        }),
      });
    });
    vi.stubGlobal("fetch", fetchMock);

    render(<ScenarioLab labId="graph-lite-routing" />);
    expect(
      await screen.findByRole("heading", { name: "Graph-lite Routing" }),
    ).toBeInTheDocument();
    fireEvent.change(screen.getByPlaceholderText("Giải thích"), {
      target: { value: "Mở graph cho prerequisite multi-hop intent." },
    });
    fireEvent.click(screen.getByRole("button", { name: /Chạy đánh giá/i }));

    expect(await screen.findByText("100/100")).toBeInTheDocument();
    expect(screen.getByText(/Study plan đã được cập nhật/)).toBeInTheDocument();
    await waitFor(() => expect(fetchMock).toHaveBeenCalledTimes(2));
    const submitCall = fetchMock.mock.calls[1];
    expect(submitCall[0]).toBe("/api/labs/graph-lite-routing/submit");
    expect(JSON.parse(submitCall[1].body)).toMatchObject({
      configuration: { routing: "adaptive", direct_fallback: true },
      transfer_answers: {
        routing: "Mở graph cho prerequisite multi-hop intent.",
      },
    });
  });
});
