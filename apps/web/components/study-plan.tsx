import {
  ArrowRight,
  BookOpen,
  Flask,
  Timer,
} from "@phosphor-icons/react/dist/ssr";
import type { StudyPlan as StudyPlanType } from "@chiron/domain";
import Link from "next/link";

const labByConcept: Record<string, string> = {
  chunking: "chunking-strategy",
  rrf: "rrf-ranking",
  reciprocal_rank_fusion: "rrf-ranking",
  "metadata-filtering": "metadata-filtering",
  metadata_filtering: "metadata-filtering",
  evaluation: "rag-evaluation",
  rag_evaluation: "rag-evaluation",
  "graph-routing": "graph-lite-routing",
  multi_hop_retrieval: "graph-lite-routing",
  dense: "hybrid-search",
  sparse: "hybrid-search",
};

function activityHref(activity: string, conceptId: string) {
  if (activity === "lab")
    return `/labs/${labByConcept[conceptId] ?? "hybrid-search"}`;
  if (activity === "lesson")
    return `/learn?concept=${encodeURIComponent(conceptId)}`;
  if (activity === "recheck") return "/diagnostic";
  return `/map?concept=${encodeURIComponent(conceptId)}`;
}

export function StudyPlan({ plan }: { plan: StudyPlanType }) {
  return (
    <section className="plan-panel" aria-labelledby="plan-title">
      <div className="panel-heading">
        <div>
          <span>Kế hoạch hôm nay</span>
          <h2 id="plan-title">{plan.title}</h2>
        </div>
        <p>
          <Timer size={18} aria-hidden="true" /> {plan.totalMinutes} phút
        </p>
      </div>
      <div className="plan-timeline">
        {plan.items.map((item, index) => (
          <Link
            href={activityHref(item.activity, item.conceptId)}
            className="plan-item"
            key={item.id}
          >
            <span className="plan-index">
              {String(index + 1).padStart(2, "0")}
            </span>
            <div className="plan-copy">
              <span>
                {item.activity === "lab" ? (
                  <Flask size={16} aria-hidden="true" />
                ) : (
                  <BookOpen size={16} aria-hidden="true" />
                )}{" "}
                {item.durationMinutes} phút
              </span>
              <h3>{item.title}</h3>
              <p>{item.reason}</p>
            </div>
            <div className="plan-gain">
              <span>Kỳ vọng</span>
              <strong>+{Math.round(item.expectedGain * 100)} mastery</strong>
            </div>
            <ArrowRight className="plan-arrow" size={20} aria-hidden="true" />
          </Link>
        ))}
      </div>
    </section>
  );
}
