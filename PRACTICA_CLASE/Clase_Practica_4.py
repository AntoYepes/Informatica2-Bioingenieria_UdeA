#%% PRACTICA EN CLASE No 4
class Pasajero:
    def __init__(self):
        # Atributos de pasajero
        self.__nombre = ''
        self.__cedula = 0
        self.__destino = ''
        self.__vuelo = ''
              
    # Metodos ver clase paciente
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verDestino(self):
        return self.__destino
    def verVuelo(self):
        return self.__vuelo
    
    # Metodos asignar clase paciente
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarCedula(self, c):
        self.__cedula = c
    def asignarDestino(self, d):
        self.__destino = d
    def asignarVuelo(self, v):
        self.__vuelo = v
        
class CopaAirlines:
    def __init__(self):
        self.__listaPasajeros =[]
        self.__numeroPasajeros = len(self.__listaPasajeros)
    # Metodos de clase sistema
    def ingresarPasajero(self):
        # 1- Creo el objeto
        pax = Pasajero()
        # 2- Pido los datos y los asigno
        pax.asignarNombre(input('Ingresar el nombre del pasajero: '))
        pax.asignarCedula(int(input('Ingresar el numero de cedula del pasajero: ')))
        pax.asignarDestino(input('Ingresar el destino del viaje: '))
        pax.asignarVuelo(input('Ingrese el numero de vuelo mas el codigo de la aerolinia: '))
        
        # 3- Agrego los datos a la ista 
        self.__listaPasajeros.append(pax)
        
        # 4- Actualizo la cantidad de pacientes
        self.__numeroPasajeros = len(self.__listaPasajeros)
        
    def verNumPasajeros(self):
        return self.__numeroPasajeros
    
    def verDatos(self):
        cedula = int(input('Ingrese el numero de la cedula para ver los datos correspondientes: '))
        for i in self.__listaPasajeros:
            if cedula == i.verCedula():
                print('Nombre:', i.verNombre())
                print('Cedula: ',i.verCedula())
                print('Destino: ', i.verDestino())
                print('Vuelo: ', i.verVuelo())
        
mi_aerolinea = CopaAirlines()        

while True:
    opciones = input('''
    1. Ingresar datos del pasajero
    2. Ver datos del pasajero
    3. Cantidad de pasajeros 
    4. Salir
    :''')
    if opciones == '1': 
        mi_aerolinea.ingresarPasajero()
    
    elif opciones == '2':
        mi_aerolinea.verDatos()
        
    elif opciones == '3':
        # Preguntar:
            # Si no pongo print, no sale nada?
        print('Ahora hay: ' + str(mi_aerolinea.verNumPasajeros()))
        
    elif opciones == '4':
        print('GRACIAS POR VOLAR CON NOSOTROS')
        break
    
    else:
        print('Opcion invalida, vuelve a intentarlo')
        
#%% El EJERCICIO DE COPAAIRLINES Y PASAJERO (V2)
# INSTRUCCIONES:
    # Ingresar Pasajero Nuevo:
        # Se solicita la info desde el metodo main
    # Ver todos los datos:
        # Se pasa la cedula y CopaAirlines devuelve el obj asociado
class Pasajero1:
    def __init__(self):
        # Atributos de pasajero
        self.__nombre = ''
        self.__cedula = 0
        self.__destino = ''
        self.__vuelo = ''
              
    # Metodos ver clase paciente
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verDestino(self):
        return self.__destino
    def verVuelo(self):
        return self.__vuelo
    
    # Metodos asignar clase paciente
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarCedula(self, c):
        self.__cedula = c
    def asignarDestino(self, d):
        self.__destino = d
    def asignarVuelo(self, v):
        self.__vuelo = v
                
class CopaAirlines1:
    def __init__(self):
        self.__listaPasajeros = []
        
    def ingresarPasajero(self, pax):
        self.__listaPasajeros.append(pax)
        
    def verDatosPax(self, c):
        # Voy a buscar pasajero por pasajero
        for p in self.__listaPasajeros:
            if c == p.verCedula():
                return p # Si encuentro el paciente lo retorno
        
    def verNumPax(self):
        print('En CopaAirlines hay ' +  str(len(self.__listaPasajeros)) + ' pasajeros')
        
def main():
    aerolinea = CopaAirlines1()
    while True:
        opciones = input('''
        A continuacion seleccione la opcion que desee...
        1. Ingresar Pajareno Nuevo
        2. Ver datos de pax existente
        3. Ver numero de pax
        4. Salir
        :''')
        if opciones == '1':
            # 1- Creo el objeto 
            pax = Pasajero1()
            # 2- Se solicitan datos y se utilizan los metodos de asignar
            pax.asignarNombre(input('Ingrese el nombre del pasajero: '))
            pax.asignarCedula((int(input('Ingresar la cedula del pasajero: '))))
            pax.asignarDestino(input('Ingresar destino del pasajero: '))
            pax.asignarVuelo(input('Ingresar el numero de vuelo del pasajero: '))
            # 3- Se almacena en la lista que esta dentro de la clase sistema
            aerolinea.ingresarPasajero(pax)
            
        elif opciones == '2':
            # Solicito la cedula
            c = int(input('Ingrese la cedula: '))
            # le pido al sistema que me devuelva en la variable p al pasajero 
            # que tenga la cc en la lista
            p = aerolinea.verDatosPax(c)
            # Si encuentro al pasajero, imprimo los datos
            print('Nombre: ' , p.verNombre())
            print('Cedula: ' , str(p.verCedula()))
            print('Destino:' , p.verDestino())
            print('Vuelo: ' , p.verVuelo())
    
        elif opciones == '3':
            aerolinea.verNumPax()
            
        elif opciones == '4':
            print('GRACIAS POR VOLAR CON NOSOTROS')
            break
        else:
            print('Opcion invalida, vuelva a intentarlo')
            
if __name__ == '__main__':
    main()
    
#%% El EJERCICIO DE COPAAIRLINES Y PASAJERO (V3)
class Pax:
    def __init__(self):
        # Atributos de pasajero
        self.__nombre = ''
        self.__cedula = 0
        self.__destino = ''
        self.__vuelo = ''
              
    # Metodos ver clase paciente
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verDestino(self):
        return self.__destino
    def verVuelo(self):
        return self.__vuelo
    
    # Metodos asignar clase paciente
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarCedula(self, c):
        self.__cedula = c
    def asignarDestino(self, d):
        self.__destino = d
    def asignarVuelo(self, v):
        self.__vuelo = v
        
class airline:
    # Creamos la lista dondevamos a almacenar la informacion
    def __init__(self):
        self.__listapax = []
    # Se crea un metodo para verificar pacientes existentes
    def verificarPax(self, cedula):
        # Creamos variable bandera
        encontrado = False
        # Utilizamos el for para que busque uno a uno
        for i in self.__listapax:
            if cedula == i.verCedula():
                encontrado = True # Si encuentro al paciente actualizo la bandera
                break # Salgo del for
        return encontrado
    
    def ingresarPax(self, paxs):
        # 1ro se verifica la existencia antes de ingresar al paciente
        if self.verificarPax(paxs.verCedula()):
            return False
        # Si no existe lo agrego a la lista
        self.__listapax.append(paxs)
        return True
    
    def verDatosPax(self, c):
        # Verifico primero si existe
        if self.verificarPax(c) == False:
            return None
        # Voy a buscar pasajero por pasajero
        for p in self.__listapax:
            if c == p.verCedula():
                return p
                
    def verNumPax(self):
        print('Ahora hay en la aerolinea ' + str(len(self.__listapax)) + ' pasajeros')
        
def main():
    air = airline()
    while True:
        # Se hace el menu
        opciones = input('''
        1. Ingresar pasajero nuevo
        2. Ver datos del pasajero
        3. Ver numero total de pasajeros
        4. Salir
        :''')
        
        if opciones == '1':
            # Se crea el objeto y se solicitan los datos
            paxs = Pax()
            paxs.asignarNombre(input('Ingresar nombre del pasajero: '))
            paxs.asignarCedula(int(input('Ingresar la cedula del pasajero: ')))
            paxs.asignarDestino(input('Ingresar el destino: '))
            paxs.asignarVuelo(input('Ingresar el numero del vuelo: '))
            
            # se almacena en la lista que esta dentro de air en ingresarPax
            resultado= air.ingresarPax(paxs) 
            
            if resultado == False:
                print('Ya existe un pasajero con esta cedula')
            else:
                print('Pasajero ingresado con exito')
        
        elif opciones == '2':
            #  Se solicita la cedula que se quiere buscar
            c = int(input('Ingrese la cedula del pasajero'))
            # Le pido al sistema que se devuelva en la variable p
            # al paciente que tenga la cedula pedida
            p = air.verDatosPax(c)
            # si encuentro al pasajero imprimo los datos
            if p != None:
                print('Nombre: ', p.verNombre())
                print('Cedula: ', str(p.verCedula()))
                print('Destino: ', p.verDestino())
                print('Vuelo: ', p.verVuelo())
                
            else:
                print('No existe paciente con esta cedula')
                
        elif opciones == '3':
            air.verNumPax()
            
        elif opciones == '4':
            break
        else:
            print('Opcion no valida, intentelo de nuevo')
            
if __name__ == '__main__':
    main()
                            
    