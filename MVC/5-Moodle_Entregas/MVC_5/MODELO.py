#%% CONTROLADOR
import random 
import numpy as np
import time
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
        # Atributos para juego 1
        self.__jugador = {}
        self.real_ans = random.randint(1000,9999)
        self.contador = 0
        self.array = np.random.randint(10, size=(3, 3))
        # Atributos para juego 2 
        # self.matriz = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
        self.matriz = [['1','1','2'],['2','3','3'],['4','4','0']]
        random.shuffle(self.matriz)
        self.lista_valores = [] # Guardamos las parejas de coord
        self.lista_posic_encontradas = [] # Guardamos todas las coord que el usuario ok
    
    def verificarExistencia(self, d):
        return d in self.__jugador
    
    def recibirInfoLogin(self, u, d):
        j = Jugador()
        j.setUsuario(u)
        j.setDocumento(d)
        self.__jugador[j.getDocumento()] = j
    
    def verif_num(self, list1, list2, n):
        self.num_ok = []
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                self.num_ok.append(str(list1[i]))
                
        print(self.num_ok)
        list_ok = ','.join(self.num_ok)
        if len(list_ok) > 0:
            return(f'{n}: Acertaste en: {list_ok}' + '\n')
        else:
            return('Incorrecto')
            
    def guessing(self, n):
        list_numgen = [int(d) for d in str(self.real_ans)]
        list_op_user = [int(d) for d in str(n)]
        print(list_numgen)
        salir = True
        
        while salir:
            if int(n) == int(self.real_ans):
                self.contador += 1
                return[(f'Ganaste con {self.contador} intento(s)')]
            else:
                self.contador += 1
                advert = self.verif_num(list_numgen, list_op_user, n)
                return[(f'Llevas {self.contador} intentos, sigue adelante'), advert]
                        
    def actualizar_matriz(self, positionx, positiony):
        self.matriz[positionx][positiony] = '-'
    
    def reiniciar_matriz(self):
        self.lista_valores = []
        # self.lista_valores = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
    
    def obtener_valor_matriz(self, positionx, positiony):
        return self.matriz[positionx][positiony]
    
    def validar_parejas(self):
        v1 = self.lista_valores[0]
        v2 = self.lista_valores[1]
        return self.matriz[v1[0]][v1[1]] == self.matriz[v2[0]][v2[1]]
    
    def agregar_valores_lista(self, positionx, positiony):
        self.lista_valores.append([positionx, positiony])
        
    def tamano_lista(self):
        return len(self.lista_valores)
    
    def agregar_posic_encontradas(self, valor): #valor es lista con una posicion
        self.lista_posic_encontradas.append(valor)

    def tamano_posic_encontradas(self):
        return len(self.lista_posic_encontradas)
        
    def reiniciar_posic_encontradas(self):
        self.lista_posic_encontradas = []
        
    def devolver_coord(self, position):
        return self.lista_valores[position]

    def validacion_boton_press(self, coordx, coordy):
        return [coordx, coordy] in self.lista_posic_encontradas 

    # %%
