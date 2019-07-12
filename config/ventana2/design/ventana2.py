# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Ventana2.ui',
# licensing of 'Ui_Ventana2.ui' applies.
#
# Created: Wed Jul 10 22:24:38 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ventana2(object):
    def setupUi(self, Ventana2):
        Ventana2.setObjectName("Ventana2")
        Ventana2.resize(675, 401)
        Ventana2.setStyleSheet("#Ventana2 {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Ventana2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_titulo = QtWidgets.QLabel(Ventana2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(27)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("color: rgb(85, 85, 85);")
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout_2.addWidget(self.label_titulo)
        self.label_subtitulo = QtWidgets.QLabel(Ventana2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_subtitulo.setFont(font)
        self.label_subtitulo.setStyleSheet("color: rgb(134, 134, 134)")
        self.label_subtitulo.setObjectName("label_subtitulo")
        self.verticalLayout_2.addWidget(self.label_subtitulo)
        spacerItem = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputUblicacion = QtWidgets.QLineEdit(Ventana2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(15)
        self.inputUblicacion.setFont(font)
        self.inputUblicacion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 0px 7px;\n"
"border: 1px solid rgb(222, 222, 222);\n"
"border-radius: 1.5px;\n"
"height: 2.9em;\n"
"color: rgb(28, 39, 65);")
        self.inputUblicacion.setText("")
        self.inputUblicacion.setFrame(True)
        self.inputUblicacion.setReadOnly(True)
        self.inputUblicacion.setObjectName("inputUblicacion")
        self.verticalLayout.addWidget(self.inputUblicacion)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(368, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.boton_buscar = QtWidgets.QPushButton(Ventana2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_buscar.setFont(font)
        self.boton_buscar.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_buscar.setStyleSheet("#boton_buscar {\n"
"    border: 1px solid rgb(54, 209, 80);\n"
"    padding: 8px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(62, 175, 42);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#boton_buscar:hover {\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(54, 209, 80);\n"
"}\n"
"#boton_buscar:disabled {\n"
"    border: 1px solid rgb(203, 203, 203);\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.boton_buscar.setObjectName("boton_buscar")
        self.horizontalLayout.addWidget(self.boton_buscar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.boton_siguiente = QtWidgets.QPushButton(Ventana2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_siguiente.setFont(font)
        self.boton_siguiente.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_siguiente.setStyleSheet("#boton_siguiente {\n"
"    border: 1px solid rgb(88, 231, 210);\n"
"    padding: 10px 0px;\n"
"    border-radius: 3px;\n"
"    color: rgb(75, 199, 181);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#boton_siguiente:hover {\n"
"    padding: 10px 0px;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(88, 231, 210);\n"
"}\n"
"\n"
"#boton_siguiente:disabled {\n"
"    border: 1px solid rgb(203, 203, 203);\n"
"    padding: 10px 0px;\n"
"    border-radius: 3px;\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.boton_siguiente.setObjectName("boton_siguiente")
        self.verticalLayout_2.addWidget(self.boton_siguiente)

        self.retranslateUi(Ventana2)
        QtCore.QMetaObject.connectSlotsByName(Ventana2)

    def retranslateUi(self, Ventana2):
        Ventana2.setWindowTitle(QtWidgets.QApplication.translate("Ventana2", "Frame", None, -1))
        self.label_titulo.setText(QtWidgets.QApplication.translate("Ventana2", "Ublicación Canción", None, -1))
        self.label_subtitulo.setText(QtWidgets.QApplication.translate("Ventana2", "Este será el lugar donde se guardará las canciones.", None, -1))
        self.inputUblicacion.setPlaceholderText(QtWidgets.QApplication.translate("Ventana2", "Destino", None, -1))
        self.boton_buscar.setText(QtWidgets.QApplication.translate("Ventana2", "Buscar...", None, -1))
        self.boton_siguiente.setText(QtWidgets.QApplication.translate("Ventana2", "Siguiente", None, -1))

