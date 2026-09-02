import { NextResponse } from "next/server";

import { authenticatedApiFetch } from "@/lib/server-auth";

type RawCitation = {
  source_span_id: string;
  title: string;
  locator: string;
  excerpt: string;
};

type RawLearningResource = {
  concept_id: string;
  title: string;
  why_it_matters: string;
  estimated_minutes: number;
  learning_outcome: string;
  key_ideas: string[];
  worked_example: unknown[];
  common_mistakes: string[];
  retrieval_prompt: string;
  citations?: RawCitation[];
};

function mapLearningResource(raw: RawLearningResource | null | undefined) {
  if (!raw) return null;
  return {
    conceptId: raw.concept_id,
    title: raw.title,
    whyItMatters: raw.why_it_matters,
    estimatedMinutes: raw.estimated_minutes,
    learningOutcome: raw.learning_outcome,
    keyIdeas: raw.key_ideas,
    workedExample: raw.worked_example,
    commonMistakes: raw.common_mistakes,
    retrievalPrompt: raw.retrieval_prompt,
    citations: raw.citations?.map((citation) => ({
      sourceSpanId: citation.source_span_id,
      title: citation.title,
      locator: citation.locator,
      excerpt: citation.excerpt,
    })),
  };
}

export async function GET() {
  const upstream = await authenticatedApiFetch("/api/v1/labs");
  const body = await upstream
    .json()
    .catch(() => ({ error: "Lab catalogue unavailable" }));
  if (!upstream.ok) return NextResponse.json(body, { status: upstream.status });
  return NextResponse.json(
    (body as Array<Record<string, unknown>>).map((lab) => ({
      id: lab.id,
      title: lab.title,
      objective: lab.objective,
      brief: lab.brief,
      estimatedMinutes: lab.estimated_minutes,
      successThreshold: lab.success_threshold,
      conceptId: lab.concept_id,
      sourceSpanIds: lab.source_span_ids,
      scenario: lab.scenario,
      learningResourceId: lab.learning_resource_id,
      learningResource: mapLearningResource(
        lab.learning_resource as RawLearningResource | null,
      ),
      controls: (lab.controls as Array<Record<string, unknown>>).map(
        (control) => ({
          id: control.id,
          label: control.label,
          kind: control.kind,
          defaultValue: control.default,
          minimum: control.minimum,
          maximum: control.maximum,
          step: control.step,
          options: control.options,
          helpText: control.help_text,
        }),
      ),
      transferPrompts: (
        lab.transfer_prompts as Array<Record<string, unknown>>
      ).map((prompt) => ({
        id: prompt.id,
        prompt: prompt.prompt,
        placeholder: prompt.placeholder,
        minLength: prompt.min_length,
      })),
    })),
  );
}
