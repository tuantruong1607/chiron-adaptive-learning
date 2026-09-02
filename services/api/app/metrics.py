from __future__ import annotations

import re
from collections import Counter
from threading import Lock

_UUID_PATH = re.compile(r"/[0-9a-fA-F]{8}-[0-9a-fA-F-]{27,}(?=/|$)")


class Metrics:
    def __init__(self) -> None:
        self._lock = Lock()
        self._counters: Counter[tuple[str, tuple[tuple[str, str], ...]]] = Counter()

    def increment(self, name: str, **labels: str) -> None:
        key = (name, tuple(sorted(labels.items())))
        with self._lock:
            self._counters[key] += 1

    def render(self, extra_lines: list[str] | None = None) -> str:
        with self._lock:
            rows = list(self._counters.items())
        lines = ["# TYPE chiron_requests_total counter"]
        for (name, labels), value in sorted(rows):
            label_text = ""
            if labels:
                label_text = "{" + ",".join(f'{key}="{value}"' for key, value in labels) + "}"
            lines.append(f"chiron_{name}{label_text} {value}")
        return "\n".join([*lines, *(extra_lines or [])]) + "\n"


def safe_path(path: str) -> str:
    return _UUID_PATH.sub("/:id/", path)


metrics = Metrics()
