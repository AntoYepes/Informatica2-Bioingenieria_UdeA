from PyQt5.QtWidgets import QApplication
import sys
from VISTA import Ventana

# codigo cliente, para ejecutar todo el programa
if __name__ == '__main__':
    # correr esta ventana
    app = QApplication(sys.argv)
    
    # creo la vista
    mi_ventana_inicio = Ventana()
    mi_ventana_inicio.show()
    
    sys.exit(app.exec_())