import { MockExam } from "@/components/mock-exam";

export default function ExamsPage() {
  return (
    <main className="product-page exams-page">
      <header className="product-header compact">
        <div>
          <p>Luyện thi · Không ảnh hưởng mastery</p>
          <h1>Thi thử 100 câu</h1>
          <span>
            Làm bài theo thời gian thật, nhận điểm và feedback tự luận theo
            rubric.
          </span>
        </div>
      </header>
      <MockExam />
    </main>
  );
}
