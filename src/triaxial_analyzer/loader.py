"""
File loading utilities for triaxial test data.
"""

import pandas as pd
from .models import Specimen
from .utils import normalize_columns

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
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)

    df = normalize_columns(df)

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    return Specimen.from_dataframe(df, source=path)
