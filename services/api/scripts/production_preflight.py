from __future__ import annotations

import argparse
import json
import os

from app.operations import audit_production_environment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit production secrets and policy gates without printing secret values")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when an error finding exists")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    findings = audit_production_environment(dict(os.environ))
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)
    print(json.dumps({"status": "pass" if errors == 0 else "blocked", "error_count": errors, "warning_count": warnings, "findings": [item.as_dict() for item in findings]}, indent=2))
    return 1 if arguments.strict and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
