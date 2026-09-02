import { SourceLocator } from "@/components/source-locator";

export default async function SourcePage({
  params,
}: {
  params: Promise<{ sourceSpanId: string }>;
}) {
  const { sourceSpanId } = await params;
  return (
    <main className="product-page lab-page">
      <header className="product-header compact">
        <div>
          <p>Knowledge source</p>
          <h1>Source locator</h1>
          <span>
            Locator lấy từ active knowledge graph của khóa học hiện tại.
          </span>
        </div>
      </header>
      <SourceLocator sourceSpanId={decodeURIComponent(sourceSpanId)} />
    </main>
  );
}
