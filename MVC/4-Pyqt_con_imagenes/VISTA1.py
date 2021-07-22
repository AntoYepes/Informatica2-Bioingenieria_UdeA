from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi

class Ventana_botones(QMainWindow):
    def __init__(self, ppal=None):
        super(Ventana_botones, self).__init__(ppal)
        loadUi('botones.ui', self)
        self.setup()
        
    def setup(self):
        #El segundo boton se inhabilita
        self.boton2.setEnabled(False)
        # señales y slots
        self.boton2.clicked.connect(self.boton_presionado)
        self.boton1.clicked.connect(self.boton_presionado)
        
    def boton_presionado(self):
        # como ambos botones tienen el mismo slot debo preguntar cual 
        # era el que genero la señal estando habilitado
        # si el  primer boton estaba habilitado
        if self.boton1.isEnabled():
            #Habilito el segundo boton
            self.boton2.setEnabled(True)
            # Inhabilito el primero
            self.boton1.setEnabled(False)
        # El else actua en sentido contrario
        elif self.boton2.isEnabled():
            self.boton1.setEnabled(True)
            self.boton2.setEnabled(False)