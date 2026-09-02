FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY pyproject.toml ./
RUN mkdir -p app && touch app/__init__.py \
    && pip install --no-cache-dir .

COPY app ./app
COPY alembic ./alembic
COPY alembic.ini ./alembic.ini
COPY scripts ./scripts
COPY start.sh ./start.sh
RUN pip install --no-cache-dir --no-deps . \
    && useradd --create-home --uid 10001 chiron \
    && chmod +x /app/start.sh

USER chiron
EXPOSE 8000

CMD ["/app/start.sh"]
