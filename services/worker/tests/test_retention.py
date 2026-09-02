from chiron_worker.retention import REDACTED, redact_payload


def test_redact_payload_removes_nested_learner_content_and_preserves_metadata() -> None:
    payload = {
        "lab_id": "hybrid-search",
        "submission": {"code": "print('private')", "score": 0.8},
        "result": {"feedback": "grounded", "evidence_id": "evidence-1"},
        "answers": [{"question_id": "q1", "answer": "private"}],
    }

    redacted = redact_payload(payload)

    assert redacted["lab_id"] == "hybrid-search"
    assert redacted["submission"] == REDACTED
    assert redacted["answers"] == REDACTED
    assert redacted["result"]["feedback"] == "grounded"
    assert redacted["retention_redacted"] is True
