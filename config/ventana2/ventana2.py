from PySide2.QtWidgets import QFrame, QMainWindow, QFileDialog
from PySide2.QtCore import Slot, QEvent
from PySide2.QtGui import QFont
from typing import List

from .design.ventana2 import Ui_Ventana2

class FrameUblicacion(Ui_Ventana2, QFrame):

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

    def __init__(self, fonts: List[str], padre, state):
        super().__init__()
        self.setupUi(self)
        from ..ventana_principal.ventana_principal import App
        from ..state import State
        self.state: State = state
        self.padre: App = padre 
        self.carpeta_output = ''
        self.label_titulo.setFont(QFont(fonts[0][0], 27))
        self.label_subtitulo.setFont(QFont(fonts[3][0], 10))
        self.boton_buscar.clicked.connect(self.buscar)
        self.boton_siguiente.clicked.connect(self.siguiente)

    @Slot(None)  
    def siguiente(self):
        self.state.set_state(directorio_guardar=self.carpeta_output)
        self.padre.stackedWidget.setCurrentWidget(self.padre.paso3)
        self.inputUblicacion.clear()

    @Slot(None)
    def buscar(self):
        self.carpeta_output = QFileDialog(self).getExistingDirectory()
        self.inputUblicacion.setText(self.carpeta_output)
        if self.carpeta_output == '':
            self.boton_siguiente.setDisabled(True)
        else:
            self.boton_siguiente.setDisabled(False)

    @Slot(QEvent)
    def showEvent(self, event: QEvent):
        self.padre.label_anadir_canciones.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_tipo_formato.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_descarga.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_ublicacion.setStyleSheet(self.STYLE["active"])
        self.carpeta_output = QFileDialog(self).getExistingDirectory()
        if self.carpeta_output == '':
            self.boton_siguiente.setDisabled(True)
        else:
            self.boton_siguiente.setDisabled(False)
        self.inputUblicacion.setText(self.carpeta_output)
        super().showEvent(event)
