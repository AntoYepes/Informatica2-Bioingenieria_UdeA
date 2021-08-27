import sys
from PyQt5.QtWidgets import QApplication
from Vista import VentanaPrincipal
from Modelo import Sistema

#La clase coordinador
class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    def infoPasiva(self, no_ref, tipo_prot, nombre, cubrimiento, zona):
        if self.__mi_modelo.verificarExiste(no_ref) == True: #esto debe arrojar true o false (si sale true, la ref ya esta, entonces msm)
            return'Ya existe la referencia'
        else:
            self.__mi_modelo.agregarPasiva(no_ref, tipo_prot, nombre, cubrimiento, zona)
            return'Informacion Pasiva ingresada con exito'
        
    def infoMecanica(self, no_ref, tipo_prot, nombre, cubrimiento, zona, accionamiento, material, sujecion):
        
        if self.__mi_modelo.verificarExiste(no_ref) == True: #esto debe arrojar true o false (si sale true, la ref ya esta, entonces msm)
            return'Ya existe la referencia'
        else:
            self.__mi_modelo.agregarMecanica(no_ref, tipo_prot, nombre, cubrimiento, zona, accionamiento, material, sujecion)
            return'Informacion Mecanica ingresada con exito'
        
    def infoElectrica(self, nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software):
        self.__mi_modelo.agregarElectrica(nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software)
        
    def infoElectrica(self, nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software, sensores):
        self.__mi_modelo.agregarMio(nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software, sensores)
        
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