
num1 = [1, 2, 3, 4]
num2 = [1, 9, 3, 8]
list_num1 = [int(d) for d in str(num1)] # num aleatorio
list_num2 = [int(d) for d in str(num2)] # num 
#%%
list1 = [1, 2, 3, 4]
list2 = [1, 9, 3, 8]

def verif_num(list1, list2):
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            num_ok = list1[i]
            print(str(num_ok) + " correcto")
            


#%%
import numpy

a = numpy.array([0, 1, 2, 9])
b = numpy.array([6, 1, 4, 7])
result = numpy.where(a==b)
print(result)
# %%
import numpy as np

a = numpy.array([0, 1, 2, 9])
b = numpy.array([6, 1, 4, 7])

print("Array a: ", a)
print("Array b: ", b)

print("a > b")
print(np.greater(a, b))

print("a >= b")
print(np.greater_equal(a, b))

print("a < b")
print(np.less(a, b))

print("a <= b")
print(np.less_equal(a, b))
# %%

# init arrays
a = [3, 1, 2, 9]
b = [3, 6, 2, 7]
#using enumerate, list comprehension and set
result = [key for key, val in enumerate(a) if val in set(b)]
# reslt = ' '.join(result) 
for i in range(len(result)):
    print('Numero en posicion ' + str(result[i]) + ' es correcto')

# %%
