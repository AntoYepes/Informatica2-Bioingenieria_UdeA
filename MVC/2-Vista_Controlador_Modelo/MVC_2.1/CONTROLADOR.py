# CONTROLADOR:
    # Aca se hara el enlace y se inicia el programa
    
# 1- Importamos 
import sys
from MODELO import BaseDatos
from VISTA import ventanaLogin
from PyQt5.QtWidgets import QApplication

# Creamos la clase de coordinador
class Coordinador:
    # Constructor debe tener acceso a vista y a modelo
    def __init__(self, vista, modelo):
        # Atributos
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
    # El controlador debe tener un metodo para recibir la info de visita
    # por eso envia esto al modelo y espera que este responda
    def validarUsuario(self, l , p):
        self.__mi_modelo.validarUsuario(l, p)
        
# main
def main():
    # creo obj app
    app = QApplication(sys.argv)
    # se crea obj ventana
    mi_vista = ventanaLogin()
    mi_modelo = BaseDatos()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setControlador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
    
    
