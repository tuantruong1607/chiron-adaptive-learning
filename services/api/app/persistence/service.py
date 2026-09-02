from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import replace
from datetime import UTC, date, datetime
from hashlib import sha256
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import text
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session, sessionmaker

from app.adaptive.contracts import EvidenceSignal, KnowledgeState, LearningUnit
from app.adaptive.mastery import update_knowledge_state
from app.adaptive.planner import build_cram_plan
from app.adaptive.priority import rank_learning_units
from app.auth import Principal
from app.db import get_session_factory, set_tenant_context
from app.labs import canonical_lab_concept_id
from app.persistence.tables import learning_events
from app.schemas import (
    Citation,
    Concept,
    ConceptEdge,
    DeferredPlanItem,
    DiagnosticAnswerReview,
    DiagnosticResult,
    DiagnosticSubmission,
    KnowledgeMap,
    LabResult,
    LabSubmission,
    LearningStateOut,
    MasteryBand,
    MasteryUpdate,
    PlanItem,
    RelationType,
    SourceLocator,
    StudyPlan,
)
from app.seed import DIAGNOSTIC_EXPLANATIONS, QUESTIONS

from .repositories import (
    AttemptRepository,
    CourseRecord,
    CourseRepository,
    EvidenceRepository,
    MasteryStateRepository,
    OutboxRepository,
    PersistedState,
    PrioritySnapshotRepository,
    StudyPlanRepository,
)


class EnrollmentRequiredError(PermissionError):
    pass


class IdempotencyConflictError(RuntimeError):
    pass


def _format_locator(locator: Any) -> str:
    if not isinstance(locator, dict):
        return str(locator or "Source span")
    if locator.get("label"):
        return str(locator["label"])
    if locator.get("kind") == "html_section":
        source_file = locator.get("source_file")
        heading = locator.get("heading")
        return " · ".join(str(value) for value in (source_file, heading) if value) or "HTML section"
    if locator.get("page") is not None:
        return f"Trang {locator['page']}"
    return ", ".join(f"{key}: {value}" for key, value in locator.items()) or "Source span"


class PostgresAdaptiveService:
    def __init__(
        self,
        session_factory: sessionmaker[Session] | None = None,
        fault_hook: Callable[[str], None] | None = None,
    ) -> None:
        self.session_factory = session_factory or get_session_factory()
        self.fault_hook = fault_hook
        self.courses = CourseRepository()
        self.attempts = AttemptRepository()
        self.evidence = EvidenceRepository()
        self.mastery = MasteryStateRepository()
        self.priorities = PrioritySnapshotRepository()
        self.plans = StudyPlanRepository()
        self.outbox = OutboxRepository()

    def diagnostic_completed(self, course_slug: str, principal: Principal) -> bool:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            course = self._course(session, course_slug, principal)
            return bool(
                session.scalar(
                    text(
                        """
                        SELECT EXISTS (
                          SELECT 1 FROM attempts
                          WHERE tenant_id=:tenant_id AND learner_id=:learner_id
                            AND course_id=:course_id AND attempt_type='diagnostic'
                            AND status='completed'
                        )
                        """
                    ),
                    {
                        "tenant_id": principal.tenant_id,
                        "learner_id": principal.user_id,
                        "course_id": course.id,
                    },
                )
            )

    def knowledge_map(self, course_slug: str, principal: Principal) -> KnowledgeMap:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            course = self._course(session, course_slug, principal)
            graph = session.execute(
                text(
                    "SELECT id, version FROM graph_versions WHERE tenant_id=:tenant_id "
                    "AND course_id=:course_id AND status='active' "
                    "ORDER BY updated_at DESC NULLS LAST, created_at DESC LIMIT 1"
                ),
                {"tenant_id": principal.tenant_id, "course_id": course.id},
            ).mappings().first()
            if graph is None:
                raise LookupError("Active knowledge graph not found")
            node_rows = session.execute(
                text(
                    """
                    SELECT n.id, n.normalized_name, n.canonical_name, n.summary, n.exam_weight,
                           n.confidence, n.evidence_source_span_id, m.mastery,
                           m.evidence_confidence, s.locator, s.text, d.title
                    FROM concept_nodes n
                    LEFT JOIN mastery_states m ON m.concept_id=n.id
                      AND m.tenant_id=:tenant_id AND m.learner_id=:learner_id
                    LEFT JOIN source_spans s ON s.id=n.evidence_source_span_id
                      AND s.tenant_id=:tenant_id
                    LEFT JOIN document_versions d ON d.id=s.document_version_id
                      AND d.tenant_id=:tenant_id AND d.course_id=:course_id
                    WHERE n.tenant_id=:tenant_id AND n.course_id=:course_id
                      AND n.graph_version_id=:graph_id AND n.review_status='active'
                    ORDER BY n.normalized_name
                    """
                ),
                {
                    "tenant_id": principal.tenant_id,
                    "learner_id": principal.user_id,
                    "course_id": course.id,
                    "graph_id": graph["id"],
                },
            ).mappings().all()
            edge_rows = session.execute(
                text(
                    """
                    SELECT e.id, source.normalized_name AS source_name,
                           target.normalized_name AS target_name, e.relation_type, e.weight
                    FROM concept_edges e
                    JOIN concept_nodes source ON source.id=e.source_concept_id
                    JOIN concept_nodes target ON target.id=e.target_concept_id
                    WHERE e.tenant_id=:tenant_id AND e.graph_version_id=:graph_id
                      AND source.tenant_id=:tenant_id AND target.tenant_id=:tenant_id
                      AND source.graph_version_id=:graph_id AND target.graph_version_id=:graph_id
                      AND e.review_status='active'
                    ORDER BY e.id
                    """
                ),
                {"tenant_id": principal.tenant_id, "graph_id": graph["id"]},
            ).mappings().all()

        nodes: list[Concept] = []
        for index, row in enumerate(node_rows):
            mastery = float(row["mastery"] if row["mastery"] is not None else 0.0)
            band = (
                MasteryBand.MASTERED
                if mastery >= 0.85
                else MasteryBand.SECURE
                if mastery >= 0.65
                else MasteryBand.DEVELOPING
                if mastery >= 0.35
                else MasteryBand.NEW
            )
            locator = _format_locator(row["locator"])
            nodes.append(
                Concept(
                    id=str(row["normalized_name"]),
                    name=str(row["canonical_name"]),
                    summary=str(row["summary"] or ""),
                    objective=(
                        "Đọc nguồn có dẫn chứng, giải thích lại khái niệm và áp dụng vào bài tập."
                    ),
                    mastery=mastery,
                    confidence=float(row["evidence_confidence"] or row["confidence"] or 0.0),
                    exam_weight=float(row["exam_weight"] or 0.0),
                    band=band,
                    x=float(10 + (index % 5) * 20),
                    y=float(10 + (index // 5) * 11),
                    citations=(
                        [
                            Citation(
                                source_span_id=str(row["evidence_source_span_id"]),
                                title=str(row["title"] or "Course source"),
                                locator=str(locator or "source span"),
                                excerpt=str(row["text"] or ""),
                            )
                        ]
                        if row["evidence_source_span_id"]
                        else []
                    ),
                )
            )
        edges = [
            ConceptEdge(
                id=str(row["id"]),
                source=str(row["source_name"]),
                target=str(row["target_name"]),
                relation=RelationType(str(row["relation_type"])),
                weight=float(row["weight"] or 0.0),
            )
            for row in edge_rows
        ]
        return KnowledgeMap(course_id=course_slug, version=str(graph["version"]), nodes=nodes, edges=edges)

    def source_locator(
        self, course_slug: str, source_span_id: str, principal: Principal
    ) -> SourceLocator:
        try:
            span_id = UUID(source_span_id)
        except ValueError as exc:
            raise LookupError("Source span not found in active knowledge graph") from exc

        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            course = self._course(session, course_slug, principal)
            row = session.execute(
                text(
                    """
                    SELECT s.id, s.locator, s.text, d.title, d.source_type
                    FROM source_spans s
                    JOIN document_versions d ON d.id=s.document_version_id
                      AND d.tenant_id=:tenant_id AND d.course_id=:course_id
                    JOIN concept_nodes n ON n.evidence_source_span_id=s.id
                      AND n.tenant_id=:tenant_id AND n.course_id=:course_id
                      AND n.review_status='active'
                    JOIN graph_versions g ON g.id=n.graph_version_id
                      AND g.tenant_id=:tenant_id AND g.course_id=:course_id
                      AND g.status='active'
                    WHERE s.id=:source_span_id AND s.tenant_id=:tenant_id
                    LIMIT 1
                    """
                ),
                {
                    "tenant_id": principal.tenant_id,
                    "course_id": course.id,
                    "source_span_id": span_id,
                },
            ).mappings().first()

        if row is None:
            raise LookupError("Source span not found in active knowledge graph")
        details = row["locator"] if isinstance(row["locator"], dict) else {}
        label = details.get("label")
        page = details.get("page")
        locator = _format_locator(details)
        return SourceLocator(
            source_span_id=str(row["id"]),
            title=str(row["title"] or "Course source"),
            locator=locator,
            excerpt=str(row["text"] or ""),
            source_type=str(row["source_type"] or "course_source"),
            locator_kind=str(details.get("kind") or "source_span"),
            label=str(label) if label is not None else None,
            page=int(page) if page is not None else None,
            section_title=(
                str(details["section_title"]) if details.get("section_title") is not None else None
            ),
            heading=str(details["heading"]) if details.get("heading") is not None else None,
            section_id=(
                str(details["section_id"]) if details.get("section_id") is not None else None
            ),
            source_file=(
                str(details["source_file"]) if details.get("source_file") is not None else None
            ),
            order=int(details["order"]) if details.get("order") is not None else None,
            extraction_method=(
                str(details["extraction_method"])
                if details.get("extraction_method") is not None
                else None
            ),
        )

    def submit_diagnostic(
        self,
        course_slug: str,
        payload: DiagnosticSubmission,
        idempotency_key: str,
        principal: Principal,
    ) -> DiagnosticResult:
        request_payload = payload.model_dump(mode="json")
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            course = self._course(session, course_slug, principal)
            attempt = self.attempts.acquire(
                session,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                course_id=course.id,
                idempotency_key=idempotency_key,
                request_payload=request_payload,
            )
            if attempt.status == "completed" and attempt.payload.get("result"):
                return DiagnosticResult.model_validate(attempt.payload["result"])
            if attempt.payload.get("request") != request_payload:
                raise IdempotencyConflictError(
                    "Idempotency-Key was already used with a different diagnostic payload"
                )

            answer_key = {question.id: answer for question, answer in QUESTIONS}
            question_map = {question.id: question for question, _ in QUESTIONS}
            answer_ids = [answer.question_id for answer in payload.answers]
            if len(answer_ids) != len(set(answer_ids)) or any(
                question_id not in question_map for question_id in answer_ids
            ):
                raise ValueError("Diagnostic contains duplicate or unknown question IDs")

            concepts = self.courses.concepts(session, principal.tenant_id, course.id)
            concepts_by_slug = {}
            for concept in concepts:
                concepts_by_slug.setdefault(concept.slug, concept)
            persisted_states = self.mastery.list_for_course(
                session,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                course_id=course.id,
                for_update=True,
            )
            # Graph versions may contain the same normalized concept. Keep an
            # enrolled learner on the node that already owns their mastery
            # state instead of creating a second state for the active graph.
            for item in persisted_states:
                concepts_by_slug[item.concept.slug] = item.concept
            states = {item.concept.slug: item.state for item in persisted_states}

            for concept_slug, raw_confidence in payload.self_assessments.items():
                concept = concepts_by_slug.get(concept_slug)
                if concept is None:
                    raise ValueError(f"Unknown concept in self_assessments: {concept_slug}")
                current = states.get(concept_slug) or self.mastery.get_for_update(
                    session, principal.tenant_id, principal.user_id, concept
                )
                self_confidence = (raw_confidence - 1) / 4
                current = replace(
                    current,
                    self_confidence=self_confidence,
                    confidence_gap=(
                        round(self_confidence - current.mastery, 4)
                        if current.mastery is not None
                        else None
                    ),
                )
                self.mastery.save(
                    session,
                    tenant_id=principal.tenant_id,
                    learner_id=principal.user_id,
                    concept_id=concept.id,
                    state=current,
                )
                states[concept_slug] = current

            updates: list[MasteryUpdate] = []
            answer_reviews: list[DiagnosticAnswerReview] = []
            correct = 0
            for answer in payload.answers:
                question = question_map[answer.question_id]
                concept = concepts_by_slug.get(question.concept_id)
                if concept is None:
                    raise ValueError(f"Question concept is not published: {question.concept_id}")
                is_correct = answer_key[answer.question_id] == answer.option_id
                correct += int(is_correct)
                answer_reviews.append(
                    DiagnosticAnswerReview(
                        question_id=answer.question_id,
                        concept_id=question.concept_id,
                        selected_option_id=answer.option_id,
                        correct_option_id=answer_key[answer.question_id],
                        correct=is_correct,
                        explanation=DIAGNOSTIC_EXPLANATIONS.get(
                            answer.question_id,
                            "Đối chiếu lại source và giải thích khái niệm bằng lời của bạn.",
                        ),
                    )
                )
                previous = states.get(concept.slug) or self.mastery.get_for_update(
                    session, principal.tenant_id, principal.user_id, concept
                )
                evidence_id = uuid4()
                evidence_key = f"{attempt.id}:{answer.question_id}"
                inserted = self.evidence.add(
                    session,
                    evidence_id=evidence_id,
                    tenant_id=principal.tenant_id,
                    learner_id=principal.user_id,
                    concept_id=concept.id,
                    attempt_id=attempt.id,
                    evidence_type="diagnostic_mcq",
                    value=1.0 if is_correct else 0.0,
                    confidence=0.84,
                    idempotency_key=evidence_key,
                )
                if not inserted:
                    continue
                current = update_knowledge_state(
                    previous,
                    [
                        EvidenceSignal(
                            evidence_id=str(evidence_id),
                            concept_id=concept.slug,
                            value=1.0 if is_correct else 0.0,
                            confidence=0.84,
                            evidence_type="diagnostic_mcq",
                            misconception=not is_correct,
                        )
                    ],
                )
                self.mastery.save(
                    session,
                    tenant_id=principal.tenant_id,
                    learner_id=principal.user_id,
                    concept_id=concept.id,
                    state=current,
                )
                states[concept.slug] = current
                updates.append(
                    MasteryUpdate(
                        concept_id=concept.slug,
                        previous=previous.mastery,
                        current=current.mastery or 0.0,
                        evidence="diagnostic_mcq",
                        diagnostic_status=current.diagnostic_status.value,
                        evidence_confidence=current.evidence_confidence or 0.0,
                        confidence_gap=current.confidence_gap or 0.0,
                    )
                )

            if self.fault_hook:
                self.fault_hook("after_evidence")

            plan = self._build_and_persist_plan(
                session,
                principal,
                course,
                horizon_days=4,
                daily_minutes=120,
            )
            result = DiagnosticResult(
                attempt_id=attempt.id,
                score=correct,
                total=len(payload.answers),
                mastery_updates=updates,
                answer_reviews=answer_reviews,
                plan=plan,
            )
            self.attempts.complete(
                session,
                attempt.id,
                {"request": request_payload, "result": result.model_dump(mode="json")},
            )
            self.outbox.add(
                session,
                tenant_id=principal.tenant_id,
                event_type="diagnostic.completed",
                aggregate_id=attempt.id,
                payload={
                    "attempt_id": str(attempt.id),
                    "learner_id": str(principal.user_id),
                    "course_id": str(course.id),
                },
                dedupe_key=f"diagnostic.completed:{attempt.id}",
            )
            return result

    def submit_lab(
        self,
        course_slug: str,
        lab_id: str,
        concept_id: str,
        payload: LabSubmission,
        score: LabResult,
        idempotency_key: str,
        principal: Principal,
    ) -> LabResult:
        request_payload = payload.model_dump(mode="json")
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            course = self._course(session, course_slug, principal)
            attempt = self.attempts.acquire(
                session,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                course_id=course.id,
                idempotency_key=idempotency_key,
                request_payload={"lab_id": lab_id, **request_payload},
                attempt_type="lab",
            )
            if attempt.status == "completed" and attempt.payload.get("result"):
                return LabResult.model_validate(attempt.payload["result"])
            if attempt.payload.get("request") != {"lab_id": lab_id, **request_payload}:
                raise IdempotencyConflictError(
                    "Idempotency-Key was already used with a different lab payload"
                )
            concepts = self.courses.concepts(session, principal.tenant_id, course.id)
            persisted_states = self.mastery.list_for_course(
                session,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                course_id=course.id,
                for_update=True,
            )
            stable_concept_id = canonical_lab_concept_id(concept_id)
            existing_concepts = {item.concept.slug: item.concept for item in persisted_states}
            concept = existing_concepts.get(stable_concept_id) or next(
                (item for item in concepts if item.slug == stable_concept_id), None
            )
            if concept is None:
                raise ValueError(f"Lab concept is not published: {stable_concept_id}")
            states = {item.concept.slug: item.state for item in persisted_states}
            previous = states.get(concept.slug) or self.mastery.get_for_update(
                session, principal.tenant_id, principal.user_id, concept
            )
            evidence_key = f"{attempt.id}:{lab_id}"
            inserted = self.evidence.add(
                session,
                evidence_id=score.evidence_event_id,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                concept_id=concept.id,
                attempt_id=attempt.id,
                evidence_type="lab",
                value=score.score / 100,
                confidence=0.78,
                idempotency_key=evidence_key,
            )
            current = update_knowledge_state(
                previous,
                [
                    EvidenceSignal(
                        evidence_id=str(score.evidence_event_id),
                        concept_id=concept.slug,
                        value=score.score / 100,
                        confidence=0.78,
                        evidence_type="lab",
                    )
                ],
            ) if inserted else previous
            if inserted:
                self.mastery.save(
                    session,
                    tenant_id=principal.tenant_id,
                    learner_id=principal.user_id,
                    concept_id=concept.id,
                    state=current,
                )
                session.execute(
                    pg_insert(learning_events)
                    .values(
                        id=score.evidence_event_id,
                        tenant_id=principal.tenant_id,
                        learner_id=principal.user_id,
                        course_id=course.id,
                        attempt_id=attempt.id,
                        event_type="lab.completed",
                        payload={
                            "lab_id": lab_id,
                            "score": score.score,
                            "passed": score.passed,
                            "concept_id": concept_id,
                        },
                        idempotency_key=evidence_key,
                        occurred_at=datetime.now(UTC),
                    )
                    .on_conflict_do_nothing(constraint="uq_learning_event_idempotency")
                )
            plan = self._build_and_persist_plan(
                session, principal, course, horizon_days=4, daily_minutes=120
            )
            result = score.model_copy(
                update={
                    "mastery_update": MasteryUpdate(
                        concept_id=concept.slug,
                        previous=previous.mastery,
                        current=current.mastery or 0.0,
                        evidence="lab",
                        diagnostic_status=current.diagnostic_status.value,
                        evidence_confidence=current.evidence_confidence or 0.0,
                        confidence_gap=current.confidence_gap or 0.0,
                    ),
                    "study_plan": plan,
                }
            )
            self.attempts.complete(
                session,
                attempt.id,
                {"request": {"lab_id": lab_id, **request_payload}, "result": result.model_dump(mode="json")},
            )
            return result

    def learning_states(self, course_slug: str, principal: Principal) -> list[LearningStateOut]:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            course = self._course(session, course_slug, principal)
            states = self._active_learning_states(session, principal, course)
            return [self._state_out(item) for item in states]

    def plan(
        self,
        course_slug: str,
        principal: Principal,
        *,
        horizon_days: int,
        daily_minutes: int,
    ) -> StudyPlan:
        with self.session_factory() as session, session.begin():
            set_tenant_context(session, principal.tenant_id)
            course = self._course(session, course_slug, principal)
            latest = self.plans.latest(
                session,
                tenant_id=principal.tenant_id,
                learner_id=principal.user_id,
                course_id=course.id,
                horizon_days=horizon_days,
                daily_minutes=daily_minutes,
            )
            if latest is not None:
                return self._stored_plan(latest)
            return self._build_and_persist_plan(
                session,
                principal,
                course,
                horizon_days=horizon_days,
                daily_minutes=daily_minutes,
            )

    def _course(self, session: Session, course_slug: str, principal: Principal) -> CourseRecord:
        course = self.courses.require_enrollment(
            session,
            tenant_id=principal.tenant_id,
            learner_id=principal.user_id,
            course_slug=course_slug,
        )
        if course is None:
            raise EnrollmentRequiredError("Active course enrollment required")
        return course

    def _build_and_persist_plan(
        self,
        session: Session,
        principal: Principal,
        course: CourseRecord,
        *,
        horizon_days: int,
        daily_minutes: int,
    ) -> StudyPlan:
        persisted = self._active_learning_states(session, principal, course)
        units = [
            LearningUnit(
                concept_id=item.concept.slug,
                title=item.concept.title,
                exam_weight=item.concept.exam_weight,
                state=item.state,
                estimated_minutes=self._duration(item.state),
            )
            for item in persisted
        ]
        evaluated_on = date.today()
        priorities = rank_learning_units(
            units, exam_date=course.exam_date, evaluated_on=evaluated_on
        )
        edges = self.courses.prerequisite_edges(session, principal.tenant_id, course.id)
        states = {item.concept.slug: item.state for item in persisted}
        decision = build_cram_plan(
            priorities,
            states,
            edges,
            horizon_days=horizon_days,
            daily_minutes=daily_minutes,
        )
        checksum = self._checksum(
            {
                "states": [
                    {
                        "concept": item.concept.slug,
                        "mastery": item.state.mastery,
                        "confidence": item.state.evidence_confidence,
                        "evidence": item.state.evidence_ids,
                    }
                    for item in persisted
                ],
                "horizon_days": horizon_days,
                "daily_minutes": daily_minutes,
                "evaluated_on": evaluated_on.isoformat(),
            }
        )
        concept_ids = {item.concept.slug: item.concept.id for item in persisted}
        snapshot_id = self.priorities.create(
            session,
            snapshot_id=uuid4(),
            tenant_id=principal.tenant_id,
            learner_id=principal.user_id,
            course_id=course.id,
            evaluated_at=datetime.now(UTC),
            exam_date=course.exam_date,
            input_checksum=checksum,
            priorities=priorities,
            concept_ids=concept_ids,
        )
        candidate_plan_id = uuid4()
        items: list[dict[str, Any]] = []
        for sequence, item in enumerate(decision.scheduled, start=1):
            items.append(
                {
                    "id": uuid4(),
                    "tenant_id": principal.tenant_id,
                    "plan_id": candidate_plan_id,
                    "concept_id": concept_ids[item.concept_id],
                    "day_offset": item.day_offset,
                    "sequence": sequence,
                    "activity": item.activity,
                    "duration_minutes": item.duration_minutes,
                    "expected_gain": item.expected_gain,
                    "decision_status": "scheduled",
                    "reason": item.reason,
                }
            )
        for sequence, item in enumerate(decision.deferred, start=len(items) + 1):
            items.append(
                {
                    "id": uuid4(),
                    "tenant_id": principal.tenant_id,
                    "plan_id": candidate_plan_id,
                    "concept_id": concept_ids[item.concept_id],
                    "day_offset": None,
                    "sequence": sequence,
                    "activity": "lesson",
                    "duration_minutes": item.duration_minutes,
                    "expected_gain": 0,
                    "decision_status": "deferred",
                    "reason": item.reason,
                }
            )
        plan_id = self.plans.create(
            session,
            plan_id=candidate_plan_id,
            tenant_id=principal.tenant_id,
            learner_id=principal.user_id,
            course_id=course.id,
            snapshot_id=snapshot_id,
            horizon_days=horizon_days,
            daily_minutes=daily_minutes,
            planner_version=decision.version,
            input_checksum=checksum,
            items=items,
        )
        return StudyPlan(
            id=plan_id,
            title=f"Lộ trình ôn cấp tốc {horizon_days} ngày",
            total_minutes=sum(item.duration_minutes for item in decision.scheduled),
            items=[
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
            ],
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

    def _active_learning_states(
        self,
        session: Session,
        principal: Principal,
        course: CourseRecord,
    ) -> list[PersistedState]:
        """Return one state for every concept in the active graph.

        A newly activated taxonomy contains concepts the learner has not seen yet.
        Those concepts stay unassessed in the read model until evidence is saved,
        but must still appear in the knowledge map and study-plan ranking.
        """
        concepts = self.courses.concepts(session, principal.tenant_id, course.id)
        persisted = self.mastery.list_for_course(
            session,
            tenant_id=principal.tenant_id,
            learner_id=principal.user_id,
            course_id=course.id,
        )
        states_by_id = {item.concept.id: item.state for item in persisted}
        return [
            PersistedState(
                concept=concept,
                state=states_by_id.get(concept.id)
                or KnowledgeState(concept_id=concept.slug, self_confidence=0.5),
            )
            for concept in concepts
        ]

    @staticmethod
    def _stored_plan(payload: dict[str, Any]) -> StudyPlan:
        plan = payload["plan"]
        scores = {row["normalized_name"]: row for row in payload["scores"]}
        scheduled: list[PlanItem] = []
        deferred: list[DeferredPlanItem] = []
        for row in payload["items"]:
            if row["decision_status"] == "deferred":
                deferred.append(
                    DeferredPlanItem(
                        concept_id=row["normalized_name"],
                        title=row["canonical_name"],
                        duration_minutes=row["duration_minutes"],
                        reason=row["reason"],
                    )
                )
                continue
            score = scores[row["normalized_name"]]
            scheduled.append(
                PlanItem(
                    id=str(row["id"]),
                    concept_id=row["normalized_name"],
                    title=row["canonical_name"],
                    activity=row["activity"],
                    duration_minutes=row["duration_minutes"],
                    reason=row["reason"],
                    expected_gain=row["expected_gain"],
                    day_offset=row["day_offset"],
                    priority_rank=score["priority_rank"],
                    priority_score=score["priority_score"],
                )
            )
        component_scores = {
            slug: {
                "need": row["need"],
                "importance": row["importance"],
                "urgency": row["urgency"],
                "reliability": row["reliability"],
                "priority": row["priority_score"],
            }
            for slug, row in scores.items()
        }
        return StudyPlan(
            id=plan["id"],
            title=f"Lộ trình ôn cấp tốc {plan['horizon_days']} ngày",
            total_minutes=sum(item.duration_minutes for item in scheduled),
            generated_at=plan["created_at"],
            items=scheduled,
            horizon_days=plan["horizon_days"],
            daily_minutes=plan["daily_minutes"],
            deferred=deferred,
            component_scores=component_scores,
            planner_version=plan["planner_version"],
        )

    @staticmethod
    def _state_out(item: PersistedState) -> LearningStateOut:
        state = item.state
        return LearningStateOut(
            concept_id=item.concept.slug,
            self_confidence=state.self_confidence,
            diagnostic_status=state.diagnostic_status.value,
            mastery=state.mastery,
            evidence_confidence=state.evidence_confidence,
            confidence_gap=state.confidence_gap,
            misconception=state.misconception,
            evidence_ids=list(state.evidence_ids),
            version=state.version,
        )

    @staticmethod
    def _duration(state: KnowledgeState) -> int:
        mastery = state.mastery if state.mastery is not None else state.self_confidence
        return 45 if mastery < 0.35 else 30 if mastery < 0.7 else 20

    @staticmethod
    def _checksum(payload: dict[str, Any]) -> str:
        encoded = json.dumps(payload, sort_keys=True, ensure_ascii=False, default=str).encode()
        return sha256(encoded).hexdigest()
