import { NextRequest, NextResponse } from "next/server";

const protectedPrefixes = [
  "/learn",
  "/map",
  "/diagnostic",
  "/exams",
  "/labs",
  "/essays",
];

export function middleware(request: NextRequest) {
  const protectedRoute = protectedPrefixes.some((prefix) =>
    request.nextUrl.pathname.startsWith(prefix),
  );
  if (!protectedRoute) return NextResponse.next();
  const hasSession =
    request.cookies.has("chiron_access") ||
    request.cookies.has("chiron_refresh");
  if (hasSession) return NextResponse.next();
  const login = new URL("/login", request.url);
  login.searchParams.set("next", request.nextUrl.pathname);
  return NextResponse.redirect(login);
}

export const config = {
  matcher: [
    "/learn/:path*",
    "/map/:path*",
    "/diagnostic/:path*",
    "/exams/:path*",
    "/labs/:path*",
    "/essays/:path*",
  ],
};
