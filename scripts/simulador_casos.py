"""Simulador explícito de casos jurídicos para a auditoria.

O simulador de ``site/src/lib/simulador.ts`` é um filtro conservador de
triagem, não um calculador de benefício. Este módulo tem outro contrato:
recebe um caso sintético, aplica os requisitos legais já transcritos e compara
o desfecho esperado com os campos da regra legada. Ele é deliberadamente
pequeno e específico; não pretende substituir o motor do Sisprev.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import TYPE_CHECKING

import yaml

if TYPE_CHECKING:
    from pathlib import Path

FAIXAS_ECE_146: frozenset[tuple[int, int]] = frozenset({(66, 15), (76, 20), (86, 25)})
REGRAS_ECE_146 = ("regra-0068", "regra-0069", "regra-0070")
MINIMO_SERVICO_PUBLICO = 20
MINIMO_TEMPO_NO_CARGO = 5


class SimuladorCasoError(ValueError):
    """Erro de entrada do catálogo usado pelo simulador de casos."""


@dataclass(frozen=True)
class CasoAgentesNocivos:
    """Fatos objetivos necessários para testar o art. 8º da ECE 146/2021."""

    data_admissao: date
    data_direito: date
    anos_servico_publico: int
    anos_no_cargo: int
    pontos: int
    anos_exposicao: int


@dataclass(frozen=True)
class ResultadoSimulacao:
    """Desfecho legal e divergências observadas no catálogo legado."""

    elegivel: bool
    faixa_legal: tuple[int, int] | None
    candidatos_legados: tuple[str, ...]
    tabelapontuacao_legada: str | None
    tabelapontuacao_esperada: str
    divergencias: tuple[str, ...]


def _carregar_regra(regra_id: str, regras_dir: Path) -> dict[str, object]:
    texto = (regras_dir / f"{regra_id}.md").read_text(encoding="utf-8")
    _, frontmatter, _ = texto.split("---", 2)
    resultado = yaml.safe_load(frontmatter)
    if not isinstance(resultado, dict):
        mensagem = f"frontmatter inválido para {regra_id}"
        raise SimuladorCasoError(mensagem)
    return resultado


def _faixa_legal(caso: CasoAgentesNocivos) -> tuple[int, int] | None:
    faixa = (caso.pontos, caso.anos_exposicao)
    if faixa not in FAIXAS_ECE_146:
        return None
    return faixa


def simular_agentes_nocivos_ece146(
    caso: CasoAgentesNocivos,
    *,
    regras_dir: Path,
) -> ResultadoSimulacao:
    """Simula o caso e compara o resultado legal com 0068--0070.

    A ECE 146 fixa três faixas; portanto, a projeção jurídica esperada para
    ``tabelapontuacao`` é ``N`` sob a leitura adotada no achado-0054. O campo
    legado é reportado, nunca corrigido pelo simulador.
    """
    faixa = _faixa_legal(caso)
    elegivel = (
        caso.data_admissao <= date(2021, 9, 14)
        and caso.data_direito >= date(2021, 9, 14)
        and caso.anos_servico_publico >= MINIMO_SERVICO_PUBLICO
        and caso.anos_no_cargo >= MINIMO_TEMPO_NO_CARGO
        and faixa is not None
    )

    candidatos: list[str] = []
    valores_tabela: set[str] = set()
    for regra_id in REGRAS_ECE_146:
        regra = _carregar_regra(regra_id, regras_dir)
        if (
            elegivel
            and regra["tipo_de_beneficio"] == "APOSENTADORIA VOLUNTÁRIA POR TEMPO DE CONTRIBUIÇÃO"
            and regra["apos_especial"] == "S"
        ):
            candidatos.append(regra_id)
            valores_tabela.add(str(regra.get("tabelapontuacao", "")))

    tabela_legada = next(iter(valores_tabela), None) if len(valores_tabela) == 1 else None
    esperado = "N"
    divergencias: list[str] = []
    if tabela_legada != esperado:
        divergencias.append(
            f"tabelapontuacao legado={tabela_legada!r}, esperado={esperado!r} para faixas fixas"
        )
    if len(candidatos) != (1 if elegivel else 0):
        divergencias.append(
            f"caso {faixa!r} devolveu {len(candidatos)} regras legadas; esperado={1 if elegivel else 0}"
        )

    return ResultadoSimulacao(
        elegivel=elegivel,
        faixa_legal=faixa,
        candidatos_legados=tuple(candidatos),
        tabelapontuacao_legada=tabela_legada,
        tabelapontuacao_esperada=esperado,
        divergencias=tuple(divergencias),
    )
