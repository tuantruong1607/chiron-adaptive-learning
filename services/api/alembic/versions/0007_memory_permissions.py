"""Harden runtime privileges for conversation and episodic memory."""

from collections.abc import Sequence

from alembic import op

revision: str = "0007_memory_permissions"
down_revision: str | None = "0006_conversation_memory"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute(
        """
        DO $$
        BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'chiron_runtime') THEN
            REVOKE DELETE ON chat_threads, chat_messages FROM chiron_runtime;
            REVOKE UPDATE, DELETE ON learning_events FROM chiron_runtime;
          END IF;
        END $$
        """
    )


def downgrade() -> None:
    op.execute(
        """
        DO $$
        BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'chiron_runtime') THEN
            GRANT DELETE ON chat_threads, chat_messages TO chiron_runtime;
            GRANT UPDATE, DELETE ON learning_events TO chiron_runtime;
          END IF;
        END $$
        """
    )
