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

**WeasyPrint, e não um navegador headless.** Três recursos de CSS Paged Media
sustentam este documento: ``string-set`` (o cabeçalho de cada folha diz de que
regra ela é), ``target-counter`` (o número de página no sumário é resolvido
pelo paginador; um sumário com números escritos pelo gerador mentiria na
primeira quebra que mudasse) e ``bookmark-level`` (marcadores navegáveis no
PDF). Num anexo de centenas de páginas, é a diferença entre um documento que
se cita por folha e um que só se lê rolando.

Medido no relatório do Ciclo 1, contra este mesmo HTML:

===================  ======  ======================================
motor                tempo   o que entrega
===================  ======  ======================================
WeasyPrint           16,2s   tudo
Chromium puro         4,4s   **nada** das caixas de margem: sem
                             número de folha, sem cabeçalho, sem
                             marcadores
Paged.js + Chromium  10,5s   tudo, sem tocar no CSS
===================  ======  ======================================

Ou seja: navegador **puro** não serve, e a alternativa viável é o polyfill.
Ele não foi adotado por três motivos que não são de desempenho — precisa de
servidor HTTP (o HTML referencia ``/sisprev/...``, e a guarda de recurso que
não resolve teria de ser reconstruída), repagina o documento em 119 folhas
contra 123, o que obriga a reconferir tudo no olho, e traz puppeteer junto.
Por 5s por documento. Fica registrado para quando o custo voltar a incomodar:
a decisão já tem número.

O PDF é artefato derivado e binário: não entra no git, exatamente como
``dados-do-site.json``. O que identifica um relatório é o commit impresso na
sua capa — reimprimir o mesmo commit dá o mesmo documento.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import logging
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
    parser.add_argument(
        "--somente-ciclos",
        action="store_true",
        help=(
            "pagina só os relatórios de fechamento de ciclo. O de validação tem 1383 folhas e "
            "responde por quatro quintos do tempo; em revisão, o que se confere são os de ciclo"
        ),
    )
    args = parser.parse_args(argv)

    # O relatório de validação primeiro, e os de ciclo depois. `--html`/`--out`
    # continuam valendo para quem pede um documento só; os de ciclo são
    # descobertos no build, porque são muitos e mudam com o catálogo.
    trabalhos = [] if args.somente_ciclos else [(args.html, args.out)]
    if not args.somente_validacao:
        trabalhos += relatorios_de_ciclo(args.dist)

    # Em processos, e não em série: os documentos são independentes, o custo é
    # inteiramente de CPU e o runner tem mais de um núcleo. Processos e não
    # threads porque a paginação do WeasyPrint é CPU-bound em Python — com
    # threads, o GIL devolveria o tempo de volta.
    #
    # O relatório de validação sozinho é maior que os outros cinco somados, de
    # modo que o ganho aqui é limitado por ele; é o `--somente-ciclos` que
    # muda a ordem de grandeza, e os dois se compõem.
    try:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futuros = {
                executor.submit(gerar_pdf, html, saida, base=args.base, dist=args.dist): saida
                for html, saida in trabalhos
            }
            for futuro in concurrent.futures.as_completed(futuros):
                escrito = futuro.result()
                logger.info("Escrito %s (%.1f MB).", escrito, escrito.stat().st_size / 1_000_000)
    except (HtmlDoRelatorioAusenteError, FolhaDeEstiloAusenteError):
        logger.exception("não foi possível gerar o relatório")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
