"""Add identity, tenant membership, enrollment, foreign keys, and RLS."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0003_identity_tenancy"
down_revision: str | None = "0002_adaptive_core"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

TENANT_TABLES = (
    "memberships",
    "course_enrollments",
    "courses",
    "document_versions",
    "source_spans",
    "chunks",
    "graph_versions",
    "concept_nodes",
    "concept_edges",
    "attempts",
    "evidence_ledger",
    "outbox_events",
    "mastery_states",
    "priority_snapshots",
    "priority_items",
    "study_plans",
    "study_plan_items",
)


def timestamps() -> list[sa.Column]:
    return [
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    ]


def upgrade() -> None:
    op.add_column("courses", sa.Column("exam_date", sa.Date(), nullable=True))
    op.add_column(
        "concept_nodes",
        sa.Column("exam_weight", sa.Float(), server_default="0.5", nullable=False),
    )
    op.create_check_constraint(
        "ck_concept_exam_weight", "concept_nodes", "exam_weight BETWEEN 0 AND 1"
    )
    op.create_table(
        "tenants",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *timestamps(),
        sa.Column("slug", sa.String(120), nullable=False, unique=True),
        sa.Column("name", sa.String(240), nullable=False),
        sa.Column("status", sa.String(24), server_default="active", nullable=False),
        sa.CheckConstraint("status IN ('active', 'suspended')", name="ck_tenant_status"),
    )
    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        *timestamps(),
        sa.Column("email", sa.String(320), nullable=False, unique=True),
        sa.Column("password_hash", sa.Text(), nullable=False),
        sa.Column("display_name", sa.String(240), nullable=False),
        sa.Column("status", sa.String(24), server_default="active", nullable=False),
        sa.CheckConstraint("status IN ('active', 'disabled')", name="ck_user_status"),
    )
    op.create_table(
        "memberships",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        *timestamps(),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("role", sa.String(24), nullable=False),
        sa.Column("status", sa.String(24), server_default="active", nullable=False),
        sa.CheckConstraint("role IN ('learner', 'instructor', 'admin')", name="ck_membership_role"),
        sa.CheckConstraint("status IN ('active', 'revoked')", name="ck_membership_status"),
        sa.UniqueConstraint("tenant_id", "user_id", name="uq_membership_tenant_user"),
    )
    op.create_table(
        "course_enrollments",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        *timestamps(),
        sa.Column(
            "course_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("courses.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "learner_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("status", sa.String(24), server_default="active", nullable=False),
        sa.CheckConstraint(
            "status IN ('active', 'completed', 'revoked')", name="ck_enrollment_status"
        ),
        sa.UniqueConstraint(
            "tenant_id", "course_id", "learner_id", name="uq_enrollment_course_learner"
        ),
    )

    for table_name in TENANT_TABLES[2:]:
        op.create_foreign_key(
            f"fk_{table_name}_tenant",
            table_name,
            "tenants",
            ["tenant_id"],
            ["id"],
        )

    for table_name in (
        "attempts",
        "evidence_ledger",
        "mastery_states",
        "priority_snapshots",
        "study_plans",
    ):
        op.create_foreign_key(
            f"fk_{table_name}_learner",
            table_name,
            "users",
            ["learner_id"],
            ["id"],
        )

    for table_name in TENANT_TABLES:
        policy_name = f"tenant_isolation_{table_name}"
        op.execute(f'ALTER TABLE "{table_name}" ENABLE ROW LEVEL SECURITY')
        op.execute(f'ALTER TABLE "{table_name}" FORCE ROW LEVEL SECURITY')
        op.execute(
            f'CREATE POLICY "{policy_name}" ON "{table_name}" '
            "USING (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid) "
            "WITH CHECK (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid)"
        )


def downgrade() -> None:
    for table_name in reversed(TENANT_TABLES):
        policy_name = f"tenant_isolation_{table_name}"
        op.execute(f'DROP POLICY IF EXISTS "{policy_name}" ON "{table_name}"')
        op.execute(f'ALTER TABLE "{table_name}" DISABLE ROW LEVEL SECURITY')

    for table_name in (
        "attempts",
        "evidence_ledger",
        "mastery_states",
        "priority_snapshots",
        "study_plans",
    ):
        op.drop_constraint(f"fk_{table_name}_learner", table_name, type_="foreignkey")
    for table_name in reversed(TENANT_TABLES[2:]):
        op.drop_constraint(f"fk_{table_name}_tenant", table_name, type_="foreignkey")

    op.drop_table("course_enrollments")
    op.drop_table("memberships")
    op.drop_table("users")
    op.drop_table("tenants")
    op.drop_constraint("ck_concept_exam_weight", "concept_nodes", type_="check")
    op.drop_column("concept_nodes", "exam_weight")
    op.drop_column("courses", "exam_date")
