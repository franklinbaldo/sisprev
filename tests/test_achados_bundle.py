"""Contract + correspondence tests over the real committed bundle (RFC 0001, P10/P14).

These call the domain library — they never re-implement the detector logic
or keep a second list of the expected detections. The parametrized test
proves every committed achado obeys the schema; the correspondence tests
prove the bidirectional relation between detections and open achados.
"""

from __future__ import annotations

import pytest
from achado_schema import load_achados, validate_achado
from bundle import (
    Bundle,
    collect_detections,
    stale_detection_refs,
    uncovered_detections,
    validate_bundle,
)
from okf_common import DEFAULT_BUNDLE

_EXPECTED_P2_DETECTIONS = 7


@pytest.fixture(scope="module")
def bundle() -> Bundle:
    """The real committed bundle, loaded once for the module."""
    return Bundle.load(DEFAULT_BUNDLE)


@pytest.mark.parametrize("doc_id", [a.doc_id for a in load_achados(DEFAULT_BUNDLE)])
def test_committed_achado_obeys_schema(doc_id: str, bundle: Bundle) -> None:
    """Every achado-*.md in the repo satisfies the P14 contract."""
    achado = next(a for a in bundle.achados if a.doc_id == doc_id)
    assert validate_achado(achado, known_regra_ids=bundle.regra_ids()) == []


def test_the_committed_bundle_has_no_violations(bundle: Bundle) -> None:
    """validate_bundle (camadas 1-2) is clean on the committed state."""
    assert validate_bundle(bundle) == []


def test_every_detection_that_requires_registration_is_covered(bundle: Bundle) -> None:
    """P14.6: no current detection lacks an open achado referencing its fingerprint."""
    assert uncovered_detections(bundle) == []


def test_open_achado_fingerprints_are_still_reproduced(bundle: Bundle) -> None:
    """P14.6: no open achado references a fingerprint the detectors no longer emit."""
    assert stale_detection_refs(bundle) == []


def test_the_seven_known_p2_groups_are_detected(bundle: Bundle) -> None:
    """The real import has exactly the 7 material-equality groups (ignoring NOME)."""
    detections = collect_detections(bundle)
    assert len(detections) == _EXPECTED_P2_DETECTIONS
    groups = {tuple(sorted(d.regras)) for d in detections}
    assert ("regra-0059", "regra-0063") in groups
    assert ("regra-0060", "regra-0064") in groups
