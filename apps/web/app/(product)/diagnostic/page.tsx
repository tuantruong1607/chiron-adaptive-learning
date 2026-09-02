import { DiagnosticExam } from "@/components/diagnostic-exam";

export default function DiagnosticPage() {
  return (
    <main className="product-page diagnostic-page">
      <header className="product-header compact">
        <div>
          <p>Bước 1/3 · Đánh giá đầu vào</p>
          <h1>Xác định kiến thức bạn đang thiếu</h1>
          <span>
            25 câu phân tầng trên toàn khóa, khoảng 15–20 phút. Kết quả sẽ cập
            nhật bản đồ kiến thức và gợi ý nội dung nên học trước.
          </span>
        </div>
      </header>
      <DiagnosticExam />
    </main>
  );
}
