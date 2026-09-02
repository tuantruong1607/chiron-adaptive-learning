import { EssayWorkspace } from "@/components/essay-workspace";

export default function EssaysPage() {
  return (
    <main className="product-page lab-page">
      <header className="product-header compact">
        <div>
          <p>Assessment</p>
          <h1>Constructed response</h1>
          <span>
            Bài viết được lưu private, chấm theo rubric version và chuyển human
            review khi confidence thấp.
          </span>
        </div>
      </header>
      <EssayWorkspace />
    </main>
  );
}
