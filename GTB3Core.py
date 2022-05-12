import regex as re
from PyQt5.QtCore import QThread


class FastProceed(QThread):
    def __init__(self, task):
        super(FastProceed, self).__init__()
        self.task = task

    def run(self):
        if self.task is not None:
            pass

