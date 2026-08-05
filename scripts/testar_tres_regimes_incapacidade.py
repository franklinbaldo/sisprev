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
complementar coerente com a família, a disjunção declarada onde ela existe, e
janelas de ingresso que particionam a linha do tempo sem buraco nem
sobreposição.
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
        "selecao": {"ingresso_na_janela", "ausencia_de_opcao_rpc"},
        "paridade": "S",
        "janela": (dt.date(1950, 1, 1), dt.date(2003, 12, 31)),
    },
    "lce1100-incapacidade-2004-a-2018-sem-rpc": {
        "prefixo": "incapacidade-lce1100-2004-ate-2018-sem-rpc-",
        "vinculo": "nao_aderiu",
        "selecao": {"ingresso_na_janela", "ausencia_de_opcao_rpc"},
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
        erros.append(
            f"{uid}: `selecao_por` é {sorted(selecao)}, a família exige {sorted(esperado['selecao'])}"
        )
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
    return erros + _conferir_janelas()


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
        "vínculo com o RPC declarado em predicado; disjunção na família sujeita ao "
        "regime complementar; janelas de ingresso particionando sem buraco nem "
        "sobreposição."
    )


if __name__ == "__main__":
    main()
