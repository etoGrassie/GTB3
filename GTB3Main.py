from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

import GTB3Thread
from GTB3Window import Ui_GTBMainWindow


class GTB3MainWindow(Ui_GTBMainWindow, QMainWindow):
    """
    GTB3MainWindow is used to add more functions or features to GTB3Window.py. 
    """

    def __init__(self):
        super(GTB3MainWindow, self).__init__()

    def setupUi(self, object_):
        self.pushButton_open_file.clicked.connect(self.test)

    def test(self):
        thr = GTB3Thread.GTB3ThreadFile()
        thr.start()
        thr.setter_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GTBMainWindow = QtWidgets.QMainWindow()
    ui = GTB3MainWindow()
    ui.setupUi(GTBMainWindow)
    GTBMainWindow.show()
    sys.exit(app.exec_())
