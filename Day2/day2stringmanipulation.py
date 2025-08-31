#STRING MANİPULATİON

string1 = 'Hello word'
string2 = 'Im Kibariye'

print(string1 + ' ' +string2)

#split split the sentence or chracter
txt= 'Python is for fun amk'
word= txt.split()
print(word)


#join
new_txt = ''.join(word)

# strip remove the spaces
messy_text = '      Hello word amk cocu         '
good_text = messy_text.strip()
print(good_text)