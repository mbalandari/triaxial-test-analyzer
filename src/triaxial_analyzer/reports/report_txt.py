"""
Generate plain text reports.
"""


def generate_txt_report(results, envelope, output_path):
    """
    Create a TXT report summarizing analysis results.

    Parameters:
        results: List of AnalysisResult objects.
        envelope: Mohr–Coulomb envelope dict.
        output_path: File path for saving.

    Returns:
        None
    """
    with open(output_path, "w") as f:
        f.write("Triaxial Test Analysis Report\n")
        f.write("=============================\n\n")

        for r in results:
            f.write(f"Specimen:\n")
            f.write(f"  Peak Stress: {r.peak_stress:.3f}\n")
            f.write(f"  Peak Strain: {r.peak_strain:.5f}\n")
            f.write(f"  Sigma1: {r.sigma1:.3f}\n")
            f.write(f"  Sigma3: {r.sigma3:.3f}\n\n")

        f.write("Mohr–Coulomb Envelope:\n")
        f.write(f"  Cohesion: {envelope['cohesion']:.3f}\n")
        f.write(f"  Friction Angle: {envelope['phi_deg']:.2f}°\n")
