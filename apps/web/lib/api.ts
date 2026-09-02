import type { KnowledgeMap, SourceLocator, StudyPlan } from "@chiron/domain";

type UpstreamCitation = {
  source_span_id: string;
  title: string;
  locator: string;
  excerpt: string;
};

type UpstreamKnowledgeMap = {
  course_id: string;
  version: string;
  nodes: Array<{
    id: string;
    name: string;
    summary: string;
    objective: string;
    mastery: number;
    confidence: number;
    exam_weight: number;
    band: "new" | "developing" | "secure" | "mastered";
    x: number;
    y: number;
    citations: UpstreamCitation[];
  }>;
  edges: Array<{
    id: string;
    source: string;
    target: string;
    relation: "prerequisite_of" | "part_of" | "contrasts_with" | "applies_to" | "causes";
    weight: number;
  }>;
};

export function toKnowledgeMap(data: UpstreamKnowledgeMap): KnowledgeMap {
  return {
    courseId: data.course_id,
    version: data.version,
    nodes: data.nodes.map((node) => ({
      id: node.id,
      name: node.name,
      summary: node.summary,
      objective: node.objective,
      mastery: node.mastery,
      confidence: node.confidence,
      examWeight: node.exam_weight,
      band: node.band,
      x: node.x,
      y: node.y,
      citations: node.citations.map((citation) => ({
        sourceSpanId: citation.source_span_id,
        title: citation.title,
        locator: citation.locator,
        excerpt: citation.excerpt,
      })),
    })),
    edges: data.edges,
  };
}

type UpstreamSourceLocator = UpstreamCitation & {
  source_type: string;
  locator_kind: string;
  label: string | null;
  page: number | null;
  section_title: string | null;
  heading: string | null;
  section_id: string | null;
  source_file: string | null;
  order: number | null;
  extraction_method: string | null;
};

export function toSourceLocator(data: UpstreamSourceLocator): SourceLocator {
  return {
    sourceSpanId: data.source_span_id,
    title: data.title,
    locator: data.locator,
    excerpt: data.excerpt,
    sourceType: data.source_type,
    locatorKind: data.locator_kind,
    label: data.label,
    page: data.page,
    sectionTitle: data.section_title,
    heading: data.heading,
    sectionId: data.section_id,
    sourceFile: data.source_file,
    order: data.order,
    extractionMethod: data.extraction_method,
  };
}

type UpstreamPlanItem = {
  id: string;
  concept_id: string;
  title: string;
  activity: "lesson" | "retrieval" | "lab" | "recheck";
  duration_minutes: number;
  reason: string;
  expected_gain: number;
};

type UpstreamStudyPlan = {
  id: string;
  title: string;
  total_minutes: number;
  generated_at: string;
  items: UpstreamPlanItem[];
};

export function toStudyPlan(data: UpstreamStudyPlan): StudyPlan {
  return {
    id: data.id,
    title: data.title,
    totalMinutes: data.total_minutes,
    generatedAt: data.generated_at,
    items: data.items.map((item) => ({
      id: item.id,
      conceptId: item.concept_id,
      title: item.title,
      activity: item.activity,
      durationMinutes: item.duration_minutes,
      reason: item.reason,
      expectedGain: item.expected_gain,
    })),
  };
}
