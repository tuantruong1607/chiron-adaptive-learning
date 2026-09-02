# Chiron LLM provider hardening architecture

Status: **Core runtime implemented**  
Decision: **No Ollama/self-hosted LLM in deployment** because of infrastructure limits.

Implemented now:

- Typed workload model registry and Qwen -> GPT-OSS -> Gemini route ladder.
- Server-enforced production default of `private` for the current tutor endpoint.
- Normalized failure kinds, usage and rate-limit headers.
- In-memory state plus Redis-backed distributed circuit/quota state when `REDIS_URL` is present.
- Passive/active model probes and optional startup probing.
- Tutor grounded degraded mode with citations.
- Unit/integration/live synthetic verification scripts.

Pending until the corresponding product modules exist:

- Course visibility/tenant policy lookup instead of the current production-safe `private` default.
- Durable `PENDING_AI_GRADING` and extraction retry jobs when essay/ingestion persistence lands.
- Authenticated quota/circuit operations dashboard.

## 1. Goals and constraints

This design keeps Chiron usable when an LLM model is rate-limited, removed or temporarily
unavailable, while preventing private learner data from crossing an unapproved provider boundary.

Goals:

- Detect unavailable/deprecated models before they break learner flows.
- Use per-model quota information rather than waiting blindly for `429`.
- Stop repeated calls to failing models with a distributed circuit breaker.
- Fall back from Qwen Preview to production GPT-OSS models inside Groq.
- Use Gemini Free only for `public` and `synthetic` workloads.
- Preserve learner work through grounded degraded responses and durable queues.
- Reuse FastAPI, Redis, PostgreSQL and the existing worker; add no LLM microservice.

Non-goals:

- Hosting Ollama or another local generative model.
- Sending private essays, learner profiles or private course material to Gemini Free.
- Using LangGraph for a deterministic provider fallback chain.
- Retrying indefinitely or hiding authentication/schema bugs behind another provider.

## 2. Runtime architecture

```text
Next.js
  -> FastAPI endpoint
       -> RequestPolicyClassifier
            workload + server-owned data sensitivity + priority
       -> LLMOrchestrator
            -> ModelRegistry
            -> AvailabilityRegistry ---- Redis TTL state
            -> QuotaTracker ----------- Redis quota snapshots
            -> CircuitBreaker --------- Redis circuit state
            -> RoutePlanner
                 -> GroqAdapter
                 -> GeminiAdapter (public/synthetic only)
            -> DegradedModeService
       -> PostgreSQL audit metadata / durable job state
       -> Celery worker for extraction, grading and retry jobs
```

The implementation stays as modules inside the API/worker codebase. Redis is shared ephemeral
coordination; PostgreSQL remains the durable source of truth.

## 3. Core components

### 3.1 RequestPolicyClassifier

The backend, not the browser, determines sensitivity. Client-provided sensitivity is never trusted
as the final policy decision.

Inputs:

- Course/source visibility and ownership.
- Workload type: tutor, extraction, grading or research.
- Presence of learner profile, essay or attempt data.
- Tenant/course policy.

Output contract:

```text
LLMRequestContext
  workload: tutor | extraction | grader | research
  sensitivity: public | synthetic | private | restricted
  priority: interactive | async_high | background
  max_fallbacks: integer
  latency_budget_ms: integer
  trace_id: UUID
```

Rules:

- An essay or learner attempt is always at least `private`.
- Private course source spans make the complete RAG request `private`.
- Only server fixtures/eval prompts are `synthetic`.
- `restricted` never reaches a Free Tier external model.

### 3.2 ModelRegistry

The registry is configuration-driven and separates workload intent from provider model IDs.

| Workload | Primary | Intra-Groq fallback | Cross-provider fallback |
|---|---|---|---|
| Tutor | `qwen/qwen3.8-27b` | `openai/gpt-oss-120b` | `gemini-3.7-flash`, public/synthetic only |
| Extraction | `openai/gpt-oss-20b` | `openai/gpt-oss-120b` | `gemini-3.5-flash-lite`, public/synthetic only |
| Grading | `openai/gpt-oss-120b` | none by default | `gemini-3.7-flash` only for synthetic/public eval |
| Research | `groq/compound-mini` | GPT-OSS plus approved research tool | `gemini-3.7-flash`, public sources only |

Qwen is Preview, so its identifier is never hard-coded in domain services. GPT-OSS is preferred as
the first fallback because model quotas are independent and the request remains inside Groq.

### 3.3 AvailabilityRegistry and probes

Two probe types are used:

1. Passive: query provider `/models`; no prompt or user data leaves the system.
2. Active: send a tiny synthetic prompt to prove the model is callable.

Deployment-friendly schedule:

- Passive probe at process startup, but do not block `/healthz` in development.
- Active probe on deployment, then at most every six hours.
- Immediate re-probe after `404 model_not_found` or after a circuit cooldown.
- In serverless environments, stale-while-revalidate from the next safe request; no dedicated cron
  service is required.

Redis record:

```text
llm:availability:{provider}:{model}
  status = available | degraded | unavailable | unknown
  checked_at
  latency_ms
  last_status_code
  consecutive_failures
  ttl
```

No course content is used in probes.

### 3.4 QuotaTracker

Every adapter returns a normalized result containing provider rate-limit headers:

```text
ProviderCallMetadata
  request_limit
  request_remaining
  token_limit
  token_remaining
  request_reset_at
  token_reset_at
  retry_after_seconds
```

Snapshots are stored with short TTLs in Redis:

```text
llm:quota:{provider}:{model}
```

Routing priorities:

1. Interactive tutor requests.
2. Submitted grading jobs.
3. Learner-triggered extraction/re-index jobs.
4. Background question generation and evaluation.

When remaining quota drops below a configured reserve, background jobs wait instead of consuming
the budget required by interactive learning.

### 3.5 Distributed circuit breaker

Circuit state is per `provider:model`, shared through Redis so multiple API replicas make the same
decision.

```text
CLOSED -- qualifying failures exceed threshold --> OPEN
OPEN -- cooldown expires --> HALF_OPEN
HALF_OPEN -- one probe succeeds --> CLOSED
HALF_OPEN -- probe fails --> OPEN
```

Initial thresholds:

- Three timeout/5xx failures within 30 seconds open the circuit for 60 seconds.
- `429` opens the model route until `retry-after`/reset, but is tracked as quota exhaustion rather
  than provider outage.
- `404 model_not_found` marks the model unavailable for one hour and triggers a probe/alert.
- `401/403` creates a configuration incident; do not automatically fall back and mask a broken key.
- `400` schema/request errors do not open the circuit and do not fall back.
- Safety refusal is final; another provider must not be used to bypass it.

Use an atomic Redis script/transaction for failure counters and half-open probe ownership.

### 3.6 RoutePlanner and fallback budget

The planner filters candidates before making a network request:

1. Candidate supports the workload/capability.
2. Data policy permits the provider.
3. Availability state is not unavailable.
4. Circuit is not open.
5. Quota reserve and latency budget are sufficient.
6. Candidate was not already attempted for this trace.

At most two fallbacks are allowed. A provider/model pair is attempted once, preventing loops.

```text
PUBLIC/SYNTHETIC TUTOR
  Qwen -> GPT-OSS 120B -> Gemini 3.7 -> grounded degraded response

PRIVATE TUTOR
  Qwen -> GPT-OSS 120B -> grounded degraded response

PRIVATE GRADING
  GPT-OSS 120B -> durable PENDING_AI_GRADING job

PUBLIC EXTRACTION
  GPT-OSS 20B -> GPT-OSS 120B -> Gemini 3.5 Flash-Lite -> retry queue

PRIVATE EXTRACTION
  GPT-OSS 20B -> GPT-OSS 120B -> retry queue

RESTRICTED
  deterministic retrieval only or explicit refusal
```

## 4. Degraded modes without Ollama

### Tutor

Return a `degraded` answer containing:

- Top retrieved source excerpts.
- Exact citations/locators.
- Related knowledge-map nodes and prerequisites.
- A transparent message that generative explanation is temporarily unavailable.

Do not synthesize unsupported prose. The learner can still open the correct lesson material.

### Essay grading

The essay is already durably saved before an LLM job starts. If GPT-OSS is unavailable:

- Set status to `PENDING_AI_GRADING`.
- Store an idempotent grading job/outbox event.
- Retry after quota reset with exponential backoff and jitter.
- Never send the private essay to Gemini Free.
- Allow an instructor/manual-review path if the SLA expires.

### Extraction and indexing

Keep the document version in `PROCESSING_RETRY`, persist the failed stage and retry from the last
checkpoint. The active previous version remains queryable until the new version is complete.

### Research

Research accepts public topics only. If Compound and the approved Gemini research adapter are both
unavailable, return `RESEARCH_TEMPORARILY_UNAVAILABLE`; never fabricate fresh external knowledge.

## 5. API and domain contracts

Recommended normalized result:

```text
LLMResult
  content
  provider
  model
  used_fallback
  fallback_reason
  degraded
  trace_id
  usage
  rate_limit_snapshot
```

Recommended domain errors:

```text
LLMQuotaExhausted
LLMUnavailable
LLMModelRemoved
LLMAuthenticationFailure
LLMSchemaFailure
LLMPolicyBlocked
LLMDeadlineExceeded
```

HTTP endpoints expose a stable application error envelope, not provider response bodies.

## 6. Observability and privacy

Record:

- Provider/model/workload/sensitivity class.
- Latency, status, token usage and rate-limit snapshot.
- Circuit transition and fallback reason.
- Queue age and degraded-mode count.
- Trace/request IDs.

Never record API keys, raw essays, raw private prompts or full retrieved private context in logs.
Provider payload tracing is disabled or redacted by default.

Alerts:

- Active model returns `404`.
- Authentication failure.
- Circuit remains open for more than five minutes.
- Remaining interactive quota falls below reserve.
- Private grading queue exceeds its SLA.
- Degraded tutor responses exceed 5% in a rolling window.

## 7. Implementation slices

### Slice 1 - Normalized adapters and registry

- Move workload-to-model mappings into typed registry configuration.
- Normalize status/errors/usage/rate-limit headers in provider adapters.
- Add model capability and data-policy metadata.

### Slice 2 - Probe, quota and circuit state

- Add passive/active probes.
- Add Redis QuotaTracker and distributed CircuitBreaker.
- Add admin/readiness summaries without exposing secrets.

### Slice 3 - Policy routing and intra-Groq fallback

- Add server-owned sensitivity classification.
- Implement candidate planning and fallback budget.
- Add Qwen -> GPT-OSS routes before Gemini.

### Slice 4 - Degraded modes and durable jobs

- Add cited tutor degraded response.
- Add idempotent `PENDING_AI_GRADING` and extraction retry jobs.
- Add learner-visible status and manual-review escalation.

### Slice 5 - Verification

- Unit tests for every error/policy route.
- Integration tests with fake 429/404/5xx/timeout/header responses.
- Live synthetic probes for currently configured models.
- Chaos test provider outage, Redis restart and duplicate worker delivery.

## 8. Acceptance criteria

- Qwen `429` routes to GPT-OSS before any cross-provider fallback.
- Public/synthetic requests may reach Gemini; private/restricted requests never do.
- Three qualifying failures open a shared circuit and suppress repeated network calls.
- Rate-limit headers are observable and background jobs preserve the interactive reserve.
- Removed models are detected by probes and do not remain active in the registry.
- Tutor degraded mode always contains real citations and no unsupported generated explanation.
- Essays survive provider outages and grading retries are idempotent.
- No fallback loop; total attempts and latency stay within the request budget.
- No Ollama/local LLM dependency exists in deployment configuration.
