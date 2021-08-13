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
        self.contador = 0
        # self.vector = self.__mi_coordinador.inicializar_vector()
        
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.uno.clicked.connect(lambda: self.boton_check(1))
        self.dos.clicked.connect(lambda: self.boton_check(2))
        self.tres.clicked.connect(lambda: self.boton_check(3))
        self.cuatro.clicked.connect(lambda: self.boton_check(4))
        self.cinco.clicked.connect(lambda: self.boton_check(5))
        self.seis.clicked.connect(lambda: self.boton_check(6))
        self.siete.clicked.connect(lambda: self.boton_check(7))
        self.ocho.clicked.connect(lambda: self.boton_check(8))
        self.nueve.clicked.connect(lambda:self.boton_check(9))
        # self.buttonBox.accepted.connect(self.matching_game)
        # self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def boton_check(self, opc):
        if opc == 1:
            valor = self.__mi_coordinador.obtener_valor(0, 0)
            self.uno.setText(valor)
        elif opc == 2:
            valor = self.__mi_coordinador.obtener_valor(0, 1)
            self.dos.setText(valor)
        elif opc == 3:
            valor = self.__mi_coordinador.obtener_valor(0, 2)
            self.tres.setText(valor)
        elif opc == 4:
            valor = self.__mi_coordinador.obtener_valor(1, 0)
            self.cuatro.setText(valor)
        elif opc == 5:
            valor = self.__mi_coordinador.obtener_valor(1, 1)
            self.cinco.setText(valor)
        elif opc == 6:
            valor = self.__mi_coordinador.obtener_valor(1, 2)
            self.seis.setText(valor)
        elif opc == 7:
            valor = self.__mi_coordinador.obtener_valor(2, 0)
            self.siete.setText(valor)
        elif opc == 8:
            valor = self.__mi_coordinador.obtener_valor(2, 1)
            self.ocho.setText(valor)
        elif opc == 9:
            valor = self.__mi_coordinador.obtener_valor(2, 2)
            self.nueve.setText(valor)
        
    
    # def generador(self, btn):
    #     print('Gen')
        
    #     btn.setText(str(valor))
    #     self.vector[self.contador] = str(valor)
    #     self.contador += 1

    #     if (self.contador == 2):
    #         result = self.__mi_coordinador.comparar(self.vector)

        
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
