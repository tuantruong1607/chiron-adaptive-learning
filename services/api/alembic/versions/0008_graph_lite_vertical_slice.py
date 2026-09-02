"""Add reviewed graph provenance and chunk-to-concept links."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0008_graph_lite_vertical_slice"
down_revision: str | None = "0007_memory_permissions"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column(
        "concept_nodes",
        sa.Column("confidence", sa.Float(), server_default="0", nullable=False),
    )
    op.add_column(
        "concept_nodes",
        sa.Column("extraction_method", sa.String(48), server_default="manual", nullable=False),
    )
    op.add_column(
        "concept_nodes",
        sa.Column("review_status", sa.String(24), server_default="candidate", nullable=False),
    )
    op.add_column(
        "concept_nodes",
        sa.Column(
            "evidence_source_span_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("source_spans.id"),
            nullable=True,
        ),
    )
    op.create_check_constraint(
        "ck_concept_node_confidence", "concept_nodes", "confidence BETWEEN 0 AND 1"
    )
    op.create_check_constraint(
        "ck_concept_node_review_status",
        "concept_nodes",
        "review_status IN ('candidate', 'approved', 'active', 'rejected')",
    )
    op.create_check_constraint(
        "ck_active_concept_node_has_evidence",
        "concept_nodes",
        "review_status <> 'active' OR evidence_source_span_id IS NOT NULL",
    )

    op.add_column(
        "concept_edges",
        sa.Column("extraction_method", sa.String(48), server_default="manual", nullable=False),
    )
    op.create_check_constraint(
        "ck_concept_edge_confidence", "concept_edges", "confidence BETWEEN 0 AND 1"
    )
    op.create_check_constraint(
        "ck_concept_edge_review_status",
        "concept_edges",
        "review_status IN ('candidate', 'approved', 'active', 'rejected')",
    )

    op.create_table(
        "chunk_concepts",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column(
            "tenant_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("tenants.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "graph_version_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("graph_versions.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "chunk_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("chunks.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "concept_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("concept_nodes.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "evidence_source_span_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey("source_spans.id"),
            nullable=False,
        ),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("extraction_method", sa.String(48), nullable=False),
        sa.Column("review_status", sa.String(24), server_default="candidate", nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.CheckConstraint("confidence BETWEEN 0 AND 1", name="ck_chunk_concept_confidence"),
        sa.CheckConstraint(
            "review_status IN ('candidate', 'approved', 'active', 'rejected')",
            name="ck_chunk_concept_review_status",
        ),
        sa.UniqueConstraint(
            "graph_version_id", "chunk_id", "concept_id", name="uq_chunk_concept_link"
        ),
    )
    op.create_index(
        "ix_chunk_concepts_concept_review",
        "chunk_concepts",
        ["concept_id", "review_status"],
    )
    op.create_index(
        "ix_chunk_concepts_chunk_review",
        "chunk_concepts",
        ["chunk_id", "review_status"],
    )
    op.execute('ALTER TABLE "chunk_concepts" ENABLE ROW LEVEL SECURITY')
    op.execute('ALTER TABLE "chunk_concepts" FORCE ROW LEVEL SECURITY')
    op.execute(
        'CREATE POLICY "tenant_isolation_chunk_concepts" ON "chunk_concepts" '
        "USING (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid) "
        "WITH CHECK (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid)"
    )
    op.execute(
        """
        DO $$
        BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'chiron_runtime') THEN
            GRANT SELECT ON graph_versions, concept_nodes, concept_edges, chunk_concepts
              TO chiron_runtime;
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
            REVOKE SELECT ON chunk_concepts FROM chiron_runtime;
          END IF;
        END $$
        """
    )
    op.execute('DROP POLICY IF EXISTS "tenant_isolation_chunk_concepts" ON "chunk_concepts"')
    op.drop_table("chunk_concepts")
    op.drop_constraint("ck_concept_edge_review_status", "concept_edges", type_="check")
    op.drop_constraint("ck_concept_edge_confidence", "concept_edges", type_="check")
    op.drop_column("concept_edges", "extraction_method")
    op.drop_constraint("ck_active_concept_node_has_evidence", "concept_nodes", type_="check")
    op.drop_constraint("ck_concept_node_review_status", "concept_nodes", type_="check")
    op.drop_constraint("ck_concept_node_confidence", "concept_nodes", type_="check")
    op.drop_column("concept_nodes", "evidence_source_span_id")
    op.drop_column("concept_nodes", "review_status")
    op.drop_column("concept_nodes", "extraction_method")
    op.drop_column("concept_nodes", "confidence")
