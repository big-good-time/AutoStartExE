from PySide6.QtWidgets import QApplication, QWidget
from view import Ui
from model import Model


class MainWindow(QWidget, Ui):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.setUi(self, self.model)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()