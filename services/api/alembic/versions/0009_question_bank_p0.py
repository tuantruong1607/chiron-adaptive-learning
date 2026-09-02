"""Add evidence-grounded question-bank authoring records."""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision: str = "0009_question_bank_p0"
down_revision: str | None = "0008_graph_lite_vertical_slice"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def _tenant_policy(table: str) -> None:
    op.execute(f'ALTER TABLE "{table}" ENABLE ROW LEVEL SECURITY')
    op.execute(f'ALTER TABLE "{table}" FORCE ROW LEVEL SECURITY')
    op.execute(
        f'CREATE POLICY "tenant_isolation_{table}" ON "{table}" '
        "USING (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid) "
        "WITH CHECK (tenant_id = NULLIF(current_setting('app.tenant_id', true), '')::uuid)"
    )


def _runtime_grants() -> None:
    op.execute(
        """
        DO $$
        BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'chiron_runtime') THEN
            GRANT SELECT, INSERT, UPDATE ON question_specs, evidence_packs,
              evidence_pack_spans, question_candidates, question_concepts,
              item_validations, review_decisions TO chiron_runtime;
          END IF;
        END $$
        """
    )


def upgrade() -> None:
    uuid = postgresql.UUID(as_uuid=True)
    jsonb = postgresql.JSONB()
    op.create_table(
        "question_specs",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("tenant_id", uuid, sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("course_id", uuid, sa.ForeignKey("courses.id", ondelete="CASCADE"), nullable=False),
        sa.Column("external_id", sa.String(160), nullable=False),
        sa.Column("blueprint_cell", jsonb, nullable=False),
        sa.Column("concept_slugs", jsonb, nullable=False),
        sa.Column("learning_objective", sa.Text(), nullable=False),
        sa.Column("format", sa.String(64), nullable=False),
        sa.Column("cognitive_level", sa.String(24), nullable=False),
        sa.Column("difficulty_target", sa.String(16), nullable=False),
        sa.Column("misconception_target", sa.Text(), nullable=False),
        sa.Column("required_evidence", sa.Integer(), server_default="1", nullable=False),
        sa.Column("generation_count", sa.Integer(), server_default="1", nullable=False),
        sa.Column("exposure_group", sa.String(80), nullable=False),
        sa.Column("state", sa.String(24), server_default="draft", nullable=False),
        sa.Column("input_checksum", sa.String(64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("required_evidence BETWEEN 1 AND 5", name="ck_question_spec_evidence"),
        sa.CheckConstraint("generation_count BETWEEN 1 AND 5", name="ck_question_spec_generation"),
        sa.CheckConstraint("state IN ('draft', 'ready', 'retired')", name="ck_question_spec_state"),
        sa.UniqueConstraint("tenant_id", "course_id", "external_id", name="uq_question_spec_external_id"),
    )
    op.create_index("ix_question_specs_course_state", "question_specs", ["course_id", "state"])

    op.create_table(
        "evidence_packs",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("tenant_id", uuid, sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("course_id", uuid, sa.ForeignKey("courses.id", ondelete="CASCADE"), nullable=False),
        sa.Column("question_spec_id", uuid, sa.ForeignKey("question_specs.id", ondelete="CASCADE"), nullable=False),
        sa.Column("corpus_version", sa.String(128), nullable=False),
        sa.Column("retrieval_mode", sa.String(32), nullable=False),
        sa.Column("retrieval_trace", jsonb, server_default=sa.text("'{}'::jsonb"), nullable=False),
        sa.Column("checksum", sa.String(64), nullable=False),
        sa.Column("state", sa.String(24), server_default="frozen", nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("state IN ('frozen', 'superseded')", name="ck_evidence_pack_state"),
        sa.UniqueConstraint("question_spec_id", "checksum", name="uq_evidence_pack_snapshot"),
    )
    op.create_index("ix_evidence_packs_spec", "evidence_packs", ["question_spec_id", "state"])

    op.create_table(
        "evidence_pack_spans",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("tenant_id", uuid, sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("evidence_pack_id", uuid, sa.ForeignKey("evidence_packs.id", ondelete="CASCADE"), nullable=False),
        sa.Column("source_span_id", uuid, sa.ForeignKey("source_spans.id"), nullable=False),
        sa.Column("rank", sa.Integer(), nullable=False),
        sa.Column("excerpt", sa.Text(), nullable=False),
        sa.CheckConstraint("rank >= 1", name="ck_evidence_pack_span_rank"),
        sa.UniqueConstraint("evidence_pack_id", "source_span_id", name="uq_evidence_pack_span"),
    )

    op.create_table(
        "question_candidates",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("tenant_id", uuid, sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("course_id", uuid, sa.ForeignKey("courses.id", ondelete="CASCADE"), nullable=False),
        sa.Column("question_spec_id", uuid, sa.ForeignKey("question_specs.id", ondelete="CASCADE"), nullable=False),
        sa.Column("evidence_pack_id", uuid, sa.ForeignKey("evidence_packs.id"), nullable=False),
        sa.Column("candidate_key", sa.String(160), nullable=False),
        sa.Column("format", sa.String(64), nullable=False),
        sa.Column("content", jsonb, nullable=False),
        sa.Column("generator_metadata", jsonb, server_default=sa.text("'{}'::jsonb"), nullable=False),
        sa.Column("state", sa.String(32), server_default="candidate", nullable=False),
        sa.Column("content_checksum", sa.String(64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint(
            "state IN ('candidate', 'validator_passed', 'expert_reviewed', 'approved', 'published', 'rejected', 'retired')",
            name="ck_question_candidate_state",
        ),
        sa.UniqueConstraint("question_spec_id", "candidate_key", name="uq_question_candidate_key"),
        sa.UniqueConstraint("question_spec_id", "content_checksum", name="uq_question_candidate_content"),
    )
    op.create_index("ix_question_candidates_spec_state", "question_candidates", ["question_spec_id", "state"])

    op.create_table(
        "question_concepts",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("tenant_id", uuid, sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("question_candidate_id", uuid, sa.ForeignKey("question_candidates.id", ondelete="CASCADE"), nullable=False),
        sa.Column("concept_id", uuid, sa.ForeignKey("concept_nodes.id"), nullable=False),
        sa.Column("role", sa.String(24), nullable=False),
        sa.CheckConstraint("role IN ('primary', 'prerequisite', 'application')", name="ck_question_concept_role"),
        sa.UniqueConstraint("question_candidate_id", "concept_id", "role", name="uq_question_candidate_concept"),
    )

    op.create_table(
        "item_validations",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("tenant_id", uuid, sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("question_candidate_id", uuid, sa.ForeignKey("question_candidates.id", ondelete="CASCADE"), nullable=False),
        sa.Column("validator_name", sa.String(80), nullable=False),
        sa.Column("validator_version", sa.String(80), nullable=False),
        sa.Column("status", sa.String(16), nullable=False),
        sa.Column("score", sa.Float(), nullable=True),
        sa.Column("findings", jsonb, nullable=False),
        sa.Column("input_checksum", sa.String(64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("status IN ('passed', 'failed', 'warning')", name="ck_item_validation_status"),
        sa.UniqueConstraint("question_candidate_id", "validator_name", "validator_version", "input_checksum", name="uq_item_validation_idempotency"),
    )
    op.create_index("ix_item_validations_candidate", "item_validations", ["question_candidate_id", "status"])

    op.create_table(
        "review_decisions",
        sa.Column("id", uuid, primary_key=True),
        sa.Column("tenant_id", uuid, sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("question_candidate_id", uuid, sa.ForeignKey("question_candidates.id", ondelete="CASCADE"), nullable=False),
        sa.Column("reviewer_id", uuid, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("decision", sa.String(16), nullable=False),
        sa.Column("reason_code", sa.String(80), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("decision IN ('approved', 'rejected', 'needs_revision')", name="ck_review_decision"),
    )

    for table in (
        "question_specs",
        "evidence_packs",
        "evidence_pack_spans",
        "question_candidates",
        "question_concepts",
        "item_validations",
        "review_decisions",
    ):
        _tenant_policy(table)
    _runtime_grants()


def downgrade() -> None:
    for table in (
        "review_decisions",
        "item_validations",
        "question_concepts",
        "question_candidates",
        "evidence_pack_spans",
        "evidence_packs",
        "question_specs",
    ):
        op.execute(f'DROP POLICY IF EXISTS "tenant_isolation_{table}" ON "{table}"')
        op.drop_table(table)
