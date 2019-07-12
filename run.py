from PySide2.QtWidgets import QMainWindow, QApplication, QSplashScreen, QWidget
from PySide2.QtGui import QFontDatabase, QPixmap, QColor, QFont
from typing import List

from config.state import State
from config.ventana_principal.ventana_principal import App


def cargar_fuentes() -> List[str]:
    font_db: QFontDatabase = QFontDatabase()

    font_black = font_db.addApplicationFont(
        "config/ventana_principal/assets/fonts/OpenSans-ExtraBold.ttf")
    font_bold = font_db.addApplicationFont(
        "config/ventana_principal/assets/fonts/OpenSans-Bold.ttf")
    font_medium = font_db.addApplicationFont(
        "config/ventana_principal/assets/fonts/Roboto-Medium.ttf")
    font_regular = font_db.addApplicationFont(
        "config/ventana_principal/assets/fonts/Roboto-Regular.ttf")

    families_black = font_db.applicationFontFamilies(font_black)
    families_bold = font_db.applicationFontFamilies(font_bold)
    families_medium = font_db.applicationFontFamilies(font_medium)
    families_regular = font_db.applicationFontFamilies(font_regular)

    return [
        families_black,
        families_bold,
        families_medium,
        families_regular
    ]


if __name__ == "__main__":
    from sys import argv, exit
    from os.path import abspath, join, dirname

    out: QApplication = QApplication(argv)

    imagen = abspath(join(dirname(__file__), 'config',
                          'ventana_principal', 'assets', 'fondo.png'))
    ventana = QWidget()
    pantalla_de_carga = QSplashScreen(ventana, imagen)
    pantalla_de_carga.show()
    from PySide2.QtCore import Qt
    pantalla_de_carga.setFont(QFont('Segoe Ui SemiBold', 15))
    pantalla_de_carga.showMessage(
        "Cargando...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter, QColor('white'))
    state: State = State()
    pantalla_de_carga.showMessage(
        "Cargando fuentes...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter, QColor('white'))
    fuentes: List[str] = cargar_fuentes()
    pantalla_de_carga.showMessage(
        "Iniciando Aplicación...", Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter, QColor('white'))
    clase: App = App(fuentes, state)
    pantalla_de_carga.close()
    clase.show()
    exit(out.exec_())
