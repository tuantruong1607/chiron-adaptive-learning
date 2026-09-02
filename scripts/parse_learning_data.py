# -*- coding: utf-8 -*-
"""Build Chiron's auditable Markdown corpus from course PDFs and lesson HTML.

Text-layer extraction is preferred. OCR is page-selective and only attempted when
the extracted text is too sparse. LLMs are intentionally not required: this stage
preserves source truth; concept extraction/enrichment belongs downstream.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

from lxml import etree, html
from pypdf import PdfReader

COURSE_ID = "rag-intensive"
PARSER_VERSION = "chiron-structured-markdown-v1"
SLIDE_DIR = Path(r"C:\Users\banka\Documents\slide bài học")
LESSON_HTML_DIR = Path(r"C:\Users\banka\Documents\Multi Agent\ontap\out")
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SLIDES_OUT = DATA / "processed" / "markdown" / "slides"
LESSONS_OUT = DATA / "processed" / "markdown" / "lessons"
MANIFESTS_OUT = DATA / "manifests"
PAGE_IMAGES_OUT = DATA / "processed" / "assets" / "page-images"

# Page-one text is occasionally clipped by a PDF's visual layout. Keep these
# source-file keyed corrections explicit and auditable rather than relying on
# fuzzy title matching downstream.
DOCUMENT_TITLE_OVERRIDES = {
    "track 2 - day 20.pdf": "Model Serving & Inference",
    "track 2 - day 27.pdf": "Data Observability",
    "track 3 - day 21.pdf": "Fine-tuning LLMs — Từ Full Fine-tuning đến LoRA/QLoRA",
    "track 3 - day 25.pdf": "Circuit Breakers, Caching & Reliability",
    "track 3- day 20.pdf": "Multi-Agent Systems",
}


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def text_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def stable_id(kind: str, digest: str) -> str:
    return str(uuid5(NAMESPACE_URL, "chiron:%s:%s:%s" % (COURSE_ID, kind, digest)))


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-") or "document"


def norm(value: str) -> str:
    value = (value or "").replace("\u00a0", " ").replace("\u200b", "")
    value = re.sub(r"[ \t\r\f\v]+", " ", value)
    value = re.sub(r"\s+([,.;:!?%])", r"\1", value)
    return value.strip()


def yaml_value(value) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def title_from(lines: list[str], fallback: str) -> str:
    for raw in lines[:24]:
        line = norm(raw).strip("#*-–— ·")
        if 4 <= len(line) <= 160 and not re.fullmatch(r"[\d\s/·.,-]+", line):
            return line
    return fallback


def locate_binary(name: str) -> str | None:
    found = shutil.which(name)
    if found:
        return found
    poppler = Path(r"C:\Users\banka\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin")
    candidate = poppler / (name + ".exe")
    if candidate.exists():
        return str(candidate)
    if name == "tesseract":
        installed = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
        if installed.exists():
            return str(installed)
    return None


def ocr_page(pdf: Path, page_number: int, language: str) -> tuple[str, str]:
    pdftoppm, tesseract = locate_binary("pdftoppm"), locate_binary("tesseract")
    if not pdftoppm or not tesseract:
        return "", "ocr-unavailable"
    with tempfile.TemporaryDirectory(prefix="chiron-ocr-") as tmp:
        prefix = str(Path(tmp) / "page")
        subprocess.run([pdftoppm, "-f", str(page_number), "-l", str(page_number),
                        "-r", "220", "-png", "-singlefile", str(pdf), prefix],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        image = prefix + ".png"
        ocr_env = dict(os.environ)
        local_tessdata = DATA / "ocr" / "tessdata"
        if local_tessdata.exists():
            ocr_env["TESSDATA_PREFIX"] = str(local_tessdata)
        for lang in (language, "eng"):
            proc = subprocess.run([tesseract, image, "stdout", "-l", lang, "--psm", "6"],
                                  check=False, capture_output=True, text=True, encoding="utf-8", errors="replace",
                                  env=ocr_env)
            if proc.returncode == 0 and len(norm(proc.stdout)) >= 20:
                return proc.stdout, "ocr-tesseract-%s" % lang
    return "", "ocr-failed"


def render_page_asset(pdf: Path, page_number: int, digest: str) -> Path | None:
    pdftoppm = locate_binary("pdftoppm")
    if not pdftoppm:
        return None
    folder = PAGE_IMAGES_OUT / digest[:12]
    folder.mkdir(parents=True, exist_ok=True)
    output = folder / ("page-%04d.png" % page_number)
    prefix = str(output.with_suffix(""))
    subprocess.run([pdftoppm, "-f", str(page_number), "-l", str(page_number), "-r", "160",
                    "-png", "-singlefile", str(pdf), prefix], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    return output if output.exists() else None


def structured_page(text: str, page_number: int) -> tuple[str, str]:
    lines = [norm(line) for line in (text or "").splitlines()]
    lines = [line for line in lines if line]
    title = title_from(lines, "Slide %d" % page_number)
    output, used_title, code = [], False, False
    for line in lines:
        if not used_title and line == title:
            used_title = True
            continue
        looks_code = bool(re.search(r"(?:^|\s)(?:def |class |import |from |SELECT |curl |docker |pip |uv |npm |const |let |var |return |if\s*\(|\{\s*$)", line))
        if looks_code and not code:
            output.extend(["", "```text"]); code = True
        elif code and not looks_code and len(line) < 100 and not re.search(r"[{}();=]", line):
            output.append("```"); code = False
        if code:
            output.append(line); continue
        bullet = re.match(r"^[■●•▪□✓✔✗✕→▶►◆◇○]\s*(.*)$", line)
        ordered = re.match(r"^(\d{1,2})[.)]\s+(.+)$", line)
        if bullet:
            output.extend(["", "- " + bullet.group(1).strip()])
        elif ordered:
            output.extend(["", ordered.group(1) + ". " + ordered.group(2).strip()])
        elif len(line) <= 90 and line.endswith(":"):
            output.extend(["", "### " + line.rstrip(":")])
        elif output and output[-1] and not output[-1].startswith(("- ", "```", "### ")):
            output[-1] += " " + line
        else:
            output.append(line)
    if code:
        output.append("```")
    return title, "\n".join(output).strip()


def pdf_document(source: Path, output: Path, digest: str, ocr_mode: str, ocr_language: str):
    reader = PdfReader(str(source))
    document_id = stable_id("document", digest)
    version_id = stable_id("document-version", digest)
    blocks, spans, methods, sparse_pages = [], [], Counter(), []
    first_title = None
    for page_number, page in enumerate(reader.pages, 1):
        extracted = page.extract_text() or ""
        method = "pdf-text-layer"
        sparse = len(norm(extracted)) < 40
        if ocr_mode == "always" or (ocr_mode == "auto" and sparse):
            ocr_text, ocr_method = ocr_page(source, page_number, ocr_language)
            if len(norm(ocr_text)) > len(norm(extracted)):
                extracted, method = ocr_text, ocr_method
            elif sparse:
                method = ocr_method if ocr_method != "ocr-failed" else "pdf-text-layer-sparse"
        still_sparse = len(norm(extracted)) < 40
        if still_sparse:
            sparse_pages.append(page_number)
        methods[method] += 1
        slide_title, body = structured_page(extracted, page_number)
        if first_title is None and not slide_title.startswith("Slide "):
            first_title = slide_title
        span_checksum = text_hash(extracted)
        span_id = stable_id("source-span", "%s:page:%d:%s" % (digest, page_number, span_checksum))
        locator = {"kind": "page", "page": page_number, "label": "Slide %d" % page_number,
                   "section_title": slide_title, "extraction_method": method}
        if still_sparse:
            page_image = render_page_asset(source, page_number, digest)
            if page_image:
                relative_image = Path(os.path.relpath(page_image, output.parent)).as_posix()
                locator["page_image"] = relative_image
                locator["visual_fallback"] = True
                visual = "![Visual fallback - %s - slide %d](%s)\n\n> Trang này được giữ dưới dạng ảnh vì text layer/OCR không đủ để biểu diễn nội dung trực quan." % (source.stem, page_number, relative_image)
                body = (body + "\n\n" + visual).strip()
        spans.append({"source_span_id": span_id, "document_version_id": version_id,
                      "document_id": document_id, "course_id": COURSE_ID, "source_type": "course_pdf",
                      "locator": locator, "checksum": span_checksum, "text": extracted.strip()})
        meta = json.dumps({"source_span_id": span_id, "locator": locator,
                           "checksum": span_checksum}, ensure_ascii=False, separators=(",", ":"))
        blocks.append('<!-- chiron-source-span: %s -->\n\n## Slide %d - %s\n\n%s' %
                      (meta, page_number, slide_title, body or "_[Trang không có text layer và OCR không cung cấp thêm văn bản.]_"))
    title = DOCUMENT_TITLE_OVERRIDES.get(source.name, first_title or source.stem)
    method_json = json.dumps(dict(methods), ensure_ascii=False, separators=(",", ":"))
    front = ["---", "schema_version: 1", "course_id: " + COURSE_ID,
             "document_id: " + yaml_value(document_id), "document_version_id: " + yaml_value(version_id),
             "document_kind: slide_deck", "source_type: course_pdf", "authority: primary",
             "title: " + yaml_value(title), "source_file: " + yaml_value(source.name),
             "source_path: " + yaml_value(str(source)), "source_sha256: " + yaml_value(digest),
             "parser_version: " + PARSER_VERSION, "page_count: %d" % len(reader.pages),
             "sparse_page_count: %d" % len(sparse_pages), "extraction_methods: " + yaml_value(method_json),
             "language: vi", "---"]
    intro = "# %s\n\n> Nguồn authoritative: slide PDF. Mỗi heading `Slide N` là một source span ổn định cho citation và chunking." % title
    output.write_text("\n".join(front) + "\n\n" + intro + "\n\n" + "\n\n---\n\n".join(blocks) + "\n", encoding="utf-8")
    entry = {"kind": "slide_deck", "source_type": "course_pdf", "authority": "primary",
             "source": str(source), "output": str(output), "source_sha256": digest,
             "document_id": document_id, "document_version_id": version_id, "title": title,
             "pages": len(reader.pages), "source_spans": len(spans), "sparse_pages": sparse_pages,
             "extraction_methods": dict(methods), "bytes_markdown": output.stat().st_size, "status": "ok"}
    return entry, spans


SKIP_TAGS = {"script", "style", "noscript", "template"}


def node_text(node) -> str:
    return norm(" ".join(node.itertext()))


def inline(node) -> str:
    if isinstance(node, etree._Comment):
        return ""
    tag = node.tag.lower() if isinstance(node.tag, str) else ""
    if tag in SKIP_TAGS:
        return ""
    parts = [norm(node.text)] if node.text else []
    for child in node:
        ctag = child.tag.lower() if isinstance(child.tag, str) else ""
        content = inline(child)
        if ctag in ("strong", "b") and content:
            content = "**%s**" % content
        elif ctag in ("em", "i") and content:
            content = "*%s*" % content
        elif ctag == "code" and content:
            content = "`%s`" % content.replace("`", "\\`")
        elif ctag == "a" and content:
            href = child.get("href", "")
            content = "[%s](%s)" % (content, href) if href else content
        elif ctag == "br":
            content = "  \n"
        elif ctag == "img":
            content = "![%s](%s)" % (child.get("alt", "image"), child.get("src", ""))
        elif ctag == "input":
            content = ""
        if content:
            parts.append(content)
        if child.tail and norm(child.tail):
            parts.append(norm(child.tail))
    return norm(" ".join(parts)).replace("  \n ", "  \n")


def markdown_table(node) -> str:
    rows = []
    for tr in node.xpath(".//tr"):
        cells = [node_text(cell).replace("|", "\\|") for cell in tr.xpath("./th|./td")]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    header, rest = rows[0], rows[1:]
    return "\n".join(["| " + " | ".join(header) + " |",
                      "| " + " | ".join(["---"] * width) + " |"] +
                     ["| " + " | ".join(row) + " |" for row in rest])


def block(node) -> str:
    if isinstance(node, etree._Comment):
        return ""
    tag = node.tag.lower() if isinstance(node.tag, str) else ""
    classes = set((node.get("class") or "").split())
    if tag in SKIP_TAGS or tag in ("footer", "aside") or (tag == "nav"):
        return ""
    if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        return "#" * int(tag[1]) + " " + node_text(node)
    if tag == "p":
        return inline(node)
    if tag == "blockquote":
        value = node_text(node)
        return "\n".join("> " + line for line in value.splitlines())
    if tag in ("ul", "ol"):
        ordered = tag == "ol"
        items = []
        for index, li in enumerate(node.xpath("./li"), 1):
            items.append((str(index) + ". " if ordered else "- ") + node_text(li))
        return "\n".join(items)
    if tag == "table":
        return markdown_table(node)
    if tag == "pre":
        return "```text\n%s\n```" % (node.text_content().strip())
    if tag == "details":
        summary = node.xpath("./summary")
        title = node_text(summary[0]) if summary else "Chi tiết"
        rest = "\n\n".join(block(child) for child in node if child.tag != "summary" and block(child))
        return "#### %s\n\n%s" % (title, rest)
    if tag == "dl":
        result = []
        for child in node:
            if child.tag == "dt":
                result.append("**%s**" % node_text(child))
            elif child.tag == "dd":
                result.append(": %s" % node_text(child))
        return "\n\n".join(result)
    if "ctrl" in classes:
        label = node.xpath(".//label")
        control = node.xpath(".//input[@type='range']")
        if control:
            c = control[0]
            return "- **Control - %s**: min `%s`, max `%s`, step `%s`, default `%s`" % (
                node_text(label[0]) if label else c.get("id", "range"), c.get("min", ""),
                c.get("max", ""), c.get("step", ""), c.get("value", ""))
    if tag == "svg":
        title = node.xpath(".//*[local-name()='title']|.//*[local-name()='desc']")
        return "_Sơ đồ: %s_" % " - ".join(node_text(x) for x in title) if title else ""
    child_blocks = [block(child) for child in node]
    child_blocks = [value for value in child_blocks if value]
    if child_blocks:
        return "\n\n".join(child_blocks)
    value = inline(node)
    return value if value and tag not in ("input", "span") else ""


def html_document(source: Path, output: Path, digest: str):
    parser = html.HTMLParser(encoding="utf-8", recover=True)
    tree = html.fromstring(source.read_bytes(), parser=parser)
    for bad in tree.xpath("//script|//style|//noscript|//template|//nav|//aside|//footer"):
        parent = bad.getparent()
        if parent is not None:
            parent.remove(bad)
    title_nodes = tree.xpath("//h1")
    title = node_text(title_nodes[0]) if title_nodes else source.stem
    document_id = stable_id("document", digest)
    version_id = stable_id("document-version", digest)
    hero_sub = tree.xpath("//header[contains(concat(' ',normalize-space(@class),' '),' hero ')]//p")
    intro = node_text(hero_sub[0]) if hero_sub else ""
    main_nodes = tree.xpath("//main")
    main = main_nodes[0] if main_nodes else tree
    top_nodes = main.xpath("./section|./article|./div") or list(main)
    blocks, spans = [], []
    for order, section in enumerate(top_nodes, 1):
        rendered = block(section).strip()
        if not rendered:
            continue
        heading = section.xpath(".//h1|.//h2|.//h3|.//h4")
        heading_text = node_text(heading[0]) if heading else "Section %d" % order
        section_id = section.get("id") or "section-%03d" % order
        source_text = node_text(section)
        checksum = text_hash(source_text)
        span_id = stable_id("source-span", "%s:section:%s:%s" % (digest, section_id, checksum))
        locator = {"kind": "html_section", "section_id": section_id, "order": order,
                   "heading": heading_text, "source_file": source.name}
        spans.append({"source_span_id": span_id, "document_version_id": version_id,
                      "document_id": document_id, "course_id": COURSE_ID, "source_type": "course_html",
                      "locator": locator, "checksum": checksum, "text": source_text})
        meta = json.dumps({"source_span_id": span_id, "locator": locator,
                           "checksum": checksum}, ensure_ascii=False, separators=(",", ":"))
        blocks.append("<!-- chiron-source-span: %s -->\n\n%s" % (meta, rendered))
    module_count = len(tree.xpath("//*[contains(concat(' ',normalize-space(@class),' '),' mod ')]"))
    control_count = len(tree.xpath("//input[@type='range']"))
    quote_count = len(tree.xpath("//blockquote"))
    front = ["---", "schema_version: 1", "course_id: " + COURSE_ID,
             "document_id: " + yaml_value(document_id), "document_version_id: " + yaml_value(version_id),
             "document_kind: interactive_lesson", "source_type: course_html", "authority: primary",
             "title: " + yaml_value(title), "source_file: " + yaml_value(source.name),
             "source_path: " + yaml_value(str(source)), "source_sha256: " + yaml_value(digest),
             "parser_version: " + PARSER_VERSION, "html_section_count: %d" % len(spans),
             "interactive_module_count: %d" % module_count, "interactive_control_count: %d" % control_count,
             "language: vi", "---"]
    header = "# %s" % title + ("\n\n> %s" % intro if intro else "")
    output.write_text("\n".join(front) + "\n\n" + header + "\n\n" + "\n\n---\n\n".join(blocks) + "\n", encoding="utf-8")
    entry = {"kind": "interactive_lesson", "source_type": "course_html", "authority": "primary",
             "source": str(source), "output": str(output), "source_sha256": digest,
             "document_id": document_id, "document_version_id": version_id, "title": title,
             "sections": len(spans), "source_spans": len(spans), "interactive_modules": module_count,
             "interactive_controls": control_count, "blockquotes": quote_count,
             "bytes_markdown": output.stat().st_size, "status": "ok"}
    return entry, spans


def unique_output(stem: str, digest: str, used: set[str]) -> str:
    base = slugify(stem)
    candidate = base
    if candidate in used:
        candidate = "%s-%s" % (base, digest[:8])
    serial = 2
    while candidate in used:
        candidate = "%s-%s-%d" % (base, digest[:8], serial); serial += 1
    used.add(candidate)
    return candidate + ".md"


def write_manifests(entries: list[dict], spans: list[dict]) -> None:
    generated = datetime.now(timezone.utc).isoformat()
    by_hash: dict[str, str] = {}
    for entry in entries:
        digest = entry["source_sha256"]
        if digest in by_hash:
            entry["duplicate_of"] = by_hash[digest]
        else:
            by_hash[digest] = entry["source"]
    manifest = {"schema_version": 1, "course_id": COURSE_ID, "parser_version": PARSER_VERSION,
                "generated_at": generated, "source_roots": {"slides": str(SLIDE_DIR), "html": str(LESSON_HTML_DIR)},
                "summary": {"documents": len(entries), "slide_decks": sum(e["kind"] == "slide_deck" for e in entries),
                            "interactive_lessons": sum(e["kind"] == "interactive_lesson" for e in entries),
                            "source_spans": len(spans), "duplicates": sum("duplicate_of" in e for e in entries),
                            "errors": sum(e["status"] != "ok" for e in entries)}, "documents": entries}
    (MANIFESTS_OUT / "corpus.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (MANIFESTS_OUT / "source_spans.jsonl").open("w", encoding="utf-8") as stream:
        for span in spans:
            stream.write(json.dumps(span, ensure_ascii=False, separators=(",", ":")) + "\n")
    rows = []
    for e in entries:
        count = e.get("pages", e.get("sections", 0))
        duplicate = e.get("duplicate_of", "")
        rows.append("| %s | %s | %s | %s | %s |" %
                    (e["source_type"], e["title"].replace("|", "\\|"), count,
                     Path(e["output"]).relative_to(DATA).as_posix(), duplicate.replace("|", "\\|")))
    report = """# Chiron parsed learning corpus

- Course: `%s`
- Parser: `%s`
- Documents: **%d**
- Source spans: **%d**
- Duplicate binaries: **%d**
- Errors: **%d**

| Type | Title | Pages/sections | Markdown | Duplicate of |
| --- | --- | ---: | --- | --- |
%s
""" % (COURSE_ID, PARSER_VERSION, len(entries), len(spans),
         sum("duplicate_of" in e for e in entries), sum(e["status"] != "ok" for e in entries), "\n".join(rows))
    (MANIFESTS_OUT / "corpus.md").write_text(report, encoding="utf-8")


def write_readme(entries: list[dict], spans: list[dict], ocr_mode: str) -> None:
    pdf_entries = [entry for entry in entries if entry.get("kind") == "slide_deck" and entry.get("status") == "ok"]
    ocr_pages = sum(value for entry in pdf_entries for method, value in entry.get("extraction_methods", {}).items()
                    if method.startswith("ocr-tesseract"))
    sparse_pages = sum(len(entry.get("sparse_pages", [])) for entry in pdf_entries)
    text = """# Chiron data corpus

This directory contains the auditable Markdown staging corpus for course `%s`.

## Layout

- `processed/markdown/slides/`: authoritative PDF decks, one Markdown file per binary source.
- `processed/markdown/lessons/`: authoritative interactive lesson HTML converted to semantic Markdown.
- `processed/assets/page-images/`: visual fallback for pages whose text layer and OCR remain sparse.
- `manifests/corpus.json`: document-level IDs, checksums, extraction metrics, and duplicate mapping.
- `manifests/source_spans.jsonl`: page/section records matching Chiron's `source_spans` persistence boundary.

## Ingestion invariants

- `document_version_id` and `source_span_id` are deterministic UUIDv5 values.
- Every source span has a locator and SHA-256 checksum.
- PDF page boundaries and HTML section boundaries are explicit in Markdown comments.
- Text-layer extraction is preferred. OCR mode for this run: `%s`.
- OCR never overwrites a richer text layer; it is selected only when it yields more text.
- Sparse visual pages retain a PNG reference in both Markdown and the source-span locator.
- OCR language data is stored under `ocr/tessdata/` for reproducible Vietnamese-English extraction.
- No LLM rewrites source text during parsing. Concept/relationship extraction is downstream and must retain source-span provenance.

## Current corpus

- Documents: %d
- Source spans: %d
- Pages improved by OCR: %d
- Pages still sparse after text/OCR inspection: %d (typically visual dividers or image-only pages; locators are retained)
""" % (COURSE_ID, ocr_mode, len(entries), len(spans), ocr_pages, sparse_pages)
    (DATA / "README.md").write_text(text, encoding="utf-8")


def validate(entries: list[dict], spans: list[dict]) -> list[str]:
    errors = []
    ids = [s["source_span_id"] for s in spans]
    if len(ids) != len(set(ids)):
        errors.append("duplicate source_span_id")
    for entry in entries:
        if entry["status"] != "ok":
            errors.append("parse failed: " + entry["source"])
            continue
        out = Path(entry["output"])
        text = out.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "document_version_id:" not in text:
            errors.append("missing frontmatter: " + str(out))
        if entry["kind"] == "slide_deck" and text.count("<!-- chiron-source-span:") != entry["pages"]:
            errors.append("page/span mismatch: " + str(out))
        if entry["kind"] == "interactive_lesson" and re.search(r"<(?:script|style)\b", text, re.I):
            errors.append("script/style leaked: " + str(out))
    return errors


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--ocr", choices=("auto", "never", "always"), default="auto")
    ap.add_argument("--ocr-language", default="vie+eng")
    args = ap.parse_args()
    for folder in (SLIDES_OUT, LESSONS_OUT, MANIFESTS_OUT, PAGE_IMAGES_OUT):
        folder.mkdir(parents=True, exist_ok=True)
    entries, spans = [], []
    used_slides, used_lessons = set(), set()
    pdfs = sorted(SLIDE_DIR.rglob("*.pdf"), key=lambda p: p.name.lower())
    htmls = sorted(LESSON_HTML_DIR.glob("*.html"), key=lambda p: p.name.lower())
    for index, source in enumerate(pdfs, 1):
        digest = file_hash(source); name = unique_output(source.stem, digest, used_slides)
        print("PDF %02d/%02d  %s" % (index, len(pdfs), source.name), flush=True)
        try:
            entry, page_spans = pdf_document(source, SLIDES_OUT / name, digest, args.ocr, args.ocr_language)
            entries.append(entry); spans.extend(page_spans)
        except Exception as exc:
            entries.append({"kind": "slide_deck", "source_type": "course_pdf", "source": str(source),
                            "output": str(SLIDES_OUT / name), "source_sha256": digest,
                            "title": source.stem, "status": "error: %s: %s" % (type(exc).__name__, exc)})
    for index, source in enumerate(htmls, 1):
        digest = file_hash(source); name = unique_output(source.stem, digest, used_lessons)
        print("HTML %02d/%02d %s" % (index, len(htmls), source.name), flush=True)
        try:
            entry, html_spans = html_document(source, LESSONS_OUT / name, digest)
            entries.append(entry); spans.extend(html_spans)
        except Exception as exc:
            entries.append({"kind": "interactive_lesson", "source_type": "course_html", "source": str(source),
                            "output": str(LESSONS_OUT / name), "source_sha256": digest,
                            "title": source.stem, "status": "error: %s: %s" % (type(exc).__name__, exc)})
    spans = list({span["source_span_id"]: span for span in spans}.values())
    write_manifests(entries, spans); write_readme(entries, spans, args.ocr)
    errors = validate(entries, spans)
    print("\n%d documents, %d source spans, %d validation errors" % (len(entries), len(spans), len(errors)))
    for error in errors:
        print("X " + error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
