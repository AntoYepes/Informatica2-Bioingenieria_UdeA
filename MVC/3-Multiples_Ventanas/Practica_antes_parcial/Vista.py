from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.uic import loadUi

class Ventana(QMainWindow):
    def __init__(self, ppal=None):
        super(Ventana, self).__init__(ppal)
        loadUi('tabla_paciente.ui', self)
        self.fila = 0
        self.setup()
        
    def setup(self):
        self.mi_tabla.setRowCount(10)
        self.mi_tabla.doubleClicked.connect(self.imprimir)
        self.boton_agregar.clicked.connect(self.opcion_agregar)
        
    def opcion_agregar(self):
        nombre = self.campo_nombre.text()
        cedula = self.campo_cedula.text()
        edad = self.campo_edad.text()
        genero = self.comboBox.currentText()
        
        self.mi_tabla.setItem(self.fila, 0, QTableWidgetItem(nombre))
        self.mi_tabla.setItem(self.fila, 1, QTableWidgetItem(cedula))
        self.mi_tabla.setItem(self.fila, 2, QTableWidgetItem(edad))
        self.mi_tabla.setItem(self.fila, 3, QTableWidgetItem(genero))
        
        self.fila += 1
        
        self.campo_nombre.setText('')
        self.campo_cedula.setText('')
        self.campo_edad.setText('')
        
        
    def imprimir(self):
        for elemento in self.mi_tabla.selectedItems():
            print(elemento.row(), elemento.column(), elemento.text())
        