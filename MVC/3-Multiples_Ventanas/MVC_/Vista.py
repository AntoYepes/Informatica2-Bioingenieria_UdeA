import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator
from Modelo import Medicamento

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal=None):
        super(VentanaPrincipal, self).__init__(ppal)
        loadUi('ventana_principal.ui', self)
        self.setup()
        
    def setup(self):
        self.boton_ingresar.clicked.connect(self.abrir_ventana_paciente)
        
    def abrir_ventana_paciente(self):
        ventana_paciente = ventanaPaciente(self)
        self.hide()
        ventana_paciente.show()
        
class ventanaPaciente():
    def __init__(self, ppal=None):
        super(ventanaPaciente, self).__init__(ppal)
        loadUi('ventana_paciente.ui', self)
        self.__mi_ventana_principal = ppal
        self.__medicamentos_paciente_actual = {}
        self.setup()
        
    def setup(self):
        self.boton_agregar.clicked.connect(self.abrir_ventana_medicamento)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.occion_cancelar)
        
    def recibir_medicamentos(self, medicamentos):
        self.__medicamentos_paciente_actual = medicamentos
        
    def opcion_aceptar(self):
        nombre = self.campo_nombre.text()
        cedula = self.campo_cedula.text()
        
        self.__mi_ventana_principal.recibir_paciente(nombre, cedula, self.__medicamentos_paciente_actual)
        self.__mi_ventana_principal.show()
        self.hide()
    
    def opcion_cancelar(self):
        self.__mi_ventana_principal.show()
        self.hide()
        
    def abrir_ventana_medicamento(self):
        ventana_medicamento = ventanaMedicamento(self)
        self.hide()
        ventana_medicamento.show()
        
class ventanaMedicamento(QDialog):
    def __init__(self, ppal=None):
        super(ventanaMedicamento, self).__init__(ppal)
        loadUi('ventana_medicamento.ui', self)
        self.__mi_ventana_principal = ppal
        self.setup()
        
    def setup(self):
        self.boton_agregar.clicked.connect(self.recuperar_info_medicamento)    
        
        soloEntero = QIntValidator()
        self.campo_dosis.setValidator(soloEntero)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def recuperar_info_medicamento(self):
        nombre = self.campo_nombre.text()
        dosis = int(self.campo_dosis.text())
        
        if nombre.lower() not in self.__medicamentos:
            m = Medicamento()
            m.AsignarNombre(nombre)
            m.AsignarDosis(dosis)
            self.__medicamentos[nombre.lower()] = m
            mensaje ='Guardado con exito'
        else:
            mensaje = 'Ya se habia asignado el medicamento'
            
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle('Resultado de operacion')
        msg.show()
        self.campo_nombre.setText('')
        self.campo_dosis.setText('')

app = QApplication(sys.argv)
mi_ventana = ventanaMedicamento()
mi_ventana.show()
sys.exit(app.exec_())        
        