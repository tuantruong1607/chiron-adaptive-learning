"""Add durable adaptive state, priority snapshots, and cram plans."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0002_adaptive_core"
down_revision: str | None = "0001_vertical_slice"
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
        "mastery_states",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column("learner_id", postgresql.UUID(as_uuid=True), nullable=False, index=True),
        sa.Column(
            "concept_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("concept_nodes.id"),
            nullable=False,
        ),
        sa.Column("self_confidence", sa.Float(), nullable=False),
        sa.Column("diagnostic_status", sa.String(24), nullable=False),
        sa.Column("mastery", sa.Float()),
        sa.Column("evidence_confidence", sa.Float()),
        sa.Column("confidence_gap", sa.Float()),
        sa.Column("misconception", sa.Boolean(), server_default=sa.false(), nullable=False),
        sa.Column("evidence_ids", postgresql.JSONB(), server_default="[]", nullable=False),
        sa.Column("engine_version", sa.String(64), nullable=False),
        sa.CheckConstraint("self_confidence BETWEEN 0 AND 1", name="ck_mastery_self_confidence"),
        sa.CheckConstraint("mastery IS NULL OR mastery BETWEEN 0 AND 1", name="ck_mastery_value"),
        sa.CheckConstraint(
            "evidence_confidence IS NULL OR evidence_confidence BETWEEN 0 AND 1",
            name="ck_mastery_evidence_confidence",
        ),
        sa.CheckConstraint(
            "diagnostic_status IN ('not_assessed', 'unverified', 'partial', 'verified')",
            name="ck_mastery_status",
        ),
        sa.CheckConstraint(
            "(diagnostic_status IN ('not_assessed', 'unverified') AND mastery IS NULL "
            "AND evidence_confidence IS NULL AND confidence_gap IS NULL) OR "
            "(diagnostic_status IN ('partial', 'verified') AND mastery IS NOT NULL "
            "AND evidence_confidence IS NOT NULL)",
            name="ck_mastery_status_coherence",
        ),
        sa.UniqueConstraint(
            "tenant_id", "learner_id", "concept_id", name="uq_mastery_learner_concept"
        ),
    )

    op.create_table(
        "priority_snapshots",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column("learner_id", postgresql.UUID(as_uuid=True), nullable=False, index=True),
        sa.Column(
            "course_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("courses.id"),
            nullable=False,
        ),
        sa.Column("evaluated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("exam_date", sa.Date(), nullable=False),
        sa.Column("engine_version", sa.String(64), nullable=False),
        sa.Column("input_checksum", sa.String(64), nullable=False),
        sa.UniqueConstraint(
            "tenant_id", "learner_id", "input_checksum", name="uq_priority_snapshot_input"
        ),
    )
    op.create_table(
        "priority_items",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "snapshot_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("priority_snapshots.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "concept_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("concept_nodes.id"),
            nullable=False,
        ),
        sa.Column("priority_rank", sa.Integer(), nullable=False),
        sa.Column("need", sa.Float(), nullable=False),
        sa.Column("importance", sa.Float(), nullable=False),
        sa.Column("urgency", sa.Float(), nullable=False),
        sa.Column("reliability", sa.Float(), nullable=False),
        sa.Column("priority_score", sa.Float(), nullable=False),
        sa.Column("reasons", postgresql.JSONB(), server_default="[]", nullable=False),
        sa.CheckConstraint("priority_score BETWEEN 0 AND 1", name="ck_priority_score"),
        sa.UniqueConstraint("snapshot_id", "concept_id", name="uq_priority_item_concept"),
    )

    op.create_table(
        "study_plans",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column("learner_id", postgresql.UUID(as_uuid=True), nullable=False, index=True),
        sa.Column(
            "course_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("courses.id"),
            nullable=False,
        ),
        sa.Column(
            "priority_snapshot_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("priority_snapshots.id"),
            nullable=False,
        ),
        sa.Column("horizon_days", sa.Integer(), nullable=False),
        sa.Column("daily_minutes", sa.Integer(), nullable=False),
        sa.Column("planner_version", sa.String(64), nullable=False),
        sa.Column("input_checksum", sa.String(64), nullable=False),
        sa.CheckConstraint("horizon_days IN (3, 4)", name="ck_plan_horizon"),
        sa.CheckConstraint("daily_minutes BETWEEN 30 AND 480", name="ck_plan_daily_minutes"),
        sa.UniqueConstraint(
            "tenant_id", "learner_id", "input_checksum", name="uq_study_plan_input"
        ),
    )
    op.create_table(
        "study_plan_items",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *common_columns(),
        sa.Column(
            "plan_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("study_plans.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "concept_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("concept_nodes.id"),
            nullable=False,
        ),
        sa.Column("day_offset", sa.Integer()),
        sa.Column("sequence", sa.Integer(), nullable=False),
        sa.Column("activity", sa.String(32), nullable=False),
        sa.Column("duration_minutes", sa.Integer(), nullable=False),
        sa.Column("expected_gain", sa.Float(), nullable=False),
        sa.Column("decision_status", sa.String(16), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.CheckConstraint("decision_status IN ('scheduled', 'deferred')", name="ck_plan_decision"),
        sa.UniqueConstraint("plan_id", "sequence", name="uq_plan_item_sequence"),
    )


def downgrade() -> None:
    for table in [
        "study_plan_items",
        "study_plans",
        "priority_items",
        "priority_snapshots",
        "mastery_states",
    ]:
        op.drop_table(table)
