FROM python:3.12-slim

# Bump CACHE_BUST to force full rebuild
ARG CACHE_BUST=3

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Install deps first (cached layer — only re-runs when pyproject.toml changes)
COPY pyproject.toml ./
RUN mkdir -p app && touch app/__init__.py \
    && pip install --no-cache-dir .

# Copy ALL source files in one shot — avoids Railway build context file-miss bugs
COPY . .

RUN pip install --no-cache-dir --no-deps . \
    && useradd --create-home --uid 10001 chiron

USER chiron
EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
