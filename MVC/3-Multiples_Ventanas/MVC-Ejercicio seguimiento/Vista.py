import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QRegExp

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaPrincipal, self).__init__(ppal)
        loadUi('ventana_principal.ui', self)
        self.setup()
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.button_info.clicked.connect(self.abrir_ventana_paciente)
        self.button_salir.clicked.connect(self.opcion_salir)
        
    def abrir_ventana_paciente(self):
        ventana_infoPaciente = ventanaInfoPaciente(self)
        ventana_infoPaciente.setControlador(self.__mi_coordinador)
        self.hide()
        ventana_infoPaciente.show()
        
    def opcion_salir(self):
        self.close()
    
class ventanaInfoPaciente(QDialog):
    def __init__(self, ppal = None):
        super(ventanaInfoPaciente, self).__init__(ppal)
        loadUi('informacion.ui', self)
        self.ventana_padre = ppal
        self.setup()
    
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_edad.setValidator(QIntValidator())
        self.campo_cedula.setValidator(QIntValidator())
        self.campo_genero.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.button_visitas.clicked.connect(self.abrir_ventana_visitas)
        self.button_ppal.clicked.connect(self.abrir_ventana_ppal)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):# cuando oprimo aceptar, quiero que se me guarde todo lo que llene
        nombre = self.campo_nombre.text()
        edad = self.campo_edad.text()
        cedula = self.campo_cedula.text()
        genero = self.campo_genero.text()   
        mensaje = self.__mi_coordinador.agregarinfoPaciente(nombre, edad, cedula, genero)     
        QMessageBox.information(self, 'Informacion', str(mensaje), QMessageBox.Ok)
        
    def opcion_cancelar(self): # que me muestre la ventana principal
        self.hide()
        self.ventana_padre.show()
        
    def abrir_ventana_visitas(self):
        ventana_visitas = ventanaVisitas(self)
        ventana_visitas.setControlador(self.__mi_coordinador)
        self.hide()
        ventana_visitas.show()
        
    def abrir_ventana_ppal(self):
        self.hide()
        self.ventana_padre.show()
    
class ventanaVisitas(QDialog):
    def __init__(self, ppal = None):
        super(ventanaVisitas, self).__init__(ppal)
        loadUi('ventana_visitas.ui', self)
        self.ventana_padre = ppal
        self.setup()
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
    
    def setup(self):
        self.campo_registro.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.button_indices.clicked.connect(self.abrir_ventana_indices)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def abrir_ventana_indices(self):
        ventana_indices = ventanaIndices(self)
        ventana_indices.setControlador(self.__mi_coordinador)
        self.hide()
        ventana_indices.show()
    
    def opcion_aceptar(self):
        fecha = self.campo_fecha.date()
        registro = self.campo_registro.text()
        notas = self.campo_notas.toPlainText()
        mensaje = self.__mi_coordinador.recibir_infoVisita(fecha, registro, notas)
        QMessageBox.information(self, 'Informacion', str(mensaje), QMessageBox.Ok)
        
    def opcion_cancelar(self):
        self.close()

class ventanaIndices(QDialog):
    def __init__(self, ppal = None):
        super(ventanaIndices, self).__init__(ppal)
        loadUi('indices.ui', self)
        self.ventana_padre = ppal
        self.setup()
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
    
    def setup(self):
        self.campo_delta.setValidator(QIntValidator())
        self.campo_theta.setValidator(QIntValidator())
        self.campo_alfa1.setValidator(QIntValidator())
        self.campo_alfa2.setValidator(QIntValidator())
        self.campo_betha.setValidator(QIntValidator())
        self.campo_gamma.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):# cuando oprimo aceptar, quiero que se me guarde todo lo que llene
        delta = self.campo_delta.text()
        theta = self.campo_theta.text()
        alfa1 = self.campo_alfa1.text()
        alfa2 = self.campo_alfa2.text()
        betha = self.campo_betha.text()
        gamma = self.campo_gamma.text()        
        self.__mi_coordinador.recibir_indices(delta, theta, alfa1, alfa2, betha, gamma)
        
    def opcion_cancelar(self):
        self.close()
        
def main():
    app=QApplication(sys.argv)
    v= VentanaPrincipal()
    v.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()       