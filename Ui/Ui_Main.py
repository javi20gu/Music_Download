# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Main.ui',
# licensing of 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Main.ui' applies.
#
# Created: Sun Sep 30 13:32:56 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ui_Main(object):
    def setupUi(self, Ui_Main):
        Ui_Main.setObjectName("Ui_Main")
        Ui_Main.resize(758, 496)
        font = QtGui.QFont()
        font.setPointSize(11)
        Ui_Main.setFont(font)
        Ui_Main.setStyleSheet("#Ui_Main{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Ui_Main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_titulo = QtWidgets.QVBoxLayout()
        self.layout_titulo.setSpacing(5)
        self.layout_titulo.setObjectName("layout_titulo")
        self.titulo = QtWidgets.QLabel(Ui_Main)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(49)
        font.setWeight(50)
        font.setBold(False)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(94, 94, 94);")
        self.titulo.setObjectName("titulo")
        self.layout_titulo.addWidget(self.titulo)
        self.proceso = QtWidgets.QProgressBar(Ui_Main)
        self.proceso.setMinimumSize(QtCore.QSize(0, 5))
        self.proceso.setMaximumSize(QtCore.QSize(10000000, 5))
        self.proceso.setStyleSheet("#proceso{\n"
"    border-radius:2px;\n"
"    background-color: rgb(245, 245, 245);\n"
"}\n"
"#proceso:chunk{\n"
"    border-radius:2px;\n"
"    background-color: rgb(29, 202, 197)\n"
"}")
        self.proceso.setProperty("value", 25)
        self.proceso.setAlignment(QtCore.Qt.AlignCenter)
        self.proceso.setTextVisible(False)
        self.proceso.setObjectName("proceso")
        self.layout_titulo.addWidget(self.proceso)
        self.verticalLayout.addLayout(self.layout_titulo)
        spacerItem = QtWidgets.QSpacerItem(719, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.descripcion_lista = QtWidgets.QLabel(Ui_Main)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        self.descripcion_lista.setFont(font)
        self.descripcion_lista.setStyleSheet("color: rgb(130, 130, 130);")
        self.descripcion_lista.setObjectName("descripcion_lista")
        self.verticalLayout.addWidget(self.descripcion_lista)
        self.lista_elementos = QtWidgets.QListWidget(Ui_Main)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setWeight(50)
        font.setBold(False)
        self.lista_elementos.setFont(font)
        self.lista_elementos.setStyleSheet("color: rgb(103, 103, 103);")
        self.lista_elementos.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lista_elementos.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lista_elementos.setObjectName("lista_elementos")
        self.verticalLayout.addWidget(self.lista_elementos)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_anadir = QtWidgets.QPushButton(Ui_Main)
        self.boton_anadir.setEnabled(True)
        self.boton_anadir.setMinimumSize(QtCore.QSize(102, 33))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.boton_anadir.setFont(font)
        self.boton_anadir.setStyleSheet("#boton_anadir{\n"
"border: 2px solid rgb(97, 97, 97);\n"
"border-radius: 5px;\n"
"color:#616161\n"
"}\n"
"#boton_anadir:hover {\n"
"border: 2px solid #616161;\n"
"border-radius: 5px;\n"
"background-color: #616161;\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"#boton_anadir:disabled {\n"
"border-left: 1px solid rgb(235, 235, 235);\n"
"border-top: 1px solid rgb(235, 235, 235);\n"
"border-right: 1px solid rgb(235, 235, 235);\n"
"border-bottom:1px solid rgb(235, 235, 235);\n"
"border-radius: 5px;\n"
"color: rgb(204, 204, 204)\n"
"}")
        self.boton_anadir.setObjectName("boton_anadir")
        self.horizontalLayout.addWidget(self.boton_anadir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.boton_borrar = QtWidgets.QPushButton(Ui_Main)
        self.boton_borrar.setEnabled(False)
        self.boton_borrar.setMinimumSize(QtCore.QSize(102, 33))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.boton_borrar.setFont(font)
        self.boton_borrar.setStyleSheet("#boton_borrar{\n"
"border: 2px solid rgb(97, 97, 97);\n"
"border-radius: 5px;\n"
"color:#616161\n"
"}\n"
"#boton_borrar:hover {\n"
"border: 2px solid #616161;\n"
"border-radius: 5px;\n"
"background-color: #616161;\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"#boton_borrar:disabled {\n"
"border-left: 1px solid rgb(235, 235, 235);\n"
"border-top: 1px solid rgb(235, 235, 235);\n"
"border-right: 1px solid rgb(235, 235, 235);\n"
"border-bottom:1px solid rgb(235, 235, 235);\n"
"border-radius: 5px;\n"
"color: rgb(204, 204, 204)\n"
"}")
        self.boton_borrar.setObjectName("boton_borrar")
        self.horizontalLayout.addWidget(self.boton_borrar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.layout_botones = QtWidgets.QHBoxLayout()
        self.layout_botones.setObjectName("layout_botones")
        spacerItem3 = QtWidgets.QSpacerItem(0, 37, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_botones.addItem(spacerItem3)
        self.cancelar = QtWidgets.QPushButton(Ui_Main)
        self.cancelar.setMinimumSize(QtCore.QSize(109, 37))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.cancelar.setFont(font)
        self.cancelar.setStyleSheet("#cancelar {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 4px;\n"
"    color: rgb(102, 102, 102)\n"
"}\n"
"#cancelar:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    background-color: rgb(112, 112, 112);\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.cancelar.setObjectName("cancelar")
        self.layout_botones.addWidget(self.cancelar)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.layout_botones.addItem(spacerItem4)
        self.siguiente = QtWidgets.QPushButton(Ui_Main)
        self.siguiente.setEnabled(False)
        self.siguiente.setMinimumSize(QtCore.QSize(109, 37))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.siguiente.setFont(font)
        self.siguiente.setStyleSheet("#siguiente{\n"
"border: 2px solid #00C53B;\n"
"border-radius: 5px;\n"
"color: #00C53B;\n"
"}\n"
"#siguiente:hover {\n"
"border: 2px solid #00C53B;\n"
"border-radius: 5px;\n"
"background-color: rgb(0, 197, 59);\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"#siguiente:disabled {\n"
"border-left: 1px solid rgb(235, 235, 235);\n"
"border-top: 1px solid rgb(235, 235, 235);\n"
"border-right: 1px solid rgb(235, 235, 235);\n"
"border-bottom:1px solid rgb(235, 235, 235);\n"
"border-radius: 5px;\n"
"color: rgb(204, 204, 204)\n"
"}")
        self.siguiente.setObjectName("siguiente")
        self.layout_botones.addWidget(self.siguiente)
        self.verticalLayout.addLayout(self.layout_botones)
        self.descripcion_lista.setBuddy(self.lista_elementos)

        self.retranslateUi(Ui_Main)
        QtCore.QMetaObject.connectSlotsByName(Ui_Main)
        Ui_Main.setTabOrder(self.lista_elementos, self.boton_anadir)
        Ui_Main.setTabOrder(self.boton_anadir, self.boton_borrar)
        Ui_Main.setTabOrder(self.boton_borrar, self.cancelar)
        Ui_Main.setTabOrder(self.cancelar, self.siguiente)

    def retranslateUi(self, Ui_Main):
        Ui_Main.setWindowTitle(QtWidgets.QApplication.translate("Ui_Main", "Music Download", None, -1))
        self.titulo.setText(QtWidgets.QApplication.translate("Ui_Main", "Bienvenido", None, -1))
        self.descripcion_lista.setText(QtWidgets.QApplication.translate("Ui_Main", "Para empezar, pulse el botón añadir para añadir canciones a la cola", None, -1))
        self.boton_anadir.setText(QtWidgets.QApplication.translate("Ui_Main", "Añadir", None, -1))
        self.boton_borrar.setText(QtWidgets.QApplication.translate("Ui_Main", "Borrar", None, -1))
        self.cancelar.setText(QtWidgets.QApplication.translate("Ui_Main", "Cancelar", None, -1))
        self.siguiente.setText(QtWidgets.QApplication.translate("Ui_Main", "Siguiente", None, -1))

