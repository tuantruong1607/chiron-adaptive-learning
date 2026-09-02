from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate full-course knowledge taxonomy")
    parser.add_argument(
        "--spec", type=Path, default=Path("services/api/app/course_taxonomy.json")
    )
    parser.add_argument(
        "--bank", type=Path, default=Path("services/api/app/generated_question_bank.json")
    )
    return parser.parse_args()


def prerequisite_cycles(nodes: set[str], edges: list[dict[str, Any]]) -> list[list[str]]:
    adjacency: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        if edge["relation"] == "prerequisite_of":
            adjacency[edge["source"]].append(edge["target"])
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []
    cycles: list[list[str]] = []

    def visit(node: str) -> None:
        if node in visiting:
            start = stack.index(node)
            cycles.append(stack[start:] + [node])
            return
        if node in visited:
            return
        visiting.add(node)
        stack.append(node)
        for target in adjacency[node]:
            visit(target)
        stack.pop()
        visiting.remove(node)
        visited.add(node)

    for node in sorted(nodes):
        visit(node)
    return cycles


def main() -> int:
    args = parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    bank = json.loads(args.bank.read_text(encoding="utf-8"))
    nodes = spec["nodes"]
    edges = spec["edges"]
    node_ids = [node["id"] for node in nodes]
    domains = {domain["id"] for domain in spec["domains"]}
    domain_counts = Counter(node["domain"] for node in nodes)
    topics = [topic for node in nodes for topic in node.get("question_topics", [])]
    bank_topics = {item["topic"] for item in bank}
    degree = Counter(
        endpoint for edge in edges for endpoint in (edge["source"], edge["target"])
    )
    checks = {
        "node_ids_unique": len(node_ids) == len(set(node_ids)),
        "all_domains_used": set(domain_counts) == domains and min(domain_counts.values()) >= 3,
        "topic_mapping_unique": len(topics) == len(set(topics)),
        "all_question_topics_mapped": bank_topics == set(topics),
        "edge_ids_unique": len({edge["id"] for edge in edges}) == len(edges),
        "edge_endpoints_exist": all(
            edge["source"] in node_ids and edge["target"] in node_ids for edge in edges
        ),
        "all_nodes_connected": all(degree[node_id] > 0 for node_id in node_ids),
        "prerequisite_graph_acyclic": not prerequisite_cycles(set(node_ids), edges),
        "full_course_size": len(nodes) >= 60 and len(edges) >= len(nodes),
    }
    result = {
        "version": spec["version"],
        "passed": all(checks.values()),
        "checks": checks,
        "domains": dict(domain_counts),
        "nodes": len(nodes),
        "edges": len(edges),
        "question_topics": len(bank_topics),
        "missing_question_topics": sorted(bank_topics - set(topics)),
        "unmapped_taxonomy_topics": sorted(set(topics) - bank_topics),
        "isolated_nodes": sorted(node_id for node_id in node_ids if degree[node_id] == 0),
        "prerequisite_cycles": prerequisite_cycles(set(node_ids), edges),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
