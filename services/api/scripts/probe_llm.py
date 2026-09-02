import argparse
import asyncio
import json

from app.config import get_settings
from app.llm.probe import AvailabilityProbe
from app.llm.router import build_llm_router


async def run(active: bool) -> None:
    router = build_llm_router(get_settings())
    if router is None:
        raise RuntimeError("LLM router is not configured")
    probe = AvailabilityProbe(router.providers, router.registry, router.state)
    results = await probe.refresh(active=active)
    print(json.dumps([result.as_dict() for result in results], indent=2))
    if any(result.status.value == "unavailable" for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Probe configured Chiron LLM routes")
    parser.add_argument(
        "--active",
        action="store_true",
        help="Send a tiny synthetic completion after checking /models",
    )
    arguments = parser.parse_args()
    asyncio.run(run(arguments.active))
