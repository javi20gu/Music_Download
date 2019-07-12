0
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Ventana1.ui',
# licensing of 'Ui_Ventana1.ui' applies.
#
# Created: Sun Jun 23 16:26:04 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Frame_Anadir_Cancion(object):
    def setupUi(self, Frame_Anadir_Cancion):
        Frame_Anadir_Cancion.setObjectName("Frame_Anadir_Cancion")
        Frame_Anadir_Cancion.resize(752, 456)
        Frame_Anadir_Cancion.setStyleSheet("#Frame_Anadir_Cancion {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Frame_Anadir_Cancion)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_titulo = QtWidgets.QLabel(Frame_Anadir_Cancion)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("color: rgb(85, 85, 85);")
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout_2.addWidget(self.label_titulo)
        self.label_subtitulo = QtWidgets.QLabel(Frame_Anadir_Cancion)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_subtitulo.setFont(font)
        self.label_subtitulo.setStyleSheet("color: rgb(134, 134, 134)")
        self.label_subtitulo.setObjectName("label_subtitulo")
        self.verticalLayout_2.addWidget(self.label_subtitulo)
        spacerItem = QtWidgets.QSpacerItem(0, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabla = QtWidgets.QTableWidget(Frame_Anadir_Cancion)
        self.tabla.setObjectName("tabla")
        self.tabla.setColumnCount(1)
        self.tabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(0, item)
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tabla)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_anadir = QtWidgets.QPushButton(Frame_Anadir_Cancion)
        self.boton_anadir.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_anadir.setFont(font)
        self.boton_anadir.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_anadir.setStyleSheet("#boton_anadir {\n"
"    border: 1px solid rgb(54, 209, 80);\n"
"    padding: 8px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(62, 175, 42);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#boton_anadir:hover {\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(54, 209, 80);\n"
"}\n"
"#boton_anadir:disabled {\n"
"    border: 1px solid rgb(203, 203, 203);\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.boton_anadir.setObjectName("boton_anadir")
        self.horizontalLayout.addWidget(self.boton_anadir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.boton_borrar = QtWidgets.QPushButton(Frame_Anadir_Cancion)
        self.boton_borrar.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        self.boton_borrar.setFont(font)
        self.boton_borrar.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_borrar.setStyleSheet("#boton_borrar {\n"
"    border: 1px solid rgb(255, 122, 112);\n"
"    padding: 8px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 122, 112);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#boton_borrar:hover {\n"
"    padding: 8px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 122, 112);\n"
"}\n"
"\n"
"#boton_borrar:disabled {\n"
"    border: 1px solid rgb(203, 203, 203);\n"
"    padding: 10px 30px;\n"
"    border-radius: 3px;\n"
"    color: rgb(207, 207, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.boton_borrar.setObjectName("boton_borrar")
        self.horizontalLayout.addWidget(self.boton_borrar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.boton_siguiente = QtWidgets.QPushButton(Frame_Anadir_Cancion)
        self.boton_siguiente.setEnabled(False)
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

        self.retranslateUi(Frame_Anadir_Cancion)
        QtCore.QMetaObject.connectSlotsByName(Frame_Anadir_Cancion)

    def retranslateUi(self, Frame_Anadir_Cancion):
        Frame_Anadir_Cancion.setWindowTitle(QtWidgets.QApplication.translate("Frame_Anadir_Cancion", "Frame", None, -1))
        self.label_titulo.setText(QtWidgets.QApplication.translate("Frame_Anadir_Cancion", "Bienvenido", None, -1))
        self.label_subtitulo.setText(QtWidgets.QApplication.translate("Frame_Anadir_Cancion", "Para empezar añada las canciones que quiera descargar", None, -1))
        self.tabla.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Frame_Anadir_Cancion", "Canciones", None, -1))
        self.boton_anadir.setText(QtWidgets.QApplication.translate("Frame_Anadir_Cancion", "Añadir", None, -1))
        self.boton_borrar.setText(QtWidgets.QApplication.translate("Frame_Anadir_Cancion", "Borrar", None, -1))
        self.boton_siguiente.setText(QtWidgets.QApplication.translate("Frame_Anadir_Cancion", "Siguiente", None, -1))

