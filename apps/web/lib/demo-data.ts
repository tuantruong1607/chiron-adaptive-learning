import type { ConceptEdge, ConceptNode, DiagnosticQuestion, StudyPlan } from "@chiron/domain";

const cite = (id: string, title: string, locator: string, excerpt: string) => ({
  sourceSpanId: id,
  title,
  locator,
  excerpt,
});

export const concepts: ConceptNode[] = [
  { id: "chunking", name: "Hierarchical chunking", summary: "Chia tài liệu theo cấu trúc và giữ quan hệ parent-child.", objective: "Thiết kế chunk có boundary và locator ổn định.", mastery: 0.46, confidence: 0.78, examWeight: 0.82, band: "developing", x: 13, y: 30, citations: [cite("pdf-07-p24", "Track 3 Day 18", "Trang 24", "Metadata và cấu trúc chunk quyết định chất lượng retrieval.")] },
  { id: "dense", name: "Dense retrieval", summary: "Biểu diễn semantic similarity bằng vector embedding.", objective: "Phân tích điểm mạnh và blind spot của dense retrieval.", mastery: 0.76, confidence: 0.86, examWeight: 0.7, band: "secure", x: 34, y: 18, citations: [cite("pdf-07-p63", "Slide Day 07", "Trang 63", "Dense vector phù hợp với truy vấn gần nghĩa.")] },
  { id: "sparse", name: "Sparse retrieval", summary: "Tìm exact token và thuật ngữ hiếm bằng sparse vector.", objective: "Kết hợp lexical evidence với semantic evidence.", mastery: 0.58, confidence: 0.72, examWeight: 0.68, band: "developing", x: 33, y: 46, citations: [cite("pdf-18-p28", "Track 3 Day 18", "Trang 28", "Sparse retrieval giữ tín hiệu từ khóa và identifier.")] },
  { id: "rrf", name: "Reciprocal Rank Fusion", summary: "Hợp nhất nhiều danh sách dựa trên thứ hạng.", objective: "Tính RRF và giải thích tính ổn định.", mastery: 0.31, confidence: 0.65, examWeight: 0.9, band: "developing", x: 53, y: 31, citations: [cite("pdf-07-p69", "Slide Day 07", "Trang 69", "RRF fuse kết quả theo vị trí xếp hạng.")] },
  { id: "metadata-filtering", name: "Metadata and tenant filtering", summary: "Giới hạn candidate theo tenant, khóa học và quyền truy cập trước retrieval.", objective: "Đặt authorization boundary trước candidate generation.", mastery: 0.38, confidence: 0.64, examWeight: 0.86, band: "developing", x: 51, y: 50, citations: [cite("pdf-18-filtering", "Track 3 Day 18", "Metadata filtering", "Authorization filter phải được áp dụng trước retrieval.")] },
  { id: "reranking", name: "Cross-encoder reranking", summary: "Chấm lại shortlist bằng query-document interaction.", objective: "Chọn rerank depth theo quality và latency.", mastery: 0.42, confidence: 0.69, examWeight: 0.88, band: "developing", x: 69, y: 18, citations: [cite("pdf-18-p54", "Track 3 Day 18", "Trang 54", "Reranking cải thiện thứ tự top-k.")] },
  { id: "citation", name: "Citation verification", summary: "Kiểm tra source span có hỗ trợ trực tiếp từng claim.", objective: "Tách relevance khỏi entailment.", mastery: 0.67, confidence: 0.75, examWeight: 0.94, band: "secure", x: 84, y: 37, citations: [cite("pdf-24-p61", "Track 3 Day 24", "Trang 61", "Citation precision được đo độc lập.")] },
  { id: "graph-routing", name: "Graph-lite routing", summary: "Mở rộng graph khi intent cần prerequisite hoặc multi-hop.", objective: "Chọn relation, hop limit và latency budget.", mastery: 0.22, confidence: 0.61, examWeight: 0.79, band: "developing", x: 57, y: 61, citations: [cite("pdf-19-p43", "Track 3 Day 19", "Trang 43", "Graph augmentation nên route theo query intent.")] },
  { id: "evaluation", name: "RAG evaluation", summary: "Đo retrieval, faithfulness và citation trên golden set.", objective: "Thiết kế eval gate phát hiện regression.", mastery: 0.18, confidence: 0.57, examWeight: 0.92, band: "new", x: 78, y: 70, citations: [cite("pdf-24-p64", "Track 3 Day 24", "Trang 64", "Failure cần trở thành regression case.")] },
];

export const edges: ConceptEdge[] = [
  { id: "e1", source: "chunking", target: "dense", relation: "prerequisite_of", weight: 0.8 },
  { id: "e2", source: "chunking", target: "sparse", relation: "prerequisite_of", weight: 0.7 },
  { id: "e3", source: "dense", target: "rrf", relation: "prerequisite_of", weight: 0.9 },
  { id: "e4", source: "sparse", target: "rrf", relation: "prerequisite_of", weight: 0.9 },
  { id: "e5", source: "rrf", target: "reranking", relation: "prerequisite_of", weight: 0.85 },
  { id: "e6", source: "reranking", target: "citation", relation: "applies_to", weight: 0.65 },
  { id: "e7", source: "rrf", target: "graph-routing", relation: "contrasts_with", weight: 0.55 },
  { id: "e8", source: "graph-routing", target: "evaluation", relation: "applies_to", weight: 0.74 },
  { id: "e9", source: "citation", target: "evaluation", relation: "part_of", weight: 0.82 },
  { id: "e10", source: "metadata-filtering", target: "dense", relation: "applies_to", weight: 0.78 },
  { id: "e11", source: "metadata-filtering", target: "sparse", relation: "applies_to", weight: 0.78 },
];

export const questions: DiagnosticQuestion[] = [
  { id: "q1", conceptId: "rrf", prompt: "Vì sao RRF ổn định hơn cộng score dense và sparse trực tiếp?", options: [{ id: "a", text: "Chuẩn hóa embedding trước khi tìm" }, { id: "b", text: "Dựa trên rank, không cần score cùng thang đo" }, { id: "c", text: "Thay thế hoàn toàn reranker" }, { id: "d", text: "Chỉ giữ kết quả dense" }] },
  { id: "q2", conceptId: "chunking", prompt: "Thuộc tính nào giúp citation mở đúng vị trí nguồn?", options: [{ id: "a", text: "Màu giao diện" }, { id: "b", text: "Tên model chat" }, { id: "c", text: "Source span và locator ổn định" }, { id: "d", text: "Nhiệt độ sampling" }] },
  { id: "q3", conceptId: "graph-routing", prompt: "Khi nào hệ thống nên mở rộng Graph-lite?", options: [{ id: "a", text: "Cho mọi truy vấn" }, { id: "b", text: "Khi intent cần prerequisite hoặc multi-hop" }, { id: "c", text: "Chỉ khi Qdrant lỗi" }, { id: "d", text: "Sau khi sinh câu trả lời" }] },
  { id: "q4", conceptId: "citation", prompt: "Citation precision đo điều gì?", options: [{ id: "a", text: "Tỷ lệ citation thực sự hỗ trợ claim" }, { id: "b", text: "Tốc độ sinh token" }, { id: "c", text: "Số chunk trong collection" }, { id: "d", text: "Độ dài câu trả lời" }] },
  { id: "q5", conceptId: "evaluation", prompt: "Failure trên production nên đi vào quy trình nào?", options: [{ id: "a", text: "Xóa log" }, { id: "b", text: "Chỉ sửa prompt" }, { id: "c", text: "Thêm regression case có version" }, { id: "d", text: "Tăng top-k vô hạn" }] },
];

export const demoPlan: StudyPlan = {
  id: "plan-demo",
  title: "Phiên học ưu tiên hôm nay",
  totalMinutes: 54,
  generatedAt: "2026-08-30T08:00:00Z",
  items: [
    { id: "p1", conceptId: "evaluation", title: "RAG evaluation", activity: "retrieval", durationMinutes: 18, reason: "Mastery thấp, trọng số đề cao", expectedGain: 0.14 },
    { id: "p2", conceptId: "rrf", title: "Hybrid Search Control Room", activity: "lab", durationMinutes: 24, reason: "Lỗi lặp lại ở rank fusion", expectedGain: 0.11 },
    { id: "p3", conceptId: "graph-routing", title: "Graph-lite routing", activity: "recheck", durationMinutes: 12, reason: "Cần xác nhận prerequisite", expectedGain: 0.09 },
  ],
};
