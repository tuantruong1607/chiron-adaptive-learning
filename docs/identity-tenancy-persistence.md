# Identity, tenancy, persistence, and readiness

Implemented on 2026-08-30 for the Chiron adaptive-learning vertical slice.

## Trust boundary

`POST /api/v1/auth/token` authenticates a user inside a tenant membership and returns a short-lived
signed access JWT plus an opaque rotating refresh token. Refresh secrets are stored only as SHA-256
hashes; rotation locks and revokes the old session in the same transaction. Learner endpoints derive
both `user_id` (`sub`) and `tenant_id` (`tid`) from the access token. Diagnostic payloads forbid
extra fields, so a client cannot submit an arbitrary `learner_id`.

The demo auth implementation is deliberately behind the API boundary. It can later be replaced by a
managed OIDC/Supabase issuer without changing adaptive domain services: only token verification and
claim mapping need to change.

## Tenant isolation

Migration `0003_identity_tenancy` adds `tenants`, `users`, `memberships`, and
`course_enrollments`, adds foreign keys for learner state, and enables/forces PostgreSQL RLS on every
tenant-owned table. Each transaction runs:

```sql
SELECT set_config('app.tenant_id', :tenant_id, true);
```

RLS policies require row `tenant_id` to match that transaction-local value for both reads and writes.
Repositories also include explicit tenant predicates. Migrations use `DATABASE_ADMIN_URL`; API and
worker use `DATABASE_URL`/`WORKER_DATABASE_URL` with the provisioned `chiron_runtime` role. That
role has `NOSUPERUSER`, `NOBYPASSRLS`, `NOCREATEDB`, `NOCREATEROLE`, and does not own the tables,
so RLS is an independent enforcement boundary rather than a configured-but-bypassable policy.

## Atomic diagnostic transaction

```text
authenticate token and require active enrollment
  -> INSERT attempt ON CONFLICT + lock existing idempotency row
  -> grade answers deterministically
  -> INSERT evidence ON CONFLICT DO NOTHING
  -> UPSERT mastery state
  -> create or reuse priority snapshot by checksum
  -> create or reuse study plan by checksum
  -> INSERT transactional outbox event
  -> mark attempt completed with replayable result
  -> COMMIT
```

The unique `(tenant_id, learner_id, idempotency_key)` attempt constraint is the concurrency gate.
Replays return the serialized completed result from PostgreSQL, including after an API restart. A
different request body with the same key is rejected. Any exception before commit rolls back the
attempt, evidence, mastery, snapshots, plan, and outbox together.

The implemented repository classes are `AttemptRepository`, `EvidenceRepository`,
`MasteryStateRepository`, `PrioritySnapshotRepository`, and `StudyPlanRepository`. The deterministic
adaptive domain remains independent from SQLAlchemy. Memory and PostgreSQL services run the same
contract test; PostgreSQL-only tests additionally cover concurrent replay, process restart, rollback,
and cross-tenant denial.

## Readiness semantics

`GET /readyz` uses bounded live probes:

- PostgreSQL: `SELECT 1`.
- Redis: `PING`.
- Qdrant: `GET /collections` with API key when configured.
- LLM: reads the configured route and Redis/in-memory circuit/probe state only; it never sends a
  prompt. An unprobed route is reported as `configured-unprobed` and does not make infrastructure
  readiness fail.

PostgreSQL, Redis, and Qdrant errors/timeouts return HTTP 503. Responses use `Cache-Control: no-store`
and expose exception class/status only, never credentials.

## Local commands

From `services/api`:

```shell
uv run alembic upgrade head
uv run python scripts/provision_runtime_role.py
uv run python scripts/seed_demo.py
uv run uvicorn app.main:app --reload
uv run pytest
```

The idempotent seed creates tenant `chiron-demo`, learner `learner@chiron.local`, instructor
`instructor@chiron.local`, and course `rag-intensive`. Both local demo accounts use password
`chiron-demo-2026`; rotate/remove them outside local development.

To include the PostgreSQL adapter contract suite, set `CHIRON_INTEGRATION_DATABASE_URL` to the local
test database URL before running pytest. The normal suite uses the memory adapter and does not require
Docker.

## Implemented delivery boundary

- Next.js stores access and refresh tokens only in `HttpOnly`, `SameSite=Lax` cookies and attaches
  the bearer access token inside server routes. A 401 triggers one refresh-and-retry.
- Celery polls the transactional outbox, claims rows with `FOR UPDATE SKIP LOCKED`, recovers stale
  leases, and marks success only after Qdrant acknowledges a `wait=true` upsert.
- Qdrant point IDs are stable chunk UUIDs. Replays overwrite the same point and include tenant,
  course, source, checksum, active status, content, and embedding version.

## Remaining production work

1. Replace local credential auth with the selected OIDC issuer; add refresh-family replay detection,
   account recovery, email verification, and security audit events.
2. Add a periodic reconciliation command comparing active PostgreSQL chunks with Qdrant points and a
   reviewed dead-letter replay workflow.
3. Add multi-instance refresh serialization (Redis lock or backend grace window); the current
   single-flight guard is per Next.js process.
4. Add audit logs and retention/redaction policies.
