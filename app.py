from PySide6.QtWidgets import QApplication, QWidget
from ui import View
from model import Model


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.resize(600, 400)
        view = View(self, self.model)
        view.setupUi()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()