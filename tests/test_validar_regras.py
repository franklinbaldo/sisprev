"""P10 validator: camada 1 (estrutural) e camada 2 (detector P2 + bidirecionalidade)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from achado_schema import load_achados
from csv_to_okf import convert as csv_to_okf
from okf_common import ORIGINAL_CSV
from validar_regras import (
    P2_DETECTOR_CODE,
    check_p2_bidirectional,
    check_structural,
    create_missing_p2_achados,
    detect_p2_groups,
    run,
)

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def bundle_dir(tmp_path: Path) -> Path:
    """A fresh bundle built from the real source CSV, no achados yet."""
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def test_check_structural_is_clean_on_a_fresh_bundle(bundle_dir: Path) -> None:
    """A freshly bootstrapped bundle has no structural violations."""
    assert check_structural(bundle_dir) == []


def test_detect_p2_groups_finds_the_known_real_groups(bundle_dir: Path) -> None:
    """The detector must find every group of materially-identical active regras.

    Confirmed against the real import: at minimum the 5 groups found by
    manual inspection during the RFC discussion, ignoring NOME per P2.
    """
    groups = detect_p2_groups(bundle_dir)
    group_id_sets = [set(g) for g in groups]

    expected_minimum = [
        {"regra-0012", "regra-0013"},
        {"regra-0014", "regra-0015"},
        {"regra-0065", "regra-0066"},
        {"regra-0068", "regra-0069", "regra-0070"},
        {"regra-0074", "regra-0075", "regra-0076", "regra-0077"},
    ]
    for expected in expected_minimum:
        assert expected in group_id_sets


def test_detect_p2_groups_ignores_inactive_regras(bundle_dir: Path) -> None:
    """An inactive member of an otherwise-identical pair must drop out of the group.

    regra-0013.md has no explicit status_regra (defaults to "ativa" —
    P2.1); inserting the field right after the opening "---" marks it
    inativa without disturbing the rest of the frontmatter.
    """
    doc = bundle_dir / "regras" / "regra-0013.md"
    text = doc.read_text(encoding="utf-8")
    doc.write_text(text.replace("---\n", "---\nstatus_regra: inativa\n", 1), encoding="utf-8")

    groups = detect_p2_groups(bundle_dir)
    assert not any({"regra-0012", "regra-0013"} <= set(g) for g in groups)


def test_check_p2_bidirectional_flags_undocumented_groups(bundle_dir: Path) -> None:
    """Before any achado exists, every detected group is a P14_DETECTOR_SEM_ACHADO violation."""
    violations = check_p2_bidirectional(bundle_dir)
    codes = {v.code for v in violations}
    assert codes == {"P14_DETECTOR_SEM_ACHADO"}
    assert len(violations) == len(detect_p2_groups(bundle_dir))


def test_create_missing_p2_achados_makes_the_bundle_clean(bundle_dir: Path) -> None:
    """Bootstrapping achados for every detected group leaves zero violations."""
    created = create_missing_p2_achados(bundle_dir)

    assert len(created) == len(detect_p2_groups(bundle_dir))
    assert run(bundle_dir) == []


def test_created_achados_are_neutral_and_valid(bundle_dir: Path) -> None:
    """Bootstrapped achados state the mechanical fact only — no inactivation is proposed."""
    create_missing_p2_achados(bundle_dir)

    achados = load_achados(bundle_dir)
    assert len(achados) > 0
    for achado in achados:
        fm = achado.frontmatter
        assert fm["detector"] == P2_DETECTOR_CODE
        assert fm["situacao"] == "aberto"
        assert "motivo_inativacao" not in fm
        assert "regra_canonica" not in fm


def test_create_missing_p2_achados_is_idempotent(bundle_dir: Path) -> None:
    """Running the bootstrap twice must not create duplicate achados for the same group."""
    create_missing_p2_achados(bundle_dir)
    second_run = create_missing_p2_achados(bundle_dir)

    assert second_run == []
    assert run(bundle_dir) == []


def test_breaking_a_documented_group_is_flagged(bundle_dir: Path) -> None:
    """P14.6 bidirectionality: an achado no longer matching a detected group must fail."""
    create_missing_p2_achados(bundle_dir)

    # Break the regra-0012/regra-0013 group by editing one member's data —
    # the achado documenting it now points at a group that no longer exists.
    regra_doc = bundle_dir / "regras" / "regra-0012.md"
    regra_text = regra_doc.read_text(encoding="utf-8")
    regra_doc.write_text(regra_text.replace("sexo: AMBOS", "sexo: MASCULINO", 1), encoding="utf-8")

    violations = check_p2_bidirectional(bundle_dir)
    codes = {v.code for v in violations}
    assert "P14_ACHADO_SEM_DETECTOR" in codes
