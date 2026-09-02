import { Logo } from "@/components/logo";
import { LoginForm } from "@/components/login-form";

export default function LoginPage() {
  const configuredMode = process.env.AUTH_MODE;
  const authMode =
    configuredMode === "oidc" || configuredMode === "hybrid"
      ? configuredMode
      : "local";
  return (
    <main className="login-page">
      <section className="login-copy">
        <Logo />
        <p className="eyebrow">Authenticated learning space</p>
        <h1>Tiếp tục từ đúng nơi kiến thức của bạn đang dở.</h1>
        <p>
          Identity quyết định tenant, enrollment và toàn bộ mastery state.
          Chiron không nhận learner ID từ trình duyệt.
        </p>
      </section>
      <LoginForm authMode={authMode} />
    </main>
  );
}
