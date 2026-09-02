"use client";

import {
  BookOpen,
  BookOpenText,
  Brain,
  ChatCircleDots,
  CheckCircle,
  Exam,
  Flask,
  List,
  MapTrifold,
  PenNib,
  SidebarSimple,
  SignOut,
  UserCircle,
  X,
  CaretRight,
  ArrowsInSimple,
  ArrowsOutSimple,
} from "@phosphor-icons/react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { Logo } from "./logo";
import { ThemeToggle } from "./theme-toggle";
import { TutorBox } from "./tutor-box";

const primaryLinks = [
  { href: "/diagnostic", label: "Đánh giá đầu vào", icon: Brain, step: 1 },
  { href: "/map", label: "Bản đồ kiến thức", icon: MapTrifold, step: 2 },
  { href: "/learn", label: "Học theo điểm yếu", icon: BookOpenText, step: 3 },
  { href: "/exams", label: "Thi thử 100 câu", icon: Exam },
];

const secondaryLinks = [
  { href: "/labs", label: "Phòng thực hành", icon: Flask },
  { href: "/essays", label: "Bài viết", icon: PenNib },
];

type OnboardingState = {
  completed: boolean;
  question_count: number;
};

function focusableElements(container: HTMLElement | null) {
  return Array.from(
    container?.querySelectorAll<HTMLElement>(
      'a[href], button:not([disabled]), input:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])',
    ) ?? [],
  ).filter((element) => element.getClientRects().length > 0);
}

export function AppShell({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const [menuOpen, setMenuOpen] = useState(false);
  const [collapsed, setCollapsed] = useState(false);
  const [tutorOpen, setTutorOpen] = useState(false);
  const [tutorExpanded, setTutorExpanded] = useState(false);
  const [role, setRole] = useState("learner");
  const [onboarding, setOnboarding] = useState<OnboardingState | null>(null);
  const menuButtonRef = useRef<HTMLButtonElement>(null);
  const menuCloseRef = useRef<HTMLButtonElement>(null);
  const tutorButtonRef = useRef<HTMLButtonElement>(null);
  const tutorCloseRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    const stored = window.localStorage.getItem("chiron:sidebar-collapsed");
    if (stored === "true") {
      setCollapsed(true);
    }
  }, []);

  useEffect(() => {
    function handleKeyDown(event: KeyboardEvent) {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "b") {
        event.preventDefault();
        setCollapsed((prev) => {
          const next = !prev;
          window.localStorage.setItem("chiron:sidebar-collapsed", String(next));
          return next;
        });
      }
    }
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, []);

  function toggleCollapse() {
    setCollapsed((prev) => {
      const next = !prev;
      window.localStorage.setItem("chiron:sidebar-collapsed", String(next));
      return next;
    });
  }

  function handleMainInteraction() {
    if (!collapsed && typeof window !== "undefined" && window.innerWidth >= 1080) {
      setCollapsed(true);
      window.localStorage.setItem("chiron:sidebar-collapsed", "true");
    }
  }

  function closeTutor() {
    setTutorOpen(false);
    window.requestAnimationFrame(() => tutorButtonRef.current?.focus());
  }

  useEffect(() => {
    Promise.all([
      fetch("/api/auth/session", { cache: "no-store" }).then((response) =>
        response.json(),
      ),
      fetch("/api/onboarding", { cache: "no-store" }).then((response) =>
        response.json(),
      ),
    ])
      .then(([session, status]) => {
        const currentRole = session.principal?.role ?? "learner";
        setRole(currentRole);
        setOnboarding(
          currentRole === "learner"
            ? status
            : { completed: true, question_count: 25 },
        );
      })
      .catch(() => setOnboarding({ completed: true, question_count: 25 }));

    function markCompleted() {
      setOnboarding((current) => ({
        completed: true,
        question_count: current?.question_count ?? 25,
      }));
    }
    window.addEventListener("chiron:diagnostic-completed", markCompleted);
    return () =>
      window.removeEventListener("chiron:diagnostic-completed", markCompleted);
  }, []);

  useEffect(() => {
    if (
      onboarding &&
      role === "learner" &&
      !onboarding.completed &&
      pathname !== "/diagnostic"
    ) {
      window.location.replace("/diagnostic");
    }
  }, [onboarding, pathname, role]);

  useEffect(() => {
    if (!menuOpen) return;
    setTutorOpen(false);
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    menuCloseRef.current?.focus();

    function handleKey(event: KeyboardEvent) {
      if (event.key === "Escape") {
        setMenuOpen(false);
        menuButtonRef.current?.focus();
        return;
      }
      if (event.key !== "Tab") return;
      const items = focusableElements(
        menuCloseRef.current?.closest("aside") ?? null,
      );
      if (!items.length) return;
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
    window.addEventListener("keydown", handleKey);
    return () => {
      document.body.style.overflow = previousOverflow;
      window.removeEventListener("keydown", handleKey);
    };
  }, [menuOpen]);

  useEffect(() => {
    if (!tutorOpen) return;
    setMenuOpen(false);
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    tutorCloseRef.current?.focus();

    function handleKey(event: KeyboardEvent) {
      if (event.key === "Escape") {
        closeTutor();
        return;
      }
      if (event.key !== "Tab") return;
      const items = focusableElements(
        tutorCloseRef.current?.closest("aside") ?? null,
      );
      if (!items.length) return;
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
    window.addEventListener("keydown", handleKey);
    return () => {
      document.body.style.overflow = previousOverflow;
      window.removeEventListener("keydown", handleKey);
    };
  }, [tutorOpen]);

  async function logout() {
    await fetch("/api/auth/logout", { method: "POST" });
    window.location.assign("/login");
  }

  return (
    <div className="app-layout">
      <a className="skip-link" href="#main-content">
        Bỏ qua điều hướng
      </a>
      <aside
        id="primary-sidebar"
        className={`sidebar ${menuOpen ? "sidebar-open" : ""} ${collapsed ? "sidebar-collapsed" : ""}`}
        aria-label="Điều hướng chính"
      >
        <div className="sidebar-head">
          <Logo />
          <div className="sidebar-actions">
            <ThemeToggle />
            <button
              type="button"
              className="icon-button desktop-only collapse-toggle"
              onClick={toggleCollapse}
              aria-label={collapsed ? "Mở rộng thanh bên (Ctrl+B)" : "Thu gọn thanh bên (Ctrl+B)"}
              title={collapsed ? "Mở rộng thanh bên (Ctrl+B)" : "Thu gọn thanh bên (Ctrl+B)"}
            >
              {collapsed ? <CaretRight size={18} /> : <SidebarSimple size={18} />}
            </button>
            <button
              ref={menuCloseRef}
              type="button"
              className="icon-button mobile-only"
              onClick={() => {
                setMenuOpen(false);
                menuButtonRef.current?.focus();
              }}
              aria-label="Đóng menu"
            >
              <X size={20} aria-hidden="true" />
            </button>
          </div>
        </div>

        <div className="flow-summary" aria-label="Lộ trình học tập">
          <span>Lộ trình của bạn</span>
          <strong>
            {onboarding?.completed
              ? "Đang học theo điểm yếu"
              : "Bắt đầu từ đánh giá đầu vào"}
          </strong>
        </div>

        <nav aria-label="Lộ trình chính">
          {primaryLinks.map(({ href, label, icon: Icon, step }) => {
            const active = pathname === href || pathname.startsWith(`${href}/`);
            const completed = Boolean(
              onboarding?.completed && step && step < 3,
            );
            return (
              <Link
                key={href}
                href={href}
                onClick={() => setMenuOpen(false)}
                className={active ? "active" : ""}
                aria-current={active ? "page" : undefined}
                title={label}
              >
                <span className="nav-step" aria-hidden="true">
                  {completed ? (
                    <CheckCircle size={19} weight="fill" />
                  ) : step ? (
                    step
                  ) : (
                    <Icon size={19} />
                  )}
                </span>
                <span>{label}</span>
              </Link>
            );
          })}
        </nav>

        <nav className="secondary-nav" aria-label="Thực hành thêm">
          <span>Thực hành thêm</span>
          {secondaryLinks.map(({ href, label, icon: Icon }) => {
            const active = pathname === href || pathname.startsWith(`${href}/`);
            return (
              <Link
                key={href}
                href={href}
                onClick={() => setMenuOpen(false)}
                className={active ? "active" : ""}
                aria-current={active ? "page" : undefined}
                title={label}
              >
                <Icon size={19} aria-hidden="true" />
                <span>{label}</span>
              </Link>
            );
          })}
        </nav>

        <div className="course-switcher" title="Khóa đang học: Chiron AI · Toàn khóa">
          <BookOpen size={20} aria-hidden="true" />
          <div>
            <span>Khóa đang học</span>
            <strong>Chiron AI · Toàn khóa</strong>
          </div>
        </div>
        <div className="session-control" title={`Phiên hiện tại: ${role}`}>
          <UserCircle size={20} aria-hidden="true" />
          <div>
            <span>Phiên hiện tại</span>
            <strong>{role}</strong>
          </div>
          <button type="button" onClick={logout} aria-label="Đăng xuất" title="Đăng xuất">
            <SignOut size={17} aria-hidden="true" />
          </button>
        </div>
      </aside>

      {menuOpen && (
        <button
          type="button"
          className="sidebar-scrim"
          onClick={() => {
            setMenuOpen(false);
            menuButtonRef.current?.focus();
          }}
          aria-label="Đóng menu"
        />
      )}

      <div
        className={`app-main ${collapsed ? "sidebar-collapsed" : ""}`}
        id="main-content"
        tabIndex={-1}
        onPointerDownCapture={handleMainInteraction}
      >
        <header className="mobile-header">
          <button
            ref={menuButtonRef}
            type="button"
            className="icon-button"
            onClick={() => setMenuOpen(true)}
            aria-label="Mở menu"
            aria-expanded={menuOpen}
            aria-controls="primary-sidebar"
          >
            <List size={22} aria-hidden="true" />
          </button>
          <Logo />
          <ThemeToggle />
        </header>
        {onboarding === null && pathname !== "/diagnostic" ? (
          <div className="route-loading" role="status">
            Đang xác định lộ trình học…
          </div>
        ) : (
          children
        )}
      </div>

      <button
        ref={tutorButtonRef}
        type="button"
        className="tutor-launcher"
        onClick={() => setTutorOpen(true)}
        aria-label="Mở chatbot hỗ trợ"
        aria-expanded={tutorOpen}
        aria-controls="tutor-drawer"
      >
        <ChatCircleDots size={24} weight="fill" aria-hidden="true" />
        <span>Hỏi Chiron</span>
      </button>

      {tutorOpen && (
        <>
          <button
            type="button"
            className="tutor-scrim"
            aria-label="Đóng chatbot"
            onClick={closeTutor}
          />
          <aside
            id="tutor-drawer"
            className={`tutor-drawer ${tutorExpanded ? "is-expanded" : ""}`}
            role="dialog"
            aria-modal="true"
            aria-label="Chatbot hỗ trợ học tập"
          >
            <div className="tutor-drawer-head">
              <div>
                <span>Trợ giảng theo nguồn</span>
                <strong>Chiron</strong>
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: "6px" }}>
                <button
                  type="button"
                  className="icon-button"
                  onClick={() => setTutorExpanded((prev) => !prev)}
                  aria-label={tutorExpanded ? "Thu gọn cửa sổ" : "Mở rộng cửa sổ"}
                  title={tutorExpanded ? "Thu gọn (600px)" : "Mở rộng (880px)"}
                >
                  {tutorExpanded ? <ArrowsInSimple size={18} /> : <ArrowsOutSimple size={18} />}
                </button>
                <button
                  ref={tutorCloseRef}
                  type="button"
                  className="icon-button"
                  onClick={closeTutor}
                  aria-label="Đóng chatbot"
                >
                  <X size={20} aria-hidden="true" />
                </button>
              </div>
            </div>
            <TutorBox />
          </aside>
        </>
      )}
    </div>
  );
}
