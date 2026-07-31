"""Casos concretos que tornam o defeito das regras 0068--0070 reproduzível.

Este não é um novo calculador previdenciário. O teste lê o frontmatter legado e
aplica apenas os requisitos explicitamente transcritos no art. 8º da ECE
146/2021. A finalidade é mostrar a divergência entre o caso jurídico esperado
e o que o catálogo consegue devolver, sem alterar as regras históricas.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from simulador_casos import CasoAgentesNocivos, simular_agentes_nocivos_ece146

REPO_ROOT = Path(__file__).parents[1]
REGRAS_DIR = REPO_ROOT / "okf" / "regras-sisprev" / "regras"
CASO_66_15 = CasoAgentesNocivos(
    data_admissao=date(2020, 1, 10),
    data_direito=date(2022, 6, 1),
    anos_servico_publico=20,
    anos_no_cargo=5,
    pontos=66,
    anos_exposicao=15,
)


def test_caso_66_pontos_15_anos_exposicao_contraria_tabela_legada() -> None:
    """A primeira faixa é elegível, mas o catálogo marca uma tabela progressiva."""
    resultado = simular_agentes_nocivos_ece146(CASO_66_15, regras_dir=REGRAS_DIR)

    assert resultado.elegivel
    assert resultado.faixa_legal == (66, 15)
    assert resultado.tabelapontuacao_legada == "S"
    assert resultado.tabelapontuacao_legada != resultado.tabelapontuacao_esperada
    assert any("tabelapontuacao" in divergencia for divergencia in resultado.divergencias)


def test_caso_66_pontos_15_anos_devolve_tres_regras_para_uma_faixa() -> None:
    """A faixa 66/15 deve ter um desfecho, mas o legado devolve 0068, 0069 e 0070."""
    resultado = simular_agentes_nocivos_ece146(CASO_66_15, regras_dir=REGRAS_DIR)

    # A faixa é um requisito jurídico diferente e deveria selecionar um único
    # desfecho. Nenhuma das três regras registra a faixa; todas compartilham os
    # mesmos critérios que o catálogo consegue consultar.
    assert resultado.candidatos_legados == ("regra-0068", "regra-0069", "regra-0070")
    assert len(resultado.candidatos_legados) != 1
    assert any("devolveu 3 regras" in divergencia for divergencia in resultado.divergencias)
