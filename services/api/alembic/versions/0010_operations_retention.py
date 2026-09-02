"""Add auditable retention enforcement runs."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0010_operations_retention"
down_revision: str | None = "0009_question_bank_p0"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "data_retention_runs",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("status", sa.String(24), nullable=False),
        sa.Column("policy", postgresql.JSONB(), nullable=False),
        sa.Column("affected_rows", postgresql.JSONB(), nullable=False),
        sa.Column("started_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("error", sa.Text(), nullable=True),
        sa.CheckConstraint("status IN ('completed', 'failed')", name="ck_retention_run_status"),
    )
    op.create_index(
        "ix_data_retention_runs_tenant_completed",
        "data_retention_runs",
        ["tenant_id", "completed_at"],
    )
    op.execute("ALTER TABLE data_retention_runs ENABLE ROW LEVEL SECURITY")
    op.execute("ALTER TABLE data_retention_runs FORCE ROW LEVEL SECURITY")
    op.execute(
        "CREATE POLICY tenant_isolation_data_retention_runs ON data_retention_runs "
        "USING (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid) "
        "WITH CHECK (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid)"
    )
    op.execute(
        """
        DO $$
        BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'chiron_runtime') THEN
            GRANT SELECT, INSERT ON data_retention_runs TO chiron_runtime;
            REVOKE UPDATE, DELETE ON data_retention_runs FROM chiron_runtime;
          END IF;
        END $$
        """
    )


def downgrade() -> None:
    op.execute(
        "DROP POLICY IF EXISTS tenant_isolation_data_retention_runs ON data_retention_runs"
    )
    op.drop_table("data_retention_runs")
