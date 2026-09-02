# Chiron AI

Chiron AI is an adaptive learning vertical slice for intensive AI and RAG exam preparation. The repository follows the architecture in `IMPLEMENT_PLAN.md`: a Next.js learner experience, a typed FastAPI boundary, worker contracts, content manifests, and evaluation fixtures.

## Included vertical slice

- Cinematic landing and learner dashboard
- Interactive knowledge map with concept provenance
- 5-question demo diagnostic with persistent progress
- Evidence-weighted mastery, auditable NIU priority, and a capacity-bound 3-4 day plan
- Six scenario practice labs with autosave/resume, deterministic transfer checks, evidence, mastery, and study-plan updates
- Versioned essay grading with an outbox worker, SLA escalation, low-confidence human review, and learner/instructor UI
- Grounded tutor and retrieval API contracts
- Tenant-scoped short-term tutor threads and append-only episodic learning events
- Adaptive hybrid retrieval: one-query direct path or multi-query RRF for prerequisite/multi-hop questions
- In-memory and PostgreSQL adaptive repository adapters behind the same contract
- JWT access + rotating refresh sessions through a Next.js BFF with HttpOnly cookies
- Non-owner PostgreSQL runtime role with forced RLS
- Transactional outbox worker with idempotent dense/BM25 Qdrant upserts and essay grading retries
- Active Graph-lite routing gated by development and frozen-holdout retrieval evaluation
- PostgreSQL/Qdrant reconciliation, retention enforcement, worker metrics, and production configuration preflight
- Docker Compose for PostgreSQL, Qdrant, Redis, MinIO, Celery worker, and scheduler

The runtime adapter is intentionally replaceable. PostgreSQL migrations already define durable
mastery, priority snapshots, and study plans; PostgreSQL remains the source of truth while Qdrant
is a rebuildable retrieval index.

## Quick start

```powershell
corepack enable
pnpm install
pnpm dev
```

In a second terminal:

```powershell
cd services/api
uv sync --extra dev
uv run uvicorn app.main:app --reload
```

Open `http://localhost:3000/login` and use `learner@chiron.local` or
`instructor@chiron.local` with the local-only password `chiron-demo-2026`. Protected learner calls
go through same-origin Next.js routes, which keep access/refresh tokens in HttpOnly cookies and add
the bearer access token server-side. There is no unauthenticated learner-data fallback.

## Verification

```powershell
pnpm lint
pnpm typecheck
pnpm build
cd services/api
uv run pytest
uv run ruff check .
```

## LLM resilience checks

The API routes tutor traffic through Qwen, then GPT-OSS inside Groq, and permits Gemini Free only
for public/synthetic traffic. Private traffic degrades to cited retrieval when Groq is unavailable.

```powershell
cd services/api

# Passive /models check; sends no prompt
uv run python scripts/probe_llm.py

# Active synthetic probes; never use learner/course data
uv run python scripts/probe_llm.py --active

# Live fallback and private-data guard
uv run python scripts/e2e_llm.py
```

Circuit/quota state uses Redis when `REDIS_URL` is configured; otherwise development falls back to
in-process memory. See `docs/provider-hardening.md` for routing and failure semantics.

## Production path

Identity/tenancy, JWT-derived learner identity, SQLAlchemy adaptive repositories, transactional
outbox writes, PostgreSQL RLS policies, demo seed, and live readiness probes are implemented. See
`docs/identity-tenancy-persistence.md` for the security boundary, transaction contract, and commands.

The local runtime now uses the non-owner `chiron_runtime` role, the frontend has login/automatic
session refresh/logout, and the Celery outbox consumer upserts stable chunk IDs into Qdrant. See
`docs/runtime-auth-outbox.md` for setup, failure semantics, and verification.

Before a pilot, provision the selected OIDC issuer/client and production secrets, run real-provider
essay calibration, execute the strict production preflight, and repeat the documented backup/rollback
rehearsal inside the deployed environment. Local PostgreSQL/Qdrant reconciliation and Graph-lite
development/holdout gates are already passing. See `docs/DEPLOYMENT_REHEARSAL.md`.
