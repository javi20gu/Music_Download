# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Main.ui',
# licensing of 'Ui_Main.ui' applies.
#
# Created: Sun Sep 16 22:38:47 2018
#      by: pyside2-uic  running on PySide2 5.11.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ventana(object):
    def setupUi(self, Ventana):
        Ventana.setObjectName("Ventana")
        Ventana.resize(550, 397)
        font = QtGui.QFont()
        font.setPointSize(8)
        Ventana.setFont(font)
        Ventana.setStyleSheet("#Ventana {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"#statusbar{\n"
"background-color:rgb(112, 112, 112);\n"
"color: rgb(113, 190, 161);\n"
"    font: 87 10pt \"Segoe UI Black\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Ventana)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(8, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(112, 112, 112);")
        self.titulo.setObjectName("titulo")
        self.horizontalLayout_3.addWidget(self.titulo)
        self.salir = QtWidgets.QPushButton(self.centralwidget)
        self.salir.setMinimumSize(QtCore.QSize(69, 37))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(22)
        font.setWeight(75)
        font.setBold(True)
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
        self.horizontalLayout_3.addWidget(self.salir)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame {\n"
"background-color: rgb(113, 190, 161);\n"
"border: 0px solid #fff;\n"
"margin: 0px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imagen_enlace = QtWidgets.QLabel(self.frame)
        self.imagen_enlace.setMinimumSize(QtCore.QSize(1, 4))
        self.imagen_enlace.setMaximumSize(QtCore.QSize(58, 48))
        self.imagen_enlace.setText("")
        self.imagen_enlace.setScaledContents(True)
        self.imagen_enlace.setObjectName("imagen_enlace")
        self.horizontalLayout_4.addWidget(self.imagen_enlace)
        self.input = QtWidgets.QLineEdit(self.frame)
        self.input.setMinimumSize(QtCore.QSize(0, 48))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(23)
        font.setWeight(75)
        font.setBold(True)
        self.input.setFont(font)
        self.input.setStyleSheet("#input {\n"
"    border: 0px solid #fff;\n"
"    border-radius: 7px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-left: 10px;\n"
"    color: rgb(112, 112, 112);\n"
"}")
        self.input.setInputMask("")
        self.input.setDragEnabled(True)
        self.input.setObjectName("input")
        self.horizontalLayout_4.addWidget(self.input)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(7, -1, 7, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, .0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.input_Ublicacion = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Ublicacion.setMinimumSize(QtCore.QSize(0, 42))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.input_Ublicacion.setFont(font)
        self.input_Ublicacion.setStyleSheet("#input_Ublicacion {\n"
"    border: 0.5px solid rgb(204, 204, 204);\n"
"    border-radius: 5px;\n"
"    padding-left: 7px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(112, 112, 112);\n"
"    padding-right: 64px;\n"
"}")
        self.input_Ublicacion.setReadOnly(True)
        self.input_Ublicacion.setObjectName("input_Ublicacion")
        self.horizontalLayout_2.addWidget(self.input_Ublicacion)
        self.botonCarpeta = QtWidgets.QToolButton(self.centralwidget)
        self.botonCarpeta.setMinimumSize(QtCore.QSize(61, 37))
        self.botonCarpeta.setStyleSheet("#botonCarpeta {\n"
"    background-color: rgba(255, 255, 255, .0);\n"
"}\n"
"#botonCarpeta:hover{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(113, 190, 161)\n"
"}")
        self.botonCarpeta.setText("")
        self.botonCarpeta.setIconSize(QtCore.QSize(35, 35))
        self.botonCarpeta.setAutoRaise(True)
        self.botonCarpeta.setObjectName("botonCarpeta")
        self.horizontalLayout_2.addWidget(self.botonCarpeta)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setContentsMargins(8, -1, 8, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.printDescargar = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.printDescargar.setFont(font)
        self.printDescargar.setObjectName("printDescargar")
        self.verticalLayout_3.addWidget(self.printDescargar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botonMp3 = QtWidgets.QToolButton(self.centralwidget)
        self.botonMp3.setStyleSheet("#botonMp3:hover{\n"
"border: 1px solid rgb(118, 118, 118);\n"
"background-color: rgb(112, 112, 112);\n"
"border-radius: 6px\n"
"}")
        self.botonMp3.setText("")
        self.botonMp3.setIconSize(QtCore.QSize(63, 86))
        self.botonMp3.setAutoRaise(True)
        self.botonMp3.setObjectName("botonMp3")
        self.horizontalLayout.addWidget(self.botonMp3)
        self.botonMp4a = QtWidgets.QToolButton(self.centralwidget)
        self.botonMp4a.setStyleSheet("#botonMp4a:hover{\n"
"border: 1px solid rgb(118, 118, 118);\n"
"background-color: rgb(112, 112, 112);\n"
"border-radius: 6px\n"
"}")
        self.botonMp4a.setText("")
        self.botonMp4a.setIconSize(QtCore.QSize(63, 86))
        self.botonMp4a.setAutoRaise(True)
        self.botonMp4a.setObjectName("botonMp4a")
        self.horizontalLayout.addWidget(self.botonMp4a)
        self.botonMp4 = QtWidgets.QToolButton(self.centralwidget)
        self.botonMp4.setStyleSheet("#botonMp4:hover{\n"
"border: 1px solid rgb(118, 118, 118);\n"
"background-color: rgb(112, 112, 112);\n"
"border-radius: 6px\n"
"}")
        self.botonMp4.setText("")
        self.botonMp4.setIconSize(QtCore.QSize(63, 86))
        self.botonMp4.setAutoRaise(True)
        self.botonMp4.setObjectName("botonMp4")
        self.horizontalLayout.addWidget(self.botonMp4)
        spacerItem2 = QtWidgets.QSpacerItem(420, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(8, 3, 8, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.proceso = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.proceso.setFont(font)
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
        self.verticalLayout.addWidget(self.proceso)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        Ventana.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ventana)
        self.statusbar.setObjectName("statusbar")
        Ventana.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(QtWidgets.QApplication.translate("Ventana", "MainWindow", None, -1))
        self.titulo.setText(QtWidgets.QApplication.translate("Ventana", "Music Download", None, -1))
        self.salir.setText(QtWidgets.QApplication.translate("Ventana", "X", None, -1))
        self.input.setPlaceholderText(QtWidgets.QApplication.translate("Ventana", "Url", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Ventana", "Guardar Como:", None, -1))
        self.input_Ublicacion.setPlaceholderText(QtWidgets.QApplication.translate("Ventana", "Ruta", None, -1))
        self.printDescargar.setText(QtWidgets.QApplication.translate("Ventana", "Descargar Como:", None, -1))

