"use client";

import { ArrowRight, LockKey } from "@phosphor-icons/react";
import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

export function LoginForm({
  authMode = "local",
}: {
  authMode?: "local" | "oidc" | "hybrid";
}) {
  const router = useRouter();
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError("");
    const form = new FormData(event.currentTarget);
    const response = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        tenantSlug: form.get("tenantSlug"),
        email: form.get("email"),
        password: form.get("password"),
      }),
    });
    if (!response.ok) {
      const payload = await response.json().catch(() => ({}));
      setError(payload.error ?? "Không thể đăng nhập lúc này.");
      setLoading(false);
      return;
    }
    router.replace("/learn");
    router.refresh();
  }

  return (
    <form className="login-form" onSubmit={submit}>
      <div className="login-lock">
        <LockKey size={22} />
      </div>
      {authMode !== "local" && (
        <a className="button button-primary" href="/api/auth/oidc/start">
          Đăng nhập với Identity Provider <ArrowRight size={18} />
        </a>
      )}
      {authMode !== "oidc" && (
        <>
          <label>
            Không gian học
            <input name="tenantSlug" defaultValue="chiron-demo" required />
          </label>
          <label>
            Email
            <input
              name="email"
              type="email"
              defaultValue="learner@chiron.local"
              required
            />
          </label>
          <label>
            Mật khẩu
            <input
              name="password"
              type="password"
              defaultValue="chiron-demo-2026"
              minLength={8}
              required
            />
          </label>
          {error && (
            <p role="alert" className="login-error">
              {error}
            </p>
          )}
          <button className="button button-primary" disabled={loading}>
            {loading ? "Đang xác thực" : "Vào phiên học"}{" "}
            <ArrowRight size={18} />
          </button>
          <small>
            Phiên đăng nhập được giữ bằng HttpOnly cookie và tự động refresh.
          </small>
        </>
      )}
    </form>
  );
}
