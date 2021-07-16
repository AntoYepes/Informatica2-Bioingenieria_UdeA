# PRACTICA EN CLASE No-8 :
    # 5to EJERC DE ABSTRACCION
# Importamos
import os
import datetime

# Creamos la clase Indices
class Indices:
    # Costructor
    def __init__(self):
        # Atributos
        self.__pot_d = 0
        self.__pot_t = 0
        self.__pot_a1 = 0
        self.__pot_a2 = 0
        self.__pot_b = 0
        self.__pot_g = 0

    # Propiedades
    # Metodos get/ver de la clase Indices
    def getPot_d(self):
        return self.__pot_d
    def getPot_t(self):
        return self.__pot_t
    def getPot_a1(self):
        return self.__pot_a1
    def getPot_a2(self):
        return self.__pot_a2
    def getPot_b(self):
        return self.__pot_b
    def getPot_g(self):
        return self.__pot_g

    # Metodos de set / asignar
    def setPot_d(self, w):
        self.__pot_d = w
    def setPot_t(self, w):
        self.__pot_t = w
    def setPot_a1(self, w):
        self.__pot_a1 = w
    def setPot_a2(self, w):
        self.__pot_a2 = w
    def setPot_b(self, w):
        self.__pot_b = w
    def setPot_g(self, w):
        self.__pot_g = w

# Creamos la clase Visitas
class Visitas:
    # Constructor
    def __init__(self):
        # Atributos
        self.__fecha = ''
        self.__registro = ''
        self.__notas = ''
        # La visita tiene una clase indice que se inicializa vacia
        self.__indice = None # Solo se guarda un objeto tipo indices

    # Propiedades
    # Metodos get/ver para la clase visitas
    def getFecha(self):
        return self.__fecha
    def getRegistro(self):
        return self.__registro
    def getNotas(self):
        return self.__notas
    def getIndices(self):
        return self.__indice

    # Metodos set/asignar para la clase visitas
    def setFecha(self, f):
        self.__fecha = f
    def setRegistro(self, r):
        self.__registro = r
    def setNotas(self, no):
        self.__notas = no
    def setIndices(self, i):
        self.__indice = i

# Creamos la clase Paciente
class Paciente:
    # Constructor
    def __init__(self):
        # Atributos
        self.__nombre = ''
        self.__cedula = 0
        self.__genero = ''
        # Un paciente tiene muchas visitasm en este ejemplo trabajaremos con dict
        self.__visitas = {} # key-value

    # Propiedades
    # Metodos
    def getNombre(self):
        return self.__nombre

    def setNombre(self, n):
        self.__nombre = n

    def getCedula(self):
        return self.__cedula
    def setCedula(self, c):
        self.__cedula = c

    def getGenero(self):
        return self.__genero
    def setGenero(self, g):
        self.__genero = g

    # Metodo para ver visita, se utiliza la fecha como key
    def verVisita(self, f):
        return self.__visitas[f]

    # Metodo para verificar existencia con la fecha
    def verificarExistencia(self, f):
        return f in self.__visitas

    # Metodo ingresar visita, se utiliza el objeto visitas
    def ingresarVisita(self, v):
        self.__visitas[v.getFecha()] = v

    # Metodo para eliminar visita, se utiliza
    def eliminarVisita(self, f):
        del self.__visitas[f]

# Creamos la clase sistema
class Sistema:
    # Constructor
    def __init__(self):
        # Atributos
        self.__pacientes = {}

    # Metodo verificar existencia, se utiliza la cedula
    def verificarExistencia(self, c):
        return c in self.__pacientes

    # Metodo ingresar Paciente, usamos el objeto paciente
    def ingresarPaciente(self, p):
        self.__pacientes[p.getCedula()] = p

    # Metodo eliminar paciente, usamos la cedula
    def eliminarPaciente(self, c):
        del self.__pacientes[c]

    # Metodo recuperar paciente, mostrar info(es como ver paciente), se utiliza la cedula
    def recuperarPaciente(self, c):
        return self.__pacientes[c]

# # Funcion de validacion
# def ingresoNumero(mensaje):
#     valido = False
#     while valido == False:
#         try:
#             valor = int(input(mensaje))
#             valido = True
#         except ValueError:
#             print('Ingrese un dato numerico...')
#     return valor

# # Funcion que valida si el valor ingresado es un float
# def validarf(valor): # Argumento valor necesario para el calculo
#     try: # Se verificara al mismo tiempo que los valores ingresados esten correctos
#         valor_entero = float(valor) # Se solicita el valor con input y verificando que sea un float
#         return {'ok': True, 'numero': valor_entero} # Si el value de 'ok' es True este valor se guardara
#     except ValueError:
#         return {'ok': False} # Si el value de 'ok' es False no se guardara el valor


# def validar(x):
#         try:
#             return float(x)
#         except:
#             return None
#     return None
# while True:
#           x=validar(input("ingresé x"))
#            If x != None
#                  Break

# 2nd Opcion Funcion de validacion
def validar(msm):
    while True:
        try:
            valor = int(input(msm))
            break
        except ValueError:
            print('Ingrese un dato numerico...')
    return valor


def main():
    # Se crea objeto sistema
    sis = Sistema()
    # Se crea el menu con while
    while True:
        print('''
        1. Nuevo Paciente
        2. Editar Paciente
        3. Eliminar un Paciente
        4. Cargar y guardar paciente
        5. Salir
        ''')
        valor = validar('Valor: ')

        if valor == 1:
            # Verificamos de primero
            cedula = validar(input('Ingrese la cedula: '))
            if sis.verificarExistencia(cedula) == True:
                print('El paciente ya esta en el sistema')
                continue
            else:
                # Se crea el objeto paciente
                pac = Paciente()
                pac.setNombre(input('Ingresar el nombre: '))
                pac.setCedula(cedula)
                pac.setGenero(input('Ingresar F femenino o M masculino: '))

                # Verificar visitas
                numVisitas = validar('Ingrese el numero de visitas: ')
                for i in range(0, numVisitas):
                    # Creo el objeto visitas
                    vis = Visitas()
                    # Asigno visitas
                    vis.setFecha(input('Ingrese la fecha: '))
                    # Adentro se ve la fecha por eso usamos get
                    if pac.verificarExistencia(vis.getFecha()) == True:
                        print('La visita ya existe')
                        # se sale del ciclo for usando continue
                        continue
                    # A la visita le asigno el registro. Metodo que nos trae la direccion actual, de la carpeta
                    vis.setRegistro(os.getcwd() + f'/Pacientes_{pac.getCedula()}')
                    vis.setNotas(input('Ingese observaciones: '))

                    # Se crea el objeto indice y se asigna lo respectivo
                    ind = Indices()
                    ind.setPot_a1(float(input('Ingrese a1: ')))
                    ind.setPot_a2(float(input('Ingrese a2: ')))
                    ind.setPot_b(float(input('Ingrese b: ')))
                    ind.setPot_d(float(input('Ingrese d: ')))
                    ind.setPot_g(float(input('Ingrese g: ')))
                    ind.setPot_t(float(input('Ingrese  t: ')))

                    # Ingresar los indices a las respectivas listas, los indices no se ha asignado al atributo indice de la visita, y la visita tampoco la hemos ingresado dentro de la lista de pacientes

                    # visita le ingresaremos el indice/ paciente le ingresamos la visita
                    vis.setIndices(ind)
                    pac.ingresarVisita(vis)

                # Se ingresa Paciente fuera del for
                sis.ingresarPaciente(pac)

        elif valor == 2: # Editar paciente
            cedula = validar('Ingrese la cedula: ')
            if sis.verificarExistencia(cedula) == True:
                # Lo guardo con la variable pa, para asi poderlo editar
                pa = sis.recuperarPaciente(cedula)
                opcion = validar('''
                Ingresar para editar:
                1. Nombre
                2. Cedula
                3. Genero
                4. Visita
                ''')
                if opcion == 1:
                    pa.setNombre(input('Ingrese el nuevo nombre: '))
                elif opcion == 2:
                    pa.setCedula(input('Ingrese la cedula nueva: '))
                elif opcion == 3:
                    pa.setGenero(input('Ingrese el genero: '))
                elif opcion == 4.:
                    # Como tengo que editar la visita, debo traer la visita
                    f = input('Ingrese fecha de la visita que desea modificar: ')
                    if pa.verificarExistencia(f) == True:
                        # Traigo el objeto asociado
                        visit = pa.verVisita(f)
                        menu = validar('''
                        Ingrese para editar:
                        1. Fecha
                        2. Registro
                        3. Nota
                        4. Indice
                        5. Eliminar visita
                        ''')

                        if menu == 1:
                            visit.setFecha(input('Ingrese la nueva fecha: '))
                        elif menu == 2:
                            visit.setRegistro(input('Ingrese el nuevo registro: '))
                        elif menu == 3:
                            visit.setNotas(input('Ingrese la nueva Nota: '))
                        elif menu == 4:
                            i = visit.getIndices()
                            i.setPot_a1(float(input('a1: ')))
                            i.setPot_a2(float(input('a2:')))
                            i.setPot_b(float(input('b: ')))
                            i.setPot_d(float(input('d: ')))
                            i.setPot_g(float(input('g: ')))
                            i.setPot_t(float(input('t: ')))

                        elif menu == 5: # Eliminar visita, esta esta dentr del paciente
                            pa.eliminarVisita(visit)

        elif valor == 3: # Eliminar un paciente

            cedula = validar('Ingrese la cedula: ')
            if sis.verificarExistencia(cedula) == False:
                print('Paciente no existe')
            else:
                sis.eliminarPaciente(cedula)

        elif valor == 4: # CARGAR Y GUARDAR PACIENTE traer el objeto paciente y traer el objeto visita e indice. archivo nuevo write en ese archivo. copie todo en ese archivo.
        # Iniciemos verificando si existe el paciente
            cedula = validar('Ingrese la cedula: ')
            if sis.verificarExistencia(cedula) == True:
                p = sis.recuperarPaciente(cedula)
                opc = validar('''
                Seleccione que desea guardar:
                1. Paciente
                2. Visita
                3. Indice
                :''')
                if opc == 1:
                    with open('D:/UDEA/SEMESTRE III/Informatica II/Archivo_Pract_8.txt', 'a') as archivo:
                        archivo.write('Nombre: ' + str(p.getNombre() + '\n'))
                        archivo.write('Cedula: ' + str(p.getCedula()) + '\n')
                        archivo.write('Genero: ' + str(p.getGenero() + '\n'))

                elif opc == 2:
                    fe = input('Ingrese fecha de la visita: ')
                    if p.verificarExistencia(fe) == True:
                        v = p.verVisita(fe)
                        with open('D:/UDEA/SEMESTRE III/Informatica II/Archivo_Pract_8.txt', 'a') as archivo:
                            archivo.write('Fecha: ' + str(v.getFecha() + '\n'))
                            archivo.write('Registro: ' + str(v.getRegistro() + '\n'))
                            archivo.write('Notas: ' + str(v.getNotas() + '\n'))

                elif opc == 3:
                    fe = input('Ingrese fecha de la visita: ')
                    if p.verificarExistencia(fe) == True:
                        v = p.verVisita(fe)
                        indc = v.getIndices()
                        with open('D:/UDEA/SEMESTRE III/Informatica II/Archivo_Pract_8.txt', 'a') as archivo:
                            archivo.write('a1: ' + str(indc.getPot_a1()) + '\n')
                            archivo.write('a2: ' + str(indc.getPot_a2()) + '\n')
                            archivo.write('b: ' + str(indc.getPot_b()) + '\n')
                            archivo.write('d: ' + str(indc.getPot_d()) + '\n')
                            archivo.write('g: ' + str(indc.getPot_g()) + '\n')
                            archivo.write('t: ' + str(indc.getPot_t()) + '\n')

            else:
                print('Paciente no existe')


        elif valor == 5: # Salir

            break

        else:
            print('Opcion invalida, vuelve a intentarlo')

if __name__ == '__main__':
    main()