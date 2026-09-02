"use client";

import {
  ArrowUpRight,
  CalendarBlank,
  Gauge,
  Target,
} from "@phosphor-icons/react";
import type { StudyPlan as StudyPlanType } from "@chiron/domain";
import Link from "next/link";
import { useEffect, useState } from "react";
import { demoPlan } from "@/lib/demo-data";
import { StudyPlan } from "./study-plan";
import { LearningResourceRail } from "./learning-resource";

export function LearnDashboard() {
  const [plan, setPlan] = useState<StudyPlanType>(demoPlan);
  const [live, setLive] = useState(false);
  const [focusConcept, setFocusConcept] = useState<string | undefined>();
  useEffect(() => {
    setFocusConcept(
      new URLSearchParams(window.location.search).get("concept") ?? undefined,
    );
    fetch("/api/study-plan", { cache: "no-store" })
      .then(async (response) => {
        if (response.status === 401) window.location.assign("/login");
        if (!response.ok) throw new Error("study plan unavailable");
        return response.json();
      })
      .then((payload) => {
        setPlan(payload);
        setLive(true);
      })
      .catch(() => setLive(false));
  }, []);
  return (
    <main className="product-page dashboard-page">
      <header className="product-header">
        <div>
          <p>Bước 3/3 · {live ? "Đã đồng bộ mastery" : "Đang đồng bộ"}</p>
          <h1>Học đúng phần đang cản bạn</h1>
        </div>
        <Link className="button button-secondary" href="/diagnostic">
          Làm diagnostic
        </Link>
      </header>
      <section className="signal-band" aria-label="Tóm tắt tiến độ">
        <div>
          <CalendarBlank size={21} aria-hidden="true" />
          <span>Còn lại</span>
          <strong>19 ngày</strong>
        </div>
        <div>
          <Gauge size={21} aria-hidden="true" />
          <span>Persistence</span>
          <strong>{live ? "PostgreSQL" : "Đang kết nối"}</strong>
        </div>
        <div>
          <Target size={21} aria-hidden="true" />
          <span>Concept ưu tiên</span>
          <strong>RAG evaluation</strong>
        </div>
        <Link href="/map">
          Mở bản đồ <ArrowUpRight size={18} aria-hidden="true" />
        </Link>
      </section>
      <div className="dashboard-grid">
        <StudyPlan plan={plan} />
        <aside className="insight-panel">
          <span>Chiron nhận thấy</span>
          <h2>Bạn hiểu retrieval, nhưng chưa biết cách chứng minh nó tốt.</h2>
          <p>
            Hai câu sai gần nhất cùng quay về evaluation design. Học lại RRF
            không phải ưu tiên cao nhất lúc này.
          </p>
          <Link href="/map">
            Xem chuỗi nguyên nhân <ArrowUpRight size={18} aria-hidden="true" />
          </Link>
        </aside>
      </div>
      <LearningResourceRail
        preferredConceptId={focusConcept ?? plan.items[0]?.conceptId}
      />
    </main>
  );
}
