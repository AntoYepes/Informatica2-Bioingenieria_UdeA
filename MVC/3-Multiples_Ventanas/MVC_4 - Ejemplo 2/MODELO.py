# MODELO
# Se requiere un sistema que permita gestionar pacientes. 
#Cada paciente tiene información de: 
    #nombre, cédula, medicamentos. 
    # Cada medicamento tiene información de: 
        # nombre y dosis.
# El sistema debe permitir
# • Ingresar un paciente, cada paciente con múltiples
# medicamentos. No pueden haber pacientes duplicados
# • Agregar un medicamento a un paciente con una cédula
# dada
# • Salir, guardando toda la información recolectada

class Medicamento:
    def __init__(self):
        self.__nombre = ''
        self.__dosis =  0
        self.__servicio = ''
        
    def setNombre(self, n):
        self.__nombre = n
    def setDosis(self, d):
        self.__dosis = d
    def setServicio(self, s):
        self.__servicio = s
        
    def getNombre(self):
        return self.__nombre
    def getDosis(self):
        return self.__dosis
    def getServicio(self):
        return self.__servicio
    
class Paciente:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
        self.__medicamentos = {}
        
    # Propiedades
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    
    def setNombre(self, no):
        self.__nombre = no
    def setCedula(self, c):
        self.__cedula = c
        
    def tieneMedicamento(self, nombre):
        return nombre.lower() in self.__medicamentos
    def asignarMedicamentos(self, medicamentos):
        self.__medicamentos = medicamentos
    def asignarMedicamento(self, m):
        self.__medicamentos[m.getNombre().lower()] = m
        
class Servicio:
    def __init__(self):
        self.__pacientes = {}
        
    def agregarPaciente(self, n, c, medicamentos):
        # Creo el objeto
        p = Paciente()
        p.setNombre(n)
        p.setCedula(c)
        p.asignarMedicamentos(medicamentos)
        # guardo el paciente, la clave es la cedula
        self.__pacientes[c] = p
        
    def verificarPaciente(self, c):  # Verificamos con la cedula
        return c in self.__pacientes
    
    def agregarMedicamente(self, c, nm, dm):
        # Creo el objeto
        m = Medicamento()
        m.setNombre(nm)
        m.setDosis(dm)
        # recuperar el paciente del diccionario
        paciente = self.__pacientes[c]
        paciente.asignarMedicamento(m)
        # vuelvo a guardar el paciente
        self.__pacientes[c] = paciente
        
    def verificarMedicamento(self, c, nm):
        # recuperar el paciente del diccionario
        paciente = self.__pacientes[c]
        return paciente.tieneMedicamento(nm)
    
        
        