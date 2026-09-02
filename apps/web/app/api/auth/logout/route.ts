import { cookies } from "next/headers";
import { NextResponse } from "next/server";
import {
  backendTokenRequest,
  clearSessionCookies,
  isSameOriginMutation,
  REFRESH_COOKIE,
} from "@/lib/server-auth";

export async function POST(request: Request) {
  if (!isSameOriginMutation(request)) {
    return NextResponse.json({ error: "Invalid origin" }, { status: 403 });
  }
  const refreshToken = (await cookies()).get(REFRESH_COOKIE)?.value;
  if (refreshToken) {
    await backendTokenRequest("/api/v1/auth/logout", {
      refresh_token: refreshToken,
    });
  }
  await clearSessionCookies();
  return NextResponse.json({ authenticated: false });
}
