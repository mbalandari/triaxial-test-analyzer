"""
Plotting utilities for Mohr circles and failure envelopes.
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def create_mohr_plot(mohr_data, envelope=None):
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot Mohr circles
    for item in mohr_data:
        center = item["center"]
        radius = item["radius"]

        theta = np.linspace(0, 2 * np.pi, 200)
        x = center + radius * np.cos(theta)
        y = radius * np.sin(theta)

        ax.plot(x, y, label=os.path.basename(item["name"]))

    # Compute sigma_n and tau
    sigma_n = [item["center"] for item in mohr_data]
    tau = [item["radius"] for item in mohr_data]

    # Plot tangent points
    ax.scatter(sigma_n, tau, color="red", s=40, label="Tangent Points")

    # Plot envelope
    if envelope is not None:
        sigma = np.linspace(min(sigma_n) * 0.9, max(sigma_n) * 1.1, 200)
        tau_env = envelope["slope"] * sigma + envelope["cohesion"]
        ax.plot(sigma, tau_env, "r--", linewidth=2, label="Mohr–Coulomb Envelope")

    ax.set_xlabel("Normal Stress σ (MPa)")
    ax.set_ylabel("Shear Stress τ (MPa)")
    ax.set_title("Mohr Circles & Failure Envelope")
    ax.grid(True)
    ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1))

    # Make circles round
    fig.tight_layout()
    ax.set_aspect("equal", adjustable="box")

    return fig
