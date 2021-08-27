import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
from PyQt5.QtCore import Qt, QRegExp

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaPrincipal, self).__init__(ppal)
        loadUi('VentanaPrincipal.ui', self)
        self.setup()
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.boton_infoPaciente.clicked.connect(self.opcion_infoPaciente)
        self.boton_cant.clicked.connect(self.opcion_cantidad)
        self.boton_salir.clicked.connect(self.opcion_salir)
    
    def opcion_infoPaciente(self):
        ventana_infoPaciente = VentanaInfoPaciente(self)
        ventana_infoPaciente.setControlador(self.__mi_coordinador)
        self.hide()
        ventana_infoPaciente.show()
        
    def opcion_cantidad(self):
        ventana_cant = ventanaCant(self)
        ventana_cant.setControlador(self.__mi_coordinador)
        self.hide()
        ventana_cant.show()
        
    def opcion_salir(self):
        self.close()
        
class VentanaInfoPaciente(QDialog):
    def __init__(self, ppal = None):
        super(VentanaInfoPaciente, self).__init__(ppal)
        loadUi('infoPaciente.ui', self)
        self.ventana_padre = ppal
        self.setup()
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_cedula.setValidator(QIntValidator())
        self.campo_edad.setValidator(QIntValidator())
        self.campo_peso.setValidator(QIntValidator())
        self.campo_estatura.setValidator(QDoubleValidator())
        self.campo_genero.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_presion.setValidator(QIntValidator())
        self.campo_resultado.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        nombre = self.campo_nombre.text()
        cedula = self.campo_cedula.text()
        edad = self.campo_edad.text()
        peso = self.campo_peso.text()
        estatura = self.campo_estatura.text()
        genero =  self.campo_genero.text()
        presion = self.campo_presion.text()
        resultado = self.campo_resultado.text()
        info = self.__mi_coordinador.agregarInfoPac(nombre, cedula, edad, peso, estatura, genero, presion, resultado)
        QMessageBox.information(self, 'Informacion', str(info), QMessageBox.Ok)
        
        ventana_ppal = VentanaPrincipal(self)
        ventana_ppal.setControlador(self.__mi_coordinador)
        ventana_ppal.show()
        
        return cedula
        
    def opcion_cancelar(self):
        self.hide()
        self.ventana_padre.show()
        
class ventanaCant(QDialog):
    def __init__(self, ppal = None):
        super(ventanaCant, self).__init__(ppal)
        loadUi('infoClasificados.ui', self)
        self.ventana_padre = ppal
        self.setup()
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
    
    def setup(self):
        self.boton_clasificados.clicked.connect(self.opcion_buscarClasif)
        
    def opcion_buscarClasif(self):
        info = self.__mi_coordinador.infoClasificada()
        QMessageBox.information(self, 'Informacion', str(info), QMessageBox.Ok)

        ventana_ppal1 = VentanaPrincipal(self)
        ventana_ppal1.setControlador(self.__mi_coordinador)
        ventana_ppal1.show()
        
def main():
    app=QApplication(sys.argv)
    v= VentanaPrincipal()
    v.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()       