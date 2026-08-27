#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "okf-parser>=0.1.0",
# ]
# ///
"""Exige que todo `type` em uso tenha documento de especificação.

Implementa aqui a regra proposta em
[okf-parser#25](https://github.com/franklinbaldo/okf-parser/issues/25): o
formato só exige que `type` seja texto não vazio, de modo que um tipo pode
existir, ser usado por centenas de documentos e nunca ter contrato escrito. O
esquema dele passa a viver em quem o implementa — aqui, no `content.config.ts`
do site — e muda sem que nada acuse.

**O incidente é desta casa.** Numa única sessão, o contrato de `Conjunto`
ganhou `substituicoes` e o de `Ciclo` ganhou `conjunto`, ambos por mão minha,
e nenhum dos dois tipos tinha documento que dissesse o que são. Foi essa a
diferença entre editar um contrato e editar um campo: nenhuma.

**O caminho da spec é derivado, não apontado.** É a escolha do issue, e é
melhor que o ponteiro explícito que este repositório chegou a gravar: o `type`
continua um nome curto — `Regra`, e não `/spec/regra.md` —, os documentos não
precisam ser reescritos quando a spec muda de lugar, e o vínculo continua
mecânico. A derivação é a do issue: minúsculas, sem acento nem cedilha,
espaço e barra viram hífen, o resto do que não é alfanumérico cai.

**Duas divergências do template padrão**, ambas deliberadas:

- as specs ficam num bundle central, `okf/spec/`, e não em `.okf/specs/`
  dentro de cada bundle. Duas das nossas governam assunto e processo em vez de
  tipo — as janelas temporais valem para `Regra` **e** para a projeção de
  `RegraProposta`, que vivem em bundles diferentes — e não teriam casa numa
  disposição por bundle. Também é o namespace único que o gate de decisões
  verificáveis procura, e espalhá-lo devolveria o "procure em toda parte" que
  a revisão mandou tirar de lá;
- a regra é **normativa**, não consultiva. O issue sugere consultiva por
  causa de bundles legados cheios de tipo sem documento; aqui todos os tipos
  em uso passaram a ter spec no mesmo commit em que este script entrou, então
  não há dívida a tolerar.

**O que ele confere é existência, não correspondência.** Nada exige que
`regra.md` declare `id: regra`, e nada acusa spec órfã — arquivo de tipo que
documento nenhum usa. A derivação também é many-to-one: `Regra` e `regra`
procuram o mesmo arquivo. Nenhuma das duas coisas produziu defeito ainda, e
guarda nova aqui exige caso concreto.

Quando o `okf-parser` implementar `--require-spec`, este script sai e o
comando entra no lugar dele. O que não pode é a regra depender de alguém
lembrar.
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
import unicodedata
from pathlib import Path

from okf_parser.parser import parse_document

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
BUNDLES = REPO_ROOT / "okf"
SPECS = REPO_ROOT / "okf/spec"
#: Nomes reservados pela spec OKF v0.2 — não são conceitos e não têm `type`.
RESERVADOS = frozenset({"index.md", "log.md"})


class TipoSemSlugError(Exception):
    """Levantada quando um `type` não deriva nome de arquivo algum."""


class DocumentoIlegivelError(Exception):
    """Levantada quando um `.md` do bundle não abre pelo parser."""


def slug(tipo: str) -> str:
    """O nome de arquivo derivado de um `type`, pela regra do okf-parser#25.

    Minúsculas, sem acento nem cedilha, espaço e barra viram hífen, o resto do
    que não é alfanumérico cai. `RegraProposta` vira `regraproposta`, e não
    `regra-proposta`: a regra não quebra CamelCase, e inventar essa quebra aqui
    faria a derivação local divergir da do parser no dia em que ele a
    implementar — que é o dia em que este script sai.

    Levanta `TipoSemSlugError` quando não sobra caractere algum: um `type` que
    não deriva nome de arquivo faria o script cobrar `okf/spec/.md`, que se lê
    como defeito do gate e não do documento.
    """
    sem_acento = unicodedata.normalize("NFKD", tipo).encode("ascii", "ignore").decode()
    com_hifen = re.sub(r"[\s/]+", "-", sem_acento.strip().lower())
    derivado = re.sub(r"[^a-z0-9-]", "", com_hifen)
    if not derivado:
        msg = f"`type: {tipo}` não deriva nome de arquivo algum"
        raise TipoSemSlugError(msg)
    return derivado


def tipos_em_uso(raiz: Path) -> dict[str, list[str]]:
    """Todo `type` encontrado nos bundles, com os documentos que o usam.

    Lê o frontmatter pelo mesmo parser do resto do repositório: `type` é o que
    o documento declara, nunca o que o nome do diretório sugere.
    """
    encontrados: dict[str, list[str]] = {}
    for caminho in sorted(raiz.rglob("*.md")):
        if caminho.name in RESERVADOS:
            continue
        try:
            documento = parse_document(caminho)
        except Exception as erro:  # o parser levanta o que a fonte provocar
            msg = f"{caminho.relative_to(REPO_ROOT)} não abre pelo parser: {erro}"
            raise DocumentoIlegivelError(msg) from erro
        tipo = documento.frontmatter.get("type")
        if not isinstance(tipo, str) or not tipo.strip():
            continue
        encontrados.setdefault(tipo.strip(), []).append(str(caminho.relative_to(REPO_ROOT)))
    return encontrados


def sem_spec(tipos: dict[str, list[str]], specs: Path) -> list[tuple[str, str, int]]:
    """Os tipos sem documento de especificação, como (tipo, arquivo esperado, quantos usam).

    Recebe os tipos já levantados, e não a raiz: percorrer os bundles é o custo
    do script, e fazê-lo de novo só para contar reparsearia tudo duas vezes.
    """
    faltando = []
    for tipo, documentos in sorted(tipos.items()):
        esperado = specs / f"{slug(tipo)}.md"
        if not esperado.is_file():
            faltando.append((tipo, str(esperado.relative_to(REPO_ROOT)), len(documentos)))
    return faltando


def main(argv: list[str] | None = None) -> int:
    """CLI: sai com 1 listando todo tipo em uso que não tem especificação."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundles", type=Path, default=BUNDLES, help="raiz dos bundles a percorrer")
    parser.add_argument(
        "--specs", type=Path, default=SPECS, help="onde a especificação de um tipo é procurada"
    )
    args = parser.parse_args(argv)

    tipos = tipos_em_uso(args.bundles)
    faltando = sem_spec(tipos, args.specs)
    if faltando:
        linhas = [
            f"  {tipo}: {documentos} documento(s), falta {esperado}"
            for tipo, esperado, documentos in faltando
        ]
        logger.error("Tipo em uso sem documento de especificação:\n%s", "\n".join(linhas))
        return 1

    logger.info("Os %d tipos em uso têm documento de especificação.", len(tipos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
