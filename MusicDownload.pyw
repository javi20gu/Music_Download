from youtube_dl import YoutubeDL
import youtube_dl
from os import path
from Ui.Ui_Main import QtCore, QtWidgets, QtGui, Ui_Ventana_1
 
RUTA_PRINCIPAL = path.abspath(path.dirname(__file__))  
 
class App(QtWidgets.QWidget):
 
    def __init__(self):
 
        super().__init__()
        self.ui = Ui_Ventana_1()
        self.ui.setupUi(self)

        self.error_hilo = ""

        RUTA_PRINCIPAL = path.abspath(path.dirname(__file__))
        self.setWindowIcon(QtGui.QIcon(path.join(RUTA_PRINCIPAL, "icono.png")))
 
        self.sombra = QtWidgets.QGraphicsDropShadowEffect()
        self.sombra.setBlurRadius(6)
        self.sombra.setOffset(0, 0)
        self.ui.input.setGraphicsEffect(self.sombra)
       
        self.ui.input.returnPressed.connect(self.proceso)
 
    def proceso(self):
        self.thread_error = False
        self.hilo = SecondThread(self)
        self.hilo.setUi(self.ui)
        self.hilo.start()
        self.hilo.finished.connect(self.error)
 
    def error(self):
        
        if self.thread_error:
            indice = self.error_hilo.find(".")
            QtWidgets.QMessageBox.critical(self, 'MusicDownload', self.error_hilo[:indice])
 
 
class SecondThread(QtCore.QThread):
 
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
       
    def setUi(self, Ui):
        self.ui = Ui
 
    def run(self):
        self.ui.proceso.setMaximum(0)
        self.ui.proceso.setValue(0)
        try:
            opciones = {}
            url = self.ui.input.text()
           
            if self.ui.botonMp4a.isChecked():
                opciones = {'format': 'm4a'}
 
            if self.ui.botonMp3.isChecked():
                opciones = {
                'format': 'bestaudio/best',
                'ffmpeg_location': path.join(RUTA_PRINCIPAL, "ffmpeg-4.0.2-win64-static\\bin\\ffmpeg.exe"),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '400',}],
                }
 
            with YoutubeDL(opciones) as ydl:
                ydl.download([url])

        except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError)as error:
            self.parent.thread_error = True
            self.parent.error_hilo = str(error)

        self.ui.proceso.setMaximum(100)
 
 
if __name__ == '__main__':
 
    from sys import exit, argv
 
    cmd = QtWidgets.QApplication(argv)
    clase = App()
    clase.show()
    exit(cmd.exec_())