import { NextResponse } from "next/server";
import { authenticatedApiFetch, isSameOriginMutation } from "@/lib/server-auth";

export async function POST(request: Request) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }

  let payload: {
    denseWeight: number;
    sparseWeight: number;
    rerankDepth: number;
    tenantFilter: boolean;
    transferAnswer: string;
  };
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json(
      { error: "Invalid JSON payload" },
      { status: 400 },
    );
  }

  const upstream = await authenticatedApiFetch(
    "/api/v1/labs/hybrid-search/submit",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Idempotency-Key":
          request.headers.get("Idempotency-Key") ?? crypto.randomUUID(),
      },
      body: JSON.stringify({
        dense_weight: payload.denseWeight,
        sparse_weight: payload.sparseWeight,
        rerank_depth: payload.rerankDepth,
        tenant_filter: payload.tenantFilter,
        transfer_answer: payload.transferAnswer,
      }),
    },
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Lab submission failed" }));
  return NextResponse.json(body, { status: upstream.status });
}
