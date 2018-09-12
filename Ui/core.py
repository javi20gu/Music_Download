from os import getcwd, name
from os.path import abspath, dirname, join
from subprocess import call
from sys import platform

import youtube_dl
from youtube_dl.YoutubeDL import YoutubeDL

from Ui.Main import QtCore, QtGui, QtWidgets, Ui_Ventana_Base

DIRECTORIO_PRINCIPAL = abspath(join(dirname(dirname(__file__))))


class SecondThread(QtCore.QThread):
 
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
       
    def setUi(self, Ui):
        self.ui = Ui
    
    def setBoton(self, boton):
        self.boton = boton

    def run(self):
        self.ui.proceso.setMaximum(0)
        self.ui.proceso.setValue(0)
        try:
            opciones = {'outtmpl': join(self.parent.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"),}
            url = self.ui.input.text()

            if self.boton == "mp4a":
                opciones = {
                    'outtmpl': join(self.parent.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"),
                    'format': 'm4a'}
 
            if self.boton == "mp3":
                if name == 'nt':
                    opciones = {
                    'format': 'bestaudio/best',
                    'outtmpl': join(self.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"),
                    'ffmpeg_location': join(DIRECTORIO_PRINCIPAL, "ffmpeg-4.0.2-win64-static\\bin\\ffmpeg.exe"),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '400',}],
                    }
                else: 
                    opciones = {
                    'format': 'bestaudio/best',
                    'outtmpl': join(self.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '400',}],}
                    
                
            with YoutubeDL(opciones) as ydl:
                ydl.download([url])
                info = ydl.extract_info(url ,download=False)
                self.filename_path = ydl.prepare_filename(info)
                self.parent.filename_path = self.filename_path

        except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError) as error:
            self.parent.thread_error = True
            self.parent.error_hilo = str(error)
            
        self.ui.proceso.setMaximum(100)


class App(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui = Ui_Ventana_Base()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(join(DIRECTORIO_PRINCIPAL, "asserts", "icono.ico")))

        self.thread_error = False
        self.ui.input.setStyleSheet("#input {\n"
"    border: 0px solid #fff;\n"
"    border-radius: 7px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-left: 80px;\n"
"    color: rgb(112, 112, 112);\n"
"    font-family: 'Roboto';\n"
"    font-weight: bold;\n"
"}")
        self.ui.printGuardar.setFont(QtGui.QFont("Roboto", 10))
        self.ui.label.setFont(QtGui.QFont("Roboto", 10))

        self.ui.imagen_enlace.setPixmap(QtGui.QPixmap(join(DIRECTORIO_PRINCIPAL, "asserts", "enlaze.png")))
        self.ui.botonMp3.setIcon(QtGui.QIcon(join(DIRECTORIO_PRINCIPAL, "asserts", "mp3.png")))
        self.ui.botonMp4a.setIcon(QtGui.QIcon(join(DIRECTORIO_PRINCIPAL, "asserts", "m4a.png")))
        self.ui.botonMp4.setIcon(QtGui.QIcon(join(DIRECTORIO_PRINCIPAL, "asserts", "mp4.png")))
        self.ui.botonCarpeta.setIcon(QtGui.QIcon(join(DIRECTORIO_PRINCIPAL, "asserts", "carpeta.png")))
        
        # Eventos
        self.ui.salir.clicked.connect(self.cerrar)
        self.ui.botonCarpeta.clicked.connect(self.guardar)
        self.ui.botonMp3.clicked.connect(lambda: self.verificar("mp3"))
        self.ui.botonMp4a.clicked.connect(lambda: self.verificar("mp4a"))
        self.ui.botonMp4.clicked.connect(lambda: self.verificar("mp4"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def verificar(self, boton):
    
        if self.ui.input.text() == "" :
            QtWidgets.QMessageBox.critical(self, "Music Download", "Debe Completar el campo de la Url.")

        if self.ui.input_Ublicacion.text() == "":
            QtWidgets.QMessageBox.critical(self, "Music Download", "Debe elegir la ublicación donde se quiere guardar.")

        if self.ui.input.text() != "" and self.ui.input_Ublicacion.text() != "":
            self.hilo = SecondThread(self)
            self.hilo.setUi(self.ui)
            self.hilo.setBoton(boton)
            self.hilo.start()
            self.setFocus(True)
            self.hilo.finished.connect(self.error)

    def guardar(self):
        self.ruta = QtWidgets.QFileDialog.getExistingDirectory(self, 'Guardar Archivo')
        self.ui.input_Ublicacion.setText(self.ruta)

    def cerrar(self):
        self.close()
        del self
        exit()

    def error(self):

        if self.thread_error:
            indice = self.error_hilo.find(".")
            QtWidgets.QMessageBox.critical(self, 'Music Download', self.error_hilo[:indice])

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
