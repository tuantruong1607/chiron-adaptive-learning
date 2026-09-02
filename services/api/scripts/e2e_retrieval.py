from __future__ import annotations

import json
import os
import sys

os.environ["PERSISTENCE_BACKEND"] = "postgres"
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from fastapi.testclient import TestClient  # noqa: E402

from app.main import app  # noqa: E402


def main() -> int:
    tenant = os.getenv("CHIRON_E2E_TENANT", "chiron-demo")
    email = os.getenv("CHIRON_E2E_EMAIL", "learner@chiron.local")
    password = os.getenv("CHIRON_E2E_PASSWORD", "chiron-demo-2026")
    query = os.getenv("CHIRON_E2E_QUERY", "Giải thích Reciprocal Rank Fusion và weighted sum")

    with TestClient(app) as client:
        login = client.post(
            "/api/v1/auth/token",
            json={"tenant_slug": tenant, "email": email, "password": password},
        )
        login.raise_for_status()
        access_token = login.json()["access_token"]
        response = client.get(
            "/api/v1/retrieval",
            params={"q": query, "course": "rag-intensive"},
            headers={"Authorization": f"Bearer {access_token}"},
        )
        response.raise_for_status()
        payload = response.json()

    print(
        json.dumps(
            {
                "login_status": login.status_code,
                "retrieval_status": response.status_code,
                "query": payload["query"],
                "route": payload["route"],
                "hit_count": len(payload["hits"]),
                "top_hit": payload["hits"][0] if payload["hits"] else None,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
