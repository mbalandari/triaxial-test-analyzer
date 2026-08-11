"""
Generate PDF reports.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generate_pdf_report(results, envelope, plot_path, output_path):
    """
    Create a PDF report including Mohr plot.

    Parameters:
        results: List of AnalysisResult objects.
        envelope: Envelope dict.
        plot_path: Path to saved plot image.
        output_path: PDF file path.

    Returns:
        None
    """
    c = canvas.Canvas(output_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Triaxial Test Analysis Report")

    y = 760
    c.setFont("Helvetica", 12)

    for r in results:
        c.drawString(50, y, f"Peak Stress: {r.peak_stress:.3f} MPa")
        y -= 20
        c.drawString(50, y, f"Peak Strain: {r.peak_strain:.5f}")
        y -= 20
        c.drawString(50, y, f"Sigma1: {r.sigma1:.3f} MPa")
        y -= 20
        c.drawString(50, y, f"Sigma3: {r.sigma3:.3f} MPa")
        y -= 40

    c.drawString(50, y, f"Cohesion: {envelope['cohesion']:.3f} MPa")
    y -= 20
    c.drawString(50, y, f"Friction Angle: {envelope['phi_deg']:.2f}°")
    y -= 40

    c.drawImage(plot_path, 50, y - 300, width=400, height=300)

    c.save()
