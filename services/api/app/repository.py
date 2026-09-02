from collections import defaultdict
from dataclasses import replace
from datetime import date
from threading import Lock
from uuid import uuid4

from .adaptive import DiagnosticStatus, EvidenceSignal, KnowledgeState
from .adaptive.contracts import LearningUnit
from .adaptive.mastery import update_knowledge_state
from .adaptive.planner import build_cram_plan
from .adaptive.priority import rank_learning_units
from .labs import canonical_lab_concept_id
from .labs import score_lab as score_lab_submission
from .schemas import (
    DeferredPlanItem,
    DiagnosticAnswerReview,
    DiagnosticResult,
    DiagnosticSubmission,
    KnowledgeMap,
    LabResult,
    LabSubmission,
    LearningStateOut,
    MasteryUpdate,
    PlanItem,
    RetrievalHit,
    RetrievalResponse,
    StudyPlan,
    TutorAnswer,
)
from .seed import CONCEPTS, COURSE, DIAGNOSTIC_EXPLANATIONS, EDGES, LABS, QUESTIONS


class AdaptiveLearningRepository:
    """In-memory adapter around the production-shaped deterministic domain core.

    State is isolated behind this boundary. A PostgreSQL implementation can replace
    the adapter without changing mastery, priority, planner, or API contracts.
    """

    def __init__(self) -> None:
        self._lock = Lock()
        self._idempotent_results: dict[str, DiagnosticResult] = {}
        self._idempotent_lab_results: dict[str, LabResult] = {}
        self._diagnostic_completed = False
        self._states = {
            concept.id: KnowledgeState(
                concept_id=concept.id,
                self_confidence=concept.confidence,
                diagnostic_status=DiagnosticStatus.PARTIAL,
                mastery=concept.mastery,
                evidence_confidence=concept.confidence,
                confidence_gap=round(concept.confidence - concept.mastery, 4),
                evidence_ids=(f"seed-{concept.id}",),
            )
            for concept in CONCEPTS
        }
        for lab in LABS:
            self._states.setdefault(
                lab.concept_id,
                KnowledgeState(
                    concept_id=lab.concept_id,
                    self_confidence=0.5,
                    diagnostic_status=DiagnosticStatus.UNVERIFIED,
                ),
            )

    def course(self):
        return COURSE

    def knowledge_map(self) -> KnowledgeMap:
        nodes = [
            node.model_copy(update={"mastery": self._states[node.id].mastery or 0.0})
            for node in CONCEPTS
        ]
        return KnowledgeMap(course_id=COURSE.id, version="graph-2026.08", nodes=nodes, edges=EDGES)

    def questions(self):
        return [question for question, _ in QUESTIONS]

    def diagnostic_completed(self) -> bool:
        return self._diagnostic_completed

    def learning_states(self) -> list[LearningStateOut]:
        return [
            LearningStateOut(
                concept_id=state.concept_id,
                self_confidence=state.self_confidence,
                diagnostic_status=state.diagnostic_status.value,
                mastery=state.mastery,
                evidence_confidence=state.evidence_confidence,
                confidence_gap=state.confidence_gap,
                misconception=state.misconception,
                evidence_ids=list(state.evidence_ids),
                version=state.version,
            )
            for state in sorted(self._states.values(), key=lambda item: item.concept_id)
        ]

    def _learning_units(self) -> list[LearningUnit]:
        units: list[LearningUnit] = []
        for concept in CONCEPTS:
            state = self._states[concept.id]
            mastery = state.mastery if state.mastery is not None else state.self_confidence
            duration = 45 if mastery < 0.35 else 30 if mastery < 0.7 else 20
            units.append(
                LearningUnit(
                    concept_id=concept.id,
                    title=concept.name,
                    exam_weight=concept.exam_weight,
                    state=state,
                    estimated_minutes=duration,
                )
            )
        return units

    def plan(self, horizon_days: int = 4, daily_minutes: int = 120) -> StudyPlan:
        priorities = rank_learning_units(
            self._learning_units(),
            exam_date=date.fromisoformat(COURSE.exam_date),
            evaluated_on=date.today(),
        )
        prerequisite_edges = [
            (edge.source, edge.target) for edge in EDGES if edge.relation.value == "prerequisite_of"
        ]
        decision = build_cram_plan(
            priorities,
            self._states,
            prerequisite_edges,
            horizon_days=horizon_days,
            daily_minutes=daily_minutes,
        )
        items = [
            PlanItem(
                id=f"plan-{item.day_offset}-{item.concept_id}",
                concept_id=item.concept_id,
                title=item.title,
                activity=item.activity,
                duration_minutes=item.duration_minutes,
                reason=item.reason,
                expected_gain=item.expected_gain,
                day_offset=item.day_offset,
                priority_rank=item.priority_rank,
                priority_score=item.priority_score,
            )
            for item in decision.scheduled
        ]
        return StudyPlan(
            id=uuid4(),
            title=f"Lộ trình ôn cấp tốc {horizon_days} ngày",
            total_minutes=sum(item.duration_minutes for item in items),
            items=items,
            horizon_days=horizon_days,
            daily_minutes=daily_minutes,
            deferred=[
                DeferredPlanItem(
                    concept_id=item.concept_id,
                    title=item.title,
                    duration_minutes=item.duration_minutes,
                    reason=item.reason,
                )
                for item in decision.deferred
            ],
            component_scores=decision.component_scores,
            planner_version=decision.version,
        )

    def submit_diagnostic(
        self, payload: DiagnosticSubmission, idempotency_key: str
    ) -> DiagnosticResult:
        with self._lock:
            if idempotency_key in self._idempotent_results:
                return self._idempotent_results[idempotency_key]
            answer_key = {question.id: answer for question, answer in QUESTIONS}
            question_map = {question.id: question for question, _ in QUESTIONS}
            correct = 0
            answer_reviews: list[DiagnosticAnswerReview] = []
            evidence: dict[str, list[EvidenceSignal]] = defaultdict(list)
            for concept_id, raw_confidence in payload.self_assessments.items():
                if concept_id in self._states:
                    state = self._states[concept_id]
                    self_confidence = (raw_confidence - 1) / 4
                    self._states[concept_id] = replace(
                        state,
                        self_confidence=self_confidence,
                        confidence_gap=(
                            round(self_confidence - state.mastery, 4)
                            if state.mastery is not None
                            else None
                        ),
                    )
            for answer in payload.answers:
                is_correct = answer_key.get(answer.question_id) == answer.option_id
                correct += int(is_correct)
                question = question_map.get(answer.question_id)
                if question:
                    correct_option_id = answer_key[answer.question_id]
                    answer_reviews.append(
                        DiagnosticAnswerReview(
                            question_id=answer.question_id,
                            concept_id=question.concept_id,
                            selected_option_id=answer.option_id,
                            correct_option_id=correct_option_id,
                            correct=correct_option_id == answer.option_id,
                            explanation=DIAGNOSTIC_EXPLANATIONS.get(
                                answer.question_id,
                                "Đối chiếu lại source và giải thích khái niệm bằng lời của bạn.",
                            ),
                        )
                    )
                    evidence[question.concept_id].append(
                        EvidenceSignal(
                            evidence_id=f"{idempotency_key}:{answer.question_id}",
                            concept_id=question.concept_id,
                            value=1.0 if is_correct else 0.0,
                            confidence=0.84,
                            evidence_type="diagnostic_mcq",
                            misconception=not is_correct,
                        )
                    )
            updates = []
            for concept_id, observations in evidence.items():
                previous_state = self._states[concept_id]
                current_state = update_knowledge_state(previous_state, observations)
                self._states[concept_id] = current_state
                updates.append(
                    MasteryUpdate(
                        concept_id=concept_id,
                        previous=previous_state.mastery,
                        current=current_state.mastery or 0.0,
                        evidence="diagnostic_mcq",
                        diagnostic_status=current_state.diagnostic_status.value,
                        evidence_confidence=current_state.evidence_confidence or 0.0,
                        confidence_gap=current_state.confidence_gap or 0.0,
                    )
                )
            result = DiagnosticResult(
                attempt_id=uuid4(),
                score=correct,
                total=len(payload.answers),
                mastery_updates=updates,
                answer_reviews=answer_reviews,
                plan=self.plan(),
            )
            self._idempotent_results[idempotency_key] = result
            self._diagnostic_completed = True
            return result

    def retrieve(self, query: str) -> RetrievalResponse:
        normalized = query.casefold()
        route = (
            "multi_hop"
            if any(term in normalized for term in ("liên hệ", "chuỗi", "multi-hop"))
            else "prerequisite"
            if "tiên quyết" in normalized
            else "direct"
        )
        tokens = set(normalized.split())
        scored = []
        for concept in CONCEPTS:
            haystack = f"{concept.name} {concept.summary} {concept.objective}".casefold()
            overlap = len(tokens.intersection(haystack.split()))
            score = 0.34 + overlap * 0.12 + concept.exam_weight * 0.1
            scored.append((score, concept))
        hits = [
            RetrievalHit(
                concept_id=concept.id,
                score=round(score, 3),
                text=concept.summary,
                citation=concept.citations[0],
            )
            for score, concept in sorted(scored, reverse=True, key=lambda item: item[0])[:3]
        ]
        return RetrievalResponse(query=query, route=route, hits=hits)

    def tutor(self, question: str) -> TutorAnswer:
        retrieval = self.retrieve(question)
        top = retrieval.hits[0]
        if top.score < 0.42:
            return TutorAnswer(
                answer="Nguồn học hiện tại chưa đủ bằng chứng để trả lời chắc chắn. Hãy thu hẹp câu hỏi vào một khái niệm trong khóa học.",
                confidence=top.score,
                citations=[],
                trace_id=uuid4(),
                refused=True,
            )
        return TutorAnswer(
            answer=f"Theo nguồn khóa học, {top.text} Điểm cần nhớ là luôn giữ source span để kiểm tra lại từng claim.",
            confidence=min(top.score + 0.22, 0.94),
            citations=[top.citation],
            trace_id=uuid4(),
        )

    def score_lab(self, lab_id: str, payload: LabSubmission) -> LabResult:
        lab = next((item for item in LABS if item.id == lab_id), None)
        if lab is None:
            raise LookupError("Lab not found")
        return score_lab_submission(lab, payload)

    def submit_lab(self, lab_id: str, payload: LabSubmission, idempotency_key: str) -> LabResult:
        with self._lock:
            existing = self._idempotent_lab_results.get(idempotency_key)
            if existing is not None:
                return existing
            lab = next((item for item in LABS if item.id == lab_id), None)
            if lab is None:
                raise LookupError("Lab not found")
            result = self.score_lab(lab_id, payload)
            concept_id = canonical_lab_concept_id(lab.concept_id)
            previous = self._states[concept_id]
            current = update_knowledge_state(
                previous,
                [
                    EvidenceSignal(
                        evidence_id=str(result.evidence_event_id),
                        concept_id=concept_id,
                        value=result.score / 100,
                        confidence=0.78,
                        evidence_type="lab",
                    )
                ],
            )
            self._states[concept_id] = current
            result = result.model_copy(
                update={
                    "mastery_update": MasteryUpdate(
                        concept_id=lab.concept_id,
                        previous=previous.mastery,
                        current=current.mastery or 0.0,
                        evidence="lab",
                        diagnostic_status=current.diagnostic_status.value,
                        evidence_confidence=current.evidence_confidence or 0.0,
                        confidence_gap=current.confidence_gap or 0.0,
                    ),
                    "study_plan": self.plan(),
                }
            )
            self._idempotent_lab_results[idempotency_key] = result
            return result


repository = AdaptiveLearningRepository()
