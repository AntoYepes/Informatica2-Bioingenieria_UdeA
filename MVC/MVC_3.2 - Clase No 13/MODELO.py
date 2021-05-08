# MODELO CLASE 13
class Usuario:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
    
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
        
    def setNombre(self, n):
        self.__nombre = n
    def setCedula(self, c):
        self.__cedula  = c
        
class BaseDatos:
    def __init__(self):
        self.__lista_usuario = {}
        
    def ingresarUsuario(self, n, c):
        if self.validarUsuario(c) == True:
            return 'El usuario ya existe'
        else:
            u = Usuario()
            u.setNombre(n)
            u.setCedula(c)
            self.__lista_usuario[c] = u
            return 'Usuario ingresado'
    
    def validarUsuario(self, c):
        return c in self.__lista_usuario
        
    
    