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
import csv as csv_module
import datetime
import hashlib
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
CSV_DE_HOMOLOGACAO = REPO_ROOT / "data/regras-propostas.csv"
#: O diretório onde vive a carga recortada por ciclo.
DIR_DAS_CARGAS = REPO_ROOT / "data"
CSV_CONGELADO = REPO_ROOT / "data/raw/regras-sisprev.csv"
SNAPSHOT_DO_SITE = REPO_ROOT / "site/src/data/dados-do-site.json"
INDICE_DE_PROPOSTAS = REPO_ROOT / "okf/regras-propostas/regras/index.md"
#: Tudo abaixo desta marca no índice de propostas é derivado; acima é autorado.
MARCA_DE_TABELAS = "<!-- tabelas:"

SCHEMA_VERSION = 1


def csv_do_ciclo(ciclo: str) -> Path:
    """O arquivo de carga de um ciclo — o anexo operacional do relatório dele.

    A carga global reúne toda proposta pronta do repositório, de qualquer
    ciclo, e serve para conferir o catálogo como um todo. Ela **não** pode ser
    o anexo de uma manifestação de ciclo: o relatório do Ciclo 1 conclui sobre
    60 regras e determinava a inserção de um arquivo com 64 linhas, quatro
    delas de outro ciclo de validação. O resumo criptográfico garantia a
    integridade do arquivo errado para aquele escopo, e uma importação integral
    levaria à homologação regras alheias ao ciclo.
    """
    return DIR_DAS_CARGAS / f"regras-propostas-{ciclo}.csv"


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
        escritor = csv_module.DictWriter(fh, fieldnames=colunas, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(linhas)
    return len(linhas)


#: Colunas de proveniência da planilha de homologação. Não vão para o Sisprev:
#: existem para que quem confere a planilha ao lado do export do sistema saiba,
#: sem abrir o repositório, de que regra cadastrada a linha descende e o que
#: falta confirmar nela antes da ativação em produção.
PROVENIENCIA: tuple[str, ...] = (
    "REGRA PROPOSTA",
    "SUBSTITUI",
    "RESSALVA HOMOLOGACAO",
)


def _id_da_ref(ref: str) -> str:
    """O id do documento a partir de uma ref de caminho, quando o campo a usa."""
    return ref.rsplit("/", 1)[-1].removesuffix(".md")


def _regras_propostas() -> dict[str, dict[str, object]]:
    """O frontmatter de toda `RegraProposta`, indexado por id."""
    propostas: dict[str, dict[str, object]] = {}
    for caminho in sorted((REPO_ROOT / "okf/regras-propostas/regras").glob("*.md")):
        if caminho.name == "index.md":
            continue
        propostas[caminho.stem] = _frontmatter(caminho)
    return propostas


def _componentes_conexos(propostas: dict[str, dict[str, object]]) -> list[set[str]]:
    """Os componentes conexos do grafo origem↔destino entre `RegraProposta`.

    Duas propostas pertencem ao mesmo componente quando compartilham, direta
    ou transitivamente, ao menos uma origem legada (`okf/spec/regraproposta.md`,
    "Atomicidade é derivada, não declarada"). Não há campo de grupo declarado à
    parte: a atomicidade é propriedade da transformação, calculada aqui.
    """
    pai: dict[str, str] = {pid: pid for pid in propostas}

    def achar(x: str) -> str:
        while pai[x] != x:
            pai[x] = pai[pai[x]]
            x = pai[x]
        return x

    def unir(a: str, b: str) -> None:
        ra, rb = achar(a), achar(b)
        if ra != rb:
            pai[ra] = rb

    por_origem: dict[str, list[str]] = {}
    for pid, fm in propostas.items():
        for origem in _lista(fm.get("origens_legacy")):
            por_origem.setdefault(str(origem), []).append(pid)
    for mesma_origem in por_origem.values():
        for outro in mesma_origem[1:]:
            unir(mesma_origem[0], outro)

    componentes: dict[str, set[str]] = {}
    for pid in propostas:
        componentes.setdefault(achar(pid), set()).add(pid)
    return list(componentes.values())


#: `estado_implantacao` que autoriza a entrada na carga de homologação —
#: `confirmada` (padrão) e `confirmada_com_ressalva` (o rótulo do Sisprev já
#: identifica a hipótese, mas a execução completa da fórmula depende de
#: confirmação prática em homologação; `okf/spec/regraproposta.md`).
#: `pendente_mapeamento_sisprev` fica de fora: não se sabe, sequer, que
#: mecanismo do sistema a fórmula ocupa.
_ESTADOS_IMPLANTACAO_NA_CARGA = frozenset({"confirmada", "confirmada_com_ressalva"})


def _carga_de_implantacao(
    propostas: dict[str, dict[str, object]],
) -> tuple[list[tuple[str, list[str]]], list[str]]:
    """Os destinos prontos para a carga de homologação, e o diagnóstico dos que não estão.

    Um componente só entra quando **todos** os seus membros têm
    `estado_auditoria: concluida` e `estado_implantacao` em
    `_ESTADOS_IMPLANTACAO_NA_CARGA` (ausente presume `confirmada`) — a troca é
    atômica, e um componente cujas origens cobrem, juntas, mais de uma
    hipótese não admite substituição parcial sem duplicar ou descobrir
    cobertura. Nunca inventa valor de coluna fechada: um componente que não
    está pronto simplesmente não entra, e o motivo vai para o diagnóstico.

    Entrar na carga de homologação não é ativação em produção: é o insumo
    para a conferência de campo contra o Sisprev, que o ato institucional do
    IPERON sucede — nunca antecede (`okf/spec/ciclo.md`, "O ato institucional
    não é condição de encerramento"). `confirmada_com_ressalva` entra na carga
    exatamente para que essa conferência aconteça; não afirma que a fórmula já
    está confirmada.

    A consistência entre `estado_implantacao` e `ressalva_homologacao` é
    verificada aqui, genericamente para toda `RegraProposta` — não apenas
    para o Bloco C: `confirmada_com_ressalva` sem `ressalva_homologacao`
    bloqueia a carga (a ressalva é o que o rótulo promete registrar), e
    `ressalva_homologacao` preenchida fora de `confirmada_com_ressalva`
    também bloqueia (ressalva residual de uma edição anterior, sem o estado
    que a justifica, é tão enganosa quanto a ausência dela).
    """
    prontos: list[tuple[str, list[str]]] = []
    diagnosticos: list[str] = []
    for componente in _componentes_conexos(propostas):
        bloqueios = []
        for pid in sorted(componente):
            fm = propostas[pid]
            estado_auditoria = str(fm.get("estado_auditoria", ""))
            estado_implantacao = str(fm.get("estado_implantacao") or "confirmada")
            ressalva = str(fm.get("ressalva_homologacao") or "").strip()
            if estado_auditoria != "concluida":
                bloqueios.append(f"{pid}: estado_auditoria={estado_auditoria!r}")
            if estado_implantacao not in _ESTADOS_IMPLANTACAO_NA_CARGA:
                bloqueios.append(f"{pid}: estado_implantacao={estado_implantacao!r}")
            if estado_implantacao == "confirmada_com_ressalva" and not ressalva:
                bloqueios.append(
                    f"{pid}: estado_implantacao=confirmada_com_ressalva sem ressalva_homologacao"
                )
            if estado_implantacao != "confirmada_com_ressalva" and ressalva:
                bloqueios.append(
                    f"{pid}: ressalva_homologacao preenchida com "
                    f"estado_implantacao={estado_implantacao!r} (só confirmada_com_ressalva a admite)"
                )
        if bloqueios:
            diagnosticos.append(
                f"componente {sorted(componente)} não entra na carga: " + "; ".join(bloqueios)
            )
            continue
        origens = sorted(
            {str(origem) for pid in componente for origem in _lista(propostas[pid].get("origens_legacy"))}
        )
        prontos.extend((pid, origens) for pid in sorted(componente))
    return prontos, diagnosticos


def escrever_csv_de_homologacao(destino: Path, ciclo: str | None = None) -> tuple[int, list[str]]:
    """Escreve a carga de homologação e devolve (linhas, diagnósticos).

    É o anexo que o relatório de fechamento promete: a projeção de cada regra
    proposta pronta para homologação nas colunas do próprio Sisprev, do jeito
    que entraria. Existe para que a conferência de campo aconteça onde ela é
    possível — numa planilha, ao lado do export do sistema —, e não folheando
    um PDF de centenas de páginas. É carga de **homologação**, não ativação em
    produção: o ato institucional do IPERON continua sendo evento posterior e
    único (`okf/spec/ciclo.md`).

    As colunas do Sisprev de uma `RegraProposta` moram em dois lugares:
    `projecao` traz a maioria e `aplicabilidade_temporal.datas_legadas` traz as
    de data. As duas entram, porque uma planilha de homologação sem as janelas
    não permite conferir qual regra alcança um requerimento.

    Não sai `ID`: a coluna é a chave do Sisprev, e uma regra que ainda não
    existe no sistema não tem uma. Inventar número seria oferecer a quem
    importa a planilha uma identidade que o sistema não reconhece.

    Só entram os componentes prontos (`_carga_de_implantacao`) — um componente
    ainda não pronto está autorado e conferido, mas não entra na carga. Pô-lo
    na planilha apresentaria a quem homologa um conjunto maior do que o
    pronto para o sistema aceitar. `RESSALVA HOMOLOGACAO` carrega, para as
    linhas com `estado_implantacao: confirmada_com_ressalva`, o que a
    homologação prática ainda precisa confirmar antes da ativação em
    produção — em branco quando não há ressalva.

    Com `ciclo`, sai só o que aquele ciclo propõe. O recorte é do **escopo da
    manifestação**, não de conveniência de arquivo: o relatório de um ciclo
    conclui sobre as regras daquele ciclo e determina a inserção do arquivo que
    identifica, e um arquivo maior que a conclusão leva à homologação regra
    sobre a qual ninguém se manifestou ali. O recorte é por proposta e não por
    componente porque componente não atravessa ciclo — as origens legadas de
    ciclos diferentes não se tocam —, mas se algum dia atravessar, o filtro
    abaixo continuará dizendo a verdade sobre o que entra no arquivo.
    """
    propostas = _regras_propostas()
    prontos, diagnosticos = _carga_de_implantacao(propostas)
    if ciclo is not None:
        prontos = [(pid, origens) for pid, origens in prontos if str(propostas[pid].get("ciclo")) == ciclo]

    colunas = [coluna for coluna in COLUNAS if coluna != "ID"]
    linhas = []
    for proposta, origens in prontos:
        fm = propostas[proposta]
        projetado: dict[str, object] = {}
        if isinstance(fm.get("projecao"), dict):
            projetado |= fm["projecao"]  # type: ignore[operator]
        temporal = fm.get("aplicabilidade_temporal")
        datas = temporal.get("datas_legadas") if isinstance(temporal, dict) else None
        if isinstance(datas, dict):
            projetado |= datas
        linhas.append(
            {coluna: projetado.get(chave, "") for coluna, chave in COLUNAS.items() if coluna != "ID"}
            | {
                "REGRA PROPOSTA": proposta,
                "SUBSTITUI": " ".join(origens),
                "RESSALVA HOMOLOGACAO": str(fm.get("ressalva_homologacao") or ""),
            }
        )

    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="utf-8", newline="") as fh:
        escritor = csv_module.DictWriter(fh, fieldnames=[*colunas, *PROVENIENCIA], lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(linhas)
    return len(linhas), diagnosticos


def escrever_indice(destino: Path, titulo: str, itens: list[str]) -> None:
    """Escreve uma listagem OKF — sem frontmatter, como a spec exige."""
    corpo = f"# {titulo}\n\n" + ("\n".join(itens) + "\n" if itens else "")
    canonico = mdformat.text(corpo, extensions={"frontmatter", "gfm"})
    destino.write_text(canonico, encoding="utf-8")


def regenerar_indice_de_propostas() -> None:
    """Reescreve as tabelas por ciclo do índice de `RegraProposta`.

    O índice era mantido à mão e nenhuma guarda o cobria. Depois de uma
    renomeação em massa ele passou meses listando os quarenta ids anteriores,
    com quarenta links para arquivos que não existiam mais — um índice que
    aponta para o vazio é pior que índice nenhum, porque quem o consulta
    conclui que a unidade sumiu.

    Só as tabelas são derivadas. O preâmbulo explica o schema e é prosa
    autorada: derivá-lo levaria texto editorial para dentro do código, que é
    de onde ele saiu. A fronteira é um comentário HTML, como no `relatorio.md`
    e pelo mesmo motivo — não renderiza e não depende de título.
    """
    corpo = INDICE_DE_PROPOSTAS.read_text(encoding="utf-8")
    corte = corpo.find(MARCA_DE_TABELAS)
    if corte == -1:
        msg = f"{INDICE_DE_PROPOSTAS}: falta a marca {MARCA_DE_TABELAS!r} que separa o autorado do derivado"
        raise SystemExit(msg)
    fim_da_marca = corpo.index("\n", corte) + 1

    propostas = _regras_propostas()
    por_ciclo: dict[str, list[tuple[str, dict[str, object]]]] = {}
    for pid, fm in sorted(propostas.items()):
        por_ciclo.setdefault(str(fm.get("ciclo") or "sem-ciclo"), []).append((pid, fm))

    partes = []
    for ciclo, unidades in sorted(por_ciclo.items()):
        partes.append(f"### {ciclo}\n")
        partes.append(
            "| unidade | origens legadas | tipo_calculo (projeção legada) "
            "| estado_auditoria | estado_implantacao |"
        )
        partes.append("| --- | --- | --- | --- | --- |")
        for pid, fm in unidades:
            origens = ", ".join(f"`{o}`" for o in (str(x) for x in _lista(fm.get("origens_legacy")))) or "—"
            tipo = (fm.get("projecao") or {}).get("tipo_calculo") or "—"
            estado = fm.get("estado_auditoria") or "—"
            implantacao = fm.get("estado_implantacao") or "confirmada"
            partes.append(f"| [`{pid}`]({pid}.md) | {origens} | `{tipo}` | `{estado}` | `{implantacao}` |")
        partes.append("")

    texto = corpo[:fim_da_marca] + "\n" + "\n".join(partes)
    canonico = mdformat.text(texto, extensions={"frontmatter", "gfm"})
    INDICE_DE_PROPOSTAS.write_text(canonico, encoding="utf-8")


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

    regenerar_indice_de_propostas()


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


def ciclos_com_carga() -> list[str]:
    """Os ciclos que têm ao menos uma regra proposta pronta para a carga.

    Derivado, não listado: um ciclo novo passa a ter arquivo de carga assim que
    a primeira proposta dele fica pronta, e deixa de ter se nenhuma estiver —
    sem que ninguém precise lembrar de acrescentá-lo a lista alguma.
    """
    propostas = _regras_propostas()
    prontos, _ = _carga_de_implantacao(propostas)
    return sorted({str(propostas[pid].get("ciclo")) for pid, _ in prontos})


def _manifesto_da_carga(caminho: Path) -> dict[str, object]:
    """A identificação documental do arquivo de carga: o que o PDF imprime dele.

    O relatório é assinado e circula fora do repositório, onde um link é
    promessa e não prova: quem o recebe precisa poder verificar que o CSV em
    mãos é o mesmo sobre o qual a manifestação se deu. O resumo criptográfico
    é o que amarra os dois, e é também o que vincula à peça assinada as três
    fundamentações — que são parágrafos inteiros, não cabem na folha do anexo
    e vivem só no CSV.

    Lido do arquivo que será efetivamente publicado, não de uma cópia: o
    `emit-data.sh` copia este mesmo arquivo para `site/public/downloads/`.
    """
    if not caminho.exists():
        msg = f"{caminho}: a carga de homologação precisa existir antes do snapshot"
        raise SystemExit(msg)
    bruto = caminho.read_bytes()
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        linhas = list(csv_module.reader(arquivo))
    return {
        "arquivo": caminho.name,
        "sha256": hashlib.sha256(bruto).hexdigest(),
        "bytes": len(bruto),
        "linhas": max(len(linhas) - 1, 0),
        "colunas": len(linhas[0]) if linhas else 0,
    }


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
        # Uma carga por ciclo, porque é por ciclo que a manifestação se dá: o
        # relatório de um ciclo identifica e determina a juntada do arquivo que
        # contém exatamente as regras sobre as quais ele concluiu.
        "cargas": {ciclo: _manifesto_da_carga(csv_do_ciclo(ciclo)) for ciclo in ciclos_com_carga()},
    }
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    """Deriva tudo. Sem argumento, escreve nos caminhos padrão do repositório."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=CSV_DERIVADO)
    parser.add_argument("--csv-homologacao", type=Path, default=CSV_DE_HOMOLOGACAO)
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
        n, diagnosticos = escrever_csv_de_homologacao(args.csv_homologacao)
        logger.info("%s: %d linhas", args.csv_homologacao, n)
        for diagnostico in diagnosticos:
            logger.info("diagnóstico de implantação: %s", diagnostico)
        # E o recorte por ciclo, que é o anexo operacional de cada relatório.
        for ciclo in ciclos_com_carga():
            destino = csv_do_ciclo(ciclo)
            n, _ = escrever_csv_de_homologacao(destino, ciclo=ciclo)
            logger.info("%s: %d linhas", destino, n)
    escrever_snapshot_do_site(docs, args.snapshot)
    logger.info("%s", args.snapshot)


if __name__ == "__main__":
    main()
