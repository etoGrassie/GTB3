import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from qt_material import apply_stylesheet

from GTB3Window import Ui_GTBMainWindow


class GTB3MainWindow(Ui_GTBMainWindow, QMainWindow, QObject):
    """
    GTB3MainWindow is used to add more functions or features to GTB3Window.py. 
    """

    def __init__(self):
        self.default_theme = 'light_blue'
        self.app = QtWidgets.QApplication(sys.argv)
        super(GTB3MainWindow, self).__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton_open_file.clicked.connect(self.test)

        self.actionDark_Mode.triggered.connect(lambda: self.use_theme(theme='dark_blue'))
        self.actionDefault_Light.triggered.connect(lambda: self.use_theme(theme='light_blue'))

    def file_mode_proceed(self):
        self.pushButton_open_file.setText("hi")

    def use_theme(self, theme):
        apply_stylesheet(self.app, theme=theme + '.xml')


if __name__ == "__main__":
    ui = GTB3MainWindow()
    app = ui.app
    apply_stylesheet(app, theme=ui.default_theme + '.xml')
    ui.show()
    sys.exit(app.exec_())
