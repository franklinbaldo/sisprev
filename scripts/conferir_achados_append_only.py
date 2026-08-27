#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
# ]
# ///
"""Confere que nenhum `achado-*.md` presente numa base de comparação sumiu.

Um `Achado` é uma acusação datada, e outros documentos o citam pelo id
(`okf/spec/achado.md`: "não se apaga e não se renumera"). O CI aplicava essa
regra percorrendo `git log --diff-filter=A` sobre a história inteira do ref
checado — o que fossiliza também achado criado e removido dentro da mesma PR
ainda não mergeada, porque a história de uma PR aberta contém todos os
commits da sua branch. Foi o que aconteceu com `achado-0061` (PR #128):
registrado e revertido em duas rodadas sem nunca ter chegado a `main`, e a
versão anterior do gate exigiu restaurá-lo só para o CI passar.

A garantia "não se apaga" só faz sentido a partir do instante em que o
achado chega a `main`. Este script confere isso comparando o estado atual
contra uma única base — o merge-base com a branch de destino, numa PR; o
commit anterior ao push, num push direto a `main` — em vez de vasculhar
commits internos da branch em busca de qualquer arquivo que já tenha
existido.
"""

from __future__ import annotations

import argparse
import logging
import subprocess
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
PADRAO_ACHADO = "okf/regras-sisprev/achados/achado-*.md"


class GitDiffError(Exception):
    """Levantada quando o `git diff` contra a base falha — base inexistente, por exemplo."""


def achados_removidos(raiz: Path, base: str) -> list[str]:
    """Os caminhos de achado presentes em `base` e ausentes no estado atual de `raiz`.

    `--no-renames` é o que torna a checagem robusta a burla por
    renomeação: sem ele, o `git diff` pode relatar a troca de nome de um
    achado como um único evento de renomeação, que `--diff-filter=D` não
    captura. Com renomeação desligada, toda renomeação aparece como uma
    exclusão do caminho antigo — e é a exclusão que este gate reprova,
    tanto para apagar quanto para renomear.
    """
    resultado = subprocess.run(
        ["git", "diff", "--no-renames", "--diff-filter=D", "--name-only", base, "--", PADRAO_ACHADO],
        cwd=raiz,
        capture_output=True,
        text=True,
        check=False,
    )
    if resultado.returncode != 0:
        msg = f"git diff contra {base} falhou: {resultado.stderr.strip()}"
        raise GitDiffError(msg)
    return [linha for linha in resultado.stdout.splitlines() if linha]


def main(argv: list[str] | None = None) -> int:
    """CLI: sai com 1 listando todo achado presente na base e ausente agora."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base", required=True, help="commit-ish contra o qual comparar (merge-base ou github.event.before)"
    )
    parser.add_argument("--raiz", type=Path, default=REPO_ROOT, help="raiz do repositório git a conferir")
    args = parser.parse_args(argv)

    removidos = achados_removidos(args.raiz, args.base)
    if removidos:
        linhas = "\n".join(
            f"  {caminho} existia em {args.base} e não está mais no repositório." for caminho in removidos
        )
        logger.error("Achado removido ou renomeado depois de já estar em main:\n%s", linhas)
        return 1

    logger.info("Nenhum achado presente em %s desapareceu.", args.base)
    return 0


if __name__ == "__main__":
    sys.exit(main())
