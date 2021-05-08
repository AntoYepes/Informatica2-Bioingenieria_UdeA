#VISTA
#1 importamos
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog, QMessageBox, QLineEdit, QTextEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QRegExp

#2 creamos clases lo quee esta dentro de la ventana principal y los nombres de los botones

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaPrincipal, self).__init__(ppal)
        loadUi("ventana_principal.ui", self)
        self.setup()
        
    def setup(self):
        #dentro del aprentesis ponemos self. abirir la ventana del boton que yo hunda
        self.boton_ingresar.clicked.connect(self.abrir_ventana_ingresar)
        self.boton_aumentar.clicked.connect(self.abrir_ventana_aumentar)
        self.boton_disminuir.clicked.connect(self.abrir_ventana_disminuir)
        self.boton_cantidad.clicked.connect(self.abrir_ventana_cantidad)
        self.boton_salir.clicked.connect(self.salir)
        
    # Metodo para el constructor
    def setControlador(self, c):
        self.__mi_coordinador = c
    
    # Metodo para recibir informacion
    def recibir_info(self, n, r, f, e, c):
        self.__mi_coordinador.agregarMedicamento(n, r, f, e, c)
        
    # Metodo aumentar stock
    def aumentar(self, r, c):
        self.__mi_coordinador.aumentarStock(r,c)
        
    # Metodo disminuir stock
    def disminuir(self, r,c):
        self.__mi_coordinador.disminuirStock(r,c)
      
    # Metodo cantidad stock
    def cantidad(self, r):
       return  self.__mi_coordinador.cantidadStock(r)
         
    #Metodos del setup
    def abrir_ventana_ingresar(self):
        #creo el objeto
        ventana_ingresar = VentanaIngresar(self) #Nombre de VentanaIngresar tiene que ser el mismo de la clase
        ventana_ingresar.show()
        self.hide()
        
    def abrir_ventana_aumentar(self):
        #crear objeto
        ventana_aumentar =  VentanaAumentar(self)
        ventana_aumentar.show()
        self.hide()
        
    def abrir_ventana_disminuir(self):
        #cerear objeto
        ventana_disminuir = VentanaDisminuir(self)
        ventana_disminuir.show()
        self.hide()
        
    def abrir_ventana_cantidad(self):
        #crear objeto
        ventana_cantidad = VentanaCantidad(self)
        ventana_cantidad.show()
        self.hide()
        
    def salir(self):
        self.close()
        
class VentanaIngresar(QDialog):
    def __init__ (self, ppal = None):
        super(VentanaIngresar, self).__init__(ppal)
        loadUi("ventana_ingreso.ui", self)
        self.setup()
        self.__ventana_padre = ppal
        
    def setup(self):
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_referencia.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        

    #Metodos de opcion aceptar y opcion cancelar
    def opcion_aceptar(self):# cuando oprimo aceptar, quiero que se me guarde todo lo que llene
        nombre = self.campo_nombre.text()
        referencia = self.campo_referencia.text()
        fecha = self.campo_fecha.date()
        efectos = self.campo_efectos.toPlainText()
        cantidad = self.campo_cantidad.value()
        self.__ventana_padre.recibir_info(nombre, referencia, fecha, efectos, cantidad)
        self.__ventana_padre.show()
        
    def opcion_cancelar(self): # que me muestre la ventana principal
        self.ventana_padre.show()
        
class VentanaAumentar(QDialog):
    def __init__(self,ppal = None):
        super(VentanaAumentar,self).__init__(ppal)
        loadUi("ventana_stock.ui", self)
        self.setup()
        self.__ventana_padre = ppal
        
    def setup(self):
        self.campo_referencia.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        referencia = self.campo_referencia.text()
        cantidad = self.campo_cantidad.value()
        self.__ventana_padre.aumentar(referencia, cantidad)
        self.__ventana_padre.show()
        
    def opcion_cancelar(self):
        self.__ventana_padre.show()
        
class VentanaDisminuir(QDialog):
    def __init__(self, ppal = None):
        super(VentanaDisminuir, self).__init__(ppal)
        loadUi("ventana_stock.ui", self)
        self.setup()
        self.__ventana_padre = ppal
        
    def setup(self):
        self.campo_referencia.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        referencia = self.campo_referencia.text()
        cantidad = self.campo_cantidad.value()
        self.__ventana_padre.disminuir(referencia, cantidad)
        
    def opcion_cancelar(self):
        self.__ventana_padre.show()
        
class VentanaCantidad(QDialog):
    def __init__(self,ppal = None):
        super(VentanaCantidad, self).__init__(ppal)
        loadUi("ventana_cantidad.ui",self)
        self.setup()
        self.__ventana_padre = ppal
        
    def setup(self):
        self.campo_referencia.setValidator(QIntValidator())
        self.buttonBox.clicked.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        resultado = self.campo_referencia.text()
        cantidad = self.__ventana_padre.cantidad(resultado)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str(cantidad))
        msgBox.setWindowTitle("Información")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
        
    def opcion_cancelar(self):
        self.__venatana_padre.show()

def main():
    app=QApplication(sys.argv)
    v= VentanaPrincipal()
    v.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()       