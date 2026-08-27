#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "okf-parser>=0.1.0",
# ]
# ///
"""Confere a decomposição da incapacidade permanente da LCE 1.100/2021.

O Bloco C do Ciclo 1 passou de duas coortes de ingresso para **três famílias
mutuamente excludentes**, porque a lei condiciona o cálculo à posição do
servidor perante o regime de previdência complementar, e não só à data:

- art. 24, *caput* e art. 25 — ambos exigem que o servidor **não** tenha feito
  a opção do § 16 do art. 40 da Constituição Federal;
- art. 24, § 11 — sujeita ao teto do RGPS quem **está** sujeito àquele regime;
- art. 24, § 12 — estende o mesmo teto a quem ingressou a partir de 06/11/2018.

Sem a terceira família, o servidor que optou pelo regime complementar não é
alcançado por nenhuma das duas primeiras: os dois artigos de base o excluem
pelo próprio caput. É esse buraco que este teste existe para não deixar voltar.

O que se confere aqui é **estrutura**, não mérito: vinte causas em cada
família, as mesmas vinte nas três, o predicado de vínculo com o regime
complementar coerente com a família, e janelas de ingresso que particionam a
linha do tempo sem buraco nem sobreposição.

**A semântica da seleção é cumulativa, e o teste a demonstra.** A família de um
caso resulta da conjugação dos campos, não de uma lista de alternativas: nas
duas primeiras é preciso estar na janela **e** não ter optado pelo regime
complementar; só a terceira admite duas vias — ingresso a partir de 06/11/2018
**ou** opção expressa, esta em qualquer data. Por isso `selecao_por` só existe
na terceira: nas outras, repetir a janela e a ausência de opção numa lista
declarada disjuntiva faria ler como "janela ou ausência de opção" o que a lei
exige junto.

Em vez de comparar conjuntos de strings, `familia_de` reconstrói a expressão
lógica a partir do que as próprias unidades gravam e os cenários sintéticos a
exercitam nos dois eixos (data e opção).
"""

from __future__ import annotations

import datetime as dt
import itertools
import logging
from pathlib import Path

from okf_parser.parser import parse_document

logger = logging.getLogger(__name__)

TOTAL_ESPERADO = 60
REPO_ROOT = Path(__file__).resolve().parent.parent
PROPOSTAS = REPO_ROOT / "okf/regras-propostas/regras"

#: As vinte causas do art. 30 que cada família tem de cobrir, uma vez cada.
CAUSAS = {
    "acidente-em-servico",
    "causa-comum",
    "doenca-alienacao-mental",
    "doenca-anomalia-da-fala-magisterio",
    "doenca-cardiopatia-grave",
    "doenca-cegueira-bilateral",
    "doenca-contaminacao-por-radiacao",
    "doenca-doenca-de-paget",
    "doenca-doenca-de-parkinson",
    "doenca-esclerose-multipla",
    "doenca-espondiloartrose-anquilosante",
    "doenca-hanseniase",
    "doenca-hepatopatia-grave",
    "doenca-nefropatia-grave",
    "doenca-neoplasia-maligna",
    "doenca-paralisia-irreversivel",
    "doenca-sida-aids",
    "doenca-surdez-permanente-magisterio",
    "doenca-tuberculose-ativa",
    "molestia-profissional",
}

#: familia -> (prefixo do id, vinculo_rpc, selecao_por, paridade, janela de ingresso)
#: A janela usa a semântica consolidada em `okf/spec/regra.md` (2026-08-01):
#: os dois campos `DATA_ADM_*` são inclusivos e gravam o primeiro e o último
#: dia cobertos.
FAMILIAS = {
    "lce1100-incapacidade-ate-2003-sem-rpc": {
        "prefixo": "incapacidade-lce1100-ate-2003-sem-rpc-",
        "vinculo": "nao_aderiu",
        "selecao": set(),
        "paridade": "S",
        "janela": (dt.date(1950, 1, 1), dt.date(2003, 12, 31)),
    },
    "lce1100-incapacidade-2004-a-2018-sem-rpc": {
        "prefixo": "incapacidade-lce1100-2004-ate-2018-sem-rpc-",
        "vinculo": "nao_aderiu",
        "selecao": set(),
        "paridade": "N",
        "janela": (dt.date(2004, 1, 1), dt.date(2018, 11, 5)),
    },
    "lce1100-incapacidade-apos-2018-ou-rpc": {
        "prefixo": "incapacidade-lce1100-apos-2018-ou-rpc-",
        "vinculo": "sujeito",
        "selecao": {"ingresso_apos_implantacao_rpc", "opcao_expressa_rpc"},
        "paridade": "N",
        "janela": (dt.date(2018, 11, 6), dt.date(2099, 12, 31)),
    },
}


class DecomposicaoInvalidaError(Exception):
    """Levantada quando a decomposição em três famílias não fecha."""


def _data(valor: str) -> dt.date:
    """A data de uma célula `dd/mm/aaaa hh:mm` do Sisprev, sem coerção de fuso."""
    dia, mes, ano = (int(x) for x in str(valor).split(" ")[0].split("/"))
    return dt.date(ano, mes, dia)


def _unidades() -> dict[str, dict]:
    """O frontmatter de cada unidade de incapacidade da LCE 1.100/2021, por id."""
    fora = {}
    for caminho in sorted(PROPOSTAS.glob("incapacidade-lce1100-*.md")):
        fora[caminho.stem] = dict(parse_document(caminho).frontmatter)
    return fora


def _conferir_predicados(uid: str, predicados: dict, esperado: dict) -> list[str]:
    """As violações do vínculo com o RPC e do modo de alcance da família."""
    erros = []
    if predicados.get("vinculo_rpc") != esperado["vinculo"]:
        erros.append(
            f"{uid}: `vinculo_rpc` é {predicados.get('vinculo_rpc')!r}, "
            f"a família exige {esperado['vinculo']!r}"
        )
    selecao = set(predicados.get("selecao_por") or [])
    if selecao != esperado["selecao"]:
        exigido = sorted(esperado["selecao"]) or "ausente (o requisito é cumulativo)"
        erros.append(f"{uid}: `selecao_por` é {sorted(selecao) or 'ausente'}, a família exige {exigido}")
    return erros


def _conferir_projecao_e_datas(uid: str, fm: dict, esperado: dict) -> list[str]:
    """As violações de paridade e da janela de ingresso gravada."""
    erros = []
    projecao = fm.get("projecao") or {}
    if str(projecao.get("paridade")) != esperado["paridade"]:
        erros.append(
            f"{uid}: `paridade` é {projecao.get('paridade')!r}, a família exige {esperado['paridade']!r}"
        )
    datas = ((fm.get("aplicabilidade_temporal") or {}).get("datas_legadas")) or {}
    inicio, fim = esperado["janela"]
    if _data(datas.get("data_adm_apos", "01/01/1900")) != inicio:
        erros.append(
            f"{uid}: `data_adm_apos` é {datas.get('data_adm_apos')!r}, a família começa em {inicio:%d/%m/%Y}"
        )
    if _data(datas.get("data_adm_ate", "31/12/2099")) != fim:
        erros.append(
            f"{uid}: `data_adm_ate` é {datas.get('data_adm_ate')!r}, a família termina em {fim:%d/%m/%Y}"
        )
    return erros


def _conferir_janelas() -> list[str]:
    """As violações da partição da linha do tempo entre as três famílias."""
    erros = []
    ordenadas = sorted(f["janela"] for f in FAMILIAS.values())
    for (_, fim), (inicio, _) in itertools.pairwise(ordenadas):
        if inicio != fim + dt.timedelta(days=1):
            erros.append(
                f"janelas de ingresso não particionam: uma termina em {fim:%d/%m/%Y} "
                f"e a seguinte começa em {inicio:%d/%m/%Y}"
            )
    sujeitas = [f for f, d in FAMILIAS.items() if d["vinculo"] == "sujeito"]
    if len(sujeitas) != 1:
        erros.append(f"esperada uma única família sujeita ao RPC, há {len(sujeitas)}: {sujeitas}")
    return erros


#: Os oito cenários que a decomposição tem de resolver, nos dois eixos
#: (data de ingresso e opção pelo regime complementar). Cada um nomeia a
#: família esperada e a via pela qual ela é alcançada.
CENARIOS: tuple[tuple[str, dt.date, bool, str], ...] = (
    ("ingresso em 2000, sem opção", dt.date(2000, 6, 1), False, "lce1100-incapacidade-ate-2003-sem-rpc"),
    ("ingresso em 2000, com opção", dt.date(2000, 6, 1), True, "lce1100-incapacidade-apos-2018-ou-rpc"),
    ("ingresso em 2010, sem opção", dt.date(2010, 6, 1), False, "lce1100-incapacidade-2004-a-2018-sem-rpc"),
    ("ingresso em 2010, com opção", dt.date(2010, 6, 1), True, "lce1100-incapacidade-apos-2018-ou-rpc"),
    (
        "ingresso em 2020, sem opção — alcança pela data",
        dt.date(2020, 6, 1),
        False,
        "lce1100-incapacidade-apos-2018-ou-rpc",
    ),
    # A opção não é hipótese possível aqui (CF, art. 40, § 16): quem ingressou
    # depois da implantação é sujeito automaticamente, e o marcador não muda a
    # família. O cenário fica para fixar essa indiferença.
    (
        "ingresso em 2020, marcado como optante — a sujeição já é automática",
        dt.date(2020, 6, 1),
        True,
        "lce1100-incapacidade-apos-2018-ou-rpc",
    ),
    (
        "véspera da implantação, sem opção",
        dt.date(2018, 11, 5),
        False,
        "lce1100-incapacidade-2004-a-2018-sem-rpc",
    ),
    ("dia da implantação, sem opção", dt.date(2018, 11, 6), False, "lce1100-incapacidade-apos-2018-ou-rpc"),
)


def familia_de(ingresso: dt.date, *, fez_opcao: bool) -> str | None:
    """A família alcançada por um caso, reconstruída do que as unidades gravam.

    A expressão é a da lei, e não uma tabela paralela:

        família 3  <=  ingresso >= implantação do RPC  OU  opção expressa
        família 1  <=  ingresso na janela até 2003     E   sem opção
        família 2  <=  ingresso na janela de 2004 a 2018    E   sem opção

    As duas vias são reais, mas **repartidas no tempo**. A opção do § 16 da
    Constituição só cabe a quem ingressou até a implantação do regime
    complementar (05/11/2018): antes dessa data ela é o que separa esta família
    das duas primeiras; a partir dela a sujeição é automática, e não há opção a
    fazer. A ausência de opção, por sua vez, nunca dispensa a janela — é
    condição cumulativa, e por isso as duas primeiras famílias não declaram
    `selecao_por`.
    """
    sujeitas = [f for f, d in FAMILIAS.items() if d["vinculo"] == "sujeito"]
    sujeita = sujeitas[0]
    inicio_rpc, _ = FAMILIAS[sujeita]["janela"]

    if fez_opcao or ingresso >= inicio_rpc:
        return sujeita
    for familia, dados in FAMILIAS.items():
        if dados["vinculo"] != "nao_aderiu":
            continue
        inicio, fim = dados["janela"]
        if inicio <= ingresso <= fim:
            return familia
    return None


def _conferir_selecao_sintetica() -> list[str]:
    """As violações da expressão lógica de seleção, nos oito cenários."""
    erros = [
        f"cenário «{rotulo}»: esperava {esperada}, obteve {familia_de(ingresso, fez_opcao=opcao)}"
        for rotulo, ingresso, opcao, esperada in CENARIOS
        if familia_de(ingresso, fez_opcao=opcao) != esperada
    ]

    # A ausência de opção não permite ignorar a janela das duas primeiras.
    if familia_de(dt.date(2010, 6, 1), fez_opcao=False) == "lce1100-incapacidade-ate-2003-sem-rpc":
        erros.append("quem ingressou em 2010 sem opção não pode alcançar a família até 2003")
    if familia_de(dt.date(2000, 6, 1), fez_opcao=False) == "lce1100-incapacidade-2004-a-2018-sem-rpc":
        erros.append("quem ingressou em 2000 sem opção não pode alcançar a família 2004-2018")

    sujeita = next(f for f, d in FAMILIAS.items() if d["vinculo"] == "sujeito")
    inicio_rpc, _ = FAMILIAS[sujeita]["janela"]

    # Antes da implantação, a opção é o que discrimina: sem ela o caso fica nas
    # duas primeiras famílias; com ela, vai para a terceira.
    erros += [
        f"antes da implantação a opção tem de discriminar: em {dia:%d/%m/%Y} sem opção "
        f"o caso não pode cair em {sujeita}, e com opção tem de cair"
        for dia in (dt.date(1990, 3, 15), dt.date(2000, 6, 1), dt.date(2010, 6, 1), dt.date(2018, 11, 5))
        if familia_de(dia, fez_opcao=False) == sujeita or familia_de(dia, fez_opcao=True) != sujeita
    ]

    # A partir da implantação a sujeição é automática (CF, art. 40, § 16, só
    # admite a opção de quem ingressou até ela): o marcador não muda a família.
    erros += [
        f"a partir de {inicio_rpc:%d/%m/%Y} a sujeição é automática: {dia:%d/%m/%Y} "
        f"deveria cair em {sujeita} com e sem marcador de opção"
        for dia in (inicio_rpc, dt.date(2020, 6, 1), dt.date(2030, 12, 31))
        if familia_de(dia, fez_opcao=False) != sujeita or familia_de(dia, fez_opcao=True) != sujeita
    ]

    # Nenhum caso possível fica sem família — varredura nos dois eixos.
    erros += [
        f"caso sem família: ingresso em {ano}, opção={opcao}"
        for ano in range(1990, 2031)
        for opcao in (False, True)
        if familia_de(dt.date(ano, 7, 1), fez_opcao=opcao) is None
    ]
    return erros


def conferir() -> list[str]:
    """As violações da decomposição em três famílias; lista vazia se tudo confere."""
    erros: list[str] = []
    unidades = _unidades()
    if len(unidades) != TOTAL_ESPERADO:
        erros.append(
            f"esperadas {TOTAL_ESPERADO} unidades de incapacidade da LCE 1.100/2021, há {len(unidades)}"
        )

    por_familia: dict[str, set[str]] = {f: set() for f in FAMILIAS}
    for uid, fm in unidades.items():
        predicados = fm.get("predicados") or {}
        regime = predicados.get("regime")
        if regime not in FAMILIAS:
            erros.append(f"{uid}: `predicados.regime` {regime!r} não é uma das três famílias")
            continue
        esperado = FAMILIAS[regime]
        if not uid.startswith(esperado["prefixo"]):
            erros.append(f"{uid}: id não começa com {esperado['prefixo']!r}, exigido pela família")
            continue
        causa = uid[len(esperado["prefixo"]) :]
        if causa not in CAUSAS:
            erros.append(f"{uid}: causa {causa!r} não está entre as vinte do art. 30")
        elif causa in por_familia[regime]:
            erros.append(f"{uid}: causa {causa!r} aparece duas vezes na mesma família")
        else:
            por_familia[regime].add(causa)
        erros += _conferir_predicados(uid, predicados, esperado)
        erros += _conferir_projecao_e_datas(uid, fm, esperado)

    for familia, causas in por_familia.items():
        if causas != CAUSAS:
            erros.append(
                f"{familia}: cobertura das causas não fecha — "
                f"faltando {sorted(CAUSAS - causas)}, sobrando {sorted(causas - CAUSAS)}"
            )
    return erros + _conferir_janelas() + _conferir_selecao_sintetica()


def main() -> None:
    """CLI: estoura listando toda inconsistência da decomposição em três famílias."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    erros = conferir()
    if erros:
        for e in erros:
            logger.error("- %s", e)
        msg = f"{len(erros)} inconsistência(s) na decomposição em três famílias"
        raise DecomposicaoInvalidaError(msg)
    logger.info(
        "Decomposição da incapacidade confere: 3 famílias de 20 causas, 60 unidades; "
        "vínculo com o RPC declarado em predicado; `selecao_por` só na família "
        "sujeita ao regime complementar, onde a disjunção é real; janelas "
        "particionando sem buraco nem sobreposição; e os oito cenários "
        "sintéticos de seleção resolvendo na família esperada."
    )


if __name__ == "__main__":
    main()
