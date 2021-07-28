import random

numgen = random.randint(1000,9999)
salir = True
contador = 0

while salir:
    op_user = int(input(f'Ingrese numero de 4 digitos: '))
    if op_user == numgen:
        contador += 1
        print(f'Ganaste con {contador} intento(s)')
        res = input('¿Deseas seguir jugando?S/N: ')
        if res == 'S' or res =='s':
            numgen = numgen
            continue
        elif res =='N' or res =='n':  
            salir = False
            continue
        else:
            print('Respuesta invalida, regresa pronto')
            break
    else:
        contador += 1
        print(f'Llevas {contador} intentos, sigue adelante')
        if op_user > numgen:
            print(f'Tu numero {op_user} esta por encima' + '\n')
        else:
            print(f'Tu numero {op_user} esta por debajo' + '\n')
print('Fin del programa')