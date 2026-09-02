from __future__ import annotations

from uuid import UUID

from chiron_worker.outbox import OutboxConsumer, OutboxEvent
from chiron_worker.qdrant import SparseVector

TENANT_ID = UUID("c2e1e494-3fa4-596f-8714-6877bac903dd")
EVENT_ID = UUID("11111111-1111-4111-8111-111111111111")
CHUNK_ID = UUID("22222222-2222-4222-8222-222222222222")
COURSE_ID = UUID("33333333-3333-4333-8333-333333333333")


class FakeStore:
    def __init__(self) -> None:
        self.event = OutboxEvent(
            EVENT_ID,
            TENANT_ID,
            {
                "chunk_ids": [str(CHUNK_ID)],
                "embedding_version": "multilingual-e5-large-mean-v1",
            },
            0,
        )
        self.done = False
        self.failures = 0

    def tenant_ids(self):
        return [TENANT_ID]

    def claim(self, _tenant_id):
        return [] if self.done else [self.event]

    def chunks(self, _event):
        return [
            {
                "id": CHUNK_ID,
                "tenant_id": TENANT_ID,
                "course_id": COURSE_ID,
                "content": "RRF fuses ranked lists",
            }
        ]

    def success(self, _event):
        self.done = True

    def failure(self, _event, _error):
        self.failures += 1


class FakeEncoder:
    def encode(self, texts):
        assert texts == ["RRF fuses ranked lists"]
        return [[0.5, 0.5]], [SparseVector([1], [1.0])]


class FakeIndex:
    def __init__(self, fail=False, existing_ids=None) -> None:
        self.fail = fail
        self.ids = []
        self.embedding_version = None
        self.existing_ids = set(existing_ids or [])

    def upsert(self, chunks, _dense, _sparse, embedding_version):
        if self.fail:
            raise ConnectionError("qdrant unavailable")
        self.ids.extend(chunk["id"] for chunk in chunks)
        self.embedding_version = embedding_version

    def delete(self, chunk_ids):
        self.ids.extend(chunk_ids)

    def point_ids(self, *, tenant_id, course_id):
        assert tenant_id == str(TENANT_ID)
        assert course_id == str(COURSE_ID)
        return self.existing_ids


def test_success_marks_event_only_after_stable_point_upsert() -> None:
    store = FakeStore()
    index = FakeIndex()
    result = OutboxConsumer(store, FakeEncoder(), index).drain_once()

    assert result == {"claimed": 1, "processed": 1, "failed": 0}
    assert index.ids == [CHUNK_ID]
    assert index.embedding_version == "multilingual-e5-large-mean-v1"
    assert store.done is True


def test_failure_keeps_event_retryable() -> None:
    store = FakeStore()
    result = OutboxConsumer(store, FakeEncoder(), FakeIndex(fail=True)).drain_once()

    assert result == {"claimed": 1, "processed": 0, "failed": 1}
    assert store.done is False
    assert store.failures == 1


def test_existing_qdrant_point_skips_embedding_and_marks_event_processed() -> None:
    class UnexpectedEncoder:
        def encode(self, _texts):
            raise AssertionError("existing points must not be embedded again")

    store = FakeStore()
    index = FakeIndex(existing_ids={str(CHUNK_ID)})

    result = OutboxConsumer(store, UnexpectedEncoder(), index).drain_once()

    assert result == {"claimed": 1, "processed": 1, "failed": 0}
    assert index.ids == []
    assert store.done is True
