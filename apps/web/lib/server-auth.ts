import "server-only";

import { cookies } from "next/headers";

import { isTrustedSameOrigin } from "@/lib/request-origin";

export const ACCESS_COOKIE = "chiron_access";
export const REFRESH_COOKIE = "chiron_refresh";
export const AUTH_SOURCE_COOKIE = "chiron_auth_source";

type TokenPair = {
  access_token: string;
  refresh_token?: string;
  expires_in: number;
  refresh_expires_in?: number;
  token_type: "bearer";
};

const apiUrl = process.env.API_BASE_URL ?? "http://localhost:8000";
// The standalone Next image is built with NODE_ENV=production even for the
// local Docker profile. Derive cookie transport security from the actual URL
// so HTTP localhost sessions work while HTTPS production sessions stay Secure.
const secure = process.env.WEB_BASE_URL?.startsWith("https://") ?? false;
const refreshFlights = new Map<string, Promise<TokenPair | null>>();

export async function storeTokenPair(pair: TokenPair, authSource: "local" | "oidc" = "local") {
  const jar = await cookies();
  jar.set(ACCESS_COOKIE, pair.access_token, {
    httpOnly: true,
    sameSite: "lax",
    secure,
    path: "/",
    maxAge: pair.expires_in,
  });
  if (pair.refresh_token) {
    jar.set(REFRESH_COOKIE, pair.refresh_token, {
      httpOnly: true,
      sameSite: "lax",
      secure,
      path: "/",
      maxAge: pair.refresh_expires_in ?? 14 * 24 * 60 * 60,
    });
  }
  jar.set(AUTH_SOURCE_COOKIE, authSource, {
    httpOnly: true,
    sameSite: "lax",
    secure,
    path: "/",
    maxAge: pair.refresh_expires_in ?? 14 * 24 * 60 * 60,
  });
}

export async function clearSessionCookies() {
  const jar = await cookies();
  jar.delete(ACCESS_COOKIE);
  jar.delete(REFRESH_COOKIE);
  jar.delete(AUTH_SOURCE_COOKIE);
}

export async function backendTokenRequest(
  path: string,
  body: unknown,
): Promise<Response> {
  return fetch(`${apiUrl}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
    cache: "no-store",
  });
}

async function refreshAccessToken(): Promise<string | null> {
  const jar = await cookies();
  const refreshToken = jar.get(REFRESH_COOKIE)?.value;
  const authSource = jar.get(AUTH_SOURCE_COOKIE)?.value;
  if (!refreshToken) return null;
  let flight = refreshFlights.get(refreshToken);
  if (!flight) {
    const request = authSource === "oidc" || process.env.AUTH_MODE === "oidc"
      ? refreshOidcToken(refreshToken)
      : backendTokenRequest("/api/v1/auth/refresh", { refresh_token: refreshToken });
    flight = request.then(async (response) =>
      response.ok ? ((await response.json()) as TokenPair) : null,
    );
    refreshFlights.set(refreshToken, flight);
  }
  let pair: TokenPair | null;
  try {
    pair = await flight;
  } finally {
    if (refreshFlights.get(refreshToken) === flight)
      refreshFlights.delete(refreshToken);
  }
  if (!pair) {
    await clearSessionCookies();
    return null;
  }
  await storeTokenPair(pair, authSource === "oidc" ? "oidc" : "local");
  return pair.access_token;
}

async function refreshOidcToken(refreshToken: string): Promise<Response> {
  const tokenUrl = process.env.OIDC_TOKEN_URL;
  const clientId = process.env.OIDC_CLIENT_ID;
  if (!tokenUrl || !clientId) return new Response(null, { status: 503 });
  const body = new URLSearchParams({
    grant_type: "refresh_token",
    refresh_token: refreshToken,
    client_id: clientId,
  });
  if (process.env.OIDC_CLIENT_SECRET)
    body.set("client_secret", process.env.OIDC_CLIENT_SECRET);
  const response = await fetch(tokenUrl, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
    cache: "no-store",
  });
  if (!response.ok) return response;
  const payload = await response.json();
  return Response.json({
    ...payload,
    refresh_token: payload.refresh_token ?? refreshToken,
    refresh_expires_in: payload.refresh_expires_in ?? 14 * 24 * 60 * 60,
  });
}

export async function authenticatedApiFetch(
  path: string,
  init: RequestInit = {},
) {
  const jar = await cookies();
  let accessToken = jar.get(ACCESS_COOKIE)?.value ?? null;
  if (!accessToken) accessToken = await refreshAccessToken();
  if (!accessToken)
    return new Response("Authentication required", { status: 401 });

  const send = (token: string) =>
    fetch(`${apiUrl}${path}`, {
      ...init,
      headers: {
        ...Object.fromEntries(new Headers(init.headers).entries()),
        Authorization: `Bearer ${token}`,
      },
      cache: "no-store",
    });
  let response = await send(accessToken);
  if (response.status === 401) {
    accessToken = await refreshAccessToken();
    if (!accessToken) return response;
    response = await send(accessToken);
  }
  return response;
}

export function isSameOriginMutation(request: Request) {
  return isTrustedSameOrigin(
    request,
    process.env.NODE_ENV === "production",
    process.env.WEB_BASE_URL,
    process.env.WEB_TRUSTED_ORIGINS,
  );
}
