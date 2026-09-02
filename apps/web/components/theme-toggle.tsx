"use client";

import { Moon, Sun } from "@phosphor-icons/react";
import { useEffect, useState } from "react";

type Theme = "light" | "dark";

const THEME_EVENT = "chiron-theme-change";

function applyTheme(theme: Theme) {
  document.documentElement.dataset.theme = theme;
}

export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>("light");

  useEffect(() => {
    const stored = window.localStorage.getItem("chiron-theme");
    const initial: Theme =
      stored === "light" || stored === "dark"
        ? stored
        : window.matchMedia("(prefers-color-scheme: dark)").matches
          ? "dark"
          : "light";

    applyTheme(initial);
    setTheme(initial);

    const syncTheme = (event: Event) => {
      const nextTheme = (event as CustomEvent<Theme>).detail;
      applyTheme(nextTheme);
      setTheme(nextTheme);
    };

    window.addEventListener(THEME_EVENT, syncTheme);
    return () => window.removeEventListener(THEME_EVENT, syncTheme);
  }, []);

  function toggleTheme() {
    const nextTheme: Theme = theme === "light" ? "dark" : "light";
    window.localStorage.setItem("chiron-theme", nextTheme);
    window.dispatchEvent(
      new CustomEvent<Theme>(THEME_EVENT, { detail: nextTheme }),
    );
  }

  const nextLabel =
    theme === "light" ? "Chuyển sang nền tối" : "Chuyển sang nền sáng";

  return (
    <button
      className="theme-toggle"
      type="button"
      onClick={toggleTheme}
      aria-label={nextLabel}
      title={nextLabel}
    >
      {theme === "light" ? <Moon size={17} /> : <Sun size={17} />}
    </button>
  );
}
