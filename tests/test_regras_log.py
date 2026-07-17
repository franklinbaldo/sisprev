"""Tests for the best-effort regras/log.md derivation (RFC 0001, P11).

Never writes into the real repo tree — the "inside a git working tree"
path is exercised against a throwaway repo built under tmp_path, with
regras_log.REPO_ROOT monkeypatched to point at it.
"""

from __future__ import annotations

import shutil
import subprocess
from typing import TYPE_CHECKING

import regras_log
from regras_log import regenerate_regras_log

if TYPE_CHECKING:
    from pathlib import Path

    import pytest


def test_noop_for_a_bundle_outside_the_repo_working_tree(tmp_path: Path) -> None:
    """A throwaway tmp_path bundle isn't inside REPO_ROOT — silent no-op, no crash."""
    bundle_dir = tmp_path / "regras-sisprev"
    (bundle_dir / "regras").mkdir(parents=True)

    assert regenerate_regras_log(bundle_dir) is False
    assert not (bundle_dir / "regras" / "log.md").exists()


def _run_git(repo_root: Path, *args: str) -> None:
    git = shutil.which("git")
    assert git is not None
    subprocess.run([git, *args], cwd=repo_root, check=True, capture_output=True)


def _init_throwaway_repo(repo_root: Path) -> Path:
    """Create a real git repo with one commit touching a regra doc; returns bundle_dir."""
    bundle_dir = repo_root / "okf" / "regras-sisprev"
    (bundle_dir / "regras").mkdir(parents=True)
    (bundle_dir / "regras" / "regra-0001.md").write_text("---\n---\n", encoding="utf-8")

    _run_git(repo_root, "init", "-q")
    _run_git(repo_root, "config", "user.email", "test@example.com")
    _run_git(repo_root, "config", "user.name", "Test")
    _run_git(repo_root, "add", ".")
    _run_git(repo_root, "commit", "-q", "-m", "add regra-0001")
    return bundle_dir


def test_regenerates_log_from_a_throwaway_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """A bundle inside a real (throwaway) git working tree gets a dated log.md."""
    bundle_dir = _init_throwaway_repo(tmp_path)
    monkeypatch.setattr(regras_log, "REPO_ROOT", tmp_path)

    assert regenerate_regras_log(bundle_dir) is True
    log_text = (bundle_dir / "regras" / "log.md").read_text(encoding="utf-8")
    assert log_text.startswith("# Log")
    assert "## " in log_text
    assert "add regra-0001" in log_text
