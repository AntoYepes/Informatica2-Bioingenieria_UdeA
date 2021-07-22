import math
import random
def generar_numero_aleatorio(inicio,fin):
    valorInicial = int(random.random()*fin) 
    numero = valorInicial if valorInicial >= inicio else valorInicial + inicio
    return numero
start = 1
end = 9999
numgen = generar_numero_aleatorio(start, end)
salir = True
contador = 0
while salir:
    op_user=int(input(f'Ingrese un valor entre {start}  y {end}: '))
    if op_user == numgen:
        contador += 1
        print(f'Ganaste con {contador} intento(s)')
        res = input('¿Deseas seguir jugando?S/N: ')
        if res == 'S' or res =='s':
            numgen = generar_numero_aleatorio(start,end)
            continue
        elif res =='N' or res =='n':  
            salir = False
            continue
        else:
            print('Respuesta invalida, regresa pronto')
            break
    else:
        contador += 1
        print(f'Fallaste llevas {contador} intentos, sigue adelante')
        if op_user > numgen:
            print('Ingresaste valor por encima,vuelve a intentar' + '\n')
        else:
            print('Ingresaste valor por debajo,vuelve a intentar' + '\n')
print('Fin del programa')