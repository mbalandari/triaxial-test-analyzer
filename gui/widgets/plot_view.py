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

        src_ax = fig.axes[0]
        dst_ax = self.fig.add_subplot(111)

        # Copy lines
        for line in src_ax.lines:
            dst_ax.plot(line.get_xdata(), line.get_ydata(), label=line.get_label())

        # Copy labels
        dst_ax.set_xlabel(src_ax.get_xlabel())
        dst_ax.set_ylabel(src_ax.get_ylabel())
        dst_ax.set_title(src_ax.get_title())

        # Copy grid
        dst_ax.grid(True)

        # ⭐ CRITICAL FIX: Make circles round in GUI
        dst_ax.set_aspect("equal", adjustable="box")

        # Copy legend
        dst_ax.legend(loc="upper left", bbox_to_anchor=(1.05, 1))

        self.fig.tight_layout()

        self.canvas.draw()
