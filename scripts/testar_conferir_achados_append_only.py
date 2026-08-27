#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.13"
# dependencies = [
# ]
# ///
"""Testa `conferir_achados_append_only.py` contra os cenários que já o quebraram.

Não há framework de teste neste repositório, e um específico só para este
script seria infraestrutura sem uso além daqui. Cada caso monta um
repositório git descartável num diretório temporário, comita o cenário e
chama `achados_removidos` diretamente contra ele — sem subprocess aninhado,
sem mock de `git`.
"""

from __future__ import annotations

import logging
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conferir_achados_append_only import achados_removidos

logger = logging.getLogger(__name__)

ACHADOS = Path("okf/regras-sisprev/achados")


def _git(raiz: Path, *args: str) -> None:
    """Roda `git` em `raiz`, levantando se o comando falhar."""
    subprocess.run(["git", *args], cwd=raiz, check=True, capture_output=True, text=True)


def _commit(raiz: Path, mensagem: str) -> str:
    """Adiciona tudo, comita e devolve o SHA do commit criado."""
    _git(raiz, "add", "-A")
    _git(raiz, "commit", "-m", mensagem, "--quiet")
    resultado = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=raiz, check=True, capture_output=True, text=True
    )
    return resultado.stdout.strip()


def _escrever(raiz: Path, caminho: Path, conteudo: str) -> None:
    """Escreve `conteudo` em `raiz / caminho`, criando diretórios pais."""
    alvo = raiz / caminho
    alvo.parent.mkdir(parents=True, exist_ok=True)
    alvo.write_text(conteudo)


def _novo_repo() -> Path:
    """Um repositório git vazio, novo, em diretório temporário."""
    raiz = Path(tempfile.mkdtemp(prefix="gate-achado-"))
    _git(raiz, "init", "--quiet", "--initial-branch=main")
    _git(raiz, "config", "user.email", "teste@example.com")
    _git(raiz, "config", "user.name", "Teste")
    return raiz


def caso_criado_e_removido_na_mesma_pr(raiz: Path) -> str:
    """Achado nasce e morre dentro da mesma PR, sem nunca ter existido em `main`."""
    _escrever(raiz, Path("README.md"), "repo de teste")
    base = _commit(raiz, "main inicial, sem achados")
    _escrever(raiz, ACHADOS / "achado-0099.md", "conteúdo transitório")
    _commit(raiz, "cria achado-0099 na PR")
    (raiz / ACHADOS / "achado-0099.md").unlink()
    _commit(raiz, "remove achado-0099 antes do merge")
    return base


def caso_marcado_improcedente(raiz: Path) -> str:
    """Achado existente em `main` tem só `situacao` alterada para `improcedente`."""
    _escrever(raiz, ACHADOS / "achado-0001.md", "situacao: aberto")
    base = _commit(raiz, "main com achado-0001 aberto")
    _escrever(raiz, ACHADOS / "achado-0001.md", "situacao: improcedente")
    _commit(raiz, "marca achado-0001 improcedente")
    return base


def caso_conteudo_acrescido(raiz: Path) -> str:
    """Achado existente em `main` recebe seção nova, sem apagar o que já havia."""
    _escrever(raiz, ACHADOS / "achado-0002.md", "corpo original")
    base = _commit(raiz, "main com achado-0002")
    _escrever(raiz, ACHADOS / "achado-0002.md", "corpo original\n\n# Resolução\n\nmais texto")
    _commit(raiz, "acrescenta resolução ao achado-0002")
    return base


def caso_exclusao_apos_main(raiz: Path) -> str:
    """Achado que já existia em `main` é apagado depois."""
    _escrever(raiz, ACHADOS / "achado-0003.md", "corpo")
    base = _commit(raiz, "main com achado-0003")
    (raiz / ACHADOS / "achado-0003.md").unlink()
    _commit(raiz, "apaga achado-0003")
    return base


def caso_renomeacao_apos_main(raiz: Path) -> str:
    """Achado que já existia em `main` é renomeado — mesmo conteúdo, id novo."""
    _escrever(raiz, ACHADOS / "achado-0004.md", "corpo idêntico")
    base = _commit(raiz, "main com achado-0004")
    _git(raiz, "mv", str(ACHADOS / "achado-0004.md"), str(ACHADOS / "achado-0004-renomeado.md"))
    _commit(raiz, "renomeia achado-0004")
    return base


def caso_substituicao_por_outro_id(raiz: Path) -> str:
    """Achado que já existia em `main` é apagado e substituído por outro id, sem relação."""
    _escrever(raiz, ACHADOS / "achado-0005.md", "corpo do 0005")
    base = _commit(raiz, "main com achado-0005")
    (raiz / ACHADOS / "achado-0005.md").unlink()
    _escrever(raiz, ACHADOS / "achado-0006.md", "corpo do 0006, sem relação com o 0005")
    _commit(raiz, "substitui achado-0005 por achado-0006")
    return base


#: (nome, deve_passar, montagem). "Passar" é o gate não acusar nada.
CASOS: list[tuple[str, bool, Callable[[Path], str]]] = [
    ("achado criado e removido na mesma PR, nunca existiu em main", True, caso_criado_e_removido_na_mesma_pr),
    ("achado existente em main marcado improcedente", True, caso_marcado_improcedente),
    ("conteúdo acrescido a achado existente, sem apagar", True, caso_conteudo_acrescido),
    ("exclusão de achado que já existia em main", False, caso_exclusao_apos_main),
    ("renomeação de achado que já existia em main", False, caso_renomeacao_apos_main),
    ("substituição de achado existente por outro id", False, caso_substituicao_por_outro_id),
]


def main() -> int:
    """CLI: roda os seis cenários e sai com 1 se algum não se comportar como esperado."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    falhas = 0
    for nome, deve_passar, montar in CASOS:
        raiz = _novo_repo()
        base = montar(raiz)
        removidos = achados_removidos(raiz, base)
        passou = not removidos
        if passou == deve_passar:
            logger.info("OK    %s", nome)
        else:
            falhas += 1
            esperado = "passar" if deve_passar else "reprovar"
            obtido = "passou" if passou else f"reprovou {removidos}"
            logger.error("FALHA %s — esperado %s, obtido %s", nome, esperado, obtido)

    if falhas:
        logger.error(
            "%d de %d cenários do gate append-only não se comportaram como esperado.", falhas, len(CASOS)
        )
        return 1
    logger.info("Os %d cenários do gate append-only se comportam como esperado.", len(CASOS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
