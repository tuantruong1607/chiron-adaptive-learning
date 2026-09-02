#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ENV_FILE="${ROOT_DIR}/deploy/aws.env"
COMPOSE_FILE="${ROOT_DIR}/compose.aws.yaml"
BACKUP_DIR="${ROOT_DIR}/backups"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"

set -a
# The deploy env is operator-controlled and contains the database credentials
# used by the compose service for this local backup command.
source "${ENV_FILE}"
set +a

mkdir -p "${BACKUP_DIR}"
docker compose --env-file "${ENV_FILE}" -f "${COMPOSE_FILE}" exec -T postgres \
  pg_dump -U "${POSTGRES_USER:-chiron}" -d "${POSTGRES_DB:-chiron}" --format=custom \
  > "${BACKUP_DIR}/chiron-${STAMP}.dump"

echo "Created ${BACKUP_DIR}/chiron-${STAMP}.dump"
