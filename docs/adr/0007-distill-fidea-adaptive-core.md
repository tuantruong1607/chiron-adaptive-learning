# ADR-007: Distill Fidea adaptive techniques into Chiron

- Status: accepted and core implemented
- Date: 2026-08-30
- Owners: Chiron architecture

## Context

Fidea contains mature deterministic logic for diagnostic evidence, learner knowledge state,
Need-Importance-Urgency priority, and capacity-aware planning. Its infrastructure is not a fit for
Chiron: it couples runtime to NVIDIA NIM, uses dense-only pgvector retrieval, mixes legacy LangGraph
with the newer deterministic diagnostic, and upgrades schema with `create_all`/runtime `ALTER`.

Chiron already owns the broader product boundaries: PostgreSQL canonical data, a rebuildable Qdrant
hybrid index, typed/provenance graph-lite, worker/outbox contracts, and policy-gated Groq/Gemini
routing.

## Decision

Keep Chiron as the platform and reimplement only Fidea's proven adaptive techniques as pure,
deterministic domain code. Do not copy the Fidea repository or infrastructure wholesale.

| Fidea capability | Chiron implementation |
|---|---|
| Knowledge State status/null coherence | `app/adaptive/contracts.py`, migration 0002 |
| Evidence reliability and mastery update | `app/adaptive/mastery.py` |
| Need-Importance-Urgency ranking | `app/adaptive/priority.py` |
| Prerequisite/capacity planner | `app/adaptive/planner.py` |
| Runtime diagnostic integration | `app/repository.py` and `/diagnostic/submit` |
| Learner-state inspection | `/learning-state` |
| Auditable 3-4 day plan | `/study-plan?horizon_days=3|4&daily_minutes=...` |

The domain core must remain independent of LLM providers, vector stores, FastAPI, and SQLAlchemy.
Self-assessment may influence need but cannot produce numeric mastery. Missing evidence remains
missing. Every priority decision exposes need, importance, urgency, reliability, reasons, and an
engine version. Every plan exposes scheduled and deferred work under a declared capacity.

## Alternatives rejected

1. Merge Fidea backend into Chiron: rejected because it creates two persistence models, two RAG
   stacks, and overlapping legacy/new diagnostic paths.
2. Use LangGraph for mastery, ranking, and scheduling: rejected because these decisions must be
   reproducible, cheap, and straightforward to audit.
3. Let the LLM directly generate the learning plan: rejected because capacity, prerequisite, and
   deadline constraints require deterministic enforcement.
4. Keep the former `mastery - exam_weight` demo sort: rejected because it omits evidence reliability
   and urgency and cannot explain the recommendation.

## Consequences

- Chiron gains an end-to-end diagnostic -> evidence -> mastery -> priority -> plan loop without a
  new provider dependency.
- The API can run deterministic tests with the in-memory adapter and uses PostgreSQL by default in
  development when `DATABASE_URL` is configured.
- Migration 0003 and the SQLAlchemy service add identity/tenant context, RLS, durable adaptive state,
  restart-safe idempotency, and an atomic transactional outbox write.
- Qdrant retrieval and knowledge graph extraction remain separate work and do not participate in
  mastery updates without a scored evidence event.

## Verification evidence

- Unit tests lock no-fabricated-mastery, evidence confidence, NIU ordering, prerequisite ordering,
  and capacity deferral.
- API tests lock token-derived learner identity, idempotency, learning-state output,
  self-assessment semantics, and plan audit fields.
- A shared adapter contract passes for memory and PostgreSQL; integration tests cover concurrent
  idempotency, restart replay, rollback, and tenant denial.
- Alembic 0001 -> 0003 was applied successfully to the local PostgreSQL 17 Compose service.

## Rollback

The API adapter can revert to the prior repository behavior while retaining migration 0002 unused.
Database rollback is `alembic downgrade 0001_vertical_slice`; it removes adaptive snapshots and must
only be run after exporting learner evidence/state.
