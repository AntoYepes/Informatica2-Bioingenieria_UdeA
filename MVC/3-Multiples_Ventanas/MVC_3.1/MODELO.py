# MODELO PRACTICA

class BaseDato:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
        
    def setNombre(self, n):
        self.__nombre = n
    def setCedula(self, c):
        self.__cedula  = c
        
    def validarUsuario(self, n, c):
        return (self.__nombre == n) and (self.__cedula == c)
        
