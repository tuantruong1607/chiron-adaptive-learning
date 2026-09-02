"""Fail-closed validator cho ngân hàng câu hỏi Markdown.

Thực thi các luật trong docs/QUESTION_AUTHORING_CONTRACT.md. Exit 0 nghĩa là item
đạt; mọi exit khác 0 liệt kê defect kèm mã luật để agent sửa đúng chỗ.

    python scripts/validate_question_bank.py data/questions/review/pilot-v1.md
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPANS = ROOT / "data" / "manifests" / "source_spans.jsonl"

QUESTION = re.compile(r"(?ms)^### (\d+)\.(.*?)(?=^### |^## Review checklist|\Z)")
# Cố ý nhận cả A-E dù form chỉ dùng A-D: option/đáp án thừa phải bị BẮT, không bị bỏ qua.
OPTION = re.compile(r"^- ([A-E])\. (.+)$", re.M)
ANSWER = re.compile(r"^\*\*Đáp án:\*\* ([A-E](?:, [A-E])*)\.", re.M)
EVIDENCE = re.compile(r"^\*\*Evidence:\*\* (.+)$", re.M)
SPAN_ID = re.compile(r"`([0-9a-fA-F-]{20,})`")
META = re.compile(r"^> \*\*Metadata:\*\* (.+)$", re.M)

# Luật 2.4 / 3.2
MAX_LENGTH_RATIO = 1.3
LENGTH_FLOOR = 25
MIN_SPAN_CHARS = 260
POSITION_SKEW = 2

# Luật 3.1 — slide điều hướng, không phải nội dung
NAVIGATION = re.compile(
    r"^\s*(mục\s*lục|nội\s*dung\s*bài\s*học|mục\s*tiêu|agenda|hỏi\s*&\s*đáp"
    r"|cảm\s*ơn|tài\s*liệu\s*tham\s*khảo|references|tổng\s*kết)",
    re.I,
)


@dataclass
class Item:
    number: int
    body: str
    options: list[tuple[str, str]]
    answer: list[str]
    meta: dict[str, str]
    span_ids: list[str]
    evidence_line: str = ""
    findings: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def parse(text: str) -> list[Item]:
    items: list[Item] = []
    for match in QUESTION.finditer(text):
        body = match.group(2)
        answer = ANSWER.search(body)
        evidence = EVIDENCE.search(body)
        meta_match = META.search(body)
        meta: dict[str, str] = {}
        if meta_match:
            for pair in re.findall(r"`([^`=]+)=([^`]*)`", meta_match.group(1)):
                meta[pair[0].strip()] = pair[1].strip()
        items.append(
            Item(
                number=int(match.group(1)),
                body=body,
                options=OPTION.findall(body),
                answer=[x.strip() for x in answer.group(1).split(",")] if answer else [],
                meta=meta,
                span_ids=SPAN_ID.findall(evidence.group(1)) if evidence else [],
                evidence_line=evidence.group(1) if evidence else "",
            )
        )
    return items


def load_spans(path: Path) -> dict[str, dict]:
    spans: dict[str, dict] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            spans[row["source_span_id"]] = row
    return spans


def check_item(item: Item, spans: dict[str, dict], is_objective: bool) -> None:
    add = item.findings.append
    warn = item.warnings.append

    for key in ("topic", "cognitive_level", "difficulty"):
        if key not in item.meta:
            add(f"[R5] thiếu metadata `{key}`")
    level = item.meta.get("cognitive_level")
    if level and level not in {"recall", "understand", "apply", "analyze"}:
        add(f"[R5] cognitive_level không hợp lệ: {level}")

    # Luật 0 / 3 — evidence
    if not item.span_ids:
        add("[R0] không có source_span_id")
    for sid in item.span_ids:
        span = spans.get(sid)
        if span is None:
            add(f"[R0] source_span_id không tồn tại trong manifest: {sid}")
            continue
        text = span["text"].strip()
        if NAVIGATION.match(text):
            add(f"[R3.1] evidence trỏ slide điều hướng: {text[:60]!r}")
        elif len(text) < MIN_SPAN_CHARS:
            # R3.2 cho phép span ngắn khi nó chứa nguyên văn mệnh đề đáp án dựa vào.
            # Máy không phán được điều đó, nên đây là cảnh báo để người review xác nhận.
            warn(f"[R3.2] span mỏng ({len(text)} ký tự) — xác nhận thủ công: {text[:60]!r}")
    if not is_objective:
        # Tự luận tái sử dụng span của câu objective nên chỉ liệt kê ID trần.
        return

    if item.span_ids and "slide" not in item.evidence_line and "—" not in item.evidence_line:
        add("[R3.4] evidence thiếu title/locator để mở lại")

    labels = [label for label, _ in item.options]
    if labels != sorted(labels):
        add(f"[R1] nhãn option không theo thứ tự: {''.join(labels)}")
    if len(set(labels)) != len(labels):
        add("[R1] nhãn option trùng")
    if not item.answer:
        add("[R1] thiếu dòng Đáp án")
        return
    for label in item.answer:
        if label not in labels:
            add(f"[R1] đáp án {label} không có trong danh sách option")

    # Form đề chỉ có một đáp án đúng: multi-select đã bị bỏ khỏi objective_blueprint.
    if len(item.answer) > 1:
        add(f"[R1] objective phải có đúng 1 đáp án, đang {len(item.answer)}: {', '.join(item.answer)}")
    if len(item.options) != 4:
        add(f"[R1] objective phải có 4 option, đang {len(item.options)}")

    lengths = {label: len(text) for label, text in item.options}
    considered = [v for v in lengths.values() if v >= LENGTH_FLOOR]
    if len(considered) == len(lengths) and considered:
        ratio = max(considered) / min(considered)
        if ratio > MAX_LENGTH_RATIO:
            add(f"[R2.4] chênh lệch độ dài option {ratio:.2f}× > {MAX_LENGTH_RATIO}×")

    if not re.search(r"^\*\*Đáp án:\*\*.*  $", item.body, re.M):
        add("[R1] dòng Đáp án thiếu hai dấu cách cuối dòng")


def check_bank(items: list[Item], objective: list[Item]) -> list[str]:
    errors: list[str] = []

    # Luật 2.4 — vị trí đáp án đúng
    positions = Counter()
    longest_is_key = 0
    single = [i for i in objective if len(i.answer) == 1]
    for item in single:
        labels = [label for label, _ in item.options]
        if item.answer[0] in labels:
            positions[labels.index(item.answer[0]) + 1] += 1
        longest = max(item.options, key=lambda o: len(o[1]))[0]
        if longest == item.answer[0]:
            longest_is_key += 1
    if positions and max(positions.values()) - min(positions.values()) > POSITION_SKEW:
        errors.append(f"[R2.4] vị trí đáp án đúng lệch: {dict(sorted(positions.items()))}")
    if single and longest_is_key > len(single) / 2:
        errors.append(
            f"[R2.4] đáp án đúng là option dài nhất ở {longest_is_key}/{len(single)} câu "
            f"(ngẫu nhiên ~{len(single) // 4})"
        )

    # Luật 4 — rò rỉ giữa các câu
    def rel(item: Item) -> set[str]:
        raw = item.meta.get("mutually_exclusive_with", "none")
        return set() if raw == "none" else {x.strip() for x in raw.split(",") if x.strip()}

    by_name = {f"Q{i.number}": i for i in objective}
    for name, item in by_name.items():
        for other in rel(item):
            if other not in by_name:
                errors.append(f"[R4] {name} trỏ tới câu không tồn tại: {other}")
            elif name not in rel(by_name[other]):
                errors.append(f"[R4] mutually_exclusive không đối xứng: {name} -> {other}")

    def tokens(text: str) -> set[str]:
        return {w for w in re.findall(r"[a-zA-ZÀ-ỹ_]{4,}", text.lower())}

    for a, b in itertools.combinations(by_name, 2):
        ia, ib = by_name[a], by_name[b]
        ga, gb = ia.meta.get("group", "none"), ib.meta.get("group", "none")
        if b in rel(ia) or (ga != "none" and ga == gb):
            continue
        overlap = sum(
            1
            for x in (tokens(t) for _, t in ia.options)
            for y in (tokens(t) for _, t in ib.options)
            if x and y and len(x & y) / len(x | y) > 0.45
        )
        if overlap >= 2:
            errors.append(f"[R4] {a} ~ {b}: {overlap} option gần trùng nhưng chưa cùng group")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--spans", type=Path, default=DEFAULT_SPANS)
    parser.add_argument("--objective-count", type=int, default=30)
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    spans = load_spans(args.spans)
    items = parse(text)
    if not items:
        print("Không parse được item nào — kiểm tra định dạng heading '### N.'")
        return 2

    objective = [i for i in items if i.number <= args.objective_count]
    for item in items:
        check_item(item, spans, is_objective=item.number <= args.objective_count)

    failures = 0
    warnings = 0
    for item in items:
        for finding in item.findings:
            print(f"Q{item.number}: {finding}")
            failures += 1
        for warning in item.warnings:
            print(f"Q{item.number}: WARN {warning}")
            warnings += 1
    for error in check_bank(items, objective):
        print(f"BANK: {error}")
        failures += 1

    summary = f"{len(items)} item ({len(objective)} objective), {len(spans)} span trong manifest"
    if failures:
        print(f"\nFAIL — {failures} defect, {warnings} cảnh báo. Xem docs/QUESTION_AUTHORING_CONTRACT.md theo mã luật.")
        return 1
    print(f"\nPASS — {summary}. {warnings} cảnh báo cần người review xác nhận.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
