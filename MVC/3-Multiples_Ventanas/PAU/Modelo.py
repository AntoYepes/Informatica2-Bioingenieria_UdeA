import datetime
import os

class Paciente:
    def __init__(self):
        self.__nombre="" 
        self.__cedula=0 
        self.__edad = 0
        self.__genero = ''
        self.__visitas = {} #un paciente puede tener varias visitas pero no el mismo día
        
    def AsignarNombre(self, n):
        self.__nombre= n 

    def AsignarCedula(self, c):
        self.__cedula= c 
        
    def AsignarEdad(self, n):
        self.__edad = n
        
    def AsignarGenero(self, n):
        self.__genero = n
    
    def VerNombre(self):
        return self.__nombre 

    def VerCedula(self):
        return self.__cedula 
    
    def VerEdad(self):
        return self.__edad 

    def VerGenero(self):
        return self.__genero
   
    def verVisita(self, f):
        return self.__visitas[f]
 
    def verificarExistenciaVisita(self,f):
        return f in self.__visitas

    def ingresarVisitas(self,v):
        self.__visitas = v
        
        
class Visita:
    def __init__(self):
        self.__fecha = ''
        self.__electro = ''
        self.__notas = ''
        #La visita tiene una clase indice que se inicializa vacia
        self.__indice = {} # Solo se guarda un objeto tipo Indices  

    def verFecha(self):
        return self.__fecha
    def asignarFecha(self, f):
        self.__fecha = f

    def verElectro(self):
        return self.__electro
    def asignarElectro(self, r):
        self.__electro = r

    def verNotas(self):
        return self.__notas
    def asignarNotas(self, n):
        self.__notas = n

    def verIndice(self):
        return self.__indice
    def asignarIndice(self,i):
        self.__indice = i 

class Indices:
    def __init__(self):
        self.__potencia_delta = 0           
        self.__potencia_theta = 0     
        self.__potencia_alfa1 = 0     
        self.__pontecia_alfa2 = 0     
        self.__pontecia_gamma = 0     
        
    def asignarDelta(self, p):
        self.__potencia_delta = p
        
    def asignarTheta(self ,p):
        self.__potencia_theta = p
        
    def asignarAlfa1(self ,p):
        self.__potencia_alfa1= p
        
    def asignarAlfa2(self, p):
        self.__pontecia_alfa2 = p

    def asignarGamma(self, p):
        self.__pontecia_gamma = p
        
    def verDelta(self):
        return self.__potencia_delta
    def verTheta(self):
        return self.__potencia_theta
    def verAlfa1(self):
        return self.__potencia_alfa1
    def verAlfa2(self):
        return self.__pontecia_alfa2
    def verGamma(self):
        return self.__pontecia_gamma
  
    
class Servicio:
    def __init__(self):
        self.__pacientes = {}
        self.__visitas = {}
    
    def verficarCedula(self, c):
        return c in self.__pacientes
    
    def verificarVisitas(self, f):
        return f in self.__visitas
    
    def AgregarPaciente(self,n,c,e,g,i):
        # Verficiar si el paciente existe
        if self.verficarCedula(c) == False:
            # En caso de que no exista, cre un nuevo paciente
            p = Paciente()
            p.AsignarNombre(n)
            p.AsignarCedula(c)
            p.AsignarEdad(e)
            p.AsignarGenero(g)
            p.ingresarVisitas(i)
            #p.cVisitas(informacion)
            #guarda la infromación en el diccionario paciente
            #self.__pacientes[c] = p 
            self.__pacientes[p.VerCedula()] = p
            return 'EL paciente se ha ingresado exitosamente'
        else: 
            return 'El paciente ya está en el sistema'
   

    #def AgregarVisitas(self,c,f,e,n):
    #    if self.verificarVisitas(f) == False:
    #        if self.verficarCedula(c) == True:
    #         p = Paciente()
    #         v = Visita()
    #         v.verFecha(f)
    #         v.verElectro(e)
    #         v.verNotas(n)
    #        #agregar visitas en paciente
    #         self.__pacientes[p.ingresarVisitas(f)] = v
    #         return 'Visita ingresada exitosamente'
    #    else:
    #        'El paciente ya tiene una visita con la fecha ingresada'
    
    def eliminarCedula(self, c):
        del self.__pacientes[c.verCedula()]
        
    def recuperarInfo(self, c): #recupera la información del paciente por medio de la cedula
        return self.__pacientes[c]
    
    
        
            
        
        