"""Unit tests for the P7 state-machine validator — synthetic bundles, no disk."""

from __future__ import annotations

import datetime

from achado_schema import Achado
from bundle import Bundle, Regra
from concept import build_body
from detections import Detection
from estado_auditoria import SECAO_ESTADO_DA_ANALISE, check_p7_estados
from regra_schema import blank_frontmatter

_VALID_ATO = {
    "tipo": "parecer",
    "autoridade": "PGE",
    "identificador": "SEI 123",
    "fonte": "SEI",
}
_TODAY = datetime.date(2026, 7, 17)
_CHECKLIST_FECHADO = {SECAO_ESTADO_DA_ANALISE: "- [x] Critérios conferidos\n- [x] Dispositivos conferidos\n"}

# Frontmatter keys _regra() treats as "unset by default, drop if None" —
# distinguishes a caller explicitly passing None from never mentioning the
# field, matching how the real Regra.status_auditoria/atos_validacao
# properties distinguish an absent key from a present-but-empty one.
_OPTIONAL_FRONTMATTER_KEYS = (
    "atos_validacao",
    "auditado_por",
    "auditado_em",
    "disposicao_de_achados",
)


def _regra(regra_id: str, *, sections: dict[str, str] | None = None, **frontmatter: object) -> Regra:
    fm = blank_frontmatter()
    fm["nome"] = f"Regra {regra_id}"
    fm["status_auditoria"] = frontmatter.pop("status_auditoria", "importada")
    for key in _OPTIONAL_FRONTMATTER_KEYS:
        value = frontmatter.pop(key, None)
        if value is not None:
            fm[key] = value
    return Regra(doc_id=regra_id, frontmatter=fm, body=build_body(sections or {}))


def _regra_revisada(regra_id: str, *, sections: dict[str, str] | None = None, **overrides: object) -> Regra:
    """A regra with a complete, valid audit trail — the baseline "clean revisada" fixture."""
    defaults: dict[str, object] = {
        "status_auditoria": "revisada",
        "auditado_por": "franklinbaldo",
        "auditado_em": "2026-07-16",
    }
    defaults.update(overrides)
    return _regra(
        regra_id, sections=sections if sections is not None else dict(_CHECKLIST_FECHADO), **defaults
    )


def _bloqueante_achado(doc_id: str, regra_id: str) -> Achado:
    return Achado(
        doc_id=doc_id,
        frontmatter={
            "situacao": "aberto",
            "severidade": "bloqueante",
            "regras_afetadas": [f"/regras/{regra_id}.md"],
        },
    )


def _detection(detector: str, *regra_ids: str) -> Detection:
    return Detection(detector=detector, fingerprint=f"sha256:{'a' * 64}", regras=frozenset(regra_ids))


def _regra_validada(regra_id: str, *, sections: dict[str, str] | None = None, **overrides: object) -> Regra:
    """A regra with a complete, valid audit trail and a well-formed ato — the "clean validada" fixture."""
    defaults: dict[str, object] = {
        "status_auditoria": "validada",
        "atos_validacao": [_VALID_ATO],
        "auditado_por": "franklinbaldo",
        "auditado_em": "2026-07-16",
    }
    defaults.update(overrides)
    return _regra(
        regra_id, sections=sections if sections is not None else dict(_CHECKLIST_FECHADO), **defaults
    )


def _bundle(regras: list[Regra], achados: list[Achado] | None = None) -> Bundle:
    return Bundle(regras=tuple(regras), achados=tuple(achados or []))


def test_importada_has_no_invariants_to_violate() -> None:
    """A regra still importada is never flagged, regardless of achados/detections."""
    regra = _regra("regra-0001")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


# --- P8: status_auditoria is a closed enum ---


def test_unknown_status_auditoria_value_is_rejected() -> None:
    """A typo like "revisad" must not silently behave like "revisada"."""
    regra = _regra("regra-0001", status_auditoria="revisad")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "status_auditoria" in violations[0].message


def test_arbitrary_string_status_auditoria_is_rejected() -> None:
    """Any value outside the three closed states is rejected, not just near-misses of real values."""
    regra = _regra("regra-0001", status_auditoria="foo")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert violations[0].code == "P7_ESTADO_INVALIDO"


# --- revisada: joins with achados/detectors ---


def test_revisada_with_no_blockers_is_valid() -> None:
    """A revisada regra with a complete trail and nothing referencing it is clean."""
    bundle = _bundle([_regra_revisada("regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_revisada_flagged_by_open_bloqueante_achado() -> None:
    """A revisada regra referenced by an open bloqueante achado is invalid."""
    regra = _regra_revisada("regra-0001")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert violations[0].code == "P7_ESTADO_INVALIDO"
    assert "bloqueante aberto" in violations[0].message


def test_revisada_requires_a_disposicao_for_an_open_informativo_achado() -> None:
    """Contrato invertido (2026-07-29), e a inversão é o ponto.

    A versão anterior deste teste afirmava que um achado `informativo` nunca
    invalidava `revisada`. Como o catálogo não tem nenhum `bloqueante`, isso
    significava que os 50 achados abertos impunham **zero** ao estado da
    auditoria — uma regra podia atravessar o gate com quatro achados abertos
    sobre ela e nada escrito sobre nenhum.

    Agora cada achado aberto que nomeie a regra exige disposição própria,
    com justificativa e trilha. O `informativo` deixou de ser silencioso
    sem virar `bloqueante`: ele não impede, mas exige resposta.
    """
    regra = _regra_revisada("regra-0001")
    achado = Achado(
        doc_id="achado-0001",
        frontmatter={
            "situacao": "aberto",
            "severidade": "informativo",
            "regras_afetadas": ["/regras/regra-0001.md"],
        },
    )
    bundle = _bundle([regra], [achado])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_ESTADO_INVALIDO"]

    disposta = _regra_revisada(
        "regra-0001",
        disposicao_de_achados=[
            {
                "achado": "/achados/achado-0001.md",
                "disposicao": "nao_impede",
                "justificativa": "Campo deployável: decisão do dono, não da auditoria.",
                "decidido_por": "franklinbaldo",
                "decidido_em": "2026-07-16",
            }
        ],
    )
    assert check_p7_estados(_bundle([disposta], [achado]), [], today=_TODAY) == []


def test_revisada_flagged_by_active_p2_detection() -> None:
    """A revisada regra still part of a P2 material-equality group is invalid."""
    bundle = _bundle([_regra_revisada("regra-0001")])
    detections = [_detection("P2_IGUALDADE_MATERIAL_ATIVA", "regra-0001", "regra-0002")]
    violations = check_p7_estados(bundle, detections, today=_TODAY)
    assert len(violations) == 1
    assert "P2_IGUALDADE_MATERIAL_ATIVA" in violations[0].message


def test_revisada_flagged_by_active_p1_detection() -> None:
    """A revisada regra still sharing a normalized nome is invalid (P1: unicidade como meta)."""
    bundle = _bundle([_regra_revisada("regra-0001")])
    detections = [_detection("P1_NOME_REPETIDO", "regra-0001", "regra-0002")]
    violations = check_p7_estados(bundle, detections, today=_TODAY)
    assert len(violations) == 1
    assert "P1_NOME_REPETIDO" in violations[0].message


# --- P11: revisada/validada require a real auditor and date ---


def test_revisada_requires_auditado_por() -> None:
    """A revisada regra without an author leaves no audit trail."""
    regra = _regra_revisada("regra-0001", auditado_por=None)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "auditado_por" in violations[0].message


def test_revisada_requires_auditado_em() -> None:
    """A revisada regra without a date leaves no audit trail."""
    regra = _regra_revisada("regra-0001", auditado_em=None)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "auditado_em" in violations[0].message


def test_revisada_rejects_a_non_iso_auditado_em() -> None:
    """A malformed date string is not silently accepted."""
    regra = _regra_revisada("regra-0001", auditado_em="17/07/2026")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "auditado_em" in violations[0].message


def test_revisada_rejects_a_future_auditado_em() -> None:
    """A revisão cannot be dated after today — that would predate the event."""
    regra = _regra_revisada("regra-0001", auditado_em="2026-07-18")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "está no futuro" in violations[0].message


def test_revisada_accepts_auditado_em_equal_to_today() -> None:
    """Today itself is a valid, non-future date."""
    regra = _regra_revisada("regra-0001", auditado_em="2026-07-17")
    bundle = _bundle([regra])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


# --- P13.1: revisada requires the four boundary-of-automation sections ---


def test_revisada_with_no_sections_at_all_is_invalid() -> None:
    """auditado_por/auditado_em alone are not enough — the exact gap the review flagged."""
    regra = _regra_revisada("regra-0001", sections={})
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert SECAO_ESTADO_DA_ANALISE in violations[0].message


def test_revisada_with_a_blank_section_is_invalid() -> None:
    """A present-but-whitespace-only section doesn't count as an answer."""
    regra = _regra_revisada("regra-0001", sections={SECAO_ESTADO_DA_ANALISE: "   "})
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "não vazia" in violations[0].message


def test_revisada_with_an_unticked_item_is_invalid() -> None:
    """The whole point of the checklist: an open box blocks revisada.

    This is what the four fixed headings could not do — they passed on the
    literal text "TODO", certifying a shape rather than any analysis.
    """
    sections = {SECAO_ESTADO_DA_ANALISE: "- [x] Critérios conferidos\n- [ ] Causa da incapacidade (Q6)\n"}
    regra = _regra_revisada("regra-0001", sections=sections)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "1 item aberto" in violations[0].message


def test_the_violation_counts_every_open_item_not_just_the_first() -> None:
    """Two open boxes report as two — the auditor sees how much is left."""
    sections = {SECAO_ESTADO_DA_ANALISE: "- [ ] Um\n- [x] Dois\n* [ ] Três\n"}
    regra = _regra_revisada("regra-0001", sections=sections)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert "2 itens abertos" in violations[0].message


def test_uppercase_x_counts_as_ticked() -> None:
    """`- [X]` is GitHub-valid and must not read as open."""
    regra = _regra_revisada("regra-0001", sections={SECAO_ESTADO_DA_ANALISE: "- [X] Feito\n"})
    bundle = _bundle([regra])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_prose_without_any_checklist_item_is_invalid() -> None:
    """Free text alone rebuilds the hole: it asserts nothing checkable."""
    sections = {SECAO_ESTADO_DA_ANALISE: "Analisei tudo, está certo."}
    regra = _regra_revisada("regra-0001", sections=sections)
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "ao menos um item" in violations[0].message


def test_prose_around_a_closed_checklist_is_fine() -> None:
    """The section is free-form: commentary is welcome, the boxes are the gate."""
    sections = {
        SECAO_ESTADO_DA_ANALISE: (
            "Esta regra é a face integral do par com a 0007.\n\n- [x] Critérios conferidos\n"
        )
    }
    regra = _regra_revisada("regra-0001", sections=sections)
    bundle = _bundle([regra])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_a_malformed_box_is_prose_not_a_checklist_item() -> None:
    """`- [TODO]` must not satisfy the gate — it is a placeholder wearing a checkbox.

    Regression: existence was tested with `"- [" in corpo`, so `- [TODO]`,
    `- [abc` and an inline `texto - [ qualquer coisa` all passed while no
    open box matched. That let exactly the placeholder the four fixed
    headings used to admit back in, only spelled differently.
    """
    for corpo in ("- [TODO] conferir critérios", "- [abc", "texto - [ qualquer coisa"):
        regra = _regra_revisada("regra-0001", sections={SECAO_ESTADO_DA_ANALISE: corpo})
        violations = check_p7_estados(_bundle([regra]), [], today=_TODAY)
        assert len(violations) == 1, corpo
        assert "ao menos um item" in violations[0].message, corpo


def test_a_closed_box_must_be_line_initial() -> None:
    """An inline `- [x]` inside prose is not an item — the marker anchors the line."""
    sections = {SECAO_ESTADO_DA_ANALISE: "conferi tudo - [x] mesmo"}
    regra = _regra_revisada("regra-0001", sections=sections)
    violations = check_p7_estados(_bundle([regra]), [], today=_TODAY)
    assert len(violations) == 1
    assert "ao menos um item" in violations[0].message


def test_asterisk_marker_and_indentation_are_accepted() -> None:
    """`*` is as valid a list marker as `-`, and nested items still count."""
    sections = {SECAO_ESTADO_DA_ANALISE: "* [x] um\n  - [x] dois aninhado\n"}
    regra = _regra_revisada("regra-0001", sections=sections)
    assert check_p7_estados(_bundle([regra]), [], today=_TODAY) == []


def test_validada_also_requires_the_p13_1_sections() -> None:
    """Validada inherits the section requirement from revisada, like every other P11/P13.1 check."""
    regra = _regra_validada("regra-0001", sections={})
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert SECAO_ESTADO_DA_ANALISE in violations[0].message


# --- validada: atos_validacao ---


def test_validada_requires_atos_validacao() -> None:
    """Validada without any atos_validacao is invalid."""
    regra = _regra_validada("regra-0001", atos_validacao=[])
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "atos_validacao" in violations[0].message


def test_validada_with_a_complete_ato_is_valid() -> None:
    """Validada with one well-formed ato, a complete trail and no other blockers is clean."""
    bundle = _bundle([_regra_validada("regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_validada_rejects_ato_missing_required_fields() -> None:
    """Each ato de validação must declare tipo/autoridade/identificador/fonte."""
    incomplete_ato = {"tipo": "parecer", "autoridade": "PGE"}
    regra = _regra_validada("regra-0001", atos_validacao=[incomplete_ato])
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "identificador" in violations[0].message
    assert "fonte" in violations[0].message


def test_validada_rejects_a_non_list_atos_validacao() -> None:
    """A malformed atos_validacao (wrong type entirely) is a violation, not a silent empty list."""
    regra = _regra_validada("regra-0001", atos_validacao="texto-malformado")
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "atos_validacao" in violations[0].message
    assert "texto-malformado" in violations[0].message


def test_validada_rejects_a_non_mapping_item_without_dropping_it_silently() -> None:
    """A mixed list (one valid ato + one malformed string) must surface the malformed item.

    This is the exact scenario the review flagged: a property that
    pre-filters to "only the dict items" would let this list quietly become
    [valid_ato] and pass — the malformed entry must be reported instead.
    """
    regra = _regra_validada("regra-0001", atos_validacao=[_VALID_ATO, "texto-malformado"])
    bundle = _bundle([regra])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "atos_validacao" in violations[0].message
    assert "texto-malformado" in violations[0].message


def test_validada_also_inherits_revisada_invariants() -> None:
    """Validada is not exempt from the revisada checks (open bloqueante achado still counts)."""
    regra = _regra_validada("regra-0001")
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert len(violations) == 1
    assert "bloqueante aberto" in violations[0].message


# --- disposicao_de_achados: cada regra dispõe de cada achado que a nomeia ---


def _informativo_achado(doc_id: str, *regra_ids: str) -> Achado:
    return Achado(
        doc_id=doc_id,
        frontmatter={
            "situacao": "aberto",
            "severidade": "informativo",
            "regras_afetadas": [f"/regras/{rid}.md" for rid in regra_ids],
        },
    )


def _disposicao(achado_id: str, disposicao: str = "nao_impede", **overrides: object) -> dict[str, object]:
    entry: dict[str, object] = {
        "achado": f"/achados/{achado_id}.md",
        "disposicao": disposicao,
        "justificativa": "Defeito real, e o que resta é decisão do dono do campo.",
        "decidido_por": "franklinbaldo",
        "decidido_em": "2026-07-16",
    }
    entry.update(overrides)
    return entry


def test_open_informativo_achado_without_disposicao_blocks_revisada() -> None:
    """O dente do campo: antes disto um achado informativo não impunha nada a `revisada`."""
    regra = _regra_revisada("regra-0001")
    bundle = _bundle([regra], [_informativo_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_ESTADO_INVALIDO"]
    assert "achado aberto sem disposição: achado-0001" in violations[0].message


def test_disposicao_unblocks_revisada() -> None:
    """Disposta com justificativa e trilha, a regra avança carregando o defeito conhecido."""
    regra = _regra_revisada("regra-0001", disposicao_de_achados=[_disposicao("achado-0001")])
    bundle = _bundle([regra], [_informativo_achado("achado-0001", "regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_disposicao_decidida_no_futuro_e_rejeitada() -> None:
    """`decidido_em` posterior a hoje é a "data impossível" que o gate prometia e não checava.

    Mesma exigência que o P11 faz de `auditado_em`: decisão datada no futuro é
    decisão que ninguém tomou. Vale numa entrada cuja função é justamente fazer
    a regra avançar carregando um defeito conhecido, então a trilha é o que
    sobra para responder por ela.
    """
    regra = _regra_revisada(
        "regra-0001",
        disposicao_de_achados=[_disposicao("achado-0001", decidido_em="2027-01-01")],
    )
    bundle = _bundle([regra], [_informativo_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_DISPOSICAO_INVALIDA"]
    assert "decidido_em=2027-01-01 está no futuro" in violations[0].message


def test_disposicao_decidida_hoje_e_aceita() -> None:
    """A fronteira é `> hoje`: decidir hoje é decidir, não é datar no futuro."""
    regra = _regra_revisada(
        "regra-0001",
        disposicao_de_achados=[_disposicao("achado-0001", decidido_em=_TODAY.isoformat())],
    )
    bundle = _bundle([regra], [_informativo_achado("achado-0001", "regra-0001")])
    assert check_p7_estados(bundle, [], today=_TODAY) == []


def test_a_new_achado_re_blocks_an_already_revisada_regra() -> None:
    """Achado novo sobre regra já revisada a invalida até ser disposto especificamente."""
    regra = _regra_revisada("regra-0001", disposicao_de_achados=[_disposicao("achado-0001")])
    bundle = _bundle(
        [regra],
        [_informativo_achado("achado-0001", "regra-0001"), _informativo_achado("achado-0002", "regra-0001")],
    )
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_ESTADO_INVALIDO"]
    assert "achado-0002" in violations[0].message
    assert "achado-0001" not in violations[0].message


def test_disposicao_is_per_regra_not_per_achado() -> None:
    """Um achado sobre duas regras: dispor numa não libera a outra."""
    disposta = _regra_revisada("regra-0001", disposicao_de_achados=[_disposicao("achado-0001")])
    pendente = _regra_revisada("regra-0002")
    bundle = _bundle([disposta, pendente], [_informativo_achado("achado-0001", "regra-0001", "regra-0002")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_ESTADO_INVALIDO"]
    assert violations[0].message.startswith("regra-0002")


def test_disposicao_of_an_achado_that_does_not_name_the_regra_is_rejected() -> None:
    """A reconciliação: sem ela o campo seria a segunda ponta declarando a relação."""
    regra = _regra("regra-0001", disposicao_de_achados=[_disposicao("achado-0001")])
    bundle = _bundle([regra], [_informativo_achado("achado-0001", "regra-0002")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_DISPOSICAO_INVALIDA"]
    assert "não nomeia esta regra" in violations[0].message


def test_disposicao_of_a_nonexistent_achado_is_rejected() -> None:
    """Referência a achado que não existe é escrituração inválida, não silêncio."""
    regra = _regra("regra-0001", disposicao_de_achados=[_disposicao("achado-9999")])
    bundle = _bundle([regra], [])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_DISPOSICAO_INVALIDA"]
    assert "não existe" in violations[0].message


def test_bloqueante_achado_is_not_disposable_by_the_regra() -> None:
    """Dispor de um bloqueante derrotaria a severidade por escrito na regra acusada."""
    regra = _regra("regra-0001", disposicao_de_achados=[_disposicao("achado-0001")])
    bundle = _bundle([regra], [_bloqueante_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_DISPOSICAO_INVALIDA"]
    assert "bloqueante" in violations[0].message


def test_the_same_achado_disposed_twice_is_rejected() -> None:
    """Duas disposições do mesmo achado poderiam divergir sem gate que as reconcilie."""
    regra = _regra(
        "regra-0001", disposicao_de_achados=[_disposicao("achado-0001"), _disposicao("achado-0001")]
    )
    bundle = _bundle([regra], [_informativo_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_DISPOSICAO_INVALIDA"]
    assert "mais de uma vez" in violations[0].message


def test_disposicao_structure_is_checked_even_on_importada() -> None:
    """Escrituração malformada é defeito agora, não na hora da transição."""
    regra = _regra("regra-0001", disposicao_de_achados=[_disposicao("achado-9999")])
    assert check_p7_estados(_bundle([regra]), [], today=_TODAY) != []


def test_disposicao_without_justificativa_is_rejected_by_the_contract() -> None:
    """Sem justificativa não há disposição — "ignorado" é omissão com lugar para morar."""
    regra = _regra("regra-0001", disposicao_de_achados=[_disposicao("achado-0001", justificativa="  ")])
    bundle = _bundle([regra], [_informativo_achado("achado-0001", "regra-0001")])
    violations = check_p7_estados(bundle, [], today=_TODAY)
    assert [v.code for v in violations] == ["P7_DISPOSICAO_INVALIDA"]
    assert "justificativa" in violations[0].message
