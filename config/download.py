from os import name
from os.path import abspath, dirname, join
from pathlib import Path
from zipfile import ZipFile

import youtube_dl
from PySide2.QtCore import QThread, Signal
from youtube_dl.YoutubeDL import YoutubeDL


class Download(QThread):
    
    is_error = Signal(bool, str, int)
    DIRECTORIO_PRINCIPAL = abspath(dirname(__file__))

    def __init__(self, padre, state):
        super().__init__()
        from .ventana4.ventana4 import FrameDescarga
        from .state import State
        self.padre: FrameDescarga = padre
        self.state: State = state

    def run(self):
        estado: dict = self.state.get_state()
        canciones = estado.get(self.state.CANCIONES)
        formato = estado.get(self.state.TIPO_FORMATO)
        localizacion = estado.get(self.state.DIRECTORIO_GUARDAR)
        opciones: dict = {}
        for i, cancion in enumerate(canciones):
            self.padre.label_subtitulo.setText(
                f"Descargando url <{cancion}> - {i+1} | {len(canciones)}")
            try:
                if formato == 'mp3':
                    if name == 'nt':
                        if not Path(abspath(join(self.DIRECTORIO_PRINCIPAL, 'ffmpeg-4.0.2-win64-static'))).exists():
                            with ZipFile(abspath(join(self.DIRECTORIO_PRINCIPAL,
                                                      'ffmpeg-4.0.2-win64-static.zip'))) as myzip:
                                myzip.extractall(path=self.DIRECTORIO_PRINCIPAL)
                        opciones = {
                            'format': 'bestaudio/best',
                            'outtmpl': join(localizacion, "%(title)s-%(id)s.%(ext)s"),
                            'ffmpeg_location': abspath(join(self.DIRECTORIO_PRINCIPAL,
                                                            "ffmpeg-4.0.2-win64-static", "bin", "ffmpeg.exe")),
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '800', }]}
                    else:
                        opciones = {
                            'format': 'bestaudio/best',
                            'outtmpl': join(localizacion, "%(title)s-%(id)s.%(ext)s"),
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '800', }]
                        }
                elif formato == 'mp4a':
                    opciones = {
                        'outtmpl': join(localizacion, "%(title)s-%(id)s.%(ext)s"),
                        'format': 'm4a',
                    }
                elif formato == 'mp4':
                    opciones = {'outtmpl': join(
                        localizacion, "%(title)s-%(id)s.%(ext)s")}

                with YoutubeDL(opciones) as ydl:
                    ydl.download([cancion])
            except (youtube_dl.utils.DownloadError, youtube_dl.utils.ExtractorError) as error:
                self.is_error.emit(True, str(error), len(canciones))

        self.is_error.emit(False, None, len(canciones))
