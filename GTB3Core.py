import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QFileDialog
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
        self.tabWidget_input.currentChanged.connect(self.input)

        self.actionDark_Mode.triggered.connect(lambda: self.use_theme(theme='dark_blue'))
        self.actionDefault_Light.triggered.connect(lambda: self.use_theme(theme='light_blue'))

    def input(self):
        current_index = self.tabWidget_input.currentIndex()
        print('current index: ' + current_index)
        if current_index == 0:
            file_object = GTB3FileMode(self)
            file_object.open_file_dialog()

    def use_theme(self, theme):
        apply_stylesheet(self.app, theme=theme + '.xml')


class GTB3FileMode(QThread, QObject):
    parent = None

    def __init__(self, parent):
        print('activated file mode')
        self.file_path = None
        self.parent = parent

    def open_file_dialog(self):
        dialog = QFileDialog.getOpenFileName(self, self.parent, 'Open Task Command File', './', 'Task Command File ('
                                                                                                '*.tsk)')
        self.file_path = dialog[0]



if __name__ == "__main__":
    ui = GTB3MainWindow()
    app = ui.app
    apply_stylesheet(app, theme=ui.default_theme + '.xml')
    ui.show()
    sys.exit(app.exec_())
