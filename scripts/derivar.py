"""Deriva os artefatos do bundle: o CSV do Sisprev, dois índices e o snapshot do site.

Este é o único comando que escreve artefato derivado. Ele lê o frontmatter dos
`regra-*.md` e dos `achado-*.md` e mais nada — não há aqui nenhuma regra de
domínio, nenhum julgamento sobre a regra, nenhum gate. Um erro de mérito numa
regra atravessa este script intacto, porque não é ele quem tem competência para
achar erro de mérito.

Três saídas, e cada uma existe por um consumidor concreto:

- `data/regras-sisprev.csv` — as colunas que o Sisprev recebe, mais as
  colunas administrativas da auditoria. É o produto operacional.
- `regras/index.md` e `achados/index.md` — as listagens que a spec OKF pede.
  Regeneradas porque carregam o `nome`, que muda durante a auditoria.
- `site/src/data/dados-do-site.json` — o snapshot que o site consome: o commit
  impresso no rodapé e o estado de auditoria de cada regra e cada achado. Nunca
  comitado, porque carrega o SHA do próprio commit que o geraria.

`data/raw/` é a importação congelada e nunca é escrita — por nada, nunca.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import logging
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

import mdformat
from okf_parser.parser import parse_document

if TYPE_CHECKING:
    from collections.abc import Iterable

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
BUNDLE = REPO_ROOT / "okf/regras-sisprev"
CSV_DERIVADO = REPO_ROOT / "data/regras-sisprev.csv"
CSV_CONGELADO = REPO_ROOT / "data/raw/regras-sisprev.csv"
SNAPSHOT_DO_SITE = REPO_ROOT / "site/src/data/dados-do-site.json"

SCHEMA_VERSION = 1

# O nome exato da coluna no CSV do Sisprev -> a chave no frontmatter. É a única
# tradução do repositório entre os dois espaços de nome, e por isso está escrita
# como dado, não derivada por slugificação: `Requisitos da IN Nº 5/2020` e
# `Relatório p/ Reserva Remunerada por Idade ex-officio` não sobrevivem a
# nenhuma regra mecânica que também acerte as outras 25.
COLUNAS: dict[str, str] = {
    # A chave do próprio Sisprev. Ela não veio na primeira importação e foi
    # recebida depois; sem ela, a única ponte entre uma linha do sistema e um
    # `regra-NNNN.md` era a posição no arquivo — que casa hoje e deixa de
    # casar na primeira linha inserida ou removida lá. `row_index` continua
    # sendo a posição na importação; este é o identificador do sistema.
    "ID": "id_sisprev",
    "NOME": "nome",
    "TIPO DE BENEFICIO": "tipo_de_beneficio",
    "ATUALMENTE NO SISTEMA": "atualmente_no_sistema",
    "CICLO DE VALIDAÇÃO": "ciclo_de_validacao",
    "VALIDADO PGE": "validado_pge",
    "VALIDADO PRESIDENCIA": "validado_presidencia",
    "SIMULAVEL": "simulavel",
    "TIPO": "tipo",
    "APOS_ESPECIAL": "apos_especial",
    "TIPO_REMUN": "tipo_remun",
    "PARIDADE": "paridade",
    "TabelaPontuacao": "tabelapontuacao",
    "Requisitos da IN Nº 5/2020": "requisitos_da_in_no_5_2020",
    "Relatório p/ Reserva Remunerada por Idade ex-officio": (
        "relatorio_p_reserva_remunerada_por_idade_ex_officio"
    ),
    "ADICIONAL_INATIVIDADE": "adicional_inatividade",
    "DATA_ADM_ATE": "data_adm_ate",
    "DATA_ADM_APOS": "data_adm_apos",
    "DATA_DIREITO_ATE": "data_direito_ate",
    "DATA_DIREITO_APOS": "data_direito_apos",
    "FUNDAMENTACAO_PROPORCIONAL": "fundamentacao_proporcional",
    "VISIVEL DTC PROPORCIONAL": "visivel_dtc_proporcional",
    "FUNDAMENTACAO_INTEGRAL": "fundamentacao_integral",
    "VISIVEL DTC INTEGRAL": "visivel_dtc_integral",
    "SEXO": "sexo",
    "INTEGRAL": "integral",
    "TIPO_CALCULO": "tipo_calculo",
    "FUNDAMENTACAO": "fundamentacao",
}

# Campos da auditoria, que não existem no Sisprev e viajam no CSV derivado para
# quem confere a planilha sem abrir o repositório. O default explícito existe
# para que nenhuma célula saia vazia por omissão e seja lida como "não sei".
ADMIN_ESCALARES: dict[str, str] = {
    # O nome como veio na importação. A coluna `NOME` leva o nome que a
    # auditoria propõe, e é ele que iria para o sistema; o original só existia
    # em `data/raw/`, de modo que ninguém cotejava a linha proposta com a de
    # origem sem abrir dois arquivos. Ele não distingue as regras — quase
    # metade delas repete o nome de outra —, e foi por isso que a auditoria o
    # reescreveu: guardá-lo preserva a origem, não propõe que ele volte.
    "nome_original": "",
    "status_regra": "ativa",
    "motivo_inativacao": "",
    "status_auditoria": "importada",
    "auditado_por": "",
    "auditado_em": "",
}
ADMIN_LISTAS = ("atos_validacao", "dispositivos", "precedentes", "disposicao_de_achados")


class ArtefatoCongeladoError(Exception):
    """Levantada ao tentar escrever sobre a importação congelada em `data/raw/`."""


class BundleInconsistenteError(Exception):
    """Levantada quando a identidade dos documentos não fecha com o Dataset."""


def _frontmatter(caminho: Path) -> dict[str, object]:
    """Frontmatter do documento, com todo escalar preservado como texto.

    O leitor do `okf-parser` não coage `2026-07-30` em `date` nem `TRUE` em
    `bool`, então o valor que sai daqui é o byte que o auditor escreveu. É isso
    que faz o CSV derivado dar round-trip com a importação original.
    """
    return dict(parse_document(caminho).frontmatter)


def _docs_de_regra() -> list[Path]:
    """Os `regra-*.md` em ordem de `row_index`, conferidos contra o Dataset.

    A conferência é de identidade, não de mérito: o `id` e o `row_index` de cada
    documento têm de casar com o nome do arquivo, e o conjunto dos `row_index`
    tem de ser exatamente `1..row_count`, sem buraco nem repetido. Contar
    documentos não basta — dois arquivos podem somar o número certo e apontar
    para a mesma linha do CSV.
    """
    dataset = _frontmatter(BUNDLE / "regras-sisprev.md")
    esperado = int(str(dataset["row_count"]))

    por_indice: dict[int, Path] = {}
    for caminho in sorted((BUNDLE / "regras").glob("regra-*.md")):
        fm = _frontmatter(caminho)
        if fm.get("id") != caminho.stem:
            msg = f"{caminho.name}: id {fm.get('id')!r} não casa com o nome do arquivo"
            raise BundleInconsistenteError(msg)
        indice = int(str(fm["row_index"]))
        if indice in por_indice:
            msg = f"{caminho.name} e {por_indice[indice].name} declaram o mesmo row_index {indice}"
            raise BundleInconsistenteError(msg)
        por_indice[indice] = caminho

    if set(por_indice) != set(range(1, esperado + 1)):
        faltando = sorted(set(range(1, esperado + 1)) - set(por_indice))
        sobrando = sorted(set(por_indice) - set(range(1, esperado + 1)))
        msg = f"row_index não cobre 1..{esperado} — faltando {faltando}, sobrando {sobrando}"
        raise BundleInconsistenteError(msg)

    return [por_indice[i] for i in range(1, esperado + 1)]


def _linha(fm: dict[str, object]) -> dict[str, object]:
    """Uma linha do CSV: as colunas do Sisprev mais os campos da auditoria."""
    linha: dict[str, object] = {coluna: fm.get(chave, "") for coluna, chave in COLUNAS.items()}
    linha |= {chave: fm.get(chave, default) for chave, default in ADMIN_ESCALARES.items()}
    linha |= {
        chave: json.dumps(fm.get(chave, []), ensure_ascii=False, default=_iso) for chave in ADMIN_LISTAS
    }
    return linha


def _iso(valor: object) -> str:
    """Serializa data para o CSV, e só data.

    O YAML dentro de uma lista administrativa ainda é lido pelo parser normal,
    então `decidido_em: 2026-07-30` chega aqui como `date`. Deliberadamente não
    é `default=str`: isso transformaria qualquer objeto inesperado numa célula
    plausível, que é como um deslize de schema vira dado silencioso.
    """
    if isinstance(valor, datetime.datetime | datetime.date):
        return valor.isoformat()
    msg = f"não serializável para o CSV derivado: {type(valor).__name__}"
    raise TypeError(msg)


def escrever_csv(docs: Iterable[Path], destino: Path) -> int:
    """Escreve o CSV derivado e devolve o número de linhas."""
    if destino.resolve() == CSV_CONGELADO.resolve():
        msg = f"{destino} é a importação congelada e nunca pode ser reescrita"
        raise ArtefatoCongeladoError(msg)

    linhas = [_linha(_frontmatter(caminho)) for caminho in docs]
    colunas = [*COLUNAS, *ADMIN_ESCALARES, *ADMIN_LISTAS]

    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8", newline="") as fh:
        # A linha em branco no topo é artefato do export original do Google
        # Sheets. Ela é reproduzida de propósito: o CSV derivado tem de ser
        # comparável com `data/raw/` sem que ninguém precise saber disso.
        fh.write("," * (len(colunas) - 1) + "\n")
        escritor = csv.DictWriter(fh, fieldnames=colunas, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(linhas)
    return len(linhas)


def escrever_indice(destino: Path, titulo: str, itens: list[str]) -> None:
    """Escreve uma listagem OKF — sem frontmatter, como a spec exige."""
    corpo = f"# {titulo}\n\n" + ("\n".join(itens) + "\n" if itens else "")
    canonico = mdformat.text(corpo, extensions={"frontmatter", "gfm"})
    destino.write_text(canonico, encoding="utf-8")


def regenerar_indices(docs: list[Path]) -> None:
    """Regenera as duas listagens que carregam `nome`, o campo que a auditoria corrige."""
    itens = []
    for caminho in docs:
        fm = _frontmatter(caminho)
        itens.append(f"* [{fm.get('nome', '')}]({caminho.name}) - {fm.get('tipo_de_beneficio', '')}")
    escrever_indice(BUNDLE / "regras/index.md", "Regras", itens)

    itens = []
    for caminho in sorted((BUNDLE / "achados").glob("achado-*.md")):
        fm = _frontmatter(caminho)
        refs = ", ".join(
            str(ref).rsplit("/", 1)[-1].removesuffix(".md") for ref in _lista(fm.get("regras_afetadas"))
        )
        itens.append(
            f"* [{fm.get('nome', '')}]({caminho.stem}.md) - "
            f"{fm.get('situacao', '')}/{fm.get('severidade', '')} - {refs}"
        )
    escrever_indice(BUNDLE / "achados/index.md", "Achados", itens)


def _lista(valor: object) -> list[object]:
    """Um campo de lista, tolerante a ausência — um doc malformado não derruba a derivação."""
    return valor if isinstance(valor, list) else []


def _git(*argv: str) -> str:
    return subprocess.run(
        ["git", "-C", str(REPO_ROOT), *argv],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


def escrever_snapshot_do_site(docs: list[Path], destino: Path) -> None:
    """Escreve o snapshot que o site consome.

    O que atravessa aqui é o estado de auditoria gravado no frontmatter, sem
    recálculo: o site imprime o que a regra diz de si mesma. O SHA e a data vêm
    do git porque são a única coisa que o frontmatter não pode saber — e são o
    motivo de este arquivo nunca ser comitado.
    """
    regras = {}
    for caminho in docs:
        fm = _frontmatter(caminho)
        regras[caminho.stem] = {
            "status_auditoria": str(fm.get("status_auditoria", "importada")),
            "validado_pge": str(fm.get("validado_pge", "FALSE")).upper() == "TRUE",
            "validado_presidencia": str(fm.get("validado_presidencia", "FALSE")).upper() == "TRUE",
            "ciclo_de_validacao": str(fm.get("ciclo_de_validacao", "")),
        }

    achados = {}
    for caminho in sorted((BUNDLE / "achados").glob("achado-*.md")):
        fm = _frontmatter(caminho)
        achados[caminho.stem] = {
            "situacao": str(fm.get("situacao", "aberto")),
            "severidade": str(fm.get("severidade", "informativo")),
            "regras_afetadas": [
                str(ref).rsplit("/", 1)[-1].removesuffix(".md") for ref in _lista(fm.get("regras_afetadas"))
            ],
        }

    payload = {
        "schema_version": SCHEMA_VERSION,
        "sha": _git("rev-parse", "HEAD"),
        "generated_at": _git("log", "-1", "--format=%cs", "HEAD"),
        "regras": regras,
        "achados": achados,
    }
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    """Deriva tudo. Sem argumento, escreve nos caminhos padrão do repositório."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=CSV_DERIVADO)
    parser.add_argument("--snapshot", type=Path, default=SNAPSHOT_DO_SITE)
    parser.add_argument(
        "--somente-snapshot",
        action="store_true",
        help="só o JSON do site — o que o build do Astro precisa",
    )
    args = parser.parse_args()

    docs = _docs_de_regra()
    if not args.somente_snapshot:
        n = escrever_csv(docs, args.csv)
        regenerar_indices(docs)
        logger.info("%s: %d linhas", args.csv, n)
    escrever_snapshot_do_site(docs, args.snapshot)
    logger.info("%s", args.snapshot)


if __name__ == "__main__":
    main()
