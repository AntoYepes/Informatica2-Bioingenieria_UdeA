import numpy as np
import random
from random import sample
# 1st argument --> numbers ranging from 0 to 9, 
# 2nd argument, row = 2, col = 3
# array = np.random.randint(10, size=(3, 3))
# print(array)
# print(array[0,0])

# lista = range(0,10)
# print(sample(lista,k=5))

def func_guess_matrix():
    lx = [3, 4, 5, 7, 0]
    lx = ([val for val in lx for _ in (0, 1)])
    random.shuffle(lx)
    return [lx[i:i+3] for i in range(0, 9, 3)]
print(func_guess_matrix())
