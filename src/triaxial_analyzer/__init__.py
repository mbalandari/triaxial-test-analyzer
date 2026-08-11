"""
Triaxial Test Analyzer package.

Provides modules for loading triaxial test data, performing analysis,
fitting Mohr–Coulomb envelopes, generating plots, and exporting reports.
"""

from .loader import load_file
from .models import Specimen, AnalysisResult
from .analysis import compute_peak_strength, prepare_mohr_circle_data
from .mohr_coulomb import fit_mohr_coulomb
from .plotting import create_mohr_plot
