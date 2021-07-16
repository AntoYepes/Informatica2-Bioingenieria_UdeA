class Usuario:
    def __init__(self):
        self.__usuario = ''
        self.__documento = 0
        
    def getUsuario(self):
        return self.__usuario
    def getDocumento(self):
        return self.__documento
    
    def setUsuario(self, u):
        self.__usuario = u
    def setDocumento(self, d):
        self.__documento = d

class Sistema:
    def init(self):
        self.__diccionario = {}
     
    # Creamos metodo para verificar el documento este se enlaza con controlador   
    def verificarExistencia(self, d):
        return d in self.__diccionario
    
    