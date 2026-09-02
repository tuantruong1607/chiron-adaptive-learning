import { NextResponse } from "next/server";
import { authenticatedApiFetch, isSameOriginMutation } from "@/lib/server-auth";

export async function POST(request: Request) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const response = await authenticatedApiFetch("/api/v1/auth/me");
  return NextResponse.json(
    response.ok ? { refreshed: true } : { refreshed: false },
    { status: response.ok ? 200 : 401 },
  );
}
