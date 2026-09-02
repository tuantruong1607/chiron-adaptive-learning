import { describe, expect, it } from "vitest";

import { isTrustedSameOrigin } from "./request-origin";

function request(origin?: string, url = "http://0.0.0.0:3000/api") {
  return { headers: new Headers(origin ? { origin } : {}), url };
}

describe("isTrustedSameOrigin", () => {
  it("accepts the configured public origin behind a reverse proxy", () => {
    expect(
      isTrustedSameOrigin(
        request("https://chiron.example.com"),
        true,
        "https://chiron.example.com",
      ),
    ).toBe(true);
  });

  it("accepts an explicitly trusted local or proxy origin", () => {
    expect(
      isTrustedSameOrigin(
        request("http://localhost:3001"),
        true,
        "https://chiron.example.com",
        "http://localhost:3001, http://127.0.0.1:3001",
      ),
    ).toBe(true);
  });

  it("rejects a different origin", () => {
    expect(
      isTrustedSameOrigin(
        request("https://attacker.example"),
        true,
        "https://chiron.example.com",
      ),
    ).toBe(false);
  });

  it("requires Origin in production", () => {
    expect(isTrustedSameOrigin(request(), true, "https://chiron.example.com")).toBe(false);
    expect(isTrustedSameOrigin(request(), false)).toBe(true);
  });
});
