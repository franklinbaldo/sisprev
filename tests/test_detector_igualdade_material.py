"""Unit tests for the P2 detector (RFC 0001, P2) — synthetic regras, no disk.

Each test builds a tiny Bundle from hand-made Regra objects and asserts one
property of the detector: what distinguishes two regras materially and what
does not, that inactive regras drop out, that groups are exact, and that the
fingerprint is stable regardless of read order.
"""

from __future__ import annotations

from pathlib import Path

from bundle import Bundle, Regra
from detectors.igualdade_material import DETECTOR_ID, detect
from regra_schema import BODY_COLUMNS, FRONTMATTER_COLUMNS, FRONTMATTER_KEYS

_BODY_HEADING_KEYS = tuple(BODY_COLUMNS)


def _regra(
    regra_id: str,
    *,
    nome: str = "Regra padrão",
    status: str = "ativa",
    frontmatter: dict[str, str] | None = None,
    sections: dict[str, str] | None = None,
) -> Regra:
    """Build a Regra with every field empty by default, then apply overrides."""
    fm: dict[str, object] = {FRONTMATTER_KEYS[c]: "" for c in FRONTMATTER_COLUMNS}
    fm["nome"] = nome
    fm["status_regra"] = status
    if frontmatter:
        fm.update(frontmatter)
    secs = dict.fromkeys(_BODY_HEADING_KEYS, "")
    if sections:
        secs.update(sections)
    return Regra(id=regra_id, frontmatter=fm, sections=secs)


def _bundle(*regras: Regra) -> Bundle:
    return Bundle(bundle_dir=Path(), regras=tuple(regras), achados=())


def test_a_different_nome_does_not_distinguish_materially() -> None:
    """P2 ignores NOME: two regras differing only by nome are one group."""
    bundle = _bundle(
        _regra("regra-0001", nome="Regra A"),
        _regra("regra-0002", nome="Regra B (inciso III)"),
    )
    detections = detect(bundle)
    assert len(detections) == 1
    assert detections[0].regras == frozenset({"regra-0001", "regra-0002"})
    assert detections[0].detector == DETECTOR_ID


def test_a_domain_field_distinguishes_materially() -> None:
    """A differing domain field (e.g. sexo) splits the group — no detection."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0002", frontmatter={"sexo": "MASCULINO"}),
    )
    assert detect(bundle) == []


def test_a_body_section_distinguishes_materially() -> None:
    """A differing body section (a semantic column) splits the group."""
    fundamentacao = next(iter(_BODY_HEADING_KEYS))
    bundle = _bundle(
        _regra("regra-0001", sections={fundamentacao: "texto A"}),
        _regra("regra-0002", sections={fundamentacao: "texto B"}),
    )
    assert detect(bundle) == []


def test_an_administrative_field_does_not_distinguish() -> None:
    """status_auditoria (admin) is outside the material comparison — still one group."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"status_auditoria": "importada"}),
        _regra("regra-0002", frontmatter={"status_auditoria": "revisada"}),
    )
    detections = detect(bundle)
    assert len(detections) == 1
    assert detections[0].regras == frozenset({"regra-0001", "regra-0002"})


def test_inactive_regras_do_not_participate() -> None:
    """An inactive member drops out; a lone active member is no group."""
    bundle = _bundle(
        _regra("regra-0001", status="ativa"),
        _regra("regra-0002", status="inativa"),
    )
    assert detect(bundle) == []


def test_two_independent_groups_are_not_merged() -> None:
    """Distinct material signatures produce distinct detections."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0002", frontmatter={"sexo": "FEMININO"}),
        _regra("regra-0003", frontmatter={"sexo": "MASCULINO"}),
        _regra("regra-0004", frontmatter={"sexo": "MASCULINO"}),
    )
    detections = detect(bundle)
    groups = {d.regras for d in detections}
    assert groups == {
        frozenset({"regra-0001", "regra-0002"}),
        frozenset({"regra-0003", "regra-0004"}),
    }


def test_fingerprint_is_stable_regardless_of_read_order() -> None:
    """Permuting the regras must not change the group's fingerprint."""
    a = _regra("regra-0001")
    b = _regra("regra-0002")
    fp_forward = detect(_bundle(a, b))[0].fingerprint
    fp_reverse = detect(_bundle(b, a))[0].fingerprint
    assert fp_forward == fp_reverse
