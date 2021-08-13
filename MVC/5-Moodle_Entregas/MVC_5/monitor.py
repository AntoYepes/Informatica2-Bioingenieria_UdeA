import time
import numpy as np 
import random 

class Match():
    '''===================Inicializacion=================='''
    def __init__(self): # constructor de inicializacion
        self.Letras='QWEASDZXC' # letras del teclado para interactuar 
        self.__posiciones={} # diccionario 
        self.arrayparejas=np.array([['!','#','#'],['!','*','$'],['$','%','%']]) 
        # matriz que se le mostrara al usuario 
        self.array=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
        self.__IncializarValores()
        self.aciertos=0 # con este se cuenta el numero de aciertos

    def __IncializarValores(self):
        #______________Se inicializa self.posisiones_________________________
        c=0 # contador
        for m in range(3): # se crea una lista con todas las posciones de la
            # matriz y se les asocia a una letra
            for n in range(3):  
                self.__posiciones[self.Letras[c]]=[m,n]
                c+=1
        # se____ incializa aletoreamente las parejas de caracteres en la matriz 
        np.random.shuffle(self.arrayparejas)
        print(self.array)
    '''====================INTERACCION CON EL JUGADOR======================='''
    def UsuarioInteractua(self):
        letra=input("====Haga su 1er jugada====\n")   #! TRAER EL VALOR DEL BOTON     
        a,b=self.__posiciones[letra][0],self.__posiciones[letra][1]
        self.array[a,b]=self.arrayparejas[a,b] # Se guarda el primer movimiento 
        print(self.array)
        letra=input("====Haga su 2da jugada====\n")
        c,d=self.__posiciones[letra][0],self.__posiciones[letra][1]
        self.array[c,d]=self.arrayparejas[c,d] # Se guarda el segundo movimiento
        print(self.array)

        if (self.arrayparejas[a,b]!=self.arrayparejas[c,d]):
            self.__RestaurarMatriz(a,b,c,d) # si no se encuentra la pareja 
                                    # se restaura la matriz 
        else: 
            self.aciertos+=1
        time.sleep(1)
        print(30*"\n"+"====INTENTE DE NUEVO===")
        print(self.array)
    def __RestaurarMatriz(self,a,b,c,d):
        self.array[a,b]='-'
        self.array[c,d]='-'

print("======BIENVENIDO=======")
# Crear matriz 3X3
Juego1=Match()
Win=False
while not(Win): 
    Juego1.UsuarioInteractua()
    print(" #Aciertos:"+str(Juego1.aciertos))
    if Juego1.aciertos==4:
        Win=True # Cuando tenga 4 aciertos es porque el jugador gano
print("=====GANASTE==============")

#%%
# def __IncializarValores(self):
#         #______________Se inicializa self.posisiones_________________________
#         c = 0 # contador
#         for m in range(3): # se crea una lista con todas las posciones de la
#             # matriz y se les asocia a una letra
#             for n in range(3):  
#                 self.__posiciones[self.letras[c]] = [m,n]
#                 c += 1
#         # se____ incializa aletoreamente las parejas de caracteres en la matriz 
#         np.random.shuffle(self.arrayparejas)
#         print(self.array)
#         return(self.array)
    
#     def UsuarioInteractua(self, boton1 = None, boton2 = None):
#         self.boton_1 = boton1
#         a,b = self.__posiciones[self.boton_1][0], self.__posiciones[self.boton_1][1]
#         self.array[a,b] = self.arrayparejas[a,b] # Se guarda el primer movimiento 
#         return self.array
#         self.boton_2 = boton2
#         c,d = self.__posiciones[self.boton_2][0], self.__posiciones[self.boton_2][1]
#         self.array[c,d] = self.arrayparejas[c,d] # Se guarda el segundo movimiento
#         return self.array

#         if (self.arrayparejas[a,b] != self.arrayparejas[c,d]):
#             self.__RestaurarMatriz(a,b,c,d) # si no se encuentra la pareja 
#         # se restaura la matriz 
#         else: 
#             self.aciertos += 1
#         time.sleep(1)
#         return self.array
    
    #  self.letras = 'n1n2n3n4n5n6n7n8n9'
    #     self.__posiciones = {} # diccionario 
    #     self.arrayparejas = np.array([['fb.png', 'insta.png', 'wtsp.png'],['tkt.png', 'fb.png', 'insta.png'],['wtsp.png', 'tkt.png', 'x.png']]) 
    #     # matriz que se le mostrara al usuario 
    #     self.array = np.array([['pregunta.png', 'pregunta.png', 'pregunta.png'],['pregunta.png', 'pregunta.png', 'pregunta.png'],['pregunta.png', 'pregunta.png', 'pregunta.png']])
    #     self.__IncializarValores()
    #     self.aciertos = 0 # con este se cuenta el numero de aciertos
    # def __RestaurarMatriz(self,a,b,c,d):
    #     self.array[a,b]='x'
    #     self.array[c,d]='x'
        
    # def matrix(self):
    #     # Crear matriz 3X3
    #     Juego2 = Sistema()
    #     Win = False
    #     while not(Win): 
    #         Juego2.UsuarioInteractua()
    #         aciertos = (" # Aciertos:" + str(Juego2.aciertos))
    #         if Juego2.aciertos == 4:
    #             Win = True # Cuando tenga 4 aciertos es porque el jugador gano
    #     return[aciertos, "==============GANASTE=============="]
