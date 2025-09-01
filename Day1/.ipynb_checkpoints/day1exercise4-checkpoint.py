# Loops 


# (LOOP FOR) Loops through a list

fruits= ['Apple','Banana','Plum','Grape']
for fruit in fruits:
    print(fruit)
    
    
# Loops with range

for i in range(7):
    print(i)


# (While Loop) 

count = 6 

while count < 12:
    count+=1
    print(count)
    

# Break and Continue

# Break: when u wanna stop the loop when condition is meet
for i in range(10):
    if i == 5:
        break
    print(i)
    
    
# Continue: skips the current iteration and proceed the next one

for r in range(4):
    if r==2:
        continue # it mean skip 2 and conitune with the number 3 (0,1,3]
    print(r)
    
    
