import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from GTB3About import Ui_AboutDialog
from GTB3Window import Ui_MainWindow


class About(Ui_AboutDialog):
    def __init__(self):
        super(About, self).__init__()

    def setupUi(self):
        super(About, self).setupUi()
        pass


class MainWindow(Ui_MainWindow):
    ABOUT = About()

    def __init__(self):
        super(MainWindow, self).__init__()

    def setupUi(self):
        super(MainWindow, self).setupUi()

        # Setup Connections

        self.actionAbout_App.triggered.connect(self.show)


if __name__ == '__init__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    MAIN_WINDOW = MainWindow()
    MAIN_WINDOW.show()
    sys.exit(app.exec_())
