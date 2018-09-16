

if __name__ == '__main__':
    from sys import argv
    from os.path import join, abspath, dirname

    from PySide2.QtWidgets import QApplication, QSplashScreen
    from PySide2.QtGui import QPixmap
    from PySide2.QtCore import Qt
   
    DIRECTORIO_PRINCIPAL = join(abspath(dirname(__file__)))

    cmd = QApplication(argv)
    ventana = QSplashScreen(QPixmap(abspath(join(DIRECTORIO_PRINCIPAL, "asserts\loanding.png"))),
                            Qt.WindowStaysOnBottomHint)
    ventana.showMessage("Cargando...", Qt.AlignBottom, Qt.darkCyan)
    ventana.show()

    from sys import exit, argv

    from Ui.core import App
    
    

    clase = App()
    clase.show()
    ventana.finish(clase)
    exit(cmd.exec_())
