# -*- coding: utf-8 -*-

# PyLibs
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

# Class
class Ui_MainWindow(object):
    # App
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 200)
        MainWindow.setMinimumSize(QtCore.QSize(350, 200))
        MainWindow.setMaximumSize(QtCore.QSize(350, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("other/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(270, 170, 75, 23))
        self.help.setObjectName("help")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(190, 170, 75, 23))
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(110, 170, 75, 23))
        self.ok.setObjectName("ok")
        self.pysys = QtWidgets.QLabel(self.centralwidget)
        self.pysys.setGeometry(QtCore.QRect(50, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pysys.setFont(font)
        self.pysys.setObjectName("pysys")
        self.version = QtWidgets.QLabel(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(10, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.Options = QtWidgets.QComboBox(self.centralwidget)
        self.Options.setGeometry(QtCore.QRect(50, 110, 271, 20))
        self.Options.setObjectName("Options")
        self.Options.addItem("")
        self.Options.addItem("")
        self.Options.addItem("")
        self.ask = QtWidgets.QLabel(self.centralwidget)
        self.ask.setGeometry(QtCore.QRect(50, 80, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ask.setFont(font)
        self.ask.setObjectName("ask")
        self.leftimage = QtWidgets.QLabel(self.centralwidget)
        self.leftimage.setGeometry(QtCore.QRect(0, 90, 51, 41))
        self.leftimage.setText("")
        self.leftimage.setPixmap(QtGui.QPixmap("other/left-image.png"))
        self.leftimage.setObjectName("other/leftimage")
        self.topimage = QtWidgets.QLabel(self.centralwidget)
        self.topimage.setGeometry(QtCore.QRect(10, 10, 41, 51))
        self.topimage.setText("")
        self.topimage.setPixmap(QtGui.QPixmap("other/top-image.png"))
        self.topimage.setObjectName("topimage")
        MainWindow.setCentralWidget(self.centralwidget)

        # Signals
        self.retranslateUi(MainWindow)
        self.cancel.clicked.connect(MainWindow.close)
        self.ok.clicked.connect(self.Act)
        self.help.clicked.connect(self.Mbox)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Message Box
    def Mbox(self):
        os.system("acts\mbox\Box.py")

    def Act(self):
        Opt = self.Options.currentText()

        if Opt == "Shut Down":
            os.system("acts\ShutDown.py")
        if Opt == "Restart":
            os.system("acts\Restart.py")
        if Opt == "Sleep":
            os.system("acts\Sleep.py")

    # Main Window Settings    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySys"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.ok.setText(_translate("MainWindow", "OK"))
        self.pysys.setText(_translate("MainWindow", "PySys"))
        self.version.setText(_translate("MainWindow", "Version 1.0.0"))
        self.Options.setItemText(0, _translate("MainWindow", "Shut Down"))
        self.Options.setItemText(1, _translate("MainWindow", "Restart"))
        self.Options.setItemText(2, _translate("MainWindow", "Sleep"))
        self.ask.setText(_translate("MainWindow", "What Do You Want To Do ?"))

# End
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
