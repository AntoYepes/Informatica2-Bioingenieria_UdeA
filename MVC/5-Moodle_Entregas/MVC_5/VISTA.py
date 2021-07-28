#%% VISTA
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QTextEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import QRegExp, QSize, Qt
import random
import string

# Creamos la clase de la ventana principal
class VentanaLogin(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaLogin, self).__init__(ppal)
        loadUi('ventana_login.ui', self)
        self.setup()
        
    def setup(self):
        self.campo_usuario.setValidator(QRegExpValidator(QRegExp('[A-Za-z]+')))
        self.campo_documento.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def opcion_aceptar(self):
        user = self.campo_usuario.text()
        doc = self.campo_documento.text()
        self.__mi_coordinador.infoLogin(user, doc)
        ventana_eleccion = VentanaEleccion(self)
        ventana_eleccion.setControlador(self.__mi_coordinador)
        ventana_eleccion.show()
        self.hide()
        
    def opcion_cancelar(self):
        self.close()
        
# Creamos la clase de la ventana eleccion juego
class VentanaEleccion(QDialog):
    def __init__(self, ppal = None):
        super(VentanaEleccion, self).__init__(ppal)
        loadUi('ventana_eleccion_juego.ui', self)
        self.setup()
        self.__ventana_ppal = ppal
        
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.boton_juego1.clicked.connect(self.opcion_juego1)
        self.boton_juego2.clicked.connect(self.opcion_juego2)
        self.boton_cancelar.clicked.connect(self.opcion_cancelar)

    def opcion_juego1(self):
        juego1 = VentanaJuego1(self)
        juego1.show()
        juego1.setControlador(self.__mi_coordinador)
        self.hide()
        
    def opcion_juego2(self, c):
        juego2 = VentanaJuego2(self)
        juego2.show()
        juego2.setControlador(self.__mi_coordinador)
        self.hide()
        
    def opcion_cancelar(self):
        self.close()
        self.__ventana_ppal.show()
    
class VentanaJuego1(QDialog):
    def __init__(self, ppal = None):
        super(VentanaJuego1, self).__init__(ppal) 
        loadUi('ventana_juego1.ui', self)
        self.setup()
        self.__ventana_ppal = ppal
        
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.campo_numero.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcion_guess)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_guess(self):
        num = self.campo_numero.text()
        resultado = self.__mi_coordinador.guessNum(num)
        msm = QMessageBox.information(self, 'Intentos', str(resultado[0]))
        msm2 = QMessageBox.information(self, 'Numeros ok', str(resultado[1]))
        juego_1_1 = VentanaJuego1(self)
        juego_1_1.setControlador(self.__mi_coordinador)
        juego_1_1.show()
        
    def opcion_cancelar(self):
        self.close()
        # self.__ventana_ppal.show() 
class VentanaJuego2(QDialog):
    def __init__(self, ppal = None):
        super(VentanaJuego2, self).__init__(ppal)
        loadUi('ventana_juego2.ui', self)
        self.setup()
        self.__ventana_ppal = ppal
        
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.uno.clicked.connect(self.btn1)
        self.dos.clicked.connect(self.btn2)
        self.tres.clicked.connect(self.btn3)
        self.cuatro.clicked.connect(self.btn4)
        self.cinco.clicked.connect(self.btn5)
        self.seis.clicked.connect(self.btn6)
        self.siete.clicked.connect(self.btn7)
        self.ocho.clicked.connect(self.btn8)
        self.nueve.clicked.connect(self.btn9)
        self.buttonBox.acceptes.connect(self.matching_game)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def btn1(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.uno.setText(str(matrix[0, 0]))
        
    def btn2(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.dos.setText(str(matrix[0, 1]))
        
    def btn3(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.tres.setText(str(matrix[0, 2]))  
        
    def btn4(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.cuatro.setText(str(matrix[1, 0]))
        
    def btn5(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.cinco.setText(str(matrix[1, 1]))
        
    def btn6(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.seis.setText(str(matrix[1, 2]))
        
    def btn7(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.siete.setText(str(matrix[2, 0]))
        
    def btn8(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.ocho.setText(str(matrix[2, 1]))
    
    def btn9(self):
        matrix = self.__mi_coordinador.matrix_button()
        self.nueve.setText(str(matrix[2, 2]))
        
    def matching_game(self):
        pass
    
    def opcion_cancelar(self):
        self.close()
        self.__ventana_ppal.show()
        
def main():
    app = QApplication(sys.argv)
    v = VentanaLogin()
    v.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 
# %%
