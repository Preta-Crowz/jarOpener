# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\_Project\jarOpener\runner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os ,sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(100, 100)
        MainWindow.setMinimumSize(QtCore.QSize(100, 100))
        MainWindow.setMaximumSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpen.setObjectName("btnOpen")
        self.btnOpen.clicked.connect(self.opn)
        self.verticalLayout.addWidget(self.btnOpen)
        self.btnWork = QtWidgets.QPushButton(self.centralwidget)
        self.btnWork.setObjectName("btnWork")
        self.btnOpen.clicked.connect(self.wrk)
        self.verticalLayout.addWidget(self.btnWork)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.file = "FILEISNOTSELECTED"
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOpen.setText(_translate("MainWindow", "Open"))
        self.btnWork.setText(_translate("MainWindow", "Run"))

    def opn(self):
        global MainWindow
        fileName = QtWidgets.QFileDialog.getOpenFileName(MainWindow,filter="*.jar")[0]
        if fileName == "": return
        if not fileName.endswith(".jar"):
            fileName += ".jar"
        self.file = fileName

    def wrk(self):
        if self.file != "FILEISNOTSELECTED":
            os.system("java -jar "+self.file)
            app.quit()
            sys.exit(0)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())