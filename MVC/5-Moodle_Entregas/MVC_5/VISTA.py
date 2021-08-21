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
        
    def reiniciar_matriz(self):
        self.uno.setText('x')
        self.dos.setText('x')
        self.tres.setText('x')
        self.cuatro.setText('x')
        self.cinco.setText('x')
        self.seis.setText('x')
        self.siete.setText('x')
        self.ocho.setText('x')
        self.nueve.setText('x')
        
        
    def boton_check(self, opc):
        if opc == 1:
            valor = self.__mi_coordinador.obtener_valor(0, 0)
            self.uno.setText(valor)
            if self.__mi_coordinador.verif_boton(0,0):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Informacion', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(0, 0)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 2:
            valor = self.__mi_coordinador.obtener_valor(0, 1)
            self.dos.setText(valor)
            if self.__mi_coordinador.verif_boton(0,1):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(0, 1)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 3:
            valor = self.__mi_coordinador.obtener_valor(0, 2)
            self.tres.setText(valor)
            if self.__mi_coordinador.verif_boton(0, 2):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(0, 2)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 4:
            valor = self.__mi_coordinador.obtener_valor(1, 0)
            self.cuatro.setText(valor)
            if self.__mi_coordinador.verif_boton(1, 0):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(1, 0)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 5:
            valor = self.__mi_coordinador.obtener_valor(1, 1)
            self.cinco.setText(valor)
            if self.__mi_coordinador.verif_boton(1,1):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(1, 1)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 6:
            valor = self.__mi_coordinador.obtener_valor(1, 2)
            self.seis.setText(valor)
            if self.__mi_coordinador.verif_boton(1, 2):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(1, 2)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 7:
            valor = self.__mi_coordinador.obtener_valor(2, 0)
            self.siete.setText(valor)
            if self.__mi_coordinador.verif_boton(2, 0):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(2, 0)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 8:
            valor = self.__mi_coordinador.obtener_valor(2, 1)
            self.ocho.setText(valor)
            if self.__mi_coordinador.verif_boton(2, 1):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(2, 1)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        elif opc == 9:
            valor = self.__mi_coordinador.obtener_valor(2, 2)
            self.nueve.setText(valor)
            if self.__mi_coordinador.verif_boton(2, 2):
                mensaje = 'ya boton'
                QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
            else:
                self.__mi_coordinador.agregar_valores(2, 2)
                
                if self.__mi_coordinador.tamano() == 2:
                    if self.__mi_coordinador.validar_valores():
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(0))
                        self.__mi_coordinador.agregar_posic(self.__mi_coordinador.devolver_coord(1))
                        self.__mi_coordinador.inicializar_vector()
                        
                    else:
                        mensaje = 'Suerte para la proxima'
                        self.__mi_coordinador.inicializar_vector()
                        QMessageBox.information(self, 'Intentos', mensaje, QMessageBox.Ok)
                        self.reiniciar_matriz()
                        self.__mi_coordinador.reiniciar_posic()
                        
        

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
