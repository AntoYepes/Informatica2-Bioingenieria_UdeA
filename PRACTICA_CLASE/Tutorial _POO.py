#%% Python Object-Oriented Programming
# VIDEO 1 - Classes and instances
# This is a simple employee class with no attributes and methods
class Employee:
    pass
# diference between a class and a instance of a class
# class = blueprint for creating instances
# Equals employee then each of these are their own unique instances
# of the employee class
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
# They both have different locations here in memory

# Instance variables contain Data that is unique to each instance
# each of these instances have atributes 
# that are unique to them
emp_1.first = 'Antonia'
emp_1.last = 'Yepes'
emp_1.email = 'Antonia.yepes@udea.edu.co'
emp_1.pay = 100000000

emp_2.first = 'Santi'
emp_2.last = 'Martinez'
emp_2.email = 'Santi.ml@udea.edu.co'
emp_2.pay = 60000


# We are gonna use this special init method
# The name, email, pay are all atributes of our class
class Employe:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
emp_1 = Employe('Antonia', 'Yepes', 100000000)

# if we want the ability to perform some kind of action
# we can add some methods to our class

emp_1.fullname()
Employe.fullname(emp_1)
#%% VIDEO 3 - classmethods and staticmethod
class Trab:
    num_of_emps = 0
    raise_amt = 1.04
    
    def __int__(self,first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + '@email.com'
        self.pay = pay
        
        Trab.num_of_emps += 1
        
    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
emp_1 = Trab('Antonia', 'Yepes', 100000000)
emp_2 = Trab('Anto', 'Yepe', 700000000)

Trab.set_raise_amt(1.05)

print(Trab.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#%% FUNCIONES PARA ATRIBUTOS
# Funcion para atributos:
    # sirve para verificar T o F
class Persona:
    edad = 22
    nombre = 'Santiago'
    
doctor = Persona()
print('¿Tiene edad el doctor?: ', hasattr(doctor, 'edad'))

# Funcion para atributos:
    # sirve para renombrar
class Persona1:
    edad = 24
    nombre = 'Antonia'
    
doctor = Persona1()
print('El nombre era:', doctor.nombre)
setattr(doctor, 'nombre', 'Lia')
print('Ahora el nombre es: ', doctor.nombre)
        
# Funcion para atributos:
    # sirve para eliminar un atributo
class Persona2:
    edad = 27
    nombre = 'Ruben'
    pais = 'Colombia'
    
doctor = Persona2()
delattr(doctor, 'pais')

#%% CONSTRUCTORES
#  Metodo constructor:
class Person:
    
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
        
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre, self.año)
    
    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)
    
ingeniero = Person('Ruben', 27)
print(ingeniero.nombre)
print(ingeniero.descripcion())

#%% Metodo constructor
# Modificar un atributo
class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()

print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)

#%% HERENCIA
# Crear una nueva clase a partir de una
# o mas clases existentes:
    # class NombreSubClase(NombreClaseSuperior):
    # class ClaseBase:
        # cuerpo de la clase base
    # class DerivadoClase(ClaseBase):
        # cuerpo de clase derivada
        
# clase padre        
class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    # voy a describir esos atributos en el metodo sig    
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)

# clase hijo de clase Pokemon   
class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipo_ataque)
    
# clase hijo de clase Pokemon
class charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipo_ataque)

# Si quiero ingresar un nuevo de pikachu    
nuevo_pokemon = Pikachu('Boby', 'Electrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('Impacto trueno'))

#%% HERENCIA EJERCICIO 
# Ejemplo practico
# clase padre
class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    
    def ingresarDato(self):
        self.datos = [int(input('Ingresar dato ' + str(i + 1) + ' : ')) for i in range(self.n)] 
        
# clase hija
class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)
        
    def suma(self):
        a,b, = self.datos
        s = a + b
        print('El resultado es: ', s)
        
    def resta(self):
        a,b, = self.datos
        r = a - b
        print('El resultado es: ', r)

# clase hija        
class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math
        a, = self.datos
        print('El resultado es: ', math.sqrt(a))
        
ejemplo = raiz()
print(ejemplo.ingresarDato())    
print(ejemplo.cuadrada())

# FUNCIONES DE PRUEBA - HERENCIA
objeto = op_basicas()
print(isinstance(objeto, op_basicas))

# verificar si la clase hija pertenece a la clase padre
print(issubclass(op_basicas, Calculadora))

#%% HERERNCIA MULTIPLE
class Telefono:
    
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')
    
    def ocupado(self):
        print('En linea...')
        
class Camara:
    
    def __init__(self):
        pass
    def fotografia(self):
        print('tomando foto...')
        
class Reproduccion:
    def __init__(self):
        pass
        
    def reproductormusic(self):
        print('Reproducir musica...')
        
    def reproducirvideo(self):
        print('Reproducir un video...')
        
# combinar las clases anteriores
class SmartPhone(Telefono, Camara, Reproduccion):
    # del para limpiar los recursos
    def __del__(self):
        print('Telefono apagado')
        
movil = SmartPhone()
print(movil.fotografia())
print(movil.llamar())
print(dir(movil))
        
#%% f-STRING
# formatear cadenas. mas legibles y concisos

class Estudiante:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    # representacion informal de una cadena o objeto
    # vamos a devolver un string     
    def __str__(self):
        return f'Hola, que tal soy {self.nombre} {self.apellido} tengo {self.edad} años.'

new_student = Estudiante('Antonia', 'Yepes', 23)
print(f'{new_student}')

#%% f-STRING
class Estudiante1:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    # repr representacion oficial y se debe correr con el codigo
    def __repr__(self):
        return f'Hola, que tal soy {self.nombre} {self.apellido} tengo {self.edad} años.'
    
student1 = Estudiante1('Antonov', 'Quintero', 24)
# !r es para l__repr
print(f'{student1 !r}')

#%% metodo CLASE Y ESTATICOS
# CLASE:
    # Es una plantilla para crear objetos
    
# INSTANCIA:
    # Un objeto se crea usando el constructor de una clase
    # Una vez que el objeto es creado se le conoce como una instancia de la clase
    
# TIPOS DE METODOS:
    # Metodos estaticos
    # Metodos clase
    # Metodos instancia
    
#%% METODOS CLASE
# @classmethod:
    # Este metodo puede ser llamado sin crear una instancia de la clase
class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes
    
    def __repr__(self):
        return f'pastel({self.ingredientes !r})'
    
    # clase de metodo
    @classmethod
    def Pastel_chocolate(cls):
        return cls(['Harina', 'Leche', 'Chocolate'])
    
    @classmethod
    def Pastel_vainilla(cls):
        return cls(['Harina', 'Lecha', 'Vainilla', 'Mantequilla'])

print(Pastel.Pastel_vainilla())

#%% METODO ESTATICO
# @staticmethod:
    # Pueden ser llamados sin tener una instancia de la clase, 
    # ademas este tipo de metodos no tienen acceso al exterior
import math
    
class Postre:
    def __init__(self, ingredientes, tamaño):
       self.ingredientes = ingredientes
       self.tamaño = tamaño
       
    def __repr__(self):
        return(f'Postre({self.ingredientes}, 'f'{self.tamaño})')
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    @staticmethod
    def tamaño_area(A):
        return A ** 2 * math.pi 
    
nuevo_postre = Postre(['Harina', 'Azucar', 'Mantequilla', 'Leche', 'Crema'], 4)
print(nuevo_postre.ingredientes)
print(nuevo_postre.tamaño_area(12))

#%% POLIMORFISMO
# Estas 2 clases tienen algo en comun:
    # Ambos son vehiculos, ambos se desplazan
    # No pueden desplazarse de la misma manera
    # Pueden ser identicos pero sus funciones 
    # y secciones son diferentes
    
class Auto:
    
    rueda = 4
    def desplazamiento(self):
        print('El auto se esta moviento sobre 4 ruedas')
    
class Moto:
    rueda = 2
    def desplazamiento(self):
        print('La moto se esta moviendo sobre 2 ruedas')
        
       
#%% POLIMORFISMO CON HERENCIA

class Animales:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def tipo_animal(self):
        pass
    
class Leon(Animales):
    def tipo_animal(self):
            print('Animal salvaje')
            
class Perro(Animales):
    def tipo_animal(self):
        print('Animal domestico')
        
# creo el objeto y lo enlazo con la clase que me interesa       
nuevo_animal = Leon('Maxi')
nuevo_animal.tipo_animal()
segundo_animal = Perro('Apolo')
segundo_animal.tipo_animal()


#%% POLIMORFISMO CON FUNCIONES, METODOS Y HERENCIA

# POLIMORFISMO CON FUNCION
class Tomate:
    def tipo(self):
        print('Vegetal')
    def color(self):
        print('Rojo')

class Manzana:
    def tipo(self):
        print('Fruta')
    def color(self):
        print('verde')

# Acceder a los metodos dentro de las clases
def funcion(objeto):
    objeto.tipo()
    objeto.color()
    
nuevo_tomate = Tomate()
funcion(nuevo_tomate)

nueva_manzana = Manzana()
funcion(nueva_manzana)

#%% POLIMORFISMO CON METODO

class Colombia:
    # Se crean directamente los metodos
    def capital(self):
        print('Bogota')
    def idioma(self):
        print('En Colombia se habla español')
    
class Francia:
    def capital(self):
        print('Paris')
    def idioma(self):
        print('En Francia se habla frances')

# Poner todos los objetos        
colombiano = Colombia()
frances = Francia()

# Bucle:
for pais in (colombiano, frances):
    pais.capital()
    pais.idioma()
    
#%% POLIMORFISMO CON HERENCIA

class Aves:
    # Metodo
    def volar(self):
        print('La mayoria de las aves pueden volar, pero algunas no')
        
class Aguila(Aves):
    def volar(self):
        print('El aguila pueden volar')
    
class Gallina(Aves):
    def volar(self):
        print('La gallina no puede volar')
        
# creo objeto y vincularlo con la clase
obj_ave = Aves()
obj_ave.volar()
obj_aguila = Aguila()
obj_aguila.volar()
obj_gallina = Gallina()
obj_gallina.volar()

#%% ENCAPSULAMIENTO
# Ocultamiento de datos del estado interno
# para proteger la integridad del objeto

class Cliente:
    def __init__(self):
        self.__codigo = 4321 # Privado
        self._nombre = '' # Protegido
        self.cedula = 0  # Publico
    
    def __cuenta(self):
        print('Cuenta de procesamiento ')
        
    def verCodigo(self):
        return self.__codigo 
    def asignarCodigo(self, c):
        self.__codigo = c
        
persona = Cliente()
# objeto._nombre de la clase__nombre atributo
print(persona._Cliente__codigo)
persona._Cliente__cuenta()

#%% SUPER()
# Super():
    #  Se utiliza para llamar metodos definidos
    # se utiliza en la herencia multiple
    
class Mamifero:
    def __init__(self, nombre):
        print(nombre, 'Es un animal de sangre caliente')
        
class Leon(Mamifero):
    def __init__(self):
        print('El leon es un animal de cuatro patas')
        # super da mas enfasis a la clase 2nd
        super().__init__('Apolo')
        # Mamifero.__init__('Alex') 
        
nuevo_leon = Leon()

#%% PROPIEDADES

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    
    def verNombre(self):
        return self.__nombre
    def verSalario(self):
        return self.__salario
    
    def asignarNombre(self, nombre):
        self.__nombre = nombre
    def asignarSalario(self, salario):
        self.__salario = salario
        
    def delNombre(self):
        del self.__nombre
    def delSalario(self):
        del self.__salario
        
empleado_1 = Empleado('Antonia', 50000000)
print(empleado_1.verNombre(), ',', empleado_1.verSalario())
empleado_1.asignarNombre('Lia')
print(empleado_1.verNombre())

#%%            
# Algun tipo de validacion:
    # propiedades
class Trabajador:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    
    def __getNombre(self):
        return self.__nombre
    def __getSalario(self):
        return self.__salario
    
    def __setNombre(self, nombre):
        self.__nombre = nombre
    def __setSalario(self, salario):
        self.__salario = salario
        
    def __delNombre(self):
        del self.__nombre
    def __delSalario(self):
        del self.__salario
    
     # propiedades dentro de la clase 
    nombre = property(fget = __getNombre, 
                      fset = __setNombre,
                      fdel = __delNombre,
                      doc = 'Soy la propiedad del nombre')    
    salario = property(fget = __getSalario,
                       fset = __setSalario)
    
trabajador_1 = Trabajador('Antonia', 50000000)
trabajador_1.nombre = 'Sara'
print(trabajador_1.nombre, trabajador_1.salario)
help(trabajador_1)


            
        
        
    
        
        

       
       

