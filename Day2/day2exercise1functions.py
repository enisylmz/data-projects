#Day2 Functions
#Functions with parameters return values

def add_numbers(a,b):
    return a+b
result = add_numbers(5,3)
print(result)

#Local Scope 

def greeting():
    message='Hello word'
    
greeting()    
print(message) #it will be undefined coz its a local scope and it will not work out of the function

# Global Scope
message= 'Hello word canımsın'
def greeting():

    print(message + 'from inside the function')
    
greeting()    
print(message+'from outside the function')


