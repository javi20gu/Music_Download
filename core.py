

from youtube_dl import YoutubeDL
import youtube_dl
from os import path, name
from sys import platform
from subprocess import call

from Ui.Ui_Main import QtCore, QtWidgets, QtGui, Ui_Ventana_1


RUTA_PRINCIPAL = path.abspath(path.dirname(__file__))


class App(QtWidgets.QWidget):
 
    def __init__(self):
 
        super().__init__()
        self.ui = Ui_Ventana_1()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnBottomHint)
        if name == 'nt':
            self.ui.botonMp3.setDisabled(False)

        else:
            self.ui.botonMp3.setDisabled(True)

        self.error_hilo = ""

        RUTA_PRINCIPAL = path.abspath(path.dirname(__file__))
        self.setWindowIcon(QtGui.QIcon(path.join(RUTA_PRINCIPAL, "icono.ico")))
 
        self.sombra = QtWidgets.QGraphicsDropShadowEffect()
        self.sombra.setBlurRadius(6)
        self.sombra.setOffset(0, 0)
        self.ui.input.setGraphicsEffect(self.sombra)
       
        self.ui.input.returnPressed.connect(self.proceso)
 
    def proceso(self):
        self.thread_error = False
        self.ruta = QtWidgets.QFileDialog.getExistingDirectory(self, 'Guardar Archivo')

        if self.ruta != "":
            self.abrir()
        

    def abrir(self):
        self.hilo = SecondThread(self)
        self.hilo.setUi(self.ui)
        self.hilo.start()
        self.setFocus(True)
        self.hilo.finished.connect(self.error)
 
    def error(self):

        if self.thread_error:
            indice = self.error_hilo.find(".")
            QtWidgets.QMessageBox.critical(self, 'MusicDownload', self.error_hilo[:indice])

        else:
            comprobar = QtWidgets.QMessageBox.information(self, 'MusicDownload', "¿Deseas escuchar la canción?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

            if comprobar == QtWidgets.QMessageBox.Yes:

                if platform.startswith('darwin'):
                    call(('open', self.filename_path))
                elif name == 'nt':
                    from os import startfile
                    indice = self.filename_path.rfind(".")
                    
                    if self.filename_path[indice:] == ".webm":
                        startfile(self.filename_path.replace(".webm", ".mp3"))
                    else:
                        startfile(self.filename_path)

                elif name == 'posix':
                    call(('xdg-open', self.filename_path))


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
            opciones = {'outtmpl': path.join(self.parent.ruta, "%(title)s-%(id)s.%(ext)s"),}
            url = self.ui.input.text()
           
            if self.ui.botonMp4a.isChecked():
                opciones = {
                    'outtmpl': path.join(self.parent.ruta, "%(title)s-%(id)s.%(ext)s"),
                    'format': 'm4a'}
 
            if self.ui.botonMp3.isChecked():
                opciones = {
                'format': 'bestaudio/best',
                'outtmpl': path.join(self.parent.ruta, "%(title)s-%(id)s.%(ext)s"),
                'ffmpeg_location': path.join(RUTA_PRINCIPAL, "ffmpeg-4.0.2-win64-static\\bin\\ffmpeg.exe"),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '400',}],
                }
                
            with YoutubeDL(opciones) as ydl:
                ydl.download([url])
                info = ydl.extract_info(url ,download=False)
                self.filename_path = ydl.prepare_filename(info)

        except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError)as error:
            self.parent.thread_error = True
            self.parent.error_hilo = str(error)
            
        self.ui.proceso.setMaximum(100)
        self.parent.filename_path = self.filename_path
