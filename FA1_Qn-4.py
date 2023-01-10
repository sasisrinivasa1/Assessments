import re
text = "Hello Gary Williams"
regexln = r'Williams$'
regexfn = r'[G](\w+)'
First_Name = re.search(regexfn,text)
Last_Name = re.search(regexln,text)
print("First_Name :",First_Name.group(0))
print("Last Name :",Last_Name.group(0))