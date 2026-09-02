from datetime import UTC, datetime, timedelta
from uuid import UUID

from fastapi.testclient import TestClient

import app.main as main_module
from app.auth import Principal, create_access_token
from app.main import app
from app.question_bank import mock_exam_item, mock_exam_questions

client = TestClient(app)
TEST_PRINCIPAL = Principal(
    user_id=UUID("11111111-1111-4111-8111-111111111111"),
    tenant_id=UUID("22222222-2222-4222-8222-222222222222"),
    role="learner",
)
AUTH_HEADERS = {"Authorization": f"Bearer {create_access_token(TEST_PRINCIPAL)}"}


def test_health_and_readiness() -> None:
    assert client.get("/healthz").json() == {"status": "ok"}
    response = client.get("/readyz")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"


def test_metrics_endpoint_requires_operations_token(monkeypatch) -> None:
    monkeypatch.setattr(main_module.settings, "ops_metrics_token", "metrics-test-token")
    assert client.get("/metrics").status_code == 401
    response = client.get("/metrics", headers={"X-Metrics-Token": "metrics-test-token"})
    assert response.status_code == 200
    assert "chiron_http_requests_total" in response.text


def test_retrieval_requires_bearer_token() -> None:
    response = client.get("/api/v1/retrieval", params={"q": "Giải thích RRF"})
    assert response.status_code == 401


def test_tutor_requires_bearer_token_and_idempotency_key() -> None:
    assert client.post("/api/v1/tutor", json={"question": "Giải thích RRF"}).status_code == 401
    response = client.post(
        "/api/v1/tutor", json={"question": "Giải thích RRF"}, headers=AUTH_HEADERS
    )
    assert response.status_code == 422


def test_tutor_keeps_short_term_thread_and_replays_idempotently() -> None:
    headers = {**AUTH_HEADERS, "Idempotency-Key": "tutor-memory-turn-0001"}
    first = client.post(
        "/api/v1/tutor", json={"question": "Giải thích RRF"}, headers=headers
    )
    assert first.status_code == 200
    first_payload = first.json()
    assert first_payload["thread_id"]
    assert first_payload["memory_turns"] == 0

    replay = client.post(
        "/api/v1/tutor", json={"question": "Giải thích RRF"}, headers=headers
    )
    assert replay.status_code == 200
    assert replay.json()["trace_id"] == first_payload["trace_id"]

    follow_up = client.post(
        "/api/v1/tutor",
        json={
            "question": "Cho một ví dụ ngắn hơn",
            "thread_id": first_payload["thread_id"],
        },
        headers={**AUTH_HEADERS, "Idempotency-Key": "tutor-memory-turn-0002"},
    )
    assert follow_up.status_code == 200
    assert follow_up.json()["thread_id"] == first_payload["thread_id"]
    assert follow_up.json()["memory_turns"] == 2


def test_knowledge_map_has_provenance_and_acyclic_prerequisites() -> None:
    unauthenticated = client.get("/api/v1/courses/rag-intensive/knowledge-map")
    assert unauthenticated.status_code == 401
    response = client.get(
        "/api/v1/courses/rag-intensive/knowledge-map", headers=AUTH_HEADERS
    )
    assert response.status_code == 200
    payload = response.json()
    assert len(payload["nodes"]) >= 8
    assert all(node["citations"] for node in payload["nodes"])
    source_span_id = payload["nodes"][0]["citations"][0]["source_span_id"]
    assert client.get(
        f"/api/v1/courses/rag-intensive/knowledge-map/sources/{source_span_id}"
    ).status_code == 401
    locator = client.get(
        f"/api/v1/courses/rag-intensive/knowledge-map/sources/{source_span_id}",
        headers=AUTH_HEADERS,
    )
    assert locator.status_code == 200
    assert locator.json()["source_span_id"] == source_span_id
    assert locator.json()["locator"] == payload["nodes"][0]["citations"][0]["locator"]
    assert client.get(
        "/api/v1/courses/rag-intensive/knowledge-map/sources/missing-span",
        headers=AUTH_HEADERS,
    ).status_code == 404
    prerequisite_edges = [
        edge for edge in payload["edges"] if edge["relation"] == "prerequisite_of"
    ]
    assert all(edge["source"] != edge["target"] for edge in prerequisite_edges)
    connected_nodes = {
        concept_id
        for edge in payload["edges"]
        for concept_id in (edge["source"], edge["target"])
    }
    assert {node["id"] for node in payload["nodes"]} <= connected_nodes


def test_diagnostic_does_not_leak_answer_key_and_is_idempotent() -> None:
    questions = client.get("/api/v1/courses/rag-intensive/diagnostic").json()
    assert len(questions) == 25
    assert "answer" not in questions[0]
    submission = {"answers": [{"question_id": "diag-foundation-01", "option_id": "b"}]}
    headers = {**AUTH_HEADERS, "Idempotency-Key": "test-diagnostic-1"}
    first = client.post(
        "/api/v1/courses/rag-intensive/diagnostic/submit", json=submission, headers=headers
    )
    second = client.post(
        "/api/v1/courses/rag-intensive/diagnostic/submit", json=submission, headers=headers
    )
    assert first.status_code == 200
    assert first.json()["attempt_id"] == second.json()["attempt_id"]


def test_onboarding_status_changes_after_first_diagnostic() -> None:
    principal = Principal(
        user_id=UUID("44444444-4444-4444-8444-444444444444"),
        tenant_id=TEST_PRINCIPAL.tenant_id,
        role="learner",
    )
    headers = {"Authorization": f"Bearer {create_access_token(principal)}"}
    before = client.get(
        "/api/v1/courses/rag-intensive/diagnostic/status", headers=headers
    )
    assert before.status_code == 200
    assert before.json() == {
        "completed": False,
        "question_count": 25,
        "next_path": "/diagnostic",
    }

    submitted = client.post(
        "/api/v1/courses/rag-intensive/diagnostic/submit",
        json={"answers": [{"question_id": "diag-foundation-01", "option_id": "b"}]},
        headers={**headers, "Idempotency-Key": "first-onboarding-diagnostic"},
    )
    assert submitted.status_code == 200
    after = client.get(
        "/api/v1/courses/rag-intensive/diagnostic/status", headers=headers
    )
    assert after.json()["completed"] is True
    assert after.json()["next_path"] == "/map"


def test_mock_exam_has_100_items_and_grades_without_leaking_keys() -> None:
    response = client.get("/api/v1/mock-exams/de-01", headers=AUTH_HEADERS)
    assert response.status_code == 200
    questions = response.json()["questions"]
    assert len(questions) == 100
    assert sum(item["kind"] == "objective" for item in questions) == 90
    assert sum(item["kind"] == "constructed" for item in questions) == 10
    assert all("answerKey" not in item and "explanation" not in item for item in questions)

    answers = []
    for item in mock_exam_questions("de-01"):
        private = mock_exam_item(item["id"])
        if item["kind"] == "objective":
            answers.append(
                {"question_id": item["id"], "option_id": private["answerKey"]}
            )
        else:
            answers.append({"question_id": item["id"], "text": ""})
    graded = client.post(
        "/api/v1/mock-exams/de-01/grade",
        json={"answers": answers},
        headers=AUTH_HEADERS,
    )
    assert graded.status_code == 200
    assert graded.json()["score"] == 90
    assert graded.json()["objective_score"] == 90
    assert graded.json()["constructed_score"] == 0
    assert graded.json()["grading_mode"] == "deterministic"


def test_lab_scoring_is_deterministic() -> None:
    payload = {
        "dense_weight": 0.55,
        "sparse_weight": 0.45,
        "rerank_depth": 24,
        "tenant_filter": True,
        "transfer_answer": "RRF dùng rank thay vì raw score khác thang đo.",
    }
    response = client.post(
        "/api/v1/labs/hybrid-search/submit",
        json=payload,
        headers={**AUTH_HEADERS, "Idempotency-Key": "lab-submit-0001"},
    )
    assert response.status_code == 201
    assert response.json()["score"] == 100
    assert response.json()["passed"] is True
    assert response.json()["mastery_update"]["concept_id"] == "reciprocal_rank_fusion"
    assert response.json()["study_plan"]["planner_version"] == "cram-planner-v1"


def test_lab_catalog_contains_six_grounded_labs() -> None:
    assert client.get("/api/v1/labs").status_code == 401
    response = client.get("/api/v1/labs", headers=AUTH_HEADERS)
    assert response.status_code == 200
    labs = response.json()
    assert len(labs) == 6
    assert {item["id"] for item in labs} == {
        "hybrid-search",
        "chunking-strategy",
        "rrf-ranking",
        "metadata-filtering",
        "rag-evaluation",
        "graph-lite-routing",
    }
    assert all(item["controls"] and item["transfer_prompts"] for item in labs)
    assert all(item["source_span_ids"] for item in labs)


def test_learning_resources_form_a_grounded_understanding_loop() -> None:
    response = client.get(
        "/api/v1/courses/rag-intensive/learning-resources",
        headers=AUTH_HEADERS,
    )
    assert response.status_code == 200
    resources = response.json()
    assert {item["concept_id"] for item in resources} >= {
        "chunking",
        "hybrid_search_rrf",
        "metadata_filtered_search",
        "graphrag_multi_hop",
        "rag_evaluation",
    }
    assert all(
        item["key_ideas"]
        and len(item["worked_example"]) >= 2
        and item["common_mistakes"]
        and item["citations"]
        for item in resources
    )


def test_each_lab_has_a_scenario_specific_perfect_submission() -> None:
    submissions = {
        "chunking-strategy": {
            "configuration": {"strategy": "hierarchical", "chunk_size": 600, "overlap": 80, "preserve_locators": True},
            "transfer_answers": {"boundary": "Dùng heading và section làm ranh giới để citation quay lại source locator ổn định."},
        },
        "rrf-ranking": {
            "configuration": {"fusion": "rrf", "rrf_k": 60, "candidate_depth": 20},
            "transfer_answers": {
                "reasoning": "Dense và sparse có raw score khác thang nên hợp nhất bằng rank.",
                "failure": "Exact term hiếm cần sparse BM25 giữ lexical signal.",
            },
        },
        "metadata-filtering": {
            "configuration": {"tenant_filter": True, "course_filter": True, "filter_stage": "pre"},
            "transfer_answers": {
                "isolation": "Tenant authorization ngăn leak và rò dữ liệu chéo.",
                "recall": "Payload pre-filter thu hẹp candidate trước top-k nhưng vẫn bảo vệ recall đúng scope.",
            },
        },
        "rag-evaluation": {
            "configuration": {"faithfulness_gate": 0.85, "context_recall_gate": 0.8, "verify_citations": True, "persist_regression": True},
            "transfer_answers": {
                "diagnosis": "Context recall đo retrieval, còn faithfulness và citation kiểm tra generation.",
                "gate": "Release gate so với golden holdout baseline và lưu regression.",
            },
        },
        "graph-lite-routing": {
            "configuration": {"routing": "adaptive", "max_hops": 2, "expansion_limit": 8, "direct_fallback": True},
            "transfer_answers": {
                "routing": "Intent prerequisite hoặc multi-hop mới route qua quan hệ graph.",
                "regression": "So direct fact với baseline để chặn regression và không giảm recall.",
            },
        },
    }
    for index, (lab_id, payload) in enumerate(submissions.items(), start=1):
        response = client.post(
            f"/api/v1/labs/{lab_id}/submit",
            json=payload,
            headers={**AUTH_HEADERS, "Idempotency-Key": f"scenario-lab-perfect-{index:02d}"},
        )
        assert response.status_code == 201, response.text
        assert response.json()["score"] == 100, (lab_id, response.json())
        assert response.json()["passed"] is True


def test_unknown_lab_is_rejected() -> None:
    payload = {
        "dense_weight": 0.55,
        "sparse_weight": 0.45,
        "rerank_depth": 24,
        "tenant_filter": True,
        "transfer_answer": "RRF dùng rank thay vì raw score khác thang đo.",
    }
    assert (
        client.post(
            "/api/v1/labs/unknown/submit",
            json=payload,
            headers={**AUTH_HEADERS, "Idempotency-Key": "lab-unknown-0001"},
        ).status_code
        == 404
    )


def test_essay_submission_is_private_and_idempotent() -> None:
    payload = {
        "course": "rag-intensive",
        "prompt": "Thiết kế pipeline retrieval an toàn.",
        "answer": "Tôi dùng tenant filter trước retrieval và lưu citation.",
        "rubric_id": "system-design-v1",
    }
    headers = {**AUTH_HEADERS, "Idempotency-Key": "essay-submit-0001"}
    first = client.post("/api/v1/essays", json=payload, headers=headers)
    replay = client.post("/api/v1/essays", json=payload, headers=headers)
    assert first.status_code == 202
    assert replay.status_code == 202
    assert first.json()["id"] == replay.json()["id"]
    assert first.json()["status"] == "pending_ai_grading"

    fetched = client.get(f"/api/v1/essays/{first.json()['id']}", headers=AUTH_HEADERS)
    assert fetched.status_code == 200
    assert fetched.json()["answer"] == payload["answer"]


def test_worker_grades_essay_and_escalates_low_confidence(monkeypatch) -> None:
    monkeypatch.setattr(main_module.settings, "worker_internal_token", "test-worker-token")
    submitted = client.post(
        "/api/v1/essays",
        json={
            "prompt": "Thiết kế một pipeline RAG có kiểm chứng nguồn.",
            "answer": "Tôi dùng citation và source span để kiểm tra evidence.",
            "rubric_id": "system-design-v1",
        },
        headers={**AUTH_HEADERS, "Idempotency-Key": "essay-grade-0001"},
    )
    assert submitted.status_code == 202

    graded = client.post(
        f"/api/v1/internal/essays/{submitted.json()['id']}/grade",
        json={"tenant_id": str(TEST_PRINCIPAL.tenant_id)},
        headers={"X-Worker-Token": "test-worker-token"},
    )
    assert graded.status_code == 200
    assert graded.json()["status"] == "needs_human_review"
    assert graded.json()["human_review_required"] is True
    assert graded.json()["criterion_scores"]
    assert graded.json()["provider"] == "mock"

    reviewer = Principal(
        user_id=UUID("33333333-3333-4333-8333-333333333333"),
        tenant_id=TEST_PRINCIPAL.tenant_id,
        role="instructor",
    )
    reviewed = client.post(
        f"/api/v1/essays/{submitted.json()['id']}/review",
        json={
            "score": 7,
            "max_score": 10,
            "feedback": "Reviewed with the rubric and source evidence.",
            "criterion_scores": {"grounding": 3, "reasoning": 3, "transfer": 1},
        },
        headers={"Authorization": f"Bearer {create_access_token(reviewer)}"},
    )
    assert reviewed.status_code == 200
    assert reviewed.json()["status"] == "graded"
    assert reviewed.json()["provider"] == "human"


def test_overdue_essay_enters_tenant_scoped_instructor_queue() -> None:
    submitted = client.post(
        "/api/v1/essays",
        json={
            "prompt": "Explain a safe retrieval design with evidence.",
            "answer": "Use a tenant filter and verify each citation against its source span.",
            "rubric_id": "system-design-v1",
        },
        headers={**AUTH_HEADERS, "Idempotency-Key": "essay-sla-queue-0001"},
    )
    assert submitted.status_code == 202
    assert client.get("/api/v1/essays/review-queue", headers=AUTH_HEADERS).status_code == 403

    store = main_module.get_essay_store()
    assert store.escalate_overdue(
        tenant_id=TEST_PRINCIPAL.tenant_id,
        cutoff=datetime.now(UTC) + timedelta(seconds=1),
    ) >= 1

    reviewer = Principal(
        user_id=UUID("33333333-3333-4333-8333-333333333333"),
        tenant_id=TEST_PRINCIPAL.tenant_id,
        role="instructor",
    )
    queue = client.get(
        "/api/v1/essays/review-queue",
        headers={"Authorization": f"Bearer {create_access_token(reviewer)}"},
    )
    assert queue.status_code == 200
    queued = next(item for item in queue.json() if item["id"] == submitted.json()["id"])
    assert queued["status"] == "needs_human_review"
    assert queued["human_review_required"] is True


def test_adaptive_state_and_three_day_plan_expose_decision_audit() -> None:
    states = client.get("/api/v1/courses/rag-intensive/learning-state", headers=AUTH_HEADERS)
    assert states.status_code == 200
    assert all("evidence_confidence" in item for item in states.json())

    plan = client.get(
        "/api/v1/courses/rag-intensive/study-plan",
        params={"horizon_days": 3, "daily_minutes": 60},
        headers=AUTH_HEADERS,
    )
    assert plan.status_code == 200
    payload = plan.json()
    assert payload["horizon_days"] == 3
    assert payload["daily_minutes"] == 60
    assert payload["planner_version"] == "cram-planner-v1"
    assert payload["component_scores"]
    assert all(0 <= item["day_offset"] <= 2 for item in payload["items"])


def test_diagnostic_accepts_self_assessment_but_updates_mastery_from_evidence() -> None:
    submission = {
        "self_assessments": {"ai_llm_foundations": 5},
        "answers": [{"question_id": "diag-foundation-01", "option_id": "a"}],
    }
    response = client.post(
        "/api/v1/courses/rag-intensive/diagnostic/submit",
        json=submission,
        headers={
            **AUTH_HEADERS,
            "Idempotency-Key": "adaptive-self-report-does-not-equal-mastery",
        },
    )

    assert response.status_code == 200
    update = response.json()["mastery_updates"][0]
    assert update["current"] < 1
    assert update["diagnostic_status"] in {"partial", "verified"}
    assert update["confidence_gap"] > 0


def test_learner_routes_reject_missing_access_token() -> None:
    response = client.get("/api/v1/courses/rag-intensive/learning-state")
    assert response.status_code == 401
    assert response.json()["detail"] == "Bearer access token required"


def test_diagnostic_rejects_client_supplied_learner_id() -> None:
    response = client.post(
        "/api/v1/courses/rag-intensive/diagnostic/submit",
        json={
            "learner_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
            "answers": [{"question_id": "diag-foundation-01", "option_id": "b"}],
        },
        headers={**AUTH_HEADERS, "Idempotency-Key": "must-use-token-principal"},
    )
    assert response.status_code == 422
    errors = response.json()["error"]["details"]["errors"]
    assert errors[0]["type"] == "extra_forbidden"
