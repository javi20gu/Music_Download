# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Ventana3.ui',
# licensing of 'Ui_Ventana3.ui' applies.
#
# Created: Thu Jul 11 17:14:39 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Formato(object):
    def setupUi(self, Formato):
        Formato.setObjectName("Formato")
        Formato.resize(832, 445)
        Formato.setStyleSheet("#Formato {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Formato)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(7, 7, 7, 24)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_titulo = QtWidgets.QLabel(Formato)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet("color: rgb(85, 85, 85);")
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout.addWidget(self.label_titulo)
        self.label_subtitulo = QtWidgets.QLabel(Formato)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_subtitulo.setFont(font)
        self.label_subtitulo.setStyleSheet("color: rgb(134, 134, 134)")
        self.label_subtitulo.setObjectName("label_subtitulo")
        self.verticalLayout.addWidget(self.label_subtitulo)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame_card_mp3 = QtWidgets.QFrame(Formato)
        self.frame_card_mp3.setMinimumSize(QtCore.QSize(181, 261))
        self.frame_card_mp3.setStyleSheet("#frame_card_mp3 {\n"
"border: 1px solid rgb(197, 197, 197);\n"
"border-radius: 15px\n"
"}")
        self.frame_card_mp3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_card_mp3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_card_mp3.setObjectName("frame_card_mp3")
        self.frame_card_arriba_mp3 = QtWidgets.QFrame(self.frame_card_mp3)
        self.frame_card_arriba_mp3.setGeometry(QtCore.QRect(0, 0, 181, 211))
        self.frame_card_arriba_mp3.setStyleSheet("#frame_card_arriba_mp3 {\n"
"border: 1px solid #777;\n"
"border-radius: 15px;\n"
"background-color: rgb(42, 98, 255);\n"
"}")
        self.frame_card_arriba_mp3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_card_arriba_mp3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_card_arriba_mp3.setObjectName("frame_card_arriba_mp3")
        self.icono_mp3 = QtWidgets.QLabel(self.frame_card_arriba_mp3)
        self.icono_mp3.setGeometry(QtCore.QRect(30, 60, 121, 121))
        self.icono_mp3.setText("")
        self.icono_mp3.setPixmap(QtGui.QPixmap("../../../../../Downloads/mp3(3).png"))
        self.icono_mp3.setScaledContents(True)
        self.icono_mp3.setObjectName("icono_mp3")
        self.titulo_mp3 = QtWidgets.QLabel(self.frame_card_arriba_mp3)
        self.titulo_mp3.setGeometry(QtCore.QRect(30, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.titulo_mp3.setFont(font)
        self.titulo_mp3.setStyleSheet("color: rgb(255, 255, 255);")
        self.titulo_mp3.setObjectName("titulo_mp3")
        self.boton_convertir_mp3 = QtWidgets.QPushButton(self.frame_card_mp3)
        self.boton_convertir_mp3.setGeometry(QtCore.QRect(2, 207, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.boton_convertir_mp3.setFont(font)
        self.boton_convertir_mp3.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_convertir_mp3.setStyleSheet("border: 0px solid black;\n"
"border-radius: 15px;\n"
"color: rgb(105, 105, 105);\n"
"padding-top:6px")
        self.boton_convertir_mp3.setObjectName("boton_convertir_mp3")
        self.horizontalLayout.addWidget(self.frame_card_mp3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.frame_card_mp4 = QtWidgets.QFrame(Formato)
        self.frame_card_mp4.setMinimumSize(QtCore.QSize(181, 261))
        self.frame_card_mp4.setStyleSheet("#frame_card_mp4 {\n"
"border: 1px solid rgb(197, 197, 197);\n"
"border-radius: 15px\n"
"}")
        self.frame_card_mp4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_card_mp4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_card_mp4.setObjectName("frame_card_mp4")
        self.frame_card_arriba_mp4 = QtWidgets.QFrame(self.frame_card_mp4)
        self.frame_card_arriba_mp4.setGeometry(QtCore.QRect(0, 0, 181, 211))
        self.frame_card_arriba_mp4.setStyleSheet("#frame_card_arriba_mp4 {\n"
"border: 1px solid #777;\n"
"border-radius: 15px;\n"
"background-color: #FFAB00;\n"
"}")
        self.frame_card_arriba_mp4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_card_arriba_mp4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_card_arriba_mp4.setObjectName("frame_card_arriba_mp4")
        self.icono_mp4 = QtWidgets.QLabel(self.frame_card_arriba_mp4)
        self.icono_mp4.setGeometry(QtCore.QRect(30, 60, 121, 121))
        self.icono_mp4.setText("")
        self.icono_mp4.setPixmap(QtGui.QPixmap("../../../../../Downloads/mp4.png"))
        self.icono_mp4.setScaledContents(True)
        self.icono_mp4.setObjectName("icono_mp4")
        self.titulo_mp4 = QtWidgets.QLabel(self.frame_card_arriba_mp4)
        self.titulo_mp4.setGeometry(QtCore.QRect(30, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.titulo_mp4.setFont(font)
        self.titulo_mp4.setStyleSheet("color: rgb(255, 255, 255);")
        self.titulo_mp4.setObjectName("titulo_mp4")
        self.boton_convertir_mp4 = QtWidgets.QPushButton(self.frame_card_mp4)
        self.boton_convertir_mp4.setGeometry(QtCore.QRect(2, 207, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.boton_convertir_mp4.setFont(font)
        self.boton_convertir_mp4.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_convertir_mp4.setStyleSheet("border: 0px solid black;\n"
"border-radius: 15px;\n"
"color: rgb(105, 105, 105);\n"
"padding-top:6px")
        self.boton_convertir_mp4.setObjectName("boton_convertir_mp4")
        self.horizontalLayout.addWidget(self.frame_card_mp4)
        spacerItem3 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.frame_card_mp4a = QtWidgets.QFrame(Formato)
        self.frame_card_mp4a.setMinimumSize(QtCore.QSize(181, 261))
        self.frame_card_mp4a.setStyleSheet("#frame_card_mp4a {\n"
"border: 1px solid rgb(197, 197, 197);\n"
"border-radius: 15px\n"
"}")
        self.frame_card_mp4a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_card_mp4a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_card_mp4a.setObjectName("frame_card_mp4a")
        self.frame_card_arriba_mp4a = QtWidgets.QFrame(self.frame_card_mp4a)
        self.frame_card_arriba_mp4a.setGeometry(QtCore.QRect(0, 0, 181, 211))
        self.frame_card_arriba_mp4a.setStyleSheet("#frame_card_arriba_mp4a {\n"
"border: 1px solid #777;\n"
"border-radius: 15px;\n"
"background-color: #D81A60\n"
"}")
        self.frame_card_arriba_mp4a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_card_arriba_mp4a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_card_arriba_mp4a.setObjectName("frame_card_arriba_mp4a")
        self.icono_mp4a = QtWidgets.QLabel(self.frame_card_arriba_mp4a)
        self.icono_mp4a.setGeometry(QtCore.QRect(30, 60, 121, 121))
        self.icono_mp4a.setText("")
        self.icono_mp4a.setPixmap(QtGui.QPixmap("../../../../../Downloads/m4a-simbolo-de-formato-de-archivo.png"))
        self.icono_mp4a.setScaledContents(True)
        self.icono_mp4a.setObjectName("icono_mp4a")
        self.titulo_mp4a = QtWidgets.QLabel(self.frame_card_arriba_mp4a)
        self.titulo_mp4a.setGeometry(QtCore.QRect(30, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.titulo_mp4a.setFont(font)
        self.titulo_mp4a.setStyleSheet("color: rgb(255, 255, 255);")
        self.titulo_mp4a.setObjectName("titulo_mp4a")
        self.boton_convertir_mp4a = QtWidgets.QPushButton(self.frame_card_mp4a)
        self.boton_convertir_mp4a.setGeometry(QtCore.QRect(2, 207, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.boton_convertir_mp4a.setFont(font)
        self.boton_convertir_mp4a.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_convertir_mp4a.setStyleSheet("border: 0px solid black;\n"
"border-radius: 15px;\n"
"color: rgb(105, 105, 105);\n"
"padding-top:6px")
        self.boton_convertir_mp4a.setObjectName("boton_convertir_mp4a")
        self.horizontalLayout.addWidget(self.frame_card_mp4a)
        spacerItem4 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Formato)
        QtCore.QMetaObject.connectSlotsByName(Formato)

    def retranslateUi(self, Formato):
        Formato.setWindowTitle(QtWidgets.QApplication.translate("Formato", "Frame", None, -1))
        self.label_titulo.setText(QtWidgets.QApplication.translate("Formato", "Tipos de Formatos", None, -1))
        self.label_subtitulo.setText(QtWidgets.QApplication.translate("Formato", "Selecione el formato que quiera descargar", None, -1))
        self.titulo_mp3.setText(QtWidgets.QApplication.translate("Formato", "Formato Mp3", None, -1))
        self.boton_convertir_mp3.setText(QtWidgets.QApplication.translate("Formato", "Convertir", None, -1))
        self.titulo_mp4.setText(QtWidgets.QApplication.translate("Formato", "Formato Mp4", None, -1))
        self.boton_convertir_mp4.setText(QtWidgets.QApplication.translate("Formato", "Convertir", None, -1))
        self.titulo_mp4a.setText(QtWidgets.QApplication.translate("Formato", "Formato Mp4a", None, -1))
        self.boton_convertir_mp4a.setText(QtWidgets.QApplication.translate("Formato", "Convertir", None, -1))

