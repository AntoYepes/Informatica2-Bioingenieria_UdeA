#%%
import random as r

class Player():
    def __init__(self):
        self.real_ans = str(r.randrange(1000,100000,2))

    def guess(self):
        self.player_guess = input("Enter a guess")

    def evaluate(self):
        correct = 0
        for n in range(4):
            if self.player_guess[n] == self.real_ans[n]:
                correct += 1
        return correct 

    def run(self):
        while True:
            self.guess()
            correct = self.evaluate()
            if not correct == 4:
                print(str(correct)," was correct")
            else:
                print("You guessed it! ")
                break

Player().run()
    
    
# %% DIVINANZA NUMERO
import random
n = random.randint(1000,9999)
print(n)
guess = int(input("Enter a number 4 digits: "))
cont = 0
while n != "guess":
    if guess < n:
        cont += 1
        print("guess is low")
        print(str(cont) + 'intentos')
        guess = int(input("Enter a number 4 digits:  "))
    elif guess > n:
        cont += 1
        print("guess is high")
        print(str(cont) + 'intentos')
        guess = int(input("Enter a number 4 digist: "))
    else:
        print("you guessed it!")
        break

#%%
import random as r
real_ans = r.randrange(1000, 10000, 2)
real_ans_str = str(real_ans)
correct = 0
class Player():
    def __init__(self):
        self.player_guess = input("Enter a guess")
        self.evaluate(correct)
    def evaluate(self, correct):
        for n in range(4):
            if self.player_guess[n] == real_ans_str[n]:
                correct += 1
            else:
                print(str(correct)," was correct")
                correct = 0
                break
        if correct == 4:
            print("You guessed it! ")
            guessing = False
            

# %%
import random
def ask_user():
    user_ask1 = int(input("Adivina numero de 4 digits "))
    return (user_ask1)

def num_gen():
    num1 = random.randint(1000,9999)
    return num1