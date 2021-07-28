import random

# funcion
def verif_num(list1, list2, num):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            num_ok = list1[i]
            return(f'{num}: Numero {num_ok} esta correcto')
        else:
            print('Numero incorrect')

            
numgen = random.randint(1000,9999)
print(numgen)
list_numgen = [int(d) for d in str(numgen)]
salir = True
contador = 0
while salir:
    op_user = int(input(f'Ingrese numero de 4 digitos: ' + '\n'))
    list_op_user = [int(d) for d in str(op_user)]
    if op_user == numgen:
        contador += 1
        print(f'Ganaste con {contador} intento(s)')
        
    else:
        contador += 1
        print(f'Llevas {contador} intentos, sigue adelante')
        verif_num(list_numgen, list_op_user, op_user)
        
