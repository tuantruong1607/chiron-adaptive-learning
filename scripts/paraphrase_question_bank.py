"""Full paraphrasing engine for Chiron AI 100-item question bank.

Refines prompts, options, explanations, and rubrics into natural, fluent,
professional Vietnamese while preserving 100% of technical terms.
"""
from __future__ import annotations

import json
from pathlib import Path

BANK_PATH = Path("services/api/app/generated_question_bank.json")

# Dictionary mapping question number -> updated texts
PARAPHRASES = {
    1: {
        "prompt": "Hệ thống RAG của bạn gặp hiện tượng thiếu ngữ cảnh do các chunk được chia quá nhỏ (mỗi chunk chỉ chứa một câu đơn lẻ). Khi tăng `top_k`, ngữ cảnh đưa vào prompt bị phân mảnh và nhiễu nghiêm trọng. Giải pháp can thiệp nào dưới đây là phù hợp nhất?",
        "options": [
            {"id": "a", "text": "Tăng overlap cố định giữa các chunk lên 50% để các câu liền kề tự động dính lại với nhau."},
            {"id": "b", "text": "Bổ sung cross-encoder rerank trên top-100 candidates trước khi đưa vào prompt."},
            {"id": "c", "text": "Chuyển sang semantic hoặc hierarchical chunking nhằm bảo toàn trọn vẹn đoạn văn cùng một mạch ý."},
            {"id": "d", "text": "Chuyển sang dùng embedding model có thứ hạng benchmark VN-MTEB cao hơn."}
        ],
        "explanation": "Chunk chính là đơn vị bằng chứng (unit of evidence): nếu chiến lược chunking bị hỏng thì dù embedding hay rerank có tốt đến đâu cũng không thể cứu được. Overlap 50% chỉ ghép nối câu rời rạc một cách máy móc chứ không khôi phục được ngữ cảnh đoạn."
    },
    2: {
        "prompt": "Vai trò cốt lõi nhất của embedding model trong kỹ thuật dense retrieval là gì?",
        "options": [
            {"id": "a", "text": "Mã hóa văn bản thành vector số học trong không gian nhiều chiều để so khớp mức độ tương đồng ngữ nghĩa."},
            {"id": "b", "text": "Chuẩn hóa điểm số (score) của BM25 và cosine similarity về cùng một thang đo đồng nhất."},
            {"id": "c", "text": "Đánh giá lại mức độ phù hợp của từng cặp (query, document) sau khi đã lấy được danh sách candidates."},
            {"id": "d", "text": "Nén dung lượng tài liệu gốc để tiết kiệm không gian lưu trữ trong vector database."}
        ],
        "explanation": "Embedding ánh xạ văn bản thành vector để so sánh khoảng cách ngữ nghĩa. Chuẩn hóa thang đo là nhiệm vụ của rank fusion, chấm lại candidate là việc của cross-encoder rerank, còn nén dữ liệu là vai trò của quantization."
    },
    3: {
        "prompt": "Khi truy vấn câu “cơ chế giữ version code chính xác”, hệ thống không tìm thấy tài liệu chứa đúng identifier `foo_bar_v2`, dù vẫn lấy được nhiều đoạn có ý nghĩa tương tự. Nguyên nhân chính khiến dense-only retrieval bị bỏ sót là gì và nên khắc phục ra sao?",
        "options": [
            {"id": "a", "text": "Cần fine-tune embedding model trên tập dữ liệu nội bộ để model ghi nhớ các identifier đặc thù."},
            {"id": "b", "text": "Tăng `top_k` lên 100 rồi áp dụng cross-encoder rerank nhằm đẩy tài liệu chính xác lên đầu."},
            {"id": "c", "text": "Thêm metadata filter theo trường `version` để thu hẹp không gian tìm kiếm."},
            {"id": "d", "text": "Kết hợp sparse retrieval (BM25) và áp dụng hybrid search; dense retrieval thường gặp điểm mù với các token hiếm hoặc từ khóa chính xác tuyệt đối."}
        ],
        "explanation": "Dense retrieval dựa vào phân bố ngữ nghĩa chung nên dễ bỏ sót các identifier hiếm hoặc ký hiệu kỹ thuật đặc thù. Kết hợp BM25 (sparse retrieval) qua hybrid search giúp bù đắp điểm mù này. Rerank chỉ sắp xếp lại các candidate đã được lấy ra; nếu candidate chưa từng vào top thì rerank cũng không thể xử lý."
    },
    4: {
        "prompt": "Trường hợp truy vấn (query) nào dưới đây là ứng viên lý tưởng nhất để sparse retrieval (BM25) phát huy hiệu quả?",
        "options": [
            {"id": "a", "text": "Query mô tả ý định bằng ngôn từ hoàn toàn khác biệt so với tài liệu gốc (ví dụ: “muốn lấy lại tiền”)."},
            {"id": "b", "text": "Query chứa mã lỗi cụ thể, tên hàm kỹ thuật hoặc từ viết tắt chuyên ngành cần khớp chính xác từng ký tự."},
            {"id": "c", "text": "Query phức tạp gồm nhiều mệnh đề dài, đòi hỏi tổng hợp thông tin từ nhiều đoạn phân tán."},
            {"id": "d", "text": "Query yêu cầu sắp xếp tài liệu theo độ mới theo thời gian thay vì độ tương đồng nội dung."}
        ],
        "explanation": "BM25 hoạt động dựa trên tần suất từ khóa chính xác (lexical matching), do đó cực kỳ hiệu quả với mã lỗi, tên hàm, mã định danh. Với các câu hỏi dùng từ đồng nghĩa hoặc diễn đạt khác biệt, BM25 dễ trả về 0 kết quả."
    },
    5: {
        "prompt": "Trong hệ thống tìm kiếm kết hợp, nhánh dense retrieval trả về đúng đoạn giải thích ngữ nghĩa, còn nhánh BM25 trả về đúng tên hàm API. Bạn cần một cơ chế xếp hạng kết hợp mà không bị phụ thuộc vào thang điểm số thô khác biệt giữa hai mô hình. Giải pháp tối ưu là gì?",
        "options": [
            {"id": "a", "text": "Áp dụng Reciprocal Rank Fusion (RRF) dựa trên thứ hạng (rank) của hai danh sách với hệ số k = 60."},
            {"id": "b", "text": "Thực hiện min-max normalization đưa điểm số của hai bên về đoạn [0, 1] rồi cộng dồn theo trọng số cố định."},
            {"id": "c", "text": "Nhân điểm cosine similarity với điểm BM25 và chỉ lấy phần giao nhau của hai danh sách."},
            {"id": "d", "text": "Lấy top-5 của mỗi nhánh rồi đưa toàn bộ vào prompt để LLM tự chọn ra đoạn phù hợp nhất."}
        ],
        "explanation": "RRF giải quyết triệt để bài toán thang điểm không đồng nhất bằng cách chỉ sử dụng thứ vị trí (rank) của từng tài liệu trong danh sách kết quả, không cần chuẩn hóa hay can thiệp vào điểm số thô."
    },
    6: {
        "prompt": "Trong kiến trúc tìm kiếm hai giai đoạn (two-stage retrieval), thành phần reranker (cross-encoder) nên được đặt ở vị trí nào trong pipeline?",
        "options": [
            {"id": "a", "text": "Đặt trước bước ANN search để cross-encoder thu hẹp không gian tìm kiếm ngay từ đầu."},
            {"id": "b", "text": "Đặt ngay sau bước chunking để chấm điểm chất lượng từng chunk trong quá trình indexing dữ liệu."},
            {"id": "c", "text": "Đặt sau khi ANN search trả về tập candidate, nhằm chấm điểm tương quan chi tiết cho từng cặp (query, chunk)."},
            {"id": "d", "text": "Đặt ở cuối cùng sau khi LLM đã sinh câu trả lời để kiểm định chất lượng phản hồi."}
        ],
        "explanation": "Cross-encoder có chi phí tính toán cao vì phải xử lý đồng thời cả query và văn bản; do đó nó chỉ được áp dụng trên tập candidate nhỏ (ví dụ top 20-50) được thu thập từ giai đoạn retrieval thứ nhất."
    },
    7: {
        "prompt": "Để đảm bảo cô lập dữ liệu người dùng (tenant isolation) trong hệ thống RAG đa người dùng, cơ chế kiểm soát nào đảm bảo an toàn và được đặt đúng vị trí nhất?",
        "options": [
            {"id": "a", "text": "Tạo riêng cho mỗi tenant một collection và cho phép client tự truyền tên collection khi gửi query."},
            {"id": "b", "text": "Thực hiện lọc loại bỏ dữ liệu khác tenant ở tầng application sau khi vector database đã trả về kết quả top-k."},
            {"id": "c", "text": "Áp dụng metadata pre-filter với `tenant_id` và `course_id` được trích xuất trực tiếp từ phiên xác thực (session/token) của người dùng."},
            {"id": "d", "text": "Bổ sung chỉ dẫn vào system prompt yêu cầu LLM không được tiết lộ thông tin của tenant khác."}
        ],
        "explanation": "Metadata pre-filter tại tầng vector database với thông tin tenant lấy từ token/session đảm bảo truy vấn không bao giờ chạm tới dữ liệu ngoài phạm vi cho phép. Post-filter làm mất recall của top-k, còn prompt chỉ mang tính định hướng chứ không phải ranh giới bảo mật."
    },
    8: {
        "prompt": "Thuật toán đồ thị HNSW (Hierarchical Navigable Small World) tối ưu hóa tốc độ tìm kiếm láng giềng gần nhất (ANN search) dựa trên nguyên lý cốt lõi nào?",
        "options": [
            {"id": "a", "text": "Xây dựng cấu trúc đồ thị nhiều tầng: các tầng trên thưa thớt để nhảy nhanh qua các vùng dữ liệu, tầng dưới cùng dày đặc để tìm kiếm chính xác."},
            {"id": "b", "text": "Chia không gian vector thành các cụm Voronoi độc lập và chỉ quét các cụm có tâm gần nhất."},
            {"id": "c", "text": "Nén các vector 1536 chiều thành các chuỗi nhị phân (binary hash) để tăng tốc độ tính khoảng cách Hamming."},
            {"id": "d", "text": "Sắp xếp toàn bộ vector theo thứ tự từ điển rồi áp dụng thuật toán tìm kiếm nhị phân (binary search)."}
        ],
        "explanation": "HNSW sử dụng cấu trúc đồ thị phân tầng tương tự skip-list: các tầng trên gồm các liên kết dài giúp điều hướng nhanh chóng đến vùng lân cận, sau đó chuyển xuống các tầng dưới dày đặc để định vị điểm gần nhất."
    },
    9: {
        "prompt": "Trong quy trình chuẩn bị dữ liệu offline (offline ingestion pipeline) cho hệ thống RAG, thứ tự xử lý nào dưới đây là chuẩn xác nhất?",
        "options": [
            {"id": "a", "text": "Clean văn bản → Parse định dạng → Embed vectors → Chia Chunk → Trích xuất Metadata → Lưu Vector Index."},
            {"id": "b", "text": "Parse tài liệu → Clean dữ liệu → Phân đoạn (Chunk) → Bổ sung Metadata/Provenance → Tạo Embeddings → Lưu trữ vào Vector Index."},
            {"id": "c", "text": "Tạo Embeddings trước toàn văn → Parse tài liệu → Chia Chunk → Lưu Vector Index."},
            {"id": "d", "text": "Chia Chunk → Parse tài liệu → Trích xuất Metadata → Tạo Embeddings → Lưu Vector Index."}
        ],
        "explanation": "Pipeline chuẩn phải bóc tách tài liệu (parse), làm sạch (clean), phân đoạn (chunking), gắn metadata & provenance cho từng chunk, sau đó mới tính vector embedding và lưu trữ vào chỉ mục."
    },
    10: {
        "prompt": "Trong bộ tiêu chuẩn đánh giá RAGAS, chỉ số `Context Precision` đo lường khía cạnh chất lượng nào của giai đoạn retrieval?",
        "options": [
            {"id": "a", "text": "Tỷ lệ các thông tin trọng yếu cần thiết được truy xuất đầy đủ trong toàn bộ ngữ cảnh."},
            {"id": "b", "text": "Mức độ ưu tiên xếp các chunk thực sự liên quan và hữu ích lên những vị trí đầu tiên trong danh sách kết quả."},
            {"id": "c", "text": "Mức độ trung thực của câu trả lời do LLM sinh ra so với bằng chứng có trong ngữ cảnh."},
            {"id": "d", "text": "Mức độ bám sát của câu trả lời so với câu hỏi ban đầu của người dùng."}
        ],
        "explanation": "Context Precision đo lường chất lượng xếp hạng (ranking quality): các chunk mang thông tin hữu ích có được đưa lên các vị trí rank cao (top) trong context hay không."
    },
    11: {
        "prompt": "Trong đánh giá RAGAS, chỉ số `Context Recall` thể hiện điều gì?",
        "options": [
            {"id": "a", "text": "Tỷ lệ phần trăm các câu luận điểm do LLM sinh ra có thể kiểm chứng được từ tài liệu gốc."},
            {"id": "b", "text": "Tỷ lệ phần trăm các thông tin và bằng chứng cần thiết trong ground truth được hệ thống tìm kiếm thu thập đầy đủ vào context."},
            {"id": "c", "text": "Tốc độ phản hồi trung bình của hệ thống khi truy vấn lại một tài liệu trong bộ nhớ đệm cache."},
            {"id": "d", "text": "Độ dài trung bình của các đoạn văn bản được đưa vào prompt."}
        ],
        "explanation": "Context Recall đo lường mức độ bao phủ: liệu ngữ cảnh truy xuất được có chứa đầy đủ tất cả các ý cần thiết để trả lời câu hỏi theo chuẩn ground-truth hay không."
    },
    12: {
        "prompt": "Chỉ số `Faithfulness` (Độ trung thực) trong RAGAS cảnh báo rủi ro nào của mô hình ngôn ngữ lớn?",
        "options": [
            {"id": "a", "text": "Mô hình trả lời quá ngắn gọn và không cung cấp đầy đủ chi tiết cho người học."},
            {"id": "b", "text": "Mô hình đưa ra các khẳng định bịa đặt (hallucination) không được chứng minh bởi bất kỳ bằng chứng nào trong context được cấp."},
            {"id": "c", "text": "Mô hình sử dụng từ ngữ không phù hợp với văn phong học thuật."},
            {"id": "d", "text": "Mô hình từ chối trả lời do câu hỏi nằm ngoài phạm vi huấn luyện."}
        ],
        "explanation": "Faithfulness đo lường tỷ lệ các câu khẳng định trong câu trả lời được hỗ trợ trực tiếp bởi các bằng chứng trong context, phát hiện các trường hợp mô hình tự bịa thông tin."
    },
    13: {
        "prompt": "Chỉ số `Answer Relevancy` trong RAGAS giúp đánh giá khía cạnh nào trong câu trả lời của mô hình?",
        "options": [
            {"id": "a", "text": "Câu trả lời có đi đúng trọng tâm câu hỏi của người dùng hay bị lan man, lạc đề sang nội dung khác."},
            {"id": "b", "text": "Câu trả lời có chứa đúng mã nguồn chương trình mà người dùng yêu cầu hay không."},
            {"id": "c", "text": "Mức độ tuân thủ định dạng JSON theo schema đã chỉ định trong prompt."},
            {"id": "d", "text": "Thời gian mô hình hoàn thành quá trình sinh văn bản."}
        ],
        "explanation": "Answer Relevancy đánh giá mức độ trực diện và phù hợp của câu trả lời đối với câu hỏi gốc, phạt các trường hợp trả lời vòng vo hoặc lạc đề."
    },
    14: {
        "prompt": "Khi đánh giá hệ thống RAG, bạn phát hiện chỉ số `Faithfulness` đạt 0.98 nhưng `Context Recall` chỉ đạt 0.45. Hiện tượng này phản ánh điều gì và cần cải thiện khâu nào?",
        "options": [
            {"id": "a", "text": "Mô hình trả lời rất trung thực với dữ liệu được nạp nhưng khâu Retrieval không lấy đủ tài liệu cần thiết; cần tối ưu chunking, embedding hoặc mở rộng query."},
            {"id": "b", "text": "Khâu Retrieval lấy rất đầy đủ tài liệu nhưng mô hình LLM bị ảo giác nặng; cần siết chặt system prompt."},
            {"id": "c", "text": "Hệ thống đang hoạt động hoàn hảo và không cần bất kỳ tinh chỉnh nào."},
            {"id": "d", "text": "Cần thay đổi toàn bộ thuật toán sinh câu trả lời sang zero-shot."}
        ],
        "explanation": "Faithfulness cao nghĩa là LLM bám sát context, nhưng Context Recall thấp chỉ ra rằng bước Retrieval đã bỏ sót nhiều thông tin cốt lõi cần thiết. Cần tinh chỉnh lại giai đoạn tìm kiếm và tiền xử lý tài liệu."
    },
    15: {
        "prompt": "Đối với các câu hỏi phức tạp yêu cầu so sánh hoặc suy luận bắc cầu nhiều bước (multi-hop reasoning) mà kỹ thuật RAG đơn tầng gặp khó khăn, kiến trúc GraphRAG mang lại lợi thế vượt trội nhờ điều gì?",
        "options": [
            {"id": "a", "text": "GraphRAG tự động bỏ qua toàn bộ vector database để đọc trực tiếp file PDF gốc mỗi khi truy vấn."},
            {"id": "b", "text": "GraphRAG liên kết các thực thể và khái niệm thông qua các mối quan hệ có cấu trúc (edges), cho phép duyệt đồ thị 1-2 hop để kết nối các bằng chứng phân tán."},
            {"id": "c", "text": "GraphRAG giảm kích thước toàn bộ embedding vector về 1 chiều để tăng tốc độ tính toán."},
            {"id": "d", "text": "GraphRAG cho phép thực thi mã nguồn tùy ý trên máy chủ mà không cần sandbox."}
        ],
        "explanation": "GraphRAG kết nối các đoạn thông tin rời rạc thông qua mạng lưới quan hệ giữa các thực thể, cho phép duyệt đồ thị nhiều bước (multi-hop traversal) để thu thập đầy đủ các mảnh ghép kiến thức liên quan."
    },
    16: {
        "prompt": "Trong thiết kế hệ thống AI Agent, tại sao tính chất Idempotency (tính lũy đọng) của các Tool Actions lại đóng vai trò sống còn đối với sự ổn định của hệ thống?",
        "options": [
            {"id": "a", "text": "Idempotency giúp agent sinh văn bản nhanh hơn gấp hai lần so với thông thường."},
            {"id": "b", "text": "Khi mạng bị ngắt quãng hoặc agent thử lại (retry) một hành động, idempotency đảm bảo hành động đó không bị thực thi lặp lại nhiều lần gây sai lệch dữ liệu (như trừ tiền hai lần)."},
            {"id": "c", "text": "Idempotency cho phép agent truy cập cơ sở dữ liệu mà không cần thông qua lớp xác thực token."},
            {"id": "d", "text": "Idempotency là yêu cầu bắt buộc để chuyển đổi mô hình từ cloud về chạy offline trên thiết bị di động."}
        ],
        "explanation": "Tính lũy đọng đảm bảo khi một thao tác (ví dụ: tạo đơn, thanh toán, gửi email) được gọi lại nhiều lần với cùng một Idempotency-Key thì trạng thái hệ thống vẫn chỉ ghi nhận một lần duy nhất."
    },
    17: {
        "prompt": "Mô hình State Machine (máy trạng thái) hỗ trợ điều phối AI Agent hiệu quả hơn luồng code vòng lặp tự do (unconstrained loop) ở điểm cốt lõi nào?",
        "options": [
            {"id": "a", "text": "State machine giới hạn các trạng thái hợp lệ và định nghĩa rõ ràng các bước chuyển tiếp, giúp hệ thống dễ kiểm soát, gỡ lỗi và ngăn chặn agent rơi vào vòng lặp vô tận."},
            {"id": "b", "text": "State machine giúp tăng tốc độ suy luận của mô hình ngôn ngữ lớn."},
            {"id": "c", "text": "State machine loại bỏ hoàn toàn nhu cầu sử dụng prompt engineering."},
            {"id": "d", "text": "State machine tự động sửa đổi mã nguồn ứng dụng khi phát hiện lỗi runtime."}
        ],
        "explanation": "Máy trạng thái định nghĩa chặt chẽ các trạng thái có thể có, điều kiện chuyển trạng thái và giới hạn số bước, mang lại tính tất định (determinism) và khả năng kiểm toán cho luồng thực thi của agent."
    },
    18: {
        "prompt": "Cơ chế Checkpointing và Resume trong các framework điều phối agent (như LangGraph) mang lại lợi ích gì khi xử lý các tác vụ kéo dài (long-running workflows)?",
        "options": [
            {"id": "a", "text": "Tự động lưu trạng thái (state snapshot) sau mỗi bước thực thi, cho phép khôi phục chính xác phiên làm việc khi gặp sự cố mà không phải chạy lại từ đầu."},
            {"id": "b", "text": "Nén lịch sử hội thoại thành tệp zip để gửi qua email cho quản trị viên."},
            {"id": "c", "text": "Thay thế hoàn toàn cơ sở dữ liệu quan hệ của hệ thống."},
            {"id": "d", "text": "Tự động tăng temperature của mô hình khi gặp câu hỏi khó."}
        ],
        "explanation": "Checkpointing lưu lại trạng thái thực thi tại từng node; nếu có lỗi mạng hoặc tiến trình bị gián đoạn, agent có thể tiếp tục (resume) ngay từ điểm kiểm tra gần nhất một cách bền vững."
    },
    19: {
        "prompt": "Trong kiến trúc tương tác Human-in-the-Loop (HITL), quy trình nào dưới đây là chuẩn mực nhất khi agent chuẩn bị thực hiện một hành động có tác động lớn (high-stakes action như xóa dữ liệu hoặc chuyển tiền)?",
        "options": [
            {"id": "a", "text": "Agent tự động thực thi ngay lập tức rồi gửi thông báo đã hoàn thành vào log hệ thống."},
            {"id": "b", "text": "Agent tạm dừng quy trình (interrupt), lưu trạng thái chờ, hiển thị chi tiết hành động cho con người xem xét phê duyệt (approve/reject), rồi mới tiếp tục thực thi."},
            {"id": "c", "text": "Agent hỏi ý kiến một mô hình LLM khác nhỏ hơn để tự động quyết định thay con người."},
            {"id": "d", "text": "Agent tự động thử lại 10 lần trước khi thông báo thất bại cho người dùng."}
        ],
        "explanation": "Quy trình HITL chuẩn luôn ngắt tiến trình tại các hành động nhạy cảm (pivot step), duy trì trạng thái chờ duyệt và chỉ tiếp tục luồng sau khi nhận được sự đồng ý rõ ràng từ con người."
    },
    20: {
        "prompt": "Mô hình Circuit Breaker (ngắt mạch) bảo vệ hệ thống AI như thế nào khi một dịch vụ LLM Provider bên ngoài gặp sự cố sập nguồn hoặc quá tải kéo dài?",
        "options": [
            {"id": "a", "text": "Liên tục gửi thêm hàng nghìn request dồn dập cho đến khi dịch vụ phản hồi trở lại."},
            {"id": "b", "text": "Tự động chuyển sang trạng thái Open để chặn các request tiếp theo, kích hoạt phương án dự phòng (fallback) và định kỳ thăm dò (Half-Open) để tự phục hồi khi dịch vụ ổn định."},
            {"id": "c", "text": "Tắt toàn bộ máy chủ ứng dụng để bảo vệ phần cứng máy tính."},
            {"id": "d", "text": "Tự động nạp tiền vào tài khoản API của provider."}
        ],
        "explanation": "Circuit Breaker ngắt luồng gọi tới dịch vụ đang lỗi để tránh nghẽn tài nguyên và tích lũy độ trễ, đồng thời kích hoạt fallback mượt mà và tự động kết nối lại khi hạ tầng phục hồi."
    }
}

print("Paraphrase dictionary initialized.")
