# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Ui_Localización.ui',
# licensing of 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Ui_Localización.ui' applies.
#
# Created: Mon Oct  1 00:03:01 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ui_Localizacin(object):
    def setupUi(self, Ui_Localizacin):
        Ui_Localizacin.setObjectName("Ui_Localizacin")
        Ui_Localizacin.resize(637, 328)
        Ui_Localizacin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Ui_Localizacin)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layout_titulo = QtWidgets.QVBoxLayout()
        self.layout_titulo.setSpacing(5)
        self.layout_titulo.setObjectName("layout_titulo")
        self.titulo = QtWidgets.QLabel(Ui_Localizacin)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(49)
        font.setWeight(50)
        font.setBold(False)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(94, 94, 94);")
        self.titulo.setObjectName("titulo")
        self.layout_titulo.addWidget(self.titulo)
        self.proceso = QtWidgets.QProgressBar(Ui_Localizacin)
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
        self.proceso.setProperty("value", 50)
        self.proceso.setAlignment(QtCore.Qt.AlignCenter)
        self.proceso.setTextVisible(False)
        self.proceso.setObjectName("proceso")
        self.layout_titulo.addWidget(self.proceso)
        self.verticalLayout_2.addLayout(self.layout_titulo)
        spacerItem = QtWidgets.QSpacerItem(96, 23, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.layout_destino = QtWidgets.QVBoxLayout()
        self.layout_destino.setObjectName("layout_destino")
        self.label_2 = QtWidgets.QLabel(Ui_Localizacin)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(130, 130, 130);")
        self.label_2.setObjectName("label_2")
        self.layout_destino.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(Ui_Localizacin)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 3px;\n"
"border: 1px solid rgb(112, 112, 112);\n"
"padding-left: 6px;")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.layout_destino.addWidget(self.lineEdit)
        self.layout_destino_boton = QtWidgets.QHBoxLayout()
        self.layout_destino_boton.setObjectName("layout_destino_boton")
        self.seleccionar = QtWidgets.QPushButton(Ui_Localizacin)
        self.seleccionar.setMinimumSize(QtCore.QSize(120, 37))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.seleccionar.setFont(font)
        self.seleccionar.setStyleSheet("#seleccionar {\n"
"    border: 2px solid rgb(49, 138, 158);\n"
"    border-radius: 4px;\n"
"    color: rgb(49, 138, 158);\n"
"}\n"
"#seleccionar:hover{\n"
"    border: 2px solid  rgb(49, 138, 158);\n"
"    background-color:rgb(49, 138, 158);\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.seleccionar.setObjectName("seleccionar")
        self.layout_destino_boton.addWidget(self.seleccionar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_destino_boton.addItem(spacerItem1)
        self.layout_destino.addLayout(self.layout_destino_boton)
        self.verticalLayout_2.addLayout(self.layout_destino)
        spacerItem2 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.layout_botones = QtWidgets.QHBoxLayout()
        self.layout_botones.setObjectName("layout_botones")
        spacerItem3 = QtWidgets.QSpacerItem(0, 37, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_botones.addItem(spacerItem3)
        self.boton_anterior = QtWidgets.QPushButton(Ui_Localizacin)
        self.boton_anterior.setMinimumSize(QtCore.QSize(109, 37))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.boton_anterior.setFont(font)
        self.boton_anterior.setStyleSheet("#boton_anterior {\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    border-radius: 4px;\n"
"    color: rgb(102, 102, 102)\n"
"}\n"
"#boton_anterior:hover{\n"
"    border: 2px solid  rgb(112, 112, 112);\n"
"    background-color: rgb(112, 112, 112);\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.boton_anterior.setObjectName("boton_anterior")
        self.layout_botones.addWidget(self.boton_anterior)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.layout_botones.addItem(spacerItem4)
        self.siguiente = QtWidgets.QPushButton(Ui_Localizacin)
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
        self.verticalLayout_2.addLayout(self.layout_botones)
        self.label_2.setBuddy(self.lineEdit)

        self.retranslateUi(Ui_Localizacin)
        QtCore.QMetaObject.connectSlotsByName(Ui_Localizacin)
        Ui_Localizacin.setTabOrder(self.lineEdit, self.seleccionar)
        Ui_Localizacin.setTabOrder(self.seleccionar, self.boton_anterior)
        Ui_Localizacin.setTabOrder(self.boton_anterior, self.siguiente)

    def retranslateUi(self, Ui_Localizacin):
        Ui_Localizacin.setWindowTitle(QtWidgets.QApplication.translate("Ui_Localizacin", "Music Download - Localización", None, -1))
        self.titulo.setText(QtWidgets.QApplication.translate("Ui_Localizacin", "Localización", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Ui_Localizacin", "Presiona el botón para selecionar el destino:", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Ui_Localizacin", "Destino", None, -1))
        self.seleccionar.setText(QtWidgets.QApplication.translate("Ui_Localizacin", "Seleccionar", None, -1))
        self.boton_anterior.setText(QtWidgets.QApplication.translate("Ui_Localizacin", "Anterior", None, -1))
        self.siguiente.setText(QtWidgets.QApplication.translate("Ui_Localizacin", "Siguiente", None, -1))

