# 5to EJERC ABSTRACCION MVC
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

        print('Ingresado: ' + login + '' + password)

    def opcion_cancelar(self):
        self.campo_usuario.setText('')
        self.campo_password.setText('')

    # Si probramos veremos que la ventana se cerrara, algo que no queremos para el ejemplo.
    # Por lo que será mejor sobre-escribir los metodos accept y reject que por defecto cierran la ventana

    def setup(self):
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    # iv- Ahora, en la vista, debemos pasar esta informacion al controlador y recuperar el resultado
    def accept(self):
        login = self.campo_usuario.text()
        password = self.campo_password.text()
        # pasamos la informacion al controlador
        resultado = self.__mi_controlador.validarUsuario(login, password)
        # imprimimos el resultado de la operacion
        print('Resultado' + str(resultado))
        print('Ingresado: ' + login + '' + password)

    def reject(self):
        self.campo_usuario.setText('')
        self.campo_password.setText('')

    # Sobre-escribir este metodo nos implica tambien reescribir el metodo closeevent()
    def closeEvent(self, event):
        print('Dentro de close')
        self.close()

    # Ahora como hacemos llegar esa informacion al controlador?
    # Necesitamos que nuestra vista tenga acceso a un objeto controlador
    # i- Programamos un metodos para que pueda recibirlo

    def setControlador(self, c):
        self.__mi_controlador = c


#%% MODELO:
    # Acá iria la logica
class BaseDatos:
    def __init__(self):
        self.__login = ''
        self.__password = ''

    def setLogin(self, l):
        self.__login = l

    def setPassword(self, p):
        self.__password = p

    def validarUsuario(self, l, p):
        return (self.__login == l) and (self.__password == p)

#%% CONTROLADOR:
    # Acá se haria el enlace y se inica el programa

# Importamos
from Modelo import BaseDatos
from Vista import VentanaLogin
import sys
from PyQt5.QtWidgets import QApplication

class Coordinador:
    # Como el coordinador enlaza el modelo con la vista debe
    # tener acceso a objetos de ambas clases
    def __init__(self, vista, modelo):
        self.__mi_vista = vista
        self.__mi_modelo = modelo

    # iii- El controlador debe tener un metodo para recibir la info de la vista
    # Pero como el controlador es bruto, simplemente debe enviar esta info al modelo y esperar que este responda
    def validarUsuario(self, l, p):
        return self.__mi_modelo.validarUsuario(l, p)


# Simplemente se hacen las conexiones que siempre van
if __name__ == '__main__':
    app = QApplication((sys.argv))
    mi_vista = VentanaLogin()
    mi_modelo = BaseDatos()
    mi_coordinador = Coordinador(mi_vista, mi_modelo)

    mi_vista.show()
    sys.exit(app.exec())

# Esra clase no cambia ya que en esta simplemente se hacen las conexiones que siempre van
class Principal:
    def __init__(self):
        self.__app = QApplication((sys.argv))
        self.__mi_vista = VentanaLogin()
        self.__mi_modelo = BaseDatos()
        self.__mi_coordinador = Coordinador((self.__mi_vista), self.__mi_modelo)
         # ii- En la clase principal le asignamos este controlador a la ventana
        # Asignamos el controlador a la vista
        self.__mi_vista.setControlador(self.__mi_coordinador)
        # Asignamos un password y una contraseña
        self.__mi_modelo.setLogin('jfochoa')
        self.__mi_modelo.setPassword('1234')


    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())

p = Principal()
p.main()




