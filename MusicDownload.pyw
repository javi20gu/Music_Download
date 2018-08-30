
from youtube_dl import YoutubeDL
from os import path

from Ui.Ui_Main import QtCore, QtWidgets, QtGui, Ui_Ventana_1


class App(QtWidgets.QWidget):

    

    def __init__(self):
        super().__init__()
        self.ui = Ui_Ventana_1()
        self.ui.setupUi(self)
        self.ui.botonMp4.setChecked(True)
        self.ui.botonMp3.setDisabled(True)
        RUTA_PRINCIPAL = path.abspath(path.dirname(__file__))
        self.setWindowIcon(QtGui.QIcon(path.join(RUTA_PRINCIPAL, "icono.png")))

        self.sombra = QtWidgets.QGraphicsDropShadowEffect()
        self.sombra.setBlurRadius(6)
        self.sombra.setOffset(0, 0)
        self.ui.input.setGraphicsEffect(self.sombra)
        
        self.ui.input.returnPressed.connect(self.proceso)

    def proceso(self):

        self.hilo = SecondThread()
        self.hilo.setUi(self.ui)
        self.hilo.start()


class SecondThread(QtCore.QThread):

    def __init__(self):
        super().__init__()
        
    def setUi(self, Ui):
        self.ui = Ui

    def run(self):
        self.ui.proceso.setMaximum(0)
        self.ui.proceso.setValue(0)
        if self.ui.botonMp4.isChecked(): 
            try:
                with YoutubeDL() as ydl:
                    ydl.download([self.ui.input.text()])
            except BaseException as error:
                self.ui.input.setPlaceholderText("Error: Comprueba que has puesto bien la dirección, o tienes internet")
                self.ui.input.setText("")
        self.ui.proceso.setMaximum(100)

if __name__ == '__main__':

    from sys import exit, argv

    cmd = QtWidgets.QApplication(argv)
    clase = App()
    clase.show()
    exit(cmd.exec_())
