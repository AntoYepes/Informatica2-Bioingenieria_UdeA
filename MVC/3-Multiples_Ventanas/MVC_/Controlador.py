from Modelo import Servicio
from Vista import *
from PyQt5.QtWidgets import QApplication
import sys

class Coordinador():
    def __init__(self, vista, sistema):
        self.__mi_vista = vista
        self.__mi_sistema = sistema
        
    def RecibirInfoPaciente(self, n, c, medicamento):
        if self.__mi_sistema.VerificarPaciente(c) == True:
            return 'Ya el paciente existe'
        else:
            self.__mi_sistema.AgregarPaciente(n, c, medicamento)
            return 'Paciente agregado con exito'
        
    def AgregarMedicamento(self, c, n, d):
        if self.__mi_sistema.VerificarPaciente(c) == False:
            return 'El paciente no existe, no se puede agregar medicamento'
        else:
            if self.__mi_sistema.VerificarMedicamento(c, n) == True:
                return 'El paciente ya tiene medicamento'
            else:
                self.__mi_sistema.AgregarMedicamento(c, n, d)
                return 'Medicamento Agregado'
            
def main():
    app = QApplication(sys.argv)
    mi_vista = VentanaPrincipal()
    mi_sistema = Servicio()
    mi_controlador = Coordinador(mi_vista, mi_sistema)
    mi_vista.asignarCoordinador(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()