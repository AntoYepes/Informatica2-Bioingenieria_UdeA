# CONTROLADOR:
    # Acá se haria el enlace y se inica el programa

# Importamos
from MODELO import BaseDatos
from VISTA import VentanaLogin
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador:
    # Como el coordinador enlaza el modelo con la vista debe
    # tener acceso a objetos de ambas clases
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    # iii- El controlador debe tener un metodo para recibir la info de la vista
    # Pero como el controlador es bruto, simplemente debe enviar esta info al modelo y esperar que este responda
    def validarUsuario(self, l, p):
        return self.__mi_modelo.validarUsuario(l, p)


# Simplemente se hacen las conexiones que siempre van
if __name__ == '__main__':
    app = QApplication((sys.argv))
    mi_vista = VentanaLogin()
    mi_modelo = BaseDatos()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setControlador(mi_coordinador)
    mi_vista.show() 
    sys.exit(app.exec())
