#Advanced Numpy operations

import numpy as np
#Array and scalar broadcasting 
arr = np.array([[5,6,3],[1,2,4],[2 ,4,5]])
print('Added 12 to each number in matrix \n',arr + 12)  # Add 12 to each number in matrix

vector = np.array([1,0,3]) 

print('This vector added this vector[1,0,1] \n', arr + vector) # add this array in every number in matrix

print('Matrixin orjinali \n',arr)
print('Mean ',np.mean(arr))  # Mean : sayı ortalaması
print('Sum',np.sum(arr))  #Sum: matrix toplamı
print('Standart Devition',np.std(arr))  # Standart devition(sapma)
print('Min',np.min(arr)) # Min sayı
print('Max',np.max(arr)) # Max sayı 
print('Rows Sum',np.sum(arr , axis=1)) # Satır toplamı
print('Columns Sum',np.sum(arr, axis=0)) # Sutun Toplamı

