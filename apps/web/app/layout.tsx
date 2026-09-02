import type { Metadata } from "next";
import { Lora, Manrope } from "next/font/google";
import "./globals.css";

const sans = Manrope({
  subsets: ["latin", "vietnamese"],
  variable: "--font-sans",
});
const display = Lora({
  weight: ["400", "500"],
  subsets: ["latin", "vietnamese"],
  variable: "--font-display",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Chiron AI | Học đúng điểm yếu",
  description: "Nền tảng học thích ứng cho luyện thi AI và RAG chuyên sâu.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="vi"
      className={`${sans.variable} ${display.variable}`}
      suppressHydrationWarning
    >
      <body>{children}</body>
    </html>
  );
}
