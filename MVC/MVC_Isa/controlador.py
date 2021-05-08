#CONTROLADOR
import sys
from PyQt5.QtWidgets import QApplication
from vista import VentanaPrincipal
from modelo import Sistema

#La clase coordinador
class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    # Metodos que enlazan vista, controlador y modelo
    def agregarMedicamento(self, n, r, f, e, c):
        self.__mi_modelo.agregarMedicamento( n, r, f, e, c)
        self.__mi_modelo.show()
    
    def aumentarStock(self, r, c):
        return  self.__mi_modelo.aumentarStock(r, c)
    
    def disminuirStock(self, r, c):
         return self.__mi_modelo.disminuirStock(r, c)
    
    def cantidadStock(self, r):
        return self.__mi_modelo.cantidadStock(r)
    
def main():
    app = QApplication(sys.argv)
    mi_vista = VentanaPrincipal()
    mi_modelo = Sistema()
    mi_coordinador = Coordinador(mi_vista,mi_modelo)
    mi_vista.setControlador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
    