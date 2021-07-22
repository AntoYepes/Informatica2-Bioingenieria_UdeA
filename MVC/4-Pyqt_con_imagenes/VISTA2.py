from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5.uic import loadUi

class VentanaRadioButton(QMainWindow):
    def __init__(self, ppal=None):
        super(VentanaRadioButton, self).__init__(ppal)
        loadUi('radio_button.ui', self)
        self.setup()
        
    def setup(self):
        # El segundo boton se inhabilita
        self.boton2.setEnabled(False)
        # Señales y los slots en elte ejemplo ambps tienen el mismo slot
        self.boton2.clicked.connect(self.boton_presionado)
        self.boton1.clicked.connect(self.boton_presionado)
        #Senal para el raadio button1, en este ejemplo tienen la misma slot
        self.opcion1.toggled.connect(self.seleccion_opcion)
        self.opcion2.toggled.connect(self.seleccion_opcion)
        self.opcion3.toggled.connect(self.seleccion_opcion)
        #señal slot para el spin box
        self.valores.valueChanged.connect(self.cambio_valor)
        
    def boton_presionado(self):
        if self.boton1.isEnabled():
            #habilito el segundo botond
            self.boton2.setEnabled(True)
            self.boton1.setEnabled(False)
        elif self.boton2.isEnabled():
            #habilito el primer boton
            self.boton1.setEnabled(True)
            self.boton2.setEnabled(False)
            
    def seleccion_opcion(self):
        if self.opcion1.isChecked():
            texto = ""
            #Recordar que son dos grupos mutuamente excluyentes
            if self.opcion4.isChecked():
                texto = "Opcion 1"
            elif self.opcion5.isChecked():
                texto = "Opcion 2"
            # Recordar que son dos grupos mutuamente excluyentes
            if self.opcion6.isChecked():
                texto = "Opcion 3"
            elif self.opcion7.isChecked():
                texto = "Opcion 4"
            #Se muestra el resultado
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Resultado")
            msgBox.setText(texto)
            msgBox.show()
            
        def cambio_valor(self):
            valor = self.valores.value()
            #Se muestra el resultado
            msgBox = QMessageBox(self)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle("Resuldado")
            msgBox.setText("Valor ingresado: " + str(valor))
            msgBox.show()