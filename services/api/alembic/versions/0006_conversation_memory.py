"""Add tenant-scoped short-term conversation memory and episodic events."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0006_conversation_memory"
down_revision: str | None = "0005_corpus_ingestion"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

TENANT_TABLES = ("chat_threads", "chat_messages", "learning_events")


def _enable_rls(table_name: str) -> None:
    op.execute(f'ALTER TABLE "{table_name}" ENABLE ROW LEVEL SECURITY')
    op.execute(f'ALTER TABLE "{table_name}" FORCE ROW LEVEL SECURITY')
    op.execute(
        f'CREATE POLICY "tenant_isolation_{table_name}" ON "{table_name}" '
        "USING (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid) "
        "WITH CHECK (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid)"
    )


def upgrade() -> None:
    op.create_table(
        "chat_threads",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
        ),
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
        sa.Column("title", sa.String(240)),
        sa.Column("initial_idempotency_key", sa.String(240), nullable=False),
        sa.Column("short_summary", sa.Text()),
        sa.Column("summary_through_sequence", sa.Integer(), server_default="0", nullable=False),
        sa.Column("next_sequence", sa.Integer(), server_default="0", nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "last_message_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.CheckConstraint("status IN ('active', 'archived')", name="ck_chat_thread_status"),
        sa.CheckConstraint(
            "summary_through_sequence >= 0 AND next_sequence >= summary_through_sequence",
            name="ck_chat_thread_sequences",
        ),
        sa.UniqueConstraint(
            "tenant_id",
            "learner_id",
            "course_id",
            "initial_idempotency_key",
            name="uq_chat_thread_initial_request",
        ),
    )
    op.create_index(
        "ix_chat_threads_learner_course",
        "chat_threads",
        ["tenant_id", "learner_id", "course_id", "status"],
    )
    op.create_index(
        "ix_chat_threads_last_message", "chat_threads", ["tenant_id", "last_message_at"]
    )

    op.create_table(
        "chat_messages",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "thread_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("chat_threads.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("role", sa.String(16), nullable=False),
        sa.Column("sequence", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column(
            "citations",
            postgresql.JSONB(),
            server_default=sa.text("'[]'::jsonb"),
            nullable=False,
        ),
        sa.Column(
            "metadata",
            postgresql.JSONB(),
            server_default=sa.text("'{}'::jsonb"),
            nullable=False,
        ),
        sa.Column("idempotency_key", sa.String(240), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.CheckConstraint("role IN ('user', 'assistant', 'system')", name="ck_chat_message_role"),
        sa.CheckConstraint("sequence > 0", name="ck_chat_message_sequence"),
        sa.UniqueConstraint("thread_id", "sequence", name="uq_chat_message_sequence"),
        sa.UniqueConstraint(
            "tenant_id", "thread_id", "idempotency_key", name="uq_chat_message_idempotency"
        ),
    )
    op.create_index(
        "ix_chat_messages_thread_sequence", "chat_messages", ["thread_id", "sequence"]
    )

    op.create_table(
        "learning_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "learner_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "course_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("courses.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "thread_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("chat_threads.id", ondelete="SET NULL"),
        ),
        sa.Column(
            "attempt_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("attempts.id", ondelete="SET NULL"),
        ),
        sa.Column("event_type", sa.String(120), nullable=False),
        sa.Column(
            "payload",
            postgresql.JSONB(),
            server_default=sa.text("'{}'::jsonb"),
            nullable=False,
        ),
        sa.Column("idempotency_key", sa.String(240), nullable=False),
        sa.Column(
            "occurred_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.UniqueConstraint("tenant_id", "idempotency_key", name="uq_learning_event_idempotency"),
    )
    op.create_index(
        "ix_learning_events_timeline",
        "learning_events",
        ["tenant_id", "learner_id", "course_id", "occurred_at"],
    )
    op.create_index(
        "ix_learning_events_thread", "learning_events", ["thread_id", "occurred_at"]
    )
    op.create_index("ix_learning_events_type", "learning_events", ["tenant_id", "event_type"])

    for table_name in TENANT_TABLES:
        _enable_rls(table_name)

    op.execute(
        """
        DO $$
        BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'chiron_runtime') THEN
            GRANT SELECT, INSERT, UPDATE ON chat_threads, chat_messages TO chiron_runtime;
            GRANT SELECT, INSERT ON learning_events TO chiron_runtime;
          END IF;
        END $$
        """
    )


def downgrade() -> None:
    for table_name in reversed(TENANT_TABLES):
        op.execute(f'DROP POLICY IF EXISTS "tenant_isolation_{table_name}" ON "{table_name}"')
    op.drop_table("learning_events")
    op.drop_table("chat_messages")
    op.drop_table("chat_threads")
