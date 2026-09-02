# Chiron vertical-slice architecture

The implemented slice preserves production boundaries while remaining easy to run locally.

```text
Next.js UI -> Next server routes -> FastAPI -> repository boundary
                                          -> deterministic adaptive core
                                             -> evidence -> mastery
                                             -> Need/Importance/Urgency
                                             -> capacity-bound 3-4 day planner
                                          -> PostgreSQL target
                                          -> transactional outbox -> Celery -> Qdrant
                                          -> LLM router -> Groq / Gemini (policy gated)
```

## Invariants

- PostgreSQL is the canonical business store. Qdrant points are rebuildable.
- Question keys and hidden rubric data never cross the server boundary before submission.
- Every concept includes source provenance.
- Graph expansion is intent-routed, relation-limited, and at most two hops.
- Diagnostic and evidence mutations accept idempotency keys.
- Lab scores come from deterministic rubric rules.
- Self-report is a need signal, never fabricated measured mastery.
- Mastery changes only from versioned evidence with an explicit confidence.
- Priority and planning are deterministic, versioned, and return component scores/reasons.
- The in-memory adapter is for deterministic tests/offline development; development with a configured
  database defaults to the PostgreSQL adapter.
- Learner and tenant identity come only from a verified access token, never a request learner field.
- Every PostgreSQL adaptive mutation, snapshot, plan, and outbox event commits atomically.
- Private learner data never falls back to Gemini Free. Without a local-model deployment,
  provider outages degrade to cited retrieval or durable async work rather than unsafe egress.

The detailed LLM resilience design is documented in
[`provider-hardening.md`](./provider-hardening.md).

## Persistence and delivery status

Identity/membership/enrollment, forced RLS, a non-owner runtime role, tenant-scoped SQLAlchemy
repositories, atomic adaptive transactions, replay-safe idempotency, rotating refresh sessions, real
readiness probes, and idempotent outbox-to-Qdrant synchronization are implemented. Details are in
[`identity-tenancy-persistence.md`](./identity-tenancy-persistence.md) and
[`runtime-auth-outbox.md`](./runtime-auth-outbox.md).

Next: ingest one real PDF and HTML document, implement hybrid retrieval/reranking over the synced
collection, add periodic PostgreSQL/Qdrant reconciliation, and move credential authentication to the
selected production OIDC issuer.

The Fidea distillation mapping and rejected legacy infrastructure are recorded in
[`adr/0007-distill-fidea-adaptive-core.md`](./adr/0007-distill-fidea-adaptive-core.md).
