import { NextResponse } from "next/server";
import { authenticatedApiFetch, isSameOriginMutation } from "@/lib/server-auth";

export async function POST(request: Request) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const payload = await request.json();
  const upstream = await authenticatedApiFetch("/api/v1/tutor", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Idempotency-Key":
        request.headers.get("Idempotency-Key") ?? crypto.randomUUID(),
    },
    body: JSON.stringify({
      question: payload.question,
      thread_id: payload.threadId ?? null,
      course: "rag-intensive",
      data_sensitivity: "private",
    }),
  });
  const body = await upstream
    .json()
    .catch(() => ({ error: "Tutor request failed" }));
  return NextResponse.json(body, { status: upstream.status });
}
