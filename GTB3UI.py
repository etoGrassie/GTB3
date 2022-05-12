from PyQt5.QtCore import pyqtSignal

import GTB3Applications
from GTB3Window import rawMainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget


class MainWindow(rawMainWindow, QMainWindow, QWidget):
    signal_event_open_file = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()

    def setupUi(self, window_object):
        super(MainWindow, self).setupUi(window_object)

        # Links go here
        self.pushButton_open_file.clicked.connect(self.signal_emitter)

    def signal_emitter(self):
        sender = self.sender()
        if sender == self.pushButton_open_file:
            print(True)
            self.signal_event_open_file.emit()

    def set_window_file_path(self):
        path = GTB3Applications.Application.getFilePath()
        self.lineEdit_file_path.setText(path)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    window = QMainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
