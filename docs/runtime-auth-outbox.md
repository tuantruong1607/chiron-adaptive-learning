# Runtime role, web session, and vector outbox

Implemented and exercised locally on 2026-08-30.

## 1. PostgreSQL privilege split

Use the owner connection only for Alembic and role provisioning:

```shell
cd services/api
uv run alembic upgrade head
uv run python scripts/provision_runtime_role.py
```

`DATABASE_ADMIN_URL` owns schema objects. `DATABASE_URL` and `WORKER_DATABASE_URL` use
`chiron_runtime`, which is `NOSUPERUSER`, `NOBYPASSRLS`, `NOCREATEDB`, `NOCREATEROLE`, and
not an object owner. The provisioning command is idempotent and grants only DML/sequence/schema usage.

Every tenant transaction must set `app.tenant_id` transaction-locally. Repository predicates remain
mandatory even though RLS is the final database enforcement layer.

## 2. Browser session flow

```text
login form
  -> POST same-origin /api/auth/login
  -> Next BFF calls FastAPI /api/v1/auth/token
  -> HttpOnly access + refresh cookies
  -> learner request enters a same-origin Next route
  -> BFF adds Authorization: Bearer <access>
  -> 401: rotate refresh token once, replace both cookies, retry once
  -> logout: revoke refresh session and clear cookies
```

The browser never receives a JavaScript-readable bearer token. Mutation routes enforce same-origin
requests. Refresh rows store only a token hash and are tenant-scoped by RLS. Rotation is one-time:
the old refresh token immediately returns 401.

The in-process single-flight map prevents concurrent refresh rotation inside one Next instance. A
multi-instance deployment still needs a Redis-distributed lock or a short backend rotation grace
window keyed by refresh family.

## 3. Transactional outbox to Qdrant

`chiron.drain_outbox` runs every `OUTBOX_POLL_SECONDS`:

1. Enumerate active tenant IDs.
2. Open one tenant-scoped runtime-role transaction.
3. Recover expired `processing` leases.
4. Claim due `chunks.sync_requested` rows using `FOR UPDATE SKIP LOCKED`.
5. Commit the lease before external I/O.
6. Load authoritative chunks from PostgreSQL under the same tenant context.
7. Create local dense and BM25 sparse vectors.
8. Upsert to Qdrant with `wait=true` and point ID equal to the stable chunk UUID.
9. Mark the outbox row `processed`; on failure, retain it with exponential backoff.

The Qdrant payload includes `tenant_id`, `course_id`, `document_version_id`, `source_span_id`,
`checksum`, `embedding_version`, `is_active`, and content. Stable IDs make retry/replay
idempotent. After `OUTBOX_MAX_ATTEMPTS`, events become `dead` for reviewed operator action.

Worker and scheduler containers run as UID/GID 10001. The embedding cache is a persistent named
volume mounted under that user's home. PostgreSQL remains canonical; Qdrant can be rebuilt.

## 4. Local run and verification

```shell
docker compose up -d postgres redis qdrant minio

cd services/api
uv run alembic upgrade head
uv run python scripts/provision_runtime_role.py
uv run python scripts/seed_demo.py

cd ../..
docker compose up -d --build worker scheduler
docker compose ps
```

Expected checks:

- `provision_runtime_role.py` reports every privileged role flag as `False`.
- Direct runtime-role queries without `app.tenant_id` see no tenant-owned learner rows.
- Login returns a pair, refresh invalidates the old refresh token, and logout revokes the new one.
- A seeded `chunks.sync_requested` row becomes `processed`.
- `chiron_chunks_v1` contains one stable demo point; replay does not increase the point count.
- Worker logs contain no Celery root-user warning.

## 5. Known operational gaps

- `verify_enriched_index.py` now detects both Qdrant orphans and active PostgreSQL chunks missing
  from Qdrant; `replay_dead_letters.py` provides reviewed replay by explicit event ID.
- API `/metrics` exposes request, retrieval, LLM, grading queue and PostgreSQL outbox counters;
  worker claim duration/vector latency/cache-warmup histograms still need a Prometheus exporter.
- Pin/model-version the exact ONNX artifact in addition to the logical embedding version.
- Add Redis-backed refresh serialization before horizontally scaling Next.js.
- Replace local credentials with production OIDC and add auth audit events.
