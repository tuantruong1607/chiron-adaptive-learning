# Operations rehearsal — 2026-08-31

## Result

PASS on the local deployment topology.

- PostgreSQL source schema: `0009_question_bank_p0`; restored copy upgraded to
  `0010_operations_retention`, downgraded to `0009_question_bank_p0`, then upgraded again.
- Restored PostgreSQL counts: 1 tenant, 1 course, 5,070 active child chunks, 42 concept nodes,
  38 concept edges and 102 chunk links.
- Retention rehearsal: dry-run selected one synthetic old attempt; apply redacted its learner
  submission and wrote one immutable retention-run record.
- Qdrant snapshot restored into a clean temporary Qdrant 1.15.1 instance: 5,070/5,070 points,
  5,070 PostgreSQL matches and zero reconciliation violations.
- Temporary restore database, container and volume were removed after verification. The backup
  artifacts below remain recoverable.

## Backup artifacts

- `chiron-pre-0010.dump`: 6,457,240 bytes; SHA-256
  `3E24610C4AE1C54D6C8BB8E24340A26EDF29B18D2722B3182FFA5C20F62F37C4`
- `chiron_chunks_v1.snapshot`: 84,947,456 bytes; SHA-256
  `7F8B6531B495458B44ACB16CF5CC473614ACBECFC4482811EFFE4B0A9C3C64E8`

## Deployment smoke

- `/readyz`: ready for PostgreSQL, Redis and Qdrant.
- Worker Prometheus exporter: available on port 9108.
- Graph-lite development gate: PASS, 35 cases, P95 423.8 ms, no recall regression.
- Graph-lite holdout gate: PASS, 15 cases, P95 448.4 ms, no recall regression.
- Active graph: 34 nodes, 29 edges, 102 chunk links, zero prerequisite cycles.
- Authenticated multi-hop retrieval: `graph_lite_2hop`, 8 hits.

OIDC code supports issuer discovery/JWKS and web Authorization Code with PKCE. A live issuer was not
configured in this environment, so deploy authentication remains `local` until issuer/client values
and the required Chiron UUID/role claims are provisioned.
