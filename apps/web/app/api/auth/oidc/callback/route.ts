import { cookies } from "next/headers";
import { NextResponse } from "next/server";

import { storeTokenPair } from "@/lib/server-auth";

export async function GET(request: Request) {
  const url = new URL(request.url);
  const jar = await cookies();
  const state = url.searchParams.get("state");
  const expectedState = jar.get("chiron_oidc_state")?.value;
  const verifier = jar.get("chiron_oidc_verifier")?.value;
  jar.delete("chiron_oidc_state");
  jar.delete("chiron_oidc_verifier");
  if (!state || !expectedState || state !== expectedState || !verifier)
    return NextResponse.json({ error: "Invalid OIDC state" }, { status: 400 });

  const code = url.searchParams.get("code");
  const tokenUrl = process.env.OIDC_TOKEN_URL;
  const clientId = process.env.OIDC_CLIENT_ID;
  if (!code || !tokenUrl || !clientId)
    return NextResponse.json(
      { error: "Incomplete OIDC callback" },
      { status: 400 },
    );

  const redirectUri =
    process.env.OIDC_REDIRECT_URI ?? `${url.origin}/api/auth/oidc/callback`;
  const body = new URLSearchParams({
    grant_type: "authorization_code",
    code,
    client_id: clientId,
    redirect_uri: redirectUri,
    code_verifier: verifier,
  });
  if (process.env.OIDC_CLIENT_SECRET)
    body.set("client_secret", process.env.OIDC_CLIENT_SECRET);
  const response = await fetch(tokenUrl, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
    cache: "no-store",
  });
  if (!response.ok)
    return NextResponse.json(
      { error: "OIDC token exchange failed" },
      { status: 401 },
    );
  const payload = await response.json();
  if (!payload.access_token)
    return NextResponse.json(
      { error: "OIDC access token missing" },
      { status: 401 },
    );
  await storeTokenPair(
    {
      access_token: payload.access_token,
      refresh_token: payload.refresh_token,
      expires_in: payload.expires_in ?? 3600,
      refresh_expires_in: payload.refresh_expires_in,
      token_type: "bearer",
    },
    "oidc",
  );
  return NextResponse.redirect(new URL("/learn", url.origin));
}
