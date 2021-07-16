# MODELO
# crear aeropuerto - pax - vuelo
class Vuelo:
    def __init__(self):
        self.__numero_vuelo = 0
        self.__fecha_vuelo = ''
        
    def getNumeroVuelo(self):
        return self.__numero_vuelo
    def getFechaVuelo(self):
        return self.__fecha_vuelo
    
    def setNumeroVuelo(self, nv):
        self.__numero_vuelo = nv
    def setFechaVuelo(self, fv):
        self.__fecha_vuelo = fv
        
class Pasajero:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
        self.__vuelo = {}
        
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    
    def setNombre(self, n):
        self.__nombre = n
    def setCedula(self, c):
        self.__cedula = c
        
    def tieneVuelo(self, numVuelo):
        return numVuelo.lower() in self.__vuelo
    def asignarVuelos(self,vuelo):
        self.__vuelo = vuelo
    def asignarVuelo(self, v):
        self.__vuelo[v.getNumeroVuelo().lower()] = v
        
class Aeropuerto:
    def __init__(self):
        self.__pasajeros = {}
        
    def agregarPasajero(self, nombre, cedula, vuelo):
        # Creo el objeto
        pax = Pasajero()
        pax.setNombre(nombre)
        pax.setCedula(cedula)
        pax.asignarVuelos(vuelo)
        self.__pasajeros[cedula] = pax
        
    def verificarPasajero(self, cedula):
        return cedula in self.__pasajeros
    
    def agregarVuelo(self, cedula, numVuelo, fechaVuelo):
        v = Vuelo()
        v.setNumeroVuelo(numVuelo)
        v.setFechaVuelo(fechaVuelo)
        pasajero = self.__pasajeros[cedula]
        pasajero.asignarVuelo(v)
        self.__pasajeros[cedula] = pasajero
        
    def verificarVuelo(self, cedula, numVuelo):
        pasajero = self.__pasajeros[cedula]
        return pasajero.tieneVuelo(numVuelo)
    
    
        
        
