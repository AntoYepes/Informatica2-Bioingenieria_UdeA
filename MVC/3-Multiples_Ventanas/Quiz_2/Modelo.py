class Paciente:
    # Constructor
    def __init__(self):
        # Atributos
        self.__nombre = str
        self.__cedula = 0
        self.__edad = 0
        self.__peso = 0
        self.__estatura = 0
        self.__genero = ''
        self.__presionArterial = 0
        self.__examen = [] #None

    # PROPIEDADES
    # Metodos get
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def getEdad(self):
        return self.__edad
    def getPeso(self):
        return self.__peso
    def getEstatura(self):
        return self.__estatura
    def getGenero(self):
        return self.__genero
    def getPresionArterial(self):
        return self.__presionArterial
    def getExamen(self):
        return self.__examen

    #Metodos set
    def setNombre(self, n):
        self.__nombre = n
    def setCedula(self, c):
        self.__cedula = c
    def setEdad(self, e):
        self.__edad = e
    def setPeso(self, p):
        self.__peso = p
    def setEstatura(self, es):
        self.__estatura = es
    def setGenero(self, g):
        self.__genero = g
    def setPresionArterial(self, pa):
        self.__presionArterial = pa
    def setExamen(self, e):
        self.__examenSangre = e

# Clase Hospital
class Hospital:
    # Constructor
    def __init__(self):
        # Atributos
        self.__pacientes = {}
        self.__clasificados = []
        
    # METODO PARA PACIENTES
    # Metodo verificar existencia paciente
    def verificarExistencia(self, c):
        return c in self.__pacientes

    # Metodo ingresar paciente
    def ingresarPaciente(self, pac):
        self.__pacientes[pac.getCedula()] = pac

    # Metodo eliminar paciente
    def eliminarPaciente(self, c):
        del self.__pacientes[c]

    # Metodo recuperar paciente (ver la info del paciente)
    def recuperarPaciente(self, c):
        return self.__pacientes[c]
    
    def agregarInfoPac(self, nombre, cedula, edad, peso, estatura, genero, presion, resultado):
        p = Paciente()
        p.setNombre(nombre)
        p.setCedula(cedula)
        p.setEdad(edad)
        p.setPeso(peso)
        p.setEstatura(estatura)
        p.setGenero(genero)
        p.setPresionArterial(presion)
        p.setExamen(resultado)
        self.__pacientes[cedula] = p
            
        if (int(resultado) > 7) and (int(resultado) < 19):
            msm = 'normal'
        elif int(resultado) >= 20:
            msm = 'Disminucion de la funcion renal'
            self.__clasificados.append(resultado)
            
        return msm

    def clasificados_cantidad(self):
        return len(self.__clasificados)