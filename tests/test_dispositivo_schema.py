"""Tests for the P3 dispositivo schema, doc I/O and validation (RFC 0001).

Uses synthetic fixture content throughout — never real legal text — since
authoring an actual dispositivo (verbatim transcription of an official
publication) is a human act, not something these tests should fabricate.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import yaml
from dispositivo_schema import (
    Dispositivo,
    dispositivo_ids,
    load_dispositivos,
    parse_dispositivo_doc,
    regenerate_dispositivos_index,
    validate_bundle_dispositivos,
    validate_dispositivo,
)

if TYPE_CHECKING:
    from pathlib import Path

_VALID_FRONTMATTER: dict[str, object] = {
    "type": "Dispositivo",
    "id": "lei-teste/art-1",
    "norma": "Lei de Teste nº 1/2026",
    "artigo": "Art. 1º",
    "fonte": "https://example.invalid/lei-teste",
}
_VALID_TEXTO = "Este é o texto de teste do dispositivo."


def _write(bundle_dir: Path, rel_path: str, frontmatter: dict, texto: str) -> Path:
    doc_path = bundle_dir / rel_path
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    doc_path.write_text(f"---\n{fm_text}---\n\n{texto}\n", encoding="utf-8")
    return doc_path


def test_parse_dispositivo_doc_round_trips_frontmatter_and_texto() -> None:
    """parse_dispositivo_doc splits frontmatter and the raw body text unchanged."""
    text = "---\ntype: Dispositivo\nid: lei-teste/art-1\n---\n\nTexto exato aqui.\n"
    frontmatter, texto = parse_dispositivo_doc(text)
    assert frontmatter == {"type": "Dispositivo", "id": "lei-teste/art-1"}
    assert texto == "Texto exato aqui."


def test_load_dispositivos_returns_empty_list_for_missing_directory(tmp_path: Path) -> None:
    """A bundle directory that doesn't exist yet loads no dispositivos."""
    assert load_dispositivos(tmp_path / "does-not-exist") == []


def test_load_dispositivos_skips_index_md(tmp_path: Path) -> None:
    """index.md files are never treated as authored dispositivo docs."""
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (tmp_path / "lei-teste" / "index.md").write_text("# lei-teste\n", encoding="utf-8")

    dispositivos = load_dispositivos(tmp_path)

    assert [d.doc_id for d in dispositivos] == ["lei-teste/art-1"]


def test_load_dispositivos_records_the_bundle_it_was_loaded_from(tmp_path: Path) -> None:
    """Every loaded dispositivo carries the path of its own bundle (P3 provenance)."""
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)
    assert dispositivo.bundle_dir == tmp_path


def test_valid_dispositivo_has_no_violations(tmp_path: Path) -> None:
    """A well-formed dispositivo satisfies every P3 invariant."""
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)
    assert validate_dispositivo(dispositivo) == []


def test_contract_is_populated_for_a_valid_dispositivo(tmp_path: Path) -> None:
    """A well-formed dispositivo gets a real, typed DispositivoFrontmatter via .contract."""
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)
    assert dispositivo.contract is not None
    assert dispositivo.contract.norma == _VALID_FRONTMATTER["norma"]
    assert dispositivo.validation_error is None


def test_contract_is_none_for_a_malformed_dispositivo(tmp_path: Path) -> None:
    """A dispositivo missing a required field has no typed contract, only a validation_error."""
    incomplete = {k: v for k, v in _VALID_FRONTMATTER.items() if k != "fonte"}
    _write(tmp_path, "lei-teste/art-1.md", incomplete, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    assert dispositivo.contract is None
    assert dispositivo.validation_error is not None


def test_frontmatter_id_must_match_path(tmp_path: Path) -> None:
    """A frontmatter id disagreeing with the file's own path is a violation."""
    bad = {**_VALID_FRONTMATTER, "id": "lei-teste/art-2"}
    _write(tmp_path, "lei-teste/art-1.md", bad, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("does not match path" in e for e in errors)


def test_empty_body_is_rejected() -> None:
    """P3 requires the body to be the provision's exact, non-empty text."""
    dispositivo = Dispositivo(doc_id="lei-teste/art-1", frontmatter=_VALID_FRONTMATTER, body="   ")
    errors = validate_dispositivo(dispositivo)
    assert any("exact text" in e for e in errors)


def test_missing_required_field_is_rejected(tmp_path: Path) -> None:
    """A dispositivo missing a required frontmatter field (fonte) is rejected."""
    incomplete = {k: v for k, v in _VALID_FRONTMATTER.items() if k != "fonte"}
    _write(tmp_path, "lei-teste/art-1.md", incomplete, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("fonte" in e for e in errors)


def test_extra_field_is_rejected(tmp_path: Path) -> None:
    """DispositivoFrontmatter is a closed schema — unknown fields cannot pass silently."""
    extra = {**_VALID_FRONTMATTER, "campo_inesperado": "valor"}
    _write(tmp_path, "lei-teste/art-1.md", extra, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("campo_inesperado" in e for e in errors)


def test_validate_bundle_dispositivos_aggregates_every_doc(tmp_path: Path) -> None:
    """The bundle-level validator reports errors from every doc, not just the first."""
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    bad = {**_VALID_FRONTMATTER, "id": "lei-teste/art-2"}
    _write(tmp_path, "lei-teste/art-2.md", bad, "")

    errors = validate_bundle_dispositivos(tmp_path)

    assert len(errors) == 1
    assert "art-2" in errors[0]


def test_dispositivo_ids_returns_every_doc_id(tmp_path: Path) -> None:
    """dispositivo_ids returns the full set of currently authored doc_ids."""
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    second = {**_VALID_FRONTMATTER, "id": "lei-teste/art-2"}
    _write(tmp_path, "lei-teste/art-2.md", second, _VALID_TEXTO)

    assert dispositivo_ids(tmp_path) == frozenset({"lei-teste/art-1", "lei-teste/art-2"})


def test_regenerate_dispositivos_index_is_a_noop_for_missing_directory(tmp_path: Path) -> None:
    """No dispositivos bundle yet means no index to regenerate."""
    missing = tmp_path / "does-not-exist"
    regenerate_dispositivos_index(missing)
    assert not missing.exists()


def test_regenerate_dispositivos_index_writes_per_norma_and_root_index(tmp_path: Path) -> None:
    """Regeneration writes both the norma subdirectory index and the bundle-root index."""
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)

    regenerate_dispositivos_index(tmp_path)

    norma_index = (tmp_path / "lei-teste" / "index.md").read_text(encoding="utf-8")
    assert "art-1.md" in norma_index
    assert "Lei de Teste" in norma_index

    root_index = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "okf_version: '0.1'" in root_index
    assert "lei-teste/" in root_index


def test_regenerate_dispositivos_index_skips_a_non_nested_doc_instead_of_crashing(
    tmp_path: Path,
) -> None:
    """A malformed, non-nested dispositivo must not crash index regeneration.

    Already reported by validate_dispositivo() — regenerate_dispositivos_index()
    just skips it instead of writing into a norma index that was never created.
    """
    top_level = {**_VALID_FRONTMATTER, "id": "solto"}
    _write(tmp_path, "solto.md", top_level, _VALID_TEXTO)
    _write(tmp_path, "lei-teste/art-1.md", _VALID_FRONTMATTER, _VALID_TEXTO)

    regenerate_dispositivos_index(tmp_path)  # must not raise

    root_index = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "lei-teste/" in root_index
    assert "solto" not in root_index
