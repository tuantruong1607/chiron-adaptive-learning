import { KnowledgeMapExplorer } from "@/components/knowledge-map";

export default async function MapPage({
  searchParams,
}: {
  searchParams: Promise<{ from?: string }>;
}) {
  const { from } = await searchParams;
  return (
    <main className="product-page map-page">
      <header className="product-header compact">
        <div>
          <p>Bước 2/3 · Bản đồ kiến thức cá nhân</p>
          <h1>Nhìn rõ phần bạn còn yếu</h1>
          <span>
            73 concept phủ toàn khóa, được chia theo 9 lĩnh vực. Node có mastery
            thấp là nơi nên bắt đầu; chọn node để xem quan hệ và mở đúng tài liệu.
          </span>
        </div>
      </header>
      {from === "diagnostic" ? (
        <section className="flow-callout" aria-label="Bước tiếp theo">
          <span>Đã chấm xong đánh giá đầu vào</span>
          <strong>
            Chọn một node “Mới” hoặc “Đang phát triển” để bắt đầu học.
          </strong>
          <p>Ưu tiên node mastery thấp nhưng có nhiều quan hệ tiên quyết.</p>
        </section>
      ) : null}
      <KnowledgeMapExplorer />
    </main>
  );
}
