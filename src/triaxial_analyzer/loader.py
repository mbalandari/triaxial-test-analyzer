"""
File loading utilities for triaxial test data.
"""

import pandas as pd
from .models import Specimen

REQUIRED_COLUMNS = ["axial_strain", "axial_stress", "confining_pressure"]


def load_file(path: str) -> Specimen:
    """
    Load a triaxial test file (CSV or XLSX).

    Parameters:
        path: Path to the file.

    Returns:
        Specimen instance.

    Raises:
        ValueError: Missing required columns.
    """
    raise NotImplementedError
