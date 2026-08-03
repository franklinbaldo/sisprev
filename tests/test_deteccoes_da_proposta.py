"""Os detectores da auditoria têm de alcançar também a regra que vai substituir.

O catálogo recebido foi auditado para tirar nome repetido e igualdade material.
Sem estes testes, a regra proposta — que ocupa exatamente a mesma linha de 27
colunas — poderia recolocar os dois defeitos e entrar no sistema sem que nada
acusasse, porque os detectores só percorriam o bundle legado.

O caso que mais importa é o de fronteira: a proposta que colide com uma regra
legada **que o grupo não substituiu**. Conferir as propostas só entre si
deixaria justamente esse passar, e é por isso que a checagem é sobre a
composição resolvida.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from bundle import Bundle
from deteccoes_da_proposta import bundle_da_composicao, detectar_na_composicao
from okf_common import DEFAULT_BUNDLE, DEFAULT_BUNDLE_PROPOSTO
from regra_proposta_schema import load_regras_propostas

if TYPE_CHECKING:
    from regra_proposta_schema import RegraProposta

CONJUNTO_DO_CICLO_1 = "ciclo-01-s6-fechamento"


@pytest.fixture(scope="module")
def bundle() -> Bundle:
    """O bundle legado comitado."""
    return Bundle.load(DEFAULT_BUNDLE)


@pytest.fixture(scope="module")
def propostas() -> list[RegraProposta]:
    """As regras propostas comitadas."""
    return load_regras_propostas(DEFAULT_BUNDLE_PROPOSTO)


def test_a_composicao_junta_o_que_sobra_do_legado_com_o_que_entra(
    bundle: Bundle, propostas: list[RegraProposta]
) -> None:
    """As substituídas saem, as propostas entram, o resto do catálogo fica."""
    composicao = bundle_da_composicao(CONJUNTO_DO_CICLO_1, bundle=bundle, propostas=propostas)

    ids = {regra.doc_id for regra in composicao.regras}
    substituidas = {"regra-0001", "regra-0002", "regra-0004"}

    assert not (ids & substituidas)
    assert "invalidez-cf88-original-acidente-em-servico" in ids
    # Uma regra que nenhum grupo do ciclo toca continua na composição.
    assert "regra-0010" in ids


def test_a_proposta_entra_como_regra_ativa(bundle: Bundle, propostas: list[RegraProposta]) -> None:
    """O P2 só compara ativas — uma proposta invisível a `active_regras` não seria conferida."""
    composicao = bundle_da_composicao(CONJUNTO_DO_CICLO_1, bundle=bundle, propostas=propostas)

    ativas = {regra.doc_id for regra in composicao.active_regras()}

    assert "invalidez-cf88-original-acidente-em-servico" in ativas


def test_a_proposta_do_ciclo_1_nao_introduz_deteccao_nova(
    bundle: Bundle, propostas: list[RegraProposta]
) -> None:
    """Estado atual: nenhuma das regras propostas recoloca um defeito conhecido.

    Este teste não é uma tautologia sobre o presente: ele falha no dia em que
    uma proposta nova reintroduzir nome repetido ou igualdade material, que é
    exatamente quando alguém precisa saber.
    """
    from bundle import collect_detections  # noqa: PLC0415

    base = {deteccao.fingerprint for deteccao in collect_detections(bundle)}
    composicao = bundle_da_composicao(CONJUNTO_DO_CICLO_1, bundle=bundle, propostas=propostas)
    ids_propostos = {regra.doc_id for regra in composicao.regras if not regra.doc_id.startswith("regra-")}

    novas = [
        deteccao
        for deteccao in detectar_na_composicao(CONJUNTO_DO_CICLO_1, bundle=bundle, propostas=propostas)
        if deteccao.fingerprint not in base and deteccao.regras & ids_propostos
    ]

    assert novas == []


def test_conjunto_sem_grupo_nao_reporta_o_catalogo_legado_de_novo(
    bundle: Bundle, propostas: list[RegraProposta]
) -> None:
    """A raiz não é uma proposta: a composição dela é o legado, já coberto pelo gate próprio.

    Sem esta guarda o gate levantaria ``CicloSemGruposError`` ao percorrer os
    conjuntos, derrubando o CLI inteiro num conjunto que não tem nada de
    errado.
    """
    assert detectar_na_composicao("catalogo-legado", bundle=bundle, propostas=propostas) == []


def test_conjunto_inexistente_nao_levanta(bundle: Bundle, propostas: list[RegraProposta]) -> None:
    """Resolução quebrada é reportada por `validate_conjuntos`, nunca duas vezes."""
    assert detectar_na_composicao("nao-existe", bundle=bundle, propostas=propostas) == []
