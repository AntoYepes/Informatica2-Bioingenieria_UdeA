# EJERCICIO PRACTICO
class Mascota:
    def __init__(self):
        self.__nombre = ''        # str del 1er atributo
        self.__historial = 0  # str del 2nd atributo
        self.__tipo = ''          # str del 3er atributo
        self.__peso = 0           # str del 4to atributo
        self.__fecha_ingreso = '' # str del 5to atributo
        self.__medicamento = ''   # str del 6to atributo
    
    # metodos para la clase mascota
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
        self.__historial = h
        
        
# clase sistema
class Sistema:
    def __init__(self):
        # vammos a tener varias mascotas, se manejaran en lista
        self.__lista_mascotas = []
        self.__numero_mascotas = len(self.__lista_mascotas)
        
    def verificarExistencia(self, historia):
        for i in self.__lista_mascotas:
            if historia == i.verHistorial():
                return True
        return False
    
        
    def ingresarMascota(self, mascota):
        self.__lista_mascotas.append(mascota)
        
    def verFechaIngreso(self, historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistorial():
                print(m.verFechaIngreso())
                
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas)
    
    def verMedicamento(self, historia):
         for k in self.__lista_mascotas:
             if historia == k.verHistorial():
                 return k.verMedicamento()
                 
def main():
    sistema = Sistema()
    while True:
        opcion = input('''
        1. Ingresar Mascota
        2. Fecha de ingreso
        3. Numero de mascotas
        4. Medicamento administrado
        5. Salir
        :''')
        
        if opcion == '1':
            if sistema.verNumeroMascotas() >= 10:
                print('Es sistema esta lleno')
                continue
            check = sistema.verificarExistencia(input('Ingrese el historial de la mascota: '))
            if check == False:
               # 1- solicito los datos de la mascota con inputs
               # creo el objeto mascota y le asigno los datos
                m = Mascota()
                m.asignarNombre(input('Ingrese el nombre de la mascota: '))
                m.asignarHistorial(int(input('Ingrese el historial de la mascota: ')))
                m.asignarTipo(input('Ingrese el tipo de mascota, canino o felino: '))
                m.asignarPeso(int(input('Ingrese el peso de la mascota: ')))
                m.asignarFechaIngreso(input('Ingrese la fecha de ingreso de la mascota: '))
                m.asignarMedicamento(input('Ingrese el medicamento administrado: '))
                resultado = sistema.ingresarMascota(m)
                
                if resultado == False:
                    print('Ya existe la mascota con esta cedula')
                else:
                    print('Mascota ingresado con exito')
            else:
                print('Ya existe mascota con el numero de historial digitado')
            
        elif opcion == '2':
            hist =int(input('Ingrese le historial de la mascota: '))
            date = sistema.verFechaIngreso(hist)
            if date != None:
                print('La fecha de ingreso es: ', date)     
                
        elif opcion == '3':
            numero = sistema.verNumeroMascotas()
            print('Ahora hay: ' +  str(numero) + ' mascotas')
            
        elif opcion == '4':
            k = int(input('Ingrese el historial de la mascota: '))
            med = sistema.verMedicamento(k)
            if med != None:
                for j in med:
                    print(j)
            else:
                print('El histotial no corresponde a ninguna mascota')
                       
        elif opcion == '5':
            break
        else:
            print('Opcion no valida')
            
# aca el python descrube cual es la funcion principal
if __name__ == '__main__':
    main()
    