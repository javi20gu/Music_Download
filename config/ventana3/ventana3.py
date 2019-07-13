from PySide2.QtGui import QFont, QPixmap
from PySide2.QtCore import QEvent, Slot
from PySide2.QtWidgets import QFrame
from os.path import join, abspath, dirname
from typing import List

from .design.ventana3 import Ui_Formato


class Frame_Formatos(Ui_Formato, QFrame):

    STYLE = {
        'active':
            """
            color: rgb(255, 255, 255);
            background-color: rgb(173, 200, 239);
            """,
        'desactive':
            """
            color: rgb(214, 228, 247);
            background-color: rgb(173, 200, 239);
            """}

    ruta_mp3  = abspath(join(dirname(dirname(dirname(__file__))), 'config', 'ventana3', 'asserts', 'mp3.png'))
    ruta_mp4  = abspath(join(dirname(dirname(dirname(__file__))), 'config', 'ventana3', 'asserts', 'mp4.png'))
    ruta_mp4a = abspath(join(dirname(dirname(dirname(__file__))), 'config', 'ventana3', 'asserts', 'm4a.png'))

    def __init__(self, fonts: List[str], padre, state):
        super().__init__()
        from ..ventana_principal.ventana_principal import App
        from ..state import State
        self.state: State = state
        self.padre: App = padre
        self.setupUi(self)
        self.label_titulo.setFont(QFont(fonts[0][0], 27))
        self.label_subtitulo.setFont(QFont(fonts[3][0], 10))

        self.frame_card_arriba_mp3.mousePressEvent = lambda event: self.convertirMp3()
        self.frame_card_arriba_mp4.mousePressEvent = lambda event: self.convertirMp4()
        self.frame_card_arriba_mp4a.mousePressEvent = lambda event: self.convertirMp4a()

        self.icono_mp3.setPixmap(QPixmap(f'{self.ruta_mp3}'))
        self.icono_mp4.setPixmap(QPixmap(f'{self.ruta_mp4}'))
        self.icono_mp4a.setPixmap(QPixmap(f'{self.ruta_mp4a}'))

        self.boton_convertir_mp3.setFont(QFont(fonts[2][0], 13))
        self.boton_convertir_mp4.setFont(QFont(fonts[2][0], 13))
        self.boton_convertir_mp4a.setFont(QFont(fonts[2][0], 13))

        self.boton_convertir_mp3.clicked.connect(self.convertirMp3)
        self.boton_convertir_mp4a.clicked.connect(self.convertirMp4a)
        self.boton_convertir_mp4.clicked.connect(self.convertirMp4)

    @Slot(None)
    def convertirMp3(self):
        self.state.set_state(tipo_formato='mp3')
        self.padre.stackedWidget.setCurrentWidget(self.padre.paso4)

    @Slot(None)
    def convertirMp4(self):
        self.state.set_state(tipo_formato='mp4')
        self.padre.stackedWidget.setCurrentWidget(self.padre.paso4)

    @Slot(None)
    def convertirMp4a(self):
        self.state.set_state(tipo_formato='mp4a')
        self.padre.stackedWidget.setCurrentWidget(self.padre.paso4)

    @Slot(QEvent)
    def showEvent(self, event: QEvent):
        self.padre.label_anadir_canciones.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_tipo_formato.setStyleSheet(self.STYLE["active"])
        self.padre.label_descarga.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_ublicacion.setStyleSheet(self.STYLE["desactive"])
