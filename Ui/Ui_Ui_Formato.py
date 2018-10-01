# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Ui_Formato.ui',
# licensing of 'c:\Users\javie\Desktop\Nueva carpeta\Ui\Ui_Formato.ui' applies.
#
# Created: Fri Sep 28 16:36:50 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Ui_Loanding(object):
    def setupUi(self, Ui_Loanding):
        Ui_Loanding.setObjectName("Ui_Loanding")
        Ui_Loanding.resize(528, 377)
        Ui_Loanding.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Ui_Loanding)
        self.verticalLayout_7.setSpacing(13)
        self.verticalLayout_7.setContentsMargins(11, 0, 16, 14)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.layout_titulo = QtWidgets.QVBoxLayout()
        self.layout_titulo.setSpacing(5)
        self.layout_titulo.setObjectName("layout_titulo")
        self.titulo = QtWidgets.QLabel(Ui_Loanding)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(49)
        font.setWeight(50)
        font.setBold(False)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(94, 94, 94);")
        self.titulo.setObjectName("titulo")
        self.layout_titulo.addWidget(self.titulo)
        self.proceso = QtWidgets.QProgressBar(Ui_Loanding)
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
        self.proceso.setProperty("value", 75)
        self.proceso.setAlignment(QtCore.Qt.AlignCenter)
        self.proceso.setTextVisible(False)
        self.proceso.setObjectName("proceso")
        self.layout_titulo.addWidget(self.proceso)
        self.verticalLayout_7.addLayout(self.layout_titulo)
        spacerItem = QtWidgets.QSpacerItem(41, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.descripcion_formato = QtWidgets.QLabel(Ui_Loanding)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        self.descripcion_formato.setFont(font)
        self.descripcion_formato.setStyleSheet("color: rgb(130, 130, 130);")
        self.descripcion_formato.setObjectName("descripcion_formato")
        self.verticalLayout_7.addWidget(self.descripcion_formato)
        self.layout_botones_formatos = QtWidgets.QHBoxLayout()
        self.layout_botones_formatos.setSpacing(34)
        self.layout_botones_formatos.setObjectName("layout_botones_formatos")
        self.marco_mp3 = QtWidgets.QFrame(Ui_Loanding)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_mp3.sizePolicy().hasHeightForWidth())
        self.marco_mp3.setSizePolicy(sizePolicy)
        self.marco_mp3.setMaximumSize(QtCore.QSize(114, 180))
        self.marco_mp3.setStyleSheet("#marco_mp3{\n"
"border: 1px solid rgb(213, 213, 213);\n"
"border-radius: 4px\n"
"}")
        self.marco_mp3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marco_mp3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marco_mp3.setObjectName("marco_mp3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.marco_mp3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.marco_titulo_mp3 = QtWidgets.QFrame(self.marco_mp3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_titulo_mp3.sizePolicy().hasHeightForWidth())
        self.marco_titulo_mp3.setSizePolicy(sizePolicy)
        self.marco_titulo_mp3.setStyleSheet("#marco_titulo_mp3{\n"
"border-radius: 4px;\n"
"}")
        self.marco_titulo_mp3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marco_titulo_mp3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marco_titulo_mp3.setObjectName("marco_titulo_mp3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.marco_titulo_mp3)
        self.verticalLayout.setContentsMargins(0, 11, 0, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imagenMp3 = QtWidgets.QLabel(self.marco_titulo_mp3)
        self.imagenMp3.setMinimumSize(QtCore.QSize(0, 7))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.imagenMp3.setFont(font)
        self.imagenMp3.setStyleSheet("color: rgb(104, 104, 104);\n"
"background-color:transparent")
        self.imagenMp3.setText("")
        self.imagenMp3.setScaledContents(True)
        self.imagenMp3.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenMp3.setObjectName("imagenMp3")
        self.verticalLayout.addWidget(self.imagenMp3)
        self.verticalLayout_2.addWidget(self.marco_titulo_mp3)
        self.boton_mp3 = QtWidgets.QPushButton(self.marco_mp3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_mp3.sizePolicy().hasHeightForWidth())
        self.boton_mp3.setSizePolicy(sizePolicy)
        self.boton_mp3.setMinimumSize(QtCore.QSize(0, 39))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.boton_mp3.setFont(font)
        self.boton_mp3.setStyleSheet("#boton_mp3 {\n"
"    border-top: 1px dotted  #3C4859;\n"
"    border-radius: 4px;\n"
"    color: #3C4859;\n"
"    background-color: rgb(249, 249, 249);\n"
"}\n"
"#boton_mp3:hover{\n"
"    background-color: rgb(113, 190, 161);\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.boton_mp3.setObjectName("boton_mp3")
        self.verticalLayout_2.addWidget(self.boton_mp3)
        self.layout_botones_formatos.addWidget(self.marco_mp3)
        spacerItem1 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_botones_formatos.addItem(spacerItem1)
        self.marco_mp4a = QtWidgets.QFrame(Ui_Loanding)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_mp4a.sizePolicy().hasHeightForWidth())
        self.marco_mp4a.setSizePolicy(sizePolicy)
        self.marco_mp4a.setMaximumSize(QtCore.QSize(121, 180))
        self.marco_mp4a.setStyleSheet("#marco_mp4a{\n"
"border: 1px solid rgb(213, 213, 213);\n"
"border-radius: 4px\n"
"}")
        self.marco_mp4a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marco_mp4a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marco_mp4a.setObjectName("marco_mp4a")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.marco_mp4a)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.marco_titulo_mp4a = QtWidgets.QFrame(self.marco_mp4a)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_titulo_mp4a.sizePolicy().hasHeightForWidth())
        self.marco_titulo_mp4a.setSizePolicy(sizePolicy)
        self.marco_titulo_mp4a.setStyleSheet("#marco_titulo_mp4a{\n"
"border-radius: 4px;\n"
"}")
        self.marco_titulo_mp4a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marco_titulo_mp4a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marco_titulo_mp4a.setObjectName("marco_titulo_mp4a")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.marco_titulo_mp4a)
        self.verticalLayout_4.setContentsMargins(0, 11, 0, 11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.imagenMp4A = QtWidgets.QLabel(self.marco_titulo_mp4a)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.imagenMp4A.setFont(font)
        self.imagenMp4A.setStyleSheet("color: rgb(104, 104, 104);\n"
"background-color:transparent")
        self.imagenMp4A.setText("")
        self.imagenMp4A.setScaledContents(True)
        self.imagenMp4A.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenMp4A.setObjectName("imagenMp4A")
        self.verticalLayout_4.addWidget(self.imagenMp4A)
        self.verticalLayout_3.addWidget(self.marco_titulo_mp4a)
        self.boton_mp4a = QtWidgets.QPushButton(self.marco_mp4a)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_mp4a.sizePolicy().hasHeightForWidth())
        self.boton_mp4a.setSizePolicy(sizePolicy)
        self.boton_mp4a.setMinimumSize(QtCore.QSize(0, 39))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.boton_mp4a.setFont(font)
        self.boton_mp4a.setStyleSheet("#boton_mp4a {\n"
"    border-top: 1px dotted  #3C4859;\n"
"    border-radius: 4px;\n"
"    color: #3C4859;\n"
"    background-color: rgb(249, 249, 249);\n"
"}\n"
"#boton_mp4a:hover{\n"
"    background-color: rgb(113, 190, 161);\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.boton_mp4a.setObjectName("boton_mp4a")
        self.verticalLayout_3.addWidget(self.boton_mp4a)
        self.layout_botones_formatos.addWidget(self.marco_mp4a)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_botones_formatos.addItem(spacerItem2)
        self.marco_mp4 = QtWidgets.QFrame(Ui_Loanding)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.marco_mp4.sizePolicy().hasHeightForWidth())
        self.marco_mp4.setSizePolicy(sizePolicy)
        self.marco_mp4.setMaximumSize(QtCore.QSize(115, 180))
        self.marco_mp4.setStyleSheet("#marco_mp4{\n"
"border: 1px solid rgb(213, 213, 213);\n"
"border-radius: 4px\n"
"}")
        self.marco_mp4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marco_mp4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marco_mp4.setObjectName("marco_mp4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.marco_mp4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.marco_titulo_mp4 = QtWidgets.QFrame(self.marco_mp4)
        self.marco_titulo_mp4.setStyleSheet("#marco_titulo_mp4{\n"
"border-radius: 4px;\n"
"}")
        self.marco_titulo_mp4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marco_titulo_mp4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marco_titulo_mp4.setObjectName("marco_titulo_mp4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.marco_titulo_mp4)
        self.verticalLayout_6.setContentsMargins(0, 11, 0, 11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.imagenMp4 = QtWidgets.QLabel(self.marco_titulo_mp4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(25)
        font.setWeight(75)
        font.setBold(True)
        self.imagenMp4.setFont(font)
        self.imagenMp4.setStyleSheet("color: rgb(104, 104, 104);\n"
"background-color:transparent")
        self.imagenMp4.setText("")
        self.imagenMp4.setScaledContents(True)
        self.imagenMp4.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenMp4.setObjectName("imagenMp4")
        self.verticalLayout_6.addWidget(self.imagenMp4)
        self.verticalLayout_5.addWidget(self.marco_titulo_mp4)
        self.boton_mp4 = QtWidgets.QPushButton(self.marco_mp4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_mp4.sizePolicy().hasHeightForWidth())
        self.boton_mp4.setSizePolicy(sizePolicy)
        self.boton_mp4.setMinimumSize(QtCore.QSize(0, 39))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.boton_mp4.setFont(font)
        self.boton_mp4.setStyleSheet("#boton_mp4 {\n"
"    border-top: 1px dotted  #3C4859;\n"
"    border-radius: 4px;\n"
"    color: #3C4859;\n"
"    background-color: rgb(249, 249, 249);\n"
"}\n"
"#boton_mp4:hover{\n"
"    background-color: rgb(113, 190, 161);\n"
"    border-radius: 4px;\n"
"    color: rgb(255, 255, 255)\n"
"}")
        self.boton_mp4.setObjectName("boton_mp4")
        self.verticalLayout_5.addWidget(self.boton_mp4)
        self.layout_botones_formatos.addWidget(self.marco_mp4)
        self.verticalLayout_7.addLayout(self.layout_botones_formatos)

        self.retranslateUi(Ui_Loanding)
        QtCore.QMetaObject.connectSlotsByName(Ui_Loanding)

    def retranslateUi(self, Ui_Loanding):
        Ui_Loanding.setWindowTitle(QtWidgets.QApplication.translate("Ui_Loanding", "Music Dowload - Formato", None, -1))
        self.titulo.setText(QtWidgets.QApplication.translate("Ui_Loanding", "Conversión", None, -1))
        self.descripcion_formato.setText(QtWidgets.QApplication.translate("Ui_Loanding", "Por ultimo elige el formato por el que quieres descargar:", None, -1))
        self.boton_mp3.setText(QtWidgets.QApplication.translate("Ui_Loanding", "Seleccionar", None, -1))
        self.boton_mp4a.setText(QtWidgets.QApplication.translate("Ui_Loanding", "Seleccionar", None, -1))
        self.boton_mp4.setText(QtWidgets.QApplication.translate("Ui_Loanding", "Seleccionar", None, -1))

