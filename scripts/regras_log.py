"""P11 — regras/log.md, an aggregated per-date changelog derived from git history.

Unlike the CSV and the ``index.md`` files, this is **not** part of the CI's
committed-artifacts-must-match-regeneration gate: a commit that touches
``regras/`` cannot know its own hash/date/message before it exists, so a
single commit can never be "in sync" with a log.md that includes itself —
regenerating it in CI and diffing would always show it one commit behind.
It's a best-effort convenience artifact instead: run
``uv run python scripts/regras_log.py`` locally after a batch of audit
commits to refresh it, and commit the result deliberately when useful.

Because nothing forces a refresh, the committed file can silently fall
arbitrarily far behind the real history (``git log`` is always the
authoritative trail — this is a projection of it, not a second source of
truth). To make staleness *visible* rather than silent, every regeneration
stamps the HEAD commit it was generated from as ``Gerado até: <sha>`` —
compare that against ``git log -1 -- regras/`` to see how far behind the
committed file is.
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from typing import TYPE_CHECKING

from md_format import write_markdown
from okf_common import DEFAULT_BUNDLE, REPO_ROOT

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)


def regenerate_regras_log(bundle_dir: Path) -> bool:
    """Rewrite ``regras/log.md`` from git history touching that directory.

    One ``## YYYY-MM-DD`` section per calendar day with a commit, newest
    first, each commit subject as a bullet. Best-effort: if ``bundle_dir``
    isn't inside this repository's working tree, or git isn't available,
    this is a silent no-op (returns False) rather than a hard failure —
    callers (tests, throwaway bundles) shouldn't need a real git history.
    """
    regras_dir = bundle_dir / "regras"
    try:
        relative = regras_dir.resolve().relative_to(REPO_ROOT)
    except ValueError:
        return False

    git = shutil.which("git")
    if git is None:
        return False

    try:
        result = subprocess.run(
            [git, "log", "--follow", "--date=short", "--pretty=format:%ad\t%s", "--", str(relative)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        head = subprocess.run(
            [git, "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return False

    by_date: dict[str, list[str]] = {}
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        date, _, subject = line.partition("\t")
        by_date.setdefault(date, []).append(subject)

    lines = ["# Log", "", f"Gerado até: {head.stdout.strip()}", ""]
    for date in sorted(by_date, reverse=True):
        lines.append(f"## {date}")
        lines.append("")
        lines.extend(f"- {subject}" for subject in by_date[date])
        lines.append("")
    regras_dir.mkdir(parents=True, exist_ok=True)
    write_markdown(regras_dir / "log.md", "\n".join(lines).rstrip() + "\n")
    return True


def main() -> None:
    """CLI entry point: regenerate regras/log.md for the default bundle."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if regenerate_regras_log(DEFAULT_BUNDLE):
        logger.info("Regenerated %s", DEFAULT_BUNDLE / "regras" / "log.md")
    else:
        logger.warning("Skipped: %s is not inside a git working tree", DEFAULT_BUNDLE)


if __name__ == "__main__":
    main()
