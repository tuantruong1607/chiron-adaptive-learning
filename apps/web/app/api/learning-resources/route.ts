import { NextResponse } from "next/server";

import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET() {
  const upstream = await authenticatedApiFetch(
    "/api/v1/courses/rag-intensive/learning-resources",
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Learning resources unavailable" }));
  if (!upstream.ok) return NextResponse.json(body, { status: upstream.status });
  return NextResponse.json(body);
}
