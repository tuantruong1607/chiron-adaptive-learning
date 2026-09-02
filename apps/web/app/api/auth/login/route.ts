import { NextResponse } from "next/server";
import {
  backendTokenRequest,
  isSameOriginMutation,
  storeTokenPair,
} from "@/lib/server-auth";

export async function POST(request: Request) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const payload = await request.json();
  const response = await backendTokenRequest("/api/v1/auth/token", {
    tenant_slug: payload.tenantSlug,
    email: payload.email,
    password: payload.password,
  });
  if (!response.ok) {
    return NextResponse.json(
      { error: "Tenant, email hoặc mật khẩu không đúng." },
      { status: 401 },
    );
  }
  const pair = await response.json();
  await storeTokenPair(pair);
  return NextResponse.json({ authenticated: true });
}
