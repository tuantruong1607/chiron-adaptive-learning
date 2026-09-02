"""Create the canonical vertical-slice schema."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0001_vertical_slice"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def common_columns() -> list[sa.Column]:
    return [
        sa.Column("tenant_id", postgresql.UUID(as_uuid=True), nullable=False, index=True),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    ]


def upgrade() -> None:
    op.create_table(
        "courses",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column("slug", sa.String(120), nullable=False),
        sa.Column("title", sa.String(240), nullable=False),
        sa.Column("status", sa.String(32), server_default="draft", nullable=False),
        sa.UniqueConstraint("tenant_id", "slug", name="uq_courses_tenant_slug"),
    )
    op.create_table(
        "document_versions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "course_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("courses.id"), nullable=False
        ),
        sa.Column("checksum", sa.String(64), nullable=False),
        sa.Column("source_type", sa.String(16), nullable=False),
        sa.Column("status", sa.String(32), server_default="pending", nullable=False),
        sa.UniqueConstraint("course_id", "checksum", name="uq_document_versions_checksum"),
    )
    op.create_table(
        "source_spans",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "document_version_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("document_versions.id"),
            nullable=False,
        ),
        sa.Column("locator", postgresql.JSONB(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("checksum", sa.String(64), nullable=False),
    )
    op.create_table(
        "chunks",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "source_span_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("source_spans.id"),
            nullable=False,
        ),
        sa.Column("parent_chunk_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("chunks.id")),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("checksum", sa.String(64), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default=sa.true(), nullable=False),
    )
    op.create_table(
        "graph_versions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "course_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("courses.id"), nullable=False
        ),
        sa.Column("version", sa.String(64), nullable=False),
        sa.Column("status", sa.String(32), server_default="draft", nullable=False),
        sa.UniqueConstraint("course_id", "version", name="uq_graph_version"),
    )
    op.create_table(
        "concept_nodes",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "course_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("courses.id"), nullable=False
        ),
        sa.Column(
            "graph_version_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("graph_versions.id"),
            nullable=False,
        ),
        sa.Column("canonical_name", sa.String(240), nullable=False),
        sa.Column("normalized_name", sa.String(240), nullable=False),
        sa.Column("node_type", sa.String(48), nullable=False),
        sa.Column("summary", sa.Text(), nullable=False),
        sa.UniqueConstraint(
            "course_id",
            "graph_version_id",
            "normalized_name",
            "node_type",
            name="uq_concept_identity",
        ),
    )
    op.create_table(
        "concept_edges",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "graph_version_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("graph_versions.id"),
            nullable=False,
        ),
        sa.Column(
            "source_concept_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("concept_nodes.id"),
            nullable=False,
        ),
        sa.Column(
            "target_concept_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("concept_nodes.id"),
            nullable=False,
        ),
        sa.Column("relation_type", sa.String(48), nullable=False),
        sa.Column("weight", sa.Float(), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column(
            "evidence_source_span_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("source_spans.id"),
            nullable=False,
        ),
        sa.Column("review_status", sa.String(32), server_default="candidate", nullable=False),
        sa.CheckConstraint(
            "source_concept_id <> target_concept_id", name="ck_concept_edge_no_self"
        ),
        sa.UniqueConstraint(
            "graph_version_id",
            "source_concept_id",
            "target_concept_id",
            "relation_type",
            "evidence_source_span_id",
            name="uq_concept_edge_evidence",
        ),
    )
    op.create_index(
        "ix_edges_source_relation", "concept_edges", ["source_concept_id", "relation_type"]
    )
    op.create_index(
        "ix_edges_target_relation", "concept_edges", ["target_concept_id", "relation_type"]
    )
    op.create_table(
        "attempts",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "course_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("courses.id"), nullable=False
        ),
        sa.Column("learner_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("attempt_type", sa.String(32), nullable=False),
        sa.Column("status", sa.String(32), server_default="in_progress", nullable=False),
        sa.Column("idempotency_key", sa.String(128), nullable=False),
        sa.Column("payload", postgresql.JSONB(), server_default="{}", nullable=False),
        sa.UniqueConstraint("tenant_id", "idempotency_key", name="uq_attempt_idempotency"),
    )
    op.create_table(
        "evidence_ledger",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column("learner_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "concept_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("concept_nodes.id"),
            nullable=False,
        ),
        sa.Column(
            "attempt_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("attempts.id"),
            nullable=False,
        ),
        sa.Column("evidence_type", sa.String(48), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("idempotency_key", sa.String(128), nullable=False),
        sa.UniqueConstraint("tenant_id", "idempotency_key", name="uq_evidence_idempotency"),
    )
    op.create_table(
        "outbox_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column("event_type", sa.String(80), nullable=False),
        sa.Column("aggregate_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("payload", postgresql.JSONB(), nullable=False),
        sa.Column("status", sa.String(32), server_default="pending", nullable=False),
        sa.Column("attempts", sa.Integer(), server_default="0", nullable=False),
        sa.Column("next_attempt_at", sa.DateTime(timezone=True)),
    )
    op.create_index("ix_outbox_claim", "outbox_events", ["status", "next_attempt_at"])


def downgrade() -> None:
    for table in [
        "outbox_events",
        "evidence_ledger",
        "attempts",
        "concept_edges",
        "concept_nodes",
        "graph_versions",
        "chunks",
        "source_spans",
        "document_versions",
        "courses",
    ]:
        op.drop_table(table)
