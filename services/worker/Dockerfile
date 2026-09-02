FROM python:3.12-slim
ARG WORKER_EXTRAS=embedding
WORKDIR /app
COPY pyproject.toml ./
RUN mkdir -p chiron_worker && touch chiron_worker/__init__.py
RUN pip install --no-cache-dir ".[${WORKER_EXTRAS}]"
COPY chiron_worker ./chiron_worker
COPY scripts ./scripts
RUN pip install --no-cache-dir --no-deps .
RUN useradd --create-home --uid 10001 chiron \
    && mkdir -p /home/chiron/.cache/fastembed \
    && chown -R chiron:chiron /home/chiron/.cache
USER chiron
CMD ["celery", "-A", "chiron_worker.app:celery_app", "worker", "--loglevel=INFO"]
