# Deployment, backup and rollback rehearsal

Run rehearsals against a disposable database and Qdrant collection. Never downgrade the canonical
database to prove rollback.

## PostgreSQL

1. Create a custom-format backup with `pg_dump -Fc` and record its SHA-256 checksum.
2. Restore into a uniquely named rehearsal database.
3. Compare tenant, course, active child chunk, graph and outbox counts with the source database.
4. Run `alembic downgrade 0009_question_bank_p0` and `alembic upgrade head` against the restored
   database, then rerun integration contracts.
5. Drop only the explicitly named rehearsal database after evidence has been recorded.

## Qdrant

1. Create and download a snapshot of the active collection.
2. Restore it into a clean temporary Qdrant instance or uniquely named rehearsal collection.
3. Run `verify_enriched_index.py` against the restored collection and compare point count and
   collection vector configuration.
4. Keep `QDRANT_COLLECTION` pointing at the old collection until the restored candidate passes
   reconciliation and retrieval smoke tests. Rollback is the environment-variable switch back to
   the previous immutable collection name.

## Application cutover

Before cutover, `/readyz`, login/OIDC, retrieval, tutor, essay queue, worker metrics and API metrics
must pass. Graph-lite remains disabled unless its fresh quality report passes every gate and direct
retrieval does not regress. Record image digests and previous environment values so code rollback is
a redeploy of the previous digest, not a rebuild from a mutable tag.

## Production configuration preflight

Before deploying, load the API, worker and web environment values into the same shell and run:

```powershell
cd services/api
uv run python scripts/production_preflight.py --strict
```

The command never prints secret values. It blocks placeholder credentials, local-only auth,
missing OIDC endpoints/client values, mock grading, unsafe private fallback, disabled retention,
an inactive approved Graph-lite gate and missing operations tokens. A pass confirms configuration
shape only. The live issuer discovery, provider calibration run and deployment smoke tests still
need to execute inside the target environment.

## Latest local rehearsal evidence — 2026-08-31

- PostgreSQL custom-format dump SHA-256:
  `7900ed01d5565f745afd7cffd5f4db8590b9f50d7579bccab06f369c286f09eb`.
- Disposable restore counts before and after the migration round trip:
  `1 tenant, 1 course, 5,070 active child chunks, 2 graph versions, 305 outbox events`.
- Alembic downgrade `0010_operations_retention -> 0009_question_bank_p0` and upgrade back to head
  both passed on the restored database. The rehearsal database and temporary dump were removed.
- Qdrant snapshot:
  `chiron_chunks_v1-4442277336304345-2026-08-31-15-10-19.snapshot`, size `84,947,456` bytes,
  SHA-256 `e8a754e7497f522da81629462496a6fae9d19b50b2398dc76cfd81647cd977ea`.
- The snapshot restored into a disposable collection with status `green`; full reconciliation
  matched `5,070/5,070` PostgreSQL child chunks with zero violations. The disposable collection was
  removed; the verified source snapshot remains available for rollback rehearsal.

When overriding a database for an Alembic rehearsal, set both `DATABASE_URL` and
`DATABASE_ADMIN_URL` to a `postgresql+psycopg://` URL. Alembic intentionally prefers the admin URL.
