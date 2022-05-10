from PyQt5.QtCore import QThread, QObject


class GTB3ThreadFile(QThread, QObject):
    def __init__(self, object_window, object_function):
        super(GTB3ThreadFile, self).__init__()
        self.object_function = object_function

    def run(self):
        if not self.object_function.open_file_path:
            self.terminate()
            return
