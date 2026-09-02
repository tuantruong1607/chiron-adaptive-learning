from __future__ import annotations

from hashlib import sha256

from chiron_worker.config import get_settings
from chiron_worker.outbox import OutboxConsumer, OutboxStore
from chiron_worker.qdrant import QdrantChunkIndex, SparseVector


class DeterministicDemoEncoder:
    """Small deterministic encoder for infrastructure E2E; never used by the Celery task."""

    def encode(self, texts: list[str]):
        dense: list[list[float]] = []
        sparse: list[SparseVector] = []
        for text in texts:
            digest = sha256(text.encode()).digest()
            vector = [byte / 255 for byte in digest[:16]]
            norm = sum(value * value for value in vector) ** 0.5 or 1
            dense.append([value / norm for value in vector])
            sparse.append(SparseVector([int(digest[16])], [1.0]))
        return dense, sparse


if __name__ == "__main__":
    base_settings = get_settings()
    settings = base_settings.model_copy(
        update={"qdrant_collection": f"{base_settings.qdrant_collection}_e2e"}
    )
    result = OutboxConsumer(
        OutboxStore(settings),
        DeterministicDemoEncoder(),
        QdrantChunkIndex(settings),
    ).drain_once()
    print(result)
