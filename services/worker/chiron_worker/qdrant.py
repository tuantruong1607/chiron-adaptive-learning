from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

import httpx

from .config import WorkerSettings


@dataclass(frozen=True, slots=True)
class SparseVector:
    indices: list[int]
    values: list[float]


@dataclass(frozen=True, slots=True)
class QdrantInferenceDocument:
    """Text input that Qdrant Cloud turns into a vector server-side."""

    text: str
    model: str


class DenseEmbeddingUnavailable(RuntimeError):
    def __init__(self, sparse: SparseVector) -> None:
        super().__init__("Dense query embedding provider is unavailable")
        self.sparse = sparse


class Encoder(Protocol):
    def encode(
        self, texts: list[str]
    ) -> tuple[list[list[float] | QdrantInferenceDocument], list[SparseVector | QdrantInferenceDocument]]: ...

    def encode_query(
        self, query: str
    ) -> tuple[list[float] | QdrantInferenceDocument, SparseVector | QdrantInferenceDocument]: ...


class FastEmbedEncoder:
    def __init__(
        self,
        dense_model: str,
        sparse_model: str,
        cache_dir: str | None = None,
    ) -> None:
        try:
            from fastembed import SparseTextEmbedding, TextEmbedding
        except ImportError as exc:
            raise RuntimeError("Install chiron-worker[embedding] to run vector sync") from exc
        self.dense = TextEmbedding(model_name=dense_model, cache_dir=cache_dir)
        self.sparse = SparseTextEmbedding(model_name=sparse_model, cache_dir=cache_dir)

    def encode(self, texts: list[str]) -> tuple[list[list[float]], list[SparseVector]]:
        return self.encode_dense(texts), self.encode_sparse(texts)

    def encode_dense(self, texts: list[str]) -> list[list[float]]:
        return [vector.tolist() for vector in self.dense.embed(texts)]

    def encode_sparse(self, texts: list[str]) -> list[SparseVector]:
        return [
            SparseVector(indices=item.indices.tolist(), values=item.values.tolist())
            for item in self.sparse.embed(texts)
        ]

    def encode_query(self, query: str) -> tuple[list[float], SparseVector]:
        dense = next(iter(self.dense.query_embed(query))).tolist()
        sparse = next(iter(self.sparse.query_embed(query)))
        return dense, SparseVector(
            indices=sparse.indices.tolist(), values=sparse.values.tolist()
        )


class OpenAIEncoder:
    """OpenAI dense embeddings combined with the existing local BM25 encoder.

    Document and query embeddings must use the same model, dimensions, version,
    and Qdrant collection. This adapter deliberately does not fall back to a
    different dense provider because vectors from different spaces are invalid
    for similarity search.
    """

    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        sparse_model: str,
        dimensions: int | None = None,
        base_url: str = "https://api.openai.com/v1",
        allow_document_embedding: bool = False,
        client: httpx.Client | None = None,
        sparse_encoder: Any | None = None,
    ) -> None:
        if not api_key:
            raise ValueError("OPENAI_API_KEY is required when EMBEDDING_PROVIDER=openai")
        if sparse_encoder is None:
            try:
                from fastembed import SparseTextEmbedding
            except ImportError as exc:
                raise RuntimeError("Install chiron-worker[embedding] to run vector sync") from exc
            sparse_encoder = SparseTextEmbedding(model_name=sparse_model)
        self.model = model
        self.dimensions = dimensions
        self.allow_document_embedding = allow_document_embedding
        self.sparse = sparse_encoder
        self.client = client or httpx.Client(
            base_url=base_url.rstrip("/"),
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30,
        )

    def _dense(self, texts: list[str]) -> list[list[float]]:
        payload: dict[str, Any] = {
            "model": self.model,
            "input": texts,
            "encoding_format": "float",
        }
        if self.dimensions is not None:
            payload["dimensions"] = self.dimensions
        response = self.client.post("/embeddings", json=payload)
        response.raise_for_status()
        data = response.json().get("data", [])
        ordered = sorted(data, key=lambda item: int(item["index"]))
        if len(ordered) != len(texts):
            raise RuntimeError(
                f"OpenAI returned {len(ordered)} embeddings for {len(texts)} inputs"
            )
        vectors = [[float(value) for value in item["embedding"]] for item in ordered]
        if self.dimensions is not None and any(
            len(vector) != self.dimensions for vector in vectors
        ):
            raise RuntimeError("OpenAI embedding dimensions do not match configuration")
        return vectors

    def encode(self, texts: list[str]) -> tuple[list[list[float]], list[SparseVector]]:
        if not self.allow_document_embedding:
            raise PermissionError(
                "OpenAI document embedding is disabled; use the local embedding pipeline"
            )
        dense = self._dense(texts)
        sparse = [
            SparseVector(indices=item.indices.tolist(), values=item.values.tolist())
            for item in self.sparse.embed(texts)
        ]
        return dense, sparse

    def encode_query(self, query: str) -> tuple[list[float], SparseVector]:
        sparse = next(iter(self.sparse.query_embed(query)))
        sparse_vector = SparseVector(
            indices=sparse.indices.tolist(), values=sparse.values.tolist()
        )
        try:
            dense = self._dense([query])[0]
        except httpx.HTTPError as exc:
            raise DenseEmbeddingUnavailable(sparse_vector) from exc
        return dense, sparse_vector


class QdrantCloudInferenceEncoder:
    """Use Qdrant Cloud Inference so the worker carries no model artifacts.

    This provider is intended for small ARM/Free-tier deployments. The dense
    and sparse documents are sent to Qdrant as inference inputs; the cluster
    materializes both vectors during upsert/query. A separate collection and
    embedding version must be used when changing models.
    """

    def __init__(
        self,
        *,
        dense_model: str,
        sparse_model: str,
        dense_size: int,
        allow_document_embedding: bool = False,
    ) -> None:
        self.dense_model = dense_model
        self.sparse_model = sparse_model
        self.dense_size = dense_size
        self.allow_document_embedding = allow_document_embedding

    def encode(
        self, texts: list[str]
    ) -> tuple[list[QdrantInferenceDocument], list[QdrantInferenceDocument]]:
        if not self.allow_document_embedding:
            raise PermissionError(
                "Qdrant Cloud document inference is disabled; enable it only for approved content"
            )
        return (
            [QdrantInferenceDocument(text, self.dense_model) for text in texts],
            [QdrantInferenceDocument(text, self.sparse_model) for text in texts],
        )

    def encode_query(
        self, query: str
    ) -> tuple[QdrantInferenceDocument, QdrantInferenceDocument]:
        return (
            QdrantInferenceDocument(query, self.dense_model),
            QdrantInferenceDocument(query, self.sparse_model),
        )


class FastEmbedReranker:
    def __init__(self, model_name: str) -> None:
        from fastembed.rerank.cross_encoder import TextCrossEncoder

        supported = {item["model"] for item in TextCrossEncoder.list_supported_models()}
        if model_name not in supported:
            raise ValueError(
                f"FastEmbed does not provide an ONNX artifact for reranker {model_name!r}"
            )
        self.model = TextCrossEncoder(model_name=model_name)

    def scores(self, query: str, documents: list[str]) -> list[float]:
        return [float(score) for score in self.model.rerank(query, documents)]


class QdrantChunkIndex:
    def __init__(self, settings: WorkerSettings) -> None:
        self.base_url = settings.qdrant_url.rstrip("/")
        self.collection = settings.qdrant_collection
        self.inference_dense_size = settings.qdrant_inference_dense_size
        self.headers = {"api-key": settings.qdrant_api_key} if settings.qdrant_api_key else {}
        self.client = httpx.Client(timeout=30, headers=self.headers)

    def ensure_collection(self, dense_size: int) -> None:
        response = self.client.get(f"{self.base_url}/collections/{self.collection}")
        if response.status_code == 200:
            return
        if response.status_code != 404:
            response.raise_for_status()
        created = self.client.put(
            f"{self.base_url}/collections/{self.collection}",
            json={
                "vectors": {"dense": {"size": dense_size, "distance": "Cosine"}},
                "sparse_vectors": {"bm25": {"modifier": "idf"}},
                "on_disk_payload": True,
            },
        )
        if created.status_code not in {200, 201, 409}:
            created.raise_for_status()

    def point_ids(self, *, tenant_id: str, course_id: str) -> set[str]:
        point_ids: set[str] = set()
        offset: str | int | None = None
        while True:
            body: dict[str, Any] = {
                "filter": self._tenant_filter(tenant_id, course_id),
                "limit": 256,
                "with_payload": False,
                "with_vector": False,
            }
            if offset is not None:
                body["offset"] = offset
            response = self.client.post(
                f"{self.base_url}/collections/{self.collection}/points/scroll",
                json=body,
            )
            if response.status_code == 404:
                return set()
            response.raise_for_status()
            result = response.json().get("result", {})
            point_ids.update(str(point["id"]) for point in result.get("points", []))
            offset = result.get("next_page_offset")
            if offset is None:
                return point_ids

    def dense_points(self, chunk_ids: list[str]) -> dict[str, dict[str, Any]]:
        if not chunk_ids:
            return {}
        response = self.client.post(
            f"{self.base_url}/collections/{self.collection}/points",
            json={
                "ids": chunk_ids,
                "with_payload": ["checksum", "embedding_version"],
                "with_vector": ["dense"],
            },
        )
        if response.status_code == 404:
            return {}
        response.raise_for_status()
        return {
            str(point["id"]): {
                "dense": point.get("vector", {}).get("dense"),
                "payload": point.get("payload") or {},
            }
            for point in response.json().get("result", [])
        }

    def fetch_by_source_span_ids(
        self,
        source_span_ids: list[str],
        *,
        tenant_id: str,
        course_id: str,
        limit: int,
    ) -> list[dict[str, Any]]:
        if not source_span_ids or limit <= 0:
            return []
        tenant_filter = self._tenant_filter(tenant_id, course_id)
        tenant_filter["must"].append(
            {"key": "source_span_id", "match": {"any": source_span_ids}}
        )
        response = self.client.post(
            f"{self.base_url}/collections/{self.collection}/points/scroll",
            json={
                "filter": tenant_filter,
                "limit": min(max(limit * 3, limit), 256),
                "with_payload": True,
                "with_vector": False,
            },
        )
        if response.status_code == 404:
            return []
        response.raise_for_status()
        points = list(response.json().get("result", {}).get("points", []))
        by_span: dict[str, dict[str, Any]] = {}
        for point in points:
            payload = point.get("payload") or {}
            source_span_id = str(payload.get("source_span_id") or "")
            if source_span_id and source_span_id not in by_span:
                by_span[source_span_id] = {**point, "score": 0.0}
        return [by_span[span_id] for span_id in source_span_ids if span_id in by_span][:limit]

    @staticmethod
    def _tenant_filter(tenant_id: str, course_id: str) -> dict[str, Any]:
        return {
            "must": [
                {"key": "tenant_id", "match": {"value": tenant_id}},
                {"key": "course_id", "match": {"value": course_id}},
                {"key": "is_active", "match": {"value": True}},
            ]
        }

    @staticmethod
    def _vector_input(value: list[float] | SparseVector | QdrantInferenceDocument) -> Any:
        if isinstance(value, QdrantInferenceDocument):
            return {"text": value.text, "model": value.model}
        if isinstance(value, SparseVector):
            return {"indices": value.indices, "values": value.values}
        return value

    def hybrid_query(
        self,
        dense: list[float] | QdrantInferenceDocument,
        sparse: SparseVector | QdrantInferenceDocument,
        *,
        tenant_id: str,
        course_id: str,
        candidate_limit: int,
    ) -> list[dict[str, Any]]:
        tenant_filter = self._tenant_filter(tenant_id, course_id)
        response = self.client.post(
            f"{self.base_url}/collections/{self.collection}/points/query",
            json={
                "prefetch": [
                    {
                        "query": self._vector_input(dense),
                        "using": "dense",
                        "filter": tenant_filter,
                        "limit": candidate_limit,
                    },
                    {
                        "query": self._vector_input(sparse),
                        "using": "bm25",
                        "filter": tenant_filter,
                        "limit": candidate_limit,
                    },
                ],
                "query": {"fusion": "rrf"},
                "limit": candidate_limit,
                "with_payload": True,
                "with_vector": False,
            },
        )
        if response.status_code == 404:
            return []
        response.raise_for_status()
        return list(response.json().get("result", {}).get("points", []))

    def dense_query(
        self,
        dense: list[float] | QdrantInferenceDocument,
        *,
        tenant_id: str,
        course_id: str,
        candidate_limit: int,
    ) -> list[dict[str, Any]]:
        response = self.client.post(
            f"{self.base_url}/collections/{self.collection}/points/query",
            json={
                "query": self._vector_input(dense),
                "using": "dense",
                "filter": self._tenant_filter(tenant_id, course_id),
                "limit": candidate_limit,
                "with_payload": True,
                "with_vector": False,
            },
        )
        if response.status_code == 404:
            return []
        response.raise_for_status()
        return list(response.json().get("result", {}).get("points", []))

    def sparse_query(
        self,
        sparse: SparseVector | QdrantInferenceDocument,
        *,
        tenant_id: str,
        course_id: str,
        candidate_limit: int,
    ) -> list[dict[str, Any]]:
        response = self.client.post(
            f"{self.base_url}/collections/{self.collection}/points/query",
            json={
                "query": self._vector_input(sparse),
                "using": "bm25",
                "filter": self._tenant_filter(tenant_id, course_id),
                "limit": candidate_limit,
                "with_payload": True,
                "with_vector": False,
            },
        )
        if response.status_code == 404:
            return []
        response.raise_for_status()
        return list(response.json().get("result", {}).get("points", []))

    def upsert(
        self,
        chunks: list[dict],
        dense_vectors: list[list[float] | QdrantInferenceDocument],
        sparse_vectors: list[SparseVector | QdrantInferenceDocument],
        embedding_version: str,
    ) -> None:
        if not chunks:
            return
        dense_size = (
            len(dense_vectors[0])
            if isinstance(dense_vectors[0], list)
            else self.inference_dense_size
        )
        self.ensure_collection(dense_size)
        points = []
        for chunk, dense, sparse in zip(chunks, dense_vectors, sparse_vectors, strict=True):
            points.append(
                {
                    "id": str(chunk["id"]),
                    "vector": {
                        "dense": self._vector_input(dense),
                        "bm25": self._vector_input(sparse),
                    },
                    "payload": {
                        "tenant_id": str(chunk["tenant_id"]),
                        "course_id": str(chunk["course_id"]),
                        "document_version_id": str(chunk["document_version_id"]),
                        "source_span_id": str(chunk["source_span_id"]),
                        "parent_chunk_id": (
                            str(chunk["parent_chunk_id"]) if chunk.get("parent_chunk_id") else None
                        ),
                        "checksum": chunk["checksum"],
                        "embedding_version": embedding_version,
                        "is_active": bool(chunk["is_active"]),
                        "chunk_type": chunk.get("chunk_type", "child"),
                        "ordinal": int(chunk.get("ordinal", 0)),
                        "token_count": int(chunk.get("token_count", 0)),
                        "locator": chunk.get("locator") or {},
                        "document_title": chunk.get("document_title"),
                        "source_path": chunk.get("source_path"),
                        "source_type": chunk.get("source_type"),
                        "content": chunk["content"],
                        "raw_checksum": chunk.get("raw_checksum", chunk["checksum"]),
                        "retrieval_text_checksum": chunk.get("retrieval_text_checksum"),
                        "enrichment_version": chunk.get("enrichment_version"),
                        "enrichment_variant": chunk.get("enrichment_variant"),
                        "enrichment_provenance": chunk.get("enrichment_provenance") or [],
                        "enrichment_aliases": chunk.get("enrichment_aliases") or [],
                        "enrichment_entities": chunk.get("enrichment_entities") or [],
                        "enrichment_pedagogy_labels": (
                            chunk.get("enrichment_pedagogy_labels") or []
                        ),
                        "enrichment_contextualized": bool(
                            chunk.get("enrichment_contextualized", False)
                        ),
                        "estimated_header_tokens": int(
                            chunk.get("estimated_header_tokens", 0)
                        ),
                        "estimated_retrieval_tokens": int(
                            chunk.get("estimated_retrieval_tokens", chunk.get("token_count", 0))
                        ),
                    },
                }
            )
        response = self.client.put(
            f"{self.base_url}/collections/{self.collection}/points?wait=true",
            json={"points": points},
        )
        response.raise_for_status()

    def delete(self, chunk_ids: list[str]) -> None:
        if not chunk_ids:
            return
        response = self.client.post(
            f"{self.base_url}/collections/{self.collection}/points/delete?wait=true",
            json={"points": chunk_ids},
        )
        if response.status_code == 404:
            return
        response.raise_for_status()
