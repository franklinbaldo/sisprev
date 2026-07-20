"""Mechanical detectors (RFC 0001, P10 camada 2/3).

Each detector is a pure ``detect(bundle) -> list[Detection]`` callable that
only **reports** occurrences — it never writes files, decides severity, or
authors achados (princípio da autoria humana). ``ALL`` is the flat registry
``collect_detections`` runs. Camada-2 detections (P2) set
``requires_achado=True``; camada-3 heuristics (P1/P9) set it False.
"""

from __future__ import annotations

from detectors import co_ocorrencias, igualdade_material, nome_repetido

ALL = (
    igualdade_material.detect,
    nome_repetido.detect,
    co_ocorrencias.detect_integral_sem_fundamentacao,
    co_ocorrencias.detect_campos_vazios,
    co_ocorrencias.detect_sexo_fundamentacao,
)

# detector_id -> pytest node files that exercise it (each module's own
# TESTS constant, aggregated here as the single lookup point) — used by
# Achado.covering_tests() so an achado can point a reader at the tests
# backing the mechanical claim behind its deteccoes, not just the RFC prose.
DETECTOR_TESTS: dict[str, tuple[str, ...]] = {
    igualdade_material.DETECTOR_ID: igualdade_material.TESTS,
    nome_repetido.DETECTOR_ID: nome_repetido.TESTS,
    co_ocorrencias.INTEGRAL_DETECTOR_ID: co_ocorrencias.TESTS,
    co_ocorrencias.VAZIOS_DETECTOR_ID: co_ocorrencias.TESTS,
    co_ocorrencias.SEXO_DETECTOR_ID: co_ocorrencias.TESTS,
}

__all__ = ["ALL", "DETECTOR_TESTS", "co_ocorrencias", "igualdade_material", "nome_repetido"]
