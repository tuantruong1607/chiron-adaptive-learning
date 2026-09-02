import {
  ArrowRight,
  CheckCircle,
  Crosshair,
  Graph,
  ShieldCheck,
} from "@phosphor-icons/react/dist/ssr";
import Image from "next/image";
import Link from "next/link";
import { HeroMap } from "@/components/hero-map";
import { MarketingNav } from "@/components/marketing-nav";
import { Reveal } from "@/components/reveal";

export default function LandingPage() {
  return (
    <main className="landing">
      <MarketingNav />
      <section className="hero section-shell">
        <div className="hero-media" aria-hidden="true">
          <Image
            src="/images/chiron-aegean-observatory.png"
            alt=""
            fill
            priority
            quality={86}
            sizes="100vw"
          />
        </div>
        <Reveal className="hero-copy">
          <p className="eyebrow">Lộ trình học thích ứng</p>
          <h1>
            Học đúng điểm yếu. <em>Trước khi quá muộn.</em>
          </h1>
          <p className="hero-lede">
            Chiron biến mọi lần trả lời thành một quyết định học tập có bằng
            chứng.
          </p>
          <div className="hero-actions">
            <Link className="button button-primary" href="/login">
              Bắt đầu phiên học <ArrowRight size={18} weight="bold" />
            </Link>
            <Link className="button button-secondary" href="/map">
              Xem knowledge map
            </Link>
          </div>
        </Reveal>
        <Reveal className="hero-visual oracle-panel">
          <HeroMap />
        </Reveal>
      </section>

      <section id="system" className="system-section section-shell">
        <Reveal className="section-intro">
          <h2>Một vòng học khép kín</h2>
          <p>
            Không phải chatbot gắn vào khóa học. Mỗi tín hiệu đều quay lại
            mastery model và kế hoạch tiếp theo.
          </p>
        </Reveal>
        <div className="system-grid">
          <Reveal className="system-block system-block-wide">
            <Crosshair size={28} />
            <h3>Chẩn đoán nguyên nhân</h3>
            <p>
              Phân biệt thiếu kiến thức, nhầm khái niệm và lỗi quy trình trước
              khi đề xuất bài học.
            </p>
            <div className="signal-stack" aria-label="Ví dụ phân tích lỗi">
              <span>Answer signal</span>
              <strong>RRF score normalization</strong>
              <span>Root cause</span>
              <strong>Nhầm rank với raw score</strong>
            </div>
          </Reveal>
          <Reveal className="system-block system-block-graph">
            <Graph size={28} />
            <h3>Map có provenance</h3>
            <p>Mỗi concept và quan hệ đều quay lại source span đã review.</p>
          </Reveal>
          <Reveal className="system-block system-block-accent">
            <ShieldCheck size={28} />
            <h3>Grounded by default</h3>
            <p>
              Tutor từ chối khi không đủ bằng chứng và không giấu nguồn khỏi
              người học.
            </p>
          </Reveal>
        </div>
      </section>

      <section id="proof" className="proof-section section-shell">
        <Reveal className="proof-quote">
          <p>
            “Bạn không cần học thêm mọi thứ. Bạn cần biết chính xác khái niệm
            nào đang chặn điểm số.”
          </p>
        </Reveal>
        <div className="proof-list">
          <div>
            <CheckCircle size={22} />
            <span>Diagnostic</span>
            <strong>Tìm lỗ hổng</strong>
          </div>
          <div>
            <CheckCircle size={22} />
            <span>Practice lab</span>
            <strong>Tạo evidence</strong>
          </div>
          <div>
            <CheckCircle size={22} />
            <span>Adaptive plan</span>
            <strong>Chọn việc tiếp theo</strong>
          </div>
        </div>
      </section>

      <section className="closing section-shell">
        <Reveal>
          <h2>Phiên học tiếp theo đã sẵn sàng.</h2>
          <Link className="button button-primary" href="/learn">
            Mở Chiron <ArrowRight size={18} weight="bold" />
          </Link>
        </Reveal>
      </section>
    </main>
  );
}
