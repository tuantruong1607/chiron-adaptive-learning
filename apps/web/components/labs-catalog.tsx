"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

type Lab = {
  id: string;
  title: string;
  objective: string;
  brief: string;
  estimatedMinutes: number;
  successThreshold: number;
  conceptId: string;
  sourceSpanIds: string[];
  scenario: string;
};

export function LabsCatalog() {
  const [labs, setLabs] = useState<Lab[]>([]);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    fetch("/api/labs", { cache: "no-store" })
      .then(async (response) => {
        if (!response.ok) throw new Error("Không thể tải catalogue lab.");
        return (await response.json()) as Lab[];
      })
      .then(setLabs)
      .catch((reason: Error) => setError(reason.message));
  }, []);

  if (error) return <div className="glass-surface catalog-state">{error}</div>;
  if (!labs.length)
    return (
      <div className="glass-surface catalog-state">Đang tải practice labs…</div>
    );
  return (
    <section className="labs-grid" aria-label="Practice lab catalogue">
      {labs.map((lab) => {
        return (
          <article className="glass-surface lab-card" key={lab.id}>
            <div className="lab-card-top">
              <span>{lab.estimatedMinutes} phút</span>
              <span>{lab.successThreshold}% pass</span>
            </div>
            <p className="eyebrow">{lab.conceptId}</p>
            <h2>{lab.title}</h2>
            <p>{lab.brief}</p>
            <small>Grounding: {lab.sourceSpanIds.join(", ")}</small>
            <Link className="button button-primary" href={`/labs/${lab.id}`}>
              Mở lab <span aria-hidden="true">→</span>
            </Link>
          </article>
        );
      })}
    </section>
  );
}
