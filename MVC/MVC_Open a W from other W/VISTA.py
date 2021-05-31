#%% VISTA
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QTextEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QRegExp
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
        self.boton_ranking.clicked.connect(self.ranking)
        
    def opcion_guess(self):
        num = self.campo_numero.text()
        resultado = self.__mi_coordinador.guessNum(num)
        msm = QMessageBox.information(self, 'No de Intentos', str(resultado))
        juego_1_1 = VentanaJuego1(self)
        juego_1_1.show()
        
    def ranking(self):
        ventana_ranking = VentanaRanking(self)
        ventana_ranking.setControlador(self.__mi_coordinador)
        ventana_ranking.show()
        
    def opcion_cancelar(self):
        self.close()
        self.__ventana_ppal.show()
        
class VentanaRanking(QDialog):
    def __init__(self, ppal = None):
        super(VentanaRanking, self).__init__(ppal)
        loadUi('ventana_ranking.ui', self)
        self.setup()
        self.__ventana_ppal  = ppal
        
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.campo_ranking.setValidator(QIntValidator())
        
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
        self.buttonBox.accepted.connect(self.opcion_busq_pareja)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def btn1(self):
        self.uno.setText(random.choice(string.ascii_letters[0:5]))
    def btn2(self):
        self.dos.setText(random.choice(string.ascii_letters[0:5]))
    def btn3(self):
        self.tres.setText(random.choice(string.ascii_letters[0:5]))   
    def btn4(self):
        self.cuatro.setText(random.choice(string.ascii_letters[0:5]))
    def btn5(self):
        self.cinco.setText(random.choice(string.ascii_letters[0:5]))
    def btn6(self):
        self.seis.setText(random.choice(string.ascii_letters[0:5]))
    def btn7(self):
        self.siete.setText(random.choice(string.ascii_letters[0:5]))
    def btn8(self):
        self.ocho.setText(random.choice(string.ascii_letters[0:5]))
    def btn9(self):
        self.nueve.setText(random.choice(string.ascii_letters[0:5]))
        
    def opcion_busq_pareja(self):
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
