from __future__ import annotations

import argparse
import json
from collections import defaultdict
from hashlib import sha256
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create an immutable stratified eval split")
    parser.add_argument("--dataset", type=Path, default=Path("eval/rag/golden.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("eval/rag/splits/v1.json"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cases = [
        json.loads(line)
        for line in args.dataset.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    grouped: dict[str, list[str]] = defaultdict(list)
    for case in cases:
        grouped[str(case["query_class"])].append(str(case["id"]))
    holdout_targets = {"direct": 5, "prerequisite": 5, "multi_hop": 5}
    holdout: set[str] = set()
    for query_class, ids in grouped.items():
        ordered = sorted(ids, key=lambda case_id: sha256(f"split-v1:{case_id}".encode()).hexdigest())
        holdout.update(ordered[: holdout_targets[query_class]])
    all_ids = {str(case["id"]) for case in cases}
    manifest = {
        "version": "retrieval-split-v1",
        "dataset": str(args.dataset),
        "dataset_sha256": sha256(args.dataset.read_bytes()).hexdigest(),
        "strategy": "sha256(split-v1:<case-id>), stratified 5 holdout per query class",
        "development_ids": sorted(all_ids - holdout),
        "holdout_ids": sorted(holdout),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"development": len(all_ids - holdout), "holdout": len(holdout)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
