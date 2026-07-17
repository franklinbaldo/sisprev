"""Tests for the --json payload (RFC 0001, P10) — the reviewer's second blocking point."""

from __future__ import annotations

from detections import Detection, Violation
from validar_regras import build_json_payload


def test_json_payload_includes_requires_achado_and_evidencia() -> None:
    """A consumer must not need a side table to know camada or the mechanical facts."""
    detection = Detection(
        detector="P9_SEXO_FUNDAMENTACAO",
        fingerprint="sha256:" + "a" * 64,
        regras=frozenset({"regra-0078"}),
        evidencia={"sexo": "MASCULINO", "has_mulher": True, "has_homem": False},
        requires_achado=False,
    )
    payload = build_json_payload([], [detection])

    (entry,) = payload["detections"]
    assert entry["requires_achado"] is False
    assert entry["evidencia"] == {"sexo": "MASCULINO", "has_mulher": True, "has_homem": False}


def test_json_payload_includes_violations() -> None:
    """Violations still carry code/message, unaffected by the detections change."""
    violation = Violation("P14_DETECCAO_SEM_ACHADO", "example")
    payload = build_json_payload([violation], [])

    assert payload["violations"] == [{"code": "P14_DETECCAO_SEM_ACHADO", "message": "example"}]
