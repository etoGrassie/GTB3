from PyQt5.QtCore import pyqtSignal, QObject


class GTB3Signal(QObject):
    signal_proceed_done = pyqtSignal()
    signal_proceed_failed = pyqtSignal()
