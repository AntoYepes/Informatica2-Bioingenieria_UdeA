import sys
from PyQt5.QtWidgets import QApplication
from Vista import VentanaPrincipal
from Modelo import Sistema

#La clase coordinador
class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    def agregarinfoPaciente(self, n, e, c, g):
        if self.__mi_modelo.VerificarPaciente(c) == True:
            return 'Paciente ya existe'
        else:
            self.__mi_modelo.AgregarPaciente(n, e, c, g)
            return 'Paciente agregado con exito'
        
    def recibir_infoVisita(self, f, r, n):
        if self.__mi_modelo.verificarExistVisita(f) == True:
            return 'Visita ya existe'
        else:
            self.__mi_modelo.AgregarVisitas(f, r, n)
            return 'Visita ingresado con exito'

    def recibir_indices(self, delta, theta, alfa1, alfa2, betha, gamma):
        self.__mi_modelo.AgregarIndices(delta, theta, alfa1, alfa2, betha, gamma)
        return 'Indice ingresado con exito'
        
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