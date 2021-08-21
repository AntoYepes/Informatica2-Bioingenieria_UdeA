from MODELO import Sistema
from VISTA import VentanaPrincipal
from PyQt5.QtWidgets import QApplication
import sys

class Coordinador:
    #como el coordinador une el modelo con la vista debe
    #tener acceso a los objetos de las dos clases
    def __init__(self,vista,sistema):
        self.__mi_vista=vista #alusion a lo que creo en la vista
        self.__mi_sistema=sistema # modelo #alusion a lo que creo en modelo
    # la vista pasa los datos que quiere guardar
    #en el modelo. Este metodo se encargara de
    #verificar que si se puedan guardar y en caso
    #de que si se pueda, se guardan.
    def RecibirInfoPaciente(self,n,e,c,g,v,i):
        if self.__mi_sistema.verificarExiste(c)==True:
            return "Ya el paciente existe"
        else:
            #Agregarlo
            self.__mi_sistema.ingresePac(n,c,e,g,v,i)
            return "Paciente agregado con exito"
    def RecibirInfoVisitas(self,f,r,n):
        if self.__mi_sistema.verificarExiste(r)==True:
            return "Esa visita ya existe"
        else:
            self.__mi_sistema.ingresarVisitas(f,r,n)
            return "La visita ha sido ingresada con exito"

    
#CODIGO CLIENTE
def main():
    app= QApplication(sys.argv)
    mi_vista= VentanaPrincipal()
    mi_sistema= Sistema()
    mi_coordinador= Coordinador(mi_vista, mi_sistema)
    mi_vista.asignarControlador(mi_coordinador)
    mi_vista.show()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()    