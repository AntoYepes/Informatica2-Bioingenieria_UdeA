#%% VISTA
# Importamos
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QTextEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QRegExp

# Cremos la clase ppal
class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaPrincipal, self).__init__(ppal)
        loadUi('ventana_principal.ui', self)
        self.setup()
        
    # Metodo para el setup
    def setup(self):
        self.boton_login.clicked.connect(self, opcion_login)
        self.boton_choose.clicked.connect(self, opcion_choose)
        self.boton_logout.clicked.connect(self, opcion_salir)
        
    # Creamos el metodo que enlaza con controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    # Metodos que enlazan las ventanas QDialog, con ventana Ppal y Controlador
    def infoLogin(self, u, d):
        self.__mi_coordinador.recibirInfoLogin(u, d)
        
    # Metodos para abrir las ventanas 
    def opcion_login(self):
        ventana_login = VentanaLogin(self) # A continuacion se crea esta clase
        ventana_login.show()
        self.hide()
        
    def opcion_choose(self):
        ventana_choose = VentanaChooseGame(self) # A continuacion se crea esta clase
        ventana_choose.show()
        self.hide()
        
    def opcion_salir(self):
        self.close()
        
# Creamos la clase ventanaLogin
class VentanaLogin(QDialog):
    def __init__(self, ppal= None):
        super(VentanaLogin, self).__init__(ppal)
        loadUi('ventana_login.ui', self)
        self.setup()
        self.__ventana_ppal = ppal # Se crea para poder enlazar esta ventana con la ppal
        
    # Metodo para el setup
    def setup(self):
        self.campo_usuario.setValidator(QRegExpValidator(QRegExp('[A-Za-z]+')))
        self.campo_documento.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self, opcion_aceptar)
        self.buttonBox.rejected.connect(self, opcion_cancelar)
        
    # Metodos para aceptar o cancelar la info
    def opcion_aceptar(self):
        user = self.campo_usuario.text()
        doc = self.campo_documento.text()
        self.__ventana_ppal.infoLogin(user, doc) # Se enlaza la informacion con la ventana ppal 
        self.__ventana_ppal.show()
        
    def opcion_cancelar(self):
        self.__ventana_ppal.show()
        
# Creamos la clase ventanaChooseGame    
class VentanaChooseGame(QDialog):
    def __init__(self, ppal= None):
        super(VentanaChooseGame, self).__init__(ppal)
        loadUi('ventana_eleccion_juego.ui', self)
        self.setup()
        self.__ventana_ppal = ppal
        
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def ingresarNum(self, n):
        self.__mi_coordinador.recibirInfoNum(n)
        
    def setup(self):
        self.boton_juego1.clicked.connect(self, opcion_juego1)
        self.boton_juego2.clicked.connect(self, opcion_juego2)
        self.boton_cancelar.clicked.connect(self, opcion_cancelar)
        
    # Metodos para cada boton
    def opcion_juego1(self):
        ventana_juego1 = VentanaJuego1(self) # A continuacion se crea esta clase
        ventana_juego1.show()
        self.hide()
        
    def opcion_juego2(self):
        ventana_juego2 = VentanaJuego2(self) # A continuacion se crea esta clase
        ventana_juego2.show()
        self.hide()
        
    def opcion_cancelar(self):
        self.__ventana_ppal.show()
        
# Clase para la ventana del juego 1
class VentanaJuego1(QDialog):
    def __init__(self, ppal = None):
        super(VentanaJuego1, self).__init__(ppal)
        loadUi('ventana_juego1.ui', self)
        self.setup()
        self.__ventana_choose = ppal
        
    def setup(self):
        self.campo_numero.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self, opcion_aceptar)
        self.buttonBox.rejected.connect(self, opcion_cancelar)
        
    def opcion_aceptar(self):
        num = self.campo_numero.text()
        self.__ventana_choose.ingresarNum(num)
        self.__ventana_choose.show()
        
    def opcion_cancelar(self):
        self.__ventana_choose.show()
        
# Clase para la ventana del juego 2
class VentanaJuego2(QDialog):
    def __init__(self, ppal = None):
        super(VentanaJuego2, self).__init__(ppal)
        loadUi('ventana_juego2.ui', self)
        self.setup()
        self.__ventana_choose = ppal
        
    def setup(self):
        self.buttonBox.accepted.connect(self, opcion_aceptar)
        self.buttonBox.rejected.connect(self, opcion_cancelar)
        
    def opcion_aceptar(self):
        pass
    
    def opcion_cancelar(self):
        self.__ventana_choose.show()
        
class VentanaRanking(QDialog):
    def __init__(self, ppal = None):
        super(VentanaRanking, self).__init__(ppal)
        loadUi('ventana_ranking.ui', self)
        self.setup()
        
    def setup(self):
        self.campo_ranking.setValidator(QIntValidator())
        
def main():
    app = QApplication(sys.argv)
    v= VentanaPrincipal()
    v.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()  
# %%
