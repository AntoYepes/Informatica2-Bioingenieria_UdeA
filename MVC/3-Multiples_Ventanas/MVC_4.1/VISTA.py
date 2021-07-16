# VISTA AEROPUERTO
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from MODELO import Vuelo

class ventanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(ventanaPrincipal, self).__init__(ppal)
        loadUi('ventanaPrincipal.ui', self)
        self.setup()
        
    def setup(self):
        self.boton_ingresar.clicked.connect(self.abrir_ventana_pax)
        
    def abrir_ventana_pax(self):
        ventana_pax = ventanaPasajero(self)
        ventana_pax.show()
        self.hide()
        
    def recibirPasajero(self, nombre, cedula, vuelo):
        resultado = self.__mi_coordinador.recibirInfoPax(nombre, cedula, vuelo)
        msm = QMessageBox.information(self, 'Mensaje de alerta', resultado, QMessageBox.Ok)
        
    def setControlador(self, c):
        self.__mi_coordinador = c
        
class ventanaPasajero(QDialog):
    def __init__(self, ppal= None):
        super(ventanaPasajero, self).__init__(ppal)
        loadUi('ventana_pasajero.ui', self)
        self.__vuelo_pax_actual = {}
        self.setup()
        self.__ventana_padre = ppal
    
    def setup(self):
        self.boton_agregar_vuelo.clicked.connect(self.abrir_ventana_vuelo)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def abrir_ventana_vuelo(self):
        ventana_vuelo = ventanaVuelo()
        ventana_vuelo.show()
        self.hide()
        
    def recibirVuelos(self, vuelo):
        self.__vuelo_pax_actual = vuelo
        
    def opcion_aceptar(self):
        nombre = self.campo_nombre.text()
        cedula = int(self.campo_cedula.text())
        self.__ventana_padre.recibirPasajero(nombre, cedula, self.__vuelo_actual)
        self.__ventana_padre.show()
        self.hide()
        
    def opcion_cancelar(self):
        self.__ventana_padre.show()
        self.hide()
        
class ventanaVuelo(QDialog):
    def __init__(self, ppal = None):
        super(ventanaVuelo, self).__init__(ppal)
        loadUi('ventana_vuelo.ui', self)
        self.__vuelos = {}
        self.setup()
        self.__ventana_padre = ppal
        
    def setup(self):
        self.boton_agregar.clicked.connect(self.recuperar_info_vuelo)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def recuperar_info_vuelo(self):
        num_vuelo = self.campo_num_vuelo.text()
        fecha_vuelo = self.campo_fecha.text()
        if num_vuelo not in self.__vuelos:
            v = Vuelo()
            v.setNumeroVuelo(num_vuelo)
            v.setFechaVuelo(fecha_vuelo)
            self.__vuelos[num_vuelo] = v
            mensaje = 'Guardado con exito'
        else:
            mensaje = 'Ya se habia asignado vuelo'
        msm = QMessageBox.information(self, 'Resultado de la operacion:  ', mensaje, QMessageBox.Ok)
           
        self.campo_num_vuelo.text('')
        self.campo_fecha.text('')
        
    def opcion_aceptar(self):
        self.__ventana_padre.recibirPasajero(nombre, cedula, self.__vuelos)
        self.__ventana_padre.show()
        self.hide()
        
    def opcion_cancelar(self):
        v = {}
        self.__ventana_padre.recibirVuelos(v)
        self.__ventana_padre.show()
        self.hide()
        
def main():
    app = QApplication(sys.argv)
    mi_ventana = ventanaVuelo()
    mi_ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
