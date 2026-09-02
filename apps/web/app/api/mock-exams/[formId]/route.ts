import { NextResponse } from "next/server";

import { authenticatedApiFetch, isSameOriginMutation } from "@/lib/server-auth";

export async function GET(
  _request: Request,
  { params }: { params: Promise<{ formId: string }> },
) {
  const { formId } = await params;
  const upstream = await authenticatedApiFetch(
    `/api/v1/mock-exams/${encodeURIComponent(formId)}`,
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Mock exam unavailable" }));
  return NextResponse.json(body, { status: upstream.status });
}

export async function POST(
  request: Request,
  { params }: { params: Promise<{ formId: string }> },
) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const { formId } = await params;
  const payload = await request.json();
  const upstream = await authenticatedApiFetch(
    `/api/v1/mock-exams/${encodeURIComponent(formId)}/grade`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    },
  );
  const body = await upstream
    .json()
    .catch(() => ({ error: "Mock exam grading failed" }));
  return NextResponse.json(body, { status: upstream.status });
}
