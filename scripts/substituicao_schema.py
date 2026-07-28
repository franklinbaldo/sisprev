"""RFC 0004 §1.4/§1.5 + RFC 0006 §3 — o grupo atômico de substituição, sem dono.

Um **grupo de substituição** declara que um conjunto de regras legadas é
substituído por um conjunto de unidades auditadas, e que isso vale **inteiro
ou não vale** — nunca destino por destino (RFC 0004 §1.4).

Este módulo é deliberadamente **neutro**. O tipo canônico não mora em
``conjunto_schema`` porque o compilador e os testes de proveniência precisam
conhecer *um grupo* sem depender do documento agregado inteiro; e não mora no
antigo ``manifesto_substituicao`` porque aquele manifesto global está sendo
aposentado — a partir da fase 1 da RFC 0006 os grupos vivem em
``Conjunto.substituicoes``, e um tipo canônico dentro do módulo que morre
seria dívida de nascença.

**Duas grafias de identidade, uma conversão explícita.** O grupo endereça por
**link OKF** (``/regras/regra-0022.md``), porque um conjunto compõe um
catálogo heterogêneo — regra legada e unidade auditada convivem nele, e o
prefixo do link é o que diz de qual bundle o item vem. Já a unidade auditada
declara suas origens por **id nu** (``regra-0022``), que é o espaço de
identidade nativo dela. As duas grafias são reais e nenhuma é errada; o que
seria errado é comparar uma com a outra sem dizer. Daí ``ref_de_regra_legada``
/ ``id_da_ref`` serem funções nomeadas e usadas em ambos os lados, em vez de
uma fatia de string escondida dentro de um `if`.
"""

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Protocol, Self

from detections import Violation
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence


class DestinoAuditado(Protocol):
    """A superfície mínima que um destino de substituição precisa expor.

    Protocolo estrutural em vez de ``UnidadeAuditada`` concreta: este módulo é
    neutro por desenho, e depender do schema do catálogo auditado tornaria a
    neutralidade nominal. O que um grupo precisa saber de um destino é só
    isto — quem ele é, de quem descende, e se está pronto.
    """

    @property
    def doc_id(self) -> str:
        """The unit's own stable id, in the audited bundle's identity space."""
        ...

    @property
    def origens_legacy(self) -> Sequence[str]:
        """The legacy rule ids this unit declares descending from — bare ids."""
        ...

    @property
    def estado_unidade(self) -> str:
        """``elaboracao`` | ``preview`` | ``deployable`` (RFC 0004 §5.3)."""
        ...


PREFIXO_REGRA_LEGADA = "/regras/"
PREFIXO_UNIDADE_AUDITADA = "/regras-auditadas/unidades/"


def ref_de_regra_legada(regra_id: str) -> str:
    """``regra-0022`` -> ``/regras/regra-0022.md``."""
    return f"{PREFIXO_REGRA_LEGADA}{regra_id}.md"


def ref_de_unidade_auditada(unidade_id: str) -> str:
    """``invalidez-acidente`` -> ``/regras-auditadas/unidades/invalidez-acidente.md``."""
    return f"{PREFIXO_UNIDADE_AUDITADA}{unidade_id}.md"


def id_da_ref(ref: str) -> str:
    """Return the bare id an OKF link names, whichever bundle it points at."""
    return ref.rsplit("/", 1)[-1].removesuffix(".md")


def parse_iso_date(value: object) -> object:
    """Accept YAML dates or strict ISO date strings — same rule as every other schema here."""
    if value is None or isinstance(value, datetime.date):
        return value
    if isinstance(value, str):
        return datetime.date.fromisoformat(value)
    return value


class DecisaoCompletude(BaseModel):
    """A decisão humana de que um grupo (ou um conjunto) está completo (RFC 0004 §1.4).

    Estruturada, nunca prosa: completude inferida do que existe em disco é
    verdadeira por construção — o sistema não tem como saber que faltava
    escrever uma terceira descendente que ninguém escreveu.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    decidido_por: str = Field(min_length=1)
    decidido_em: datetime.date
    justificativa: str = Field(min_length=1)
    fonte: str = Field(min_length=1)

    _check_data = field_validator("decidido_em", mode="before")(parse_iso_date)


class GrupoSubstituicao(BaseModel):
    """Um grupo atômico de substituição — ativa e reverte inteiro (RFC 0004 §1.4).

    ``origens_legacy`` e ``destinos_auditados`` são listas não vazias, o que
    cobre 1:N (decomposição) e N:1 (consolidação) e **exclui** substituição
    sem sucessora ou introdução sem antecessora — para essas o conjunto tem
    ``revoga`` e ``introduz`` (RFC 0006 §3).
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    grupo: str = Field(min_length=1)
    origens_legacy: tuple[str, ...] = Field(min_length=1)
    destinos_auditados: tuple[str, ...] = Field(min_length=1)
    estado_grupo: Literal["inativo", "ativo"] = "inativo"
    decisao_completude: DecisaoCompletude | None = None

    @model_validator(mode="after")
    def _check_ativacao(self) -> Self:
        """Ativação exige a decisão humana registrada (RFC 0004 §1.4)."""
        if self.estado_grupo == "ativo" and self.decisao_completude is None:
            msg = "estado_grupo='ativo' requires decisao_completude"
            raise ValueError(msg)
        return self


def checar_proveniencia(
    grupo: GrupoSubstituicao,
    unidades_por_id: dict[str, DestinoAuditado],
) -> list[Violation]:
    """As origens que o grupo declara devem ser exatamente as que seus destinos reconhecem.

    Esta é a propriedade que o resolvedor de pertinência (RFC 0006 §3) **não**
    prova: ele calcula quem entra e quem sai do catálogo, mas nada nele exige
    que os destinos reconheçam as origens que o conjunto afirma substituir.
    Sem esta verificação, um conjunto poderia declarar que a unidade X
    substitui a regra-0022 enquanto a própria X diz descender de outra — uma
    substituição que o catálogo aceitaria e que ninguém autorou.

    Checada **independentemente de ``estado_grupo``**: uma divergência é
    defeito da declaração, e esperar a ativação para reportá-la é descobri-la
    no pior momento. Destinos desconhecidos são ignorados aqui — quem os
    reporta é ``validar_grupos``, e comparar contra uma unidade que não se
    consegue ler produziria uma divergência espúria em cima do erro real.
    """
    origens_dos_destinos: set[str] = set()
    for destino in grupo.destinos_auditados:
        unidade = unidades_por_id.get(id_da_ref(destino))
        if unidade is not None:
            origens_dos_destinos.update(ref_de_regra_legada(origem) for origem in unidade.origens_legacy)
    origens_do_grupo = set(grupo.origens_legacy)

    violations: list[Violation] = []
    excedentes = sorted(origens_dos_destinos - origens_do_grupo)
    if excedentes:
        violations.append(
            Violation(
                "P15_PROVENIENCIA_DIVERGENTE",
                f"grupo {grupo.grupo!r}: destino(s) declaram origem(ns) {excedentes} fora de "
                "origens_legacy do grupo",
            )
        )
    nao_cobertas = sorted(origens_do_grupo - origens_dos_destinos)
    if nao_cobertas:
        violations.append(
            Violation(
                "P15_PROVENIENCIA_INCOMPLETA",
                f"grupo {grupo.grupo!r}: origem(ns) {nao_cobertas} não são cobertas por nenhum "
                "destino_auditado",
            )
        )
    return violations


def _checar_ativacao(
    grupo: GrupoSubstituicao,
    unidades_por_id: dict[str, DestinoAuditado],
) -> list[Violation]:
    nao_deployable = sorted(
        destino
        for destino in grupo.destinos_auditados
        if (unidade := unidades_por_id.get(id_da_ref(destino))) is not None
        and unidade.estado_unidade != "deployable"
    )
    if not nao_deployable:
        return []
    return [
        Violation(
            "P15_GRUPO_PARCIAL",
            f"grupo {grupo.grupo!r} está estado_grupo=ativo mas destino(s) "
            f"{nao_deployable} não estão deployable",
        )
    ]


def validar_grupos(
    grupos: Sequence[GrupoSubstituicao],
    *,
    unidades: Iterable[DestinoAuditado],
    refs_legadas: frozenset[str],
) -> list[Violation]:
    """Every cross-group structural invariant, wherever the groups are declared.

    Takes the groups, not the document holding them: the same rules apply to
    a conjunto's ``substituicoes`` and to any other future carrier, and the
    caller is the one who knows which document to blame.
    """
    unidades_por_id = {unidade.doc_id: unidade for unidade in unidades}
    violations: list[Violation] = []

    ids = [grupo.grupo for grupo in grupos]
    violations.extend(
        Violation("P15_GRUPO_DUPLICADO", f"duplicate grupo id {dup!r}")
        for dup in sorted({gid for gid in ids if ids.count(gid) > 1})
    )

    origens_ativas: dict[str, list[str]] = {}
    donos_de_destino: dict[str, list[str]] = {}
    for grupo in grupos:
        for origem in grupo.origens_legacy:
            if origem not in refs_legadas:
                violations.append(
                    Violation(
                        "P15_ORIGEM_INEXISTENTE",
                        f"grupo {grupo.grupo!r} references unknown legacy rule {origem!r}",
                    )
                )
            if grupo.estado_grupo == "ativo":
                origens_ativas.setdefault(origem, []).append(grupo.grupo)
        for destino in grupo.destinos_auditados:
            if id_da_ref(destino) not in unidades_por_id:
                violations.append(
                    Violation(
                        "P15_DESTINO_INEXISTENTE",
                        f"grupo {grupo.grupo!r} references unknown audited unit {destino!r}",
                    )
                )
            donos_de_destino.setdefault(destino, []).append(grupo.grupo)

        violations.extend(checar_proveniencia(grupo, unidades_por_id))

        if grupo.estado_grupo == "ativo":
            violations.extend(_checar_ativacao(grupo, unidades_por_id))
        elif grupo.decisao_completude is not None:
            violations.append(
                Violation(
                    "P15_DECISAO_SEM_ATIVACAO",
                    f"grupo {grupo.grupo!r} está estado_grupo=inativo mas ainda carrega "
                    "decisao_completude — rollback deve limpá-la",
                )
            )

    violations.extend(
        Violation(
            "P15_ORIGEM_EM_GRUPOS_ATIVOS",
            f"legacy rule {origem!r} claimed by more than one active grupo {sorted(donos)}",
        )
        for origem, donos in origens_ativas.items()
        if len(donos) > 1
    )
    violations.extend(
        Violation(
            "P15_DESTINO_EM_GRUPOS_CONFLITANTES",
            f"audited unit {destino!r} claimed by more than one grupo {sorted(donos)}",
        )
        for destino, donos in donos_de_destino.items()
        if len(donos) > 1
    )
    return violations


def selecionar_origem_operacional(
    regra_id: str,
    grupos: Sequence[GrupoSubstituicao],
) -> Literal["legado", "auditado"]:
    """RFC 0004 §1.5 — a origem única do exportador para uma regra legada.

    Devolve ``"auditado"`` apenas quando ``regra_id`` está nas origens de um
    grupo cujo ``estado_grupo`` é ``"ativo"`` — nunca por um destino que
    esteja ``deployable`` isoladamente. Exatamente um valor de retorno por
    chamada é o que torna "nunca as duas ao mesmo tempo"
    (``P_EXPORT_ORIGEM_DUPLA``) estruturalmente impossível de violar aqui.
    """
    ref = ref_de_regra_legada(regra_id)
    for grupo in grupos:
        if grupo.estado_grupo == "ativo" and ref in grupo.origens_legacy:
            return "auditado"
    return "legado"
