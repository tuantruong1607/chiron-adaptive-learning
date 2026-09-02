import { NextResponse } from "next/server";
import { authenticatedApiFetch, isSameOriginMutation } from "@/lib/server-auth";

export async function GET() {
  const upstream = await authenticatedApiFetch(
    "/api/v1/courses/rag-intensive/diagnostic",
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Diagnostic unavailable" }));
  return NextResponse.json(body, { status: upstream.status });
}

export async function POST(request: Request) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const payload = await request.json();
  const upstream = await authenticatedApiFetch(
    "/api/v1/courses/rag-intensive/diagnostic/submit",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Idempotency-Key":
          request.headers.get("Idempotency-Key") ?? crypto.randomUUID(),
      },
      body: JSON.stringify({
        answers: payload.answers.map(
          (answer: { questionId: string; optionId: string }) => ({
            question_id: answer.questionId,
            option_id: answer.optionId,
          }),
        ),
      }),
    },
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Diagnostic request failed" }));
  return NextResponse.json(body, { status: upstream.status });
}
