from __future__ import annotations

import argparse
import json
from datetime import date
from uuid import NAMESPACE_URL, UUID, uuid5

from sqlalchemy.dialects.postgresql import insert as pg_insert

from app.auth import hash_password
from app.db import get_session_factory, set_tenant_context
from app.persistence.tables import (
    chunk_concepts,
    chunks,
    concept_edges,
    concept_nodes,
    course_enrollments,
    courses,
    document_versions,
    graph_versions,
    mastery_states,
    memberships,
    outbox_events,
    source_spans,
    tenants,
    users,
)
from app.seed import CONCEPTS, COURSE, EDGES


def stable_id(name: str) -> UUID:
    return uuid5(NAMESPACE_URL, f"https://chiron.local/demo/{name}")


def upsert(session, table, values: dict, constraint: str, update_fields: tuple[str, ...]) -> None:
    session.execute(
        pg_insert(table)
        .values(**values)
        .on_conflict_do_update(
            constraint=constraint,
            set_={field: values[field] for field in update_fields},
        )
    )


def seed(tenant_slug: str, email: str, password: str) -> dict[str, str]:
    tenant_id = stable_id(f"tenant:{tenant_slug}")
    user_id = stable_id(f"user:{email.casefold()}")
    instructor_email = "instructor@chiron.local"
    instructor_id = stable_id(f"user:{instructor_email}")
    course_id = stable_id(f"course:{tenant_slug}:{COURSE.id}")
    graph_id = stable_id(f"graph:{course_id}:graph-2026.08")
    document_id = stable_id(f"document:{course_id}:demo-source")
    span_id = stable_id(f"span:{document_id}:overview")
    chunk_id = stable_id(f"chunk:{span_id}:overview")
    session_factory = get_session_factory()

    with session_factory() as session, session.begin():
        upsert(
            session,
            tenants,
            {
                "id": tenant_id,
                "slug": tenant_slug,
                "name": "Chiron Demo Academy",
                "status": "active",
            },
            "tenants_slug_key",
            ("name", "status"),
        )
        set_tenant_context(session, tenant_id)
        upsert(
            session,
            users,
            {
                "id": user_id,
                "email": email.casefold(),
                "password_hash": hash_password(password),
                "display_name": "Demo Learner",
                "status": "active",
            },
            "users_email_key",
            ("password_hash", "display_name", "status"),
        )
        upsert(
            session,
            memberships,
            {
                "id": stable_id(f"membership:{tenant_id}:{user_id}"),
                "tenant_id": tenant_id,
                "user_id": user_id,
                "role": "learner",
                "status": "active",
            },
            "uq_membership_tenant_user",
            ("role", "status"),
        )
        upsert(
            session,
            users,
            {
                "id": instructor_id,
                "email": instructor_email,
                "password_hash": hash_password(password),
                "display_name": "Demo Instructor",
                "status": "active",
            },
            "users_email_key",
            ("password_hash", "display_name", "status"),
        )
        upsert(
            session,
            memberships,
            {
                "id": stable_id(f"membership:{tenant_id}:{instructor_id}"),
                "tenant_id": tenant_id,
                "user_id": instructor_id,
                "role": "instructor",
                "status": "active",
            },
            "uq_membership_tenant_user",
            ("role", "status"),
        )
        upsert(
            session,
            courses,
            {
                "id": course_id,
                "tenant_id": tenant_id,
                "slug": COURSE.id,
                "title": COURSE.title,
                "status": "published",
                "exam_date": date.fromisoformat(COURSE.exam_date),
            },
            "uq_courses_tenant_slug",
            ("title", "status", "exam_date"),
        )
        upsert(
            session,
            course_enrollments,
            {
                "id": stable_id(f"enrollment:{tenant_id}:{course_id}:{user_id}"),
                "tenant_id": tenant_id,
                "course_id": course_id,
                "learner_id": user_id,
                "status": "active",
            },
            "uq_enrollment_course_learner",
            ("status",),
        )
        upsert(
            session,
            graph_versions,
            {
                "id": graph_id,
                "tenant_id": tenant_id,
                "course_id": course_id,
                "version": "graph-2026.08",
                "status": "active",
            },
            "uq_graph_version",
            ("status",),
        )
        upsert(
            session,
            document_versions,
            {
                "id": document_id,
                "tenant_id": tenant_id,
                "course_id": course_id,
                "checksum": "demo-source-v1",
                "source_type": "html",
                "status": "active",
            },
            "uq_document_versions_checksum",
            ("status",),
        )
        session.execute(
            pg_insert(source_spans)
            .values(
                id=span_id,
                tenant_id=tenant_id,
                document_version_id=document_id,
                locator={"section": "demo-overview"},
                text="Chiron demo source span for reviewed prerequisite relationships.",
                checksum="demo-span-v1",
            )
            .on_conflict_do_nothing(index_elements=[source_spans.c.id])
        )
        session.execute(
            pg_insert(chunks)
            .values(
                id=chunk_id,
                tenant_id=tenant_id,
                source_span_id=span_id,
                content=(
                    "Reciprocal Rank Fusion kết hợp dense và sparse retrieval theo thứ hạng, "
                    "giúp tránh cộng trực tiếp các raw score khác thang đo."
                ),
                checksum="demo-chunk-rrf-v1",
                is_active=True,
            )
            .on_conflict_do_update(
                index_elements=[chunks.c.id],
                set_={
                    "content": (
                        "Reciprocal Rank Fusion kết hợp dense và sparse retrieval theo thứ hạng, "
                        "giúp tránh cộng trực tiếp các raw score khác thang đo."
                    ),
                    "checksum": "demo-chunk-rrf-v1",
                    "is_active": True,
                },
            )
        )
        session.execute(
            pg_insert(outbox_events)
            .values(
                id=stable_id(
                    f"outbox:chunks.sync_requested:{chunk_id}:multilingual-e5-large-mean-v1"
                ),
                tenant_id=tenant_id,
                event_type="chunks.sync_requested",
                aggregate_id=document_id,
                payload={
                    "chunk_ids": [str(chunk_id)],
                    "operation": "upsert",
                    "embedding_version": "multilingual-e5-large-mean-v1",
                },
                dedupe_key=(
                    f"chunks.sync_requested:{chunk_id}:multilingual-e5-large-mean-v1"
                ),
                status="pending",
                attempts=0,
            )
            .on_conflict_do_nothing(constraint="uq_outbox_event_dedupe")
        )

        concept_ids: dict[str, UUID] = {}
        for concept in CONCEPTS:
            concept_id = stable_id(f"concept:{course_id}:{concept.id}")
            concept_ids[concept.id] = concept_id
            upsert(
                session,
                concept_nodes,
                {
                    "id": concept_id,
                    "tenant_id": tenant_id,
                    "course_id": course_id,
                    "graph_version_id": graph_id,
                    "canonical_name": concept.name,
                    "normalized_name": concept.id,
                    "node_type": "concept",
                    "summary": concept.summary,
                    "exam_weight": concept.exam_weight,
                    "confidence": 1.0,
                    "extraction_method": "manual_seed",
                    "review_status": "active",
                    "evidence_source_span_id": span_id,
                },
                "uq_concept_identity",
                (
                    "canonical_name",
                    "summary",
                    "exam_weight",
                    "confidence",
                    "extraction_method",
                    "review_status",
                    "evidence_source_span_id",
                ),
            )
            session.execute(
                pg_insert(chunk_concepts)
                .values(
                    id=stable_id(f"chunk-concept:{graph_id}:{chunk_id}:{concept_id}"),
                    tenant_id=tenant_id,
                    graph_version_id=graph_id,
                    chunk_id=chunk_id,
                    concept_id=concept_id,
                    evidence_source_span_id=span_id,
                    confidence=1.0,
                    extraction_method="manual_seed",
                    review_status="active",
                )
                .on_conflict_do_nothing(constraint="uq_chunk_concept_link")
            )
            upsert(
                session,
                mastery_states,
                {
                    "id": stable_id(f"mastery:{tenant_id}:{user_id}:{concept_id}"),
                    "tenant_id": tenant_id,
                    "learner_id": user_id,
                    "concept_id": concept_id,
                    "self_confidence": concept.confidence,
                    "diagnostic_status": "partial",
                    "mastery": concept.mastery,
                    "evidence_confidence": concept.confidence,
                    "confidence_gap": round(concept.confidence - concept.mastery, 4),
                    "misconception": False,
                    "evidence_ids": [f"seed-{concept.id}"],
                    "engine_version": "adaptive-v1",
                },
                "uq_mastery_learner_concept",
                (
                    "self_confidence",
                    "diagnostic_status",
                    "mastery",
                    "evidence_confidence",
                    "confidence_gap",
                    "misconception",
                    "evidence_ids",
                    "engine_version",
                ),
            )

        for edge in EDGES:
            session.execute(
                pg_insert(concept_edges)
                .values(
                    id=stable_id(f"edge:{graph_id}:{edge.id}"),
                    tenant_id=tenant_id,
                    graph_version_id=graph_id,
                    source_concept_id=concept_ids[edge.source],
                    target_concept_id=concept_ids[edge.target],
                    relation_type=edge.relation.value,
                    weight=edge.weight,
                    confidence=1.0,
                    evidence_source_span_id=span_id,
                    review_status="active",
                    extraction_method="manual_seed",
                )
                .on_conflict_do_nothing(constraint="uq_concept_edge_evidence")
            )

    return {
        "tenant_slug": tenant_slug,
        "email": email.casefold(),
        "instructor_email": instructor_email,
        "course_slug": COURSE.id,
        "tenant_id": str(tenant_id),
        "user_id": str(user_id),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed one Chiron demo tenant and learner")
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--email", default="learner@chiron.local")
    parser.add_argument("--password", default="chiron-demo-2026")
    args = parser.parse_args()
    print(json.dumps(seed(args.tenant, args.email, args.password), indent=2))


if __name__ == "__main__":
    main()
