from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import QIcon, QFont
from os.path import abspath, join, dirname

from config.ventana_principal.design.ventana_principal import Ui_App
from ..ventana1.ventana1 import FrameAnadirCanciones
from ..ventana2.ventana2 import FrameUblicacion
from ..ventana3.ventana3 import Frame_Formatos
from ..ventana4.ventana4 import FrameDescarga


class App(Ui_App, QMainWindow):

    def __init__(self, fonts, state):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(abspath(join(dirname(dirname(dirname(__file__))), "config", "ventana_principal", "assets", "icono.ico"))))
        self.setWindowTitle("MusicDw")
        self.splitter.setStretchFactor(1, 1)
        self.line.setStyleSheet("""
            color: #84ADE7;
            background-color: rgb(173, 200, 239);
        """)
        self.label_titulo_app.setFont(QFont(fonts[1][0], 19, QFont.Bold))
        self.label_current_proceso.setFont(QFont(fonts[1][0], 24, QFont.Bold))
        self.label_pasos.setFont(QFont(fonts[0][0], 20))
        self.label_anadir_canciones.setFont(QFont(fonts[1][0], 10))
        self.label_ublicacion.setFont(QFont(fonts[1][0], 10))
        self.label_tipo_formato.setFont(QFont(fonts[1][0], 10))
        self.label_descarga.setFont(QFont(fonts[1][0], 10))
        self.stackedWidget.setCurrentWidget(self.paso1)
        self.label_current_proceso.setText("Añadir Canciones")
        self.layout_paso1.addWidget(FrameAnadirCanciones(fonts, self, state))
        self.layout_paso2.addWidget(FrameUblicacion(fonts, self, state))
        self.layout_paso3.addWidget(Frame_Formatos(fonts, self, state))
        self.layout_paso4.addWidget(FrameDescarga(fonts, self, state))
