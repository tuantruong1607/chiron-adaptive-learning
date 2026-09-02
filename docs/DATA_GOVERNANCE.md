# Learner data governance

This policy is required before a production pilot. It separates private learner work from
public/synthetic corpus data and keeps provider traces minimal.

## Data classes

- `private`: essay answers, learner identity, mastery, evidence and tutor conversation content.
- `public`: reviewed course source spans and published graph metadata.
- `synthetic`: seeded demo data and provider probe prompts.
- `restricted`: secrets, credentials and security-sensitive operational data.

Private or restricted data must not be sent to Gemini or any provider route whose policy does
not explicitly allow it. Essay grading uses the rubric version in the durable outbox payload;
the answer is not copied into application logs or metrics labels.

## Audit and retention

- Keep immutable attempt/evidence/audit metadata for the configured pilot retention window.
- Keep learner answer content only for the active retention window; deletion must remove the
  attempt payload, related evidence and learning events for the same tenant/learner scope.
- Redact provider request/response bodies from logs. Retain provider, model, rubric version,
  confidence, decision status, request ID and timestamps instead.
- Any manual dead-letter replay requires an event ID and a human-readable reason. Use
  `services/worker/scripts/replay_dead_letters.py` with an operations database credential.
- Retention deletion and export must be tenant-scoped, reviewed, logged and rehearsed against
  a backup before enabling it in production.

## Required production settings

`WORKER_INTERNAL_TOKEN` protects the API grading callback and `OPS_METRICS_TOKEN` protects
operational metrics. Production startup rejects either setting when it is missing.

## Enforcement

The worker runs `chiron.enforce_retention` on the configured schedule. It is disabled and
read-only by default. Production must set `RETENTION_ENABLED=true`, first run with
`RETENTION_DRY_RUN=true`, review the table counts, and then set `RETENTION_DRY_RUN=false`.

The enforcement job:

- redacts learner-authored chat, attempt and learning-event payload fields after the learner
  content window;
- redacts processed outbox payloads after the operations window;
- removes expired or long-revoked refresh sessions after the grace window;
- writes one immutable `data_retention_runs` record per tenant and run.

Use `python services/worker/scripts/enforce_retention.py` for a read-only report. Applying changes
requires the explicit `--apply` flag and an operations database role with the required update/delete
privileges. Qdrant stores course evidence, not learner answers, so learner-content retention does not
delete canonical course vectors.

## OIDC boundary

`AUTH_MODE=oidc` disables local password and refresh-token endpoints. The API validates issuer,
audience, expiry and signature through OIDC discovery/JWKS. The IdP must issue UUID claims configured
by `OIDC_USER_ID_CLAIM` and `OIDC_TENANT_ID_CLAIM`, plus a role claim containing `learner`,
`instructor` or `admin`. The web application uses Authorization Code with PKCE; `hybrid` mode keeps
the local login form available only for a controlled migration period.
