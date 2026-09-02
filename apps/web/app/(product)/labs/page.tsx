import { LabsCatalog } from "@/components/labs-catalog";

export default function LabsPage() {
  return (
    <main className="product-page lab-page">
      <header className="product-header compact">
        <div>
          <p>Practice</p>
          <h1>Practice labs</h1>
          <span>
            Sáu scenario bám theo knowledge graph; mỗi lần hoàn thành tạo
            evidence cho adaptive loop.
          </span>
        </div>
      </header>
      <LabsCatalog />
    </main>
  );
}
