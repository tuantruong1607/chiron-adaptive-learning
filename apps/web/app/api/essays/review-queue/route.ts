import { NextResponse } from "next/server";

import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET() {
  const upstream = await authenticatedApiFetch("/api/v1/essays/review-queue");
  const body = await upstream
    .json()
    .catch(() => ({ error: "Review queue unavailable" }));
  return NextResponse.json(body, { status: upstream.status });
}
