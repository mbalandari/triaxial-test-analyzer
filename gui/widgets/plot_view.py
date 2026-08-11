# gui/widgets/plot_view.py

from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class PlotView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.fig = Figure(figsize=(5, 4))
        self.canvas = FigureCanvasQTAgg(self.fig)
        layout.addWidget(self.canvas)

    def update_plot(self, fig):
        self.fig.clear()

        # Copy axes from provided figure
        src_ax = fig.axes[0]
        dst_ax = self.fig.add_subplot(111)

        for line in src_ax.lines:
            dst_ax.plot(line.get_xdata(), line.get_ydata(), label=line.get_label())

        dst_ax.set_xlabel(src_ax.get_xlabel())
        dst_ax.set_ylabel(src_ax.get_ylabel())
        dst_ax.set_title(src_ax.get_title())
        dst_ax.grid(True)
        dst_ax.legend()

        self.canvas.draw()
