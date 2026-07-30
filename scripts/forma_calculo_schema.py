"""P16 — `type: FormaCalculo`: a fórmula de cálculo do benefício, decomposta.

**Por que este bundle existe.** O `tipo_calculo` do Sisprev **não identifica
fórmulas** — ele mistura três dimensões diferentes no mesmo rótulo. Os nove
valores do catálogo põem lado a lado uma *base* (`Valor Efetivo`, `Valor
Médio`, `Remuneração de Contribuição`), um *ajuste* (`Proporcionalidade Dias`,
`Valor Médio com Redutor da Idade`) e um *limitador* (`Valor Efetivo mais 70%
do que exceder do Teto RGPS`), sem que nenhum deles seja decomponível a partir
do próprio rótulo.

A prova é a `regra-0025`. A conferência do art. 40, § 3º na redação da EC
20/1998 mostrou que a base dela é a **totalidade da remuneração do cargo
efetivo**, reduzida à **proporção do tempo de contribuição** — combinação para a
qual **nenhum rótulo do enum existe**. A regra grava `Não identificado`, o que é
fiel ao estado do Sisprev e falso sobre o estado do conhecimento: a fórmula
jurídica é conhecida e está transcrita.

Daí a inversão que este bundle implementa: **a fórmula é a ontologia, e o enum
do Sisprev é uma projeção dela** — registrada em ``projecao_sisprev`` junto com
a perda que a projeção causa. Modelar um documento por valor do enum
canonizaria a confusão.

Cinco cautelas de desenho, e cada uma tem consequência no código:

1. **Nada é inferido do rótulo legado.** Este módulo **não tem** função que
   mapeie `tipo_calculo` para componentes, e não deve ganhar uma: a decomposição
   é autorada contra os dispositivos, um caso por vez. Um mapeador produziria a
   mesma classe de acusação plausível e não verificada que levou à remoção do
   leitor de citações por regex (RFC 0008).
2. **A regra importada não muda.** Compreender a fórmula não autoriza reescrever
   `tipo_calculo` na `regra-*.md`: a ausência de representação no enum é
   **achado sobre o produto**, não lapso a corrigir.
3. **Uma forma é uma combinação jurídica reutilizável**, não uma regra nem um
   valor do enum. Por isso não há campo apontando para regras, e a cardinalidade
   forma↔regra é livre nas duas direções.
   Pela mesma razão, o vínculo com o dispositivo mora **em cada componente**, e
   não numa lista da forma: o que se afirma é *este* dispositivo funda *esta*
   base, *este* ajuste, *este* limitador. Uma lista global provaria só que as
   fontes existem — nunca qual fundamenta o quê —, e a relação componente →
   dispositivo é justamente o que este bundle existe para registrar (é o
   ``critério → dispositivo`` da RFC 0008 §5 aplicado ao cálculo). A lista da
   forma inteira continua disponível, mas **derivada** (``dispositivos()``,
   união ordenada), nunca autorada em duas pontas.
4. **`paridade` e índice de reajuste ficam fora.** A fórmula descreve o cálculo
   **na concessão**; manutenção do benefício é outro conceito, e misturá-los
   faria o documento responder por duas perguntas com um vocabulário só.
5. **Vocabulário pequeno, extraído dos casos conferidos.** Os enums abaixo têm
   só o que já foi lido em dispositivo transcrito. Combinação nova entra quando
   a conferência que a sustenta for escrita — nunca preventivamente.

O corpo do documento carrega a explicação, a fórmula e, quando houver, código
executável com entradas e saídas descritas. O gate exige **duas** seções
(``# Como calcular`` e ``# Entradas e saídas``) e não exige as outras: uma forma
pode ser corretamente descrita sem implementação, e exigir código produziria
implementação de fachada — o mesmo defeito das quatro seções fixas que o P13.1
abandonou.
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

BODY_HEADINGS = ("Como calcular", "Fórmula", "Entradas e saídas", "Implementação")
_REQUIRED_SECTIONS = ("Como calcular", "Entradas e saídas")

# Vocabulário mínimo, cada termo com o dispositivo conferido que o sustenta.
# Acrescentar termo aqui é ato de autoria que exige a conferência escrita.
BaseTipo = Literal[
    # art. 40, § 3º, CF, red. EC 20/1998: "calculados com base na remuneração
    # do servidor no cargo efetivo (...) corresponderão à totalidade da
    # remuneração"
    "totalidade_remuneracao_cargo_efetivo",
    # art. 40, § 3º, CF, red. EC 41/2003: "serão consideradas as remunerações
    # utilizadas como base para as contribuições"
    "media_remuneracoes_contribuicao",
    # art. 40, § 7º, I, CF, red. EC 41/2003: "ao valor da totalidade dos
    # proventos do servidor falecido"
    "totalidade_proventos_servidor_falecido",
]

AjusteTipo = Literal[
    # art. 40, § 1º, II, CF, red. EC 20/1998: "com proventos proporcionais ao
    # tempo de contribuição"
    "proporcional_tempo_contribuicao",
]

LimitadorTipo = Literal[
    # art. 40, § 7º, CF, red. EC 41/2003: "até o limite máximo estabelecido
    # para os benefícios do regime geral (...), acrescido de setenta por cento
    # da parcela excedente a este limite"
    "teto_rgps_mais_percentual_do_excedente",
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


class ComponenteDeFormula(BaseModel):
    """O que todo componente da fórmula carrega: o seu tipo e o que o funda.

    ``dispositivos`` é obrigatório e não vazio porque um componente sem
    fundamento declarado é exatamente a asserção que este bundle não pode
    fazer — a decomposição vale pela conferência que a sustenta, e é o
    componente, não a forma, que a conferência alcança.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    dispositivos: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def _refs_validas(self) -> ComponenteDeFormula:
        _checar_refs(self.dispositivos, "dispositivos")
        return self


class Base(ComponenteDeFormula):
    """Sobre qual valor o cálculo começa."""

    tipo: BaseTipo


class Ajuste(ComponenteDeFormula):
    """Uma operação aplicada à base. A **ordem da lista é significativa**."""

    tipo: AjusteTipo


class Limitador(ComponenteDeFormula):
    """Piso, teto ou regra de excedente.

    ``percentual_excedente`` existe porque o limitador do art. 40, § 7º não é um
    teto simples: acima do limite do RGPS o benefício continua, a 70% da parcela
    excedente. Um enum sem o número não expressaria a regra — e, por isso mesmo,
    o tipo que depende do número **exige** o número: sem ele o documento diria
    "há excedente" sem dizer quanto, que é menos do que o dispositivo diz.
    """

    tipo: LimitadorTipo
    percentual_excedente: float | None = Field(default=None, ge=0, le=100)

    @model_validator(mode="after")
    def _excedente_exigido(self) -> Limitador:
        if self.tipo == "teto_rgps_mais_percentual_do_excedente" and self.percentual_excedente is None:
            msg = f"tipo={self.tipo!r} exige percentual_excedente"
            raise ValueError(msg)
        return self


class ProjecaoSisprev(BaseModel):
    """Como — e com que perda — a fórmula cabe no ``tipo_calculo`` legado.

    ``justificativa`` é obrigatória sempre que a fidelidade **não** for
    ``exata``: uma perda declarada sem razão escrita é a mesma omissão que
    ``disposicao_de_achados`` existe para impedir do lado da regra.
    """

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
    def _ordem_dos_ajustes(self) -> FormaCalculoFrontmatter:
        tipos = [a.tipo for a in self.ajustes]
        if len(set(tipos)) != len(tipos):
            msg = "ajustes: tipo repetido — a ordem importa, a repetição não é modelada"
            raise ValueError(msg)
        return self

    def componentes(self) -> list[ComponenteDeFormula]:
        """Every component in reading order: base, then ajustes, then limitadores."""
        return [self.base, *self.ajustes, *self.limitadores]

    def dispositivos(self) -> list[str]:
        """Ordered union of every component's ``dispositivos`` — derived, never authored.

        Deduplicated because the same provision legitimately founds more than
        one component (the art. 40, § 1º of a redação can ground both the
        proportion and the base it applies to); order is reading order, so the
        list is stable across loads.
        """
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
    """Load every authored forma from ``bundle_dir``, or none if it doesn't exist.

    A missing directory is not an error: introducing the bundle must never be a
    precondition for the rest of the catalog to validate.
    """
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
