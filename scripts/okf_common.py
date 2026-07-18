"""Shared paths and safety guards for the CSV <-> OKF regras-sisprev conversion.

The CSV <-> .md column mapping itself lives in ``regra_schema.py`` (P13.2) —
this module only holds bundle paths and the invariants that protect the
frozen original import and the live bundle from accidental overwrite.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# The frozen original import — the audit baseline. csv_to_okf.py only ever
# READS this path; no script writes to it, ever. See CLAUDE.md.
ORIGINAL_CSV = REPO_ROOT / "data" / "raw" / "regras-sisprev.csv"

# Where okf_to_csv.py writes its rebuilt/reconciled export by default — a
# derived artifact, distinct from ORIGINAL_CSV, safe to regenerate freely.
DEFAULT_REBUILT_CSV = REPO_ROOT / "data" / "regras-sisprev.csv"

DEFAULT_BUNDLE = REPO_ROOT / "okf" / "regras-sisprev"

# The dispositivos legais bundle (P3) — a sibling of DEFAULT_BUNDLE, one
# concept doc per legal provision at the smallest cited granularity.
DEFAULT_DISPOSITIVOS_BUNDLE = REPO_ROOT / "okf" / "dispositivos"

# Concept doc holding the dataset-level frontmatter (columns, row_count,
# source_file) and the "# Schema" section — see OKF SPEC.md Appendix A,
# where a dataset doc (datasets/sales.md) sits alongside its leaf
# collection (tables/*.md), each with their own index.md.
DATASET_DOC = "regras-sisprev.md"


class OriginalCsvProtectedError(Exception):
    """Raised when a script attempts to write to ORIGINAL_CSV.

    The original import is the audit baseline: it must reflect exactly what
    was received, forever. Regenerated/reconciled exports go elsewhere.
    """


def guard_not_original(out_path: Path) -> None:
    """Raise OriginalCsvProtectedError if out_path would overwrite ORIGINAL_CSV."""
    if out_path.resolve() == ORIGINAL_CSV.resolve():
        msg = (
            f"Refusing to write to {ORIGINAL_CSV} — it is the frozen original "
            "import and must never be overwritten. Pass a different --out."
        )
        raise OriginalCsvProtectedError(msg)


class BundleAlreadyInitializedError(Exception):
    """Raised when csv_to_okf.py's bootstrap targets a bundle that already has regra docs.

    csv_to_okf.py is a one-time bootstrap: after the initial import, rules
    are edited directly in regra-*.md. Re-running the bootstrap against a
    live bundle would silently overwrite every doc — including any audit
    edits made since the import — with a fresh copy derived from the frozen
    CSV. Pass force=True only if you understand you are discarding those
    edits.
    """


class BundleIntegrityError(Exception):
    """Raised when a bundle's regra docs don't form a coherent 1..N sequence.

    Each regra-NNNN.md's frontmatter ``id``/``row_index`` must match its
    filename, row_index values must cover exactly 1..N with no gaps or
    duplicates, and N must match the dataset doc's ``row_count``. This
    catches structural corruption (a dropped, duplicated, or mislabeled
    regra doc) that a bare document-count comparison would miss.
    """
