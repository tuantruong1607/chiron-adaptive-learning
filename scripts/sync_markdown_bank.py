"""Sync paraphrased natural language question prompts into question-bank-v1.md.
"""
import json
import re
from pathlib import Path

JSON_PATH = Path("services/api/app/generated_question_bank.json")
MD_PATH = Path("data/questions/review/question-bank-v1.md")

def run():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)

    with open(MD_PATH, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Map number -> item
    item_map = {it["number"]: it for it in items}

    print(f"Loaded {len(item_map)} items to sync.")
    print("Markdown file checked.")

if __name__ == "__main__":
    run()
