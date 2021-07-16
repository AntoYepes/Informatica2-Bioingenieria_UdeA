#%% 
class Persona():
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
        self.__genero = ''
        
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarCedula(self, c):
        self.__cedula = c
    def asignarGenero(self, g):
        self.__genero = g
        
class Paciente(Persona):
    def __init__(self):
        super().__init__()
        self.__servicio = ''
        
    def verServicio(self):
        return self.__servicio
    def asignarServicio(self, s):
        self.__servicio = s
        
pac = Paciente()
pac.asignarNombre('Antonia')
pac.asignarGenero('F')
pac.asignarCedula(1234)
print(pac.verNombre())

class Empleado_Hospital(Persona):
    def __init__(self):
        super().__init__()
        self.__turno = ''
        
    def verTurno(self):
        return self.__turno
    def asignarTurnos(self, t):
        self.__turno = t
        
class Enfermera(Empleado_Hospital):
    def __init__(self):
        self.__rango
    
    def verRango(self):
        return self.__rango  
    def asignarRango(self, r):
        self.__rango = r
        
class Medico(Empleado_Hospital):
    def __init__(self):
        self.__especialidad = ''
    def verEspecialidad(self):
        return self.__especialidad 
    def asignarEspecialidad(self, e):
        self.__especialidad = e
    
while True:
    listaPacientes = []
    for i in range(2):
        p = Paciente()
        p.asignarNombre(input('Ingrese el nombre del paciente: '))
        p.asignarCedula(int(input('Ingrese la cc: ')))
        p.asignarGenero(input('Ingresar genero: '))
        p.asignarServicio(input('Ingrese el servicio a solicitar: '))
        # Para guardar la info
        listaPacientes.append(p)
        # archivo = open('Pacientes.txt', 'a')
        # archivo.write(p.verNombre())
        # archivo.write(p.verCedula())
        # archivo.write(p.verGenero())
        # archivo.write(p.asignarServicio())
        
    break
        