from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi

# Necesitamos un codigo lazador
class Ventana(QMainWindow):
    def __init__(self, ppal=None):
        # Llamamos la constructor de la clase padre
        super(Ventana, self).__init__(ppal)
        loadUi('imagen.ui', self)
        self.setup()
        
    # Codigo de configuracion de la interfaz
    def setup(self):
        # señales y los slots
        pass