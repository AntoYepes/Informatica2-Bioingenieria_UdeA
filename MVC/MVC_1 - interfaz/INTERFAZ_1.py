import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class LanzarApp(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('interfaz.ui', self)

def main():
    #maneja el flujo principal, con los eventos e interacciones
    app = QApplication(sys.argv)
    v = LanzarApp()
    v.show()
    # Se comienza el lazo de ejecución
    sys.exit(app.exec_()) # Da la orden de que se ejecute


if __name__ == '__main__':
    main()
    
#%%
import sys
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv) #Solo se hace un objeto app 
    
    # Vetana
    w = QtWidgets.QWidget()
    w.setGeometry(100,100,200,50)
    w.setWindowTitle('PyQt')
    
    # Etiqueta 
    # Esta etiqueta se añade a la interfaz
    b = QtWidgets.QLabel(w)
    b.setText('Hola mundo!')
    b.move(50,20)
    
    #Cuando la ventana esta construida se muestra
    w.show()

    # Se comienza el lazo de ejecución
    sys.exit(app.exec_()) # Da 