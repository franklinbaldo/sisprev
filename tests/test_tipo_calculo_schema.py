"""Unit tests for P17 — ``type: TipoCalculo``."""

from __future__ import annotations

import datetime
from pathlib import Path

import pytest
import tipo_calculo_schema as mod
from pydantic import ValidationError
from tipo_calculo_schema import (
    TipoCalculoFrontmatter,
    load_tipos_calculo,
    validate_tipos_calculo,
    valores_tipo_calculo_das_formas,
    valores_tipo_calculo_das_regras,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
TIPOS_DIR = REPO_ROOT / "okf" / "tipos-calculo"
REGRAS_DIR = REPO_ROOT / "okf" / "regras-sisprev" / "regras"
FORMAS_DIR = REPO_ROOT / "okf" / "formas-calculo"

VALORES_ESPERADOS = frozenset(
    {
        "Não identificado",
        "Valor Efetivo",
        "Valor Médio",
        "Remuneração de Contribuição",
        "Proporcionalidade Dias",
        "Valor Médio com Redutor da Idade",
        "Valor Efetivo mais 70% do que exceder do Teto RGPS",
        "Tipo Cálculo Nova Previdência Pensão por morte",
        "Tipo Cálculo Nova Previdência",
    }
)


def _doc(doc_id: str, valor: str, body: str | None = None) -> str:
    body = body or "# Estado da análise\n\nDescrição autorada.\n"
    return (
        "---\n"
        "type: TipoCalculo\n"
        f"id: {doc_id}\n"
        f"valor: {valor}\n"
        "autorado_por: franklinbaldo\n"
        "autorado_em: 2026-07-31\n"
        "---\n\n"
        f"{body}"
    )


def test_o_bundle_comitado_cobre_o_vocabulario_observado() -> None:
    """As regras e as projeções P16 resolvem integralmente no novo bundle."""
    observados = valores_tipo_calculo_das_regras(REGRAS_DIR)
    projetados = valores_tipo_calculo_das_formas(FORMAS_DIR)

    assert observados == VALORES_ESPERADOS
    assert projetados <= observados
    assert len(load_tipos_calculo(TIPOS_DIR)) == len(VALORES_ESPERADOS)
    assert (
        validate_tipos_calculo(
            TIPOS_DIR,
            valores_observados=observados,
            valores_projetados=projetados,
        )
        == []
    )


def test_diretorio_ausente_sem_referencias_nao_e_erro() -> None:
    """Um bundle sintético sem uso do enum não precisa autorar P17."""
    assert load_tipos_calculo(Path("/nao/existe")) == []
    assert validate_tipos_calculo(Path("/nao/existe")) == []


def test_valor_observado_sem_conceito_e_erro(tmp_path: Path) -> None:
    """Todo membro gravado numa regra precisa resolver em um concept."""
    errors = validate_tipos_calculo(
        tmp_path,
        valores_observados=frozenset({"Valor Efetivo"}),
    )
    assert errors == ["valor observado nas regras sem concept TipoCalculo: 'Valor Efetivo'"]


def test_valor_projetado_sem_conceito_e_erro(tmp_path: Path) -> None:
    """Toda projeção de uma FormaCalculo precisa resolver no vocabulário."""
    errors = validate_tipos_calculo(
        tmp_path,
        valores_projetados=frozenset({"Valor Médio"}),
    )
    assert errors == ["valor projetado por FormaCalculo sem concept TipoCalculo: 'Valor Médio'"]


def test_conceito_sem_ocorrencia_e_rejeitado(tmp_path: Path) -> None:
    """O bundle não pode inventar membro que nenhuma fonte operacional usa."""
    (tmp_path / "tipo-calculo-futuro.md").write_text(
        _doc("tipo-calculo-futuro", "Rótulo futuro"),
        encoding="utf-8",
    )
    errors = validate_tipos_calculo(tmp_path)
    assert errors == ["valor autorado sem ocorrência em regra ou projeção de FormaCalculo: 'Rótulo futuro'"]


def test_valor_repetido_em_dois_documentos_e_rejeitado(tmp_path: Path) -> None:
    """Um membro do enum tem uma única identidade no bundle."""
    (tmp_path / "tipo-calculo-a.md").write_text(
        _doc("tipo-calculo-a", "Valor Médio"),
        encoding="utf-8",
    )
    (tmp_path / "tipo-calculo-b.md").write_text(
        _doc("tipo-calculo-b", "Valor Médio"),
        encoding="utf-8",
    )
    errors = validate_tipos_calculo(
        tmp_path,
        valores_observados=frozenset({"Valor Médio"}),
    )
    assert errors == ["valor 'Valor Médio' repetido em tipo-calculo-a, tipo-calculo-b"]


def test_estado_da_analise_e_obrigatorio(tmp_path: Path) -> None:
    """O concept exige análise autorada, não apenas frontmatter."""
    (tmp_path / "tipo-calculo-valor-medio.md").write_text(
        _doc(
            "tipo-calculo-valor-medio",
            "Valor Médio",
            body="# Outra seção\n\nx\n",
        ),
        encoding="utf-8",
    )
    errors = validate_tipos_calculo(
        tmp_path,
        valores_observados=frozenset({"Valor Médio"}),
    )
    assert any('seção "Estado da análise" ausente ou vazia' in error for error in errors)


def test_valor_deve_ser_literal_e_sem_espacos_laterais() -> None:
    """A identidade preserva literalmente caixa, acentos e limites do valor."""
    with pytest.raises(ValidationError, match="sem espaços laterais"):
        TipoCalculoFrontmatter.model_validate(
            {
                "type": "TipoCalculo",
                "id": "tipo-calculo-valor-medio",
                "valor": " Valor Médio ",
                "autorado_por": "franklinbaldo",
                "autorado_em": datetime.date(2026, 7, 31),
            }
        )

    contract = TipoCalculoFrontmatter.model_validate(
        {
            "type": "TipoCalculo",
            "id": "tipo-calculo-valor-medio",
            "valor": "Valor Médio",
            "autorado_por": "franklinbaldo",
            "autorado_em": datetime.date(2026, 7, 31),
        }
    )
    assert contract.type == "TipoCalculo"
    assert contract.valor == "Valor Médio"
    assert contract.autorado_por == "franklinbaldo"
    assert contract.autorado_em == datetime.date(2026, 7, 31)


def test_o_modulo_nao_infere_formula_do_rotulo() -> None:
    """O concept documenta o enum; não o transforma em base, ajuste ou limitador."""
    termos_proibidos = ("infer", "mapea", "decompoe", "from_tipo", "forma_from")
    suspeitos = [
        nome
        for nome in dir(mod)
        if not nome.startswith("_")
        and callable(getattr(mod, nome))
        and any(termo in nome.lower() for termo in termos_proibidos)
    ]
    assert suspeitos == []
