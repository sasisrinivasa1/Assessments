def sorting():
    bfsort.sort()
    bfsort.remove('Musk Melon')
    bfsort.insert(5,'Musk Melon\n')
    return bfsort

def appending(value):
    file1 = open("OutputFile.txt","a+")
    for i in range(0,len(value)):
        file1.write(value[i])
    file1.close()

file = open("sampleFile.txt","r")
bfsort = []
for line in file:
    bfsort.append(line)
file.close()

value = sorting()
appending(value)