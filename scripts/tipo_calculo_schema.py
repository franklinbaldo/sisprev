"""P17 — ``type: TipoCalculo``: o vocabulário operacional legado do Sisprev.

Um ``TipoCalculo`` registra um valor exato do enum ``tipo_calculo``. Ele não é
uma fórmula jurídica e não autoriza inferir ``base``, ``ajustes`` ou
``limitadores`` a partir do rótulo. A fórmula continua sendo a ontologia de
``type: FormaCalculo``; este bundle documenta somente a linguagem em que o
Sisprev recebe a projeção daquela fórmula.

A completude é bidirecional e derivada de duas fontes já existentes:

- todo valor não vazio observado em ``regra-*.md`` precisa de um conceito;
- todo valor usado em ``FormaCalculo.projecao_sisprev`` precisa de um conceito;
- nenhum conceito pode existir sem ser observado em uma dessas duas pontas.

Assim o bundle não inventa membros do enum, não deixa valores operacionais sem
documentação e não transforma o nome legado numa decomposição normativa.
"""

from __future__ import annotations

import datetime
import re
from functools import cached_property
from pathlib import Path
from typing import Literal

from concept import Concept, ConceptFrontmatter, format_pydantic_errors, parse_concept_doc
from forma_calculo_schema import load_formas_calculo
from pydantic import Field, ValidationError, field_validator

DOC_NAME_RE = re.compile(r"^tipo-calculo-[a-z0-9]+(?:-[a-z0-9]+)*$")
_REQUIRED_SECTIONS = ("Estado da análise",)


class TipoCalculoFrontmatter(ConceptFrontmatter):
    """Contrato do frontmatter de ``type: TipoCalculo``."""

    type: Literal["TipoCalculo"]
    valor: str = Field(min_length=1)
    autorado_por: str = Field(min_length=1)
    autorado_em: datetime.date

    @field_validator("valor")
    @classmethod
    def _valor_exato(cls, valor: str) -> str:
        """Preserve o membro literalmente; espaços laterais criariam outro valor."""
        if not valor.strip():
            msg = "valor não pode ser vazio ou só espaços"
            raise ValueError(msg)
        if valor != valor.strip():
            msg = "valor deve ser o membro exato do enum, sem espaços laterais"
            raise ValueError(msg)
        return valor


class TipoCalculo(Concept):
    """Um membro autorado do vocabulário ``tipo_calculo`` do Sisprev."""

    @cached_property
    def _validation(self) -> TipoCalculoFrontmatter | ValidationError:
        try:
            return TipoCalculoFrontmatter.model_validate(self.frontmatter)
        except ValidationError as exc:
            return exc

    @property
    def contract(self) -> TipoCalculoFrontmatter | None:
        """Return the validated contract, or None when malformed."""
        result = self._validation
        return result if isinstance(result, TipoCalculoFrontmatter) else None

    @property
    def validation_error(self) -> ValidationError | None:
        """Return the caught validation error, or None when valid."""
        result = self._validation
        return result if isinstance(result, ValidationError) else None


def load_tipos_calculo(bundle_dir: Path) -> list[TipoCalculo]:
    """Load every authored ``TipoCalculo``; a missing directory is an empty bundle."""
    if not bundle_dir.is_dir():
        return []
    tipos: list[TipoCalculo] = []
    for path in sorted(bundle_dir.glob("tipo-calculo-*.md")):
        frontmatter, body = parse_concept_doc(path.read_text(encoding="utf-8"))
        tipos.append(
            TipoCalculo(
                doc_id=path.stem,
                frontmatter=frontmatter,
                body=body,
                bundle_dir=bundle_dir,
            )
        )
    return tipos


def valores_tipo_calculo_das_regras(regras_dir: Path) -> frozenset[str]:
    """Return the exact non-empty values recorded in legacy rule frontmatter."""
    if not regras_dir.is_dir():
        return frozenset()
    valores: set[str] = set()
    for path in sorted(regras_dir.glob("regra-*.md")):
        frontmatter, _body = parse_concept_doc(path.read_text(encoding="utf-8"))
        valor = frontmatter.get("tipo_calculo")
        if isinstance(valor, str) and valor:
            valores.add(valor)
    return frozenset(valores)


def valores_tipo_calculo_das_formas(formas_dir: Path) -> frozenset[str]:
    """Return every valid ``FormaCalculo.projecao_sisprev.tipo_calculo`` value."""
    valores: set[str] = set()
    for forma in load_formas_calculo(formas_dir):
        contract = forma.contract
        if contract is not None:
            valores.add(contract.projecao_sisprev.tipo_calculo)
    return frozenset(valores)


def validate_tipo_calculo(tipo: TipoCalculo) -> list[str]:
    """Structural errors of one concept — never a judgement on its semantics."""
    errors: list[str] = []
    if DOC_NAME_RE.fullmatch(tipo.doc_id) is None:
        errors.append(f"{tipo.doc_id}: nome fora do padrão tipo-calculo-<slug>")
    contract = tipo.contract
    if contract is None:
        exc = tipo.validation_error
        if exc is not None:
            errors.extend(format_pydantic_errors(tipo.doc_id, exc))
        else:
            errors.append(f"{tipo.doc_id}: contrato inválido")
        return errors
    if contract.id != tipo.doc_id:
        errors.append(
            f"{tipo.doc_id}: frontmatter id={contract.id!r} discorda do nome do arquivo"
        )
    errors.extend(
        f'{tipo.doc_id}: seção "{heading}" ausente ou vazia'
        for heading in _REQUIRED_SECTIONS
        if not tipo.sections.get(heading, "").strip()
    )
    return errors


def validate_tipos_calculo(
    bundle_dir: Path,
    *,
    valores_observados: frozenset[str] = frozenset(),
    valores_projetados: frozenset[str] = frozenset(),
) -> list[str]:
    """Validate documents and reconcile them with rules and formula projections."""
    tipos = load_tipos_calculo(bundle_dir)
    errors: list[str] = []
    for tipo in tipos:
        errors.extend(validate_tipo_calculo(tipo))

    por_valor: dict[str, list[str]] = {}
    for tipo in tipos:
        contract = tipo.contract
        if contract is not None:
            por_valor.setdefault(contract.valor, []).append(tipo.doc_id)

    errors.extend(
        f"valor {valor!r} repetido em {', '.join(ids)}"
        for valor, ids in sorted(por_valor.items())
        if len(ids) > 1
    )

    valores_autorados = frozenset(por_valor)
    errors.extend(
        f"valor observado nas regras sem concept TipoCalculo: {valor!r}"
        for valor in sorted(valores_observados - valores_autorados)
    )
    errors.extend(
        f"valor projetado por FormaCalculo sem concept TipoCalculo: {valor!r}"
        for valor in sorted(valores_projetados - valores_autorados)
    )

    valores_referenciados = valores_observados | valores_projetados
    errors.extend(
        f"valor autorado sem ocorrência em regra ou projeção de FormaCalculo: {valor!r}"
        for valor in sorted(valores_autorados - valores_referenciados)
    )
    return errors
