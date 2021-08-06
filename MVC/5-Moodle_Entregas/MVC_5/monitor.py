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


