export type MasteryBand = "new" | "developing" | "secure" | "mastered";
export type RelationType =
  | "prerequisite_of"
  | "part_of"
  | "contrasts_with"
  | "applies_to"
  | "causes";

export interface SourceCitation {
  sourceSpanId: string;
  title: string;
  locator: string;
  excerpt: string;
}

export interface SourceLocator extends SourceCitation {
  sourceType: string;
  locatorKind: string;
  label: string | null;
  page: number | null;
  sectionTitle: string | null;
  heading: string | null;
  sectionId: string | null;
  sourceFile: string | null;
  order: number | null;
  extractionMethod: string | null;
}

export interface ConceptNode {
  id: string;
  name: string;
  summary: string;
  objective: string;
  mastery: number;
  confidence: number;
  examWeight: number;
  band: MasteryBand;
  x: number;
  y: number;
  citations: SourceCitation[];
}

export interface ConceptEdge {
  id: string;
  source: string;
  target: string;
  relation: RelationType;
  weight: number;
}

export interface KnowledgeMap {
  courseId: string;
  version: string;
  nodes: ConceptNode[];
  edges: ConceptEdge[];
}

export interface LearningResourceStep {
  title: string;
  explanation: string;
  example: string;
}

export interface LearningResource {
  conceptId: string;
  title: string;
  whyItMatters: string;
  estimatedMinutes: number;
  learningOutcome: string;
  keyIdeas: string[];
  workedExample: LearningResourceStep[];
  commonMistakes: string[];
  retrievalPrompt: string;
  citations: SourceCitation[];
}

export interface DiagnosticQuestion {
  id: string;
  conceptId: string;
  prompt: string;
  options: { id: string; text: string }[];
}

export interface StudyPlanItem {
  id: string;
  conceptId: string;
  title: string;
  activity: "lesson" | "retrieval" | "lab" | "recheck";
  durationMinutes: number;
  reason: string;
  expectedGain: number;
}

export interface StudyPlan {
  id: string;
  title: string;
  totalMinutes: number;
  generatedAt: string;
  items: StudyPlanItem[];
}

export interface TutorAnswer {
  answer: string;
  confidence: number;
  citations: SourceCitation[];
  traceId: string;
  refused: boolean;
}
