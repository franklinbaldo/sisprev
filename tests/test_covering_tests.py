"""Tests for bundle.covering_tests() — achado -> pytest node files traceability."""

from __future__ import annotations

from achado_schema import Achado, load_achados
from bundle import covering_tests
from okf_common import DEFAULT_BUNDLE


def test_covering_tests_returns_the_p2_test_files_for_a_real_p2_achado() -> None:
    """A real committed achado referencing P2_IGUALDADE_MATERIAL_ATIVA points at its tests."""
    achado = next(
        a
        for a in load_achados(DEFAULT_BUNDLE)
        if any(detector == "P2_IGUALDADE_MATERIAL_ATIVA" for detector, _ in a.detection_refs)
    )

    tests = covering_tests(achado)

    assert "tests/test_detector_igualdade_material.py" in tests
    assert "tests/test_detector_properties.py" in tests


def test_covering_tests_is_empty_for_a_manual_achado_with_no_deteccoes() -> None:
    """An achado with verificacao=manual (no deteccoes) has no covering tests."""
    achado = Achado(doc_id="achado-9999", frontmatter={"deteccoes": []})
    assert covering_tests(achado) == []


def test_covering_tests_ignores_an_unknown_detector_id() -> None:
    """A detector id absent from the registry contributes nothing, never raises."""
    achado = Achado(
        doc_id="achado-9999",
        frontmatter={"deteccoes": [{"detector": "P99_NAO_EXISTE", "fingerprint": f"sha256:{'a' * 64}"}]},
    )
    assert covering_tests(achado) == []


def test_covering_tests_dedupes_across_multiple_deteccoes_from_the_same_detector() -> None:
    """Two deteccoes from the same detector must not duplicate its test files."""
    achado = Achado(
        doc_id="achado-9999",
        frontmatter={
            "deteccoes": [
                {"detector": "P1_NOME_REPETIDO", "fingerprint": f"sha256:{'a' * 64}"},
                {"detector": "P1_NOME_REPETIDO", "fingerprint": f"sha256:{'b' * 64}"},
            ]
        },
    )
    tests = covering_tests(achado)
    assert tests == ["tests/test_detector_camada_3.py"]
