"""Harness genérico de casos jurídicos contra o catálogo legado.

O filtro do site é conservador e esta implementação reproduz somente os critérios
estruturados que ele consegue avaliar. A expectativa jurídica fica separada do catálogo;
casos novos são fixtures de dados e teses novas entram no registro de callbacks.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import UTC, date, datetime
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from pathlib import Path

from bundle import Bundle, Regra
from okf_common import DEFAULT_BUNDLE
from sentinela import sentinela_de

Faixa = tuple[int, int]
Fatos = Mapping[str, object]
AvaliadorJuridico = Callable[[Fatos], "ExpectativaJuridica"]


class SimuladorCasoError(ValueError):
    """Erro de entrada do catálogo ou da fixture."""


@dataclass(frozen=True)
class ExpectativaJuridica:
    """Expectativa jurídica independente do catálogo legado."""

    elegivel: bool
    faixa_legal: Faixa | None
    tabelapontuacao: str


@dataclass(frozen=True)
class CasoSimulado:
    """Fixture genérica com fatos, escopo e avaliador registrado."""

    id: str
    fatos: Fatos
    escopo: Literal["catalogo-legado"] = "catalogo-legado"
    avaliador: str = "ece146_art8"
    diagnosticos_esperados: tuple[str, ...] = ()


@dataclass(frozen=True)
class RegraConhecida:
    """Campos usados pela assinatura de critérios conhecida do seletor."""

    id: str
    tipo_de_beneficio: str
    sexo: str
    apos_especial: str
    simulavel: str
    status_regra: str
    data_adm_apos: date | None
    data_adm_ate: date | None
    data_direito_apos: date | None
    data_direito_ate: date | None
    tabelapontuacao: str


@dataclass(frozen=True)
class ResultadoCaso:
    """Resultado comparativo do runner."""

    caso_id: str
    expectativa: ExpectativaJuridica
    candidatos_legados: tuple[str, ...]
    tabelapontuacao_legada: tuple[str, ...]
    faixa_alcancada: Faixa | None
    divergencias: tuple[str, ...]


def _data(value: object) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        for formato in ("%d/%m/%Y %H:%M", "%d/%m/%Y"):
            try:
                return datetime.strptime(value, formato).replace(tzinfo=UTC).date()
            except ValueError:
                continue
    msg = f"data de catálogo inválida: {value!r}"
    raise SimuladorCasoError(msg)


def _limite_avaliavel(value: object) -> date | None:
    limite = _data(value)
    return None if limite is None or sentinela_de(limite.strftime("%d/%m/%Y 00:00")) is not None else limite


def _regra(regra: Regra) -> RegraConhecida:
    fm = regra.frontmatter
    return RegraConhecida(
        id=regra.doc_id,
        tipo_de_beneficio=str(fm.get("tipo_de_beneficio", "")),
        sexo=str(fm.get("sexo", "")),
        apos_especial=str(fm.get("apos_especial", "")),
        simulavel=str(fm.get("simulavel", "")),
        status_regra=regra.status_regra,
        data_adm_apos=_limite_avaliavel(fm.get("data_adm_apos")),
        data_adm_ate=_limite_avaliavel(fm.get("data_adm_ate")),
        data_direito_apos=_limite_avaliavel(fm.get("data_direito_apos")),
        data_direito_ate=_limite_avaliavel(fm.get("data_direito_ate")),
        tabelapontuacao=str(fm.get("tabelapontuacao", "")),
    )


def carregar_catalogo(bundle_dir: Path = DEFAULT_BUNDLE) -> tuple[RegraConhecida, ...]:
    """Carrega e normaliza pelo carregador único de Bundle."""
    return tuple(_regra(regra) for regra in Bundle.load(bundle_dir).regras)


def assinatura_criterios_conhecidos(regra: RegraConhecida) -> tuple[object, ...]:
    """Assinatura dos mesmos critérios estruturados usados pelo seletor."""
    return (
        regra.tipo_de_beneficio,
        regra.sexo,
        regra.apos_especial,
        regra.data_adm_apos,
        regra.data_adm_ate,
        regra.data_direito_apos,
        regra.data_direito_ate,
    )


def _dentro(value: object, inferior: date | None, superior: date | None) -> bool:
    fato = _data(value)
    return (
        fato is not None and (inferior is None or fato >= inferior) and (superior is None or fato <= superior)
    )


def selecionar_regras(catalogo: tuple[RegraConhecida, ...], fatos: Fatos) -> tuple[RegraConhecida, ...]:
    """Reproduz os critérios conhecidos do avaliarSolicitacao do site."""
    tipo = str(fatos.get("tipo_de_beneficio", ""))
    sexo = fatos.get("sexo")
    especial = fatos.get("apos_especial")
    return tuple(
        regra
        for regra in catalogo
        if regra.simulavel == "S"
        and regra.status_regra == "ativa"
        and regra.tipo_de_beneficio == tipo
        and (regra.sexo in ("", "AMBOS") or regra.sexo == sexo)
        and (especial is None or regra.apos_especial == str(especial))
        and _dentro(fatos.get("data_admissao"), regra.data_adm_apos, regra.data_adm_ate)
        and _dentro(fatos.get("data_direito"), regra.data_direito_apos, regra.data_direito_ate)
    )


MINIMO_SERVICO_PUBLICO = 20
MINIMO_TEMPO_NO_CARGO = 5


def _ece146_art8(fatos: Fatos) -> ExpectativaJuridica:
    """Trata 66/15, 76/20 e 86/25 como limiares, não igualdade exata."""
    pontos = int(fatos["pontos"])
    exposicao = int(fatos["anos_exposicao"])
    faixas = ((66, 15), (76, 20), (86, 25))
    aplicaveis = tuple(faixa for faixa in faixas if pontos >= faixa[0] and exposicao >= faixa[1])
    faixa = aplicaveis[-1] if aplicaveis else None
    admissao = _data(fatos["data_admissao"])
    direito = _data(fatos["data_direito"])
    elegivel = (
        admissao is not None
        and admissao <= date(2021, 9, 14)
        and direito is not None
        and direito >= date(2021, 9, 14)
        and int(fatos["anos_servico_publico"]) >= MINIMO_SERVICO_PUBLICO
        and int(fatos["anos_no_cargo"]) >= MINIMO_TEMPO_NO_CARGO
        and faixa is not None
    )
    return ExpectativaJuridica(elegivel=elegivel, faixa_legal=faixa, tabelapontuacao="N")


AVALIADORES: dict[str, AvaliadorJuridico] = {"ece146_art8": _ece146_art8}


def executar_caso(caso: CasoSimulado, catalogo: tuple[RegraConhecida, ...]) -> ResultadoCaso:
    """Executa a fixture contra o cat�logo e registra diverg�ncias."""
    try:
        avaliador = AVALIADORES[caso.avaliador]
    except KeyError as exc:
        msg = f"avaliador jurídico não registrado: {caso.avaliador}"
        raise SimuladorCasoError(msg) from exc
    expectativa = avaliador(caso.fatos)
    candidatos = selecionar_regras(catalogo, caso.fatos) if expectativa.elegivel else ()
    tabelas = tuple(sorted({regra.tabelapontuacao for regra in candidatos}))
    divergencias: list[str] = []
    if tabelas != (expectativa.tabelapontuacao,):
        divergencias.append(f"tabelapontuacao legado={tabelas!r}, esperado={expectativa.tabelapontuacao!r}")
    esperado = 1 if expectativa.elegivel else 0
    if len(candidatos) != esperado:
        divergencias.append(
            f"caso {expectativa.faixa_legal!r} devolveu {len(candidatos)} regras; esperado={esperado}"
        )
    return ResultadoCaso(
        caso_id=caso.id,
        expectativa=expectativa,
        candidatos_legados=tuple(regra.id for regra in candidatos),
        tabelapontuacao_legada=tabelas,
        faixa_alcancada=expectativa.faixa_legal,
        divergencias=tuple(divergencias),
    )
