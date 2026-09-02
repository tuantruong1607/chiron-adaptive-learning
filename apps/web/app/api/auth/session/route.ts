import { NextResponse } from "next/server";
import { authenticatedApiFetch } from "@/lib/server-auth";

export async function GET() {
  const response = await authenticatedApiFetch("/api/v1/auth/me");
  if (!response.ok)
    return NextResponse.json({ authenticated: false }, { status: 401 });
  return NextResponse.json({
    authenticated: true,
    principal: await response.json(),
  });
}
