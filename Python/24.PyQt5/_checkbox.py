# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnHobilerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnHobilerSecilenleriAl.setGeometry(QtCore.QRect(100, 340, 93, 28))
        self.btnHobilerSecilenleriAl.setObjectName("btnHobilerSecilenleriAl")
        self.lblResultHobiler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultHobiler.setGeometry(QtCore.QRect(90, 380, 101, 111))
        self.lblResultHobiler.setText("")
        self.lblResultHobiler.setObjectName("lblResultHobiler")
        self.groupHobiler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupHobiler.setGeometry(QtCore.QRect(30, 40, 291, 271))
        self.groupHobiler.setObjectName("groupHobiler")
        self.widget = QtWidgets.QWidget(self.groupHobiler)
        self.widget.setGeometry(QtCore.QRect(80, 60, 114, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.widget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.cbKitapokumak = QtWidgets.QCheckBox(self.widget)
        self.cbKitapokumak.setObjectName("cbKitapokumak")
        self.verticalLayout.addWidget(self.cbKitapokumak)
        self.cbSpor = QtWidgets.QCheckBox(self.widget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        self.groupDersler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDersler.setGeometry(QtCore.QRect(480, 40, 291, 271))
        self.groupDersler.setObjectName("groupDersler")
        self.layoutWidget = QtWidgets.QWidget(self.groupDersler)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 60, 114, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbWebTasarim = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbWebTasarim.setObjectName("cbWebTasarim")
        self.verticalLayout_2.addWidget(self.cbWebTasarim)
        self.cbProgramlama = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbProgramlama.setObjectName("cbProgramlama")
        self.verticalLayout_2.addWidget(self.cbProgramlama)
        self.cbFizik = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbFizik.setObjectName("cbFizik")
        self.verticalLayout_2.addWidget(self.cbFizik)
        self.btnDerslerSecilenleriAl = QtWidgets.QPushButton(self.centralwidget)
        self.btnDerslerSecilenleriAl.setGeometry(QtCore.QRect(570, 340, 93, 28))
        self.btnDerslerSecilenleriAl.setObjectName("btnDerslerSecilenleriAl")
        self.lblResultDersler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultDersler.setGeometry(QtCore.QRect(570, 380, 101, 111))
        self.lblResultDersler.setText("")
        self.lblResultDersler.setObjectName("lblResultDersler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnHobilerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
        self.groupHobiler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbSinema.setText(_translate("MainWindow", "Sinema"))
        self.cbKitapokumak.setText(_translate("MainWindow", "Kitap Okumak"))
        self.cbSpor.setText(_translate("MainWindow", "Spor"))
        self.groupDersler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbWebTasarim.setText(_translate("MainWindow", "Web Tasarım"))
        self.cbProgramlama.setText(_translate("MainWindow", "Programlama"))
        self.cbFizik.setText(_translate("MainWindow", "Fizik"))
        self.btnDerslerSecilenleriAl.setText(_translate("MainWindow", "Seçilenleri Al"))
