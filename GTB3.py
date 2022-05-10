from GTB3UI import *

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    window = QMainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())