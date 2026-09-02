from .schemas import Citation, Concept, LearningResource, LearningResourceStep


def _citation(span_id: str, title: str, locator: str, excerpt: str) -> Citation:
    return Citation(
        source_span_id=span_id,
        title=title,
        locator=locator,
        excerpt=excerpt,
    )


# These are deliberately short, source-grounded micro-lessons.  Slides remain the
# reference corpus; this layer gives learners a usable explain -> example -> recall
# path before they enter a lab or ask the tutor.
LEARNING_RESOURCES = [
    LearningResource(
        concept_id="chunking",
        title="Chunking: chia để giữ đúng ngữ cảnh",
        why_it_matters="Chunk quá nhỏ làm mất ý; chunk quá lớn làm retrieval loãng và citation khó kiểm tra.",
        estimated_minutes=8,
        learning_outcome="Bạn chọn được boundary, kích thước và overlap phù hợp cho một tài liệu có heading, bảng hoặc code.",
        key_ideas=[
            "Ưu tiên boundary theo heading/section thay vì cắt giữa một ý.",
            "Parent-child giữ ngữ cảnh rộng nhưng vẫn trả về đoạn con chính xác.",
            "Mỗi chunk phải giữ source span và locator ổn định để mở lại nguồn.",
        ],
        worked_example=[
            LearningResourceStep(
                title="Tình huống",
                explanation="Một tài liệu có mục 2.1, bảng cấu hình và code block.",
                example="Không cắt giữa heading và bảng; xem section là boundary tự nhiên.",
            ),
            LearningResourceStep(
                title="Quyết định",
                explanation="Dùng parent-child, child khoảng 400–800 token và overlap vừa phải.",
                example="Child trả về claim; parent cung cấp ngữ cảnh khi cần giải thích.",
            ),
            LearningResourceStep(
                title="Kiểm chứng",
                explanation="Kiểm tra citation sau khi chunk: source span phải mở đúng section/page.",
                example="Nếu người học bấm citation mà rơi sang section khác, pipeline chưa đạt.",
            ),
        ],
        common_mistakes=[
            "Chọn fixed-size cho mọi loại tài liệu.",
            "Tăng overlap để chữa mọi lỗi context nhưng không kiểm soát chi phí.",
            "Để mất locator khi tạo child chunk.",
        ],
        retrieval_prompt="Hãy tự nói: boundary nào sẽ giúp người khác kiểm tra lại claim nhanh nhất?",
        citations=[
            _citation("5a51c6c4-07eb-57a2-82ff-7681f1738879", "Track 3 Day 18", "Trang 24", "Metadata và cấu trúc chunk quyết định chất lượng retrieval."),
        ],
    ),
    LearningResource(
        concept_id="dense",
        title="Dense retrieval: bắt đúng ý nghĩa",
        why_it_matters="Dense retrieval tốt với câu hỏi diễn đạt khác từ tài liệu, nhưng có thể bỏ sót mã lỗi hoặc exact term.",
        estimated_minutes=6,
        learning_outcome="Bạn nhận ra khi nào semantic similarity đủ dùng và khi nào cần bổ sung sparse retrieval.",
        key_ideas=[
            "Embedding đưa query và document về không gian vector để tìm gần nghĩa.",
            "Dense mạnh ở paraphrase và ngữ nghĩa tương đương.",
            "Identifier, mã lỗi và tên riêng hiếm thường cần tín hiệu lexical.",
        ],
        worked_example=[
            LearningResourceStep(title="Query gần nghĩa", explanation="Người học hỏi 'làm sao lưu phiên đăng nhập lâu hơn?'.", example="Dense có thể tìm đoạn nói về refresh token dù không lặp đúng từ trong câu hỏi."),
            LearningResourceStep(title="Blind spot", explanation="Người học hỏi 'ERR_CONN_04'.", example="Nếu embedding không phân biệt tốt mã hiếm, sparse/BM25 phải giữ tín hiệu exact term."),
        ],
        common_mistakes=["Coi dense là retriever duy nhất.", "Đánh đồng điểm vector với xác suất đúng.", "Không đo riêng nhóm query exact term."],
        retrieval_prompt="Ví dụ query nào trong sản phẩm của bạn là paraphrase, query nào là identifier?",
        citations=[_citation("pdf-07-p63-s1", "Slide Day 07", "Trang 63", "Dense vectors phù hợp với truy vấn gần nghĩa.")],
    ),
    LearningResource(
        concept_id="sparse",
        title="Sparse retrieval: giữ lại tín hiệu từ khóa",
        why_it_matters="Sparse retrieval bảo vệ các token có ý nghĩa chính xác mà semantic search dễ làm mờ.",
        estimated_minutes=6,
        learning_outcome="Bạn biết lúc nào sparse/BM25 là tín hiệu bắt buộc và cách kết hợp nó với dense.",
        key_ideas=[
            "Token hiếm, tên hàm, mã lỗi và thuật ngữ chuyên môn thường là lexical signal.",
            "Sparse không thay thế dense; nó bù blind spot của dense.",
            "Cần hợp nhất ranked lists bằng phương pháp không giả định raw score cùng thang đo.",
        ],
        worked_example=[
            LearningResourceStep(title="Exact term", explanation="Query chứa 'ERR_CONN_04 timeout'.", example="BM25 ưu tiên tài liệu có đúng mã ERR_CONN_04; dense có thể bổ sung tài liệu nói về timeout tương tự."),
            LearningResourceStep(title="Kết hợp", explanation="Hai retriever trả về hai danh sách khác nhau.", example="Giữ cả hai candidate list rồi dùng RRF trước rerank.")
        ],
        common_mistakes=["Chỉ tối ưu semantic recall.", "So sánh raw score sparse với dense trực tiếp.", "Không kiểm thử query có token hiếm."],
        retrieval_prompt="Nếu bỏ một token khỏi query, kết quả đúng có biến mất không? Nếu có, đó là lexical signal.",
        citations=[_citation("pdf-18-p28-s3", "Track 3 Day 18", "Trang 28", "Sparse retrieval giữ tín hiệu từ khóa và mã định danh.")],
    ),
    LearningResource(
        concept_id="rrf",
        title="RRF: hợp nhất theo thứ hạng",
        why_it_matters="Dense và sparse tạo score khác bản chất; RRF giúp một kết quả tốt ở cả hai danh sách không bị thang đo lấn át.",
        estimated_minutes=8,
        learning_outcome="Bạn giải thích được vì sao RRF dùng rank, chọn k/candidate depth và nhận diện trade-off latency.",
        key_ideas=[
            "RRF dùng đóng góp theo vị trí, không cộng raw score khác thang đo.",
            "k lớn làm ảnh hưởng của rank giảm chậm hơn; k nhỏ ưu tiên top rank mạnh hơn.",
            "RRF chỉ hợp nhất candidate; rerank là bước khác để đọc sâu query-document.",
        ],
        worked_example=[
            LearningResourceStep(title="Hai tín hiệu", explanation="Dense xếp A hạng 1, sparse xếp B hạng 1; raw score của hai hệ không tương thích.", example="Không cộng 0.82 của dense với 12.4 của BM25 như thể cùng đơn vị."),
            LearningResourceStep(title="RRF", explanation="Mỗi document nhận điểm từ rank trong từng list.", example="Một document xuất hiện cao ở cả hai list sẽ được nâng; document chỉ cao ở một list vẫn có cơ hội."),
            LearningResourceStep(title="Sau fusion", explanation="Shortlist cần được đọc lại theo query.", example="Rerank top 10–30 để cân bằng precision với latency."),
        ],
        common_mistakes=["Nói RRF chuẩn hóa embedding.", "Dùng RRF như một reranker.", "Tăng candidate depth vô hạn mà không đo latency."],
        retrieval_prompt="Hãy giải thích RRF cho một đồng đội bằng một câu không dùng công thức.",
        citations=[_citation("pdf-07-p69-s1", "Slide Day 07", "Trang 69", "RRF fuse kết quả dựa trên vị trí xếp hạng.")],
    ),
    LearningResource(
        concept_id="reranking",
        title="Reranking: đọc kỹ shortlist",
        why_it_matters="Retrieval tạo candidate nhanh; reranker giúp sắp xếp lại những ứng viên gần nhất với câu hỏi.",
        estimated_minutes=6,
        learning_outcome="Bạn chọn được rerank depth dựa trên chất lượng, ngân sách latency và giá trị của top-k.",
        key_ideas=["Reranker đọc query và document cùng nhau.", "Rerank sau fusion, không thay thế candidate generation.", "Depth càng lớn thường tăng chi phí; phải đo P95 và quality cùng lúc."],
        worked_example=[
            LearningResourceStep(title="Shortlist", explanation="Hybrid retrieval trả về 50 ứng viên.", example="Không cần rerank cả corpus; chọn top 10–30 theo budget."),
            LearningResourceStep(title="Trade-off", explanation="Depth 70 có thể tăng precision nhưng vượt SLA.", example="Chọn depth 20 rồi so sánh recall/faithfulness và P95 với baseline."),
        ],
        common_mistakes=["Rerank trước khi có candidate.", "Chỉ nhìn điểm relevance mà bỏ qua latency.", "Không có baseline để biết rerank thực sự cải thiện."],
        retrieval_prompt="Nếu tăng rerank depth, metric nào phải tăng và metric nào không được vượt ngưỡng?",
        citations=[_citation("pdf-18-p54-s2", "Track 3 Day 18", "Trang 54", "Reranking cải thiện thứ tự top-k sau retrieval.")],
    ),
    LearningResource(
        concept_id="citation",
        title="Citation verification: claim phải có bằng chứng",
        why_it_matters="Câu trả lời trôi chảy chưa đủ; người học cần biết claim nào thật sự được source span hỗ trợ.",
        estimated_minutes=7,
        learning_outcome="Bạn phân biệt relevance, entailment và citation correctness; đồng thời biết mở lại đúng locator.",
        key_ideas=["Relevance hỏi context có liên quan không.", "Faithfulness hỏi câu trả lời có bám context không.", "Citation precision hỏi citation có hỗ trợ đúng claim không."],
        worked_example=[
            LearningResourceStep(title="Claim", explanation="Câu trả lời nói 'RRF thay thế reranker'.", example="Nếu source chỉ nói RRF fuse theo rank, citation không đủ để hỗ trợ claim thay thế reranker."),
            LearningResourceStep(title="Sửa", explanation="Tách claim thành phần có thể kiểm chứng.", example="'RRF hợp nhất danh sách theo rank; rerank là bước khác' rồi gắn span tương ứng."),
        ],
        common_mistakes=["Dùng citation liên quan nhưng không entail claim.", "Đo citation bằng số lượng link.", "Không cho người học mở source locator."],
        retrieval_prompt="Mỗi claim trong câu trả lời đang được source span nào chứng minh?",
        citations=[_citation("pdf-24-p61-s4", "Track 3 Day 24", "Trang 61", "Citation precision phải được đo độc lập với answer relevancy.")],
    ),
    LearningResource(
        concept_id="metadata-filtering",
        title="Metadata filtering: ranh giới an toàn trước retrieval",
        why_it_matters="Filter tenant và course là authorization boundary; ranking không được phép nhìn thấy dữ liệu người học không có quyền xem.",
        estimated_minutes=7,
        learning_outcome="Bạn đặt đúng tenant/course filter trước candidate generation và giải thích trade-off recall trong phạm vi được phép.",
        key_ideas=["Tenant filter bảo vệ dữ liệu, không phải một tín hiệu ranking.", "Course/enrollment filter giới hạn scope hợp lệ.", "Pre-filter làm giảm candidate universe nhưng giữ recall đúng scope và tránh leak."],
        worked_example=[
            LearningResourceStep(title="Rủi ro", explanation="Cùng một query tồn tại ở hai tenant.", example="Post-filter sau retrieval có thể đã để document sai tenant đi vào pipeline hoặc context."),
            LearningResourceStep(title="Thiết kế", explanation="Áp dụng tenant_id và course_id trước retrieval.", example="Candidate set chỉ được tạo từ dữ liệu learner được phép truy cập."),
        ],
        common_mistakes=["Xem filter như một ranking hint.", "Lọc sau khi đã lấy context.", "Đánh đổi isolation để lấy thêm candidate ngoài scope."],
        retrieval_prompt="Trước khi tìm, hệ thống đã biết learner được phép xem những tenant/course nào chưa?",
        citations=[_citation("c30965da-a1a8-5893-a494-dc0bc667531b", "Track 3 Day 18", "Metadata filtering", "Authorization và course filters phải giới hạn candidate trước retrieval.")],
    ),
    LearningResource(
        concept_id="graph-routing",
        title="Graph-lite: chỉ mở rộng khi cần quan hệ",
        why_it_matters="Graph giúp nối prerequisite/multi-hop nhưng mở cho mọi query sẽ tăng nhiễu, latency và rủi ro regression direct fact.",
        estimated_minutes=8,
        learning_outcome="Bạn route đúng intent, giới hạn hop/expansion và giữ direct-fact fallback.",
        key_ideas=["Direct fact thường chỉ cần hybrid retrieval.", "Prerequisite hoặc multi-hop mới cần graph expansion.", "Mọi activation cần bounded hop, expansion limit và direct-fact gate."],
        worked_example=[
            LearningResourceStep(title="Direct fact", explanation="Query hỏi 'RRF dùng rank hay raw score?'.", example="Route hybrid-only; graph không thêm giá trị và có thể thêm nhiễu."),
            LearningResourceStep(title="Multi-hop", explanation="Query hỏi 'chunking ảnh hưởng citation verification thế nào?'.", example="Route adaptive qua quan hệ prerequisite/applies_to với tối đa 1–2 hop."),
            LearningResourceStep(title="Gate", explanation="So sánh direct-fact retrieval với baseline trước activate.", example="Nếu direct recall giảm, giữ graph ở trạng thái inactive và điều tra.")
        ],
        common_mistakes=["Always-graph cho mọi câu hỏi.", "Không giới hạn traversal.", "Activate graph trước khi vượt evaluation gate."],
        retrieval_prompt="Query này cần lấy một fact hay cần nối nhiều quan hệ? Hãy nêu lý do.",
        citations=[_citation("pdf-19-p43-s1", "Track 3 Day 19", "Trang 43", "Graph augmentation nên được route theo loại truy vấn.")],
    ),
    LearningResource(
        concept_id="evaluation",
        title="RAG evaluation: biến lỗi thành bài học",
        why_it_matters="Không đo đúng stage thì sửa prompt một cách mù; eval giúp biết lỗi nằm ở retrieval, generation hay citation.",
        estimated_minutes=9,
        learning_outcome="Bạn thiết kế được failure diagnosis, golden/holdout gate và regression case có version.",
        key_ideas=["Context recall kiểm tra evidence có được lấy lên không.", "Faithfulness kiểm tra câu trả lời có bám evidence không.", "Citation verification kiểm tra link có chứng minh claim không.", "Failure phải được lưu thành case để lần deploy sau không lặp lại."],
        worked_example=[
            LearningResourceStep(title="Chẩn đoán", explanation="Answer trôi chảy nhưng citation không hỗ trợ claim.", example="Nếu context recall tốt nhưng citation sai, ưu tiên kiểm tra generation/citation thay vì tăng top-k."),
            LearningResourceStep(title="Release gate", explanation="Một bản build mới thay đổi embedding hoặc graph route.", example="So với golden/holdout baseline; không đạt gate thì hold release."),
            LearningResourceStep(title="Học từ failure", explanation="Lưu query, expected evidence, actual evidence và version.", example="Case này trở thành regression test cho lần thay đổi tiếp theo."),
        ],
        common_mistakes=["Gộp mọi lỗi thành một điểm tổng.", "Chỉ kiểm tra answer relevancy.", "Không version baseline/regression case."],
        retrieval_prompt="Lỗi này bắt đầu ở candidate retrieval, claim generation hay citation locator?",
        citations=[_citation("pdf-24-p64-s2", "Track 3 Day 24", "Trang 64", "Evaluation liên tục biến failure thành regression case.")],
    ),
]

RESOURCE_BY_CONCEPT = {resource.concept_id: resource for resource in LEARNING_RESOURCES}

_CURATED_RESOURCE_ALIASES = {
    "dense_retrieval": "dense",
    "sparse_retrieval": "sparse",
    "hybrid_search_rrf": "rrf",
    "reranking_mmr": "reranking",
    "faithfulness_grounding": "citation",
    "metadata_filtered_search": "metadata-filtering",
    "graphrag_multi_hop": "graph-routing",
    "rag_evaluation": "evaluation",
}


def resource_for_concept(concept: Concept) -> LearningResource:
    curated_id = _CURATED_RESOURCE_ALIASES.get(concept.id, concept.id)
    curated = RESOURCE_BY_CONCEPT.get(curated_id)
    if curated is not None:
        return curated.model_copy(
            update={"concept_id": concept.id, "citations": concept.citations}
        )
    return LearningResource(
        concept_id=concept.id,
        title=f"{concept.name}: hiểu trước khi áp dụng",
        why_it_matters=concept.summary,
        estimated_minutes=7,
        learning_outcome=concept.objective,
        key_ideas=[
            concept.summary,
            "Xác định input, output và ranh giới trách nhiệm của concept này.",
            "So sánh trade-off và dùng source evidence để kiểm chứng quyết định.",
        ],
        worked_example=[
            LearningResourceStep(
                title="Nhận diện",
                explanation=f"Tìm tín hiệu cho thấy tình huống đang kiểm tra {concept.name}.",
                example="Gạch chân constraint, failure hoặc outcome được hỏi trước khi chọn giải pháp.",
            ),
            LearningResourceStep(
                title="Lập luận",
                explanation="Nêu lựa chọn, điều kiện áp dụng và trade-off thay vì chỉ nhớ định nghĩa.",
                example="Giải thích vì sao phương án đúng phù hợp constraint và phương án gần đúng bị loại.",
            ),
            LearningResourceStep(
                title="Kiểm chứng",
                explanation="Mở source locator và đối chiếu claim quan trọng với tài liệu khóa học.",
                example="Nếu source không hỗ trợ trực tiếp, thu hẹp claim hoặc tìm evidence khác.",
            ),
        ],
        common_mistakes=[
            "Học thuộc tên nhưng không chỉ ra được điều kiện áp dụng.",
            "Bỏ qua trade-off về chất lượng, latency, chi phí hoặc rủi ro.",
            "Kết luận khi chưa đối chiếu nguồn khóa học.",
        ],
        retrieval_prompt=(
            f"Hãy giải thích {concept.name} bằng lời của bạn, rồi nêu một tình huống nên dùng "
            "và một tình huống không nên dùng."
        ),
        citations=concept.citations,
    )


def resources_for_concepts(concepts: list[Concept]) -> list[LearningResource]:
    return [resource_for_concept(concept) for concept in concepts]
