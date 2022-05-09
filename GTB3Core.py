import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from qt_material import apply_stylesheet

from GTB3Window import Ui_GTBMainWindow


class GTB3MainWindow(Ui_GTBMainWindow, QMainWindow, QObject):
    """
    GTB3MainWindow is used to add more functions or features to GTB3Window.py. 
    """

    def __init__(self):
        super(GTB3MainWindow, self).__init__()
        self.default_theme = 'light_blue'
        self.app = QtWidgets.QApplication(sys.argv)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_open_file.clicked.connect(self.open_file_dialog)

        self.actionDark_Mode.triggered.connect(lambda: self.use_theme(theme='dark_blue'))
        self.actionDefault_Light.triggered.connect(lambda: self.use_theme(theme='light_blue'))

    def use_theme(self, theme):
        apply_stylesheet(self.app, theme=theme + '.xml')

    def open_file_dialog(self):
        dialog = QFileDialog.getOpenFileName(self, 'Open Task Command File', './', 'Task Command File ('
                                                                                   '*.tskx)')
        self.file_path = dialog[0]

    def save_file_dialog(self):
        dialog = QFileDialog.getSaveFileName(self, 'Save Output File', './', 'Task Command File (*.tskx)')


if __name__ == "__main__":
    ui = GTB3MainWindow()
    app = ui.app
    apply_stylesheet(app, theme=ui.default_theme + '.xml')
    ui.show()
    sys.exit(app.exec_())
