# VISTA CLASE 13
# VISTA PRACTICA

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super(ventanaPrincipal, self).__init__()
        loadUi('ventanaPrincipal.ui', self)
        self.setup()
        
    def setup(self):
        self.boton_ingreso.clicked.connect(self.on_click_ingresar)
        self.boton_salir.clicked.connect(self.on_click_salir)
    
    def ingresoInfo(self, datos):
        nombre = datos[0]
        cedula = datos[1]
        self.__mi_controlador.ingresarUsuario(nombre, cedula)
        print('Recibido en ventana ppal: ' + nombre + '' + str(cedula))
     
    # dentro creo objeto ventana ingreso
    def on_click_ingresar(self):
        ventana_ingreso = ventanaIngreso(self)
        ventana_ingreso.show()
        self.hide()
    
    def on_click_salir(self):
        self.close()
        
    def setControlador(self, c):
        self.__mi_controlador = c
        
class ventanaIngreso(QDialog):
    def __init__(self, ppal = None):
        super(ventanaIngreso, self).__init__(ppal)
        loadUi('ventana_ingreso.ui', self)
        self.setup()
        self.__ventana_padre = ppal
        
    def setup(self):
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        # creo nombre y cedula: datos
        nombre = self.campo_nombre.text()
        cedula = int(self.campo_cedula.text())
        datos = [nombre, cedula]
        self.__ventana_padre.ingresoInfo(datos) # ingresoInfo es un metodo de la clase padre
        self.__ventana_padre.show()
        
    def opcion_cancelar(self):
        self.__ventana_padre.show()
        
def main():
    app = QApplication(sys.argv)
    v = ventanaPrincipal()
    v.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
        



