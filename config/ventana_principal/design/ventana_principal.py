# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Ventana_Principal.ui',
# licensing of 'Ui_Ventana_Principal.ui' applies.
#
# Created: Wed Jul 10 20:54:12 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(1120, 612)
        App.setStyleSheet("#statusbar {\n"
"background-color: rgb(91, 145, 223);\n"
"color: rgb(118, 118, 118)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(App)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("background-color: rgb(91, 145, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_titulo_app = QtWidgets.QLabel(self.frame)
        self.label_titulo_app.setMinimumSize(QtCore.QSize(0, 78))
        self.label_titulo_app.setMaximumSize(QtCore.QSize(16777215, 73))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setWeight(75)
        font.setBold(True)
        self.label_titulo_app.setFont(font)
        self.label_titulo_app.setStyleSheet("color: rgb(27, 74, 140);\n"
"padding-left:10px;\n"
"padding-bottom: 7px\n"
"")
        self.label_titulo_app.setObjectName("label_titulo_app")
        self.verticalLayout_5.addWidget(self.label_titulo_app)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(132, 173, 231);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_pasos = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_pasos.setFont(font)
        self.label_pasos.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding-top:14px;\n"
"padding-left: 10px;")
        self.label_pasos.setObjectName("label_pasos")
        self.verticalLayout_3.addWidget(self.label_pasos)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("#frame_4 {\n"
"background-color: rgb(173, 200, 239);\n"
"margin-top:13px;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setMidLineWidth(-4)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setContentsMargins(25, 24, 25, 24)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_anadir_canciones = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_anadir_canciones.setFont(font)
        self.label_anadir_canciones.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(173, 200, 239);")
        self.label_anadir_canciones.setAlignment(QtCore.Qt.AlignCenter)
        self.label_anadir_canciones.setObjectName("label_anadir_canciones")
        self.verticalLayout_2.addWidget(self.label_anadir_canciones)
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setStyleSheet("color: #84ADE7;\n"
"background-color: rgb(173, 200, 239);\n"
"")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_ublicacion = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_ublicacion.setFont(font)
        self.label_ublicacion.setStyleSheet("color: rgb(214, 228, 247);\n"
"background-color: rgb(173, 200, 239);")
        self.label_ublicacion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ublicacion.setObjectName("label_ublicacion")
        self.verticalLayout_2.addWidget(self.label_ublicacion)
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setStyleSheet("#line_2\n"
"{\n"
"color: #84ADE7;\n"
"background-color: rgb(173, 200, 239);\n"
"}")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_tipo_formato = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_tipo_formato.setFont(font)
        self.label_tipo_formato.setStyleSheet("color: rgb(214, 228, 247);\n"
"background-color: rgb(173, 200, 239);")
        self.label_tipo_formato.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tipo_formato.setObjectName("label_tipo_formato")
        self.verticalLayout_2.addWidget(self.label_tipo_formato)
        self.line_3 = QtWidgets.QFrame(self.frame_4)
        self.line_3.setStyleSheet("#line_3\n"
"{\n"
"color: #84ADE7;\n"
"background-color: rgb(173, 200, 239);\n"
"}")
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_descarga = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_descarga.setFont(font)
        self.label_descarga.setStyleSheet("color: #D6E4F7;\n"
"background-color: rgb(173, 200, 239);")
        self.label_descarga.setAlignment(QtCore.Qt.AlignCenter)
        self.label_descarga.setObjectName("label_descarga")
        self.verticalLayout_2.addWidget(self.label_descarga)
        self.verticalLayout_3.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(20, 267, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setStyleSheet("#frame_2 \n"
"{\n"
"background-color: rgb(91, 145, 223);\n"
"border-left: 1px solid rgb(132, 173, 231);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_current_proceso = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_current_proceso.setFont(font)
        self.label_current_proceso.setStyleSheet("color: rgb(214, 228, 247);\n"
"margin-left: .1em")
        self.label_current_proceso.setObjectName("label_current_proceso")
        self.verticalLayout.addWidget(self.label_current_proceso)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.layoutWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.paso1 = QtWidgets.QWidget()
        self.paso1.setStyleSheet("#paso1 {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.paso1.setObjectName("paso1")
        self.layout_paso1 = QtWidgets.QVBoxLayout(self.paso1)
        self.layout_paso1.setSpacing(0)
        self.layout_paso1.setContentsMargins(9, 1, 9, 1)
        self.layout_paso1.setObjectName("layout_paso1")
        self.stackedWidget.addWidget(self.paso1)
        self.paso2 = QtWidgets.QWidget()
        self.paso2.setStyleSheet("#paso2{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.paso2.setObjectName("paso2")
        self.layout_paso2 = QtWidgets.QVBoxLayout(self.paso2)
        self.layout_paso2.setSpacing(0)
        self.layout_paso2.setContentsMargins(8, 0, 8, 0)
        self.layout_paso2.setObjectName("layout_paso2")
        self.stackedWidget.addWidget(self.paso2)
        self.paso3 = QtWidgets.QWidget()
        self.paso3.setStyleSheet("#paso3 {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.paso3.setObjectName("paso3")
        self.layout_paso3 = QtWidgets.QVBoxLayout(self.paso3)
        self.layout_paso3.setSpacing(0)
        self.layout_paso3.setContentsMargins(0, 0, 0, 0)
        self.layout_paso3.setObjectName("layout_paso3")
        self.stackedWidget.addWidget(self.paso3)
        self.paso4 = QtWidgets.QWidget()
        self.paso4.setStyleSheet("#paso4 {\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.paso4.setObjectName("paso4")
        self.layout_paso4 = QtWidgets.QVBoxLayout(self.paso4)
        self.layout_paso4.setSpacing(0)
        self.layout_paso4.setContentsMargins(0, 0, 0, 0)
        self.layout_paso4.setObjectName("layout_paso4")
        self.stackedWidget.addWidget(self.paso4)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_6.addWidget(self.splitter)
        App.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)

        self.retranslateUi(App)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        App.setWindowTitle(QtWidgets.QApplication.translate("App", "MainWindow", None, -1))
        self.label_titulo_app.setText(QtWidgets.QApplication.translate("App", "MusicDw", None, -1))
        self.label_pasos.setText(QtWidgets.QApplication.translate("App", "Proceso", None, -1))
        self.label_anadir_canciones.setText(QtWidgets.QApplication.translate("App", "Añadir Canciones", None, -1))
        self.label_ublicacion.setText(QtWidgets.QApplication.translate("App", "Ublicación", None, -1))
        self.label_tipo_formato.setText(QtWidgets.QApplication.translate("App", "Tipo de Formato", None, -1))
        self.label_descarga.setText(QtWidgets.QApplication.translate("App", "Descarga", None, -1))
        self.label_current_proceso.setText(QtWidgets.QApplication.translate("App", "Titulo", None, -1))

