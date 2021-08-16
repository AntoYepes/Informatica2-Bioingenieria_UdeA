
import os
import datetime

class Indices:
    def __init__(self):
        #Atributos de la clase
        self.__pot_d = 0
        self.__pot_t = 0
        self.__pot_a1 = 0
        self.__pot_a2 = 0
        self.__pot_b = 0
        self.__pot_g = 0

    def verPot_D(self):
        return self.__pot_d
    def asignarPot_D(self,p):
        self.__pot_d = p

    def verPot_T(self):
        return self.__pot_t
    def asignarPot_T(self,p):
        self.__pot_t = p

    def verPot_A1(self):
        return self.__pot_a1
    def asignarPot_A1(self,p):
        self.__pot_a1 = p

    def verPot_A2(self):
        return self.__pot_a2
    def asignarPot_A2(self,p):
        self.__pot_a2 = p

    def verPot_B(self):
        return self.__pot_b
    def asignarPot_B(self,p):
        self.__pot_b = p

    def verPot_G(self):
        return self.__pot_g
    def asignarPot_G(self,p):
        self.__pot_g = p

class Visitas:
    def __init__(self):
        #Atributos de la clase
        self.__fecha = ''
        self.__registro = ''
        self.__notas = ''
        #La visita tiene una clase indice que se inicializa vacia
        self.__indice = {} # Solo se guarda un objeto tipo Indices  

    def verFecha(self):
        return self.__fecha
    def asignarFecha(self,f):
        self.__fecha = f

    def verRegistro(self):
        return self.__registro
    def asignarRegistro(self,r):
        self.__registro = r

    def verNotas(self):
        return self.__notas
    def asignarNotas(self,n):
        self.__notas = n

    def verIndice(self):
        return self.__indice
    
    def asignarIndice(self,i):
        self.__indice[1] = i

class Paciente:
    def __init__(self):
        #Atributos de la clase
        self.__nombre = ''
        self.__edad = 0
        self.__cedula = 0
        self.__genero = ''
        #Un paciente tiene muchas visitas, en este ejemplo los trabajamos
        #como diccionarios
        self.__visitas = {} # Clave-->fecha, valor-->Visita

    def verNombre(self):
        return self.__nombre
    def asignarNombre(self,n):
        self.__nombre = n

    def verEdad(self):
        return self.__edad
    def asignarEdad(self, e):
        self.__edad = e
        
    def verCedula(self):
        return self.__cedula
    def asignarCedula(self,c):
        self.__cedula = c

    def verGenero(self):
        return self.__genero
    def asignarGenero(self,g):
        self.__genero = g

    def verVisita(self, f):
        return self.__visitas[f]
        
    def verificarExistenciaVisita(self,f):
        return f in self.__visitas

    def ingresarVisitas(self,v):
        self.__visitas[v.verFecha()] = v
    
    def eliminarVisita(self,v):
        del self.__visitas[v.verFecha()]

class Sistema:
    def __init__(self):
        self.__pacientes = {} #la llave seria la cedula y el valor el paciente dueño de dicha cedula

    def verificarExistePaciente(self, c):
        return c in self.__pacientes

    def ingresePac(self, p):
        self.__pacientes[p.verCedula()]=p

    def eliminarPac(self,p):
        del self.__pacientes[p.verCedula()]

    def recuperaPac(self,c):
        return self.__pacientes[c]

    def AgregarPaciente(self, nombre, edad, cedula, genero):
            #creo el objeto
            p = Paciente() 
            p.asignarNombre(nombre)
            p.asignarEdad(edad)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            #guardo el paciente. LA CLAVE ES LA CEDULA
            self.__pacientes[cedula] = p 
            
    def VerificarPaciente(self, c):
        return c in self.__pacientes 

    def AgregarVisitas(self, fecha, registro, notas):
        #creo el objeto
        v = Visitas()
        v.asignarFecha(fecha)
        v.asignarRegistro(registro)
        v.asignarNotas(notas)
        cedula = Paciente.verCedula()
        paciente = Sistema.recuperaPac()
        #asignarle al paciente el nuevo medicamento
        paciente.ingresarVisita(v) 
        #vuelvo a guardar el paciente
        self.__pacientes[cedula] = paciente 
        
    def verificarExistenciaVisita(self,f):
        return f in self.__visitas
        
    def AgregarIndices(self, delta, theta, alfa1, alfa2, betha, gamma):
        I = Indices()
        I.asignarPot_D(delta)
        I.asignarPot_T(theta)
        I.asignarPot_A1(alfa1)
        I.asignarPot_A2(alfa2)
        I.asignarPot_B(betha)
        I.asignarPot_G(gamma)
        p = Paciente.asignarIndice(I)
        self.__pacientes[Paciente.verCedula()] = p 
    