# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ventana_Base(object):
    def setupUi(self, Ventana_Base):
        Ventana_Base.setObjectName("Ventana_Base")
        Ventana_Base.resize(641, 511)
        Ventana_Base.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Ventana_Base)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 41))
        self.frame.setStyleSheet("border: 0px solid #fff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titulo = QtWidgets.QLabel(self.frame)
        self.titulo.setGeometry(QtCore.QRect(20, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(112, 112, 112);")
        self.titulo.setObjectName("titulo")
        self.salir = QtWidgets.QPushButton(self.frame)
        self.salir.setGeometry(QtCore.QRect(570, 0, 71, 41))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.salir.setFont(font)
        self.salir.setStyleSheet("#salir {\n"
"    border: 0px solid #fff;\n"
"    color: rgb(112, 112, 112);\n"
"}\n"
"#salir:hover {\n"
"    border: 0px solid #fff;\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.salir.setObjectName("salir")
        self.frame_2 = QtWidgets.QFrame(Ventana_Base)
        self.frame_2.setGeometry(QtCore.QRect(0, 40, 641, 91))
        self.frame_2.setStyleSheet("#frame_2 {\n"
"background-color: rgb(113, 190, 161);\n"
"border: 0px solid #fff\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.input = QtWidgets.QLineEdit(self.frame_2)
        self.input.setGeometry(QtCore.QRect(20, 20, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.input.setFont(font)
        self.input.setStyleSheet("#input {\n"
"    border: 0px solid #fff;\n"
"    border-radius: 7px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-left: 80px;\n"
"    color: rgb(112, 112, 112);\n"
"}")
        self.input.setObjectName("input")
        self.imagen_enlace = QtWidgets.QLabel(self.frame_2)
        self.imagen_enlace.setGeometry(QtCore.QRect(30, 20, 51, 51))
        self.imagen_enlace.setStyleSheet("background-color: rgba(23,23,23, .0)")
        self.imagen_enlace.setScaledContents(True)
        self.imagen_enlace.setObjectName("imagen_enlace")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(80, 20, 20, 51))
        self.line.setStyleSheet("background-color: rgba(255, 255, 255);\n"
"color: rgb(112, 112, 112)")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.printGuardar = QtWidgets.QLabel(Ventana_Base)
        self.printGuardar.setGeometry(QtCore.QRect(20, 170, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        font.setItalic(False)
        self.printGuardar.setFont(font)
        self.printGuardar.setStyleSheet("background-color: rgba(255, 255, 255, .0);")
        self.printGuardar.setObjectName("printGuardar")
        self.input_Ublicacion = QtWidgets.QLineEdit(Ventana_Base)
        self.input_Ublicacion.setGeometry(QtCore.QRect(20, 190, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        self.input_Ublicacion.setFont(font)
        self.input_Ublicacion.setStyleSheet("#input_Ublicacion {\n"
"    border: 0.5px solid rgb(204, 204, 204);\n"
"    border-radius: 5px;\n"
"    padding-left: 7px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    padding-right: 64px;\n"
"}")
        self.input_Ublicacion.setReadOnly(True)
        self.input_Ublicacion.setPlaceholderText("")
        self.input_Ublicacion.setObjectName("input_Ublicacion")
        self.line_2 = QtWidgets.QFrame(Ventana_Base)
        self.line_2.setGeometry(QtCore.QRect(550, 190, 21, 31))
        self.line_2.setStyleSheet("background-color: rgba(255, 255, 255, .0);\n"
"color: rgb(204, 204, 204);\n"
"")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.botonCarpeta = QtWidgets.QToolButton(Ventana_Base)
        self.botonCarpeta.setGeometry(QtCore.QRect(560, 190, 61, 31))
        self.botonCarpeta.setStyleSheet("#botonCarpeta {\n"
"    background-color: rgba(255, 255, 255, .0);\n"
"}\n"
"#botonCarpeta:hover{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(113, 190, 161)\n"
"}")
        self.botonCarpeta.setIconSize(QtCore.QSize(44, 44))
        self.botonCarpeta.setAutoRaise(True)
        self.botonCarpeta.setObjectName("botonCarpeta")
        self.proceso = QtWidgets.QProgressBar(Ventana_Base)
        self.proceso.setGeometry(QtCore.QRect(10, 480, 621, 21))
        self.proceso.setStyleSheet("#proceso {\n"
"    border: 1px solid #fff;\n"
"    background-color: rgb(113, 190, 161);\n"
"    border-radius: 4px\n"
"}\n"
"#proceso:chunk{\n"
"    background-color: rgb(112, 112, 112);\n"
"    border-radius: 9px\n"
"}")
        self.proceso.setMaximum(100)
        self.proceso.setProperty("value", 0)
        self.proceso.setTextVisible(False)
        self.proceso.setObjectName("proceso")
        self.frame_3 = QtWidgets.QFrame(Ventana_Base)
        self.frame_3.setGeometry(QtCore.QRect(0, 130, 641, 381))
        self.frame_3.setStyleSheet("#frame_3{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid #fff;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setObjectName("frame_3")
        self.botonMp3 = QtWidgets.QToolButton(self.frame_3)
        self.botonMp3.setEnabled(True)
        self.botonMp3.setGeometry(QtCore.QRect(20, 180, 61, 71))
        self.botonMp3.setStyleSheet("#botonMp3:hover{\n"
"border: 1px solid rgb(118, 118, 118);\n"
"background-color: rgb(112, 112, 112);\n"
"border-radius: 6px\n"
"}")
        self.botonMp3.setIconSize(QtCore.QSize(53, 53))
        self.botonMp3.setAutoRaise(True)
        self.botonMp3.setObjectName("botonMp3")
        self.botonMp4 = QtWidgets.QToolButton(self.frame_3)
        self.botonMp4.setEnabled(True)
        self.botonMp4.setGeometry(QtCore.QRect(180, 180, 61, 71))
        self.botonMp4.setStyleSheet("#botonMp4:hover{\n"
"border: 1px solid rgb(118, 118, 118);\n"
"background-color: rgb(112, 112, 112);\n"
"border-radius: 6px\n"
"}")
        self.botonMp4.setIconSize(QtCore.QSize(53, 53))
        self.botonMp4.setAutoRaise(True)
        self.botonMp4.setObjectName("botonMp4")
        self.botonMp4a = QtWidgets.QToolButton(self.frame_3)
        self.botonMp4a.setGeometry(QtCore.QRect(100, 180, 61, 71))
        self.botonMp4a.setStyleSheet("#botonMp4a:hover{\n"
"border: 1px solid rgb(118, 118, 118);\n"
"background-color: rgb(112, 112, 112);\n"
"border-radius: 6px\n"
"}")
        self.botonMp4a.setIconSize(QtCore.QSize(53, 53))
        self.botonMp4a.setAutoRaise(True)
        self.botonMp4a.setObjectName("botonMp4a")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 140, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(20, 155, 221, 21))
        self.line_3.setStyleSheet("color: rgb(204, 204, 204);\n"
"background-color: rgba(255, 255, 255, .0);")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setGeometry(QtCore.QRect(0, 330, 641, 21))
        self.line_4.setStyleSheet("color: rgb(204, 204, 204);\n"
"background-color: rgba(255, 255, 255,.0);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.input_Ublicacion.raise_()
        self.printGuardar.raise_()
        self.proceso.raise_()
        self.botonCarpeta.raise_()
        self.line_2.raise_()
        self.imagen_enlace.setBuddy(self.input)
        self.printGuardar.setBuddy(self.input_Ublicacion)

        self.retranslateUi(Ventana_Base)
        QtCore.QMetaObject.connectSlotsByName(Ventana_Base)
        Ventana_Base.setTabOrder(self.input, self.input_Ublicacion)
        Ventana_Base.setTabOrder(self.input_Ublicacion, self.botonCarpeta)
        Ventana_Base.setTabOrder(self.botonCarpeta, self.botonMp3)
        Ventana_Base.setTabOrder(self.botonMp3, self.botonMp4a)
        Ventana_Base.setTabOrder(self.botonMp4a, self.botonMp4)
        Ventana_Base.setTabOrder(self.botonMp4, self.salir)

    def retranslateUi(self, Ventana_Base):
        _translate = QtCore.QCoreApplication.translate
        Ventana_Base.setWindowTitle(_translate("Ventana_Base", "Music Download"))
        self.titulo.setText(_translate("Ventana_Base", "Music Dowload"))
        self.salir.setText(_translate("Ventana_Base", "X"))
        self.input.setPlaceholderText(_translate("Ventana_Base", "Url"))
        self.printGuardar.setText(_translate("Ventana_Base", "Guardar como..."))
        self.botonMp3.setToolTip(_translate("Ventana_Base", "Mp3"))
        self.botonMp4.setToolTip(_translate("Ventana_Base", "Mp4"))
        self.botonMp4a.setToolTip(_translate("Ventana_Base", "Mp4a"))
        self.label.setText(_translate("Ventana_Base", "Descargar como:"))

