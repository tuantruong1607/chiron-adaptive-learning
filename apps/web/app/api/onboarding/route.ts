import { NextResponse } from "next/server";

import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET() {
  const upstream = await authenticatedApiFetch(
    "/api/v1/courses/rag-intensive/diagnostic/status",
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Onboarding status unavailable" }));
  return NextResponse.json(body, { status: upstream.status });
}
