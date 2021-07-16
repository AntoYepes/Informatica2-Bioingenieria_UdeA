# INTERFAZ 1.3
# Crear una interfaz Widget
# 1- Importamos
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi

# Creamos la clase
class lanzarVentana(QWidget):
    # Constructor
    def __init__(self):
        # super herencia
        super().__init__()
        # loadui
        loadUi('interfaz1.3.ui', self)
        
# main
def main():
    # cramos objeto app
    app = QApplication(sys.argv)
    # creamos objeto ventana
    v = lanzarVentana()
    # Show
    v.show()
    # Enlazar y ejecutar
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
