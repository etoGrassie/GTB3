from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep

import GTB3Funtions
import GTB3Window


class GTB3ThreadFile(GTB3Window.Ui_GTBMainWindow, QThread):
    is_running = False

    def __init__(self):
        super(GTB3ThreadFile, self).__init__()

    def run(self):
        file_index = GTB3Funtions.FileControl.user_open_and_read_file()
        while self.is_running is True:
            text = ''
            for line in file_index:
                text += line
            self.textBrowser_file_preview.setPlainText(text)
            self.commandLinkButton_run.setText()
            sleep(5)

    def setter_(self):
        self.is_running = True