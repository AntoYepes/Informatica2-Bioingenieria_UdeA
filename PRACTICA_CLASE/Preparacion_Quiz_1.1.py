# EJERCICIO EVALUATIVO (V2)
class Persona:
    # Atributos
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
        self.__genero = ''

    # Propiedades ver y asignar
    # Metodos de ver
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero

    # Metodos de asignar
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarCedula(self, c):
        self.__cedula = c
    def asignarGenero(self, g):
        self.__genero = g

# Se crea la clase paciente
class Paciente(Persona):
    # Se crea el constructor init y atributos
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = '' # atributo

    # Metodos de ver/asignar
    def verServicio(self):
        return self.__servicio
    def asignarServicio(self, s):
        self.__servicio = s

# Se crea la clase Empleado Hospital
class EmpleadoHospital(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__turno = '' # atributo

    # Metodos ver/asignar
    def verTurno(self):
        return self.__turno
    def asignarTurno(self, t):
        self.__turno = t

# Se crea la clase de Enfermera
class Enfermera(EmpleadoHospital):
    def __init__(self):
        EmpleadoHospital.__init__(self)
        self.__rango = ''

    # Metodos ver/asignar: propiedades
    def verRango(self):
        return self.__rango
    def asignarRango(self, r):
        self.__rango = r

# Se crea la clase Medica
class Medico(EmpleadoHospital):
    def __init__(self):
        EmpleadoHospital.__init__(self)
        self.__especialidades = ''

    # Metodos ver/asignar: propiedades
    def verEspecialidades(self):
        return self.__especialidades
    def asignarEspecialidades(self, e):
        self.__especialidades = e

class Sistema:
    # Se crean las respectivas listas
    def __init__(self):
        self.__listaPaciente = []
        self.__listaMedico = []
        self.__listaEnfermera = []

    def verificar(self, cc):
        for i in (self.__listaPaciente + self.__listaEnfermera + self.__listaMedico):
            if cc == i.verCedula():
                return True
        return False

    def ingresar(self, cc, person):
        for i in (self.__listaPaciente + self.__listaEnfermera + self.__listaMedico):
            if cc not in self.__listaPaciente:
                self.__listaPaciente.append(person)
            elif cc not in self.__listaEnfermera:
                self.__listaEnfermera.append(person)
            elif cc not in self.__listaMedico:
                self.__listaMedico.append(person)

    def verDatos(self, cc, p):
        # Verifico primero si existe
        if self.verificar(cc) == False:
            return None
        elif cc == p.verCedula():
            return p

    def verNumPac(self):
        print('En Pacientes hay ' +  str(len(self.__listaPaciente)) + ' pacientes')

    def verNumEnf(self):
        print('En Enfermeros hay ' +  str(len(self.__listaEnfermera)) + ' enfermeros')

    def verNumMed(self):
        print('En Medicos hay ' +  str(len(self.__listaMedico)) + ' medicos')

def asig(cc, p):
    if p == Paciente():
        return p
    elif p == Enfermera():
        return p
    elif p == Medico():
        return p

    p.asignarNombre(input('Ingresar el nombre del paciente: '))
    p.asignarCedula(cc)
    p.asignarGenero(input('Ingresar F. femenino / M. masculino: '))


def ver(cc, p):

    if p == Paciente():
        return p
    elif p == Enfermera():
        return p
    elif p == Medico():
        return p

    # Si encuentro al pasajero, imprimo los datos
    print('Nombre: ', p.verNombre())
    print('Cedula: ', str(p.verCedula()))
    print('Genero: ', p.verGenero())

def main():
    sis = Sistema()
    while True:
        opc = input('''
        1. Ingresar
        2. Ver datos
        3. Ver cantidad
        4. Salir
        :''')
        while True:
                op1 = input('''
                A. Paciente
                B. Enfermera
                C. Medico
                D. Salir
                :''')
                if opc == '1':
                    if op1 == 'A':
                        cc = int(input('Ingrese la cedula: '))
                        p = Paciente()
                        asig(cc, p)
                        p.asignarServicio(input('Ingresar el servicio a solicitar: '))
                        # Se almacena en la lista que esta dentro de la clase sistema

                        resultado = sis.ingresar(cc, p)

                        if resultado == False:
                            print('Ya existe pasajero con esa cedula')
                        else:
                            print('Paciente ingresado con exito')

                    elif op1 == 'B':
                        # Crear objeto y solicitar datos
                        cc = int(input('Ingrese el numero de cedula del enfermer@: '))
                        p = Enfermera()
                        asig(cc, p)
                        p.asignarTurno(input('Ingrese el turno de la enfermer@ : '))
                        p.asignarRango(input('Ingrese el rango de la enferner@ :'))
                        # Se almacena en la lista que esta dentro de la clase sistema
                        resultado = sis.ingresar(cc, p)

                        if resultado == False:
                            print('Ya existe Enfermero con esa cedula')
                        else:
                            print('Enfermera ingresado con exito')

                    elif op1 == 'C':
                        # Crear objeto y solicitar datos
                        cc = int(input('Ingrese el numero de cedula del medico: '))
                        p = Medico()
                        asig(cc, p)
                        p.asignarTurno(input('Ingrese el turno de la medic@ : '))
                        p.asignarEspecialidades(input('Ingrese el rango de la medic@ :'))
                        # Se almacena en la lista que esta dentro de la clase sistema
                        resultado = sis.ingresar(cc, p)

                        if resultado == False:
                            print('Ya existe Medico con esa cedula')
                        else:
                            print('Medico ingresado con exito')

                    elif op1 == 'D':
                        break


                elif opc == '2':
                    if op1 == 'A':
                        # Se solicita la cedula para la busqueda
                        cc = input('Ingrese la cedula a buscar: ')
                        # le pido al sistema que me devuelva en la variable p al pasajero
                        # que tenga la cc en la lista
                        ver(cc, p)
                        sis.verDatos(cc, p)
                        print('Servicio: ', p.verServicio())

                    elif op1 == 'B':
                        # Se solicita la cedula para la busqueda
                        cc = input('Ingrese la cedula a buscar: ')
                        # le pido al sistema que me devuelva en la variable p al pasajero
                        # que tenga la cc en la lista
                        ver(cc, p)
                        sis.verDatos(cc, p)
                        print('Turno: ', p.verTurno())
                        print('Rango: ', p.verRango())

                    elif op1 == 'C':
                        # Se solicita la cedula para la busqueda
                        cc = input('Ingrese la cedula a buscar: ')
                        # le pido al sistema que me devuelva en la variable p al pasajero
                        # que tenga la cc en la lista
                        ver(cc, p)
                        sis.verDatos(cc, p)
                        print('Turno: ', p.verTurno())
                        print('Rango: ', p.verEspecialidades())

                    elif op1 == 'D':
                        break

                elif opc == '3':

                    if op1 == 'A':
                        sis.verNumPac()
                    elif op1 == 'B':
                        sis.verNumEnf()
                    elif op1 == 'C':
                        sis.verNumMed()
                    elif op1 == 'D':
                        break


                break

        if opc == '4':
            break

if __name__ == '__main__':
    main()
