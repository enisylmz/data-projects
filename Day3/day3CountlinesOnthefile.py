
# count the list on the file

def countonTheFile(file):
    with open(file,'r') as f:
        readLines = f.readlines()
        for item in readLines:
            print(item.strip())
            
countonTheFile('metin.txt')