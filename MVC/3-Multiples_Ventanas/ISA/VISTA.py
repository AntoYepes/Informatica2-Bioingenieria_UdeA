from MODELO import Indices, Visitas
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QRegExp

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ventana_principal.ui",self)
        self.setup()

    def asignarControlador(self,c):
        self.__mi_coordinador=c

    def setup(self):
        self.boton_ingresarp.clicked.connect(self.abrir_ventana_paciente)
        self.boton_salir.clicked.connect(self.opcion_salir)

    def abrir_ventana_paciente(self):
        ventana_paciente= ventanaPaciente(self)
        #ventana_paciente= ventanaVisitas(self)
        ventana_paciente.asignarControlador(self.__mi_coordinador)
        self.hide()
        ventana_paciente.show()
        
    def opcion_salir(self):
        self.close()
        
class ventanaPaciente(QDialog):
    def __init__(self, ppal):
        super().__init__(ppal)
        self.__ventana_padre= ppal
        loadUi("ventana_paciente.ui",self)
        self.setup()

    def asignarControlador(self,c):
        self.__mi_coordinador=c

    def setup(self):
        self.boton_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.boton_edad.setValidator(QIntValidator())
        self.boton_cedula.setValidator(QIntValidator())
        self.boton_genero.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.boton_visitas.clicked.connect(self.abrir_ventana_visitas)
        self.boton_volver.clicked.connect(self.abrir_ventana_principal)
        self.boton_aceptar.clicked.connect(self.opcion_aceptar)
        self.boton_cancelar.clicked.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self): #Necesito que se guarde la informacion que llene
        nombre= self.boton_nombre.text()
        edad=self.boton_edad.text()
        cedula=self.boton_cedula.text()
        genero=self.boton_genero.text()
        msj= self.__mi_coordinador.RecibirInfoPaciente(nombre,edad,cedula,genero,0,1)
        QMessageBox.information(self, "Informacion" , str(msj) ,QMessageBox.Ok)
        
    def opcion_cancelar(self): #Volver a la ventana principal
        self.hide()
        self.__ventana_padre.show()        
                
    def abrir_ventana_visitas(self):
        ventana_visitas= ventanaVisitas(self.__ventana_padre)
        ventana_visitas.asignarControlador(self.__mi_coordinador)        
        self.hide()
        ventana_visitas.show()
        
    def abrir_ventana_principal(self):
        self.hide()
        self.__ventana_padre.show()        

    # def informacion_total(self,todo):
        #self.__informacion_total=todo    
class ventanaVisitas(QDialog):
    def __init__(self, ppal):
        super().__init__(ppal)
        self.__ventana_padre= ppal
        loadUi("ventana_visitas.ui",self)
        self.__visitas={}
        self.__inidices=None
        self.setup()


    #Enlazo con el controlador
    def asignarControlador(self,c):
        self.__mi_coordinador=c

    def setup(self):
        self.boton_fecha.date()
        self.boton_registro.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.boton_indice.clicked.connect(self.abir_ventana_indices)
        self.boton_aceptar.clicked.connect(self.opcion_aceptar)
        self.boton_cancelar.clicked.connect(self.opcion_cancelar)
        
    def abir_ventana_indices(self):
        ventana_indices= ventanaIndices(self)
        ventana_indices.asignarControlador(self.__mi_coordinador)
        ventana_indices.show()
        self.hide()
        

    def recbir_indices(self,c):
        self.__indices=c
        

    def asignarControlador(self,c):
        self.__mi_coordinador=c
        

    def opcion_aceptar(self):
        fecha= self.boton_fecha.date()
        registro= self.boton_registro.text()
        notas= self.boton_notas.toPlainText()
        if fecha not in self.__visitas:
            v=Visitas()
            v.asignarFecha(fecha)
            v.asignarRegistro(registro)
            v.asignarNotas(notas)
            self.__visitas[v.verFecha()]=v
        msj= self.__mi_coordinador.RecibirInfoVisitas(fecha,registro,notas)
        QMessageBox.Information(self,"Informacion" , str(msj) ,QMessageBox.Ok)
        self.__ventana_padre.informacion_total(self.__visitas)
        self.__ventana_padre.show()
        self.hide()
        
    def opcion_cancelar(self):
        self.__ventana_padre.show()
        self.close()
        
        
class ventanaIndices(QDialog):
    def __init__(self,ppal=None):
        super(ventanaIndices,self).__init__(ppal) 
        self.__ventana_padre=ppal 
        loadUi("ventana_indices.ui", self)
        self.setup()
    #Lo enlazo con el controlador
    def asignarControlador(self,c):
        self.__mi_coordinador=c
    
    def setup(self):
        self.boton_pot_d.setValidator(QIntValidator())
        self.boton_pot_t.setValidator(QIntValidator())
        self.boton_pot_a1.setValidator(QIntValidator())
        self.boton_pot_a2.setValidator(QIntValidator())
        self.boton_pot_b.setValidator(QIntValidator())
        self.boton_pot_g.setValidator(QIntValidator())
        self.boton_aceptar.clicked.connect(self.opcion_aceptar)
        self.boton_cancelar.clicked.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        delta=self.boton_pot_d.text()
        teta=self.boton_pot_t.text()
        alfa1=self.boton_pot_a1.text()
        alfa2=self.boton_pot_a2.text()
        beta=self.boton_pot_b.text()
        gama=self.boton_pot_g.text()
        
        h= Indices()
        h.asignarPot_D(delta)
        h.asignarPot_T(teta)
        h.asignarPot_A1(alfa1)
        h.asignarPot_A2(alfa2)
        h.asignarPot_B(beta)
        h.asignarPot_G(gama)
        
        msj= self.__ventana_padre.recbir_indices(h)
        QMessageBox.information(self, "Informacion", str(msj),QMessageBox.Ok)
        
        self.__ventana_padre.show()
        self.hide()  
    
    def opcion_cancelar(self):
        self.close()
        
        
def main():
    app=QApplication(sys.argv)
    v= VentanaPrincipal()
    v.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
