# PRACTICA QUIZ 1
# Clase Examen Sangre
class ExamenSangre:
    # Constructor
    def __init__(self):
        # Atributos de la clase examen de sangre
        self.__tasaFiltracionGlomerular = 0
        self.__cocienteAlbuminaCreatinina = 0
        self.__creatininaSuero = 0
        self.__nitrogenoUreicoSangre = 0

    # PROPIEDADES
    # Metodos de /GETver para la clase ExamenSangre
    def getTasaFiltracionGlomerular(self):
        return self.__tasaFiltracionGlomerular

    def getCocienteAlbuminaCreatinina(self):
        return self.__cocienteAlbuminaCreatinina

    def getCreatininaSuero(self):
        return self.__creatininaSuero

    def getNitrogenoUreicoSangre(self):
        return self.__nitrogenoUreicoSangre

    # Metodo de set/asignar para la clase Examen de sangre
    def setTasaFiltracionGlomerular(self, tfg):
        self.__tasaFiltracionGlomerular = tfg

    def setCocienteAlbuminaCreatinina(self, cac):
        self.__cocienteAlbuminaCreatinina = cac

    def setCreatininaSuero(self, cs):
        self.__creatininaSuero = cs

    def setNitrogenoUreicoSangre(self, nus):
        self.__nitrogenoUreicoSangre = nus

# Clase Paciente
class Paciente:
    # Constructor
    def __init__(self):
        # Atributos
        self.__nombre = str
        self.__cedula = 0
        self.__edad = 0
        self.__peso = 0
        self.__estatura = 0
        self.__genero = ''
        self.__presionArterial = 0
        self.__examenSangre = {} #None

    # PROPIEDADES
    # Metodos get
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def getEdad(self):
        return self.__edad
    def getPeso(self):
        return self.__peso
    def getEstatura(self):
        return self.__estatura
    def getGenero(self):
        return self.__genero
    def getPresionArterial(self):
        return self.__presionArterial
    def getExamenSangre(self,id_examen):
        return self.__examenSangre[id_examen]

    #Metodos set
    def setNombre(self, n):
        self.__nombre = n
    def setCedula(self, c):
        self.__cedula = c
    def setEdad(self, e):
        self.__edad = e
    def setPeso(self, p):
        self.__peso = p
    def setEstatura(self, es):
        self.__estatura = es
    def setGenero(self, g):
        self.__genero = g
    def setPresionArterial(self, pa):
        self.__presionArterial = pa

    # Metodo ingresar Examen Sangre, Objeto: ExamenSangre
    def ingresarExamenSangre(self, ex):
        self.__examenSangre[1] = ex

# Clase Hospital
class Hospital:
    # Constructor
    def __init__(self):
        # Atributos
        self.__pacientes = {}

    # METODO PARA PACIENTES
    # Metodo verificar existencia paciente
    def verificarExistencia(self, c):
        return c in self.__pacientes

    # Metodo ingresar paciente
    def ingresarPaciente(self, pac):
        self.__pacientes[pac.getCedula()] = pac

    # Metodo eliminar paciente
    def eliminarPaciente(self, c):
        del self.__pacientes[c]

    # Metodo recuperar paciente (ver la info del paciente)
    def recuperarPaciente(self, c):
        return self.__pacientes[c]

# FUNCIONES
def error(h):
    print('\nERROR - Ingresó una opción no válida.\Intente de nuevo por favor.\n')

def check(x):
    while True:
        try:
            value = int(input(x))
            break
        except ValueError:
            print('Ingrese un dato numerico...')
    return value

def main():
    # Creamos el objeto de hospital
    hosp = Hospital()
    # Creamos el menu con while True
    while True:
        menu = check('''
        1. Ingresar Paciente
        2. Clasificar Paciente
        3. Editar Paciente
        4. Mostrar Paciente
        5. Salir
        :''')

        if menu == 1: # Ingresar Paciente
            # 1. Verificamos si la cedula del pac ya existe
            cedula = check('Ingresar la cedula: ')
            if hosp.verificarExistencia(cedula) ==  True:
                print('El paciente con esta cedula ya existe')
            else:
                # 2. Como la cedula no existe, crea el obj paciente
                pac = Paciente()
                # 3 Se asignan los datos a paciente
                pac.setCedula(cedula)
                pac.setNombre(input('Ingrese el nombre: '))
                pac.setEdad(check('Ingrese la edad: '))
                pac.setGenero(input('Ingrese F o M:'))
                pac.setEstatura(input('Ingrese la estatura: '))
                pac.setPeso(input('Ingrese el peso: '))
                pac.setPresionArterial(input('Ingrese la presion arterial: '))

                # 4. Crear objeto exam sangre
                examS = ExamenSangre()
                examS.setCocienteAlbuminaCreatinina(input('Ingresar CAC:'))
                examS.setCreatininaSuero(input('Ingresar CS: '))
                examS.setNitrogenoUreicoSangre(input('Ingresar NUS: '))
                examS.setTasaFiltracionGlomerular(input('Ingresar TFG: '))

                pac.ingresarExamenSangre(examS)
                hosp.ingresarPaciente(pac)

        elif menu == 2: # Clasificacion de paciente
            cedula = check('verificacion cedula: ')
            if hosp.verificarExistencia(cedula) == True:
                pa = hosp.recuperarPaciente(cedula)
                p =  pa.getExamenSangre(1)
                lista = []

                if int(p.getTasaFiltracionGlomerular()) < 120:
                    lista.append(True)

                if int(p.getCocienteAlbuminaCreatinina()) > 30:
                    lista.append(True)

                if int(pa.getPresionArterial()) >= 130:
                    lista.append(True)

                if int(p.getNitrogenoUreicoSangre()) >= 20:
                    lista.append(True)

                if pa.getGenero() == 'M':
                    if float(p.getCreatininaSuero()) > 1.2:
                        lista.append(True)
                else:
                    if float(p.getCreatininaSuero()) > 1.4:
                        lista.append(True)

                if sum(lista) == 5:
                    print('Paciente requiere dialisis')
                else:
                    print('Paciente no requiere dialisis')


        elif menu == 3: # Editar paciente
            cedula = check('Ingrese la cedula: ')
            if hosp.verificarExistencia(cedula) == True:
                # Lo guardo con la variable pa, para asi poderlo editar
                pa = hosp.recuperarPaciente(cedula)
                opcion = check('''
                Ingrese para editar:
                1. Nombre
                2. Edad
                3. Peso
                4. Estatura
                5. Genero
                6. Presion Arterial 
                7. Examen Sangre
                8. Eliminar Paciente
                ''')
                if opcion == 1:
                    pa.setNombre(input('Ingrese el nuevo nombre: '))
                    print('Cambio exitoso')
                elif opcion == 2:
                    pa.setEdad(check('Ingresa la nueva edad: '))
                    print('Cambio exitoso')
                elif opcion == 3:
                    pa.setPeso(input('Ingresa el nuevo peso: '))
                    print('Cambio exitoso')
                elif opcion == 4:
                    pa.setEstatura(input('Ingresa la nueva estatura: '))
                    print('Cambio exitoso')
                elif opcion == 5:
                    pa.setGenero(input('Ingresa F o M: '))
                    print('Cambio exitoso')
                elif opcion == 6:
                    pa.setPresionArterial(input('Ingresa la nueva Presion Arterial: '))
                    print('Cambio exitoso')
                elif opcion == 7:
                    if hosp.verificarExistencia(cedula) == True:
                        # Lo guardo con la variable pa, para asi poderlo editar
                        pa = hosp.recuperarPaciente(cedula)
                        print(pa.getCedula())
                        print(pa.getExamenSangre(1))
                        # Traigo el objeto asociado
                        exSag =  pa.getExamenSangre(1)
                        menu = check('''
                        1. CAC
                        2. CS
                        3. NUS
                        4. TFG
                        :''')

                        if menu == 1:
                            exSag.setCocienteAlbuminaCreatinina(input('Ingresa el nuevo CAC: '))
                            print('Cambio exitoso')
                        elif menu == 2:
                            exSag.setCreatininaSuero(input('Ingresa el nuevo CS: '))
                            print('Cambio exitoso')
                        elif menu == 3:
                            exSag.setNitrogenoUreicoSangre(input('Ingresa el nuevo NUS: '))
                            print('Cambio exitoso')
                        elif menu == 4:
                            exSag.setTasaFiltracionGlomerular(input('Ingresa el nuevo TFG: '))
                            print('Cambio exitoso')

                elif opcion == 8:
                    pa.eliminarPaciente(cedula)

            else:
                print('Paciente no existe')

        elif menu == 4:
            cedula = check('Ingrese la cedula: ')
            if hosp.verificarExistencia(cedula) == True:
                # Lo guardo con la variable pa, para asi poderlo editar
                pa = hosp.recuperarPaciente(cedula)
                print('Cedula: ' + str(pa.getCedula()))
                print('Nombre: ' + str(pa.getNombre()))
                print('Edad: ' + str(pa.getEdad()))
                print('Estatura: ' + str(pa.getEstatura()))
                print('Peso: ' + str(pa.getPeso()))
                print('Genero: ' + str(pa.getGenero()))
                print('Presion Arterial: ' + str(pa.getPresionArterial()))
                if hosp.verificarExistencia(cedula) == True:
                        # Lo guardo con la variable pa, para asi poderlo editar
                        pa = hosp.recuperarPaciente(cedula)
                        # Traigo el objeto asociado
                        exSag =  pa.getExamenSangre(1)
                        print('CAC: ' + str(exSag.getCocienteAlbuminaCreatinina()))
                        print('CS: ' + str(exSag.getCreatininaSuero()))
                        print('NUS: ' + str(exSag.getNitrogenoUreicoSangre()))
                        print('TFG: ' + str(exSag.getTasaFiltracionGlomerular()))

        elif menu == 5: # Salir
            break

        else:
            print('Opcion invalida, vuelve a intentarlo')

if __name__ == '__main__':
    main()












