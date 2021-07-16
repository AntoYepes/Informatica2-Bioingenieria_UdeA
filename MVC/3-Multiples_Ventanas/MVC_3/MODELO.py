#MODELO
class BaseDatos:
    # Constructor
    def __init__(self):
        self.__nombre = ''
        self.__cedula = ''
        
    def setNombre(self, n):
        self.__nombre = n

    def setCedula(self, c):
        self.__ce = c
    
    def validarUsuario(self, n, c):
        return (self.__nombre == n) and (self.__cedula == c)
    