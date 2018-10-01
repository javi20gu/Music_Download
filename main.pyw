from PySide2.QtWidgets import QWidget


class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.ui_main = Ui_Ui_Main()
        self.ui_main.setupUi(self)
        self.ventana = Ublicacion(self)
        self.setWindowIcon(QIcon(join(getcwd(), "asserts", "icono.ico")))
        self.ui_main.cancelar.clicked.connect(self.salir)
        self.ui_main.siguiente.clicked.connect(self.siguiente)
        self.ui_main.boton_anadir.clicked.connect(self.añadir)
        self.ui_main.boton_borrar.clicked.connect(self.borrar)

    def borrar(self):
        fila = self.ui_main.lista_elementos.currentRow()
        item = self.ui_main.lista_elementos.takeItem(fila)
        del item
        if self.ui_main.lista_elementos.count() == 0:
            self.ui_main.boton_borrar.setEnabled(False)
            self.ui_main.siguiente.setEnabled(False)

    def añadir(self):
        fila = self.ui_main.lista_elementos.currentRow()
        item_url, acept = QInputDialog.getText(self, "Music Download", "Introduce o arrastra el url")
        if acept and item_url != "":
            self.ui_main.lista_elementos.insertItem(fila, item_url)
        if self.ui_main.lista_elementos.count() != 0:
            self.ui_main.boton_borrar.setEnabled(True)
            self.ui_main.siguiente.setEnabled(True)

    def siguiente(self):
        if self.ui_main.lista_elementos.count() != 0:
            self.close()
            self.ventana.show()
        else:
            QMessageBox.warning(self, "Music Download", "Tienes que poner como minimo una canción con el botón añadir",
                                QMessageBox.Retry)

    def salir(self):
        opción_mensaje = QMessageBox.information(self, "Music Download", "¿Desea Salir?",
                                                 QMessageBox.Yes, QMessageBox.No)
        if opción_mensaje == QMessageBox.Yes:
            self.close()
            del self
            exit()


class Ublicacion(QWidget):

    def __init__(self, parent=None):
        super(Ublicacion, self).__init__()
        self.ui_ublicacion = Ui_Ui_Localizacin()
        self.ui_ublicacion.setupUi(self)
        self.setWindowIcon(QIcon(join(getcwd(), "asserts", "icono.ico")))
        self.padre = parent
        self.ui_ublicacion.siguiente.clicked.connect(self.siguiente)
        self.ui_ublicacion.boton_anterior.clicked.connect(self.anterior)
        self.ui_ublicacion.seleccionar.clicked.connect(self.seleccionar_ruta)

    def seleccionar_ruta(self):
        ruta = QFileDialog.getExistingDirectory(self, "Guardar Archivo", dirname(dirname(getcwd())))
        self.ui_ublicacion.lineEdit.setText(ruta)
        self.ui_ublicacion.siguiente.setEnabled(True)

    def anterior(self):
        self.close()
        self.padre.show()

    def siguiente(self):
        self.urls = [self.padre.ui_main.lista_elementos.item(i).text() for i in
                     range(self.padre.ui_main.lista_elementos.count())]
        Data.localizacion = self.ui_ublicacion.lineEdit.text()
        self.ventana = Formato(self)
        self.close()
        self.ventana.show()


class Formato(QWidget):

    def __init__(self, parent=None):
        super(Formato, self).__init__()
        self.ui_formato = Ui_Ui_Loanding()
        self.ui_formato.setupUi(self)
        self.ventana_padre = parent
        self.setWindowIcon(QIcon(join(getcwd(), "asserts", "icono.ico")))
        self.ui_formato.imagenMp3.setPixmap(QPixmap("./asserts/mp3.png"))
        self.ui_formato.imagenMp4.setPixmap(QPixmap("./asserts/mp4.png"))
        self.ui_formato.imagenMp4A.setPixmap(QPixmap("./asserts/m4a.png"))
        self.ui_formato.boton_mp3.clicked.connect(self.mp3)
        self.ui_formato.boton_mp4a.clicked.connect(self.mp4a)
        self.ui_formato.boton_mp4.clicked.connect(self.mp4)

    def mp3(self):
        Data.formatos["mp3"] = True
        Data.formatos["mp4a"] = False
        Data.formatos["mp4"] = False
        self.close()
        self.ventana = Proceso(self)
        self.ventana.show()

    def mp4a(self):
        Data.formatos["mp3"] = False
        Data.formatos["mp4a"] = True
        Data.formatos["mp4"] = False
        self.close()
        self.ventana = Proceso(self)
        self.ventana.show()

    def mp4(self):
        Data.formatos["mp3"] = False
        Data.formatos["mp4"] = True
        Data.formatos["mp4a"] = False
        self.close()
        self.ventana = Proceso(self)
        self.ventana.show()


class Proceso(QWidget):

    def __init__(self, parent=None):
        super(Proceso, self).__init__()
        self.ui_proceso = Ui_Ui_Proceso()
        self.ui_proceso.setupUi(self)
        self.setWindowIcon(QIcon(join(getcwd(), "asserts", "icono.ico")))
        self.padre = parent
        self.ui_proceso.error = []
        self.ui_proceso.excepcion = False
        self.descarga = Data(self.ui_proceso, self.padre.ventana_padre.urls)
        self.descarga.start()
        self.descarga.finished.connect(self.finalizar)

    def finalizar(self):

        errores = tuple(self.ui_proceso.error)

        if self.ui_proceso.excepcion:
            for error in errores:
                QMessageBox.warning(self, "Music Download", str(error))

        self.ui_proceso.descripcion_proceso.setText("Finalizado")
        self.ui_proceso.proceso.setMaximum(100)
        self.ui_proceso.boton_volver.setEnabled(True)
        self.ui_proceso.boton_salir.setEnabled(True)
        self.ui_proceso.boton_salir.clicked.connect(self.salir)
        self.ui_proceso.boton_volver.clicked.connect(self.volver)

    def salir(self):
        opción_mensaje = QMessageBox.information(self, "Music Download", "¿Estas seguro que quieres salir?",
                                                 QMessageBox.Yes, QMessageBox.No)
        if opción_mensaje == QMessageBox.Yes:
            self.close()
            del self
            exit()

    def volver(self):
        self.app = App()
        self.close()
        self.app.show()
        del self


if __name__ == '__main__':
    from os import getcwd
    from os.path import dirname, join

    from sys import argv
    from PySide2.QtWidgets import QSplashScreen, QApplication

    cmd = QApplication(argv)

    from PySide2.QtCore import Qt
    from PySide2.QtGui import QPixmap

    ventana = QSplashScreen(QPixmap(join(getcwd(), "asserts", "carga.png")), Qt.WindowStaysOnTopHint)
    ventana.showMessage("Cargando...", Qt.AlignBottom, Qt.darkCyan)
    ventana.show()

    from PySide2.QtWidgets import (QApplication, QFileDialog, QInputDialog,
                                   QMessageBox, QWidget)
    from PySide2.QtGui import QIcon
    from other.data import Data
    from Ui.Ui_Ui_Formato import Ui_Ui_Loanding
    from Ui.Ui_Ui_Localización import Ui_Ui_Localizacin
    from Ui.Ui_Ui_Proceso import Ui_Ui_Proceso
    from Ui.Ui_Main import Ui_Ui_Main

    run = App()
    ventana.finish(run)
    run.show()
    from sys import exit

    exit(cmd.exec_())
