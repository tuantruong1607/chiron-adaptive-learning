import json
from pathlib import Path

from .question_bank import build_diagnostic_questions
from .schemas import (
    Citation,
    Concept,
    ConceptEdge,
    Course,
    DiagnosticQuestion,
    LabControl,
    LabControlOption,
    LabDefinition,
    LabTransferPrompt,
    MasteryBand,
    QuestionOption,
    RelationType,
)

COURSE = Course(
    id="rag-intensive",
    title="Chiron AI Comprehensive Assessment",
    description="Ôn tập toàn khóa từ nền tảng AI/LLM đến RAG, agent, evaluation, alignment và vận hành production.",
    exam_date="2026-09-18",
    learner_count=1,
)


def citation(span: str, title: str, locator: str, excerpt: str) -> Citation:
    return Citation(source_span_id=span, title=title, locator=locator, excerpt=excerpt)


CONCEPTS = [
    Concept(
        id="chunking",
        name="Hierarchical chunking",
        summary="Chia tài liệu theo cấu trúc và giữ quan hệ parent-child giữa các đoạn.",
        objective="Thiết kế chunk có boundary ổn định và locator quay lại nguồn.",
        mastery=0.46,
        confidence=0.78,
        exam_weight=0.82,
        band=MasteryBand.DEVELOPING,
        x=14,
        y=27,
        citations=[
            citation(
                "pdf-07-p24-s2",
                "Track 3 Day 18",
                "Trang 24",
                "Metadata và cấu trúc chunk quyết định chất lượng retrieval.",
            )
        ],
    ),
    Concept(
        id="dense",
        name="Dense retrieval",
        summary="Biểu diễn semantic similarity bằng vector embedding.",
        objective="Phân tích khi dense retrieval bỏ sót exact term và identifier.",
        mastery=0.76,
        confidence=0.86,
        exam_weight=0.7,
        band=MasteryBand.SECURE,
        x=33,
        y=18,
        citations=[
            citation(
                "pdf-07-p63-s1",
                "Slide Day 07",
                "Trang 63",
                "Dense vectors phù hợp với truy vấn gần nghĩa.",
            )
        ],
    ),
    Concept(
        id="sparse",
        name="Sparse retrieval",
        summary="Tìm exact token và thuật ngữ hiếm bằng biểu diễn sparse.",
        objective="Kết hợp lexical evidence với semantic evidence.",
        mastery=0.58,
        confidence=0.72,
        exam_weight=0.68,
        band=MasteryBand.DEVELOPING,
        x=33,
        y=43,
        citations=[
            citation(
                "pdf-18-p28-s3",
                "Track 3 Day 18",
                "Trang 28",
                "Sparse retrieval giữ tín hiệu từ khóa và mã định danh.",
            )
        ],
    ),
    Concept(
        id="rrf",
        name="Reciprocal Rank Fusion",
        summary="Hợp nhất nhiều danh sách theo thứ hạng thay vì score thô.",
        objective="Tính RRF và giải thích tính ổn định giữa nhiều retriever.",
        mastery=0.31,
        confidence=0.65,
        exam_weight=0.9,
        band=MasteryBand.DEVELOPING,
        x=52,
        y=31,
        citations=[
            citation(
                "pdf-07-p69-s1",
                "Slide Day 07",
                "Trang 69",
                "RRF fuse kết quả dựa trên vị trí xếp hạng.",
            )
        ],
    ),
    Concept(
        id="metadata-filtering",
        name="Metadata and tenant filtering",
        summary="Giới hạn candidate theo tenant, course và quyền truy cập trước retrieval.",
        objective="Đặt authorization boundary trước candidate generation và giữ recall trong scope hợp lệ.",
        mastery=0.38,
        confidence=0.64,
        exam_weight=0.86,
        band=MasteryBand.DEVELOPING,
        x=51,
        y=50,
        citations=[
            citation(
                "c30965da-a1a8-5893-a494-dc0bc667531b",
                "Track 3 Day 18",
                "Metadata filtering",
                "Authorization và course filters phải giới hạn candidate trước retrieval.",
            )
        ],
    ),
    Concept(
        id="reranking",
        name="Cross-encoder reranking",
        summary="Chấm lại shortlist bằng mô hình đọc đồng thời query và document.",
        objective="Chọn rerank depth theo chất lượng, latency và chi phí.",
        mastery=0.42,
        confidence=0.69,
        exam_weight=0.88,
        band=MasteryBand.DEVELOPING,
        x=69,
        y=21,
        citations=[
            citation(
                "pdf-18-p54-s2",
                "Track 3 Day 18",
                "Trang 54",
                "Reranking cải thiện thứ tự top-k sau retrieval.",
            )
        ],
    ),
    Concept(
        id="citation",
        name="Citation verification",
        summary="Kiểm tra claim có được source span hỗ trợ trực tiếp hay không.",
        objective="Tách retrieval relevance khỏi citation entailment.",
        mastery=0.67,
        confidence=0.75,
        exam_weight=0.94,
        band=MasteryBand.SECURE,
        x=84,
        y=37,
        citations=[
            citation(
                "pdf-24-p61-s4",
                "Track 3 Day 24",
                "Trang 61",
                "Citation precision phải được đo độc lập với answer relevancy.",
            )
        ],
    ),
    Concept(
        id="graph-routing",
        name="Graph-lite routing",
        summary="Chỉ mở rộng quan hệ khi intent cần prerequisite hoặc multi-hop.",
        objective="Chọn relation whitelist, hop limit và latency budget.",
        mastery=0.22,
        confidence=0.61,
        exam_weight=0.79,
        band=MasteryBand.DEVELOPING,
        x=57,
        y=59,
        citations=[
            citation(
                "pdf-19-p43-s1",
                "Track 3 Day 19",
                "Trang 43",
                "Graph augmentation nên được route theo loại truy vấn.",
            )
        ],
    ),
    Concept(
        id="evaluation",
        name="RAG evaluation",
        summary="Đo retrieval, faithfulness và citation trên golden set có version.",
        objective="Thiết kế eval gate phát hiện regression trước deploy.",
        mastery=0.18,
        confidence=0.57,
        exam_weight=0.92,
        band=MasteryBand.NEW,
        x=78,
        y=65,
        citations=[
            citation(
                "pdf-24-p64-s2",
                "Track 3 Day 24",
                "Trang 64",
                "Evaluation liên tục biến failure thành regression case.",
            )
        ],
    ),
]

EDGES = [
    ConceptEdge(
        id="e1",
        source="chunking",
        target="dense",
        relation=RelationType.PREREQUISITE_OF,
        weight=0.8,
    ),
    ConceptEdge(
        id="e2",
        source="chunking",
        target="sparse",
        relation=RelationType.PREREQUISITE_OF,
        weight=0.7,
    ),
    ConceptEdge(
        id="e3", source="dense", target="rrf", relation=RelationType.PREREQUISITE_OF, weight=0.9
    ),
    ConceptEdge(
        id="e4", source="sparse", target="rrf", relation=RelationType.PREREQUISITE_OF, weight=0.9
    ),
    ConceptEdge(
        id="e5",
        source="rrf",
        target="reranking",
        relation=RelationType.PREREQUISITE_OF,
        weight=0.85,
    ),
    ConceptEdge(
        id="e6",
        source="reranking",
        target="citation",
        relation=RelationType.APPLIES_TO,
        weight=0.65,
    ),
    ConceptEdge(
        id="e7",
        source="rrf",
        target="graph-routing",
        relation=RelationType.CONTRASTS_WITH,
        weight=0.55,
    ),
    ConceptEdge(
        id="e8",
        source="graph-routing",
        target="evaluation",
        relation=RelationType.APPLIES_TO,
        weight=0.74,
    ),
    ConceptEdge(
        id="e9", source="citation", target="evaluation", relation=RelationType.PART_OF, weight=0.82
    ),
    ConceptEdge(
        id="e10",
        source="metadata-filtering",
        target="dense",
        relation=RelationType.APPLIES_TO,
        weight=0.78,
    ),
    ConceptEdge(
        id="e11",
        source="metadata-filtering",
        target="sparse",
        relation=RelationType.APPLIES_TO,
        weight=0.78,
    ),
]

# The JSON taxonomy is the source of truth shared by diagnostic sampling and
# Graph-lite publication. The explicit objects above remain as historical seed
# fixtures, while every runtime adapter exposes the complete course map below.
_COURSE_TAXONOMY = json.loads(
    Path(__file__).with_name("course_taxonomy.json").read_text(encoding="utf-8")
)
_DOMAIN_INDEX = {
    domain["id"]: index for index, domain in enumerate(_COURSE_TAXONOMY["domains"])
}
_DOMAIN_NODE_INDEX: dict[str, int] = {}
CONCEPTS = []
for _node in _COURSE_TAXONOMY["nodes"]:
    _domain = _node["domain"]
    _index = _DOMAIN_NODE_INDEX.get(_domain, 0)
    _DOMAIN_NODE_INDEX[_domain] = _index + 1
    CONCEPTS.append(
        Concept(
            id=_node["id"],
            name=_node["name"],
            summary=_node["summary"],
            objective=f"Giải thích, so sánh trade-off và áp dụng {_node['name']} trong một tình huống thực tế.",
            mastery=0.0,
            confidence=0.0,
            exam_weight=min(1.0, 0.45 + len(_node.get("question_topics", [])) * 0.08),
            band=MasteryBand.NEW,
            x=12 + (_index % 4) * 24,
            y=14 + (_index // 4) * 22,
            citations=[
                citation(
                    f"course-taxonomy-{_node['id']}",
                    "Giáo trình Chiron AI toàn khóa",
                    _node["name"],
                    _node["summary"],
                )
            ],
        )
    )

EDGES = [
    ConceptEdge(
        id=edge["id"],
        source=edge["source"],
        target=edge["target"],
        relation=RelationType(edge["relation"]),
        weight=0.8,
    )
    for edge in _COURSE_TAXONOMY["edges"]
]

FOUNDATION_DIAGNOSTIC_QUESTIONS = [
    (
        DiagnosticQuestion(
            id="diag-foundation-01",
            concept_id="ai_llm_foundations",
            prompt="Phát biểu nào mô tả đúng nhất cách một LLM sinh câu trả lời?",
            options=[
                QuestionOption(id="a", text="Tra cứu nguyên văn một câu trả lời cố định trong cơ sở dữ liệu"),
                QuestionOption(id="b", text="Dự đoán token tiếp theo theo xác suất dựa trên context"),
                QuestionOption(id="c", text="Luôn suy luận theo cùng một chuỗi bước xác định"),
                QuestionOption(id="d", text="Chỉ sao chép dữ liệu huấn luyện gần nhất"),
            ],
        ),
        "b",
    ),
    (
        DiagnosticQuestion(
            id="diag-foundation-02",
            concept_id="prompt_engineering",
            prompt="Thông tin nào nên đặt ở system prompt thay vì lặp lại trong từng câu hỏi người dùng?",
            options=[
                QuestionOption(id="a", text="Vai trò, nguyên tắc an toàn và định dạng đầu ra ổn định"),
                QuestionOption(id="b", text="Một dữ kiện chỉ dùng cho đúng câu hỏi hiện tại"),
                QuestionOption(id="c", text="Toàn bộ tài liệu retrieval chưa lọc"),
                QuestionOption(id="d", text="Secret key của provider"),
            ],
        ),
        "a",
    ),
    (
        DiagnosticQuestion(
            id="diag-foundation-03",
            concept_id="tool_calling",
            prompt="Thiết kế nào giúp tool calling an toàn và kiểm tra được nhất?",
            options=[
                QuestionOption(id="a", text="Cho model tự tạo lệnh shell bất kỳ"),
                QuestionOption(id="b", text="Schema typed, validate input và kiểm tra quyền trước khi thực thi"),
                QuestionOption(id="c", text="Đưa token truy cập vào mô tả tool"),
                QuestionOption(id="d", text="Tự động retry mọi action ghi dữ liệu"),
            ],
        ),
        "b",
    ),
    (
        DiagnosticQuestion(
            id="diag-foundation-04",
            concept_id="ai_problem_framing",
            prompt="Một problem statement tốt cho sản phẩm AI cần ưu tiên điều gì?",
            options=[
                QuestionOption(id="a", text="Chọn model trước khi biết người dùng"),
                QuestionOption(id="b", text="Mô tả người dùng, outcome, ràng buộc và tiêu chí thành công đo được"),
                QuestionOption(id="c", text="Liệt kê càng nhiều tính năng càng tốt"),
                QuestionOption(id="d", text="Chỉ đặt mục tiêu tăng độ chính xác"),
            ],
        ),
        "b",
    ),
    (
        DiagnosticQuestion(
            id="diag-foundation-05",
            concept_id="ai_product_delivery",
            prompt="Metric nào phản ánh giá trị sản phẩm AI tốt hơn việc chỉ đo model accuracy?",
            options=[
                QuestionOption(id="a", text="Outcome người dùng kèm chất lượng, latency và tỷ lệ escalation"),
                QuestionOption(id="b", text="Số tham số của model"),
                QuestionOption(id="c", text="Số prompt đã viết"),
                QuestionOption(id="d", text="Số agent trong kiến trúc"),
            ],
        ),
        "a",
    ),
]

DIAGNOSTIC_EXPLANATIONS = {
    "diag-foundation-01": "LLM sinh văn bản bằng cách ước lượng phân phối xác suất của token tiếp theo từ context hiện có.",
    "diag-foundation-02": "System prompt phù hợp với vai trò và quy tắc ổn định; dữ kiện theo câu hỏi nên nằm ở user/context.",
    "diag-foundation-03": "Tool contract typed, validation và authorization giúp chặn input sai và hành động vượt quyền.",
    "diag-foundation-04": "Problem framing phải gắn nhu cầu người dùng với outcome, constraint và phép đo thành công.",
    "diag-foundation-05": "Sản phẩm AI phải tạo outcome hữu ích trong giới hạn chất lượng, độ trễ và rủi ro vận hành.",
}

_BANK_DIAGNOSTIC_QUESTIONS, _BANK_DIAGNOSTIC_EXPLANATIONS = build_diagnostic_questions(20)
QUESTIONS = FOUNDATION_DIAGNOSTIC_QUESTIONS + _BANK_DIAGNOSTIC_QUESTIONS
DIAGNOSTIC_EXPLANATIONS.update(_BANK_DIAGNOSTIC_EXPLANATIONS)

def range_control(
    control_id: str,
    label: str,
    default: float,
    minimum: float,
    maximum: float,
    step: float,
    help_text: str,
) -> LabControl:
    return LabControl(
        id=control_id,
        label=label,
        kind="range",
        default=default,
        minimum=minimum,
        maximum=maximum,
        step=step,
        help_text=help_text,
    )


def toggle_control(control_id: str, label: str, default: bool, help_text: str) -> LabControl:
    return LabControl(
        id=control_id,
        label=label,
        kind="toggle",
        default=default,
        help_text=help_text,
    )


def select_control(
    control_id: str,
    label: str,
    default: str,
    options: tuple[tuple[str, str], ...],
    help_text: str,
) -> LabControl:
    return LabControl(
        id=control_id,
        label=label,
        kind="select",
        default=default,
        options=[LabControlOption(value=value, label=option_label) for value, option_label in options],
        help_text=help_text,
    )


LABS = [
    LabDefinition(
        id="hybrid-search",
        title="Hybrid Search Control Room",
        objective="Cấu hình fusion, rerank và tenant filter cho một retrieval pipeline an toàn.",
        brief="Tìm chính xác thuật ngữ hiếm nhưng vẫn giữ semantic recall trong ngân sách latency.",
        estimated_minutes=18,
        success_threshold=75,
        concept_id="reciprocal_rank_fusion",
        source_span_ids=["c54b8f84-4b7c-5e47-b9c3-cab7162b9bf4"],
        scenario="Một tenant báo mã lỗi hiếm không xuất hiện trong top-10. Cấu hình pipeline an toàn dưới 220 ms.",
        controls=[
            range_control("dense_weight", "Dense weight", 0.5, 0, 1, 0.05, "Semantic recall"),
            range_control("sparse_weight", "Sparse weight", 0.5, 0, 1, 0.05, "Exact terms"),
            range_control("rerank_depth", "Rerank depth", 20, 1, 70, 1, "Latency and precision"),
            toggle_control("tenant_filter", "Tenant filter trước retrieval", False, "Security boundary"),
        ],
        transfer_prompts=[
            LabTransferPrompt(
                id="reasoning",
                prompt="Vì sao dùng RRF thay vì cộng raw score?",
                placeholder="Phân biệt rank và raw score giữa các retriever",
            )
        ],
        learning_resource_id="rrf",
    ),
    LabDefinition(
        id="chunking-strategy",
        title="Chunking Strategy Workshop",
        objective="Chọn boundary parent-child ổn định và giữ source locator.",
        brief="Cân bằng continuity, retrieval precision và citation stability.",
        estimated_minutes=20,
        success_threshold=75,
        concept_id="chunking",
        source_span_ids=["5a51c6c4-07eb-57a2-82ff-7681f1738879"],
        scenario="Tài liệu có heading sâu, bảng và code block. Thiết kế chunk để câu trả lời vẫn mở đúng nguồn.",
        controls=[
            select_control("strategy", "Chunking strategy", "fixed", (("fixed", "Fixed"), ("hierarchical", "Hierarchical"), ("parent-child", "Parent-child")), "Cấu trúc hierarchy"),
            range_control("chunk_size", "Chunk size", 500, 200, 1200, 50, "Token budget"),
            range_control("overlap", "Overlap", 50, 0, 250, 10, "Context continuity"),
            toggle_control("preserve_locators", "Giữ source locator", True, "Citation stability"),
        ],
        transfer_prompts=[LabTransferPrompt(id="boundary", prompt="Khi nào boundary theo heading tốt hơn cắt cố định?", placeholder="Nối section boundary với citation/locator")],
        learning_resource_id="chunking",
    ),
    LabDefinition(
        id="rrf-ranking",
        title="RRF Ranking Trade-offs",
        objective="Hợp nhất ranked lists mà không so raw score khác thang đo.",
        brief="Tune fusion và giải thích tính ổn định của rank-based normalization.",
        estimated_minutes=18,
        success_threshold=75,
        concept_id="reciprocal_rank_fusion",
        source_span_ids=["196d7f1f-56f1-5416-8a32-b4513bf90ee1"],
        scenario="Dense tìm đúng nghĩa, BM25 bắt exact term. Hợp nhất hai danh sách mà không thiên vị thang điểm.",
        controls=[
            select_control("fusion", "Fusion method", "weighted-sum", (("weighted-sum", "Weighted raw score"), ("rrf", "Reciprocal Rank Fusion")), "Score compatibility"),
            range_control("rrf_k", "RRF constant k", 60, 10, 120, 5, "Rank damping"),
            range_control("candidate_depth", "Candidate depth", 20, 5, 60, 1, "Recall and cost"),
        ],
        transfer_prompts=[
            LabTransferPrompt(id="reasoning", prompt="Vì sao raw score của dense và sparse không nên so trực tiếp?"),
            LabTransferPrompt(id="failure", prompt="Exact term hiếm bị bỏ sót thì retriever nào cần giữ tín hiệu?"),
        ],
        learning_resource_id="rrf",
    ),
    LabDefinition(
        id="metadata-filtering",
        title="Metadata and Tenant Filtering",
        objective="Áp dụng authorization và course filters trước retrieval.",
        brief="Ngăn rò rỉ chéo tenant trong khi vẫn giữ candidate hữu ích.",
        estimated_minutes=18,
        success_threshold=75,
        concept_id="metadata_filtering",
        source_span_ids=["c30965da-a1a8-5893-a494-dc0bc667531b"],
        scenario="Một query giống nhau tồn tại ở hai tenant. Chỉ dữ liệu của enrollment hiện tại được phép vào candidate set.",
        controls=[
            toggle_control("tenant_filter", "Tenant filter", False, "Mandatory authorization"),
            toggle_control("course_filter", "Course enrollment filter", False, "Course boundary"),
            select_control("filter_stage", "Filter stage", "post", (("post", "Post-filter"), ("pre", "Pre-filter")), "Security and recall"),
        ],
        transfer_prompts=[
            LabTransferPrompt(id="isolation", prompt="Vì sao tenant filter là authorization boundary, không chỉ là ranking hint?"),
            LabTransferPrompt(id="recall", prompt="Pre-filter ảnh hưởng candidate recall và top-k như thế nào?"),
        ],
        learning_resource_id="metadata-filtering",
    ),
    LabDefinition(
        id="rag-evaluation",
        title="RAG Evaluation Diagnosis",
        objective="Biến retrieval và citation failures thành regression cases.",
        brief="Tách retrieval relevance, faithfulness và citation correctness.",
        estimated_minutes=22,
        success_threshold=75,
        concept_id="rag_evaluation",
        source_span_ids=["6bc653d6-19b4-5f79-ba52-646751098ca7"],
        scenario="Một câu trả lời trôi chảy nhưng citation không hỗ trợ claim. Thiết kế gate xác định đúng stage bị lỗi.",
        controls=[
            range_control("faithfulness_gate", "Faithfulness gate", 0.7, 0, 1, 0.05, "Generation grounding"),
            range_control("context_recall_gate", "Context recall gate", 0.7, 0, 1, 0.05, "Retrieval coverage"),
            toggle_control("verify_citations", "Verify citations", False, "Claim support"),
            toggle_control("persist_regression", "Persist regression case", False, "Release safety"),
        ],
        transfer_prompts=[
            LabTransferPrompt(id="diagnosis", prompt="Làm sao tách lỗi retrieval khỏi lỗi generation/faithfulness?"),
            LabTransferPrompt(id="gate", prompt="Release gate cần so sánh với baseline nào?"),
        ],
        learning_resource_id="evaluation",
    ),
    LabDefinition(
        id="graph-lite-routing",
        title="Graph-lite Routing",
        objective="Dùng bounded graph expansion cho prerequisite hoặc multi-hop intent.",
        brief="Chọn hop và cost limits mà không làm giảm direct factual queries.",
        estimated_minutes=20,
        success_threshold=75,
        concept_id="multi_hop_retrieval",
        source_span_ids=["bb1a06df-b5ce-55a1-9c2b-0a2e69a61ea1", "a26b72c3-30d7-5675-9a2d-6ee59554281f"],
        scenario="Direct fact chỉ cần hybrid retrieval, còn prerequisite query cần mở graph có giới hạn.",
        controls=[
            select_control("routing", "Routing mode", "always-graph", (("always-graph", "Always graph"), ("adaptive", "Adaptive by intent"), ("hybrid-only", "Hybrid only")), "Query intent"),
            range_control("max_hops", "Max graph hops", 2, 1, 4, 1, "Traversal bound"),
            range_control("expansion_limit", "Expansion limit", 8, 2, 20, 1, "Latency budget"),
            toggle_control("direct_fallback", "Direct-fact fallback", True, "Regression guard"),
        ],
        transfer_prompts=[
            LabTransferPrompt(id="routing", prompt="Query intent nào cần prerequisite hoặc multi-hop routing?"),
            LabTransferPrompt(id="regression", prompt="Gate nào bảo vệ direct facts khỏi regression?"),
        ],
        learning_resource_id="graph-routing",
    ),
]

LAB = LABS[0]
