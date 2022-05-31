from PyQt5.QtWidgets import QApplication

from Signals import Signal
from Window import Ui_MainWindow

signals = Signal()


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    def setupUi(self):
        super(MainWindow, self).setupUi()
        # Connect signals and slots
        signals.return_successful_output.connect(self.encode)

    def retranslateUi(self):
        super(MainWindow, self).retranslateUi()
        signals.return_successful_output.emit(['h'])
        pass

    

    @staticmethod
    def Debugger(msg=''):
        print(f'debug activated! {msg}')

    @staticmethod
    def emitter():
        signals.return_successful_output.emit(['TEST'])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.emitter()
    sys.exit(app.exec())
