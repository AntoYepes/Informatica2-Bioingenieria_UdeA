import os
import datetime

class Indices:
 #constructor
    def __init__(self):
        #Atributos de la clase
        self.__pot_d = 0
        self.__pot_t = 0
        self.__pot_a1 = 0
        self.__pot_a2 = 0
        self.__pot_b = 0
        self.__pot_g = 0

 # Metodos ver y asignar
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
        self.__indice = None # Solo se guarda un objeto tipo Indices  


 # Métodos ver y asignar
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
        self.__indice = i 

class Paciente:
    def __init__(self):
        #Atributos de la clase
        self.__nombre = ''
        self.__cedula = 0
        self.__edad= 0
        self.__genero = ''
        #Un paciente tiene muchas visitas, en este ejemplo los trabajamos
        #como diccionarios
        self.__visitas = {} # Clave-->fecha, valor-->Visita

 #Métodos
    def verNombre(self):
        return self.__nombre
    def asignarNombre(self,n):
        self.__nombre = n

    def verCedula(self):
        return self.__cedula
    def asignarCedula(self,c):
        self.__cedula = c
    
    def verEdad(self):
        return self.__edad
    def asignarEdad(self,e):
        self.__edad=e

    def verGenero(self):
        return self.__genero
    def asignarGenero(self,g):
        self.__genero = g

    def verVisita(self, f):
        return self.__visitas[f]
        
    def verificarExiste(self,f):
        return f in self.__visitas

    def ingresarVisitas(self,v):
        self.__visitas[v.verFecha()] = v
    
    def eliminarVisita(self,v):
        del self.__visitas[v.verFecha()]

class Sistema:
    def __init__(self):
        self.__pacientes = {} #la llave seria la cedula y el valor el paciente dueño de dicha cedula
        self.__visitas={}
    
    def verificarVisita(self, f):
        return f in self.__visitas

    def verificarExiste(self,c):
        return c in self.__pacientes

    def ingresePac(self,n, c,e,g,v,i ):
        if self.verificarExiste(c)==False:
            p =Paciente()
            p.asignarNombre(n)
            p.asignarCedula(c)
            p.asignarEdad(e)
            p.asignarGenero(g)
            #numVis = input(("Ingrese el numero de visitas: "))
            #for i in range(0,numVis):
            # v = Visitas()
            # v.asignarFecha(input("ingrese Fecha: "))
            # if p.verificarExiste(v.verFecha()) == True:
                #    print("Ya existe la visita: ")
                #   continue
                #v.asignarRegistro(os.getcwd()+f'/Pacientes_{p.verCedula()}')
                #v.asignarNotas(input("Ingrese Observaciones"))
                #ind = Indices()
            # ind.asignarPot_A1(float(input("Ingrese a1= ")))
                #ind.asignarPot_A2(float(input("Ingrese a2= ")))
                #ind.asignarPot_B(float(input("Ingrese b= ")))
                #ind.asignarPot_D(float(input("Ingrese d= ")))
                #ind.asignarPot_G(float(input("Ingrese g= ")))
                #ind.asignarPot_T(float(input("Ingrese t= ")))
                #v.asignarIndice(ind)
            #p.ingresarVisitas(i)
            self.__pacientes[p.verCedula()]=p
        else:
            return "el paciente ya existe"

    def eliminarPac(self,p):
        del self.__pacientes[p.verCedula()]

    def recuperaPac(self,c):
        return self.__pacientes[c]

    def ingresarVisitas(self,v):
        self.__visitas[v.verFecha()] = v

