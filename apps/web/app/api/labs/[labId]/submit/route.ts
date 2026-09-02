import { NextResponse } from "next/server";

import { authenticatedApiFetch, isSameOriginMutation } from "@/lib/server-auth";

export async function POST(
  request: Request,
  { params }: { params: Promise<{ labId: string }> },
) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const { labId } = await params;
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
    `/api/v1/labs/${encodeURIComponent(labId)}/submit`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Idempotency-Key":
          request.headers.get("Idempotency-Key") ?? crypto.randomUUID(),
      },
      body: JSON.stringify(payload),
    },
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Lab submission failed" }));
  return NextResponse.json(body, { status: upstream.status });
}
