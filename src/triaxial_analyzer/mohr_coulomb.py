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
    # Linear regression: tau = m * sigma_n + c
    m, c = np.polyfit(sigma_n, tau, 1)

    phi_deg = np.degrees(np.arctan(m))
    cohesion = c

    return {"slope": m, "cohesion": cohesion, "phi_deg": phi_deg}
