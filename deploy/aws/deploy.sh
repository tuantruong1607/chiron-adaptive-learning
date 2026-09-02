#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENV_FILE="${ROOT_DIR}/deploy/aws.env"
COMPOSE_FILE="${ROOT_DIR}/compose.aws.yaml"

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "Missing ${ENV_FILE}. Copy deploy/aws.env.example and fill the secrets." >&2
  exit 1
fi

cd "${ROOT_DIR}"
docker compose --env-file "${ENV_FILE}" -f "${COMPOSE_FILE}" up -d --build postgres redis
docker compose --env-file "${ENV_FILE}" -f "${COMPOSE_FILE}" run --rm api alembic upgrade head
docker compose --env-file "${ENV_FILE}" -f "${COMPOSE_FILE}" up -d --build api worker web
docker compose --env-file "${ENV_FILE}" -f "${COMPOSE_FILE}" ps

echo "Deploy complete. Check the web URL and /readyz through the web/API routing."
