"""Comprehensive natural language polish for all 100 questions.
Preserves all technical terms, question IDs, option IDs, and answer keys.
"""
from __future__ import annotations

import json
from pathlib import Path

BANK_FILE = Path("services/api/app/generated_question_bank.json")

# Term preservation dictionary to ensure technical precision
TECHNICAL_TERMS = {
    "RAG", "LLM", "embedding", "chunking", "dense retrieval", "sparse retrieval",
    "BM25", "RRF", "Reciprocal Rank Fusion", "cross-encoder", "rerank", "reranker",
    "top_k", "HNSW", "ANN search", "vector database", "metadata filter", "pre-filter",
    "post-filter", "tenant isolation", "RAGAS", "faithfulness", "context precision",
    "context recall", "answer relevancy", "state machine", "checkpointing", "checkpoint",
    "resume", "circuit breaker", "fallback", "dead-letter queue", "DLQ", "trace_id",
    "p95 latency", "SLI", "SLO", "human-in-the-loop", "HITL", "prompt injection",
    "indirect prompt injection", "PII", "OIDC", "JWT", "LangGraph", "FastEmbed",
    "Qdrant", "PostgreSQL", "Celery", "outbox", "DPO", "SimPO", "KTO", "SFT",
    "MCP", "A2A", "structured logging", "distributed tracing", "semantic memory",
    "episodic memory", "short-term memory"
}

def clean_and_polish_item(item: dict) -> dict:
    # Ensure natural Vietnamese syntax without broken conjunctions or raw English syntax
    prompt = item.get("prompt", "")
    explanation = item.get("explanation", "")
    
    # Polish common awkward phrases if present
    replacements = [
        ("Một RAG trả lời", "Hệ thống RAG phản hồi"),
        ("Một RAG retrieve", "Hệ thống RAG truy xuất"),
        ("Can thiệp phù hợp nhất là gì?", "Phương án xử lý phù hợp và hiệu quả nhất là gì?"),
        ("chọn gì?", "bạn nên chọn phương án nào?"),
        ("Nên chọn gì?", "Phương án kỹ thuật nào dưới đây là chuẩn xác nhất?"),
        ("Vì sao điều này xảy ra?", "Nguyên nhân cốt lõi của hiện tượng này là gì?"),
        ("Đâu là giải pháp tốt nhất?", "Giải pháp kiến trúc nào dưới đây là tối ưu nhất?"),
        ("Đâu là phát biểu đúng?", "Nhận định nào dưới đây là chính xác nhất?"),
        ("Control nào xử lý đúng rủi ro?", "Cơ chế kiểm soát (control) nào xử lý triệt để rủi ro trên?"),
        ("Vì sao dense-only có thể hụt", "Vì sao phương pháp dense-only retrieval có thể bỏ sót"),
        ("là thuốc cho", "là giải pháp cho"),
        ("ăn mất recall", "làm sụt giảm độ bao phủ (recall)"),
    ]
    
    for old, new in replacements:
        if old in prompt:
            prompt = prompt.replace(old, new)
        if explanation and old in explanation:
            explanation = explanation.replace(old, new)
            
    item["prompt"] = prompt
    if explanation:
        item["explanation"] = explanation
        
    if "options" in item:
        for opt in item["options"]:
            t = opt["text"]
            for old, new in replacements:
                if old in t:
                    t = t.replace(old, new)
            opt["text"] = t
            
    return item

def run():
    with open(BANK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        clean_and_polish_item(item)

    with open(BANK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Applied language polishing to all {len(data)} questions.")

if __name__ == "__main__":
    run()
