import re

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog, QWidget

from GTB3Exceptions import *


class FileControl(QWidget, QObject):

    @staticmethod
    def open_file_dialog(window_object):
        dialog = QFileDialog.getOpenFileName(window_object, 'Open Task Command File', './',
                                             'Task Command File (*.tskx)')
        if bool(dialog[0]) is True:
            return dialog[0]
        else:
            return

    @staticmethod
    def save_file_dialog(window_object):
        dialog = QFileDialog.getSaveFileName(window_object, 'Save Output File', './',
                                             'Task Command File (*.tskx)')
        if bool(dialog[0]) is True:
            return dialog[0]
        else:
            return

    @staticmethod
    def open_file(file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        except IOError:
            raise GTBIOError('Cannot open file {}'.format(file_path))
        return lines


class TaskProceed:

    def proceed(self, task):
        pass

    @staticmethod
    def raw_proceed(task):
        if re.match(r'^(gtb)\b ', task) is None:
            return
        if re.match(r'(prt)|(print)\b ', task) is None:
            return
        string = re.match(r"'.*';$", task)
        if string is not None:
            return string
        else:
            return


if __name__ == '__main__':
    print(TaskProceed.raw_proceed('gtb prt \'Hello here!!!\';'))
