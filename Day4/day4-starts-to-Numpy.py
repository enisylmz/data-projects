#NumPy: Numerical python

# What is Numpy :Numpy or numerical python is a foundational library in Python for numerical computatitions

# Why is numpy : provides fast large data sets ,Performance , Ease of use , Integration

#importing Numpy 

import numpy as np

#creating a list in numpy 

arr = np.array({1,2,3,4,5,6,7,8,9})
print(arr)

#using built functions for examples zeroes
#create zero variables 

zeroes = np.zeros((3,2))  # np.Zeros : created matrix from zeros,first number is line second number is column 
print(zeroes)

ones = np.ones((2,5))    # np.Ones: Created matrix from ones 
print(ones)


arrange = np.arange(1,10,1)  # first number is which number you will start second number is which number you will stop(but last number nor include and the last number what arrange will be
print(arrange)

linspace = np.linspace(1,3,7) # np.Linspace generates equally spaced numbers within a specified range in NumPy. first number is where will u start second number is where will u stop (last number is include) and last number is step count
print(linspace)

#reshaped the array
secondArr=np.array([1,2,3,4,5,6,7,8,9])
arrShaped= secondArr.reshape((3,3))
print(arrShaped)

thirdArr= np.array([10,20,30,40,50,70])
expanded = thirdArr [:,np.newaxis]
print(expanded)