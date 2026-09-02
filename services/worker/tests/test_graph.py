from chiron_worker.graph import GraphLiteRetriever, GraphSource


class FakeAdaptive:
    def retrieve(self, query, **scope):
        return {
            "hits": [
                {
                    "id": "seed",
                    "score": 0.9,
                    "payload": {"source_span_id": "span-seed", "content": query},
                },
                {
                    "id": "semantic",
                    "score": 0.5,
                    "payload": {"source_span_id": "span-semantic", "content": "semantic"},
                },
            ],
            "strategy": "single_hybrid",
            "subqueries": [query],
            "route": scope["route"],
        }


class FakeGraphStore:
    def __init__(self):
        self.calls = []

    def expand_source_spans(self, spans, **scope):
        self.calls.append((spans, scope))
        return [GraphSource("span-graph", "concept-prerequisite", 1, 1.0)]


class FakeIndex:
    def fetch_by_source_span_ids(self, spans, **scope):
        assert spans == ["span-graph"]
        return [
            {
                "id": "graph",
                "payload": {"source_span_id": "span-graph", "content": "graph evidence"},
            }
        ]


def _retrieve(route: str):
    graph_store = FakeGraphStore()
    result = GraphLiteRetriever(FakeAdaptive(), graph_store, FakeIndex()).retrieve(
        "query",
        tenant_id="tenant",
        course_id="course",
        route=route,
        direct_candidate_limit=16,
        direct_limit=5,
        multi_hop_candidate_limit=12,
        multi_hop_limit=3,
        max_subqueries=1,
    )
    return result, graph_store


def test_graph_lite_never_expands_direct_queries() -> None:
    result, graph_store = _retrieve("direct")
    assert result["graph_expanded"] is False
    assert graph_store.calls == []


def test_graph_lite_injects_provenance_scored_evidence_for_prerequisite() -> None:
    result, graph_store = _retrieve("prerequisite")
    assert result["strategy"] == "graph_lite_1hop"
    assert result["graph_expanded"] is True
    assert result["hits"][1]["payload"]["source_span_id"] == "span-semantic"
    assert result["hits"][2]["payload"]["source_span_id"] == "span-graph"
    assert result["hits"][2]["retrieval_origin"] == "graph"
    assert graph_store.calls[0][1]["max_hops"] == 1
