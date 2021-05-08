# CONTROLADOR AEROPUERTO
import sys
from MODELO import Aeropuerto
from VISTA import ventanaPrincipal
from PyQt5. QtWidgets import QApplication

class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
    def recibirInfoPax(self, n, c, vuelo):
        if self.__mi_modelo.verificarPasajero(c) == True:
            return 'Pasajero ya registrado'
        else:
            self.__mi_modelo.agregarPasajero(n, c, vuelo)
            return 'Pasajero ingresado con exito'
        
    def agregarVuelo(self, c, numVuelo, fechaVuelo):
        if self.__mi_modelo.verificarPasajero(c) == False:
            return 'El pasajero no existe, no se le puede agregar vuelo'
        else:
            if self.__mi_modelo.verificarVuelo(c, numVuelo) == True:
                return 'El pasajero ya tiene vuelo asignado'
            else:
                self.__mi_modelo.agregarVuelo(c, numVuelo, fechaVuelo)
                return 'Vuelo ingresado con exito'
            
def main():
    app = QApplication(sys.argv)
    mi_vista = ventanaPrincipal()
    mi_modelo = Aeropuerto()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setControlador(mi_coordinador)
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()