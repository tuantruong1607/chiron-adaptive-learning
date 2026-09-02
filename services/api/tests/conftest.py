from __future__ import annotations

import os

# Unit/API tests must be deterministic and must not depend on Docker. PostgreSQL
# contract tests create their own session factory when explicitly enabled.
os.environ["APP_ENV"] = "test"
os.environ["PERSISTENCE_BACKEND"] = "memory"
os.environ["DATABASE_URL"] = ""
os.environ["REDIS_URL"] = ""
os.environ["QDRANT_URL"] = ""
os.environ["LLM_PROVIDER"] = "mock"
os.environ["AUTH_JWT_SECRET"] = "chiron-test-secret-at-least-32-characters"
