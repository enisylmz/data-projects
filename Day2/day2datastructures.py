# Day 2 Data Structures

#Lists

numbers = [1 , 2, 3, 4, 5, 6, 7, 8]

fruits = ['apple', 'banana', 'cherry']

mixed = ['apple', 1, True]

print(numbers[0])
print(fruits[2])

fruits.append('orange')
print(fruits)
fruits.insert(3,'grape')
print(fruits)
fruits.pop() #remove the last element
print(fruits)
fruits.remove('grape')
print(fruits)
del fruits[1]
print(fruits)
fruits.append('a')
fruits.append('b')
fruits.append('c')
print(fruits)

sliced_fruits = fruits[1:4]
print(sliced_fruits)

#Tuples 
colors = {'red', 'blue', 'purple'}
single_item = {'color'}


#Dictianorys
student= { 'name':'Alice', 'age':25, 'grade': 'A'}
print(student)
print(student['age'])
student['age']= 26 
print(student)

#Sets in python 


numbers = {1, 2, 3, 4, 5}
set_empty = set()
print(numbers)
numbers.add(7)
print(numbers)

#sets cannot repeat for example there is 4 and 5 same in that two sets if i use & şt will show me common cluster 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1 & set2)
print(set1 | set2)


sentence = input('Enter a sentence')
words= sentence.split()

words = {}

print(words)