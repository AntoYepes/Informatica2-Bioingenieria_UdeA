# PRACTICA EN CLASE No-9
import sys
from PyQt5 import QtWidgets

def main():
    # Manejo del flujo principal, con los eventos e interacciones
    app = QtWidgets.QApplication((sys.argv))

    # Ventana
    w = QtWidgets.QWidget()
    w.setGeometry(100, 100, 200, 50)
    w.setWindowTitle('PyQt')

    # Etiqueta
    # Esta etiqueta se añade a la interfaz
    b = QtWidgets.QLabel(w)
    b.setText('Hola')
    b.move(50,20) # x= 50  y= 20

    # Cuando se tiene la ventana construida se muestra
    w.show()

    # Se comienza el lazo de la ejecucion
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


#%%
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class LanzarApp(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('Ejemplo_GUI_1.ui', self)

def main():
    app = QApplication(sys.argv)
    v = LanzarApp()
    v.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

#%%
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self):
       super(Ui, self).__init()
       uic.loadUi('Ejemplo_GUI_1.ui', self)
       self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

#%%
import sys
from PyQt5 import QtGui, uic, QtWidgets

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Ejemplo_GUI_1.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())


