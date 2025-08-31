# HandsOnExercise

def add(a,b ):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b ):
    return a*b

def division(a,b ):
    return a/b

while True:
    
    print("1.Add")
    print("2.Substract")
    print("3.Exit Program")
    
    choise=input("Enter your choise: ")
    if choise=="3":
        print("Exiting program")
        break
    if choise == "1":
        a=float(input("Enter Your First Number"))
        b=float(input("Enter YOUR SECOND NUMBER"))
        print(add(a,b))
    
    if choise=="2":
        a=float(input("Enter Your First Number"))
        b=float(input("Enter YOUR SECOND NUMBER"))
        print(substract(a,b))
        
    
    


    
