# MODELO:
    # Aca iria la logica
# Creamos clase base de datos
class BaseDatos:
    # Constructor
    def __init__(self):
        # Atributos, login y password
        self.__login =  ''
        self.__password = ''
     
    # PROPIEDADES
    def setLogin(self, l):
        self.__login = l

    def setPassword(self, p):
        self.__password = p
        
    # Metodo para validar 
    def validarUsuario(self, l, p):
        return (self.__login == l) and (self.__password == p)

