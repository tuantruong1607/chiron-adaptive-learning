import { NextResponse } from "next/server";

import { authenticatedApiFetch, isSameOriginMutation } from "@/lib/server-auth";

export async function POST(
  request: Request,
  { params }: { params: Promise<{ essayId: string }> },
) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const { essayId } = await params;
  let payload: unknown;
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json(
      { error: "Invalid JSON payload" },
      { status: 400 },
    );
  }
  const upstream = await authenticatedApiFetch(
    `/api/v1/essays/${essayId}/review`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    },
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Essay review failed" }));
  return NextResponse.json(body, { status: upstream.status });
}
