"""Unit tests for P16 — `type: FormaCalculo`."""

from __future__ import annotations

import datetime
from pathlib import Path

import forma_calculo_schema as mod
import pytest
from dispositivo_schema import dispositivo_ids
from forma_calculo_schema import (
    FormaCalculoFrontmatter,
    load_formas_calculo,
    validate_formas_calculo,
)
from pydantic import ValidationError

REPO_ROOT = Path(__file__).resolve().parent.parent
FORMAS_DIR = REPO_ROOT / "okf" / "formas-calculo"

_BASE_FM: dict[str, object] = {
    "type": "FormaCalculo",
    "id": "forma-calculo-exemplo",
    "nome": "Exemplo",
    "base": {"tipo": "totalidade_remuneracao_cargo_efetivo"},
    "dispositivos": ["/dispositivos/cf88/art-40-par-3/ec-20-1998.md"],
    "projecao_sisprev": {"tipo_calculo": "Valor Efetivo", "fidelidade": "exata"},
    "autorado_por": "franklinbaldo",
    "autorado_em": datetime.date(2026, 7, 30),
}


def _fm(**overrides: object) -> dict[str, object]:
    return {**_BASE_FM, **overrides}


def test_the_committed_formas_bundle_validates() -> None:
    """O bundle autorado passa no próprio gate — contrato de CI, não teste sintético."""
    ids = dispositivo_ids(REPO_ROOT / "okf" / "dispositivos")
    assert validate_formas_calculo(FORMAS_DIR, ids) == []
    assert load_formas_calculo(FORMAS_DIR), "o bundle não deve estar vazio"


def test_a_missing_bundle_directory_is_not_an_error() -> None:
    """Introduzir o bundle nunca pode ser pré-requisito para o resto validar."""
    assert load_formas_calculo(Path("/nao/existe")) == []
    assert validate_formas_calculo(Path("/nao/existe"), frozenset()) == []


def test_fidelidade_diferente_de_exata_exige_justificativa() -> None:
    """Perda declarada sem razão escrita é a omissão que este campo existe para impedir."""
    with pytest.raises(ValidationError, match="exige justificativa"):
        FormaCalculoFrontmatter.model_validate(
            _fm(projecao_sisprev={"tipo_calculo": "Não identificado", "fidelidade": "sem_representacao"})
        )
    ok = FormaCalculoFrontmatter.model_validate(
        _fm(
            projecao_sisprev={
                "tipo_calculo": "Não identificado",
                "fidelidade": "sem_representacao",
                "justificativa": "nenhum rótulo combina base efetiva com proporção",
            }
        )
    )
    assert ok.projecao_sisprev.fidelidade == "sem_representacao"


def test_fidelidade_exata_dispensa_justificativa() -> None:
    """Sem perda declarada não há razão a escrever."""
    contrato = FormaCalculoFrontmatter.model_validate(_fm())
    assert contrato.projecao_sisprev.justificativa is None


def test_vocabulario_e_fechado() -> None:
    """Termo novo entra com a conferência que o sustenta, nunca por uso."""
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(base={"tipo": "media_dos_ultimos_36_meses"}))
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(ajustes=[{"tipo": "bonus_professor"}]))


def test_dispositivos_nao_pode_ser_vazio_nem_repetido() -> None:
    """Uma fórmula sem dispositivo é afirmação sem fundamento."""
    with pytest.raises(ValidationError):
        FormaCalculoFrontmatter.model_validate(_fm(dispositivos=[]))
    ref = "/dispositivos/cf88/art-40-par-3/ec-20-1998.md"
    with pytest.raises(ValidationError, match="repetida"):
        FormaCalculoFrontmatter.model_validate(_fm(dispositivos=[ref, ref]))


def test_ajuste_repetido_e_rejeitado() -> None:
    """A ordem dos ajustes é significativa; repetição não é modelada."""
    with pytest.raises(ValidationError, match="tipo repetido"):
        FormaCalculoFrontmatter.model_validate(
            _fm(
                ajustes=[
                    {"tipo": "proporcional_tempo_contribuicao"},
                    {"tipo": "proporcional_tempo_contribuicao"},
                ]
            )
        )


def test_referencia_a_dispositivo_inexistente_e_violacao(tmp_path: Path) -> None:
    """O vínculo tem de resolver — mesma exigência que o P3 faz às regras."""
    doc = tmp_path / "forma-calculo-fantasma.md"
    doc.write_text(
        "---\n"
        "type: FormaCalculo\n"
        "id: forma-calculo-fantasma\n"
        "nome: Fantasma\n"
        "base:\n"
        "  tipo: totalidade_remuneracao_cargo_efetivo\n"
        "dispositivos:\n"
        "  - /dispositivos/cf88/art-999/original.md\n"
        "projecao_sisprev:\n"
        "  tipo_calculo: Valor Efetivo\n"
        "  fidelidade: exata\n"
        "autorado_por: franklinbaldo\n"
        "autorado_em: 2026-07-30\n"
        "---\n\n"
        "# Como calcular\n\nx\n\n# Entradas e saídas\n\ny\n",
        encoding="utf-8",
    )
    erros = validate_formas_calculo(tmp_path, frozenset({"cf88/art-40-par-3/ec-20-1998"}))
    assert any("não existe no bundle" in e for e in erros)


def test_secoes_obrigatorias_sao_exigidas_e_as_outras_nao(tmp_path: Path) -> None:
    """`# Fórmula` e `# Implementação` ficam de fora: exigir código gera fachada."""
    corpo_minimo = "# Como calcular\n\nprosa\n\n# Entradas e saídas\n\nprosa\n"
    doc = tmp_path / "forma-calculo-minima.md"
    frontmatter = (
        "---\n"
        "type: FormaCalculo\n"
        "id: forma-calculo-minima\n"
        "nome: Mínima\n"
        "base:\n"
        "  tipo: totalidade_remuneracao_cargo_efetivo\n"
        "dispositivos:\n"
        "  - /dispositivos/cf88/art-40-par-3/ec-20-1998.md\n"
        "projecao_sisprev:\n"
        "  tipo_calculo: Valor Efetivo\n"
        "  fidelidade: exata\n"
        "autorado_por: franklinbaldo\n"
        "autorado_em: 2026-07-30\n"
        "---\n\n"
    )
    ids = frozenset({"cf88/art-40-par-3/ec-20-1998"})

    doc.write_text(frontmatter + corpo_minimo, encoding="utf-8")
    assert validate_formas_calculo(tmp_path, ids) == []

    doc.write_text(frontmatter + "# Como calcular\n\nsó isto\n", encoding="utf-8")
    erros = validate_formas_calculo(tmp_path, ids)
    assert any("Entradas e saídas" in e for e in erros)


def test_o_modulo_nao_expoe_mapeador_do_enum_legado() -> None:
    """Cautela 1, como teste: inferir componentes do rótulo é o que não se faz.

    A decomposição é autorada contra os dispositivos, um caso por vez. Um
    mapeador `tipo_calculo -> componentes` produziria a mesma classe de
    acusação plausível e não verificada que levou à remoção do leitor de
    citações por regex (RFC 0008). Se alguém acrescentar um, este teste cai —
    e a queda é o pedido de justificação.
    """
    suspeitos = [
        nome
        for nome in dir(mod)
        if not nome.startswith("_")
        and callable(getattr(mod, nome))
        and any(t in nome.lower() for t in ("infer", "deriv", "mapea", "from_tipo", "parse_tipo"))
    ]
    assert suspeitos == []
