"""Unit tests for the camada-3 heuristic detectors (RFC 0001, P1/P9) — synthetic regras.

They assert what each detector reports and, crucially, that every camada-3
detection is informative (``requires_achado=False``) so it never blocks the CI.
"""

from __future__ import annotations

from pathlib import Path

from bundle import Bundle, Regra
from detectors import co_ocorrencias, nome_repetido
from regra_schema import FRONTMATTER_COLUMNS, FRONTMATTER_KEYS


def _regra(
    regra_id: str,
    *,
    nome: str = "Regra padrão",
    status: str = "ativa",
    frontmatter: dict[str, str] | None = None,
    sections: dict[str, str] | None = None,
) -> Regra:
    fm: dict[str, object] = {FRONTMATTER_KEYS[c]: "" for c in FRONTMATTER_COLUMNS}
    fm["nome"] = nome
    fm["status_regra"] = status
    if frontmatter:
        fm.update(frontmatter)
    return Regra(id=regra_id, frontmatter=fm, sections=sections or {})


def _bundle(*regras: Regra) -> Bundle:
    return Bundle(bundle_dir=Path(), regras=tuple(regras), achados=())


# --- P1: nome repetido ---


def test_p1_groups_active_regras_with_the_same_normalized_nome() -> None:
    """Accents/case/whitespace are normalized; a 2+ group is one detection."""
    bundle = _bundle(
        _regra("regra-0001", nome="Pensão por Morte"),
        _regra("regra-0002", nome="pensao  por   morte "),
        _regra("regra-0003", nome="Voluntária"),
    )
    detections = nome_repetido.detect(bundle)
    assert len(detections) == 1
    assert detections[0].regras == frozenset({"regra-0001", "regra-0002"})


def test_p1_is_informative_never_blocking() -> None:
    """P1 detections never require an achado."""
    bundle = _bundle(
        _regra("regra-0001", nome="X"),
        _regra("regra-0002", nome="X"),
    )
    assert all(d.requires_achado is False for d in nome_repetido.detect(bundle))


def test_p1_ignores_inactive_regras() -> None:
    """An inactive member drops out; a lone active name is no group."""
    bundle = _bundle(
        _regra("regra-0001", nome="X", status="ativa"),
        _regra("regra-0002", nome="X", status="inativa"),
    )
    assert nome_repetido.detect(bundle) == []


def test_p1_fingerprint_changes_when_the_shared_nome_changes() -> None:
    """Same regra ids, different shared name: the fingerprint must not be reused."""
    bundle_a = _bundle(_regra("regra-0001", nome="X"), _regra("regra-0002", nome="X"))
    bundle_b = _bundle(_regra("regra-0001", nome="Y"), _regra("regra-0002", nome="Y"))
    fp_a = nome_repetido.detect(bundle_a)[0].fingerprint
    fp_b = nome_repetido.detect(bundle_b)[0].fingerprint
    assert fp_a != fp_b


# --- P9/E5: INTEGRAL=N sem FUNDAMENTACAO_PROPORCIONAL ---


def test_p9_integral_sem_fundamentacao_reports_one_per_regra() -> None:
    """E5: INTEGRAL=N with an empty Fundamentação Proporcional body."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"integral": "N"}, sections={"Fundamentação Proporcional": ""}),
        _regra("regra-0002", frontmatter={"integral": "N"}, sections={"Fundamentação Proporcional": "texto"}),
        _regra("regra-0003", frontmatter={"integral": "S"}, sections={"Fundamentação Proporcional": ""}),
    )
    detections = co_ocorrencias.detect_integral_sem_fundamentacao(bundle)
    assert {r for d in detections for r in d.regras} == {"regra-0001"}
    assert all(d.requires_achado is False for d in detections)


def test_p9_e5_evidencia_carries_the_examined_values() -> None:
    """The reported evidencia isn't just {"regra": id} — it carries what the detector examined."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"integral": "N"}, sections={"Fundamentação Proporcional": ""}),
    )
    detections = co_ocorrencias.detect_integral_sem_fundamentacao(bundle)
    assert len(detections) == 1
    assert detections[0].evidencia == {"integral": "N", "fundamentacao_proporcional": ""}


# --- P9/E3-E4: SEXO vazio + INTEGRAL vazio + TIPO_CALCULO "Não identificado" ---


def test_p9_campos_vazios_requires_all_three_conditions() -> None:
    """E3/E4: only the regra with all three conditions is reported."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "", "integral": "", "tipo_calculo": "Não identificado"}),
        _regra(
            "regra-0002", frontmatter={"sexo": "FEMININO", "integral": "", "tipo_calculo": "Não identificado"}
        ),
    )
    detections = co_ocorrencias.detect_campos_vazios(bundle)
    assert {r for d in detections for r in d.regras} == {"regra-0001"}
    assert all(d.requires_achado is False for d in detections)


def test_p9_e3_e4_evidencia_carries_the_examined_values() -> None:
    """The reported evidencia carries sexo/integral/tipo_calculo, not just the regra id."""
    bundle = _bundle(
        _regra("regra-0001", frontmatter={"sexo": "", "integral": "", "tipo_calculo": "Não identificado"}),
    )
    detections = co_ocorrencias.detect_campos_vazios(bundle)
    assert len(detections) == 1
    assert detections[0].evidencia == {"sexo": "", "integral": "", "tipo_calculo": "Não identificado"}


# --- P9/E7: SEXO x fundamentação ---


def test_p9_sexo_fundamentacao_flags_single_gender_mismatch() -> None:
    """E7: MASCULINO but the fundamentação mentions only 'mulher' (and vice versa)."""
    bundle = _bundle(
        _regra(
            "regra-0001", frontmatter={"sexo": "MASCULINO"}, sections={"Fundamentação": "regra da mulher"}
        ),
        _regra("regra-0002", frontmatter={"sexo": "MASCULINO"}, sections={"Fundamentação": "regra do homem"}),
        _regra("regra-0003", frontmatter={"sexo": "FEMININO"}, sections={"Fundamentação": "regra do homem"}),
    )
    detections = co_ocorrencias.detect_sexo_fundamentacao(bundle)
    assert {r for d in detections for r in d.regras} == {"regra-0001", "regra-0003"}
    assert all(d.requires_achado is False for d in detections)


def test_p9_e7_fingerprint_changes_when_the_premise_flips() -> None:
    """The exact regression the review flagged: same regra id, opposite sexo/mention — must not collide.

    MASCULINO+"only mulher mentioned" and FEMININO+"only homem mentioned" both
    satisfy the same boolean OR condition in detect_sexo_fundamentacao. If the
    fingerprint only depended on regra_id, editing a regra from one case to
    the other would keep the old fingerprint — the CI would treat a reversed
    claim about the regra as "still the same, already-documented" occurrence.
    """
    bundle_masculino = _bundle(
        _regra("regra-0078", frontmatter={"sexo": "MASCULINO"}, sections={"Fundamentação": "da mulher"}),
    )
    bundle_feminino = _bundle(
        _regra("regra-0078", frontmatter={"sexo": "FEMININO"}, sections={"Fundamentação": "do homem"}),
    )
    fp_masculino = co_ocorrencias.detect_sexo_fundamentacao(bundle_masculino)[0].fingerprint
    fp_feminino = co_ocorrencias.detect_sexo_fundamentacao(bundle_feminino)[0].fingerprint
    assert fp_masculino != fp_feminino
