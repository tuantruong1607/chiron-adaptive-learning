import Link from "next/link";

export function Logo() {
  return (
    <Link className="logo" href="/" aria-label="Chiron AI, trang chủ">
      <span className="logo-mark" aria-hidden="true">
        C
      </span>
      <span>CHIRON</span>
    </Link>
  );
}
