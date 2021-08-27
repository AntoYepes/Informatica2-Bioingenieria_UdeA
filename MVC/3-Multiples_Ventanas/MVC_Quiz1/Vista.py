import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt, QRegExp

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal = None):
        super(VentanaPrincipal, self).__init__(ppal)
        loadUi('VentanaPrincipal.ui', self)
        self.setup()
        
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c
        
    def setup(self):
        self.boton_nueva_protesis.clicked.connect(self.opcion_nueva_protesis)
        self.boton_buscar.clicked.connect(self.opcion_buscar)
        self.boton_borrar.clicked.connect(self.opcion_borrar)
        self.boton_editar.clicked.connect(self.opcion_editar)
        self.boton_guardar.clicked.connect(self.opcion_guardar)
        self.boton_salir.clicked.connect(self.opcion_salir)
        
    def opcion_nueva_protesis(self):
        nueva_protesis = NuevaProtesis(self)
        nueva_protesis.setControlador(self.__mi_coordinador)
        self.hide()
        nueva_protesis.show()
        
    def opcion_buscar(self):
        buscar_protesis = BuscarProtesis(self)
        buscar_protesis.setControlador(self.__mi_coordinador)
        self.hide()
        buscar_protesis.show()
        
    def opcion_borrar(self):
        borrar_protesis = BorrarProtesis(self)
        borrar_protesis.setControlador(self.__mi_coordinador)
        self.hide()
        borrar_protesis.show()
        
    def opcion_editar(self):
        editar_protesis = EditarProtesis(self)
        editar_protesis.setControlador(self.__mi_coordinador)
        self.hide()
        editar_protesis.show()
        
    def opcion_guardar(self):
        guardar_protesis = GuardarProtesis(self)
        guardar_protesis.setControlador(self.__mi_coordinador)
        self.hide()
        guardar_protesis.show()
        
    def opcion_salir(self):
        self.close()
        
class NuevaProtesis(QDialog):
    def __init__(self, ppal = None):
        super(NuevaProtesis, self).__init__(ppal)
        loadUi('TipoProtesis.ui', self)
        self.ventana_padre = ppal
        self.setup()
    
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c  
        
    def setup(self):
        self.campo_ref.setValidator(QIntValidator())
        self.boton_aceptar.clicked.connect(self.opcion_aceptar)

    def opcion_aceptar(self):
        no_ref = self.campo_ref.text()
        tipo_protesis = self.comboBox.currentText()
        # info = self.__mi_coordinador.registroPro(no_ref, tipo_protesis) # esto me trae una lista [0, 1]
        # QMessageBox.information(self, 'Informacion', str(info), QMessageBox.Ok)
        if tipo_protesis == 'Pasiva':
            protesis_pasiva = ProtesisPasiva(self)
            protesis_pasiva.setControlador(self.__mi_coordinador)
            self.hide()
            protesis_pasiva.show()
        elif tipo_protesis == 'Mecanica':
            protesis_mecanica = ProtesisMecanica(self)
            protesis_mecanica.setControlador(self.__mi_coordinador)
            self.hide()
            protesis_mecanica.show()
        elif tipo_protesis == 'Electrica':
            protesis_electrica = ProtesisElectrica(self)
            protesis_electrica.setControlador(self.__mi_coordinador)
            self.hide()
            protesis_electrica.show()
        elif tipo_protesis == 'Mioelectrica':
            protesis_mio = ProtesisMio(self)
            protesis_mio.setControlador(self.__mi_coordinador)
            self.hide()
            protesis_mio.show()
        return[no_ref, tipo_protesis]
    
    def infoPasiva(self, nombre, cubrimiento, zona):
        no_ref = NuevaProtesis.opcion_aceptar(self)[0]
        tipo_prot = NuevaProtesis.opcion_aceptar(self)[1]
        info = self.__mi_coordinador.infoPasiva(no_ref, tipo_prot, nombre, cubrimiento, zona)
        QMessageBox.information(self, 'Informacion', str(info), QMessageBox.Ok)
        self.hide()
        
    def infoMecanica(self, nombre, cubrimiento, zona, accionamiento, material, sujecion):
        no_ref = NuevaProtesis.opcion_aceptar(self)[0]
        tipo_prot = NuevaProtesis.opcion_aceptar(self)[1]  
        info = self.__mi_coordinador.infoMecanica(no_ref, tipo_prot, nombre, cubrimiento, zona, accionamiento, material, sujecion)
        QMessageBox.information(self, 'Informacion', str(info), QMessageBox.Ok)
        self.hide()
        
    def opcion_cancelar(self): # que me muestre la ventana principal
        self.hide()
        self.ventana_padre.show()
        
class ProtesisPasiva(QDialog):
    def __init__(self, ppal = None):
        super(ProtesisPasiva, self).__init__(ppal)
        loadUi('ProtesisPasiva.ui', self)
        self.ventana_padre = ppal
        self.setup()
    
    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c 
        
    def setup(self):
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_cubrimiento.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_zona.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        nombre = self.campo_nombre.text()
        cubrimiento = self.campo_cubrimiento.text()
        zona = self.campo_zona.text()
        self.ventana_padre.infoPasiva(nombre, cubrimiento, zona)
        #Nos vamos para el menu inicial
        ventanappal = VentanaPrincipal(self)
        ventanappal.setControlador(self.__mi_coordinador)
        self.hide()
        ventanappal.show()
    
        
    def opcion_cancelar(self):
        self.hide()
        self.ventana_padre.show()
    
class ProtesisMecanica(QDialog):
    def __init__(self, ppal = None):
        super(ProtesisMecanica, self).__init__(ppal)
        loadUi('ProtesisMecanica.ui', self)
        self.ventana_padre = ppal
        self.setup()

    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c    
        
    def setup(self):
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_cubrimiento.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_zona.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_accionamiento.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_material.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_sujecion.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        nombre = self.campo_nombre.text()
        cubrimiento = self.campo_cubrimiento.text()
        zona = self.campo_zona.text()
        accionamiento = self.campo_accionamiento.text()
        material = self.campo_material.text()
        sujecion = self.campo_sujecion.text()
        self.ventana_padre.infoMecanica(nombre, cubrimiento, zona, accionamiento, material, sujecion)
        
        #Nos vamos para el menu inicial
        ventanappal_1 = VentanaPrincipal(self)
        ventanappal_1.setControlador(self.__mi_coordinador)
        self.hide()
        ventanappal_1.show()
    
    def opcion_cancelar(self):
        self.hide()
        self.ventana_padre.show()

class ProtesisElectrica(QDialog):
    def __init__(self, ppal = None):
        super(ProtesisElectrica, self).__init__(ppal)
        loadUi('ProtesisElectrica.ui', self)
        self.ventana_padre = ppal
        self.setup()

    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c    
        
    def setup(self):
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_cubrimiento.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_zona.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_tipomotor.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_cantmotor.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_hardware.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_software.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        nombre = self.campo_nombre.text()
        cubrimiento = self.campo_cubrimiento.text()
        zona = self.campo_zona.text()
        tipo_motor = self.campo_tipomotor.text()
        cant_motor = self.campo_cantmotor.text()
        hardware = self.campo_hardware.text()
        software = self.campo_software.text()
        self.__mi_coordinador.infoElectrica(nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software)
    
    def opcion_cancelar(self):
        self.hide()
        self.ventana_padre.show()

class ProtesisMio(QDialog):
    def __init__(self, ppal = None):
        super(ProtesisMio, self).__init__(ppal)
        loadUi('ProtesisMio.ui', self)
        self.ventana_padre = ppal
        self.setup()

    # Creamos el metodo setControlador para enlazarlo con el controlador
    def setControlador(self, c):
        self.__mi_coordinador = c    
        
    def setup(self):
        self.campo_nombre.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_cubrimiento.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_zona.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_tipomotor.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_cantmotor.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_hardware.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_software.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.campo_sensores.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_cancelar)
        
    def opcion_aceptar(self):
        nombre = self.campo_nombre.text()
        cubrimiento = self.campo_cubrimiento.text()
        zona = self.campo_zona.text()
        tipo_motor = self.campo_tipomotor.text()
        cant_motor = self.campo_cantmotor.text()
        hardware = self.campo_hardware.text()
        software = self.campo_software.text()
        sensores = self.campo_sensores.text()
        self.__mi_coordinador.infoElectrica(nombre, cubrimiento, zona, tipo_motor, cant_motor, hardware, software, sensores)
    
    def opcion_cancelar(self):
        self.hide()
        self.ventana_padre.show()

class BuscarProtesis(QDialog):
    pass

class BorrarProtesis(QDialog):
    pass

class  EditarProtesis(QDialog):
    pass

class GuardarProtesis(QDialog):
    pass

def main():
    app=QApplication(sys.argv)
    v= VentanaPrincipal()
    v.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()        