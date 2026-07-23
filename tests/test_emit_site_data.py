"""Tests for the Fase B site data emitter (RFC 0003 §4/§8)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
import yaml
from achado_schema import build_achado_doc
from bundle import Bundle, collect_detections
from csv_to_okf import convert as csv_to_okf
from emit_site_data import SiteDataBundleInvalidError, build_payload, render_payload
from md_format import write_markdown
from okf_common import ORIGINAL_CSV
from regra_schema import COLUMNS, blank_frontmatter

if TYPE_CHECKING:
    from pathlib import Path


def _write_regra(bundle_dir: Path, regra_id: str, row_index: int, **overrides: object) -> None:
    """Write a minimal, hand-authored regra doc — no CSV bootstrap involved."""
    fm = blank_frontmatter()
    fm.update({"type": "Regra", "id": regra_id, "row_index": row_index, "nome": f"Regra {regra_id}"})
    fm.update(overrides)
    regras_dir = bundle_dir / "regras"
    regras_dir.mkdir(parents=True, exist_ok=True)
    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    write_markdown(regras_dir / f"{regra_id}.md", f"---\n{fm_text}---\n")


def _write_dataset_doc(bundle_dir: Path, row_count: int) -> None:
    fm = {
        "type": "Dataset",
        "title": "Teste",
        "description": "Catálogo de teste.",
        "source_file": "data/raw/regras-sisprev.csv",
        "row_count": row_count,
        "columns": [c.csv_name for c in COLUMNS],
    }
    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    write_markdown(bundle_dir / "regras-sisprev.md", f"---\n{fm_text}---\n\n# Dataset\n")


@pytest.fixture
def minimal_bundle_dir(tmp_path: Path) -> Path:
    """A hand-authored, materially-distinct 2-regra bundle — no achados/ directory at all.

    "Materially distinct" (different ``fundamentacao_integral``) matters: two
    regras with otherwise-blank identical frontmatter would trip the P2
    detector, and ``build_payload`` refuses to emit over any outstanding
    violation (see ``test_refuses_to_emit_over_a_bundle_with_outstanding_violations``)
    — this fixture exists to exercise the *clean* path instead.
    """
    out = tmp_path / "regras-sisprev"
    _write_regra(
        out,
        "regra-0001",
        1,
        validado_pge="FALSE",
        validado_presidencia="FALSE",
        ciclo_de_validacao="1º",
        fundamentacao_integral="Dispositivo A",
    )
    _write_regra(
        out,
        "regra-0002",
        2,
        validado_pge="TRUE",
        validado_presidencia="TRUE",
        ciclo_de_validacao="2º",
        fundamentacao_integral="Dispositivo B — distinto",
    )
    _write_dataset_doc(out, row_count=2)
    return out


@pytest.fixture
def bundle_dir(tmp_path: Path) -> Path:
    """A fresh bundle built from the real source CSV — has known, uncovered P2 detections."""
    out = tmp_path / "regras-sisprev"
    csv_to_okf(ORIGINAL_CSV, out)
    return out


def _cover_every_detection(bundle_dir: Path) -> None:
    """Author one achado per current P2 detection, so ``validate_bundle`` passes clean."""
    bundle = Bundle.load(bundle_dir)
    detections = collect_detections(bundle)
    (bundle_dir / "achados").mkdir(parents=True, exist_ok=True)
    for i, detection in enumerate(detections, start=1):
        regra_ids = sorted(detection.regras)
        frontmatter = {
            "type": "Achado",
            "id": f"achado-{i:04d}",
            "nome": f"Igualdade material entre {', '.join(regra_ids)}",
            "situacao": "aberto",
            "severidade": "informativo",
            "verificacao": "mecanica",
            "natureza": "dados",
            "deteccoes": [{"detector": detection.detector, "fingerprint": detection.fingerprint}],
            "regras_afetadas": [f"/regras/{regra_id}.md" for regra_id in regra_ids],
            "detectado_em": "2026-07-22",
            "detectado_por": "franklinbaldo",
        }
        sections = {
            "Descrição": "Descrição autoral.",
            "Evidências": "Evidência mecânica.",
            "Questão a investigar": "Questão aberta.",
        }
        (bundle_dir / "achados" / f"achado-{i:04d}.md").write_text(
            build_achado_doc(frontmatter, sections), encoding="utf-8"
        )


def test_payload_has_one_entry_per_regra_with_effective_defaults(minimal_bundle_dir: Path) -> None:
    """Every regra appears once, with status_auditoria defaulted like ADMIN_FIELD_DEFAULTS."""
    bundle = Bundle.load(minimal_bundle_dir)
    payload = build_payload(bundle, sha="a" * 40, generated_at="2026-07-22")

    assert payload["schema_version"] == 1
    assert payload["sha"] == "a" * 40
    assert payload["generated_at"] == "2026-07-22"
    assert set(payload["regras"]) == {"regra-0001", "regra-0002"}

    regra_0001 = payload["regras"]["regra-0001"]
    assert regra_0001["status_auditoria"] == "importada"  # neither regra declares it (P7 default)
    assert regra_0001["validado_pge"] is False
    assert regra_0001["validado_presidencia"] is False
    assert regra_0001["ciclo_de_validacao"] == "1º"


def test_validado_flags_coerce_quoted_true_false_strings_to_booleans(minimal_bundle_dir: Path) -> None:
    """'TRUE'/'FALSE' (the CSV's literal quoted strings) become real JSON booleans."""
    bundle = Bundle.load(minimal_bundle_dir)
    payload = build_payload(bundle, sha="a" * 40, generated_at="2026-07-22")

    regra_0002 = payload["regras"]["regra-0002"]
    assert regra_0002["validado_pge"] is True
    assert regra_0002["validado_presidencia"] is True
    for regra_payload in payload["regras"].values():
        assert isinstance(regra_payload["validado_pge"], bool)
        assert isinstance(regra_payload["validado_presidencia"], bool)


def test_payload_has_no_achados_on_a_bundle_without_an_achados_dir(minimal_bundle_dir: Path) -> None:
    """A bundle with no achados/ directory yet emits an empty achados map, not an error."""
    bundle = Bundle.load(minimal_bundle_dir)
    payload = build_payload(bundle, sha="a" * 40, generated_at="2026-07-22")

    assert payload["achados"] == {}


def test_payload_includes_achado_state_and_bare_regra_ids(minimal_bundle_dir: Path) -> None:
    """Achados map exposes situacao/severidade/regras_afetadas, ids normalized from /regras/*.md."""
    frontmatter = {
        "type": "Achado",
        "id": "achado-0001",
        "nome": "Teste",
        "situacao": "aberto",
        "severidade": "bloqueante",
        "verificacao": "manual",
        "natureza": "dados",
        "regras_afetadas": ["/regras/regra-0001.md", "/regras/regra-0002.md"],
        "detectado_em": "2026-07-22",
        "detectado_por": "franklinbaldo",
    }
    sections = {
        "Descrição": "Descrição autoral.",
        "Evidências": "Evidência.",
        "Questão a investigar": "Questão.",
    }
    (minimal_bundle_dir / "achados").mkdir(parents=True, exist_ok=True)
    (minimal_bundle_dir / "achados" / "achado-0001.md").write_text(
        build_achado_doc(frontmatter, sections), encoding="utf-8"
    )

    bundle = Bundle.load(minimal_bundle_dir)
    payload = build_payload(bundle, sha="a" * 40, generated_at="2026-07-22")

    assert payload["achados"]["achado-0001"] == {
        "situacao": "aberto",
        "severidade": "bloqueante",
        "regras_afetadas": ["regra-0001", "regra-0002"],
    }


def test_refuses_to_emit_over_a_bundle_with_outstanding_violations(bundle_dir: Path) -> None:
    """A bundle the P2 detector flags (uncovered by any achado) must not silently emit."""
    bundle = Bundle.load(bundle_dir)
    detections = collect_detections(bundle)
    assert detections, "the real bundle is expected to have at least one P2 detection uncovered by an achado"

    with pytest.raises(SiteDataBundleInvalidError):
        build_payload(bundle, sha="a" * 40, generated_at="2026-07-22")


def test_render_payload_is_deterministic_across_calls(bundle_dir: Path) -> None:
    """The same source state renders to byte-identical text every time (sorted keys, no clock)."""
    _cover_every_detection(bundle_dir)

    first = render_payload(build_payload(Bundle.load(bundle_dir), sha="a" * 40, generated_at="2026-07-22"))
    second = render_payload(build_payload(Bundle.load(bundle_dir), sha="a" * 40, generated_at="2026-07-22"))

    assert first == second
    assert first.endswith("\n")
    assert not first.endswith("\n\n")
