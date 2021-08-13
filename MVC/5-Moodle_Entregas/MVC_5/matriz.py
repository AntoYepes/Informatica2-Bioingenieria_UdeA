import numpy as np
import random
from random import sample

# def func_guess_matrix():
#     lx = [3, 4, 5, 7, 0]
#     lx = ([val for val in lx for _ in (0, 1)])
#     random.shuffle(lx)
#     return [lx[i:i+3] for i in range(0, 9, 3)]
# print(func_guess_matrix())

matches = [['/img/fb.png', '/img/insta.png', '/img/tkt.png'],['/img/wtsp.png', '/img/x.png', '/img/fb.png'], ['/img/insta.png', '/img/tkt.png', '/img/wtsp.png']]
random.shuffle(matches)
print(matches)

count = 0
answer_list = []
answer_dict = {}

def button_click(boton, number):
    global count, answer_list, answer_dict
    
    if boton['text'] == ' ' and count < 2:
        boton['text'] == matches[number]
        # Agregamos el numero a la lista
        answer_list.append(number)
        # Agregamos boton y numero al dict
        answer_dict[boton] = matches[number] # {b1:fb, 24:tkt}
        # Incrementamos el contador
        count += 1
        
        
    