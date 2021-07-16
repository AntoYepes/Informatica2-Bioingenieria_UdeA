# PRACTICA EN CLASE 6
# SolucionaMOS y corregimos errores de la evaluacion No 1
class Pet:
    def __init__(self):
        self.__nombre = ''
        self.__numHistorial = 0
        self.__tipo = ''
        self.__peso = 0
        self.__fechaIngreso = ''
        self.__medicamento = ''

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
    def verMedicamento(self):
        return self.__medicamento

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
    def asignarMedicamento(self, m):
        self.__medicamento = m

class Sistema:
    # Se crea el constructor y sus atributos
    def __init__(self):
        self.__listaCanino = []
        self.__listaFelino = []

    # Metodo de verificar
    def verificarExistencia(self, historial):
        for i in (self.__listaCanino + self.__listaFelino):
            if historial == i.verNumHistorial():
                return True # Si lo encuentra
        return False

    # Metodo ingresar
    def ingresarMascota(self, masc):
        if masc.verTipo() == 'Canino':
            self.__listaCanino.append(masc)

        elif masc.verTipo() == 'Felino':
            self.__listaFelino.append(masc)

    # Metodo ver Fecha Ingreso
    def verFechaIngreso(self, historial):
        for k in (self.__listaCanino + self.__listaFelino):
            if historial == k.verNumHistorial():
                return k.verFechaIngreso()
        return None

    # Metodo Numero de Canino y Felino
    def verNumCanino(self):
        return len(self.__listaCanino)

    def verNumFelino(self):
        return len(self.__listaFelino)

    # Metodo ver Medicamento
    def verMedicamento(self, historial):
        for j in (self.__listaCanino + self.__listaFelino):
            if historial == j.verNumHistorial():
                return j.verMedicamento()
        return None

# Ciclo o Menu principal
def main():
    # Creo el objeto usando la clase sistema
    vet = Sistema()
    # Creo el while
    while True:
        opc = input('''
        1. Ingresar Pet
        2. Ver Fecha Ingreso
        3. Ver Numero de Pet
        4. Ver Medicamento
        5. Salir
        :''')

        if opc == '1':
            if vet.verNumCanino() >= 5:
                print('La veterinaria esta full')
                continue
            if vet.verNumFelino() >= 5:
                print('La veterinaria esta full')
                continue
            # Se pide los datos del historial
            h = int(input('Ingrese el historial del Pet: '))
            # Vamos a verificar la existencia
            if vet.verificarExistencia(h) == False:
                # Se objeto mascota y se solicitan los datos asignandolos
                pet = Pet()
                pet.asignarNombre(input('Ingrese el nombre del Pet: '))
                pet.asignarNumHistorial(h)
                pet.asignarTipo(input('Ingrese el tipo del Pet: '))
                pet.asignarPeso(int(input('Ingrese el peso del Pet: ')))
                pet.asignarFechaIngreso(input('Ingrese la fecha de ingreso: '))
                pet.asignarMedicamento(input('Ingresar el medicamento adiministrado: '))
                # Ingresar Mascota
                vet.ingresarMascota(pet)

        elif opc == '2':
            # Se solicita el historial
            h = int(input('Ingrese el historial del Pet a buscar: '))
            # Llamo a verFechaIngreso
            if vet.verFechaIngreso(h) != None:
                print('La fecha de ingreso es: ', vet.verFechaIngreso(h))
            else:
                print('No existe Pet con ese historial')

        elif opc == '3':
            print('El numero de caninos es : ', str(vet.verNumCanino()))
            print('El numero de felino es: ', str(vet.verNumFelino()))

        elif opc == '4':
            # Se solicita l historial
            h = int(input('Ingrese el historial del Pet a buscar: '))
            # Se verifica que si tenga un valor para asi imprimirlo
            if vet.verMedicamento(h) != None:
                print('El medicamento administrado es: ', vet.verMedicamento(h))
            else:
                print('No existe Pet con este historial')

        elif opc == '5':
            print('Gracias por su visita')
            break

        else:
            print('Opcion invalida, vuelve a intentarlo')


if __name__ == '__main__':
    main()

#%% TERCER EJERCICIO DE ABSTRACCION (V2)
# EJERCICIO MASCOTA:
    # 1. Ingresar mascota: no repetir No Historial. Max 10 mascotas
    # 2. Ver fecha ingreso
    # 3. ver Num mascotas
    # 4. Ver medicamento
    # 5. Eliminar mascota
    # 6. Salir

class Mascota:
    def __init__(self):
        self.__nombre = ''
        self.__numHistorial = 0
        self.__tipo = ''
        self.__peso = 0
        self.__fechaIngreso = ''
        self.__medicamento = ''

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
    def verMedicamento(self):
        return self.__medicamento

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
    def asignarMedicamento(self, m):
        self.__medicamento = m

class Veterinaria:
    # Se crea el constructor y sus atributos
    def __init__(self):
        self.__listaMascotas = []

    # Metodo de verificar
    def verificarExistencia(self, historial):
        for i in self.__listaMascotas:
            if historial == i.verNumHistorial():
                return True # Si lo encuentra
        return False

    # Metodo ingresar
    def ingresarMascota(self, masc):
        self.__listaMascotas.append(masc)

    # Metodo ver Fecha Ingreso
    def verFechaIngreso(self, historial):
        for k in self.__listaMascotas:
            if historial == k.verNumHistorial():
                return k.verFechaIngreso()
        return None

    # Metodo Numero de Canino y Felino
    def verNumMascotas(self):
        return len(self.__listaMascotas)

    # Metodo ver Medicamento
    def verMedicamento(self, historial):
        for j in self.__listaMascotas:
            if historial == j.verNumHistorial():
                return j.verMedicamento()
        return None
    # Metodo para eliminar
    def eliminarMascota(self, historial):
        for i in self.__listaMascotas:
            if historial == i.verNumHistorial():
                self.__listaMascotas.remove(i)
                return True # eliminado con exito
        return False

# Ciclo o Menu principal
def main():
    # Creo el objeto usando la clase sistema
    vet = Veterinaria()
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
                # Solicito los datos y creo el objeto
                pet = Mascota()
                pet.asignarNombre(input('Ingrese el nombre del Pet: '))
                pet.asignarNumHistorial(h)
                pet.asignarTipo(input('Ingrese el tipo del Pet: '))
                pet.asignarPeso(int(input('Ingrese el peso del Pet: ')))
                pet.asignarFechaIngreso(input('Ingrese la fecha de ingreso: '))
                pet.asignarMedicamento(input('Ingresar el medicamento adiministrado: '))
                # Ingreso el objeto
                resultado = vet.ingresarMascota(pet)

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
                print('El medicamento administrado es: ', vet.verMedicamento(h))
            else:
                print('No existe')

        elif opc ==  '5':
            h = int(input('Ingrese el historial de la mascota: '))
            if vet.eliminarMascota(h) == True:
                print('Mascota eliminada con exito')
            else:
                print('No se ha podido eliminar la mascota')

        elif opc == '6':
            print('GRACIAS POR UTILIZAR NUESTROS SERVICIOS')
            break
        else:
            print('Opcion no valida, intentelo de nuevo')

if __name__ ==  '__main__':
    main()

#%% CUARTO EJERCICIO DE ABSTRACCION (V1)
# VETERINARIA:
    # Clases: Mascota/Medicamento/Sistema
    # Medicamento : nombre y dosis
    # 1. Ingresar mascota: max 10. No se repite historial
    # 2. Ver fecha ingreso
    # 3. ver Num mascotas
    # 4. ver medicamentos
    # 5. Eliminar mascota
    # 6. salir

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

class Mascot:
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
        self.__listaMascotas = []

    # Metodo de verificar
    def verificarExistencia(self, historial):
        for i in self.__listaMascotas:
            if historial == i.verNumHistorial():
                return True # Si lo encuentra
        return False

    # Metodo ingresar
    def ingresarMascota(self, masc):
        self.__listaMascotas.append(masc)

    # Metodo ver Fecha Ingreso
    def verFechaIngreso(self, historial):
        for k in self.__listaMascotas:
            if historial == k.verNumHistorial():
                return k.verFechaIngreso()
        return None

    # Metodo Numero de Canino y Felino
    def verNumMascotas(self):
        return len(self.__listaMascotas)

    # Metodo ver Medicamento
    def verMedicamento(self, historial):
        for j in self.__listaMascotas:
            if historial == j.verNumHistorial():
                return j.verlista_Medicamento()
        return None
    # Metodo para eliminar
    def eliminarMascota(self, historial):
        for i in self.__listaMascotas:
            if historial == i.verNumHistorial():
                self.__listaMascotas.remove(i)
                return True # eliminado con exito
        return False

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
                    medic = Medicamento()
                    medic.asignarNombreMedicamento(input('Ingresar el nombre del medicamento: '))
                    medic.asignarDosis(int(input('Ingresar la dosis del medicamento: ')))
                    lista_medic.append(medic)

                # creo el objeto de mascota, solicitando los datos
                pet = Mascot()
                pet.asignarNombre(input('Ingrese el nombre del Pet: '))
                pet.asignarNumHistorial(h)
                pet.asignarTipo(input('Ingrese el tipo del Pet: '))
                pet.asignarPeso(int(input('Ingrese el peso del Pet: ')))
                pet.asignarFechaIngreso(input('Ingrese la fecha de ingreso: '))
                pet.asignarlista_Medicamento(lista_medic)
                # Ingreso el objeto
                resultado = vet.ingresarMascota(pet)

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
                    print(m) # NO ME IMPRIME COMO DEBE SI LO PONGO COMO EL PROFE
            else:
                print('No existe')

        elif opc ==  '5':
            h = int(input('Ingrese el historial de la mascota: '))
            if vet.eliminarMascota(h) == True:
                print('Mascota eliminada con exito')
            else:
                print('No se ha podido eliminar la mascota')

        elif opc == '6':
            print('GRACIAS POR UTILIZAR NUESTROS SERVICIOS')
            break

        else:
            print('Opcion no valida, intentelo de nuevo')

if __name__ == '__main__':
    main()
