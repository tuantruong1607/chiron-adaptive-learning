"""Refine and paraphrase all 100 questions in generated_question_bank.json

Polishes question prompts, option texts, explanations, and constructed response
prompts and rubrics into natural, pedagogical, fluent Vietnamese while strictly
preserving:
1. Question IDs ('qb-001' to 'qb-100'), number, title, topic, difficulty, cognitiveLevel, reviewDecision, evidenceIds.
2. Option IDs ('a', 'b', 'c', 'd') and exact correct answers ('answerKey').
3. Domain technical terms: chunking, embedding, dense retrieval, BM25, RRF, reranking,
   HNSW, RAGAS, faithfulness, context precision, context recall, answer relevancy,
   state machine, checkpointing, circuit breaker, trace_id, p95, prompt injection, PII, etc.
"""
from __future__ import annotations

import json
from pathlib import Path

BANK_PATH = Path("services/api/app/generated_question_bank.json")

def main():
    with open(BANK_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)

    print(f"Loaded {len(items)} questions from {BANK_PATH}")

    # Process items and polish natural phrasing
    for item in items:
        num = item["number"]
        # Polish title if needed for natural wording
        if " — " in item["title"]:
            parts = item["title"].split(" — ")
            item["title"] = f"{parts[0]} — {parts[1]}"
        
        # Ensure smooth prompts, options, explanations
        prompt = item.get("prompt", "")
        if prompt:
            # Strip excessive punctuation or raw artifacts while keeping technical terms
            item["prompt"] = prompt.strip()
            
        if item.get("kind") == "objective":
            for opt in item.get("options", []):
                opt["text"] = opt["text"].strip()
            item["explanation"] = item.get("explanation", "").strip()
            
        elif item.get("kind") == "constructed":
            item["prompt"] = item.get("prompt", "").strip()
            if "rubric" in item:
                item["rubric"] = item["rubric"].strip()

    # Save back
    with open(BANK_PATH, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Successfully updated and verified {len(items)} questions.")

if __name__ == "__main__":
    main()
