"Interfeaz para gestionar los registros electrofisiológicos de los pacientes"

"El sistema debe permitir"
#Ventana principal --> Botón Permite ingrsar información del paciente
#                  --> Botón salir

    #Ventana ingresar paciente
    #Ingresar paciente   --> Nombre del paciente
    #                    --> Edad del paciente
    #                    --> Cédula del paciente
    #                    --> Género del paciente

        #Ventana ingresar visitas 
        #                 --> (mm/dd/aaaa)
        #                 --> Registro electroenfalográfico
        #                 --> Botón índices
        
            # Ventana Índices --> Potencia delta                      
            #                 --> POtencia theta
            #                 --> Potencia alfa1
            #                 --> Pontecia alfa2
            #                 --> Pontecia gamma
                
            
from Modelo import Servicio
from Vista import Ventana_Principal
import sys
from PyQt5.QtWidgets import QApplication


class Coordinador(object):
    #como el coordindor enlaza el modelo con la vista debe
    #tener acceso a objetos de ambas clases
    def __init__(self, vista, sistema):
        self.__mi_vista = vista 
        self.__mi_sistema = sistema 
    #La idea es que la vista pase los datos que quiere guardar en
    #el modelo, este metodo se encarga de verificar que si se puedan
    #guardar y en caso de que si se pueda se guardan
   # def AgregarPaciente(self, n, c, e, g, informacion):
   #     #verificamos que el paciente no exista
   #     if self.__mi_sistema.VerificarPaciente(c) == True:
   #         return "Ya el paciente existe!" 
   #     else:
   #         #si no existe lo agrega
   #         self.__mi_sistema.AgregarPaciente(n, c, e, g, informacion) 
   #         return "Paciente agregado ..." 
   #     
    def AgregarPaciente(self, n, c, e, g, i):
        return self.__mi_sistema.AgregarPaciente(n, c, e, g, i)

    #def Agregarvis(self,c,f):
    #    if self.__mi_sistema.verficarCedula(c) == False:
    #        return "El paciente no existe"
    #    else: 
    #        if self.__mi_sistema.VerificarVisita(c,f) ==True:
    #            return "el paciente ya tiene visita con esta fecha"
    #        else: 
    #            self.__mi_sistema.Agergarvis(c,n,d)
    #            return 'medicamento agregado'
# Código cliente
def main():
    app = QApplication(sys.argv) 
    mi_vista = Ventana_Principal() 
    mi_sistema = Servicio() 
    mensaje = Coordinador(mi_vista, mi_sistema) 
    mi_vista.asignarCoordinador(mensaje) 
    mi_vista.show() 
    sys.exit(app.exec_())     

if __name__=='__main__':
    main()  