"""Deterministically shuffle objective options and rewrite answer labels."""
from __future__ import annotations

import random
import re
import sys
from collections import Counter
from pathlib import Path

QUESTION = re.compile(r"(?ms)(^### (\d+)\..*?)(?=^### |^## Constructed|\Z)")
OPTION = re.compile(r"^- ([A-D])\. (.+)$", re.M)
ANSWER = re.compile(r"(\*\*Đáp án:\*\* )([A-D](?:, [A-D])*)(\.)")


def shuffle(text: str, seed: int) -> tuple[str, Counter[str], int]:
    rng = random.Random(seed)
    keys: list[str] = []
    def question(match: re.Match[str]) -> str:
        block = match.group(1)
        options = OPTION.findall(block)
        answer = ANSWER.search(block)
        if len(options) != 4 or answer is None:
            return block
        shuffled = options[:]
        rng.shuffle(shuffled)
        mapping = {old_label: "ABCD"[index] for index, (old_label, _text) in enumerate(shuffled)}
        option_iter = iter(enumerate(shuffled))

        def replace_option(_match: re.Match[str]) -> str:
            index, (_old_label, option_text) = next(option_iter)
            return f"- {'ABCD'[index]}. {option_text}"

        block = OPTION.sub(replace_option, block)
        new_keys = [mapping[key] for key in answer.group(2).split(", ")]
        keys.extend(new_keys)
        return ANSWER.sub(lambda m: f"{m.group(1)}{', '.join(sorted(new_keys))}{m.group(3)}", block, count=1)
    updated = QUESTION.sub(question, text)
    max_run = 0; run = 0; previous = ""
    for key in keys:
        run = run + 1 if key == previous else 1
        max_run = max(max_run, run); previous = key
    return updated, Counter(keys), max_run


def main() -> None:
    path = Path(sys.argv[1]); source = path.read_text(encoding="utf-8")
    for seed in range(10_000):
        updated, counts, max_run = shuffle(source, seed)
        if all(6 <= counts[key] <= 9 for key in "ABCD") and max_run <= 3:
            path.write_text(updated, encoding="utf-8")
            print({"seed": seed, "counts": dict(counts), "max_run": max_run})
            return
    raise RuntimeError("Could not find a balanced deterministic permutation")


if __name__ == "__main__":
    main()
