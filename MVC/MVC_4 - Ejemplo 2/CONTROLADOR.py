# CONTROLADOR
# Coordinador: Clase que hace enlace entre modelo y vista
# Principal: Clase que se encarga de inicializar las variables para
# comenzar el programa

import sys
from PyQt5.QtWidgets import QApplication
from VISTA import VentanaPrincipal
from MODELO import Servicio

class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
    def recibirInfoPaciente(self, n, c, medicamentos):
        if self.__mi_modelo.verificarPaciente(c) == True:
            return 'Ya el paciente existe!'
        else: 
            # si lo existe lo agrega
            self.__mi_modelo.agregarPaciente(n, c, medicamentos)
            return 'Paciente agregado con exito'
    
    def agregarMedicamento(self, c, n, d):
        if self.__mi_modelo.verificarPaciente(c) == False:
            return 'El paciente no existe, no se puede agregar medicamento'
        else:
            if self.__mi_modelo.verificarMedicamento(c, n) == True:
                return 'El paciente ya tiene el medicamento'
            else:
                self.__mi_modelo.agregarMedicamente(c, n, d)
                return 'Medicamento ingresado con exito'
            
def main():
    app = QApplication(sys.argv)
    mi_vista = VentanaPrincipal()
    mi_modelo = Servicio() 
    mi_controlador = Coordinador(mi_vista, mi_modelo)
    mi_vista.asignarCoordinador(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
    
                
            