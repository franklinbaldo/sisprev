"""P3 — cross-bundle dispositivo link resolution (RFC 0001).

Unit-level: calls check_p3_dispositivos() directly (not the full
validate_bundle(), which also needs a structurally valid regras-sisprev
bundle_dir) — mirrors how estado_auditoria's check_p7_estados is tested.
Uses synthetic on-disk fixtures for the dispositivos side, never real
bundle content.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import yaml
from bundle import Bundle, Regra, check_p3_dispositivos
from regra_schema import FRONTMATTER_COLUMNS, FRONTMATTER_KEYS

if TYPE_CHECKING:
    from pathlib import Path

_VALID_DISPOSITIVO_FRONTMATTER = {
    "type": "Dispositivo",
    "id": "lei-teste/art-1",
    "norma": "Lei de Teste nº 1/2026",
    "artigo": "Art. 1º",
    "fonte": "https://example.invalid/lei-teste",
}


def _regra(regra_id: str, *, dispositivos: list[str] | None = None) -> Regra:
    fm: dict[str, object] = {FRONTMATTER_KEYS[c]: "" for c in FRONTMATTER_COLUMNS}
    fm["nome"] = f"Regra {regra_id}"
    if dispositivos is not None:
        fm["dispositivos"] = dispositivos
    return Regra(doc_id=regra_id, frontmatter=fm)


def _write_dispositivo(dispositivos_dir: Path) -> None:
    doc_path = dispositivos_dir / "lei-teste" / "art-1.md"
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    fm_text = yaml.safe_dump(_VALID_DISPOSITIVO_FRONTMATTER, allow_unicode=True, sort_keys=False)
    doc_path.write_text(f"---\n{fm_text}---\n\nTexto de teste.\n", encoding="utf-8")


def _bundle(regras: list[Regra], dispositivos_dir: Path) -> Bundle:
    return Bundle(
        bundle_dir=dispositivos_dir,
        regras=tuple(regras),
        achados=(),
        dispositivos_dir=dispositivos_dir,
    )


def test_regra_with_no_dispositivos_field_has_no_violations(tmp_path: Path) -> None:
    """A regra that never mentions dispositivos: triggers no P3 check at all."""
    bundle = _bundle([_regra("regra-0001")], tmp_path)
    assert check_p3_dispositivos(bundle) == []


def test_regra_referencing_an_existing_dispositivo_has_no_violations(tmp_path: Path) -> None:
    """A reference that resolves to an authored dispositivo passes."""
    _write_dispositivo(tmp_path)
    bundle = _bundle([_regra("regra-0001", dispositivos=["/dispositivos/lei-teste/art-1.md"])], tmp_path)

    assert check_p3_dispositivos(bundle) == []


def test_regra_referencing_an_unknown_dispositivo_is_a_violation(tmp_path: Path) -> None:
    """A canonically formed reference that resolves to nothing is a violation."""
    bundle = _bundle([_regra("regra-0001", dispositivos=["/dispositivos/lei-teste/art-1.md"])], tmp_path)

    violations = check_p3_dispositivos(bundle)

    assert len(violations) == 1
    assert violations[0].code == "P3_DISPOSITIVO_INVALIDO"
    assert "regra-0001" in violations[0].message
    assert "unknown dispositivo" in violations[0].message


def test_non_canonical_dispositivo_reference_is_a_violation(tmp_path: Path) -> None:
    """A reference missing the leading slash is rejected before resolution is even tried."""
    _write_dispositivo(tmp_path)
    bundle = _bundle([_regra("regra-0001", dispositivos=["dispositivos/lei-teste/art-1.md"])], tmp_path)

    violations = check_p3_dispositivos(bundle)

    assert len(violations) == 1
    assert "non-canonical" in violations[0].message


def test_multiple_dispositivos_are_each_checked_independently(tmp_path: Path) -> None:
    """One valid and one unknown reference on the same regra yields exactly one violation."""
    _write_dispositivo(tmp_path)
    bundle = _bundle(
        [
            _regra(
                "regra-0001",
                dispositivos=["/dispositivos/lei-teste/art-1.md", "/dispositivos/lei-teste/art-2.md"],
            )
        ],
        tmp_path,
    )

    violations = check_p3_dispositivos(bundle)

    assert len(violations) == 1
    assert "art-2" in violations[0].message
