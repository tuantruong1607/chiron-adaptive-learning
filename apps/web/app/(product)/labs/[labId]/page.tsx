import { ScenarioLab } from "@/components/scenario-lab";

export default async function LabPage({
  params,
}: {
  params: Promise<{ labId: string }>;
}) {
  const { labId } = await params;
  return (
    <main className="product-page lab-page">
      <header className="product-header compact">
        <div>
          <p>Practice lab</p>
          <h1>Scenario workspace</h1>
          <span>
            Tiến độ được autosave. Kết quả sinh evidence và cập nhật study plan.
          </span>
        </div>
      </header>
      <ScenarioLab labId={labId} />
    </main>
  );
}
