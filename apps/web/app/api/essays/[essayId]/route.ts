import { NextResponse } from "next/server";

import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET(
  _request: Request,
  { params }: { params: Promise<{ essayId: string }> },
) {
  const { essayId } = await params;
  const upstream = await authenticatedApiFetch(`/api/v1/essays/${essayId}`);
  const body = await upstream
    .json()
    .catch(() => ({ error: "Essay lookup failed" }));
  return NextResponse.json(body, { status: upstream.status });
}
