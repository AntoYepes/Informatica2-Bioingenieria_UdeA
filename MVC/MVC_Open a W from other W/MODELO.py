#%% CONTROLADOR
import random as r

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
        self.real_ans = str(r.randrange(1000,100000,2))
        
    def verificarExistencia(self, d):
        return d in self.__jugador
    
    def recibirInfoLogin(self, u, d):
        j = Jugador()
        j.setUsuario(u)
        j.setDocumento(d)
        self.__jugador[j.getDocumento()] = j
        
    def evaluate(self, n):
        correct = 0
        for i in range(4):
            if n[i] == self.real_ans[i]:
                correct += 1
        return correct 

    def guessing(self, n):
        while True:
            correct = self.evaluate(n)
            if not correct == 4:
                return(str(correct)," was correct")
            else:
                return("You guessed it! ")
    
# %%
