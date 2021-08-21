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
        
    def inicializar_vector(self):
        return self.__mi_modelo.reiniciar_matriz()

    def obtener_valor(self, valx, valy):
        return self.__mi_modelo.obtener_valor_matriz(valx, valy)
    
    def agregar_valores(self, valx, valy):
        return self.__mi_modelo.agregar_valores_lista(valx, valy)
    
    def tamano(self):
        return self.__mi_modelo.tamano_lista()
    
    def validar_valores(self):
        return self.__mi_modelo.validar_parejas()
    
    def agregar_posic(self, valor):
        return self.__mi_modelo.agregar_posic_encontradas(valor)
    
    def reiniciar_posic(self):
        return self.__mi_modelo.reiniciar_posic_encontradas()
    
    def devolver_coord(self, position):
        return self.__mi_modelo.devolver_coord(position)
    
    def verif_boton(self, coordx, coordy):
        return self.__mi_modelo.validacion_boton_press(coordx, coordy)
    
    def tamano_posic(self):
        return self.__mi_modelo.tamano_posic_encontradas()
    
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
