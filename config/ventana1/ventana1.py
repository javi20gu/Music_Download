from PySide2.QtWidgets import QFrame, QInputDialog, QTableWidgetItem, QMainWindow
from PySide2.QtGui import QFont
from PySide2.QtCore import Slot, QEvent
from typing import List

from .design.ventana1 import Ui_Frame_Anadir_Cancion

class FrameAnadirCanciones(Ui_Frame_Anadir_Cancion, QFrame):

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
        from ..state import State
        from ..ventana_principal.ventana_principal import App
        self.state: State = state
        self.setupUi(self)
        self.padre: App = padre 
        self.label_titulo.setFont(QFont(fonts[0][0], 27))
        self.label_subtitulo.setFont(QFont(fonts[3][0], 10))
        self.tabla.itemPressed.connect(self.select_item)
        self.tabla.setFont(QFont(fonts[2][0], 10))

        self.boton_siguiente.clicked.connect(self.siguiente)
        self.boton_anadir.clicked.connect(self.añadirCancion)
        self.boton_borrar.clicked.connect(self.borrarCancion)

    @Slot(QEvent)
    def showEvent(self, event: QEvent):
        for row in range(self.tabla.rowCount()):
            self.tabla.removeRow(row)
        if self.tabla.rowCount() == 0:
            self.boton_siguiente.setEnabled(False)
        self.padre.label_anadir_canciones.setStyleSheet(self.STYLE["active"])
        self.padre.label_tipo_formato.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_descarga.setStyleSheet(self.STYLE["desactive"])
        self.padre.label_ublicacion.setStyleSheet(self.STYLE["desactive"])
        super().showEvent(event)
        
    @Slot(None)
    def siguiente(self):
        lista = []
        for row in range(self.tabla.rowCount()):
            lista.append(self.tabla.item(row, 0).text())
        self.state.set_state(canciones=lista)
        self.padre.stackedWidget.setCurrentWidget(self.padre.paso2)

    @Slot(QTableWidgetItem)
    def select_item(self, item: QTableWidgetItem):
        self.boton_borrar.setEnabled(True)

    @Slot(None)
    def borrarCancion(self):
        fila_actual = self.tabla.currentRow()
        item = self.tabla.takeItem(fila_actual, 0)
        del item
        if self.tabla.rowCount() == 1:
            self.tabla.setRowCount(0)
            self.boton_borrar.setEnabled(False)
            self.boton_siguiente.setEnabled(False)
        else:
            self.tabla.removeRow(fila_actual)
            

    @Slot(None)
    def añadirCancion(self):
        respuesta = QInputDialog.getText(self, 'MusicDw', 'Introduce el Url o Arrástralo')
        if respuesta[0] == '' or respuesta == False:
            pass
        else:
            self.tabla.setRowCount(self.tabla.rowCount() + 1)
            item = QTableWidgetItem(respuesta[0])
            self.tabla.setItem(self.tabla.rowCount() - 1, 0, item)
        if self.tabla.rowCount() >= 1:
            self.boton_siguiente.setEnabled(True)
