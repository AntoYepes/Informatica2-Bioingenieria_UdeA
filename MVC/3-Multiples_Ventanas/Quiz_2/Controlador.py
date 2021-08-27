import sys
from PyQt5.QtWidgets import QApplication
from Vista import VentanaPrincipal
from Modelo import Hospital

class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
        
    def agregarInfoPac(self, nombre, cedula, edad, peso, estatura, genero, presion, resultado):
        if self.__mi_modelo.verificarExistencia(cedula) == True:
            return 'Paciente ya existe'
        else:
            return self.__mi_modelo.agregarInfoPac(nombre, cedula, edad, peso, estatura, genero, presion, resultado)
        
    def infoClasificada(self):
        return self.__mi_modelo.clasificados_cantidad()
        
def main():
    app = QApplication(sys.argv)
    mi_vista = VentanaPrincipal()
    mi_modelo = Hospital()
    mi_coordinador = Coordinador(mi_vista,mi_modelo)
    mi_vista.setControlador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    
    main()