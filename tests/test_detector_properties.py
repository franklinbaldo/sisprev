"""Property-based tests (Hypothesis) for the P2 detector and fingerprints (RFC 0001).

Complementary to the unit tests, not a replacement: these assert invariants
that hold for arbitrary inputs — read order never changes a fingerprint,
changing an ignored field never changes a detection, and changing a semantic
field always does. pytest is the runner; Hypothesis generates the inputs.
"""

from __future__ import annotations

from pathlib import Path

from bundle import Bundle, Regra
from detectors.igualdade_material import detect
from hypothesis import given
from hypothesis import strategies as st
from regra_schema import FRONTMATTER_COLUMNS, FRONTMATTER_KEYS

_IDS = st.lists(
    st.integers(min_value=1, max_value=99).map(lambda n: f"regra-{n:04d}"),
    min_size=2,
    max_size=6,
    unique=True,
)


def _regra(regra_id: str, *, nome: str = "n", sexo: str = "") -> Regra:
    fm: dict[str, object] = {FRONTMATTER_KEYS[c]: "" for c in FRONTMATTER_COLUMNS}
    fm["nome"] = nome
    fm["status_regra"] = "ativa"
    fm["sexo"] = sexo
    return Regra(id=regra_id, frontmatter=fm, sections={})


def _bundle(regras: list[Regra]) -> Bundle:
    return Bundle(bundle_dir=Path(), regras=tuple(regras), achados=())


@given(ids=_IDS)
def test_read_order_never_changes_the_fingerprint(ids: list[str]) -> None:
    """Permuting the identical regras yields the same single detection fingerprint."""
    forward = detect(_bundle([_regra(i) for i in ids]))
    reverse = detect(_bundle([_regra(i) for i in reversed(ids)]))
    assert len(forward) == len(reverse) == 1
    assert forward[0].fingerprint == reverse[0].fingerprint


@given(ids=_IDS, names=st.lists(st.text(min_size=1, max_size=8), min_size=2, max_size=6))
def test_renaming_never_changes_the_detection(ids: list[str], names: list[str]) -> None:
    """NOME is ignored: distinct names over identical regras stay one group."""
    regras = [_regra(rid, nome=names[i % len(names)]) for i, rid in enumerate(ids)]
    detections = detect(_bundle(regras))
    assert len(detections) == 1
    assert detections[0].regras == frozenset(ids)


@given(ids=_IDS)
def test_a_semantic_field_always_splits_the_group(ids: list[str]) -> None:
    """Giving one member a distinct SEXO removes it from the group."""
    regras = [_regra(rid) for rid in ids]
    odd = regras[0]
    regras[0] = _regra(odd.id, sexo="MASCULINO")
    detections = detect(_bundle(regras))
    for detection in detections:
        assert odd.id not in detection.regras
