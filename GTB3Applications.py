import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog


class Application(QObject, object):
    signal_update_file_path = pyqtSignal()

    def __init__(self, ui_window):
        super().__init__()

        self.__open_file_path = None
        self.output_successful = None
        self.output_failed = None
        self.control = Control()
        self.ui_window = ui_window

    @property
    def getFilePath(self):
        return self.open_file_path

    def event_open_file(self):
        file_path = self.control.dialog_open_file()
        if file_path is None:
            return
        self.ui_window.lineEdit_file_path.setText(self.getFilePath())


class Control(QWidget, QObject):

    def dialog_open_file(self):
        open_file = QFileDialog.getOpenFileName(self, 'Open file', './', 'Task Command File (*.tsk)')
        if bool(open_file[0]) is False:
            return
        return open_file[0]

    def dialog_save_file(self):
        save_file = QFileDialog.getSaveFileName(self, 'Save file', './', 'Text File (*.txt)')
        if bool(save_file[0]) is False:
            return
        return save_file[0]
