"""Arquivo local das fontes oficiais citadas pelo bundle de dispositivos.

Não confundir com ``scripts/fontes.py``, que valida o *campo* ``fontes:``
(toda entrada tem de ser URL http(s)). Este módulo cuida do outro lado: ter
localmente **o conteúdo** que aquelas URLs servem.

Toda transcrição de dispositivo é conferida contra a publicação oficial da
norma. Depender da rede para isso é frágil de um jeito que importa: durante a
sessão que criou este módulo o Planalto esteve fora do ar por horas (HTTP 503
e depois timeout), e um agente sem a fonte à mão é um agente tentado a
escrever texto legal de memória — exatamente o modo de falha que a RFC 0008
baniu ao remover o leitor de citações por regex.

Com as fontes no repositório a conferência também vira **reproduzível**: quem
auditar uma transcrição compara com o byte que estava lá quando ela foi
escrita, não com o que o site serve hoje.

Três decisões que valem registro:

- **Arquivo bruto, nunca documento OKF.** ``fontes/`` guarda o HTML/PDF como
  veio, com o hash. Não é um bundle, não tem frontmatter, e nada aqui vira
  ``type: Dispositivo`` automaticamente — a decomposição continua sob demanda
  e autoral (``docs/spec/dispositivo.md``). Baixar a norma inteira é o oposto
  de fragmentá-la preventivamente: é ter o todo para poder recortar à mão.
- **Indexado por URL, não por norma.** A EC 20/1998 é fonte de ``cf88`` e de
  ``ec-20-1998``; a LC 949/2017 é fonte de ``lce-432-2008`` e ``lce-949-2017``.
  Guardar por norma duplicaria bytes e, pior, deixaria duas cópias divergirem.
- **Falha é registrada, não silenciada.** Uma URL que não baixou entra em
  ``faltando:`` com o motivo. Um manifesto que lista só o que deu certo é
  lido como cobertura completa, e é assim que se conclui "a norma não diz
  nada sobre isso" a partir de um arquivo que simplesmente não foi buscado.

Uso::

    uv run python scripts/arquivo_de_fontes.py              # baixa o que falta
    uv run python scripts/arquivo_de_fontes.py --verificar  # confere hashes, sem rede
"""

from __future__ import annotations

import argparse
import hashlib
import logging
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from typing import TYPE_CHECKING
from urllib.parse import unquote, urlparse

import yaml
from okf_common import REPO_ROOT

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)

FONTES_DIR = REPO_ROOT / "fontes"
ARQUIVOS_DIR = FONTES_DIR / "arquivos"
MANIFESTO = FONTES_DIR / "manifesto.yaml"
DISPOSITIVOS_DIR = REPO_ROOT / "okf" / "dispositivos"

HTTP_OK = "200"
TIMEOUT_SEGUNDOS = "45"
PARTES_MINIMAS_DE_FRONTMATTER = 3

#: Um PDF cujo texto extraído fica abaixo disto é imagem escaneada, não texto.
#: A ECE 146/2021 é o caso real: 4,8 MB de digitalização, 10 caracteres de
#: camada de texto. Registrar isso é o que impede alguém de concluir, de um
#: ``grep`` vazio, que a norma não trata do assunto.
MINIMO_TEXTO_UTIL = 2000


def _frontmatter(caminho: Path) -> dict[str, object]:
    """Devolve o frontmatter YAML de um documento OKF, ou ``{}`` se não houver.

    Deliberadamente tolerante: este módulo só quer as URLs em ``fontes:``, e
    um documento malformado por outro motivo não pode impedir o arquivamento
    das fontes de todos os outros.
    """
    partes = caminho.read_text(encoding="utf-8").split("---")
    if len(partes) < PARTES_MINIMAS_DE_FRONTMATTER:
        return {}
    try:
        dados = yaml.safe_load(partes[1])
    except yaml.YAMLError:
        return {}
    return dados if isinstance(dados, dict) else {}


def coletar_urls(raiz: Path = DISPOSITIVOS_DIR) -> dict[str, set[str]]:
    """Mapeia cada URL citada em ``fontes:`` para as normas que a citam.

    Varre tanto os ``norma.md`` quanto os documentos de dispositivo. ``http``
    é normalizado para ``https`` só para deduplicar — as duas grafias ocorrem
    no bundle e apontam para o mesmo documento.
    """
    urls: dict[str, set[str]] = {}
    for caminho in sorted(raiz.rglob("*.md")):
        dados = _frontmatter(caminho)
        tipo = dados.get("type")
        if tipo == "Norma":
            norma = dados.get("id")
        elif tipo == "Dispositivo":
            norma = dados.get("norma")
        else:
            continue
        fontes = dados.get("fontes")
        if not isinstance(norma, str) or not isinstance(fontes, list):
            continue
        for bruta in fontes:
            if not isinstance(bruta, str):
                continue
            url = f"https://{bruta.removeprefix('http://')}" if bruta.startswith("http://") else bruta
            urls.setdefault(url, set()).add(norma)
    return urls


def nome_de_arquivo(url: str) -> str:
    """Nome local determinístico para uma URL: ``<host>-<último segmento>``.

    Determinístico porque o manifesto tem de ser estável entre execuções: um
    nome que mudasse a cada captura faria o arquivo inteiro aparecer como
    modificado no diff sem nada ter mudado.
    """
    partes = urlparse(url)
    host = partes.netloc.removeprefix("www.").removeprefix("www2.").split(".")[0]
    base = unquote(partes.path.rstrip("/").split("/")[-1] or "index").replace(" ", "-")
    return f"{host}-{base}"


def _sha256(caminho: Path) -> str:
    """Hash do conteúdo do arquivo, para conferência posterior sem rede."""
    return hashlib.sha256(caminho.read_bytes()).hexdigest()


def _baixar(url: str, destino: Path) -> str | None:
    """Baixa ``url`` para ``destino``; devolve o motivo da falha, ou ``None``.

    Usa ``curl`` em vez de ``urllib`` porque o ambiente roteia HTTPS por um
    proxy com CA própria que o ``curl`` do sistema já resolve.
    """
    curl = shutil.which("curl")
    if curl is None:
        return "curl indisponível"
    comando = [
        curl,
        "-sS",
        "-L",
        "--retry",
        "2",
        "--retry-delay",
        "3",
        "-m",
        TIMEOUT_SEGUNDOS,
        "-o",
        str(destino),
        "-w",
        "%{http_code}",
        url,
    ]
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=False)
    except OSError as erro:
        return f"erro de execução: {erro}"
    codigo = resultado.stdout.strip()
    if codigo != HTTP_OK or not destino.exists() or destino.stat().st_size == 0:
        destino.unlink(missing_ok=True)
        return f"HTTP {codigo or 'sem resposta'}"
    return None


def _extrair_texto(pdf: Path) -> Path | None:
    """Gera o ``.txt`` ao lado de um PDF, se ele tiver camada de texto.

    O ``.txt`` é o que torna o arquivo útil: um PDF não se grepa. Devolve
    ``None`` quando o PDF é digitalização — nesse caso nada é gravado, para
    que a ausência do ``.txt`` seja o próprio registro do problema.
    """
    pdftotext = shutil.which("pdftotext")
    if pdftotext is None:
        return None
    saida = pdf.with_suffix(".txt")
    try:
        subprocess.run([pdftotext, "-layout", str(pdf), str(saida)], capture_output=True, check=False)
    except OSError:
        return None
    if not saida.exists():
        return None
    if saida.stat().st_size < MINIMO_TEXTO_UTIL:
        saida.unlink(missing_ok=True)
        return None
    return saida


def _manifesto_atual() -> dict[str, object]:
    """Lê o manifesto já comitado, ou ``{}`` na primeira execução."""
    if not MANIFESTO.exists():
        return {}
    dados = yaml.safe_load(MANIFESTO.read_text(encoding="utf-8"))
    return dados if isinstance(dados, dict) else {}


def _itens_arquivados(manifesto: dict[str, object]) -> list[dict[str, object]]:
    """Extrai a lista ``arquivos:`` do manifesto, tolerando forma inesperada.

    O manifesto é dado no disco, então "está lá e é uma lista de dicts" é
    hipótese, não garantia — um arquivo truncado ou editado à mão não pode
    derrubar o script que existe justamente para detectar isso.
    """
    itens = manifesto.get("arquivos")
    if not isinstance(itens, list):
        return []
    return [{str(chave): valor for chave, valor in item.items()} for item in itens if isinstance(item, dict)]


def _capturado_em(anterior: dict[str, dict[str, object]], url: str) -> str:
    """Preserva a data de captura original de uma fonte já arquivada."""
    registro = anterior.get(url)
    if isinstance(registro, dict):
        data = registro.get("capturado_em")
        if isinstance(data, str):
            return data
    return datetime.now(tz=UTC).date().isoformat()


def _registrar_pdf(destino: Path, registro: dict[str, object]) -> None:
    """Acrescenta ao registro o ``.txt`` do PDF, ou a nota de que não há.

    Um ``.txt`` que já esteja em disco é submetido ao mesmo mínimo que um
    recém-extraído: ``pdftotext`` sobre uma digitalização não falha, ele grava
    um punhado de bytes vazios. Aceitar esse resto como texto faria o
    manifesto anunciar cobertura que não existe — que é exatamente o que este
    módulo se propõe a não fazer.
    """
    texto = destino.with_suffix(".txt")
    if texto.exists() and texto.stat().st_size < MINIMO_TEXTO_UTIL:
        texto.unlink()
    if not texto.exists():
        texto = _extrair_texto(destino) or texto
    if texto.exists():
        registro["texto"] = texto.relative_to(FONTES_DIR).as_posix()
        return
    registro["texto"] = None
    registro["observacao"] = "PDF sem camada de texto (digitalização) — leitura visual necessária"


def construir(*, baixar: bool = True) -> dict[str, object]:
    """Baixa o que falta e devolve o manifesto como dado.

    Idempotente: um arquivo já presente não é rebaixado, para que o
    ``capturado_em`` de cada fonte continue sendo a data em que aquele byte
    entrou no repositório.
    """
    ARQUIVOS_DIR.mkdir(parents=True, exist_ok=True)
    anterior = {str(item.get("url")): item for item in _itens_arquivados(_manifesto_atual())}

    arquivados: list[dict[str, object]] = []
    faltando: list[dict[str, object]] = []

    for url, normas in sorted(coletar_urls().items()):
        destino = ARQUIVOS_DIR / nome_de_arquivo(url)
        motivo = None
        if not destino.exists():
            motivo = _baixar(url, destino) if baixar else "ausente (execução sem rede)"

        if not destino.exists():
            logger.warning("falhou: %s (%s)", url, motivo)
            faltando.append({"url": url, "normas": sorted(normas), "motivo": motivo})
            continue

        registro: dict[str, object] = {
            "url": url,
            "arquivo": destino.relative_to(FONTES_DIR).as_posix(),
            "sha256": _sha256(destino),
            "bytes": destino.stat().st_size,
            "normas": sorted(normas),
            "capturado_em": _capturado_em(anterior, url),
        }
        if destino.suffix.lower() == ".pdf":
            _registrar_pdf(destino, registro)
        arquivados.append(registro)
        logger.info("ok: %s -> %s", url, registro["arquivo"])

    return {"arquivos": arquivados, "faltando": faltando}


def escrever(manifesto: dict[str, object]) -> None:
    """Grava ``fontes/manifesto.yaml`` de forma estável entre execuções."""
    MANIFESTO.write_text(
        yaml.safe_dump(manifesto, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )


def verificar() -> list[str]:
    """Confere, sem rede, que cada arquivo do manifesto bate com seu hash.

    É o que dá valor de prova ao arquivo: uma transcrição citada como
    conferida contra ``fontes/arquivos/X`` só significa alguma coisa se X não
    puder ter mudado silenciosamente depois.
    """
    manifesto = _manifesto_atual()
    if not manifesto:
        return ["fontes/manifesto.yaml não existe — rode scripts/arquivo_de_fontes.py"]
    problemas: list[str] = []
    for item in _itens_arquivados(manifesto):
        caminho = FONTES_DIR / str(item.get("arquivo"))
        if not caminho.exists():
            problemas.append(f"ausente: {item.get('arquivo')}")
        elif _sha256(caminho) != item.get("sha256"):
            problemas.append(f"hash diverge: {item.get('arquivo')}")
    return problemas


def main(argv: list[str] | None = None) -> int:
    """CLI: baixa o que falta (padrão) ou apenas confere os hashes."""
    parser = argparse.ArgumentParser(description="Arquivo local das fontes oficiais das normas.")
    parser.add_argument("--verificar", action="store_true", help="confere hashes, sem acessar a rede")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    if args.verificar:
        problemas = verificar()
        for problema in problemas:
            logger.error("%s", problema)
        if not problemas:
            logger.info("manifesto confere.")
        return 1 if problemas else 0

    manifesto = construir()
    escrever(manifesto)
    arquivos = manifesto["arquivos"]
    faltando = manifesto["faltando"]
    if isinstance(arquivos, list) and isinstance(faltando, list):
        logger.info("%d fonte(s) arquivada(s), %d faltando.", len(arquivos), len(faltando))
    return 0


if __name__ == "__main__":
    sys.exit(main())
