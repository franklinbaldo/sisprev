"""The committed data/regras-sisprev.csv must always match the committed bundle.

Rules are edited in okf/regras-sisprev/regras/*.md, never in a CSV by hand.
data/regras-sisprev.csv is a derived, always-regenerated export of that
bundle's current (possibly audit-corrected) state — this test (and CI) fail
if someone edits a regra doc without regenerating and committing it.
"""

from __future__ import annotations

import datetime
import json
from typing import TYPE_CHECKING

import pandas as pd
import pytest
from okf_common import DEFAULT_BUNDLE, DEFAULT_REBUILT_CSV
from okf_to_csv import _admin_scalar, _json_admin, load_bundle_extended

if TYPE_CHECKING:
    from pathlib import Path


def _read(csv_path: Path) -> pd.DataFrame:
    """Read a regras-sisprev CSV the same way the conversion scripts do."""
    return pd.read_csv(csv_path, skiprows=1, keep_default_na=False, dtype=str)


def test_committed_csv_matches_committed_bundle() -> None:
    """data/regras-sisprev.csv (27 original + admin columns, P12) must match the live bundle."""
    committed = _read(DEFAULT_REBUILT_CSV)
    current = load_bundle_extended(DEFAULT_BUNDLE)

    pd.testing.assert_frame_equal(committed, current)


def test_a_trilha_da_regra_0025_chega_ao_csv_no_caminho_real() -> None:
    """Integração do caminho inteiro: YAML -> Bundle -> CSV -> leitura.

    Os testes de contrato de `disposicao_de_achados` usam Bundle sintético e não
    passam pelo `okf_to_csv`, e foi exatamente essa fronteira que quebrou no
    primeiro uso real do campo: o YAML lê `2026-07-30` como `datetime.date`, que
    `json.dumps` recusa (célula JSON) e que faz o dtype da coluna escalar virar
    `object`. Este teste cobre as duas formas de célula de uma vez, sobre o
    bundle comitado — que é onde a `regra-0025` carrega a trilha de verdade.

    Cobre também o **vocabulário da disposição**, e é por isso que ele mora aqui
    e não entre os testes de contrato: `encaminhada` e `decisao_pendente_de` são
    checados nos dois lados por Bundle sintético, mas nada provava que o primeiro
    consumidor real do campo — esta regra — atravessa a serialização carregando
    os dois. Foi o que a integração das duas frentes teve de migrar à mão
    (`nao_impede` era o valor gravado antes do rename), e um valor de enum
    aposentado que sobrevivesse num doc real falharia só no `validar_regras`.
    """
    csv = pd.read_csv(DEFAULT_REBUILT_CSV, dtype=str, skiprows=1)
    linha = csv[csv["NOME"].notna()].iloc[24]  # row_index 25

    # célula escalar
    assert linha["auditado_em"] == "2026-07-30"

    # célula JSON, relida como JSON — não basta a string conter a data
    disposicoes = json.loads(linha["disposicao_de_achados"])
    assert disposicoes, "a regra-0025 deve carregar a disposição do achado-0008"
    disposicao = disposicoes[0]
    assert disposicao["decidido_em"] == "2026-07-30"

    # o vocabulário vigente, e o responsável nomeado junto com ele
    assert disposicao["disposicao"] == "encaminhada"
    assert disposicao["decisao_pendente_de"].strip(), "`encaminhada` sem responsável deixa o defeito sem dono"

    # e o serializador continua estourando no que não é data
    assert _admin_scalar(datetime.date(2026, 7, 30)) == "2026-07-30"
    with pytest.raises(TypeError, match="não serializável"):
        _json_admin([{"x": object()}])
