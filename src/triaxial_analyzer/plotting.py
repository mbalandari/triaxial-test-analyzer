"""
Plotting utilities for Mohr circles and failure envelopes.
"""

import numpy as np
import matplotlib.pyplot as plt


def create_mohr_plot(mohr_data, envelope=None):
    """
    Create a matplotlib Figure containing Mohr circles and envelope.

    Parameters:
        mohr_data: List of dicts with center and radius.
        envelope: Optional dict with slope and cohesion.

    Returns:
        matplotlib Figure object.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot Mohr circles
    for item in mohr_data:
        center = item["center"]
        radius = item["radius"]

        theta = np.linspace(0, 2 * np.pi, 200)
        x = center + radius * np.cos(theta)
        y = radius * np.sin(theta)

        ax.plot(x, y, label=item["name"])

    # Plot envelope
    if envelope is not None:
        sigma = np.linspace(0, max([d["sigma1"] for d in mohr_data]) * 1.2, 200)
        tau = envelope["slope"] * sigma + envelope["cohesion"]
        ax.plot(sigma, tau, "r--", linewidth=2, label="Mohr–Coulomb Envelope")

    ax.set_xlabel("Normal Stress σ (MPa)")
    ax.set_ylabel("Shear Stress τ (MPa)")
    ax.set_title("Mohr Circles & Failure Envelope")
    ax.grid(True)
    ax.legend()

    return fig
