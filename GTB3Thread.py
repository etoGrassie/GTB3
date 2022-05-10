from PyQt5.QtCore import QThread, QObject
from GTB3Exceptions import *
from GTB3Signals import GTB3Signal
from GTB3Funtions import FileControl


class GTB3ThreadFile(QThread, QObject):
    def __init__(self, file_path):
        super(GTB3ThreadFile, self).__init__()
        self.file_path = file_path

    def end(self):
        self.terminate()

    def run(self):
        super(GTB3ThreadFile, self).run()
        try:
            file_content = FileControl.open_file(self.file_path)
            print(file_content)
        except GTBIOError:
            GTB3Signal.signal_done_failed.emit()
            return

