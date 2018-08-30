# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ventana_1(object):
    def setupUi(self, Ventana_1):
        Ventana_1.setObjectName("Ventana_1")
        Ventana_1.resize(772, 111)
        Ventana_1.setMinimumSize(QtCore.QSize(772, 111))
        Ventana_1.setMaximumSize(QtCore.QSize(790, 111))
        Ventana_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.input = QtWidgets.QLineEdit(Ventana_1)
        self.input.setGeometry(QtCore.QRect(20, 20, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.input.setFont(font)
        self.input.setStyleSheet("#input {\n"
"    border-radius: 10px 10px 10px 10px;\n"
"    border: 0px solid rgb(255, 255, 255);\n"
"    padding-left: 10px;\n"
"    color: rgb(69, 73, 75)\n"
"}")
        self.input.setDragEnabled(True)
        self.input.setObjectName("input")
        self.botonMp3 = QtWidgets.QRadioButton(Ventana_1)
        self.botonMp3.setGeometry(QtCore.QRect(30, 80, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.botonMp3.setFont(font)
        self.botonMp3.setChecked(True)
        self.botonMp3.setObjectName("botonMp3")
        self.botonMp4 = QtWidgets.QRadioButton(Ventana_1)
        self.botonMp4.setGeometry(QtCore.QRect(90, 80, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.botonMp4.setFont(font)
        self.botonMp4.setObjectName("botonMp4")
        self.proceso = QtWidgets.QProgressBar(Ventana_1)
        self.proceso.setGeometry(QtCore.QRect(230, 80, 521, 21))
        self.proceso.setStyleSheet("border-radius: 4px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(21, 126, 255);\n"
"border: 1px solid rgb(225, 225, 225);")
        self.proceso.setMaximum(100)
        self.proceso.setProperty("value", 0)
        self.proceso.setTextVisible(False)
        self.proceso.setObjectName("proceso")
        self.botonMp4a = QtWidgets.QRadioButton(Ventana_1)
        self.botonMp4a.setGeometry(QtCore.QRect(160, 80, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.botonMp4a.setFont(font)
        self.botonMp4a.setObjectName("botonMp4a")

        self.retranslateUi(Ventana_1)
        QtCore.QMetaObject.connectSlotsByName(Ventana_1)

    def retranslateUi(self, Ventana_1):
        _translate = QtCore.QCoreApplication.translate
        Ventana_1.setWindowTitle(_translate("Ventana_1", "MusicDownload"))
        self.input.setPlaceholderText(_translate("Ventana_1", "Introduce el Url o Arrastralo"))
        self.botonMp3.setText(_translate("Ventana_1", "MP3"))
        self.botonMp4.setText(_translate("Ventana_1", "MP4"))
        self.botonMp4a.setText(_translate("Ventana_1", "MP4A"))

