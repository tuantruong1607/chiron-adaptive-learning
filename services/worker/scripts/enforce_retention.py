from __future__ import annotations

import argparse
import json

from chiron_worker.config import get_settings
from chiron_worker.retention import RetentionEnforcer, policy_from_settings


def main() -> int:
    parser = argparse.ArgumentParser(description="Enforce learner-data retention policy")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply redaction/deletion; without this flag the command is read-only",
    )
    args = parser.parse_args()
    settings = get_settings()
    database_url = settings.operations_database_url or settings.database_url
    report = RetentionEnforcer(database_url, policy_from_settings(settings)).run(
        dry_run=not args.apply
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
