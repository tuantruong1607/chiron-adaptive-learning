"use client";

import { useEffect, useState } from "react";

import { EssayEditor } from "./essay-editor";
import { EssayReviewQueue } from "./essay-review-queue";

export function EssayWorkspace() {
  const [role, setRole] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/auth/session", { cache: "no-store" })
      .then((response) => response.json())
      .then((payload) => setRole(payload.principal?.role ?? "learner"))
      .catch(() => setRole("learner"));
  }, []);

  if (role === null) {
    return (
      <div className="glass-surface catalog-state">Đang tải workspace…</div>
    );
  }
  return role === "instructor" || role === "admin" ? (
    <EssayReviewQueue />
  ) : (
    <EssayEditor />
  );
}
