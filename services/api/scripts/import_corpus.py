from __future__ import annotations

import argparse
import json
from pathlib import Path

from app.db import get_session_factory
from app.ingestion import import_corpus
from app.ingestion.importer import DEFAULT_EMBEDDING_VERSION, DEFAULT_OUTBOX_CHUNK_BATCH_SIZE


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Chiron Markdown corpus idempotently")
    parser.add_argument("--data-root", type=Path, default=Path(__file__).resolve().parents[3] / "data")
    parser.add_argument("--tenant", default="demo")
    parser.add_argument("--course", default="rag-intensive")
    parser.add_argument("--target-tokens", type=int, default=500)
    parser.add_argument("--max-tokens", type=int, default=700)
    parser.add_argument("--overlap-tokens", type=int, default=80)
    parser.add_argument("--embedding-version", default=DEFAULT_EMBEDDING_VERSION)
    parser.add_argument(
        "--outbox-chunk-batch-size", type=int, default=DEFAULT_OUTBOX_CHUNK_BATCH_SIZE
    )
    args = parser.parse_args()
    report = import_corpus(
        get_session_factory(), args.data_root, args.tenant, args.course,
        args.target_tokens, args.max_tokens, args.overlap_tokens,
        args.embedding_version, args.outbox_chunk_batch_size,
    )
    print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
