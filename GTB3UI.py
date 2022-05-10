from GTB3Window import MainWindow as rawMainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget


class MainWindow(rawMainWindow, QMainWindow, QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

    def setupUi(self, window_object):
        super(MainWindow, self).setupUi(window_object)

        # Links go here


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    window = QMainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())