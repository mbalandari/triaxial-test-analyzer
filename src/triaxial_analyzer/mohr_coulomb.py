"""
Mohr–Coulomb envelope fitting.
"""

import numpy as np


def fit_mohr_coulomb(sigma_n, tau):
    """
    Fit a linear Mohr–Coulomb envelope: τ = m * σ + c.

    Parameters:
        sigma_n: Normal stresses.
        tau: Shear stresses.

    Returns:
        Dictionary containing:
            - slope
            - cohesion
            - phi_deg
    """
    raise NotImplementedError
