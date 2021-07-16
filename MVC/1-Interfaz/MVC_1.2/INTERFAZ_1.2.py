# INTERFAZ 1.2
# Crear interfaz MainWindow

# 1- Importamos
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

# 2- Se crea la clase
class lanzarVentana(QMainWindow):
    # Constructor
    def __init__(self):
        # super herencia
        super().__init__()
        # loadui
        loadUi('interfaz1.2.ui', self)
        
# Main
def main():
    # Objeto app
    app = QApplication(sys.argv)
    # Objeto ventana
    v = lanzarVentana()
    # Show para mostrar
    v.show()
    # Enlazar y ejecutar
    sys.exit(app.exec_()) 
    
if __name__ == '__main__':
    main()