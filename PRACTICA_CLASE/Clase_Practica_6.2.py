import datetime

class Medicamento:
    def __init__(self):
        self.__nombre = ""
        self.__dosis = 0

    def verNombre(self):
        return self.__nombre
    def verDosis(self):
        return self.__dosis

    def asignarNombre(self,temp):
        self.__nombre = temp
    def asignarDosis(self,temp):
        self.__dosis = temp

class Mascota:
    def __init__(self):
        self.__nombre = ""
        self.__tipo = ""
        self.__num_historia = 0
        self.__peso = 0
        self.__fecha_ingreso = ""
        self.__lista_medicamentos = []

    def verNombre(self):
        return self.__nombre
    def asignarNombre(self,temp):
        self.__nombre = temp
    def verTipo(self):
        return self.__tipo
    def asignarTipo(self,temp):
        self.__tipo = temp
    def verHistoria(self):
        return self.__num_historia

    def asignarHistoria(self,temp):
        self.__num_historia = temp
    def verPeso(self,temp):
        return self.__peso
    def asignarPeso(self,temp):
        self.__peso = temp
    def verFechaIngreso(self):
        return self.__fecha_ingreso
    def asignarFechaIngreso(self,temp):
        self.__fecha_ingreso = temp
    def verMedicamentos(self):
        return self.__lista_medicamentos
    def asignarMedicamentos(self,temp):
        self.__lista_medicamentos = temp

class Sistema:
    def __init__(self):
        self.__lista_mascotas = {}

    def verificarMascota(self,nhc):
        return nhc in self.__lista_mascotas

    def ingresarMascota(self,m):
        self.__lista_mascotas[m.verHistoria()] = m

    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)

    def eliminarMascota(self,nhc):
        if self.verificarMascota(nhc) == True:
            del self.__lista_mascotas[nhc]
            return "La mascota fue eliminada del sistema con exito"
        else:
            return "La mascota no se encuentra en el sistema, ingrese otra numero de historia clinica"

    def recuperarMascota(self,nhc):
        if self.verificarMascota(nhc) == False:
            #no existe la mascota
            return None
        return self.__lista_mascotas[nhc]

    def verFechaIngresoMascota(self,nhc):
        m = self.recuperarMascota(nhc)
        if m == None:
            return "La mascota no está en el sistema"
        return m.verFechaIngreso()

#funciones
def ingresoNumerico(mensaje):
    valido = False
    while valido == False:
        try:
            valor = int(input(mensaje))
            valido = True
        except ValueError:
            print("ingrese un dato numerico ...")
            return valor


def main():
    #Se crea la instancia del sistema
    sistema = Sistema()
    while True:
        opcion = ingresoNumerico('''
        0. para salir
        1. para ingresar mascota
        2. para eliminar
        3. ver Fecha Ingreso
        4. ver lista medicamentos
        5. ver numero de mascotas
        :''')
        if opcion == 0:
            print("Fin del programa ...")
            break
        elif opcion == 5:
            print("El sistema tiene " + str(sistema.verNumeroMascotas()) + " mascotas")

        elif opcion == 4:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = ingresoNumerico("Ingrese Numero de Historia Clinica:")
            if sistema.verificarMascota(nhc) == False:
                print("La mascota no esta en el sistema ...")
                continue
            #recupero la mascota de la base de datos
            m = sistema.recuperarMascota(nhc)
            lista_medicamentos = m.verMedicamentos()
            print("La mascota: " + m.verNombre() + " tiene los sgtes medicamentos:")

            for medicamento in lista_medicamentos:
                print("Medicamento con nombre: " + medicamento.verNombre() + " dosis " + str(medicamento.verDosis()))

        elif opcion == 3:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = ingresoNumerico("Ingrese Numero de Historia Clinica:")
            if sistema.verificarMascota(nhc) == False:
                print("La mascota no esta en el sistema ...")
                continue
            print(sistema.verFechaIngresoMascota(nhc))

        elif opcion == 2:
            #1. solicitar numero de historia clinica y ver que no este
            nhc = ingresoNumerico("Ingrese Numero de Historia Clinica:")
            resultado = sistema.eliminarMascota(nhc)
            print(resultado)

        elif opcion == 1:
            #1. debo verificar que haya espacio en el servicio
            if sistema.verNumeroMascotas() >= 10:
                print("No hay espacio ...")
                continue
            #2. solicitar numero de historia clinica y ver que no este
            nhc = ingresoNumerico("Ingrese Numero de Historia Clinica:")
            if sistema.verificarMascota(nhc) == True:
                print("La mascota ya esta en el sistema ...")
                continue
            #3. Si la historia no esta pido los datos restantes
            n = input("Ingrese el nombre de la mascota: ")
            t = input("Ingrese CANINO o FELINO: ")
            p = int(input("Ingrese el peso: "))
            dia = ingresoNumerico("Ingrese dia:")
            mes = ingresoNumerico("Ingrese mes:")
            año = ingresoNumerico("Ingrese año:")
            f = datetime.datetime(año, mes, dia)
            nm = int(input("Ingrese el numero de medicamentos: "))
            lista_medicamentos = []
            #4. por cada medicamento solicito los datos
            for i in range(0,nm):
                nombre_medicamentos = input("Ingrese el nombre: ")
                dosis = ingresoNumerico("Ingrese la dosis: ")
                medicamento = Medicamento()
                medicamento.asignarDosis(dosis)
                medicamento.asignarNombre(nombre_medicamentos)
                lista_medicamentos.append(medicamento)
            #5. crear la mascota y asignarle la informacion
            mascota = Mascota()
            mascota.asignarHistoria(nhc)
            mascota.asignarNombre(n)
            mascota.asignarTipo(t)
            mascota.asignarPeso(p)
            mascota.asignarFechaIngreso(f.strftime("%x"))
            mascota.asignarMedicamentos(lista_medicamentos)
            #6. Ingresar la mascota al sistema
            sistema.ingresarMascota(mascota)
            print("Mascota " + n + " ingresada ...")

        else:
            print("Opcion no valida: ")

if __name__ == '__main__':
    main()