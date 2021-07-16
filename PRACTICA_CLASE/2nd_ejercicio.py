# OOP- OBJECTS 
# Introduction
class Dog:
    # one method
    def meow(self):
        return 'meow'
    #second method
    def add_one(self, x):
        return x + 1
    #third method
    def bark(self):
        print('bark')

d = Dog()
d.bark()
d.add_one(5)
print(d.add_one(5))
print(type(d))

#%% __init__ method
class Dog:
    def __init__(self, name, age):
        self.name = name #save the name, we create an atribute of the class dog wich is name
        print(name)
        self.age = age # We create a second atribute
        print(age)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
d = Dog('Apolo', 10)
d.set_age(23)
print(d.name)
print(d.get_name())
d2 = Dog('Roco', 14)
print(d2.name)
print(d2.get_name())

#%% INHERIT
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')
        
class Cat(Pet):
    def speak(self):
        print('Meow')
        
# upper level parent class       
class Caat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
        
class Dog(Pet):
    def speak(self):
        print('Bark')
        
p = Pet('Tim', 19)
p.show()
c = Cat('Bill', 34)
c.speak()
d = Dog('Jill', 25)
d.speak()

#%% ADVANTAGE EXAMPLE

class Student: 
    def __init__(self, name, age, grade):
        self.name = name #First atribute
        self.age = age # Second atribute
        self.grade = grade # 0-100 Third atribute
    
    def get_grade(self): # method
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = [] # Thi is one atribute but it's not assigned to (name, max_students)
        self.is_active  = False
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)
            
    
s1 = Student('Lia', 15, 95)
s2 = Student('Santi', 22, 85)
s3 = Student('Alejo', 18, 65)

course = Course('science', 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())
        
#%% 2nd EJERCICIO DE ABSTRACCION V1

class Paciente:
    def __init__(self):
        self.__nombre = ''   # str 1ra atributo
        self.__cedula = 0    # int 2nd atributo
        self.__genero = ''   # str 3er atributo
        self.__servicio = '' # str 4to atributo
    
    # metodos para la clase paciente    
    def verNombre(self):
        return self.__nombre
    
    def verCedula(self):
        return self.__cedula
    
    def verGenero(self):
        return self.__genero
    
    def verServicio(self):
        return self.__servicio
    
    #metodos para la clase paciente
    def asignarNombre(self, n):
        self.__nombre = n
        
    def asignarCedula(self, c):
        self.__cedula = c
        
    def asignarGenero(self, g):
        self.__genero = g
        
    def asignarServicio(self, s):
        self.__servicio = s
        
class Sistema:
    def __init__(self):
        # vamos a tener varios pacientes, seran manejados en una lista
        self.__lista_pacientes = []
        # esta variable siempre dependera del tamaño de la lista por lo
        # que no se podra modficar
        # con un metodo asignar
        self.__numero_pacientes = len(self.__lista_pacientes)
        
    def ingresarPaciente(self):
        # 1- solicito los datos por teclado
        nombre = input('Ingrese el nombre del paciente: ')
        cedula = int(input('Ingrese el numero de cedula: '))
        genero = input('Ingrese el genero: ')
        servicio = input('Ingrese el servicio: ')
        # 2- creo el objeto paciente y le asigno los datos
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        # 3- guardo el paciente en la lista
        self.__lista_pacientes.append(p)
        # 4- actualizo la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)
        
    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self):
        cedula = int(input('Ingrese el numero de cedula a buscar: '))
        # cedula en self.__lista_pacientes no sirve porque en la lista
        # hay pacientes NO numeros
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                # si coincide la cedula del paciente con la busqueda
                # muestro los datos
                print('Nombre: '+ paciente.verNombre())
                print('Cedula: ' + str(paciente.verCedula()))
                print('Genero: ' + paciente.verGenero())
                print('Servicio: ' + paciente.verServicio())
                
# cuando creamos las clases podemos generar objetos de esas clases y con esos objetos
# acceder a las funcionalidades y metodos
mi_sistema = Sistema() # Se crea una instancia de la clase sistema

# ciclo infinito
while True:
    opcion = int(input('''
    1. Nuevo paciente
    2. Numero de pacientes
    3. Datos de paciente
    4. Salir
    '''))
    if opcion == 1:
        mi_sistema.ingresarPaciente()
    elif opcion == 2:
        print('Ahora hay: ' +  str(mi_sistema.verNumeroPacientes()))
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print('Opcion invalida')
        
        
#%% 2ND EJERCICIO DE ABSTRACCION V2
class PacienteV2:
    def __init__(self):
        self.__nombre = ''
        self.__cedula = int
        self.__genero = ''
        self.__servicio = ''
        
    def asignarNombre(self, n):
        self.__nombre = n
        
    def asignarCedula(self, c):
        self.__cedula = c
        
    def asignarGenero(self, g):
        self.__genero = g
        
    def asignarServicio(self, s):
        self.__servicio = s
        
    def verCedula(self):
        return self.__cedula
    
    def verNombre(self):
        return self.__nombre
    
    def verGenero(self):
        return self.__genero
    
    def verServicio(self):
        return self.__servicio
    
class SistemaV2:
    def __init__(self):
        self.lista_pacientes = []
    
    def ingresarPaciente(self, pac):
        self.lista_pacientes.append(pac)
    
    def verDatosPaciente(self, c):
        # voy a buscar paciente por paciente
        for p in self.lista_pacientes:
            # por cada paciente de la lista, le digo al paciente que
            # me retorne la cedula y la comparo con la ingresada por el teclado
            if c == p.verCedula():
                return p # si encuentro el paciente lo retorno
    
    def verNumeroPacientes(self):
        print('En el sistema hay: ' + str(len(self.lista_pacientes)) + 'pacientes')
        
# la funcion main veremos como varia la solicitud y tratamiento de los pacientes 

def main():
    sis = SistemaV2()
    # probemos lo que llevamos programado
    while True:
        # Hacer el menu
        opcion = int(input('''
        0. Salir
        1. Ingresar nuevo paciente
        2. Ver paciente
        '''))
        if opcion == 1:
            # Ingreso pacientes
            print('A continuacion se solicitan los datos: ')
            # 1- se solicitan los datos
            nombre = input('Ingrese el nombre: ')
            cedula = int(input('Ingrese la cedula: '))
            genero = input('Ingrese el genero: ')
            servicio = input('Ingrese el servicio: ')
            # 2- se crea un objeto paciente
            pac = PacienteV2()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            # 3- se almacena en la lista que esta dentro de la clase sistema
            sis.ingresarPaciente(pac)
            
        elif opcion == 2:
            # 1- solicito la cedula que quiero buscar
            c = int(input('Ingrese la cedula a buscar: '))
            # le pido al sistema que me devuelva en la variable p al paciente 
            # que tenga la cc en la lista
            p = sis.verDatosPaciente(c)
            # Si encuentro el paciente imprimo los datos
            print('Nombre: ' + p.verNombre())
            print('Cedula: ' + str(p.verCedula()))
            print('Genero: ' + p.verGenero())
            print('Servicio: ' + p.verServicio())
        
        elif opcion != 0:
            continue
        
        else:
            break
            
# aca el python descrube cual es la funcion principal
if __name__ == '__main__':
    main()
    
    
#%% 2ND EJERCICIO DE ABSTRACCION V3
class sistema(object):
    def __init__(self):
        self.lista_pacientes = []
    
    def verificarPaciente(self, cedula):
        # variable bandera
        encontrado = False
        # voy a buscar paciente por paciente
        for i in self.lista_pacientes:
            # por cada paciente de la lista, le digo al paciente que me
            # retorne la cedula y la comparo con la ingresada por el teclado
            if cedula == i.verCedula():
                encontrado = True # Si encuentro la cedula actualizo la bandera
                break # salgo del for
        return encontrado
# De este modo es posible verificar si el paciente existe en BD antes de ser ingresado
    def ingresarPaciente(self, pac):
        #  verifico primero si existe
        if self.verificarPaciente(pac.verCedula()):
            return False
        #si no existe lo agrego y retorno verdadero
        self.__lista_pacientes.append(pac);
        return True
def main():
    sis = SistemaV2()
    # probemos lo que llevamos programado
    # verificacio del paciente
    # ciclo infinito
    while True:
        opcion = int(input('''
        1. Nuevo paciente
        2. Numero de pacientes
        3. Datos de paciente
        4. Salir
        '''))
        if opcion == 1:
            print('A continuacion se solicitan los datos...')
            # 1- se solicitan los datos
            nombre = input('Ingrese el nombre: ')
            cedula = int(input('Ingrese la cedula: '))
            genero = input('Ingrese el genero: ')
            servicio = input('Ingrese el servicio: ')
            # 2- se crea un objeto paciente
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            # 3- se almacena en la lista que esta dentro de la clase sistema
            resultado = sis.ingresarPaciente(pac);
            
            if resultado == False:
                print('Ya existe un paciente con esa cedula');
                
            else:
                print('Paciente ingresado');
    
    # si existe antes de mostrar sus datos
    def verDatosPaciente(self, c):
        # verifico primero si existe, si no existe devuelvo None
        if self.verificarPaciente(c) == False:
            return None
        # Voy a buscar paciente por paciente
        for i in self.__lista_pacientes:
            # por cada paciente de la lisa, le digo al paciente que me
            # retorne la cc y la comparo con la ingresada
            if c == i.verCedula():
                return i
            
        
    
        
    
    
