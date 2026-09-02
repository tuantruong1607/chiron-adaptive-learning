import { ArrowRight } from "@phosphor-icons/react/dist/ssr";
import Link from "next/link";
import { Logo } from "./logo";
import { ThemeToggle } from "./theme-toggle";

export function MarketingNav() {
  return (
    <header className="marketing-nav glass-surface">
      <Logo />
      <nav aria-label="Điều hướng chính">
        <Link href="#system">Cách hoạt động</Link>
        <Link href="#proof">Bằng chứng học tập</Link>
      </nav>
      <div className="nav-actions">
        <ThemeToggle />
        <Link className="nav-cta" href="/learn">
          Vào phòng học <ArrowRight size={16} weight="bold" />
        </Link>
      </div>
    </header>
  );
}
