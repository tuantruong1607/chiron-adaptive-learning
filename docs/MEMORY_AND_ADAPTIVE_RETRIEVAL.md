# Conversation memory and adaptive retrieval

## Memory boundaries

- `chat_threads` and `chat_messages` provide tenant-scoped short-term conversation history.
- `learning_events` is an append-only episodic timeline. Tutor events record identifiers and decision metadata, not a second copy of message content.
- The learner and tenant always come from the bearer token. A client-supplied thread must belong to that learner, tenant and course.
- Chat messages never update mastery. Only assessed evidence may change `mastery_states`.
- All three tables use forced PostgreSQL RLS. The runtime role cannot update or delete episodic events.
- Raw conversation history is stored server-side but is not forwarded to Groq or Gemini by default. This avoids creating an implicit new private-data flow.

## Adaptive hybrid retrieval

The API classifies a query before dispatching work:

- `direct`: one dense + BM25 hybrid query, smaller candidate pool (`16` by default).
- `prerequisite` or `multi_hop`: two or three deterministic subqueries, each hybrid-searched, then deduplicated by `source_span_id` and fused with reciprocal-rank fusion.

Multi-query RRF scores are normalized against the theoretical top-rank score for the number of subqueries. This keeps the tutor's evidence threshold meaningful across both direct hybrid scores and fused multi-hop scores.

This keeps the common narrow-question path cheap while spending more retrieval work only when the wording indicates relationships, dependencies, comparisons or causal chains. Tenant and course filters are applied inside every subquery.

This is graph-ready, not yet graph traversal: after concept-to-chunk links are populated at scale, deterministic graph-neighbor expansion can replace or complement the query expansions without changing the tutor API.
