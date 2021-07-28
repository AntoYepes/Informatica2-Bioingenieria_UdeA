import numpy as np
# 1st argument --> numbers ranging from 0 to 9, 
# 2nd argument, row = 2, col = 3
array = np.random.randint(10, size=(3, 3))
print(array)
print(array[0,0])

result = np.where(array == array[0,0])
print(result)