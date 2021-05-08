# VISTA:
    # Señales y slot. construtor
# Importamos
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox

class VentanaLogin(QDialog):
    def __init__(self):
        super(VentanaLogin, self).__init__()
        loadUi('Ventana_ingreso.ui', self)
        self.setup()

    def setup(self):
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)

    # 1RO PROGRAMEMOS LA LOGICA DE LOS BOTONES:
    # 1- Recuperemos la informacion desde la interfaz de una vez se presione el boron aceptar
    # 2- Limpiamps los campos en la interfaz una vez se presiona cancelar

    def opcion_aceptar(self):
        login = self.campo_usuario.text()
        password = self.campo_password.text()
        self.__mi_controlador.validarUsuario(login, password)
        print('Ingresado: ' + login + '' + password)

    def opcion_cancelar(self):
        self.campo_usuario.setText('')
        self.campo_password.setText('')
        
    def closeEvent(self, event):
        print('Dentro del close')
        self.close()

    def setControlador(self, c):
        self.__mi_controlador = c
        