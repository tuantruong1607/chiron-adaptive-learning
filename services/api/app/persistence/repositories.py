from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, date, datetime
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import Select, and_, insert, select, update
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.orm import Session

from app.adaptive.contracts import DiagnosticStatus, KnowledgeState, PriorityDecision

from .tables import (
    attempts,
    auth_refresh_sessions,
    concept_edges,
    concept_nodes,
    course_enrollments,
    courses,
    evidence_ledger,
    graph_versions,
    mastery_states,
    memberships,
    outbox_events,
    priority_items,
    priority_snapshots,
    study_plan_items,
    study_plans,
    tenants,
    users,
)


@dataclass(frozen=True, slots=True)
class IdentityRecord:
    user_id: UUID
    tenant_id: UUID
    password_hash: str
    role: str


@dataclass(frozen=True, slots=True)
class CourseRecord:
    id: UUID
    slug: str
    exam_date: date


@dataclass(frozen=True, slots=True)
class ConceptRecord:
    id: UUID
    slug: str
    title: str
    exam_weight: float


@dataclass(frozen=True, slots=True)
class AttemptRecord:
    id: UUID
    status: str
    payload: dict[str, Any]
    created: bool


@dataclass(frozen=True, slots=True)
class PersistedState:
    concept: ConceptRecord
    state: KnowledgeState


class IdentityRepository:
    def find_tenant(self, session: Session, tenant_slug: str) -> UUID | None:
        return session.scalar(
            select(tenants.c.id).where(
                tenants.c.slug == tenant_slug.casefold(), tenants.c.status == "active"
            )
        )

    def find_login(self, session: Session, tenant_id: UUID, email: str) -> IdentityRecord | None:
        row = (
            session.execute(
                select(
                    users.c.id.label("user_id"),
                    users.c.password_hash,
                    memberships.c.role,
                )
                .join(memberships, memberships.c.user_id == users.c.id)
                .where(
                    users.c.email == email.casefold(),
                    users.c.status == "active",
                    memberships.c.tenant_id == tenant_id,
                    memberships.c.status == "active",
                )
            )
            .mappings()
            .first()
        )
        if row is None:
            return None
        return IdentityRecord(
            user_id=row["user_id"],
            tenant_id=tenant_id,
            password_hash=row["password_hash"],
            role=row["role"],
        )

    def active_membership(
        self, session: Session, tenant_id: UUID, user_id: UUID
    ) -> IdentityRecord | None:
        row = (
            session.execute(
                select(users.c.password_hash, memberships.c.role)
                .select_from(memberships)
                .join(users, users.c.id == memberships.c.user_id)
                .where(
                    memberships.c.tenant_id == tenant_id,
                    memberships.c.user_id == user_id,
                    memberships.c.status == "active",
                    users.c.status == "active",
                )
            )
            .mappings()
            .first()
        )
        if row is None:
            return None
        return IdentityRecord(
            user_id=user_id,
            tenant_id=tenant_id,
            password_hash=row["password_hash"],
            role=row["role"],
        )


class RefreshSessionRepository:
    def create(
        self,
        session: Session,
        *,
        session_id: UUID,
        tenant_id: UUID,
        user_id: UUID,
        token_hash: str,
        expires_at: datetime,
        user_agent: str | None,
    ) -> None:
        session.execute(
            insert(auth_refresh_sessions).values(
                id=session_id,
                tenant_id=tenant_id,
                user_id=user_id,
                token_hash=token_hash,
                expires_at=expires_at,
                user_agent=(user_agent or "")[:512] or None,
            )
        )

    def acquire_active(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        session_id: UUID,
        token_hash: str,
    ) -> dict[str, Any] | None:
        row = (
            session.execute(
                select(auth_refresh_sessions)
                .where(
                    auth_refresh_sessions.c.id == session_id,
                    auth_refresh_sessions.c.tenant_id == tenant_id,
                    auth_refresh_sessions.c.token_hash == token_hash,
                    auth_refresh_sessions.c.revoked_at.is_(None),
                    auth_refresh_sessions.c.expires_at > datetime.now(UTC),
                )
                .with_for_update()
            )
            .mappings()
            .first()
        )
        return dict(row) if row else None

    def revoke(
        self,
        session: Session,
        *,
        session_id: UUID,
        replacement_id: UUID | None = None,
    ) -> None:
        session.execute(
            update(auth_refresh_sessions)
            .where(
                auth_refresh_sessions.c.id == session_id,
                auth_refresh_sessions.c.revoked_at.is_(None),
            )
            .values(
                revoked_at=datetime.now(UTC),
                replaced_by_id=replacement_id,
                updated_at=datetime.now(UTC),
            )
        )


class CourseRepository:
    def require_enrollment(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        learner_id: UUID,
        course_slug: str,
    ) -> CourseRecord | None:
        row = (
            session.execute(
                select(courses.c.id, courses.c.slug, courses.c.exam_date)
                .join(
                    course_enrollments,
                    and_(
                        course_enrollments.c.course_id == courses.c.id,
                        course_enrollments.c.tenant_id == tenant_id,
                    ),
                )
                .where(
                    courses.c.tenant_id == tenant_id,
                    courses.c.slug == course_slug,
                    courses.c.status == "published",
                    course_enrollments.c.learner_id == learner_id,
                    course_enrollments.c.status == "active",
                )
            )
            .mappings()
            .first()
        )
        if row is None:
            return None
        return CourseRecord(id=row["id"], slug=row["slug"], exam_date=row["exam_date"])

    def concepts(self, session: Session, tenant_id: UUID, course_id: UUID) -> list[ConceptRecord]:
        rows = session.execute(
            select(
                concept_nodes.c.id,
                concept_nodes.c.normalized_name,
                concept_nodes.c.canonical_name,
                concept_nodes.c.exam_weight,
            )
            .join(graph_versions, graph_versions.c.id == concept_nodes.c.graph_version_id)
            .where(
                concept_nodes.c.tenant_id == tenant_id,
                concept_nodes.c.course_id == course_id,
                graph_versions.c.tenant_id == tenant_id,
                graph_versions.c.course_id == course_id,
                graph_versions.c.status == "active",
            )
            .order_by(concept_nodes.c.normalized_name)
        ).mappings()
        return [
            ConceptRecord(
                id=row["id"],
                slug=row["normalized_name"],
                title=row["canonical_name"],
                exam_weight=float(row["exam_weight"]),
            )
            for row in rows
        ]

    def prerequisite_edges(
        self, session: Session, tenant_id: UUID, course_id: UUID
    ) -> list[tuple[str, str]]:
        source_node = concept_nodes.alias("source_node")
        target_node = concept_nodes.alias("target_node")
        rows = session.execute(
            select(
                source_node.c.normalized_name.label("source_slug"),
                target_node.c.normalized_name.label("target_slug"),
            )
            .select_from(concept_edges)
            .join(graph_versions, graph_versions.c.id == concept_edges.c.graph_version_id)
            .join(source_node, source_node.c.id == concept_edges.c.source_concept_id)
            .join(target_node, target_node.c.id == concept_edges.c.target_concept_id)
            .where(
                concept_edges.c.tenant_id == tenant_id,
                graph_versions.c.tenant_id == tenant_id,
                graph_versions.c.course_id == course_id,
                graph_versions.c.status == "active",
                concept_edges.c.relation_type == "prerequisite_of",
                concept_edges.c.review_status == "active",
                source_node.c.course_id == course_id,
                target_node.c.course_id == course_id,
            )
        ).mappings()
        return [(row["source_slug"], row["target_slug"]) for row in rows]


class AttemptRepository:
    def acquire(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        learner_id: UUID,
        course_id: UUID,
        idempotency_key: str,
        request_payload: dict[str, Any],
        attempt_type: str = "diagnostic",
    ) -> AttemptRecord:
        attempt_id = uuid4()
        inserted_id = session.scalar(
            pg_insert(attempts)
            .values(
                id=attempt_id,
                tenant_id=tenant_id,
                course_id=course_id,
                learner_id=learner_id,
                attempt_type=attempt_type,
                status="in_progress",
                idempotency_key=idempotency_key,
                payload={"request": request_payload},
            )
            .on_conflict_do_nothing(constraint="uq_attempt_idempotency")
            .returning(attempts.c.id)
        )
        query: Select = select(attempts.c.id, attempts.c.status, attempts.c.payload).where(
            attempts.c.tenant_id == tenant_id,
            attempts.c.idempotency_key == idempotency_key,
        )
        if inserted_id is None:
            query = query.with_for_update()
        row = session.execute(query).mappings().one()
        return AttemptRecord(
            id=row["id"],
            status=row["status"],
            payload=dict(row["payload"] or {}),
            created=inserted_id is not None,
        )

    def complete(self, session: Session, attempt_id: UUID, payload: dict[str, Any]) -> None:
        session.execute(
            update(attempts)
            .where(attempts.c.id == attempt_id)
            .values(status="completed", payload=payload)
        )

    def get_owned(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        learner_id: UUID,
        attempt_id: UUID,
        attempt_type: str,
    ) -> AttemptRecord | None:
        row = (
            session.execute(
                select(attempts.c.id, attempts.c.status, attempts.c.payload).where(
                    attempts.c.id == attempt_id,
                    attempts.c.tenant_id == tenant_id,
                    attempts.c.learner_id == learner_id,
                    attempts.c.attempt_type == attempt_type,
                )
            )
            .mappings()
            .first()
        )
        if row is None:
            return None
        return AttemptRecord(
            id=row["id"],
            status=row["status"],
            payload=dict(row["payload"] or {}),
            created=False,
        )


class EvidenceRepository:
    def add(
        self,
        session: Session,
        *,
        evidence_id: UUID,
        tenant_id: UUID,
        learner_id: UUID,
        concept_id: UUID,
        attempt_id: UUID,
        evidence_type: str,
        value: float,
        confidence: float,
        idempotency_key: str,
    ) -> bool:
        inserted = session.scalar(
            pg_insert(evidence_ledger)
            .values(
                id=evidence_id,
                tenant_id=tenant_id,
                learner_id=learner_id,
                concept_id=concept_id,
                attempt_id=attempt_id,
                evidence_type=evidence_type,
                value=value,
                confidence=confidence,
                idempotency_key=idempotency_key,
            )
            .on_conflict_do_nothing(constraint="uq_evidence_idempotency")
            .returning(evidence_ledger.c.id)
        )
        return inserted is not None


class MasteryStateRepository:
    def get_for_update(
        self, session: Session, tenant_id: UUID, learner_id: UUID, concept: ConceptRecord
    ) -> KnowledgeState:
        row = (
            session.execute(
                select(mastery_states)
                .where(
                    mastery_states.c.tenant_id == tenant_id,
                    mastery_states.c.learner_id == learner_id,
                    mastery_states.c.concept_id == concept.id,
                )
                .with_for_update()
            )
            .mappings()
            .first()
        )
        if row is None:
            return KnowledgeState(concept_id=concept.slug, self_confidence=0.5)
        return self._to_state(row, concept.slug)

    def save(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        learner_id: UUID,
        concept_id: UUID,
        state: KnowledgeState,
    ) -> None:
        values = {
            "id": uuid4(),
            "tenant_id": tenant_id,
            "learner_id": learner_id,
            "concept_id": concept_id,
            "self_confidence": state.self_confidence,
            "diagnostic_status": state.diagnostic_status.value,
            "mastery": state.mastery,
            "evidence_confidence": state.evidence_confidence,
            "confidence_gap": state.confidence_gap,
            "misconception": state.misconception,
            "evidence_ids": list(state.evidence_ids),
            "engine_version": state.version,
        }
        session.execute(
            pg_insert(mastery_states)
            .values(**values)
            .on_conflict_do_update(
                constraint="uq_mastery_learner_concept",
                set_={key: value for key, value in values.items() if key != "id"},
            )
        )

    def list_for_course(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        learner_id: UUID,
        course_id: UUID,
        for_update: bool = False,
    ) -> list[PersistedState]:
        statement = (
            select(
                mastery_states,
                concept_nodes.c.normalized_name,
                concept_nodes.c.canonical_name,
                concept_nodes.c.exam_weight,
            )
            .join(concept_nodes, concept_nodes.c.id == mastery_states.c.concept_id)
            .join(graph_versions, graph_versions.c.id == concept_nodes.c.graph_version_id)
            .where(
                mastery_states.c.tenant_id == tenant_id,
                mastery_states.c.learner_id == learner_id,
                concept_nodes.c.course_id == course_id,
                graph_versions.c.tenant_id == tenant_id,
                graph_versions.c.course_id == course_id,
                graph_versions.c.status == "active",
            )
            .order_by(concept_nodes.c.normalized_name)
        )
        if for_update:
            statement = statement.with_for_update(of=mastery_states)
        rows = session.execute(statement).mappings()
        return [
            PersistedState(
                concept=ConceptRecord(
                    id=row["concept_id"],
                    slug=row["normalized_name"],
                    title=row["canonical_name"],
                    exam_weight=float(row["exam_weight"]),
                ),
                state=self._to_state(row, row["normalized_name"]),
            )
            for row in rows
        ]

    @staticmethod
    def _to_state(row: Any, concept_slug: str) -> KnowledgeState:
        return KnowledgeState(
            concept_id=concept_slug,
            self_confidence=float(row["self_confidence"]),
            diagnostic_status=DiagnosticStatus(row["diagnostic_status"]),
            mastery=float(row["mastery"]) if row["mastery"] is not None else None,
            evidence_confidence=(
                float(row["evidence_confidence"])
                if row["evidence_confidence"] is not None
                else None
            ),
            confidence_gap=(
                float(row["confidence_gap"]) if row["confidence_gap"] is not None else None
            ),
            misconception=bool(row["misconception"]),
            evidence_ids=tuple(row["evidence_ids"] or ()),
            version=row["engine_version"],
        )


class PrioritySnapshotRepository:
    def create(
        self,
        session: Session,
        *,
        snapshot_id: UUID,
        tenant_id: UUID,
        learner_id: UUID,
        course_id: UUID,
        evaluated_at: datetime,
        exam_date: date,
        input_checksum: str,
        priorities: list[PriorityDecision],
        concept_ids: dict[str, UUID],
    ) -> UUID:
        inserted_id = session.scalar(
            pg_insert(priority_snapshots)
            .values(
                id=snapshot_id,
                tenant_id=tenant_id,
                learner_id=learner_id,
                course_id=course_id,
                evaluated_at=evaluated_at,
                exam_date=exam_date,
                engine_version="niu-v1",
                input_checksum=input_checksum,
            )
            .on_conflict_do_nothing(constraint="uq_priority_snapshot_input")
            .returning(priority_snapshots.c.id)
        )
        if inserted_id is None:
            existing_id = session.scalar(
                select(priority_snapshots.c.id).where(
                    priority_snapshots.c.tenant_id == tenant_id,
                    priority_snapshots.c.learner_id == learner_id,
                    priority_snapshots.c.input_checksum == input_checksum,
                )
            )
            if existing_id is None:
                raise RuntimeError("Priority snapshot conflict could not be resolved")
            return existing_id
        if priorities:
            session.execute(
                insert(priority_items),
                [
                    {
                        "id": uuid4(),
                        "tenant_id": tenant_id,
                        "snapshot_id": inserted_id,
                        "concept_id": concept_ids[item.concept_id],
                        "priority_rank": item.rank,
                        "need": item.need,
                        "importance": item.importance,
                        "urgency": item.urgency,
                        "reliability": item.reliability,
                        "priority_score": item.score,
                        "reasons": list(item.reasons),
                    }
                    for item in priorities
                ],
            )
        return inserted_id


class StudyPlanRepository:
    def create(
        self,
        session: Session,
        *,
        plan_id: UUID,
        tenant_id: UUID,
        learner_id: UUID,
        course_id: UUID,
        snapshot_id: UUID,
        horizon_days: int,
        daily_minutes: int,
        planner_version: str,
        input_checksum: str,
        items: list[dict[str, Any]],
    ) -> UUID:
        inserted_id = session.scalar(
            pg_insert(study_plans)
            .values(
                id=plan_id,
                tenant_id=tenant_id,
                learner_id=learner_id,
                course_id=course_id,
                priority_snapshot_id=snapshot_id,
                horizon_days=horizon_days,
                daily_minutes=daily_minutes,
                planner_version=planner_version,
                input_checksum=input_checksum,
            )
            .on_conflict_do_nothing(constraint="uq_study_plan_input")
            .returning(study_plans.c.id)
        )
        if inserted_id is None:
            existing_id = session.scalar(
                select(study_plans.c.id).where(
                    study_plans.c.tenant_id == tenant_id,
                    study_plans.c.learner_id == learner_id,
                    study_plans.c.input_checksum == input_checksum,
                )
            )
            if existing_id is None:
                raise RuntimeError("Study plan conflict could not be resolved")
            return existing_id
        if items:
            session.execute(
                insert(study_plan_items),
                [{**item, "plan_id": inserted_id} for item in items],
            )
        return inserted_id

    def latest(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        learner_id: UUID,
        course_id: UUID,
        horizon_days: int,
        daily_minutes: int,
    ) -> dict[str, Any] | None:
        plan = (
            session.execute(
                select(study_plans)
                .where(
                    study_plans.c.tenant_id == tenant_id,
                    study_plans.c.learner_id == learner_id,
                    study_plans.c.course_id == course_id,
                    study_plans.c.horizon_days == horizon_days,
                    study_plans.c.daily_minutes == daily_minutes,
                )
                .order_by(study_plans.c.created_at.desc())
                .limit(1)
            )
            .mappings()
            .first()
        )
        if plan is None:
            return None
        item_rows = (
            session.execute(
                select(
                    study_plan_items,
                    concept_nodes.c.normalized_name,
                    concept_nodes.c.canonical_name,
                    graph_versions.c.status.label("graph_status"),
                )
                .join(concept_nodes, concept_nodes.c.id == study_plan_items.c.concept_id)
                .join(graph_versions, graph_versions.c.id == concept_nodes.c.graph_version_id)
                .where(study_plan_items.c.plan_id == plan["id"])
                .order_by(study_plan_items.c.sequence)
            )
            .mappings()
            .all()
        )
        if not item_rows or any(row["graph_status"] != "active" for row in item_rows):
            return None
        score_rows = (
            session.execute(
                select(
                    concept_nodes.c.normalized_name,
                    priority_items.c.need,
                    priority_items.c.importance,
                    priority_items.c.urgency,
                    priority_items.c.reliability,
                    priority_items.c.priority_score,
                    priority_items.c.priority_rank,
                )
                .join(concept_nodes, concept_nodes.c.id == priority_items.c.concept_id)
                .where(priority_items.c.snapshot_id == plan["priority_snapshot_id"])
            )
            .mappings()
            .all()
        )
        return {"plan": plan, "items": item_rows, "scores": score_rows}


class OutboxRepository:
    def add(
        self,
        session: Session,
        *,
        tenant_id: UUID,
        event_type: str,
        aggregate_id: UUID,
        payload: dict[str, Any],
        dedupe_key: str,
    ) -> None:
        session.execute(
            pg_insert(outbox_events)
            .values(
                id=uuid4(),
                tenant_id=tenant_id,
                event_type=event_type,
                aggregate_id=aggregate_id,
                payload=payload,
                dedupe_key=dedupe_key,
                status="pending",
                attempts=0,
            )
            .on_conflict_do_nothing(constraint="uq_outbox_event_dedupe")
        )
