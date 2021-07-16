import sys
from PyQt5.QtWidgets import QApplication
from VISTA import VentanaPrincipal

class Coordinador:
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo
        
    def recibirInfoLogin(self, u, d):
        # Verificamos si el documento ya existe
        if self.__mi_modelo.verificarExistencia(d) == True:
            return 'El documento ya existe'
        else:
            self.__mi_modelo.IngresarUsuario(u, d)
            return 'Usuario ingresado con exito'
    
    def recibirInfoNum(self, n):
        self.__mi_modelo.ingresarNum(n)
        