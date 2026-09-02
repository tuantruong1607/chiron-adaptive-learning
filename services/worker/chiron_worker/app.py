import os

from celery import Celery
from celery.signals import worker_ready

from .metrics import start_exporter

def _normalize_redis_url(url: str) -> str:
    if url.startswith("rediss://") and "ssl_cert_reqs" not in url:
        sep = "&" if "?" in url else "?"
        return f"{url}{sep}ssl_cert_reqs=none"
    return url


_redis_url = _normalize_redis_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))

celery_app = Celery(
    "chiron",
    broker=_redis_url,
    backend=_redis_url,
    include=["chiron_worker.tasks"],
)
celery_app.conf.update(
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    task_track_started=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    beat_schedule={
        "drain-vector-outbox": {
            "task": "chiron.drain_outbox",
            "schedule": float(os.getenv("OUTBOX_POLL_SECONDS", "5")),
            "options": {"expires": float(os.getenv("OUTBOX_POLL_SECONDS", "5"))},
        },
        "enforce-data-retention": {
            "task": "chiron.enforce_retention",
            "schedule": float(os.getenv("RETENTION_SCHEDULE_SECONDS", "86400")),
        },
    },
)


@worker_ready.connect
def _start_metrics_exporter(**_: object) -> None:
    start_exporter(int(os.getenv("WORKER_METRICS_PORT", "9108")))
