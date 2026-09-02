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
  const response = await backendTokenRequest("/api/v1/auth/register", {
    tenant_slug: payload.tenantSlug || "chiron-demo",
    email: payload.email,
    password: payload.password,
    display_name: payload.displayName || null,
  });
  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    return NextResponse.json(
      { error: errorBody.detail || "Không thể tạo tài khoản lúc này." },
      { status: response.status },
    );
  }
  const pair = await response.json();
  await storeTokenPair(pair);
  return NextResponse.json({ authenticated: true });
}
