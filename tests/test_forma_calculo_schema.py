"""Unit tests for P16 — `type: FormaCalculo`."""

from __future__ import annotations

import datetime
from pathlib import Path

import forma_calculo_schema as mod
import pytest
from dispositivo_schema import dispositivo_ids
from forma_calculo_schema import (
    FormaCalculoFrontmatter,
    load_formas_calculo,
    validate_formas_calculo,
)
from pydantic import ValidationError

REPO_ROOT = Path(__file__).resolve().parent.parent
FORMAS_DIR = REPO_ROOT / "okf" / "formas-calculo"

_PAR_3 = "/dispositivos/cf88/art-40-par-3/ec-20-1998.md"
_INC_II = "/dispositivos/cf88/art-40-par-1-inc-ii/ec-20-1998.md"
_SETENTA_POR_CENTO = 70.0

_BASE_FM: dict[str, object] = {
    "type": "FormaCalculo",
    "id": "forma-calculo-exemplo",
    "nome": "Exemplo",
    "base": {"tipo": "totalidade_remuneracao_cargo_efetivo", "dispositivos": [_PAR_3]},
    "projecao_sisprev": {"tipo_calculo": "Valor Efetivo", "fidelidade": "exata"},
    "autorado_por": "franklinbaldo",
    "autorado_em": datetime.date(2026, 7, 30),
}

_FRONTMATTER_MINIMO = (
    "---\n"
    "type: FormaCalculo\n"
    "id: {doc_id}\n"
    "nome: Mínima\n"
    "base:\n"
    "  tipo: totalidade_remuneracao_cargo_efetivo\n"
    "  dispositivos:\n"
    "    - {ref}\n"
    "projecao_sisprev:\n"
    "  tipo_calculo: Valor Efetivo\n"
    "  fidelidade: exata\n"
    "autorado_por: franklinbaldo\n"
    "autorado_em: 2026-07-30\n"
    "---\n\n"
)


def _fm(**overrides: object) -> dict[str, object]:
    return {**_BASE_FM, **overrides}


def test_the_committed_formas_bundle_validates() -> None:
    """O bundle autorado passa no próprio gate — contrato de CI, não teste sintético."""
    ids = dispositivo_ids(REPO_ROOT / "okf" / "dispositivos")
    assert validate_formas_calculo(FORMAS_DIR, ids) == []
    assert load_formas_calculo(FORMAS_DIR), "o bundle não deve estar vazio"


def test_a_missing_bundle_directory_is_not_an_error() -> None:
    """Introduzir o bundle nunca pode ser pré-requisito para o resto validar."""
    assert load_formas_calculo(Path("/nao/existe")) == []
    assert validate_formas_calculo(Path("/nao/existe"), frozenset()) == []


def test_fidelidade_diferente_de_exata_exige_justificativa() -> None:
    """Perda declarada sem razão escrita é omissão estrutural."""
    with pytest.raises(ValidationError, match="exige justificativa"):
        FormaCalculoFrontmatter.model_validate(
            _fm(projecao_sisprev={"tipo_calculo": "Não identificado", "fidelidade": "sem_representacao"})
        )
    ok = FormaCalculoFrontmatter.model_validate(
        _fm(
            projecao_sisprev={
                "tipo_calculo": "Não identificado",
                "fidelidade": "sem_representacao",
                "justificativa": "nenhum rótulo combina base efetiva com proporção",
            }
        )
    )
    assert ok.projecao_sisprev.fidelidade == "sem_representacao"


def test_fidelidade_exata_dispensa_justificativa() -> None:
    """Sem perda declarada não há razão obrigatória a escrever."""
    contrato = FormaCalculoFrontmatter.model_validate(_fm())
    assert contrato.projecao_sisprev.justificativa is None


def test_vocabulario_e_fechado() -> None:
    """Termo novo entra com a conferência que o sustenta, nunca apenas por uso."""
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(
            _fm(base={"tipo": "media_dos_ultimos_36_meses", "dispositivos": [_PAR_3]})
        )
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(
            _fm(ajustes=[{"tipo": "bonus_professor", "ordem": 1, "dispositivos": [_PAR_3]}])
        )


def test_cada_componente_exige_o_seu_dispositivo() -> None:
    """A proveniência por componente diz qual norma funda qual operação."""
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(base={"tipo": "totalidade_remuneracao_cargo_efetivo"}))
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(
            _fm(base={"tipo": "totalidade_remuneracao_cargo_efetivo", "dispositivos": []})
        )
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(
            _fm(ajustes=[{"tipo": "proporcional_tempo_contribuicao", "ordem": 1}])
        )


def test_ref_malformada_e_repetida_no_componente_sao_rejeitadas() -> None:
    """Referências têm forma canônica e não se repetem dentro do componente."""
    with pytest.raises(ValidationError, match="não é link OKF"):
        FormaCalculoFrontmatter.model_validate(
            _fm(base={"tipo": "totalidade_remuneracao_cargo_efetivo", "dispositivos": ["art. 40, § 3º"]})
        )
    with pytest.raises(ValidationError, match="repetida"):
        FormaCalculoFrontmatter.model_validate(
            _fm(base={"tipo": "totalidade_remuneracao_cargo_efetivo", "dispositivos": [_PAR_3, _PAR_3]})
        )


def test_media_exige_percentual_e_competencia_inicial() -> None:
    """Uma média sem período selecionado nem marco inicial não é fórmula completa."""
    base = {"tipo": "media_remuneracoes_contribuicao", "dispositivos": [_PAR_3]}
    with pytest.raises(ValidationError, match="exige"):
        FormaCalculoFrontmatter.model_validate(_fm(base=base))

    contrato = FormaCalculoFrontmatter.model_validate(
        _fm(base={**base, "percentual_periodo": 80, "competencia_inicial": "1994-07"})
    )
    assert contrato.base.percentual_periodo == 80
    assert contrato.base.competencia_inicial == "1994-07"


def test_parametros_de_media_nao_cabem_em_outra_base() -> None:
    """Parâmetros específicos não vazam para bases de outra natureza."""
    with pytest.raises(ValidationError, match="não aceita parâmetros de média"):
        FormaCalculoFrontmatter.model_validate(
            _fm(
                base={
                    "tipo": "totalidade_remuneracao_cargo_efetivo",
                    "percentual_periodo": 80,
                    "competencia_inicial": "1994-07",
                    "dispositivos": [_PAR_3],
                }
            )
        )


def test_ordem_unifica_ajustes_e_limitadores() -> None:
    """O teto pode preceder a fração, como mandam LCE 432 art. 17 e LCE 1.100 art. 26."""
    contrato = FormaCalculoFrontmatter.model_validate(
        _fm(
            ajustes=[
                {"tipo": "proporcional_tempo_contribuicao", "ordem": 2, "dispositivos": [_INC_II]}
            ],
            limitadores=[
                {"tipo": "teto_remuneracao_cargo_efetivo", "ordem": 1, "dispositivos": [_PAR_3]}
            ],
        )
    )
    assert [operacao.tipo for operacao in contrato.operacoes()] == [
        "teto_remuneracao_cargo_efetivo",
        "proporcional_tempo_contribuicao",
    ]
    assert contrato.dispositivos() == [_PAR_3, _INC_II]


def test_ordem_repetida_ou_com_lacuna_e_rejeitada() -> None:
    """Uma sequência ambígua ou incompleta não pode parecer executável."""
    with pytest.raises(ValidationError, match="ordem repetida"):
        FormaCalculoFrontmatter.model_validate(
            _fm(
                ajustes=[{"tipo": "proporcional_tempo_contribuicao", "ordem": 1, "dispositivos": [_INC_II]}],
                limitadores=[
                    {"tipo": "teto_remuneracao_cargo_efetivo", "ordem": 1, "dispositivos": [_PAR_3]}
                ],
            )
        )
    with pytest.raises(ValidationError, match="ordem deve cobrir"):
        FormaCalculoFrontmatter.model_validate(
            _fm(ajustes=[{"tipo": "proporcional_tempo_contribuicao", "ordem": 2, "dispositivos": [_INC_II]}])
        )


def test_redutor_de_idade_exige_as_duas_aliquotas_e_o_marco() -> None:
    """O redutor da EC 41 art. 2º muda de 3,5% para 5% em 2006."""
    ajuste: dict[str, object] = {
        "tipo": "redutor_idade_por_ano_antecipado",
        "ordem": 1,
        "dispositivos": [_INC_II],
    }
    with pytest.raises(ValidationError, match="exige"):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))

    contrato = FormaCalculoFrontmatter.model_validate(
        _fm(
            ajustes=[
                {
                    **ajuste,
                    "percentual_ate_marco": 3.5,
                    "percentual_a_partir_marco": 5,
                    "marco_alteracao": "2006-01-01",
                }
            ]
        )
    )
    assert contrato.ajustes[0].marco_alteracao == datetime.date(2006, 1, 1)


def test_cota_familiar_exige_base_incremento_e_maximo() -> None:
    """A cota de pensão é 50% + 10 pontos por dependente, limitada a 100%."""
    ajuste: dict[str, object] = {
        "tipo": "cota_familiar_por_dependente",
        "ordem": 1,
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError, match="exige"):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))

    contrato = FormaCalculoFrontmatter.model_validate(
        _fm(
            ajustes=[
                {
                    **ajuste,
                    "percentual_base": 50,
                    "percentual_por_dependente": 10,
                    "percentual_maximo": 100,
                }
            ]
        )
    )
    assert contrato.ajustes[0].percentual_base == 50


def test_limitador_de_excedente_exige_o_percentual() -> None:
    """Dizer que há excedente sem dizer quanto é menos do que a norma diz."""
    limitador: dict[str, object] = {
        "tipo": "teto_rgps_mais_percentual_do_excedente",
        "ordem": 1,
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError, match="exige percentual_excedente"):
        FormaCalculoFrontmatter.model_validate(_fm(limitadores=[limitador]))
    ok = FormaCalculoFrontmatter.model_validate(
        _fm(limitadores=[{**limitador, "percentual_excedente": _SETENTA_POR_CENTO}])
    )
    assert ok.limitadores[0].percentual_excedente == _SETENTA_POR_CENTO


def test_ajuste_repetido_e_rejeitado() -> None:
    """Repetição do mesmo tipo ainda não é modelada."""
    with pytest.raises(ValidationError, match="tipo repetido"):
        FormaCalculoFrontmatter.model_validate(
            _fm(
                ajustes=[
                    {"tipo": "proporcional_tempo_contribuicao", "ordem": 1, "dispositivos": [_INC_II]},
                    {"tipo": "proporcional_tempo_contribuicao", "ordem": 2, "dispositivos": [_PAR_3]},
                ]
            )
        )


def test_referencia_a_dispositivo_inexistente_e_violacao(tmp_path: Path) -> None:
    """O vínculo tem de resolver no bundle de dispositivos."""
    doc = tmp_path / "forma-calculo-fantasma.md"
    doc.write_text(
        _FRONTMATTER_MINIMO.format(
            doc_id="forma-calculo-fantasma", ref="/dispositivos/cf88/art-999/original.md"
        )
        + "# Como calcular\n\nx\n\n# Entradas e saídas\n\ny\n",
        encoding="utf-8",
    )
    erros = validate_formas_calculo(tmp_path, frozenset({"cf88/art-40-par-3/ec-20-1998"}))
    assert any("não existe no bundle" in erro for erro in erros)


def test_secoes_obrigatorias_sao_exigidas_e_as_outras_nao(tmp_path: Path) -> None:
    """Fórmula e implementação ficam opcionais para evitar fachada."""
    doc = tmp_path / "forma-calculo-minima.md"
    frontmatter = _FRONTMATTER_MINIMO.format(doc_id="forma-calculo-minima", ref=_PAR_3)
    ids = frozenset({"cf88/art-40-par-3/ec-20-1998"})

    doc.write_text(
        frontmatter + "# Como calcular\n\nprosa\n\n# Entradas e saídas\n\nprosa\n", encoding="utf-8"
    )
    assert validate_formas_calculo(tmp_path, ids) == []

    doc.write_text(frontmatter + "# Como calcular\n\nsó isto\n", encoding="utf-8")
    erros = validate_formas_calculo(tmp_path, ids)
    assert any("Entradas e saídas" in erro for erro in erros)


def test_o_modulo_nao_expoe_mapeador_do_enum_legado() -> None:
    """O rótulo legado nunca vira componentes por inferência automática."""
    suspeitos = [
        nome
        for nome in dir(mod)
        if not nome.startswith("_")
        and callable(getattr(mod, nome))
        and any(termo in nome.lower() for termo in ("infer", "deriv", "mapea", "from_tipo", "parse_tipo"))
    ]
    assert suspeitos == []
