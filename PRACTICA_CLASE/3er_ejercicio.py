#%% 3er EJERCICIO DE ABSTRACCION (V1)
# CLINICA VETERINARIA

# PREGUNTAR AL PROFE:
    # Para que salga la fecha me sale lo siguiente
    # no entiendo el porque
    # <bound method Mascota.verFechaIngreso of <__main__.Mascota object at 0x00000219246F1D60>>
    

class Mascota:
    def __init__(self):
        self.__nombre = ''        # str del 1er atributo
        self.__historial = 0  # str del 2nd atributo
        self.__tipo = ''          # str del 3er atributo
        self.__peso = 0           # str del 4to atributo
        self.__fecha_ingreso = '' # str del 5to atributo
        self.__medicamento = ''   # str del 6to atributo
    
    # metodos para la clase mascota
    def verHistorial(self):
        return self.__historial
    
    def verTipo(self):
        return self.__tipo
    
    def verMedicamento(self):
        return self.__medicamento
    
    def verFechaIngreso(self):
        return self.__fecha_ingreso
    
    def verNombre(self):
        return self.__nombre
    
    def verPeso(self):
        return self.__peso
    
    # metodos para la clase mascota
    def asignarPeso(self, p):
        self.__peso = p
        
    def asignarNombre(self, n):
        self.__nombre = n
        
    def asignarFechaIngreso(self, f):
        self.__fecha_ingreso = f
        
    def asignarMedicamento(self, k):
        self.__medicamento = k
        
    def asignarTipo(self, t):
        self.__tipo = t
        
    def asignarHistorial(self, h):
        self.__num_historial = h
        
        
# clase sistema
class Sistema:
    def __init__(self):
        # vammos a tener varias mascotas, se manejaran en listas
        self.__lista_mascotas = []
        self.__numero_mascotas = len(self.__lista_mascotas)
        
        
    def ingresarMascota(self):
        # 1- solicito los datos de la mascota con inputs
        nombre = input('Ingrese el nombre de la mascota: ')
        historial = int(input('Ingrese el numero de la historia clinica: '))
        tipo = input('Ingrese el tipo de mascota, canino o felino: ')
        peso = int(input('Ingrese el peso de la mascota: '))
        fecha_ingreso = input('Ingrese la fecha de ingreso de la mascota: ')
        medicamento = input('Ingrese el medicamento administrado: ')
        
        # 2- creo el objeto mascota y le asigno los datos
        m = Mascota()
        m.asignarNombre(nombre)
        m.asignarHistorial(historial)
        m.asignarTipo(tipo)
        m.asignarPeso(peso)
        m.asignarFechaIngreso(fecha_ingreso)
        m.asignarMedicamento(medicamento)
        
        # 3- guardo la mascota en la lista
        self.__lista_mascotas.append(m)
        # 4- actualizo la cantidad de mascotas en el sistema
        self.__numero_mascotas =  len(self.__lista_mascotas)
        
    def verIngreso(self):
        nom = input('Ingrese el nombre de la mascota: ')
        for masc in self.__lista_mascotas:
            if nom == masc.verHistorial():
                print(masc.verFechaIngreso())
                
    def verNumeroMascotas(self):
        return self.__numero_mascotas
    
    def verMedicamentoAdm(self):
         nom = input('Ingrese el nombre de la mascota: ')
         for pet in self.__lista_mascotas:
             if nom == pet.verNombre():
                 print(pet.verMedicamento())

mi_sistema = Sistema()

while True:
    opcion = input('''
    1. Ingresar Mascota
    2. Fecha de ingreso
    3. Numero de mascotas
    4. Medicamento administrado
    5. salir
    ''')
    
    if opcion == '1':
        mi_sistema.ingresarMascota()
    elif opcion == '2':
        mi_sistema.verIngreso()
    elif opcion == '3':
        print('Ahora hay: ' +  str(mi_sistema.verNumeroMascotas()) + ' mascotas')
    elif opcion == '4':
        mi_sistema.verMedicamentoAdm()
    elif opcion == '5':
        break
    else:
        print('Opcion no valida')


#%% 3er EJERCICIO DE ABSTRACCION (V2)
# CLINICA VETERINARIA:
    # Como hago para eliminar una mascota
    
class Pet:
    def __init__(self):
        # atributos
        self.__nombre = ''
        self.__historial = 0
        self.__tipo = ''
        self.__peso = 0
        self.__fecha_ingreso = ''
        self.__medicamento = ''
        
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
    
    def verMedicamento(self):
        return self.__medicamento
    
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
    
    def asignarMedicamento(self, k):
        self.__medicamento = k
        
class Sistema2:
    def __init__(self):
        self.__listaPet = []
        self.__numeroPet = len(self.__listaPet)
        
    def verMedicAdm(self):
        nom = input('Ingrese el nombre de la mascota: ')
        for mascot in self.__listaPet:
            if nom == mascot.verNombre():
                print(mascot.verMedicamento())
    
    def verNumMascotas(self):
        return len(self.__listaPet)
    
    def verIngreso(self):
        nom = input('Ingrese el nombre de la mascota: ')
        for j in self.__listaPet:
            if nom == j.verNombre():
                print(j.verFechaIngreso())
        
    def verificarPet(self, historial):
        # variable bandera
        encontrado = False
        # se busca paciente por paciente
        for i in self.__listaPet:
            if historial == i.verHistorial():
                encontrado = True
                break
        return encontrado
    
    def ingresarPet(self, pet):
        # verifico primero si existe
        if self.verificarPet(pet.verHistorial()):
            return False
        # si no existe lo agrego y torno true
        self.__listaPet.append(pet)
        return True
        
    def deletePet(self):
        pet = input('Ingrese el nombre de la masccota: ')
        for k in self.__listaPet:
            if pet == k.verHistorial():
                self.__listaPet.remove(pet)
                return True
        return False
                
def main():
    sis = Sistema2()
    while True:
        opcion = input('''
        1. Ingresar Mascota
        2. Ver fecha ingreso
        3. Ver medicamento administrado
        4. Ver numero de mascotas en sistema
        5. Eliminar mascota
        6. Salir
        ''')
        if opcion == '1':
            print('A continuacion se le solicitaran los datos...')
            # 1- Se solicitan los datos
            nombre = input('Ingresar el nombre de la mascota: ')
            historial = int(input('Ingresar el numero del historial: '))
            tipo = input('Ingrese el tipo; C si es canico o F si es felino: ')
            peso = input('Ingrese el peso de la mascota: ')
            fecha_ingreso = input('Ingrese la fecha de ingreso de la mascota: ')
            medicamento = input('Ingrese el medicamento administrado: ')
            # 2- se crea un objeto pet
            p = Pet()
            p.asignarNombre(nombre)
            p.asignarHistorial(historial)
            p.asignarTipo(tipo)
            p.asignarPeso(peso)
            p.asignarFechaIngreso(fecha_ingreso)
            p.asignarMedicamento(medicamento)
            # 3- Se almacena en la lista que esta dentro de la clase sistema
            resultado = sis.ingresarPet(p)

            if resultado == False:
                print('Ya existe una mascota con este historial')
            else:
                print('Paciente ingresado')
                
        elif opcion == '2':
            sis.verIngreso()
        elif opcion == '3':
            sis.verMedicAdm()
        elif opcion == '4':
            print('Ahora hay: ' +  str(sis.verNumMascotas()) + ' mascotas')
        elif opcion == '5':
            sis.deletePet()
        elif opcion == '6':
            break
        else:
            print('Opcion invalida')
            
# aca el python descrube cual es la funcion principal
if __name__ == '__main__':
    main()
    