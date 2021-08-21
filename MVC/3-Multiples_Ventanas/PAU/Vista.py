from Modelo import Indices, Visita
import datetime
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator,QIntValidator
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.uic import loadUi

class Ventana_Principal(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi('Ventana_principal.ui',self)
        self.setup()
    
    def asignarCoordinador(self,c):
        self.__mensaje = c
        
    def setup(self):
        self.ingresar_pac.clicked.connect(self.abrir_ven_pacientes)
        self.salir.clicked.connect(self.op_salir)
        
    def abrir_ven_pacientes(self):
        ventana_paciente = Ventana_ingresar(self)
        ventana_paciente.asignarCoordinador(self.__mensaje)
        self.hide()
        ventana_paciente.show()
        
    def op_salir(self):
        self.close()
    
    def closeEvent(self, event):
        d = QMessageBox.question(self,'Salir','¿Seguro que desea salir?',QMessageBox.Yes,QMessageBox.No)
        if d == QMessageBox.Yes:event.accept()
        else:
            event.ignore()
        
class Ventana_ingresar(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi('Ventana_ingresar.ui', self)
        self.__mi_ventana_principal = parent
        self.__informacion = None 
        self.setup()
        
    def asignarCoordinador(self,c):
        self.__mensaje = c
        
    def setup(self):
        self.c_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z]+")))  
        self.c_cedula.setValidator(QIntValidator())
        self.c_edad.setValidator(QIntValidator())
        self.c_genero.setValidator(QRegExpValidator(QRegExp("[a-zA-Z]+")))      
        self.cancelar.clicked.connect(self.opcion_cancelar)
        self.b_visitas.clicked.connect(self.opcion_agregar_visitas)
        self.b_ventanappal.clicked.connect(self.opcion_volverppal)
        
    def opcion_cancelar(self):
        self.__mi_ventana_principal.show() 
        self.hide()
    
    def opcion_agregar_visitas(self):
        # 1 recuperar los campos
        nombre = self.c_nombre.text()
        cedula = self.c_cedula.text()
        edad = self.c_edad.text()
        genero = self.c_genero.text()
        # 2. se envia la información al contralador
        enviar = self.__mensaje.AgregarPaciente(nombre, cedula, genero, edad, self.__informacion)
        print('nombre' + nombre)
        print('cedula' + cedula)
        print('edad' + edad)
        print('genero'+ genero)   
        QMessageBox.information(self, 'Informacion',' ' + str(enviar))
        
        ventana_visitas = Ventana_visitas(self)
        ventana_visitas.asignarCoordinador(self.__mensaje)
        ventana_visitas.show()
        self.hide()
        
    def opcion_volverppal(self):
        self.__mi_ventana_principal.show()
        self.hide()
        
    def informacion_total(self, todo):
        self.__informacion = todo
        
    def closeEvent(self, event):
        d = QMessageBox.question(self,'Salir','¿Seguro que desea salir de la ventana ingresar paciente?',QMessageBox.Yes,QMessageBox.No)
        if d == QMessageBox.Yes:
            event.accept()
            self.__mi_ventana_principal.show()
        else:
            event.ignore()
        
class Ventana_visitas(QDialog):
    def __init__(self, parent = None):
        super(Ventana_visitas,self).__init__(parent)
        loadUi("Ventana_visitas.ui",self)
        self.__mi_ventana_principal = parent
        self.__visitas = {}
        self.__indices = None
        self.setup()
        
    def asignarCoordinador(self,c):
        self.__mensaje = c
        
    def setup(self):
        self.b_indices.clicked.connect(self.abrir_ventana_indices)
        self.cancelar.clicked.connect(self.opcion_cancelar)
        
    def opcion_cancelar(self):
        self.__mi_ventana_principal.show()
        self.hide()
        
    def abrir_ventana_indices(self):
        fecha = self.c_fecha.date()
        fecha_s = fecha.toPyDate()
        electro = self.c_electro.text()
        notas = self.c_notas.toPlainText()
        if fecha not in self.__visitas: 
            v = Visita()
            v.asignarFecha(fecha)
            v.asignarElectro(electro)
            v.asignarNotas(notas)
            self.__visitas[v.verFecha()] = v 
            enviar = 'Se agrego la visita con exito'
        else:
            enviar = 'No se guardo la visita'
            
        QMessageBox.information(self, 'Informacion',' ' + str(enviar))
        
        self.__mi_ventana_principal.informacion_total(self.__visitas)
        
        ventana_indices = Ventana_indices(self)
        ventana_indices.asignarCoordinador(self.__mensaje)
        self.hide()
        ventana_indices.show()
        
    def recibir_indices(self, c):
        self.__indices = c
        return 'Se ha enviado toda la información correctamente'
    
        
    def closeEvent(self, event):
        d = QMessageBox.question(self,'Salir','¿Seguro que desea salir?',QMessageBox.Yes,QMessageBox.No)
        if d == QMessageBox.Yes:
            event.accept()
            self.__mi_ventana_principal.show()
        else:
            event.ignore()
            
class Ventana_indices(QDialog):
    def __init__(self, parent = None):
        super(Ventana_indices,self).__init__(parent)
        loadUi("Ventana_indices.ui",self) 
        self.__mi_ventana_principal = parent
        self.setup()
    
    def asignarCoordinador(self,c):
        self.__mensaje = c
      
        
    def setup(self):
        self.c_theta.setValidator(QRegExpValidator(QRegExp("[0-9.,]+")))
        self.c_delta.setValidator(QRegExpValidator(QRegExp("[0-9.,]+")))
        self.c_alfa1.setValidator(QRegExpValidator(QRegExp("[0-9.,]+")))
        self.c_alfa2.setValidator(QRegExpValidator(QRegExp("[0-9.,]+")))
        self.c_gamma.setValidator(QRegExpValidator(QRegExp("[0-9.,]+")))
        self.aceptar.clicked.connect(self.opcion_aceptar)
        self.cancelar.clicked.connect(self.opcion_cancelar)
        
    def opcion_cancelar(self):
        self.__mi_ventana_principal.show()
        self.hide()
        
    def opcion_aceptar(self):
        theta = self.c_theta.text()
        delta = self.c_delta.text()
        alfa1 = self.c_alfa1.text()
        alfa2 = self.c_alfa2.text()
        gamma = self.c_gamma.text()
        
        x = Indices()
        x.asignarAlfa1(alfa1)
        x.asignarDelta(delta)
        x.asignarTheta(theta)
        x.asignarGamma(gamma)
        x.asignarAlfa2(alfa2)
        enviar_indices = self.__mi_ventana_principal.recibir_indices(x)
        QMessageBox.information(self, 'Informacion',' ' + str(enviar_indices))
        ventana_Principal = Ventana_Principal(self)
        ventana_Principal.asignarCoordinador(self.__mensaje)
        ventana_Principal.show()
        
        self.hide()
        
        
    def closeEvent(self, event):
        d = QMessageBox.question(self,'Salir','¿Seguro que desea salir?',QMessageBox.Yes,QMessageBox.No)
        if d == QMessageBox.Yes:
            event.accept()
            self.__mi_ventana_principal.show()
        else:
            event.ignore()
        