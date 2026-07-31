"""Contracts for self-contained cycle reports."""

from __future__ import annotations

from pathlib import Path

from concept import parse_concept_doc

REPO_ROOT = Path(__file__).resolve().parent.parent
CICLOS_DIR = REPO_ROOT / "okf" / "regras-sisprev" / "ciclos"
REQUIRED_SECTIONS = (
    "Identificação",
    "Contexto acadêmico e histórico",
    "Dimensão social",
    "Cotejo jurídico",
    "Fluxo processual",
    "Entregável",
    "Resultado por regra",
    "Referências de outros ciclos",
    "Fontes legais consultadas",
    "Pendências que permanecem abertas",
    "Conclusão do ciclo",
)


def test_cycle_report_lives_in_the_cycle_concept() -> None:
    """Every cycle carries its own report and a result slot for each owned rule."""
    paths = sorted(CICLOS_DIR.glob("ciclo-*.md"))
    assert paths

    for path in paths:
        frontmatter, body = parse_concept_doc(path.read_text(encoding="utf-8"))

        assert frontmatter["type"] == "Ciclo"
        for section in REQUIRED_SECTIONS:
            assert f"## {section}" in body, f"{path.name}: seção {section!r} ausente"

        regras = frontmatter["regras"]
        assert isinstance(regras, list)
        for regra in regras:
            assert isinstance(regra, str)
            assert f"`{regra}`" in body, f"{path.name}: {regra} sem resultado no relatório"


def test_no_parallel_cycle_report_tree_exists() -> None:
    """A second report tree would recreate two competing sources of truth."""
    assert not (REPO_ROOT / "docs" / "relatorio" / "ciclos").exists()
    assert not (REPO_ROOT / "docs" / "relatorio" / "modelo-ciclo.md").exists()
