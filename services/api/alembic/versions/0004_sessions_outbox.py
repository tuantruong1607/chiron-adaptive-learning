"""Add refresh-token rotation and durable outbox leases."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0004_sessions_outbox"
down_revision: str | None = "0003_identity_tenancy"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "auth_refresh_sessions",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "user_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("token_hash", sa.String(64), nullable=False, unique=True),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("revoked_at", sa.DateTime(timezone=True)),
        sa.Column(
            "replaced_by_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("auth_refresh_sessions.id"),
        ),
        sa.Column("user_agent", sa.String(512)),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index(
        "ix_refresh_session_active",
        "auth_refresh_sessions",
        ["tenant_id", "user_id", "expires_at"],
    )
    op.execute('ALTER TABLE "auth_refresh_sessions" ENABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE "auth_refresh_sessions" FORCE ROW LEVEL SECURITY')
    op.execute(
        'CREATE POLICY "tenant_isolation_auth_refresh_sessions" '
        'ON "auth_refresh_sessions" '
        "USING (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid) "
        "WITH CHECK (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid)"
    )

    op.add_column("outbox_events", sa.Column("dedupe_key", sa.String(240)))
    op.add_column("outbox_events", sa.Column("locked_at", sa.DateTime(timezone=True)))
    op.add_column("outbox_events", sa.Column("locked_by", sa.String(160)))
    op.add_column("outbox_events", sa.Column("last_error", sa.Text()))
    op.add_column("outbox_events", sa.Column("processed_at", sa.DateTime(timezone=True)))
    op.execute("UPDATE outbox_events SET dedupe_key = 'legacy:' || id::text")
    op.alter_column("outbox_events", "dedupe_key", nullable=False)
    op.create_unique_constraint(
        "uq_outbox_event_dedupe",
        "outbox_events",
        ["tenant_id", "event_type", "dedupe_key"],
    )


def downgrade() -> None:
    op.drop_constraint("uq_outbox_event_dedupe", "outbox_events", type_="unique")
    for column in ("processed_at", "last_error", "locked_by", "locked_at", "dedupe_key"):
        op.drop_column("outbox_events", column)
    op.execute(
        'DROP POLICY IF EXISTS "tenant_isolation_auth_refresh_sessions" ON "auth_refresh_sessions"'
    )
    op.drop_table("auth_refresh_sessions")
