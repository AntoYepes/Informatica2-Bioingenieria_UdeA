# EJEMPLO 2 MVC
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from MODELO import Medicamento
from PyQt5.QtGui import QIntValidator

class ventanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(ventanaPrincipal, self).__init__(ppal)
        loadUi('ventana_principal.ui', self)
        self.setup()
        
    def setup(self):
        self.boton_ingresar.clicked.connect(self.abrir_ventana_paciente)
    
    def recibirPaciente(self, nombre, cedula, medicamentos):
        resultado = self.__mi_coordinador.recibirInfoPaciente(nombre, cedula, medicamentos)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(resultado)
        msg.setWindowTitle('Resultado de la operacion: ')
        msg.show()
        
    def abrir_ventana_paciente(self):
        ventana_paciente = ventanaPaciente(self)
        self.hide()
        ventana_paciente.show()
        
class ventanaPaciente(QDialog):
    def __init__(self, ppal = None):
        super(ventanaPaciente, self).__init__(ppal)
        loadUi('ventana_paciente.ui', self)
        self.__medicamentos_paciente_actual = {}
        self.setup()
        
    def setup(self):
        self.boton_agregar.clicked.connect(self.abrir_ventana_medicamento)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def recibirMedicamentos(self, medicamentos):
        self.__medicamentos_paciente_actual = medicamentos
        
    def opcion_aceptar(self):
        # 1- se recuperan los campos
        nombre = self.campo_nombre.text()
        cedula = self.campo_cedula.text()
        
        # 2- se envia la informacion al campo principal
        self.__mi_ventana_principal.recibir_paciente(nombre, cedula, self.__medicamentos_paciente_actual)
        # 3- se muestra la ventana pricipal y se oculta la actual
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
    def __init__(self, ppal = None):
        super(ventanaMedicamento, self).__init__(ppal)
        loadUi('ventana_medicamento.ui', self)
        self.__medicamentos = {}
        self.__mi_ventana_principal = ppal
        self.setup()
        
    def setup(self):
        self.boton_agregar.clicked.connect(self.recuperar_info_medicamento)
        soloEntero = QIntValidator()
        self.campo_dosis.setValidator(soloEntero)
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def recuperar_info_medicamento(self):
        # 1- se recuperan los campos
        nombre = self.campo_nombre.text()
        dosis = self.campo_dosis.text()
        #2- si el medicamento no esta se guarda
        if nombre.lower() not in self.__medicamentos:
            m = Medicamento()
            m.setNombre(nombre)
            m.setdosis(dosis)
            self.__medicamentos[nombre.lower()] = m
            mensaje = 'Guardado con exito'
        else:
            mensaje = 'Ya se habia asignado el medicamento'
            
        #3- se muestra el resultado de la operacion que esta en la variable mensaje
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle('Resultado de la operacion: ')
        msg.show()
        
        #6- se vuelven a poner en blanco los campos
        self.campo_nombre.setText('')
        self.campo_dosis.setText('')
        
    def opcion_aceptar(self):
        self.__mi_ventana_principal.recibir_medicamentos(self.__medicamentos)
        self.__mi_ventana_principal.show()
        self.hide()
        
    def opcion_cancelar(self):
        m = {}
        self.__mi_ventana_principal.recibir_medicamentos(m)
        self.__mi_ventana_principal.show()
        self.hide()
        
        
def main():
    app =  QApplication(sys.argv)
    mi_ventana = ventanaMedicamento()
    mi_ventana.show()
    sys.exit(app.exec_())
    
        
            
        