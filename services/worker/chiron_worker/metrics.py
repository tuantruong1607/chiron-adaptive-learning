from __future__ import annotations

from prometheus_client import Counter, Gauge, Histogram, start_http_server

OUTBOX_EVENTS = Counter(
    "chiron_worker_outbox_events_total",
    "Outbox events handled by worker consumers",
    ("consumer", "outcome"),
)
OUTBOX_QUEUE_DEPTH = Gauge(
    "chiron_worker_outbox_queue_depth",
    "Current outbox queue depth",
    ("event_type", "status"),
)
RETRIEVAL_DURATION = Histogram(
    "chiron_worker_retrieval_duration_seconds",
    "Worker retrieval task latency",
    ("mode", "route", "outcome"),
    buckets=(0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 30, 60, 120),
)
RETENTION_ROWS = Counter(
    "chiron_worker_retention_rows_total",
    "Rows redacted or removed by retention enforcement",
    ("table",),
)
RETENTION_RUNS = Counter(
    "chiron_worker_retention_runs_total",
    "Retention enforcement runs",
    ("outcome",),
)
GRADING_SLA_ESCALATIONS = Counter(
    "chiron_worker_grading_sla_escalations_total",
    "Essay attempts routed to instructor review after the grading SLA expired",
)


def start_exporter(port: int) -> None:
    if port > 0:
        start_http_server(port)


def record_outbox(consumer: str, result: dict[str, int]) -> None:
    for outcome in ("claimed", "processed", "failed"):
        OUTBOX_EVENTS.labels(consumer=consumer, outcome=outcome).inc(result.get(outcome, 0))


def update_queue_depths(depths: dict[tuple[str, str], int]) -> None:
    for event_type in ("chunks.sync_requested", "essay.grading.requested"):
        for status in ("pending", "processing", "dead"):
            OUTBOX_QUEUE_DEPTH.labels(event_type=event_type, status=status).set(
                depths.get((event_type, status), 0)
            )
