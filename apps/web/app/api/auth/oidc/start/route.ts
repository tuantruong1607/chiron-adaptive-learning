import { createHash, randomBytes } from "node:crypto";

import { cookies } from "next/headers";
import { NextResponse } from "next/server";

const secure = process.env.NODE_ENV === "production";

function base64url(value: Buffer) {
  return value.toString("base64url");
}

export async function GET(request: Request) {
  const authorizationUrl = process.env.OIDC_AUTHORIZATION_URL;
  const clientId = process.env.OIDC_CLIENT_ID;
  if (!authorizationUrl || !clientId)
    return NextResponse.json(
      { error: "OIDC is not configured" },
      { status: 503 },
    );

  const origin = new URL(request.url).origin;
  const redirectUri =
    process.env.OIDC_REDIRECT_URI ?? `${origin}/api/auth/oidc/callback`;
  const state = base64url(randomBytes(32));
  const verifier = base64url(randomBytes(64));
  const challenge = base64url(createHash("sha256").update(verifier).digest());
  const jar = await cookies();
  const cookieOptions = {
    httpOnly: true,
    sameSite: "lax" as const,
    secure,
    path: "/",
    maxAge: 600,
  };
  jar.set("chiron_oidc_state", state, cookieOptions);
  jar.set("chiron_oidc_verifier", verifier, cookieOptions);

  const target = new URL(authorizationUrl);
  target.searchParams.set("response_type", "code");
  target.searchParams.set("client_id", clientId);
  target.searchParams.set("redirect_uri", redirectUri);
  target.searchParams.set(
    "scope",
    process.env.OIDC_SCOPE ?? "openid profile email offline_access",
  );
  target.searchParams.set("state", state);
  target.searchParams.set("code_challenge", challenge);
  target.searchParams.set("code_challenge_method", "S256");
  if (process.env.OIDC_AUDIENCE)
    target.searchParams.set("audience", process.env.OIDC_AUDIENCE);
  return NextResponse.redirect(target);
}
