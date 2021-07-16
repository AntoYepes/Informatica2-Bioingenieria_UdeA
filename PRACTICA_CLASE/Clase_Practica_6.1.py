#%% PRACTICA EN CLASE No 7
# 4TO EJERCICIO DE ABSTRACCION ( MODIFICANDO EL CODIGO)
# CLINICA VET:
    # 1. No se puede ingresar medicamentos con el mismo nombre
    # 2. Lista de mascotas dadas por un diccionario
    # 3. Fecha que se ingrese dd/mm/aa si no ERROR
    # 4. Eliminar medicamento de una mascota
import datetime

class Medicamento:
    # Se crea el constructor y los atributos
    def __init__(self):
        self.__nombreMedicamento = ''
        self.__dosis = 0

    # Metodos ver/asignar de la clase Medicamento
    def verNombreMedicamento(self):
        return self.__nombreMedicamento
    def verDosis(self):
        return self.__dosis

    def asignarNombreMedicamento(self, nm):
        self.__nombreMedicamento = nm
    def asignarDosis(self, d):
        self.__dosis = d


class Mascota:
    def __init__(self):
        self.__nombre = ''
        self.__numHistorial = 0
        self.__tipo = ''
        self.__peso = 0
        self.__fechaIngreso = ''
        self.__lista_Medicamento = []

    # Metodos ver de la clase Pet
    def verNombre(self):
        return self.__nombre
    def verNumHistorial(self):
        return self.__numHistorial
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFechaIngreso(self):
        return self.__fechaIngreso
    def verlista_Medicamento(self):
        return self.__lista_Medicamento

    # Metodos asignar de la clase Pet
    def asignarNombre(self, n):
        self.__nombre =  n
    def asignarNumHistorial(self, h):
        self.__numHistorial = h
    def asignarTipo(self, t):
        self.__tipo = t
    def asignarPeso(self, p):
        self.__peso = p
    def asignarFechaIngreso(self, f):
        self.__fechaIngreso = f
    def asignarlista_Medicamento(self, m):
        self.__lista_Medicamento = m

class Vet:
    # Se crea el constructor y sus atributos
    def __init__(self):
        self.__listaMascotas = {}

    # Metodo de verificar
    def verificarExistencia(self, historial):
        return historial in self.__listaMascotas

    # Metodo ingresar
    def ingresarMascota(self, historial, obj):
        self.__listaMascotas[historial] = obj

    # Metodo ver Fecha Ingreso
    def verFechaIngreso(self, historial):
        return self.__listaMascotas[historial].verFechaIngreso()

    # Metodo Numero de Canino y Felino
    def verNumMascotas(self):
        return len(self.__listaMascotas)

    # Metodo ver Medicamento
    def verMedicamento(self, historial):
        return self.__listaMascotas[historial].verlista_Medicamento()

    # # Metodo para verificar nombre del medicamento
    # def verificarNomMedicamento(self, name):
    #     return name in self.__listaMascotas[].verNombreMedicamento()

    # Metodo para eliminar
    def eliminarMascota(self, historial):
        self.__listaMascotas.pop(historial)

def main():
    # Creo el objeto usando la clase sistema
    vet = Vet()
    # Creo el while
    while True:
        opc = input('''
        1. Ingresar mascota
        2. Ver Fecha Ingreso
        3. Ver Numero de mascota
        4. Ver Medicamento
        5. Eliminar mascota
        6. Salir
        :''')
        if opc == '1':
            if vet.verNumMascotas() >= 10:
                print('Capacidad maxima, No se aceptan mas mascotas')
                continue
            h = int(input('Ingrese el historial de la mascota: '))
            if vet.verificarExistencia(h) == False:
                # Solicito los datos para crear el objeto medicamento
                nm = int(input('Ingrese la cantidad de medicamento de la mascota: '))
                lista_medic = []

                for i in range(0, nm):
                    # Creo el objeto de medicamento
                    name = input('Ingresar el nombre del medicamento: ')
                    medic = Medicamento()
                    medic.asignarNombreMedicamento(name)
                    medic.asignarDosis(int(input('Ingresar la dosis del medicamento: ')))
                    lista_medic.append(medic)

                    # if vet.verificarNomMedicamento(name, ) == False:
                    #     print('El medicamento se ingreso con exito')
                    # else:
                    #     print('Ya existe medicamento con el mismo nombre')

                # creo el objeto de mascota, solicitando los datos
                pet = Mascota()
                pet.asignarNombre(input('Ingrese el nombre del Pet: '))
                pet.asignarNumHistorial(h)
                pet.asignarTipo(input('Ingrese el tipo del Pet: '))
                pet.asignarPeso(int(input('Ingrese el peso del Pet: ')))
                pet.asignarFechaIngreso(datetime.datetime.now())
                pet.asignarlista_Medicamento(lista_medic)
                # Ingreso el objeto
                resultado = vet.ingresarMascota(h, pet)
                if resultado == True:
                    print('Mascota ingresada con exito')

            else:
                print('La mascota ya esta registrada')

        elif opc == '2':
            h = int(input('Ingrese el historial de la mascota: '))
            if vet.verFechaIngreso(h) != None:
                print('La fecha de ingreso es: ' , vet.verFechaIngreso(h))
            else:
                print('No existe')

        elif opc == '3':
            print('El numero de mascotas es: ', str(vet.verNumMascotas()))

        elif opc == '4':
            h = int(input('Ingrese el historial de la mascota: '))
            if vet.verMedicamento(h) != None:
                print('El medicamento administrado es: ')
                for m in vet.verMedicamento(h):
                    print(f'\n- {m.verNombreMedicamento()}') # NO ME IMPRIME COMO DEBE SI LO PONGO COMO EL PROFE
            else:
                print('No existe')

        elif opc ==  '5':
            h = int(input('Ingrese el historial de la mascota: '))
            if vet.eliminarMascota(h) == True:
                print('Mascota eliminada con exito')


        elif opc == '6':
            print('GRACIAS POR UTILIZAR NUESTROS SERVICIOS')
            break

        else:
            print('Opcion no valida, intentelo de nuevo')

if __name__ == '__main__':
    main()