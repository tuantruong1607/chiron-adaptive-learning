from datetime import UTC, datetime
from enum import StrEnum
from typing import Annotated, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MasteryBand(StrEnum):
    NEW = "new"
    DEVELOPING = "developing"
    SECURE = "secure"
    MASTERED = "mastered"


class RelationType(StrEnum):
    PREREQUISITE_OF = "prerequisite_of"
    PART_OF = "part_of"
    CONTRASTS_WITH = "contrasts_with"
    APPLIES_TO = "applies_to"
    CAUSES = "causes"


class Citation(BaseModel):
    source_span_id: str
    title: str
    locator: str
    excerpt: str


class SourceLocator(Citation):
    source_type: str
    locator_kind: str
    label: str | None = None
    page: int | None = None
    section_title: str | None = None
    heading: str | None = None
    section_id: str | None = None
    source_file: str | None = None
    order: int | None = None
    extraction_method: str | None = None


class Concept(BaseModel):
    id: str
    name: str
    summary: str
    objective: str
    mastery: Annotated[float, Field(ge=0, le=1)]
    confidence: Annotated[float, Field(ge=0, le=1)]
    exam_weight: Annotated[float, Field(ge=0, le=1)]
    band: MasteryBand
    x: float
    y: float
    citations: list[Citation]


class ConceptEdge(BaseModel):
    id: str
    source: str
    target: str
    relation: RelationType
    weight: Annotated[float, Field(ge=0, le=1)]


class KnowledgeMap(BaseModel):
    course_id: str
    version: str
    nodes: list[Concept]
    edges: list[ConceptEdge]


class LearningResourceStep(BaseModel):
    title: str
    explanation: str
    example: str


class LearningResource(BaseModel):
    concept_id: str
    title: str
    why_it_matters: str
    estimated_minutes: int
    learning_outcome: str
    key_ideas: list[str] = Field(min_length=2)
    worked_example: list[LearningResourceStep] = Field(min_length=2)
    common_mistakes: list[str] = Field(min_length=1)
    retrieval_prompt: str
    citations: list[Citation] = Field(min_length=1)


class Course(BaseModel):
    id: str
    title: str
    description: str
    exam_date: str
    learner_count: int


class LoginRequest(BaseModel):
    tenant_slug: Annotated[str, Field(min_length=2, max_length=120)]
    email: Annotated[str, Field(min_length=3, max_length=320)]
    password: Annotated[str, Field(min_length=8, max_length=256)]


class AccessTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: Literal["bearer"] = "bearer"
    expires_in: int
    refresh_expires_in: int


class RefreshTokenRequest(BaseModel):
    refresh_token: Annotated[str, Field(min_length=32, max_length=1024)]


class LogoutRequest(RefreshTokenRequest):
    pass


class PrincipalOut(BaseModel):
    user_id: UUID
    tenant_id: UUID
    role: Literal["learner", "instructor", "admin"]


class QuestionOption(BaseModel):
    id: str
    text: str


class DiagnosticQuestion(BaseModel):
    id: str
    concept_id: str
    prompt: str
    options: list[QuestionOption]


class AnswerInput(BaseModel):
    question_id: str
    option_id: str


class DiagnosticAnswerReview(BaseModel):
    question_id: str
    concept_id: str
    selected_option_id: str
    correct_option_id: str
    correct: bool
    explanation: str


class DiagnosticSubmission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    answers: Annotated[list[AnswerInput], Field(min_length=1)]
    self_assessments: dict[str, Annotated[int, Field(ge=1, le=5)]] = Field(
        default_factory=dict,
        description="Optional 1-5 confidence per concept; never treated as measured mastery.",
    )


class MasteryUpdate(BaseModel):
    concept_id: str
    previous: float | None
    current: float
    evidence: str
    diagnostic_status: Literal["not_assessed", "unverified", "partial", "verified"]
    evidence_confidence: Annotated[float, Field(ge=0, le=1)]
    confidence_gap: float


class PlanItem(BaseModel):
    id: str
    concept_id: str
    title: str
    activity: Literal["lesson", "retrieval", "lab", "recheck"]
    duration_minutes: int
    reason: str
    expected_gain: float
    day_offset: Annotated[int, Field(ge=0)] = 0
    priority_rank: Annotated[int, Field(ge=1)] = 1
    priority_score: Annotated[float, Field(ge=0, le=1)] = 0


class DeferredPlanItem(BaseModel):
    concept_id: str
    title: str
    duration_minutes: int
    reason: str


class StudyPlan(BaseModel):
    id: UUID
    title: str
    total_minutes: int
    generated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    items: list[PlanItem]
    horizon_days: Literal[3, 4] = 4
    daily_minutes: Annotated[int, Field(ge=30, le=480)] = 120
    deferred: list[DeferredPlanItem] = Field(default_factory=list)
    component_scores: dict[str, dict[str, float]] = Field(default_factory=dict)
    planner_version: str = "cram-planner-v1"


class LearningStateOut(BaseModel):
    concept_id: str
    self_confidence: Annotated[float, Field(ge=0, le=1)]
    diagnostic_status: Literal["not_assessed", "unverified", "partial", "verified"]
    mastery: Annotated[float | None, Field(ge=0, le=1)] = None
    evidence_confidence: Annotated[float | None, Field(ge=0, le=1)] = None
    confidence_gap: float | None = None
    misconception: bool = False
    evidence_ids: list[str] = Field(default_factory=list)
    version: str


class DiagnosticResult(BaseModel):
    attempt_id: UUID
    score: int
    total: int
    mastery_updates: list[MasteryUpdate]
    answer_reviews: list[DiagnosticAnswerReview] = Field(default_factory=list)
    plan: StudyPlan


class OnboardingStatus(BaseModel):
    completed: bool
    question_count: int
    next_path: Literal["/diagnostic", "/map"]


class MockExamAnswer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question_id: str
    option_id: str | None = None
    text: Annotated[str | None, Field(max_length=12000)] = None


class MockExamSubmission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    answers: Annotated[list[MockExamAnswer], Field(max_length=100)]


class MockExamResult(BaseModel):
    form_id: str
    score: float
    total: int = 100
    objective_score: int
    objective_total: int = 90
    constructed_score: float
    constructed_total: int = 10
    grading_mode: Literal["llm", "hybrid", "deterministic"]
    providers: list[str] = Field(default_factory=list)
    objective_reviews: list[dict] = Field(default_factory=list)
    constructed_reviews: list[dict] = Field(default_factory=list)


class TutorRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: Annotated[str, Field(min_length=3, max_length=1000)]
    concept_id: str | None = None
    course: Annotated[str, Field(min_length=2, max_length=120)] = "rag-intensive"
    thread_id: UUID | None = None
    data_sensitivity: Literal["public", "synthetic", "private", "restricted"] = "private"


class TutorAnswer(BaseModel):
    answer: str
    confidence: float
    citations: list[Citation]
    trace_id: UUID
    refused: bool = False
    provider: str = "mock"
    model: str | None = None
    used_fallback: bool = False
    fallback_reason: str | None = None
    degraded: bool = False
    thread_id: UUID | None = None
    route: Literal["direct", "prerequisite", "multi_hop"] = "direct"
    retrieval_strategy: Literal[
        "single_hybrid",
        "multi_query_hybrid_rrf",
        "graph_lite_no_expansion",
        "graph_lite_1hop",
        "graph_lite_2hop",
    ] = "single_hybrid"
    memory_turns: Annotated[int, Field(ge=0, le=8)] = 0


class RetrievalHit(BaseModel):
    concept_id: str | None = None
    score: float
    text: str
    citation: Citation


class RetrievalResponse(BaseModel):
    query: str
    route: Literal["direct", "prerequisite", "multi_hop"]
    hits: list[RetrievalHit]
    retrieval_mode: Literal["hybrid", "bm25_only"] = "hybrid"
    degraded: bool = False
    strategy: Literal[
        "single_hybrid",
        "multi_query_hybrid_rrf",
        "graph_lite_no_expansion",
        "graph_lite_1hop",
        "graph_lite_2hop",
    ] = "single_hybrid"
    subqueries: list[str] = Field(default_factory=list)


class LabControlOption(BaseModel):
    value: str
    label: str


class LabControl(BaseModel):
    id: str
    label: str
    kind: Literal["range", "toggle", "select"]
    default: bool | float | int | str
    minimum: float | None = None
    maximum: float | None = None
    step: float | None = None
    options: list[LabControlOption] = Field(default_factory=list)
    help_text: str = ""


class LabTransferPrompt(BaseModel):
    id: str
    prompt: str
    placeholder: str = "Giải thích bằng lời của bạn"
    min_length: int = 12


class LabDefinition(BaseModel):
    id: str
    title: str
    objective: str
    brief: str
    estimated_minutes: int
    success_threshold: int
    concept_id: str
    source_span_ids: list[str] = Field(default_factory=list)
    scenario: str
    controls: list[LabControl] = Field(default_factory=list)
    transfer_prompts: list[LabTransferPrompt] = Field(default_factory=list)
    learning_resource_id: str | None = None
    learning_resource: LearningResource | None = None


class LabSubmission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    configuration: dict[str, bool | float | int | str] = Field(default_factory=dict)
    transfer_answers: dict[str, Annotated[str, Field(max_length=2000)]] = Field(
        default_factory=dict
    )
    understanding_answers: dict[str, str] = Field(default_factory=dict)
    dense_weight: Annotated[float | None, Field(ge=0, le=1)] = None
    sparse_weight: Annotated[float | None, Field(ge=0, le=1)] = None
    rerank_depth: Annotated[int | None, Field(ge=1, le=100)] = None
    tenant_filter: bool | None = None
    transfer_answer: Annotated[str | None, Field(min_length=12, max_length=1000)] = None


class LabResult(BaseModel):
    score: int
    passed: bool
    feedback: list[str]
    evidence_event_id: UUID
    mastery_update: MasteryUpdate | None = None
    study_plan: StudyPlan | None = None


class EssaySubmissionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    course: Annotated[str, Field(min_length=2, max_length=120)] = "rag-intensive"
    prompt: Annotated[str, Field(min_length=12, max_length=5000)]
    answer: Annotated[str, Field(min_length=1, max_length=20000)]
    rubric_id: Annotated[str, Field(min_length=2, max_length=120)]


class InternalEssayGradeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tenant_id: UUID


class EssayHumanReviewRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    score: Annotated[float, Field(ge=0)]
    max_score: Annotated[float, Field(gt=0)]
    feedback: Annotated[str, Field(min_length=1, max_length=5000)]
    criterion_scores: dict[str, float] = Field(default_factory=dict)


class EssayResponse(BaseModel):
    id: UUID
    course: str
    prompt: str
    answer: str
    rubric_id: str
    status: Literal["pending_ai_grading", "graded", "needs_human_review"]
    score: float | None = None
    max_score: float | None = None
    confidence: Annotated[float | None, Field(ge=0, le=1)] = None
    provider: str | None = None
    model: str | None = None
    feedback: str | None = None
    rubric_version: str | None = None
    criterion_scores: dict[str, float] = Field(default_factory=dict)
    human_review_required: bool = False
    graded_at: datetime | None = None
    reviewer_id: UUID | None = None
    created_at: datetime


class ErrorDetail(BaseModel):
    code: str
    message: str
    request_id: str
    details: dict = Field(default_factory=dict)


class ErrorEnvelope(BaseModel):
    error: ErrorDetail
