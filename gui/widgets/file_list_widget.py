from PySide6.QtWidgets import QWidget, QListWidget, QVBoxLayout


class FileListWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.list = QListWidget()
        layout.addWidget(self.list)

    def add_files(self, paths):
        for p in paths:
            self.list.addItem(p)

    def get_files(self):
        return [self.list.item(i).text() for i in range(self.list.count())]
