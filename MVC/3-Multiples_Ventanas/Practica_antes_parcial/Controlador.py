from PyQt5.QtWidgets import QApplication
import sys
from Vista import Ventana

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    mi_ventana = Ventana()
    mi_ventana.show()
    
    sys.exit(app.exec_())