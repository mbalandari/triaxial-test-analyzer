from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QMenuBar,
    QFileDialog,
    QMessageBox,
)

# GUI widgets
from gui.widgets.file_list_widget import FileListWidget
from gui.widgets.specimen_view import SpecimenView
from gui.widgets.plot_view import PlotView

# Backend modules
from src.triaxial_analyzer.loader import load_file
from src.triaxial_analyzer.analysis import (
    compute_peak_strength,
    prepare_mohr_circle_data,
)
from src.triaxial_analyzer.mohr_coulomb import fit_mohr_coulomb
from src.triaxial_analyzer.plotting import create_mohr_plot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.specimens = []
        self.results = []
        self.envelope = None

        self.setWindowTitle("Triaxial Test Analyzer")
        self.resize(1200, 800)

        self._create_menu()
        self._create_layout()

    def _create_menu(self):
        menu = QMenuBar()
        self.setMenuBar(menu)

        file_menu = menu.addMenu("File")
        file_menu.addAction("Load Files", self.load_files)
        file_menu.addAction("Exit", self.close)

        analyze_menu = menu.addMenu("Analyze")
        analyze_menu.addAction("Run Analysis", self.run_analysis)

        export_menu = menu.addMenu("Export")
        export_menu.addAction("Export Report", self.export_report)

    def _create_layout(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        # Left panel: file list
        self.file_list = FileListWidget()
        main_layout.addWidget(self.file_list, 1)

        # Right panel: specimen info + plot
        right_layout = QVBoxLayout()

        self.specimen_view = SpecimenView()
        right_layout.addWidget(self.specimen_view, 1)

        self.plot_view = PlotView()
        right_layout.addWidget(self.plot_view, 2)

        main_layout.addLayout(right_layout, 2)

    # Placeholder functions
    def load_files(self):
        paths, _ = QFileDialog.getOpenFileNames(
            self, "Select Triaxial Test Files", "", "Data Files (*.csv *.xlsx)"
        )

        if paths:
            self.file_list.add_files(paths)

            # Load backend specimens
            self.specimens = []
            for p in paths:
                try:
                    sp = load_file(p)
                    self.specimens.append(sp)
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Failed to load {p}\n{e}")

            QMessageBox.information(
                self, "Loaded", f"Loaded {len(self.specimens)} specimens."
            )

    def run_analysis(self):
        if not self.specimens:
            QMessageBox.warning(self, "No Data", "Load files first.")
            return

        # Compute results for each specimen
        self.results = [compute_peak_strength(sp) for sp in self.specimens]

        # Prepare Mohr circle data
        mohr_data = prepare_mohr_circle_data(self.specimens)

        # Convert Mohr circles to sigma_n, tau pairs for envelope fitting
        sigma_n = []
        tau = []
        for item in mohr_data:
            center = item["center"]
            radius = item["radius"]
            sigma_n.append(center)
            tau.append(radius)

        # Fit envelope
        self.envelope = fit_mohr_coulomb(sigma_n, tau)

        # Create plot
        fig = create_mohr_plot(mohr_data, self.envelope)
        self.plot_view.update_plot(fig)

        # Update specimen info panel
        info_text = self._format_results_text()
        self.specimen_view.update_info(info_text)

        QMessageBox.information(
            self, "Analysis Complete", "Analysis finished successfully."
        )

    def _format_results_text(self):
        lines = []
        for r in self.results:
            lines.append(
                f"Peak Stress: {r.peak_stress:.3f} MPa\n"
                f"Peak Strain: {r.peak_strain:.5f}\n"
                f"Sigma1: {r.sigma1:.3f} MPa\n"
                f"Sigma3: {r.sigma3:.3f} MPa\n"
                "-----------------------------\n"
            )

        lines.append(
            f"Cohesion: {self.envelope['cohesion']:.3f} MPa\n"
            f"Friction Angle: {self.envelope['phi_deg']:.2f}°\n"
        )

        return "".join(lines)

    def export_report(self):
        QMessageBox.information(
            self, "Export", "Report export will be implemented in Step 8."
        )
