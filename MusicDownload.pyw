

if __name__ == '__main__':


    from sys import argv
    from os.path import join, abspath, dirname

    from Ui.Ui_Main import QtCore, QtWidgets, QtGui


    cmd = QtWidgets.QApplication(argv)
    ventana = QtWidgets.QSplashScreen(QtGui.QPixmap(join(abspath(dirname(__file__)), "loanding.png")),
                                      QtCore.Qt.WindowStaysOnBottomHint) 
    ventana.showMessage("Cargando...", QtCore.Qt.AlignBottom, QtCore.Qt.white)
    ventana.show()


    from sys import exit, argv

    from core import App


    clase = App()
    clase.show()
    ventana.finish(clase)
    exit(cmd.exec_())
