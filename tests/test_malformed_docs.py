"""A malformed concept doc must raise a catchable, domain-appropriate error.

Regression coverage for the shared concept.py parser: each loader must wrap
concept.ConceptDocError into its own domain error (or, for Bundle.load()'s
regra loop, rely on ConceptDocError itself subclassing ValueError) rather
than letting the generic type leak out uncaught.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from achado_schema import AchadoValidationError, load_achados
from bundle import Bundle
from concept import ConceptDocError

if TYPE_CHECKING:
    from pathlib import Path


def test_load_achados_wraps_a_malformed_doc_in_achado_validation_error(tmp_path: Path) -> None:
    """A malformed achado-*.md raises AchadoValidationError, not the generic ConceptDocError."""
    achados_dir = tmp_path / "achados"
    achados_dir.mkdir()
    (achados_dir / "achado-0001.md").write_text("no frontmatter delimiters here\n", encoding="utf-8")

    with pytest.raises(AchadoValidationError):
        load_achados(tmp_path)


def test_bundle_load_on_a_malformed_regra_raises_a_catchable_value_error(tmp_path: Path) -> None:
    """A malformed regra-*.md still raises something catchable as ValueError.

    Bundle.load() has no regra-specific wrapper error (unlike Achado's
    AchadoValidationError/Dispositivo's DispositivoValidationError) — the
    contract it preserves is only that ConceptDocError subclasses
    ValueError, matching the plain str.split()-raised ValueError this
    replaced.
    """
    (tmp_path / "regras-sisprev.md").write_text(
        "---\ntype: Dataset\nrow_count: 1\ndescription: teste\ncolumns: []\n---\n\nCorpo.\n",
        encoding="utf-8",
    )
    regras_dir = tmp_path / "regras"
    regras_dir.mkdir()
    (regras_dir / "regra-0001.md").write_text("no frontmatter delimiters here\n", encoding="utf-8")

    with pytest.raises(ValueError, match="frontmatter"):
        Bundle.load(tmp_path)

    with pytest.raises(ConceptDocError):
        Bundle.load(tmp_path)
