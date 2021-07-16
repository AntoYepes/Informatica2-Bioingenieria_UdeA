#INTERFAZ No-2
# Crear una interfaz con QDdialog with button bottons
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

# Creo la clase de lanzamiento
class lanzarVentana(QDialog):
    # Constructor
    def __init__(self):
        # super de herencia
        super().__init__()
        # usamos loadUi 
        loadUi('interfaz1.1.ui', self)
        
# funcion main
def main():
    # Creamos el objeto app para el manejo del flujo usamos QApplication
    app = QApplication(sys.argv)
    # Creamos objeto ventana 
    v = lanzarVentana()
    # Show para mostrar
    v.show()
    # Se inicia el lazo de ejecucion
    sys.exit(app.exec_()) # Da la orden de que se ejecute
    

if __name__ == '__main__':
    main()