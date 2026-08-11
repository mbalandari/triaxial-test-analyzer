"""
Core analysis functions for triaxial test data.
"""

import numpy as np
from .models import Specimen, AnalysisResult


def compute_peak_strength(specimen: Specimen) -> AnalysisResult:
    """
    Compute peak stress, peak strain, and principal stresses.

    Parameters:
        specimen: Specimen object.

    Returns:
        AnalysisResult instance.
    """
    stress = specimen.stress
    strain = specimen.strain

    idx = np.argmax(stress)
    peak_stress = float(stress[idx])
    peak_strain = float(strain[idx])

    sigma1 = peak_stress
    sigma3 = specimen.confining_pressure

    return AnalysisResult(
        peak_stress=peak_stress, peak_strain=peak_strain, sigma1=sigma1, sigma3=sigma3
    )


def prepare_mohr_circle_data(specimens):
    """
    Prepare Mohr circle centers and radii for multiple specimens.

    Parameters:
        specimens: List of Specimen objects.

    Returns:
        List of dicts containing:
            - center
            - radius
            - sigma1
            - sigma3
    """
    mohr_data = []

    for sp in specimens:
        res = compute_peak_strength(sp)

        center = (res.sigma1 + res.sigma3) / 2
        radius = (res.sigma1 - res.sigma3) / 2

        mohr_data.append(
            {
                "name": sp.name,
                "center": center,
                "radius": radius,
                "sigma1": res.sigma1,
                "sigma3": res.sigma3,
            }
        )

    return mohr_data
