from PyQt5.QtWidgets import QFileDialog


class FileControl:
    def __init__(self):
        super(FileControl, self).__init__()
        self.file_path = None

    def user_open_and_read_file(self):
        file_path = self.user_open_file()
        self.file_path = file_path
        file_index = self.read_file(file_path)
        return file_index

    def user_open_file(self):
        file_filter = 'Task Command 3 File (*.tskx);;Task File (*.tsk)'
        file_value = QFileDialog.getOpenFileName(caption='Open Task File', directory='./', filter=file_filter)
        if file_value[0] is not None:
            file_path = file_value[0]
            print(file_path)
            return file_path

    def read_file(self, path):
        try:
            with open(path, 'r') as file:
                lines = file.readlines()
                return lines
        except IOError:
            return
        finally:
            pass
