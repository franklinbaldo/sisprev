"""Mechanical detectors (RFC 0001, P10 camada 2/3).

Each detector module exposes ``DETECTOR_ID``, ``VERSION`` and a pure
``detect(bundle) -> list[Detection]`` function. Detectors only **report**
occurrences — they never write files, decide severity, or author achados
(princípio da autoria humana).
"""

from __future__ import annotations

from detectors import igualdade_material

# Every registered detector. collect_detections() (bundle.py) runs them all.
ALL = (igualdade_material,)

__all__ = ["ALL", "igualdade_material"]
