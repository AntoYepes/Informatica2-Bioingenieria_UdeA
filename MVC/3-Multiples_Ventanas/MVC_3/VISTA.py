# 6to EJERCICIO DE ABSTRACCION:
    # VENTANAS MULTIPLES
# Importamos
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi

class ventanaPrincipal(QMainWindow):
    # constructor
    def __init__(self):
        # herencia super
        super(ventanaPrincipal, self).__init__()
        loadUi('ventanaPrincipal.ui', self)
        self.setup()
        
    def setup(self):
        self.boton_ingresar.clicked.connect(self.on_click_ingreso)
        self.boton_salir.clicked.connect(self.on_click_salir)
    
    # Recoge los datos de la clase ventana Ingreso en la clase opcion aceptar
    def recibirInfoIngresada(self, datos):
        nombre = datos[0]
        cedula = datos[1]
        self.__mi_controlador.validarUsuario(nombre, cedula)
        print('Recibido en ventana ppal: ' + nombre + '' + str(cedula)) 
        
    def on_click_ingreso(self):
        # creamos una ventana de ingreso pasando la ventana actual (ventanaPrincipal) como argumento
        ventana_ingreso = ventanaIngreso(self)
        # la hacemos visible
        ventana_ingreso.show()
        # ocultamos la ventana actual
        self.hide()
        
    def on_click_salir(self):
        self.close()
        
    def setControlador(self, c):
        self.__mi_controlador = c
        
class ventanaIngreso(QDialog):
    def __init__(self, ppal = None):
        # Esta clase padre se usa en el constructor
        super(ventanaIngreso, self).__init__(ppal)
        loadUi('ingreso.ui', self)
        self.setup()
        # guardo la referencia de la ventana padre
        self.__ventana_padre =  ppal
        
    def setup(self):
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        print('Dentro de la opcion aceptar')
        # recuperamos los campos
        n = self.nombre.text()
        c = int(self.cedula.text())
        # ingresamos los datos a la lista
        datos = [n, c]
        # se la pasamos a la ventana padre
        self.__ventana_padre.recibirInfoIngresada(datos)
        # hacemos de nuevo visible la ventana principal
        self.__ventana_padre.show()
    
    def opcion_cancelar(self):
        self.__ventana_padre.show()
        
def main():
    app = QApplication(sys.argv)
    widget = ventanaPrincipal()
    widget.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    