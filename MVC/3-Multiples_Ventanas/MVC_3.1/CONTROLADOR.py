# CONTROLADOR
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from MODELO import BaseDato
from VISTA import ventanaPrincipal

class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
    def validarUsuario(self, n, c):
        self.__mi_modelo.validarUsuario(n, c)
        
def main():
    app = QApplication(sys.argv)
    mi_vista = ventanaPrincipal()
    mi_modelo = BaseDato()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setControlador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    