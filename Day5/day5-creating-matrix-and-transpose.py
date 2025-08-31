#Day 5 understand the transpose and creating matrix wiith np.array

import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('ORIGINAL MATRİX \n',matrix)

#  .T changing the rows and columns
transpose = matrix.T
print('Transpose matrix\n',transpose)

matrixForToFor = np.array([[2,3,4,5],[3,4,5,6],[7,8,9,10],[11,12,13,14]])
print('Matrix 4X4 \n',matrixForToFor)

matrixForToForSecond = np.array([[2,7,4,5],[3,8,14,6],[7,8,14,10],[21,12,24,35]])
print('Matrix 4X4 Second \n',matrixForToForSecond)

print('Matrix 1 multiply Matrix 2 \n ' , matrixForToFor*matrixForToForSecond)

# create a program to normalize an array
