#%% CONTROLADOR
import sys
from VISTA import VentanaLogin
from PyQt5.QtWidgets import QApplication
from MODELO import Sistema

class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
    def infoLogin(self, u, d):
        if self.__mi_modelo.verificarExistencia(d) == True:
            return 'El jugador ya existe'
        else: 
            self.__mi_modelo.recibirInfoLogin(u, d)
            return 'Jugador ingresado con exito'
        
    def guessNum(self, n):
        return self.__mi_modelo.guessing(n)
        
    def matrix_button(self):
        return self.__mi_modelo.matrix()
    
    def match(self, num):
        return self.__mi_modelo.match_review(num)
    
def main():
    app = QApplication(sys.argv)
    mi_vista = VentanaLogin()
    mi_modelo = Sistema()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)
    mi_vista.setControlador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
# %%
