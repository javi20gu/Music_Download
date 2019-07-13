from PySide2.QtCore import QEvent, Slot, QThread, Qt
from PySide2.QtWidgets import QFrame, QMessageBox
from PySide2.QtGui import QFont, QCursor

from ..download import Download
from .design.ventana4 import Ui_Descarga


class FrameDescarga(Ui_Descarga, QFrame):

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

    def __init__(self, fonts: QFont, padre, state):
        super().__init__()
        from ..ventana_principal.ventana_principal import App
        from ..state import State
        self.state: State = state
        self.padre: App = padre
        self.erroneas = 0
        self.setupUi(self)

        self.label_titulo.setFont(QFont(fonts[0][0], 27))
        self.label_subtitulo.setFont(QFont(fonts[3][0], 10))
        self.boton_salir.clicked.connect(self.salir)
        self.boton_inicio.clicked.connect(self.inicio)

    #@Slot(QEvent)
    def showEvent(self, event: QEvent):
        self.proceso.setValue(0)
        self.boton_salir.setEnabled(False)
        self.boton_inicio.setEnabled(False)
        self.padre.label_anadir_canciones.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_tipo_formato.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_descarga.setStyleSheet(self.STYLE["active"])
        self.padre.label_ublicacion.setStyleSheet(self.STYLE["desactive"])
        super().showEvent(event)
        self.download = Download(self, self.state)
        self.download.start(QThread.HighPriority)
        self.download.status.connect(self.progress)
        self.download.is_error.connect(self.is_error)

    @Slot(str)
    def progress(self, porcentaje: str):
        if int(float(porcentaje.split("%")[0].strip())) == 100:
            self.label_subtitulo.setText("Eliminando fichero .webm (Puede durar unos minutos)...")
            self.proceso.setMaximum(0)
            self.proceso.setValue(-1)
        else:
            self.proceso.setMaximum(100)
            self.proceso.setValue(int(float(porcentaje.split("%")[0].strip())))

    @Slot(bool, str, int)
    @Slot(bool, None, int)
    def is_error(self, is_error: bool, error: str, total_canciones: int):
        
        if is_error:
            self.erroneas += 1
            QMessageBox.critical(self, 'MusicDw', f'Se ha producido un error: \n{error}')
        else:
            self.proceso.setMaximum(100)
            self.proceso.setValue(100)
            self.label_subtitulo.setText(f"Finalizado, Completadas: {total_canciones - self.erroneas} | Erroneas: {self.erroneas}")
            self.proceso.setCursor(Qt.ArrowCursor)
            self.boton_salir.setEnabled(True)
            self.boton_inicio.setEnabled(True)
            self.erroneas = 0

    @Slot(None)
    def salir(self):
        self.padre.close()
        
    @Slot(None)
    def inicio(self):
        self.padre.stackedWidget.setCurrentWidget(self.padre.paso1)
