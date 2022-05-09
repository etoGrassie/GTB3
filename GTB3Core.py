import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QWidget
from qt_material import apply_stylesheet

from GTB3Window import Ui_GTBMainWindow


class GTB3MainWindow(Ui_GTBMainWindow, QWidget, QObject):
    """
    GTB3MainWindow is used to add more functions or features to GTB3Window.py. 
    """

    def __init__(self):
        super(GTB3MainWindow, self).__init__()
        self.file_path = None
        self.default_theme = 'dark_blue'

    def init_link(self, window_object):
        window_object.pushButton_open_file.clicked.connect(self.open_file)

        window_object.actionDark_Mode.triggered.connect(lambda: self.use_theme(theme='dark_blue'))
        window_object.actionDefault_Light.triggered.connect(lambda: self.use_theme(theme='light_blue'))

    def open_file(self):
        result = self.open_file_dialog()
        if result is True:
            with open(self.file_path, 'r') as file:
                file_index = file.readlines()
            self.textBrowser_file_preview.setPlainText(''.join(file_index))
            return
        else:
            return

    @staticmethod
    def use_theme(theme):
        apply_stylesheet(app, theme=theme + '.xml')

    def open_file_dialog(self):
        dialog = QFileDialog.getOpenFileName(self, 'Open Task Command File', './', 'Task Command File ('
                                                                                   '*.tskx)')
        if bool(dialog[0]) is True:
            self.file_path = dialog[0]
            return True
        else:
            self.file_path = None
            return

    def save_file_dialog(self):
        dialog = QFileDialog.getSaveFileName(self, 'Save Output File', './', 'Task Command File (*.tskx)')
        if bool(dialog[0]) is True:
            self.file_path = dialog[0]
            return True
        else:
            self.file_path = None
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = GTB3MainWindow()  # Init GTB3MainWindow
    apply_stylesheet(app, ui.default_theme + '.xml')  # Apply default style
    ui.setupUi(MainWindow)  # Setup UI for GTBMainWindow
    ui.init_link(ui)  # Setup Links for GTBMainWindow
    MainWindow.show()  # Show Window

    sys.exit(app.exec_())  # Join Main Loop
