"""RFC 0004 §14 + RFC 0006 fase 1 — o gate sobre as duas dimensões, e o estado real.

O gate verifica **duas coisas separadas**, e os testes daqui existem para que
elas continuem separadas: *a unidade é válida e compilável* (por unidade,
qualquer que seja o estado do grupo) e *o grupo é válido dentro de um conjunto
válido* (cardinalidade, proveniência, ativação atômica).

Depois da fase 1 a fonte dos grupos é ``Conjunto.substituicoes``, não mais um
YAML global — então os fixtures montam um bundle de conjuntos sintético em vez
de um manifesto.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import yaml
from bundle import Bundle
from catalogo_proposto_gate import check_catalogo_proposto
from okf_common import DEFAULT_BUNDLE

if TYPE_CHECKING:
    from pathlib import Path

_LEGACY_ROW_COUNT = 112


def _unidade_valida_yaml(doc_id: str, origem: str) -> str:
    return (
        "---\n"
        "type: RegraProposta\n"
        f"id: {doc_id}\n"
        "schema_version: 1\n"
        "estado_proposta: elaboracao\n"
        f"origens_legacy: [{origem}]\n"
        "---\n"
    )


def _bundle_com_conjunto(tmp_path: Path, **frontmatter: object) -> Bundle:
    """Um Bundle real do repo, com um diretório de conjuntos sintético."""
    conjuntos_dir = tmp_path / "conjuntos"
    conjuntos_dir.mkdir(parents=True, exist_ok=True)
    fm: dict[str, object] = {
        "type": "Conjunto",
        "id": "vigente",
        "nome": "Conjunto de teste",
        "situacao": "vigente",
        "origem": "catalogo-legado",
    }
    fm.update(frontmatter)
    texto = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    (conjuntos_dir / "vigente.md").write_text(f"---\n{texto}---\n\n# Conjunto de teste\n", encoding="utf-8")
    return Bundle.load(DEFAULT_BUNDLE, conjuntos_dir=conjuntos_dir)


def _bundle_sem_conjuntos(tmp_path: Path) -> Bundle:
    """Um Bundle real do repo, com diretório de conjuntos vazio.

    Isolar os conjuntos é o que permite afirmar algo sobre uma unidade
    sintética: um conjunto real do repositório referencia unidades reais, que
    não existem no ``bundle_proposto_dir`` do teste, e cada referência viraria
    ``P15_DESTINO_INEXISTENTE``. O par (bundle real, auditado sintético) só é
    coerente se nenhum dos dois lados reivindicar o outro.
    """
    conjuntos_dir = tmp_path / "conjuntos-vazio"
    conjuntos_dir.mkdir(parents=True, exist_ok=True)
    return Bundle.load(DEFAULT_BUNDLE, conjuntos_dir=conjuntos_dir)


def _grupo(destinos: list[str], origens: list[str], **extra: object) -> dict[str, object]:
    grupo: dict[str, object] = {
        "grupo": "g",
        "origens_legacy": [f"/regras/{o}.md" for o in origens],
        "destinos_propostos": [f"/regras-propostas/regras/{d}.md" for d in destinos],
    }
    grupo.update(extra)
    return grupo


def test_the_real_repo_state_passes_cleanly() -> None:
    """Bundle auditado vazio e conjunto raiz sem grupos: nada a reportar (RFC 0004 §14)."""
    assert check_catalogo_proposto(Bundle.load(DEFAULT_BUNDLE)) == []


def test_112_legacy_regras_are_untouched() -> None:
    """Não-regressão: nem a Fase 1A nem a fase 1 mexem na cardinalidade legada."""
    assert len(Bundle.load(DEFAULT_BUNDLE).regras) == _LEGACY_ROW_COUNT


def test_malformed_audited_unit_fails_the_gate(tmp_path: Path) -> None:
    """Uma unidade com frontmatter inválida reprova, sem depender de grupo nenhum."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "invalido.md").write_text(
        "---\ntype: RegraProposta\nid: invalido\nschema_version: 2\n---\n", encoding="utf-8"
    )

    violations = check_catalogo_proposto(Bundle.load(DEFAULT_BUNDLE), bundle_proposto_dir=bundle_proposto_dir)

    assert violations != []


def test_malformed_document_yields_a_stable_violation_instead_of_crashing(tmp_path: Path) -> None:
    """Documento sem delimitadores não levanta — a forma do payload --json sobrevive."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "sem-frontmatter.md").write_text(
        "isto não é um documento OKF válido\n", encoding="utf-8"
    )

    violations = check_catalogo_proposto(Bundle.load(DEFAULT_BUNDLE), bundle_proposto_dir=bundle_proposto_dir)

    assert len(violations) == 1
    assert violations[0].code == "PROPOSTA_DOCUMENTO_INVALIDO"


def test_deployable_unit_with_impossible_projection_fails_with_no_group_at_all(
    tmp_path: Path,
) -> None:
    """Dimensão 1, isolada: "schema válido" nunca é "projeção deployável válida".

    A unidade não é referenciada por grupo nenhum, e ainda assim reprova —
    é o que impede o gate de confundir as duas dimensões.
    """
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001").replace("elaboracao", "deployable"),
        encoding="utf-8",
    )

    violations = check_catalogo_proposto(Bundle.load(DEFAULT_BUNDLE), bundle_proposto_dir=bundle_proposto_dir)

    codes = {v.code for v in violations}
    assert "P_COMPILA_SEM_PROVENIENCIA" in codes
    assert "P_COMPILA_PENDENTE" in codes


def test_a_unit_no_group_references_changes_nothing(tmp_path: Path) -> None:
    """Uma unidade bem formada, sem grupo que a reivindique, é inerte."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )

    bundle = _bundle_sem_conjuntos(tmp_path)

    assert check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir) == []


def test_group_provenance_must_match_what_the_destinations_declare(tmp_path: Path) -> None:
    """Dimensão 2 — a propriedade que o resolvedor de pertinência não prova.

    O conjunto afirma substituir a regra-0002; a unidade destino diz descender
    da regra-0001. Pertinência resolveria normalmente (0002 sai, a unidade
    entra) e ninguém notaria que o destino não reconhece a origem.
    """
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )
    bundle = _bundle_com_conjunto(tmp_path, substituicoes=[_grupo(["unidade-a"], ["regra-0002"])])

    codes = {v.code for v in check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir)}

    assert "P15_PROVENIENCIA_DIVERGENTE" in codes
    assert "P15_PROVENIENCIA_INCOMPLETA" in codes


def test_a_proposed_conjunto_with_divergent_provenance_also_fails(tmp_path: Path) -> None:
    """O mesmo defeito, mas numa proposta (`situacao: proposto`) — não só no vigente.

    É na proposta que a revisão de fato acontece; esperar a promoção a
    vigente para reportar a divergência é descobri-la tarde demais. O gate
    tem de percorrer todo conjunto cujo contrato valida, não só o vigente.
    """
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )
    bundle = _bundle_com_conjunto(
        tmp_path,
        situacao="proposto",
        substituicoes=[_grupo(["unidade-a"], ["regra-0002"])],
    )

    codes = {v.code for v in check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir)}

    assert "P15_PROVENIENCIA_DIVERGENTE" in codes
    assert "P15_PROVENIENCIA_INCOMPLETA" in codes


def test_matching_provenance_passes(tmp_path: Path) -> None:
    """O caso bom: o grupo declara a origem que o seu destino reconhece."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )
    bundle = _bundle_com_conjunto(tmp_path, substituicoes=[_grupo(["unidade-a"], ["regra-0001"])])

    assert check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir) == []


def test_a_group_referencing_an_unknown_unit_is_reported(tmp_path: Path) -> None:
    """Destino que não existe é reportado — e não vira divergência de proveniência espúria."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    bundle = _bundle_com_conjunto(tmp_path, substituicoes=[_grupo(["fantasma"], ["regra-0001"])])

    codes = {v.code for v in check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir)}

    assert "P15_DESTINO_INEXISTENTE" in codes


def test_an_active_group_with_a_non_deployable_destination_is_reported(tmp_path: Path) -> None:
    """Ativação é atômica: um destino em elaboração trava o grupo inteiro (RFC 0004 §1.4)."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )
    bundle = _bundle_com_conjunto(
        tmp_path,
        substituicoes=[
            _grupo(
                ["unidade-a"],
                ["regra-0001"],
                estado_grupo="ativo",
                decisao_completude={
                    "decidido_por": "x",
                    "decidido_em": "2026-01-01",
                    "justificativa": "x",
                    "fonte": "x",
                },
            )
        ],
    )

    codes = {v.code for v in check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir)}

    assert "P15_GRUPO_PARCIAL" in codes


def test_an_inactive_group_still_carrying_a_decision_is_reported(tmp_path: Path) -> None:
    """Rollback limpa a decisão; deixá-la para trás é registro de uma ativação que não há."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )
    bundle = _bundle_com_conjunto(
        tmp_path,
        substituicoes=[
            _grupo(
                ["unidade-a"],
                ["regra-0001"],
                decisao_completude={
                    "decidido_por": "x",
                    "decidido_em": "2026-01-01",
                    "justificativa": "x",
                    "fonte": "x",
                },
            )
        ],
    )

    codes = {v.code for v in check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir)}

    assert "P15_DECISAO_SEM_ATIVACAO" in codes


def test_a_group_whose_origin_is_not_a_real_legacy_rule_is_reported(tmp_path: Path) -> None:
    """Substituir o que não existe no bundle legado é declarar sobre outro catálogo."""
    bundle_proposto_dir = tmp_path / "regras-propostas"
    (bundle_proposto_dir / "regras").mkdir(parents=True)
    (bundle_proposto_dir / "regras" / "unidade-a.md").write_text(
        _unidade_valida_yaml("unidade-a", "regra-0001"), encoding="utf-8"
    )
    bundle = _bundle_com_conjunto(tmp_path, substituicoes=[_grupo(["unidade-a"], ["regra-9999"])])

    codes = {v.code for v in check_catalogo_proposto(bundle, bundle_proposto_dir=bundle_proposto_dir)}

    assert "P15_ORIGEM_INEXISTENTE" in codes
