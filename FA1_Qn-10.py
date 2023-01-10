import re

regex = r'[Mm]elon'
file = open("sampleFileQn10.txt","r")
for line in file:
    file1 = open("outputQn10.txt","a")
    if re.search(regex,line):
        file1.write(line)
file.close()
file1.close()