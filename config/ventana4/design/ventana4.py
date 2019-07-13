# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Ventana4.ui',
# licensing of 'Ui_Ventana4.ui' applies.
#
# Created: Fri Jul 12 22:00:08 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Descarga(object):
    def setupUi(self, Descarga):
        Descarga.setObjectName("Descarga")
        Descarga.resize(687, 431)
        Descarga.setStyleSheet("#Descarga {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Descarga)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_titulo = QtWidgets.QLabel(Descarga)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(27)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("color: rgb(85, 85, 85);")
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout.addWidget(self.label_titulo)
        self.label_subtitulo = QtWidgets.QLabel(Descarga)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_subtitulo.setFont(font)
        self.label_subtitulo.setStyleSheet("color: rgb(134, 134, 134)")
        self.label_subtitulo.setObjectName("label_subtitulo")
        self.verticalLayout.addWidget(self.label_subtitulo)
        spacerItem = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.proceso = QtWidgets.QProgressBar(Descarga)
        self.proceso.setCursor(QtCore.Qt.WaitCursor)
        self.proceso.setStyleSheet("#proceso{\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(255, 255, 255)\n"
"}\n"
"#proceso:chunk{\n"
"    border-radius:3px;\n"
"    background-color: rgb(29, 202, 197)\n"
"}")
        self.proceso.setMaximum(100)
        self.proceso.setProperty("value", 0)
        self.proceso.setAlignment(QtCore.Qt.AlignCenter)
        self.proceso.setTextVisible(True)
        self.proceso.setObjectName("proceso")
        self.verticalLayout.addWidget(self.proceso)
        spacerItem1 = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.boton_inicio = QtWidgets.QPushButton(Descarga)
        self.boton_inicio.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_inicio.setFont(font)
        self.boton_inicio.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_inicio.setStyleSheet("#boton_inicio {\n"
"    border: 1px solid rgb(78, 104, 255);\n"
"    padding: 8px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(54, 72, 177);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#boton_inicio:hover {\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4e68ff\n"
"}\n"
"#boton_inicio:disabled {\n"
"    border: 1px solid rgb(203, 203, 203);\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.boton_inicio.setObjectName("boton_inicio")
        self.horizontalLayout.addWidget(self.boton_inicio)
        spacerItem3 = QtWidgets.QSpacerItem(17, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.boton_salir = QtWidgets.QPushButton(Descarga)
        self.boton_salir.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_salir.setFont(font)
        self.boton_salir.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_salir.setStyleSheet("#boton_salir {\n"
"    border: 1px solid rgb(255, 76, 76);\n"
"    padding: 8px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(200, 59, 59);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#boton_salir:hover {\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #ff4c4c;\n"
"}\n"
"#boton_salir:disabled {\n"
"    border: 1px solid rgb(203, 203, 203);\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.boton_salir.setObjectName("boton_salir")
        self.horizontalLayout.addWidget(self.boton_salir)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Descarga)
        QtCore.QMetaObject.connectSlotsByName(Descarga)

    def retranslateUi(self, Descarga):
        Descarga.setWindowTitle(QtWidgets.QApplication.translate("Descarga", "Frame", None, -1))
        self.label_titulo.setText(QtWidgets.QApplication.translate("Descarga", "Descargando...", None, -1))
        self.label_subtitulo.setText(QtWidgets.QApplication.translate("Descarga", "Iniciando Descarga...", None, -1))
        self.boton_inicio.setText(QtWidgets.QApplication.translate("Descarga", "Inicio", None, -1))
        self.boton_salir.setText(QtWidgets.QApplication.translate("Descarga", "Salir", None, -1))

