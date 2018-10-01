# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Ui_Proceso.ui',
# licensing of 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Ui_Proceso.ui' applies.
#
# Created: Mon Oct  1 12:20:30 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ui_Proceso(object):
    def setupUi(self, Ui_Proceso):
        Ui_Proceso.setObjectName("Ui_Proceso")
        Ui_Proceso.setEnabled(True)
        Ui_Proceso.resize(518, 252)
        Ui_Proceso.setStyleSheet("#Ui_Proceso {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Ui_Proceso)
        self.verticalLayout_2.setSpacing(13)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titulo = QtWidgets.QLabel(Ui_Proceso)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(49)
        font.setWeight(50)
        font.setBold(False)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(94, 94, 94);")
        self.titulo.setObjectName("titulo")
        self.verticalLayout_2.addWidget(self.titulo)
        spacerItem = QtWidgets.QSpacerItem(19, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.descripcion_proceso = QtWidgets.QLabel(Ui_Proceso)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(11)
        self.descripcion_proceso.setFont(font)
        self.descripcion_proceso.setStyleSheet("color: rgb(130, 130, 130);")
        self.descripcion_proceso.setObjectName("descripcion_proceso")
        self.verticalLayout.addWidget(self.descripcion_proceso)
        self.proceso = QtWidgets.QProgressBar(Ui_Proceso)
        self.proceso.setStyleSheet("#proceso{\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgb(235, 235, 235);\n"
"    background-color: rgb(255, 255, 255)\n"
"}\n"
"#proceso:chunk{\n"
"    border-radius:3px;\n"
"    background-color: rgb(29, 202, 197)\n"
"}")
        self.proceso.setMaximum(0)
        self.proceso.setProperty("value", -1)
        self.proceso.setAlignment(QtCore.Qt.AlignCenter)
        self.proceso.setTextVisible(False)
        self.proceso.setObjectName("proceso")
        self.verticalLayout.addWidget(self.proceso)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.boton_volver = QtWidgets.QPushButton(Ui_Proceso)
        self.boton_volver.setEnabled(False)
        self.boton_volver.setMinimumSize(QtCore.QSize(109, 37))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.boton_volver.setFont(font)
        self.boton_volver.setStyleSheet("#boton_volver{\n"
"border-right: 2px solid rgb(93, 93, 93);\n"
"border-bottom: 2px solid rgb(93, 93, 93);\n"
"border-left: 1px solid rgb(172, 172, 172);\n"
"border-top: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"color: rgb(93, 93, 93);\n"
"}\n"
"#boton_volver:pressed {\n"
"border-left: 2px solid rgb(93, 93, 93);\n"
"border-top: 2px solid rgb(93, 93, 93);\n"
"border-right: 1px solid rgb(172, 172, 172);\n"
"border-bottom:1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"color: rgb(93, 93, 93);\n"
"}\n"
"#boton_volver:disabled {\n"
"border-left: 1px solid rgb(235, 235, 235);\n"
"border-top: 1px solid rgb(235, 235, 235);\n"
"border-right: 1px solid rgb(235, 235, 235);\n"
"border-bottom:1px solid rgb(235, 235, 235);\n"
"border-radius: 5px;\n"
"color: rgb(204, 204, 204)\n"
"}")
        self.boton_volver.setObjectName("boton_volver")
        self.horizontalLayout.addWidget(self.boton_volver)
        self.boton_salir = QtWidgets.QPushButton(Ui_Proceso)
        self.boton_salir.setEnabled(False)
        self.boton_salir.setMinimumSize(QtCore.QSize(109, 37))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.boton_salir.setFont(font)
        self.boton_salir.setStyleSheet("#boton_salir{\n"
"border-right: 3px solid rgb(121, 53, 21);\n"
"border-bottom: 3px solid rgb(121, 53, 21);\n"
"border-left: 1px solid rgb(172, 172, 172);\n"
"border-top: 1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"color: rgb(121, 53, 21);\n"
"}\n"
"#boton_salir:pressed {\n"
"border-left: 3px solid rgb(121, 53, 21);\n"
"border-top: 3px solid rgb(121, 53, 21);\n"
"border-right: 1px solid rgb(172, 172, 172);\n"
"border-bottom:1px solid rgb(172, 172, 172);\n"
"border-radius: 5px;\n"
"color: rgb(121, 53, 21);\n"
"}\n"
"#boton_salir:disabled {\n"
"border-left: 1px solid rgb(235, 235, 235);\n"
"border-top: 1px solid rgb(235, 235, 235);\n"
"border-right: 1px solid rgb(235, 235, 235);\n"
"border-bottom:1px solid rgb(235, 235, 235);\n"
"border-radius: 5px;\n"
"color: rgb(204, 204, 204)\n"
"}")
        self.boton_salir.setObjectName("boton_salir")
        self.horizontalLayout.addWidget(self.boton_salir)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Ui_Proceso)
        QtCore.QMetaObject.connectSlotsByName(Ui_Proceso)
        Ui_Proceso.setTabOrder(self.boton_volver, self.boton_salir)

    def retranslateUi(self, Ui_Proceso):
        Ui_Proceso.setWindowTitle(QtWidgets.QApplication.translate("Ui_Proceso", "Music Download - Descargando y Convirtiendo", None, -1))
        self.titulo.setText(QtWidgets.QApplication.translate("Ui_Proceso", "Manos a la Obra  ", None, -1))
        self.descripcion_proceso.setText(QtWidgets.QApplication.translate("Ui_Proceso", "Descargando y convertiendo en el formato solicitado...", None, -1))
        self.boton_volver.setText(QtWidgets.QApplication.translate("Ui_Proceso", "Volver", None, -1))
        self.boton_salir.setText(QtWidgets.QApplication.translate("Ui_Proceso", "Salir", None, -1))

