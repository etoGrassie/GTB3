from PyQt5.QtCore import QObject, pyqtSignal


class Signal(QObject):
    return_successful_output = pyqtSignal(list)
    return_failed_output = pyqtSignal(dict)
    pop_warn_msg = pyqtSignal(str, str)
    pop_ques_msg = pyqtSignal(str, str)
