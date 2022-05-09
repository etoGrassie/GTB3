from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog


class FileControl(QObject):
    file_path = None

    def __init__(self):
        super(FileControl, self).__init__()

    def open_file_dialog(self, window_object):
        dialog = QFileDialog.getOpenFileName(window_object, 'Open Task Command File', './',
                                             'Task Command File (*.tskx)')
        if bool(dialog[0]) is True:
            self.file_path = dialog[0]
            return True
        else:
            self.file_path = None
            return

    def save_file_dialog(self, window_object):
        dialog = QFileDialog.getSaveFileName(self, window_object, 'Save Output File', './',
                                             'Task Command File (*.tskx)')
        if bool(dialog[0]) is True:
            self.file_path = dialog[0]
            return True
        else:
            self.file_path = None
            return False
