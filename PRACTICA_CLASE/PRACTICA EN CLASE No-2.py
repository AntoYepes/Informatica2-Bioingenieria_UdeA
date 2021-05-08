# PRACTICA EN CLASE NO-2
class Estudiante:
    # Estos serian los atributos
    # Metodo __init__(self)
    # init = constructor; se ejecita automat una vez aplicamos la clase
    # self = reconocer el propio objeto 
    def __init__(self, n, c, cr):
        self.nombre = n
        self.cedula = c
        self.carrera = cr
    
    def estudiar(self, m):
        self.materia = m
        pass
        
    def jugar(self):
        pass
        
# Se crea el objeto    
student = Estudiante('Anto', 1234, 'Bio')
# student_2 = Estudiante()
student.nombre = 'Lia'

# Herencia = otras clases hijas heredan de la clase padre
# class Hijo(Padre):
#     def __init__(self, tipo,):
#         # Constructor siempre hay que hacerlo
#         Padre.__init__(self,)

# ENCAPSULAMIENTO
# proteger a los atributos
# self.__nombre =  nombre

#%% 
class Coche:
    def __init__(self, p, c, m, v, b):
        self.__placa = p
        self.__color = c
        self.__modelo = m
        self.__velocidad = v
        self.__carburante = b
    
    def arrancar(self):
        if self.__velocidad == 0:
            print('No esta en movimiento')
        else:
            print('Esta en movimiento')
            
    def ir(self):
        if self.__velocidad != 0:
            destino = input('Ingrese el destino: ')
            print(destino)
            
    def parar(self):
        if self.__velocidad == 0:
            print('El carro se detuvo')
        else:
            print('Esta en movimiento')
        
    def girar(self):
        if self.__velocidad != 0:
            direccion_giro = input('Ingrese R right or L left: ')
            print(direccion_giro)
        pass
        
ferrari = Coche('123ARG', 'Rojo', 2021, 90, 'frez')    
ferrari.parar()

#%% HERENCIA:
    # BIO Y ESTUDIANTE
# clase padre    
class Estudiante:
    # se utiliza el constructor
    def __init__(self, n, a, c, cr):
        # atributos
        self.__nombre = n
        self.__apellido = a
        self.__cedula = c
        self.__carrera = cr
    # metodo    
    def estudiar(self):
        if self.__carrera == 'Bio':
            return '{} esta en la carrera {}'.format(self.__nombre, self.__carrera)

# se crea clase hija        
class EstudianteBio(Estudiante):
    def __init__(self, n, a, c, cr, m, s):
        Estudiante.__init__(self, n, a, c, cr)
        self.__materia = m
        self.__semestre = s
        
    def practicas(self):
        if self.__semestre == 10:
            print('El estudiante ya esta realizando las practicas ')
        else:
            print('El estudiante aun esta en semestres bajos')
            
student = EstudianteBio('Antonia', 'Yepes', '123456', 'Bio', 'Info2', 3)
print(student.estudiar())

#%% EJERCICIO DE ABSTRACCION No. 1
class Casa:
    
    def __init__(self, c, t, u, s):
        self.__color = c
        self.__tamaño = t
        self.__ubicacion = u
        self.__costo = s
        
    def cc(self):
        print('La cada esta ok')
        
departamento = Casa('blanca', 'grande', 'llanogrande', 13000000)
pen_house = Casa('plata', 'gigante', 'via las palmas', 20000000000)

#%% 
class Casa:
    
    def __init__(self, t, ti, c, u, ct):
        self.__tamaño = t
        self.__tipo = ti
        self.__color = c
        self.__ubicacion = u
        self.__costo = ct
        
    def verCasa(self):
        return self.__tipo
    
    def verCosto(self):
        return self.__costo
    
    def verColor(self):
        return self.__color
    
casa1 = Casa('Grande', 'Pen_house', 'Blanco', 'Via las Palmas', 5000000000)
print(casa1.verCosto())
print(casa1.verColor())



#%%
class Casa:
    
    def __init__(self, t, ti, c, u, ct):
        self.tamaño = t
        self.tipo = ti
        self.color = c
        self.ubicacion = u
        self.costo = ct
        
    def verCasa(self):
        return self.tipo
    
    def verCosto(self):
        return self.costo
    
    def verColor(self):
        return self.color
    
casa1 = Casa('Grande', 'Pen_house', 'Blanco', 'Via las Palmas', 5000000000)
print(casa1.verCosto())
print(casa1.verColor())
print(casa1.tamaño)

        



