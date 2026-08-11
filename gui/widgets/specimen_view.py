from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class SpecimenView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Specimen Information")
        self.label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.label)

    def update_info(self, text):
        self.label.setText(text)
