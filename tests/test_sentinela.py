"""RFC 0011 — o conjunto declarado das sentinelas, amarrado à importação congelada.

As asserções sobre o dado são todas contra ``data/raw/regras-sisprev.csv``, que
é **imutável para sempre**: são números que não envelhecem, e uma correção de
data no bundle vivo (campo deployável, veículo é `Conjunto` proposto) não as
falseia. Nada aqui roda sobre o bundle vivo de propósito — uma regra não fica
inválida por ter sentinela, 49% dos limites têm.
"""

from __future__ import annotations

import pandas as pd
from okf_common import ORIGINAL_CSV
from regra_schema import COLUMNS
from sentinela import Sentinela, sentinela_de

# As quatro colunas de data derivadas do mapa normativo (P13.2), nunca
# reescritas à mão aqui: se uma coluna de data for renomeada em COLUMNS, este
# teste acompanha em vez de conferir uma coluna que não existe mais.
COLUNAS_DE_DATA: tuple[str, ...] = tuple(c.csv_name for c in COLUMNS if c.tipo.startswith("datetime"))

QUANTAS_COLUNAS_DE_DATA = 4
LINHAS_DA_IMPORTACAO = 112
TOTAL_DE_LIMITES = 448
LIMITES_SENTINELA = 218
LIMITES_NAO_SENTINELA = 230

# A posição em que cada valor **foi observado** na importação — fato sobre o
# dado, não parte da definição. É por isso que mora aqui e não como atributo de
# `Sentinela`: um campo `posicao` no enum convidaria a `if posicao == "superior"`,
# que é interpretar (§5.3.4 do levantamento segue aberta).
POSICAO_OBSERVADA: dict[Sentinela, frozenset[str]] = {
    Sentinela.D_1900_01_01: frozenset({"DATA_ADM_APOS", "DATA_DIREITO_APOS"}),
    Sentinela.D_1910_01_01: frozenset({"DATA_ADM_APOS", "DATA_DIREITO_APOS"}),
    Sentinela.D_1950_01_01: frozenset({"DATA_ADM_APOS", "DATA_DIREITO_APOS"}),
    Sentinela.D_2099_12_31: frozenset({"DATA_ADM_ATE", "DATA_DIREITO_ATE"}),
}


def _importacao() -> pd.DataFrame:
    """A importação congelada, lida como as conversões a leem (linha branca do Sheets à parte)."""
    return pd.read_csv(ORIGINAL_CSV, skiprows=1, keep_default_na=False, dtype=str)


def _limites() -> list[str]:
    """Os 448 valores das quatro colunas de data, na importação congelada."""
    tabela = _importacao()
    return [str(valor) for coluna in COLUNAS_DE_DATA for valor in tabela[coluna]]


def test_membro_e_igual_a_string_gravada() -> None:
    """A garantia que sustenta a escolha de ``StrEnum``: o membro *é* o valor gravado.

    Se isto deixar de valer, a constante virou uma representação nova e o
    round-trip byte-idêntico com a planilha original está em risco (Q4).
    """
    assert Sentinela.D_2099_12_31 == "31/12/2099 00:00"
    assert f"{Sentinela.D_1950_01_01}" == "01/01/1950 00:00"


def test_classifica_a_forma_gravada_e_a_forma_sem_hora() -> None:
    """A hora é ignorada, como em todo o resto do projeto (`parse-sisprev.ts`)."""
    assert sentinela_de("31/12/2099 00:00") is Sentinela.D_2099_12_31
    assert sentinela_de("31/12/2099") is Sentinela.D_2099_12_31
    assert sentinela_de("  01/01/1910 00:00  ") is Sentinela.D_1910_01_01


def test_nao_sentinela_devolve_none_sem_levantar() -> None:
    """Inclui o que *parece* sentinela e não é — nada aqui coage nem levanta."""
    assert sentinela_de("31/12/2003 00:00") is None
    assert sentinela_de("15/12/1998 00:00") is None
    assert sentinela_de("") is None
    assert sentinela_de("banana") is None
    # Não pode casar por prefixo: o ano tem quatro dígitos, não "os quatro
    # primeiros de cinco".
    assert sentinela_de("01/01/19000") is None


def test_mil_novecentos_e_sessenta_e_nove_fica_fora() -> None:
    """`01/01/1969` é suspeita registrada, não membro — e a exclusão é deliberada.

    Ocorre na importação (`regra-0003`, `data_direito_apos`, anterior à própria
    CF/88) e é o item 9 da fila de conferência do levantamento. Uma suspeita que
    entra no conjunto vira, sem ato de ninguém, a decisão de que aquele limite
    não é critério — o modo de falha da RFC 0008. Se a coordenação confirmar que
    é sentinela, este teste muda junto com o enum, por edição autorada.
    """
    assert sentinela_de("01/01/1969 00:00") is None
    assert "01/01/1969 00:00" in _limites()


def test_nenhum_membro_orfao() -> None:
    """Todo membro ocorre ao menos uma vez na importação congelada.

    Um membro que ninguém usa é conjunto que cresceu por palpite. E é
    exatamente por não haver esta asserção que `01/01/1900` — presente numa
    única linha, a `regra-0087` — ficou fora da lista do P5 por dois meses.
    """
    limites = set(_limites())
    ausentes = [membro.name for membro in Sentinela if membro.value not in limites]
    assert ausentes == []


def test_posicao_observada_de_cada_sentinela() -> None:
    """As três de piso só em colunas `APOS`, `31/12/2099` só em colunas `ATE`.

    Observação sobre a importação, não definição: se uma importação futura
    quebrar isso, queremos saber — não porque o conjunto esteja errado, mas
    porque a convenção da planilha mudou.
    """
    tabela = _importacao()
    observado = {
        membro: frozenset(coluna for coluna in COLUNAS_DE_DATA if (tabela[coluna] == membro.value).any())
        for membro in Sentinela
    }
    assert observado == POSICAO_OBSERVADA


def test_a_populacao_que_a_fila_de_conferencia_conta() -> None:
    """218 sentinelas e 230 limites não-sentinela, dos 448 da importação.

    230 é o total que a §3 do levantamento publica, e é o número que só fecha
    com o conjunto de quatro — com os três do P5 original seriam 232. É esta
    asserção que impede a divergência de voltar.
    """
    assert len(COLUNAS_DE_DATA) == QUANTAS_COLUNAS_DE_DATA
    assert len(_importacao()) == LINHAS_DA_IMPORTACAO

    limites = _limites()
    sentinelas = [valor for valor in limites if sentinela_de(valor) is not None]
    assert len(limites) == TOTAL_DE_LIMITES
    assert len(sentinelas) == LIMITES_SENTINELA
    assert len(limites) - len(sentinelas) == LIMITES_NAO_SENTINELA


def test_vazio_nao_ocorre_em_coluna_de_data() -> None:
    """A asserção que sustenta a célula `semantica_vazio` corrigida (P13.2).

    O mapa normativo dizia, para as quatro colunas de data, que a semântica de
    vazio era "sentinela — preservada, não interpretada". Vazio simplesmente não
    ocorre: descrevia um caso que não acontece e deixava sem descrição o que
    acontece em 49% dos limites.
    """
    assert [valor for valor in _limites() if not valor.strip()] == []
