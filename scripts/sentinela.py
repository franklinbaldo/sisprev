"""RFC 0011 — o conjunto declarado das sentinelas de data (P5).

Fonte única do predicado **"limite não-sentinela"**, que já era critério de
auditoria em vigor antes de existir declaração: é com ele que a spec da regra
diz o que se confere ("todo limite não-sentinela deveria coincidir com uma data
declarada pelos dispositivos que a regra cita") e é ele que produz a fila de
conferência do levantamento das janelas temporais. Antes desta declaração o
predicado vivia em prosa, em quatro lugares, e dois discordavam — o P5 listava
três valores e o levantamento quatro, e os 230 limites não-sentinela publicados
só fecham com o conjunto de quatro.

**O que este módulo declara, e o que não declara.** Declara que estes quatro
valores são os que a coordenação da auditoria nomeou sentinela na decisão de
2026-07-17, isto é, valores que não pretendem nomear um marco. Nomear o
conjunto é **forma**. Dizer o que os membros *significam* — se `31/12/2099` quer
dizer "sem limite superior", se as três de piso são três grafias de um mesmo
sentido — é **mérito**, é a pergunta 4 da §5.3 do levantamento, e segue aberta.
Nada aqui a responde, e nada aqui deve passar a responder.

O conjunto é, portanto, **autorado** — registro de uma decisão, como uma entrada
de ``dispositivos:``. Ele não deriva de nada e não pode: "este valor não parece
um marco legal" é conclusão jurídica, e produzir conclusão jurídica plausível
por regra mecânica é o modo de falha que a RFC 0008 documentou com nove erros
reais. Daí que ``01/01/1969`` (``regra-0003``, ``data_direito_apos``, anterior à
própria CF/88) **fique fora**: é suspeita registrada (item 9 da fila de
conferência), e uma suspeita que entra no conjunto vira, sem ato de ninguém, a
decisão de que aquele limite não é critério.

Contrato completo em
[`docs/rfc/0011-sentinelas-de-data-como-conjunto-declarado.md`](../docs/rfc/0011-sentinelas-de-data-como-conjunto-declarado.md).
Puro de propósito — nenhum import de ``bundle``/``concept``, mesmo lugar
arquitetural de ``dispositivo_endereco.py``: quem define forma não pode depender
de quem carrega documento.
"""

from __future__ import annotations

import re
from enum import StrEnum

# Aceita a forma gravada (`DD/MM/AAAA HH:MM`) e a forma sem hora que o site e o
# relatório exibem (`formato.ts` tira a hora constante `00:00`). Validar formato
# **não** é trabalho deste módulo — quem faz isso é `_LEGACY_DATETIME_RE` no
# compilador; aqui um valor que não casa simplesmente não é sentinela.
_FORMA = re.compile(r"(\d{2}/\d{2}/\d{4})(?: \d{2}:\d{2})?")


class Sentinela(StrEnum):
    """Os quatro valores que a coordenação nomeou sentinela (P5, 2026-07-17).

    **O valor de cada membro é a string exatamente como gravada** no
    frontmatter e no CSV, e é por isso que a classe é uma ``StrEnum``:
    ``Sentinela.D_2099_12_31 == "31/12/2099 00:00"`` é verdadeiro, então nada
    no caminho de escrita muda e a constante **não pode virar uma
    representação nova**. Um enum de ``datetime.date`` seria serializado por
    alguém, algum dia, e o round-trip byte-idêntico com a planilha original
    morreria em silêncio — é o risco que a Q4 do RFC 0001 avaliou ao decidir
    manter as sentinelas como estão.

    **Os nomes dos membros não significam nada, de propósito.** É no nome que a
    interpretação entraria sem pedir licença: ``SEM_LIMITE_SUPERIOR``
    responderia a §5.3.4 do levantamento num identificador, e todo ``if`` que o
    lesse herdaria a resposta. ``D_2099_12_31`` é a data em ordem ISO —
    derivável do valor, portanto incapaz de divergir dele, e sem nenhum
    significado agregado.
    """

    D_1900_01_01 = "01/01/1900 00:00"
    D_1910_01_01 = "01/01/1910 00:00"
    D_1950_01_01 = "01/01/1950 00:00"
    D_2099_12_31 = "31/12/2099 00:00"


_POR_DATA: dict[str, Sentinela] = {membro.value[:10]: membro for membro in Sentinela}


def sentinela_de(valor: str) -> Sentinela | None:
    """A sentinela que ``valor`` é, ou ``None``. Nunca levanta.

    A hora é ignorada na classificação, como já é ignorada em todo o projeto na
    comparação de datas (nota de topo de ``site/src/lib/parse-sisprev.ts``): o
    que se compara é a parte de data.

    **Não existe, e não deve passar a existir, uma ``limite_valido()`` neste
    módulo.** Um limite não-sentinela não é um limite correto: ``15/12/1998`` é
    não-sentinela e é o candidato a erro de um dia da §3.1 do levantamento. O
    complemento de "sentinela" é "valor a conferir", nunca "valor bom", e uma
    função com esse nome faria a fila de conferência parecer resolvida.
    """
    forma = _FORMA.fullmatch(valor.strip())
    if forma is None:
        return None
    return _POR_DATA.get(forma.group(1))
