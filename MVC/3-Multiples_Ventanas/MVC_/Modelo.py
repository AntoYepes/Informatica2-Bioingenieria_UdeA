class Medicamento():
    def __init__(self):
        self.__nombre = ''
        self.__dosis = 0
        self.__servicio = ''
    
    def AsignarNombre(self, n):
        self.__nombre = n
        
    def AsignarDosis(self, a):
        self.__dosis = a
        
    def VerNombre(self):
        return self.__nombre
    
    def VerDosis(self):
        return self.__dosis
    
class Paciente():
    def __init__(self):
        self.__nombre = ''
        self.__cedula = 0
        self.__medicamentos = {}
        
    def AsignarNombre(self, n):
        self.__nombre = n
        
    def AsignarCedula(self, c):
        self.__cedula = c
    
    def TieneMedicamento(self, nombre):
        return nombre.lower() in self.__medicamentos
    
    def AsignarMedicamentos(self, medicamentos):
        self.__medicamentos = medicamentos
        
    def AsignarMedicamento(self, m):
        self.__medicamentos[m.VerNombre().lower] = m
        
    def VerNombre(self):
        return self.__nombre
    
    def VerCedula(self):
        return self.__cedula
    
class Servicio():
    def __init__(self):
        self.__pacientes = {}
        
    def AgregarPaciente(self, n, c, medicamentos):
        p = Paciente()
        p.AsignarNombre(n)
        p.AsignarCedula(c)
        p.AsignarMedicamentos(medicamentos)
        self.__pacientes[c] = p
        
    def VerficarPacinte(self, c):
        return c in self.__pacientes
        
    def AgregarMedicament(self, c, nm, dm):
        m = Medicamento()
        m.AsignarNombre(nm)
        m.AsignarDosis(dm)
        
        paciente = self.__pacientes[c]
        paciente.AsignarMedicamento(m)
        self.__pacientes[c] = paciente
        
    def VerificarMedicamento(self, c, nm):
        paciente = self.__pacientes[c]
        return paciente.TieneMedicamento(nm)
    