"""P16 — `type: FormaCalculo`: a fórmula de cálculo do benefício, decomposta.

**Por que este bundle existe.** O `tipo_calculo` do Sisprev **não identifica
fórmulas** — ele mistura dimensões diferentes no mesmo rótulo. Os valores do
catálogo põem lado a lado bases (`Valor Efetivo`, `Valor Médio`), ajustes
(`Proporcionalidade Dias`, `Valor Médio com Redutor da Idade`) e pacotes
operacionais (`Tipo Cálculo Nova Previdência`), sem que nenhum deles seja
seguramente decomponível a partir do próprio nome.

A prova inicial foi a `regra-0025`: a fórmula jurídica é a totalidade da
remuneração do cargo efetivo reduzida proporcionalmente ao tempo de
contribuição, combinação para a qual nenhum rótulo legado existe. A regra grava
`Não identificado`, valor fiel ao estado do Sisprev e não ao estado do
conhecimento jurídico.

Daí a inversão: **a fórmula é a ontologia, e o enum do Sisprev é uma projeção
dela** — registrada em ``projecao_sisprev`` junto com a perda causada pela
projeção. Modelar um documento por valor do enum canonizaria a confusão.

Seis cautelas de desenho:

1. **Nada é inferido do rótulo legado.** A decomposição é autorada contra os
   dispositivos, uma combinação por vez.
2. **A regra importada não muda.** Compreender a fórmula não autoriza reescrever
   `tipo_calculo`; ausência de representação é achado sobre o produto.
3. **Uma forma é combinação jurídica reutilizável**, não regra nem valor do
   enum. A cardinalidade forma↔regra é livre nas duas direções.
4. **O vínculo é componente → dispositivo.** A lista da forma inteira é
   derivada por ``dispositivos()``, nunca autorada em duas pontas.
5. **A ordem das operações é explícita.** A LCE 432/2008, art. 17, § 1º, e a
   LCE 1.100/2021, art. 26, § 1º, mandam aplicar o teto da remuneração antes da
   proporcionalidade. Separar ajustes e limitadores sem uma ordem comum
   inverteria juridicamente essas fórmulas.
6. **`paridade` e índice de reajuste ficam fora.** A forma descreve o cálculo na
   concessão; manutenção do benefício é outro conceito.

O corpo exige ``# Como calcular`` e ``# Entradas e saídas``. Fórmula simbólica e
implementação são opcionais: exigi-las produziria código ou álgebra de fachada
quando a fonte ainda não fechou todos os parâmetros.
"""

from __future__ import annotations

import datetime
import re
from functools import cached_property
from typing import TYPE_CHECKING, Literal

from concept import Concept, ConceptFrontmatter, format_pydantic_errors, parse_concept_doc
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

if TYPE_CHECKING:
    from pathlib import Path

DOC_NAME_RE = re.compile(r"^forma-calculo-[a-z0-9]+(?:-[a-z0-9]+)*$")
DISPOSITIVO_REF_RE = re.compile(r"^/dispositivos/[a-z0-9-]+/[a-z0-9-]+/[a-z0-9-]+\.md$")
COMPETENCIA_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")

BODY_HEADINGS = ("Como calcular", "Fórmula", "Entradas e saídas", "Implementação")
_REQUIRED_SECTIONS = ("Como calcular", "Entradas e saídas")

# Vocabulário pequeno: cada termo entrou com uma conferência escrita contra
# dispositivo transcrito. Termo novo não entra preventivamente.
BaseTipo = Literal[
    "totalidade_remuneracao_cargo_efetivo",
    "media_remuneracoes_contribuicao",
    "totalidade_proventos_servidor_falecido",
    "proventos_aposentadoria_ou_incapacidade_hipotetica",
]

AjusteTipo = Literal[
    "proporcional_tempo_contribuicao",
    "redutor_idade_por_ano_antecipado",
    "cota_familiar_por_dependente",
    "rateio_igual_dependentes",
]

LimitadorTipo = Literal[
    "teto_rgps_mais_percentual_do_excedente",
    "teto_remuneracao_cargo_efetivo",
]

Fidelidade = Literal["exata", "parcial", "sem_representacao", "pendente"]


def _checar_refs(refs: list[str], campo: str) -> None:
    """Raise unless every ref is a well-formed, non-repeated dispositivo link."""
    for ref in refs:
        if DISPOSITIVO_REF_RE.fullmatch(ref) is None:
            msg = f"{campo}: {ref!r} não é link OKF de dispositivo"
            raise ValueError(msg)
    if len(set(refs)) != len(refs):
        msg = f"{campo}: referência repetida"
        raise ValueError(msg)


def _campos_presentes(modelo: BaseModel, nomes: tuple[str, ...]) -> set[str]:
    """Return parameter names whose value is not None."""
    return {nome for nome in nomes if getattr(modelo, nome) is not None}


class ComponenteDeFormula(BaseModel):
    """Componente com proveniência própria."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    dispositivos: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def _refs_validas(self) -> ComponenteDeFormula:
        _checar_refs(self.dispositivos, "dispositivos")
        return self


class Base(ComponenteDeFormula):
    """Valor sobre o qual as operações começam."""

    tipo: BaseTipo
    percentual_periodo: float | None = Field(default=None, gt=0, le=100)
    competencia_inicial: str | None = None

    @model_validator(mode="after")
    def _parametros_da_media(self) -> Base:
        parametros = ("percentual_periodo", "competencia_inicial")
        presentes = _campos_presentes(self, parametros)
        if self.tipo == "media_remuneracoes_contribuicao":
            faltantes = set(parametros) - presentes
            if faltantes:
                msg = f"tipo={self.tipo!r} exige {', '.join(sorted(faltantes))}"
                raise ValueError(msg)
            if self.competencia_inicial is None or COMPETENCIA_RE.fullmatch(self.competencia_inicial) is None:
                msg = "competencia_inicial deve usar YYYY-MM"
                raise ValueError(msg)
        elif presentes:
            msg = f"tipo={self.tipo!r} não aceita parâmetros de média: {', '.join(sorted(presentes))}"
            raise ValueError(msg)
        return self


class Operacao(ComponenteDeFormula):
    """Componente aplicado à base numa posição explícita da sequência."""

    ordem: int = Field(ge=1)


class Ajuste(Operacao):
    """Transformação aplicada ao resultado da operação anterior."""

    tipo: AjusteTipo
    percentual_ate_marco: float | None = Field(default=None, ge=0, le=100)
    percentual_a_partir_marco: float | None = Field(default=None, ge=0, le=100)
    marco_alteracao: datetime.date | None = None
    percentual_base: float | None = Field(default=None, ge=0, le=100)
    percentual_por_dependente: float | None = Field(default=None, ge=0, le=100)
    percentual_maximo: float | None = Field(default=None, ge=0, le=100)

    @model_validator(mode="after")
    def _parametros_do_ajuste(self) -> Ajuste:
        redutor = ("percentual_ate_marco", "percentual_a_partir_marco", "marco_alteracao")
        cotas = ("percentual_base", "percentual_por_dependente", "percentual_maximo")
        presentes_redutor = _campos_presentes(self, redutor)
        presentes_cotas = _campos_presentes(self, cotas)

        if self.tipo == "redutor_idade_por_ano_antecipado":
            faltantes = set(redutor) - presentes_redutor
            if faltantes:
                msg = f"tipo={self.tipo!r} exige {', '.join(sorted(faltantes))}"
                raise ValueError(msg)
            if presentes_cotas:
                msg = f"tipo={self.tipo!r} não aceita parâmetros de cotas"
                raise ValueError(msg)
        elif self.tipo == "cota_familiar_por_dependente":
            faltantes = set(cotas) - presentes_cotas
            if faltantes:
                msg = f"tipo={self.tipo!r} exige {', '.join(sorted(faltantes))}"
                raise ValueError(msg)
            if presentes_redutor:
                msg = f"tipo={self.tipo!r} não aceita parâmetros de redutor"
                raise ValueError(msg)
            if self.percentual_base is not None and self.percentual_maximo is not None:
                if self.percentual_base > self.percentual_maximo:
                    msg = "percentual_base não pode superar percentual_maximo"
                    raise ValueError(msg)
        elif presentes_redutor or presentes_cotas:
            msg = f"tipo={self.tipo!r} não aceita parâmetros adicionais"
            raise ValueError(msg)
        return self


class Limitador(Operacao):
    """Teto ou regra de tratamento da parcela excedente."""

    tipo: LimitadorTipo
    percentual_excedente: float | None = Field(default=None, ge=0, le=100)

    @model_validator(mode="after")
    def _parametros_do_limitador(self) -> Limitador:
        if self.tipo == "teto_rgps_mais_percentual_do_excedente":
            if self.percentual_excedente is None:
                msg = f"tipo={self.tipo!r} exige percentual_excedente"
                raise ValueError(msg)
        elif self.percentual_excedente is not None:
            msg = f"tipo={self.tipo!r} não aceita percentual_excedente"
            raise ValueError(msg)
        return self


class ProjecaoSisprev(BaseModel):
    """Como — e com que perda — a fórmula cabe no ``tipo_calculo`` legado."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    tipo_calculo: str = Field(min_length=1)
    fidelidade: Fidelidade
    justificativa: str | None = None

    @model_validator(mode="after")
    def _perda_exige_justificativa(self) -> ProjecaoSisprev:
        if self.fidelidade != "exata" and not (self.justificativa or "").strip():
            msg = f"fidelidade={self.fidelidade!r} exige justificativa não vazia"
            raise ValueError(msg)
        return self


class FormaCalculoFrontmatter(ConceptFrontmatter):
    """Contrato do frontmatter de ``type: FormaCalculo``."""

    type: Literal["FormaCalculo"]
    nome: str = Field(min_length=1)
    base: Base
    ajustes: list[Ajuste] = Field(default_factory=list)
    limitadores: list[Limitador] = Field(default_factory=list)
    projecao_sisprev: ProjecaoSisprev
    autorado_por: str = Field(min_length=1)
    autorado_em: datetime.date

    @model_validator(mode="after")
    def _operacoes_coerentes(self) -> FormaCalculoFrontmatter:
        tipos_ajustes = [ajuste.tipo for ajuste in self.ajustes]
        if len(set(tipos_ajustes)) != len(tipos_ajustes):
            msg = "ajustes: tipo repetido — repetição não é modelada"
            raise ValueError(msg)

        tipos_limitadores = [limitador.tipo for limitador in self.limitadores]
        if len(set(tipos_limitadores)) != len(tipos_limitadores):
            msg = "limitadores: tipo repetido — repetição não é modelada"
            raise ValueError(msg)

        ordens = [operacao.ordem for operacao in self.operacoes()]
        if len(set(ordens)) != len(ordens):
            msg = "operações: ordem repetida"
            raise ValueError(msg)
        esperadas = list(range(1, len(ordens) + 1))
        if sorted(ordens) != esperadas:
            msg = f"operações: ordem deve cobrir {esperadas}, recebido {sorted(ordens)}"
            raise ValueError(msg)
        return self

    def operacoes(self) -> list[Operacao]:
        """Return adjustments and limiters ordered by their explicit position."""
        return sorted([*self.ajustes, *self.limitadores], key=lambda operacao: operacao.ordem)

    def componentes(self) -> list[ComponenteDeFormula]:
        """Return the base followed by the legally ordered operations."""
        return [self.base, *self.operacoes()]

    def dispositivos(self) -> list[str]:
        """Ordered, deduplicated union of every component's device links."""
        vistos: dict[str, None] = {}
        for componente in self.componentes():
            for ref in componente.dispositivos:
                vistos.setdefault(ref, None)
        return list(vistos)


class FormaCalculo(Concept):
    """Uma forma de cálculo autorada (P16)."""

    @cached_property
    def _validation(self) -> FormaCalculoFrontmatter | ValidationError:
        try:
            return FormaCalculoFrontmatter.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def contract(self) -> FormaCalculoFrontmatter | None:
        """Return the validated contract, or None when the frontmatter is malformed."""
        result = self._validation
        return result if isinstance(result, FormaCalculoFrontmatter) else None

    @property
    def validation_error(self) -> ValidationError | None:
        """Return the caught error when the frontmatter is malformed, or None."""
        result = self._validation
        return result if isinstance(result, ValidationError) else None


def load_formas_calculo(bundle_dir: Path) -> list[FormaCalculo]:
    """Load every authored forma from ``bundle_dir``, or none if it doesn't exist."""
    if not bundle_dir.is_dir():
        return []
    formas = []
    for path in sorted(bundle_dir.glob("forma-calculo-*.md")):
        frontmatter, body = parse_concept_doc(path.read_text(encoding="utf-8"))
        formas.append(FormaCalculo(doc_id=path.stem, frontmatter=frontmatter, body=body))
    return formas


def validate_forma_calculo(forma: FormaCalculo, dispositivo_ids: frozenset[str]) -> list[str]:
    """Structural errors of one forma — never a judgement on the formula's merit."""
    errors: list[str] = []
    if DOC_NAME_RE.fullmatch(forma.doc_id) is None:
        errors.append(f"{forma.doc_id}: nome de arquivo fora do padrão forma-calculo-<slug>")
    contract = forma.contract
    if contract is None:
        exc = forma.validation_error
        if exc is not None:
            errors.extend(format_pydantic_errors(forma.doc_id, exc))
        else:
            errors.append(f"{forma.doc_id}: contrato inválido")
        return errors
    if contract.id != forma.doc_id:
        errors.append(f"{forma.doc_id}: frontmatter id={contract.id!r} discorda do nome do arquivo")
    for ref in contract.dispositivos():
        alvo = ref.removeprefix("/dispositivos/").removesuffix(".md")
        if alvo not in dispositivo_ids:
            errors.append(f"{forma.doc_id}: dispositivo {alvo!r} não existe no bundle")
    errors.extend(
        f'{forma.doc_id}: seção "{heading}" ausente ou vazia'
        for heading in _REQUIRED_SECTIONS
        if not forma.sections.get(heading, "").strip()
    )
    return errors


def validate_formas_calculo(bundle_dir: Path, dispositivo_ids: frozenset[str]) -> list[str]:
    """Every forma's structural errors, plus id uniqueness across the bundle."""
    formas = load_formas_calculo(bundle_dir)
    errors: list[str] = []
    for forma in formas:
        errors.extend(validate_forma_calculo(forma, dispositivo_ids))
    vistos: dict[str, int] = {}
    for forma in formas:
        vistos[forma.doc_id] = vistos.get(forma.doc_id, 0) + 1
    errors.extend(f"{doc_id}: id repetido no bundle" for doc_id, n in vistos.items() if n > 1)
    return errors
