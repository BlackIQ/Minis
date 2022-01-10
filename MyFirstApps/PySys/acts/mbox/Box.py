# -*- coding: utf-8 -*-

# PyLibs
from PyQt5 import QtCore, QtGui, QtWidgets

# Class
class Ui_MainWindow(object):
    
    # App
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 150)
        MainWindow.setMinimumSize(QtCore.QSize(250, 150))
        MainWindow.setMaximumSize(QtCore.QSize(250, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("other\icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(170, 120, 75, 25))
        self.close.setObjectName("close")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("other\left-image.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 171, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 141, 21))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 5, 65, 41))
        self.label_7.setObjectName("label_7")
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        # Signals
        self.retranslateUi(MainWindow)
        self.close.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Main Window Setting
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help"))
        self.close.setText(_translate("MainWindow", "TNX !"))
        self.label_2.setText(_translate("MainWindow", "PySys"))
        self.label_3.setText(_translate("MainWindow", "This Program Can Does Things With Your System"))
        self.label_4.setText(_translate("MainWindow", "Developer => Amirhossein Mohammadi"))
        self.label_5.setText(_translate("MainWindow", "Choose One Option And Press OK !"))
        self.label_6.setText(_translate("MainWindow", "Developed By PyQT"))
        self.label_7.setText(_translate("MainWindow", "Version 1.0.0"))

# End
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
