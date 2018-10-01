from os import name
from os.path import abspath, dirname, join
from pathlib import Path
from zipfile import ZipFile

import youtube_dl
from PySide2.QtCore import QThread
from youtube_dl.YoutubeDL import YoutubeDL

DIRECTORIO_PRINCIPAL = abspath(dirname(dirname(__file__)))


class Data(QThread):
    localizacion: str = ""
    formatos = {
        "mp3": False,
        "mp4a": False,
        "mp4": False,
    }

    def __init__(self, padre, urls: list):
        QThread.__init__(self)
        self.padre = padre
        self.urls = urls

    def run(self):
        
        for formato, check in self.formatos.items():
            if check:
                for cancion_numero, url in enumerate(self.urls):
                    self.padre.descripcion_proceso.setText("({}-{}) Descargando canción desde el enlace {} y "
                                                           "convirtiendo en {}.".format((cancion_numero + 1),
                                                                                        len(self.urls), url, formato))
                    # Descarga
                    try:
                        # Formato Mp4
                        opciones = {'outtmpl': join(self.localizacion, "%(title)s-%(id)s.%(ext)s")}

                        if formato == "mp4a":
                            opciones = {
                                'outtmpl': join(self.localizacion, "%(title)s-%(id)s.%(ext)s"),
                                'format': 'm4a',
                            }

                        if formato == "mp3":

                            if name == 'nt':

                                if not Path(abspath(join(DIRECTORIO_PRINCIPAL, 'ffmpeg-4.0.2-win64-static'))).exists():
                                    with ZipFile(abspath(join(DIRECTORIO_PRINCIPAL,
                                                              'ffmpeg-4.0.2-win64-static.zip'))) as myzip:
                                        myzip.extractall()

                                opciones = {
                                    'format': 'bestaudio/best',
                                    'outtmpl': join(self.localizacion, "%(title)s-%(id)s.%(ext)s"),
                                    'ffmpeg_location': abspath(join(DIRECTORIO_PRINCIPAL,
                                                                    "ffmpeg-4.0.2-win64-static", "bin", "ffmpeg.exe")),
                                    'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '400', }]}
                            else:
                                opciones = {
                                    'format': 'bestaudio/best',
                                    'outtmpl': join(self.localizacion, "%(title)s-%(id)s.%(ext)s"),
                                    'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '400', }]}

                        with YoutubeDL(opciones) as ydl:
                            ydl.download([url])

                    except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError) as error:
                        self.padre.excepcion = True
                        self.padre.error.append(error)
