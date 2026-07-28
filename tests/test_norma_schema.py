"""Tests for ``type: Norma`` — the closed vocabulary of citable norms (P4)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import yaml
from norma_schema import load_normas, normas_por_id, validate_norma

if TYPE_CHECKING:
    from pathlib import Path

_VALID: dict[str, object] = {
    "type": "Norma",
    "id": "lei-teste",
    "nome": "Lei de Teste nº 1/2026",
    "apelido": "Lei 1/2026",
    "fontes": ["https://example.invalid/lei-teste"],
}


def _write(bundle_dir: Path, norma_id: str, frontmatter: dict) -> None:
    doc_path = bundle_dir / norma_id / "norma.md"
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    doc_path.write_text(f"---\n{fm_text}---\n\n# {frontmatter.get('nome', '')}\n", encoding="utf-8")


def test_load_normas_returns_empty_list_for_missing_directory(tmp_path: Path) -> None:
    """A bundle directory that doesn't exist yet loads no normas."""
    assert load_normas(tmp_path / "does-not-exist") == []


def test_norma_is_keyed_by_its_own_directory(tmp_path: Path) -> None:
    """The directory name *is* the citation key a dispositivo resolves against."""
    _write(tmp_path, "lei-teste", _VALID)
    (norma,) = load_normas(tmp_path)

    assert norma.doc_id == "lei-teste"
    assert norma.nome == "Lei de Teste nº 1/2026"
    assert norma.apelido == "Lei 1/2026"
    assert validate_norma(norma) == []


def test_frontmatter_id_must_match_the_directory(tmp_path: Path) -> None:
    """A key stated twice is checked, not trusted."""
    _write(tmp_path, "lei-teste", {**_VALID, "id": "outra-lei"})
    (norma,) = load_normas(tmp_path)

    assert any("does not match its directory" in e for e in validate_norma(norma))


def test_fonte_must_be_a_web_url(tmp_path: Path) -> None:
    """A norm's official publication is a link the reader can follow."""
    _write(tmp_path, "lei-teste", {**_VALID, "fontes": ["Diário Oficial de 2026"]})
    (norma,) = load_normas(tmp_path)

    assert any("must be an http(s) URL" in e for e in validate_norma(norma))


def test_at_least_one_fonte_is_required(tmp_path: Path) -> None:
    """A norm with no reachable source cannot verify anything transcribed from it."""
    _write(tmp_path, "lei-teste", {**_VALID, "fontes": []})
    (norma,) = load_normas(tmp_path)

    assert validate_norma(norma) != []


def test_extra_field_is_rejected(tmp_path: Path) -> None:
    """NormaFrontmatter is a closed contract — unknown keys cannot pass silently."""
    _write(tmp_path, "lei-teste", {**_VALID, "vigencia": "2026"})
    (norma,) = load_normas(tmp_path)

    assert any("vigencia" in e for e in validate_norma(norma))


def test_malformed_norma_still_loads_and_exposes_its_name(tmp_path: Path) -> None:
    """A doc invalid for one field's sake must not hide the others.

    Same ungated-fallback rule as ``Regra.status_regra``/``Achado.situacao``:
    an index still needs the norm's name from a doc that fails validation for
    an unrelated reason, so ``Bundle.load()`` never raises mid-load.
    """
    _write(tmp_path, "lei-teste", {**_VALID, "fontes": []})
    (norma,) = load_normas(tmp_path)

    assert norma.contract is None
    assert norma.validation_error is not None
    assert norma.nome == "Lei de Teste nº 1/2026"
    assert norma.apelido == "Lei 1/2026"


def test_normas_por_id_indexes_every_authored_norma(tmp_path: Path) -> None:
    """The resolution map a dispositivo's norma key is checked against."""
    _write(tmp_path, "lei-teste", _VALID)
    _write(tmp_path, "outra-lei", {**_VALID, "id": "outra-lei", "nome": "Outra Lei"})

    assert sorted(normas_por_id(tmp_path)) == ["lei-teste", "outra-lei"]
