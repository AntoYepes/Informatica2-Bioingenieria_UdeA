#%% 4TO EJERCICIO DE ABSTRACCION (V1)
# CLINICA VETERINARIA

class Pet:
    def __init__(self):
        # atributos de la clase Pet
        self.__nombre = ''
        self.__historial = 0
        self.__tipo = ''
        self.__peso =  0
        self.__fecha_ingreso = ''
        self.__lista_medicamentos = []

    # metodos de la clase pet
    def verNombre(self):
        return self.__nombre

    def verHistorial(self):
        return self.__historial

    def verTipo(self):
        return self.__tipo

    def verPeso(self):
        return self.__peso

    def verFechaIngreso(self):
        return self.__fecha_ingreso

    def verLista_Medicamentos(self):
        return self.__lista_medicamentos

    # metodos de la clase pet
    def asignarNombre(self, n):
        self.__nombre = n

    def asignarHistorial(self, h):
        self.__historial = h

    def asignarTipo(self, t):
        self.__tipo = t

    def asignarPeso(self, p):
        self.__peso = p

    def asignarFechaIngreso(self, f):
        self.__fecha_ingreso = f

    def asignarLista_Medicamentos(self, k):
        self.__medicamento = k

class Medicamento:
    def __init__(self):
        self.__nombre_medic = ''
        self.__dosis = 0

     # metodos de la clase medicamento
    def verNombreMedicamento(self):
        return self.__nombre_medic

    def verDosis(self):
        return self.__dosis

    # metodos de la clase medicamento
    def asignarNombreMedicamento(self, med):
        self.__nombre_medic = med

    def asignarDosis(self, med):
        self.__dosis = med

class Sistema:
    def __init__(self):
        self.__listPet = []
        self.__numPet = len(self.__listPet)

    def verificarExiste(self, historial):
        for i in self.__listPet:
            if i == historial:
                return True
        return False

    def verNumeroPet(self):
        return len(self.__listPet)

    def ingresarPet(self, pet):
        self.__listPet.append(pet)

    def verFechaIngreso(self, historial):
        for masc in self.__listPet:
            if historial == masc.verHistorial():
                return masc.verFechaIngreso()

    def verMedicamento(self, historial):
        for masc in self.__listPet:
            if historial == masc.verHistorial():
                return masc.verLista_Medicamentos()

    def eliminarMascota(self, historial):
        for masc in self.__listPet:
            if historial == masc.verHistorial():
                self.__listPet.remove(masc)
                return True
        return False

def main():
    servicio_hospitalario = Sistema()
    while True:
        menu = input('''
        Ingrese una opción:\n
        1- Ingrese una mascota:
        2- Ver fecha de ingreso:
        3- Ver numero de mascota en el servicio:
        4- Ver medicamentos que se estan administrando:
        5- Eliminar mascota
        6- Salir\n
        Usted Ingreso la opcion:
        ''')
        # Ingresar una mascota
        if menu == '1':
            if servicio_hospitalario.verNumeroPet() >= 10:
                print('No hay espacio ...ALERT!!!')
                continue
            historia = int(input('Ingrese la historia clinica de la mascota: '))
        historia = int(input('Ingrese la historia clinica de la mascota: '))
        verificacion =  servicio_hospitalario.verHistorial(historia)
        if verificacion == False:

            nombre = input('Ingrese el nombre de la mascota: ')
            tipo = input('Ingrese C para canino o F para fenino: ')
            peso = int(input('Ingrese el peso de la mascota: '))
            fecha =  input('Ingrese la fecha de entrada: ')
            nm = int(input('Ingrese la cantidad de medicamento administrado: '))
            lista_medicamentos = []

            for i in range(0, nm):
                nombre_medic = input('Ingrese el nombre del medicamento: ')
                dosis = int(input('Ingrese la dosis administrada: '))
                med = Medicamento()
                med.asignarDosis(dosis)
                med.asignarNombreMedicamento(nombre_medic)
                lista_medicamentos.append(med)

                mascota = Pet()
                mascota.asignarNombre(nombre)
                mascota.asignarHistorial(historia)
                mascota.asignarPeso(peso)
                mascota.asignarTipo(tipo)
                mascota.asignarFechaIngreso(fecha)
                mascota.asignarLista_Medicamentos(lista_medicamentos)
                servicio_hospitalario.ingresarPet(mascota)
            else:
                print('Ya existe una mascota con el numero de historia clinica ingresado: ')

        elif menu == '2':
            q = int(input('Ingrese la historia clinica de la mascota: '))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print('La fecha de ingreso de la mascota es: ' + fecha)
            else:
                print('La historia clinica ingresada no corresponde con ninguna mascota')

        elif menu == '3':
            numero = servicio_hospitalario.verNumeroPet()
            print('El numero de mascotas en el sistema es: ' + str(numero))

        elif menu == '4':
            q = int(input('Ingrese la historia clinica de la mascota: '))
            medic = servicio_hospitalario.verMedicamento(q)
            if medic != None:
                print('Los medicamentos administrados son: ')
                for m in medic:
                    print(f'\n{m.verNombre()}')
            else:
                print('La historia clinica ingresada no corresponde con ninguna mascota en el sistema')

        elif menu == '5':
            q = int(input('Ingresar la historia clinica de la mascota: '))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q)
            if resultado_operacion == True:
                print('Mascota eliminada con exito')
            else:
                print('No se ha podido eliminar la mascota')

        elif menu == '6':
            break
        else:
            print('Ingreso valor no valido')

if __name__ == '__main__':
    main()


