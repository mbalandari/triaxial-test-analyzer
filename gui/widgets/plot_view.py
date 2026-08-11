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
        for ax in fig.axes:
            new_ax = self.fig.add_subplot(111)
            for line in ax.lines:
                new_ax.plot(line.get_xdata(), line.get_ydata())
        self.canvas.draw()
