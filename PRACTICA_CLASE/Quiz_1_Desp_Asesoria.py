# QUIZ 1- DESPUES DE ASESORIA

# Clase protesis, guardare todo
class Protesis:
    # constructor
    def __init__(self):
        # Atributos
        self.__nombre = ''
        self.__numReferencia = 0
        self.__completo = 0
        self.__transtibial = 0
        self.__transfemoral = 0
        self.__transradial = 0
        self.__transhumeral = 0
        self.__pasivas = 0
        self.__mecanicas = 0 
        self.__electricas = 0
        self.__mioelectricas = 0

    # PROPIEDADES PROTESIS
    def getNombre(self):
        return self.__nombre
    def getNumReferencia(self):
        return self.__numReferencia
    
    def setNombre(self, no):
        self.__nombre = no
    def setNumReferencia(self, r):
        self.__numReferencia = r
    
    # PROPIEDADES DE CUBRIMIENTO
    def getCompleto(self):
        return self.__completo
    def getTranstibial(self):
        return self.__transtibial
    def getTransfemoral(self):
        return self.__transfemoral
    def getTransradial(self):
        return self.__transradial
    def getTranshumeral(self):
        return self.__transhumeral

    def setCompleto(self, c):
        self.__completo = c
    def setTranstibial(self, tt):
        self.__transtibial = tt
    def setTransfemoral(self, tf):
        self.__transfemoral = tf
    def setTransradial(self, tr):
        self.__transradial = tr
    def setTranshumeral(self, th):
        self.__transhumeral = th

    # PROPIEDADES DE TIPO   
    def getPasivas(self):
        return self.__pasivas   
    def getMecanias(self):
        return self.__mecanicas
    def getElectricas(self):
        return self.__electricas
    def getMioelectricas(self):
        return self.__mioelectricas
    
    def setPasivas(self, p):
        self.__pasivas = p
    def setMecanicas(self, m):
        self.__mecanicas = m
    def setElectricas(self, e):
        self.__electricas = e
    def setMioelectricas(self, mi):
        self.__mioelectricas = mi
        
# Clase Pasiva
class Pasiva(Protesis):
    # Constructor
    def __init__(self):
        super().__init__()
        
# Clase Mecanica
class Mecanica(Protesis):
    # Constructor
    def __init__(self):
        super().__init__()
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
class Electrica(Protesis):
    # Constructor
    def __init__(self):
        super().__init__()
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
        
# Clase sistema
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

def hereda(pro):
    pro.setNombre(input('Ingrese el nombre: '))
    pro.setCompleto(check('Ingresa el No del cubrimiento completo: '))
    pro.setTranstibial(check('Ingrese el No del cubrimiento transtibial: '))
    pro.setTransfemoral(check('Ingrese el No del cubrimiento transfemoral: '))
    pro.setTransradial(check('Ingrese el No del cubrimiento transradial: '))
    pro.setTranshumeral(check('Ingrese el No del transhumeral: '))
    
def out(p):
    print('Nombre: ' + str(p.getNombre()))
    print('NumRef: ' + str(p.getNumReferencia()))
    print('Completo: ' + str(p.getCompleto()))
    print('Transfemoral: ' + str(p.getTransfemoral()))
    print('TransHumeral: ' + str(p.getTranshumeral()))
    print('Transtibial: ' + str(p.getTranstibial()))
    print('Transradial: ' + str(p.getTransradial()))

def elect_mio(elect):
    elect.setTipoMotores(input('Ingrese tipo de motores: '))
    elect.setCantidadMotores(check('Ingrese cantidad de motores'))
    elect.setHardware(input('Ingrese el hardware: '))
    elect.setSoftware(input('Ingrese el software: '))

def guardar(p):
    with open ('Archivo.txt', 'a') as archivo:
        archivo.write('Nombre: ' + str(p.getNombre()) + '\n')
        archivo.write('NumRef: ' + str(p.getNumReferencia()) + '\n')
        archivo.write('Completo: ' + str(p.getCompleto()) + '\n')
        archivo.write('Transfemoral: ' + str(p.getTransfemoral()) + '\n')
        archivo.write('Transhumeral: ' + str(p.getTranshumeral()) + '\n')
        archivo.write('Transtibial: ' + str(p.getTranstibial()) + '\n')
        archivo.wirte('Transradial: ' + str(p.getTransradial()) + '\n')
        
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
        :''')

        if menu == 1: # Ingresar Protesis
            # 1. Verificamos si el numero de ref existe
            numRef = check('Ingrese el numero de referencia: ')
            if sis.verificarExistencia(numRef) == True:
                print('La protesis ya existe')
            else:
                opc = check('''
                1. Pasivas
                2. Mecanicas
                3. Electricas
                4. Mioelectricas
                :''')
                if opc == 1:
                    pas = Pasiva()
                    pas.setNumReferencia(numRef)
                    hereda(pas)
                    pas.setPasivas(check('Ingrese No pasivas: '))
                    pas.setNombre(input('Ingrese el nombre: '))
                    pas.setNumReferencia(numRef)
                    sis.ingresarProtesis(pas)
                    
                if opc == 2:
                    mec = Mecanica()
                    mec.setNumReferencia(numRef)
                    hereda(mec)
                    mec.setMecanicas(check('Ingres No mecanicas: '))
                    mec.setAccionamiento(input('Ingrese el accionamiento: '))
                    mec.setMaterialConstruido(input('Ingrese material contruido: '))
                    mec.setTipoSujecion(input('Ingrese el tio de sujecion: '))
                    sis.ingresarProtesis(mec)
                    
                if opc == 3:
                    elect = Electrica()
                    elect.setNumReferencia(numRef)
                    hereda(elect)
                    elect.setElectricas(check('Ingrese No Electricas: '))
                    elect_mio(elect)
                    sis.ingresarProtesis(elect)
                    
                if opc == 4:
                    mio = Mioelectrica()
                    mio.setNumReferencia(numRef)
                    hereda(mio)
                    mio.setMioelectricas(check('Ingrese No mioelectricas: '))
                    elect_mio(mio)
                    mio.setTipoSensores(input('Ingrese el tipo sensores: '))
                    sis.ingresarProtesis(mio)
                
        elif menu == 2: # Buscar
            opc1 = check('''
            1. Pasivas
            2. Mecanicas
            3. Electricas
            4. Mioelectricas
            :''')
            numRef = check('Ingresa el numero de referencia:')
            if sis.verificarExistencia(numRef) == True:
                p = sis.recuperarProtesis(numRef)
                 
                if opc1 == 1:
                    print('Pasivas: ' + str(p.getPasivas()))
                    out(p)
                    
                elif opc1 == 2:
                    print('Mecanica: ' + str(p.getMecanias()))
                    print('Accionamiento: ' + str(p.getAccionamiento()))
                    print('Material: ' + str(p.getMaterialConstruido()))
                    print('Sujecion: ' + str(p.getTipoSujecion()))
                    out(p)
                    
                elif opc1 == 3: 
                    print('Electricas: ' + str(p.getElectricas()))
                    print('Tipo motor: ' + str(p.getTipoMotores()))
                    print('Cantidad motores: ' + str(p.getCantidadMotores()))
                    print('Hardware: ' + str(p.getHardwaree()))
                    print('Software: ' + str(p.getSoftware()))
                    out(p)
                    
                elif opc1 == 4:
                    print('Mioelectricas: ' + str(p.getMioelectricas()))
                    print('Tipo motor: ' + str(p.getTipoMotores()))
                    print('Cantidad motores: ' + str(p.getCantidadMotores()))
                    print('Hardware: ' + str(p.getHardwaree()))
                    print('Software: ' + str(p.getSoftware()))
                    print('Tipo sensores: ' + str(p.getTipoSensores()))
                    out(p)
        
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
                        opc = check('''
                        1. Pasivo
                        2. Mecanico
                        3. Electrico
                        4. Mioelectrico
                        ''')
                        if opc == 1:
                            p.setPasivas(check('Ingresar las nuevas pasivo: '))
                        elif opc == 2:
                            p.setMecanicas(check('Ingresar las nuevas mecanicas: '))
                        elif opc == 3:
                            p.setElectricas(check('Ingresar las nuevas electricas: '))
                        elif opc == 4:
                            p.setMioelectricas(check('Ingresar las nuevas mioelectricas: '))
                elif menu1 == 4:
                    if sis.verificarExistencia(numRef) == True:
                        p = sis.recuperarProtesis(numRef)
                        opc1 = check('''
                        1. completo
                        2. TransFemoral
                        3. TransHumeral
                        4. Transtibial
                        5. TransRadial
                        ''')
                        if opc1 == 1:
                            p.setCompleto(check('Ingresar las nuevos c'))
                        elif opc1 == 2:
                            p.setTransfemoral(check('Ingresar los nuevo transfemorales: '))
                        elif opc1 == 3:
                            p.setTranshumeral(check('Ingresar los nuevos transhumeral: '))
                        elif opc1 == 4:
                            p.setTranstibial(check('Ingresar los nuevos transtibiales: '))
                        elif opc1 == 5:
                            p.setTransradial(check('Ingresar los nuevos transradiales: '))

        elif menu == 5: #  GUARDAR ARCHIVO
             if sis.verificarExistencia(numRef) == True:
                 p = sis.recuperarProtesis(numRef)
                 select = check ('''
                 1. Protesis
                 2. Tipo
                 ''')
                 if select == 1:
                     with open ('Archivo.txt', 'a') as archivo:
                         archivo.write('Nombre: ' + str(p.getNombre()) + '\n')
                         archivo.write('NumRef: ' + str(p.getNumReferencia()) + '\n')
                         archivo.write('Completo: ' + str(p.getCompleto()) + '\n')
                         archivo.write('Transfemoral: ' + str(p.getTransfemoral()) + '\n')
                         archivo.write('Transhumeral: ' + str(p.getTranshumeral()) + '\n')
                         archivo.write('Transtibial: ' + str(p.getTranstibial()) + '\n')
                         archivo.write('Transradial: ' + str(p.getTransradial()) + '\n')

                 elif select == 2:
                     opc2 = check('''
                     1. Pasiva
                     2. Mecanica
                     3. Electrica
                     4. Mioelectrica
                     :''')
                     if opc2 == 1:
                         with open ('Archivo.txt', 'a') as archivo:
                             archivo.write('Pasiva: ' + str(p.getPasivas()) + '\n')
                     if opc2 == 2:
                         with open ('Archivo.txt', 'a') as archivo:
                             archivo.write('Mecanicas: ' + str(p.getMecanias()) + '\n')
                             archivo.write('Accionamiento: ' + str(p.getAccionamiento()) + '\n')
                             archivo.write('Material: ' + str(p.getMaterialConstruido()) + '\n')
                             archivo.write('Sujecion: ' + str(p.getTipoSujecion()) + '\n')
                     if opc2 == 3:
                         with open ('Archivo.txt', 'a') as archivo:
                             archivo.write('Electricas: ' + str(p.getElectricas()) + '\n')
                             archivo.write('Tipo motor: ' + str(p.getTipoMotores()) + '\n')
                             archivo.write('Cantidad motores: ' + str(p.getCantidadMotores()) +'\n')
                             archivo.write('Hardware: ' + str(p.getHardwaree()) + '\n')
                             archivo.write('Software: ' + str(p.getSoftware()) + '\n')
                     if opc2 == 4:
                         with open ('Archivo.txt', 'a') as archivo:
                             archivo.write('MioElectricas: ' + str(p.getMioelectricas()) + '\n')
                             archivo.write('Tipo motor: ' + str(p.getTipoMotores()) + '\n')
                             archivo.write('Cantidad motores: ' + str(p.getCantidadMotores()) + '\n')
                             archivo.write('Hardware: ' + str(p.getHardwaree()) + '\n')
                             archivo.write('Software: ' + str(p.getSoftware()) + '\n')
                             archivo.write('Sensores: ' + str(p.getTipoSensores()) + '\n')
                             
        elif menu == 6:
            break
        else:
            print('Opcion no valida, vuelve a intentarlo')

if __name__ == '__main__':
    main()