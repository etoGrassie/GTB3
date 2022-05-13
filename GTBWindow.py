# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GTBWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        self.setupUi()

    def setupUi(self):
        self.setObjectName("GTBMainWindow")
        self.resize(763, 625)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/pycharm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_output = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.groupBox_output.setFont(font)
        self.groupBox_output.setObjectName("groupBox_output")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_output)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget_output = QtWidgets.QTabWidget(self.groupBox_output)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.tabWidget_output.setFont(font)
        self.tabWidget_output.setObjectName("tabWidget_output")
        self.tab_output_successful = QtWidgets.QWidget()
        self.tab_output_successful.setObjectName("tab_output_successful")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_output_successful)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser_output_successful = QtWidgets.QTextBrowser(self.tab_output_successful)
        self.textBrowser_output_successful.setObjectName("textBrowser_output_successful")
        self.verticalLayout_5.addWidget(self.textBrowser_output_successful)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_output_save = QtWidgets.QPushButton(self.tab_output_successful)
        self.pushButton_output_save.setEnabled(False)
        self.pushButton_output_save.setObjectName("pushButton_output_save")
        self.horizontalLayout_3.addWidget(self.pushButton_output_save)
        self.pushButton_output_clear = QtWidgets.QPushButton(self.tab_output_successful)
        self.pushButton_output_clear.setEnabled(False)
        self.pushButton_output_clear.setObjectName("pushButton_output_clear")
        self.horizontalLayout_3.addWidget(self.pushButton_output_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.tabWidget_output.addTab(self.tab_output_successful, "")
        self.tab_output_failed = QtWidgets.QWidget()
        self.tab_output_failed.setObjectName("tab_output_failed")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_output_failed)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_failed_tasks = QtWidgets.QLabel(self.tab_output_failed)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_failed_tasks.setFont(font)
        self.label_failed_tasks.setObjectName("label_failed_tasks")
        self.verticalLayout_6.addWidget(self.label_failed_tasks)
        self.listWidget = QtWidgets.QListWidget(self.tab_output_failed)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignLeading)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_6.addWidget(self.listWidget)
        self.label_failed_reasons = QtWidgets.QLabel(self.tab_output_failed)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_failed_reasons.setFont(font)
        self.label_failed_reasons.setObjectName("label_failed_reasons")
        self.verticalLayout_6.addWidget(self.label_failed_reasons)
        self.lineEdit_failed_reason = QtWidgets.QLineEdit(self.tab_output_failed)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.lineEdit_failed_reason.setFont(font)
        self.lineEdit_failed_reason.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_failed_reason.setObjectName("lineEdit_failed_reason")
        self.verticalLayout_6.addWidget(self.lineEdit_failed_reason)
        self.tabWidget_output.addTab(self.tab_output_failed, "")
        self.verticalLayout_2.addWidget(self.tabWidget_output)
        self.horizontalLayout.addWidget(self.groupBox_output)
        self.groupBox_input = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.groupBox_input.setFont(font)
        self.groupBox_input.setObjectName("groupBox_input")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_input)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_input = QtWidgets.QTabWidget(self.groupBox_input)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.tabWidget_input.setFont(font)
        self.tabWidget_input.setObjectName("tabWidget_input")
        self.tab_input_file = QtWidgets.QWidget()
        self.tab_input_file.setObjectName("tab_input_file")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_input_file)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_file_select = QtWidgets.QLabel(self.tab_input_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_file_select.setFont(font)
        self.label_file_select.setObjectName("label_file_select")
        self.verticalLayout_4.addWidget(self.label_file_select)
        self.pushButton_open_file = QtWidgets.QPushButton(self.tab_input_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.pushButton_open_file.setFont(font)
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.verticalLayout_4.addWidget(self.pushButton_open_file)
        self.lineEdit_file_path = QtWidgets.QLineEdit(self.tab_input_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.lineEdit_file_path.setFont(font)
        self.lineEdit_file_path.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.verticalLayout_4.addWidget(self.lineEdit_file_path)
        self.label_file_preview = QtWidgets.QLabel(self.tab_input_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_file_preview.setFont(font)
        self.label_file_preview.setObjectName("label_file_preview")
        self.verticalLayout_4.addWidget(self.label_file_preview)
        self.textBrowser_file_preview = QtWidgets.QTextBrowser(self.tab_input_file)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.textBrowser_file_preview.setFont(font)
        self.textBrowser_file_preview.setObjectName("textBrowser_file_preview")
        self.verticalLayout_4.addWidget(self.textBrowser_file_preview)
        self.tabWidget_input.addTab(self.tab_input_file, "")
        self.tab_input_IDLE_multiple = QtWidgets.QWidget()
        self.tab_input_IDLE_multiple.setObjectName("tab_input_IDLE_multiple")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_input_IDLE_multiple)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_IDLE_mul = QtWidgets.QLabel(self.tab_input_IDLE_multiple)
        self.label_IDLE_mul.setObjectName("label_IDLE_mul")
        self.verticalLayout_7.addWidget(self.label_IDLE_mul)
        self.textBrowser_IDLE_multiple = QtWidgets.QTextBrowser(self.tab_input_IDLE_multiple)
        self.textBrowser_IDLE_multiple.setObjectName("textBrowser_IDLE_multiple")
        self.verticalLayout_7.addWidget(self.textBrowser_IDLE_multiple)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_IDLE_mul_edit = QtWidgets.QPushButton(self.tab_input_IDLE_multiple)
        self.pushButton_IDLE_mul_edit.setObjectName("pushButton_IDLE_mul_edit")
        self.horizontalLayout_4.addWidget(self.pushButton_IDLE_mul_edit)
        self.pushButton_IDLE_mul_clear = QtWidgets.QPushButton(self.tab_input_IDLE_multiple)
        self.pushButton_IDLE_mul_clear.setObjectName("pushButton_IDLE_mul_clear")
        self.horizontalLayout_4.addWidget(self.pushButton_IDLE_mul_clear)
        self.pushButton_IDLE_mul_help = QtWidgets.QPushButton(self.tab_input_IDLE_multiple)
        self.pushButton_IDLE_mul_help.setObjectName("pushButton_IDLE_mul_help")
        self.horizontalLayout_4.addWidget(self.pushButton_IDLE_mul_help)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.tabWidget_input.addTab(self.tab_input_IDLE_multiple, "")
        self.verticalLayout_3.addWidget(self.tabWidget_input)
        self.commandLinkButton_run = QtWidgets.QCommandLinkButton(self.groupBox_input)
        self.commandLinkButton_run.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.commandLinkButton_run.setFont(font)
        self.commandLinkButton_run.setObjectName("commandLinkButton_run")
        self.verticalLayout_3.addWidget(self.commandLinkButton_run)
        self.horizontalLayout.addWidget(self.groupBox_input)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 23))
        self.menubar.setObjectName("menubar")
        self.menuGTB = QtWidgets.QMenu(self.menubar)
        self.menuGTB.setObjectName("menuGTB")
        self.menu_Application = QtWidgets.QMenu(self.menuGTB)
        self.menu_Application.setObjectName("menu_Application")
        self.menuCustomization = QtWidgets.QMenu(self.menuGTB)
        self.menuCustomization.setObjectName("menuCustomization")
        self.menuWindow_Style = QtWidgets.QMenu(self.menuCustomization)
        self.menuWindow_Style.setObjectName("menuWindow_Style")
        self.menuLight = QtWidgets.QMenu(self.menuWindow_Style)
        self.menuLight.setObjectName("menuLight")
        self.menuDark = QtWidgets.QMenu(self.menuWindow_Style)
        self.menuDark.setObjectName("menuDark")
        self.menuFont = QtWidgets.QMenu(self.menuCustomization)
        self.menuFont.setObjectName("menuFont")
        self.menuAbout = QtWidgets.QMenu(self.menuGTB)
        self.menuAbout.setObjectName("menuAbout")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.action_Quit = QtWidgets.QAction(self)
        self.action_Quit.setObjectName("action_Quit")
        self.actionSet_to_Default = QtWidgets.QAction(self)
        self.actionSet_to_Default.setObjectName("actionSet_to_Default")
        self.actionCustomize = QtWidgets.QAction(self)
        self.actionCustomize.setObjectName("actionCustomize")
        self.actionAbout_App = QtWidgets.QAction(self)
        self.actionAbout_App.setObjectName("actionAbout_App")
        self.actionGithub = QtWidgets.QAction(self)
        self.actionGithub.setObjectName("actionGithub")
        self.actionYellow = QtWidgets.QAction(self)
        self.actionYellow.setObjectName("actionYellow")
        self.actionBlue = QtWidgets.QAction(self)
        self.actionBlue.setObjectName("actionBlue")
        self.actionCyan = QtWidgets.QAction(self)
        self.actionCyan.setObjectName("actionCyan")
        self.actionLightgreen = QtWidgets.QAction(self)
        self.actionLightgreen.setObjectName("actionLightgreen")
        self.actionOrange = QtWidgets.QAction(self)
        self.actionOrange.setObjectName("actionOrange")
        self.actionPink = QtWidgets.QAction(self)
        self.actionPink.setObjectName("actionPink")
        self.actionPurple = QtWidgets.QAction(self)
        self.actionPurple.setObjectName("actionPurple")
        self.actionRed = QtWidgets.QAction(self)
        self.actionRed.setObjectName("actionRed")
        self.actionTeal = QtWidgets.QAction(self)
        self.actionTeal.setObjectName("actionTeal")
        self.actionYell9ow = QtWidgets.QAction(self)
        self.actionYell9ow.setObjectName("actionYell9ow")
        self.actionAmber = QtWidgets.QAction(self)
        self.actionAmber.setObjectName("actionAmber")
        self.actionBlue_2 = QtWidgets.QAction(self)
        self.actionBlue_2.setObjectName("actionBlue_2")
        self.actionCyan_2 = QtWidgets.QAction(self)
        self.actionCyan_2.setObjectName("actionCyan_2")
        self.actionLightgreen_2 = QtWidgets.QAction(self)
        self.actionLightgreen_2.setObjectName("actionLightgreen_2")
        self.actionPink_2 = QtWidgets.QAction(self)
        self.actionPink_2.setObjectName("actionPink_2")
        self.actionPurple_2 = QtWidgets.QAction(self)
        self.actionPurple_2.setObjectName("actionPurple_2")
        self.actionRed_2 = QtWidgets.QAction(self)
        self.actionRed_2.setObjectName("actionRed_2")
        self.actionYellow_2 = QtWidgets.QAction(self)
        self.actionYellow_2.setObjectName("actionYellow_2")
        self.actionSet_to_default = QtWidgets.QAction(self)
        self.actionSet_to_default.setObjectName("actionSet_to_default")
        self.menu_Application.addAction(self.action_Quit)
        self.menuLight.addAction(self.actionYellow)
        self.menuLight.addAction(self.actionBlue)
        self.menuLight.addAction(self.actionCyan)
        self.menuLight.addAction(self.actionLightgreen)
        self.menuLight.addAction(self.actionOrange)
        self.menuLight.addAction(self.actionPink)
        self.menuLight.addAction(self.actionPurple)
        self.menuLight.addAction(self.actionRed)
        self.menuLight.addAction(self.actionTeal)
        self.menuLight.addAction(self.actionYell9ow)
        self.menuDark.addAction(self.actionAmber)
        self.menuDark.addAction(self.actionBlue_2)
        self.menuDark.addAction(self.actionCyan_2)
        self.menuDark.addAction(self.actionLightgreen_2)
        self.menuDark.addAction(self.actionPink_2)
        self.menuDark.addAction(self.actionPurple_2)
        self.menuDark.addAction(self.actionRed_2)
        self.menuDark.addAction(self.actionYellow_2)
        self.menuWindow_Style.addAction(self.actionSet_to_default)
        self.menuWindow_Style.addSeparator()
        self.menuWindow_Style.addAction(self.menuLight.menuAction())
        self.menuWindow_Style.addAction(self.menuDark.menuAction())
        self.menuFont.addAction(self.actionSet_to_Default)
        self.menuFont.addSeparator()
        self.menuFont.addAction(self.actionCustomize)
        self.menuCustomization.addAction(self.menuFont.menuAction())
        self.menuCustomization.addAction(self.menuWindow_Style.menuAction())
        self.menuAbout.addAction(self.actionAbout_App)
        self.menuAbout.addAction(self.actionGithub)
        self.menuGTB.addAction(self.menu_Application.menuAction())
        self.menuGTB.addAction(self.menuCustomization.menuAction())
        self.menuGTB.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuGTB.menuAction())

        self.retranslateUi(self)
        self.tabWidget_output.setCurrentIndex(0)
        self.tabWidget_input.setCurrentIndex(0)
        self.action_Quit.triggered.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, GTBMainWindow):
        _translate = QtCore.QCoreApplication.translate
        GTBMainWindow.setWindowTitle(_translate("GTBMainWindow", "GTB Release 3"))
        self.groupBox_output.setTitle(_translate("GTBMainWindow", "Output"))
        self.textBrowser_output_successful.setPlaceholderText(
            _translate("GTBMainWindow", "Run a task to see the output of successfully ran tasks"))
        self.pushButton_output_save.setText(_translate("GTBMainWindow", "Save Output"))
        self.pushButton_output_clear.setText(_translate("GTBMainWindow", "Clear"))
        self.tabWidget_output.setTabText(self.tabWidget_output.indexOf(self.tab_output_successful),
                                         _translate("GTBMainWindow", "Successful"))
        self.label_failed_tasks.setText(_translate("GTBMainWindow", "Failed Task (s)"))
        self.label_failed_reasons.setText(_translate("GTBMainWindow", "Failure Reason (s)"))
        self.lineEdit_failed_reason.setPlaceholderText(
            _translate("GTBMainWindow", "Select a failed task to see the error message"))
        self.tabWidget_output.setTabText(self.tabWidget_output.indexOf(self.tab_output_failed),
                                         _translate("GTBMainWindow", "Failed Task(s)"))
        self.groupBox_input.setTitle(_translate("GTBMainWindow", "Input"))
        self.label_file_select.setText(_translate("GTBMainWindow", "File Select"))
        self.pushButton_open_file.setText(_translate("GTBMainWindow", "Open task file (*.tsk)"))
        self.lineEdit_file_path.setPlaceholderText(_translate("GTBMainWindow", "Open a file to see file path"))
        self.label_file_preview.setText(_translate("GTBMainWindow", "File Preview"))
        self.textBrowser_file_preview.setPlaceholderText(_translate("GTBMainWindow", "Open a file to see the preview"))
        self.tabWidget_input.setTabText(self.tabWidget_input.indexOf(self.tab_input_file),
                                        _translate("GTBMainWindow", "From a File"))
        self.label_IDLE_mul.setText(_translate("GTBMainWindow", "Input multiple tasks below"))
        self.textBrowser_IDLE_multiple.setPlaceholderText(_translate("GTBMainWindow",
                                                                     "Input tasks here, switch lines by pressing the Enter key. Use buttons below to get more functions. "))
        self.pushButton_IDLE_mul_edit.setText(_translate("GTBMainWindow", "Edit"))
        self.pushButton_IDLE_mul_clear.setText(_translate("GTBMainWindow", "Clear"))
        self.pushButton_IDLE_mul_help.setText(_translate("GTBMainWindow", "Help"))
        self.tabWidget_input.setTabText(self.tabWidget_input.indexOf(self.tab_input_IDLE_multiple),
                                        _translate("GTBMainWindow", "IDLE Multiple"))
        self.commandLinkButton_run.setText(_translate("GTBMainWindow", "Run 0 Task(s) From File/ IDLE Multiple"))
        self.menuGTB.setTitle(_translate("GTBMainWindow", "&GTB"))
        self.menu_Application.setTitle(_translate("GTBMainWindow", "&Application"))
        self.menuCustomization.setTitle(_translate("GTBMainWindow", "&Customization"))
        self.menuWindow_Style.setTitle(_translate("GTBMainWindow", "&Window Style"))
        self.menuLight.setTitle(_translate("GTBMainWindow", "Light"))
        self.menuDark.setTitle(_translate("GTBMainWindow", "Dark"))
        self.menuFont.setTitle(_translate("GTBMainWindow", "&Font"))
        self.menuAbout.setTitle(_translate("GTBMainWindow", "A&bout"))
        self.action_Quit.setText(_translate("GTBMainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("GTBMainWindow", "Ctrl+Alt+Q"))
        self.actionSet_to_Default.setText(_translate("GTBMainWindow", "Set to Default"))
        self.actionCustomize.setText(_translate("GTBMainWindow", "Customize"))
        self.actionAbout_App.setText(_translate("GTBMainWindow", "Ab&out App"))
        self.actionGithub.setText(_translate("GTBMainWindow", "&Github"))
        self.actionYellow.setText(_translate("GTBMainWindow", "Amber"))
        self.actionBlue.setText(_translate("GTBMainWindow", "Blue"))
        self.actionCyan.setText(_translate("GTBMainWindow", "Cyan"))
        self.actionLightgreen.setText(_translate("GTBMainWindow", "Lightgreen"))
        self.actionOrange.setText(_translate("GTBMainWindow", "Orange"))
        self.actionPink.setText(_translate("GTBMainWindow", "Pink"))
        self.actionPurple.setText(_translate("GTBMainWindow", "Purple"))
        self.actionRed.setText(_translate("GTBMainWindow", "Red"))
        self.actionTeal.setText(_translate("GTBMainWindow", "Teal"))
        self.actionYell9ow.setText(_translate("GTBMainWindow", "Yellow"))
        self.actionAmber.setText(_translate("GTBMainWindow", "Amber"))
        self.actionBlue_2.setText(_translate("GTBMainWindow", "Blue (Default)"))
        self.actionCyan_2.setText(_translate("GTBMainWindow", "Cyan"))
        self.actionLightgreen_2.setText(_translate("GTBMainWindow", "Lightgreen"))
        self.actionPink_2.setText(_translate("GTBMainWindow", "Pink"))
        self.actionPurple_2.setText(_translate("GTBMainWindow", "Purple"))
        self.actionRed_2.setText(_translate("GTBMainWindow", "Red"))
        self.actionYellow_2.setText(_translate("GTBMainWindow", "Yellow"))
        self.actionSet_to_default.setText(_translate("GTBMainWindow", "Set to Default"))


import GTBResourses

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GTBMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(GTBMainWindow)
    GTBMainWindow.show()
    sys.exit(app.exec_())
