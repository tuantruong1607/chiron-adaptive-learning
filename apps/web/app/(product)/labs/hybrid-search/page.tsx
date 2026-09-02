import { ScenarioLab } from "@/components/scenario-lab";

export default function HybridSearchLabPage() {
  return (
    <main className="product-page lab-page">
      <header className="product-header compact">
        <div>
          <p>Practice lab</p>
          <h1>Hybrid Search Control Room</h1>
          <span>
            Scenario có thể lưu và chạy lại. Mọi lần submit tạo một evidence
            event.
          </span>
        </div>
      </header>
      <ScenarioLab labId="hybrid-search" />
    </main>
  );
}
