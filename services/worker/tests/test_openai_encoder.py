from __future__ import annotations

import json

import httpx
import pytest

from chiron_worker.qdrant import (
    OpenAIEncoder,
    QdrantChunkIndex,
    QdrantCloudInferenceEncoder,
    QdrantInferenceDocument,
)


class FakeArray(list):
    def tolist(self) -> list:
        return list(self)


class FakeSparseVector:
    def __init__(self, index: int) -> None:
        self.indices = FakeArray([index])
        self.values = FakeArray([1.0])


class FakeSparseEncoder:
    def embed(self, texts):
        return iter(FakeSparseVector(index) for index, _ in enumerate(texts))

    def query_embed(self, query):
        assert query == "RRF là gì?"
        return iter([FakeSparseVector(7)])


def test_openai_encoder_preserves_api_order_and_combines_sparse_vectors() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/v1/embeddings"
        payload = json.loads(request.content)
        assert payload == {
            "model": "text-embedding-3-small",
            "input": ["first", "second"],
            "encoding_format": "float",
            "dimensions": 2,
        }
        return httpx.Response(
            200,
            json={
                "data": [
                    {"index": 1, "embedding": [0.3, 0.4]},
                    {"index": 0, "embedding": [0.1, 0.2]},
                ]
            },
        )

    client = httpx.Client(
        transport=httpx.MockTransport(handler), base_url="https://api.openai.com/v1"
    )
    encoder = OpenAIEncoder(
        api_key="test-key",
        model="text-embedding-3-small",
        sparse_model="Qdrant/bm25",
        dimensions=2,
        allow_document_embedding=True,
        client=client,
        sparse_encoder=FakeSparseEncoder(),
    )

    dense, sparse = encoder.encode(["first", "second"])

    assert dense == [[0.1, 0.2], [0.3, 0.4]]
    assert [item.indices for item in sparse] == [[0], [1]]


def test_openai_encoder_rejects_missing_key() -> None:
    with pytest.raises(ValueError, match="OPENAI_API_KEY"):
        OpenAIEncoder(
            api_key="",
            model="text-embedding-3-small",
            sparse_model="Qdrant/bm25",
            sparse_encoder=FakeSparseEncoder(),
        )


def test_openai_encoder_blocks_document_embedding_by_default() -> None:
    encoder = OpenAIEncoder(
        api_key="test-key",
        model="text-embedding-3-small",
        sparse_model="Qdrant/bm25",
        sparse_encoder=FakeSparseEncoder(),
    )

    with pytest.raises(PermissionError, match="local embedding pipeline"):
        encoder.encode(["private course material"])


def test_openai_encoder_rejects_wrong_dimension() -> None:
    client = httpx.Client(
        transport=httpx.MockTransport(
            lambda _request: httpx.Response(
                200, json={"data": [{"index": 0, "embedding": [0.1]}]}
            )
        ),
        base_url="https://api.openai.com/v1",
    )
    encoder = OpenAIEncoder(
        api_key="test-key",
        model="text-embedding-3-small",
        sparse_model="Qdrant/bm25",
        dimensions=2,
        allow_document_embedding=True,
        client=client,
        sparse_encoder=FakeSparseEncoder(),
    )

    with pytest.raises(RuntimeError, match="dimensions"):
        encoder.encode(["one"])


def test_qdrant_cloud_inference_encoder_uses_named_documents_without_local_models() -> None:
    encoder = QdrantCloudInferenceEncoder(
        dense_model="sentence-transformers/all-MiniLM-L6-v2",
        sparse_model="qdrant/bm25",
        dense_size=384,
        allow_document_embedding=True,
    )

    dense, sparse = encoder.encode(["Nội dung công khai"])
    query_dense, query_sparse = encoder.encode_query("câu hỏi")

    assert dense[0].text == "Nội dung công khai"
    assert dense[0].model == "sentence-transformers/all-MiniLM-L6-v2"
    assert sparse[0].model == "qdrant/bm25"
    assert query_dense.text == "câu hỏi"
    assert query_sparse.model == "qdrant/bm25"


def test_qdrant_cloud_inference_encoder_blocks_unapproved_documents() -> None:
    encoder = QdrantCloudInferenceEncoder(
        dense_model="sentence-transformers/all-MiniLM-L6-v2",
        sparse_model="qdrant/bm25",
        dense_size=384,
    )

    with pytest.raises(PermissionError, match="document inference"):
        encoder.encode(["private content"])


def test_qdrant_index_serializes_cloud_inference_documents_as_rest_inputs() -> None:
    document = QdrantInferenceDocument("public text", "qdrant/bm25")

    assert QdrantChunkIndex._vector_input(document) == {
        "text": "public text",
        "model": "qdrant/bm25",
    }
