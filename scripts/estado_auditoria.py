"""P7 — máquina mínima de estados de auditoria (RFC 0001).

``status_auditoria`` is a **join** with ``achados/*`` and the detectors, not
a field whose validity can be checked in isolation — a regra ``revisada``
that starts appearing in an open bloqueante achado's ``regras_afetadas``, or
that re-enters an active P1/P2 group, becomes invalid *without anyone
touching that regra's frontmatter*. That's the point (RFC P7): the CI
re-verifies the join on every commit; nothing here auto-downgrades a regra's
declared state — a human commits the explicit rebaixamento, with the
`P7_ESTADO_INVALIDO` violation as the forcing function.

The intra-document part of the contract (is ``status_auditoria`` one of the
three closed values? does ``auditado_por``/``auditado_em`` form a real,
non-future trail? is ``atos_validacao`` a well-formed list of institutional
acts?) is a Pydantic model, ``RegraAuditoriaContrato`` — same pattern
achado_schema.py already uses for achados. It intentionally covers *only*
the P7/P11 administrative fields, never the domain fields: those stay a
loose dict on ``bundle.Regra`` because P2's material-equality detector
treats every current and future domain field/section as material by
default (RFC 0001, P2 v2) — a strict schema there would contradict that
extensibility. ``extra="ignore"`` lets the model validate just its slice of
a frontmatter dict that also has ``nome``, ``sexo``, and every other
original column mixed in.

Currently enforced invariants:

- ``status_auditoria`` is a **closed enum** (P8) — any value outside
  ``importada``/``revisada``/``validada`` (``RegraAuditoriaContrato``'s
  ``Literal`` field) is itself a violation, checked before anything else. The
  default (``importada``) applies only when the key is genuinely absent;
  Pydantic's own semantics already draw this distinction (a present-but-
  malformed value is validated, not silently defaulted) — no hand-written
  "if key not in frontmatter" check is needed.
- ``revisada``: no achado with ``situacao: aberto`` and
  ``severidade: bloqueante`` references the regra; the regra is not part of
  a currently-detected ``P2_IGUALDADE_MATERIAL_ATIVA`` group (igualdade
  material com outra ativa) nor a currently-detected ``P1_NOME_REPETIDO``
  group, over *all* regras including inactive ones (P1's "unicidade global
  como meta de revisada"); ``auditado_por`` a real non-empty string and
  ``auditado_em`` a real, non-future date (P11 — the transition must leave
  a trail, not just a state flip); a ``# Estado da análise`` body section
  carrying at least one checklist item and **no unticked one** — the CI
  counts ``- [ ]``, never judges whether the items are the right ones.
- ``validada``: every ``revisada`` invariant, plus ``atos_validacao`` a
  non-empty **list**, every item a **mapping** declaring non-empty
  ``tipo``/``autoridade``/``identificador``/``fonte`` — a malformed
  ``atos_validacao`` (wrong type, a non-mapping item, or a field that's
  merely truthy instead of real text) is itself a violation, never silently
  ignored or coerced.

Deliberately **not yet enforced** — the infrastructure they depend on
doesn't exist:

- "dispositivos: vinculados e válidos" — depends on P3 (``okf/dispositivos/``),
  not built yet (Fase 2); once it exists, the fifth P13.1 question
  ("quais dispositivos justificam cada critério e efeito") should become a
  fifth required section, the same way the other four are enforced now;
- the *merit* of the four required sections' content — the CI only checks
  they're non-empty text, never that the answer is correct or complete.
  That remains a human-judgment gate.

The RFC's Q12 (institutional flow behind ``atos_validacao`` — is SEI the
only valid ``fonte``? are PGE and Presidência one act or two?) remains
explicitly unconfirmed; this module does not resolve it and does not fix
``fonte`` to any particular authority.
"""

from __future__ import annotations

import datetime
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Annotated, Literal

from detections import Violation
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    ValidationError,
    ValidationInfo,
    field_validator,
    model_validator,
)
from regra_schema import DISPOSICAO_ACHADOS_KEY, DisposicaoDeAchado

if TYPE_CHECKING:
    from achado_schema import Achado
    from bundle import Bundle, Regra
    from detections import Detection
    from pydantic_core import ErrorDetails

_P2_DETECTOR_ID = "P2_IGUALDADE_MATERIAL_ATIVA"
_P1_DETECTOR_ID = "P1_NOME_REPETIDO"
_ESTADOS_COM_TRILHA_OBRIGATORIA = ("revisada", "validada")

# P13.1's audit-state section for revisada — a flat level-1 heading
# (bundle.py's parser only understands `# Heading`, never `## Heading`).
#
# It replaced four *fixed* headings (Critérios avaliados pelo Sisprev,
# Requisitos de verificação manual, Documentos ou evidências necessários,
# Resultado após a seleção), each of which only had to *exist and be
# non-empty*. That gate passed on the literal text "TODO" — it certified a
# shape, never that any analysis happened. And having a fixed shape, it had
# nowhere to record what was still *missing*, which is the state an audit
# most needs to carry.
#
# The checklist inverts both: the auditor writes the items this particular
# regra needs, and an unticked box blocks `revisada`. Still purely
# structural — counting `- [ ]` is not judging merit, the line this module
# does not cross (see the module docstring). The four questions survive in
# docs/spec/regra.md as the recommended starting items.
SECAO_ESTADO_DA_ANALISE = "Estado da análise"

# GitHub-flavoured task list, recognised by one grammar for both states:
# a line-initial `-`/`*` marker, then a box holding exactly one space (open)
# or `x`/`X` (done), then whitespace or end of line.
#
# The anchor and the lookahead are the whole point. An earlier version tested
# existence with `"- [" in corpo`, which let `- [TODO] conferir`, `- [abc` and
# an inline `texto - [ qualquer coisa` satisfy the gate — a placeholder passed
# again, only spelled differently. Anything that is not exactly an open or a
# closed box is now ordinary prose, and prose alone never satisfies P13.1.
_ITEM_ABERTO_RE = re.compile(r"^[ \t]*[-*][ \t]+\[ \](?=[ \t]|$)", re.MULTILINE)
_ITEM_FECHADO_RE = re.compile(r"^[ \t]*[-*][ \t]+\[[xX]\](?=[ \t]|$)", re.MULTILINE)

# strip_whitespace + min_length=1: rejects "", "   ", and non-str values
# (Pydantic doesn't coerce int/None to str) in one declarative annotation —
# exactly the "real, non-empty text" bar P7/P11 set for these fields.
NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class AtoValidacao(BaseModel):
    """One institutional act backing ``status_auditoria: validada`` (P7).

    ``fonte`` is deliberately free text, not an enum fixed to SEI — the
    RFC's Q12 (is SEI the only valid source of a validation document?)
    remains unconfirmed.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    tipo: NonEmptyStr
    autoridade: NonEmptyStr
    identificador: NonEmptyStr
    fonte: NonEmptyStr


class RegraAuditoriaContrato(BaseModel):
    """The P7/P11 slice of a regra's frontmatter, validated on demand — never stored.

    Pass ``today`` via ``model_validate(..., context={"today": ...})`` for
    the non-future ``auditado_em`` check; omit it (or pass ``None``) to skip
    that check (used by callers that don't care, if any).
    """

    model_config = ConfigDict(extra="ignore")

    status_auditoria: Literal["importada", "revisada", "validada"] = "importada"
    auditado_por: NonEmptyStr | None = None
    auditado_em: datetime.date | None = None
    atos_validacao: list[AtoValidacao] = Field(default_factory=list)

    @field_validator("auditado_em")
    @classmethod
    def _nao_pode_ser_no_futuro(
        cls, value: datetime.date | None, info: ValidationInfo
    ) -> datetime.date | None:
        today = info.context.get("today") if info.context else None
        if value is not None and today is not None and value > today:
            msg = f"está no futuro (hoje: {today})"
            raise ValueError(msg)
        return value

    @model_validator(mode="after")
    def _trilha_p11_obrigatoria_para_revisada_e_validada(self) -> RegraAuditoriaContrato:
        if self.status_auditoria in _ESTADOS_COM_TRILHA_OBRIGATORIA:
            if self.auditado_por is None:
                msg = "auditado_por: exige string não vazia (P11)"
                raise ValueError(msg)
            if self.auditado_em is None:
                msg = "auditado_em: exige data ISO não vazia (P11)"
                raise ValueError(msg)
        return self

    @model_validator(mode="after")
    def _atos_validacao_obrigatorio_para_validada(self) -> RegraAuditoriaContrato:
        if self.status_auditoria == "validada" and not self.atos_validacao:
            msg = "atos_validacao: status_auditoria=validada exige ao menos um ato"
            raise ValueError(msg)
        return self


def _format_pydantic_errors(exc: ValidationError) -> list[str]:
    """One flat message per Pydantic error, ``campo: motivo`` — nothing hidden in a nested structure."""
    return [_format_one_error(err) for err in exc.errors()]


def _format_one_error(err: ErrorDetails) -> str:
    """Render one Pydantic error as ``campo: motivo``, echoing the bad input for structural errors.

    Custom ``raise ValueError(...)`` from our own validators (``type ==
    "value_error"``) already spell out the field name and reason in their
    message — echoing the whole model dict alongside would be redundant.
    Pydantic's own structural rejections (wrong type, bad enum, unparseable
    date) don't, so those get the actual received value appended.
    """
    loc = ".".join(str(part) for part in err["loc"])
    prefix = f"{loc}: " if loc else ""
    if err["type"] == "value_error":
        return f"{prefix}{err['msg']}"
    return f"{prefix}{err['msg']} (recebido: {err['input']!r})"


def _open_bloqueante_regra_ids(bundle: Bundle) -> frozenset[str]:
    """Regra ids referenced by an open, bloqueante achado."""
    return frozenset(
        regra_id
        for achado in bundle.open_achados()
        if achado.frontmatter.get("severidade") == "bloqueante"
        for regra_id in (ref.rsplit("/", 1)[-1].removesuffix(".md") for ref in achado.regras_afetadas)
    )


def _detected_regra_ids(detections: list[Detection], detector_id: str) -> frozenset[str]:
    """Every regra id currently part of any detection from ``detector_id``."""
    ids: set[str] = set()
    for detection in detections:
        if detection.detector == detector_id:
            ids.update(detection.regras)
    return frozenset(ids)


def _secoes_p13_1_errors(regra: Regra) -> list[str]:
    """P13.1: revisada requires `# Estado da análise` with no unticked item.

    Structural only — this counts `- [ ]`, never judges whether the items
    are the right ones or whether the ticked ones are honestly ticked.
    Merit stays a human judgment (see this module's docstring). Body
    sections aren't part of the frontmatter Pydantic validates, so this
    stays a plain check.

    An empty checklist is itself a failure: a section with no item at all
    asserts nothing, and letting it through would rebuild the hole the four
    fixed headings had. So is a section whose only "items" are malformed —
    `- [TODO]` is prose wearing a checkbox, and it must not satisfy the gate.
    """
    corpo = regra.sections.get(SECAO_ESTADO_DA_ANALISE, "")
    if not corpo.strip():
        return [f'"{SECAO_ESTADO_DA_ANALISE}": exige seção não vazia (P13.1)']
    abertos = len(_ITEM_ABERTO_RE.findall(corpo))
    if abertos:
        plural = "itens abertos" if abertos > 1 else "item aberto"
        return [f'"{SECAO_ESTADO_DA_ANALISE}": {abertos} {plural} `- [ ]` (P13.1)']
    if not _ITEM_FECHADO_RE.search(corpo):
        return [f'"{SECAO_ESTADO_DA_ANALISE}": exige ao menos um item de checklist (P13.1)']
    return []


def _disposicao_errors(regra: Regra, achados_por_id: dict[str, Achado]) -> list[str]:
    """Estrutura de ``disposicao_de_achados``: o que vale para qualquer estado.

    Checado sempre, não só em ``revisada``: uma disposição malformada é
    defeito de escrituração mesmo numa regra `importada`, e deixá-la passar
    até a transição atrasaria o erro até o momento em que ele mais custa.

    A reconciliação é o ponto. Uma entrada só é válida se o achado que ela
    nomeia **existe** e **já nomeia esta regra** em ``regras_afetadas``. Sem
    isso o campo seria a segunda ponta declarando a mesma relação, que é
    exatamente o que a convenção de ``dispositivos:``/``precedentes`` evita:
    duas verdades sem gate que as reconcilie.
    """
    admin = regra.admin
    if admin is None:
        # Contrato malformado: sem isto o campo ficaria invisível e o único
        # sintoma seria "achado aberto sem disposição" — o defeito verdadeiro
        # (justificativa vazia, disposicao fora do enum, data impossível)
        # nomeado como sua própria consequência.
        if DISPOSICAO_ACHADOS_KEY not in regra.frontmatter:
            return []
        exc = regra.validation_error
        detalhe = "; ".join(_format_pydantic_errors(exc)) if exc is not None else "contrato inválido"
        return [f"{DISPOSICAO_ACHADOS_KEY}: {detalhe}"]
    reasons: list[str] = []
    vistos: set[str] = set()
    for item in admin.disposicao_de_achados:
        achado_id = item.achado.rsplit("/", 1)[-1].removesuffix(".md")
        if item.achado in vistos:
            reasons.append(f"{achado_id}: disposto mais de uma vez")
            continue
        vistos.add(item.achado)
        achado = achados_por_id.get(achado_id)
        if achado is None:
            reasons.append(f"{achado_id}: disposição de achado que não existe")
            continue
        if regra.doc_id not in _regras_do_achado(achado):
            reasons.append(
                f"{achado_id}: não nomeia esta regra em regras_afetadas — "
                "disposição de relação que ninguém declarou",
            )
            continue
        reasons.extend(_regras_da_disposicao(item, achado, achado_id))
    return reasons


def _regras_da_disposicao(item: DisposicaoDeAchado, achado: Achado, achado_id: str) -> list[str]:
    """O que cada disposição exige, dada a severidade do achado que ela dispõe.

    Estas são as checagens de **escrituração**, válidas em qualquer estado. O
    que muda entre ``revisada`` e ``validada`` não está aqui: está em
    :func:`_bloqueantes_nao_liberados`.

    A proibição categórica de dispor de um bloqueante foi revista em
    2026-07-30 — ela alcançava as três disposições quando o problema é de uma
    só, e o custo apareceu no próprio documento que a descrevia (o exemplo
    canônico da spec era inválido pelo gate que ela documentava).
    """
    bloqueante = achado.frontmatter.get("severidade") == "bloqueante"
    reasons: list[str] = []

    if bloqueante and item.disposicao == "nao_se_aplica":
        reasons.append(
            f"{achado_id}: achado bloqueante não admite `nao_se_aplica` — a regra acusada não "
            "afirma que o defeito não existe nela; quem corrige a população é o autor do achado",
        )

    if item.disposicao == "corrigida":
        detectado = achado.frontmatter.get("detectado_em")
        detectado_em = detectado if isinstance(detectado, datetime.date) else None
        if detectado_em is not None and item.decidido_em < detectado_em:
            reasons.append(
                f"{achado_id}: `corrigida` em {item.decidido_em.isoformat()}, antes de o achado ser "
                f"detectado em {detectado_em.isoformat()} — não se corrige o que ainda não existia",
            )

    if bloqueante and item.disposicao == "encaminhada" and not (item.decisao_pendente_de or "").strip():
        reasons.append(
            f"{achado_id}: `encaminhada` em achado bloqueante exige `decisao_pendente_de` — "
            "defeito sem dono não é encaminhamento, é arquivamento com outro nome",
        )

    return reasons


def _regras_do_achado(achado: Achado) -> frozenset[str]:
    """Ids de regra que o achado nomeia em ``regras_afetadas``."""
    return frozenset(ref.rsplit("/", 1)[-1].removesuffix(".md") for ref in achado.regras_afetadas)


def _achados_sem_disposicao(regra: Regra, abertos: tuple[Achado, ...]) -> list[str]:
    """Achados abertos que nomeiam a regra e que ela não dispôs — bloqueia ``revisada``.

    Este é o dente do campo, e ele **aperta** o gate em vez de afrouxá-lo.
    Hoje ``revisada`` só olha achado ``bloqueante``, e o catálogo não tem
    nenhum: os achados abertos impõem zero ao estado da auditoria. Com isto,
    avançar exige resposta escrita para **cada** achado aberto que nomeie a
    regra.

    E a recíproca é o que o campo garante: um achado autorado amanhã sobre
    uma regra já ``revisada`` a invalida na hora, até que ela disponha dele
    especificamente. Mesma semântica de rebaixamento não automático do P7 —
    o CI acusa, e um humano decide entre dispor e rebaixar.
    """
    admin = regra.admin
    dispostos: set[str] = set()
    if admin is not None:
        dispostos = {
            item.achado.rsplit("/", 1)[-1].removesuffix(".md") for item in admin.disposicao_de_achados
        }
    pendentes = sorted(
        achado.doc_id
        for achado in abertos
        if regra.doc_id in _regras_do_achado(achado) and achado.doc_id not in dispostos
    )
    if not pendentes:
        return []
    return [f"achado aberto sem disposição: {', '.join(pendentes)}"]


@dataclass(frozen=True)
class _JoinContext:
    """The bundle-wide facts an individual regra's estado is joined against.

    Computed once per check_p7_estados call, not per regra — these are the
    checks that genuinely can't be expressed as single-document Pydantic
    validation, since they depend on the rest of the bundle (achados,
    detections across every regra).
    """

    bloqueante_ids: frozenset[str]
    p2_ids: frozenset[str]
    p1_ids: frozenset[str]
    achados_por_id: dict[str, Achado]
    abertos: tuple[Achado, ...]


def _disposicoes_por_achado(regra: Regra) -> dict[str, DisposicaoDeAchado]:
    """Disposições da regra indexadas pelo id do achado, ou vazio se o contrato não valida."""
    admin = regra.admin
    if admin is None:
        return {}
    return {item.achado.rsplit("/", 1)[-1].removesuffix(".md"): item for item in admin.disposicao_de_achados}


def _bloqueantes_nao_liberados(regra: Regra, context: _JoinContext, estado: str) -> list[str]:
    """Achados bloqueantes abertos que esta regra não liberou **para este estado**.

    É aqui que a trava entre os dois estados vive, e é a razão de a proibição
    categórica ter caído:

    - **sem disposição** o bloqueante impede os dois estados, como antes;
    - **`corrigida`** libera os dois: o defeito não existe mais nesta regra, e
      isso é fato conferível no diff, não juízo sobre a acusação;
    - **`encaminhada`** libera só ``revisada``. A auditoria terminou o que era
      dela — identificou o defeito e registrou de quem é a decisão que falta —
      e é isso que ``revisada`` afirma. ``validada`` afirma outra coisa: que a
      regra pode receber validação institucional, e isso não se dá com defeito
      bloqueante ainda reconhecido como real pela própria regra.

    ``nao_se_aplica`` não aparece aqui porque já é erro de escrituração em
    qualquer estado (:func:`_regras_da_disposicao`).
    """
    if regra.doc_id not in context.bloqueante_ids:
        return []
    disposicoes = _disposicoes_por_achado(regra)
    reasons: list[str] = []
    for achado in context.abertos:
        if achado.frontmatter.get("severidade") != "bloqueante":
            continue
        if regra.doc_id not in _regras_do_achado(achado):
            continue
        item = disposicoes.get(achado.doc_id)
        if item is None:
            reasons.append(f"achado bloqueante aberto sem disposição: {achado.doc_id}")
        elif item.disposicao == "encaminhada" and estado == "validada":
            reasons.append(
                f"{achado.doc_id} está `encaminhada` — libera `revisada`, nunca `validada`: "
                f"a decisão pendente é de {item.decisao_pendente_de!r}",
            )
    return reasons


def _join_reasons(regra: Regra, context: _JoinContext) -> list[str]:
    """Cross-document invariant violations — never expressible as intra-document validation."""
    reasons: list[str] = []
    if regra.doc_id in context.p2_ids:
        reasons.append(f"participa de uma detecção {_P2_DETECTOR_ID} ativa")
    if regra.doc_id in context.p1_ids:
        reasons.append(f"participa de uma detecção {_P1_DETECTOR_ID} ativa")
    return reasons


def check_p7_estados(
    bundle: Bundle,
    detections: list[Detection],
    *,
    today: datetime.date | None = None,
) -> list[Violation]:
    """Camada 1 [bloqueante]: every regra satisfies the invariants of its declared state.

    Pass ``today`` explicitly for deterministic tests; defaults to the real
    current date for normal (CLI) use.
    """
    if today is None:
        today = datetime.datetime.now(tz=datetime.UTC).date()
    context = _JoinContext(
        bloqueante_ids=_open_bloqueante_regra_ids(bundle),
        p2_ids=_detected_regra_ids(detections, _P2_DETECTOR_ID),
        p1_ids=_detected_regra_ids(detections, _P1_DETECTOR_ID),
        achados_por_id={achado.doc_id: achado for achado in bundle.achados},
        abertos=tuple(bundle.open_achados()),
    )

    violations: list[Violation] = []
    # Pertinência, não status: uma regra que o conjunto vigente revogou saiu
    # do catálogo e não participa mais do join; uma regra `inativa` continua
    # tendo `status_auditoria` a validar (RFC 0006 §4).
    for regra in bundle.regras_pertinentes():
        try:
            contrato = RegraAuditoriaContrato.model_validate(regra.frontmatter, context={"today": today})
        except ValidationError as exc:
            violations.append(
                Violation("P7_ESTADO_INVALIDO", f"{regra.doc_id}: {'; '.join(_format_pydantic_errors(exc))}"),
            )
            continue

        estruturais = _disposicao_errors(regra, context.achados_por_id)
        if estruturais:
            violations.append(
                Violation("P7_DISPOSICAO_INVALIDA", f"{regra.doc_id}: {'; '.join(estruturais)}"),
            )

        if contrato.status_auditoria == "importada":
            continue

        reasons = _join_reasons(regra, context)
        reasons.extend(_bloqueantes_nao_liberados(regra, context, contrato.status_auditoria))
        if contrato.status_auditoria in _ESTADOS_COM_TRILHA_OBRIGATORIA:
            reasons.extend(_secoes_p13_1_errors(regra))
            reasons.extend(_achados_sem_disposicao(regra, context.abertos))

        if reasons:
            violations.append(
                Violation(
                    "P7_ESTADO_INVALIDO",
                    f"{regra.doc_id} declara status_auditoria={contrato.status_auditoria!r} mas: "
                    f"{'; '.join(reasons)}",
                ),
            )

    return violations
