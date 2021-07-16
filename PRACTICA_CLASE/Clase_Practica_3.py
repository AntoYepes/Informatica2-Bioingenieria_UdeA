# id:
    # retorna la identidad de donde esta
    # guardado el objeto

class Materia:
    def __init__(self, s, n, c):
        self.__semestre = s
        self.__nombre = n
        self.__cedula = c
    # Propiedades: ver y asignar    
    def verNombre(self):
        return self.__nombre
    
    def asignarNombre(self, n):
        self.__nombre = n
        
    def borrarNombre(self):
        del self.__nombre
    
    def verCedula(self):
        return self.__cedula
    
    def asignarCedula(self,c):
        self.__cedula = c
        
    def verSemestre(self):
        return self.__semestre 
    
        
m1 = Materia
m1.asignarNombre('Anto')

print(id(m1))

# privado 2 _ _ metodos de la propia clase
# publico sin guion bajo
# protegido 1 _ metodos de la propia clase y herencia


#%% Donde existen las variables
# variables de instancia = dentro de constructor
# variables

#%% DIAGRAMA DE CLASES
class Aviones:
    def __init__(self):
        self.__modelo_avion = ''
        self.__cant_motores = 0
        self.__vel_crucero = 0
        self.__carga = 0
        self.__destino = ''
        
    def verModeloAvion(self):
        return self.__modelo_avion
    def verCantMotores(self):
        return self.__cant_motores
    def verVelCrucero(self):
        return self.__vel_crucero
    def verCarga(self):
        return self.__carga
    def verDestino(self):
        return self.__destino
    
    def asignarModeloAvion(self, m):
        self.__modelo_avion = m
    def asignarCantMotores(self, c):
        self.__cant_motores = c
    def asignarVelCrucero(self, v):
        self.__vel_crucero = v
    def asignarCarga(self, g):
        self.__carga = g
    def asignarDestino(self, d):
        self.__destino = d
        
    def acelerar(self):
        if self.__vel_crucero == 0:
            print('El avion debe acelerar ')
        else:
            print('El avion esta quieto')
            
    def elevarse(self):
        if self.__vel_crucero == 10000:
            print('El avion debe elevarse')
        else:
            print('El avion esta despegando')
            
    def girar(self):
        print('Girar a la derecha')
        
    def descender(self):
        print('Se ha arrivao al destino')
        
avion = Aviones()        
print(avion.elevarse())
print(avion.girar())
print(avion.descender())

#%% EJEMPLO No 1
# En que clase guardo los datos para poder ver los que ya ingrese?
class Persona: 
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
        Persona.__init__(self)
        self.__servicio = ''
        
    def verServicio(self):
        return self.__servicio
    def asignarServicio(self, v):
        self.__servicio = v
    
      
class Empleado_Hospital(Persona):
    def __init__(self):
        super().__init__()
        self.__turno = ''
        
    def verTurno(self):
        return self.__turno
    def asignarTurno(self, t):
        self.__turno = t
        
        
class Enfermera(Empleado_Hospital):
    def __init__(self, t):
        super().__init__(t)
        self.__rango = ''
        
    def verRango(self):
        return self.__rango
    def asignarRango(self, r):
        self.__rango = r
        
        
class Medico(Empleado_Hospital):
    def __init__(self, t):
        super.__init__(t)
        self.__especialidad = ''
        
    def verEspecialidad(self):
        return self.__especialidad
    def asignarEspecialidad(self, e):
        self.__especialidad = e


while True:
    listaPacientes = []
    opcion = input('''
    1. Ingresar datos paciente
    2. Ver datos paciente
    3. Ingresar datos Enfermera
    4. Salir
    :''')
    if opcion == '1':
        pac = Paciente()
        pac.asignarNombre(input('Ingrese el nombre del paciente: '))
        pac.asignarCedula(int(input('Ingrese el numero de cedula: ')))
        pac.asignarGenero(input('Ingrese el genero del paciente: '))
        
        resultado = listaPacientes.append(pac)
    
    elif opcion == '2':
        print(resultado)
        
    elif opcion == '3':
        pass
    elif opcion == '4':
        break
    
    else:
        print('Opcion no valida')

#%% TRADUCIR SIN METODOS

class Vehiculo:
    def __init__(self):
        self.__dueño = ''
        self.__puertas = 0
        self.__ruedas = 0
        
    # metodos de dueño    
    def verDueño(self):
        return self.__dueño
    def asignarDueño(self, d):
        self.__dueño = d
        
    # Metodos de puertas
    def verPuertas(self):
        return self.__puertas
    def asignarPuertas(self, p):
        self.__puertas = p
        
    # Metodos para ruedas
    def verRuedas(self):
        return self.__ruedas
    def asignarRuedas(self, r):
        self.__ruedas = r
        
    # Metodos
    def vehiculo(self):
        print('Este es un vehiculo')
        
    def caracteristicas(self):
        pass
    
# Segunda clase:
    # 1ra clase hija
class Auto(Vehiculo):
    def __init__(self):
        super().__init__()
        self.__descapotable = True
        
    # Metodos de Auto
    def Auto(self):
        print('Este es unn automovil')
    
    def caracteristicas(self):
        pass
    
    def subir(self):
        pass
    def bajar(self):
        pass
    
# 3ra clase:
    # 2nd clase hija
class Camioneta(Vehiculo):
    def __init__(self):
        super().__init__()
        self.__tara = 0.1
        self.__carga = 0.1
        
    # Metodos para camioneta
    def camioneta(self):
        print('Este es una camioneta')
        
    def caracteristicas(self):
        pass
    def cargar(self):
        pass
    
        
        
        