from PyQt5.QtWidgets import QApplication
import sys
from VISTA1 import Ventana_botones

# codigo cliente, para ejecutar todo el programa
if __name__ == '__main__':
    # correr esta ventana
    app = QApplication(sys.argv)
    
    # creo la vista
    mi_ventana_inicio = Ventana_botones()
    mi_ventana_inicio.show()
    
    sys.exit(app.exec_())