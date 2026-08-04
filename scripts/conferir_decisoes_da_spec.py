"""Confere o catálogo proposto contra as decisões verificáveis declaradas nas specs.

Fecha um circuito que estava aberto: uma decisão da coordenação valia nos
documentos e não valia no dado. As quarenta unidades do Ciclo 1 gravaram a
fronteira de ingresso pela convenção **oposta** à que a spec fixa, e nenhum dos
gates viu — bundle conforme, derivado em sincronia, importação íntegra, achados
preservados, e o valor mesmo assim contrariando a decisão escrita.

**O código não sabe nada sobre janelas temporais.** Ele não infere fronteira de
nome de grupo, não conhece "após 2003", não interpreta operador inclusivo ou
exclusivo, e não tem opinião sobre qual convenção é certa. Ele sabe três
coisas: onde procurar uma decisão verificável, que documentos estão no alcance
dela, e se o valor gravado é o valor declarado. Mudou a decisão? Muda-se a
spec, e este script passa a exigir a nova — sem tocar em Python.

É por isso que a declaração é procurada, e não lida de um caminho fixo: a spec
vai mudar de casa quando as decisões de tipo virarem bundle OKF próprio, e uma
mudança de endereço não pode ser uma mudança de código.

Alcance atual: `campo` de uma `RegraProposta`, alcançada pelos grupos de
substituição que a declaração nomeia. Ampliar isto exige um caso concreto — o
mesmo critério que o CI aplica a guarda nova.
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import yaml
from okf_parser.parser import parse_document

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
#: Onde procurar declarações e documentos. Diretórios, nunca arquivos: a spec
#: muda de nome e de pasta, e o gate não pode depender disso.
ONDE_PROCURAR_DECLARACOES = (REPO_ROOT / "docs", REPO_ROOT / "okf")
CONJUNTOS = REPO_ROOT / "okf/conjuntos"
PROPOSTAS = REPO_ROOT / "okf/regras-propostas/regras"


class DeclaracaoInvalidaError(Exception):
    """Levantada quando uma declaração existe mas não diz o que conferir."""


def _frontmatter(caminho: Path) -> dict[str, object]:
    """Frontmatter do documento, com todo escalar preservado como texto.

    Mesmo leitor de `derivar.py`, e pela mesma razão: `01/01/2004 00:00` tem de
    chegar aqui como o byte que foi escrito. Comparar datas coagidas faria o
    gate aprovar uma grafia que o Sisprev nunca recebeu.
    """
    return dict(parse_document(caminho).frontmatter)


def _frontmatter_de_documento_livre(caminho: Path) -> dict[str, object]:
    """Frontmatter de um `.md` que não é documento OKF — a spec, hoje, é um.

    `parse_document` exige `type`, e uma spec em `docs/` não tem. Ler o bloco
    à mão evita obrigar a spec a fingir-se de conceito antes da migração.
    """
    texto = caminho.read_text(encoding="utf-8")
    if not texto.startswith("---\n"):
        return {}
    fim = texto.find("\n---\n", 4)
    if fim == -1:
        return {}
    carregado = yaml.safe_load(texto[4:fim])
    return carregado if isinstance(carregado, dict) else {}


def declaracoes(raizes: tuple[Path, ...]) -> list[tuple[Path, dict[str, object]]]:
    """Toda decisão verificável declarada, com o documento que a declara.

    A busca é por conteúdo — o documento que traz `decisoes_verificaveis` é a
    autoridade daquela decisão, onde quer que ele esteja.
    """
    achadas: list[tuple[Path, dict[str, object]]] = []
    for raiz in raizes:
        for caminho in sorted(raiz.rglob("*.md")):
            fm = _frontmatter_de_documento_livre(caminho)
            for decisao in fm.get("decisoes_verificaveis") or []:
                if not isinstance(decisao, dict):
                    msg = f"{caminho}: cada decisão verificável tem de ser um mapa"
                    raise DeclaracaoInvalidaError(msg)
                achadas.append((caminho, decisao))
    return achadas


def _id_da_ref(ref: str) -> str:
    return ref.rsplit("/", 1)[-1].removesuffix(".md")


def destinos_dos_grupos(grupos: set[str]) -> dict[str, str]:
    """Os ids de `RegraProposta` alcançados, e por qual grupo.

    O alcance vem do **grupo de substituição**, que é a unidade de decisão da
    auditoria, e não de casamento de nome de arquivo: uma unidade entra no
    alcance porque um grupo a declarou destino, nunca porque o id dela se
    parece com o do grupo.
    """
    alcancados: dict[str, str] = {}
    for caminho in sorted(CONJUNTOS.glob("*.md")):
        if caminho.name == "index.md":
            continue
        for substituicao in _frontmatter(caminho).get("substituicoes") or []:
            if not isinstance(substituicao, dict) or substituicao.get("grupo") not in grupos:
                continue
            for destino in substituicao.get("destinos_propostos") or []:
                alcancados[_id_da_ref(str(destino))] = str(substituicao["grupo"])
    return alcancados


def _valor_gravado(fm: dict[str, object], campo: str) -> str:
    """O valor do campo na unidade, procurado onde a unidade de fato o grava.

    As colunas do Sisprev moram em dois lugares na `RegraProposta`: `projecao`
    traz a maioria e `aplicabilidade_temporal.datas_legadas` traz as de data.
    O gate procura nos dois em vez de eleger um — a divisão é da autoria, e
    conferir só metade seria pior que não conferir.
    """
    projecao = fm.get("projecao")
    if isinstance(projecao, dict) and campo in projecao:
        return str(projecao[campo])
    temporal = fm.get("aplicabilidade_temporal")
    datas = temporal.get("datas_legadas") if isinstance(temporal, dict) else None
    if isinstance(datas, dict) and campo in datas:
        return str(datas[campo])
    return ""


def divergencias(caminho: Path, decisao: dict[str, object]) -> list[str]:
    """As unidades cujo valor não é o declarado, ditas uma por linha."""
    campo = decisao.get("campo")
    valor = decisao.get("valor")
    grupos = decisao.get("aplica_a_grupos")
    if not campo or valor is None or not grupos:
        msg = f"{caminho}: decisão verificável precisa de `campo`, `valor` e `aplica_a_grupos`"
        raise DeclaracaoInvalidaError(msg)

    esperado = str(valor)
    operador = decisao.get("operador", "não declarado")
    alcancados = destinos_dos_grupos({str(g) for g in grupos})
    if not alcancados:
        msg = f"{caminho}: nenhum grupo de substituição declarado em `aplica_a_grupos` existe"
        raise DeclaracaoInvalidaError(msg)

    linhas: list[str] = []
    for proposta_id, grupo in sorted(alcancados.items()):
        arquivo = PROPOSTAS / f"{proposta_id}.md"
        if not arquivo.is_file():
            linhas.append(f"  {proposta_id}: destino do grupo {grupo} não existe no bundle")
            continue
        gravado = _valor_gravado(_frontmatter(arquivo), str(campo))
        if gravado != esperado:
            linhas.append(f"  {proposta_id}: grava {gravado or '(vazio)'}, a spec declara {esperado}")

    if linhas:
        cabecalho = (
            f"{caminho.relative_to(REPO_ROOT)} decide `{campo} = {esperado}` "
            f"(operador {operador}) para os grupos {', '.join(sorted(str(g) for g in grupos))}:"
        )
        return [cabecalho, *linhas]
    return []


def main(argv: list[str] | None = None) -> int:
    """CLI: sai com 1 listando toda divergência entre a spec e o catálogo proposto."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)

    encontradas = declaracoes(ONDE_PROCURAR_DECLARACOES)
    if not encontradas:
        # Silêncio aqui seria lido como "está tudo certo". Nenhuma declaração
        # significa que o circuito não está fechado por ninguém.
        logger.info("Nenhuma decisão verificável declarada em spec alguma.")
        return 0

    problemas = [linha for caminho, decisao in encontradas for linha in divergencias(caminho, decisao)]
    if problemas:
        logger.error("O catálogo proposto contraria decisão declarada em spec:\n%s", "\n".join(problemas))
        return 1

    quantas = len(encontradas)
    decisoes = "decisão verificável confere" if quantas == 1 else "decisões verificáveis conferem"
    logger.info("%d %s com o catálogo proposto.", quantas, decisoes)
    return 0


if __name__ == "__main__":
    sys.exit(main())
