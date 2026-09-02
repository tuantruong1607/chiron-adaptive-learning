type RequestOriginInput = Pick<Request, "headers" | "url">;

export function isTrustedSameOrigin(
  request: RequestOriginInput,
  production: boolean,
  configuredBaseUrl?: string,
  configuredTrustedOrigins?: string,
) {
  const origin = request.headers.get("origin");
  if (!origin) return !production;
  try {
    const trustedOrigins = [
      configuredBaseUrl,
      ...(configuredTrustedOrigins?.split(",") ?? []),
    ]
      .map((value) => value?.trim())
      .filter((value): value is string => Boolean(value))
      .map((value) => new URL(value).origin);
    if (trustedOrigins.length === 0) {
      trustedOrigins.push(new URL(request.url).origin);
    }
    return trustedOrigins.includes(new URL(origin).origin);
  } catch {
    return false;
  }
}
