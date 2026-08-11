"""
Data models for triaxial test analysis.
"""

from dataclasses import dataclass
import numpy as np


@dataclass
class Specimen:
    """
    Represents a single triaxial test specimen.

    Attributes:
        name: Identifier or filename.
        strain: Axial strain array.
        stress: Axial stress array.
        confining_pressure: σ3 (constant for each specimen).
    """

    name: str
    strain: np.ndarray
    stress: np.ndarray
    confining_pressure: float

    @staticmethod
    def from_dataframe(df, source=""):
        """
        Create a Specimen object from a pandas DataFrame.

        Parameters:
            df: DataFrame containing axial_strain, axial_stress, confining_pressure.
            source: Optional filename or identifier.

        Returns:
            Specimen instance.
        """
        strain = df["axial_strain"].to_numpy(dtype=float)
        stress = df["axial_stress"].to_numpy(dtype=float)
        conf = float(df["confining_pressure"].iloc[0])

        return Specimen(
            name=source, strain=strain, stress=stress, confining_pressure=conf
        )


@dataclass
class AnalysisResult:
    """
    Stores computed results for a specimen.

    Attributes:
        peak_stress: Maximum axial stress.
        peak_strain: Strain at peak stress.
        sigma1: Major principal stress at failure.
        sigma3: Minor principal stress (confining pressure).
    """

    peak_stress: float
    peak_strain: float
    sigma1: float
    sigma3: float
