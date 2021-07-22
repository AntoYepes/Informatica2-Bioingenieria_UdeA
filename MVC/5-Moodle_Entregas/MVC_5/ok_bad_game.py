import random
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
                print("You Guess!!!")    
                
def game_on(num1):
    ok, bad = 0,0
    num2 = ask_user()
    while(1):
        if(num1==num2):
            ok+=1
            print("right guess:", ok, "   ", "wrong guess:", bad)
            print("You guessed correctly..GameOver")
            break
        else:
            bad+=1
            print("right guess:",ok,"   ","wrong guess:",bad)
            num2=ask_user()
            if bad>9:
                break
            else:
                continue

print("Welcome!!!!")
numgen=num_gen()
game_on(numgen)