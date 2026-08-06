"""Imprime os relatórios da PGE em PDF, a partir do HTML já buildado.

São dois documentos, e o script pagina os dois: o relatório de validação, que
analisa o catálogo como está gravado, e um relatório de fechamento por
composição, que analisa o que a auditoria propõe pôr no lugar. O segundo é
descoberto no build — a página oferece o download, e é este script que o
produz, de modo que a promessa e o arquivo saem do mesmo id de rota.


Este script **não gera conteúdo**: quem monta o relatório é a página
``site/src/pages/relatorio.astro``, com as mesmas coleções, os mesmos
formatadores e o mesmo pipeline de Markdown do resto do site. Aqui só se
pagina o HTML que o build já produziu — a divisão é deliberada, e é o que
faz o relatório nunca poder divergir da ficha da regra: são a mesma leitura
do mesmo bundle, em duas superfícies.

Por isso a ordem é sempre a mesma, e a primeira metade dela é onde moram as
garantias:

    cd site && npm run build      # roda emit_site_data.py, que se recusa a
                                  # emitir sobre bundle com violação
    uv run python scripts/gerar_relatorio_pdf.py

**WeasyPrint, e não um navegador headless.** A escolha não é de gosto: três
recursos de CSS Paged Media sustentam este documento e nenhum motor de
navegador os implementa — ``string-set`` (o cabeçalho de cada folha diz de
que regra ela é), ``target-counter`` (o número de página no sumário é
resolvido pelo paginador; um sumário com números escritos pelo gerador
mentiria na primeira quebra que mudasse) e ``bookmark-level`` (marcadores
navegáveis no PDF). Num anexo de centenas de páginas, é a diferença entre um
documento que se cita por folha e um que só se lê rolando.

O PDF é artefato derivado e binário: não entra no git, exatamente como
``dados-do-site.json``. O que identifica um relatório é o commit impresso na
sua capa — reimprimir o mesmo commit dá o mesmo documento.
"""

from __future__ import annotations

import argparse
import itertools
import logging
import re
import sys
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import unquote, urlparse

if TYPE_CHECKING:
    from collections.abc import Callable

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST = REPO_ROOT / "site" / "dist"
HTML_PADRAO = DIST / "relatorio" / "index.html"
PDF_PADRAO = DIST / "relatorio-de-validacao.pdf"

# O mesmo `base` declarado em `site/astro.config.mjs`. O site é publicado num
# subcaminho do GitHub Pages, então o Astro emite `<link
# href="/sisprev/_astro/...">` — um caminho absoluto de URL, que fora de um
# servidor resolve contra a raiz do sistema de arquivos e não acha nada. É
# por isso que o PDF precisa deste prefixo, e por isso ele é declarado aqui
# em vez de adivinhado: se o `base` do site mudar e este valor não, o
# relatório sai sem folha de estilo — falha silenciosa que só se vê olhando.
BASE_DO_SITE = "/sisprev"


class HtmlDoRelatorioAusenteError(Exception):
    """Levantada quando a página do relatório ainda não foi buildada.

    Falha alto em vez de gerar um PDF vazio ou desatualizado: um anexo de
    processo emitido a partir de um build antigo é pior que nenhum anexo,
    porque nada nele denuncia a defasagem — a capa exibiria um commit que não
    é o do catálogo que se quis submeter.
    """


class FolhaDeEstiloAusenteError(Exception):
    """Levantada quando um recurso referenciado pela página não resolve no ``dist``.

    Estourar aqui é deliberado. Um PDF sem folha de estilo *é gerado* — sai
    legível, com a tipografia padrão do motor —, mas sem cabeçalho corrente,
    sem numeração no sumário e sem nenhuma das quebras de página que separam
    um capítulo do outro. É exatamente o tipo de defeito que passa numa
    conferência rápida e só aparece depois de o anexo estar no processo.
    """


def _leitor_de_recursos(dist: Path, base: str) -> Callable[..., dict]:
    """Devolve um ``url_fetcher`` que resolve os caminhos absolutos do site dentro de ``dist``.

    O prefixo de publicação (``/sisprev``) não existe no disco: no ``dist``,
    ``/sisprev/_astro/x.css`` é ``dist/_astro/x.css``. Um recurso que ainda
    assim não resolva **levanta**, em vez de virar um 404 silencioso que o
    WeasyPrint absorveria seguindo em frente sem estilo nenhum.
    """
    from weasyprint.urls import default_url_fetcher  # noqa: PLC0415

    prefixo = base.rstrip("/")

    def fetcher(url: str, *args: object, **kwargs: object) -> dict:
        if url.startswith("file://"):
            caminho = unquote(urlparse(url).path)
            if not Path(caminho).is_file() and caminho.startswith(f"{prefixo}/"):
                alvo = dist / caminho[len(prefixo) + 1 :]
                if not alvo.is_file():
                    msg = f"{url} não resolve em {alvo} — o build do site está incompleto?"
                    raise FolhaDeEstiloAusenteError(msg)
                url = alvo.as_uri()
        return default_url_fetcher(url, *args, **kwargs)

    return fetcher


def gerar_pdf(html: Path, saida: Path, *, base: str = BASE_DO_SITE, dist: Path | None = None) -> Path:
    """Pagina ``html`` em ``saida`` e devolve o caminho do PDF escrito.

    ``dist`` é a raiz do build, onde os caminhos absolutos do site resolvem.
    O default deriva de ``html.parent.parent``, que vale para uma página na
    raiz (``dist/relatorio/index.html``) e **não** para uma rota aninhada
    (``dist/relatorio-ciclo/<id>/index.html``, cujo avô é
    ``dist/relatorio-ciclo``). Quem chama de uma rota aninhada passa ``dist``
    explicitamente — errar isso não dá erro, dá PDF sem folha de estilo.
    """
    if not html.is_file():
        msg = (
            f"{html} não existe — rode `cd site && npm run build` antes. "
            "O relatório é buildado pelo Astro; este script só o pagina."
        )
        raise HtmlDoRelatorioAusenteError(msg)

    # Importado aqui, e não no topo: weasyprint puxa as bibliotecas de
    # tipografia do sistema no import, e nenhum outro comando deste
    # repositório depende delas. Uma falha de ambiente deve estourar para
    # quem pediu o PDF, não para quem rodou `validar_regras.py`.
    from weasyprint import HTML  # noqa: PLC0415

    # O subsetting de fontes do fontTools loga uma centena de linhas em
    # INFO ("glyf subsetted", ...) por fonte embutida. Isso é ruído sobre a
    # única linha que importa aqui, a do arquivo escrito.
    logging.getLogger("fontTools").setLevel(logging.WARNING)

    saida.parent.mkdir(parents=True, exist_ok=True)
    HTML(
        filename=str(html),
        base_url=str(html),
        url_fetcher=_leitor_de_recursos(dist if dist is not None else html.parent.parent, base),
    ).write_pdf(str(saida))
    return saida


#: O que um rótulo de página pode ser: algarismos romanos minúsculos ou
#: arábicos. Qualquer outra coisa no pé da folha não é numeração.
ROMANO = re.compile(r"^[ivxlcdm]+$")


class RotulosIncoerentesError(RuntimeError):
    """A numeração impressa não forma sequência contínua e crescente."""


def _rotulo_impresso(pagina: object) -> str | None:
    """O número impresso no pé de uma folha, ou ``None`` se ela não leva um.

    Lido do próprio PDF, e não deduzido da estrutura do documento: quem tem de
    conferir é o rótulo que o leitor vê. A caixa `@bottom-center` é o elemento
    mais baixo da folha, então é a última linha do texto extraído.
    """
    linhas = [linha.strip() for linha in pagina.extract_text().splitlines() if linha.strip()]  # type: ignore[attr-defined]
    if not linhas:
        return None
    ultima = linhas[-1]
    if ultima.isdigit() or ROMANO.match(ultima):
        return ultima
    return None


def _romano_para_int(rotulo: str) -> int:
    valores = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    total = 0
    anterior = 0
    for letra in reversed(rotulo):
        atual = valores[letra]
        total += atual if atual >= anterior else -atual
        anterior = max(anterior, atual)
    return total


def _trechos_de_rotulo(rotulos: list[str | None]) -> list[tuple[int, str, int]]:
    """Agrupa os rótulos impressos em trechos ``(inicio, estilo, primeiro)``.

    Estilo é ``""`` para folha sem numeração, ``"r"`` para romano minúsculo e
    ``"D"`` para arábico — os códigos que o PDF usa em ``/PageLabels``.
    """
    trechos: list[tuple[int, str, int]] = []
    for indice, rotulo in enumerate(rotulos):
        if rotulo is None:
            estilo, valor = "", 0
        elif rotulo.isdigit():
            estilo, valor = "D", int(rotulo)
        else:
            estilo, valor = "r", _romano_para_int(rotulo)
        # Só abre trecho novo quando o estilo muda ou a contagem salta: um
        # trecho por folha inflaria o arquivo e não diria nada a mais.
        if trechos:
            inicio, estilo_anterior, primeiro = trechos[-1]
            if estilo == estilo_anterior and (estilo == "" or valor == primeiro + (indice - inicio)):
                continue
        trechos.append((indice, estilo, valor))
    return trechos


def _conferir_rotulos(rotulos: list[str | None]) -> None:
    """Estoura se a numeração impressa não for contínua e crescente.

    O modo de falha que isto pega é o que já aconteceu neste documento: a
    representação alternando entre romano e arábico sobre um contador só, de
    modo que o leitor via 50, `li`, `lii`, 53 e quem citasse "página 51" não a
    encontrava. Uma sequência que salta ou retrocede é defeito de folha de
    estilo, e um rótulo lógico fiel a ela apenas propagaria o defeito para a
    navegação do arquivo.
    """
    impressos = [r for r in rotulos if r is not None]
    numeros = [int(r) if r.isdigit() else _romano_para_int(r) for r in impressos]
    for anterior, atual in itertools.pairwise(numeros):
        if atual != anterior + 1:
            msg = (
                f"numeração impressa salta de {anterior} para {atual}: o documento não pode "
                "receber rótulos lógicos fiéis a uma sequência descontínua"
            )
            raise RotulosIncoerentesError(msg)

    # E a representação só pode virar uma vez, de romano para arábico. Um
    # contador só alternando de representação já saiu impresso como 50, `li`,
    # `lii`, 53 — quem citasse "página 51" num despacho não a encontrava. A
    # continuidade acima não pega isso, porque o contador não salta: o que muda
    # é como ele é escrito.
    estilos = ["D" if r.isdigit() else "r" for r in impressos]
    viradas = [i for i, (a, b) in enumerate(itertools.pairwise(estilos)) if a != b]
    if len(viradas) > 1 or (viradas and estilos[0] != "r"):
        trechos = [estilos[0], *(estilos[i + 1] for i in viradas)]
        msg = (
            f"a numeração impressa alterna de representação: {' → '.join(trechos)}. "
            "O documento admite um único trecho romano, no início, seguido de arábicos"
        )
        raise RotulosIncoerentesError(msg)


def aplicar_rotulos_de_pagina(pdf: Path) -> list[str | None]:
    """Escreve em ``/PageLabels`` a numeração que o documento imprime.

    Sem isso, o campo de página do leitor conta folhas físicas enquanto o
    documento conta as suas: quem recebe o anexo e digita o número citado num
    despacho chega à folha errada. O pós-processamento não redesenha nada —
    abre, acrescenta a árvore de rótulos e regrava, preservando marcadores,
    links, fontes e metadados.
    """
    import pikepdf  # noqa: PLC0415
    from pypdf import PdfReader  # noqa: PLC0415

    rotulos = [_rotulo_impresso(pagina) for pagina in PdfReader(str(pdf)).pages]
    _conferir_rotulos(rotulos)

    nums: list[object] = []
    for inicio, estilo, primeiro in _trechos_de_rotulo(rotulos):
        entrada: dict[str, object] = {}
        if estilo:
            entrada["/S"] = pikepdf.Name(f"/{estilo}")
            entrada["/St"] = primeiro
        else:
            # Folha sem numeração institucional — a capa. Prefixo em vez de
            # rótulo vazio: sem nada, o leitor exibe o índice físico e volta a
            # sugerir uma numeração que o documento não tem.
            entrada["/P"] = "capa"
        nums += [inicio, pikepdf.Dictionary(entrada)]

    with pikepdf.open(pdf, allow_overwriting_input=True) as documento:
        documento.Root.PageLabels = pikepdf.Dictionary(Nums=pikepdf.Array(nums))
        documento.save(pdf)
    return rotulos


def relatorios_de_ciclo(dist: Path) -> list[tuple[Path, Path]]:
    """Os relatórios de fechamento buildados, como pares (html, pdf).

    O nome do PDF é o que a própria página oferece no link "Baixar em PDF" —
    `relatorio-de-ciclo-<id>.pdf`. Os dois lados saem do mesmo id da rota, de
    modo que uma composição nova aparece nos dois sem que ninguém liste nada:
    o modo de falha que isto evita é a página prometer um download que o
    build não produziu, e o 404 só aparecer para quem foi baixar.
    """
    raiz = dist / "relatorio-ciclo"
    if not raiz.is_dir():
        # Nenhuma composição com grupo ativo: a rota não existe, e não há
        # documento a paginar. Diferente de um HTML faltando dentro dela, que
        # `gerar_pdf` estoura.
        return []
    return [
        (pasta / "index.html", dist / f"relatorio-de-ciclo-{pasta.name}.pdf")
        for pasta in sorted(raiz.iterdir())
        if pasta.is_dir() and (pasta / "index.html").is_file()
    ]


def main(argv: list[str] | None = None) -> int:
    """CLI: pagina os relatórios buildados, ou sai com 1 explicando o que falta."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", type=Path, default=HTML_PADRAO, help="HTML buildado da página do relatório")
    parser.add_argument("--out", type=Path, default=PDF_PADRAO, help="caminho do PDF a escrever")
    parser.add_argument("--base", default=BASE_DO_SITE, help="o mesmo `base` de site/astro.config.mjs")
    parser.add_argument("--dist", type=Path, default=DIST, help="raiz do build do site")
    parser.add_argument(
        "--somente-validacao",
        action="store_true",
        help="pagina só o relatório de validação, sem os relatórios de fechamento de ciclo",
    )
    args = parser.parse_args(argv)

    # O relatório de validação primeiro, e os de ciclo depois. `--html`/`--out`
    # continuam valendo para quem pede um documento só; os de ciclo são
    # descobertos no build, porque são muitos e mudam com o catálogo.
    trabalhos = [(args.html, args.out)]
    if not args.somente_validacao:
        trabalhos += relatorios_de_ciclo(args.dist)

    try:
        for html, saida in trabalhos:
            escrito = gerar_pdf(html, saida, base=args.base, dist=args.dist)
            rotulos = aplicar_rotulos_de_pagina(escrito)
            numeradas = sum(1 for rotulo in rotulos if rotulo is not None)
            logger.info(
                "Escrito %s (%.1f MB, %d folhas, %d numeradas).",
                escrito,
                escrito.stat().st_size / 1_000_000,
                len(rotulos),
                numeradas,
            )
    except (HtmlDoRelatorioAusenteError, FolhaDeEstiloAusenteError, RotulosIncoerentesError):
        logger.exception("não foi possível gerar o relatório")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
