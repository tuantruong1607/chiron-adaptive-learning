"""Add auditable corpus and hierarchical chunk metadata."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0005_corpus_ingestion"
down_revision: str | None = "0004_sessions_outbox"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("document_versions", sa.Column("title", sa.String(500)))
    op.add_column("document_versions", sa.Column("source_path", sa.Text()))
    op.add_column("document_versions", sa.Column("parser_version", sa.String(120)))
    op.add_column(
        "document_versions",
        sa.Column("metadata", postgresql.JSONB(), server_default=sa.text("'{}'::jsonb"), nullable=False),
    )
    op.add_column(
        "chunks", sa.Column("chunk_type", sa.String(24), server_default="child", nullable=False)
    )
    op.add_column("chunks", sa.Column("ordinal", sa.Integer(), server_default="0", nullable=False))
    op.add_column("chunks", sa.Column("token_count", sa.Integer(), server_default="0", nullable=False))
    op.add_column(
        "chunks",
        sa.Column("metadata", postgresql.JSONB(), server_default=sa.text("'{}'::jsonb"), nullable=False),
    )
    op.create_check_constraint("ck_chunks_type", "chunks", "chunk_type IN ('parent', 'child')")
    op.create_check_constraint("ck_chunks_ordinal", "chunks", "ordinal >= 0")
    op.create_check_constraint("ck_chunks_token_count", "chunks", "token_count >= 0")
    op.create_index("ix_chunks_span_type_ordinal", "chunks", ["source_span_id", "chunk_type", "ordinal"])


def downgrade() -> None:
    op.drop_index("ix_chunks_span_type_ordinal", table_name="chunks")
    op.drop_constraint("ck_chunks_token_count", "chunks", type_="check")
    op.drop_constraint("ck_chunks_ordinal", "chunks", type_="check")
    op.drop_constraint("ck_chunks_type", "chunks", type_="check")
    for column in ("metadata", "token_count", "ordinal", "chunk_type"):
        op.drop_column("chunks", column)
    for column in ("metadata", "parser_version", "source_path", "title"):
        op.drop_column("document_versions", column)
