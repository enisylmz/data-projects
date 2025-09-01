# Conditional Statements

#Example 1 checking a conditon 

number = 10 

if number > 11:
    print('Im bigger than everyone')

elif number == 10:
    print(' we are the same')
    
else: print('Yours is small')    

# nested conditions

age = int(input('Enter guys age: '))

if age > 18:
    if age <= 30:
        print('This guy still young')
    elif age >= 30:
        print("This guy old")
    else:
        print("This guy a baby")
        
