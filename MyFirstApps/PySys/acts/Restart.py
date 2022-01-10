# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restart.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def system(self):
        os.system("shutdown /r /t 0")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 100)
        MainWindow.setMinimumSize(QtCore.QSize(200, 100))
        MainWindow.setMaximumSize(QtCore.QSize(200, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("other/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 51, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("other/left-image.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(45, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(120, 70, 75, 25))
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(40, 70, 75, 25))
        self.ok.setObjectName("ok")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cancel.clicked.connect(MainWindow.close)
        self.ok.clicked.connect(self.system)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Restart"))
        self.label_2.setText(_translate("MainWindow", "Are Sure To Restart ?"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.ok.setText(_translate("MainWindow", "Restart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
