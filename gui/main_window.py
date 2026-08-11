from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QMenuBar,
    QFileDialog,
    QMessageBox,
)
from gui.widgets.file_list_widget import FileListWidget
from gui.widgets.specimen_view import SpecimenView
from gui.widgets.plot_view import PlotView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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

    def run_analysis(self):
        QMessageBox.information(
            self, "Analysis", "Analysis will be implemented in Step 7."
        )

    def export_report(self):
        QMessageBox.information(
            self, "Export", "Report export will be implemented in Step 8."
        )
