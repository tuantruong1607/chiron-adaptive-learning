from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

import psycopg

from chiron_worker.config import get_settings
from chiron_worker.graph import GraphStore

REQUIRED_CHECKS = {
    "graph_lite_p95_within_budget",
    "graph_lite_direct_recall_gate",
    "graph_lite_prerequisite_recall_gate",
    "graph_lite_multi_hop_recall_gate",
}

# The first vertical slice used compact concept identifiers. Preserve learner
# evidence and reviewed question coverage when the full taxonomy supersedes it.
LEGACY_CONCEPT_ALIASES = {
    "agent_memory": "agent_memory",
    "answer_relevancy": "answer_relevancy",
    "checkpointing": "durable_execution",
    "chunking": "chunking",
    "citation": "faithfulness_grounding",
    "context_precision": "context_precision_recall",
    "context_recall": "context_precision_recall",
    "dense": "dense_retrieval",
    "embedding": "embeddings",
    "evaluation": "rag_evaluation",
    "faithfulness": "faithfulness_grounding",
    "fallback_chain": "fallback_policy",
    "graph-routing": "graphrag_multi_hop",
    "graphrag": "graphrag_multi_hop",
    "hnsw": "vector_database",
    "human_in_the_loop": "human_in_loop",
    "hybrid_search": "hybrid_search_rrf",
    "llm_agent_orchestration": "agent_architecture",
    "metadata-filtering": "metadata_filtered_search",
    "metadata_filtering": "metadata_filtered_search",
    "multi_hop_retrieval": "graphrag_multi_hop",
    "prompt_injection": "retrieval_prompt_injection",
    "reciprocal_rank_fusion": "hybrid_search_rrf",
    "reranking": "reranking_mmr",
    "rrf": "hybrid_search_rrf",
    "sparse": "sparse_retrieval",
    "state_machine": "agent_architecture",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Activate a reviewed Graph-lite version")
    parser.add_argument("--version", default="course-knowledge-v2")
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument(
        "--spec", type=Path, default=Path("services/api/app/course_taxonomy.json")
    )
    parser.add_argument("--tenant", default="chiron-demo")
    parser.add_argument("--course", default="rag-intensive")
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    if spec.get("version") != args.version:
        raise ValueError("Taxonomy spec targets a different graph version")
    topic_to_concept = {
        topic: node["id"]
        for node in spec["nodes"]
        for topic in node.get("question_topics", [])
    }
    report = json.loads(args.report.read_text(encoding="utf-8"))
    generated_at = datetime.fromisoformat(str(report["generated_at"]))
    if generated_at < datetime.now(UTC) - timedelta(hours=24):
        raise ValueError("Graph activation report is older than 24 hours")
    quality_gate = report.get("quality_gate") or {}
    checks = {str(item["name"]): item for item in quality_gate.get("checks", [])}
    if not quality_gate.get("passed") or not set(checks) >= REQUIRED_CHECKS:
        raise ValueError("Graph quality gate is incomplete or failed")
    if any(not checks[name].get("passed") for name in REQUIRED_CHECKS):
        raise ValueError("A required Graph-lite gate failed")
    if float(checks["graph_lite_direct_recall_gate"]["actual"]) < 0:
        raise ValueError("Direct-fact recall regression blocks activation")
    if float(checks["graph_lite_multi_hop_recall_gate"]["actual"]) < 0:
        raise ValueError("Multi-hop recall regression blocks activation")
    graph_policy = report.get("graph_policy") or {}
    if graph_policy.get("version_status") != "draft" or set(
        graph_policy.get("review_statuses") or []
    ) != {"approved"}:
        raise ValueError("Activation report did not evaluate the approved draft graph")

    settings = get_settings()
    database_url = (settings.operations_database_url or settings.database_url).replace(
        "postgresql+psycopg://", "postgresql://", 1
    )
    with psycopg.connect(database_url) as connection:
        tenant_row = connection.execute(
            "SELECT id::text FROM tenants WHERE slug=%s", (args.tenant,)
        ).fetchone()
        if tenant_row is None:
            raise LookupError(f"Unknown tenant: {args.tenant}")
        tenant_id = str(tenant_row[0])
        connection.execute("SELECT set_config('app.tenant_id', %s, false)", (tenant_id,))
        row = connection.execute(
            """
            SELECT g.id::text, g.status, c.id::text
            FROM graph_versions g JOIN courses c ON c.id=g.course_id
            WHERE g.tenant_id=%s AND c.slug=%s AND g.version=%s
            FOR UPDATE
            """,
            (tenant_id, args.course, args.version),
        ).fetchone()
        if row is None:
            raise LookupError(f"Unknown graph version: {args.version}")
        graph_id, graph_status, course_id = map(str, row)
        if graph_status != "draft":
            raise ValueError("Only a draft graph may be activated")
        counts = connection.execute(
            """
            SELECT
              (SELECT count(*) FROM concept_nodes WHERE tenant_id=%s AND graph_version_id=%s),
              (SELECT count(*) FROM concept_edges WHERE tenant_id=%s AND graph_version_id=%s),
              (SELECT count(*) FROM chunk_concepts WHERE tenant_id=%s AND graph_version_id=%s),
              (SELECT count(*) FROM concept_nodes WHERE tenant_id=%s AND graph_version_id=%s
                 AND (review_status<>'approved' OR evidence_source_span_id IS NULL)),
              (SELECT count(*) FROM concept_edges WHERE tenant_id=%s AND graph_version_id=%s
                 AND (review_status<>'approved' OR evidence_source_span_id IS NULL)),
              (SELECT count(*) FROM chunk_concepts WHERE tenant_id=%s AND graph_version_id=%s
                 AND review_status<>'approved')
            """,
            (tenant_id, graph_id) * 6,
        ).fetchone()
        expected_nodes = len(spec["nodes"])
        expected_edges = len(spec["edges"])
        links_are_complete = expected_nodes <= counts[2] <= expected_nodes * 3
        if tuple(counts[:2]) != (expected_nodes, expected_edges) or not links_are_complete or any(counts[3:]):
            raise ValueError(f"Graph review/provenance gate failed: counts={counts}")
        cycles = GraphStore(settings.operations_database_url or settings.database_url).prerequisite_cycles(
            tenant_id=tenant_id,
            course_id=course_id,
            review_statuses=("approved",),
            graph_version_status="draft",
        )
        if cycles:
            raise ValueError(f"Prerequisite graph contains cycles: {cycles}")
        previous_versions = [
            str(item[0])
            for item in connection.execute(
                "SELECT version FROM graph_versions WHERE tenant_id=%s AND course_id=%s "
                "AND status='active' AND id<>%s FOR UPDATE",
                (tenant_id, course_id, graph_id),
            ).fetchall()
        ]
        migrated_mastery = connection.execute(
            """
            INSERT INTO mastery_states (
              id, tenant_id, learner_id, concept_id, self_confidence,
              diagnostic_status, mastery, evidence_confidence, confidence_gap,
              misconception, evidence_ids, engine_version, updated_at
            )
            SELECT DISTINCT ON (old_state.tenant_id, old_state.learner_id, new_node.id)
                   gen_random_uuid(), old_state.tenant_id, old_state.learner_id,
                   new_node.id, old_state.self_confidence, old_state.diagnostic_status,
                   old_state.mastery, old_state.evidence_confidence,
                   old_state.confidence_gap, old_state.misconception,
                   old_state.evidence_ids, old_state.engine_version, now()
            FROM mastery_states old_state
            JOIN concept_nodes old_node ON old_node.id=old_state.concept_id
            JOIN concept_nodes new_node
              ON new_node.tenant_id=old_node.tenant_id
             AND new_node.graph_version_id=%s
             AND new_node.normalized_name=(
               CASE old_node.normalized_name
                 WHEN 'citation' THEN 'faithfulness_grounding'
                 WHEN 'context_precision' THEN 'context_precision_recall'
                 WHEN 'context_recall' THEN 'context_precision_recall'
                 WHEN 'dense' THEN 'dense_retrieval'
                 WHEN 'embedding' THEN 'embeddings'
                 WHEN 'evaluation' THEN 'rag_evaluation'
                 WHEN 'faithfulness' THEN 'faithfulness_grounding'
                 WHEN 'fallback_chain' THEN 'fallback_policy'
                 WHEN 'graph-routing' THEN 'graphrag_multi_hop'
                 WHEN 'graphrag' THEN 'graphrag_multi_hop'
                 WHEN 'hnsw' THEN 'vector_database'
                 WHEN 'human_in_the_loop' THEN 'human_in_loop'
                 WHEN 'hybrid_search' THEN 'hybrid_search_rrf'
                 WHEN 'llm_agent_orchestration' THEN 'agent_architecture'
                 WHEN 'metadata-filtering' THEN 'metadata_filtered_search'
                 WHEN 'metadata_filtering' THEN 'metadata_filtered_search'
                 WHEN 'multi_hop_retrieval' THEN 'graphrag_multi_hop'
                 WHEN 'prompt_injection' THEN 'retrieval_prompt_injection'
                 WHEN 'reciprocal_rank_fusion' THEN 'hybrid_search_rrf'
                 WHEN 'reranking' THEN 'reranking_mmr'
                 WHEN 'rrf' THEN 'hybrid_search_rrf'
                 WHEN 'sparse' THEN 'sparse_retrieval'
                 WHEN 'state_machine' THEN 'agent_architecture'
                 ELSE old_node.normalized_name
               END
             )
            WHERE old_state.tenant_id=%s
              AND old_node.graph_version_id<>%s
            ORDER BY old_state.tenant_id, old_state.learner_id, new_node.id,
                     old_state.mastery DESC NULLS LAST, old_state.updated_at DESC
            ON CONFLICT (tenant_id, learner_id, concept_id) DO UPDATE SET
              self_confidence=excluded.self_confidence,
              diagnostic_status=excluded.diagnostic_status,
              mastery=excluded.mastery,
              evidence_confidence=excluded.evidence_confidence,
              confidence_gap=excluded.confidence_gap,
              misconception=excluded.misconception,
              evidence_ids=excluded.evidence_ids,
              engine_version=excluded.engine_version,
              updated_at=now()
            """,
            (graph_id, tenant_id, graph_id),
        ).rowcount
        remapped_questions = 0
        for topic, concept_slug in topic_to_concept.items():
            remapped_questions += connection.execute(
                """
                UPDATE question_concepts qc
                SET concept_id=new_node.id
                FROM question_candidates candidate
                JOIN question_specs spec ON spec.id=candidate.question_spec_id
                JOIN concept_nodes new_node
                  ON new_node.tenant_id=candidate.tenant_id
                 AND new_node.graph_version_id=%s
                 AND new_node.normalized_name=%s
                WHERE qc.tenant_id=%s
                  AND qc.question_candidate_id=candidate.id
                  AND spec.concept_slugs ? %s
                """,
                (graph_id, concept_slug, tenant_id, topic),
            ).rowcount
            remapped_questions += connection.execute(
                """
                INSERT INTO question_concepts (
                  id, tenant_id, question_candidate_id, concept_id, role
                )
                SELECT gen_random_uuid(), candidate.tenant_id, candidate.id,
                       new_node.id, 'primary'
                FROM question_candidates candidate
                JOIN question_specs spec ON spec.id=candidate.question_spec_id
                JOIN concept_nodes new_node
                  ON new_node.tenant_id=candidate.tenant_id
                 AND new_node.graph_version_id=%s
                 AND new_node.normalized_name=%s
                WHERE candidate.tenant_id=%s
                  AND spec.concept_slugs ? %s
                ON CONFLICT (question_candidate_id, concept_id, role) DO NOTHING
                """,
                (graph_id, concept_slug, tenant_id, topic),
            ).rowcount
        missing_question_links = connection.execute(
            """
            SELECT count(*)
            FROM question_candidates candidate
            WHERE candidate.tenant_id=%s AND candidate.course_id=%s
              AND NOT EXISTS (
                SELECT 1 FROM question_concepts qc
                JOIN concept_nodes node ON node.id=qc.concept_id
                WHERE qc.question_candidate_id=candidate.id
                  AND node.graph_version_id=%s
              )
            """,
            (tenant_id, course_id, graph_id),
        ).fetchone()[0]
        if missing_question_links:
            raise ValueError(
                f"Question-concept coverage gate failed: missing={missing_question_links}"
            )
        connection.execute(
            "UPDATE graph_versions SET status='superseded', updated_at=now() "
            "WHERE tenant_id=%s AND course_id=%s AND status='active' AND id<>%s",
            (tenant_id, course_id, graph_id),
        )
        for table in ("concept_nodes", "concept_edges", "chunk_concepts"):
            connection.execute(
                f"UPDATE {table} SET review_status='active', updated_at=now() "
                "WHERE tenant_id=%s AND graph_version_id=%s AND review_status='approved'",
                (tenant_id, graph_id),
            )
        connection.execute(
            "UPDATE graph_versions SET status='active', updated_at=now() "
            "WHERE tenant_id=%s AND id=%s",
            (tenant_id, graph_id),
        )
        connection.commit()

    print(
        json.dumps(
            {
                "status": "activated",
                "graph_version": args.version,
                "previous_versions": previous_versions,
                "nodes": counts[0],
                "edges": counts[1],
                "chunk_links": counts[2],
                "mastery_rows_migrated": migrated_mastery,
                "question_links_remapped": remapped_questions,
                "question_links_missing": missing_question_links,
                "quality_report": str(args.report),
                "prerequisite_cycles": cycles,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
