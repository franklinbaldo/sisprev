"""Confere o PDF do relatório de ciclo contra os dados de que ele deriva.

O build verde não basta: o documento sai bem formado e ainda assim pode
afirmar coisa que o catálogo não sustenta, ou perder no impresso o que o HTML
tinha. Este script abre o PDF gerado e confere o que quem assina veria.

O que ele cobre são regressões concretas, todas já ocorridas neste documento:

- a leitura humana colada ao valor canônico (`SimTRUE`, `NãoN`), que impedia
  saber qual cadeia o sistema grava;
- a palavra "componente" impressa antes de um identificador que já a contém;
- a contagem de conferências em aberto anunciada como contagem de ressalvas de
  homologação, que fazia um componente com regra ressalvada dizer "0";
- o resumo criptográfico da carga divergindo do arquivo publicado ao lado;
- vocabulário de repositório e história editorial na voz jurídica;
- `/PageLabels` ausente, que faz o leitor contar folhas enquanto o documento
  conta páginas.
"""

from __future__ import annotations

import hashlib
import logging
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derivar import _regras_propostas

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF = REPO_ROOT / "site/dist/relatorio-de-ciclo-ciclo-01.pdf"
CSV_PUBLICADO = REPO_ROOT / "site/dist/downloads/regras-propostas.csv"
CICLO = "ciclo-01"

#: Concatenações de leitura e valor canônico. Cada uma é um par que o anexo
#: imprimia sem rótulo, e que ninguém consegue desfazer olhando a folha.
CONCATENACOES = ("SimTRUE", "NãoFALSE", "SimS", "NãoN", "componente componente-")

#: O que não pode aparecer na voz jurídica do documento: vocabulário de
#: repositório, história editorial e metalinguagem.
PROIBIDOS = (
    "data venia",
    "issue #",
    "tipo_calculo",
    "estado_implantacao",
    "pendente_mapeamento",
    "versão anterior",
    "nesta revisão",
    "a planilha é o que se importa",
    "o que se lê aqui",
    "Providência do Instituto",
)

#: Títulos conversacionais substituídos por títulos que nomeiam o conteúdo.
TITULOS_APOSENTADOS = (
    "O que a Procuradoria afirma juridicamente",
    "O que depende do Instituto",
    "Como este documento está organizado",
    "Por que o número de regras aumenta",
    "Limite do que a regra decide",
    "Limite do que a auditoria altera",
)

#: O que o documento precisa afirmar para ser autossuficiente.
EXIGIDOS = (
    "Encaminhamento institucional",
    "Situação do ciclo",
    "Origem e referência administrativa",
    "Componente de substituição",
    "Conclusões jurídicas do Ciclo 1",
    "Responsabilidades e providências",
    "Identificação e integridade da carga de homologação",
    "não se identifica óbice jurídico",
    "Rastreabilidade interna",
)


def _texto_do_pdf() -> str:
    from pypdf import PdfReader  # noqa: PLC0415

    return "\n".join(pagina.extract_text() for pagina in PdfReader(str(PDF)).pages)


def _compacto(texto: str) -> str:
    """O texto sem espaço nem hífen, para comparar frase com o que foi impresso.

    O paginador justifica e hifeniza: "não se identifica" pode sair como "não
    se iden-tifica" quebrado em duas linhas, e um identificador de sessenta
    caracteres sai partido em três. Procurar a frase crua no texto extraído
    daria falso negativo em toda linha que o paginador tenha quebrado. A
    comparação é feita sobre a forma compacta dos **dois** lados.
    """
    return re.sub(r"[\s\u00ad\u2010\u2011-]+", "", texto)


def _contem(texto: str, agulha: str) -> bool:
    """Se o impresso traz a frase, ignorando quebra de linha e hifenização."""
    return _compacto(agulha) in _compacto(texto)


def _propostas_do_ciclo() -> dict[str, dict[str, object]]:
    return {pid: fm for pid, fm in _regras_propostas().items() if str(fm.get("ciclo")) == CICLO}


def _conferir_cadeias(texto: str) -> list[str]:
    """Concatenações, vocabulário proibido e títulos aposentados."""
    # Estas são procuradas no texto com os espaços preservados, e não na forma
    # compacta: o defeito é a leitura **colada** ao valor canônico, e apagar o
    # espaço acusaria também as três colunas da tabela, que são distintas na
    # folha e só se encostam na extração.
    espacado = re.sub(r"[ \t]+", " ", texto)
    violacoes = [f"o impresso ainda traz {c!r}" for c in CONCATENACOES if c in espacado]
    violacoes += [
        f"vocabulário de repositório no corpo jurídico: {p!r}" for p in PROIBIDOS if _contem(texto, p)
    ]
    violacoes += [
        f"título conversacional remanescente: {t!r}" for t in TITULOS_APOSENTADOS if _contem(texto, t)
    ]
    violacoes += [f"o impresso não afirma {e!r}" for e in EXIGIDOS if not _contem(texto, e)]
    return violacoes


def _conferir_ressalvas(texto: str) -> list[str]:
    """As populações do documento batem com o catálogo, e não se confundem."""
    propostas = _propostas_do_ciclo()
    do_bloco = {p: fm for p, fm in propostas.items() if p.startswith("incapacidade-lce1100-")}
    ressalvadas = {
        p for p, fm in do_bloco.items() if str(fm.get("estado_implantacao")) == "confirmada_com_ressalva"
    }
    violacoes: list[str] = []

    # Cada regra ressalvada precisa estar nominalmente no documento: contar não
    # basta, porque quem homologa precisa saber *quais* não podem ir a produção.
    ausentes = sorted(p for p in ressalvadas if not _contem(texto, p))
    if ausentes:
        violacoes.append(
            f"{len(ausentes)} regra(s) ressalvada(s) não identificadas no impresso: {ausentes[:3]}"
        )

    # E as não ressalvadas também são reconhecidas — a contrapartida que o
    # documento deve declarar em vez de deixar por dedução.
    sem_ressalva = len(do_bloco) - len(ressalvadas)
    if not _contem(texto, f"{sem_ressalva} sem ressalva específica"):
        violacoes.append(f"o impresso não reconhece as {sem_ressalva} regras sem ressalva específica")

    # Nenhum selo pode anunciar ressalvas contando conferências em aberto.
    if re.search(r"\b\d+ ressalvas?\b", re.sub(r"\s+", " ", texto)):
        violacoes.append("selo genérico 'N ressalvas' — as duas populações precisam ser nomeadas")
    return violacoes


def _conferir_integridade(texto: str) -> list[str]:
    """O resumo impresso é o do arquivo publicado ao lado do relatório."""
    if not CSV_PUBLICADO.is_file():
        return [f"{CSV_PUBLICADO} não existe — o build do site não publicou a carga"]
    real = hashlib.sha256(CSV_PUBLICADO.read_bytes()).hexdigest()
    if real not in _compacto(texto):
        return [f"o resumo criptográfico impresso não é o do arquivo publicado ({real})"]
    return []


def _conferir_rotulos_logicos() -> list[str]:
    """`/PageLabels` existe e reproduz a numeração impressa."""
    import pikepdf  # noqa: PLC0415

    with pikepdf.open(PDF) as documento:
        if "/PageLabels" not in documento.Root:
            return ["o PDF não tem /PageLabels: o leitor conta folhas, o documento conta páginas"]
        nums = documento.Root.PageLabels.Nums
    if len(nums) < 4:  # noqa: PLR2004 — capa + ao menos um trecho numerado
        return [f"/PageLabels tem {len(nums) // 2} trecho(s); esperava capa e ao menos um numerado"]
    return []


def conferir() -> list[str]:
    """As violações do documento impresso; lista vazia se tudo confere."""
    if not PDF.is_file():
        return [f"{PDF} não existe — rode o build do site e `scripts/gerar_relatorio_pdf.py`"]
    texto = _texto_do_pdf()
    return [
        *_conferir_cadeias(texto),
        *_conferir_ressalvas(texto),
        *_conferir_integridade(texto),
        *_conferir_rotulos_logicos(),
    ]


def main() -> int:
    """CLI: sai com 1 listando toda divergência entre o impresso e os dados."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    violacoes = conferir()
    if violacoes:
        logger.error("O relatório impresso não confere:\n%s", "\n".join(violacoes))
        return 1
    logger.info(
        "O relatório impresso confere: sem concatenação de valor, sem vocabulário de "
        "repositório na voz jurídica, regras ressalvadas identificadas nominalmente, "
        "resumo criptográfico igual ao do arquivo publicado e rótulos lógicos de página."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
