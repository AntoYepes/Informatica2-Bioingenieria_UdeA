#%%CONTROLADOR
import sys
from PyQt5.QtWidgets import QApplication
from VISTA import VentanaPrincipal
from MODELO import Sistema

#La clase coordinador
class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    # Metodos que enlazan vista, controlador y modelo
    def agregarMedicamento(self, n, r, f, e, c):
        if self.__mi_modelo.verificarExistencia(r) == True:
            return 'Medicamento ya existe'
        else:
            self.__mi_modelo.agregarMedicamento( n, r, f, e, c)
            self.__mi_modelo.show()
            return 'Medicamento agregado con exito'
        
    def aumentarStock(self, r, c):
        if self.__mi_modelo.verificarExistencia(r) == True:
            self.__mi_modelo.aumentarStock(r, c)   
        else:
            return 'El medicamento no existe'
    
    def disminuirStock(self, r, c):
        if self.__mi_modelo.verificarExistencia(r) == True:
            self.__mi_modelo.disminuirStock(r, c) 
        else:
            return 'El medicamento no existe'
    
    def cantidadStock(self, r):
        if self.__mi_modelo.verificarExistencia(r) == True:
            return self.__mi_modelo.cantidadStock(r)
        else:
            return 'El medicamento no existe'
    
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
    
    

# %%
