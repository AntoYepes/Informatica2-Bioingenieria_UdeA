# # QUIZ No1
# Clase Cubrimiento
class Cubrimiento:
    # Constructor
    def __init__(self):
        self.__completo = 0

    # PROPIEDADES
    # Metodo set/get
    def getCompleto(self):
        return self.__completo
    def setCompleto(self, c):
        self.__completo = c

# Clase Tipo
class Tipo:
    # Constructor
    def __init__(self):
        # Atributos
        self.__pasivas = 0
        self.__mecanicas = 0
        self.__electricas = 0
        self.__mioelectricas = 0

    # PROPIEDADES
    # Metodos GET
    def getPasivas(self):
        return self.__pasivas
    def getMecanias(self):
        return self.__mecanicas
    def getElectricas(self):
        return self.__electricas
    def getMioelectricas(self):
        return self.__mioelectricas

    # Metodos SET
    def setPasivas(self, p):
        self.__pasivas = p
    def setMecanicas(self, m):
        self.__mecanicas = m
    def setElectricas(self, e):
        self.__electricas = e
    def setMioelectricas(self, mi):
        self.__mioelectricas = mi

# Clase Protesis
class Protesis:
    # constructor
    def __init__(self):
        # Atributos
        self.__nombre = ''
        self.__numReferencia = 0
        self.__tipo = {}
        self.__cubrimiento = {}

    # PROPIEDADES
    # Metodo get
    def getNombre(self):
        return self.__nombre
    def getNumReferencia(self):
        return self.__numReferencia

    # Metodos set
    def setNombre(self, no):
        self.__nombre = no
    def setNumReferencia(self, r):
        self.__numReferencia = r

    # Metodos para los 2 diccionarios
    # TIPO
    def verTipo(self, i):
        self.__tipo[i]
    def ingresarTipo(self, tipo):
        self.__tipo[1] = tipo

    # CUBRIMIENTO
    def verCubrimiento(self, x):
        self.__cubrimiento[x]

    def ingresarCubrimiento(self, cubri):
        self.__cubrimiento[1] = cubri

# Clase inferior
class Inferior(Protesis):
    # Constructor
    def __init__(self):
        Protesis.__init__(self)
        self.__transtibial = 0
        self.__transfemoral = 0

    # PROPIEDADES
    # Metodos set y get
    def getTranstibial(self):
        return self.__transtibial
    def getTransemoral(self):
        return self.__transfemoral

    def setTrantibial(self, tt):
        self.__transtibial = tt
    def setTransfemoral(self, tf):
        self.__transfemoral = tf

# Clase superior
class Superior(Protesis):
    # Constructor
    def __init__(self):
        Protesis.__init__(self)
        self.__transradial = 0
        self.__transhumeral = 0

    # PROPIEDADES
    # Metodos set y get
    def getTransradial(self):
        return self.__transradial
    def getTranshumeral(self):
        return self.__transhumeral

    def setTransradial(self, tr):
        self.__transradial = tr
    def setTranshumeral(self, th):
        self.__transhumeral = th

# Clase Pasiva
class Pasiva(Superior, Inferior):
    # Constructor
    def __init__(self):
        Superior.__init__(self)
        Inferior.__init__(self)
        
        
# Clase Mecanica
class Mecanica(Superior, Inferior):
    # Constructor
    def __init__(self):
        Superior.__init__(self)
        Inferior.__init__(self)
        # Atributos
        self.__accionamiento = ''
        self.__materialConstruido = ''
        self.__tipoSujecion = ''

    # PROPIEDADES
    # Metodos set y get
    def getAccionamiento(self):
        return self.__accionamiento
    def getMaterialConstruido(self):
        return self.__materialConstruido
    def getTipoSujecion(self):
        return self.__tipoSujecion

    def setAccionamiento(self, a):
        self.__accionamiento = a
    def setMaterialConstruido(self, mc):
        self.__materialConstruido = mc
    def setTipoSujecion(self, ts):
        self.__tipoSujecion = ts

# Clase Electrica
class Electrica(Superior, Inferior):
    # Constructor
    def __init__(self):
        Superior.__init__(self)
        Inferior.__init__(self)
        # Atributos
        self.__tipoMotores = ''
        self.__cantidadMotores = 0
        self.__hardware = ''
        self.__software = ''

    # PROPIEDADES
    # Metodos get y set
    def getTipoMotores(self):
        return self.__tipoMotores
    def getCantidadMotores(self):
        return self.__cantidadMotores
    def getHardwaree(self):
        return self.__hardware
    def getSoftware(self):
        return self.__software

    def setTipoMotores(self, tm):
        self.__tipoMotores = tm
    def setCantidadMotores(self, cm):
        self.__cantidadMotores = cm
    def setHardware(self, h):
        self.__hardware = h
    def setSoftware(self, s):
        self.__software = s

# Clase mioelectrica
class Mioelectrica(Electrica):
    # Constructor
    def __init__(self):
        Electrica.__init__(self)
        # Atributos
        self.__tipoSensores = ''

    # PROPIEDADES
    # Metodos get y set
    def getTipoSensores(self):
        return self.__tipoSensores
    def setTipoSensores(self, ts):
        self.__tipoSensores =  ts

# CLASE SISTEMA
class Sistema:
    # Constructor
    def __init__(self):
        self.__protesis = {}

    # PROPIEDADES
    # Metodos
    def verificarExistencia(self, numRef):
        return numRef in self.__protesis

    def ingresarProtesis(self, pro):
        self.__protesis[pro.getNumReferencia()] = pro

    def eliminarProtesis(self, numRef):
        del self.__protesis[numRef]

    def recuperarProtesis(self, numRef):
        return self.__protesis[numRef]

# FUNCION VALIDAR NUMERO ENTERO
def check(x):
   while True:
       try:
           value = int(input(x))
           break
       except ValueError:
           print('Ingrese un dato numerico...')
   return value

# MENU
def main():
    # Creo el obejto sistema
    sis = Sistema()
    # Creamos el menu con while True
    while True:
        menu = check('''
        1. Ingresar Protesis
        2. Buscar Protesis
        3. Borrar Protesis
        4. EditarProtesis
        5. Archivo Guardar
        6. Salir
        ''')

        if menu == 1: # Ingresar Protesis
            # 1. Verificamos si el numero de ref existe
            numRef = check('Ingrese el numero de referencia: ')
            if sis.verificarExistencia(numRef) == True:
                print('La protesis ya existe')
            else:
                # Como numRef no esta, creo el objeto y asigno
                pro = Protesis()
                pro.setNombre(input('Ingrese INFERIOR o SUPERIOR: '))
                pro.setNumReferencia(numRef)

                # Creo el objeto Tipo
                tipo = Tipo()
                tipo.setPasivas(check('Ingresa Pasivas: '))
                tipo.setMecanicas(check('Ingresa Mecanicas: '))
                tipo.setElectricas(check('Ingresa Electricas: '))
                tipo.setMioelectricas(check('Ingresa Mioelectricas: '))
                # Creo el objeto cubrimiento
                cubri = Cubrimiento()
                cubri.setCompleto(check('Ingresa Completa: '))

                pro.ingresarTipo(tipo)
                pro.ingresarCubrimiento(cubri)

                infe = Inferior()
                if pro == 'INFERIOR':
                    infe.setTrantibial(check('Ingresa la transtibial: '))
                    infe.setTransfemoral(check('Ingresa la tranfemoral: '))
                    
                    # Pasiva
                    pas = Pasiva()

                    # Mecanica
                    mec = Mecanica()
                    mec.setAccionamiento(input('Ingresa el Accionamiento: '))
                    mec.setMaterialConstruido(input('Ingresa el material contruido: '))
                    mec.setTipoSujecion(input('Ingresa el tipo de sujecion: '))

                    # Electrica
                    elec = Electrica()
                    elec.setTipoMotores(input('Ingresa el tipo de motores: '))
                    elec.setCantidadMotores(check('Ingresa la cantidad de motores: '))
                    elec.setHardware(input('Ingresa el hardware: '))
                    elec.setSoftware(input('Ingresa el software: '))

                    #  Mioelectricas
                    mio = Mioelectrica()
                    mio.setTipoSensores(input('Ingresa el tipo de sensores: '))


                else:
                    supe = Superior()
                    supe.setTranshumeral(check('Ingresa la transhumeral: '))
                    supe.setTransradial(check('Ingresa la transradial: '))

                    # Mecanica
                    mec = Mecanica()
                    mec.setAccionamiento(input('Ingresa el Accionamiento: '))
                    mec.setMaterialConstruido(input('Ingresa el material contruido: '))
                    mec.setTipoSujecion(input('Ingresa el tipo de sujecion: '))

                    # Electrica
                    elec = Electrica()
                    elec.setTipoMotores(input('Ingresa el tipo de motores: '))
                    elec.setCantidadMotores(check('Ingresa la cantidad de motores: '))
                    elec.setHardware(input('Ingresa el hardware: '))
                    elec.setSoftware(input('Ingresa el software: '))

                    #  Mioelectricas
                    mio = Mioelectrica()
                    mio.setTipoSensores(input('Ingresa el tipo de sensores: '))

                sis.ingresarProtesis(pro)

        elif menu == 2: # Buscar
            numRef = check('Ingresa el numero de referencia:')
            if sis.verificarExistencia(numRef) == True:
                p = sis.recuperarProtesis(numRef)
                cubri = p.verCubrimiento(1)

                print('Nombre: ' + str(p.getNombre()))
                print('NumRef: ' + str(p.getNumReferencia()))
                print('Completo: ' + str(cubri.getCompleto()))
                print('Transfemoral: ' + str(cubri.getTransfemoral()))
                print('TransHumeral: ' + str(cubri.getTranshumeral()))
                print('Transtibial: ' + str(cubri.getTranstibial()))
                print('Transradial: ' + str(cubri.getTransradial()))
                f = input('Ingrese fecha: ')
                if pro.verificarExistencia(f) == True:
                    # Traigo el objeto asociado
                    tipo = p.verTipo(f)
                    print('Mecanica: ' + str(tipo.getMecanias()))
                    print('Electricas: ' + str(tipo.getElectricas()))
                    print('Mioelectricas: ' + str(tipo.getMioelectricas()))
            
        elif menu == 3: # Borrar Protesis
            numRef = check('Ingresa el numero de referencia:')
            if sis.verificarExistencia(numRef) == True:
                p = sis.recuperarProtesis(numRef)
                sis.eliminarProtesis(p)

        elif menu == 4: # Editar Protesis
            numRef = check('Ingresa el numero de referencia:')
            if sis.verificarExistencia(numRef) == True:
                p = sis.recuperarProtesis(numRef)
                menu1 = check('''
                1. Nombre
                2. Num Referencia
                3. Tipo
                4. Cubrimiento
                ''')
                if menu1 == 1:
                    p.setNombre(input('Ingrese el nuevo nombre: '))
                elif menu1 == 2:
                    p.setNumReferencia(check('Ingresa el nuevo numero de referencia: '))
                elif menu1 == 3:
                    if sis.verificarExistencia(numRef) == True:
                        p = sis.recuperarProtesis(numRef)
                        t = p.verTipo(1)
                        opc = check('''
                        1. Pasivo
                        2. Mecanico
                        3. Electrico
                        4. Mioelectrico
                        ''')
                        if opc == 1:
                            t.setPasivas(check('Ingresar las nuevas pasivo: '))
                        elif opc == 2:
                            t.setMecanicas(check('Ingresar las nuevas mecanicas: '))
                        elif opc == 3:
                            t.setElectricas(check('Ingresar las nuevas electricas: '))
                        elif opc == 4:
                            t.setMioelectricas(check('Ingresar las nuevas mioelectricas: '))
                elif menu1 == 4:
                    if sis.verificarExistencia(numRef) == True:
                        p = sis.recuperarProtesis(numRef)
                        c = p.verCubrimiento(1)
                        opc1 = check('''
                        1. completo
                        ''')
                        if opc1 == 1:
                            c.setCompleto(check('Ingresar las nuevos c'))

        elif menu == 5: #  GUARDAR ARCHIVO
             if sis.verificarExistencia(numRef) == True:
                 p = sis.recuperarProtesis(numRef)
                 select = check ('''
                 1. Protesis
                 2. Tipo
                 3. Cubrimiento
                 ''')
                 if select == 1:
                     with open ('Archivo.tct', 'a') as archivo:
                         archivo.write('Nombre: ' + str(p.getNombre()))
                         archivo.write('NumRef: ' + str(p.getNumReferencia()))

                 elif select == 2:
                     t = p.verTipo(1)
                     with open ('Archivo.txt', 'a') as archivo:
                         archivo.write('Pasiva: ' + str(t.getPasivas()))
                         archivo.write('Mecanicas: ' + str(t.getMecanias()))
                         archivo.write('Electricas: ' + str(t.getElectricas()))
                         archivo.write('MioElectricas: ' + str(t.getMioelectricas()))

                 elif select == 3:
                     c = p.verCubrimiento(1)
                     with open ('Archivo.txt', 'a') as archivo:
                         archivo.write('Completo: ' + str(c.getCompleto()))

        elif menu == 6:
            break
        else:
            print('Opcion no valida, vuelve a intentarlo')

if __name__ == '__main__':
    main()