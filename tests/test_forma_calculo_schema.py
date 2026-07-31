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
    "base": {
        "tipo": "totalidade_remuneracao_cargo_efetivo",
        "dispositivos": [_PAR_3],
    },
    "projecao_sisprev": {
        "tipo_calculo": "Valor Efetivo",
        "fidelidade": "exata",
    },
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


def _proporcional(ordem: int = 1) -> dict[str, object]:
    return {
        "tipo": "proporcional_tempo_contribuicao",
        "ordem": ordem,
        "dispositivos": [_INC_II],
    }


def _teto_remuneracao(ordem: int = 1) -> dict[str, object]:
    return {
        "tipo": "teto_remuneracao_cargo_efetivo",
        "ordem": ordem,
        "dispositivos": [_PAR_3],
    }


def test_the_committed_formas_bundle_validates() -> None:
    """O bundle autorado passa no próprio gate."""
    ids = dispositivo_ids(REPO_ROOT / "okf" / "dispositivos")
    assert validate_formas_calculo(FORMAS_DIR, ids) == []
    assert load_formas_calculo(FORMAS_DIR)


def test_a_missing_bundle_directory_is_not_an_error() -> None:
    """Bundle ausente e não referenciado não é pré-requisito global."""
    assert load_formas_calculo(Path("/nao/existe")) == []
    assert validate_formas_calculo(Path("/nao/existe"), frozenset()) == []


def test_fidelidade_diferente_de_exata_exige_justificativa() -> None:
    """Perda declarada sem razão escrita é omissão estrutural."""
    projecao = {
        "tipo_calculo": "Não identificado",
        "fidelidade": "sem_representacao",
    }
    with pytest.raises(ValidationError, match="exige justificativa"):
        FormaCalculoFrontmatter.model_validate(_fm(projecao_sisprev=projecao))

    projecao["justificativa"] = "O enum não representa a combinação."
    contrato = FormaCalculoFrontmatter.model_validate(_fm(projecao_sisprev=projecao))
    assert contrato.projecao_sisprev.fidelidade == "sem_representacao"


def test_fidelidade_exata_dispensa_justificativa() -> None:
    """Sem perda declarada não há justificativa obrigatória."""
    contrato = FormaCalculoFrontmatter.model_validate(_fm())
    assert contrato.projecao_sisprev.justificativa is None


def test_vocabulario_e_fechado() -> None:
    """Termo novo entra com conferência, não apenas por uso."""
    base = {
        "tipo": "media_dos_ultimos_36_meses",
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(base=base))

    ajuste = {
        "tipo": "bonus_professor",
        "ordem": 1,
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))


def test_cada_componente_exige_o_seu_dispositivo() -> None:
    """A proveniência por componente é obrigatória."""
    base = {"tipo": "totalidade_remuneracao_cargo_efetivo"}
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(base=base))

    ajuste = {
        "tipo": "proporcional_tempo_contribuicao",
        "ordem": 1,
    }
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))


def test_ref_malformada_e_repetida_sao_rejeitadas() -> None:
    """Links têm forma canônica e não se repetem no componente."""
    base = {
        "tipo": "totalidade_remuneracao_cargo_efetivo",
        "dispositivos": ["art. 40, § 3º"],
    }
    with pytest.raises(ValidationError, match="não é link OKF"):
        FormaCalculoFrontmatter.model_validate(_fm(base=base))

    base["dispositivos"] = [_PAR_3, _PAR_3]
    with pytest.raises(ValidationError, match="repetida"):
        FormaCalculoFrontmatter.model_validate(_fm(base=base))


def test_media_exige_percentual_e_competencia_inicial() -> None:
    """Média sem recorte percentual e marco inicial não é completa."""
    base = {
        "tipo": "media_remuneracoes_contribuicao",
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError, match="exige"):
        FormaCalculoFrontmatter.model_validate(_fm(base=base))

    base["percentual_periodo"] = 80
    base["competencia_inicial"] = "1994-07"
    contrato = FormaCalculoFrontmatter.model_validate(_fm(base=base))
    assert contrato.base.percentual_periodo == 80
    assert contrato.base.competencia_inicial == "1994-07"


def test_parametros_de_media_nao_cabem_em_outra_base() -> None:
    """Parâmetros específicos não vazam para outra base."""
    base = {
        "tipo": "totalidade_remuneracao_cargo_efetivo",
        "percentual_periodo": 80,
        "competencia_inicial": "1994-07",
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError, match="não aceita parâmetros de média"):
        FormaCalculoFrontmatter.model_validate(_fm(base=base))


def test_ordem_unifica_ajustes_e_limitadores() -> None:
    """O teto pode preceder a fração quando a norma assim manda."""
    contrato = FormaCalculoFrontmatter.model_validate(
        _fm(
            ajustes=[_proporcional(ordem=2)],
            limitadores=[_teto_remuneracao(ordem=1)],
        )
    )
    assert [operacao.tipo for operacao in contrato.operacoes()] == [
        "teto_remuneracao_cargo_efetivo",
        "proporcional_tempo_contribuicao",
    ]
    assert contrato.dispositivos() == [_PAR_3, _INC_II]


def test_ordem_repetida_ou_com_lacuna_e_rejeitada() -> None:
    """Sequência ambígua ou incompleta não pode parecer executável."""
    with pytest.raises(ValidationError, match="ordem repetida"):
        FormaCalculoFrontmatter.model_validate(
            _fm(
                ajustes=[_proporcional()],
                limitadores=[_teto_remuneracao()],
            )
        )

    with pytest.raises(ValidationError, match="ordem deve cobrir"):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[_proporcional(ordem=2)]))


def test_redutor_exige_aliquotas_e_marco() -> None:
    """O redutor muda de 3,5% para 5% em 2006."""
    ajuste: dict[str, object] = {
        "tipo": "redutor_idade_por_ano_antecipado",
        "ordem": 1,
        "dispositivos": [_INC_II],
    }
    with pytest.raises(ValidationError, match="exige"):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))

    ajuste.update(
        percentual_ate_marco=3.5,
        percentual_a_partir_marco=5,
        marco_alteracao="2006-01-01",
    )
    contrato = FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))
    assert contrato.ajustes[0].marco_alteracao == datetime.date(2006, 1, 1)


def test_cota_familiar_exige_tres_percentuais() -> None:
    """A cota exige base, incremento por dependente e máximo."""
    ajuste: dict[str, object] = {
        "tipo": "cota_familiar_por_dependente",
        "ordem": 1,
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError, match="exige"):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))

    ajuste.update(
        percentual_base=50,
        percentual_por_dependente=10,
        percentual_maximo=100,
    )
    contrato = FormaCalculoFrontmatter.model_validate(_fm(ajustes=[ajuste]))
    assert contrato.ajustes[0].percentual_base == 50


def test_limitador_de_excedente_exige_percentual() -> None:
    """Excedente sem percentual não expressa a regra."""
    limitador: dict[str, object] = {
        "tipo": "teto_rgps_mais_percentual_do_excedente",
        "ordem": 1,
        "dispositivos": [_PAR_3],
    }
    with pytest.raises(ValidationError, match="exige percentual_excedente"):
        FormaCalculoFrontmatter.model_validate(_fm(limitadores=[limitador]))

    limitador["percentual_excedente"] = _SETENTA_POR_CENTO
    contrato = FormaCalculoFrontmatter.model_validate(_fm(limitadores=[limitador]))
    assert contrato.limitadores[0].percentual_excedente == _SETENTA_POR_CENTO


def test_ajuste_repetido_e_rejeitado() -> None:
    """Repetição do mesmo tipo ainda não é modelada."""
    with pytest.raises(ValidationError, match="tipo repetido"):
        FormaCalculoFrontmatter.model_validate(
            _fm(
                ajustes=[
                    _proporcional(ordem=1),
                    _proporcional(ordem=2),
                ]
            )
        )


def test_referencia_a_dispositivo_inexistente_e_violacao(
    tmp_path: Path,
) -> None:
    """O vínculo tem de resolver no bundle de dispositivos."""
    doc = tmp_path / "forma-calculo-fantasma.md"
    frontmatter = _FRONTMATTER_MINIMO.format(
        doc_id="forma-calculo-fantasma",
        ref="/dispositivos/cf88/art-999/original.md",
    )
    doc.write_text(
        frontmatter + "# Como calcular\n\nx\n\n# Entradas e saídas\n\ny\n",
        encoding="utf-8",
    )
    ids = frozenset({"cf88/art-40-par-3/ec-20-1998"})
    erros = validate_formas_calculo(tmp_path, ids)
    assert any("não existe no bundle" in erro for erro in erros)


def test_secoes_obrigatorias_sao_exigidas(
    tmp_path: Path,
) -> None:
    """Fórmula e implementação permanecem opcionais."""
    doc = tmp_path / "forma-calculo-minima.md"
    frontmatter = _FRONTMATTER_MINIMO.format(
        doc_id="forma-calculo-minima",
        ref=_PAR_3,
    )
    ids = frozenset({"cf88/art-40-par-3/ec-20-1998"})

    doc.write_text(
        frontmatter + "# Como calcular\n\nprosa\n\n" + "# Entradas e saídas\n\nprosa\n",
        encoding="utf-8",
    )
    assert validate_formas_calculo(tmp_path, ids) == []

    doc.write_text(
        frontmatter + "# Como calcular\n\nsó isto\n",
        encoding="utf-8",
    )
    erros = validate_formas_calculo(tmp_path, ids)
    assert any("Entradas e saídas" in erro for erro in erros)


def test_o_modulo_nao_expoe_mapeador_do_enum_legado() -> None:
    """Rótulo legado não vira componentes por inferência."""
    termos = ("infer", "deriv", "mapea", "from_tipo", "parse_tipo")
    suspeitos = [
        nome
        for nome in dir(mod)
        if not nome.startswith("_")
        and callable(getattr(mod, nome))
        and any(termo in nome.lower() for termo in termos)
    ]
    assert suspeitos == []
