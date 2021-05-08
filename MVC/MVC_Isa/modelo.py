#MODELO
class Medicamento:
    def __init__(self):
        self.__nombre = ''
        self.__referencia = 0
        self.__fecha = ''
        self.__cantidad = 0
        self.__efectos = ''
        
    def getNombre(self):
        return self.__nombre
    def getReferencia(self):
        return self.__referencia
    def getFecha(self):
        return self.__fecha
    def getCantidad(self):
        return self.__cantidad
    def getEfectos(self):
        return self.__efectos
    
    def setNombre(self, n):
        self.__nombre = n
    def setReferencia(self, r):
        self.__referencia = r
    def setFecha(self, f):
        self.__fecha = f
    def setCantidad(self, c):
        self.__cantidad = c
    def setEfectos(self, e):
        self.__efectos = e
        
class Sistema:
    def __init__(self):
        self.__stock = {}
        
    # Metodos que se enlazan con controlador
    def agregarMedicamento(self, n, r, f, e, c):
        #se crea el objeto medicamento
        m = Medicamento()
        m.setNombre(n)
        m.setReferencia(r)
        m.setFecha(f)
        m.setEfectos(e)
        m.setCantidad(c)
        # Guardamos la informacion en el diccionario
        self.__stock[m.getReferencia()] = m
         
    #verificar existencia
    def verificarExistencia(self, r):
        return r in self.__stock
    
    def aumentarStock(self, r, c):
        return self.__stock[r].setCantidad(c) 
    
    def disminuirStock(self, r, c):
        return self.__stock[r].setCantidad(c)
     
    def cantidadStock(self, r):
        return self.__stock[r].getCantidad()
    
    def show(self):
        print(self.__stock)
    
        
        
        
        
        
        