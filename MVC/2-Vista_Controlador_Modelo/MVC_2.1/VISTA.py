# VISTA

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

class ventanaLogin(QDialog):
    # Constructor
    def __init__(self):
        # super herencua
        super().__init__()
        loadUi('ventana_ingreso.ui', self)
        # atributo setup publico
        self.setup()
        
    # Metodo setup
    def setup(self):
        # self.NOMBRE DEL OBJ EN INTERFAZ.SEÑAL_INICIAL.connect(self.NOMBRE QUE QUIERA)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    # 1- Programamos la logica de los botones
    # A- Recuperemos la info desde la interfaz una vez se presione el boton aceptar
    # B- Limpiamos los campos en la interfaz una vez se presione el boton cancelar
    
    # Metodo para la opcion aceptar
    def opcion_aceptar(self):
        # Al ser un LINE EDIT, la manera de ingresar info es .text()
        login = self.campo_usuario.text()
        password = self.campo_password.text()
        # llamamos self.__mi_controlador, para que en el  metodo de alla se verifique
        self.__mi_controlador.validarUsuario(login, password)
        print('Ingresado: ' + login + '' + password)
    
    # Metodo para la opcion cancelar
    def opcion_cancelar(self):
        # Al ser LINE EDIT la manera de reasignar la informacion para que quede en blanco es .setText()
        self.campo_usuario.setText('')
        self.campo_password.setText('')
        
    def closeEvent(self, event):
        print('Dentro del close')
        self.close()
      
    # Metodo para asignar controlador
    def setControlador(self, c):
        self.__mi_controlador = c

        
        
        
        
    
        