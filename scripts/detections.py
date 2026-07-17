"""Mechanical detections and validation findings (RFC 0001, P10/P14).

A ``Detection`` is a pure mechanical fact a detector reports — it never
implies a conclusion, a severity, or an achado (princípio da autoria
humana). Each detection carries a stable ``fingerprint`` derived only from
the detector, its version, and a canonical mechanical subject, so the same
occurrence hashes identically regardless of read order. Achados reference
detections by ``fingerprint``; the bidirectional check (P14.6) operates on
those fingerprints, never on set-equality with ``regras_afetadas``.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping


def canonical_json(value: object) -> str:
    """Deterministic JSON rendering of ``value``, for building a fingerprint's canonical subject.

    Detectors must feed the mechanical evidence itself into the fingerprint,
    not just the regra ids — otherwise the same fingerprint can outlive a
    materially different premise, and the CI would wrongly treat a changed
    occurrence as "still reproduced."
    """
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)


def fingerprint(detector: str, version: int, canonical_subject: str) -> str:
    """Stable id for one mechanical occurrence: detector + version + canonical subject.

    The caller supplies an already-canonical subject (e.g. ``canonical_json``
    of the sorted regra ids *and* the mechanical evidence), so permuting the
    read order never changes the result, and a materially different premise
    always changes the fingerprint. Bumping ``version`` when a detector's
    semantics change deliberately invalidates every old fingerprint, forcing
    achados to be re-confirmed.
    """
    payload = f"{detector}\nv{version}\n{canonical_subject}".encode()
    return "sha256:" + hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class Detection:
    """One mechanical occurrence reported by a detector — never a conclusion."""

    detector: str
    fingerprint: str
    regras: frozenset[str]
    evidencia: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True)
class Violation:
    """One validation finding — always carries a stable code (P10)."""

    code: str
    message: str

    def __str__(self) -> str:
        """Render as "CODE: message" for CLI output."""
        return f"{self.code}: {self.message}"
