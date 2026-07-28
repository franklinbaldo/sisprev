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
    check_vigencias,
    dispositivo_ids,
    load_dispositivos,
    parse_dispositivo_doc,
    regenerate_dispositivos_index,
    validate_bundle_dispositivos,
    validate_dispositivo,
)
from norma_schema import normas_por_id

if TYPE_CHECKING:
    from pathlib import Path

_VALID_FRONTMATTER: dict[str, object] = {
    "type": "Dispositivo",
    "id": "lei-teste/art-1/original",
    "norma": "lei-teste",
    "componentes": [{"tipo": "artigo", "valor": "1"}],
    "fontes": ["https://example.invalid/lei-teste"],
}
_VALID_TEXTO = "Este é o texto de teste do dispositivo."

_NORMA_FRONTMATTER: dict[str, object] = {
    "type": "Norma",
    "id": "lei-teste",
    "nome": "Lei de Teste nº 1/2026",
    "apelido": "Lei 1/2026",
    "fontes": ["https://example.invalid/lei-teste"],
}


def _write(bundle_dir: Path, rel_path: str, frontmatter: dict, texto: str) -> Path:
    doc_path = bundle_dir / rel_path
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    fm_text = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False)
    doc_path.write_text(f"---\n{fm_text}---\n\n{texto}\n", encoding="utf-8")
    return doc_path


def _write_norma(bundle_dir: Path, norma_id: str = "lei-teste") -> None:
    _write(bundle_dir, f"{norma_id}/norma.md", {**_NORMA_FRONTMATTER, "id": norma_id}, "")


def test_parse_dispositivo_doc_round_trips_frontmatter_and_texto() -> None:
    """parse_dispositivo_doc splits frontmatter and the raw body text unchanged."""
    text = "---\ntype: Dispositivo\nid: lei-teste/art-1/original\n---\n\nTexto exato aqui.\n"
    frontmatter, texto = parse_dispositivo_doc(text)
    assert frontmatter == {"type": "Dispositivo", "id": "lei-teste/art-1/original"}
    assert texto == "Texto exato aqui."


def test_load_dispositivos_returns_empty_list_for_missing_directory(tmp_path: Path) -> None:
    """A bundle directory that doesn't exist yet loads no dispositivos."""
    assert load_dispositivos(tmp_path / "does-not-exist") == []


def test_load_dispositivos_skips_generated_and_norma_docs(tmp_path: Path) -> None:
    """index.md (generated) and norma.md (a P4 concept) are never dispositivo docs."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    _write_norma(tmp_path)
    (tmp_path / "lei-teste" / "index.md").write_text("# lei-teste\n", encoding="utf-8")

    dispositivos = load_dispositivos(tmp_path)

    assert [d.doc_id for d in dispositivos] == ["lei-teste/art-1/original"]


def test_load_dispositivos_records_the_bundle_it_was_loaded_from(tmp_path: Path) -> None:
    """Every loaded dispositivo carries the path of its own bundle (P3 provenance)."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)
    assert dispositivo.bundle_dir == tmp_path


def test_valid_dispositivo_has_no_violations(tmp_path: Path) -> None:
    """A well-formed dispositivo satisfies every P3 invariant."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)
    assert validate_dispositivo(dispositivo) == []


def test_contract_is_populated_for_a_valid_dispositivo(tmp_path: Path) -> None:
    """A well-formed dispositivo gets a real, typed DispositivoFrontmatter via .contract."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)
    assert dispositivo.contract is not None
    assert dispositivo.contract.norma == "lei-teste"
    assert dispositivo.validation_error is None


def test_contract_is_none_for_a_malformed_dispositivo(tmp_path: Path) -> None:
    """A dispositivo missing a required field has no typed contract, only a validation_error."""
    incomplete = {k: v for k, v in _VALID_FRONTMATTER.items() if k != "fontes"}
    _write(tmp_path, "lei-teste/art-1/original.md", incomplete, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    assert dispositivo.contract is None
    assert dispositivo.validation_error is not None


def test_frontmatter_id_must_match_path(tmp_path: Path) -> None:
    """A frontmatter id disagreeing with the file's own path is a violation."""
    bad = {**_VALID_FRONTMATTER, "id": "lei-teste/art-2/original"}
    _write(tmp_path, "lei-teste/art-1/original.md", bad, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("does not match path" in e for e in errors)


def test_empty_body_is_rejected() -> None:
    """P3 requires a non-empty body: the transcribed chain down to the provision.

    Only its *existence* is checked. Whether the chain is complete, and whether
    each ancestor is in the wording contemporaneous with this one, is curation
    — a legal reading no validator derives (see docs/spec/dispositivo.md).
    """
    dispositivo = Dispositivo(doc_id="lei-teste/art-1/original", frontmatter=_VALID_FRONTMATTER, body="   ")
    errors = validate_dispositivo(dispositivo)
    assert any("chain down to the provision" in e for e in errors)


def test_missing_required_field_is_rejected(tmp_path: Path) -> None:
    """A dispositivo missing a required frontmatter field (fontes) is rejected."""
    incomplete = {k: v for k, v in _VALID_FRONTMATTER.items() if k != "fontes"}
    _write(tmp_path, "lei-teste/art-1/original.md", incomplete, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("fontes" in e for e in errors)


def test_extra_field_is_rejected(tmp_path: Path) -> None:
    """DispositivoFrontmatter is a closed schema — unknown fields cannot pass silently.

    Notably this now rejects the *old* flat fields (``artigo``, ``paragrafo``,
    ``inciso``, ``alinea``, ``fonte``), so a doc left behind by the migration
    fails loudly rather than validating with an empty address.
    """
    extra = {**_VALID_FRONTMATTER, "artigo": "Art. 1º"}
    _write(tmp_path, "lei-teste/art-1/original.md", extra, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("artigo" in e for e in errors)


# --- derived identity ---------------------------------------------------


def test_address_directory_must_match_the_componentes(tmp_path: Path) -> None:
    """The path is a function of the frontmatter — a hand-edited slug cannot drift."""
    fm = {**_VALID_FRONTMATTER, "id": "lei-teste/art-9/original"}
    _write(tmp_path, "lei-teste/art-9/original.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("does not match the componentes" in e for e in errors)
    assert any("'art-1'" in e for e in errors)


def test_wording_file_must_match_redacao_dada_por(tmp_path: Path) -> None:
    """A wording file named for one amending norm cannot declare another."""
    fm = {
        **_VALID_FRONTMATTER,
        "id": "lei-teste/art-1/lei-outra",
        "redacao_dada_por": "lei-terceira",
    }
    _write(tmp_path, "lei-teste/art-1/lei-outra.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("does not match redacao_dada_por" in e for e in errors)


def test_original_wording_declares_no_amending_norm(tmp_path: Path) -> None:
    """``original.md`` and ``redacao_dada_por`` are mutually exclusive by construction."""
    fm = {**_VALID_FRONTMATTER, "redacao_dada_por": "lei-outra"}
    _write(tmp_path, "lei-teste/art-1/original.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("does not match redacao_dada_por" in e for e in errors)


def test_norma_field_must_match_its_directory(tmp_path: Path) -> None:
    """The norm key is stated once and cross-checked, never trusted on its own."""
    fm = {**_VALID_FRONTMATTER, "norma": "outra-lei"}
    _write(tmp_path, "lei-teste/art-1/original.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("does not match its directory" in e for e in errors)


def test_path_must_have_exactly_three_segments(tmp_path: Path) -> None:
    """<norma>/<endereço>/<redação> — a flat doc has no place to hold a wording."""
    fm = {**_VALID_FRONTMATTER, "id": "lei-teste/art-1"}
    _write(tmp_path, "lei-teste/art-1.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("<norma>/<endereço>/<redação>" in e for e in errors)


def test_endereco_and_redacao_ids_split_provision_from_wording(tmp_path: Path) -> None:
    """The provision is the directory; the wording is the file inside it."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    assert dispositivo.endereco_id == "lei-teste/art-1"
    assert dispositivo.redacao_id == "original"
    assert dispositivo.rotulo == "art. 1º"


# --- P4 vocabulary ------------------------------------------------------


def test_unknown_norma_key_is_rejected_when_the_vocabulary_is_supplied(tmp_path: Path) -> None:
    """A norm enters the corpus by being authored, never by being typed."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo, normas={})

    assert any("has no authored norma.md" in e for e in errors)


def test_unknown_amending_norma_key_is_rejected(tmp_path: Path) -> None:
    """The amending norm is what verifies the wording, so it must be authored too."""
    fm = {
        **_VALID_FRONTMATTER,
        "id": "lei-teste/art-1/lei-outra",
        "redacao_dada_por": "lei-outra",
    }
    _write(tmp_path, "lei-teste/art-1/lei-outra.md", fm, _VALID_TEXTO)
    _write_norma(tmp_path)

    errors = validate_bundle_dispositivos(tmp_path)

    assert any("redacao_dada_por 'lei-outra'" in e for e in errors)


def test_resolved_vocabulary_passes(tmp_path: Path) -> None:
    """A dispositivo whose norm key resolves has no P4 violation."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    _write_norma(tmp_path)
    (dispositivo,) = load_dispositivos(tmp_path)

    assert validate_dispositivo(dispositivo, normas_por_id(tmp_path)) == []


# --- wording continuity -------------------------------------------------


def _com_vigencia(rel: str, redacao: str, inicio: str, fim: str | None) -> dict[str, object]:
    fm: dict[str, object] = {
        **_VALID_FRONTMATTER,
        "id": f"lei-teste/{rel}/{redacao}",
        "vigencia_inicio": inicio,
    }
    if redacao != "original":
        fm["redacao_dada_por"] = redacao
    if fim is not None:
        fm["vigencia_fim"] = fim
    return fm


def test_consecutive_wordings_of_one_provision_are_accepted(tmp_path: Path) -> None:
    """A provision's wordings form a chain: one ends the day before the next starts."""
    _write(
        tmp_path,
        "lei-teste/art-1/original.md",
        _com_vigencia("art-1", "original", "2008-01-01", "2019-11-12"),
        _VALID_TEXTO,
    )
    _write(
        tmp_path,
        "lei-teste/art-1/lei-outra.md",
        _com_vigencia("art-1", "lei-outra", "2019-11-13", None),
        _VALID_TEXTO,
    )

    assert check_vigencias(load_dispositivos(tmp_path)) == []


def test_overlapping_wordings_of_one_provision_are_a_violation(tmp_path: Path) -> None:
    """Two wordings cannot both be in force — a contradiction in the transcription.

    This is the invariant the previous flat schema could not even state,
    because provision and wording were fused into one opaque slug with no
    group to compare within.
    """
    _write(
        tmp_path,
        "lei-teste/art-1/original.md",
        _com_vigencia("art-1", "original", "2008-01-01", "2020-01-01"),
        _VALID_TEXTO,
    )
    _write(
        tmp_path,
        "lei-teste/art-1/lei-outra.md",
        _com_vigencia("art-1", "lei-outra", "2019-11-13", None),
        _VALID_TEXTO,
    )

    erros = check_vigencias(load_dispositivos(tmp_path))

    assert len(erros) == 1
    assert "both in force" in erros[0]


def test_a_gap_between_wordings_is_not_a_violation(tmp_path: Path) -> None:
    """P3 authors on demand, so a missing intermediate wording is expected, not broken."""
    _write(
        tmp_path,
        "lei-teste/art-1/original.md",
        _com_vigencia("art-1", "original", "2008-01-01", "2012-01-01"),
        _VALID_TEXTO,
    )
    _write(
        tmp_path,
        "lei-teste/art-1/lei-outra.md",
        _com_vigencia("art-1", "lei-outra", "2019-11-13", None),
        _VALID_TEXTO,
    )

    assert check_vigencias(load_dispositivos(tmp_path)) == []


def test_wordings_sharing_a_start_date_are_reported_not_crashed(tmp_path: Path) -> None:
    """Neither wording dating itself is a violation to *report*, never a traceback.

    Both docs read as starting at ``date.min`` and one is still open-ended, so
    ordering them by the whole window would compare ``None`` against a date.
    ``check_vigencias`` has to survive a bundle that is wrong — that is the
    only state it is ever run against.
    """
    aberta = {**_VALID_FRONTMATTER, "id": "lei-teste/art-1/original"}
    fechada = {
        **_VALID_FRONTMATTER,
        "id": "lei-teste/art-1/lei-outra",
        "redacao_dada_por": "lei-outra",
        "vigencia_fim": "2019-11-12",
    }
    _write(tmp_path, "lei-teste/art-1/original.md", aberta, _VALID_TEXTO)
    _write(tmp_path, "lei-teste/art-1/lei-outra.md", fechada, _VALID_TEXTO)

    erros = check_vigencias(load_dispositivos(tmp_path))

    assert len(erros) == 1
    assert "both in force" in erros[0]


def test_wordings_of_different_provisions_never_collide(tmp_path: Path) -> None:
    """Continuity is checked per provision, not across the whole norm."""
    _write(
        tmp_path,
        "lei-teste/art-1/original.md",
        _com_vigencia("art-1", "original", "2008-01-01", None),
        _VALID_TEXTO,
    )
    fm = {
        **_com_vigencia("art-2", "original", "2008-01-01", None),
        "componentes": [{"tipo": "artigo", "valor": "2"}],
    }
    _write(tmp_path, "lei-teste/art-2/original.md", fm, _VALID_TEXTO)

    assert check_vigencias(load_dispositivos(tmp_path)) == []


def test_backwards_validity_window_is_rejected(tmp_path: Path) -> None:
    """A wording cannot end before it starts."""
    fm = _com_vigencia("art-1", "original", "2019-01-01", "2008-01-01")
    _write(tmp_path, "lei-teste/art-1/original.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("precedes vigencia_inicio" in e for e in errors)


# --- fontes -------------------------------------------------------------


def test_fonte_must_be_a_web_url(tmp_path: Path) -> None:
    """Every fonte is published on the site as a link, so it has to be one."""
    fm = {**_VALID_FRONTMATTER, "fontes": ["Diário Oficial, p. 3"]}
    _write(tmp_path, "lei-teste/art-1/original.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    errors = validate_dispositivo(dispositivo)

    assert any("must be an http(s) URL" in e for e in errors)


def test_at_least_one_fonte_is_required(tmp_path: Path) -> None:
    """An untraceable transcription cannot be audited."""
    fm = {**_VALID_FRONTMATTER, "fontes": []}
    _write(tmp_path, "lei-teste/art-1/original.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    assert validate_dispositivo(dispositivo) != []


def test_multiple_fontes_are_allowed(tmp_path: Path) -> None:
    """A provision may be verifiable against more than one official publication."""
    fm = {
        **_VALID_FRONTMATTER,
        "fontes": ["https://example.invalid/a", "https://example.invalid/b"],
    }
    _write(tmp_path, "lei-teste/art-1/original.md", fm, _VALID_TEXTO)
    (dispositivo,) = load_dispositivos(tmp_path)

    assert validate_dispositivo(dispositivo) == []


# --- bundle-level -------------------------------------------------------


def test_validate_bundle_dispositivos_aggregates_every_doc(tmp_path: Path) -> None:
    """The bundle-level validator reports errors from every doc, not just the first."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    _write_norma(tmp_path)
    bad = {**_VALID_FRONTMATTER, "id": "lei-teste/art-2/original"}
    _write(tmp_path, "lei-teste/art-2/original.md", bad, "")

    errors = validate_bundle_dispositivos(tmp_path)

    assert errors
    assert all("art-2" in e for e in errors)


def test_dispositivo_ids_returns_every_doc_id(tmp_path: Path) -> None:
    """dispositivo_ids returns the full set of currently authored doc_ids."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    second = {
        **_VALID_FRONTMATTER,
        "id": "lei-teste/art-2/original",
        "componentes": [{"tipo": "artigo", "valor": "2"}],
    }
    _write(tmp_path, "lei-teste/art-2/original.md", second, _VALID_TEXTO)

    assert dispositivo_ids(tmp_path) == frozenset({"lei-teste/art-1/original", "lei-teste/art-2/original"})


# --- index regeneration -------------------------------------------------


def test_regenerate_dispositivos_index_is_a_noop_for_missing_directory(tmp_path: Path) -> None:
    """No dispositivos bundle yet means no index to regenerate."""
    missing = tmp_path / "does-not-exist"
    regenerate_dispositivos_index(missing)
    assert not missing.exists()


def test_regenerate_dispositivos_index_writes_per_norma_and_root_index(tmp_path: Path) -> None:
    """Regeneration writes both the norma index and the bundle-root index."""
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    _write_norma(tmp_path)

    regenerate_dispositivos_index(tmp_path)

    norma_index = (tmp_path / "lei-teste" / "index.md").read_text(encoding="utf-8")
    assert "art-1/original.md" in norma_index
    # The heading is the norm's canonical name, read from norma.md — not the
    # key, and not the same prose retyped in every dispositivo.
    assert "Lei de Teste nº 1/2026" in norma_index
    assert "redação original" in norma_index

    root_index = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "okf_version: '0.1'" in root_index
    assert "lei-teste/index.md" in root_index


def test_norma_index_labels_each_entry_with_its_full_address(tmp_path: Path) -> None:
    """Seven provisions of one article must not all read "Art. 20"."""
    for valor, slug in (("1", "art-20-par-1"), ("14", "art-20-par-14"), ("2", "art-20-par-2")):
        fm = {
            **_VALID_FRONTMATTER,
            "id": f"lei-teste/{slug}/original",
            "componentes": [
                {"tipo": "artigo", "valor": "20"},
                {"tipo": "paragrafo", "valor": valor},
            ],
        }
        _write(tmp_path, f"lei-teste/{slug}/original.md", fm, _VALID_TEXTO)
    _write_norma(tmp_path)

    regenerate_dispositivos_index(tmp_path)
    linhas = [
        linha
        for linha in (tmp_path / "lei-teste" / "index.md").read_text(encoding="utf-8").splitlines()
        if linha.startswith("- [")
    ]

    # Distinct labels, and in legal order — § 2º before § 14.
    assert linhas[0].startswith("- [art. 20, § 1º]")
    assert linhas[1].startswith("- [art. 20, § 2º]")
    assert linhas[2].startswith("- [art. 20, § 14]")


def test_regenerate_dispositivos_index_skips_a_malformed_path_instead_of_crashing(
    tmp_path: Path,
) -> None:
    """A doc whose path isn't <norma>/<endereço>/<redação> must not crash regeneration.

    Already reported by validate_dispositivo() — regeneration skips it rather
    than indexing it under a key nothing can resolve.
    """
    _write(tmp_path, "solto.md", {**_VALID_FRONTMATTER, "id": "solto"}, _VALID_TEXTO)
    _write(tmp_path, "lei-teste/art-1/original.md", _VALID_FRONTMATTER, _VALID_TEXTO)
    _write_norma(tmp_path)

    regenerate_dispositivos_index(tmp_path)  # must not raise

    root_index = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "lei-teste/index.md" in root_index
    assert "solto" not in root_index
