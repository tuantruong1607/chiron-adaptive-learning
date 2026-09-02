"use client";

import { ArrowRight, LockKey, SignIn, Sparkle, UserPlus } from "@phosphor-icons/react";
import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

export function LoginForm({
  authMode = "local",
}: {
  authMode?: "local" | "oidc" | "hybrid";
}) {
  const router = useRouter();
  const [tab, setTab] = useState<"login" | "register">("login");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleLogin(event: FormEvent<HTMLFormElement>) {
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

  async function handleRegister(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError("");
    const form = new FormData(event.currentTarget);
    const password = String(form.get("password") ?? "");
    const confirmPassword = String(form.get("confirmPassword") ?? "");

    if (password !== confirmPassword) {
      setError("Mật khẩu xác nhận không khớp.");
      setLoading(false);
      return;
    }

    if (password.length < 8) {
      setError("Mật khẩu phải có ít nhất 8 ký tự.");
      setLoading(false);
      return;
    }

    const response = await fetch("/api/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        displayName: form.get("displayName"),
        email: form.get("email"),
        password,
        tenantSlug: form.get("tenantSlug") || "chiron-demo",
      }),
    });

    if (!response.ok) {
      const payload = await response.json().catch(() => ({}));
      setError(payload.error ?? "Không thể đăng ký lúc này.");
      setLoading(false);
      return;
    }

    // New users start with diagnostic evaluation
    router.replace("/diagnostic");
    router.refresh();
  }

  return (
    <div className="login-form-container">
      {authMode !== "oidc" && (
        <div className="auth-tabs" role="tablist" aria-label="Chế độ xác thực">
          <button
            type="button"
            role="tab"
            aria-selected={tab === "login"}
            className={`auth-tab ${tab === "login" ? "active" : ""}`}
            onClick={() => {
              setTab("login");
              setError("");
            }}
          >
            <SignIn size={16} /> Đăng nhập
          </button>
          <button
            type="button"
            role="tab"
            aria-selected={tab === "register"}
            className={`auth-tab ${tab === "register" ? "active" : ""}`}
            onClick={() => {
              setTab("register");
              setError("");
            }}
          >
            <UserPlus size={16} /> Đăng ký tài khoản
          </button>
        </div>
      )}

      {tab === "login" ? (
        <form className="login-form" onSubmit={handleLogin}>
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
                {loading ? "Đang xác thực..." : "Vào phiên học"}{" "}
                <ArrowRight size={18} />
              </button>
              <div className="auth-switch-prompt">
                Chưa có tài khoản?{" "}
                <button
                  type="button"
                  className="auth-link-button"
                  onClick={() => {
                    setTab("register");
                    setError("");
                  }}
                >
                  Đăng ký ngay
                </button>
              </div>
              <small>
                Phiên đăng nhập được giữ bằng HttpOnly cookie và tự động refresh.
              </small>
            </>
          )}
        </form>
      ) : (
        <form className="login-form" onSubmit={handleRegister}>
          <div className="login-lock">
            <Sparkle size={22} color="#38bdf8" weight="fill" />
          </div>
          <div style={{ textAlign: "center", marginBottom: "0.5rem" }}>
            <h2 style={{ fontSize: "1.25rem", margin: 0 }}>Tạo tài khoản học viên</h2>
            <p style={{ fontSize: "0.82rem", color: "var(--text-muted, #94a3b8)", margin: "0.25rem 0 0" }}>
              Bắt đầu lộ trình học thích ứng cá nhân hóa với Chiron AI
            </p>
          </div>
          <label>
            Họ và tên
            <input
              name="displayName"
              placeholder="Nguyễn Văn A"
              required
              minLength={2}
            />
          </label>
          <label>
            Email
            <input
              name="email"
              type="email"
              placeholder="learner@example.com"
              required
            />
          </label>
          <label>
            Mật khẩu
            <input
              name="password"
              type="password"
              placeholder="Tối thiểu 8 ký tự"
              minLength={8}
              required
            />
          </label>
          <label>
            Xác nhận mật khẩu
            <input
              name="confirmPassword"
              type="password"
              placeholder="Nhập lại mật khẩu"
              minLength={8}
              required
            />
          </label>
          <input type="hidden" name="tenantSlug" value="chiron-demo" />
          {error && (
            <p role="alert" className="login-error">
              {error}
            </p>
          )}
          <button className="button button-primary" disabled={loading}>
            {loading ? "Đang tạo tài khoản..." : "Tạo tài khoản & Bắt đầu"}{" "}
            <ArrowRight size={18} />
          </button>
          <div className="auth-switch-prompt">
            Đã có tài khoản?{" "}
            <button
              type="button"
              className="auth-link-button"
              onClick={() => {
                setTab("login");
                setError("");
              }}
            >
              Đăng nhập
            </button>
          </div>
          <small>
            Hệ thống tự động kích hoạt tài khoản và mở khóa khóa học RAG Intensive.
          </small>
        </form>
      )}
    </div>
  );
}
