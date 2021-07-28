#%% CONTROLADOR
import random 
import numpy as np
class Jugador:
    def __init__(self):
        self.__usuario = ''
        self.__documento = 0
        
    def getUsuario(self):
        return self.__usuario
    def getDocumento(self):
        return self.__documento
    
    def setUsuario(self, u):
        self.__usuario = u
    def setDocumento(self, d):
        self.__documento = d
        
class Sistema:
    def __init__(self):
        self.__jugador = {}
        self.real_ans = random.randint(1000,9999)
        self.contador = 0
        self.array = np.random.randint(10, size=(3, 3))
        
        
    def verificarExistencia(self, d):
        return d in self.__jugador
    
    def recibirInfoLogin(self, u, d):
        j = Jugador()
        j.setUsuario(u)
        j.setDocumento(d)
        self.__jugador[j.getDocumento()] = j
    
    def verif_num(self, list1, list2, n):
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                num_ok = list1[i]
                return(f'{n}: Numero {num_ok} esta correcto' + '\n')
            else:
                return('Numero incorrecto')
            
    def guessing(self, n):
        list_numgen = [int(d) for d in str(self.real_ans)]
        print(list_numgen)
        salir = True
        while salir:
            list_op_user = [int(d) for d in str(n)]
            if int(n) == int(self.real_ans):
                self.contador += 1
                return[(f'Ganaste con {self.contador} intento(s)')]
            else:
                self.contador += 1
                advert = self.verif_num(list_numgen, list_op_user, n)
                return[(f'Llevas {self.contador} intentos, sigue adelante'), advert]
            
            
    def matrix(self):
        print(self.array)
        return self.array
    
    def match_review(self, num):
        result = np.where(self.matrix() == num)
        return result

    # %%
