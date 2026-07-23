"""RFC 0004 §7 — requisitos de verificação humana: synthetic fixtures, five parts never confused.

Covers the shape of ``protocolo_verificacao`` (never a concrete constatação,
Q6-S) and the compiler's fundamentação template (RFC 0004 §6: describes the
requirement, never asserts it was actually confirmed for a real case).
"""

from __future__ import annotations

import pytest
from compilador_auditado import gerar_fundamentacao_projetada
from pydantic import ValidationError
from unidade_auditada_schema import ProtocoloVerificacao, RequisitoVerificacaoHumana

_NEXO_ACIDENTE = {
    "pergunta": "Há nexo entre a incapacidade e o acidente em serviço?",
    "responsavel": "IPERON",
    "meio_de_prova": "pericia_oficial",
    "momento": "processo_concessorio",
    "evidencia_exigida": "laudo pericial oficial",
}


def test_acidente_em_servico_requisito_is_well_formed() -> None:
    """The acidente-em-servico synthetic fixture is well-formed."""
    requisito = RequisitoVerificacaoHumana(
        predicado="nexo entre a incapacidade e o acidente em serviço",
        protocolo_verificacao=_NEXO_ACIDENTE,
        portador_primario="fundamentacao_integral",
    )
    assert requisito.protocolo_verificacao.responsavel == "IPERON"


def test_pericia_dependent_requisito_names_the_evidence_and_responsible_party() -> None:
    """The generated text names the responsible party and required evidence."""
    requisito = RequisitoVerificacaoHumana(
        predicado="doença enquadrada no rol de doença grave/contagiosa/incurável",
        protocolo_verificacao={
            "pergunta": "O requerente está acometido por doença do rol aplicável?",
            "responsavel": "IPERON",
            "meio_de_prova": "pericia_oficial",
            "momento": "processo_concessorio",
            "evidencia_exigida": "laudo pericial oficial",
        },
        portador_primario="fundamentacao_integral",
    )
    texto = gerar_fundamentacao_projetada(requisito)
    assert "IPERON" in texto
    assert "pericia_oficial" in texto
    assert "laudo pericial oficial" in texto


def test_complete_protocolo_is_accepted() -> None:
    """A protocolo with every field present is accepted."""
    ProtocoloVerificacao(**_NEXO_ACIDENTE)


@pytest.mark.parametrize("campo_ausente", sorted(_NEXO_ACIDENTE))
def test_incomplete_protocolo_is_rejected(campo_ausente: str) -> None:
    """Every field of the protocol is required — an incomplete one must not silently pass."""
    incompleto = {k: v for k, v in _NEXO_ACIDENTE.items() if k != campo_ausente}
    with pytest.raises(ValidationError):
        ProtocoloVerificacao(**incompleto)


def test_portador_primario_must_be_a_legacy_column_other_than_nome() -> None:
    """portador_primario=nome is rejected — nome is interface, never a portador."""
    with pytest.raises(ValidationError):
        RequisitoVerificacaoHumana(
            predicado="qualquer coisa",
            protocolo_verificacao=_NEXO_ACIDENTE,
            portador_primario="nome",
        )


def test_projected_fundamentacao_describes_the_requirement_not_a_concrete_finding() -> None:
    """RFC 0004 §7/§12.2 — the generated text carries the predicado, never a concrete finding.

    It carries the predicado (Q6-R) and points at the protocol, but must
    never read as though IPERON already made the concrete finding (Q6-S).
    """
    requisito = RequisitoVerificacaoHumana(
        predicado="nexo entre a incapacidade e o acidente em serviço",
        protocolo_verificacao=_NEXO_ACIDENTE,
        portador_primario="fundamentacao_integral",
    )
    texto = gerar_fundamentacao_projetada(requisito)

    assert requisito.predicado in texto
    assert "conforme constatação de" in texto
    for frase_de_fato_concreto in ("foi constatado", "restou comprovado", "confirmado no caso concreto"):
        assert frase_de_fato_concreto not in texto
