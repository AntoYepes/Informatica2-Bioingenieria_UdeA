from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi

class Ventana_tabla(QMainWindow):
    def __init__(self, ppal=None):
        super(Ventana_tabla, self).__init__(ppal)
        loadUi('tabla.ui', self)
        self.setup()
        
    # Codigo de configuracion de la interfaz
    def setup(self):
        self.mi_tabla.setRowCount(10)
        self.boton_agregar.clicked.connect(self.opcion_agregar)
        
    def opcion_agregar(self):
        nombre = self.campo_nombre.text()
        cedula = self.campo_cedula.text()
        edad = self.campo_cedula.text()
        genero = self.campo_genero.currentText()
        
        self.mi_tabla.setItem(self.fila, 0, QTableWidgetItem(nombre))
        self.mi_tabla.setItems(self.fila, 1, QTableWidgetItem(cedula))
        self.mi_tabla.setItem(self.fila, 2, QTableWidgetItem(edad))
        self.mi_tabla.setItem(self.fila, 3, QTableWidgetItem(genero))
        
        self.fila += 1