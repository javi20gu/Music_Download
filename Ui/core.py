from os import name
from os.path import abspath, dirname, join
from pathlib import Path
from subprocess import call
from sys import platform
from zipfile import ZipFile

import youtube_dl
from youtube_dl.YoutubeDL import YoutubeDL

from Ui.Main import QtCore, QtGui, QtWidgets, Ui_Ventana

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
        self.ui.statusbar.showMessage("Descargando...")
        self.ui.proceso.setMaximum(0)
        self.ui.proceso.setValue(0)
        try:
            opciones = {'outtmpl': join(self.parent.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"), }
            url = self.ui.input.text()

            if self.boton == "mp4a":
                opciones = {
                    'outtmpl': join(self.parent.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"),
                    'format': 'm4a'}

            if self.boton == "mp3":
                if name == 'nt':
                    if not Path(abspath(join(DIRECTORIO_PRINCIPAL, 'ffmpeg-4.0.2-win64-static'))).exists():
                        with ZipFile(abspath(join(DIRECTORIO_PRINCIPAL, 'ffmpeg-4.0.2-win64-static.zip'))) as myzip:
                            myzip.extractall()
                    opciones = {
                        'format': 'bestaudio/best',
                        'outtmpl': join(self.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"),
                        'ffmpeg_location': abspath(
                            join(DIRECTORIO_PRINCIPAL, "ffmpeg-4.0.2-win64-static/bin/ffmpeg.exe")),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '400', }],
                    }
                else:
                    opciones = {
                        'format': 'bestaudio/best',
                        'outtmpl': join(self.ui.input_Ublicacion.text(), "%(title)s-%(id)s.%(ext)s"),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '400', }], }

            with YoutubeDL(opciones) as ydl:
                ydl.download([url])
                info = ydl.extract_info(url, download=False)
                self.filename_path = ydl.prepare_filename(info)
                self.parent.filename_path = self.filename_path

        except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError) as error:
            self.parent.thread_error = True
            self.parent.error_hilo = str(error)

        self.ui.proceso.setMaximum(100)


class App(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Ventana()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(abspath(join(DIRECTORIO_PRINCIPAL, "asserts", "icono.ico"))))

        self._drag_pos = None
        self.thread_error = False

        self.ui.imagen_enlace.setPixmap(QtGui.QPixmap(abspath(join(DIRECTORIO_PRINCIPAL, "asserts\enlaze.png"))))
        self.ui.botonMp3.setIcon(QtGui.QIcon(abspath(join(DIRECTORIO_PRINCIPAL, "asserts\mp3.png"))))
        self.ui.botonMp4a.setIcon(QtGui.QIcon(abspath(join(DIRECTORIO_PRINCIPAL, "asserts\m4a.png"))))
        self.ui.botonMp4.setIcon(QtGui.QIcon(abspath(join(DIRECTORIO_PRINCIPAL, "asserts", "mp4.png"))))
        self.ui.botonCarpeta.setIcon(QtGui.QIcon(abspath(join(DIRECTORIO_PRINCIPAL, "asserts", "carpeta.png"))))

        # Eventos
        self.ui.salir.clicked.connect(self.cerrar)
        self.ui.botonCarpeta.clicked.connect(self.guardar)
        self.ui.botonMp3.clicked.connect(lambda: self.verificar("mp3"))
        self.ui.botonMp4a.clicked.connect(lambda: self.verificar("mp4a"))
        self.ui.botonMp4.clicked.connect(lambda: self.verificar("mp4"))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._drag_pos= event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self._drag_pos is not None:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._drag_pos = None      
            event.accept()

    def verificar(self, boton):

        if self.ui.input.text() == "":
            QtWidgets.QMessageBox.critical(self, "Music Download", "Debe Completar el campo de la Url.")

        if self.ui.input_Ublicacion.text() == "":
            QtWidgets.QMessageBox.critical(self, "Music Download", "Debe elegir la ublicación donde se quiere guardar.")

        if self.ui.input.text() != "" and self.ui.input_Ublicacion.text() != "":
            self.hilo = SecondThread(self)
            self.hilo.setUi(self.ui)
            self.hilo.setBoton(boton)
            self.hilo.start()
            self.hilo.finished.connect(self.error)

    def guardar(self):
        self.ruta = QtWidgets.QFileDialog.getExistingDirectory(self, 'Guardar Archivo')
        self.ui.input_Ublicacion.setText(self.ruta)

    def cerrar(self):
        self.close()
        del self
        exit()

    def error(self):

        self.ui.statusbar.showMessage("")

        if self.thread_error:
            indice = self.error_hilo.find(".")
            QtWidgets.QMessageBox.critical(self, 'Music Download', self.error_hilo[:indice])

        else:
            comprobar = QtWidgets.QMessageBox.information(self, 'MusicDownload', "¿Deseas escuchar la canción?",
                                                          QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

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
