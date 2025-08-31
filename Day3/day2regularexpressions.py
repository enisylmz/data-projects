# Regular expressions for pattern matching 
#Using 're module'
# command files 
#re.search , re.findall,re.sub

import re

text= 'Contact me at +905366337085'
digits= re.findall(r'\d+',text)
print(digits)

#chaging digits with X
updated_text= re.sub(r'\d','X',text)
print(updated_text)

#clean texts
def cleanText(txt):
    #clean punctition
    txt= re.sub(r'[^\w\s]' , '' , txt)
    #remove the spaces
    txt= ' '.join(txt.split())
    #upper the letters
    return txt.upper()
    
input_text= 'Hello.,,, word           hi how are          you aqq               efefef!!!!'
cleanedtext= cleanText(input_text)
print(cleanedtext)
kelime='ama'
def isPalindrome(kelime):
    return kelime == kelime[::-1]

if isPalindrome(kelime):
    print(f'{kelime} is a palindrome u got it amk cocu')

else:
    print(f'{kelime} is not a palindrome')