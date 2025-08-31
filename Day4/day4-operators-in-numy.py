#working with operator in numpy
import numpy as np

arrOne = np.array([1,2,3])
arrSecond = np.array([4,16,9])
print(f'{arrOne + arrSecond}sayıların toplamı')
print(f'{arrOne * arrSecond}sayıların carpımı')
print(f'{arrOne / arrSecond}sayıların bolumu')

print(f'{np.sqrt(arrSecond)} sayıların kökü')

print(np.mean(arrOne)) # ortadaki sayı
print(np.sum(arrOne)) # Sum sayıların toplamı
print(np.max(arrOne)) # sayıların en buyugu 

a = np.arange(1,4)
b= np.arange(3,6)
print(a-b)
print(a)