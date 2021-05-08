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
    
    