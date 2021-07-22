import random

def ask_user():
    user_ask1 = int(input("Adivina numero de 4 digitos!"))
    return (user_ask1)
def num_gen():
    num1=random.randint(1000,9999)
    return num1
def game_on(num1):
    ok, bad = 0,0
    num2 = ask_user()
    list_num1 = [int(d) for d in str(num1)] # num aleatorio
    list_num2 = [int(d) for d in str(num2)] # num guess
    print(list_num1)
    print(list_num2)
    while(1):
        y = 0
        # Output list intialisation
        Output = [] 
        
        # Using iteration to find
        for x in list_num1:
            if x != list_num2[y]:
                Output.append(y)
            y = y + 1
        
        # Printing output
        print(Output)
        if(num1==num2):
            ok+=1
            print("right guess:", ok, "   ", "wrong guess:", bad)
            print("You guessed correctly..GameOver")
            break
        else:
            bad += 1
            
            print("right guess:",ok,"   ","wrong guess:",bad)
            num2 = ask_user()
            if bad>50:
                break
            else:
                continue

print("Welcome!!!!")
numgen=num_gen()
game_on(numgen)

#%%
list1 = [1, 2, 3, 4]
list2 = [1, 9, 3, 8]

def verif_num(list1, list2):
    cont = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            cont += 1
            num_ok = list1[i]
            print(str(num_ok) + " correcto")
            if cont == 4:
                print("You Guess!!!")    
    return cont
func = verif_num(list1, list2)
print(func)

# %%
list1 = [9, 2, 7, 4]
list2 = [9, 2, 7, 4]

def verif_num(list1, list2):
    cont = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            cont += 1
            num_ok = list1[i]
            print(str(num_ok) + " correcto")
            if cont == 4:
                print("You Guess!!!")    
    
verif_num(list1, list2)

# %%
def ask_user():
    user_ask1=int(input("Adivina numero de 4 digits "))
    return (user_ask1)

def num_gen():
    num1 = random.randint(1000,9999)
    return num1

def verif_num(list1, list2):
    cont = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            cont += 1
            num_ok = list1[i]
            print(str(num_ok) + " correcto")
            if cont == 4:
                msg = "You Guess!!!"   
    
    return msg