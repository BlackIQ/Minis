from PyQt5 import QtCore, QtGui, QtWidgets
from Kernel import *
import time , os , sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 450)
        MainWindow.setMinimumSize(QtCore.QSize(300, 450))
        MainWindow.setMaximumSize(QtCore.QSize(300, 450))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputs = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputs.setGeometry(QtCore.QRect(10, 10, 281, 261))
        self.outputs.setObjectName("outputs")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.inputs = QtWidgets.QLineEdit(self.centralwidget)
        self.inputs.setGeometry(QtCore.QRect(10, 360, 281, 25))
        self.inputs.setObjectName("inputs")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(200, 410, 90, 25))
        self.close.setObjectName("close")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(10, 410, 90, 25))
        self.help.setObjectName("help")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.close.clicked.connect(self.done)
        self.help.clicked.connect(self.HelpWindow)
        self.inputs.returnPressed.connect(self.Proses)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	
    def done(self):
        self.outputs.append("Good bye Amir !")
        # time.sleep(1)
        MainWindow.close()

    def HelpWindow(self):
        os.system("includes/Help.py")

    def Proses(self):
        q = self.inputs.text()
        # { ----- Start ----- } Commands
        if 'hello' in q:
            hello(self)
        elif 'hi' in q:
            hello(self)

        # { How are you ? } Command
        elif 'how are you' in q:
            H_A_Y(self)

        # { ----- Doing ----- } Commands
        # { StarDate } Command
        elif 'stardate' in q:
            StarDate(self)
        # { Date } Command
        elif 'date' in q:
            Date(self)
        elif 'what date is today' in q:
            Date(self)
        elif 'today' in q:
            Date(self)
        # { Time } Command
        elif 'time' in q:
            Time(self)
        elif 'what time is it' in q:
            Time(self)
        elif 'now' in q:
            Time(self)

        # { ----- Information ----- } Commands
        elif 'about' in q:
            About(self)
        elif 'help' in q:
            Help(self)

        # { ----- System ----- }
        elif 'shutdown' in q:
            shutdown(self)

        # { ----- End  ----- } Commands
        # { Close } Command
        elif 'close' in q:
            bye(self)
        # { Sleep ) Command
        elif 'sleep' in q:
            Sleep(self)
        # { Good night } Command
        elif 'good night' in q:
            Goodnight(self)
        # { Bye } Command
        elif 'bye' in q:
            bye(self)
            # break

        # { ----- Problem ----- } Command
        else:
            problem(self)
            pass

        if "clear" in q:
            self.outputs.clear()
	
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rachel"))
        self.label.setText(_translate("MainWindow", "Type You Command"))
        self.close.setText(_translate("MainWindow", "Close"))
        self.help.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
