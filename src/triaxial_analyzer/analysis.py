"""
Core analysis functions for triaxial test data.
"""

from .models import Specimen, AnalysisResult


def compute_peak_strength(specimen: Specimen) -> AnalysisResult:
    """
    Compute peak stress, peak strain, and principal stresses.

    Parameters:
        specimen: Specimen object.

    Returns:
        AnalysisResult instance.
    """
    raise NotImplementedError


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
    raise NotImplementedError
