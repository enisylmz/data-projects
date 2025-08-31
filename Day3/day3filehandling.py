#File handling ( open file write file read file )

#open an exists file and read it
with open('metin.txt', 'r') as file:
   openFile=file.read()
   print(openFile)
   
#write on the file

with open('metin.txt','w') as dosya:
    openWfile=dosya.write('Merhaba amk cocu')
    print(openWfile)
    

# count the lines and words 

def countLines(cFile):
    with open(cFile,'r') as clsFile:
        countline=clsFile.readlines()
        lenCfile=len(countline)
        print(f'{lenCfile} is the length of the file')

countLines('metin.txt')

