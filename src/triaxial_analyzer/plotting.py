"""
Plotting utilities for Mohr circles and failure envelopes.
"""

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
    raise NotImplementedError
