class Protesis:
    def __init__(self):
        self.__nombre = ""        
        self.__referencia = 0       
        self.__tipo = ""        
        self.__cubrimiento = ""
        self.__zona = ""

    def getNombre(self):
        return self.__nombre
    def getRef(self):
        return self.__referencia
    def getTipo(self):
        return self.__tipo
    def getCubrimi(self):
        return self.__cubrimiento
    def getZona(self):
        return self.__zona
    
    def setNombre(self, n):
        self.__nombre = n
    def setRef(self, r):
        self.__referencia = r
    def setTipo(self, t):
        self.__tipo = t
    def setCubrimi(self, c):
        self.__cubrimiento = c
    def setZona(self, z):
        self.__zona = z

class Mecanica(Protesis):
    def __init__(self):
        super().__init__()
        self.__accionamiento=  ""
        self.__material=  ""
        self.__sujeción=  ""
        
    def getAccionamiento(self):
        return self.__accionamiento
    def getMaterial(self):
        return self.__material
    def getSujecion(self):
        return self.__sujecion
    
    def setAccionamiento(self, acc):
        self.__accionamiento = acc
    def setMaterial(self, ma):
        self.__material = ma
    def setSujecion(self, suj):
        self.__sujecion = suj
        
class Electrica(Protesis): 
    def __init__(self):
        super().__init__()
        self.__tipoMotor=  ""
        self.__CantMotor=  ""
        self.__hardware=  ""
        self.__software=  ""  

    def getTipoMotor(self):
        return self.__tipoMotor
    def getCantMotor(self):
        return self.__CantMotor
    def getHardware(self):
        return self.__hardware
    def getSoftware(self):
        return self.__software
    
    def setTipoMotor(self, tm):
        self.__tipoMotor = tm
    def setCantMotor(self, cm):
        self.__CantMotor = cm
    def setHardware(self, h):
        self.__hardware = h
    def setSoftware(self, s):
        self.__software = s

class Mioelectrica(Electrica): 
    def __init__(self):
        super().__init__()
        self.__sensores = ""             
    def getSensors(self):
        return self.__sensores
    def setSensors(self, s):
        self.__sensores = s

class Sistema:
    def __init__(self) -> None:
        self.__listadoSuperior = {}
        self.__listadoInferior = {}

    def verificarExiste(self,r):
        if r in self.__listadoSuperior:
            return True
        if r in self.__listadoInferior:
            return True
        else:
            return False

        # return r in self.__listadoSuperior or r in self.__listadoInferior

    def registrar(self,p):
        if p.getZona == "Sup":
            self.__listadoSuperior[p.getRef()]=p
        else:
            self.__listadoInferior[p.getRef()]=p

    def buscar(self,r):
        if r in self.__listadoSuperior: 
            return self.__listadoSuperior[r]
        elif r in self.__listadoInferior:
            return self.__listadoInferior[r]
        else:
            return None

    def borrar(self,p):
        if p.verZona == "Sup":
            del self.__listadoSuperior[p.verRef()]
        else: 
            del self.__listadoInferior[p.verRef()]

    def archivo(self):
        pass

    
    def agregarPasiva(self, no_ref, tipo, nombre, cubrimiento, zona):
        p = Protesis()
        p.setNombre(nombre)
        p.setRef(no_ref)
        p.setTipo(tipo)
        p.setCubrimi(cubrimiento)
        p.setZona(zona)
        
        if p.getZona == "Sup":
            self.__listadoSuperior[no_ref]=p
        else:
            self.__listadoInferior[no_ref]=p
        
    def agregarMecanica(self, no_ref, tipo, nombre, cubrimiento, zona, accionamiento, material, sujecion):
        p = Mecanica()
        p.setNombre(nombre)
        p.setRef(no_ref)
        p.setTipo(tipo)
        p.setCubrimi(cubrimiento)
        p.setZona(zona)
        p.setAccionamiento(accionamiento)
        p.setMaterial(material)
        p.setSujecion(sujecion)
        
        if p.getZona == "Sup":
            self.__listadoSuperior[no_ref]=p
        else:
            self.__listadoInferior[no_ref]=p
    
    def agregarElectrica(self, nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software):
        pass
    
    def agregarMio(self, nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software, sensores):
        pass
        
        
# if str(tipo) == 'Pasiva':
#     p = Protesis()
# elif str(tipo) == 'Mecanica':
#     p = Mecanica()
# elif str(tipo) == 'Electrica':
#     p = Electrica()
# elif str(tipo) == 'Mioelectrica':
#     p = Mioelectrica()
# def main():
#     sist=SistemaProt()
#     while True:
#         print("Ingrese:\n 1 REgistrar nueva prótesise\n 2 Buscar prótesis\n 3 Borrar prótesis\n 4 Editar una prótesis\n 5 Cargar y guardar prótesis\n 6- Salir del sistema")
#         valor = validar("Valor: ")

#         if valor == 1:
#             ref =  validar("Ingrese Ref: ")
#             if sist.verificarExiste(ref):
#                 print ("Prótesis ya esta en el sistema...")
#             else: 
#                 print("Qué protesis desea ingresar: \n1 Pasiva \n2 Mecánica\n3 Eléctrica\n3 Mioeléctrica")
#                 v = validar("Prótesis: ")
#                 if v == 1:
#                     p = Protesis()
#                 elif v == 2:
#                     p = Mecanica()
#                 elif v == 3:
#                     p = Electrica()
#                 elif v == 4:
#                     p = Mioelectrica()
#                 p.asignarNombre(input("Nombre de la prótesis: "))
#                 p.asignarRef(validar("Referencia única: "))
#                 p.asignarTipo(input("Tipo de la prótesis: "))
#                 p.asignarCubrimi(input("Nivel de cubrimiento de la prótesis: "))
#                 p.asignarZona(input("Sup/Inf: "))
#                 if v == 2:
#                     p.asignarAccionamiento()
#                     p.asignarMaterial()
#                     p.asignarSujecion()
#                 if v == 3:
#                     p.asignarTipoMotor()
#                     p.asignarCantMotor()
#                     p.asignarHardware()
#                     p.asignarSoftware()
#                 if v == 4:
#                     p.asignarTipoMotor()
#                     p.asignarCantMotor()
#                     p.asignarHardware()
#                     p.asignarSoftware()
#                     p.asignarSensors()

#             sist.registrar(p)

#         elif valor == 2:
#             r = validar("Numero de referencia: ")
#             p = SistemaProt.buscar(r)
#             print(p.verNombre())
#             print(p.verRef())
#             print(p.verTipo())
#             print(p.verCubrimi())
            
#             if p.verTipo() == "Mecanica":
#                 print(p.verAccionamiento())
#                 print(p.verMaterial())
#                 print(p.verSujecion())
#             elif p.verTipo() == "Electrica":
#                 print(p.verTipo())
#                 print(p.verCant())
#                 print(p.verHardware())
#                 print(p.verSoftware())
#             elif p.verTipo() == "Mioelectrica":
#                 print(p.verTipo())
#                 print(p.verCant())
#                 print(p.verHardware())
#                 print(p.verSoftware())
#                 print(p.verSensors())

            
#         elif valor == 3:
#             ref = validar("Numero de referencia: ")
#             if sist.verificarExiste(ref):
#                 p = SistemaProt.borrar(r)
#             else:    
#                 print ("Prótesis no esta en el sistema...")


#         elif valor == 4:
#             ref = validar("Numero de referencia: ")
#             if sist.verificarExiste(ref):
#                 p=sist.buscar(ref)
#                 opcion = validar("Ingresar parar editar:\n0- Pasiva\n 1- Mecanica\n2- Electrica\n3- Mioelectrica\n Opción:  ")
#                 p.asignarNombre(input("Ingresar: "))
#                 p.asignarRef(input("Ingresar: "))
#                 p.asignarTipo(input("Ingresar: "))
#                 p.asignarCubrimi(input("Ingresar: "))
#                 if opcion == 1:
#                     p.asignarAccionamiento(input())
#                     p.asignarMaterial(input())
#                     p.asignarSujecion(input())
#                 if opcion == 2:
#                     p.asignarTipo(input())
#                     p.asignarCant(input())
#                     p.asignarHardware(input())
#                     p.asignarSoftware(input())
#                 if opcion == 3:
#                     p.asignarTipo(input())
#                     p.asignarCant(input())
#                     p.asignarHardware(input())
#                     p.asignarSoftware(input())
#                     p.asignarSensors(input())

#                 sist.registrar(p)

